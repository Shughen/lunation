// ============================================
// CALCUL DU THÈME NATAL V3 - ARCHITECTURE MODULAIRE
// ============================================
// Supporte plusieurs providers: local, Prokerala, Astrologer API
// Provider par défaut: LOCAL (gratuit, auto-hébergé)

import { calculateNatalChart } from './natal-providers.js';

// ============================================
// HANDLER PRINCIPAL
// ============================================

export default async function handler(req, res) {
  const startTime = Date.now();

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { date, time, lat, lon, tz = 'UTC', provider } = req.body;

    if (!date || !time || lat === undefined || lon === undefined) {
      return res.status(400).json({
        error: 'Validation error',
        message: 'date, time, lat, lon sont requis',
      });
    }

    console.log(`[Natal] Calculating for: ${date} ${time} at ${lat},${lon}`);

    // Calculer avec le provider configuré ou spécifié
    const result = await calculateNatalChart({
      date,
      time,
      lat,
      lon,
      tz,
      provider,
    });

    const latencyMs = Date.now() - startTime;

    console.log(`[Natal] Success - Provider: ${result.meta.provider}`);
    console.log(`[Natal] Sun: ${result.positions.sun.sign}, Moon: ${result.positions.moon.sign}, Asc: ${result.positions.ascendant.sign}`);

    return res.status(200).json({
      chart: result.positions,
      positions: result.positions, // Alias pour compatibilité
      meta: {
        ...result.meta,
        birthDate: date,
        birthTime: time,
        location: { lat, lon },
        timezone: tz,
        version: 'V3-modular',
      },
      latencyMs,
    });

  } catch (error) {
    console.error('[Natal] Error:', error);

    return res.status(500).json({
      error: 'Internal server error',
      message: error.message || 'Erreur lors du calcul',
      stack: process.env.NODE_ENV === 'development' ? error.stack : undefined,
    });
  }
}
