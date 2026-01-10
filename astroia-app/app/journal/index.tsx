import React, { useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Animated,
  Alert,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { useJournalStore, MOODS } from '@/stores/journalStore';
import { Empty } from '@/components/ui';
import { useRouter } from 'expo-router';
import haptics from '@/utils/haptics';
import { color, space, radius, type as typography, hitSlop as hitSlopTokens, shadow } from '@/theme/tokens';

// Type pour une entrée de journal
interface JournalEntry {
  id: string;
  mood: keyof typeof MOODS;
  note?: string;
  tags?: string[];
  moonPhase?: string;
  createdAt: string;
  updatedAt?: string;
}

export default function JournalScreen() {
  const router = useRouter();
  const { entries, isLoading, loadEntries, deleteEntry, getStats } = useJournalStore();
  
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    loadEntries();
    
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 500,
      useNativeDriver: true,
    }).start();
  }, []);

  const handleDelete = (id: string) => {
    haptics.light();
    Alert.alert(
      'Supprimer cette entrée ?',
      'Cette action est irréversible.',
      [
        { text: 'Annuler', style: 'cancel' },
        { 
          text: 'Supprimer', 
          style: 'destructive',
          onPress: () => {
            haptics.success();
            deleteEntry(id);
          }
        },
      ]
    );
  };

  const handleAddEntry = () => {
    haptics.medium();
    router.push('/journal/new' as any);
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffTime = Math.abs(now.getTime() - date.getTime());
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return "Aujourd'hui";
    if (diffDays === 1) return 'Hier';
    if (diffDays < 7) return `Il y a ${diffDays} jours`;
    
    return date.toLocaleDateString('fr-FR', { 
      day: 'numeric', 
      month: 'long',
      year: date.getFullYear() !== now.getFullYear() ? 'numeric' : undefined
    });
  };

  const stats = getStats();

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <StatusBar style="light" backgroundColor={color.bg} />
      
      <LinearGradient
        colors={[color.bg, color.surface]}
        style={styles.gradient}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 1 }}
      >
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity 
            onPress={() => {
              haptics.light();
              router.back();
            }} 
            style={styles.backButton}
            hitSlop={hitSlopTokens.md}
            accessibilityRole="button"
            accessibilityLabel="Retour"
          >
            <Ionicons name="arrow-back" size={24} color={color.text} />
          </TouchableOpacity>
          
          <Text style={styles.headerTitle}>📖 Mon Journal</Text>
          
          <TouchableOpacity 
            onPress={handleAddEntry} 
            style={styles.addButton}
            hitSlop={hitSlopTokens.md}
            accessibilityRole="button"
            accessibilityLabel="Ajouter une entrée"
            accessibilityHint="Créer une nouvelle entrée de journal"
          >
            <LinearGradient
              colors={[color.brand, color.brandHover]}
              style={styles.addGradient}
            >
              <Ionicons name="add" size={24} color="white" />
            </LinearGradient>
          </TouchableOpacity>
        </View>

        <Animated.ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
          style={{ opacity: fadeAnim }}
        >
          {/* Statistiques */}
          {stats && entries.length > 0 && (
            <View style={styles.statsCard}>
              <Text style={styles.statsTitle}>✨ Vos statistiques</Text>
              <View style={styles.statsRow}>
                <View style={styles.statItem}>
                  <Text style={styles.statValue}>{stats.totalEntries}</Text>
                  <Text style={styles.statLabel}>Entrées</Text>
                </View>
                <View style={styles.statItem}>
                  <Text style={styles.statValue}>
                    {MOODS[stats.mostFrequentMood as keyof typeof MOODS]?.emoji || '🌟'}
                  </Text>
                  <Text style={styles.statLabel}>Humeur dominante</Text>
                </View>
              </View>
            </View>
          )}

          {/* Liste des entrées */}
          {isLoading ? (
            <View style={styles.loadingContainer}>
              <Text style={styles.loadingText}>Chargement...</Text>
            </View>
          ) : entries.length === 0 ? (
            <Empty
              icon="book-outline"
              title="Aucune entrée pour l'instant"
              subtitle="Note ton humeur ou un événement marquant du jour."
              actionLabel="Ajouter une entrée"
              onActionPress={handleAddEntry}
            />
          ) : (
            <View style={styles.entriesContainer}>
              {entries.map((entry: JournalEntry, index: number) => (
                <EntryCard 
                  key={entry.id} 
                  entry={entry} 
                  onDelete={handleDelete}
                  formatDate={formatDate}
                  delay={index * 50}
                />
              ))}
            </View>
          )}
        </Animated.ScrollView>
      </LinearGradient>
    </SafeAreaView>
  );
}

interface EntryCardProps {
  entry: JournalEntry;
  onDelete: (id: string) => void;
  formatDate: (date: string) => string;
  delay: number;
}

function EntryCard({ entry, onDelete, formatDate, delay }: EntryCardProps) {
  const scaleAnim = useRef(new Animated.Value(0.9)).current;
  const opacityAnim = useRef(new Animated.Value(0)).current;
  
  const mood = MOODS[entry.mood] || MOODS.neutral;

  useEffect(() => {
    setTimeout(() => {
      Animated.parallel([
        Animated.spring(scaleAnim, {
          toValue: 1,
          tension: 50,
          friction: 7,
          useNativeDriver: true,
        }),
        Animated.timing(opacityAnim, {
          toValue: 1,
          duration: 400,
          useNativeDriver: true,
        }),
      ]).start();
    }, delay);
  }, []);

  return (
    <Animated.View 
      style={[
        styles.entryCard,
        { opacity: opacityAnim, transform: [{ scale: scaleAnim }] }
      ]}
      accessible={true}
      accessibilityRole="button"
      accessibilityLabel={`Entrée – ${mood.label} – ${formatDate(entry.createdAt)}`}
    >
      <View style={styles.entryHeader}>
        <View style={styles.entryMoodContainer}>
          <Text style={styles.entryMood} accessible={false}>{mood.emoji}</Text>
          <View>
            <Text style={styles.entryMoodLabel}>{mood.label}</Text>
            <Text style={styles.entryDate}>{formatDate(entry.createdAt)}</Text>
          </View>
        </View>
        <TouchableOpacity 
          onPress={() => onDelete(entry.id)}
          style={styles.deleteButton}
          hitSlop={hitSlopTokens.lg}
          accessibilityRole="button"
          accessibilityLabel="Supprimer cette entrée"
          accessibilityHint="Double tap pour confirmer la suppression"
        >
          <Ionicons name="trash-outline" size={20} color={color.danger} />
        </TouchableOpacity>
      </View>

      {entry.note && (
        <Text style={styles.entryNote} numberOfLines={3}>
          {entry.note}
        </Text>
      )}

      {entry.tags && entry.tags.length > 0 && (
        <View style={styles.tagsContainer}>
          {entry.tags.slice(0, 3).map((tag: string, tagIndex: number) => (
            <View key={tagIndex} style={styles.tag}>
              <Text style={styles.tagText}>{tag}</Text>
            </View>
          ))}
          {entry.tags.length > 3 && (
            <Text style={styles.moreTagsText}>+{entry.tags.length - 3}</Text>
          )}
        </View>
      )}

      {entry.moonPhase && (
        <View style={styles.moonPhaseContainer}>
          <Ionicons name="moon" size={14} color={color.brand} />
          <Text style={styles.moonPhaseText}>{entry.moonPhase}</Text>
        </View>
      )}
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: color.bg,
  },
  gradient: {
    flex: 1,
  },

  // Header
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: space.lg,
    paddingVertical: space.md,
    borderBottomWidth: 1,
    borderBottomColor: color.border,
  },
  backButton: {
    width: 40,
    height: 40,
    alignItems: 'center',
    justifyContent: 'center',
  },
  headerTitle: {
    ...typography.h2,
    color: color.text,
  },
  addButton: {
    width: 40,
    height: 40,
    backgroundColor: color.brandSoft, // Fond semi-transparent pour lisibilité
    borderRadius: radius.lg,
  },
  addGradient: {
    width: 40,
    height: 40,
    borderRadius: radius.lg,
    alignItems: 'center',
    justifyContent: 'center',
    ...shadow.md,
  },

  // Content
  scrollContent: {
    padding: space.lg,
    paddingBottom: space['3xl'],
  },

  // Stats
  statsCard: {
    backgroundColor: color.surfaceElevated,
    padding: space.xl,
    borderRadius: radius.lg,
    marginBottom: space.xl, // Augmenté de lg à xl (+4px) pour aérer
    borderWidth: 1,
    borderColor: color.border,
  },
  statsTitle: {
    ...typography.h3,
    color: color.text,
    marginBottom: space.md,
  },
  statsRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  statItem: {
    alignItems: 'center',
  },
  statValue: {
    ...typography.h1,
    color: color.brand,
    marginBottom: space.xs,
  },
  statLabel: {
    ...typography.bodySm,
    color: color.textMuted,
  },

  // Loading
  loadingContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: space['4xl'],
  },
  loadingText: {
    ...typography.bodySm,
    color: color.textMuted,
  },

  // Entries
  entriesContainer: {
    gap: space.md,
  },
  entryCard: {
    backgroundColor: color.surface,
    padding: space.lg,
    borderRadius: radius.lg + 2, // +2px pour adoucir les coins
    borderWidth: 1,
    borderColor: color.border,
  },
  entryHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: space.sm,
  },
  entryMoodContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.sm,
  },
  entryMood: {
    fontSize: 32,
  },
  entryMoodLabel: {
    ...typography.h4,
    color: color.text,
  },
  entryDate: {
    ...typography.caption,
    color: color.textMuted,
    marginTop: 2,
  },
  deleteButton: {
    padding: space.xs,
  },
  entryNote: {
    ...typography.body,
    color: color.textMuted,
    lineHeight: 22,
    marginBottom: space.sm,
  },
  tagsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: space.xs,
    marginTop: space.sm,
  },
  tag: {
    backgroundColor: color.brandSoft,
    paddingHorizontal: space.sm,
    paddingVertical: space.xs - 2,
    borderRadius: radius.sm,
  },
  tagText: {
    ...typography.caption,
    color: color.brand,
    fontWeight: '600',
  },
  moreTagsText: {
    ...typography.caption,
    color: color.textMuted,
    alignSelf: 'center',
  },
  moonPhaseContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.xs,
    marginTop: space.sm,
  },
  moonPhaseText: {
    ...typography.caption,
    color: color.brand,
    fontWeight: '600',
  },
});

