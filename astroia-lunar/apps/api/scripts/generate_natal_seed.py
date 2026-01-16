"""
Générateur de seed d'interprétations natales offline
Produit 432 interprétations (sun/moon/ascendant × 12 signes × 12 maisons)
"""

import json
from typing import Dict, List

# Mapping des signes (français)
SIGNS = [
    "Bélier", "Taureau", "Gémeaux", "Cancer",
    "Lion", "Vierge", "Balance", "Scorpion",
    "Sagittaire", "Capricorne", "Verseau", "Poissons"
]

# Mapping des maisons
HOUSES = {
    1: ("identité, apparence", "Maison 1 : identité, apparence, nouveau départ"),
    2: ("ressources, valeurs", "Maison 2 : ressources personnelles, valeurs, sécurité matérielle"),
    3: ("communication, environnement proche", "Maison 3 : communication, apprentissage, environnement proche"),
    4: ("foyer, racines", "Maison 4 : foyer, famille, racines, vie privée"),
    5: ("créativité, plaisir", "Maison 5 : créativité, plaisir, expression personnelle"),
    6: ("quotidien, service", "Maison 6 : quotidien, santé, service, travail"),
    7: ("relations, partenariats", "Maison 7 : relations, partenariats, l'autre comme miroir"),
    8: ("intimité, transformation", "Maison 8 : intimité, transformation, ressources partagées"),
    9: ("philosophie, expansion", "Maison 9 : philosophie, voyages, expansion de conscience"),
    10: ("carrière, accomplissement", "Maison 10 : carrière, accomplissement social, visibilité"),
    11: ("projets collectifs, idéaux", "Maison 11 : projets collectifs, amitiés, idéaux"),
    12: ("spiritualité, inconscient", "Maison 12 : spiritualité, inconscient, transcendance")
}

# Emojis par subject
EMOJIS = {
    "sun": "☀️",
    "moon": "🌙",
    "ascendant": "↑"
}

# Labels français
LABELS = {
    "sun": "Soleil",
    "moon": "Lune",
    "ascendant": "Ascendant"
}

# Traits caractéristiques par signe (pour variation)
SIGN_TRAITS = {
    "Bélier": ("action directe", "impulsivité", "pionnier", "feu cardinal"),
    "Taureau": ("stabilité", "sensualité", "patience", "terre fixe"),
    "Gémeaux": ("curiosité", "communication", "versatilité", "air mutable"),
    "Cancer": ("sensibilité", "protection", "mémoire émotionnelle", "eau cardinal"),
    "Lion": ("rayonnement", "créativité", "générosité", "feu fixe"),
    "Vierge": ("analyse", "service", "perfectionnement", "terre mutable"),
    "Balance": ("harmonie", "relation", "esthétique", "air cardinal"),
    "Scorpion": ("intensité", "transformation", "profondeur", "eau fixe"),
    "Sagittaire": ("expansion", "quête de sens", "optimisme", "feu mutable"),
    "Capricorne": ("structure", "ambition", "responsabilité", "terre cardinal"),
    "Verseau": ("innovation", "indépendance", "collectif", "air fixe"),
    "Poissons": ("compassion", "dissolution", "imagination", "eau mutable")
}


def generate_interpretation(subject: str, sign: str, house: int) -> str:
    """Génère une interprétation structurée de ~900-1400 chars"""

    emoji = EMOJIS[subject]
    label = LABELS[subject]
    house_short, house_desc = HOUSES[house]
    trait1, trait2, trait3, element = SIGN_TRAITS[sign]

    # Templates adaptés par subject
    if subject == "sun":
        moteur = f"Cette combinaison pousse à exprimer ton identité à travers {trait1} du {sign} dans le domaine de {house_short}. Tu cherches à rayonner par {trait3}, tout en développant ta {trait2}. L'énergie {element} te donne une approche {trait1.split()[0] if ' ' in trait1 else trait1} de la vie."

        defi = f"Le piège ? Trop de {trait2} peut bloquer ton rayonnement naturel. Équilibre ta force {element} avec la souplesse nécessaire dans tes {house_short}."

        maison = f"Ton Soleil éclaire particulièrement ta {house_desc.lower()}. C'est là que tu construis ton autorité personnelle, en cultivant {trait1} et {trait3}."

        rituel = f"""- Identifie une action concrète qui honore {trait1} dans tes {house_short}
- Prends 3 respirations en visualisant l'énergie {element}
- Note : \"Comment puis-je rayonner davantage dans ma {house_short} tout en restant authentique ?\""""

    elif subject == "moon":
        moteur = f"Tes besoins émotionnels passent par {trait1} du {sign} dans le secteur {house_short}. Tu te ressources grâce à {trait3}, et ta sécurité intérieure se nourrit de {trait2}. L'élément {element} colore tes réactions instinctives."

        defi = f"Attention à ne pas chercher la sécurité uniquement dans {trait2}. Ton défi : accueillir tes émotions {element} sans te laisser submerger dans tes {house_short}."

        maison = f"Ta Lune habite ta {house_desc.lower()}. C'est là que tu trouves ton confort émotionnel, en nourrissant {trait1} et en développant {trait3}."

        rituel = f"""- Crée un espace de confort lié à {house_short}
- Respire en conscience, connecté(e) à l'élément {element}
- Questionne-toi : \"De quoi ai-je vraiment besoin pour me sentir en sécurité dans ma {house_short} ?\""""

    else:  # ascendant
        moteur = f"Tu entres en contact avec le monde par {trait1} du {sign}. Ton masque social exprime {trait3}, et ta première impression passe par {trait2}. L'énergie {element} définit comment tu abordes les nouvelles situations dans le domaine de {house_short}."

        defi = f"Le risque : s'identifier trop au masque {sign} et oublier qui tu es vraiment. Utilise {trait1} comme outil, pas comme prison."

        maison = f"Ton Ascendant façonne ton approche de {house_desc.lower()}. C'est par {trait1} et {trait3} que tu te présentes au monde dans ce secteur."

        rituel = f"""- Observe comment tu te présentes spontanément dans tes {house_short}
- Sens l'énergie {element} à travers ta respiration
- Demande-toi : \"Mon masque social reflète-t-il vraiment mes {house_short} ?\""""

    text = f"""# {emoji} {label} en {sign}

**En une phrase :** {label} en {sign}, maison {house}, c'est l'art de cultiver {trait1} pour nourrir sa {house_short}, tout en transformant {trait2} en force créatrice.

## Ton moteur
{moteur}

## Ton défi
{defi}

## Maison {house} en {sign}
{maison}

## Micro-rituel du jour (2 min)
{rituel}"""

    return text


def generate_seed_file(output_path: str = "apps/api/seeds/natal_interpretations_fr_v2.jsonl"):
    """Génère le fichier JSONL complet avec 432 lignes"""

    subjects = ["sun", "moon", "ascendant"]
    count = 0

    with open(output_path, 'w', encoding='utf-8') as f:
        for subject in subjects:
            for sign in SIGNS:
                for house in range(1, 13):
                    # Générer l'interprétation
                    text = generate_interpretation(subject, sign, house)

                    # Créer l'objet JSON
                    entry = {
                        "lang": "fr",
                        "version": 2,
                        "subject": subject,
                        "sign": sign,
                        "house": house,
                        "text": text,
                        "model": "offline_seed"
                    }

                    # Écrire en JSONL
                    f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                    count += 1

    print(f"✅ Généré {count} interprétations dans {output_path}")
    print(f"   Subjects: {', '.join(subjects)}")
    print(f"   Signes: {len(SIGNS)}")
    print(f"   Maisons: 12")
    print(f"   Total: {len(subjects)} × {len(SIGNS)} × 12 = {count}")


if __name__ == "__main__":
    generate_seed_file()
