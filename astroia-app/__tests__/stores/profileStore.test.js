/**
 * Tests unitaires pour profileStore
 * 
 * Vérifie les deux modes :
 * - Mode invité : stockage local (AsyncStorage)
 * - Mode connecté : Supabase (via profileService)
 */

import { useProfileStore } from '@/stores/profileStore';
import { profileService } from '@/lib/api/profileService';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Mock profileService
jest.mock('@/lib/api/profileService', () => ({
  profileService: {
    isUserAuthenticated: jest.fn(),
    getCurrentProfile: jest.fn(),
    upsertProfile: jest.fn(),
  },
}));

// Mock AsyncStorage est déjà dans jest.setup.js

describe('profileStore', () => {
  // Store en mémoire pour les tests
  let mockStorage = {};

  beforeEach(() => {
    // Réinitialiser le store à son état initial
    useProfileStore.setState({
      profile: {
        name: '',
        birthDate: null,
        birthTime: null,
        birthPlace: '',
        latitude: null,
        longitude: null,
        timezone: null,
        sunSign: null,
        moonSign: null,
        ascendant: null,
        gender: null,
        hasCycles: false,
      },
      isLoading: false,
      hasProfile: false,
    });

    // Réinitialiser les mocks
    jest.clearAllMocks();
    mockStorage = {};

    // Configurer les mocks AsyncStorage
    AsyncStorage.getItem.mockImplementation((key) => {
      return Promise.resolve(mockStorage[key] || null);
    });

    AsyncStorage.setItem.mockImplementation((key, value) => {
      mockStorage[key] = value;
      return Promise.resolve(undefined);
    });

    AsyncStorage.removeItem.mockImplementation((key) => {
      delete mockStorage[key];
      return Promise.resolve(undefined);
    });

    // Mocks par défaut pour profileService
    profileService.isUserAuthenticated.mockResolvedValue(false);
    profileService.getCurrentProfile.mockResolvedValue(null);
    profileService.upsertProfile.mockResolvedValue(null);
  });

  describe('Mode invité (AsyncStorage)', () => {
    it('devrait charger un profil depuis AsyncStorage en mode invité', async () => {
      // Configuration : utilisateur non connecté
      profileService.isUserAuthenticated.mockResolvedValue(false);

      // Profil stocké localement
      const storedProfile = {
        name: 'Test User',
        birthDate: '1990-01-15T00:00:00.000Z',
        birthTime: '2000-01-01T12:00:00.000Z',
        birthPlace: 'Paris',
        latitude: 48.8566,
        longitude: 2.3522,
        timezone: 'Europe/Paris',
        gender: 'female',
        hasCycles: true,
      };

      mockStorage['@profile:guest'] = JSON.stringify(storedProfile);

      // Charger le profil
      await useProfileStore.getState().loadProfile();

      // Vérifier que le profil a été chargé
      const { profile, hasProfile } = useProfileStore.getState();
      expect(profile.name).toBe('Test User');
      expect(profile.birthPlace).toBe('Paris');
      expect(profile.gender).toBe('female');
      expect(profile.hasCycles).toBe(true);
      expect(hasProfile).toBe(true);

      // Vérifier qu'on n'a pas appelé Supabase
      expect(profileService.getCurrentProfile).not.toHaveBeenCalled();
      expect(AsyncStorage.getItem).toHaveBeenCalledWith('@profile:guest');
    });

    it('devrait sauvegarder un profil dans AsyncStorage en mode invité', async () => {
      // Configuration : utilisateur non connecté
      profileService.isUserAuthenticated.mockResolvedValue(false);

      const profileData = {
        name: 'New User',
        birthDate: new Date('1990-01-15'),
        birthTime: new Date('2000-01-01T12:00:00'),
        birthPlace: 'Lyon',
      };

      // Sauvegarder le profil
      await useProfileStore.getState().saveProfile(profileData);

      // Vérifier que le profil a été sauvegardé dans AsyncStorage
      expect(AsyncStorage.setItem).toHaveBeenCalledWith(
        '@profile:guest',
        expect.stringContaining('"name":"New User"')
      );

      // Vérifier que le store a été mis à jour
      const { profile } = useProfileStore.getState();
      expect(profile.name).toBe('New User');
      expect(profile.birthPlace).toBe('Lyon');

      // Vérifier qu'on n'a pas appelé Supabase
      expect(profileService.upsertProfile).not.toHaveBeenCalled();
    });

    it('devrait retourner un profil vide si rien n\'est stocké en mode invité', async () => {
      // Configuration : utilisateur non connecté, pas de profil stocké
      profileService.isUserAuthenticated.mockResolvedValue(false);
      AsyncStorage.getItem.mockResolvedValue(null);

      // Charger le profil
      await useProfileStore.getState().loadProfile();

      // Vérifier qu'on a un profil vide
      const { profile, hasProfile } = useProfileStore.getState();
      expect(profile.name).toBe('');
      expect(profile.birthDate).toBeNull();
      expect(hasProfile).toBe(false);
    });

    it('devrait supprimer le profil local lors d\'un reset en mode invité', async () => {
      // Configuration : utilisateur non connecté
      profileService.isUserAuthenticated.mockResolvedValue(false);

      // Sauvegarder un profil d'abord
      await useProfileStore.getState().saveProfile({
        name: 'Test',
        birthDate: new Date('1990-01-15'),
      });

      // Reset le profil
      await useProfileStore.getState().resetProfile();

      // Vérifier que AsyncStorage.removeItem a été appelé
      expect(AsyncStorage.removeItem).toHaveBeenCalledWith('@profile:guest');

      // Vérifier que le store est réinitialisé
      const { profile, hasProfile } = useProfileStore.getState();
      expect(profile.name).toBe('');
      expect(hasProfile).toBe(false);
    });
  });

  describe('Mode connecté (Supabase)', () => {
    it('devrait charger un profil depuis Supabase en mode connecté', async () => {
      // Configuration : utilisateur connecté
      profileService.isUserAuthenticated.mockResolvedValue(true);

      const supabaseProfile = {
        id: 'user-123',
        email: 'test@example.com',
        name: 'Supabase User',
        birthDate: new Date('1990-01-15'),
        birthTime: new Date('2000-01-01T12:00:00'),
        birthPlace: 'Paris',
        latitude: 48.8566,
        longitude: 2.3522,
        timezone: 'Europe/Paris',
        sunSign: { id: 1, name: 'Capricorne' },
        moonSign: { id: 5, name: 'Lion' },
        ascendant: { id: 9, name: 'Sagittaire' },
        gender: 'male',
        hasCycles: false,
      };

      profileService.getCurrentProfile.mockResolvedValue(supabaseProfile);

      // Charger le profil
      await useProfileStore.getState().loadProfile();

      // Vérifier que le profil a été chargé depuis Supabase
      const { profile, hasProfile } = useProfileStore.getState();
      expect(profile.name).toBe('Supabase User');
      expect(profile.id).toBe('user-123');
      expect(profile.email).toBe('test@example.com');
      expect(hasProfile).toBe(true);

      // Vérifier qu'on a appelé Supabase
      expect(profileService.getCurrentProfile).toHaveBeenCalled();
      
      // Vérifier qu'on a aussi mis en cache local
      expect(AsyncStorage.setItem).toHaveBeenCalled();
    });

    it('devrait sauvegarder un profil dans Supabase en mode connecté', async () => {
      // Configuration : utilisateur connecté
      profileService.isUserAuthenticated.mockResolvedValue(true);

      const profileData = {
        name: 'Updated User',
        birthDate: new Date('1990-01-15'),
        birthTime: new Date('2000-01-01T12:00:00'),
        birthPlace: 'Lyon',
      };

      const savedProfile = {
        id: 'user-123',
        email: 'test@example.com',
        ...profileData,
      };

      profileService.upsertProfile.mockResolvedValue(savedProfile);

      // Sauvegarder le profil
      await useProfileStore.getState().saveProfile(profileData);

      // Vérifier que le profil a été sauvegardé dans Supabase
      expect(profileService.upsertProfile).toHaveBeenCalledWith(
        expect.objectContaining({
          name: 'Updated User',
          birthPlace: 'Lyon',
        })
      );

      // Vérifier que le store a été mis à jour
      const { profile } = useProfileStore.getState();
      expect(profile.name).toBe('Updated User');
      expect(profile.id).toBe('user-123');

      // Vérifier qu'on a aussi mis en cache local
      expect(AsyncStorage.setItem).toHaveBeenCalled();
    });

    it('devrait utiliser le cache local si Supabase ne retourne rien en mode connecté', async () => {
      // Configuration : utilisateur connecté mais pas de profil Supabase
      profileService.isUserAuthenticated.mockResolvedValue(true);
      profileService.getCurrentProfile.mockResolvedValue(null);

      // Profil en cache local
      const cachedProfile = {
        name: 'Cached User',
        birthDate: '1990-01-15T00:00:00.000Z',
        birthTime: '2000-01-01T12:00:00.000Z',
        birthPlace: 'Paris',
      };

      mockStorage['@profile:guest'] = JSON.stringify(cachedProfile);

      // Charger le profil
      await useProfileStore.getState().loadProfile();

      // Vérifier qu'on a utilisé le cache local
      const { profile } = useProfileStore.getState();
      expect(profile.name).toBe('Cached User');

      // Vérifier qu'on a quand même appelé Supabase
      expect(profileService.getCurrentProfile).toHaveBeenCalled();
      expect(AsyncStorage.getItem).toHaveBeenCalledWith('@profile:guest');
    });

    it('devrait gérer les erreurs Supabase en fallback local', async () => {
      // Configuration : utilisateur connecté mais erreur Supabase
      profileService.isUserAuthenticated.mockResolvedValue(true);
      profileService.getCurrentProfile.mockRejectedValue(new Error('Supabase error'));

      // Profil en cache local
      const cachedProfile = {
        name: 'Fallback User',
        birthDate: '1990-01-15T00:00:00.000Z',
        birthTime: '2000-01-01T12:00:00.000Z',
        birthPlace: 'Paris',
      };

      mockStorage['@profile:guest'] = JSON.stringify(cachedProfile);

      // Charger le profil
      await useProfileStore.getState().loadProfile();

      // Vérifier qu'on a utilisé le cache local comme fallback
      const { profile } = useProfileStore.getState();
      expect(profile.name).toBe('Fallback User');
    });

    it('ne devrait pas supprimer le profil Supabase lors d\'un reset en mode connecté', async () => {
      // Configuration : utilisateur connecté
      profileService.isUserAuthenticated.mockResolvedValue(true);

      // Reset le profil
      await useProfileStore.getState().resetProfile();

      // Vérifier que AsyncStorage.removeItem n'a PAS été appelé
      expect(AsyncStorage.removeItem).not.toHaveBeenCalled();

      // Vérifier que le store est réinitialisé localement
      const { profile, hasProfile } = useProfileStore.getState();
      expect(profile.name).toBe('');
      expect(hasProfile).toBe(false);
    });
  });

  describe('Méthodes utilitaires', () => {
    it('devrait calculer le pourcentage de complétion correctement', () => {
      useProfileStore.setState({
        profile: {
          name: 'Test',
          birthDate: new Date('1990-01-15'),
          birthTime: new Date('2000-01-01T12:00:00'),
          birthPlace: 'Paris',
        },
      });

      const percentage = useProfileStore.getState().getCompletionPercentage();
      expect(percentage).toBe(100);
    });

    it('devrait retourner le signe solaire correctement', () => {
      const sunSign = { id: 1, name: 'Capricorne' };
      useProfileStore.setState({
        profile: {
          sunSign,
          birthDate: new Date('1990-01-15'),
        },
      });

      const result = useProfileStore.getState().getSunSign();
      expect(result).toEqual(sunSign);
    });

    it('devrait mettre à jour un champ spécifique', () => {
      useProfileStore.setState({
        profile: {
          name: 'Old Name',
        },
      });

      useProfileStore.getState().updateField('name', 'New Name');

      const { profile } = useProfileStore.getState();
      expect(profile.name).toBe('New Name');
    });
  });
});
