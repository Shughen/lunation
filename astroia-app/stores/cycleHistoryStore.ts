import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Analytics } from '@/lib/analytics';
import {
  isValidCycle,
  isTooCloseToPrevious,
  getValidCycles as getValidCyclesFromService,
  calculateAverages,
  median,
} from '@/lib/services/cycleValidationService';
import type { CycleEntry as CycleEntryFromService } from '@/lib/services/cycleValidationService';

const STORAGE_KEY = '@luna_cycle_history';
const MIGRATION_KEY = '@luna_cycle_migrated';

export interface CycleEntry {
  id: string;
  startDate: string; // ISO UTC
  endDate: string | null; // ISO UTC, null si en cours
  cycleLength: number | null; // Durée totale cycle (jusqu'aux prochaines règles)
  periodLength: number | null; // Durée des règles (endDate - startDate)
  createdAt: string; // ISO UTC
  updatedAt: string; // ISO UTC
}

interface CycleHistoryState {
  cycles: CycleEntry[];
  isLoading: boolean;
  
  // Actions
  loadCycles: () => Promise<void>;
  startPeriod: (date?: Date) => Promise<boolean>;
  endPeriod: (date?: Date) => Promise<boolean>;
  deleteCycle: (id: string) => Promise<boolean>;
  editCycle: (id: string, startDate: Date, endDate?: Date) => Promise<boolean>;
  getAverages: () => { avgPeriod: number; avgCycle: number; totalCycles: number; validCount: number; method: 'median' | 'mean' } | null;
  predictNextPeriod: () => { nextDate: Date; daysUntil: number; needsVerification?: boolean } | null;
  getCurrentCycle: () => CycleEntry | null;
  getValidCycles: () => CycleEntry[];
  getCurrentCycleData: () => {
    dayOfCycle: number;
    phase: string;
    phaseInfo: any;
    energy: string;
    fertile: boolean;
    isInPeriod: boolean;
  } | null;
  
  // Migration
  migrateFromSettings: (lastPeriodDate: Date, cycleLength: number) => Promise<void>;
}

export const useCycleHistoryStore = create<CycleHistoryState>((set, get) => ({
  cycles: [],
  isLoading: false,
  
  // Charger historique depuis AsyncStorage
  loadCycles: async () => {
    try {
      set({ isLoading: true });
      const stored = await AsyncStorage.getItem(STORAGE_KEY);
      
      if (stored) {
        const cycles: CycleEntry[] = JSON.parse(stored);
        set({ cycles, isLoading: false });
      } else {
        set({ isLoading: false });
      }
    } catch (error) {
      console.error('[CycleHistory] Load error:', error);
      set({ isLoading: false });
    }
  },
  
  // Démarrer une nouvelle période
  startPeriod: async (date = new Date()) => {
    try {
      const cycles = get().cycles;
      
      // Normaliser la date (minuit LOCAL)
      const normalizedDate = new Date(date);
      normalizedDate.setHours(0, 0, 0, 0);
      
      // Vérifier qu'il n'y a pas déjà un cycle en cours
      const currentCycle = cycles.find(c => !c.endDate);
      if (currentCycle) {
        console.warn('[CycleHistory] Un cycle est déjà en cours, impossible d\'en démarrer un nouveau');
        return false;
      }
      
      // Vérifier dates futures (comparaison à minuit)
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      
      if (normalizedDate > today) {
        console.warn('[CycleHistory] Impossible de démarrer un cycle dans le futur');
        return false;
      }
      
      const newCycle: CycleEntry = {
        id: `cycle_${Date.now()}`,
        startDate: normalizedDate.toISOString(),
        endDate: null,
        cycleLength: null,
        periodLength: null,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };
      
      // Si on a un cycle précédent, calculer sa durée totale
      if (cycles.length > 0) {
        const previousCycle = cycles[cycles.length - 1];
        const daysBetween = Math.round(
          (normalizedDate.getTime() - new Date(previousCycle.startDate).getTime()) / (1000 * 60 * 60 * 24)
        );
        previousCycle.cycleLength = daysBetween;
        previousCycle.updatedAt = new Date().toISOString();
      }
      
      const updatedCycles = [...cycles, newCycle];
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(updatedCycles));
      set({ cycles: updatedCycles });
      
      console.log('[CycleHistory] ✅ Nouveau cycle démarré:', newCycle.id);
      return true;
    } catch (error) {
      console.error('[CycleHistory] Start period error:', error);
      return false;
    }
  },
  
  // Terminer la période en cours
  endPeriod: async (date = new Date()) => {
    try {
      const cycles = get().cycles;
      const currentCycle = cycles.find(c => !c.endDate);
      
      if (!currentCycle) {
        console.warn('[CycleHistory] Aucun cycle en cours à terminer');
        return false;
      }
      
      // Normaliser les dates (minuit LOCAL)
      const normalizedDate = new Date(date);
      normalizedDate.setHours(0, 0, 0, 0);
      
      const startDate = new Date(currentCycle.startDate);
      startDate.setHours(0, 0, 0, 0);
      
      // Vérifier que endDate > startDate
      if (normalizedDate <= startDate) {
        console.warn('[CycleHistory] Date de fin doit être après date de début', {
          start: startDate.toISOString(),
          end: normalizedDate.toISOString(),
        });
        return false;
      }
      
      // Vérifier dates futures (comparaison à minuit)
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      
      if (normalizedDate > today) {
        console.warn('[CycleHistory] Impossible de terminer un cycle dans le futur', {
          date: normalizedDate.toISOString(),
          today: today.toISOString(),
        });
        return false;
      }
      
      // Calculer durée de la période
      const periodDays = Math.ceil(
        (normalizedDate.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24)
      );
      
      currentCycle.endDate = normalizedDate.toISOString();
      currentCycle.periodLength = periodDays;
      currentCycle.updatedAt = new Date().toISOString();
      
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(cycles));
      set({ cycles: [...cycles] }); // Force update
      
      console.log('[CycleHistory] ✅ Cycle terminé:', currentCycle.id, periodDays, 'jours');
      return true;
    } catch (error) {
      console.error('[CycleHistory] End period error:', error);
      return false;
    }
  },
  
  // Récupérer cycles valides (filtrés selon bornes + intervalle)
  getValidCycles: () => {
    const cycles = get().cycles;
    return getValidCyclesFromService(cycles);
  },
  
  // Calculer les moyennes (médiane des 3 derniers cycles valides, ou moyenne si 2)
  getAverages: () => {
    const cycles = get().cycles;
    return calculateAverages(cycles);
  },
  
  // Prédire prochaines règles (basé sur médiane)
  predictNextPeriod: () => {
    const cycles = get().cycles;
    const averages = get().getAverages();
    
    if (!averages || cycles.length === 0) {
      return null;
    }
    
    const lastCycle = cycles[cycles.length - 1];
    const lastStart = new Date(lastCycle.startDate);
    const today = new Date();
    
    // Calculer dayOfCycle actuel
    const daysSinceStart = Math.floor(
      (today.getTime() - lastStart.getTime()) / (1000 * 60 * 60 * 24)
    );
    const dayOfCycle = Math.max(1, daysSinceStart + 1);
    
    // Prédiction = dernier début + cycle médian
    const nextDate = new Date(lastStart);
    nextDate.setDate(nextDate.getDate() + averages.avgCycle);
    
    // Jours restants (clamp à [0, avgCycle])
    const daysUntilRaw = Math.ceil(
      (nextDate.getTime() - today.getTime()) / (1000 * 60 * 60 * 24)
    );
    
    // Si > avgCycle, c'est probablement un cycle irrégulier → remettre à 0
    const daysUntil = daysUntilRaw > averages.avgCycle
      ? 0
      : Math.max(0, daysUntilRaw);
    
    // Si daysUntil === 0 et dayOfCycle > avgCycle, marquer comme "à vérifier"
    const needsVerification = daysUntil === 0 && dayOfCycle > averages.avgCycle;
    
    return {
      nextDate,
      daysUntil,
      needsVerification,
    };
  },
  
  // Récupérer le cycle en cours (sans endDate)
  getCurrentCycle: () => {
    const cycles = get().cycles;
    return cycles.find(c => !c.endDate) || null;
  },
  
  // Calculer les données du cycle actuel pour affichage (Home, etc.)
  getCurrentCycleData: () => {
    const cycles = get().cycles;
    const averages = get().getAverages();
    
    if (cycles.length === 0) return null;
    
    const lastCycle = cycles[cycles.length - 1];
    const startDate = new Date(lastCycle.startDate);
    const today = new Date();
    
    // Calculer jour du cycle
    const daysSinceStart = Math.floor(
      (today.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24)
    );
    const dayOfCycle = Math.max(1, daysSinceStart + 1);
    
    // Déterminer si on est en période (cycle en cours sans endDate)
    const isInPeriod = !lastCycle.endDate;
    
    // Utiliser la médiane du cycle si disponible, sinon 28 par défaut
    const cycleLength = averages?.avgCycle || 28;
    
    // Calculer la phase
    let phase = 'Menstruelle';
    let phaseInfo = {
      name: 'Menstruelle',
      emoji: '🩸',
      color: '#FF6B9D',
      description: 'Période des règles',
    };
    
    // Si en période, forcer phase Menstruelle
    if (isInPeriod) {
      phase = 'Menstruelle';
      phaseInfo = {
        name: 'Menstruelle',
        emoji: '🩸',
        color: '#FF6B9D',
        description: 'Règles en cours',
      };
    } else {
      // Calculer phase selon dayOfCycle
      const menstrualEnd = lastCycle.periodLength || 5;
      const ovulationStart = Math.round(cycleLength * 0.43);
      const ovulationEnd = Math.round(cycleLength * 0.57);
      
      if (dayOfCycle <= menstrualEnd) {
        phase = 'Menstruelle';
        phaseInfo = {
          name: 'Menstruelle',
          emoji: '🩸',
          color: '#FF6B9D',
          description: 'Période des règles',
        };
      } else if (dayOfCycle <= ovulationStart) {
        phase = 'Folliculaire';
        phaseInfo = {
          name: 'Folliculaire',
          emoji: '🌱',
          color: '#30CF7B',
          description: 'Énergie montante',
        };
      } else if (dayOfCycle <= ovulationEnd) {
        phase = 'Ovulation';
        phaseInfo = {
          name: 'Ovulation',
          emoji: '🌕',
          color: '#FFD93D',
          description: 'Pic d\'énergie',
        };
      } else {
        phase = 'Lutéale';
        phaseInfo = {
          name: 'Lutéale',
          emoji: '🌙',
          color: '#A78BFA',
          description: 'Énergie descendante',
        };
      }
    }
    
    // Calculer énergie (simple mapping)
    let energy = 'Moyenne';
    if (phase === 'Ovulation') energy = 'Haute';
    else if (phase === 'Folliculaire') energy = 'Moyenne';
    else if (phase === 'Lutéale') energy = 'Basse';
    else energy = 'Basse'; // Menstruelle
    
    // Fertilité (Ovulation + Folliculaire tardive)
    const fertile = phase === 'Ovulation' || (phase === 'Folliculaire' && dayOfCycle > cycleLength * 0.35);
    
    return {
      dayOfCycle,
      phase,
      phaseInfo,
      energy,
      fertile,
      isInPeriod,
    };
  },
  
  // Supprimer un cycle
  deleteCycle: async (id: string) => {
    try {
      const cycles = get().cycles;
      const updatedCycles = cycles.filter(c => c.id !== id);
      
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(updatedCycles));
      set({ cycles: updatedCycles });
      
      // Analytics
      Analytics.track('cycle_history_deleted', { cycleId: id });
      
      // Recalculer les cycleLength après suppression
      for (let i = 0; i < updatedCycles.length - 1; i++) {
        const current = updatedCycles[i];
        const next = updatedCycles[i + 1];
        
        if (current.startDate && next.startDate) {
          const daysBetween = Math.round(
            (new Date(next.startDate).getTime() - new Date(current.startDate).getTime()) / (1000 * 60 * 60 * 24)
          );
          current.cycleLength = daysBetween;
          current.updatedAt = new Date().toISOString();
        }
      }
      
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(updatedCycles));
      set({ cycles: updatedCycles });
      
      console.log('[CycleHistory] ✅ Cycle supprimé:', id);
      return true;
    } catch (error) {
      console.error('[CycleHistory] Delete cycle error:', error);
      return false;
    }
  },
  
  // Éditer un cycle
  editCycle: async (id: string, startDate: Date, endDate?: Date) => {
    try {
      const cycles = get().cycles;
      const cycle = cycles.find(c => c.id === id);
      
      if (!cycle) {
        console.warn('[CycleHistory] Cycle non trouvé:', id);
        return false;
      }
      
      // Vérifier dates
      if (endDate && endDate <= startDate) {
        console.warn('[CycleHistory] Date de fin doit être après date de début');
        return false;
      }
      
      // Mettre à jour
      cycle.startDate = startDate.toISOString();
      cycle.endDate = endDate ? endDate.toISOString() : null;
      cycle.updatedAt = new Date().toISOString();
      
      // Recalculer periodLength
      if (endDate) {
        const periodDays = Math.ceil(
          (endDate.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24)
        );
        cycle.periodLength = periodDays;
      } else {
        cycle.periodLength = null;
      }
      
      // Recalculer cycleLength (impact sur cycle suivant)
      const cycleIndex = cycles.findIndex(c => c.id === id);
      if (cycleIndex >= 0 && cycleIndex < cycles.length - 1) {
        const nextCycle = cycles[cycleIndex + 1];
        const daysBetween = Math.round(
          (new Date(nextCycle.startDate).getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24)
        );
        cycle.cycleLength = daysBetween;
      }
      
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(cycles));
      set({ cycles: [...cycles] }); // Force update
      
      // Analytics
      Analytics.track('cycle_history_edited', { cycleId: id });
      
      console.log('[CycleHistory] ✅ Cycle édité:', id);
      return true;
    } catch (error) {
      console.error('[CycleHistory] Edit cycle error:', error);
      return false;
    }
  },
  
  // Migration depuis settings/cycle.js
  migrateFromSettings: async (lastPeriodDate: Date, cycleLength: number) => {
    try {
      // Vérifier si déjà migré
      const migrated = await AsyncStorage.getItem(MIGRATION_KEY);
      if (migrated) {
        console.log('[CycleHistory] Migration déjà effectuée, skip');
        return;
      }
      
      // Créer une entrée initiale avec estimation
      const estimatedPeriodLength = 5; // Valeur par défaut
      const endDate = new Date(lastPeriodDate);
      endDate.setDate(endDate.getDate() + estimatedPeriodLength);
      
      const initialCycle: CycleEntry = {
        id: `cycle_migration_${Date.now()}`,
        startDate: lastPeriodDate.toISOString(),
        endDate: endDate.toISOString(),
        periodLength: estimatedPeriodLength,
        cycleLength: cycleLength,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };
      
      const cycles = [initialCycle];
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(cycles));
      await AsyncStorage.setItem(MIGRATION_KEY, 'true');
      
      set({ cycles });
      
      console.log('[CycleHistory] ✅ Migration effectuée avec succès');
      console.log('[CycleHistory] Cycle initial créé:', initialCycle);
    } catch (error) {
      console.error('[CycleHistory] Migration error:', error);
    }
  },
}));

