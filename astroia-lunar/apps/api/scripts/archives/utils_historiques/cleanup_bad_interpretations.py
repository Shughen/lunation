"""Nettoyer les interprétations mal générées et garder uniquement Aries"""
import asyncio
from database import AsyncSessionLocal
from sqlalchemy import delete, select, func
from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation

async def cleanup():
    async with AsyncSessionLocal() as session:
        # Supprimer tout sauf Aries
        stmt = delete(PregeneratedLunarInterpretation).where(
            PregeneratedLunarInterpretation.moon_sign.notin_(['Aries'])
        )
        result = await session.execute(stmt)
        await session.commit()
        print(f'[+] Supprimé {result.rowcount} interprétations mal générées')

        # Stats finales
        result = await session.execute(select(func.count()).select_from(PregeneratedLunarInterpretation))
        total = result.scalar()
        print(f'[+] Restant en base: {total}/1728 (Aries uniquement)')

        result = await session.execute(
            select(PregeneratedLunarInterpretation.moon_sign, func.count())
            .group_by(PregeneratedLunarInterpretation.moon_sign)
        )
        for row in result:
            print(f'  {row[0]}: {row[1]}')

asyncio.run(cleanup())
