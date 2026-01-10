/**
 * Service pour la lecture complète de thème natal
 * Utilise le backend FastAPI avec cache intelligent
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import Constants from 'expo-constants';
import { Platform } from 'react-native';

// Configuration - Utiliser l'URL depuis app.json ou fallback
// Pour iOS Simulator, utiliser localhost
// Pour Android/device physique, utiliser l'IP locale de votre machine
const getApiBaseUrl = () => {
  // 1. En dev, utiliser la config depuis app.json ou IP locale par défaut
  if (__DEV__) {
    // Utiliser la config depuis app.json si disponible
    if (Constants.expoConfig?.extra?.fastApiUrl) {
      return Constants.expoConfig.extra.fastApiUrl;
    }
    // Fallback : IP locale (fonctionne pour iOS Simulator ET device physique)
    return 'http://192.168.0.150:8000';
  }
  
  // 2. Production : utiliser la config ou URL de prod
  if (Constants.expoConfig?.extra?.fastApiUrl) {
    return Constants.expoConfig.extra.fastApiUrl;
  }
  
  return 'https://ton-api-prod.com';
};

const FASTAPI_BASE_URL = getApiBaseUrl();

// Log de debug pour voir quelle URL est utilisée
if (__DEV__) {
  console.log('[NatalReading] API URL configurée:', FASTAPI_BASE_URL, 'Platform:', Platform.OS);
}

/**
 * Récupère ou génère une lecture complète de thème natal
 * @param {Object} birthData - Données de naissance
 * @param {Object} options - Options (language, force_refresh)
 * @returns {Promise<Object>} - Lecture natale complète
 */
export async function getNatalReading(birthData, options = {}) {
  try {
    console.log('[NatalReading] 📖 Demande lecture natal...', birthData.city);
    
    const payload = {
      birth_data: {
        year: birthData.year,
        month: birthData.month,
        day: birthData.day,
        hour: birthData.hour,
        minute: birthData.minute,
        second: birthData.second || 0,
        city: birthData.city,
        country_code: birthData.country_code || 'FR',
        latitude: birthData.latitude,
        longitude: birthData.longitude,
        timezone: birthData.timezone || 'Europe/Paris'
      },
      options: {
        language: options.language || 'fr',
        force_refresh: options.force_refresh || false,
        include_interpretations: options.include_interpretations !== false // true par défaut
      }
    };

    const response = await fetch(`${FASTAPI_BASE_URL}/api/natal/reading`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    // Vérifier le Content-Type avant de parser
    const contentType = response.headers.get('content-type') || '';
    const isJson = contentType.includes('application/json');

    // Lire le texte brut d'abord (on ne peut le lire qu'une fois)
    const responseText = await response.text().catch(() => 'Réponse vide');

    if (!response.ok) {
      // Si c'est du JSON, essayer de parser
      let errorText = `HTTP ${response.status}`;
      if (isJson && responseText) {
        try {
          const errorData = JSON.parse(responseText);
          errorText = errorData.detail || errorData.message || errorText;
        } catch (parseError) {
          // Si le parsing échoue, utiliser le texte brut
          errorText = responseText.substring(0, 200);
        }
      } else if (responseText) {
        errorText = responseText.substring(0, 200);
      }
      console.error('[NatalReading] ⚠️ Erreur HTTP:', response.status, 'Réponse:', responseText.substring(0, 200));
      throw new Error(errorText);
    }

    // Parser la réponse JSON si possible
    let data;
    if (isJson) {
      try {
        data = JSON.parse(responseText);
      } catch (parseError) {
        console.error('[NatalReading] ⚠️ Erreur parsing JSON (premiers 200 caractères):', responseText.substring(0, 200));
        throw new Error(`L'API a retourné une réponse invalide (pas du JSON). Réponse reçue: ${responseText.substring(0, 100)}...`);
      }
    } else {
      console.error('[NatalReading] ⚠️ Réponse non-JSON (Content-Type: ' + contentType + ')');
      console.error('[NatalReading] ⚠️ Réponse (premiers 200 caractères):', responseText.substring(0, 200));
      throw new Error(`L'API a retourné une réponse invalide (pas du JSON). Content-Type: ${contentType}`);
    }
    
    console.log('[NatalReading] ✅ Lecture reçue:', {
      positions: data.positions?.length || 0,
      aspects: data.aspects?.length || 0,
      source: data.source,
      api_calls: data.api_calls_count
    });

    return data;

  } catch (error) {
    console.error('[NatalReading] ❌ Erreur:', error.message);
    console.error('[NatalReading] ❌ Stack:', error.stack);
    
    // Message d'erreur plus explicite selon le type d'erreur
    if (error.message === 'Network request failed' || error.message.includes('Network')) {
      const errorMessage = `Impossible de se connecter à l'API backend.\n\nVérifiez que:\n1. L'API backend est démarrée (uvicorn)\n2. L'URL est correcte: ${FASTAPI_BASE_URL}\n3. Votre appareil et votre ordinateur sont sur le même réseau WiFi`;
      console.error('[NatalReading]', errorMessage);
      throw new Error(errorMessage);
    }
    
    // Erreur de parsing JSON
    if (error.message.includes('JSON') || error.message.includes('Unexpected character')) {
      const errorMessage = `L'API backend a retourné une réponse invalide.\n\nVérifiez que:\n1. L'API backend est bien démarrée et fonctionne\n2. L'URL est correcte: ${FASTAPI_BASE_URL}\n3. Le serveur n'a pas d'erreur (voir les logs backend)`;
      console.error('[NatalReading] Erreur de parsing JSON:', error.message);
      throw new Error(errorMessage);
    }
    
    throw error;
  }
}

/**
 * Sauvegarde la lecture en local pour accès rapide
 * @param {Object} reading - Lecture à sauvegarder
 */
export async function saveReadingLocally(reading) {
  try {
    await AsyncStorage.setItem('natal_reading', JSON.stringify(reading));
    console.log('[NatalReading] 💾 Lecture sauvegardée localement');
  } catch (error) {
    console.error('[NatalReading] Erreur sauvegarde locale:', error);
  }
}

/**
 * Récupère la lecture sauvegardée localement
 * @returns {Promise<Object|null>} - Lecture ou null
 */
export async function getLocalReading() {
  try {
    const data = await AsyncStorage.getItem('natal_reading');
    return data ? JSON.parse(data) : null;
  } catch (error) {
    console.error('[NatalReading] Erreur lecture locale:', error);
    return null;
  }
}

/**
 * Filtre les aspects par force
 * @param {Array} aspects - Liste complète des aspects
 * @param {String} minStrength - Force minimale ('strong', 'medium', 'weak')
 * @returns {Array} - Aspects filtrés
 */
export function filterAspectsByStrength(aspects, minStrength = 'medium') {
  const strengthOrder = { strong: 3, medium: 2, weak: 1 };
  const minLevel = strengthOrder[minStrength] || 2;
  
  return aspects.filter(asp => strengthOrder[asp.strength] >= minLevel);
}

/**
 * Formate un aspect pour l'affichage
 * @param {Object} aspect - Aspect à formater
 * @returns {String} - Format lisible
 */
export function formatAspect(aspect) {
  // Importer depuis astrologyTranslations pour cohérence
  const { translateAspect, translatePlanet } = require('../utils/astrologyTranslations');
  
  const typeName = translateAspect(aspect.aspect_type);
  const orbStr = Math.abs(aspect.orb).toFixed(2);
  const planetFrom = translatePlanet(aspect.from);
  const planetTo = translatePlanet(aspect.to);
  
  return `${planetFrom} ${typeName} ${planetTo} (${orbStr}°)`;
}

