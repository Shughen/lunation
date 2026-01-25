"""
Services de planification pour notifications et tâches périodiques (P4)
Utilise APScheduler pour rafraîchir les données VoC et autres tâches récurrentes
"""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import logging
import time

from services import lunar_services
from database import get_db
from models.lunar_pack import LunarVocWindow
from prometheus_client import Counter, Histogram, Gauge

logger = logging.getLogger(__name__)

# === MÉTRIQUES PROMETHEUS - SCHEDULER ===

# Métrique 1 : Nombre total de users rafraîchis (par statut)
lunar_returns_refresh_total = Counter(
    'lunar_returns_refresh_total',
    'Total users processed during lunar returns refresh',
    ['status']  # 'success' | 'failed'
)

# Métrique 2 : Durée totale du refresh complet
lunar_returns_refresh_duration_seconds = Histogram(
    'lunar_returns_refresh_duration_seconds',
    'Duration of complete refresh cycle',
    buckets=(5, 10, 30, 60, 120, 300, 600)  # 5s → 10min
)

# Métrique 3 : Taux d'échec du dernier refresh (0-1)
lunar_returns_refresh_failure_rate = Gauge(
    'lunar_returns_refresh_failure_rate',
    'Failure rate of last refresh cycle (0-1)'
)

# Métrique 4 : Nombre total d'utilisateurs traités
lunar_returns_refresh_users_total = Gauge(
    'lunar_returns_refresh_users_total',
    'Total users processed in last refresh cycle'
)

# Instance du scheduler (singleton)
scheduler = AsyncIOScheduler()


async def refresh_voc_windows():
    """
    Tâche périodique pour rafraîchir les fenêtres Void of Course.
    
    Appelée toutes les 2 heures pour maintenir les données VoC à jour.
    En production, cette tâche devrait être déplacée vers un worker séparé.
    """
    logger.info("🔄 Rafraîchissement automatique des fenêtres VoC...")
    
    try:
        # Calculer les fenêtres VoC pour les 7 prochains jours
        # (logique simplifiée, à adapter selon les besoins réels)
        now = datetime.now()
        end_date = now + timedelta(days=7)
        
        # Payload générique (Paris par défaut)
        payload = {
            "start_date": now.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "latitude": 48.8566,
            "longitude": 2.3522,
            "timezone": "Europe/Paris"
        }
        
        # Appel au service (si l'API provider le supporte)
        # result = await lunar_services.get_void_of_course_status(payload)
        
        # Pour l'instant, log uniquement
        logger.info("✅ Rafraîchissement VoC terminé (placeholder)")
        
    except Exception as e:
        logger.error(f"❌ Erreur lors du rafraîchissement VoC: {str(e)}")


async def refresh_lunar_returns_cron():
    """
    Tâche cron : Rafraîchir lunar returns (batching intelligent).
    Exécuté CHAQUE JOUR à 3h (UTC).

    Cible : Users dont la prochaine révolution lunaire tombe entre J+7 et J+14.
    """
    logger.info("🌙 [CRON] Démarrage rafraîchissement lunar returns (batch quotidien)...")

    start_time = time.time()

    try:
        async for db in get_db():
            from services.lunar_returns_service import refresh_lunar_returns_batch
            from config import settings

            # Appeler fonction batch avec fenêtre configurable
            result = await refresh_lunar_returns_batch(
                db=db,
                window_start_days=settings.LUNAR_REFRESH_WINDOW_START_DAYS,
                window_end_days=settings.LUNAR_REFRESH_WINDOW_END_DAYS
            )

            duration = time.time() - start_time

            # === MÉTRIQUES PROMETHEUS ===
            lunar_returns_refresh_total.labels(status='success').inc(result['successful'])
            lunar_returns_refresh_total.labels(status='failed').inc(result['failed'])
            lunar_returns_refresh_duration_seconds.observe(duration)
            lunar_returns_refresh_users_total.set(result['total_users'])

            # Calculer taux d'échec (éviter division par zéro)
            failure_rate = 0.0
            if result['total_users'] > 0:
                failure_rate = result['failed'] / result['total_users']

            lunar_returns_refresh_failure_rate.set(failure_rate)

            # === LOG STANDARD (INFO) ===
            logger.info(
                f"✅ [CRON] Rafraîchissement terminé - "
                f"window={result['window']['start']}→{result['window']['end']}, "
                f"users={result['total_users']}, "
                f"success={result['successful']}, "
                f"failed={result['failed']}, "
                f"failure_rate={failure_rate:.1%}, "
                f"duration={duration:.1f}s"
            )

            # === ALERTE SI TAUX D'ÉCHEC > SEUIL ===
            threshold = settings.LUNAR_REFRESH_ALERT_THRESHOLD

            if failure_rate > threshold:
                # Limiter les erreurs à 5 pour éviter logs trop longs
                errors_sample = result['errors'][:5]

                logger.error(
                    f"🚨 [ALERT] Taux d'échec élevé: {failure_rate:.1%} "
                    f"({result['failed']}/{result['total_users']} users) - "
                    f"window={result['window']['start']}→{result['window']['end']}",
                    extra={
                        "alert_type": "lunar_refresh_high_failure_rate",
                        "failure_rate": failure_rate,
                        "threshold": threshold,
                        "total_users": result['total_users'],
                        "successful": result['successful'],
                        "failed": result['failed'],
                        "duration_seconds": round(duration, 2),
                        "window_start": result['window']['start'],
                        "window_end": result['window']['end'],
                        "errors_sample": errors_sample
                    }
                )

            break  # Important : sortir après première DB session

    except Exception as e:
        logger.error(f"❌ [CRON] Erreur rafraîchissement batch: {e}", exc_info=True)


async def get_next_voc_window() -> dict:
    """
    Récupère la prochaine fenêtre VoC depuis la DB.

    Returns:
        {
            "start_at": "2025-01-15T10:30:00+01:00",
            "end_at": "2025-01-15T14:45:00+01:00",
            "time_until": "2h 15min"
        }
        ou None si aucune fenêtre trouvée
    """
    try:
        async for db in get_db():
            from sqlalchemy import select

            now = datetime.now()

            # Chercher la prochaine fenêtre VoC
            stmt = select(LunarVocWindow).where(
                LunarVocWindow.start_at > now
            ).order_by(LunarVocWindow.start_at).limit(1)

            result = await db.execute(stmt)
            next_voc = result.scalar_one_or_none()

            if next_voc:
                time_until = next_voc.start_at - now
                hours = int(time_until.total_seconds() // 3600)
                minutes = int((time_until.total_seconds() % 3600) // 60)

                return {
                    "start_at": next_voc.start_at.isoformat(),
                    "end_at": next_voc.end_at.isoformat(),
                    "time_until": f"{hours}h {minutes}min",
                    "time_until_seconds": int(time_until.total_seconds())
                }

            return None

    except Exception as e:
        logger.error(f"❌ Erreur récupération next VoC: {str(e)}")
        return None


def start_scheduler():
    """
    Démarre le scheduler avec les tâches périodiques.

    IMPORTANT: En production, déplacer vers un worker dédié (Celery, RQ, etc.)
    pour éviter de surcharger le serveur web.
    """
    if not scheduler.running:
        # Tâche: Rafraîchir les fenêtres VoC toutes les 2 heures
        scheduler.add_job(
            refresh_voc_windows,
            trigger='interval',
            hours=2,
            id='refresh_voc',
            name='Rafraîchir fenêtres Void of Course',
            replace_existing=True
        )

        # Tâche: Rafraîchir lunar returns CHAQUE JOUR à 3h UTC
        scheduler.add_job(
            refresh_lunar_returns_cron,
            trigger='cron',
            hour=3,         # 3h du matin
            minute=0,       # Pile
            timezone='UTC', # Toujours UTC
            id='refresh_lunar_returns',
            name='Rafraîchir révolutions lunaires quotidiennes (batch intelligent)',
            replace_existing=True
        )

        scheduler.start()
        logger.info("✅ Scheduler démarré (VoC + Lunar Returns)")
    else:
        logger.info("ℹ️  Scheduler déjà en cours d'exécution")


def stop_scheduler():
    """Arrête le scheduler proprement."""
    if scheduler.running:
        scheduler.shutdown(wait=False)
        logger.info("👋 Scheduler arrêté")

