/**
 * Service de compatibilité intelligente basée sur la Lune
 * 
 * Ce service prépare l'architecture pour des compatibilités futures qui intègrent :
 * - La révolution lunaire actuelle (maison activée, signe)
 * - Les maisons relationnelles (Maison 5, Maison 7, etc.)
 * - Les thèmes natals des personnes
 * 
 * TODO: Implémentation future
 * L'idée sera de relier :
 * - la révolution lunaire actuelle (maison activée, signe),
 * - les maisons / planètes relationnelles (ex : Maison 5, Maison 7…),
 * - les thèmes des autres personnes.
 */

import type { LunarRevolution } from './lunarRevolutionService';

/**
 * Contexte lunaire pour la compatibilité intelligente
 * Représente la révolution lunaire actuelle qui influence les relations
 */
export type LunarCompatibilityContext = {
  month: string; // Format YYYY-MM
  lunarSign: string; // Nom du signe en français
  house: number; // Maison activée (1-12)
  phase: 'new' | 'waxing' | 'full' | 'waning';
  phaseName: string; // Nom de la phase en français
};

/**
 * Données du thème natal simplifiées pour la compatibilité
 */
export type NatalChart = {
  sunSign: number; // ID du signe (1-12)
  moonSign: number;
  ascendant: number;
  // TODO: Ajouter d'autres planètes si nécessaire
};

/**
 * Résumé de compatibilité avec contexte lunaire
 */
export type CompatibilitySummary = {
  globalScore: number; // Score global (0-100)
  lunarInfluence: {
    houseActivated: number;
    impact: 'positive' | 'neutral' | 'challenging';
    description: string;
  };
  detailedScores: {
    communication: number;
    passion: number;
    complicity: number;
    goals: number;
  };
  lunarAdvice?: string[]; // Conseils basés sur la révolution lunaire
};

/**
 * Calcule un résumé de compatibilité basique avec contexte lunaire optionnel
 * 
 * @param userNatalChart - Thème natal de l'utilisateur
 * @param partnerNatalChart - Thème natal du partenaire
 * @param lunarContext - Contexte lunaire actuel (optionnel)
 * @returns Résumé de compatibilité
 * 
 * TODO: Implémenter la logique astrologique complète
 * - Analyser l'influence de la maison activée sur la relation
 * - Prendre en compte les maisons relationnelles (5, 7, 11)
 * - Intégrer la phase lunaire dans l'analyse
 */
export function getBasicCompatibilitySummary(
  userNatalChart: NatalChart,
  partnerNatalChart: NatalChart,
  lunarContext?: LunarCompatibilityContext
): CompatibilitySummary {
  // TODO: Implémenter la logique complète
  // Pour l'instant, retourner un résumé basique
  
  const globalScore = 75; // Placeholder
  
  const summary: CompatibilitySummary = {
    globalScore,
    lunarInfluence: lunarContext ? {
      houseActivated: lunarContext.house,
      impact: 'neutral',
      description: `La Lune en ${lunarContext.lunarSign} active la Maison ${lunarContext.house}.`,
    } : {
      houseActivated: 0,
      impact: 'neutral',
      description: 'Aucun contexte lunaire disponible.',
    },
    detailedScores: {
      communication: 75,
      passion: 75,
      complicity: 75,
      goals: 75,
    },
  };
  
  return summary;
}

/**
 * Convertit une LunarRevolution en LunarCompatibilityContext
 * 
 * @param revolution - Révolution lunaire
 * @returns Contexte de compatibilité lunaire
 */
export function revolutionToCompatibilityContext(
  revolution: LunarRevolution
): LunarCompatibilityContext {
  return {
    month: revolution.month,
    lunarSign: revolution.moonSign,
    house: revolution.house,
    phase: revolution.phase,
    phaseName: revolution.phaseName,
  };
}

/**
 * Détermine l'impact lunaire sur une relation selon la maison activée
 * 
 * @param house - Maison activée (1-12)
 * @param relationType - Type de relation ('couple' | 'friends' | 'colleagues')
 * @returns Impact et description
 * 
 * TODO: Implémenter la logique complète selon les maisons astrologiques
 * - Maison 1 (Identité) : Impact sur l'image de soi dans la relation
 * - Maison 5 (Créativité, Amour) : Impact sur la passion et la créativité partagée
 * - Maison 7 (Partenariats) : Impact direct sur les relations
 * - Maison 11 (Amitiés, Projets) : Impact sur les amitiés et projets communs
 */
export function getLunarHouseImpact(
  house: number,
  relationType: 'couple' | 'friends' | 'colleagues'
): { impact: 'positive' | 'neutral' | 'challenging'; description: string } {
  // TODO: Implémenter la logique complète
  
  const houseMeanings: Record<number, string> = {
    1: 'identité et image de soi',
    2: 'valeurs et ressources',
    3: 'communication et apprentissage',
    4: 'foyer et famille',
    5: 'créativité et plaisir',
    6: 'santé et routine',
    7: 'relations et partenariats',
    8: 'transformation et partage',
    9: 'sagesse et exploration',
    10: 'carrière et responsabilités',
    11: 'amitié et projets',
    12: 'introspection et spiritualité',
  };
  
  const meaning = houseMeanings[house] || 'développement personnel';
  
  return {
    impact: 'neutral',
    description: `La Maison ${house} (${meaning}) est activée cette période.`,
  };
}

