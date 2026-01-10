/**
 * Service d'audit des consentements RGPD
 * Enregistre tous les changements de consentement (Art. 7.1 RGPD - preuve)
 */

import { supabase } from '@/lib/supabase';
import AsyncStorage from '@react-native-async-storage/async-storage';

const POLICY_VERSION = '2.0.0';

/**
 * Enregistre un consentement dans l'audit trail
 */
export async function logConsent(consentType, status, surface = 'settings') {
  try {
    // Essayer Supabase d'abord (audit centralisé)
    const { data: { user } } = await supabase.auth.getUser();
    
    if (user) {
      const { error } = await supabase
        .from('consents_audit')
        .insert({
          user_id: user.id,
          consent_type: consentType,
          status,
          surface,
          policy_version: POLICY_VERSION,
        });
      
      if (error) {
        console.warn('[ConsentAudit] Supabase log warning:', error.message);
      } else {
        console.log(`[ConsentAudit] Logged: ${consentType} ${status} from ${surface}`);
      }
    }
    
    // Backup local (AsyncStorage) au cas où
    const localAudit = await AsyncStorage.getItem('consent_audit_local') || '[]';
    const audit = JSON.parse(localAudit);
    
    audit.push({
      consent_type: consentType,
      status,
      surface,
      policy_version: POLICY_VERSION,
      timestamp: new Date().toISOString(),
    });
    
    await AsyncStorage.setItem('consent_audit_local', JSON.stringify(audit));
    
    return { success: true };
  } catch (error) {
    console.error('[ConsentAudit] Log error:', error);
    return { success: false, error };
  }
}

/**
 * Récupère l'historique des consentements d'un utilisateur
 */
export async function getConsentHistory() {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    
    if (!user) {
      // Fallback local
      const localAudit = await AsyncStorage.getItem('consent_audit_local');
      return localAudit ? JSON.parse(localAudit) : [];
    }
    
    const { data, error } = await supabase
      .from('consents_audit')
      .select('*')
      .eq('user_id', user.id)
      .order('created_at', { ascending: false })
      .limit(50);
    
    if (error) {
      console.warn('[ConsentAudit] Get history warning:', error.message);
      return [];
    }
    
    return data || [];
  } catch (error) {
    console.error('[ConsentAudit] Get history error:', error);
    return [];
  }
}

/**
 * Récupère le dernier consentement d'un type spécifique
 */
export async function getLastConsent(consentType) {
  try {
    const history = await getConsentHistory();
    const typeHistory = history.filter(c => c.consent_type === consentType);
    
    if (typeHistory.length === 0) {
      return null;
    }
    
    return typeHistory[0]; // Plus récent (tri desc)
  } catch (error) {
    console.error('[ConsentAudit] Get last consent error:', error);
    return null;
  }
}

export default {
  logConsent,
  getConsentHistory,
  getLastConsent,
};

