// ============================================
// API TIMEZONE - Détection du fuseau horaire
// ============================================
// Utilise TimeZoneDB API (gratuit avec clé)
// Alternative : tz-lookup en local (offline)

export default async function handler(req, res) {
  // CORS preflight
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { lat, lon } = req.body;

    if (lat === undefined || lon === undefined) {
      return res.status(400).json({
        error: 'Validation error',
        message: 'Les coordonnées lat/lon sont requises',
      });
    }

    console.log(`[Timezone] Request for: ${lat}, ${lon}`);

    // Utiliser TimeAPI.io (gratuit, pas de clé requise)
    const timeApiUrl = `https://timeapi.io/api/TimeZone/coordinate?latitude=${lat}&longitude=${lon}`;

    const response = await fetch(timeApiUrl);

    if (!response.ok) {
      throw new Error(`TimeAPI error: ${response.status}`);
    }

    const data = await response.json();

    const timezone = {
      iana: data.timeZone || 'UTC',
      offset: data.currentUtcOffset?.seconds ? data.currentUtcOffset.seconds / 3600 : 0,
      name: data.timeZone || 'UTC',
    };

    console.log(`[Timezone] Success: ${timezone.iana}`);

    return res.status(200).json(timezone);

  } catch (error) {
    console.error('[Timezone] Error:', error);

    // Fallback : estimation basique par longitude
    const { lon } = req.body;
    const estimatedOffset = Math.round(lon / 15);
    const fallbackTz = `Etc/GMT${estimatedOffset >= 0 ? '-' : '+'}${Math.abs(estimatedOffset)}`;

    console.log(`[Timezone] Fallback: ${fallbackTz}`);

    return res.status(200).json({
      iana: fallbackTz,
      offset: estimatedOffset,
      name: fallbackTz,
      warning: 'Estimation approximative du fuseau horaire',
    });
  }
}

