#!/usr/bin/env python3
"""
Sprint 4 - Génération des 178 interprétations manquantes
- Pisces : 106 (M4: 10 + M5-M12: 96)
- Scorpio : 72 (M7-M12: 72)
"""

import asyncio
import anthropic
import sys
from pathlib import Path
import uuid
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from config import settings
from database import AsyncSessionLocal
from sqlalchemy.dialects.postgresql import insert
from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation

# Missing combinations
PISCES_MISSING = [
    # Maison 4: 10 ascendants manquants
    ('Pisces', 4, 'Gemini'), ('Pisces', 4, 'Cancer'), ('Pisces', 4, 'Leo'),
    ('Pisces', 4, 'Virgo'), ('Pisces', 4, 'Libra'), ('Pisces', 4, 'Scorpio'),
    ('Pisces', 4, 'Sagittarius'), ('Pisces', 4, 'Capricorn'),
    ('Pisces', 4, 'Aquarius'), ('Pisces', 4, 'Pisces'),
]

# Maisons 5-12 : tous les 12 ascendants pour chaque maison
ASCENDANTS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
              'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

for house in range(5, 13):
    for asc in ASCENDANTS:
        PISCES_MISSING.append(('Pisces', house, asc))

SCORPIO_MISSING = []
for house in range(7, 13):
    for asc in ASCENDANTS:
        SCORPIO_MISSING.append(('Scorpio', house, asc))

ALL_MISSING = PISCES_MISSING + SCORPIO_MISSING

HOUSE_MEANINGS = {
    1: "identité personnelle, image, corps physique, la manière de se présenter au monde",
    2: "ressources matérielles, finances, valeur personnelle, possessions, sécurité matérielle",
    3: "communication, apprentissages courts, échanges locaux, fratrie, voisinage, mental concret",
    4: "foyer, famille, racines, intimité, bases émotionnelles, héritage familial",
    5: "créativité, expression personnelle, romance, plaisir, jeu, enfants, art",
    6: "quotidien, travail, santé, routines, service, organisation pratique",
    7: "relations, partenariats, mariage, l'autre comme miroir, contrats",
    8: "transformations, mort/renaissance, ressources partagées, intimité profonde, pouvoir",
    9: "expansion, voyages lointains, philosophie, études supérieures, quête de sens, spiritualité",
    10: "carrière, ambitions, reconnaissance sociale, accomplissement public, statut",
    11: "collectif, amis, réseaux, projets communs, idéaux, innovations",
    12: "intériorité, spiritualité, inconscient, retraite, ce qui est caché, dissolution de l'ego"
}

SIGN_KEYWORDS = {
    'Aries': "action, impulsivité, courage, initiative, indépendance, pionnier, feu cardinal",
    'Taurus': "stabilité, patience, sensualité, matérialité, persévérance, terre fixe",
    'Gemini': "communication, versatilité, curiosité, mouvement mental, air mutable",
    'Cancer': "émotion, protection, famille, sensibilité, eau cardinale",
    'Leo': "rayonnement, créativité, fierté, générosité, leadership, feu fixe",
    'Virgo': "analyse, service, perfectionnement, discernement, terre mutable",
    'Libra': "harmonie, relations, équilibre, beauté, diplomatie, air cardinal",
    'Scorpio': "intensité, transformation, profondeur, pouvoir, eau fixe",
    'Sagittarius': "expansion, optimisme, philosophie, aventure, feu mutable",
    'Capricorn': "ambition, structure, discipline, responsabilité, terre cardinale",
    'Aquarius': "innovation, liberté, collectif, originalité, air fixe",
    'Pisces': "intuition, compassion, spiritualité, dissolution, eau mutable"
}


def get_system_prompt() -> str:
    """Prompt système pour Claude Opus 4.5"""
    return """Tu es un astrologue expert spécialisé dans l'astrologie lunaire moderne.
Tu dois générer des interprétations lunaires mensuelles qui CROISENT vraiment les 3 dimensions:
1. Le signe de la Lune (tempérament émotionnel)
2. La maison (domaine de vie activé)
3. L'ascendant lunaire (approche instinctive)

RÈGLES STRICTES:
- Ton: 2e personne (tu), présent, chaleureux, direct
- Longueur: 800-1200 caractères pour l'interprétation principale
- Structure EXACTE obligatoire (avec titres en gras):
  **Ton mois en un mot : [thème en 2-3 mots]**
  [3-4 phrases croisant les 3 paramètres]
  **Domaine activé** : Maison X — [2 phrases sur le domaine]
  **Ton approche instinctive** : [2 phrases sur l'ascendant]
  **Tensions possibles** : [1-2 phrases sur les défis]
  **Conseil clé** : [1 phrase actionnable]
- Conseils hebdomadaires: 4 conseils de 80-120 caractères, concrets et actionnables
- CROISER vraiment les 3 dimensions, pas de template générique
- Être SPÉCIFIQUE à cette combinaison unique

Génère UNIQUEMENT le JSON valide avec les clés: moon_sign, moon_house, lunar_ascendant, interpretation, weekly_advice."""


async def generate_interpretation(
    client: anthropic.AsyncAnthropic,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str
) -> dict:
    """Génère une interprétation via Claude Opus 4.5"""

    user_prompt = f"""Génère l'interprétation lunaire pour:
- Signe de la Lune: {moon_sign} ({SIGN_KEYWORDS[moon_sign]})
- Maison: {moon_house} ({HOUSE_MEANINGS[moon_house]})
- Ascendant lunaire: {lunar_ascendant} ({SIGN_KEYWORDS[lunar_ascendant]})

IMPORTANT: Croise VRAIMENT ces 3 dimensions. Par exemple:
- Si Lune Bélier (impulsif) + Maison 4 (foyer) + Asc Taureau (stable) → tension entre vouloir tout changer rapidement à la maison VS besoin de sécurité domestique
- Si Lune Cancer (émotionnel) + Maison 10 (carrière) + Asc Sagittaire (expansif) → nourrir sa carrière émotionnellement tout en visant grand

Réponds UNIQUEMENT avec un JSON valide:
{{
  "moon_sign": "{moon_sign}",
  "moon_house": {moon_house},
  "lunar_ascendant": "{lunar_ascendant}",
  "interpretation": "**Ton mois en un mot : ...**\\n\\n...",
  "weekly_advice": {{
    "week_1": "...",
    "week_2": "...",
    "week_3": "...",
    "week_4": "..."
  }}
}}"""

    try:
        message = await client.messages.create(
            model="claude-opus-4-20250514",  # Opus 4.5 for best quality
            max_tokens=2000,
            temperature=0.8,
            system=get_system_prompt(),
            messages=[{
                "role": "user",
                "content": user_prompt
            }]
        )

        content = message.content[0].text.strip()

        # Clean JSON markers
        if content.startswith('```json'):
            content = content[7:]
        if content.startswith('```'):
            content = content[3:]
        if content.endswith('```'):
            content = content[:-3]
        content = content.strip()

        import json
        interpretation = json.loads(content)

        return interpretation

    except Exception as e:
        print(f"❌ Error for {moon_sign} M{moon_house} Asc {lunar_ascendant}: {e}")
        return None


async def insert_interpretation(
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    interpretation: str,
    weekly_advice: dict
):
    """Insert interpretation into DB"""
    async with AsyncSessionLocal() as session:
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
            model_used='claude-opus-4.5-sprint4'
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=['moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'],
            set_={
                'interpretation_full': interpretation,
                'weekly_advice': weekly_advice,
                'length': len(interpretation),
                'model_used': 'claude-opus-4.5-sprint4',
                'updated_at': datetime.now()
            }
        )

        await session.execute(stmt)
        await session.commit()


async def main():
    """Generate all 178 missing interpretations"""

    if not settings.ANTHROPIC_API_KEY:
        print("❌ ANTHROPIC_API_KEY manquant dans .env")
        return

    print(f"\n{'='*60}")
    print(f"SPRINT 4 - GÉNÉRATION 178 INTERPRÉTATIONS MANQUANTES")
    print(f"{'='*60}\n")
    print(f"📊 Total: 178 = Pisces (106) + Scorpio (72)")
    print(f"🤖 Modèle: Claude Opus 4.5")
    print(f"💰 Coût estimé: $3-5")
    print(f"⏱️  Temps estimé: 10-15min\n")

    client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)

    total_generated = 0
    total_failed = 0

    for i, (sign, house, asc) in enumerate(ALL_MISSING, 1):
        print(f"[{i}/178] {sign} M{house} Asc {asc}...", end=" ", flush=True)

        interp = await generate_interpretation(client, sign, house, asc)

        if interp:
            await insert_interpretation(
                sign, house, asc,
                interp['interpretation'],
                interp['weekly_advice']
            )
            total_generated += 1
            print("✓")
        else:
            total_failed += 1
            print("✗ FAILED")

        # Pause pour ne pas surcharger l'API
        await asyncio.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"🎉 GÉNÉRATION TERMINÉE")
    print(f"{'='*60}")
    print(f"✅ Générées: {total_generated}/178")
    print(f"❌ Échecs: {total_failed}")

    if total_failed == 0:
        print(f"\n🎊 MIGRATION V2 COMPLÈTE À 100% (1728/1728) !")
    else:
        print(f"\n⚠️  Relancer pour réessayer les {total_failed} échecs")

    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    asyncio.run(main())
