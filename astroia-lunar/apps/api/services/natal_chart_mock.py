"""
Service de génération de natal charts mock complets.

Utilisé comme fallback quand RapidAPI est indisponible ou qu'un chart est incomplet.
Génère des données déterministes (basées sur hash des paramètres de naissance).
"""

import hashlib
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

# Noms des signes du zodiaque
SIGN_NAMES = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Noms des planètes (10 planètes + ascendant)
PLANET_NAMES = [
    "sun", "moon", "mercury", "venus", "mars",
    "jupiter", "saturn", "uranus", "neptune", "pluto"
]


def _deterministic_hash(birth_data: dict) -> int:
    """
    Génère un hash déterministe à partir des données de naissance.

    Args:
        birth_data: {"year", "month", "day", "hour", "minute", "latitude", "longitude"}

    Returns:
        int: Hash déterministe (pour seed de génération)
    """
    key = f"{birth_data['year']}{birth_data['month']}{birth_data['day']}"
    key += f"{birth_data['hour']}{birth_data['minute']}"
    key += f"{birth_data['latitude']:.4f}{birth_data['longitude']:.4f}"

    # SHA256 hash pour déterminisme
    hash_obj = hashlib.sha256(key.encode())
    return int.from_bytes(hash_obj.digest()[:8], 'big')


def _get_sign_from_seed(seed: int, offset: int = 0) -> str:
    """
    Retourne un signe du zodiaque de manière déterministe.

    Args:
        seed: Hash déterministe
        offset: Offset pour varier les signes

    Returns:
        str: Nom du signe (ex: "Aries", "Taurus", ...)
    """
    index = (seed + offset) % len(SIGN_NAMES)
    return SIGN_NAMES[index]


def _get_degree_from_seed(seed: int, offset: int = 0) -> float:
    """
    Retourne un degré (0-30) de manière déterministe.

    Args:
        seed: Hash déterministe
        offset: Offset pour varier les degrés

    Returns:
        float: Degré dans le signe (0.0-29.99)
    """
    # Utiliser modulo pour obtenir un degré entre 0 et 30
    degree_base = ((seed + offset * 137) % 3000) / 100.0  # 137 est un nombre premier pour distribution
    return round(min(degree_base, 29.99), 2)


def _get_house_from_seed(seed: int, offset: int = 0) -> int:
    """
    Retourne une maison (1-12) de manière déterministe.

    Args:
        seed: Hash déterministe
        offset: Offset pour varier les maisons

    Returns:
        int: Numéro de maison (1-12)
    """
    house = ((seed + offset * 73) % 12) + 1  # 73 est un nombre premier
    return house


def generate_complete_natal_mock(birth_data: dict, reason: str = "rapidapi_unavailable") -> dict:
    """
    Génère un natal chart mock complet de manière déterministe.

    AVEC MÉTADONNÉES : Inclut "_mock": true et "_reason" pour que le mobile
    puisse détecter que c'est un fallback et afficher un warning.

    Args:
        birth_data: {
            "year": int,
            "month": int,
            "day": int,
            "hour": int,
            "minute": int,
            "latitude": float,
            "longitude": float
        }
        reason: Raison du fallback mock (ex: "rapidapi_unavailable", "rapidapi_403", "rapidapi_429")

    Returns:
        dict: Structure positions JSONB complète avec :
            - sun, moon, ascendant (top-level)
            - planets (dict avec 10+ planètes)
            - houses (dict avec 12 maisons)
            - aspects (array, vide pour MVP)
            - _mock: true (métadonnée pour le mobile)
            - _reason: str (code de la raison du fallback)

    Example:
        >>> mock = generate_complete_natal_mock({
        ...     "year": 1990, "month": 5, "day": 15,
        ...     "hour": 14, "minute": 30,
        ...     "latitude": 48.8566, "longitude": 2.3522
        ... }, reason="rapidapi_403")
        >>> mock["_mock"]
        True
        >>> len(mock["planets"]) >= 10
        True
        >>> len(mock["houses"]) == 12
        True
    """
    # Générer hash déterministe
    seed = _deterministic_hash(birth_data)

    logger.info(
        f"🎭 Génération natal chart mock déterministe: "
        f"date={birth_data['year']}-{birth_data['month']:02d}-{birth_data['day']:02d} "
        f"{birth_data['hour']:02d}:{birth_data['minute']:02d}, "
        f"coords=({birth_data['latitude']:.4f}, {birth_data['longitude']:.4f})"
    )

    # === 1. GÉNÉRER BIG3 (sun, moon, ascendant) ===
    sun_sign = _get_sign_from_seed(seed, offset=0)
    sun_degree = _get_degree_from_seed(seed, offset=0)
    sun_house = _get_house_from_seed(seed, offset=0)

    moon_sign = _get_sign_from_seed(seed, offset=1)
    moon_degree = _get_degree_from_seed(seed, offset=1)
    moon_house = _get_house_from_seed(seed, offset=1)

    ascendant_sign = _get_sign_from_seed(seed, offset=2)
    ascendant_degree = _get_degree_from_seed(seed, offset=2)

    # Structure Big3 (top-level keys)
    sun_data = {
        "sign": sun_sign,
        "degree": sun_degree,
        "house": sun_house
    }

    moon_data = {
        "sign": moon_sign,
        "degree": moon_degree,
        "house": moon_house
    }

    ascendant_data = {
        "sign": ascendant_sign,
        "degree": ascendant_degree
    }

    # === 2. GÉNÉRER PLANETS DICT (10 planètes + ascendant) ===
    planets_dict = {}

    # Ajouter les 10 planètes principales
    for i, planet_name in enumerate(PLANET_NAMES):
        sign = _get_sign_from_seed(seed, offset=i + 3)
        degree = _get_degree_from_seed(seed, offset=i + 3)
        house = _get_house_from_seed(seed, offset=i + 3)

        planets_dict[planet_name] = {
            "sign": sign,
            "degree": degree,
            "house": house
        }

    # Ajouter ascendant dans planets (clé "ascendant" en minuscule pour cohérence)
    planets_dict["ascendant"] = {
        "sign": ascendant_sign,
        "degree": ascendant_degree,
        "house": 1  # Ascendant est toujours en maison 1
    }

    logger.debug(f"📊 Mock: {len(planets_dict)} planètes générées")

    # === 3. GÉNÉRER HOUSES (12 maisons) ===
    houses_dict = {}

    for house_num in range(1, 13):
        sign = _get_sign_from_seed(seed, offset=house_num + 100)
        degree = _get_degree_from_seed(seed, offset=house_num + 100)

        houses_dict[str(house_num)] = {
            "sign": sign,
            "degree": degree
        }

    logger.debug(f"🏠 Mock: {len(houses_dict)} maisons générées")

    # === 4. ASPECTS (vide pour MVP - décision utilisateur) ===
    # Le mobile accepte aspects: []
    aspects_list = []

    logger.debug(f"✨ Mock: {len(aspects_list)} aspects (vide pour MVP)")

    # === 5. ASSEMBLER POSITIONS JSONB ===
    positions = {
        "sun": sun_data,
        "moon": moon_data,
        "ascendant": ascendant_data,
        "planets": planets_dict,
        "houses": houses_dict,
        "aspects": aspects_list,
        # Métadonnées pour détection par le mobile
        "_mock": True,
        "_reason": reason
    }

    logger.info(
        f"✅ Mock généré (_mock=True, reason={reason}): "
        f"Big3={sun_sign}/{moon_sign}/{ascendant_sign}, "
        f"{len(planets_dict)} planètes, {len(houses_dict)} maisons, "
        f"{len(aspects_list)} aspects"
    )

    return positions
