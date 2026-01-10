import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Alert,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router } from 'expo-router';
import { useProfileStore } from '@/stores/profileStore';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

export default function SettingsScreen() {
  const { profile, clearProfile } = useProfileStore();

  const handleLogout = async () => {
    Alert.alert(
      'Déconnexion',
      'Êtes-vous sûr de vouloir vous déconnecter ?',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Déconnexion',
          style: 'destructive',
          onPress: async () => {
            await clearProfile();
            await AsyncStorage.clear();
            router.replace('/(auth)/login');
          },
        },
      ]
    );
  };

  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea}>
          <Stack.Screen
            options={{
              title: 'Paramètres',
              headerStyle: { backgroundColor: '#0F172A' },
              headerTintColor: '#fff',
              headerShadowVisible: false,
            }}
          />

          {/* Header */}
          <View style={styles.header}>
            <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
              <Ionicons name="arrow-back" size={24} color="#fff" />
              <Text style={styles.backButtonText}>Retour</Text>
            </TouchableOpacity>
          </View>

          <ScrollView
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
          >
            {/* Title */}
            <View style={styles.titleSection}>
              <Text style={styles.mainTitle}>⚙️ Paramètres</Text>
              <Text style={styles.subtitle}>Gérez votre expérience LUNA</Text>
            </View>

            {/* Profil Section */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Profil</Text>
              
              <SettingsItem
                icon="person-outline"
                label="Mon profil astral"
                value={profile?.name || 'Non configuré'}
                onPress={() => router.push('/(tabs)/profile')}
              />
              
              <SettingsItem
                icon="calendar-outline"
                label="Configuration cycle"
                value="Gérer mon cycle"
                onPress={() => router.push('/settings/cycle')}
              />
            </View>

            {/* Notifications Section */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Notifications</Text>
              
              <SettingsItem
                icon="notifications-outline"
                label="Rappels et alertes"
                value="Gérer"
                onPress={() => router.push('/settings/notifications')}
              />
            </View>

            {/* Confidentialité Section */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Confidentialité & Données</Text>
              
              <SettingsItem
                icon="shield-checkmark-outline"
                label="Politique de confidentialité"
                onPress={() => router.push('/settings/privacy')}
              />
              
              <SettingsItem
                icon="download-outline"
                label="Exporter mes données"
                onPress={() => router.push('/settings/privacy')}
              />
              
              <SettingsItem
                icon="trash-outline"
                label="Supprimer mon compte"
                iconColor="#EF4444"
                onPress={() => router.push('/settings/privacy')}
              />
            </View>

            {/* À propos Section */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>À propos</Text>
              
              <SettingsItem
                icon="information-circle-outline"
                label="À propos de LUNA"
                onPress={() => router.push('/settings/about')}
              />
              
              <SettingsItem
                icon="document-text-outline"
                label="Disclaimer médical"
                onPress={() => router.push('/settings/about')}
              />
              
              <SettingsItem
                icon="code-outline"
                label="Version"
                value="2.0.0"
              />
            </View>

            {/* Logout */}
            <TouchableOpacity style={styles.logoutButton} onPress={handleLogout}>
              <Ionicons name="log-out-outline" size={20} color="#EF4444" />
              <Text style={styles.logoutText}>Déconnexion</Text>
            </TouchableOpacity>

            {/* Footer branding */}
            <View style={styles.branding}>
              <Text style={styles.brandingEmoji}>🌙</Text>
              <Text style={styles.brandingText}>LUNA - Cycle & Cosmos</Text>
              <Text style={styles.brandingSubtext}>Suis ton cycle, écoute les étoiles</Text>
            </View>
          </ScrollView>
        </SafeAreaView>
      </LinearGradient>
    </View>
  );
}

// Composant pour un item de settings
function SettingsItem({ icon, label, value, onPress, iconColor = '#FFB6C1' }) {
  return (
    <TouchableOpacity
      style={styles.settingsItem}
      onPress={onPress}
      activeOpacity={0.7}
      disabled={!onPress}
    >
      <View style={styles.settingsItemLeft}>
        <View style={[styles.settingsIconContainer, { backgroundColor: `${iconColor}20` }]}>
          <Ionicons name={icon} size={20} color={iconColor} />
        </View>
        <Text style={styles.settingsLabel}>{label}</Text>
      </View>
      
      <View style={styles.settingsItemRight}>
        {value && <Text style={styles.settingsValue}>{value}</Text>}
        {onPress && <Ionicons name="chevron-forward" size={20} color="rgba(255,255,255,0.4)" />}
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  header: {
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: borderRadius.md,
    alignSelf: 'flex-start',
  },
  backButtonText: {
    color: '#fff',
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  scrollContent: {
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.xxl,
  },
  titleSection: {
    marginBottom: spacing.xl,
  },
  mainTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: spacing.xs,
  },
  subtitle: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255,255,255,0.7)',
  },
  section: {
    marginBottom: spacing.xl,
  },
  sectionTitle: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: spacing.md,
    textTransform: 'uppercase',
    letterSpacing: 1,
  },
  settingsItem: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
  },
  settingsItemLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
    flex: 1,
  },
  settingsIconContainer: {
    width: 36,
    height: 36,
    borderRadius: 18,
    justifyContent: 'center',
    alignItems: 'center',
  },
  settingsLabel: {
    fontSize: fonts.sizes.md,
    color: '#fff',
    fontWeight: '500',
    flex: 1,
  },
  settingsItemRight: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
  },
  settingsValue: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255,255,255,0.6)',
  },
  logoutButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: spacing.sm,
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    marginTop: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(239, 68, 68, 0.3)',
  },
  logoutText: {
    fontSize: fonts.sizes.md,
    color: '#EF4444',
    fontWeight: '600',
  },
  branding: {
    alignItems: 'center',
    marginTop: spacing.xxl,
    paddingVertical: spacing.xl,
  },
  brandingEmoji: {
    fontSize: 40,
    marginBottom: spacing.sm,
  },
  brandingText: {
    fontSize: fonts.sizes.lg,
    color: '#FFC8DD',
    fontWeight: 'bold',
    marginBottom: spacing.xs,
  },
  brandingSubtext: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255,255,255,0.6)',
    fontStyle: 'italic',
  },
});
