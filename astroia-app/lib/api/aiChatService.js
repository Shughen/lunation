import Constants from 'expo-constants';
import { supabase } from '@/lib/supabase';

// Configuration de l'API IA
const AI_API_URL = Constants.expoConfig?.extra?.aiApiUrl || 'http://localhost:3000/api/ai/chat';

/**
 * Service pour communiquer avec l'API IA via proxy Vercel
 * Toutes les appels à OpenAI passent par ce proxy pour sécuriser la clé API
 */
class AIChatService {
  /**
   * Envoyer un message et recevoir une réponse de l'IA
   * @param {Object} params
   * @param {string} params.chatId - ID de la conversation (optionnel)
   * @param {string} params.userId - ID utilisateur Supabase
   * @param {Array} params.messages - Historique messages [{role, content}]
   * @param {Object} params.astroProfile - Profil astrologique (optionnel)
   * @returns {Promise<Object>} - { message, conversationId, usage, latencyMs }
   */
  async sendMessage({ chatId, userId, messages, astroProfile = null }) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 30000); // 30s timeout

      const response = await fetch(AI_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          chatId,
          userId,
          messages,
          astroProfile,
        }),
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        
        // Gestion d'erreurs spécifiques avec messages explicites
        if (response.status === 429) {
          throw new Error('Trop de requêtes. Veuillez patienter quelques instants avant de réessayer.');
        }
        
        if (response.status === 401 || response.status === 403) {
          throw new Error('Erreur d\'authentification. Veuillez vous reconnecter.');
        }

        if (response.status === 500 || response.status >= 502) {
          throw new Error('Le service est temporairement indisponible. Veuillez réessayer plus tard.');
        }

        if (response.status === 408 || response.status === 504) {
          throw new Error('La requête a pris trop de temps. Vérifiez votre connexion internet et réessayez.');
        }

        throw new Error(errorData.message || `Erreur serveur (${response.status}). Veuillez réessayer.`);
      }

      const data = await response.json();
      return data;

    } catch (error) {
      console.error('[AIChatService] Error:', error);
      
      // Erreur de timeout
      if (error.name === 'AbortError') {
        throw new Error('La requête a pris trop de temps. Vérifiez votre connexion et réessayez.');
      }

      // Erreur réseau
      if (error.message === 'Failed to fetch' || error.message.includes('Network') || error.message.includes('network')) {
        throw new Error('Pas de connexion internet. Vérifiez votre connexion réseau et réessayez.');
      }

      // Si l'erreur a déjà un message explicite, la renvoyer telle quelle
      if (error.message && !error.message.includes('Error')) {
        throw error;
      }

      // Message générique avec contexte
      throw new Error(`Impossible de communiquer avec l'assistant IA. ${error.message || 'Veuillez réessayer.'}`);
    }
  }

  /**
   * Récupérer l'historique d'une conversation depuis Supabase
   * @param {string} conversationId - ID de la conversation
   * @returns {Promise<Array>} - Messages [{role, content, created_at}]
   */
  async getConversationHistory(conversationId) {
    try {
      const { data, error } = await supabase
        .from('chat_messages')
        .select('role, content, created_at')
        .eq('conversation_id', conversationId)
        .order('created_at', { ascending: true });

      if (error) throw error;

      return data || [];
    } catch (error) {
      console.error('[AIChatService] Error fetching history:', error);
      return [];
    }
  }

  /**
   * Récupérer toutes les conversations de l'utilisateur
   * @returns {Promise<Array>} - Conversations
   */
  async getUserConversations() {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) return [];

      const { data, error } = await supabase
        .from('chat_conversations')
        .select('*')
        .eq('user_id', user.id)
        .order('updated_at', { ascending: false });

      if (error) throw error;

      return data || [];
    } catch (error) {
      console.error('[AIChatService] Error fetching conversations:', error);
      return [];
    }
  }

  /**
   * Supprimer une conversation
   * @param {string} conversationId
   */
  async deleteConversation(conversationId) {
    try {
      const { error } = await supabase
        .from('chat_conversations')
        .delete()
        .eq('id', conversationId);

      if (error) throw error;

      return true;
    } catch (error) {
      console.error('[AIChatService] Error deleting conversation:', error);
      throw error;
    }
  }
}

export const aiChatService = new AIChatService();

