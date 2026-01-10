# 🌟 Guide des Providers de Thème Natal

## Architecture Modulaire V3

Ce système permet de basculer facilement entre plusieurs sources de calcul de thème natal, en suivant les recommandations de ChatGPT Research.

---

## 📋 **Providers Disponibles**

### 1. **LOCAL (V2-Enhanced)** ⭐ **Par défaut**

**Caractéristiques** :
- ✅ **Gratuit** : $0/mois
- ✅ **Auto-hébergé** : Aucune dépendance externe
- ✅ **Précision** :
  - Soleil : ±1 minute d'arc (VSOP87)
  - Lune : ±10 minutes d'arc (ELP2000)
  - Ascendant : ±1 degré (Jean Meeus)
- ✅ **Latence** : ~50-100ms
- ✅ **Illimité** : Pas de quotas

**Utilisation** :
```bash
# Aucune configuration requise - provider par défaut
NATAL_PROVIDER=local
```

**Idéal pour** :
- MVP / Prototype
- Développement
- Usage illimité sans coûts
- Précision suffisante pour l'astrologie grand public

---

### 2. **PROKERALA API** 💎

**Caractéristiques** :
- ✅ **Plan gratuit** : 5000 credits/mois (~₹1000/mois = $12/mois)
- ✅ **Précision professionnelle** : Swiss Ephemeris
- ✅ **Support** : Vedic + Western astrology
- ✅ **Latence** : ~200-400ms
- ⚠️ **Quotas** : 5000 calculs/mois (plan gratuit)

**Configuration** :
```bash
# Dans .env
NATAL_PROVIDER=prokerala
PROKERALA_API_KEY=your_api_key
PROKERALA_API_USER=your_user_id
```

**Documentation** :
- Site : https://api.prokerala.com
- Pricing : https://api.prokerala.com/pricing
- Free Plan : 5000 credits/mois

**Idéal pour** :
- Production avec précision maximale
- Budget limité mais besoin de qualité professionnelle
- Backup du provider local

---

### 3. **ASTROLOGER API (GitHub Open-Source)** 🔓

**Caractéristiques** :
- ✅ **Open-source** : AGPLv3
- ✅ **Gratuit si auto-hébergé** : ~$30/mois (serveur Render/Fly.io)
- ✅ **Précision professionnelle** : Swiss Ephemeris
- ✅ **Contrôle total** : Personnalisable à volonté
- ⚠️ **Setup complexe** : Nécessite hébergement + maintenance

**Configuration** :
```bash
# Dans .env
NATAL_PROVIDER=astrologer
ASTROLOGER_API_URL=https://your-astrologer-instance.com
```

**Repository** :
- GitHub : https://github.com/theriftlab/immanuel-python
- Alternative : https://github.com/g-battaglia/Astrologer-API

**Idéal pour** :
- Production à long terme
- Autonomie complète
- Économies de coûts si grand volume

---

## 🚀 **Configuration**

### Méthode 1 : Variable d'environnement (Global)

```bash
# Dans .env ou Vercel Environment Variables
NATAL_PROVIDER=local  # ou 'prokerala', 'astrologer'

# Si Prokerala :
PROKERALA_API_KEY=your_key
PROKERALA_API_USER=your_user

# Si Astrologer :
ASTROLOGER_API_URL=https://your-instance.com
```

### Méthode 2 : Paramètre par requête (Flexible)

```javascript
// Dans votre code client
const response = await fetch('/api/astro/natal', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    date: '1989-04-15',
    time: '17:55',
    lat: 48.919,
    lon: 2.543,
    tz: 'Europe/Paris',
    provider: 'prokerala', // Override le provider par défaut
  }),
});
```

---

## 📊 **Comparaison des Providers**

| Critère | LOCAL | PROKERALA | ASTROLOGER |
|---------|-------|-----------|------------|
| **Coût/mois** | $0 | $12 (5000 calls) | $30 (hébergement) |
| **Précision** | Bonne (±1') | Excellente (Swiss Eph) | Excellente (Swiss Eph) |
| **Latence** | 50-100ms | 200-400ms | 300-800ms (cold start) |
| **Quotas** | Illimité | 5000/mois | Illimité |
| **Setup** | Aucun ✅ | API Key ⚠️ | Hébergement ❌ |
| **Maintenance** | Aucune ✅ | Aucune ✅ | Requise ⚠️ |
| **Autonomie** | Total ✅ | Dépendance externe | Total ✅ |
| **Open-source** | Oui ✅ | Non ❌ | Oui ✅ |

---

## 🎯 **Recommandations**

### Phase 1 : MVP (Maintenant)
```
Provider : LOCAL
Coût : $0
Durée : 0-6 mois
```

**Pourquoi** :
- Zéro configuration
- Zéro coûts
- Précision suffisante pour MVP
- Déploiement immédiat

---

### Phase 2 : Production avec volume limité (6-12 mois)
```
Provider : PROKERALA
Coût : $12/mois (5000 calculs)
Durée : 6-12 mois
```

**Pourquoi** :
- Précision professionnelle
- Coût très faible
- Pas de maintenance
- Backup avec LOCAL si quotas dépassés

**Fallback** :
```javascript
// Automatiquement rebasculer sur LOCAL si erreur ou quotas dépassés
try {
  return await calculateProkerala(params);
} catch (error) {
  console.warn('[Natal] Prokerala failed, fallback to local');
  return await calculateLocal(params);
}
```

---

### Phase 3 : Scale & Autonomie (12+ mois)
```
Provider : ASTROLOGER (auto-hébergé)
Coût : $30/mois (serveur)
Durée : Long-terme
```

**Pourquoi** :
- Zéro dépendance externe
- Coûts fixes prévisibles
- Illimité
- Contrôle total

---

## 🔄 **Roadmap de Migration**

### Étape 1 : Maintenant (Semaine 1)
- ✅ Utiliser **LOCAL** par défaut
- ✅ Architecture modulaire en place
- ✅ Tests fonctionnels

### Étape 2 : Court terme (Mois 1-6)
- 🎯 Tester **PROKERALA** avec quelques utilisateurs
- 🎯 Comparer précision LOCAL vs PROKERALA
- 🎯 Implémenter fallback automatique
- 🎯 Monitorer quotas et coûts

### Étape 3 : Moyen terme (Mois 6-12)
- 🎯 Si volume > 5000/mois : préparer migration ASTROLOGER
- 🎯 Héberger instance ASTROLOGER sur Render/Fly.io
- 🎯 Tester en parallèle

### Étape 4 : Long terme (Mois 12+)
- 🎯 Migrer 100% vers ASTROLOGER auto-hébergé
- 🎯 Sunset PROKERALA (économies)
- 🎯 Garder LOCAL comme backup

---

## 🧪 **Tests**

### Tester le provider local
```bash
curl -X POST http://localhost:3000/api/astro/natal \
  -H 'Content-Type: application/json' \
  -d '{
    "date": "1989-04-15",
    "time": "17:55",
    "lat": 48.919,
    "lon": 2.543,
    "tz": "Europe/Paris"
  }'
```

### Tester Prokerala (avec API key)
```bash
curl -X POST http://localhost:3000/api/astro/natal \
  -H 'Content-Type: application/json' \
  -d '{
    "date": "1989-04-15",
    "time": "17:55",
    "lat": 48.919,
    "lon": 2.543,
    "tz": "Europe/Paris",
    "provider": "prokerala"
  }'
```

---

## 💰 **Estimation de Coûts**

### Scénario 1 : Startup (0-1000 utilisateurs)
```
Calculs/mois : ~2000
Provider : LOCAL
Coût : $0
```

### Scénario 2 : Croissance (1000-5000 utilisateurs)
```
Calculs/mois : ~4000
Provider : PROKERALA (plan gratuit)
Coût : $12/mois
Fallback : LOCAL (si quotas dépassés)
```

### Scénario 3 : Scale (5000+ utilisateurs)
```
Calculs/mois : 10,000+
Provider : ASTROLOGER (auto-hébergé)
Coût : $30/mois (serveur) + $0/calcul
ROI : Économies dès 10k calculs/mois
```

---

## 📚 **Ressources**

### Documentation APIs
- **Prokerala** : https://api.prokerala.com/docs
- **Astrologer (Immanuel)** : https://github.com/theriftlab/immanuel-python
- **Swiss Ephemeris** : https://www.astro.com/swisseph/

### Formules astronomiques (LOCAL)
- **VSOP87** (Soleil) : https://en.wikipedia.org/wiki/VSOP_(planets)
- **ELP2000** (Lune) : https://en.wikipedia.org/wiki/ELP2000-82B
- **Jean Meeus** (Ascendant) : Astronomical Algorithms (livre de référence)

---

## 🚨 **Troubleshooting**

### Erreur : "PROKERALA_API_KEY required"
**Solution** : Ajouter la clé API dans `.env` ou utiliser LOCAL par défaut

### Erreur : "Prokerala API error: 429"
**Solution** : Quotas dépassés, passer à LOCAL ou upgrade plan Prokerala

### Erreur : "ASTROLOGER_API_URL unreachable"
**Solution** : Vérifier que l'instance Astrologer est bien hébergée et accessible

### Latence élevée (>2s)
**Solution** : Utiliser LOCAL (50-100ms) ou mettre en cache les résultats dans Supabase

---

## 🎓 **Best Practices**

1. **Toujours avoir LOCAL comme fallback**
2. **Cacher les résultats dans Supabase** (thèmes natals immuables)
3. **Monitorer les quotas Prokerala** pour éviter surprises
4. **Tester la migration Astrologer en parallèle** avant de basculer
5. **Documenter les différences de précision** pour les utilisateurs

---

**Créé le** : 2025-11-07  
**Version** : 3.0  
**Statut** : Production-ready

