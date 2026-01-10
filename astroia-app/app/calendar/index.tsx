import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Platform, StatusBar as RNStatusBar } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { predictOvulationDate, predictFertilityWindow } from '@/lib/services/cycleCalculator';
import FertilityLegend from '@/components/FertilityLegend';
import { color, space, radius, type as typography, hitSlop as hitSlopTokens } from '@/theme/tokens';
import haptics from '@/utils/haptics';
import { Analytics } from '@/lib/analytics';

/**
 * Calendrier simplifié (compatible Expo Go)
 * Version simplifiée sans react-native-calendars
 */
export default function CalendarScreen() {
  const router = useRouter();
  const { cycles, predictNextPeriod, getAverages, getValidCycles } = useCycleHistoryStore();
  const validCycles = getValidCycles();
  
  useEffect(() => {
    Analytics.track('calendar_view_opened', { totalCycles: cycles.length, validCycles: validCycles.length });
  }, []);
  
  const prediction = predictNextPeriod();
  const averages = getAverages();
  
  const formatDate = (date: Date) => {
    return date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' });
  };
  
  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <StatusBar style="light" backgroundColor={color.bg} />
      
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity
          onPress={() => {
            haptics.light();
            router.back();
          }}
          style={styles.backButton}
          hitSlop={hitSlopTokens.md}
          accessibilityRole="button"
          accessibilityLabel="Retour"
        >
          <Ionicons name="arrow-back" size={24} color={color.text} />
        </TouchableOpacity>
        
        <Text style={styles.headerTitle}>🌙 Calendrier du cycle</Text>
        
        <View style={{ width: 40 }} />
      </View>
      
      <ScrollView
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Version complète arrive bientôt */}
        <View style={styles.comingSoonCard}>
          <Text style={styles.comingSoonIcon}>📅</Text>
          <Text style={styles.comingSoonTitle}>Calendrier visuel arrive bientôt</Text>
          <Text style={styles.comingSoonSubtitle}>
            En attendant, consulte "Mes cycles" pour voir ton historique détaillé.
          </Text>
          
          <TouchableOpacity
            style={styles.comingSoonCTA}
            onPress={() => {
              haptics.light();
              router.push('/my-cycles' as any);
            }}
          >
            <Text style={styles.comingSoonCTAText}>Voir mes cycles →</Text>
          </TouchableOpacity>
        </View>
        
        {/* Prédictions si disponibles */}
        {prediction && averages && (
          <View style={styles.predictionsCard}>
            <Text style={styles.predictionsTitle}>📊 Prédictions</Text>
            
            <View style={styles.predictionRow}>
              <Text style={styles.predictionEmoji}>📅</Text>
              <View style={styles.predictionText}>
                <Text style={styles.predictionLabel}>Prochaines règles</Text>
                <Text style={styles.predictionValue}>{formatDate(prediction.nextDate)}</Text>
              </View>
            </View>
            
            {(() => {
              const nextDate = new Date(prediction.nextDate);
              const ovulation = predictOvulationDate(nextDate, averages.avgCycle);
              const fertile = predictFertilityWindow(ovulation);
              
              return (
                <>
                  {ovulation && (
                    <View style={styles.predictionRow}>
                      <Text style={styles.predictionEmoji}>🥚</Text>
                      <View style={styles.predictionText}>
                        <Text style={styles.predictionLabel}>Ovulation estimée</Text>
                        <Text style={styles.predictionValue}>{formatDate(ovulation)}</Text>
                      </View>
                    </View>
                  )}
                  
                  {fertile && (
                    <View style={styles.predictionRow}>
                      <Text style={styles.predictionEmoji}>🌱</Text>
                      <View style={styles.predictionText}>
                        <Text style={styles.predictionLabel}>Fenêtre fertile</Text>
                        <Text style={styles.predictionValue}>
                          {formatDate(fertile.start)} - {formatDate(fertile.end)}
                        </Text>
                      </View>
                    </View>
                  )}
                </>
              );
            })()}
          </View>
        )}
        
        {/* Légende */}
        <FertilityLegend />
        
        {/* Hint si <2 cycles valides */}
        {validCycles.length < 2 && (
          <View style={styles.hintCard}>
            <Ionicons name="information-circle" size={24} color={color.brand} />
            <Text style={styles.hintText}>
              Pas assez de cycles pour afficher les prédictions.{'\n'}
              Ajoute {2 - validCycles.length} cycle(s) de plus depuis "Mes cycles".
            </Text>
          </View>
        )}
        
        {/* Footer disclaimer */}
        <Text style={styles.disclaimer}>
          💡 Les prédictions sont basées sur tes cycles enregistrés.{'\n'}
          Outil de bien-être, non médical.
        </Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: color.bg,
    paddingTop: Platform.OS === 'android' ? RNStatusBar.currentHeight : 0,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: space.lg,
    paddingVertical: space.md,
    borderBottomWidth: 1,
    borderBottomColor: `${color.text}11`,
  },
  backButton: {
    width: 40,
    height: 40,
    alignItems: 'center',
    justifyContent: 'center',
  },
  headerTitle: {
    ...typography.h2,
    color: color.text,
  },
  scrollContent: {
    paddingBottom: space.xl * 2,
  },
  comingSoonCard: {
    marginHorizontal: space.lg,
    marginTop: space.xl,
    padding: space.xl,
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.xl,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: `${color.brand}22`,
  },
  comingSoonIcon: {
    fontSize: 64,
    marginBottom: space.md,
  },
  comingSoonTitle: {
    ...typography.h2,
    color: color.text,
    marginBottom: space.sm,
    textAlign: 'center',
  },
  comingSoonSubtitle: {
    ...typography.body,
    color: color.textMuted,
    textAlign: 'center',
    marginBottom: space.lg,
  },
  comingSoonCTA: {
    backgroundColor: color.brand,
    paddingHorizontal: space.xl,
    paddingVertical: space.md,
    borderRadius: radius.md,
    minHeight: 48,
  },
  comingSoonCTAText: {
    ...typography.h4,
    color: '#FFFFFF',
  },
  predictionsCard: {
    marginHorizontal: space.lg,
    marginTop: space.lg,
    padding: space.lg,
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.lg,
    borderWidth: 1,
    borderColor: color.border,
  },
  predictionsTitle: {
    ...typography.h3,
    color: color.text,
    marginBottom: space.md,
  },
  predictionRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: space.md,
    marginBottom: space.md,
  },
  predictionEmoji: {
    fontSize: 24,
  },
  predictionText: {
    flex: 1,
  },
  predictionLabel: {
    ...typography.label,
    color: color.textMuted,
    marginBottom: space.xs / 2,
  },
  predictionValue: {
    ...typography.body,
    color: color.text,
    fontWeight: '600',
  },
  hintCard: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.sm,
    marginHorizontal: space.lg,
    marginTop: space.md,
    padding: space.md,
    backgroundColor: `${color.brand}11`,
    borderRadius: radius.lg,
    borderWidth: 1,
    borderColor: `${color.brand}22`,
  },
  hintText: {
    ...typography.bodySm,
    color: color.text,
    flex: 1,
  },
  disclaimer: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
    marginHorizontal: space.lg,
    marginTop: space.lg,
    fontStyle: 'italic',
  },
});
