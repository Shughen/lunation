import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Animated, Platform, TextInput, Alert, ActivityIndicator } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { colors, fonts, spacing, borderRadius, shadows } from '@/constants/theme';
import { useState, useEffect, useRef } from 'react';
import DateTimePicker from '@react-native-community/datetimepicker';
import { useProfileStore, validateProfile } from '@/stores/profileStore';
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'expo-router';
import { natalService } from '@/lib/api/natalService';
import { deleteAccount } from '@/lib/services/accountDeletionService';

export default function ProfileScreen() {
  const router = useRouter();
  const {
    profile,
    isLoading,
    hasProfile,
    loadProfile,
    saveProfile,
    updateField,
    getCompletionPercentage,
    getZodiacSign,
    resetProfile,
  } = useProfileStore();

  const [localProfile, setLocalProfile] = useState(profile);
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [showTimePicker, setShowTimePicker] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  const [isValidatingPlace, setIsValidatingPlace] = useState(false);
  const [placeValidated, setPlaceValidated] = useState(false);

  // Animation d'entrée
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    // Charger le profil au montage
    console.log('[Profile] Loading profile...');
    loadProfile();
    
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 500,
      useNativeDriver: true,
    }).start();
  }, []);

  // Synchroniser avec le store
  useEffect(() => {
    console.log('[Profile] Store updated:', profile);
    setLocalProfile(profile);
  }, [profile]);

  const handleDateChange = (event, selectedDate) => {
    setShowDatePicker(Platform.OS === 'ios');
    if (selectedDate) {
      // Créer une date locale sans conversion timezone
      const localDate = new Date(
        selectedDate.getFullYear(),
        selectedDate.getMonth(),
        selectedDate.getDate(),
        12, 0, 0 // Midi pour éviter les problèmes de timezone
      );
      console.log('[Profile] Date selected:', { original: selectedDate, local: localDate });
      setLocalProfile({ ...localProfile, birthDate: localDate });
      updateField('birthDate', localDate);
    }
  };

  const handleTimeChange = (event, selectedTime) => {
    setShowTimePicker(Platform.OS === 'ios');
    if (selectedTime) {
      // Créer une date avec l'heure choisie (peu importe la date)
      const localTime = new Date(
        2000, 0, 1, // Date arbitraire
        selectedTime.getHours(),
        selectedTime.getMinutes(),
        0
      );
      console.log('[Profile] Time selected:', { original: selectedTime, local: localTime });
      setLocalProfile({ ...localProfile, birthTime: localTime });
      updateField('birthTime', localTime);
    }
  };

  const handleValidatePlace = async () => {
    if (!localProfile.birthPlace || localProfile.birthPlace.trim().length < 3) {
      Alert.alert('Lieu requis', 'Entrez d\'abord votre lieu de naissance');
      return;
    }

    setIsValidatingPlace(true);

    try {
      // Géocoder le lieu
      const geoData = await natalService.geocodePlace(localProfile.birthPlace);
      
      // Obtenir le fuseau horaire
      const tzData = await natalService.getTimezone(geoData.lat, geoData.lon);

      // Mettre à jour le profil avec les coordonnées
      const updatedProfile = {
        ...localProfile,
        birthPlace: geoData.formatted,
        latitude: geoData.lat,
        longitude: geoData.lon,
        timezone: tzData.iana,
      };

      setLocalProfile(updatedProfile);
      updateField('latitude', geoData.lat);
      updateField('longitude', geoData.lon);
      updateField('timezone', tzData.iana);
      updateField('birthPlace', geoData.formatted);
      
      setPlaceValidated(true);

      Alert.alert(
        '✅ Lieu validé !',
        `${geoData.formatted}\nCoordonnées : ${geoData.lat.toFixed(4)}°N, ${geoData.lon.toFixed(4)}°E\nFuseau : ${tzData.iana}`,
        [{ text: 'OK' }]
      );
    } catch (error) {
      Alert.alert(
        'Lieu introuvable',
        'Essayez un format différent :\n- "Livry-Gargan, France"\n- "Paris, France"\n- "Lyon, France"',
        [{ text: 'OK' }]
      );
    } finally {
      setIsValidatingPlace(false);
    }
  };

  const handleSaveProfile = async () => {
    // Valider le profil
    const validation = validateProfile(localProfile);
    
    if (!validation.isValid) {
      const firstError = Object.values(validation.errors)[0];
      Alert.alert('Profil incomplet', firstError);
      return;
    }

    setIsSaving(true);
    const success = await saveProfile(localProfile);
    setIsSaving(false);

    if (success) {
      Alert.alert(
        '✨ Profil enregistré !',
        'Votre profil astral a été créé avec succès',
        [{ text: 'Super !' }]
      );
    } else {
      Alert.alert('Erreur', 'Impossible de sauvegarder le profil');
    }
  };
  const handleDeleteProfile = () => {
    Alert.alert(
      '⚠️ Supprimer mon profil',
      'Êtes-vous sûr de vouloir supprimer votre profil ? Cette action est irréversible et vous devrez recommencer le processus d\'onboarding.',
      [
        {
          text: 'Annuler',
          style: 'cancel',
        },
        {
          text: 'Supprimer',
          style: 'destructive',
          onPress: async () => {
            try {
              console.log('[Profile] Début suppression complète du profil...');
              
              // 1. Supprimer toutes les données du profil
              const success = await resetProfile();
              if (!success) {
                Alert.alert('Erreur', 'Impossible de supprimer le profil. Réessayez.');
                return;
              }
              
              console.log('[Profile] Profil supprimé, déconnexion en cours...');
              
              // 2. Attendre un peu pour que les suppressions Supabase se terminent
              await new Promise(resolve => setTimeout(resolve, 500));
              
              // 3. Déconnecter l'utilisateur (cela nettoie aussi le cache)
              const { signOut } = useAuthStore.getState();
              await signOut();
              
              console.log('[Profile] Utilisateur déconnecté, redirection...');
              
              // 4. Nettoyer aussi AsyncStorage des données onboarding
              const AsyncStorage = (await import('@react-native-async-storage/async-storage')).default;
              await AsyncStorage.multiRemove([
                '@onboarding_completed',
                'onboarding_intro_seen',
                '@profile_migrated_to_supabase',
                'natal_chart_local',
                '@astroia_user_profile',
              ]);
              
              // 5. Afficher message de succès puis rediriger
              Alert.alert(
                '✅ Profil supprimé',
                'Votre profil a été complètement supprimé. Vous allez être redirigé vers la page de connexion.',
                [
                  {
                    text: 'OK',
                    onPress: () => {
                      router.replace('/(auth)/login');
                    },
                  },
                ]
              );
            } catch (error) {
              console.error('[Profile] Erreur suppression profil:', error);
              Alert.alert('Erreur', 'Une erreur est survenue lors de la suppression.');
            }
          },
        },
      ],
      { cancelable: true }
    );
  };



  const handleDeleteAccount = () => {
    Alert.alert(
      '⚠️ Supprimer mon compte',
      'Cette action est IRRÉVERSIBLE. Toutes tes données seront définitivement supprimées.\n\nÊtes-vous absolument sûre ?',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Supprimer définitivement',
          style: 'destructive',
          onPress: confirmDeleteAccount,
        },
      ]
    );
  };

  const confirmDeleteAccount = () => {
    Alert.alert(
      'Confirmation finale',
      'Tape "SUPPRIMER" pour confirmer',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Continuer',
          onPress: async () => {
            try {
              console.log('[Profile] Début suppression compte...');
              const { success, errors } = await deleteAccount();
              
              if (success) {
                Alert.alert(
                  '✅ Compte supprimé',
                  'Toutes tes données ont été supprimées avec succès.',
                  [
                    { text: 'OK', onPress: () => router.replace('/(auth)/login') },
                  ]
                );
              } else {
                // Afficher les erreurs mais confirmer la suppression locale
                const errorMsg = errors.length > 0 
                  ? `Certaines données n'ont pas pu être supprimées :\n${errors.join('\n')}\n\nLes données locales ont été supprimées et tu as été déconnecté.`
                  : 'Les données locales ont été supprimées et tu as été déconnecté.';
                
                Alert.alert(
                  '⚠️ Suppression partielle',
                  errorMsg,
                  [
                    { text: 'OK', onPress: () => router.replace('/(auth)/login') },
                  ]
                );
              }
            } catch (error) {
              console.error('[Profile] Delete account error:', error);
              Alert.alert(
                'Erreur',
                `Impossible de supprimer complètement le compte : ${error.message}\n\nLes données locales ont été nettoyées et tu as été déconnecté.`,
                [
                  { text: 'OK', onPress: () => router.replace('/(auth)/login') },
                ]
              );
            }
          },
        },
      ]
    );
  };

  const formatDate = (date) => {
    if (!date) return 'Non renseignée';
    return new Date(date).toLocaleDateString('fr-FR', { 
      day: '2-digit', 
      month: 'long', 
      year: 'numeric' 
    });
  };

  const formatTime = (time) => {
    if (!time) return 'Non renseignée';
    return new Date(time).toLocaleTimeString('fr-FR', { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  const completionPercentage = getCompletionPercentage();
  const zodiacSign = getZodiacSign();

  // Debug log
  console.log('[DEBUG Profile] hasProfile:', hasProfile, 'profile:', {
    name: localProfile?.name,
    birthDate: localProfile?.birthDate,
    birthTime: localProfile?.birthTime,
    birthPlace: localProfile?.birthPlace,
    sunSign: localProfile?.sunSign?.name,
    moonSign: localProfile?.moonSign?.name,
    ascendant: localProfile?.ascendant?.name,
  });

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea} edges={['bottom']}>
        <Animated.ScrollView 
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
          style={{ opacity: fadeAnim }}
        >
          {/* Avatar & Nom */}
          <View style={styles.profileHeader}>
            <View style={styles.avatarContainer}>
              <LinearGradient
                colors={[colors.primary, colors.secondary]}
                style={styles.avatar}
              >
                {zodiacSign ? (
                  <Text style={styles.zodiacEmoji}>{zodiacSign.emoji}</Text>
                ) : (
                  <Ionicons name="person" size={48} color="white" />
                )}
              </LinearGradient>
            </View>
            <Text style={styles.profileName}>
              {localProfile.name || 'Votre profil'}
            </Text>
            {zodiacSign && (
              <View style={styles.zodiacBadge}>
                <Text style={styles.zodiacText}>
                  {zodiacSign.sign} • {zodiacSign.element}
                </Text>
              </View>
            )}
            <Text style={styles.profileSubtitle}>
              {hasProfile ? '✨ Profil complet' : '⚠️ Profil à compléter'}
            </Text>
            {!hasProfile && (
              <View style={styles.incompleteWarning}>
                <Ionicons name="information-circle" size={16} color={colors.warning} />
                <Text style={styles.incompleteWarningText}>
                  Complétez votre profil pour accéder à toutes les fonctionnalités astrales
                </Text>
              </View>
            )}
          </View>

          {/* Bouton Voir le récapitulatif (si profil complet) */}
          {hasProfile && (
            <TouchableOpacity 
              style={styles.summaryButton}
              activeOpacity={0.8}
              onPress={() => router.push('/profile/summary')}
            >
              <View style={styles.summaryButtonContent}>
                <View style={styles.summaryIcon}>
                  <Ionicons name="eye" size={20} color={colors.accent} />
                </View>
                <Text style={styles.summaryButtonText}>Voir mon profil complet</Text>
                <Ionicons name="arrow-forward" size={20} color={colors.accent} />
              </View>
            </TouchableOpacity>
          )}

          {/* Bouton Supprimer mon compte */}
          <TouchableOpacity 
            style={styles.deleteAccountButton}
            activeOpacity={0.8}
            onPress={handleDeleteAccount}
          >
            <View style={styles.deleteAccountButtonContent}>
              <View style={styles.deleteAccountIconContainer}>
                <Ionicons name="trash-outline" size={20} color="#EF4444" />
              </View>
              <Text style={styles.deleteAccountButtonText}>Supprimer mon compte</Text>
              <Ionicons name="warning-outline" size={18} color="#EF4444" />
            </View>
          </TouchableOpacity>

          {/* Bouton Settings */}
          <TouchableOpacity 
            style={styles.settingsButton}
            activeOpacity={0.8}
            onPress={() => router.push('/settings')}
          >
            <View style={styles.settingsButtonContent}>
              <Ionicons name="settings-outline" size={20} color="rgba(255,255,255,0.8)" />
              <Text style={styles.settingsButtonText}>Paramètres</Text>
              <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.5)" />
            </View>
          </TouchableOpacity>

          {/* Bouton Supprimer mon profil */}
          {hasProfile && (
            <TouchableOpacity 
              style={styles.deleteButton}
              activeOpacity={0.8}
              onPress={handleDeleteProfile}
            >
              <View style={styles.deleteButtonContent}>
                <Ionicons name="trash-outline" size={20} color="#EF4444" />
                <Text style={styles.deleteButtonText}>Supprimer mon profil</Text>
              </View>
            </TouchableOpacity>
          )}

          {/* Bouton Créer/Enregistrer mon profil */}
          <TouchableOpacity 
            style={styles.createProfileButton}
            activeOpacity={0.8}
            onPress={handleSaveProfile}
            disabled={isSaving}
          >
            <LinearGradient
              colors={colors.ctaGradient}
              style={styles.buttonGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Ionicons 
                name={hasProfile ? "save" : "flash"} 
                size={24} 
                color="white" 
              />
              <Text style={styles.buttonText}>
                {isSaving 
                  ? 'Enregistrement...' 
                  : hasProfile 
                    ? 'Mettre à jour mon profil' 
                    : 'Enregistrer mon profil'}
              </Text>
            </LinearGradient>
          </TouchableOpacity>

          {/* Informations à remplir */}
          <View style={styles.infoSection}>
            <Text style={styles.sectionTitle}>Informations nécessaires</Text>
            
            {/* Nom */}
            <View style={styles.infoCard}>
              <View style={[styles.infoIcon, localProfile.name && styles.infoIconComplete]}>
                <Ionicons 
                  name="person-outline" 
                  size={24} 
                  color={localProfile.name ? colors.accent : colors.textMuted} 
                />
              </View>
              <View style={styles.infoContent}>
                <Text style={styles.infoTitle}>Nom / Prénom</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Votre nom"
                  placeholderTextColor={colors.textMuted}
                  value={localProfile.name}
                  onChangeText={(text) => {
                    setLocalProfile({ ...localProfile, name: text });
                    updateField('name', text);
                  }}
                />
              </View>
            </View>

            {/* Date de naissance */}
            <TouchableOpacity 
              style={styles.infoCard}
              activeOpacity={0.7}
              onPress={() => setShowDatePicker(true)}
            >
              <View style={[styles.infoIcon, localProfile.birthDate && styles.infoIconComplete]}>
                <Ionicons 
                  name="calendar-outline" 
                  size={24} 
                  color={localProfile.birthDate ? colors.accent : colors.textMuted} 
                />
              </View>
              <View style={styles.infoContent}>
                <Text style={styles.infoTitle}>Date de naissance</Text>
                <Text style={[
                  styles.infoDescription, 
                  !localProfile.birthDate && styles.infoDescriptionIncomplete
                ]}>
                  {formatDate(localProfile.birthDate)}
                </Text>
              </View>
              <Ionicons name="create-outline" size={20} color={colors.accent} />
            </TouchableOpacity>

            {/* Heure de naissance */}
            <TouchableOpacity 
              style={styles.infoCard}
              activeOpacity={0.7}
              onPress={() => setShowTimePicker(true)}
            >
              <View style={[styles.infoIcon, localProfile.birthTime && styles.infoIconComplete]}>
                <Ionicons 
                  name="time-outline" 
                  size={24} 
                  color={localProfile.birthTime ? colors.accent : colors.textMuted} 
                />
              </View>
              <View style={styles.infoContent}>
                <Text style={styles.infoTitle}>Heure de naissance</Text>
                <Text style={[
                  styles.infoDescription,
                  !localProfile.birthTime && styles.infoDescriptionIncomplete
                ]}>
                  {formatTime(localProfile.birthTime)}
                </Text>
              </View>
              <Ionicons name="create-outline" size={20} color={colors.accent} />
            </TouchableOpacity>

            {/* Lieu de naissance */}
            <View style={styles.infoCard}>
              <View style={[styles.infoIcon, placeValidated && styles.infoIconComplete]}>
                <Ionicons 
                  name="location-outline" 
                  size={24} 
                  color={placeValidated ? colors.accent : colors.textMuted} 
                />
              </View>
              <View style={styles.infoContent}>
                <Text style={styles.infoTitle}>Lieu de naissance</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: Paris, France"
                  placeholderTextColor={colors.textMuted}
                  value={localProfile.birthPlace}
                  onChangeText={(text) => {
                    setLocalProfile({ ...localProfile, birthPlace: text });
                    updateField('birthPlace', text);
                    setPlaceValidated(false);
                  }}
                />
                {placeValidated && (
                  <Text style={styles.validatedText}>
                    ✅ Validé ({localProfile.latitude?.toFixed(2)}°N, {localProfile.longitude?.toFixed(2)}°E)
                  </Text>
                )}
              </View>
              <TouchableOpacity 
                onPress={handleValidatePlace}
                disabled={isValidatingPlace}
                style={styles.validateButton}
              >
                {isValidatingPlace ? (
                  <ActivityIndicator size="small" color={colors.accent} />
                ) : (
                  <Ionicons 
                    name={placeValidated ? "checkmark-circle" : "search"} 
                    size={24} 
                    color={placeValidated ? colors.accent : colors.textMuted} 
                  />
                )}
              </TouchableOpacity>
            </View>
          </View>

          {/* Pickers iOS/Android */}
          {showDatePicker && (
            <DateTimePicker
              value={localProfile.birthDate || new Date()}
              mode="date"
              display={Platform.OS === 'ios' ? 'spinner' : 'default'}
              onChange={handleDateChange}
              maximumDate={new Date()}
              minimumDate={new Date(1900, 0, 1)}
              themeVariant="dark"
            />
          )}

          {showTimePicker && (
            <DateTimePicker
              value={localProfile.birthTime || new Date()}
              mode="time"
              display={Platform.OS === 'ios' ? 'spinner' : 'default'}
              onChange={handleTimeChange}
              themeVariant="dark"
            />
          )}

          {/* Message explicatif */}
          <View style={styles.explanationCard}>
            <Ionicons name="information-circle" size={28} color={colors.primary} />
            <Text style={styles.explanationText}>
              Ces informations sont nécessaires pour calculer votre thème natal avec précision et vous fournir des prédictions personnalisées basées sur votre carte du ciel.
            </Text>
          </View>

          {/* Progression */}
          <View style={styles.progressContainer}>
            <View style={styles.progressBar}>
              <Animated.View 
                style={[
                  styles.progressFill, 
                  { width: `${completionPercentage}%` }
                ]} 
              />
            </View>
            <Text style={styles.progressText}>
              {completionPercentage}% complété
            </Text>
          </View>
        </Animated.ScrollView>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  scrollContent: {
    paddingHorizontal: spacing.md,
    paddingBottom: spacing.xl,
  },
  loadingContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  loadingText: {
    fontSize: fonts.sizes.md,
    color: colors.textMuted,
  },

  // Profile Header
  profileHeader: {
    alignItems: 'center',
    paddingVertical: spacing.xl,
  },
  avatarContainer: {
    marginBottom: spacing.md,
  },
  avatar: {
    width: 100,
    height: 100,
    borderRadius: borderRadius.full,
    alignItems: 'center',
    justifyContent: 'center',
    ...shadows.lg,
  },
  zodiacEmoji: {
    fontSize: 48,
  },
  profileName: {
    fontSize: fonts.sizes.xxl,
    color: colors.text,
    fontWeight: 'bold',
    marginTop: spacing.sm,
  },
  zodiacBadge: {
    backgroundColor: 'rgba(139, 92, 246, 0.2)',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.xs,
    borderRadius: borderRadius.full,
    marginTop: spacing.xs,
  },
  zodiacText: {
    fontSize: fonts.sizes.sm,
    color: colors.primary,
    fontWeight: '600',
  },
  profileSubtitle: {
    fontSize: fonts.sizes.md,
    color: colors.textMuted,
    marginTop: spacing.xs,
  },
  incompleteWarning: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(245, 158, 11, 0.15)',
    padding: spacing.sm,
    borderRadius: borderRadius.md,
    marginTop: spacing.sm,
    gap: spacing.xs,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
  },
  incompleteWarningText: {
    flex: 1,
    fontSize: fonts.sizes.xs,
    color: colors.warning || '#F59E0B',
    lineHeight: 16,
  },

  // Summary Button
  summaryButton: {
    marginTop: spacing.lg,
    marginBottom: spacing.sm,
  },
  summaryButtonContent: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: colors.cardBg,
    padding: spacing.md,
    borderRadius: borderRadius.lg,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.5)',
    gap: spacing.sm,
  },
  summaryIcon: {
    width: 32,
    height: 32,
    borderRadius: borderRadius.full,
    backgroundColor: 'rgba(245, 158, 11, 0.15)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  summaryButtonText: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: colors.text,
    fontWeight: '600',
  },

  // Create Profile Button
  createProfileButton: {
    marginVertical: spacing.lg,
    borderRadius: borderRadius.xl,
    ...shadows.lg,
  },
  buttonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    paddingHorizontal: spacing.lg,
    borderRadius: borderRadius.xl,
    gap: spacing.sm,
  },
  buttonText: {
    fontSize: fonts.sizes.lg,
    color: 'white',
    fontWeight: 'bold',
  },

  // Info Section
  infoSection: {
    marginTop: spacing.lg,
  },
  sectionTitle: {
    fontSize: fonts.sizes.lg,
    color: colors.text,
    fontWeight: 'bold',
    marginBottom: spacing.md,
  },
  infoCard: {
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
    width: 48,
    height: 48,
    borderRadius: borderRadius.md,
    backgroundColor: 'rgba(148, 163, 184, 0.15)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  infoIconComplete: {
    backgroundColor: 'rgba(245, 158, 11, 0.15)',
  },
  infoContent: {
    flex: 1,
  },
  infoTitle: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  infoDescription: {
    fontSize: fonts.sizes.sm,
    color: colors.textSecondary,
  },
  infoDescriptionIncomplete: {
    color: colors.textMuted,
    fontStyle: 'italic',
  },
  input: {
    fontSize: fonts.sizes.sm,
    color: colors.text,
    paddingVertical: spacing.xs,
  },
  validatedText: {
    fontSize: fonts.sizes.xs,
    color: colors.accent,
    marginTop: spacing.xs - 2,
  },
  validateButton: {
    padding: spacing.xs,
  },

  // Explanation
  explanationCard: {
    backgroundColor: 'rgba(139, 92, 246, 0.1)',
    padding: spacing.md,
    borderRadius: borderRadius.lg,
    marginTop: spacing.xl,
    flexDirection: 'row',
    gap: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  // Delete Account Button (danger style)
  deleteAccountButton: {
    marginTop: spacing.md,
    marginBottom: spacing.sm,
  },
  deleteAccountButtonContent: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    borderRadius: borderRadius.md,
    borderWidth: 1,
    borderColor: 'rgba(239, 68, 68, 0.3)',
  },
  deleteAccountIconContainer: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: 'rgba(239, 68, 68, 0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  deleteAccountButtonText: {
    fontSize: fonts.sizes.md,
    color: '#EF4444',
    fontWeight: '500',
    flex: 1,
    marginLeft: spacing.sm,
  },
  settingsButton: {
    marginTop: spacing.md,
    marginBottom: spacing.sm,
  },
  settingsButtonContent: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    borderRadius: borderRadius.md,
  },
  settingsButtonText: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255,255,255,0.8)',
    fontWeight: '500',
    flex: 1,
    marginLeft: spacing.sm,
  },
  explanationText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: colors.textSecondary,
    lineHeight: 20,
  },

  // Progress
  progressContainer: {
    marginTop: spacing.lg,
    alignItems: 'center',
  },
  progressBar: {
    width: '100%',
    height: 8,
    backgroundColor: 'rgba(148, 163, 184, 0.2)',
    borderRadius: borderRadius.full,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: colors.accent,
    borderRadius: borderRadius.full,
  },
  progressText: {
    fontSize: fonts.sizes.sm,
    color: colors.textSecondary,
    marginTop: spacing.sm,
    fontWeight: '600',
  },

  // Delete Button
  deleteButton: {
    marginTop: spacing.md,
    marginBottom: spacing.sm,
  },
  deleteButtonContent: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    borderRadius: borderRadius.md,
    borderWidth: 1,
    borderColor: 'rgba(239, 68, 68, 0.3)',
    gap: spacing.sm,
  },
  deleteButtonText: {
    fontSize: fonts.sizes.md,
    color: '#EF4444',
    fontWeight: '600',
  },
});
