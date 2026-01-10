import React from 'react';
import { StyleSheet, Pressable, PressableProps } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { color, space, radius, hitSlop as hitSlopTokens } from '@/theme/tokens';

interface IconButtonProps extends PressableProps {
  icon: keyof typeof Ionicons.glyphMap;
  size?: number;
  variant?: 'default' | 'ghost' | 'danger';
  accessibilityLabel: string;
}

/**
 * IconButton - Bouton icon seul avec variantes
 */
export default function IconButton({
  icon,
  size = 24,
  variant = 'default',
  accessibilityLabel,
  ...pressableProps
}: IconButtonProps) {
  const variantStyles = {
    default: {
      backgroundColor: color.surfaceElevated,
      iconColor: color.text,
    },
    ghost: {
      backgroundColor: 'transparent',
      iconColor: color.textMuted,
    },
    danger: {
      backgroundColor: color.dangerSoft,
      iconColor: color.danger,
    },
  };

  const styles = variantStyles[variant];

  return (
    <Pressable
      style={({ pressed }) => [
        styleSheet.container,
        { backgroundColor: styles.backgroundColor },
        pressed && styleSheet.pressed,
      ]}
      hitSlop={hitSlopTokens.md}
      accessibilityRole="button"
      accessibilityLabel={accessibilityLabel}
      {...pressableProps}
    >
      <Ionicons name={icon} size={size} color={styles.iconColor} />
    </Pressable>
  );
}

const styleSheet = StyleSheet.create({
  container: {
    width: 40,
    height: 40,
    borderRadius: radius.sm,
    alignItems: 'center',
    justifyContent: 'center',
  },
  pressed: {
    opacity: 0.6,
  },
});

