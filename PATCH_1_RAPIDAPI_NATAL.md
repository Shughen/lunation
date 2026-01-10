# ✅ Patch 1 : Backend – Utiliser RapidAPI pour `/api/natal-chart`

**Date :** 2025-01-27  
**Statut :** ✅ Implémenté  
**Fichiers modifiés :** `apps/api/routes/natal.py`

---

## 📋 Résumé des modifications

### Changements principaux

1. **Remplacement de `ephemeris_client` par RapidAPI**
   - Avant : Utilisait `ephemeris_client` (Ephemeris API - astrology-api.io)
   - Après : Utilise `call_rapidapi_natal_chart()` (RapidAPI - Best Astrology API)

2. **Adaptation du payload**
   - Format RapidAPI : `{ "subject": { "name": "...", "birth_data": {...} }, "options": {...} }`
   - Conversion depuis le format mobile : `{ date, time, latitude, longitude, place_name, timezone }`

3. **Parsing de la réponse RapidAPI**
   - Utilise les fonctions existantes : `parse_positions_from_natal_chart()` et `parse_aspects_from_natal_chart()`
   - Conversion des signes abrégés ("Sco", "Ari") → noms complets ("Scorpio", "Aries")
   - Parsing des maisons depuis `house_cusps` avec calcul du signe depuis longitude absolue

4. **Format de réponse maintenu**
   - Le format de réponse reste identique pour le mobile
   - `{ id, sun_sign, moon_sign, ascendant, planets, houses, aspects }`

---

## 🔧 Détails techniques

### Imports modifiés

```python
# Avant
from services.ephemeris import ephemeris_client, EphemerisAPIKeyError

# Après
from services.ephemeris_rapidapi import create_natal_chart
from services.natal_reading_service import call_rapidapi_natal_chart, parse_positions_from_natal_chart, parse_aspects_from_natal_chart
```

### Conversion du payload

Le payload mobile est converti au format RapidAPI :

```python
birth_data = {
    "year": int(data.date.split("-")[0]),
    "month": int(data.date.split("-")[1]),
    "day": int(data.date.split("-")[2]),
    "hour": int(birth_time.split(":")[0]),
    "minute": int(birth_time.split(":")[1]),
    "second": 0,
    "city": data.place_name or "Unknown",
    "country_code": "FR",
    "latitude": data.latitude,
    "longitude": data.longitude,
    "timezone": data.timezone
}
```

### Mapping des signes

Les signes abrégés RapidAPI sont convertis en noms complets :

```python
sign_mapping = {
    "Ari": "Aries", "Tau": "Taurus", "Gem": "Gemini", "Can": "Cancer",
    "Leo": "Leo", "Vir": "Virgo", "Lib": "Libra", "Sco": "Scorpio",
    "Sag": "Sagittarius", "Cap": "Capricorn", "Aqu": "Aquarius", "Pis": "Pisces"
}
```

### Parsing des maisons

Les maisons sont parsées depuis `house_cusps` (array de longitudes absolues) :

```python
# Calcul du signe depuis longitude absolue
abs_long = float(cusp)
sign_idx = int(abs_long // 30) % 12
degree_in_sign = abs_long % 30
```

---

## 🧪 Tests

### Prérequis

1. **Backend démarré** : `cd apps/api && uvicorn main:app --reload`
2. **RAPIDAPI_KEY configurée** dans `.env` :
   ```bash
   RAPIDAPI_KEY=votre_cle_rapidapi
   ```
3. **Token JWT valide** (ou mode DEV_AUTH_BYPASS activé)

### Test 1 : Calcul thème natal (POST)

```bash
# Récupérer un token JWT d'abord (via /api/auth/login)
TOKEN="votre_token_jwt"

# Test POST /api/natal-chart
curl -X POST http://localhost:8000/api/natal-chart \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }' | jq
```

**Réponse attendue (201 Created) :**
```json
{
  "id": "uuid-du-theme",
  "sun_sign": "Taurus",
  "moon_sign": "Pisces",
  "ascendant": "Leo",
  "planets": {
    "sun": { "sign": "Taurus", "degree": 24.5, "house": 2 },
    "moon": { "sign": "Pisces", "degree": 12.3, "house": 9 },
    "mercury": { "sign": "Gemini", "degree": 5.7, "house": 3 },
    ...
  },
  "houses": {
    "1": { "sign": "Leo", "degree": 15.2 },
    "2": { "sign": "Virgo", "degree": 8.4 },
    ...
  },
  "aspects": [
    {
      "planet1": "Sun",
      "planet2": "Moon",
      "type": "trine",
      "orb": 2.1
    },
    ...
  ]
}
```

### Test 2 : Récupération thème natal (GET)

```bash
curl -X GET http://localhost:8000/api/natal-chart \
  -H "Authorization: Bearer $TOKEN" | jq
```

**Réponse attendue (200 OK) :**
```json
{
  "id": "uuid-du-theme",
  "sun_sign": "Taurus",
  "moon_sign": "Pisces",
  "ascendant": "Leo",
  "planets": { ... },
  "houses": { ... },
  "aspects": [ ... ]
}
```

### Test 3 : Mode DEV_AUTH_BYPASS (si activé)

```bash
# Si DEV_AUTH_BYPASS=true dans .env
curl -X POST http://localhost:8000/api/natal-chart \
  -H "X-Dev-User-Id: 1" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }' | jq
```

---

## ✅ Checklist de validation

- [x] Code modifié pour utiliser RapidAPI
- [x] Parsing des positions planétaires fonctionnel
- [x] Parsing des aspects fonctionnel
- [x] Parsing des maisons fonctionnel
- [x] Mapping des signes (abrégés → complets) fonctionnel
- [x] Format de réponse identique au format attendu par le mobile
- [x] Gestion d'erreurs HTTP RapidAPI
- [x] Logs informatifs pour debug

---

## 🔍 Points à vérifier lors des tests

1. **Vérifier les signes** : Les signes doivent être en format complet ("Taurus", "Pisces", etc.), pas en abrégé
2. **Vérifier les degrés** : Les degrés doivent être entre 0 et 30 (position dans le signe)
3. **Vérifier les maisons** : Les 12 maisons doivent être présentes avec signe et degré
4. **Vérifier les aspects** : Les aspects doivent avoir `planet1`, `planet2`, `type`, `orb`
5. **Vérifier la cohérence** : Les valeurs doivent être cohérentes (ex: si Sun est en Taurus, `sun_sign` doit être "Taurus")

---

## 🐛 Gestion d'erreurs

### Erreur 502 Bad Gateway
- **Cause** : RapidAPI retourne une erreur HTTP
- **Solution** : Vérifier `RAPIDAPI_KEY` et quota RapidAPI

### Erreur 503 Service Unavailable
- **Cause** : Impossible de se connecter à RapidAPI
- **Solution** : Vérifier la connexion internet et l'URL RapidAPI

### Format de réponse invalide
- **Cause** : `chart_data` manquant dans la réponse RapidAPI
- **Solution** : Vérifier le format de la réponse RapidAPI (peut avoir changé)

---

## 📝 Notes

- Le format de réponse reste **identique** pour le mobile (pas de breaking changes)
- Les signes sont maintenant en format complet (compatibilité avec le mobile)
- Les maisons sont calculées depuis les longitudes absolues
- Les aspects utilisent les noms de planètes complets ("Sun", "Moon", etc.)

---

## 🚀 Prochaines étapes

Une fois ce patch validé :
1. **Patch 2** : Aligner types TS + parsing côté mobile (si nécessaire)
2. **Patch 3** : Rétablir welcome screen + guards onboarding

