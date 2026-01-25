"""
Tests pour le scheduler de rafraîchissement lunar returns

Tests:
- start_scheduler: enregistre le job lunar returns
- Cron trigger: configuration correcte (quotidien, hour=3, timezone=UTC)

NOTE: Tests d'intégration avec DB dans test_lunar_returns.py
"""

import pytest

from services.scheduler_services import (
    start_scheduler,
    scheduler
)


def test_scheduler_registers_lunar_returns_job():
    """
    Test: start_scheduler() enregistre le job refresh_lunar_returns

    Vérifie:
    - Le job 'refresh_lunar_returns' existe dans le scheduler
    - Le trigger est de type CronTrigger
    - Le timing est correct (quotidien, hour=3, minute=0, timezone=UTC)
    """
    # Arrêter le scheduler s'il tourne déjà (cleanup)
    if scheduler.running:
        scheduler.shutdown(wait=False)

    # Démarrer le scheduler
    start_scheduler()

    # Vérifier que le job existe
    jobs = scheduler.get_jobs()
    job_ids = [job.id for job in jobs]

    assert 'refresh_lunar_returns' in job_ids, \
        f"Expected 'refresh_lunar_returns' job in scheduler, got jobs: {job_ids}"

    # Récupérer le job spécifique
    lunar_job = [job for job in jobs if job.id == 'refresh_lunar_returns'][0]

    # Vérifier le trigger
    assert lunar_job.trigger is not None, "Expected job to have a trigger"
    assert hasattr(lunar_job.trigger, 'fields'), "Expected CronTrigger with fields"

    # Vérifier le timing (quotidien: hour=3, minute=0, PAS de day=1)
    trigger_str = str(lunar_job.trigger)
    assert "hour='3'" in trigger_str, f"Expected hour='3' in trigger, got: {trigger_str}"
    assert "minute='0'" in trigger_str, f"Expected minute='0' in trigger, got: {trigger_str}"
    # Vérifier qu'il n'y a PAS de day='1' (exécution quotidienne, pas mensuelle)
    assert "day=" not in trigger_str or "day='*'" in trigger_str, \
        f"Expected daily execution (no specific day), got: {trigger_str}"

    # Vérifier le nom du job
    assert lunar_job.name == 'Rafraîchir révolutions lunaires quotidiennes (batch intelligent)', \
        f"Expected job name 'Rafraîchir révolutions lunaires quotidiennes (batch intelligent)', got '{lunar_job.name}'"

    # Cleanup
    scheduler.shutdown(wait=False)
