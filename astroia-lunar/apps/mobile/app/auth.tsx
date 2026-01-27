/**
 * Écran unifié d'authentification (Login/Signup + OAuth)
 */

import React, { useState, useEffect } from 'react';
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

// Imports OAuth conditionnels (nécessitent un dev build)
let Google: any = null;
let AppleAuthentication: any = null;
let WebBrowser: any = null;

try {
  Google = require('expo-auth-session/providers/google');
  WebBrowser = require('expo-web-browser');
  WebBrowser.maybeCompleteAuthSession();
} catch (e) {
  console.log('[Auth] expo-auth-session non disponible (Expo Go)');
}

try {
  AppleAuthentication = require('expo-apple-authentication');
} catch (e) {
  console.log('[Auth] expo-apple-authentication non disponible');
}

// Validation email
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

type AuthMode = 'login' | 'signup';

export default function AuthScreen() {
  const router = useRouter();
  const { setUser } = useAuthStore();

  const [mode, setMode] = useState<AuthMode>('login');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState<{
    email?: string;
    password?: string;
    confirmPassword?: string;
  }>({});
  const [oauthAvailable, setOauthAvailable] = useState(false);

  // === Google OAuth (conditionnel) ===
  const googleAuth = Google?.useAuthRequest?.({
    iosClientId: process.env.EXPO_PUBLIC_GOOGLE_CLIENT_ID_IOS,
    androidClientId: process.env.EXPO_PUBLIC_GOOGLE_CLIENT_ID_ANDROID,
    webClientId: process.env.EXPO_PUBLIC_GOOGLE_CLIENT_ID_WEB,
  });

  const googleRequest = googleAuth?.[0];
  const googleResponse = googleAuth?.[1];
  const googlePromptAsync = googleAuth?.[2];

  // Vérifier si OAuth est disponible
  useEffect(() => {
    setOauthAvailable(!!Google && !!WebBrowser);
  }, []);

  // Gérer la réponse Google
  useEffect(() => {
    if (googleResponse?.type === 'success') {
      const idToken = googleResponse.authentication?.idToken;
      if (idToken) {
        handleGoogleLogin(idToken);
      }
    } else if (googleResponse?.type === 'error') {
      Alert.alert('Erreur', 'Connexion Google échouée');
    }
  }, [googleResponse]);

  // === Handlers OAuth ===
  const handleGoogleLogin = async (idToken: string) => {
    setLoading(true);
    try {
      const result = await auth.oauthLogin('google', idToken);
      const user = await auth.getMeWithToken(result.access_token);
      setUser(user);
      router.replace(result.is_new_user ? '/onboarding/profile-setup' : '/');
    } catch (error: any) {
      const message = error.response?.data?.detail || 'Connexion Google échouée';
      Alert.alert('Erreur', message);
    } finally {
      setLoading(false);
    }
  };

  const handleAppleLogin = async () => {
    if (!AppleAuthentication) {
      Alert.alert('Non disponible', 'Apple Sign-In nécessite un dev build');
      return;
    }

    try {
      const credential = await AppleAuthentication.signInAsync({
        requestedScopes: [
          AppleAuthentication.AppleAuthenticationScope.EMAIL,
          AppleAuthentication.AppleAuthenticationScope.FULL_NAME,
        ],
      });

      if (!credential.identityToken) {
        Alert.alert('Erreur', 'Token Apple manquant');
        return;
      }

      setLoading(true);
      const result = await auth.oauthLogin('apple', credential.identityToken, {
        firstName: credential.fullName?.givenName || undefined,
        lastName: credential.fullName?.familyName || undefined,
      });
      const user = await auth.getMeWithToken(result.access_token);
      setUser(user);
      router.replace(result.is_new_user ? '/onboarding/profile-setup' : '/');
    } catch (error: any) {
      // ERR_CANCELED = utilisateur a annulé
      if (error.code !== 'ERR_REQUEST_CANCELED') {
        const message = error.response?.data?.detail || 'Connexion Apple échouée';
        Alert.alert('Erreur', message);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleGooglePress = () => {
    if (!oauthAvailable || !googlePromptAsync) {
      Alert.alert('Non disponible', 'Google Sign-In nécessite un dev build.\n\nUtilisez la connexion par email.');
      return;
    }
    googlePromptAsync();
  };

  // === Validation ===
  const validate = (): boolean => {
    const newErrors: typeof errors = {};

    if (!email) {
      newErrors.email = 'Email requis';
    } else if (!EMAIL_REGEX.test(email)) {
      newErrors.email = 'Format email invalide';
    }

    if (!password) {
      newErrors.password = 'Mot de passe requis';
    } else if (mode === 'signup' && password.length < 8) {
      newErrors.password = 'Minimum 8 caractères';
    }

    if (mode === 'signup') {
      if (!confirmPassword) {
        newErrors.confirmPassword = 'Confirmation requise';
      } else if (password !== confirmPassword) {
        newErrors.confirmPassword = 'Les mots de passe ne correspondent pas';
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  // === Handler Email Auth ===
  const handleEmailAuth = async () => {
    if (!validate()) {
      return;
    }

    setLoading(true);
    try {
      if (mode === 'login') {
        await auth.login(email, password);
        const user = await auth.getMe();
        setUser(user);
        router.replace('/');
      } else {
        const { access_token } = await auth.register(email, password);
        const user = await auth.getMeWithToken(access_token);
        setUser(user);
        router.replace('/onboarding/profile-setup');
      }
    } catch (error: any) {
      const message = error.response?.data?.detail || 'Une erreur est survenue';

      // Gestion erreur email déjà utilisé
      if (error.response?.status === 400 && message.toLowerCase().includes('email')) {
        setErrors({ email: message });
      } else {
        Alert.alert('Erreur', message);
      }
    } finally {
      setLoading(false);
    }
  };

  // === Switch mode ===
  const switchMode = (newMode: AuthMode) => {
    setMode(newMode);
    setErrors({});
    if (newMode === 'login') {
      setConfirmPassword('');
    }
  };

  // === Render Apple Button ===
  const renderAppleButton = () => {
    if (Platform.OS !== 'ios') return null;

    // Si AppleAuthentication natif disponible, utiliser le composant officiel
    if (AppleAuthentication?.AppleAuthenticationButton) {
      return (
        <AppleAuthentication.AppleAuthenticationButton
          buttonType={AppleAuthentication.AppleAuthenticationButtonType.CONTINUE}
          buttonStyle={AppleAuthentication.AppleAuthenticationButtonStyle.WHITE}
          cornerRadius={12}
          style={styles.appleButton}
          onPress={handleAppleLogin}
        />
      );
    }

    // Fallback: bouton custom
    return (
      <TouchableOpacity
        style={styles.appleButtonFallback}
        onPress={handleAppleLogin}
      >
        <Text style={styles.appleButtonText}>Continuer avec Apple</Text>
      </TouchableOpacity>
    );
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
            {/* Header */}
            <Text style={styles.logo}>Lunation</Text>
            <Text style={styles.subtitle}>Ton voyage lunaire commence ici</Text>

            {/* Tabs */}
            <View style={styles.tabs}>
              <TouchableOpacity
                style={[styles.tab, mode === 'login' && styles.tabActive]}
                onPress={() => switchMode('login')}
              >
                <Text style={[styles.tabText, mode === 'login' && styles.tabTextActive]}>
                  Connexion
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.tab, mode === 'signup' && styles.tabActive]}
                onPress={() => switchMode('signup')}
              >
                <Text style={[styles.tabText, mode === 'signup' && styles.tabTextActive]}>
                  Inscription
                </Text>
              </TouchableOpacity>
            </View>

            {/* Social Buttons */}
            <View style={styles.socialButtons}>
              {/* Apple Sign-In (iOS only) */}
              {renderAppleButton()}

              {/* Google Sign-In */}
              <TouchableOpacity
                style={[styles.googleButton, !oauthAvailable && styles.buttonUnavailable]}
                onPress={handleGooglePress}
                disabled={loading}
              >
                <Text style={styles.googleButtonText}>G  Continuer avec Google</Text>
              </TouchableOpacity>

              {!oauthAvailable && (
                <Text style={styles.oauthNote}>
                  OAuth nécessite un dev build
                </Text>
              )}
            </View>

            {/* Divider */}
            <View style={styles.divider}>
              <View style={styles.dividerLine} />
              <Text style={styles.dividerText}>ou</Text>
              <View style={styles.dividerLine} />
            </View>

            {/* Email Form */}
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

              {/* Password */}
              <View style={styles.inputContainer}>
                <TextInput
                  style={[styles.input, errors.password && styles.inputError]}
                  placeholder={mode === 'signup' ? 'Mot de passe (min. 8 caractères)' : 'Mot de passe'}
                  placeholderTextColor={colors.textMuted}
                  value={password}
                  onChangeText={(text) => {
                    setPassword(text);
                    if (errors.password) setErrors({ ...errors, password: undefined });
                  }}
                  secureTextEntry
                  autoComplete={mode === 'signup' ? 'new-password' : 'current-password'}
                />
                {errors.password && (
                  <Text style={styles.errorText}>{errors.password}</Text>
                )}
              </View>

              {/* Confirm Password (signup only) */}
              {mode === 'signup' && (
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
              )}

              {/* Submit Button */}
              <TouchableOpacity
                style={[styles.submitButton, loading && styles.buttonDisabled]}
                onPress={handleEmailAuth}
                disabled={loading}
              >
                {loading ? (
                  <ActivityIndicator color="#fff" />
                ) : (
                  <Text style={styles.submitButtonText}>
                    {mode === 'login' ? 'Se connecter' : "S'inscrire"}
                  </Text>
                )}
              </TouchableOpacity>

              {/* Forgot Password (login only) */}
              {mode === 'login' && (
                <TouchableOpacity style={styles.forgotPassword}>
                  <Text style={styles.forgotPasswordText}>Mot de passe oublié ?</Text>
                </TouchableOpacity>
              )}
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
    paddingVertical: spacing.xl,
  },
  logo: {
    fontSize: 36,
    fontWeight: 'bold',
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.xs,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: spacing.xl,
  },
  tabs: {
    flexDirection: 'row',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: 4,
    marginBottom: spacing.lg,
  },
  tab: {
    flex: 1,
    paddingVertical: spacing.sm,
    borderRadius: borderRadius.sm,
    alignItems: 'center',
  },
  tabActive: {
    backgroundColor: colors.accent,
  },
  tabText: {
    ...fonts.body,
    color: colors.textMuted,
  },
  tabTextActive: {
    color: colors.text,
    fontWeight: '600',
  },
  socialButtons: {
    marginBottom: spacing.md,
  },
  appleButton: {
    height: 50,
    marginBottom: spacing.sm,
  },
  appleButtonFallback: {
    backgroundColor: '#fff',
    height: 50,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: spacing.sm,
  },
  appleButtonText: {
    color: '#000',
    fontSize: 16,
    fontWeight: '600',
  },
  googleButton: {
    backgroundColor: '#fff',
    height: 50,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
  },
  googleButtonText: {
    color: '#000',
    fontSize: 16,
    fontWeight: '600',
  },
  buttonUnavailable: {
    opacity: 0.6,
  },
  oauthNote: {
    ...fonts.caption,
    color: colors.textMuted,
    textAlign: 'center',
    marginTop: spacing.xs,
    fontStyle: 'italic',
  },
  divider: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: spacing.md,
  },
  dividerLine: {
    flex: 1,
    height: 1,
    backgroundColor: colors.cardBg,
  },
  dividerText: {
    ...fonts.caption,
    color: colors.textMuted,
    paddingHorizontal: spacing.md,
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
  submitButton: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginTop: spacing.sm,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  submitButtonText: {
    ...fonts.button,
    color: colors.text,
  },
  forgotPassword: {
    marginTop: spacing.md,
    alignItems: 'center',
  },
  forgotPasswordText: {
    ...fonts.caption,
    color: colors.accent,
    textDecorationLine: 'underline',
  },
});
