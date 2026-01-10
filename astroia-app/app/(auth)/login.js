import { View, Text, StyleSheet, TextInput, TouchableOpacity, KeyboardAvoidingView, Platform, Alert, Animated } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';
import { useState, useEffect, useRef } from 'react';
import { useRouter } from 'expo-router';
import { useAuthStore } from '@/stores/authStore';

export default function LoginScreen() {
  const router = useRouter();
  const { signInWithOTP, isAuthenticated } = useAuthStore();
  
  const [email, setEmail] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    console.log('[ROUTING] Mounted LoginScreen');
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 600,
      useNativeDriver: true,
    }).start();
  }, []);

  // Rediriger si déjà connecté - passer par index pour la logique déterministe
  useEffect(() => {
    if (isAuthenticated) {
      console.log('[AUTH] Login - Utilisateur déjà connecté, navigation vers index (/)');
      router.replace('/');
    }
  }, [isAuthenticated]);

  const handleSendOTP = async () => {
    if (!email.trim() || !email.includes('@')) {
      Alert.alert('Email invalide', 'Veuillez entrer un email valide');
      return;
    }

    setIsLoading(true);
    const { error } = await signInWithOTP(email);
    setIsLoading(false);

    if (error) {
      Alert.alert('Erreur', error.message || 'Impossible d\'envoyer le lien de connexion');
    } else {
      // Rediriger vers l'écran de vérification OTP
      router.push({
        pathname: '/(auth)/verify-otp',
        params: { email },
      });
    }
  };

  const handleSkipAuth = () => {
    // Mode hors ligne (optionnel) - passer par index
    console.log('[AUTH] Login - Mode hors ligne, navigation vers index (/)');
    router.replace('/');
  };

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea}>
        <KeyboardAvoidingView
          behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
          style={styles.keyboardView}
        >
          <Animated.View style={[styles.content, { opacity: fadeAnim }]}>
            {/* Logo & Titre */}
            <View style={styles.header}>
              <Text style={styles.logo}>✨ LUNA</Text>
              <Text style={styles.tagline}>
                Votre guide astral personnel
              </Text>
            </View>

            {/* Formulaire */}
            <View style={styles.form}>
              <Text style={styles.formTitle}>Connexion magique</Text>
              <Text style={styles.formSubtitle}>
                Entrez votre email, nous vous enverrons un code de vérification
              </Text>

              <View style={styles.inputContainer}>
                <Ionicons name="mail-outline" size={20} color={colors.textMuted} />
                <TextInput
                  style={styles.input}
                  placeholder="votre@email.com"
                  placeholderTextColor={colors.textMuted}
                  value={email}
                  onChangeText={setEmail}
                  keyboardType="email-address"
                  autoCapitalize="none"
                  autoCorrect={false}
                />
              </View>

              <TouchableOpacity
                style={styles.button}
                onPress={handleSendOTP}
                disabled={isLoading}
                activeOpacity={0.8}
              >
                <LinearGradient
                  colors={colors.ctaGradient}
                  style={styles.buttonGradient}
                >
                  {isLoading ? (
                    <Text style={styles.buttonText}>Envoi en cours...</Text>
                  ) : (
                    <>
                      <Ionicons name="send" size={20} color="white" />
                      <Text style={styles.buttonText}>Recevoir le code</Text>
                    </>
                  )}
                </LinearGradient>
              </TouchableOpacity>

              {/* Link to signup */}
              <View style={styles.signupLink}>
                <Text style={styles.signupLinkText}>
                  Pas encore de compte ?{' '}
                </Text>
                <TouchableOpacity onPress={() => router.push('/(auth)/signup')}>
                  <Text style={styles.signupLinkButton}>Créer un compte</Text>
                </TouchableOpacity>
              </View>

              <TouchableOpacity
                style={styles.skipButton}
                onPress={handleSkipAuth}
              >
                <Text style={styles.skipText}>
                  Continuer sans compte (mode local)
                </Text>
              </TouchableOpacity>
            </View>

            {/* Footer */}
            <View style={styles.footer}>
              <Text style={styles.footerText}>
                En continuant, vous acceptez nos conditions d'utilisation
              </Text>
            </View>
          </Animated.View>
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
  content: {
    flex: 1,
    paddingHorizontal: spacing.lg,
    justifyContent: 'center',
  },

  // Header
  header: {
    alignItems: 'center',
    marginBottom: spacing.xxl,
  },
  logo: {
    fontSize: fonts.sizes.xxxl + 8,
    color: colors.text,
    fontWeight: 'bold',
    marginBottom: spacing.sm,
  },
  tagline: {
    fontSize: fonts.sizes.md,
    color: colors.textMuted,
    textAlign: 'center',
  },

  // Form
  form: {
    marginBottom: spacing.xxl,
  },
  formTitle: {
    fontSize: fonts.sizes.xxl,
    color: colors.text,
    fontWeight: 'bold',
    marginBottom: spacing.sm,
    textAlign: 'center',
  },
  formSubtitle: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: spacing.xl,
    lineHeight: 20,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    marginBottom: spacing.md,
    gap: spacing.sm,
  },
  input: {
    flex: 1,
    fontSize: fonts.sizes.md,
    color: colors.text,
    paddingVertical: spacing.sm,
  },
  button: {
    borderRadius: borderRadius.xl,
    marginBottom: spacing.md,
  },
  buttonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    borderRadius: borderRadius.xl,
    gap: spacing.sm,
  },
  buttonText: {
    fontSize: fonts.sizes.lg,
    color: 'white',
    fontWeight: 'bold',
  },
  skipButton: {
    padding: spacing.md,
    alignItems: 'center',
  },
  signupLink: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: spacing.sm,
    marginBottom: spacing.md,
  },
  signupLinkText: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
  },
  signupLinkButton: {
    fontSize: fonts.sizes.sm,
    color: colors.accent,
    fontWeight: '600',
    textDecorationLine: 'underline',
  },
  skipText: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    textDecorationLine: 'underline',
  },

  // Footer
  footer: {
    alignItems: 'center',
    paddingVertical: spacing.lg,
  },
  footerText: {
    fontSize: fonts.sizes.xs,
    color: colors.textMuted,
    textAlign: 'center',
  },
});

