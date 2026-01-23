"""Script de génération des 144 interprétations complètes pour Libra"""
import json

# Énergie Balance : air cardinal, harmonieux, diplomatique, esthétique, relationnel, juste, équilibré

HOUSES_THEMES = {
    1: {"theme": "Identité et image", "focus": "présentation personnelle, apparence, authenticité"},
    2: {"theme": "Ressources et valeurs", "focus": "finances, possessions, estime de soi matérielle"},
    3: {"theme": "Communication et apprentissage", "focus": "échanges, voisinage, déplacements quotidiens"},
    4: {"theme": "Foyer et racines", "focus": "maison, famille, intimité émotionnelle"},
    5: {"theme": "Créativité et plaisir", "focus": "expression artistique, romance, jeu, enfants"},
    6: {"theme": "Travail et santé", "focus": "quotidien, service, bien-être physique"},
    7: {"theme": "Partenariats et relations", "focus": "couple, associations, contrats"},
    8: {"theme": "Transformation et intimité", "focus": "ressources partagées, sexualité, profondeur"},
    9: {"theme": "Expansion et sagesse", "focus": "voyages, philosophie, enseignement"},
    10: {"theme": "Carrière et réputation", "focus": "ambition professionnelle, image publique"},
    11: {"theme": "Communauté et idéaux", "focus": "amitiés, réseaux, projets collectifs"},
    12: {"theme": "Spiritualité et transcendance", "focus": "retraite, guérison, inconscient"}
}

ASCENDANTS_ENERGY = {
    'Aries': "action, impulsivité, franchise, courage",
    'Taurus': "stabilité, patience, sensorialité, pragmatisme",
    'Gemini': "communication, curiosité, adaptabilité, légèreté",
    'Cancer': "sensibilité, protection, empathie, sécurité",
    'Leo': "rayonnement, générosité, confiance, créativité",
    'Virgo': "précision, analyse, service, perfectionnisme",
    'Libra': "harmonie, diplomatie, esthétique, équilibre",
    'Scorpio': "intensité, transformation, profondeur, contrôle",
    'Sagittarius': "expansion, optimisme, liberté, philosophie",
    'Capricorn': "structure, ambition, discipline, responsabilité",
    'Aquarius': "originalité, innovation, indépendance, collectif",
    'Pisces': "intuition, compassion, fluidité, spiritualité"
}

def generate_interpretation(moon_sign, moon_house, lunar_ascendant):
    """Génère une interprétation complète pour Libra"""

    house_info = HOUSES_THEMES[moon_house]
    asc_energy = ASCENDANTS_ENERGY[lunar_ascendant]

    # Titre synthétique
    if lunar_ascendant == 'Libra':
        title = f"{'Double' if moon_house in [1, 7] else 'Triple'} harmonie"
    elif lunar_ascendant in ['Aries', 'Scorpio']:
        title = f"Équilibre {'actif' if lunar_ascendant == 'Aries' else 'intense'}"
    elif lunar_ascendant in ['Taurus', 'Cancer', 'Pisces']:
        title = f"Grâce {'solide' if lunar_ascendant == 'Taurus' else 'tendre' if lunar_ascendant == 'Cancer' else 'fluide'}"
    elif lunar_ascendant in ['Gemini', 'Sagittarius', 'Aquarius']:
        title = f"Harmonie {'vive' if lunar_ascendant == 'Gemini' else 'libre' if lunar_ascendant == 'Sagittarius' else 'originale'}"
    else:
        title = f"Équilibre {lunar_ascendant.lower()[:8]}"

    # Interprétation principale (800-1200 chars)
    interpretation = f"""**Ton mois en un mot : {title}**

Ta Lune en Balance en Maison {moon_house} active {house_info['theme'].lower()}. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans {house_info['focus']}. Ton Ascendant {lunar_ascendant} ajoute {asc_energy}, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison {moon_house} — {house_info['theme']} devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant {lunar_ascendant} colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche {"équilibrée et naturelle" if lunar_ascendant == 'Libra' else "unique qui allie diplomatie et " + asc_energy.split(',')[0]} dans la gestion de {house_info['focus']}.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et {"l'intensité de ton Ascendant" if lunar_ascendant in ['Aries', 'Scorpio', 'Leo'] else "l'énergie de ton Ascendant " + lunar_ascendant} peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance."""

    # Conseils hebdomadaires
    weekly_advice = {
        'week_1': f"Identifie ce qui manque d'équilibre dans {house_info['theme'].lower()}.",
        'week_2': f"Prends une initiative pour harmoniser {house_info['focus'].split(',')[0]}.",
        'week_3': f"Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
        'week_4': f"Célèbre l'harmonie que tu as créée dans {house_info['theme'].lower()}."
    }

    return {
        'moon_sign': moon_sign,
        'moon_house': moon_house,
        'lunar_ascendant': lunar_ascendant,
        'interpretation': interpretation,
        'weekly_advice': weekly_advice
    }

def generate_all_libra_interpretations():
    """Génère les 144 interprétations pour Libra (12 maisons × 12 ascendants)"""
    batch = []
    houses = range(1, 13)
    ascendants = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                  'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

    for house in houses:
        for ascendant in ascendants:
            interp = generate_interpretation('Libra', house, ascendant)
            batch.append(interp)

    return batch

def write_batch_file():
    """Écrit le fichier batch_complete_libra.py"""
    batch = generate_all_libra_interpretations()

    content = '''"""Batch complet: Libra - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [\n'''

    for i, interp in enumerate(batch):
        if i > 0:
            content += ",\n\n"

        # Formatage de l'interprétation
        content += f"    {{\n"
        content += f"        'moon_sign': '{interp['moon_sign']}', 'moon_house': {interp['moon_house']}, 'lunar_ascendant': '{interp['lunar_ascendant']}',\n"
        content += f"        'interpretation': \"\"\"{interp['interpretation']}\"\"\",\n"
        content += f"        'weekly_advice': {{\n"
        for week, advice in interp['weekly_advice'].items():
            content += f"            '{week}': \"{advice}\",\n"
        content += "        }\n"
        content += "    }"

    content += '''\n]

if __name__ == "__main__":
    print(f"Préparation de l'insertion de {len(BATCH)} interprétations Libra...")
    asyncio.run(insert_batch(BATCH))
    print("✅ Batch Libra complet inséré avec succès !")
'''

    with open('/Users/remibeaurain/astroia/astroia-lunar/apps/api/scripts/batch_complete_libra.py', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Généré {len(batch)} interprétations Libra dans batch_complete_libra.py")

if __name__ == "__main__":
    write_batch_file()
