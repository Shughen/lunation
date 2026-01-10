import React, { useEffect, useState, useCallback, useMemo } from 'react';
import { View, ScrollView, Alert, StyleSheet, Platform, Text, TouchableOpacity } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import TodayHeader from '@/components/home/TodayHeader';
import CycleCard from '@/components/home/CycleCard';
import MoodCard from '@/components/home/MoodCard';
import AstroCard from '@/components/home/AstroCard';
import ExploreGrid from '@/components/home/ExploreGrid';
import QuickPeriodLog from '@/components/QuickPeriodLog';
import CycleCountdown from '@/components/CycleCountdown';
import FertilityWidget from '@/components/FertilityWidget';
import { MedicalDisclaimer } from '@/components/MedicalDisclaimer';
import LunarRevolutionHero from '@/components/home/LunarRevolutionHero';
import MonthlyTrendsCard from '@/components/home/MonthlyTrendsCard';
import NatalSummaryCard from '@/components/home/NatalSummaryCard';
import { Analytics } from '@/lib/analytics';
import { hasHealthConsent } from '@/lib/services/consentService';
import { getCachedMoonContext } from '@/lib/services/moonCalculator';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { useProfileStore } from '@/stores/profileStore';
import { useLunarRevolutionStore } from '@/stores/useLunarRevolutionStore';
import haptics from '@/utils/haptics';
import { color, space, layout, type as typography, hitSlop as hitSlopTokens } from '@/theme/tokens';

export default function Home() {
  const router = useRouter();
  
  // Store cycle (source de vérité unique)
  const { getCurrentCycleData, cycles } = useCycleHistoryStore();
  
  // Store profil pour thème natal
  const { profile, shouldShowCycles } = useProfileStore();
  
  // Store révolution lunaire
  const { currentMonthRevolution, fetchForMonth, status: revolutionStatus } = useLunarRevolutionStore();

  // État cycle
  const [hasHealth, setHasHealth] = useState(false);
  
  // Déterminer si les cycles doivent être affichés
  const showCycles = shouldShowCycles();
  
  useEffect(() => {
    console.log('[ROUTING] Mounted Home');
  }, []);
  
  // Charger la révolution lunaire du mois actuel
  useEffect(() => {
    // Laisser le store gérer la validation : il vérifie automatiquement le cache, 
    // la complétude du profil (birthDate, birthTime, birthPlace) et retourne une erreur claire si nécessaire
    // On déclenche le chargement si le profil change (notamment après chargement depuis storage)
    console.log('[Home] ⚡ Tentative chargement révolution - Profil:', {
      hasBirthDate: !!profile.birthDate,
      hasBirthTime: !!profile.birthTime,
      hasBirthPlace: !!profile.birthPlace,
      birthDate: profile.birthDate,
      birthTime: profile.birthTime,
      birthPlace: profile.birthPlace,
    });
    fetchForMonth(new Date()).catch(err => {
      console.error('[Home] ❌ Erreur chargement révolution:', err);
    });
  }, [profile.birthDate, profile.birthTime, profile.birthPlace, fetchForMonth]);

  useEffect(() => {
    loadHealthConsent();
  }, []);

  const loadHealthConsent = async () => {
    const health = await hasHealthConsent();
    setHasHealth(health);
  };
  
  // Calculer cycle depuis store
  const cycleData = getCurrentCycleData();
  const cycle = cycleData ? {
    dayLabel: `Jour ${cycleData.dayOfCycle}${cycleData.isInPeriod ? ' (en cours)' : ''}`,
    phase: cycleData.phase,
    energy: cycleData.energy,
    fertile: cycleData.fertile,
  } : null;

  // Données lunaires réelles
  const moonContext = useMemo(() => getCachedMoonContext(), []);
  const moonSign = moonContext.displayText;
  const mantra = moonContext.mantra;
  const astroEnergyText = useMemo(() => moonContext.sign.energy, [moonContext]);

  // Handlers avec haptics
  const openCycleDetails = useCallback(async () => {
    haptics.light();
    const health = await hasHealthConsent();
    
    if (!health) {
      haptics.warning();
      Alert.alert(
        'Consentement requis',
        'Active le consentement santé et configure ton cycle pour accéder aux détails.',
        [
          { text: 'Plus tard' },
          { 
            text: 'Ouvrir les paramètres', 
            onPress: () => {
              haptics.medium();
              router.push('/settings/privacy');
            }
          }
        ]
      );
      return;
    }
    
    Analytics.track('home_tap_cycle_details');
    router.push('/cycle-astro');
  }, [router]);

  const openJournal = useCallback(() => {
    haptics.light();
    Analytics.track('home_quick_mood_opened');
    router.push('/journal');
  }, [router]);

  const openAstroDetails = useCallback(() => {
    haptics.light();
    Analytics.track('home_tap_astro_details');
    router.push('/horoscope'); // Fix: Astro du jour → Horoscope (pas cycle-astro)
  }, [router]);

  const openLunarRevolution = useCallback(() => {
    haptics.light();
    Analytics.track('home_tap_lunar_revolution');
    router.push('/lunar-revolution');
  }, [router]);

  const openNatalReading = useCallback(() => {
    haptics.light();
    Analytics.track('home_tap_natal_summary');
    router.push('/natal-reading');
  }, [router]);

  const onExploreTap = useCallback((feature: string) => {
    haptics.medium();
    Analytics.track('home_explore_tapped', { feature });
    
    const routes: Record<string, string> = {
      my_cycles: '/my-cycles',
      calendar: '/calendar',
      theme: '/natal-reading',  // Nouveau système avec backend FastAPI
      compat: '/compatibility',
      horoscope: '/horoscope',
      parent_enfant: '/parent-child'
    };
    
    const targetRoute = routes[feature];
    if (targetRoute) {
      router.push(targetRoute as any);
    } else {
      Alert.alert('À venir', 'Cette fonctionnalité arrive bientôt !');
    }
  }, [router]);

  // View impression
  useEffect(() => {
    Analytics.track('home_viewed');
  }, []);

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <StatusBar style="light" backgroundColor={color.bg} />
      
      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
        contentInsetAdjustmentBehavior="automatic"
      >
        {/* Header Aujourd'hui */}
        <TodayHeader
          cycleLabel={showCycles && hasHealth && cycle ? `${cycle.dayLabel} – ${cycle.phase}` : moonSign}
          moonLabel={moonSign}
          mantra={mantra}
        />

        <View style={styles.spacer} />

        {/* Section Héro : Révolution lunaire du mois */}
        <LunarRevolutionHero
          moonSign={currentMonthRevolution?.moonSign}
          house={currentMonthRevolution?.house}
          isLoading={revolutionStatus === 'loading'}
          onPress={openLunarRevolution}
        />

        {/* Section : Tendances du mois */}
        <MonthlyTrendsCard
          focus={currentMonthRevolution?.focus}
          summary={currentMonthRevolution?.interpretationSummary}
          isLoading={revolutionStatus === 'loading'}
        />

        {/* Section : Thème natal (mini résumé) */}
        <NatalSummaryCard
          sun={profile.sunSign ? {
            sign: profile.sunSign.name,
            emoji: profile.sunSign.emoji,
            element: 'Feu', // TODO: récupérer depuis données complètes
          } : undefined}
          moon={profile.moonSign ? {
            sign: profile.moonSign.name,
            emoji: profile.moonSign.emoji,
            element: 'Eau', // TODO: récupérer depuis données complètes
          } : undefined}
          ascendant={profile.ascendant ? {
            sign: profile.ascendant.name,
            emoji: profile.ascendant.emoji,
            element: 'Air', // TODO: récupérer depuis données complètes
          } : undefined}
          onPress={openNatalReading}
        />

        {/* Section Cycles (conditionnelle) */}
        {showCycles && (
          <>
            {/* Carte Cycle */}
            {hasHealth && cycle ? (
              <CycleCard
                dayLabel={cycle.dayLabel}
                phase={cycle.phase}
                energy={cycle.energy}
                fertile={cycle.fertile}
                onPress={openCycleDetails}
              />
            ) : (
              <CycleCard
                dayLabel="Commence ici"
                phase="Configure ton cycle"
                energy="—"
                fertile={false}
                onPress={() => {
                  haptics.light();
                  router.push('/settings/cycle');
                }}
              />
            )}

            {/* Quick Period Log */}
            <QuickPeriodLog />
            
            {/* Countdown prochaines règles */}
            <CycleCountdown />
            
            {/* Fertilité & Ovulation */}
            <FertilityWidget />
            
            {/* Link vers Mes cycles */}
            <TouchableOpacity
              onPress={() => {
                haptics.light();
                router.push('/my-cycles' as any);
              }}
              style={{
                alignSelf: 'flex-end',
                marginHorizontal: space.lg,
                marginBottom: space.sm,
              }}
              hitSlop={hitSlopTokens.md}
            >
              <Text style={{ 
                ...typography.bodySm, 
                color: color.brand, 
                fontWeight: '600' 
              }}>
                → Mes cycles
              </Text>
            </TouchableOpacity>
          </>
        )}

        {/* Carte Humeur */}
        <MoodCard onOpenJournal={openJournal} />

        {/* Carte Astro */}
        <AstroCard 
          moonSign={moonSign} 
          energyText={astroEnergyText} 
          onPress={openAstroDetails} 
        />

        {/* Grille Explorer */}
        <ExploreGrid onTap={onExploreTap} showCycles={showCycles} />

        {/* Disclaimer */}
        <View style={styles.disclaimerContainer}>
          <MedicalDisclaimer compact />
        </View>

        {/* Bottom padding */}
        <View style={styles.bottomPadding} />
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: color.bg,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    paddingHorizontal: layout.containerPadding,
    paddingBottom: space['2xl'],
  },
  spacer: {
    height: space.sm,
  },
  disclaimerContainer: {
    marginTop: space.lg,
  },
  bottomPadding: {
    height: space.xl,
  },
});

