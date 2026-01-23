"""Générateur automatique des 144 interprétations Virgo complètes"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Structure: moon_house -> themes/keywords
HOUSE_THEMES = {
    1: {
        'titre': 'Identité personnelle',
        'focus': 'ton image, ton corps, ta présentation au monde',
        'verbe': 'te perfectionner, te montrer impeccable, optimiser qui tu es'
    },
    2: {
        'titre': 'Ressources et sécurité',
        'focus': 'tes finances, tes possessions, ta valeur matérielle',
        'verbe': 'gérer méthodiquement, économiser efficacement, optimiser tes revenus'
    },
    3: {
        'titre': 'Communication et apprentissage',
        'focus': 'tes échanges, tes mots, ton quotidien intellectuel',
        'verbe': 'communiquer précisément, apprendre méthodiquement, analyser les échanges'
    },
    4: {
        'titre': 'Foyer et racines',
        'focus': 'ton chez-toi, ta famille, tes fondations émotionnelles',
        'verbe': 'organiser ton espace, trier ton passé, créer un refuge fonctionnel'
    },
    5: {
        'titre': 'Créativité et plaisir',
        'focus': 'tes créations, tes loisirs, tes romances',
        'verbe': 'créer avec méthode, perfectionner tes talents, analyser le plaisir'
    },
    6: {
        'titre': 'Travail quotidien et santé',
        'focus': 'tes routines, ta santé, ton service aux autres',
        'verbe': 'optimiser ton quotidien, perfectionner tes habitudes, servir efficacement'
    },
    7: {
        'titre': 'Relations et partenariats',
        'focus': 'tes couples, tes associations, tes collaborations',
        'verbe': 'analyser tes relations, améliorer tes partenariats, perfectionner l\'équilibre'
    },
    8: {
        'titre': 'Transformation et intimité',
        'focus': 'tes profondeurs, ta sexualité, les ressources partagées',
        'verbe': 'transformer méthodiquement, analyser l\'intimité, gérer le partagé'
    },
    9: {
        'titre': 'Philosophie et expansion',
        'focus': 'tes croyances, tes voyages, ton sens de la vie',
        'verbe': 'analyser tes convictions, perfectionner ta vision, organiser l\'exploration'
    },
    10: {
        'titre': 'Carrière et réputation',
        'focus': 'ton ambition, ta réussite publique, ton impact social',
        'verbe': 'exceller professionnellement, perfectionner ton image, optimiser ta carrière'
    },
    11: {
        'titre': 'Amitiés et communauté',
        'focus': 'tes réseaux, tes idéaux, tes projets collectifs',
        'verbe': 'analyser tes amitiés, contribuer avec précision, perfectionner le collectif'
    },
    12: {
        'titre': 'Spiritualité et inconscient',
        'focus': 'ton intériorité, tes rêves, ton lâcher-prise',
        'verbe': 'analyser ton inconscient, organiser le chaos intérieur, servir silencieusement'
    }
}

# Ascendants: energie principale
ASCENDANT_ENERGY = {
    'Aries': ('fonce', 'action immédiate', 'impatience constructive'),
    'Taurus': ('ancre', 'stabilité progressive', 'patience concrète'),
    'Gemini': ('explore', 'curiosité multiple', 'dispersion intellectuelle'),
    'Cancer': ('ressens', 'sensibilité profonde', 'besoin de sécurité émotionnelle'),
    'Leo': ('brille', 'fierté visible', 'besoin de reconnaissance'),
    'Virgo': ('analyse', 'perfectionnisme total', 'contrôle minutieux'),
    'Libra': ('équilibre', 'recherche d\'harmonie', 'indécision élégante'),
    'Scorpio': ('transforme', 'intensité émotionnelle', 'profondeur obsessionnelle'),
    'Sagittarius': ('explore', 'vision philosophique', 'lâcher-prise optimiste'),
    'Capricorn': ('construit', 'ambition structurée', 'discipline à long terme'),
    'Aquarius': ('innove', 'originalité détachée', 'expérimentation conceptuelle'),
    'Pisces': ('dissout', 'fluidité intuitive', 'fusion compassionnelle')
}

def generate_interpretation(moon_house, lunar_asc):
    """Génère une interprétation Virgo complète"""
    theme = HOUSE_THEMES[moon_house]
    asc_verb, asc_energy, asc_tension = ASCENDANT_ENERGY[lunar_asc]

    # Titre court
    if lunar_asc == 'Virgo':
        titre = f"Triple analyse {theme['titre'].lower()}"
    elif lunar_asc == 'Taurus':
        titre = f"Perfectionnisme ancré"
    elif lunar_asc == 'Capricorn':
        titre = f"Excellence structurée"
    elif lunar_asc == 'Scorpio':
        titre = f"Perfection intense"
    elif lunar_asc == 'Pisces':
        titre = f"Ordre et chaos"
    else:
        titre = f"Analyse et {asc_energy.split()[0]}"

    # Corps de l'interprétation (800-1200 chars)
    intro = f"Ta Lune en Vierge en Maison {moon_house} analyse {theme['focus']} avec minutie. "

    if lunar_asc == 'Virgo':
        intro += f"Triple Vierge : le perfectionnisme atteint son paroxysme. Chaque détail est scruté, optimisé, amélioré sans relâche."
    else:
        intro += f"L'Ascendant {lunar_asc} {asc_verb} : {asc_energy}. Cette combinaison crée une dynamique unique dans ta quête de perfection."

    domaine = f"**Domaine activé** : Maison {moon_house} — {theme['titre']}. Tu veux {theme['verbe']}. Chaque imperfection te saute aux yeux et demande correction."

    approche = f"**Ton approche instinctive** : L'Ascendant {lunar_asc} te pousse à {asc_verb} dans ce domaine. {asc_energy.capitalize()}. La Vierge analyse et ajuste constamment."

    if lunar_asc in ['Aries', 'Leo', 'Sagittarius']:
        tension = f"**Tensions possibles** : Le feu de {lunar_asc} crée de l'impatience face au perfectionnisme méthodique de la Vierge. Tu veux des résultats rapides mais la qualité prend du temps."
    elif lunar_asc in ['Taurus', 'Virgo', 'Capricorn']:
        tension = f"**Tensions possibles** : Triple terre ou double terre : {asc_tension}. Tu risques la paralysie par excès d'analyse, l'incapacité à passer à l'action par peur de l'imperfection."
    elif lunar_asc in ['Gemini', 'Libra', 'Aquarius']:
        tension = f"**Tensions possibles** : L'air intellectuel de {lunar_asc} multiplie les observations sans toujours agir. {asc_tension.capitalize()}. L'analyse remplace parfois l'action concrète."
    else:  # Cancer, Scorpio, Pisces
        tension = f"**Tensions possibles** : L'eau émotionnelle de {lunar_asc} complique l'analyse Vierge. {asc_tension.capitalize()}. Tu peux te perdre entre raison et ressenti."

    conseil = f"**Conseil clé** : Accepter le 'suffisamment bien' dans ce domaine. La perfection absolue est une illusion qui empêche de vivre et d'avancer."""

    interp = f"**Ton mois en un mot : {titre}**\n\n{intro}\n\n{domaine}\n\n{approche}\n\n{tension}\n\n{conseil}"

    # Weekly advice adapté
    week1 = f"Identifie CE qui mérite vraiment ton attention dans {theme['focus']}."
    week2 = f"Agis avec méthode sur cette priorité unique, sans te disperser."
    week3 = f"Maintiens le cap même si ce n'est pas encore parfait. Progresse."
    week4 = f"Évalue les progrès accomplis et célèbre le 'suffisamment bien'."

    return {
        'moon_sign': 'Virgo',
        'moon_house': moon_house,
        'lunar_ascendant': lunar_asc,
        'interpretation': interp,
        'weekly_advice': {
            'week_1': week1,
            'week_2': week2,
            'week_3': week3,
            'week_4': week4
        }
    }

def generate_all_144():
    """Génère les 144 interprétations Virgo"""
    batch = []
    ascendants = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                  'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

    for house in range(1, 13):
        for asc in ascendants:
            batch.append(generate_interpretation(house, asc))

    return batch

if __name__ == "__main__":
    from scripts.insert_lunar_v2_manual import insert_batch
    import asyncio

    batch = generate_all_144()
    print(f"✅ {len(batch)} interprétations Virgo générées")

    # Affichage d'un exemple
    print("\n📝 Exemple (Virgo M1 + Aries Asc):")
    print(batch[0]['interpretation'][:500] + "...")

    # Insertion
    print("\n🚀 Insertion en DB...")
    asyncio.run(insert_batch(batch))
    print("✅ Batch Virgo complet terminé")
