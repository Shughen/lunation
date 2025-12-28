"""
Fixtures et helpers pour les tests FastAPI

Fournit:
- FakeAsyncSession: stub DB sans vraie connection
- Fixtures pour override oauth2_scheme, get_current_user, get_db
"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from typing import AsyncGenerator, Optional, Dict, Any
from sqlalchemy.engine.result import Result
from sqlalchemy.ext.asyncio import AsyncSession

from main import app
from models.user import User
from models.natal_chart import NatalChart


class FakeAsyncSession:
    """
    Stub AsyncSession minimal pour les tests.
    Ne crée pas de vraie connection DB (évite greenlet).
    
    Supporte:
    - execute(query) -> FakeResult
    - scalar_one_or_none() -> objet mocké ou None
    - commit(), rollback(), close()
    - add(), refresh()
    """
    
    def __init__(self, scenario: Optional[str] = None):
        """
        Args:
            scenario: "natal_exists" | "natal_missing" | None (default: natal_exists)
        """
        self.scenario = scenario or "natal_exists"
        self._added_objects = []
        self._committed = False
        
    async def execute(self, query):
        """Retourne un FakeResult selon le scenario"""
        query_str = str(query)
        
        # Créer un FakeResult
        fake_result = FakeResult()
        
        # Si query pour NatalChart
        if "NatalChart" in query_str or "natal_charts" in query_str:
            if self.scenario == "natal_exists":
                # Créer un mock natal_chart avec tous les attributs nécessaires
                mock_natal = MagicMock(spec=NatalChart)
                mock_natal.id = "123e4567-e89b-12d3-a456-426614174000"
                mock_natal.user_id = 1
                mock_natal.latitude = 48.8566
                mock_natal.longitude = 2.3522
                mock_natal.timezone = "Europe/Paris"
                mock_natal.positions = {
                    "moon": {
                        "sign": "Aries",
                        "degree": 15.5,
                        "house": 1
                    },
                    "sun": {
                        "sign": "Taurus",
                        "degree": 10.0
                    },
                    "angles": {
                        "ascendant": {
                            "sign": "Leo",
                            "degree": 5.0
                        }
                    }
                }
                fake_result._scalar = mock_natal
            else:  # natal_missing
                fake_result._scalar = None
        elif "LunarReturn" in query_str or "lunar_returns" in query_str:
            # Query pour vérifier si un lunar return existe déjà
            # Par défaut, on retourne None (pas d'existant) pour permettre la génération
            fake_result._scalar = None
        else:
            # Autres queries (par défaut None)
            fake_result._scalar = None
            
        return fake_result
    
    async def commit(self):
        self._committed = True
    
    async def rollback(self):
        self._committed = False
    
    def add(self, obj):
        self._added_objects.append(obj)
    
    def refresh(self, obj):
        pass  # No-op pour les tests
    
    def close(self):
        pass  # No-op pour les tests
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()


class FakeResult:
    """Stub pour sqlalchemy.engine.result.Result"""
    
    def __init__(self):
        self._scalar = None
    
    def scalar_one_or_none(self):
        return self._scalar
    
    def scalar(self):
        return self._scalar
    
    def scalars(self):
        # Retourner un itérable vide pour les tests simples
        return iter([])


@pytest.fixture
def fake_user():
    """Mock User pour les tests"""
    user = MagicMock(spec=User)
    user.id = 1
    user.email = "test@example.com"
    user.birth_latitude = "48.8566"
    user.birth_longitude = "2.3522"
    user.birth_timezone = "Europe/Paris"
    return user


@pytest.fixture
def override_dependencies(fake_user):
    """
    Fixture qui override oauth2_scheme, get_current_user, et get_db.
    Scenario par défaut: "natal_exists"
    
    Usage:
        @pytest.mark.asyncio
        async def test_something(override_dependencies):
            # Les overrides sont déjà appliqués
            async with AsyncClient(app=app, base_url="http://test") as client:
                ...
            # Nettoyage automatique après le test
    """
    from routes.auth import oauth2_scheme, get_current_user
    from database import get_db
    
    # Override oauth2_scheme pour retourner un token factice
    async def override_oauth2_scheme():
        return "test-token"
    
    # Override get_current_user pour retourner fake_user
    async def override_get_current_user():
        return fake_user
    
    # Override get_db pour retourner FakeAsyncSession (scenario natal_exists)
    async def override_get_db():
        async_session = FakeAsyncSession(scenario="natal_exists")
        yield async_session
    
    # Appliquer les overrides
    app.dependency_overrides[oauth2_scheme] = override_oauth2_scheme
    app.dependency_overrides[get_current_user] = override_get_current_user
    app.dependency_overrides[get_db] = override_get_db
    
    yield
    
    # Nettoyage
    app.dependency_overrides.clear()


@pytest.fixture
def override_dependencies_no_natal(fake_user):
    """
    Fixture similaire mais avec scenario "natal_missing"
    
    Usage:
        @pytest.mark.asyncio
        async def test_error(override_dependencies_no_natal):
            # Les overrides sont déjà appliqués (natal_chart absent)
            async with AsyncClient(app=app, base_url="http://test") as client:
                ...
    """
    from routes.auth import oauth2_scheme, get_current_user
    from database import get_db
    
    async def override_oauth2_scheme():
        return "test-token"
    
    async def override_get_current_user():
        return fake_user
    
    async def override_get_db():
        async_session = FakeAsyncSession(scenario="natal_missing")
        yield async_session
    
    app.dependency_overrides[oauth2_scheme] = override_oauth2_scheme
    app.dependency_overrides[get_current_user] = override_get_current_user
    app.dependency_overrides[get_db] = override_get_db
    
    yield
    
    app.dependency_overrides.clear()

