import * as Haptics from 'expo-haptics';

/**
 * Haptics Utils - Retours tactiles uniformisés
 */

export const haptics = {
  /**
   * Impact léger (sélection, toggle, petits boutons)
   */
  light: () => {
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
  },

  /**
   * Impact moyen (boutons standards, navigation)
   */
  medium: () => {
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
  },

  /**
   * Impact fort (actions importantes, validation)
   */
  heavy: () => {
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy);
  },

  /**
   * Succès (action confirmée, sauvegarde)
   */
  success: () => {
    Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
  },

  /**
   * Warning (alerte, attention)
   */
  warning: () => {
    Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning);
  },

  /**
   * Erreur (action échouée, validation invalide)
   */
  error: () => {
    Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error);
  },

  /**
   * Sélection (picker, wheel, slider)
   */
  selection: () => {
    Haptics.selectionAsync();
  },
};

export default haptics;

