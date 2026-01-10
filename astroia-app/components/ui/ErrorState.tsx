import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { color, space, radius, type as typography } from '@/theme/tokens';

interface ErrorStateProps {
  title?: string;
  message: string;
  retryLabel?: string;
  onRetry?: () => void;
}

/**
 * ErrorState - État d'erreur avec bouton retry
 */
export default function ErrorState({
  title = 'Une erreur est survenue',
  message,
  retryLabel = 'Réessayer',
  onRetry,
}: ErrorStateProps) {
  return (
    <View style={styles.container}>
      <View style={styles.iconContainer}>
        <Ionicons name="alert-circle" size={64} color={color.danger} />
      </View>

      <Text style={styles.title}>{title}</Text>
      <Text style={styles.message}>{message}</Text>

      {onRetry && (
        <TouchableOpacity
          style={styles.button}
          onPress={onRetry}
          activeOpacity={0.7}
        >
          <Ionicons name="refresh" size={18} color={color.text} />
          <Text style={styles.buttonText}>{retryLabel}</Text>
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
    opacity: 0.8,
  },
  title: {
    ...typography.h3,
    color: color.text,
    textAlign: 'center',
    marginBottom: space.xs,
  },
  message: {
    ...typography.bodySm,
    color: color.textMuted,
    textAlign: 'center',
    maxWidth: 300,
    lineHeight: 20,
  },
  button: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.xs,
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

