/**
 * Service Dashboard
 * Agrège toutes les données utilisateur pour affichage centralisé
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { supabase } from '../supabase';

/**
 * Récupère toutes les statistiques du dashboard
 */
export async function getDashboardStats(userId = null) {
  try {
    const stats = {
      totalAnalyses: 0,
      parentChildAnalyses: 0,
      compatibilityAnalyses: 0,
      cycleAstroAnalyses: 0,
      horoscopesViewed: 0,
      avgScore: 0,
      lastActivity: null,
      streak: 0,
      badges: [],
    };

    // Données locales (AsyncStorage)
    const localStats = await getLocalStats();
    
    // Données Supabase (si connecté)
    const supabaseStats = await getSupabaseStats(userId);

    // Fusionner
    stats.totalAnalyses = localStats.totalAnalyses + supabaseStats.totalAnalyses;
    stats.parentChildAnalyses = localStats.parentChildAnalyses + supabaseStats.parentChildAnalyses;
    stats.compatibilityAnalyses = localStats.compatibilityAnalyses + supabaseStats.compatibilityAnalyses;
    stats.cycleAstroAnalyses = localStats.cycleAstroAnalyses + supabaseStats.cycleAstroAnalyses;
    stats.horoscopesViewed = localStats.horoscopesViewed;
    stats.avgScore = calculateAvgScore(localStats, supabaseStats);
    stats.lastActivity = new Date().toISOString();
    stats.streak = await calculateStreak();
    stats.badges = calculateBadges(stats);

    return stats;
  } catch (error) {
    console.error('[dashboardService] Error:', error);
    return getDefaultStats();
  }
}

/**
 * Récupère les stats depuis AsyncStorage
 */
async function getLocalStats() {
  try {
    const keys = await AsyncStorage.getAllKeys();
    
    const parentChildKeys = keys.filter(k => k.startsWith('analysis_parent_child_'));
    const compatKeys = keys.filter(k => k.startsWith('analysis_compat_'));
    const cycleAstroKeys = keys.filter(k => k.startsWith('cycle_astro_'));
    const horoscopeKeys = keys.filter(k => k.startsWith('horoscope_'));

    return {
      totalAnalyses: parentChildKeys.length + compatKeys.length + cycleAstroKeys.length,
      parentChildAnalyses: parentChildKeys.length,
      compatibilityAnalyses: compatKeys.length,
      cycleAstroAnalyses: cycleAstroKeys.length,
      horoscopesViewed: horoscopeKeys.length,
    };
  } catch (error) {
    console.error('[getLocalStats] Error:', error);
    return { totalAnalyses: 0, parentChildAnalyses: 0, compatibilityAnalyses: 0, cycleAstroAnalyses: 0, horoscopesViewed: 0 };
  }
}

/**
 * Récupère les stats depuis Supabase
 */
async function getSupabaseStats(userId) {
  try {
    if (!userId) {
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) return { totalAnalyses: 0, parentChildAnalyses: 0, compatibilityAnalyses: 0, cycleAstroAnalyses: 0 };
      userId = user.id;
    }

    // Compatibilité parent-enfant (exclure cycle-astro)
    const { count: parentChildCount } = await supabase
      .from('compatibility_history')
      .select('*', { count: 'exact', head: true })
      .eq('user_id', userId)
      .neq('type', 'cycle-astro');

    // Compatibilité relationnelle
    const { count: compatCount } = await supabase
      .from('compatibility_analyses')
      .select('*', { count: 'exact', head: true })
      .eq('user_id', userId);

    // Cycle & Astrologie
    const { count: cycleAstroCount } = await supabase
      .from('compatibility_history')
      .select('*', { count: 'exact', head: true })
      .eq('user_id', userId)
      .eq('type', 'cycle-astro');

    return {
      totalAnalyses: (parentChildCount || 0) + (compatCount || 0) + (cycleAstroCount || 0),
      parentChildAnalyses: parentChildCount || 0,
      compatibilityAnalyses: compatCount || 0,
      cycleAstroAnalyses: cycleAstroCount || 0,
    };
  } catch (error) {
    console.error('[getSupabaseStats] Error:', error);
    return { totalAnalyses: 0, parentChildAnalyses: 0, compatibilityAnalyses: 0, cycleAstroAnalyses: 0 };
  }
}

/**
 * Calcule le score moyen
 */
function calculateAvgScore(_localStats, _supabaseStats) {
  // Simplifié : retourne 0 pour l'instant
  // À améliorer avec les vrais scores
  return 0;
}

/**
 * Calcule la série de jours consécutifs
 */
async function calculateStreak() {
  try {
    const streakKey = 'user_streak';
    const lastVisitKey = 'last_visit';
    
    const today = new Date().toISOString().split('T')[0];
    const lastVisit = await AsyncStorage.getItem(lastVisitKey);
    const currentStreak = parseInt(await AsyncStorage.getItem(streakKey) || '0', 10);

    if (!lastVisit) {
      // Première visite
      await AsyncStorage.setItem(lastVisitKey, today);
      await AsyncStorage.setItem(streakKey, '1');
      return 1;
    }

    const yesterday = new Date(Date.now() - 86400000).toISOString().split('T')[0];

    if (lastVisit === today) {
      // Même jour
      return currentStreak;
    } else if (lastVisit === yesterday) {
      // Jour consécutif
      const newStreak = currentStreak + 1;
      await AsyncStorage.setItem(lastVisitKey, today);
      await AsyncStorage.setItem(streakKey, newStreak.toString());
      return newStreak;
    } else {
      // Série cassée
      await AsyncStorage.setItem(lastVisitKey, today);
      await AsyncStorage.setItem(streakKey, '1');
      return 1;
    }
  } catch (error) {
    console.error('[calculateStreak] Error:', error);
    return 0;
  }
}

/**
 * Calcule les badges débloqués
 */
function calculateBadges(stats) {
  const badges = [];

  // Badge Explorateur (5 analyses)
  if (stats.totalAnalyses >= 5) {
    badges.push({
      id: 'explorer',
      name: 'Explorateur',
      emoji: '🌟',
      description: '5 analyses effectuées',
      unlocked: true,
    });
  }

  // Badge Passionné (10 analyses)
  if (stats.totalAnalyses >= 10) {
    badges.push({
      id: 'passionate',
      name: 'Passionné',
      emoji: '💫',
      description: '10 analyses effectuées',
      unlocked: true,
    });
  }

  // Badge Expert (25 analyses)
  if (stats.totalAnalyses >= 25) {
    badges.push({
      id: 'expert',
      name: 'Expert',
      emoji: '✨',
      description: '25 analyses effectuées',
      unlocked: true,
    });
  }

  // Badge Régulier (7 jours consécutifs)
  if (stats.streak >= 7) {
    badges.push({
      id: 'regular',
      name: 'Régulier',
      emoji: '📅',
      description: '7 jours consécutifs',
      unlocked: true,
    });
  }

  // Badge Streak 30 jours
  if (stats.streak >= 30) {
    badges.push({
      id: 'committed',
      name: 'Engagé',
      emoji: '🔥',
      description: '30 jours consécutifs',
      unlocked: true,
    });
  }

  return badges;
}

/**
 * Récupère l'historique complet des analyses
 */
export async function getFullHistory(limit = 50) {
  try {
    const history = [];

    // AsyncStorage - Analyses locales
    const keys = await AsyncStorage.getAllKeys();
    
    // Parent-enfant
    const parentChildKeys = keys.filter(k => k.startsWith('analysis_parent_child_'));
    for (const key of parentChildKeys) {
      const data = await AsyncStorage.getItem(key);
      if (data) {
        const parsed = JSON.parse(data);
        history.push({
          id: key,
          type: 'parent-child',
          icon: '👶',
          score: parsed.score || parsed.compatibility_score || 0,
          created_at: parsed.created_at || parsed.date || new Date().toISOString(),
          ...parsed,
        });
      }
    }

    // Compatibilité relationnelle
    const compatKeys = keys.filter(k => k.startsWith('analysis_compat_'));
    for (const key of compatKeys) {
      const data = await AsyncStorage.getItem(key);
      if (data) {
        const parsed = JSON.parse(data);
        history.push({
          id: key,
          type: parsed.relationType || parsed.relation_type || 'couple',
          icon: parsed.relationType === 'couple' ? '💑' : parsed.relationType === 'friends' ? '🤝' : '💼',
          score: parsed.globalScore || parsed.global_score || 0,
          created_at: parsed.created_at || new Date().toISOString(),
          ...parsed,
        });
      }
    }

    // Cycle & Astrologie
    const cycleAstroKeys = keys.filter(k => k.startsWith('cycle_astro_'));
    for (const key of cycleAstroKeys) {
      const data = await AsyncStorage.getItem(key);
      if (data) {
        const parsed = JSON.parse(data);
        history.push({
          id: key,
          type: 'cycle-astro',
          icon: '🌙',
          score: parsed.analysis?.energyLevel || 0,
          created_at: parsed.created_at || new Date().toISOString(),
          interpretation: {
            emoji: parsed.analysis?.moonPhase?.emoji || '🌙',
            title: `Jour ${parsed.cycleData?.dayOfCycle || 1} • ${parsed.analysis?.moonPhase?.name || 'Analyse'}`,
            description: parsed.analysis?.transitInfo?.description || 'Analyse de cycle',
          },
          recommendations: parsed.analysis?.recommendations || [],
          detailedScores: null, // Pas de scores détaillés pour cycle-astro
          ...parsed,
        });
      }
    }

    // Essayer Supabase aussi (si connecté)
    try {
      const { data: parentChildData } = await supabase
        .from('compatibility_history')
        .select('*')
        .neq('type', 'cycle-astro')
        .order('created_at', { ascending: false })
        .limit(limit);

      if (parentChildData) {
        history.push(...parentChildData.map(item => ({
          ...item,
          type: 'parent-child',
          icon: '👶',
          score: item.compatibility_score,
        })));
      }

      // Cycle & Astrologie depuis Supabase
      const { data: cycleAstroData } = await supabase
        .from('compatibility_history')
        .select('*')
        .eq('type', 'cycle-astro')
        .order('created_at', { ascending: false })
        .limit(limit);

      if (cycleAstroData) {
        history.push(...cycleAstroData.map(item => ({
          ...item,
          type: 'cycle-astro',
          icon: '🌙',
          score: item.compatibility_score, // energyLevel stocké ici
        })));
      }

      const { data: compatData } = await supabase
        .from('compatibility_analyses')
        .select('*')
        .order('created_at', { ascending: false })
        .limit(limit);

      if (compatData) {
        history.push(...compatData.map(item => ({
          ...item,
          type: item.relation_type,
          icon: item.relation_type === 'couple' ? '💑' : item.relation_type === 'friends' ? '🤝' : '💼',
          score: item.global_score,
        })));
      }
    } catch (supaError) {
      console.log('[getFullHistory] Supabase not available:', supaError.message);
    }

    // Trier par date
    history.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

    return history.slice(0, limit);
  } catch (error) {
    console.error('[getFullHistory] Error:', error);
    return [];
  }
}

/**
 * Supprime une analyse de l'historique
 */
export async function deleteAnalysis(id, type) {
  try {
    // Supprimer de AsyncStorage (priorité)
    if (id.startsWith('analysis_') || id.startsWith('cycle_astro_')) {
      await AsyncStorage.removeItem(id);
      console.log('[deleteAnalysis] Deleted from AsyncStorage:', id);
      return true;
    }

    // Sinon essayer Supabase
    const table = (type === 'parent-child' || type === 'cycle-astro') ? 'compatibility_history' : 'compatibility_analyses';
    
    const { error } = await supabase
      .from(table)
      .delete()
      .eq('id', id);

    if (error) {
      console.error('[deleteAnalysis] Supabase error:', error);
      return false;
    }

    console.log('[deleteAnalysis] Deleted from Supabase:', id);
    return true;
  } catch (error) {
    console.error('[deleteAnalysis] Error:', error);
    return false;
  }
}

/**
 * Stats par défaut
 */
function getDefaultStats() {
  return {
    totalAnalyses: 0,
    parentChildAnalyses: 0,
    compatibilityAnalyses: 0,
    cycleAstroAnalyses: 0,
    horoscopesViewed: 0,
    avgScore: 0,
    lastActivity: new Date().toISOString(),
    streak: 0,
    badges: [],
  };
}

export default {
  getDashboardStats,
  getFullHistory,
  deleteAnalysis,
};

