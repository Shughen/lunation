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
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

export default function ConsentScreen() {
  const [consentHealth, setConsentHealth] = useState(false);
  const [consentAnalytics, setConsentAnalytics] = useState(false);

  const handleContinue = async () => {
    if (!consentHealth) {
      Alert.alert(
        'Consentement requis',
        'Pour utiliser LUNA, nous devons pouvoir traiter tes données de cycle menstruel. Ce consentement est obligatoire pour le fonctionnement de l\'app.',
        [{ text: 'OK' }]
      );
      return;
    }

    try {
      // Sauvegarder les consentements avec version et date
      const consentData = {
        health: consentHealth,
        analytics: consentAnalytics,
        version: '2.0.0',
        date: new Date().toISOString(),
      };

      await AsyncStorage.setItem('user_consent', JSON.stringify(consentData));
      
      // Continuer vers cycle setup
      router.push('/onboarding/cycle-setup');
    } catch (error) {
      console.error('[Consent] Save error:', error);
      Alert.alert('Erreur', 'Impossible de sauvegarder. Veuillez réessayer.');
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
          <Text style={styles.headerTitle}>Étape 2/4</Text>
          <View style={{ width: 40 }} />
        </View>

        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          {/* Title */}
          <View style={styles.titleSection}>
            <Text style={styles.emoji}>🔐</Text>
            <Text style={styles.title}>Tes données, tes choix</Text>
            <Text style={styles.subtitle}>
              Conformément au RGPD, nous avons besoin de ton consentement explicite
            </Text>
          </View>

          {/* Consentement Santé (Obligatoire) */}
          <View style={styles.consentCard}>
            <View style={styles.consentHeader}>
              <View style={styles.consentIconContainer}>
                <Ionicons name="heart-outline" size={24} color="#FFB6C1" />
              </View>
              <Text style={styles.consentBadge}>OBLIGATOIRE</Text>
            </View>

            <Text style={styles.consentTitle}>Traitement de mes données de cycle</Text>
            <Text style={styles.consentDescription}>
              Pour fonctionner, LUNA doit traiter tes données de cycle menstruel (dates, phases, humeur). Ces données sont considérées comme <Text style={styles.bold}>données de santé</Text> selon le RGPD (Art. 9).
              {'\n\n'}
              <Text style={styles.bold}>Usage :</Text> Calcul de ta phase actuelle, recommandations personnalisées, suivi dans ton journal
              {'\n\n'}
              <Text style={styles.bold}>Stockage :</Text> Supabase (région UE - Irlande), chiffré en transit et au repos
              {'\n\n'}
              <Text style={styles.bold}>Accès :</Text> Toi uniquement (RLS activé), jamais partagé ni vendu
            </Text>

            <TouchableOpacity
              style={styles.checkboxContainer}
              onPress={() => setConsentHealth(!consentHealth)}
              activeOpacity={0.7}
            >
              <View style={[styles.checkbox, consentHealth && styles.checkboxActive]}>
                {consentHealth && <Ionicons name="checkmark" size={20} color="#fff" />}
              </View>
              <Text style={styles.checkboxText}>
                J'accepte le traitement de mes données de cycle pour le fonctionnement de LUNA
              </Text>
            </TouchableOpacity>
          </View>

          {/* Consentement Analytics (Optionnel) */}
          <View style={[styles.consentCard, styles.consentOptional]}>
            <View style={styles.consentHeader}>
              <View style={[styles.consentIconContainer, { backgroundColor: 'rgba(192, 132, 252, 0.15)' }]}>
                <Ionicons name="analytics-outline" size={24} color="#C084FC" />
              </View>
              <Text style={[styles.consentBadge, styles.consentBadgeOptional]}>OPTIONNEL</Text>
            </View>

            <Text style={styles.consentTitle}>Analytics et amélioration produit</Text>
            <Text style={styles.consentDescription}>
              Nous utilisons <Text style={styles.bold}>Mixpanel</Text> pour comprendre comment l'app est utilisée (pages visitées, fonctionnalités populaires).
              {'\n\n'}
              <Text style={styles.bold}>Données anonymisées</Text> : aucune donnée personnelle ou de santé n'est envoyée à Mixpanel
              {'\n\n'}
              <Text style={styles.bold}>Tu peux refuser</Text> : LUNA fonctionnera exactement pareil
              {'\n\n'}
              Tu pourras changer ce choix à tout moment dans Settings &gt; Confidentialité
            </Text>

            <TouchableOpacity
              style={styles.checkboxContainer}
              onPress={() => setConsentAnalytics(!consentAnalytics)}
              activeOpacity={0.7}
            >
              <View style={[styles.checkbox, consentAnalytics && styles.checkboxActive]}>
                {consentAnalytics && <Ionicons name="checkmark" size={20} color="#fff" />}
              </View>
              <Text style={styles.checkboxText}>
                J'accepte le partage de données d'usage anonymisées pour améliorer l'app
              </Text>
            </TouchableOpacity>
          </View>

          {/* Liens documentation */}
          <View style={styles.linksContainer}>
            <TouchableOpacity
              style={styles.linkButton}
              onPress={() => {/* Afficher DATA_POLICY.md */}}
            >
              <Ionicons name="document-text-outline" size={16} color="#FFB6C1" />
              <Text style={styles.linkText}>Politique de confidentialité complète</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.linkButton}
              onPress={() => {/* Afficher DISCLAIMER.md */}}
            >
              <Ionicons name="medical-outline" size={16} color="#FFB6C1" />
              <Text style={styles.linkText}>Disclaimer médical</Text>
            </TouchableOpacity>
          </View>

          {/* Info RGPD */}
          <View style={styles.rgpdCard}>
            <Ionicons name="shield-checkmark" size={20} color="#10B981" />
            <Text style={styles.rgpdText}>
              Tes droits RGPD : accès, rectification, portabilité, suppression. Contact : privacy@luna-app.fr
            </Text>
          </View>
        </ScrollView>

        {/* Footer */}
        <View style={styles.footer}>
          <TouchableOpacity
            style={[styles.continueButton, !consentHealth && styles.continueButtonDisabled]}
            onPress={handleContinue}
            activeOpacity={0.8}
            disabled={!consentHealth}
          >
            <LinearGradient
              colors={consentHealth ? ['#FFB6C1', '#FFC8DD'] : ['rgba(255,255,255,0.1)', 'rgba(255,255,255,0.1)']}
              style={styles.continueButtonGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Text style={[styles.continueButtonText, !consentHealth && styles.continueButtonTextDisabled]}>
                Continuer
              </Text>
              <Ionicons name="arrow-forward" size={20} color={consentHealth ? "#fff" : "rgba(255,255,255,0.5)"} />
            </LinearGradient>
          </TouchableOpacity>
        </View>
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
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.xl,
  },
  titleSection: {
    alignItems: 'center',
    marginBottom: spacing.xl,
    marginTop: spacing.lg,
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
    textAlign: 'center',
    textShadowColor: 'rgba(255, 182, 193, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  subtitle: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.7)',
    textAlign: 'center',
    lineHeight: 22,
  },
  consentCard: {
    backgroundColor: 'rgba(255, 182, 193, 0.1)',
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    marginBottom: spacing.lg,
    borderWidth: 2,
    borderColor: 'rgba(255, 182, 193, 0.3)',
  },
  consentOptional: {
    backgroundColor: 'rgba(192, 132, 252, 0.08)',
    borderColor: 'rgba(192, 132, 252, 0.2)',
  },
  consentHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: spacing.md,
  },
  consentIconContainer: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: 'rgba(255, 182, 193, 0.15)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  consentBadge: {
    backgroundColor: '#FFB6C1',
    paddingHorizontal: spacing.sm,
    paddingVertical: 4,
    borderRadius: 12,
    fontSize: fonts.sizes.xs,
    color: '#fff',
    fontWeight: 'bold',
  },
  consentBadgeOptional: {
    backgroundColor: '#C084FC',
  },
  consentTitle: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: spacing.sm,
  },
  consentDescription: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.85)',
    lineHeight: 22,
    marginBottom: spacing.md,
  },
  bold: {
    fontWeight: '700',
    color: '#FFFFFF',
  },
  checkboxContainer: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: spacing.md,
    paddingTop: spacing.md,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255, 255, 255, 0.1)',
  },
  checkbox: {
    width: 28,
    height: 28,
    borderRadius: 14,
    borderWidth: 2,
    borderColor: 'rgba(255, 255, 255, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 2,
  },
  checkboxActive: {
    backgroundColor: '#FFB6C1',
    borderColor: '#FFB6C1',
  },
  checkboxText: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.95)',
    fontWeight: '500',
    lineHeight: 22,
  },
  linksContainer: {
    gap: spacing.sm,
    marginBottom: spacing.xl,
  },
  linkButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: spacing.xs,
    paddingVertical: spacing.sm,
  },
  linkText: {
    fontSize: fonts.sizes.sm,
    color: '#FFB6C1',
    fontWeight: '600',
    textDecorationLine: 'underline',
  },
  rgpdCard: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    backgroundColor: 'rgba(16, 185, 129, 0.12)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(16, 185, 129, 0.25)',
  },
  rgpdText: {
    flex: 1,
    fontSize: fonts.sizes.xs,
    color: 'rgba(255, 255, 255, 0.8)',
    lineHeight: 18,
  },
  footer: {
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.lg,
  },
  continueButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  continueButtonDisabled: {
    opacity: 0.5,
    shadowOpacity: 0,
    elevation: 0,
  },
  continueButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    gap: spacing.sm,
  },
  continueButtonText: {
    color: '#fff',
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
  continueButtonTextDisabled: {
    color: 'rgba(255,255,255,0.5)',
  },
});

