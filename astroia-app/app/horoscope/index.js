import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Animated,
  ActivityIndicator,
  SafeAreaView,
  Alert,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useProfileStore } from '@/stores/profileStore';
import { getDailyHoroscope, cleanOldCache } from '@/lib/api/horoscopeService';
import { SkeletonProfile, SkeletonCard } from '@/components/SkeletonLoader';
import { ErrorState } from '@/components/ErrorState';
import { useHapticFeedback } from '@/hooks/useHapticFeedback';
import THEME from '@/constants/theme';

const ZODIAC_EMOJIS = {
  'Bélier': '♈', 'Taureau': '♉', 'Gémeaux': '♊', 'Cancer': '♋',
  'Lion': '♌', 'Vierge': '♍', 'Balance': '♎', 'Scorpion': '♏',
  'Sagittaire': '♐', 'Capricorne': '♑', 'Verseau': '♒', 'Poissons': '♓',
};

export default function HoroscopeScreen() {
  const profile = useProfileStore((state) => state.profile);
  const [horoscope, setHoroscope] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Haptic feedback
  const haptic = useHapticFeedback();

  // Animations
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const slideAnim = useRef(new Animated.Value(50)).current;

  useEffect(() => {
    // Nettoyer le cache pour forcer le rechargement avec le bon signe
    AsyncStorage.getAllKeys().then(keys => {
      const horoscopeKeys = keys.filter(k => k.startsWith('horoscope_'));
      AsyncStorage.multiRemove(horoscopeKeys);
    });
    
    loadHoroscope();
    cleanOldCache(); // Nettoyer le cache ancien
  }, []);

  useEffect(() => {
    if (horoscope) {
      Animated.parallel([
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.spring(slideAnim, {
          toValue: 0,
          tension: 50,
          friction: 8,
          useNativeDriver: true,
        }),
      ]).start();
    }
  }, [horoscope]);

  const loadHoroscope = async () => {
    try {
      setLoading(true);
      setError(null);

      // Récupérer le signe depuis le profile
      const signName = profile?.sunSign?.name || useProfileStore.getState().getSunSign();
      console.log('[Horoscope] User sign:', signName, 'Profile:', profile);
      
      const signMapping = {
        'Bélier': 1, 'Taureau': 2, 'Gémeaux': 3, 'Cancer': 4,
        'Lion': 5, 'Vierge': 6, 'Balance': 7, 'Scorpion': 8,
        'Sagittaire': 9, 'Capricorne': 10, 'Verseau': 11, 'Poissons': 12,
      };
      
      const userSignId = signMapping[signName] || 1; // Bélier par défaut
      console.log('[Horoscope] Using sign ID:', userSignId);

      const data = await getDailyHoroscope(userSignId, profile);
      setHoroscope(data);
    } catch (err) {
      console.error('Load horoscope error:', err);
      setError('Impossible de charger l\'horoscope');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.wrapper}>
        <LinearGradient colors={['#FF6B9D', '#C239B3', '#4E54C8']} style={styles.container}>
          <SafeAreaView style={styles.safeArea}>
            <Stack.Screen
              options={{
                title: 'Horoscope du Jour',
                headerStyle: { backgroundColor: '#FF6B9D' },
                headerTintColor: '#fff',
                headerShadowVisible: false,
              }}
            />
            <View style={styles.header}>
              <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
                <Ionicons name="arrow-back" size={24} color="#fff" />
                <Text style={styles.backButtonText}>Retour au menu</Text>
              </TouchableOpacity>
            </View>
            <ScrollView contentContainerStyle={styles.scrollContent}>
              <Text style={styles.loadingText}>✨ Consultation des astres...</Text>
              <SkeletonProfile />
              <SkeletonCard />
              <SkeletonCard />
              <SkeletonCard />
            </ScrollView>
          </SafeAreaView>
        </LinearGradient>
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.wrapper}>
        <LinearGradient colors={['#FF6B9D', '#C239B3', '#4E54C8']} style={styles.container}>
          <SafeAreaView style={styles.safeArea}>
            <View style={styles.header}>
              <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
                <Ionicons name="arrow-back" size={24} color="#fff" />
                <Text style={styles.backButtonText}>Retour au menu</Text>
              </TouchableOpacity>
            </View>
            <ErrorState
              icon="partly-sunny-outline"
              title="Erreur de chargement"
              message={error}
              onRetry={() => {
                haptic.impact.light();
                loadHoroscope();
              }}
            />
          </SafeAreaView>
        </LinearGradient>
      </View>
    );
  }

  const today = new Date();
  const dateStr = today.toLocaleDateString('fr-FR', {
    weekday: 'long',
    day: 'numeric',
    month: 'long',
  });

  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={['#FF6B9D', '#C239B3', '#4E54C8']} style={styles.container}>
        <SafeAreaView style={styles.safeArea}>
          <Stack.Screen
            options={{
              title: 'Horoscope du Jour',
              headerStyle: { backgroundColor: '#FF6B9D' },
              headerTintColor: '#fff',
              headerShadowVisible: false,
            }}
          />

          {/* Bouton retour */}
          <View style={styles.header}>
            <TouchableOpacity
              style={styles.backButton}
              onPress={() => router.back()}
            >
              <Ionicons name="arrow-back" size={24} color="#fff" />
              <Text style={styles.backButtonText}>Retour au menu</Text>
            </TouchableOpacity>
          </View>

          <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
          <Animated.View style={{ opacity: fadeAnim, transform: [{ translateY: slideAnim }] }}>
            {/* Hero Card */}
            <View style={styles.heroCard}>
              <Text style={styles.heroDate}>{dateStr}</Text>
              <Text style={styles.heroEmoji}>
                {ZODIAC_EMOJIS[horoscope?.sign] || '✨'}
              </Text>
              <Text style={styles.heroSign}>{horoscope?.sign}</Text>
              <Text style={styles.heroSubtitle}>Votre horoscope du jour</Text>
            </View>

            {/* Section Travail */}
            <View style={styles.section}>
              <View style={styles.sectionHeader}>
                <Text style={styles.sectionIcon}>💼</Text>
                <Text style={styles.sectionTitle}>Travail & Carrière</Text>
              </View>
              <Text style={styles.sectionText}>{horoscope?.work}</Text>
            </View>

            {/* Section Amour */}
            <View style={styles.section}>
              <View style={styles.sectionHeader}>
                <Text style={styles.sectionIcon}>❤️</Text>
                <Text style={styles.sectionTitle}>Amour & Relations</Text>
              </View>
              <Text style={styles.sectionText}>{horoscope?.love}</Text>
            </View>

            {/* Section Santé */}
            <View style={styles.section}>
              <View style={styles.sectionHeader}>
                <Text style={styles.sectionIcon}>💪</Text>
                <Text style={styles.sectionTitle}>Santé & Bien-être</Text>
              </View>
              <Text style={styles.sectionText}>{horoscope?.health}</Text>
            </View>

            {/* Section Conseil */}
            <View style={styles.adviceCard}>
              <View style={styles.sectionHeader}>
                <Text style={styles.sectionIcon}>✨</Text>
                <Text style={styles.sectionTitle}>Conseil du jour</Text>
              </View>
              <Text style={styles.adviceText}>{horoscope?.advice}</Text>
            </View>

            {/* Infos cosmiques */}
            <View style={styles.cosmicInfo}>
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>🍀 Numéro chance :</Text>
                <Text style={styles.infoValue}>{horoscope?.luckyNumber}</Text>
              </View>
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>🌙 Lune en :</Text>
                <Text style={styles.infoValue}>{horoscope?.moonSign}</Text>
              </View>
            </View>

            {/* Footer */}
            <View style={styles.footer}>
              <Text style={styles.footerText}>
                Mis à jour : {new Date(horoscope?.generatedAt).toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' })}
              </Text>
              {horoscope?.isFallback && (
                <Text style={styles.fallbackNote}>Mode local (IA non disponible)</Text>
              )}
              <TouchableOpacity 
                onPress={() => {
                  haptic.impact.medium();
                  loadHoroscope();
                }} 
                style={styles.refreshButton}
              >
                <Ionicons name="refresh" size={18} color="rgba(255,255,255,0.7)" />
                <Text style={styles.refreshText}>Actualiser</Text>
              </TouchableOpacity>
            </View>
          </Animated.View>
        </ScrollView>
        </SafeAreaView>
      </LinearGradient>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
    backgroundColor: '#4E54C8', // Couleur du bas du dégradé
  },
  safeArea: {
    flex: 1,
  },
  container: {
    flex: 1,
  },
  header: {
    paddingHorizontal: 20,
    paddingTop: 10,
    paddingBottom: 5,
  },
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center', // Centrage vertical
    gap: 8,
    height: 44, // Hauteur fixe pour alignement parfait
    paddingHorizontal: 12,
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    borderRadius: 12,
    alignSelf: 'flex-start',
  },
  backButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  scrollContent: {
    padding: 20,
    paddingTop: 10,
    paddingBottom: 60,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    gap: 20,
  },
  loadingText: {
    fontSize: 18,
    color: '#fff',
    fontWeight: '600',
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 40,
  },
  errorText: {
    fontSize: 18,
    color: '#fff',
    textAlign: 'center',
    marginBottom: 20,
  },
  retryButton: {
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    paddingVertical: 14,
    paddingHorizontal: 30,
    borderRadius: 12,
  },
  retryButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  heroCard: {
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    borderRadius: 24,
    padding: 30,
    alignItems: 'center',
    marginBottom: 32, // Augmenté de 20 à 32 (+12px) pour marge Scorpion ↔ Travail
  },
  heroDate: {
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.8)',
    textTransform: 'capitalize',
    marginBottom: 15,
  },
  heroEmoji: {
    fontSize: 80,
    marginBottom: 10,
  },
  heroSign: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  heroSubtitle: {
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.7)',
  },
  section: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 16,
    padding: 20,
    marginBottom: 15,
  },
  sectionHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
    gap: 10,
  },
  sectionIcon: {
    fontSize: 24,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
  },
  sectionText: {
    fontSize: 15,
    color: 'rgba(255, 255, 255, 0.9)',
    lineHeight: 24, // Augmenté de 22 à 24 pour lisibilité
  },
  adviceCard: {
    backgroundColor: 'rgba(245, 158, 11, 0.2)',
    borderRadius: 16,
    padding: 20,
    marginBottom: 15,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
  },
  adviceText: {
    fontSize: 16,
    color: '#fff',
    lineHeight: 24,
    fontWeight: '500',
    fontStyle: 'italic',
  },
  cosmicInfo: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 15,
    gap: 10,
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  infoLabel: {
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.8)',
  },
  infoValue: {
    fontSize: 16,
    color: '#fff',
    fontWeight: 'bold',
  },
  footer: {
    alignItems: 'center',
    marginTop: 10,
    gap: 8,
  },
  footerText: {
    fontSize: 12,
    color: 'rgba(255, 255, 255, 0.6)',
  },
  fallbackNote: {
    fontSize: 11,
    color: 'rgba(245, 158, 11, 0.8)',
    fontStyle: 'italic',
  },
  refreshButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingVertical: 10,
    paddingHorizontal: 16,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 10,
    marginTop: 10,
  },
  refreshText: {
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.7)',
    fontWeight: '600',
  },
});
