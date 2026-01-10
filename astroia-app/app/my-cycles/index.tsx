import React, { useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Alert } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import CycleStats from '@/components/CycleStats';
import CycleHistoryBar from '@/components/CycleHistoryBar';
import { Empty } from '@/components/ui';
import haptics from '@/utils/haptics';
import { Analytics } from '@/lib/analytics';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { color, space, radius, type as typography, hitSlop as hitSlopTokens } from '@/theme/tokens';

export default function MyCyclesScreen() {
  const { cycles, loadCycles, isLoading, getValidCycles } = useCycleHistoryStore();
  const validCycles = getValidCycles(); // Filtrer cycles invalides
  
  useEffect(() => {
    loadCycles();
    
    // Analytics : nombre de cycles masqués
    const hiddenCount = cycles.length - validCycles.length;
    if (hiddenCount > 0) {
      console.log(`[MyCycles] ${hiddenCount} cycle(s) invalide(s) masqué(s)`);
      Analytics.track('ui_history_invalid_hidden', { count: hiddenCount });
    }
  }, [cycles.length]);
  
  // RESET STORAGE (TEMPORAIRE - DEBUG)
  const handleResetStorage = () => {
    Alert.alert(
      '🔄 Reset complet',
      'Supprimer TOUS les cycles et repartir de zéro ?\n\n⚠️ Action irréversible !',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Reset',
          style: 'destructive',
          onPress: async () => {
            haptics.warning();
            
            try {
              await AsyncStorage.multiRemove([
                '@luna_cycle_history',
                '@luna_cycle_migrated',
                'cycle_config',
              ]);
              
              // Recharger le store
              await loadCycles();
              
              haptics.success();
              Alert.alert('✅ Reset effectué', 'Le storage a été nettoyé. Redémarre l\'app pour effet complet.');
            } catch (error) {
              haptics.error();
              Alert.alert('❌ Erreur', 'Impossible de reset le storage.');
            }
          },
        },
      ]
    );
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
        
        <Text style={styles.headerTitle}>📊 Mes cycles</Text>
        
        <View style={{ width: 40 }} />
      </View>
      
      <ScrollView
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {isLoading ? (
          <View style={styles.loadingContainer}>
            <Text style={styles.loadingText}>Chargement...</Text>
          </View>
        ) : cycles.length === 0 ? (
          <Empty
            icon="calendar-outline"
            title="Aucun cycle complet pour le moment"
            subtitle="Enregistre au moins deux cycles pour afficher les moyennes."
            actionLabel="Retour à l'accueil"
            onActionPress={() => router.back()}
          />
        ) : (
          <>
            {/* Stats moyennes - Visible uniquement si ≥2 cycles */}
            <CycleStats />
            
            {/* Historique - N'afficher que les cycles valides */}
            <View style={styles.historySection}>
              <Text style={styles.sectionTitle}>📅 Historique</Text>
              
              {validCycles.length > 0 ? (
                validCycles
                  .slice()
                  .reverse() // Plus récent en premier
                  .map((cycle) => (
                    <CycleHistoryBar
                      key={cycle.id}
                      cycle={cycle}
                    />
                  ))
              ) : (
                <Text style={styles.emptyHistoryText}>
                  Aucun cycle valide à afficher (période: 2-8j, cycle: 18-40j)
                </Text>
              )}
              
              {/* Info cycles masqués */}
              {validCycles.length < cycles.length && (
                <>
                  <Text style={styles.hiddenCyclesHint}>
                    {cycles.length - validCycles.length} cycle(s) invalide(s) masqué(s)
                  </Text>
                  
                  {/* Bouton Reset (TEMPORAIRE DEBUG) */}
                  <TouchableOpacity
                    style={styles.resetButton}
                    onPress={handleResetStorage}
                  >
                    <Ionicons name="trash-outline" size={16} color="#FF3B30" />
                    <Text style={styles.resetButtonText}>
                      Reset complet (debug)
                    </Text>
                  </TouchableOpacity>
                </>
              )}
            </View>
            
            {/* Info */}
            <View style={styles.infoCard}>
              <Ionicons name="information-circle-outline" size={16} color={color.brand} />
              <Text style={styles.infoText}>
                Les moyennes sont calculées après 2 cycles complets minimum.
              </Text>
            </View>
            
            {/* Disclaimer */}
            <View style={styles.disclaimerCard}>
              <Text style={styles.disclaimerText}>
                Données stockées sur votre appareil. Outil de bien-être, non médical.
              </Text>
            </View>
          </>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: color.bg,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: space.lg,
    paddingVertical: space.md,
    borderBottomWidth: 1,
    borderBottomColor: color.border,
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
    padding: space.lg,
    paddingBottom: space['3xl'],
  },
  loadingContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: space['4xl'],
  },
  loadingText: {
    ...typography.bodySm,
    color: color.textMuted,
  },
  historySection: {
    marginTop: space.lg,
  },
  sectionTitle: {
    ...typography.h3,
    color: color.text,
    marginBottom: space.md,
  },
  infoCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: space.xs,
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.md,
    padding: space.md,
    marginTop: space.xl,
  },
  infoText: {
    ...typography.caption,
    color: color.textMuted,
    flex: 1,
    lineHeight: 18,
  },
  disclaimerCard: {
    marginTop: space.xl,
    paddingVertical: space.md,
    borderTopWidth: 1,
    borderTopColor: color.border,
  },
  disclaimerText: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
    fontStyle: 'italic',
  },
  emptyHistoryText: {
    ...typography.body,
    color: color.textMuted,
    textAlign: 'center',
    marginTop: space.lg,
    fontStyle: 'italic',
  },
  hiddenCyclesHint: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
    marginTop: space.md,
    fontStyle: 'italic',
  },
  resetButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: space.xs,
    marginTop: space.md,
    paddingVertical: space.sm,
    paddingHorizontal: space.md,
    backgroundColor: 'rgba(255, 59, 48, 0.1)',
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: 'rgba(255, 59, 48, 0.3)',
    alignSelf: 'center',
  },
  resetButtonText: {
    ...typography.caption,
    color: '#FF3B30',
    fontWeight: '600',
  },
});

