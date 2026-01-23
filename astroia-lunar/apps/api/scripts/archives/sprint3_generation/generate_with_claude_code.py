"""
Génération d'interprétations lunaires directement avec Claude Code
Ce script sert de template pour générer les interprétations progressivement
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

# Signes du zodiaque
SIGNS = [
    ('Aries', 'Belier'), ('Taurus', 'Taureau'), ('Gemini', 'Gemeaux'),
    ('Cancer', 'Cancer'), ('Leo', 'Lion'), ('Virgo', 'Vierge'),
    ('Libra', 'Balance'), ('Scorpio', 'Scorpion'), ('Sagittarius', 'Sagittaire'),
    ('Capricorn', 'Capricorne'), ('Aquarius', 'Verseau'), ('Pisces', 'Poissons')
]

HOUSE_DESCRIPTIONS = {
    1: "identité, apparence, nouveaux départs",
    2: "ressources, valeurs, sécurité matérielle",
    3: "communication, apprentissages, environnement proche",
    4: "foyer, famille, racines, vie intérieure",
    5: "créativité, plaisir, expression personnelle, romance",
    6: "quotidien, routine, santé, organisation",
    7: "relations, partenariats, collaborations",
    8: "transformations, crises, intimité, ressources partagées",
    9: "expansion, voyages, philosophie, quête de sens",
    10: "carrière, ambitions, accomplissements, statut",
    11: "projets collectifs, amitiés, réseaux, idéaux",
    12: "intériorité, inconscient, spiritualité, lâcher-prise"
}

def get_sign_label(sign_key):
    for key, label in SIGNS:
        if key == sign_key:
            return label
    return sign_key


# === BATCH À INSÉRER ===
# Les interprétations seront ajoutées ici par Claude Code
BATCH = []


async def main():
    if not BATCH:
        print("[!] Aucune interprétation dans BATCH")
        print("[!] Claude Code doit remplir BATCH avec les interprétations générées")
        return

    print(f"[*] Insertion de {len(BATCH)} interprétations...")
    await insert_batch(BATCH)
    print(f"[✓] Terminé !")


if __name__ == "__main__":
    asyncio.run(main())
