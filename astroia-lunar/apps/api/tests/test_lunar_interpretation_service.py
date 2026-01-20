"""
Tests pour lunar_interpretation_service.py

Architecture par couches :
- lunar_climate : Tonalité émotionnelle par signe
- lunar_focus : Domaine de vie par maison
- lunar_approach : Approche par ascendant

Tests:
- Chargement depuis la base
- Fallbacks si pas en base
- Génération conseils hebdomadaires
"""

import pytest
from datetime import datetime, timezone, timedelta
from unittest.mock import MagicMock, AsyncMock

from services.lunar_interpretation_service import (
    load_lunar_climate,
    load_lunar_focus,
    load_lunar_approach,
    load_lunar_interpretation_layers,
    get_fallback_climate,
    get_fallback_focus,
    get_fallback_approach,
    generate_weekly_advice,
    FALLBACK_CLIMATE,
    FALLBACK_FOCUS,
    FALLBACK_APPROACH
)


class TestFallbackTemplates:
    """Tests des templates fallback (sans base de données)"""

    def test_fallback_climate_all_signs(self):
        """Tous les signes ont un fallback climat"""
        signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
        for sign in signs:
            result = get_fallback_climate(sign)
            assert result is not None
            assert len(result) > 20
            assert sign not in result or "dynamique" in result.lower() or "mois" in result.lower()

    def test_fallback_focus_all_houses(self):
        """Toutes les maisons ont un fallback focus"""
        for house in range(1, 13):
            result = get_fallback_focus(house)
            assert result is not None
            assert len(result) > 20
            assert "Focus" in result

    def test_fallback_approach_all_ascendants(self):
        """Tous les ascendants ont un fallback approche"""
        ascendants = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                      'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
        for asc in ascendants:
            result = get_fallback_approach(asc)
            assert result is not None
            assert len(result) > 20
            assert "abordes" in result.lower()

    def test_fallback_climate_unknown_sign(self):
        """Signe inconnu retourne un fallback générique"""
        result = get_fallback_climate("Unknown")
        assert "Unknown" in result

    def test_fallback_focus_invalid_house(self):
        """Maison invalide retourne un fallback générique"""
        result = get_fallback_focus(99)
        assert "99" in result

    def test_fallback_approach_unknown_ascendant(self):
        """Ascendant inconnu retourne un fallback générique"""
        result = get_fallback_approach("Unknown")
        assert "Unknown" in result


class TestGenerateWeeklyAdvice:
    """Tests de la génération des conseils hebdomadaires"""

    def test_generates_4_weeks(self):
        """Génère exactement 4 semaines"""
        return_date = datetime(2025, 2, 15, 12, 0, 0, tzinfo=timezone.utc)
        result = generate_weekly_advice(return_date)
        assert "week_1" in result
        assert "week_2" in result
        assert "week_3" in result
        assert "week_4" in result
        assert len(result) == 4

    def test_each_week_has_required_fields(self):
        """Chaque semaine a les champs requis"""
        return_date = datetime(2025, 3, 1, 0, 0, 0, tzinfo=timezone.utc)
        result = generate_weekly_advice(return_date)
        for week_key in ["week_1", "week_2", "week_3", "week_4"]:
            week = result[week_key]
            assert "dates" in week
            assert "theme" in week
            assert "conseil" in week
            assert "focus" in week

    def test_dates_are_sequential(self):
        """Les dates sont séquentielles (7 jours par semaine)"""
        return_date = datetime(2025, 1, 10, 0, 0, 0, tzinfo=timezone.utc)
        result = generate_weekly_advice(return_date)
        # Semaine 1 commence le 10/01
        assert "10/01" in result["week_1"]["dates"]
        # Semaine 2 commence le 17/01
        assert "17/01" in result["week_2"]["dates"]
        # Semaine 3 commence le 24/01
        assert "24/01" in result["week_3"]["dates"]
        # Semaine 4 commence le 31/01
        assert "31/01" in result["week_4"]["dates"]

    def test_themes_are_progressive(self):
        """Les thèmes suivent une progression logique"""
        return_date = datetime(2025, 4, 1, 0, 0, 0, tzinfo=timezone.utc)
        result = generate_weekly_advice(return_date)
        # Les thèmes devraient évoluer sur le cycle
        themes = [result[f"week_{i}"]["theme"] for i in range(1, 5)]
        assert "Lancement" in themes[0]
        assert "Consolidation" in themes[1]
        assert "Ajustements" in themes[2]
        assert "Bilan" in themes[3] or "clôture" in themes[3].lower()


class TestLoadFromDatabase:
    """Tests du chargement depuis la base de données (avec mocks)"""

    @pytest.mark.asyncio
    async def test_load_lunar_climate_found(self):
        """Charge le climat depuis la DB quand trouvé"""
        mock_db = AsyncMock()
        mock_entry = MagicMock()
        mock_entry.interpretation_full = "**Climat du mois : Test**\n\nContenu test."

        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_entry
        mock_db.execute.return_value = mock_result

        result = await load_lunar_climate(mock_db, "Aries", version=1, lang='fr')

        assert result is not None
        assert "Climat du mois" in result
        mock_db.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_load_lunar_climate_not_found(self):
        """Retourne None si climat non trouvé"""
        mock_db = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_db.execute.return_value = mock_result

        result = await load_lunar_climate(mock_db, "Aries", version=1, lang='fr')

        assert result is None

    @pytest.mark.asyncio
    async def test_load_lunar_focus_found(self):
        """Charge le focus depuis la DB quand trouvé"""
        mock_db = AsyncMock()
        mock_entry = MagicMock()
        mock_entry.interpretation_full = "**Focus du mois : Toi-même**\n\nContenu test."

        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_entry
        mock_db.execute.return_value = mock_result

        result = await load_lunar_focus(mock_db, 1, version=1, lang='fr')

        assert result is not None
        assert "Focus du mois" in result

    @pytest.mark.asyncio
    async def test_load_lunar_approach_found(self):
        """Charge l'approche depuis la DB quand trouvée"""
        mock_db = AsyncMock()
        mock_entry = MagicMock()
        mock_entry.interpretation_full = "**Ton approche ce mois**\n\nContenu test."

        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_entry
        mock_db.execute.return_value = mock_result

        result = await load_lunar_approach(mock_db, "Aries", version=1, lang='fr')

        assert result is not None
        assert "approche" in result.lower()

    @pytest.mark.asyncio
    async def test_load_interpretation_layers_all_found(self):
        """Charge les 3 couches quand toutes trouvées"""
        mock_db = AsyncMock()

        # Simuler 3 appels successifs
        mock_entries = [
            MagicMock(interpretation_full="Climate content"),
            MagicMock(interpretation_full="Focus content"),
            MagicMock(interpretation_full="Approach content"),
        ]

        call_count = [0]
        def mock_execute(*args, **kwargs):
            result = MagicMock()
            result.scalar_one_or_none.return_value = mock_entries[call_count[0]]
            call_count[0] += 1
            return result

        mock_db.execute.side_effect = mock_execute

        result = await load_lunar_interpretation_layers(
            mock_db, "Aries", 1, "Taurus", version=1, lang='fr'
        )

        assert result['climate'] == "Climate content"
        assert result['focus'] == "Focus content"
        assert result['approach'] == "Approach content"

    @pytest.mark.asyncio
    async def test_load_interpretation_layers_partial(self):
        """Retourne None pour les couches non trouvées"""
        mock_db = AsyncMock()

        # Simuler: climate trouvé, focus non trouvé, approach trouvé
        responses = [
            MagicMock(interpretation_full="Climate content"),  # climate
            None,  # focus
            MagicMock(interpretation_full="Approach content"),  # approach
        ]

        call_count = [0]
        def mock_execute(*args, **kwargs):
            result = MagicMock()
            result.scalar_one_or_none.return_value = responses[call_count[0]]
            call_count[0] += 1
            return result

        mock_db.execute.side_effect = mock_execute

        result = await load_lunar_interpretation_layers(
            mock_db, "Leo", 5, "Virgo", version=1, lang='fr'
        )

        assert result['climate'] == "Climate content"
        assert result['focus'] is None
        assert result['approach'] == "Approach content"


class TestFallbackConstantsIntegrity:
    """Tests de l'intégrité des constantes fallback"""

    def test_fallback_climate_has_12_entries(self):
        """FALLBACK_CLIMATE a exactement 12 entrées"""
        assert len(FALLBACK_CLIMATE) == 12

    def test_fallback_focus_has_12_entries(self):
        """FALLBACK_FOCUS a exactement 12 entrées"""
        assert len(FALLBACK_FOCUS) == 12

    def test_fallback_approach_has_12_entries(self):
        """FALLBACK_APPROACH a exactement 12 entrées"""
        assert len(FALLBACK_APPROACH) == 12

    def test_fallback_focus_keys_are_1_to_12(self):
        """FALLBACK_FOCUS a les clés 1 à 12"""
        for i in range(1, 13):
            assert i in FALLBACK_FOCUS

    def test_all_zodiac_signs_in_climate(self):
        """Tous les signes du zodiaque sont dans FALLBACK_CLIMATE"""
        expected_signs = {
            'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
            'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
        }
        assert set(FALLBACK_CLIMATE.keys()) == expected_signs

    def test_all_zodiac_signs_in_approach(self):
        """Tous les signes du zodiaque sont dans FALLBACK_APPROACH"""
        expected_signs = {
            'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
            'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
        }
        assert set(FALLBACK_APPROACH.keys()) == expected_signs
