/**
 * Templates d'interprétation des aspects astrologiques
 * Version locale, sans appel API
 */

import { translatePlanet } from './astrologyTranslations';
import { rewriteWithGPT, getUseGPTInterp } from './gptInterpreter';

/**
 * Mots-clés pour chaque planète (pour les templates)
 */
const PLANET_KEYWORDS: Record<string, { name: string; role: string }> = {
  'Sun': { name: 'Soleil', role: 'identité et volonté' },
  'Moon': { name: 'Lune', role: 'émotions et besoins' },
  'Mercury': { name: 'Mercure', role: 'communication et pensée' },
  'Venus': { name: 'Vénus', role: 'affects et valeurs' },
  'Mars': { name: 'Mars', role: 'action et désir' },
  'Jupiter': { name: 'Jupiter', role: 'expansion et chance' },
  'Saturn': { name: 'Saturne', role: 'structure et responsabilités' },
  'Uranus': { name: 'Uranus', role: 'liberté et changement' },
  'Neptune': { name: 'Neptune', role: 'intuition et rêves' },
  'Pluto': { name: 'Pluton', role: 'transformation et puissance' },
  'Ascendant': { name: 'Ascendant', role: 'image et manière d\'aborder le monde' },
  'Medium_Coeli': { name: 'Milieu du Ciel', role: 'vocation et destinée sociale' },
  'Mean_Node': { name: 'Nœud Nord', role: 'axe d\'évolution' },
  'Mean_South_Node': { name: 'Nœud Sud', role: 'habitudes passées' },
  'Mean_Lilith': { name: 'Lilith', role: 'désirs bruts' },
  'Chiron': { name: 'Chiron', role: 'blessure et guérison' },
};

/**
 * Templates par type d'aspect
 * Textes en français naturel, fluide et moderne, sans répétitions
 */
export const ASPECT_TEMPLATES = {
  conjunction: (planetA: string, planetB: string, intensity: string) => {
    const nameA = translatePlanet(planetA);
    const nameB = translatePlanet(planetB);
    
    if (intensity === 'strong') {
      return `${nameA} et ${nameB} fusionnent puissamment : cette combinaison intensifie tes réactions et colore profondément ta personnalité.`;
    } else if (intensity === 'medium') {
      return `${nameA} et ${nameB} s'unissent : leurs influences se renforcent mutuellement dans ton thème.`;
    }
    return `${nameA} et ${nameB} se rencontrent : une connexion subtile qui module tes traits de caractère.`;
  },
  
  opposition: (planetA: string, planetB: string, intensity: string) => {
    const nameA = translatePlanet(planetA);
    const nameB = translatePlanet(planetB);
    
    if (intensity === 'strong') {
      return `${nameA} s'oppose à ${nameB} : tu navigues entre deux pôles complémentaires, cherchant un équilibre dynamique dans ta vie.`;
    } else if (intensity === 'medium') {
      return `${nameA} et ${nameB} créent une tension constructive : cette polarité t'invite à intégrer leurs forces opposées.`;
    }
    return `${nameA} et ${nameB} se font face : une tension légère qui demande un ajustement.`;
  },
  
  square: (planetA: string, planetB: string, intensity: string) => {
    const nameA = translatePlanet(planetA);
    const nameB = translatePlanet(planetB);
    
    if (intensity === 'strong') {
      return `${nameA} forme un carré avec ${nameB} : cette friction active te pousse à dépasser tes limites et à trouver des solutions créatives.`;
    } else if (intensity === 'medium') {
      return `${nameA} et ${nameB} créent une friction modérée : cette tension stimule ta capacité à résoudre les conflits intérieurs.`;
    }
    return `${nameA} et ${nameB} génèrent une légère friction : une source discrète de défi dans ton thème.`;
  },
  
  trine: (planetA: string, planetB: string, intensity: string) => {
    const nameA = translatePlanet(planetA);
    const nameB = translatePlanet(planetB);
    
    if (intensity === 'strong') {
      return `${nameA} et ${nameB} s'harmonisent parfaitement : cette alliance facilite ton expression naturelle et renforce tes talents.`;
    } else if (intensity === 'medium') {
      return `${nameA} et ${nameB} créent une belle synergie : leur coopération apporte fluidité et aisance dans tes démarches.`;
    }
    return `${nameA} et ${nameB} s'harmonisent : une connexion douce qui facilite ton expression.`;
  },
  
  sextile: (planetA: string, planetB: string, intensity: string) => {
    const nameA = translatePlanet(planetA);
    const nameB = translatePlanet(planetB);
    
    if (intensity === 'strong') {
      return `${nameA} et ${nameB} s'entraident activement : cette alliance ouvre des opportunités concrètes et favorise tes projets.`;
    } else if (intensity === 'medium') {
      return `${nameA} et ${nameB} coopèrent harmonieusement : cette connexion positive soutient tes initiatives avec bienveillance.`;
    }
    return `${nameA} et ${nameB} créent une opportunité discrète : une ouverture subtile pour tes actions.`;
  },
  
  minor: (planetA: string, planetB: string, aspectType: string, intensity: string) => {
    const nameA = translatePlanet(planetA);
    const nameB = translatePlanet(planetB);
    
    if (intensity === 'strong') {
      return `${nameA} et ${nameB} forment un aspect mineur (${aspectType}) : cette connexion subtile mais réelle influence ton caractère en profondeur.`;
    } else if (intensity === 'medium') {
      return `${nameA} et ${nameB} créent un lien discret (${aspectType}) : une influence douce qui nuance ton thème.`;
    }
    return `${nameA} et ${nameB} forment un aspect mineur (${aspectType}) : une influence légère en arrière-plan.`;
  },
};

/**
 * Génère une interprétation lisible pour un aspect (version synchrone par défaut)
 * Version rapide sans appel async, utilisée par défaut dans l'UI
 * 
 * @param aspect - Aspect avec from, to, aspect_type, strength, orb
 * @param options - Options (useGPT pour mode GPT optionnel - nécessite version async)
 * @returns Phrase d'interprétation en français
 */
export function getReadableInterpretation(
  aspect: {
    from: string;
    to: string;
    aspect_type: string;
    strength: string;
    orb?: number;
  },
  options: { useGPT?: boolean } = {}
): string {
  const { from, to, aspect_type, strength } = aspect;
  
  const normalizedType = aspect_type?.toLowerCase() || '';
  const normalizedStrength = strength?.toLowerCase() || 'medium';
  
  // Générer le texte de base avec le template approprié
  let baseText = '';
  
  if (normalizedType === 'conjunction') {
    baseText = ASPECT_TEMPLATES.conjunction(from, to, normalizedStrength);
  } else if (normalizedType === 'opposition') {
    baseText = ASPECT_TEMPLATES.opposition(from, to, normalizedStrength);
  } else if (normalizedType === 'square') {
    baseText = ASPECT_TEMPLATES.square(from, to, normalizedStrength);
  } else if (normalizedType === 'trine') {
    baseText = ASPECT_TEMPLATES.trine(from, to, normalizedStrength);
  } else if (normalizedType === 'sextile') {
    baseText = ASPECT_TEMPLATES.sextile(from, to, normalizedStrength);
  } else {
    // Aspect mineur
    const aspectTypeName = aspect_type || 'aspect mineur';
    baseText = ASPECT_TEMPLATES.minor(from, to, aspectTypeName, normalizedStrength);
  }
  
  // Version synchrone : retourne directement le template
  // Pour utiliser GPT, utiliser getReadableInterpretationAsync() dans l'UI
  return baseText;
}

/**
 * Alias synchrone pour compatibilité
 * @deprecated Utiliser getReadableInterpretation() à la place
 */
export function getReadableInterpretationSync(
  aspect: {
    from: string;
    to: string;
    aspect_type: string;
    strength: string;
    orb?: number;
  },
  options: { useGPT?: boolean } = {}
): string {
  return getReadableInterpretation(aspect, options);
}

/**
 * Génère une interprétation lisible pour un aspect avec GPT optionnel (version async)
 * @param aspect - Aspect avec from, to, aspect_type, strength, orb
 * @param options - Options (useGPT pour mode GPT optionnel)
 * @returns Promise<string> - Phrase d'interprétation en français
 */
export async function getReadableInterpretationAsync(
  aspect: {
    from: string;
    to: string;
    aspect_type: string;
    strength: string;
    orb?: number;
  },
  options: { useGPT?: boolean } = {}
): Promise<string> {
  const baseText = getReadableInterpretation(aspect, options);
  
  // Réécrire avec GPT si activé
  if ((options.useGPT || getUseGPTInterp()) && baseText) {
    try {
      const rewritten = await rewriteWithGPT(baseText, 'aspect');
      return rewritten || baseText; // Fallback sur le template si GPT échoue
    } catch (error) {
      console.warn('[AspectTextTemplates] Erreur GPT rewriting:', error);
      return baseText; // Fallback sur le template en cas d'erreur
    }
  }
  
  return baseText;
}

