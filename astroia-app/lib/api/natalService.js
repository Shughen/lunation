import Constants from 'expo-constants';
import { supabase } from '@/lib/supabase';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Configuration des URLs d'API
const API_BASE = Constants.expoConfig?.extra?.aiApiUrl?.replace('/api/ai/chat', '') || 'http://localhost:3000';
const GEOCODE_URL = `${API_BASE}/api/geo/geocode`;
const TIMEZONE_URL = `${API_BASE}/api/geo/timezone`;
const NATAL_URL = `${API_BASE}/api/astro/natal`; // V2 Enhanced - Gratuit

/**
 * Service pour gérer les thèmes natals
 */
class NatalService {
  /**
   * Géocoder un lieu
   * @param {string} place - Ex: "Paris, France"
   * @returns {Promise<{lat, lon, formatted, city, country}>}
   */
  async geocodePlace(place) {
    try {
      const response = await fetch(GEOCODE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: place }),
      });

      if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        if (response.status === 404) {
          throw new Error('Lieu introuvable. Vérifiez l\'orthographe et réessayez avec un format comme "Ville, Pays".');
        }
        if (response.status >= 500) {
          throw new Error('Service de géocodage temporairement indisponible. Réessayez plus tard.');
        }
        throw new Error(error.message || 'Erreur lors de la recherche du lieu. Vérifiez votre connexion.');
      }

      return await response.json();
    } catch (error) {
      console.error('[NatalService] Geocode error:', error);
      throw error;
    }
  }

  /**
   * Obtenir le fuseau horaire
   * @param {number} lat
   * @param {number} lon
   * @returns {Promise<{iana, offset, name}>}
   */
  async getTimezone(lat, lon) {
    try {
      const response = await fetch(TIMEZONE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lat, lon }),
      });

      if (!response.ok) {
        if (response.status >= 500) {
          throw new Error('Service de fuseau horaire temporairement indisponible.');
        }
        throw new Error('Impossible de déterminer le fuseau horaire pour ce lieu.');
      }

      return await response.json();
    } catch (error) {
      console.error('[NatalService] Timezone error:', error);
      throw error;
    }
  }

  /**
   * Calculer le thème natal
   * @param {Object} birthData
   * @returns {Promise<Object>}
   */
  async computeNatalChart(birthData) {
    try {
      const { birthDate, birthTime, birthPlace, lat, lon, tz } = birthData;

      // Formater la date et l'heure pour l'API
      // FIX : Utiliser directement les composants locaux sans conversion UTC
      
      const birthDateObj = new Date(birthDate);
      const birthTimeObj = new Date(birthTime);
      
      // CORRECTION : Utiliser getDate() (local) au lieu de getUTCDate()
      // Cela évite le décalage de jour causé par la conversion UTC
      const year = birthDateObj.getFullYear();
      const month = String(birthDateObj.getMonth() + 1).padStart(2, '0');
      const day = String(birthDateObj.getDate()).padStart(2, '0');
      const dateStr = `${year}-${month}-${day}`;
      
      // CORRECTION : Utiliser getHours()/getMinutes() (local) au lieu de getUTCHours()/getUTCMinutes()
      const hours = String(birthTimeObj.getHours()).padStart(2, '0');
      const minutes = String(birthTimeObj.getMinutes()).padStart(2, '0');
      const timeStr = `${hours}:${minutes}`;
      
      console.log('[NatalService] Date saisie:', { year, month, day });
      console.log('[NatalService] Heure saisie:', { hours, minutes });
      console.log('[NatalService] Envoi à l\'API:', { dateStr, timeStr, lat, lon, tz });

      const response = await fetch(NATAL_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          date: dateStr,
          time: timeStr,
          lat,
          lon,
          tz,
        }),
      });

      if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        if (response.status === 429) {
          throw new Error('Trop de calculs aujourd\'hui. Veuillez réessayer demain.');
        }
        if (response.status >= 500) {
          throw new Error('Service de calcul astrologique temporairement indisponible. Réessayez plus tard.');
        }
        if (response.status === 400) {
          throw new Error(error.message || 'Données invalides. Vérifiez votre date et lieu de naissance.');
        }
        throw new Error(error.message || `Erreur lors du calcul du thème natal (${response.status}).`);
      }

      return await response.json();
    } catch (error) {
      console.error('[NatalService] Compute error:', error);
      
      // Améliorer les messages d'erreur réseau
      if (error.message && (error.message.includes('Failed to fetch') || error.message.includes('Network'))) {
        throw new Error('Pas de connexion internet. Vérifiez votre réseau et réessayez.');
      }
      
      // Si l'erreur a déjà un message explicite, la renvoyer
      if (error.message && !error.message.includes('Error')) {
        throw error;
      }
      
      throw new Error(`Impossible de calculer le thème natal. ${error.message || 'Veuillez réessayer.'}`);
    }
  }

  /**
   * Calculer et sauvegarder le thème natal pour l'utilisateur connecté
   * Mode local si non authentifié (pas de sauvegarde Supabase)
   * @param {Object} profileData
   * @returns {Promise<Object>}
   */
  async computeNatalChartForCurrentUser(profileData) {
    try {
      const { data: { user } } = await supabase.auth.getUser();

      // Calculer le thème natal via l'API
      const natalData = await this.computeNatalChart(profileData);
      
      // Si connecté, sauvegarder dans Supabase
      if (user) {
        try {
          // Vérifier la limite (1 calcul/24h)
          const canCompute = await this.canComputeToday(user.id);
          if (!canCompute) {
            throw new Error('Vous avez déjà calculé votre thème aujourd\'hui. Revenez demain !');
          }

          // Sauvegarder dans Supabase
          const { data, error } = await supabase
            .from('natal_charts')
            .insert({
              user_id: user.id,
              birth_date: profileData.birthDate.toISOString().split('T')[0],
              birth_time: `${profileData.birthTime.getHours()}:${profileData.birthTime.getMinutes()}:00`,
              birth_place: profileData.birthPlace,
              latitude: profileData.lat,
              longitude: profileData.lon,
              timezone: profileData.tz,
              positions: natalData.chart,
              version: natalData.meta.version,
            })
            .select()
            .single();

          if (error) {
            console.warn('[NatalService] Supabase save failed, continuing in local mode:', error);
          } else {
            return { ...data, ...natalData };
          }
        } catch (supabaseError) {
          console.warn('[NatalService] Supabase error, continuing in local mode:', supabaseError);
        }
      }

      // Mode local : sauvegarder dans AsyncStorage et retourner les données
      console.log('[NatalService] Mode local - Saving to AsyncStorage');
      const localResult = {
        ...natalData,
        id: 'local-' + Date.now(),
        computed_at: new Date().toISOString(),
        local: true, // Flag pour indiquer mode local
      };
      
      await AsyncStorage.setItem('natal_chart_local', JSON.stringify(localResult));
      
      return localResult;
    } catch (error) {
      console.error('[NatalService] Compute for user error:', error);
      throw error;
    }
  }

  /**
   * Récupérer le dernier thème natal de l'utilisateur
   * Vérifie d'abord AsyncStorage (mode local), puis Supabase si connecté
   * @returns {Promise<Object|null>}
   */
  async getLatestNatalChart() {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      // 1. Vérifier AsyncStorage (mode local ou backup)
      const localChart = await AsyncStorage.getItem('natal_chart_local');
      
      if (localChart) {
        console.log('[NatalService] Loaded from AsyncStorage');
        return JSON.parse(localChart);
      }
      
      // 2. Mode connecté : récupérer depuis Supabase
      if (!user) {
        console.log('[NatalService] No local chart and not authenticated');
        return null;
      }

      const { data, error } = await supabase
        .from('natal_charts')
        .select('*')
        .eq('user_id', user.id)
        .order('computed_at', { ascending: false })
        .limit(1)
        .single();

      if (error && error.code !== 'PGRST116') {
        console.warn('[NatalService] Error fetching chart:', error);
        return null;
      }

      return data;
    } catch (error) {
      console.error('[NatalService] Get latest error:', error);
      return null;
    }
  }

  /**
   * Vérifier si l'utilisateur peut calculer aujourd'hui
   * @param {string} userId
   * @returns {Promise<boolean>}
   */
  async canComputeToday(userId) {
    try {
      const { data, error } = await supabase
        .rpc('can_compute_natal_chart', { p_user_id: userId });

      if (error) {
        console.warn('[NatalService] Cannot check limit, allowing:', error);
        return true; // En cas d'erreur, autoriser
      }

      return data;
    } catch (error) {
      console.warn('[NatalService] Cannot check limit, allowing:', error);
      return true;
    }
  }
}

export const natalService = new NatalService();

