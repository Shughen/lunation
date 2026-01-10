/**
 * Service ML - Analyse Parent-Enfant
 * Utilise le modèle XGBoost optimisé (98.19% précision)
 */

import Constants from 'expo-constants';

const API_URL = Constants.expoConfig?.extra?.parentChildApiUrl || 
  'https://astro-ia-niei71xao-remibeaurain-4057s-projects.vercel.app/api/ml/parent-child';

/**
 * Calcule la compatibilité parent-enfant avec le modèle ML
 * @param {Object} parentData - Données astrologiques du parent
 * @param {Object} enfantData - Données astrologiques de l'enfant
 * @param {Object} additionalData - Données complémentaires (âge, etc.)
 */
export async function analyzeParentChildCompatibility(parentData, enfantData, additionalData = {}) {
  try {
    const payload = {
      parent: {
        sun_sign: parentData.sunSign || 1,
        moon_sign: parentData.moonSign || 1,
        ascendant: parentData.ascendant || 1,
        mercury: parentData.mercury || 1,
        venus: parentData.venus || 1,
        mars: parentData.mars || 1,
      },
      enfant: {
        sun_sign: enfantData.sunSign || 1,
        moon_sign: enfantData.moonSign || 1,
        ascendant: enfantData.ascendant || 1,
        mercury: enfantData.mercury || 1,
        venus: enfantData.venus || 1,
        mars: enfantData.mars || 1,
      },
      age_diff: additionalData.ageDiff || 25,
      house_overlap: additionalData.houseOverlap || 0.5,
      moon_phase_birth: additionalData.moonPhaseBirth || 0.5,
      karmic_nodes: additionalData.karmicNodes || 0.0,
    };

    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`API Error ${response.status}: ${errorText}`);
    }

    const result = await response.json();

    if (!result.success) {
      throw new Error(result.error || 'Analyse échouée');
    }

    return result;
  } catch (error) {
    console.error('[parentChildService] Error:', error);
    throw error;
  }
}

/**
 * Convertit un signe zodiacal en numéro (1-12)
 */
export function zodiacSignToNumber(signName) {
  const signs = {
    'belier': 1,
    'taureau': 2,
    'gemeaux': 3,
    'cancer': 4,
    'lion': 5,
    'vierge': 6,
    'balance': 7,
    'scorpion': 8,
    'sagittaire': 9,
    'capricorne': 10,
    'verseau': 11,
    'poissons': 12,
  };
  return signs[signName.toLowerCase()] || 1;
}

/**
 * Convertit un numéro en signe zodiacal
 */
export function numberToZodiacSign(num) {
  const signs = [
    '', 'Bélier', 'Taureau', 'Gémeaux', 'Cancer', 'Lion', 'Vierge',
    'Balance', 'Scorpion', 'Sagittaire', 'Capricorne', 'Verseau', 'Poissons'
  ];
  return signs[num] || 'Inconnu';
}

/**
 * Extrait les données astrologiques depuis un profil utilisateur
 */
export function extractAstroData(profile) {
  if (!profile) return null;

  // Si le profil a un natal chart calculé
  if (profile.natalChart && profile.natalChart.positions) {
    const positions = profile.natalChart.positions;
    return {
      sunSign: zodiacSignToNumber(positions.sun?.sign || 'belier'),
      moonSign: zodiacSignToNumber(positions.moon?.sign || 'belier'),
      ascendant: zodiacSignToNumber(positions.ascendant?.sign || 'belier'),
      mercury: zodiacSignToNumber(positions.mercury?.sign || 'belier'),
      venus: zodiacSignToNumber(positions.venus?.sign || 'belier'),
      mars: zodiacSignToNumber(positions.mars?.sign || 'belier'),
    };
  }

  // Sinon, calcul basique depuis la date de naissance
  if (profile.birthDate) {
    const sunSign = calculateSunSign(profile.birthDate);
    return {
      sunSign: zodiacSignToNumber(sunSign),
      moonSign: 1,  // Par défaut
      ascendant: 1,
      mercury: zodiacSignToNumber(sunSign),
      venus: zodiacSignToNumber(sunSign),
      mars: zodiacSignToNumber(sunSign),
    };
  }

  return null;
}

/**
 * Calcule le signe solaire depuis une date
 */
function calculateSunSign(dateString) {
  const date = new Date(dateString);
  const month = date.getMonth() + 1;
  const day = date.getDate();

  if ((month === 3 && day >= 21) || (month === 4 && day <= 19)) return 'belier';
  if ((month === 4 && day >= 20) || (month === 5 && day <= 20)) return 'taureau';
  if ((month === 5 && day >= 21) || (month === 6 && day <= 20)) return 'gemeaux';
  if ((month === 6 && day >= 21) || (month === 7 && day <= 22)) return 'cancer';
  if ((month === 7 && day >= 23) || (month === 8 && day <= 22)) return 'lion';
  if ((month === 8 && day >= 23) || (month === 9 && day <= 22)) return 'vierge';
  if ((month === 9 && day >= 23) || (month === 10 && day <= 22)) return 'balance';
  if ((month === 10 && day >= 23) || (month === 11 && day <= 21)) return 'scorpion';
  if ((month === 11 && day >= 22) || (month === 12 && day <= 21)) return 'sagittaire';
  if ((month === 12 && day >= 22) || (month === 1 && day <= 19)) return 'capricorne';
  if ((month === 1 && day >= 20) || (month === 2 && day <= 18)) return 'verseau';
  return 'poissons';
}

export default {
  analyzeParentChildCompatibility,
  zodiacSignToNumber,
  numberToZodiacSign,
  extractAstroData,
};

