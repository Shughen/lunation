import React, { useEffect, useRef } from 'react';
import { View, StyleSheet, Animated, ViewStyle } from 'react-native';
import { color, radius, animation } from '@/theme/tokens';

interface SkeletonProps {
  width?: number | string;
  height?: number;
  borderRadius?: number;
  style?: ViewStyle;
}

/**
 * Skeleton - Placeholder animé pour le chargement
 */
export default function Skeleton({
  width = '100%',
  height = 20,
  borderRadius: customRadius,
  style,
}: SkeletonProps) {
  const opacity = useRef(new Animated.Value(0.3)).current;

  useEffect(() => {
    Animated.loop(
      Animated.sequence([
        Animated.timing(opacity, {
          toValue: 0.7,
          duration: animation.slow * 2,
          useNativeDriver: true,
        }),
        Animated.timing(opacity, {
          toValue: 0.3,
          duration: animation.slow * 2,
          useNativeDriver: true,
        }),
      ])
    ).start();
  }, [opacity]);

  // Convertir width string en format compatible avec Animated.View
  const widthStyle = typeof width === 'string' 
    ? { width: width as `${number}%` | 'auto' }
    : { width };

  return (
    <Animated.View
      style={[
        styles.skeleton,
        {
          ...widthStyle,
          height,
          borderRadius: customRadius !== undefined ? customRadius : radius.sm,
          opacity,
        },
        style,
      ]}
    />
  );
}

/**
 * SkeletonGroup - Groupe de skeletons pour cards complexes
 */
export function SkeletonGroup({ count = 3 }: { count?: number }) {
  return (
    <View style={styles.group}>
      {Array.from({ length: count }).map((_, index) => (
        <View key={index} style={styles.item}>
          <Skeleton width={80} height={80} borderRadius={radius.md} />
          <View style={styles.textGroup}>
            <Skeleton width="70%" height={18} />
            <Skeleton width="90%" height={14} style={{ marginTop: 8 }} />
            <Skeleton width="60%" height={14} style={{ marginTop: 4 }} />
          </View>
        </View>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  skeleton: {
    backgroundColor: color.surfaceElevated,
  },
  group: {
    gap: 16,
  },
  item: {
    flexDirection: 'row',
    gap: 16,
    backgroundColor: color.surface,
    padding: 16,
    borderRadius: radius.md,
  },
  textGroup: {
    flex: 1,
    justifyContent: 'center',
  },
});

