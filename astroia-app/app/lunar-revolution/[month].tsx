/**
 * Écran détaillé pour un mois spécifique de révolution lunaire
 * Route dynamique : /lunar-revolution/2025-01
 */

import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  ScrollView,
  ActivityIndicator,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { useLunarRevolutionStore } from '@/stores/useLunarRevolutionStore';
import { useProfileStore } from '@/stores/profileStore';
import RevolutionCard from '@/components/lunar-revolution/RevolutionCard';
import AspectsList from '@/components/lunar-revolution/AspectsList';
import { color, space, layout, type as typography } from '@/theme/tokens';
import haptics from '@/utils/haptics';
import { Analytics } from '@/lib/analytics';
import type { LunarRevolution } from '@/lib/services/lunarRevolutionService';

export default function LunarRevolutionMonthScreen() {
  const router = useRouter();
  const params = useLocalSearchParams<{ month: string }>();
  const { profile } = useProfileStore();
  const { 
    getForMonth, 
    fetchForMonth, 
    status,
    error: storeError 
  } = useLunarRevolutionStore();
  
  const [error, setError] = useState<string | null>(null);
  
  // Mettre à jour l'erreur locale si le store a une erreur
  useEffect(() => {
    if (storeError && status === 'error') {
      setError(storeError);
    }
  }, [storeError, status]);

  const [revolution, setRevolution] = useState<LunarRevolution | null>(null);
  const [loading, setLoading] = useState(true);

  // Parser le paramètre month (format: YYYY-MM)
  const monthKey = params.month || '';
  const [year, month] = monthKey.split('-').map(Number);

  useEffect(() => {
    if (!monthKey || isNaN(year) || isNaN(month)) {
      router.replace('/lunar-revolution');
      return;
    }

    loadRevolution();
  }, [monthKey]);

  const loadRevolution = async () => {
    if (!profile.birthDate || !profile.birthTime) {
      setLoading(false);
      return;
    }

    setLoading(true);
    setError(null);

    try {
      // Créer une date pour le mois cible
      const targetDate = new Date(year, month - 1, 1);
      
      // Vérifier le cache
      let cached = getForMonth(targetDate);
      
      if (!cached) {
        // Charger depuis le service
        await fetchForMonth(targetDate);
        
        // Attendre un peu pour que le store mette à jour l'état
        await new Promise(resolve => setTimeout(resolve, 100));
        
        cached = getForMonth(targetDate);
      }

      if (!cached) {
        setError('Impossible de charger la révolution lunaire pour ce mois.');
      } else {
        setRevolution(cached);
      }
    } catch (err: any) {
      console.error('[LunarRevolutionMonth] Erreur:', err);
      const errorMessage = err?.message || 'Impossible de charger la révolution lunaire pour ce mois.';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  // Navigation vers mois précédent/suivant
  const navigateToMonth = (offset: number) => {
    haptics.light();
    const currentDate = new Date(year, month - 1, 1);
    const targetDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + offset, 1);
    const newMonthKey = `${targetDate.getFullYear()}-${String(targetDate.getMonth() + 1).padStart(2, '0')}`;
    router.push(`/lunar-revolution/${newMonthKey}`);
  };

  // Formatage du mois pour affichage
  const monthDisplay = (targetDate: Date): string => {
    return targetDate.toLocaleDateString('fr-FR', { month: 'long', year: 'numeric' });
  };

  // Analytics
  useEffect(() => {
    if (monthKey) {
      Analytics.track('lunar_revolution_month_viewed', { month: monthKey });
    }
  }, [monthKey]);

  // Vérifier que le profil est configuré
  if (!profile.birthDate || !profile.birthTime) {
    return (
      <SafeAreaView style={styles.container} edges={['top']}>
        <StatusBar style="light" />
        <View style={styles.errorContainer}>
          <Text style={styles.errorTitle}>Profil incomplet</Text>
          <Text style={styles.errorText}>
            Configure ton thème natal pour accéder aux révolutions lunaires.
          </Text>
          <TouchableOpacity
            style={styles.button}
            onPress={() => {
              haptics.medium();
              router.push('/natal-reading');
            }}
          >
            <Text style={styles.buttonText}>Configurer mon thème natal</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  // État de chargement
  if (loading) {
    return (
      <SafeAreaView style={styles.container} edges={['top']}>
        <StatusBar style="light" />
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color={color.brand} />
          <Text style={styles.loadingText}>Chargement de la révolution lunaire...</Text>
        </View>
      </SafeAreaView>
    );
  }

  // Erreur ou pas de données
  if (!revolution && !loading) {
    return (
      <SafeAreaView style={styles.container} edges={['top']}>
        <StatusBar style="light" />
        <View style={styles.errorContainer}>
          <Text style={styles.errorTitle}>
            {error?.includes('Impossible de remonter aussi loin') || error?.includes('avant ta date de naissance')
              ? 'Date trop ancienne'
              : 'Révolution non disponible'}
          </Text>
          <Text style={styles.errorText}>
            {error || storeError || 'Impossible de charger la révolution lunaire pour ce mois.'}
          </Text>
          {!error?.includes('Impossible de remonter aussi loin') && !error?.includes('avant ta date de naissance') && (
            <TouchableOpacity
              style={styles.button}
              onPress={() => {
                haptics.medium();
                loadRevolution();
              }}
            >
              <Text style={styles.buttonText}>Réessayer</Text>
            </TouchableOpacity>
          )}
        </View>
      </SafeAreaView>
    );
  }

  const currentDate = new Date(year, month - 1, 1);

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <StatusBar style="light" backgroundColor={color.bg} />
      
      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* En-tête */}
        <View style={styles.header}>
          <TouchableOpacity
            onPress={() => {
              haptics.light();
              router.push('/(tabs)/home');
            }}
            hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
          >
            <Text style={styles.backButton}>← Retour au menu</Text>
          </TouchableOpacity>
          <Text style={styles.title}>Révolution lunaire</Text>
          <Text style={styles.subtitle}>
            {monthDisplay(currentDate)}
          </Text>
        </View>

        {/* Navigation mois précédent/suivant */}
        <View style={styles.navigationContainer}>
          <TouchableOpacity
            style={styles.navButton}
            onPress={() => navigateToMonth(-1)}
            hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
          >
            <Text style={styles.navButtonText}>← Mois précédent</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.navButton}
            onPress={() => navigateToMonth(1)}
            hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
          >
            <Text style={styles.navButtonText}>Mois suivant →</Text>
          </TouchableOpacity>
        </View>

        {/* Carte principale */}
        <RevolutionCard revolution={revolution} />

        {/* Liste des aspects */}
        <AspectsList aspects={revolution.aspects || []} />

        {/* Suggestions de focus */}
        <View style={styles.suggestionsContainer}>
          <Text style={styles.suggestionsLabel}>SUGGESTIONS DE FOCUS</Text>
          <View style={styles.suggestionsList}>
            <SuggestionItem 
              icon="💭" 
              title="Émotions" 
              text="Porte attention à tes besoins émotionnels et à ton intuition ce mois-ci." 
            />
            <SuggestionItem 
              icon="⚡" 
              title="Rythme & Énergie" 
              text="Ajuste ton rythme selon la phase lunaire et l'énergie disponible." 
            />
            <SuggestionItem 
              icon="🤝" 
              title="Relations" 
              text="Les aspects lunaires influencent tes interactions et tes connexions." 
            />
            <SuggestionItem 
              icon="🔮" 
              title="Introspection" 
              text="Prends du temps pour réfléchir et intégrer les enseignements de cette période." 
            />
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

function SuggestionItem({ icon, title, text }: { icon: string; title: string; text: string }) {
  return (
    <View style={styles.suggestionItem}>
      <Text style={styles.suggestionIcon}>{icon}</Text>
      <View style={styles.suggestionContent}>
        <Text style={styles.suggestionTitle}>{title}</Text>
        <Text style={styles.suggestionText}>{text}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: color.bg,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    paddingHorizontal: layout.containerPadding,
    paddingBottom: space['2xl'],
  },
  header: {
    paddingTop: space.lg,
    paddingBottom: space.md,
  },
  backButton: {
    ...typography.body,
    color: color.brand,
    fontWeight: '600',
    marginBottom: space.sm,
  },
  title: {
    ...typography.h1,
    color: color.text,
    fontWeight: '800',
    marginBottom: space.xs,
  },
  subtitle: {
    ...typography.body,
    color: color.textMuted,
    textTransform: 'capitalize',
  },
  navigationContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: space.lg,
    gap: space.sm,
  },
  navButton: {
    flex: 1,
    paddingVertical: space.sm,
    paddingHorizontal: space.md,
    borderRadius: 8,
    backgroundColor: color.surface,
    borderWidth: 1,
    borderColor: color.border,
    alignItems: 'center',
  },
  navButtonText: {
    ...typography.bodySm,
    color: color.brand,
    fontWeight: '600',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    gap: space.md,
  },
  loadingText: {
    ...typography.body,
    color: color.textMuted,
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: space.lg,
    gap: space.md,
  },
  errorTitle: {
    ...typography.h2,
    color: color.text,
    fontWeight: '700',
  },
  errorText: {
    ...typography.body,
    color: color.textMuted,
    textAlign: 'center',
    lineHeight: 22,
  },
  button: {
    marginTop: space.md,
    paddingVertical: space.md,
    paddingHorizontal: space.lg,
    borderRadius: 8,
    backgroundColor: color.brand,
  },
  buttonText: {
    ...typography.body,
    color: color.text,
    fontWeight: '700',
  },
  suggestionsContainer: {
    marginTop: space.lg,
  },
  suggestionsLabel: {
    ...typography.label,
    color: color.brand,
    letterSpacing: 1.2,
    marginBottom: space.md,
  },
  suggestionsList: {
    gap: space.md,
  },
  suggestionItem: {
    flexDirection: 'row',
    backgroundColor: color.surface,
    borderRadius: 12,
    padding: space.md,
    borderWidth: 1,
    borderColor: color.border,
  },
  suggestionIcon: {
    fontSize: 24,
    marginRight: space.md,
  },
  suggestionContent: {
    flex: 1,
  },
  suggestionTitle: {
    ...typography.h4,
    color: color.text,
    fontWeight: '700',
    marginBottom: space.xs,
  },
  suggestionText: {
    ...typography.body,
    color: color.textSecondary,
    lineHeight: 20,
  },
});

