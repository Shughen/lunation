/**
 * Profile Tab Screen
 * User information and settings
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Switch,
  Alert,
  Linking,
  Platform,
} from 'react-native';
import { router } from 'expo-router';
import { LinearGradient } from 'expo-linear-gradient';
import { useAuthStore } from '../../stores/useAuthStore';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { useNotificationsStore } from '../../stores/useNotificationsStore';
import { resetAllUserData } from '../../services/resetUserData';
import { useResetStore } from '../../stores/useResetStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { ZodiacBadge } from '../../components/icons/ZodiacIcon';
import { haptics } from '../../services/haptics';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors: bgColors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: bgColors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

// Helper to get sun sign from birth date
function getSunSign(birthDate: string | undefined): string {
  if (!birthDate) return 'Aries';

  const date = new Date(birthDate);
  const month = date.getMonth() + 1;
  const day = date.getDate();

  if ((month === 3 && day >= 21) || (month === 4 && day <= 19)) return 'Aries';
  if ((month === 4 && day >= 20) || (month === 5 && day <= 20)) return 'Taurus';
  if ((month === 5 && day >= 21) || (month === 6 && day <= 20)) return 'Gemini';
  if ((month === 6 && day >= 21) || (month === 7 && day <= 22)) return 'Cancer';
  if ((month === 7 && day >= 23) || (month === 8 && day <= 22)) return 'Leo';
  if ((month === 8 && day >= 23) || (month === 9 && day <= 22)) return 'Virgo';
  if ((month === 9 && day >= 23) || (month === 10 && day <= 22)) return 'Libra';
  if ((month === 10 && day >= 23) || (month === 11 && day <= 21)) return 'Scorpio';
  if ((month === 11 && day >= 22) || (month === 12 && day <= 21)) return 'Sagittarius';
  if ((month === 12 && day >= 22) || (month === 1 && day <= 19)) return 'Capricorn';
  if ((month === 1 && day >= 20) || (month === 2 && day <= 18)) return 'Aquarius';
  return 'Pisces';
}

export default function ProfileScreen() {
  const { user, logout } = useAuthStore();
  const profileData = useOnboardingStore((state) => state.profileData);
  const {
    notificationsEnabled,
    hydrated,
    loadPreferences,
    setNotificationsEnabled,
  } = useNotificationsStore();

  const [isTogglingNotifications, setIsTogglingNotifications] = useState(false);
  const { isResetting, setIsResetting } = useResetStore();

  useEffect(() => {
    if (!hydrated) {
      loadPreferences();
    }
  }, [hydrated, loadPreferences]);

  // Derive user data from auth store or onboarding profile
  const birthDateRaw = user?.birth_date || profileData?.birthDate;
  const birthDate = birthDateRaw ? (typeof birthDateRaw === 'string' ? birthDateRaw : birthDateRaw.toISOString()) : undefined;
  const birthTimeRaw = user?.birth_time || profileData?.birthTime;
  const birthTime = birthTimeRaw ? String(birthTimeRaw) : undefined;
  const birthPlace = user?.birth_place_name || profileData?.birthPlace;
  const sunSign = getSunSign(birthDate);

  const handleNotificationToggle = async (value: boolean) => {
    haptics.selection();
    setIsTogglingNotifications(true);

    try {
      const success = await setNotificationsEnabled(value);

      if (!success && value) {
        Alert.alert(
          'Permission requise',
          'Veuillez autoriser les notifications dans les parametres de votre appareil.',
          [
            { text: 'Annuler', style: 'cancel' },
            {
              text: 'Ouvrir Parametres',
              onPress: () => {
                if (Platform.OS === 'ios') {
                  Linking.openURL('app-settings:');
                } else {
                  Linking.openSettings();
                }
              },
            },
          ]
        );
      }
    } catch (error) {
      console.error('[Profile] Error toggling notifications:', error);
      Alert.alert('Erreur', 'Une erreur est survenue. Veuillez reessayer.');
    } finally {
      setIsTogglingNotifications(false);
    }
  };

  const handleLogout = () => {
    haptics.medium();
    Alert.alert('Deconnexion', 'Etes-vous sur de vouloir vous deconnecter ?', [
      { text: 'Annuler', style: 'cancel' },
      {
        text: 'Deconnexion',
        style: 'destructive',
        onPress: async () => {
          await logout();
          router.replace('/welcome');
        },
      },
    ]);
  };

  const handleResetUserData = () => {
    haptics.warning();
    Alert.alert(
      'Supprimer mes donnees locales',
      'Cette action va supprimer toutes vos donnees locales :\n\n' +
        '- Onboarding et profil\n' +
        '- Journal personnel\n' +
        '- Cache lunaire\n' +
        '- Preferences\n\n' +
        'Vous serez redirige vers l\'ecran d\'accueil.',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Supprimer',
          style: 'destructive',
          onPress: async () => {
            try {
              setIsResetting(true);
              await resetAllUserData();
              router.replace('/welcome');
              setTimeout(() => setIsResetting(false), 500);
            } catch (error) {
              console.error('[Profile] Reset error:', error);
              setIsResetting(false);
              Alert.alert('Erreur', 'Une erreur est survenue lors de la suppression.');
            }
          },
        },
      ]
    );
  };

  const formatBirthDate = (dateStr: string | undefined) => {
    if (!dateStr) return 'Non renseigne';
    try {
      return new Date(dateStr).toLocaleDateString('fr-FR', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
      });
    } catch {
      return dateStr;
    }
  };

  return (
    <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header with Avatar */}
        <View style={styles.header}>
          <Text style={styles.title}>Mon Profil</Text>
        </View>

        {/* Profile Card */}
        <View style={styles.profileCard}>
          <View style={styles.avatarSection}>
            <ZodiacBadge sign={sunSign} size={80} />
            <View style={styles.userInfo}>
              <Text style={styles.userName}>{user?.email?.split('@')[0] || 'Utilisateur'}</Text>
              <Text style={styles.userEmail}>{user?.email || ''}</Text>
            </View>
          </View>
        </View>

        {/* Birth Info Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Informations de naissance</Text>

          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Date de naissance</Text>
            <Text style={styles.infoValue}>{formatBirthDate(birthDate)}</Text>
          </View>

          {birthTime && (
            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Heure de naissance</Text>
              <Text style={styles.infoValue}>{birthTime}</Text>
            </View>
          )}

          {birthPlace && (
            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Lieu de naissance</Text>
              <Text style={styles.infoValue}>{birthPlace}</Text>
            </View>
          )}
        </View>

        {/* Notifications Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Notifications</Text>

          <View style={styles.settingRow}>
            <View style={styles.settingInfo}>
              <Text style={styles.settingLabel}>Activer les notifications</Text>
              <Text style={styles.settingDescription}>
                Rappels pour les fenetres VoC et nouveaux cycles lunaires
              </Text>
            </View>

            <Switch
              value={notificationsEnabled}
              onValueChange={handleNotificationToggle}
              disabled={isTogglingNotifications}
              trackColor={{ false: '#2D3561', true: colors.accent }}
              thumbColor={notificationsEnabled ? '#FFFFFF' : colors.textMuted}
              ios_backgroundColor="#2D3561"
            />
          </View>
        </View>

        {/* Actions Section */}
        <View style={styles.section}>
          <TouchableOpacity
            style={styles.logoutButton}
            onPress={handleLogout}
            disabled={isResetting}
          >
            <Text style={styles.logoutButtonText}>Deconnexion</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.resetButton, isResetting && styles.buttonDisabled]}
            onPress={handleResetUserData}
            disabled={isResetting}
          >
            <Text style={styles.resetButtonText}>
              {isResetting ? 'Suppression...' : 'Supprimer mes donnees locales'}
            </Text>
          </TouchableOpacity>
        </View>

        {/* Footer */}
        <View style={styles.footer}>
          <Text style={styles.footerText}>Lunation v2.0</Text>
          <Text style={styles.footerText}>Votre rituel lunaire quotidien</Text>
        </View>
      </ScrollView>
    </LinearGradientComponent>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: 100,
  },
  header: {
    alignItems: 'center',
    marginBottom: spacing.xl,
  },
  title: {
    ...fonts.h2,
    color: colors.text,
  },
  profileCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  avatarSection: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  userInfo: {
    marginLeft: spacing.lg,
    flex: 1,
  },
  userName: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  userEmail: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  section: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  sectionTitle: {
    ...fonts.body,
    color: colors.accent,
    fontWeight: '600',
    marginBottom: spacing.md,
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: spacing.sm,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(183, 148, 246, 0.1)',
  },
  infoLabel: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  infoValue: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '500',
  },
  settingRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  settingInfo: {
    flex: 1,
    marginRight: spacing.md,
  },
  settingLabel: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '500',
    marginBottom: spacing.xs,
  },
  settingDescription: {
    ...fonts.caption,
    color: colors.textMuted,
    lineHeight: 16,
  },
  logoutButton: {
    backgroundColor: colors.fire,
    padding: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginBottom: spacing.md,
  },
  logoutButtonText: {
    ...fonts.button,
    color: colors.text,
  },
  resetButton: {
    backgroundColor: 'transparent',
    borderWidth: 1,
    borderColor: colors.error,
    padding: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
  },
  buttonDisabled: {
    opacity: 0.5,
  },
  resetButtonText: {
    ...fonts.button,
    color: colors.error,
  },
  footer: {
    alignItems: 'center',
    paddingVertical: spacing.xl,
  },
  footerText: {
    ...fonts.caption,
    color: colors.textMuted,
    marginBottom: spacing.xs,
  },
});
