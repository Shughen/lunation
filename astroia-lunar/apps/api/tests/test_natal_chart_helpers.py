"""
Tests unitaires pour utils/natal_chart_helpers.py

Vérifie que is_chart_incomplete() détecte correctement les charts incomplets
selon les nouveaux critères MVP (sans vérifier aspects vides).
"""

import pytest
from utils.natal_chart_helpers import (
    is_chart_incomplete,
    extract_big3_from_positions,
    normalize_subject_data_to_positions
)


class TestIsChartIncomplete:
    """Tests de détection de chart incomplet"""

    def test_is_chart_incomplete_returns_true_for_none(self):
        """is_chart_incomplete retourne True si positions est None"""
        assert is_chart_incomplete(None) is True

    def test_is_chart_incomplete_returns_true_for_empty_dict(self):
        """is_chart_incomplete retourne True si positions est un dict vide"""
        assert is_chart_incomplete({}) is True

    def test_is_chart_incomplete_returns_true_for_non_dict(self):
        """is_chart_incomplete retourne True si positions n'est pas un dict"""
        assert is_chart_incomplete([]) is True
        assert is_chart_incomplete("invalid") is True
        assert is_chart_incomplete(123) is True

    def test_is_chart_incomplete_returns_true_if_sun_missing(self):
        """is_chart_incomplete retourne True si sun manque"""
        positions = {
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_moon_missing(self):
        """is_chart_incomplete retourne True si moon manque"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_ascendant_missing(self):
        """is_chart_incomplete retourne True si ascendant manque"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_planets_less_than_10(self):
        """is_chart_incomplete retourne True si moins de 10 planètes"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(9)},  # 9 planètes
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_planets_empty(self):
        """is_chart_incomplete retourne True si planets est vide"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {},  # Vide
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_planets_missing(self):
        """is_chart_incomplete retourne True si clé planets manque"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            # "planets" manquant
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_planets_not_dict(self):
        """is_chart_incomplete retourne True si planets n'est pas un dict"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": [],  # Liste au lieu de dict
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_houses_less_than_12(self):
        """is_chart_incomplete retourne True si moins de 12 maisons"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 11)}  # 10 maisons
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_houses_more_than_12(self):
        """is_chart_incomplete retourne True si plus de 12 maisons"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 15)}  # 14 maisons
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_houses_empty(self):
        """is_chart_incomplete retourne True si houses est vide"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {}  # Vide
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_houses_missing(self):
        """is_chart_incomplete retourne True si clé houses manque"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            # "houses" manquant
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_true_if_houses_not_dict(self):
        """is_chart_incomplete retourne True si houses n'est pas un dict"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": []  # Liste au lieu de dict
        }
        assert is_chart_incomplete(positions) is True

    def test_is_chart_incomplete_returns_false_for_complete_chart_with_empty_aspects(self):
        """
        is_chart_incomplete retourne False si chart complet MÊME SI aspects est vide.
        MVP accepte aspects=[] comme valide.
        """
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)},
            "aspects": []  # Vide, mais acceptable
        }
        assert is_chart_incomplete(positions) is False

    def test_is_chart_incomplete_returns_false_for_complete_chart_without_aspects(self):
        """is_chart_incomplete retourne False si chart complet sans clé aspects"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)},
            # "aspects" manquant
        }
        assert is_chart_incomplete(positions) is False

    def test_is_chart_incomplete_returns_false_for_complete_chart_with_aspects(self):
        """is_chart_incomplete retourne False si chart complet avec aspects"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)},
            "aspects": [
                {"planet1": "Sun", "planet2": "Moon", "type": "opposition", "orb": 2.38}
            ]
        }
        assert is_chart_incomplete(positions) is False

    def test_is_chart_incomplete_returns_false_for_exactly_10_planets(self):
        """is_chart_incomplete retourne False si exactement 10 planètes"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},  # Exactement 10
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is False

    def test_is_chart_incomplete_returns_false_for_more_than_10_planets(self):
        """is_chart_incomplete retourne False si plus de 10 planètes"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(15)},  # 15 planètes
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}
        }
        assert is_chart_incomplete(positions) is False

    def test_is_chart_incomplete_returns_false_for_exactly_12_houses(self):
        """is_chart_incomplete retourne False si exactement 12 maisons"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}  # Exactement 12
        }
        assert is_chart_incomplete(positions) is False

    def test_is_chart_incomplete_with_mock_metadata(self):
        """is_chart_incomplete retourne False si chart complet avec _mock et _reason"""
        positions = {
            "sun": {"sign": "Aries", "degree": 5.0, "house": 1},
            "moon": {"sign": "Taurus", "degree": 10.0, "house": 2},
            "ascendant": {"sign": "Gemini", "degree": 15.0},
            "planets": {f"planet_{i}": {"sign": "Aries", "degree": 0.0, "house": 1} for i in range(10)},
            "houses": {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)},
            "aspects": [],
            "_mock": True,
            "_reason": "rapidapi_403"
        }
        assert is_chart_incomplete(positions) is False


class TestExtractBig3FromPositions:
    """Tests de extraction Big3 depuis positions JSONB"""

    def test_extract_big3_from_none(self):
        """extract_big3_from_positions retourne None pour toutes les valeurs si positions est None"""
        result = extract_big3_from_positions(None)

        assert result["sun_sign"] is None
        assert result["moon_sign"] is None
        assert result["ascendant_sign"] is None

    def test_extract_big3_from_empty_dict(self):
        """extract_big3_from_positions retourne None si positions est vide"""
        result = extract_big3_from_positions({})

        assert result["sun_sign"] is None
        assert result["moon_sign"] is None
        assert result["ascendant_sign"] is None

    def test_extract_big3_from_complete_positions(self):
        """extract_big3_from_positions extrait correctement Big3"""
        positions = {
            "sun": {"sign": "Aries"},
            "moon": {"sign": "Taurus"},
            "ascendant": {"sign": "Gemini"}
        }
        result = extract_big3_from_positions(positions)

        assert result["sun_sign"] == "Aries"
        assert result["moon_sign"] == "Taurus"
        assert result["ascendant_sign"] == "Gemini"

    def test_extract_big3_handles_zodiac_sign_key(self):
        """extract_big3_from_positions gère la clé 'zodiac_sign' alternative"""
        positions = {
            "sun": {"zodiac_sign": "Aries"},
            "moon": {"zodiac_sign": "Taurus"},
            "ascendant": {"zodiac_sign": "Gemini"}
        }
        result = extract_big3_from_positions(positions)

        assert result["sun_sign"] == "Aries"
        assert result["moon_sign"] == "Taurus"
        assert result["ascendant_sign"] == "Gemini"

    def test_extract_big3_handles_capitalized_keys(self):
        """extract_big3_from_positions gère les clés capitalisées"""
        positions = {
            "Sun": {"sign": "Aries"},
            "Moon": {"sign": "Taurus"},
            "Ascendant": {"sign": "Gemini"}
        }
        result = extract_big3_from_positions(positions)

        assert result["sun_sign"] == "Aries"
        assert result["moon_sign"] == "Taurus"
        assert result["ascendant_sign"] == "Gemini"


class TestNormalizeSubjectDataToPositions:
    """Tests de normalisation depuis subject_data RapidAPI"""

    def test_normalize_subject_data_manaus_scorpio(self):
        """
        Test de normalisation pour Manaus 1989-11-01 13:20
        Vérifie que sun_sign == planets.sun.sign == "Scorpio"
        """
        rapidapi_response = {
            "subject_data": {
                "sun": {"sign": "Sco", "position": 218.45, "house": "Ninth_House"},
                "moon": {"sign": "Gem", "position": 82.30, "house": "Fifth_House"},
                "ascendant": {"sign": "Aqu", "position": 315.20, "house": "First_House"},
                "mercury": {"sign": "Sco", "position": 225.10, "house": "Ninth_House"},
                "venus": {"sign": "Sag", "position": 240.50, "house": "Tenth_House"},
                "mars": {"sign": "Cap", "position": 270.20, "house": "Eleventh_House"},
                "jupiter": {"sign": "Can", "position": 95.15, "house": "Sixth_House"},
                "saturn": {"sign": "Cap", "position": 275.30, "house": "Eleventh_House"},
                "uranus": {"sign": "Cap", "position": 280.40, "house": "Eleventh_House"},
                "neptune": {"sign": "Cap", "position": 285.50, "house": "Eleventh_House"},
                "pluto": {"sign": "Sco", "position": 230.60, "house": "Ninth_House"}
            }
        }

        positions = normalize_subject_data_to_positions(rapidapi_response)

        # Vérifier que sun est normalisé
        assert positions["sun"]["sign"] == "Scorpio"
        assert positions["planets"]["sun"]["sign"] == "Scorpio"

        # ✅ COHÉRENCE Big3: sun_sign == planets.sun.sign
        big3 = extract_big3_from_positions(positions)
        assert big3["sun_sign"] == "Scorpio"
        assert big3["sun_sign"] == positions["planets"]["sun"]["sign"], \
            f"sun_sign={big3['sun_sign']} doit être égal à planets.sun.sign={positions['planets']['sun']['sign']}"

        # Vérifier que moon est normalisé
        assert positions["moon"]["sign"] == "Gemini"
        assert positions["planets"]["moon"]["sign"] == "Gemini"
        assert big3["moon_sign"] == "Gemini"
        assert big3["moon_sign"] == positions["planets"]["moon"]["sign"]

        # Vérifier que ascendant est normalisé
        assert positions["ascendant"]["sign"] == "Aquarius"
        assert positions["planets"]["Ascendant"]["sign"] == "Aquarius"
        assert big3["ascendant_sign"] == "Aquarius"

        # Vérifier que toutes les planètes sont présentes
        assert len(positions["planets"]) >= 10
        assert "sun" in positions["planets"]
        assert "moon" in positions["planets"]
        assert "mercury" in positions["planets"]
        assert "venus" in positions["planets"]
        assert "mars" in positions["planets"]
        assert "jupiter" in positions["planets"]
        assert "saturn" in positions["planets"]
        assert "uranus" in positions["planets"]
        assert "neptune" in positions["planets"]
        assert "pluto" in positions["planets"]
        assert "Ascendant" in positions["planets"]

        # Vérifier mapping maisons
        assert positions["sun"]["house"] == 9  # Ninth_House -> 9
        assert positions["moon"]["house"] == 5  # Fifth_House -> 5

    def test_normalize_subject_data_missing_subject_data(self):
        """Test que ValueError est levée si subject_data absent"""
        rapidapi_response = {
            "chart_data": {
                "planetary_positions": []
            }
        }

        with pytest.raises(ValueError, match="subject_data absent"):
            normalize_subject_data_to_positions(rapidapi_response)

    def test_normalize_subject_data_all_signs_mapping(self):
        """Test que tous les signes sont correctement mappés"""
        sign_abbrs = ["Ari", "Tau", "Gem", "Can", "Leo", "Vir", "Lib", "Sco", "Sag", "Cap", "Aqu", "Pis"]
        sign_full_expected = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ]

        for abbr, expected in zip(sign_abbrs, sign_full_expected):
            rapidapi_response = {
                "subject_data": {
                    "sun": {"sign": abbr, "position": 0.0, "house": "First_House"},
                    "moon": {"sign": "Ari", "position": 0.0, "house": "First_House"},
                    "mercury": {"sign": "Ari", "position": 0.0, "house": "First_House"},
                    "venus": {"sign": "Ari", "position": 0.0, "house": "First_House"},
                    "mars": {"sign": "Ari", "position": 0.0, "house": "First_House"},
                    "jupiter": {"sign": "Ari", "position": 0.0, "house": "First_House"},
                    "saturn": {"sign": "Ari", "position": 0.0, "house": "First_House"},
                    "uranus": {"sign": "Ari", "position": 0.0, "house": "First_House"},
                    "neptune": {"sign": "Ari", "position": 0.0, "house": "First_House"},
                    "pluto": {"sign": "Ari", "position": 0.0, "house": "First_House"}
                }
            }

            positions = normalize_subject_data_to_positions(rapidapi_response)
            assert positions["sun"]["sign"] == expected, \
                f"Signe {abbr} doit être mappé vers {expected}, mais obtenu {positions['sun']['sign']}"
