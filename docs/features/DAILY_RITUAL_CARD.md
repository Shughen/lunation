# Feature: Carte Rituel Quotidien

**Status**: ✅ Implémentée (2025-12-31)

---

## Vue d'ensemble

Carte "Aujourd'hui" affichée sur le dashboard Home pour renforcer l'usage quotidien de l'app.

### Principes
- **Déterministe** : Pas d'IA, logique claire basée sur phase lunaire
- **Minimaliste** : 1 phrase de guidance max, design calme
- **Robuste** : Fallback cascade (API → cache → calcul local)
- **Premium** : Animation subtile au premier affichage du jour

---

## Architecture

### Fichiers créés

```
apps/mobile/
├── types/ritual.ts                    # Types TypeScript (MoonPhase, DailyRitualData, etc.)
├── utils/ritualHelpers.ts             # Helpers (emoji, formatage, calcul phase locale)
├── services/ritualService.ts          # Service fetch API + cache AsyncStorage
├── components/DailyRitualCard.tsx     # Composant principal
├── __tests__/ritualHelpers.test.ts    # Tests unitaires (12 tests, 100% pass)
└── i18n/
    ├── fr.json                        # +13 clés (guidance, vocActive, etc.)
    └── en.json                        # +13 clés (traductions EN)
```

### Fichiers modifiés

```
apps/mobile/
└── app/index.tsx                      # Intégration carte dans Home (ligne 418)
```

---

## Contenu affiché

### Header
```
🌑 Aujourd'hui
```
- Emoji dynamique selon phase lunaire (8 phases)

### Phase + Signe
```
NOUVELLE LUNE EN VERSEAU
PREMIER QUARTIER EN TAUREAU
```
- All caps pour impact visuel
- Fallback "NOUVELLE LUNE" si signe inconnu

### Guidance (1 phrase)
8 phrases déterministes selon phase lunaire :

| Phase | Guidance FR |
|-------|-------------|
| Nouvelle Lune | "Énergie de renouveau. Moment propice aux intentions." |
| Premier Croissant | "Élan créatif. Posez vos premières pierres." |
| Premier Quartier | "Tension fertile. Ajustez vos actions." |
| Gibbeuse Croissante | "Affinez vos projets. La pleine lumière approche." |
| Pleine Lune | "Apogée émotionnelle. Contemplez ce qui se révèle." |
| Gibbeuse Décroissante | "Gratitude active. Partagez ce qui a mûri." |
| Dernier Quartier | "Relâchez ce qui pèse. Faites de la place." |
| Dernier Croissant | "Transition douce. Intériorité avant le renouveau." |
| Fallback | "Écoutez votre intuition lunaire." |

### Badge VoC (si actif)
```
⚠️ Lune flottante jusqu'à 14h32
```
- Background warning transparent
- Affiché uniquement si `VocStatus.now.is_active === true`

### CTA
```
→ Voir le climat lunaire
```
- Navigation vers `/lunar` (future: `/lunar/daily-climate`)

---

## Logique de fetch

### Cascade de fallback

1. **Cache AsyncStorage** (TTL 24h)
   - Key: `daily_ritual_card_${YYYY-MM-DD}`
   - Validité: même date + age < 24h

2. **API parallèle** (si cache invalide)
   - `GET /api/lunar/daily-climate` → phase + signe
   - `GET /api/lunar/voc/status` → VoC actif

3. **Calcul local** (si API fail)
   - Phase lunaire calculée avec algorithme simplifié
   - Signe: "Unknown"
   - VoC: undefined

### Cache local
```typescript
{
  data: {
    date: "2025-12-31",
    moon: { phase: "Full Moon", sign: "Scorpio" },
    voc: { is_active: true, end_at: "2025-12-31T14:32:00Z" }
  },
  cached_at: 1735660800000
}
```

---

## États UI

### 1. Loading
- Skeleton shimmer violet (160px height)
- Durée: ~500ms en moyenne

### 2. Nominal (premier affichage)
- Animation fade-in (600ms) + translateY (20px → 0)
- Marque AsyncStorage key `ritual_card_last_viewed_${YYYY-MM-DD}`

### 3. Nominal (déjà consulté)
- Pas d'animation
- Données identiques, consultable à nouveau

### 4. VoC actif
- Badge warning affiché
- Heure de fin formatée (HH:mm)

### 5. Erreur API (fallback total)
- Affiche phase calculée localement
- Signe "Unknown" → texte "NOUVELLE LUNE" (sans signe)
- Guidance fallback

### 6. Offline (cache expiré)
- Affiche dernière donnée en cache
- Badge "📡 Données du 30 déc."

---

## Design system

### Couleurs
```typescript
card: {
  backgroundColor: colors.cardBg,      // #2a1a4e
  borderColor: 'rgba(183, 148, 246, 0.1)',
}
vocBadge: {
  backgroundColor: 'rgba(251, 191, 36, 0.1)',
  borderColor: colors.warning,         // #fbbf24
}
```

### Typographie
```typescript
headerText: fonts.bodySmall,           // 14px, uppercase, letter-spacing: 0.8
phaseTitle: fonts.h3,                  // 20px, weight 600, letter-spacing: 0.5
guidance: fonts.body + italic,         // 16px, italic
ctaText: fonts.button,                 // 15px, weight 600, color: accent
```

### Spacing
```typescript
padding: spacing.lg,                   // 24px
marginBottom: spacing.md,              // 16px
```

---

## i18n

### Clés FR (13 nouvelles)
```json
{
  "ritualCard": {
    "header": "Aujourd'hui",
    "guidance": {
      "new_moon": "...",
      "waxing_crescent": "...",
      // ... 8 phases
      "fallback": "..."
    },
    "vocActive": "Lune flottante jusqu'à {{endTime}}",
    "cachedData": "Données du {{date}}",
    "cta": "Voir le climat lunaire"
  }
}
```

### Clés EN (13 nouvelles)
Traductions équivalentes avec interpolation `{{endTime}}` et `{{date}}`.

---

## Tests

### Tests unitaires (__tests__/ritualHelpers.test.ts)
- ✅ 12 tests, 100% pass
- Couverture:
  - `getPhaseEmoji()` → 4 tests
  - `getPhaseKey()` → 1 test
  - `formatTime()` → 1 test
  - `formatCacheDate()` → 2 tests (FR + EN)
  - `getTodayDateString()` → 2 tests
  - `calculateLocalPhase()` → 2 tests

### Validation TypeScript
```bash
npm run lint
# ✅ 0 errors
```

### Validation i18n
```bash
npm run check:i18n
# ✅ 118 keys in FR, 118 keys in EN (100% parity)
```

---

## Intégration Home

### Placement
```tsx
{/* Salutation temporelle */}
{moonPosition && (
  <Text style={styles.greeting}>{greeting}</Text>
)}

{/* Carte Rituel Quotidien */}
<DailyRitualCard />

{/* HERO : Mon Cycle Lunaire Actuel */}
<TouchableOpacity style={styles.currentCycleCard}>
  ...
</TouchableOpacity>
```

**Position** : Juste après la salutation, avant la carte "Mon Cycle Actuel"

---

## Performance

### Cache
- **Client-side** : AsyncStorage, TTL 24h
- **Serveur** : Daily Climate API cache 24h (serveur)
- **Invalidation** : Automatique à minuit local (changement de date)

### Animations
- **useNativeDriver: true** → GPU-accelerated
- **Durée**: 600ms (subtile)
- **Trigger**: 1x/jour max (first view)

### Fetch
- **Parallèle** : Daily Climate + VoC en `Promise.allSettled()`
- **Timeout** : Géré par axios (défaut 30s)
- **Retry** : Aucun (fallback immédiat)

---

## Prochaines étapes (Phase 2)

### v2.1 : Guidance enrichie
- Combiner phase + signe lunaire (64 combinaisons)
- Table `phase_sign` → phrase nuancée
- Fallback sur phase seule si mapping manquant

### v2.2 : Page détail Climat Lunaire
- Route `/lunar/daily-climate`
- Affichage complet `insight.text` (markdown)
- Possibilité d'approfondir

### v2.3 : Résonance du soir
- "Comment était votre journée ?" (5 étoiles + note)
- Stockage local pour future corrélation cycle/événements

### v2.4 : Analytics
- Tracker vues quotidiennes
- Taux de clic CTA
- Heure de consultation (distribution)

---

## Metrics de succès (post-lancement)

### Primaires
1. **DAU/MAU** : +15% après 1 mois
2. **Taux de consultation** : 40% des users 5j/7
3. **Taux de clic CTA** : 30-40% des vues

### Secondaires
4. **Heure de consultation** : 60%+ matin (6h-12h)
5. **Rétention J+7 et J+30** : +10% vs baseline
6. **NPS** : Survey in-app après 2 semaines

---

## Notes techniques

### Dépendances
- `react-i18next` : i18n FR/EN
- `@react-native-async-storage/async-storage` : Cache local
- `expo-router` : Navigation
- Aucune nouvelle dépendance ajoutée

### Compatibilité
- iOS ✅
- Android ✅
- Web ⚠️ (AsyncStorage remplacé par localStorage automatiquement)

### Sécurité
- Aucune donnée sensible
- Cache local uniquement (pas de sync serveur)
- Pas de tracking utilisateur

---

**Implémentation complète, production-ready.**
**TypeScript strict, i18n 100% parity, tests 100% pass.**
