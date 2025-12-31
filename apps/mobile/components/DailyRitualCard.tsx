/**
 * DailyRitualCard Component
 * Carte "Rituel Quotidien" pour le dashboard Home
 *
 * Features:
 * - Affiche phase lunaire + signe + guidance quotidienne
 * - Badge VoC si actif
 * - Animation fade-in au premier affichage du jour
 * - Cache 24h avec fallback robuste
 * - i18n FR/EN
 */

import React, { useEffect, useState, useRef } from 'react';
import {
  View,
  Text,
  Pressable,
  StyleSheet,
  Animated,
  Easing,
  ActivityIndicator,
} from 'react-native';
import { useTranslation } from 'react-i18next';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { useLunar } from '../contexts/LunarProvider';
import { isFirstViewToday, markAsViewedToday } from '../services/ritualService';
import { getTodayDateString } from '../utils/ritualHelpers';
import { Skeleton } from './Skeleton';
import { JournalEntryModal } from './JournalEntryModal';
import { hasJournalEntry } from '../services/journalService';

export function DailyRitualCard() {
  const { t, i18n } = useTranslation();
  const router = useRouter();

  // Lunar context (remplace fetchRitualData)
  const { current: data, status, helpers } = useLunar();

  // State
  const [isFirstView, setIsFirstView] = useState(false);
  const [journalModalVisible, setJournalModalVisible] = useState(false);
  const [hasJournalToday, setHasJournalToday] = useState(false);

  // Animations
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const translateAnim = useRef(new Animated.Value(20)).current;

  // Check first view and journal on mount
  useEffect(() => {
    checkFirstView();
    checkJournalEntry();
  }, []);

  // Refresh journal status when modal closes
  useEffect(() => {
    if (!journalModalVisible) {
      checkJournalEntry();
    }
  }, [journalModalVisible]);

  // Animate if first view
  useEffect(() => {
    if (isFirstView && data && !status.isLoading) {
      Animated.parallel([
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.timing(translateAnim, {
          toValue: 0,
          duration: 600,
          easing: Easing.out(Easing.cubic),
          useNativeDriver: true,
        }),
      ]).start();
    } else if (data && !status.isLoading) {
      // Pas d'animation, affichage direct
      fadeAnim.setValue(1);
      translateAnim.setValue(0);
    }
  }, [isFirstView, data, status.isLoading]);

  const checkFirstView = async () => {
    const isFirst = await isFirstViewToday();
    setIsFirstView(isFirst);
    if (isFirst) {
      await markAsViewedToday();
    }
  };

  const checkJournalEntry = async () => {
    const today = getTodayDateString();
    const exists = await hasJournalEntry(today);
    setHasJournalToday(exists);
  };

  const handleCtaPress = () => {
    // Navigation vers page climat lunaire (future)
    // Pour l'instant, on peut naviguer vers /lunar ou créer /lunar/daily-climate
    router.push('/lunar');
  };

  const handleJournalPress = () => {
    setJournalModalVisible(true);
  };

  // Render loading
  if (status.isLoading && !data) {
    return (
      <View style={styles.container}>
        <Skeleton width="100%" height={160} borderRadius={borderRadius.md} />
      </View>
    );
  }

  // Pas de données (ne devrait jamais arriver avec les fallbacks)
  if (!data) {
    return null;
  }

  // Derive display data from helpers
  const phaseEmoji = helpers.phaseEmoji;
  const phaseKey = helpers.phaseKey;
  const guidance = t(`ritualCard.guidance.${phaseKey}`, {
    defaultValue: t('ritualCard.guidance.fallback'),
  });
  const vocActive = helpers.vocActive;
  const vocEndTime = helpers.vocEndTime;

  // Texte phase + signe
  const phaseText =
    data.moon.sign !== 'Unknown'
      ? `${data.moon.phase.toUpperCase()} EN ${data.moon.sign.toUpperCase()}`
      : data.moon.phase.toUpperCase();

  return (
    <Animated.View
      style={[
        styles.container,
        {
          opacity: fadeAnim,
          transform: [{ translateY: translateAnim }],
        },
      ]}
    >
      <View style={styles.card}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.headerText}>
            {phaseEmoji} {t('ritualCard.header')}
          </Text>
        </View>

        {/* Phase + Sign */}
        <Text style={styles.phaseTitle}>{phaseText}</Text>

        {/* Guidance */}
        <Text style={styles.guidance}>{guidance}</Text>

        {/* VoC Badge */}
        {vocActive && vocEndTime && (
          <View style={styles.vocBadge}>
            <Text style={styles.vocText}>
              ⚠️ {t('ritualCard.vocActive', { endTime: vocEndTime })}
            </Text>
          </View>
        )}

        {/* Error indicator (données limitées) */}
        {status.error && (
          <View style={styles.errorBadge}>
            <Text style={styles.errorText}>ℹ️ {status.source === 'local' ? 'Calcul local' : 'Cache'}</Text>
          </View>
        )}

        {/* Journal CTA (text-button discret) */}
        <Pressable
          onPress={handleJournalPress}
          style={({ pressed }) => [
            styles.journalCta,
            pressed && styles.journalCtaPressed,
          ]}
        >
          <Text
            style={[
              styles.journalCtaText,
              hasJournalToday && styles.journalCtaTextEdited,
            ]}
          >
            {hasJournalToday ? '✓ ' : ''}
            {hasJournalToday
              ? t('ritualCard.journalEdited')
              : t('ritualCard.journalPrompt')}
          </Text>
        </Pressable>

        {/* CTA climat lunaire */}
        <Pressable
          onPress={handleCtaPress}
          style={({ pressed }) => [styles.cta, pressed && styles.ctaPressed]}
        >
          <Text style={styles.ctaText}>→ {t('ritualCard.cta')}</Text>
        </Pressable>
      </View>

      {/* Journal Modal */}
      {data && (
        <JournalEntryModal
          visible={journalModalVisible}
          onClose={() => setJournalModalVisible(false)}
          moonContext={data.moon}
        />
      )}
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: spacing.md,
    marginVertical: spacing.sm,
  },
  card: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  header: {
    marginBottom: spacing.sm,
  },
  headerText: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    textTransform: 'uppercase',
    letterSpacing: 0.8,
  },
  phaseTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.md,
    letterSpacing: 0.5,
  },
  guidance: {
    ...fonts.body,
    color: colors.text,
    lineHeight: 24,
    marginBottom: spacing.md,
    fontStyle: 'italic',
  },
  vocBadge: {
    backgroundColor: 'rgba(251, 191, 36, 0.1)',
    borderWidth: 1,
    borderColor: colors.warning,
    borderRadius: borderRadius.sm,
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
    marginBottom: spacing.sm,
  },
  vocText: {
    ...fonts.bodySmall,
    color: colors.warning,
  },
  errorBadge: {
    backgroundColor: 'rgba(160, 160, 176, 0.1)',
    borderWidth: 1,
    borderColor: colors.textMuted,
    borderRadius: borderRadius.sm,
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
    marginBottom: spacing.sm,
  },
  errorText: {
    ...fonts.caption,
    color: colors.textMuted,
  },
  cta: {
    paddingVertical: spacing.sm,
    marginTop: spacing.xs,
  },
  ctaPressed: {
    opacity: 0.7,
  },
  ctaText: {
    ...fonts.button,
    color: colors.accent,
    fontSize: 15,
  },
  journalCta: {
    paddingVertical: spacing.sm,
    marginBottom: spacing.xs,
  },
  journalCtaPressed: {
    opacity: 0.6,
  },
  journalCtaText: {
    ...fonts.body,
    color: colors.textMuted,
    fontSize: 14,
  },
  journalCtaTextEdited: {
    color: colors.success,
  },
});
