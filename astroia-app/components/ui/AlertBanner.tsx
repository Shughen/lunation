import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { color, space, radius, type as typography } from '@/theme/tokens';

interface AlertBannerProps {
  variant?: 'info' | 'warning' | 'success' | 'danger';
  title?: string;
  children: React.ReactNode;
}

/**
 * AlertBanner - Bannière d'alerte avec icône et titre
 */
export default function AlertBanner({
  variant = 'info',
  title,
  children,
}: AlertBannerProps) {
  const variantConfig = {
    info: {
      icon: 'information-circle' as const,
      borderColor: color.info + '33',
      backgroundColor: color.info + '14',
      iconColor: color.info,
      textColor: color.text,
    },
    warning: {
      icon: 'alert-circle' as const,
      borderColor: color.warning + '33',
      backgroundColor: color.warning + '14',
      iconColor: color.warning,
      textColor: color.text,
    },
    success: {
      icon: 'checkmark-circle' as const,
      borderColor: color.success + '33',
      backgroundColor: color.success + '14',
      iconColor: color.success,
      textColor: color.text,
    },
    danger: {
      icon: 'close-circle' as const,
      borderColor: color.danger + '33',
      backgroundColor: color.danger + '14',
      iconColor: color.danger,
      textColor: color.text,
    },
  };

  const config = variantConfig[variant];

  return (
    <View
      style={[
        styles.container,
        {
          borderColor: config.borderColor,
          backgroundColor: config.backgroundColor,
        },
      ]}
    >
      <View style={styles.iconContainer}>
        <Ionicons name={config.icon} size={24} color={config.iconColor} />
      </View>
      <View style={styles.content}>
        {title && (
          <Text style={[styles.title, { color: config.textColor }]}>
            {title}
          </Text>
        )}
        <Text style={[styles.body, { color: config.textColor }]}>
          {children}
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    borderWidth: 1,
    borderRadius: radius.md,
    padding: space.md,
    gap: space.sm,
  },
  iconContainer: {
    paddingTop: 2, // Aligner avec baseline du texte
  },
  content: {
    flex: 1,
    gap: space.xs / 2,
  },
  title: {
    ...typography.label,
  },
  body: {
    ...typography.bodySm,
    maxWidth: 340,
  },
});

