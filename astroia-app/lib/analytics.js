// lib/analytics.js
// Analytics centralisé pour LUNA – Cycle & Cosmos
// Utilise Mixpanel pour le tracking utilisateur

import { Mixpanel } from 'mixpanel-react-native';
import { Platform } from 'react-native';
import { hasAnalyticsConsent } from './services/consentService';

// Mixpanel instance (lazy init)
let mixpanel = null;
let isInitialized = false;

/**
 * Initialise Mixpanel SEULEMENT si consentement analytics accordé
 * ⚠️ RGPD: Pas d'init = pas de tracking = pas de connexion réseau
 */
async function ensureMixpanelInit() {
  // Déjà initialisé
  if (isInitialized) {
    return mixpanel;
  }
  
  // Vérifier consentement
  const consent = await hasAnalyticsConsent();
  
  if (!consent) {
    console.log('[Analytics] Mixpanel NOT initialized - no consent');
    return null;
  }
  
  // Init seulement si consentement
  try {
    mixpanel = new Mixpanel('TON_TOKEN_MIXPANEL_ICI', true);
    await mixpanel.init();
    isInitialized = true;
    console.log('[Analytics] Mixpanel initialized with consent');
    return mixpanel;
  } catch (error) {
    console.error('[Analytics] Mixpanel init error:', error);
    return null;
  }
}

export const Analytics = {
  track: async (event, props = {}) => {
    try {
      const mp = await ensureMixpanelInit();
      
      if (!mp) {
        console.log('[Analytics] Tracking skipped - no consent or init failed');
        return;
      }

      await mp.track(event, {
        platform: Platform.OS,
        timestamp: new Date().toISOString(),
        ...props,
      });
    } catch (err) {
      console.warn('Analytics error:', err);
    }
  },

  identify: async (userId) => {
    try {
      const mp = await ensureMixpanelInit();
      if (mp) {
        await mp.identify(userId);
      }
    } catch (err) {
      console.warn('Identify error:', err);
    }
  },

  setUserProperties: async (props) => {
    try {
      const mp = await ensureMixpanelInit();
      if (mp) {
        await mp.getPeople().set(props);
      }
    } catch (err) {
      console.warn('UserProps error:', err);
    }
  },
  
  /**
   * Force reset de Mixpanel (quand consentement retiré)
   */
  reset: () => {
    if (mixpanel && isInitialized) {
      try {
        mixpanel.reset();
        console.log('[Analytics] Mixpanel reset');
      } catch (err) {
        console.warn('[Analytics] Reset error:', err);
      }
    }
    mixpanel = null;
    isInitialized = false;
  },
};

// === Événements standardisés ===
export const trackEvents = {
  // Onboarding
  onboardingCompleted: (userId) => {
    Analytics.track('onboarding_completed', { user_id: userId });
    Analytics.identify(userId);
  },

  // Home
  homeViewed: () => Analytics.track('home_viewed'),
  homeTapCycleDetails: () => Analytics.track('home_tap_cycle_details'),
  homeQuickMoodOpened: () => Analytics.track('home_quick_mood_opened'),
  homeTapAstroDetails: () => Analytics.track('home_tap_astro_details'),
  homeExploreTapped: (feature) => Analytics.track('home_explore_tapped', { feature }),

  // Journal
  journalEntryCreated: (mood, cyclePhase) => {
    Analytics.track('journal_entry_created', {
      mood,
      cycle_phase: cyclePhase || 'unknown',
    });
  },

  // Chat IA
  aiMessageSent: (conversationId, messageLength) => {
    Analytics.track('ai_message_sent', {
      conversation_id: conversationId,
      message_length: messageLength,
    });
  },

  aiMessageReceived: (conversationId, latency) => {
    Analytics.track('ai_message_received', {
      conversation_id: conversationId,
      latency_ms: latency,
    });
  },

  // Cycle & Astro
  cycleAnalysisCompleted: (phase, moonSign, energy) => {
    Analytics.track('cycle_analysis_completed', {
      cycle_phase: phase,
      moon_sign: moonSign,
      energy_level: energy,
    });
  },

  cycleConfigured: (cycleLength, lastPeriodDate) => {
    Analytics.track('cycle_configured', {
      cycle_length: cycleLength,
      days_since_period: Math.floor((new Date() - new Date(lastPeriodDate)) / (1000 * 60 * 60 * 24)),
    });
  },

  // Cycle Tracking V2
  cycleStartLogged: (totalCycles) => {
    Analytics.track('cycle_start_logged', {
      total_cycles: totalCycles || 0,
    });
  },

  cycleEndLogged: (periodLength, totalCycles) => {
    Analytics.track('cycle_end_logged', {
      period_length: periodLength,
      total_cycles: totalCycles || 0,
    });
  },

  cyclePredictionShown: (daysUntil, hasAverages) => {
    Analytics.track('cycle_prediction_shown', {
      days_until_next: daysUntil,
      has_averages: hasAverages,
    });
  },

  cycleStatsVisible: (avgPeriod, avgCycle, totalCycles) => {
    Analytics.track('cycle_stats_visible', {
      avg_period: avgPeriod,
      avg_cycle: avgCycle,
      total_cycles: totalCycles,
    });
  },

  cycleMigrationSkipped: (reason) => {
    Analytics.track('cycle_migration_skipped', {
      reason, // 'no_config' | 'invalid_data'
    });
  },

  cycleButtonDisabledMs: (duration) => {
    Analytics.track('cycle_button_disabled_ms', {
      duration_ms: duration,
    });
  },

  // Cycle Tracking V3 - Calendar & Fertility
  calendarViewOpened: (totalCycles) => {
    Analytics.track('calendar_view_opened', {
      total_cycles: totalCycles || 0,
    });
  },

  calendarDayTap: (date) => {
    Analytics.track('calendar_day_tap', {
      date,
    });
  },

  fertilityPredicted: (hasOvulation, hasFertileWindow) => {
    Analytics.track('fertility_predicted', {
      has_ovulation: hasOvulation,
      has_fertile_window: hasFertileWindow,
    });
  },

  // Cycle Tracking V3 Fix - New events
  cycleAverageRecomputed: (validCount, method, avgCycle, avgPeriod) => {
    Analytics.track('cycle_average_recomputed', {
      valid_count: validCount,
      method, // 'median' | 'mean'
      avg_cycle: avgCycle,
      avg_period: avgPeriod,
    });
  },

  cycleOutlierIgnored: (reason, value) => {
    Analytics.track('cycle_outlier_ignored', {
      reason, // 'period_length' | 'cycle_length' | 'too_close'
      value,
    });
  },

  cycleHistoryDeleted: (cycleId) => {
    Analytics.track('cycle_history_deleted', {
      cycle_id: cycleId,
    });
  },

  cycleHistoryEdited: (cycleId) => {
    Analytics.track('cycle_history_edited', {
      cycle_id: cycleId,
    });
  },

  cycleCountdownTapped: (destination, validCount) => {
    Analytics.track('cycle_countdown_tapped', {
      destination, // 'calendar' | 'my-cycles'
      valid_count: validCount,
    });
  },

  // Cycle Editor & Actions
  cycleHistoryOpenEditor: (mode, from) => {
    Analytics.track('cycle_history_open_editor', {
      mode, // 'create' | 'edit'
      from, // 'my-cycles' | 'home'
    });
  },

  cycleHistorySaved: (mode, periodLength, validAfterSave) => {
    Analytics.track('cycle_history_saved', {
      mode, // 'create' | 'edit'
      period_length: periodLength,
      valid_after_save: validAfterSave,
    });
  },

  cycleHistoryValidationError: (code, details) => {
    Analytics.track('cycle_history_validation_error', {
      code, // 'PERIOD_TOO_SHORT' | 'PERIOD_TOO_LONG' | 'INVALID_RANGE' | 'SAVE_FAILED'
      details,
    });
  },

  uiHistoryInvalidHidden: (count) => {
    Analytics.track('ui_history_invalid_hidden', {
      count,
    });
  },

  // Thème natal
  natalChartCalculated: (sunSign, moonSign, ascendant) => {
    Analytics.track('natal_chart_calculated', {
      sun_sign: sunSign,
      moon_sign: moonSign,
      ascendant: ascendant,
    });
  },

  natalChartViewed: () => Analytics.track('natal_chart_viewed'),

  // Compatibilité
  compatibilityAnalyzed: (type, score) => {
    Analytics.track('compatibility_analyzed', {
      compatibility_type: type, // couple, friend, work
      overall_score: score,
    });
  },

  // Horoscope
  horoscopeViewed: (sign) => {
    Analytics.track('horoscope_viewed', {
      zodiac_sign: sign,
    });
  },

  horoscopeRequested: (sign) => {
    Analytics.track('horoscope_requested', {
      zodiac_sign: sign,
    });
  },

  // Parent-Enfant
  parentChildAnalyzed: (childAge, parentSign, childSign) => {
    Analytics.track('parent_child_analyzed', {
      child_age: childAge,
      parent_sign: parentSign,
      child_sign: childSign,
    });
  },

  // Dashboard
  dashboardViewed: () => Analytics.track('dashboard_viewed'),

  dashboardFilterChanged: (filter) => {
    Analytics.track('dashboard_filter_changed', {
      filter_type: filter,
    });
  },

  // Settings & Privacy
  dataExported: (format) => {
    Analytics.track('data_exported', {
      export_format: format, // json, pdf
    });
  },

  accountDeleted: () => {
    Analytics.track('account_deleted');
  },

  consentChanged: (type, granted) => {
    Analytics.track('consent_changed', {
      consent_type: type, // health, analytics
      granted: granted,
    });
  },

  // App lifecycle
  appOpen: () => {
    Analytics.track('app_opened');
  },

  appClosed: (sessionDuration) => {
    Analytics.track('app_closed', {
      session_duration_seconds: sessionDuration,
    });
  },
};
