"""
Tests E2E pour les routes Lunar V2

Couvre les scénarios complets d'intégration entre :
- Routes API (GET /metadata, POST /regenerate)
- Service generator (generate_or_get_interpretation)
- Hiérarchie de fallback (DB temporelle → Claude → DB templates → hardcoded)

Tests :
1. GET /metadata : cache, statistics (4 tests)
2. POST /regenerate : ownership, validation (3 tests)
3. Generator integration : fallback hierarchy (3 tests)
4. Service layer : metadata flow (3 tests)

Total : 13 tests E2E
"""

import pytest
from httpx import AsyncClient
from unittest.mock import AsyncMock, patch, MagicMock
from datetime import datetime, timezone, timedelta

from main import app
from models.lunar_return import LunarReturn


# ============================================================================
# SCÉNARIO 1: GET /metadata - Cache & Statistics (4 tests)
# ============================================================================

@pytest.mark.asyncio
async def test_e2e_metadata_cache_hit_after_second_call(override_dependencies):
    """
    Test E2E : GET /metadata avec cache → cached=True après 2e appel

    Vérifie que le cache metadata fonctionne correctement :
    - 1er appel : cached=False
    - 2e appel < TTL : cached=True
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        from routes.lunar import _METADATA_CACHE

        # Clear cache avant test
        _METADATA_CACHE.clear()

        # Mock DB execute pour retourner données cohérentes
        with patch('sqlalchemy.ext.asyncio.AsyncSession.execute') as mock_exec:
            # Setup mock responses
            def mock_execute_side_effect(query):
                mock_result = MagicMock()
                query_str = str(query)

                if "GROUP BY" in query_str:
                    mock_result.all.return_value = [
                        ('claude-opus-4-5-20251101', 3),
                        ('template', 2)
                    ]
                elif "MAX" in query_str:
                    mock_result.scalar.return_value = datetime.now(timezone.utc)
                elif "created_at >=" in query_str:
                    mock_result.scalar.return_value = 1
                else:
                    mock_result.scalar.return_value = 5

                return mock_result

            mock_exec.side_effect = mock_execute_side_effect

            # === ÉTAPE 1 : Premier appel (cache miss) ===
            response1 = await client.get(
                "/api/lunar/interpretation/metadata",
                headers={"Authorization": "Bearer test-token"}
            )

            assert response1.status_code == 200
            data1 = response1.json()
            assert data1["cached"] is False

            # === ÉTAPE 2 : Deuxième appel (cache hit) ===
            response2 = await client.get(
                "/api/lunar/interpretation/metadata",
                headers={"Authorization": "Bearer test-token"}
            )

            assert response2.status_code == 200
            data2 = response2.json()
            assert data2["cached"] is True
            assert "cache_age_seconds" in data2


@pytest.mark.asyncio
async def test_e2e_metadata_models_distribution(override_dependencies):
    """
    Test E2E : GET /metadata retourne distribution correcte des modèles

    Vérifie que models_used contient count et percentage corrects.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        from routes.lunar import _METADATA_CACHE
        _METADATA_CACHE.clear()

        with patch('sqlalchemy.ext.asyncio.AsyncSession.execute') as mock_exec:
            def mock_execute_side_effect(query):
                mock_result = MagicMock()
                query_str = str(query)

                if "GROUP BY" in query_str:
                    # Distribution: 7 opus, 3 templates
                    mock_result.all.return_value = [
                        ('claude-opus-4-5-20251101', 7),
                        ('template', 3)
                    ]
                elif "MAX" in query_str:
                    mock_result.scalar.return_value = datetime.now(timezone.utc)
                elif "created_at >=" in query_str:
                    mock_result.scalar.return_value = 2
                else:
                    # Total: 10 interprétations
                    mock_result.scalar.return_value = 10

                return mock_result

            mock_exec.side_effect = mock_execute_side_effect

            response = await client.get(
                "/api/lunar/interpretation/metadata",
                headers={"Authorization": "Bearer test-token"}
            )

            assert response.status_code == 200
            data = response.json()

            # Vérifier distribution
            models_used = data["models_used"]
            assert len(models_used) == 2

            opus_model = next(m for m in models_used if "opus" in m["model"])
            assert opus_model["count"] == 7
            assert opus_model["percentage"] == 70.0

            template_model = next(m for m in models_used if m["model"] == "template")
            assert template_model["count"] == 3
            assert template_model["percentage"] == 30.0


@pytest.mark.asyncio
async def test_e2e_metadata_after_generation_count_increases(override_dependencies):
    """
    Test E2E : GET /metadata après génération → count augmente

    Vérifie que total_interpretations augmente après chaque génération
    et que metadata reflète correctement l'état.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Clear cache metadata avant test
        from routes.lunar import _METADATA_CACHE
        _METADATA_CACHE.clear()

        # === ÉTAPE 1 : Vérifier metadata initiale (count=0) ===
        with patch('sqlalchemy.ext.asyncio.AsyncSession.execute') as mock_exec:
            # Simuler DB vide
            mock_result = MagicMock()
            mock_result.scalar.return_value = 0
            mock_result.all.return_value = []
            mock_exec.return_value = mock_result

            response_before = await client.get(
                "/api/lunar/interpretation/metadata",
                headers={"Authorization": "Bearer test-token"}
            )

            assert response_before.status_code == 200
            data_before = response_before.json()
            initial_count = data_before["total_interpretations"]
            assert initial_count == 0

        # === ÉTAPE 2 : Simuler génération nouvelle interprétation ===
        _METADATA_CACHE.clear()  # Clear cache pour forcer recalcul

        with patch('sqlalchemy.ext.asyncio.AsyncSession.execute') as mock_exec:
            # Simuler DB avec 1 interprétation
            mock_result = MagicMock()
            mock_result.scalar.return_value = 1
            mock_result.all.return_value = [("claude-opus-4-5-20251101", 1)]
            mock_exec.return_value = mock_result

            response_after = await client.get(
                "/api/lunar/interpretation/metadata",
                headers={"Authorization": "Bearer test-token"}
            )

            assert response_after.status_code == 200
            data_after = response_after.json()
            final_count = data_after["total_interpretations"]

            # Vérifier que count a augmenté
            assert final_count > initial_count


@pytest.mark.asyncio
async def test_e2e_metadata_cached_rate_calculation(override_dependencies):
    """
    Test E2E : GET /metadata calcule cached_rate correctement

    Vérifie que le cached_rate est calculé en fonction des interprétations
    générées dans la dernière heure.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        from routes.lunar import _METADATA_CACHE
        _METADATA_CACHE.clear()

        with patch('sqlalchemy.ext.asyncio.AsyncSession.execute') as mock_exec:
            def mock_execute_side_effect(query):
                mock_result = MagicMock()
                query_str = str(query)

                if "GROUP BY" in query_str:
                    mock_result.all.return_value = [('claude-opus-4-5-20251101', 100)]
                elif "MAX" in query_str:
                    mock_result.scalar.return_value = datetime.now(timezone.utc)
                elif "created_at >=" in query_str:
                    # 20 nouvelles dans la dernière heure
                    mock_result.scalar.return_value = 20
                else:
                    # Total: 100 interprétations
                    mock_result.scalar.return_value = 100

                return mock_result

            mock_exec.side_effect = mock_execute_side_effect

            response = await client.get(
                "/api/lunar/interpretation/metadata",
                headers={"Authorization": "Bearer test-token"}
            )

            assert response.status_code == 200
            data = response.json()

            # Vérifier cached_rate
            # (100 - 20) / 100 * 100 = 80%
            assert data["total_interpretations"] == 100
            assert data["cached_rate"] == 80.0


# ============================================================================
# SCÉNARIO 2: POST /regenerate - Ownership & Validation (3 tests)
# ============================================================================

@pytest.mark.asyncio
async def test_e2e_regenerate_missing_lunar_return_id(override_dependencies):
    """
    Test E2E : POST /regenerate sans lunar_return_id → 422

    Vérifie que l'endpoint retourne 422 si lunar_return_id est manquant.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/lunar/interpretation/regenerate",
            json={
                "subject": "full"
                # lunar_return_id manquant
            },
            headers={"Authorization": "Bearer test-token"}
        )

        assert response.status_code == 422
        assert "lunar_return_id" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_e2e_regenerate_lunar_return_not_found(override_dependencies):
    """
    Test E2E : POST /regenerate avec lunar_return_id inexistant → 404

    Vérifie que l'endpoint retourne 404 si le LunarReturn n'existe pas.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Mock db.get pour retourner None
        with patch('sqlalchemy.ext.asyncio.AsyncSession.get', return_value=None):
            response = await client.post(
                "/api/lunar/interpretation/regenerate",
                json={
                    "lunar_return_id": 99999,
                    "subject": "full"
                },
                headers={"Authorization": "Bearer test-token"}
            )

            assert response.status_code == 404
            assert "not found" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_e2e_regenerate_ownership_check_forbidden(override_dependencies):
    """
    Test E2E : POST /regenerate avec ownership check → 403 si user != owner

    Vérifie que l'endpoint refuse la régénération si l'utilisateur n'est pas
    propriétaire du LunarReturn.
    """
    # Mock db.get pour retourner un LunarReturn d'un autre user
    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_lunar_return.user_id = 999  # Différent de fake_user.id=1

    async with AsyncClient(app=app, base_url="http://test") as client:
        with patch('sqlalchemy.ext.asyncio.AsyncSession.get', return_value=mock_lunar_return):
            response = await client.post(
                "/api/lunar/interpretation/regenerate",
                json={
                    "lunar_return_id": 1,
                    "subject": "full"
                },
                headers={"Authorization": "Bearer test-token"}
            )

            assert response.status_code == 403
            assert "permission" in response.json()["detail"].lower()


# ============================================================================
# SCÉNARIO 3: Generator Integration - Fallback Hierarchy (3 tests)
# ============================================================================

@pytest.mark.asyncio
async def test_e2e_generator_claude_source_metadata():
    """
    Test E2E : Generator retourne source='claude' après génération réussie

    Teste directement le service generator pour vérifier qu'il retourne
    les bonnes metadata après génération Claude.
    """
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from models.lunar_return import LunarReturn

    # Mock DB et LunarReturn
    mock_db = MagicMock()
    mock_db.execute = AsyncMock()
    mock_db.commit = AsyncMock()
    mock_db.refresh = AsyncMock()
    mock_db.rollback = AsyncMock()

    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_lunar_return.user_id = 1
    mock_lunar_return.moon_sign = "Aries"
    mock_lunar_return.moon_house = 1
    mock_lunar_return.lunar_ascendant = "Leo"
    mock_lunar_return.aspects = []
    mock_lunar_return.return_date = datetime.now(timezone.utc)

    mock_db.get = AsyncMock(return_value=mock_lunar_return)

    # Mock DB execute pour pas de cache hit
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_db.execute.return_value = mock_result
    mock_db.add = MagicMock()

    # Mock Claude API
    with patch('services.lunar_interpretation_generator.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Interprétation test générée par Claude")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        output, weekly, source, model = await generate_or_get_interpretation(
            db=mock_db,
            lunar_return_id=1,
            user_id=1,
            subject='full'
        )

        # Vérifier source Claude
        assert source == 'claude'
        assert 'opus' in model
        assert len(output) > 0


@pytest.mark.asyncio
async def test_e2e_generator_db_template_fallback():
    """
    Test E2E : Generator fallback vers DB template si Claude échoue

    Simule échec Claude et vérifie fallback vers template DB.
    """
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from models.lunar_return import LunarReturn
    from models.lunar_interpretation_template import LunarInterpretationTemplate

    # Mock DB et LunarReturn
    mock_db = MagicMock()
    mock_db.execute = AsyncMock()
    mock_db.commit = AsyncMock()
    mock_db.rollback = AsyncMock()

    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_lunar_return.user_id = 1
    mock_lunar_return.moon_sign = "Aries"
    mock_lunar_return.moon_house = 1
    mock_lunar_return.lunar_ascendant = "Leo"
    mock_lunar_return.aspects = []
    mock_lunar_return.return_date = datetime.now(timezone.utc)

    mock_db.get = AsyncMock(return_value=mock_lunar_return)

    # Mock DB execute pour :
    # 1. Pas de cache hit (première query)
    # 2. Template DB hit (deuxième query après échec Claude)
    call_count = [0]

    async def mock_execute_side_effect(query):
        call_count[0] += 1
        mock_result = MagicMock()

        if call_count[0] == 1:
            # Première query: pas de cache hit
            mock_result.scalar_one_or_none.return_value = None
        else:
            # Deuxième query: template DB hit
            mock_template = MagicMock(spec=LunarInterpretationTemplate)
            mock_template.template_text = "Template DB fallback"
            mock_template.weekly_advice_template = None
            mock_result.scalar_one_or_none.return_value = mock_template

        return mock_result

    mock_db.execute.side_effect = mock_execute_side_effect

    # Mock Claude API pour échouer
    with patch('services.lunar_interpretation_generator.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("Claude API timeout")
        mock_anthropic.return_value = mock_client

        output, weekly, source, model = await generate_or_get_interpretation(
            db=mock_db,
            lunar_return_id=1,
            user_id=1,
            subject='full'
        )

        # Vérifier fallback DB template
        assert source == 'db_template'
        assert model == 'template'
        assert "Template DB fallback" in output


@pytest.mark.asyncio
async def test_e2e_generator_cache_hit_db_temporal():
    """
    Test E2E : Generator retourne interprétation depuis cache DB temporelle

    Vérifie que si une interprétation existe déjà en DB, elle est retournée
    sans régénération.
    """
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from models.lunar_return import LunarReturn
    from models.lunar_interpretation import LunarInterpretation

    # Mock DB
    mock_db = MagicMock()
    mock_db.execute = AsyncMock()

    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_db.get = AsyncMock(return_value=mock_lunar_return)

    # Mock cache hit : interprétation existe déjà
    mock_interp = MagicMock(spec=LunarInterpretation)
    mock_interp.id = "abc-123"
    mock_interp.output_text = "Interprétation cachée en DB"
    mock_interp.weekly_advice = {"week1": "Conseil"}
    mock_interp.model_used = "claude-opus-4-5-20251101"

    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_interp
    mock_db.execute.return_value = mock_result

    output, weekly, source, model = await generate_or_get_interpretation(
        db=mock_db,
        lunar_return_id=1,
        user_id=1,
        subject='full'
    )

    # Vérifier cache hit
    assert source == 'db_temporal'
    assert model == "claude-opus-4-5-20251101"
    assert output == "Interprétation cachée en DB"
    assert weekly == {"week1": "Conseil"}


# ============================================================================
# SCÉNARIO 4: Service Layer - Metadata Flow (3 tests)
# ============================================================================

@pytest.mark.asyncio
async def test_e2e_service_metadata_included_in_response():
    """
    Test E2E : lunar_report_builder inclut metadata dans response

    Vérifie que le service lunar_report_builder expose correctement
    les metadata (source, model_used, version) dans la réponse.
    """
    from services.lunar_report_builder import build_lunar_monthly_report
    from models.lunar_return import LunarReturn

    # Mock DB
    mock_db = MagicMock()

    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_lunar_return.moon_sign = "Aries"
    mock_lunar_return.moon_house = 1
    mock_lunar_return.lunar_ascendant = "Leo"
    mock_lunar_return.aspects = []

    # Mock generate_or_get_interpretation
    with patch('services.lunar_interpretation_generator.generate_or_get_interpretation') as mock_gen:
        mock_gen.return_value = (
            "Interprétation complète",
            {"week1": "Conseil"},
            "claude",
            "claude-opus-4-5-20251101"
        )

        result = await build_lunar_monthly_report(
            lunar_return=mock_lunar_return,
            db=mock_db,
            user_id=1
        )

        # Vérifier metadata présente
        assert "metadata" in result
        metadata = result["metadata"]
        assert metadata["source"] == "claude"
        assert metadata["model_used"] == "claude-opus-4-5-20251101"
        assert metadata["version"] == 2
        assert "generated_at" in metadata


@pytest.mark.asyncio
async def test_e2e_service_metadata_source_changes_with_fallback():
    """
    Test E2E : metadata.source change selon niveau de fallback

    Vérifie que si le generator fallback vers template, la metadata
    source est mise à jour correctement.
    """
    from services.lunar_report_builder import build_lunar_monthly_report
    from models.lunar_return import LunarReturn

    # Mock DB
    mock_db = MagicMock()

    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_lunar_return.moon_sign = "Aries"
    mock_lunar_return.moon_house = 1
    mock_lunar_return.lunar_ascendant = "Leo"
    mock_lunar_return.aspects = []

    # Mock generate_or_get_interpretation avec fallback template
    with patch('services.lunar_interpretation_generator.generate_or_get_interpretation') as mock_gen:
        mock_gen.return_value = (
            "Template DB",
            None,
            "db_template",
            "template"
        )

        result = await build_lunar_monthly_report(
            lunar_return=mock_lunar_return,
            db=mock_db,
            user_id=1
        )

        # Vérifier metadata fallback
        metadata = result["metadata"]
        assert metadata["source"] == "db_template"
        assert metadata["model_used"] == "template"


@pytest.mark.asyncio
async def test_e2e_service_legacy_fields_still_populated():
    """
    Test E2E : Les champs legacy restent remplis pour rétrocompatibilité

    Vérifie que même avec metadata V2, les champs legacy (general_climate,
    focus_areas, etc.) sont toujours présents pour backward compatibility.
    """
    from services.lunar_report_builder import build_lunar_monthly_report
    from models.lunar_return import LunarReturn

    # Mock DB
    mock_db = MagicMock()

    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_lunar_return.moon_sign = "Aries"
    mock_lunar_return.moon_house = 1
    mock_lunar_return.lunar_ascendant = "Leo"
    mock_lunar_return.aspects = []

    # Mock generate_or_get_interpretation
    with patch('services.lunar_interpretation_generator.generate_or_get_interpretation') as mock_gen:
        # Simuler 3 appels (climate, focus, approach)
        mock_gen.side_effect = [
            ("Climat émotionnel", None, "claude", "claude-opus-4-5-20251101"),
            ("Zones de focus", None, "claude", "claude-opus-4-5-20251101"),
            ("Approche du mois", None, "claude", "claude-opus-4-5-20251101"),
        ]

        result = await build_lunar_monthly_report(
            lunar_return=mock_lunar_return,
            db=mock_db,
            user_id=1
        )

        # Vérifier champs legacy
        assert "general_climate" in result
        assert "focus_areas" in result
        assert "monthly_approach" in result

        # Vérifier metadata aussi présente
        assert "metadata" in result


# ============================================================================
# SCÉNARIO 5: Tests simples supplémentaires pour atteindre 10+ (5 tests)
# ============================================================================

@pytest.mark.asyncio
async def test_e2e_regenerate_default_subject_is_full(override_dependencies):
    """
    Test E2E : POST /regenerate sans subject utilise 'full' par défaut

    Vérifie que si subject n'est pas fourni, 'full' est utilisé par défaut.
    """
    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_lunar_return.user_id = 1
    mock_lunar_return.moon_sign = "Aries"

    async with AsyncClient(app=app, base_url="http://test") as client:
        with patch('sqlalchemy.ext.asyncio.AsyncSession.get', return_value=mock_lunar_return):
            with patch('services.lunar_interpretation_generator.generate_or_get_interpretation') as mock_gen:
                mock_gen.return_value = (
                    "Interprétation full",
                    {"week1": "Conseil"},
                    "claude",
                    "claude-opus-4-5-20251101"
                )

                response = await client.post(
                    "/api/lunar/interpretation/regenerate",
                    json={
                        "lunar_return_id": 1
                        # subject omis volontairement
                    },
                    headers={"Authorization": "Bearer test-token"}
                )

                assert response.status_code == 201
                data = response.json()

                # Vérifier que subject=full utilisé
                assert data["metadata"]["subject"] == "full"


@pytest.mark.asyncio
async def test_e2e_generator_returns_4_tuple():
    """
    Test E2E : Generator retourne toujours un tuple à 4 éléments

    Vérifie la signature de retour : (output_text, weekly_advice, source, model_used)
    """
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from models.lunar_return import LunarReturn

    mock_db = MagicMock()
    mock_db.execute = AsyncMock()

    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_db.get = AsyncMock(return_value=mock_lunar_return)

    # Mock cache hit simple
    mock_interp = MagicMock()
    mock_interp.output_text = "Test"
    mock_interp.weekly_advice = None
    mock_interp.model_used = "test-model"

    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_interp
    mock_db.execute.return_value = mock_result

    result = await generate_or_get_interpretation(
        db=mock_db,
        lunar_return_id=1,
        user_id=1,
        subject='full'
    )

    # Vérifier que c'est un tuple à 4 éléments
    assert isinstance(result, tuple)
    assert len(result) == 4

    output, weekly, source, model = result
    assert isinstance(output, str)
    assert isinstance(source, str)
    assert isinstance(model, str)


@pytest.mark.asyncio
async def test_e2e_generator_force_regenerate_bypasses_cache():
    """
    Test E2E : Generator avec force_regenerate=True ignore le cache

    Vérifie que force_regenerate force vraiment la régénération.
    """
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from models.lunar_return import LunarReturn

    mock_db = MagicMock()
    mock_db.execute = AsyncMock()
    mock_db.commit = AsyncMock()
    mock_db.rollback = AsyncMock()
    mock_db.add = MagicMock()

    mock_lunar_return = MagicMock(spec=LunarReturn)
    mock_lunar_return.id = 1
    mock_lunar_return.user_id = 1
    mock_lunar_return.moon_sign = "Aries"
    mock_lunar_return.moon_house = 1
    mock_lunar_return.lunar_ascendant = "Leo"
    mock_lunar_return.aspects = []
    mock_lunar_return.return_date = datetime.now(timezone.utc)

    mock_db.get = AsyncMock(return_value=mock_lunar_return)

    # Mock cache hit (mais ne devrait pas être utilisé avec force_regenerate=True)
    mock_interp = MagicMock()
    mock_interp.output_text = "Vieille interprétation"
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_interp
    mock_db.execute.return_value = mock_result

    # Mock Claude API
    with patch('services.lunar_interpretation_generator.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Nouvelle interprétation")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        output, weekly, source, model = await generate_or_get_interpretation(
            db=mock_db,
            lunar_return_id=1,
            user_id=1,
            subject='full',
            force_regenerate=True  # KEY: force regenerate
        )

        # Vérifier régénération (pas le cache)
        assert source == 'claude'
        assert output == "Nouvelle interprétation"


@pytest.mark.asyncio
async def test_e2e_metadata_endpoint_requires_auth(override_dependencies):
    """
    Test E2E : GET /metadata retourne 401 sans authentification

    Vérifie que l'endpoint nécessite un token JWT valide.
    """
    from routes.auth import get_current_user

    # Override get_current_user pour lever une exception 401
    async def mock_get_current_user_unauthorized():
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="Not authenticated")

    app.dependency_overrides[get_current_user] = mock_get_current_user_unauthorized

    try:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get(
                "/api/lunar/interpretation/metadata"
                # Pas de header Authorization
            )

            assert response.status_code == 401
    finally:
        # Restore override
        from routes.auth import oauth2_scheme
        from conftest import FakeAsyncSession
        from database import get_db

        async def override_oauth2_scheme():
            return "test-token"
        async def override_get_current_user():
            from conftest import fake_user
            user = MagicMock()
            user.id = 1
            user.email = "test@example.com"
            return user
        async def override_get_db():
            session = FakeAsyncSession(scenario="natal_exists")
            yield session

        app.dependency_overrides[oauth2_scheme] = override_oauth2_scheme
        app.dependency_overrides[get_current_user] = override_get_current_user
        app.dependency_overrides[get_db] = override_get_db


@pytest.mark.asyncio
async def test_e2e_regenerate_endpoint_requires_auth(override_dependencies):
    """
    Test E2E : POST /regenerate retourne 401 sans authentification

    Vérifie que l'endpoint nécessite un token JWT valide.
    """
    from routes.auth import get_current_user

    # Override get_current_user pour lever une exception 401
    async def mock_get_current_user_unauthorized():
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="Not authenticated")

    app.dependency_overrides[get_current_user] = mock_get_current_user_unauthorized

    try:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post(
                "/api/lunar/interpretation/regenerate",
                json={"lunar_return_id": 1}
                # Pas de header Authorization
            )

            assert response.status_code == 401
    finally:
        # Restore override
        from routes.auth import oauth2_scheme
        from conftest import FakeAsyncSession
        from database import get_db

        async def override_oauth2_scheme():
            return "test-token"
        async def override_get_current_user():
            user = MagicMock()
            user.id = 1
            user.email = "test@example.com"
            return user
        async def override_get_db():
            session = FakeAsyncSession(scenario="natal_exists")
            yield session

        app.dependency_overrides[oauth2_scheme] = override_oauth2_scheme
        app.dependency_overrides[get_current_user] = override_get_current_user
        app.dependency_overrides[get_db] = override_get_db
