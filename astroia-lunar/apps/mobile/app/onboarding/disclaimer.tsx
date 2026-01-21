/**
 * Onboarding - Disclaimer allege
 *
 * Features:
 * - Titre engageant: "L'astrologie comme boussole, pas comme GPS"
 * - Texte court et conversationnel
 * - Checkbox plus legere: "Je comprends"
 * - Placement apres chart-preview (contexte etabli)
 */

import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Alert,
  Animated,
  Easing,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { goToNextOnboardingStep, goToPreviousOnboardingStep } from '../../services/onboardingFlow';
import { getOnboardingFlowState } from '../../utils/onboardingHelpers';

export default function DisclaimerScreen() {
  const router = useRouter();
  const onboardingStore = useOnboardingStore();
  const { setDisclaimerSeen } = onboardingStore;
  const [understood, setUnderstood] = useState(false);

  // Animations
  const checkboxScale = useRef(new Animated.Value(1)).current;
  const contentOpacity = useRef(new Animated.Value(0)).current;
  const contentTranslate = useRef(new Animated.Value(20)).current;

  useEffect(() => {
    // Animation d'entree
    Animated.parallel([
      Animated.timing(contentOpacity, {
        toValue: 1,
        duration: 500,
        useNativeDriver: true,
      }),
      Animated.timing(contentTranslate, {
        toValue: 0,
        duration: 500,
        easing: Easing.out(Easing.cubic),
        useNativeDriver: true,
      }),
    ]).start();
  }, []);

  const handleToggleUnderstood = () => {
    // Animation spring sur la checkbox
    Animated.sequence([
      Animated.timing(checkboxScale, {
        toValue: 0.85,
        duration: 100,
        useNativeDriver: true,
      }),
      Animated.spring(checkboxScale, {
        toValue: 1,
        friction: 4,
        tension: 100,
        useNativeDriver: true,
      }),
    ]).start();

    setUnderstood(!understood);
  };

  const handleNext = async () => {
    if (!understood) {
      Alert.alert(
        'Confirmation requise',
        'Confirme que tu as lu cette note pour continuer.'
      );
      return;
    }

    await setDisclaimerSeen();
    await goToNextOnboardingStep(router, 'DISCLAIMER', getOnboardingFlowState);
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header avec progress */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => goToPreviousOnboardingStep(router, 'DISCLAIMER')} style={styles.backButton}>
            <Text style={styles.backText}>←</Text>
          </TouchableOpacity>
          <View style={styles.progressContainer}>
            <View style={styles.progressBar}>
              <View style={[styles.progressFill, { width: '100%' }]} />
            </View>
            <Text style={styles.headerTitle}>Étape 4/4</Text>
          </View>
          <View style={{ width: 40 }} />
        </View>

        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          <Animated.View
            style={{
              opacity: contentOpacity,
              transform: [{ translateY: contentTranslate }],
            }}
          >
            {/* Icon */}
            <View style={styles.iconContainer}>
              <Text style={styles.icon}>🧭</Text>
            </View>

            {/* Title */}
            <Text style={styles.title}>
              L'astrologie comme boussole,{'\n'}pas comme GPS
            </Text>
            <Text style={styles.subtitle}>
              Une petite note avant de commencer ton voyage
            </Text>

            {/* Content */}
            <View style={styles.content}>
              <View style={styles.messageCard}>
                <Text style={styles.message}>
                  Lunation est un outil de découverte de soi et de bien-être basé sur l'astrologie.
                </Text>
                <Text style={styles.message}>
                  Les cycles lunaires et les interprétations astrologiques t'offrent des pistes de réflexion, pas des réponses définitives.
                </Text>
                <Text style={styles.messageHighlight}>
                  Tu restes toujours maître de tes décisions.
                </Text>
              </View>

              <View style={styles.noteCard}>
                <Text style={styles.noteIcon}>💚</Text>
                <Text style={styles.noteText}>
                  Si tu traverses des moments difficiles, n'hésite pas à consulter un professionnel de santé. L'astrologie est un complément, jamais un substitut.
                </Text>
              </View>
            </View>

            {/* Checkbox */}
            <TouchableOpacity
              style={styles.checkbox}
              onPress={handleToggleUnderstood}
              activeOpacity={0.7}
            >
              <Animated.View
                style={[
                  styles.checkboxBox,
                  understood && styles.checkboxBoxChecked,
                  { transform: [{ scale: checkboxScale }] },
                ]}
              >
                {understood && <Text style={styles.checkboxCheck}>✓</Text>}
              </Animated.View>
              <Text style={styles.checkboxLabel}>
                Je comprends
              </Text>
            </TouchableOpacity>
          </Animated.View>
        </ScrollView>

        {/* Footer */}
        <View style={styles.footer}>
          <TouchableOpacity
            style={[styles.nextButton, !understood && styles.nextButtonDisabled]}
            onPress={handleNext}
            activeOpacity={0.8}
            disabled={!understood}
          >
            <LinearGradient
              colors={
                understood
                  ? [colors.accent, colors.accentDark || colors.accent]
                  : ['rgba(100,100,100,0.5)', 'rgba(100,100,100,0.5)']
              }
              style={styles.nextButtonGradient}
            >
              <Text style={styles.nextButtonText}>Découvrir mes cycles</Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>
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
    justifyContent: 'center',
  },
  iconContainer: {
    alignItems: 'center',
    marginBottom: spacing.lg,
  },
  icon: {
    fontSize: 56,
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
    color: 'rgba(255, 255, 255, 0.6)',
    marginBottom: spacing.xl,
    textAlign: 'center',
  },
  content: {
    gap: spacing.lg,
    marginBottom: spacing.xl,
  },
  messageCard: {
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.15)',
    gap: spacing.md,
  },
  message: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.85)',
    lineHeight: 24,
    textAlign: 'center',
  },
  messageHighlight: {
    fontSize: fonts.sizes.md,
    color: colors.accent,
    fontWeight: '600',
    lineHeight: 24,
    textAlign: 'center',
    marginTop: spacing.xs,
  },
  noteCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    backgroundColor: 'rgba(74, 222, 128, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(74, 222, 128, 0.2)',
    gap: spacing.sm,
  },
  noteIcon: {
    fontSize: 20,
  },
  noteText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.75)',
    lineHeight: 20,
  },
  checkbox: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: spacing.md,
    paddingVertical: spacing.md,
  },
  checkboxBox: {
    width: 26,
    height: 26,
    borderRadius: 6,
    borderWidth: 2,
    borderColor: colors.accent,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'transparent',
  },
  checkboxBoxChecked: {
    backgroundColor: colors.accent,
  },
  checkboxCheck: {
    color: colors.text,
    fontSize: 16,
    fontWeight: 'bold',
  },
  checkboxLabel: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    fontWeight: '500',
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
  },
  nextButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 4,
  },
  nextButtonDisabled: {
    opacity: 0.6,
    shadowOpacity: 0,
  },
  nextButtonGradient: {
    paddingVertical: spacing.md + 4,
    alignItems: 'center',
  },
  nextButtonText: {
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});
