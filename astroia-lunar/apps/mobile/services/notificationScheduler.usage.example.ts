/**
 * Exemple d'utilisation TypeScript pour notificationScheduler
 *
 * Ce fichier montre comment importer et utiliser le service de notifications VoC
 */

// Import des fonctions et types
import {
  // Feature flag
  ENABLE_VOC_NOTIFICATIONS,

  // Types
  VocWindow,
  LunarReturn,

  // Fonctions principales
  setupNotificationPermissions,
  scheduleVocNotification,
  scheduleVocNotifications,
  cancelAllVocNotifications,
  getScheduledNotifications,

  // Fonctions bonus
  requestNotificationPermissions,
  scheduleLunarCycleNotification,
  setupNotificationTapListener,
  shouldReschedule,
  markScheduled
} from './notificationScheduler';

// Exemple 1: Vérifier si feature activée
console.log('VoC notifications enabled:', ENABLE_VOC_NOTIFICATIONS);

// Exemple 2: Demander permissions
async function requestPermissions() {
  const granted = await setupNotificationPermissions();
  if (!granted) {
    console.log('Permissions refusées ou feature désactivée');
    return false;
  }
  return true;
}

// Exemple 3: Scheduler une fenêtre VoC
async function scheduleNextVoc() {
  const vocWindow: VocWindow = {
    start_at: '2026-01-17T14:30:00Z',
    end_at: '2026-01-17T16:45:00Z'
  };

  await scheduleVocNotification(vocWindow);
}

// Exemple 4: Lister notifications planifiées
async function listScheduled() {
  const scheduled = await getScheduledNotifications();
  console.log(`${scheduled.length} notifications VoC planifiées`);
  return scheduled;
}

// Exemple 5: Annuler toutes les notifications VoC
async function cancelAll() {
  await cancelAllVocNotifications();
}

// Exemple 6: Intégration dans un composant React
/*
import { useEffect } from 'react';

function VocWidget({ vocWindow }: { vocWindow: VocWindow | null }) {
  useEffect(() => {
    if (!vocWindow) return;

    const init = async () => {
      const granted = await setupNotificationPermissions();
      if (granted) {
        await scheduleVocNotification(vocWindow);
      }
    };

    init();
  }, [vocWindow]);

  return <View>...</View>;
}
*/

// Exemple 7: Scheduler plusieurs fenêtres VoC (batch)
async function scheduleBatch() {
  const vocWindows: VocWindow[] = [
    {
      start_at: '2026-01-17T14:30:00Z',
      end_at: '2026-01-17T16:45:00Z'
    },
    {
      start_at: '2026-01-18T09:15:00Z',
      end_at: '2026-01-18T11:20:00Z'
    }
  ];

  await scheduleVocNotifications(vocWindows);
}

// Exemple 8: Setup notification tap handler
/*
import { router } from 'expo-router';

const subscription = setupNotificationTapListener((screen) => {
  console.log('Notification tapped, navigating to:', screen);
  router.push(screen);
});

// Cleanup
subscription.remove();
*/
