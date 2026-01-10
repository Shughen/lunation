# 🚀 Déployer ephemeris-api sur Railway (GRATUIT)

## 🎯 LA SOLUTION GRATUITE PARFAITE

**ephemeris-api** : API HTTP complète avec **Swiss Ephemeris** 
- ✅ Précision professionnelle (même qu'Astrotheme)
- ✅ 100% Gratuit ($0/an)
- ✅ Open-source (Unlicense/public domain)
- ✅ Self-hosted (tu contrôles tout)

---

## 🚂 OPTION 1 : RAILWAY.APP (RECOMMANDÉ)

### Étape 1 : Créer compte Railway
1. Va sur https://railway.app
2. Connecte-toi avec GitHub
3. **Plan gratuit : $5 de crédit gratuit/mois** (largement suffisant)

### Étape 2 : Déployer ephemeris-api

```bash
# Depuis ton terminal
cd /Users/remibeaurain/astroia/ephemeris-api

# Installer Railway CLI
brew install railway

# Login
railway login

# Créer nouveau projet
railway init

# Déployer
railway up
```

### Étape 3 : Récupérer l'URL

```bash
# Afficher l'URL de ton API
railway domain

# Exemple de résultat : https://ephemeris-api-production.up.railway.app
```

### Étape 4 : Tester

```bash
curl https://[ton-url].railway.app/
```

**Tu devrais voir l'interface Swagger avec la doc de l'API !** ✅

---

## 🎨 OPTION 2 : RENDER.COM (Alternative)

### Étape 1 : Créer compte Render
1. Va sur https://render.com
2. Connecte-toi avec GitHub
3. **Plan gratuit** disponible

### Étape 2 : Nouveau Web Service

1. Clique "New +" → "Web Service"
2. Connecte ton repo GitHub : `ephemeris-api`
3. Configure :
   ```
   Name: ephemeris-api
   Environment: Docker
   Plan: Free
   ```
4. Deploy !

### Étape 3 : Attendre ~5 minutes

Render va :
- Compiler le JAR Clojure
- Construire le container Docker
- Déployer l'API

### Étape 4 : Récupérer l'URL

```
https://ephemeris-api.onrender.com
```

---

## 🔌 INTÉGRATION DANS TON APP

Une fois l'API déployée, configure ton backend Vercel :

### Dans .env (ou Vercel Environment Variables)

```bash
NATAL_PROVIDER=ephemeris-api
EPHEMERIS_API_URL=https://[ton-url].railway.app
# ou https://ephemeris-api.onrender.com
```

### Le code est déjà prêt !

Le provider `ephemeris-api` est déjà créé dans `natal-providers.js`, il suffit de configurer l'URL !

---

## 📊 COMPARAISON RAILWAY VS RENDER

| Critère | Railway | Render |
|---------|---------|--------|
| **Plan gratuit** | $5/mois de crédit | 750h/mois |
| **Setup** | CLI simple | UI simple |
| **Déploiement** | Instantané | ~5 min |
| **Logs** | Temps réel ✅ | Temps réel ✅ |
| **Custom domain** | ✅ | ✅ |
| **Sleep/Wake** | Toujours actif | Sleep après inactivité |

**Recommandation** : **Railway** (plus simple, toujours actif)

---

## 🧪 TESTER L'API DÉPLOYÉE

### Test simple

```bash
curl -X POST https://[ton-url].railway.app/calc \
  -H 'Content-Type: application/json' \
  -d '{
    "year": 1989,
    "month": 11,
    "day": 1,
    "hour": 17.333,
    "latitude": -3.1316333,
    "longitude": -59.9825041,
    "houses": "Placidus"
  }'
```

### Résultat attendu

```json
{
  "sun": { "longitude": 219.xxx, "sign": "Scorpion", ... },
  "moon": { "longitude": 253.xxx, "sign": "Sagittaire", ... },
  "ascendant": { "longitude": 329.xxx, "sign": "Verseau", ... },
  ...
}
```

---

## 💰 COÛTS RÉELS

### Railway
```
Plan gratuit : $5 crédit/mois
Consommation : ~$0.50-2/mois (pour une API légère)
Coût réel : $0 (dans la limite gratuite)
```

### Render
```
Plan gratuit : 750h/mois
Consommation : 730h/mois (toujours actif)
Coût réel : $0
Sleep/Wake : Peut dormir après inactivité
```

**Les deux sont GRATUITS pour ton usage !** ✅

---

## 📈 COMPARAISON FINALE

| Solution | Coût/an | Précision | Setup | Gratuit ? |
|----------|---------|-----------|-------|-----------|
| **ephemeris-api + Railway** | **$0** | **Parfaite** | **5 min** | **OUI** ✅ |
| PROKERALA | $144 | Parfaite | 5 min | Non |
| AstrologyAPI | $588-1188 | Parfaite | 5 min | Non |
| LOCAL | $0 | Mauvaise | 0 min | Oui |

---

## 🎯 PROCHAINES ÉTAPES

### Maintenant (5 minutes)

1. **Installer Railway CLI** :
   ```bash
   brew install railway
   ```

2. **Déployer ephemeris-api** :
   ```bash
   cd /Users/remibeaurain/astroia/ephemeris-api
   railway login
   railway init
   railway up
   railway domain
   ```

3. **Configurer dans Vercel** :
   ```bash
   EPHEMERIS_API_URL=https://[ton-url].railway.app
   NATAL_PROVIDER=ephemeris-api
   ```

4. **Tester dans l'app** → Précision parfaite ! ✅

---

## 📚 RESSOURCES

- **Repo GitHub** : https://github.com/astrolin/ephemeris-api
- **Railway** : https://railway.app
- **Render** : https://render.com
- **Guide Railway** : https://docs.railway.app/deploy/deployments

---

## ✨ RÉSUMÉ

✅ **ephemeris-api** : API Swiss Ephemeris complète  
✅ **Railway/Render** : Hébergement gratuit  
✅ **Setup** : 5 minutes  
✅ **Coût** : $0  
✅ **Précision** : Professionnelle  
✅ **Économie** : $588-1188/an vs AstrologyAPI  

**C'EST LA SOLUTION PARFAITE ! Gratuite, précise, et facile à déployer !** 🎉

---

**Date** : 2025-11-07  
**Status** : ✅ READY TO DEPLOY

