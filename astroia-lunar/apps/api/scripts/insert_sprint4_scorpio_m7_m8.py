"""Insert Scorpio M7-M8 interpretations"""
import asyncio
import sys
import uuid
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation
from sqlalchemy.dialects.postgresql import insert
from scripts.batch_sprint4_scorpio_m7_m8 import BATCH_SCORPIO_M7_M8


async def insert_interpretation(moon_sign: str, moon_house: int, lunar_ascendant: str,
                                interpretation: str, weekly_advice: dict):
    """Insere une interpretation en base"""
    async with AsyncSessionLocal() as session:
        stmt = insert(PregeneratedLunarInterpretation).values(
            id=uuid.uuid4(),
            moon_sign=moon_sign,
            moon_house=moon_house,
            lunar_ascendant=lunar_ascendant,
            version=2,
            lang='fr',
            interpretation_full=interpretation,
            weekly_advice=weekly_advice,
            length=len(interpretation),
            model_used='claude-opus-4-5-manual'
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=['moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'],
            set_={
                'interpretation_full': interpretation,
                'weekly_advice': weekly_advice,
                'length': len(interpretation),
                'model_used': 'claude-opus-4-5-manual',
                'updated_at': datetime.now()
            }
        )

        await session.execute(stmt)
        await session.commit()
        print(f"  [+] {moon_sign} M{moon_house} ASC {lunar_ascendant} ({len(interpretation)} chars)")


async def insert_batch(interpretations: list):
    """Insere un batch d'interpretations"""
    for item in interpretations:
        await insert_interpretation(
            item['moon_sign'],
            item['moon_house'],
            item['lunar_ascendant'],
            item['interpretation'],
            item['weekly_advice']
        )
    print(f"\n[OK] {len(interpretations)} interpretations inserees")


if __name__ == "__main__":
    print(f"Insertion de {len(BATCH_SCORPIO_M7_M8)} interpretations Scorpio M7-M8...")
    asyncio.run(insert_batch(BATCH_SCORPIO_M7_M8))
