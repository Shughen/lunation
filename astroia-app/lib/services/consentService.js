/**
 * Service de gestion des consentements RGPD
 * Gère les consentements santé (Art. 9) et analytics (Art. 6)
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { logConsent } from './consentAuditService';

/**
 * Vérifie si l'utilisateur a donné son consentement pour les données de santé
 */
export async function hasHealthConsent() {
  try {
    const consent = await AsyncStorage.getItem('user_consent');
    if (!consent) return false;
    
    const consentData = JSON.parse(consent);
    return consentData.health === true;
  } catch (error) {
    console.error('[ConsentService] Check health consent error:', error);
    return false;
  }
}

/**
 * Vérifie si l'utilisateur a donné son consentement pour les analytics
 */
export async function hasAnalyticsConsent() {
  try {
    const consent = await AsyncStorage.getItem('user_consent');
    if (!consent) return false;
    
    const consentData = JSON.parse(consent);
    return consentData.analytics === true;
  } catch (error) {
    console.error('[ConsentService] Check analytics consent error:', error);
    return false;
  }
}

/**
 * Récupère tous les consentements
 */
export async function getConsents() {
  try {
    const consent = await AsyncStorage.getItem('user_consent');
    if (!consent) {
      return {
        health: false,
        analytics: false,
        version: null,
        date: null,
      };
    }
    
    return JSON.parse(consent);
  } catch (error) {
    console.error('[ConsentService] Get consents error:', error);
    return {
      health: false,
      analytics: false,
      version: null,
      date: null,
    };
  }
}

/**
 * Met à jour un consentement spécifique
 */
export async function updateConsent(type, value, surface = 'settings') {
  try {
    const currentConsent = await getConsents();
    const previousValue = currentConsent[type];
    
    const updatedConsent = {
      ...currentConsent,
      [type]: value,
      version: '2.0.0',
      date: new Date().toISOString(),
    };

    await AsyncStorage.setItem('user_consent', JSON.stringify(updatedConsent));
    
    // Log dans audit trail
    const status = value ? 'granted' : 'revoked';
    if (previousValue !== value) {
      await logConsent(type, status, surface);
    }
    
    return { success: true };
  } catch (error) {
    console.error('[ConsentService] Update consent error:', error);
    throw error;
  }
}

/**
 * Retire tous les consentements (RGPD droit de retrait)
 */
export async function revokeAllConsents() {
  try {
    await AsyncStorage.removeItem('user_consent');
    return { success: true };
  } catch (error) {
    console.error('[ConsentService] Revoke error:', error);
    throw error;
  }
}

export default {
  hasHealthConsent,
  hasAnalyticsConsent,
  getConsents,
  updateConsent,
  revokeAllConsents,
};

