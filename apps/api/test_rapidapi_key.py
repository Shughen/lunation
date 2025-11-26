"""
Script de test pour vérifier que la clé RapidAPI fonctionne correctement
"""
import asyncio
import httpx
import os
from dotenv import load_dotenv
from config import settings

async def test_rapidapi_key():
    """Teste la clé RapidAPI avec un appel simple"""
    print("🔍 Test de la clé RapidAPI...")
    print(f"📋 Host: {settings.RAPIDAPI_HOST}")
    print(f"📋 Key (premiers 20 caractères): {settings.RAPIDAPI_KEY[:20]}...")
    print(f"📋 Key complète présente: {'Oui' if settings.RAPIDAPI_KEY and len(settings.RAPIDAPI_KEY) > 20 else 'Non'}")
    print()
    
    # Payload de test simple (date de naissance valide)
    test_payload = {
        "subject": {
            "name": "Test User",
            "birth_data": {
                "year": 1990,
                "month": 1,
                "day": 15,
                "hour": 12,
                "minute": 0,
                "second": 0,
                "city": "Paris",
                "country_code": "FR",
                "latitude": 48.8566,
                "longitude": 2.3522,
                "timezone": "Europe/Paris"
            }
        },
        "options": {
            "house_system": "placidus",
            "orb_system": "standard"
        }
    }
    
    url = f"{settings.BASE_RAPID_URL}/api/v3/charts/natal"
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": settings.RAPIDAPI_HOST,
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
    }
    
    print(f"🌐 URL: {url}")
    print(f"📤 Headers (x-rapidapi-key): {headers['x-rapidapi-key'][:20]}...")
    print()
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            print("⏳ Envoi de la requête de test...")
            response = await client.post(url, json=test_payload, headers=headers)
            
            print(f"📊 Status Code: {response.status_code}")
            print(f"📋 Headers de réponse:")
            for key, value in response.headers.items():
                if 'rapidapi' in key.lower() or 'x-' in key.lower():
                    print(f"   {key}: {value}")
            print()
            
            if response.status_code == 200:
                print("✅ SUCCÈS ! La clé RapidAPI fonctionne correctement")
                data = response.json()
                print(f"📊 Réponse reçue: {len(str(data))} caractères")
                if 'chart_data' in data:
                    print(f"✅ Structure chart_data trouvée")
                return True
            elif response.status_code == 403:
                print("❌ ERREUR 403 - Clé API refusée")
                try:
                    error_data = response.json()
                    print(f"📋 Message d'erreur: {error_data}")
                except:
                    print(f"📋 Réponse (texte): {response.text[:200]}")
                
                print()
                print("🔧 DIAGNOSTIC:")
                print("   1. Vérifiez que la clé API est correcte dans le .env")
                print("   2. Vérifiez que vous êtes bien abonné au plan BASIC sur RapidAPI")
                print("   3. Vérifiez que l'endpoint /api/v3/charts/natal est disponible dans votre plan")
                print("   4. Testez la clé directement sur RapidAPI Playground:")
                print(f"      https://rapidapi.com/procoders-development-procoders-development-default/api/best-astrology-api-natal-charts-transits-synastry/playground")
                return False
            elif response.status_code == 429:
                print("⚠️ ERREUR 429 - Trop de requêtes (rate limit)")
                print("   Attendez quelques minutes et réessayez")
                return False
            elif response.status_code == 401:
                print("❌ ERREUR 401 - Clé API invalide")
                print("   La clé API dans votre .env est probablement incorrecte")
                return False
            else:
                print(f"❌ ERREUR {response.status_code}")
                try:
                    error_data = response.json()
                    print(f"📋 Détails: {error_data}")
                except:
                    print(f"📋 Réponse (texte): {response.text[:500]}")
                return False
                
    except Exception as e:
        print(f"❌ Erreur lors du test: {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    # Charger les variables d'environnement
    load_dotenv()
    asyncio.run(test_rapidapi_key())
