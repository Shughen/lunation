/**
 * TimeWheelPicker - Sélecteur d'heure simplifié
 *
 * Approche simple: deux champs de saisie pour heures et minutes
 * avec clavier numérique
 */

import React, { useState, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  Dimensions,
} from 'react-native';
import { colors, spacing, borderRadius } from '../../constants/theme';

interface TimeWheelPickerProps {
  value: string; // Format "HH:MM"
  onChange: (time: string) => void;
}

export function TimeWheelPicker({ value, onChange }: TimeWheelPickerProps) {
  const [hoursStr, minutesStr] = value.split(':');
  const [hours, setHours] = useState(hoursStr || '12');
  const [minutes, setMinutes] = useState(minutesStr || '00');

  const minutesRef = useRef<TextInput>(null);

  const handleHoursChange = (text: string) => {
    // Garder seulement les chiffres
    const cleaned = text.replace(/[^0-9]/g, '');
    if (cleaned.length <= 2) {
      const num = parseInt(cleaned, 10);
      if (cleaned === '' || (num >= 0 && num <= 23)) {
        setHours(cleaned);
        if (cleaned.length === 2) {
          // Auto-focus sur les minutes
          minutesRef.current?.focus();
        }
      }
    }
  };

  const handleMinutesChange = (text: string) => {
    const cleaned = text.replace(/[^0-9]/g, '');
    if (cleaned.length <= 2) {
      const num = parseInt(cleaned, 10);
      if (cleaned === '' || (num >= 0 && num <= 59)) {
        setMinutes(cleaned);
      }
    }
  };

  const handleHoursBlur = () => {
    const h = hours === '' ? '12' : hours.padStart(2, '0');
    const num = parseInt(h, 10);
    const validHours = Math.min(23, Math.max(0, num)).toString().padStart(2, '0');
    setHours(validHours);
    updateTime(validHours, minutes.padStart(2, '0'));
  };

  const handleMinutesBlur = () => {
    const m = minutes === '' ? '00' : minutes.padStart(2, '0');
    const num = parseInt(m, 10);
    const validMinutes = Math.min(59, Math.max(0, num)).toString().padStart(2, '0');
    setMinutes(validMinutes);
    updateTime(hours.padStart(2, '0'), validMinutes);
  };

  const updateTime = (h: string, m: string) => {
    onChange(`${h}:${m}`);
  };

  // Boutons rapides pour ajuster +/- 1
  const adjustHours = (delta: number) => {
    const current = parseInt(hours || '12', 10);
    const newVal = (current + delta + 24) % 24; // Wrap around
    const newHours = newVal.toString().padStart(2, '0');
    setHours(newHours);
    updateTime(newHours, minutes.padStart(2, '0'));
  };

  const adjustMinutes = (delta: number) => {
    const current = parseInt(minutes || '0', 10);
    const newVal = (current + delta + 60) % 60; // Wrap around
    const newMinutes = newVal.toString().padStart(2, '0');
    setMinutes(newMinutes);
    updateTime(hours.padStart(2, '0'), newMinutes);
  };

  const { width: screenWidth } = Dimensions.get('window');
  const pickerWidth = Math.min(screenWidth - spacing.xl * 2, 220);

  return (
    <View style={[styles.container, { width: pickerWidth }]}>
      {/* Heures */}
      <View style={styles.column}>
        <TouchableOpacity
          style={styles.adjustButton}
          onPress={() => adjustHours(1)}
          activeOpacity={0.7}
        >
          <Text style={styles.adjustButtonText}>▲</Text>
        </TouchableOpacity>

        <TextInput
          style={styles.input}
          value={hours}
          onChangeText={handleHoursChange}
          onBlur={handleHoursBlur}
          keyboardType="number-pad"
          maxLength={2}
          selectTextOnFocus
          placeholder="12"
          placeholderTextColor="rgba(255,255,255,0.3)"
        />

        <TouchableOpacity
          style={styles.adjustButton}
          onPress={() => adjustHours(-1)}
          activeOpacity={0.7}
        >
          <Text style={styles.adjustButtonText}>▼</Text>
        </TouchableOpacity>
      </View>

      {/* Séparateur */}
      <Text style={styles.separator}>:</Text>

      {/* Minutes */}
      <View style={styles.column}>
        <TouchableOpacity
          style={styles.adjustButton}
          onPress={() => adjustMinutes(5)}
          activeOpacity={0.7}
        >
          <Text style={styles.adjustButtonText}>▲</Text>
        </TouchableOpacity>

        <TextInput
          ref={minutesRef}
          style={styles.input}
          value={minutes}
          onChangeText={handleMinutesChange}
          onBlur={handleMinutesBlur}
          keyboardType="number-pad"
          maxLength={2}
          selectTextOnFocus
          placeholder="00"
          placeholderTextColor="rgba(255,255,255,0.3)"
        />

        <TouchableOpacity
          style={styles.adjustButton}
          onPress={() => adjustMinutes(-5)}
          activeOpacity={0.7}
        >
          <Text style={styles.adjustButtonText}>▼</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
  },
  column: {
    alignItems: 'center',
  },
  input: {
    fontSize: 32,
    fontWeight: 'bold',
    color: colors.text,
    textAlign: 'center',
    width: 70,
    paddingVertical: spacing.sm,
    fontVariant: ['tabular-nums'],
  },
  separator: {
    fontSize: 32,
    fontWeight: 'bold',
    color: colors.accent,
    marginHorizontal: spacing.sm,
  },
  adjustButton: {
    padding: spacing.xs,
    paddingHorizontal: spacing.md,
  },
  adjustButtonText: {
    fontSize: 18,
    color: colors.accent,
  },
});

export default TimeWheelPicker;
