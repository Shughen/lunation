import { Stack } from 'expo-router';

/**
 * Layout pour le groupe de routes onboarding
 * Gère les écrans d'onboarding : index, profile-setup, consent, cycle-setup, tour, disclaimer
 */
export default function OnboardingLayout() {
  return (
    <Stack
      screenOptions={{
        headerShown: false,
        contentStyle: { backgroundColor: '#0F172A' },
      }}
    >
      <Stack.Screen name="index" />
      <Stack.Screen name="profile-setup" />
      <Stack.Screen name="consent" />
      <Stack.Screen name="cycle-setup" />
      <Stack.Screen name="tour" />
      <Stack.Screen name="disclaimer" />
    </Stack>
  );
}

