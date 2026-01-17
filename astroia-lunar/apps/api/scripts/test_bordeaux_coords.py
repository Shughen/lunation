"""
Vérifier si les coordonnées de Bordeaux sont correctes
et si elles n'influencent pas le calcul (elles ne devraient pas pour la Lune)
"""

import sys
import asyncio
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.swiss_ephemeris import get_moon_position
from services.natal_reading_service import call_rapidapi_natal_chart

async def test_coords():
    """
    Test avec différentes coordonnées pour voir si ça change la position de la Lune
    """
    print("=" * 80)
    print("TEST - INFLUENCE DES COORDONNÉES GPS SUR LA LUNE")
    print("=" * 80)
    print()

    # La Lune ne devrait PAS être influencée par les coordonnées GPS
    # (seulement l'Ascendant et les Maisons le sont)

    coords_tests = [
        {
            "name": "Bordeaux (coordonnées correctes)",
            "lat": 44.8378,
            "lon": -0.5792
        },
        {
            "name": "Bordeaux (coordonnées inversées)",
            "lat": -0.5792,
            "lon": 44.8378
        },
        {
            "name": "Paris",
            "lat": 48.8566,
            "lon": 2.3522
        }
    ]

    # Position Lune depuis Swiss Ephemeris (ne dépend PAS des coordonnées)
    birth_datetime_utc = datetime(2001, 2, 9, 10, 30, 0, tzinfo=timezone.utc)
    expected_moon = get_moon_position(birth_datetime_utc)

    print(f"Position Lune attendue (Swiss Ephemeris, indépendante du lieu):")
    print(f"  {expected_moon.sign} {expected_moon.degree:.2f}° (longitude: {expected_moon.longitude:.2f}°)")
    print()
    print("-" * 80)
    print()

    for test in coords_tests:
        print(f"Test avec: {test['name']}")
        print(f"  Lat: {test['lat']}, Lon: {test['lon']}")

        birth_data = {
            "year": 2001,
            "month": 2,
            "day": 9,
            "hour": 11,
            "minute": 30,
            "second": 0,
            "city": "Test",
            "country_code": "FR",
            "latitude": test['lat'],
            "longitude": test['lon'],
            "timezone": "Europe/Paris"
        }

        try:
            response = await call_rapidapi_natal_chart(birth_data)
            chart_data = response.get("chart_data", {})
            positions = chart_data.get("planetary_positions", [])

            moon_pos = None
            for pos in positions:
                if pos.get("name", "").lower() == "moon":
                    moon_pos = pos
                    break

            if moon_pos:
                moon_sign = moon_pos.get("sign")
                moon_degree = moon_pos.get("degree")
                moon_abs_long = moon_pos.get("absolute_longitude")

                status = "✅" if moon_sign == "Vir" else "❌"
                print(f"  {status} Lune: {moon_sign} {moon_degree}° (abs: {moon_abs_long}°)")
            else:
                print(f"  ❌ Pas de position Lune trouvée")

        except Exception as e:
            print(f"  ❌ Erreur: {e}")

        print()

    print("=" * 80)
    print("CONCLUSION:")
    print("=" * 80)
    print()
    print("La position de la Lune ne devrait PAS changer avec les coordonnées GPS.")
    print("Seules l'Ascendant et les Maisons sont influencés par le lieu de naissance.")
    print()
    print("Si la Lune change de signe selon les coordonnées, c'est un BUG dans RapidAPI.")
    print()

if __name__ == "__main__":
    asyncio.run(test_coords())
