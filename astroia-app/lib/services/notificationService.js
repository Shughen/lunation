/**
 * Service de notifications push
 * Rappels cycle, changements phase, insights quotidiens
 */

// Temporairement désactivé (module natif)
// import * as Notifications from 'expo-notifications';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { hasHealthConsent } from './consentService';
import { predictNextPeriod } from './cycleCalculator';

// Configuration du handler de notifications
// Temporairement désactivé (module natif non disponible)
/*
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: true,
    priority: Notifications.AndroidNotificationPriority.HIGH,
  }),
});
*/

/**
 * Demande la permission notifications
 * @returns {Promise<boolean>} Permission accordée
 */
export async function requestNotificationPermission() {
  try {
    const { status: existingStatus } = await Notifications.getPermissionsAsync();
    let finalStatus = existingStatus;
    
    if (existingStatus !== 'granted') {
      const { status } = await Notifications.requestPermissionsAsync();
      finalStatus = status;
    }
    
    if (finalStatus !== 'granted') {
      console.log('[Notifications] Permission refusée');
      return false;
    }
    
    console.log('[Notifications] Permission accordée');
    
    // Sauvegarder la permission
    await AsyncStorage.setItem('notifications_permission', 'granted');
    
    return true;
  } catch (error) {
    console.error('[Notifications] Erreur permission:', error);
    return false;
  }
}

/**
 * Vérifie si les notifications sont activées
 */
export async function hasNotificationPermission() {
  try {
    const stored = await AsyncStorage.getItem('notifications_permission');
    if (stored === 'granted') {
      const { status } = await Notifications.getPermissionsAsync();
      return status === 'granted';
    }
    return false;
  } catch (error) {
    return false;
  }
}

/**
 * Planifie une notification de rappel prochaines règles
 * @param {Date} nextPeriodDate - Date prévue prochaines règles
 */
export async function scheduleNextPeriodReminder(nextPeriodDate) {
  try {
    // Vérifier consentement santé
    const healthConsent = await hasHealthConsent();
    if (!healthConsent) {
      console.log('[Notifications] Pas de consentement santé');
      return null;
    }
    
    // Vérifier permission notifs
    const hasPermission = await hasNotificationPermission();
    if (!hasPermission) {
      console.log('[Notifications] Pas de permission');
      return null;
    }
    
    // Annuler notifications existantes "period_reminder"
    await cancelNotificationsByType('period_reminder');
    
    // Programmer 2 jours avant
    const reminderDate = new Date(nextPeriodDate);
    reminderDate.setDate(reminderDate.getDate() - 2);
    reminderDate.setHours(9, 0, 0, 0); // 9h du matin
    
    // Ne pas programmer si dans le passé
    if (reminderDate <= new Date()) {
      console.log('[Notifications] Date dans le passé, skip');
      return null;
    }
    
    const notificationId = await Notifications.scheduleNotificationAsync({
      content: {
        title: '🩸 Tes règles arrivent',
        body: 'Dans 2 jours environ. Prépare-toi en douceur et écoute ton corps.',
        data: { type: 'period_reminder' },
        sound: true,
      },
      trigger: {
        date: reminderDate,
      },
    });
    
    console.log('[Notifications] Period reminder planifiée:', notificationId);
    return notificationId;
  } catch (error) {
    console.error('[Notifications] Erreur schedule period:', error);
    return null;
  }
}

/**
 * Planifie notification changement de phase
 * @param {string} newPhase - Nouvelle phase ('follicular', 'ovulation', 'luteal', 'menstrual')
 * @param {Date} changeDate - Date du changement
 */
export async function schedulePhaseChangeNotification(newPhase, changeDate) {
  try {
    const hasPermission = await hasNotificationPermission();
    if (!hasPermission) return null;
    
    const phaseEmojis = {
      menstrual: '🌑',
      follicular: '🌒',
      ovulation: '🌕',
      luteal: '🌘',
    };
    
    const phaseMessages = {
      menstrual: 'Tu entres en phase menstruelle. Douceur et repos sont tes alliés.',
      follicular: 'Phase folliculaire ! Ton énergie remonte, c\'est le moment de planifier.',
      ovulation: 'Phase d\'ovulation ! Tu es au pic de ton énergie, profites-en !',
      luteal: 'Phase lutéale. Temps de ralentir progressivement et te recentrer.',
    };
    
    const emoji = phaseEmojis[newPhase] || '🌙';
    const message = phaseMessages[newPhase] || 'Nouvelle phase de cycle';
    
    // Programmer le jour du changement à 8h
    const notifDate = new Date(changeDate);
    notifDate.setHours(8, 0, 0, 0);
    
    if (notifDate <= new Date()) return null;
    
    const notificationId = await Notifications.scheduleNotificationAsync({
      content: {
        title: `${emoji} Changement de phase`,
        body: message,
        data: { type: 'phase_change', phase: newPhase },
      },
      trigger: {
        date: notifDate,
      },
    });
    
    console.log('[Notifications] Phase change planifiée:', notificationId);
    return notificationId;
  } catch (error) {
    console.error('[Notifications] Erreur schedule phase:', error);
    return null;
  }
}

/**
 * Planifie notification insight quotidien (10h chaque jour)
 */
export async function scheduleDailyInsightNotification() {
  try {
    const hasPermission = await hasNotificationPermission();
    if (!hasPermission) return null;
    
    // Annuler anciennes
    await cancelNotificationsByType('daily_insight');
    
    // Programmer tous les jours à 10h
    const notificationId = await Notifications.scheduleNotificationAsync({
      content: {
        title: '💡 Ton insight du jour',
        body: 'Découvre ce que les astres et ton cycle te réservent aujourd\'hui !',
        data: { type: 'daily_insight' },
      },
      trigger: {
        hour: 10,
        minute: 0,
        repeats: true,
      },
    });
    
    console.log('[Notifications] Daily insight planifiée:', notificationId);
    return notificationId;
  } catch (error) {
    console.error('[Notifications] Erreur schedule insight:', error);
    return null;
  }
}

/**
 * Annule toutes les notifications d'un type
 * @param {string} type - Type de notification
 */
async function cancelNotificationsByType(type) {
  try {
    const scheduled = await Notifications.getAllScheduledNotificationsAsync();
    
    for (const notif of scheduled) {
      if (notif.content?.data?.type === type) {
        await Notifications.cancelScheduledNotificationAsync(notif.identifier);
        console.log('[Notifications] Cancelled:', notif.identifier);
      }
    }
  } catch (error) {
    console.error('[Notifications] Erreur cancel:', error);
  }
}

/**
 * Annule toutes les notifications planifiées
 */
export async function cancelAllNotifications() {
  try {
    await Notifications.cancelAllScheduledNotificationsAsync();
    console.log('[Notifications] Toutes annulées');
  } catch (error) {
    console.error('[Notifications] Erreur cancel all:', error);
  }
}

/**
 * Setup complet des notifications pour le cycle actuel
 * @param {string|Date} lastPeriodDate - Dernières règles
 * @param {number} cycleLength - Durée cycle
 */
export async function setupCycleNotifications(lastPeriodDate, cycleLength = 28) {
  try {
    const hasPermission = await hasNotificationPermission();
    if (!hasPermission) {
      console.log('[Notifications] Pas de permission, skip setup');
      return;
    }
    
    // 1. Notification prochaines règles
    const nextPeriod = predictNextPeriod(lastPeriodDate, cycleLength);
    await scheduleNextPeriodReminder(nextPeriod);
    
    // 2. Notifications changements de phase (calculer les dates)
    const start = new Date(lastPeriodDate);
    
    // Phase folliculaire (J6)
    const follicularDate = new Date(start);
    follicularDate.setDate(start.getDate() + 5);
    await schedulePhaseChangeNotification('follicular', follicularDate);
    
    // Phase ovulation (J14)
    const ovulationDate = new Date(start);
    ovulationDate.setDate(start.getDate() + 13);
    await schedulePhaseChangeNotification('ovulation', ovulationDate);
    
    // Phase lutéale (J17)
    const lutealDate = new Date(start);
    lutealDate.setDate(start.getDate() + 16);
    await schedulePhaseChangeNotification('luteal', lutealDate);
    
    // 3. Insight quotidien (10h chaque jour)
    await scheduleDailyInsightNotification();
    
    console.log('[Notifications] Setup complet terminé');
  } catch (error) {
    console.error('[Notifications] Erreur setup:', error);
  }
}

/**
 * Retourne toutes les notifications planifiées
 * (pour debug/Settings)
 */
export async function getScheduledNotifications() {
  try {
    const scheduled = await Notifications.getAllScheduledNotificationsAsync();
    return scheduled;
  } catch (error) {
    console.error('[Notifications] Erreur get scheduled:', error);
    return [];
  }
}

export default {
  requestNotificationPermission,
  hasNotificationPermission,
  scheduleNextPeriodReminder,
  schedulePhaseChangeNotification,
  scheduleDailyInsightNotification,
  setupCycleNotifications,
  cancelAllNotifications,
  getScheduledNotifications,
};
