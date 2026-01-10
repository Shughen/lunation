# Notes de Stabilisation - Routing

## Date : $(date)
## Branche : `stabilisation-parcours`

---

## 🔧 CORRECTIONS APPLIQUÉES

### 1. **app/_layout.js** - Suppression des Stack.Screen invalides ✅

**Problème** : 
- `<Stack.Screen name="(auth)" />` - Référence un groupe, pas une route concrète
- `<Stack.Screen name="onboarding" />` - Référence un dossier, pas une route concrète

**Solution** : 
- Supprimé ces deux Stack.Screen
- Conservé uniquement `index` et `(tabs)` qui sont des routes valides

**Résultat** : Les warnings "No route named (auth)" et "No route named onboarding" devraient disparaître.

---

### 2. **app/index.js** - Simplification du flux de routing ✅

**Problèmes** :
- Flux trop complexe avec vérification onboarding qui pouvait bloquer
- Boucle d'attente sur profileLoading pouvant bloquer indéfiniment
- `isChecking` pouvait rester à `true` en cas d'erreur

**Solutions** :
- **Simplification** : Redirection uniquement vers `/login` ou `/home` selon la session
- **Onboarding désactivé temporairement** : Plus de redirection automatique vers `/onboarding` au démarrage
- **Timeout réduit** : Attente profil limitée à 1 seconde (au lieu de 5)
- **Non-bloquant** : Le chargement du profil ne bloque plus le routing
- **Finally** : `isChecking` passe à `false` dans un `finally` pour garantir la sortie
- **Logs explicites** : Ajout de logs `[INDEX]` pour tracer le flux

**Nouveau flux** :
1. Si `!session` → `/login`
2. Si `session` → `/home`
3. Pas de vérification onboarding/profil au démarrage

---

## 📝 CHANGEMENTS DÉTAILLÉS

### Fichiers modifiés :

1. **app/_layout.js**
   - Supprimé : `<Stack.Screen name="(auth)" />`
   - Supprimé : `<Stack.Screen name="onboarding" />`
   - Conservé : `<Stack.Screen name="index" />` et `<Stack.Screen name="(tabs)" />`

2. **app/index.js**
   - Supprimé : Vérification `onboarding_completed` depuis AsyncStorage
   - Supprimé : Vérification `hasProfile` pour redirection vers `/profile`
   - Supprimé : Import `AsyncStorage` (non utilisé)
   - Ajouté : Utilisation de `session` depuis `authStore`
   - Ajouté : Logs explicites `[INDEX]`
   - Modifié : Timeout profil réduit à 1 seconde
   - Modifié : `isChecking` dans un `finally` pour garantir la sortie
   - Modifié : `profileLoading` retiré de la condition `isLoading` (non bloquant)

---

## 🎯 RÉSULTAT ATTENDU

### Logs attendus après `npx expo start` :

```
[ROUTING] Mounted RootLayout
[App] Initialisation de l'authentification...
[App] Chargement du profil au démarrage...
[INDEX] Mounted
[INDEX] Début checkRouting { authLoading: false, isAuthenticated: false, hasSession: false }
[INDEX] Pas de session → redirection vers /(auth)/login
```

OU (si connecté) :

```
[ROUTING] Mounted RootLayout
[App] Initialisation de l'authentification...
[App] Chargement du profil au démarrage...
[INDEX] Mounted
[INDEX] Début checkRouting { authLoading: false, isAuthenticated: true, hasSession: true }
[INDEX] Session détectée, chargement du profil...
[INDEX] Session détectée → redirection vers /(tabs)/home
```

### Warnings supprimés :
- ✅ `No route named "(auth)" exists in nested children` - **RÉSOLU**
- ✅ `No route named "onboarding" exists in nested children` - **RÉSOLU**

### Comportement :
- ✅ Plus de blocage au démarrage
- ✅ Redirection rapide vers login ou home
- ✅ Pas de boucle infinie

---

## ⚠️ ONBOARDING TEMPORAIREMENT DÉSACTIVÉ

**Note importante** : La redirection automatique vers `/onboarding` a été désactivée pour stabiliser le flux.

**Impact** : 
- Les utilisateurs ne seront plus redirigés automatiquement vers l'onboarding au démarrage
- L'onboarding reste accessible manuellement depuis le profil si nécessaire

**Pour réactiver** :
1. Vérifier que le flux de base fonctionne correctement
2. Réintégrer la vérification `onboarding_completed` dans `app/index.js`
3. Tester le parcours complet

---

## 🧪 TESTS À EFFECTUER

1. **Démarrage sans session** :
   - [ ] L'app redirige vers `/login`
   - [ ] Pas de blocage
   - [ ] Logs `[INDEX]` visibles

2. **Démarrage avec session** :
   - [ ] L'app redirige vers `/home`
   - [ ] Pas de blocage
   - [ ] Logs `[INDEX]` visibles

3. **Warnings** :
   - [ ] Plus de warnings "No route named (auth)"
   - [ ] Plus de warnings "No route named onboarding"

4. **Performance** :
   - [ ] Redirection rapide (< 2 secondes)
   - [ ] Pas de loader qui tourne indéfiniment

---

## 📋 PROCHAINES ÉTAPES

1. **Tester le flux de base** (login/home)
2. **Valider l'absence de warnings**
3. **Vérifier les logs dans la console**
4. **Réintégrer l'onboarding** si nécessaire (après validation)

---

**Branche** : `stabilisation-parcours`  
**Statut** : ✅ Corrections appliquées, prêt pour tests

