/**
 * Configuration Jest globale
 * 
 * Mocks communs utilisés dans tous les tests :
 * - expo-constants : configuration Expo avec variables d'environnement
 * - AsyncStorage : stockage asynchrone React Native
 * - supabase : client Supabase de base (sans logique métier)
 */

// Mock expo-constants
jest.mock('expo-constants', () => ({
  default: {
    expoConfig: {
      extra: {
        supabaseUrl: 'https://test.supabase.co',
        supabaseAnonKey: 'test-key',
        aiApiUrl: 'https://example.com/api/ai/chat',
        fastapiBaseUrl: 'https://fastapi.test',
      },
    },
  },
}));

// Mock AsyncStorage
jest.mock('@react-native-async-storage/async-storage', () => ({
  getItem: jest.fn(),
  setItem: jest.fn(),
  removeItem: jest.fn(),
  getAllKeys: jest.fn(),
  multiRemove: jest.fn(),
  default: {
    getItem: jest.fn(),
    setItem: jest.fn(),
    removeItem: jest.fn(),
    getAllKeys: jest.fn(),
    multiRemove: jest.fn(),
  },
}));

// Mock Supabase client de base
// Les tests peuvent surcharger ces mocks si nécessaire
jest.mock('@/lib/supabase', () => ({
  supabase: {
    auth: {
      getUser: jest.fn(),
    },
    from: jest.fn(),
    rpc: jest.fn(),
  },
}));

