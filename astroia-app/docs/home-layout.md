# Structure cible de la page d'accueil LUNA

## Objectif produit
La page d'accueil doit immédiatement communiquer que LUNA est un assistant lunaire personnalisé centré sur la Révolution lunaire mensuelle, avec le thème natal et les cycles comme compléments.

## Ordre des sections (du haut vers le bas)

### 1. Header "Aujourd'hui" (TodayHeader)
- **Position** : Tout en haut
- **Contenu** : Cycle du jour (si applicable) + Lune du jour + Mantra
- **Composant** : `components/home/TodayHeader.js` (existant)

### 2. Révolution lunaire du mois (HERO)
- **Position** : Immédiatement après TodayHeader
- **Composant** : `components/home/LunarRevolutionHero.tsx` (existant)
- **Contenu** :
  - Titre : "RÉVOLUTION LUNAIRE DU MOIS"
  - Signe de la Lune + élément
  - Maison activée
  - Phase lunaire (dernier quartier, gibbeuse, etc.)
  - Court résumé (2-3 phrases max)
  - CTA : "→ Voir ma Révolution lunaire" → `/lunar-revolution`
- **Données** : Via `useLunarRevolutionStore.currentMonthRevolution`

### 3. Tendances du mois
- **Position** : Juste après la révolution lunaire
- **Composant** : `components/home/MonthlyTrendsCard.tsx` (existant)
- **Contenu** :
  - Focus du mois (domaines activés)
  - Résumé d'interprétation
- **Données** : Via `currentMonthRevolution.focus` et `currentMonthRevolution.interpretationSummary`

### 4. Résumé Thème Natal (Big Three)
- **Position** : Après les tendances du mois
- **Composant** : `components/home/NatalSummaryCard.tsx` (existant)
- **Contenu** :
  - Titre : "THÈME NATAL"
  - Soleil, Lune, Ascendant + éléments
  - CTA : "→ Voir mon thème complet" → `/natal-reading`
- **Données** : Via `useProfileStore.profile` (sunSign, moonSign, ascendant)

### 5. Section Cycles (conditionnelle)
- **Position** : Après le thème natal
- **Affichage** : Uniquement si `profile.gender === 'female' && profile.hasCycles === true`
- **Composants** :
  - `CycleCard` : "Mon cycle aujourd'hui" (Jour X, phase, Énergie)
  - `QuickPeriodLog` : Log rapide des règles
  - `CycleCountdown` : Compte à rebours prochaines règles
  - `FertilityWidget` : Fertilité & Ovulation
  - Lien "→ Mes cycles" → `/my-cycles`
- **CTA** : "→ Voir détails" → `/cycle-astro`

### 6. Suggestions du mois (dérivées de la Révolution lunaire)
- **Position** : Après les cycles (ou après thème natal si pas de cycles)
- **Composants** : À créer ou réutiliser depuis `components/lunar-revolution/`
- **Contenu** : 4 cartes de focus :
  - Émotions
  - Rythme & Énergie
  - Relations
  - Introspection
- **Note** : Pour l'instant, `MonthlyTrendsCard` peut servir de placeholder

### 7. Humeur & Émotions
- **Position** : Après les suggestions
- **Composant** : `components/home/MoodCard.js` (existant)
- **CTA** : "Ouvrir le journal" → `/journal`

### 8. Astro du jour (secondaire)
- **Position** : Après Humeur
- **Composant** : `components/home/AstroCard.js` (existant)
- **Note** : Gardé mais positionné comme élément secondaire
- **CTA** : "→ Voir analyse" → `/horoscope`

### 9. Explorateur (grid des autres fonctionnalités)
- **Position** : Après Astro du jour
- **Composant** : `components/home/ExploreGrid.tsx` (existant)
- **Contenu** : Modules secondaires :
  - Thème natal (si pas déjà affiché en résumé)
  - Mes cycles (conditionnel selon `hasCycles`)
  - Calendrier
  - Compatibilité
  - Horoscope IA
  - Parent-enfant
- **Note** : La tuile "Mes cycles" doit être masquée si `hasCycles === false`

### 10. Disclaimer médical
- **Position** : En bas, avant le padding final
- **Composant** : `components/MedicalDisclaimer.js` (existant)

## Points d'intégration avec les stores

### `useLunarRevolutionStore`
- `currentMonthRevolution` : Données de la révolution du mois
- `fetchForMonth(date)` : Charger la révolution pour un mois
- `status` : État de chargement ('idle' | 'loading' | 'loaded' | 'error')

### `useProfileStore`
- `profile.gender` : 'female' | 'male' | 'other' | null
- `profile.hasCycles` : boolean (détermine l'affichage des cycles)
- `profile.sunSign`, `profile.moonSign`, `profile.ascendant` : Données astrologiques

### `useCycleHistoryStore`
- `getCurrentCycleData()` : Données du cycle actuel
- Utilisé uniquement si `hasCycles === true`

## Composants à modifier/créer

### À modifier
- `app/(tabs)/home.tsx` : Réorganiser l'ordre des sections
- `components/home/ExploreGrid.tsx` : Conditionner l'affichage de "Mes cycles"

### À créer (optionnel, Sprint 4+)
- `components/home/MonthlyFocusCards.tsx` : 4 cartes de suggestions (Émotions, Rythme, Relations, Introspection)
- `lib/utils/dateFormatters.ts` : Utilitaires de formatage de dates

## Logique d'affichage conditionnel

### Cycles menstruels
```typescript
const shouldShowCycles = profile.gender === 'female' && profile.hasCycles === true;
```

### Composants conditionnels dans home.tsx
- `CycleCard` : `{shouldShowCycles && hasHealth && cycle ? <CycleCard ... /> : null}`
- `QuickPeriodLog` : `{shouldShowCycles ? <QuickPeriodLog /> : null}`
- `CycleCountdown` : `{shouldShowCycles ? <CycleCountdown /> : null}`
- `FertilityWidget` : `{shouldShowCycles ? <FertilityWidget /> : null}`
- Lien "→ Mes cycles" : `{shouldShowCycles ? <TouchableOpacity>...</TouchableOpacity> : null}`

### ExploreGrid
- Filtrer la tuile "Mes cycles" si `hasCycles === false`

## Migration des profils existants

Lors du chargement d'un profil existant sans `gender` ou `hasCycles` :
- `gender` : `null` (à définir par l'utilisateur)
- `hasCycles` : `false` (par défaut, pour ne pas afficher les cycles si non configuré)

