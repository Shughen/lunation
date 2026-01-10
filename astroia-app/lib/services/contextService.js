/**
 * Service de contexte pour enrichir les prompts IA
 * Fournit le contexte complet : cycle, humeur, profil astro
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { useProfileStore } from '@/stores/profileStore';

/**
 * Récupère les données du cycle actuel
 */
export async function getCycleData() {
  try {
    // Récupérer la config cycle depuis AsyncStorage
    const cycleConfig = await AsyncStorage.getItem('cycle_config');
    
    if (!cycleConfig) {
      return null;
    }
    
    const { lastPeriodDate, cycleLength = 28 } = JSON.parse(cycleConfig);
    
    // Calculer le jour du cycle actuel
    const lastPeriod = new Date(lastPeriodDate);
    const today = new Date();
    const diffTime = Math.abs(today - lastPeriod);
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    const dayOfCycle = (diffDays % cycleLength) + 1;
    
    // Déterminer la phase
    let phase = 'menstrual';
    let phaseDay = '';
    let energyLevel = 50;
    
    if (dayOfCycle <= 5) {
      phase = 'menstrual';
      phaseDay = `J${dayOfCycle}/5`;
      energyLevel = 30 + (dayOfCycle * 4); // 30-50%
    } else if (dayOfCycle <= 13) {
      phase = 'follicular';
      phaseDay = `J${dayOfCycle - 5}/8`;
      energyLevel = 50 + ((dayOfCycle - 5) * 5); // 50-90%
    } else if (dayOfCycle <= 16) {
      phase = 'ovulation';
      phaseDay = `J${dayOfCycle - 13}/3`;
      energyLevel = 90 + ((dayOfCycle - 13) * 3); // 90-100%
    } else {
      phase = 'luteal';
      phaseDay = `J${dayOfCycle - 16}/${cycleLength - 16}`;
      const luteaDays = cycleLength - 16;
      const currentLutealDay = dayOfCycle - 16;
      energyLevel = 85 - (currentLutealDay / luteaDays) * 55; // 85-30%
    }
    
    return {
      dayOfCycle,
      phase,
      phaseDay,
      energyLevel: Math.round(energyLevel),
      cycleLength,
    };
  } catch (error) {
    console.error('[ContextService] Error getting cycle data:', error);
    return null;
  }
}

/**
 * Récupère la dernière humeur enregistrée
 */
async function getLatestMood() {
  try {
    const keys = await AsyncStorage.getAllKeys();
    const journalKeys = keys
      .filter(k => k.startsWith('journal_'))
      .sort()
      .reverse();
    
    if (journalKeys.length === 0) {
      return null;
    }
    
    const latestEntry = await AsyncStorage.getItem(journalKeys[0]);
    if (!latestEntry) {
      return null;
    }
    
    const entry = JSON.parse(latestEntry);
    return {
      mood: entry.mood,
      date: entry.date,
    };
  } catch (error) {
    console.error('[ContextService] Error getting latest mood:', error);
    return null;
  }
}

/**
 * Récupère le profil astrologique
 */
function getProfile() {
  try {
    const profile = useProfileStore.getState().profile;
    return {
      name: profile.name || null,
      sunSign: profile.sunSign?.name || null,
      moonSign: profile.moonSign?.name || null,
      ascendant: profile.ascendant?.name || null,
    };
  } catch (error) {
    console.error('[ContextService] Error getting profile:', error);
    return {
      name: null,
      sunSign: null,
      moonSign: null,
      ascendant: null,
    };
  }
}

/**
 * PHASE DESCRIPTIONS pour contexte IA
 */
const PHASE_DESCRIPTIONS = {
  menstrual: {
    name: 'Menstruelle',
    emoji: '🌑',
    keywords: ['repos', 'introspection', 'renouveau', 'lâcher-prise'],
    energy: 'basse à montante',
    recommendations: [
      'Privilégie le repos et l\'hydratation',
      'Évite les activités trop intenses',
      'Accorde-toi du temps pour toi',
      'Journaling et méditation recommandés',
    ],
  },
  follicular: {
    name: 'Folliculaire',
    emoji: '🌒',
    keywords: ['créativité', 'nouveaux projets', 'énergie montante', 'optimisme'],
    energy: 'montante',
    recommendations: [
      'Lance de nouveaux projets',
      'Planifie tes objectifs du mois',
      'Socialise et connecte avec les autres',
      'Activité physique modérée à intense',
    ],
  },
  ovulation: {
    name: 'Ovulation',
    emoji: '🌕',
    keywords: ['pic d\'énergie', 'communication', 'charisme', 'fertilité'],
    energy: 'maximale',
    recommendations: [
      'Moments importants et réunions clés',
      'Expression de soi et créativité',
      'Sport intense si tu en as envie',
      'Moments de qualité avec tes proches',
    ],
  },
  luteal: {
    name: 'Lutéale',
    emoji: '🌘',
    keywords: ['ralentissement', 'introspection', 'cocooning', 'énergie descendante'],
    energy: 'descendante',
    recommendations: [
      'Termine les projets en cours',
      'Prends soin de toi (self-care)',
      'Ralentis progressivement',
      'Alimentation douce et réconfortante',
    ],
  },
};

/**
 * Génère le contexte complet pour enrichir les prompts IA
 * @returns {Promise<Object>}
 */
export async function getAIContext() {
  try {
    const cycleData = await getCycleData();
    const mood = await getLatestMood();
    const profile = getProfile();
    
    // Contexte textuel pour les prompts
    let contextText = '';
    
    // 1. Profil
    if (profile.name) {
      contextText += `Tu t'adresses à ${profile.name}. `;
    }
    if (profile.sunSign) {
      contextText += `Signe solaire : ${profile.sunSign}. `;
    }
    if (profile.moonSign) {
      contextText += `Signe lunaire : ${profile.moonSign}. `;
    }
    
    // 2. Cycle menstruel
    if (cycleData) {
      const phaseInfo = PHASE_DESCRIPTIONS[cycleData.phase];
      contextText += `\n\nCYCLE MENSTRUEL:\n`;
      contextText += `- Phase actuelle : ${phaseInfo.name} ${phaseInfo.emoji} (${cycleData.phaseDay})\n`;
      contextText += `- Jour du cycle : ${cycleData.dayOfCycle}/${cycleData.cycleLength}\n`;
      contextText += `- Niveau d'énergie : ${cycleData.energyLevel}%\n`;
      contextText += `- Énergie typique : ${phaseInfo.energy}\n`;
      contextText += `- Mots-clés phase : ${phaseInfo.keywords.join(', ')}\n`;
    }
    
    // 3. Humeur récente
    if (mood) {
      contextText += `\n\nHUMEUR RÉCENTE:\n`;
      contextText += `- Dernière humeur : ${mood.mood}\n`;
      contextText += `- Date : ${new Date(mood.date).toLocaleDateString('fr-FR')}\n`;
    }
    
    return {
      // Données brutes
      cycle: cycleData,
      mood,
      profile,
      
      // Texte formaté pour prompt
      contextText,
      
      // Phase info détaillée
      phaseInfo: cycleData ? PHASE_DESCRIPTIONS[cycleData.phase] : null,
    };
  } catch (error) {
    console.error('[ContextService] Error getting AI context:', error);
    return {
      cycle: null,
      mood: null,
      profile: getProfile(),
      contextText: '',
      phaseInfo: null,
    };
  }
}

/**
 * Génère des recommandations adaptées à la phase actuelle
 * @returns {Promise<string[]>}
 */
export async function getPhaseRecommendations() {
  try {
    const cycleData = await getCycleData();
    
    if (!cycleData) {
      return [
        'Configure ton cycle pour recevoir des recommandations personnalisées',
      ];
    }
    
    const phaseInfo = PHASE_DESCRIPTIONS[cycleData.phase];
    return phaseInfo.recommendations;
  } catch (error) {
    console.error('[ContextService] Error getting recommendations:', error);
    return [];
  }
}

/**
 * Vérifie si le contexte cycle est disponible
 * @returns {Promise<boolean>}
 */
export async function hasCycleContext() {
  const cycleData = await getCycleData();
  return cycleData !== null;
}

export default {
  getAIContext,
  getPhaseRecommendations,
  hasCycleContext,
  getCycleData,
};

