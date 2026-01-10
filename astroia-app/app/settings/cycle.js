import React, { useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';
import haptics from '@/utils/haptics';

/**
 * Écran settings/cycle - DÉPRÉCIÉ
 * Redirige vers le nouveau système (Suivi rapide + Mes cycles)
 */
export default function CycleSettingsScreen() {
  useEffect(() => {
    // Auto-redirect vers Home au montage
    const timer = setTimeout(() => {
      router.replace('/(tabs)/home');
    }, 100);
    
    return () => clearTimeout(timer);
  }, []);

  return (
    <View style={styles.wrapper}>
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top']}>
          {/* Header */}
          <View style={styles.header}>
            <TouchableOpacity
              onPress={() => {
                haptics.light();
                router.back();
              }}
              style={styles.backButton}
            >
              <Ionicons name="arrow-back" size={24} color="#fff" />
              <Text style={styles.backText}>Retour</Text>
            </TouchableOpacity>
          </View>

          {/* Info redirection */}
          <View style={styles.redirectCard}>
            <Ionicons name="information-circle" size={48} color={colors.accent} />
            <Text style={styles.redirectTitle}>Nouvelle interface de suivi</Text>
            <Text style={styles.redirectText}>
              La configuration du cycle a été déplacée.{'\n\n'}
              Utilise maintenant "Suivi rapide" sur l'écran d'accueil.
            </Text>
            <TouchableOpacity
              style={styles.redirectButton}
              onPress={() => {
                haptics.medium();
                router.push('/(tabs)/home');
              }}
            >
              <Text style={styles.redirectButtonText}>Aller à l'accueil →</Text>
            </TouchableOpacity>
          </View>
        </SafeAreaView>
      </LinearGradient>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
  },
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
  },
  backText: {
    ...fonts.body,
    color: '#fff',
  },
  redirectCard: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: spacing.xl,
  },
  redirectTitle: {
    ...fonts.h2,
    color: '#fff',
    marginTop: spacing.lg,
    marginBottom: spacing.sm,
    textAlign: 'center',
  },
  redirectText: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    lineHeight: 24,
    marginBottom: spacing.xl,
  },
  redirectButton: {
    backgroundColor: colors.accent,
    paddingHorizontal: spacing.xl,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
  },
  redirectButtonText: {
    ...fonts.button,
    color: '#fff',
  },
});
