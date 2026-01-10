import React, { useState, useRef, useEffect } from 'react';
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
import AsyncStorage from '@react-native-async-storage/async-storage';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

const { width } = Dimensions.get('window');

export default function OnboardingScreen() {
  const [currentStep, setCurrentStep] = useState(0);
  const scrollViewRef = useRef(null);
  const fadeAnim = useRef(new Animated.Value(1)).current;

  useEffect(() => {
    console.log('[ROUTING] Mounted OnboardingScreen (index)');
  }, []);

  const steps = [
    {
      id: 'welcome',
      emoji: '🌙',
      title: 'Bienvenue sur LUNA',
      subtitle: 'Cycle & Cosmos',
      description: 'Suis ton cycle menstruel, écoute les étoiles, et découvre ton énergie au quotidien.',
    },
    {
      id: 'value1',
      emoji: '📅',
      title: 'Comprends ton cycle',
      description: 'Suis tes phases menstruelles et découvre comment elles influencent ton énergie, tes émotions et ton bien-être.',
    },
    {
      id: 'value2',
      emoji: '🌟',
      title: 'Écoute les astres',
      description: 'Découvre les transits lunaires et comment la lune influence ta vie au quotidien selon ton thème natal.',
    },
    {
      id: 'value3',
      emoji: '📖',
      title: 'Journalise tes émotions',
      description: 'Crée des connexions entre ton cycle, les astres et tes ressentis grâce à un journal intelligent.',
    },
  ];

  const handleNext = () => {
    if (currentStep < steps.length - 1) {
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
      // Dernier écran → aller au setup profil
      router.push('/onboarding/profile-setup');
    }
  };

  const handleSkip = async () => {
    // Marquer onboarding comme terminé (simplifié pour l'instant)
    await AsyncStorage.setItem('onboarding_completed', 'true');
    router.replace('/(tabs)/home');
  };

  const currentStepData = steps[currentStep];

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header avec Skip */}
        <View style={styles.header}>
          <TouchableOpacity onPress={handleSkip} style={styles.skipButton}>
            <Text style={styles.skipText}>Passer</Text>
          </TouchableOpacity>
        </View>

        {/* Content */}
        <ScrollView
          ref={scrollViewRef}
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          <Animated.View style={[styles.content, { opacity: fadeAnim }]}>
            {/* Emoji */}
            <View style={styles.emojiContainer}>
              <Text style={styles.emoji}>{currentStepData.emoji}</Text>
            </View>

            {/* Title */}
            <Text style={styles.title}>{currentStepData.title}</Text>
            
            {/* Subtitle (si existe) */}
            {currentStepData.subtitle && (
              <Text style={styles.subtitle}>{currentStepData.subtitle}</Text>
            )}

            {/* Description */}
            <Text style={styles.description}>{currentStepData.description}</Text>
          </Animated.View>
        </ScrollView>

        {/* Footer avec indicateurs et bouton */}
        <View style={styles.footer}>
          {/* Indicateurs */}
          <View style={styles.indicators}>
            {steps.map((_, index) => (
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
                {currentStep < steps.length - 1 ? 'Suivant' : 'Commencer'}
              </Text>
              <Ionicons name="arrow-forward" size={20} color="#fff" />
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
    justifyContent: 'flex-end',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  skipButton: {
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
  },
  skipText: {
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
    paddingVertical: spacing.xxl,
  },
  emojiContainer: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: 'rgba(255, 182, 193, 0.15)',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: spacing.xl,
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
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FFFFFF',
    textAlign: 'center',
    marginBottom: spacing.sm,
    textShadowColor: 'rgba(255, 182, 193, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  subtitle: {
    fontSize: 24,
    fontWeight: '600',
    color: '#FFC8DD',
    textAlign: 'center',
    marginBottom: spacing.lg,
    textShadowColor: 'rgba(255, 200, 221, 0.4)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 8,
  },
  description: {
    fontSize: fonts.sizes.lg,
    color: 'rgba(255, 255, 255, 0.85)',
    textAlign: 'center',
    lineHeight: 28,
    paddingHorizontal: spacing.md,
    maxWidth: width * 0.8,
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
