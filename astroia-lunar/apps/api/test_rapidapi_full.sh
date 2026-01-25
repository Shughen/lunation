#!/bin/bash
# Test complet RapidAPI pour thème natal
# Usage: ./test_rapidapi_full.sh

set -e

echo "🧪 TEST RAPIDAPI - Thème Natal (1er nov 1989, Manaus)"
echo "=================================================="
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Vérifier que l'API tourne
echo "1️⃣  Vérification API..."
if curl -s http://localhost:8000/health | grep -q "healthy"; then
    echo -e "${GREEN}✅ API accessible${NC}"
else
    echo -e "${RED}❌ API non accessible - Redémarrez l'API${NC}"
    exit 1
fi

# 2. Vérifier que DEV_MOCK_NATAL est désactivé
echo ""
echo "2️⃣  Vérification configuration..."
if grep -q "DEV_MOCK_NATAL=false" ../../.env; then
    echo -e "${GREEN}✅ DEV_MOCK_NATAL=false${NC}"
else
    echo -e "${RED}❌ DEV_MOCK_NATAL devrait être false${NC}"
    echo "Correction..."
    sed -i '' 's/DEV_MOCK_NATAL=true/DEV_MOCK_NATAL=false/' ../../.env
    echo -e "${YELLOW}⚠️  Redémarrez l'API pour appliquer les changements${NC}"
    exit 1
fi

# 3. Tester avec un nouvel utilisateur (user_id=99) pour éviter cache
echo ""
echo "3️⃣  Test calcul thème natal via RapidAPI..."
echo "Date: 1989-11-01, Heure: 13:20, Lieu: Manaus, Brésil"
echo ""

RESPONSE=$(curl -s -X POST http://localhost:8000/api/natal-chart \
  -H "Content-Type: application/json" \
  -H "X-Dev-User-Id: 99" \
  -d '{
    "date": "1989-11-01",
    "time": "13:20",
    "place_name": "Manaus",
    "latitude": -3.131633,
    "longitude": -59.982504,
    "timezone": "America/Manaus"
  }')

# Vérifier si erreur
if echo "$RESPONSE" | grep -q "detail"; then
    echo -e "${RED}❌ Erreur API:${NC}"
    echo "$RESPONSE" | python3 -m json.tool
    exit 1
fi

# Extraire les infos clés
SUN_SIGN=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin).get('sun_sign', 'N/A'))")
MOON_SIGN=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin).get('moon_sign', 'N/A'))")
ASCENDANT=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin).get('ascendant', 'N/A'))")

echo "Résultats:"
echo "----------"
echo "☀️  Signe solaire : $SUN_SIGN"
echo "🌙 Signe lunaire  : $MOON_SIGN"
echo "⬆️  Ascendant     : $ASCENDANT"
echo ""

# Vérifier signe solaire
if [ "$SUN_SIGN" = "Scorpio" ]; then
    echo -e "${GREEN}✅ Signe solaire correct (Scorpio)${NC}"
else
    echo -e "${RED}❌ Signe solaire incorrect (attendu: Scorpio, reçu: $SUN_SIGN)${NC}"
fi

# Vérifier que l'ascendant n'est pas aléatoire (si Gemini c'est encore le cache)
if [ "$ASCENDANT" = "Gemini" ]; then
    echo -e "${YELLOW}⚠️  Ascendant = Gemini (possible cache/MOCK)${NC}"
else
    echo -e "${GREEN}✅ Ascendant calculé par RapidAPI${NC}"
fi

echo ""
echo "4️⃣  Données complètes:"
echo "$RESPONSE" | python3 -m json.tool | head -50

echo ""
echo -e "${GREEN}✅ Test terminé${NC}"
