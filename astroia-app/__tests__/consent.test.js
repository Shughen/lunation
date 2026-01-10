/**
 * Tests de conformité RGPD – Consentement santé
 * Test A: Sans consentement santé, navigation vers cycle-astro doit afficher une alerte
 * 
 * TODO(remi): Ce test est skip car il nécessite une configuration Jest complexe pour mocker
 * tous les modules Expo (expo-linear-gradient, expo-router, etc.) utilisés par CycleAstroScreen.
 * Pour faire passer ce test, il faudrait :
 * 1. Ajouter tous les modules Expo dans transformIgnorePatterns dans package.json
 * 2. Ou mocker complètement CycleAstroScreen avec un composant simplifié
 * 3. Ou migrer ce test vers un test d'intégration E2E avec Detox/Maestro
 */

// Les mocks pour expo-constants, supabase et AsyncStorage sont maintenant dans jest.setup.js

// Mock dependencies
jest.mock('expo-router', () => ({
  Stack: () => null,
  router: {
    back: jest.fn(),
    push: jest.fn(),
  },
}));

jest.mock('@/stores/profileStore', () => ({
  useProfileStore: jest.fn(() => ({
    profile: { birthDate: '1990-01-01' },
    getSunSign: jest.fn(() => 'Bélier'),
    getMoonSign: jest.fn(() => 'Gémeaux'),
    getAscendant: jest.fn(() => 'Lion'),
  })),
}));

jest.mock('@/hooks/useHapticFeedback', () => ({
  useHapticFeedback: jest.fn(() => ({
    selectionFeedback: jest.fn(),
    impactFeedback: jest.fn(),
    successFeedback: jest.fn(),
    errorFeedback: jest.fn(),
  })),
}));

jest.mock('@/components/MedicalDisclaimer', () => ({
  MedicalDisclaimer: () => null,
}));

// Mock Alert
const mockAlert = jest.fn();
jest.spyOn(require('react-native'), 'Alert', 'get').mockReturnValue({
  alert: mockAlert,
});

describe.skip('Conformité RGPD - Consentement santé', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('Test A: Bloque l\'accès à Cycle & Astro sans consentement santé', async () => {
    // Simuler absence de consentement
    jest.spyOn(consentService, 'hasHealthConsent').mockResolvedValue(false);

    // Render component
    // const CycleAstroScreen = require('@/app/cycle-astro/index').default;
    // render(<CycleAstroScreen />);

    // Attendre que le check de consentement soit effectué
    await waitFor(() => {
      expect(consentService.hasHealthConsent).toHaveBeenCalled();
    });

    // Vérifier qu'une alerte a été affichée
    await waitFor(() => {
      expect(mockAlert).toHaveBeenCalledWith(
        'Consentement requis',
        expect.stringContaining('données de cycle'),
        expect.arrayContaining([
          expect.objectContaining({ text: 'Annuler' }),
          expect.objectContaining({ text: 'Voir les paramètres' }),
        ])
      );
    });
  });

  it('Test A bis: Permet l\'accès à Cycle & Astro avec consentement santé', async () => {
    // Simuler présence de consentement
    jest.spyOn(consentService, 'hasHealthConsent').mockResolvedValue(true);

    // Render component
    // const CycleAstroScreen = require('@/app/cycle-astro/index').default;
    // render(<CycleAstroScreen />);

    // Attendre que le check de consentement soit effectué
    await waitFor(() => {
      expect(consentService.hasHealthConsent).toHaveBeenCalled();
    });

    // Vérifier qu'AUCUNE alerte n'a été affichée
    expect(mockAlert).not.toHaveBeenCalled();
  });
});

