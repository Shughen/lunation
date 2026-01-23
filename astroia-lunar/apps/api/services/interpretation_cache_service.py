"""
Service de cache optimisé pour interprétations astrologiques (DB)
- Cache en mémoire avec TTL configurable (1h pour données statiques)
- Retry logic pour requêtes DB
- Performance optimisée pour requêtes fréquentes
"""

import logging
import time
import asyncio
from typing import Dict, Any, Optional, Tuple
from functools import wraps

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)

# Configuration cache (1h = 3600s pour données statiques)
INTERPRETATION_CACHE_TTL = 3600  # 1 heure

# Configuration retry logic
MAX_DB_RETRIES = 3
BASE_DB_BACKOFF = 0.2  # secondes
MAX_DB_BACKOFF = 2.0   # secondes

# Caches globaux avec timestamp
_LUNAR_CLIMATE_CACHE: Dict[str, Any] = {
    "data": {},  # Clé: (moon_sign, version, lang) → interprétation
    "timestamp": 0,
    "ttl": INTERPRETATION_CACHE_TTL
}

_LUNAR_FOCUS_CACHE: Dict[str, Any] = {
    "data": {},  # Clé: (moon_house, version, lang) → interprétation
    "timestamp": 0,
    "ttl": INTERPRETATION_CACHE_TTL
}

_LUNAR_APPROACH_CACHE: Dict[str, Any] = {
    "data": {},  # Clé: (lunar_ascendant, version, lang) → interprétation
    "timestamp": 0,
    "ttl": INTERPRETATION_CACHE_TTL
}

_LUNAR_V2_FULL_CACHE: Dict[str, Any] = {
    "data": {},  # Clé: (moon_sign, moon_house, lunar_ascendant, version, lang) → (interpretation, weekly_advice)
    "timestamp": 0,
    "ttl": INTERPRETATION_CACHE_TTL
}

_NATAL_PREGENERATED_CACHE: Dict[str, Any] = {
    "data": {},  # Clé: (subject, sign, house, version, lang) → interprétation
    "timestamp": 0,
    "ttl": INTERPRETATION_CACHE_TTL
}


def _with_db_retry(max_retries: int = MAX_DB_RETRIES):
    """
    Décorateur pour ajouter retry logic aux requêtes DB avec exponential backoff.

    Args:
        max_retries: Nombre maximum de tentatives

    Returns:
        Décorateur pour fonction async
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)

                except SQLAlchemyError as e:
                    if attempt < max_retries - 1:
                        # Calcul du backoff avec jitter
                        backoff = min(BASE_DB_BACKOFF * (2 ** attempt), MAX_DB_BACKOFF)
                        jitter = backoff * 0.3
                        wait_time = backoff + jitter

                        logger.warning(
                            f"⚠️  DB error in {func.__name__}, "
                            f"retry {attempt + 1}/{max_retries} in {wait_time:.2f}s: {str(e)}"
                        )
                        await asyncio.sleep(wait_time)
                        continue
                    else:
                        # Dernière tentative échouée
                        logger.error(
                            f"❌ DB error in {func.__name__} after {max_retries} attempts: {str(e)}",
                            exc_info=True
                        )
                        raise

                except Exception as e:
                    # Autres erreurs non-SQL (ne pas retry)
                    logger.error(
                        f"❌ Unexpected error in {func.__name__}: {str(e)}",
                        exc_info=True
                    )
                    raise

            # Normalement inaccessible
            raise Exception(f"Unexpected retry loop exit in {func.__name__}")

        return wrapper
    return decorator


# ============================================================================
# LUNAR CLIMATE CACHE
# ============================================================================

@_with_db_retry()
async def _fetch_lunar_climate_from_db(
    db: AsyncSession,
    moon_sign: str,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Récupère le template de climat depuis la DB avec retry logic.

    Args:
        db: Session DB async
        moon_sign: Signe lunaire (Aries, Taurus, etc.)
        version: Version du prompt
        lang: Langue

    Returns:
        Texte d'interprétation ou None
    """
    from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation

    result = await db.execute(
        select(PregeneratedLunarInterpretation).where(
            PregeneratedLunarInterpretation.moon_sign == moon_sign,
            PregeneratedLunarInterpretation.moon_house == 0,
            PregeneratedLunarInterpretation.lunar_ascendant == '_climate_',
            PregeneratedLunarInterpretation.version == version,
            PregeneratedLunarInterpretation.lang == lang
        )
    )
    entry = result.scalar_one_or_none()
    return entry.interpretation_full if entry else None


async def get_lunar_climate_cached(
    db: AsyncSession,
    moon_sign: str,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Récupère le template de climat lunaire avec cache (TTL: 1h).

    Args:
        db: Session DB async
        moon_sign: Signe lunaire
        version: Version du prompt
        lang: Langue

    Returns:
        Texte d'interprétation ou None
    """
    global _LUNAR_CLIMATE_CACHE

    cache_key = (moon_sign, version, lang)
    current_time = time.time()

    # Vérifier le cache
    if (
        _LUNAR_CLIMATE_CACHE["timestamp"] > 0
        and (current_time - _LUNAR_CLIMATE_CACHE["timestamp"]) < _LUNAR_CLIMATE_CACHE["ttl"]
        and cache_key in _LUNAR_CLIMATE_CACHE["data"]
    ):
        cache_age = int(current_time - _LUNAR_CLIMATE_CACHE["timestamp"])
        logger.debug(f"[LunarClimate] ✅ Cache hit for {moon_sign} (age: {cache_age}s)")
        return _LUNAR_CLIMATE_CACHE["data"][cache_key]

    # Cache miss - fetch from DB
    logger.debug(f"[LunarClimate] 🔄 Cache miss for {moon_sign}, fetching from DB")

    try:
        interpretation = await _fetch_lunar_climate_from_db(db, moon_sign, version, lang)

        # Mettre à jour le cache
        if interpretation:
            _LUNAR_CLIMATE_CACHE["data"][cache_key] = interpretation
            _LUNAR_CLIMATE_CACHE["timestamp"] = current_time
            logger.debug(f"[LunarClimate] 💾 Cache updated for {moon_sign}")

        return interpretation

    except Exception as e:
        logger.error(f"[LunarClimate] ❌ Error fetching {moon_sign}: {str(e)}", exc_info=True)
        # Si cache existe (même expiré), le retourner en fallback
        if cache_key in _LUNAR_CLIMATE_CACHE["data"]:
            logger.warning(f"[LunarClimate] ⚠️  Returning stale cache for {moon_sign}")
            return _LUNAR_CLIMATE_CACHE["data"][cache_key]
        raise


# ============================================================================
# LUNAR FOCUS CACHE
# ============================================================================

@_with_db_retry()
async def _fetch_lunar_focus_from_db(
    db: AsyncSession,
    moon_house: int,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Récupère le template de focus depuis la DB avec retry logic.

    Args:
        db: Session DB async
        moon_house: Maison lunaire (1-12)
        version: Version du prompt
        lang: Langue

    Returns:
        Texte d'interprétation ou None
    """
    from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation

    result = await db.execute(
        select(PregeneratedLunarInterpretation).where(
            PregeneratedLunarInterpretation.moon_sign == '_focus_',
            PregeneratedLunarInterpretation.moon_house == moon_house,
            PregeneratedLunarInterpretation.lunar_ascendant == '_focus_',
            PregeneratedLunarInterpretation.version == version,
            PregeneratedLunarInterpretation.lang == lang
        )
    )
    entry = result.scalar_one_or_none()
    return entry.interpretation_full if entry else None


async def get_lunar_focus_cached(
    db: AsyncSession,
    moon_house: int,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Récupère le template de focus lunaire avec cache (TTL: 1h).

    Args:
        db: Session DB async
        moon_house: Maison lunaire (1-12)
        version: Version du prompt
        lang: Langue

    Returns:
        Texte d'interprétation ou None
    """
    global _LUNAR_FOCUS_CACHE

    cache_key = (moon_house, version, lang)
    current_time = time.time()

    # Vérifier le cache
    if (
        _LUNAR_FOCUS_CACHE["timestamp"] > 0
        and (current_time - _LUNAR_FOCUS_CACHE["timestamp"]) < _LUNAR_FOCUS_CACHE["ttl"]
        and cache_key in _LUNAR_FOCUS_CACHE["data"]
    ):
        cache_age = int(current_time - _LUNAR_FOCUS_CACHE["timestamp"])
        logger.debug(f"[LunarFocus] ✅ Cache hit for M{moon_house} (age: {cache_age}s)")
        return _LUNAR_FOCUS_CACHE["data"][cache_key]

    # Cache miss - fetch from DB
    logger.debug(f"[LunarFocus] 🔄 Cache miss for M{moon_house}, fetching from DB")

    try:
        interpretation = await _fetch_lunar_focus_from_db(db, moon_house, version, lang)

        # Mettre à jour le cache
        if interpretation:
            _LUNAR_FOCUS_CACHE["data"][cache_key] = interpretation
            _LUNAR_FOCUS_CACHE["timestamp"] = current_time
            logger.debug(f"[LunarFocus] 💾 Cache updated for M{moon_house}")

        return interpretation

    except Exception as e:
        logger.error(f"[LunarFocus] ❌ Error fetching M{moon_house}: {str(e)}", exc_info=True)
        # Si cache existe (même expiré), le retourner en fallback
        if cache_key in _LUNAR_FOCUS_CACHE["data"]:
            logger.warning(f"[LunarFocus] ⚠️  Returning stale cache for M{moon_house}")
            return _LUNAR_FOCUS_CACHE["data"][cache_key]
        raise


# ============================================================================
# LUNAR APPROACH CACHE
# ============================================================================

@_with_db_retry()
async def _fetch_lunar_approach_from_db(
    db: AsyncSession,
    lunar_ascendant: str,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Récupère le template d'approche depuis la DB avec retry logic.

    Args:
        db: Session DB async
        lunar_ascendant: Ascendant lunaire (Aries, Taurus, etc.)
        version: Version du prompt
        lang: Langue

    Returns:
        Texte d'interprétation ou None
    """
    from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation

    result = await db.execute(
        select(PregeneratedLunarInterpretation).where(
            PregeneratedLunarInterpretation.moon_sign == '_approach_',
            PregeneratedLunarInterpretation.moon_house == 0,
            PregeneratedLunarInterpretation.lunar_ascendant == lunar_ascendant,
            PregeneratedLunarInterpretation.version == version,
            PregeneratedLunarInterpretation.lang == lang
        )
    )
    entry = result.scalar_one_or_none()
    return entry.interpretation_full if entry else None


async def get_lunar_approach_cached(
    db: AsyncSession,
    lunar_ascendant: str,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Récupère le template d'approche lunaire avec cache (TTL: 1h).

    Args:
        db: Session DB async
        lunar_ascendant: Ascendant lunaire
        version: Version du prompt
        lang: Langue

    Returns:
        Texte d'interprétation ou None
    """
    global _LUNAR_APPROACH_CACHE

    cache_key = (lunar_ascendant, version, lang)
    current_time = time.time()

    # Vérifier le cache
    if (
        _LUNAR_APPROACH_CACHE["timestamp"] > 0
        and (current_time - _LUNAR_APPROACH_CACHE["timestamp"]) < _LUNAR_APPROACH_CACHE["ttl"]
        and cache_key in _LUNAR_APPROACH_CACHE["data"]
    ):
        cache_age = int(current_time - _LUNAR_APPROACH_CACHE["timestamp"])
        logger.debug(f"[LunarApproach] ✅ Cache hit for {lunar_ascendant} (age: {cache_age}s)")
        return _LUNAR_APPROACH_CACHE["data"][cache_key]

    # Cache miss - fetch from DB
    logger.debug(f"[LunarApproach] 🔄 Cache miss for {lunar_ascendant}, fetching from DB")

    try:
        interpretation = await _fetch_lunar_approach_from_db(db, lunar_ascendant, version, lang)

        # Mettre à jour le cache
        if interpretation:
            _LUNAR_APPROACH_CACHE["data"][cache_key] = interpretation
            _LUNAR_APPROACH_CACHE["timestamp"] = current_time
            logger.debug(f"[LunarApproach] 💾 Cache updated for {lunar_ascendant}")

        return interpretation

    except Exception as e:
        logger.error(f"[LunarApproach] ❌ Error fetching {lunar_ascendant}: {str(e)}", exc_info=True)
        # Si cache existe (même expiré), le retourner en fallback
        if cache_key in _LUNAR_APPROACH_CACHE["data"]:
            logger.warning(f"[LunarApproach] ⚠️  Returning stale cache for {lunar_ascendant}")
            return _LUNAR_APPROACH_CACHE["data"][cache_key]
        raise


# ============================================================================
# LUNAR V2 FULL INTERPRETATION CACHE
# ============================================================================

@_with_db_retry()
async def _fetch_lunar_v2_full_from_db(
    db: AsyncSession,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    version: int = 2,
    lang: str = 'fr'
) -> Optional[Tuple[str, Optional[Dict[str, Any]]]]:
    """
    Récupère une interprétation lunaire complète v2 depuis la DB avec retry logic.

    Args:
        db: Session DB async
        moon_sign: Signe lunaire
        moon_house: Maison lunaire (1-12)
        lunar_ascendant: Ascendant lunaire
        version: Version du prompt
        lang: Langue

    Returns:
        Tuple (interpretation_full, weekly_advice) ou None
    """
    from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation

    result = await db.execute(
        select(PregeneratedLunarInterpretation).where(
            PregeneratedLunarInterpretation.moon_sign == moon_sign,
            PregeneratedLunarInterpretation.moon_house == moon_house,
            PregeneratedLunarInterpretation.lunar_ascendant == lunar_ascendant,
            PregeneratedLunarInterpretation.version == version,
            PregeneratedLunarInterpretation.lang == lang
        )
    )
    entry = result.scalar_one_or_none()

    if entry:
        return (entry.interpretation_full, entry.weekly_advice)
    return None


async def get_lunar_v2_full_cached(
    db: AsyncSession,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    version: int = 2,
    lang: str = 'fr'
) -> Optional[Tuple[str, Optional[Dict[str, Any]]]]:
    """
    Récupère une interprétation lunaire complète v2 avec cache (TTL: 1h).

    Args:
        db: Session DB async
        moon_sign: Signe lunaire
        moon_house: Maison lunaire (1-12)
        lunar_ascendant: Ascendant lunaire
        version: Version du prompt
        lang: Langue

    Returns:
        Tuple (interpretation_full, weekly_advice) ou None
    """
    global _LUNAR_V2_FULL_CACHE

    cache_key = (moon_sign, moon_house, lunar_ascendant, version, lang)
    current_time = time.time()

    # Vérifier le cache
    if (
        _LUNAR_V2_FULL_CACHE["timestamp"] > 0
        and (current_time - _LUNAR_V2_FULL_CACHE["timestamp"]) < _LUNAR_V2_FULL_CACHE["ttl"]
        and cache_key in _LUNAR_V2_FULL_CACHE["data"]
    ):
        cache_age = int(current_time - _LUNAR_V2_FULL_CACHE["timestamp"])
        logger.debug(
            f"[LunarV2Full] ✅ Cache hit for {moon_sign}/M{moon_house}/ASC_{lunar_ascendant} (age: {cache_age}s)"
        )
        return _LUNAR_V2_FULL_CACHE["data"][cache_key]

    # Cache miss - fetch from DB
    logger.debug(
        f"[LunarV2Full] 🔄 Cache miss for {moon_sign}/M{moon_house}/ASC_{lunar_ascendant}, fetching from DB"
    )

    try:
        result = await _fetch_lunar_v2_full_from_db(
            db, moon_sign, moon_house, lunar_ascendant, version, lang
        )

        # Mettre à jour le cache
        if result:
            _LUNAR_V2_FULL_CACHE["data"][cache_key] = result
            _LUNAR_V2_FULL_CACHE["timestamp"] = current_time
            logger.debug(
                f"[LunarV2Full] 💾 Cache updated for {moon_sign}/M{moon_house}/ASC_{lunar_ascendant}"
            )

        return result

    except Exception as e:
        logger.error(
            f"[LunarV2Full] ❌ Error fetching {moon_sign}/M{moon_house}/ASC_{lunar_ascendant}: {str(e)}",
            exc_info=True
        )
        # Si cache existe (même expiré), le retourner en fallback
        if cache_key in _LUNAR_V2_FULL_CACHE["data"]:
            logger.warning(
                f"[LunarV2Full] ⚠️  Returning stale cache for {moon_sign}/M{moon_house}/ASC_{lunar_ascendant}"
            )
            return _LUNAR_V2_FULL_CACHE["data"][cache_key]
        raise


# ============================================================================
# NATAL PREGENERATED INTERPRETATION CACHE
# ============================================================================

@_with_db_retry()
async def _fetch_natal_pregenerated_from_db(
    db: AsyncSession,
    subject: str,
    sign: str,
    house: int,
    version: int = 2,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Récupère une interprétation natale pré-générée depuis la DB avec retry logic.

    Args:
        db: Session DB async
        subject: Sujet (sun, moon, etc.)
        sign: Signe (aries, taurus, etc. - en anglais normalisé)
        house: Maison (1-12)
        version: Version du prompt
        lang: Langue

    Returns:
        Texte d'interprétation ou None
    """
    from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

    result = await db.execute(
        select(PregeneratedNatalInterpretation).where(
            PregeneratedNatalInterpretation.subject == subject,
            PregeneratedNatalInterpretation.sign == sign,
            PregeneratedNatalInterpretation.house == house,
            PregeneratedNatalInterpretation.version == version,
            PregeneratedNatalInterpretation.lang == lang
        )
    )
    entry = result.scalar_one_or_none()
    return entry.content if entry else None


async def get_natal_pregenerated_cached(
    db: AsyncSession,
    subject: str,
    sign: str,
    house: int,
    version: int = 2,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Récupère une interprétation natale pré-générée avec cache (TTL: 1h).

    Args:
        db: Session DB async
        subject: Sujet (sun, moon, etc.)
        sign: Signe (aries, taurus, etc. - en anglais normalisé)
        house: Maison (1-12)
        version: Version du prompt
        lang: Langue

    Returns:
        Texte d'interprétation ou None
    """
    global _NATAL_PREGENERATED_CACHE

    cache_key = (subject, sign, house, version, lang)
    current_time = time.time()

    # Vérifier le cache
    if (
        _NATAL_PREGENERATED_CACHE["timestamp"] > 0
        and (current_time - _NATAL_PREGENERATED_CACHE["timestamp"]) < _NATAL_PREGENERATED_CACHE["ttl"]
        and cache_key in _NATAL_PREGENERATED_CACHE["data"]
    ):
        cache_age = int(current_time - _NATAL_PREGENERATED_CACHE["timestamp"])
        logger.debug(f"[NatalPregenerated] ✅ Cache hit for {subject}/{sign}/M{house} (age: {cache_age}s)")
        return _NATAL_PREGENERATED_CACHE["data"][cache_key]

    # Cache miss - fetch from DB
    logger.debug(f"[NatalPregenerated] 🔄 Cache miss for {subject}/{sign}/M{house}, fetching from DB")

    try:
        interpretation = await _fetch_natal_pregenerated_from_db(
            db, subject, sign, house, version, lang
        )

        # Mettre à jour le cache
        if interpretation:
            _NATAL_PREGENERATED_CACHE["data"][cache_key] = interpretation
            _NATAL_PREGENERATED_CACHE["timestamp"] = current_time
            logger.debug(f"[NatalPregenerated] 💾 Cache updated for {subject}/{sign}/M{house}")

        return interpretation

    except Exception as e:
        logger.error(
            f"[NatalPregenerated] ❌ Error fetching {subject}/{sign}/M{house}: {str(e)}",
            exc_info=True
        )
        # Si cache existe (même expiré), le retourner en fallback
        if cache_key in _NATAL_PREGENERATED_CACHE["data"]:
            logger.warning(
                f"[NatalPregenerated] ⚠️  Returning stale cache for {subject}/{sign}/M{house}"
            )
            return _NATAL_PREGENERATED_CACHE["data"][cache_key]
        raise


# ============================================================================
# CACHE MANAGEMENT
# ============================================================================

def clear_cache():
    """Invalide tous les caches d'interprétation (utile pour tests ou mise à jour DB)"""
    global _LUNAR_CLIMATE_CACHE, _LUNAR_FOCUS_CACHE, _LUNAR_APPROACH_CACHE
    global _LUNAR_V2_FULL_CACHE, _NATAL_PREGENERATED_CACHE

    _LUNAR_CLIMATE_CACHE["data"] = {}
    _LUNAR_CLIMATE_CACHE["timestamp"] = 0

    _LUNAR_FOCUS_CACHE["data"] = {}
    _LUNAR_FOCUS_CACHE["timestamp"] = 0

    _LUNAR_APPROACH_CACHE["data"] = {}
    _LUNAR_APPROACH_CACHE["timestamp"] = 0

    _LUNAR_V2_FULL_CACHE["data"] = {}
    _LUNAR_V2_FULL_CACHE["timestamp"] = 0

    _NATAL_PREGENERATED_CACHE["data"] = {}
    _NATAL_PREGENERATED_CACHE["timestamp"] = 0

    logger.info("[InterpretationCache] 🗑️  All caches cleared")


def get_cache_stats() -> Dict[str, Any]:
    """
    Retourne les statistiques des caches d'interprétation (pour monitoring).

    Returns:
        {
            "lunar_climate": {"size": int, "age_seconds": int, "ttl": int},
            "lunar_focus": {...},
            "lunar_approach": {...},
            "lunar_v2_full": {...},
            "natal_pregenerated": {...}
        }
    """
    current_time = time.time()

    return {
        "lunar_climate": {
            "size": len(_LUNAR_CLIMATE_CACHE["data"]),
            "age_seconds": int(current_time - _LUNAR_CLIMATE_CACHE["timestamp"])
                if _LUNAR_CLIMATE_CACHE["timestamp"] > 0 else None,
            "ttl": _LUNAR_CLIMATE_CACHE["ttl"]
        },
        "lunar_focus": {
            "size": len(_LUNAR_FOCUS_CACHE["data"]),
            "age_seconds": int(current_time - _LUNAR_FOCUS_CACHE["timestamp"])
                if _LUNAR_FOCUS_CACHE["timestamp"] > 0 else None,
            "ttl": _LUNAR_FOCUS_CACHE["ttl"]
        },
        "lunar_approach": {
            "size": len(_LUNAR_APPROACH_CACHE["data"]),
            "age_seconds": int(current_time - _LUNAR_APPROACH_CACHE["timestamp"])
                if _LUNAR_APPROACH_CACHE["timestamp"] > 0 else None,
            "ttl": _LUNAR_APPROACH_CACHE["ttl"]
        },
        "lunar_v2_full": {
            "size": len(_LUNAR_V2_FULL_CACHE["data"]),
            "age_seconds": int(current_time - _LUNAR_V2_FULL_CACHE["timestamp"])
                if _LUNAR_V2_FULL_CACHE["timestamp"] > 0 else None,
            "ttl": _LUNAR_V2_FULL_CACHE["ttl"]
        },
        "natal_pregenerated": {
            "size": len(_NATAL_PREGENERATED_CACHE["data"]),
            "age_seconds": int(current_time - _NATAL_PREGENERATED_CACHE["timestamp"])
                if _NATAL_PREGENERATED_CACHE["timestamp"] > 0 else None,
            "ttl": _NATAL_PREGENERATED_CACHE["ttl"]
        }
    }
