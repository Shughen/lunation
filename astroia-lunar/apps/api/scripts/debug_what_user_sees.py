"""
Script de débogage final : qu'est-ce que l'utilisateur voit vraiment?
"""

import sys
import asyncio
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.natal_reading_service import call_rapidapi_natal_chart, parse_positions_from_natal_chart

async def debug_user_view():
    """
    Simule exactement ce que l'utilisateur devrait voir
    """
    print("=" * 80)
    print("DÉBOGAGE - CE QUE L'UTILISATEUR DEVRAIT VOIR")
    print("=" * 80)
    print()

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

    print("1️⃣  APPEL RAPIDAPI")
    print("-" * 80)
    response = await call_rapidapi_natal_chart(birth_data)

    # Extraire la Lune de la réponse brute
    chart_data = response.get("chart_data", {})
    positions = chart_data.get("planetary_positions", [])

    moon_raw = next((p for p in positions if p.get("name", "").lower() == "moon"), None)

    print(f"✅ RapidAPI retourne:")
    print(f"   sign: {moon_raw.get('sign')}")
    print(f"   degree: {moon_raw.get('degree')}")
    print(f"   absolute_longitude: {moon_raw.get('absolute_longitude')}")
    print()

    print("2️⃣  APRÈS PARSING")
    print("-" * 80)
    parsed_positions = parse_positions_from_natal_chart(response)
    moon_parsed = next((p for p in parsed_positions if p.get("name", "").lower() == "moon"), None)

    print(f"✅ Position parsée:")
    print(f"   sign: {moon_parsed.get('sign')}")
    print(f"   sign_fr: {moon_parsed.get('sign_fr')}")
    print(f"   degree: {moon_parsed.get('degree')}")
    print()

    print("3️⃣  APRÈS MAPPING (routes/natal.py)")
    print("-" * 80)

    sign_mapping = {
        "Ari": "Aries", "Tau": "Taurus", "Gem": "Gemini", "Can": "Cancer",
        "Leo": "Leo", "Vir": "Virgo", "Lib": "Libra", "Sco": "Scorpio",
        "Sag": "Sagittarius", "Cap": "Capricorn", "Aqu": "Aquarius", "Pis": "Pisces"
    }

    sign_abbr = moon_parsed.get('sign')
    sign_full = sign_mapping.get(sign_abbr, sign_abbr)

    print(f"✅ Signe mappé:")
    print(f"   {sign_abbr} → {sign_full}")
    print()

    print("4️⃣  CE QUI EST SAUVEGARDÉ EN BASE")
    print("-" * 80)

    # Simuler la structure JSONB positions
    positions_jsonb = {
        "moon": {
            "sign": sign_full,
            "degree": moon_parsed.get('degree'),
            "house": moon_parsed.get('house')
        },
        "planets": {
            "moon": {
                "sign": sign_full,
                "degree": moon_parsed.get('degree'),
                "house": moon_parsed.get('house')
            }
        }
    }

    print(f"✅ Structure JSONB positions:")
    print(json.dumps(positions_jsonb, indent=2))
    print()

    print("5️⃣  CE QUI EST RETOURNÉ PAR GET /api/natal-chart")
    print("-" * 80)

    # Simuler la réponse de l'API
    api_response = {
        "id": "uuid-here",
        "moon_sign": sign_full,  # Extrait de positions.moon.sign
        "planets": {
            "moon": {
                "sign": sign_full,
                "degree": moon_parsed.get('degree'),
                "house": moon_parsed.get('house')
            }
        }
    }

    print(f"✅ Réponse API:")
    print(json.dumps(api_response, indent=2))
    print()

    print("6️⃣  CE QUE LE MOBILE AFFICHE")
    print("-" * 80)
    print()
    print("Le mobile devrait afficher:")
    print(f"   Lune en {sign_full} ({moon_parsed.get('degree')}°)")
    print()

    print("=" * 80)
    print("SI VOUS VOYEZ 'LEO' AU LIEU DE 'VIRGO'")
    print("=" * 80)
    print()
    print("Causes possibles:")
    print()
    print("1. Cache du mobile:")
    print("   → Désinstaller l'app et réinstaller")
    print("   → OU vider le cache dans les paramètres de l'app")
    print()
    print("2. Mauvaise entrée en base:")
    print("   → Vérifier avec: SELECT positions->'moon' FROM natal_charts")
    print("                    WHERE birth_date = '2001-02-09';")
    print()
    print("3. Utilisateur différent:")
    print("   → Vérifier que vous êtes connecté avec le bon compte")
    print("   → Vérifier user_id dans natal_charts")
    print()
    print("4. Bug dans le mobile:")
    print("   → Vérifier le code de mapping des signes dans le mobile")
    print("   → Chercher si le mobile ne convertit pas 'Virgo' en 'Leo' par erreur")
    print()
    print("5. Ancienne migration de données:")
    print("   → Chercher s'il n'y a pas plusieurs entrées pour le même utilisateur")
    print("   → DELETE FROM natal_charts WHERE user_id = X AND id != (dernier_id);")
    print()

if __name__ == "__main__":
    asyncio.run(debug_user_view())
