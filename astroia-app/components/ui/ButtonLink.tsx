import React from 'react';
import { Text, StyleSheet, Pressable, PressableProps } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { color, space, type as typography, hitSlop as hitSlopTokens } from '@/theme/tokens';

interface ButtonLinkProps extends PressableProps {
  children: string;
  icon?: keyof typeof Ionicons.glyphMap;
  variant?: 'default' | 'brand' | 'muted';
}

/**
 * ButtonLink - Bouton lien secondaire avec icône chevron
 */
export default function ButtonLink({
  children,
  icon = 'chevron-forward',
  variant = 'default',
  ...pressableProps
}: ButtonLinkProps) {
  const variantColors = {
    default: color.text,
    brand: color.brand,
    muted: color.textMuted,
  };

  const textColor = variantColors[variant];

  return (
    <Pressable
      style={({ pressed }) => [
        styles.container,
        pressed && styles.pressed,
      ]}
      hitSlop={hitSlopTokens.md}
      accessibilityRole="link"
      {...pressableProps}
    >
      <Text style={[styles.text, { color: textColor }]}>{children}</Text>
      <Ionicons name={icon} size={18} color={textColor} />
    </Pressable>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.xs / 2,
    alignSelf: 'flex-start',
  },
  text: {
    ...typography.bodySm,
    fontWeight: '600',
  },
  pressed: {
    opacity: 0.6,
  },
});

