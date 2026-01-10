/**
 * Service Horoscope Quotidien
 * Gère la génération, le cache et le stockage des horoscopes
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import Constants from 'expo-constants';
import { supabase } from '../supabase';

const AI_API_URL = Constants.expoConfig?.extra?.aiApiUrl || 
  'https://astro-ia-niei71xao-remibeaurain-4057s-projects.vercel.app/api/ai/chat';

const ZODIAC_SIGNS = {
  1: 'Bélier', 2: 'Taureau', 3: 'Gémeaux', 4: 'Cancer',
  5: 'Lion', 6: 'Vierge', 7: 'Balance', 8: 'Scorpion',
  9: 'Sagittaire', 10: 'Capricorne', 11: 'Verseau', 12: 'Poissons',
};

/**
 * Calcule le signe lunaire du jour (simplifié)
 */
function getCurrentMoonSign() {
  const signs = Object.values(ZODIAC_SIGNS);
  const dayOfYear = Math.floor((Date.now() - new Date(new Date().getFullYear(), 0, 0)) / 86400000);
  const signIndex = Math.floor((dayOfYear / 2.5) % 12); // La Lune change de signe tous les ~2.5 jours
  return signs[signIndex];
}

/**
 * Génère un numéro chance basé sur le signe et la date
 */
function getLuckyNumber(sign, date) {
  const seed = new Date(date).getTime() + sign;
  return ((seed % 49) + 1); // Numéro entre 1 et 49
}

/**
 * Récupère l'horoscope du jour depuis le cache ou génère un nouveau
 */
export async function getDailyHoroscope(signId, userProfile = null) {
  try {
    const today = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
    const cacheKey = `horoscope_${signId}_${today}`;

    // 1. Vérifier le cache local
    const cached = await AsyncStorage.getItem(cacheKey);
    if (cached) {
      console.log('[horoscopeService] Loaded from cache');
      return JSON.parse(cached);
    }

    // 2. Générer un nouveau horoscope via IA
    console.log('[horoscopeService] Generating new horoscope...');
    const horoscope = await generateHoroscope(signId, today, userProfile);

    // 3. Sauvegarder dans le cache
    await AsyncStorage.setItem(cacheKey, JSON.stringify(horoscope));

    // 4. Sauvegarder dans Supabase (silencieusement)
    saveToSupabase(horoscope).catch(err => 
      console.log('[horoscopeService] Supabase save failed:', err)
    );

    return horoscope;
  } catch (error) {
    console.error('[horoscopeService] Error:', error);
    throw error;
  }
}

/**
 * Génère un horoscope via l'API IA
 */
async function generateHoroscope(signId, date, userProfile) {
  const signName = ZODIAC_SIGNS[signId];
  const moonSign = getCurrentMoonSign();
  const luckyNumber = getLuckyNumber(signId, date);

  const prompt = `Tu es un astrologue professionnel expert.

Génère un horoscope quotidien pour le signe ${signName}.
Date : ${new Date(date).toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })}
Lune actuelle : en ${moonSign}

${userProfile?.name ? `Prénom : ${userProfile.name}` : ''}
${userProfile?.birthPlace ? `Lieu de naissance : ${userProfile.birthPlace}` : ''}

Structure ta réponse EXACTEMENT comme suit (respecte les titres et saute une ligne entre chaque) :

TRAVAIL & CARRIÈRE
[50 mots maximum - Conseils professionnels du jour]

AMOUR & RELATIONS
[50 mots maximum - Vie amoureuse et relations]

SANTÉ & BIEN-ÊTRE
[50 mots maximum - Énergie physique et mentale]

CONSEIL DU JOUR
[30 mots maximum - Un conseil actionnable]

Ton ton : bienveillant, précis, actionnable.
Utilise des métaphores cosmiques.
Sois positif mais réaliste.`;

  try {
    const response = await fetch(AI_API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        userId: 'horoscope-user',
        messages: [
          { role: 'user', content: prompt }
        ],
      }),
    });

    if (!response.ok) {
      // Messages d'erreur explicites selon le code de statut
      if (response.status === 429) {
        throw new Error('Trop de requêtes. Veuillez patienter avant de réessayer.');
      }
      
      if (response.status === 401 || response.status === 403) {
        throw new Error('Erreur d\'authentification API.');
      }

      if (response.status >= 500) {
        throw new Error('Le service horoscope est temporairement indisponible.');
      }

      throw new Error(`Erreur lors de la génération de l'horoscope (${response.status}).`);
    }

    const data = await response.json();
    const aiResponse = data.message || data.response || '';

    // Parser la réponse IA
    const parsed = parseHoroscopeResponse(aiResponse);

    return {
      sign: signName,
      signId: signId,
      date: date,
      moonSign: moonSign,
      luckyNumber: luckyNumber,
      ...parsed,
      generatedAt: new Date().toISOString(),
    };
  } catch (error) {
    console.error('[generateHoroscope] Error:', error);
    
    // Vérifier si c'est une erreur réseau
    if (error.message && (error.message.includes('Network') || error.message.includes('Failed to fetch'))) {
      console.log('[generateHoroscope] Erreur réseau, utilisation du fallback');
    } else {
      console.log('[generateHoroscope] Erreur API:', error.message, '- Utilisation du fallback');
    }
    
    // Fallback : horoscope générique
    return generateFallbackHoroscope(signId, date, moonSign, luckyNumber);
  }
}

/**
 * Parse la réponse de l'IA
 */
function parseHoroscopeResponse(text) {
  const sections = {
    work: '',
    love: '',
    health: '',
    advice: '',
  };

  try {
    // Extraire les sections
    const workMatch = text.match(/TRAVAIL & CARRIÈRE\s*\n(.*?)(?=\n\n|AMOUR & RELATIONS|$)/s);
    const loveMatch = text.match(/AMOUR & RELATIONS\s*\n(.*?)(?=\n\n|SANTÉ & BIEN-ÊTRE|$)/s);
    const healthMatch = text.match(/SANTÉ & BIEN-ÊTRE\s*\n(.*?)(?=\n\n|CONSEIL DU JOUR|$)/s);
    const adviceMatch = text.match(/CONSEIL DU JOUR\s*\n(.*?)$/s);

    sections.work = workMatch?.[1]?.trim() || 'Journée propice aux projets professionnels.';
    sections.love = loveMatch?.[1]?.trim() || 'Harmonie dans vos relations.';
    sections.health = healthMatch?.[1]?.trim() || 'Énergie stable, prenez soin de vous.';
    sections.advice = adviceMatch?.[1]?.trim() || 'Suivez votre intuition.';
  } catch (error) {
    console.error('[parseHoroscopeResponse] Parse error:', error);
  }

  return sections;
}

/**
 * Génère un horoscope fallback si l'API échoue
 */
function generateFallbackHoroscope(signId, date, moonSign, luckyNumber) {
  const signName = ZODIAC_SIGNS[signId];
  
  return {
    sign: signName,
    signId: signId,
    date: date,
    moonSign: moonSign,
    luckyNumber: luckyNumber,
    work: `Belle énergie pour vos projets ${signName}. Les astres favorisent votre créativité et votre détermination aujourd'hui.`,
    love: `Journée propice aux échanges sincères. La Lune en ${moonSign} apporte douceur et compréhension dans vos relations.`,
    health: `Votre vitalité est au rendez-vous. Profitez-en pour vous reconnecter à votre corps par une activité physique douce.`,
    advice: `Écoutez votre intuition cosmique. Les signes sont là, il suffit de les observer avec attention.`,
    generatedAt: new Date().toISOString(),
    isFallback: true,
  };
}

/**
 * Sauvegarde dans Supabase
 */
async function saveToSupabase(horoscope) {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    
    if (!user) {
      console.log('[horoscopeService] User not authenticated, skip Supabase save');
      return;
    }

    const { error } = await supabase
      .from('daily_horoscopes')
      .upsert({
        sign: horoscope.sign.toLowerCase(),
        date: horoscope.date,
        work: horoscope.work,
        love: horoscope.love,
        health: horoscope.health,
        advice: horoscope.advice,
        lucky_number: horoscope.luckyNumber,
        moon_sign: horoscope.moonSign,
      }, {
        onConflict: 'sign,date',
      });

    if (error) {
      // Si la table n'existe pas, ignorer silencieusement (c'est normal si la table n'est pas encore créée)
      if (error.code === 'PGRST205' || error.message?.includes('Could not find the table')) {
        console.log('[horoscopeService] Table daily_horoscopes n\'existe pas encore, skip sauvegarde Supabase');
      } else {
        // Pour les autres erreurs, logger en warning
        console.warn('[horoscopeService] Erreur Supabase (non bloquante):', error.message || error);
      }
    } else {
      console.log('[horoscopeService] Saved to Supabase');
    }
  } catch (error) {
    console.error('[horoscopeService] Error:', error);
  }
}

/**
 * Nettoie le cache ancien (>7 jours)
 */
export async function cleanOldCache() {
  try {
    const keys = await AsyncStorage.getAllKeys();
    const horoscopeKeys = keys.filter(k => k.startsWith('horoscope_'));
    
    const today = new Date();
    const sevenDaysAgo = new Date(today.getTime() - 7 * 24 * 60 * 60 * 1000);
    
    for (const key of horoscopeKeys) {
      const dateStr = key.split('_')[2]; // horoscope_{sign}_{date}
      const keyDate = new Date(dateStr);
      
      if (keyDate < sevenDaysAgo) {
        await AsyncStorage.removeItem(key);
        console.log('[horoscopeService] Cleaned old cache:', key);
      }
    }
  } catch (error) {
    console.error('[horoscopeService] Clean cache error:', error);
  }
}

export default {
  getDailyHoroscope,
  cleanOldCache,
};

