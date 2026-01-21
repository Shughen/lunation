/**
 * Écran de bienvenue - Hero Splash avec effet "whaou"
 *
 * Features:
 * - Animation de lune qui se remplit (nouvelle → pleine)
 * - Étoiles animées en arrière-plan
 * - Phase lunaire réelle du jour affichée
 * - Texte accrocheur et différenciant
 */

import React, { useEffect, useRef, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Animated,
  Easing,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../stores/useOnboardingStore';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { goToNextOnboardingStep } from '../services/onboardingFlow';
import { getOnboardingFlowState } from '../utils/onboardingHelpers';
import { AnimatedMoon } from '../components/onboarding/AnimatedMoon';

export default function WelcomeScreen() {
  const router = useRouter();
  const onboardingStore = useOnboardingStore();
  const { setWelcomeSeen } = onboardingStore;

  // Animations
  const titleOpacity = useRef(new Animated.Value(0)).current;
  const titleTranslate = useRef(new Animated.Value(30)).current;
  const subtitleOpacity = useRef(new Animated.Value(0)).current;
  const subtitleTranslate = useRef(new Animated.Value(20)).current;
  const buttonOpacity = useRef(new Animated.Value(0)).current;
  const buttonScale = useRef(new Animated.Value(0.9)).current;

  useEffect(() => {
    console.log('[WELCOME] Composant Welcome monte et affiche');

    // Séquence d'animations d'entrée
    const animationSequence = Animated.stagger(300, [
      // Titre principal (après animation lune ~2s)
      Animated.delay(1800),
      Animated.parallel([
        Animated.timing(titleOpacity, {
          toValue: 1,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.timing(titleTranslate, {
          toValue: 0,
          duration: 600,
          easing: Easing.out(Easing.cubic),
          useNativeDriver: true,
        }),
      ]),
      // Sous-titre
      Animated.parallel([
        Animated.timing(subtitleOpacity, {
          toValue: 1,
          duration: 500,
          useNativeDriver: true,
        }),
        Animated.timing(subtitleTranslate, {
          toValue: 0,
          duration: 500,
          easing: Easing.out(Easing.cubic),
          useNativeDriver: true,
        }),
      ]),
      // Bouton CTA
      Animated.parallel([
        Animated.timing(buttonOpacity, {
          toValue: 1,
          duration: 400,
          useNativeDriver: true,
        }),
        Animated.spring(buttonScale, {
          toValue: 1,
          friction: 6,
          tension: 40,
          useNativeDriver: true,
        }),
      ]),
    ]);

    animationSequence.start();
  }, []);

  const handleContinue = async () => {
    console.log('[WELCOME] Bouton CTA clique');

    // Marquer le welcome comme vu via le store
    await setWelcomeSeen();
    console.log('[WELCOME] hasSeenWelcomeScreen defini a true');

    // Naviguer vers la prochaine étape
    await goToNextOnboardingStep(router, 'WELCOME', getOnboardingFlowState);
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        <View style={styles.content}>
          {/* Animation de la lune */}
          <View style={styles.moonSection}>
            <AnimatedMoon size={100} animationDuration={2000} showStars={true} />
          </View>

          {/* Texte principal */}
          <View style={styles.textSection}>
            <Animated.Text
              style={[
                styles.title,
                {
                  opacity: titleOpacity,
                  transform: [{ translateY: titleTranslate }],
                },
              ]}
            >
              Découvre ce que la Lune révèle sur toi
            </Animated.Text>

            <Animated.Text
              style={[
                styles.subtitle,
                {
                  opacity: subtitleOpacity,
                  transform: [{ translateY: subtitleTranslate }],
                },
              ]}
            >
              12 saisons lunaires par an.{'\n'}
              12 opportunités de te connaître.
            </Animated.Text>

            <Animated.View
              style={[
                styles.featureHint,
                { opacity: subtitleOpacity },
              ]}
            >
              <Text style={styles.featureHintText}>
                Cycles lunaires personnalisés | Pauses lunaires | Journal | Transits
              </Text>
            </Animated.View>
          </View>

          {/* Bouton CTA */}
          <Animated.View
            style={[
              styles.buttonContainer,
              {
                opacity: buttonOpacity,
                transform: [{ scale: buttonScale }],
              },
            ]}
          >
            <TouchableOpacity
              style={styles.button}
              onPress={handleContinue}
              activeOpacity={0.85}
            >
              <LinearGradient
                colors={[colors.accent, colors.accentDark || colors.accent]}
                style={styles.buttonGradient}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 0 }}
              >
                <Text style={styles.buttonText}>Commencer mon voyage lunaire</Text>
              </LinearGradient>
            </TouchableOpacity>
          </Animated.View>
        </View>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  content: {
    flex: 1,
    paddingHorizontal: spacing.xl,
    paddingTop: spacing.xxl,
    paddingBottom: spacing.xl,
  },
  moonSection: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    minHeight: 250,
  },
  textSection: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: spacing.md,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.lg,
    lineHeight: 36,
    textShadowColor: 'rgba(183, 148, 246, 0.4)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  subtitle: {
    fontSize: fonts.sizes.lg,
    color: 'rgba(255, 255, 255, 0.85)',
    textAlign: 'center',
    lineHeight: 28,
    marginBottom: spacing.lg,
  },
  featureHint: {
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
  },
  featureHintText: {
    fontSize: fonts.sizes.sm,
    color: colors.accent,
    textAlign: 'center',
  },
  buttonContainer: {
    paddingTop: spacing.xl,
  },
  button: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  buttonGradient: {
    paddingVertical: spacing.md + 4,
    paddingHorizontal: spacing.xl,
    alignItems: 'center',
  },
  buttonText: {
    ...fonts.button,
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});
