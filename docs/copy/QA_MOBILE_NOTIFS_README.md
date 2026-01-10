# QA Mobile - Notifications & Empty States

**Version:** 1.0  
**Date:** 2025-01-XX  
**Focus:** Empty state "aucun cycle", permissions notifications, 3 notifications + deep links

---

## 📚 Documentation

Ce package QA comprend 3 documents complémentaires:

### 1. **Plan de Tests Manuels** (`QA_MOBILE_NOTIFS_PLAN_DE_TESTS.md`)
- Plan d'exécution détaillé (20-30 min)
- 6 tests avec steps précis, captures, critères de réussite/échec
- Guide pour forcer les scénarios (debug flags, mocks)
- Checklist finale avant validation

**À utiliser:** Pour exécuter les tests manuels sur device.

### 2. **Code-Path Check** (`QA_MOBILE_NOTIFS_CODE_PATH_CHECK.md`)
- Tableau de référence rapide: Test → Steps → Expected → Where in Code
- Points de risque critiques avec commandes de vérification
- Checklist avant tests (vérification code)

**À utiliser:** Pour vérifier le code avant les tests ou investiguer un bug.

### 3. **Checklist Copy Originale** (`QA_COPY_NOTIFS_CHECKLIST.md`)
- Checklist complète (30 scénarios) pour validation copy ADN
- Référence pour validation tone, i18n, fréquence notifications

**À utiliser:** Pour validation copy complète (hors scope focus actuel).

---

## 🎯 Focus Actuel

Les tests ci-dessous sont prioritaires et doivent être validés en premier:

1. ✅ **Empty state "aucun cycle"** (TEST 1)
   - Affichage correct avec i18n
   - CTA fonctionnel pour générer cycles

2. ✅ **Alert permissions notifications** (TEST 2 + TEST 3)
   - Refus bien géré avec message "Permission requise"
   - Accord bien géré avec scheduling automatique

3. ✅ **3 notifications + deep links** (TEST 4 + TEST 5 + TEST 6)
   - VoC Start → `/lunar/voc`
   - VoC End -30min → `/lunar/voc`
   - Nouveau cycle → `/lunar/report`

---

## 🚀 Démarrage Rapide

### Étape 1: Vérifier le Code (5 min)
```bash
# Ouvrir le Code-Path Check
open docs/copy/QA_MOBILE_NOTIFS_CODE_PATH_CHECK.md

# Exécuter les commandes de vérification rapide
cd apps/mobile
grep -r "i18n" app/_layout.tsx services/notificationScheduler.ts
grep -n "notificationsEnabled.*false" stores/useNotificationsStore.ts
ls app/lunar/voc.tsx app/lunar/report.tsx
```

### Étape 2: Exécuter les Tests (20-30 min)
```bash
# Ouvrir le Plan de Tests
open docs/copy/QA_MOBILE_NOTIFS_PLAN_DE_TESTS.md

# Suivre les steps dans l'ordre:
# TEST 1 → TEST 2 → TEST 3 → TEST 4 → TEST 5 → TEST 6
```

### Étape 3: Valider (5 min)
- [ ] Tous les tests passent (6/6)
- [ ] Screenshots capturés
- [ ] Logs vérifiés (pas d'erreurs)
- [ ] Checklist finale validée

---

## 🔧 Outillage Debug

### Forcer les Scénarios

#### Forcer Empty State
```typescript
// Dans Expo DevTools
import AsyncStorage from '@react-native-async-storage/async-storage';
await AsyncStorage.removeItem('lunar_returns_cache'); // si utilisé
// Puis relancer l'app
```

#### Forcer Permission Refusée
```bash
# iOS: Settings → Astroia Lunar → Notifications → OFF
# Android: Paramètres → Applications → Astroia Lunar → Notifications → Désactivées
```

#### Forcer Notification Test (VoC Start)
```typescript
// Dans Expo DevTools
import * as Notifications from 'expo-notifications';
Notifications.scheduleNotificationAsync({
  content: {
    title: "🌑 Void of Course",
    body: "La Lune entre en VoC jusqu'à 14:30. Fenêtre d'observation.",
    data: { type: 'voc_start', screen: '/lunar/voc' },
  },
  trigger: { seconds: 5 },
});
```

#### Forcer Notification Test (Nouveau Cycle)
```typescript
// Dans Expo DevTools
import * as Notifications from 'expo-notifications';
Notifications.scheduleNotificationAsync({
  content: {
    title: "🌙 Nouveau cycle lunaire",
    body: "Janvier 2025 — Lune en Cancer, Ascendant Bélier. Consultez votre rapport mensuel.",
    data: { type: 'lunar_cycle_start', screen: '/lunar/report' },
  },
  trigger: { seconds: 5 },
});
```

---

## 📊 Points Bloquants

Si un des points suivants échoue, la release est **bloquée**:

- ❌ Empty state non affiché (affichage cycle fantôme)
- ❌ Permission demandée au lancement (violation UX)
- ❌ Deep link ne fonctionne pas (navigation échouée)
- ❌ Notification envoyée sans opt-in (toggle ON par défaut)
- ❌ Strings hardcodés (pas depuis i18n)

---

## 📝 Historique des Tests

| Date | Tester | Device | Version | Résultats | Commentaires |
|------|--------|--------|---------|-----------|--------------|
| [À compléter] | [Nom] | [iOS/Android] | [Version] | [6/6] | [Notes] |

---

## 🔗 Liens Utiles

- **Backend API:** `http://localhost:8000` (dev) / [staging URL] (staging)
- **Documentation API:** `docs/API_DOCUMENTATION.md` (si existe)
- **Expo DevTools:** `http://localhost:19002` (si Expo Go)
- **React Native Debugger:** [Instructions si utilisé]

---

**Documentation créée le:** 2025-01-XX  
**Dernière mise à jour:** 2025-01-XX

