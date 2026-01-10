/**
 * Tests pour les calculs de médiane et filtres de cycles
 */

// Mock Analytics
jest.mock('@/lib/analytics', () => ({
  Analytics: {
    track: jest.fn(),
  },
}));

// Le mock AsyncStorage est maintenant dans jest.setup.js

import AsyncStorage from '@react-native-async-storage/async-storage';
import { useCycleHistoryStore, CycleEntry } from '@/stores/cycleHistoryStore';

describe('CycleHistoryStore - Médiane & Filtres', () => {
  beforeEach(() => {
    // Reset store avant chaque test
    useCycleHistoryStore.setState({ cycles: [] });
    // Reset AsyncStorage mocks
    jest.clearAllMocks();
    (AsyncStorage.getItem as jest.Mock).mockResolvedValue(null);
    (AsyncStorage.setItem as jest.Mock).mockResolvedValue(undefined);
  });

  describe('Médiane des cycles', () => {
    it('devrait calculer la médiane de [28, 29, 31] = 29', () => {
      const store = useCycleHistoryStore.getState();
      const now = new Date();
      
      // Créer 3 cycles valides
      const cycles: CycleEntry[] = [
        {
          id: '1',
          startDate: new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 85 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 28,
          createdAt: new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
        {
          id: '2',
          startDate: new Date(now.getTime() - 62 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 57 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 29,
          createdAt: new Date(now.getTime() - 62 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
        {
          id: '3',
          startDate: new Date(now.getTime() - 33 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 28 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 31,
          createdAt: new Date(now.getTime() - 33 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
      ];
      
      useCycleHistoryStore.setState({ cycles });
      const averages = store.getAverages();
      
      expect(averages).not.toBeNull();
      expect(averages?.avgCycle).toBe(29); // Médiane de [28, 29, 31]
      expect(averages?.method).toBe('median');
    });

    it('devrait filtrer [14, 60, 28] → 28 (cycles hors bornes ignorés)', () => {
      const store = useCycleHistoryStore.getState();
      const now = new Date();
      
      // Créer cycles avec outliers
      const cycles: CycleEntry[] = [
        {
          id: '1',
          startDate: new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 89 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 1, // INVALIDE (<2)
          cycleLength: 14, // INVALIDE (<18)
          createdAt: new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
        {
          id: '2',
          startDate: new Date(now.getTime() - 62 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 57 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 60, // INVALIDE (>40)
          createdAt: new Date(now.getTime() - 62 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
        {
          id: '3',
          startDate: new Date(now.getTime() - 33 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 28 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 28, // VALIDE
          createdAt: new Date(now.getTime() - 33 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
      ];
      
      useCycleHistoryStore.setState({ cycles });
      const validCycles = store.getValidCycles();
      
      // Seul le 3ème cycle devrait être valide
      expect(validCycles.length).toBe(1);
      expect(validCycles[0].id).toBe('3');
    });
  });

  describe('Prédictions', () => {
    it('ne devrait pas avoir de prédiction avec 1 seul cycle', () => {
      const store = useCycleHistoryStore.getState();
      const now = new Date();
      
      const cycles: CycleEntry[] = [
        {
          id: '1',
          startDate: new Date(now.getTime() - 10 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 5 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: null,
          createdAt: new Date(now.getTime() - 10 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
      ];
      
      useCycleHistoryStore.setState({ cycles });
      const averages = store.getAverages();
      const prediction = store.predictNextPeriod();
      
      expect(averages).toBeNull(); // <2 cycles
      expect(prediction).toBeNull();
    });

    it('devrait calculer moyenne avec 2 cycles valides', () => {
      const store = useCycleHistoryStore.getState();
      const now = new Date();
      
      const cycles: CycleEntry[] = [
        {
          id: '1',
          startDate: new Date(now.getTime() - 60 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 55 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 28,
          createdAt: new Date(now.getTime() - 60 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
        {
          id: '2',
          startDate: new Date(now.getTime() - 32 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 27 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 30,
          createdAt: new Date(now.getTime() - 32 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
      ];
      
      useCycleHistoryStore.setState({ cycles });
      const averages = store.getAverages();
      
      expect(averages).not.toBeNull();
      expect(averages?.avgCycle).toBe(29); // Moyenne de [28, 30]
      expect(averages?.method).toBe('mean');
      expect(averages?.validCount).toBe(2);
    });
  });

  describe('Suppression & édition', () => {
    it('devrait recalculer après suppression', async () => {
      const store = useCycleHistoryStore.getState();
      const now = new Date();
      
      const cycles: CycleEntry[] = [
        {
          id: '1',
          startDate: new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 85 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 28,
          createdAt: new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
        {
          id: '2',
          startDate: new Date(now.getTime() - 62 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 57 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 29,
          createdAt: new Date(now.getTime() - 62 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
        {
          id: '3',
          startDate: new Date(now.getTime() - 33 * 24 * 60 * 60 * 1000).toISOString(),
          endDate: new Date(now.getTime() - 28 * 24 * 60 * 60 * 1000).toISOString(),
          periodLength: 5,
          cycleLength: 31,
          createdAt: new Date(now.getTime() - 33 * 24 * 60 * 60 * 1000).toISOString(),
          updatedAt: new Date().toISOString(),
        },
      ];
      
      useCycleHistoryStore.setState({ cycles });
      
      // Supprimer cycle 2
      await store.deleteCycle('2');
      
      const updatedCycles = useCycleHistoryStore.getState().cycles;
      expect(updatedCycles.length).toBe(2);
      expect(updatedCycles.find(c => c.id === '2')).toBeUndefined();
    });
  });
});

