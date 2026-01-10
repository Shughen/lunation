/**
 * Tests ciblés pour natalService (Supabase comme source de vérité)
 */

// Mock global fetch
global.fetch = jest.fn();

// Les mocks pour expo-constants, AsyncStorage et supabase sont maintenant dans jest.setup.js

jest.mock('@/lib/api/natalServiceRapidAPI', () => ({
  natalServiceRapidAPI: {
    computeNatalChart: jest.fn(),
  },
}));

import { supabase } from '@/lib/supabase';
import { natalServiceRapidAPI } from '@/lib/api/natalServiceRapidAPI';
import { natalService } from '@/lib/api/natalService';
import { createQueryMock } from '../helpers/mockSupabase';
import { resetAsyncStorageMock, setItemMock } from '../helpers/mockAsyncStorage';

describe('natalService → Supabase', () => {
  const profileData = {
    birthDate: new Date('1990-03-21T00:00:00.000Z'),
    birthTime: new Date('1990-03-21T12:00:00.000Z'),
    birthPlace: 'Paris',
    lat: 48.8566,
    lon: 2.3522,
    tz: 'Europe/Paris',
  };

  beforeEach(() => {
    jest.clearAllMocks();
    supabase.rpc = jest.fn().mockResolvedValue({ data: true, error: null });
    natalService.localChartCache = null;
    
    // Réinitialiser le mock AsyncStorage
    resetAsyncStorageMock();
    
    // Mock fetch par défaut pour retourner une réponse JSON valide
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => ({
        chart: {
          sun: { sign: 'Bélier', emoji: '♈', degree: 0, minutes: 0 },
        },
        meta: {
          provider: 'local',
          version: 'v1',
          computed_at: '2025-01-01T00:00:00.000Z',
        },
      }),
    });
  });

  it('enregistre le thème natal dans Supabase pour un user connecté', async () => {
    const supabaseRow = {
      id: 'chart-123',
      user_id: 'user-1',
      positions: {
        sun: { sign: 'Bélier', emoji: '♈', degree: 0, minutes: 0 },
      },
      version: 'rapidapi-v3',
      computed_at: '2025-01-01T00:00:00.000Z',
    };

    supabase.auth.getUser.mockResolvedValue({ data: { user: { id: 'user-1' } } });
    
    // Mock fetch pour retourner les données attendues
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => ({
        chart: supabaseRow.positions,
        meta: {
          provider: 'rapidapi',
          version: 'rapidapi-v3',
          computed_at: supabaseRow.computed_at,
        },
      }),
    });

    supabase.from.mockReturnValue(createQueryMock({ data: supabaseRow, error: null }));

    const result = await natalService.computeNatalChartForCurrentUser(profileData, { provider: 'rapidapi' });

    expect(supabase.from).toHaveBeenCalledWith('natal_charts');
    expect(result.positions.sun.sign).toBe('Bélier');
    // Le résultat peut venir du fetch mocké ou de Supabase, on vérifie juste qu'il a la structure attendue
    expect(result.positions).toBeDefined();
  });

  it('retourne un résultat uniquement en mémoire pour un user non connecté', async () => {
    supabase.auth.getUser.mockResolvedValue({ data: { user: null } });
    
    // Mock AsyncStorage vide au départ
    resetAsyncStorageMock();
    
    // Mock fetch pour retourner les données attendues
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => ({
        chart: {
          sun: { sign: 'Bélier', emoji: '♈', degree: 0, minutes: 0 },
        },
        meta: { provider: 'rapidapi', version: 'rapidapi-v3', computed_at: '2025-01-01T00:00:00.000Z' },
      }),
    });

    const result = await natalService.computeNatalChartForCurrentUser(profileData, { provider: 'rapidapi' });

    expect(result.local).toBe(true);
    expect(supabase.from).not.toHaveBeenCalled();
    
    // Vérifier que les données ont été sauvegardées dans AsyncStorage
    const AsyncStorage = require('@react-native-async-storage/async-storage');
    expect(AsyncStorage.setItem).toHaveBeenCalledWith(
      'natal_chart_local',
      expect.stringContaining('"local":true')
    );

    // Configurer le mock pour retourner les données sauvegardées
    setItemMock('natal_chart_local', JSON.stringify(result));

    const latest = await natalService.getLatestNatalChart();
    expect(latest).not.toBeNull();
    expect(latest.local).toBe(true);
  });
});


