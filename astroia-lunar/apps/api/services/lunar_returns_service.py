"""
Service de génération des révolutions lunaires.

Centralise la logique de génération des révolutions lunaires pour réutilisation
dans les routes API et le cron job mensuel.
"""

import logging
import time
import uuid
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, func
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from models.natal_chart import NatalChart
from models.user import User
from models.lunar_return import LunarReturn
from services.swiss_ephemeris import find_lunar_return, SWISS_EPHEMERIS_AVAILABLE
from services.ephemeris import ephemeris_client, EphemerisAPIKeyError
from services.interpretations import generate_lunar_return_interpretation
from utils.natal_chart_helpers import extract_moon_data_from_positions

logger = logging.getLogger(__name__)


# === CONSTANTES ===
SIGN_TO_LONGITUDE_OFFSET = {
    'Aries': 0, 'Taurus': 30, 'Gemini': 60, 'Cancer': 90,
    'Leo': 120, 'Virgo': 150, 'Libra': 180, 'Scorpio': 210,
    'Sagittarius': 240, 'Capricorn': 270, 'Aquarius': 300, 'Pisces': 330,
    # Variantes françaises
    'Bélier': 0, 'Taureau': 30, 'Gémeaux': 60, 'Lion': 120,
    'Vierge': 150, 'Balance': 180, 'Verseau': 300, 'Poissons': 330,
}


# === HELPERS ===
def _extract_result_rowcount(result):
    """
    Extrait le rowcount d'un résultat de manière robuste.
    Compatible avec SQLAlchemy AsyncResult et FakeResult de tests.

    Args:
        result: Résultat de db.execute() (AsyncResult ou FakeResult)

    Returns:
        Nombre de lignes affectées, ou None si non disponible
    """
    if hasattr(result, 'rowcount'):
        return result.rowcount
    return None


def _sign_degree_to_longitude(sign: str, degree: float) -> float:
    """
    Convertit un signe zodiacal + degré dans le signe en longitude écliptique absolue (0-360).

    Args:
        sign: Signe zodiacal (ex: 'Aries', 'Taurus', 'Bélier', etc.)
        degree: Degré dans le signe (0-30)

    Returns:
        Longitude écliptique absolue (0-360)

    Raises:
        ValueError: Si le signe n'est pas reconnu
    """
    # Normaliser le signe (première lettre majuscule)
    sign_normalized = sign.strip().title()

    if sign_normalized not in SIGN_TO_LONGITUDE_OFFSET:
        raise ValueError(f"Signe zodiacal non reconnu: {sign}")

    offset = SIGN_TO_LONGITUDE_OFFSET[sign_normalized]
    return (offset + degree) % 360


def _parse_return_date(raw_data: Dict[str, Any], month: str, correlation_id: str) -> datetime:
    """
    Parse return_date depuis raw_data avec fallback garanti non-null.

    Args:
        raw_data: Données brutes d'Ephemeris
        month: Mois au format YYYY-MM
        correlation_id: ID de corrélation pour les logs

    Returns:
        datetime UTC timezone-aware (jamais None)
    """
    return_date = None

    # Parser depuis return_datetime si disponible
    if "return_datetime" in raw_data:
        try:
            return_datetime_str = str(raw_data["return_datetime"])
            if return_datetime_str.endswith("Z"):
                return_datetime_str = return_datetime_str[:-1]
                if "+" not in return_datetime_str and "-" not in return_datetime_str[-6:]:
                    return_datetime_str = return_datetime_str + "+00:00"
            elif "+" not in return_datetime_str and "-" not in return_datetime_str[-6:]:
                return_datetime_str = return_datetime_str + "+00:00"
            return_date = datetime.fromisoformat(return_datetime_str)
        except (ValueError, AttributeError, TypeError) as e:
            logger.debug(
                f"[corr={correlation_id}] ⚠️ Impossible de parser return_datetime '{raw_data.get('return_datetime')}': {e}"
            )

    # Fallback MVP : 15 du mois à 12:00 UTC
    if return_date is None:
        try:
            year, month_num = map(int, month.split('-'))
            return_date = datetime(year, month_num, 15, 12, 0, 0, tzinfo=timezone.utc)
            logger.info(
                f"[corr={correlation_id}] ℹ️ Fallback return_date pour {month}: 15 du mois à 12:00 UTC"
            )
        except (ValueError, AttributeError) as fallback_error:
            logger.warning(
                f"[corr={correlation_id}] ⚠️ Impossible de créer fallback return_date pour {month}: {fallback_error}"
            )
            # Dernier recours : utiliser maintenant
            return_date = datetime.now(timezone.utc)

    return return_date


def _compute_rolling_months(now_utc: datetime) -> List[str]:
    """
    Calcule la liste des 12 prochains mois rolling à partir de now_utc.

    Toujours commencer au mois courant car on calcule maintenant la vraie date
    de révolution lunaire (qui peut être n'importe quand dans le mois).

    Args:
        now_utc: Datetime UTC actuel

    Returns:
        Liste de 12 mois au format YYYY-MM
    """
    # Toujours commencer au mois courant
    start_year = now_utc.year
    start_month = now_utc.month

    months = []
    current_year = start_year
    current_month = start_month
    for i in range(12):
        month_str = f"{current_year}-{str(current_month).zfill(2)}"
        months.append(month_str)
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1

    return months


async def _generate_rolling_returns(
    db: AsyncSession,
    user_id: int,
    correlation_id: str,
    months: List[str],
    natal_moon_degree: float,
    natal_moon_sign: str,
    birth_latitude: float,
    birth_longitude: float,
    birth_timezone: str,
    delete_existing: bool = False
) -> int:
    """
    Service centralisé pour générer les révolutions lunaires rolling.

    Args:
        db: Session DB
        user_id: ID utilisateur (primitif int pour éviter MissingGreenlet)
        correlation_id: ID de corrélation pour les logs
        months: Liste des mois à générer (format YYYY-MM)
        natal_moon_degree: Degré de la Lune natale
        natal_moon_sign: Signe de la Lune natale
        birth_latitude: Latitude de naissance
        birth_longitude: Longitude de naissance
        birth_timezone: Timezone de naissance
        delete_existing: Si True, supprime tous les retours existants avant génération

    Returns:
        Nombre de retours générés avec succès
    """
    if delete_existing:
        try:
            delete_stmt = delete(LunarReturn).where(
                LunarReturn.user_id == user_id
            )
            delete_result = await db.execute(delete_stmt)
            deleted_count = _extract_result_rowcount(delete_result)
            if deleted_count is not None:
                logger.info(
                    f"[corr={correlation_id}] 🗑️  Suppression de toutes les révolutions lunaires existantes: "
                    f"{deleted_count} retour(s) supprimé(s)"
                )
        except Exception as delete_error:
            logger.warning(
                f"[corr={correlation_id}] ⚠️ Erreur lors de la suppression des retours existants: {delete_error}"
            )
            await db.rollback()

    generated_count = 0

    # Calculer la longitude écliptique absolue de la Lune natale (0-360°)
    try:
        natal_moon_longitude = _sign_degree_to_longitude(natal_moon_sign, natal_moon_degree)
        logger.info(
            f"[corr={correlation_id}] 🌙 Lune natale: {natal_moon_sign} {natal_moon_degree:.2f}° "
            f"→ longitude absolue {natal_moon_longitude:.2f}°"
        )
    except ValueError as e:
        logger.error(f"[corr={correlation_id}] ❌ Erreur conversion signe→longitude: {e}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "detail": f"Signe lunaire invalide: {natal_moon_sign}",
                "correlation_id": correlation_id,
                "step": "sign_to_longitude",
            }
        )

    for month in months:
        try:
            logger.debug(
                f"[corr={correlation_id}] 🔄 Calcul révolution lunaire {month}..."
            )

            # === ÉTAPE 1: Calculer la vraie date de révolution lunaire avec Swiss Ephemeris ===
            year, month_num = map(int, month.split('-'))
            # Point de départ: milieu du mois (approximation initiale)
            search_start = datetime(year, month_num, 15, 12, 0, 0, tzinfo=timezone.utc)

            return_date = None
            if SWISS_EPHEMERIS_AVAILABLE:
                # Rechercher la révolution lunaire dans une fenêtre de ±15 jours (couvre tout le mois)
                return_date = find_lunar_return(
                    natal_moon_longitude=natal_moon_longitude,
                    start_dt=search_start - timedelta(days=15),  # Début du mois
                    search_window_hours=31 * 24,  # Fenêtre de 31 jours pour couvrir le mois entier
                    tolerance_seconds=60
                )

                if return_date:
                    # Vérifier que la date trouvée est bien dans le mois cible
                    if return_date.month == month_num and return_date.year == year:
                        logger.info(
                            f"[corr={correlation_id}] ✅ Révolution lunaire {month} trouvée: "
                            f"{return_date.strftime('%Y-%m-%d %H:%M:%S')} UTC"
                        )
                    else:
                        # La révolution n'est pas dans ce mois, chercher le mois suivant
                        logger.debug(
                            f"[corr={correlation_id}] ℹ️ Révolution lunaire trouvée {return_date.strftime('%Y-%m-%d')} "
                            f"n'est pas dans {month}, on la garde quand même"
                        )
                else:
                    logger.warning(
                        f"[corr={correlation_id}] ⚠️ Swiss Ephemeris: aucune révolution trouvée pour {month}, "
                        f"fallback sur API Ephemeris"
                    )
            else:
                logger.debug(
                    f"[corr={correlation_id}] ℹ️ Swiss Ephemeris non disponible, utilisation API Ephemeris"
                )

            # === ÉTAPE 2: Appeler l'API Ephemeris pour les données du thème (ascendant, maisons, aspects) ===
            raw_data = {}
            try:
                raw_data = await ephemeris_client.calculate_lunar_return(
                    natal_moon_degree=natal_moon_degree,
                    natal_moon_sign=natal_moon_sign,
                    target_month=month,
                    birth_latitude=birth_latitude,
                    birth_longitude=birth_longitude,
                    timezone=birth_timezone,
                )
            except EphemerisAPIKeyError as e:
                logger.warning(
                    f"[corr={correlation_id}] ⚠️ Clé API Ephemeris manquante: {e}, "
                    f"utilisation des données par défaut"
                )
                # Continuer avec raw_data vide, on a quand même la return_date de Swiss Ephemeris
            except Exception as e:
                logger.warning(
                    f"[corr={correlation_id}] ⚠️ Erreur API Ephemeris pour {month}: {e}, "
                    f"utilisation des données par défaut"
                )
                # Continuer avec raw_data vide

            # === ÉTAPE 3: Si pas de return_date Swiss Ephemeris, utiliser celle de l'API ou fallback ===
            if return_date is None:
                return_date = _parse_return_date(raw_data, month, correlation_id)

        except Exception as e:
            logger.warning(
                f"[corr={correlation_id}] ⚠️ Erreur calcul révolution lunaire {month}: {e}, continue"
            )
            continue

        # Parser les données du thème
        lunar_ascendant = raw_data.get("ascendant", {}).get("sign", "Unknown")
        moon_house = raw_data.get("moon", {}).get("house", 1)
        moon_sign = raw_data.get("moon", {}).get("sign", natal_moon_sign)
        aspects = raw_data.get("aspects", [])

        # Générer l'interprétation
        interpretation = generate_lunar_return_interpretation(
            lunar_ascendant=lunar_ascendant,
            moon_house=moon_house,
            aspects=aspects,
        )

        # Protection contre génération concurrente:
        # Vérifier d'abord si l'entrée existe déjà (évite calcul inutile si doublon)
        check_result = await db.execute(
            select(LunarReturn).where(
                LunarReturn.user_id == user_id,
                LunarReturn.month == month
            )
        )
        existing = check_result.scalar_one_or_none()

        if existing:
            logger.debug(
                f"[corr={correlation_id}] ℹ️ {month} existe déjà (id={existing.id}), skip génération"
            )
            generated_count += 1
            continue

        # Créer l'entrée
        lunar_return = LunarReturn(
            user_id=user_id,
            month=month,
            return_date=return_date,
            lunar_ascendant=lunar_ascendant,
            moon_house=moon_house,
            moon_sign=moon_sign,
            aspects=aspects,
            planets=raw_data.get("planets", {}),
            houses=raw_data.get("houses", {}),
            interpretation=interpretation,
            raw_data=raw_data,
        )

        # Protection contre génération concurrente au niveau DB:
        # Utiliser un savepoint pour isoler chaque insertion et gérer les conflits individuellement
        # Si un autre process a déjà inséré ce (user_id, month) entre le SELECT et l'INSERT,
        # IntegrityError sera levée et on récupère l'entrée existante
        savepoint = await db.begin_nested()  # Savepoint pour rollback individuel
        try:
            db.add(lunar_return)
            await db.flush()  # Tenter l'insertion (sans commit global)
            await savepoint.commit()  # Commit du savepoint (insertion réussie)
            generated_count += 1
            logger.debug(
                f"[corr={correlation_id}] ✅ Insertion réussie pour {month}"
            )
        except IntegrityError:
            # Conflit: un autre process a inséré ce (user_id, month) entre le SELECT et l'INSERT
            await savepoint.rollback()
            logger.debug(
                f"[corr={correlation_id}] ℹ️ Conflit détecté pour {month} (inséré entre-temps), "
                f"récupération de l'entrée existante..."
            )

            # Refaire un SELECT pour récupérer l'entrée existante
            result = await db.execute(
                select(LunarReturn).where(
                    LunarReturn.user_id == user_id,
                    LunarReturn.month == month
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                logger.debug(
                    f"[corr={correlation_id}] ✅ Entrée existante récupérée pour {month} (id={existing.id})"
                )
                generated_count += 1
            else:
                # Cas rare: conflit mais entrée non trouvée (peut arriver en cas de rollback concurrent)
                logger.warning(
                    f"[corr={correlation_id}] ⚠️ Conflit pour {month} mais entrée non trouvée après SELECT"
                )

    return generated_count


# === FONCTIONS PUBLIQUES ===
async def generate_lunar_returns_for_user(
    user_id: int,
    db: AsyncSession,
    force_regenerate: bool = False
) -> dict:
    """
    Génère 12 mois glissants de lunar returns pour un utilisateur.

    Args:
        user_id: ID utilisateur
        db: Session DB
        force_regenerate: Si True, supprime existants avant

    Returns:
        {
            "success": True,
            "generated_count": 12,
            "user_id": 1,
            "duration_seconds": 2.5
        }

    Raises:
        HTTPException: 404 si natal_chart manquant
    """
    start_time = time.time()
    correlation_id = str(uuid.uuid4())

    logger.info(f"[corr={correlation_id}] 🌙 Génération lunar returns pour user_id={user_id}")

    # 1. Fetch natal_chart
    stmt = select(NatalChart).where(NatalChart.user_id == user_id)
    result = await db.execute(stmt)
    natal_chart = result.scalar_one_or_none()

    if not natal_chart:
        raise HTTPException(
            status_code=404,
            detail="Natal chart non trouvé"
        )

    # 2. Extraire données Lune natale
    # Fallback vers raw_data si positions est NULL (pour compatibilité avec anciens enregistrements)
    positions = natal_chart.positions
    if not positions and hasattr(natal_chart, 'raw_data') and natal_chart.raw_data:
        positions = natal_chart.raw_data
    positions = positions or {}

    moon_data_extracted = extract_moon_data_from_positions(positions)
    natal_moon_degree = moon_data_extracted.get("degree", 0)
    natal_moon_sign = moon_data_extracted.get("sign")

    if not natal_moon_sign:
        raise HTTPException(
            status_code=422,
            detail="Données de la Lune manquantes dans le thème natal"
        )

    # 3. Extraire coordonnées de naissance
    birth_latitude = None
    birth_longitude = None
    birth_timezone = None

    if natal_chart.latitude is not None:
        try:
            birth_latitude = float(natal_chart.latitude)
        except (ValueError, TypeError):
            logger.warning(
                f"[corr={correlation_id}] ⚠️ latitude invalide: {natal_chart.latitude}"
            )

    if natal_chart.longitude is not None:
        try:
            birth_longitude = float(natal_chart.longitude)
        except (ValueError, TypeError):
            logger.warning(
                f"[corr={correlation_id}] ⚠️ longitude invalide: {natal_chart.longitude}"
            )

    if natal_chart.timezone:
        birth_timezone = str(natal_chart.timezone)

    if birth_latitude is None or birth_longitude is None or not birth_timezone:
        raise HTTPException(
            status_code=422,
            detail="Coordonnées de naissance manquantes dans le thème natal"
        )

    # 4. Calculer 12 mois rolling
    now_utc = datetime.now(timezone.utc)
    months = _compute_rolling_months(now_utc)

    # 5. Générer via fonction interne
    generated_count = await _generate_rolling_returns(
        db=db,
        user_id=user_id,
        correlation_id=correlation_id,
        months=months,
        natal_moon_degree=natal_moon_degree,
        natal_moon_sign=natal_moon_sign,
        birth_latitude=birth_latitude,
        birth_longitude=birth_longitude,
        birth_timezone=birth_timezone,
        delete_existing=force_regenerate
    )

    duration = time.time() - start_time

    logger.info(
        f"[corr={correlation_id}] ✅ {generated_count} lunar returns générés "
        f"pour user_id={user_id} en {duration:.1f}s"
    )

    return {
        "success": True,
        "generated_count": generated_count,
        "user_id": user_id,
        "duration_seconds": round(duration, 2)
    }


async def refresh_all_lunar_returns(db: AsyncSession) -> dict:
    """
    Régénère lunar returns pour tous les users actifs.
    Appelé par cron job mensuel.

    Returns:
        {
            "total_users": 100,
            "successful": 95,
            "failed": 5,
            "duration_seconds": 120.5,
            "errors": [{"user_id": 5, "error": "..."}]
        }
    """
    start_time = time.time()
    logger.info("🔄 [REFRESH_ALL] Démarrage rafraîchissement global lunar returns...")

    # 1. Récupérer tous users avec natal_chart
    stmt = select(User).join(NatalChart).where(NatalChart.id.isnot(None))
    result = await db.execute(stmt)
    users = result.scalars().all()

    total_users = len(users)
    successful = 0
    failed = 0
    errors = []

    # 2. Parcourir chaque user
    for user in users:
        try:
            await generate_lunar_returns_for_user(
                user_id=user.id,
                db=db,
                force_regenerate=True
            )
            successful += 1

        except Exception as e:
            failed += 1
            error_msg = str(e)
            logger.error(
                f"❌ [REFRESH_ALL] Échec génération pour user_id={user.id}: {error_msg}",
                exc_info=True
            )
            errors.append({"user_id": user.id, "error": error_msg})

    duration = time.time() - start_time

    logger.info(
        f"✅ [REFRESH_ALL] Terminé - "
        f"total={total_users}, success={successful}, failed={failed}, "
        f"duration={duration:.1f}s"
    )

    return {
        "total_users": total_users,
        "successful": successful,
        "failed": failed,
        "duration_seconds": round(duration, 2),
        "errors": errors
    }


async def refresh_lunar_returns_batch(
    db: AsyncSession,
    window_start_days: int = 7,
    window_end_days: int = 14
) -> dict:
    """
    Rafraîchit lunar returns pour les users dans une fenêtre temporelle.

    Cible : Users dont la prochaine révolution lunaire tombe entre
    [NOW + window_start_days, NOW + window_end_days].

    Utilisé par cron quotidien pour distribuer la charge.

    Args:
        db: Session AsyncSession
        window_start_days: Début de la fenêtre (ex: 7 jours)
        window_end_days: Fin de la fenêtre (ex: 14 jours)

    Returns:
        {
            "total_users": 10,
            "successful": 9,
            "failed": 1,
            "duration_seconds": 45.2,
            "errors": [{"user_id": 5, "error": "..."}],
            "window": {"start": "2026-02-01", "end": "2026-02-08"}
        }
    """
    start_time = time.time()
    now_utc = datetime.now(timezone.utc)

    # Calculer fenêtre
    window_start = now_utc + timedelta(days=window_start_days)
    window_end = now_utc + timedelta(days=window_end_days)

    logger.info(
        f"🔄 [REFRESH_BATCH] Démarrage refresh batch - "
        f"fenêtre: {window_start.date()} → {window_end.date()}"
    )

    # === REQUÊTE SQL : Identifier users concernés ===
    # Stratégie : Récupérer users dont le MIN(return_date) futur tombe dans la fenêtre
    #
    # Logique :
    # 1. Pour chaque user, trouver la prochaine révolution lunaire (return_date > NOW())
    # 2. Si cette date tombe entre [window_start, window_end] → inclure user
    # 3. Cela garantit qu'on rafraîchit avant que les données deviennent obsolètes

    from sqlalchemy import and_

    # Subquery : Prochaine révolution lunaire par user
    subq = (
        select(
            LunarReturn.user_id,
            func.min(LunarReturn.return_date).label('next_return_date')
        )
        .where(LunarReturn.return_date > now_utc)
        .group_by(LunarReturn.user_id)
        .subquery()
    )

    # Main query : Users dans la fenêtre
    stmt = (
        select(User)
        .join(NatalChart, NatalChart.user_id == User.id)
        .join(subq, subq.c.user_id == User.id)
        .where(
            and_(
                subq.c.next_return_date >= window_start,
                subq.c.next_return_date <= window_end
            )
        )
    )

    result = await db.execute(stmt)
    users = result.scalars().all()

    total_users = len(users)
    successful = 0
    failed = 0
    errors = []

    logger.info(f"🎯 [REFRESH_BATCH] {total_users} users identifiés dans la fenêtre")

    # === Parcourir chaque user ===
    for user in users:
        try:
            await generate_lunar_returns_for_user(
                user_id=user.id,
                db=db,
                force_regenerate=True
            )
            successful += 1

        except Exception as e:
            failed += 1
            error_msg = str(e)
            logger.error(
                f"❌ [REFRESH_BATCH] Échec génération pour user_id={user.id}: {error_msg}",
                exc_info=True
            )
            errors.append({"user_id": user.id, "error": error_msg})

    duration = time.time() - start_time

    logger.info(
        f"✅ [REFRESH_BATCH] Terminé - "
        f"total={total_users}, success={successful}, failed={failed}, "
        f"duration={duration:.1f}s"
    )

    return {
        "total_users": total_users,
        "successful": successful,
        "failed": failed,
        "duration_seconds": round(duration, 2),
        "errors": errors,
        "window": {
            "start": window_start.date().isoformat(),
            "end": window_end.date().isoformat()
        }
    }
