import AsyncStorage from '@react-native-async-storage/async-storage';
import { supabase } from '@/lib/supabase';

/**
 * Service pour l'analyse Cycle Menstruel + Astrologie
 * 
 * Cette fonctionnalité combine :
 * - Phase du cycle menstruel
 * - Transits lunaires actuels
 * - Thème natal de l'utilisateur
 * 
 * Pour fournir des recommandations personnalisées sur :
 * - Niveau d'énergie
 * - Activités recommandées
 * - Conseils wellness
 */

// Signes du zodiaque avec leurs éléments et qualités
const ZODIAC_DATA = {
  1: { name: 'Bélier', emoji: '♈', element: 'fire', quality: 'cardinal', energy: 90 },
  2: { name: 'Taureau', emoji: '♉', element: 'earth', quality: 'fixed', energy: 70 },
  3: { name: 'Gémeaux', emoji: '♊', element: 'air', quality: 'mutable', energy: 85 },
  4: { name: 'Cancer', emoji: '♋', element: 'water', quality: 'cardinal', energy: 65 },
  5: { name: 'Lion', emoji: '♌', element: 'fire', quality: 'fixed', energy: 95 },
  6: { name: 'Vierge', emoji: '♍', element: 'earth', quality: 'mutable', energy: 75 },
  7: { name: 'Balance', emoji: '♎', element: 'air', quality: 'cardinal', energy: 80 },
  8: { name: 'Scorpion', emoji: '♏', element: 'water', quality: 'fixed', energy: 85 },
  9: { name: 'Sagittaire', emoji: '♐', element: 'fire', quality: 'mutable', energy: 90 },
  10: { name: 'Capricorne', emoji: '♑', element: 'earth', quality: 'cardinal', energy: 70 },
  11: { name: 'Verseau', emoji: '♒', element: 'air', quality: 'fixed', energy: 85 },
  12: { name: 'Poissons', emoji: '♓', element: 'water', quality: 'mutable', energy: 60 },
};

// Phases de cycle avec leurs caractéristiques énergétiques
const CYCLE_PHASES_DATA = {
  menstrual: {
    name: 'Menstruelle',
    emoji: '🌑',
    energyMultiplier: 0.5,
    element: 'water',
    description: 'Phase introspective, idéale pour le repos et la réflexion',
  },
  follicular: {
    name: 'Folliculaire',
    emoji: '🌒',
    energyMultiplier: 0.8,
    element: 'air',
    description: 'Énergie montante, créativité et nouveaux départs',
  },
  ovulation: {
    name: 'Ovulation',
    emoji: '🌕',
    energyMultiplier: 1.0,
    element: 'fire',
    description: 'Pic d\'énergie, communication et sociabilité maximales',
  },
  luteal: {
    name: 'Lutéale',
    emoji: '🌘',
    energyMultiplier: 0.7,
    element: 'earth',
    description: 'Énergie stable, organisation et finalisation des projets',
  },
};

/**
 * Calcule la position approximative de la Lune dans le zodiaque
 * La Lune parcourt le zodiaque en ~28 jours (environ 1 signe tous les 2.3 jours)
 */
function calculateMoonPosition() {
  const now = new Date();
  const startOfYear = new Date(now.getFullYear(), 0, 1);
  const dayOfYear = Math.floor((now - startOfYear) / (1000 * 60 * 60 * 24));
  
  // Position approximative (simplifié)
  const moonCycle = 27.3; // jours lunaires
  const signsPerDay = 12 / moonCycle;
  const currentSign = Math.floor((dayOfYear * signsPerDay) % 12) + 1;
  
  return {
    sign: currentSign,
    ...ZODIAC_DATA[currentSign],
  };
}

/**
 * Calcule le niveau d'énergie en fonction du cycle et des transits
 */
function calculateEnergyLevel(cyclePhase, astroData, moonSign) {
  const phaseData = CYCLE_PHASES_DATA[cyclePhase];
  const baseEnergy = 70;
  
  // Multiplier par la phase du cycle
  let energy = baseEnergy * phaseData.energyMultiplier;
  
  // Bonus si le signe solaire est compatible avec la phase
  const userElement = ZODIAC_DATA[astroData.sunSign?.id || 1]?.element;
  if (userElement === phaseData.element) {
    energy += 10;
  }
  
  // Bonus si la Lune transite en harmonie avec le signe natal
  const moonElement = moonSign.element;
  if (moonElement === userElement) {
    energy += 15;
  } else if (
    (moonElement === 'fire' && userElement === 'air') ||
    (moonElement === 'air' && userElement === 'fire') ||
    (moonElement === 'earth' && userElement === 'water') ||
    (moonElement === 'water' && userElement === 'earth')
  ) {
    energy += 8;
  }
  
  // Arrondir et limiter entre 20 et 100
  return Math.round(Math.max(20, Math.min(100, energy)));
}

/**
 * Génère des recommandations personnalisées
 */
function generateRecommendations(cyclePhase, energyLevel, moonSign, astroData) {
  const recommendations = [];
  
  // Recommandations basées sur la phase du cycle
  if (cyclePhase === 'menstrual') {
    recommendations.push({
      icon: '🛀',
      text: 'Privilégiez le repos et les pratiques douces comme le yin yoga ou la méditation.',
    });
    recommendations.push({
      icon: '🫖',
      text: 'Hydratez-vous bien et optez pour des tisanes chaudes (camomille, gingembre).',
    });
  } else if (cyclePhase === 'follicular') {
    recommendations.push({
      icon: '🏃‍♀️',
      text: 'C\'est le moment idéal pour commencer de nouveaux projets et sortir de votre zone de confort.',
    });
    recommendations.push({
      icon: '🎨',
      text: 'Votre créativité est à son maximum, profitez-en pour des activités artistiques.',
    });
  } else if (cyclePhase === 'ovulation') {
    recommendations.push({
      icon: '💬',
      text: 'Excellente période pour les échanges sociaux, les présentations et la communication.',
    });
    recommendations.push({
      icon: '💪',
      text: 'Votre énergie est au top : parfait pour les entraînements intenses.',
    });
  } else if (cyclePhase === 'luteal') {
    recommendations.push({
      icon: '📋',
      text: 'Finalisez vos projets en cours et organisez votre environnement.',
    });
    recommendations.push({
      icon: '🧘‍♀️',
      text: 'Pratiquez des exercices de respiration pour gérer les éventuelles fluctuations émotionnelles.',
    });
  }
  
  // Recommandations basées sur la Lune
  if (moonSign.element === 'fire') {
    recommendations.push({
      icon: '🔥',
      text: `Lune en ${moonSign.name} : Profitez de cette énergie dynamique pour avancer sur vos objectifs.`,
    });
  } else if (moonSign.element === 'water') {
    recommendations.push({
      icon: '🌊',
      text: `Lune en ${moonSign.name} : Écoutez vos émotions et accordez-vous des moments de ressourcement.`,
    });
  } else if (moonSign.element === 'earth') {
    recommendations.push({
      icon: '🌱',
      text: `Lune en ${moonSign.name} : Ancrez-vous dans des activités concrètes et pratiques.`,
    });
  } else if (moonSign.element === 'air') {
    recommendations.push({
      icon: '💨',
      text: `Lune en ${moonSign.name} : Période favorable pour l'apprentissage et les échanges intellectuels.`,
    });
  }
  
  return recommendations;
}

/**
 * Génère les meilleures activités selon la phase et les transits
 */
function generateBestActivities(cyclePhase, energyLevel, moonSign) {
  const activities = [];
  
  if (cyclePhase === 'menstrual') {
    activities.push({
      emoji: '📖',
      name: 'Lecture & Journaling',
      description: 'Prenez du temps pour vous et notez vos réflexions.',
    });
    activities.push({
      emoji: '🧘‍♀️',
      name: 'Yoga doux',
      description: 'Yin yoga, étirements légers, respiration.',
    });
  } else if (cyclePhase === 'follicular') {
    activities.push({
      emoji: '🎯',
      name: 'Nouveaux projets',
      description: 'Lancez ce que vous aviez en tête depuis longtemps.',
    });
    activities.push({
      emoji: '🏃‍♀️',
      name: 'Cardio & Sport',
      description: 'Course, danse, HIIT - votre corps est prêt.',
    });
  } else if (cyclePhase === 'ovulation') {
    activities.push({
      emoji: '🎤',
      name: 'Présentation publique',
      description: 'Votre charisme est au maximum, profitez-en.',
    });
    activities.push({
      emoji: '👥',
      name: 'Socialisation',
      description: 'Sortez, rencontrez du monde, connectez-vous.',
    });
  } else if (cyclePhase === 'luteal') {
    activities.push({
      emoji: '✅',
      name: 'Finaliser & Organiser',
      description: 'Terminez vos tâches en cours et faites le tri.',
    });
    activities.push({
      emoji: '🍲',
      name: 'Meal prep & Routine',
      description: 'Préparez vos repas et établissez des routines.',
    });
  }
  
  return activities;
}

/**
 * Analyse complète Cycle + Astrologie
 */
export async function analyzeCycleAstro({ cycleData, astroData, birthDate }) {
  try {
    // Calculer la position lunaire actuelle
    const moonSign = calculateMoonPosition();
    
    // Calculer le niveau d'énergie
    const energyLevel = calculateEnergyLevel(
      cycleData.phase,
      astroData,
      moonSign
    );
    
    // Générer les recommandations
    const recommendations = generateRecommendations(
      cycleData.phase,
      energyLevel,
      moonSign,
      astroData
    );
    
    // Générer les activités recommandées
    const bestActivities = generateBestActivities(
      cycleData.phase,
      energyLevel,
      moonSign
    );
    
    // Informations sur les transits
    const transitInfo = {
      moonSign,
      description: `La Lune transite actuellement en ${moonSign.name} ${moonSign.emoji}, un signe ${moonSign.element === 'fire' ? 'de feu' : moonSign.element === 'earth' ? 'de terre' : moonSign.element === 'air' ? 'd\'air' : 'd\'eau'}, favorisant ${moonSign.element === 'fire' ? 'l\'action et l\'initiative' : moonSign.element === 'earth' ? 'la stabilité et le concret' : moonSign.element === 'air' ? 'la communication et les idées' : 'l\'intuition et les émotions'}.`,
      aspect: energyLevel > 75 ? 'Harmonieux (trigone)' : energyLevel > 50 ? 'Neutre' : 'Tendu (carré)',
    };
    
    // Phase lunaire (approximation)
    const phaseData = CYCLE_PHASES_DATA[cycleData.phase];
    const moonPhase = {
      emoji: phaseData.emoji,
      name: phaseData.name,
    };
    
    return {
      success: true,
      energyLevel,
      moonPhase,
      transitInfo,
      recommendations,
      bestActivities,
      cyclePhase: cycleData.phase,
      dayOfCycle: cycleData.dayOfCycle,
      timestamp: new Date().toISOString(),
    };
  } catch (error) {
    console.error('[CycleAstroService] Analyze error:', error);
    throw error;
  }
}

/**
 * Sauvegarde l'analyse dans AsyncStorage et Supabase
 */
export async function saveCycleAnalysis({ cycleData, analysis, astroData }) {
  const timestamp = Date.now();
  const analysisToSave = {
    id: `cycle_astro_${timestamp}`,
    type: 'cycle-astro',
    cycleData,
    analysis,
    astroData,
    created_at: new Date().toISOString(),
  };
  
  try {
    // Sauvegarder dans AsyncStorage (local)
    await AsyncStorage.setItem(
      `cycle_astro_${timestamp}`,
      JSON.stringify(analysisToSave)
    );
    console.log('[CycleAstroService] Saved to AsyncStorage');
    
    // Sauvegarder dans Supabase (si disponible)
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (user) {
        // Créer une table cycle_analyses si elle n'existe pas encore
        // Pour l'instant, on stocke dans compatibility_history avec un type spécial
        const { error: supabaseError } = await supabase
          .from('compatibility_history')
          .insert({
            user_id: user.id,
            type: 'cycle-astro',
            person1_data: {
              cyclePhase: cycleData.phase,
              dayOfCycle: cycleData.dayOfCycle,
              mood: cycleData.mood,
            },
            person2_data: {
              astroData: astroData,
            },
            compatibility_score: analysis.energyLevel,
            interpretation: JSON.stringify(analysis),
          });
        
        if (supabaseError) {
          console.warn('[CycleAstroService] Supabase save warning:', supabaseError.message);
        } else {
          console.log('[CycleAstroService] Saved to Supabase');
        }
      }
    } catch (supabaseError) {
      console.warn('[CycleAstroService] Supabase not available:', supabaseError.message);
    }
    
    return analysisToSave;
  } catch (error) {
    console.error('[CycleAstroService] Save error:', error);
    throw error;
  }
}

/**
 * Récupère l'historique des analyses Cycle & Astrologie
 */
export async function getCycleHistory(limit = 20) {
  try {
    // Récupérer depuis AsyncStorage
    const keys = await AsyncStorage.getAllKeys();
    const cycleKeys = keys.filter(key => key.startsWith('cycle_astro_'));
    
    const analyses = await Promise.all(
      cycleKeys.map(async (key) => {
        const data = await AsyncStorage.getItem(key);
        return data ? JSON.parse(data) : null;
      })
    );
    
    // Filtrer les null et trier par date
    const validAnalyses = analyses
      .filter(a => a !== null)
      .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      .slice(0, limit);
    
    return validAnalyses;
  } catch (error) {
    console.error('[CycleAstroService] Get history error:', error);
    return [];
  }
}

/**
 * Supprime une analyse
 */
export async function deleteCycleAnalysis(id) {
  try {
    await AsyncStorage.removeItem(id);
    console.log('[CycleAstroService] Deleted:', id);
    return true;
  } catch (error) {
    console.error('[CycleAstroService] Delete error:', error);
    return false;
  }
}

