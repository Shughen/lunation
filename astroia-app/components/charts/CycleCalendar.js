/**
 * Calendrier du cycle menstruel
 * Vue mensuelle avec couleurs par phase
 */

import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';
import { Calendar } from 'react-native-calendars';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { calculateCurrentCycle } from '@/lib/services/cycleCalculator';
import { fonts, spacing } from '@/constants/theme';

export function CycleCalendar() {
  const [loading, setLoading] = useState(true);
  const [markedDates, setMarkedDates] = useState({});

  useEffect(() => {
    loadCalendarData();
  }, []);

  const loadCalendarData = async () => {
    try {
      const cycleConfig = await AsyncStorage.getItem('cycle_config');
      if (!cycleConfig) {
        setLoading(false);
        return;
      }

      const { lastPeriodDate, cycleLength } = JSON.parse(cycleConfig);
      const marked = {};

      // Marquer les 60 prochains jours (2 cycles)
      for (let i = 0; i < 60; i++) {
        const date = new Date(lastPeriodDate);
        date.setDate(date.getDate() + i);
        
        const dayOfCycle = (i % cycleLength) + 1;
        const dateString = date.toISOString().split('T')[0];
        
        // Déterminer phase et couleur
        let color = '#FF6B9D'; // menstrual
        let phase = 'menstrual';
        
        if (dayOfCycle > 16) {
          color = '#C084FC'; // luteal
          phase = 'luteal';
        } else if (dayOfCycle > 13) {
          color = '#FFD93D'; // ovulation
          phase = 'ovulation';
        } else if (dayOfCycle > 5) {
          color = '#FFB347'; // follicular
          phase = 'follicular';
        }
        
        marked[dateString] = {
          selected: true,
          selectedColor: color,
          phase,
        };
      }

      // Marquer aujourd'hui spécialement
      const today = new Date().toISOString().split('T')[0];
      if (marked[today]) {
        marked[today].marked = true;
        marked[today].dotColor = '#FFFFFF';
      }

      setMarkedDates(marked);
    } catch (error) {
      console.error('[CycleCalendar] Load error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator color="#FFB6C1" />
      </View>
    );
  }

  if (Object.keys(markedDates).length === 0) {
    return (
      <View style={styles.emptyContainer}>
        <Text style={styles.emptyEmoji}>📅</Text>
        <Text style={styles.emptyText}>
          Configure ton cycle dans Settings pour voir le calendrier
        </Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Calendrier du cycle</Text>
      <Calendar
        markedDates={markedDates}
        theme={{
          calendarBackground: 'transparent',
          textSectionTitleColor: 'rgba(255,255,255,0.7)',
          selectedDayBackgroundColor: '#FFB6C1',
          selectedDayTextColor: '#ffffff',
          todayTextColor: '#FFB6C1',
          dayTextColor: '#ffffff',
          textDisabledColor: 'rgba(255,255,255,0.3)',
          monthTextColor: '#FFC8DD',
          textMonthFontWeight: 'bold',
          textDayFontSize: 14,
          textMonthFontSize: 16,
        }}
        style={styles.calendar}
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
  calendar: {
    borderRadius: 12,
    marginBottom: spacing.md,
  },
  legend: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.md,
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

