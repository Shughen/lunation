#!/usr/bin/env python3
"""
Identify missing lunar interpretation combinations in DB
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from sqlalchemy import text

SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
HOUSES = list(range(1, 13))
ASCENDANTS = SIGNS.copy()

async def identify_missing():
    """Identify all missing combinations for Pisces and Scorpio"""
    async with AsyncSessionLocal() as session:
        for target_sign in ['Pisces', 'Scorpio']:
            print(f"\n{'='*60}")
            print(f"Missing combinations for {target_sign}")
            print(f"{'='*60}\n")

            missing = []

            for house in HOUSES:
                for asc in ASCENDANTS:
                    result = await session.execute(
                        text("""
                            SELECT COUNT(*)
                            FROM pregenerated_lunar_interpretations
                            WHERE moon_sign = :sign
                            AND moon_house = :house
                            AND lunar_ascendant = :asc
                        """),
                        {'sign': target_sign, 'house': house, 'asc': asc}
                    )
                    count = result.scalar()

                    if count == 0:
                        missing.append((target_sign, house, asc))

            print(f"Missing: {len(missing)} combinations\n")

            # Group by house
            by_house = {}
            for sign, house, asc in missing:
                if house not in by_house:
                    by_house[house] = []
                by_house[house].append(asc)

            for house in sorted(by_house.keys()):
                ascs = by_house[house]
                print(f"  Maison {house:2d}: {len(ascs):2d} manquantes → {', '.join(ascs)}")

if __name__ == "__main__":
    asyncio.run(identify_missing())
