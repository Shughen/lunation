import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { color, space, radius, type as typography } from '@/theme/tokens';

/**
 * Légende expliquant les couleurs du calendrier de cycle
 */
export default function FertilityLegend() {
  const items = [
    { color: '#FF6B9D', label: 'Règles', emoji: '🩸' },
    { color: '#FFD93D', label: 'Fenêtre fertile', emoji: '🌱' },
    { color: '#FFA500', label: 'Ovulation', emoji: '🥚' },
  ];

  return (
    <View style={styles.container}>
      <Text style={styles.title}>📖 Légende</Text>
      
      <View style={styles.itemsRow}>
        {items.map((item, index) => (
          <View key={index} style={styles.item}>
            <View style={[styles.dot, { backgroundColor: item.color }]} />
            <Text style={styles.emoji}>{item.emoji}</Text>
            <Text style={styles.label}>{item.label}</Text>
          </View>
        ))}
      </View>
      
      <Text style={styles.disclaimer}>
        Prédictions basées sur ta moyenne de cycles. Les données peuvent varier.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: space.lg,
    marginTop: space.lg,
    marginBottom: space.md,
    padding: space.md,
    backgroundColor: `${color.brand}11`,
    borderRadius: radius.xl,
    borderWidth: 1,
    borderColor: `${color.brand}22`,
  },
  title: {
    ...typography.label,
    color: color.text,
    marginBottom: space.sm,
    textAlign: 'center',
  },
  itemsRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    marginBottom: space.sm,
  },
  item: {
    alignItems: 'center',
    gap: 4,
  },
  dot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginBottom: 2,
  },
  emoji: {
    fontSize: 18,
    marginBottom: 2,
  },
  label: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
  },
  disclaimer: {
    ...typography.caption,
    color: color.textMuted,
    textAlign: 'center',
    fontStyle: 'italic',
    marginTop: space.xs,
  },
});

