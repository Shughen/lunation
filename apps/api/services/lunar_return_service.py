"""
Service de gestion des révolutions lunaires
Utilise Supabase directement via supabase-py
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from uuid import UUID

from lib.supabase_client import get_supabase_client
from services.natal_reading_service import (
    call_rapidapi_natal_chart,
    parse_positions_from_natal_chart,
    parse_aspects_from_natal_chart
)
from schemas.lunar_return import (
    LunarReturnCreate,
    LunarReturnResponse,
    UserProfileForLunarReturn
)

logger = logging.getLogger(__name__)


def calculate_lunar_return_date(birth_date: datetime, cycle_number: int) -> datetime:
    """
    Calcule la date exacte d'une révolution lunaire
    
    Une révolution lunaire = ~29.5 jours après la naissance
    Cycle 1 = première révolution après la naissance
    Cycle 2 = deuxième révolution, etc.
    
    Args:
        birth_date: Date de naissance
        cycle_number: Numéro du cycle (1, 2, 3, ...)
    
    Returns:
        Date exacte de la révolution lunaire
    """
    # Durée moyenne d'une révolution lunaire (en jours)
    LUNAR_CYCLE_DAYS = 29.53059
    
    # Calculer la date de la révolution
    days_offset = cycle_number * LUNAR_CYCLE_DAYS
    lunar_return_date = birth_date + timedelta(days=days_offset)
    
    logger.info(f"📅 Calcul révolution lunaire cycle {cycle_number}: {birth_date.date()} + {days_offset:.2f} jours = {lunar_return_date.date()}")
    
    return lunar_return_date


def calculate_lunar_return_period(lunar_return_date: datetime) -> tuple[datetime, datetime]:
    """
    Calcule la période d'une révolution lunaire (du début à la fin)
    
    Args:
        lunar_return_date: Date exacte de la révolution
    
    Returns:
        Tuple (start_date, end_date)
    """
    # La révolution lunaire dure ~29.5 jours
    # On considère qu'elle commence quelques heures avant la date exacte
    # et se termine à la prochaine révolution
    LUNAR_CYCLE_DAYS = 29.53059
    
    start_date = lunar_return_date - timedelta(hours=12)
    end_date = lunar_return_date + timedelta(days=LUNAR_CYCLE_DAYS)
    
    return (start_date, end_date)


async def calculate_planet_positions(
    date: datetime,
    latitude: float,
    longitude: float,
    timezone: str
) -> Dict[str, Any]:
    """
    Calcule les positions planétaires à une date donnée
    
    Utilise RapidAPI pour obtenir les positions exactes
    """
    logger.info(f"🌍 Calcul positions planétaires pour {date.date()}")
    
    birth_data = {
        "year": date.year,
        "month": date.month,
        "day": date.day,
        "hour": date.hour,
        "minute": date.minute,
        "second": date.second,
        "city": "Location",
        "country_code": "FR",
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
    }
    
    try:
        # Appel à RapidAPI pour obtenir les positions
        chart_response = await call_rapidapi_natal_chart(birth_data)
        positions = parse_positions_from_natal_chart(chart_response)
        
        logger.info(f"✅ {len(positions)} positions calculées")
        return {
            "positions": positions,
            "raw_response": chart_response
        }
    except Exception as e:
        logger.error(f"❌ Erreur calcul positions: {e}")
        # Retourner des positions vides en cas d'erreur
        return {
            "positions": [],
            "raw_response": {}
        }


async def calculate_aspects(planet_positions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Calcule les aspects entre les planètes
    
    Pour simplifier, on utilise les aspects déjà calculés par RapidAPI
    Si pas disponibles, on retourne une liste vide
    """
    # Les aspects sont généralement calculés en même temps que les positions
    # On les extrait du raw_response si disponible
    return []


def generate_interpretation_keys(
    moon_sign: Optional[str],
    moon_house: Optional[int],
    ascendant_sign: Optional[str],
    sun_sign: Optional[str],
    aspects: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Génère les clés d'interprétation pour la révolution lunaire
    
    Ces clés servent à générer les textes d'interprétation côté frontend
    """
    interpretation_keys = {
        "moon": {
            "sign": moon_sign,
            "house": moon_house,
            "theme": None,  # À compléter avec logique métier
        },
        "ascendant": {
            "sign": ascendant_sign,
            "theme": None,
        },
        "major_aspects_count": len([a for a in aspects if a.get("aspect_type") in ["conjunction", "opposition", "trine", "square", "sextile"]]),
        "dominant_theme": None,  # À calculer selon les positions
    }
    
    return interpretation_keys


async def calculate_lunar_return(
    user_profile: UserProfileForLunarReturn,
    cycle_number: int
) -> Dict[str, Any]:
    """
    Calcule une révolution lunaire complète
    
    Args:
        user_profile: Profil utilisateur avec données de naissance
        cycle_number: Numéro du cycle (1, 2, 3, ...)
    
    Returns:
        Dictionnaire avec toutes les données calculées de la révolution
    """
    logger.info(f"🌙 Calcul révolution lunaire cycle {cycle_number} pour utilisateur")
    
    # 1. Calculer la date exacte de la révolution
    birth_date = user_profile.birth_date
    if user_profile.birth_time:
        birth_datetime = datetime.combine(
            birth_date.date(),
            user_profile.birth_time.time() if isinstance(user_profile.birth_time, datetime) else birth_date.time()
        )
    else:
        birth_datetime = birth_date
    
    lunar_return_date = calculate_lunar_return_date(birth_datetime, cycle_number)
    start_date, end_date = calculate_lunar_return_period(lunar_return_date)
    
    # 2. Calculer les positions planétaires à la révolution
    planet_data = await calculate_planet_positions(
        lunar_return_date,
        user_profile.latitude,
        user_profile.longitude,
        user_profile.timezone
    )
    
    positions = planet_data.get("positions", [])
    raw_response = planet_data.get("raw_response", {})
    
    # 3. Extraire les données clés de la révolution
    moon_position = next((p for p in positions if p.get("name") == "Moon"), None)
    sun_position = next((p for p in positions if p.get("name") == "Sun"), None)
    ascendant = next((p for p in positions if p.get("name") == "Ascendant") or 
                     next((p for p in positions if "Asc" in p.get("name", "")), None), None)
    
    # 4. Extraire les aspects depuis la réponse RapidAPI
    aspects = parse_aspects_from_natal_chart(raw_response) if raw_response else []
    
    # 5. Générer les clés d'interprétation
    interpretation_keys = generate_interpretation_keys(
        moon_position.get("sign") if moon_position else None,
        moon_position.get("house") if moon_position else None,
        ascendant.get("sign") if ascendant else None,
        sun_position.get("sign") if sun_position else None,
        aspects
    )
    
    # 6. Construire le résultat
    result = {
        "cycle_number": cycle_number,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "moon_sign": moon_position.get("sign") if moon_position else None,
        "moon_degree": moon_position.get("degree") if moon_position else None,
        "moon_house": moon_position.get("house") if moon_position else None,
        "ascendant_sign": ascendant.get("sign") if ascendant else None,
        "ascendant_degree": ascendant.get("degree") if ascendant else None,
        "sun_sign": sun_position.get("sign") if sun_position else None,
        "sun_degree": sun_position.get("degree") if sun_position else None,
        "planet_positions": {
            "positions": positions,
            "raw_response": raw_response
        },
        "aspects": aspects,
        "interpretation_keys": interpretation_keys,
    }
    
    logger.info(f"✅ Révolution lunaire calculée: Lune {result['moon_sign']} en maison {result['moon_house']}")
    
    return result


async def create_lunar_return(user_id: UUID, computed_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Crée une révolution lunaire dans Supabase
    
    Args:
        user_id: ID de l'utilisateur
        computed_data: Données calculées de la révolution
    
    Returns:
        Données créées dans Supabase
    """
    logger.info(f"💾 Sauvegarde révolution lunaire cycle {computed_data['cycle_number']} pour user {user_id}")
    
    supabase = get_supabase_client()
    
    # Préparer les données pour Supabase
    lunar_return_data = {
        "user_id": str(user_id),
        "cycle_number": computed_data["cycle_number"],
        "start_date": computed_data["start_date"],
        "end_date": computed_data["end_date"],
        "moon_sign": computed_data.get("moon_sign"),
        "moon_degree": computed_data.get("moon_degree"),
        "moon_house": computed_data.get("moon_house"),
        "ascendant_sign": computed_data.get("ascendant_sign"),
        "ascendant_degree": computed_data.get("ascendant_degree"),
        "sun_sign": computed_data.get("sun_sign"),
        "sun_degree": computed_data.get("sun_degree"),
        "planet_positions": computed_data.get("planet_positions"),
        "aspects": computed_data.get("aspects"),
        "interpretation_keys": computed_data.get("interpretation_keys"),
    }
    
    try:
        logger.info(f"📤 Insertion dans Supabase - données: cycle={lunar_return_data['cycle_number']}, user_id={lunar_return_data['user_id']}")
        
        # Vérifier que les dates sont au bon format (ISO string)
        if isinstance(lunar_return_data.get("start_date"), datetime):
            lunar_return_data["start_date"] = lunar_return_data["start_date"].isoformat()
        if isinstance(lunar_return_data.get("end_date"), datetime):
            lunar_return_data["end_date"] = lunar_return_data["end_date"].isoformat()
        
        logger.debug(f"📤 Payload complet (après formatage dates): {lunar_return_data}")
        
        # Insérer dans Supabase
        response = supabase.table("lunar_returns").insert(lunar_return_data).execute()
        
        logger.info(f"📥 Réponse Supabase reçue, type: {type(response)}")
        logger.debug(f"📥 Réponse complète: {response}")
        
        # Vérifier s'il y a une erreur dans la réponse
        if hasattr(response, 'error') and response.error:
            error_msg = f"Erreur Supabase: {response.error}"
            logger.error(f"❌ {error_msg}")
            raise Exception(error_msg)
        
        if not response.data:
            error_msg = "Aucune donnée retournée par Supabase après insertion"
            logger.error(f"❌ {error_msg}")
            logger.error(f"   Réponse: {response}")
            raise Exception(error_msg)
        
        created = response.data[0]
        logger.info(f"✅ Révolution lunaire sauvegardée (id: {created.get('id', 'N/A')})")
        
        return created
    
    except Exception as e:
        logger.error(f"❌ Erreur sauvegarde révolution lunaire: {type(e).__name__}: {e}")
        import traceback
        logger.error(f"   Traceback: {traceback.format_exc()}")
        raise


async def list_lunar_returns(user_id: UUID, limit: int = 50) -> List[Dict[str, Any]]:
    """
    Liste les révolutions lunaires d'un utilisateur
    
    Args:
        user_id: ID de l'utilisateur
        limit: Nombre maximum de résultats
    
    Returns:
        Liste des révolutions lunaires
    """
    logger.info(f"📋 Liste révolutions lunaires pour user {user_id}")
    
    supabase = get_supabase_client()
    
    try:
        response = supabase.table("lunar_returns")\
            .select("*")\
            .eq("user_id", str(user_id))\
            .order("cycle_number", desc=False)\
            .limit(limit)\
            .execute()
        
        lunar_returns = response.data if response.data else []
        logger.info(f"✅ {len(lunar_returns)} révolutions trouvées")
        
        return lunar_returns
    
    except Exception as e:
        logger.error(f"❌ Erreur liste révolutions: {e}")
        raise


async def get_lunar_return_by_id(lunar_return_id: UUID) -> Optional[Dict[str, Any]]:
    """
    Récupère une révolution lunaire par son ID
    
    Args:
        lunar_return_id: ID de la révolution lunaire
    
    Returns:
        Données de la révolution ou None si non trouvée
    """
    logger.info(f"🔍 Récupération révolution lunaire {lunar_return_id}")
    
    supabase = get_supabase_client()
    
    try:
        response = supabase.table("lunar_returns")\
            .select("*")\
            .eq("id", str(lunar_return_id))\
            .single()\
            .execute()
        
        if not response.data:
            logger.warning(f"⚠️ Révolution lunaire {lunar_return_id} non trouvée")
            return None
        
        logger.info(f"✅ Révolution lunaire trouvée")
        return response.data
    
    except Exception as e:
        logger.error(f"❌ Erreur récupération révolution: {e}")
        return None

