"""
Tests pour le système d'alerte du scheduler lunar returns

Tests:
1. test_batch_identifies_users_in_window: Requête SQL identifie les bons users
2. test_alert_triggered_when_failure_rate_above_threshold: 25% échecs → alerte
3. test_no_alert_when_failure_rate_below_threshold: 10% échecs → pas d'alerte
4. test_metrics_recorded_correctly: Métriques Prometheus enregistrées
5. test_alert_handles_zero_users_gracefully: Gestion cas limite total_users=0
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import logging
from datetime import datetime, timedelta, timezone

from services.scheduler_services import refresh_lunar_returns_cron
from services.lunar_returns_service import refresh_lunar_returns_batch


# === TEST 1 : Requête SQL identifie les bons users ===

@pytest.mark.asyncio
async def test_batch_identifies_users_in_window(test_db):
    """
    Test : La requête SQL identifie correctement les users dans la fenêtre.

    Scénario :
    - Dans un cas normal, la fonction batch identifie les users dont la prochaine
      révolution lunaire tombe dans la fenêtre configurée

    Expected : La fonction retourne un dict avec les bons champs
    """
    # Mock de la fonction generate_lunar_returns_for_user
    with patch('services.lunar_returns_service.generate_lunar_returns_for_user') as mock_gen:
        mock_gen.return_value = {"success": True}

        result = await refresh_lunar_returns_batch(
            db=test_db,
            window_start_days=7,
            window_end_days=14
        )

        # Vérifier structure du résultat
        assert 'total_users' in result
        assert 'successful' in result
        assert 'failed' in result
        assert 'duration_seconds' in result
        assert 'errors' in result
        assert 'window' in result
        assert isinstance(result['errors'], list)


# === TEST 2 : Alerte déclenchée si taux d'échec > 20% ===

@pytest.mark.asyncio
async def test_alert_triggered_when_failure_rate_above_threshold(caplog):
    """
    Test: Alerte déclenchée si taux d'échec > 20%

    Scénario: 25% d'échecs (5 failed / 20 users)
    Expected: Log ERROR avec prefix 🚨 [ALERT]
    """
    mock_db = AsyncMock()

    # Mock 25% d'échecs
    mock_result = {
        "total_users": 20,
        "successful": 15,
        "failed": 5,
        "duration_seconds": 45.5,
        "errors": [
            {"user_id": 5, "error": "Signe lunaire invalide"},
            {"user_id": 12, "error": "Coordonnées manquantes"},
            {"user_id": 18, "error": "API timeout"},
            {"user_id": 22, "error": "DB connection failed"},
            {"user_id": 29, "error": "Unknown error"},
        ],
        "window": {"start": "2026-02-01", "end": "2026-02-08"}
    }

    with patch('services.scheduler_services.get_db') as mock_get_db_func:
        async def mock_generator():
            yield mock_db

        mock_get_db_func.return_value = mock_generator()

        with patch('services.lunar_returns_service.refresh_lunar_returns_batch') as mock_refresh:
            mock_refresh.return_value = mock_result

            with caplog.at_level(logging.ERROR):
                await refresh_lunar_returns_cron()

    # Vérifier log ERROR émis
    error_logs = [r for r in caplog.records if r.levelname == 'ERROR']
    assert len(error_logs) > 0, "Expected at least one ERROR log"

    # Vérifier contenu
    alert_log = None
    for record in error_logs:
        if "🚨 [ALERT]" in record.message and "Taux d'échec élevé" in record.message:
            alert_log = record
            break

    assert alert_log is not None, "Expected alert log with 🚨 [ALERT]"

    # Vérifier contexte extra
    assert hasattr(alert_log, 'alert_type')
    assert alert_log.alert_type == "lunar_refresh_high_failure_rate"
    assert alert_log.failure_rate == 0.25
    assert alert_log.total_users == 20
    assert alert_log.successful == 15
    assert alert_log.failed == 5
    assert len(alert_log.errors_sample) == 5


# === TEST 3 : Pas d'alerte si taux d'échec <= 20% ===

@pytest.mark.asyncio
async def test_no_alert_when_failure_rate_below_threshold(caplog):
    """
    Test: Pas d'alerte si taux d'échec <= 20%

    Scénario: 10% d'échecs (2 failed / 20 users)
    Expected: Pas de log ERROR avec 🚨 [ALERT]
    """
    mock_db = AsyncMock()

    # Mock 10% d'échecs
    mock_result = {
        "total_users": 20,
        "successful": 18,
        "failed": 2,
        "duration_seconds": 30.2,
        "errors": [
            {"user_id": 5, "error": "Signe lunaire invalide"},
            {"user_id": 12, "error": "Coordonnées manquantes"},
        ],
        "window": {"start": "2026-02-01", "end": "2026-02-08"}
    }

    with patch('services.scheduler_services.get_db') as mock_get_db_func:
        async def mock_generator():
            yield mock_db

        mock_get_db_func.return_value = mock_generator()

        with patch('services.lunar_returns_service.refresh_lunar_returns_batch') as mock_refresh:
            mock_refresh.return_value = mock_result

            with caplog.at_level(logging.INFO):
                await refresh_lunar_returns_cron()

    # Vérifier AUCUN log ERROR avec 🚨
    error_logs = [r for r in caplog.records if r.levelname == 'ERROR']
    alert_logs = [r for r in error_logs if "🚨 [ALERT]" in r.message]

    assert len(alert_logs) == 0, "No alert expected when failure rate <= threshold"

    # Vérifier log INFO standard existe
    info_logs = [r for r in caplog.records if r.levelname == 'INFO']
    success_logs = [r for r in info_logs if "✅ [CRON] Rafraîchissement terminé" in r.message]

    assert len(success_logs) > 0, "Expected success log"


# === TEST 4 : Métriques Prometheus enregistrées ===

@pytest.mark.asyncio
async def test_metrics_recorded_correctly():
    """
    Test: Métriques Prometheus enregistrées correctement
    """
    mock_db = AsyncMock()

    mock_result = {
        "total_users": 100,
        "successful": 92,
        "failed": 8,
        "duration_seconds": 150.3,
        "errors": [],
        "window": {"start": "2026-02-01", "end": "2026-02-08"}
    }

    with patch('services.scheduler_services.get_db') as mock_get_db_func:
        async def mock_generator():
            yield mock_db

        mock_get_db_func.return_value = mock_generator()

        with patch('services.lunar_returns_service.refresh_lunar_returns_batch') as mock_refresh:
            mock_refresh.return_value = mock_result

            with patch('services.scheduler_services.lunar_returns_refresh_total') as mock_counter:
                with patch('services.scheduler_services.lunar_returns_refresh_duration_seconds') as mock_histogram:
                    with patch('services.scheduler_services.lunar_returns_refresh_failure_rate') as mock_gauge_rate:
                        with patch('services.scheduler_services.lunar_returns_refresh_users_total') as mock_gauge_users:

                            await refresh_lunar_returns_cron()

                            # Vérifier Counter
                            mock_counter.labels.assert_any_call(status='success')
                            mock_counter.labels.assert_any_call(status='failed')

                            # Vérifier Histogram
                            mock_histogram.observe.assert_called_once()

                            # Vérifier Gauge failure_rate
                            expected_failure_rate = 8 / 100
                            mock_gauge_rate.set.assert_called_once_with(expected_failure_rate)

                            # Vérifier Gauge total_users
                            mock_gauge_users.set.assert_called_once_with(100)


# === TEST 5 : Gestion cas limite total_users = 0 ===

@pytest.mark.asyncio
async def test_alert_handles_zero_users_gracefully(caplog):
    """
    Test: Gestion cas limite total_users = 0
    Expected: Pas de division par zéro, failure_rate = 0.0
    """
    mock_db = AsyncMock()

    mock_result = {
        "total_users": 0,
        "successful": 0,
        "failed": 0,
        "duration_seconds": 5.0,
        "errors": [],
        "window": {"start": "2026-02-01", "end": "2026-02-08"}
    }

    with patch('services.scheduler_services.get_db') as mock_get_db_func:
        async def mock_generator():
            yield mock_db

        mock_get_db_func.return_value = mock_generator()

        with patch('services.lunar_returns_service.refresh_lunar_returns_batch') as mock_refresh:
            mock_refresh.return_value = mock_result

            with caplog.at_level(logging.INFO):
                await refresh_lunar_returns_cron()

    # Vérifier aucune exception (pas de division par zéro)
    info_logs = [r for r in caplog.records if r.levelname == 'INFO']
    success_logs = [r for r in info_logs if "✅ [CRON] Rafraîchissement terminé" in r.message]

    assert len(success_logs) > 0, "Expected success log even with 0 users"
    assert "failure_rate=0.0%" in success_logs[0].message or "failure_rate=0%" in success_logs[0].message
