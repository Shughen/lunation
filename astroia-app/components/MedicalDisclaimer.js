/**
 * Bandeau de disclaimer médical
 * À afficher sur tous les écrans avec données de santé/cycle
 */

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { fonts, spacing, borderRadius } from '@/constants/theme';

export function MedicalDisclaimer({ compact = false }) {
  if (compact) {
    return (
      <View style={styles.bannerCompact}>
        <Ionicons name="information-circle-outline" size={14} color="#F59E0B" />
        <Text style={styles.textCompact}>
          Contenu bien-être, non diagnostic médical
        </Text>
      </View>
    );
  }

  return (
    <View style={styles.banner}>
      <Ionicons name="medical-outline" size={20} color="#F59E0B" />
      <View style={styles.content}>
        <Text style={styles.title}>⚕️ Information importante</Text>
        <Text style={styles.text}>
          LUNA est un outil de bien-être, pas un dispositif médical. Les recommandations sont générales et ne remplacent pas un avis médical professionnel. En cas de doute sur ta santé, consulte un·e professionnel·le.
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  banner: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: spacing.md,
    backgroundColor: 'rgba(245, 158, 11, 0.12)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
    borderLeftWidth: 3,
    borderLeftColor: '#F59E0B',
  },
  content: {
    flex: 1,
  },
  title: {
    fontSize: fonts.sizes.sm,
    fontWeight: 'bold',
    color: '#F59E0B',
    marginBottom: spacing.xs,
  },
  text: {
    fontSize: fonts.sizes.xs,
    color: 'rgba(255, 255, 255, 0.85)',
    lineHeight: 18,
  },
  bannerCompact: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.xs,
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    borderRadius: borderRadius.sm,
    paddingVertical: spacing.xs,
    paddingHorizontal: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.25)',
  },
  textCompact: {
    fontSize: 10, // Réduit de 11 à 10
    color: 'rgba(255, 255, 255, 0.6)', // Opacité réduite de 0.8 à 0.6
    fontStyle: 'italic',
  },
});

