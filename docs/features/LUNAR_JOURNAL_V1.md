# Feature: Journal Lunaire V1

**Status**: ✅ Implémentée (2025-12-31)

---

## Vue d'ensemble

Journal quotidien simple permettant à l'utilisateur de noter son ressenti et de le lier au contexte lunaire du jour.

### Principes
- **Une entrée par jour** : Date locale (YYYY-MM-DD) comme clé unique
- **Texte libre** : Pas de limite strict (5000 caractères max)
- **Pas d'analyse automatique** : Simple stockage, pas d'IA
- **UX rassurante** : Pas de pression, écriture optionnelle
- **Contexte lunaire** : Phase + signe sauvegardés avec chaque entrée

---

## Choix technique : AsyncStorage

### Pourquoi AsyncStorage ?

✅ **Avantages** :
- Déjà utilisé dans le projet (cohérence)
- Simplicité : Pas de migration schema, pas de SQL
- Performance suffisante pour < 1000 entrées (~3 ans d'usage quotidien)
- Sérialisation JSON native
- Accès O(1) par date (key-value direct)
- Zero config, zero dépendance supplémentaire

❌ **SQLite serait overkill** :
- Requiert `expo-sqlite` (nouvelle dépendance)
- Migrations schema complexes
- Overhead pour simple key-value storage
- Queries inutiles (pas de search fulltext, pas de relations)

### Structure AsyncStorage

```typescript
// Clé par date (O(1) lookup)
journal_entry_2025-12-31 → {
  date: "2025-12-31",
  text: "Mon ressenti...",
  createdAt: 1735660800000,
  updatedAt: 1735660800000,
  moonContext: {
    phase: "Full Moon",
    sign: "Scorpio"
  }
}

// Pas d'index global (Phase 2 optionnel)
// getAllJournalEntries() scanne toutes les clés avec prefix
```

---

## Architecture

### Fichiers créés

```
apps/mobile/
├── types/journal.ts                   # Types (JournalEntry, CreatePayload, etc.)
├── services/journalService.ts         # CRUD AsyncStorage (6 fonctions)
├── components/JournalEntryModal.tsx   # Modal d'édition (full screen)
└── __tests__/journalService.test.ts   # Tests unitaires (11 tests, 100% pass)
```

### Fichiers modifiés

```
apps/mobile/
├── components/DailyRitualCard.tsx     # +bouton "Noter mon ressenti"
└── i18n/
    ├── fr.json                        # +11 clés journal
    └── en.json                        # +11 clés journal
```

---

## Modèle de données

### Type: JournalEntry

```typescript
interface JournalEntry {
  date: string; // YYYY-MM-DD (date locale)
  text: string; // Texte libre utilisateur
  createdAt: number; // Timestamp création
  updatedAt: number; // Timestamp dernière modif

  // Contexte lunaire (snapshot du jour)
  moonContext: {
    phase: MoonPhase; // "New Moon", "Full Moon", etc.
    sign: string; // "Aquarius", "Scorpio", etc.
  };
}
```

### Payload création/mise à jour

```typescript
interface CreateJournalEntryPayload {
  date: string; // YYYY-MM-DD
  text: string;
  moonContext: {
    phase: MoonPhase;
    sign: string;
  };
}
```

---

## Service CRUD

### Fonctions disponibles

#### 1. `getJournalEntry(date: string)`
```typescript
const result = await getJournalEntry('2025-12-31');
// → { exists: true, entry: JournalEntry } | { exists: false, entry: null }
```

#### 2. `saveJournalEntry(payload: CreateJournalEntryPayload)`
```typescript
const entry = await saveJournalEntry({
  date: '2025-12-31',
  text: 'Mon ressenti aujourd\'hui...',
  moonContext: { phase: 'Full Moon', sign: 'Scorpio' }
});
// → JournalEntry (créé ou mis à jour)
```

**Logique** :
- Si entrée existe → Met à jour `text` et `updatedAt`, préserve `createdAt`
- Si nouvelle → Crée avec `createdAt = updatedAt = now`

#### 3. `deleteJournalEntry(date: string)`
```typescript
await deleteJournalEntry('2025-12-31');
// → Supprime l'entrée AsyncStorage
```

#### 4. `hasJournalEntry(date: string)`
```typescript
const exists = await hasJournalEntry('2025-12-31');
// → boolean
```

#### 5. `getAllJournalEntries()` (Phase 2)
```typescript
const entries = await getAllJournalEntries();
// → JournalEntry[] (triées par date DESC)
```

**Performance** :
- Scanne toutes les clés AsyncStorage avec prefix `journal_entry_`
- Acceptable pour < 1000 entrées
- Utilise `multiGet` pour batch read

#### 6. `getJournalEntriesCount()`
```typescript
const count = await getJournalEntriesCount();
// → number
```

---

## UI : Modal d'édition

### JournalEntryModal

**Composant** : Modal full-screen avec KeyboardAvoidingView

**Props** :
```typescript
interface JournalEntryModalProps {
  visible: boolean;
  onClose: () => void;
  date?: string; // Défaut: aujourd'hui
  moonContext: {
    phase: MoonPhase;
    sign: string;
  };
}
```

**Features** :
- TextInput multiline avec autoFocus (si nouvelle entrée)
- Header sticky avec boutons Cancel / Save
- Badge contexte lunaire (phase + signe)
- Character count (`5000 caractères`)
- Bouton Delete (si entrée existante)
- Confirmation Alert avant suppression
- Feedback Toast après save/delete

**États** :
1. **Loading** : Chargement entrée existante
2. **Nouvelle** : TextInput vide, autoFocus
3. **Édition** : TextInput pré-rempli
4. **Saving** : ActivityIndicator sur bouton Save
5. **Deleted** : Alert + fermeture modal

---

## Intégration : DailyRitualCard

### Bouton journal

**Placement** : Entre guidance et CTA "Voir le climat lunaire"

**États visuels** :

#### Pas d'entrée aujourd'hui
```
┌─────────────────────────────────────┐
│  Noter mon ressenti                 │  ← Violet, border accent
└─────────────────────────────────────┘
```
- Background: `rgba(183, 148, 246, 0.15)`
- Border: `rgba(183, 148, 246, 0.3)`
- Color: `colors.accent`

#### Déjà écrit aujourd'hui
```
┌─────────────────────────────────────┐
│  ✓ Déjà noté                        │  ← Vert, border success
└─────────────────────────────────────┘
```
- Background: `rgba(74, 222, 128, 0.1)`
- Border: `rgba(74, 222, 128, 0.3)`
- Color: `colors.success`

**Logique** :
- Au mount : `checkJournalEntry()` via `hasJournalEntry(today)`
- Au close modal : Re-check pour refresh état bouton
- Pas de polling, update manuel uniquement

---

## i18n

### Clés FR (11 nouvelles)

```json
{
  "ritualCard": {
    "journalPrompt": "Noter mon ressenti",
    "journalEdited": "✓ Déjà noté"
  },
  "journal": {
    "title": "Journal Lunaire",
    "entryTitle": "Comment vous sentez-vous aujourd'hui ?",
    "placeholder": "Notez votre ressenti, vos observations, ce qui vous marque aujourd'hui...",
    "save": "Enregistrer",
    "delete": "Supprimer",
    "cancel": "Annuler",
    "saved": "Entrée enregistrée",
    "deleted": "Entrée supprimée",
    "moonContext": "{{phase}} en {{sign}}",
    "emptyState": "Aucune note pour aujourd'hui",
    "deleteConfirm": "Supprimer cette entrée ?",
    "characterCount": "{{count}} caractères",
    "maxLength": "Maximum {{max}} caractères"
  }
}
```

### Clés EN (11 équivalentes)
Traductions anglaises avec même interpolation.

---

## Tests

### Tests unitaires (__tests__/journalService.test.ts)

✅ **11 tests, 100% pass**

**Couverture** :
- `getJournalEntry()` → 2 tests (existe / n'existe pas)
- `saveJournalEntry()` → 2 tests (create / update)
- `deleteJournalEntry()` → 1 test
- `hasJournalEntry()` → 2 tests (true / false)
- `getAllJournalEntries()` → 2 tests (empty / sorted)
- `getJournalEntriesCount()` → 2 tests (0 / count)

**Mocks** :
- AsyncStorage mocké avec Jest
- Tests unitaires purs (pas de side effects)

### Validation TypeScript
```bash
npm run lint
# ✅ 0 errors
```

### Validation i18n
```bash
npm run check:i18n
# ✅ 127 keys FR, 127 keys EN (100% parity)
```

---

## UX Flow

### Première utilisation

1. User voit carte "Aujourd'hui" sur Home
2. Bouton "Noter mon ressenti" (violet)
3. Tap → Modal full-screen s'ouvre
4. User écrit texte libre
5. Tap "Enregistrer" → Alert "✓ Entrée enregistrée"
6. Modal se ferme
7. Bouton devient "✓ Déjà noté" (vert)

### Modification entrée existante

1. Tap "✓ Déjà noté" (vert)
2. Modal s'ouvre avec texte pré-rempli
3. User modifie texte
4. Tap "Enregistrer" → `updatedAt` mis à jour
5. Ou tap "Supprimer" → Confirmation → Suppression

### Consultation ancienne entrée (Phase 2)

Future feature : Timeline des entrées passées.

---

## Performance

### Stockage
- **AsyncStorage** : Key-value store natif
- **Taille moyenne entrée** : ~500 octets (texte 300 chars + metadata)
- **Capacité** : 1000 entrées = ~500 KB (négligeable)

### Lecture/Écriture
- **getJournalEntry()** : O(1) (direct key lookup)
- **saveJournalEntry()** : O(1) (setItem)
- **getAllJournalEntries()** : O(n) où n = nombre total de clés AsyncStorage
  - Acceptable si < 1000 entrées
  - Utilise `multiGet` (batch read optimisé)

### Animations
- Modal : `animationType="slide"` native
- Pas d'animations custom (perf optimale)

---

## Limitations connues (Phase 1)

1. **Pas de liste historique** : Phase 2
   - User ne peut consulter qu'aujourd'hui
   - `getAllJournalEntries()` existe mais pas d'UI

2. **Pas de synchronisation cloud** : AsyncStorage local uniquement
   - Perte de données si désinstallation
   - Pas de backup automatique

3. **Pas de statistiques** : Phase 2
   - Nombre d'entrées total
   - Corrélations phase lunaire / sentiment

4. **Pas de recherche** : Phase 2
   - Fulltext search impossible avec AsyncStorage
   - Migration SQLite si besoin

---

## Roadmap Phase 2

### v2.1 : Timeline des entrées
- Écran `/journal/history`
- Liste scrollable par date DESC
- Card par entrée avec preview texte (3 lignes)
- Tap → Ouvre modal édition

### v2.2 : Statistiques
- Nombre total d'entrées
- Streak (jours consécutifs)
- Distribution par phase lunaire
- Émotions les plus fréquentes (tags optionnels)

### v2.3 : Export
- Export CSV (date, texte, phase, signe)
- Export JSON (backup complet)
- Partage iOS/Android via share sheet

### v2.4 : Synchronisation cloud (optionnel)
- Backup automatique Firebase/Supabase
- Sync multi-device
- Encryption côté client

---

## Metrics de succès (post-lancement)

### Primaires
1. **Taux d'adoption** : 40% des users écrivent au moins 1 entrée
2. **Fréquence d'écriture** : 20% écrivent 3j/semaine ou plus
3. **Rétention** : +15% rétention J+30 pour users avec journal

### Secondaires
4. **Longueur moyenne** : 200-400 caractères (sweet spot)
5. **Édition** : 10% des entrées sont modifiées après création
6. **Suppression** : < 5% des entrées supprimées

---

## Notes techniques

### Dépendances
- `@react-native-async-storage/async-storage` : Déjà installé
- `react-i18next` : Déjà installé
- Aucune nouvelle dépendance

### Compatibilité
- iOS ✅
- Android ✅
- Web ⚠️ (AsyncStorage → localStorage, OK)

### Sécurité
- Données stockées localement (pas de cloud)
- Pas de données sensibles médicales/financières
- Pas de tracking tiers

### Accessibilité
- TextInput accessible via screenreader
- Labels i18n clairs
- Tap targets 44px minimum

---

**Implémentation complète, production-ready.**
**AsyncStorage robuste, CRUD testé, UX rassurante.**
**Code prêt à être branché, zero breaking change.**
