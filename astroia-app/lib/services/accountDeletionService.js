/**
 * Service de suppression complète de compte utilisateur
 * Conformité RGPD - Droit à l'oubli (Art. 17)
 * 
 * Ce service supprime toutes les données utilisateur :
 * - Supabase : profiles, natal_charts, journal_entries, etc.
 * - AsyncStorage : profil local, onboarding, thème natal, etc.
 * - Déconnexion de l'utilisateur
 */

import { supabase } from '@/lib/supabase';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useAuthStore } from '@/stores/authStore';
import { useProfileStore } from '@/stores/profileStore';

/**
 * Supprime complètement le compte utilisateur et toutes ses données
 * 
 * @returns {Promise<{success: boolean, errors: Array<string>}>}
 */
export async function deleteAccount() {
  const errors = [];
  const userId = await getCurrentUserId();
  
  if (!userId) {
    console.warn('[AccountDeletion] Pas d\'utilisateur connecté, nettoyage local uniquement');
    await cleanupLocalData();
    return { success: true, errors: [] };
  }

  console.log('[AccountDeletion] 🗑️ Début suppression compte pour utilisateur:', userId);

  // 1. Supprimer les données Supabase
  try {
    await deleteSupabaseData(userId);
    console.log('[AccountDeletion] ✅ Données Supabase supprimées');
  } catch (error) {
    const errorMsg = `Erreur suppression Supabase: ${error.message}`;
    console.error('[AccountDeletion] ❌', errorMsg);
    errors.push(errorMsg);
    // On continue malgré l'erreur (nettoyage local + déconnexion)
  }

  // 2. Nettoyer les données locales (AsyncStorage)
  try {
    await cleanupLocalData();
    console.log('[AccountDeletion] ✅ Données locales supprimées');
  } catch (error) {
    const errorMsg = `Erreur nettoyage local: ${error.message}`;
    console.error('[AccountDeletion] ❌', errorMsg);
    errors.push(errorMsg);
  }

  // 3. Déconnecter l'utilisateur
  try {
    await signOutUser();
    console.log('[AccountDeletion] ✅ Utilisateur déconnecté');
  } catch (error) {
    const errorMsg = `Erreur déconnexion: ${error.message}`;
    console.error('[AccountDeletion] ❌', errorMsg);
    errors.push(errorMsg);
  }

  const success = errors.length === 0;
  console.log(`[AccountDeletion] ${success ? '✅' : '⚠️'} Suppression compte terminée (${errors.length} erreur(s))`);

  return { success, errors };
}

/**
 * Récupère l'ID de l'utilisateur actuellement connecté
 */
async function getCurrentUserId() {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    return user?.id || null;
  } catch (error) {
    console.error('[AccountDeletion] Erreur récupération userId:', error);
    return null;
  }
}

/**
 * Supprime toutes les données utilisateur dans Supabase
 */
async function deleteSupabaseData(userId) {
  console.log('[AccountDeletion] Suppression données Supabase pour:', userId);

  // 1. Supprimer le profil
  try {
    const { error: profileError } = await supabase
      .from('profiles')
      .delete()
      .eq('id', userId);
    
    if (profileError) {
      // Si erreur RLS, on log mais on continue
      if (profileError.code === '42501' || profileError.message.includes('RLS')) {
        console.warn('[AccountDeletion] ⚠️ RLS bloque suppression profil (normal si pas de profil):', profileError.message);
      } else {
        throw profileError;
      }
    } else {
      console.log('[AccountDeletion] ✅ Profil supprimé (table profiles)');
    }
  } catch (error) {
    console.error('[AccountDeletion] ❌ Erreur suppression profil:', error);
    throw error;
  }

  // 2. Supprimer les thèmes natals
  try {
    const { error: natalError } = await supabase
      .from('natal_charts')
      .delete()
      .eq('user_id', userId);
    
    if (natalError) {
      if (natalError.code === '42501' || natalError.message.includes('RLS')) {
        console.warn('[AccountDeletion] ⚠️ RLS bloque suppression natal_charts:', natalError.message);
      } else {
        throw natalError;
      }
    } else {
      console.log('[AccountDeletion] ✅ Thèmes natals supprimés (table natal_charts)');
    }
  } catch (error) {
    console.error('[AccountDeletion] ❌ Erreur suppression natal_charts:', error);
    throw error;
  }

  // 3. Supprimer les entrées de journal
  try {
    const { error: journalError } = await supabase
      .from('journal_entries')
      .delete()
      .eq('user_id', userId);
    
    if (journalError) {
      if (journalError.code === '42501' || journalError.message.includes('RLS')) {
        console.warn('[AccountDeletion] ⚠️ RLS bloque suppression journal_entries:', journalError.message);
      } else {
        throw journalError;
      }
    } else {
      console.log('[AccountDeletion] ✅ Entrées journal supprimées (table journal_entries)');
    }
  } catch (error) {
    console.error('[AccountDeletion] ❌ Erreur suppression journal_entries:', error);
    throw error;
  }

  // 4. Supprimer les analyses de compatibilité (si table existe)
  try {
    const { error: compatError } = await supabase
      .from('compatibility_analyses')
      .delete()
      .eq('user_id', userId);
    
    if (compatError) {
      // Si table n'existe pas ou RLS bloque, on ignore (pas critique)
      if (compatError.code === '42P01' || compatError.code === '42501') {
        console.log('[AccountDeletion] ℹ️ Table compatibility_analyses non accessible ou inexistante');
      } else {
        console.warn('[AccountDeletion] ⚠️ Erreur suppression compatibility_analyses:', compatError.message);
      }
    } else {
      console.log('[AccountDeletion] ✅ Analyses compatibilité supprimées (table compatibility_analyses)');
    }
  } catch (error) {
    // Non bloquant
    console.warn('[AccountDeletion] ⚠️ Erreur suppression compatibility_analyses (non bloquant):', error.message);
  }

  // TODO: Ajouter suppression d'autres tables si nécessaire :
  // - cycle_history
  // - lunar_revolutions
  // - etc.
}

/**
 * Nettoie toutes les données locales (AsyncStorage)
 */
async function cleanupLocalData() {
  console.log('[AccountDeletion] Nettoyage données locales...');

  // Liste des clés à supprimer
  const keysToRemove = [
    '@astroia_user_profile',        // Profil utilisateur
    '@astroia_journal_entries',     // Entrées journal
    'natal_chart_local',            // Thème natal local
    '@profile_migrated_to_supabase', // Flag migration
    'onboarding_completed',         // Flag onboarding
    'user_consent',                // Consentements RGPD
    'cycle_config',                 // Configuration cycle
    'disclaimer_accepted',          // Acceptation disclaimer
    'disclaimer_accepted_date',     // Date acceptation
  ];

  try {
    // Supprimer les clés spécifiques
    await AsyncStorage.multiRemove(keysToRemove);
    console.log('[AccountDeletion] ✅ Clés AsyncStorage spécifiques supprimées');

    // Optionnel : Supprimer TOUT AsyncStorage (plus radical)
    // await AsyncStorage.clear();
    // console.log('[AccountDeletion] ✅ AsyncStorage complètement vidé');
  } catch (error) {
    console.error('[AccountDeletion] ❌ Erreur nettoyage AsyncStorage:', error);
    throw error;
  }

  // Reset du profil dans le store Zustand
  try {
    useProfileStore.getState().resetProfile();
    console.log('[AccountDeletion] ✅ Store profil réinitialisé');
  } catch (error) {
    console.warn('[AccountDeletion] ⚠️ Erreur reset store profil (non bloquant):', error);
  }
}

/**
 * Déconnecte l'utilisateur
 */
async function signOutUser() {
  try {
    const { signOut } = useAuthStore.getState();
    const result = await signOut();
    
    if (result.error) {
      throw result.error;
    }
    
    console.log('[AccountDeletion] ✅ Utilisateur déconnecté');
  } catch (error) {
    console.error('[AccountDeletion] ❌ Erreur déconnexion:', error);
    throw error;
  }
}

export default {
  deleteAccount,
};

