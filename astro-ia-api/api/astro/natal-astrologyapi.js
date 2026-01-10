/**
 * API Vercel - Calcul de thème natal via AstrologyAPI v3
 * Endpoint: /api/astro/natal-astrologyapi
 * 
 * Documentation AstrologyAPI: https://astrologyapi.com/western-astrology
 */

const ASTROLOGY_API_USER_ID = process.env.ASTROLOGY_API_USER_ID;
const ASTROLOGY_API_KEY = process.env.ASTROLOGY_API_KEY;
const ASTROLOGY_API_URL = 'https://json.astrologyapi.com/v1';

/**
 * Authentification Basic Auth pour AstrologyAPI
 */
function getAuthHeader() {
  if (!ASTROLOGY_API_USER_ID || !ASTROLOGY_API_KEY) {
    throw new Error('AstrologyAPI credentials not configured');
  }
  
  const credentials = Buffer.from(`${ASTROLOGY_API_USER_ID}:${ASTROLOGY_API_KEY}`).toString('base64');
  return `Basic ${credentials}`;
}

/**
 * Calculer le thème natal complet
 */
async function computeNatalChart(birthData) {
  const { date, time, lat, lon, tz } = birthData;
  
  // Parser la date et l'heure
  const [year, month, day] = date.split('-').map(Number);
  const [hour, minute] = time.split(':').map(Number);
  
  // Calculer le timezone offset (ex: "Europe/Paris" = +1 ou +2)
  // Pour simplifier, on utilise le tz numérique fourni ou on calcule
  const tzOffset = typeof tz === 'number' ? tz : 1.0; // Paris = UTC+1 (hiver) ou UTC+2 (été)
  
  const payload = {
    day,
    month,
    year,
    hour,
    min: minute,
    lat,
    lon,
    tzone: tzOffset,
    house_type: 'placidus', // Système de maisons Placidus (standard)
  };
  
  console.log('[AstrologyAPI] Request payload:', payload);
  
  try {
    const response = await fetch(`${ASTROLOGY_API_URL}/western_chart_data`, {
      method: 'POST',
      headers: {
        'Authorization': getAuthHeader(),
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });
    
    if (!response.ok) {
      const errorText = await response.text();
      console.error('[AstrologyAPI] Error response:', errorText);
      throw new Error(`AstrologyAPI error: ${response.status} - ${errorText}`);
    }
    
    const data = await response.json();
    console.log('[AstrologyAPI] Response received:', Object.keys(data));
    
    // Formatter la réponse pour l'app
    return formatNatalChart(data);
  } catch (error) {
    console.error('[AstrologyAPI] Request failed:', error);
    throw error;
  }
}

/**
 * Formatter la réponse AstrologyAPI au format attendu par l'app
 */
function formatNatalChart(apiResponse) {
  const { ascendant, planets, houses, aspects } = apiResponse;
  
  // Mapper les noms de signes anglais → français
  const signMapping = {
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
  };
  
  const emojiMapping = {
    'Aries': '♈', 'Taurus': '♉', 'Gemini': '♊', 'Cancer': '♋',
    'Leo': '♌', 'Virgo': '♍', 'Libra': '♎', 'Scorpio': '♏',
    'Sagittarius': '♐', 'Capricorn': '♑', 'Aquarius': '♒', 'Pisces': '♓',
  };
  
  const elementMapping = {
    'Aries': 'Feu', 'Leo': 'Feu', 'Sagittarius': 'Feu',
    'Taurus': 'Terre', 'Virgo': 'Terre', 'Capricorn': 'Terre',
    'Gemini': 'Air', 'Libra': 'Air', 'Aquarius': 'Air',
    'Cancer': 'Eau', 'Scorpio': 'Eau', 'Pisces': 'Eau',
  };
  
  // Fonction helper pour formater une position
  const formatPosition = (planetData) => ({
    sign: signMapping[planetData.sign] || planetData.sign,
    emoji: emojiMapping[planetData.sign] || '⭐',
    element: elementMapping[planetData.sign] || 'Inconnu',
    longitude: planetData.full_degree,
    degree: Math.floor(planetData.full_degree % 30),
    minutes: Math.floor((planetData.full_degree % 30 - Math.floor(planetData.full_degree % 30)) * 60),
    house: planetData.house,
  });
  
  // Trouver chaque planète
  const sun = planets.find(p => p.name === 'Sun');
  const moon = planets.find(p => p.name === 'Moon');
  const mercury = planets.find(p => p.name === 'Mercury');
  const venus = planets.find(p => p.name === 'Venus');
  const mars = planets.find(p => p.name === 'Mars');
  const jupiter = planets.find(p => p.name === 'Jupiter');
  const saturn = planets.find(p => p.name === 'Saturn');
  
  const positions = {
    sun: sun ? formatPosition(sun) : null,
    moon: moon ? formatPosition(moon) : null,
    ascendant: ascendant ? formatPosition(ascendant) : null,
    mercury: mercury ? formatPosition(mercury) : null,
    venus: venus ? formatPosition(venus) : null,
    mars: mars ? formatPosition(mars) : null,
    jupiter: jupiter ? formatPosition(jupiter) : null,
    saturn: saturn ? formatPosition(saturn) : null,
  };
  
  return {
    chart: positions,
    positions,
    houses: houses || [],
    aspects: aspects || [],
    meta: {
      version: 'AstrologyAPI v3',
      precision: 'professional',
      source: 'Swiss Ephemeris',
    },
  };
}

/**
 * Handler Vercel
 */
export default async function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }
  
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  
  try {
    const { date, time, lat, lon, tz } = req.body;
    
    // Validation
    if (!date || !time || lat === undefined || lon === undefined) {
      return res.status(400).json({
        error: 'Missing required fields: date, time, lat, lon',
      });
    }
    
    // Calculer le thème natal
    const natalChart = await computeNatalChart({ date, time, lat, lon, tz });
    
    return res.status(200).json(natalChart);
  } catch (error) {
    console.error('[natal-astrologyapi] Error:', error);
    return res.status(500).json({
      error: error.message || 'Internal server error',
      details: process.env.NODE_ENV === 'development' ? error.stack : undefined,
    });
  }
}

