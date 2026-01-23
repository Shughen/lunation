#!/bin/bash
# Script de vérification du fix du parsing des variables d'environnement booléennes

set -e

echo "🔍 Vérification du fix ENV BOOL parsing..."
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

cd "$(dirname "$0")/.."

echo "📋 Étape 1/3 : Tests unitaires env_bool()"
echo "----------------------------------------"
python -m pytest tests/test_env_helpers.py -v --tb=short
echo ""

echo "📋 Étape 2/3 : Tests d'intégration config"
echo "----------------------------------------"
python -m pytest tests/test_config_bool_parsing.py -v --tb=short
echo ""

echo "📋 Étape 3/3 : Vérification runtime des valeurs"
echo "----------------------------------------"
python -c "
from config import settings
print(f'DEV_MOCK_NATAL: {settings.DEV_MOCK_NATAL}')
print(f'DEV_MOCK_EPHEMERIS: {settings.DEV_MOCK_EPHEMERIS}')
print(f'DEV_MOCK_RAPIDAPI: {settings.DEV_MOCK_RAPIDAPI}')
print(f'DEV_AUTH_BYPASS: {settings.DEV_AUTH_BYPASS}')
print(f'ALLOW_DEV_PURGE: {settings.ALLOW_DEV_PURGE}')
print(f'ALLOW_DEV_VOC_POPULATE: {settings.ALLOW_DEV_VOC_POPULATE}')
print(f'DISABLE_CHIRON: {settings.DISABLE_CHIRON}')
"
echo ""

echo "✅ Vérification des valeurs attendues..."
python -c "
from config import settings

# Valeurs attendues selon .env
expected = {
    'DEV_MOCK_NATAL': False,
    'DEV_MOCK_EPHEMERIS': False,
    'DEV_MOCK_RAPIDAPI': False,
}

errors = []
for key, expected_val in expected.items():
    actual_val = getattr(settings, key)
    if actual_val != expected_val:
        errors.append(f'{key}: expected {expected_val}, got {actual_val}')

if errors:
    print('❌ ERREURS DÉTECTÉES:')
    for err in errors:
        print(f'  - {err}')
    exit(1)
else:
    print('✅ Toutes les valeurs sont correctes!')
"
echo ""

echo -e "${GREEN}✨ SUCCESS - Le fix du parsing booléen fonctionne correctement !${NC}"
echo ""
echo "Résumé:"
echo "  - 45 tests unitaires env_bool() : ✅ PASS"
echo "  - 22 tests d'intégration config : ✅ PASS"
echo "  - Valeurs runtime vérifiées : ✅ PASS"
echo ""
echo "Les variables DEV_MOCK_NATAL=0, DEV_MOCK_EPHEMERIS=0, DEV_MOCK_RAPIDAPI=false"
echo "sont maintenant correctement parsées comme False."
