/**
 * Tests unitaires pour useLunarRevolutionStore
 */

import { renderHook, act, waitFor } from '@testing-library/react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useLunarRevolutionStore } from '@/stores/useLunarRevolutionStore';

// Le mock AsyncStorage est maintenant dans jest.setup.js

// Mock profileStore
jest.mock('@/stores/profileStore', () => ({
  useProfileStore: {
    getState: jest.fn(() => ({
      profile: {
        birthDate: new Date('1990-01-15'),
        birthTime: new Date('1990-01-15T12:00:00'),
        birthPlace: 'Paris',
        latitude: 48.8566,
        longitude: 2.3522,
        timezone: 'Europe/Paris',
      },
    })),
  },
}));

// Mock lunarRevolutionService
jest.mock('@/lib/services/lunarRevolutionService', () => ({
  getLunarRevolution: jest.fn(() => Promise.resolve({
    month: '2025-01',
    revolutionDate: '2025-01-15T12:00:00Z',
    moonSign: 'Bélier',
    moonSignEmoji: '♈',
    moonDegree: 10,
    house: 1,
    phase: 'new',
    phaseName: 'Nouvelle lune',
    aspects: [],
    interpretationSummary: 'Test interpretation',
    focus: 'identité et image de soi',
  })),
  getCachedRevolution: jest.fn(() => Promise.resolve(null)),
}));

describe('useLunarRevolutionStore', () => {
  beforeEach(() => {
    jest.clearAllMocks();
    // Reset store state
    useLunarRevolutionStore.setState({
      currentMonthRevolution: null,
      historyByMonth: {},
      status: 'idle',
      error: null,
    });
  });

  it('devrait initialiser avec un état vide', () => {
    const { result } = renderHook(() => useLunarRevolutionStore());
    
    expect(result.current.currentMonthRevolution).toBeNull();
    expect(result.current.historyByMonth).toEqual({});
    expect(result.current.status).toBe('idle');
  });

  it('devrait charger une révolution pour un mois donné', async () => {
    const { result } = renderHook(() => useLunarRevolutionStore());
    const testDate = new Date(2025, 0, 1); // Janvier 2025

    await act(async () => {
      await result.current.fetchForMonth(testDate);
    });

    await waitFor(() => {
      expect(result.current.status).toBe('loaded');
    });

    const revolution = result.current.getForMonth(testDate);
    expect(revolution).not.toBeNull();
    expect(revolution?.month).toBe('2025-01');
  });

  it('devrait retourner null si aucune révolution n\'existe pour un mois', () => {
    const { result } = renderHook(() => useLunarRevolutionStore());
    const testDate = new Date(2025, 5, 1); // Juin 2025

    const revolution = result.current.getForMonth(testDate);
    expect(revolution).toBeNull();
  });

  it('devrait gérer les erreurs correctement', async () => {
    const { getLunarRevolution } = require('@/lib/services/lunarRevolutionService');
    getLunarRevolution.mockRejectedValueOnce(new Error('Test error'));

    const { result } = renderHook(() => useLunarRevolutionStore());
    const testDate = new Date(2025, 0, 1);

    await act(async () => {
      await result.current.fetchForMonth(testDate);
    });

    await waitFor(() => {
      expect(result.current.status).toBe('error');
      expect(result.current.error).toBeTruthy();
    });
  });
});

