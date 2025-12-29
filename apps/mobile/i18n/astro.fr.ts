/**
 * Dictionnaires de traduction astrologique FR
 * Mapping EN → FR pour signes, planètes, aspects
 */

// Signes du zodiaque
export const SIGN_FR: Record<string, string> = {
  'aries': 'Bélier',
  'taurus': 'Taureau',
  'gemini': 'Gémeaux',
  'cancer': 'Cancer',
  'leo': 'Lion',
  'virgo': 'Vierge',
  'libra': 'Balance',
  'scorpio': 'Scorpion',
  'sagittarius': 'Sagittaire',
  'capricorn': 'Capricorne',
  'aquarius': 'Verseau',
  'pisces': 'Poissons',
};

// Planètes
export const PLANET_FR: Record<string, string> = {
  'sun': 'Soleil',
  'moon': 'Lune',
  'mercury': 'Mercure',
  'venus': 'Vénus',
  'mars': 'Mars',
  'jupiter': 'Jupiter',
  'saturn': 'Saturne',
  'uranus': 'Uranus',
  'neptune': 'Neptune',
  'pluto': 'Pluton',
  'chiron': 'Chiron',
  'lilith': 'Lilith',
  'northnode': 'Nœud Nord',
  'north_node': 'Nœud Nord',
  'southnode': 'Nœud Sud',
  'south_node': 'Nœud Sud',
};

// Aspects
export const ASPECT_FR: Record<string, string> = {
  'conjunction': 'Conjonction',
  'sextile': 'Sextile',
  'square': 'Carré',
  'trine': 'Trigone',
  'opposition': 'Opposition',
  'quincunx': 'Quinconce',
  'semisextile': 'Semi-sextile',
  'semi_sextile': 'Semi-sextile',
  'semisquare': 'Semi-carré',
  'semi_square': 'Semi-carré',
  'sesquisquare': 'Sesqui-carré',
  'sesqui_square': 'Sesqui-carré',
};
