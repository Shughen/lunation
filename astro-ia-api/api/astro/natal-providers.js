// ============================================
// NATAL CHART PROVIDERS - ARCHITECTURE MODULAIRE
// ============================================
// Permet de basculer entre plusieurs sources de calcul

/**
 * PROVIDER: LOCAL (V2 - Enhanced)
 * Gratuit, auto-hébergé, formules astronomiques précises
 * Précision: Soleil ±1', Lune ±10', Ascendant ±1°
 */
import {
  dateToJulianDay,
  calculateSunPosition,
  calculateMoonPosition,
  calculateAscendant,
  longitudeToZodiac,
} from './natal-calculations.js';

// Swiss Ephemeris et Ephemeris API : Optionnels (non utilisés en production)
// import { calculateSwissEphemeris } from './natal-swisseph.js';
// import { calculateEphemerisAPI } from './natal-ephemeris.js';

async function calculateLocal(params) {
  const { date, time, lat, lon, tz } = params;
  
  const [year, month, day] = date.split('-').map(Number);
  const [hours, minutes] = time.split(':').map(Number);
  
  const jd = dateToJulianDay(year, month, day, hours, minutes);
  
  const sunLon = calculateSunPosition(jd);
  const moonLon = calculateMoonPosition(jd);
  const ascLon = calculateAscendant(jd, lat, lon);
  
  const sun = longitudeToZodiac(sunLon);
  const moon = longitudeToZodiac(moonLon);
  const ascendant = longitudeToZodiac(ascLon);
  
  // Approximations simples pour les autres planètes
  const mercuryLon = (sunLon + (Math.sin(jd * 0.0004) * 20)) % 360;
  const venusLon = (sunLon + (Math.sin(jd * 0.00025) * 45)) % 360;
  const marsLon = (sunLon + (Math.sin(jd * 0.00015) * 135)) % 360;
  
  const mercury = longitudeToZodiac(mercuryLon);
  const venus = longitudeToZodiac(venusLon);
  const mars = longitudeToZodiac(marsLon);
  
  return {
    positions: {
      sun,
      moon,
      ascendant,
      mercury,
      venus,
      mars,
    },
    meta: {
      provider: 'local-v2-enhanced',
      cost: 0,
      precision: {
        sun: '±1 minute d\'arc',
        moon: '±10 minutes d\'arc',
        ascendant: '±1 degré',
      },
      formulas: 'VSOP87 (Soleil) + ELP2000 (Lune) + Jean Meeus (Ascendant)',
      julianDay: jd,
    },
  };
}

/**
 * PROVIDER: PROKERALA API
 * Plan gratuit: 5000 credits/mois
 * Précision: Professionnelle (Swiss Ephemeris)
 * Documentation: https://api.prokerala.com
 */
async function calculateProkerala(params) {
  const { date, time, lat, lon, tz } = params;
  
  // Clé API depuis variables d'environnement
  const apiKey = process.env.PROKERALA_API_KEY;
  const apiUser = process.env.PROKERALA_API_USER;
  
  if (!apiKey || !apiUser) {
    throw new Error('PROKERALA_API_KEY and PROKERALA_API_USER required');
  }
  
  // Convertir la date/heure au format Prokerala
  const datetime = `${date}T${time}:00`;
  
  const url = 'https://api.prokerala.com/v2/astrology/birth-details';
  const params_query = new URLSearchParams({
    ayanamsa: 1, // Western astrology
    datetime,
    coordinates: `${lat},${lon}`,
  });
  
  const response = await fetch(`${url}?${params_query}`, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'x-api-key': apiUser,
      'Content-Type': 'application/json',
    },
  });
  
  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Prokerala API error: ${response.status} - ${error}`);
  }
  
  const data = await response.json();
  
  // Mapper les données Prokerala vers notre format standard
  const positions = mapProkeralaToStandard(data);
  
  return {
    positions,
    meta: {
      provider: 'prokerala-api',
      cost: 0.001, // ~$12/mois pour 5000 credits
      precision: 'Swiss Ephemeris (professionnel)',
      credits_used: 1,
      raw_data: data,
    },
  };
}

/**
 * PROVIDER: ASTROLOGER API (GitHub Open-Source)
 * Gratuit si auto-hébergé
 * À implémenter quand hébergé
 */
async function calculateAstrologer(params) {
  const { date, time, lat, lon, tz } = params;
  
  // URL de votre instance Astrologer API
  const baseUrl = process.env.ASTROLOGER_API_URL || 'http://localhost:5000';
  
  const response = await fetch(`${baseUrl}/natal-chart`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      date,
      time,
      latitude: lat,
      longitude: lon,
      timezone: tz,
    }),
  });
  
  if (!response.ok) {
    throw new Error(`Astrologer API error: ${response.status}`);
  }
  
  const data = await response.json();
  
  return {
    positions: mapAstrologerToStandard(data),
    meta: {
      provider: 'astrologer-api-self-hosted',
      cost: 0,
      precision: 'Swiss Ephemeris (professionnel)',
      open_source: true,
    },
  };
}

/**
 * MAPPER: Prokerala vers format standard
 */
function mapProkeralaToStandard(data) {
  // À adapter selon la structure réelle de Prokerala
  const { planets, ascendant } = data.data || {};
  
  return {
    sun: mapPlanetData(planets?.sun),
    moon: mapPlanetData(planets?.moon),
    ascendant: mapPlanetData(ascendant),
    mercury: mapPlanetData(planets?.mercury),
    venus: mapPlanetData(planets?.venus),
    mars: mapPlanetData(planets?.mars),
  };
}

/**
 * MAPPER: Astrologer vers format standard
 */
function mapAstrologerToStandard(data) {
  // À adapter selon la structure réelle de Astrologer API
  return {
    sun: mapPlanetData(data.sun),
    moon: mapPlanetData(data.moon),
    ascendant: mapPlanetData(data.ascendant),
    mercury: mapPlanetData(data.mercury),
    venus: mapPlanetData(data.venus),
    mars: mapPlanetData(data.mars),
  };
}

/**
 * Helper: Mapper les données planétaires
 */
function mapPlanetData(planetData) {
  if (!planetData) return null;
  
  return {
    sign: planetData.sign || planetData.zodiac_sign,
    emoji: getZodiacEmoji(planetData.sign || planetData.zodiac_sign),
    degree: planetData.degree,
    minutes: planetData.minutes,
    longitude: planetData.longitude || planetData.full_degree,
  };
}

/**
 * Helper: Emoji du signe
 */
function getZodiacEmoji(signName) {
  const emojis = {
    'Aries': '♈', 'Bélier': '♈',
    'Taurus': '♉', 'Taureau': '♉',
    'Gemini': '♊', 'Gémeaux': '♊',
    'Cancer': '♋',
    'Leo': '♌', 'Lion': '♌',
    'Virgo': '♍', 'Vierge': '♍',
    'Libra': '♎', 'Balance': '♎',
    'Scorpio': '♏', 'Scorpion': '♏',
    'Sagittarius': '♐', 'Sagittaire': '♐',
    'Capricorn': '♑', 'Capricorne': '♑',
    'Aquarius': '♒', 'Verseau': '♒',
    'Pisces': '♓', 'Poissons': '♓',
  };
  
  return emojis[signName] || '⭐';
}

// ============================================
// ROUTER PRINCIPAL
// ============================================

/**
 * Calcule un thème natal avec le provider configuré
 * @param {Object} params - {date, time, lat, lon, tz, provider}
 * @returns {Object} Résultats du thème natal
 */
async function calculateNatalChart(params) {
  // Provider LOCAL par défaut : gratuit, compatible Vercel, précision suffisante pour MVP
  const provider = params.provider || process.env.NATAL_PROVIDER || 'local';
  
  console.log(`[Natal] Using provider: ${provider}`);
  
  switch (provider.toLowerCase()) {
    case 'local':
    case 'local-v2':
      return await calculateLocal(params);
    
    case 'prokerala':
      return await calculateProkerala(params);
    
    // Autres providers désactivés (non utilisés en production)
    // case 'swisseph':
    // case 'ephemeris-api':
    // case 'astrologer':
    
    default:
      console.log(`[Natal] Using default provider: local`);
      return await calculateLocal(params);
  }
}

export {
  calculateNatalChart,
  calculateLocal,
  calculateProkerala,
};

