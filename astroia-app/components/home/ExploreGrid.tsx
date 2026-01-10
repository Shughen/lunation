import React from 'react';
import { View, Text, StyleSheet, Pressable, Dimensions } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { color, space, radius, type as typography, hitSlop as hitSlopTokens } from '@/theme/tokens';

interface ExploreTileProps {
  icon: keyof typeof Ionicons.glyphMap;
  label: string;
  onPress: () => void;
  accessibilityLabel: string;
}

const Tile = React.memo(function Tile({ 
  icon, 
  label, 
  onPress, 
  accessibilityLabel 
}: ExploreTileProps) {
  return (
    <Pressable
      onPress={onPress}
      style={({ pressed }) => [
        styles.tile,
        pressed && styles.tilePressed,
      ]}
      hitSlop={hitSlopTokens.md}
      accessible={true}
      accessibilityRole="button"
      accessibilityLabel={accessibilityLabel}
      accessibilityHint="Toucher deux fois pour ouvrir"
    >
      <Ionicons name={icon} size={24} color={color.brand} style={styles.icon} />
      <Text style={styles.tileLabel}>{label}</Text>
    </Pressable>
  );
});

interface ExploreGridProps {
  onTap: (feature: string) => void;
  showCycles?: boolean; // Si false, masque la tuile "Mes cycles"
}

export default React.memo(function ExploreGrid({ onTap, showCycles = true }: ExploreGridProps) {
  const tiles: Array<{
    id: string;
    icon: keyof typeof Ionicons.glyphMap;
    label: string;
    accessibilityLabel: string;
    conditional?: boolean;
  }> = [
    {
      id: 'theme',
      icon: 'planet' as const,
      label: 'Thème natal',
      accessibilityLabel: 'Thème natal - Calculer ou voir mon thème astrologique complet',
    },
    {
      id: 'my_cycles',
      icon: 'stats-chart' as const,
      label: 'Mes cycles',
      accessibilityLabel: 'Mes cycles - Voir l\'historique et les statistiques de vos cycles',
      conditional: true, // Tuile conditionnelle
    },
    {
      id: 'calendar',
      icon: 'calendar' as const,
      label: 'Calendrier',
      accessibilityLabel: 'Calendrier du cycle - Vue mensuelle avec prédictions de fertilité',
    },
    {
      id: 'compat',
      icon: 'heart' as const,
      label: 'Compatibilité',
      accessibilityLabel: 'Compatibilité astrologique - Analyser une relation',
    },
    {
      id: 'horoscope',
      icon: 'sparkles' as const,
      label: 'Horoscope IA',
      accessibilityLabel: 'Horoscope du jour personnalisé par intelligence artificielle',
    },
    {
      id: 'parent_enfant',
      icon: 'people' as const,
      label: 'Parent-Enfant',
      accessibilityLabel: 'Compatibilité parent-enfant avec analyse astrologique',
    },
  ].filter((tile) => {
    // Filtrer la tuile "Mes cycles" si showCycles est false
    if (tile.conditional && !showCycles) {
      return false;
    }
    return true;
  });

  return (
    <View style={styles.container}>
      <Text 
        style={styles.header}
        accessibilityRole="header"
      >
        EXPLORER
      </Text>
      
      <View style={styles.grid}>
        {tiles.map((tile) => (
          <View key={tile.id} style={styles.tileWrapper}>
            <Tile
              icon={tile.icon}
              label={tile.label}
              onPress={() => onTap(tile.id)}
              accessibilityLabel={tile.accessibilityLabel}
            />
          </View>
        ))}
      </View>
    </View>
  );
});

const styles = StyleSheet.create({
  container: {
    marginTop: space.lg,
  },
  header: {
    ...typography.label,
    color: color.brand,
    letterSpacing: 1.2,
    marginBottom: space.sm,
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginHorizontal: -space.xs,
  },
  tileWrapper: {
    width: '50%',
    padding: space.xs, // Augmenté de xs/2 à xs pour aérer
  },
  tile: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: color.border,
    paddingVertical: space.md, // Réduit de lg à md pour affiner
    paddingHorizontal: space.sm, // Réduit de md à sm
    minHeight: 88,
    justifyContent: 'center',
    alignItems: 'center',
  },
  tilePressed: {
    opacity: 0.7,
    transform: [{ scale: 0.97 }],
  },
  icon: {
    marginBottom: space.xs,
  },
  tileLabel: {
    ...typography.bodySm,
    fontWeight: '700',
    color: color.text,
    textAlign: 'center',
  },
});

