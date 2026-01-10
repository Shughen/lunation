/**
 * Helpers pour mocker AsyncStorage dans les tests
 * 
 * Ce module fournit des utilitaires réutilisables pour créer des mocks AsyncStorage
 * cohérents dans tous les tests. Les mocks globaux sont définis dans jest.setup.js,
 * ce helper fournit des fonctions de convenance pour les utiliser.
 */

import AsyncStorage from '@react-native-async-storage/async-storage';

/**
 * Mock en mémoire pour simuler le stockage AsyncStorage
 * Les tests peuvent utiliser ce store pour vérifier les valeurs stockées
 */
let mockStorage = {};

/**
 * Réinitialise le mock AsyncStorage pour un nouveau test
 * 
 * @param {Object} initialData - Données initiales à charger dans le mock (optionnel)
 * 
 * @example
 * resetAsyncStorageMock({ key1: 'value1', key2: 'value2' });
 */
export function resetAsyncStorageMock(initialData = {}) {
  mockStorage = { ...initialData };
  
  // Réinitialiser les mocks Jest
  jest.clearAllMocks();
  
  // Configurer les mocks pour utiliser le store en mémoire
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
  
  AsyncStorage.getAllKeys.mockImplementation(() => {
    return Promise.resolve(Object.keys(mockStorage));
  });
  
  AsyncStorage.multiRemove = AsyncStorage.multiRemove || jest.fn();
  if (AsyncStorage.multiRemove) {
    AsyncStorage.multiRemove.mockImplementation((keys) => {
      keys.forEach(key => delete mockStorage[key]);
      return Promise.resolve(undefined);
    });
  }
}

/**
 * Configure le mock AsyncStorage pour retourner une valeur spécifique pour une clé
 * 
 * @param {string} key - Clé à mocker
 * @param {string|null} value - Valeur à retourner (ou null si non trouvé)
 * 
 * @example
 * setItemMock('user_preferences', JSON.stringify({ theme: 'dark' }));
 */
export function setItemMock(key, value) {
  if (value === null || value === undefined) {
    delete mockStorage[key];
  } else {
    mockStorage[key] = value;
  }
  
  AsyncStorage.getItem.mockImplementation((requestedKey) => {
    if (requestedKey === key) {
      return Promise.resolve(value);
    }
    return Promise.resolve(mockStorage[requestedKey] || null);
  });
}

/**
 * Récupère la valeur actuellement stockée dans le mock pour une clé
 * 
 * @param {string} key - Clé à récupérer
 * @returns {string|null} - Valeur stockée ou null
 * 
 * @example
 * const value = getItemMock('user_preferences');
 */
export function getItemMock(key) {
  return mockStorage[key] || null;
}

/**
 * Vérifie qu'une clé a été stockée dans AsyncStorage
 * 
 * @param {string} key - Clé à vérifier
 * @param {string} expectedValue - Valeur attendue (optionnel)
 * @returns {boolean} - true si la clé existe (et correspond à expectedValue si fourni)
 * 
 * @example
 * expect(hasItemMock('user_preferences', JSON.stringify({ theme: 'dark' }))).toBe(true);
 */
export function hasItemMock(key, expectedValue = undefined) {
  if (!(key in mockStorage)) {
    return false;
  }
  if (expectedValue !== undefined) {
    return mockStorage[key] === expectedValue;
  }
  return true;
}

/**
 * Supprime toutes les données du mock
 * 
 * @example
 * clearAsyncStorageMock();
 */
export function clearAsyncStorageMock() {
  mockStorage = {};
  resetAsyncStorageMock();
}

// Par défaut, initialiser le mock avec un store vide
// Les tests peuvent appeler resetAsyncStorageMock() avec des données initiales si nécessaire
resetAsyncStorageMock();

