// Les mocks pour expo-constants et supabase sont maintenant dans jest.setup.js

jest.mock('@/lib/api/profileService', () => ({
  profileService: {
    getCurrentProfile: jest.fn(),
  },
}));

jest.mock('@/lib/config/backend', () => ({
  getFastApiBaseUrl: jest.fn(() => 'https://fastapi.test'),
}));

import { supabase } from '@/lib/supabase';
import { profileService } from '@/lib/api/profileService';
import {
  computeNatalReadingForCurrentUser,
  getLatestNatalReading,
} from '@/lib/services/natalReadingService';
import { createQueryMock } from '../helpers/mockSupabase';

const sampleReading = {
  subject_name: 'Bianca',
  summary: { big_three: {}, dominant_element: 'Feu' },
  positions: [],
  aspects: [],
  source: 'fastapi',
  api_calls_count: 1,
};

beforeEach(() => {
  jest.clearAllMocks();
  global.fetch = jest.fn().mockResolvedValue({
    ok: true,
    json: async () => sampleReading,
  });
});

afterEach(() => {
  global.fetch.mockReset();
});

describe('natalReadingService', () => {
  it('persiste la lecture dans Supabase pour un utilisateur connecté', async () => {
    supabase.auth.getUser.mockResolvedValue({ data: { user: { id: 'user-1' } } });
    profileService.getCurrentProfile.mockResolvedValue({
      birthDate: new Date('1990-01-01'),
      birthTime: new Date('1990-01-01T10:00:00Z'),
      birthPlace: 'Paris',
      latitude: 48.8566,
      longitude: 2.3522,
      timezone: 'Europe/Paris',
    });

    supabase.from.mockReturnValue(
      createQueryMock({
        data: {
          id: 'reading-1',
          user_id: 'user-1',
          birth_data: {},
          reading: sampleReading,
          provider: 'fastapi',
          version: 'v1',
          computed_at: '2025-01-01T00:00:00.000Z',
        },
        error: null,
      })
    );

    const result = await computeNatalReadingForCurrentUser();

    expect(supabase.from).toHaveBeenCalledWith('natal_readings');
    expect(result.reading).toEqual(sampleReading);
    expect(result.meta.provider).toBe('fastapi');
  });

  it('retourne un résultat éphémère si utilisateur non connecté', async () => {
    supabase.auth.getUser.mockResolvedValue({ data: { user: null } });
    const birthData = {
      year: 1990,
      month: 3,
      day: 12,
      hour: 14,
      minute: 30,
      city: 'Paris',
      latitude: 48.8566,
      longitude: 2.3522,
      timezone: 'Europe/Paris',
    };

    const result = await computeNatalReadingForCurrentUser({ birthData });

    expect(result.isLocal).toBe(true);
    expect(supabase.from).not.toHaveBeenCalled();
  });

  it('récupère la dernière lecture depuis Supabase', async () => {
    supabase.auth.getUser.mockResolvedValue({ data: { user: { id: 'user-1' } } });
    supabase.from.mockReturnValue(
      createQueryMock({
        data: {
          id: 'reading-2',
          user_id: 'user-1',
          birth_data: {},
          reading: sampleReading,
          provider: 'fastapi',
          version: 'v1',
          computed_at: '2025-01-02T00:00:00.000Z',
        },
        error: null,
      })
    );

    const result = await getLatestNatalReading();

    expect(result.reading).toEqual(sampleReading);
  });
});


