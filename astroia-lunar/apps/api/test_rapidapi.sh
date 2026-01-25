#!/bin/bash
# Script de test RapidAPI pour thème natal

echo "🧪 Test appel RapidAPI (1er nov 1989, Manaus)"
echo ""

# Appeler l'API avec force=true pour bypasser le cache
curl -X POST http://localhost:8000/api/natal-chart \
  -H "Content-Type: application/json" \
  -H "X-Dev-User-Id: 2" \
  -d '{
    "date": "1989-11-01",
    "time": "13:20",
    "place_name": "Manaus",
    "latitude": -3.131633,
    "longitude": -59.982504,
    "timezone": "America/Manaus"
  }' | python3 -m json.tool | head -50

echo ""
echo "✅ Si vous voyez sun_sign et ascendant différents, RapidAPI fonctionne"
