import { supabase } from '@/lib/supabase';

/**
 * Service pour gérer les cycles lunaires personnels avec Supabase
 * 
 * Le cycle lunaire personnel est simplifié à 28 jours pour le MVP.
 * TODO: Remplacer le calcul simplifié (28 jours à partir d'aujourd'hui) 
 *       par un calcul basé sur la vraie révolution lunaire de l'utilisateur.
 */
class LunarCycleService {
  /**
   * Récupère ou crée un cycle lunaire actif pour l'utilisateur
   * @param {string} userId - ID de l'utilisateur
   * @returns {Promise<{cycleStartDate: Date, cycleEndDate: Date}>}
   */
  async getOrCreateCurrentLunarCycle(userId) {
    try {
      // Vérifier si un cycle actif existe
      const activeCycle = await this._getCurrentActiveCycle(userId);
      
      if (activeCycle) {
        console.log('[LunarCycleService] Cycle actif trouvé:', {
          start: activeCycle.cycle_start_date,
          end: activeCycle.cycle_end_date
        });
        return {
          cycleStartDate: new Date(activeCycle.cycle_start_date),
          cycleEndDate: new Date(activeCycle.cycle_end_date),
        };
      }

      // Aucun cycle actif trouvé, créer un nouveau cycle
      // TODO: Remplacer new Date() par le calcul de la vraie date de révolution lunaire
      //       en utilisant les données de naissance de l'utilisateur (date, heure, lieu)
      const today = new Date();
      today.setHours(0, 0, 0, 0); // Réinitialiser l'heure à minuit pour éviter les problèmes de fuseau horaire
      
      const newCycle = await this._createCycle(userId, today);
      
      console.log('[LunarCycleService] Nouveau cycle créé:', {
        start: newCycle.cycle_start_date,
        end: newCycle.cycle_end_date
      });
      
      return {
        cycleStartDate: new Date(newCycle.cycle_start_date),
        cycleEndDate: new Date(newCycle.cycle_end_date),
      };
    } catch (error) {
      console.error('[LunarCycleService] Erreur getOrCreateCurrentLunarCycle:', error);
      throw error;
    }
  }

  /**
   * Retourne le jour du cycle et la phase pour une date donnée
   * @param {string} userId - ID de l'utilisateur
   * @param {Date} date - Date pour laquelle calculer le jour du cycle
   * @returns {Promise<{cycleDay: number, phase: string} | null>}
   */
  async getLunarDayForDate(userId, date) {
    try {
      // Normaliser la date (réinitialiser l'heure à minuit)
      const targetDate = new Date(date);
      targetDate.setHours(0, 0, 0, 0);

      // Récupérer le cycle actif
      const activeCycle = await this._getCurrentActiveCycle(userId);
      
      if (!activeCycle) {
        console.log('[LunarCycleService] Aucun cycle actif trouvé pour la date:', targetDate);
        return null;
      }

      const cycleStartDate = new Date(activeCycle.cycle_start_date);
      cycleStartDate.setHours(0, 0, 0, 0);
      
      const cycleEndDate = new Date(activeCycle.cycle_end_date);
      cycleEndDate.setHours(0, 0, 0, 0);

      // Vérifier si la date est dans le cycle
      if (targetDate < cycleStartDate || targetDate > cycleEndDate) {
        console.log('[LunarCycleService] Date hors du cycle actif:', {
          date: targetDate,
          cycleStart: cycleStartDate,
          cycleEnd: cycleEndDate
        });
        return null;
      }

      // Calculer le jour du cycle (1-28)
      const cycleDay = this._calculateCycleDay(cycleStartDate, targetDate);
      
      // Déterminer la phase
      const phase = this._getPhaseFromCycleDay(cycleDay);

      // TODO: Utiliser la table lunar_daily_states pour mettre en cache le résultat
      //       et éviter de recalculer à chaque fois

      return {
        cycleDay,
        phase,
      };
    } catch (error) {
      console.error('[LunarCycleService] Erreur getLunarDayForDate:', error);
      return null;
    }
  }

  /**
   * Récupère le cycle actif depuis Supabase
   * Un cycle est actif si la date actuelle est entre cycle_start_date et cycle_end_date
   * @private
   * @param {string} userId - ID de l'utilisateur
   * @returns {Promise<Object | null>}
   */
  async _getCurrentActiveCycle(userId) {
    try {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const todayStr = this._formatDateForSupabase(today);

      const { data, error } = await supabase
        .from('lunar_cycles')
        .select('*')
        .eq('user_id', userId)
        .lte('cycle_start_date', todayStr)
        .gte('cycle_end_date', todayStr)
        .order('created_at', { ascending: false })
        .limit(1)
        .single();

      if (error) {
        // PGRST116 = not found (aucun cycle actif)
        if (error.code === 'PGRST116') {
          console.log('[LunarCycleService] Aucun cycle actif trouvé');
          return null;
        }
        throw error;
      }

      return data;
    } catch (error) {
      console.error('[LunarCycleService] Erreur _getCurrentActiveCycle:', error);
      throw error;
    }
  }

  /**
   * Crée un nouveau cycle dans Supabase
   * @private
   * @param {string} userId - ID de l'utilisateur
   * @param {Date} startDate - Date de début du cycle (Jour 1)
   * @returns {Promise<Object>}
   */
  async _createCycle(userId, startDate) {
    try {
      // Normaliser la date de début
      const cycleStartDate = new Date(startDate);
      cycleStartDate.setHours(0, 0, 0, 0);
      
      // Calculer la date de fin (28 jours après le début, donc Jour 28)
      // cycle_end_date = cycle_start_date + 27 jours (jours 1 à 28 inclus)
      const cycleEndDate = new Date(cycleStartDate);
      cycleEndDate.setDate(cycleEndDate.getDate() + 27);

      const cycleData = {
        user_id: userId,
        cycle_start_date: this._formatDateForSupabase(cycleStartDate),
        cycle_end_date: this._formatDateForSupabase(cycleEndDate),
      };

      const { data, error } = await supabase
        .from('lunar_cycles')
        .insert(cycleData)
        .select()
        .single();

      if (error) {
        throw error;
      }

      console.log('[LunarCycleService] Cycle créé avec succès:', data.id);
      return data;
    } catch (error) {
      console.error('[LunarCycleService] Erreur _createCycle:', error);
      throw error;
    }
  }

  /**
   * Calcule le jour du cycle (1-28) entre la date de début et la date cible
   * @private
   * @param {Date} startDate - Date de début du cycle (Jour 1)
   * @param {Date} targetDate - Date cible
   * @returns {number} Jour du cycle (1-28)
   */
  _calculateCycleDay(startDate, targetDate) {
    // Calculer la différence en jours
    const diffTime = targetDate.getTime() - startDate.getTime();
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    
    // Le jour du cycle est 1-indexé (1-28)
    const cycleDay = diffDays + 1;
    
    // S'assurer que le jour est entre 1 et 28
    // (normalement toujours le cas si targetDate est dans le cycle)
    if (cycleDay < 1 || cycleDay > 28) {
      console.warn('[LunarCycleService] Jour du cycle hors limites:', cycleDay);
    }
    
    return Math.max(1, Math.min(28, cycleDay));
  }

  /**
   * Détermine la phase du cycle depuis le jour du cycle
   * Selon SPEC.md :
   * - Phase 1 (Jours 1-7) : 'start' - Ouverture & nouveaux ressentis
   * - Phase 2 (Jours 8-14) : 'rise' - Montée émotionnelle & prises de conscience
   * - Phase 3 (Jours 15-21) : 'peak' - Apogée & tension intérieure
   * - Phase 4 (Jours 22-28) : 'integration' - Intégration & retour à soi
   * @private
   * @param {number} cycleDay - Jour du cycle (1-28)
   * @returns {string} Phase du cycle ('start' | 'rise' | 'peak' | 'integration')
   */
  _getPhaseFromCycleDay(cycleDay) {
    if (cycleDay >= 1 && cycleDay <= 7) {
      return 'start';
    } else if (cycleDay >= 8 && cycleDay <= 14) {
      return 'rise';
    } else if (cycleDay >= 15 && cycleDay <= 21) {
      return 'peak';
    } else if (cycleDay >= 22 && cycleDay <= 28) {
      return 'integration';
    } else {
      console.warn('[LunarCycleService] Jour du cycle invalide pour déterminer la phase:', cycleDay);
      // Par défaut, retourner 'start' pour les jours hors limites
      return 'start';
    }
  }

  /**
   * Formate une Date en string pour Supabase (format YYYY-MM-DD)
   * @private
   * @param {Date} date - Date à formater
   * @returns {string} Date formatée (YYYY-MM-DD)
   */
  _formatDateForSupabase(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }
}

export const lunarCycleService = new LunarCycleService();

