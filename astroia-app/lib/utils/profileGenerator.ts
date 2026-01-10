/**
 * Génération du profil astrologique
 * Version template locale et version GPT optionnelle
 */

import { getUseGPTInterp, rewriteWithGPT } from './gptInterpreter';

/**
 * Dictionnaire des noms de planètes en français
 */
const planetNamesFR: Record<string, string> = {
  Sun: 'Soleil',
  Moon: 'Lune',
  Mercury: 'Mercure',
  Venus: 'Vénus',
  Mars: 'Mars',
  Jupiter: 'Jupiter',
  Saturn: 'Saturne',
  Uranus: 'Uranus',
  Neptune: 'Neptune',
  Pluto: 'Pluton',
  Ascendant: 'Ascendant',
  Midheaven: 'Milieu du Ciel',
  Medium_Coeli: 'Milieu du Ciel',
};

/**
 * Traits de personnalité par signe (pour templates)
 */
const SIGN_TRAITS: Record<string, string> = {
  'Bélier': 'dynamique, entreprenant, impulsif',
  'Taureau': 'stable, sensuel, déterminé',
  'Gémeaux': 'curieux, communicatif, adaptable',
  'Cancer': 'sensible, protecteur, intuitif',
  'Lion': 'rayonnant, créatif, généreux',
  'Vierge': 'analytique, précis, perfectionniste',
  'Balance': 'harmonieux, diplomate, esthète',
  'Scorpion': 'intense, transformateur, passionné',
  'Sagittaire': 'aventureux, philosophe, optimiste',
  'Capricorne': 'ambitieux, structuré, persévérant',
  'Verseau': 'original, visionnaire, indépendant',
  'Poissons': 'intuitif, empathique, rêveur',
};

/**
 * Génère un profil astrologique avec templates
 */
function generateTemplateProfile(bigThree: {
  sun?: { sign_fr: string; element?: string; degree?: number };
  moon?: { sign_fr: string; element?: string; degree?: number };
  ascendant?: { sign_fr: string; element?: string; degree?: number };
}): string {
  if (!bigThree || !bigThree.sun || !bigThree.moon || !bigThree.ascendant) {
    return '';
  }
  
  const { sun, moon, ascendant } = bigThree;
  const sunSign = sun.sign_fr || '';
  const moonSign = moon.sign_fr || '';
  const ascSign = ascendant.sign_fr || '';
  
  const sunTraits = SIGN_TRAITS[sunSign] || 'unique';
  const moonTraits = SIGN_TRAITS[moonSign] || 'sensible';
  const ascTraits = SIGN_TRAITS[ascSign] || 'distinct';
  
  // Construction du texte avec français propre, naturel et fluide
  const profile = `Ton Soleil en ${sunSign} révèle une personnalité ${sunTraits}. Ta Lune en ${moonSign} colore ton monde émotionnel d'un esprit ${moonTraits}. Ton Ascendant en ${ascSign} façonne ta manière d'être perçu(e) : ${ascTraits}. Ces trois piliers forment l'essence de ton thème natal et guident tes choix de vie.`;
  
  return profile;
}

/**
 * Génère un profil astrologique complet
 * @param natalData - Données du thème natal
 * @returns Promise<string> - Profil généré (template ou GPT)
 */
export async function generateProfile(natalData: {
  big_three?: {
    sun?: { sign_fr: string; element?: string; degree?: number };
    moon?: { sign_fr: string; element?: string; degree?: number };
    ascendant?: { sign_fr: string; element?: string; degree?: number };
  };
  dominant_element?: string;
  positions?: Array<{
    name: string;
    sign_fr: string;
    house: number;
    element: string;
  }>;
}): Promise<string> {
  const { big_three, dominant_element, positions } = natalData;
  
  // Générer le profil de base avec templates
  let profile = generateTemplateProfile(big_three || {});
  
  // Enrichir avec élément dominant si disponible
  if (dominant_element && profile) {
    profile += ` L'élément ${dominant_element} domine ton thème, imprégnant tes choix et ta façon d'être.`;
  }
  
  // Ajouter une note sur les positions planétaires si disponibles
  if (positions && positions.length > 0) {
    const personalPlanets = positions.filter(p => 
      ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars'].includes(p.name)
    );
    
    if (personalPlanets.length > 0) {
      const planetsSummary = personalPlanets
        .slice(0, 3)
        .map(p => {
          const planetNameFR = planetNamesFR[p.name] || p.name;
          return `${planetNameFR} en ${p.sign_fr}`;
        })
        .join(', ');
      
      profile += ` Tes planètes personnelles (${planetsSummary}) révèlent des facettes complémentaires de ta personnalité.`;
    }
  }
  
  // Réécrire avec GPT si activé
  if (getUseGPTInterp()) {
    try {
      const rewritten = await rewriteWithGPT(profile, 'profile');
      return rewritten || profile; // Fallback sur le template si GPT échoue
    } catch (error) {
      console.warn('[ProfileGenerator] Erreur GPT rewriting:', error);
      return profile; // Fallback sur le template en cas d'erreur
    }
  }
  
  return profile;
}

