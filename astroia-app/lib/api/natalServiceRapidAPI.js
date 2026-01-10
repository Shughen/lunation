import AsyncStorage from '@react-native-async-storage/async-storage';
import { supabase } from '@/lib/supabase';

/**
 * Service pour gérer les thèmes natals via le backend FastAPI + RapidAPI
 * Backend: astroia-lunar FastAPI
 */

// Configuration
// IMPORTANT: Utiliser l'IP locale de ton Mac, PAS localhost !
// Pour trouver ton IP: ifconfig | grep "inet " | grep -v 127.0.0.1
const FASTAPI_BASE_URL = __DEV__ 
  ? 'http://192.168.0.150:8000'  // ← Ton IP locale détectée automatiquement
  : 'https://ton-api-prod.com';  // URL de production

class NatalServiceRapidAPI {
  /**
   * Calculer le thème natal via FastAPI + RapidAPI
   * @param {Object} birthData
   * @returns {Promise<Object>}
   */
  async computeNatalChart(birthData) {
    try {
      const { birthDate, birthTime, birthPlace, lat, lon, tz } = birthData;

      // Formater les données pour RapidAPI (format attendu par le backend)
      const birthDateObj = new Date(birthDate);
      const birthTimeObj = new Date(birthTime);

      const year = birthDateObj.getFullYear();
      const month = birthDateObj.getMonth() + 1; // 1-12
      const day = birthDateObj.getDate();
      const hour = birthTimeObj.getHours();
      const minute = birthTimeObj.getMinutes();

      console.log('[NatalServiceRapidAPI] Données de naissance:', {
        year, month, day, hour, minute, lat, lon, tz
      });

      // Payload pour RapidAPI (format exact attendu par le backend FastAPI)
      const payload = {
        subject: {
          name: birthPlace || 'User',
          birth_data: {
            year,
            month,
            day,
            hour,
            minute,
            timezone: tz || 'Europe/Paris',
            latitude: parseFloat(lat),
            longitude: parseFloat(lon),
          },
        },
      };

      console.log('[NatalServiceRapidAPI] Payload envoyé:', JSON.stringify(payload, null, 2));

      // Appel au backend FastAPI
      const response = await fetch(`${FASTAPI_BASE_URL}/api/natal-chart/external`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error('[NatalServiceRapidAPI] Erreur API:', errorText);
        throw new Error(`Erreur API: ${response.status} - ${errorText}`);
      }

      const result = await response.json();
      console.log('[NatalServiceRapidAPI] Réponse brute:', JSON.stringify(result, null, 2));

      // Le backend retourne { provider, endpoint, data }
      const rapidApiData = result.data;
      console.log('[NatalServiceRapidAPI] RapidAPI data:', JSON.stringify(rapidApiData, null, 2));

      // Parser les données RapidAPI et les convertir au format attendu par l'app
      const parsedChart = this.parseRapidAPIResponse(rapidApiData);

      console.log('[NatalServiceRapidAPI] Chart parsé:', JSON.stringify(parsedChart, null, 2));

      return parsedChart;
    } catch (error) {
      console.error('[NatalServiceRapidAPI] Erreur:', error);
      throw error;
    }
  }

  /**
   * Parser la réponse RapidAPI et la convertir au format de l'app
   * @param {Object} rapidApiData - Données brutes de RapidAPI
   * @returns {Object}
   */
  parseRapidAPIResponse(rapidApiData) {
    try {
      // RapidAPI retourne : { subject_data: { sun: {}, moon: {}, ... }, chart_data: { ... } }
      const subjectData = rapidApiData.subject_data || rapidApiData;
      
      console.log('[Parser] subject_data.sun:', subjectData.sun);
      console.log('[Parser] subject_data.moon:', subjectData.moon);
      console.log('[Parser] subject_data.ascendant:', subjectData.ascendant);

      // Mapping des signes abrégés RapidAPI → français
      const signMapping = {
        'Ari': 'Bélier',
        'Tau': 'Taureau',
        'Gem': 'Gémeaux',
        'Can': 'Cancer',
        'Leo': 'Lion',
        'Vir': 'Vierge',
        'Lib': 'Balance',
        'Sco': 'Scorpion',
        'Sag': 'Sagittaire',
        'Cap': 'Capricorne',
        'Aqu': 'Verseau',
        'Pis': 'Poissons',
      };

      const emojiMapping = {
        'Ari': '♈', 'Tau': '♉', 'Gem': '♊', 'Can': '♋',
        'Leo': '♌', 'Vir': '♍', 'Lib': '♎', 'Sco': '♏',
        'Sag': '♐', 'Cap': '♑', 'Aqu': '♒', 'Pis': '♓',
      };

      // Fonction helper pour formater une position planétaire depuis subject_data
      const formatPosition = (planetData) => {
        if (!planetData) {
          console.warn('[Parser] planetData is null or undefined');
          return null;
        }
        
        const signAbr = planetData.sign; // Ex: "Sco", "Sag", "Aqu"
        const signFr = signMapping[signAbr] || signAbr;
        const element = planetData.element || 'Inconnu'; // Déjà en anglais: Water, Fire, etc.
        
        // Traduire l'élément en français
        const elementFr = {
          'Fire': 'Feu',
          'Earth': 'Terre',
          'Air': 'Air',
          'Water': 'Eau',
        }[element] || element;
        
        const degree = Math.floor(planetData.position);
        const minutes = Math.floor((planetData.position % 1) * 60);
        
        return {
          sign: signFr,
          emoji: planetData.emoji || emojiMapping[signAbr] || '⭐',
          element: elementFr,
          degree,
          minutes,
          longitude: planetData.abs_pos, // Longitude absolue (0-360)
        };
      };

      // Extraire les planètes depuis subject_data (structure directe)
      const chart = {
        sun: formatPosition(subjectData.sun),
        moon: formatPosition(subjectData.moon),
        ascendant: formatPosition(subjectData.ascendant),
        mercury: formatPosition(subjectData.mercury),
        venus: formatPosition(subjectData.venus),
        mars: formatPosition(subjectData.mars),
      };
      
      console.log('[Parser] Chart formaté:', chart);

      // Métadonnées
      const meta = {
        version: 'RapidAPI-v3',
        provider: 'best-astrology-api',
        computed_at: new Date().toISOString(),
      };

      return {
        chart,
        meta,
        raw: rapidApiData, // Garder les données brutes pour debug
      };
    } catch (error) {
      console.error('[NatalServiceRapidAPI] Erreur parsing:', error);
      throw new Error('Erreur lors du parsing des données astrologiques');
    }
  }


  /**
   * Calculer et sauvegarder le thème natal pour l'utilisateur connecté
   * @param {Object} profileData
   * @returns {Promise<Object>}
   */
  async computeNatalChartForCurrentUser(profileData) {
    try {
      const { data: { user } } = await supabase.auth.getUser();

      // Calculer le thème natal via RapidAPI
      const natalData = await this.computeNatalChart(profileData);

      // Mode local : toujours sauvegarder dans AsyncStorage
      console.log('[NatalServiceRapidAPI] Sauvegarde dans AsyncStorage');
      const localResult = {
        ...natalData,
        id: 'local-rapidapi-' + Date.now(),
        computed_at: new Date().toISOString(),
        local: true,
        positions: natalData.chart, // Alias pour compatibilité
        chart: natalData.chart, // Double alias pour être sûr
      };

      console.log('[NatalServiceRapidAPI] localResult.positions:', JSON.stringify(localResult.positions, null, 2));
      console.log('[NatalServiceRapidAPI] localResult.chart:', JSON.stringify(localResult.chart, null, 2));

      await AsyncStorage.setItem('natal_chart_rapidapi', JSON.stringify(localResult));

      // Si connecté, sauvegarder aussi dans Supabase
      if (user) {
        try {
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
              version: 'rapidapi-v3',
            })
            .select()
            .single();

          if (error) {
            console.warn('[NatalServiceRapidAPI] Supabase save failed:', error);
          } else {
            console.log('[NatalServiceRapidAPI] ✅ Sauvegardé dans Supabase');
          }
        } catch (supabaseError) {
          console.warn('[NatalServiceRapidAPI] Supabase error:', supabaseError);
        }
      }

      return localResult;
    } catch (error) {
      console.error('[NatalServiceRapidAPI] Erreur compute for user:', error);
      throw error;
    }
  }

  /**
   * Récupérer le dernier thème natal calculé via RapidAPI
   * @returns {Promise<Object|null>}
   */
  async getLatestNatalChart() {
    try {
      // 1. Vérifier AsyncStorage
      const localChart = await AsyncStorage.getItem('natal_chart_rapidapi');

      if (localChart) {
        console.log('[NatalServiceRapidAPI] Chargé depuis AsyncStorage');
        return JSON.parse(localChart);
      }

      // 2. Mode connecté : récupérer depuis Supabase
      const { data: { user } } = await supabase.auth.getUser();

      if (!user) {
        console.log('[NatalServiceRapidAPI] Pas de chart local ni de user connecté');
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
        console.warn('[NatalServiceRapidAPI] Erreur fetch:', error);
        return null;
      }

      return data;
    } catch (error) {
      console.error('[NatalServiceRapidAPI] Erreur get latest:', error);
      return null;
    }
  }

  /**
   * Effacer le cache local
   */
  async clearCache() {
    try {
      await AsyncStorage.removeItem('natal_chart_rapidapi');
      console.log('[NatalServiceRapidAPI] Cache effacé');
    } catch (error) {
      console.error('[NatalServiceRapidAPI] Erreur clear cache:', error);
    }
  }
}

export const natalServiceRapidAPI = new NatalServiceRapidAPI();

