#!/usr/bin/env python3
"""
Script Nettoyage Complet A/B Test
Date: 2026-01-24

OBJECTIF:
- Supprimer TOUTES les données de lunar_interpretations_ab_test
- Repartir à zéro pour un test A/B propre

Usage:
    python scripts/ab_test_reset_complete.py
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from database import get_db


async def reset_ab_test_table():
    """Supprimer toutes les données A/B test et repartir à zéro"""

    print("⚠️  NETTOYAGE COMPLET : Reset table lunar_interpretations_ab_test")
    print("   Action: DELETE FROM lunar_interpretations_ab_test (TOUT)")
    print()

    # Compter d'abord
    count_sql = "SELECT COUNT(*) FROM lunar_interpretations_ab_test"

    count_by_model_sql = """
    SELECT model_tested, COUNT(*) as count
    FROM lunar_interpretations_ab_test
    GROUP BY model_tested
    ORDER BY model_tested
    """

    async for db in get_db():
        # Compter total
        result = await db.execute(text(count_sql))
        total_count = result.scalar()

        print(f"📊 Données actuelles : {total_count} entrées")

        if total_count == 0:
            print("✅ Table déjà vide")
            return

        # Compter par modèle
        result = await db.execute(text(count_by_model_sql))
        rows = result.fetchall()

        print("\n📋 Répartition par modèle:")
        for row in rows:
            print(f"   {row.model_tested}: {row.count} entrées")

        # Confirmation
        print(f"\n⚠️  Confirmer suppression de TOUTES les {total_count} entrées ? (y/N): ", end="")
        confirm = input().strip().lower()

        if confirm != 'y':
            print("❌ Annulé")
            return

        # Suppression totale
        delete_sql = "DELETE FROM lunar_interpretations_ab_test"
        await db.execute(text(delete_sql))
        await db.commit()

        # Vérifier après suppression
        result = await db.execute(text(count_sql))
        count_after = result.scalar()

        print(f"\n✅ Suppression terminée : {total_count} → {count_after} entrées")
        print()
        print("🎯 Prêt pour nouveau test A/B complet:")
        print("   1. python scripts/ab_test_generate_sample.py --model opus --count 24")
        print("   2. python scripts/ab_test_generate_sonnet_fixed.py")
        print("   3. python scripts/ab_test_analyze.py --cost")

        break


if __name__ == "__main__":
    asyncio.run(reset_ab_test_table())
