/**
 * Routing Guard Screen
 * Handles authentication and onboarding flow before redirecting to main app
 */

import React, { useEffect, useRef } from 'react';
import { View, StyleSheet } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { useAuthStore } from '../stores/useAuthStore';
import { useOnboardingStore } from '../stores/useOnboardingStore';
import { useResetStore } from '../stores/useResetStore';
import { isDevAuthBypassActive } from '../services/api';
import { colors, spacing } from '../constants/theme';
import { cleanupGhostFlags } from '../services/onboardingMigration';
import { isProfileComplete } from '../utils/onboardingHelpers';
import { MoonLoader } from '../components/MoonLoader';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors: bgColors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: bgColors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

export default function RoutingGuardScreen() {
  const router = useRouter();
  const { isAuthenticated } = useAuthStore();

  // Onboarding store selectors
  const isOnboardingHydrated = useOnboardingStore((state) => state.hydrated);
  const hasSeenWelcomeScreen = useOnboardingStore((state) => state.hasSeenWelcomeScreen);
  const hasAcceptedConsent = useOnboardingStore((state) => state.hasAcceptedConsent);
  const hasCompletedProfile = useOnboardingStore((state) => state.hasCompletedProfile);
  const hasSeenDisclaimer = useOnboardingStore((state) => state.hasSeenDisclaimer);
  const hasCompletedOnboarding = useOnboardingStore((state) => state.hasCompletedOnboarding);
  const hydrateOnboarding = useOnboardingStore((state) => state.hydrate);
  const resetProfileFlag = useOnboardingStore((state) => state.resetProfileFlag);
  const profileData = useOnboardingStore((state) => state.profileData);

  const { isResetting } = useResetStore();

  // Guards refs
  const routingInFlightRef = useRef(false);
  const selfHealExecutedRef = useRef(false);
  const hydrationTriggeredRef = useRef(false);

  // Effect d'hydratation - fire-and-forget, se déclenche une seule fois au mount
  useEffect(() => {
    if (!isOnboardingHydrated && !hydrationTriggeredRef.current) {
      hydrationTriggeredRef.current = true;
      console.log('[INDEX] Triggering hydration...');
      cleanupGhostFlags().then(() => hydrateOnboarding());
    }
  }, [isOnboardingHydrated, hydrateOnboarding]);

  // Guards de routing : vérifier auth, onboarding et profil complet
  useEffect(() => {
    const checkRouting = async () => {
      // Guard 1: Attendre hydratation
      if (!isOnboardingHydrated) {
        console.log('[INDEX] Waiting for hydration...');
        return;
      }

      // Guard 2: Ne pas router pendant reset
      if (isResetting) {
        console.log('[INDEX] Reset in progress, skip routing');
        return;
      }

      // Guard 3: Éviter double-run pendant un routing en cours
      if (routingInFlightRef.current) {
        console.log('[INDEX] Routing already in progress, skip');
        return;
      }

      routingInFlightRef.current = true;

      try {
        console.log('[INDEX] Starting routing check');

        // SELF-HEAL: Vérifier et corriger incohérences profil/flags
        if (!selfHealExecutedRef.current) {
          const profileIsComplete = isProfileComplete(profileData);

          if ((hasCompletedProfile || hasCompletedOnboarding) && !profileIsComplete) {
            console.log('[SELF_HEAL] Profile incomplete, resetting flag');
            await resetProfileFlag();
            selfHealExecutedRef.current = true;
            router.replace('/onboarding/profile-setup');
            return;
          }

          selfHealExecutedRef.current = true;
        }

        const isBypassActive = isDevAuthBypassActive();

        // A) Vérifier auth
        if (!isBypassActive && !isAuthenticated) {
          console.log('[INDEX] Redirecting to /auth');
          router.replace('/auth');
          return;
        }

        // B) Vérifier welcome screen
        if (!hasSeenWelcomeScreen) {
          console.log('[INDEX] Redirecting to /welcome');
          router.replace('/welcome');
          return;
        }

        // C) Vérifier consentement RGPD
        if (!hasAcceptedConsent) {
          console.log('[INDEX] Redirecting to /onboarding/consent');
          router.replace('/onboarding/consent');
          return;
        }

        // D) Vérifier profil setup
        if (!hasCompletedProfile) {
          console.log('[INDEX] Redirecting to /onboarding/profile-setup');
          router.replace('/onboarding/profile-setup');
          return;
        }

        // E) Vérifier disclaimer médical
        if (!hasSeenDisclaimer) {
          console.log('[INDEX] Redirecting to /onboarding/disclaimer');
          router.replace('/onboarding/disclaimer');
          return;
        }

        // F) Vérifier onboarding complet
        if (!hasCompletedOnboarding) {
          console.log('[INDEX] Redirecting to /onboarding');
          router.replace('/onboarding');
          return;
        }

        // All guards passed - redirect to tabs
        console.log('[INDEX] All guards passed, redirecting to (tabs)/home');
        router.replace('/(tabs)/home');
      } catch (error) {
        console.error('[INDEX] Error in routing check:', error);
        router.replace('/auth');
      } finally {
        routingInFlightRef.current = false;
      }
    };

    checkRouting();
  }, [
    isAuthenticated,
    isResetting,
    isOnboardingHydrated,
    hasSeenWelcomeScreen,
    hasAcceptedConsent,
    hasCompletedProfile,
    hasSeenDisclaimer,
    hasCompletedOnboarding,
    resetProfileFlag,
    profileData,
    router,
  ]);

  // Réinitialiser les guards quand l'hydratation change
  useEffect(() => {
    if (!isOnboardingHydrated) {
      selfHealExecutedRef.current = false;
      hydrationTriggeredRef.current = false;
    }
  }, [isOnboardingHydrated]);

  // Always show loader - this screen redirects immediately
  return (
    <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
      <View style={styles.center}>
        <MoonLoader size="large" text="Chargement..." />
      </View>
    </LinearGradientComponent>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: spacing.xl,
  },
});
