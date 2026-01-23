"""
Generateur de batch pour un signe lunaire complet
Usage: python scripts/batch_sign_generator.py SIGN_KEY
Exemple: python scripts/batch_sign_generator.py Taurus
"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

SIGNS_FR = {
    'Aries': 'Belier', 'Taurus': 'Taureau', 'Gemini': 'Gemeaux',
    'Cancer': 'Cancer', 'Leo': 'Lion', 'Virgo': 'Vierge',
    'Libra': 'Balance', 'Scorpio': 'Scorpion', 'Sagittarius': 'Sagittaire',
    'Capricorn': 'Capricorne', 'Aquarius': 'Verseau', 'Pisces': 'Poissons'
}

SIGN_TRAITS = {
    'Aries': ('dynamique', 'action', 'impatient', 'feu'),
    'Taurus': ('stable', 'securite', 'patient', 'terre'),
    'Gemini': ('curieux', 'communication', 'versatile', 'air'),
    'Cancer': ('emotionnel', 'protection', 'sensible', 'eau'),
    'Leo': ('rayonnant', 'expression', 'fier', 'feu'),
    'Virgo': ('analytique', 'service', 'perfectionniste', 'terre'),
    'Libra': ('harmonieux', 'relation', 'indecis', 'air'),
    'Scorpio': ('intense', 'transformation', 'magnetique', 'eau'),
    'Sagittarius': ('expansif', 'liberte', 'optimiste', 'feu'),
    'Capricorn': ('structure', 'ambition', 'discipline', 'terre'),
    'Aquarius': ('original', 'independance', 'detache', 'air'),
    'Pisces': ('intuitif', 'compassion', 'reveur', 'eau')
}

ASC_APPROACH = {
    'Aries': "tu fonces d'abord, tu reflechis ensuite",
    'Taurus': "tu prends le temps de t'ancrer avant d'agir",
    'Gemini': "tu explores toutes les options en communicant",
    'Cancer': "tu ressens l'ambiance avant de t'engager",
    'Leo': "tu prends le lead avec assurance",
    'Virgo': "tu analyses les details avant de decider",
    'Libra': "tu cherches le consensus et l'equilibre",
    'Scorpio': "tu vas en profondeur, sans compromis",
    'Sagittarius': "tu vises l'horizon avec optimisme",
    'Capricorn': "tu structures et planifies methodiquement",
    'Aquarius': "tu penses differemment, hors des normes",
    'Pisces': "tu laisses ton intuition te guider"
}

HOUSE_THEMES = {
    1: ("identite", "affirmation de soi", "nouveau depart"),
    2: ("ressources", "valeur personnelle", "securite materielle"),
    3: ("communication", "environnement proche", "apprentissage"),
    4: ("foyer", "famille", "racines"),
    5: ("creativite", "plaisir", "expression personnelle"),
    6: ("quotidien", "sante", "organisation"),
    7: ("relations", "partenariats", "l'autre"),
    8: ("transformation", "intimite", "partage"),
    9: ("expansion", "philosophie", "voyages"),
    10: ("carriere", "accomplissement", "statut"),
    11: ("projets collectifs", "amities", "ideaux"),
    12: ("interiorite", "spiritualite", "lacher-prise")
}

HOUSE_KEYWORDS = {
    1: "qui tu es", 2: "ce que tu possedes", 3: "comment tu echanges",
    4: "d'ou tu viens", 5: "ce que tu crees", 6: "ce que tu fais chaque jour",
    7: "avec qui tu t'allies", 8: "ce que tu transformes", 9: "ce que tu cherches",
    10: "ce que tu accomplis", 11: "ce que tu reves collectivement", 12: "ce que tu laches"
}

def get_element_synergy(moon_elem, asc_elem):
    if moon_elem == asc_elem:
        return f"Harmonie {moon_elem.capitalize()}"
    elif (moon_elem in ['feu', 'air'] and asc_elem in ['feu', 'air']) or \
         (moon_elem in ['terre', 'eau'] and asc_elem in ['terre', 'eau']):
        return "Synergie"
    else:
        return "Integration"

def generate_interpretation(moon_sign, moon_house, lunar_asc):
    moon_fr = SIGNS_FR[moon_sign]
    asc_fr = SIGNS_FR[lunar_asc]
    moon_tr = SIGN_TRAITS[moon_sign]
    asc_tr = SIGN_TRAITS[lunar_asc]
    house_th = HOUSE_THEMES[moon_house]
    house_kw = HOUSE_KEYWORDS[moon_house]
    asc_app = ASC_APPROACH[lunar_asc]

    theme = get_element_synergy(moon_tr[3], asc_tr[3])

    interp = f"""**Ton mois en un mot : {theme}**

Ce mois-ci, ta Lune en {moon_fr} active la Maison {moon_house} : {house_th[0]}, {house_th[1]}, {house_th[2]}. Ton energie emotionnelle est {moon_tr[0]}, portee par un besoin de {moon_tr[1]}. L'ascendant lunaire {asc_fr} colore ta maniere d'aborder ce cycle.

**Domaine active** : Maison {moon_house} — {house_kw.capitalize()} est au centre de tes preoccupations emotionnelles. Ce domaine demande ton attention et ton energie ce mois-ci. Les situations liees a {house_th[0]} te touchent particulierement.

**Ton approche instinctive** : Avec l'ascendant {asc_fr}, {asc_app}. Cette energie {asc_tr[0]} influence ta maniere de reagir face aux situations de la Maison {moon_house}.

**Tensions possibles** : La nature {moon_tr[2]} de ta Lune {moon_fr} peut creer des frictions avec ton approche {asc_tr[2]} ({asc_fr}). Trouve l'equilibre entre ces deux energies.

**Conseil cle** : Honorer ton besoin de {moon_tr[1]} tout en cultivant l'approche {asc_tr[0]} dans le domaine de {house_th[0]}."""

    weekly = {
        'week_1': f"Pose tes intentions pour ce cycle en Maison {moon_house}. Clarifie {house_kw}.",
        'week_2': f"Approfondi ce que tu as initie. Utilise ton energie {moon_tr[0]}.",
        'week_3': f"Ajuste si necessaire. L'approche {asc_tr[0]} t'aide a naviguer.",
        'week_4': f"Fais le bilan du cycle. Qu'as-tu appris sur {house_kw} ?"
    }

    return interp, weekly

def generate_batch_for_sign(moon_sign):
    """Genere les 144 interpretations pour un signe lunaire"""
    batch = []
    for house in range(1, 13):
        for asc in SIGNS:
            interp, weekly = generate_interpretation(moon_sign, house, asc)
            batch.append({
                'moon_sign': moon_sign,
                'moon_house': house,
                'lunar_ascendant': asc,
                'interpretation': interp,
                'weekly_advice': weekly
            })
    return batch

async def main(moon_sign):
    print(f"[*] Generation batch pour {moon_sign} (144 interpretations)...")
    batch = generate_batch_for_sign(moon_sign)
    await insert_batch(batch)

    # Calculer la progression
    sign_index = SIGNS.index(moon_sign)
    done = (sign_index + 1) * 144
    print(f"\n[BATCH] {moon_sign} complete - {done}/1728")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/batch_sign_generator.py SIGN_KEY")
        print("Signs: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces")
        sys.exit(1)

    moon_sign = sys.argv[1]
    if moon_sign not in SIGNS:
        print(f"Signe invalide: {moon_sign}")
        sys.exit(1)

    asyncio.run(main(moon_sign))
