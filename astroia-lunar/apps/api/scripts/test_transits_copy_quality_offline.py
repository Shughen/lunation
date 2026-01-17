#!/usr/bin/env python
"""
Script de test pour auditer la qualité des interprétations de transits (Tâche 4.4)
VERSION OFFLINE - utilise les services directement sans appel API externe

Ce script :
1. Génère des transits via les services internes avec major_only=true
2. Analyse la structure des insights (summary, manifestation, why, advice)
3. Évalue la qualité du copy selon les critères MVP
4. Valide le filtrage des aspects majeurs uniquement
5. Produit une checklist de validation et des recommandations
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

# Ajouter le répertoire parent au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.aspect_explanation_service import (
    enrich_aspects_v4,
    MAJOR_ASPECT_TYPES
)

# === CONSTANTES ===

# Mots ésotériques à compter
ESOTERIC_WORDS = [
    'énergie', 'énergies', 'vibration', 'vibrations', 'manifestation',
    'univers', 'cosmos', 'mystique', 'magique', 'spirituel', 'karma',
    'chakra', 'aura', 'éveillé', 'conscience supérieure', 'destinée',
    'cosmique', 'transcendance', 'illumination', 'sacré'
]

# === DONNÉES DE TEST ===

# Aspects bruts simulés (comme retournés par RapidAPI)
TEST_ASPECTS = [
    # Aspects majeurs (doivent être retenus)
    {'planet1': 'Sun', 'planet2': 'Moon', 'type': 'conjunction', 'orb': 2.3},
    {'planet1': 'Mars', 'planet2': 'Jupiter', 'type': 'square', 'orb': 3.5},
    {'planet1': 'Venus', 'planet2': 'Saturn', 'type': 'trine', 'orb': 1.8},
    {'planet1': 'Mercury', 'planet2': 'Pluto', 'type': 'opposition', 'orb': 4.2},
    {'planet1': 'Moon', 'planet2': 'Uranus', 'type': 'square', 'orb': 2.9},
    {'planet1': 'Sun', 'planet2': 'Jupiter', 'type': 'trine', 'orb': 0.5},
    {'planet1': 'Venus', 'planet2': 'Mars', 'type': 'opposition', 'orb': 5.1},

    # Aspects mineurs (doivent être filtrés si major_only=True)
    {'planet1': 'Sun', 'planet2': 'Venus', 'type': 'sextile', 'orb': 2.0},
    {'planet1': 'Moon', 'planet2': 'Neptune', 'type': 'quincunx', 'orb': 1.5},
    {'planet1': 'Mars', 'planet2': 'Saturn', 'type': 'semi-square', 'orb': 3.0},

    # Aspects hors orbe (doivent être filtrés)
    {'planet1': 'Mercury', 'planet2': 'Jupiter', 'type': 'conjunction', 'orb': 8.5},

    # Aspects avec Lilith (doivent être filtrés)
    {'planet1': 'Mean_Lilith', 'planet2': 'Sun', 'type': 'conjunction', 'orb': 1.0},
]

# Données planétaires simulées
TEST_PLANETS_DATA = {
    'sun': {'sign': 'Taurus', 'house': 2, 'degree': 45.0, 'longitude': 45.0},
    'moon': {'sign': 'Taurus', 'house': 2, 'degree': 47.3, 'longitude': 47.3},
    'mercury': {'sign': 'Gemini', 'house': 3, 'degree': 75.0, 'longitude': 75.0},
    'venus': {'sign': 'Pisces', 'house': 12, 'degree': 350.0, 'longitude': 350.0},
    'mars': {'sign': 'Aries', 'house': 1, 'degree': 15.0, 'longitude': 15.0},
    'jupiter': {'sign': 'Leo', 'house': 5, 'degree': 135.5, 'longitude': 135.5},
    'saturn': {'sign': 'Capricorn', 'house': 10, 'degree': 285.0, 'longitude': 285.0},
    'uranus': {'sign': 'Aquarius', 'house': 11, 'degree': 315.0, 'longitude': 315.0},
    'neptune': {'sign': 'Pisces', 'house': 12, 'degree': 345.0, 'longitude': 345.0},
    'pluto': {'sign': 'Scorpio', 'house': 8, 'degree': 225.0, 'longitude': 225.0},
}

# === FONCTIONS D'ANALYSE ===

def count_words(text: str) -> int:
    """Compte le nombre de mots dans un texte"""
    return len(text.split())


def count_esoteric_words(text: str) -> tuple[int, List[str]]:
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


def analyze_insight_structure(insight: Dict[str, Any], index: int) -> Dict[str, Any]:
    """
    Analyse la structure d'un insight de transit

    Vérifie :
    - Présence des 4 champs requis (summary, manifestation, why, advice)
    - Longueur des textes
    - Qualité du contenu
    """
    print(f"\n{'─'*80}")
    print(f"🔍 INSIGHT #{index + 1}")
    print(f"{'─'*80}")

    # Informations de base
    aspect_type = insight.get('type', 'N/A')
    planet1 = insight.get('planet1', 'N/A')
    planet2 = insight.get('planet2', 'N/A')
    orb = insight.get('orb', 0)

    print(f"\n📌 Aspect : {planet1} {aspect_type} {planet2} (orbe: {abs(orb):.2f}°)")

    # Récupérer le copy
    copy_data = insight.get('copy', {})

    # Vérifier la présence des champs requis
    required_fields = ['summary', 'manifestation', 'why', 'advice']
    present_fields = [field for field in required_fields if field in copy_data and copy_data[field]]
    missing_fields = [field for field in required_fields if field not in present_fields]

    print(f"\n✓ Structure")
    print(f"  Champs présents : {len(present_fields)}/4")
    for field in required_fields:
        status = "✅" if field in present_fields else "❌"
        print(f"    {status} {field}")

    # Analyse détaillée de chaque champ
    analysis = {
        'type': aspect_type,
        'planet1': planet1,
        'planet2': planet2,
        'orb': orb,
        'fields_present': len(present_fields),
        'fields_missing': missing_fields,
        'field_analysis': {}
    }

    # Summary
    if 'summary' in copy_data:
        summary = copy_data['summary']
        summary_words = count_words(summary)
        print(f"\n✓ Summary ({summary_words} mots, {len(summary)} chars)")
        print(f"  \"{summary}\"")
        analysis['field_analysis']['summary'] = {
            'present': True,
            'length_words': summary_words,
            'length_chars': len(summary),
            'content': summary
        }
    else:
        print(f"\n❌ Summary : MANQUANT")
        analysis['field_analysis']['summary'] = {'present': False}

    # Why
    if 'why' in copy_data:
        why = copy_data['why']
        if isinstance(why, list):
            print(f"\n✓ Why ({len(why)} points)")
            for i, point in enumerate(why, 1):
                print(f"  {i}. {point}")
            analysis['field_analysis']['why'] = {
                'present': True,
                'num_points': len(why),
                'content': why
            }
        else:
            print(f"\n⚠️ Why : format incorrect (devrait être une liste)")
            print(f"  {why}")
            analysis['field_analysis']['why'] = {
                'present': True,
                'format_error': True,
                'content': why
            }
    else:
        print(f"\n❌ Why : MANQUANT")
        analysis['field_analysis']['why'] = {'present': False}

    # Manifestation
    if 'manifestation' in copy_data:
        manifestation = copy_data['manifestation']
        manif_words = count_words(manifestation)
        print(f"\n✓ Manifestation ({manif_words} mots, {len(manifestation)} chars)")
        print(f"  {manifestation[:150]}...")

        # Vérifier si contient des exemples concrets
        concrete_indicators = ['concrètement', 'exemple', 'par exemple', 'situation', 'contexte']
        has_concrete = any(ind in manifestation.lower() for ind in concrete_indicators)

        analysis['field_analysis']['manifestation'] = {
            'present': True,
            'length_words': manif_words,
            'length_chars': len(manifestation),
            'has_concrete_examples': has_concrete,
            'content': manifestation
        }

        if has_concrete:
            print(f"  ✅ Contient des exemples concrets")
        else:
            print(f"  ⚠️ Pourrait bénéficier d'exemples plus concrets")
    else:
        print(f"\n❌ Manifestation : MANQUANT")
        analysis['field_analysis']['manifestation'] = {'present': False}

    # Advice
    if 'advice' in copy_data:
        advice = copy_data['advice']
        if advice:  # Peut être None
            advice_words = count_words(advice)
            print(f"\n✓ Advice ({advice_words} mots)")
            print(f"  \"{advice}\"")

            # Vérifier si actionnable
            action_verbs = ['observer', 'chercher', 'utiliser', 'mobiliser', 'cultiver', 'développer', 'éviter', 'pratiquer']
            is_actionable = any(verb in advice.lower() for verb in action_verbs)

            analysis['field_analysis']['advice'] = {
                'present': True,
                'length_words': advice_words,
                'is_actionable': is_actionable,
                'content': advice
            }

            if is_actionable:
                print(f"  ✅ Conseil actionnable")
            else:
                print(f"  ⚠️ Pourrait être plus actionnable")
        else:
            print(f"\n✓ Advice : None (optionnel)")
            analysis['field_analysis']['advice'] = {'present': True, 'is_null': True}
    else:
        print(f"\n❌ Advice : MANQUANT")
        analysis['field_analysis']['advice'] = {'present': False}

    # Analyse du langage ésotérique
    all_text = ' '.join([
        copy_data.get('summary', ''),
        ' '.join(copy_data.get('why', [])) if isinstance(copy_data.get('why'), list) else str(copy_data.get('why', '')),
        copy_data.get('manifestation', ''),
        copy_data.get('advice', '') or ''
    ])

    esoteric_count, esoteric_found = count_esoteric_words(all_text)
    analysis['esoteric_words'] = {
        'count': esoteric_count,
        'found': esoteric_found
    }

    print(f"\n✓ Langage ésotérique : {esoteric_count} mots")
    if esoteric_found:
        print(f"  Trouvés : {', '.join(esoteric_found)}")

    return analysis


def generate_transits_offline() -> List[Dict[str, Any]]:
    """Génère des transits via les services internes"""
    print(f"\n{'='*80}")
    print(f"📡 GÉNÉRATION DES TRANSITS (MODE OFFLINE)")
    print(f"{'='*80}")

    print(f"\n🔧 Aspects bruts : {len(TEST_ASPECTS)}")
    print(f"🔧 Filtrage : major_only=True (4 types majeurs uniquement)")
    print(f"🔧 Orbe max : 6°")
    print(f"🔧 Exclure : Lilith")

    # Utiliser le service d'enrichissement
    enriched_aspects = enrich_aspects_v4(
        aspects=TEST_ASPECTS,
        planets_data=TEST_PLANETS_DATA,
        limit=10
    )

    print(f"\n✅ Aspects enrichis : {len(enriched_aspects)}")

    # Sauvegarder les aspects enrichis
    output_file = Path(__file__).parent / "transits_enriched_sample.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(enriched_aspects, f, indent=2, ensure_ascii=False)
    print(f"💾 Aspects sauvegardés : {output_file}")

    return enriched_aspects


def validate_major_aspects_only(insights: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Valide que seuls les aspects majeurs sont présents"""
    print(f"\n{'='*80}")
    print(f"🎯 VALIDATION DES ASPECTS MAJEURS")
    print(f"{'='*80}")

    aspect_types = {}
    non_major_aspects = []

    for insight in insights:
        aspect_type = insight.get('type', '').lower()
        aspect_types[aspect_type] = aspect_types.get(aspect_type, 0) + 1

        if aspect_type not in MAJOR_ASPECT_TYPES:
            non_major_aspects.append(insight)

    print(f"\n📊 Distribution des types d'aspects ({len(insights)} total)")
    for aspect_type, count in sorted(aspect_types.items()):
        is_major = aspect_type in MAJOR_ASPECT_TYPES
        status = "✅" if is_major else "❌"
        print(f"  {status} {aspect_type}: {count}")

    if non_major_aspects:
        print(f"\n❌ ASPECTS NON-MAJEURS DÉTECTÉS ({len(non_major_aspects)}):")
        for aspect in non_major_aspects:
            print(f"  - {aspect.get('planet1')} {aspect.get('type')} {aspect.get('planet2')}")
    else:
        print(f"\n✅ TOUS LES ASPECTS SONT MAJEURS")

    return {
        'total_aspects': len(insights),
        'aspect_types': aspect_types,
        'non_major_count': len(non_major_aspects),
        'all_major': len(non_major_aspects) == 0
    }


def create_validation_checklist(
    aspects_validation: Dict[str, Any],
    insights_analysis: List[Dict[str, Any]]
) -> Dict[str, bool]:
    """Crée la checklist de validation MVP"""
    print(f"\n{'='*80}")
    print(f"✅ CHECKLIST DE VALIDATION MVP")
    print(f"{'='*80}")

    checklist = {}

    # 1. Uniquement aspects majeurs
    all_major = aspects_validation['all_major']
    checklist['only_major_aspects'] = all_major
    print(f"\n{'✅' if all_major else '❌'} Uniquement aspects majeurs (4 types)")

    # 2. Structure des insights (4 champs présents)
    all_have_4_fields = all(
        analysis['fields_present'] == 4
        for analysis in insights_analysis
    )
    checklist['all_insights_have_4_fields'] = all_have_4_fields
    print(f"{'✅' if all_have_4_fields else '❌'} Tous les insights ont 4 champs (summary, manifestation, why, advice)")

    # 3. Explication factuelle et accessible
    avg_esoteric = sum(a['esoteric_words']['count'] for a in insights_analysis) / max(len(insights_analysis), 1)
    is_factual = avg_esoteric <= 2
    checklist['factual_and_accessible'] = is_factual
    print(f"{'✅' if is_factual else '⚠️'} Explication factuelle et accessible (mots ésotériques: {avg_esoteric:.1f} moy.)")

    # 4. Manifestations concrètes
    concrete_count = sum(
        1 for a in insights_analysis
        if a.get('field_analysis', {}).get('manifestation', {}).get('has_concrete_examples', False)
    )
    has_concrete = concrete_count >= len(insights_analysis) * 0.7  # Au moins 70%
    checklist['concrete_manifestations'] = has_concrete
    print(f"{'✅' if has_concrete else '⚠️'} Manifestations concrètes ({concrete_count}/{len(insights_analysis)} insights)")

    # 5. Conseils pratiques
    actionable_count = sum(
        1 for a in insights_analysis
        if a.get('field_analysis', {}).get('advice', {}).get('is_actionable', False)
    )
    has_actionable = actionable_count >= len(insights_analysis) * 0.7  # Au moins 70%
    checklist['practical_advice'] = has_actionable
    print(f"{'✅' if has_actionable else '⚠️'} Conseils pratiques ({actionable_count}/{len(insights_analysis)} insights)")

    # Score global
    score = sum(1 for v in checklist.values() if v)
    total = len(checklist)
    print(f"\n{'='*80}")
    print(f"📊 SCORE GLOBAL : {score}/{total} ({score/total*100:.0f}%)")
    print(f"{'='*80}")

    return checklist


def generate_recommendations(
    checklist: Dict[str, bool],
    insights_analysis: List[Dict[str, Any]]
) -> List[str]:
    """Génère des recommandations d'amélioration"""
    print(f"\n{'='*80}")
    print(f"💡 RECOMMANDATIONS")
    print(f"{'='*80}")

    recommendations = []

    if not checklist.get('only_major_aspects', True):
        rec = "🔧 Filtrer strictement les aspects pour ne garder que les 4 types majeurs (conjunction, opposition, square, trine)"
        recommendations.append(rec)
        print(f"\n{rec}")

    if not checklist.get('all_insights_have_4_fields', True):
        rec = "🔧 Assurer la présence des 4 champs requis dans tous les insights (summary, manifestation, why, advice)"
        recommendations.append(rec)
        print(f"\n{rec}")

    if not checklist.get('factual_and_accessible', True):
        rec = "🔧 Réduire l'usage de termes ésotériques, privilégier un langage factuel et accessible"
        recommendations.append(rec)
        print(f"\n{rec}")

    if not checklist.get('concrete_manifestations', True):
        rec = "🔧 Enrichir les manifestations avec plus d'exemples concrets et situations observables"
        recommendations.append(rec)
        print(f"\n{rec}")

    if not checklist.get('practical_advice', True):
        rec = "🔧 Rendre les conseils plus actionnables avec des verbes d'action clairs"
        recommendations.append(rec)
        print(f"\n{rec}")

    # Analyse qualitative des textes
    avg_manif_length = sum(
        a.get('field_analysis', {}).get('manifestation', {}).get('length_words', 0)
        for a in insights_analysis
    ) / max(len(insights_analysis), 1)

    if avg_manif_length < 40:
        rec = f"🔧 Manifestations assez courtes ({avg_manif_length:.0f} mots moy.), considérer d'ajouter plus de détails"
        recommendations.append(rec)
        print(f"\n{rec}")
    elif avg_manif_length > 100:
        rec = f"🔧 Manifestations assez longues ({avg_manif_length:.0f} mots moy.), considérer de condenser"
        recommendations.append(rec)
        print(f"\n{rec}")

    if not recommendations:
        print(f"\n✅ Aucune recommandation : la qualité du copy est conforme aux critères MVP !")

    return recommendations


def main():
    """Fonction principale"""
    print(f"\n{'='*80}")
    print(f"🌙 AUDIT QUALITÉ COPY INTERPRÉTATIONS TRANSITS (Tâche 4.4)")
    print(f"{'='*80}")
    print(f"\nDate : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        # 1. Générer les transits (offline)
        enriched_aspects = generate_transits_offline()

        if not enriched_aspects:
            print(f"\n⚠️ Aucun aspect enrichi généré")
            return

        # 2. Valider filtrage aspects majeurs
        aspects_validation = validate_major_aspects_only(enriched_aspects)

        # 3. Analyser chaque insight
        print(f"\n{'='*80}")
        print(f"🔍 ANALYSE DÉTAILLÉE DES INSIGHTS")
        print(f"{'='*80}")

        insights_analysis = []
        for i, insight in enumerate(enriched_aspects):
            analysis = analyze_insight_structure(insight, i)
            insights_analysis.append(analysis)

        # 4. Créer checklist de validation
        checklist = create_validation_checklist(aspects_validation, insights_analysis)

        # 5. Générer recommandations
        recommendations = generate_recommendations(checklist, insights_analysis)

        # Sauvegarder le rapport d'analyse
        report = {
            'date': datetime.now().isoformat(),
            'aspects_validation': aspects_validation,
            'insights_count': len(enriched_aspects),
            'insights_analysis': insights_analysis,
            'checklist': checklist,
            'recommendations': recommendations
        }

        report_file = Path(__file__).parent / "transits_copy_quality_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"\n{'='*80}")
        print(f"💾 Rapport d'analyse sauvegardé : {report_file}")
        print(f"{'='*80}\n")

    except Exception as e:
        print(f"\n❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
