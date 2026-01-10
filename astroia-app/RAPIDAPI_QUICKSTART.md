# ⚡ RapidAPI - Démarrage Rapide

## 🎯 Ce qui a été fait

J'ai intégré le **backend FastAPI + RapidAPI** de `astroia-lunar` dans ton app `astroia-app`.

Tu peux maintenant utiliser RapidAPI pour des calculs astrologiques **très précis** !

---

## 🚀 Comment tester (3 étapes)

### 1️⃣ Lancer le backend FastAPI

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
source .venv/bin/activate
uvicorn main:app --reload --port 8000
```

✅ Backend sur : `http://localhost:8000`

### 2️⃣ Lancer l'app mobile

```bash
cd /Users/remibeaurain/astroia/astroia-app
npx expo start
```

### 3️⃣ Tester dans l'app

1. Ouvre l'app sur ton téléphone
2. Va dans **Thème Natal** 🪐
3. **Active le toggle** "🌟 RapidAPI" en haut
4. Clique sur **"Calculer mon thème"**

✨ **C'est tout !**

---

## 🎛️ Le Toggle

```
┌─────────────────────────────────┐
│  🪐 Thème Natal                │
├─────────────────────────────────┤
│  🌟 RapidAPI (Précis)    [ON]  │  ← Toggle ici
└─────────────────────────────────┘
```

- **🌟 RapidAPI** : Backend FastAPI + RapidAPI (précis)
- **📡 API V1** : Ton ancienne API (approximatif)

---

## 📊 Différence API V1 vs RapidAPI

| Feature | API V1 | RapidAPI |
|---------|--------|----------|
| Précision | ±10° | Degré/minute exact |
| Limite | 1/24h | Illimité |
| Planètes | 6 | Toutes + Chiron |
| Maisons | Non | 12 maisons |
| Aspects | Non | Complets |
| Coût | Gratuit | 12€/mois |

---

## 🐛 Si ça marche pas

### Erreur "Network request failed"

→ Le backend n'est pas lancé. Lance-le avec :

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
uvicorn main:app --reload --port 8000
```

### Erreur "Erreur API: 500"

→ Vérifie que ta clé RapidAPI est dans le `.env` :

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
cat .env | grep RAPIDAPI_KEY
```

---

## 📝 Logs à surveiller

Dans **Expo** (terminal), tu devrais voir :

```bash
LOG  [NatalServiceRapidAPI] Payload envoyé: {...}
LOG  [NatalServiceRapidAPI] Réponse brute: {...}
LOG  [NatalServiceRapidAPI] Chart parsé: {...}
LOG  [NatalServiceRapidAPI] ✅ Sauvegardé dans AsyncStorage
LOG  [NatalChart] ✅ Données astro sauvegardées automatiquement !
```

---

## 📂 Fichiers modifiés

1. **`lib/api/natalServiceRapidAPI.js`** (NOUVEAU)
   - Client pour backend FastAPI
   - Parser RapidAPI → format app
   - Mapping signes EN → FR

2. **`app/natal-chart/index.js`** (MODIFIÉ)
   - Toggle RapidAPI vs API V1
   - Sélection dynamique du service

3. **`docs/RAPIDAPI_INTEGRATION.md`** (NOUVEAU)
   - Documentation complète

---

## ✅ C'est prêt !

Tu peux maintenant :
- ✅ **Tester** RapidAPI vs ton ancienne API
- ✅ **Comparer** les résultats
- ✅ **Basculer** facilement entre les deux
- ✅ **Garder** les deux systèmes en parallèle

---

**Questions ? Regarde `docs/RAPIDAPI_INTEGRATION.md` pour plus de détails ! 🌙**

