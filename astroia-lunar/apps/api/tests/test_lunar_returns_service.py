"""
Tests unitaires pour le service lunar_returns_service

Tests:
- _compute_rolling_months: calcule 12 mois à partir de now
- _sign_degree_to_longitude: convertit signe + degré en longitude

NOTE: Les tests d'intégration avec DB sont dans test_lunar_returns.py
"""

import pytest
from datetime import datetime, timezone

from services.lunar_returns_service import (
    _compute_rolling_months,
    _sign_degree_to_longitude
)


def test_compute_rolling_months():
    """
    Test: _compute_rolling_months() génère 12 mois à partir de now

    Vérifie:
    - Liste de 12 éléments
    - Format YYYY-MM
    - Ordre croissant
    """
    now = datetime(2025, 1, 15, 12, 0, 0, tzinfo=timezone.utc)
    months = _compute_rolling_months(now)

    assert len(months) == 12, f"Expected 12 months, got {len(months)}"
    assert months[0] == "2025-01", f"Expected first month to be 2025-01, got {months[0]}"
    assert months[-1] == "2025-12", f"Expected last month to be 2025-12, got {months[-1]}"

    # Vérifier format YYYY-MM
    for month in months:
        assert len(month) == 7, f"Expected format YYYY-MM, got {month}"
        assert month[4] == '-', f"Expected format YYYY-MM with dash, got {month}"


def test_sign_degree_to_longitude():
    """
    Test: _sign_degree_to_longitude() convertit signe + degré en longitude

    Vérifie:
    - Aries 0° = 0°
    - Taurus 0° = 30°
    - Gemini 15° = 75°
    - Erreur si signe invalide
    """
    # Aries 0°
    assert _sign_degree_to_longitude("Aries", 0) == 0, "Aries 0° should be 0°"

    # Taurus 0°
    assert _sign_degree_to_longitude("Taurus", 0) == 30, "Taurus 0° should be 30°"

    # Gemini 15°
    assert _sign_degree_to_longitude("Gemini", 15) == 75, "Gemini 15° should be 75°"

    # Cancer 0°
    assert _sign_degree_to_longitude("Cancer", 0) == 90, "Cancer 0° should be 90°"

    # Test variante française
    assert _sign_degree_to_longitude("Bélier", 0) == 0, "Bélier 0° should be 0°"

    # Test erreur signe invalide
    with pytest.raises(ValueError):
        _sign_degree_to_longitude("InvalidSign", 0)
