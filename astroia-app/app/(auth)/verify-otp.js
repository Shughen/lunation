import { View, Text, StyleSheet, TextInput, TouchableOpacity, KeyboardAvoidingView, Platform, Alert, ActivityIndicator, Animated } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';
import { useState, useEffect, useRef } from 'react';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { useAuthStore } from '@/stores/authStore';

export default function VerifyOTPScreen() {
  const router = useRouter();
  const params = useLocalSearchParams();
  const email = params.email || '';
  const { verifyOTP, isAuthenticated } = useAuthStore();
  
  const [code, setCode] = useState(['', '', '', '', '', '']);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const inputRefs = useRef([]);
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
      console.log('[AUTH] VerifyOTP - OTP vérifié et utilisateur connecté, navigation vers index (/)');
      router.replace('/');
    }
  }, [isAuthenticated]);

  // Rediriger si pas d'email
  useEffect(() => {
    if (!email) {
      Alert.alert('Email manquant', 'Veuillez entrer votre email d\'abord', [
        { text: 'OK', onPress: () => router.back() }
      ]);
    }
  }, [email]);

  const handleCodeChange = (text, index) => {
    // N'autoriser que les chiffres
    const numericText = text.replace(/[^0-9]/g, '');
    
    if (numericText.length > 1) {
      // Si plusieurs caractères (colle), prendre le dernier
      const lastChar = numericText[numericText.length - 1];
      const newCode = [...code];
      newCode[index] = lastChar;
      setCode(newCode);
      
      // Passer au champ suivant
      if (index < 5 && inputRefs.current[index + 1]) {
        inputRefs.current[index + 1].focus();
      }
    } else {
      const newCode = [...code];
      newCode[index] = numericText;
      setCode(newCode);
      
      // Passer automatiquement au champ suivant
      if (numericText && index < 5 && inputRefs.current[index + 1]) {
        inputRefs.current[index + 1].focus();
      }
    }
    
    setError(null);
  };

  const handleKeyPress = (key, index) => {
    // Si backspace et champ vide, revenir au champ précédent
    if (key === 'Backspace' && !code[index] && index > 0) {
      inputRefs.current[index - 1].focus();
    }
  };

  const handleVerify = async () => {
    const codeString = code.join('');
    
    if (codeString.length !== 6) {
      setError('Veuillez entrer les 6 chiffres du code');
      return;
    }

    setIsLoading(true);
    setError(null);

    const { error: verifyError } = await verifyOTP(email, codeString);
    setIsLoading(false);

    if (verifyError) {
      setError(verifyError.message || 'Code invalide. Veuillez réessayer.');
      // Réinitialiser le code en cas d'erreur
      setCode(['', '', '', '', '', '']);
      if (inputRefs.current[0]) {
        inputRefs.current[0].focus();
      }
    } else {
      // Succès - la redirection se fera via le useEffect qui surveille isAuthenticated
      console.log('[AUTH] VerifyOTP - OTP vérifié avec succès, redirection automatique via useEffect');
      Alert.alert(
        '✅ Connexion réussie !',
        'Vous êtes maintenant connecté.',
        [{ text: 'Super !' }]
      );
    }
  };

  const handleResend = async () => {
    // Retourner à l'écran de login pour renvoyer le code
    router.back();
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
                Vérification du code
              </Text>
            </View>

            {/* Instructions */}
            <View style={styles.instructionsContainer}>
              <Text style={styles.instructionsTitle}>
                Code envoyé par email
              </Text>
              <Text style={styles.instructionsText}>
                Entrez le code à 6 chiffres que nous avons envoyé à{'\n'}
                <Text style={styles.emailText}>{email}</Text>
              </Text>
            </View>

            {/* Code Inputs */}
            <View style={styles.codeContainer}>
              {code.map((digit, index) => (
                <TextInput
                  key={index}
                  ref={(ref) => (inputRefs.current[index] = ref)}
                  style={[
                    styles.codeInput,
                    digit && styles.codeInputFilled,
                    error && styles.codeInputError,
                  ]}
                  value={digit}
                  onChangeText={(text) => handleCodeChange(text, index)}
                  onKeyPress={({ nativeEvent }) => handleKeyPress(nativeEvent.key, index)}
                  keyboardType="number-pad"
                  maxLength={1}
                  selectTextOnFocus
                  editable={!isLoading}
                />
              ))}
            </View>

            {/* Error Message */}
            {error && (
              <View style={styles.errorContainer}>
                <Ionicons name="alert-circle" size={20} color={colors.error} />
                <Text style={styles.errorText}>{error}</Text>
              </View>
            )}

            {/* Verify Button */}
            <TouchableOpacity
              style={styles.button}
              onPress={handleVerify}
              disabled={isLoading || code.join('').length !== 6}
              activeOpacity={0.8}
            >
              <LinearGradient
                colors={code.join('').length === 6 && !isLoading ? colors.ctaGradient : ['#475569', '#64748B']}
                style={styles.buttonGradient}
              >
                {isLoading ? (
                  <ActivityIndicator size="small" color="white" />
                ) : (
                  <>
                    <Ionicons name="checkmark-circle" size={20} color="white" />
                    <Text style={styles.buttonText}>Vérifier</Text>
                  </>
                )}
              </LinearGradient>
            </TouchableOpacity>

            {/* Resend Link */}
            <TouchableOpacity
              style={styles.resendButton}
              onPress={handleResend}
              disabled={isLoading}
            >
              <Text style={styles.resendText}>
                Je n'ai pas reçu le code
              </Text>
            </TouchableOpacity>

            {/* Footer */}
            <View style={styles.footer}>
              <Text style={styles.footerText}>
                Le code expire dans 10 minutes
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
  instructionsContainer: {
    alignItems: 'center',
    marginBottom: spacing.xl,
  },
  instructionsTitle: {
    fontSize: fonts.sizes.xl,
    color: colors.text,
    fontWeight: 'bold',
    marginBottom: spacing.sm,
    textAlign: 'center',
  },
  instructionsText: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    textAlign: 'center',
    lineHeight: 20,
  },
  emailText: {
    color: colors.accent,
    fontWeight: '600',
  },
  codeContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: spacing.sm,
    marginBottom: spacing.lg,
  },
  codeInput: {
    width: 50,
    height: 60,
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    borderWidth: 2,
    borderColor: 'rgba(139, 92, 246, 0.3)',
    textAlign: 'center',
    fontSize: fonts.sizes.xxl,
    color: colors.text,
    fontWeight: 'bold',
  },
  codeInputFilled: {
    borderColor: colors.accent,
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
  },
  codeInputError: {
    borderColor: colors.error,
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
  },
  errorContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    padding: spacing.md,
    borderRadius: borderRadius.md,
    marginBottom: spacing.md,
    gap: spacing.sm,
    borderWidth: 1,
    borderColor: colors.error,
  },
  errorText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: colors.error,
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
  resendButton: {
    padding: spacing.md,
    alignItems: 'center',
  },
  resendText: {
    fontSize: fonts.sizes.sm,
    color: colors.accent,
    fontWeight: '600',
    textDecorationLine: 'underline',
  },
  footer: {
    alignItems: 'center',
    paddingVertical: spacing.lg,
    marginTop: spacing.xl,
  },
  footerText: {
    fontSize: fonts.sizes.xs,
    color: colors.textMuted,
    textAlign: 'center',
  },
});


