/**
 * Home Tab Screen - "Mon Cycle"
 * Dashboard avec Hero Lunar Card et Bottom Sheet quotidien
 *
 * Architecture 3 tabs:
 * - Hero: Revolution Lunaire Mensuelle (60% ecran)
 * - TodayMiniCard: ouvre le bottom sheet
 * - NatalMiniCard: raccourci vers le theme natal
 * - TodayBottomSheet: rituel quotidien complet
 */

import React, { useEffect, useCallback, useState, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  RefreshControl,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import NetInfo from '@react-native-community/netinfo';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { useCurrentLunarReturn, useVocStatus, useMansionToday } from '../../hooks/useLunarData';
import { useLunar } from '../../contexts/LunarProvider';
import { haptics } from '../../services/haptics';

// Components
import { VocBanner } from '../../components/VocBanner';
import { HeroLunarCard } from '../../components/HeroLunarCard';
import { TodayMiniCard } from '../../components/TodayMiniCard';
import { NatalMiniCard } from '../../components/NatalMiniCard';
import { TodayBottomSheet, TodayBottomSheetRef } from '../../components/TodayBottomSheet';
import { LunationLogo } from '../../components/LunationLogo';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors: bgColors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: bgColors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

export default function HomeScreen() {
  const router = useRouter();
  const bottomSheetRef = useRef<TodayBottomSheetRef>(null);
  const [isOnline, setIsOnline] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  // Data hooks
  const { data: currentLunarReturn, mutate: refreshLunarReturn } = useCurrentLunarReturn();
  const { current: lunarData, helpers } = useLunar();
  const { data: vocStatus } = useVocStatus();
  const { data: mansionData } = useMansionToday();

  // Network state
  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsOnline(state.isConnected ?? true);
    });
    return () => unsubscribe();
  }, []);

  // Pull-to-refresh
  const onRefresh = useCallback(async () => {
    setRefreshing(true);
    await refreshLunarReturn();
    setRefreshing(false);
  }, [refreshLunarReturn]);

  // Open bottom sheet at 50%
  const handleTodayPress = useCallback(() => {
    haptics.light();
    bottomSheetRef.current?.snapToIndex(1);
  }, []);

  // Navigate to profile (which now contains natal chart)
  const handleNatalPress = useCallback(() => {
    haptics.light();
    router.push('/(tabs)/profile');
  }, [router]);

  return (
    <View style={styles.flex1}>
      <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
        <ScrollView
          contentContainerStyle={styles.scrollContent}
          refreshControl={
            <RefreshControl
              refreshing={refreshing}
              onRefresh={onRefresh}
              tintColor={colors.accent}
              colors={[colors.accent]}
            />
          }
        >
          {/* Header */}
          <View style={styles.header}>
            <LunationLogo variant="horizontal" size={80} />
            <Text style={styles.subtitle}>Ton rituel lunaire</Text>
          </View>

          {/* Offline Banner */}
          {!isOnline && (
            <View style={styles.offlineCard}>
              <Text style={styles.offlineTitle}>Mode hors ligne</Text>
              <Text style={styles.offlineText}>
                Certaines fonctionnalites peuvent etre limitees.
              </Text>
            </View>
          )}

          {/* VoC Banner (conditionnelle) */}
          <VocBanner vocStatus={vocStatus} />

          {/* HERO: Revolution Lunaire Mensuelle (60% ecran) */}
          <HeroLunarCard
            lunarReturn={currentLunarReturn}
            loading={false}
          />

          {/* Mini Cards */}
          <TodayMiniCard
            moonPhase={lunarData?.moon?.phase}
            moonSign={lunarData?.moon?.sign}
            onPress={handleTodayPress}
          />

          <NatalMiniCard onPress={handleNatalPress} />

          {/* Extra bottom padding for scroll */}
          <View style={{ height: 100 }} />
        </ScrollView>

        {/* Bottom Sheet */}
        <TodayBottomSheet
          ref={bottomSheetRef}
          vocStatus={vocStatus}
          lunarReturn={currentLunarReturn}
          mansion={mansionData}
        />
      </LinearGradientComponent>
    </View>
  );
}

const styles = StyleSheet.create({
  flex1: {
    flex: 1,
  },
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingBottom: 100,
  },
  header: {
    marginBottom: spacing.lg,
    paddingHorizontal: spacing.lg,
    alignItems: 'center',
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.xs,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
  },
  offlineCard: {
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginHorizontal: spacing.md,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
  },
  offlineTitle: {
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.xs,
    fontWeight: '500',
  },
  offlineText: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    lineHeight: 18,
  },
});
