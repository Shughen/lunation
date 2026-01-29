# Lunation Mobile - Documentation des Ecrans

## Architecture de Navigation

```
app/
├── index.tsx                 # Routing guards (auth, onboarding)
├── _layout.tsx               # Root Stack Navigator
├── (tabs)/                   # Tab Navigator (5 onglets)
│   ├── _layout.tsx           # Configuration tabs
│   ├── home.tsx              # Accueil
│   ├── calendar.tsx          # Calendrier lunaire
│   ├── horoscope.tsx         # Horoscope du jour
│   ├── rituals.tsx           # Rituels quotidiens
│   └── profile.tsx           # Profil utilisateur
├── auth.tsx                  # Authentification (modal)
├── welcome.tsx               # Ecran bienvenue (modal)
├── onboarding/               # Flow onboarding (modal)
├── lunar/                    # Details lunaires (stack)
├── natal-chart/              # Theme natal (stack)
└── transits/                 # Transits (stack)
```

---

## Tab Navigator

**Fichier** : `app/(tabs)/_layout.tsx`

### Configuration
- 5 onglets avec icones SVG custom
- Style : fond `#1a0b2e`, accent or `#ffd700` pour onglet actif
- Hauteur : 70px + safe area iOS

### Onglets
| Onglet | Route | Icone | Description |
|--------|-------|-------|-------------|
| Accueil | `/home` | Maison + lune | Dashboard principal |
| Calendrier | `/calendar` | Calendrier + point lune | Vue mensuelle |
| Horoscope | `/horoscope` | Oeil mystique | Horoscope du jour |
| Rituels | `/rituals` | Ampoule | Rituels quotidiens |
| Profil | `/profile` | Silhouette | Parametres utilisateur |

---

## Ecrans Tabs

### 1. Home (`home.tsx`)

**Role** : Dashboard principal avec widgets lunaires

**Composants utilises** :
- `CurrentLunarCard` - Revolution lunaire en cours (hero)
- `DailyRitualCard` - Rituel du jour
- `VocWidget` - Statut Void of Course
- `TransitsWidget` - Transits majeurs
- `JournalPrompt` - Invitation journal

**Donnees** :
- `useCurrentLunarReturn()` - SWR hook pour revolution lunaire
- `useLunar()` - Context pour donnees lunaires temps reel

**Features** :
- Pull-to-refresh
- Detection mode hors ligne
- Notification tap listener
- Quick access vers theme natal

---

### 2. Calendar (`calendar.tsx`)

**Role** : Vue mensuelle avec phases lunaires

**Composants** :
- Navigation mois (precedent/suivant)
- Grille 7x6 jours
- Legende phases principales

**Calculs locaux** :
- `getMoonPhase(date)` - Calcule la phase lunaire pour chaque jour
  - Base : cycle synodique de 29.53 jours
  - Reference : nouvelle lune du 6 janvier 2000

**Interactions** :
- Tap sur jour → navigation vers `/lunar-month/{YYYY-MM}`
- Tap sur titre mois → retour a aujourd'hui

**Affichage phases** :
| Phase | Emoji |
|-------|-------|
| Nouvelle Lune | 🌑 |
| Premier Croissant | 🌒 |
| Premier Quartier | 🌓 |
| Gibbeuse Croissante | 🌔 |
| Pleine Lune | 🌕 |
| Gibbeuse Decroissante | 🌖 |
| Dernier Quartier | 🌗 |
| Dernier Croissant | 🌘 |

---

### 3. Horoscope (`horoscope.tsx`)

**Role** : Horoscope lunaire quotidien personnalise

**Structure UI** :
```
┌─────────────────────────────────────┐
│       Horoscope Lunaire             │
│         [ZodiacBadge]               │
│    Date · Phase lunaire             │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ Guidance du Jour                │ │
│ │ Texte d'orientation...          │ │
│ │ Mots-cles: [Chip] [Chip]        │ │
│ └─────────────────────────────────┘ │
│                                     │
│ [ProgressBar Energie]  [ProgressBar]│
│                                     │
│ [DomainCard Amour] [DomainCard Pro] │
│                                     │
│ [LuckyElements]                     │
│                                     │
│      [Partager mon horoscope]       │
└─────────────────────────────────────┘
```

**Composants dedies** :
- `ProgressBar` - Barre de progression animee
- `KeywordChip` - Badge mot-cle
- `DomainCard` - Carte domaine (Amour/Carriere)
- `LuckyElements` - Elements chanceux

**Donnees** :
- `useLunar()` - Phase et signe lunaire
- `useCurrentLunarReturn()` - Aspects du mois

**Calculs locaux** (`utils/horoscopeCalculations.ts`) :
| Metrique | Source |
|----------|--------|
| Energie Creative | Phase lunaire + aspects favorables |
| Intuition | Signe lunaire (boost si eau) + aspects Neptune |
| Nombres chanceux | Jour du mois (algo simple) |
| Couleur | Element du signe (Feu→Rouge, Eau→Violet...) |
| Pierre | Mapping signe → pierre traditionnelle |
| Heures | Mapping element → plage horaire |

**Note** : Les "elements chanceux" sont des calculs simplifies a but inspirationnel, pas de l'astrologie traditionnelle.

---

### 4. Rituals (`rituals.tsx`)

**Role** : Rituels quotidiens adaptes a la phase lunaire

**Structure** :
- Header avec phase actuelle et progression
- Liste de 3 rituels (checkable)
- Section reflexion du jour avec prompt
- Tip card

**Rituels par phase** :
| Phase | Theme |
|-------|-------|
| Nouvelle Lune | Intentions, visualisation, nettoyage |
| Croissant | Action, affirmations, planification |
| Premier Quartier | Decision, perseverance |
| Gibbeuse | Perfectionnement, gratitude |
| Pleine Lune | Celebration, liberation |
| Gibbeuse Dec. | Partage, reflexion |
| Dernier Quartier | Lacher-prise, tri |
| Decroissant | Repos, introspection |

**Interactions** :
- Toggle rituel complete (state local, non persiste)
- Ouvrir journal modal

**Composants** :
- `JournalEntryModal` - Modal d'ecriture journal
- `MoonPhaseIcon` - Icone phase lunaire

---

### 5. Profile (`profile.tsx`)

**Role** : Informations utilisateur et parametres

**Sections** :
1. **Carte profil** - Avatar (ZodiacBadge basee sur signe solaire), nom, email
2. **Informations naissance** - Date, heure, lieu
3. **Notifications** - Toggle avec demande permission
4. **Actions** - Deconnexion, suppression donnees locales

**Donnees** :
- `useAuthStore()` - Utilisateur authentifie
- `useOnboardingStore()` - Donnees profil onboarding
- `useNotificationsStore()` - Preferences notifications

**Calcul signe solaire** :
- Fonction `getSunSign(birthDate)` basee sur date de naissance

---

## Composants Partages

### ProgressBar (`components/ProgressBar.tsx`)
```tsx
<ProgressBar
  label="Energie Creative"
  value={86}
  color={colors.gold}
  showPercentage={true}
  animate={true}
/>
```

### KeywordChip (`components/KeywordChip.tsx`)
```tsx
<KeywordChip label="Action" variant="accent" />
// variants: 'default' | 'accent' | 'gold'
```

### DomainCard (`components/DomainCard.tsx`)
```tsx
<DomainCard
  domain="love"  // 'love' | 'career' | 'health' | 'finance'
  title="Amour"
  description="Periode favorable..."
  subtitle="Compatibilite +"
/>
```

### LuckyElements (`components/LuckyElements.tsx`)
```tsx
<LuckyElements
  numbers={[7, 14]}
  color="Rouge"
  colorHex="#FF6B6B"
  stone="Diamant"
  favorableHours="14h-16h"
/>
```

---

## Utilitaires

### horoscopeCalculations.ts

**Fonctions exportees** :
```typescript
// Metriques completes
getHoroscopeMetrics(moonSign, lunarPhase, aspects) → HoroscopeMetrics

// Metriques individuelles
calculateCreativeEnergy(lunarPhase, aspects) → number (0-100)
calculateIntuition(moonSign, aspects) → number (0-100)
getLuckyElements(moonSign, dayOfMonth) → LuckyElements

// Traductions
getZodiacSignFrench(sign) → string
getMoonPhaseFrench(phase) → string

// Contenu
getPhaseGuidance(phase) → string
getLoveInsight(moonSign) → string
getCareerInsight(moonSign) → string
```

---

## Flux de Navigation

```
App Start
    │
    ▼
index.tsx (Guards)
    │
    ├─ Non authentifie → /auth
    ├─ Welcome non vu → /welcome
    ├─ Consent non accepte → /onboarding/consent
    ├─ Profil incomplet → /onboarding/profile-setup
    ├─ Disclaimer non vu → /onboarding/disclaimer
    ├─ Onboarding non fini → /onboarding
    │
    ▼
/(tabs)/home ◄────────────────────┐
    │                             │
    ├─ Tab Calendrier ────────────┤
    ├─ Tab Horoscope ─────────────┤
    ├─ Tab Rituels ───────────────┤
    └─ Tab Profil ────────────────┘
         │
         ├─ Deconnexion → /welcome
         └─ Reset donnees → /welcome
```

---

## Points d'Attention

1. **Donnees hors ligne** : Home detecte le reseau et affiche un banner
2. **Cache SWR** : Les hooks utilisent SWR avec deduplication 60s
3. **Haptics** : Feedback tactile sur toutes les interactions
4. **Safe Area** : Tab bar ajustee pour iOS (24px bottom padding)
5. **Calculs locaux** : Elements chanceux = approximations, pas d'astrologie reelle

---

*Derniere mise a jour : 29 janvier 2026*
