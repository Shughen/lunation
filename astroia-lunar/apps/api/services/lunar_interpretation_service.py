"""
Service pour charger les interprétations lunaires pré-générées

Architecture par couches :
- lunar_climate : Tonalité émotionnelle par signe lunaire (12)
- lunar_focus : Domaine de vie par maison (12)
- lunar_approach : Approche par ascendant lunaire (12)

Total : 36 templates combinés dynamiquement
"""

import logging
from typing import Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

logger = logging.getLogger(__name__)


# === CHARGEMENT DEPUIS LA BASE ===

async def load_lunar_climate(
    db: AsyncSession,
    moon_sign: str,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Charge le template de climat pour un signe lunaire (avec cache)

    Convention DB:
    - moon_sign = le signe (Aries, Taurus, etc.)
    - moon_house = 0 (marqueur climat)
    - lunar_ascendant = '_climate_' (marqueur)
    """
    from services.interpretation_cache_service import get_lunar_climate_cached

    try:
        interpretation = await get_lunar_climate_cached(db, moon_sign, version, lang)

        if interpretation:
            logger.debug(f"✅ Loaded lunar_climate/{moon_sign}")
            return interpretation

        logger.warning(f"⚠️ lunar_climate/{moon_sign} not found in DB")
        return None

    except Exception as e:
        logger.error(f"❌ Error loading lunar_climate: {e}")
        return None


async def load_lunar_focus(
    db: AsyncSession,
    moon_house: int,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Charge le template de focus pour une maison (avec cache)

    Convention DB:
    - moon_sign = '_focus_' (marqueur)
    - moon_house = la maison (1-12)
    - lunar_ascendant = '_focus_' (marqueur)
    """
    from services.interpretation_cache_service import get_lunar_focus_cached

    try:
        interpretation = await get_lunar_focus_cached(db, moon_house, version, lang)

        if interpretation:
            logger.debug(f"✅ Loaded lunar_focus/M{moon_house}")
            return interpretation

        logger.warning(f"⚠️ lunar_focus/M{moon_house} not found in DB")
        return None

    except Exception as e:
        logger.error(f"❌ Error loading lunar_focus: {e}")
        return None


async def load_lunar_approach(
    db: AsyncSession,
    lunar_ascendant: str,
    version: int = 1,
    lang: str = 'fr'
) -> Optional[str]:
    """
    Charge le template d'approche pour un ascendant (avec cache)

    Convention DB:
    - moon_sign = '_approach_' (marqueur)
    - moon_house = 0
    - lunar_ascendant = l'ascendant (Aries, Taurus, etc.)
    """
    from services.interpretation_cache_service import get_lunar_approach_cached

    try:
        interpretation = await get_lunar_approach_cached(db, lunar_ascendant, version, lang)

        if interpretation:
            logger.debug(f"✅ Loaded lunar_approach/{lunar_ascendant}")
            return interpretation

        logger.warning(f"⚠️ lunar_approach/{lunar_ascendant} not found in DB")
        return None

    except Exception as e:
        logger.error(f"❌ Error loading lunar_approach: {e}")
        return None


async def load_lunar_interpretation_layers(
    db: AsyncSession,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    version: int = 1,
    lang: str = 'fr'
) -> Dict[str, Optional[str]]:
    """
    Charge les 3 couches d'interprétation lunaire

    Returns:
        {
            'climate': str | None,
            'focus': str | None,
            'approach': str | None
        }
    """
    climate = await load_lunar_climate(db, moon_sign, version, lang)
    focus = await load_lunar_focus(db, moon_house, version, lang)
    approach = await load_lunar_approach(db, lunar_ascendant, version, lang)

    return {
        'climate': climate,
        'focus': focus,
        'approach': approach
    }


# === TEMPLATES FALLBACK (si pas en base) ===

FALLBACK_CLIMATE = {
    'Aries': "Mois dynamique et impulsif. Besoin d'action, d'initiative, d'affirmation.",
    'Taurus': "Mois stable et ancré. Besoin de sécurité, de confort, de construction.",
    'Gemini': "Mois communicatif et curieux. Besoin d'échanges, d'apprentissages, de variété.",
    'Cancer': "Mois émotionnel et protecteur. Besoin de sécurité affective, de foyer.",
    'Leo': "Mois créatif et rayonnant. Besoin d'expression personnelle, de reconnaissance.",
    'Virgo': "Mois organisé et analytique. Besoin d'ordre, de service, de perfectionnement.",
    'Libra': "Mois relationnel et harmonieux. Besoin d'équilibre, de partenariats, d'esthétique.",
    'Scorpio': "Mois intense et transformateur. Besoin de profondeur, de vérité, de régénération.",
    'Sagittarius': "Mois expansif et optimiste. Besoin d'aventure, de sens, de liberté.",
    'Capricorn': "Mois structuré et ambitieux. Besoin d'accomplissement, de discipline, de responsabilité.",
    'Aquarius': "Mois innovant et collectif. Besoin de liberté, d'originalité, de projets de groupe.",
    'Pisces': "Mois fluide et empathique. Besoin de dissolution, de spiritualité, de compassion."
}

FALLBACK_FOCUS = {
    1: "Focus sur toi-même : identité, image, nouveaux départs.",
    2: "Focus sur tes ressources : finances, valeurs, talents.",
    3: "Focus sur ta communication : échanges, apprentissages, déplacements.",
    4: "Focus sur ton foyer : famille, racines, vie intérieure.",
    5: "Focus sur ta créativité : expression, plaisir, romance.",
    6: "Focus sur ton quotidien : routine, santé, organisation.",
    7: "Focus sur tes relations : partenariats, collaborations, contrats.",
    8: "Focus sur tes transformations : crises, intimité, ressources partagées.",
    9: "Focus sur ton expansion : voyages, études, philosophie.",
    10: "Focus sur ta carrière : ambitions, statut, accomplissements.",
    11: "Focus sur tes projets collectifs : amitiés, réseaux, idéaux.",
    12: "Focus sur ton intériorité : inconscient, spiritualité, lâcher-prise."
}

FALLBACK_APPROACH = {
    'Aries': "Tu abordes ce mois en mode conquérant : action directe, initiative, courage.",
    'Taurus': "Tu abordes ce mois en mode prudent : patience, stabilité, ancrage.",
    'Gemini': "Tu abordes ce mois en mode curieux : questions, options, adaptabilité.",
    'Cancer': "Tu abordes ce mois en mode réceptif : intuition, protection, empathie.",
    'Leo': "Tu abordes ce mois en mode rayonnant : leadership, générosité, confiance.",
    'Virgo': "Tu abordes ce mois en mode méthodique : analyse, discernement, efficacité.",
    'Libra': "Tu abordes ce mois en mode diplomatique : équilibre, harmonie, négociation.",
    'Scorpio': "Tu abordes ce mois en mode intense : profondeur, transformation, vérité.",
    'Sagittarius': "Tu abordes ce mois en mode expansif : optimisme, vision, aventure.",
    'Capricorn': "Tu abordes ce mois en mode stratégique : structure, responsabilité, endurance.",
    'Aquarius': "Tu abordes ce mois en mode original : innovation, indépendance, collectif.",
    'Pisces': "Tu abordes ce mois en mode fluide : intuition, compassion, créativité."
}


def get_fallback_climate(moon_sign: str) -> str:
    """Retourne le climat fallback pour un signe"""
    return FALLBACK_CLIMATE.get(moon_sign, f"Climat lunaire en {moon_sign}.")


def get_fallback_focus(moon_house: int) -> str:
    """Retourne le focus fallback pour une maison"""
    return FALLBACK_FOCUS.get(moon_house, f"Focus sur la Maison {moon_house}.")


def get_fallback_approach(lunar_ascendant: str) -> str:
    """Retourne l'approche fallback pour un ascendant"""
    return FALLBACK_APPROACH.get(lunar_ascendant, f"Approche avec ascendant {lunar_ascendant}.")


# === GÉNÉRATION CONSEILS HEBDOMADAIRES ===

def generate_weekly_advice(return_date: datetime) -> Dict[str, Any]:
    """
    Génère les conseils hebdomadaires datés (statiques pour l'instant)

    Structure:
    {
        "week_1": {"dates": "Du X au Y", "theme": "...", "conseil": "...", "focus": "..."},
        ...
    }
    """
    weeks = {}
    themes = ["Lancement du cycle", "Consolidation", "Ajustements", "Bilan et clôture"]
    conseils = [
        "Pose tes intentions pour ce nouveau cycle lunaire. C'est le moment d'initier.",
        "Approfondi ce que tu as commencé. Reste ancré(e) et persévère.",
        "Fais le point et ajuste ce qui doit l'être. Flexibilité requise.",
        "Prépare-toi pour le prochain cycle. Lâche ce qui ne sert plus."
    ]
    focus_list = ["intention", "stabilité", "adaptation", "clôture"]

    for i in range(4):
        start = return_date + timedelta(days=i * 7)
        end = start + timedelta(days=6)
        week_key = f"week_{i + 1}"
        weeks[week_key] = {
            "dates": f"Du {start.strftime('%d/%m')} au {end.strftime('%d/%m')}",
            "theme": themes[i],
            "conseil": conseils[i],
            "focus": focus_list[i]
        }

    return weeks


# === CHARGEMENT INTERPRETATION V2 (1728 combinaisons complètes) ===

async def load_full_lunar_interpretation_v2(
    db: AsyncSession,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    version: int = 2,
    lang: str = 'fr'
) -> Optional[Tuple[str, Optional[Dict[str, Any]]]]:
    """
    Charge une interprétation lunaire complète v2 (combinaison unique) avec cache

    V2 = 1728 combinaisons pré-générées par Opus 4.5
    (12 signes × 12 maisons × 12 ascendants)

    Args:
        db: Session async SQLAlchemy
        moon_sign: Signe lunaire (Aries, Taurus, etc.)
        moon_house: Maison lunaire (1-12)
        lunar_ascendant: Ascendant lunaire (Aries, Taurus, etc.)
        version: Version du prompt (2 = Opus 4.5)
        lang: Langue (fr, en)

    Returns:
        Tuple (interpretation_full, weekly_advice) ou None si non trouvé
    """
    from services.interpretation_cache_service import get_lunar_v2_full_cached

    try:
        result = await get_lunar_v2_full_cached(
            db, moon_sign, moon_house, lunar_ascendant, version, lang
        )

        if result:
            logger.debug(
                f"✅ Loaded lunar_interpretation_v2/{moon_sign}/M{moon_house}/ASC_{lunar_ascendant}"
            )
            return result

        logger.debug(
            f"⚠️ lunar_interpretation_v2/{moon_sign}/M{moon_house}/ASC_{lunar_ascendant} not found"
        )
        return None

    except Exception as e:
        logger.error(f"❌ Error loading lunar_interpretation_v2: {e}")
        return None


async def load_lunar_interpretation_with_fallback(
    db: AsyncSession,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    preferred_version: int = 2,
    lang: str = 'fr'
) -> Tuple[Optional[str], Optional[Dict[str, Any]], str]:
    """
    Charge une interprétation lunaire avec fallback automatique

    Ordre de priorité:
    1. V2 (1728 combinaisons Opus 4.5) si disponible
    2. V1 (36 templates par couches) assemblé
    3. Fallback statique

    Args:
        db: Session async SQLAlchemy
        moon_sign: Signe lunaire
        moon_house: Maison lunaire (1-12)
        lunar_ascendant: Ascendant lunaire
        preferred_version: Version préférée (défaut: 2)
        lang: Langue

    Returns:
        Tuple (interpretation_full, weekly_advice, source)
        source = 'database-v2' | 'database-v1' | 'fallback'
    """
    # 1. Essayer V2 d'abord si demandé
    if preferred_version >= 2:
        v2_result = await load_full_lunar_interpretation_v2(
            db, moon_sign, moon_house, lunar_ascendant, version=2, lang=lang
        )
        if v2_result:
            interpretation, weekly_advice = v2_result
            return (interpretation, weekly_advice, 'database-v2')

    # 2. Fallback sur V1 (templates par couches)
    layers = await load_lunar_interpretation_layers(
        db, moon_sign, moon_house, lunar_ascendant, version=1, lang=lang
    )

    # Vérifier si on a au moins une couche V1
    if layers['climate'] or layers['focus'] or layers['approach']:
        # Assembler les couches V1
        parts = []
        if layers['climate']:
            parts.append(layers['climate'])
        else:
            parts.append(get_fallback_climate(moon_sign))

        if layers['focus']:
            parts.append(layers['focus'])
        else:
            parts.append(get_fallback_focus(moon_house))

        if layers['approach']:
            parts.append(layers['approach'])
        else:
            parts.append(get_fallback_approach(lunar_ascendant))

        interpretation = '\n\n'.join(parts)
        return (interpretation, None, 'database-v1')

    # 3. Fallback complet (statique)
    interpretation = '\n\n'.join([
        get_fallback_climate(moon_sign),
        get_fallback_focus(moon_house),
        get_fallback_approach(lunar_ascendant)
    ])
    return (interpretation, None, 'fallback')


def format_weekly_advice_v2(
    weekly_advice_db: Optional[Dict[str, Any]],
    return_date: datetime
) -> Dict[str, Any]:
    """
    Formate les conseils hebdomadaires V2 avec les dates

    Args:
        weekly_advice_db: Conseils depuis la DB (format simple {"week_1": "conseil", ...})
        return_date: Date de début du cycle lunaire

    Returns:
        Format enrichi avec dates: {"week_1": {"dates": "...", "conseil": "...", ...}}
    """
    if not weekly_advice_db:
        # Fallback sur les conseils statiques
        return generate_weekly_advice(return_date)

    weeks = {}
    themes = ["Lancement du cycle", "Consolidation", "Ajustements", "Bilan et clôture"]
    focus_list = ["intention", "stabilité", "adaptation", "clôture"]

    for i in range(4):
        week_key = f"week_{i + 1}"
        start = return_date + timedelta(days=i * 7)
        end = start + timedelta(days=6)

        # Conseil depuis DB ou fallback
        conseil_db = weekly_advice_db.get(week_key, "")

        weeks[week_key] = {
            "dates": f"Du {start.strftime('%d/%m')} au {end.strftime('%d/%m')}",
            "theme": themes[i],
            "conseil": conseil_db if conseil_db else f"Semaine {i + 1} : continue ton cycle.",
            "focus": focus_list[i]
        }

    return weeks
