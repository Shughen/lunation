import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { color, space, radius, type as typography } from '@/theme/tokens';
import { LunarRevolution } from '@/lib/services/lunarRevolutionService';

interface RevolutionCardProps {
  revolution: LunarRevolution;
}

export default React.memo(function RevolutionCard({ revolution }: RevolutionCardProps) {
  return (
    <View style={styles.card}>
      <Text style={styles.label}>RÉVOLUTION LUNAIRE</Text>
      
      <View style={styles.mainInfo}>
        <Text style={styles.moonSign}>
          {revolution.moonSignEmoji} Lune en {revolution.moonSign}
        </Text>
        <Text style={styles.house}>
          Maison {revolution.house}
        </Text>
        <Text style={styles.phase}>
          {revolution.phaseName}
        </Text>
      </View>
      
      {revolution.interpretationSummary && (
        <View style={styles.summaryContainer}>
          <Text style={styles.summaryLabel}>Résumé du mois</Text>
          <Text style={styles.summaryText}>
            {revolution.interpretationSummary}
          </Text>
        </View>
      )}
      
      {revolution.focus && (
        <View style={styles.focusContainer}>
          <Text style={styles.focusLabel}>Domaines activés</Text>
          <Text style={styles.focusText}>
            Focus : {revolution.focus}
          </Text>
        </View>
      )}
    </View>
  );
});

const styles = StyleSheet.create({
  card: {
    borderRadius: radius.lg,
    padding: space.lg,
    backgroundColor: color.surfaceElevated,
    borderWidth: 1,
    borderColor: color.border,
    marginBottom: space.lg,
  },
  label: {
    ...typography.label,
    color: color.brand,
    letterSpacing: 1.2,
    marginBottom: space.md,
  },
  mainInfo: {
    marginBottom: space.md,
  },
  moonSign: {
    ...typography.h1,
    color: color.text,
    fontWeight: '800',
    marginBottom: space.xs,
  },
  house: {
    ...typography.h4,
    color: color.textSecondary,
    marginBottom: space.xs,
  },
  phase: {
    ...typography.body,
    color: color.textMuted,
  },
  summaryContainer: {
    marginTop: space.md,
    paddingTop: space.md,
    borderTopWidth: 1,
    borderTopColor: color.border,
  },
  summaryLabel: {
    ...typography.label,
    color: color.brand,
    marginBottom: space.xs,
  },
  summaryText: {
    ...typography.body,
    color: color.textSecondary,
    lineHeight: 22,
  },
  focusContainer: {
    marginTop: space.md,
    paddingTop: space.md,
    borderTopWidth: 1,
    borderTopColor: color.border,
  },
  focusLabel: {
    ...typography.label,
    color: color.brand,
    marginBottom: space.xs,
  },
  focusText: {
    ...typography.body,
    color: color.textSecondary,
    fontWeight: '600',
  },
});

