"""
Tests d'intégration pour les endpoints Luna Pack (/api/lunar/voc et /api/lunar/mansion)
Teste le format flat du payload et les codes d'erreur provider (502/504)

IMPORTANT: Pour les tests V2 (lunar_interpretation), on utilise des UUID strings
car SQLite ne supporte pas les UUID natifs. Les patches dans conftest.py
convertissent automatiquement UUID -> String(36).
"""

import pytest
from unittest.mock import patch, AsyncMock
from fastapi import HTTPException
from httpx import AsyncClient
import uuid

from main import app


@pytest.mark.asyncio
async def test_voc_success_with_flat_payload():
    """Test /api/lunar/voc - succès avec payload flat (format HH:MM)"""
    mock_response = {
        "is_void": True,
        "void_of_course": {
            "start": "2025-12-31T10:30:00",
            "end": "2025-12-31T14:45:00"
        },
        "moon_sign": "Gemini"
    }

    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/voc", json=flat_payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier la structure de réponse
            assert data["provider"] == "rapidapi"
            assert data["kind"] == "void_of_course"
            assert data["data"] == mock_response
            assert data["cached"] is False

            # Vérifier que le payload a été transformé correctement
            call_args = mock_post.call_args
            transformed_payload = call_args[0][1]
            assert "datetime_location" in transformed_payload
            dtl = transformed_payload["datetime_location"]
            assert dtl["year"] == 2025
            assert dtl["month"] == 12
            assert dtl["day"] == 31
            assert dtl["hour"] == 12
            assert dtl["minute"] == 0
            assert dtl["second"] == 0
            assert dtl["latitude"] == 48.8566
            assert dtl["longitude"] == 2.3522
            assert dtl["timezone"] == "Europe/Paris"


@pytest.mark.asyncio
async def test_voc_success_with_time_hh_mm_ss():
    """Test /api/lunar/voc - accepte le format HH:MM:SS pour time"""
    mock_response = {
        "is_void": False,
        "next_void": {
            "start": "2025-12-31T18:00:00",
            "end": "2025-12-31T22:30:00"
        }
    }

    payload_with_seconds = {
        "date": "2025-12-31",
        "time": "14:30:45",  # Format HH:MM:SS
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/voc", json=payload_with_seconds)

            assert response.status_code == 200
            data = response.json()
            assert data["data"] == mock_response

            # Vérifier que les secondes sont ignorées (toujours 0)
            transformed_payload = mock_post.call_args[0][1]
            dtl = transformed_payload["datetime_location"]
            assert dtl["hour"] == 14
            assert dtl["minute"] == 30
            assert dtl["second"] == 0


@pytest.mark.asyncio
async def test_voc_provider_error_502():
    """Test /api/lunar/voc - erreur provider 5xx renvoie bien 502"""
    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    # Simuler une erreur 502 du provider
    error_detail = {
        "code": "PROVIDER_UNAVAILABLE",
        "message": "Service astrologique indisponible après 3 tentatives (HTTP 503)",
        "provider_error": {"error": "Service unavailable"}
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail=error_detail)):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/voc", json=flat_payload)

            # Vérifier que l'erreur 502 est bien propagée (pas 500)
            assert response.status_code == 502
            error_data = response.json()
            assert error_data["detail"]["code"] == "PROVIDER_UNAVAILABLE"


@pytest.mark.asyncio
async def test_voc_provider_timeout_504():
    """Test /api/lunar/voc - timeout provider renvoie bien 504"""
    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    # Simuler un timeout (504)
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=504, detail="Timeout provider après 3 tentatives")):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/voc", json=flat_payload)

            # Vérifier que l'erreur 504 est bien propagée (pas 500)
            assert response.status_code == 504
            assert "timeout" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_voc_invalid_payload_422():
    """Test /api/lunar/voc - payload invalide renvoie 422 (pas 500 ni 502)"""
    invalid_payload = {
        "date": "2025-12-31",
        # time manquant -> ValueError dans transformation
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/lunar/voc", json=invalid_payload)

        # Vérifier que c'est bien une 422 (erreur de validation)
        assert response.status_code == 422
        error_data = response.json()
        assert error_data["detail"]["code"] == "INVALID_PAYLOAD"
        assert "time" in error_data["detail"]["message"].lower()


@pytest.mark.asyncio
async def test_mansion_success_with_flat_payload():
    """Test /api/lunar/mansion - succès avec payload flat"""
    mock_response = {
        "mansion": {
            "number": 14,
            "name": "Al-Simak",
            "interpretation": "Favorable aux nouveaux projets"
        },
        "upcoming_changes": [
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            },
            {
                "change_time": "2026-01-01T16:45:00",
                "from_mansion": {"number": 15, "name": "Al-Ghafr"},
                "to_mansion": {"number": 16, "name": "Az-Zubana"}
            }
        ],
        "calendar_summary": {
            "significant_periods": [
                {
                    "change_time": "2025-12-31T15:30:00",
                    "from_mansion": {"number": 14, "name": "Al-Simak"},
                    "to_mansion": {"number": 15, "name": "Al-Ghafr"}
                },
                {
                    "change_time": "2026-01-01T16:45:00",
                    "from_mansion": {"number": 15, "name": "Al-Ghafr"},
                    "to_mansion": {"number": 16, "name": "Az-Zubana"}
                }
            ]
        }
    }

    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=flat_payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier la structure de réponse
            assert data["provider"] == "rapidapi"
            assert data["kind"] == "lunar_mansion"
            assert data["data"] == mock_response
            assert data["cached"] is False

            # Vérifier que le payload a été transformé correctement
            call_args = mock_post.call_args
            transformed_payload = call_args[0][1]
            assert "datetime_location" in transformed_payload
            dtl = transformed_payload["datetime_location"]
            assert dtl["year"] == 2025
            assert dtl["month"] == 12
            assert dtl["day"] == 31
            assert dtl["hour"] == 12
            assert dtl["minute"] == 0
            assert dtl["second"] == 0


@pytest.mark.asyncio
async def test_mansion_success_with_time_hh_mm_ss():
    """Test /api/lunar/mansion - accepte le format HH:MM:SS pour time"""
    mock_response = {
        "mansion": {
            "number": 7,
            "name": "Al-Dhira",
            "interpretation": "Test"
        }
    }

    payload_with_seconds = {
        "date": "2025-12-31",
        "time": "18:45:30",  # Format HH:MM:SS
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=payload_with_seconds)

            assert response.status_code == 200
            data = response.json()
            assert data["data"] == mock_response

            # Vérifier que les secondes sont ignorées
            transformed_payload = mock_post.call_args[0][1]
            dtl = transformed_payload["datetime_location"]
            assert dtl["hour"] == 18
            assert dtl["minute"] == 45
            assert dtl["second"] == 0


@pytest.mark.asyncio
async def test_mansion_provider_error_502():
    """Test /api/lunar/mansion - erreur provider 5xx renvoie bien 502"""
    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    # Simuler une erreur 502 du provider
    error_detail = {
        "code": "PROVIDER_UNAVAILABLE",
        "message": "Service astrologique indisponible après 3 tentatives (HTTP 500)",
        "provider_error": {"error": "Internal server error"}
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail=error_detail)):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=flat_payload)

            # Vérifier que l'erreur 502 est bien propagée (pas 500)
            assert response.status_code == 502
            error_data = response.json()
            assert error_data["detail"]["code"] == "PROVIDER_UNAVAILABLE"


@pytest.mark.asyncio
async def test_mansion_provider_timeout_504():
    """Test /api/lunar/mansion - timeout provider renvoie bien 504"""
    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    # Simuler un timeout (504)
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=504, detail="Timeout provider après 3 tentatives")):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=flat_payload)

            # Vérifier que l'erreur 504 est bien propagée (pas 500)
            assert response.status_code == 504
            assert "timeout" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_mansion_invalid_payload_422():
    """Test /api/lunar/mansion - payload invalide renvoie 422 (pas 500 ni 502)"""
    invalid_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        # latitude manquante -> ValueError dans transformation
        "longitude": 2.3522
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/lunar/mansion", json=invalid_payload)

        # Vérifier que c'est bien une 422 (erreur de validation)
        assert response.status_code == 422
        error_data = response.json()
        assert error_data["detail"]["code"] == "INVALID_PAYLOAD"
        assert "latitude" in error_data["detail"]["message"].lower()


@pytest.mark.asyncio
async def test_voc_and_mansion_use_same_datetime_location_format():
    """Test que VoC et Mansion utilisent le même format datetime_location"""
    mock_voc_response = {"is_void": False}
    mock_mansion_response = {"mansion": {"number": 1, "name": "Al-Sharatain"}}

    payload = {
        "date": "2025-12-31",
        "time": "23:59",
        "latitude": -33.9249,
        "longitude": 18.4241,
        "timezone": "Africa/Johannesburg"
    }

    # Test VoC transformation
    with patch('services.rapidapi_client.post_json', return_value=mock_voc_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            await client.post("/api/lunar/voc", json=payload)

            voc_transformed = mock_post.call_args[0][1]
            assert "datetime_location" in voc_transformed
            voc_dtl = voc_transformed["datetime_location"]

    # Test Mansion transformation
    with patch('services.rapidapi_client.post_json', return_value=mock_mansion_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            await client.post("/api/lunar/mansion", json=payload)

            mansion_transformed = mock_post.call_args[0][1]
            assert "datetime_location" in mansion_transformed
            mansion_dtl = mansion_transformed["datetime_location"]

    # Vérifier que les deux transformations sont identiques
    assert voc_dtl == mansion_dtl
    assert mansion_dtl["year"] == 2025
    assert mansion_dtl["month"] == 12
    assert mansion_dtl["day"] == 31
    assert mansion_dtl["hour"] == 23
    assert mansion_dtl["minute"] == 59
    assert mansion_dtl["second"] == 0
    assert mansion_dtl["latitude"] == -33.9249
    assert mansion_dtl["longitude"] == 18.4241
    assert mansion_dtl["timezone"] == "Africa/Johannesburg"


@pytest.mark.asyncio
async def test_mansion_deduplication_upcoming_changes():
    """Test que la déduplication fonctionne sur upcoming_changes"""
    # Mock response avec doublons dans upcoming_changes
    mock_response_with_duplicates = {
        "mansion": {
            "number": 14,
            "name": "Al-Simak"
        },
        "upcoming_changes": [
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            },
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            },  # Doublon exact
            {
                "change_time": "2026-01-01T16:45:00",
                "from_mansion": {"number": 15, "name": "Al-Ghafr"},
                "to_mansion": {"number": 16, "name": "Az-Zubana"}
            }
        ]
    }

    payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response_with_duplicates):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier que les doublons ont été supprimés
            upcoming_changes = data["data"]["upcoming_changes"]
            assert len(upcoming_changes) == 2  # Au lieu de 3

            # Vérifier que les entrées uniques sont conservées
            assert upcoming_changes[0]["change_time"] == "2025-12-31T15:30:00"
            assert upcoming_changes[0]["from_mansion"]["number"] == 14
            assert upcoming_changes[0]["to_mansion"]["name"] == "Al-Ghafr"

            assert upcoming_changes[1]["change_time"] == "2026-01-01T16:45:00"
            assert upcoming_changes[1]["from_mansion"]["number"] == 15
            assert upcoming_changes[1]["to_mansion"]["name"] == "Az-Zubana"


@pytest.mark.asyncio
async def test_mansion_deduplication_calendar_summary():
    """Test que la déduplication fonctionne sur calendar_summary.significant_periods"""
    # Mock response avec doublons dans significant_periods
    mock_response_with_duplicates = {
        "mansion": {
            "number": 7,
            "name": "Al-Dhira"
        },
        "calendar_summary": {
            "significant_periods": [
                {
                    "change_time": "2025-12-31T10:00:00",
                    "from_mansion": {"number": 7, "name": "Al-Dhira"},
                    "to_mansion": {"number": 8, "name": "An-Nathrah"}
                },
                {
                    "change_time": "2025-12-31T10:00:00",
                    "from_mansion": {"number": 7, "name": "Al-Dhira"},
                    "to_mansion": {"number": 8, "name": "An-Nathrah"}
                },  # Doublon exact
                {
                    "change_time": "2025-12-31T10:00:00",
                    "from_mansion": {"number": 7, "name": "Al-Dhira"},
                    "to_mansion": {"number": 8, "name": "An-Nathrah"}
                },  # Triple
                {
                    "change_time": "2026-01-02T14:00:00",
                    "from_mansion": {"number": 8, "name": "An-Nathrah"},
                    "to_mansion": {"number": 9, "name": "At-Tarf"}
                }
            ]
        }
    }

    payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response_with_duplicates):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier que les doublons ont été supprimés
            significant_periods = data["data"]["calendar_summary"]["significant_periods"]
            assert len(significant_periods) == 2  # Au lieu de 4

            # Vérifier que les entrées uniques sont conservées
            assert significant_periods[0]["change_time"] == "2025-12-31T10:00:00"
            assert significant_periods[1]["change_time"] == "2026-01-02T14:00:00"


@pytest.mark.asyncio
async def test_mansion_deduplication_both():
    """Test que la déduplication fonctionne sur les deux listes en même temps"""
    # Mock response avec doublons dans les deux listes
    mock_response_with_duplicates = {
        "mansion": {
            "number": 14,
            "name": "Al-Simak"
        },
        "upcoming_changes": [
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            },
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            }
        ],
        "calendar_summary": {
            "significant_periods": [
                {
                    "change_time": "2025-12-31T15:30:00",
                    "from_mansion": {"number": 14, "name": "Al-Simak"},
                    "to_mansion": {"number": 15, "name": "Al-Ghafr"}
                },
                {
                    "change_time": "2025-12-31T15:30:00",
                    "from_mansion": {"number": 14, "name": "Al-Simak"},
                    "to_mansion": {"number": 15, "name": "Al-Ghafr"}
                }
            ]
        }
    }

    payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response_with_duplicates):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier que les doublons ont été supprimés dans les deux listes
            upcoming_changes = data["data"]["upcoming_changes"]
            assert len(upcoming_changes) == 1

            significant_periods = data["data"]["calendar_summary"]["significant_periods"]
            assert len(significant_periods) == 1


# ============================================================================
# TESTS INTÉGRATION LUNAR INTERPRETATION V2 (Agent B - Vague 4)
# ============================================================================

import pytest_asyncio
from sqlalchemy import text
from database import AsyncSessionLocal


@pytest_asyncio.fixture
async def async_db_real():
    """
    Fixture qui crée une session DB PostgreSQL réelle pour tests d'intégration.
    Skip automatiquement si DB inaccessible.
    """
    async with AsyncSessionLocal() as session:
        # Tester la connexion
        try:
            await session.execute(text("SELECT 1"))
        except Exception as e:
            pytest.skip(f"DB not accessible (required for integration tests): {str(e)[:100]}")

        yield session


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_cache_hit(async_db_real):
    """Test 1: Cache DB temporelle - Cache Hit

    Vérifie qu'une interprétation existante est retournée depuis le cache DB
    sans régénération Claude.
    """
    from models import LunarReturn, LunarInterpretation
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from datetime import datetime, timezone

    # Créer un LunarReturn en DB
    lunar_return = LunarReturn(
        user_id=1,
        month="2025-01",
        return_date=datetime(2025, 1, 15, tzinfo=timezone.utc),
        moon_sign="Aries",
        moon_house=1,
        lunar_ascendant="Leo",
        aspects=[],
        planets={},
        houses={}
    )
    async_db_real.add(lunar_return)
    await async_db_real.commit()
    await async_db_real.refresh(lunar_return)

    # Créer une interprétation en cache DB
    cached_interpretation = LunarInterpretation(
        user_id=1,
        lunar_return_id=lunar_return.id,
        subject='full',
        version=2,
        lang='fr',
        input_json={'test': 'context'},
        output_text='Cached interpretation text',
        weekly_advice={'week1': 'Advice 1'},
        model_used='claude-opus-4-5'
    )
    async_db_real.add(cached_interpretation)
    await async_db_real.commit()

    # Appeler generate_or_get_interpretation
    output_text, weekly_advice, source, model_used = await generate_or_get_interpretation(
        db=async_db_real,
        lunar_return_id=lunar_return.id,
        user_id=1,
        subject='full',
        version=2,
        lang='fr'
    )

    # Assertions
    assert source == 'db_temporal', "Source devrait être db_temporal (cache hit)"
    assert output_text == 'Cached interpretation text'
    assert weekly_advice == {'week1': 'Advice 1'}
    assert model_used == 'claude-opus-4-5'

    # Cleanup
    await async_db_real.delete(cached_interpretation)
    await async_db_real.delete(lunar_return)
    await async_db_real.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_cache_miss_then_fallback(async_db_real):
    """Test 2: Cache DB temporelle - Cache Miss puis Fallback Template

    Vérifie qu'une interprétation manquante déclenche le fallback vers templates.
    (On mock Claude pour forcer le fallback vers templates DB)
    """
    from models import LunarReturn, LunarInterpretationTemplate
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from datetime import datetime, timezone

    # Créer un LunarReturn en DB
    lunar_return = LunarReturn(
        user_id=1,
        month="2025-02",
        return_date=datetime(2025, 2, 15, tzinfo=timezone.utc),
        moon_sign="Taurus",
        moon_house=2,
        lunar_ascendant="Virgo",
        aspects=[],
        planets={},
        houses={}
    )
    async_db_real.add(lunar_return)
    await async_db_real.commit()
    await async_db_real.refresh(lunar_return)

    # Créer un template fallback en DB
    template = LunarInterpretationTemplate(
        template_type='full',
        moon_sign='Taurus',
        moon_house=2,
        lunar_ascendant='Virgo',
        version=2,
        lang='fr',
        template_text='Template fallback text for Taurus/2/Virgo',
        weekly_advice_template={'week1': 'Template advice'},
        model_used='template'
    )
    async_db_real.add(template)
    await async_db_real.commit()

    # Mock Claude API pour forcer l'échec (fallback vers templates)
    with patch('services.lunar_interpretation_generator._generate_via_claude') as mock_claude:
        from services.lunar_interpretation_generator import ClaudeAPIError
        mock_claude.side_effect = ClaudeAPIError("Mocked Claude failure")

        # Appeler generate_or_get_interpretation
        output_text, weekly_advice, source, model_used = await generate_or_get_interpretation(
            db=async_db_real,
            lunar_return_id=lunar_return.id,
            user_id=1,
            subject='full',
            version=2,
            lang='fr'
        )

        # Assertions
        assert source == 'db_template', "Source devrait être db_template après échec Claude"
        assert output_text == 'Template fallback text for Taurus/2/Virgo'
        assert weekly_advice == {'week1': 'Template advice'}
        assert model_used == 'template'

    # Cleanup
    await async_db_real.delete(template)
    await async_db_real.delete(lunar_return)
    await async_db_real.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_idempotence(async_db_real):
    """Test 3: Cache DB temporelle - Idempotence

    Vérifie que deux appels consécutifs avec mêmes paramètres retournent
    la même interprétation (même ID, même contenu).
    """
    from models import LunarReturn, LunarInterpretation
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from datetime import datetime, timezone
    from sqlalchemy import select

    # Créer un LunarReturn en DB
    lunar_return = LunarReturn(
        user_id=1,
        month="2025-03",
        return_date=datetime(2025, 3, 15, tzinfo=timezone.utc),
        moon_sign="Gemini",
        moon_house=3,
        lunar_ascendant="Libra",
        aspects=[],
        planets={},
        houses={}
    )
    async_db_real.add(lunar_return)
    await async_db_real.commit()
    await async_db_real.refresh(lunar_return)

    # Mock Claude pour retourner une génération
    with patch('services.lunar_interpretation_generator._generate_via_claude') as mock_claude:
        mock_claude.return_value = (
            'Generated interpretation',
            {'week1': 'Generated advice'},
            {'test': 'input'}
        )

        # Premier appel (génération)
        output1, advice1, source1, model1 = await generate_or_get_interpretation(
            db=async_db_real,
            lunar_return_id=lunar_return.id,
            user_id=1,
            subject='full',
            version=2,
            lang='fr'
        )

        # Vérifier qu'on a généré via Claude
        assert source1 == 'claude'
        assert mock_claude.call_count == 1

    # Deuxième appel (cache hit) - SANS mock Claude
    output2, advice2, source2, model2 = await generate_or_get_interpretation(
        db=async_db_real,
        lunar_return_id=lunar_return.id,
        user_id=1,
        subject='full',
        version=2,
        lang='fr'
    )

    # Assertions idempotence
    assert source2 == 'db_temporal', "Deuxième appel devrait être un cache hit"
    assert output1 == output2, "Output devrait être identique"
    assert advice1 == advice2, "Weekly advice devrait être identique"
    assert model1 == model2, "Model used devrait être identique"

    # Cleanup
    result = await async_db_real.execute(
        select(LunarInterpretation).filter_by(lunar_return_id=lunar_return.id)
    )
    interpretations = result.scalars().all()
    for interp in interpretations:
        await async_db_real.delete(interp)
    await async_db_real.delete(lunar_return)
    await async_db_real.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_fallback_template_lookup(async_db_real):
    """Test 4: Fallback Templates - Lookup par critères

    Vérifie que le lookup de templates fonctionne correctement selon le type
    de sujet (full, climate, focus, approach).
    """
    from models import LunarReturn, LunarInterpretationTemplate
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from datetime import datetime, timezone

    # Créer un LunarReturn
    lunar_return = LunarReturn(
        user_id=1,
        month="2025-04",
        return_date=datetime(2025, 4, 15, tzinfo=timezone.utc),
        moon_sign="Cancer",
        moon_house=4,
        lunar_ascendant="Scorpio",
        aspects=[],
        planets={},
        houses={}
    )
    async_db_real.add(lunar_return)
    await async_db_real.commit()
    await async_db_real.refresh(lunar_return)

    # Créer un template 'climate' (utilise uniquement moon_sign)
    template_climate = LunarInterpretationTemplate(
        template_type='climate',
        moon_sign='Cancer',
        moon_house=None,
        lunar_ascendant=None,
        version=2,
        lang='fr',
        template_text='Climate template for Cancer',
        model_used='template'
    )
    async_db_real.add(template_climate)
    await async_db_real.commit()

    # Mock Claude pour forcer fallback
    with patch('services.lunar_interpretation_generator._generate_via_claude') as mock_claude:
        from services.lunar_interpretation_generator import ClaudeAPIError
        mock_claude.side_effect = ClaudeAPIError("Mocked failure")

        # Appeler avec subject='climate'
        output, advice, source, model = await generate_or_get_interpretation(
            db=async_db_real,
            lunar_return_id=lunar_return.id,
            user_id=1,
            subject='climate',
            version=2,
            lang='fr'
        )

        # Assertions
        assert source == 'db_template'
        assert output == 'Climate template for Cancer'
        assert 'Cancer' in output

    # Cleanup
    await async_db_real.delete(template_climate)
    await async_db_real.delete(lunar_return)
    await async_db_real.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_fallback_hierarchy(async_db_real):
    """Test 5: Fallback Templates - Hiérarchie complète

    Vérifie que la hiérarchie de fallback fonctionne :
    DB temporelle → Claude → DB templates → Hardcoded
    """
    from models import LunarReturn
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from datetime import datetime, timezone

    # Créer un LunarReturn sans template DB
    lunar_return = LunarReturn(
        user_id=1,
        month="2025-05",
        return_date=datetime(2025, 5, 15, tzinfo=timezone.utc),
        moon_sign="Leo",
        moon_house=5,
        lunar_ascendant="Sagittarius",
        aspects=[],
        planets={},
        houses={}
    )
    async_db_real.add(lunar_return)
    await async_db_real.commit()
    await async_db_real.refresh(lunar_return)

    # Mock Claude pour forcer fallback (pas de template DB = fallback hardcoded)
    with patch('services.lunar_interpretation_generator._generate_via_claude') as mock_claude:
        from services.lunar_interpretation_generator import ClaudeAPIError
        mock_claude.side_effect = ClaudeAPIError("Mocked failure")

        # Appeler generate_or_get_interpretation
        output, advice, source, model = await generate_or_get_interpretation(
            db=async_db_real,
            lunar_return_id=lunar_return.id,
            user_id=1,
            subject='full',
            version=2,
            lang='fr'
        )

        # Assertions - devrait fallback vers hardcoded
        assert source == 'hardcoded', "Devrait fallback vers hardcoded si pas de template DB"
        assert model == 'placeholder'
        assert output is not None and len(output) > 0

    # Cleanup
    await async_db_real.delete(lunar_return)
    await async_db_real.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_model_used_persistence(async_db_real):
    """Test 6: Metadata Persistence - model_used

    Vérifie que le champ model_used est correctement persisté en DB
    lors de la génération.
    """
    from models import LunarReturn, LunarInterpretation
    from services.lunar_interpretation_generator import generate_or_get_interpretation, CLAUDE_MODELS
    from datetime import datetime, timezone
    from sqlalchemy import select

    # Créer un LunarReturn
    lunar_return = LunarReturn(
        user_id=1,
        month="2025-06",
        return_date=datetime(2025, 6, 15, tzinfo=timezone.utc),
        moon_sign="Virgo",
        moon_house=6,
        lunar_ascendant="Capricorn",
        aspects=[],
        planets={},
        houses={}
    )
    async_db_real.add(lunar_return)
    await async_db_real.commit()
    await async_db_real.refresh(lunar_return)

    # Mock Claude pour simuler génération
    with patch('services.lunar_interpretation_generator._generate_via_claude') as mock_claude:
        mock_claude.return_value = (
            'Generated text',
            {'week1': 'Advice'},
            {'test': 'input'}
        )

        # Générer interprétation
        output, advice, source, model_used = await generate_or_get_interpretation(
            db=async_db_real,
            lunar_return_id=lunar_return.id,
            user_id=1,
            subject='full',
            version=2,
            lang='fr'
        )

        # Vérifier que model_used est retourné
        assert model_used == CLAUDE_MODELS['opus']

    # Vérifier en DB
    result = await async_db_real.execute(
        select(LunarInterpretation).filter_by(
            lunar_return_id=lunar_return.id,
            subject='full'
        )
    )
    interpretation = result.scalar_one_or_none()

    assert interpretation is not None
    assert interpretation.model_used == CLAUDE_MODELS['opus']

    # Cleanup
    await async_db_real.delete(interpretation)
    await async_db_real.delete(lunar_return)
    await async_db_real.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_weekly_advice_persistence(async_db_real):
    """Test 7: Metadata Persistence - weekly_advice

    Vérifie que le champ weekly_advice (JSONB) est correctement persisté
    lors de la génération avec subject='full'.
    """
    from models import LunarReturn, LunarInterpretation
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from datetime import datetime, timezone
    from sqlalchemy import select

    # Créer un LunarReturn
    lunar_return = LunarReturn(
        user_id=1,
        month="2025-07",
        return_date=datetime(2025, 7, 15, tzinfo=timezone.utc),
        moon_sign="Libra",
        moon_house=7,
        lunar_ascendant="Aquarius",
        aspects=[],
        planets={},
        houses={}
    )
    async_db_real.add(lunar_return)
    await async_db_real.commit()
    await async_db_real.refresh(lunar_return)

    # Mock Claude avec weekly_advice structuré
    weekly_advice_data = {
        'week1': 'Focus on communication',
        'week2': 'Time for introspection',
        'week3': 'Action phase begins',
        'week4': 'Integration and rest'
    }

    with patch('services.lunar_interpretation_generator._generate_via_claude') as mock_claude:
        mock_claude.return_value = (
            'Full interpretation with weekly structure',
            weekly_advice_data,
            {'test': 'input'}
        )

        # Générer interprétation
        output, advice, source, model = await generate_or_get_interpretation(
            db=async_db_real,
            lunar_return_id=lunar_return.id,
            user_id=1,
            subject='full',
            version=2,
            lang='fr'
        )

        # Vérifier que weekly_advice est retourné
        assert advice == weekly_advice_data

    # Vérifier persistence en DB
    result = await async_db_real.execute(
        select(LunarInterpretation).filter_by(
            lunar_return_id=lunar_return.id,
            subject='full'
        )
    )
    interpretation = result.scalar_one_or_none()

    assert interpretation is not None
    assert interpretation.weekly_advice == weekly_advice_data
    assert 'week1' in interpretation.weekly_advice
    assert interpretation.weekly_advice['week1'] == 'Focus on communication'

    # Cleanup
    await async_db_real.delete(interpretation)
    await async_db_real.delete(lunar_return)
    await async_db_real.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_force_regenerate(async_db_real):
    """Test 8: Force Regenerate - Bypass cache

    Vérifie que force_regenerate=True bypass le cache DB temporelle
    et force une nouvelle génération même si une interprétation existe.
    """
    from models import LunarReturn, LunarInterpretation
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from datetime import datetime, timezone
    from sqlalchemy import select

    # Créer un LunarReturn
    lunar_return = LunarReturn(
        user_id=1,
        month="2025-08",
        return_date=datetime(2025, 8, 15, tzinfo=timezone.utc),
        moon_sign="Scorpio",
        moon_house=8,
        lunar_ascendant="Pisces",
        aspects=[],
        planets={},
        houses={}
    )
    async_db_real.add(lunar_return)
    await async_db_real.commit()
    await async_db_real.refresh(lunar_return)

    # Créer une interprétation existante en cache
    old_interpretation = LunarInterpretation(
        user_id=1,
        lunar_return_id=lunar_return.id,
        subject='full',
        version=2,
        lang='fr',
        input_json={'old': 'context'},
        output_text='Old cached interpretation',
        weekly_advice={'week1': 'Old advice'},
        model_used='claude-opus-old'
    )
    async_db_real.add(old_interpretation)
    await async_db_real.commit()

    # Mock Claude pour nouvelle génération
    with patch('services.lunar_interpretation_generator._generate_via_claude') as mock_claude:
        mock_claude.return_value = (
            'Newly generated interpretation',
            {'week1': 'New advice'},
            {'new': 'context'}
        )

        # Appeler avec force_regenerate=True
        output, advice, source, model = await generate_or_get_interpretation(
            db=async_db_real,
            lunar_return_id=lunar_return.id,
            user_id=1,
            subject='full',
            version=2,
            lang='fr',
            force_regenerate=True
        )

        # Assertions
        assert source == 'claude', "force_regenerate devrait bypasser cache et générer via Claude"
        assert output == 'Newly generated interpretation'
        assert advice == {'week1': 'New advice'}
        assert mock_claude.call_count == 1, "Claude devrait être appelé malgré cache existant"

    # Vérifier qu'une nouvelle interprétation a été créée (ou updated via UNIQUE constraint)
    result = await async_db_real.execute(
        select(LunarInterpretation).filter_by(
            lunar_return_id=lunar_return.id,
            subject='full',
            version=2
        )
    )
    interpretations = result.scalars().all()

    # Avec UNIQUE constraint, on devrait avoir soit 1 (upsert) soit 2 (nouvelle entrée)
    # Le comportement dépend de l'implémentation, mais le contenu devrait être nouveau
    assert len(interpretations) >= 1
    latest = interpretations[-1]  # Dernière version
    assert latest.output_text == 'Newly generated interpretation'

    # Cleanup
    for interp in interpretations:
        await async_db_real.delete(interp)
    await async_db_real.delete(lunar_return)
    await async_db_real.commit()
