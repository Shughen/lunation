// ============================================
// NATAL CHART - EPHEMERIS-API PROVIDER
// ============================================
// Appelle une instance ephemeris-api (Swiss Ephemeris)
// Gratuit si self-hosted sur Railway/Render/Heroku
// Précision professionnelle

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
 * Calculer un thème natal avec ephemeris-api
 */
export async function calculateEphemerisAPI(params) {
  const { date, time, lat, lon, tz } = params;

  try {
    // URL de l'instance ephemeris-api
    const apiUrl = process.env.EPHEMERIS_API_URL;
    
    if (!apiUrl) {
      throw new Error('EPHEMERIS_API_URL not configured. Deploy ephemeris-api first!');
    }

    // Parser date et heure
    const [year, month, day] = date.split('-').map(Number);
    const [hours, minutes] = time.split(':').map(Number);

    console.log('[Ephemeris-API] Calling:', apiUrl);
    console.log('[Ephemeris-API] Data:', { year, month, day, hours, minutes, lat, lon });

    // Convertir l'heure locale en UTC
    let utcHours = hours;
    let utcDay = day;
    
    const timezoneOffsets = {
      'America/Manaus': 4,
      'America/Sao_Paulo': 3,
      'Europe/Paris': -1,
      'America/New_York': 5,
    };
    
    const offset = timezoneOffsets[tz] || 0;
    utcHours = hours + offset;
    
    if (utcHours >= 24) {
      utcHours -= 24;
      utcDay += 1;
    } else if (utcHours < 0) {
      utcHours += 24;
      utcDay -= 1;
    }

    const hourDecimal = utcHours + minutes / 60.0;

    // Appeler l'API ephemeris
    const response = await fetch(`${apiUrl}/calc`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        year,
        month,
        day: utcDay,
        hour: hourDecimal,
        latitude: lat,
        longitude: lon,
        houses: 'Placidus',
      }),
    });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`Ephemeris API error: ${response.status} - ${error}`);
    }

    const data = await response.json();

    console.log('[Ephemeris-API] Response:', data);

    // Mapper les données vers notre format
    const sun = longitudeToZodiac(data.sun.longitude || data.sun);
    const moon = longitudeToZodiac(data.moon.longitude || data.moon);
    const ascendant = longitudeToZodiac(data.ascendant.longitude || data.ascendant || data.asc);
    const mercury = longitudeToZodiac(data.mercury?.longitude || data.mercury || 0);
    const venus = longitudeToZodiac(data.venus?.longitude || data.venus || 0);
    const mars = longitudeToZodiac(data.mars?.longitude || data.mars || 0);

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
        provider: 'ephemeris-api',
        cost: 0,
        precision: 'Professionnelle (Swiss Ephemeris)',
        api_url: apiUrl,
        note: 'API self-hosted gratuite - Même précision qu\'Astrotheme',
      },
    };
  } catch (error) {
    console.error('[Ephemeris-API] Error:', error);
    throw error;
  }
}

