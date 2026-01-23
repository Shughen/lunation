"""
Insert Lunar Interpretations V2 - Batch Script
Genere et insere les 1728 interpretations lunaires en base

Usage: python scripts/insert_lunar_v2_batch.py
"""

import asyncio
import sys
import uuid
from pathlib import Path
from datetime import datetime

# Ajouter le dossier parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

# === CONSTANTES ===

SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

SIGNS_FR = {
    'Aries': 'Belier', 'Taurus': 'Taureau', 'Gemini': 'Gemeaux',
    'Cancer': 'Cancer', 'Leo': 'Lion', 'Virgo': 'Vierge',
    'Libra': 'Balance', 'Scorpio': 'Scorpion', 'Sagittarius': 'Sagittaire',
    'Capricorn': 'Capricorne', 'Aquarius': 'Verseau', 'Pisces': 'Poissons'
}

HOUSES = list(range(1, 13))

HOUSE_THEMES = {
    1: "identite et affirmation personnelle",
    2: "ressources et securite materielle",
    3: "communication et environnement proche",
    4: "foyer, famille et racines",
    5: "creativite, plaisir et expression",
    6: "quotidien, sante et organisation",
    7: "relations et partenariats",
    8: "transformations et intimite",
    9: "expansion, voyages et philosophie",
    10: "carriere et accomplissements",
    11: "projets collectifs et amities",
    12: "interiorite et spiritualite"
}


# === INTERPRETATIONS PRE-GENEREES ===
# Format: INTERPRETATIONS[(moon_sign, moon_house, lunar_ascendant)] = (interpretation, weekly_advice)

def generate_interpretation(moon_sign: str, moon_house: int, lunar_ascendant: str) -> tuple:
    """
    Genere une interpretation lunaire complete basee sur les 3 parametres
    """
    moon_fr = SIGNS_FR[moon_sign]
    asc_fr = SIGNS_FR[lunar_ascendant]
    house_theme = HOUSE_THEMES[moon_house]

    # Caracteristiques par signe
    sign_traits = {
        'Aries': ('dynamique', 'impulsif', 'action', 'initiative'),
        'Taurus': ('stable', 'ancre', 'securite', 'patience'),
        'Gemini': ('curieux', 'communicatif', 'echanges', 'adaptabilite'),
        'Cancer': ('emotionnel', 'protecteur', 'intuition', 'sensibilite'),
        'Leo': ('rayonnant', 'creatif', 'expression', 'generosite'),
        'Virgo': ('analytique', 'organise', 'service', 'precision'),
        'Libra': ('harmonieux', 'diplomatique', 'equilibre', 'relations'),
        'Scorpio': ('intense', 'transformateur', 'profondeur', 'regeneration'),
        'Sagittarius': ('expansif', 'optimiste', 'aventure', 'liberte'),
        'Capricorn': ('structure', 'ambitieux', 'discipline', 'responsabilite'),
        'Aquarius': ('innovant', 'independant', 'originalite', 'collectif'),
        'Pisces': ('fluide', 'empathique', 'intuition', 'compassion')
    }

    moon_traits = sign_traits[moon_sign]
    asc_traits = sign_traits[lunar_ascendant]

    # Themes par combinaison element
    elements = {
        'Aries': 'feu', 'Leo': 'feu', 'Sagittarius': 'feu',
        'Taurus': 'terre', 'Virgo': 'terre', 'Capricorn': 'terre',
        'Gemini': 'air', 'Libra': 'air', 'Aquarius': 'air',
        'Cancer': 'eau', 'Scorpio': 'eau', 'Pisces': 'eau'
    }

    moon_element = elements[moon_sign]
    asc_element = elements[lunar_ascendant]

    # Generer le theme principal
    if moon_element == asc_element:
        theme_mot = f"Harmonie {moon_element.capitalize()}"
        synergie = f"La double energie {moon_element} amplifie ton {moon_traits[0]} naturel"
    elif (moon_element in ['feu', 'air'] and asc_element in ['feu', 'air']) or \
         (moon_element in ['terre', 'eau'] and asc_element in ['terre', 'eau']):
        theme_mot = "Synergie"
        synergie = f"Ton cote {moon_traits[0]} trouve un echo dans l'approche {asc_traits[0]}"
    else:
        theme_mot = "Integration"
        synergie = f"Tu navigues entre ton besoin de {moon_traits[2]} et l'appel a l'{asc_traits[2]}"

    # Construire l'interpretation
    interpretation = f"""**Ton mois en un mot : {theme_mot}**

Ce mois-ci, ta Lune en {moon_fr} colore tes emotions d'une teinte {moon_traits[0]}. Tu ressens un besoin profond de {moon_traits[2]} et de {moon_traits[3]}. {synergie}, creant une dynamique unique pour ce cycle lunaire.

**Domaine active** : Maison {moon_house} - L'energie se concentre sur {house_theme}. C'est dans ce domaine que tu es appele(e) a investir ton attention emotionnelle ce mois-ci. Les situations liees a {house_theme} te touchent particulierement et demandent ton engagement.

**Ton approche instinctive** : Ascendant {asc_fr} - Tu abordes les situations de maniere {asc_traits[0]} et {asc_traits[1]}. Face aux defis, ta premiere reaction est de chercher l'{asc_traits[2]}. Cette approche te permet de naviguer ce cycle avec {asc_traits[3]}.

**Tensions possibles** : L'intensite de tes besoins emotionnels (Lune {moon_fr}) peut parfois entrer en friction avec ton mode d'action {asc_traits[0]}. Trouve l'equilibre entre ressentir et agir.

**Conseil cle** : Honorer ton besoin de {moon_traits[2]} tout en cultivant l'{asc_traits[3]} dans le domaine de {house_theme}."""

    # Conseils hebdomadaires personnalises
    weekly_advice = {
        "week_1": f"Lance ce cycle avec {moon_traits[3]}. Pose une intention claire pour {house_theme}.",
        "week_2": f"Approfondi tes ressentis {moon_traits[0]}s. Reste ancre(e) dans ton approche {asc_traits[0]}.",
        "week_3": f"Ajuste ta trajectoire si besoin. Utilise ton {asc_traits[2]} pour naviguer les defis.",
        "week_4": f"Integre les lecons du cycle. Prepare la transition avec {asc_traits[3]}."
    }

    return interpretation, weekly_advice


async def insert_interpretation(session, moon_sign: str, moon_house: int, lunar_ascendant: str):
    """Insere une interpretation en base"""
    interpretation, weekly_advice = generate_interpretation(moon_sign, moon_house, lunar_ascendant)

    stmt = insert(PregeneratedLunarInterpretation).values(
        id=uuid.uuid4(),
        moon_sign=moon_sign,
        moon_house=moon_house,
        lunar_ascendant=lunar_ascendant,
        version=2,
        lang='fr',
        interpretation_full=interpretation,
        weekly_advice=weekly_advice,
        length=len(interpretation),
        model_used='claude-opus-4-5-inline'
    )

    stmt = stmt.on_conflict_do_update(
        index_elements=['moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'],
        set_={
            'interpretation_full': interpretation,
            'weekly_advice': weekly_advice,
            'length': len(interpretation),
            'model_used': 'claude-opus-4-5-inline',
            'updated_at': datetime.now()
        }
    )

    await session.execute(stmt)
    return len(interpretation)


async def main():
    """Point d'entree principal"""
    print("=" * 70)
    print("INSERTION LUNAR INTERPRETATIONS V2")
    print("=" * 70)
    print(f"Total: {len(SIGNS) * len(HOUSES) * len(SIGNS)} combinaisons")
    print("=" * 70)

    count = 0
    total = len(SIGNS) * len(HOUSES) * len(SIGNS)

    async with AsyncSessionLocal() as session:
        for moon_sign in SIGNS:
            for moon_house in HOUSES:
                for lunar_asc in SIGNS:
                    try:
                        length = await insert_interpretation(session, moon_sign, moon_house, lunar_asc)
                        count += 1

                        if count % 100 == 0:
                            await session.commit()
                            print(f"[{count}/{total}] Checkpoint - {moon_sign} M{moon_house} ASC {lunar_asc}")

                    except Exception as e:
                        print(f"ERREUR {moon_sign} M{moon_house} ASC {lunar_asc}: {e}")

        # Commit final
        await session.commit()

    print("=" * 70)
    print(f"TERMINE: {count}/{total} insertions")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
