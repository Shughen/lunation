#!/usr/bin/env python3
"""
Script Génération Sonnet A/B Test - Version Simple
Date: 2026-01-24

Utilise le même pattern que le script Opus qui fonctionne,
mais génère avec Sonnet au lieu d'Opus.
"""

import asyncio
import sys
import os
import json
from sqlalchemy import text

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import get_db
from services.lunar_interpretation_generator import generate_or_get_interpretation
from config import settings

# Override temporairement le model pour Sonnet
original_model = settings.LUNAR_CLAUDE_MODEL

async def run_sonnet_test():
    """Exécuter test Sonnet en utilisant le service generator avec modèle Sonnet"""

    print("=" * 60)
    print("🧪 A/B Test Sonnet - Version Simple")
    print("   Stratégie: Utilise le service generator avec Sonnet")
    print("=" * 60)
    print()

    # Override model config temporairement
    settings.LUNAR_CLAUDE_MODEL = "sonnet"

    try:
        # Récupérer les lunar_return_ids depuis le test Opus
        async for db in get_db():
            result = await db.execute(text("""
                SELECT DISTINCT lunar_return_id, user_id
                FROM lunar_interpretations_ab_test
                WHERE model_tested = 'opus'
                ORDER BY lunar_return_id
            """))
            opus_samples = result.fetchall()
            print(f"✅ Récupéré {len(opus_samples)} lunar_returns depuis test Opus")
            print()
            break

        count = len(opus_samples)
        successful = 0
        failed = 0
        total_duration = 0.0

        for i, row in enumerate(opus_samples, 1):
            lunar_return_id = row.lunar_return_id
            user_id = row.user_id

            try:
                print(f"[{i}/{count}] Génération Sonnet (lunar_return_id={lunar_return_id})...", end=" ", flush=True)

                # Utiliser le service generator (force=True pour bypass cache)
                import time
                start = time.time()

                interpretation = await generate_or_get_interpretation(
                    lunar_return_id=lunar_return_id,
                    subject="full",
                    version=2,
                    lang="fr",
                    force_regenerate=True  # Force nouvelle génération
                )

                duration = time.time() - start

                # Sauvegarder dans table A/B test
                async for db in get_db():
                    await db.execute(text("""
                        INSERT INTO lunar_interpretations_ab_test
                        (user_id, lunar_return_id, model_tested, output_text, weekly_advice, metadata, duration_seconds)
                        VALUES (:user_id, :lunar_return_id, :model_tested, :output_text, :weekly_advice, :metadata, :duration_seconds)
                    """), {
                        "user_id": user_id,
                        "lunar_return_id": lunar_return_id,
                        "model_tested": "sonnet",
                        "output_text": interpretation["output_text"],
                        "weekly_advice": json.dumps(interpretation.get("weekly_advice", [])),
                        "metadata": json.dumps({"source": interpretation["source"], "model_used": interpretation.get("model_used", "sonnet")}),
                        "duration_seconds": duration
                    })
                    await db.commit()
                    break

                source = interpretation["source"]
                length = len(interpretation["output_text"])
                total_duration += duration
                successful += 1

                print(f"✅ {duration:.1f}s | {source} | {length} chars")

            except Exception as e:
                failed += 1
                print(f"❌ Erreur: {e}")
                import traceback
                traceback.print_exc()

        # Rapport final
        print()
        print("=" * 60)
        print("📊 Résultats A/B Test - SONNET")
        print("=" * 60)
        print(f"Générations réussies : {successful}/{count} ({successful/count*100:.1f}%)" if count > 0 else "N/A")
        print(f"Générations échouées : {failed}/{count}")
        print(f"Durée moyenne        : {total_duration/successful:.1f}s" if successful > 0 else "N/A")
        print(f"Durée totale         : {total_duration:.1f}s ({total_duration/60:.1f} minutes)")
        print("=" * 60)
        print()

    finally:
        # Restore original model
        settings.LUNAR_CLAUDE_MODEL = original_model


if __name__ == "__main__":
    asyncio.run(run_sonnet_test())
