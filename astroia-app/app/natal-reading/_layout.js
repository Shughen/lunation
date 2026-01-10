/**
 * Layout pour la section Thème Natal
 * Redirige automatiquement vers setup ou index selon les données
 */

import { useEffect } from 'react';
import { Stack } from 'expo-router';

export default function NatalReadingLayout() {
  return (
    <Stack
      screenOptions={{
        headerShown: false,
        animation: 'slide_from_right',
      }}
    >
      <Stack.Screen name="index" />
      <Stack.Screen name="setup" />
    </Stack>
  );
}

