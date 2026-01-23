#!/usr/bin/env python3
"""
Sprint 4 - Audit initial de l'état des interprétations lunaires V2
"""
import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from sqlalchemy import text

async def audit_interpretations():
    """Audit l'état actuel des interprétations V2 en DB"""
    async with AsyncSessionLocal() as session:
        # Count total
        result = await session.execute(
            text("SELECT COUNT(*) FROM pregenerated_lunar_interpretations")
        )
        total_result = result.scalar()

        print(f"\n{'='*60}")
        print(f"SPRINT 4 - AUDIT INTERPRETATIONS LUNAIRES V2")
        print(f"{'='*60}\n")
        print(f"Total interprétations en DB: {total_result}/1728")
        print(f"Progression: {total_result/1728*100:.1f}%")
        print(f"\n{'='*60}")
        print(f"DÉTAIL PAR SIGNE LUNAIRE")
        print(f"{'='*60}\n")

        # Count by sign
        result = await session.execute(
            text("""
                SELECT moon_sign, COUNT(*) as count
                FROM pregenerated_lunar_interpretations
                GROUP BY moon_sign
                ORDER BY moon_sign
            """)
        )
        results = result.fetchall()

        complete_signs = []
        partial_signs = []

        for row in results:
            sign, count = row
            status = "✅ COMPLET" if count == 144 else f"⚠️  PARTIEL ({144-count} manquantes)"
            print(f"{sign:12} : {count:3}/144 {status}")

            if count == 144:
                complete_signs.append(sign)
            else:
                partial_signs.append((sign, count, 144-count))

        # All signs
        all_signs = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ]

        existing_signs = [row[0] for row in results]
        missing_signs = [s for s in all_signs if s not in existing_signs]

        if missing_signs:
            print(f"\n{'='*60}")
            print(f"SIGNES MANQUANTS (0/144)")
            print(f"{'='*60}\n")
            for sign in missing_signs:
                print(f"{sign:12} : 0/144 ❌ AUCUNE INTERPRÉTATION")

        print(f"\n{'='*60}")
        print(f"RÉSUMÉ SPRINT 4")
        print(f"{'='*60}\n")
        print(f"✅ Signes complets (144/144) : {len(complete_signs)}/12")
        for sign in complete_signs:
            print(f"   - {sign}")

        if partial_signs or missing_signs:
            total_missing = sum(missing for _, _, missing in partial_signs) + len(missing_signs) * 144
            print(f"\n⚠️  Signes partiels : {len(partial_signs)}/12")
            for sign, count, missing in partial_signs:
                print(f"   - {sign}: {count}/144 ({missing} manquantes)")

            if missing_signs:
                print(f"\n❌ Signes vides : {len(missing_signs)}/12")
                for sign in missing_signs:
                    print(f"   - {sign}: 0/144 (144 manquantes)")

            print(f"\n🎯 OBJECTIF SPRINT 4 : Générer {total_missing} interprétations")
            print(f"   Coût estimé: $3-5 / Temps: 10-15min")
        else:
            print(f"\n🎉 MIGRATION V2 COMPLÈTE À 100% !")

        print(f"\n{'='*60}\n")

if __name__ == "__main__":
    asyncio.run(audit_interpretations())
