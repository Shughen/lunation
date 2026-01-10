import { Stack } from 'expo-router';

/**
 * Layout pour le groupe de routes (auth)
 * Gère les écrans d'authentification : login, signup, verify-otp
 */
export default function AuthLayout() {
  return (
    <Stack
      screenOptions={{
        headerShown: false,
        contentStyle: { backgroundColor: '#0F172A' },
      }}
    >
      <Stack.Screen name="login" />
      <Stack.Screen name="signup" />
      <Stack.Screen name="verify-otp" />
    </Stack>
  );
}

