import React, { useState, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Dimensions,
  Animated,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

const { width } = Dimensions.get('window');

const TOUR_STEPS = [
  {
    emoji: '🌙',
    title: 'Suis ton cycle',
    description: 'Découvre dans quelle phase tu es et comment ton énergie varie selon ton cycle menstruel et les transits lunaires.',
    color: '#FFB6C1',
  },
  {
    emoji: '📖',
    title: 'Journalise tes émotions',
    description: 'Crée des connexions entre ton humeur, ton cycle et les positions des astres grâce à un journal intelligent.',
    color: '#C084FC',
  },
  {
    emoji: '💬',
    title: 'Parle à ton IA',
    description: 'Pose tes questions sur le bien-être, la gestion de l\'énergie et reçois des conseils personnalisés selon ta phase actuelle.',
    color: '#FFC8DD',
  },
];

export default function TourScreen() {
  const [currentStep, setCurrentStep] = useState(0);
  const fadeAnim = useRef(new Animated.Value(1)).current;
  const scrollViewRef = useRef(null);

  const handleNext = () => {
    if (currentStep < TOUR_STEPS.length - 1) {
      // Fade out
      Animated.timing(fadeAnim, {
        toValue: 0,
        duration: 200,
        useNativeDriver: true,
      }).start(() => {
        setCurrentStep(currentStep + 1);
        scrollViewRef.current?.scrollTo({ x: 0, y: 0, animated: false });
        
        // Fade in
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 300,
          useNativeDriver: true,
        }).start();
      });
    } else {
      // Dernier slide → aller au disclaimer
      router.push('/onboarding/disclaimer');
    }
  };

  const handleBack = () => {
    if (currentStep > 0) {
      // Fade out
      Animated.timing(fadeAnim, {
        toValue: 0,
        duration: 200,
        useNativeDriver: true,
      }).start(() => {
        setCurrentStep(currentStep - 1);
        scrollViewRef.current?.scrollTo({ x: 0, y: 0, animated: false });
        
        // Fade in
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 300,
          useNativeDriver: true,
        }).start();
      });
    } else {
      router.back();
    }
  };

  const currentStepData = TOUR_STEPS[currentStep];

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
            <Text style={styles.headerTitle}>Étape 4/4</Text>
          <View style={{ width: 40 }} />
        </View>

        {/* Content */}
        <ScrollView
          ref={scrollViewRef}
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          <Animated.View style={[styles.content, { opacity: fadeAnim }]}>
            {/* Emoji container avec couleur dynamique */}
            <View style={[
              styles.emojiContainer,
              { backgroundColor: `${currentStepData.color}15`, borderColor: `${currentStepData.color}40` }
            ]}>
              <Text style={styles.emoji}>{currentStepData.emoji}</Text>
            </View>

            {/* Title */}
            <Text style={styles.title}>{currentStepData.title}</Text>

            {/* Description */}
            <Text style={styles.description}>{currentStepData.description}</Text>

            {/* Feature highlights */}
            <View style={styles.highlights}>
              {currentStep === 0 && (
                <>
                  <FeatureItem icon="analytics-outline" text="Calcul automatique de ta phase" />
                  <FeatureItem icon="moon-outline" text="Transits lunaires en temps réel" />
                  <FeatureItem icon="flash-outline" text="Niveau d'énergie personnalisé" />
                </>
              )}
              {currentStep === 1 && (
                <>
                  <FeatureItem icon="create-outline" text="Notes et tags intelligents" />
                  <FeatureItem icon="stats-chart-outline" text="Graphiques sur 30/90 jours" />
                  <FeatureItem icon="heart-outline" text="Corrélations cycle & humeur" />
                </>
              )}
              {currentStep === 2 && (
                <>
                  <FeatureItem icon="chatbubbles-outline" text="Conseils bien-être personnalisés" />
                  <FeatureItem icon="sparkles-outline" text="Contexte astro + cycle intégré" />
                  <FeatureItem icon="shield-checkmark-outline" text="100% confidentiel et sécurisé" />
                </>
              )}
            </View>
          </Animated.View>
        </ScrollView>

        {/* Footer */}
        <View style={styles.footer}>
          {/* Indicateurs */}
          <View style={styles.indicators}>
            {TOUR_STEPS.map((_, index) => (
              <View
                key={index}
                style={[
                  styles.indicator,
                  index === currentStep && styles.indicatorActive,
                ]}
              />
            ))}
          </View>

          {/* Bouton Suivant */}
          <TouchableOpacity
            style={styles.nextButton}
            onPress={handleNext}
            activeOpacity={0.8}
          >
            <LinearGradient
              colors={['#FFB6C1', '#FFC8DD']}
              style={styles.nextButtonGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Text style={styles.nextButtonText}>
                {currentStep < TOUR_STEPS.length - 1 ? 'Suivant' : 'Continuer'}
              </Text>
              <Ionicons name="arrow-forward" size={20} color="#fff" />
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </LinearGradient>
  );
}

// Composant pour les items de features
function FeatureItem({ icon, text }) {
  return (
    <View style={styles.featureItem}>
      <View style={styles.featureIconContainer}>
        <Ionicons name={icon} size={20} color="#FFB6C1" />
      </View>
      <Text style={styles.featureText}>{text}</Text>
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
    flexGrow: 1,
    paddingHorizontal: spacing.xl,
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingVertical: spacing.xl,
  },
  emojiContainer: {
    width: 120,
    height: 120,
    borderRadius: 60,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: spacing.xl,
    borderWidth: 2,
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.3,
    shadowRadius: 16,
    elevation: 8,
  },
  emoji: {
    fontSize: 64,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FFFFFF',
    textAlign: 'center',
    marginBottom: spacing.md,
    textShadowColor: 'rgba(255, 182, 193, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  description: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.85)',
    textAlign: 'center',
    lineHeight: 24,
    paddingHorizontal: spacing.md,
    maxWidth: width * 0.85,
    marginBottom: spacing.xl,
  },
  highlights: {
    width: '100%',
    gap: spacing.md,
    marginTop: spacing.md,
  },
  featureItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.2)',
  },
  featureIconContainer: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: 'rgba(255, 182, 193, 0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  featureText: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.9)',
    fontWeight: '500',
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
    gap: spacing.lg,
  },
  indicators: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: spacing.sm,
  },
  indicator: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.3)',
  },
  indicatorActive: {
    backgroundColor: '#FFB6C1',
    width: 24,
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.6,
    shadowRadius: 4,
  },
  nextButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  nextButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    gap: spacing.sm,
  },
  nextButtonText: {
    color: '#fff',
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});

