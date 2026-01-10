import Constants from 'expo-constants';

// Configuration de l'API IA
const AI_API_URL = Constants.expoConfig?.extra?.aiApiUrl || 'http://localhost:3000/api/generate';

/**
 * Service pour communiquer avec l'API IA
 */
class AIService {
  /**
   * Génère une réponse de l'IA
   * @param {Array} messages - Historique des messages [{role: 'user'|'assistant', content: string}]
   * @param {Object} userProfile - Profil utilisateur pour le contexte (optionnel)
   * @returns {Promise<string>} - Réponse de l'IA
   */
  async generateResponse(messages, userProfile = null) {
    try {
      const response = await fetch(AI_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          messages,
          userProfile,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Erreur API');
      }

      const data = await response.json();
      return data.message;
    } catch (error) {
      console.error('Erreur AIService:', error);
      throw error;
    }
  }

  /**
   * Génère une réponse astrologique personnalisée
   * @param {string} question - Question de l'utilisateur
   * @param {Object} userProfile - Profil utilisateur
   * @returns {Promise<string>}
   */
  async getAstrologicalAdvice(question, userProfile) {
    const messages = [
      {
        role: 'user',
        content: question,
      },
    ];

    return this.generateResponse(messages, userProfile);
  }

  /**
   * Analyse un thème natal (placeholder pour le futur)
   * @param {Object} birthData - Données de naissance
   * @returns {Promise<Object>}
   */
  async analyzeNatalChart(birthData) {
    const messages = [
      {
        role: 'user',
        content: `Analyse mon thème natal: né(e) le ${birthData.birthDate} à ${birthData.birthTime} à ${birthData.birthPlace}`,
      },
    ];

    const response = await this.generateResponse(messages, birthData);
    
    return {
      analysis: response,
      sun: birthData.zodiacSign,
      element: birthData.zodiacElement,
    };
  }

  /**
   * Génère un horoscope quotidien
   * @param {string} zodiacSign - Signe astrologique
   * @returns {Promise<string>}
   */
  async getDailyHoroscope(zodiacSign) {
    const messages = [
      {
        role: 'user',
        content: `Donne-moi l'horoscope du jour pour le signe ${zodiacSign}`,
      },
    ];

    return this.generateResponse(messages);
  }

  /**
   * Analyse de compatibilité (placeholder)
   * @param {string} sign1 - Premier signe
   * @param {string} sign2 - Deuxième signe
   * @returns {Promise<string>}
   */
  async getCompatibility(sign1, sign2) {
    const messages = [
      {
        role: 'user',
        content: `Quelle est la compatibilité astrologique entre ${sign1} et ${sign2} ?`,
      },
    ];

    return this.generateResponse(messages);
  }
}

export const aiService = new AIService();

