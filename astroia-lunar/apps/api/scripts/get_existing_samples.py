#!/usr/bin/env python3
"""
Récupère des exemples d'interprétations existantes pour comprendre le format
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from sqlalchemy import text

async def get_samples():
    """Récupère 5 exemples d'interprétations existantes"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            text("""
                SELECT moon_sign, moon_house, lunar_ascendant, interpretation_full, weekly_advice
                FROM pregenerated_lunar_interpretations
                WHERE moon_sign IN ('Aries', 'Taurus', 'Gemini')
                LIMIT 5
            """)
        )
        samples = result.fetchall()

        for i, (sign, house, asc, interp, advice) in enumerate(samples, 1):
            print(f"\n{'='*60}")
            print(f"EXEMPLE {i}: {sign} M{house} Asc {asc}")
            print(f"{'='*60}\n")
            print("INTERPRETATION:")
            print(interp)
            print(f"\nWEEKLY ADVICE:")
            import json
            print(json.dumps(advice, indent=2, ensure_ascii=False))
            print(f"\n{'='*60}\n")

if __name__ == "__main__":
    asyncio.run(get_samples())
