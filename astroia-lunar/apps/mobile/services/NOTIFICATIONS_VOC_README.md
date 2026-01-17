# Service de Notifications VoC (Void of Course)

## État actuel

**DÉSACTIVÉ PAR DÉFAUT** - Feature flag `ENABLE_VOC_NOTIFICATIONS = false`

Le service de notifications VoC est implémenté mais **désactivé** pour éviter tout déclenchement accidentel de notifications avant validation complète du MVP.

## Architecture

### Fichier principal
`/apps/mobile/services/notificationScheduler.ts`

### Fonctions publiques disponibles

1. **`setupNotificationPermissions(): Promise<boolean>`**
   - Demande les permissions système pour les notifications
   - Configure le canal Android si nécessaire
   - Retourne `false` si feature désactivée

2. **`scheduleVocNotification(vocWindow: VocWindow): Promise<void>`**
   - Planifie les notifications pour UNE fenêtre VoC
   - Notification 30 minutes AVANT le début VoC
   - Notification AU DÉBUT du VoC
   - Structure de données:
     ```typescript
     {
       title: "Void of Course actif",
       body: "La Lune entre en VoC dans 30 minutes",
       data: { type: 'voc_start', windowId: 'xxx', screen: '/lunar/voc' },
       trigger: { seconds: xxx }
     }
     ```

3. **`scheduleVocNotifications(vocWindows: VocWindow[]): Promise<void>`**
   - Planifie les notifications pour PLUSIEURS fenêtres VoC (batch)
   - Utilise la même logique que `scheduleVocNotification` en boucle

4. **`cancelAllVocNotifications(): Promise<void>`**
   - Annule toutes les notifications VoC planifiées
   - Alias de `cancelAllNotifications()`

5. **`getScheduledNotifications(): Promise<NotificationRequest[]>`**
   - Récupère la liste des notifications VoC planifiées
   - Utile pour debug et monitoring

## Comment activer les notifications VoC

### Étape 1: Activer le feature flag

Dans `/apps/mobile/services/notificationScheduler.ts`:

```typescript
// Passer de false à true
export const ENABLE_VOC_NOTIFICATIONS = true;
```

### Étape 2: Intégrer dans VocWidget.tsx

Exemple d'intégration (à décommenter):

```typescript
import {
  setupNotificationPermissions,
  scheduleVocNotification,
  getScheduledNotifications
} from '../services/notificationScheduler';

// Au montage du composant ou dans un useEffect
useEffect(() => {
  const initNotifications = async () => {
    const granted = await setupNotificationPermissions();
    if (granted && vocWindow) {
      await scheduleVocNotification(vocWindow);
    }
  };

  initNotifications();
}, [vocWindow]);
```

### Étape 3: Vérifier l'API backend

S'assurer que `/voc/status` retourne:

```json
{
  "is_active": true,
  "current_window": {
    "start_at": "2026-01-17T14:30:00Z",
    "end_at": "2026-01-17T16:45:00Z"
  },
  "next_window": {
    "start_at": "2026-01-18T09:15:00Z",
    "end_at": "2026-01-18T11:20:00Z"
  }
}
```

### Étape 4: Tester le scheduling

```typescript
// Debug: afficher les notifications planifiées
const scheduled = await getScheduledNotifications();
console.log('Notifications VoC planifiées:', scheduled);

// Tester avec une fenêtre VoC dans 5 minutes
const testWindow = {
  start_at: new Date(Date.now() + 5 * 60 * 1000).toISOString(),
  end_at: new Date(Date.now() + 65 * 60 * 1000).toISOString()
};
await scheduleVocNotification(testWindow);
```

## Configuration des notifications

### Timing
- **30 minutes AVANT** le début du VoC: notification "VoC approche"
- **AU DÉBUT** du VoC: notification "VoC actif"

### Deep linking
Toutes les notifications ouvrent l'écran `/lunar/voc` au tap.

### Badge count
**Désactivé** pour le MVP (`shouldSetBadge: false`)

## Dépendances

- `expo-notifications: ^0.32.15` (déjà installé)
- `@react-native-async-storage/async-storage` (pour cache)

## Monitoring

Tous les logs sont préfixés `[Notifications]` ou `[VoC Notifications]`:

```
[VoC Notifications] Feature désactivée (ENABLE_VOC_NOTIFICATIONS = false)
[Notifications] ✅ Permission accordée
[Notifications] ✅ 2 notifications VoC schedulées pour fenêtre
```

## Sécurité

Le feature flag empêche **toute** notification si `ENABLE_VOC_NOTIFICATIONS = false`:
- `setupNotificationPermissions()` → retourne `false` immédiatement
- `scheduleVocNotification()` → log et return immédiatement
- `cancelAllVocNotifications()` → log "aucune notification à annuler"

## Prochaines étapes (hors scope MVP)

- [ ] Préférence utilisateur pour activer/désactiver les notifications VoC
- [ ] Personnalisation du délai de pré-notification (15/30/60 min)
- [ ] Badge count dynamique si VoC actif
- [ ] Notifications push serveur (vs local scheduling)
