import { useEffect, useState, useRef } from 'react';
import { useRouter } from 'expo-router';
import { View, ActivityIndicator, StyleSheet } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { colors } from '@/constants/theme';
import { useAuthStore } from '@/stores/authStore';
import { useProfileStore } from '@/stores/profileStore';
import { isProfileComplete } from '@/stores/profileStore';

/**
 * Point d'entrée de l'application
 * Gère le routing conditionnel selon l'état d'authentification, onboarding et profil
 * 
 * Logique déterministe :
 * 1. Pas de session → /(auth)/login
 * 2. Session + profil incomplet → /onboarding
 * 3. Session + profil complet + onboarding_completed !== 'true' → /onboarding
 * 4. Session + profil complet + onboarding_completed === 'true' → /(tabs)/home
 */
export default function Index() {
  const router = useRouter();
  const { isAuthenticated, isLoading: authLoading, session } = useAuthStore();
  const { isLoading: profileLoading } = useProfileStore();
  const loadProfile = useProfileStore((state) => state.loadProfile);
  const [isChecking, setIsChecking] = useState(true);
  const hasRunRef = useRef(false); // Flag local pour éviter les appels multiples
  const previousSessionIdRef = useRef(null); // Pour détecter les changements de session

  // Réinitialiser le flag si la session change (déconnexion/reconnexion)
  useEffect(() => {
    const currentSessionId = session?.user?.id || null;
    if (previousSessionIdRef.current !== null && previousSessionIdRef.current !== currentSessionId) {
      console.log('[INDEX] Changement de session détecté, réinitialisation du flag de routing');
      hasRunRef.current = false;
    }
    previousSessionIdRef.current = currentSessionId;
  }, [session?.user?.id]);

  useEffect(() => {
    // Éviter les appels multiples
    if (hasRunRef.current) {
      console.log('[INDEX] Routing déjà vérifié, skip');
      return;
    }

    const checkRouting = async () => {
      try {
        console.log('[INDEX] checkRouting() - session=', !!session, 'authLoading=', authLoading, 'profileLoading=', profileLoading);

        // Étape 1 : Attendre que l'authentification soit initialisée
        if (authLoading) {
          console.log('[INDEX] Auth encore en chargement, attente...');
          return;
        }

        // Étape 2 : Si pas de session, rediriger vers login
        if (!isAuthenticated || !session) {
          console.log('[INDEX] Décision : redirection vers /(auth)/login (pas de session)');
          setIsChecking(false);
          hasRunRef.current = true;
          router.replace('/(auth)/login');
          return;
        }

        // Étape 3 : Charger le profil si nécessaire et attendre qu'il soit chargé
        if (profileLoading) {
          console.log('[INDEX] Profil en chargement, attente...');
          // Déclencher le chargement si pas déjà fait
          try {
            await loadProfile();
          } catch (error) {
            console.warn('[INDEX] Erreur chargement profil (non bloquant):', error);
          }
          
          // Attendre que le chargement soit terminé (max 3 secondes)
          let attempts = 0;
          const maxAttempts = 30; // 3 secondes max
          while (useProfileStore.getState().isLoading && attempts < maxAttempts) {
            await new Promise(resolve => setTimeout(resolve, 100));
            attempts++;
          }
          
          if (useProfileStore.getState().isLoading) {
            console.warn('[INDEX] Timeout chargement profil, continuation avec état actuel');
          }
        }

        // Étape 4 : Récupérer une vue stable du profil depuis le store
        const storeState = useProfileStore.getState();
        const profile = storeState.profile || {};
        const profileComplete = isProfileComplete(profile);

        console.log('[INDEX] Profil détecté :', {
          name: profile.name || '(vide)',
          birthDate: profile.birthDate ? 'présente' : '(manquante)',
          birthTime: profile.birthTime ? 'présente' : '(manquante)',
          birthPlace: profile.birthPlace || '(vide)',
          isComplete: profileComplete
        });

        // Étape 5 : Récupérer onboarding_completed depuis AsyncStorage
        const onboardingCompleted = await AsyncStorage.getItem('onboarding_completed');
        console.log('[INDEX] onboarding_completed =', onboardingCompleted);

        // Étape 6 : Appliquer la logique de routing déterministe
        setIsChecking(false);
        hasRunRef.current = true;

        // Cas 1 : Profil incomplet → toujours vers onboarding
        if (!profileComplete) {
          console.log('[INDEX] Décision : redirection vers /onboarding (profil incomplet)');
          router.replace('/onboarding');
          return;
        }

        // Cas 2 : Profil complet mais onboarding_completed !== 'true' → vers onboarding
        if (onboardingCompleted !== 'true') {
          console.log('[INDEX] Décision : redirection vers /onboarding (profil complet mais onboarding non terminé)');
          router.replace('/onboarding');
          return;
        }

        // Cas 3 : Profil complet ET onboarding_completed === 'true' → vers home
        console.log('[INDEX] Décision : redirection vers /(tabs)/home (profil complet + onboarding_completed === true)');
        router.replace('/(tabs)/home');
      } catch (error) {
        console.error('[INDEX] Erreur dans checkRouting:', error);
        setIsChecking(false);
        hasRunRef.current = true;
        // En cas d'erreur, rediriger vers login pour sécurité
        router.replace('/(auth)/login');
      }
    };

    checkRouting();
  }, [isAuthenticated, authLoading, session, router, loadProfile]); // Note: profileLoading retiré des dépendances pour éviter les boucles

  // Afficher un loader pendant la vérification
  // On attend que authLoading ET profileLoading soient terminés
  const isLoading = authLoading || isChecking || profileLoading;
  
  if (isLoading) {
    return (
      <LinearGradient
        colors={colors.darkBg}
        style={styles.container}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 1 }}
      >
        <View style={styles.loaderContainer}>
          <ActivityIndicator size="large" color={colors.accent} />
        </View>
      </LinearGradient>
    );
  }

  // État de transition (ne devrait jamais arriver ici en production)
  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <View style={styles.loaderContainer}>
        <ActivityIndicator size="large" color={colors.accent} />
      </View>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  loaderContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
