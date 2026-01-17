"""
Traçage complet du flux de données pour Nathan
De RapidAPI jusqu'à la réponse finale
"""

import sys
import asyncio
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.natal_reading_service import call_rapidapi_natal_chart, parse_positions_from_natal_chart

async def trace_full_flow():
    """
    Trace complète du flux de données
    """
    print("=" * 80)
    print("TRAÇAGE COMPLET - FLUX DE DONNÉES POUR NATHAN")
    print("=" * 80)
    print()

    # Données de naissance
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

    # ÉTAPE 1: Appel RapidAPI
    print("ÉTAPE 1: APPEL RAPIDAPI")
    print("-" * 80)
    response = await call_rapidapi_natal_chart(birth_data)

    # Extraire chart_data
    chart_data = response.get("chart_data", {})
    positions = chart_data.get("planetary_positions", [])

    # Trouver la Lune dans la réponse brute
    moon_raw = None
    for pos in positions:
        if pos.get("name", "").lower() == "moon":
            moon_raw = pos
            break

    print("Réponse brute RapidAPI (Lune):")
    print(json.dumps(moon_raw, indent=2))
    print()

    # ÉTAPE 2: Parsing avec parse_positions_from_natal_chart
    print("ÉTAPE 2: PARSING (parse_positions_from_natal_chart)")
    print("-" * 80)
    parsed_positions = parse_positions_from_natal_chart(response)

    moon_parsed = None
    for pos in parsed_positions:
        if pos.get("name", "").lower() == "moon":
            moon_parsed = pos
            break

    print("Position parsée (Lune):")
    print(json.dumps(moon_parsed, indent=2))
    print()

    # ÉTAPE 3: Simulation du mapping dans routes/natal.py
    print("ÉTAPE 3: MAPPING SIGNES (routes/natal.py)")
    print("-" * 80)

    sign_mapping = {
        "Ari": "Aries", "Tau": "Taurus", "Gem": "Gemini", "Can": "Cancer",
        "Leo": "Leo", "Vir": "Virgo", "Lib": "Libra", "Sco": "Scorpio",
        "Sag": "Sagittarius", "Cap": "Capricorn", "Aqu": "Aquarius", "Pis": "Pisces"
    }

    def map_sign(sign_abbr: str) -> str:
        """Convertit un signe abrégé en nom complet"""
        if not sign_abbr:
            return ""
        # Si déjà en format complet, retourner tel quel
        if sign_abbr in sign_mapping.values():
            return sign_abbr
        # Sinon mapper depuis l'abréviation
        return sign_mapping.get(sign_abbr, sign_abbr)

    # Simuler la transformation dans le code
    sign_abbr = moon_raw.get("sign", "") if moon_raw else ""
    sign_full = map_sign(sign_abbr)

    print(f"Signe abrégé (RapidAPI): {sign_abbr}")
    print(f"Signe complet (mappé): {sign_full}")
    print()

    # ÉTAPE 4: Construction du dict planets
    print("ÉTAPE 4: CONSTRUCTION DICT PLANETS (routes/natal.py)")
    print("-" * 80)

    planets_dict = {}
    for pos in parsed_positions:
        name = pos.get("name", "").lower()
        sign_abbr = pos.get("sign", "")
        sign_full = map_sign(sign_abbr)

        if name == "moon":
            moon_data = {
                "sign": sign_full,
                "degree": pos.get("degree", 0.0),
                "house": pos.get("house", 0)
            }
            planets_dict["moon"] = moon_data
            print("Moon dans planets_dict:")
            print(json.dumps(moon_data, indent=2))
            break

    print()

    # ÉTAPE 5: Construction positions JSONB
    print("ÉTAPE 5: CONSTRUCTION POSITIONS JSONB")
    print("-" * 80)

    # Simuler ce qui est sauvegardé en base
    positions_jsonb = {
        "moon": moon_data if 'moon_data' in locals() else {},
        "planets": planets_dict
    }

    print("Structure positions JSONB (Lune):")
    print(json.dumps(positions_jsonb, indent=2))
    print()

    # VÉRIFICATION FINALE
    print("=" * 80)
    print("VÉRIFICATION FINALE")
    print("=" * 80)
    print()

    # Vérifier chaque étape
    checks = [
        ("RapidAPI brut", moon_raw.get("sign") if moon_raw else None, "Vir"),
        ("Après parsing", moon_parsed.get("sign") if moon_parsed else None, "Vir"),
        ("Après mapping", sign_full if 'sign_full' in locals() else None, "Virgo"),
        ("Dans planets_dict", planets_dict.get("moon", {}).get("sign"), "Virgo"),
    ]

    all_correct = True
    for step, actual, expected in checks:
        status = "✅" if actual == expected else "❌"
        print(f"{status} {step:20s}: {actual:10s} (attendu: {expected})")
        if actual != expected:
            all_correct = False

    print()
    if all_correct:
        print("✅ TOUTES LES ÉTAPES SONT CORRECTES")
        print()
        print("⚠️ Le problème doit être ailleurs:")
        print("   - Vérifier l'extraction depuis la base (extract_big3_from_positions)")
        print("   - Vérifier l'affichage dans le mobile")
        print("   - Vérifier qu'il n'y a pas plusieurs entrées en base")
    else:
        print("❌ PROBLÈME DÉTECTÉ dans une des étapes ci-dessus")

    # ÉTAPE 6: Test extraction depuis positions (comme dans get_natal_chart)
    print()
    print("ÉTAPE 6: EXTRACTION DEPUIS POSITIONS (extract_big3_from_positions)")
    print("-" * 80)

    from utils.natal_chart_helpers import extract_big3_from_positions

    big3 = extract_big3_from_positions(positions_jsonb)
    print("Big3 extrait:")
    print(json.dumps(big3, indent=2))
    print()

    if big3["moon_sign"] == "Virgo":
        print("✅ Big3 extraction correcte")
    else:
        print(f"❌ Big3 extraction incorrecte: {big3['moon_sign']} au lieu de Virgo")

if __name__ == "__main__":
    asyncio.run(trace_full_flow())
