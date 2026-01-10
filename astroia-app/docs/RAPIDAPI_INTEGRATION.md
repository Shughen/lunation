# 🌟 Intégration RapidAPI - Thème Natal

## 🎯 Objectif

Intégrer le backend **FastAPI + RapidAPI** de `astroia-lunar` dans l'application `astroia-app` existante, permettant d'utiliser l'API RapidAPI (Best Astrology API) pour des calculs astrologiques précis.

---

## 📦 Architecture

```
astroia-app/                    # Frontend React Native (Expo)
├── lib/api/
│   ├── natalService.js         # ✅ Service original (API V1 custom)
│   └── natalServiceRapidAPI.js # ✨ NOUVEAU: Service RapidAPI
└── app/natal-chart/
    └── index.js                # ✅ Écran modifié avec toggle API

astroia-lunar/apps/api/         # Backend FastAPI
├── main.py                     # Point d'entrée
├── routes/natal.py             # Endpoint /api/natal-chart/external
└── services/ephemeris_rapidapi.py  # Client RapidAPI
```

---

## 🚀 Installation & Configuration

### 1️⃣ Lancer le backend FastAPI

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

# Activer l'environnement virtuel
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows

# Vérifier les dépendances
pip install -r requirements.txt

# Configurer .env
# Ajouter ta clé RapidAPI:
# RAPIDAPI_KEY=ta_cle_ici

# Lancer le serveur
uvicorn main:app --reload --port 8000
```

✅ **Backend disponible sur** : `http://localhost:8000`  
✅ **Docs API** : `http://localhost:8000/docs`

### 2️⃣ Configurer l'app mobile

Le nouveau service est déjà intégré dans `astroia-app`. Pas de configuration supplémentaire nécessaire.

### 3️⃣ Lancer l'app mobile

```bash
cd /Users/remibeaurain/astroia/astroia-app

# Lancer Expo
npx expo start
```

---

## 💻 Utilisation

### Toggle entre API V1 et RapidAPI

Dans l'écran **Thème Natal** (`app/natal-chart/index.js`), tu as maintenant un **toggle en haut** :

```
┌─────────────────────────────────┐
│  ← 🪐 Thème Natal              │
├─────────────────────────────────┤
│  🌟 RapidAPI (Précis)    [ON]  │  ← Toggle ici
└─────────────────────────────────┘
```

- **🌟 RapidAPI (Précis)** : Utilise le backend FastAPI + RapidAPI (calculs très précis)
- **📡 API V1 (Approx)** : Utilise l'ancienne API custom (approximatif, limite 1/24h)

### Calcul d'un thème natal

1. **Assure-toi que ton profil est complet** (date, heure, lieu de naissance avec coordonnées)
2. Va dans l'onglet **Thème Natal**
3. **Active le toggle RapidAPI** (activé par défaut)
4. Clique sur **"Calculer mon thème"**
5. Le système appelle le backend FastAPI qui utilise RapidAPI
6. Les données sont **sauvegardées automatiquement** dans ton profil

---

## 📊 Format des données

### Payload envoyé au backend

```json
{
  "subject": {
    "name": "Paris, France",
    "birth_data": {
      "year": 1989,
      "month": 11,
      "day": 1,
      "hour": 13,
      "minute": 20,
      "timezone": "Etc/GMT+4",
      "latitude": -3.1316333,
      "longitude": -59.9825041
    }
  }
}
```

### Réponse du backend

```json
{
  "provider": "rapidapi",
  "endpoint": "chart_natal",
  "data": {
    "planets": [
      {
        "name": "Sun",
        "sign": "Scorpio",
        "degree": 9.09,
        "house": 8,
        "retrograde": false
      },
      {
        "name": "Moon",
        "sign": "Sagittarius",
        "degree": 10.61,
        "house": 9,
        "retrograde": false
      },
      ...
    ],
    "houses": [...],
    "aspects": [...]
  }
}
```

### Données parsées et sauvegardées

```javascript
{
  chart: {
    sun: {
      sign: 'Scorpion',  // Traduit en français
      emoji: '♏',
      element: 'Eau',
      degree: 9,
      minutes: 5,
      longitude: 219.09
    },
    moon: { ... },
    ascendant: { ... },
    mercury: { ... },
    venus: { ... },
    mars: { ... }
  },
  meta: {
    version: 'RapidAPI-v3',
    provider: 'best-astrology-api',
    computed_at: '2025-11-12T...'
  }
}
```

---

## 🔧 Services disponibles

### `natalServiceRapidAPI.js`

Nouveau service qui communique avec le backend FastAPI :

```javascript
import { natalServiceRapidAPI } from '@/lib/api/natalServiceRapidAPI';

// Calculer un thème natal
const chart = await natalServiceRapidAPI.computeNatalChart({
  birthDate: new Date('1989-11-01'),
  birthTime: new Date('1989-11-01T13:20:00'),
  birthPlace: 'Manaus, Brazil',
  lat: -3.1316333,
  lon: -59.9825041,
  tz: 'America/Manaus'
});

// Récupérer le dernier thème calculé
const lastChart = await natalServiceRapidAPI.getLatestNatalChart();

// Effacer le cache
await natalServiceRapidAPI.clearCache();
```

---

## 🎨 Interface utilisateur

### Changements visuels

1. **Toggle en haut de l'écran** pour choisir l'API
2. **Indicateur de source** dans le disclaimer ("Source : best-astrology-api")
3. **Message de confirmation** indique quelle API a été utilisée

### Screenshots

```
┌─────────────────────────────────┐
│  🌟 RapidAPI (Précis)    [ON]  │
├─────────────────────────────────┤
│                                 │
│         ⭐                      │
│       John Doe                  │
│   Scorpion • Eau               │
│                                 │
├─────────────────────────────────┤
│  Carte du ciel                 │
│  [Roue zodiacale]              │
├─────────────────────────────────┤
│  Positions planétaires         │
│  ☀️ Soleil                     │
│  ♏ Scorpion - 9°5' ✓          │
│                                 │
│  🌙 Lune                       │
│  ♐ Sagittaire - 10°36' ✓      │
│                                 │
│  ⬆️ Ascendant                  │
│  ♓ Poissons - 15°14' ✓        │
└─────────────────────────────────┘
```

---

## 🐛 Debugging

### Activer les logs

Les logs sont déjà activés. Dans Expo, tu verras :

```bash
LOG  [NatalServiceRapidAPI] Données de naissance: {...}
LOG  [NatalServiceRapidAPI] Payload envoyé: {...}
LOG  [NatalServiceRapidAPI] Réponse brute: {...}
LOG  [NatalServiceRapidAPI] Chart parsé: {...}
LOG  [NatalServiceRapidAPI] ✅ Sauvegardé dans AsyncStorage
```

### Erreurs courantes

#### ❌ "Erreur API: 500"
- **Cause** : Backend FastAPI n'est pas démarré
- **Solution** : Lancer `uvicorn main:app --reload --port 8000`

#### ❌ "Network request failed"
- **Cause** : Mauvaise URL du backend
- **Solution** : Vérifier `FASTAPI_BASE_URL` dans `natalServiceRapidAPI.js`

#### ❌ "Erreur lors du parsing"
- **Cause** : Format de réponse RapidAPI inattendu
- **Solution** : Vérifier les logs et adapter `parseRapidAPIResponse()`

### Tester l'endpoint directement

```bash
curl -X POST http://localhost:8000/api/natal-chart/external \
  -H "Content-Type: application/json" \
  -d '{
    "subject": {
      "name": "Test",
      "birth_data": {
        "year": 1989,
        "month": 11,
        "day": 1,
        "hour": 13,
        "minute": 20,
        "timezone": "America/Manaus",
        "latitude": -3.1316333,
        "longitude": -59.9825041
      }
    }
  }'
```

---

## 📈 Avantages de RapidAPI

### API V1 (ancienne)
- ❌ Approximatif (ascendant ±10°)
- ❌ Limite 1 calcul / 24h
- ❌ Planètes limitées (Soleil, Lune, 4 planètes)
- ✅ Gratuit

### RapidAPI (nouvelle)
- ✅ **Très précis** (degré/minute exact)
- ✅ **Pas de limite** de calculs
- ✅ **Toutes les planètes** + Chiron, Nœuds, Lilith
- ✅ **12 maisons** + aspects complets
- ✅ **Phase lunaire**
- 💰 Payant (12€/mois pour 10k requêtes)

---

## 🔄 Migration des données existantes

Les deux systèmes coexistent. Les anciennes données (API V1) restent accessibles en désactivant le toggle.

### Stockage séparé

- **API V1** : `natal_chart_local` (AsyncStorage) + `natal_charts` (Supabase)
- **RapidAPI** : `natal_chart_rapidapi` (AsyncStorage) + `natal_charts` (Supabase avec `version: 'rapidapi-v3'`)

---

## 📝 TODO / Améliorations

- [ ] Ajouter configuration de l'URL backend dans les settings
- [ ] Gérer les erreurs réseau plus gracieusement
- [ ] Ajouter un indicateur de connexion au backend
- [ ] Afficher plus de planètes (Jupiter, Saturne, Uranus, Neptune, Pluton)
- [ ] Ajouter les aspects dans l'interface
- [ ] Calculer et afficher les 12 maisons
- [ ] Intégrer la phase lunaire

---

## 🎯 Prochaines étapes

1. **Tester** le calcul avec RapidAPI activé
2. **Comparer** les résultats entre API V1 et RapidAPI
3. **Valider** que les données sont bien sauvegardées
4. **Déployer** le backend FastAPI en production (Railway/Vercel)
5. **Configurer** l'URL de production dans l'app

---

**Fait avec 🌙 et ⭐ - Intégration RapidAPI complète !**

