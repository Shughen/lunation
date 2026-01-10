# 🌟 Configuration AstrologyAPI v3 - Astro.IA

**Date:** 5 novembre 2025  
**API:** AstrologyAPI Western Astrology  
**Plan recommandé:** Sapphire ($99/mois)

---

## 📋 ÉTAPES DE CONFIGURATION

### 1. Créer un compte AstrologyAPI

1. **Aller sur** https://astrologyapi.com
2. **S'inscrire** (email + password)
3. **Choisir le plan Sapphire** ($99/mois)
   - 100,000 appels API/mois
   - Western + Vedic Astrology
   - Support prioritaire
   - Pas de rate limiting

### 2. Récupérer les credentials

Après inscription, aller dans **Dashboard > API Keys** :

```
User ID: 123456
API Key: abc123def456...
```

### 3. Configurer dans Vercel

**Variables d'environnement à ajouter :**

```bash
ASTROLOGY_API_USER_ID=123456
ASTROLOGY_API_KEY=abc123def456...
```

**Via Vercel CLI :**
```bash
cd /Users/remibeaurain/astroia/astro-ia-api

vercel env add ASTROLOGY_API_USER_ID
# Coller le User ID

vercel env add ASTROLOGY_API_KEY
# Coller l'API Key
```

**Via Vercel Dashboard :**
1. Aller sur https://vercel.com/[votre-projet]/settings/environment-variables
2. Ajouter `ASTROLOGY_API_USER_ID` (production + preview + development)
3. Ajouter `ASTROLOGY_API_KEY` (production + preview + development)
4. Redéployer : `vercel --prod`

### 4. Tester l'endpoint

```bash
curl -X POST https://[votre-projet].vercel.app/api/astro/natal-astrologyapi \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1989-04-15",
    "time": "17:55",
    "lat": 48.917335,
    "lon": 2.5298854,
    "tz": 1.0
  }'
```

**Réponse attendue :**
```json
{
  "chart": {
    "sun": {
      "sign": "Bélier",
      "emoji": "♈",
      "element": "Feu",
      "degree": 25,
      "minutes": 44
    },
    "moon": {
      "sign": "Lion",
      "emoji": "♌",
      "element": "Feu",
      "degree": 26,
      "minutes": 47
    },
    "ascendant": {
      "sign": "Cancer",
      "emoji": "♋",
      "element": "Eau",
      "degree": 19,
      "minutes": 29
    }
  },
  "meta": {
    "version": "AstrologyAPI v3",
    "precision": "professional",
    "source": "Swiss Ephemeris"
  }
}
```

---

## 🔧 INTÉGRATION DANS L'APP MOBILE

### Mise à jour du natalService

**Fichier:** `astroia-app/lib/api/natalService.js`

**Changement:**
```javascript
// Remplacer l'URL de l'API
const NATAL_URL = `${API_BASE}/api/astro/natal-astrologyapi`;

// Pas besoin de changer le reste, l'interface est la même !
```

### Mise à jour de app.json

**Ajouter l'URL de l'API :**
```json
{
  "extra": {
    "natalApiUrl": "https://[votre-projet].vercel.app/api/astro/natal-astrologyapi"
  }
}
```

---

## 💰 PRICING

### Plan Sapphire ($99/mois)

**Inclus :**
- 100,000 appels API/mois
- Toutes les fonctionnalités Western Astrology
- Support prioritaire
- Pas de rate limiting
- Accès API Vedic (bonus)

**Usage estimé Astro.IA :**
- 1000 utilisateurs actifs/mois
- 2-3 calculs de thème natal par utilisateur
- ~3,000 appels/mois
- **3% du quota** → Largement suffisant !

**Coût par thème natal :** $0.03 (3 centimes)

### Alternatives

**Plan Diamond ($49/mois)** - 50,000 appels
- Suffisant pour MVP (<1500 utilisateurs)

**Plan Premium ($199/mois)** - 200,000 appels
- Pour scale rapide (2000+ utilisateurs)

---

## 🚀 DÉPLOIEMENT

### 1. Créer la fonction Vercel

```bash
cd /Users/remibeaurain/astroia/astro-ia-api

# Le fichier est déjà créé : api/astro/natal-astrologyapi.js
```

### 2. Configurer les variables d'environnement

```bash
vercel env add ASTROLOGY_API_USER_ID
vercel env add ASTROLOGY_API_KEY
```

### 3. Déployer

```bash
vercel --prod
```

### 4. Tester

```bash
curl -X POST https://[URL].vercel.app/api/astro/natal-astrologyapi \
  -H "Content-Type: application/json" \
  -d '{"date":"1989-04-15","time":"17:55","lat":48.917335,"lon":2.5298854,"tz":1.0}'
```

### 5. Mettre à jour l'app mobile

**app.json :**
```json
"natalApiUrl": "https://[URL].vercel.app/api/astro/natal-astrologyapi"
```

**natalService.js :**
```javascript
const NATAL_URL = Constants.expoConfig?.extra?.natalApiUrl;
```

---

## 🎯 AVANTAGES ASTROLOGYAPI

### vs API actuelle

| Critère | API Actuelle | AstrologyAPI v3 |
|---------|-------------|-----------------|
| **Précision** | ⚠️ Approximative | ✅ Professionnelle |
| **Ascendant** | ⚠️ ±10° | ✅ Précis |
| **Maisons** | ❌ Non | ✅ 12 maisons |
| **Aspects** | ❌ Non | ✅ Complets |
| **Latence** | ~1-2s | ~300-500ms |
| **Fiabilité** | ⚠️ Variable | ✅ 99.9% uptime |
| **Support** | ❌ Aucun | ✅ Prioritaire |

### Features additionnelles

**Disponibles avec AstrologyAPI :**
- ✅ Aspects planétaires (trigone, carré, opposition...)
- ✅ 12 maisons astrologiques
- ✅ Rétrogradations
- ✅ Dignités planétaires
- ✅ Points fictifs (Nœuds lunaires, Lilith...)
- ✅ Progressions et transits

**Utilisables pour futures features !**

---

## 🔒 SÉCURITÉ

### Best Practices

**✅ Stockage des credentials :**
- Variables d'environnement Vercel (chiffrées)
- Jamais dans le code source
- Jamais dans le client mobile

**✅ Authentification :**
- Basic Auth côté serveur uniquement
- Client mobile → Vercel → AstrologyAPI
- Pas d'exposition des clés API

**✅ Caching :**
- Thèmes natals immuables (date/heure/lieu fixes)
- Cache Supabase : TTL 1 an
- Réduire les appels API → Économies

---

## 📊 MONITORING

### Vérifier l'usage

**Dashboard AstrologyAPI :**
- Connexion à https://astrologyapi.com/dashboard
- Voir les métriques en temps réel
- Alertes si quota dépassé

**Logs Vercel :**
```bash
vercel logs --prod
```

**Filtrer les appels AstrologyAPI :**
```bash
vercel logs --prod | grep "AstrologyAPI"
```

---

## 🐛 TROUBLESHOOTING

### Erreur 401 Unauthorized

**Cause :** Credentials invalides

**Solution :**
```bash
# Vérifier les variables
vercel env ls

# Reconfigurer si nécessaire
vercel env rm ASTROLOGY_API_KEY
vercel env add ASTROLOGY_API_KEY
vercel --prod
```

### Erreur 429 Too Many Requests

**Cause :** Quota dépassé

**Solution :**
- Vérifier le dashboard AstrologyAPI
- Upgrader le plan si nécessaire
- Implémenter du caching agressif

### Erreur 500 Internal Server Error

**Cause :** Payload invalide ou erreur serveur

**Solution :**
- Vérifier les logs : `vercel logs --prod`
- Valider le format de la requête
- Contacter le support AstrologyAPI

---

## 📚 RESSOURCES

- [Documentation AstrologyAPI](https://astrologyapi.com/western-api-docs)
- [Pricing](https://astrologyapi.com/pricing)
- [Western Chart Data](https://www.astrologyapi.com/western-api-docs/api-ref/163/western_chart_data)
- [Natal Chart Interpretation](https://www.astrologyapi.com/western-api-docs/api-ref/192/natal_chart_interpretation)

---

## ✅ CHECKLIST DÉPLOIEMENT

- [ ] Compte AstrologyAPI créé
- [ ] Plan Sapphire souscrit ($99/mois)
- [ ] User ID + API Key récupérés
- [ ] Variables Vercel configurées
- [ ] Fonction `natal-astrologyapi.js` créée
- [ ] Déployé sur Vercel
- [ ] Testé avec curl
- [ ] `app.json` mis à jour
- [ ] `natalService.js` mis à jour
- [ ] App mobile testée
- [ ] Caching Supabase implémenté

---

**Prêt pour un thème natal professionnel ! 🌟**

