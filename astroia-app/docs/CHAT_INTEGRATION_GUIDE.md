# 🤖 Guide d'intégration du Chat IA

Ce guide explique comment remplacer le stub local par l'API réelle dans `app/(tabs)/chat.js`.

---

## 📋 Prérequis

- ✅ API déployée sur Vercel
- ✅ URL configurée dans `app.json`
- ✅ Service `aiChatService` créé

---

## 🔧 Modifications à apporter

### 1. Imports et hooks

```javascript
// Ajouter ces imports en haut
import { useAuthStore } from '@/stores/authStore';
import { useProfileStore } from '@/stores/profileStore';
import { aiChatService } from '@/lib/api/aiChatService';
import NetInfo from '@react-native-community/netinfo';
```

### 2. État du composant

```javascript
const { user, isAuthenticated } = useAuthStore();
const { profile } = useProfileStore();

const [conversationId, setConversationId] = useState(null);
const [isOnline, setIsOnline] = useState(true);
const [error, setError] = useState(null);

// Détecter la connexion
useEffect(() => {
  const unsubscribe = NetInfo.addEventListener(state => {
    setIsOnline(state.isConnected);
  });
  return () => unsubscribe();
}, []);
```

### 3. Fonction handleSend (remplacer complètement)

```javascript
const handleSend = async () => {
  if (!message.trim()) return;

  // Vérifier la connexion
  if (!isOnline) {
    Alert.alert('Hors ligne', 'Connectez-vous à internet pour utiliser l\'IA');
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
    const apiMessages = messages.concat(userMessage).map(m => ({
      role: m.type === 'user' ? 'user' : 'assistant',
      content: m.text,
    }));

    // Appeler l'API
    const response = await aiChatService.sendMessage({
      chatId: conversationId,
      userId: user?.id || 'anonymous',
      messages: apiMessages,
      astroProfile: profile ? {
        name: profile.name,
        birthDate: profile.birthDate?.toISOString(),
        zodiacSign: profile.zodiacSign,
        zodiacElement: profile.zodiacElement,
      } : null,
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

  } catch (error) {
    console.error('Chat error:', error);
    setIsTyping(false);
    setError(error.message);

    // Afficher l'erreur
    Alert.alert(
      'Erreur',
      error.message,
      [
        { text: 'Annuler', style: 'cancel' },
        { text: 'Réessayer', onPress: () => handleSend() },
      ]
    );
  }
};
```

### 4. Affichage des erreurs

```jsx
{/* Afficher l'erreur */}
{error && (
  <View style={styles.errorBanner}>
    <Ionicons name="warning" size={20} color={colors.error} />
    <Text style={styles.errorText}>{error}</Text>
    <TouchableOpacity onPress={() => setError(null)}>
      <Ionicons name="close" size={20} color={colors.error} />
    </TouchableOpacity>
  </View>
)}
```

### 5. Styles pour l'erreur

```javascript
errorBanner: {
  flexDirection: 'row',
  alignItems: 'center',
  backgroundColor: 'rgba(239, 68, 68, 0.1)',
  padding: spacing.sm,
  marginHorizontal: spacing.md,
  marginBottom: spacing.sm,
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
```

---

## 🧪 Tests

### Test 1 : Message simple
1. Ouvre le chat
2. Envoie "Bonjour"
3. Vérifie la réponse de l'IA
4. Vérifie dans Supabase que les messages sont enregistrés

### Test 2 : Avec profil
1. Complète ton profil astral
2. Envoie "Comment gérer mon stress ?"
3. L'IA doit mentionner ton signe

### Test 3 : Erreurs
1. Mets l'app en mode avion
2. Envoie un message
3. Vérifie le message d'erreur
4. Réactive le réseau
5. Clique "Réessayer"

### Test 4 : Conversation longue
1. Envoie 5-6 messages
2. Vérifie que le contexte est gardé
3. Vérifie la latence (< 5s normalement)

---

## 📊 Monitoring

### Logs à vérifier

**Console app :**
```
[AIChatService] Sending message...
[AIChatService] Response received: {...}
```

**Console Vercel :**
```
[API] Chat request - User: xxx, Messages: 3
[API] Success - Latency: 2500ms, Tokens: 450
```

**Supabase Dashboard :**
- Table `chat_messages` se remplit
- Table `chat_conversations` créée

---

## 🚀 Optimisations futures

### 1. Streaming

Remplacer `stream: false` par `stream: true` dans l'API :

```typescript
// Dans api/ai/chat.ts
const stream = await openai.chat.completions.create({
  model: 'gpt-4o-mini',
  messages: contextualizedMessages,
  stream: true,
});

for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content || '';
  // Envoyer chunk par chunk via Server-Sent Events
}
```

Côté client :

```javascript
// Utiliser EventSource ou fetch avec ReadableStream
const response = await fetch(AI_API_URL, {
  method: 'POST',
  body: JSON.stringify({...}),
});

const reader = response.body.getReader();
// Lire le stream progressivement
```

### 2. Cache local

```javascript
// Utiliser AsyncStorage pour cache
const cacheKey = `chat_${conversationId}`;
await AsyncStorage.setItem(cacheKey, JSON.stringify(messages));
```

### 3. Retry automatique

```javascript
async function sendWithRetry(params, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await aiChatService.sendMessage(params);
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}
```

### 4. Rate limiting côté client

```javascript
const [lastMessageTime, setLastMessageTime] = useState(0);

const handleSend = async () => {
  const now = Date.now();
  if (now - lastMessageTime < 2000) {
    Alert.alert('Trop rapide', 'Attendez 2 secondes entre chaque message');
    return;
  }
  setLastMessageTime(now);
  // ...
};
```

---

## 🎯 Checklist finale

- [ ] Imports ajoutés
- [ ] État mis à jour
- [ ] handleSend remplacé
- [ ] Erreurs affichées
- [ ] Tests passés
- [ ] Logs vérifiés
- [ ] Testée sur device réel
- [ ] Performance OK (< 5s)

---

**Le chat IA est maintenant connecté à l'API ! 🎉**

