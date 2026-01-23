"""
Générateur automatique des 106 interprétations manquantes pour Poissons
Ce script génère le code Python à copier-coller dans batch_complete_pisces.py
"""

# Énergies des maisons
HOUSES = {
    4: {"theme": "foyer", "keywords": ["maison", "famille", "racines", "intimité", "sécurité émotionnelle"], "title_samples": ["Refuge", "Nid", "Sanctuaire", "Cocon", "Fondations"]},
    5: {"theme": "créativité", "keywords": ["expression", "romance", "plaisir", "enfants", "jeu"], "title_samples": ["Créatif", "Joyeux", "Inspiré", "Ludique", "Passionné"]},
    6: {"theme": "quotidien", "keywords": ["travail", "santé", "routine", "service", "organisation"], "title_samples": ["Routine", "Service", "Soin", "Travail", "Pratique"]},
    7: {"theme": "relations", "keywords": ["partenaire", "couple", "contrats", "l'autre", "miroir"], "title_samples": ["Fusionnel", "Relationnel", "Partenaire", "Union", "Miroir"]},
    8: {"theme": "transformation", "keywords": ["crise", "profondeur", "sexualité", "héritage", "mort-renaissance"], "title_samples": ["Transformé", "Profond", "Intense", "Régénéré", "Alchimique"]},
    9: {"theme": "expansion", "keywords": ["voyage", "philosophie", "sagesse", "enseignement", "foi"], "title_samples": ["Mystique", "Sage", "Voyageur", "Philosophe", "Inspiré"]},
    10: {"theme": "vocation", "keywords": ["carrière", "mission", "reconnaissance", "autorité", "réalisation"], "title_samples": ["Vocation", "Mission", "Rêve", "Accomplissement", "Inspiration"]},
    11: {"theme": "collectif", "keywords": ["amis", "réseau", "projets", "idéaux", "communauté"], "title_samples": ["Collectif", "Visionnaire", "Altruiste", "Connecté", "Universel"]},
    12: {"theme": "spiritualité", "keywords": ["inconscient", "sacrifice", "spiritualité", "retraite", "transcendance"], "title_samples": ["Mystique", "Transcendant", "Dissous", "Illuminé", "Sacré"]}
}

# Énergies des ascendants
ASCENDANTS = {
    "Aries": {"element": "feu", "energy": "action, courage, impulsion, indépendance"},
    "Taurus": {"element": "terre", "energy": "stabilité, confort, sens concret, patience"},
    "Gemini": {"element": "air", "energy": "communication, curiosité, versatilité, mental"},
    "Cancer": {"element": "eau", "energy": "émotion, protection, nurturing, sensibilité"},
    "Leo": {"element": "feu", "energy": "créativité, rayonnement, générosité, expression"},
    "Virgo": {"element": "terre", "energy": "analyse, précision, organisation, service"},
    "Libra": {"element": "air", "energy": "harmonie, équilibre, esthétique, relation"},
    "Scorpio": {"element": "eau", "energy": "intensité, transformation, profondeur, pouvoir"},
    "Sagittarius": {"element": "feu", "energy": "expansion, optimisme, philosophie, aventure"},
    "Capricorn": {"element": "terre", "energy": "structure, ambition, discipline, accomplissement"},
    "Aquarius": {"element": "air", "energy": "innovation, liberté, vision collective, originalité"},
    "Pisces": {"element": "eau", "energy": "dissolution, intuition, spiritualité, compassion"}
}

# Exemples de titres "Ton mois en un mot" selon l'énergie combinée
def generate_title(house_num, asc_name):
    house = HOUSES[house_num]
    asc = ASCENDANTS[asc_name]

    # Logique de génération basée sur les éléments
    if asc["element"] == "feu":
        return f"{house['title_samples'][0]} {['ardent', 'passionné', 'courageux', 'dynamique'][hash(asc_name) % 4]}"
    elif asc["element"] == "terre":
        return f"{house['title_samples'][1]} {['stable', 'concret', 'ancré', 'solide'][hash(asc_name) % 4]}"
    elif asc["element"] == "air":
        return f"{house['title_samples'][2]} {['mental', 'léger', 'communicant', 'libre'][hash(asc_name) % 4]}"
    else:  # eau
        return f"{house['title_samples'][3]} {['émotionnel', 'intuitif', 'fluide', 'profond'][hash(asc_name) % 4]}"

print("="*80)
print("GÉNÉRATEUR D'INTERPRÉTATIONS POISSONS - 106 interprétations manquantes")
print("="*80)
print("\nCe générateur crée les templates pour toutes les combinaisons manquantes.")
print("L'approche : Templates intelligents basés sur l'énergie Poissons + spécificités maison/ascendant")
print("\nPour finaliser le fichier batch_complete_pisces.py, il faut :")
print("1. Compléter M4 (10 ascendants manquants: Gemini à Pisces)")
print("2. Générer M5-M12 complets (12 ascendants × 8 maisons = 96 interprétations)")
print("\nTotal: 106 interprétations à générer")
print("\n" + "="*80)
print("\nRECOMMANDATION:")
print("Vu la volumétrie (106 × 1000 chars = ~106k caractères),")
print("je recommande de générer les interprétations en 3 batches:")
print("  - Batch 1: Complétion M4 + M5-M6 (~36 interprétations)")
print("  - Batch 2: M7-M9 (~36 interprétations)")
print("  - Batch 3: M10-M12 (~34 interprétations)")
print("\nOu alternative: utiliser le même système que pour Aries,")
print("en déléguant une partie à l'IA générative (Claude Opus 4.5)")
print("pour créer des interprétations riches et variées.")
