/**
 * Configuration des fonctionnalités par phase
 * Phase Bêta : Accès illimité à toutes les fonctionnalités
 */

export const BETA_CONFIG = {
  lunarReturns: {
    pastMonthsAccess: 'unlimited' as const,
    futureMonthsAccess: 'unlimited' as const,
    interpretationsAccess: 'full' as const,
  },
  journal: {
    historyLimit: null, // illimité
  },
  natalChart: {
    aspectsAccess: 'full' as const,
  },
};

// Pour la phase production (à activer plus tard)
export const PRODUCTION_CONFIG = {
  freeTier: {
    lunarReturns: {
      currentMonth: 'full' as const,
      nextMonth: 'preview' as const,
      futureMonths: 'locked' as const,
      pastMonths: 'last_one_only' as const,
    },
    journal: {
      historyDays: 7,
    },
  },
  premiumTier: {
    lunarReturns: {
      pastMonthsAccess: 'unlimited' as const,
      futureMonthsAccess: 'unlimited' as const,
      interpretationsAccess: 'full' as const,
    },
    journal: {
      historyLimit: null, // illimité
    },
  },
};

// Configuration active
export const CURRENT_CONFIG = BETA_CONFIG;

// Helper pour vérifier si on est en mode bêta
export const isBetaMode = (): boolean => {
  return CURRENT_CONFIG === BETA_CONFIG;
};

// Types pour TypeScript
export type AccessLevel = 'full' | 'preview' | 'locked' | 'unlimited' | 'last_one_only';

export interface FeatureConfig {
  lunarReturns: {
    pastMonthsAccess: AccessLevel;
    futureMonthsAccess: AccessLevel;
    interpretationsAccess: AccessLevel;
  };
  journal: {
    historyLimit: number | null;
  };
  natalChart: {
    aspectsAccess: AccessLevel;
  };
}
