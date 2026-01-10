/**
 * Graphique Énergie par Phase du Cycle
 * Affiche l'énergie moyenne par phase
 */

import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, Dimensions, ActivityIndicator } from 'react-native';
import { BarChart } from 'react-native-chart-kit';
import { prepareEnergyCycleData } from '@/lib/services/chartDataService';
import { fonts, spacing } from '@/constants/theme';

const screenWidth = Dimensions.get('window').width;

export function EnergyCycleChart() {
  const [chartData, setChartData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadChartData();
  }, []);

  const loadChartData = async () => {
    try {
      const data = await prepareEnergyCycleData();
      setChartData(data);
    } catch (error) {
      console.error('[EnergyCycleChart] Load error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator color="#FFB6C1" />
        <Text style={styles.loadingText}>Chargement...</Text>
      </View>
    );
  }

  if (!chartData) {
    return (
      <View style={styles.emptyContainer}>
        <Text style={styles.emptyEmoji}>⚡</Text>
        <Text style={styles.emptyText}>
          Données insuffisantes pour l'instant
        </Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Énergie moyenne par phase</Text>
      <BarChart
        data={chartData}
        width={screenWidth - 60}
        height={220}
        yAxisLabel=""
        yAxisSuffix="%"
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
          propsForLabels: {
            fontSize: 10,
          },
        }}
        style={styles.chart}
        showValuesOnTopOfBars
        fromZero
      />
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
    borderColor: 'rgba(192, 132, 252, 0.2)',
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
  loadingContainer: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 16,
    padding: spacing.xl,
    alignItems: 'center',
    gap: spacing.sm,
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
    fontSize: 40,
    marginBottom: spacing.sm,
  },
  emptyText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
    textAlign: 'center',
  },
});

