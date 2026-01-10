/**
 * Tests pour contextService
 * Service critique pour l'IA contextuelle
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { getAIContext, getPhaseRecommendations, hasCycleContext, getCycleData } from '@/lib/services/contextService';

// Le mock AsyncStorage est maintenant dans jest.setup.js

// Mock profileStore
jest.mock('@/stores/profileStore', () => ({
  useProfileStore: {
    getState: jest.fn(() => ({
      profile: {
        name: 'Bianca',
        sunSign: { name: 'Scorpion' },
        moonSign: { name: 'Gémeaux' },
      },
    })),
  },
}));

describe('contextService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('getCycleData', () => {
    it('retourne null si pas de config cycle', async () => {
      AsyncStorage.getItem.mockResolvedValue(null);
      
      const result = await getCycleData();
      
      expect(result).toBeNull();
    });

    it('calcule correctement la phase menstruelle (J1-5)', async () => {
      const today = new Date();
      const lastPeriod = new Date(today.getTime() - 2 * 24 * 60 * 60 * 1000); // Il y a 2 jours
      
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        lastPeriodDate: lastPeriod.toISOString(),
        cycleLength: 28,
      }));
      
      const result = await getCycleData();
      
      expect(result).not.toBeNull();
      expect(result.phase).toBe('menstrual');
      expect(result.dayOfCycle).toBe(3);
      expect(result.energyLevel).toBeGreaterThanOrEqual(30);
      expect(result.energyLevel).toBeLessThanOrEqual(50);
    });

    it('calcule correctement la phase folliculaire (J6-13)', async () => {
      const today = new Date();
      const lastPeriod = new Date(today.getTime() - 10 * 24 * 60 * 60 * 1000); // Il y a 10 jours
      
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        lastPeriodDate: lastPeriod.toISOString(),
        cycleLength: 28,
      }));
      
      const result = await getCycleData();
      
      expect(result).not.toBeNull();
      expect(result.phase).toBe('follicular');
      expect(result.dayOfCycle).toBe(11);
    });

    it('calcule correctement la phase ovulation (J14-16)', async () => {
      const today = new Date();
      const lastPeriod = new Date(today.getTime() - 14 * 24 * 60 * 60 * 1000); // Il y a 14 jours
      
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        lastPeriodDate: lastPeriod.toISOString(),
        cycleLength: 28,
      }));
      
      const result = await getCycleData();
      
      expect(result).not.toBeNull();
      expect(result.phase).toBe('ovulation');
      expect(result.energyLevel).toBeGreaterThanOrEqual(90);
    });

    it('calcule correctement la phase lutéale (J17+)', async () => {
      const today = new Date();
      const lastPeriod = new Date(today.getTime() - 20 * 24 * 60 * 60 * 1000); // Il y a 20 jours
      
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        lastPeriodDate: lastPeriod.toISOString(),
        cycleLength: 28,
      }));
      
      const result = await getCycleData();
      
      expect(result).not.toBeNull();
      expect(result.phase).toBe('luteal');
    });
  });

  describe('getPhaseRecommendations', () => {
    it('retourne message si pas de cycle configuré', async () => {
      AsyncStorage.getItem.mockResolvedValue(null);
      
      const recs = await getPhaseRecommendations();
      
      expect(recs).toHaveLength(1);
      expect(recs[0]).toContain('Configure ton cycle');
    });

    it('retourne recommandations pour phase menstruelle', async () => {
      const today = new Date();
      const lastPeriod = new Date(today.getTime() - 2 * 24 * 60 * 60 * 1000);
      
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        lastPeriodDate: lastPeriod.toISOString(),
        cycleLength: 28,
      }));
      
      const recs = await getPhaseRecommendations();
      
      expect(recs.length).toBeGreaterThan(0);
      expect(recs.some(r => r.includes('repos'))).toBe(true);
    });
  });

  describe('getAIContext', () => {
    it('retourne contexte complet avec cycle + profil', async () => {
      const today = new Date();
      const lastPeriod = new Date(today.getTime() - 15 * 24 * 60 * 60 * 1000);
      
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        lastPeriodDate: lastPeriod.toISOString(),
        cycleLength: 28,
      }));
      
      AsyncStorage.getAllKeys.mockResolvedValue([]);
      
      const context = await getAIContext();
      
      expect(context).toHaveProperty('cycle');
      expect(context).toHaveProperty('profile');
      expect(context).toHaveProperty('contextText');
      expect(context.contextText).toContain('Bianca');
      expect(context.contextText).toContain('Scorpion');
      expect(context.contextText).toContain('CYCLE MENSTRUEL');
    });

    it('fonctionne sans cycle configuré', async () => {
      AsyncStorage.getItem.mockResolvedValue(null);
      AsyncStorage.getAllKeys.mockResolvedValue([]);
      
      const context = await getAIContext();
      
      expect(context).toHaveProperty('profile');
      expect(context.cycle).toBeNull();
    });
  });

  describe('hasCycleContext', () => {
    it('retourne true si cycle configuré', async () => {
      AsyncStorage.getItem.mockResolvedValue(JSON.stringify({
        lastPeriodDate: new Date().toISOString(),
        cycleLength: 28,
      }));
      
      const result = await hasCycleContext();
      
      expect(result).toBe(true);
    });

    it('retourne false si pas de cycle', async () => {
      AsyncStorage.getItem.mockResolvedValue(null);
      
      const result = await hasCycleContext();
      
      expect(result).toBe(false);
    });
  });
});

