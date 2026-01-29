/**
 * DomainCard Component
 * Card for horoscope domains (Love, Career, etc.)
 */

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Svg, { Path, Circle, G } from 'react-native-svg';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

interface DomainCardProps {
  domain: 'love' | 'career' | 'health' | 'finance';
  title: string;
  description: string;
  subtitle?: string;
}

// Icon components for each domain
function LoveIcon({ size = 20, color = colors.fire }: { size?: number; color?: string }) {
  return (
    <Svg width={size} height={size} viewBox="0 0 24 24" fill="none">
      <Path
        d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"
        fill={color}
        opacity={0.2}
        stroke={color}
        strokeWidth={1.5}
      />
    </Svg>
  );
}

function CareerIcon({ size = 20, color = colors.accent }: { size?: number; color?: string }) {
  return (
    <Svg width={size} height={size} viewBox="0 0 24 24" fill="none">
      <Path
        d="M20 7H4c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2z"
        stroke={color}
        strokeWidth={1.5}
        fill={`${color}20`}
      />
      <Path
        d="M16 7V5c0-1.1-.9-2-2-2h-4c-1.1 0-2 .9-2 2v2"
        stroke={color}
        strokeWidth={1.5}
        strokeLinecap="round"
      />
      <Circle cx="12" cy="13" r="2" fill={color} />
    </Svg>
  );
}

function HealthIcon({ size = 20, color = colors.success }: { size?: number; color?: string }) {
  return (
    <Svg width={size} height={size} viewBox="0 0 24 24" fill="none">
      <Path
        d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"
        stroke={color}
        strokeWidth={1.5}
        fill={`${color}20`}
      />
      <Path
        d="M12 8v8M8 12h8"
        stroke={color}
        strokeWidth={2}
        strokeLinecap="round"
      />
    </Svg>
  );
}

function FinanceIcon({ size = 20, color = colors.gold }: { size?: number; color?: string }) {
  return (
    <Svg width={size} height={size} viewBox="0 0 24 24" fill="none">
      <Circle
        cx="12"
        cy="12"
        r="9"
        stroke={color}
        strokeWidth={1.5}
        fill={`${color}20`}
      />
      <Path
        d="M12 6v12M15 9c0-1.1-1.34-2-3-2s-3 .9-3 2 1.34 2 3 2 3 .9 3 2-1.34 2-3 2-3-.9-3-2"
        stroke={color}
        strokeWidth={1.5}
        strokeLinecap="round"
      />
    </Svg>
  );
}

const DOMAIN_CONFIG = {
  love: {
    icon: LoveIcon,
    color: colors.fire,
  },
  career: {
    icon: CareerIcon,
    color: colors.accent,
  },
  health: {
    icon: HealthIcon,
    color: colors.success,
  },
  finance: {
    icon: FinanceIcon,
    color: colors.gold,
  },
};

export function DomainCard({ domain, title, description, subtitle }: DomainCardProps) {
  const config = DOMAIN_CONFIG[domain];
  const IconComponent = config.icon;

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <IconComponent size={20} color={config.color} />
        <Text style={[styles.title, { color: config.color }]}>{title}</Text>
      </View>
      <Text style={styles.description}>{description}</Text>
      {subtitle && <Text style={styles.subtitle}>{subtitle}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.sm,
    gap: spacing.xs,
  },
  title: {
    ...fonts.body,
    fontWeight: '600',
  },
  description: {
    ...fonts.bodySmall,
    color: colors.text,
    lineHeight: 18,
    marginBottom: spacing.xs,
  },
  subtitle: {
    ...fonts.caption,
    color: colors.textMuted,
  },
});

export default DomainCard;
