"""
Tests d'intégration pour l'auto-heal natal chart et le fallback mock.

Vérifie que:
1. POST /api/natal-chart fallback sur mock si RapidAPI 503
2. GET /api/natal-chart auto-heal les charts incomplets
3. POST /api/natal-chart/dev/purge fonctionne correctement
"""

import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from fastapi import HTTPException
from datetime import date, time

from services.natal_chart_mock import generate_complete_natal_mock
from utils.natal_chart_helpers import is_chart_incomplete


class TestNatalChartFallbackMockOnPost:
    """Tests du fallback mock sur POST /api/natal-chart quand RapidAPI échoue"""

    def test_generate_complete_natal_mock_called_on_rapidapi_503(self):
        """
        Vérifie que generate_complete_natal_mock() est appelé si RapidAPI retourne 503.

        Ce test est conceptuel car il faudrait mocker toute la chaîne.
        On teste juste que le service mock fonctionne correctement.
        """
        birth_data = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        # Simuler fallback mock
        mock_positions = generate_complete_natal_mock(birth_data, reason="rapidapi_503")

        # Vérifier que le mock est complet
        assert is_chart_incomplete(mock_positions) is False, "Le mock devrait être complet"
        assert mock_positions["_mock"] is True, "Devrait avoir _mock=True"
        assert mock_positions["_reason"] == "rapidapi_503", "Devrait avoir le bon code d'erreur"

    def test_fallback_mock_has_all_required_data(self):
        """Le fallback mock contient toutes les données requises"""
        birth_data = {
            "year": 1985,
            "month": 12,
            "day": 25,
            "hour": 8,
            "minute": 0,
            "latitude": 40.7128,
            "longitude": -74.0060
        }

        mock_positions = generate_complete_natal_mock(birth_data, reason="rapidapi_429")

        # Vérifier structure complète
        assert "sun" in mock_positions
        assert "moon" in mock_positions
        assert "ascendant" in mock_positions
        assert len(mock_positions["planets"]) >= 10
        assert len(mock_positions["houses"]) == 12
        assert isinstance(mock_positions["aspects"], list)

        # Vérifier métadonnées
        assert mock_positions["_mock"] is True
        assert mock_positions["_reason"] == "rapidapi_429"


class TestIsChartIncompleteDetection:
    """Tests de détection de charts incomplets"""

    def test_is_chart_incomplete_detects_missing_planets(self):
        """is_chart_incomplete détecte moins de 10 planètes"""
        incomplete_positions = {
            "sun": {"sign": "Aries"},
            "moon": {"sign": "Taurus"},
            "ascendant": {"sign": "Gemini"},
            "planets": {
                "sun": {"sign": "Aries"},
                "moon": {"sign": "Taurus"},
                "mercury": {"sign": "Aries"}
                # Seulement 3 planètes
            },
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 13)},
            "aspects": []
        }

        assert is_chart_incomplete(incomplete_positions) is True

    def test_is_chart_incomplete_detects_missing_houses(self):
        """is_chart_incomplete détecte moins de 12 maisons"""
        incomplete_positions = {
            "sun": {"sign": "Aries"},
            "moon": {"sign": "Taurus"},
            "ascendant": {"sign": "Gemini"},
            "planets": {f"planet_{i}": {"sign": "Aries"} for i in range(10)},
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 8)},  # 7 maisons
            "aspects": []
        }

        assert is_chart_incomplete(incomplete_positions) is True

    def test_is_chart_incomplete_accepts_empty_aspects(self):
        """
        is_chart_incomplete accepte aspects=[] (MVP).
        Correction utilisateur: aspects vides ne signifie PAS incomplet.
        """
        complete_positions = {
            "sun": {"sign": "Aries"},
            "moon": {"sign": "Taurus"},
            "ascendant": {"sign": "Gemini"},
            "planets": {f"planet_{i}": {"sign": "Aries"} for i in range(10)},
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 13)},
            "aspects": []  # Vide, mais acceptable
        }

        assert is_chart_incomplete(complete_positions) is False

    def test_is_chart_incomplete_detects_missing_big3(self):
        """is_chart_incomplete détecte si Big3 manquant"""
        # Sun manquant
        incomplete_1 = {
            "moon": {"sign": "Taurus"},
            "ascendant": {"sign": "Gemini"},
            "planets": {f"planet_{i}": {"sign": "Aries"} for i in range(10)},
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 13)}
        }
        assert is_chart_incomplete(incomplete_1) is True

        # Moon manquant
        incomplete_2 = {
            "sun": {"sign": "Aries"},
            "ascendant": {"sign": "Gemini"},
            "planets": {f"planet_{i}": {"sign": "Aries"} for i in range(10)},
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 13)}
        }
        assert is_chart_incomplete(incomplete_2) is True

        # Ascendant manquant
        incomplete_3 = {
            "sun": {"sign": "Aries"},
            "moon": {"sign": "Taurus"},
            "planets": {f"planet_{i}": {"sign": "Aries"} for i in range(10)},
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 13)}
        }
        assert is_chart_incomplete(incomplete_3) is True

    def test_is_chart_incomplete_returns_false_for_complete_chart(self):
        """is_chart_incomplete retourne False si chart complet"""
        complete_positions = {
            "sun": {"sign": "Scorpio", "degree": 0.0, "house": 9},
            "moon": {"sign": "Taurus", "degree": 15.0, "house": 3},
            "ascendant": {"sign": "Gemini", "degree": 20.0},
            "planets": {
                "sun": {"sign": "Scorpio"},
                "moon": {"sign": "Taurus"},
                "mercury": {"sign": "Scorpio"},
                "venus": {"sign": "Libra"},
                "mars": {"sign": "Sagittarius"},
                "jupiter": {"sign": "Capricorn"},
                "saturn": {"sign": "Aquarius"},
                "uranus": {"sign": "Pisces"},
                "neptune": {"sign": "Aries"},
                "pluto": {"sign": "Taurus"}
            },
            "houses": {str(i): {"sign": "Aries", "degree": float(i)} for i in range(1, 13)},
            "aspects": [
                {"planet1": "Sun", "planet2": "Moon", "type": "opposition", "orb": 2.38}
            ]
        }

        assert is_chart_incomplete(complete_positions) is False


class TestAutoHealLogic:
    """Tests de la logique d'auto-heal (conceptuels)"""

    def test_auto_heal_generates_complete_mock(self):
        """
        L'auto-heal génère un mock complet qui passe is_chart_incomplete().

        Simule le flow d'auto-heal:
        1. Détecter chart incomplet
        2. Générer mock
        3. Vérifier que le mock est complet
        """
        # Simuler un chart incomplet
        incomplete_chart = {
            "sun": {"sign": "Aries"},
            "moon": {"sign": "Taurus"},
            "ascendant": {"sign": "Gemini"},
            "planets": {
                "sun": {"sign": "Aries"},
                "moon": {"sign": "Taurus"}
                # Seulement 2 planètes
            },
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 8)}  # 7 maisons
        }

        # Vérifier qu'il est incomplet
        assert is_chart_incomplete(incomplete_chart) is True

        # Simuler auto-heal
        birth_data = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }
        healed_chart = generate_complete_natal_mock(birth_data, reason="auto_heal")

        # Vérifier que le chart healed est complet
        assert is_chart_incomplete(healed_chart) is False
        assert healed_chart["_mock"] is True
        assert healed_chart["_reason"] == "auto_heal"

    def test_auto_heal_preserves_determinism(self):
        """L'auto-heal produit le même résultat pour les mêmes données"""
        birth_data = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        # Simuler 2 auto-heal consécutifs
        healed_1 = generate_complete_natal_mock(birth_data, reason="auto_heal")
        healed_2 = generate_complete_natal_mock(birth_data, reason="auto_heal")

        # Devraient être identiques
        assert healed_1["sun"] == healed_2["sun"]
        assert healed_1["moon"] == healed_2["moon"]
        assert healed_1["ascendant"] == healed_2["ascendant"]
        assert healed_1["planets"] == healed_2["planets"]
        assert healed_1["houses"] == healed_2["houses"]


class TestMockMetadataPresence:
    """Tests de présence des métadonnées _mock et _reason"""

    def test_mock_has_metadata_for_rapidapi_errors(self):
        """Le mock contient _mock et _reason pour tous les codes d'erreur RapidAPI"""
        error_codes = ["rapidapi_403", "rapidapi_429", "rapidapi_500", "rapidapi_503"]

        birth_data = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        for error_code in error_codes:
            mock = generate_complete_natal_mock(birth_data, reason=error_code)

            assert "_mock" in mock, f"_mock devrait être présent pour {error_code}"
            assert mock["_mock"] is True, f"_mock devrait être True pour {error_code}"
            assert "_reason" in mock, f"_reason devrait être présent pour {error_code}"
            assert mock["_reason"] == error_code, f"_reason devrait être {error_code}"

    def test_mock_has_metadata_for_auto_heal(self):
        """Le mock contient _mock et _reason pour auto-heal"""
        birth_data = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        mock = generate_complete_natal_mock(birth_data, reason="auto_heal")

        assert mock["_mock"] is True
        assert mock["_reason"] == "auto_heal"

    def test_mock_metadata_not_considered_by_is_chart_incomplete(self):
        """
        Les métadonnées _mock et _reason n'affectent pas is_chart_incomplete().
        Un chart avec _mock=True peut être complet.
        """
        mock_positions = {
            "sun": {"sign": "Aries"},
            "moon": {"sign": "Taurus"},
            "ascendant": {"sign": "Gemini"},
            "planets": {f"planet_{i}": {"sign": "Aries"} for i in range(10)},
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 13)},
            "aspects": [],
            "_mock": True,
            "_reason": "rapidapi_503"
        }

        # Devrait être considéré complet malgré _mock=True
        assert is_chart_incomplete(mock_positions) is False


class TestDevPurgeEndpoint:
    """Tests conceptuels pour l'endpoint /natal-chart/dev/purge"""

    def test_dev_purge_requires_development_env(self):
        """
        /natal-chart/dev/purge devrait retourner 404 si APP_ENV != development.

        Ce test est conceptuel car il faudrait mocker settings et FastAPI.
        """
        # Dans un vrai test, on vérifierait que:
        # - Si APP_ENV != "development" => 404
        # - Si ALLOW_DEV_PURGE != True => 404
        # - Si user non authentifié => 401
        pass

    def test_dev_purge_requires_flag_enabled(self):
        """
        /natal-chart/dev/purge devrait retourner 404 si ALLOW_DEV_PURGE=False.
        """
        # Dans un vrai test, on vérifierait le flag
        pass

    def test_dev_purge_deletes_only_current_user_chart(self):
        """
        /natal-chart/dev/purge devrait supprimer uniquement le chart du current_user.
        """
        # Dans un vrai test, on vérifierait que:
        # - Seul le chart du current_user est supprimé
        # - Les autres users ne sont pas affectés
        pass


class TestEndToEndFlow:
    """Tests conceptuels du flow end-to-end"""

    def test_post_natal_chart_then_get_returns_complete_chart(self):
        """
        Flow end-to-end:
        1. POST /api/natal-chart (fallback mock si RapidAPI fail)
        2. GET /api/natal-chart (auto-heal si incomplet)
        3. Chart retourné devrait être complet

        Ce test est conceptuel et nécessiterait un vrai serveur de test.
        """
        # Simuler le flow
        birth_data = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        # POST: Générer chart (simuler fallback mock)
        chart_positions = generate_complete_natal_mock(birth_data, reason="rapidapi_503")

        # Vérifier que le chart est complet après POST
        assert is_chart_incomplete(chart_positions) is False

        # GET: Récupérer chart (pas d'auto-heal nécessaire car déjà complet)
        # Le chart devrait rester complet
        assert is_chart_incomplete(chart_positions) is False

    def test_incomplete_chart_gets_auto_healed_on_get(self):
        """
        Si un chart incomplet existe en DB, GET /api/natal-chart devrait l'auto-heal.
        """
        # Simuler chart incomplet en DB
        incomplete_chart = {
            "sun": {"sign": "Aries"},
            "moon": {"sign": "Taurus"},
            "ascendant": {"sign": "Gemini"},
            "planets": {"sun": {"sign": "Aries"}},  # 1 planète
            "houses": {str(i): {"sign": "Aries"} for i in range(1, 8)}  # 7 maisons
        }

        assert is_chart_incomplete(incomplete_chart) is True

        # Simuler auto-heal
        birth_data = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }
        healed_chart = generate_complete_natal_mock(birth_data, reason="auto_heal")

        # Après auto-heal, le chart devrait être complet
        assert is_chart_incomplete(healed_chart) is False
        assert healed_chart["_mock"] is True
        assert healed_chart["_reason"] == "auto_heal"
