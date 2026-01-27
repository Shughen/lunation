# Bug : Routing bloqué sans DEV_AUTH_BYPASS

## Problème

Quand `EXPO_PUBLIC_DEV_AUTH_BYPASS=false`, l'app reste bloquée sur l'écran "Chargement..." au lieu de rediriger vers `/login` ou `/welcome`.

## Reproduction

1. Désactiver DEV_AUTH_BYPASS dans `.env` :
   ```
   EXPO_PUBLIC_DEV_AUTH_BYPASS=false
   ```
2. Effacer les données Expo Go : `adb shell pm clear host.exp.exponent`
3. Relancer l'app : `npx expo start --clear` puis `a`
4. L'app affiche "Chargement..." indéfiniment

## Logs observés

```
[INDEX] ⏳ Hydratation en cours...
[INDEX] ⏸️ Routing déjà en cours, skip double-run
[INDEX] ✅ Hydratation terminée
```

Après "Hydratation terminée", aucun log de routing n'apparaît.

## Cause probable

Dans `app/index.tsx`, le flow de routing a un problème :

1. `isCheckingRouting` est initialisé à `true` (ligne 59)
2. Le loader s'affiche tant que `isCheckingRouting && !isDevAuthBypassActive()` (ligne 291)
3. Après hydratation, le useEffect devrait re-run car `isOnboardingHydrated` change
4. Mais le re-render ne semble pas déclencher un nouveau passage dans le useEffect

## Solution proposée

Options à explorer :
1. Vérifier que `hydrateOnboarding()` déclenche bien un re-render via le selector Zustand
2. Ajouter un `setIsCheckingRouting(false)` avant les redirections (lignes 166, 174, etc.)
3. Utiliser un state local pour forcer le re-render après hydratation

## Fichiers concernés

- `apps/mobile/app/index.tsx` (lignes 68-233, 291-299)
- `apps/mobile/stores/useOnboardingStore.ts`

## Priorité

Moyenne - bloque le test de l'inscription sans DEV_AUTH_BYPASS

## Date

2026-01-27
