import { supabase } from '@/lib/supabase';

/**
 * Service pour gérer les cycles menstruels avec Supabase
 * Les données renvoyées sont toujours normalisées au format CycleEntry attendu par le store.
 * 
 * Mode invité : retourne null si l'utilisateur n'est pas connecté (pas d'erreur)
 */
class CycleService {
  /**
   * Vérifie si un utilisateur est connecté à Supabase
   * @returns {Promise<boolean>}
   */
  async isUserAuthenticated() {
    const { data, error } = await supabase.auth.getUser();
    return !error && data?.user !== null;
  }

  /**
   * Récupère tous les cycles de l'utilisateur connecté
   * Retourne null si l'utilisateur n'est pas connecté (mode invité)
   * @returns {Promise<CycleEntry[] | null>}
   */
  async getAllCycles() {
    const { data, error } = await supabase.auth.getUser();
    if (error || !data?.user) {
      console.log('[CycleService] Pas d\'utilisateur connecté (mode invité)');
      return null;
    }

    const { data: cycles, error: cyclesError } = await supabase
      .from('cycle_history')
      .select('*')
      .eq('user_id', data.user.id)
      .order('start_date', { ascending: false });

    if (cyclesError) {
      // Si la table n'existe pas encore, ce n'est pas une erreur critique
      if (cyclesError.code === '42P01') {
        console.log('[CycleService] Table cycle_history n\'existe pas encore');
        return null;
      }
      console.error('[CycleService] Erreur getAllCycles:', cyclesError);
      return null;
    }

    if (!cycles || cycles.length === 0) {
      return [];
    }

    return cycles.map(deserializeCycle);
  }

  /**
   * Crée un nouveau cycle dans Supabase
   * Retourne null si l'utilisateur n'est pas connecté (mode invité)
   * @param {Object} cycle - CycleEntry sans id
   * @returns {Promise<CycleEntry | null>}
   */
  async createCycle(cycle) {
    const { data, error } = await supabase.auth.getUser();
    if (error || !data?.user) {
      console.log('[CycleService] Pas d\'utilisateur connecté (mode invité)');
      return null;
    }

    const payload = serializeCycle({
      ...cycle,
      id: undefined, // L'id sera généré par Supabase
    });

    const { data: created, error: createError } = await supabase
      .from('cycle_history')
      .insert({
        ...payload,
        user_id: data.user.id,
      })
      .select()
      .single();

    if (createError) {
      // Si la table n'existe pas encore, ce n'est pas une erreur critique
      if (createError.code === '42P01') {
        console.log('[CycleService] Table cycle_history n\'existe pas encore');
        return null;
      }
      console.error('[CycleService] Erreur createCycle:', createError);
      return null;
    }

    return deserializeCycle(created);
  }

  /**
   * Met à jour un cycle existant dans Supabase
   * Retourne null si l'utilisateur n'est pas connecté (mode invité)
   * @param {string} cycleId - ID du cycle
   * @param {Object} updates - Champs à mettre à jour
   * @returns {Promise<CycleEntry | null>}
   */
  async updateCycle(cycleId, updates) {
    const { data, error } = await supabase.auth.getUser();
    if (error || !data?.user) {
      console.log('[CycleService] Pas d\'utilisateur connecté (mode invité)');
      return null;
    }

    const payload = serializeCycle(updates, true); // true = partial update

    const { data: updated, error: updateError } = await supabase
      .from('cycle_history')
      .update(payload)
      .eq('id', cycleId)
      .eq('user_id', data.user.id) // Sécurité : s'assurer que c'est bien le cycle de l'utilisateur
      .select()
      .single();

    if (updateError) {
      // Si la table n'existe pas encore, ce n'est pas une erreur critique
      if (updateError.code === '42P01') {
        console.log('[CycleService] Table cycle_history n\'existe pas encore');
        return null;
      }
      console.error('[CycleService] Erreur updateCycle:', updateError);
      return null;
    }

    return deserializeCycle(updated);
  }

  /**
   * Supprime un cycle dans Supabase
   * Retourne null si l'utilisateur n'est pas connecté (mode invité)
   * @param {string} cycleId - ID du cycle
   * @returns {Promise<boolean | null>}
   */
  async deleteCycle(cycleId) {
    const { data, error } = await supabase.auth.getUser();
    if (error || !data?.user) {
      console.log('[CycleService] Pas d\'utilisateur connecté (mode invité)');
      return null;
    }

    const { error: deleteError } = await supabase
      .from('cycle_history')
      .delete()
      .eq('id', cycleId)
      .eq('user_id', data.user.id); // Sécurité : s'assurer que c'est bien le cycle de l'utilisateur

    if (deleteError) {
      // Si la table n'existe pas encore, ce n'est pas une erreur critique
      if (deleteError.code === '42P01') {
        console.log('[CycleService] Table cycle_history n\'existe pas encore');
        return null;
      }
      console.error('[CycleService] Erreur deleteCycle:', deleteError);
      return false;
    }

    return true;
  }

  /**
   * Upsert d'un cycle (création ou mise à jour)
   * Retourne null si l'utilisateur n'est pas connecté (mode invité)
   * @param {CycleEntry} cycle - CycleEntry complet
   * @returns {Promise<CycleEntry | null>}
   */
  async upsertCycle(cycle) {
    const { data, error } = await supabase.auth.getUser();
    if (error || !data?.user) {
      console.log('[CycleService] Pas d\'utilisateur connecté (mode invité)');
      return null;
    }

    const payload = serializeCycle(cycle);

    const { data: upserted, error: upsertError } = await supabase
      .from('cycle_history')
      .upsert({
        ...payload,
        id: cycle.id,
        user_id: data.user.id,
      })
      .select()
      .single();

    if (upsertError) {
      // Si la table n'existe pas encore, ce n'est pas une erreur critique
      if (upsertError.code === '42P01') {
        console.log('[CycleService] Table cycle_history n\'existe pas encore');
        return null;
      }
      console.error('[CycleService] Erreur upsertCycle:', upsertError);
      return null;
    }

    return deserializeCycle(upserted);
  }
}

/**
 * Convertit une ligne Supabase (snake_case) vers le format CycleEntry (camelCase)
 * @param {Object} row - Ligne Supabase
 * @returns {CycleEntry}
 */
function deserializeCycle(row) {
  if (!row) return null;

  return {
    id: row.id,
    startDate: row.start_date ? new Date(row.start_date).toISOString() : new Date().toISOString(),
    endDate: row.end_date ? new Date(row.end_date).toISOString() : null,
    cycleLength: row.cycle_length ?? null,
    periodLength: row.period_length ?? null,
    createdAt: row.created_at ? new Date(row.created_at).toISOString() : new Date().toISOString(),
    updatedAt: row.updated_at ? new Date(row.updated_at).toISOString() : new Date().toISOString(),
  };
}

/**
 * Transforme un CycleEntry (camelCase) en payload compatible Supabase (snake_case)
 * @param {Object} cycle - CycleEntry
 * @param {boolean} partial - Si true, ne serialise que les champs présents (pour update)
 * @returns {Object}
 */
function serializeCycle(cycle, partial = false) {
  const result = {};

  if (!partial || cycle.startDate !== undefined) {
    result.start_date = cycle.startDate ? new Date(cycle.startDate).toISOString() : null;
  }

  if (!partial || cycle.endDate !== undefined) {
    result.end_date = cycle.endDate ? new Date(cycle.endDate).toISOString() : null;
  }

  if (!partial || cycle.cycleLength !== undefined) {
    result.cycle_length = cycle.cycleLength ?? null;
  }

  if (!partial || cycle.periodLength !== undefined) {
    result.period_length = cycle.periodLength ?? null;
  }

  // Toujours mettre à jour updated_at
  result.updated_at = new Date().toISOString();

  // Pour create, on laisse Supabase gérer created_at
  // Pour update, on ne modifie pas created_at

  return result;
}

export const cycleService = new CycleService();
