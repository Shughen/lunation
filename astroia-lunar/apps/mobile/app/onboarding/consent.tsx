/**
 * Onboarding - Consentement RGPD humanise
 *
 * Features:
 * - Ton chaleureux et rassurant
 * - Mini-FAQ deployable
 * - Animation checkbox (spring)
 * - Progress bar "Etape 1/4"
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
  LayoutAnimation,
  Platform,
  UIManager,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { goToNextOnboardingStep, goToPreviousOnboardingStep } from '../../services/onboardingFlow';
import { getOnboardingFlowState } from '../../utils/onboardingHelpers';

// Enable LayoutAnimation on Android
if (Platform.OS === 'android' && UIManager.setLayoutAnimationEnabledExperimental) {
  UIManager.setLayoutAnimationEnabledExperimental(true);
}

// FAQ items
const FAQ_ITEMS = [
  {
    id: 'birthdate',
    question: 'Pourquoi ma date de naissance ?',
    answer: 'Ta date, heure et lieu de naissance permettent de calculer précisément les positions planétaires au moment de ta naissance. C\'est la base de ton thème natal unique.',
  },
  {
    id: 'privacy',
    question: 'Mes données sont-elles en sécurité ?',
    answer: 'Tes données sont stockées de manière sécurisée et ne sont jamais vendues à des tiers. Tu peux les supprimer à tout moment depuis les paramètres de l\'app.',
  },
  {
    id: 'usage',
    question: 'Comment mes données sont-elles utilisées ?',
    answer: 'Uniquement pour calculer ton thème natal, tes révolutions lunaires et personnaliser ton expérience. Aucune utilisation commerciale.',
  },
];

interface FAQItemProps {
  item: typeof FAQ_ITEMS[0];
  isExpanded: boolean;
  onToggle: () => void;
}

function FAQItem({ item, isExpanded, onToggle }: FAQItemProps) {
  return (
    <TouchableOpacity
      style={styles.faqItem}
      onPress={onToggle}
      activeOpacity={0.7}
    >
      <View style={styles.faqHeader}>
        <Text style={styles.faqQuestion}>{item.question}</Text>
        <Text style={styles.faqChevron}>{isExpanded ? '−' : '+'}</Text>
      </View>
      {isExpanded && (
        <Text style={styles.faqAnswer}>{item.answer}</Text>
      )}
    </TouchableOpacity>
  );
}

export default function ConsentScreen() {
  const router = useRouter();
  const onboardingStore = useOnboardingStore();
  const { setConsentAccepted } = onboardingStore;
  const [accepted, setAccepted] = useState(false);
  const [expandedFaq, setExpandedFaq] = useState<string | null>(null);

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

  const handleToggleAccept = () => {
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

    setAccepted(!accepted);
  };

  const handleToggleFaq = (id: string) => {
    LayoutAnimation.configureNext(LayoutAnimation.Presets.easeInEaseOut);
    setExpandedFaq(expandedFaq === id ? null : id);
  };

  const handleNext = async () => {
    if (!accepted) {
      Alert.alert(
        'Consentement requis',
        'Pour continuer, accepte notre politique de confidentialité. Tes données sont en sécurité avec nous.'
      );
      return;
    }

    await setConsentAccepted();
    await goToNextOnboardingStep(router, 'CONSENT', getOnboardingFlowState);
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header avec progress */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => goToPreviousOnboardingStep(router, 'CONSENT')} style={styles.backButton}>
            <Text style={styles.backText}>←</Text>
          </TouchableOpacity>
          <View style={styles.progressContainer}>
            <View style={styles.progressBar}>
              <View style={[styles.progressFill, { width: '25%' }]} />
            </View>
            <Text style={styles.headerTitle}>Étape 1/4</Text>
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
              <Text style={styles.icon}>🔒</Text>
            </View>

            {/* Title */}
            <Text style={styles.title}>Tes données, ton contrôle</Text>
            <Text style={styles.subtitle}>
              On croit en la transparence. Voici ce que tu dois savoir.
            </Text>

            {/* Content cards */}
            <View style={styles.content}>
              <View style={styles.card}>
                <Text style={styles.cardIcon}>🌙</Text>
                <View style={styles.cardContent}>
                  <Text style={styles.cardTitle}>Calculs astronomiques</Text>
                  <Text style={styles.cardText}>
                    Tes données de naissance servent uniquement à calculer ton thème natal et tes cycles lunaires personnalisés.
                  </Text>
                </View>
              </View>

              <View style={styles.card}>
                <Text style={styles.cardIcon}>🛡️</Text>
                <View style={styles.cardContent}>
                  <Text style={styles.cardTitle}>Jamais vendues</Text>
                  <Text style={styles.cardText}>
                    Tes données ne sont jamais vendues ni partagées avec des tiers. Point final.
                  </Text>
                </View>
              </View>

              <View style={styles.card}>
                <Text style={styles.cardIcon}>🗑️</Text>
                <View style={styles.cardContent}>
                  <Text style={styles.cardTitle}>Suppression facile</Text>
                  <Text style={styles.cardText}>
                    Tu peux supprimer toutes tes données à tout moment depuis les paramètres.
                  </Text>
                </View>
              </View>
            </View>

            {/* FAQ Section */}
            <View style={styles.faqSection}>
              <Text style={styles.faqTitle}>Questions fréquentes</Text>
              {FAQ_ITEMS.map((item) => (
                <FAQItem
                  key={item.id}
                  item={item}
                  isExpanded={expandedFaq === item.id}
                  onToggle={() => handleToggleFaq(item.id)}
                />
              ))}
            </View>

            {/* Checkbox */}
            <TouchableOpacity
              style={styles.checkbox}
              onPress={handleToggleAccept}
              activeOpacity={0.7}
            >
              <Animated.View
                style={[
                  styles.checkboxBox,
                  accepted && styles.checkboxBoxChecked,
                  { transform: [{ scale: checkboxScale }] },
                ]}
              >
                {accepted && <Text style={styles.checkboxCheck}>✓</Text>}
              </Animated.View>
              <Text style={styles.checkboxLabel}>
                J'accepte la politique de confidentialite
              </Text>
            </TouchableOpacity>
          </Animated.View>
        </ScrollView>

        {/* Footer */}
        <View style={styles.footer}>
          <TouchableOpacity
            style={[styles.nextButton, !accepted && styles.nextButtonDisabled]}
            onPress={handleNext}
            activeOpacity={0.8}
            disabled={!accepted}
          >
            <LinearGradient
              colors={
                accepted
                  ? [colors.accent, colors.accentDark || colors.accent]
                  : ['rgba(100,100,100,0.5)', 'rgba(100,100,100,0.5)']
              }
              style={styles.nextButtonGradient}
            >
              <Text style={styles.nextButtonText}>Continuer</Text>
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
  },
  iconContainer: {
    alignItems: 'center',
    marginTop: spacing.lg,
    marginBottom: spacing.md,
  },
  icon: {
    fontSize: 48,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.sm,
    textAlign: 'center',
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
  content: {
    gap: spacing.md,
    marginBottom: spacing.xl,
  },
  card: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.15)',
    gap: spacing.md,
  },
  cardIcon: {
    fontSize: 24,
  },
  cardContent: {
    flex: 1,
  },
  cardTitle: {
    fontSize: fonts.sizes.md,
    fontWeight: '600',
    color: colors.text,
    marginBottom: spacing.xs,
  },
  cardText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.75)',
    lineHeight: 20,
  },
  faqSection: {
    marginBottom: spacing.xl,
  },
  faqTitle: {
    fontSize: fonts.sizes.md,
    fontWeight: '600',
    color: colors.accent,
    marginBottom: spacing.md,
  },
  faqItem: {
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    marginBottom: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
  },
  faqHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  faqQuestion: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    fontWeight: '500',
    color: colors.text,
  },
  faqChevron: {
    fontSize: 18,
    color: colors.accent,
    fontWeight: 'bold',
    marginLeft: spacing.sm,
  },
  faqAnswer: {
    marginTop: spacing.sm,
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
    lineHeight: 20,
  },
  checkbox: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
    paddingVertical: spacing.sm,
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
    flex: 1,
    fontSize: fonts.sizes.md,
    color: colors.text,
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
