/**
 * Graphique Mood vs Cycle (30 jours)
 * Affiche l'humeur sur les 30 derniers jours avec background coloré par phase
 */

import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, Dimensions, ActivityIndicator } from 'react-native';
import { LineChart } from 'react-native-chart-kit';
import { prepareMoodCycleData } from '@/lib/services/chartDataService';
import { fonts, spacing } from '@/constants/theme';

const screenWidth = Dimensions.get('window').width;

export function MoodCycleChart() {
  const [chartData, setChartData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadChartData();
  }, []);

  const loadChartData = async () => {
    try {
      const data = await prepareMoodCycleData();
      setChartData(data);
    } catch (error) {
      console.error('[MoodCycleChart] Load error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator color="#FFB6C1" />
        <Text style={styles.loadingText}>Chargement du graphique...</Text>
      </View>
    );
  }

  if (!chartData || !chartData.labels || chartData.labels.length === 0) {
    return (
      <View style={styles.emptyContainer}>
        <Text style={styles.emptyEmoji}>📊</Text>
        <Text style={styles.emptyText}>
          Crée au moins 7 entrées de journal pour voir ton graphique
        </Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Humeur vs Cycle (30 jours)</Text>
      <LineChart
        data={chartData}
        width={screenWidth - 60}
        height={220}
        chartConfig={{
          backgroundColor: 'transparent',
          backgroundGradientFrom: 'rgba(255, 182, 193, 0.1)',
          backgroundGradientTo: 'rgba(192, 132, 252, 0.1)',
          decimalPlaces: 0,
          color: (opacity = 1) => `rgba(255, 182, 193, ${opacity})`,
          labelColor: (opacity = 1) => `rgba(255, 255, 255, ${opacity * 0.7})`,
          style: {
            borderRadius: 16,
          },
          propsForDots: {
            r: '5',
            strokeWidth: '2',
            stroke: '#FFB6C1',
          },
          propsForBackgroundLines: {
            strokeDasharray: '',
            stroke: 'rgba(255, 255, 255, 0.1)',
          },
        }}
        bezier
        style={styles.chart}
        withInnerLines
        withOuterLines
        withVerticalLines={false}
        withHorizontalLines
        segments={4}
      />
      <View style={styles.legend}>
        <View style={styles.legendItem}>
          <View style={[styles.legendDot, { backgroundColor: '#FF6B9D' }]} />
          <Text style={styles.legendText}>Menstruelle</Text>
        </View>
        <View style={styles.legendItem}>
          <View style={[styles.legendDot, { backgroundColor: '#FFB347' }]} />
          <Text style={styles.legendText}>Folliculaire</Text>
        </View>
        <View style={styles.legendItem}>
          <View style={[styles.legendDot, { backgroundColor: '#FFD93D' }]} />
          <Text style={styles.legendText}>Ovulation</Text>
        </View>
        <View style={styles.legendItem}>
          <View style={[styles.legendDot, { backgroundColor: '#C084FC' }]} />
          <Text style={styles.legendText}>Lutéale</Text>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 16,
    padding: spacing.md,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.2)',
  },
  title: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: spacing.md,
  },
  chart: {
    marginVertical: spacing.sm,
    borderRadius: 16,
  },
  legend: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.md,
    marginTop: spacing.md,
    justifyContent: 'center',
  },
  legendItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.xs,
  },
  legendDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
  },
  legendText: {
    fontSize: fonts.sizes.xs,
    color: 'rgba(255, 255, 255, 0.7)',
  },
  loadingContainer: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 16,
    padding: spacing.xl,
    alignItems: 'center',
    gap: spacing.md,
  },
  loadingText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
  },
  emptyContainer: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 16,
    padding: spacing.xl,
    alignItems: 'center',
  },
  emptyEmoji: {
    fontSize: 48,
    marginBottom: spacing.md,
  },
  emptyText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
    textAlign: 'center',
    lineHeight: 20,
  },
});

