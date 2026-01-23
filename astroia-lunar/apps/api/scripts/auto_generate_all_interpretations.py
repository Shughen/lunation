"""
Script de génération automatique de TOUTES les interprétations lunaires
Utilise Claude API pour générer 1728 interprétations (12 signes × 12 maisons × 12 ascendants)
"""

import asyncio
import anthropic
import sys
from pathlib import Path
from typing import List, Dict
import json

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import settings

# Configuration
SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
HOUSES = list(range(1, 13))
ASCENDANTS = SIGNS.copy()

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
    """Prompt système pour Claude"""
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
) -> Dict:
    """Génère une interprétation via Claude API"""

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
            model="claude-opus-4-20250514",  # Opus 4.5 pour la qualité maximale
            max_tokens=2000,
            temperature=0.8,  # Créativité contrôlée
            system=get_system_prompt(),
            messages=[{
                "role": "user",
                "content": user_prompt
            }]
        )

        # Extraire le JSON de la réponse
        content = message.content[0].text

        # Nettoyer la réponse (enlever les ```json si présents)
        content = content.strip()
        if content.startswith('```json'):
            content = content[7:]
        if content.startswith('```'):
            content = content[3:]
        if content.endswith('```'):
            content = content[:-3]
        content = content.strip()

        # Parser le JSON
        interpretation = json.loads(content)

        return interpretation

    except Exception as e:
        print(f"❌ Erreur pour {moon_sign} M{moon_house} Asc {lunar_ascendant}: {e}")
        return None


async def generate_batch_file(
    client: anthropic.AsyncAnthropic,
    moon_sign: str,
    moon_house: int
):
    """Génère un fichier batch complet (12 ascendants)"""

    print(f"\n{'='*60}")
    print(f"🌙 Génération: {moon_sign} Maison {moon_house}")
    print(f"{'='*60}")

    batch = []

    for i, asc in enumerate(ASCENDANTS, 1):
        print(f"  [{i}/12] Ascendant {asc}...", end=" ", flush=True)

        interp = await generate_interpretation(client, moon_sign, moon_house, asc)

        if interp:
            batch.append(interp)
            print("✓")
        else:
            print("✗ ÉCHEC")
            return False

        # Petite pause pour ne pas surcharger l'API
        await asyncio.sleep(0.5)

    # Écrire le fichier
    filename = f"batch_generated_{moon_sign.lower()}_m{moon_house}.py"
    filepath = Path(__file__).parent / filename

    # Calculer la progression
    total_done = (SIGNS.index(moon_sign) * 12 + moon_house) * 12
    percentage = (total_done / 1728) * 100

    content = f'''"""Batch généré: {moon_sign} M{moon_house} - 12 ascendants"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = {json.dumps(batch, indent=4, ensure_ascii=False)}

if __name__ == "__main__":
    print(f"[*] Batch: {moon_sign} M{moon_house} - {{len(BATCH)}} interprétations")
    asyncio.run(insert_batch(BATCH))
    print(f"[✓] {moon_sign} M{moon_house} terminé - {total_done}/1728 ({percentage:.1f}%)")
'''

    filepath.write_text(content, encoding='utf-8')
    print(f"✅ Fichier créé: {filename}")

    return True


async def main():
    """Génère tous les fichiers batch manquants"""

    if not settings.ANTHROPIC_API_KEY:
        print("❌ ANTHROPIC_API_KEY manquant dans .env")
        return

    print("🚀 Démarrage de la génération automatique")
    print(f"📊 Total à générer: 1728 interprétations = 144 fichiers")
    print(f"🤖 Modèle: Claude Opus 4.5")
    print()

    client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)

    # Vérifier les fichiers existants
    existing_files = list(Path(__file__).parent.glob("batch_generated_*.py"))
    print(f"📁 Fichiers existants: {len(existing_files)}")

    # Générer tous les fichiers manquants
    total_files = 0
    failed_files = []

    for sign in SIGNS:
        for house in HOUSES:
            filename = f"batch_generated_{sign.lower()}_m{house}.py"
            filepath = Path(__file__).parent / filename

            # Skip si déjà existant
            if filepath.exists():
                print(f"⏭️  Skip: {filename} (existe déjà)")
                continue

            success = await generate_batch_file(client, sign, house)

            if success:
                total_files += 1
            else:
                failed_files.append(f"{sign} M{house}")

    # Résumé
    print(f"\n{'='*60}")
    print(f"🎉 GÉNÉRATION TERMINÉE")
    print(f"{'='*60}")
    print(f"✅ Fichiers générés: {total_files}")
    print(f"❌ Échecs: {len(failed_files)}")

    if failed_files:
        print(f"\n⚠️  Fichiers en échec:")
        for f in failed_files:
            print(f"  - {f}")

    print(f"\n📊 Total de fichiers batch: {len(list(Path(__file__).parent.glob('batch_generated_*.py')))}/144")
    print(f"💾 Total d'interprétations générées: {total_files * 12}")


if __name__ == "__main__":
    asyncio.run(main())
