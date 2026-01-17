#!/bin/bash

echo "=========================================="
echo "TEST CURL - Calcul thème Nathan"
echo "=========================================="
echo ""
echo "Prérequis: API lancée sur http://localhost:8000"
echo "            Token d'authentification valide"
echo ""
echo "Instructions:"
echo "1. Récupérer un token d'authentification"
echo "2. Remplacer YOUR_TOKEN ci-dessous"
echo "3. Lancer ce script"
echo ""
echo "=========================================="
echo ""

# TODO: Remplacer YOUR_TOKEN par un vrai token
TOKEN="YOUR_TOKEN"

echo "Appel POST /api/natal-chart..."
echo ""

curl -X POST http://localhost:8000/api/natal-chart \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "date": "2001-02-09",
    "time": "11:30",
    "latitude": 44.8378,
    "longitude": -0.5792,
    "place_name": "Bordeaux",
    "timezone": "Europe/Paris"
  }' | jq '.'

echo ""
echo "=========================================="
echo "Vérifications:"
echo "=========================================="
echo ""
echo "1. Chercher 'moon_sign' dans la réponse"
echo "2. Chercher 'planets.moon.sign' dans la réponse"
echo ""
echo "Si vous voyez 'Leo', copier/coller la réponse complète"
echo "pour que je puisse voir où est le problème."
echo ""
