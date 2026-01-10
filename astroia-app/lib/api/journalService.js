import { supabase } from '@/lib/supabase';

/**
 * Service pour gérer le journal d'humeur avec Supabase
 */
class JournalService {
  /**
   * Récupérer toutes les entrées de l'utilisateur
   */
  async getEntries() {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) throw new Error('Non authentifié');

      const { data, error } = await supabase
        .from('journal_entries')
        .select('*')
        .eq('user_id', user.id)
        .order('created_at', { ascending: false });

      if (error) throw error;

      return data || [];
    } catch (error) {
      console.error('Erreur getEntries:', error);
      return [];
    }
  }

  /**
   * Créer une nouvelle entrée
   */
  async createEntry(entry) {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) throw new Error('Non authentifié');

      const { data, error } = await supabase
        .from('journal_entries')
        .insert({
          user_id: user.id,
          mood: entry.mood,
          note: entry.note,
          tags: entry.tags,
          moon_phase: entry.moonPhase,
        })
        .select()
        .single();

      if (error) throw error;

      return data;
    } catch (error) {
      console.error('Erreur createEntry:', error);
      throw error;
    }
  }

  /**
   * Mettre à jour une entrée
   */
  async updateEntry(id, updates) {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) throw new Error('Non authentifié');

      const { data, error } = await supabase
        .from('journal_entries')
        .update({
          mood: updates.mood,
          note: updates.note,
          tags: updates.tags,
          updated_at: new Date().toISOString(),
        })
        .eq('id', id)
        .eq('user_id', user.id)
        .select()
        .single();

      if (error) throw error;

      return data;
    } catch (error) {
      console.error('Erreur updateEntry:', error);
      throw error;
    }
  }

  /**
   * Supprimer une entrée
   */
  async deleteEntry(id) {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) throw new Error('Non authentifié');

      const { error } = await supabase
        .from('journal_entries')
        .delete()
        .eq('id', id)
        .eq('user_id', user.id);

      if (error) throw error;

      return true;
    } catch (error) {
      console.error('Erreur deleteEntry:', error);
      throw error;
    }
  }

  /**
   * Synchroniser les entrées locales vers Supabase
   */
  async syncLocalEntries(localEntries) {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) return;

      // Insérer toutes les entrées locales
      const entriesToSync = localEntries.map(entry => ({
        user_id: user.id,
        mood: entry.mood,
        note: entry.note,
        tags: entry.tags,
        moon_phase: entry.moonPhase,
        created_at: entry.createdAt,
      }));

      const { data, error } = await supabase
        .from('journal_entries')
        .insert(entriesToSync)
        .select();

      if (error) throw error;

      return data;
    } catch (error) {
      console.error('Erreur syncLocalEntries:', error);
      throw error;
    }
  }

  /**
   * Obtenir les statistiques
   */
  async getStats() {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) throw new Error('Non authentifié');

      const { data, error } = await supabase
        .from('journal_stats')
        .select('*')
        .eq('user_id', user.id)
        .single();

      if (error && error.code !== 'PGRST116') {
        throw error;
      }

      return data;
    } catch (error) {
      console.error('Erreur getStats:', error);
      return null;
    }
  }
}

export const journalService = new JournalService();

