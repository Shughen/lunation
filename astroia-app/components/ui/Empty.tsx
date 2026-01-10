import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { color, space, radius, type as typography } from '@/theme/tokens';

interface EmptyProps {
  icon?: keyof typeof Ionicons.glyphMap;
  title: string;
  subtitle?: string;
  actionLabel?: string;
  onActionPress?: () => void;
}

/**
 * Empty - État vide avec CTA optionnel
 */
export default function Empty({
  icon = 'document-outline',
  title,
  subtitle,
  actionLabel,
  onActionPress,
}: EmptyProps) {
  return (
    <View style={styles.container}>
      <View style={styles.iconContainer}>
        <Ionicons name={icon} size={64} color={color.textMuted} />
      </View>

      <Text style={styles.title}>{title}</Text>
      {subtitle && <Text style={styles.subtitle}>{subtitle}</Text>}

      {actionLabel && onActionPress && (
        <TouchableOpacity
          style={styles.button}
          onPress={onActionPress}
          activeOpacity={0.7}
        >
          <Text style={styles.buttonText}>{actionLabel}</Text>
        </TouchableOpacity>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: space['3xl'],
    paddingHorizontal: space.xl,
  },
  iconContainer: {
    marginBottom: space.lg,
    opacity: 0.5,
  },
  title: {
    ...typography.h3,
    color: color.text,
    textAlign: 'center',
    marginBottom: space.xs,
  },
  subtitle: {
    ...typography.bodySm,
    color: color.textMuted,
    textAlign: 'center',
    maxWidth: 280,
    lineHeight: 20,
  },
  button: {
    marginTop: space.xl,
    backgroundColor: color.brand,
    paddingVertical: space.sm,
    paddingHorizontal: space.xl,
    borderRadius: radius.md,
  },
  buttonText: {
    ...typography.label,
    color: color.text,
  },
});

