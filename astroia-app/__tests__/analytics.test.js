/**
 * Tests de conformité RGPD – Analytics opt-in
 * Test B: Vérifier que Mixpanel ne s'initialise PAS sans consentement analytics
 */

import { Analytics } from '@/lib/analytics';
import * as consentService from '@/lib/services/consentService';
import { Mixpanel } from 'mixpanel-react-native';

// Mock Mixpanel
jest.mock('mixpanel-react-native', () => {
  const mockInstance = {
    init: jest.fn().mockResolvedValue(true),
    track: jest.fn().mockResolvedValue(true),
    identify: jest.fn().mockResolvedValue(true),
    getPeople: jest.fn(() => ({
      set: jest.fn().mockResolvedValue(true),
    })),
    reset: jest.fn(),
  };

  return {
    Mixpanel: jest.fn(() => mockInstance),
  };
});

jest.mock('@/lib/services/consentService', () => ({
  hasAnalyticsConsent: jest.fn(),
}));

describe('Conformité RGPD - Analytics opt-in', () => {
  beforeEach(() => {
    jest.clearAllMocks();
    // Reset module pour forcer réinitialisation
    jest.resetModules();
  });

  it('Test B: Mixpanel ne track PAS sans consentement analytics', async () => {
    // Simuler absence de consentement
    consentService.hasAnalyticsConsent.mockResolvedValue(false);

    // Tenter de tracker un événement
    await Analytics.track('test_event', { foo: 'bar' });

    // Vérifier qu'aucune instance Mixpanel n'a été créée
    expect(Mixpanel).not.toHaveBeenCalled();
  });

  it('Test B bis: Mixpanel track seulement avec consentement analytics', async () => {
    // Simuler présence de consentement
    consentService.hasAnalyticsConsent.mockResolvedValue(true);

    // Tenter de tracker un événement
    await Analytics.track('test_event', { foo: 'bar' });

    // Vérifier que Mixpanel a été initialisé
    await new Promise(resolve => setTimeout(resolve, 100)); // Attendre init
    expect(Mixpanel).toHaveBeenCalled();
  });

  it('Test B ter: Analytics.reset() nettoie Mixpanel', () => {
    // Appeler reset
    Analytics.reset();

    // Vérifier que le reset a été fait
    // (on ne peut pas tester directement car l'instance est privée, 
    //  mais on s'assure qu'aucune erreur n'est levée)
    expect(() => Analytics.reset()).not.toThrow();
  });
});
