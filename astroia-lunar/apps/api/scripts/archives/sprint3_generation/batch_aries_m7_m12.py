"""Batch: Aries M7 to M12 - 72 interpretations"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

# Helper pour generer les 12 ascendants pour chaque maison
ASCENDANTS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
              'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

ASC_TRAITS = {
    'Aries': ('directe', 'fonce d\'abord', 'impulsif'),
    'Taurus': ('ancree', 'prend son temps', 'concret'),
    'Gemini': ('curieuse', 'communique beaucoup', 'adaptable'),
    'Cancer': ('emotionnelle', 'protege ses proches', 'sensible'),
    'Leo': ('rayonnante', 'veut briller', 'genereuse'),
    'Virgo': ('analytique', 'optimise tout', 'precisie'),
    'Libra': ('diplomatique', 'cherche l\'harmonie', 'equilibree'),
    'Scorpio': ('intense', 'transforme en profondeur', 'magnetique'),
    'Sagittarius': ('enthousiaste', 'voit grand', 'aventuriere'),
    'Capricorn': ('structuree', 'planifie long terme', 'disciplinee'),
    'Aquarius': ('originale', 'pense differemment', 'independante'),
    'Pisces': ('intuitive', 'ressent les ambiances', 'fluide')
}

def generate_m7(asc):
    """Maison 7: Relations, Partenariats"""
    t = ASC_TRAITS[asc]
    base = f"""**Ton mois en un mot : Alliance {'ardente' if asc in ['Aries','Leo','Sagittarius'] else 'reflechie' if asc in ['Virgo','Capricorn'] else 'sensible'}**

Ta Lune Belier en Maison 7 active tes relations avec intensite. Tu veux des partenariats dynamiques, des echanges directs. L'ascendant {asc} colore ta maniere d'etre en relation : {t[0]} et {t[2]}.

**Domaine active** : Maison 7 — Partenariats, relations significatives, l'autre comme miroir. Les questions relationnelles sont au premier plan ce mois-ci.

**Ton approche instinctive** : Tu {t[1]}. Dans les relations, tu cherches quelqu'un qui peut suivre ton rythme ou te completer.

**Tensions possibles** : Conflits de pouvoir en couple ou en partenariat, impatience avec les compromis necessaires.

**Conseil cle** : Construire des alliances qui respectent ton energie et celle de l'autre."""
    return base

def generate_m8(asc):
    """Maison 8: Transformations, Intimite"""
    t = ASC_TRAITS[asc]
    return f"""**Ton mois en un mot : Mutation {'intense' if asc in ['Scorpio','Aries','Capricorn'] else 'progressive'}**

Ta Lune Belier en Maison 8 plonge dans les profondeurs. Les themes de transformation, de sexualite, de partage des ressources emergent avec force. L'ascendant {asc} apporte une approche {t[0]}.

**Domaine active** : Maison 8 — Crises, metamorphoses, intimite, ressources partagees. Ce qui etait cache veut emerger.

**Ton approche instinctive** : Tu {t[1]}. Face aux transformations, tu reagis de maniere {t[2]}.

**Tensions possibles** : Confrontation a des peurs profondes, luttes de pouvoir liees a l'argent ou au sexe.

**Conseil cle** : Accueillir les transformations necessaires avec courage et discernement."""

def generate_m9(asc):
    """Maison 9: Expansion, Philosophie"""
    t = ASC_TRAITS[asc]
    return f"""**Ton mois en un mot : Horizon {'enflamme' if asc in ['Aries','Sagittarius','Leo'] else 'reflechi'}**

Ta Lune Belier en Maison 9 veut explorer, apprendre, s'elargir. Les voyages, les etudes, la philosophie t'appellent. L'ascendant {asc} colore cette quete : {t[0]} et {t[2]}.

**Domaine active** : Maison 9 — Voyages lointains, etudes superieures, spiritualite, quete de sens. Tu veux voir plus loin que ton quotidien.

**Ton approche instinctive** : Tu {t[1]}. L'expansion passe par une approche {t[0]}.

**Tensions possibles** : Impatience avec les apprentissages lents, tendance a imposer ta vision.

**Conseil cle** : Explorer avec ouverture sans perdre ton ancrage."""

def generate_m10(asc):
    """Maison 10: Carriere, Accomplissement"""
    t = ASC_TRAITS[asc]
    return f"""**Ton mois en un mot : Ambition {'fulgurante' if asc in ['Aries','Leo','Capricorn'] else 'strategic'}**

Ta Lune Belier en Maison 10 propulse ta carriere. Tu veux reussir, etre reconnu·e, accomplir quelque chose de visible. L'ascendant {asc} structure cette ambition : {t[0]} et {t[2]}.

**Domaine active** : Maison 10 — Carriere, reputation, accomplissements publics. Ton image professionnelle est en jeu.

**Ton approche instinctive** : Tu {t[1]}. Ta strategie professionnelle est {t[0]}.

**Tensions possibles** : Conflits d'autorite, impatience avec la hierarchie, ambition au detriment du reste.

**Conseil cle** : Viser haut tout en construisant des bases solides."""

def generate_m11(asc):
    """Maison 11: Projets collectifs, Amities"""
    t = ASC_TRAITS[asc]
    return f"""**Ton mois en un mot : Vision {'collective' if asc in ['Aquarius','Sagittarius','Libra'] else 'personnelle'}**

Ta Lune Belier en Maison 11 active tes reseaux et projets collectifs. Tu veux faire partie de quelque chose de plus grand, mais a ta maniere. L'ascendant {asc} influence ton role dans le groupe : {t[0]}.

**Domaine active** : Maison 11 — Amities, reseaux, projets de groupe, ideaux. Les causes qui te tiennent a coeur emergent.

**Ton approche instinctive** : Tu {t[1]}. Dans le collectif, tu es {t[2]}.

**Tensions possibles** : Conflits dans le groupe, impatience avec les consensus lents, ego vs collectif.

**Conseil cle** : Contribuer au groupe sans perdre ta singularite."""

def generate_m12(asc):
    """Maison 12: Interiorite, Spiritualite"""
    t = ASC_TRAITS[asc]
    return f"""**Ton mois en un mot : Plongee {'profonde' if asc in ['Scorpio','Pisces','Cancer'] else 'active'}**

Ta Lune Belier en Maison 12 pousse vers l'interieur. C'est paradoxal : l'energie d'action rencontre le lacher-prise. L'ascendant {asc} colore ce voyage interieur : {t[0]} et {t[2]}.

**Domaine active** : Maison 12 — Inconscient, spiritualite, retraite, ce qui est cache. Un temps de bilan et de ressourcement.

**Ton approche instinctive** : Tu {t[1]}, meme face a l'invisible. Ta spiritualite est {t[0]}.

**Tensions possibles** : Resistance au repos, frustration face au flou, confrontation a des peurs cachees.

**Conseil cle** : Laisser l'action ceder la place a la receptivite."""

# Generer les weekly_advice adaptes
def make_weekly(house, asc):
    base_weeks = {
        7: {'week_1': "Clarifie tes attentes relationnelles.", 'week_2': "Engage un dialogue important avec un partenaire.", 'week_3': "Ecoute autant que tu parles.", 'week_4': "Quel partenariat veux-tu pour l'avenir ?"},
        8: {'week_1': "Accepte qu'une transformation soit necessaire.", 'week_2': "Plonge dans ce qui t'effraie.", 'week_3': "Lache ce qui doit mourir.", 'week_4': "Observe ce qui renait en toi."},
        9: {'week_1': "Ouvre-toi a une nouvelle perspective.", 'week_2': "Apprends quelque chose qui t'elargit.", 'week_3': "Connecte savoir et experience.", 'week_4': "Quelle vision emportes-tu ?"},
        10: {'week_1': "Definis un objectif professionnel clair.", 'week_2': "Agis pour ta carriere.", 'week_3': "Gere les enjeux de pouvoir avec diplomatie.", 'week_4': "Evalue tes progres professionnels."},
        11: {'week_1': "Connecte-toi avec ta communaute.", 'week_2': "Contribue a un projet collectif.", 'week_3': "Equilibre individuel et collectif.", 'week_4': "Quel role veux-tu dans le groupe ?"},
        12: {'week_1': "Prends du temps pour toi, seul·e.", 'week_2': "Explore ton monde interieur.", 'week_3': "Lache les combats inutiles.", 'week_4': "Qu'as-tu decouvert sur toi-meme ?"}
    }
    return base_weeks[house]

BATCH = []

for house, gen_func in [(7, generate_m7), (8, generate_m8), (9, generate_m9),
                         (10, generate_m10), (11, generate_m11), (12, generate_m12)]:
    for asc in ASCENDANTS:
        BATCH.append({
            'moon_sign': 'Aries',
            'moon_house': house,
            'lunar_ascendant': asc,
            'interpretation': gen_func(asc),
            'weekly_advice': make_weekly(house, asc)
        })

if __name__ == "__main__":
    asyncio.run(insert_batch(BATCH))
    print(f"\n[BATCH] Aries M7-M12 complete - 144/1728 (Aries DONE)")
