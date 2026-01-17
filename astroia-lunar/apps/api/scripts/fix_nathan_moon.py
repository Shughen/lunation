"""
Script pour recalculer le thème natal de Nathan avec les bonnes données
Cela va écraser l'ancienne entrée en base de données
"""

import sys
import asyncio
import json
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.natal_reading_service import call_rapidapi_natal_chart, parse_positions_from_natal_chart
from services.swiss_ephemeris import get_moon_position
from datetime import datetime, timezone

async def recalculate_nathan_chart():
    """
    Recalcule le thème natal de Nathan
    """
    print("=" * 60)
    print("RECALCUL DU THÈME NATAL DE NATHAN")
    print("=" * 60)
    print()

    # Données de naissance de Nathan
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

    print("📅 Données de naissance:")
    print(f"   - Nom: Nathan")
    print(f"   - Date: 9 février 2001")
    print(f"   - Heure: 11:30 (heure locale)")
    print(f"   - Lieu: Bordeaux (44.8378, -0.5792)")
    print(f"   - Timezone: Europe/Paris")
    print()

    # Vérifier la position avec Swiss Ephemeris
    birth_datetime_utc = datetime(2001, 2, 9, 10, 30, 0, tzinfo=timezone.utc)
    expected_moon = get_moon_position(birth_datetime_utc)

    print(f"🌙 Position attendue (Swiss Ephemeris):")
    print(f"   - Signe: {expected_moon.sign}")
    print(f"   - Longitude: {expected_moon.longitude}°")
    print(f"   - Degré dans le signe: {expected_moon.degree}°")
    print()

    # Appeler RapidAPI pour calculer le thème
    print("🌐 Calcul du thème natal via RapidAPI...")
    try:
        response = await call_rapidapi_natal_chart(birth_data)

        # Parser les positions
        positions = parse_positions_from_natal_chart(response)

        # Chercher la Lune
        moon_pos = None
        for pos in positions:
            if pos.get('name', '').lower() == 'moon':
                moon_pos = pos
                break

        if moon_pos:
            print(f"✅ Thème natal calculé avec succès")
            print(f"   - Lune: {moon_pos.get('sign_fr')} ({moon_pos.get('sign')})")
            print(f"   - Degré: {moon_pos.get('degree')}°")
            print(f"   - Maison: {moon_pos.get('house')}")
            print()

            # Afficher toutes les positions pour vérification
            print("📊 Positions planétaires:")
            for pos in positions[:10]:  # Limiter aux 10 premières
                name = pos.get('name', 'Unknown')
                sign_fr = pos.get('sign_fr', '')
                degree = pos.get('degree', 0)
                house = pos.get('house', 0)
                print(f"   {pos.get('emoji', '⭐')} {name}: {sign_fr} {degree:.2f}° (Maison {house})")

            print()
            print("=" * 60)
            print("SOLUTION:")
            print("=" * 60)
            print()
            print("Pour corriger le thème natal de Nathan en base de données,")
            print("vous devez recalculer son thème via l'API:")
            print()
            print("POST /api/natal-chart")
            print("Body:")
            print(json.dumps({
                "date": "2001-02-09",
                "time": "11:30",
                "latitude": 44.8378,
                "longitude": -0.5792,
                "place_name": "Bordeaux",
                "timezone": "Europe/Paris"
            }, indent=2))
            print()
            print("Cela écrasera l'ancienne entrée en base avec les bonnes données.")
            print()
        else:
            print("❌ Aucune position de Lune trouvée dans la réponse")

    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(recalculate_nathan_chart())
