import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Platform, ToastAndroid, Alert, ActivityIndicator } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { trackEvents } from '@/lib/analytics';
import haptics from '@/utils/haptics';
import { color, space, radius, type as typography, shadow } from '@/theme/tokens';

/**
 * QuickPeriodLog - Suivi rapide début/fin des règles
 * Affiche "Début" si aucun cycle en cours, "Fin" si cycle en cours
 */
export default function QuickPeriodLog() {
  const { getCurrentCycle, startPeriod, endPeriod } = useCycleHistoryStore();
  const [isSaving, setIsSaving] = useState(false);
  
  const currentCycle = getCurrentCycle();
  const isInPeriod = !!currentCycle;
  
  const showToast = (message: string) => {
    if (Platform.OS === 'android') {
      ToastAndroid.show(message, ToastAndroid.SHORT);
    } else {
      // iOS: Alert simple ou on pourrait utiliser une lib toast
      Alert.alert('', message, [{ text: 'OK' }]);
    }
  };
  
  const handleStartPeriod = async () => {
    if (isSaving) return; // Lock pour éviter double-tap
    
    // Vérifier qu'il n'y a pas déjà un cycle en cours
    if (getCurrentCycle()) {
      haptics.warning();
      showToast('⚠️ Un cycle est en cours, termine-le d\'abord.');
      return;
    }
    
    setIsSaving(true);
    haptics.medium();
    
    const lockStart = Date.now();
    const success = await startPeriod();
    const lockDuration = Date.now() - lockStart;
    
    if (success) {
      haptics.success();
      showToast('✅ Règles logées ! Pense à marquer la fin.');
      
      // Analytics
      const { cycles } = useCycleHistoryStore.getState();
      trackEvents.cycleStartLogged(cycles.length);
    } else {
      haptics.error();
      showToast('❌ Erreur : Impossible de démarrer le cycle.');
    }
    
    // Analytics lock duration
    if (lockDuration > 100) {
      trackEvents.cycleButtonDisabledMs?.(lockDuration);
    }
    
    setIsSaving(false);
  };
  
  const handleEndPeriod = async () => {
    if (isSaving) return; // Lock pour éviter double-tap
    
    // Vérifier qu'il y a bien un cycle en cours
    if (!getCurrentCycle()) {
      haptics.warning();
      showToast('⚠️ Aucun cycle en cours à terminer.');
      return;
    }
    
    setIsSaving(true);
    haptics.medium();
    
    const lockStart = Date.now();
    const success = await endPeriod();
    const lockDuration = Date.now() - lockStart;
    
    if (success) {
      haptics.success();
      showToast('✅ Règles terminées ! Cycle enregistré.');
      
      // Analytics
      const { cycles } = useCycleHistoryStore.getState();
      const lastCycle = cycles[cycles.length - 1];
      trackEvents.cycleEndLogged(lastCycle?.periodLength || 0, cycles.length);
    } else {
      haptics.error();
      showToast('❌ Erreur : Impossible de terminer le cycle.');
    }
    
    // Analytics lock duration
    if (lockDuration > 100) {
      trackEvents.cycleButtonDisabledMs?.(lockDuration);
    }
    
    setIsSaving(false);
  };
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>📅 Suivi rapide</Text>
      
      <View style={styles.buttonsRow}>
        {!isInPeriod ? (
          <TouchableOpacity
            style={[styles.button, styles.buttonStart, isSaving && styles.buttonDisabled]}
            onPress={handleStartPeriod}
            disabled={isSaving}
            activeOpacity={0.8}
            accessibilityRole="button"
            accessibilityLabel="Début des règles"
            accessibilityHint="Enregistrer le premier jour de vos règles"
          >
            {isSaving ? (
              <ActivityIndicator size="small" color="white" />
            ) : (
              <>
                <Ionicons name="play" size={20} color="white" />
                <Text style={styles.buttonText}>🩸 Début des règles</Text>
              </>
            )}
          </TouchableOpacity>
        ) : (
          <TouchableOpacity
            style={[styles.button, styles.buttonEnd, isSaving && styles.buttonDisabled]}
            onPress={handleEndPeriod}
            disabled={isSaving}
            activeOpacity={0.8}
            accessibilityRole="button"
            accessibilityLabel="Fin des règles"
            accessibilityHint="Enregistrer le dernier jour de vos règles"
          >
            {isSaving ? (
              <ActivityIndicator size="small" color="white" />
            ) : (
              <>
                <Ionicons name="stop" size={20} color="white" />
                <Text style={styles.buttonText}>🔵 Fin des règles</Text>
              </>
            )}
          </TouchableOpacity>
        )}
      </View>
      
      {isInPeriod && (
        <Text style={styles.hint}>
          En cours depuis {Math.ceil(
            (new Date().getTime() - new Date(currentCycle.startDate).getTime()) / (1000 * 60 * 60 * 24)
          )} jour(s)
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: space.lg,
    marginTop: space.md + 8, // +8px pour aérer avec CycleCard au-dessus
    marginBottom: space.lg,
  },
  title: {
    ...typography.label,
    color: color.textMuted,
    marginBottom: space.sm,
  },
  buttonsRow: {
    flexDirection: 'row',
    gap: space.sm,
  },
  button: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: space.xs,
    paddingVertical: space.md,
    borderRadius: radius.md,
    minHeight: 48, // Zone tactile ≥ 44px
    ...shadow.sm,
  },
  buttonStart: {
    backgroundColor: '#FF6B9D',
  },
  buttonEnd: {
    backgroundColor: '#4DA3FF',
  },
  buttonDisabled: {
    opacity: 0.5,
  },
  buttonText: {
    ...typography.h4,
    color: '#FFFFFF', // Blanc pur pour meilleur contraste sur rose clair
  },
  hint: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
    marginTop: space.xs,
  },
});

