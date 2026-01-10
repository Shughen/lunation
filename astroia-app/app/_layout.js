import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { useEffect } from 'react';
import { useProfileStore } from '@/stores/profileStore';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { useLunarRevolutionStore } from '@/stores/useLunarRevolutionStore';
import { useAuthStore } from '@/stores/authStore';
import { migrateCycleDataIfNeeded } from '@/lib/services/cycleMigration';

export default function RootLayout() {
  const loadProfile = useProfileStore((state) => state.loadProfile);
  const loadCycles = useCycleHistoryStore((state) => state.loadCycles);
  const loadRevolutions = useLunarRevolutionStore((state) => state.loadFromStorage);
  const initializeAuth = useAuthStore((state) => state.initialize);
  
  useEffect(() => {
    const initializeApp = async () => {
      try {
        console.log('[ROUTING] Mounted RootLayout');
        console.log('[App] Initialisation de l\'authentification...');
        // Initialiser l'authentification en premier
        await initializeAuth();
        
        console.log('[App] Chargement du profil au démarrage...');
        try {
          await loadProfile();
        } catch (error) {
          console.error('[App] Erreur lors du chargement du profil:', error);
          // Continuer même en cas d'erreur
        }
        
        // Migration + chargement historique cycles
        try {
          await migrateCycleDataIfNeeded();
          await loadCycles();
        } catch (error) {
          console.error('[App] Erreur lors de l\'initialisation des cycles:', error);
        }
        
        // Charger le cache des révolutions lunaires
        try {
          loadRevolutions();
        } catch (error) {
          console.error('[App] Erreur lors du chargement des révolutions:', error);
        }
      } catch (error) {
        console.error('[App] Erreur critique lors de l\'initialisation:', error);
      }
    };

    initializeApp();
  }, []);

  return (
    <>
      <StatusBar style="light" />
      <Stack
        screenOptions={{
          headerShown: false,
          contentStyle: { backgroundColor: '#0F172A' },
        }}
      >
        <Stack.Screen name="index" />
        {/* Expo Router découvre automatiquement les autres routes depuis la structure de fichiers */}
        {/* Les groupes (auth) et onboarding ont leurs propres _layout.js */}
      </Stack>
    </>
  );
}
