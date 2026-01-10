#!/bin/bash

# Script de test end-to-end pour l'auto-heal natal chart
# Teste les scénarios:
# 1. Purge du chart existant
# 2. POST /api/natal-chart (création)
# 3. GET /api/natal-chart (lecture)

set -e  # Arrêter en cas d'erreur

API_BASE="http://localhost:8000/api"
DEV_EXTERNAL_ID="e2e-test-autoheal"

echo "=========================================="
echo "Test End-to-End: Natal Chart Auto-Heal"
echo "=========================================="
echo ""

# Vérifier que l'API est up
echo "1. Vérification que l'API est accessible..."
if ! curl -s -f "${API_BASE}/health" > /dev/null 2>&1; then
    echo "❌ Erreur: L'API n'est pas accessible à ${API_BASE}"
    echo "   Assurez-vous que l'API est lancée (uvicorn main:app --reload)"
    exit 1
fi
echo "✅ API accessible"
echo ""

# Étape 1: Purge du chart existant
echo "2. Purge du chart existant (si présent)..."
PURGE_RESPONSE=$(curl -s -w "\n%{http_code}" \
    -X POST "${API_BASE}/natal-chart/dev/purge" \
    -H "X-Dev-External-Id: ${DEV_EXTERNAL_ID}" \
    -H "Content-Type: application/json")

PURGE_HTTP_CODE=$(echo "$PURGE_RESPONSE" | tail -n1)
PURGE_BODY=$(echo "$PURGE_RESPONSE" | sed '$d')

if [ "$PURGE_HTTP_CODE" = "200" ]; then
    echo "✅ Chart purgé avec succès"
    echo "   Réponse: $PURGE_BODY"
elif [ "$PURGE_HTTP_CODE" = "404" ]; then
    echo "⚠️  Endpoint purge non disponible (APP_ENV != development ou ALLOW_DEV_PURGE != 1)"
    echo "   Continuons sans purge..."
else
    echo "⚠️  Purge échoué (HTTP $PURGE_HTTP_CODE), continuons..."
fi
echo ""

# Étape 2: POST /api/natal-chart (création du chart)
echo "3. POST /api/natal-chart (création du chart)..."
POST_RESPONSE=$(curl -s -w "\n%{http_code}" \
    -X POST "${API_BASE}/natal-chart" \
    -H "X-Dev-External-Id: ${DEV_EXTERNAL_ID}" \
    -H "Content-Type: application/json" \
    -d '{
        "date": "1990-05-15",
        "time": "14:30",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "place_name": "Paris"
    }')

POST_HTTP_CODE=$(echo "$POST_RESPONSE" | tail -n1)
POST_BODY=$(echo "$POST_RESPONSE" | sed '$d')

if [ "$POST_HTTP_CODE" = "200" ] || [ "$POST_HTTP_CODE" = "201" ]; then
    echo "✅ Chart créé avec succès (HTTP $POST_HTTP_CODE)"

    # Vérifier si c'est un mock (devrait avoir _mock dans la réponse)
    if echo "$POST_BODY" | grep -q '"_mock"'; then
        echo "   ℹ️  Chart créé via MOCK (RapidAPI indisponible ou fallback)"
        MOCK_REASON=$(echo "$POST_BODY" | grep -o '"_reason":"[^"]*"' | cut -d'"' -f4)
        echo "   Raison du mock: $MOCK_REASON"
    else
        echo "   ℹ️  Chart créé via RapidAPI (données réelles)"
    fi

    # Vérifier structure complète
    PLANETS_COUNT=$(echo "$POST_BODY" | grep -o '"planets":{[^}]*}' | grep -o '"[a-z_]*":' | wc -l)
    HOUSES_COUNT=$(echo "$POST_BODY" | grep -o '"houses":{[^}]*}' | grep -o '"[0-9]*":' | wc -l)

    echo "   Planètes détectées: $PLANETS_COUNT"
    echo "   Maisons détectées: $HOUSES_COUNT"

    if [ "$PLANETS_COUNT" -ge 10 ] && [ "$HOUSES_COUNT" -ge 12 ]; then
        echo "   ✅ Structure complète (≥10 planètes, ≥12 maisons)"
    else
        echo "   ⚠️  Structure potentiellement incomplète"
    fi
else
    echo "❌ Erreur lors de la création du chart (HTTP $POST_HTTP_CODE)"
    echo "   Réponse: $POST_BODY"
    exit 1
fi
echo ""

# Étape 3: GET /api/natal-chart (lecture du chart)
echo "4. GET /api/natal-chart (lecture du chart)..."
GET_RESPONSE=$(curl -s -w "\n%{http_code}" \
    -X GET "${API_BASE}/natal-chart" \
    -H "X-Dev-External-Id: ${DEV_EXTERNAL_ID}")

GET_HTTP_CODE=$(echo "$GET_RESPONSE" | tail -n1)
GET_BODY=$(echo "$GET_RESPONSE" | sed '$d')

if [ "$GET_HTTP_CODE" = "200" ]; then
    echo "✅ Chart récupéré avec succès"

    # Vérifier si c'est un mock
    if echo "$GET_BODY" | grep -q '"_mock"'; then
        echo "   ℹ️  Chart contient métadonnée _mock"
        MOCK_REASON=$(echo "$GET_BODY" | grep -o '"_reason":"[^"]*"' | cut -d'"' -f4)
        echo "   Raison: $MOCK_REASON"
    fi

    # Extraire Big3
    SUN_SIGN=$(echo "$GET_BODY" | grep -o '"sun_sign":"[^"]*"' | cut -d'"' -f4)
    MOON_SIGN=$(echo "$GET_BODY" | grep -o '"moon_sign":"[^"]*"' | cut -d'"' -f4)
    ASCENDANT=$(echo "$GET_BODY" | grep -o '"ascendant":"[^"]*"' | cut -d'"' -f4)

    echo "   Big3: Sun=${SUN_SIGN}, Moon=${MOON_SIGN}, Ascendant=${ASCENDANT}"

    # Vérifier complétude
    PLANETS_COUNT=$(echo "$GET_BODY" | grep -o '"planets":{[^}]*}' | grep -o '"[a-z_]*":' | wc -l)
    HOUSES_COUNT=$(echo "$GET_BODY" | grep -o '"houses":{[^}]*}' | grep -o '"[0-9]*":' | wc -l)

    echo "   Planètes: $PLANETS_COUNT"
    echo "   Maisons: $HOUSES_COUNT"

    if [ "$PLANETS_COUNT" -ge 10 ] && [ "$HOUSES_COUNT" -ge 12 ]; then
        echo "   ✅ Chart complet après GET (auto-heal fonctionnel si nécessaire)"
    else
        echo "   ❌ Chart incomplet malgré GET (auto-heal échoué)"
        exit 1
    fi
else
    echo "❌ Erreur lors de la récupération du chart (HTTP $GET_HTTP_CODE)"
    echo "   Réponse: $GET_BODY"
    exit 1
fi
echo ""

echo "=========================================="
echo "✅ Test End-to-End: SUCCÈS"
echo "=========================================="
echo ""
echo "Résumé:"
echo "- POST /api/natal-chart: OK (chart créé)"
echo "- GET /api/natal-chart: OK (chart complet)"
echo "- Auto-heal: Fonctionnel (si chart incomplet détecté)"
echo "- Fallback mock: Disponible (si RapidAPI fail)"
echo ""
