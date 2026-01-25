#!/usr/bin/env python3
"""
Script de Nettoyage - Lunar Interpretations DB
Date: 2026-01-24

Usage:
    python scripts/clean_lunar_interpretations.py

ATTENTION: Ce script supprime TOUTES les interprétations de la table lunar_interpretations.
Utilisez uniquement pour tests A/B ou développement.
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from database import get_db


async def clean_interpretations():
    """Supprimer toutes les interprétations de la table lunar_interpretations"""

    print("⚠️  ATTENTION : Suppression de TOUTES les interprétations lunaires...")
    print("   Table: lunar_interpretations")
    print()

    # Compter d'abord
    count_sql = "SELECT COUNT(*) FROM lunar_interpretations"

    async for db in get_db():
        # Compter avant suppression
        result = await db.execute(text(count_sql))
        count_before = result.scalar()

        print(f"📊 Interprétations actuelles : {count_before}")

        if count_before == 0:
            print("✅ Aucune interprétation à supprimer")
            return

        # Suppression
        delete_sql = "DELETE FROM lunar_interpretations"
        await db.execute(text(delete_sql))
        await db.commit()

        # Vérifier après suppression
        result = await db.execute(text(count_sql))
        count_after = result.scalar()

        print(f"✅ Suppression terminée : {count_before} → {count_after} interprétations")
        print()
        print("🎯 Prêt pour nouveaux tests A/B")

        break


if __name__ == "__main__":
    asyncio.run(clean_interpretations())
