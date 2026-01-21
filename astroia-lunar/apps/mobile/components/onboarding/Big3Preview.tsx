/**
 * Big3Preview Component
 * Affiche le Big 3 (Soleil, Lune, Ascendant) avec animations
 *
 * Utilise pour:
 * - Profile-setup: preview en temps reel pendant la saisie
 * - Chart-preview: reveal anime apres calcul complet
 */

import React, { useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Animated,
  Easing,
} from 'react-native';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { translateZodiacSign } from '../../utils/astrologyTranslations';
import { ZodiacBadge } from '../icons';

interface Big3Item {
  label: string;
  sign: string | null | undefined;
  icon: string;
  description: string;
  isLoading?: boolean;
  placeholder?: string;
}

interface Big3PreviewProps {
  sunSign: string | null | undefined;
  moonSign: string | null | undefined;
  ascendant: string | null | undefined;
  isLoading?: boolean;
  animated?: boolean;
  compact?: boolean;
  name?: string;
  // Placeholders personnalisés
  sunPlaceholder?: string;
  moonPlaceholder?: string;
  ascendantPlaceholder?: string;
}

interface Big3ItemComponentProps {
  item: Big3Item;
  index: number;
  animated: boolean;
  compact: boolean;
}

function Big3ItemComponent({ item, index, animated, compact }: Big3ItemComponentProps) {
  const opacityAnim = useRef(new Animated.Value(animated ? 0 : 1)).current;
  const translateAnim = useRef(new Animated.Value(animated ? 30 : 0)).current;
  const scaleAnim = useRef(new Animated.Value(animated ? 0.9 : 1)).current;

  useEffect(() => {
    if (animated && item.sign) {
      // Animation de reveal avec delai progressif
      Animated.sequence([
        Animated.delay(index * 300),
        Animated.parallel([
          Animated.timing(opacityAnim, {
            toValue: 1,
            duration: 500,
            useNativeDriver: true,
          }),
          Animated.timing(translateAnim, {
            toValue: 0,
            duration: 500,
            easing: Easing.out(Easing.cubic),
            useNativeDriver: true,
          }),
          Animated.spring(scaleAnim, {
            toValue: 1,
            friction: 6,
            tension: 40,
            useNativeDriver: true,
          }),
        ]),
      ]).start();
    }
  }, [animated, item.sign, index]);

  const translatedSign = item.sign ? translateZodiacSign(item.sign) : null;
  const isAvailable = !!item.sign;

  return (
    <Animated.View
      style={[
        compact ? styles.itemCompact : styles.item,
        animated && {
          opacity: opacityAnim,
          transform: [{ translateY: translateAnim }, { scale: scaleAnim }],
        },
      ]}
    >
      {/* Icon + Badge */}
      <View style={styles.itemHeader}>
        <Text style={styles.itemIcon}>{item.icon}</Text>
        {isAvailable && item.sign && (
          <ZodiacBadge sign={item.sign} size={compact ? 24 : 32} />
        )}
      </View>

      {/* Label */}
      <Text style={[styles.itemLabel, compact && styles.itemLabelCompact]}>
        {item.label}
      </Text>

      {/* Sign or placeholder */}
      {item.isLoading ? (
        <View style={styles.loadingContainer}>
          <Text style={styles.loadingText}>Calcul...</Text>
        </View>
      ) : isAvailable ? (
        <Text style={[styles.itemSign, compact && styles.itemSignCompact]}>
          {translatedSign}
        </Text>
      ) : (
        <Text style={[styles.placeholder, compact && styles.placeholderCompact]}>
          {item.placeholder || '...'}
        </Text>
      )}

      {/* Description (only in full mode) */}
      {!compact && isAvailable && (
        <Text style={styles.itemDescription}>{item.description}</Text>
      )}
    </Animated.View>
  );
}

export function Big3Preview({
  sunSign,
  moonSign,
  ascendant,
  isLoading = false,
  animated = false,
  compact = false,
  name,
  sunPlaceholder = 'Date requise',
  moonPlaceholder = 'Date requise',
  ascendantPlaceholder = 'Heure + lieu',
}: Big3PreviewProps) {
  const big3Items: Big3Item[] = [
    {
      label: 'Soleil',
      sign: sunSign,
      icon: '☀️',
      description: 'Ta nature profonde',
      isLoading: isLoading,
      placeholder: sunPlaceholder,
    },
    {
      label: 'Lune',
      sign: moonSign,
      icon: '🌙',
      description: 'Tes émotions',
      isLoading: isLoading,
      placeholder: moonPlaceholder,
    },
    {
      label: 'Ascendant',
      sign: ascendant,
      icon: '⬆️',
      description: 'Ton image',
      isLoading: isLoading,
      placeholder: ascendantPlaceholder,
    },
  ];

  return (
    <View style={[styles.container, compact && styles.containerCompact]}>
      {/* Title (only in full mode with name) */}
      {!compact && name && (
        <Text style={styles.title}>
          Voici ton ciel de naissance, {name}
        </Text>
      )}

      {/* Big 3 items */}
      <View style={[styles.grid, compact && styles.gridCompact]}>
        {big3Items.map((item, index) => (
          <Big3ItemComponent
            key={item.label}
            item={item}
            index={index}
            animated={animated}
            compact={compact}
          />
        ))}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: '100%',
  },
  containerCompact: {
    paddingVertical: spacing.sm,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.xl,
    textShadowColor: 'rgba(183, 148, 246, 0.4)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  grid: {
    gap: spacing.md,
  },
  gridCompact: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    gap: spacing.sm,
  },
  item: {
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
    alignItems: 'center',
  },
  itemCompact: {
    flex: 1,
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.sm,
    padding: spacing.sm,
    alignItems: 'center',
    minWidth: 90,
  },
  itemHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    marginBottom: spacing.xs,
  },
  itemIcon: {
    fontSize: 24,
  },
  itemLabel: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
    marginBottom: spacing.xs,
  },
  itemLabelCompact: {
    fontSize: 11,
    marginBottom: 2,
  },
  itemSign: {
    fontSize: 22,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.xs,
  },
  itemSignCompact: {
    fontSize: 14,
    marginBottom: 0,
  },
  itemDescription: {
    fontSize: fonts.sizes.sm,
    color: colors.accent,
    fontStyle: 'italic',
  },
  placeholder: {
    fontSize: 14,
    color: colors.textDark,
    fontStyle: 'italic',
  },
  placeholderCompact: {
    fontSize: 11,
  },
  loadingContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.xs,
  },
  loadingText: {
    fontSize: fonts.sizes.sm,
    color: colors.accent,
    fontStyle: 'italic',
  },
});

export default Big3Preview;
