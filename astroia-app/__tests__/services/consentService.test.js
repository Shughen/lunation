/**
 * Tests pour consentService
 * Service critique RGPD
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { hasHealthConsent, hasAnalyticsConsent, getConsents, updateConsent } from '@/lib/services/consentService';

// Le mock AsyncStorage est maintenant dans jest.setup.js

// Mock consentAuditService
jest.mock('@/lib/services/consentAuditService', () => ({
  logConsent: jest.fn(),
}));

describe('consentService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('hasHealthConsent', () => {
    it('retourne false si pas de consentement enregistré', async () => {
      AsyncStorage.getItem.mockResolvedValue(null);
      
      const result = await hasHealthConsent();
      
      expect(result).toBe(false);
    });

    it('retourne true si consentement santé accordé', async () => {
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        health: true,
        analytics: false,
      }));
      
      const result = await hasHealthConsent();
      
      expect(result).toBe(true);
    });
  });

  describe('hasAnalyticsConsent', () => {
    it('retourne false par défaut', async () => {
      AsyncStorage.getItem.mockResolvedValue(null);
      
      const result = await hasAnalyticsConsent();
      
      expect(result).toBe(false);
    });

    it('retourne true si consentement analytics accordé', async () => {
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        health: true,
        analytics: true,
      }));
      
      const result = await hasAnalyticsConsent();
      
      expect(result).toBe(true);
    });
  });

  describe('getConsents', () => {
    it('retourne structure par défaut si aucun consentement', async () => {
      AsyncStorage.getItem.mockResolvedValue(null);
      
      const consents = await getConsents();
      
      expect(consents).toHaveProperty('health');
      expect(consents).toHaveProperty('analytics');
      expect(consents.health).toBe(false);
      expect(consents.analytics).toBe(false);
    });

    it('retourne les consentements enregistrés', async () => {
      const stored = {
        health: true,
        analytics: true,
        version: '2.0.0',
        date: '2025-11-09T10:00:00Z',
      };
      
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify(stored));
      
      const consents = await getConsents();
      
      expect(consents.health).toBe(true);
      expect(consents.analytics).toBe(true);
      expect(consents.version).toBe('2.0.0');
    });
  });

  describe('updateConsent', () => {
    it('met à jour le consentement et sauvegarde', async () => {
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        health: false,
        analytics: false,
      }));
      
      await updateConsent('health', true);
      
      expect(AsyncStorage.setItem).toHaveBeenCalledWith(
        'user_consent',
        expect.stringContaining('"health":true')
      );
    });

    it('log l\'audit trail quand consentement change', async () => {
      const { logConsent } = require('@/lib/services/consentAuditService');
      
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        health: false,
        analytics: false,
      }));
      
      await updateConsent('health', true, 'settings');
      
      expect(logConsent).toHaveBeenCalledWith('health', 'granted', 'settings');
    });
  });
});

