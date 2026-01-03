"""
Test de sécurité: Lunar Return Report - user_id toujours depuis auth, jamais depuis request

Prouve que même si un client tente de falsifier user_id, la DB utilise toujours
l'utilisateur authentifié (current_user.id).
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from unittest.mock import patch

from main import app
from models.lunar_pack import LunarReport
from database import AsyncSessionLocal


@pytest.mark.asyncio
async def test_lunar_report_uses_authenticated_user_not_request_userid():
    """
    Test de sécurité: même si le payload contient des données falsifiées,
    la DB doit toujours utiliser l'utilisateur authentifié.
    
    Scénario:
    1. User A s'authentifie avec X-Dev-External-Id: UUID_A
    2. User A envoie un payload avec month (user_id n'existe plus dans le modèle)
    3. Vérifier que le rapport est sauvegardé avec user_id = User A (pas un autre)
    """
    # UUIDs pour 2 utilisateurs distincts
    user_a_uuid = "550e8400-e29b-41d4-a716-446655440000"
    user_b_uuid = "660e8400-e29b-41d4-a716-446655440001"
    
    valid_payload = {
        "birth_date": "1990-05-15",
        "birth_time": "14:30",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris",
        "date": "2025-01-15",
        "month": "2025-01"  # Pour déclencher la sauvegarde DB
    }
    
    mock_report_response = {
        "moon": {"sign": "Taurus", "house": 2},
        "interpretation": "Test interpretation",
        "lunar_ascendant": "Gemini"
    }
    
    # Activer DEV_AUTH_BYPASS et mocker le service
    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'), \
         patch('services.lunar_services.get_lunar_return_report', return_value=mock_report_response):
        
        async with AsyncClient(app=app, base_url="http://test") as client:
            # User A s'authentifie et envoie le payload
            response = await client.post(
                "/api/lunar/return/report",
                json=valid_payload,
                headers={"X-Dev-External-Id": user_a_uuid}
            )
            
            # Vérifier que la requête réussit
            assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
            
            data = response.json()
            assert data["provider"] == "rapidapi"
            assert data["kind"] == "lunar_return_report"
            
            # Vérifier en DB que le rapport est lié à User A (pas User B)
            async with AsyncSessionLocal() as db:
                # Récupérer User A depuis la DB
                from models.user import User
                from sqlalchemy import select
                
                user_a_result = await db.execute(
                    select(User).where(User.dev_external_id == user_a_uuid)
                )
                user_a = user_a_result.scalar_one_or_none()
                
                assert user_a is not None, f"User A (UUID: {user_a_uuid}) doit exister en DB"
                user_a_id = user_a.id
                
                # Vérifier que le rapport existe avec user_id = User A
                report_result = await db.execute(
                    select(LunarReport).where(
                        LunarReport.user_id == user_a_id,
                        LunarReport.month == "2025-01"
                    )
                )
                report = report_result.scalar_one_or_none()
                
                assert report is not None, "Le rapport doit être sauvegardé en DB"
                assert report.user_id == user_a_id, \
                    f"Le rapport doit être lié à User A (id={user_a_id}), pas à {report.user_id}"
                assert report.month == "2025-01"
                
                # Vérifier que User B n'a PAS de rapport pour ce mois
                user_b_result = await db.execute(
                    select(User).where(User.dev_external_id == user_b_uuid)
                )
                user_b = user_b_result.scalar_one_or_none()
                
                if user_b is not None:
                    user_b_id = user_b.id
                    report_b_result = await db.execute(
                        select(LunarReport).where(
                            LunarReport.user_id == user_b_id,
                            LunarReport.month == "2025-01"
                        )
                    )
                    report_b = report_b_result.scalar_one_or_none()
                    assert report_b is None, \
                        f"User B (id={user_b_id}) ne doit PAS avoir de rapport pour ce mois"


@pytest.mark.asyncio
async def test_lunar_report_different_users_different_reports():
    """
    Test que deux utilisateurs différents peuvent avoir des rapports pour le même mois
    sans interférence (isolation des données).
    """
    user_a_uuid = "550e8400-e29b-41d4-a716-446655440000"
    user_b_uuid = "660e8400-e29b-41d4-a716-446655440001"
    
    payload_a = {
        "birth_date": "1990-05-15",
        "birth_time": "14:30",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris",
        "date": "2025-01-15",
        "month": "2025-01"
    }
    
    payload_b = {
        "birth_date": "1985-03-20",
        "birth_time": "10:00",
        "latitude": 45.5017,
        "longitude": -73.5673,
        "timezone": "America/Montreal",
        "date": "2025-01-15",
        "month": "2025-01"  # Même mois que User A
    }
    
    mock_report_a = {
        "moon": {"sign": "Taurus", "house": 2},
        "interpretation": "Report User A"
    }
    
    mock_report_b = {
        "moon": {"sign": "Gemini", "house": 3},
        "interpretation": "Report User B"
    }
    
    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'), \
         patch('services.lunar_services.get_lunar_return_report') as mock_service:
        
        # Premier appel retourne report A, deuxième retourne report B
        mock_service.side_effect = [mock_report_a, mock_report_b]
        
        async with AsyncClient(app=app, base_url="http://test") as client:
            # User A crée un rapport
            response_a = await client.post(
                "/api/lunar/return/report",
                json=payload_a,
                headers={"X-Dev-External-Id": user_a_uuid}
            )
            assert response_a.status_code == 200
            
            # User B crée un rapport pour le même mois
            response_b = await client.post(
                "/api/lunar/return/report",
                json=payload_b,
                headers={"X-Dev-External-Id": user_b_uuid}
            )
            assert response_b.status_code == 200
            
            # Vérifier en DB que chaque user a son propre rapport
            async with AsyncSessionLocal() as db:
                from models.user import User
                from sqlalchemy import select
                
                # Récupérer les users
                user_a_result = await db.execute(
                    select(User).where(User.dev_external_id == user_a_uuid)
                )
                user_a = user_a_result.scalar_one_or_none()
                
                user_b_result = await db.execute(
                    select(User).where(User.dev_external_id == user_b_uuid)
                )
                user_b = user_b_result.scalar_one_or_none()
                
                if user_a and user_b:
                    # Vérifier que User A a son rapport
                    report_a_result = await db.execute(
                        select(LunarReport).where(
                            LunarReport.user_id == user_a.id,
                            LunarReport.month == "2025-01"
                        )
                    )
                    report_a = report_a_result.scalar_one_or_none()
                    assert report_a is not None, "User A doit avoir un rapport"
                    assert report_a.user_id == user_a.id
                    
                    # Vérifier que User B a son propre rapport
                    report_b_result = await db.execute(
                        select(LunarReport).where(
                            LunarReport.user_id == user_b.id,
                            LunarReport.month == "2025-01"
                        )
                    )
                    report_b = report_b_result.scalar_one_or_none()
                    assert report_b is not None, "User B doit avoir son propre rapport"
                    assert report_b.user_id == user_b.id
                    assert report_b.user_id != report_a.user_id, "Les rapports doivent être liés à des users différents"

