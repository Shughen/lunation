import React, { useMemo } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { predictOvulationDate, predictFertilityWindow } from '@/lib/services/cycleCalculator';
import { color, space, radius, type as typography } from '@/theme/tokens';

/**
 * Widget compact affichant la fenêtre de fertilité prévue
 */
export default function FertilityWidget() {
  const { predictNextPeriod, getAverages } = useCycleHistoryStore();
  
  const fertilityInfo = useMemo(() => {
    const prediction = predictNextPeriod();
    const averages = getAverages();
    
    if (!prediction || !averages) return null;
    
    const nextDate = new Date(prediction.nextDate);
    const ovulation = predictOvulationDate(nextDate, averages.avgCycle);
    const fertile = predictFertilityWindow(ovulation);
    
    if (!ovulation || !fertile) return null;
    
    // Formatter les dates
    const formatDate = (date: Date) => {
      return date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' });
    };
    
    const ovulationStr = formatDate(ovulation);
    const fertileStartStr = formatDate(fertile.start);
    const fertileEndStr = formatDate(fertile.end);
    
    return {
      ovulation: ovulationStr,
      fertileWindow: `${fertileStartStr} – ${fertileEndStr}`,
    };
  }, [predictNextPeriod, getAverages]);
  
  if (!fertilityInfo) return null;
  
  return (
    <View style={styles.container}>
      <View style={styles.row}>
        <Text style={styles.emoji}>🥚</Text>
        <View style={styles.textContainer}>
          <Text style={styles.label}>Ovulation prévue</Text>
          <Text style={styles.value}>{fertilityInfo.ovulation}</Text>
        </View>
      </View>
      
      <View style={[styles.row, { marginTop: space.xs }]}>
        <Text style={styles.emoji}>🌱</Text>
        <View style={styles.textContainer}>
          <Text style={styles.label}>Fenêtre fertile</Text>
          <Text style={styles.value}>{fertilityInfo.fertileWindow}</Text>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: space.lg,
    marginTop: space.md,
    padding: space.md,
    backgroundColor: `${color.brand}11`,
    borderRadius: radius.lg,
    borderWidth: 1,
    borderColor: `${color.brand}22`,
  },
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.sm,
  },
  emoji: {
    fontSize: 20,
  },
  textContainer: {
    flex: 1,
  },
  label: {
    ...typography.caption,
    color: color.textMuted,
    marginBottom: 2,
  },
  value: {
    ...typography.h4,
    color: color.text,
  },
});

