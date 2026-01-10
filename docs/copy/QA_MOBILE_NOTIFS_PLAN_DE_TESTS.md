# Plan de Tests QA Mobile - Notifications & Empty States

**Version:** 1.0  
**Durée estimée:** 20-30 minutes  
**Device:** iOS/Android (device réel recommandé)  
**Focus:** Empty state "aucun cycle", permissions notifications, 3 types de notifications + deep links

---

## 🎯 Prérequis

### Setup Device
- [ ] App installée via Expo Go ou build de développement
- [ ] Backend API accessible (localhost ou staging)
- [ ] Mode debug activé (`__DEV__ = true`)
- [ ] i18n français activé (`fr.json`)
- [ ] AsyncStorage accessible pour reset

### Outils de Debug
- [ ] Console logs accessibles (Expo DevTools ou React Native Debugger)
- [ ] Device logs activés (iOS: Console.app, Android: `adb logcat`)
- [ ] Screenshot tool activé (iOS: ⌘+Shift+4, Android: Power+Vol Down)
- [ ] Accès aux Settings système (Notifications)

### Flags de Debug Disponibles
```typescript
// Dans stores/useNotificationsStore.ts
// Forcer re-scheduling immédiatement (bypass 24h)
await AsyncStorage.removeItem('notifications_last_scheduled_at');

// Forcer empty state (supprimer cycles générés)
await AsyncStorage.removeItem('lunar_returns'); // si stocké localement
// OU: Ne pas appeler l'API de génération

// Simuler permission refusée
// Dans notificationScheduler.ts, modifier temporairement:
// return false; // dans requestNotificationPermissions()
```

---

## ✅ TEST 1: Empty State "Aucun Cycle"

### Objectif
Valider l'affichage et le comportement de l'empty state quand aucun cycle lunaire n'est généré.

### Steps

1. **Préparer l'environnement**
   ```bash
   # Option 1: Reset AsyncStorage (si cycles stockés localement)
   # Via DevTools: AsyncStorage.clear() ou reset app
   
   # Option 2: S'assurer qu'aucun cycle n'est généré côté backend
   # OU: Compte utilisateur sans cycles générés
   ```

2. **Ouvrir l'app**
   - Lancer l'app depuis le home screen
   - Attendre que l'écran Home (`/`) se charge
   - **Capture:** Screenshot de l'écran Home complet

3. **Observer l'empty state**
   - Vérifier que la section "Mon Cycle Actuel" affiche l'empty state
   - **Attendu:**
     - Titre: "Aucune révolution lunaire générée" (ou traduction depuis `emptyStates.noCycles.title`)
     - Body: "Générez vos 12 prochains cycles mensuels..." (ou `emptyStates.noCycles.body`)
     - CTA: Bouton "Générer mes cycles" visible et cliquable
   - **Capture:** Screenshot de la carte "Mon Cycle Actuel" avec empty state

4. **Tester le CTA**
   - Taper sur "Générer mes cycles"
   - **Attendu:**
     - Loader affiché (bouton disabled)
     - Appel API `POST /api/lunar-returns/generate` visible dans logs
     - Après succès: Alert "Révolutions lunaires générées avec succès ! ✨"
     - Rechargement de la carte avec cycle actuel affiché
   - **Capture:** Screenshot du loader, puis du cycle généré

5. **Vérifier i18n**
   - Changer la langue de l'app (Settings système → Langue → English)
   - Relancer l'app
   - **Attendu:**
     - Titre: "No Lunar Returns Generated" (depuis `en.json`)
     - Body: "Generate your next 12 monthly cycles..." (depuis `en.json`)
     - CTA: "Generate My Cycles"
   - **Capture:** Screenshot avec langue anglaise

### Critères de Réussite ✅
- [ ] Empty state affiché correctement (titre + body + CTA)
- [ ] Strings proviennent de `i18n/fr.json` et `i18n/en.json`
- [ ] CTA génère les cycles et recharge l'affichage
- [ ] Pas d'erreur console lors de l'affichage de l'empty state
- [ ] Layout responsive (pas de débordement texte sur petit écran)

### Critères d'Échec ❌
- [ ] Empty state non affiché (cycle fantôme affiché à la place)
- [ ] Strings hardcodés (pas depuis i18n)
- [ ] CTA ne fonctionne pas ou génère une erreur
- [ ] Texte tronqué ou débordement visuel
- [ ] Erreur console: `Cannot read property 'return_date' of null`

### Fichiers à Vérifier (Code-Path Check)

```bash
# 1. Empty state rendering
grep -n "emptyStates.noCycles" apps/mobile/app/index.tsx
# Attendu: ligne ~468 avec t('emptyStates.noCycles.title')

# 2. Traductions
grep -A 3 '"noCycles"' apps/mobile/i18n/fr.json
grep -A 3 '"noCycles"' apps/mobile/i18n/en.json

# 3. Condition d'affichage
grep -B 5 -A 10 "emptyText\|noCycles\|currentLunarReturn" apps/mobile/app/index.tsx
# Attendu: condition !currentLunarReturn ou currentLunarReturn === null

# 4. Fonction handleGenerate
grep -A 15 "handleGenerate" apps/mobile/app/index.tsx
# Attendu: Appel à lunarReturns.generate() puis rechargement
```

### Points de Risque 🔴
- **i18n pas initialisé** avant affichage → Vérifier que `i18n` est importé dans `_layout.tsx`
- **Condition empty state incorrecte** → Vérifier que `currentLunarReturn` est bien `null` et pas `undefined`
- **Carte non rechargée après génération** → Vérifier `loadCurrentLunarReturn()` appelé après `handleGenerate()`
- **Erreur API non gérée** → Vérifier try/catch dans `handleGenerate()`

### Commandes Debug Utiles

```bash
# Vérifier que l'API retourne bien 404 pour cycles non générés
curl -X GET "http://localhost:8000/api/lunar-returns/current" \
  -H "Authorization: Bearer <token>" \
  -H "X-Dev-User-Id: 1" # si DEV_AUTH_BYPASS

# Vérifier AsyncStorage (via DevTools)
AsyncStorage.getItem('lunar_returns_cache') // si utilisé

# Logs console
grep "empty.*cycle\|noCycles\|handleGenerate" <device_logs>
```

---

## ✅ TEST 2: Alert Permissions Notifications (Refusée)

### Objectif
Valider le comportement quand l'utilisateur refuse la permission système pour les notifications.

### Steps

1. **Préparer l'environnement**
   - Révoquer la permission notifications dans Settings système (si déjà accordée)
   - Settings iOS: Réglages → Astroia Lunar → Notifications → OFF
   - Settings Android: Paramètres → Applications → Astroia Lunar → Notifications → Désactivées
   - **Capture:** Screenshot des Settings système

2. **Ouvrir l'app et naviguer vers Settings**
   - Lancer l'app
   - Taper sur l'icône Settings (⚙️) ou naviguer vers `/settings`
   - **Attendu:** Écran Settings affiché
   - **Capture:** Screenshot de l'écran Settings

3. **Tester le toggle "Nouveau cycle lunaire"**
   - Localiser le toggle "Nouveau cycle lunaire" (section Notifications)
   - Vérifier que le toggle est **OFF** par défaut
   - Taper sur le toggle pour l'activer
   - **Attendu:**
     - Popup système iOS: "Astroia Lunar aimerait vous envoyer des notifications"
     - Popup Android: "Autoriser les notifications?"
     - **Capture:** Screenshot du popup système

4. **Refuser la permission**
   - Taper sur "Ne pas autoriser" (iOS) ou "Refuser" (Android)
   - **Attendu:**
     - Popup système se ferme
     - Toggle reste OFF (ou revient à OFF)
     - Alert/message affiché: "Permission requise" + "Ouvrir les réglages" (depuis `settings.notifications.permissionRequired`)
     - **Capture:** Screenshot de l'alert/message

5. **Tester le bouton "Ouvrir les réglages"**
   - Taper sur "Ouvrir les réglages"
   - **Attendu:**
     - Redirection vers Settings système → Notifications → Astroia Lunar
     - iOS: `Linking.openSettings()` ouvre les réglages app
     - Android: Redirection vers la page notifications de l'app
   - **Capture:** Screenshot des Settings système ouverts

6. **Vérifier le message d'erreur**
   - Revenir à l'app (sans activer la permission)
   - Observer le message/alert affiché
   - **Attendu:**
     - Message: "Permission requise" (depuis `settings.notifications.permissionRequired`)
     - Description: "Autorisez les notifications dans les réglages système." (depuis `settings.notifications.permissionDesc`)
     - Bouton: "Ouvrir les réglages" (depuis `settings.notifications.openSettings`)
   - **Capture:** Screenshot du message final

### Critères de Réussite ✅
- [ ] Toggle OFF par défaut (opt-in volontaire)
- [ ] Popup système affiché lors du toggle ON
- [ ] Refus bien géré (toggle reste OFF ou revient OFF)
- [ ] Message "Permission requise" affiché avec bouton Settings
- [ ] Bouton "Ouvrir les réglages" redirige vers Settings système
- [ ] Strings proviennent de i18n (`settings.notifications.*`)

### Critères d'Échec ❌
- [ ] Toggle ON par défaut (violation opt-in)
- [ ] Popup système non affiché
- [ ] Refus non géré (app crash ou état incohérent)
- [ ] Message d'erreur hardcodé (pas depuis i18n)
- [ ] Bouton Settings ne fonctionne pas
- [ ] Permission demandée au lancement de l'app (violation UX)

### Fichiers à Vérifier (Code-Path Check)

```bash
# 1. Store notifications
grep -A 20 "setNotificationsEnabled" apps/mobile/stores/useNotificationsStore.ts
# Attendu: Appel à requestNotificationPermissions() puis gestion du refus

# 2. Service permissions
grep -A 15 "requestNotificationPermissions" apps/mobile/services/notificationScheduler.ts
# Attendu: Notifications.requestPermissionsAsync() puis check finalStatus !== 'granted'

# 3. UI Settings (si écran dédié existe)
find apps/mobile -name "*settings*" -o -name "*notification*" | grep -i screen
# Vérifier affichage du message "Permission requise"

# 4. Traductions
grep -A 5 '"permissionRequired"\|"permissionDesc"\|"openSettings"' apps/mobile/i18n/fr.json

# 5. Linking vers Settings
grep -r "openSettings\|Linking.open" apps/mobile
# Attendu: Utilisation de Linking.openSettings() (iOS/Android)
```

### Points de Risque 🔴
- **i18n pas initialisé** avant affichage du message → Vérifier import i18n dans composant Settings
- **Permission déjà accordée** → Vérifier `getPermissionsAsync()` avant de demander
- **Linking.openSettings() non disponible** → Vérifier import depuis `react-native` ou `expo-linking`
- **Toggle reste ON après refus** → Vérifier que `setNotificationsEnabled(false)` est appelé en cas de refus
- **Message d'erreur non affiché** → Vérifier Alert.alert() ou Toast dans le code après refus

### Commandes Debug Utiles

```bash
# Vérifier statut permission (via Expo DevTools)
# Dans console:
import * as Notifications from 'expo-notifications';
Notifications.getPermissionsAsync().then(console.log);

# Logs console
grep "Permission refusée\|Permission denied\|requestPermission" <device_logs>

# Vérifier AsyncStorage
AsyncStorage.getItem('notifications_permission') // devrait être null ou 'denied'
```

---

## ✅ TEST 3: Alert Permissions Notifications (Acceptée)

### Objectif
Valider le comportement quand l'utilisateur accorde la permission système pour les notifications.

### Steps

1. **Préparer l'environnement**
   - S'assurer que la permission est refusée (voir TEST 2)
   - OU: Révoquer la permission dans Settings système

2. **Ouvrir l'app et naviguer vers Settings**
   - Lancer l'app
   - Naviguer vers `/settings`
   - Localiser le toggle "Nouveau cycle lunaire"

3. **Activer le toggle**
   - Taper sur le toggle pour l'activer
   - Popup système affiché

4. **Accorder la permission**
   - Taper sur "Autoriser" (iOS) ou "Autoriser" (Android)
   - **Attendu:**
     - Popup système se ferme
     - Toggle passe à ON
     - Message de succès: "Notifications activées" (depuis `settings.notifications.enabledSuccess`)
     - Console log: `[Notifications] ✅ Permission accordée`
     - Console log: `[NotificationsStore] ✅ Notifications activées`
     - Console log: `[NotificationsStore] Début scheduling...`
   - **Capture:** Screenshot du toggle ON + message de succès

5. **Vérifier le scheduling automatique**
   - Attendre 2-3 secondes
   - **Attendu:**
     - Console log: `[NotificationsStore] ✅ Scheduling terminé`
     - AsyncStorage: `notifications_enabled = 'true'`
     - AsyncStorage: `notifications_last_scheduled_at` présent
   - **Vérification:** DevTools → AsyncStorage → `notifications_enabled`

6. **Vérifier que les notifications sont schedulées**
   - Console: `[Notifications] ✅ X notifications VoC schedulées`
   - Console: `[Notifications] ✅ Notification cycle lunaire schedulée` (si cycle en cours)
   - **Vérification (optionnel):** Device Settings → Notifications → Voir les notifications planifiées

7. **Vérifier i18n**
   - Changer la langue → English
   - Relancer l'app
   - Naviguer vers Settings
   - **Attendu:**
     - Message: "Notifications enabled" (depuis `en.json`)
     - Toggle labels en anglais

### Critères de Réussite ✅
- [ ] Permission accordée correctement (toggle ON)
- [ ] Message de succès affiché (depuis i18n)
- [ ] Scheduling automatique déclenché après accord
- [ ] AsyncStorage mis à jour (`notifications_enabled = 'true'`)
- [ ] Logs console cohérents (permission accordée + scheduling)
- [ ] Toggle reste ON après redémarrage de l'app

### Critères d'Échec ❌
- [ ] Toggle ne passe pas à ON après accord
- [ ] Message de succès non affiché
- [ ] Scheduling non déclenché automatiquement
- [ ] AsyncStorage non mis à jour
- [ ] Erreur console lors du scheduling
- [ ] Toggle revient à OFF après redémarrage

### Fichiers à Vérifier (Code-Path Check)

```bash
# 1. Flow complet après accord
grep -A 30 "if.*finalStatus.*granted" apps/mobile/services/notificationScheduler.ts
# Attendu: return true après accord

# 2. Store: sauvegarde préférence
grep -A 10 "AsyncStorage.setItem.*NOTIFICATIONS_ENABLED" apps/mobile/stores/useNotificationsStore.ts
# Attendu: Sauvegarde 'true' puis appel scheduleAllNotifications()

# 3. Scheduling automatique
grep -A 20 "scheduleAllNotifications" apps/mobile/stores/useNotificationsStore.ts
# Attendu: Appel API VoC + cycle lunaire puis markScheduled()

# 4. Message de succès
grep -r "enabledSuccess\|Notifications activées" apps/mobile
# Attendu: Affichage via Alert.alert() ou Toast

# 5. Traductions
grep -A 2 '"enabledSuccess"' apps/mobile/i18n/fr.json
```

### Points de Risque 🔴
- **Scheduling déclenché avant sauvegarde AsyncStorage** → Vérifier ordre: save → schedule
- **i18n pas initialisé** avant affichage message → Vérifier import i18n
- **API VoC/Cycle non disponible** → Vérifier try/catch dans `scheduleAllNotifications()`
- **Permission accordée mais toggle reste OFF** → Vérifier `set({ notificationsEnabled: true })`
- **Scheduling échoue silencieusement** → Vérifier logs console pour erreurs

### Commandes Debug Utiles

```bash
# Vérifier permissions (via Expo DevTools)
import * as Notifications from 'expo-notifications';
Notifications.getPermissionsAsync().then(console.log);
# Attendu: { status: 'granted', ... }

# Vérifier AsyncStorage
AsyncStorage.getItem('notifications_enabled') // devrait être 'true'
AsyncStorage.getItem('notifications_last_scheduled_at') // devrait être timestamp ISO

# Vérifier notifications schedulées (iOS Simulator)
# Settings → Notifications → Voir notifications planifiées

# Logs console
grep "Permission accordée\|Notifications activées\|Scheduling terminé" <device_logs>
```

---

## ✅ TEST 4: Notification "VoC Start" + Deep Link

### Objectif
Valider la réception de la notification "VoC Start" et la navigation via deep link vers `/lunar/voc`.

### Steps

1. **Préparer l'environnement**
   - Permission notifications accordée (voir TEST 3)
   - Toggle "Void of Course" activé dans Settings (si option séparée)
   - S'assurer qu'une fenêtre VoC est à venir dans les prochaines 2-48h
   - OU: Forcer une fenêtre VoC via debug (voir "Forcer les Scénarios" ci-dessous)

2. **Scheduler la notification (si nécessaire)**
   - Ouvrir Settings → Notifications → Désactiver puis réactiver le toggle
   - OU: Relancer l'app (re-scheduling automatique si >24h)
   - **Attendu:**
     - Console log: `[Notifications] ✅ X notifications VoC schedulées`
     - Notification planifiée dans le futur

3. **Forcer la notification (debug)**
   ```typescript
   // Option 1: Modifier temporairement le trigger dans notificationScheduler.ts
   // Dans scheduleVocNotifications(), changer:
   trigger: {
     type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
     seconds: 10, // Au lieu de Math.floor(startTrigger / 1000)
   }
   
   // Option 2: Via Expo DevTools
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

4. **Recevoir la notification**
   - Attendre la notification (ou utiliser le trigger forcé ci-dessus)
   - App en background ou fermée
   - **Attendu:**
     - Notification affichée avec:
       - Titre: "🌑 Void of Course" (depuis `notifications.vocStart.title`)
       - Body: "La Lune entre en VoC jusqu'à {endTime}. Fenêtre d'observation." (depuis `notifications.vocStart.body`)
       - Son activé (si configuré)
   - **Capture:** Screenshot de la notification système

5. **Tester le deep link (app fermée)**
   - Fermer complètement l'app (swipe up depuis recent apps)
   - Recevoir la notification (ou déclencher manuellement)
   - Taper sur la notification
   - **Attendu:**
     - App s'ouvre
     - Navigation vers `/lunar/voc` (écran Void of Course)
     - Écran VoC affiché avec statut actuel (VoC actif ou prochain)
     - Console log: `[Notifications] Tap notification → /lunar/voc`
     - Console log: `[INDEX] Tap notification → /lunar/voc`
   - **Capture:** Screenshot de l'écran VoC ouvert depuis la notification

6. **Tester le deep link (app en background)**
   - Mettre l'app en background (Home button)
   - Recevoir la notification
   - Taper sur la notification
   - **Attendu:**
     - App repasse au premier plan
     - Navigation vers `/lunar/voc`
     - Écran VoC affiché
   - **Capture:** Screenshot de la navigation

7. **Vérifier le contenu de l'écran VoC**
   - Observer l'écran `/lunar/voc`
   - **Attendu:**
     - Badge "VoC actif" ou "Pas de VoC" visible
     - Fenêtre VoC actuelle affichée (si active)
     - Liste des prochaines fenêtres VoC visible
   - **Capture:** Screenshot de l'écran VoC complet

8. **Vérifier i18n**
   - Changer la langue → English
   - Relancer l'app et re-scheduler la notification
   - **Attendu:**
     - Titre: "🌑 Void of Course" (identique)
     - Body: "Moon enters VoC until {endTime}. Observation window." (depuis `en.json`)

### Critères de Réussite ✅
- [ ] Notification reçue avec titre et body corrects (depuis i18n)
- [ ] Deep link fonctionne depuis app fermée
- [ ] Deep link fonctionne depuis app en background
- [ ] Navigation vers `/lunar/voc` réussie
- [ ] Écran VoC affiché correctement
- [ ] Logs console cohérents (tap notification → route)

### Critères d'Échec ❌
- [ ] Notification non reçue
- [ ] Notification reçue mais titre/body incorrects
- [ ] Deep link ne fonctionne pas (app ne s'ouvre pas ou mauvaise route)
- [ ] Navigation vers écran blanc ou erreur 404
- [ ] Écran VoC non chargé ou erreur API
- [ ] Deep link fonctionne mais route incorrecte (ex: `/` au lieu de `/lunar/voc`)

### Fichiers à Vérifier (Code-Path Check)

```bash
# 1. Scheduling VoC notifications
grep -A 20 "scheduleVocNotifications" apps/mobile/services/notificationScheduler.ts
# Attendu: Scheduling avec data: { type: 'voc_start', screen: '/lunar/voc' }

# 2. Deep link listener
grep -A 10 "setupNotificationTapListener" apps/mobile/services/notificationScheduler.ts
# Attendu: addNotificationResponseReceivedListener avec extraction data.screen

# 3. Setup listener dans app
grep -A 10 "setupNotificationTapListener" apps/mobile/app/index.tsx
# Attendu: useEffect avec subscription et router.push(screen)

# 4. Traductions
grep -A 2 '"vocStart"' apps/mobile/i18n/fr.json
grep -A 2 '"vocStart"' apps/mobile/i18n/en.json

# 5. Route /lunar/voc
ls apps/mobile/app/lunar/voc.tsx
# Vérifier que le fichier existe et est accessible
```

### Points de Risque 🔴
- **Deep link listener pas initialisé** → Vérifier `setupNotificationTapListener()` appelé dans `index.tsx` (useEffect)
- **Route `/lunar/voc` n'existe pas** → Vérifier fichier `app/lunar/voc.tsx` présent
- **i18n pas initialisé** avant scheduling → Vérifier import i18n dans `notificationScheduler.ts`
- **Data payload incorrect** → Vérifier `data: { screen: '/lunar/voc' }` dans le scheduling
- **Router.push() échoue** → Vérifier que router est disponible au moment du tap
- **Notification reçue mais tap non détecté** → Vérifier subscription active (pas supprimée trop tôt)

### Commandes Debug Utiles

```bash
# Vérifier notifications schedulées (via Expo DevTools)
import * as Notifications from 'expo-notifications';
Notifications.getAllScheduledNotificationsAsync().then(console.log);
# Attendu: Array avec notifications VoC contenant data.screen = '/lunar/voc'

# Logs console
grep "Tap notification\|voc_start\|setupNotificationTapListener" <device_logs>

# Vérifier route
grep -r "'/lunar/voc'\|/lunar/voc" apps/mobile/app
# Attendu: Fichier app/lunar/voc.tsx existe
```

### Forcer les Scénarios (Debug)

```typescript
// 1. Forcer une fenêtre VoC future (mock API)
// Dans app/index.tsx ou notificationScheduler.ts, ajouter temporairement:
const mockVocWindow = {
  start_at: new Date(Date.now() + 60000).toISOString(), // +1 min
  end_at: new Date(Date.now() + 120000).toISOString(), // +2 min
};

// 2. Forcer scheduling immédiat
await scheduleVocNotifications([mockVocWindow]);

// 3. Forcer notification test (Expo DevTools)
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

---

## ✅ TEST 5: Notification "VoC End -30min" + Deep Link

### Objectif
Valider la réception de la notification "VoC End" (30 min avant fin) et la navigation via deep link.

### Steps

1. **Préparer l'environnement**
   - Permission notifications accordée
   - Toggle VoC activé
   - S'assurer qu'une fenêtre VoC se termine dans >30min
   - OU: Forcer via debug (voir ci-dessous)

2. **Scheduler la notification**
   - Réactiver le toggle ou relancer l'app
   - **Attendu:**
     - Console log: `[Notifications] ✅ X notifications VoC schedulées`
     - Notification "VoC End" planifiée 30min avant la fin de la fenêtre

3. **Forcer la notification (debug)**
   ```typescript
   // Modifier temporairement dans scheduleVocNotifications():
   const endWarning = new Date(endDate.getTime() - 30 * 60 * 1000);
   // Remplacer par:
   const endWarning = new Date(Date.now() + 10000); // +10 sec pour test
   
   // OU via Expo DevTools:
   import * as Notifications from 'expo-notifications';
   Notifications.scheduleNotificationAsync({
     content: {
       title: "🌑 Fin du VoC dans 30 min",
       body: "La Lune quitte le Void of Course à 14:30.",
       data: { type: 'voc_end_soon', screen: '/lunar/voc' },
     },
     trigger: { seconds: 5 },
   });
   ```

4. **Recevoir la notification**
   - Attendre la notification (ou utiliser le trigger forcé)
   - **Attendu:**
     - Titre: "🌑 Fin du VoC dans 30 min" (depuis `notifications.vocEnd.title`)
     - Body: "La Lune quitte le Void of Course à {endTime}." (depuis `notifications.vocEnd.body`)
   - **Capture:** Screenshot de la notification

5. **Tester le deep link**
   - Taper sur la notification (app fermée ou background)
   - **Attendu:**
     - Navigation vers `/lunar/voc`
     - Écran VoC affiché
   - **Capture:** Screenshot de l'écran VoC

6. **Vérifier le timing**
   - Observer l'heure de la notification vs heure de fin VoC
   - **Attendu:**
     - Notification reçue exactement 30min avant la fin (ou à quelques secondes près)
     - Body affiche l'heure de fin correcte

### Critères de Réussite ✅
- [ ] Notification reçue 30min avant la fin de VoC
- [ ] Titre et body corrects (depuis i18n)
- [ ] Deep link fonctionne vers `/lunar/voc`
- [ ] Timing précis (30min ± quelques secondes)

### Critères d'Échec ❌
- [ ] Notification non reçue
- [ ] Notification reçue à un mauvais moment (pas 30min avant)
- [ ] Titre/body incorrects
- [ ] Deep link ne fonctionne pas

### Fichiers à Vérifier (Code-Path Check)

```bash
# 1. Scheduling VoC End
grep -A 15 "30.*60.*1000\|endWarning\|voc_end_soon" apps/mobile/services/notificationScheduler.ts
# Attendu: Calcul endWarning = endDate - 30min puis scheduling

# 2. Traductions
grep -A 2 '"vocEnd"' apps/mobile/i18n/fr.json

# 3. Data payload
grep -A 5 '"voc_end_soon"' apps/mobile/services/notificationScheduler.ts
# Attendu: data: { type: 'voc_end_soon', screen: '/lunar/voc' }
```

### Points de Risque 🔴
- **Timing incorrect** → Vérifier calcul: `endDate.getTime() - 30 * 60 * 1000`
- **Notification pas schedulée si <30min** → Vérifier condition `endTrigger > 0 && endWarning > now`
- **Double notification** → Vérifier qu'une seule notification "end" est schedulée par fenêtre

---

## ✅ TEST 6: Notification "Nouveau Cycle Lunaire" + Deep Link

### Objectif
Valider la réception de la notification "Nouveau Cycle Lunaire" et la navigation vers `/lunar/report`.

### Steps

1. **Préparer l'environnement**
   - Permission notifications accordée
   - Toggle "Nouveau cycle lunaire" activé
   - S'assurer qu'un cycle lunaire est généré et commence dans le futur
   - OU: Forcer via debug (voir ci-dessous)

2. **Scheduler la notification**
   - Réactiver le toggle ou relancer l'app
   - **Attendu:**
     - Console log: `[Notifications] ✅ Notification cycle lunaire schedulée`
     - Notification planifiée au début du cycle (return_date)

3. **Forcer la notification (debug)**
   ```typescript
   // Modifier temporairement dans scheduleLunarCycleNotification():
   // Remplacer cycleStart par:
   const cycleStart = new Date(Date.now() + 10000); // +10 sec pour test
   
   // OU via Expo DevTools:
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

4. **Recevoir la notification**
   - Attendre la notification (ou utiliser le trigger forcé)
   - **Attendu:**
     - Titre: "🌙 Nouveau cycle lunaire" (depuis `notifications.newCycle.title`)
     - Body: "{month} — Lune en {sign}, Ascendant {ascendant}. Consultez votre rapport mensuel." (depuis `notifications.newCycle.body`)
     - Variables interpolées: {month}, {sign}, {ascendant} remplis
   - **Capture:** Screenshot de la notification

5. **Tester le deep link**
   - Taper sur la notification (app fermée ou background)
   - **Attendu:**
     - Navigation vers `/lunar/report` (rapport du cycle actuel)
     - Écran Rapport Lunaire affiché avec:
       - Mois du cycle
       - Lune en {sign}
       - Ascendant {ascendant}
       - Interprétation complète
   - **Capture:** Screenshot de l'écran Rapport

6. **Vérifier le contenu du rapport**
   - Observer l'écran `/lunar/report`
   - **Attendu:**
     - Rapport complet du cycle actuel affiché
     - Pas d'erreur 404 ou "Cycle non trouvé"
     - Données cohérentes avec la notification (signe, ascendant)

7. **Vérifier i18n**
   - Changer la langue → English
   - Relancer et re-scheduler
   - **Attendu:**
     - Titre: "🌙 New Lunar Cycle"
     - Body: "{month} — Moon in {sign}, Ascendant {ascendant}. View your monthly report."

### Critères de Réussite ✅
- [ ] Notification reçue au début du cycle (return_date)
- [ ] Titre et body corrects avec variables interpolées
- [ ] Deep link fonctionne vers `/lunar/report`
- [ ] Écran Rapport affiché correctement
- [ ] Pas de notification si cycle déjà commencé (>24h)

### Critères d'Échec ❌
- [ ] Notification non reçue
- [ ] Notification reçue à un mauvais moment
- [ ] Variables non interpolées dans le body ({month}, {sign} littéraux)
- [ ] Deep link ne fonctionne pas
- [ ] Écran Rapport non chargé ou erreur 404
- [ ] Notification envoyée même si cycle déjà commencé

### Fichiers à Vérifier (Code-Path Check)

```bash
# 1. Scheduling cycle lunaire
grep -A 30 "scheduleLunarCycleNotification" apps/mobile/services/notificationScheduler.ts
# Attendu: Vérification hoursSinceStart > 24, puis scheduling avec trigger = return_date

# 2. Interpolation variables
grep -A 10 "notifications.newCycle.body" apps/mobile/services/notificationScheduler.ts
# Attendu: i18n.t('notifications.newCycle.body', { month, sign, ascendant })

# 3. Deep link
grep -A 5 "'lunar_cycle_start'\|'/lunar/report'" apps/mobile/services/notificationScheduler.ts
# Attendu: data: { type: 'lunar_cycle_start', screen: '/lunar/report' }

# 4. Route /lunar/report
ls apps/mobile/app/lunar/report.tsx
# Vérifier que le fichier existe

# 5. Traductions
grep -A 2 '"newCycle"' apps/mobile/i18n/fr.json
```

### Points de Risque 🔴
- **Variables non interpolées** → Vérifier `i18n.t('notifications.newCycle.body', { month, sign, ascendant })`
- **Cycle déjà commencé** → Vérifier condition `hoursSinceStart > 24` pour skip
- **Route `/lunar/report` incorrecte** → Vérifier fichier `app/lunar/report.tsx` présent
- **Rapport non chargé** → Vérifier API `/api/lunar-returns/current` appelée correctement
- **i18n pas initialisé** → Vérifier import i18n dans `notificationScheduler.ts`

### Commandes Debug Utiles

```bash
# Vérifier cycle lunaire actuel
curl -X GET "http://localhost:8000/api/lunar-returns/current" \
  -H "Authorization: Bearer <token>"
# Attendu: { return_date: "2025-01-15T...", moon_sign: "Cancer", ... }

# Vérifier notifications schedulées
import * as Notifications from 'expo-notifications';
Notifications.getAllScheduledNotificationsAsync().then(console.log);
# Attendu: Notification avec data.screen = '/lunar/report'

# Logs console
grep "cycle lunaire\|lunar_cycle_start\|Notification cycle" <device_logs>
```

---

## 📊 Checklist Finale

### Avant de Valider ✅
- [ ] Tous les tests passent (6/6)
- [ ] Screenshots capturés pour chaque test
- [ ] Logs console vérifiés (pas d'erreurs)
- [ ] i18n validé (FR + EN)
- [ ] Deep links fonctionnent (3/3)
- [ ] Permissions gérées correctement (refus + accord)
- [ ] Empty state affiché correctement
- [ ] Timing notifications vérifié (VoC start/end, cycle lunaire)

### Points Bloquants ❌
Si un des points suivants échoue, la release est **bloquée**:
- [ ] Empty state non affiché (affichage cycle fantôme)
- [ ] Permission demandée au lancement (violation UX)
- [ ] Deep link ne fonctionne pas (navigation échouée)
- [ ] Notification envoyée sans opt-in (toggle ON par défaut)
- [ ] Strings hardcodés (pas depuis i18n)

### Points Non-Bloquants ⚠️
Ces points peuvent être corrigés en post-release:
- [ ] Message d'erreur légèrement imprécis (mais fonctionnel)
- [ ] Timing notification à ±1min près (acceptable)
- [ ] Layout responsive sur très petits écrans (edge case)

---

## 🔧 Outillage Debug Additionnel (Optionnel)

### Script Helper pour Forcer les Scénarios

Créer un fichier `apps/mobile/utils/debugNotifications.ts`:

```typescript
/**
 * Helpers de debug pour forcer les scénarios de tests
 * Utiliser uniquement en mode __DEV__
 */

import * as Notifications from 'expo-notifications';
import { scheduleVocNotifications, scheduleLunarCycleNotification } from '../services/notificationScheduler';
import { VocWindow, LunarReturn } from '../services/notificationScheduler';

export async function forceVocStartNotification(secondsDelay: number = 10): Promise<void> {
  if (!__DEV__) return;
  
  const mockWindow: VocWindow = {
    start_at: new Date(Date.now() + secondsDelay * 1000).toISOString(),
    end_at: new Date(Date.now() + (secondsDelay + 60) * 1000).toISOString(),
  };
  
  await scheduleVocNotifications([mockWindow]);
  console.log(`[DEBUG] Notification VoC start forcée dans ${secondsDelay}s`);
}

export async function forceVocEndNotification(secondsDelay: number = 10): Promise<void> {
  if (!__DEV__) return;
  
  // Créer une fenêtre VoC qui se termine dans secondsDelay + 30min
  const endDate = new Date(Date.now() + (secondsDelay + 30 * 60) * 1000);
  const mockWindow: VocWindow = {
    start_at: new Date(Date.now() - 60 * 60 * 1000).toISOString(), // Commencée il y a 1h
    end_at: endDate.toISOString(),
  };
  
  await scheduleVocNotifications([mockWindow]);
  console.log(`[DEBUG] Notification VoC end forcée dans ${secondsDelay}s`);
}

export async function forceLunarCycleNotification(secondsDelay: number = 10): Promise<void> {
  if (!__DEV__) return;
  
  const mockReturn: LunarReturn = {
    id: 'debug-cycle-1',
    return_date: new Date(Date.now() + secondsDelay * 1000).toISOString(),
    moon_sign: 'Cancer',
    lunar_ascendant: 'Bélier',
  };
  
  await scheduleLunarCycleNotification(mockReturn);
  console.log(`[DEBUG] Notification cycle lunaire forcée dans ${secondsDelay}s`);
}

// Utilisation dans Expo DevTools:
// import { forceVocStartNotification } from './utils/debugNotifications';
// forceVocStartNotification(5); // Notification dans 5 secondes
```

---

## 📝 Notes de Test

### Historique des Tests
- **Date:** [À compléter]
- **Tester:** [À compléter]
- **Device:** [iOS/Android] [Version OS]
- **App Version:** [À compléter]
- **Backend:** [localhost/staging/prod]

### Résultats
- **TEST 1 (Empty State):** ✅ / ❌ / ⚠️
- **TEST 2 (Permission Refusée):** ✅ / ❌ / ⚠️
- **TEST 3 (Permission Acceptée):** ✅ / ❌ / ⚠️
- **TEST 4 (VoC Start):** ✅ / ❌ / ⚠️
- **TEST 5 (VoC End):** ✅ / ❌ / ⚠️
- **TEST 6 (Nouveau Cycle):** ✅ / ❌ / ⚠️

### Commentaires
[À compléter avec observations, screenshots, logs pertinents]

---

**Fin du Plan de Tests**

