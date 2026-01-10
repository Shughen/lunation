/**
 * Tests unitaires pour lunarRevolutionService
 */

// Les mocks pour expo-constants, supabase et AsyncStorage sont maintenant dans jest.setup.js

import {
  calculateRevolutionDate,
  getLunarRevolution,
  getCachedRevolution,
  type BirthData,
} from '@/lib/services/lunarRevolutionService';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Mock moonCalculator
jest.mock('@/lib/services/moonCalculator', () => ({
  getTodayMoonSign: jest.fn(() => ({
    name: 'Bélier',
    emoji: '♈',
    element: 'Feu',
  })),
  getMoonPhase: jest.fn(() => ({
    phaseName: 'Nouvelle lune',
    emoji: '🌑',
    illumination: 0,
    dayInLunation: 1,
  })),
}));

describe('lunarRevolutionService', () => {
  const mockBirthData: BirthData = {
    year: 1990,
    month: 1,
    day: 15,
    hour: 12,
    minute: 0,
    second: 0,
    city: 'Paris',
    country_code: 'FR',
    latitude: 48.8566,
    longitude: 2.3522,
    timezone: 'Europe/Paris',
  };

  beforeEach(() => {
    jest.clearAllMocks();
    (AsyncStorage.getItem as jest.Mock).mockResolvedValue(null);
    (AsyncStorage.setItem as jest.Mock).mockResolvedValue(undefined);
  });

  describe('calculateRevolutionDate', () => {
    it('devrait calculer la date de révolution approximative', () => {
      const birthDate = new Date(1990, 0, 15, 12, 0, 0);
      const targetMonth = new Date(2025, 0, 1); // Janvier 2025

      const revolutionDate = calculateRevolutionDate(birthDate, targetMonth);

      expect(revolutionDate).toBeInstanceOf(Date);
      // La date devrait être dans le mois cible
      expect(revolutionDate.getMonth()).toBe(0); // Janvier
      expect(revolutionDate.getFullYear()).toBe(2025);
    });

    it('devrait gérer les mois différents', () => {
      const birthDate = new Date(1990, 5, 15); // Juin
      const targetMonth = new Date(2025, 2, 1); // Mars 2025

      const revolutionDate = calculateRevolutionDate(birthDate, targetMonth);

      expect(revolutionDate.getMonth()).toBe(2); // Mars
      expect(revolutionDate.getFullYear()).toBe(2025);
    });
  });

  describe('getLunarRevolution', () => {
    it('devrait générer une révolution lunaire basique', async () => {
      const targetMonth = new Date(2025, 0, 1);

      const revolution = await getLunarRevolution(mockBirthData, targetMonth);

      expect(revolution).toBeDefined();
      expect(revolution.month).toBe('2025-01');
      expect(revolution.moonSign).toBe('Bélier');
      expect(revolution.house).toBeGreaterThanOrEqual(1);
      expect(revolution.house).toBeLessThanOrEqual(12);
      expect(revolution.phase).toBeDefined();
      expect(revolution.interpretationSummary).toBeDefined();
      expect(revolution.focus).toBeDefined();
    });

    it('devrait utiliser le cache si disponible', async () => {
      const targetMonth = new Date(2025, 0, 1);
      const cachedRevolution = {
        month: '2025-01',
        revolutionDate: '2025-01-15T12:00:00Z',
        moonSign: 'Taureau',
        moonSignEmoji: '♉',
        moonDegree: 15,
        house: 2,
        phase: 'waxing',
        phaseName: 'Premier croissant',
        aspects: [],
        interpretationSummary: 'Cached interpretation',
        focus: 'valeurs et ressources',
      };

      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(
        JSON.stringify(cachedRevolution)
      );

      const revolution = await getLunarRevolution(mockBirthData, targetMonth, {
        force_refresh: false,
      });

      expect(revolution.moonSign).toBe('Taureau');
      expect(revolution.interpretationSummary).toBe('Cached interpretation');
    });

    it('devrait forcer le refresh si demandé', async () => {
      const targetMonth = new Date(2025, 0, 1);
      const cachedRevolution = {
        month: '2025-01',
        moonSign: 'Taureau',
      };

      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(
        JSON.stringify(cachedRevolution)
      );

      const revolution = await getLunarRevolution(mockBirthData, targetMonth, {
        force_refresh: true,
      });

      // Devrait recalculer même avec cache
      expect(revolution.moonSign).toBe('Bélier'); // Depuis le mock
    });
  });

  describe('getCachedRevolution', () => {
    it('devrait retourner null si aucun cache', async () => {
      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(null);

      const cached = await getCachedRevolution('2025-01');

      expect(cached).toBeNull();
    });

    it('devrait retourner la révolution depuis le cache', async () => {
      const cachedRevolution = {
        month: '2025-01',
        moonSign: 'Bélier',
      };

      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(
        JSON.stringify(cachedRevolution)
      );

      const cached = await getCachedRevolution('2025-01');

      expect(cached).not.toBeNull();
      expect(cached?.month).toBe('2025-01');
      expect(cached?.moonSign).toBe('Bélier');
    });
  });
});

