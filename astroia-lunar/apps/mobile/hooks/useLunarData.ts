/**
 * Hooks SWR personnalisés pour les données lunaires
 *
 * Implémente un cache intelligent avec SWR pour:
 * - Révolution lunaire actuelle
 * - Statut Void of Course
 * - Transits majeurs
 *
 * Bénéfices:
 * - Déduplication automatique des requêtes
 * - Cache avec revalidation intelligente
 * - Stale-while-revalidate strategy
 * - Réduction des re-renders inutiles
 */

import useSWR from 'swr';
import { lunarReturns, transits, LunarReturn, isDevAuthBypassActive, getDevAuthHeader } from '../services/api';
import apiClient from '../services/api';
import { useAuthStore } from '../stores/useAuthStore';

// ===== Configuration SWR par défaut =====
const swrConfig = {
  revalidateOnFocus: false, // Ne pas revalider au focus (évite les requêtes inutiles)
  dedupingInterval: 60000, // Déduplication sur 1 minute
  shouldRetryOnError: false, // Pas de retry automatique (évite les logs d'erreur)
};

// ===== Types =====
interface VocWindow {
  start_at: string;
  end_at: string;
}

interface VocStatus {
  now: (VocWindow & { is_active: true }) | null;
  next: VocWindow | null;
  upcoming: VocWindow[];
}

interface AspectInfo {
  transit_planet: string;
  natal_planet: string;
  aspect: string;
  orb: number;
  interpretation?: string;
}

// ===== Hook: Révolution lunaire actuelle =====
/**
 * Hook pour récupérer la révolution lunaire en cours
 * Cache: 60 secondes (données peu changeantes)
 *
 * @returns { data, error, isLoading, mutate }
 */
export function useCurrentLunarReturn() {
  const { isAuthenticated } = useAuthStore();

  // Ne faire la requête que si authentifié ou en mode bypass
  const shouldFetch = isAuthenticated || isDevAuthBypassActive();

  return useSWR<LunarReturn | null>(
    shouldFetch ? 'lunar-return-current' : null,
    async () => {
      try {
        return await lunarReturns.getCurrent();
      } catch (error: any) {
        // Si 404, retourner null (pas de révolution lunaire en cours)
        if (error.response?.status === 404) {
          return null;
        }
        throw error;
      }
    },
    {
      ...swrConfig,
      refreshInterval: 0, // Pas de refresh automatique
      revalidateOnMount: true, // Revalider au mount
    }
  );
}

// ===== Hook: Statut Void of Course =====
/**
 * Hook pour récupérer le statut VoC
 * Cache: 5 minutes (peut changer fréquemment)
 * Auto-refresh: toutes les 5 minutes
 *
 * @returns { data, error, isLoading, mutate }
 */
export function useVocStatus() {
  const { isAuthenticated } = useAuthStore();

  // Ne faire la requête que si authentifié ou en mode bypass
  const shouldFetch = isAuthenticated || isDevAuthBypassActive();

  return useSWR<VocStatus | null>(
    shouldFetch ? 'voc-status' : null,
    async () => {
      try {
        const response = await apiClient.get('/api/lunar/voc/status');
        return response.data;
      } catch (error) {
        // Log uniquement en dev, ne pas exposer l'erreur technique
        if (__DEV__) {
          console.log('[useVocStatus] VoC non disponible:', error);
        }
        return null;
      }
    },
    {
      ...swrConfig,
      refreshInterval: 5 * 60 * 1000, // Refresh toutes les 5 minutes
      revalidateOnMount: true,
    }
  );
}

// ===== Hook: Transits majeurs =====
/**
 * Hook pour récupérer les transits majeurs du mois
 * Cache: 60 secondes (données stables sur un mois)
 *
 * @returns { data, error, isLoading, mutate }
 */
export function useMajorTransits() {
  const { user, isAuthenticated } = useAuthStore();

  // Déterminer l'userId
  let userId: string | null = null;
  if (isDevAuthBypassActive()) {
    const devHeader = getDevAuthHeader();
    userId = devHeader.value || 'dev-user-id';
  } else if (user?.id) {
    userId = typeof user.id === 'string' ? user.id : String(user.id);
  }

  // Construire le mois au format YYYY-MM
  const now = new Date();
  const month = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;

  // Ne faire la requête que si on a un userId
  const shouldFetch = (isAuthenticated || isDevAuthBypassActive()) && userId;

  return useSWR<AspectInfo[]>(
    shouldFetch ? `transits-major-${userId}-${month}` : null,
    async () => {
      try {
        const response = await transits.getOverview(userId!, month, true);

        if (response) {
          const overviewData = response?.overview || response?.summary;
          const insights = overviewData?.insights || {};
          const allAspects = insights?.major_aspects || [];

          // Garder uniquement les 3 aspects les plus serrés
          return [...allAspects]
            .sort((a, b) => Math.abs(a.orb) - Math.abs(b.orb))
            .slice(0, 3);
        }

        return [];
      } catch (error) {
        // Log uniquement en dev, ne pas exposer l'erreur technique à l'utilisateur
        if (__DEV__) {
          console.log('[useMajorTransits] Transits non disponibles:', error);
        }
        // Retourner tableau vide au lieu de relancer l'erreur
        return [];
      }
    },
    {
      ...swrConfig,
      refreshInterval: 0, // Pas de refresh automatique
      revalidateOnMount: true,
    }
  );
}
