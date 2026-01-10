/**
 * Service de calcul du cycle menstruel
 * Algorithmes précis pour tracking et prédictions
 */

/**
 * Calcule le jour actuel du cycle
 * @param {string|Date} lastPeriodStart - Date des dernières règles
 * @param {number} cycleLength - Durée cycle (défaut 28j)
 * @returns {number} Jour du cycle (1-cycleLength)
 */
export function getCurrentCycleDay(lastPeriodStart, cycleLength = 28) {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  
  const start = new Date(lastPeriodStart);
  start.setHours(0, 0, 0, 0);
  
  const diffTime = today - start;
  const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
  
  // Modulo pour cycles multiples
  const dayOfCycle = (diffDays % cycleLength) + 1;
  
  return dayOfCycle;
}

/**
 * Détermine la phase actuelle du cycle
 * @param {number} cycleDay - Jour du cycle (1-28)
 * @param {number} cycleLength - Durée totale cycle
 * @returns {string} Phase : 'menstrual' | 'follicular' | 'ovulation' | 'luteal'
 */
export function getCurrentPhase(cycleDay, cycleLength = 28) {
  // Adaptation selon durée cycle
  const menstrualEnd = 5;
  const follicularEnd = Math.round(cycleLength * 0.46); // ~46% du cycle
  const ovulationEnd = Math.round(cycleLength * 0.57); // ~57% du cycle
  
  if (cycleDay <= menstrualEnd) {
    return 'menstrual';
  } else if (cycleDay <= follicularEnd) {
    return 'follicular';
  } else if (cycleDay <= ovulationEnd) {
    return 'ovulation';
  } else {
    return 'luteal';
  }
}

/**
 * Retourne les infos détaillées de la phase
 * @param {string} phase - Phase du cycle
 * @returns {Object} Infos phase complètes
 */
export function getPhaseInfo(phase) {
  const phases = {
    menstrual: {
      name: 'Menstruelle',
      emoji: '🌑',
      color: '#FF6B9D',
      gradient: ['#FF6B9D', '#FF8FB3'],
      description: 'Phase de renouveau et introspection',
      keywords: ['repos', 'introspection', 'lâcher-prise', 'douceur'],
      energyRange: [30, 50],
      recommendations: [
        'Accorde-toi du repos et de la douceur',
        'Hydrate-toi abondamment',
        'Privilégie les activités calmes (yoga, méditation)',
        'Écoute ton besoin de solitude',
        'Alimentation réconfortante et chaude',
      ],
    },
    follicular: {
      name: 'Folliculaire',
      emoji: '🌒',
      color: '#FFB347',
      gradient: ['#FFB347', '#FFC670'],
      description: 'Phase de renouveau et créativité',
      keywords: ['créativité', 'projets', 'optimisme', 'énergie montante'],
      energyRange: [50, 90],
      recommendations: [
        'Lance de nouveaux projets personnels ou pros',
        'Planifie tes objectifs du mois',
        'Socialise et connecte avec les autres',
        'Activité physique modérée à intense',
        'Essaie de nouvelles choses',
      ],
    },
    ovulation: {
      name: 'Ovulation',
      emoji: '🌕',
      color: '#FFD93D',
      gradient: ['#FFD93D', '#FFE66D'],
      description: 'Pic d\'énergie et communication',
      keywords: ['pic énergie', 'communication', 'charisme', 'fertilité'],
      energyRange: [90, 100],
      recommendations: [
        'Planifie tes moments importants et réunions clés',
        'Exprime-toi et communique (tu es au top !)',
        'Sport intense si tu en as envie',
        'Moments de qualité avec tes proches',
        'Profite de ton charisme naturel',
      ],
    },
    luteal: {
      name: 'Lutéale',
      emoji: '🌘',
      color: '#C084FC',
      gradient: ['#C084FC', '#D8B4FE'],
      description: 'Phase de ralentissement progressif',
      keywords: ['ralentissement', 'introspection', 'cocooning', 'préparation'],
      energyRange: [85, 30],
      recommendations: [
        'Termine les projets en cours',
        'Prends soin de toi (self-care, bains, lecture)',
        'Ralentis progressivement ton rythme',
        'Alimentation douce et réconfortante',
        'Anticipe SPM (si tu en as) avec douceur',
      ],
    },
  };
  
  return phases[phase] || phases.menstrual;
}

/**
 * Calcule si fenêtre fertile (J10-J17 typiquement)
 * @param {number} cycleDay - Jour du cycle
 * @param {number} cycleLength - Durée totale
 * @returns {boolean} Est fertile
 */
export function isFertile(cycleDay, cycleLength = 28) {
  // Ovulation ~14j avant fin cycle
  const ovulationDay = cycleLength - 14;
  
  // Fenêtre fertile : 5j avant ovulation, 1j après
  const fertileStart = ovulationDay - 5;
  const fertileEnd = ovulationDay + 1;
  
  return cycleDay >= fertileStart && cycleDay <= fertileEnd;
}

/**
 * Prédit la date des prochaines règles
 * @param {string|Date} lastPeriodStart - Dernières règles
 * @param {number} cycleLength - Durée cycle
 * @returns {Date} Date prévue prochaines règles
 */
export function predictNextPeriod(lastPeriodStart, cycleLength = 28) {
  const start = new Date(lastPeriodStart);
  const nextPeriod = new Date(start);
  nextPeriod.setDate(start.getDate() + cycleLength);
  
  return nextPeriod;
}

/**
 * Calcule le niveau d'énergie selon phase + jour
 * @param {string} phase - Phase du cycle
 * @param {number} dayInPhase - Jour dans la phase (0-indexed)
 * @returns {number} Niveau énergie (0-100)
 */
export function calculateEnergyLevel(phase, dayInPhase) {
  const energyMaps = {
    menstrual: [30, 35, 40, 45, 50],                    // J1-5
    follicular: [55, 60, 65, 70, 75, 80, 85, 90],      // J6-13
    ovulation: [95, 100, 95],                           // J14-16
    luteal: [85, 80, 75, 70, 65, 60, 55, 50, 45, 40], // J17-26
  };
  
  const map = energyMaps[phase] || [50];
  const index = Math.min(dayInPhase, map.length - 1);
  
  return map[index];
}

/**
 * Calcule le cycle complet avec toutes les infos
 * @param {string|Date} lastPeriodStart - Dernières règles
 * @param {number} cycleLength - Durée cycle
 * @returns {Object} Infos cycle complètes
 */
export function calculateCurrentCycle(lastPeriodStart, cycleLength = 28) {
  const dayOfCycle = getCurrentCycleDay(lastPeriodStart, cycleLength);
  const phase = getCurrentPhase(dayOfCycle, cycleLength);
  const phaseInfo = getPhaseInfo(phase);
  const fertile = isFertile(dayOfCycle, cycleLength);
  const nextPeriod = predictNextPeriod(lastPeriodStart, cycleLength);
  
  // Calculer jour dans la phase (pour énergie)
  let dayInPhase = 0;
  if (phase === 'menstrual') {
    dayInPhase = dayOfCycle - 1; // J1-5 → index 0-4
  } else if (phase === 'follicular') {
    dayInPhase = dayOfCycle - 6; // J6-13 → index 0-7
  } else if (phase === 'ovulation') {
    dayInPhase = dayOfCycle - 14; // J14-16 → index 0-2
  } else if (phase === 'luteal') {
    const ovulationEnd = Math.round(cycleLength * 0.57);
    dayInPhase = dayOfCycle - ovulationEnd - 1;
  }
  
  const energy = calculateEnergyLevel(phase, dayInPhase);
  
  // Jours restants jusqu'aux prochaines règles
  const daysUntilNextPeriod = cycleLength - dayOfCycle + 1;
  
  return {
    dayOfCycle,
    cycleLength,
    phase,
    phaseInfo,
    dayInPhase,
    energy,
    fertile,
    nextPeriod,
    daysUntilNextPeriod,
  };
}

/**
 * Retourne un conseil adapté à la phase
 * @param {string} phase - Phase du cycle
 * @returns {string} Conseil du jour
 */
export function getPhaseAdvice(phase) {
  const advice = {
    menstrual: 'Aujourd\'hui, ton corps se régénère. Accorde-toi du repos et de la douceur.',
    follicular: 'C\'est le moment parfait pour lancer tes projets ! Ton énergie est montante.',
    ovulation: 'Tu es au sommet de ton énergie ! Profite de ce pic pour briller.',
    luteal: 'Temps de ralentir progressivement. Écoute ton besoin de cocooning.',
  };
  
  return advice[phase] || 'Écoute ton corps et respecte tes besoins du moment.';
}

/**
 * Prédit la date d'ovulation en fonction du cycle moyen
 * Ovulation = 14 jours avant les prochaines règles prédites
 * @param {Date} nextPeriodDate - Date prédite des prochaines règles
 * @param {number} avgCycleLength - Longueur moyenne du cycle
 * @returns {Date} Date d'ovulation estimée
 */
export function predictOvulationDate(nextPeriodDate, avgCycleLength) {
  if (!nextPeriodDate || !avgCycleLength) return null;
  
  const ovulationDate = new Date(nextPeriodDate);
  ovulationDate.setDate(ovulationDate.getDate() - 14); // 14 jours avant règles
  
  return ovulationDate;
}

/**
 * Calcule la fenêtre de fertilité
 * Fenêtre fertile = 5 jours avant ovulation + jour d'ovulation + 1 jour après
 * @param {Date} ovulationDate - Date d'ovulation estimée
 * @returns {{ start: Date, end: Date } | null} Fenêtre de fertilité
 */
export function predictFertilityWindow(ovulationDate) {
  if (!ovulationDate) return null;
  
  const start = new Date(ovulationDate);
  start.setDate(start.getDate() - 5); // 5 jours avant
  
  const end = new Date(ovulationDate);
  end.setDate(end.getDate() + 1); // 1 jour après
  
  return { start, end };
}

/**
 * Génère les marqueurs pour react-native-calendars
 * @param {Array} cycles - Historique des cycles
 * @param {Object} prediction - Prédiction (nextDate, ovulation, fertile)
 * @returns {Object} markedDates pour calendrier
 */
export function generateCalendarMarkers(cycles = [], prediction = null) {
  const markers = {};
  
  // Marqueurs pour cycles passés
  cycles.forEach((cycle) => {
    if (!cycle.startDate) return;
    
    const start = new Date(cycle.startDate);
    const end = cycle.endDate ? new Date(cycle.endDate) : new Date();
    
    // Marquer jours de règles (rose)
    let current = new Date(start);
    while (current <= end) {
      const dateKey = current.toISOString().split('T')[0];
      markers[dateKey] = {
        marked: true,
        dotColor: '#FF6B9D',
        customStyles: {
          container: { backgroundColor: '#FF6B9D22' },
          text: { color: '#FF6B9D', fontWeight: 'bold' },
        },
      };
      current.setDate(current.getDate() + 1);
    }
  });
  
  // Marqueurs pour prédiction future
  if (prediction) {
    // Prochaines règles prédites
    if (prediction.nextDate) {
      const nextStart = new Date(prediction.nextDate);
      for (let i = 0; i < 5; i++) { // 5 jours de règles estimés
        const dateKey = new Date(nextStart);
        dateKey.setDate(dateKey.getDate() + i);
        const key = dateKey.toISOString().split('T')[0];
        markers[key] = {
          marked: true,
          dotColor: '#FF6B9D',
          customStyles: {
            container: { backgroundColor: '#FF6B9D33', borderWidth: 1, borderColor: '#FF6B9D' },
            text: { color: '#FF6B9D', fontWeight: '600' },
          },
        };
      }
    }
    
    // Fenêtre fertile (jaune)
    if (prediction.fertile) {
      let current = new Date(prediction.fertile.start);
      const end = new Date(prediction.fertile.end);
      
      while (current <= end) {
        const dateKey = current.toISOString().split('T')[0];
        // Ne pas écraser les règles
        if (!markers[dateKey]) {
          markers[dateKey] = {
            marked: true,
            dotColor: '#FFD93D',
            customStyles: {
              container: { backgroundColor: '#FFD93D22' },
              text: { color: '#FFD93D', fontWeight: '600' },
            },
          };
        }
        current.setDate(current.getDate() + 1);
      }
    }
    
    // Ovulation (orange)
    if (prediction.ovulation) {
      const ovuKey = new Date(prediction.ovulation).toISOString().split('T')[0];
      markers[ovuKey] = {
        marked: true,
        dotColor: '#FFA500',
        customStyles: {
          container: { backgroundColor: '#FFA50044', borderWidth: 2, borderColor: '#FFA500' },
          text: { color: '#FFA500', fontWeight: 'bold' },
        },
      };
    }
  }
  
  return markers;
}

// Default export pour compatibilité
export default {
  getCurrentCycleDay,
  getCurrentPhase,
  getPhaseInfo,
  isFertile,
  predictNextPeriod,
  calculateEnergyLevel,
  calculateCurrentCycle,
  getPhaseAdvice,
  predictOvulationDate,
  predictFertilityWindow,
  generateCalendarMarkers,
};
