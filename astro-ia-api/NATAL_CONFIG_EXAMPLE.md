# 🔧 Configuration des Providers de Thème Natal

## Variables d'environnement

Copier ces variables dans votre fichier `.env` ou dans Vercel Environment Variables.

```bash
# ====== NATAL CHART PROVIDER ======
# Options: local, prokerala, astrologer
# Par défaut: local (gratuit, auto-hébergé)
NATAL_PROVIDER=local

# ====== PROKERALA API (Optionnel) ======
# Plan gratuit: 5000 credits/mois (~$12)
# Documentation: https://api.prokerala.com
# Inscription: https://api.prokerala.com/sign-up
PROKERALA_API_KEY=your_api_key_here
PROKERALA_API_USER=your_user_id_here

# ====== ASTROLOGER API (Optionnel) ======
# Open-source self-hosted
# GitHub: https://github.com/theriftlab/immanuel-python
# Nécessite hébergement sur Render/Fly.io (~$30/mois)
ASTROLOGER_API_URL=https://your-astrologer-instance.com
```

---

## Configuration Vercel (Production)

Dans le dashboard Vercel → Settings → Environment Variables :

| Variable | Value | Description |
|----------|-------|-------------|
| `NATAL_PROVIDER` | `local` | Provider par défaut |
| `PROKERALA_API_KEY` | `(secret)` | Clé API Prokerala (si utilisé) |
| `PROKERALA_API_USER` | `(secret)` | User ID Prokerala (si utilisé) |

---

## Test des Providers

### 1. LOCAL (Default)
```bash
# Aucune configuration requise
curl -X POST https://your-api.vercel.app/api/astro/natal \
  -H 'Content-Type: application/json' \
  -d '{
    "date": "1989-04-15",
    "time": "17:55",
    "lat": 48.919,
    "lon": 2.543
  }'
```

### 2. PROKERALA
```bash
# Ajouter provider dans le body
curl -X POST https://your-api.vercel.app/api/astro/natal \
  -H 'Content-Type: application/json' \
  -d '{
    "date": "1989-04-15",
    "time": "17:55",
    "lat": 48.919,
    "lon": 2.543,
    "provider": "prokerala"
  }'
```

---

## Inscription Prokerala

1. Aller sur https://api.prokerala.com/sign-up
2. Créer un compte
3. Aller dans API Keys section
4. Copier `API Key` et `User ID`
5. Ajouter dans `.env` :
   ```
   PROKERALA_API_KEY=pk_xxx
   PROKERALA_API_USER=usr_xxx
   ```

**Plan gratuit** : 5000 credits/mois (suffisant pour MVP)

---

## Hébergement Astrologer API (Optionnel)

### Option 1 : Render.com
```bash
# 1. Fork le repo GitHub
https://github.com/theriftlab/immanuel-python

# 2. Créer un Web Service sur Render
# 3. Connecter le repo forké
# 4. Deploy (automatique)
# 5. Copier l'URL : https://your-app.onrender.com
```

### Option 2 : Fly.io
```bash
# 1. Installer Fly CLI
brew install flyctl

# 2. Clone le repo
git clone https://github.com/theriftlab/immanuel-python
cd immanuel-python

# 3. Deploy
fly launch
fly deploy

# 4. Copier l'URL : https://your-app.fly.dev
```

**Coût** : ~$30/mois pour hébergement continu

---

## Monitoring

### Vérifier le provider actif
```javascript
// Dans les logs Vercel
console.log(process.env.NATAL_PROVIDER); // 'local'
```

### Vérifier les quotas Prokerala
- Dashboard : https://api.prokerala.com/dashboard
- Credits restants affichés en temps réel

---

## Fallback Strategy

Si un provider échoue, le système rebasculer automatiquement sur LOCAL :

```javascript
try {
  // Essayer le provider configuré (ex: Prokerala)
  return await calculateProkerala(params);
} catch (error) {
  console.warn('[Natal] Provider failed, fallback to local');
  // Rebasculer sur LOCAL
  return await calculateLocal(params);
}
```

**Avantage** : 
- ✅ Service toujours disponible
- ✅ Zéro downtime
- ✅ Résilience maximale

