# Optimisation Performance Home avec SWR

## Contexte
L'écran Home (`apps/mobile/app/index.tsx`) effectuait de multiples requêtes API à chaque render, causant des re-renders inutiles et une expérience utilisateur dégradée.

## Solution Implémentée
Implémentation de **SWR (Stale-While-Revalidate)** pour optimiser le cache et réduire les requêtes API redondantes.

## Fichiers Modifiés

### 1. Nouveau fichier: `apps/mobile/hooks/useLunarData.ts`
Création de 3 hooks personnalisés avec SWR:

#### `useCurrentLunarReturn()`
- **Cache**: 60 secondes
- **Auto-refresh**: Non (données stables)
- **Déduplication**: 1 minute
- **Use case**: Révolution lunaire du mois actuel

#### `useVocStatus()`
- **Cache**: 5 minutes
- **Auto-refresh**: Oui, toutes les 5 minutes
- **Déduplication**: 1 minute
- **Use case**: Statut Void of Course (change fréquemment)

#### `useMajorTransits()`
- **Cache**: 60 secondes
- **Auto-refresh**: Non (données stables sur un mois)
- **Déduplication**: 1 minute
- **Use case**: Transits majeurs du mois

### 2. Modifié: `apps/mobile/app/index.tsx`
**Avant:**
```typescript
const [currentLunarReturn, setCurrentLunarReturn] = useState<LunarReturn | null>(null);

const loadCurrentLunarReturn = useCallback(async () => {
  try {
    const current = await lunarReturns.getCurrent();
    setCurrentLunarReturn(current);
  } catch (error: any) {
    // Error handling
  }
}, []);

useEffect(() => {
  if ((isAuthenticated || isDevAuthBypassActive()) && !isCheckingRouting) {
    loadCurrentLunarReturn();
  }
}, [isAuthenticated, isCheckingRouting, loadCurrentLunarReturn]);
```

**Après:**
```typescript
const { data: currentLunarReturn, mutate: refreshLunarReturn } = useCurrentLunarReturn();

// Plus besoin de useEffect - SWR gère automatiquement
```

### 3. Modifié: `apps/mobile/components/VocWidget.tsx`
**Avant:**
```typescript
const [status, setStatus] = useState<VocStatus | null>(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(false);

useEffect(() => {
  loadVocStatus();
  const interval = setInterval(loadVocStatus, 5 * 60 * 1000);
  return () => clearInterval(interval);
}, []);
```

**Après:**
```typescript
const { data: status, error, isLoading } = useVocStatus();
// SWR gère automatiquement le refresh toutes les 5 minutes
```

### 4. Modifié: `apps/mobile/components/TransitsWidget.tsx`
**Avant:**
```typescript
const [majorAspects, setMajorAspects] = useState<AspectInfo[]>([]);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(false);

useEffect(() => {
  if (isAuthenticated || isDevAuthBypassActive()) {
    loadTransits();
  }
}, [user, isAuthenticated]);
```

**Après:**
```typescript
const { data: majorAspects, error, isLoading } = useMajorTransits();
// SWR gère automatiquement le cache et la déduplication
```

## Bénéfices

### 1. Performance
- **Déduplication automatique**: Si plusieurs composants demandent la même ressource, une seule requête est effectuée
- **Cache intelligent**: Les données sont servies depuis le cache pendant la revalidation
- **Réduction des re-renders**: SWR optimise les mises à jour du state

### 2. Expérience Utilisateur
- **Affichage instantané**: Données du cache affichées immédiatement (stale-while-revalidate)
- **Mise à jour en arrière-plan**: Les données sont revalidées en arrière-plan sans bloquer l'UI
- **Refresh automatique**: VoC se met à jour automatiquement toutes les 5 minutes

### 3. Code Quality
- **Moins de boilerplate**: Plus besoin de gérer manuellement `useState`, `useEffect`, `setInterval`
- **Meilleure séparation des responsabilités**: Logique de fetching isolée dans les hooks
- **Type-safe**: TypeScript garantit la cohérence des types

## Métriques Attendues

### Avant SWR
- **Requêtes API au mount de Home**: 3 (lunarReturn + VoC + transits)
- **Re-renders inutiles**: Multiple par useEffect
- **Requêtes redondantes**: Oui (pas de déduplication)

### Après SWR
- **Requêtes API au mount de Home**: 3 (initial) puis 0 si données en cache
- **Re-renders optimisés**: SWR minimise les re-renders
- **Requêtes redondantes**: Non (déduplication sur 60s)
- **Cache hit rate**: ~80% après warm-up

## Configuration SWR

```typescript
const swrConfig = {
  revalidateOnFocus: false,    // Pas de revalidation au focus (évite requêtes inutiles)
  dedupingInterval: 60000,     // Déduplication sur 1 minute
  shouldRetryOnError: false,   // Pas de retry automatique
};
```

## Tests de Validation

### Test 1: Déduplication
1. Ouvrir Home screen
2. Naviguer vers un autre screen
3. Revenir sur Home dans les 60 secondes
4. **Résultat attendu**: Aucune requête API (données servies du cache)

### Test 2: Auto-refresh VoC
1. Ouvrir Home screen
2. Attendre 5 minutes
3. **Résultat attendu**: VocWidget se met à jour automatiquement

### Test 3: Partage de cache
1. Ouvrir Home screen (charge lunarReturn)
2. Naviguer vers `/lunar/report` (même lunarReturn)
3. **Résultat attendu**: Données instantanées (cache partagé)

### Test 4: Performance
1. Ouvrir React DevTools Profiler
2. Mesurer le temps de render de Home
3. Comparer avant/après SWR
4. **Résultat attendu**: Réduction du temps de render de 30-50%

## Migration Future

### Candidats pour SWR
- `DailyRitualCard`: Cache daily climate
- `JournalPrompt`: Cache journal entries
- Écrans `/lunar/report`: Réutiliser le cache de `useCurrentLunarReturn()`
- Écrans `/transits/overview`: Réutiliser le cache de `useMajorTransits()`

### Configuration avancée
- **Fallback data**: Pré-remplir le cache au démarrage de l'app
- **Mutation optimiste**: Mettre à jour l'UI avant la confirmation serveur
- **Pagination**: Implémenter infinite scroll avec SWR

## Références
- [SWR Documentation](https://swr.vercel.app/)
- [React Performance Optimization](https://react.dev/learn/render-and-commit)
- [Stale-While-Revalidate Strategy](https://web.dev/stale-while-revalidate/)

---

**Date**: 2026-01-17
**Auteur**: Claude Code
**Status**: Implémenté et testé (typecheck OK)
