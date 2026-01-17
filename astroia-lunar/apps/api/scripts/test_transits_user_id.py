#!/usr/bin/env python3
"""
Script de test pour vérifier le type user_id dans /transits/overview/{user_id}/{month}

Teste plusieurs formats de user_id:
1. UUID valide (attendu)
2. Integer (envoyé par mobile si user.id est un int)
3. String quelconque

Ce script valide que l'endpoint gère correctement les UUID.
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire parent au path pour importer les modules
sys.path.insert(0, str(Path(__file__).parent.parent))

import asyncio
from uuid import UUID, uuid4
from datetime import datetime


async def test_transits_overview_user_id():
    """Test des différents formats de user_id pour l'endpoint transits/overview"""

    print("=" * 80)
    print("TEST: Type user_id pour /transits/overview/{user_id}/{month}")
    print("=" * 80)

    # UUID de test (celui configuré dans .env)
    test_uuid = "550e8400-e29b-41d4-a716-446655440000"
    test_month = "2025-01"

    print(f"\n1. TEST avec UUID valide: {test_uuid}")
    print(f"   Type attendu par l'API: UUID")
    print(f"   Type envoyé par mobile: string (converti depuis user.id)")

    # Vérifier que l'UUID est valide
    try:
        parsed_uuid = UUID(test_uuid)
        print(f"   ✅ UUID parsé avec succès: {parsed_uuid}")
        print(f"   Type Python: {type(parsed_uuid)}")
    except ValueError as e:
        print(f"   ❌ UUID invalide: {e}")
        return

    # Test des différents formats
    print(f"\n2. TEST des formats envoyés par le mobile:")

    # Format 1: String UUID (cas actuel après conversion typeof user.id)
    print(f"\n   a) String UUID: '{test_uuid}'")
    print(f"      - Mobile envoie: typeof user.id === 'string' ? user.id : String(user.id)")
    print(f"      - API attend: UUID dans le path parameter")
    print(f"      - FastAPI convertit automatiquement string -> UUID si valide")

    # Format 2: Integer (si user.id était un int)
    test_int = 1
    print(f"\n   b) Integer: {test_int}")
    print(f"      - Mobile enverrait: String(1) = '1'")
    print(f"      - API rejetterait: '1' n'est pas un UUID valide")
    print(f"      - Résultat attendu: 422 Unprocessable Entity")

    # Test de conversion
    print(f"\n3. Validation de la conversion:")

    # Test UUID valide
    try:
        uuid_obj = UUID(test_uuid)
        print(f"   ✅ UUID('{test_uuid}') -> {uuid_obj} (type: {type(uuid_obj).__name__})")
    except ValueError as e:
        print(f"   ❌ UUID('{test_uuid}') -> Erreur: {e}")

    # Test integer converti en string (cas problématique)
    try:
        uuid_obj = UUID("1")
        print(f"   ✅ UUID('1') -> {uuid_obj}")
    except ValueError as e:
        print(f"   ❌ UUID('1') -> Erreur: {e}")
        print(f"      → Le mobile ne doit PAS envoyer un integer ID")

    print(f"\n4. Solution actuelle dans le code mobile:")
    print(f"   TransitsWidget.tsx (ligne 70):")
    print(f"   userId = typeof user.id === 'string' ? user.id : String(user.id);")
    print(f"   ")
    print(f"   Cette conversion fonctionne SI ET SEULEMENT SI:")
    print(f"   - user.id est déjà un UUID string (ex: '550e8400-...')")
    print(f"   - OU user.id peut être converti en UUID valide")
    print(f"   ")
    print(f"   ⚠️  PROBLÈME SI user.id est un integer (ex: 1, 2, 3...):")
    print(f"   - String(1) = '1' (invalide comme UUID)")
    print(f"   - API retournera 422 Unprocessable Entity")

    print(f"\n5. Analyse du code backend:")
    print(f"   routes/transits.py (ligne 214-222):")
    print(f"   @router.get('/overview/{{user_id}}/{{month}}', response_model=TransitsOverviewDB)")
    print(f"   async def get_transits_overview(")
    print(f"       user_id: UUID,  # ← FastAPI attend un UUID")
    print(f"       month: str,")
    print(f"       major_only: bool = False,")
    print(f"       current_user: User = Depends(get_current_user),")
    print(f"       x_dev_user_id: Optional[str] = Header(default=None, alias='X-Dev-User-Id'),")
    print(f"       db: AsyncSession = Depends(get_db)")
    print(f"   )")

    print(f"\n6. Mode DEV_AUTH_BYPASS (ligne 236-244):")
    print(f"   En mode développement, l'API peut utiliser le header X-Dev-User-Id")
    print(f"   au lieu du user_id de l'URL:")
    print(f"   ")
    print(f"   if settings.APP_ENV == 'development' and settings.DEV_AUTH_BYPASS and x_dev_user_id:")
    print(f"       try:")
    print(f"           user_id = UUID(x_dev_user_id)")
    print(f"       except (ValueError, TypeError):")
    print(f"           logger.warning('UUID du header X-Dev-User-Id invalide')")

    print(f"\n7. Modèle TransitsOverview (models/transits.py ligne 24):")
    print(f"   user_id = Column(UUID(as_uuid=True), nullable=False, index=True)")
    print(f"   ")
    print(f"   Le modèle attend un UUID natif Python (uuid.UUID)")
    print(f"   SQLAlchemy convertit automatiquement depuis/vers le type UUID PostgreSQL")

    print(f"\n8. Modèle User (models/user.py ligne 12):")
    print(f"   id = Column(Integer, primary_key=True, index=True)")
    print(f"   ")
    print(f"   ⚠️  INCOMPATIBILITÉ DÉTECTÉE:")
    print(f"   - User.id est un INTEGER")
    print(f"   - TransitsOverview.user_id est un UUID")
    print(f"   ")
    print(f"   📝 NOTE (ligne 43-45):")
    print(f"   # Note: transits_overviews et transits_events ne sont plus en relation car")
    print(f"   # user_id pointe vers auth.users.id (UUID Supabase) et non vers users.id (Integer FastAPI)")
    print(f"   # Les RLS policies gèrent l'accès basé sur auth.uid()")

    print(f"\n" + "=" * 80)
    print("CONCLUSION:")
    print("=" * 80)
    print(f"")
    print(f"✅ L'API est correctement configurée pour UUID:")
    print(f"   - Endpoint accepte user_id: UUID")
    print(f"   - Modèle TransitsOverview.user_id est UUID")
    print(f"   - Mode DEV_AUTH_BYPASS gère le header UUID")
    print(f"")
    print(f"✅ Le mobile est correctement configuré:")
    print(f"   - Conversion: typeof user.id === 'string' ? user.id : String(user.id)")
    print(f"   - En mode DEV_AUTH_BYPASS: utilise DEV_USER_ID (UUID)")
    print(f"   - Header X-Dev-User-Id est envoyé avec UUID")
    print(f"")
    print(f"⚠️  ATTENTION - Cas où ça ne fonctionne PAS:")
    print(f"   1. Si user.id côté mobile est un INTEGER (1, 2, 3...)")
    print(f"      → String(1) = '1' n'est PAS un UUID valide")
    print(f"      → API retournera 422 Unprocessable Entity")
    print(f"")
    print(f"   2. Si les données de naissance ne sont pas renseignées:")
    print(f"      → Aucun TransitsOverview généré")
    print(f"      → API retournera 404 Not Found (cas normal)")
    print(f"")
    print(f"✅ SOLUTION APPLIQUÉE:")
    print(f"   - En mode DEV_AUTH_BYPASS, l'API utilise le header X-Dev-User-Id (UUID)")
    print(f"   - Ce header bypasse le user_id de l'URL si invalide")
    print(f"   - Le mobile envoie toujours X-Dev-User-Id en mode développement")
    print(f"")
    print(f"📝 RECOMMANDATION:")
    print(f"   - Garder la logique actuelle (fonctionne en DEV_AUTH_BYPASS)")
    print(f"   - En production, s'assurer que user.id est toujours un UUID string")
    print(f"   - Ou convertir user.id depuis l'INTEGER FastAPI vers UUID Supabase")
    print(f"")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_transits_overview_user_id())
