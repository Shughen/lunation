/**
 * Home Tab Screen
 * Main dashboard with lunar data and widgets
 */

import React, { useEffect, useCallback, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
  RefreshControl,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import NetInfo from '@react-native-community/netinfo';
import { useRouter, useFocusEffect } from 'expo-router';
import { useAuthStore } from '../../stores/useAuthStore';
import { useNotificationsStore } from '../../stores/useNotificationsStore';
import { isDevAuthBypassActive } from '../../services/api';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { DailyRitualCard } from '../../components/DailyRitualCard';
import { VocWidget } from '../../components/VocWidget';
import { TransitsWidget } from '../../components/TransitsWidget';
import { CurrentLunarCard } from '../../components/CurrentLunarCard';
import { JournalPrompt } from '../../components/JournalPrompt';
import { setupNotificationTapListener, shouldReschedule } from '../../services/notificationScheduler';
import { useCurrentLunarReturn } from '../../hooks/useLunarData';
import { haptics } from '../../services/haptics';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors: bgColors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: bgColors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

export default function HomeScreen() {
  const router = useRouter();
  const { isAuthenticated } = useAuthStore();
  const { notificationsEnabled, hydrated, loadPreferences, scheduleAllNotifications } = useNotificationsStore();

  const [isOnline, setIsOnline] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  // Hook SWR pour charger la révolution lunaire en cours
  const { data: currentLunarReturn, mutate: refreshLunarReturn } = useCurrentLunarReturn();

  // Hydratation store notifications au mount
  useEffect(() => {
    if (!hydrated) {
      loadPreferences();
    }
  }, [hydrated, loadPreferences]);

  // Détecter l'état du réseau
  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsOnline(state.isConnected ?? true);
    });
    return () => unsubscribe();
  }, []);

  // Setup listener tap notifications au mount
  useEffect(() => {
    const subscription = setupNotificationTapListener((screen: string) => {
      console.log(`[HOME] Tap notification → ${screen}`);
      router.push(screen as any);
    });
    return () => subscription.remove();
  }, [router]);

  // Re-scheduler notifications au focus si nécessaire
  useFocusEffect(
    useCallback(() => {
      if (isAuthenticated || isDevAuthBypassActive()) {
        // Refresh révolution lunaire (SWR le gère avec cache)
        refreshLunarReturn();

        // Re-scheduler notifications si nécessaire (max 1x/24h)
        if (notificationsEnabled && hydrated) {
          (async () => {
            const should = await shouldReschedule();
            if (should) {
              console.log('[HOME] Re-scheduling notifications (>24h depuis dernier)');
              await scheduleAllNotifications();
            }
          })();
        }
      }
    }, [isAuthenticated, notificationsEnabled, hydrated, scheduleAllNotifications, refreshLunarReturn])
  );

  // Pull-to-refresh handler
  const onRefresh = useCallback(async () => {
    setRefreshing(true);
    await refreshLunarReturn();
    setRefreshing(false);
  }, [refreshLunarReturn]);

  return (
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
          <Text style={styles.title}>Lunation</Text>
          <Text style={styles.subtitle}>Ton rituel lunaire quotidien</Text>
        </View>

        {/* Carte Mode Hors Connexion */}
        {!isOnline && (
          <View style={styles.offlineCard}>
            <Text style={styles.offlineTitle}>Mode hors ligne</Text>
            <Text style={styles.offlineText}>
              Ton rituel et ton journal restent accessibles. Les donnees viennent du cache local.
            </Text>
          </View>
        )}

        {/* Carte Revolution Lunaire (HERO) */}
        <CurrentLunarCard
          lunarReturn={currentLunarReturn}
          loading={false}
          onRefresh={refreshLunarReturn}
        />

        {/* Carte Rituel Quotidien */}
        <DailyRitualCard />

        {/* Widget Void of Course */}
        <VocWidget />

        {/* Widget Transits Majeurs */}
        <TransitsWidget />

        {/* Widget Journal Prompt */}
        <JournalPrompt />

        {/* Quick Access Card - Natal Chart */}
        <TouchableOpacity
          style={[styles.quickAccessCard, !isOnline && styles.cardDisabled]}
          onPress={() => {
            haptics.light();
            if (!isOnline) {
              Alert.alert('Hors ligne', 'Cette fonctionnalite necessite une connexion Internet.');
              return;
            }
            router.push('/natal-chart');
          }}
          disabled={!isOnline}
        >
          <Text style={styles.quickAccessIcon}>*</Text>
          <View style={styles.quickAccessContent}>
            <Text style={styles.quickAccessTitle}>Theme natal</Text>
            <Text style={styles.quickAccessDesc}>Decouvre ton ciel de naissance</Text>
          </View>
          <Text style={styles.quickAccessArrow}></Text>
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
    paddingBottom: 100, // Extra padding for tab bar
  },
  header: {
    marginBottom: spacing.xl,
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
  quickAccessCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginTop: spacing.md,
    flexDirection: 'row',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  cardDisabled: {
    opacity: 0.5,
  },
  quickAccessIcon: {
    fontSize: 32,
    marginRight: spacing.md,
  },
  quickAccessContent: {
    flex: 1,
  },
  quickAccessTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  quickAccessDesc: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  quickAccessArrow: {
    ...fonts.h2,
    color: colors.accent,
  },
});
