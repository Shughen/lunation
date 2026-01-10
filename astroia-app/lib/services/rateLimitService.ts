import AsyncStorage from '@react-native-async-storage/async-storage';

const STORAGE_KEY = '@luna_rate_limit';
const MAX_MESSAGES_FREE = 10; // Limite gratuite quotidienne

interface RateLimitData {
  count: number;
  date: string; // Format YYYY-MM-DD
}

/**
 * Obtient la date actuelle au format YYYY-MM-DD
 */
function getTodayKey(): string {
  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, '0');
  const day = String(today.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * Charge les données de rate limit depuis AsyncStorage
 */
async function loadRateLimitData(): Promise<RateLimitData> {
  try {
    const stored = await AsyncStorage.getItem(STORAGE_KEY);
    if (!stored) {
      return { count: 0, date: getTodayKey() };
    }

    const data: RateLimitData = JSON.parse(stored);

    // Si la date stockée est différente d'aujourd'hui, reset
    if (data.date !== getTodayKey()) {
      console.log('[RateLimit] Reset quotidien détecté');
      const resetData = { count: 0, date: getTodayKey() };
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(resetData));
      return resetData;
    }

    return data;
  } catch (error) {
    console.error('[RateLimit] Erreur chargement données:', error);
    // Fail-open : en cas d'erreur, autoriser l'usage
    return { count: 0, date: getTodayKey() };
  }
}

/**
 * Sauvegarde les données de rate limit
 */
async function saveRateLimitData(data: RateLimitData): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  } catch (error) {
    console.error('[RateLimit] Erreur sauvegarde données:', error);
  }
}

/**
 * Vérifie si l'utilisateur peut envoyer un message
 * @returns {allowed: boolean, remaining: number, limit: number}
 */
export async function canSendMessage(): Promise<{
  allowed: boolean;
  remaining: number;
  limit: number;
}> {
  try {
    const data = await loadRateLimitData();
    const remaining = Math.max(0, MAX_MESSAGES_FREE - data.count);
    const allowed = data.count < MAX_MESSAGES_FREE;

    console.log(`[RateLimit] Check: ${data.count}/${MAX_MESSAGES_FREE} (remaining: ${remaining})`);

    return {
      allowed,
      remaining,
      limit: MAX_MESSAGES_FREE,
    };
  } catch (error) {
    console.error('[RateLimit] Erreur vérification:', error);
    // Fail-open : en cas d'erreur, autoriser l'usage
    return {
      allowed: true,
      remaining: MAX_MESSAGES_FREE,
      limit: MAX_MESSAGES_FREE,
    };
  }
}

/**
 * Incrémente le compteur d'usage (à appeler après succès de l'envoi)
 */
export async function incrementUsage(): Promise<void> {
  try {
    const data = await loadRateLimitData();
    data.count += 1;
    await saveRateLimitData(data);

    console.log(`[RateLimit] Usage incrémenté: ${data.count}/${MAX_MESSAGES_FREE}`);
  } catch (error) {
    console.error('[RateLimit] Erreur incrémentation:', error);
    // Ne pas bloquer en cas d'erreur
  }
}

/**
 * Récupère l'usage actuel
 */
export async function getCurrentUsage(): Promise<{
  count: number;
  remaining: number;
  limit: number;
  resetDate: string;
}> {
  try {
    const data = await loadRateLimitData();
    const remaining = Math.max(0, MAX_MESSAGES_FREE - data.count);

    return {
      count: data.count,
      remaining,
      limit: MAX_MESSAGES_FREE,
      resetDate: data.date,
    };
  } catch (error) {
    console.error('[RateLimit] Erreur récupération usage:', error);
    return {
      count: 0,
      remaining: MAX_MESSAGES_FREE,
      limit: MAX_MESSAGES_FREE,
      resetDate: getTodayKey(),
    };
  }
}

/**
 * Reset manuel du compteur (pour debug uniquement)
 */
export async function resetUsage(): Promise<void> {
  try {
    const resetData = { count: 0, date: getTodayKey() };
    await saveRateLimitData(resetData);
    console.log('[RateLimit] Reset manuel effectué');
  } catch (error) {
    console.error('[RateLimit] Erreur reset:', error);
  }
}
