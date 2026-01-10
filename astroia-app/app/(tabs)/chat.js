import { 
  View, 
  Text, 
  StyleSheet, 
  TextInput, 
  TouchableOpacity, 
  ScrollView, 
  KeyboardAvoidingView, 
  Platform, 
  Animated,
  Alert,
  ActivityIndicator 
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { colors, fonts, spacing, borderRadius } from '@/constants/theme';
import { useState, useEffect, useRef } from 'react';
import { useAuthStore } from '@/stores/authStore';
import { useProfileStore } from '@/stores/profileStore';
import { aiChatService } from '@/lib/api/aiChatService';
import { getAIContext } from '@/lib/services/contextService';
import NetInfo from '@react-native-community/netinfo';
import { canSendMessage, incrementUsage } from '@/lib/services/rateLimitService';
import { useRouter } from 'expo-router';

export default function ChatScreen() {
  const { user } = useAuthStore();
  const { profile, getZodiacSign } = useProfileStore();
  const router = useRouter();

  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'bot',
      text: "Bonjour ! Je suis votre assistant astral IA. Posez-moi vos questions sur l'astrologie, votre thème natal ou votre horoscope. ✨",
      timestamp: new Date(),
    }
  ]);
  const [isTyping, setIsTyping] = useState(false);
  const [conversationId, setConversationId] = useState(null);
  const [isOnline, setIsOnline] = useState(true);
  const [error, setError] = useState(null);
  
  const scrollViewRef = useRef(null);
  const fadeAnim = useRef(new Animated.Value(0)).current;

  // Détection connexion réseau
  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsOnline(state.isConnected ?? true);
      if (!state.isConnected) {
        setError('Pas de connexion internet');
      } else if (error === 'Pas de connexion internet') {
        setError(null);
      }
    });
    return () => unsubscribe();
  }, [error]);

  useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 400,
      useNativeDriver: true,
    }).start();
  }, []);

  useEffect(() => {
    // Auto-scroll au dernier message
    scrollViewRef.current?.scrollToEnd({ animated: true });
  }, [messages, isTyping]);

  const handleSend = async () => {
    if (!message.trim()) return;

    // Vérifier la connexion
    if (!isOnline) {
      Alert.alert('Hors ligne', 'Connectez-vous à internet pour utiliser l\'IA');
      return;
    }

    // ✅ 1. Vérifier rate limit AVANT d'envoyer
    const { allowed, remaining } = await canSendMessage();

    if (!allowed) {
      Alert.alert(
        'Limite atteinte 🚫',
        'Tu as utilisé tes 10 messages gratuits aujourd\'hui.\n\nReviens demain ou passe à la version Premium pour un accès illimité ! 💎',
        [
          { text: 'OK' },
          {
            text: 'Voir Premium',
            onPress: () => {
              // TODO: Créer la page premium
              Alert.alert('À venir', 'La page Premium arrive bientôt !');
            },
          },
        ]
      );
      return;
    }

    const userMessage = {
      id: Date.now().toString(),
      type: 'user',
      text: message.trim(),
      timestamp: new Date(),
    };

    // Ajouter le message de l'utilisateur (optimistic UI)
    setMessages(prev => [...prev, userMessage]);
    setMessage('');
    setError(null);
    setIsTyping(true);

    try {
      // Construire l'historique pour l'API
      const apiMessages = messages
        .concat(userMessage)
        .filter(m => m.type !== 'error')
        .map(m => ({
          role: m.type === 'user' ? 'user' : 'assistant',
          content: m.text,
        }));

      // Préparer le profil astrologique
      const zodiacSign = getZodiacSign();
      const astroProfile = profile.name ? {
        name: profile.name,
        birthDate: profile.birthDate?.toLocaleDateString('fr-FR'),
        zodiacSign: zodiacSign?.sign,
        zodiacElement: zodiacSign?.element,
      } : null;

      // 🆕 Récupérer le contexte cycle pour enrichir la réponse
      const aiContext = await getAIContext();
      console.log('[Chat] AI Context:', aiContext.contextText ? 'Context available' : 'No context');

      // Appeler l'API avec le contexte enrichi
      const response = await aiChatService.sendMessage({
        chatId: conversationId,
        userId: user?.id || 'anonymous',
        messages: apiMessages,
        astroProfile,
        cycleContext: aiContext.contextText || null, // 🆕 Ajout contexte cycle
      });

      // Sauvegarder l'ID de conversation
      if (response.conversationId && !conversationId) {
        setConversationId(response.conversationId);
      }

      // Ajouter la réponse de l'IA
      const botMessage = {
        id: (Date.now() + 1).toString(),
        type: 'bot',
        text: response.message,
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, botMessage]);
      setIsTyping(false);

      // ✅ 3. Incrémenter usage APRÈS succès
      await incrementUsage();

      // ✅ 4. Afficher alerte si proche limite (3 messages restants ou moins)
      const updatedRemaining = remaining - 1;
      if (updatedRemaining <= 3 && updatedRemaining > 0) {
        Alert.alert(
          'Limite proche ⚠️',
          `Plus que ${updatedRemaining} message${updatedRemaining > 1 ? 's' : ''} aujourd'hui.`,
          [{ text: 'OK' }]
        );
      }

    } catch (error) {
      console.error('[Chat] Error:', error);
      setIsTyping(false);
      
      const errorMessage = error.message || 'Une erreur est survenue';
      setError(errorMessage);

      // Ajouter un message d'erreur visible
      const errorMsg = {
        id: (Date.now() + 1).toString(),
        type: 'error',
        text: `❌ ${errorMessage}`,
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, errorMsg]);

      // Afficher l'erreur avec option retry
      Alert.alert(
        'Erreur',
        errorMessage,
        [
          { text: 'Annuler', style: 'cancel' },
          { 
            text: 'Réessayer', 
            onPress: () => {
              // Retirer le message utilisateur et le message d'erreur
              setMessages(prev => prev.slice(0, -2));
              setMessage(userMessage.text);
            }
          },
        ]
      );
    }
  };

  const handleSuggestion = (text) => {
    setMessage(text);
  };

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea} edges={['bottom']}>
        <KeyboardAvoidingView 
          behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
          style={styles.keyboardView}
          keyboardVerticalOffset={90}
        >
          {/* Bannière d'erreur */}
          {error && (
            <View style={styles.errorBanner}>
              <Ionicons name="warning" size={20} color={colors.error} />
              <Text style={styles.errorText}>{error}</Text>
              <TouchableOpacity onPress={() => setError(null)}>
                <Ionicons name="close" size={20} color={colors.error} />
              </TouchableOpacity>
            </View>
          )}

          {/* Messages */}
          <Animated.ScrollView
            ref={scrollViewRef}
            contentContainerStyle={styles.messagesContainer}
            showsVerticalScrollIndicator={false}
            style={{ opacity: fadeAnim }}
          >
            {messages.map((msg) => (
              <MessageBubble key={msg.id} message={msg} />
            ))}
            
            {/* Indicateur de saisie */}
            {isTyping && <TypingIndicator />}
          </Animated.ScrollView>

          {/* Suggestions rapides */}
          {messages.length <= 2 && (
            <ScrollView 
              horizontal 
              showsHorizontalScrollIndicator={false}
              contentContainerStyle={styles.suggestionsContainer}
            >
              <SuggestionChip 
                icon="star" 
                text="Mon signe" 
                onPress={() => handleSuggestion("Quel est mon signe astrologique ?")}
              />
              <SuggestionChip 
                icon="heart" 
                text="Compatibilité" 
                onPress={() => handleSuggestion("Comment fonctionne la compatibilité astrologique ?")}
              />
              <SuggestionChip 
                icon="planet" 
                text="Thème natal" 
                onPress={() => handleSuggestion("C'est quoi un thème natal ?")}
              />
              <SuggestionChip 
                icon="calendar" 
                text="Horoscope" 
                onPress={() => handleSuggestion("Quel est mon horoscope du jour ?")}
              />
            </ScrollView>
          )}

          {/* Input zone */}
          <View style={styles.inputContainer}>
            <View style={styles.inputWrapper}>
              <TextInput
                style={styles.input}
                placeholder="Posez votre question..."
                placeholderTextColor={colors.textMuted}
                value={message}
                onChangeText={setMessage}
                multiline
                maxLength={500}
                onSubmitEditing={handleSend}
                editable={!isTyping && isOnline}
              />
              <TouchableOpacity 
                style={[styles.sendButton, (!message.trim() || isTyping || !isOnline) && styles.sendButtonDisabled]}
                onPress={handleSend}
                disabled={!message.trim() || isTyping || !isOnline}
                activeOpacity={0.7}
              >
                <LinearGradient
                  colors={message.trim() && isOnline && !isTyping ? colors.ctaGradient : ['#475569', '#64748B']}
                  style={styles.sendGradient}
                >
                  {isTyping ? (
                    <ActivityIndicator size="small" color="white" />
                  ) : (
                    <Ionicons name="send" size={20} color="white" />
                  )}
                </LinearGradient>
              </TouchableOpacity>
            </View>
            {!isOnline && (
              <Text style={styles.offlineText}>Mode hors ligne</Text>
            )}
          </View>
        </KeyboardAvoidingView>
      </SafeAreaView>
    </LinearGradient>
  );
}

function MessageBubble({ message }) {
  const isBot = message.type === 'bot';
  const isError = message.type === 'error';
  const scaleAnim = useRef(new Animated.Value(0.8)).current;
  
  useEffect(() => {
    Animated.spring(scaleAnim, {
      toValue: 1,
      tension: 100,
      friction: 7,
      useNativeDriver: true,
    }).start();
  }, []);
  
  return (
    <Animated.View style={[
      styles.messageBubble, 
      isBot ? styles.botBubble : styles.userBubble,
      { transform: [{ scale: scaleAnim }] }
    ]}>
      {isBot && (
        <View style={styles.botAvatar}>
          <Ionicons name="sparkles" size={16} color={colors.accent} />
        </View>
      )}
      <View style={[
        styles.messageContent, 
        isBot ? styles.botContent : isError ? styles.errorContent : styles.userContent
      ]}>
        <Text style={[
          styles.messageText, 
          isBot ? styles.botText : isError ? styles.errorText : styles.userText
        ]}>
          {message.text}
        </Text>
      </View>
    </Animated.View>
  );
}

function TypingIndicator() {
  const dot1 = useRef(new Animated.Value(0)).current;
  const dot2 = useRef(new Animated.Value(0)).current;
  const dot3 = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    const animate = (dot, delay) => {
      Animated.loop(
        Animated.sequence([
          Animated.delay(delay),
          Animated.timing(dot, {
            toValue: -8,
            duration: 400,
            useNativeDriver: true,
          }),
          Animated.timing(dot, {
            toValue: 0,
            duration: 400,
            useNativeDriver: true,
          }),
        ])
      ).start();
    };

    animate(dot1, 0);
    animate(dot2, 200);
    animate(dot3, 400);
  }, []);

  return (
    <View style={styles.typingContainer}>
      <View style={styles.botAvatar}>
        <Ionicons name="sparkles" size={16} color={colors.accent} />
      </View>
      <View style={styles.typingBubble}>
        <Animated.View style={[styles.typingDot, { transform: [{ translateY: dot1 }] }]} />
        <Animated.View style={[styles.typingDot, { transform: [{ translateY: dot2 }] }]} />
        <Animated.View style={[styles.typingDot, { transform: [{ translateY: dot3 }] }]} />
      </View>
    </View>
  );
}

function SuggestionChip({ icon, text, onPress }) {
  return (
    <TouchableOpacity style={styles.suggestionChip} onPress={onPress} activeOpacity={0.7}>
      <Ionicons name={icon} size={16} color={colors.accent} />
      <Text style={styles.suggestionText}>{text}</Text>
    </TouchableOpacity>
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

  // Error Banner
  errorBanner: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    padding: spacing.sm,
    marginHorizontal: spacing.md,
    marginTop: spacing.sm,
    borderRadius: borderRadius.md,
    gap: spacing.sm,
    borderWidth: 1,
    borderColor: colors.error,
  },
  errorText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: colors.error,
  },

  // Messages
  messagesContainer: {
    padding: spacing.md,
    gap: spacing.md,
  },
  messageBubble: {
    flexDirection: 'row',
    alignItems: 'flex-end',
    gap: spacing.sm,
  },
  botBubble: {
    justifyContent: 'flex-start',
  },
  userBubble: {
    justifyContent: 'flex-end',
  },
  botAvatar: {
    width: 32,
    height: 32,
    borderRadius: borderRadius.full,
    backgroundColor: 'rgba(245, 158, 11, 0.2)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  messageContent: {
    maxWidth: '75%',
    padding: spacing.md,
    borderRadius: borderRadius.lg,
  },
  botContent: {
    backgroundColor: colors.cardBg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  userContent: {
    backgroundColor: colors.accent,
  },
  errorContent: {
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    borderWidth: 1,
    borderColor: colors.error,
  },
  messageText: {
    fontSize: fonts.sizes.md,
    lineHeight: 22,
  },
  botText: {
    color: colors.text,
  },
  userText: {
    color: 'white',
  },

  // Typing Indicator
  typingContainer: {
    flexDirection: 'row',
    alignItems: 'flex-end',
    gap: spacing.sm,
  },
  typingBubble: {
    flexDirection: 'row',
    backgroundColor: colors.cardBg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
    padding: spacing.md,
    borderRadius: borderRadius.lg,
    gap: spacing.xs,
    alignItems: 'center',
    justifyContent: 'center',
  },
  typingDot: {
    width: 8,
    height: 8,
    borderRadius: borderRadius.full,
    backgroundColor: colors.accent,
  },

  // Suggestions
  suggestionsContainer: {
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    gap: spacing.sm,
  },
  suggestionChip: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.cardBg,
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    borderRadius: borderRadius.full,
    gap: spacing.xs,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
  },
  suggestionText: {
    fontSize: fonts.sizes.sm,
    color: colors.text,
    fontWeight: '600',
  },

  // Input
  inputContainer: {
    padding: spacing.md,
    paddingTop: spacing.sm,
  },
  inputWrapper: {
    flexDirection: 'row',
    alignItems: 'flex-end',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    gap: spacing.sm,
  },
  input: {
    flex: 1,
    color: colors.text,
    fontSize: fonts.sizes.md,
    maxHeight: 100,
    paddingVertical: spacing.xs,
  },
  sendButton: {
    marginBottom: 2,
  },
  sendButtonDisabled: {
    opacity: 0.5,
  },
  sendGradient: {
    width: 40,
    height: 40,
    borderRadius: borderRadius.full,
    alignItems: 'center',
    justifyContent: 'center',
  },
  offlineText: {
    fontSize: fonts.sizes.xs,
    color: colors.textMuted,
    textAlign: 'center',
    marginTop: spacing.xs,
  },
});
