# 🪐 Guide du Thème Natal - Astro.IA V1

**Date :** 5 novembre 2025  
**Version :** V1-simplified  
**Statut :** ✅ Fonctionnel avec limitations documentées

---

## 🎯 Objectif

Calculer et afficher un thème natal basique avec :
- Position du Soleil (signe solaire)
- Position de la Lune (signe lunaire)
- Ascendant
- Mercure, Vénus, Mars (bonus)

---

## ⚙️ Architecture

```
App Mobile
    ↓
natalService.js
    ↓
Vercel API
    ├── /api/geo/geocode (Nominatim OSM)
    ├── /api/geo/timezone (TimeAPI.io)
    └── /api/astro/natal (Calculs astronomiques)
    ↓
Supabase (natal_charts table)
```

---

## 📊 Limites et approximations V1

### ✅ Ce qui est précis

- **Soleil** : Précision ~1° (excellente pour le signe)
- **Lune** : Précision ~2-3° (bonne pour le signe)
- **Géocodage** : OpenStreetMap (excellent)
- **Timezone** : Détection automatique (fiable)

### ⚠️ Ce qui est approximé

- **Ascendant** : Formule simplifiée (précision ~5-10°)
  - Suffisant pour identifier le signe dans 90% des cas
  - Peut être imprécis aux heures de changement de signe
  
- **Mercure/Vénus/Mars** : Calculs très simplifiés
  - Positions approximatives basées sur le Soleil
  - **À NE PAS** utiliser pour des analyses sérieuses
  - Placeholder pour V2

- **Maisons** : Non calculées en V1
  - Retour : "N/A"
  - Nécessite Swiss Ephemeris pour précision

### 🚫 Ce qui n'est PAS calculé

- Jupiter, Saturne, Uranus, Neptune, Pluton
- Nœuds lunaires
- Chiron, Lilith
- Parts (Part de Fortune, etc.)
- Aspects (conjonctions, oppositions, etc.)
- Maisons astrologiques précises

---

## 🔬 Précision technique

| Élément | Méthode | Précision | Usage |
|---------|---------|-----------|-------|
| **Soleil** | VSOP87 simplifié | ±1° | ✅ Production OK |
| **Lune** | ELP2000 simplifié | ±2-3° | ✅ Production OK |
| **Ascendant** | Temps sidéral local | ±5-10° | ⚠️ Indicatif |
| **Autres planètes** | Estimation | ±10-30° | ❌ Placeholder |

---

## 📝 Format des données

### Request (API /api/astro/natal)

```json
{
  "date": "1990-05-15",
  "time": "14:30",
  "lat": 48.8566,
  "lon": 2.3522,
  "tz": "Europe/Paris"
}
```

### Response

```json
{
  "chart": {
    "sun": {
      "sign": "Taureau",
      "emoji": "♉",
      "element": "Terre",
      "degree": 24,
      "minutes": 15,
      "longitude": 54.25
    },
    "moon": { ... },
    "ascendant": { ... },
    "mercury": { ... },
    "venus": { ... },
    "mars": { ... }
  },
  "meta": {
    "birthDate": "1990-05-15",
    "birthTime": "14:30",
    "location": { "lat": 48.8566, "lon": 2.3522 },
    "timezone": "Europe/Paris",
    "julianDay": 2448023.104,
    "approximation": true,
    "version": "V1-simplified",
    "note": "Calculs simplifiés..."
  },
  "latencyMs": 150
}
```

---

## 🔄 Limite de calcul

### Règle : 1 calcul par 24h

**Pourquoi ?**
- Éviter les abus
- Le thème natal ne change pas
- Économiser les ressources API

**Implémentation :**
- Fonction SQL `can_compute_natal_chart(user_id)`
- Vérification avant chaque calcul
- Message utilisateur clair

**Contournement (dev) :**
```sql
-- Réinitialiser la limite manuellement
DELETE FROM natal_charts WHERE user_id = 'xxx';
```

---

## 🚀 Roadmap V2 (Précision professionnelle)

### Améliorations prioritaires

1. **Swiss Ephemeris** (sweph)
   - Précision : ±0.01° pour toutes les planètes
   - Package : `swisseph` ou `astronomia-pro`
   - Coût : Gratuit (GPL) ou licence commerciale

2. **Maisons Placidus**
   - Calcul précis des 12 maisons
   - Nécessaire pour analyses avancées

3. **Aspects**
   - Conjonctions, oppositions, trigones, etc.
   - Orbes configurables

4. **Planètes lentes**
   - Jupiter, Saturne, Uranus, Neptune, Pluton
   - Important pour l'analyse complète

5. **Transits**
   - Positions actuelles des planètes
   - Comparaison avec le natal

---

## 🧪 Tests de validation

### Test 1 : Signe solaire connu

**Entrée :** 15 mai 1990, 14h30, Paris
**Attendu :** Soleil en Taureau
**Tolérance :** ±1 jour autour des cusps (20-21 avril, 20-21 mai)

### Test 2 : Ascendant approximé

**Entrée :** 15 mai 1990, 14h30, Paris
**Méthode :** Comparer avec un calcul professionnel
**Tolérance V1 :** ±10° acceptable

### Test 3 : Lune

**Entrée :** 15 mai 1990, 14h30, Paris  
**Attendu :** Signe lunaire cohérent
**Tolérance :** ±1 signe

---

## 📚 Ressources

### Calculs astronomiques
- [Astronomia](https://www.npmjs.com/package/astronomia) - Utilisé en V1
- [Swiss Ephemeris](https://www.astro.com/swisseph/) - Pour V2
- [VSOP87](https://en.wikipedia.org/wiki/VSOP_(planets)) - Théorie planétaire

### Astrologie
- [Astro.com](https://www.astro.com) - Référence pour validation
- [AstroDienst](https://www.astrodienst.com) - Calculs professionnels

---

## ⚠️ Avertissement

Cette version V1 est un **MVP fonctionnel** mais **non professionnel**.

- ✅ OK pour : App mobile grand public, découverte, fun
- ❌ PAS OK pour : Consultations professionnelles, analyses approfondies

**Pour usage professionnel**, upgrader vers Swiss Ephemeris obligatoire.

---

## 🆘 Support

### Erreurs courantes

| Erreur | Cause | Solution |
|--------|-------|----------|
| "Lieu introuvable" | Ville mal orthographiée | Essayer "Ville, Pays" |
| "Limite dépassée" | Déjà calculé aujourd'hui | Attendre 24h |
| "Profil requis" | Profil incomplet | Compléter le profil |
| "Erreur timezone" | API indisponible | Fallback UTC activé |

---

**Thème Natal V1 prêt ! Pour V2 professionnelle : Swiss Ephemeris** 🌟

*Mis à jour : 5 novembre 2025*

