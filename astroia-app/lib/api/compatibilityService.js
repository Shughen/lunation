/**
 * Service pour sauvegarder l'historique des compatibilités dans Supabase
 */

import { supabase } from '../supabase';

/**
 * Sauvegarde une analyse de compatibilité dans Supabase
 */
export async function saveCompatibilityHistory(analysisData) {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    
    if (!user) {
      console.log('[compatibilityService] Utilisateur non connecté, historique non sauvegardé');
      return null;
    }

    const { parentData, enfantData, result } = analysisData;

    const { data, error } = await supabase
      .from('compatibility_history')
      .insert({
        user_id: user.id,
        parent_sun_sign: parentData.sunSign,
        parent_moon_sign: parentData.moonSign,
        parent_ascendant: parentData.ascendant,
        child_sun_sign: enfantData.sunSign,
        child_moon_sign: enfantData.moonSign,
        child_ascendant: enfantData.ascendant,
        compatibility_score: result.compatibility_score,
        interpretation_level: result.interpretation?.level || null,
        interpretation_emoji: result.interpretation?.emoji || null,
      })
      .select()
      .single();

    if (error) {
      console.error('[compatibilityService] Error saving:', error);
      return null;
    }

    console.log('[compatibilityService] Saved successfully:', data.id);
    return data;
  } catch (error) {
    console.error('[compatibilityService] Error:', error);
    return null;
  }
}

/**
 * Récupère l'historique des compatibilités de l'utilisateur
 */
export async function getCompatibilityHistory(limit = 10) {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    
    if (!user) {
      return [];
    }

    const { data, error } = await supabase
      .from('compatibility_history')
      .select('*')
      .eq('user_id', user.id)
      .order('created_at', { ascending: false })
      .limit(limit);

    if (error) {
      console.error('[compatibilityService] Error fetching history:', error);
      return [];
    }

    return data || [];
  } catch (error) {
    console.error('[compatibilityService] Error:', error);
    return [];
  }
}

/**
 * Supprime une entrée de l'historique
 */
export async function deleteCompatibilityHistory(id) {
  try {
    const { error } = await supabase
      .from('compatibility_history')
      .delete()
      .eq('id', id);

    if (error) {
      console.error('[compatibilityService] Error deleting:', error);
      return false;
    }

    return true;
  } catch (error) {
    console.error('[compatibilityService] Error:', error);
    return false;
  }
}

export default {
  saveCompatibilityHistory,
  getCompatibilityHistory,
  deleteCompatibilityHistory,
};

