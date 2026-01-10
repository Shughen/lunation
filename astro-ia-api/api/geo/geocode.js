// ============================================
// API GÉOCODAGE - Nominatim (OpenStreetMap)
// ============================================
// Pas de clé API requise, service gratuit et open-source

export default async function handler(req, res) {
  // CORS preflight
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { query } = req.body;

    if (!query || typeof query !== 'string' || query.trim().length === 0) {
      return res.status(400).json({
        error: 'Validation error',
        message: 'Le champ "query" est requis (ex: "Paris, France")',
      });
    }

    console.log(`[Geocode] Request for: ${query}`);

    // Appel à Nominatim (OpenStreetMap)
    const nominatimUrl = `https://nominatim.openstreetmap.org/search?` + new URLSearchParams({
      q: query,
      format: 'json',
      limit: '1',
      addressdetails: '1',
    });

    const response = await fetch(nominatimUrl, {
      headers: {
        'User-Agent': 'Astro.IA/1.0', // Requis par Nominatim
      },
    });

    if (!response.ok) {
      throw new Error(`Nominatim error: ${response.status}`);
    }

    const data = await response.json();

    if (!data || data.length === 0) {
      return res.status(404).json({
        error: 'Not found',
        message: 'Lieu introuvable. Essayez "Ville, Pays" (ex: "Lyon, France")',
      });
    }

    const result = data[0];

    // Formater la réponse
    const formatted = {
      lat: parseFloat(result.lat),
      lon: parseFloat(result.lon),
      formatted: result.display_name,
      city: result.address?.city || result.address?.town || result.address?.village || '',
      country: result.address?.country || '',
    };

    console.log(`[Geocode] Success: ${formatted.formatted}`);

    return res.status(200).json(formatted);

  } catch (error) {
    console.error('[Geocode] Error:', error);

    return res.status(500).json({
      error: 'Internal server error',
      message: 'Erreur lors du géocodage. Réessayez.',
    });
  }
}

