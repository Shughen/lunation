/**
 * Service de suggestions de tags intelligents pour le journal
 * Basé sur la phase du cycle et les transits lunaires
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { calculateCurrentCycle } from './cycleCalculator';

/**
 * Génère des suggestions de tags selon la phase actuelle
 */
export async function getSuggestedTags() {
  try {
    const cycleConfig = await AsyncStorage.getItem('cycle_config');
    
    if (!cycleConfig) {
      return getDefaultTags();
    }

    const { lastPeriodDate, cycleLength } = JSON.parse(cycleConfig);
    const current = calculateCurrentCycle(lastPeriodDate, cycleLength);
    
    return getTagsByPhase(current.phase);
  } catch (error) {
    console.error('[TagSuggestion] Error:', error);
    return getDefaultTags();
  }
}

/**
 * Tags par phase du cycle
 */
function getTagsByPhase(phase) {
  const tagsByPhase = {
    menstrual: [
      '🛀 Repos',
      '💧 Hydratation',
      '🌊 Introspection',
      '😴 Fatigue',
      '🧘‍♀️ Douceur',
      '📖 Lecture',
    ],
    follicular: [
      '⚡ Énergie',
      '🎨 Créativité',
      '🌱 Nouveau départ',
      '💪 Sport',
      '✨ Motivation',
      '🚀 Productivité',
    ],
    ovulation: [
      '💬 Communication',
      '👥 Social',
      '💃 Confiance',
      '🎤 Expression',
      '❤️ Connexion',
      '🌟 Rayonnement',
    ],
    luteal: [
      '📋 Organisation',
      '🏠 Cocooning',
      '🍂 Ralentissement',
      '🧠 Réflexion',
      '🍲 Nutrition',
      '😌 Calme',
    ],
  };

  return tagsByPhase[phase] || getDefaultTags();
}

/**
 * Tags par défaut (si pas de config cycle)
 */
function getDefaultTags() {
  return [
    '😊 Bonne humeur',
    '💭 Pensif',
    '⚡ Énergique',
    '😴 Fatigué',
    '❤️ Amour',
    '🌈 Gratitude',
  ];
}

/**
 * Tags contextuels selon l'humeur sélectionnée
 */
export function getTagsByMood(mood) {
  const tagsByMood = {
    amazing: [
      '🎉 Accomplissement',
      '✨ Joie',
      '💖 Amour',
      '🌈 Gratitude',
      '🚀 Énergie débordante',
    ],
    happy: [
      '😊 Contentement',
      '☀️ Positif',
      '🌸 Léger',
      '💫 Bien-être',
      '🌻 Optimisme',
    ],
    neutral: [
      '😐 Équilibre',
      '🧘 Neutre',
      '📚 Routine',
      '☁️ Tranquille',
      '🌙 Observation',
    ],
    sad: [
      '😢 Tristesse',
      '💔 Mélancolie',
      '🌧️ Bas',
      '😔 Solitude',
      '🍂 Lourd',
    ],
    anxious: [
      '😰 Stress',
      '💭 Inquiétude',
      '⚠️ Anxiété',
      '😣 Tension',
      '🌀 Surcharge',
    ],
  };

  return tagsByMood[mood] || [];
}

/**
 * Combine suggestions phase + humeur pour liste intelligente
 */
export async function getSmartTagSuggestions(mood = null) {
  const phaseTags = await getSuggestedTags();
  
  if (!mood) {
    return phaseTags.slice(0, 6);
  }

  const moodTags = getTagsByMood(mood);
  
  // Combiner : 3 tags phase + 3 tags humeur
  const combined = [
    ...phaseTags.slice(0, 3),
    ...moodTags.slice(0, 3),
  ];

  return combined;
}

export default {
  getSuggestedTags,
  getTagsByMood,
  getSmartTagSuggestions,
};

