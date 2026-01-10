import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { CycleEntry } from '@/stores/cycleHistoryStore';
import { color, space, radius, type as typography } from '@/theme/tokens';

interface CycleHistoryBarProps {
  cycle: CycleEntry;
}

/**
 * CycleHistoryBar - Barre horizontale représentant un cycle (lecture seule)
 * Rose pour règles, jaune pour le reste, icône ovulation
 */
export default function CycleHistoryBar({ cycle }: CycleHistoryBarProps) {
  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' });
  };
  
  const startDate = formatDate(cycle.startDate);
  const endDate = cycle.endDate ? formatDate(cycle.endDate) : 'En cours';
  const periodLength = cycle.periodLength || 0;
  const cycleLength = cycle.cycleLength || 0;
  
  // Calculer proportions
  const totalWidth = cycleLength || 28;
  const periodPercentage = totalWidth > 0 ? (periodLength / totalWidth) * 100 : 0;
  const ovulationDay = Math.max(0, totalWidth - 14); // ~14 jours avant fin
  const ovulationPercentage = totalWidth > 0 ? (ovulationDay / totalWidth) * 100 : 0;

  return (
    <View style={styles.container}>
      {/* Dates */}
      <View style={styles.header}>
        <Text style={styles.dateRange}>
          {startDate} - {endDate}
        </Text>
        {cycleLength > 0 && (
          <Text style={styles.cycleLength}>{cycleLength}</Text>
        )}
      </View>
      
      {/* Barre visuelle */}
      <View style={styles.bar}>
        {/* Segment règles (rose) */}
        {periodLength > 0 && (
          <View 
            style={[
              styles.barSegmentPeriod, 
              { width: `${Math.min(periodPercentage, 100)}%` }
            ]}
          >
            <Text style={styles.barLabel}>{periodLength}</Text>
          </View>
        )}
        
        {/* Segment reste (jaune) */}
        {cycleLength > 0 && periodPercentage < 100 && (
          <View 
            style={[
              styles.barSegmentRest,
              { width: `${100 - periodPercentage}%` }
            ]}
          >
            {/* Icône ovulation */}
            {ovulationPercentage > periodPercentage && (
              <View 
                style={[
                  styles.ovulationMarker,
                  { 
                    left: `${((ovulationPercentage - periodPercentage) / (100 - periodPercentage)) * 100}%` 
                  }
                ]}
              >
                <Text style={styles.ovulationIcon}>🥚</Text>
              </View>
            )}
          </View>
        )}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: space.md,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: space.xs,
  },
  dateRange: {
    ...typography.bodySm,
    color: color.text,
    fontWeight: '600',
  },
  cycleLength: {
    ...typography.bodySm,
    color: color.textMuted,
    fontWeight: '600',
  },
  bar: {
    flexDirection: 'row',
    height: 40,
    borderRadius: radius.sm,
    overflow: 'hidden',
  },
  barSegmentPeriod: {
    backgroundColor: '#FF6B9D',
    justifyContent: 'center',
    alignItems: 'center',
  },
  barSegmentRest: {
    backgroundColor: '#FFD93D',
    position: 'relative',
  },
  barLabel: {
    ...typography.label,
    color: 'white',
  },
  ovulationMarker: {
    position: 'absolute',
    top: -8,
    width: 24,
    height: 24,
    alignItems: 'center',
    justifyContent: 'center',
  },
  ovulationIcon: {
    fontSize: 20,
  },
});

