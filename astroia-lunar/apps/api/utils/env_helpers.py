"""
Helpers pour parser les variables d'environnement de manière robuste
"""

import os
from typing import Optional


def env_bool(name: str, default: bool = False) -> bool:
    """
    Parse une variable d'environnement en booléen de manière robuste.

    Valeurs considérées comme True (case-insensitive, trimmed):
    - "1", "true", "yes", "y", "on"

    Valeurs considérées comme False (case-insensitive, trimmed):
    - "0", "false", "no", "n", "off"

    Si la variable n'existe pas ou est vide, retourne `default`.

    Args:
        name: Nom de la variable d'environnement
        default: Valeur par défaut si la variable n'existe pas ou est vide

    Returns:
        bool: La valeur parsée

    Examples:
        >>> os.environ["TEST_VAR"] = "1"
        >>> env_bool("TEST_VAR")
        True
        >>> os.environ["TEST_VAR"] = "0"
        >>> env_bool("TEST_VAR")
        False
        >>> os.environ["TEST_VAR"] = "false"
        >>> env_bool("TEST_VAR")
        False
        >>> os.environ["TEST_VAR"] = " True "
        >>> env_bool("TEST_VAR")
        True
        >>> env_bool("NON_EXISTENT", default=True)
        True
    """
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    return raw.strip().lower() in {"1", "true", "yes", "y", "on"}
