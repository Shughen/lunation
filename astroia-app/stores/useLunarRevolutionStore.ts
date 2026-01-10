/**
 * Store Zustand pour les révolutions lunaires
 * Gère le cache et le chargement des révolutions par mois
 */

import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { 
  getLunarRevolution, 
  getCachedRevolution,
  type LunarRevolution,
  type BirthData 
} from '@/lib/services/lunarRevolutionService';
import { useProfileStore } from './profileStore';
import { profileService } from '@/lib/api/profileService';

const STORAGE_KEY = '@luna_lunar_revolutions';

interface LunarRevolutionState {
  // État actuel
  currentMonthRevolution: LunarRevolution | null;
  historyByMonth: Record<string, LunarRevolution>; // clé: YYYY-MM
  status: 'idle' | 'loading' | 'loaded' | 'error';
  error: string | null;
  
  // Actions
  fetchForMonth: (date: Date, forceRefresh?: boolean) => Promise<void>;
  getForMonth: (date: Date) => LunarRevolution | null;
  loadFromStorage: () => Promise<void>;
  clearCache: () => Promise<void>;
}

/**
 * Convertit une Date en clé mois (YYYY-MM)
 */
function getMonthKey(date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  return `${year}-${month}`;
}

/**
 * Récupère les données de naissance depuis le store profil
 * Si les données manquent dans le store local, essaie de charger depuis Supabase
 */
async function getBirthDataFromProfile(): Promise<BirthData | null> {
  let profile = useProfileStore.getState().profile;
  
  // Si les données manquent dans le store local, essayer de charger depuis Supabase
  if (!profile.birthDate || !profile.birthTime || !profile.birthPlace) {
    console.log('[LunarRevolutionStore] ⚠️ Données manquantes dans store local, tentative chargement depuis Supabase...');
    try {
      const supabaseProfile = await profileService.loadProfileFromSupabase();
      if (supabaseProfile && supabaseProfile.birthDate && supabaseProfile.birthTime && supabaseProfile.birthPlace) {
        console.log('[LunarRevolutionStore] ✅ Profil chargé depuis Supabase');
        // Mettre à jour le store local pour les prochaines fois
        await useProfileStore.getState().saveProfile(supabaseProfile);
        profile = supabaseProfile;
      } else {
        console.log('[LunarRevolutionStore] ❌ Données manquantes également dans Supabase');
        return null;
      }
    } catch (error) {
      console.error('[LunarRevolutionStore] Erreur chargement depuis Supabase:', error);
      return null;
    }
  }
  
  if (!profile.birthDate || !profile.birthTime || !profile.birthPlace) {
    return null;
  }
  
  const birthDate = new Date(profile.birthDate);
  const birthTime = new Date(profile.birthTime);
  
  return {
    year: birthDate.getFullYear(),
    month: birthDate.getMonth() + 1,
    day: birthDate.getDate(),
    hour: birthTime.getHours(),
    minute: birthTime.getMinutes(),
    second: birthTime.getSeconds(),
    city: profile.birthPlace,
    country_code: 'FR', // TODO: récupérer depuis profil
    latitude: profile.latitude || 0,
    longitude: profile.longitude || 0,
    timezone: profile.timezone || 'Europe/Paris',
  };
}

export const useLunarRevolutionStore = create<LunarRevolutionState>((set, get) => ({
  currentMonthRevolution: null,
  historyByMonth: {},
  status: 'idle',
  error: null,

  /**
   * Charge la révolution lunaire pour un mois donné
   */
  fetchForMonth: async (date: Date, forceRefresh = false) => {
    const monthKey = getMonthKey(date);
    
    // Vérifier le cache si pas de force refresh
    if (!forceRefresh) {
      const cached = get().getForMonth(date);
      if (cached) {
        console.log('[LunarRevolutionStore] ✅ Récupéré depuis cache:', monthKey);
        return;
      }
    }

    // Vérifier que les données de naissance sont disponibles
    // (la fonction peut maintenant charger depuis Supabase si nécessaire)
    const birthData = await getBirthDataFromProfile();
    if (!birthData) {
      set({ 
        status: 'error', 
        error: 'Données de naissance manquantes. Configure ton profil pour accéder aux révolutions lunaires.' 
      });
      return;
    }

    set({ status: 'loading', error: null });

    try {
      // Normaliser la date au 1er du mois pour le calcul
      const targetMonth = new Date(date.getFullYear(), date.getMonth(), 1);
      
      const revolution = await getLunarRevolution(birthData, targetMonth, {
        force_refresh: forceRefresh,
      });

      // Mettre à jour le store
      const newHistory = { ...get().historyByMonth, [monthKey]: revolution };
      
      // Si c'est le mois actuel, mettre à jour currentMonthRevolution
      const currentMonthKey = getMonthKey(new Date());
      const isCurrentMonth = monthKey === currentMonthKey;
      
      set({
        currentMonthRevolution: isCurrentMonth ? revolution : get().currentMonthRevolution,
        historyByMonth: newHistory,
        status: 'loaded',
        error: null,
      });

      // Sauvegarder dans AsyncStorage
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(newHistory));
      
      console.log('[LunarRevolutionStore] ✅ Révolution chargée:', monthKey);
    } catch (error: any) {
      console.error('[LunarRevolutionStore] ❌ Erreur:', error);
      const errorMessage = error?.message || error?.toString() || 'Erreur lors du chargement de la révolution lunaire';
      set({ 
        status: 'error', 
        error: errorMessage
      });
    }
  },

  /**
   * Récupère la révolution pour un mois depuis le cache
   */
  getForMonth: (date: Date) => {
    const monthKey = getMonthKey(date);
    return get().historyByMonth[monthKey] || null;
  },

  /**
   * Charge les révolutions depuis AsyncStorage au démarrage
   */
  loadFromStorage: async () => {
    try {
      const data = await AsyncStorage.getItem(STORAGE_KEY);
      if (data) {
        const history = JSON.parse(data);
        const currentMonthKey = getMonthKey(new Date());
        
        set({
          historyByMonth: history,
          currentMonthRevolution: history[currentMonthKey] || null,
          status: history[currentMonthKey] ? 'loaded' : 'idle',
        });
        
        console.log('[LunarRevolutionStore] ✅ Historique chargé depuis storage:', Object.keys(history).length, 'mois');
      } else {
        console.log('[LunarRevolutionStore] Aucun cache trouvé');
      }
    } catch (error) {
      console.error('[LunarRevolutionStore] Erreur chargement storage:', error);
    }
  },

  /**
   * Vide le cache
   */
  clearCache: async () => {
    try {
      await AsyncStorage.removeItem(STORAGE_KEY);
      set({
        currentMonthRevolution: null,
        historyByMonth: {},
        status: 'idle',
        error: null,
      });
      console.log('[LunarRevolutionStore] 🗑️ Cache vidé');
    } catch (error) {
      console.error('[LunarRevolutionStore] Erreur clear cache:', error);
    }
  },
}));

