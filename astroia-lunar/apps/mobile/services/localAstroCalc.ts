/**
 * Local Astrology Calculations (Approximations)
 *
 * Calculs locaux approximatifs pour preview en temps reel
 * NOTE: Ces calculs sont des approximations pour le feedback visuel uniquement.
 * Les calculs precis sont effectues par le backend.
 */

// Zodiac sign date ranges (approximate, using tropical zodiac)
const ZODIAC_RANGES = [
  { sign: 'Capricorn', startMonth: 12, startDay: 22, endMonth: 1, endDay: 19 },
  { sign: 'Aquarius', startMonth: 1, startDay: 20, endMonth: 2, endDay: 18 },
  { sign: 'Pisces', startMonth: 2, startDay: 19, endMonth: 3, endDay: 20 },
  { sign: 'Aries', startMonth: 3, startDay: 21, endMonth: 4, endDay: 19 },
  { sign: 'Taurus', startMonth: 4, startDay: 20, endMonth: 5, endDay: 20 },
  { sign: 'Gemini', startMonth: 5, startDay: 21, endMonth: 6, endDay: 20 },
  { sign: 'Cancer', startMonth: 6, startDay: 21, endMonth: 7, endDay: 22 },
  { sign: 'Leo', startMonth: 7, startDay: 23, endMonth: 8, endDay: 22 },
  { sign: 'Virgo', startMonth: 8, startDay: 23, endMonth: 9, endDay: 22 },
  { sign: 'Libra', startMonth: 9, startDay: 23, endMonth: 10, endDay: 22 },
  { sign: 'Scorpio', startMonth: 10, startDay: 23, endMonth: 11, endDay: 21 },
  { sign: 'Sagittarius', startMonth: 11, startDay: 22, endMonth: 12, endDay: 21 },
];

/**
 * Calculate approximate sun sign from birth date
 * This is an approximation based on standard date ranges
 *
 * @param birthDate - Date object representing the birth date
 * @returns The zodiac sign name in English, or null if invalid date
 */
export function calculateSunSign(birthDate: Date | null | undefined): string | null {
  if (!birthDate || !(birthDate instanceof Date) || isNaN(birthDate.getTime())) {
    return null;
  }

  const month = birthDate.getMonth() + 1; // JavaScript months are 0-indexed
  const day = birthDate.getDate();

  // Handle Capricorn which spans year boundary
  if (
    (month === 12 && day >= 22) ||
    (month === 1 && day <= 19)
  ) {
    return 'Capricorn';
  }

  // Find the matching sign
  for (const range of ZODIAC_RANGES) {
    if (range.sign === 'Capricorn') continue; // Already handled above

    if (
      (month === range.startMonth && day >= range.startDay) ||
      (month === range.endMonth && day <= range.endDay)
    ) {
      return range.sign;
    }
  }

  return null;
}

/**
 * Placeholder for moon sign calculation
 * Moon sign requires precise time and ephemeris data
 * This function returns null to indicate "requires API calculation"
 *
 * In a future version, we could implement approximate moon sign calculation
 * based on lunar cycle position, but it would be less accurate than the API.
 *
 * @param _birthDate - Date object
 * @param _birthTime - Time string (HH:MM)
 * @returns null (placeholder - requires API for accurate calculation)
 */
export function calculateMoonSign(
  _birthDate: Date | null | undefined,
  _birthTime: string | null | undefined
): string | null {
  // Moon sign calculation requires ephemeris data
  // Return null to indicate this needs API calculation
  return null;
}

/**
 * Placeholder for ascendant calculation
 * Ascendant requires precise time, date, and location
 * This function returns null to indicate "requires API calculation"
 *
 * @param _birthDate - Date object
 * @param _birthTime - Time string (HH:MM)
 * @param _latitude - Latitude
 * @param _longitude - Longitude
 * @returns null (placeholder - requires API for accurate calculation)
 */
export function calculateAscendant(
  _birthDate: Date | null | undefined,
  _birthTime: string | null | undefined,
  _latitude: number | null | undefined,
  _longitude: number | null | undefined
): string | null {
  // Ascendant calculation requires precise astronomical calculations
  // Return null to indicate this needs API calculation
  return null;
}

/**
 * Get Big 3 preview data based on input fields
 * Returns approximate values where possible, null otherwise
 */
export interface Big3PreviewData {
  sunSign: string | null;
  moonSign: string | null;
  ascendant: string | null;
  sunPlaceholder: string;
  moonPlaceholder: string;
  ascendantPlaceholder: string;
}

export function getBig3Preview(
  birthDate: Date | null | undefined,
  birthTime: string | null | undefined,
  latitude: number | null | undefined,
  longitude: number | null | undefined
): Big3PreviewData {
  const sunSign = calculateSunSign(birthDate);
  const moonSign = calculateMoonSign(birthDate, birthTime);
  const ascendant = calculateAscendant(birthDate, birthTime, latitude, longitude);

  // Determine placeholders based on what's missing
  const hasDate = birthDate instanceof Date && !isNaN(birthDate.getTime());
  const hasTime = typeof birthTime === 'string' && birthTime.trim().length >= 4;
  const hasLocation =
    typeof latitude === 'number' &&
    Number.isFinite(latitude) &&
    typeof longitude === 'number' &&
    Number.isFinite(longitude);

  // Lune: dépend de la date (change de signe tous les ~2.5 jours)
  // Ascendant: dépend de l'heure ET du lieu
  const moonPlaceholder = hasDate ? 'Calcul API...' : 'Date requise';
  const ascendantPlaceholder = hasTime && hasLocation
    ? 'Calcul API...'
    : !hasTime && !hasLocation
      ? 'Heure + lieu'
      : !hasTime
        ? 'Heure requise'
        : 'Lieu requis';

  return {
    sunSign,
    moonSign,
    ascendant,
    sunPlaceholder: hasDate ? 'Calcul...' : 'Date requise',
    moonPlaceholder,
    ascendantPlaceholder,
  };
}
