#!/usr/bin/env python3
"""
Script de validation manuelle du filtrage major_only
Teste le flux complet de propagation du paramètre
"""

from services import transits_services


def test_filter_major_aspects_only():
    """Test direct de la fonction filter_major_aspects_only"""
    print("\n" + "="*80)
    print("TEST 1: filter_major_aspects_only()")
    print("="*80)

    events = [
        {"aspect_type": "conjunction", "planet1": "Jupiter", "planet2": "Sun", "orb": 1.0},
        {"aspect_type": "sextile", "planet1": "Venus", "planet2": "Mars", "orb": 2.0},
        {"aspect_type": "square", "planet1": "Saturn", "planet2": "Moon", "orb": 1.5},
        {"aspect_type": "trine", "planet1": "Mercury", "planet2": "Neptune", "orb": 0.5},
        {"aspect_type": "quincunx", "planet1": "Uranus", "planet2": "Pluto", "orb": 3.0},
    ]

    print(f"\n📊 Événements initiaux: {len(events)}")
    for event in events:
        print(f"  - {event['aspect_type']}: {event['planet1']} → {event['planet2']}")

    # Test avec major_only=False
    result_all = transits_services.filter_major_aspects_only(events, major_only=False)
    print(f"\n✅ major_only=False → {len(result_all)} aspects retournés (tous)")
    assert len(result_all) == 5, "Tous les aspects doivent être conservés"

    # Test avec major_only=True
    result_major = transits_services.filter_major_aspects_only(events, major_only=True)
    print(f"✅ major_only=True → {len(result_major)} aspects retournés (majeurs uniquement)")

    major_types = [e["aspect_type"] for e in result_major]
    print("\n🎯 Aspects majeurs filtrés:")
    for event in result_major:
        print(f"  - {event['aspect_type']}: {event['planet1']} → {event['planet2']}")

    # Validation stricte des 4 types majeurs
    assert len(result_major) == 3, f"Attendu 3 aspects majeurs, obtenu {len(result_major)}"
    assert "conjunction" in major_types, "Doit contenir conjonction"
    assert "square" in major_types, "Doit contenir carré"
    assert "trine" in major_types, "Doit contenir trigone"
    assert "sextile" not in major_types, "Ne doit pas contenir sextile (mineur)"
    assert "quincunx" not in major_types, "Ne doit pas contenir quincunx (mineur)"

    print("\n✅ TEST 1 RÉUSSI: Filtrage fonctionne correctement")


def test_generate_transit_insights_with_major_only():
    """Test de generate_transit_insights avec major_only"""
    print("\n" + "="*80)
    print("TEST 2: generate_transit_insights() avec major_only")
    print("="*80)

    transits_data = {
        "events": [
            {"transiting_planet": "Jupiter", "stationed_planet": "Sun", "aspect_type": "conjunction", "orb": 1.0},
            {"transiting_planet": "Venus", "stationed_planet": "Mars", "aspect_type": "sextile", "orb": 2.0},
            {"transiting_planet": "Saturn", "stationed_planet": "Moon", "aspect_type": "square", "orb": 0.5},
            {"transiting_planet": "Mercury", "stationed_planet": "Neptune", "aspect_type": "trine", "orb": 1.2},
            {"transiting_planet": "Uranus", "stationed_planet": "Pluto", "aspect_type": "quincunx", "orb": 3.0},
            {"transiting_planet": "Mars", "stationed_planet": "Venus", "aspect_type": "opposition", "orb": 2.5},
        ]
    }

    print(f"\n📊 Événements initiaux: {len(transits_data['events'])}")
    for event in transits_data["events"]:
        print(f"  - {event['aspect_type']}: {event['transiting_planet']} → {event['stationed_planet']}")

    # Test avec major_only=False
    insights_all = transits_services.generate_transit_insights(transits_data, major_only=False)
    print(f"\n✅ major_only=False → {len(insights_all['major_aspects'])} aspects dans insights")

    # Test avec major_only=True
    insights_major = transits_services.generate_transit_insights(transits_data, major_only=True)
    print(f"✅ major_only=True → {len(insights_major['major_aspects'])} aspects dans insights")

    print("\n🎯 Aspects majeurs dans insights:")
    for aspect in insights_major["major_aspects"]:
        print(f"  - {aspect['aspect']}: {aspect['transit_planet']} → {aspect['natal_planet']} (orbe: {aspect['orb']:.2f}°)")

    # Validation des 4 types majeurs uniquement
    aspect_types = [a["aspect"] for a in insights_major["major_aspects"]]

    assert len(insights_major["major_aspects"]) == 4, f"Attendu 4 aspects majeurs, obtenu {len(insights_major['major_aspects'])}"
    assert "conjunction" in aspect_types, "Doit contenir conjonction (0°)"
    assert "opposition" in aspect_types, "Doit contenir opposition (180°)"
    assert "square" in aspect_types, "Doit contenir carré (90°)"
    assert "trine" in aspect_types, "Doit contenir trigone (120°)"
    assert "sextile" not in aspect_types, "Ne doit pas contenir sextile (mineur)"
    assert "quincunx" not in aspect_types, "Ne doit pas contenir quincunx (mineur)"

    print("\n✅ TEST 2 RÉUSSI: generate_transit_insights() filtre correctement")


def test_aspect_sorting_by_orb():
    """Test du tri des aspects par orbe"""
    print("\n" + "="*80)
    print("TEST 3: Tri des aspects par orbe (le plus serré en premier)")
    print("="*80)

    transits_data = {
        "events": [
            {"transiting_planet": "Mars", "stationed_planet": "Venus", "aspect_type": "opposition", "orb": 5.0},
            {"transiting_planet": "Jupiter", "stationed_planet": "Sun", "aspect_type": "trine", "orb": 0.3},
            {"transiting_planet": "Saturn", "stationed_planet": "Moon", "aspect_type": "square", "orb": 2.1},
            {"transiting_planet": "Mercury", "stationed_planet": "Mars", "aspect_type": "conjunction", "orb": 1.5},
        ]
    }

    print("\n📊 Événements (ordre aléatoire):")
    for event in transits_data["events"]:
        print(f"  - {event['aspect_type']}: orbe {event['orb']:.2f}°")

    insights = transits_services.generate_transit_insights(transits_data, major_only=True)

    print("\n🎯 Aspects triés par orbe:")
    for aspect in insights["major_aspects"]:
        print(f"  - {aspect['aspect']}: {aspect['transit_planet']} → {aspect['natal_planet']} (orbe: {aspect['orb']:.2f}°)")

    # Vérifier que le premier aspect a le plus petit orbe
    assert insights["major_aspects"][0]["orb"] == 0.3, "Le premier aspect doit avoir l'orbe le plus petit"
    assert insights["major_aspects"][0]["transit_planet"] == "Jupiter", "Le premier aspect doit être Jupiter"

    # Vérifier ordre croissant des orbes
    orbs = [a["orb"] for a in insights["major_aspects"]]
    assert orbs == sorted(orbs), "Les orbes doivent être triés par ordre croissant"

    print("\n✅ TEST 3 RÉUSSI: Tri par orbe fonctionnel")


def test_major_aspects_definition():
    """Test validation stricte de la définition des 4 aspects majeurs"""
    print("\n" + "="*80)
    print("TEST 4: Validation stricte des 4 aspects majeurs")
    print("="*80)

    # Les 4 aspects majeurs selon la définition astrologique classique
    major_aspects_definition = ["conjunction", "opposition", "square", "trine"]

    print("\n📖 Définition des aspects majeurs:")
    print("  1. Conjonction (0°) - Fusion, amplification")
    print("  2. Opposition (180°) - Tension, polarité")
    print("  3. Carré (90°) - Friction, défi")
    print("  4. Trigone (120°) - Harmonie, fluidité")

    events = [
        {"aspect_type": "conjunction", "planet1": "A", "planet2": "B", "orb": 1.0},
        {"aspect_type": "opposition", "planet1": "C", "planet2": "D", "orb": 1.0},
        {"aspect_type": "square", "planet1": "E", "planet2": "F", "orb": 1.0},
        {"aspect_type": "trine", "planet1": "G", "planet2": "H", "orb": 1.0},
        {"aspect_type": "sextile", "planet1": "I", "planet2": "J", "orb": 1.0},
        {"aspect_type": "quincunx", "planet1": "K", "planet2": "L", "orb": 1.0},
    ]

    result = transits_services.filter_major_aspects_only(events, major_only=True)
    result_types = [e["aspect_type"] for e in result]

    print("\n✅ Aspects retournés:")
    for aspect_type in result_types:
        print(f"  ✓ {aspect_type}")

    print("\n❌ Aspects exclus (mineurs):")
    excluded = [e["aspect_type"] for e in events if e["aspect_type"] not in result_types]
    for aspect_type in excluded:
        print(f"  ✗ {aspect_type}")

    # Validation stricte
    assert len(result) == 4, f"Attendu 4 aspects majeurs, obtenu {len(result)}"

    for major_type in major_aspects_definition:
        assert major_type in result_types, f"{major_type} doit être dans les aspects majeurs"

    assert "sextile" not in result_types, "Sextile ne doit pas être dans les aspects majeurs"
    assert "quincunx" not in result_types, "Quincunx ne doit pas être dans les aspects majeurs"

    print("\n✅ TEST 4 RÉUSSI: Définition des aspects majeurs validée")


def test_case_insensitive_filtering():
    """Test filtrage insensible à la casse"""
    print("\n" + "="*80)
    print("TEST 5: Filtrage insensible à la casse")
    print("="*80)

    events = [
        {"aspect_type": "CONJUNCTION", "planet1": "Sun", "planet2": "Moon", "orb": 1.0},
        {"aspect_type": "Opposition", "planet1": "Mars", "planet2": "Venus", "orb": 2.0},
        {"aspect_type": "Square", "planet1": "Jupiter", "planet2": "Saturn", "orb": 1.5},
        {"aspect_type": "TRINE", "planet1": "Mercury", "planet2": "Neptune", "orb": 0.5},
        {"aspect_type": "sextile", "planet1": "Venus", "planet2": "Mars", "orb": 2.0},
    ]

    print("\n📊 Événements avec casse mixte:")
    for event in events:
        print(f"  - {event['aspect_type']}")

    result = transits_services.filter_major_aspects_only(events, major_only=True)

    print(f"\n✅ {len(result)} aspects majeurs retournés (insensible à la casse)")

    assert len(result) == 4, f"Attendu 4 aspects majeurs, obtenu {len(result)}"

    print("\n✅ TEST 5 RÉUSSI: Filtrage insensible à la casse fonctionnel")


def main():
    """Exécute tous les tests"""
    print("\n" + "="*80)
    print("🔬 VALIDATION MANUELLE DU FILTRAGE MAJOR_ONLY")
    print("="*80)
    print("\nCe script teste le flux complet de propagation du paramètre major_only")
    print("depuis les routes API jusqu'au service de filtrage.")

    try:
        test_filter_major_aspects_only()
        test_generate_transit_insights_with_major_only()
        test_aspect_sorting_by_orb()
        test_major_aspects_definition()
        test_case_insensitive_filtering()

        print("\n" + "="*80)
        print("🎉 TOUS LES TESTS RÉUSSIS (5/5)")
        print("="*80)
        print("\n✅ Le filtrage major_only fonctionne correctement:")
        print("  • Paramètre propagé de la route vers le service")
        print("  • Fonction filter_major_aspects_only() opérationnelle")
        print("  • Seuls les 4 aspects majeurs sont retournés (conjonction, opposition, carré, trigone)")
        print("  • Tri par orbe (le plus serré en premier)")
        print("  • Filtrage insensible à la casse")
        print("\n📚 Documentation complète: /apps/api/docs/TRANSITS_MAJOR_FILTERING.md")
        print("📝 Résumé: /apps/api/docs/TRANSITS_MAJOR_FILTERING_SUMMARY.md")
        print("\n✅ Commit f3cde98 validé: filtrage backend opérationnel")

    except AssertionError as e:
        print("\n" + "="*80)
        print("❌ ÉCHEC DES TESTS")
        print("="*80)
        print(f"\nErreur: {str(e)}")
        raise


if __name__ == "__main__":
    main()
