/**
 * Helpers pour mocker les services API dans les tests
 * 
 * Ce module fournit des utilitaires réutilisables pour créer des mocks
 * cohérents des services utilisés dans l'application.
 */

/**
 * Crée un mock simple pour profileService
 * 
 * @param {Object} profileData - Profil à retourner par défaut (optionnel)
 * @param {Object} options - Options additionnelles (success/error)
 * @returns {Object} Mock de profileService
 * 
 * @example
 * const mockProfileService = createProfileServiceMock({
 *   name: 'Bianca',
 *   birthDate: new Date('1990-01-15'),
 * });
 */
export function createProfileServiceMock(profileData = null, options = {}) {
  const defaultProfile = profileData || {
    name: '',
    birthDate: null,
    birthTime: null,
    birthPlace: '',
    latitude: null,
    longitude: null,
    timezone: null,
  };

  const mockService = {
    profileService: {
      getCurrentProfile: jest.fn(() => {
        if (options.error) {
          return Promise.reject(options.error);
        }
        return Promise.resolve(defaultProfile);
      }),
      upsertProfile: jest.fn((profile) => {
        if (options.error) {
          return Promise.reject(options.error);
        }
        return Promise.resolve({ ...defaultProfile, ...profile });
      }),
      updateProfile: jest.fn((updates) => {
        if (options.error) {
          return Promise.reject(options.error);
        }
        return Promise.resolve({ ...defaultProfile, ...updates });
      }),
    },
  };

  return mockService;
}

/**
 * Crée un mock simple pour consentService
 * 
 * @param {Object} options - Options de configuration
 * @param {boolean} options.hasHealthConsent - Consentement santé par défaut
 * @param {boolean} options.hasAnalyticsConsent - Consentement analytics par défaut
 * @param {Error} options.error - Erreur à retourner (optionnel)
 * @returns {Object} Mock de consentService
 * 
 * @example
 * const mockConsentService = createConsentServiceMock({
 *   hasHealthConsent: true,
 *   hasAnalyticsConsent: false,
 * });
 */
export function createConsentServiceMock(options = {}) {
  const {
    hasHealthConsent = false,
    hasAnalyticsConsent = false,
    error = null,
  } = options;

  return {
    hasHealthConsent: jest.fn(() => {
      if (error) {
        return Promise.reject(error);
      }
      return Promise.resolve(hasHealthConsent);
    }),
    hasAnalyticsConsent: jest.fn(() => {
      if (error) {
        return Promise.reject(error);
      }
      return Promise.resolve(hasAnalyticsConsent);
    }),
    getConsents: jest.fn(() => {
      if (error) {
        return Promise.reject(error);
      }
      return Promise.resolve({
        health: hasHealthConsent,
        analytics: hasAnalyticsConsent,
      });
    }),
    updateConsent: jest.fn((type, value) => {
      if (error) {
        return Promise.reject(error);
      }
      return Promise.resolve({ [type]: value });
    }),
  };
}

/**
 * Crée un mock simple pour natalReadingService
 * 
 * @param {Object} readingData - Données de lecture à retourner (optionnel)
 * @param {Object} options - Options additionnelles (success/error)
 * @returns {Object} Mock de natalReadingService
 * 
 * @example
 * const mockNatalReadingService = createNatalReadingServiceMock({
 *   subject_name: 'Bianca',
 *   summary: { big_three: {} },
 * });
 */
export function createNatalReadingServiceMock(readingData = null, options = {}) {
  const defaultReading = readingData || {
    subject_name: 'Test Subject',
    summary: {
      big_three: {},
      dominant_element: 'Feu',
    },
    positions: [],
    aspects: [],
    source: 'fastapi',
    api_calls_count: 1,
  };

  return {
    computeNatalReadingForCurrentUser: jest.fn(() => {
      if (options.error) {
        return Promise.reject(options.error);
      }
      return Promise.resolve({
        reading: defaultReading,
        meta: {
          provider: 'fastapi',
          version: 'v1',
          computed_at: new Date().toISOString(),
        },
      });
    }),
    getLatestNatalReading: jest.fn(() => {
      if (options.error) {
        return Promise.reject(options.error);
      }
      return Promise.resolve({
        reading: defaultReading,
        meta: {
          provider: 'fastapi',
          version: 'v1',
          computed_at: new Date().toISOString(),
        },
      });
    }),
  };
}

/**
 * Réinitialise tous les mocks de services entre les tests
 * 
 * @example
 * beforeEach(() => {
 *   resetServicesMocks();
 * });
 */
export function resetServicesMocks() {
  jest.clearAllMocks();
}

/**
 * Configure les mocks Jest pour un service spécifique
 * 
 * @param {string} servicePath - Chemin du service (ex: '@/lib/api/profileService')
 * @param {Object} mockImplementation - Implémentation du mock
 * 
 * @example
 * setupServiceMock('@/lib/api/profileService', createProfileServiceMock());
 */
export function setupServiceMock(servicePath, mockImplementation) {
  jest.mock(servicePath, () => mockImplementation);
}
