import React, { useState } from 'react';
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
import { router } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { trackEvents } from '@/lib/analytics';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

export default function DisclaimerScreen() {
  const [accepted, setAccepted] = useState(false);

  const handleFinish = async () => {
    if (!accepted) {
      Alert.alert(
        'Acceptation requise',
        'Tu dois accepter les conditions pour utiliser LUNA',
        [{ text: 'OK' }]
      );
      return;
    }

    try {
      // Marquer l'onboarding comme terminé
      await AsyncStorage.setItem('onboarding_completed', 'true');
      await AsyncStorage.setItem('disclaimer_accepted', 'true');
      await AsyncStorage.setItem('disclaimer_accepted_date', new Date().toISOString());
      
      // Récupérer les données cycle pour analytics
      const cycleConfig = await AsyncStorage.getItem('cycle_config');
      const cycleData = cycleConfig ? JSON.parse(cycleConfig) : null;
      
      // Track analytics
      if (cycleData) {
        trackEvents.onboardingCompleted(
          cycleData.lastPeriodDate,
          cycleData.cycleLength
        );
      }
      
      // Rediriger vers Home
      router.replace('/(tabs)/home');
    } catch (error) {
      console.error('[Disclaimer] Finish error:', error);
      Alert.alert('Erreur', 'Impossible de terminer. Veuillez réessayer.');
    }
  };

  const handleBack = () => {
    router.back();
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
          <TouchableOpacity onPress={handleBack} style={styles.backButton}>
            <Ionicons name="arrow-back" size={24} color="#fff" />
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Dernière étape</Text>
          <View style={{ width: 40 }} />
        </View>

        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          {/* Title */}
          <View style={styles.titleSection}>
            <Text style={styles.emoji}>⚠️</Text>
            <Text style={styles.title}>Important</Text>
            <Text style={styles.subtitle}>Avant de commencer, voici ce que tu dois savoir</Text>
          </View>

          {/* Disclaimer content */}
          <View style={styles.disclaimerCard}>
            <DisclaimerItem
              icon="medical-outline"
              title="LUNA n'est pas un dispositif médical"
              description="Cette app est un outil de bien-être et de développement personnel, pas un outil médical."
            />
            
            <DisclaimerItem
              icon="shield-checkmark-outline"
              title="Conseils non médicaux"
              description="Nos recommandations sont générales. Pour toute question de santé, consulte un professionnel."
            />
            
            <DisclaimerItem
              icon="close-circle-outline"
              title="Pas de contraception"
              description="LUNA ne doit PAS être utilisé comme méthode contraceptive ni pour planifier une grossesse."
            />
            
            <DisclaimerItem
              icon="heart-outline"
              title="Bien-être et écoute de soi"
              description="LUNA t'aide à mieux te connaître à travers ton cycle et l'astrologie, dans une approche bienveillante."
            />
          </View>

          {/* Checkbox d'acceptation */}
          <TouchableOpacity
            style={styles.checkboxContainer}
            onPress={() => setAccepted(!accepted)}
            activeOpacity={0.7}
          >
            <View style={[styles.checkbox, accepted && styles.checkboxActive]}>
              {accepted && <Ionicons name="checkmark" size={20} color="#fff" />}
            </View>
            <Text style={styles.checkboxText}>
              J'ai lu et j'accepte ces conditions d'utilisation
            </Text>
          </TouchableOpacity>

          {/* Link vers disclaimer complet */}
          <TouchableOpacity
            style={styles.linkButton}
            onPress={() => router.push('/settings/privacy')}
          >
            <Text style={styles.linkText}>Lire le disclaimer complet</Text>
            <Ionicons name="open-outline" size={16} color="#FFB6C1" />
          </TouchableOpacity>
        </ScrollView>

        {/* Footer */}
        <View style={styles.footer}>
          <TouchableOpacity
            style={[styles.finishButton, !accepted && styles.finishButtonDisabled]}
            onPress={handleFinish}
            activeOpacity={0.8}
            disabled={!accepted}
          >
            <LinearGradient
              colors={accepted ? ['#FFB6C1', '#FFC8DD'] : ['rgba(255,255,255,0.1)', 'rgba(255,255,255,0.1)']}
              style={styles.finishButtonGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Text style={[styles.finishButtonText, !accepted && styles.finishButtonTextDisabled]}>
                Commencer à utiliser LUNA
              </Text>
              <Ionicons name="sparkles" size={20} color={accepted ? "#fff" : "rgba(255,255,255,0.5)"} />
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </LinearGradient>
  );
}

// Composant pour un item du disclaimer
function DisclaimerItem({ icon, title, description }) {
  return (
    <View style={styles.disclaimerItem}>
      <View style={styles.disclaimerIconContainer}>
        <Ionicons name={icon} size={24} color="#FFB6C1" />
      </View>
      <View style={styles.disclaimerContent}>
        <Text style={styles.disclaimerTitle}>{title}</Text>
        <Text style={styles.disclaimerDescription}>{description}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  backButton: {
    width: 40,
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerTitle: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  scrollContent: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.xl,
  },
  titleSection: {
    alignItems: 'center',
    marginVertical: spacing.xl,
  },
  emoji: {
    fontSize: 48,
    marginBottom: spacing.md,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: spacing.sm,
    textShadowColor: 'rgba(255, 182, 193, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  subtitle: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.7)',
    textAlign: 'center',
  },
  disclaimerCard: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    gap: spacing.lg,
    marginBottom: spacing.xl,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.2)',
  },
  disclaimerItem: {
    flexDirection: 'row',
    gap: spacing.md,
  },
  disclaimerIconContainer: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: 'rgba(255, 182, 193, 0.15)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  disclaimerContent: {
    flex: 1,
    gap: spacing.xs,
  },
  disclaimerTitle: {
    fontSize: fonts.sizes.md,
    color: '#FFC8DD',
    fontWeight: 'bold',
  },
  disclaimerDescription: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.8)',
    lineHeight: 20,
  },
  checkboxContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    backgroundColor: 'rgba(255, 182, 193, 0.1)',
    borderRadius: borderRadius.md,
    marginBottom: spacing.lg,
    borderWidth: 2,
    borderColor: 'rgba(255, 182, 193, 0.3)',
  },
  checkbox: {
    width: 28,
    height: 28,
    borderRadius: 14,
    borderWidth: 2,
    borderColor: 'rgba(255, 255, 255, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  checkboxActive: {
    backgroundColor: '#FFB6C1',
    borderColor: '#FFB6C1',
  },
  checkboxText: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.9)',
    fontWeight: '500',
  },
  linkButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: spacing.xs,
    paddingVertical: spacing.sm,
    marginBottom: spacing.lg,
  },
  linkText: {
    fontSize: fonts.sizes.sm,
    color: '#FFB6C1',
    fontWeight: '600',
    textDecorationLine: 'underline',
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
  },
  finishButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  finishButtonDisabled: {
    opacity: 0.5,
    shadowOpacity: 0,
    elevation: 0,
  },
  finishButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    gap: spacing.sm,
  },
  finishButtonText: {
    color: '#fff',
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
  finishButtonTextDisabled: {
    color: 'rgba(255,255,255,0.5)',
  },
});

