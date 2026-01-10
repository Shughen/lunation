/**
 * Service de génération d'interprétations courtes pour les aspects astrologiques
 * Génère des descriptions en français sans appel API supplémentaire
 */

import { translatePlanet } from './astrologyTranslations';

/**
 * Mots-clés fonctionnels pour chaque planète
 */
const PLANET_KEYWORDS = {
  'Sun': { keyword: 'identité', secondary: 'ego, volonté' },
  'Moon': { keyword: 'émotions', secondary: 'besoins intérieurs' },
  'Mercury': { keyword: 'communication', secondary: 'pensée' },
  'Venus': { keyword: 'affects', secondary: 'relations, valeurs' },
  'Mars': { keyword: 'action', secondary: 'désir, affirmation' },
  'Jupiter': { keyword: 'expansion', secondary: 'foi, chance' },
  'Saturn': { keyword: 'structure', secondary: 'responsabilités' },
  'Uranus': { keyword: 'liberté', secondary: 'changement' },
  'Neptune': { keyword: 'intuition', secondary: 'rêves' },
  'Pluto': { keyword: 'transformation', secondary: 'puissance' },
  'Ascendant': { keyword: 'image', secondary: 'manière d\'aborder le monde' },
  'Medium_Coeli': { keyword: 'vocation', secondary: 'destinée sociale' },
  'Mean_Node': { keyword: 'axe d\'évolution', secondary: 'direction de vie' },
  'Mean_South_Node': { keyword: 'habitudes passées', secondary: 'zone de confort' },
  'Mean_Lilith': { keyword: 'désirs bruts', secondary: 'zones de tabou' },
  'Chiron': { keyword: 'blessure', secondary: 'guérison' },
};

/**
 * Verbes de lien pour chaque type d'aspect
 */
const ASPECT_VERBS = {
  'conjunction': { verb: 'fusionne avec', tone: 'amplification' },
  'opposition': { verb: 'met en tension avec', tone: 'polarisation' },
  'square': { verb: 'crée un défi avec', tone: 'tension dynamique' },
  'trine': { verb: 'facilite l\'harmonie avec', tone: 'fluidité' },
  'sextile': { verb: 'ouvre une opportunité avec', tone: 'potentiel' },
  'quintile': { verb: 'apporte une créativité avec', tone: 'talent' },
  'biquintile': { verb: 'stimule l\'innovation avec', tone: 'génie créatif' },
  'semisextile': { verb: 'crée une légère connexion avec', tone: 'ajustement' },
  'semisquare': { verb: 'génère une friction mineure avec', tone: 'irritation' },
  'sesquisquare': { verb: 'provoque une tension subtile avec', tone: 'contrainte' },
  'quincunx': { verb: 'demande un ajustement avec', tone: 'adaptation' },
};

/**
 * Tonalités selon l'intensité
 */
const INTENSITY_TONES = {
  'strong': 'Influence très marquée',
  'medium': 'Influence importante',
  'weak': 'Influence subtile',
};

/**
 * Génère une interprétation courte pour un aspect
 * @param {Object} aspect - Aspect avec from, to, aspect_type, strength, orb
 * @returns {string} - Description courte en français
 */
export function generateAspectInterpretation(aspect) {
  const { from, to, aspect_type, strength, orb } = aspect;
  
  // Récupérer les infos des planètes
  const planet1 = PLANET_KEYWORDS[from] || { keyword: translatePlanet(from), secondary: '' };
  const planet2 = PLANET_KEYWORDS[to] || { keyword: translatePlanet(to), secondary: '' };
  
  // Récupérer le verbe d'aspect
  const aspectInfo = ASPECT_VERBS[aspect_type] || { verb: 'interagit avec', tone: 'dynamique' };
  
  // Intensité
  const intensityStr = INTENSITY_TONES[strength] || 'Influence modérée';
  
  // Construction de la phrase
  const description = `${intensityStr} : ${planet1.keyword} ${aspectInfo.verb} ${planet2.keyword}.`;
  
  // Ajouter une nuance si orbe très proche (< 1°)
  if (Math.abs(orb) < 1.0) {
    return `${description} Aspect exact, effet puissant.`;
  }
  
  return description;
}

/**
 * Génère une interprétation plus détaillée pour un aspect
 * @param {Object} aspect - Aspect complet
 * @returns {string} - Description détaillée
 */
export function generateDetailedAspectInterpretation(aspect) {
  const { from, to, aspect_type, strength, orb } = aspect;
  
  const planet1 = PLANET_KEYWORDS[from];
  const planet2 = PLANET_KEYWORDS[to];
  const aspectInfo = ASPECT_VERBS[aspect_type];
  
  if (!planet1 || !planet2 || !aspectInfo) {
    return generateAspectInterpretation(aspect);
  }
  
  const intensityStr = INTENSITY_TONES[strength] || 'Influence modérée';
  const p1Name = translatePlanet(from);
  const p2Name = translatePlanet(to);
  
  // Phrase principale
  let description = `${intensityStr} : ${p1Name} (${planet1.secondary}) ${aspectInfo.verb} ${p2Name} (${planet2.secondary}). `;
  
  // Ajout selon le type d'aspect
  switch (aspect_type) {
    case 'conjunction':
      description += `Ces énergies fusionnent et s'amplifient mutuellement.`;
      break;
    case 'opposition':
      description += `Une tension créative qui demande équilibre et intégration.`;
      break;
    case 'square':
      description += `Un défi dynamique qui pousse à l'action et au dépassement.`;
      break;
    case 'trine':
      description += `Une harmonie naturelle qui facilite l'expression.`;
      break;
    case 'sextile':
      description += `Une opportunité à saisir qui demande un effort conscient.`;
      break;
    default:
      description += `Tonalité : ${aspectInfo.tone}.`;
  }
  
  // Note sur l'orbe
  if (Math.abs(orb) < 1.0) {
    description += ` Aspect exact (orbe ${Math.abs(orb).toFixed(2)}°), effet maximal.`;
  } else if (Math.abs(orb) > 5.0) {
    description += ` Orbe large (${Math.abs(orb).toFixed(2)}°), effet atténué.`;
  }
  
  return description;
}

/**
 * Aspects majeurs (utilisés dans la section "Aspects clés du thème")
 */
export const MAJOR_ASPECTS = [
  'conjunction',  // Conjonction
  'opposition',   // Opposition
  'square',       // Carré
  'trine',        // Trigone
  'sextile',      // Sextile
];

/**
 * Catégories d'aspects selon l'astrologie classique
 */
export const ASPECT_CATEGORIES = {
  // Aspects tendus majeurs
  'major_tense': ['conjunction', 'opposition', 'square'],
  // Aspects harmonieux majeurs
  'major_harmonious': ['trine', 'sextile'],
  // Aspects mineurs (tous les autres)
  'minor': [], // Sera rempli dynamiquement pour tout ce qui n'est pas majeur
};

/**
 * Importance astrologique des types d'aspects
 * Plus le score est élevé, plus l'aspect est important
 */
const ASPECT_IMPORTANCE = {
  'conjunction': 5,   // Conjonction = le plus important
  'opposition': 4,    // Opposition = très important
  'square': 4,        // Carré = très important
  'trine': 3,         // Trigone = important
  'sextile': 2,       // Sextile = modérément important
  // Tout le reste (quintile, sesquiquadrate, etc.) = 1
};

/**
 * Retourne la catégorie d'un aspect selon l'astrologie classique
 * @param {string} aspectType - Type d'aspect (conjunction, opposition, etc.)
 * @returns {string} - 'major_tense', 'major_harmonious', ou 'minor'
 */
export function getAspectCategory(aspectType) {
  if (!aspectType) return 'minor';
  
  const normalized = aspectType.toLowerCase();
  
  if (ASPECT_CATEGORIES.major_tense.includes(normalized)) {
    return 'major_tense';
  }
  
  if (ASPECT_CATEGORIES.major_harmonious.includes(normalized)) {
    return 'major_harmonious';
  }
  
  return 'minor';
}

/**
 * Points du Big Three (Soleil, Lune, Ascendant, Milieu du Ciel)
 * Utilisés pour un bonus supplémentaire dans le calcul de score
 */
const BIG_THREE_POINTS = new Set(['Sun', 'Moon', 'Ascendant', 'Medium_Coeli']);

/**
 * Catégories de planètes pour le calcul d'importance
 */
const PERSONAL_PLANETS = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Ascendant', 'Medium_Coeli'];
const SOCIAL_PLANETS = ['Jupiter', 'Saturn'];
// Les autres (Uranus, Neptune, Pluto, Lilith, Nodes, etc.) sont considérées comme "lentes/points"

/**
 * Retourne la catégorie d'une planète
 * @param {string} planet - Nom de la planète
 * @returns {string} - 'personal', 'social', ou 'outer'
 */
function getPlanetCategory(planet) {
  if (PERSONAL_PLANETS.includes(planet)) {
    return 'personal';
  }
  if (SOCIAL_PLANETS.includes(planet)) {
    return 'social';
  }
  return 'outer';
}

/**
 * Vérifie si un aspect implique au moins une planète personnelle ou un angle
 * Les planètes personnelles incluent : Sun, Moon, Mercury, Venus, Mars, Ascendant, Medium_Coeli
 * @param {Object} aspect - Aspect avec from et to
 * @returns {boolean} - true si l'aspect implique au moins une planète personnelle/angle
 */
export function isPersonalRelated(aspect) {
  if (!aspect || !aspect.from || !aspect.to) {
    return false;
  }
  
  // Vérifier si au moins une des deux planètes est dans PERSONAL_PLANETS
  return PERSONAL_PLANETS.includes(aspect.from) || PERSONAL_PLANETS.includes(aspect.to);
}

/**
 * Calcule le bonus selon la combinaison de planètes
 * @param {string} planet1 - Première planète
 * @param {string} planet2 - Deuxième planète
 * @returns {number} - Bonus (0 à 3)
 */
function getPlanetCombinationBonus(planet1, planet2) {
  const cat1 = getPlanetCategory(planet1);
  const cat2 = getPlanetCategory(planet2);
  
  // perso ↔ perso → +3
  if (cat1 === 'personal' && cat2 === 'personal') {
    return 3;
  }
  
  // perso ↔ sociale → +2
  if ((cat1 === 'personal' && cat2 === 'social') || 
      (cat1 === 'social' && cat2 === 'personal')) {
    return 2;
  }
  
  // perso ↔ lente/point → +1
  if ((cat1 === 'personal' && cat2 === 'outer') || 
      (cat1 === 'outer' && cat2 === 'personal')) {
    return 1;
  }
  
  // Autres combinaisons → 0
  return 0;
}

/**
 * Calcule le bonus d'intensité
 * @param {string} strength - Intensité ('weak', 'medium', 'strong')
 * @returns {number} - Bonus (0 à 2)
 */
function getIntensityBonus(strength) {
  const bonuses = {
    'weak': 0,
    'medium': 1,
    'strong': 2,
  };
  return bonuses[strength] || 0;
}

/**
 * Calcule le bonus d'orbe (plus l'orbe est petit, plus le bonus est élevé)
 * @param {number} orb - Orbe en degrés
 * @returns {number} - Bonus (0 à 1)
 */
function getOrbBonus(orb) {
  // + (10 - min(10, orb)) / 10 pour favoriser les aspects serrés
  const orbAbs = Math.abs(orb);
  const cappedOrb = Math.min(10, orbAbs);
  return (10 - cappedOrb) / 10;
}

/**
 * Calcule le bonus Big Three si l'aspect implique au moins un point du Big Three
 * @param {string} planet1 - Première planète
 * @param {string} planet2 - Deuxième planète
 * @returns {number} - Bonus (0 ou 2)
 */
function getBigThreeBonus(planet1, planet2) {
  // Bonus si au moins un des deux corps est dans le Big Three
  if (BIG_THREE_POINTS.has(planet1) || BIG_THREE_POINTS.has(planet2)) {
    return 2;
  }
  return 0;
}

/**
 * Calcule le score global d'un aspect pour le tri
 * 
 * Formule :
 * score = importance_aspect + bonus_combinaison_planètes + bonus_intensité + bonus_orbe + bonus_big_three
 * 
 * Où :
 * - importance_aspect : 1 à 5 selon le type d'aspect (conjunction=5, opposition/square=4, etc.)
 * - bonus_combinaison : 0 à 3 selon les planètes (perso↔perso=3, perso↔sociale=2, perso↔lente=1)
 * - bonus_intensité : 0 à 2 (weak=0, medium=1, strong=2)
 * - bonus_orbe : 0 à 1 (plus petit = mieux, max quand orbe < 1°)
 * - bonus_big_three : 0 ou 2 si l'aspect implique Soleil/Lune/Ascendant/Medium_Coeli
 * 
 * Score total possible : 1 à 13 (au lieu de 1 à 11)
 * 
 * @param {Object} aspect - Aspect avec from, to, aspect_type, strength, orb
 * @returns {number} - Score global
 */
function calculateAspectScore(aspect) {
  const { from, to, aspect_type, strength, orb } = aspect;
  
  // Importance du type d'aspect (1 à 5)
  const aspectImportance = ASPECT_IMPORTANCE[aspect_type] || 1;
  
  // Bonus selon la combinaison de planètes (0 à 3)
  const planetBonus = getPlanetCombinationBonus(from, to);
  
  // Bonus d'intensité (0 à 2)
  const intensityBonus = getIntensityBonus(strength);
  
  // Bonus d'orbe (0 à 1)
  const orbBonus = getOrbBonus(orb);
  
  // Bonus Big Three (0 ou 2)
  const bigThreeBonus = getBigThreeBonus(from, to);
  
  // Score total
  const totalScore = aspectImportance + planetBonus + intensityBonus + orbBonus + bigThreeBonus;
  
  return totalScore;
}

/**
 * Poids de catégorie pour la hiérarchie astrologique
 * Utilisé pour garantir l'ordre : major_tense > major_harmonious > minor
 */
const CATEGORY_WEIGHT = {
  'major_tense': 1000,      // Passe devant tout
  'major_harmonious': 500,  // Passe devant minor
  'minor': 0,               // Base
};

/**
 * Trie les aspects selon la hiérarchie astrologique professionnelle STRICTE
 * 
 * LOGIQUE STRICTE (immutable) :
 * 1. PRIORITÉ ABSOLUE : Intensité (Fort=3 > Moyen=2 > Faible=1)
 * 2. PRIORITÉ 2 : Type d'aspect (ordre fixe : Conj=1 > Opp=2 > Carré=3 > Trigone=4 > Sextile=5 > Quintile=6 > autres=10)
 * 3. PRIORITÉ 3 : Score de base (UNIQUEMENT pour départager même intensité + même type)
 * 
 * Le tri utilise getFinalAspectSortKey() qui garantit :
 * - Un Sextile Fort ne peut JAMAIS dépasser une Conjonction Fort
 * - Un aspect mineur Fort ne peut JAMAIS dépasser un aspect majeur Fort
 * - Un aspect Moyen ne peut JAMAIS dépasser un aspect Fort de même type
 * 
 * @param {Array} aspects - Liste des aspects à trier
 * @returns {Array} - Aspects triés selon la hiérarchie astrologique stricte
 */
export function sortAspects(aspects) {
  if (!aspects || !Array.isArray(aspects)) {
    return [];
  }
  
  // Importer la fonction de tri depuis aspectCategories
  // Note: aspectCategories.ts est compilé en JS par TypeScript
  let getFinalAspectSortKey;
  try {
    const aspectCategories = require('./aspectCategories');
    getFinalAspectSortKey = aspectCategories.getFinalAspectSortKey;
  } catch (err) {
    // Fallback si l'import échoue (développement)
    console.warn('[sortAspects] Impossible d\'importer aspectCategories, utilisation du fallback simplifié');
    
    // Fallback avec logique stricte simplifiée (intensité > type > orbe)
    return [...aspects].sort((a, b) => {
      const strengthOrder = { strong: 3, medium: 2, weak: 1 };
      const strengthA = strengthOrder[a.strength?.toLowerCase()] || 1;
      const strengthB = strengthOrder[b.strength?.toLowerCase()] || 1;
      
      // PRIORITÉ 1 : Intensité
      if (strengthB !== strengthA) {
        return strengthB - strengthA;
      }
      
      // PRIORITÉ 2 : Type d'aspect (ordre fixe)
      const typeOrder = {
        'conjunction': 1,
        'opposition': 2,
        'square': 3,
        'trine': 4,
        'sextile': 5,
      };
      const typeA = a.aspect_type?.toLowerCase() || '';
      const typeB = b.aspect_type?.toLowerCase() || '';
      const rankA = typeOrder[typeA] || 10;
      const rankB = typeOrder[typeB] || 10;
      
      if (rankB !== rankA) {
        return rankA - rankB; // Plus petit = mieux
      }
      
      // PRIORITÉ 3 : Orbe (plus petit = mieux)
      return Math.abs(a.orb || 0) - Math.abs(b.orb || 0);
    });
  }
  
  // Créer une copie pour éviter de modifier l'original
  const sortedAspects = [...aspects];
  
  // Trier avec la clé de tri stricte (intensité × 1_000_000 + type × 10_000 + score)
  // Le tri est décroissant : plus grand = plus prioritaire
  sortedAspects.sort((a, b) => {
    const keyA = getFinalAspectSortKey(a);
    const keyB = getFinalAspectSortKey(b);
    
    // Tri décroissant (plus grand = plus prioritaire)
    return keyB - keyA;
  });
  
  return sortedAspects;
}

/**
 * Helper pour obtenir les aspects visibles triés
 * Applique le tri APRÈS le filtrage pour garantir un ordre cohérent
 * 
 * @param {Array} aspects - Liste complète des aspects
 * @param {boolean} hideWeak - Si true, exclut les aspects "weak"
 * @returns {Array} - Aspects filtrés et triés selon la hiérarchie stricte
 */
export function getSortedVisibleAspects(aspects, hideWeak = false) {
  if (!aspects || !Array.isArray(aspects)) {
    return [];
  }
  
  // Étape 1 : Filtrer selon hideWeak
  const filtered = hideWeak
    ? aspects.filter(a => a.strength?.toLowerCase() !== 'weak')
    : aspects;
  
  // Étape 2 : Appliquer le tri strict APRÈS le filtrage
  return sortAspects(filtered);
}

/**
 * Filtre les aspects selon leur pertinence (déprécié, utiliser sortAspects + filter)
 * @deprecated Utiliser sortAspects() à la place
 * @param {Array} aspects - Liste des aspects
 * @param {string} minStrength - Force minimale ('strong', 'medium', 'weak')
 * @returns {Array} - Aspects filtrés
 */
export function filterAspectsByRelevance(aspects, minStrength = 'medium') {
  const strengthOrder = { strong: 3, medium: 2, weak: 1 };
  const minLevel = strengthOrder[minStrength] || 2;
  
  return aspects
    .filter(asp => strengthOrder[asp.strength] >= minLevel)
    .sort((a, b) => {
      // Tri par force puis par orbe
      const strengthDiff = strengthOrder[b.strength] - strengthOrder[a.strength];
      if (strengthDiff !== 0) return strengthDiff;
      return Math.abs(a.orb) - Math.abs(b.orb);
    });
}

/**
 * Génère un résumé général basé sur le Big Three
 * @param {Object} bigThree - {sun, moon, ascendant}
 * @returns {string} - Résumé de personnalité
 */
export function generateBigThreeSummary(bigThree) {
  if (!bigThree || !bigThree.sun || !bigThree.moon || !bigThree.ascendant) {
    return '';
  }
  
  const { sun, moon, ascendant } = bigThree;
  
  const summary = `Votre Soleil en ${sun.sign_fr} ${sun.element ? `(${sun.element})` : ''} donne une personnalité ${getSignTrait(sun.sign_fr)}. Votre Lune en ${moon.sign_fr} révèle un monde émotionnel ${getSignTrait(moon.sign_fr)}. L'Ascendant en ${ascendant.sign_fr} colore votre manière d'être perçu(e) et d'aborder la vie.`;
  
  return summary;
}

/**
 * Retourne un trait de personnalité basé sur le signe
 * @param {string} signFr - Nom du signe en français
 * @returns {string} - Trait de personnalité
 */
function getSignTrait(signFr) {
  const traits = {
    'Bélier': 'dynamique et entreprenante',
    'Taureau': 'stable et sensuelle',
    'Gémeaux': 'curieuse et communicative',
    'Cancer': 'sensible et protectrice',
    'Lion': 'rayonnante et créative',
    'Vierge': 'analytique et précise',
    'Balance': 'harmonieuse et diplomate',
    'Scorpion': 'intense et transformatrice',
    'Sagittaire': 'aventureuse et philosophe',
    'Capricorne': 'ambitieuse et structurée',
    'Verseau': 'originale et visionnaire',
    'Poissons': 'intuitive et empathique',
  };
  
  return traits[signFr] || 'unique';
}

/**
 * Retourne un emoji pour un type d'aspect
 * @param {string} aspectType - Type d'aspect
 * @returns {string} - Emoji
 */
export function getAspectEmoji(aspectType) {
  const emojis = {
    'conjunction': '🔵',
    'opposition': '⚪',
    'trine': '🔺',
    'square': '🟦',
    'sextile': '⬡',
    'quintile': '⭐',
    'biquintile': '✨',
    'semisextile': '◇',
    'semisquare': '▫️',
    'sesquisquare': '▪️',
    'quincunx': '⚡',
  };
  return emojis[aspectType] || '◆';
}

/**
 * Retourne une couleur pour l'intensité
 * @param {string} strength - Force de l'aspect
 * @returns {string} - Code couleur hex
 */
export function getStrengthColor(strength) {
  const colors = {
    'strong': '#2ECC71',  // Vert
    'medium': '#FF9F1C',  // Orange
    'weak': '#8E8E98',    // Gris
  };
  return colors[strength] || '#8E8E98';
}

