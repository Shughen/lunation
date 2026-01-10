/**
 * I18n - Système d'internationalisation simple
 * Pour une v2, migrer vers react-i18next
 */

export const strings = {
  // Common
  back: 'Retour',
  save: 'Sauvegarder',
  cancel: 'Annuler',
  delete: 'Supprimer',
  confirm: 'Confirmer',
  loading: 'Chargement...',
  error: 'Erreur',
  success: 'Succès',
  
  // Home
  home_title: 'Aujourd\'hui',
  home_explore: 'EXPLORER',
  
  // Journal
  journal_title: 'Mon Journal',
  journal_empty_title: 'Aucune entrée pour l\'instant',
  journal_empty_subtitle: 'Note ton humeur ou un événement marquant du jour.',
  journal_empty_action: 'Ajouter une entrée',
  journal_delete_confirm_title: 'Supprimer cette entrée ?',
  journal_delete_confirm_message: 'Cette action est irréversible.',
  journal_stats_title: 'Vos statistiques',
  journal_stats_entries: 'Entrées',
  journal_stats_dominant_mood: 'Humeur dominante',
  
  // Cycle
  cycle_title: 'Configuration Cycle',
  cycle_saved: 'Ta configuration de cycle a été mise à jour',
  
  // Accessibility labels
  a11y_add_entry: 'Ajouter une entrée',
  a11y_delete_entry: 'Supprimer cette entrée',
  a11y_back: 'Retour',
  
  // Accessibility hints
  a11y_hint_double_tap: 'Double tap pour ouvrir',
  a11y_hint_confirm_delete: 'Double tap pour confirmer la suppression',
} as const;

/**
 * Fonction helper pour récupérer une chaîne
 */
export function t(key: keyof typeof strings): string {
  return strings[key];
}

/**
 * Fonction helper avec interpolation simple
 * Exemple: t('welcome', { name: 'Marie' }) → "Bienvenue Marie"
 */
export function ti(key: string, params?: Record<string, string | number>): string {
  let result = (strings as any)[key] || key;
  
  if (params) {
    Object.entries(params).forEach(([paramKey, value]) => {
      result = result.replace(`{${paramKey}}`, String(value));
    });
  }
  
  return result;
}

export default { strings, t, ti };

