#!/bin/bash
# Script de test pour /api/natal-chart avec DEV_MOCK_NATAL=1
# User standardisé : 550e8400-e29b-41d4-a716-446655440000

set -e

# Détecter le répertoire du script de manière robuste
SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"

# API URL avec override possible via variable d'environnement
API_URL="${API_URL:-http://127.0.0.1:8000}"
DEV_USER_UUID="550e8400-e29b-41d4-a716-446655440000"

echo "🧪 Test /api/natal-chart avec DEV_MOCK_NATAL=1"
echo "📡 API: $API_URL"
echo "👤 User UUID: $DEV_USER_UUID"
echo "📂 Script dir: $SCRIPT_DIR"
echo ""

# Payload natal chart (dates de naissance fictives)
PAYLOAD=$(cat <<'EOF'
{
  "date": "1990-01-15",
  "time": "14:30",
  "latitude": 48.8566,
  "longitude": 2.3522,
  "place_name": "Paris, France"
}
EOF
)

echo "1️⃣ Test création natal chart mock..."
echo "Payload:"
echo "$PAYLOAD" | python3 -m json.tool
echo ""

# Utiliser un fichier temporaire pour le body et récupérer http_code séparément
tmpfile=$(mktemp)
trap "rm -f $tmpfile" EXIT

# POST /api/natal-chart
http_code=$(curl -X POST "$API_URL/api/natal-chart" \
  -H "X-Dev-External-Id: $DEV_USER_UUID" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD" \
  -w "%{http_code}" \
  -o "$tmpfile" \
  -sS)

echo "HTTP Status: $http_code"

if [ "$http_code" = "200" ]; then
    echo "✅ Succès - Thème natal créé/mis à jour"
    echo "Réponse:"
    if [ -s "$tmpfile" ]; then
        python3 -m json.tool < "$tmpfile" || {
            echo "❌ Erreur parsing JSON"
            echo "Body brut:"
            cat "$tmpfile"
            rm -f "$tmpfile"
            exit 1
        }
    else
        echo "⚠️ Body vide"
    fi
else
    echo "❌ Erreur HTTP $http_code"
    echo "Réponse:"
    cat "$tmpfile"
    rm -f "$tmpfile"
    exit 1
fi

rm -f "$tmpfile"
echo ""
echo "✅ Test terminé"
