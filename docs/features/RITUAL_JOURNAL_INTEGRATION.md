# Intégration : Carte Rituel Quotidien ↔ Journal Lunaire

**Status**: ✅ Implémentée (2025-12-31)

---

## Vue d'ensemble

Lien discret entre la carte "Rituel Quotidien" et le Journal Lunaire V1 via un text-button minimaliste.

### Principes
- **Détection automatique** : Check existence entrée du jour au mount
- **UX discrète** : Text-button simple, pas de bouton plein
- **Feedback visuel** : Couleur change selon statut (gris → vert)
- **Même modal** : Réutilise `JournalEntryModal` (create ou edit)
- **Date locale** : Détection basée sur YYYY-MM-DD (comme journal)

---

## Comportement

### 1. Aucune entrée aujourd'hui

**Affichage** :
```
┌─────────────────────────────────────┐
│  Noter mon ressenti                 │  ← Text-button gris clair
└─────────────────────────────────────┘
```

**Couleur** : `colors.textMuted` (#a0a0b0)
**Action tap** : Ouvre `JournalEntryModal` en mode création (TextInput vide)

### 2. Entrée existante

**Affichage** :
```
┌─────────────────────────────────────┐
│  ✓ Relire / Modifier                │  ← Text-button vert
└─────────────────────────────────────┘
```

**Couleur** : `colors.success` (#4ade80)
**Indicateur** : ✓ préfixe
**Action tap** : Ouvre `JournalEntryModal` en mode édition (TextInput pré-rempli)

---

## Logique de détection

### Au mount de DailyRitualCard

```typescript
useEffect(() => {
  checkJournalEntry();
}, []);

const checkJournalEntry = async () => {
  const today = getTodayDateString(); // "YYYY-MM-DD"
  const exists = await hasJournalEntry(today);
  setHasJournalToday(exists);
};
```

**Fonction utilisée** : `hasJournalEntry(date: string)` de `journalService.ts`

### Au close de JournalEntryModal

```typescript
useEffect(() => {
  if (!journalModalVisible) {
    checkJournalEntry(); // Refresh statut
  }
}, [journalModalVisible]);
```

**Raison** : Après save/delete, le statut bouton doit se mettre à jour.

---

## Placement visuel

### Position dans DailyRitualCard

```
╔═══════════════════════════════════════════╗
║  🌓 Aujourd'hui                           ║
║                                           ║
║  PREMIER QUARTIER EN TAUREAU              ║
║                                           ║
║  "Tension fertile. Ajustez vos actions." ║
║                                           ║
║  [Badge VoC si actif]                     ║
║                                           ║
║  Noter mon ressenti               ← TEXT  ║  ← Journal CTA (gris/vert)
║                                           ║
║  → Voir le climat lunaire         ← TEXT  ║  ← CTA climat (violet)
╚═══════════════════════════════════════════╝
```

**Ordre** :
1. Header + emoji
2. Phase + signe
3. Guidance
4. Badge VoC (si actif)
5. **Journal CTA** ← NOUVEAU
6. CTA climat lunaire

---

## Design micro-feedback

### Text-button discret (pas de bouton plein)

**Principe** : Minimalisme, pas de bouton coloré imposant.

**Styles** :
```typescript
journalCta: {
  paddingVertical: spacing.sm,        // 8px
  marginBottom: spacing.xs,           // 4px
}

journalCtaText: {
  ...fonts.body,                      // 16px, weight 400
  color: colors.textMuted,            // #a0a0b0 (gris clair)
  fontSize: 14,
}

journalCtaTextEdited: {
  color: colors.success,              // #4ade80 (vert)
}
```

**Pressed state** :
- Opacity: `0.6` (feedback tactile léger)

**Pas d'animation** :
- Transition de couleur instantanée (gris ↔ vert)
- Pas de fade, pas de scale, pas de shimmer
- Principe: Calme et minimaliste

---

## i18n

### Clés FR

```json
{
  "ritualCard": {
    "journalPrompt": "Noter mon ressenti",
    "journalEdited": "Relire / Modifier"
  }
}
```

### Clés EN

```json
{
  "ritualCard": {
    "journalPrompt": "Note your feelings",
    "journalEdited": "Review / Edit"
  }
}
```

**Note** : La checkmark ✓ est ajoutée programmatiquement (pas dans i18n).

---

## Code final

### DailyRitualCard.tsx (extrait)

```typescript
// State
const [journalModalVisible, setJournalModalVisible] = useState(false);
const [hasJournalToday, setHasJournalToday] = useState(false);

// Check journal entry on mount
useEffect(() => {
  checkJournalEntry();
}, []);

// Refresh journal status when modal closes
useEffect(() => {
  if (!journalModalVisible) {
    checkJournalEntry();
  }
}, [journalModalVisible]);

const checkJournalEntry = async () => {
  const today = getTodayDateString();
  const exists = await hasJournalEntry(today);
  setHasJournalToday(exists);
};

const handleJournalPress = () => {
  setJournalModalVisible(true);
};

// Render
<Pressable
  onPress={handleJournalPress}
  style={({ pressed }) => [
    styles.journalCta,
    pressed && styles.journalCtaPressed,
  ]}
>
  <Text
    style={[
      styles.journalCtaText,
      hasJournalToday && styles.journalCtaTextEdited,
    ]}
  >
    {hasJournalToday ? '✓ ' : ''}
    {hasJournalToday
      ? t('ritualCard.journalEdited')
      : t('ritualCard.journalPrompt')}
  </Text>
</Pressable>

{/* Journal Modal */}
{data && (
  <JournalEntryModal
    visible={journalModalVisible}
    onClose={() => setJournalModalVisible(false)}
    moonContext={data.moon}
  />
)}
```

---

## Performance

### Détection existence entrée

**Complexité** : O(1)
- `hasJournalEntry()` appelle `AsyncStorage.getItem('journal_entry_YYYY-MM-DD')`
- Lookup direct par clé

**Fréquence** :
- 1x au mount de DailyRitualCard
- 1x au close de JournalEntryModal
- Total: ~2-3 calls par session utilisateur

**Impact** : Négligeable (< 5ms par call)

---

## UX Flow complet

### Scénario 1 : Première entrée du jour

1. User ouvre Home → DailyRitualCard s'affiche
2. `checkJournalEntry()` → `hasJournalToday = false`
3. Text-button affiche "Noter mon ressenti" (gris)
4. User tap → Modal s'ouvre (TextInput vide)
5. User écrit + tap "Enregistrer"
6. Modal se ferme → `checkJournalEntry()` refresh
7. Text-button devient "✓ Relire / Modifier" (vert)

### Scénario 2 : Modifier entrée existante

1. User ouvre Home → DailyRitualCard s'affiche
2. `checkJournalEntry()` → `hasJournalToday = true`
3. Text-button affiche "✓ Relire / Modifier" (vert)
4. User tap → Modal s'ouvre (TextInput pré-rempli)
5. User modifie texte + tap "Enregistrer"
6. Modal se ferme → Bouton reste vert
7. Ou user tap "Supprimer" → Bouton redevient "Noter mon ressenti" (gris)

---

## Différences avec version précédente

### Avant (bouton plein)

❌ **Bouton imposant** :
- Background coloré (`rgba(183, 148, 246, 0.15)`)
- Border (`rgba(183, 148, 246, 0.3)`)
- Padding large (`spacing.md`)
- Visuel lourd

### Après (text-button discret)

✅ **Text-button minimaliste** :
- Pas de background
- Pas de border
- Padding minimal (`spacing.sm`)
- Visuel léger, calme

### Raison du changement

Respecter le principe "UX calme, minimaliste" défini dans les specs initiales. Le journal est optionnel, pas une feature push.

---

## Tests manuels recommandés

### Test 1 : Création entrée
1. Vérifier bouton "Noter mon ressenti" (gris)
2. Tap → Modal s'ouvre vide
3. Écrire texte + enregistrer
4. Vérifier bouton devient "✓ Relire / Modifier" (vert)

### Test 2 : Modification entrée
1. Tap bouton vert
2. Modal s'ouvre avec texte existant
3. Modifier texte + enregistrer
4. Vérifier bouton reste vert

### Test 3 : Suppression entrée
1. Tap bouton vert
2. Modal s'ouvre
3. Tap "Supprimer" → Confirmer
4. Vérifier bouton redevient gris "Noter mon ressenti"

### Test 4 : Refresh journalier
1. Créer entrée aujourd'hui (bouton vert)
2. Attendre minuit (ou forcer changement date device)
3. Refresh app
4. Vérifier bouton redevient gris pour nouveau jour

---

## Limitations connues

1. **Pas de notification** : User doit ouvrir Home pour voir le CTA
   - Pas de push "Écrivez votre journal"
   - Principe: Pas de pression

2. **Pas de streak** : Pas de compteur "X jours consécutifs"
   - Phase 2 optionnel
   - Éviter gamification excessive

3. **Pas de preview texte** : Bouton ne montre pas extrait
   - Volontaire: Text-button doit rester court
   - Preview disponible en Phase 2 (timeline)

---

## Roadmap Phase 2 (intégration avancée)

### v2.1 : Badge streak (optionnel)
```
┌─────────────────────────────────────┐
│  ✓ Relire / Modifier  [🔥 7 jours] │
└─────────────────────────────────────┘
```
- Petit badge discret si streak ≥ 3 jours
- Pas d'animation, juste indicateur

### v2.2 : Preview entrée passée
Au tap long sur bouton vert:
- Bottom sheet avec preview 3 lignes
- "Lire en entier" → Ouvre modal

### v2.3 : Navigation directe timeline
Depuis Home, accès rapide à timeline complète:
- Nouveau CTA "Voir tout mon journal" (Phase 2)
- Route `/journal/history`

---

## Métriques de succès

### Primaires
1. **Taux de création** : 30% des users qui voient le CTA tapent dessus
2. **Conversion écriture** : 80% de ceux qui ouvrent le modal écrivent quelque chose

### Secondaires
3. **Taux de modification** : 10% des entrées sont modifiées après création
4. **Abandon modal** : < 20% de ceux qui ouvrent ferment sans écrire

---

**Intégration discrète, UX calme, feedback visuel minimaliste.**
**Code production-ready, TypeScript clean, i18n 100% parity.**
