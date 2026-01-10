import { Analytics } from '@/lib/analytics';

// Types
export interface CycleEntry {
  id: string;
  startDate: string; // ISO UTC
  endDate: string | null; // ISO UTC, null si en cours
  cycleLength: number | null; // Durée totale cycle (jusqu'aux prochaines règles)
  periodLength: number | null; // Durée des règles (endDate - startDate)
  createdAt: string; // ISO UTC
  updatedAt: string; // ISO UTC
}

export interface CycleAverages {
  avgPeriod: number;
  avgCycle: number;
  totalCycles: number;
  validCount: number;
  method: 'median' | 'mean';
}

// Bornes plausibles
const VALID_CYCLE_LENGTH_RANGE = [18, 40] as const; // Jours
const VALID_PERIOD_LENGTH_RANGE = [2, 8] as const; // Jours
const MIN_INTERVAL_HOURS = 24; // Minimum entre 2 cycles

/**
 * Vérifie si un cycle est valide selon les bornes plausibles
 */
export function isValidCycle(cycle: CycleEntry): boolean {
  // Cycle incomplet → invalide pour les calculs
  if (!cycle.endDate || !cycle.periodLength) return false;

  // Vérifier bornes periodLength
  const [minPeriod, maxPeriod] = VALID_PERIOD_LENGTH_RANGE;
  if (cycle.periodLength < minPeriod || cycle.periodLength > maxPeriod) {
    Analytics.track('cycle_outlier_ignored', { reason: 'period_length', value: cycle.periodLength });
    return false;
  }

  // Vérifier bornes cycleLength (si disponible)
  if (cycle.cycleLength) {
    const [minCycle, maxCycle] = VALID_CYCLE_LENGTH_RANGE;
    if (cycle.cycleLength < minCycle || cycle.cycleLength > maxCycle) {
      Analytics.track('cycle_outlier_ignored', { reason: 'cycle_length', value: cycle.cycleLength });
      return false;
    }
  }

  return true;
}

/**
 * Vérifie si un cycle a été créé trop rapidement après le précédent
 */
export function isTooCloseToPrevious(cycle: CycleEntry, previousCycle: CycleEntry | null): boolean {
  if (!previousCycle) return false;

  const currentCreated = new Date(cycle.createdAt).getTime();
  const prevCreated = new Date(previousCycle.createdAt).getTime();
  const hoursDiff = (currentCreated - prevCreated) / (1000 * 60 * 60);

  if (hoursDiff < MIN_INTERVAL_HOURS) {
    Analytics.track('cycle_outlier_ignored', { reason: 'too_close', hours: hoursDiff });
    return true;
  }

  return false;
}

/**
 * Calcule la médiane d'un tableau de nombres
 */
export function median(values: number[]): number {
  if (values.length === 0) return 0;

  const sorted = [...values].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);

  return sorted.length % 2 === 0
    ? Math.round((sorted[mid - 1] + sorted[mid]) / 2)
    : sorted[mid];
}

/**
 * Calcule la moyenne d'un tableau de nombres
 */
export function mean(values: number[]): number {
  if (values.length === 0) return 0;
  return Math.round(values.reduce((sum, v) => sum + v, 0) / values.length);
}

/**
 * Récupère les cycles valides d'une liste (filtrés selon bornes + intervalle)
 */
export function getValidCycles(cycles: CycleEntry[]): CycleEntry[] {
  const validCycles: CycleEntry[] = [];

  for (let i = 0; i < cycles.length; i++) {
    const cycle = cycles[i];
    const prevCycle = i > 0 ? cycles[i - 1] : null;

    // Filtrer cycles invalides
    if (!isValidCycle(cycle)) continue;
    if (isTooCloseToPrevious(cycle, prevCycle)) continue;

    validCycles.push(cycle);
  }

  return validCycles;
}

/**
 * Calcule les moyennes (médiane des 3 derniers cycles valides, ou moyenne si 2)
 */
export function calculateAverages(cycles: CycleEntry[]): CycleAverages | null {
  const validCycles = getValidCycles(cycles);

  // Besoin d'au moins 2 cycles valides
  if (validCycles.length < 2) {
    return null;
  }

  // Prendre les 3 derniers cycles pour la médiane
  const recentCycles = validCycles.slice(-3);

  // Durée des règles (médiane ou moyenne)
  const periodLengths = recentCycles.map(c => c.periodLength!).filter(Boolean);
  const avgPeriod = recentCycles.length >= 3
    ? median(periodLengths)
    : mean(periodLengths);

  // Durée cycle (médiane ou moyenne, uniquement sur cycles avec cycleLength)
  const cycleLengthsAll = validCycles.map(c => c.cycleLength).filter(Boolean) as number[];
  const recentCycleLengths = recentCycles.map(c => c.cycleLength).filter(Boolean) as number[];

  const avgCycle = recentCycleLengths.length >= 3
    ? median(recentCycleLengths)
    : recentCycleLengths.length >= 2
      ? mean(recentCycleLengths)
      : cycleLengthsAll.length > 0
        ? mean(cycleLengthsAll)
        : 28; // Fallback

  const method = recentCycles.length >= 3 ? 'median' : 'mean';

  // Analytics
  Analytics.track('cycle_average_recomputed', {
    validCount: validCycles.length,
    method,
    avgCycle,
    avgPeriod,
  });

  return {
    avgPeriod,
    avgCycle,
    totalCycles: validCycles.length,
    validCount: validCycles.length,
    method,
  };
}

/**
 * Calcule la régularité des cycles (écart-type des durées de cycle)
 */
export function calculateRegularity(cycles: CycleEntry[]): number {
  const validCycles = getValidCycles(cycles);
  const cycleLengths = validCycles.map(c => c.cycleLength).filter(Boolean) as number[];

  if (cycleLengths.length < 2) return 0;

  const avg = mean(cycleLengths);
  const variance = cycleLengths.reduce((sum, v) => sum + Math.pow(v - avg, 2), 0) / cycleLengths.length;

  return Math.sqrt(variance);
}

/**
 * Vérifie si les cycles sont réguliers (écart-type < 5 jours)
 */
export function isRegularCycle(cycles: CycleEntry[]): boolean {
  const regularity = calculateRegularity(cycles);
  return regularity < 5;
}

/**
 * Détecte si un cycle présente une irrégularité par rapport à la moyenne
 */
export function hasIrregularity(cycle: CycleEntry, cycles: CycleEntry[]): boolean {
  if (!cycle.cycleLength) return false;

  const averages = calculateAverages(cycles);
  if (!averages) return false;

  // Irrégularité si écart > 7 jours par rapport à la moyenne
  const deviation = Math.abs(cycle.cycleLength - averages.avgCycle);
  return deviation > 7;
}
