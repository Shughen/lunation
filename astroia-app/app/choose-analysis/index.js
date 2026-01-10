import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  SafeAreaView,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { Stack, router } from 'expo-router';
import THEME from '@/constants/theme';
import { useHapticFeedback } from '@/hooks/useHapticFeedback';

export default function ChooseAnalysisScreen() {
  const { selection, impact } = useHapticFeedback();

  const analyses = [
    {
      id: 'parent-child',
      icon: 'people',
      emoji: '👶',
      title: 'Parent-Enfant',
      description: 'Analysez la compatibilité astrologique avec votre enfant',
      color: THEME.colors.secondary,
      route: '/parent-child',
    },
    {
      id: 'compatibility-couple',
      icon: 'heart',
      emoji: '💑',
      title: 'Compatibilité Amoureuse',
      description: 'Découvrez votre compatibilité avec votre partenaire',
      color: '#FF6B9D',
      route: '/compatibility',
      params: { defaultType: 'couple' },
    },
    {
      id: 'compatibility-friends',
      icon: 'people-circle',
      emoji: '🤝',
      title: 'Compatibilité Amicale',
      description: 'Analysez votre relation amicale',
      color: '#4ECDC4',
      route: '/compatibility',
      params: { defaultType: 'friends' },
    },
    {
      id: 'compatibility-colleagues',
      icon: 'briefcase',
      emoji: '💼',
      title: 'Compatibilité Professionnelle',
      description: 'Évaluez la collaboration avec vos collègues',
      color: '#95E1D3',
      route: '/compatibility',
      params: { defaultType: 'colleagues' },
    },
    {
      id: 'horoscope',
      icon: 'star',
      emoji: '✨',
      title: 'Horoscope du Jour',
      description: 'Votre horoscope personnalisé quotidien',
      color: THEME.colors.accent,
      route: '/horoscope',
    },
  ];

  const handleSelectAnalysis = (analysis) => {
    selection();
    if (analysis.params) {
      router.push({
        pathname: analysis.route,
        params: analysis.params,
      });
    } else {
      router.push(analysis.route);
    }
  };

  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={THEME.colors.gradientDark} style={styles.container}>
        <Stack.Screen
          options={{
            headerShown: false,
          }}
        />

        <SafeAreaView style={styles.safeArea}>
          {/* Header */}
          <View style={styles.header}>
            <TouchableOpacity
              style={styles.backButton}
              onPress={() => {
                impact.light();
                router.back();
              }}
            >
              <Ionicons name="arrow-back" size={24} color="#fff" />
            </TouchableOpacity>
          </View>

          <ScrollView
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
          >
            {/* Title */}
            <View style={styles.titleSection}>
              <Text style={styles.mainTitle}>Quelle analyse souhaitez-vous créer ?</Text>
              <Text style={styles.subtitle}>
                Choisissez le type d'analyse astrologique qui vous intéresse
              </Text>
            </View>

            {/* Cartes d'analyses */}
            <View style={styles.cardsContainer}>
              {analyses.map((analysis, index) => (
                <TouchableOpacity
                  key={analysis.id}
                  style={[
                    styles.analysisCard,
                    { borderColor: analysis.color + '40' },
                  ]}
                  onPress={() => handleSelectAnalysis(analysis)}
                  activeOpacity={0.7}
                >
                  {/* Glow effect */}
                  <View
                    style={[
                      styles.cardGlow,
                      { backgroundColor: analysis.color + '20' },
                    ]}
                  />

                  {/* Icon */}
                  <View
                    style={[
                      styles.iconContainer,
                      { backgroundColor: analysis.color + '30' },
                    ]}
                  >
                    <Text style={styles.emoji}>{analysis.emoji}</Text>
                  </View>

                  {/* Content */}
                  <View style={styles.cardContent}>
                    <Text style={styles.cardTitle}>{analysis.title}</Text>
                    <Text style={styles.cardDescription}>{analysis.description}</Text>
                  </View>

                  {/* Arrow */}
                  <Ionicons
                    name="chevron-forward"
                    size={24}
                    color="rgba(255,255,255,0.4)"
                    style={styles.cardArrow}
                  />
                </TouchableOpacity>
              ))}
            </View>

            {/* Hint */}
            <View style={styles.hintCard}>
              <Ionicons name="bulb-outline" size={20} color="#F59E0B" />
              <Text style={styles.hintText}>
                Chaque analyse est unique et personnalisée selon vos données astrologiques
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
    paddingHorizontal: 20,
    paddingTop: 60,
    paddingBottom: 10,
  },
  backButton: {
    width: 44,
    height: 44,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderRadius: 12,
  },
  scrollContent: {
    padding: 20,
    paddingTop: 10,
    paddingBottom: 40,
  },
  titleSection: {
    marginBottom: 30,
  },
  mainTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: 'rgba(255,255,255,0.7)',
    lineHeight: 22,
  },
  cardsContainer: {
    gap: 16,
  },
  analysisCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(255,255,255,0.08)',
    borderRadius: 16,
    padding: 16,
    borderWidth: 1,
    position: 'relative',
    overflow: 'hidden',
  },
  cardGlow: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    opacity: 0.3,
  },
  iconContainer: {
    width: 60,
    height: 60,
    borderRadius: 14,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 14,
  },
  emoji: {
    fontSize: 32,
  },
  cardContent: {
    flex: 1,
  },
  cardTitle: {
    fontSize: 17,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 4,
  },
  cardDescription: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.7)',
    lineHeight: 20,
  },
  cardArrow: {
    marginLeft: 8,
  },
  hintCard: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    borderRadius: 12,
    padding: 16,
    marginTop: 20,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
  },
  hintText: {
    flex: 1,
    fontSize: 13,
    color: 'rgba(255,255,255,0.8)',
    lineHeight: 19,
  },
});

