/**
 * Analytics layer - utilise PostHog via le service analytics
 * Ce fichier maintient la compatibilité avec le code existant
 */

import { trackEvent as posthogTrackEvent } from '../services/analytics';

export type AnalyticsEvent =
  | { name: 'daily_climate_view'; properties: { firstOfDay: boolean; source: 'home' | 'lunar' } }
  | { name: 'daily_climate_reset_dev'; properties: { timestamp: number } };

export function trackEvent(event: AnalyticsEvent): void {
  // Utilise le service PostHog pour tracker l'événement
  posthogTrackEvent(event.name, event.properties);
}
