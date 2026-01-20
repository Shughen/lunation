"""
Service pour les interpretations d'aspects natals
Version 2 - Interpretations pre-generees depuis DB
"""

import logging
from typing import Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

logger = logging.getLogger(__name__)

# Planetes supportees pour les aspects (ordre alphabetique)
ASPECT_PLANETS = [
    'jupiter', 'mars', 'mercury', 'moon', 'neptune',
    'pluto', 'saturn', 'sun', 'uranus', 'venus'
]

# Types d'aspects supportes
ASPECT_TYPES = ['conjunction', 'opposition', 'trine', 'square', 'sextile']

# Symboles des aspects
ASPECT_SYMBOLS = {
    'conjunction': '\u260c',  # Conjonction
    'opposition': '\u260d',   # Opposition
    'trine': '\u25b3',        # Trigone
    'square': '\u25a1',       # Carre
    'sextile': '\u26b9'       # Sextile
}

# Noms francais des aspects
ASPECT_NAMES_FR = {
    'conjunction': 'Conjonction',
    'opposition': 'Opposition',
    'trine': 'Trigone',
    'square': 'Carre',
    'sextile': 'Sextile'
}

# Noms francais des planetes
PLANET_NAMES_FR = {
    'sun': 'Soleil',
    'moon': 'Lune',
    'mercury': 'Mercure',
    'venus': 'Venus',
    'mars': 'Mars',
    'jupiter': 'Jupiter',
    'saturn': 'Saturne',
    'uranus': 'Uranus',
    'neptune': 'Neptune',
    'pluto': 'Pluton'
}


def normalize_planet_pair(p1: str, p2: str) -> Tuple[str, str]:
    """
    Ordonne une paire de planetes alphabetiquement

    Args:
        p1: Premiere planete
        p2: Deuxieme planete

    Returns:
        Tuple (planet1, planet2) ordonne alphabetiquement
    """
    p1_lower = p1.lower().strip()
    p2_lower = p2.lower().strip()

    if p1_lower < p2_lower:
        return (p1_lower, p2_lower)
    return (p2_lower, p1_lower)


async def load_pregenerated_aspect_from_db(
    db: AsyncSession,
    planet1: str,
    planet2: str,
    aspect_type: str,
    version: int = 2,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Charge une interpretation d'aspect pre-generee depuis la base de donnees

    Args:
        db: Session async SQLAlchemy
        planet1: Premiere planete (sera normalisee)
        planet2: Deuxieme planete (sera normalisee)
        aspect_type: Type d'aspect (conjunction, opposition, etc.)
        version: Version du contenu (default 2)
        lang: Langue (default 'fr')

    Returns:
        Texte markdown complet OU None si introuvable
    """
    from models.pregenerated_natal_aspect import PregeneratedNatalAspect

    # Normaliser la paire de planetes
    p1_norm, p2_norm = normalize_planet_pair(planet1, planet2)
    aspect_norm = aspect_type.lower().strip()

    try:
        result = await db.execute(
            select(PregeneratedNatalAspect).where(
                PregeneratedNatalAspect.planet1 == p1_norm,
                PregeneratedNatalAspect.planet2 == p2_norm,
                PregeneratedNatalAspect.aspect_type == aspect_norm,
                PregeneratedNatalAspect.version == version,
                PregeneratedNatalAspect.lang == lang
            )
        )
        interpretation = result.scalar_one_or_none()

        if interpretation:
            logger.info(f"Interpretation aspect chargee depuis DB: {p1_norm}-{p2_norm} {aspect_norm} ({interpretation.length} chars)")
            return interpretation.content

        logger.warning(f"Interpretation aspect introuvable en DB: {p1_norm}-{p2_norm} {aspect_norm} v{version} lang={lang}")
        return None

    except Exception as e:
        logger.error(f"Erreur chargement aspect DB: {e}")
        return None


def generate_placeholder_aspect_interpretation(
    planet1: str,
    planet2: str,
    aspect_type: str
) -> str:
    """
    Genere une interpretation placeholder quand pas de contenu pre-genere

    Args:
        planet1: Premiere planete
        planet2: Deuxieme planete
        aspect_type: Type d'aspect

    Returns:
        Texte placeholder formate en markdown
    """
    p1_norm, p2_norm = normalize_planet_pair(planet1, planet2)

    symbol = ASPECT_SYMBOLS.get(aspect_type.lower(), '')
    aspect_fr = ASPECT_NAMES_FR.get(aspect_type.lower(), aspect_type)
    planet1_fr = PLANET_NAMES_FR.get(p1_norm, p1_norm.title())
    planet2_fr = PLANET_NAMES_FR.get(p2_norm, p2_norm.title())

    placeholder = f"""# {symbol} {aspect_fr} {planet1_fr} - {planet2_fr}
**En une phrase :** Interpretation en cours de redaction.

## L'energie de cet aspect
Cet aspect entre {planet1_fr} et {planet2_fr} cree une dynamique particuliere dans votre theme natal. L'interpretation detaillee sera bientot disponible.

## Ton potentiel
Les forces et talents associes a cet aspect seront decrits prochainement.

## Ton defi
Les zones de vigilance liees a cet aspect seront expliquees dans une mise a jour future.

## Conseil pratique
Des conseils concrets pour optimiser cette configuration seront ajoutes."""

    return placeholder


async def get_aspect_interpretation(
    db: AsyncSession,
    planet1: str,
    planet2: str,
    aspect_type: str,
    version: int = 2,
    lang: str = 'fr'
) -> Tuple[str, str, str, str]:
    """
    Obtient une interpretation d'aspect (DB first, placeholder fallback)

    Args:
        db: Session async SQLAlchemy
        planet1: Premiere planete
        planet2: Deuxieme planete
        aspect_type: Type d'aspect
        version: Version du contenu
        lang: Langue

    Returns:
        Tuple (text, source, planet1_normalized, planet2_normalized)
        source = 'pregenerated' ou 'placeholder'
    """
    p1_norm, p2_norm = normalize_planet_pair(planet1, planet2)

    # Essayer de charger depuis DB
    content = await load_pregenerated_aspect_from_db(
        db=db,
        planet1=p1_norm,
        planet2=p2_norm,
        aspect_type=aspect_type,
        version=version,
        lang=lang
    )

    if content:
        return (content, 'pregenerated', p1_norm, p2_norm)

    # Fallback placeholder
    placeholder = generate_placeholder_aspect_interpretation(
        planet1=p1_norm,
        planet2=p2_norm,
        aspect_type=aspect_type
    )

    return (placeholder, 'placeholder', p1_norm, p2_norm)


def get_all_planet_pairs() -> list:
    """
    Retourne toutes les 45 paires de planetes possibles (ordre alphabetique)

    Returns:
        Liste de tuples (planet1, planet2)
    """
    pairs = []
    for i, p1 in enumerate(ASPECT_PLANETS):
        for p2 in ASPECT_PLANETS[i+1:]:
            pairs.append((p1, p2))
    return pairs
