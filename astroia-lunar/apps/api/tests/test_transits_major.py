"""
Tests pour le filtrage des transits majeurs (major_only)
Valide que seuls les 4 aspects majeurs sont retournés quand major_only=true

IMPORTANT: Ces tests sont des tests unitaires purs qui n'utilisent pas la DB.
Ils ne dépendent pas de conftest.py et peuvent s'exécuter de manière isolée.
"""

import pytest
from services import transits_services


# --- Tests unitaires de la fonction filter_major_aspects_only ---

def test_filter_major_aspects_only_all_major():
    """Test filtrage avec tous aspects majeurs - aucun filtré"""
    events = [
        {"aspect_type": "conjunction", "planet1": "Sun", "planet2": "Moon", "orb": 1.0},
        {"aspect_type": "opposition", "planet1": "Mars", "planet2": "Venus", "orb": 2.0},
        {"aspect_type": "square", "planet1": "Jupiter", "planet2": "Saturn", "orb": 1.5},
        {"aspect_type": "trine", "planet1": "Mercury", "planet2": "Neptune", "orb": 0.5},
    ]

    result = transits_services.filter_major_aspects_only(events, major_only=True)

    assert len(result) == 4, "Tous les aspects majeurs doivent être conservés"


def test_filter_major_aspects_only_mixed():
    """Test filtrage avec aspects majeurs et mineurs - seuls majeurs conservés"""
    events = [
        {"aspect_type": "conjunction", "planet1": "Sun", "planet2": "Moon", "orb": 1.0},
        {"aspect_type": "sextile", "planet1": "Venus", "planet2": "Mars", "orb": 2.0},  # Mineur
        {"aspect_type": "square", "planet1": "Jupiter", "planet2": "Saturn", "orb": 1.5},
        {"aspect_type": "quincunx", "planet1": "Uranus", "planet2": "Pluto", "orb": 3.0},  # Mineur
        {"aspect_type": "trine", "planet1": "Mercury", "planet2": "Neptune", "orb": 0.5},
        {"aspect_type": "semisextile", "planet1": "Moon", "planet2": "Sun", "orb": 1.0},  # Mineur
    ]

    result = transits_services.filter_major_aspects_only(events, major_only=True)

    assert len(result) == 3, "Seuls les 3 aspects majeurs doivent être conservés"
    aspect_types = [e["aspect_type"] for e in result]
    assert "conjunction" in aspect_types
    assert "square" in aspect_types
    assert "trine" in aspect_types
    assert "sextile" not in aspect_types
    assert "quincunx" not in aspect_types
    assert "semisextile" not in aspect_types


def test_filter_major_aspects_only_disabled():
    """Test filtrage désactivé (major_only=False) - tous aspects conservés"""
    events = [
        {"aspect_type": "conjunction", "planet1": "Sun", "planet2": "Moon", "orb": 1.0},
        {"aspect_type": "sextile", "planet1": "Venus", "planet2": "Mars", "orb": 2.0},
        {"aspect_type": "quincunx", "planet1": "Uranus", "planet2": "Pluto", "orb": 3.0},
    ]

    result = transits_services.filter_major_aspects_only(events, major_only=False)

    assert len(result) == 3, "Tous les aspects doivent être conservés quand major_only=False"


def test_filter_major_aspects_only_case_insensitive():
    """Test filtrage insensible à la casse"""
    events = [
        {"aspect_type": "CONJUNCTION", "planet1": "Sun", "planet2": "Moon", "orb": 1.0},
        {"aspect_type": "Opposition", "planet1": "Mars", "planet2": "Venus", "orb": 2.0},
        {"aspect_type": "Square", "planet1": "Jupiter", "planet2": "Saturn", "orb": 1.5},
        {"aspect_type": "TRINE", "planet1": "Mercury", "planet2": "Neptune", "orb": 0.5},
    ]

    result = transits_services.filter_major_aspects_only(events, major_only=True)

    assert len(result) == 4, "Tous les aspects majeurs doivent être conservés (case insensitive)"


def test_filter_major_aspects_fallback_aspect_key():
    """Test filtrage avec clé 'aspect' au lieu de 'aspect_type'"""
    events = [
        {"aspect": "conjunction", "planet1": "Sun", "planet2": "Moon", "orb": 1.0},
        {"aspect": "sextile", "planet1": "Venus", "planet2": "Mars", "orb": 2.0},
    ]

    result = transits_services.filter_major_aspects_only(events, major_only=True)

    assert len(result) == 1, "Seul l'aspect majeur doit être conservé"
    assert result[0]["aspect"] == "conjunction"


# --- Tests de generate_transit_insights avec major_only ---

def test_generate_transit_insights_major_only_true():
    """Test generate_transit_insights avec major_only=True - seuls aspects majeurs retournés"""
    transits_data = {
        "events": [
            {"transiting_planet": "Jupiter", "stationed_planet": "Sun", "aspect_type": "conjunction", "orb": 1.0},
            {"transiting_planet": "Venus", "stationed_planet": "Mars", "aspect_type": "sextile", "orb": 2.0},  # Mineur
            {"transiting_planet": "Saturn", "stationed_planet": "Moon", "aspect_type": "square", "orb": 0.5},
            {"transiting_planet": "Uranus", "stationed_planet": "Mercury", "aspect_type": "quincunx", "orb": 3.0},  # Mineur
        ]
    }

    insights = transits_services.generate_transit_insights(transits_data, major_only=True)

    assert len(insights["major_aspects"]) == 2, "Seuls les 2 aspects majeurs doivent être retournés"
    aspect_types = [a["aspect"] for a in insights["major_aspects"]]
    assert "conjunction" in aspect_types
    assert "square" in aspect_types
    assert "sextile" not in aspect_types
    assert "quincunx" not in aspect_types


def test_generate_transit_insights_major_only_false():
    """Test generate_transit_insights avec major_only=False - tous aspects retournés"""
    transits_data = {
        "events": [
            {"transiting_planet": "Jupiter", "stationed_planet": "Sun", "aspect_type": "conjunction", "orb": 1.0},
            {"transiting_planet": "Venus", "stationed_planet": "Mars", "aspect_type": "sextile", "orb": 2.0},
            {"transiting_planet": "Saturn", "stationed_planet": "Moon", "aspect_type": "square", "orb": 0.5},
        ]
    }

    insights = transits_services.generate_transit_insights(transits_data, major_only=False)

    # Tous les aspects doivent être retournés
    assert len(insights["major_aspects"]) == 3, "Tous les aspects doivent être retournés"


def test_generate_transit_insights_major_only_four_types():
    """Test que seuls les 4 types d'aspects majeurs sont retournés (conjonction, opposition, carré, trigone)"""
    transits_data = {
        "events": [
            {"transiting_planet": "Sun", "stationed_planet": "Moon", "aspect_type": "conjunction", "orb": 1.0},
            {"transiting_planet": "Mars", "stationed_planet": "Venus", "aspect_type": "opposition", "orb": 2.0},
            {"transiting_planet": "Jupiter", "stationed_planet": "Saturn", "aspect_type": "square", "orb": 1.5},
            {"transiting_planet": "Mercury", "stationed_planet": "Neptune", "aspect_type": "trine", "orb": 0.5},
            {"transiting_planet": "Uranus", "stationed_planet": "Pluto", "aspect_type": "sextile", "orb": 3.0},
            {"transiting_planet": "Moon", "stationed_planet": "Sun", "aspect_type": "semisquare", "orb": 2.5},
        ]
    }

    insights = transits_services.generate_transit_insights(transits_data, major_only=True)

    assert len(insights["major_aspects"]) == 4, "Seuls les 4 aspects majeurs (conjonction, opposition, carré, trigone)"
    aspect_types = [a["aspect"] for a in insights["major_aspects"]]

    # Vérifier les 4 aspects majeurs sont présents
    assert "conjunction" in aspect_types, "Doit contenir conjonction (0°)"
    assert "opposition" in aspect_types, "Doit contenir opposition (180°)"
    assert "square" in aspect_types, "Doit contenir carré (90°)"
    assert "trine" in aspect_types, "Doit contenir trigone (120°)"

    # Vérifier que les mineurs sont exclus
    assert "sextile" not in aspect_types, "Ne doit pas contenir sextile (aspect mineur)"
    assert "semisquare" not in aspect_types, "Ne doit pas contenir semisquare (aspect mineur)"


def test_generate_transit_insights_empty():
    """Test generate_transit_insights avec données vides"""
    insights = transits_services.generate_transit_insights({}, major_only=True)

    assert insights["insights"] == []
    assert insights["major_aspects"] == []
    assert insights["energy_level"] in ["low", "medium", "high"]


def test_generate_transit_insights_with_old_format():
    """Test compatibilité avec l'ancien format 'aspects' au lieu de 'events'"""
    transits_data = {
        "aspects": [  # Ancien format
            {"planet1": "Jupiter", "planet2": "Sun", "aspect": "trine", "orb": 1.2},
            {"planet1": "Saturn", "planet2": "Moon", "aspect": "square", "orb": 0.5},
        ]
    }

    insights = transits_services.generate_transit_insights(transits_data, major_only=True)

    assert len(insights["major_aspects"]) == 2
    aspect_types = [a["aspect"] for a in insights["major_aspects"]]
    assert "trine" in aspect_types
    assert "square" in aspect_types


# --- Tests de validation des aspects majeurs uniquement ---

def test_major_aspects_definition():
    """Test validation de la définition des 4 aspects majeurs"""
    # Les 4 aspects majeurs selon la définition astrologique classique
    major_aspects_definition = ["conjunction", "opposition", "square", "trine"]

    # Tester que filter_major_aspects_only utilise bien ces 4 aspects
    events = [
        {"aspect_type": "conjunction", "planet1": "A", "planet2": "B", "orb": 1.0},
        {"aspect_type": "opposition", "planet1": "C", "planet2": "D", "orb": 1.0},
        {"aspect_type": "square", "planet1": "E", "planet2": "F", "orb": 1.0},
        {"aspect_type": "trine", "planet1": "G", "planet2": "H", "orb": 1.0},
        {"aspect_type": "sextile", "planet1": "I", "planet2": "J", "orb": 1.0},  # Aspect mineur (60°)
    ]

    result = transits_services.filter_major_aspects_only(events, major_only=True)

    # Vérifier que seuls les 4 majeurs sont retournés
    assert len(result) == 4
    result_types = [e["aspect_type"] for e in result]

    # Chaque type majeur doit être présent
    for major_type in major_aspects_definition:
        assert major_type in result_types, f"{major_type} doit être dans les aspects majeurs"

    # Sextile (mineur) ne doit pas être présent
    assert "sextile" not in result_types


def test_aspects_sorted_by_orb():
    """Test que les aspects sont triés par orbe (le plus serré d'abord)"""
    transits_data = {
        "events": [
            {"transiting_planet": "Mars", "stationed_planet": "Venus", "aspect_type": "opposition", "orb": 5.0},
            {"transiting_planet": "Jupiter", "stationed_planet": "Sun", "aspect_type": "trine", "orb": 0.3},
            {"transiting_planet": "Saturn", "stationed_planet": "Moon", "aspect_type": "square", "orb": 2.1},
        ]
    }

    insights = transits_services.generate_transit_insights(transits_data, major_only=True)

    # Le premier aspect devrait avoir l'orbe le plus petit
    assert insights["major_aspects"][0]["orb"] == 0.3
    assert insights["major_aspects"][0]["transit_planet"] == "Jupiter"
