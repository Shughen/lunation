import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { color, space, radius, type as typography } from '@/theme/tokens';

/**
 * CycleStats - Affiche les moyennes (règles + cycle)
 * Visible uniquement si ≥2 cycles complets
 */
export default function CycleStats() {
  const { getAverages } = useCycleHistoryStore();
  const avg = getAverages();
  
  if (!avg) return null;
  
  // Afficher "≈" si basé sur <3 cycles (estimation moins fiable)
  const prefix = avg.validCount < 3 ? '≈' : '';
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>📊 Mes cycles</Text>
      <Text style={styles.subtitle}>
        {avg.totalCycles} cycles saisis • {avg.validCount} valides
        {avg.validCount < 3 && ' (estimation)'}
      </Text>
      
      <View style={styles.cardsRow}>
        {/* Règles moyennes */}
        <View style={[styles.statCard, styles.statCardPink]}>
          <Text style={styles.statIcon}>🩸</Text>
          <Text style={styles.statValue}>{prefix}{avg.avgPeriod} Jours</Text>
          <Text style={styles.statLabel}>Règles moyennes</Text>
        </View>
        
        {/* Cycle moyen */}
        <View style={[styles.statCard, styles.statCardYellow]}>
          <Text style={styles.statIcon}>🔄</Text>
          <Text style={styles.statValue}>{prefix}{avg.avgCycle} Jours</Text>
          <Text style={styles.statLabel}>Cycle moyen</Text>
        </View>
      </View>
      
      {/* Hint si <3 cycles */}
      {avg.validCount < 3 && (
        <Text style={styles.hint}>
          💡 Ajoute {3 - avg.validCount} cycle(s) de plus pour des prédictions plus fiables
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: space.lg,
    marginBottom: space.xl,
  },
  title: {
    ...typography.h3,
    color: color.text,
    marginBottom: space.xs / 2,
  },
  subtitle: {
    ...typography.caption,
    color: color.textMuted,
    marginBottom: space.md,
  },
  cardsRow: {
    flexDirection: 'row',
    gap: space.sm,
  },
  statCard: {
    flex: 1,
    borderRadius: radius.lg,
    padding: space.lg,
    alignItems: 'center',
  },
  statCardPink: {
    backgroundColor: 'rgba(255, 107, 157, 0.15)',
    borderWidth: 1,
    borderColor: 'rgba(255, 107, 157, 0.3)',
  },
  statCardYellow: {
    backgroundColor: 'rgba(255, 217, 61, 0.15)',
    borderWidth: 1,
    borderColor: 'rgba(255, 217, 61, 0.3)',
  },
  statIcon: {
    fontSize: 32,
    marginBottom: space.xs,
  },
  statValue: {
    ...typography.h2,
    color: color.text,
    marginBottom: space.xs / 2,
  },
  statLabel: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
  },
  hint: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
    marginTop: space.md,
    fontStyle: 'italic',
  },
});

