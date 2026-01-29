/**
 * Hooks SWR pour les données du thème natal
 */

import useSWR from 'swr';
import { natalChart, isDevAuthBypassActive } from '../services/api';
import { useAuthStore } from '../stores/useAuthStore';

// Type correspondant à la vraie réponse de l'API /natal-chart
interface NatalChartAPIResponse {
  id: string;
  sun_sign: string;
  moon_sign: string;
  ascendant: string;
  planets: Record<string, { sign: string; degree?: number; house?: number }>;
  houses: Record<string, { sign: string; degree?: number }>;
  aspects: Array<{ planet1: string; planet2: string; type: string; orb: number }>;
}

// Configuration SWR par défaut
const swrConfig = {
  revalidateOnFocus: false,
  dedupingInterval: 60000,
  shouldRetryOnError: false,
};

/**
 * Hook pour récupérer le thème natal de l'utilisateur
 * Cache: 5 minutes (données stables)
 */
export function useNatalChart() {
  const { isAuthenticated } = useAuthStore();

  const shouldFetch = isAuthenticated || isDevAuthBypassActive();

  return useSWR<NatalChartAPIResponse | null>(
    shouldFetch ? 'natal-chart' : null,
    async () => {
      try {
        return await natalChart.get();
      } catch (error: any) {
        if (error.response?.status === 404) {
          return null;
        }
        if (__DEV__) {
          console.log('[useNatalChart] Thème natal non disponible:', error);
        }
        return null;
      }
    },
    {
      ...swrConfig,
      refreshInterval: 0,
      revalidateOnMount: true,
    }
  );
}

/**
 * Helper pour trouver une planète par nom
 * L'API retourne planets comme un objet { sun: {...}, moon: {...}, ... }
 */
export function findPlanetSign(planets: Record<string, { sign: string; degree?: number; house?: number }> | undefined | null, name: string): string | undefined {
  if (!planets || typeof planets !== 'object') return undefined;

  // Chercher la clé (insensible à la casse)
  const key = Object.keys(planets).find(k => k.toLowerCase() === name.toLowerCase());
  if (!key) return undefined;

  return planets[key]?.sign;
}
