#!/usr/bin/env python3
"""
Script Nettoyage Résultats Sonnet Invalides
Date: 2026-01-24

CONTEXTE:
- Premier test Sonnet a échoué (UNIQUE constraint violations)
- 24 entrées "sonnet" dans lunar_interpretations_ab_test sont en fait des templates
- Ce script les supprime pour permettre régénération propre

Usage:
    python scripts/ab_test_cleanup_invalid_sonnet.py
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from database import get_db


async def cleanup_invalid_sonnet():
    """Supprimer résultats Sonnet invalides (templates, pas Claude)"""

    print("⚠️  NETTOYAGE : Suppression résultats Sonnet invalides...")
    print("   Contexte: Premier test Sonnet a échoué (UNIQUE constraints)")
    print("   Action: DELETE FROM lunar_interpretations_ab_test WHERE model_tested='sonnet'")
    print()

    # Compter d'abord
    count_sql = """
    SELECT COUNT(*) FROM lunar_interpretations_ab_test
    WHERE model_tested = 'sonnet'
    """

    async for db in get_db():
        # Compter avant suppression
        result = await db.execute(text(count_sql))
        count_before = result.scalar()

        print(f"📊 Résultats Sonnet actuels : {count_before}")

        if count_before == 0:
            print("✅ Aucun résultat Sonnet à supprimer")
            return

        # Afficher échantillon pour vérifier
        sample_sql = """
        SELECT lunar_return_id, LENGTH(output_text) as length
        FROM lunar_interpretations_ab_test
        WHERE model_tested = 'sonnet'
        LIMIT 5
        """

        result = await db.execute(text(sample_sql))
        samples = result.fetchall()

        print("\n📋 Échantillon résultats à supprimer:")
        for s in samples:
            print(f"   lunar_return_id={s.lunar_return_id}, length={s.length} chars")

        # Confirmation
        print(f"\n⚠️  Confirmer suppression de {count_before} résultats Sonnet ? (y/N): ", end="")
        confirm = input().strip().lower()

        if confirm != 'y':
            print("❌ Annulé")
            return

        # Suppression
        delete_sql = """
        DELETE FROM lunar_interpretations_ab_test
        WHERE model_tested = 'sonnet'
        """

        await db.execute(text(delete_sql))
        await db.commit()

        # Vérifier après suppression
        result = await db.execute(text(count_sql))
        count_after = result.scalar()

        print(f"\n✅ Suppression terminée : {count_before} → {count_after} résultats Sonnet")
        print()
        print("🎯 Prêt pour régénération propre avec:")
        print("   python scripts/ab_test_generate_sonnet_fixed.py")

        break


if __name__ == "__main__":
    asyncio.run(cleanup_invalid_sonnet())
