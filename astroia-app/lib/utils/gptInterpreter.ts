/**
 * Interprétation GPT optionnelle des aspects astrologiques
 * Mode activable via USE_GPT_INTERP
 */

// Flag global pour activer/désactiver GPT
let USE_GPT_INTERP = false;

/**
 * Active ou désactive le mode GPT
 */
export function setUseGPTInterp(value: boolean): void {
  USE_GPT_INTERP = value;
}

/**
 * Obtient le statut du mode GPT
 */
export function getUseGPTInterp(): boolean {
  return USE_GPT_INTERP;
}

/**
 * Vérifie si le mode GPT est activé
 */
export function isGptInterpEnabled(): boolean {
  return USE_GPT_INTERP;
}

/**
 * Fonction générique de rewriting avec GPT
 * Réécrit un texte en français simple, fluide et naturel
 * 
 * @param text - Texte à réécrire
 * @param context - Contexte : "aspect" ou "profile"
 * @returns Promise<string> - Texte réécrit ou texte original en cas d'erreur
 */
export async function rewriteWithGPT(
  text: string,
  context: 'aspect' | 'profile'
): Promise<string> {
  if (!USE_GPT_INTERP) {
    return text;
  }

  // TODO: Intégrer l'API OpenAI / GPT 3.5
  // Pour l'instant, on retourne le texte original
  // 
  // Exemple d'implémentation à faire quand l'API sera disponible :
  /*
  const systemPrompt = context === 'profile'
    ? "Tu es astrologue professionnel. Tu réécris ce texte d'interprétation astrologique en français naturel, fluide et clair. Ton bienveillant et accessible. Évite le jargon ésotérique. Ne change pas le sens, ne rajoute pas d'informations. Garde un style moderne et 3 à 5 phrases maximum. Utilise le tutoiement (tu/ton/tes)."
    : "Tu es astrologue professionnel. Tu réécris cette interprétation d'aspect astrologique en français naturel et fluide. Ton bienveillant et simple. Ne change pas le sens. Garde 2 à 3 phrases maximum. Utilise le tutoiement (tu/ton/tes).";

  try {
    // Utiliser l'API OpenAI (à adapter selon le client existant dans le projet)
    const response = await callOpenAI({
      model: 'gpt-3.5-turbo',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: `Réécris cette interprétation astrologique en français naturel et fluide :\n\n${text}` }
      ],
      max_tokens: context === 'profile' ? 250 : 150,
      temperature: 0.7,
    });
    
    const rewritten = response.choices[0].message.content?.trim() || text;
    
    // Vérifier que le texte n'est pas trop long ou verbeux
    if (rewritten.length > text.length * 1.5) {
      console.warn('[GPT Interpreter] Texte GPT trop long, utilisation du texte original');
      return text;
    }
    
    return rewritten;
  } catch (error) {
    console.warn('[GPT Interpreter] Erreur rewriting:', error);
    return text; // Fallback sur le texte original
  }
  */
  
  // Pour l'instant, retourner le texte original
  return text;
}

/**
 * Génère une interprétation GPT pour un aspect
 * @param aspect - Aspect complet avec toutes les infos nécessaires
 * @returns Promise<string> - Interprétation générée par GPT
 */
export async function getGPTInterpretation(aspect: {
  from: string;
  to: string;
  aspect_type: string;
  strength: string;
  orb?: number;
  signA?: string;
  signB?: string;
  houseA?: number;
  houseB?: number;
}): Promise<string> {
  const { from, to, aspect_type, strength, orb, signA, signB, houseA, houseB } = aspect;
  
  // TODO: Implémenter l'appel à l'API GPT
  // Pour l'instant, on retourne une version enrichie basée sur les templates
  
  // Version enrichie avec les signes si disponibles
  let interpretation = `${from} en ${signA || '?'} aspect ${aspect_type} ${to} en ${signB || '?'}`;
  interpretation += ` (intensité ${strength}, orbe ${orb?.toFixed(2) || '?'}°). `;
  interpretation += `Cet aspect influence particulièrement les domaines des maisons ${houseA || '?'} et ${houseB || '?'}.`;
  
  // TODO: Remplacer par un vrai appel GPT quand l'API sera configurée
  return Promise.resolve(interpretation);
}

