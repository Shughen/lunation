import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Linking,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

const APP_VERSION = '2.0.0';

export default function AboutScreen() {
  const handleOpenDisclaimer = () => {
    router.push('/settings/disclaimer');
  };

  const handleOpenPolicy = () => {
    router.push('/settings/data-policy');
  };

  const handleContactSupport = () => {
    Linking.openURL('mailto:support@luna-app.fr?subject=Support LUNA');
  };

  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea}>
          <Stack.Screen
            options={{
              title: 'À propos',
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

          <ScrollView contentContainerStyle={styles.scrollContent}>
            {/* Logo & branding */}
            <View style={styles.logoSection}>
              <Text style={styles.logoEmoji}>🌙</Text>
              <Text style={styles.logoText}>LUNA</Text>
              <Text style={styles.logoSubtext}>Cycle & Cosmos</Text>
              <Text style={styles.version}>Version {APP_VERSION}</Text>
            </View>

            {/* Mission */}
            <View style={styles.missionCard}>
              <Text style={styles.missionTitle}>Notre Mission</Text>
              <Text style={styles.missionText}>
                LUNA t'aide à mieux comprendre ton corps et ton énergie en reliant ton cycle menstruel aux cycles lunaires et astrologiques.
                {'\n\n'}
                Nous croyons que chaque femme mérite de se connaître profondément, d'honorer ses cycles naturels et de vivre en harmonie avec son énergie.
              </Text>
            </View>

            {/* Legal */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Informations légales</Text>
              
              <TouchableOpacity style={styles.legalItem} onPress={handleOpenDisclaimer}>
                <Ionicons name="medical-outline" size={20} color="#F59E0B" />
                <Text style={styles.legalLabel}>Disclaimer médical</Text>
                <Ionicons name="chevron-forward" size={20} color="rgba(255,255,255,0.4)" />
              </TouchableOpacity>

              <TouchableOpacity style={styles.legalItem} onPress={handleOpenPolicy}>
                <Ionicons name="shield-checkmark-outline" size={20} color="#10B981" />
                <Text style={styles.legalLabel}>Politique de confidentialité (RGPD)</Text>
                <Ionicons name="chevron-forward" size={20} color="rgba(255,255,255,0.4)" />
              </TouchableOpacity>
            </View>

            {/* Crédits */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Crédits</Text>
              
              <View style={styles.creditItem}>
                <Text style={styles.creditLabel}>Développé par</Text>
                <Text style={styles.creditValue}>Rémi Beaurain</Text>
              </View>

              <View style={styles.creditItem}>
                <Text style={styles.creditLabel}>Technologies</Text>
                <Text style={styles.creditValue}>React Native • Expo • Supabase</Text>
              </View>

              <View style={styles.creditItem}>
                <Text style={styles.creditLabel}>IA</Text>
                <Text style={styles.creditValue}>OpenAI GPT-3.5-turbo</Text>
              </View>
            </View>

            {/* Contact */}
            <TouchableOpacity style={styles.contactButton} onPress={handleContactSupport}>
              <Ionicons name="mail-outline" size={20} color="#FFB6C1" />
              <Text style={styles.contactText}>Contacter le support</Text>
            </TouchableOpacity>

            {/* Footer */}
            <View style={styles.footer}>
              <Text style={styles.footerText}>
                Développé avec 💜 et beaucoup de 🌙
              </Text>
              <Text style={styles.copyright}>
                © 2025 LUNA - Tous droits réservés
              </Text>
            </View>
          </ScrollView>
        </SafeAreaView>
      </LinearGradient>
    </View>
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
  logoSection: {
    alignItems: 'center',
    paddingVertical: spacing.xxl,
  },
  logoEmoji: {
    fontSize: 64,
    marginBottom: spacing.md,
  },
  logoText: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: spacing.xs,
    textShadowColor: 'rgba(255, 182, 193, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  logoSubtext: {
    fontSize: fonts.sizes.lg,
    color: '#FFC8DD',
    fontWeight: '600',
    marginBottom: spacing.md,
  },
  version: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255,255,255,0.5)',
  },
  missionCard: {
    backgroundColor: 'rgba(255, 182, 193, 0.12)',
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    marginBottom: spacing.xl,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.25)',
  },
  missionTitle: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: spacing.md,
  },
  missionText: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255,255,255,0.85)',
    lineHeight: 24,
  },
  section: {
    marginBottom: spacing.xl,
  },
  sectionTitle: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: spacing.md,
  },
  legalItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
  },
  legalLabel: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: '#fff',
    fontWeight: '500',
  },
  creditItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  creditLabel: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255,255,255,0.6)',
  },
  creditValue: {
    fontSize: fonts.sizes.md,
    color: '#fff',
    fontWeight: '500',
  },
  contactButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: spacing.sm,
    backgroundColor: 'rgba(255, 182, 193, 0.15)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    marginBottom: spacing.xl,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.3)',
  },
  contactText: {
    fontSize: fonts.sizes.md,
    color: '#FFB6C1',
    fontWeight: '600',
  },
  footer: {
    alignItems: 'center',
    paddingTop: spacing.xl,
    gap: spacing.sm,
  },
  footerText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255,255,255,0.6)',
  },
  copyright: {
    fontSize: fonts.sizes.xs,
    color: 'rgba(255,255,255,0.4)',
  },
  infoCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: spacing.md,
    backgroundColor: 'rgba(16, 185, 129, 0.12)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(16, 185, 129, 0.25)',
  },
  infoText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: 'rgba(255,255,255,0.8)',
    lineHeight: 20,
  },
});

