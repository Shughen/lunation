/**
 * Service de géocodage - Convertit ville/pays en coordonnées GPS
 * Utilise OpenStreetMap Nominatim (gratuit, pas de clé API nécessaire)
 */

/**
 * Recherche une ville et retourne ses coordonnées
 * @param {String} city - Nom de la ville
 * @param {String} country - Code pays (FR, BR, US, etc.)
 * @returns {Promise<Object>} - { latitude, longitude, timezone, display_name }
 */
export async function searchCity(city, country = '') {
  try {
    console.log(`[Geocoding] 🔍 Recherche: ${city}, ${country}`);

    // ÉTAPE 1: Chercher d'abord dans les villes populaires (instant + fiable)
    // Parser la recherche (ex: "Manaus, Brésil" → ville="Manaus", pays="Brésil")
    const cityLower = city.toLowerCase().trim();
    const cityParts = cityLower.split(',').map(p => p.trim());
    const cityName = cityParts[0];
    const countryName = cityParts[1] || country.toLowerCase();

    const popularMatch = POPULAR_CITIES.find(c => {
      const cName = c.name.toLowerCase();
      const cCountry = c.country.toLowerCase();
      
      // Match par nom de ville seul
      if (cName === cityName) return true;
      
      // Match par nom + pays (ex: "manaus, brésil" ou "manaus, br")
      if (countryName) {
        // Mapping pays FR → codes
        const countryMap = {
          'france': 'fr', 'brésil': 'br', 'brazil': 'br', 'usa': 'us', 
          'états-unis': 'us', 'royaume-uni': 'gb', 'angleterre': 'gb',
          'japon': 'jp', 'canada': 'ca', 'belgique': 'be', 'suisse': 'ch'
        };
        const normalizedCountry = countryMap[countryName] || countryName;
        
        if (cName === cityName && (cCountry === normalizedCountry || normalizedCountry.includes(cCountry))) {
          return true;
        }
      }
      
      return false;
    });

    if (popularMatch) {
      console.log(`[Geocoding] ✅ Trouvé dans villes populaires: ${popularMatch.name}`);
      return {
        latitude: popularMatch.lat,
        longitude: popularMatch.lon,
        timezone: popularMatch.tz,
        display_name: `${popularMatch.name}, ${getCountryName(popularMatch.country)}`,
        country_code: popularMatch.country,
        all_results: [popularMatch],
      };
    }

    // ÉTAPE 2: Appeler Nominatim si pas trouvé
    const query = country ? `${city}, ${country}` : city;
    const url = `https://nominatim.openstreetmap.org/search?` +
      `q=${encodeURIComponent(query)}&` +
      `format=json&` +
      `limit=5&` +
      `addressdetails=1&` +
      `accept-language=fr`;  // Préférer les noms en français

    const response = await fetch(url, {
      headers: {
        'User-Agent': 'AstroiaApp/1.0',
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const results = await response.json();

    if (results.length === 0) {
      throw new Error('Aucune ville trouvée');
    }

    // Filtrer les résultats bizarres (type=city ou type=town uniquement)
    const validResults = results.filter(r => 
      r.type === 'city' || 
      r.type === 'town' || 
      r.type === 'village' ||
      r.class === 'place'
    );

    const place = validResults.length > 0 ? validResults[0] : results[0];
    const lat = parseFloat(place.lat);
    const lon = parseFloat(place.lon);
    const timezone = guessTimezoneFromCoords(lat, lon);

    console.log(`[Geocoding] ✅ Trouvé: ${place.display_name} (${lat}, ${lon})`);

    return {
      latitude: lat,
      longitude: lon,
      timezone: timezone,
      display_name: place.display_name,
      country_code: place.address?.country_code?.toUpperCase() || 'XX',
      all_results: validResults.slice(0, 3).map(r => ({
        name: r.display_name,
        lat: parseFloat(r.lat),
        lon: parseFloat(r.lon),
        type: r.type,
      })),
    };

  } catch (error) {
    console.error('[Geocoding] ❌ Erreur:', error.message);
    throw error;
  }
}

/**
 * Devine le timezone depuis les coordonnées GPS (mapping simplifié)
 * @param {Number} lat - Latitude
 * @param {Number} lon - Longitude
 * @returns {String} - Timezone IANA
 */
function guessTimezoneFromCoords(lat, lon) {
  // Mapping par longitude (simplifié mais fonctionnel)
  // Source: https://en.wikipedia.org/wiki/List_of_UTC_offsets
  
  // Europe (lon: -10 à 40)
  if (lon >= -10 && lon <= 10) return 'Europe/Paris';  // UTC+1
  if (lon >= 10 && lon <= 30) return 'Europe/Berlin';  // UTC+1/2
  if (lon >= 30 && lon <= 45) return 'Europe/Moscow';  // UTC+3
  
  // Amériques
  if (lon >= -130 && lon <= -120) return 'America/Los_Angeles';  // UTC-8
  if (lon >= -120 && lon <= -105) return 'America/Denver';  // UTC-7
  if (lon >= -105 && lon <= -90) return 'America/Chicago';  // UTC-6
  if (lon >= -90 && lon <= -60) return 'America/New_York';  // UTC-5
  if (lon >= -75 && lon <= -34) {
    // Amérique du Sud
    if (lat < -15) return 'America/Sao_Paulo';  // Brésil Sud
    return 'America/Manaus';  // Brésil Nord/Amazonie
  }
  
  // Asie
  if (lon >= 100 && lon <= 110) return 'Asia/Bangkok';  // UTC+7
  if (lon >= 110 && lon <= 125) return 'Asia/Shanghai';  // UTC+8
  if (lon >= 125 && lon <= 145) return 'Asia/Tokyo';  // UTC+9
  if (lon >= 145 && lon <= 180) return 'Pacific/Auckland';  // UTC+12
  
  // Afrique
  if (lon >= -5 && lon <= 15 && lat >= -35 && lat <= 37) return 'Africa/Cairo';
  
  // Défaut
  return 'UTC';
}

/**
 * Mapping codes pays → noms français
 */
function getCountryName(code) {
  const names = {
    FR: 'France',
    BR: 'Brésil',
    US: 'États-Unis',
    GB: 'Royaume-Uni',
    CA: 'Canada',
    BE: 'Belgique',
    CH: 'Suisse',
    JP: 'Japon',
    DE: 'Allemagne',
    IT: 'Italie',
    ES: 'Espagne',
  };
  return names[code] || code;
}

/**
 * Villes prédéfinies populaires (autocomplete)
 * Ces villes sont garanties fiables (coords vérifiées)
 */
export const POPULAR_CITIES = [
  // France
  { name: 'Paris', country: 'FR', lat: 48.8566, lon: 2.3522, tz: 'Europe/Paris' },
  { name: 'Lyon', country: 'FR', lat: 45.7640, lon: 4.8357, tz: 'Europe/Paris' },
  { name: 'Marseille', country: 'FR', lat: 43.2965, lon: 5.3698, tz: 'Europe/Paris' },
  { name: 'Toulouse', country: 'FR', lat: 43.6047, lon: 1.4442, tz: 'Europe/Paris' },
  { name: 'Nice', country: 'FR', lat: 43.7102, lon: 7.2620, tz: 'Europe/Paris' },
  { name: 'Bordeaux', country: 'FR', lat: 44.8378, lon: -0.5792, tz: 'Europe/Paris' },
  { name: 'Lille', country: 'FR', lat: 50.6292, lon: 3.0573, tz: 'Europe/Paris' },
  { name: 'Strasbourg', country: 'FR', lat: 48.5734, lon: 7.7521, tz: 'Europe/Paris' },
  
  // Brésil
  { name: 'Manaus', country: 'BR', lat: -3.1190, lon: -60.0217, tz: 'America/Manaus' },
  { name: 'São Paulo', country: 'BR', lat: -23.5505, lon: -46.6333, tz: 'America/Sao_Paulo' },
  { name: 'Rio de Janeiro', country: 'BR', lat: -22.9068, lon: -43.1729, tz: 'America/Sao_Paulo' },
  { name: 'Brasília', country: 'BR', lat: -15.8267, lon: -47.9218, tz: 'America/Sao_Paulo' },
  
  // Autres
  { name: 'Londres', country: 'GB', lat: 51.5074, lon: -0.1278, tz: 'Europe/London' },
  { name: 'New York', country: 'US', lat: 40.7128, lon: -74.0060, tz: 'America/New_York' },
  { name: 'Los Angeles', country: 'US', lat: 34.0522, lon: -118.2437, tz: 'America/Los_Angeles' },
  { name: 'Tokyo', country: 'JP', lat: 35.6762, lon: 139.6503, tz: 'Asia/Tokyo' },
  { name: 'Montréal', country: 'CA', lat: 45.5017, lon: -73.5673, tz: 'America/Toronto' },
  { name: 'Bruxelles', country: 'BE', lat: 50.8503, lon: 4.3517, tz: 'Europe/Brussels' },
  { name: 'Genève', country: 'CH', lat: 46.2044, lon: 6.1432, tz: 'Europe/Zurich' },
];

/**
 * Recherche dans les villes populaires (instant, pas d'API)
 * @param {String} query - Recherche
 * @returns {Array} - Villes correspondantes
 */
export function searchPopularCities(query) {
  if (!query || query.length < 2) return [];
  
  const q = query.toLowerCase();
  return POPULAR_CITIES.filter(city => 
    city.name.toLowerCase().includes(q)
  ).slice(0, 5);
}

