/**
 * Calendar Tab Screen
 * Monthly view with lunar phases
 */

import React, { useState, useMemo } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Dimensions,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { haptics } from '../../services/haptics';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors: bgColors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: bgColors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

const SCREEN_WIDTH = Dimensions.get('window').width;
const DAY_SIZE = (SCREEN_WIDTH - spacing.lg * 2 - spacing.xs * 6) / 7;

const WEEKDAYS = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'];
const MONTH_NAMES = [
  'Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin',
  'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre'
];

// Simple moon phase calculation (synodic month = 29.53 days)
function getMoonPhase(date: Date): { phase: string; emoji: string } {
  // Known new moon reference: January 6, 2000
  const knownNewMoon = new Date(2000, 0, 6).getTime();
  const lunarCycle = 29.530588853;
  const daysSinceNew = (date.getTime() - knownNewMoon) / (1000 * 60 * 60 * 24);
  const currentCycleDay = ((daysSinceNew % lunarCycle) + lunarCycle) % lunarCycle;

  if (currentCycleDay < 1.85) return { phase: 'new', emoji: '' };
  if (currentCycleDay < 7.38) return { phase: 'waxing_crescent', emoji: '' };
  if (currentCycleDay < 9.23) return { phase: 'first_quarter', emoji: '' };
  if (currentCycleDay < 14.77) return { phase: 'waxing_gibbous', emoji: '' };
  if (currentCycleDay < 16.61) return { phase: 'full', emoji: '' };
  if (currentCycleDay < 22.15) return { phase: 'waning_gibbous', emoji: '' };
  if (currentCycleDay < 24.0) return { phase: 'last_quarter', emoji: '' };
  return { phase: 'waning_crescent', emoji: '' };
}

interface CalendarDay {
  date: Date;
  day: number;
  isCurrentMonth: boolean;
  isToday: boolean;
  moonPhase: { phase: string; emoji: string };
}

function generateCalendarDays(year: number, month: number): CalendarDay[] {
  const days: CalendarDay[] = [];
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  // First day of month
  const firstDay = new Date(year, month, 1);
  // Day of week (0 = Sunday, convert to Monday start)
  let startDay = firstDay.getDay();
  startDay = startDay === 0 ? 6 : startDay - 1;

  // Days in current month
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  // Days in previous month
  const daysInPrevMonth = new Date(year, month, 0).getDate();

  // Previous month days
  for (let i = startDay - 1; i >= 0; i--) {
    const date = new Date(year, month - 1, daysInPrevMonth - i);
    days.push({
      date,
      day: daysInPrevMonth - i,
      isCurrentMonth: false,
      isToday: false,
      moonPhase: getMoonPhase(date),
    });
  }

  // Current month days
  for (let i = 1; i <= daysInMonth; i++) {
    const date = new Date(year, month, i);
    date.setHours(0, 0, 0, 0);
    days.push({
      date,
      day: i,
      isCurrentMonth: true,
      isToday: date.getTime() === today.getTime(),
      moonPhase: getMoonPhase(date),
    });
  }

  // Next month days (fill to complete weeks)
  const remainingDays = 42 - days.length; // 6 rows * 7 days
  for (let i = 1; i <= remainingDays; i++) {
    const date = new Date(year, month + 1, i);
    days.push({
      date,
      day: i,
      isCurrentMonth: false,
      isToday: false,
      moonPhase: getMoonPhase(date),
    });
  }

  return days;
}

// Key phases to highlight
const KEY_PHASES = ['new', 'full', 'first_quarter', 'last_quarter'];

export default function CalendarScreen() {
  const router = useRouter();
  const today = new Date();
  const [currentMonth, setCurrentMonth] = useState(today.getMonth());
  const [currentYear, setCurrentYear] = useState(today.getFullYear());

  const calendarDays = useMemo(
    () => generateCalendarDays(currentYear, currentMonth),
    [currentYear, currentMonth]
  );

  const goToPreviousMonth = () => {
    haptics.light();
    if (currentMonth === 0) {
      setCurrentMonth(11);
      setCurrentYear(currentYear - 1);
    } else {
      setCurrentMonth(currentMonth - 1);
    }
  };

  const goToNextMonth = () => {
    haptics.light();
    if (currentMonth === 11) {
      setCurrentMonth(0);
      setCurrentYear(currentYear + 1);
    } else {
      setCurrentMonth(currentMonth + 1);
    }
  };

  const goToToday = () => {
    haptics.light();
    setCurrentMonth(today.getMonth());
    setCurrentYear(today.getFullYear());
  };

  const handleDayPress = (day: CalendarDay) => {
    if (!day.isCurrentMonth) return;
    haptics.light();
    // Navigate to lunar details for that day
    const monthStr = `${day.date.getFullYear()}-${String(day.date.getMonth() + 1).padStart(2, '0')}`;
    router.push(`/lunar-month/${monthStr}`);
  };

  // Find key phase days for the legend
  const keyPhaseDays = calendarDays.filter(
    (d) => d.isCurrentMonth && KEY_PHASES.includes(d.moonPhase.phase)
  );

  return (
    <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Calendrier Lunaire</Text>
        </View>

        {/* Month Navigation */}
        <View style={styles.monthNav}>
          <TouchableOpacity onPress={goToPreviousMonth} style={styles.navButton}>
            <Text style={styles.navButtonText}>{'<'}</Text>
          </TouchableOpacity>

          <TouchableOpacity onPress={goToToday}>
            <Text style={styles.monthTitle}>
              {MONTH_NAMES[currentMonth]} {currentYear}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity onPress={goToNextMonth} style={styles.navButton}>
            <Text style={styles.navButtonText}>{'>'}</Text>
          </TouchableOpacity>
        </View>

        {/* Weekday Headers */}
        <View style={styles.weekdaysRow}>
          {WEEKDAYS.map((day) => (
            <View key={day} style={styles.weekdayCell}>
              <Text style={styles.weekdayText}>{day}</Text>
            </View>
          ))}
        </View>

        {/* Calendar Grid */}
        <View style={styles.calendarGrid}>
          {calendarDays.map((day, index) => (
            <TouchableOpacity
              key={index}
              style={[
                styles.dayCell,
                !day.isCurrentMonth && styles.dayCellInactive,
                day.isToday && styles.dayCellToday,
              ]}
              onPress={() => handleDayPress(day)}
              disabled={!day.isCurrentMonth}
            >
              <Text
                style={[
                  styles.dayNumber,
                  !day.isCurrentMonth && styles.dayNumberInactive,
                  day.isToday && styles.dayNumberToday,
                ]}
              >
                {day.day}
              </Text>
              {day.isCurrentMonth && (
                <Text style={styles.moonEmoji}>{day.moonPhase.emoji}</Text>
              )}
            </TouchableOpacity>
          ))}
        </View>

        {/* Key Phases Legend */}
        <View style={styles.legendCard}>
          <Text style={styles.legendTitle}>Phases principales ce mois</Text>
          <View style={styles.legendGrid}>
            {keyPhaseDays.slice(0, 4).map((day, index) => (
              <View key={index} style={styles.legendItem}>
                <Text style={styles.legendEmoji}>{day.moonPhase.emoji}</Text>
                <Text style={styles.legendDate}>
                  {day.day} {MONTH_NAMES[currentMonth].slice(0, 3)}
                </Text>
                <Text style={styles.legendPhase}>
                  {day.moonPhase.phase === 'new' && 'Nouvelle Lune'}
                  {day.moonPhase.phase === 'full' && 'Pleine Lune'}
                  {day.moonPhase.phase === 'first_quarter' && '1er Quartier'}
                  {day.moonPhase.phase === 'last_quarter' && 'Dernier Quartier'}
                </Text>
              </View>
            ))}
          </View>
        </View>

        {/* Quick Access */}
        <TouchableOpacity
          style={styles.quickAccessButton}
          onPress={() => {
            haptics.light();
            const monthStr = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}`;
            router.push(`/lunar-month/${monthStr}`);
          }}
        >
          <Text style={styles.quickAccessText}>
            Voir le rapport de {MONTH_NAMES[currentMonth]}
          </Text>
        </TouchableOpacity>
      </ScrollView>
    </LinearGradientComponent>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: 100,
  },
  header: {
    alignItems: 'center',
    marginBottom: spacing.lg,
  },
  title: {
    ...fonts.h2,
    color: colors.text,
  },
  monthNav: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.lg,
  },
  navButton: {
    padding: spacing.md,
  },
  navButtonText: {
    ...fonts.h2,
    color: colors.accent,
  },
  monthTitle: {
    ...fonts.h3,
    color: colors.text,
  },
  weekdaysRow: {
    flexDirection: 'row',
    marginBottom: spacing.sm,
  },
  weekdayCell: {
    width: DAY_SIZE,
    alignItems: 'center',
    paddingVertical: spacing.xs,
  },
  weekdayText: {
    ...fonts.caption,
    color: colors.textMuted,
    fontWeight: '600',
  },
  calendarGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.xs,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  dayCell: {
    width: DAY_SIZE,
    height: DAY_SIZE + 10,
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: borderRadius.sm,
  },
  dayCellInactive: {
    opacity: 0.3,
  },
  dayCellToday: {
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    borderWidth: 1,
    borderColor: colors.accent,
  },
  dayNumber: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '500',
  },
  dayNumberInactive: {
    color: colors.textDark,
  },
  dayNumberToday: {
    color: colors.accent,
    fontWeight: '700',
  },
  moonEmoji: {
    fontSize: 12,
    marginTop: 2,
  },
  legendCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginTop: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  legendTitle: {
    ...fonts.body,
    color: colors.gold,
    fontWeight: '600',
    marginBottom: spacing.md,
  },
  legendGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  legendItem: {
    width: '48%',
    alignItems: 'center',
    paddingVertical: spacing.sm,
    marginBottom: spacing.sm,
  },
  legendEmoji: {
    fontSize: 24,
    marginBottom: spacing.xs,
  },
  legendDate: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
  },
  legendPhase: {
    ...fonts.caption,
    color: colors.textMuted,
  },
  quickAccessButton: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginTop: spacing.md,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: colors.accent,
  },
  quickAccessText: {
    ...fonts.body,
    color: colors.accent,
  },
});
