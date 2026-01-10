import React from 'react';
import { View, Text, Pressable, ActivityIndicator, StyleSheet } from 'react-native';
import { color, space, radius, type as typography, hitSlop as hitSlopTokens } from '@/theme/tokens';

interface LunarRevolutionHeroProps {
  moonSign?: string;
  house?: number;
  isLoading?: boolean;
  onPress: () => void;
}

export default React.memo(function LunarRevolutionHero({ 
  moonSign, 
  house, 
  isLoading = false,
  onPress 
}: LunarRevolutionHeroProps) {
  const hasData = moonSign && house;

  return (
    <Pressable
      onPress={onPress}
      accessible={true}
      accessibilityRole="button"
      accessibilityLabel="Révolution lunaire du mois. Toucher pour voir les détails complets."
      accessibilityHint="Toucher deux fois pour ouvrir la révolution lunaire"
      style={({ pressed }) => [
        styles.card,
        pressed && styles.cardPressed,
      ]}
      hitSlop={hitSlopTokens.md}
    >
      <Text style={styles.label}>🌙 RÉVOLUTION LUNAIRE DU MOIS</Text>
      
      {isLoading ? (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="small" color={color.brand} />
          <Text style={styles.loadingText}>Chargement...</Text>
        </View>
      ) : hasData ? (
        <>
          <Text style={styles.title}>
            Lune en {moonSign}
          </Text>
          <Text style={styles.subtitle}>
            Maison {house}
          </Text>
          <Text style={styles.description}>
            Découvre comment la Lune du mois active ton thème natal et influence tes tendances émotionnelles.
          </Text>
        </>
      ) : (
        <>
          <Text style={styles.title}>
            Révolution lunaire
          </Text>
          <Text style={styles.description}>
            Connecte ta carte natale avec la Lune du mois pour des insights personnalisés.
          </Text>
        </>
      )}
      
      <Text style={styles.cta}>→ Voir ma Révolution lunaire</Text>
    </Pressable>
  );
});

const styles = StyleSheet.create({
  card: {
    marginHorizontal: space.md,
    marginBottom: space.md,
    borderRadius: radius.lg,
    padding: space.lg,
    backgroundColor: color.surfaceElevated,
    borderWidth: 1,
    borderColor: color.border,
  },
  cardPressed: {
    opacity: 0.7,
    transform: [{ scale: 0.98 }],
  },
  label: {
    ...typography.label,
    color: color.brand,
    letterSpacing: 1.2,
    marginBottom: space.sm,
  },
  title: {
    ...typography.h2,
    color: color.text,
    fontWeight: '800',
    marginBottom: space.xs,
  },
  subtitle: {
    ...typography.h4,
    color: color.textSecondary,
    marginBottom: space.sm,
  },
  description: {
    ...typography.body,
    color: color.textMuted,
    marginTop: space.xs,
    lineHeight: 20,
  },
  cta: {
    ...typography.bodySm,
    color: color.brand,
    fontWeight: '600',
    marginTop: space.md,
  },
  loadingContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: space.md,
  },
  loadingText: {
    ...typography.body,
    color: color.textMuted,
    marginLeft: space.sm,
  },
});

