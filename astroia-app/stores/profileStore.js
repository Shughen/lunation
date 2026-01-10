import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Clé de stockage
const PROFILE_STORAGE_KEY = '@astroia_user_profile';

// Store Zustand avec persistance AsyncStorage pour le profil utilisateur
export const useProfileStore = create((set, get) => ({
  profile: {
    name: '',
    birthDate: null,
    birthTime: null,
    birthPlace: '',
    latitude: null,
    longitude: null,
    timezone: null,
    // Données astrologiques calculées
    sunSign: null,      // { id, name, emoji }
    moonSign: null,     // { id, name, emoji }
    ascendant: null,    // { id, name, emoji }
    // Gestion cycles menstruels
    gender: null,       // 'female' | 'male' | 'other' | null
    hasCycles: false,   // boolean - détermine l'affichage des fonctionnalités cycles
  },
  isLoading: false,
  hasProfile: false,
  
  // Charger le profil depuis AsyncStorage
  loadProfile: async () => {
    try {
      set({ isLoading: true });
      const stored = await AsyncStorage.getItem(PROFILE_STORAGE_KEY);
      if (stored) {
        let profile = JSON.parse(stored);
        // Reconstruire les dates
        if (profile.birthDate) {
          profile.birthDate = new Date(profile.birthDate);
        }
        if (profile.birthTime) {
          profile.birthTime = new Date(profile.birthTime);
        }
        
        // PATCH : Calculer le signe solaire si manquant (migration des anciens profils)
        if (profile.birthDate && !profile.sunSign) {
          const calculatedSign = calculateZodiacFromDate(profile.birthDate);
          if (calculatedSign) {
            profile.sunSign = {
              id: getSignId(calculatedSign.sign),
              name: calculatedSign.sign,
              emoji: calculatedSign.emoji,
            };
            console.log('[ProfileStore] Migration : Signe solaire calculé pour profil existant');
            // Sauvegarder le profil mis à jour
            await AsyncStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(profile));
          }
        }
        
        // PATCH : Migration des profils existants - ajouter gender et hasCycles si manquants
        let profileUpdated = false;
        if (profile.gender === undefined || profile.gender === null) {
          profile.gender = null;
          profileUpdated = true;
        }
        if (profile.hasCycles === undefined) {
          // Par défaut, hasCycles = false pour sécurité (ne pas afficher les cycles si non configuré)
          profile.hasCycles = false;
          profileUpdated = true;
        }
        
        // Si le profil a été mis à jour, sauvegarder
        if (profileUpdated) {
          console.log('[ProfileStore] Migration : gender et hasCycles ajoutés au profil existant');
          await AsyncStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(profile));
        }
        
        set({ 
          profile, 
          hasProfile: isProfileComplete(profile),
          isLoading: false 
        });
      } else {
        set({ isLoading: false });
      }
    } catch (error) {
      console.error('Erreur lors du chargement du profil:', error);
      set({ isLoading: false });
    }
  },
  
  // Sauvegarder le profil dans AsyncStorage
  saveProfile: async (profileData) => {
    try {
      let updatedProfile = { ...get().profile, ...profileData };
      
      // Calculer automatiquement le signe solaire si birthDate est fourni
      if (updatedProfile.birthDate && !updatedProfile.sunSign) {
        const calculatedSign = calculateZodiacFromDate(updatedProfile.birthDate);
        if (calculatedSign) {
          updatedProfile.sunSign = {
            id: getSignId(calculatedSign.sign),
            name: calculatedSign.sign,
            emoji: calculatedSign.emoji,
          };
          console.log('[ProfileStore] Signe solaire calculé automatiquement:', updatedProfile.sunSign);
        }
      }
      
      await AsyncStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(updatedProfile));
      set({ 
        profile: updatedProfile,
        hasProfile: isProfileComplete(updatedProfile)
      });
      return true;
    } catch (error) {
      console.error('Erreur lors de la sauvegarde du profil:', error);
      return false;
    }
  },
  
  // Mettre à jour un champ du profil
  updateField: (field, value) => {
    set((state) => ({
      profile: { ...state.profile, [field]: value }
    }));
  },
  
  // Réinitialiser le profil
  resetProfile: async () => {
    try {
      await AsyncStorage.removeItem(PROFILE_STORAGE_KEY);
      set({
        profile: {
          name: '',
          birthDate: null,
          birthTime: null,
          birthPlace: '',
          latitude: null,
          longitude: null,
          timezone: null,
          sunSign: null,
          moonSign: null,
          ascendant: null,
          gender: null,
          hasCycles: false,
        },
        hasProfile: false,
      });
      return true;
    } catch (error) {
      console.error('Erreur lors de la réinitialisation du profil:', error);
      return false;
    }
  },
  
  // Obtenir le pourcentage de complétion
  getCompletionPercentage: () => {
    const profile = get().profile;
    let completed = 0;
    let total = 4;
    
    if (profile.name && profile.name.trim().length > 0) completed++;
    if (profile.birthDate) completed++;
    if (profile.birthTime) completed++;
    if (profile.birthPlace && profile.birthPlace.trim().length > 0) completed++;
    
    return Math.round((completed / total) * 100);
  },
  
  // Obtenir le signe solaire (calculé ou stocké)
  getSunSign: () => {
    const profile = get().profile;
    // Si déjà stocké, le retourner
    if (profile.sunSign) return profile.sunSign;
    // Sinon calculer depuis la date de naissance
    return get().getZodiacSign();
  },

  // Obtenir l'ascendant (stocké)
  getAscendant: () => {
    const profile = get().profile;
    return profile.ascendant || null;
  },

  // Obtenir le signe lunaire (stocké)
  getMoonSign: () => {
    const profile = get().profile;
    return profile.moonSign || null;
  },

  // Vérifier si le thème natal complet existe
  hasNatal: () => {
    const profile = get().profile;
    return !!(profile.sunSign && profile.moonSign && profile.ascendant);
  },

  // Obtenir les données du thème natal (IDs uniquement)
  getNatal: () => {
    const profile = get().profile;
    if (!profile.sunSign || !profile.moonSign || !profile.ascendant) {
      return null;
    }
    return {
      sun: profile.sunSign.id,
      moon: profile.moonSign.id,
      asc: profile.ascendant.id,
    };
  },

  // Sauvegarder les données astrologiques du thème natal
  saveAstrologicalData: async (astroData) => {
    try {
      const profile = get().profile;
      const updatedProfile = {
        ...profile,
        sunSign: astroData.sunSign,
        moonSign: astroData.moonSign,
        ascendant: astroData.ascendant,
      };
      await AsyncStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(updatedProfile));
      set({ profile: updatedProfile });
      return true;
    } catch (error) {
      console.error('Erreur sauvegarde données astro:', error);
      return false;
    }
  },

  // Mettre à jour le genre et hasCycles
  updateGenderAndCycles: async (gender, hasCycles) => {
    try {
      const profile = get().profile;
      const updatedProfile = {
        ...profile,
        gender: gender,
        hasCycles: hasCycles,
      };
      await AsyncStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(updatedProfile));
      set({ profile: updatedProfile });
      return true;
    } catch (error) {
      console.error('Erreur mise à jour gender/hasCycles:', error);
      return false;
    }
  },

  // Helper : déterminer si les cycles doivent être affichés
  shouldShowCycles: () => {
    const profile = get().profile;
    return profile.gender === 'female' && profile.hasCycles === true;
  },

  // Calculer le signe astrologique
  getZodiacSign: () => {
    const profile = get().profile;
    // Si déjà stocké, le retourner
    if (profile.sunSign) return profile.sunSign;
    // Sinon calculer depuis la date de naissance
    if (!profile.birthDate) return null;
    
    const date = new Date(profile.birthDate);
    const month = date.getMonth() + 1;
    const day = date.getDate();
    
    if ((month === 3 && day >= 21) || (month === 4 && day <= 19)) return { sign: 'Bélier', emoji: '♈', element: 'Feu' };
    if ((month === 4 && day >= 20) || (month === 5 && day <= 20)) return { sign: 'Taureau', emoji: '♉', element: 'Terre' };
    if ((month === 5 && day >= 21) || (month === 6 && day <= 20)) return { sign: 'Gémeaux', emoji: '♊', element: 'Air' };
    if ((month === 6 && day >= 21) || (month === 7 && day <= 22)) return { sign: 'Cancer', emoji: '♋', element: 'Eau' };
    if ((month === 7 && day >= 23) || (month === 8 && day <= 22)) return { sign: 'Lion', emoji: '♌', element: 'Feu' };
    if ((month === 8 && day >= 23) || (month === 9 && day <= 22)) return { sign: 'Vierge', emoji: '♍', element: 'Terre' };
    if ((month === 9 && day >= 23) || (month === 10 && day <= 22)) return { sign: 'Balance', emoji: '♎', element: 'Air' };
    if ((month === 10 && day >= 23) || (month === 11 && day <= 21)) return { sign: 'Scorpion', emoji: '♏', element: 'Eau' };
    if ((month === 11 && day >= 22) || (month === 12 && day <= 21)) return { sign: 'Sagittaire', emoji: '♐', element: 'Feu' };
    if ((month === 12 && day >= 22) || (month === 1 && day <= 19)) return { sign: 'Capricorne', emoji: '♑', element: 'Terre' };
    if ((month === 1 && day >= 20) || (month === 2 && day <= 18)) return { sign: 'Verseau', emoji: '♒', element: 'Air' };
    if ((month === 2 && day >= 19) || (month === 3 && day <= 20)) return { sign: 'Poissons', emoji: '♓', element: 'Eau' };
    
    return null;
  },
}));

// Helper pour calculer le signe zodiacal depuis une date
function calculateZodiacFromDate(birthDate) {
  if (!birthDate) return null;
  
  const date = new Date(birthDate);
  const month = date.getMonth() + 1;
  const day = date.getDate();
  
  if ((month === 3 && day >= 21) || (month === 4 && day <= 19)) return { sign: 'Bélier', emoji: '♈', element: 'Feu' };
  if ((month === 4 && day >= 20) || (month === 5 && day <= 20)) return { sign: 'Taureau', emoji: '♉', element: 'Terre' };
  if ((month === 5 && day >= 21) || (month === 6 && day <= 20)) return { sign: 'Gémeaux', emoji: '♊', element: 'Air' };
  if ((month === 6 && day >= 21) || (month === 7 && day <= 22)) return { sign: 'Cancer', emoji: '♋', element: 'Eau' };
  if ((month === 7 && day >= 23) || (month === 8 && day <= 22)) return { sign: 'Lion', emoji: '♌', element: 'Feu' };
  if ((month === 8 && day >= 23) || (month === 9 && day <= 22)) return { sign: 'Vierge', emoji: '♍', element: 'Terre' };
  if ((month === 9 && day >= 23) || (month === 10 && day <= 22)) return { sign: 'Balance', emoji: '♎', element: 'Air' };
  if ((month === 10 && day >= 23) || (month === 11 && day <= 21)) return { sign: 'Scorpion', emoji: '♏', element: 'Eau' };
  if ((month === 11 && day >= 22) || (month === 12 && day <= 21)) return { sign: 'Sagittaire', emoji: '♐', element: 'Feu' };
  if ((month === 12 && day >= 22) || (month === 1 && day <= 19)) return { sign: 'Capricorne', emoji: '♑', element: 'Terre' };
  if ((month === 1 && day >= 20) || (month === 2 && day <= 18)) return { sign: 'Verseau', emoji: '♒', element: 'Air' };
  if ((month === 2 && day >= 19) || (month === 3 && day <= 20)) return { sign: 'Poissons', emoji: '♓', element: 'Eau' };
  
  return null;
}

// Helper pour mapper un nom de signe vers son ID
function getSignId(signName) {
  const mapping = {
    'Bélier': 1, 'Taureau': 2, 'Gémeaux': 3, 'Cancer': 4,
    'Lion': 5, 'Vierge': 6, 'Balance': 7, 'Scorpion': 8,
    'Sagittaire': 9, 'Capricorne': 10, 'Verseau': 11, 'Poissons': 12
  };
  return mapping[signName] || 1;
}

// Helper pour vérifier si le profil est complet
// Exporté pour être utilisé dans le routing initial
export function isProfileComplete(profile) {
  return !!(
    profile &&
    profile.name &&
    profile.name.trim().length > 0 &&
    profile.birthDate &&
    profile.birthTime &&
    profile.birthPlace &&
    profile.birthPlace.trim().length > 0
  );
}

// Validation du profil
export const validateProfile = (profile) => {
  const errors = {};
  
  // Nom
  if (!profile.name || profile.name.trim().length === 0) {
    errors.name = 'Le nom est requis';
  } else if (profile.name.trim().length < 2) {
    errors.name = 'Le nom doit contenir au moins 2 caractères';
  }
  
  // Date de naissance
  if (!profile.birthDate) {
    errors.birthDate = 'La date de naissance est requise';
  } else {
    const date = new Date(profile.birthDate);
    const now = new Date();
    if (date > now) {
      errors.birthDate = 'La date ne peut pas être dans le futur';
    }
    if (date.getFullYear() < 1900) {
      errors.birthDate = 'Date invalide';
    }
  }
  
  // Heure de naissance
  if (!profile.birthTime) {
    errors.birthTime = 'L\'heure de naissance est requise';
  }
  
  // Lieu de naissance
  if (!profile.birthPlace || profile.birthPlace.trim().length === 0) {
    errors.birthPlace = 'Le lieu de naissance est requis';
  } else if (profile.birthPlace.trim().length < 2) {
    errors.birthPlace = 'Le lieu doit contenir au moins 2 caractères';
  }
  
  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
};

