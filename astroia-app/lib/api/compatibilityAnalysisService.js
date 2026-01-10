/**
 * Service d'Analyse de Compatibilité Universelle
 * Calcule la compatibilité entre deux personnes (couple, amis, collègues)
 */

import { supabase } from '../supabase';

const ELEMENTS = {
  1: 'fire', 5: 'fire', 9: 'fire',       // Bélier, Lion, Sagittaire
  2: 'earth', 6: 'earth', 10: 'earth',   // Taureau, Vierge, Capricorne
  3: 'air', 7: 'air', 11: 'air',         // Gémeaux, Balance, Verseau
  4: 'water', 8: 'water', 12: 'water',   // Cancer, Scorpion, Poissons
};

const ZODIAC_NAMES = {
  1: 'Bélier', 2: 'Taureau', 3: 'Gémeaux', 4: 'Cancer',
  5: 'Lion', 6: 'Vierge', 7: 'Balance', 8: 'Scorpion',
  9: 'Sagittaire', 10: 'Capricorne', 11: 'Verseau', 12: 'Poissons',
};

/**
 * Analyse la compatibilité entre deux personnes
 */
export async function analyzeCompatibility(person1, person2, relationType = 'couple') {
  try {
    // Calculs détaillés
    const elementCompatibility = calculateElementCompatibility(person1, person2);
    const aspectScore = calculateAspectScore(person1.sunSign, person2.sunSign);
    const moonSynastry = calculateMoonSynastry(person1.moonSign, person2.moonSign);
    const ascendantHarmony = calculateAscendantHarmony(person1.ascendant, person2.ascendant);

    // Scores détaillés selon le type de relation
    const detailedScores = calculateDetailedScores(
      person1,
      person2,
      relationType,
      elementCompatibility,
      aspectScore,
      moonSynastry,
      ascendantHarmony
    );

    // Score global
    const globalScore = Math.round(
      (detailedScores.communication +
        detailedScores.passion +
        detailedScores.complicity +
        detailedScores.goals) / 4
    );

    // Interprétation
    const interpretation = getInterpretation(globalScore, relationType);

    // Points forts et attention
    const strengths = getStrengths(detailedScores, person1, person2);
    const warnings = getWarnings(detailedScores, person1, person2);

    // Conseils
    const advice = getAdvice(globalScore, relationType, detailedScores);

    return {
      success: true,
      relationType,
      globalScore,
      detailedScores,
      interpretation,
      strengths,
      warnings,
      advice,
      person1: {
        name: person1.name || 'Personne 1',
        sun: ZODIAC_NAMES[person1.sunSign],
        moon: ZODIAC_NAMES[person1.moonSign],
        ascendant: ZODIAC_NAMES[person1.ascendant],
      },
      person2: {
        name: person2.name || 'Personne 2',
        sun: ZODIAC_NAMES[person2.sunSign],
        moon: ZODIAC_NAMES[person2.moonSign],
        ascendant: ZODIAC_NAMES[person2.ascendant],
      },
    };
  } catch (error) {
    console.error('[compatibilityAnalysisService] Error:', error);
    throw error;
  }
}

/**
 * Calcule la compatibilité élémentaire (0-100)
 */
function calculateElementCompatibility(person1, person2) {
  const elem1 = ELEMENTS[person1.sunSign];
  const elem2 = ELEMENTS[person2.sunSign];

  // Même élément = 90%
  if (elem1 === elem2) return 90;

  // Éléments compatibles (Feu+Air, Terre+Eau) = 75%
  if (
    (elem1 === 'fire' && elem2 === 'air') ||
    (elem1 === 'air' && elem2 === 'fire') ||
    (elem1 === 'earth' && elem2 === 'water') ||
    (elem1 === 'water' && elem2 === 'earth')
  ) {
    return 75;
  }

  // Éléments neutres = 55%
  if (
    (elem1 === 'fire' && elem2 === 'earth') ||
    (elem1 === 'earth' && elem2 === 'fire') ||
    (elem1 === 'air' && elem2 === 'water') ||
    (elem1 === 'water' && elem2 === 'air')
  ) {
    return 55;
  }

  // Éléments opposés (Feu+Eau, Terre+Air) = 40%
  return 40;
}

/**
 * Calcule le score des aspects planétaires
 */
function calculateAspectScore(sun1, sun2) {
  const diff = Math.abs(sun1 - sun2);

  // Conjonction (même signe) = 85%
  if (diff === 0) return 85;

  // Trigone (4 signes d'écart) = 90%
  if (diff === 4 || diff === 8) return 90;

  // Sextile (2 signes) = 80%
  if (diff === 2 || diff === 10) return 80;

  // Opposition (6 signes) = 50%
  if (diff === 6) return 50;

  // Carré (3 signes) = 45%
  if (diff === 3 || diff === 9) return 45;

  // Autre = 60%
  return 60;
}

/**
 * Calcule la synastrie lunaire (émotions)
 */
function calculateMoonSynastry(moon1, moon2) {
  const moonDiff = Math.abs(moon1 - moon2);

  // Lunes compatibles
  if (moonDiff === 0) return 95; // Même lune
  if (moonDiff === 4 || moonDiff === 8) return 88; // Trigone
  if (moonDiff === 2 || moonDiff === 10) return 82; // Sextile
  if (moonDiff === 6) return 45; // Opposition
  if (moonDiff === 3 || moonDiff === 9) return 40; // Carré

  return 65;
}

/**
 * Calcule l'harmonie des ascendants
 */
function calculateAscendantHarmony(asc1, asc2) {
  const ascDiff = Math.abs(asc1 - asc2);

  if (ascDiff === 0) return 90;
  if (ascDiff === 4 || ascDiff === 8) return 85;
  if (ascDiff === 2 || ascDiff === 10) return 80;
  if (ascDiff === 6) return 50;
  if (ascDiff === 3 || ascDiff === 9) return 48;

  return 68;
}

/**
 * Calcule les scores détaillés selon le type de relation
 */
function calculateDetailedScores(
  person1,
  person2,
  relationType,
  elementCompat,
  aspectScore,
  moonSynastry,
  ascendantHarmony
) {
  const elem1 = ELEMENTS[person1.sunSign];
  const elem2 = ELEMENTS[person2.sunSign];

  let scores = {
    communication: 0,
    passion: 0,
    complicity: 0,
    goals: 0,
  };

  if (relationType === 'couple') {
    // Couple : Focus sur passion et émotions
    scores.communication = Math.round((aspectScore + ascendantHarmony) / 2);
    scores.passion = Math.round((elementCompat + aspectScore) / 2);
    scores.complicity = Math.round((moonSynastry + elementCompat) / 2);
    scores.goals = Math.round((ascendantHarmony + aspectScore) / 2);
  } else if (relationType === 'friends') {
    // Amis : Focus sur complicité et communication
    scores.communication = Math.round((aspectScore + moonSynastry) / 2);
    scores.passion = Math.round((elementCompat * 0.6 + aspectScore * 0.4));
    scores.complicity = Math.round((moonSynastry + ascendantHarmony) / 2);
    scores.goals = Math.round((elementCompat + ascendantHarmony) / 2);
  } else {
    // Collègues : Focus sur objectifs et communication
    scores.communication = Math.round((aspectScore + ascendantHarmony + moonSynastry) / 3);
    scores.passion = Math.round(elementCompat * 0.7);
    scores.complicity = Math.round((moonSynastry * 0.6 + elementCompat * 0.4));
    scores.goals = Math.round((ascendantHarmony + aspectScore) / 2);
  }

  return scores;
}

/**
 * Interprète le score global
 */
function getInterpretation(score, relationType) {
  const relationLabels = {
    couple: { high: 'Relation passionnée', mid: 'Relation harmonieuse', low: 'Relation à construire' },
    friends: { high: 'Amitié exceptionnelle', mid: 'Belle amitié', low: 'Amitié à cultiver' },
    colleagues: { high: 'Collaboration idéale', mid: 'Bonne synergie', low: 'Ajustements nécessaires' },
  };

  const labels = relationLabels[relationType] || relationLabels.couple;

  if (score >= 80) {
    return {
      level: 'Excellente',
      emoji: '💚',
      title: labels.high,
      description: `Avec ${score}%, votre connexion astrologique est remarquable. Les énergies s'harmonisent naturellement.`,
    };
  } else if (score >= 65) {
    return {
      level: 'Bonne',
      emoji: '💙',
      title: labels.mid,
      description: `Score de ${score}%. Belle compatibilité avec quelques ajustements à faire pour maximiser l'harmonie.`,
    };
  } else if (score >= 50) {
    return {
      level: 'Moyenne',
      emoji: '💛',
      title: labels.low,
      description: `Compatibilité de ${score}%. Des efforts conscients peuvent transformer cette relation en succès.`,
    };
  } else {
    return {
      level: 'Délicate',
      emoji: '🧡',
      title: 'Relation challengeante',
      description: `Score de ${score}%. Les énergies contrastent, mais avec compréhension et communication, tout est possible.`,
    };
  }
}

/**
 * Identifie les points forts
 */
function getStrengths(scores, person1, person2) {
  const strengths = [];

  if (scores.communication >= 80) {
    strengths.push({
      icon: '💬',
      text: 'Excellent dialogue et compréhension mutuelle',
    });
  }

  if (scores.passion >= 80) {
    strengths.push({
      icon: '🔥',
      text: 'Énergie partagée et dynamisme commun',
    });
  }

  if (scores.complicity >= 80) {
    strengths.push({
      icon: '🤝',
      text: 'Complicité naturelle et empathie profonde',
    });
  }

  if (scores.goals >= 80) {
    strengths.push({
      icon: '🎯',
      text: 'Vision commune et objectifs alignés',
    });
  }

  // Compatibilité élémentaire
  const elem1 = ELEMENTS[person1.sunSign];
  const elem2 = ELEMENTS[person2.sunSign];
  if (elem1 === elem2) {
    strengths.push({
      icon: '✨',
      text: `Même élément (${elem1 === 'fire' ? 'Feu' : elem1 === 'earth' ? 'Terre' : elem1 === 'air' ? 'Air' : 'Eau'}) : connexion instinctive`,
    });
  }

  return strengths.slice(0, 4); // Max 4 points forts
}

/**
 * Identifie les points d'attention
 */
function getWarnings(scores, person1, person2) {
  const warnings = [];

  if (scores.communication < 60) {
    warnings.push({
      icon: '⚠️',
      text: 'Travaillez la communication et l\'écoute active',
    });
  }

  if (scores.passion < 60) {
    warnings.push({
      icon: '💡',
      text: 'Cultivez des activités partagées pour renforcer le lien',
    });
  }

  if (scores.complicity < 60) {
    warnings.push({
      icon: '🌊',
      text: 'Accordez du temps pour vous connaître en profondeur',
    });
  }

  if (scores.goals < 60) {
    warnings.push({
      icon: '🔧',
      text: 'Clarifiez vos attentes et objectifs communs',
    });
  }

  return warnings.slice(0, 3); // Max 3 points d'attention
}

/**
 * Génère des conseils personnalisés
 */
function getAdvice(score, relationType, scores) {
  const advice = [];

  if (relationType === 'couple') {
    if (score >= 80) {
      advice.push('Célébrez votre connexion naturelle et continuez à nourrir votre intimité.');
    } else if (scores.passion < scores.communication) {
      advice.push('Ravivez la flamme avec des surprises et des moments de qualité ensemble.');
    } else {
      advice.push('Renforcez votre complicité par des discussions sincères et régulières.');
    }
  } else if (relationType === 'friends') {
    if (score >= 80) {
      advice.push('Votre amitié est précieuse, entretenez-la avec des moments partagés.');
    } else {
      advice.push('Créez des rituels communs pour renforcer vos liens amicaux.');
    }
  } else {
    if (score >= 80) {
      advice.push('Votre synergie professionnelle est excellente, capitalisez dessus.');
    } else {
      advice.push('Définissez des objectifs clairs et communiquez régulièrement.');
    }
  }

  advice.push('L\'astrologie révèle les potentiels, mais c\'est l\'intention qui crée la relation.');

  return advice;
}

/**
 * Sauvegarde l'analyse dans Supabase
 */
export async function saveCompatibilityAnalysis(analysisData) {
  try {
    const { data: { user } } = await supabase.auth.getUser();

    if (!user) {
      console.log('[compatibilityAnalysisService] User not authenticated');
      return null;
    }

    const { person1, person2, relationType, result } = analysisData;

    const { data, error } = await supabase
      .from('compatibility_analyses')
      .insert({
        user_id: user.id,
        relation_type: relationType,
        person1_name: person1.name || null,
        person1_sun: person1.sunSign,
        person1_moon: person1.moonSign,
        person1_ascendant: person1.ascendant,
        person2_name: person2.name || null,
        person2_sun: person2.sunSign,
        person2_moon: person2.moonSign,
        person2_ascendant: person2.ascendant,
        global_score: result.globalScore,
        communication_score: result.detailedScores.communication,
        passion_score: result.detailedScores.passion,
        complicity_score: result.detailedScores.complicity,
        goals_score: result.detailedScores.goals,
      })
      .select()
      .single();

    if (error) {
      console.error('[compatibilityAnalysisService] Save error:', error);
      return null;
    }

    return data;
  } catch (error) {
    console.error('[compatibilityAnalysisService] Error:', error);
    return null;
  }
}

/**
 * Récupère l'historique des analyses
 */
export async function getAnalysisHistory(limit = 10) {
  try {
    const { data: { user } } = await supabase.auth.getUser();

    if (!user) return [];

    const { data, error } = await supabase
      .from('compatibility_analyses')
      .select('*')
      .eq('user_id', user.id)
      .order('created_at', { ascending: false })
      .limit(limit);

    if (error) {
      console.error('[compatibilityAnalysisService] Fetch error:', error);
      return [];
    }

    return data || [];
  } catch (error) {
    console.error('[compatibilityAnalysisService] Error:', error);
    return [];
  }
}

export default {
  analyzeCompatibility,
  saveCompatibilityAnalysis,
  getAnalysisHistory,
};

