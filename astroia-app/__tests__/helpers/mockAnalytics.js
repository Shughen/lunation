/**
 * Helpers pour mocker Mixpanel / Analytics dans les tests
 * 
 * Ce module fournit des utilitaires réutilisables pour créer des mocks Mixpanel
 * cohérents dans tous les tests.
 */

/**
 * Mock instance de Mixpanel utilisée pour les tests
 */
let mockMixpanelInstance = null;

/**
 * Crée un mock de Mixpanel avec toutes les méthodes nécessaires
 * 
 * @returns {Object} Mock instance de Mixpanel
 * 
 * @example
 * const mockInstance = createMixpanelMockInstance();
 */
export function createMixpanelMockInstance() {
  return {
    init: jest.fn().mockResolvedValue(true),
    track: jest.fn().mockResolvedValue(true),
    identify: jest.fn().mockResolvedValue(true),
    getPeople: jest.fn(() => ({
      set: jest.fn().mockResolvedValue(true),
      setOnce: jest.fn().mockResolvedValue(true),
      increment: jest.fn().mockResolvedValue(true),
    })),
    reset: jest.fn(),
    timeEvent: jest.fn(),
    registerSuperProperties: jest.fn(),
    registerSuperPropertiesOnce: jest.fn(),
    setProfileProperties: jest.fn(),
  };
}

/**
 * Configure le mock global de Mixpanel
 * Cette fonction doit être appelée avant l'import de modules qui utilisent Mixpanel
 * 
 * @param {Object} customMock - Mock personnalisé (optionnel)
 * 
 * @example
 * setupAnalyticsMock();
 * // ou avec un mock personnalisé :
 * setupAnalyticsMock({
 *   track: jest.fn().mockRejectedValue(new Error('Failed'))
 * });
 */
export function setupAnalyticsMock(customMock = {}) {
  mockMixpanelInstance = { ...createMixpanelMockInstance(), ...customMock };
  
  // Le mock est déjà défini globalement dans jest.setup.js si nécessaire
  // Cette fonction permet de personnaliser le mock pour des tests spécifiques
  return mockMixpanelInstance;
}

/**
 * Réinitialise le mock Mixpanel entre les tests
 * 
 * @example
 * beforeEach(() => {
 *   resetAnalyticsMock();
 * });
 */
export function resetAnalyticsMock() {
  if (mockMixpanelInstance) {
    Object.keys(mockMixpanelInstance).forEach(key => {
      if (jest.isMockFunction(mockMixpanelInstance[key])) {
        mockMixpanelInstance[key].mockClear();
      }
    });
  }
  
  // Réinitialiser aussi le mock global si disponible
  try {
    const { Mixpanel } = require('mixpanel-react-native');
    if (Mixpanel && jest.isMockFunction(Mixpanel)) {
      Mixpanel.mockClear();
    }
  } catch (e) {
    // Mixpanel n'est pas disponible dans ce contexte, c'est ok
  }
}

/**
 * Récupère le mock instance actuel de Mixpanel
 * 
 * @returns {Object|null} Mock instance ou null si non disponible
 * 
 * @example
 * const instance = getMixpanelMockInstance();
 * expect(instance.track).toHaveBeenCalledWith('event_name', { prop: 'value' });
 */
export function getMixpanelMockInstance() {
  if (mockMixpanelInstance) {
    return mockMixpanelInstance;
  }
  
  // Essayer de récupérer depuis le mock global
  try {
    const { Mixpanel } = require('mixpanel-react-native');
    if (Mixpanel && jest.isMockFunction(Mixpanel)) {
      // Si Mixpanel a été appelé, retourner la dernière instance créée
      const calls = Mixpanel.mock.results;
      if (calls && calls.length > 0) {
        return calls[calls.length - 1].value;
      }
    }
  } catch (e) {
    // Mixpanel n'est pas disponible dans ce contexte
  }
  
  return null;
}

/**
 * Vérifie qu'un événement a été tracké
 * 
 * @param {string} eventName - Nom de l'événement attendu
 * @param {Object} expectedProperties - Propriétés attendues (optionnel)
 * @returns {boolean} - true si l'événement a été tracké
 * 
 * @example
 * expect(hasTrackedEvent('user_signed_up', { plan: 'premium' })).toBe(true);
 */
export function hasTrackedEvent(eventName, expectedProperties = undefined) {
  const instance = getMixpanelMockInstance();
  if (!instance || !instance.track) {
    return false;
  }
  
  const calls = instance.track.mock.calls;
  for (const call of calls) {
    const [trackedEvent, properties] = call;
    if (trackedEvent === eventName) {
      if (expectedProperties === undefined) {
        return true;
      }
      // Vérifier que toutes les propriétés attendues sont présentes
      for (const key in expectedProperties) {
        if (properties[key] !== expectedProperties[key]) {
          return false;
        }
      }
      return true;
    }
  }
  
  return false;
}

/**
 * Obtient toutes les propriétés trackées pour un événement
 * 
 * @param {string} eventName - Nom de l'événement
 * @returns {Array<Object>} - Liste des appels track avec leurs propriétés
 * 
 * @example
 * const calls = getTrackedEventCalls('button_clicked');
 * expect(calls[0].properties.buttonId).toBe('submit');
 */
export function getTrackedEventCalls(eventName) {
  const instance = getMixpanelMockInstance();
  if (!instance || !instance.track) {
    return [];
  }
  
  const calls = instance.track.mock.calls;
  return calls
    .filter(([trackedEvent]) => trackedEvent === eventName)
    .map(([event, properties]) => ({ event, properties }));
}

