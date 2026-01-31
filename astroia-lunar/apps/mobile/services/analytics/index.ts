/**
 * Analytics Service - PostHog Integration
 * Phase Bêta : Tracking des événements clés pour comprendre l'usage
 */

import PostHog from 'posthog-react-native';

// Type pour les propriétés d'événements (compatible PostHog)
type EventProperties = Record<string, string | number | boolean | null | undefined>;

// Instance PostHog (initialisée dans le provider)
let posthogInstance: PostHog | null = null;

// Configuration PostHog
export const POSTHOG_CONFIG = {
  apiKey: process.env.EXPO_PUBLIC_POSTHOG_KEY || '',
  host: process.env.EXPO_PUBLIC_POSTHOG_HOST || 'https://eu.i.posthog.com',
};

/**
 * Initialise PostHog (appelé dans _layout.tsx)
 */
export const initAnalytics = async (): Promise<void> => {
  if (!POSTHOG_CONFIG.apiKey) {
    if (__DEV__) {
      console.log('[Analytics] PostHog API key not configured, running in dev mode');
    }
    return;
  }

  try {
    posthogInstance = new PostHog(POSTHOG_CONFIG.apiKey, {
      host: POSTHOG_CONFIG.host,
    });

    if (__DEV__) {
      console.log('[Analytics] PostHog initialized');
    }
  } catch (error) {
    console.error('[Analytics] Failed to initialize PostHog:', error);
  }
};

/**
 * Ferme proprement PostHog (cleanup)
 */
export const shutdownAnalytics = async (): Promise<void> => {
  if (posthogInstance) {
    await posthogInstance.shutdown();
    posthogInstance = null;
  }
};

// ==================== ÉVÉNEMENTS TRACKING ====================

/**
 * Track une vue d'écran
 */
export const trackScreenView = (screenName: string, properties?: EventProperties): void => {
  const event: EventProperties = {
    screen_name: screenName,
    ...properties,
  };

  if (__DEV__) {
    console.log('[Analytics] screen_view:', event);
  }

  posthogInstance?.capture('screen_view', event);
};

/**
 * Track la consultation d'une révolution lunaire
 */
export const trackLunarReturnViewed = (month: string, properties?: EventProperties): void => {
  const event: EventProperties = {
    month,
    ...properties,
  };

  if (__DEV__) {
    console.log('[Analytics] lunar_return_viewed:', event);
  }

  posthogInstance?.capture('lunar_return_viewed', event);
};

/**
 * Track la création d'une entrée journal
 */
export const trackJournalEntry = (
  wordCount: number,
  moonSign?: string,
  moonPhase?: string,
): void => {
  const event: EventProperties = {
    word_count: wordCount,
    moon_sign: moonSign,
    moon_phase: moonPhase,
  };

  if (__DEV__) {
    console.log('[Analytics] journal_entry_created:', event);
  }

  posthogInstance?.capture('journal_entry_created', event);
};

/**
 * Track l'ouverture d'une notification
 */
export const trackNotificationOpened = (type: string, properties?: EventProperties): void => {
  const event: EventProperties = {
    notification_type: type,
    ...properties,
  };

  if (__DEV__) {
    console.log('[Analytics] notification_opened:', event);
  }

  posthogInstance?.capture('notification_opened', event);
};

/**
 * Track la fin de l'onboarding
 */
export const trackOnboardingCompleted = (properties?: EventProperties): void => {
  if (__DEV__) {
    console.log('[Analytics] onboarding_completed:', properties);
  }

  posthogInstance?.capture('onboarding_completed', properties || {});
};

/**
 * Track l'affichage d'un paywall (prépare Phase Production)
 */
export const trackPaywallShown = (feature: string, properties?: EventProperties): void => {
  const event: EventProperties = {
    feature,
    ...properties,
  };

  if (__DEV__) {
    console.log('[Analytics] paywall_shown:', event);
  }

  posthogInstance?.capture('paywall_shown', event);
};

/**
 * Track un événement générique
 */
export const trackEvent = (eventName: string, properties?: EventProperties): void => {
  if (__DEV__) {
    console.log(`[Analytics] ${eventName}:`, properties);
  }

  posthogInstance?.capture(eventName, properties || {});
};

/**
 * Identifier un utilisateur (après login)
 */
export const identifyUser = (userId: string, properties?: EventProperties): void => {
  if (__DEV__) {
    console.log('[Analytics] identify:', userId, properties);
  }

  posthogInstance?.identify(userId, properties);
};

/**
 * Reset l'identification (après logout)
 */
export const resetUser = (): void => {
  if (__DEV__) {
    console.log('[Analytics] reset user');
  }

  posthogInstance?.reset();
};

// Export par défaut pour faciliter les imports
export const Analytics = {
  init: initAnalytics,
  shutdown: shutdownAnalytics,
  trackScreenView,
  trackLunarReturnViewed,
  trackJournalEntry,
  trackNotificationOpened,
  trackOnboardingCompleted,
  trackPaywallShown,
  trackEvent,
  identifyUser,
  resetUser,
};

export default Analytics;
