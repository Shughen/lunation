/**
 * Traductions des termes astrologiques anglais → français
 */

export const PLANET_NAMES_FR = {
  'Sun': 'Soleil',
  'Moon': 'Lune',
  'Mercury': 'Mercure',
  'Venus': 'Vénus',
  'Mars': 'Mars',
  'Jupiter': 'Jupiter',
  'Saturn': 'Saturne',
  'Uranus': 'Uranus',
  'Neptune': 'Neptune',
  'Pluto': 'Pluton',
  'Ascendant': 'Ascendant',
  'Medium_Coeli': 'Milieu du Ciel',
  'Mean_Node': 'Nœud Nord',
  'Mean_South_Node': 'Nœud Sud',
  'Mean_Lilith': 'Lilith',
  'Lilith': 'Lilith',  // Variante sans préfixe
  'Chiron': 'Chiron',
};

export const SIGN_NAMES_FR = {
  // Noms complets
  'Aries': 'Bélier',
  'Taurus': 'Taureau',
  'Gemini': 'Gémeaux',
  'Cancer': 'Cancer',
  'Leo': 'Lion',
  'Virgo': 'Vierge',
  'Libra': 'Balance',
  'Scorpio': 'Scorpion',
  'Sagittarius': 'Sagittaire',
  'Capricorn': 'Capricorne',
  'Aquarius': 'Verseau',
  'Pisces': 'Poissons',
  // Abréviations (de l'API Best Astrology)
  'Ari': 'Bélier',
  'Tau': 'Taureau',
  'Gem': 'Gémeaux',
  'Can': 'Cancer',
  'Leo': 'Lion',
  'Vir': 'Vierge',
  'Lib': 'Balance',
  'Sco': 'Scorpion',
  'Sag': 'Sagittaire',
  'Cap': 'Capricorne',
  'Aqu': 'Verseau',
  'Pis': 'Poissons',
};

export const ASPECT_TYPES_FR = {
  'conjunction': 'Conjonction',
  'opposition': 'Opposition',
  'trine': 'Trigone',
  'square': 'Carré',
  'sextile': 'Sextile',
  'quintile': 'Quintile',
  'biquintile': 'Biquintile',
  'semisextile': 'Semi-sextile',
  'semisquare': 'Semi-carré',
  'sesquisquare': 'Sesqui-carré',
  'quincunx': 'Quinconce',
};

export const HOUSE_NAMES_FR = {
  1: 'Maison I',
  2: 'Maison II',
  3: 'Maison III',
  4: 'Maison IV',
  5: 'Maison V',
  6: 'Maison VI',
  7: 'Maison VII',
  8: 'Maison VIII',
  9: 'Maison IX',
  10: 'Maison X',
  11: 'Maison XI',
  12: 'Maison XII',
};

/**
 * Traduit un nom de planète
 */
export function translatePlanet(englishName) {
  return PLANET_NAMES_FR[englishName] || englishName;
}

/**
 * Traduit un type d'aspect
 */
export function translateAspect(englishType) {
  if (!englishType) return '';
  const normalized = englishType.toLowerCase();
  return ASPECT_TYPES_FR[normalized] || englishType;
}

/**
 * Traduit un numéro de maison
 */
export function translateHouse(houseNumber) {
  return HOUSE_NAMES_FR[houseNumber] || `Maison ${houseNumber}`;
}

/**
 * Traduit les niveaux de force des aspects
 */
export function translateStrength(strength) {
  const strengths = {
    'strong': 'Fort',
    'medium': 'Moyen',
    'weak': 'Faible',
  };
  if (!strength) return '';
  const normalized = strength.toLowerCase();
  return strengths[normalized] || strength;
}

/**
 * Traduit un nom de signe zodiacal
 */
export function translateSign(englishSign) {
  if (!englishSign) return '';
  return SIGN_NAMES_FR[englishSign] || englishSign;
}

