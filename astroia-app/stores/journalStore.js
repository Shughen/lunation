import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Clé de stockage
const JOURNAL_STORAGE_KEY = '@astroia_journal_entries';

// Store Zustand avec persistance AsyncStorage
export const useJournalStore = create((set, get) => ({
  entries: [],
  isLoading: false,
  
  // Charger les entrées depuis AsyncStorage
  loadEntries: async () => {
    try {
      set({ isLoading: true });
      const stored = await AsyncStorage.getItem(JOURNAL_STORAGE_KEY);
      if (stored) {
        const entries = JSON.parse(stored);
        set({ entries, isLoading: false });
      } else {
        set({ isLoading: false });
      }
    } catch (error) {
      console.error('Erreur lors du chargement des entrées:', error);
      set({ isLoading: false });
    }
  },
  
  // Sauvegarder dans AsyncStorage
  saveEntries: async (entries) => {
    try {
      await AsyncStorage.setItem(JOURNAL_STORAGE_KEY, JSON.stringify(entries));
    } catch (error) {
      console.error('Erreur lors de la sauvegarde:', error);
    }
  },
  
  // Ajouter une nouvelle entrée
  addEntry: async (entry) => {
    const newEntry = {
      id: Date.now().toString(),
      ...entry,
      createdAt: new Date().toISOString(),
    };
    
    const updatedEntries = [newEntry, ...get().entries];
    set({ entries: updatedEntries });
    await get().saveEntries(updatedEntries);
    return newEntry;
  },
  
  // Mettre à jour une entrée
  updateEntry: async (id, updates) => {
    const updatedEntries = get().entries.map((entry) =>
      entry.id === id ? { ...entry, ...updates, updatedAt: new Date().toISOString() } : entry
    );
    set({ entries: updatedEntries });
    await get().saveEntries(updatedEntries);
  },
  
  // Supprimer une entrée
  deleteEntry: async (id) => {
    const updatedEntries = get().entries.filter((entry) => entry.id !== id);
    set({ entries: updatedEntries });
    await get().saveEntries(updatedEntries);
  },
  
  // Obtenir une entrée par ID
  getEntryById: (id) => {
    return get().entries.find((entry) => entry.id === id);
  },
  
  // Obtenir les statistiques
  getStats: () => {
    const entries = get().entries;
    if (entries.length === 0) return null;
    
    // Compter les humeurs
    const moodCounts = entries.reduce((acc, entry) => {
      acc[entry.mood] = (acc[entry.mood] || 0) + 1;
      return acc;
    }, {});
    
    // Humeur la plus fréquente
    const mostFrequentMood = Object.entries(moodCounts).reduce((a, b) => 
      moodCounts[a[0]] > moodCounts[b[0]] ? a : b
    )[0];
    
    return {
      totalEntries: entries.length,
      moodCounts,
      mostFrequentMood,
    };
  },
}));

// Émojis et labels pour les humeurs
export const MOODS = {
  amazing: { emoji: '🤩', label: 'Incroyable', color: '#10B981' },
  happy: { emoji: '😊', label: 'Heureux', color: '#F59E0B' },
  neutral: { emoji: '😐', label: 'Neutre', color: '#6366F1' },
  sad: { emoji: '😔', label: 'Triste', color: '#8B5CF6' },
  anxious: { emoji: '😰', label: 'Anxieux', color: '#EF4444' },
};

// Suggestions de tags
export const SUGGESTED_TAGS = [
  'Travail',
  'Famille',
  'Amour',
  'Amitié',
  'Santé',
  'Créativité',
  'Spiritualité',
  'Rêve',
  'Pleine lune',
  'Nouvelle lune',
  'Méditation',
  'Gratitude',
];

