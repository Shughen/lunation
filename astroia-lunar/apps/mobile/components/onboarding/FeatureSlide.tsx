/**
 * FeatureSlide Component
 * Slide individuel pour l'onboarding avec preview interactive
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  Dimensions,
} from 'react-native';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

const { width: SCREEN_WIDTH } = Dimensions.get('window');

export interface FeatureSlideData {
  id: string;
  icon: string;
  title: string;
  description: string;
  preview?: React.ReactNode;
}

interface FeatureSlideProps {
  slide: FeatureSlideData;
}

export function FeatureSlide({ slide }: FeatureSlideProps) {
  return (
    <View style={styles.container}>
      {/* Icon */}
      <View style={styles.iconContainer}>
        <Text style={styles.icon}>{slide.icon}</Text>
      </View>

      {/* Title */}
      <Text style={styles.title}>{slide.title}</Text>

      {/* Description */}
      <Text style={styles.description}>{slide.description}</Text>

      {/* Preview (if provided) */}
      {slide.preview && (
        <View style={styles.previewContainer}>
          {slide.preview}
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: SCREEN_WIDTH - spacing.xl * 2,
    alignItems: 'center',
    paddingVertical: spacing.xl,
  },
  iconContainer: {
    width: 100,
    height: 100,
    borderRadius: 50,
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: spacing.xl,
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.3,
    shadowRadius: 16,
    elevation: 8,
  },
  icon: {
    fontSize: 48,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.md,
    textShadowColor: 'rgba(183, 148, 246, 0.4)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  description: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.8)',
    textAlign: 'center',
    lineHeight: 24,
    marginBottom: spacing.lg,
    paddingHorizontal: spacing.md,
  },
  previewContainer: {
    width: '100%',
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.15)',
  },
});

export default FeatureSlide;
