# 📋 SPRINT 15 - AUDIT UX MODULES RESTANTS

**Date :** 10 novembre 2025  
**Status :** En attente tests utilisateur  
**Modules :** 6 (Home amélioré, Cycle saisie/résultat, Journal liste/création, Transverses)

---

## 🎯 **OBJECTIF SPRINT 15**

Finaliser l'audit UX sur tous les modules opérationnels + améliorations transverses (thème, A11y, perfs, analytics).

---

## 📦 **MODULES À IMPLÉMENTER**

### 🏠 **MODULE 1/6 : ACCUEIL (Home amélioré)**

#### 🔍 **Audit rapide**

**✅ Points forts :**
- Cartes "Mon cycle / Humeur / Astro du jour" : claires et lisibles
- Hiérarchie visuelle cohérente

**⚠️ Points à améliorer :**
1. Header "AUJOURD'HUI" prend une ligne entière → perte de place
2. Bouton "Ouvrir le journal" manque de hiérarchie (ressemble à un link)
3. L'aperçu "Astro du jour" répète l'info du header → densité texte forte
4. Scrolling : fin de page abrupte (pas assez de padding bas)

---

#### 🧠 **Prompt Cursor — `app/(tabs)/home.tsx`**

**Objectifs UI/UX Accueil :**

1️⃣ **Remplacer "AUJOURD'HUI" par un chip compact :**
```tsx
import { Chip } from '@/components/ui';

<Chip icon="calendar" variant="default">
  Aujourd'hui
</Chip>
```

2️⃣ **Harmoniser les 3 cartes principales :**
```tsx
// Dans SectionCard ou style commun :
const cardStyle = {
  minHeight: 120,
  padding: space.lg,
  borderRadius: radius.lg,
  ...shadow.md,
};

// Titre
<Text style={{ ...typography.h4, fontWeight: '600' }}>
  {title}
</Text>

// Sous-titre
<Text style={{ ...typography.bodySm, color: color.textMuted }}>
  {subtitle}
</Text>
```

3️⃣ **CTA "Ouvrir le journal" :**
```tsx
import { Button } from '@/components/ui';

<Button 
  size="md" 
  variant="primary" 
  leftIcon="book-open" 
  label="Ouvrir le journal"
  onPress={openJournal}
/>
```

4️⃣ **Carte "Astro du jour" :**
```tsx
<SectionCard
  title={`Lune en ${moonSign}`}
  subtitle={mantra}
  footerLink={{
    label: "Voir l'analyse",
    onPress: () => router.push('/horoscope')
  }}
/>

// Sous-titre avec ellipsis :
<Text 
  numberOfLines={1} 
  ellipsizeMode="tail"
  style={styles.subtitle}
>
  {mantra}
</Text>
```

5️⃣ **ScrollView avec padding bottom :**
```tsx
import { useSafeAreaInsets } from 'react-native-safe-area-context';

const insets = useSafeAreaInsets();

<ScrollView
  contentContainerStyle={{
    paddingBottom: insets.bottom + 32,
  }}
>
```

6️⃣ **Animation à l'apparition des cartes :**
```tsx
import Animated, { FadeInUp } from 'react-native-reanimated';

<Animated.View entering={FadeInUp.duration(300).springify()}>
  <CycleCard {...props} />
</Animated.View>

<Animated.View entering={FadeInUp.duration(300).delay(100).springify()}>
  <MoodCard {...props} />
</Animated.View>

<Animated.View entering={FadeInUp.duration(300).delay(200).springify()}>
  <AstroCard {...props} />
</Animated.View>
```

**Note :** Nécessite `react-native-reanimated` (déjà installé si Expo SDK 49+)

---

### 🌙 **MODULE 2/6 : CYCLE & ASTROLOGIE — SAISIE**

#### 🔍 **Audit rapide**

**✅ Points forts :**
- Bandeau "Information importante" (non médical) bien placé
- Sélection de phase + humeur : propre et intuitive

**⚠️ Points à améliorer :**
1. Champ "Jour du cycle (1–35)" : pas borné, pas de clavier numérique
2. Cartes de phase dépassent sur petits écrans (break en 2 lignes)
3. Manque d'état "profil astral chargé" si thème natal n'existe pas
4. CTA "Analyser mon cycle" doit être désactivé si champs invalides

---

#### 🧠 **Prompt Cursor — `app/cycle/index.tsx` (ou similaire)**

**Améliorations saisie cycle :**

1️⃣ **"Jour du cycle" avec validation :**
```tsx
const [day, setDay] = useState('');
const [dayError, setDayError] = useState('');

<TextInput
  keyboardType="number-pad"
  maxLength={2}
  value={day}
  onChangeText={(value) => {
    setDay(value.replace(/[^0-9]/g, ''));
    
    const num = parseInt(value);
    if (value && (num < 1 || num > 35)) {
      setDayError('Entre 1 et 35');
    } else {
      setDayError('');
    }
  }}
  style={[styles.input, dayError && styles.inputError]}
/>

{dayError && (
  <Text style={styles.helperTextError}>{dayError}</Text>
)}
```

2️⃣ **Cartes "Phase du cycle" responsive :**
```tsx
import { useWindowDimensions } from 'react-native';

const { width } = useWindowDimensions();
const numColumns = width < 360 ? 2 : 4; // 2 colonnes sur petits écrans

<View style={{
  flexDirection: 'row',
  flexWrap: 'wrap',
  gap: space.sm,
}}>
  {PHASES.map((phase) => (
    <TouchableOpacity
      key={phase.id}
      style={[
        styles.phaseCard,
        {
          width: `${100 / numColumns - 2}%`,
          minHeight: 90,
          justifyContent: 'center',
        },
        selectedPhase === phase.id && styles.phaseCardActive
      ]}
      onPress={() => setSelectedPhase(phase.id)}
    >
      <Text style={styles.phaseEmoji}>{phase.emoji}</Text>
      <Text style={styles.phaseName}>{phase.name}</Text>
    </TouchableOpacity>
  ))}
</View>
```

3️⃣ **Humeurs avec toggle + "Autre..." :**
```tsx
const [selectedMood, setSelectedMood] = useState(null);
const [customMood, setCustomMood] = useState('');
const [showCustomMoodModal, setShowCustomMoodModal] = useState(false);

<View style={styles.moodsGrid}>
  {MOODS.map((mood) => (
    <TouchableOpacity
      key={mood.id}
      style={[
        styles.moodChip,
        selectedMood === mood.id && styles.moodChipActive
      ]}
      onPress={() => setSelectedMood(mood.id)}
    >
      <Text>{mood.emoji} {mood.label}</Text>
    </TouchableOpacity>
  ))}
  
  <TouchableOpacity
    style={styles.moodChip}
    onPress={() => setShowCustomMoodModal(true)}
  >
    <Text>Autre...</Text>
  </TouchableOpacity>
</View>

{/* Modal pour custom mood */}
<Modal visible={showCustomMoodModal} transparent>
  <View style={styles.modalOverlay}>
    <View style={styles.modalContent}>
      <Text style={styles.modalTitle}>Quelle humeur ?</Text>
      <TextInput
        placeholder="Ex: Sereine"
        value={customMood}
        onChangeText={setCustomMood}
        style={styles.modalInput}
        autoFocus
      />
      <Button 
        label="Valider" 
        onPress={() => {
          setSelectedMood('custom');
          setShowCustomMoodModal(false);
        }}
      />
    </View>
  </View>
</Modal>
```

4️⃣ **Profil astral check :**
```tsx
const { hasNatal } = useProfileStore();

{!hasNatal() && (
  <AlertBanner 
    variant="info"
    title="Thème natal recommandé"
    icon="information-circle"
  >
    Pour une analyse plus précise, calcule ton thème natal complet.
    <TouchableOpacity 
      onPress={() => router.push('/natal-chart')}
      style={{ marginTop: 8 }}
    >
      <Text style={{ color: color.brand, fontWeight: '600' }}>
        Calculer mon thème →
      </Text>
    </TouchableOpacity>
  </AlertBanner>
)}
```

5️⃣ **CTA avec validation :**
```tsx
const [isAnalyzing, setIsAnalyzing] = useState(false);

const isValidForm = () => {
  const dayNum = parseInt(day);
  return (
    selectedPhase &&
    selectedMood &&
    day &&
    dayNum >= 1 &&
    dayNum <= 35 &&
    !dayError
  );
};

<Button
  label="Analyser mon cycle"
  disabled={!isValidForm() || isAnalyzing}
  loading={isAnalyzing}
  onPress={async () => {
    haptics.medium();
    Analytics.track('cycle_analyze_clicked', {
      phase: selectedPhase,
      mood: selectedMood,
      day: parseInt(day),
    });
    
    setIsAnalyzing(true);
    try {
      await analyzeCoordinates();
      router.push('/cycle/result');
    } finally {
      setIsAnalyzing(false);
    }
  }}
/>
```

6️⃣ **Scroll + KeyboardAvoidingView :**
```tsx
<KeyboardAvoidingView
  behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
  style={{ flex: 1 }}
>
  <ScrollView
    contentContainerStyle={{
      paddingBottom: insets.bottom + 32,
    }}
    keyboardShouldPersistTaps="handled"
  >
    {/* Form content */}
  </ScrollView>
</KeyboardAvoidingView>
```

---

### 🌕 **MODULE 3/6 : CYCLE & ASTROLOGIE — RÉSULTAT**

#### 🔍 **Audit rapide**

**✅ Points forts :**
- Carte "Énergie cosmique" + barre : top
- Sections "Transits du jour", "Activités recommandées", "Conseils" : faciles à lire

**⚠️ Points à améliorer :**
1. Récap ("Lune en Vierge", "Aspect") trop bas niveau hiérarchie
2. Pas de CTA "Ajouter au journal" / "Partager"
3. Long scroll : prévoir sommaire sticky optionnel

---

#### 🧠 **Prompt Cursor — `app/cycle/result.tsx`**

**Refonte résultat cycle :**

1️⃣ **En-tête avec phase + énergie :**
```tsx
<View style={styles.header}>
  <Text style={styles.phaseTitle}>{currentPhase.name}</Text>
  <Text style={styles.phaseSubtitle}>
    Jour {dayOfCycle} • Phase {currentPhase.name}
  </Text>
  
  {/* Barre d'énergie */}
  <View style={styles.energyBarContainer}>
    <View style={styles.energyBar}>
      <View 
        style={[
          styles.energyBarFill,
          { width: `${energyPercent}%` }
        ]}
      />
    </View>
    <Text style={styles.energyPercent}>{energyPercent}%</Text>
  </View>
</View>
```

2️⃣ **Bloc "Transits du jour" avec pills :**
```tsx
import { Tag } from '@/components/ui';

<View style={styles.transitsSection}>
  <Text style={styles.sectionTitle}>Transits du jour</Text>
  
  <View style={{ flexDirection: 'row', gap: 12, flexWrap: 'wrap' }}>
    <Tag 
      icon={<Ionicons name="moon" size={16} color={color.brand} />}
      label={`Lune en : ${moonSign} ${moonEmoji}`}
    />
    
    <Tag 
      icon={<Ionicons name="sparkles" size={16} color={color.info} />}
      label={`Aspect : ${aspect}`}
      variant="info"
    />
  </View>
</View>
```

3️⃣ **Groupes "Activités" et "Conseils" :**
```tsx
import RecommendationGroup from '@/components/RecommendationGroup';

<RecommendationGroup
  title="Activités recommandées"
  icon="🎯"
  items={activities}
/>

<RecommendationGroup
  title="Conseils personnalisés"
  icon="💡"
  items={advices}
/>
```

4️⃣ **Sommaire sticky (optionnel) :**
```tsx
import { useState, useRef } from 'react';

const transitsRef = useRef(null);
const activitiesRef = useRef(null);
const advicesRef = useRef(null);

const [activeTab, setActiveTab] = useState('transits');

<View style={styles.stickyTabs}>
  {['transits', 'activities', 'advices'].map((tab) => (
    <TouchableOpacity
      key={tab}
      style={[
        styles.tab,
        activeTab === tab && styles.tabActive
      ]}
      onPress={() => {
        setActiveTab(tab);
        const ref = tab === 'transits' ? transitsRef : 
                    tab === 'activities' ? activitiesRef : advicesRef;
        ref.current?.measureLayout(
          scrollViewRef.current,
          (x, y) => {
            scrollViewRef.current?.scrollTo({ y, animated: true });
          }
        );
      }}
    >
      <Text style={styles.tabText}>
        {tab === 'transits' ? 'Transits' : 
         tab === 'activities' ? 'Activités' : 'Conseils'}
      </Text>
    </TouchableOpacity>
  ))}
</View>
```

5️⃣ **Footer avec timestamp + CTA :**
```tsx
<View style={styles.footer}>
  <Text style={styles.timestamp}>
    Généré à {new Date().toLocaleTimeString('fr-FR', { 
      hour: '2-digit', 
      minute: '2-digit' 
    })}
  </Text>
  
  <Button
    variant="outline"
    label="Nouvelle analyse"
    onPress={() => router.back()}
  />
</View>
```

6️⃣ **Analytics :**
```tsx
useEffect(() => {
  Analytics.track('cycle_result_viewed', {
    phase: currentPhase.name,
    energy: energyPercent,
    moonSign: moonSign,
    hasNatal: hasNatal(),
  });
}, []);
```

---

### 📓 **MODULE 4/6 : JOURNAL — LISTE**

#### 🔍 **Audit rapide**

**✅ Points forts :**
- Carte "Vos statistiques" simple et efficace
- Items d'entrées lisibles (emoji humeur + titre + date)

**⚠️ Points à améliorer :**
1. Bouton "+" flotte sans label → mieux : FAB + label
2. Badge "Nouvelle lune" joli mais contraste insuffisant
3. Pas de recherche / filtre (période, humeur)

---

#### 🧠 **Prompt Cursor — `app/journal/index.tsx`**

**Journal liste :**

1️⃣ **FAB avec label :**
```tsx
// components/ui/FAB.tsx à créer
interface FABProps {
  icon: string;
  label: string;
  onPress: () => void;
  position?: 'bottom-right' | 'bottom-center';
}

export function FAB({ icon, label, onPress, position = 'bottom-right' }: FABProps) {
  const insets = useSafeAreaInsets();
  
  return (
    <TouchableOpacity
      style={[
        styles.fab,
        position === 'bottom-right' && styles.fabRight,
        position === 'bottom-center' && styles.fabCenter,
        { bottom: insets.bottom + 16 }
      ]}
      onPress={onPress}
      activeOpacity={0.8}
    >
      <LinearGradient colors={[color.brand, color.brandHover]} style={styles.fabGradient}>
        <Ionicons name={icon} size={20} color="white" />
        <Text style={styles.fabLabel}>{label}</Text>
      </LinearGradient>
    </TouchableOpacity>
  );
}

// Utilisation :
<FAB
  icon="add"
  label="Nouvelle entrée"
  onPress={() => router.push('/journal/new')}
/>
```

2️⃣ **Cartes d'entrées améliorées :**
```tsx
<TouchableOpacity 
  style={styles.entryCard}
  onPress={() => router.push(`/journal/${entry.id}`)}
  accessibilityRole="button"
  accessibilityLabel={`Entrée – ${mood.label} – ${formatDate(entry.createdAt)}`}
>
  <View style={styles.entryContent}>
    {/* Left: Emoji */}
    <Text style={styles.entryEmoji}>{mood.emoji}</Text>
    
    {/* Center: Info */}
    <View style={styles.entryInfo}>
      <Text style={styles.entryTitle}>{mood.label}</Text>
      <Text style={styles.entryDate}>{formatDate(entry.createdAt)}</Text>
      
      {/* Footer chips */}
      {entry.moonPhase && (
        <View style={styles.entryChips}>
          <Tag 
            icon={<Ionicons name="moon" size={12} />}
            label={entry.moonPhase}
            variant="default"
          />
        </View>
      )}
    </View>
    
    {/* Right: Chevron */}
    <Ionicons name="chevron-forward" size={20} color={color.textMuted} />
  </View>
</TouchableOpacity>
```

3️⃣ **Filtres :**
```tsx
const [period, setPeriod] = useState('all'); // '7d', '30d', 'all'
const [moodFilter, setMoodFilter] = useState(null);
const [searchQuery, setSearchQuery] = useState('');

<View style={styles.filtersBar}>
  {/* Période */}
  <View style={styles.periodChips}>
    {['7j', '30j', 'Tout'].map((label, idx) => {
      const value = ['7d', '30d', 'all'][idx];
      return (
        <TouchableOpacity
          key={value}
          style={[
            styles.chip,
            period === value && styles.chipActive
          ]}
          onPress={() => setPeriod(value)}
        >
          <Text style={styles.chipText}>{label}</Text>
        </TouchableOpacity>
      );
    })}
  </View>
  
  {/* Humeur dropdown */}
  <TouchableOpacity 
    style={styles.filterButton}
    onPress={() => setShowMoodPicker(true)}
  >
    <Ionicons name="filter" size={16} color={color.brand} />
    <Text>Humeur</Text>
  </TouchableOpacity>
  
  {/* Search */}
  <TextInput
    placeholder="Rechercher..."
    value={searchQuery}
    onChangeText={setSearchQuery}
    style={styles.searchInput}
  />
</View>

// Filtrage :
const filteredEntries = useMemo(() => {
  let result = entries;
  
  if (period !== 'all') {
    const days = period === '7d' ? 7 : 30;
    const cutoff = new Date();
    cutoff.setDate(cutoff.getDate() - days);
    result = result.filter(e => new Date(e.createdAt) >= cutoff);
  }
  
  if (moodFilter) {
    result = result.filter(e => e.mood === moodFilter);
  }
  
  if (searchQuery) {
    result = result.filter(e => 
      e.note?.toLowerCase().includes(searchQuery.toLowerCase())
    );
  }
  
  return result;
}, [entries, period, moodFilter, searchQuery]);
```

4️⃣ **Swipe actions (nécessite gesture-handler) :**
```tsx
import { Swipeable } from 'react-native-gesture-handler';

<Swipeable
  renderRightActions={() => (
    <TouchableOpacity
      style={styles.deleteAction}
      onPress={() => handleDelete(entry.id)}
    >
      <Ionicons name="trash" size={24} color="white" />
      <Text style={styles.deleteText}>Supprimer</Text>
    </TouchableOpacity>
  )}
  renderLeftActions={() => (
    <TouchableOpacity
      style={styles.editAction}
      onPress={() => router.push(`/journal/${entry.id}/edit`)}
    >
      <Ionicons name="pencil" size={24} color="white" />
      <Text style={styles.editText}>Éditer</Text>
    </TouchableOpacity>
  )}
>
  <EntryCard entry={entry} />
</Swipeable>
```

5️⃣ **Padding bottom :**
```tsx
<ScrollView
  contentContainerStyle={{
    paddingBottom: insets.bottom + 80, // 80 pour le FAB
  }}
>
```

---

### 📝 **MODULE 5/6 : JOURNAL — CRÉATION / ÉDITION**

#### 🔍 **Audit rapide**

**✅ Points forts :**
- Champs (humeur, notes) cohérents avec saisie du cycle

**⚠️ Points à améliorer :**
1. Pas de save state (autosave brouillon)
2. Pas de lien direct "Préremplir depuis résultat cycle/horoscope"

---

#### 🧠 **Prompt Cursor — `app/journal/new.tsx`**

**Création d'entrée :**

1️⃣ **Props initiales via query :**
```tsx
import { useLocalSearchParams } from 'expo-router';

const params = useLocalSearchParams();

const [mood, setMood] = useState(params.mood || '');
const [note, setNote] = useState(params.note || '');
const [tags, setTags] = useState(
  params.tags ? (params.tags as string).split(',') : []
);
const [source, setSource] = useState(params.source || null);

useEffect(() => {
  // Pré-remplir depuis params
  if (params.mood) setMood(params.mood as string);
  if (params.note) setNote(params.note as string);
  if (params.tags) setTags((params.tags as string).split(','));
}, [params]);
```

2️⃣ **Autosave avec debounce :**
```tsx
import { useDebouncedCallback } from 'use-debounce';
import AsyncStorage from '@react-native-async-storage/async-storage';

const [showSavedToast, setShowSavedToast] = useState(false);

const saveDraft = useDebouncedCallback(async (data) => {
  try {
    await AsyncStorage.setItem('journal_draft', JSON.stringify(data));
    setShowSavedToast(true);
    setTimeout(() => setShowSavedToast(false), 2000);
  } catch (error) {
    console.error('Draft save error:', error);
  }
}, 1000);

useEffect(() => {
  saveDraft({ mood, note, tags, timestamp: Date.now() });
}, [mood, note, tags]);

// Charger draft au montage
useEffect(() => {
  const loadDraft = async () => {
    const draft = await AsyncStorage.getItem('journal_draft');
    if (draft && !params.mood) { // Ne pas écraser params
      const { mood, note, tags } = JSON.parse(draft);
      setMood(mood);
      setNote(note);
      setTags(tags);
    }
  };
  loadDraft();
}, []);

{/* Snackbar */}
{showSavedToast && (
  <View style={styles.snackbar}>
    <Text style={styles.snackbarText}>✓ Enregistré</Text>
  </View>
)}
```

3️⃣ **Champs du formulaire :**
```tsx
<ScrollView style={styles.form}>
  {/* Humeur (chips) */}
  <Text style={styles.label}>Humeur *</Text>
  <View style={styles.moodsGrid}>
    {MOODS.map((m) => (
      <TouchableOpacity
        key={m.id}
        style={[
          styles.moodChip,
          mood === m.id && styles.moodChipActive
        ]}
        onPress={() => setMood(m.id)}
      >
        <Text>{m.emoji}</Text>
        <Text style={styles.moodLabel}>{m.label}</Text>
      </TouchableOpacity>
    ))}
  </View>
  
  {/* Titre (optionnel) */}
  <Text style={styles.label}>Titre (optionnel)</Text>
  <TextInput
    placeholder="Ex: Belle journée"
    value={title}
    onChangeText={setTitle}
    style={styles.input}
  />
  
  {/* Notes (multiline) */}
  <Text style={styles.label}>Notes</Text>
  <TextInput
    placeholder="Écris tes pensées du jour..."
    value={note}
    onChangeText={setNote}
    multiline
    numberOfLines={6}
    style={[styles.input, { minHeight: 100, textAlignVertical: 'top' }]}
  />
  
  {/* Tags (chips) */}
  <Text style={styles.label}>Tags</Text>
  <View style={styles.tagsContainer}>
    {tags.map((tag, idx) => (
      <Tag
        key={idx}
        label={tag}
        onRemove={() => setTags(tags.filter((_, i) => i !== idx))}
      />
    ))}
    <TouchableOpacity 
      style={styles.addTagButton}
      onPress={() => setShowAddTagModal(true)}
    >
      <Ionicons name="add" size={16} />
      <Text>Ajouter</Text>
    </TouchableOpacity>
  </View>
  
  {/* Joindre recommandation */}
  {lastCycleResult && (
    <TouchableOpacity
      style={styles.attachRecoButton}
      onPress={() => setShowRecoPicker(true)}
    >
      <Ionicons name="link" size={20} color={color.brand} />
      <Text style={styles.attachRecoText}>
        Joindre une recommandation du dernier résultat
      </Text>
    </TouchableOpacity>
  )}
</ScrollView>
```

4️⃣ **CTA avec save :**
```tsx
const [isSaving, setIsSaving] = useState(false);

const handleSave = async () => {
  if (!mood) {
    Alert.alert('Humeur requise', 'Sélectionne une humeur');
    return;
  }
  
  haptics.medium();
  setIsSaving(true);
  
  try {
    await addEntry({
      mood,
      title,
      note,
      tags,
      moonPhase: moonContext.phase,
      createdAt: new Date().toISOString(),
    });
    
    // Supprimer le brouillon
    await AsyncStorage.removeItem('journal_draft');
    
    // Analytics
    Analytics.track('journal_created', {
      mood,
      hasTags: tags.length > 0,
      source: source || 'manual',
    });
    
    haptics.success();
    
    // Toast succès
    if (Platform.OS === 'android') {
      ToastAndroid.show('Entrée enregistrée !', ToastAndroid.SHORT);
    }
    
    router.replace('/journal');
  } catch (error) {
    Alert.alert('Erreur', error.message);
  } finally {
    setIsSaving(false);
  }
};

<Button
  label="Enregistrer"
  onPress={handleSave}
  loading={isSaving}
  disabled={isSaving || !mood}
/>
```

5️⃣ **Analytics :**
```tsx
useEffect(() => {
  Analytics.track('journal_new_opened', {
    source: params.source || 'manual',
    hasPrefill: !!params.mood || !!params.note,
  });
}, []);
```

---

### 🧩 **MODULE 6/6 : AMÉLIORATIONS TRANSVERSES**

#### 🎨 **1. Thème & cohérence**

**Créer `theme/scale.ts` :**
```tsx
export const spacing = {
  xs: 4,
  sm: 8,
  md: 12,
  lg: 16,
  xl: 24,
  '2xl': 32,
} as const;

export const fontSize = {
  xs: 12,
  sm: 14,
  md: 17,
  lg: 20,
  xl: 24,
} as const;

export const colors = {
  primary: '#FF4E80',
  gradient: ['#FF4E80', '#FF6BA0', '#FF8BC0'],
  surface: '#121424',
  elevated: '#181B2A',
  textMuted: '#A7AEC3',
  text: '#F6F5F9',
  border: '#2A2B3E',
} as const;
```

**Créer `components/Section.tsx` :**
```tsx
interface SectionProps {
  title: string;
  subtitle?: string;
  children: React.ReactNode;
  spacing?: 'compact' | 'normal' | 'relaxed';
}

export function Section({ 
  title, 
  subtitle, 
  children, 
  spacing = 'normal' 
}: SectionProps) {
  const spacingValue = {
    compact: 12,
    normal: 24,
    relaxed: 32,
  }[spacing];
  
  return (
    <View style={{ marginBottom: spacingValue }}>
      <Text style={styles.sectionTitle}>{title}</Text>
      {subtitle && (
        <Text style={styles.sectionSubtitle}>{subtitle}</Text>
      )}
      <View style={{ marginTop: 12 }}>
        {children}
      </View>
    </View>
  );
}
```

---

#### ♿️ **2. Accessibilité**

**Checklist A11y :**

1️⃣ **Labels sur tous les boutons :**
```tsx
<TouchableOpacity
  accessibilityRole="button"
  accessibilityLabel="Ouvrir le journal"
  accessibilityHint="Double tap pour ouvrir votre journal personnel"
>
```

2️⃣ **Taille min tappable 44x44 :**
```tsx
// Dans theme/tokens.ts
export const minTappableSize = {
  width: 44,
  height: 44,
} as const;

// Utilisation :
<TouchableOpacity
  style={[
    styles.button,
    { minWidth: 44, minHeight: 44 }
  ]}
  hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}
>
```

3️⃣ **Support Dynamic Type :**
```tsx
import { useWindowDimensions, PixelRatio } from 'react-native';

const { fontScale } = useWindowDimensions();

const scaledFontSize = (size: number) => {
  const scale = Math.min(fontScale, 1.3); // Cap à 1.3x
  return Math.round(size * scale);
};

// Utilisation :
<Text style={{ fontSize: scaledFontSize(16) }}>
  Texte adaptatif
</Text>
```

4️⃣ **Contraste WCAG AA > 4.5 :**
```tsx
// Vérifier avec outil : https://webaim.org/resources/contrastchecker/

// Exemples OK :
// - Texte blanc (#F6F5F9) sur fond sombre (#121424) → contraste > 15:1 ✅
// - Texte muted (#A7AEC3) sur fond sombre (#121424) → contraste > 7:1 ✅

// Exemples KO :
// - Texte gris clair (#64748B) sur fond (#181B2A) → contraste < 3:1 ❌
// → Remplacer par textMuted (#A7AEC3)
```

---

#### ⚡️ **3. Performance & state**

1️⃣ **Mémoïser les listes :**
```tsx
import { FlashList } from '@shopify/flash-list';

// Au lieu de ScrollView + map :
<FlashList
  data={entries}
  renderItem={({ item }) => <EntryCard entry={item} />}
  estimatedItemSize={100}
  keyExtractor={(item) => item.id}
/>
```

2️⃣ **useCallback/useMemo sur handlers lourds :**
```tsx
const handleAnalyze = useCallback(async () => {
  // ... logique lourde
}, [dependencies]);

const filteredEntries = useMemo(() => {
  return entries.filter(/* ... */);
}, [entries, filterCriteria]);
```

3️⃣ **Suspense/Lazy pour modules non critiques :**
```tsx
import { lazy, Suspense } from 'react';

const CompatibilityResult = lazy(() => import('./CompatibilityResult'));

<Suspense fallback={<Skeleton />}>
  {showResult && <CompatibilityResult />}
</Suspense>
```

4️⃣ **Précharger polices/icônes au splash :**
```tsx
// app/_layout.tsx
import * as SplashScreen from 'expo-splash-screen';
import { useFonts } from 'expo-font';

SplashScreen.preventAutoHideAsync();

export default function RootLayout() {
  const [fontsLoaded] = useFonts({
    'CustomFont': require('../assets/fonts/CustomFont.ttf'),
  });
  
  useEffect(() => {
    if (fontsLoaded) {
      SplashScreen.hideAsync();
    }
  }, [fontsLoaded]);
  
  if (!fontsLoaded) return null;
  
  return <Stack />;
}
```

---

#### 📈 **4. Analytics**

**Créer `lib/analytics.ts` amélioré :**
```tsx
import { Mixpanel } from 'mixpanel-react-native';

class Analytics {
  private mixpanel: Mixpanel | null = null;
  private userId: string | null = null;
  
  async init(token: string) {
    this.mixpanel = new Mixpanel(token);
    await this.mixpanel.init();
  }
  
  setUserId(userId: string) {
    this.userId = userId;
    this.mixpanel?.identify(userId);
  }
  
  track(event: string, properties?: Record<string, any>) {
    const enrichedProperties = {
      ...properties,
      userId: this.userId || 'anonymous',
      timestamp: new Date().toISOString(),
      platform: Platform.OS,
      appVersion: Constants.expoConfig?.version,
    };
    
    console.log('[Analytics]', event, enrichedProperties);
    this.mixpanel?.track(event, enrichedProperties);
  }
  
  // Events prédéfinis
  appOpen() {
    this.track('app_open');
  }
  
  homeView() {
    this.track('home_view');
  }
  
  natalCalculated(data: { sunSign: string; moonSign: string; ascendant: string }) {
    this.track('natal_calculated', data);
  }
  
  compatibilityAnalyzed(data: { relationType: string; score: number }) {
    this.track('compatibility_analyzed', data);
  }
  
  cycleAnalyzeClicked(data: { phase: string; mood: string; day: number }) {
    this.track('cycle_analyze_clicked', data);
  }
  
  cycleResultViewed(data: { phase: string; energy: number; moonSign: string }) {
    this.track('cycle_result_viewed', data);
  }
  
  journalCreated(data: { mood: string; hasTags: boolean; source: string }) {
    this.track('journal_created', data);
  }
}

export default new Analytics();
```

**Utilisation :**
```tsx
// app/_layout.tsx
import Analytics from '@/lib/analytics';
import Constants from 'expo-constants';

useEffect(() => {
  Analytics.init(Constants.expoConfig?.extra?.mixpanelToken);
  Analytics.appOpen();
}, []);

// Dans les screens :
useEffect(() => {
  Analytics.homeView();
}, []);

// Lors d'actions :
Analytics.natalCalculated({
  sunSign: 'Scorpion',
  moonSign: 'Sagittaire',
  ascendant: 'Poissons',
});
```

---

## 📊 **MÉTRIQUES ESTIMÉES SPRINT 15**

| Module | Lignes | Temps | Priorité |
|--------|--------|-------|----------|
| Home amélioré | ~80 | 1.5h | Haute |
| Cycle saisie | ~150 | 2h | Haute |
| Cycle résultat | ~120 | 2h | Haute |
| Journal liste | ~100 | 1.5h | Moyenne |
| Journal création | ~130 | 2h | Moyenne |
| Transverses | ~200 | 3h | Basse |
| **TOTAL** | **~780** | **12h** | - |

---

## 🚀 **ORDRE D'IMPLÉMENTATION RECOMMANDÉ**

1. **Transverses** (thème + A11y) → Fondations pour les autres modules
2. **Home amélioré** → Haute visibilité
3. **Cycle saisie** → Bloquant pour résultat
4. **Cycle résultat** → Compléter le flow
5. **Journal liste** → État actuel OK, peut attendre
6. **Journal création** → État actuel OK, peut attendre

---

## ✅ **CHECKLIST SPRINT 15**

### **Avant :**
- [ ] Installer `react-native-reanimated` (si pas déjà fait)
- [ ] Installer `@shopify/flash-list` (optionnel)
- [ ] Installer `use-debounce` (npm i use-debounce)
- [ ] Créer branche `feat/sprint15-ux`

### **Pendant :**
- [ ] Implémenter Transverses (thème + A11y + perfs + analytics)
- [ ] Implémenter Home amélioré
- [ ] Implémenter Cycle saisie
- [ ] Implémenter Cycle résultat
- [ ] (Optionnel) Implémenter Journal liste
- [ ] (Optionnel) Implémenter Journal création
- [ ] Tester sur device réel
- [ ] Commits réguliers

### **Après :**
- [ ] Tests E2E complets
- [ ] Vérifier analytics dans Mixpanel
- [ ] Merge dans `main`
- [ ] Mise à jour `SPRINT15_COMPLETE.md`

---

**Auteur :** Cursor AI (Claude Sonnet 4.5)  
**Date :** 10 novembre 2025  
**Status :** 📋 TODO Sprint 15 (en attente tests user Sprint 13)

