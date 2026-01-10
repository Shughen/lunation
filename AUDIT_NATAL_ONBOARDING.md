# 🔍 Audit End-to-End : Calcul Natal + Onboarding

**Date :** 2025-01-27  
**Contexte :** Projet Astroia Lunar (monorepo FastAPI + Expo RN)  
**Problèmes identifiés :** Calcul natal incorrect + Onboarding disparu

---

## A) AUDIT CALCUL NATAL

### 1. Flow actuel (Mobile → Backend)

#### Mobile (`apps/mobile/services/api.ts`)
```typescript
// Ligne 142-153
natalChart: {
  calculate: async (data) => {
    const response = await apiClient.post('/api/natal-chart', data);
    return response.data;
  }
}
```

**Endpoint appelé :** `POST /api/natal-chart`  
**Payload envoyé :**
```typescript
{
  date: "1990-05-15",      // YYYY-MM-DD
  time: "14:30",            // HH:MM
  latitude: 48.8566,
  longitude: 2.3522,
  place_name: "Paris, France",
  timezone: "Europe/Paris"
}
```

#### Backend (`apps/api/routes/natal.py`)
```python
# Ligne 45-82
@router.post("/natal-chart")
async def calculate_natal_chart(data: NatalChartRequest, ...):
    # ❌ PROBLÈME : Utilise ephemeris_client (Ephemeris API, pas RapidAPI)
    raw_data = await ephemeris_client.calculate_natal_chart(
        date=data.date,
        time=birth_time,
        latitude=data.latitude,
        longitude=data.longitude,
        timezone=data.timezone
    )
```

**Service utilisé :** `ephemeris_client` (`apps/api/services/ephemeris.py`)  
- Appelle `astrology-api.io` (Ephemeris API)  
- **N'utilise PAS RapidAPI**

#### Service RapidAPI existant mais non utilisé
```python
# apps/api/services/ephemeris_rapidapi.py
async def create_natal_chart(payload: Dict[str, Any]) -> Dict[str, Any]:
    # ✅ Ce service existe et utilise RapidAPI
    # Mais il n'est utilisé QUE par /api/natal-chart/external
```

**Endpoint alternatif :** `POST /api/natal-chart/external`  
- Utilise `ephemeris_rapidapi.create_natal_chart()`  
- **Non utilisé par le mobile**

### 2. Format de réponse attendu vs réel

#### Format attendu par le mobile (`apps/mobile/app/natal-chart.tsx`)
```typescript
// Lignes 84-85, 202-232
{
  id: string,
  sun_sign: string,        // Ex: "Taurus"
  moon_sign: string,       // Ex: "Pisces"
  ascendant: string,       // Ex: "Leo"
  planets: {              // Dict des planètes
    [planetName]: {
      sign: string,
      degree: number,
      house: number
    }
  },
  houses: {               // Dict ou Array des maisons
    [houseKey]: {
      sign: string,
      degree: number
    }
  },
  aspects: [              // Array des aspects
    {
      planet1: string,
      planet2: string,
      type: string,        // "conjunction", "trine", etc.
      orb: number
    }
  ]
}
```

#### Format retourné par le backend (`apps/api/routes/natal.py`)
```python
# Lignes 219-227
return {
    "id": str(chart.id),
    "sun_sign": big3["sun_sign"] or "Unknown",
    "moon_sign": big3["moon_sign"] or "Unknown",
    "ascendant": big3["ascendant_sign"] or "Unknown",
    "planets": planets,      # Depuis positions["planets"]
    "houses": houses,        # Depuis positions["houses"]
    "aspects": aspects       # Depuis positions["aspects"]
}
```

**✅ Le format de réponse est correct**, mais les données viennent de la mauvaise API.

### 3. Divergence identifiée

**PROBLÈME PRINCIPAL :**
- Le backend utilise `ephemeris_client` (Ephemeris API) au lieu de `ephemeris_rapidapi` (RapidAPI)
- RapidAPI est configuré et fonctionnel (`RAPIDAPI_KEY`, `NATAL_URL` dans `config.py`)
- Le service `ephemeris_rapidapi.py` existe et fonctionne
- Mais il n'est pas utilisé par `/api/natal-chart`

**CAUSE :**
- `routes/natal.py` ligne 16 importe `ephemeris_client` au lieu d'utiliser `ephemeris_rapidapi`
- Le format de payload RapidAPI est différent de celui d'Ephemeris API

---

## B) AUDIT ONBOARDING

### 1. Écrans existants

#### `apps/mobile/app/onboarding.tsx`
- ✅ Existe et fonctionne
- Combine auth (step 1) + birth data (step 2)
- Marque `onboarding_completed = 'true'` dans AsyncStorage après succès

#### `apps/mobile/app/index.tsx`
- ✅ Guards de navigation présents (lignes 34-94)
- Vérifie :
  1. `isAuthenticated`
  2. `onboarding_completed` dans AsyncStorage
  3. Thème natal existant via `natalChart.get()`

### 2. Problème identifié

**Pas de welcome screen séparé :**
- L'onboarding commence directement par l'inscription
- Pas d'écran "Bienvenue" pour les nouveaux utilisateurs
- Les guards redirigent vers `/onboarding` si `onboarding_completed !== 'true'`

**Guards peut-être trop stricts :**
- Si un utilisateur a déjà un compte mais pas de thème natal, il est redirigé vers onboarding
- Mais l'onboarding est conçu pour l'inscription, pas pour compléter un profil existant

### 3. Flow attendu vs réel

**Flow attendu (selon demande) :**
1. Welcome screen (première connexion)
2. Onboarding (collecte infos naissance si nécessaire)
3. Guards : `hasSeenWelcomeScreen`, `hasCompletedOnboarding`, `hasValidProfile`

**Flow réel :**
1. Pas de welcome screen
2. Onboarding direct (auth + birth data)
3. Guards : `isAuthenticated`, `onboarding_completed`, `natalChart.get()`

---

## C) PLAN DE CORRECTION

### Patch 1 : Backend – Utiliser RapidAPI pour `/api/natal-chart`

**Objectif :** Remplacer `ephemeris_client` par `ephemeris_rapidapi` dans `routes/natal.py`

**Modifications :**
1. Adapter le payload pour RapidAPI (format différent)
2. Parser la réponse RapidAPI vers le format attendu par le mobile
3. Tester avec curl/Postman

**Fichiers à modifier :**
- `apps/api/routes/natal.py` (lignes 16, 60-82)

**Format payload RapidAPI :**
```python
{
    "name": "John Doe",           # Optionnel
    "date": "1990-05-15",          # YYYY-MM-DD
    "time": "14:30",               # HH:MM
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
}
```

**Format réponse RapidAPI :**
- À analyser depuis `ephemeris_rapidapi.py` et adapter le parsing

---

### Patch 2 : Mobile – Aligner types TS + parsing

**Objectif :** S'assurer que le mobile parse correctement la réponse backend

**Modifications :**
1. Vérifier les types TypeScript dans `natal-chart.tsx`
2. Adapter le parsing si nécessaire (planets, houses, aspects)
3. Tester l'affichage

**Fichiers à modifier :**
- `apps/mobile/app/natal-chart.tsx` (si nécessaire)

---

### Patch 3 : Onboarding – Rétablir welcome screen + guards

**Objectif :** Ajouter un welcome screen et améliorer les guards

**Modifications :**
1. Créer `apps/mobile/app/welcome.tsx` (écran de bienvenue)
2. Modifier les guards dans `index.tsx` pour vérifier `hasSeenWelcomeScreen`
3. Modifier `onboarding.tsx` pour gérer les utilisateurs existants (compléter profil)

**Fichiers à créer/modifier :**
- `apps/mobile/app/welcome.tsx` (nouveau)
- `apps/mobile/app/index.tsx` (guards)
- `apps/mobile/app/onboarding.tsx` (gestion utilisateurs existants)

---

## D) ORDRE D'IMPLÉMENTATION

1. **Patch 1 uniquement** → Test backend via curl/Postman
2. Attendre validation
3. Patch 2 → Test mobile
4. Attendre validation
5. Patch 3 → Test flow complet

---

## E) TESTS À EFFECTUER

### Patch 1 (Backend)
```bash
# Test POST /api/natal-chart
curl -X POST http://localhost:8000/api/natal-chart \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-05-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France",
    "timezone": "Europe/Paris"
  }'
```

**Vérifier :**
- ✅ Réponse 201 avec `id`, `sun_sign`, `moon_sign`, `ascendant`
- ✅ `planets` est un dict avec toutes les planètes
- ✅ `houses` est un dict/array avec les 12 maisons
- ✅ `aspects` est un array avec les aspects majeurs
- ✅ Les valeurs sont cohérentes (signes valides, degrés entre 0-30, etc.)

---

## F) NOTES IMPORTANTES

- ⚠️ **NE PAS inventer une nouvelle Ephemeris API** - Utiliser RapidAPI existant
- ⚠️ **Pas de refacto large** - Modifications minimales
- ⚠️ **Compatibilité Expo Go iPhone** - Tester sur device réel
- ⚠️ **Priorité : exactitude du thème natal** - Le calcul doit être correct

