"""
Tests unitaires pour utils/env_helpers.py
"""

import pytest
import os
from utils.env_helpers import env_bool


class TestEnvBool:
    """Tests pour la fonction env_bool()"""

    def test_env_bool_returns_default_when_not_set(self):
        """Test: retourne default quand la variable n'existe pas"""
        # Ensure variable doesn't exist
        if "TEST_NONEXISTENT_VAR" in os.environ:
            del os.environ["TEST_NONEXISTENT_VAR"]

        assert env_bool("TEST_NONEXISTENT_VAR", default=False) is False
        assert env_bool("TEST_NONEXISTENT_VAR", default=True) is True

    def test_env_bool_returns_default_when_empty(self):
        """Test: retourne default quand la variable est vide"""
        os.environ["TEST_EMPTY_VAR"] = ""
        try:
            assert env_bool("TEST_EMPTY_VAR", default=False) is False
            assert env_bool("TEST_EMPTY_VAR", default=True) is True
        finally:
            del os.environ["TEST_EMPTY_VAR"]

    def test_env_bool_returns_default_when_whitespace(self):
        """Test: retourne default quand la variable ne contient que des espaces"""
        os.environ["TEST_WHITESPACE_VAR"] = "   "
        try:
            assert env_bool("TEST_WHITESPACE_VAR", default=False) is False
            assert env_bool("TEST_WHITESPACE_VAR", default=True) is True
        finally:
            del os.environ["TEST_WHITESPACE_VAR"]

    @pytest.mark.parametrize("value", ["1", "true", "True", "TRUE", "yes", "Yes", "YES", "y", "Y", "on", "On", "ON"])
    def test_env_bool_true_values(self, value):
        """Test: reconnaît les valeurs truthy (case-insensitive)"""
        os.environ["TEST_BOOL_VAR"] = value
        try:
            assert env_bool("TEST_BOOL_VAR") is True
        finally:
            del os.environ["TEST_BOOL_VAR"]

    @pytest.mark.parametrize("value", ["0", "false", "False", "FALSE", "no", "No", "NO", "n", "N", "off", "Off", "OFF"])
    def test_env_bool_false_values(self, value):
        """Test: reconnaît les valeurs falsy (case-insensitive)"""
        os.environ["TEST_BOOL_VAR"] = value
        try:
            assert env_bool("TEST_BOOL_VAR") is False
        finally:
            del os.environ["TEST_BOOL_VAR"]

    @pytest.mark.parametrize("value", [" 1 ", "  true  ", " True ", " YES ", "  on  "])
    def test_env_bool_trims_whitespace_true(self, value):
        """Test: trim les espaces avant/après pour valeurs truthy"""
        os.environ["TEST_BOOL_VAR"] = value
        try:
            assert env_bool("TEST_BOOL_VAR") is True
        finally:
            del os.environ["TEST_BOOL_VAR"]

    @pytest.mark.parametrize("value", [" 0 ", "  false  ", " False ", " NO ", "  off  "])
    def test_env_bool_trims_whitespace_false(self, value):
        """Test: trim les espaces avant/après pour valeurs falsy"""
        os.environ["TEST_BOOL_VAR"] = value
        try:
            assert env_bool("TEST_BOOL_VAR") is False
        finally:
            del os.environ["TEST_BOOL_VAR"]

    @pytest.mark.parametrize("value", ["oui", "non", "vrai", "faux", "2", "invalid", "null"])
    def test_env_bool_invalid_values_are_false(self, value):
        """Test: valeurs invalides sont considérées comme False"""
        os.environ["TEST_BOOL_VAR"] = value
        try:
            assert env_bool("TEST_BOOL_VAR") is False
        finally:
            del os.environ["TEST_BOOL_VAR"]

    def test_env_bool_default_is_false(self):
        """Test: le default par défaut est False"""
        if "TEST_NONEXISTENT_VAR" in os.environ:
            del os.environ["TEST_NONEXISTENT_VAR"]

        # When default is not specified, it should be False
        assert env_bool("TEST_NONEXISTENT_VAR") is False
