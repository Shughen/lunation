#!/usr/bin/env python
"""
Script de test pour valider le format des rapports lunaires (Chantier 2)

Ce script génère des rapports échantillons pour différentes configurations
et mesure leur conformité aux critères MVP :
- 3 sections identifiables
- Ton factuel, non ésotérique
- Longueur 300-800 mots
- Contenu actionnable
"""

import sys
from datetime import datetime, date, timezone
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.lunar_report_builder import build_lunar_report_v4
from models.lunar_return import LunarReturn


# Mots ésotériques à compter
ESOTERIC_WORDS = [
    'énergie', 'énergies', 'vibration', 'vibrations', 'manifestation',
    'univers', 'cosmos', 'mystique', 'magique', 'spirituel', 'karma',
    'chakra', 'aura', 'éveillé', 'conscience supérieure'
]


class MockLunarReturn:
    """Mock objet LunarReturn pour tests"""
    def __init__(self, month, return_date, moon_sign, moon_house, lunar_ascendant, aspects=None, planets=None):
        self.id = 1
        self.user_id = 1
        self.month = month
        self.return_date = return_date
        self.moon_sign = moon_sign
        self.moon_house = moon_house
        self.lunar_ascendant = lunar_ascendant
        self.aspects = aspects or []
        self.planets = planets or {}
        self.houses = {}
        self.raw_data = {}
        self.interpretation = None


def count_words(text):
    """Compte le nombre de mots dans un texte"""
    return len(text.split())


def count_esoteric_words(text):
    """Compte les occurrences de mots ésotériques"""
    text_lower = text.lower()
    count = 0
    found = []
    for word in ESOTERIC_WORDS:
        occurrences = text_lower.count(word)
        if occurrences > 0:
            count += occurrences
            found.append(f"{word} ({occurrences}x)")
    return count, found


def analyze_report(report, config_name):
    """Analyse un rapport et affiche les métriques"""
    print(f"\n{'='*80}")
    print(f"Configuration : {config_name}")
    print(f"{'='*80}")

    # Header
    header = report.get('header', {})
    print(f"\n📋 HEADER")
    print(f"  Mois : {header.get('month')}")
    print(f"  Dates : {header.get('dates')}")
    print(f"  Lune : {header.get('moon_sign')} en Maison {header.get('moon_house')}")
    print(f"  Ascendant lunaire : {header.get('lunar_ascendant')}")

    # Climat général
    climate = report.get('general_climate', '')
    print(f"\n🌙 CLIMAT GÉNÉRAL DU MOIS")
    print(f"  Longueur : {count_words(climate)} mots")
    print(f"  Texte : {climate[:200]}...")

    # Axes dominants
    axes = report.get('dominant_axes', [])
    print(f"\n🎯 AXES DOMINANTS")
    print(f"  Nombre d'axes : {len(axes)}")
    for i, axis in enumerate(axes, 1):
        print(f"  {i}. {axis}")

    # Aspects majeurs
    aspects = report.get('major_aspects', [])
    print(f"\n⭐ ASPECTS MAJEURS")
    print(f"  Nombre d'aspects : {len(aspects)}")
    for i, aspect in enumerate(aspects[:3], 1):  # Afficher les 3 premiers
        print(f"\n  Aspect {i}: {aspect.get('planet1')} {aspect.get('type')} {aspect.get('planet2')} (orbe: {aspect.get('orb')}°)")
        copy_data = aspect.get('copy', {})
        if copy_data.get('summary'):
            print(f"    Summary: {copy_data['summary']}")
        if copy_data.get('manifestation'):
            print(f"    Manifestation ({count_words(copy_data['manifestation'])} mots): {copy_data['manifestation'][:150]}...")
        if copy_data.get('why'):
            why_text = ' ; '.join(copy_data['why']) if isinstance(copy_data['why'], list) else copy_data['why']
            print(f"    Why: {why_text[:100]}...")
        if copy_data.get('advice'):
            print(f"    Advice: {copy_data['advice'][:100]}...")

    # Métriques MVP
    print(f"\n📊 MÉTRIQUES MVP")

    # Longueur totale (inclure tous les champs copy)
    total_text = climate + ' '.join(axes)
    for aspect in aspects:
        copy_data = aspect.get('copy', {})
        if copy_data.get('summary'):
            total_text += ' ' + copy_data['summary']
        if copy_data.get('manifestation'):
            total_text += ' ' + copy_data['manifestation']
        if copy_data.get('why'):
            if isinstance(copy_data['why'], list):
                total_text += ' ' + ' '.join(copy_data['why'])
            else:
                total_text += ' ' + copy_data['why']
        if copy_data.get('advice'):
            total_text += ' ' + copy_data['advice']
    total_words = count_words(total_text)

    print(f"  Longueur totale : {total_words} mots", end='')
    if 300 <= total_words <= 800:
        print(" ✅")
    else:
        print(f" ⚠️ (attendu: 300-800)")

    # Sections identifiables
    sections = ['header', 'general_climate', 'dominant_axes', 'major_aspects']
    sections_present = sum(1 for s in sections if report.get(s))
    print(f"  Sections présentes : {sections_present}/4 ✅")

    # Mots ésotériques
    esoteric_count, found = count_esoteric_words(total_text)
    print(f"  Mots ésotériques : {esoteric_count}", end='')
    if esoteric_count <= 2:
        print(" ✅")
    else:
        print(f" ⚠️ (attendu: ≤ 2)")
        if found:
            print(f"    Trouvés : {', '.join(found)}")

    # Contenu actionnable
    has_dates = any(str(aspect.get('orb', 0)) for aspect in aspects)
    has_recommendations = any('attention' in axis.lower() or 'besoin' in axis.lower() for axis in axes)
    actionable = has_dates or has_recommendations
    print(f"  Contenu actionnable : {'✅' if actionable else '⚠️'}")

    return {
        'config': config_name,
        'total_words': total_words,
        'esoteric_count': esoteric_count,
        'sections': sections_present,
        'actionable': actionable
    }


def main():
    """Génère et analyse plusieurs rapports échantillons"""

    print("🌙 Test du format des rapports lunaires (Chantier 2)")
    print("=" * 80)

    # Configurations de test
    configs = [
        {
            'name': 'Bélier Maison 1 (Action)',
            'month': '2026-01',
            'moon_sign': 'Aries',
            'moon_house': 1,
            'lunar_ascendant': 'Gemini',
            'aspects': [
                {'planet1': 'Moon', 'planet2': 'Mars', 'type': 'conjunction', 'orb': 2.3},
                {'planet1': 'Moon', 'planet2': 'Sun', 'type': 'square', 'orb': 4.1},
                {'planet1': 'Venus', 'planet2': 'Jupiter', 'type': 'trine', 'orb': 3.5},
            ],
            'planets': {
                'Moon': {'sign': 'Aries', 'house': 1, 'degree': 15.5, 'longitude': 15.5},
                'Mars': {'sign': 'Aries', 'house': 1, 'degree': 13.2, 'longitude': 13.2},
                'Sun': {'sign': 'Cancer', 'house': 4, 'degree': 105.5, 'longitude': 105.5},
                'Venus': {'sign': 'Pisces', 'house': 12, 'degree': 350.0, 'longitude': 350.0},
                'Jupiter': {'sign': 'Scorpio', 'house': 8, 'degree': 230.0, 'longitude': 230.0},
            }
        },
        {
            'name': 'Taureau Maison 2 (Stabilité)',
            'month': '2026-02',
            'moon_sign': 'Taurus',
            'moon_house': 2,
            'lunar_ascendant': 'Virgo',
            'aspects': [
                {'planet1': 'Moon', 'planet2': 'Venus', 'type': 'trine', 'orb': 1.5},
                {'planet1': 'Sun', 'planet2': 'Saturn', 'type': 'square', 'orb': 2.8},
            ],
            'planets': {
                'Moon': {'sign': 'Taurus', 'house': 2, 'degree': 45.0, 'longitude': 45.0},
                'Venus': {'sign': 'Capricorn', 'house': 10, 'degree': 285.0, 'longitude': 285.0},
                'Sun': {'sign': 'Aquarius', 'house': 11, 'degree': 315.0, 'longitude': 315.0},
                'Saturn': {'sign': 'Taurus', 'house': 2, 'degree': 45.0, 'longitude': 45.0},
            }
        },
        {
            'name': 'Gémeaux Maison 3 (Communication)',
            'month': '2026-03',
            'moon_sign': 'Gemini',
            'moon_house': 3,
            'lunar_ascendant': 'Aquarius',
            'aspects': [
                {'planet1': 'Moon', 'planet2': 'Mercury', 'type': 'conjunction', 'orb': 0.8},
                {'planet1': 'Moon', 'planet2': 'Jupiter', 'type': 'opposition', 'orb': 5.2},
                {'planet1': 'Mars', 'planet2': 'Neptune', 'type': 'square', 'orb': 4.0},
            ],
            'planets': {
                'Moon': {'sign': 'Gemini', 'house': 3, 'degree': 75.0, 'longitude': 75.0},
                'Mercury': {'sign': 'Gemini', 'house': 3, 'degree': 74.2, 'longitude': 74.2},
                'Jupiter': {'sign': 'Sagittarius', 'house': 9, 'degree': 255.0, 'longitude': 255.0},
                'Mars': {'sign': 'Virgo', 'house': 6, 'degree': 165.0, 'longitude': 165.0},
                'Neptune': {'sign': 'Pisces', 'house': 12, 'degree': 345.0, 'longitude': 345.0},
            }
        },
    ]

    results = []

    for config in configs:
        # Créer mock LunarReturn
        return_date = datetime(2026, int(config['month'].split('-')[1]), 15, 12, 0, 0, tzinfo=timezone.utc)

        mock_return = MockLunarReturn(
            month=config['month'],
            return_date=return_date,
            moon_sign=config['moon_sign'],
            moon_house=config['moon_house'],
            lunar_ascendant=config['lunar_ascendant'],
            aspects=config['aspects'],
            planets=config.get('planets', {})
        )

        # Générer rapport
        report = build_lunar_report_v4(mock_return)

        # Analyser
        result = analyze_report(report, config['name'])
        results.append(result)

    # Synthèse finale
    print(f"\n{'='*80}")
    print("📊 SYNTHÈSE FINALE")
    print(f"{'='*80}")

    all_pass = True
    for result in results:
        status = "✅" if (
            300 <= result['total_words'] <= 800 and
            result['esoteric_count'] <= 2 and
            result['sections'] >= 3
        ) else "⚠️"

        print(f"{status} {result['config']}: {result['total_words']} mots, "
              f"{result['esoteric_count']} mots ésotériques")

        if status == "⚠️":
            all_pass = False

    print(f"\n{'='*80}")
    if all_pass:
        print("✅ TOUS LES CRITÈRES MVP SONT RESPECTÉS")
    else:
        print("⚠️ AJUSTEMENTS NÉCESSAIRES (voir détails ci-dessus)")
    print(f"{'='*80}\n")


if __name__ == '__main__':
    main()
