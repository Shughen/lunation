/**
 * Horoscope Tab Screen
 * Daily lunar horoscope with guidance, metrics, and lucky elements
 */

import React, { useMemo } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Share,
  Platform,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { useLunar } from '../../contexts/LunarProvider';
import { useCurrentLunarReturn } from '../../hooks/useLunarData';
import { ZodiacBadge } from '../../components/icons/ZodiacIcon';
import { ProgressBar } from '../../components/ProgressBar';
import { KeywordChip } from '../../components/KeywordChip';
import { DomainCard } from '../../components/DomainCard';
import { LuckyElements } from '../../components/LuckyElements';
import { Skeleton } from '../../components/Skeleton';
import { haptics } from '../../services/haptics';
import {
  getHoroscopeMetrics,
  getZodiacSignFrench,
  getMoonPhaseFrench,
  getPhaseGuidance,
  getLoveInsight,
  getCareerInsight,
} from '../../utils/horoscopeCalculations';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors: bgColors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: bgColors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

// Keywords based on moon phase
const PHASE_KEYWORDS: Record<string, string[]> = {
  new_moon: ['Intention', 'Nouveaute', 'Potentiel'],
  waxing_crescent: ['Action', 'Courage', 'Mouvement'],
  first_quarter: ['Decision', 'Perseverance', 'Force'],
  waxing_gibbous: ['Perfectionnement', 'Patience', 'Detail'],
  full_moon: ['Accomplissement', 'Celebration', 'Liberation'],
  waning_gibbous: ['Gratitude', 'Partage', 'Sagesse'],
  last_quarter: ['Lacher-prise', 'Transformation', 'Bilan'],
  waning_crescent: ['Repos', 'Introspection', 'Preparation'],
};

function normalizePhase(phase: string | undefined): string {
  if (!phase) return 'new_moon';
  return phase.toLowerCase().replace(/\s+/g, '_');
}

export default function HoroscopeScreen() {
  // Get lunar data from context
  const { current: lunarData, status } = useLunar();
  const { data: lunarReturn } = useCurrentLunarReturn();

  // Derive values
  const moonSign = lunarReturn?.moon_sign || lunarData?.moon?.sign || 'Aries';
  const moonPhase = lunarData?.moon?.phase || 'waxing_crescent';
  const normalizedPhase = normalizePhase(moonPhase);
  const aspects = lunarReturn?.aspects || [];

  // Calculate metrics
  const metrics = useMemo(
    () => getHoroscopeMetrics(moonSign, moonPhase, aspects),
    [moonSign, moonPhase, aspects]
  );

  // Get French translations and content
  const signFrench = getZodiacSignFrench(moonSign);
  const phaseFrench = getMoonPhaseFrench(moonPhase);
  const guidance = getPhaseGuidance(moonPhase);
  const loveInsight = getLoveInsight(moonSign);
  const careerInsight = getCareerInsight(moonSign);
  const keywords = PHASE_KEYWORDS[normalizedPhase] || ['Energie', 'Intuition', 'Equilibre'];

  // Format today's date
  const today = new Date();
  const formattedDate = today.toLocaleDateString('fr-FR', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  });

  // Share handler
  const handleShare = async () => {
    haptics.light();
    try {
      const message = `Mon horoscope lunaire du ${formattedDate}\n\nLune en ${signFrench} - ${phaseFrench}\n\n${guidance}\n\nMots-cles: ${keywords.join(', ')}\n\nEnergie creative: ${metrics.creativeEnergy}%\nIntuition: ${metrics.intuition}%\n\nDecouvrez votre horoscope lunaire sur Lunation!`;

      await Share.share({
        message,
        title: 'Mon Horoscope Lunaire',
      });
    } catch (error) {
      console.log('Share error:', error);
    }
  };

  // Loading state
  if (status.isLoading && !lunarData) {
    return (
      <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
        <ScrollView contentContainerStyle={styles.scrollContent}>
          <View style={styles.header}>
            <Text style={styles.title}>Horoscope Lunaire</Text>
          </View>
          <View style={styles.loadingContainer}>
            <Skeleton width={80} height={80} borderRadius={40} />
            <Skeleton width={200} height={20} style={{ marginTop: spacing.md }} />
            <Skeleton width="100%" height={150} style={{ marginTop: spacing.lg }} />
            <Skeleton width="100%" height={100} style={{ marginTop: spacing.md }} />
          </View>
        </ScrollView>
      </LinearGradientComponent>
    );
  }

  return (
    <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Horoscope Lunaire</Text>
        </View>

        {/* Zodiac Badge & Date */}
        <View style={styles.zodiacSection}>
          <ZodiacBadge sign={moonSign} size={72} />
          <Text style={styles.signName}>{signFrench}</Text>
          <Text style={styles.datePhase}>
            {formattedDate} - {phaseFrench}
          </Text>
        </View>

        {/* Guidance Card */}
        <View style={styles.guidanceCard}>
          <Text style={styles.guidanceTitle}>Guidance du Jour</Text>
          <Text style={styles.guidanceText}>{guidance}</Text>

          {/* Keywords */}
          <View style={styles.keywordsContainer}>
            <Text style={styles.keywordsLabel}>Mots-cles:</Text>
            <View style={styles.keywordsRow}>
              {keywords.map((keyword, index) => (
                <KeywordChip
                  key={index}
                  label={keyword}
                  variant={index === 0 ? 'accent' : 'default'}
                />
              ))}
            </View>
          </View>
        </View>

        {/* Metrics */}
        <View style={styles.metricsContainer}>
          <View style={styles.metricRow}>
            <View style={styles.metricItem}>
              <ProgressBar
                label="Energie Creative"
                value={metrics.creativeEnergy}
                color={colors.gold}
              />
            </View>
            <View style={styles.metricItem}>
              <ProgressBar
                label="Intuition"
                value={metrics.intuition}
                color={colors.accent}
              />
            </View>
          </View>
        </View>

        {/* Domain Cards */}
        <View style={styles.domainCardsRow}>
          <View style={styles.domainCardWrapper}>
            <DomainCard
              domain="love"
              title="Amour"
              description={loveInsight}
              subtitle="Compatibilite +"
            />
          </View>
          <View style={styles.domainCardWrapper}>
            <DomainCard
              domain="career"
              title="Carriere"
              description={careerInsight}
            />
          </View>
        </View>

        {/* Lucky Elements */}
        <LuckyElements {...metrics.luckyElements} />

        {/* Share Button */}
        <TouchableOpacity style={styles.shareButton} onPress={handleShare}>
          <Text style={styles.shareButtonText}>Partager mon horoscope</Text>
        </TouchableOpacity>
      </ScrollView>
    </LinearGradientComponent>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: 100,
  },
  header: {
    alignItems: 'center',
    marginBottom: spacing.xl,
  },
  title: {
    ...fonts.h2,
    color: colors.text,
    letterSpacing: 2,
  },
  loadingContainer: {
    alignItems: 'center',
    paddingTop: spacing.xl,
  },
  zodiacSection: {
    alignItems: 'center',
    marginBottom: spacing.xl,
  },
  signName: {
    ...fonts.h2,
    color: colors.text,
    marginTop: spacing.md,
  },
  datePhase: {
    ...fonts.body,
    color: colors.textMuted,
    marginTop: spacing.xs,
  },
  guidanceCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: colors.accent,
  },
  guidanceTitle: {
    ...fonts.body,
    color: colors.gold,
    fontWeight: '600',
    marginBottom: spacing.md,
  },
  guidanceText: {
    ...fonts.body,
    color: colors.text,
    lineHeight: 24,
    marginBottom: spacing.md,
  },
  keywordsContainer: {
    marginTop: spacing.sm,
  },
  keywordsLabel: {
    ...fonts.caption,
    color: colors.textMuted,
    marginBottom: spacing.xs,
  },
  keywordsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  metricsContainer: {
    marginBottom: spacing.lg,
  },
  metricRow: {
    flexDirection: 'row',
    gap: spacing.md,
  },
  metricItem: {
    flex: 1,
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  domainCardsRow: {
    flexDirection: 'row',
    gap: spacing.md,
    marginBottom: spacing.lg,
  },
  domainCardWrapper: {
    flex: 1,
  },
  shareButton: {
    backgroundColor: 'transparent',
    borderWidth: 1,
    borderColor: colors.textMuted,
    borderRadius: borderRadius.full,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.xl,
    alignItems: 'center',
    marginTop: spacing.md,
    marginBottom: spacing.xl,
  },
  shareButtonText: {
    ...fonts.body,
    color: colors.text,
  },
});
