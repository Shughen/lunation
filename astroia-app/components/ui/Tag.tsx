import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { color, space, radius, type as typography } from '@/theme/tokens';

interface TagProps {
  icon?: React.ReactNode;
  label: string;
  variant?: 'default' | 'success' | 'warning' | 'danger' | 'info';
}

/**
 * Tag - Badge informatif avec icône optionnelle
 */
export default function Tag({ icon, label, variant = 'default' }: TagProps) {
  const variantColors = {
    default: { bg: color.surfaceElevated, text: color.textMuted },
    success: { bg: color.successSoft, text: color.success },
    warning: { bg: color.warningSoft, text: color.warning },
    danger: { bg: color.dangerSoft, text: color.danger },
    info: { bg: color.infoSoft, text: color.info },
  };

  const colors = variantColors[variant];

  return (
    <View style={[styles.container, { backgroundColor: colors.bg }]}>
      {icon && <View style={styles.icon}>{icon}</View>}
      <Text style={[styles.label, { color: colors.text }]}>{label}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: space.xs,
    paddingHorizontal: space.sm,
    borderRadius: radius.sm,
    alignSelf: 'flex-start',
  },
  icon: {
    marginRight: space.xs / 2,
  },
  label: {
    ...typography.bodySm,
    fontWeight: '600',
  },
});

