/**
 * Carte "Aujourd'hui" pour le Home
 * Affiche la phase actuelle, le transit lunaire et un conseil
 */

import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { calculateCurrentCycle, calculateEnergyLevel, getPhaseAdvice } from '@/lib/services/cycleCalculator';
import { fonts, spacing, borderRadius } from '@/constants/theme';

export function TodayCard() {
  const [loading, setLoading] = useState(true);
  const [cycleData, setCycleData] = useState(null);
  const [moonSign, setMoonSign] = useState({ name: 'Vierge', emoji: '♍' }); // Simplifié pour MVP

  useEffect(() => {
    loadTodayData();
  }, []);

  const loadTodayData = async () => {
    try {
      const cycleConfig = await AsyncStorage.getItem('cycle_config');
      
      if (cycleConfig) {
        const { lastPeriodDate, cycleLength } = JSON.parse(cycleConfig);
        const current = calculateCurrentCycle(lastPeriodDate, cycleLength);
        const energy = calculateEnergyLevel(current.phase);
        const advice = getPhaseAdvice(current.phase);
        
        setCycleData({
          ...current,
          energy,
          advice,
        });
      }
    } catch (error) {
      console.error('[TodayCard] Load error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.container}>
        <ActivityIndicator color="#FFB6C1" size="large" />
      </View>
    );
  }

  if (!cycleData) {
    return (
      <View style={styles.container}>
        <Text style={styles.noDataEmoji}>🌙</Text>
        <Text style={styles.noDataTitle}>Configure ton cycle</Text>
        <Text style={styles.noDataText}>
          Va dans Settings pour configurer ton cycle et voir tes infos du jour
        </Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Aujourd'hui</Text>
        <Text style={styles.headerDate}>
          {new Date().toLocaleDateString('fr-FR', { 
            weekday: 'long', 
            day: 'numeric', 
            month: 'long' 
          })}
        </Text>
      </View>

      {/* Phase actuelle */}
      <View style={styles.phaseSection}>
        <Text style={styles.phaseEmoji}>{cycleData.phaseEmoji}</Text>
        <Text style={styles.phaseName}>Phase {cycleData.phaseName}</Text>
        <Text style={styles.phaseDay}>
          Jour {cycleData.dayOfCycle}/{cycleData.cycleLength}
        </Text>
      </View>

      {/* Barre d'énergie */}
      <View style={styles.energySection}>
        <View style={styles.energyHeader}>
          <Text style={styles.energyLabel}>Énergie cosmique</Text>
          <Text style={styles.energyValue}>{cycleData.energy}%</Text>
        </View>
        <View style={styles.energyBar}>
          <View style={[styles.energyFill, { 
            width: `${cycleData.energy}%`,
            backgroundColor: cycleData.phaseColor,
          }]} />
        </View>
      </View>

      {/* Transit lunaire */}
      <View style={styles.transitSection}>
        <Ionicons name="moon" size={16} color="#FFB6C1" />
        <Text style={styles.transitText}>
          Lune en {moonSign.emoji} {moonSign.name}
        </Text>
      </View>

      {/* Conseil du jour */}
      <View style={styles.adviceSection}>
        <Text style={styles.adviceEmoji}>{cycleData.advice.emoji}</Text>
        <Text style={styles.adviceTitle}>{cycleData.advice.title}</Text>
        <Text style={styles.adviceText}>{cycleData.advice.text}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'rgba(255, 182, 193, 0.12)',
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.25)',
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 12,
    elevation: 3,
  },
  header: {
    marginBottom: spacing.md,
    paddingBottom: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255, 255, 255, 0.1)',
  },
  headerTitle: {
    fontSize: fonts.sizes.xl,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: spacing.xs,
    textShadowColor: 'rgba(255, 200, 221, 0.4)',
    textShadowOffset: { width: 0, height: 1 },
    textShadowRadius: 4,
  },
  headerDate: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
    textTransform: 'capitalize',
  },
  phaseSection: {
    alignItems: 'center',
    marginBottom: spacing.lg,
  },
  phaseEmoji: {
    fontSize: 48,
    marginBottom: spacing.sm,
  },
  phaseName: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: spacing.xs,
  },
  phaseDay: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
  },
  energySection: {
    marginBottom: spacing.lg,
  },
  energyHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.sm,
  },
  energyLabel: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
    fontWeight: '600',
  },
  energyValue: {
    fontSize: fonts.sizes.lg,
    color: '#fff',
    fontWeight: 'bold',
  },
  energyBar: {
    height: 12,
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    borderRadius: 6,
    overflow: 'hidden',
  },
  energyFill: {
    height: '100%',
    borderRadius: 6,
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.6,
    shadowRadius: 6,
  },
  transitSection: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.xs,
    backgroundColor: 'rgba(192, 132, 252, 0.15)',
    borderRadius: borderRadius.sm,
    paddingVertical: spacing.xs,
    paddingHorizontal: spacing.sm,
    alignSelf: 'flex-start',
    marginBottom: spacing.lg,
  },
  transitText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.9)',
    fontWeight: '500',
  },
  adviceSection: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderLeftWidth: 3,
    borderLeftColor: '#FFB6C1',
  },
  adviceEmoji: {
    fontSize: 24,
    marginBottom: spacing.xs,
  },
  adviceTitle: {
    fontSize: fonts.sizes.md,
    fontWeight: 'bold',
    color: '#FFC8DD',
    marginBottom: spacing.xs,
  },
  adviceText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.85)',
    lineHeight: 20,
  },
  noDataEmoji: {
    fontSize: 48,
    textAlign: 'center',
    marginBottom: spacing.md,
  },
  noDataTitle: {
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
    color: '#fff',
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  noDataText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
    textAlign: 'center',
    lineHeight: 20,
  },
});

