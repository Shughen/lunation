import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Animated } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { colors, fonts, spacing, borderRadius, shadows } from '@/constants/theme';
import { useProfileStore } from '@/stores/profileStore';
import { useEffect, useRef } from 'react';
import { useRouter } from 'expo-router';

export default function ProfileSummaryScreen() {
  const router = useRouter();
  const { profile, getZodiacSign } = useProfileStore();
  
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const slideAnim = useRef(new Animated.Value(30)).current;

  useEffect(() => {
    Animated.parallel([
      Animated.timing(fadeAnim, {
        toValue: 1,
        duration: 600,
        useNativeDriver: true,
      }),
      Animated.timing(slideAnim, {
        toValue: 0,
        duration: 500,
        useNativeDriver: true,
      }),
    ]).start();
  }, []);

  const zodiacSign = getZodiacSign();

  const formatDate = (date) => {
    if (!date) return '';
    return new Date(date).toLocaleDateString('fr-FR', { 
      weekday: 'long',
      day: 'numeric', 
      month: 'long', 
      year: 'numeric' 
    });
  };

  const formatTime = (time) => {
    if (!time) return '';
    return new Date(time).toLocaleTimeString('fr-FR', { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

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
            <Ionicons name="arrow-back" size={24} color={colors.text} />
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Récapitulatif</Text>
          <TouchableOpacity 
            onPress={() => router.push('/(tabs)/profile')} 
            style={styles.editButton}
          >
            <Ionicons name="create-outline" size={24} color={colors.accent} />
          </TouchableOpacity>
        </View>

        <Animated.ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
          style={{
            opacity: fadeAnim,
            transform: [{ translateY: slideAnim }],
          }}
        >
          {/* Hero Card */}
          <View style={styles.heroCard}>
            <LinearGradient
              colors={[colors.primary, colors.secondary]}
              style={styles.zodiacAvatar}
            >
              {zodiacSign && (
                <Text style={styles.zodiacEmoji}>{zodiacSign.emoji}</Text>
              )}
            </LinearGradient>
            <Text style={styles.heroName}>{profile.name}</Text>
            {zodiacSign && (
              <>
                <Text style={styles.heroZodiac}>{zodiacSign.sign}</Text>
                <View style={styles.elementBadge}>
                  <Text style={styles.elementText}>Élément : {zodiacSign.element}</Text>
                </View>
              </>
            )}
          </View>

          {/* Informations détaillées */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>📋 Informations de naissance</Text>
            
            <InfoRow 
              icon="calendar"
              label="Date de naissance"
              value={formatDate(profile.birthDate)}
            />
            <InfoRow 
              icon="time"
              label="Heure de naissance"
              value={formatTime(profile.birthTime)}
            />
            <InfoRow 
              icon="location"
              label="Lieu de naissance"
              value={profile.birthPlace}
            />
          </View>

          {/* Carte du thème natal (placeholder) */}
          <View style={styles.themeCard}>
            <View style={styles.themeHeader}>
              <Ionicons name="planet" size={32} color={colors.accent} />
              <Text style={styles.themeTitle}>Votre thème natal</Text>
            </View>
            <Text style={styles.themeSubtitle}>
              Basé sur votre {zodiacSign ? zodiacSign.sign : 'signe'} du {formatDate(profile.birthDate)}
            </Text>
            <View style={styles.themeContent}>
              <Text style={styles.themeText}>
                🌟 Votre carte du ciel personnalisée est prête à être analysée
              </Text>
            </View>
            <TouchableOpacity 
              style={styles.themeButton} 
              activeOpacity={0.8}
              onPress={() => router.push('/natal-chart')}
            >
              <LinearGradient
                colors={colors.ctaGradient}
                style={styles.themeButtonGradient}
              >
                <Text style={styles.themeButtonText}>Calculer mon thème complet</Text>
                <Ionicons name="arrow-forward" size={20} color="white" />
              </LinearGradient>
            </TouchableOpacity>
          </View>

          {/* Actions rapides */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>⚡ Actions rapides</Text>
            
            <QuickActionCard
              icon="chatbubbles"
              title="Consulter l'assistant IA"
              description="Posez vos questions astrologiques"
              color={colors.primary}
              onPress={() => router.push('/(tabs)/chat')}
            />
            <QuickActionCard
              icon="book"
              title="Mon journal d'humeur"
              description="Suivez vos émotions cosmiques"
              color={colors.accent}
              onPress={() => router.push('/journal')}
            />
          </View>
        </Animated.ScrollView>
      </SafeAreaView>
    </LinearGradient>
  );
}

function InfoRow({ icon, label, value }) {
  return (
    <View style={styles.infoRow}>
      <View style={styles.infoIcon}>
        <Ionicons name={icon} size={20} color={colors.accent} />
      </View>
      <View style={styles.infoContent}>
        <Text style={styles.infoLabel}>{label}</Text>
        <Text style={styles.infoValue}>{value}</Text>
      </View>
    </View>
  );
}

function QuickActionCard({ icon, title, description, color, onPress }) {
  return (
    <TouchableOpacity style={styles.actionCard} onPress={onPress} activeOpacity={0.7}>
      <View style={[styles.actionIcon, { backgroundColor: `${color}33` }]}>
        <Ionicons name={icon} size={24} color={color} />
      </View>
      <View style={styles.actionContent}>
        <Text style={styles.actionTitle}>{title}</Text>
        <Text style={styles.actionDescription}>{description}</Text>
      </View>
      <Ionicons name="chevron-forward" size={20} color={colors.textMuted} />
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
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
  editButton: {
    width: 40,
    height: 40,
    alignItems: 'center',
    justifyContent: 'center',
  },

  // Content
  scrollContent: {
    padding: spacing.md,
  },

  // Hero Card
  heroCard: {
    alignItems: 'center',
    backgroundColor: colors.cardBg,
    padding: spacing.xl,
    borderRadius: borderRadius.lg,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  zodiacAvatar: {
    width: 120,
    height: 120,
    borderRadius: borderRadius.full,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: spacing.md,
    ...shadows.lg,
  },
  zodiacEmoji: {
    fontSize: 64,
  },
  heroName: {
    fontSize: fonts.sizes.xxxl,
    color: colors.text,
    fontWeight: 'bold',
    marginBottom: spacing.xs,
  },
  heroZodiac: {
    fontSize: fonts.sizes.xl,
    color: colors.primary,
    fontWeight: '600',
    marginBottom: spacing.sm,
  },
  elementBadge: {
    backgroundColor: 'rgba(245, 158, 11, 0.2)',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.xs,
    borderRadius: borderRadius.full,
  },
  elementText: {
    fontSize: fonts.sizes.sm,
    color: colors.accent,
    fontWeight: '600',
  },

  // Section
  section: {
    marginBottom: spacing.lg,
  },
  sectionTitle: {
    fontSize: fonts.sizes.lg,
    color: colors.text,
    fontWeight: 'bold',
    marginBottom: spacing.md,
  },

  // Info Row
  infoRow: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.cardBg,
    padding: spacing.md,
    borderRadius: borderRadius.lg,
    marginBottom: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.2)',
    gap: spacing.md,
  },
  infoIcon: {
    width: 40,
    height: 40,
    borderRadius: borderRadius.md,
    backgroundColor: 'rgba(245, 158, 11, 0.15)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  infoContent: {
    flex: 1,
  },
  infoLabel: {
    fontSize: fonts.sizes.xs,
    color: colors.textMuted,
    marginBottom: spacing.xs - 2,
  },
  infoValue: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    fontWeight: '600',
  },

  // Theme Card
  themeCard: {
    backgroundColor: colors.cardBg,
    padding: spacing.lg,
    borderRadius: borderRadius.lg,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  themeHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    marginBottom: spacing.sm,
  },
  themeTitle: {
    fontSize: fonts.sizes.xl,
    color: colors.text,
    fontWeight: 'bold',
  },
  themeSubtitle: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    marginBottom: spacing.md,
  },
  themeContent: {
    backgroundColor: 'rgba(139, 92, 246, 0.1)',
    padding: spacing.md,
    borderRadius: borderRadius.md,
    marginBottom: spacing.md,
  },
  themeText: {
    fontSize: fonts.sizes.md,
    color: colors.textSecondary,
    lineHeight: 22,
  },
  themeButton: {
    borderRadius: borderRadius.xl,
    ...shadows.md,
  },
  themeButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    borderRadius: borderRadius.xl,
    gap: spacing.sm,
  },
  themeButtonText: {
    fontSize: fonts.sizes.md,
    color: 'white',
    fontWeight: 'bold',
  },

  // Action Cards
  actionCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.cardBg,
    padding: spacing.md,
    borderRadius: borderRadius.lg,
    marginBottom: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.2)',
    gap: spacing.md,
  },
  actionIcon: {
    width: 48,
    height: 48,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    justifyContent: 'center',
  },
  actionContent: {
    flex: 1,
  },
  actionTitle: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    fontWeight: '600',
    marginBottom: spacing.xs - 2,
  },
  actionDescription: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
  },
});

