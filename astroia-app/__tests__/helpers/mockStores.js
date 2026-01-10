/**
 * Helpers pour mocker les stores Zustand dans les tests
 * 
 * Ce module fournit des utilitaires réutilisables pour créer des mocks
 * cohérents des stores Zustand utilisés dans l'application.
 */

/**
 * Crée un mock simple pour profileStore
 * 
 * @param {Object} profileData - Données du profil à utiliser dans le mock
 * @returns {Object} Mock de profileStore avec getState configuré
 * 
 * @example
 * const mockProfileStore = createProfileStoreMock({
 *   name: 'Bianca',
 *   birthDate: new Date('1990-01-15'),
 *   sunSign: { name: 'Scorpion' },
 * });
 */
export function createProfileStoreMock(profileData = {}) {
  const defaultProfile = {
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
    ...profileData,
  };

  return {
    useProfileStore: {
      getState: jest.fn(() => ({
        profile: defaultProfile,
      })),
      setState: jest.fn(),
      getSunSign: jest.fn(() => defaultProfile.sunSign),
      getMoonSign: jest.fn(() => defaultProfile.moonSign),
      getAscendant: jest.fn(() => defaultProfile.ascendant),
    },
  };
}

/**
 * Crée un mock simple pour cycleHistoryStore
 * 
 * @param {Array} cycles - Cycles initiaux (optionnel)
 * @returns {Object} Mock de cycleHistoryStore
 * 
 * @example
 * const mockCycleStore = createCycleHistoryStoreMock([
 *   { id: 1, startDate: '2025-01-01', length: 28 }
 * ]);
 */
export function createCycleHistoryStoreMock(cycles = []) {
  return {
    useCycleHistoryStore: {
      getState: jest.fn(() => ({
        cycles,
      })),
      setState: jest.fn(),
      addCycle: jest.fn(),
      removeCycle: jest.fn(),
      getLatestCycle: jest.fn(() => cycles[cycles.length - 1] || null),
    },
  };
}

/**
 * Crée un mock simple pour useLunarRevolutionStore
 * 
 * @param {Object} revolutionData - Données de révolution (optionnel)
 * @returns {Object} Mock de useLunarRevolutionStore
 * 
 * @example
 * const mockLunarStore = createLunarRevolutionStoreMock({
 *   currentMonthRevolution: { month: '2025-01', moonSign: 'Bélier' }
 * });
 */
export function createLunarRevolutionStoreMock(revolutionData = {}) {
  const defaultState = {
    currentMonthRevolution: null,
    historyByMonth: {},
    status: 'idle',
    error: null,
    ...revolutionData,
  };

  return {
    useLunarRevolutionStore: {
      getState: jest.fn(() => defaultState),
      setState: jest.fn(),
      fetchForMonth: jest.fn(),
      getForMonth: jest.fn(() => defaultState.currentMonthRevolution),
    },
  };
}

/**
 * Réinitialise tous les stores mockés entre les tests
 * Cette fonction est utile dans beforeEach() pour nettoyer l'état
 * 
 * @param {Object} stores - Objets des stores à réinitialiser (optionnel)
 * 
 * @example
 * beforeEach(() => {
 *   resetStoresMocks();
 * });
 */
export function resetStoresMocks(stores = {}) {
  // Réinitialiser les mocks Jest
  jest.clearAllMocks();
  
  // Si on a des instances de stores passées, les réinitialiser
  if (stores.useLunarRevolutionStore && stores.useLunarRevolutionStore.setState) {
    stores.useLunarRevolutionStore.setState({
      currentMonthRevolution: null,
      historyByMonth: {},
      status: 'idle',
      error: null,
    });
  }
  
  if (stores.useCycleHistoryStore && stores.useCycleHistoryStore.setState) {
    stores.useCycleHistoryStore.setState({
      cycles: [],
    });
  }
}

/**
 * Configure les mocks Jest pour un store spécifique
 * 
 * @param {string} storePath - Chemin du store (ex: '@/stores/profileStore')
 * @param {Object} mockImplementation - Implémentation du mock
 * 
 * @example
 * setupStoreMock('@/stores/profileStore', createProfileStoreMock({
 *   name: 'Test User'
 * }));
 */
export function setupStoreMock(storePath, mockImplementation) {
  jest.mock(storePath, () => mockImplementation);
}
