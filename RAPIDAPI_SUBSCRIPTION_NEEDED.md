# ⚠️ Erreur RapidAPI : "You are not subscribed to this API"

## 🔴 Problème

```
HTTP/1.1 403 Forbidden
{"message":"You are not subscribed to this API."}
```

**Ta clé RapidAPI n'a pas accès à l'API "Best Astrology API".**

---

## ✅ Solution rapide : Utilise l'API V1

Ton ancien système **marche déjà** ! Il suffit de **désactiver le toggle RapidAPI** dans l'app :

1. Ouvre **Thème Natal** 🪐
2. **Désactive le toggle** en haut
3. Recalcule ton thème

```
┌─────────────────────────────────┐
│  📡 API V1 (Approx)    [OFF] │  ← Clique ici
└─────────────────────────────────┘
```

**Ça marche ! ✅** (Même si c'est approximatif)

---

## 🌟 Si tu veux vraiment RapidAPI (précis)

### 1️⃣ Souscris à l'API

Va sur : https://rapidapi.com/abarth_astrology/api/best-astrology-api-natal-charts-transits-synastry

**Plans disponibles** :
- **Basic** : Gratuit (100 requêtes/mois)
- **Pro** : $9.99/mois (5000 requêtes/mois)
- **Ultra** : $19.99/mois (50000 requêtes/mois)

### 2️⃣ Récupère ta clé

Après souscription, copie ta **X-RapidAPI-Key**.

### 3️⃣ Configure le .env

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
nano .env
```

Ajoute ou modifie :
```bash
RAPIDAPI_KEY=ta_vraie_cle_ici
```

### 4️⃣ Relance le backend

```bash
# Arrête le backend (Ctrl+C)
# Relance-le
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Tu devrais voir :
```
✅ (plus d'avertissement "⚠️ EPHEMERIS_API_KEY non configurée")
```

### 5️⃣ Teste

Réactive le toggle RapidAPI dans l'app et recalcule !

---

## 📊 Comparaison

| | **API V1** | **RapidAPI** |
|---|---|---|
| **Précision** | ±10° | Degré/minute ✓ |
| **Coût** | Gratuit | $9.99-19.99/mois |
| **Limite** | 1/24h | 100-50000/mois |
| **Setup** | ✅ Déjà prêt | Nécessite abonnement |

---

## 🎯 Recommandation

**Pour le développement** : Utilise l'API V1 (gratuit, fonctionne)

**Pour la production** : Souscris à RapidAPI Basic (gratuit, 100 requêtes) pour tester

---

**En attendant, désactive le toggle et utilise l'API V1 ! 🚀**

