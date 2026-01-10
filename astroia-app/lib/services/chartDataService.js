/**
 * Service de préparation des données pour les graphiques
 * Transforme les données brutes en format compatible avec react-native-chart-kit
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { calculateCurrentCycle } from './cycleCalculator';

/**
 * Récupère les données du journal des 30 derniers jours
 */
export async function getLast30DaysJournal() {
  try {
    const allKeys = await AsyncStorage.getAllKeys();
    const journalKeys = allKeys.filter(k => k.startsWith('journal_'));
    
    const journalEntries = [];
    for (const key of journalKeys) {
      const data = await AsyncStorage.getItem(key);
      if (data) {
        journalEntries.push(JSON.parse(data));
      }
    }
    
    // Trier par date et garder 30 derniers jours
    const today = new Date();
    const thirtyDaysAgo = new Date(today - 30 * 24 * 60 * 60 * 1000);
    
    return journalEntries
      .filter(entry => new Date(entry.date || entry.created_at) >= thirtyDaysAgo)
      .sort((a, b) => new Date(a.date || a.created_at) - new Date(b.date || b.created_at));
  } catch (error) {
    console.error('[ChartDataService] Get journal error:', error);
    return [];
  }
}

/**
 * Prépare les données pour le graphique Mood vs Cycle (30 jours)
 */
export async function prepareMoodCycleData() {
  try {
    const journalEntries = await getLast30DaysJournal();
    const cycleConfig = await AsyncStorage.getItem('cycle_config');
    
    if (!cycleConfig || journalEntries.length === 0) {
      return null;
    }
    
    const { lastPeriodDate, cycleLength } = JSON.parse(cycleConfig);
    
    // Mapper les humeurs à des valeurs numériques
    const moodValues = {
      amazing: 5,
      happy: 4,
      neutral: 3,
      sad: 2,
      anxious: 1,
    };
    
    // Préparer les labels (dates) et les données
    const labels = [];
    const data = [];
    const phaseColors = [];
    
    journalEntries.forEach(entry => {
      const date = new Date(entry.date || entry.created_at);
      const daysSince = Math.floor((date - new Date(lastPeriodDate)) / (1000 * 60 * 60 * 24));
      const dayOfCycle = (daysSince % cycleLength) + 1;
      
      // Déterminer la phase
      let phaseColor = '#FF6B9D'; // menstrual
      if (dayOfCycle > 16) phaseColor = '#C084FC'; // luteal
      else if (dayOfCycle > 13) phaseColor = '#FFD93D'; // ovulation
      else if (dayOfCycle > 5) phaseColor = '#FFB347'; // follicular
      
      labels.push(date.getDate()); // Jour du mois
      data.push(moodValues[entry.mood] || 3);
      phaseColors.push(phaseColor);
    });
    
    return {
      labels,
      datasets: [
        {
          data,
          color: (opacity = 1) => `rgba(255, 182, 193, ${opacity})`,
          strokeWidth: 3,
        },
      ],
      phaseColors, // Pour background coloré
    };
  } catch (error) {
    console.error('[ChartDataService] Prepare mood cycle error:', error);
    return null;
  }
}

/**
 * Calcule les moyennes d'énergie par phase (90 jours)
 */
export async function prepareEnergyCycleData() {
  try {
    const journalEntries = await getLast30DaysJournal(); // On garde 30j pour MVP
    
    if (journalEntries.length === 0) {
      return null;
    }
    
    // Grouper par phase et calculer moyenne
    const energyByPhase = {
      menstrual: [],
      follicular: [],
      ovulation: [],
      luteal: [],
    };
    
    const cycleConfig = await AsyncStorage.getItem('cycle_config');
    if (!cycleConfig) return null;
    
    const { lastPeriodDate, cycleLength } = JSON.parse(cycleConfig);
    
    journalEntries.forEach(entry => {
      const date = new Date(entry.date || entry.created_at);
      const daysSince = Math.floor((date - new Date(lastPeriodDate)) / (1000 * 60 * 60 * 24));
      const dayOfCycle = (daysSince % cycleLength) + 1;
      
      // Déterminer phase
      let phase = 'menstrual';
      if (dayOfCycle > 16) phase = 'luteal';
      else if (dayOfCycle > 13) phase = 'ovulation';
      else if (dayOfCycle > 5) phase = 'follicular';
      
      // Mapper mood à énergie (1-5)
      const moodEnergy = {
        amazing: 5,
        happy: 4,
        neutral: 3,
        sad: 2,
        anxious: 1,
      };
      
      energyByPhase[phase].push(moodEnergy[entry.mood] || 3);
    });
    
    // Calculer moyennes
    const averages = {};
    Object.keys(energyByPhase).forEach(phase => {
      const values = energyByPhase[phase];
      averages[phase] = values.length > 0
        ? Math.round(values.reduce((a, b) => a + b, 0) / values.length * 20) // Sur 100
        : 0;
    });
    
    return {
      labels: ['Menstruelle', 'Folliculaire', 'Ovulation', 'Lutéale'],
      datasets: [
        {
          data: [
            averages.menstrual || 45,
            averages.follicular || 75,
            averages.ovulation || 95,
            averages.luteal || 65,
          ],
          color: (opacity = 1) => `rgba(255, 182, 193, ${opacity})`,
          strokeWidth: 3,
        },
      ],
    };
  } catch (error) {
    console.error('[ChartDataService] Prepare energy error:', error);
    return null;
  }
}

/**
 * Génère des insights automatiques basés sur les données
 */
export async function generateInsights() {
  try {
    const journalEntries = await getLast30DaysJournal();
    const cycleConfig = await AsyncStorage.getItem('cycle_config');
    
    if (!cycleConfig || journalEntries.length < 7) {
      return [];
    }
    
    const { lastPeriodDate, cycleLength } = JSON.parse(cycleConfig);
    const insights = [];
    
    // 🆕 Récupérer le contexte cycle actuel
    const { getAIContext } = await import('./contextService');
    const aiContext = await getAIContext();
    const currentPhase = aiContext.cycle?.phase;
    
    // Insight 1 : Phase avec plus d'énergie
    const energyByPhase = {
      menstrual: [],
      follicular: [],
      ovulation: [],
      luteal: [],
    };
    
    journalEntries.forEach(entry => {
      const date = new Date(entry.date || entry.created_at);
      const daysSince = Math.floor((date - new Date(lastPeriodDate)) / (1000 * 60 * 60 * 24));
      const dayOfCycle = (daysSince % cycleLength) + 1;
      
      let phase = 'menstrual';
      if (dayOfCycle > 16) phase = 'luteal';
      else if (dayOfCycle > 13) phase = 'ovulation';
      else if (dayOfCycle > 5) phase = 'follicular';
      
      const moodScore = { amazing: 5, happy: 4, neutral: 3, sad: 2, anxious: 1 }[entry.mood] || 3;
      energyByPhase[phase].push(moodScore);
    });
    
    // Trouver phase avec meilleure moyenne
    let bestPhase = 'ovulation';
    let bestScore = 0;
    
    Object.keys(energyByPhase).forEach(phase => {
      const values = energyByPhase[phase];
      if (values.length > 0) {
        const avg = values.reduce((a, b) => a + b) / values.length;
        if (avg > bestScore) {
          bestScore = avg;
          bestPhase = phase;
        }
      }
    });
    
    const phaseNames = {
      menstrual: 'menstruelle',
      follicular: 'folliculaire',
      ovulation: 'd\'ovulation',
      luteal: 'lutéale',
    };
    
    insights.push({
      emoji: '⚡',
      text: `Tu es plus énergique en phase ${phaseNames[bestPhase]}`,
    });
    
    // Insight 2 : Fréquence journaling
    const entriesByPhase = {};
    Object.keys(energyByPhase).forEach(phase => {
      entriesByPhase[phase] = energyByPhase[phase].length;
    });
    
    let mostJournaledPhase = Object.keys(entriesByPhase).reduce((a, b) => 
      entriesByPhase[a] > entriesByPhase[b] ? a : b
    );
    
    insights.push({
      emoji: '📖',
      text: `Tu journalises plus en phase ${phaseNames[mostJournaledPhase]}`,
    });
    
    // Insight 3 : Streak
    const streak = journalEntries.length >= 7 ? Math.floor(journalEntries.length / 7) : 0;
    if (streak > 0) {
      insights.push({
        emoji: '🔥',
        text: `Belle régularité : ${journalEntries.length} entrées ce mois !`,
      });
    }
    
    // 🆕 Insight 4 : Recommandation basée sur phase actuelle
    if (currentPhase && aiContext.phaseInfo) {
      const phaseAdvice = {
        menstrual: 'En phase menstruelle : accorde-toi du repos et de la douceur',
        follicular: 'En phase folliculaire : c\'est le moment de lancer tes projets !',
        ovulation: 'En phase d\'ovulation : ton énergie est au max, profites-en !',
        luteal: 'En phase lutéale : temps de ralentir et de te recentrer',
      };
      
      insights.push({
        emoji: aiContext.phaseInfo.emoji,
        text: phaseAdvice[currentPhase],
      });
    }
    
    return insights.slice(0, 5); // Max 5 insights
  } catch (error) {
    console.error('[ChartDataService] Generate insights error:', error);
    return [];
  }
}

export default {
  getLast30DaysJournal,
  prepareMoodCycleData,
  prepareEnergyCycleData,
  generateInsights,
};

