/**
 * Service de calcul position lunaire
 * Algorithme simplifié pour signe lunaire quotidien
 */

const ZODIAC_SIGNS = [
  { name: 'Bélier', emoji: '♈', element: 'Feu', energy: 'Initiative et action' },
  { name: 'Taureau', emoji: '♉', element: 'Terre', energy: 'Stabilité et sensualité' },
  { name: 'Gémeaux', emoji: '♊', element: 'Air', energy: 'Communication et curiosité' },
  { name: 'Cancer', emoji: '♋', element: 'Eau', energy: 'Émotions et intuition' },
  { name: 'Lion', emoji: '♌', element: 'Feu', energy: 'Créativité et expression' },
  { name: 'Vierge', emoji: '♍', element: 'Terre', energy: 'Analyse et organisation' },
  { name: 'Balance', emoji: '♎', element: 'Air', energy: 'Harmonie et lien social' },
  { name: 'Scorpion', emoji: '♏', element: 'Eau', energy: 'Transformation et profondeur' },
  { name: 'Sagittaire', emoji: '♐', element: 'Feu', energy: 'Exploration et optimisme' },
  { name: 'Capricorne', emoji: '♑', element: 'Terre', energy: 'Ambition et structure' },
  { name: 'Verseau', emoji: '♒', element: 'Air', energy: 'Innovation et liberté' },
  { name: 'Poissons', emoji: '♓', element: 'Eau', energy: 'Compassion et rêverie' },
];

/**
 * Calcule le signe lunaire du jour (algorithme simplifié)
 * La Lune change de signe tous les ~2.5 jours
 * 
 * Note : Pour une précision professionnelle, utiliser une API d'éphémérides
 * Ici on utilise un algorithme simplifié basé sur la progression annuelle
 * 
 * @param {Date} date - Date à calculer (défaut : aujourd'hui)
 * @returns {Object} { name, emoji, element, energy }
 */
export function getTodayMoonSign(date = new Date()) {
  // Algorithme simplifié :
  // La Lune fait un cycle complet du zodiaque en ~27.3 jours
  // Elle passe ~2.3 jours par signe (27.3 / 12)
  
  // Référence : 1er janvier 2025, la Lune était en Gémeaux (index 2)
  const referenceDate = new Date('2025-01-01T00:00:00Z');
  const referenceSignIndex = 2; // Gémeaux
  
  // Calculer jours depuis référence
  const diffTime = date - referenceDate;
  const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
  
  // Calculer progression dans le zodiaque
  // Lune fait 1 tour complet (12 signes) en 27.3 jours
  const lunarCycleDays = 27.3;
  const progress = diffDays / lunarCycleDays;
  const signsPassed = Math.floor(progress * 12);
  
  // Index du signe actuel
  const currentSignIndex = (referenceSignIndex + signsPassed) % 12;
  
  return ZODIAC_SIGNS[currentSignIndex];
}

/**
 * Calcule la phase lunaire actuelle
 * Nouvelle lune, Premier quartier, Pleine lune, Dernier quartier
 * 
 * @param {Date} date - Date à calculer (défaut : aujourd'hui)
 * @returns {Object} { phaseName, emoji, illumination }
 */
export function getMoonPhase(date = new Date()) {
  // Algorithme simplifié :
  // Lunaison complète = ~29.53 jours
  
  // Référence : 1er janvier 2025 = Nouvelle lune
  const referenceNewMoon = new Date('2025-01-01T00:00:00Z');
  const lunationDays = 29.53;
  
  // Calculer jours depuis dernière nouvelle lune
  const diffTime = date - referenceNewMoon;
  const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
  const dayInLunation = diffDays % lunationDays;
  
  // Calculer pourcentage illumination
  const illumination = Math.round(Math.abs(Math.cos(dayInLunation / lunationDays * 2 * Math.PI)) * 100);
  
  // Déterminer phase
  let phaseName = '';
  let emoji = '';
  
  if (dayInLunation < 3.7) {
    phaseName = 'Nouvelle lune';
    emoji = '🌑';
  } else if (dayInLunation < 7.4) {
    phaseName = 'Premier croissant';
    emoji = '🌒';
  } else if (dayInLunation < 11.1) {
    phaseName = 'Premier quartier';
    emoji = '🌓';
  } else if (dayInLunation < 14.8) {
    phaseName = 'Gibbeuse croissante';
    emoji = '🌔';
  } else if (dayInLunation < 18.5) {
    phaseName = 'Pleine lune';
    emoji = '🌕';
  } else if (dayInLunation < 22.2) {
    phaseName = 'Gibbeuse décroissante';
    emoji = '🌖';
  } else if (dayInLunation < 25.9) {
    phaseName = 'Dernier quartier';
    emoji = '🌗';
  } else {
    phaseName = 'Dernier croissant';
    emoji = '🌘';
  }
  
  return {
    phaseName,
    emoji,
    illumination,
    dayInLunation: Math.round(dayInLunation),
  };
}

/**
 * Retourne un mantra adapté au signe lunaire
 * @param {Object} moonSign - Signe lunaire (de getTodayMoonSign)
 * @returns {string} Mantra/conseil du jour
 */
export function getMoonSignMantra(moonSign) {
  const mantras = {
    'Bélier': 'Ose et avance avec courage.',
    'Taureau': 'Ancre-toi et savoure l\'instant présent.',
    'Gémeaux': 'Communique et connecte avec curiosité.',
    'Cancer': 'Écoute ton intuition et prends soin de toi.',
    'Lion': 'Brille et exprime ta créativité.',
    'Vierge': 'Organise et perfectionne avec soin.',
    'Balance': 'Recherche l\'harmonie et l\'équilibre.',
    'Scorpion': 'Plonge en profondeur et transforme-toi.',
    'Sagittaire': 'Explore et reste optimiste.',
    'Capricorne': 'Structure et avance vers tes objectifs.',
    'Verseau': 'Innove et libère-toi des conventions.',
    'Poissons': 'Rêve et fais confiance à ton intuition.',
  };
  
  return mantras[moonSign.name] || 'Suis le flow cosmique du jour.';
}

/**
 * Contexte lunaire complet pour le jour
 * @returns {Object} Toutes les infos lunaires
 */
export function getTodayMoonContext() {
  const sign = getTodayMoonSign();
  const phase = getMoonPhase();
  const mantra = getMoonSignMantra(sign);
  
  return {
    sign,
    phase,
    mantra,
    displayText: `Lune en ${sign.name} ${sign.emoji}`,
  };
}

/**
 * Cache les données lunaires (change 1x/jour)
 */
let cachedMoonData = null;
let cacheDate = null;

export function getCachedMoonContext() {
  const today = new Date().toDateString();
  
  if (cachedMoonData && cacheDate === today) {
    return cachedMoonData;
  }
  
  cachedMoonData = getTodayMoonContext();
  cacheDate = today;
  
  return cachedMoonData;
}

// Les fonctions sont déjà exportées individuellement ci-dessus
// Pas besoin de ré-exporter

