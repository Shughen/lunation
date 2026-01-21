/**
 * Onboarding slides - Interactive Feature Discovery
 *
 * Features:
 * - 5 slides interactifs avec previews reelles
 * - Navigation swipe horizontal
 * - Indicateurs cliquables
 * - Donnees reelles de l'utilisateur
 */

import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Dimensions,
  Animated,
  Easing,
  FlatList,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { useNatalStore } from '../../stores/useNatalStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { goToNextOnboardingStep } from '../../services/onboardingFlow';
import { getOnboardingFlowState } from '../../utils/onboardingHelpers';
import { translateZodiacSign } from '../../utils/astrologyTranslations';

const { width: SCREEN_WIDTH } = Dimensions.get('window');

// Slide data structure
interface SlideData {
  id: string;
  icon: string;
  title: string;
  description: string;
  previewType: 'ritual' | 'lunar' | 'voc' | 'journal' | 'transits';
}

const SLIDES: SlideData[] = [
  {
    id: 'ritual',
    icon: '🌙',
    title: 'Rituel Quotidien',
    description: 'Chaque jour, découvre l\'énergie lunaire du moment et prends un temps pour toi.',
    previewType: 'ritual',
  },
  {
    id: 'lunar',
    icon: '🔮',
    title: 'Saisons Lunaires',
    description: '12 cycles de 29 jours par an. Chaque mois, une nouvelle énergie à explorer.',
    previewType: 'lunar',
  },
  {
    id: 'voc',
    icon: '⏸️',
    title: 'Pauses Lunaires',
    description: 'Sache quand la Lune fait une pause (Void of Course) pour mieux planifier.',
    previewType: 'voc',
  },
  {
    id: 'journal',
    icon: '📝',
    title: 'Journal Lunaire',
    description: 'Note tes pensées et émotions. Vois les patterns se dessiner au fil des cycles.',
    previewType: 'journal',
  },
  {
    id: 'transits',
    icon: '✨',
    title: 'Transits Personnels',
    description: 'Vois comment les planètes dialoguent avec ton thème natal, chaque jour.',
    previewType: 'transits',
  },
];

// Preview components
function RitualPreview() {
  const today = new Date();
  const dayName = today.toLocaleDateString('fr-FR', { weekday: 'long' });
  const { chart } = useNatalStore();
  const moonSign = chart?.moon_sign ? translateZodiacSign(chart.moon_sign) : 'ton signe';

  return (
    <View style={styles.previewCard}>
      <Text style={styles.previewLabel}>AUJOURD'HUI</Text>
      <Text style={styles.previewTitle}>
        {dayName.charAt(0).toUpperCase() + dayName.slice(1)}
      </Text>
      <View style={styles.previewRow}>
        <Text style={styles.previewIcon}>🌗</Text>
        <Text style={styles.previewText}>Lune croissante en {moonSign}</Text>
      </View>
      <Text style={styles.previewHint}>
        Énergie favorable pour initier de nouveaux projets
      </Text>
    </View>
  );
}

function LunarPreview() {
  const now = new Date();
  const monthName = now.toLocaleDateString('fr-FR', { month: 'long' });

  return (
    <View style={styles.previewCard}>
      <Text style={styles.previewLabel}>CE MOIS</Text>
      <Text style={styles.previewTitle}>
        {monthName.charAt(0).toUpperCase() + monthName.slice(1)} {now.getFullYear()}
      </Text>
      <View style={styles.previewRow}>
        <Text style={styles.previewIcon}>🌕</Text>
        <Text style={styles.previewText}>Ta révolution lunaire personnalisée</Text>
      </View>
      <Text style={styles.previewHint}>
        Découvre les thèmes majeurs de ce cycle
      </Text>
    </View>
  );
}

function VocPreview() {
  return (
    <View style={styles.previewCard}>
      <Text style={styles.previewLabel}>STATUT ACTUEL</Text>
      <View style={styles.previewStatusRow}>
        <View style={styles.statusDot} />
        <Text style={styles.previewTitle}>Lune active</Text>
      </View>
      <Text style={styles.previewText}>
        Prochaine pause: demain 14h30
      </Text>
      <Text style={styles.previewHint}>
        Notification avant chaque pause lunaire
      </Text>
    </View>
  );
}

function JournalPreview() {
  return (
    <View style={styles.previewCard}>
      <Text style={styles.previewLabel}>TON JOURNAL</Text>
      <View style={styles.journalLines}>
        <View style={styles.journalLine}>
          <Text style={styles.journalLineText}>Aujourd'hui...</Text>
        </View>
        <View style={[styles.journalLine, styles.journalLineFaded]} />
        <View style={[styles.journalLine, styles.journalLineFaded, { width: '60%' }]} />
      </View>
      <Text style={styles.previewHint}>
        Écris tes pensées, reviens-y plus tard
      </Text>
    </View>
  );
}

function TransitsPreview() {
  const { chart } = useNatalStore();
  const sunSign = chart?.sun_sign ? translateZodiacSign(chart.sun_sign) : 'ton signe';

  return (
    <View style={styles.previewCard}>
      <Text style={styles.previewLabel}>TES TRANSITS</Text>
      <View style={styles.transitItem}>
        <Text style={styles.transitIcon}>☀️</Text>
        <Text style={styles.transitText}>
          Soleil conjoint Soleil natal en {sunSign}
        </Text>
      </View>
      <View style={styles.transitItem}>
        <Text style={styles.transitIcon}>🌙</Text>
        <Text style={styles.transitText}>
          Lune trigone Lune natale
        </Text>
      </View>
      <Text style={styles.previewHint}>
        Mis à jour quotidiennement
      </Text>
    </View>
  );
}

function SlideItem({ item, index }: { item: SlideData; index: number }) {
  const renderPreview = () => {
    switch (item.previewType) {
      case 'ritual':
        return <RitualPreview />;
      case 'lunar':
        return <LunarPreview />;
      case 'voc':
        return <VocPreview />;
      case 'journal':
        return <JournalPreview />;
      case 'transits':
        return <TransitsPreview />;
      default:
        return null;
    }
  };

  return (
    <View style={styles.slideContainer}>
      {/* Icon */}
      <View style={styles.iconContainer}>
        <Text style={styles.icon}>{item.icon}</Text>
      </View>

      {/* Title */}
      <Text style={styles.title}>{item.title}</Text>

      {/* Description */}
      <Text style={styles.description}>{item.description}</Text>

      {/* Preview */}
      <View style={styles.previewContainer}>
        {renderPreview()}
      </View>
    </View>
  );
}

export default function OnboardingIndexScreen() {
  const router = useRouter();
  const onboardingStore = useOnboardingStore();
  const { completeOnboarding } = onboardingStore;
  const [currentIndex, setCurrentIndex] = useState(0);
  const flatListRef = useRef<FlatList>(null);
  const fadeAnim = useRef(new Animated.Value(1)).current;

  useEffect(() => {
    console.log('[ONBOARDING] Slides montees, slide:', currentIndex);
  }, [currentIndex]);

  const handleNext = async () => {
    if (currentIndex < SLIDES.length - 1) {
      // Fade out
      Animated.timing(fadeAnim, {
        toValue: 0.5,
        duration: 150,
        useNativeDriver: true,
      }).start(() => {
        const nextIndex = currentIndex + 1;
        setCurrentIndex(nextIndex);
        flatListRef.current?.scrollToIndex({ index: nextIndex, animated: true });

        // Fade in
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 200,
          useNativeDriver: true,
        }).start();
      });
    } else {
      // Last slide → complete onboarding
      console.log('[ONBOARDING] Dernier slide → completeOnboarding()');

      try {
        await completeOnboarding();
        console.log('[ONBOARDING] completeOnboarding reussi, navigation vers /');
        router.replace('/');
      } catch (error: any) {
        console.error('[ONBOARDING] completeOnboarding echoue:', error.message);
        // Redirect to missing step
        await goToNextOnboardingStep(router, 'ONBOARDING_SLIDES_ERROR', getOnboardingFlowState);
      }
    }
  };

  const handleSkip = async () => {
    console.log('[ONBOARDING] Skip → completeOnboarding()');

    try {
      await completeOnboarding();
      console.log('[ONBOARDING] completeOnboarding reussi, navigation vers /');
      router.replace('/');
    } catch (error: any) {
      console.error('[ONBOARDING] completeOnboarding echoue:', error.message);
      // Redirect to missing step
      await goToNextOnboardingStep(router, 'ONBOARDING_SLIDES_SKIP_ERROR', getOnboardingFlowState);
    }
  };

  const handleIndicatorPress = (index: number) => {
    setCurrentIndex(index);
    flatListRef.current?.scrollToIndex({ index, animated: true });
  };

  const handleScroll = (event: any) => {
    const offsetX = event.nativeEvent.contentOffset.x;
    const index = Math.round(offsetX / SCREEN_WIDTH);
    if (index !== currentIndex && index >= 0 && index < SLIDES.length) {
      setCurrentIndex(index);
    }
  };

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header with Skip */}
        <View style={styles.header}>
          <View style={{ width: 60 }} />
          <Text style={styles.headerTitle}>Découvre Lunation</Text>
          <TouchableOpacity onPress={handleSkip} style={styles.skipButton}>
            <Text style={styles.skipText}>Passer</Text>
          </TouchableOpacity>
        </View>

        {/* Slides */}
        <Animated.View style={[styles.slidesContainer, { opacity: fadeAnim }]}>
          <FlatList
            ref={flatListRef}
            data={SLIDES}
            horizontal
            pagingEnabled
            showsHorizontalScrollIndicator={false}
            onScroll={handleScroll}
            scrollEventThrottle={16}
            renderItem={({ item, index }) => (
              <SlideItem item={item} index={index} />
            )}
            keyExtractor={(item) => item.id}
            getItemLayout={(data, index) => ({
              length: SCREEN_WIDTH,
              offset: SCREEN_WIDTH * index,
              index,
            })}
          />
        </Animated.View>

        {/* Footer with indicators and button */}
        <View style={styles.footer}>
          {/* Indicators */}
          <View style={styles.indicators}>
            {SLIDES.map((_, index) => (
              <TouchableOpacity
                key={index}
                onPress={() => handleIndicatorPress(index)}
                style={[
                  styles.indicator,
                  index === currentIndex && styles.indicatorActive,
                ]}
              />
            ))}
          </View>

          {/* Next Button */}
          <TouchableOpacity
            style={styles.nextButton}
            onPress={handleNext}
            activeOpacity={0.8}
          >
            <LinearGradient
              colors={[colors.accent, colors.accentDark || colors.accent]}
              style={styles.nextButtonGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Text style={styles.nextButtonText}>
                {currentIndex < SLIDES.length - 1 ? 'Suivant' : 'Entrer dans mon univers'}
              </Text>
            </LinearGradient>
          </TouchableOpacity>
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
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  headerTitle: {
    color: colors.textMuted,
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  skipButton: {
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
  },
  skipText: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  slidesContainer: {
    flex: 1,
  },
  slideContainer: {
    width: SCREEN_WIDTH,
    paddingHorizontal: spacing.xl,
    alignItems: 'center',
    justifyContent: 'center',
  },
  iconContainer: {
    width: 100,
    height: 100,
    borderRadius: 50,
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: spacing.lg,
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.3,
    shadowRadius: 16,
    elevation: 8,
  },
  icon: {
    fontSize: 48,
  },
  title: {
    fontSize: 26,
    fontWeight: 'bold',
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
    textShadowColor: 'rgba(183, 148, 246, 0.4)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  description: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.8)',
    textAlign: 'center',
    lineHeight: 24,
    marginBottom: spacing.xl,
    paddingHorizontal: spacing.sm,
  },
  previewContainer: {
    width: '100%',
  },
  previewCard: {
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
  },
  previewLabel: {
    fontSize: 11,
    color: colors.accent,
    fontWeight: '600',
    letterSpacing: 1,
    marginBottom: spacing.xs,
  },
  previewTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.sm,
  },
  previewRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    marginBottom: spacing.sm,
  },
  previewIcon: {
    fontSize: 20,
  },
  previewText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.8)',
    flex: 1,
  },
  previewHint: {
    fontSize: fonts.sizes.sm,
    color: colors.accent,
    fontStyle: 'italic',
    marginTop: spacing.xs,
  },
  previewStatusRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    marginBottom: spacing.sm,
  },
  statusDot: {
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: colors.success,
  },
  journalLines: {
    gap: spacing.sm,
    marginBottom: spacing.sm,
  },
  journalLine: {
    height: 20,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 4,
    justifyContent: 'center',
    paddingLeft: spacing.sm,
  },
  journalLineFaded: {
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    width: '80%',
  },
  journalLineText: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    fontStyle: 'italic',
  },
  transitItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    marginBottom: spacing.sm,
  },
  transitIcon: {
    fontSize: 18,
  },
  transitText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.8)',
    flex: 1,
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
    gap: spacing.lg,
  },
  indicators: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: spacing.sm,
  },
  indicator: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.3)',
  },
  indicatorActive: {
    backgroundColor: colors.accent,
    width: 24,
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.6,
    shadowRadius: 4,
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
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    gap: spacing.sm,
  },
  nextButtonText: {
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});
