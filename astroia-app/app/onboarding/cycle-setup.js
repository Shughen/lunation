import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Alert,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import DateTimePicker from '@react-native-community/datetimepicker';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';

const CYCLE_LENGTHS = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35];

export default function CycleSetupScreen() {
  const [lastPeriodDate, setLastPeriodDate] = useState(new Date());
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [cycleLength, setCycleLength] = useState(28);

  const handleNext = async () => {
    try {
      // Sauvegarder les infos du cycle
      const cycleConfig = {
        lastPeriodDate: lastPeriodDate.toISOString().split('T')[0],
        cycleLength,
        setupDate: new Date().toISOString(),
      };
      
      await AsyncStorage.setItem('cycle_config', JSON.stringify(cycleConfig));
      
      // Passer au tour guidé
      router.push('/onboarding/tour');
    } catch (error) {
      console.error('[CycleSetup] Save error:', error);
      Alert.alert('Erreur', 'Impossible de sauvegarder. Veuillez réessayer.');
    }
  };

  const handleBack = () => {
    router.back();
  };

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        <KeyboardAvoidingView
          behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
          style={styles.keyboardView}
        >
          {/* Header */}
          <View style={styles.header}>
            <TouchableOpacity onPress={handleBack} style={styles.backButton}>
              <Ionicons name="arrow-back" size={24} color="#fff" />
            </TouchableOpacity>
            <Text style={styles.headerTitle}>Étape 3/4</Text>
            <View style={{ width: 40 }} />
          </View>

          <ScrollView
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
            keyboardShouldPersistTaps="handled"
          >
            {/* Title */}
            <Text style={styles.title}>Configurons ton cycle</Text>
            <Text style={styles.subtitle}>
              Pour des recommandations personnalisées, nous avons besoin de connaître ton cycle menstruel
            </Text>

            {/* Form */}
            <View style={styles.form}>
              {/* Date dernières règles */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>📅 Date de tes dernières règles</Text>
                <TouchableOpacity
                  style={styles.dateButton}
                  onPress={() => setShowDatePicker(true)}
                >
                  <Text style={styles.dateButtonText}>
                    {lastPeriodDate.toLocaleDateString('fr-FR', {
                      day: 'numeric',
                      month: 'long',
                      year: 'numeric',
                    })}
                  </Text>
                  <Ionicons name="calendar-outline" size={20} color="#FFB6C1" />
                </TouchableOpacity>
              </View>

              {showDatePicker && (
                <DateTimePicker
                  value={lastPeriodDate}
                  mode="date"
                  display="spinner"
                  onChange={(event, selectedDate) => {
                    setShowDatePicker(Platform.OS === 'ios');
                    if (selectedDate) {
                      setLastPeriodDate(selectedDate);
                    }
                  }}
                  maximumDate={new Date()}
                  minimumDate={new Date(Date.now() - 90 * 24 * 60 * 60 * 1000)} // 90 jours max
                />
              )}

              {/* Durée du cycle */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>🌙 Durée moyenne de ton cycle</Text>
                <Text style={styles.hint}>Sélectionne la durée (en jours)</Text>
                
                <ScrollView
                  horizontal
                  showsHorizontalScrollIndicator={false}
                  style={styles.cycleLengthScroll}
                  contentContainerStyle={styles.cycleLengthContent}
                >
                  {CYCLE_LENGTHS.map((length) => (
                    <TouchableOpacity
                      key={length}
                      style={[
                        styles.cycleLengthButton,
                        cycleLength === length && styles.cycleLengthButtonActive,
                      ]}
                      onPress={() => setCycleLength(length)}
                    >
                      <Text
                        style={[
                          styles.cycleLengthText,
                          cycleLength === length && styles.cycleLengthTextActive,
                        ]}
                      >
                        {length}
                      </Text>
                    </TouchableOpacity>
                  ))}
                </ScrollView>
              </View>

              {/* Info box */}
              <View style={styles.infoBox}>
                <Ionicons name="heart-circle" size={24} color="#FFB6C1" />
                <Text style={styles.infoText}>
                  Ces informations restent 100% privées et nous permettent de calculer ta phase actuelle et tes prédictions d'énergie
                </Text>
              </View>
            </View>
          </ScrollView>

          {/* Footer */}
          <View style={styles.footer}>
            <TouchableOpacity
              style={styles.nextButton}
              onPress={handleNext}
              activeOpacity={0.8}
            >
              <LinearGradient
                colors={['#FFB6C1', '#FFC8DD']}
                style={styles.nextButtonGradient}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 0 }}
              >
                <Text style={styles.nextButtonText}>Suivant</Text>
                <Ionicons name="arrow-forward" size={20} color="#fff" />
              </LinearGradient>
            </TouchableOpacity>
          </View>
        </KeyboardAvoidingView>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  keyboardView: {
    flex: 1,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  backButton: {
    width: 40,
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerTitle: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.xl,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: spacing.sm,
    textShadowColor: 'rgba(255, 182, 193, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  subtitle: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.7)',
    marginBottom: spacing.xxl,
    lineHeight: 22,
  },
  form: {
    gap: spacing.xl,
  },
  inputGroup: {
    gap: spacing.sm,
  },
  label: {
    fontSize: fonts.sizes.md,
    color: '#FFC8DD',
    fontWeight: '600',
  },
  hint: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.5)',
    marginBottom: spacing.xs,
  },
  dateButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    borderWidth: 2,
    borderColor: 'rgba(255, 182, 193, 0.3)',
  },
  dateButtonText: {
    fontSize: fonts.sizes.lg,
    color: '#fff',
    fontWeight: '500',
  },
  cycleLengthScroll: {
    marginHorizontal: -spacing.xs,
  },
  cycleLengthContent: {
    paddingHorizontal: spacing.xs,
    gap: spacing.sm,
  },
  cycleLengthButton: {
    width: 50,
    height: 50,
    borderRadius: 25,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2,
    borderColor: 'rgba(255, 255, 255, 0.2)',
  },
  cycleLengthButtonActive: {
    backgroundColor: 'rgba(255, 182, 193, 0.25)',
    borderColor: '#FFB6C1',
    borderWidth: 3,
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.5,
    shadowRadius: 6,
    elevation: 4,
  },
  cycleLengthText: {
    fontSize: fonts.sizes.lg,
    color: 'rgba(255, 255, 255, 0.7)',
    fontWeight: '600',
  },
  cycleLengthTextActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  infoBox: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: spacing.md,
    backgroundColor: 'rgba(255, 182, 193, 0.12)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(255, 182, 193, 0.3)',
  },
  infoText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.85)',
    lineHeight: 20,
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
  },
  nextButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: '#FFB6C1',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  nextButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    gap: spacing.sm,
  },
  nextButtonText: {
    color: '#fff',
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});

