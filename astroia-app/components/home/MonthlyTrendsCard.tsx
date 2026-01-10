import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { color, space, radius, type as typography } from '@/theme/tokens';

interface MonthlyTrendsCardProps {
  focus?: string;
  summary?: string;
  isLoading?: boolean;
}

export default React.memo(function MonthlyTrendsCard({ 
  focus, 
  summary, 
  isLoading = false 
}: MonthlyTrendsCardProps) {
  const hasData = focus || summary;

  return (
    <View style={styles.card}>
      <Text style={styles.label}>TENDANCES DU MOIS</Text>
      
      {isLoading ? (
        <Text style={styles.placeholder}>Chargement des tendances...</Text>
      ) : hasData ? (
        <>
          {focus && (
            <Text style={styles.focus}>
              Focus : {focus}
            </Text>
          )}
          {summary && (
            <Text style={styles.summary}>
              {summary}
            </Text>
          )}
        </>
      ) : (
        <Text style={styles.placeholder}>
          Les tendances du mois seront disponibles une fois ta révolution lunaire calculée.
        </Text>
      )}
    </View>
  );
});

const styles = StyleSheet.create({
  card: {
    marginHorizontal: space.md,
    marginBottom: space.md,
    borderRadius: radius.md,
    padding: space.md,
    backgroundColor: color.surface,
    borderWidth: 1,
    borderColor: color.border,
  },
  label: {
    ...typography.label,
    color: color.brand,
    letterSpacing: 1.2,
    marginBottom: space.sm,
  },
  focus: {
    ...typography.h4,
    color: color.text,
    fontWeight: '700',
    marginBottom: space.xs,
  },
  summary: {
    ...typography.body,
    color: color.textSecondary,
    marginTop: space.xs,
    lineHeight: 20,
  },
  placeholder: {
    ...typography.body,
    color: color.textMuted,
    fontStyle: 'italic',
    lineHeight: 20,
  },
});

