import AsyncStorage from '@react-native-async-storage/async-storage';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { trackEvents } from '@/lib/analytics';

/**
 * Migration douce depuis settings/cycle.js vers cycleHistoryStore
 * 
 * À appeler au démarrage de l'app (app/_layout.tsx ou home)
 */
export async function migrateCycleDataIfNeeded() {
  try {
    // Vérifier si déjà migré
    const migrated = await AsyncStorage.getItem('@luna_cycle_migrated');
    if (migrated) {
      console.log('[CycleMigration] Déjà migré, skip');
      return;
    }
    
    // Lire ancienne config
    const oldConfig = await AsyncStorage.getItem('cycle_config');
    if (!oldConfig) {
      console.log('[CycleMigration] Pas de config existante, skip migration');
      await AsyncStorage.setItem('@luna_cycle_migrated', 'true');
      trackEvents.cycleMigrationSkipped?.('no_config');
      return;
    }
    
    const { lastPeriodDate, cycleLength } = JSON.parse(oldConfig);
    
    if (!lastPeriodDate) {
      console.log('[CycleMigration] Pas de lastPeriodDate, skip migration');
      await AsyncStorage.setItem('@luna_cycle_migrated', 'true');
      trackEvents.cycleMigrationSkipped?.('invalid_data');
      return;
    }
    
    // Migrer vers nouveau store
    const date = new Date(lastPeriodDate);
    const length = cycleLength || 28;
    
    console.log('[CycleMigration] Migration en cours...', {
      lastPeriodDate: date,
      cycleLength: length,
    });
    
    await useCycleHistoryStore.getState().migrateFromSettings(date, length);
    
    console.log('[CycleMigration] ✅ Migration terminée avec succès');
  } catch (error) {
    console.error('[CycleMigration] Erreur lors de la migration:', error);
  }
}

