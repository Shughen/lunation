/**
 * Catégorisation et tri astrologique professionnel des aspects
 * Hiérarchie : Aspects majeurs tendus > Aspects majeurs harmonieux > Aspects mineurs
 */

// Points du Big Three (pour bonus)
export const BIG_THREE_POINTS = new Set(['Sun', 'Moon', 'Ascendant', 'Medium_Coeli']);

// Planètes personnelles
export const PERSONAL_PLANETS = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Ascendant', 'Medium_Coeli'];

// Planètes sociales
export const SOCIAL_PLANETS = ['Jupiter', 'Saturn'];

/**
 * Ordre strict des types d'aspects selon la hiérarchie astrologique professionnelle
 * Plus le rang est petit, plus l'aspect est prioritaire
 * Utilisé pour le tri strict : l'ordre est FIXE et ne peut jamais être inversé par le score
 */
export const ORDERED_ASPECT_TYPES = [
  'conjunction',    // 1
  'opposition',     // 2
  'square',         // 3
  'trine',          // 4
  'sextile',        // 5
  'quintile',       // 6
  'semi-sextile',   // 7
  'semi-square',    // 8
  'quincunx',       // 9
  // 'other' = catch-all (tous les autres types)
] as const;

/**
 * Dictionnaire de priorité des types d'aspects
 * Généré automatiquement à partir de ORDERED_ASPECT_TYPES
 * Utilisé pour obtenir rapidement le rang d'un type d'aspect
 */
export const ASPECT_TYPE_PRIORITY: Record<string, number> = ORDERED_ASPECT_TYPES.reduce((acc, type, index) => {
  acc[type] = index + 1;
  return acc;
}, {} as Record<string, number>);

// Ajouter 'other' avec le rang le plus élevé (10)
ASPECT_TYPE_PRIORITY['other'] = 10;

/**
 * Poids des types d'aspects selon la hiérarchie astrologique (conservé pour compatibilité)
 * @deprecated Utiliser ASPECT_TYPE_PRIORITY et getAspectTypeRank() pour le tri strict
 */
export const ASPECT_TYPE_WEIGHT = {
  conjunction: 3000,   // Conjonction = priorité maximale
  opposition: 2900,    // Opposition = très importante
  square: 2800,        // Carré = très important
  trine: 2000,         // Trigone = harmonieux majeur
  sextile: 1900,       // Sextile = harmonieux majeur
  // Tout le reste (quintile, semi-sextile, etc.) = minor
  minor: 1000,
} as const;

/**
 * Poids de l'intensité des aspects
 */
export const INTENSITY_WEIGHT = {
  strong: 300,   // Fort = prioritaire
  medium: 200,   // Moyen
  weak: 100,     // Faible
} as const;

/**
 * Vérifie si un aspect est de type "majeur tendu"
 */
export function isMajorTense(aspectType: string): boolean {
  if (!aspectType) return false;
  const normalized = aspectType.toLowerCase();
  return normalized === 'conjunction' || 
         normalized === 'opposition' || 
         normalized === 'square';
}

/**
 * Vérifie si un aspect est de type "majeur harmonieux"
 */
export function isMajorHarmonious(aspectType: string): boolean {
  if (!aspectType) return false;
  const normalized = aspectType.toLowerCase();
  return normalized === 'trine' || normalized === 'sextile';
}

/**
 * Vérifie si un aspect est de type "mineur"
 */
export function isMinor(aspectType: string): boolean {
  if (!aspectType) return true; // Par défaut, tout ce qui n'est pas majeur est mineur
  return !isMajorTense(aspectType) && !isMajorHarmonious(aspectType);
}

/**
 * Vérifie si un aspect implique au moins une planète personnelle ou un angle
 */
export function isPersonalRelated(aspect: { from: string; to: string }): boolean {
  if (!aspect || !aspect.from || !aspect.to) {
    return false;
  }
  return PERSONAL_PLANETS.includes(aspect.from) || PERSONAL_PLANETS.includes(aspect.to);
}

/**
 * Retourne le poids du type d'aspect
 */
export function getAspectTypeWeight(aspectType: string): number {
  if (!aspectType) return ASPECT_TYPE_WEIGHT.minor;
  
  const normalized = aspectType.toLowerCase();
  
  // Vérifier les types majeurs
  if (normalized === 'conjunction') return ASPECT_TYPE_WEIGHT.conjunction;
  if (normalized === 'opposition') return ASPECT_TYPE_WEIGHT.opposition;
  if (normalized === 'square') return ASPECT_TYPE_WEIGHT.square;
  if (normalized === 'trine') return ASPECT_TYPE_WEIGHT.trine;
  if (normalized === 'sextile') return ASPECT_TYPE_WEIGHT.sextile;
  
  // Tout le reste est mineur
  return ASPECT_TYPE_WEIGHT.minor;
}

/**
 * Retourne le poids de l'intensité
 */
export function getIntensityWeight(strength: string): number {
  if (!strength) return INTENSITY_WEIGHT.weak;
  
  const normalized = strength.toLowerCase();
  return INTENSITY_WEIGHT[normalized as keyof typeof INTENSITY_WEIGHT] || INTENSITY_WEIGHT.weak;
}

/**
 * Retourne le rang de l'intensité (pour tri)
 * Utilisé pour établir la hiérarchie : Fort > Moyen > Faible
 * 
 * @param intensity - Intensité de l'aspect ('strong', 'medium', 'weak')
 * @returns Rang de l'intensité : 3 (strong), 2 (medium), 1 (weak par défaut)
 */
export function getIntensityRank(intensity?: string | null): number {
  if (!intensity) return 1;
  
  const val = intensity.toLowerCase();
  
  if (val === 'strong') return 3;
  if (val === 'medium') return 2;
  
  return 1; // weak par défaut
}

/**
 * Retourne le rang du type d'aspect selon l'ordre strict astrologique
 * Utilisé pour le tri strict : un aspect de rang inférieur passe toujours avant
 * 
 * @param aspectType - Type d'aspect (conjunction, opposition, etc.)
 * @returns Rang du type d'aspect (1 pour conjunction, 2 pour opposition, etc., 10 pour autres)
 */
export function getAspectTypeRank(aspectType?: string | null): number {
  if (!aspectType) return ASPECT_TYPE_PRIORITY['other'];
  
  const key = aspectType.toLowerCase();
  
  // Vérifier d'abord dans le dictionnaire de priorité principal
  if (key in ASPECT_TYPE_PRIORITY) {
    return ASPECT_TYPE_PRIORITY[key];
  }
  
  // Gérer les variantes avec tirets ou synonymes
  const normalizedVariants: Record<string, number> = {
    'semisextile': ASPECT_TYPE_PRIORITY['semi-sextile'],
    'semisquare': ASPECT_TYPE_PRIORITY['semi-square'],
    'sesquiquadrate': ASPECT_TYPE_PRIORITY['semi-square'], // Variante de semi-square
    'sesquiquadrant': ASPECT_TYPE_PRIORITY['semi-square'],
    'inconjunct': ASPECT_TYPE_PRIORITY['quincunx'], // Synonyme de quincunx
    'biquintile': ASPECT_TYPE_PRIORITY['quintile'], // Variante de quintile
  };
  
  if (key in normalizedVariants) {
    return normalizedVariants[key];
  }
  
  // Tous les autres types = other (10)
  return ASPECT_TYPE_PRIORITY['other'];
}

/**
 * Calcule le score de base d'un aspect (combinaison de planètes + orbe + bonus Big Three)
 * C'est le score fin sans le type d'aspect et l'intensité (qui sont dans les poids)
 */
function calculateBaseAspectScore(aspect: {
  from: string;
  to: string;
  orb: number;
}): number {
  const { from, to, orb } = aspect;
  
  // Bonus selon la combinaison de planètes
  let planetBonus = 0;
  const fromCategory = PERSONAL_PLANETS.includes(from) ? 'personal' :
                       SOCIAL_PLANETS.includes(from) ? 'social' : 'outer';
  const toCategory = PERSONAL_PLANETS.includes(to) ? 'personal' :
                     SOCIAL_PLANETS.includes(to) ? 'social' : 'outer';
  
  if (fromCategory === 'personal' && toCategory === 'personal') {
    planetBonus = 30;
  } else if ((fromCategory === 'personal' && toCategory === 'social') || 
             (fromCategory === 'social' && toCategory === 'personal')) {
    planetBonus = 20;
  } else if ((fromCategory === 'personal' && toCategory === 'outer') || 
             (fromCategory === 'outer' && toCategory === 'personal')) {
    planetBonus = 10;
  }
  
  // Bonus d'orbe (plus petit = mieux, max 10 points)
  const orbAbs = Math.abs(orb);
  const cappedOrb = Math.min(10, orbAbs);
  const orbBonus = Math.max(0, 10 - cappedOrb);
  
  // Bonus Big Three (2 points si implique Soleil/Lune/Ascendant/MC)
  const bigThreeBonus = (BIG_THREE_POINTS.has(from) || BIG_THREE_POINTS.has(to)) ? 20 : 0;
  
  return planetBonus + orbBonus + bigThreeBonus;
}

/**
 * Génère la clé de tri finale pour un aspect
 * Utilisée pour trier les aspects selon la hiérarchie astrologique professionnelle STRICTE
 * 
 * LOGIQUE STRICTE (ordre fixe, utilisé par les astrologues professionnels) :
 * 1. PRIORITÉ ABSOLUE : Intensité (strong=3 > medium=2 > weak=1)
 * 2. PRIORITÉ 2 : Type d'aspect (ordre fixe : Conj > Opp > Carré > Trigone > Sextile > Quintile > autres)
 * 3. PRIORITÉ 3 : Score de base (UNIQUEMENT pour départager les aspects de même intensité ET même type)
 * 
 * Format : (intensityRank * 1000000) + (aspectTypeRank * 10000) + (baseScore)
 * 
 * Les multiplications très hautes garantissent que :
 * - Un Sextile strong NE PEUT JAMAIS passer avant une Conjonction strong
 * - Un aspect medium NE PEUT JAMAIS passer avant un aspect strong de même type
 * - Le baseScore ne peut inverser l'ordre du type ou de l'intensité
 * 
 * Exemple :
 * - Conjonction Forte (intensité 3, rang 1) :
 *   3 * 1000000 + 1 * 10000 + 60 (base score) = 3010060
 * 
 * - Opposition Forte (intensité 3, rang 2) :
 *   3 * 1000000 + 2 * 10000 + 50 (base score) = 3020050
 * 
 * - Sextile Forte (intensité 3, rang 5) :
 *   3 * 1000000 + 5 * 10000 + 30 (base score) = 3050030
 * 
 * - Conjonction Moyen (intensité 2, rang 1) :
 *   2 * 1000000 + 1 * 10000 + 60 (base score) = 2010060
 * 
 * Résultat : Tous les aspects Fort (3000000+) passent avant les Moyen (2000000+)
 *            Et à l'intérieur des Fort, Conj (3010000+) > Opp (3020000+) > Carré > Trigone > Sextile
 */
export function getFinalAspectSortKey(aspect: {
  aspect_type: string;
  strength: string;
  from: string;
  to: string;
  orb: number;
}): number {
  // PRIORITÉ ABSOLUE : Intensité (Fort > Moyen > Faible)
  const intensityRank = getIntensityRank(aspect.strength);
  
  // PRIORITÉ 2 : Type d'aspect (ordre fixe, ne peut jamais être inversé)
  const typeRank = getAspectTypeRank(aspect.aspect_type);
  
  // PRIORITÉ 3 : Score de base (UNIQUEMENT pour départager même intensité + même type)
  const baseScore = calculateBaseAspectScore(aspect);
  
  // Construction de la clé de tri finale STRICTE
  // On force une hiérarchie très stricte :
  // 1) Intensité (× 1_000_000)
  // 2) Type d'aspect (× 10_000)
  // 3) Score interne (baseScore)
  // La multiplication forte est VOLONTAIRE pour empêcher toute inversion
  return intensityRank * 1_000_000 + typeRank * 10_000 + baseScore;
}

/**
 * Retourne la catégorie d'un aspect (pour affichage)
 */
export function getAspectCategory(aspectType: string): 'major_tense' | 'major_harmonious' | 'minor' {
  if (isMajorTense(aspectType)) return 'major_tense';
  if (isMajorHarmonious(aspectType)) return 'major_harmonious';
  return 'minor';
}

