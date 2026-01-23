"""
Tests pour le service de cache VoC (voc_cache_service.py)
- Tests de cache avec TTL
- Tests de retry logic DB
- Tests anti-doublons
- Tests de performance
"""

import pytest
import pytest_asyncio
from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, patch, MagicMock
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from services import voc_cache_service
from models.lunar_pack import LunarVocWindow
from config import settings


@pytest.fixture(autouse=True)
def clear_voc_cache():
    """Clear cache avant et après chaque test"""
    voc_cache_service.clear_cache()
    yield
    voc_cache_service.clear_cache()


@pytest_asyncio.fixture
async def db_session():
    """
    Fixture pour créer une session DB async réelle pour les tests.
    Utilise NullPool pour éviter les conflits de connexion.
    Skip si la DB n'est pas accessible.
    """
    # Convertir postgresql:// en postgresql+asyncpg://
    database_url = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
    engine = create_async_engine(database_url, poolclass=NullPool)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    try:
        # Tester la connexion
        async with async_session() as test_session:
            from sqlalchemy import text
            await test_session.execute(text("SELECT 1"))
    except Exception as e:
        await engine.dispose()
        pytest.skip(f"DB not accessible: {str(e)[:100]}")

    async with async_session() as session:
        yield session

    await engine.dispose()


class TestVoCCacheService:
    """Tests pour le service de cache VoC"""

    @pytest.mark.asyncio
    @pytest.mark.real_db
    async def test_get_voc_status_cached_cache_miss(self, db_session):
        """Test: premier appel = cache miss, fetch DB"""
        # Setup: créer des fenêtres VoC de test
        now = datetime.now(timezone.utc)
        current_voc = LunarVocWindow(
            start_at=now - timedelta(hours=1),
            end_at=now + timedelta(hours=1),
            source={"test": "current"}
        )
        next_voc = LunarVocWindow(
            start_at=now + timedelta(hours=2),
            end_at=now + timedelta(hours=3),
            source={"test": "next"}
        )
        db_session.add(current_voc)
        db_session.add(next_voc)
        await db_session.commit()

        # Act: premier appel
        result = await voc_cache_service.get_voc_status_cached(db_session)

        # Assert
        assert result is not None
        assert result["now"] is not None
        assert result["now"]["is_active"] is True
        assert result["next"] is not None

    @pytest.mark.asyncio
    async def test_get_voc_status_cached_cache_hit(self, db_session):
        """Test: deuxième appel = cache hit, pas de requête DB"""
        # Setup: créer une fenêtre VoC
        now = datetime.now(timezone.utc)
        current_voc = LunarVocWindow(
            start_at=now - timedelta(hours=1),
            end_at=now + timedelta(hours=1),
            source={"test": "current"}
        )
        db_session.add(current_voc)
        await db_session.commit()

        # Act: premier appel (cache miss)
        result1 = await voc_cache_service.get_voc_status_cached(db_session)

        # Mock DB pour vérifier qu'il n'est pas appelé
        with patch.object(db_session, 'execute', new_callable=AsyncMock) as mock_execute:
            # Deuxième appel (cache hit)
            result2 = await voc_cache_service.get_voc_status_cached(db_session)

            # Assert: DB pas appelé
            mock_execute.assert_not_called()
            assert result2 == result1

    @pytest.mark.asyncio
    async def test_get_current_voc_cached_no_active_voc(self, db_session):
        """Test: aucun VoC actif"""
        # Act
        result = await voc_cache_service.get_current_voc_cached(db_session)

        # Assert
        assert result["is_active"] is False
        assert result["start_at"] is None
        assert result["end_at"] is None

    @pytest.mark.asyncio
    async def test_get_current_voc_cached_active_voc(self, db_session):
        """Test: VoC actif présent"""
        # Setup
        now = datetime.now(timezone.utc)
        current_voc = LunarVocWindow(
            start_at=now - timedelta(hours=1),
            end_at=now + timedelta(hours=1),
            source={"test": "active"}
        )
        db_session.add(current_voc)
        await db_session.commit()

        # Act
        result = await voc_cache_service.get_current_voc_cached(db_session)

        # Assert
        assert result["is_active"] is True
        assert result["start_at"] is not None
        assert result["end_at"] is not None
        assert result["source"] == {"test": "active"}

    @pytest.mark.asyncio
    async def test_save_voc_window_safe_new_window(self, db_session):
        """Test: sauvegarder une nouvelle fenêtre VoC"""
        # Setup
        start_at = datetime.now(timezone.utc) + timedelta(hours=1)
        end_at = datetime.now(timezone.utc) + timedelta(hours=2)
        source = {"test": "new_window"}

        # Act
        result = await voc_cache_service.save_voc_window_safe(
            db_session, start_at, end_at, source
        )

        # Assert
        assert result is not None
        assert result.start_at == start_at
        assert result.end_at == end_at
        assert result.source == source

        # Vérifier que c'est bien en DB
        await db_session.refresh(result)
        assert result.id is not None

    @pytest.mark.asyncio
    async def test_save_voc_window_safe_duplicate_prevention(self, db_session):
        """Test: éviter les doublons lors de la sauvegarde"""
        # Setup: créer une fenêtre existante
        start_at = datetime.now(timezone.utc) + timedelta(hours=1)
        end_at = datetime.now(timezone.utc) + timedelta(hours=2)
        source_v1 = {"test": "version1"}

        existing_voc = LunarVocWindow(
            start_at=start_at,
            end_at=end_at,
            source=source_v1
        )
        db_session.add(existing_voc)
        await db_session.commit()

        existing_id = existing_voc.id

        # Act: tenter de sauvegarder la même fenêtre avec source différent
        source_v2 = {"test": "version2"}
        result = await voc_cache_service.save_voc_window_safe(
            db_session, start_at, end_at, source_v2
        )

        # Assert: même ID, source mis à jour
        assert result.id == existing_id
        assert result.source == source_v2

        # Vérifier qu'il n'y a qu'une seule entrée en DB
        from sqlalchemy import select, func
        stmt = select(func.count(LunarVocWindow.id)).where(
            LunarVocWindow.start_at == start_at
        )
        count_result = await db_session.execute(stmt)
        count = count_result.scalar()
        assert count == 1

    @pytest.mark.asyncio
    async def test_cache_invalidation_after_save(self, db_session):
        """Test: le cache est invalidé après sauvegarde"""
        # Setup: remplir le cache
        now = datetime.now(timezone.utc)
        initial_voc = LunarVocWindow(
            start_at=now - timedelta(hours=1),
            end_at=now + timedelta(hours=1),
            source={"test": "initial"}
        )
        db_session.add(initial_voc)
        await db_session.commit()

        # Premier appel pour remplir le cache
        await voc_cache_service.get_voc_status_cached(db_session)

        # Vérifier que le cache a des données
        stats = voc_cache_service.get_cache_stats()
        assert stats["voc_status"]["has_data"] is True

        # Act: sauvegarder une nouvelle fenêtre
        new_start = now + timedelta(hours=2)
        new_end = now + timedelta(hours=3)
        await voc_cache_service.save_voc_window_safe(
            db_session, new_start, new_end, {"test": "new"}
        )

        # Assert: cache invalidé
        stats_after = voc_cache_service.get_cache_stats()
        assert stats_after["voc_status"]["has_data"] is False

    def test_get_cache_stats(self):
        """Test: récupérer les stats de cache"""
        # Act
        stats = voc_cache_service.get_cache_stats()

        # Assert
        assert "voc_status" in stats
        assert "voc_current" in stats
        assert "has_data" in stats["voc_status"]
        assert "age_seconds" in stats["voc_status"]
        assert "ttl" in stats["voc_status"]

    @pytest.mark.asyncio
    async def test_retry_logic_on_db_error(self, db_session):
        """Test: retry logic en cas d'erreur DB"""
        # Setup: mock pour simuler erreur DB puis succès
        from sqlalchemy.exc import OperationalError

        call_count = 0
        original_execute = db_session.execute

        async def mock_execute_with_retry(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                # Première tentative: erreur
                raise OperationalError("DB connection failed", None, None)
            else:
                # Deuxième tentative: succès
                return await original_execute(*args, **kwargs)

        # Act: patcher execute pour simuler erreur puis succès
        with patch.object(db_session, 'execute', side_effect=mock_execute_with_retry):
            # Devrait réussir après retry
            result = await voc_cache_service.get_voc_status_cached(db_session)

            # Assert: retry a fonctionné
            assert call_count >= 2
            assert result is not None

    def test_clear_cache(self):
        """Test: clear_cache invalide tous les caches"""
        # Setup: simuler cache rempli
        voc_cache_service._VOC_STATUS_CACHE["data"] = {"test": "data"}
        voc_cache_service._VOC_STATUS_CACHE["timestamp"] = 12345
        voc_cache_service._VOC_CURRENT_CACHE["data"] = {"test": "data"}
        voc_cache_service._VOC_CURRENT_CACHE["timestamp"] = 12345

        # Act
        voc_cache_service.clear_cache()

        # Assert
        assert voc_cache_service._VOC_STATUS_CACHE["data"] is None
        assert voc_cache_service._VOC_STATUS_CACHE["timestamp"] == 0
        assert voc_cache_service._VOC_CURRENT_CACHE["data"] is None
        assert voc_cache_service._VOC_CURRENT_CACHE["timestamp"] == 0


class TestVoCCacheTTL:
    """Tests de TTL et expiration cache"""

    @pytest.mark.asyncio
    async def test_cache_expires_after_ttl(self, db_session):
        """Test: cache expire après TTL"""
        # Setup: créer VoC et remplir cache
        now = datetime.now(timezone.utc)
        voc = LunarVocWindow(
            start_at=now,
            end_at=now + timedelta(hours=1),
            source={"test": "ttl"}
        )
        db_session.add(voc)
        await db_session.commit()

        # Premier appel: cache miss
        await voc_cache_service.get_current_voc_cached(db_session)

        # Simuler expiration cache en modifiant TTL à 0
        original_ttl = voc_cache_service._VOC_CURRENT_CACHE["ttl"]
        voc_cache_service._VOC_CURRENT_CACHE["ttl"] = 0

        # Deuxième appel: devrait être cache miss car TTL=0
        with patch.object(db_session, 'execute', wraps=db_session.execute) as mock_execute:
            await voc_cache_service.get_current_voc_cached(db_session)

            # Assert: DB appelé (cache expiré)
            assert mock_execute.called

        # Restore TTL
        voc_cache_service._VOC_CURRENT_CACHE["ttl"] = original_ttl


class TestVoCCachePerformance:
    """Tests de performance et optimisation"""

    @pytest.mark.asyncio
    async def test_parallel_db_queries_in_get_voc_status(self, db_session):
        """Test: les requêtes DB sont bien parallélisées"""
        # Setup
        now = datetime.now(timezone.utc)
        for i in range(5):
            voc = LunarVocWindow(
                start_at=now + timedelta(hours=i),
                end_at=now + timedelta(hours=i + 1),
                source={"test": f"voc_{i}"}
            )
            db_session.add(voc)
        await db_session.commit()

        # Act: mesurer le temps d'exécution
        import time
        start_time = time.time()
        result = await voc_cache_service.get_voc_status_cached(db_session)
        elapsed = time.time() - start_time

        # Assert: devrait être rapide grâce à la parallélisation
        assert elapsed < 1.0  # Moins de 1 seconde
        assert result is not None
