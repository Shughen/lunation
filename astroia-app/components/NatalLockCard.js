import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import THEME from '@/constants/theme';

const ZODIAC_SIGNS = [
  { id: 1, name: 'Bélier', emoji: '♈' },
  { id: 2, name: 'Taureau', emoji: '♉' },
  { id: 3, name: 'Gémeaux', emoji: '♊' },
  { id: 4, name: 'Cancer', emoji: '♋' },
  { id: 5, name: 'Lion', emoji: '♌' },
  { id: 6, name: 'Vierge', emoji: '♍' },
  { id: 7, name: 'Balance', emoji: '♎' },
  { id: 8, name: 'Scorpion', emoji: '♏' },
  { id: 9, name: 'Sagittaire', emoji: '♐' },
  { id: 10, name: 'Capricorne', emoji: '♑' },
  { id: 11, name: 'Verseau', emoji: '♒' },
  { id: 12, name: 'Poissons', emoji: '♓' },
];

/**
 * Carte verrouillée affichant les données du thème natal (Soleil, Ascendant, Lune)
 * en lecture seule, avec CTA pour recalculer le thème natal.
 */
export default function NatalLockCard({ natal }) {
  const getZodiacById = (id) => {
    return ZODIAC_SIGNS.find((sign) => sign.id === id) || ZODIAC_SIGNS[0];
  };

  const sunSign = getZodiacById(natal.sun);
  const ascSign = getZodiacById(natal.asc);
  const moonSign = getZodiacById(natal.moon);

  return (
    <View style={styles.container}>
      {/* En-tête */}
      <View style={styles.header}>
        <Ionicons name="lock-closed" size={20} color={THEME.colors.primary} />
        <Text style={styles.headerText}>Tes données astrologiques</Text>
      </View>

      {/* Lignes des signes */}
      <View style={styles.signsContainer}>
        <View style={styles.signRow}>
          <Text style={styles.signIcon}>☉</Text>
          <Text style={styles.signLabel}>Soleil</Text>
          <View style={styles.signValue}>
            <Text style={styles.signEmoji}>{sunSign.emoji}</Text>
            <Text style={styles.signName}>{sunSign.name}</Text>
          </View>
        </View>

        <View style={styles.signRow}>
          <Text style={styles.signIcon}>↑</Text>
          <Text style={styles.signLabel}>Ascendant</Text>
          <View style={styles.signValue}>
            <Text style={styles.signEmoji}>{ascSign.emoji}</Text>
            <Text style={styles.signName}>{ascSign.name}</Text>
          </View>
        </View>

        <View style={styles.signRow}>
          <Text style={styles.signIcon}>☽</Text>
          <Text style={styles.signLabel}>Lune</Text>
          <View style={styles.signValue}>
            <Text style={styles.signEmoji}>{moonSign.emoji}</Text>
            <Text style={styles.signName}>{moonSign.name}</Text>
          </View>
        </View>
      </View>

      {/* Bandeau info */}
      <View style={styles.infoBanner}>
        <Ionicons name="information-circle-outline" size={16} color="#94A3B8" />
        <Text style={styles.infoText}>
          Données issues de ton thème natal
        </Text>
      </View>

      {/* CTA recalcul */}
      <TouchableOpacity
        style={styles.recalcButton}
        onPress={() => router.push('/natal-chart')}
        activeOpacity={0.7}
      >
        <LinearGradient
          colors={['#6366F1', '#8B5CF6']}
          start={{ x: 0, y: 0 }}
          end={{ x: 1, y: 0 }}
          style={styles.recalcGradient}
        >
          <Ionicons name="refresh-outline" size={18} color="white" />
          <Text style={styles.recalcText}>Recalculer mon thème natal</Text>
        </LinearGradient>
      </TouchableOpacity>

      {/* Tooltip */}
      <Text style={styles.tooltip}>
        Pour modifier ces éléments, recalcule ton thème dans l'onglet dédié
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  headerText: {
    fontSize: 16,
    fontWeight: '600',
    color: 'white',
    marginLeft: 8,
  },
  signsContainer: {
    marginBottom: 16,
  },
  signRow: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  signIcon: {
    fontSize: 24,
    width: 32,
    textAlign: 'center',
  },
  signLabel: {
    fontSize: 15,
    color: '#94A3B8',
    flex: 1,
    marginLeft: 8,
  },
  signValue: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  signEmoji: {
    fontSize: 20,
    marginRight: 8,
  },
  signName: {
    fontSize: 15,
    fontWeight: '600',
    color: 'white',
  },
  infoBanner: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#0F172A',
    borderRadius: 8,
    padding: 12,
    marginBottom: 16,
  },
  infoText: {
    fontSize: 13,
    color: '#94A3B8',
    marginLeft: 8,
  },
  recalcButton: {
    marginBottom: 12,
  },
  recalcGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 14,
    borderRadius: 12,
  },
  recalcText: {
    fontSize: 15,
    fontWeight: '600',
    color: 'white',
    marginLeft: 8,
  },
  tooltip: {
    fontSize: 12,
    color: '#64748B',
    textAlign: 'center',
    fontStyle: 'italic',
  },
});

