# 🎨 ASTRO.IA DESIGN SYSTEM

**Version :** 1.0  
**Dernière mise à jour :** 5 novembre 2025

---

## 🎨 PALETTE DE COULEURS

### Couleurs Principales
```javascript
primary: '#8B5CF6'     // Violet cosmique
secondary: '#6366F1'   // Bleu indigo
accent: '#F59E0B'      // Doré
```

### Dégradés par Module
```javascript
// Navigation & Base
gradientDark: ['#0F172A', '#1E1B4B', '#4C1D95']

// Horoscope
gradientAube: ['#FF6B9D', '#C239B3', '#4E54C8']

// Compatibilité Couple
gradientCouple: ['#FF1744', '#F50057', '#E91E63']

// Compatibilité Amis
gradientAmis: ['#FFB300', '#FF6F00', '#F57C00']

// Compatibilité Collègues
gradientPro: ['#00B0FF', '#0091EA', '#01579B']

// CTA
ctaGradient: ['#F59E0B', '#F97316']
```

### Texte
```javascript
textLight: '#F8FAFC'           // Blanc cassé
textSecondary: '#CBD5E1'       // Gris clair
textMuted: '#94A3B8'           // Gris moyen
```

### États
```javascript
success: '#10B981'   // Vert
warning: '#F59E0B'   // Orange
error: '#EF4444'     // Rouge
info: '#3B82F6'      // Bleu
```

### Overlays
```javascript
cardBg: 'rgba(255, 255, 255, 0.08)'
cardBgLight: 'rgba(255, 255, 255, 0.15)'
divider: 'rgba(59, 30, 114, 0.3)'
```

---

## ✍️ TYPOGRAPHIE

### Tailles (strictes)
```javascript
xs: 11px   // Labels secondaires
sm: 14px   // Body, descriptions
md: 16px   // Body principal
lg: 20px   // Subtitles
xl: 24px   // Section titles
xxl: 28px  // Page titles
xxxl: 32px // Hero titles
```

### Poids
```javascript
regular: '400'
medium: '600'
bold: 'bold'
```

### Line Heights
```javascript
tight: 1.2
normal: 1.5
relaxed: 1.6
```

**Exemple d'usage :**
```javascript
// Titre de page
fontSize: 28, fontWeight: 'bold', lineHeight: 1.2

// Body text
fontSize: 14, fontWeight: '400', lineHeight: 1.5
```

---

## 📏 SPACING

### Système 4-8-16-24-32-48
```javascript
xs: 4px
sm: 8px
md: 16px
lg: 24px
xl: 32px
xxl: 48px
```

**Usage :**
- Padding cards : 20px (entre md et lg)
- Margin entre sections : 20-24px
- Gap entre éléments : 8-12px

---

## 🔲 BORDER RADIUS

```javascript
sm: 8px    // Petits éléments (badges, chips)
md: 12px   // Boutons standards
lg: 16px   // Cards
xl: 20px   // Cards hero
xxl: 24px  // Modals
full: 9999px // Éléments ronds (avatars)
```

---

## 🌊 OMBRES

### Small (Buttons)
```javascript
shadowColor: '#000',
shadowOffset: { width: 0, height: 2 },
shadowOpacity: 0.25,
shadowRadius: 3.84,
elevation: 5,
```

### Medium (Cards)
```javascript
shadowColor: '#000',
shadowOffset: { width: 0, height: 4 },
shadowOpacity: 0.3,
shadowRadius: 4.65,
elevation: 8,
```

### Large (Modals)
```javascript
shadowColor: '#000',
shadowOffset: { width: 0, height: 6 },
shadowOpacity: 0.37,
shadowRadius: 7.49,
elevation: 12,
```

### Glow (CTA, scores élevés)
```javascript
shadowColor: '#8B5CF6', // Violet
shadowOffset: { width: 0, height: 4 },
shadowOpacity: 0.5,
shadowRadius: 12,
elevation: 8,
```

---

## 🎬 ANIMATIONS

### Durées Standard
```javascript
fast: 200ms      // Micro-interactions
normal: 300ms    // Transitions standard
slow: 600ms      // FadeIn, entrées de page
verySlowjavascript : 1000ms+  // Pulsations, loops
```

### Types d'Animations

**FadeIn (standard partout) :**
```javascript
Animated.timing(fadeAnim, {
  toValue: 1,
  duration: 600,
  useNativeDriver: true,
}).start();
```

**Slide Up :**
```javascript
Animated.spring(slideAnim, {
  toValue: 0,
  tension: 50,
  friction: 8,
  useNativeDriver: true,
}).start();
```

**Pulse (scores, emojis) :**
```javascript
Animated.loop(
  Animated.sequence([
    Animated.timing(pulseAnim, {
      toValue: 1.15,
      duration: 1000,
      useNativeDriver: true,
    }),
    Animated.timing(pulseAnim, {
      toValue: 1,
      duration: 1000,
      useNativeDriver: true,
    }),
  ])
).start();
```

**Press Scale (boutons) :**
```javascript
onPressIn: () => scaleAnim.setValue(0.95)
onPressOut: () => scaleAnim.setValue(1)
```

---

## 🧩 COMPOSANTS RÉUTILISABLES

### SkeletonLoader
```javascript
import { SkeletonLoader, SkeletonCard, SkeletonProfile } from '@/components/SkeletonLoader';

<SkeletonLoader width="100%" height={20} borderRadius={8} />
<SkeletonCard />
<SkeletonProfile />
```

### EmptyState
```javascript
import { EmptyState } from '@/components/EmptyState';

<EmptyState
  icon="folder-open-outline"
  title="Aucune analyse"
  message="Créez votre première analyse pour commencer"
  actionLabel="Créer une analyse"
  onAction={() => router.push('/parent-child')}
/>
```

### ErrorState
```javascript
import { ErrorState, NetworkError, ServerError } from '@/components/ErrorState';

<ErrorState
  title="Erreur"
  message="Impossible de charger"
  onRetry={() => reload()}
/>

<NetworkError onRetry={() => reload()} />
<ServerError onRetry={() => reload()} />
```

---

## 🎯 PATTERNS D'USAGE

### Structure d'un Screen
```javascript
<View style={styles.wrapper}>
  <LinearGradient colors={GRADIENT} style={styles.container}>
    <SafeAreaView style={styles.safeArea}>
      <Stack.Screen options={{...}} />
      
      {/* Header avec bouton retour */}
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()}>
          <Ionicons name="arrow-back" />
          <Text>Retour au menu</Text>
        </TouchableOpacity>
      </View>

      {/* Contenu */}
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {loading && <SkeletonLoader />}
        {error && <ErrorState onRetry={reload} />}
        {!loading && !error && data && (
          <Animated.View style={{ opacity: fadeAnim }}>
            {/* Contenu réel */}
          </Animated.View>
        )}
      </ScrollView>
    </SafeAreaView>
  </LinearGradient>
</View>
```

### Styles Standards
```javascript
const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
    backgroundColor: '#0F172A', // Bas du dégradé
  },
  safeArea: {
    flex: 1,
  },
  container: {
    flex: 1,
  },
  scrollContent: {
    padding: 20,
    paddingTop: 5,
    paddingBottom: 60,
  },
});
```

---

## 🎭 ICONOGRAPHIE

**Source :** Ionicons (`@expo/vector-icons`)

### Icons par Context
```javascript
// Navigation
arrow-back, home, menu

// Actions
analytics, share-social, refresh, trash

// Status
checkmark-circle, alert-circle, close-circle

// Features
book, planet, heart, calendar, people, stats-chart

// Emojis contextuels
Utiliser emojis natifs (✨💫🌙⭐💚💙💛🧡)
```

### Tailles Standards
```javascript
small: 16px
medium: 20px
large: 24px
xlarge: 32px
hero: 60-80px (emojis de scores)
```

---

## 📱 SAFE AREAS

**Toujours utiliser SafeAreaView :**
```javascript
import { SafeAreaView } from 'react-native';

<View style={styles.wrapper}>
  <LinearGradient colors={...} style={styles.container}>
    <SafeAreaView style={styles.safeArea}>
      {/* Contenu */}
    </SafeAreaView>
  </LinearGradient>
</View>
```

**Évite les problèmes :**
- Encoche iPhone
- Barre de status
- Barre de navigation
- Bandeau coloré en bas

---

## ✅ CHECKLIST DESIGN

Avant de finaliser un nouveau screen :

- [ ] SafeAreaView utilisé
- [ ] Bouton "Retour au menu" présent
- [ ] Dégradé cohérent avec le module
- [ ] Animation fadeIn au chargement
- [ ] Skeleton loader pendant chargement
- [ ] Empty state si pas de données
- [ ] Error state si erreur
- [ ] Spacing respect le système (4-8-16-24-32-48)
- [ ] Border radius cohérent (8-12-16-20)
- [ ] Typographie dans les tailles standard
- [ ] Icons Ionicons
- [ ] Contraste texte/fond suffisant

---

## 🎨 EXEMPLES DE COMPOSANTS

### Card Standard
```javascript
<View style={{
  backgroundColor: 'rgba(255, 255, 255, 0.08)',
  borderRadius: 16,
  padding: 20,
  marginBottom: 16,
}}>
  <Text style={{
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 12,
  }}>
    Titre
  </Text>
  <Text style={{
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.8)',
    lineHeight: 20,
  }}>
    Description
  </Text>
</View>
```

### Bouton Primary
```javascript
<TouchableOpacity style={{
  backgroundColor: '#8B5CF6',
  paddingVertical: 16,
  paddingHorizontal: 24,
  borderRadius: 12,
  alignItems: 'center',
}}>
  <Text style={{
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  }}>
    Action
  </Text>
</TouchableOpacity>
```

### Divider
```javascript
<View style={{
  height: 1,
  backgroundColor: 'rgba(59, 30, 114, 0.3)',
  marginVertical: 16,
}} />
```

---

## 📐 GRIDS & LAYOUTS

### Grid 2 Colonnes
```javascript
<View style={{
  flexDirection: 'row',
  flexWrap: 'wrap',
  gap: 12,
}}>
  <View style={{ flex: 1, minWidth: '47%' }}>
    {/* Card 1 */}
  </View>
  <View style={{ flex: 1, minWidth: '47%' }}>
    {/* Card 2 */}
  </View>
</View>
```

### Scroll Horizontal (Zodiac)
```javascript
<ScrollView 
  horizontal 
  showsHorizontalScrollIndicator={false}
>
  {items.map(item => (
    <TouchableOpacity key={item.id} style={{ marginRight: 10 }}>
      {/* Item */}
    </TouchableOpacity>
  ))}
</ScrollView>
```

---

## 🎯 BONNES PRATIQUES

### DO ✅
- Utiliser `THEME` importé depuis `@/constants/theme`
- Animations avec `useNativeDriver: true`
- FadeIn sur tous les screens
- SafeAreaView partout
- Bouton retour sur chaque screen (sauf tabs)
- Emojis pour renforcer le message
- Loading states clairs

### DON'T ❌
- Hardcoder les couleurs (utiliser THEME)
- Oublier SafeAreaView
- Animations sans useNativeDriver
- Textes trop longs (max 2-3 lignes)
- Boutons < 44px (iOS guidelines)
- Oublier les empty/error states

---

## 📚 RESSOURCES

- **Thème :** `/constants/theme.js`
- **Composants :** `/components/`
- **Hooks :** `/hooks/`
- **Icons :** https://icons.expo.fyi

---

**Design System complet et cohérent ! 🎨✨**

