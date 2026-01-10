import React from 'react';
import { View, Text, Pressable, StyleSheet } from 'react-native';
import { color, space, radius, type as typography, hitSlop as hitSlopTokens } from '@/theme/tokens';

interface BigThreeItem {
  sign?: string;
  degree?: number;
  element?: string;
  emoji?: string;
}

interface NatalSummaryCardProps {
  sun?: BigThreeItem;
  moon?: BigThreeItem;
  ascendant?: BigThreeItem;
  onPress: () => void;
}

export default React.memo(function NatalSummaryCard({ 
  sun, 
  moon, 
  ascendant, 
  onPress 
}: NatalSummaryCardProps) {
  const hasData = sun || moon || ascendant;

  const renderBigThreeItem = (label: string, item?: BigThreeItem) => {
    if (!item || !item.sign) return null;
    
    return (
      <View key={label} style={styles.bigThreeItem}>
        <Text style={styles.bigThreeLabel}>{label}</Text>
        <Text style={styles.bigThreeValue}>
          {item.emoji} {item.sign}
          {item.degree !== undefined && ` ${item.degree}°`}
          {item.element && ` (${item.element})`}
        </Text>
      </View>
    );
  };

  return (
    <Pressable
      onPress={onPress}
      accessible={true}
      accessibilityRole="button"
      accessibilityLabel="Thème natal. Toucher pour voir le thème complet."
      accessibilityHint="Toucher deux fois pour ouvrir le thème natal"
      style={({ pressed }) => [
        styles.card,
        pressed && styles.cardPressed,
      ]}
      hitSlop={hitSlopTokens.md}
    >
      <Text style={styles.label}>THÈME NATAL</Text>
      
      {hasData ? (
        <View style={styles.bigThreeContainer}>
          {renderBigThreeItem('Soleil', sun)}
          {renderBigThreeItem('Lune', moon)}
          {renderBigThreeItem('Ascendant', ascendant)}
        </View>
      ) : (
        <Text style={styles.placeholder}>
          Configure ton thème natal pour voir tes Big Three.
        </Text>
      )}
      
      <Text style={styles.cta}>→ Voir mon thème complet</Text>
    </Pressable>
  );
});

const styles = StyleSheet.create({
  card: {
    marginHorizontal: space.md,
    marginBottom: space.md,
    borderRadius: radius.md,
    padding: space.md,
    backgroundColor: color.surface,
    borderWidth: 1,
    borderColor: color.border,
  },
  cardPressed: {
    opacity: 0.7,
    transform: [{ scale: 0.98 }],
  },
  label: {
    ...typography.label,
    color: color.brand,
    letterSpacing: 1.2,
    marginBottom: space.sm,
  },
  bigThreeContainer: {
    marginTop: space.xs,
  },
  bigThreeItem: {
    marginBottom: space.sm,
  },
  bigThreeLabel: {
    ...typography.bodySm,
    color: color.textMuted,
    marginBottom: 2,
  },
  bigThreeValue: {
    ...typography.h4,
    color: color.text,
    fontWeight: '700',
  },
  placeholder: {
    ...typography.body,
    color: color.textMuted,
    fontStyle: 'italic',
    marginTop: space.xs,
  },
  cta: {
    ...typography.bodySm,
    color: color.brand,
    fontWeight: '600',
    marginTop: space.md,
  },
});

