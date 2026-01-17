"""
Simule exactement ce que le mobile reçoit en appelant l'API
"""

import sys
import asyncio
import json
import httpx
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from config import settings

async def test_api_response():
    """
    Simule un appel API complet comme le mobile le ferait
    """
    print("=" * 80)
    print("TEST - RÉPONSE API COMPLÈTE (Simulation Mobile)")
    print("=" * 80)
    print()

    # URL de l'API
    api_url = "http://localhost:8000/api/natal-chart"

    # Payload
    payload = {
        "date": "2001-02-09",
        "time": "11:30",
        "latitude": 44.8378,
        "longitude": -0.5792,
        "place_name": "Bordeaux",
        "timezone": "Europe/Paris"
    }

    print("Payload envoyé:")
    print(json.dumps(payload, indent=2))
    print()

    try:
        print("🌐 Appel POST /api/natal-chart...")
        print()

        # Note: Normalement il faudrait un token d'authentification
        # Pour ce test, on va juste montrer ce qui devrait être retourné

        print("⚠️ Note: Ce script nécessite que l'API soit lancée")
        print("   et qu'un utilisateur soit authentifié.")
        print()
        print("Pour tester manuellement:")
        print()
        print("curl -X POST http://localhost:8000/api/natal-chart \\")
        print("  -H 'Content-Type: application/json' \\")
        print("  -H 'Authorization: Bearer YOUR_TOKEN' \\")
        print("  -d '{")
        print('    "date": "2001-02-09",')
        print('    "time": "11:30",')
        print('    "latitude": 44.8378,')
        print('    "longitude": -0.5792,')
        print('    "place_name": "Bordeaux",')
        print('    "timezone": "Europe/Paris"')
        print("  }'")
        print()

        # Simulation de la réponse attendue
        print("=" * 80)
        print("RÉPONSE ATTENDUE:")
        print("=" * 80)
        print()

        expected_response = {
            "id": "uuid-here",
            "sun_sign": "Aquarius",
            "moon_sign": "Virgo",  # ← DEVRAIT ÊTRE VIRGO
            "ascendant": "Taurus",
            "planets": {
                "sun": {"sign": "Aquarius", "degree": 20.74, "house": 11},
                "moon": {"sign": "Virgo", "degree": 6.9, "house": 5},  # ← VIRGO ICI
                # ... autres planètes
            },
            "houses": {
                # ... maisons
            },
            "aspects": [
                # ... aspects
            ]
        }

        print("Structure JSON attendue:")
        print(json.dumps(expected_response, indent=2))
        print()

        print("=" * 80)
        print("VÉRIFICATIONS À FAIRE:")
        print("=" * 80)
        print()
        print("1. ✅ Vérifier que moon_sign = 'Virgo' (pas 'Leo')")
        print("2. ✅ Vérifier que planets.moon.sign = 'Virgo'")
        print("3. ✅ Vérifier que planets.moon.degree = 6.9 (pas 126.9 ou autre)")
        print()
        print("Si vous voyez 'Leo' au lieu de 'Virgo':")
        print()
        print("  a) Vérifier dans la base de données:")
        print("     SELECT positions->'moon', positions->'planets'->'moon'")
        print("     FROM natal_charts WHERE birth_date = '2001-02-09';")
        print()
        print("  b) Vérifier les logs de l'API lors du POST:")
        print("     Chercher '[Parser]' et vérifier le signe retourné")
        print()
        print("  c) Vérifier le cache du mobile:")
        print("     Supprimer l'app et réinstaller pour vider le cache")
        print()

    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    asyncio.run(test_api_response())
