import { supabase } from '@/lib/supabase';

/**
 * Service pour gérer les profils utilisateurs avec Supabase
 */
class ProfileService {
  /**
   * Récupérer le profil de l'utilisateur connecté
   */
  async getProfile() {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) {
        console.log('[ProfileService] Aucun utilisateur connecté');
        return null;
      }

      const { data, error } = await supabase
        .from('profiles')
        .select('*')
        .eq('id', user.id)
        .single();

      if (error) {
        // PGRST116 = not found (profil n'existe pas encore)
        if (error.code === 'PGRST116') {
          console.log('[ProfileService] Aucun profil trouvé pour cet utilisateur');
          return null;
        }
        throw error;
      }

      return data;
    } catch (error) {
      console.error('[ProfileService] Erreur getProfile:', error);
      return null;
    }
  }

  /**
   * Créer ou mettre à jour le profil
   */
  async upsertProfile(profileData) {
    try {
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) throw new Error('Non authentifié');

      const payload = {
        id: user.id,
        email: user.email,
        ...profileData,
        updated_at: new Date().toISOString(),
      };

      const { data, error } = await supabase
        .from('profiles')
        .upsert(payload, {
          onConflict: 'id',
        })
        .select()
        .single();

      if (error) throw error;

      console.log('[ProfileService] Profil synchronisé avec succès');
      return data;
    } catch (error) {
      console.error('[ProfileService] Erreur upsertProfile:', error);
      throw error;
    }
  }

  /**
   * Synchroniser le profil local vers Supabase
   * Convertit le format local vers le format Supabase
   */
  async syncLocalProfile(localProfile) {
    try {
      console.log('[ProfileService] syncLocalProfile appelé avec:', {
        hasName: !!localProfile?.name,
        name: localProfile?.name,
        hasBirthDate: !!localProfile?.birthDate,
        hasBirthTime: !!localProfile?.birthTime,
        hasBirthPlace: !!localProfile?.birthPlace,
      });
      
      // Mapper le profil local vers le format Supabase
      // NOTE: N'utiliser que les colonnes qui existent dans le schéma Supabase actuel
      // Pour l'instant, la table profiles n'a pas encore astrological_data, latitude, longitude, timezone
      const supabaseProfile = {
        name: localProfile.name || null,
        birth_date: localProfile.birthDate ? localProfile.birthDate.toISOString().split('T')[0] : null, // Format DATE seulement
        birth_time: localProfile.birthTime 
          ? localProfile.birthTime.toTimeString().slice(0, 8) // Format HH:MM:SS
          : null,
        birth_place: localProfile.birthPlace || null,
        // Signe solaire (colonnes existantes)
        zodiac_sign: localProfile.sunSign?.name || null,
        zodiac_element: localProfile.sunSign?.element || null,
        // NOTE: moonSign et ascendant seront stockés dans natal_charts uniquement pour l'instant
        // TODO: Ajouter colonnes astrological_data, latitude, longitude, timezone dans Supabase plus tard
      };

      const result = await this.upsertProfile(supabaseProfile);
      console.log('[ProfileService] ✅ syncLocalProfile réussi:', {
        hasResult: !!result,
        hasName: !!result?.name,
      });
      return result;
    } catch (error) {
      console.error('[ProfileService] ❌ Erreur syncLocalProfile:', error);
      throw error;
    }
  }

  /**
   * Charger le profil depuis Supabase et le convertir en format local
   */
  async loadProfileFromSupabase() {
    try {
      const supabaseProfile = await this.getProfile();
      
      if (!supabaseProfile) {
        return null;
      }

      // Convertir le format Supabase vers le format local
      const localProfile = {
        name: supabaseProfile.name || '',
        birthDate: supabaseProfile.birth_date ? new Date(supabaseProfile.birth_date) : null,
        birthTime: supabaseProfile.birth_time 
          ? (() => {
              // Convertir "HH:MM:SS" en Date
              const [hours, minutes] = supabaseProfile.birth_time.split(':');
              const date = new Date();
              date.setHours(parseInt(hours), parseInt(minutes), 0, 0);
              return date;
            })()
          : null,
        birthPlace: supabaseProfile.birth_place || '',
        latitude: supabaseProfile.latitude || null,
        longitude: supabaseProfile.longitude || null,
        timezone: supabaseProfile.timezone || null,
        // Reconstruire sunSign depuis zodiac_sign ou astrological_data
        sunSign: supabaseProfile.astrological_data?.sunSign || (supabaseProfile.zodiac_sign ? {
          name: supabaseProfile.zodiac_sign,
          element: supabaseProfile.zodiac_element || null,
          // Essayer de trouver l'emoji et l'ID
          id: this.getSignIdFromName(supabaseProfile.zodiac_sign),
          emoji: this.getSignEmojiFromName(supabaseProfile.zodiac_sign),
        } : null),
        // Charger moonSign et ascendant depuis astrological_data
        moonSign: supabaseProfile.astrological_data?.moonSign || null,
        ascendant: supabaseProfile.astrological_data?.ascendant || null,
      };

      return localProfile;
    } catch (error) {
      console.error('[ProfileService] Erreur loadProfileFromSupabase:', error);
      return null;
    }
  }

  /**
   * Helper: Obtenir l'ID d'un signe depuis son nom
   */
  getSignIdFromName(signName) {
    const mapping = {
      'Bélier': 1, 'Taureau': 2, 'Gémeaux': 3, 'Cancer': 4,
      'Lion': 5, 'Vierge': 6, 'Balance': 7, 'Scorpion': 8,
      'Sagittaire': 9, 'Capricorne': 10, 'Verseau': 11, 'Poissons': 12,
    };
    return mapping[signName] || null;
  }

  /**
   * Helper: Obtenir l'emoji d'un signe depuis son nom
   */
  getSignEmojiFromName(signName) {
    const mapping = {
      'Bélier': '♈', 'Taureau': '♉', 'Gémeaux': '♊', 'Cancer': '♋',
      'Lion': '♌', 'Vierge': '♍', 'Balance': '♎', 'Scorpion': '♏',
      'Sagittaire': '♐', 'Capricorne': '♑', 'Verseau': '♒', 'Poissons': '♓',
    };
    return mapping[signName] || '⭐';
  }
}

export const profileService = new ProfileService();

