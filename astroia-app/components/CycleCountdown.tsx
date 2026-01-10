import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { color, space, radius, type as typography, hitSlop as hitSlopTokens } from '@/theme/tokens';
import haptics from '@/utils/haptics';
import { Analytics } from '@/lib/analytics';

/**
 * CycleCountdown - Affiche "X jours restants" jusqu'aux prochaines règles
 * Pressable → navigation vers /my-cycles (si ≥1 cycle) ou /calendar (si ≥2 cycles)
 */
export default function CycleCountdown() {
  const router = useRouter();
  const { predictNextPeriod, getAverages, cycles, getValidCycles } = useCycleHistoryStore();
  const prediction = predictNextPeriod();
  const averages = getAverages();
  const validCycles = getValidCycles();
  
  // Empty state si <2 cycles valides
  if (!averages || validCycles.length < 2) {
    const cyclesNeeded = Math.max(0, 2 - validCycles.length);
    
    return (
      <View style={styles.container}>
        <View style={styles.emptyStateCard}>
          <Text style={styles.emptyStateIcon}>📊</Text>
          <Text style={styles.emptyStateTitle}>
            Prédictions non disponibles
          </Text>
          <Text style={styles.emptyStateSubtitle}>
            Ajoute encore {cyclesNeeded} cycle(s) pour débloquer les prédictions (médiane)
          </Text>
          <TouchableOpacity
            style={styles.emptyStateCTA}
            onPress={() => {
              haptics.light();
              router.push('/my-cycles' as any);
            }}
            activeOpacity={0.8}
          >
            <Ionicons name="add-circle" size={20} color="#FFFFFF" />
            <Text style={styles.emptyStateCTAText}>Commencer un cycle</Text>
          </TouchableOpacity>
        </View>
      </View>
    );
  }
  
  if (!prediction) return null;
  
  const formatDate = (date: Date) => {
    return date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' });
  };
  
  const handlePress = () => {
    haptics.light();
    
    // Navigation intelligente
    if (averages && averages.validCount >= 2) {
      // ≥2 cycles valides → Calendrier
      Analytics.track('cycle_countdown_tapped', { destination: 'calendar', validCount: averages.validCount });
      router.push('/calendar' as any);
    } else if (cycles.length >= 1) {
      // ≥1 cycle → Mes cycles
      Analytics.track('cycle_countdown_tapped', { destination: 'my-cycles', validCount: cycles.length });
      router.push('/my-cycles' as any);
    }
  };
  
  return (
    <View style={styles.container}>
      <TouchableOpacity
        style={styles.countdownCard}
        onPress={handlePress}
        activeOpacity={0.8}
        hitSlop={hitSlopTokens.md}
        accessibilityRole="button"
        accessibilityLabel={`Compte à rebours: ${prediction.daysUntil} jours restants avant vos prochaines règles`}
        accessibilityHint="Toucher deux fois pour voir les détails de vos cycles"
      >
        <Text style={styles.countdownNumber}>{prediction.daysUntil}</Text>
        <Text style={styles.countdownLabel}>JOURS RESTANTS</Text>
        <Text style={styles.nextDate}>
          {formatDate(prediction.nextDate)} - Règles suivantes
        </Text>
        
        {/* Sous-texte indication */}
        {averages && (
          <Text style={styles.hint}>
            Basé sur {averages.method === 'median' ? 'la médiane' : 'la moyenne'} des {averages.validCount} derniers cycles
          </Text>
        )}
        
        {/* Warning si cycle irrégulier */}
        {prediction.needsVerification && (
          <View style={styles.warningBadge}>
            <Text style={styles.warningText}>⚠️ À vérifier</Text>
          </View>
        )}
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: space.lg,
    marginBottom: space.lg,
  },
  countdownCard: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.lg,
    padding: space.xl,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255, 107, 157, 0.3)',
    minHeight: 48, // A11y tappable area
  },
  countdownNumber: {
    fontSize: 64,
    fontWeight: '700',
    color: '#FF6B9D',
    marginBottom: space.xs,
  },
  countdownLabel: {
    ...typography.label,
    color: color.text,
    letterSpacing: 1.2,
    marginBottom: space.sm,
  },
  nextDate: {
    ...typography.bodySm,
    color: color.textMuted,
    marginBottom: space.xs,
  },
  hint: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
    marginTop: space.xs,
    fontStyle: 'italic',
  },
  warningBadge: {
    marginTop: space.sm,
    paddingHorizontal: space.md,
    paddingVertical: space.xs,
    backgroundColor: 'rgba(255, 193, 7, 0.15)',
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: 'rgba(255, 193, 7, 0.3)',
  },
  warningText: {
    ...typography.caption,
    color: '#FFC107',
    fontWeight: '600',
  },
  emptyStateCard: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.lg,
    padding: space.xl,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255, 107, 157, 0.2)',
  },
  emptyStateIcon: {
    fontSize: 48,
    marginBottom: space.md,
  },
  emptyStateTitle: {
    ...typography.h3,
    color: color.text,
    marginBottom: space.xs,
    textAlign: 'center',
  },
  emptyStateSubtitle: {
    ...typography.body,
    color: color.textMuted,
    textAlign: 'center',
    marginBottom: space.lg,
  },
  emptyStateCTA: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.xs,
    backgroundColor: '#FF6B9D',
    paddingHorizontal: space.lg,
    paddingVertical: space.md,
    borderRadius: radius.md,
    minHeight: 48,
  },
  emptyStateCTAText: {
    ...typography.h4,
    color: '#FFFFFF',
  },
});
