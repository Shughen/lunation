"""
Tests pour le service de cache des interprétations (lunar + natal)

Pattern de test:
1. Vérifier cache miss → fetch DB
2. Vérifier cache hit → pas de fetch DB
3. Vérifier invalidation cache
4. Vérifier stats du cache
"""

import pytest
import pytest_asyncio
import time
from unittest.mock import AsyncMock, MagicMock, patch
from sqlalchemy.ext.asyncio import AsyncSession
from services.interpretation_cache_service import (
    get_lunar_climate_cached,
    get_lunar_focus_cached,
    get_lunar_approach_cached,
    get_lunar_v2_full_cached,
    get_natal_pregenerated_cached,
    clear_cache,
    get_cache_stats,
    INTERPRETATION_CACHE_TTL
)


@pytest_asyncio.fixture
async def mock_db():
    """Fixture qui crée une session DB mockée"""
    session = AsyncMock(spec=AsyncSession)
    return session


@pytest.fixture(autouse=True)
def clear_cache_before_each_test():
    """Fixture autouse qui clear le cache avant chaque test pour garantir l'isolation"""
    clear_cache()
    yield
    clear_cache()  # Clean après également


@pytest.mark.asyncio
async def test_lunar_climate_cache_miss_then_hit(mock_db):
    """
    Test cache miss puis cache hit pour lunar_climate
    """
    # Clear cache au début
    clear_cache()

    # Mock du résultat DB pour climate
    with patch('services.interpretation_cache_service._fetch_lunar_climate_from_db') as mock_fetch:
        mock_fetch.return_value = "Mois dynamique et impulsif"

        # 1. Premier appel → cache miss
        climate1 = await get_lunar_climate_cached(mock_db, "Aries", version=1, lang='fr')

        # Vérifier que la DB a été appelée
        assert mock_fetch.call_count == 1

        # 2. Deuxième appel → cache hit (même clé)
        climate2 = await get_lunar_climate_cached(mock_db, "Aries", version=1, lang='fr')

        # La DB ne doit PAS être appelée à nouveau
        assert mock_fetch.call_count == 1  # Toujours 1

        # Les deux résultats doivent être identiques
        assert climate1 == climate2

        # Stats doivent montrer le cache populé
        stats = get_cache_stats()
        assert stats["lunar_climate"]["age_seconds"] is not None
        assert stats["lunar_climate"]["ttl"] == INTERPRETATION_CACHE_TTL


@pytest.mark.asyncio
async def test_lunar_focus_cache_miss_then_hit(mock_db):
    """
    Test cache miss puis cache hit pour lunar_focus
    """
    # Clear cache au début
    clear_cache()

    with patch('services.interpretation_cache_service._fetch_lunar_focus_from_db') as mock_fetch:
        mock_fetch.return_value = "Focus sur ton identité"

        # 1. Premier appel → cache miss
        focus1 = await get_lunar_focus_cached(mock_db, moon_house=1, version=1, lang='fr')

        # Vérifier que la DB a été appelée
        assert mock_fetch.call_count == 1

        # 2. Deuxième appel → cache hit
        focus2 = await get_lunar_focus_cached(mock_db, moon_house=1, version=1, lang='fr')

        # La DB ne doit PAS être appelée à nouveau
        assert mock_fetch.call_count == 1

        # Les deux résultats doivent être identiques
        assert focus1 == focus2

        # Stats doivent montrer le cache populé
        stats = get_cache_stats()
        assert stats["lunar_focus"]["age_seconds"] is not None


@pytest.mark.asyncio
async def test_lunar_approach_cache_miss_then_hit(mock_db):
    """
    Test cache miss puis cache hit pour lunar_approach
    """
    # Clear cache au début
    clear_cache()

    with patch('services.interpretation_cache_service._fetch_lunar_approach_from_db') as mock_fetch:
        mock_fetch.return_value = "Tu abordes en mode conquérant"

        # 1. Premier appel → cache miss
        approach1 = await get_lunar_approach_cached(mock_db, "Aries", version=1, lang='fr')

        # Vérifier que la DB a été appelée
        assert mock_fetch.call_count == 1

        # 2. Deuxième appel → cache hit
        approach2 = await get_lunar_approach_cached(mock_db, "Aries", version=1, lang='fr')

        # La DB ne doit PAS être appelée à nouveau
        assert mock_fetch.call_count == 1

        # Les deux résultats doivent être identiques
        assert approach1 == approach2

        # Stats doivent montrer le cache populé
        stats = get_cache_stats()
        assert stats["lunar_approach"]["age_seconds"] is not None


@pytest.mark.asyncio
async def test_lunar_v2_full_cache_miss_then_hit(mock_db):
    """
    Test cache miss puis cache hit pour lunar_v2_full
    """
    # Clear cache au début
    clear_cache()

    mock_interpretation = ("Interprétation complète v2", {"week_1": "Conseil semaine 1"})

    with patch('services.interpretation_cache_service._fetch_lunar_v2_full_from_db') as mock_fetch:
        mock_fetch.return_value = mock_interpretation

        # 1. Premier appel → cache miss
        result1 = await get_lunar_v2_full_cached(
            mock_db,
            moon_sign="Aries",
            moon_house=1,
            lunar_ascendant="Aries",
            version=2,
            lang='fr'
        )

        # Vérifier que la DB a été appelée
        assert mock_fetch.call_count == 1

        # 2. Deuxième appel → cache hit
        result2 = await get_lunar_v2_full_cached(
            mock_db,
            moon_sign="Aries",
            moon_house=1,
            lunar_ascendant="Aries",
            version=2,
            lang='fr'
        )

        # La DB ne doit PAS être appelée à nouveau
        assert mock_fetch.call_count == 1

        # Les deux résultats doivent être identiques
        assert result1 == result2

        # Stats doivent montrer le cache populé
        stats = get_cache_stats()
        assert stats["lunar_v2_full"]["age_seconds"] is not None


@pytest.mark.asyncio
async def test_natal_pregenerated_cache_miss_then_hit(mock_db):
    """
    Test cache miss puis cache hit pour natal_pregenerated
    """
    # Clear cache au début
    clear_cache()

    with patch('services.interpretation_cache_service._fetch_natal_pregenerated_from_db') as mock_fetch:
        mock_fetch.return_value = "# Soleil en Bélier\n\nInterprétation complète..."

        # 1. Premier appel → cache miss
        natal1 = await get_natal_pregenerated_cached(
            mock_db,
            subject="sun",
            sign="aries",
            house=1,
            version=2,
            lang='fr'
        )

        # Vérifier que la DB a été appelée
        assert mock_fetch.call_count == 1

        # 2. Deuxième appel → cache hit
        natal2 = await get_natal_pregenerated_cached(
            mock_db,
            subject="sun",
            sign="aries",
            house=1,
            version=2,
            lang='fr'
        )

        # La DB ne doit PAS être appelée à nouveau
        assert mock_fetch.call_count == 1

        # Les deux résultats doivent être identiques
        assert natal1 == natal2

        # Stats doivent montrer le cache populé
        stats = get_cache_stats()
        assert stats["natal_pregenerated"]["age_seconds"] is not None


def test_clear_cache():
    """
    Test invalidation complète du cache
    """
    # Populate cache d'abord (indirect via get_cache_stats)
    stats_before = get_cache_stats()

    # Clear
    clear_cache()

    # Vérifier que tous les caches sont vides
    stats_after = get_cache_stats()

    assert stats_after["lunar_climate"]["size"] == 0
    assert stats_after["lunar_focus"]["size"] == 0
    assert stats_after["lunar_approach"]["size"] == 0
    assert stats_after["lunar_v2_full"]["size"] == 0
    assert stats_after["natal_pregenerated"]["size"] == 0

    # Age doit être None après clear
    assert stats_after["lunar_climate"]["age_seconds"] is None
    assert stats_after["lunar_focus"]["age_seconds"] is None
    assert stats_after["lunar_approach"]["age_seconds"] is None
    assert stats_after["lunar_v2_full"]["age_seconds"] is None
    assert stats_after["natal_pregenerated"]["age_seconds"] is None


def test_cache_stats_structure():
    """
    Test structure des statistiques de cache
    """
    clear_cache()
    stats = get_cache_stats()

    # Vérifier structure
    assert "lunar_climate" in stats
    assert "lunar_focus" in stats
    assert "lunar_approach" in stats
    assert "lunar_v2_full" in stats
    assert "natal_pregenerated" in stats

    # Vérifier sous-structure
    for cache_name in stats:
        assert "size" in stats[cache_name]
        assert "age_seconds" in stats[cache_name]
        assert "ttl" in stats[cache_name]
        assert stats[cache_name]["ttl"] == INTERPRETATION_CACHE_TTL


@pytest.mark.asyncio
async def test_cache_different_keys_are_separate(mock_db):
    """
    Test que différentes clés de cache ne se mélangent pas
    """
    clear_cache()

    with patch('services.interpretation_cache_service._fetch_lunar_climate_from_db') as mock_fetch:
        # Configurer des retours différents selon l'appel
        mock_fetch.side_effect = [
            "Mois dynamique Bélier",
            "Mois stable Taureau"
        ]

        # Fetch 2 différents signes lunaires
        climate_aries = await get_lunar_climate_cached(mock_db, "Aries", version=1, lang='fr')
        climate_taurus = await get_lunar_climate_cached(mock_db, "Taurus", version=1, lang='fr')

        # Les deux doivent être différents
        assert climate_aries != climate_taurus

        # Stats doivent montrer au moins 2 entrées
        stats = get_cache_stats()
        assert stats["lunar_climate"]["size"] >= 2


@pytest.mark.asyncio
async def test_cache_survives_multiple_calls(mock_db):
    """
    Test que le cache survit à plusieurs appels consécutifs
    """
    clear_cache()

    with patch('services.interpretation_cache_service._fetch_lunar_climate_from_db') as mock_fetch:
        mock_fetch.return_value = "Mois dynamique"

        # Faire 5 appels avec la même clé
        results = []
        for _ in range(5):
            result = await get_lunar_climate_cached(mock_db, "Aries", version=1, lang='fr')
            results.append(result)

        # La DB ne doit être appelée qu'une seule fois
        assert mock_fetch.call_count == 1

        # Tous les résultats doivent être identiques
        assert all(r == results[0] for r in results)
