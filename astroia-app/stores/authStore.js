import { create } from 'zustand';
import { supabase, getCurrentUser, signOut as supabaseSignOut } from '@/lib/supabase';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useProfileStore } from './profileStore';

// Store d'authentification avec Supabase
export const useAuthStore = create((set, get) => ({
  user: null,
  session: null,
  isLoading: true,
  isAuthenticated: false,
  
  // Initialiser l'authentification au démarrage
  initialize: async () => {
    try {
      set({ isLoading: true });
      
      // Récupérer la session actuelle
      const { data: { session } } = await supabase.auth.getSession();
      
      if (session) {
        set({
          user: session.user,
          session,
          isAuthenticated: true,
          isLoading: false,
        });
      } else {
        set({ isLoading: false });
      }
      
      // Écouter les changements d'authentification
      supabase.auth.onAuthStateChange(async (event, session) => {
        const previousUser = get().user;
        const newUser = session?.user ?? null;
        
        // MODIFICATION : Nettoyer le profil local si changement d'utilisateur ou déconnexion
        if (event === 'SIGNED_OUT' || (previousUser && newUser && previousUser.id !== newUser.id)) {
          console.log('[AuthStore] Changement d\'utilisateur ou déconnexion, nettoyage du profil local');
          await AsyncStorage.multiRemove([
            '@astroia_user_profile',
            '@astroia_journal_entries',
            'natal_chart_local',
            '@profile_migrated_to_supabase',
          ]);
          
          // Reset du profil dans le store
          useProfileStore.getState().resetProfile();
        }
        
        set({
          user: newUser,
          session,
          isAuthenticated: !!session,
        });
      });
    } catch (error) {
      console.error('Erreur d\'initialisation auth:', error);
      set({ isLoading: false });
    }
  },
  
  // Inscription avec email + mot de passe
  signUp: async (email, password, userData = {}) => {
    try {
      console.log('[AuthStore] Tentative de signUp pour:', email);
      const { data, error } = await supabase.auth.signUp({
        email,
        password,
        options: {
          data: userData, // Métadonnées utilisateur
        },
      });
      
      if (error) {
        console.error('[AuthStore] Erreur signup:', error);
        throw error;
      }
      
      // Si une session est retournée (pas de confirmation email nécessaire), mettre à jour le store
      if (data.session) {
        console.log('[AuthStore] Session créée lors du signUp, mise à jour du store');
        set({
          user: data.user,
          session: data.session,
          isAuthenticated: true,
        });
      } else {
        console.log('[AuthStore] SignUp réussi mais pas de session (confirmation email requise)');
      }
      
      return { data, error: null };
    } catch (error) {
      console.error('[AuthStore] Erreur signup:', error);
      return { data: null, error };
    }
  },
  
  // Connexion avec email + mot de passe
  signIn: async (email, password) => {
    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password,
      });
      
      if (error) throw error;
      
      set({
        user: data.user,
        session: data.session,
        isAuthenticated: true,
      });
      
      return { data, error: null };
    } catch (error) {
      console.error('Erreur signin:', error);
      return { data: null, error };
    }
  },
  
  // Connexion magique avec OTP (Email sans mot de passe)
  signInWithOTP: async (email) => {
    try {
      const { data, error } = await supabase.auth.signInWithOtp({
        email,
        options: {
          shouldCreateUser: true,
        },
      });
      
      if (error) throw error;
      
      return { data, error: null };
    } catch (error) {
      console.error('Erreur OTP:', error);
      return { data: null, error };
    }
  },
  
  // Vérifier le code OTP
  verifyOTP: async (email, token) => {
    try {
      const { data, error } = await supabase.auth.verifyOtp({
        email,
        token,
        type: 'email',
      });
      
      if (error) throw error;
      
      set({
        user: data.user,
        session: data.session,
        isAuthenticated: true,
      });
      
      return { data, error: null };
    } catch (error) {
      console.error('Erreur verify OTP:', error);
      return { data: null, error };
    }
  },
  
  // Déconnexion
  // MODIFICATION : Nettoyer aussi natal_chart_local et le profil
  signOut: async () => {
    try {
      await supabaseSignOut();
      
      // Nettoyer le store local (profil, journal, thème natal, flags de migration)
      await AsyncStorage.multiRemove([
        '@astroia_journal_entries',
        'natal_chart_local',
        '@profile_migrated_to_supabase',
      ]);
      
      // Reset du profil dans le store
      const { resetProfile } = await import('./profileStore');
      useProfileStore.getState().resetProfile();
      
      set({
        user: null,
        session: null,
        isAuthenticated: false,
      });
      
      return { error: null };
    } catch (error) {
      console.error('Erreur signout:', error);
      return { error };
    }
  },
  
  // Réinitialiser le mot de passe
  resetPassword: async (email) => {
    try {
      const { data, error } = await supabase.auth.resetPasswordForEmail(email);
      
      if (error) throw error;
      
      return { data, error: null };
    } catch (error) {
      console.error('Erreur reset password:', error);
      return { data: null, error };
    }
  },
  
  // Mettre à jour l'utilisateur
  updateUser: async (updates) => {
    try {
      const { data, error } = await supabase.auth.updateUser(updates);
      
      if (error) throw error;
      
      set({ user: data.user });
      
      return { data, error: null };
    } catch (error) {
      console.error('Erreur update user:', error);
      return { data: null, error };
    }
  },
}));

