#!/usr/bin/env zsh

# Script E2E (mode DEV_MOCK_EPHEMERIS=1)
# Flow: login -> POST /api/natal-chart -> POST /api/lunar-returns/generate -> GET /api/lunar-returns/
#
# Prérequis .env:
#   EPHEMERIS_API_KEY=
#   DEV_MOCK_EPHEMERIS=1

API_URL=http://127.0.0.1:8000
EMAIL=$1
PASSWORD=$2

if [ -z $EMAIL ] || [ -z $PASSWORD ]; then
  echo 'Usage: ./scripts/e2e_mock.sh email password' >&2
  exit 1
fi

echo '🔐 Login...'
TOKEN=$(./scripts/get_token.sh $EMAIL $PASSWORD)

if [ -z $TOKEN ] || [ $TOKEN = null ]; then
  echo '❌ Erreur login' >&2
  exit 1
fi

echo "✅ Token: ${TOKEN:0:20}..."

echo ''
echo '✨ Création natal_chart (mode mock)...'

NATAL_PAYLOAD=$(python3 - << 'EOF'
import json
payload = {
    'date': '1990-05-15',
    'time': '14:30:00',
    'latitude': 48.8566,
    'longitude': 2.3522,
    'place_name': 'Paris, France',
    'timezone': 'Europe/Paris',
}
print(json.dumps(payload))
EOF
)

NATAL_RESPONSE=$(printf '%s' $NATAL_PAYLOAD | curl -s -X POST $API_URL/api/natal-chart \
  -H 'Authorization: Bearer '$TOKEN \
  -H 'Content-Type: application/json' \
  -d @-)

NATAL_ID=$(printf '%s' $NATAL_RESPONSE | python3 - << 'EOF'
import sys, json
data = sys.stdin.read()
try:
    parsed = json.loads(data)
    val = parsed.get('id')
    if val is None:
        sys.exit(1)
    print(val)
except Exception:
    sys.exit(1)
EOF
)

if [ -z $NATAL_ID ]; then
  echo '❌ Erreur création natal_chart' >&2
  printf '%s\n' $NATAL_RESPONSE
  exit 1
fi

echo '✅ Natal chart créé - ID:' $NATAL_ID

echo ''
echo '🌙 Génération révolutions lunaires...'

LUNAR_RESPONSE=$(curl -s -X POST $API_URL/api/lunar-returns/generate \
  -H 'Authorization: Bearer '$TOKEN \
  -H 'Content-Type: application/json')

GENERATED_COUNT=$(printf '%s' $LUNAR_RESPONSE | python3 - << 'EOF'
import sys, json
data = sys.stdin.read()
try:
    parsed = json.loads(data)
    val = parsed.get('generated_count')
    if val is None:
        sys.exit(1)
    print(val)
except Exception:
    sys.exit(1)
EOF
)

if [ -z $GENERATED_COUNT ]; then
  echo '❌ Erreur génération lunar returns' >&2
  printf '%s\n' $LUNAR_RESPONSE
  exit 1
fi

echo '✅' $GENERATED_COUNT 'révolution(s) lunaire(s) générée(s)'

echo ''
echo '📋 Récupération révolutions lunaires...'

LUNAR_LIST=$(curl -s -X GET $API_URL/api/lunar-returns/ \
  -H 'Authorization: Bearer '$TOKEN)

LUNAR_COUNT=$(printf '%s' $LUNAR_LIST | python3 - << 'EOF'
import sys, json
data = sys.stdin.read()
try:
    parsed = json.loads(data)
    if not isinstance(parsed, list):
        sys.exit(1)
    print(len(parsed))
except Exception:
    sys.exit(1)
EOF
)

if [ -z $LUNAR_COUNT ]; then
  echo '❌ Erreur lecture lunar returns' >&2
  printf '%s\n' $LUNAR_LIST
  exit 1
fi

echo '✅' $LUNAR_COUNT 'révolution(s) trouvée(s)'

echo ''
echo '🎉 Flow E2E mock complété avec succès'


