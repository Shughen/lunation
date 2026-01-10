import { View, Text, StyleSheet, TextInput, TouchableOpacity, KeyboardAvoidingView, Platform, Alert, Animated } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';
import { useState, useEffect, useRef } from 'react';
import { useRouter } from 'expo-router';
import { useAuthStore } from '@/stores/authStore';

export default function SignupScreen() {
  const router = useRouter();
  const { signUp, isAuthenticated } = useAuthStore();
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 600,
      useNativeDriver: true,
    }).start();
  }, []);

  // Rediriger si déjà connecté - passer par index pour la logique déterministe
  useEffect(() => {
    if (isAuthenticated) {
      console.log('[AUTH] Signup - Utilisateur déjà connecté, navigation vers index (/)');
      router.replace('/');
    }
  }, [isAuthenticated]);

  const validateForm = () => {
    if (!email.trim() || !email.includes('@')) {
      Alert.alert('Email invalide', 'Veuillez entrer un email valide');
      return false;
    }

    if (password.length < 6) {
      Alert.alert('Mot de passe trop court', 'Le mot de passe doit contenir au moins 6 caractères');
      return false;
    }

    if (password !== confirmPassword) {
      Alert.alert('Mots de passe différents', 'Les deux mots de passe doivent être identiques');
      return false;
    }

    return true;
  };

  const handleSignUp = async () => {
    if (!validateForm()) {
      return;
    }

    setIsLoading(true);
    console.log('[Signup] Début de la création de compte pour:', email);
    const { data, error } = await signUp(email, password);
    setIsLoading(false);

    if (error) {
      console.error('[Signup] Erreur lors de la création de compte:', error);
      Alert.alert('Erreur', error.message || 'Impossible de créer le compte');
      return;
    }

    // Attendre un peu pour que le store se mette à jour si une session a été créée
    await new Promise(resolve => setTimeout(resolve, 100));
    
    // Vérifier si l'utilisateur est maintenant connecté (pas de confirmation email nécessaire)
    console.log('[Signup] Compte créé, vérification de l\'état d\'authentification...');
    const { isAuthenticated: authStatus } = useAuthStore.getState();
    console.log('[Signup] État d\'authentification après signUp:', authStatus);
    console.log('[Signup] Données retournées par signUp:', { 
      hasUser: !!data?.user, 
      hasSession: !!data?.session,
      userEmail: data?.user?.email 
    });
    
    if (authStatus || data?.session) {
      // L'utilisateur est déjà connecté (pas de confirmation email)
      console.log('[AUTH] Signup - Compte créé et utilisateur connecté automatiquement, navigation vers index (/)');
      // La redirection se fera automatiquement via le useEffect qui surveille isAuthenticated
      // On affiche juste un message de succès
      Alert.alert(
        '✅ Compte créé !',
        'Votre compte a été créé avec succès. Vous êtes maintenant connecté.',
        [
          {
            text: 'Continuer',
            onPress: () => {
              // Le useEffect devrait déjà avoir redirigé, mais on force au cas où
              console.log('[AUTH] Signup - Navigation vers index (/) depuis Alert');
              router.replace('/');
            },
          },
        ]
      );
    } else {
      // Confirmation email nécessaire
      console.log('[Signup] Confirmation email requise, redirection vers login');
      Alert.alert(
        '✅ Compte créé !',
        'Un email de confirmation a été envoyé. Vous pouvez maintenant vous connecter.',
        [
          {
            text: 'Se connecter',
            onPress: () => router.replace('/(auth)/login'),
          },
        ]
      );
    }
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
            {/* Header */}
            <TouchableOpacity 
              style={styles.backButton}
              onPress={() => router.back()}
            >
              <Ionicons name="arrow-back" size={24} color={colors.text} />
            </TouchableOpacity>

            {/* Logo & Titre */}
            <View style={styles.header}>
              <Text style={styles.logo}>✨ LUNA</Text>
              <Text style={styles.tagline}>
                Créer mon compte
              </Text>
            </View>

            {/* Formulaire */}
            <View style={styles.form}>
              <Text style={styles.formTitle}>Inscription</Text>
              <Text style={styles.formSubtitle}>
                Créez votre compte pour sauvegarder vos données astrales
              </Text>

              {/* Email */}
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
                  editable={!isLoading}
                />
              </View>

              {/* Password */}
              <View style={styles.inputContainer}>
                <Ionicons name="lock-closed-outline" size={20} color={colors.textMuted} />
                <TextInput
                  style={styles.input}
                  placeholder="Mot de passe (min. 6 caractères)"
                  placeholderTextColor={colors.textMuted}
                  value={password}
                  onChangeText={setPassword}
                  secureTextEntry={!showPassword}
                  autoCapitalize="none"
                  autoCorrect={false}
                  editable={!isLoading}
                />
                <TouchableOpacity
                  onPress={() => setShowPassword(!showPassword)}
                  style={styles.eyeButton}
                >
                  <Ionicons
                    name={showPassword ? 'eye-outline' : 'eye-off-outline'}
                    size={20}
                    color={colors.textMuted}
                  />
                </TouchableOpacity>
              </View>

              {/* Confirm Password */}
              <View style={styles.inputContainer}>
                <Ionicons name="lock-closed-outline" size={20} color={colors.textMuted} />
                <TextInput
                  style={styles.input}
                  placeholder="Confirmer le mot de passe"
                  placeholderTextColor={colors.textMuted}
                  value={confirmPassword}
                  onChangeText={setConfirmPassword}
                  secureTextEntry={!showConfirmPassword}
                  autoCapitalize="none"
                  autoCorrect={false}
                  editable={!isLoading}
                />
                <TouchableOpacity
                  onPress={() => setShowConfirmPassword(!showConfirmPassword)}
                  style={styles.eyeButton}
                >
                  <Ionicons
                    name={showConfirmPassword ? 'eye-outline' : 'eye-off-outline'}
                    size={20}
                    color={colors.textMuted}
                  />
                </TouchableOpacity>
              </View>

              <TouchableOpacity
                style={styles.button}
                onPress={handleSignUp}
                disabled={isLoading}
                activeOpacity={0.8}
              >
                <LinearGradient
                  colors={colors.ctaGradient}
                  style={styles.buttonGradient}
                >
                  {isLoading ? (
                    <Text style={styles.buttonText}>Création en cours...</Text>
                  ) : (
                    <>
                      <Ionicons name="person-add" size={20} color="white" />
                      <Text style={styles.buttonText}>Créer mon compte</Text>
                    </>
                  )}
                </LinearGradient>
              </TouchableOpacity>

              {/* Link to login */}
              <View style={styles.loginLink}>
                <Text style={styles.loginLinkText}>
                  Vous avez déjà un compte ?{' '}
                </Text>
                <TouchableOpacity onPress={() => router.replace('/(auth)/login')}>
                  <Text style={styles.loginLinkButton}>Se connecter</Text>
                </TouchableOpacity>
              </View>
            </View>

            {/* Footer */}
            <View style={styles.footer}>
              <Text style={styles.footerText}>
                En créant un compte, vous acceptez nos conditions d'utilisation
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
  backButton: {
    position: 'absolute',
    top: spacing.lg,
    left: spacing.lg,
    width: 40,
    height: 40,
    alignItems: 'center',
    justifyContent: 'center',
    zIndex: 10,
  },
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
  eyeButton: {
    padding: spacing.xs,
  },
  button: {
    borderRadius: borderRadius.xl,
    marginTop: spacing.md,
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
  loginLink: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: spacing.sm,
  },
  loginLinkText: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
  },
  loginLinkButton: {
    fontSize: fonts.sizes.sm,
    color: colors.accent,
    fontWeight: '600',
    textDecorationLine: 'underline',
  },
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


