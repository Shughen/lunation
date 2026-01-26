/**
 * Écran Luna Pack (/lunar)
 *
 * Hub lunaire du présent centré sur aujourd'hui :
 * - Section 1: Daily Climate (phase + signe + insight)
 * - Section 2: Liens contextuels (rapport mensuel, VoC)
 * - Section 3: Dev Tools (DEV only)
 */

import React, { useRef, useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';
import { useLocalSearchParams, router } from 'expo-router';
import { useLunar } from '../../contexts/LunarProvider';
import { lunaPack } from '../../services/api';
import { AnimatedCard } from '../../components/AnimatedCard';
import { translateZodiacSign } from '../../utils/astrologyTranslations';
import { haptics } from '../../services/haptics';

/**
 * Convertit une longitude écliptique absolue (0-360°) en degré dans le signe (0-29°)
 * Un signe = 30°, donc degré_dans_signe = longitude % 30
 */
function getDegreeInSign(absoluteDegree: number): number {
  return Math.floor(absoluteDegree % 30);
}

interface DailyClimate {
  date: string;
  moon: {
    sign: string;
    degree: number;
    phase: string;
  };
  insight: {
    title: string;
    text: string;
    keywords: string[];
    version: string;
  };
}

interface VocStatus {
  now: { is_active: boolean; end_at: string } | null;
  next: { start_at: string; end_at: string } | null;
}

export default function LunarPackScreen() {
  const { focus } = useLocalSearchParams<{ focus?: string }>();
  const scrollViewRef = useRef<ScrollView>(null);
  const dailyClimateY = useRef(0);

  // Lunar context for VoC status
  const { helpers, clearCache: clearLunarCache } = useLunar();

  // Local state for daily climate
  const [dailyClimate, setDailyClimate] = useState<DailyClimate | null>(null);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // VoC status for contextual link
  const [vocStatus, setVocStatus] = useState<VocStatus | null>(null);

  // Dev tools state
  const [devToolsExpanded, setDevToolsExpanded] = useState(false);
  const [showRawJson, setShowRawJson] = useState(false);

  // Auto-scroll to daily_climate if focus param is set
  useEffect(() => {
    if (focus === 'daily_climate' && dailyClimateY.current > 0) {
      setTimeout(() => {
        scrollViewRef.current?.scrollTo({
          y: dailyClimateY.current,
          animated: true,
        });
      }, 100);
    }
  }, [focus, dailyClimate]);

  // Load data on mount
  useEffect(() => {
    loadData();
  }, []);

  const loadData = async (isRefresh = false) => {
    try {
      if (isRefresh) {
        setRefreshing(true);
      } else {
        setLoading(true);
      }
      setError(null);

      // Fetch daily climate and VoC status in parallel
      const [climateResult, vocResult] = await Promise.allSettled([
        lunaPack.getDailyClimate(),
        fetch(`${process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000'}/api/lunar/voc/status`).then((r) =>
          r.ok ? r.json() : null
        ),
      ]);

      if (climateResult.status === 'fulfilled') {
        setDailyClimate(climateResult.value);
      } else {
        console.error('[LunarPack] Daily climate error:', climateResult.reason);
        setError('Impossible de charger le climat lunaire');
      }

      if (vocResult.status === 'fulfilled' && vocResult.value) {
        setVocStatus(vocResult.value);
      }
    } catch (err: any) {
      console.error('[LunarPack] Load error:', err);
      setError('Erreur lors du chargement');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const onRefresh = () => loadData(true);

  const handleClearCache = async () => {
    haptics.light();
    await clearLunarCache();
    await loadData(true);
    haptics.success();
  };

  const formatVocEndTime = (isoString: string): string => {
    const date = new Date(isoString);
    return date.toLocaleTimeString('fr-FR', {
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  // Render loading state
  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#8B7BF7" />
        <Text style={styles.loadingText}>Chargement du climat lunaire...</Text>
      </View>
    );
  }

  // Render error state
  if (error && !dailyClimate) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorText}>{error}</Text>
        <TouchableOpacity style={styles.retryButton} onPress={() => loadData()}>
          <Text style={styles.retryButtonText}>Réessayer</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
          <Text style={styles.backButtonText}>← Retour</Text>
        </TouchableOpacity>
      </View>
    );
  }

  const vocActive = vocStatus?.now?.is_active || helpers.vocActive;
  const vocEndTime = vocStatus?.now?.end_at
    ? formatVocEndTime(vocStatus.now.end_at)
    : helpers.vocEndTime;

  return (
    <ScrollView
      ref={scrollViewRef}
      style={styles.container}
      contentContainerStyle={styles.scrollContent}
      refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor="#8B7BF7" />}
    >
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity
          style={styles.backButtonSmall}
          onPress={() => router.back()}
          hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
        >
          <Text style={styles.backButtonText}>← Retour</Text>
        </TouchableOpacity>

        <Text style={styles.title}>Ton Climat Lunaire</Text>
        <Text style={styles.subtitle}>Aujourd'hui</Text>
      </View>

      {/* Section 1: Daily Climate */}
      <View onLayout={(e) => (dailyClimateY.current = e.nativeEvent.layout.y)}>
        <AnimatedCard style={styles.climateCard} delay={0} duration={500}>
          {dailyClimate && (
            <>
              {/* Phase + Sign + Degree */}
              <View style={styles.moonInfo}>
                <Text style={styles.phaseText}>
                  {dailyClimate.moon.phase} en {translateZodiacSign(dailyClimate.moon.sign)}
                </Text>
                <Text style={styles.degreeText}>{getDegreeInSign(dailyClimate.moon.degree)}° {translateZodiacSign(dailyClimate.moon.sign)}</Text>
              </View>

              {/* Insight */}
              <View style={styles.insightSection}>
                <Text style={styles.insightTitle}>{dailyClimate.insight.title}</Text>
                <Text style={styles.insightText}>{dailyClimate.insight.text}</Text>
              </View>

              {/* Keywords */}
              <View style={styles.keywordsRow}>
                {dailyClimate.insight.keywords.map((keyword, index) => (
                  <View key={index} style={styles.keywordBadge}>
                    <Text style={styles.keywordText}>#{keyword}</Text>
                  </View>
                ))}
              </View>

              {/* VoC Badge if active */}
              {vocActive && vocEndTime && (
                <View style={styles.vocBadge}>
                  <Text style={styles.vocText}>⏸️ Pause Lunaire jusqu'à {vocEndTime}</Text>
                </View>
              )}
            </>
          )}
        </AnimatedCard>
      </View>

      {/* Section 2: Contextual Links */}
      <AnimatedCard style={styles.linksCard} delay={150} duration={500}>
        <TouchableOpacity
          style={styles.linkRow}
          onPress={() => {
            haptics.light();
            router.push('/lunar/report');
          }}
        >
          <Text style={styles.linkText}>→ Voir le rapport mensuel</Text>
        </TouchableOpacity>

        {vocActive && (
          <TouchableOpacity
            style={[styles.linkRow, styles.linkRowVoc]}
            onPress={() => {
              haptics.light();
              router.push('/lunar/voc');
            }}
          >
            <Text style={styles.linkTextVoc}>⏸️ Pause Lunaire en cours</Text>
          </TouchableOpacity>
        )}
      </AnimatedCard>

      {/* Section 3: Dev Tools (DEV only) */}
      {__DEV__ && (
        <AnimatedCard style={styles.devCard} delay={300} duration={500}>
          <TouchableOpacity
            style={styles.devHeader}
            onPress={() => setDevToolsExpanded(!devToolsExpanded)}
          >
            <Text style={styles.devTitle}>Dev Tools</Text>
            <Text style={styles.devToggle}>{devToolsExpanded ? '▲' : '▼'}</Text>
          </TouchableOpacity>

          {devToolsExpanded && (
            <View style={styles.devContent}>
              <View style={styles.devButtonsRow}>
                <TouchableOpacity style={styles.devButton} onPress={handleClearCache}>
                  <Text style={styles.devButtonText}>Clear Cache</Text>
                </TouchableOpacity>

                <TouchableOpacity
                  style={styles.devButton}
                  onPress={() => setShowRawJson(!showRawJson)}
                >
                  <Text style={styles.devButtonText}>{showRawJson ? 'Masquer JSON' : 'Voir JSON'}</Text>
                </TouchableOpacity>
              </View>

              {showRawJson && dailyClimate && (
                <View style={styles.jsonContainer}>
                  <Text style={styles.jsonText}>{JSON.stringify(dailyClimate, null, 2)}</Text>
                </View>
              )}
            </View>
          )}
        </AnimatedCard>
      )}

      {/* Footer */}
      <Text style={styles.footerText}>
        {dailyClimate?.insight.version ? `v${dailyClimate.insight.version}` : ''}
      </Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0A0E27',
  },
  scrollContent: {
    paddingBottom: 40,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0A0E27',
  },
  loadingText: {
    marginTop: 16,
    fontSize: 16,
    color: '#8B7BF7',
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0A0E27',
    padding: 20,
  },
  errorText: {
    fontSize: 18,
    color: '#FF6B6B',
    marginBottom: 20,
    textAlign: 'center',
  },
  retryButton: {
    backgroundColor: '#8B7BF7',
    padding: 16,
    borderRadius: 8,
    marginBottom: 12,
  },
  retryButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  backButton: {
    backgroundColor: '#2D3561',
    padding: 16,
    borderRadius: 8,
  },
  backButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  header: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#1A1F3E',
    borderBottomWidth: 2,
    borderBottomColor: '#8B7BF7',
    position: 'relative',
  },
  backButtonSmall: {
    position: 'absolute',
    top: 60,
    left: 20,
    zIndex: 10,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FFFFFF',
    textAlign: 'center',
    marginBottom: 4,
    marginTop: 24,
  },
  subtitle: {
    fontSize: 16,
    color: '#A0A0B0',
    textAlign: 'center',
  },
  climateCard: {
    margin: 16,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 2,
    borderColor: '#8B7BF7',
  },
  moonInfo: {
    marginBottom: 20,
  },
  phaseText: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 4,
  },
  degreeText: {
    fontSize: 14,
    color: '#A0A0B0',
  },
  insightSection: {
    marginBottom: 16,
  },
  insightTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#8B7BF7',
    marginBottom: 8,
  },
  insightText: {
    fontSize: 15,
    color: '#C0C0D0',
    lineHeight: 24,
  },
  keywordsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    marginBottom: 16,
  },
  keywordBadge: {
    backgroundColor: 'rgba(139, 123, 247, 0.2)',
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 16,
  },
  keywordText: {
    fontSize: 13,
    color: '#8B7BF7',
    fontWeight: '500',
  },
  vocBadge: {
    backgroundColor: 'rgba(251, 191, 36, 0.15)',
    borderWidth: 1,
    borderColor: '#FBBF24',
    borderRadius: 8,
    padding: 12,
  },
  vocText: {
    fontSize: 14,
    color: '#FBBF24',
    fontWeight: '600',
  },
  linksCard: {
    margin: 16,
    marginTop: 0,
    padding: 16,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  linkRow: {
    paddingVertical: 12,
  },
  linkRowVoc: {
    borderTopWidth: 1,
    borderTopColor: '#2D3561',
    marginTop: 8,
    paddingTop: 16,
  },
  linkText: {
    fontSize: 16,
    color: '#8B7BF7',
    fontWeight: '600',
  },
  linkTextVoc: {
    fontSize: 16,
    color: '#FBBF24',
    fontWeight: '600',
  },
  devCard: {
    margin: 16,
    marginTop: 0,
    padding: 16,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  devHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  devTitle: {
    fontSize: 14,
    color: '#A0A0B0',
    fontWeight: '600',
  },
  devToggle: {
    fontSize: 12,
    color: '#A0A0B0',
  },
  devContent: {
    marginTop: 16,
  },
  devButtonsRow: {
    flexDirection: 'row',
    gap: 12,
  },
  devButton: {
    flex: 1,
    backgroundColor: '#2D3561',
    paddingVertical: 10,
    paddingHorizontal: 16,
    borderRadius: 8,
    alignItems: 'center',
  },
  devButtonText: {
    fontSize: 13,
    color: '#FFFFFF',
    fontWeight: '500',
  },
  jsonContainer: {
    marginTop: 16,
    backgroundColor: '#0A0E27',
    padding: 12,
    borderRadius: 8,
  },
  jsonText: {
    fontSize: 11,
    color: '#A0A0B0',
    fontFamily: 'monospace',
  },
  footerText: {
    fontSize: 12,
    color: '#A0A0B0',
    textAlign: 'center',
    marginTop: 8,
    marginBottom: 20,
  },
});
