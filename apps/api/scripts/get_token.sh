#!/usr/bin/env zsh

# Script zsh pour récupérer un JWT depuis l'API Astroia Lunar
# Usage:
#   ./scripts/get_token.sh email password
# Exemple:
#   TOKEN=$(./scripts/get_token.sh remi+test1@local.dev 'MonMotDePasse123!')
#   echo ${TOKEN:0:20}

API_URL=http://127.0.0.1:8000

EMAIL=$1
PASSWORD=$2

if [ -z $EMAIL ] || [ -z $PASSWORD ]; then
  echo 'Usage: ./scripts/get_token.sh email password' >&2
  exit 1
fi

RESPONSE=$(curl -s -X POST $API_URL/api/auth/login \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d username=$EMAIL \
  -d password=$PASSWORD)

TOKEN=$(printf '%s' $RESPONSE | python3 - << 'EOF'
import sys
import json

data = sys.stdin.read()
try:
    parsed = json.loads(data)
    token = parsed.get('access_token')
    if not token:
        sys.exit(1)
    print(token)
except Exception:
    sys.exit(1)
EOF
)

if [ -z $TOKEN ]; then
  echo 'Erreur: impossible de récupérer le token' >&2
  exit 1
fi

echo $TOKEN


