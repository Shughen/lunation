"""
Script de test pour vérifier la réponse RapidAPI pour Nathan
Né le 9 février 2001 à 11h30 à Bordeaux
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime, timezone

# Ajouter le répertoire parent au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.natal_reading_service import call_rapidapi_natal_chart
from services.swiss_ephemeris import get_moon_position

async def test_nathan_rapidapi():
    """
    Test la réponse RapidAPI pour Nathan
    """
    # Données de naissance de Nathan
    # Bordeaux: lat=44.8378, lon=-0.5792
    # Date: 9 février 2001 à 11h30 (heure locale)
    # Timezone: Europe/Paris (UTC+1 en hiver)

    birth_data = {
        "year": 2001,
        "month": 2,
        "day": 9,
        "hour": 11,
        "minute": 30,
        "second": 0,
        "city": "Bordeaux",
        "country_code": "FR",
        "latitude": 44.8378,
        "longitude": -0.5792,
        "timezone": "Europe/Paris"
    }

    print("📅 Données de naissance de Nathan:")
    print(f"   - Date: {birth_data['year']}-{birth_data['month']:02d}-{birth_data['day']:02d}")
    print(f"   - Heure: {birth_data['hour']:02d}:{birth_data['minute']:02d}")
    print(f"   - Lieu: {birth_data['city']} ({birth_data['latitude']}, {birth_data['longitude']})")
    print(f"   - Timezone: {birth_data['timezone']}")
    print()

    # Calculer la position attendue avec Swiss Ephemeris
    # 11h30 en Europe/Paris le 9 février 2001 = 10h30 UTC (heure d'hiver)
    birth_datetime_utc = datetime(2001, 2, 9, 10, 30, 0, tzinfo=timezone.utc)
    expected_moon = get_moon_position(birth_datetime_utc)

    print(f"🌙 Position attendue (Swiss Ephemeris):")
    print(f"   - Signe: {expected_moon.sign}")
    print(f"   - Longitude: {expected_moon.longitude}°")
    print(f"   - Degré dans le signe: {expected_moon.degree}°")
    print()

    # Appeler RapidAPI
    print("🌐 Appel RapidAPI...")
    try:
        response = await call_rapidapi_natal_chart(birth_data)

        # Extraire les positions planétaires
        chart_data = response.get("chart_data", {})
        positions = chart_data.get("planetary_positions", [])

        # Chercher la Lune
        moon_position = None
        for pos in positions:
            if pos.get("name", "").lower() == "moon":
                moon_position = pos
                break

        if moon_position:
            print(f"🌙 Position retournée par RapidAPI:")
            print(f"   - Signe: {moon_position.get('sign')}")
            print(f"   - Degré: {moon_position.get('degree')}")
            print(f"   - Longitude absolue: {moon_position.get('absolute_longitude')}")
            print(f"   - Maison: {moon_position.get('house')}")
            print()

            # Mapper les abréviations
            sign_mapping = {
                'Vir': 'Virgo',
                'Leo': 'Leo',
                'Ari': 'Aries', 'Tau': 'Taurus', 'Gem': 'Gemini', 'Can': 'Cancer',
                'Lib': 'Libra', 'Sco': 'Scorpio',
                'Sag': 'Sagittarius', 'Cap': 'Capricorn', 'Aqu': 'Aquarius', 'Pis': 'Pisces'
            }

            rapidapi_sign = sign_mapping.get(moon_position.get('sign'), moon_position.get('sign'))

            # Comparer
            if rapidapi_sign == expected_moon.sign:
                print(f"✅ CORRECT: RapidAPI retourne bien {rapidapi_sign}")
            else:
                print(f"❌ ERREUR: RapidAPI retourne {rapidapi_sign}, attendu {expected_moon.sign}")
                print()
                print(f"💡 Analyse:")
                abs_long = moon_position.get('absolute_longitude')
                if abs_long:
                    # Déterminer le signe depuis la longitude
                    sign_index = int(abs_long / 30)
                    signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                            'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
                    calculated_sign = signs[sign_index] if sign_index < 12 else "Unknown"
                    print(f"   - Longitude absolue: {abs_long}°")
                    print(f"   - Signe calculé depuis longitude: {calculated_sign}")
        else:
            print("❌ Aucune position de Lune trouvée dans la réponse RapidAPI")

    except Exception as e:
        print(f"❌ Erreur lors de l'appel RapidAPI: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_nathan_rapidapi())
