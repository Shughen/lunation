import { 
  View, 
  Text, 
  StyleSheet, 
  TouchableOpacity, 
  ScrollView, 
  TextInput,
  KeyboardAvoidingView,
  Platform,
  Animated,
  Alert
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';
import { useJournalStore, MOODS, SUGGESTED_TAGS } from '@/stores/journalStore';
import { trackEvents } from '@/lib/analytics';
import { getSmartTagSuggestions } from '@/lib/services/tagSuggestionService';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useState, useEffect, useRef } from 'react';
import { useRouter } from 'expo-router';

export default function NewJournalEntryScreen() {
  const router = useRouter();
  const { addEntry } = useJournalStore();
  
  const [mood, setMood] = useState(null);
  const [note, setNote] = useState('');
  const [selectedTags, setSelectedTags] = useState([]);
  const [customTag, setCustomTag] = useState('');
  const [isSaving, setIsSaving] = useState(false);
  const [suggestedTags, setSuggestedTags] = useState(SUGGESTED_TAGS);
  
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 400,
      useNativeDriver: true,
    }).start();
    
    // Charger suggestions initiales
    loadSmartTags();
  }, []);

  // Recharger suggestions quand humeur change
  useEffect(() => {
    if (mood) {
      loadSmartTags(mood);
    }
  }, [mood]);

  const loadSmartTags = async (currentMood = null) => {
    try {
      const smart = await getSmartTagSuggestions(currentMood);
      setSuggestedTags(smart);
    } catch (error) {
      console.error('[Journal] Load tags error:', error);
    }
  };

  const toggleTag = (tag) => {
    if (selectedTags.includes(tag)) {
      setSelectedTags(selectedTags.filter(t => t !== tag));
    } else {
      setSelectedTags([...selectedTags, tag]);
    }
  };

  const addCustomTag = () => {
    if (customTag.trim() && !selectedTags.includes(customTag.trim())) {
      setSelectedTags([...selectedTags, customTag.trim()]);
      setCustomTag('');
    }
  };

  const handleSave = async () => {
    if (!mood) {
      Alert.alert('Humeur requise', 'Veuillez sélectionner une humeur');
      return;
    }

    setIsSaving(true);
    
    try {
      await addEntry({
        mood,
        note: note.trim(),
        tags: selectedTags,
        moonPhase: getMoonPhase(), // Fonction helper pour la phase lunaire
      });

      // Track analytics avec phase cycle
      try {
        const cycleConfig = await AsyncStorage.getItem('cycle_config');
        let phase = 'unknown';
        if (cycleConfig) {
          const { lastPeriodDate, cycleLength } = JSON.parse(cycleConfig);
          const daysSince = Math.floor((new Date() - new Date(lastPeriodDate)) / (1000 * 60 * 60 * 24));
          const dayOfCycle = (daysSince % cycleLength) + 1;
          
          if (dayOfCycle <= 5) phase = 'menstrual';
          else if (dayOfCycle <= 13) phase = 'follicular';
          else if (dayOfCycle <= 16) phase = 'ovulation';
          else phase = 'luteal';
        }
        
        trackEvents.journalEntryCreated(mood, phase);
      } catch (err) {
        console.log('[Journal] Analytics error:', err);
      }

      // Animation de succès
      Alert.alert(
        '✨ Entrée créée !',
        'Votre journal a été mis à jour',
        [{ text: 'OK', onPress: () => router.back() }]
      );
    } catch (error) {
      Alert.alert('Erreur', 'Impossible de sauvegarder l\'entrée');
      setIsSaving(false);
    }
  };

  const getMoonPhase = () => {
    // Calcul simple de la phase lunaire (peut être amélioré)
    const phases = ['🌑 Nouvelle lune', '🌒 Premier croissant', '🌓 Premier quartier', 
                    '🌔 Gibbeuse croissante', '🌕 Pleine lune', '🌖 Gibbeuse décroissante', 
                    '🌗 Dernier quartier', '🌘 Dernier croissant'];
    const index = Math.floor(Math.random() * phases.length); // Placeholder
    return phases[index];
  };

  const isValid = mood !== null;

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
            <Ionicons name="close" size={28} color={colors.text} />
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Nouvelle entrée</Text>
          <TouchableOpacity 
            onPress={handleSave}
            disabled={!isValid || isSaving}
            style={[styles.saveButton, (!isValid || isSaving) && styles.saveButtonDisabled]}
          >
            <Text style={[styles.saveButtonText, (!isValid || isSaving) && styles.saveButtonTextDisabled]}>
              {isSaving ? 'Enregistrement...' : 'Enregistrer'}
            </Text>
          </TouchableOpacity>
        </View>

        <KeyboardAvoidingView 
          behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
          style={styles.keyboardView}
        >
          <Animated.ScrollView
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
            style={{ opacity: fadeAnim }}
          >
            {/* Sélection d'humeur */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Comment vous sentez-vous ? *</Text>
              <View style={styles.moodsContainer}>
                {Object.entries(MOODS).map(([key, value]) => (
                  <MoodButton
                    key={key}
                    moodKey={key}
                    emoji={value.emoji}
                    label={value.label}
                    color={value.color}
                    isSelected={mood === key}
                    onPress={() => setMood(key)}
                  />
                ))}
              </View>
            </View>

            {/* Note */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Vos réflexions (optionnel)</Text>
              <View style={styles.noteInputContainer}>
                <TextInput
                  style={styles.noteInput}
                  placeholder="Que s'est-il passé aujourd'hui ? Comment les astres vous influencent-ils ?"
                  placeholderTextColor={colors.textMuted}
                  value={note}
                  onChangeText={setNote}
                  multiline
                  numberOfLines={6}
                  maxLength={1000}
                  textAlignVertical="top"
                />
                <Text style={styles.charCount}>{note.length}/1000</Text>
              </View>
            </View>

            {/* Tags suggérés */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>
                Tags suggérés {mood && '(basés sur ton humeur et ta phase)'}
              </Text>
              <View style={styles.tagsContainer}>
                {suggestedTags.map((tag) => (
                  <TouchableOpacity
                    key={tag}
                    style={[
                      styles.tagChip,
                      selectedTags.includes(tag) && styles.tagChipSelected
                    ]}
                    onPress={() => toggleTag(tag)}
                    activeOpacity={0.7}
                  >
                    <Text style={[
                      styles.tagChipText,
                      selectedTags.includes(tag) && styles.tagChipTextSelected
                    ]}>
                      {tag}
                    </Text>
                  </TouchableOpacity>
                ))}
              </View>

              {/* Tag personnalisé */}
              <View style={styles.customTagContainer}>
                <TextInput
                  style={styles.customTagInput}
                  placeholder="Ajouter un tag personnalisé"
                  placeholderTextColor={colors.textMuted}
                  value={customTag}
                  onChangeText={setCustomTag}
                  onSubmitEditing={addCustomTag}
                  returnKeyType="done"
                />
                {customTag.trim() && (
                  <TouchableOpacity onPress={addCustomTag} style={styles.addTagButton}>
                    <Ionicons name="add-circle" size={24} color={colors.accent} />
                  </TouchableOpacity>
                )}
              </View>

              {/* Tags sélectionnés */}
              {selectedTags.length > 0 && (
                <View style={styles.selectedTagsContainer}>
                  <Text style={styles.selectedTagsLabel}>Sélectionnés :</Text>
                  <View style={styles.selectedTags}>
                    {selectedTags.map((tag, index) => (
                      <View key={index} style={styles.selectedTag}>
                        <Text style={styles.selectedTagText}>{tag}</Text>
                        <TouchableOpacity onPress={() => toggleTag(tag)}>
                          <Ionicons name="close-circle" size={18} color={colors.textMuted} />
                        </TouchableOpacity>
                      </View>
                    ))}
                  </View>
                </View>
              )}
            </View>

            {/* Info card */}
            <View style={styles.infoCard}>
              <Ionicons name="sparkles" size={24} color={colors.accent} />
              <Text style={styles.infoText}>
                Suivre vos humeurs vous aide à identifier les cycles et patterns cosmiques dans votre vie.
              </Text>
            </View>
          </Animated.ScrollView>
        </KeyboardAvoidingView>
      </SafeAreaView>
    </LinearGradient>
  );
}

function MoodButton({ moodKey, emoji, label, color, isSelected, onPress }) {
  const scaleAnim = useRef(new Animated.Value(1)).current;

  const handlePressIn = () => {
    Animated.spring(scaleAnim, {
      toValue: 0.9,
      useNativeDriver: true,
    }).start();
  };

  const handlePressOut = () => {
    Animated.spring(scaleAnim, {
      toValue: 1,
      tension: 100,
      friction: 5,
      useNativeDriver: true,
    }).start();
  };

  return (
    <Animated.View style={{ transform: [{ scale: scaleAnim }] }}>
      <TouchableOpacity
        style={[
          styles.moodButton,
          isSelected && { ...styles.moodButtonSelected, borderColor: color }
        ]}
        onPress={onPress}
        onPressIn={handlePressIn}
        onPressOut={handlePressOut}
        activeOpacity={0.8}
      >
        <Text style={styles.moodEmoji}>{emoji}</Text>
        <Text style={[styles.moodLabel, isSelected && { color }]}>{label}</Text>
      </TouchableOpacity>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  keyboardView: {
    flex: 1,
  },

  // Header
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(139, 92, 246, 0.3)',
  },
  backButton: {
    width: 40,
    height: 40,
    alignItems: 'center',
    justifyContent: 'center',
  },
  headerTitle: {
    fontSize: fonts.sizes.xl,
    color: colors.text,
    fontWeight: 'bold',
  },
  saveButton: {
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
  },
  saveButtonDisabled: {
    opacity: 0.5,
  },
  saveButtonText: {
    fontSize: fonts.sizes.md,
    color: colors.accent,
    fontWeight: 'bold',
  },
  saveButtonTextDisabled: {
    color: colors.textMuted,
  },

  // Content
  scrollContent: {
    padding: spacing.md,
    paddingBottom: spacing.xxl,
  },

  // Section
  section: {
    marginBottom: spacing.xl,
  },
  sectionTitle: {
    fontSize: fonts.sizes.lg,
    color: colors.text,
    fontWeight: 'bold',
    marginBottom: spacing.md,
  },

  // Moods
  moodsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.sm,
  },
  moodButton: {
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: colors.cardBg,
    borderWidth: 2,
    borderColor: 'rgba(139, 92, 246, 0.2)',
    borderRadius: borderRadius.lg,
    padding: spacing.md,
    minWidth: 100,
  },
  moodButtonSelected: {
    backgroundColor: 'rgba(139, 92, 246, 0.15)',
    borderWidth: 2,
  },
  moodEmoji: {
    fontSize: 40,
    marginBottom: spacing.xs,
  },
  moodLabel: {
    fontSize: fonts.sizes.sm,
    color: colors.textSecondary,
    fontWeight: '600',
  },

  // Note
  noteInputContainer: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.2)',
    padding: spacing.md,
  },
  noteInput: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    minHeight: 120,
    marginBottom: spacing.sm,
  },
  charCount: {
    fontSize: fonts.sizes.xs,
    color: colors.textMuted,
    textAlign: 'right',
  },

  // Tags
  tagsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.sm,
    marginBottom: spacing.md,
  },
  tagChip: {
    backgroundColor: colors.cardBg,
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    borderRadius: borderRadius.full,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.2)',
  },
  tagChipSelected: {
    backgroundColor: 'rgba(139, 92, 246, 0.3)',
    borderColor: colors.primary,
  },
  tagChipText: {
    fontSize: fonts.sizes.sm,
    color: colors.textSecondary,
    fontWeight: '600',
  },
  tagChipTextSelected: {
    color: colors.text,
  },
  customTagContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.2)',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.xs,
    gap: spacing.sm,
  },
  customTagInput: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: colors.text,
    paddingVertical: spacing.sm,
  },
  addTagButton: {
    padding: spacing.xs,
  },
  selectedTagsContainer: {
    marginTop: spacing.md,
  },
  selectedTagsLabel: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    marginBottom: spacing.sm,
  },
  selectedTags: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.sm,
  },
  selectedTag: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(139, 92, 246, 0.3)',
    paddingLeft: spacing.md,
    paddingRight: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: borderRadius.full,
    gap: spacing.xs,
  },
  selectedTagText: {
    fontSize: fonts.sizes.sm,
    color: colors.text,
    fontWeight: '600',
  },

  // Info
  infoCard: {
    flexDirection: 'row',
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    padding: spacing.md,
    borderRadius: borderRadius.lg,
    gap: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
  },
  infoText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: colors.textSecondary,
    lineHeight: 20,
  },
});

