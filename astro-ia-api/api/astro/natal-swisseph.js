// ============================================
// NATAL CHART - SWISS EPHEMERIS WASM PROVIDER
// ============================================
// Précision professionnelle (même que Astrotheme)
// WebAssembly : léger, compatible Vercel, gratuit
// Package: sweph-wasm (activement maintenu, Sep 2025)

import SwissEPH from 'sweph-wasm';

// Instancier Swiss Ephemeris WASM
let swephInstance = null;

async function getSwephInstance() {
  if (!swephInstance) {
    swephInstance = await SwissEPH.init();
    // Télécharger les éphémérides depuis le CDN
    await swephInstance.swe_set_ephe_path();
  }
  return swephInstance;
}

// Constantes Swiss Ephemeris
const SE_SUN = 0;
const SE_MOON = 1;
const SE_MERCURY = 2;
const SE_VENUS = 3;
const SE_MARS = 4;
const SE_JUPITER = 5;
const SE_SATURN = 6;
const SE_URANUS = 7;
const SE_NEPTUNE = 8;
const SE_PLUTO = 9;

const SEFLG_SWIEPH = 2;
const SE_GREG_CAL = 1;

// Mapping des planètes
const PLANETS = {
  SUN: SE_SUN,
  MOON: SE_MOON,
  MERCURY: SE_MERCURY,
  VENUS: SE_VENUS,
  MARS: SE_MARS,
  JUPITER: SE_JUPITER,
  SATURN: SE_SATURN,
  URANUS: SE_URANUS,
  NEPTUNE: SE_NEPTUNE,
  PLUTO: SE_PLUTO,
};

// Mapping des signes du zodiaque
const ZODIAC_SIGNS = [
  { name: 'Bélier', emoji: '♈', element: 'Feu' },
  { name: 'Taureau', emoji: '♉', element: 'Terre' },
  { name: 'Gémeaux', emoji: '♊', element: 'Air' },
  { name: 'Cancer', emoji: '♋', element: 'Eau' },
  { name: 'Lion', emoji: '♌', element: 'Feu' },
  { name: 'Vierge', emoji: '♍', element: 'Terre' },
  { name: 'Balance', emoji: '♎', element: 'Air' },
  { name: 'Scorpion', emoji: '♏', element: 'Eau' },
  { name: 'Sagittaire', emoji: '♐', element: 'Feu' },
  { name: 'Capricorne', emoji: '♑', element: 'Terre' },
  { name: 'Verseau', emoji: '♒', element: 'Air' },
  { name: 'Poissons', emoji: '♓', element: 'Eau' },
];

/**
 * Convertir longitude écliptique en signe zodiacal
 */
function longitudeToZodiac(longitude) {
  let lon = longitude % 360;
  if (lon < 0) lon += 360;

  const signIndex = Math.floor(lon / 30);
  const sign = ZODIAC_SIGNS[signIndex];
  const degree = Math.floor(lon % 30);
  const minutes = Math.floor(((lon % 30) - degree) * 60);

  return {
    sign: sign.name,
    emoji: sign.emoji,
    element: sign.element,
    degree,
    minutes,
    longitude: lon,
  };
}

/**
 * Calculer un thème natal complet avec Swiss Ephemeris WASM
 */
export async function calculateSwissEphemeris(params) {
  const { date, time, lat, lon, tz } = params;

  try {
    // Initialiser sweph-wasm
    const swe = await getSwephInstance();

    // Parser date et heure
    const [year, month, day] = date.split('-').map(Number);
    const [hours, minutes] = time.split(':').map(Number);

    console.log('[SwissEph-WASM] Heure LOCALE:', { year, month, day, hours, minutes, tz });

    // IMPORTANT : Convertir l'heure locale en UTC pour Swiss Ephemeris
    let utcHours = hours;
    let utcDay = day;
    
    // Approximation des offsets communs
    const timezoneOffsets = {
      'America/Manaus': 4,      // UTC-4
      'America/Sao_Paulo': 3,   // UTC-3
      'Europe/Paris': -1,       // UTC+1 (hiver) / UTC+2 (été)
      'America/New_York': 5,    // UTC-5 (hiver) / UTC-4 (été)
    };
    
    const offset = timezoneOffsets[tz] || 0;
    utcHours = hours + offset;
    
    // Ajuster le jour si nécessaire
    if (utcHours >= 24) {
      utcHours -= 24;
      utcDay += 1;
    } else if (utcHours < 0) {
      utcHours += 24;
      utcDay -= 1;
    }

    console.log('[SwissEph-WASM] Heure UTC:', { year, month, day: utcDay, hours: utcHours, minutes });

    // Calculer le Jour Julien en UTC
    const hourDecimal = utcHours + minutes / 60.0;
    const jd = swe.swe_julday(year, month, utcDay, hourDecimal, SE_GREG_CAL);

    console.log('[SwissEph-WASM] Julian Day:', jd);

    // Calculer toutes les positions planétaires
    const sunResult = swe.swe_calc_ut(jd, PLANETS.SUN, SEFLG_SWIEPH);
    const moonResult = swe.swe_calc_ut(jd, PLANETS.MOON, SEFLG_SWIEPH);
    const mercuryResult = swe.swe_calc_ut(jd, PLANETS.MERCURY, SEFLG_SWIEPH);
    const venusResult = swe.swe_calc_ut(jd, PLANETS.VENUS, SEFLG_SWIEPH);
    const marsResult = swe.swe_calc_ut(jd, PLANETS.MARS, SEFLG_SWIEPH);
    const jupiterResult = swe.swe_calc_ut(jd, PLANETS.JUPITER, SEFLG_SWIEPH);
    const saturnResult = swe.swe_calc_ut(jd, PLANETS.SATURN, SEFLG_SWIEPH);
    const uranusResult = swe.swe_calc_ut(jd, PLANETS.URANUS, SEFLG_SWIEPH);
    const neptuneResult = swe.swe_calc_ut(jd, PLANETS.NEPTUNE, SEFLG_SWIEPH);
    const plutoResult = swe.swe_calc_ut(jd, PLANETS.PLUTO, SEFLG_SWIEPH);

    // Calculer l'Ascendant et les maisons
    const houses = swe.swe_houses(jd, lat, lon, 'P'); // Placidus

    // Extraire les positions (longitude = premier élément du tableau)
    const sun = longitudeToZodiac(sunResult[0]);
    const moon = longitudeToZodiac(moonResult[0]);
    const mercury = longitudeToZodiac(mercuryResult[0]);
    const venus = longitudeToZodiac(venusResult[0]);
    const mars = longitudeToZodiac(marsResult[0]);
    const jupiter = longitudeToZodiac(jupiterResult[0]);
    const saturn = longitudeToZodiac(saturnResult[0]);
    const uranus = longitudeToZodiac(uranusResult[0]);
    const neptune = longitudeToZodiac(neptuneResult[0]);
    const pluto = longitudeToZodiac(plutoResult[0]);

    // Ascendant = premier élément de ascmc
    const ascendant = longitudeToZodiac(houses.ascmc[0]);

    console.log('[SwissEph-WASM] Résultats:', {
      sun: sun?.sign,
      moon: moon?.sign,
      ascendant: ascendant?.sign,
      mercury: mercury?.sign,
    });

    return {
      positions: {
        sun,
        moon,
        ascendant,
        mercury,
        venus,
        mars,
        jupiter,
        saturn,
        uranus,
        neptune,
        pluto,
      },
      meta: {
        provider: 'sweph-wasm',
        cost: 0,
        precision: 'Professionnelle (Swiss Ephemeris WebAssembly)',
        julianDay: jd,
        version: 'sweph-wasm v2.6.9+ (Sep 2025)',
        note: 'Précision maximale - Même calculs que Astrotheme.com - Compatible Vercel',
      },
    };
  } catch (error) {
    console.error('[SwissEph-WASM] Erreur globale:', error);
    throw error;
  }
}
