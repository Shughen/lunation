# Diagnostic du flux de routage Expo Router

## Problème identifié

L'app s'ouvre sur `onboarding/profile-setup` au lieu de `(auth)/login` malgré la simplification de `app/index.js`.

## Flux réel de démarrage selon Expo Router

### 1. Point d'entrée

```
index.js (racine)
  └─> expo-router/entry
      └─> app/_layout.js (RootLayout - Stack Navigator)
          └─> app/index.js (route initiale)
```

### 2. Ordre de montage des composants

1. **`app/_layout.js`** monte en premier
   - Log : `[ROUTING] Mounted RootLayout`
   - Initialise les stores (auth, profile, cycles, révolutions)
   - Configure le Stack Navigator avec 4 groupes :
     - `index` (app/index.js)
     - `(auth)` (app/(auth)/*)
     - `(tabs)` (app/(tabs)/*)
     - `onboarding` (app/onboarding/*)

2. **`app/index.js`** monte ensuite (route initiale)
   - Log : `[ROUTING] Mounted Index`
   - Exécute `checkRouting()` dans un `useEffect`
   - Log : `[ROUTING] checkRouting started`

### 3. Logique de routage dans `app/index.js`

Le fichier `app/index.js` contient la logique de routage conditionnel. Voici le flux détaillé :

```
app/index.js (checkRouting)
  │
  ├─> Attendre que authLoading === false
  │   └─> Si authLoading === true : retour (attente)
  │
  ├─> Si isAuthenticated === true
  │   ├─> Log : "[ROUTING] User authenticated, loading profile from Supabase..."
  │   └─> Charger le profil depuis Supabase
  │
  ├─> Lire AsyncStorage.getItem('onboarding_completed')
  │   └─> Log : "[ROUTING] Onboarding status from AsyncStorage: <valeur>"
  │
  ├─> DÉCISION 1 : Si !isAuthenticated
  │   └─> Log : "[ROUTING] User not authenticated → redirecting to /(auth)/login"
  │   └─> router.replace('/(auth)/login')
  │       └─> app/(auth)/login.js monte
  │           └─> Log : "[ROUTING] Mounted LoginScreen"
  │
  ├─> DÉCISION 2 : Si isAuthenticated ET onboardingStatus !== 'true'
  │   └─> Log : "[ROUTING] Onboarding not completed → redirecting to /onboarding"
  │   └─> router.replace('/onboarding')
  │       └─> app/onboarding/index.js monte
  │           └─> Log : "[ROUTING] Mounted OnboardingScreen (index)"
  │           └─> L'utilisateur peut naviguer vers profile-setup via le carrousel
  │               └─> app/onboarding/profile-setup.js monte
  │                   └─> Log : "[ROUTING] Mounted ProfileSetupScreen"
  │
  ├─> DÉCISION 3 : Si isAuthenticated ET onboardingStatus === 'true' ET !hasProfile
  │   └─> Log : "[ROUTING] Profile incomplete → redirecting to /(tabs)/profile"
  │   └─> router.replace('/(tabs)/profile')
  │
  └─> DÉCISION 4 : Si isAuthenticated ET onboardingStatus === 'true' ET hasProfile
      └─> Log : "[ROUTING] All checks passed → redirecting to /(tabs)/home"
      └─> router.replace('/(tabs)/home')
          └─> app/(tabs)/home.tsx monte
              └─> Log : "[ROUTING] Mounted Home"
```

## Cause racine du problème

### Analyse du code dans `app/index.js` (lignes 54-58)

```javascript
// Utilisateur connecté
if (onboardingStatus !== 'true') {
  // Onboarding non terminé → Onboarding
  console.log('[ROUTING] Onboarding not completed → redirecting to /onboarding');
  router.replace('/onboarding');
  return;
}
```

**Le problème** : Même après désinstallation/réinstallation, si :
1. L'utilisateur a une session Supabase active (via `supabase.auth.getSession()`)
2. Mais `onboarding_completed` n'existe pas dans AsyncStorage (ou vaut `null`)

Alors l'app considère que l'onboarding n'est pas terminé et redirige vers `/onboarding`.

### Pourquoi `profile-setup` s'affiche ?

1. `app/index.js` redirige vers `/onboarding` (app/onboarding/index.js)
2. L'écran d'onboarding affiche un carrousel avec 4 étapes
3. Si l'utilisateur clique sur "Commencer" (dernière étape), il navigue vers `/onboarding/profile-setup`
4. **OU** si l'utilisateur a déjà vu le carrousel et qu'il y a une navigation automatique ou un état persistant, il peut arriver directement sur `profile-setup`

## Schéma du flux complet

```
┌─────────────────────────────────────────────────────────────┐
│                    DÉMARRAGE DE L'APP                       │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  index.js → expo-router/entry                               │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  app/_layout.js (RootLayout)                                │
│  [ROUTING] Mounted RootLayout                               │
│  - Initialise stores (auth, profile, cycles)                 │
│  - Configure Stack Navigator                                │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  app/index.js (route initiale)                              │
│  [ROUTING] Mounted Index                                    │
│  [ROUTING] checkRouting started                             │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
                    ┌─────────┐
                    │ DÉCISION │
                    └─────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   ┌─────────┐      ┌─────────┐      ┌─────────┐
   │ PAS AUTH │      │ AUTH    │      │ AUTH    │
   │          │      │ NO ONBO │      │ ONBO OK │
   └─────────┘      └─────────┘      └─────────┘
        │                 │                 │
        ▼                 ▼                 ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ (auth)/login  │ │ /onboarding   │ │ (tabs)/home   │
│               │ │               │ │               │
│ [ROUTING]     │ │ [ROUTING]     │ │ [ROUTING]     │
│ Mounted       │ │ Mounted       │ │ Mounted       │
│ LoginScreen   │ │ Onboarding    │ │ Home          │
└───────────────┘ └───────────────┘ └───────────────┘
                          │
                          ▼
                  ┌─────────────────┐
                  │ profile-setup   │
                  │ (via carrousel) │
                  │                 │
                  │ [ROUTING]       │
                  │ Mounted         │
                  │ ProfileSetup    │
                  └─────────────────┘
```

## Points d'attention

### 1. AsyncStorage persiste après désinstallation
- Sur iOS/Android, AsyncStorage peut persister dans certains cas
- Même après réinstallation, si l'utilisateur se reconnecte avec le même compte Supabase, la session peut être restaurée
- Mais `onboarding_completed` peut ne pas exister dans AsyncStorage

### 2. Logique de routage dans `app/index.js`
La logique actuelle vérifie dans cet ordre :
1. Authentification (Supabase session)
2. Onboarding (AsyncStorage `onboarding_completed`)
3. Profil complet (Supabase)

**Problème** : Si l'utilisateur est authentifié mais que `onboarding_completed` n'existe pas, il est redirigé vers `/onboarding` au lieu de `/(auth)/login`.

### 3. Navigation depuis `/onboarding`
- L'écran `/onboarding/index.js` peut naviguer vers `profile-setup` via le bouton "Commencer"
- Il n'y a pas de vérification d'authentification dans l'écran d'onboarding

## Recommandations pour la correction

1. **Simplifier la logique dans `app/index.js`** :
   - Si pas de session Supabase → `/(auth)/login`
   - Si session Supabase → `/(tabs)/home`
   - Ne plus vérifier `onboarding_completed` dans AsyncStorage

2. **Gérer l'onboarding différemment** :
   - Vérifier l'onboarding dans l'écran Home ou Profile
   - Ou utiliser un flag dans Supabase au lieu d'AsyncStorage

3. **Ajouter une vérification dans `/onboarding`** :
   - Si l'utilisateur n'est pas authentifié, rediriger vers `/(auth)/login`

## Logs ajoutés pour le diagnostic

Tous les fichiers suivants ont maintenant des logs `[ROUTING]` :
- `app/_layout.js` : `[ROUTING] Mounted RootLayout`
- `app/index.js` : Logs détaillés à chaque étape de `checkRouting`
- `app/onboarding/index.js` : `[ROUTING] Mounted OnboardingScreen (index)`
- `app/onboarding/profile-setup.js` : `[ROUTING] Mounted ProfileSetupScreen`
- `app/(tabs)/home.tsx` : `[ROUTING] Mounted Home`
- `app/(auth)/login.js` : `[ROUTING] Mounted LoginScreen`

Ces logs permettront de tracer exactement quel écran est monté en premier et dans quel ordre les redirections se produisent.

