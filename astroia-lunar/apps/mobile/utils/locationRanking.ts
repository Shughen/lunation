/**
 * Location Ranking - Trie les résultats Nominatim par pertinence locale
 *
 * Objectif : Prioriser les lieux géographiquement pertinents selon la locale utilisateur
 * Exemple : Pour un utilisateur FR, "Paris, France" doit apparaître avant "Paris, Texas"
 */

export interface LocationResult {
  display_name: string;
  lat: string;
  lon: string;
  address?: {
    city?: string;
    town?: string;
    village?: string;
    municipality?: string;
    hamlet?: string;
    state?: string;
    region?: string;
    county?: string;
    state_district?: string;
    country?: string;
  };
  place_rank?: number;
  type?: string;
  [key: string]: any;
}

/**
 * Mapping locale → pays prioritaires (scoring +100 points)
 *
 * Utilise les codes ISO 3166-1 (noms anglais Nominatim)
 */
const LOCALE_TO_COUNTRIES: Record<string, string[]> = {
  // Français : pays francophones prioritaires
  fr: ['France', 'Belgium', 'Switzerland', 'Luxembourg', 'Monaco'],

  // Anglais : pays anglophones prioritaires
  en: ['United States', 'United Kingdom', 'Canada', 'Australia', 'New Zealand', 'Ireland'],

  // Espagnol
  es: ['Spain', 'Mexico', 'Argentina', 'Colombia', 'Peru', 'Chile', 'Venezuela'],

  // Allemand
  de: ['Germany', 'Austria', 'Switzerland', 'Liechtenstein'],

  // Italien
  it: ['Italy', 'Switzerland', 'San Marino', 'Vatican City'],

  // Portugais
  pt: ['Portugal', 'Brazil', 'Angola', 'Mozambique'],
};

/**
 * Pays francophones (scoring secondaire +50 points)
 */
const FRANCOPHONE_COUNTRIES = new Set([
  'France', 'Belgium', 'Switzerland', 'Luxembourg', 'Monaco',
  'Canada', 'Haiti', 'Senegal', 'Ivory Coast', 'Cameroon',
  'Madagascar', 'Mali', 'Niger', 'Burkina Faso', 'Benin',
  'Chad', 'Togo', 'Rwanda', 'Burundi', 'Djibouti',
  'Central African Republic', 'Republic of the Congo',
  'Democratic Republic of the Congo', 'Gabon', 'Equatorial Guinea',
  'Comoros', 'Seychelles', 'Mauritius', 'Vanuatu',
  'French Polynesia', 'New Caledonia', 'French Guiana',
  'Martinique', 'Guadeloupe', 'Reunion', 'Mayotte',
]);

/**
 * Pays anglophones (scoring secondaire +50 points)
 */
const ANGLOPHONE_COUNTRIES = new Set([
  'United States', 'United Kingdom', 'Canada', 'Australia',
  'New Zealand', 'Ireland', 'South Africa', 'India',
  'Pakistan', 'Nigeria', 'Kenya', 'Uganda', 'Tanzania',
  'Ghana', 'Zimbabwe', 'Zambia', 'Jamaica', 'Trinidad and Tobago',
  'Barbados', 'Singapore', 'Malaysia', 'Philippines',
  'Malta', 'Cyprus', 'Bahamas', 'Fiji',
]);

/**
 * Calcule le score de pertinence d'un lieu selon la locale utilisateur
 *
 * Critères (ordre de priorité) :
 * 1. Pays correspondant à la locale (+100 points)
 * 2. Langue commune (+50 points pour pays francophone/anglophone)
 * 3. Importance du lieu (+0-30 points selon place_rank ou type)
 * 4. Ordre Nominatim (-1 par position, tiebreaker)
 *
 * @param location - Résultat Nominatim
 * @param locale - Code locale (fr, en, etc.)
 * @param originalIndex - Position dans les résultats Nominatim originaux
 * @returns Score numérique (plus élevé = plus pertinent)
 */
function scoreLocation(
  location: LocationResult,
  locale: string,
  originalIndex: number
): number {
  let score = 0;

  // Extraire le pays (priorité: address.country > parsing display_name)
  let country: string | undefined = location.address?.country;

  if (!country) {
    // Fallback : parser display_name (dernier segment = pays généralement)
    const parts = location.display_name.split(',').map(s => s.trim());
    country = parts.length > 0 ? parts[parts.length - 1] : undefined;
  }

  // 1. Pays correspondant à la locale (+100 points)
  const priorityCountries = LOCALE_TO_COUNTRIES[locale] || [];
  if (country && priorityCountries.includes(country)) {
    score += 100;
  }

  // 2. Langue commune (+50 points)
  if (country) {
    if (locale === 'fr' && FRANCOPHONE_COUNTRIES.has(country)) {
      score += 50;
    } else if (locale === 'en' && ANGLOPHONE_COUNTRIES.has(country)) {
      score += 50;
    }
  }

  // 3. Importance du lieu (+0-30 points)
  // Nominatim place_rank : 0-30 (plus petit = plus important)
  // On inverse pour que grande ville = plus de points
  if (location.place_rank !== undefined && location.place_rank !== null) {
    const importanceScore = Math.max(0, 30 - location.place_rank);
    score += importanceScore;
  } else if (location.type) {
    // Fallback sur type si place_rank absent
    const typeScores: Record<string, number> = {
      city: 30,
      town: 25,
      municipality: 20,
      village: 15,
      hamlet: 10,
      locality: 10,
      suburb: 5,
    };
    score += typeScores[location.type] || 0;
  }

  // 4. Ordre Nominatim comme tiebreaker (-1 par position)
  // Permet de préserver l'ordre de Nominatim en cas d'égalité
  score -= originalIndex;

  return score;
}

/**
 * Trie les résultats de lieux par pertinence selon la locale utilisateur
 *
 * @param locations - Résultats Nominatim (déjà dédupliqués)
 * @param locale - Code locale (fr, en, etc.)
 * @returns Tableau trié par pertinence décroissante
 *
 * @example
 * // Utilisateur français cherche "Paris"
 * const results = [
 *   { display_name: "Paris, Texas, United States", ... },
 *   { display_name: "Paris, Île-de-France, France", ... }
 * ];
 * const ranked = rankLocationsByRelevance(results, 'fr');
 * // ranked[0] → Paris, France (score ~180)
 * // ranked[1] → Paris, Texas (score ~69)
 */
export function rankLocationsByRelevance<T extends LocationResult>(
  locations: T[],
  locale: string
): T[] {
  // Normaliser la locale (retirer variantes régionales : fr-FR → fr)
  const baseLocale = locale.split('-')[0].toLowerCase();

  // Calculer le score pour chaque lieu
  const scored = locations.map((location, index) => ({
    location,
    score: scoreLocation(location, baseLocale, index),
  }));

  // Trier par score décroissant
  scored.sort((a, b) => b.score - a.score);

  // Retourner les lieux triés (sans les scores)
  return scored.map(item => item.location);
}
