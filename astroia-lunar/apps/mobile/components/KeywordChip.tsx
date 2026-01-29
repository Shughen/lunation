/**
 * KeywordChip Component
 * Badge-style chip for keywords/tags
 */

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

interface KeywordChipProps {
  label: string;
  variant?: 'default' | 'accent' | 'gold';
}

export function KeywordChip({ label, variant = 'default' }: KeywordChipProps) {
  const getVariantStyles = () => {
    switch (variant) {
      case 'accent':
        return {
          container: styles.containerAccent,
          text: styles.textAccent,
        };
      case 'gold':
        return {
          container: styles.containerGold,
          text: styles.textGold,
        };
      default:
        return {
          container: styles.containerDefault,
          text: styles.textDefault,
        };
    }
  };

  const variantStyles = getVariantStyles();

  return (
    <View style={[styles.container, variantStyles.container]}>
      <Text style={[styles.text, variantStyles.text]}>{label}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.xs,
    borderRadius: borderRadius.full,
    borderWidth: 1,
    marginRight: spacing.xs,
    marginBottom: spacing.xs,
  },
  containerDefault: {
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  containerAccent: {
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    borderColor: colors.accent,
  },
  containerGold: {
    backgroundColor: 'rgba(255, 215, 0, 0.1)',
    borderColor: colors.gold,
  },
  text: {
    ...fonts.caption,
    fontWeight: '500',
  },
  textDefault: {
    color: colors.textMuted,
  },
  textAccent: {
    color: colors.accent,
  },
  textGold: {
    color: colors.gold,
  },
});

export default KeywordChip;
