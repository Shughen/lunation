#!/usr/bin/env python3
"""
Script de test pour vérifier la connexion à Supabase
"""
import asyncio
import asyncpg
from config import settings
from urllib.parse import urlparse

async def test_connection():
    """Test de connexion à Supabase"""
    print("🔍 Test de connexion à Supabase...")
    
    parsed = urlparse(settings.DATABASE_URL)
    print(f"Host: {parsed.hostname}")
    print(f"Port: {parsed.port}")
    print(f"User: {parsed.username}")
    print(f"Database: {parsed.path[1:]}")
    print(f"Password: {'***' if parsed.password else 'None'}")
    print()
    
    try:
        print("⏳ Tentative de connexion...")
        conn = await asyncio.wait_for(
            asyncpg.connect(
                host=parsed.hostname,
                port=parsed.port,
                user=parsed.username,
                password=parsed.password,
                database=parsed.path[1:] if parsed.path else 'postgres',
                ssl='require'
            ),
            timeout=10
        )
        print("✅ Connexion réussie !")
        
        # Test d'une requête simple
        version = await conn.fetchval('SELECT version()')
        print(f"✅ Version PostgreSQL: {version[:50]}...")
        
        await conn.close()
        print("✅ Connexion fermée proprement")
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {type(e).__name__}: {e}")
        
        if "nodename nor servname" in str(e) or "Name resolution" in str(e):
            print()
            print("🔍 DIAGNOSTIC:")
            print("   Le hostname n'est pas résolvable par DNS.")
            print("   Causes possibles:")
            print("   1. Le projet Supabase est en pause (plan gratuit)")
            print("   2. Vérifiez dans le dashboard Supabase si le projet est actif")
            print("   3. Essayez de 'réveiller' le projet en accédant au dashboard")
            print("   4. Vérifiez que le hostname est correct dans Settings > Database")
        elif "password authentication failed" in str(e).lower():
            print()
            print("🔍 DIAGNOSTIC:")
            print("   Le mot de passe est incorrect.")
            print("   Vérifiez le mot de passe dans le dashboard Supabase")
        elif "role" in str(e).lower() and "does not exist" in str(e).lower():
            print()
            print("🔍 DIAGNOSTIC:")
            print("   Le rôle utilisateur est incorrect.")
            print("   Pour Supabase, utilisez 'postgres' (pas 'user')")
        
        return False

if __name__ == "__main__":
    success = asyncio.run(test_connection())
    exit(0 if success else 1)

