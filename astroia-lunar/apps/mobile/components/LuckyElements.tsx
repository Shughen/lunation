/**
 * LuckyElements Component
 * Display lucky numbers, colors, stones, and hours
 */

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

interface LuckyElementsProps {
  numbers: number[];
  color: string;
  colorHex: string;
  stone: string;
  favorableHours: string;
}

function LuckyItem({
  label,
  value,
  colorDot,
}: {
  label: string;
  value: string;
  colorDot?: string;
}) {
  return (
    <View style={styles.item}>
      <Text style={styles.itemLabel}>{label}</Text>
      <View style={styles.itemValueContainer}>
        {colorDot && <View style={[styles.colorDot, { backgroundColor: colorDot }]} />}
        <Text style={styles.itemValue}>{value}</Text>
      </View>
    </View>
  );
}

export function LuckyElements({
  numbers,
  color,
  colorHex,
  stone,
  favorableHours,
}: LuckyElementsProps) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Elements Chanceux</Text>
      <View style={styles.grid}>
        <LuckyItem label="Nombres" value={numbers.join(', ')} />
        <LuckyItem label="Couleur" value={color} colorDot={colorHex} />
        <LuckyItem label="Pierre" value={stone} />
        <LuckyItem label="Heures" value={favorableHours} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  title: {
    ...fonts.body,
    color: colors.gold,
    fontWeight: '600',
    marginBottom: spacing.md,
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  item: {
    width: '48%',
    marginBottom: spacing.sm,
  },
  itemLabel: {
    ...fonts.caption,
    color: colors.textMuted,
    marginBottom: spacing.xs,
  },
  itemValueContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  itemValue: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '500',
  },
  colorDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: spacing.xs,
  },
});

export default LuckyElements;
