"""
Script pour vérifier l'entrée en base de données de Nathan
"""

import sys
import asyncio
from pathlib import Path
from datetime import datetime

# Ajouter le répertoire parent au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from models.natal_chart import NatalChart
from sqlalchemy import select

async def check_nathan_chart():
    """Vérifie le thème natal de Nathan en base"""
    async with AsyncSessionLocal() as session:
        # Chercher tous les thèmes nataux avec date de naissance = 2001-02-09
        stmt = select(NatalChart).where(NatalChart.birth_date == datetime(2001, 2, 9).date())
        result = await session.execute(stmt)
        charts = result.scalars().all()

        if not charts:
            print("❌ Aucun thème natal trouvé pour le 9 février 2001")
            return

        for chart in charts:
            print(f"\n📊 Thème natal trouvé:")
            print(f"   - ID: {chart.id}")
            print(f"   - User ID: {chart.user_id}")
            print(f"   - Date: {chart.birth_date}")
            print(f"   - Heure: {chart.birth_time}")
            print(f"   - Lieu: {chart.birth_place}")
            print(f"   - Latitude: {chart.latitude}")
            print(f"   - Longitude: {chart.longitude}")
            print(f"   - Timezone: {chart.timezone}")
            print()

            # Vérifier les positions
            positions = chart.positions or {}

            # Vérifier la Lune
            moon_data = positions.get("moon")
            if moon_data:
                print(f"🌙 Lune (données brutes):")
                print(f"   - Signe: {moon_data.get('sign')}")
                print(f"   - Degré: {moon_data.get('degree')}")
                print(f"   - Maison: {moon_data.get('house')}")
            else:
                print(f"⚠️ Pas de données pour la Lune dans positions")

            # Vérifier planets
            planets = positions.get("planets", {})
            moon_planet = planets.get("moon")
            if moon_planet:
                print(f"\n🌙 Lune (dans planets):")
                print(f"   - Signe: {moon_planet.get('sign')}")
                print(f"   - Degré: {moon_planet.get('degree')}")
                print(f"   - Maison: {moon_planet.get('house')}")

            # Afficher toutes les clés de positions pour debug
            print(f"\n📦 Clés dans positions: {list(positions.keys())}")

            # Si la Lune est en Lion, c'est une erreur
            moon_sign = moon_data.get('sign') if moon_data else None
            if moon_sign and "Leo" in moon_sign:
                print(f"\n❌ ERREUR DÉTECTÉE: La Lune est en {moon_sign}, devrait être en Virgo")

if __name__ == "__main__":
    asyncio.run(check_nathan_chart())
