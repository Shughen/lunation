/**
 * Onboarding - Chart Preview
 * Écran clé: L'utilisateur voit son thème natal pour la première fois
 *
 * Features:
 * - Big 3 affichés en grand avec animations de reveal
 * - Titre personnalisé avec le prénom
 * - Teaser des cycles lunaires
 * - CTA vers la suite
 */

import React, { useEffect, useRef, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Animated,
  Easing,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { useNatalStore } from '../../stores/useNatalStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { goToNextOnboardingStep, goToPreviousOnboardingStep } from '../../services/onboardingFlow';
import { getOnboardingFlowState } from '../../utils/onboardingHelpers';
import { Big3Preview } from '../../components/onboarding/Big3Preview';

export default function ChartPreviewScreen() {
  const router = useRouter();
  const { profileData, setChartPreviewSeen } = useOnboardingStore();
  const { chart } = useNatalStore();

  // Animations
  const headerOpacity = useRef(new Animated.Value(0)).current;
  const headerTranslate = useRef(new Animated.Value(-20)).current;
  const teaserOpacity = useRef(new Animated.Value(0)).current;
  const buttonOpacity = useRef(new Animated.Value(0)).current;
  const buttonScale = useRef(new Animated.Value(0.9)).current;

  // Get user name
  const userName = profileData?.name || 'toi';

  // Get Big 3 from natal chart
  const sunSign = chart?.sun_sign || null;
  const moonSign = chart?.moon_sign || null;
  const ascendant = chart?.ascendant || null;

  useEffect(() => {
    // Animation sequence
    const animationSequence = Animated.sequence([
      // Header animation
      Animated.parallel([
        Animated.timing(headerOpacity, {
          toValue: 1,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.timing(headerTranslate, {
          toValue: 0,
          duration: 600,
          easing: Easing.out(Easing.cubic),
          useNativeDriver: true,
        }),
      ]),
      // Wait for Big3 animations (300ms * 3 items + 500ms animation)
      Animated.delay(1400),
      // Teaser animation
      Animated.timing(teaserOpacity, {
        toValue: 1,
        duration: 500,
        useNativeDriver: true,
      }),
      // Button animation
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
    // Mark chart preview as seen
    if (setChartPreviewSeen) {
      await setChartPreviewSeen();
    }

    // Navigate to next step
    await goToNextOnboardingStep(router, 'CHART-PREVIEW', getOnboardingFlowState);
  };

  // Calculate teaser content based on current month
  const getCurrentMonthTeaser = () => {
    const now = new Date();
    const monthNames = [
      'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
      'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
    ];
    const currentMonth = monthNames[now.getMonth()];
    return `Ce mois de ${currentMonth}, découvre ta saison lunaire personnalisée`;
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header with progress */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => goToPreviousOnboardingStep(router, 'CHART-PREVIEW')} style={styles.backButton}>
            <Text style={styles.backText}>←</Text>
          </TouchableOpacity>
          <View style={styles.progressContainer}>
            <View style={styles.progressBar}>
              <View style={[styles.progressFill, { width: '75%' }]} />
            </View>
            <Text style={styles.headerTitle}>Étape 3/4</Text>
          </View>
          <View style={{ width: 40 }} />
        </View>

        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          {/* Animated header */}
          <Animated.View
            style={{
              opacity: headerOpacity,
              transform: [{ translateY: headerTranslate }],
            }}
          >
            <View style={styles.iconContainer}>
              <Text style={styles.icon}>✨</Text>
            </View>

            <Text style={styles.title}>
              Voici ton ciel de naissance, {userName}
            </Text>
            <Text style={styles.subtitle}>
              Les énergies qui t'accompagnent depuis ta première respiration
            </Text>
          </Animated.View>

          {/* Big 3 Preview with animations */}
          <View style={styles.big3Container}>
            <Big3Preview
              sunSign={sunSign}
              moonSign={moonSign}
              ascendant={ascendant}
              animated={true}
              compact={false}
            />
          </View>

          {/* Teaser */}
          <Animated.View
            style={[
              styles.teaserContainer,
              { opacity: teaserOpacity },
            ]}
          >
            <View style={styles.teaserCard}>
              <Text style={styles.teaserIcon}>🌙</Text>
              <Text style={styles.teaserText}>{getCurrentMonthTeaser()}</Text>
            </View>
          </Animated.View>
        </ScrollView>

        {/* Footer */}
        <Animated.View
          style={[
            styles.footer,
            {
              opacity: buttonOpacity,
              transform: [{ scale: buttonScale }],
            },
          ]}
        >
          <TouchableOpacity
            style={styles.nextButton}
            onPress={handleContinue}
            activeOpacity={0.85}
          >
            <LinearGradient
              colors={[colors.accent, colors.accentDark || colors.accent]}
              style={styles.nextButtonGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Text style={styles.nextButtonText}>Découvrir mes cycles lunaires</Text>
            </LinearGradient>
          </TouchableOpacity>
        </Animated.View>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  safeArea: { flex: 1 },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  backButton: { width: 40, height: 40, justifyContent: 'center' },
  backText: { fontSize: 24, color: colors.text },
  progressContainer: {
    alignItems: 'center',
    gap: spacing.xs,
  },
  progressBar: {
    width: 120,
    height: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    borderRadius: 2,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: colors.accent,
    borderRadius: 2,
  },
  headerTitle: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: fonts.sizes.sm,
    fontWeight: '600',
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.xl,
  },
  iconContainer: {
    alignItems: 'center',
    marginTop: spacing.md,
    marginBottom: spacing.md,
  },
  icon: {
    fontSize: 48,
  },
  title: {
    fontSize: 26,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.sm,
    textAlign: 'center',
    lineHeight: 34,
    textShadowColor: 'rgba(183, 148, 246, 0.4)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  subtitle: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.7)',
    marginBottom: spacing.xl,
    textAlign: 'center',
    lineHeight: 22,
  },
  big3Container: {
    marginBottom: spacing.xl,
  },
  teaserContainer: {
    marginTop: spacing.md,
  },
  teaserCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
    gap: spacing.sm,
  },
  teaserIcon: {
    fontSize: 24,
  },
  teaserText: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: colors.text,
    lineHeight: 22,
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
  },
  nextButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  nextButtonGradient: {
    paddingVertical: spacing.md + 4,
    paddingHorizontal: spacing.xl,
    alignItems: 'center',
  },
  nextButtonText: {
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});
