import React from 'react';
import { View, Text, StyleSheet, Pressable, PressableProps } from 'react-native';
import { color, space, radius, shadow, type as typography } from '@/theme/tokens';
import ButtonLink from './ButtonLink';

interface SectionCardProps extends PressableProps {
  title: string;
  subtitle?: string;
  icon?: React.ReactNode;
  children?: React.ReactNode;
  footerLink?: {
    label: string;
    onPress: () => void;
  };
}

/**
 * SectionCard - Carte de section unifiée pour Home
 */
export default function SectionCard({
  title,
  subtitle,
  icon,
  children,
  footerLink,
  onPress,
  ...pressableProps
}: SectionCardProps) {
  const Wrapper = onPress ? Pressable : View;

  return (
    <Wrapper
      style={({ pressed }) => [
        styles.container,
        onPress && pressed && styles.pressed,
      ]}
      onPress={onPress}
      accessibilityRole={onPress ? 'button' : undefined}
      {...pressableProps}
    >
      {/* Header */}
      <View style={styles.header}>
        {icon && <View style={styles.iconContainer}>{icon}</View>}
        <View style={styles.headerText}>
          <Text style={styles.title}>{title}</Text>
          {subtitle && <Text style={styles.subtitle}>{subtitle}</Text>}
        </View>
      </View>

      {/* Content */}
      {children && <View style={styles.content}>{children}</View>}

      {/* Footer Link */}
      {footerLink && (
        <View style={styles.footer}>
          <ButtonLink variant="brand" onPress={footerLink.onPress}>
            {footerLink.label}
          </ButtonLink>
        </View>
      )}
    </Wrapper>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: color.surface,
    borderRadius: radius.lg,
    padding: space.xl,
    ...shadow.md,
  },
  pressed: {
    opacity: 0.9,
    transform: [{ scale: 0.98 }],
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.sm,
    marginBottom: space.md,
  },
  iconContainer: {
    alignSelf: 'flex-start',
    paddingTop: 2, // Aligner avec baseline du titre
  },
  headerText: {
    flex: 1,
    gap: space.xs / 2,
  },
  title: {
    ...typography.h3,
    color: color.text,
  },
  subtitle: {
    ...typography.bodySm,
    color: color.textMuted,
    lineHeight: 20, // Augmenté pour lisibilité
  },
  content: {
    marginBottom: space.md,
  },
  footer: {
    paddingTop: space.sm,
    borderTopWidth: 1,
    borderTopColor: color.border,
  },
});

