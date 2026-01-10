import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Alert,
  ActivityIndicator,
  Switch,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router } from 'expo-router';
import { exportDataJSON, exportDataPDF } from '@/lib/services/exportService';
import { deleteAccount } from '@/lib/services/accountDeletionService';
import { getConsents, updateConsent } from '@/lib/services/consentService';
import { getLastConsent } from '@/lib/services/consentAuditService';
import { trackEvents, Analytics } from '@/lib/analytics';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

export default function PrivacyScreen() {
  const [exportingJSON, setExportingJSON] = useState(false);
  const [exportingPDF, setExportingPDF] = useState(false);
  const [healthConsent, setHealthConsent] = useState(false);
  const [analyticsConsent, setAnalyticsConsent] = useState(false);
  const [healthConsentDate, setHealthConsentDate] = useState(null);
  const [policyVersion, setPolicyVersion] = useState(null);

  useEffect(() => {
    loadConsents();
    loadConsentDetails();
  }, []);

  const loadConsents = async () => {
    const consents = await getConsents();
    setHealthConsent(consents.health || false);
    setAnalyticsConsent(consents.analytics || false);
    setHealthConsentDate(consents.date);
    setPolicyVersion(consents.version || '2.0.0');
  };

  const loadConsentDetails = async () => {
    const lastHealthConsent = await getLastConsent('health');
    if (lastHealthConsent && lastHealthConsent.created_at) {
      setHealthConsentDate(lastHealthConsent.created_at);
    }
  };

  const handleToggleHealth = async (value) => {
    if (!value) {
      // Retirer le consentement santé = supprimer le compte
      Alert.alert(
        'Retrait du consentement santé',
        'Retirer ce consentement signifie que nous devons supprimer toutes tes données de cycle. Cela équivaut à supprimer ton compte.\n\nVeux-tu vraiment continuer ?',
        [
          { text: 'Annuler', style: 'cancel' },
          {
            text: 'Supprimer mes données',
            style: 'destructive',
            onPress: handleDeleteAccount,
          },
        ]
      );
      return;
    }

    // Accepter le consentement santé
    try {
      await updateConsent('health', true);
      setHealthConsent(true);
      Alert.alert(
        '✅ Consentement accordé',
        'Tu peux maintenant utiliser toutes les fonctionnalités de LUNA liées au cycle menstruel.'
      );
    } catch (error) {
      Alert.alert('Erreur', 'Impossible de modifier le consentement');
    }
  };

  const handleToggleAnalytics = async (value) => {
    try {
      await updateConsent('analytics', value);
      setAnalyticsConsent(value);
      
      if (!value) {
        // Reset Mixpanel quand consentement retiré
        Analytics.reset();
      }
      
      Alert.alert(
        value ? 'Analytics activés' : 'Analytics désactivés',
        value 
          ? 'Nous collecterons maintenant des données d\'usage anonymes pour améliorer l\'app'
          : 'Nous ne collecterons plus de données d\'usage. Mixpanel a été réinitialisé'
      );
    } catch (error) {
      Alert.alert('Erreur', 'Impossible de modifier le consentement');
    }
  };

  const handleExportJSON = async () => {
    setExportingJSON(true);
    try {
      await exportDataJSON();
      trackEvents.exportPDF(30); // 30 jours pour JSON aussi
      Alert.alert('Succès', 'Tes données ont été exportées au format JSON');
    } catch (error) {
      console.error('[Privacy] Export JSON error:', error);
      Alert.alert('Erreur', 'Impossible d\'exporter les données');
    } finally {
      setExportingJSON(false);
    }
  };

  const handleExportPDF = async () => {
    setExportingPDF(true);
    try {
      await exportDataPDF();
      trackEvents.exportPDF(30);
      Alert.alert('Succès', 'Ton rapport PDF a été créé');
    } catch (error) {
      console.error('[Privacy] Export PDF error:', error);
      Alert.alert('Erreur', 'Impossible de créer le PDF');
    } finally {
      setExportingPDF(false);
    }
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
          onPress: confirmDelete,
        },
      ]
    );
  };

  const confirmDelete = () => {
    Alert.alert(
      'Confirmation finale',
      'Tape "SUPPRIMER" pour confirmer',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Continuer',
          onPress: async () => {
            try {
              console.log('[Privacy] Début suppression compte...');
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
              console.error('[Privacy] Delete account error:', error);
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

  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea}>
          <Stack.Screen
            options={{
              title: 'Confidentialité',
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
            {/* Consentements */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Mes Consentements</Text>
              
              <View style={styles.consentCard}>
                <View style={styles.consentItem}>
                  <View style={styles.consentLeft}>
                    <Ionicons name="heart" size={20} color="#FFB6C1" />
                    <View style={styles.consentText}>
                      <Text style={styles.consentLabel}>Données de cycle (santé)</Text>
                      <Text style={styles.consentDescription}>
                        {healthConsent 
                          ? `Accordé le ${healthConsentDate ? new Date(healthConsentDate).toLocaleDateString('fr-FR') : 'N/A'} - Version ${policyVersion}` 
                          : 'Requis pour accéder aux fonctionnalités cycle'}
                      </Text>
                    </View>
                  </View>
                  {healthConsent ? (
                    <Ionicons name="checkmark-circle" size={24} color="#10B981" />
                  ) : (
                    <Switch
                      value={healthConsent}
                      onValueChange={handleToggleHealth}
                      trackColor={{ false: 'rgba(255,255,255,0.2)', true: '#FFB6C1' }}
                      thumbColor={healthConsent ? '#fff' : '#f4f3f4'}
                    />
                  )}
                </View>

                <View style={styles.consentItem}>
                  <View style={styles.consentLeft}>
                    <Ionicons name="analytics" size={20} color="#C084FC" />
                    <View style={styles.consentText}>
                      <Text style={styles.consentLabel}>Analytics (optionnel)</Text>
                      <Text style={styles.consentDescription}>
                        Aide à améliorer l'app - Peut être modifié
                      </Text>
                    </View>
                  </View>
                  <Switch
                    value={analyticsConsent}
                    onValueChange={handleToggleAnalytics}
                    trackColor={{ false: 'rgba(255,255,255,0.2)', true: '#C084FC' }}
                    thumbColor={analyticsConsent ? '#fff' : '#f4f3f4'}
                  />
                </View>
              </View>

              {healthConsent ? (
                <Text style={styles.consentNote}>
                  💡 Pour retirer ton consentement santé, utilise le bouton "Supprimer mon compte" ci-dessous (toutes les données seront perdues).
                </Text>
              ) : (
                <Text style={[styles.consentNote, { color: '#F59E0B' }]}>
                  ⚠️ Tu dois accepter le traitement de tes données de cycle pour utiliser les fonctionnalités de suivi menstruel de LUNA.
                </Text>
              )}
            </View>

            {/* Politique */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Documentation</Text>
              
              <TouchableOpacity
                style={styles.actionItem}
                onPress={() => {/* Afficher DATA_POLICY.md */}}
              >
                <Ionicons name="document-text-outline" size={24} color="#C084FC" />
                <View style={styles.actionContent}>
                  <Text style={styles.actionLabel}>Politique de confidentialité</Text>
                  <Text style={styles.actionDescription}>
                    Comment nous protégeons tes données (RGPD) - Version {policyVersion}
                  </Text>
                </View>
                <Ionicons name="chevron-forward" size={20} color="rgba(255,255,255,0.4)" />
              </TouchableOpacity>

              <TouchableOpacity
                style={styles.actionItem}
                onPress={() => {
                  Alert.alert(
                    'Demander l\'effacement de mes données',
                    'Tu seras redirigé vers notre support pour traiter ta demande d\'effacement.\n\nTu peux aussi supprimer directement ton compte ci-dessous (action immédiate).',
                    [
                      { text: 'Annuler', style: 'cancel' },
                      { text: 'Contacter support', onPress: () => {
                        // mailto:privacy@luna-app.fr
                        const subject = 'Demande d\'effacement de données (Art. 17 RGPD)';
                        const body = `Bonjour,\n\nJe souhaite exercer mon droit à l'effacement de mes données personnelles conformément à l'Article 17 du RGPD.\n\nMerci de traiter ma demande sous 30 jours.\n\nCordialement`;
                        console.log('[Privacy] Mailto:', `privacy@luna-app.fr?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`);
                        Alert.alert('Email', 'Fonctionnalité à implémenter avec Linking.openURL');
                      }},
                    ]
                  );
                }}
              >
                <Ionicons name="mail-outline" size={24} color="#F59E0B" />
                <View style={styles.actionContent}>
                  <Text style={styles.actionLabel}>Demander l'effacement de mes données</Text>
                  <Text style={styles.actionDescription}>
                    Art. 17 RGPD - Droit à l'oubli (traité sous 30 jours)
                  </Text>
                </View>
                <Ionicons name="send-outline" size={20} color="#F59E0B" />
              </TouchableOpacity>
            </View>

            {/* Export */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Mes données</Text>
              
              <TouchableOpacity
                style={styles.actionItem}
                onPress={handleExportJSON}
                disabled={exportingJSON}
              >
                <Ionicons name="code-download-outline" size={24} color="#10B981" />
                <View style={styles.actionContent}>
                  <Text style={styles.actionLabel}>Exporter en JSON</Text>
                  <Text style={styles.actionDescription}>
                    Toutes tes données dans un fichier JSON
                  </Text>
                </View>
                {exportingJSON ? (
                  <ActivityIndicator color="#10B981" />
                ) : (
                  <Ionicons name="download-outline" size={20} color="#10B981" />
                )}
              </TouchableOpacity>

              <TouchableOpacity
                style={styles.actionItem}
                onPress={handleExportPDF}
                disabled={exportingPDF}
              >
                <Ionicons name="document-outline" size={24} color="#F59E0B" />
                <View style={styles.actionContent}>
                  <Text style={styles.actionLabel}>Exporter en PDF</Text>
                  <Text style={styles.actionDescription}>
                    Rapport du dernier mois (journal + stats)
                  </Text>
                </View>
                {exportingPDF ? (
                  <ActivityIndicator color="#F59E0B" />
                ) : (
                  <Ionicons name="download-outline" size={20} color="#F59E0B" />
                )}
              </TouchableOpacity>
            </View>

            {/* Zone danger */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Zone de danger</Text>
              
              <TouchableOpacity
                style={styles.dangerItem}
                onPress={handleDeleteAccount}
              >
                <Ionicons name="trash-outline" size={24} color="#EF4444" />
                <View style={styles.actionContent}>
                  <Text style={[styles.actionLabel, { color: '#EF4444' }]}>
                    Supprimer mon compte
                  </Text>
                  <Text style={styles.actionDescription}>
                    Action irréversible - toutes tes données seront perdues
                  </Text>
                </View>
                <Ionicons name="warning-outline" size={20} color="#EF4444" />
              </TouchableOpacity>
            </View>

            {/* Info RGPD */}
            <View style={styles.infoCard}>
              <Ionicons name="shield-checkmark" size={24} color="#10B981" />
              <Text style={styles.infoText}>
                Conformément au RGPD, tu as le droit d'accéder, modifier, exporter et supprimer tes données à tout moment. Tes données sont chiffrées et ne sont jamais vendues.
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
  section: {
    marginBottom: spacing.xl,
  },
  sectionTitle: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: spacing.md,
  },
  actionItem: {
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
  dangerItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(239, 68, 68, 0.3)',
  },
  actionContent: {
    flex: 1,
  },
  actionLabel: {
    fontSize: fonts.sizes.md,
    color: '#fff',
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  actionDescription: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255,255,255,0.6)',
    lineHeight: 18,
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
    marginTop: spacing.lg,
  },
  infoText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: 'rgba(255,255,255,0.8)',
    lineHeight: 20,
  },
  consentCard: {
    backgroundColor: 'rgba(255, 182, 193, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    gap: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.2)',
  },
  consentItem: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: spacing.sm,
  },
  consentLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
    flex: 1,
  },
  consentText: {
    flex: 1,
  },
  consentLabel: {
    fontSize: fonts.sizes.md,
    color: '#fff',
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  consentDescription: {
    fontSize: fonts.sizes.xs,
    color: 'rgba(255,255,255,0.6)',
    lineHeight: 16,
  },
  consentNote: {
    fontSize: fonts.sizes.xs,
    color: 'rgba(255,255,255,0.6)',
    lineHeight: 18,
    fontStyle: 'italic',
    marginTop: spacing.sm,
  },
});

