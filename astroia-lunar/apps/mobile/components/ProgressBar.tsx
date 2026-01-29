/**
 * ProgressBar Component
 * Animated progress bar for horoscope metrics
 */

import React, { useEffect, useRef } from 'react';
import { View, Text, StyleSheet, Animated } from 'react-native';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

interface ProgressBarProps {
  label: string;
  value: number; // 0-100
  color?: string;
  showPercentage?: boolean;
  animate?: boolean;
}

export function ProgressBar({
  label,
  value,
  color = colors.accent,
  showPercentage = true,
  animate = true,
}: ProgressBarProps) {
  const animatedWidth = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    if (animate) {
      Animated.timing(animatedWidth, {
        toValue: value,
        duration: 800,
        useNativeDriver: false,
      }).start();
    } else {
      animatedWidth.setValue(value);
    }
  }, [value, animate]);

  const widthInterpolated = animatedWidth.interpolate({
    inputRange: [0, 100],
    outputRange: ['0%', '100%'],
  });

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.label}>{label}</Text>
        {showPercentage && (
          <Text style={[styles.percentage, { color }]}>{Math.round(value)}%</Text>
        )}
      </View>
      <View style={styles.trackContainer}>
        <View style={styles.track}>
          <Animated.View
            style={[
              styles.fill,
              {
                width: widthInterpolated,
                backgroundColor: color,
              },
            ]}
          />
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: spacing.md,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.xs,
  },
  label: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  percentage: {
    ...fonts.body,
    fontWeight: '600',
  },
  trackContainer: {
    height: 8,
    borderRadius: 4,
    overflow: 'hidden',
  },
  track: {
    flex: 1,
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderRadius: 4,
    overflow: 'hidden',
  },
  fill: {
    height: '100%',
    borderRadius: 4,
  },
});

export default ProgressBar;
