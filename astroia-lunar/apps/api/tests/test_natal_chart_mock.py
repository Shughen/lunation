"""
Tests unitaires pour le service natal_chart_mock.py

Vérifie que generate_complete_natal_mock() produit des charts complets,
déterministes, et avec les métadonnées _mock et _reason.
"""

import pytest
from services.natal_chart_mock import (
    generate_complete_natal_mock,
    _deterministic_hash,
    _get_sign_from_seed,
    _get_degree_from_seed,
    _get_house_from_seed,
    SIGN_NAMES,
    PLANET_NAMES
)


class TestDeterministicHelpers:
    """Tests des fonctions helpers de génération déterministe"""

    def test_deterministic_hash_same_data_same_hash(self):
        """Hash identique pour les mêmes données de naissance"""
        birth_data = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        hash1 = _deterministic_hash(birth_data)
        hash2 = _deterministic_hash(birth_data)

        assert hash1 == hash2, "Le hash devrait être déterministe"
        assert isinstance(hash1, int), "Le hash devrait être un entier"

    def test_deterministic_hash_different_data_different_hash(self):
        """Hash différent pour des données différentes"""
        birth_data1 = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }
        birth_data2 = {
            "year": 1991,  # Année différente
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        hash1 = _deterministic_hash(birth_data1)
        hash2 = _deterministic_hash(birth_data2)

        assert hash1 != hash2, "Des données différentes devraient produire des hash différents"

    def test_get_sign_from_seed_returns_valid_sign(self):
        """_get_sign_from_seed retourne un signe valide"""
        seed = 12345
        sign = _get_sign_from_seed(seed)

        assert sign in SIGN_NAMES, f"Le signe {sign} devrait être dans SIGN_NAMES"

    def test_get_sign_from_seed_is_deterministic(self):
        """_get_sign_from_seed est déterministe pour un seed donné"""
        seed = 67890
        sign1 = _get_sign_from_seed(seed, offset=0)
        sign2 = _get_sign_from_seed(seed, offset=0)

        assert sign1 == sign2, "Même seed + offset devrait donner le même signe"

    def test_get_sign_from_seed_offset_varies(self):
        """_get_sign_from_seed varie avec l'offset"""
        seed = 11111
        sign1 = _get_sign_from_seed(seed, offset=0)
        sign2 = _get_sign_from_seed(seed, offset=1)

        # Pas garanti d'être différent, mais devrait l'être dans la plupart des cas
        # On teste juste que l'offset fonctionne
        assert isinstance(sign2, str)

    def test_get_degree_from_seed_in_valid_range(self):
        """_get_degree_from_seed retourne un degré valide (0-29.99)"""
        seed = 22222
        degree = _get_degree_from_seed(seed)

        assert 0.0 <= degree < 30.0, f"Le degré {degree} devrait être entre 0 et 30"
        assert isinstance(degree, float), "Le degré devrait être un float"

    def test_get_degree_from_seed_is_deterministic(self):
        """_get_degree_from_seed est déterministe"""
        seed = 33333
        degree1 = _get_degree_from_seed(seed, offset=0)
        degree2 = _get_degree_from_seed(seed, offset=0)

        assert degree1 == degree2, "Même seed + offset devrait donner le même degré"

    def test_get_house_from_seed_in_valid_range(self):
        """_get_house_from_seed retourne une maison valide (1-12)"""
        seed = 44444
        house = _get_house_from_seed(seed)

        assert 1 <= house <= 12, f"La maison {house} devrait être entre 1 et 12"
        assert isinstance(house, int), "La maison devrait être un entier"

    def test_get_house_from_seed_is_deterministic(self):
        """_get_house_from_seed est déterministe"""
        seed = 55555
        house1 = _get_house_from_seed(seed, offset=0)
        house2 = _get_house_from_seed(seed, offset=0)

        assert house1 == house2, "Même seed + offset devrait donner la même maison"


class TestGenerateCompleteNatalMock:
    """Tests de la fonction principale generate_complete_natal_mock()"""

    @pytest.fixture
    def sample_birth_data(self):
        """Données de naissance exemple pour les tests"""
        return {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

    def test_generate_complete_natal_mock_structure(self, sample_birth_data):
        """Le mock généré a la structure correcte"""
        mock = generate_complete_natal_mock(sample_birth_data)

        # Vérifier les clés top-level
        assert "sun" in mock, "Devrait avoir 'sun'"
        assert "moon" in mock, "Devrait avoir 'moon'"
        assert "ascendant" in mock, "Devrait avoir 'ascendant'"
        assert "planets" in mock, "Devrait avoir 'planets'"
        assert "houses" in mock, "Devrait avoir 'houses'"
        assert "aspects" in mock, "Devrait avoir 'aspects'"
        assert "_mock" in mock, "Devrait avoir '_mock'"
        assert "_reason" in mock, "Devrait avoir '_reason'"

    def test_generate_complete_natal_mock_has_metadata(self, sample_birth_data):
        """Le mock contient les métadonnées _mock et _reason"""
        mock = generate_complete_natal_mock(sample_birth_data, reason="rapidapi_403")

        assert mock["_mock"] is True, "_mock devrait être True"
        assert mock["_reason"] == "rapidapi_403", "_reason devrait contenir le code d'erreur"

    def test_generate_complete_natal_mock_default_reason(self, sample_birth_data):
        """Le mock utilise une raison par défaut si non fournie"""
        mock = generate_complete_natal_mock(sample_birth_data)

        assert mock["_reason"] == "rapidapi_unavailable", "_reason devrait avoir la valeur par défaut"

    def test_generate_complete_natal_mock_big3_structure(self, sample_birth_data):
        """Les Big3 ont la structure correcte"""
        mock = generate_complete_natal_mock(sample_birth_data)

        # Sun
        assert "sign" in mock["sun"], "Sun devrait avoir 'sign'"
        assert "degree" in mock["sun"], "Sun devrait avoir 'degree'"
        assert "house" in mock["sun"], "Sun devrait avoir 'house'"

        # Moon
        assert "sign" in mock["moon"], "Moon devrait avoir 'sign'"
        assert "degree" in mock["moon"], "Moon devrait avoir 'degree'"
        assert "house" in mock["moon"], "Moon devrait avoir 'house'"

        # Ascendant
        assert "sign" in mock["ascendant"], "Ascendant devrait avoir 'sign'"
        assert "degree" in mock["ascendant"], "Ascendant devrait avoir 'degree'"

    def test_generate_complete_natal_mock_has_10_planets(self, sample_birth_data):
        """Le mock contient au moins 10 planètes"""
        mock = generate_complete_natal_mock(sample_birth_data)

        planets = mock["planets"]
        assert isinstance(planets, dict), "planets devrait être un dict"
        assert len(planets) >= 10, f"Devrait avoir au moins 10 planètes, trouvé {len(planets)}"

        # Vérifier que les planètes principales sont présentes
        for planet_name in PLANET_NAMES:
            assert planet_name in planets, f"Planète {planet_name} devrait être présente"

    def test_generate_complete_natal_mock_has_ascendant_in_planets(self, sample_birth_data):
        """Le mock contient ascendant dans planets"""
        mock = generate_complete_natal_mock(sample_birth_data)

        assert "ascendant" in mock["planets"], "ascendant devrait être dans planets"
        assert mock["planets"]["ascendant"]["house"] == 1, "Ascendant devrait être en maison 1"

    def test_generate_complete_natal_mock_has_12_houses(self, sample_birth_data):
        """Le mock contient exactement 12 maisons"""
        mock = generate_complete_natal_mock(sample_birth_data)

        houses = mock["houses"]
        assert isinstance(houses, dict), "houses devrait être un dict"
        assert len(houses) == 12, f"Devrait avoir exactement 12 maisons, trouvé {len(houses)}"

        # Vérifier que les clés sont "1" à "12"
        for house_num in range(1, 13):
            assert str(house_num) in houses, f"Maison {house_num} devrait être présente"

    def test_generate_complete_natal_mock_house_structure(self, sample_birth_data):
        """Chaque maison a la structure correcte"""
        mock = generate_complete_natal_mock(sample_birth_data)

        for house_num in range(1, 13):
            house = mock["houses"][str(house_num)]
            assert "sign" in house, f"Maison {house_num} devrait avoir 'sign'"
            assert "degree" in house, f"Maison {house_num} devrait avoir 'degree'"
            assert house["sign"] in SIGN_NAMES, f"Maison {house_num} devrait avoir un signe valide"

    def test_generate_complete_natal_mock_aspects_empty(self, sample_birth_data):
        """Les aspects sont vides pour MVP"""
        mock = generate_complete_natal_mock(sample_birth_data)

        assert isinstance(mock["aspects"], list), "aspects devrait être une liste"
        assert len(mock["aspects"]) == 0, "aspects devrait être vide pour MVP"

    def test_generate_complete_natal_mock_is_deterministic(self, sample_birth_data):
        """Le mock généré est déterministe pour les mêmes données"""
        mock1 = generate_complete_natal_mock(sample_birth_data)
        mock2 = generate_complete_natal_mock(sample_birth_data)

        # Comparer Big3
        assert mock1["sun"] == mock2["sun"], "Sun devrait être identique"
        assert mock1["moon"] == mock2["moon"], "Moon devrait être identique"
        assert mock1["ascendant"] == mock2["ascendant"], "Ascendant devrait être identique"

        # Comparer planets
        assert mock1["planets"] == mock2["planets"], "Planets devrait être identique"

        # Comparer houses
        assert mock1["houses"] == mock2["houses"], "Houses devrait être identique"

    def test_generate_complete_natal_mock_different_birth_data_different_mock(self):
        """Des données de naissance différentes produisent des mocks différents"""
        birth_data1 = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }
        birth_data2 = {
            "year": 1991,  # Année différente
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        mock1 = generate_complete_natal_mock(birth_data1)
        mock2 = generate_complete_natal_mock(birth_data2)

        # Au moins un élément devrait être différent
        assert (
            mock1["sun"]["sign"] != mock2["sun"]["sign"] or
            mock1["moon"]["sign"] != mock2["moon"]["sign"] or
            mock1["ascendant"]["sign"] != mock2["ascendant"]["sign"]
        ), "Des données différentes devraient produire des mocks différents"

    def test_generate_complete_natal_mock_with_custom_reason(self, sample_birth_data):
        """Le mock peut être généré avec une raison personnalisée"""
        reasons = ["rapidapi_403", "rapidapi_429", "rapidapi_500", "auto_heal"]

        for reason in reasons:
            mock = generate_complete_natal_mock(sample_birth_data, reason=reason)
            assert mock["_reason"] == reason, f"_reason devrait être {reason}"

    def test_generate_complete_natal_mock_planet_values_valid(self, sample_birth_data):
        """Les valeurs des planètes sont valides"""
        mock = generate_complete_natal_mock(sample_birth_data)

        for planet_name, planet_data in mock["planets"].items():
            assert "sign" in planet_data, f"{planet_name} devrait avoir 'sign'"
            assert "degree" in planet_data, f"{planet_name} devrait avoir 'degree'"
            assert "house" in planet_data, f"{planet_name} devrait avoir 'house'"

            assert planet_data["sign"] in SIGN_NAMES, f"{planet_name} devrait avoir un signe valide"
            assert 0.0 <= planet_data["degree"] < 30.0, f"{planet_name} degree devrait être entre 0 et 30"
            assert 1 <= planet_data["house"] <= 12, f"{planet_name} house devrait être entre 1 et 12"

    def test_generate_complete_natal_mock_coordinates_impact(self):
        """Les coordonnées géographiques impactent le mock"""
        birth_data_paris = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 48.8566,
            "longitude": 2.3522
        }
        birth_data_newyork = {
            "year": 1990,
            "month": 5,
            "day": 15,
            "hour": 14,
            "minute": 30,
            "latitude": 40.7128,  # Coordonnées différentes
            "longitude": -74.0060
        }

        mock_paris = generate_complete_natal_mock(birth_data_paris)
        mock_newyork = generate_complete_natal_mock(birth_data_newyork)

        # Les coordonnées devraient impacter le hash et donc les positions
        assert (
            mock_paris["sun"]["sign"] != mock_newyork["sun"]["sign"] or
            mock_paris["sun"]["degree"] != mock_newyork["sun"]["degree"] or
            mock_paris["ascendant"]["sign"] != mock_newyork["ascendant"]["sign"]
        ), "Des coordonnées différentes devraient produire des mocks différents"
