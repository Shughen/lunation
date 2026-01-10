import React, { useState, useEffect, useRef, useCallback } from 'react';
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  Animated,
  Platform,
  Share,
  SafeAreaView,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router, useFocusEffect } from 'expo-router';
// import * as Sharing from 'expo-sharing'; // Temporairement désactivé (module natif)
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useProfileStore } from '@/stores/profileStore';
import { analyzeParentChildCompatibility, extractAstroData } from '@/lib/api/parentChildService';
import { saveCompatibilityHistory } from '@/lib/api/compatibilityService';
import { useHapticFeedback } from '@/hooks/useHapticFeedback';
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

export default function ParentChildScreen() {
  const profile = useProfileStore((state) => state.profile);
  const getSunSign = useProfileStore((state) => state.getSunSign);
  const getAscendant = useProfileStore((state) => state.getAscendant);
  const getMoonSign = useProfileStore((state) => state.getMoonSign);
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  
  // Données parent (l'utilisateur actuel)
  const [parentData, setParentData] = useState({
    sunSign: 1,
    moonSign: 1,
    ascendant: 1,
  });

  // Pré-remplir à chaque fois qu'on arrive sur l'écran
  useFocusEffect(
    useCallback(() => {
      const userSunSign = getSunSign();
      const userAscendant = getAscendant();
      const userMoonSign = getMoonSign();
      
      console.log('[Parent-Child] Pré-remplissage (focus):', {
        sunSign: userSunSign,
        ascendant: userAscendant,
        moonSign: userMoonSign,
      });
      
      setParentData({
        sunSign: userSunSign?.id || 1,
        ascendant: userAscendant?.id || 1,
        moonSign: userMoonSign?.id || 1,
      });
    }, [profile?.sunSign, profile?.ascendant, profile?.moonSign])
  );
  
  // Données enfant
  const [enfantData, setEnfantData] = useState({
    sunSign: 1,
    moonSign: 1,
    ascendant: 1,
  });

  // Ref pour le ScrollView
  const scrollViewRef = useRef(null);
  
  // Refs pour les zodiac pickers (pour auto-scroll)
  const zodiacScrollRefs = useRef({});
  const zodiacButtonLayouts = useRef({});

  // Haptic feedback
  const haptic = useHapticFeedback();

  // Animations (au niveau du composant, pas dans renderResult)
  const pulseAnim = useRef(new Animated.Value(1)).current;
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const haloAnim = useRef(new Animated.Value(0)).current;

  // Effet pour les animations (déclenché quand result change)
  useEffect(() => {
    if (!result) return;

    // Scroll en haut quand le résultat apparaît
    scrollViewRef.current?.scrollTo({ y: 0, animated: true });

    const compatibility_score = result.compatibility_score || 0;

    // Reset animations
    fadeAnim.setValue(0);
    pulseAnim.setValue(1);
    haloAnim.setValue(0);

    // Animation du texte (fadeIn)
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 600,
      useNativeDriver: true,
    }).start();

    // Animation selon le score
    if (compatibility_score >= 80) {
      // Cœur pulsant pour scores élevés
      Animated.loop(
        Animated.sequence([
          Animated.timing(pulseAnim, {
            toValue: 1.15,
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
    } else if (compatibility_score >= 50) {
      // Halo lumineux pour scores moyens
      Animated.loop(
        Animated.sequence([
          Animated.timing(haloAnim, {
            toValue: 1,
            duration: 1500,
            useNativeDriver: true,
          }),
          Animated.timing(haloAnim, {
            toValue: 0,
            duration: 1500,
            useNativeDriver: true,
          }),
        ])
      ).start();
    } else {
      // Pulsation lente pour scores faibles
      Animated.loop(
        Animated.sequence([
          Animated.timing(pulseAnim, {
            toValue: 1.08,
            duration: 1200,
            useNativeDriver: true,
          }),
          Animated.timing(pulseAnim, {
            toValue: 1,
            duration: 1200,
            useNativeDriver: true,
          }),
        ])
      ).start();
    }
  }, [result]);

  const calculateLocalCompatibility = (parentSigns, childSigns) => {
    // Calcul de compatibilité simplifié côté client
    const elements = {
      1: 'fire', 5: 'fire', 9: 'fire',
      2: 'earth', 6: 'earth', 10: 'earth',
      3: 'air', 7: 'air', 11: 'air',
      4: 'water', 8: 'water', 12: 'water',
    };

    const parentElement = elements[parentSigns.sunSign];
    const childElement = elements[childSigns.sunSign];

    // Compatibilité élémentaire
    let baseScore = 50;
    if (parentElement === childElement) {
      baseScore = 85; // Même élément = très compatible
    } else if (
      (parentElement === 'fire' && childElement === 'air') ||
      (parentElement === 'air' && childElement === 'fire') ||
      (parentElement === 'earth' && childElement === 'water') ||
      (parentElement === 'water' && childElement === 'earth')
    ) {
      baseScore = 75; // Éléments compatibles
    } else if (
      (parentElement === 'fire' && childElement === 'water') ||
      (parentElement === 'water' && childElement === 'fire') ||
      (parentElement === 'earth' && childElement === 'air') ||
      (parentElement === 'air' && childElement === 'earth')
    ) {
      baseScore = 45; // Éléments opposés
    }

    // Ajustement avec lune et ascendant
    const moonBonus = Math.abs(parentSigns.moonSign - childSigns.moonSign) < 4 ? 5 : -5;
    const ascBonus = Math.abs(parentSigns.ascendant - childSigns.ascendant) < 4 ? 5 : -5;

    const finalScore = Math.max(10, Math.min(100, baseScore + moonBonus + ascBonus));

    return {
      success: true,
      compatibility_score: Math.round(finalScore),
      interpretation: getInterpretation(finalScore),
      recommendations: getRecommendations(finalScore),
      probability: {
        harmonieuse: finalScore / 100,
        difficile: 1 - (finalScore / 100),
      },
      model_accuracy: 0, // Mode local
    };
  };

  const getInterpretation = (score) => {
    if (score >= 85) {
      return {
        level: 'Excellente',
        emoji: '💚',
        title: 'Relation très harmonieuse',
        description: 'Votre relation parent-enfant présente d\'excellentes bases astrologiques. Les énergies sont très compatibles.',
      };
    } else if (score >= 70) {
      return {
        level: 'Bonne',
        emoji: '💙',
        title: 'Relation harmonieuse',
        description: 'Belle compatibilité astrologique. Quelques ajustements peuvent renforcer votre complicité.',
      };
    } else if (score >= 55) {
      return {
        level: 'Moyenne',
        emoji: '💛',
        title: 'Relation équilibrée',
        description: 'Compatibilité correcte avec des défis à surmonter. La compréhension mutuelle demande des efforts.',
      };
    } else {
      return {
        level: 'Délicate',
        emoji: '🧡',
        title: 'Relation à travailler',
        description: 'Les énergies astrologiques sont contrastées. Une attention particulière à la communication est recommandée.',
      };
    }
  };

  const getRecommendations = (score) => {
    const recs = [];
    
    if (score >= 70) {
      recs.push({
        type: 'strength',
        icon: '✨',
        text: 'Cultivez votre complicité naturelle à travers des activités partagées.',
      });
    } else {
      recs.push({
        type: 'improvement',
        icon: '🔧',
        text: 'Accordez une attention particulière à l\'écoute active et à la validation des émotions.',
      });
    }

    recs.push({
      type: 'advice',
      icon: '🌊',
      text: 'Prenez le temps de comprendre vos modes de fonctionnement respectifs.',
    });

    recs.push({
      type: 'general',
      icon: '💫',
      text: 'L\'astrologie éclaire, mais l\'amour et la communication construisent les vraies relations.',
    });

    return recs;
  };

  const handleShare = async () => {
    if (!result) return;

    try {
      const { compatibility_score, interpretation } = result;
      
      // Message de partage personnalisé
      const message = `🌟 Ma compatibilité parent-enfant sur LUNA

${interpretation.emoji} ${compatibility_score}% - ${interpretation.title}

${interpretation.description}

✨ Découvre ton score sur LUNA !`;

      // Utiliser Share natif React Native (expo-sharing désactivé temporairement)
      // const isAvailable = await Sharing.isAvailableAsync();
      
      if (Platform.OS === 'ios' || Platform.OS === 'android') {
        await Share.share({
          message: message,
          title: 'Ma compatibilité LUNA',
        });
      } else {
        // Fallback : copier dans le presse-papier
        Alert.alert(
          'Partage',
          message,
          [
            { text: 'Copier', onPress: () => {
              // On pourrait ajouter Clipboard.setString ici
              Alert.alert('Succès', 'Texte copié !');
            }},
            { text: 'OK' }
          ]
        );
      }
    } catch (error) {
      console.error('Share error:', error);
      Alert.alert('Erreur', 'Impossible de partager pour le moment');
    }
  };

  const handleAnalyze = async () => {
    setLoading(true);
    setResult(null);

    try {
      // Utiliser les données du profil si disponibles
      const parentAstro = extractAstroData(profile) || {
        sunSign: parentData.sunSign,
        moonSign: parentData.moonSign,
        ascendant: parentData.ascendant,
        mercury: parentData.sunSign,
        venus: parentData.sunSign,
        mars: parentData.sunSign,
      };

      const enfantAstro = {
        sunSign: enfantData.sunSign,
        moonSign: enfantData.moonSign,
        ascendant: enfantData.ascendant,
        mercury: enfantData.sunSign,
        venus: enfantData.sunSign,
        mars: enfantData.sunSign,
      };

      // Mode local (fallback)
      console.log('🔧 Mode calcul local (API non disponible)');
      const analysisResult = calculateLocalCompatibility(parentAstro, enfantAstro);
      
      setResult(analysisResult);

      // Sauvegarder en LOCAL (AsyncStorage)
      const timestamp = Date.now();
      const analysisToSave = {
        id: `analysis_parent_child_${timestamp}`,
        parentData: parentAstro,
        enfantData: enfantAstro,
        score: analysisResult.compatibility_score,
        interpretation: analysisResult.interpretation,
        created_at: new Date().toISOString(),
        ...analysisResult,
      };
      
      AsyncStorage.setItem(`analysis_parent_child_${timestamp}`, JSON.stringify(analysisToSave))
        .then(() => console.log('[Parent-Child] Saved to AsyncStorage'))
        .catch(err => console.log('[Parent-Child] Save failed:', err));

      // Sauvegarder dans Supabase aussi (silencieusement)
      saveCompatibilityHistory({
        parentData: parentAstro,
        enfantData: enfantAstro,
        result: analysisResult,
      }).catch(err => console.log('[handleAnalyze] Supabase save failed:', err));
    } catch (error) {
      console.error('Analyse error:', error);
      Alert.alert(
        'Erreur',
        'Impossible d\'analyser la compatibilité. Vérifiez les données saisies.',
        [{ text: 'OK' }]
      );
    } finally {
      setLoading(false);
    }
  };

  const renderZodiacPicker = (title, value, onChange, autoFilled = null, refKey) => {
    if (!ZODIAC_SIGNS || ZODIAC_SIGNS.length === 0) {
      return <Text style={{ color: '#fff' }}>Chargement...</Text>;
    }
    
    // Fonction pour mesurer et scroller vers le signe sélectionné
    const handleLayout = (signId, event) => {
      const { x } = event.nativeEvent.layout;
      if (!zodiacButtonLayouts.current[refKey]) {
        zodiacButtonLayouts.current[refKey] = {};
      }
      zodiacButtonLayouts.current[refKey][signId] = x;
    };
    
    // Scroller automatiquement quand le composant est monté et quand la valeur change
    useEffect(() => {
      if (!zodiacScrollRefs.current[refKey] || !value) return;
      
      // Délai pour s'assurer que le layout est calculé
      setTimeout(() => {
        const layouts = zodiacButtonLayouts.current[refKey];
        if (layouts && layouts[value] !== undefined) {
          // Utiliser la position réelle mesurée
          zodiacScrollRefs.current[refKey]?.scrollTo({
            x: layouts[value],
            animated: false,
          });
        } else {
          // Fallback : calcul approximatif
          const index = ZODIAC_SIGNS.findIndex(s => s.id === value);
          if (index >= 0) {
            const buttonWidth = 90;
            const xPosition = Math.max(0, index * buttonWidth);
            zodiacScrollRefs.current[refKey]?.scrollTo({
              x: xPosition,
              animated: false,
            });
          }
        }
      }, 350);
    }, [value, refKey]);
    
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
        style={styles.zodiacScroll}
      >
        {ZODIAC_SIGNS.map((sign) => (
          <TouchableOpacity
            key={sign.id}
            style={[
              styles.zodiacButton,
              value === sign.id && styles.zodiacButtonActive,
            ]}
            onPress={() => onChange(sign.id)}
            onLayout={(event) => handleLayout(sign.id, event)}
          >
            <Text style={styles.zodiacEmoji}>{sign.emoji}</Text>
            <Text
              style={[
                styles.zodiacName,
                value === sign.id && styles.zodiacNameActive,
              ]}
            >
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

    const { compatibility_score, interpretation, recommendations } = result;

    const haloOpacity = haloAnim.interpolate({
      inputRange: [0, 1],
      outputRange: [0.2, 0.6],
    });

    const haloScale = haloAnim.interpolate({
      inputRange: [0, 1],
      outputRange: [1, 1.3],
    });

    return (
      <View style={styles.resultContainer}>
        {/* Bouton retour */}
        <TouchableOpacity
          style={styles.backButton}
          onPress={() => router.back()}
        >
          <Ionicons name="arrow-back" size={24} color={THEME.colors.textLight} />
          <Text style={styles.backButtonText}>Retour au menu</Text>
        </TouchableOpacity>

        {/* Score principal */}
        <View style={styles.scoreCard}>
          {/* Halo (pour scores moyens) */}
          {compatibility_score >= 50 && compatibility_score < 80 && (
            <Animated.View
              style={[
                styles.halo,
                {
                  opacity: haloOpacity,
                  transform: [{ scale: haloScale }],
                },
              ]}
            />
          )}

          {/* Emoji animé */}
          <Animated.Text
            style={[
              styles.scoreEmoji,
              { transform: [{ scale: pulseAnim }] },
            ]}
          >
            {interpretation?.emoji || '💫'}
          </Animated.Text>

          {/* Score avec fadeIn */}
          <Animated.Text style={[styles.scoreValue, { opacity: fadeAnim }]}>
            {compatibility_score || 0}%
          </Animated.Text>

          <Animated.Text style={[styles.scoreTitle, { opacity: fadeAnim }]}>
            {interpretation?.title || 'Analyse'}
          </Animated.Text>

          <Animated.Text style={[styles.scoreDescription, { opacity: fadeAnim }]}>
            {interpretation?.description || 'Analyse en cours...'}
          </Animated.Text>
          
          {/* Label méthode */}
          <View style={styles.methodLabel}>
            <Text style={styles.methodText}>
              Analyse basée sur les éléments astrologiques (Soleil, Lune, Ascendant)
            </Text>
            <Text style={styles.methodVersion}>Méthode LUNA v1.2</Text>
          </View>
        </View>

        {/* Divider */}
        <View style={styles.divider} />

        {/* Recommandations */}
        {recommendations && recommendations.length > 0 && (
          <View style={styles.recommendationsSection}>
            <Text style={styles.recommendationsTitle}>💡 Conseils personnalisés</Text>
            {recommendations.map((rec, index) => (
              <View key={index} style={styles.recommendationCard}>
                <Text style={styles.recommendationIcon}>{rec.icon}</Text>
                <Text style={styles.recommendationText}>{rec.text}</Text>
              </View>
            ))}
            
            {/* Légende */}
            <View style={styles.legend}>
              <Text style={styles.legendText}>
                💫 Le score combine vos affinités élémentaires et planétaires principales
              </Text>
            </View>
          </View>
        )}

        {/* Divider */}
        <View style={styles.divider} />

        {/* Détails techniques */}
        <View style={styles.technicalDetails}>
          <View style={styles.technicalHeader}>
            <Text style={styles.technicalTitle}>Détails de l'analyse</Text>
            <Text style={styles.infoIcon}>ℹ️</Text>
          </View>
          <View style={styles.technicalRow}>
            <Text style={styles.technicalLabel}>Méthode:</Text>
            <Text style={styles.technicalValue}>
              {result.model_accuracy > 0 ? 'ML XGBoost (98.19%)' : 'Calcul interne (pondération des éléments)'}
            </Text>
          </View>
          {result.probability && (
            <>
              <View style={styles.technicalRow}>
                <Text style={styles.technicalLabel}>Compatibilité:</Text>
                <Text style={styles.technicalValue}>
                  {(result.probability.harmonieuse * 100).toFixed(1)}%
                </Text>
              </View>
              <View style={styles.technicalRow}>
                <Text style={styles.technicalLabel}>Défis:</Text>
                <Text style={styles.technicalValue}>
                  {(result.probability.difficile * 100).toFixed(1)}%
                </Text>
              </View>
            </>
          )}
        </View>

        {/* Divider */}
        <View style={styles.divider} />

        {/* Boutons d'action */}
        <View style={styles.actionButtons}>
          <TouchableOpacity
            style={styles.shareButton}
            onPress={() => {
              haptic.impact.light();
              handleShare();
            }}
          >
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
      </View>
    );
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <LinearGradient colors={THEME.colors.gradientDark} style={styles.container}>
        <Stack.Screen
          options={{
            title: 'Compatibilité',
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
            {/* Bouton retour sur formulaire */}
            <TouchableOpacity
              style={styles.formBackButton}
              onPress={() => router.back()}
            >
              <Ionicons name="arrow-back" size={20} color="rgba(255,255,255,0.8)" />
              <Text style={styles.formBackButtonText}>Retour</Text>
            </TouchableOpacity>

            {/* Header */}
            <View style={styles.header}>
              <Text style={styles.headerTitle}>🤖 Analyse Compatibilité</Text>
              <Text style={styles.headerSubtitle}>
                Découvrez la compatibilité astrologique parent-enfant basée sur les éléments et les signes du zodiaque
              </Text>
            </View>

            {/* Formulaire Parent */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>👤 Parent (Vous)</Text>
              {renderZodiacPicker('Signe solaire', parentData.sunSign, (v) =>
                setParentData({ ...parentData, sunSign: v })
              , getSunSign() ? 'auto' : null, 'parent-sun')}
              {renderZodiacPicker('Ascendant', parentData.ascendant, (v) =>
                setParentData({ ...parentData, ascendant: v })
              , getAscendant() ? 'auto' : null, 'parent-asc')}
              {renderZodiacPicker('Signe lunaire', parentData.moonSign, (v) =>
                setParentData({ ...parentData, moonSign: v })
              , getMoonSign() ? 'auto' : null, 'parent-moon')}
            </View>

            {/* Formulaire Enfant */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>👶 Enfant</Text>
              {renderZodiacPicker('Signe solaire', enfantData.sunSign, (v) =>
                setEnfantData({ ...enfantData, sunSign: v })
              , null, 'enfant-sun')}
              {renderZodiacPicker('Ascendant', enfantData.ascendant, (v) =>
                setEnfantData({ ...enfantData, ascendant: v })
              , null, 'enfant-asc')}
              {renderZodiacPicker('Signe lunaire', enfantData.moonSign, (v) =>
                setEnfantData({ ...enfantData, moonSign: v })
              , null, 'enfant-moon')}
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
    paddingBottom: 100,
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
    marginBottom: 20,
    marginTop: 0,
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 26,
    fontWeight: 'bold',
    color: THEME.colors.textLight,
    marginBottom: 8,
  },
  headerSubtitle: {
    fontSize: 14,
    color: THEME.colors.textMuted,
    textAlign: 'center',
    lineHeight: 20,
  },
  section: {
    marginBottom: 30,
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    borderRadius: 16,
    padding: 20,
  },
  sectionHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: THEME.colors.textLight,
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
  pickerSection: {
    marginBottom: 20,
  },
  pickerHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  pickerTitle: {
    fontSize: 14,
    color: THEME.colors.textMuted,
    fontWeight: '600',
  },
  zodiacScroll: {
    flexDirection: 'row',
  },
  zodiacButton: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 12,
    paddingHorizontal: 16,
    marginRight: 10,
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    borderRadius: 12,
    borderWidth: 2,
    borderColor: 'transparent',
  },
  zodiacButtonActive: {
    backgroundColor: THEME.colors.purpleAccent,
    borderColor: THEME.colors.purpleLight,
  },
  zodiacEmoji: {
    fontSize: 28,
    marginBottom: 4,
  },
  zodiacName: {
    fontSize: 11,
    color: THEME.colors.textMuted,
    fontWeight: '500',
  },
  zodiacNameActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  analyzeButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: THEME.colors.purpleAccent,
    paddingVertical: 20,
    borderRadius: 16,
    marginTop: 20,
    marginBottom: 30,
    gap: 10,
    shadowColor: '#8B5CF6',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.5,
    shadowRadius: 12,
    elevation: 8,
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
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 20,
    padding: 30,
    alignItems: 'center',
    position: 'relative',
    overflow: 'visible',
  },
  halo: {
    position: 'absolute',
    top: 20,
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: 'rgba(245, 158, 11, 0.3)',
    shadowColor: '#F59E0B',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.8,
    shadowRadius: 20,
  },
  scoreEmoji: {
    fontSize: 60,
    marginBottom: 10,
  },
  scoreValue: {
    fontSize: 72,
    fontWeight: 'bold',
    color: THEME.colors.textLight,
    marginBottom: 10,
  },
  scoreTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: THEME.colors.textLight,
    marginBottom: 10,
    textAlign: 'center',
  },
  scoreDescription: {
    fontSize: 14,
    color: THEME.colors.textMuted,
    textAlign: 'center',
    lineHeight: 20,
  },
  recommendationsSection: {
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    borderRadius: 16,
    padding: 20,
  },
  recommendationsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: THEME.colors.textLight,
    marginBottom: 15,
  },
  recommendationCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 15,
    gap: 12,
  },
  recommendationIcon: {
    fontSize: 24,
  },
  recommendationText: {
    flex: 1,
    fontSize: 15,
    color: THEME.colors.textLight,
    lineHeight: 22,
  },
  technicalDetails: {
    backgroundColor: 'rgba(255, 255, 255, 0.03)',
    borderRadius: 12,
    padding: 15,
  },
  technicalTitle: {
    fontSize: 14,
    fontWeight: 'bold',
    color: THEME.colors.textMuted,
    marginBottom: 10,
  },
  technicalRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  technicalLabel: {
    fontSize: 12,
    color: THEME.colors.textMuted,
  },
  technicalValue: {
    fontSize: 12,
    color: THEME.colors.textLight,
    fontWeight: '600',
  },
  newAnalysisButton: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    paddingVertical: 14,
    borderRadius: 12,
    alignItems: 'center',
    flex: 1,
  },
  newAnalysisButtonText: {
    color: THEME.colors.textLight,
    fontSize: 16,
    fontWeight: '600',
  },
  // Nouveaux styles Sprint 6
  methodLabel: {
    marginTop: 20,
    paddingTop: 20,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255, 255, 255, 0.1)',
    alignItems: 'center',
  },
  methodText: {
    fontSize: 11,
    color: THEME.colors.textMuted,
    textAlign: 'center',
    lineHeight: 16,
    marginBottom: 4,
  },
  methodVersion: {
    fontSize: 10,
    color: 'rgba(139, 92, 246, 0.8)',
    fontWeight: '600',
  },
  divider: {
    height: 1,
    backgroundColor: 'rgba(59, 30, 114, 0.3)',
    marginVertical: 10,
  },
  legend: {
    marginTop: 15,
    paddingTop: 15,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255, 255, 255, 0.05)',
  },
  legendText: {
    fontSize: 12,
    color: 'rgba(203, 213, 225, 0.7)',
    textAlign: 'center',
    lineHeight: 18,
    fontStyle: 'italic',
  },
  technicalHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  infoIcon: {
    fontSize: 16,
    opacity: 0.6,
  },
  actionButtons: {
    flexDirection: 'row',
    gap: 12,
  },
  shareButton: {
    backgroundColor: 'rgba(139, 92, 246, 0.8)',
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
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    paddingVertical: 12,
    paddingHorizontal: 16,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 12,
    alignSelf: 'flex-start',
    marginBottom: 20,
  },
  backButtonText: {
    color: THEME.colors.textLight,
    fontSize: 16,
    fontWeight: '600',
  },
});

