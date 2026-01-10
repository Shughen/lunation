/**
 * Écran de configuration des données de naissance
 * Pour générer le thème natal
 */

import { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  Alert,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { router } from 'expo-router';

import { color, space, type as typography, radius } from '@/theme/tokens';
import { searchCity } from '@/lib/services/geocodingService';
import { useProfileStore } from '@/stores/profileStore';

export default function NatalReadingSetupScreen() {
  const { saveProfile } = useProfileStore();
  const [formData, setFormData] = useState({
    year: '',
    month: '',
    day: '',
    hour: '',
    minute: '',
    city: '',
    country_code: 'FR',
    latitude: '',
    longitude: '',
    timezone: 'Europe/Paris', // Fuseau par défaut (sera écrasé par la recherche)
  });

  const [loading, setLoading] = useState(false);
  const [searching, setSearching] = useState(false);
  const [locationFound, setLocationFound] = useState(null);

  const updateField = (field, value) => {
    setFormData({ ...formData, [field]: value });
    
    // Reset location si on modifie la ville
    if (field === 'city') {
      setLocationFound(null);
    }
  };

  const handleSearchCity = async () => {
    if (!formData.city || formData.city.length < 2) {
      Alert.alert('Erreur', 'Entre au moins 2 caractères pour la ville');
      return;
    }

    try {
      setSearching(true);

      // Ne pas passer country_code si la ville contient déjà une virgule (ex: "Manaus, Brésil")
      const hasCountryInCity = formData.city.includes(',');
      const result = await searchCity(formData.city, hasCountryInCity ? '' : formData.country_code);

      // Auto-remplir les coordonnées, timezone et country_code
      setFormData({
        ...formData,
        latitude: result.latitude.toString(),
        longitude: result.longitude.toString(),
        timezone: result.timezone,
        country_code: result.country_code || formData.country_code,
      });

      setLocationFound(result.display_name);

      Alert.alert(
        '✅ Ville trouvée !',
        `${result.display_name}\n\n` +
        `Latitude: ${result.latitude.toFixed(4)}\n` +
        `Longitude: ${result.longitude.toFixed(4)}\n` +
        `Fuseau horaire: ${result.timezone}`
      );

    } catch (error) {
      Alert.alert(
        '❌ Ville non trouvée',
        `Impossible de trouver "${formData.city}". Vérifie l'orthographe ou essaie avec le pays (ex: "Paris, France").`
      );
    } finally {
      setSearching(false);
    }
  };

  const validateForm = () => {
    const required = ['year', 'month', 'day', 'hour', 'minute', 'city', 'latitude', 'longitude'];
    
    for (const field of required) {
      if (!formData[field]) {
        Alert.alert('Champs manquants', `Le champ "${field}" est requis`);
        return false;
      }
    }

    // Validation des valeurs
    const year = parseInt(formData.year);
    const month = parseInt(formData.month);
    const day = parseInt(formData.day);
    const hour = parseInt(formData.hour);
    const minute = parseInt(formData.minute);
    const lat = parseFloat(formData.latitude);
    const lon = parseFloat(formData.longitude);

    if (year < 1900 || year > 2100) {
      Alert.alert('Erreur', 'Année invalide (1900-2100)');
      return false;
    }
    if (month < 1 || month > 12) {
      Alert.alert('Erreur', 'Mois invalide (1-12)');
      return false;
    }
    if (day < 1 || day > 31) {
      Alert.alert('Erreur', 'Jour invalide (1-31)');
      return false;
    }
    if (hour < 0 || hour > 23) {
      Alert.alert('Erreur', 'Heure invalide (0-23)');
      return false;
    }
    if (minute < 0 || minute > 59) {
      Alert.alert('Erreur', 'Minute invalide (0-59)');
      return false;
    }
    if (lat < -90 || lat > 90) {
      Alert.alert('Erreur', 'Latitude invalide (-90 à 90)');
      return false;
    }
    if (lon < -180 || lon > 180) {
      Alert.alert('Erreur', 'Longitude invalide (-180 à 180)');
      return false;
    }

    return true;
  };

  // Auto-détecte le timezone basé sur les coordonnées (mapping simple)
  const guessTimezone = (lat, lon) => {
    // Mapping simplifié par longitude (pas parfait mais suffisant)
    if (lon >= -10 && lon <= 40) return 'Europe/Paris';  // Europe
    if (lon >= -75 && lon <= -34) return 'America/Sao_Paulo';  // Amérique du Sud
    if (lon >= -130 && lon <= -60) return 'America/New_York';  // Amérique du Nord
    if (lon >= 100 && lon <= 180) return 'Asia/Tokyo';  // Asie Est
    return 'UTC';  // Par défaut
  };

  const handleSubmit = async () => {
    if (!validateForm()) return;

    try {
      setLoading(true);

      const lat = parseFloat(formData.latitude);
      const lon = parseFloat(formData.longitude);
      
      // Priorité au timezone du géocodage, sinon devine depuis les coordonnées
      const timezone = formData.timezone || guessTimezone(lat, lon);

      const birthData = {
        year: parseInt(formData.year),
        month: parseInt(formData.month),
        day: parseInt(formData.day),
        hour: parseInt(formData.hour),
        minute: parseInt(formData.minute),
        second: 0,
        city: formData.city,
        country_code: formData.country_code,
        latitude: lat,
        longitude: lon,
        timezone: timezone,  // Du géocodage si disponible, sinon auto-détecté
      };

      console.log('[Setup] 📊 Timezone utilisé:', {
        formData_tz: formData.timezone,
        guessed_tz: guessTimezone(lat, lon),
        final_tz: timezone
      });

      // Convertir birthData au format attendu par le profil
      // Créer des objets Date pour birthDate et birthTime
      const birthDate = new Date(birthData.year, birthData.month - 1, birthData.day);
      const birthTime = new Date(2000, 0, 1, birthData.hour, birthData.minute, 0);

      // Sauvegarder le profil dans Supabase
      console.log('[Setup] 💾 Sauvegarde du profil dans Supabase...');
      const profileData = {
        birthDate: birthDate,
        birthTime: birthTime,
        birthPlace: formData.city,
        latitude: lat,
        longitude: lon,
        timezone: timezone,
      };

      const profileSaved = await saveProfile(profileData);
      
      if (!profileSaved) {
        console.error('[Setup] ❌ Erreur lors de la sauvegarde du profil');
        Alert.alert('Erreur', 'Impossible de sauvegarder le profil');
        return;
      }

      console.log('[Setup] ✅ Profil sauvegardé avec succès dans Supabase');

      // Passer les données en override pour la lecture natale immédiate
      const encoded = encodeURIComponent(JSON.stringify(birthData));
      router.replace(`/natal-reading?override=${encoded}`);

    } catch (error) {
      console.error('[Setup] Erreur:', error);
      Alert.alert('Erreur', 'Impossible de sauvegarder les données');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        keyboardShouldPersistTaps="handled"
      >
        <View style={styles.header}>
          <Text style={styles.title}>🌟 Configuration</Text>
          <Text style={styles.subtitle}>
            Entrez vos données de naissance pour générer votre thème natal
          </Text>
        </View>

        {/* Date de naissance */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>📅 Date de naissance</Text>
          
          <View style={styles.row}>
            <View style={styles.inputGroup}>
              <Text style={styles.label}>Jour</Text>
              <TextInput
                style={styles.input}
                value={formData.day}
                onChangeText={(val) => updateField('day', val)}
                placeholder="1"
                keyboardType="number-pad"
                maxLength={2}
              />
            </View>

            <View style={styles.inputGroup}>
              <Text style={styles.label}>Mois</Text>
              <TextInput
                style={styles.input}
                value={formData.month}
                onChangeText={(val) => updateField('month', val)}
                placeholder="11"
                keyboardType="number-pad"
                maxLength={2}
              />
            </View>

            <View style={styles.inputGroup}>
              <Text style={styles.label}>Année</Text>
              <TextInput
                style={styles.input}
                value={formData.year}
                onChangeText={(val) => updateField('year', val)}
                placeholder="1989"
                keyboardType="number-pad"
                maxLength={4}
              />
            </View>
          </View>
        </View>

        {/* Heure de naissance */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>🕐 Heure de naissance</Text>
          
          <View style={styles.row}>
            <View style={styles.inputGroup}>
              <Text style={styles.label}>Heure (0-23)</Text>
              <TextInput
                style={styles.input}
                value={formData.hour}
                onChangeText={(val) => updateField('hour', val)}
                placeholder="13"
                keyboardType="number-pad"
                maxLength={2}
              />
            </View>

            <View style={styles.inputGroup}>
              <Text style={styles.label}>Minute (0-59)</Text>
              <TextInput
                style={styles.input}
                value={formData.minute}
                onChangeText={(val) => updateField('minute', val)}
                placeholder="20"
                keyboardType="number-pad"
                maxLength={2}
              />
            </View>
          </View>
        </View>

        {/* Lieu de naissance */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>📍 Lieu de naissance</Text>
          
          <View style={styles.inputGroup}>
            <Text style={styles.label}>Ville de naissance</Text>
            <View style={styles.cityInputRow}>
              <TextInput
                style={[styles.input, styles.cityInput]}
                value={formData.city}
                onChangeText={(val) => updateField('city', val)}
                placeholder="Manaus"
                placeholderTextColor={color.textDisabled}
                autoCapitalize="words"
              />
              <TouchableOpacity
                style={[styles.searchButton, searching && styles.searchButtonDisabled]}
                onPress={handleSearchCity}
                disabled={searching}
              >
                <Text style={styles.searchButtonText}>
                  {searching ? '⏳' : '🔍 Rechercher'}
                </Text>
              </TouchableOpacity>
            </View>
            
            {/* Affichage si ville trouvée */}
            {locationFound && (
              <View style={styles.locationFoundCard}>
                <Text style={styles.locationFoundText}>✅ {locationFound}</Text>
                <Text style={styles.locationCoords}>
                  {parseFloat(formData.latitude).toFixed(4)}, {parseFloat(formData.longitude).toFixed(4)}
                </Text>
              </View>
            )}
          </View>

        </View>

        {/* Note: Coordonnées et fuseau horaire auto-détectés */}

        {/* Bouton de validation */}
        <TouchableOpacity
          style={[styles.submitButton, loading && styles.submitButtonDisabled]}
          onPress={handleSubmit}
          disabled={loading}
        >
          <Text style={styles.submitButtonText}>
            {loading ? 'Sauvegarde...' : '✨ Générer mon thème natal'}
          </Text>
        </TouchableOpacity>

        {/* Helper */}
        <View style={styles.helperCard}>
          <Text style={styles.helperTitle}>💡 Astuce</Text>
          <Text style={styles.helperText}>
            Entre ta ville et tape "🔍 Rechercher" :{'\n'}
            • Villes connues : juste "Manaus" ou "Paris"{'\n'}
            • Autres villes : ajoute le pays "Angers, France"{'\n'}
            {'\n'}
            Villes populaires disponibles : Paris, Lyon, Marseille, Toulouse, Bordeaux, Nice, Manaus, São Paulo, Rio, New York, Londres, Tokyo...
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: color.bg,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    padding: space.md,
    paddingBottom: space.xl * 2,
  },
  header: {
    marginBottom: space.lg,
  },
  title: {
    ...typography.h1,
    marginBottom: space.xs,
  },
  subtitle: {
    ...typography.bodySm,
    color: color.textMuted,
    lineHeight: 20,
  },
  section: {
    marginBottom: space.lg,
  },
  sectionTitle: {
    ...typography.h3,
    marginBottom: space.md,
  },
  row: {
    flexDirection: 'row',
    gap: space.sm,
  },
  inputGroup: {
    flex: 1,
    marginBottom: space.md,
  },
  label: {
    ...typography.bodySm,
    fontWeight: '500',
    color: color.textMuted,
    marginBottom: space.xs,
  },
  input: {
    backgroundColor: color.surfaceElevated,
    borderWidth: 1,
    borderColor: color.border,
    borderRadius: radius.md,
    paddingHorizontal: space.md,
    paddingVertical: space.sm,
    ...typography.body,
  },
  cityInputRow: {
    flexDirection: 'row',
    gap: space.sm,
    alignItems: 'flex-end',
  },
  cityInput: {
    flex: 1,
  },
  searchButton: {
    backgroundColor: color.brand,
    paddingHorizontal: space.md,
    paddingVertical: space.sm + 2,
    borderRadius: radius.md,
    justifyContent: 'center',
  },
  searchButtonDisabled: {
    opacity: 0.5,
  },
  searchButtonText: {
    ...typography.bodySm,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  locationFoundCard: {
    marginTop: space.sm,
    backgroundColor: color.successSoft,
    borderWidth: 1,
    borderColor: color.success,
    borderRadius: radius.md,
    padding: space.sm,
  },
  locationFoundText: {
    ...typography.bodySm,
    color: color.text,
    marginBottom: 2,
  },
  locationCoords: {
    ...typography.caption,
    color: color.textMuted,
  },
  submitButton: {
    backgroundColor: color.brand,
    paddingVertical: space.md,
    borderRadius: radius.lg,
    alignItems: 'center',
    marginTop: space.md,
  },
  submitButtonDisabled: {
    opacity: 0.5,
  },
  submitButtonText: {
    ...typography.bodyMd,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  helperCard: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.lg,
    padding: space.md,
    marginTop: space.lg,
    borderWidth: 1,
    borderColor: color.border,
  },
  helperTitle: {
    ...typography.bodySm,
    fontWeight: '600',
    color: color.text,
    marginBottom: space.xs,
  },
  helperText: {
    ...typography.caption,
    color: color.textMuted,
    lineHeight: 18,
  },
});

