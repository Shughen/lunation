"""
Tests P0-2: Lunar Return Report avec authentification requise
Vérifie que la route nécessite auth et retourne 401 si non authentifié
"""

import pytest
from httpx import AsyncClient
from unittest.mock import patch

from main import app


@pytest.mark.asyncio
async def test_lunar_return_report_without_auth_returns_401():
    """
    P0-2 FIX TEST: Route /api/lunar/return/report doit nécessiter auth.
    Sans token ni DEV_AUTH_BYPASS, doit retourner 401.
    """
    valid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "17:55",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris",
        "date": "2025-01-15",
        "month": "2025-01"
    }

    # Désactiver DEV_AUTH_BYPASS pour ce test
    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            # Requête sans header Authorization
            response = await client.post("/api/lunar/return/report", json=valid_payload)

            # Doit retourner 401 Unauthorized
            assert response.status_code == 401


@pytest.mark.asyncio
async def test_lunar_return_report_with_dev_bypass_succeeds():
    """
    Test de régression: avec DEV_AUTH_BYPASS actif + header X-Dev-User-Id,
    la route doit fonctionner (200)
    """
    valid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "17:55",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris",
        "date": "2025-01-15",
        "month": "2025-01"
    }

    mock_response = {
        "moon": {"sign": "Taurus", "house": 2},
        "interpretation": "Test"
    }

    # Activer DEV_AUTH_BYPASS et mocker le service
    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'), \
         patch('services.lunar_services.get_lunar_return_report', return_value=mock_response):

        async with AsyncClient(app=app, base_url="http://test") as client:
            # Requête avec header X-Dev-User-Id
            response = await client.post(
                "/api/lunar/return/report",
                json=valid_payload,
                headers={"X-Dev-User-Id": "1"}
            )

            # Doit retourner 200
            assert response.status_code == 200

            data = response.json()
            assert data["provider"] == "rapidapi"
            assert data["kind"] == "lunar_return_report"
