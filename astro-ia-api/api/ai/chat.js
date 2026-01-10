import OpenAI from 'openai';

// ============================================
// CONFIGURATION
// ============================================

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Système prompt astrologique
const ASTRO_SYSTEM_PROMPT = `Tu es un assistant astrologique expert et bienveillant nommé Astro.IA.

Tu combines connaissances traditionnelles et approche moderne de l'astrologie.
Tu réponds de manière claire, empathique et personnalisée.
Tu utilises des emojis cosmiques quand approprié : ✨🌙⭐🔮💫
Tu es là pour guider, pas pour prédire l'avenir de façon déterministe.

Reste concis (max 3-4 paragraphes) et structuré.`;

// ============================================
// HANDLER PRINCIPAL
// ============================================

export default async function handler(req, res) {
  const startTime = Date.now();

  // CORS preflight
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { userId, messages, astroProfile } = req.body;

    // Validation basique
    if (!userId || !messages || !Array.isArray(messages) || messages.length === 0) {
      return res.status(400).json({ 
        error: 'Validation error',
        message: 'userId et messages sont requis' 
      });
    }

    console.log(`[API] Chat request - User: ${userId}, Messages: ${messages.length}`);

    // Construire le contexte avec le profil
    let contextualizedMessages = [...messages];
    
    if (astroProfile && astroProfile.name) {
      const profileContext = `Contexte utilisateur: ${astroProfile.name}${
        astroProfile.birthDate ? `, né(e) le ${astroProfile.birthDate}` : ''
      }${astroProfile.zodiacSign ? `, signe ${astroProfile.zodiacSign}` : ''}${
        astroProfile.zodiacElement ? ` (élément: ${astroProfile.zodiacElement})` : ''
      }.`;

      contextualizedMessages = [
        { role: 'system', content: ASTRO_SYSTEM_PROMPT + '\n\n' + profileContext },
        ...messages.filter(m => m.role !== 'system'),
      ];
    } else {
      contextualizedMessages = [
        { role: 'system', content: ASTRO_SYSTEM_PROMPT },
        ...messages.filter(m => m.role !== 'system'),
      ];
    }

    // Appel OpenAI - GPT-3.5-turbo pour les tests (moins cher et plus rapide)
    const completion = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: contextualizedMessages,
      temperature: 0.7,
      max_tokens: 500, // Réduit pour économiser
    });

    const assistantMessage = completion.choices[0].message.content || '';
    const usage = completion.usage;

    // Calculer la latence
    const latencyMs = Date.now() - startTime;

    console.log(`[API] Success - Latency: ${latencyMs}ms, Tokens: ${usage?.total_tokens || 0}`);

    // Retourner la réponse (sans Supabase pour l'instant)
    return res.status(200).json({
      message: assistantMessage,
      conversationId: null, // Pas de persistance pour l'instant
      usage: {
        promptTokens: usage?.prompt_tokens || 0,
        completionTokens: usage?.completion_tokens || 0,
        totalTokens: usage?.total_tokens || 0,
      },
      latencyMs,
    });

  } catch (error) {
    console.error('[API] Error:', error);

    // Gestion d'erreurs spécifiques
    if (error.status === 429) {
      return res.status(429).json({
        error: 'Rate limit exceeded',
        message: 'Trop de requêtes. Réessayez dans quelques instants.',
      });
    }

    if (error.status === 401) {
      return res.status(500).json({
        error: 'Configuration error',
        message: 'Erreur de configuration de l\'API OpenAI',
      });
    }

    return res.status(500).json({
      error: 'Internal server error',
      message: error.message || 'Une erreur est survenue. Réessayez.',
    });
  }
}
