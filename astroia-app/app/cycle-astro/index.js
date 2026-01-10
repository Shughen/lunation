import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  SafeAreaView,
  TextInput,
  Platform,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router } from 'expo-router';
import { useProfileStore } from '@/stores/profileStore';
import { useCycleHistoryStore } from '@/stores/cycleHistoryStore';
import { analyzeCycleAstro, saveCycleAnalysis } from '@/lib/api/cycleAstroService';
import { useHapticFeedback } from '@/hooks/useHapticFeedback';
import { hasHealthConsent } from '@/lib/services/consentService';
import { MedicalDisclaimer } from '@/components/MedicalDisclaimer';
import THEME from '@/constants/theme';

const CYCLE_PHASES = [
  { id: 'menstrual', name: 'Menstruelle', emoji: '🌑', description: '1-5 jours', color: '#FF6B9D', gradient: ['#FF6B9D', '#FF8FB3'] },
  { id: 'follicular', name: 'Folliculaire', emoji: '🌒', description: '6-13 jours', color: '#FFB347', gradient: ['#FFB347', '#FFC670'] },
  { id: 'ovulation', name: 'Ovulation', emoji: '🌕', description: '14-16 jours', color: '#FFD93D', gradient: ['#FFD93D', '#FFE66D'] },
  { id: 'luteal', name: 'Lutéale', emoji: '🌘', description: '17-28 jours', color: '#C084FC', gradient: ['#C084FC', '#D8B4FE'] },
];

const MOOD_OPTIONS = [
  { id: 'energetic', name: 'Énergique', emoji: '⚡' },
  { id: 'calm', name: 'Calme', emoji: '😌' },
  { id: 'creative', name: 'Créative', emoji: '🎨' },
  { id: 'tired', name: 'Fatiguée', emoji: '😴' },
  { id: 'irritable', name: 'Irritable', emoji: '😤' },
  { id: 'emotional', name: 'Émotive', emoji: '🥺' },
];

export default function CycleAstroScreen() {
  const profile = useProfileStore((state) => state.profile);
  const getSunSign = useProfileStore((state) => state.getSunSign);
  const getMoonSign = useProfileStore((state) => state.getMoonSign);
  const getAscendant = useProfileStore((state) => state.getAscendant);
  const predictNextPeriod = useCycleHistoryStore((state) => state.predictNextPeriod);
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  
  // Prédiction prochaines règles
  const prediction = predictNextPeriod();
  
  // État du formulaire
  const [cycleData, setCycleData] = useState({
    phase: 'menstrual',
    dayOfCycle: '1',
    mood: 'calm',
    symptoms: '',
  });

  const haptic = useHapticFeedback();
  const scrollViewRef = useRef(null);

  // Vérifier consentement au chargement
  useEffect(() => {
    checkConsent();
  }, []);

  const checkConsent = async () => {
    const consent = await hasHealthConsent();
    if (!consent) {
      Alert.alert(
        'Consentement requis',
        'Pour utiliser cette fonctionnalité, tu dois accepter le traitement de tes données de cycle (données de santé).',
        [
          { text: 'Annuler', onPress: () => router.back(), style: 'cancel' },
          { text: 'Voir les paramètres', onPress: () => router.push('/settings/privacy') },
        ]
      );
    }
  };

  const handleAnalyze = async () => {
    // Vérifier consentement avant analyse
    const consent = await hasHealthConsent();
    if (!consent) {
      Alert.alert(
        'Consentement requis',
        'Tu dois accepter le traitement de tes données de cycle pour utiliser cette fonctionnalité.',
        [{ text: 'OK' }]
      );
      return;
    }
    if (!profile?.birthDate) {
      Alert.alert(
        'Profil incomplet',
        'Veuillez compléter votre profil astrologique pour continuer',
        [
          { text: 'Annuler', style: 'cancel' },
          { text: 'Compléter', onPress: () => router.push('/(tabs)/profile') },
        ]
      );
      return;
    }

    const dayNum = parseInt(cycleData.dayOfCycle);
    if (isNaN(dayNum) || dayNum < 1 || dayNum > 35) {
      Alert.alert('Erreur', 'Veuillez entrer un jour de cycle valide (1-35)');
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      // Récupérer les données astrologiques de l'utilisateur
      const astroData = {
        sunSign: getSunSign(),
        moonSign: getMoonSign(),
        ascendant: getAscendant(),
      };

      // Analyser avec le service
      const analysis = await analyzeCycleAstro({
        cycleData: {
          ...cycleData,
          dayOfCycle: dayNum,
        },
        astroData,
        birthDate: profile.birthDate,
      });

      setResult(analysis);

      // Sauvegarder l'analyse
      await saveCycleAnalysis({
        cycleData,
        analysis,
        astroData,
      });

      // Scroll vers le résultat
      setTimeout(() => {
        scrollViewRef.current?.scrollTo({ y: 0, animated: true });
      }, 100);
    } catch (error) {
      console.error('[CycleAstro] Analyze error:', error);
      Alert.alert(
        'Erreur',
        'Impossible d\'analyser pour le moment. Veuillez réessayer.',
        [{ text: 'OK' }]
      );
    } finally {
      setLoading(false);
    }
  };

  const renderResult = () => {
    if (!result) return null;

    const { recommendations, moonPhase, transitInfo, energyLevel, bestActivities } = result;

    return (
      <View style={styles.resultContainer}>
        {/* Bouton retour */}
        <TouchableOpacity
          style={styles.backButton}
          onPress={() => setResult(null)}
        >
          <Ionicons name="arrow-back" size={24} color={THEME.colors.textLight} />
          <Text style={styles.backButtonText}>Nouvelle analyse</Text>
        </TouchableOpacity>

        {/* Card principale */}
        <View style={styles.mainCard}>
          <Text style={styles.mainEmoji}>{moonPhase.emoji}</Text>
          <Text style={styles.mainTitle}>{moonPhase.name}</Text>
          <Text style={styles.mainSubtitle}>
            Jour {cycleData.dayOfCycle} • Phase {CYCLE_PHASES.find(p => p.id === cycleData.phase)?.name}
          </Text>
          
          {/* Badge J-X avant prochaines règles */}
          {prediction && prediction.daysUntil > 0 && (
            <View style={styles.countdownBadge}>
              <Text style={styles.countdownBadgeText}>
                J-{prediction.daysUntil} avant prochaines règles
              </Text>
            </View>
          )}
          
          <View style={styles.energyBar}>
            <View style={styles.energyBarLabel}>
              <Text style={styles.energyBarText}>Énergie cosmique</Text>
              <Text style={styles.energyBarValue}>{energyLevel}%</Text>
            </View>
            <View style={styles.energyBarTrack}>
              <View style={[styles.energyBarFill, { width: `${energyLevel}%` }]} />
            </View>
          </View>
        </View>

        {/* Transits */}
        {transitInfo && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>🌙 Transits du jour</Text>
            <Text style={styles.cardText}>{transitInfo.description}</Text>
            <View style={styles.transitDetails}>
              <View style={styles.transitItem}>
                <Text style={styles.transitLabel}>Lune en</Text>
                <Text style={styles.transitValue}>{transitInfo.moonSign?.emoji} {transitInfo.moonSign?.name}</Text>
              </View>
              {transitInfo.aspect && (
                <View style={styles.transitItem}>
                  <Text style={styles.transitLabel}>Aspect</Text>
                  <Text style={styles.transitValue}>⚖️ {transitInfo.aspect}</Text>
                </View>
              )}
            </View>
          </View>
        )}

        {/* Activités recommandées */}
        {bestActivities && bestActivities.length > 0 && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>✨ Activités recommandées</Text>
            {bestActivities.map((activity, index) => (
              <View key={index} style={styles.activityItem}>
                <Text style={styles.activityEmoji}>{activity.emoji}</Text>
                <View style={styles.activityContent}>
                  <Text style={styles.activityName}>{activity.name}</Text>
                  <Text style={styles.activityDescription}>{activity.description}</Text>
                </View>
              </View>
            ))}
          </View>
        )}

        {/* Recommandations */}
        {recommendations && recommendations.length > 0 && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>💡 Conseils personnalisés</Text>
            {recommendations.map((rec, index) => (
              <View key={index} style={styles.recommendationItem}>
                <Text style={styles.recIcon}>{rec.icon}</Text>
                <Text style={styles.recText}>{rec.text}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Légende */}
        <View style={styles.legend}>
          <Text style={styles.legendText}>
            🌙 Cette analyse combine votre thème natal, les transits lunaires actuels et votre phase de cycle menstruel pour des recommandations personnalisées.
          </Text>
        </View>
      </View>
    );
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <LinearGradient colors={THEME.colors.gradientDark} style={styles.container}>
        <Stack.Screen
          options={{
            title: 'Cycle & Astrologie',
            headerStyle: { backgroundColor: THEME.colors.darkBg },
            headerTintColor: THEME.colors.textLight,
            headerShadowVisible: false,
          }}
        />

        <ScrollView
          ref={scrollViewRef}
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          {!result ? (
            <>
              {/* Bouton retour */}
              <TouchableOpacity
                style={styles.formBackButton}
                onPress={() => router.back()}
              >
                <Ionicons name="arrow-back" size={20} color="rgba(255,255,255,0.8)" />
                <Text style={styles.formBackButtonText}>Retour</Text>
              </TouchableOpacity>

              {/* Header */}
              <View style={styles.header}>
                <Text style={styles.headerTitle}>🌙 Cycle & Astrologie</Text>
              <Text style={styles.headerSubtitle}>
                Découvrez comment votre cycle menstruel et les transits lunaires influencent votre énergie et vos émotions
              </Text>
            </View>

            {/* Disclaimer médical */}
            <MedicalDisclaimer />

            {/* Formulaire */}
              <View style={styles.section}>
                <Text style={styles.sectionTitle}>📅 Mon cycle actuel</Text>

                {/* Jour du cycle */}
                <View style={styles.inputGroup}>
                  <Text style={styles.inputLabel}>Jour du cycle (1-35)</Text>
                  <TextInput
                    style={styles.textInput}
                    value={cycleData.dayOfCycle}
                    onChangeText={(text) => setCycleData({ ...cycleData, dayOfCycle: text.replace(/[^0-9]/g, '') })}
                    keyboardType="number-pad"
                    maxLength={2}
                    placeholder="Ex : 12"
                    placeholderTextColor="rgba(255,255,255,0.3)"
                  />
                </View>

                {/* Phase du cycle */}
                <View style={styles.inputGroup}>
                  <Text style={styles.inputLabel}>Phase du cycle</Text>
                  <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.phaseScroll}>
                    {CYCLE_PHASES.map((phase) => (
                      <TouchableOpacity
                        key={phase.id}
                        style={[
                          styles.phaseButton,
                          cycleData.phase === phase.id && styles.phaseButtonActive,
                        ]}
                        onPress={() => {
                          haptic.impact.light();
                          setCycleData({ ...cycleData, phase: phase.id });
                        }}
                      >
                        <Text style={styles.phaseEmoji}>{phase.emoji}</Text>
                        <Text style={[
                          styles.phaseName,
                          cycleData.phase === phase.id && styles.phaseNameActive,
                        ]}>
                          {phase.name}
                        </Text>
                        <Text style={styles.phaseDescription}>{phase.description}</Text>
                      </TouchableOpacity>
                    ))}
                  </ScrollView>
                </View>

                {/* Humeur */}
                <View style={styles.inputGroup}>
                  <Text style={styles.inputLabel}>Comment vous sentez-vous ?</Text>
                  <View style={styles.moodGrid}>
                    {MOOD_OPTIONS.map((mood) => (
                      <TouchableOpacity
                        key={mood.id}
                        style={[
                          styles.moodButton,
                          cycleData.mood === mood.id && styles.moodButtonActive,
                        ]}
                        onPress={() => {
                          haptic.impact.light();
                          setCycleData({ ...cycleData, mood: mood.id });
                        }}
                      >
                        <Text style={styles.moodEmoji}>{mood.emoji}</Text>
                        <Text style={[
                          styles.moodName,
                          cycleData.mood === mood.id && styles.moodNameActive,
                        ]}>
                          {mood.name}
                        </Text>
                      </TouchableOpacity>
                    ))}
                  </View>
                </View>

                {/* Symptômes (optionnel) */}
                <View style={styles.inputGroup}>
                  <Text style={styles.inputLabel}>Symptômes ou notes (optionnel)</Text>
                  <TextInput
                    style={[styles.textInput, styles.textArea]}
                    value={cycleData.symptoms}
                    onChangeText={(text) => setCycleData({ ...cycleData, symptoms: text })}
                    placeholder="Ex: crampes légères, fatigue..."
                    placeholderTextColor="rgba(255,255,255,0.3)"
                    multiline
                    numberOfLines={3}
                  />
                </View>
              </View>

              {/* Info profil */}
              {profile?.birthDate ? (
                <View style={styles.profileInfo}>
                  <Ionicons name="checkmark-circle" size={16} color="#10B981" />
                  <Text style={styles.profileInfoText}>
                    Profil astral : {getSunSign()?.emoji} {getSunSign()?.name}
                  </Text>
                </View>
              ) : (
                <TouchableOpacity
                  style={styles.completeProfileButton}
                  onPress={() => router.push('/(tabs)/profile')}
                >
                  <Ionicons name="alert-circle" size={16} color="#F59E0B" />
                  <Text style={styles.completeProfileText}>
                    Complétez votre profil pour une analyse personnalisée
                  </Text>
                </TouchableOpacity>
              )}

              {/* Bouton Analyser */}
              <TouchableOpacity
                style={[styles.analyzeButton, loading && styles.analyzeButtonDisabled]}
                onPress={() => {
                  haptic.impact.medium();
                  handleAnalyze();
                }}
                disabled={loading}
                activeOpacity={0.9}
              >
                {loading ? (
                  <ActivityIndicator color="#111111cc" />
                ) : (
                  <>
                    <Ionicons name="sparkles" size={24} color="#111111cc" style={{ paddingLeft: 4 }} />
                    <Text style={styles.analyzeButtonText}>Analyser mon cycle</Text>
                  </>
                )}
              </TouchableOpacity>

              {/* Info card */}
              <View style={styles.infoCard}>
                <Text style={styles.infoIcon}>💡</Text>
                <Text style={styles.infoText}>
                  Cette fonctionnalité combine les principes de l'astrologie avec les cycles naturels féminins pour vous offrir des recommandations personnalisées sur votre énergie, vos émotions et les meilleures activités selon votre phase de cycle et les transits lunaires.
                </Text>
              </View>
            </>
          ) : (
            renderResult()
          )}
        </ScrollView>
      </LinearGradient>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  container: {
    flex: 1,
  },
  scrollContent: {
    padding: 20,
    paddingTop: 10,
    paddingBottom: 124, // Augmenté de 100 à 124 (+24px) pour aérer le bas
  },
  formBackButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingVertical: 8,
    paddingHorizontal: 12,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 10,
    alignSelf: 'flex-start',
    marginBottom: 15,
  },
  formBackButtonText: {
    color: 'rgba(255,255,255,0.8)',
    fontSize: 14,
    fontWeight: '500',
  },
  header: {
    marginBottom: 25,
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 26,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 8,
    textAlign: 'center',
    textShadowColor: 'rgba(255, 182, 193, 0.6)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  headerSubtitle: {
    fontSize: 14,
    color: THEME.colors.textMuted,
    textAlign: 'center',
    lineHeight: 20,
    paddingHorizontal: 10,
  },
  section: {
    marginBottom: 20,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 20,
    padding: 20,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.12)',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 2,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: THEME.colors.textLight,
    marginBottom: 8, // Réduit de 20 à 8 pour alignement proche
  },
  inputGroup: {
    marginBottom: 25,
  },
  inputLabel: {
    fontSize: 14,
    color: THEME.colors.textMuted,
    fontWeight: '600',
    marginBottom: 10,
  },
  textInput: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 12,
    paddingVertical: 14,
    paddingHorizontal: 16,
    color: THEME.colors.textLight,
    fontSize: 16,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  textArea: {
    minHeight: 80,
    textAlignVertical: 'top',
  },
  phaseScroll: {
    marginHorizontal: -5,
  },
  phaseButton: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 14,
    paddingHorizontal: 18,
    marginHorizontal: 5,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 16,
    borderWidth: 2,
    borderColor: 'rgba(255, 255, 255, 0.1)',
    minWidth: 100,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  phaseButtonActive: {
    backgroundColor: 'rgba(255, 182, 193, 0.2)', // Saturation uniforme à 0.2
    borderColor: 'rgba(255, 182, 193, 0.95)', // Bordure lumineuse uniforme
    borderWidth: 2.5,
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.5, // Légèrement augmenté pour uniformité
    shadowRadius: 10, // Augmenté pour glow plus doux
    elevation: 6, // Augmenté pour Android
  },
  phaseEmoji: {
    fontSize: 28,
    marginBottom: 6,
  },
  phaseName: {
    fontSize: 13,
    color: THEME.colors.textMuted,
    fontWeight: '600',
    marginBottom: 2,
  },
  phaseNameActive: {
    color: THEME.colors.textLight,
    fontWeight: 'bold',
  },
  phaseDescription: {
    fontSize: 10,
    color: 'rgba(255,255,255,0.4)',
  },
  moodGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 10,
  },
  moodButton: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 12,
    paddingHorizontal: 16,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 14,
    borderWidth: 2,
    borderColor: 'rgba(255, 255, 255, 0.1)',
    minWidth: '30%',
    flexGrow: 1,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 3,
    elevation: 2,
  },
  moodButtonActive: {
    backgroundColor: 'rgba(255, 182, 193, 0.18)',
    borderColor: 'rgba(255, 182, 193, 0.9)',
    borderWidth: 2.5,
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.4,
    shadowRadius: 6,
    elevation: 3,
  },
  moodEmoji: {
    fontSize: 32,
    marginBottom: 6,
  },
  moodName: {
    fontSize: 12,
    color: THEME.colors.textMuted,
    fontWeight: '500',
  },
  moodNameActive: {
    color: THEME.colors.textLight,
    fontWeight: 'bold',
  },
  profileInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: 'rgba(16, 185, 129, 0.1)',
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderRadius: 12,
    marginBottom: 20,
  },
  profileInfoText: {
    fontSize: 14,
    color: '#10B981',
    fontWeight: '600',
  },
  completeProfileButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderRadius: 12,
    marginBottom: 20,
  },
  completeProfileText: {
    fontSize: 14,
    color: '#F59E0B',
    fontWeight: '600',
    flex: 1,
  },
  analyzeButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FFB6C1',
    paddingVertical: 18,
    borderRadius: 16,
    marginBottom: 25,
    gap: 10,
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.25)',
  },
  analyzeButtonDisabled: {
    opacity: 0.6,
  },
  analyzeButtonText: {
    color: '#111111cc', // Noir translucide pour meilleur contraste sur rose
    fontSize: 18,
    fontWeight: 'bold',
  },
  infoCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 12,
    backgroundColor: 'rgba(139, 92, 246, 0.1)',
    paddingVertical: 16,
    paddingHorizontal: 18,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  infoIcon: {
    fontSize: 24,
  },
  infoText: {
    flex: 1,
    fontSize: 13,
    color: THEME.colors.textMuted,
    lineHeight: 20,
  },
  // Résultats
  resultContainer: {
    gap: 20,
  },
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    paddingVertical: 12,
    paddingHorizontal: 16,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 12,
    alignSelf: 'flex-start',
  },
  backButtonText: {
    color: THEME.colors.textLight,
    fontSize: 16,
    fontWeight: '600',
  },
  mainCard: {
    backgroundColor: 'rgba(255, 255, 255, 0.12)',
    borderRadius: 24,
    padding: 30,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.3)',
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.2,
    shadowRadius: 16,
    elevation: 5,
  },
  mainEmoji: {
    fontSize: 64,
    marginBottom: 12,
  },
  mainTitle: {
    fontSize: 26,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 6,
    textShadowColor: 'rgba(255, 182, 193, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 8,
  },
  mainSubtitle: {
    fontSize: 14,
    color: THEME.colors.textMuted,
    marginBottom: 12,
  },
  countdownBadge: {
    backgroundColor: 'rgba(255, 107, 157, 0.2)',
    borderRadius: 12,
    paddingVertical: 6,
    paddingHorizontal: 12,
    alignSelf: 'center',
    marginBottom: 12,
  },
  countdownBadgeText: {
    fontSize: 12,
    color: '#FF6B9D',
    fontWeight: '600',
  },
  energyBar: {
    width: '100%',
    marginTop: 10,
  },
  energyBarLabel: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 8,
    paddingHorizontal: 6, // +6px pour éviter coller au bord
  },
  energyBarText: {
    fontSize: 13,
    color: THEME.colors.textMuted,
    fontWeight: '600',
  },
  energyBarValue: {
    fontSize: 16,
    color: THEME.colors.textLight,
    fontWeight: 'bold',
  },
  energyBarTrack: {
    height: 10,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 5,
    overflow: 'hidden',
  },
  energyBarFill: {
    height: '100%',
    backgroundColor: '#FFC8DD',
    borderRadius: 5,
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.5,
    shadowRadius: 6,
  },
  card: {
    backgroundColor: 'rgba(255, 255, 255, 0.09)',
    borderRadius: 20,
    padding: 20,
    borderWidth: 1,
    borderColor: 'rgba(192, 132, 252, 0.2)',
    shadowColor: '#C084FC',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 12,
    elevation: 3,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: 12,
    textShadowColor: 'rgba(255, 200, 221, 0.4)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
  },
  cardText: {
    fontSize: 14,
    color: THEME.colors.textMuted,
    lineHeight: 22,
    marginBottom: 15,
  },
  transitDetails: {
    gap: 10,
  },
  transitItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 12,
    paddingHorizontal: 16,
    backgroundColor: 'rgba(192, 132, 252, 0.1)',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: 'rgba(192, 132, 252, 0.2)',
  },
  transitLabel: {
    fontSize: 13,
    color: THEME.colors.textMuted,
  },
  transitValue: {
    fontSize: 14,
    color: THEME.colors.textLight,
    fontWeight: '600',
  },
  activityItem: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 12,
    marginBottom: 12,
    padding: 14,
    backgroundColor: 'rgba(255, 182, 193, 0.08)',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.15)',
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 1,
  },
  activityEmoji: {
    fontSize: 28,
  },
  activityContent: {
    flex: 1,
  },
  activityName: {
    fontSize: 15,
    fontWeight: 'bold',
    color: THEME.colors.textLight,
    marginBottom: 4,
  },
  activityDescription: {
    fontSize: 13,
    color: THEME.colors.textMuted,
    lineHeight: 18,
  },
  recommendationItem: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 12,
    marginBottom: 12,
    padding: 12,
    backgroundColor: 'rgba(255, 182, 193, 0.06)',
    borderRadius: 12,
    borderLeftWidth: 3,
    borderLeftColor: 'rgba(255, 182, 193, 0.4)',
  },
  recIcon: {
    fontSize: 20,
  },
  recText: {
    flex: 1,
    fontSize: 14,
    color: THEME.colors.textLight,
    lineHeight: 20,
  },
  legend: {
    backgroundColor: 'rgba(192, 132, 252, 0.12)',
    borderRadius: 16,
    padding: 18,
    borderWidth: 1,
    borderColor: 'rgba(192, 132, 252, 0.25)',
    shadowColor: '#C084FC',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.15,
    shadowRadius: 8,
    elevation: 2,
  },
  legendText: {
    fontSize: 12,
    color: THEME.colors.textMuted,
    lineHeight: 18,
    textAlign: 'center',
    fontStyle: 'italic',
  },
});

