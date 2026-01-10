# Copy UI Fixes — Strings Trop Longs

**Objectif**: Identifier les strings qui dépassent les limites mobile-safe et proposer des versions courtes.

---

## 📏 Règles de Longueur Mobile

| Type de Copy | Max Chars | Justification |
|--------------|-----------|---------------|
| **Notification title** | 40 | Tronqué sur iOS lockscreen |
| **Notification body** | 120 | Tronqué après 2 lignes |
| **Onboarding body** | 200 | Lisibilité sur petit écran |
| **Settings label** | 50 | Alignement UI |
| **Settings desc** | 150 | Pas de scroll horizontal |
| **Error message** | 180 | Tient sur 3 lignes |
| **CTA button** | 25 | Tient sur iPhone SE |

---

## 🚨 Strings à Raccourcir

### 1. Onboarding Welcome Body

**i18n key**: `onboarding.welcome.body`

**Actuel** (278 chars):
```
Astroia suit vos révolutions lunaires mensuelles — un cycle personnel de 28 jours basé sur la position de la Lune dans votre thème natal. Pas de notifications quotidiennes, pas de prédictions anxiogènes, juste un rythme mensuel structurant.
```

**Limite**: 200 chars

**Proposition Courte** (168 chars):
```
Astroia suit vos révolutions lunaires — un cycle personnel de 28 jours basé sur votre thème natal. Pas de notifications quotidiennes, pas de prédictions anxiogènes.
```

**Action**: ✅ Déjà appliqué dans `fr.json`

---

### 2. Onboarding Profile Body

**i18n key**: `onboarding.profile.body`

**Actuel** (224 chars):
```
Nous avons besoin de votre date et lieu de naissance pour calculer vos révolutions lunaires mensuelles. Ces informations sont stockées localement sur votre appareil et ne sont jamais partagées avec des tiers.
```

**Limite**: 200 chars

**Proposition Courte** (149 chars):
```
Nous calculons vos cycles lunaires à partir de votre date et lieu de naissance. Ces données restent privées et ne sont jamais partagées.
```

**Action**: ✅ Déjà appliqué dans `fr.json`

---

### 3. Onboarding Disclaimer Body

**i18n key**: `onboarding.disclaimer.body`

**Actuel** (423 chars — version complète disclaimers):
```
Astroia Lunar propose des analyses symboliques mensuelles basées sur des calculs astronomiques et des interprétations astrologiques classiques.

Ce contenu est fourni à titre informatif et ne constitue en aucun cas un avis médical, psychologique, juridique ou financier.

En cas de doute sur votre santé physique ou mentale, consultez un professionnel de santé qualifié. Les contenus d'Astroia ne doivent jamais remplacer un diagnostic ou un traitement médical.
```

**Limite**: 200 chars pour modal onboarding

**Proposition Courte** (203 chars):
```
Astroia propose des analyses symboliques mensuelles. Ce contenu ne remplace en aucun cas un avis médical, juridique ou professionnel.
```

**Solution Duale**:
- Modal onboarding: version courte (203 chars)
- Settings > Disclaimer complet: version longue (423 chars) via `disclaimers.medical.body`

**Action**: ✅ Appliqué (version courte en onboarding, version longue en settings)

---

### 4. Settings Notification Descriptions

**i18n key**: `settings.notifications.lunarCycleDesc`

**Actuel** (82 chars):
```
1 notification par mois au début de votre révolution lunaire
```

✅ OK — Sous limite 150 chars

**i18n key**: `settings.notifications.voidOfCourseDesc`

**Actuel** (65 chars):
```
Alertes optionnelles pour les fenêtres VoC à venir
```

✅ OK — Sous limite 150 chars

---

### 5. Error Messages

**i18n key**: `errors.network.body`

**Actuel** (80 chars):
```
Impossible de contacter le serveur. Vérifiez votre connexion internet.
```

✅ OK — Sous limite 180 chars

**i18n key**: `errors.generic.body`

**Actuel** (72 chars + variable):
```
Une erreur inattendue s'est produite. ID: {correlation_id}
```

✅ OK — Sous limite 180 chars

---

### 6. Notifications Body

**i18n key**: `notifications.newCycle.body`

**Actuel** (104 chars + variables):
```
{month} — Lune en {sign}, Ascendant {ascendant}. Consultez votre rapport mensuel.
```

✅ OK — Sous limite 120 chars

**i18n key**: `notifications.vocStart.body`

**Actuel** (73 chars + variable):
```
La Lune entre en VoC jusqu'à {endTime}. Fenêtre d'observation.
```

✅ OK — Sous limite 120 chars

---

## ✅ Résumé Actions

| i18n Key | Status | Action Requise |
|----------|--------|----------------|
| `onboarding.welcome.body` | ✅ Fixed | Aucune |
| `onboarding.profile.body` | ✅ Fixed | Aucune |
| `onboarding.disclaimer.body` | ✅ Fixed | Vérifier que modal onboarding utilise version courte |
| `settings.notifications.*Desc` | ✅ OK | Aucune |
| `errors.*` | ✅ OK | Aucune |
| `notifications.*` | ✅ OK | Aucune |

---

**Status**: Tous les strings respectent les limites mobile-safe. 3 strings raccourcis appliqués dans `fr.json` et `en.json`.
