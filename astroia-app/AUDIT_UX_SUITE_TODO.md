# 📋 AUDIT UX SUITE - TODO SPRINT 14

**Date :** 10 novembre 2025  
**Status :** En attente  
**Modules restants :** 4 (Thème Natal, Compatibilité, Horoscope, Recommendations)

---

## 🎯 **RÉSUMÉ : CE QUI A ÉTÉ FAIT (SPRINT 13.5)**

### ✅ **Livrés** (Commits 1-6)
1. ✅ **Design System LUNA** (13 fichiers, tokens + 9 composants + utils)
2. ✅ **Home refactoré** (StatusBar + SafeAreaView + ExploreGrid + Haptics)
3. ✅ **Journal refactoré** (Empty DS + A11y + Haptics + TypeScript)
4. ✅ **Compatibilité** (2 bugs fixés : double bouton + partage enrichi)
5. ✅ **i18n simple** (30+ chaînes)
6. ✅ **Documentation complète** (`AUDIT_UX_COMPLETE.md`)

---

## 📝 **CE QUI RESTE À FAIRE (SPRINT 14)**

### 🌌 **1. THÈME NATAL** (`app/natal-chart/index.js`, 569 lignes)

#### **Améliorations à implémenter :**

✅ **AlertBanner** au lieu du disclaimer actuel
```tsx
// Remplacer le <View style={styles.disclaimerCard}> par :
<AlertBanner 
  variant="warning"
  title="Version simplifiée (V1)"
  message="Soleil et Lune précis. Ascendant approximatif (±10°). Pour précision professionnelle, consultez Astrotheme.com"
/>
```

✅ **Légende** sous la "Carte du ciel"
```tsx
<View style={styles.chartCard}>
  <ZodiacWheel positions={positions} />
  <Text style={{ textAlign: 'center', color: colors.textMuted, marginTop: 8, fontSize: 12 }}>
    ☉ Soleil · ☽ Lune · ↑ Ascendant
  </Text>
</View>
```

✅ **Espacements** entre sections
```tsx
// Ajouter marginTop: 24 entre :
// - Carte du ciel
// - Positions planétaires
// - CTA Recalculer

// Gap 12 entre PlanetCards :
<View style={{ gap: 12 }}>
  <PlanetCard ... />
  <PlanetCard ... />
</View>
```

✅ **PlanetCard améliorée**
```tsx
// Dans le composant PlanetCard :
<View style={{
  flexDirection: 'row',
  alignItems: 'center', // Au lieu de flex-start
  gap: 12,
  backgroundColor: colors.surfaceElevated, // Au lieu de surface
  padding: 16,
  borderRadius: 16,
}}>
  <Ionicons size={24} /> {/* Taille uniforme */}
  <View style={{ flex: 1 }}>
    <Text style={{ lineHeight: 20 }}>{planet}</Text>
    <Text style={{ lineHeight: 20 }}>{position.sign}</Text>
  </View>
</View>
```

✅ **CTA Recalculer** avec loading + SafeArea
```tsx
<TouchableOpacity 
  style={[styles.computeButton, { marginBottom: insets.bottom + 12 }]}
  onPress={handleCompute}
  disabled={isComputing}
>
  <LinearGradient colors={['#FF7E5F', '#FF6B9D']} style={styles.computeGradient}>
    {isComputing ? (
      <ActivityIndicator size="small" color="white" />
    ) : (
      <Ionicons name="refresh" size={20} color="white" />
    )}
    <Text style={styles.computeText}>
      {isComputing ? 'Calcul en cours...' : 'Recalculer'}
    </Text>
  </LinearGradient>
</TouchableOpacity>

{/* Texte état */}
<Text style={{ 
  color: colors.textMuted, 
  fontSize: 12, 
  textAlign: 'center', 
  marginTop: 8,
  marginBottom: insets.bottom + 12
}}>
  Dernière mise à jour : {formatDate(natalChart?.updatedAt)} • Limite : 1 calcul / 24h
</Text>
```

✅ **Animation fadeIn** sur "Sauvegardé dans le profil"
```tsx
const savedFadeAnim = useRef(new Animated.Value(0)).current;

useEffect(() => {
  if (natalChart?.savedToProfile) {
    Animated.timing(savedFadeAnim, {
      toValue: 1,
      duration: 400,
      useNativeDriver: true,
    }).start();
  }
}, [natalChart?.savedToProfile]);

// Dans le JSX :
<Animated.View style={{ opacity: savedFadeAnim }}>
  <Text style={styles.savedLabel}>✅ Sauvegardé dans le profil</Text>
</Animated.View>
```

---

### 💞 **2. COMPATIBILITÉ** (`app/compatibility/index.js`, 1003 lignes)

#### **Améliorations à implémenter :**

✅ **Gradient cohérent**
```tsx
// Remplacer le fond actuel par :
<LinearGradient 
  colors={['#FF4E80', '#FF6BA0', '#FF8BC0']} 
  style={StyleSheet.absoluteFillObject}
  start={{ x: 0, y: 0 }}
  end={{ x: 0, y: 1 }}
/>
```

✅ **Validation formulaire**
```tsx
const canAnalyze = () => {
  if (hasNatal()) {
    // Si thème natal, vérifier juste person2
    return person2.sunSign && person2.moonSign && person2.ascendant;
  } else {
    // Sinon vérifier person1 ET person2
    return person1.sunSign && person1.moonSign && person1.ascendant &&
           person2.sunSign && person2.moonSign && person2.ascendant;
  }
};

// Dans le bouton :
<TouchableOpacity
  disabled={!canAnalyze() || loading}
  style={[
    styles.analyzeButton,
    (!canAnalyze() || loading) && styles.analyzeButtonDisabled
  ]}
  onPress={handleAnalyze}
>
```

✅ **Spinner pendant analyse** (déjà fait avec `loading` state)

✅ **Feedback Toast**
```tsx
// Ajouter en début d'analyse :
import { ToastAndroid, Platform } from 'react-native';

const showToast = (message) => {
  if (Platform.OS === 'android') {
    ToastAndroid.show(message, ToastAndroid.SHORT);
  } else {
    // Utiliser Alert simple ou une librairie toast
    Alert.alert('', message, [{ text: 'OK' }]);
  }
};

// Dans handleAnalyze :
showToast('Analyse en cours…');
```

✅ **Cartes relation responsive**
```tsx
<View style={styles.typeCards}>
  {RELATION_TYPES.map((type) => (
    <TouchableOpacity
      key={type.id}
      style={[
        styles.typeCard,
        { 
          minWidth: 110, 
          flexShrink: 1 
        },
        relationType === type.id && styles.typeCardActive,
      ]}
    >
      <Text style={{ fontSize: 15, textAlign: 'center' }}>{type.name}</Text>
    </TouchableOpacity>
  ))}
</View>

// Dans styles :
typeCards: {
  flexDirection: 'row',
  flexWrap: 'wrap', // Permettre retour à la ligne
  gap: 12,
},
```

---

### ♏️ **3. HOROSCOPE** (`app/horoscope/index.js`, à trouver)

#### **Améliorations à implémenter :**

✅ **SectionTitle component**
```tsx
const SectionTitle = ({ icon, title }) => (
  <Text style={{
    fontSize: 18,
    fontWeight: '700',
    color: colors.text,
    marginBottom: 8,
    marginTop: 24,
  }}>
    {icon} {title}
  </Text>
);

// Utiliser :
<SectionTitle icon="💼" title="Travail" />
<SectionTitle icon="❤️" title="Amour" />
<SectionTitle icon="💪" title="Santé" />
<SectionTitle icon="✨" title="Conseil du jour" />
```

✅ **Paragraphes lisibles**
```tsx
<Text style={{
  maxWidth: '90%',
  alignSelf: 'center',
  lineHeight: 22,
  color: colors.text,
  fontSize: 15,
}}>
  {content}
</Text>
```

✅ **CTA "Actualiser"** amélioré
```tsx
<TouchableOpacity 
  style={styles.refreshButton}
  onPress={handleRefresh}
  disabled={isRefreshing}
>
  <LinearGradient
    colors={['#FF7E9A', '#FFB5C5']}
    style={styles.refreshGradient}
  >
    {isRefreshing ? (
      <ActivityIndicator size="small" color="white" />
    ) : (
      <Ionicons name="refresh" size={20} color="white" />
    )}
    <Text style={styles.refreshText}>
      {isRefreshing ? 'Mise à jour...' : 'Actualiser'}
    </Text>
  </LinearGradient>
</TouchableOpacity>
```

✅ **Bloc info bas**
```tsx
<View style={{
  backgroundColor: '#ffffff12',
  borderRadius: 16,
  padding: 12,
  marginTop: 24,
  flexDirection: 'row',
  justifyContent: 'space-around',
}}>
  <View style={{ alignItems: 'center' }}>
    <Text style={{ fontSize: 24 }}>🍀</Text>
    <Text style={{ color: colors.text, fontWeight: '600' }}>34</Text>
    <Text style={{ color: colors.textMuted, fontSize: 12 }}>Chance</Text>
  </View>
  <View style={{ alignItems: 'center' }}>
    <Text style={{ fontSize: 24 }}>🌙</Text>
    <Text style={{ color: colors.text, fontWeight: '600' }}>Vierge</Text>
    <Text style={{ color: colors.textMuted, fontSize: 12 }}>Lune</Text>
  </View>
</View>
```

✅ **Feedback Toast**
```tsx
// Après refresh :
showToast('Horoscope mis à jour à ' + new Date().toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' }));
```

---

### ✨ **4. RECOMMENDATIONS** (`components/RecommendationGroup.tsx`, à créer)

#### **Composant à créer :**

```tsx
import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Share } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { color, space, radius, type as typography } from '@/theme/tokens';
import haptics from '@/utils/haptics';

interface RecommendationItem {
  icon: string;
  title: string;
  body: string;
}

interface RecommendationGroupProps {
  title: string;
  icon: string;
  items: RecommendationItem[];
}

export default function RecommendationGroup({ 
  title, 
  icon, 
  items 
}: RecommendationGroupProps) {
  const handleShare = async (item: RecommendationItem) => {
    haptics.light();
    try {
      await Share.share({
        message: `${item.icon} ${item.title}\n\n${item.body}`,
      });
    } catch (error) {
      console.error('Share error:', error);
    }
  };

  const handleAddToJournal = (item: RecommendationItem) => {
    haptics.medium();
    router.push({
      pathname: '/journal/new',
      params: {
        prefilledNote: `${item.icon} ${item.title}\n\n${item.body}`,
      },
    });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{icon} {title}</Text>
      
      {items.map((item, index) => (
        <View key={index} style={styles.card}>
          <View style={styles.cardHeader}>
            <View style={styles.cardContent}>
              <Text style={styles.itemIcon}>{item.icon}</Text>
              <View style={{ flex: 1 }}>
                <Text style={styles.itemTitle}>{item.title}</Text>
                <Text style={styles.itemBody}>{item.body}</Text>
              </View>
            </View>
            
            <View style={styles.actions}>
              <TouchableOpacity
                onPress={() => handleShare(item)}
                hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}
                accessibilityRole="button"
                accessibilityLabel="Partager cette recommandation"
              >
                <Ionicons name="share-social-outline" size={22} color={color.brand} />
              </TouchableOpacity>
              
              <TouchableOpacity
                onPress={() => handleAddToJournal(item)}
                hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}
                accessibilityRole="button"
                accessibilityLabel="Ajouter au journal"
              >
                <Ionicons name="book-outline" size={22} color={color.brand} />
              </TouchableOpacity>
            </View>
          </View>
        </View>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginVertical: space.lg,
  },
  title: {
    ...typography.h3,
    color: color.text,
    marginBottom: space.md,
  },
  card: {
    backgroundColor: color.surfaceElevated,
    borderRadius: radius.lg,
    padding: space.lg,
    marginBottom: space.sm,
    borderWidth: 1,
    borderColor: color.border,
  },
  cardHeader: {
    flexDirection: 'column',
    gap: space.md,
  },
  cardContent: {
    flexDirection: 'row',
    gap: space.sm,
    alignItems: 'flex-start',
  },
  itemIcon: {
    fontSize: 22,
  },
  itemTitle: {
    ...typography.h4,
    color: color.text,
    marginBottom: space.xs / 2,
  },
  itemBody: {
    ...typography.bodySm,
    color: color.textMuted,
    lineHeight: 22,
  },
  actions: {
    flexDirection: 'row',
    gap: space.md,
    justifyContent: 'flex-end',
  },
});
```

#### **Utilisation :**
```tsx
// Dans app/recommendations/index.tsx :
import RecommendationGroup from '@/components/RecommendationGroup';

<ScrollView>
  <RecommendationGroup
    title="Activités"
    icon="🎯"
    items={[
      { icon: '📚', title: 'Lecture', body: 'Idéal pour stimuler votre intellect...' },
      { icon: '🧘', title: 'Yoga', body: 'Parfait pour équilibrer vos énergies...' },
    ]}
  />
  
  <RecommendationGroup
    title="Conseils"
    icon="💡"
    items={[
      { icon: '🌱', title: 'Croissance', body: 'Concentrez-vous sur votre développement personnel...' },
    ]}
  />
</ScrollView>
```

---

## 📊 **MÉTRIQUES ESTIMÉES (Sprint 14)**

| Module | Lignes à modifier | Temps estimé | Priorité |
|--------|------------------|--------------|----------|
| Thème Natal | ~100 | 2h | Haute |
| Compatibilité | ~50 | 1h | Moyenne |
| Horoscope | ~80 | 1.5h | Moyenne |
| Recommendations | ~150 (nouveau) | 2h | Basse |
| **TOTAL** | **~380** | **6.5h** | - |

---

## 🚀 **ORDRE D'IMPLÉMENTATION RECOMMANDÉ**

1. **Thème Natal** (plus visible, plus utilisé)
2. **Horoscope** (feature IA, haute valeur)
3. **Compatibilité** (déjà bien, petits ajustements)
4. **Recommendations** (nouveau composant, peut attendre)

---

## ✅ **CHECKLIST SPRINT 14**

### **Avant de commencer :**
- [ ] Lire ce document en entier
- [ ] Créer une branche `feat/audit-ux-suite`
- [ ] Backup des fichiers actuels

### **Pendant :**
- [ ] Implémenter Thème Natal (2h)
- [ ] Tester sur device réel
- [ ] Commit + push
- [ ] Implémenter Horoscope (1.5h)
- [ ] Tester sur device réel
- [ ] Commit + push
- [ ] Implémenter Compatibilité (1h)
- [ ] Tester sur device réel
- [ ] Commit + push
- [ ] (Optionnel) Implémenter Recommendations (2h)

### **Après :**
- [ ] Tests E2E complets
- [ ] Merge dans `main`
- [ ] Mise à jour `AUDIT_UX_COMPLETE.md`
- [ ] Créer `SPRINT14_COMPLETE.md`

---

**Auteur :** Cursor AI (Claude Sonnet 4.5)  
**Date :** 10 novembre 2025  
**Status :** 📋 TODO Sprint 14

