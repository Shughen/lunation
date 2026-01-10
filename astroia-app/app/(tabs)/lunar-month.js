import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, ActivityIndicator, TouchableOpacity } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { StatusBar } from 'expo-status-bar';
import { supabase } from '@/lib/supabase';
import { lunarCycleService } from '@/lib/api/lunarCycleService';
import { colors, fonts, spacing, borderRadius, shadows } from '@/constants/theme';

// Labels français pour les phases
const PHASE_LABELS = {
  start: 'Ouverture & nouveaux ressentis',
  rise: 'Montée émotionnelle & prises de conscience',
  peak: 'Apogée & intensité intérieure',
  integration: 'Intégration & retour à soi',
};

// Helper pour formater une date en format français (ex: 12/11/2025)
const formatDateFR = (date) => {
  if (!date) return '';
  const d = new Date(date);
  const day = String(d.getDate()).padStart(2, '0');
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const year = d.getFullYear();
  return `${day}/${month}/${year}`;
};

export default function LunarMonthScreen() {
  const [userId, setUserId] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [cycleData, setCycleData] = useState(null);
  const [todayData, setTodayData] = useState(null);

  // Récupérer l'utilisateur connecté
  useEffect(() => {
    loadUser();
  }, []);

  const loadUser = async () => {
    try {
      const { data: { user }, error: userError } = await supabase.auth.getUser();
      
      if (userError) {
        throw userError;
      }
      
      if (!user) {
        setError('Vous devez être connecté pour voir votre cycle lunaire.');
        setIsLoading(false);
        return;
      }
      
      setUserId(user.id);
      loadCycleData(user.id);
    } catch (err) {
      console.error('[LunarMonth] Erreur récupération utilisateur:', err);
      setError('Impossible de charger ton cycle lunaire pour le moment. Vérifie ta connexion ou réessaie plus tard.');
      setIsLoading(false);
    }
  };

  const loadCycleData = async (userId) => {
    try {
      setIsLoading(true);
      setError(null);

      // Récupérer ou créer le cycle actif
      const cycle = await lunarCycleService.getOrCreateCurrentLunarCycle(userId);
      
      // Récupérer les données du jour actuel
      const today = await lunarCycleService.getLunarDayForDate(userId, new Date());
      
      if (!today) {
        // Si aucune donnée pour aujourd'hui, le cycle est peut-être expiré ou en transition
        setError('Aucun cycle actif trouvé pour aujourd\'hui.');
        setIsLoading(false);
        return;
      }

      setCycleData(cycle);
      setTodayData(today);
      setIsLoading(false);
    } catch (err) {
      console.error('[LunarMonth] Erreur chargement cycle:', err);
      setError('Impossible de charger ton cycle lunaire pour le moment. Vérifie ta connexion ou réessaie plus tard.');
      setIsLoading(false);
    }
  };

  const handleRetry = () => {
    if (userId) {
      loadCycleData(userId);
    } else {
      loadUser();
    }
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container} start={{ x: 0, y: 0 }} end={{ x: 1, y: 1 }}>
      <SafeAreaView style={styles.safeArea} edges={['top']}>
        <StatusBar style="light" backgroundColor={colors.darkBg[0]} />
        
        <ScrollView
          style={styles.scrollView}
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          {/* Header */}
          <View style={styles.header}>
            <Text style={styles.headerTitle}>Mois lunaire</Text>
            <Text style={styles.headerSubtitle}>Ton cycle personnel de 28 jours</Text>
          </View>

          {/* État de chargement */}
          {isLoading && (
            <View style={styles.loadingContainer}>
              <ActivityIndicator size="large" color={colors.accent} />
              <Text style={styles.loadingText}>Calcul de ton cycle lunaire…</Text>
            </View>
          )}

          {/* État d'erreur */}
          {error && !isLoading && (
            <View style={styles.errorContainer}>
              <Ionicons name="alert-circle" size={48} color={colors.error} />
              <Text style={styles.errorTitle}>Oops !</Text>
              <Text style={styles.errorText}>{error}</Text>
              <TouchableOpacity
                style={styles.retryButton}
                onPress={handleRetry}
                activeOpacity={0.8}
              >
                <LinearGradient
                  colors={colors.ctaGradient}
                  style={styles.retryButtonGradient}
                  start={{ x: 0, y: 0 }}
                  end={{ x: 1, y: 0 }}
                >
                  <Ionicons name="refresh" size={20} color="white" />
                  <Text style={styles.retryButtonText}>Réessayer</Text>
                </LinearGradient>
              </TouchableOpacity>
            </View>
          )}

          {/* État de succès */}
          {!isLoading && !error && cycleData && todayData && (
            <>
              {/* Carte principale : Dates du cycle */}
              <View style={styles.cycleCard}>
                <View style={styles.cardHeader}>
                  <Ionicons name="calendar" size={24} color={colors.accent} />
                  <Text style={styles.cardTitle}>Période du cycle</Text>
                </View>
                <View style={styles.datesContainer}>
                  <View style={styles.dateItem}>
                    <Text style={styles.dateLabel}>Début</Text>
                    <Text style={styles.dateValue}>{formatDateFR(cycleData.cycleStartDate)}</Text>
                  </View>
                  <View style={styles.dateSeparator}>
                    <Ionicons name="arrow-forward" size={20} color={colors.textMuted} />
                  </View>
                  <View style={styles.dateItem}>
                    <Text style={styles.dateLabel}>Fin</Text>
                    <Text style={styles.dateValue}>{formatDateFR(cycleData.cycleEndDate)}</Text>
                  </View>
                </View>
                <View style={styles.fullDateText}>
                  <Text style={styles.fullDate}>
                    du {formatDateFR(cycleData.cycleStartDate)} au {formatDateFR(cycleData.cycleEndDate)}
                  </Text>
                </View>
              </View>

              {/* Carte : Jour actuel */}
              <View style={styles.todayCard}>
                <View style={styles.cardHeader}>
                  <Ionicons name="moon" size={24} color={colors.primary} />
                  <Text style={styles.cardTitle}>Aujourd'hui</Text>
                </View>
                <View style={styles.todayContent}>
                  <Text style={styles.todayLabel}>
                    Jour {todayData.cycleDay} / 28
                  </Text>
                </View>
              </View>

              {/* Carte : Phase actuelle */}
              <View style={styles.phaseCard}>
                <View style={styles.cardHeader}>
                  <Ionicons name="sparkles" size={24} color={colors.secondary} />
                  <Text style={styles.cardTitle}>Phase actuelle</Text>
                </View>
                <View style={styles.phaseContent}>
                  <View style={styles.phaseBadge}>
                    <Text style={styles.phaseName}>
                      {PHASE_LABELS[todayData.phase] || todayData.phase}
                    </Text>
                  </View>
                  <Text style={styles.phaseDescription}>
                    {todayData.phase === 'start' && 'Phase d\'ouverture et de nouveaux ressentis. Un nouveau cycle commence, propice à l\'introspection et aux nouveaux départs.'}
                    {todayData.phase === 'rise' && 'Phase de montée émotionnelle et de prises de conscience. Les émotions s\'intensifient, les intuitions se clarifient.'}
                    {todayData.phase === 'peak' && 'Phase d\'apogée et d\'intensité intérieure. Le moment le plus intense du cycle, avec des tensions et des opportunités.'}
                    {todayData.phase === 'integration' && 'Phase d\'intégration et de retour à soi. Temps de digestion des expériences et de préparation à la transition.'}
                  </Text>
                </View>
              </View>

              {/* Informations supplémentaires */}
              <View style={styles.infoCard}>
                <View style={styles.infoRow}>
                  <Ionicons name="information-circle-outline" size={20} color={colors.textMuted} />
                  <Text style={styles.infoText}>
                    Ton cycle lunaire personnel suit un rythme de 28 jours, aligné avec les phases de la Lune.
                  </Text>
                </View>
              </View>
            </>
          )}
        </ScrollView>
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
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    paddingHorizontal: spacing.md,
    paddingTop: spacing.lg,
    paddingBottom: spacing.xl,
  },
  header: {
    marginBottom: spacing.xl,
  },
  headerTitle: {
    fontSize: fonts.sizes.xxl,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.xs,
  },
  headerSubtitle: {
    fontSize: fonts.sizes.md,
    color: colors.textMuted,
  },
  loadingContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.xxl,
    minHeight: 200,
  },
  loadingText: {
    fontSize: fonts.sizes.md,
    color: colors.textMuted,
    marginTop: spacing.md,
  },
  errorContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.xxl,
    minHeight: 200,
  },
  errorTitle: {
    fontSize: fonts.sizes.xl,
    fontWeight: 'bold',
    color: colors.text,
    marginTop: spacing.md,
    marginBottom: spacing.sm,
  },
  errorText: {
    fontSize: fonts.sizes.md,
    color: colors.textSecondary,
    textAlign: 'center',
    marginHorizontal: spacing.lg,
    marginBottom: spacing.lg,
    lineHeight: 22,
  },
  retryButton: {
    marginTop: spacing.md,
    borderRadius: borderRadius.xl,
    overflow: 'hidden',
    ...shadows.md,
  },
  retryButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    gap: spacing.sm,
  },
  retryButtonText: {
    fontSize: fonts.sizes.md,
    color: 'white',
    fontWeight: 'bold',
  },
  cycleCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.2)',
    ...shadows.md,
  },
  todayCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(107, 124, 255, 0.2)',
    ...shadows.md,
  },
  phaseCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.2)',
    ...shadows.md,
  },
  cardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.md,
    gap: spacing.sm,
  },
  cardTitle: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: colors.text,
  },
  datesContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: spacing.sm,
  },
  dateItem: {
    flex: 1,
    alignItems: 'center',
  },
  dateLabel: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    marginBottom: spacing.xs,
  },
  dateValue: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: colors.text,
  },
  dateSeparator: {
    paddingHorizontal: spacing.md,
  },
  fullDateText: {
    marginTop: spacing.md,
    paddingTop: spacing.md,
    borderTopWidth: 1,
    borderTopColor: 'rgba(139, 92, 246, 0.2)',
  },
  fullDate: {
    fontSize: fonts.sizes.md,
    color: colors.textSecondary,
    textAlign: 'center',
  },
  todayContent: {
    alignItems: 'center',
  },
  todayLabel: {
    fontSize: fonts.sizes.xxl,
    fontWeight: 'bold',
    color: colors.primary,
  },
  phaseContent: {
    marginTop: spacing.sm,
  },
  phaseBadge: {
    backgroundColor: 'rgba(139, 92, 246, 0.15)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  phaseName: {
    fontSize: fonts.sizes.lg,
    fontWeight: '600',
    color: colors.secondary,
    textAlign: 'center',
  },
  phaseDescription: {
    fontSize: fonts.sizes.md,
    color: colors.textSecondary,
    lineHeight: 22,
  },
  infoCard: {
    backgroundColor: 'rgba(139, 92, 246, 0.1)',
    borderRadius: borderRadius.lg,
    padding: spacing.md,
    marginTop: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.2)',
  },
  infoRow: {
    flexDirection: 'row',
    gap: spacing.sm,
    alignItems: 'flex-start',
  },
  infoText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: colors.textSecondary,
    lineHeight: 20,
  },
});

