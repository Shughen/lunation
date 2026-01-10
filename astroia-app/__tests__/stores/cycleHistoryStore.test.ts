/**
 * Tests unitaires pour cycleHistoryStore
 */

import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';

// Le mock AsyncStorage est maintenant dans jest.setup.js

// Mock Analytics
jest.mock('@/lib/analytics', () => ({
  Analytics: {
    track: jest.fn(),
  },
}));

describe('cycleHistoryStore', () => {
  beforeEach(() => {
    // Reset store avant chaque test
    useCycleHistoryStore.setState({ cycles: [] });
  });

  describe('getAverages', () => {
    it('devrait retourner null si <2 cycles complets', () => {
      const store = useCycleHistoryStore.getState();
      
      // 0 cycle
      expect(store.getAverages()).toBeNull();
      
      // 1 cycle complet
      useCycleHistoryStore.setState({
        cycles: [
          {
            id: 'cycle1',
            startDate: '2025-10-01T00:00:00.000Z',
            endDate: '2025-10-05T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2025-10-01T00:00:00.000Z',
            updatedAt: '2025-10-05T00:00:00.000Z',
          },
        ],
      });
      
      expect(store.getAverages()).toBeNull();
    });

    it('devrait calculer les moyennes avec ≥2 cycles complets', () => {
      useCycleHistoryStore.setState({
        cycles: [
          {
            id: 'cycle1',
            startDate: '2025-09-01T00:00:00.000Z',
            endDate: '2025-09-05T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2025-09-01T00:00:00.000Z',
            updatedAt: '2025-09-05T00:00:00.000Z',
          },
          {
            id: 'cycle2',
            startDate: '2025-09-29T00:00:00.000Z',
            endDate: '2025-10-03T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 27,
            createdAt: '2025-09-29T00:00:00.000Z',
            updatedAt: '2025-10-03T00:00:00.000Z',
          },
        ],
      });
      
      const store = useCycleHistoryStore.getState();
      const avg = store.getAverages();
      
      expect(avg).not.toBeNull();
      expect(avg?.avgPeriod).toBe(5); // (5 + 5) / 2
      expect(avg?.avgCycle).toBe(28); // (28 + 27) / 2 arrondi
      expect(avg?.totalCycles).toBe(2);
    });

    it('ne devrait PAS inclure cycle ouvert dans les moyennes', () => {
      useCycleHistoryStore.setState({
        cycles: [
          {
            id: 'cycle1',
            startDate: '2025-09-01T00:00:00.000Z',
            endDate: '2025-09-05T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2025-09-01T00:00:00.000Z',
            updatedAt: '2025-09-05T00:00:00.000Z',
          },
          {
            id: 'cycle2',
            startDate: '2025-09-29T00:00:00.000Z',
            endDate: '2025-10-03T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 27,
            createdAt: '2025-09-29T00:00:00.000Z',
            updatedAt: '2025-10-03T00:00:00.000Z',
          },
          {
            id: 'cycle3',
            startDate: '2025-10-26T00:00:00.000Z',
            endDate: null, // Cycle ouvert (en cours)
            periodLength: null,
            cycleLength: null,
            createdAt: '2025-10-26T00:00:00.000Z',
            updatedAt: '2025-10-26T00:00:00.000Z',
          },
        ],
      });
      
      const store = useCycleHistoryStore.getState();
      const avg = store.getAverages();
      
      // Devrait calculer sur les 2 premiers uniquement
      expect(avg).not.toBeNull();
      expect(avg?.totalCycles).toBe(2); // Pas 3
      expect(avg?.avgPeriod).toBe(5);
    });
  });

  describe('predictNextPeriod', () => {
    it('devrait retourner null si pas de moyennes', () => {
      const store = useCycleHistoryStore.getState();
      expect(store.predictNextPeriod()).toBeNull();
    });

    it('devrait prédire correctement avec cycles complets', () => {
      useCycleHistoryStore.setState({
        cycles: [
          {
            id: 'cycle1',
            startDate: '2025-10-01T00:00:00.000Z',
            endDate: '2025-10-05T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2025-10-01T00:00:00.000Z',
            updatedAt: '2025-10-05T00:00:00.000Z',
          },
          {
            id: 'cycle2',
            startDate: '2025-10-29T00:00:00.000Z',
            endDate: '2025-11-02T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2025-10-29T00:00:00.000Z',
            updatedAt: '2025-11-02T00:00:00.000Z',
          },
        ],
      });
      
      const store = useCycleHistoryStore.getState();
      const prediction = store.predictNextPeriod();
      
      expect(prediction).not.toBeNull();
      // Dernier cycle commence le 29 oct, +28 jours = 26 nov
      expect(prediction?.nextDate).toEqual(new Date('2025-11-26T00:00:00.000Z'));
      // daysUntil dépend de la date actuelle, on vérifie juste qu'il existe
      expect(prediction?.daysUntil).toBeGreaterThanOrEqual(0);
    });

    it('ne devrait jamais afficher daysUntil négatif', () => {
      // Cycle très ancien (prédiction dans le passé)
      useCycleHistoryStore.setState({
        cycles: [
          {
            id: 'cycle1',
            startDate: '2024-01-01T00:00:00.000Z',
            endDate: '2024-01-05T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2024-01-01T00:00:00.000Z',
            updatedAt: '2024-01-05T00:00:00.000Z',
          },
          {
            id: 'cycle2',
            startDate: '2024-01-29T00:00:00.000Z',
            endDate: '2024-02-02T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2024-01-29T00:00:00.000Z',
            updatedAt: '2024-02-02T00:00:00.000Z',
          },
        ],
      });
      
      const store = useCycleHistoryStore.getState();
      const prediction = store.predictNextPeriod();
      
      // daysUntil devrait être 0 (pas négatif)
      expect(prediction?.daysUntil).toBeGreaterThanOrEqual(0);
    });
  });

  describe('getCurrentCycle', () => {
    it('devrait retourner le cycle sans endDate', () => {
      useCycleHistoryStore.setState({
        cycles: [
          {
            id: 'cycle1',
            startDate: '2025-10-01T00:00:00.000Z',
            endDate: '2025-10-05T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2025-10-01T00:00:00.000Z',
            updatedAt: '2025-10-05T00:00:00.000Z',
          },
          {
            id: 'cycle2',
            startDate: '2025-10-29T00:00:00.000Z',
            endDate: null, // En cours
            periodLength: null,
            cycleLength: null,
            createdAt: '2025-10-29T00:00:00.000Z',
            updatedAt: '2025-10-29T00:00:00.000Z',
          },
        ],
      });
      
      const store = useCycleHistoryStore.getState();
      const current = store.getCurrentCycle();
      
      expect(current).not.toBeNull();
      expect(current?.id).toBe('cycle2');
      expect(current?.endDate).toBeNull();
    });

    it('devrait retourner null si aucun cycle ouvert', () => {
      useCycleHistoryStore.setState({
        cycles: [
          {
            id: 'cycle1',
            startDate: '2025-10-01T00:00:00.000Z',
            endDate: '2025-10-05T00:00:00.000Z',
            periodLength: 5,
            cycleLength: 28,
            createdAt: '2025-10-01T00:00:00.000Z',
            updatedAt: '2025-10-05T00:00:00.000Z',
          },
        ],
      });
      
      const store = useCycleHistoryStore.getState();
      expect(store.getCurrentCycle()).toBeNull();
    });
  });
});

