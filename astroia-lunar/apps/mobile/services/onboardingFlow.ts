/**
 * Onboarding Flow Service
 *
 * Centralizes all onboarding routing logic to ensure sequential progression
 * and prevent rebounding or skipped steps.
 *
 * Flow:
 * /welcome → /onboarding/consent → /onboarding/profile-setup → /onboarding/chart-preview → /onboarding/disclaimer → /onboarding (slides) → / (Home)
 *
 * NOTE: This file does NOT import useOnboardingStore to avoid require cycles.
 * State is passed via a getter function parameter.
 */

import { Router } from 'expo-router';

/**
 * OnboardingState type
 * Represents the minimal state needed to determine next onboarding step
 */
export type OnboardingState = {
  hasSeenWelcomeScreen: boolean;
  hasAcceptedConsent: boolean;
  hasCompletedProfile: boolean;
  hasSeenChartPreview: boolean;
  hasSeenDisclaimer: boolean;
  hasCompletedOnboarding: boolean;
};

/**
 * Pure function that calculates the next onboarding step based on state
 *
 * @param state - Current onboarding state
 * @returns Next route to navigate to
 */
export function getNextOnboardingStep(state: OnboardingState): string {
  // Sequential guards - first incomplete step determines next route
  if (!state.hasSeenWelcomeScreen) {
    return '/welcome';
  }
  if (!state.hasAcceptedConsent) {
    return '/onboarding/consent';
  }
  if (!state.hasCompletedProfile) {
    return '/onboarding/profile-setup';
  }
  if (!state.hasSeenChartPreview) {
    return '/onboarding/chart-preview';
  }
  if (!state.hasSeenDisclaimer) {
    return '/onboarding/disclaimer';
  }
  if (!state.hasCompletedOnboarding) {
    return '/onboarding'; // Slides
  }

  // All steps completed → Home
  return '/';
}

/**
 * Ordered list of onboarding steps for navigation
 */
const ONBOARDING_STEPS = [
  '/welcome',
  '/onboarding/consent',
  '/onboarding/profile-setup',
  '/onboarding/chart-preview',
  '/onboarding/disclaimer',
  '/onboarding', // slides
] as const;

/**
 * Get the previous step in the onboarding flow
 *
 * @param currentStep - Current step identifier (e.g., 'PROFILE-SETUP', 'CONSENT')
 * @returns Previous route or null if at the beginning
 */
export function getPreviousOnboardingStep(currentStep: string): string | null {
  // Map step identifiers to routes
  const stepToRoute: Record<string, string> = {
    'WELCOME': '/welcome',
    'CONSENT': '/onboarding/consent',
    'PROFILE-SETUP': '/onboarding/profile-setup',
    'CHART-PREVIEW': '/onboarding/chart-preview',
    'DISCLAIMER': '/onboarding/disclaimer',
    'SLIDES': '/onboarding',
  };

  const currentRoute = stepToRoute[currentStep];
  if (!currentRoute) {
    console.warn(`[ONBOARDING_FLOW] Unknown step: ${currentStep}`);
    return null;
  }

  const currentIndex = ONBOARDING_STEPS.indexOf(currentRoute as any);
  if (currentIndex <= 0) {
    // Already at the first step, no previous
    return null;
  }

  return ONBOARDING_STEPS[currentIndex - 1];
}

/**
 * Navigate to the previous onboarding step
 *
 * @param router - Expo router instance
 * @param currentStep - Current step identifier (e.g., 'PROFILE-SETUP', 'CONSENT')
 */
export function goToPreviousOnboardingStep(
  router: Router,
  currentStep: string
): void {
  const previousStep = getPreviousOnboardingStep(currentStep);

  if (previousStep) {
    console.log(`[ONBOARDING_FLOW] back from=${currentStep} to=${previousStep}`);
    router.replace(previousStep as any);
  } else {
    console.log(`[ONBOARDING_FLOW] at first step (${currentStep}), cannot go back`);
  }
}

/**
 * Helper function that navigates to the next onboarding step with logging
 *
 * IMPORTANT: Receives a state getter to avoid circular dependencies with useOnboardingStore.
 * The getter ensures fresh state is read at navigation time.
 *
 * @param router - Expo router instance
 * @param sourceTag - Source identifier for logging (e.g., 'WELCOME', 'CONSENT')
 * @param getState - Function that returns fresh onboarding state (e.g., useOnboardingStore.getState)
 */
export async function goToNextOnboardingStep(
  router: Router,
  sourceTag: string,
  getState: () => OnboardingState
): Promise<void> {
  // Read FRESH state via the getter function
  // This ensures we get the most up-to-date state after async operations like setProfileData()
  const state = getState();

  const nextStep = getNextOnboardingStep(state);

  // Single comprehensive log line
  console.log(
    `[ONBOARDING_FLOW] from=${sourceTag} nextStep=${nextStep} state={` +
    `welcome=${state.hasSeenWelcomeScreen}, ` +
    `consent=${state.hasAcceptedConsent}, ` +
    `profile=${state.hasCompletedProfile}, ` +
    `chartPreview=${state.hasSeenChartPreview}, ` +
    `disclaimer=${state.hasSeenDisclaimer}, ` +
    `completed=${state.hasCompletedOnboarding}}`
  );

  // Navigate to next step using replace (not push) to avoid back-stack issues
  router.replace(nextStep as any);
}
