# QA Code-Path Check - Notifications & Empty States

**Version:** 1.0  
**Format:** Tableau de référence rapide pour vérification code avant tests

---

## 📋 Tableau: Test → Steps → Expected → Where in Code

| Test | Étape | Attendu | Fichier / Section | Commande Vérification |
|------|-------|---------|-------------------|----------------------|
| **TEST 1: Empty State** | Affichage empty state | Titre + body + CTA depuis i18n | `apps/mobile/app/index.tsx:465-477` | `grep -n "emptyStates.noCycles" apps/mobile/app/index.tsx` |
| | Condition empty state | `!currentLunarReturn` ou `currentLunarReturn === null` | `apps/mobile/app/index.tsx:435-477` | `grep -B 5 -A 10 "currentLunarReturn.*null\|!currentLunarReturn" apps/mobile/app/index.tsx` |
| | Traductions FR | `emptyStates.noCycles.title` et `.body` | `apps/mobile/i18n/fr.json:79-83` | `grep -A 3 '"noCycles"' apps/mobile/i18n/fr.json` |
| | Traductions EN | `emptyStates.noCycles.title` et `.body` | `apps/mobile/i18n/en.json:79-83` | `grep -A 3 '"noCycles"' apps/mobile/i18n/en.json` |
| | CTA génération | `handleGenerate()` → `lunarReturns.generate()` | `apps/mobile/app/index.tsx:340-351` | `grep -A 15 "handleGenerate" apps/mobile/app/index.tsx` |
| | Rechargement après génération | `loadCurrentLunarReturn()` appelé après succès | `apps/mobile/app/index.tsx:344-345` | `grep -A 5 "lunarReturns.generate" apps/mobile/app/index.tsx` |
| | i18n initialisé | Import `i18n` dans `_layout.tsx` | `apps/mobile/app/_layout.tsx:10` | `grep -n "i18n" apps/mobile/app/_layout.tsx` |
| **TEST 2: Permission Refusée** | Toggle OFF par défaut | `notificationsEnabled: false` initial | `apps/mobile/stores/useNotificationsStore.ts:32` | `grep -n "notificationsEnabled.*false" apps/mobile/stores/useNotificationsStore.ts` |
| | Demande permission | `requestNotificationPermissions()` appelée | `apps/mobile/stores/useNotificationsStore.ts:55` | `grep -A 10 "requestNotificationPermissions" apps/mobile/stores/useNotificationsStore.ts` |
| | Gestion refus | Check `finalStatus !== 'granted'` | `apps/mobile/services/notificationScheduler.ts:55-58` | `grep -A 5 "finalStatus.*granted" apps/mobile/services/notificationScheduler.ts` |
| | Message erreur | Alert avec "Permission requise" | `apps/mobile/stores/useNotificationsStore.ts:58-59` | `grep -r "Permission requise\|permissionRequired" apps/mobile` |
| | Traductions message | `settings.notifications.permissionRequired` | `apps/mobile/i18n/fr.json:61-64` | `grep -A 3 '"permissionRequired"' apps/mobile/i18n/fr.json` |
| | Bouton Settings | `Linking.openSettings()` ou équivalent | Rechercher dans composant Settings | `grep -r "openSettings\|Linking.open" apps/mobile` |
| | Toggle reste OFF | `set({ notificationsEnabled: false })` après refus | `apps/mobile/stores/useNotificationsStore.ts:59` | `grep -A 5 "Permission refusée" apps/mobile/stores/useNotificationsStore.ts` |
| **TEST 3: Permission Acceptée** | Permission accordée | `finalStatus === 'granted'` | `apps/mobile/services/notificationScheduler.ts:70-71` | `grep -A 3 "Permission accordée" apps/mobile/services/notificationScheduler.ts` |
| | Sauvegarde préférence | `AsyncStorage.setItem('notifications_enabled', 'true')` | `apps/mobile/stores/useNotificationsStore.ts:63` | `grep -A 2 "NOTIFICATIONS_ENABLED.*true" apps/mobile/stores/useNotificationsStore.ts` |
| | Toggle passe ON | `set({ notificationsEnabled: true })` | `apps/mobile/stores/useNotificationsStore.ts:64` | `grep -A 2 "notificationsEnabled.*true" apps/mobile/stores/useNotificationsStore.ts` |
| | Scheduling automatique | `scheduleAllNotifications()` appelé | `apps/mobile/stores/useNotificationsStore.ts:67` | `grep -A 5 "scheduleAllNotifications" apps/mobile/stores/useNotificationsStore.ts` |
| | Message succès | Alert "Notifications activées" | Rechercher dans UI Settings | `grep -r "enabledSuccess\|Notifications activées" apps/mobile` |
| | Traductions succès | `settings.notifications.enabledSuccess` | `apps/mobile/i18n/fr.json:64` | `grep -A 1 '"enabledSuccess"' apps/mobile/i18n/fr.json` |
| | Mark scheduled | `markScheduled()` appelé après scheduling | `apps/mobile/stores/useNotificationsStore.ts:134` | `grep -A 2 "markScheduled" apps/mobile/stores/useNotificationsStore.ts` |
| **TEST 4: VoC Start** | Scheduling VoC | `scheduleVocNotifications()` appelé | `apps/mobile/stores/useNotificationsStore.ts:109` | `grep -A 5 "scheduleVocNotifications" apps/mobile/stores/useNotificationsStore.ts` |
| | Notification VoC Start | Scheduling avec titre i18n | `apps/mobile/services/notificationScheduler.ts:111-123` | `grep -A 12 "vocStart.title" apps/mobile/services/notificationScheduler.ts` |
| | Traductions VoC Start | `notifications.vocStart.title` et `.body` | `apps/mobile/i18n/fr.json:119-122` | `grep -A 3 '"vocStart"' apps/mobile/i18n/fr.json` |
| | Data payload | `data: { type: 'voc_start', screen: '/lunar/voc' }` | `apps/mobile/services/notificationScheduler.ts:115` | `grep -A 2 "'voc_start'" apps/mobile/services/notificationScheduler.ts` |
| | Deep link listener | `setupNotificationTapListener()` dans index.tsx | `apps/mobile/app/index.tsx:242-249` | `grep -A 8 "setupNotificationTapListener" apps/mobile/app/index.tsx` |
| | Navigation deep link | `router.push(screen)` dans listener | `apps/mobile/app/index.tsx:245` | `grep -A 3 "onNotificationTap.*router.push" apps/mobile/app/index.tsx` |
| | Route /lunar/voc | Fichier `app/lunar/voc.tsx` existe | `apps/mobile/app/lunar/voc.tsx` | `ls apps/mobile/app/lunar/voc.tsx` |
| | i18n dans scheduler | Import `i18n` dans `notificationScheduler.ts` | `apps/mobile/services/notificationScheduler.ts:15` | `grep -n "i18n" apps/mobile/services/notificationScheduler.ts` |
| **TEST 5: VoC End** | Calcul 30min avant | `endDate.getTime() - 30 * 60 * 1000` | `apps/mobile/services/notificationScheduler.ts:127` | `grep -A 5 "30.*60.*1000" apps/mobile/services/notificationScheduler.ts` |
| | Notification VoC End | Scheduling avec titre i18n | `apps/mobile/services/notificationScheduler.ts:131-143` | `grep -A 12 "vocEnd.title" apps/mobile/services/notificationScheduler.ts` |
| | Traductions VoC End | `notifications.vocEnd.title` et `.body` | `apps/mobile/i18n/fr.json:123-126` | `grep -A 3 '"vocEnd"' apps/mobile/i18n/fr.json` |
| | Data payload | `data: { type: 'voc_end_soon', screen: '/lunar/voc' }` | `apps/mobile/services/notificationScheduler.ts:135` | `grep -A 2 "'voc_end_soon'" apps/mobile/services/notificationScheduler.ts` |
| | Condition scheduling | `endTrigger > 0 && endWarning > now` | `apps/mobile/services/notificationScheduler.ts:130` | `grep -A 2 "endTrigger.*0\|endWarning.*now" apps/mobile/services/notificationScheduler.ts` |
| **TEST 6: Nouveau Cycle** | Scheduling cycle | `scheduleLunarCycleNotification()` appelé | `apps/mobile/stores/useNotificationsStore.ts:123` | `grep -A 5 "scheduleLunarCycleNotification" apps/mobile/stores/useNotificationsStore.ts` |
| | Check cycle commencé | `hoursSinceStart > 24` → skip | `apps/mobile/services/notificationScheduler.ts:163-167` | `grep -A 5 "hoursSinceStart.*24" apps/mobile/services/notificationScheduler.ts` |
| | Notification cycle | Scheduling avec titre i18n | `apps/mobile/services/notificationScheduler.ts:181-196` | `grep -A 15 "newCycle.title" apps/mobile/services/notificationScheduler.ts` |
| | Interpolation variables | `i18n.t('notifications.newCycle.body', { month, sign, ascendant })` | `apps/mobile/services/notificationScheduler.ts:184-188` | `grep -A 8 "newCycle.body" apps/mobile/services/notificationScheduler.ts` |
| | Traductions cycle | `notifications.newCycle.title` et `.body` | `apps/mobile/i18n/fr.json:115-118` | `grep -A 3 '"newCycle"' apps/mobile/i18n/fr.json` |
| | Data payload | `data: { type: 'lunar_cycle_start', screen: '/lunar/report' }` | `apps/mobile/services/notificationScheduler.ts:189` | `grep -A 2 "'lunar_cycle_start'" apps/mobile/services/notificationScheduler.ts` |
| | Route /lunar/report | Fichier `app/lunar/report.tsx` existe | `apps/mobile/app/lunar/report.tsx` | `ls apps/mobile/app/lunar/report.tsx` |

---

## 🔴 Points de Risque Critiques

### 1. i18n Non Initialisé
**Risque:** Strings hardcodés ou erreurs `i18n is not defined`  
**Fichiers à vérifier:**
- `apps/mobile/app/_layout.tsx:10` → Import `import '../i18n';`
- `apps/mobile/services/notificationScheduler.ts:15` → Import `import i18n from '../i18n';`
- Composant Settings → Vérifier import i18n si message affiché

**Commande:**
```bash
grep -r "i18n" apps/mobile/app/_layout.tsx apps/mobile/services/notificationScheduler.ts
```

### 2. Empty State Condition Incorrecte
**Risque:** Empty state non affiché ou affiché quand cycle existe  
**Fichiers à vérifier:**
- `apps/mobile/app/index.tsx:435` → Condition `!currentLunarReturn` ou `currentLunarReturn === null`
- Vérifier que `currentLunarReturn` est bien `null` initialement (pas `undefined`)

**Commande:**
```bash
grep -B 5 -A 10 "currentLunarReturn.*null\|!currentLunarReturn" apps/mobile/app/index.tsx
```

### 3. Deep Link Listener Non Initialisé
**Risque:** Tap notification non détecté, pas de navigation  
**Fichiers à vérifier:**
- `apps/mobile/app/index.tsx:242-249` → `useEffect` avec `setupNotificationTapListener()`
- Vérifier que subscription n'est pas supprimée trop tôt (return dans useEffect)

**Commande:**
```bash
grep -A 10 "setupNotificationTapListener" apps/mobile/app/index.tsx
```

### 4. Permission Demandée au Lancement
**Risque:** Violation UX (demande intrusive)  
**Fichiers à vérifier:**
- `apps/mobile/app/index.tsx` → Pas d'appel à `requestNotificationPermissions()` au mount
- `apps/mobile/app/_layout.tsx` → Pas d'appel au lancement
- Uniquement dans Settings → Toggle activé

**Commande:**
```bash
grep -r "requestNotificationPermissions" apps/mobile/app/index.tsx apps/mobile/app/_layout.tsx
# Ne devrait PAS apparaître dans index.tsx ou _layout.tsx
```

### 5. Toggle ON par Défaut
**Risque:** Violation opt-in volontaire  
**Fichiers à vérifier:**
- `apps/mobile/stores/useNotificationsStore.ts:32` → `notificationsEnabled: false` initial
- `apps/mobile/stores/useNotificationsStore.ts:36-43` → `loadPreferences()` lit AsyncStorage (par défaut `null` = false)

**Commande:**
```bash
grep -n "notificationsEnabled.*false\|notificationsEnabled.*true" apps/mobile/stores/useNotificationsStore.ts
```

### 6. Route Deep Link Incorrecte
**Risque:** Navigation vers écran blanc ou erreur 404  
**Fichiers à vérifier:**
- `apps/mobile/services/notificationScheduler.ts:115` → `screen: '/lunar/voc'`
- `apps/mobile/services/notificationScheduler.ts:135` → `screen: '/lunar/voc'`
- `apps/mobile/services/notificationScheduler.ts:189` → `screen: '/lunar/report'`
- Vérifier que fichiers existent:
  - `apps/mobile/app/lunar/voc.tsx`
  - `apps/mobile/app/lunar/report.tsx`

**Commande:**
```bash
grep -n "'/lunar/voc'\|'/lunar/report'" apps/mobile/services/notificationScheduler.ts
ls apps/mobile/app/lunar/voc.tsx apps/mobile/app/lunar/report.tsx
```

### 7. Variables Non Interpolées dans Notification
**Risque:** Body affiche `{month}`, `{sign}` littéraux  
**Fichiers à vérifier:**
- `apps/mobile/services/notificationScheduler.ts:184-188` → `i18n.t('notifications.newCycle.body', { month, sign, ascendant })`
- Vérifier que variables sont définies: `moonInfo`, `ascInfo`

**Commande:**
```bash
grep -A 10 "newCycle.body" apps/mobile/services/notificationScheduler.ts
```

### 8. Scheduling Échoue Silencieusement
**Risque:** Notifications non planifiées sans erreur visible  
**Fichiers à vérifier:**
- `apps/mobile/stores/useNotificationsStore.ts:103-131` → Try/catch avec logs console
- `apps/mobile/services/notificationScheduler.ts` → Logs `console.log` après chaque scheduling

**Commande:**
```bash
grep -A 5 "catch\|console.error\|console.log" apps/mobile/stores/useNotificationsStore.ts apps/mobile/services/notificationScheduler.ts
```

---

## 🛠️ Commandes de Vérification Rapide

### Vérifier Structure Globale
```bash
# 1. Vérifier tous les fichiers clés existent
ls apps/mobile/app/index.tsx \
   apps/mobile/app/lunar/voc.tsx \
   apps/mobile/app/lunar/report.tsx \
   apps/mobile/stores/useNotificationsStore.ts \
   apps/mobile/services/notificationScheduler.ts \
   apps/mobile/i18n/fr.json \
   apps/mobile/i18n/en.json

# 2. Vérifier imports i18n
grep -r "from.*i18n\|import.*i18n" apps/mobile/app/_layout.tsx apps/mobile/services/notificationScheduler.ts

# 3. Vérifier routes deep links
grep -o "'/[^']*'" apps/mobile/services/notificationScheduler.ts | sort -u
# Attendu: '/lunar/voc', '/lunar/report'
```

### Vérifier Traductions
```bash
# 1. Vérifier toutes les clés notifications
grep -o '"[^"]*"' apps/mobile/i18n/fr.json | grep -E "vocStart|vocEnd|newCycle|permissionRequired|enabledSuccess|noCycles"

# 2. Vérifier cohérence FR/EN
diff <(grep -o '"[^"]*":' apps/mobile/i18n/fr.json | sort) <(grep -o '"[^"]*":' apps/mobile/i18n/en.json | sort)
```

### Vérifier Logique Notifications
```bash
# 1. Vérifier scheduling automatique après accord
grep -A 3 "scheduleAllNotifications" apps/mobile/stores/useNotificationsStore.ts

# 2. Vérifier gestion refus permission
grep -A 5 "Permission refusée\|finalStatus.*granted" apps/mobile/stores/useNotificationsStore.ts apps/mobile/services/notificationScheduler.ts

# 3. Vérifier deep link listener
grep -A 5 "setupNotificationTapListener\|addNotificationResponseReceivedListener" apps/mobile/app/index.tsx apps/mobile/services/notificationScheduler.ts
```

---

## 📝 Checklist Avant Tests

- [ ] Tous les fichiers clés existent (voir "Vérifier Structure Globale")
- [ ] i18n initialisé dans `_layout.tsx` et `notificationScheduler.ts`
- [ ] Routes deep links existent (`/lunar/voc`, `/lunar/report`)
- [ ] Toggle notifications OFF par défaut
- [ ] Permission demandée uniquement au toggle (pas au lancement)
- [ ] Deep link listener initialisé dans `index.tsx`
- [ ] Variables interpolées dans notification cycle (`{month}`, `{sign}`, `{ascendant}`)
- [ ] Empty state condition correcte (`!currentLunarReturn`)
- [ ] Try/catch avec logs dans scheduling
- [ ] Traductions FR/EN complètes et cohérentes

---

**Fin du Code-Path Check**

