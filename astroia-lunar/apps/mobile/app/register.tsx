/**
 * Écran d'inscription par email
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  Alert,
  ActivityIndicator,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { useAuthStore } from '../stores/useAuthStore';
import { auth } from '../services/api';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

// Validation regex pour email
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export default function RegisterScreen() {
  const router = useRouter();
  const { setUser } = useAuthStore();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState<{
    email?: string;
    password?: string;
    confirmPassword?: string;
  }>({});

  const validate = (): boolean => {
    const newErrors: typeof errors = {};

    // Validation email
    if (!email) {
      newErrors.email = 'Email requis';
    } else if (!EMAIL_REGEX.test(email)) {
      newErrors.email = 'Format email invalide';
    }

    // Validation mot de passe
    if (!password) {
      newErrors.password = 'Mot de passe requis';
    } else if (password.length < 8) {
      newErrors.password = 'Minimum 8 caractères';
    }

    // Validation confirmation
    if (!confirmPassword) {
      newErrors.confirmPassword = 'Confirmation requise';
    } else if (password !== confirmPassword) {
      newErrors.confirmPassword = 'Les mots de passe ne correspondent pas';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleRegister = async () => {
    if (!validate()) {
      return;
    }

    setLoading(true);
    try {
      // 1. Inscription (token auto-stocké par auth.register)
      const { access_token } = await auth.register(email, password);

      // 2. Récupération des infos utilisateur avec le token explicite
      // (bypasse DEV_AUTH_BYPASS qui utiliserait un autre user)
      const user = await auth.getMeWithToken(access_token);
      setUser(user);

      // 3. Redirection vers la collecte des données de naissance
      router.replace('/onboarding/profile-setup');
    } catch (error: any) {
      const message = error.response?.data?.detail || 'Inscription échouée';

      // Gestion erreur email déjà utilisé
      if (error.response?.status === 400 && message.toLowerCase().includes('email')) {
        setErrors({ email: 'Cet email est déjà utilisé' });
      } else {
        Alert.alert('Erreur', message);
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
        style={styles.keyboardView}
      >
        <ScrollView
          contentContainerStyle={styles.scrollContent}
          keyboardShouldPersistTaps="handled"
        >
          <View style={styles.content}>
            <Text style={styles.title}>Créer un compte</Text>
            <Text style={styles.subtitle}>
              Rejoignez Lunation pour explorer vos cycles lunaires
            </Text>

            <View style={styles.form}>
              {/* Email */}
              <View style={styles.inputContainer}>
                <TextInput
                  style={[styles.input, errors.email && styles.inputError]}
                  placeholder="Email"
                  placeholderTextColor={colors.textMuted}
                  value={email}
                  onChangeText={(text) => {
                    setEmail(text);
                    if (errors.email) setErrors({ ...errors, email: undefined });
                  }}
                  keyboardType="email-address"
                  autoCapitalize="none"
                  autoComplete="email"
                />
                {errors.email && (
                  <Text style={styles.errorText}>{errors.email}</Text>
                )}
              </View>

              {/* Mot de passe */}
              <View style={styles.inputContainer}>
                <TextInput
                  style={[styles.input, errors.password && styles.inputError]}
                  placeholder="Mot de passe (min. 8 caractères)"
                  placeholderTextColor={colors.textMuted}
                  value={password}
                  onChangeText={(text) => {
                    setPassword(text);
                    if (errors.password) setErrors({ ...errors, password: undefined });
                  }}
                  secureTextEntry
                  autoComplete="new-password"
                />
                {errors.password && (
                  <Text style={styles.errorText}>{errors.password}</Text>
                )}
              </View>

              {/* Confirmation mot de passe */}
              <View style={styles.inputContainer}>
                <TextInput
                  style={[styles.input, errors.confirmPassword && styles.inputError]}
                  placeholder="Confirmer le mot de passe"
                  placeholderTextColor={colors.textMuted}
                  value={confirmPassword}
                  onChangeText={(text) => {
                    setConfirmPassword(text);
                    if (errors.confirmPassword) setErrors({ ...errors, confirmPassword: undefined });
                  }}
                  secureTextEntry
                  autoComplete="new-password"
                />
                {errors.confirmPassword && (
                  <Text style={styles.errorText}>{errors.confirmPassword}</Text>
                )}
              </View>

              {/* Bouton inscription */}
              <TouchableOpacity
                style={[styles.button, loading && styles.buttonDisabled]}
                onPress={handleRegister}
                disabled={loading}
              >
                {loading ? (
                  <ActivityIndicator color="#fff" />
                ) : (
                  <Text style={styles.buttonText}>Créer mon compte</Text>
                )}
              </TouchableOpacity>

              {/* Lien vers connexion */}
              <TouchableOpacity
                style={styles.linkButton}
                onPress={() => router.push('/login')}
              >
                <Text style={styles.linkText}>
                  Déjà un compte ? Se connecter
                </Text>
              </TouchableOpacity>
            </View>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  keyboardView: {
    flex: 1,
  },
  scrollContent: {
    flexGrow: 1,
    justifyContent: 'center',
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    paddingHorizontal: spacing.xl,
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: spacing.xl,
  },
  form: {
    width: '100%',
  },
  inputContainer: {
    marginBottom: spacing.md,
  },
  input: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    ...fonts.body,
    color: colors.text,
    borderWidth: 1,
    borderColor: 'transparent',
  },
  inputError: {
    borderColor: '#ff6b6b',
  },
  errorText: {
    ...fonts.caption,
    color: '#ff6b6b',
    marginTop: spacing.xs,
    marginLeft: spacing.xs,
  },
  button: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginTop: spacing.lg,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonText: {
    ...fonts.button,
    color: colors.text,
  },
  linkButton: {
    marginTop: spacing.md,
    alignItems: 'center',
  },
  linkText: {
    ...fonts.body,
    color: colors.accent,
    textDecorationLine: 'underline',
  },
});
