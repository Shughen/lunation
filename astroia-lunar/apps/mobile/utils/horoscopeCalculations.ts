/**
 * Horoscope Calculations
 * Local calculation of horoscope metrics based on lunar data
 */

// Types
export interface LuckyElements {
  numbers: number[];
  color: string;
  colorHex: string;
  stone: string;
  favorableHours: string;
}

export interface HoroscopeMetrics {
  creativeEnergy: number;
  intuition: number;
  luckyElements: LuckyElements;
}

// Moon phase to progress mapping (0-100)
const PHASE_ENERGY_MAP: Record<string, number> = {
  new_moon: 50,
  waxing_crescent: 65,
  first_quarter: 75,
  waxing_gibbous: 85,
  full_moon: 100,
  waning_gibbous: 80,
  last_quarter: 60,
  waning_crescent: 45,
};

// Element to color mapping
const ELEMENT_COLORS: Record<string, { name: string; hex: string }> = {
  fire: { name: 'Rouge', hex: '#FF6B6B' },
  earth: { name: 'Vert', hex: '#7CB342' },
  air: { name: 'Bleu', hex: '#64B5F6' },
  water: { name: 'Violet', hex: '#9575CD' },
};

// Sign to element mapping
const SIGN_ELEMENTS: Record<string, string> = {
  Aries: 'fire',
  Leo: 'fire',
  Sagittarius: 'fire',
  Taurus: 'earth',
  Virgo: 'earth',
  Capricorn: 'earth',
  Gemini: 'air',
  Libra: 'air',
  Aquarius: 'air',
  Cancer: 'water',
  Scorpio: 'water',
  Pisces: 'water',
};

// Sign to stone mapping
const SIGN_STONES: Record<string, string> = {
  Aries: 'Diamant',
  Taurus: 'Emeraude',
  Gemini: 'Agate',
  Cancer: 'Perle',
  Leo: 'Rubis',
  Virgo: 'Saphir',
  Libra: 'Opale',
  Scorpio: 'Topaze',
  Sagittarius: 'Turquoise',
  Capricorn: 'Grenat',
  Aquarius: 'Amethyste',
  Pisces: 'Aigue-marine',
};

// Water signs boost intuition
const WATER_SIGNS = ['Cancer', 'Scorpio', 'Pisces'];

/**
 * Normalize moon phase string to our expected format
 */
function normalizePhase(phase: string | undefined): string {
  if (!phase) return 'new_moon';

  const normalized = phase.toLowerCase().replace(/\s+/g, '_');

  // Map common variations
  const phaseMap: Record<string, string> = {
    new: 'new_moon',
    new_moon: 'new_moon',
    waxing_crescent: 'waxing_crescent',
    crescent: 'waxing_crescent',
    first_quarter: 'first_quarter',
    waxing_gibbous: 'waxing_gibbous',
    gibbous: 'waxing_gibbous',
    full: 'full_moon',
    full_moon: 'full_moon',
    waning_gibbous: 'waning_gibbous',
    disseminating: 'waning_gibbous',
    last_quarter: 'last_quarter',
    third_quarter: 'last_quarter',
    waning_crescent: 'waning_crescent',
    balsamic: 'waning_crescent',
  };

  return phaseMap[normalized] || 'new_moon';
}

/**
 * Calculate creative energy based on moon phase and aspects
 * @param lunarPhase - Current moon phase
 * @param aspects - Optional array of active aspects
 * @returns Number between 0 and 100
 */
export function calculateCreativeEnergy(
  lunarPhase: string | undefined,
  aspects?: Array<{ aspect?: string; type?: string }> | null
): number {
  const normalizedPhase = normalizePhase(lunarPhase);
  let energy = PHASE_ENERGY_MAP[normalizedPhase] || 50;

  // Boost from favorable aspects
  if (aspects && aspects.length > 0) {
    const favorableAspects = aspects.filter(
      (a) => {
        const aspectType = a.aspect || a.type || '';
        return aspectType.toLowerCase().includes('trine') ||
               aspectType.toLowerCase().includes('sextile');
      }
    );
    energy += favorableAspects.length * 3;
  }

  // Waxing phases = more creative energy
  if (normalizedPhase.includes('waxing')) {
    energy += 5;
  }

  return Math.min(100, Math.max(0, energy));
}

/**
 * Calculate intuition level based on moon sign and aspects
 * @param moonSign - Current moon sign
 * @param aspects - Optional array of active aspects
 * @returns Number between 0 and 100
 */
export function calculateIntuition(
  moonSign: string | undefined,
  aspects?: Array<{ planet1?: string; planet2?: string; aspect?: string }> | null
): number {
  let intuition = 60; // Base level

  // Water signs boost intuition significantly
  if (moonSign && WATER_SIGNS.includes(moonSign)) {
    intuition += 20;
  }

  // Neptune or Moon aspects boost intuition
  if (aspects && aspects.length > 0) {
    const neptuneAspects = aspects.filter(
      (a) =>
        a.planet1?.toLowerCase().includes('neptune') ||
        a.planet2?.toLowerCase().includes('neptune') ||
        a.planet1?.toLowerCase().includes('moon') ||
        a.planet2?.toLowerCase().includes('moon')
    );
    intuition += neptuneAspects.length * 5;
  }

  // Element-based adjustments
  if (moonSign) {
    const element = SIGN_ELEMENTS[moonSign];
    if (element === 'water') intuition += 10;
    else if (element === 'air') intuition += 5;
  }

  return Math.min(100, Math.max(0, intuition));
}

/**
 * Get lucky elements based on moon sign and day
 * @param moonSign - Current moon sign
 * @param dayOfMonth - Day of the month (1-31)
 * @returns Lucky elements object
 */
export function getLuckyElements(
  moonSign: string | undefined,
  dayOfMonth?: number
): LuckyElements {
  const day = dayOfMonth || new Date().getDate();
  const sign = moonSign || 'Aries';

  // Calculate lucky numbers based on day
  const number1 = (day % 9) + 1;
  const number2 = ((day * 2) % 21) + 1;
  const numbers = [number1, number2].sort((a, b) => a - b);

  // Get color from element
  const element = SIGN_ELEMENTS[sign] || 'fire';
  const colorInfo = ELEMENT_COLORS[element] || ELEMENT_COLORS.fire;

  // Get stone from sign
  const stone = SIGN_STONES[sign] || 'Diamant';

  // Calculate favorable hours based on element
  const hourRanges: Record<string, string> = {
    fire: '12h-14h',
    earth: '6h-8h',
    air: '10h-12h',
    water: '20h-22h',
  };
  const favorableHours = hourRanges[element] || '14h-16h';

  return {
    numbers,
    color: colorInfo.name,
    colorHex: colorInfo.hex,
    stone,
    favorableHours,
  };
}

/**
 * Get all horoscope metrics in one call
 */
export function getHoroscopeMetrics(
  moonSign: string | undefined,
  lunarPhase: string | undefined,
  aspects?: Array<any> | null
): HoroscopeMetrics {
  return {
    creativeEnergy: calculateCreativeEnergy(lunarPhase, aspects),
    intuition: calculateIntuition(moonSign, aspects),
    luckyElements: getLuckyElements(moonSign),
  };
}

/**
 * Get zodiac sign in French
 */
export function getZodiacSignFrench(sign: string | undefined): string {
  const frenchNames: Record<string, string> = {
    Aries: 'Belier',
    Taurus: 'Taureau',
    Gemini: 'Gemeaux',
    Cancer: 'Cancer',
    Leo: 'Lion',
    Virgo: 'Vierge',
    Libra: 'Balance',
    Scorpio: 'Scorpion',
    Sagittarius: 'Sagittaire',
    Capricorn: 'Capricorne',
    Aquarius: 'Verseau',
    Pisces: 'Poissons',
  };
  return frenchNames[sign || ''] || sign || 'Inconnu';
}

/**
 * Get moon phase in French
 */
export function getMoonPhaseFrench(phase: string | undefined): string {
  const normalizedPhase = normalizePhase(phase);
  const frenchNames: Record<string, string> = {
    new_moon: 'Nouvelle Lune',
    waxing_crescent: 'Lune Croissante',
    first_quarter: 'Premier Quartier',
    waxing_gibbous: 'Lune Gibbeuse Croissante',
    full_moon: 'Pleine Lune',
    waning_gibbous: 'Lune Gibbeuse Decroissante',
    last_quarter: 'Dernier Quartier',
    waning_crescent: 'Lune Decroissante',
  };
  return frenchNames[normalizedPhase] || 'Lune';
}

/**
 * Get guidance text based on moon phase
 */
export function getPhaseGuidance(phase: string | undefined): string {
  const normalizedPhase = normalizePhase(phase);
  const guidances: Record<string, string> = {
    new_moon: 'Moment ideal pour planter de nouvelles intentions et demarrer des projets.',
    waxing_crescent: 'La lune croissante vous pousse a exprimer vos idees avec audace. C\'est le moment ideal pour initier de nouveaux projets et prendre des risques calcules dans vos entreprises.',
    first_quarter: 'Temps d\'action et de decision. Surmontez les obstacles avec determination.',
    waxing_gibbous: 'Affinez vos plans et preparez-vous pour la culmination de vos efforts.',
    full_moon: 'Energie a son apogee. Celebrez vos accomplissements et liberez ce qui ne vous sert plus.',
    waning_gibbous: 'Partagez votre sagesse et reflechissez a vos reussites.',
    last_quarter: 'Temps de lacher-prise. Liberez les vieilles habitudes et croyances.',
    waning_crescent: 'Phase de repos et d\'introspection. Preparez-vous pour un nouveau cycle.',
  };
  return guidances[normalizedPhase] || 'Suivez votre intuition et restez a l\'ecoute de vos besoins.';
}

/**
 * Get domain insight for love
 */
export function getLoveInsight(moonSign: string | undefined): string {
  const element = SIGN_ELEMENTS[moonSign || ''] || 'fire';
  const insights: Record<string, string> = {
    fire: 'Periode favorable aux nouvelles rencontres. Votre charisme est au plus haut.',
    earth: 'Moment propice pour solidifier vos liens. Privilegiez la stabilite.',
    air: 'Communication fluide avec vos proches. Echangez vos idees.',
    water: 'Connexion emotionnelle profonde. Laissez parler votre coeur.',
  };
  return insights[element] || 'Suivez votre coeur.';
}

/**
 * Get domain insight for career
 */
export function getCareerInsight(moonSign: string | undefined): string {
  const element = SIGN_ELEMENTS[moonSign || ''] || 'fire';
  const insights: Record<string, string> = {
    fire: 'Ideal pour proposer vos idees innovantes. Osez prendre des initiatives.',
    earth: 'Concentrez-vous sur les taches concretes. Vos efforts seront recompenses.',
    air: 'Jours favorables: Mer, Ven. Networking et collaboration au programme.',
    water: 'Fiez-vous a votre intuition pour les decisions professionnelles.',
  };
  return insights[element] || 'Restez focus sur vos objectifs.';
}
