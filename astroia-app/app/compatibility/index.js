import React, { useState, useEffect, useRef, useCallback } from 'react';
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
  TextInput,
  Share,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router, useLocalSearchParams, useFocusEffect } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useProfileStore } from '@/stores/profileStore';
import { analyzeCompatibility, saveCompatibilityAnalysis } from '@/lib/api/compatibilityAnalysisService';
import { useHapticFeedback } from '@/hooks/useHapticFeedback';
import NatalLockCard from '@/components/NatalLockCard';
import THEME from '@/constants/theme';

const ZODIAC_SIGNS = [
  { id: 1, name: 'Bélier', emoji: '♈' },
  { id: 2, name: 'Taureau', emoji: '♉' },
  { id: 3, name: 'Gémeaux', emoji: '♊' },
  { id: 4, name: 'Cancer', emoji: '♋' },
  { id: 5, name: 'Lion', emoji: '♌' },
  { id: 6, name: 'Vierge', emoji: '♍' },
  { id: 7, name: 'Balance', emoji: '♎' },
  { id: 8, name: 'Scorpion', emoji: '♏' },
  { id: 9, name: 'Sagittaire', emoji: '♐' },
  { id: 10, name: 'Capricorne', emoji: '♑' },
  { id: 11, name: 'Verseau', emoji: '♒' },
  { id: 12, name: 'Poissons', emoji: '♓' },
];

const RELATION_TYPES = [
  { id: 'couple', name: 'Couple', emoji: '💑', gradient: ['#ff5b8a', '#ff8aa8', '#ffa9c0'] }, // Gradient plus doux pour meilleure lisibilité
  { id: 'friends', name: 'Amis', emoji: '🤝', gradient: ['#FFB300', '#FF6F00', '#F57C00'] },
  { id: 'colleagues', name: 'Collègues', emoji: '💼', gradient: ['#00B0FF', '#0091EA', '#01579B'] },
];

export default function CompatibilityScreen() {
  const profile = useProfileStore((state) => state.profile);
  const getSunSign = useProfileStore((state) => state.getSunSign);
  const getAscendant = useProfileStore((state) => state.getAscendant);
  const getMoonSign = useProfileStore((state) => state.getMoonSign);
  const hasNatal = useProfileStore((state) => state.hasNatal);
  const getNatal = useProfileStore((state) => state.getNatal);
  
  const params = useLocalSearchParams();
  const [relationType, setRelationType] = useState(params.defaultType || null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  
  // Haptic feedback
  const haptic = useHapticFeedback();

  // Personne 1 (utilisateur)
  const [person1, setPerson1] = useState({
    name: '',
    sunSign: 1,
    moonSign: 1,
    ascendant: 1,
  });

  // Personne 2
  const [person2, setPerson2] = useState({
    name: '',
    sunSign: 1,
    moonSign: 1,
    ascendant: 1,
  });

  // Refs pour scroll et animations
  const scrollViewRef = useRef(null);
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const pulseAnim = useRef(new Animated.Value(1)).current;
  const zodiacScrollRefs = useRef({});
  const zodiacButtonLayouts = useRef({});

  // Pré-remplir à chaque fois qu'on arrive sur l'écran (uniquement si pas de thème natal)
  useFocusEffect(
    useCallback(() => {
      // Si thème natal complet existe, on ne pré-remplit pas (sera verrouillé)
      if (hasNatal()) {
        console.log('[Compatibility] Thème natal détecté, mode verrouillé');
        return;
      }
      
      // Sinon, pré-remplir avec les données disponibles (fallback)
      const userSunSign = getSunSign();
      const userAscendant = getAscendant();
      const userMoonSign = getMoonSign();
      
      console.log('[Compatibility] Pré-remplissage fallback (focus):', {
        sunSign: userSunSign,
        ascendant: userAscendant,
        moonSign: userMoonSign,
      });
      
      setPerson1({
        name: profile?.name || '',
        sunSign: userSunSign?.id || 1,
        ascendant: userAscendant?.id || 1,
        moonSign: userMoonSign?.id || 1,
      });
    }, [hasNatal, getSunSign, getAscendant, getMoonSign, profile?.name])
  );
  
  // Auto-scroll vers les signes sélectionnés
  useEffect(() => {
    scrollToSign('person1-sun', person1.sunSign);
  }, [person1.sunSign]);
  
  useEffect(() => {
    scrollToSign('person1-asc', person1.ascendant);
  }, [person1.ascendant]);
  
  useEffect(() => {
    scrollToSign('person1-moon', person1.moonSign);
  }, [person1.moonSign]);
  
  useEffect(() => {
    scrollToSign('person2-sun', person2.sunSign);
  }, [person2.sunSign]);
  
  useEffect(() => {
    scrollToSign('person2-asc', person2.ascendant);
  }, [person2.ascendant]);
  
  useEffect(() => {
    scrollToSign('person2-moon', person2.moonSign);
    
    // Auto-scroll vers le CTA après sélection du dernier picker (Lune P2)
    if (person2.moonSign && person2.sunSign && person2.ascendant) {
      setTimeout(() => {
        scrollViewRef.current?.scrollToEnd({ animated: true });
      }, 600); // Délai pour laisser le scroll des signes se finir
    }
  }, [person2.moonSign]);
  
  // Fonction pour scroller vers un signe
  const scrollToSign = (refKey, signId) => {
    console.log(`[Compatibility] scrollToSign(${refKey}, ${signId})`);
    
    if (!signId) {
      console.log(`[Compatibility] Pas de signId, skip scroll`);
      return;
    }
    
    // Délai plus long pour que les refs soient prêts
    setTimeout(() => {
      if (!zodiacScrollRefs.current[refKey]) {
        console.log(`[Compatibility] Ref ${refKey} pas encore prêt, retry...`);
        // Retry après 500ms si le ref n'est pas prêt
        setTimeout(() => scrollToSign(refKey, signId), 500);
        return;
      }
      
      const index = ZODIAC_SIGNS.findIndex(s => s.id === signId);
      console.log(`[Compatibility] Scroll ${refKey} vers index ${index} (signe ${signId})`);
      
      if (index >= 0) {
        const buttonWidth = 90;
        const xPosition = Math.max(0, (index - 1) * buttonWidth); // -1 pour centrer
        zodiacScrollRefs.current[refKey]?.scrollTo({
          x: xPosition,
          animated: true,
        });
      }
    }, 300); // Augmenté à 300ms
  };

  // (Chargement géré par useFocusEffect ci-dessus)

  // Animations du résultat
  useEffect(() => {
    if (!result) return;

    scrollViewRef.current?.scrollTo({ y: 0, animated: true });

    fadeAnim.setValue(0);
    pulseAnim.setValue(1);

    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 600,
      useNativeDriver: true,
    }).start();

    if (result.globalScore >= 80) {
      Animated.loop(
        Animated.sequence([
          Animated.timing(pulseAnim, {
            toValue: 1.12,
            duration: 1000,
            useNativeDriver: true,
          }),
          Animated.timing(pulseAnim, {
            toValue: 1,
            duration: 1000,
            useNativeDriver: true,
          }),
        ])
      ).start();
    }
  }, [result]);

  const handleAnalyze = async () => {
    if (!relationType) {
      Alert.alert('Type de relation', 'Veuillez sélectionner un type de relation');
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      // Construire person1 : depuis thème natal si disponible, sinon depuis pickers
      let person1Data;
      let person1Source;
      
      if (hasNatal()) {
        const natal = getNatal();
        person1Data = {
          name: profile?.name || '',
          sunSign: natal.sun,
          moonSign: natal.moon,
          ascendant: natal.asc,
        };
        person1Source = 'natal';
        console.log('[Compatibility] Analyse avec données du thème natal (verrouillé)');
      } else {
        person1Data = person1;
        person1Source = 'manual';
        console.log('[Compatibility] Analyse avec données manuelles (fallback)');
      }

      const analysisResult = await analyzeCompatibility(person1Data, person2, relationType);
      setResult(analysisResult);

      // Sauvegarder en LOCAL (AsyncStorage)
      const timestamp = Date.now();
      const analysisToSave = {
        id: `analysis_compat_${timestamp}`,
        person1: person1Data,
        person1_source: person1Source, // 🆕 Source des données P1
        person2,
        relationType,
        globalScore: analysisResult.globalScore,
        created_at: new Date().toISOString(),
        ...analysisResult,
      };
      
      AsyncStorage.setItem(`analysis_compat_${timestamp}`, JSON.stringify(analysisToSave))
        .then(() => console.log('[Compatibility] Saved to AsyncStorage'))
        .catch(err => console.log('[Compatibility] Save failed:', err));

      // Sauvegarder dans Supabase aussi (silencieusement)
      saveCompatibilityAnalysis({
        person1: person1Data,
        person1_source: person1Source,
        person2,
        relationType,
        result: analysisResult,
      }).catch(err => console.log('Supabase save failed:', err));
    } catch (error) {
      console.error('Analyze error:', error);
      Alert.alert('Erreur', 'Impossible d\'analyser la compatibilité');
    } finally {
      setLoading(false);
    }
  };

  const handleShare = async () => {
    if (!result) return;

    const { globalScore, interpretation, detailedScores, strengths, warnings, advice, person1: p1, person2: p2 } = result;
    const typeEmoji = RELATION_TYPES.find(t => t.id === relationType)?.emoji || '💫';
    const typeLabel = relationType === 'couple' ? 'Amoureuse' : relationType === 'friends' ? 'Amicale' : 'Professionnelle';

    // Construction du message enrichi
    let message = `${typeEmoji} Compatibilité ${typeLabel} sur LUNA

${p1.name || 'Moi'} (${p1.sun}) × ${p2.name || 'Autre'} (${p2.sun})

${interpretation.emoji} ${globalScore}% - ${interpretation.title}
${interpretation.description}

📊 Analyse détaillée :
💬 Communication : ${detailedScores.communication}%
🔥 Passion/Énergie : ${detailedScores.passion}%
🤝 Complicité : ${detailedScores.complicity}%
🎯 Objectifs : ${detailedScores.goals}%`;

    // Ajouter les points forts
    if (strengths && strengths.length > 0) {
      message += `\n\n✨ Points forts :\n`;
      strengths.forEach(s => {
        message += `${s.icon} ${s.text}\n`;
      });
    }

    // Ajouter les points d'attention
    if (warnings && warnings.length > 0) {
      message += `\n⚠️ Points d'attention :\n`;
      warnings.forEach(w => {
        message += `${w.icon} ${w.text}\n`;
      });
    }

    // Ajouter les conseils
    if (advice && advice.length > 0) {
      message += `\n💡 Conseils :\n`;
      advice.forEach(a => {
        message += `• ${a}\n`;
      });
    }

    message += `\n✨ Découvre ta compatibilité sur LUNA !`;

    try {
      await Share.share({ message, title: 'Ma compatibilité LUNA' });
    } catch (error) {
      console.error('Share error:', error);
    }
  };

  const renderTypeSelection = () => (
    <View style={styles.typeSelection}>
      <Text style={styles.sectionTitle}>Quel type de relation ?</Text>
      <View style={styles.typeCards}>
        {RELATION_TYPES.map((type) => (
          <TouchableOpacity
            key={type.id}
            style={[
              styles.typeCard,
              relationType === type.id && styles.typeCardActive,
            ]}
            onPress={() => {
              haptic.selection();
              setRelationType(type.id);
            }}
          >
            <Text style={styles.typeEmoji}>{type.emoji}</Text>
            <Text style={[
              styles.typeName,
              relationType === type.id && styles.typeNameActive,
            ]}>
              {type.name}
            </Text>
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );

  const renderZodiacPicker = (title, value, onChange, autoFilled = null, refKey) => {
    return (
      <View style={styles.pickerSection}>
        <View style={styles.pickerHeader}>
          <Text style={styles.pickerTitle}>{title}</Text>
          {autoFilled && (
            <View style={styles.autoFillBadgeSmall}>
              <Ionicons name="checkmark-circle" size={12} color="#10B981" />
              <Text style={styles.autoFillTextSmall}>Auto</Text>
            </View>
          )}
        </View>
        <ScrollView 
          ref={(ref) => zodiacScrollRefs.current[refKey] = ref}
          horizontal 
          showsHorizontalScrollIndicator={false}
        >
          {ZODIAC_SIGNS.map((sign) => (
            <TouchableOpacity
              key={sign.id}
              style={[
                styles.zodiacButton,
                value === sign.id && styles.zodiacButtonActive,
              ]}
              onPress={() => onChange(sign.id)}
            >
              <Text style={styles.zodiacEmoji}>{sign.emoji}</Text>
              <Text style={[
                styles.zodiacName,
                value === sign.id && styles.zodiacNameActive,
              ]}>
                {sign.name}
              </Text>
            </TouchableOpacity>
          ))}
        </ScrollView>
      </View>
    );
  };

  const renderResult = () => {
    if (!result) return null;

    const { globalScore, interpretation, detailedScores, strengths, warnings, advice } = result;
    const selectedType = RELATION_TYPES.find(t => t.id === relationType);

    return (
      <Animated.View style={[styles.resultContainer, { opacity: fadeAnim }]}>
        {/* Score principal */}
        <View style={styles.scoreCard}>
          <Animated.Text style={[styles.scoreEmoji, { transform: [{ scale: pulseAnim }] }]}>
            {interpretation.emoji}
          </Animated.Text>
          <Text style={styles.scoreValue}>{globalScore}%</Text>
          <Text style={styles.scoreTitle}>{interpretation.title}</Text>
          <Text style={styles.scoreDescription}>{interpretation.description}</Text>
        </View>

        {/* Scores détaillés */}
        <View style={styles.detailedSection}>
          <Text style={styles.detailedTitle}>📊 Analyse détaillée</Text>
          {renderScoreBar('💬', 'Communication', detailedScores.communication)}
          {renderScoreBar('🔥', 'Passion/Énergie', detailedScores.passion)}
          {renderScoreBar('🤝', 'Complicité', detailedScores.complicity)}
          {renderScoreBar('🎯', 'Objectifs', detailedScores.goals)}
        </View>

        {/* Points forts */}
        {strengths && strengths.length > 0 && (
          <View style={styles.strengthsSection}>
            <Text style={styles.strengthsTitle}>✨ Points forts</Text>
            {strengths.map((strength, index) => (
              <View key={index} style={styles.strengthCard}>
                <Text style={styles.strengthIcon}>{strength.icon}</Text>
                <Text style={styles.strengthText}>{strength.text}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Points d'attention */}
        {warnings && warnings.length > 0 && (
          <View style={styles.warningsSection}>
            <Text style={styles.warningsTitle}>⚠️ Points d'attention</Text>
            {warnings.map((warning, index) => (
              <View key={index} style={styles.warningCard}>
                <Text style={styles.warningIcon}>{warning.icon}</Text>
                <Text style={styles.warningText}>{warning.text}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Conseils */}
        {advice && advice.length > 0 && (
          <View style={styles.adviceSection}>
            <Text style={styles.adviceTitle}>💡 Conseils</Text>
            {advice.map((tip, index) => (
              <Text key={index} style={styles.adviceText}>• {tip}</Text>
            ))}
          </View>
        )}

        {/* Boutons d'action */}
        <View style={styles.actionButtons}>
          <TouchableOpacity style={styles.shareButton} onPress={() => {
            haptic.impact.light();
            handleShare();
          }}>
            <Ionicons name="share-social" size={20} color="#fff" />
            <Text style={styles.shareButtonText}>Partager</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.newAnalysisButton}
            onPress={() => setResult(null)}
          >
            <Text style={styles.newAnalysisButtonText}>Nouvelle analyse</Text>
          </TouchableOpacity>
        </View>
      </Animated.View>
    );
  };

  const scoreColors = {
    'Communication': '#4DA3FF',
    'Passion/Énergie': '#FF6B6B',
    'Complicité': '#30CF7B',
    'Objectifs': '#FFC857',
  };

  const renderScoreBar = (icon, label, score) => (
    <View style={styles.scoreBarContainer}>
      <View style={styles.scoreBarHeader}>
        <Text style={styles.scoreBarIcon}>{icon}</Text>
        <Text style={styles.scoreBarLabel}>{label}</Text>
        <Text style={styles.scoreBarValue}>{score}%</Text>
      </View>
      <View style={styles.scoreBarTrack}>
        <View 
          style={[
            styles.scoreBarFill, 
            { 
              width: `${score}%`,
              backgroundColor: scoreColors[label] || '#fff', // Couleur différenciée par type
            }
          ]} 
        />
      </View>
    </View>
  );

  const getCurrentGradient = () => {
    if (!relationType) return THEME.colors.gradientDark;
    return RELATION_TYPES.find(t => t.id === relationType)?.gradient || THEME.colors.gradientDark;
  };

  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={getCurrentGradient()} style={styles.container}>
        <SafeAreaView style={styles.safeArea}>
          <Stack.Screen
            options={{
              title: 'Compatibilité',
              headerStyle: { backgroundColor: 'transparent' },
              headerTintColor: '#fff',
              headerShadowVisible: false,
            }}
          />

          <View style={styles.header}>
            <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
              <Ionicons name="arrow-back" size={24} color="#fff" />
              <Text style={styles.backButtonText}>Retour</Text>
            </TouchableOpacity>
          </View>

          <ScrollView
            ref={scrollViewRef}
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
          >
            {!result ? (
              <>
                {/* Header */}
                <View style={styles.headerSection}>
                  <Text style={styles.headerTitle}>💕 Analyse de Compatibilité</Text>
                  <Text style={styles.headerSubtitle}>
                    Découvrez votre compatibilité astrologique complète
                  </Text>
                </View>

                {/* Sélection du type */}
                {renderTypeSelection()}

                {relationType && (
                  <>
                    {/* Personne 1 (Vous) - Verrouillé si thème natal existe */}
                    {hasNatal() ? (
                      // Mode verrouillé : afficher le NatalLockCard
                      <View style={styles.section}>
                        <Text style={styles.sectionTitle}>👤 Vous</Text>
                        <NatalLockCard natal={getNatal()} />
                      </View>
                    ) : (
                      // Mode fallback : afficher les pickers manuels
                      <View style={styles.section}>
                        <Text style={styles.sectionTitle}>👤 Vous</Text>
                        <TextInput
                          style={styles.nameInput}
                          placeholder="Votre prénom (optionnel)"
                          placeholderTextColor="rgba(255,255,255,0.5)"
                          value={person1.name}
                          onChangeText={(name) => setPerson1({ ...person1, name })}
                        />
                        {renderZodiacPicker('Signe solaire', person1.sunSign, (v) =>
                          setPerson1({ ...person1, sunSign: v })
                        , getSunSign() ? 'auto' : null, 'person1-sun')}
                        {renderZodiacPicker('Ascendant', person1.ascendant, (v) =>
                          setPerson1({ ...person1, ascendant: v })
                        , getAscendant() ? 'auto' : null, 'person1-asc')}
                        {renderZodiacPicker('Signe lunaire', person1.moonSign, (v) =>
                          setPerson1({ ...person1, moonSign: v })
                        , getMoonSign() ? 'auto' : null, 'person1-moon')}
                      </View>
                    )}

                    {/* Personne 2 */}
                    <View style={styles.section}>
                      <Text style={styles.sectionTitle}>👤 Autre personne</Text>
                      <TextInput
                        style={styles.nameInput}
                        placeholder="Prénom (optionnel)"
                        placeholderTextColor="rgba(255,255,255,0.5)"
                        value={person2.name}
                        onChangeText={(name) => setPerson2({ ...person2, name })}
                      />
                      {renderZodiacPicker('Signe solaire', person2.sunSign, (v) =>
                        setPerson2({ ...person2, sunSign: v })
                      , null, 'person2-sun')}
                      {renderZodiacPicker('Ascendant', person2.ascendant, (v) =>
                        setPerson2({ ...person2, ascendant: v })
                      , null, 'person2-asc')}
                      {renderZodiacPicker('Signe lunaire', person2.moonSign, (v) =>
                        setPerson2({ ...person2, moonSign: v })
                      , null, 'person2-moon')}
                    </View>

                    {/* Bouton Analyser */}
                    <TouchableOpacity
                      style={[styles.analyzeButton, loading && styles.analyzeButtonDisabled]}
                      onPress={() => {
                        haptic.impact.medium();
                        handleAnalyze();
                      }}
                      disabled={loading}
                    >
                      {loading ? (
                        <ActivityIndicator color="#fff" />
                      ) : (
                        <>
                          <Ionicons name="analytics" size={24} color="#fff" />
                          <Text style={styles.analyzeButtonText}>Analyser la compatibilité</Text>
                        </>
                      )}
                    </TouchableOpacity>
                  </>
                )}
              </>
            ) : (
              renderResult()
            )}
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
    gap: 8,
    paddingVertical: 10,
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
    paddingTop: 5,
    paddingBottom: 60,
  },
  headerSection: {
    alignItems: 'center',
    marginBottom: 25,
  },
  headerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 8,
  },
  headerSubtitle: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.8)',
    textAlign: 'center',
  },
  typeSelection: {
    marginBottom: 25,
  },
  sectionHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 15,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
  },
  autoFillBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: 'rgba(16, 185, 129, 0.15)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: 'rgba(16, 185, 129, 0.3)',
  },
  autoFillText: {
    fontSize: 12,
    color: '#10B981',
    fontWeight: '600',
  },
  autoFillBadgeSmall: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 3,
    backgroundColor: 'rgba(16, 185, 129, 0.15)',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: 'rgba(16, 185, 129, 0.3)',
  },
  autoFillTextSmall: {
    fontSize: 10,
    color: '#10B981',
    fontWeight: '600',
  },
  pickerHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  typeCards: {
    flexDirection: 'row',
    gap: 12,
  },
  typeCard: {
    flex: 1,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 16,
    padding: 20,
    alignItems: 'center',
    borderWidth: 2,
    borderColor: 'transparent',
  },
  typeCardActive: {
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    borderColor: '#fff',
  },
  typeEmoji: {
    fontSize: 36,
    marginBottom: 8,
  },
  typeName: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.7)',
    fontWeight: '600',
  },
  typeNameActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  section: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
  },
  nameInput: {
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    borderRadius: 12,
    paddingVertical: 14,
    paddingHorizontal: 16,
    color: '#fff',
    fontSize: 16,
    marginBottom: 15,
  },
  pickerSection: {
    marginBottom: 15,
  },
  pickerTitle: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.8)',
    marginBottom: 10,
    fontWeight: '600',
  },
  zodiacButton: {
    alignItems: 'center',
    paddingVertical: 10,
    paddingHorizontal: 14,
    marginRight: 10,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 12,
    borderWidth: 2,
    borderColor: 'transparent',
  },
  zodiacButtonActive: {
    backgroundColor: 'rgba(255, 255, 255, 0.25)',
    borderColor: '#fff',
  },
  zodiacEmoji: {
    fontSize: 24,
    marginBottom: 4,
  },
  zodiacName: {
    fontSize: 11,
    color: 'rgba(255,255,255,0.7)',
  },
  zodiacNameActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  analyzeButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.25)',
    paddingVertical: 18,
    borderRadius: 16,
    marginTop: 10,
    marginBottom: 20,
    gap: 10,
    shadowColor: '#fff',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  analyzeButtonDisabled: {
    opacity: 0.6,
  },
  analyzeButtonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  resultContainer: {
    gap: 20,
  },
  scoreCard: {
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    borderRadius: 20,
    padding: 30,
    alignItems: 'center',
  },
  scoreEmoji: {
    fontSize: 60,
    marginBottom: 10,
  },
  scoreValue: {
    fontSize: 72,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 10,
  },
  scoreTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 10,
    textAlign: 'center',
  },
  scoreDescription: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.9)',
    textAlign: 'center',
    lineHeight: 20,
  },
  detailedSection: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 16,
    padding: 20,
  },
  detailedTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 20,
  },
  scoreBarContainer: {
    marginBottom: 16,
  },
  scoreBarHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
    gap: 8,
  },
  scoreBarIcon: {
    fontSize: 20,
  },
  scoreBarLabel: {
    flex: 1,
    fontSize: 14,
    color: '#fff',
    fontWeight: '600',
  },
  scoreBarValue: {
    fontSize: 16,
    color: '#fff',
    fontWeight: 'bold',
  },
  scoreBarTrack: {
    height: 8,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    borderRadius: 4,
    overflow: 'hidden',
  },
  scoreBarFill: {
    height: '100%',
    backgroundColor: '#fff',
    borderRadius: 4,
  },
  strengthsSection: {
    backgroundColor: 'rgba(16, 185, 129, 0.15)',
    borderRadius: 16,
    padding: 20,
  },
  strengthsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 15,
  },
  strengthCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 12,
    gap: 10,
  },
  strengthIcon: {
    fontSize: 20,
  },
  strengthText: {
    flex: 1,
    fontSize: 14,
    color: '#fff',
    lineHeight: 20,
  },
  warningsSection: {
    backgroundColor: 'rgba(251, 191, 36, 0.15)',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20, // Espacement avec section suivante
  },
  warningsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 15,
  },
  warningCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 12,
    gap: 10,
  },
  warningIcon: {
    fontSize: 20,
  },
  warningText: {
    flex: 1,
    fontSize: 14,
    color: '#fff',
    lineHeight: 20,
  },
  adviceSection: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 16,
    padding: 20,
  },
  adviceTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 15,
  },
  adviceText: {
    fontSize: 14,
    color: '#fff',
    lineHeight: 22,
    marginBottom: 8,
  },
  actionButtons: {
    flexDirection: 'row',
    gap: 12,
  },
  shareButton: {
    backgroundColor: 'rgba(255, 255, 255, 0.25)',
    paddingVertical: 14,
    paddingHorizontal: 20,
    borderRadius: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    flex: 1,
  },
  shareButtonText: {
    color: '#fff',
    fontSize: 15,
    fontWeight: '600',
  },
  newAnalysisButton: {
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    paddingVertical: 14,
    borderRadius: 12,
    alignItems: 'center',
    flex: 1,
  },
  newAnalysisButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});
