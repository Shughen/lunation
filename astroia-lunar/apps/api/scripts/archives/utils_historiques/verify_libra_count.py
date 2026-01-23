"""Vérification du nombre d'interprétations Libra insérées"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import select, func
from database import AsyncSessionLocal
from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation

async def verify_libra():
    """Vérifie les interprétations Libra en DB"""
    async with AsyncSessionLocal() as session:
        # Count total
        stmt = select(func.count()).where(
            PregeneratedLunarInterpretation.moon_sign == 'Libra',
            PregeneratedLunarInterpretation.version == 2
        )
        result = await session.execute(stmt)
        total = result.scalar()
        print(f"Total Libra V2: {total}")

        # Count per house
        stmt = select(
            PregeneratedLunarInterpretation.moon_house,
            func.count().label('count')
        ).where(
            PregeneratedLunarInterpretation.moon_sign == 'Libra',
            PregeneratedLunarInterpretation.version == 2
        ).group_by(
            PregeneratedLunarInterpretation.moon_house
        ).order_by(
            PregeneratedLunarInterpretation.moon_house
        )
        result = await session.execute(stmt)
        print("\nPar maison:")
        for row in result:
            print(f"  M{row.moon_house}: {row.count} interprétations")

if __name__ == "__main__":
    asyncio.run(verify_libra())
