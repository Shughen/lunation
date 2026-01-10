/**
 * Constants d'accessibilité pour LUNA
 * Labels pour VoiceOver/TalkBack
 */

export const A11Y_LABELS = {
  // Home screen
  home: {
    cycleCard: "Voir les détails de mon cycle menstruel actuel",
    cycleCardConfigure: "Configurer mon cycle menstruel",
    moodCard: "Ouvrir le journal d'humeur rapide",
    astroCard: "Voir l'analyse astrologique du jour",
    exploreTile: (feature) => `Explorer la fonctionnalité ${feature}`,
  },

  // Navigation
  nav: {
    home: "Aller à l'accueil",
    chat: "Ouvrir l'assistant IA LUNA",
    profile: "Voir mon profil astrologique",
    dashboard: "Voir mon tableau de bord",
    settings: "Ouvrir les paramètres",
  },

  // Actions
  actions: {
    save: "Sauvegarder",
    cancel: "Annuler",
    delete: "Supprimer",
    edit: "Modifier",
    close: "Fermer",
    back: "Retour",
    next: "Suivant",
    skip: "Passer",
    submit: "Envoyer",
    share: "Partager",
    export: "Exporter",
  },

  // Journal
  journal: {
    newEntry: "Créer une nouvelle entrée de journal",
    selectMood: (mood) => `Sélectionner l'humeur ${mood}`,
    selectTag: (tag) => `Ajouter le tag ${tag}`,
    saveEntry: "Sauvegarder l'entrée de journal",
  },

  // Cycle
  cycle: {
    selectPhase: (phase) => `Sélectionner la phase ${phase}`,
    selectDate: "Sélectionner la date des dernières règles",
    selectLength: (length) => `Sélectionner une durée de cycle de ${length} jours`,
    saveConfig: "Sauvegarder la configuration du cycle",
  },

  // Chat
  chat: {
    messageInput: "Écrire un message à l'assistant IA",
    sendMessage: "Envoyer le message",
    deleteConversation: "Supprimer la conversation",
  },

  // Settings
  settings: {
    toggleNotifications: "Activer ou désactiver les notifications",
    toggleAnalytics: "Activer ou désactiver le suivi analytics",
    exportData: "Exporter mes données personnelles",
    deleteAccount: "Supprimer définitivement mon compte",
  },

  // Dashboard
  dashboard: {
    filterAll: "Afficher toutes les analyses",
    filterType: (type) => `Filtrer par ${type}`,
    viewAnalysis: "Voir les détails de l'analyse",
    deleteAnalysis: "Supprimer cette analyse",
  },
};

/**
 * Hints d'accessibilité (descriptions contextuelles)
 */
export const A11Y_HINTS = {
  home: {
    cycleCard: "Touchez pour voir votre phase actuelle et vos recommandations",
    moodCard: "Touchez pour enregistrer rapidement votre humeur du jour",
    astroCard: "Touchez pour voir votre horoscope et vos transits",
  },

  journal: {
    moodButton: "Touchez pour choisir cette humeur",
    tagButton: "Touchez pour ajouter ce tag à votre entrée",
  },

  settings: {
    toggleSwitch: "Glissez pour activer ou désactiver",
    dangerButton: "Action irréversible, confirmation requise",
  },
};

/**
 * Rôles d'accessibilité
 */
export const A11Y_ROLES = {
  button: 'button',
  header: 'header',
  link: 'link',
  search: 'search',
  image: 'image',
  text: 'text',
  none: 'none',
  adjustable: 'adjustable', // Pour sliders
  switch: 'switch',
};

/**
 * États d'accessibilité
 */
export const A11Y_STATES = {
  disabled: { disabled: true },
  selected: { selected: true },
  checked: { checked: true },
  busy: { busy: true },
  expanded: { expanded: true },
  collapsed: { expanded: false },
};

export default {
  A11Y_LABELS,
  A11Y_HINTS,
  A11Y_ROLES,
  A11Y_STATES,
};
