"""
Tests d'intégration pour le parsing des booléens dans config.py
Vérifie que les variables d'environnement DEV_MOCK_* sont correctement parsées.
"""

import pytest
import os
from config import Settings


class TestConfigBoolParsing:
    """Tests d'intégration pour le parsing des flags booléens dans Settings"""

    def test_dev_mock_natal_false_when_zero(self, monkeypatch):
        """Test: DEV_MOCK_NATAL=0 doit être False"""
        monkeypatch.setenv("DEV_MOCK_NATAL", "0")
        settings = Settings()
        assert settings.DEV_MOCK_NATAL is False

    def test_dev_mock_ephemeris_false_when_zero(self, monkeypatch):
        """Test: DEV_MOCK_EPHEMERIS=0 doit être False"""
        monkeypatch.setenv("DEV_MOCK_EPHEMERIS", "0")
        settings = Settings()
        assert settings.DEV_MOCK_EPHEMERIS is False

    def test_dev_mock_rapidapi_false_when_false_string(self, monkeypatch):
        """Test: DEV_MOCK_RAPIDAPI=false doit être False"""
        monkeypatch.setenv("DEV_MOCK_RAPIDAPI", "false")
        settings = Settings()
        assert settings.DEV_MOCK_RAPIDAPI is False

    def test_dev_mock_natal_true_when_one(self, monkeypatch):
        """Test: DEV_MOCK_NATAL=1 doit être True"""
        monkeypatch.setenv("DEV_MOCK_NATAL", "1")
        settings = Settings()
        assert settings.DEV_MOCK_NATAL is True

    def test_dev_mock_ephemeris_true_when_true_string(self, monkeypatch):
        """Test: DEV_MOCK_EPHEMERIS=true doit être True"""
        monkeypatch.setenv("DEV_MOCK_EPHEMERIS", "true")
        settings = Settings()
        assert settings.DEV_MOCK_EPHEMERIS is True

    def test_dev_mock_rapidapi_true_when_yes(self, monkeypatch):
        """Test: DEV_MOCK_RAPIDAPI=yes doit être True"""
        monkeypatch.setenv("DEV_MOCK_RAPIDAPI", "yes")
        settings = Settings()
        assert settings.DEV_MOCK_RAPIDAPI is True

    def test_dev_auth_bypass_false_when_off(self, monkeypatch):
        """Test: DEV_AUTH_BYPASS=off doit être False"""
        monkeypatch.setenv("DEV_AUTH_BYPASS", "off")
        settings = Settings()
        assert settings.DEV_AUTH_BYPASS is False

    def test_allow_dev_purge_true_when_on(self, monkeypatch):
        """Test: ALLOW_DEV_PURGE=on doit être True"""
        monkeypatch.setenv("ALLOW_DEV_PURGE", "on")
        settings = Settings()
        assert settings.ALLOW_DEV_PURGE is True

    def test_disable_chiron_false_when_no(self, monkeypatch):
        """Test: DISABLE_CHIRON=no doit être False"""
        monkeypatch.setenv("DISABLE_CHIRON", "no")
        settings = Settings()
        assert settings.DISABLE_CHIRON is False

    @pytest.mark.parametrize("value", ["0", "false", "False", "no", "off"])
    def test_all_dev_mock_flags_false_values(self, monkeypatch, value):
        """Test: tous les flags DEV_MOCK_* reconnaissent les valeurs falsy"""
        monkeypatch.setenv("DEV_MOCK_NATAL", value)
        monkeypatch.setenv("DEV_MOCK_EPHEMERIS", value)
        monkeypatch.setenv("DEV_MOCK_RAPIDAPI", value)

        settings = Settings()

        assert settings.DEV_MOCK_NATAL is False, f"DEV_MOCK_NATAL should be False when set to '{value}'"
        assert settings.DEV_MOCK_EPHEMERIS is False, f"DEV_MOCK_EPHEMERIS should be False when set to '{value}'"
        assert settings.DEV_MOCK_RAPIDAPI is False, f"DEV_MOCK_RAPIDAPI should be False when set to '{value}'"

    @pytest.mark.parametrize("value", ["1", "true", "True", "yes", "on"])
    def test_all_dev_mock_flags_true_values(self, monkeypatch, value):
        """Test: tous les flags DEV_MOCK_* reconnaissent les valeurs truthy"""
        monkeypatch.setenv("DEV_MOCK_NATAL", value)
        monkeypatch.setenv("DEV_MOCK_EPHEMERIS", value)
        monkeypatch.setenv("DEV_MOCK_RAPIDAPI", value)

        settings = Settings()

        assert settings.DEV_MOCK_NATAL is True, f"DEV_MOCK_NATAL should be True when set to '{value}'"
        assert settings.DEV_MOCK_EPHEMERIS is True, f"DEV_MOCK_EPHEMERIS should be True when set to '{value}'"
        assert settings.DEV_MOCK_RAPIDAPI is True, f"DEV_MOCK_RAPIDAPI should be True when set to '{value}'"

    def test_whitespace_trimming(self, monkeypatch):
        """Test: les espaces sont correctement trimés"""
        monkeypatch.setenv("DEV_MOCK_NATAL", " 1 ")
        monkeypatch.setenv("DEV_MOCK_EPHEMERIS", "  false  ")
        monkeypatch.setenv("DEV_MOCK_RAPIDAPI", " true ")

        settings = Settings()

        assert settings.DEV_MOCK_NATAL is True
        assert settings.DEV_MOCK_EPHEMERIS is False
        assert settings.DEV_MOCK_RAPIDAPI is True

    def test_case_insensitive_parsing(self, monkeypatch):
        """Test: le parsing est case-insensitive"""
        monkeypatch.setenv("DEV_MOCK_NATAL", "TRUE")
        monkeypatch.setenv("DEV_MOCK_EPHEMERIS", "False")
        monkeypatch.setenv("DEV_MOCK_RAPIDAPI", "YeS")

        settings = Settings()

        assert settings.DEV_MOCK_NATAL is True
        assert settings.DEV_MOCK_EPHEMERIS is False
        assert settings.DEV_MOCK_RAPIDAPI is True

    def test_simulation_env_file_with_zeros(self, monkeypatch):
        """
        Test: simulation du scénario réel du .env avec DEV_MOCK_*=0
        Ce test simule exactement le problème initial rapporté.
        """
        # Simulate .env file content
        monkeypatch.setenv("DEV_MOCK_NATAL", "0")
        monkeypatch.setenv("DEV_MOCK_EPHEMERIS", "0")
        monkeypatch.setenv("DEV_MOCK_RAPIDAPI", "false")

        settings = Settings()

        # These MUST all be False
        assert settings.DEV_MOCK_NATAL is False, "DEV_MOCK_NATAL should be False when .env has '0'"
        assert settings.DEV_MOCK_EPHEMERIS is False, "DEV_MOCK_EPHEMERIS should be False when .env has '0'"
        assert settings.DEV_MOCK_RAPIDAPI is False, "DEV_MOCK_RAPIDAPI should be False when .env has 'false'"
