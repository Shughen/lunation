# Diagnostic de Stabilisation - Astro.IA

## Date : $(date)
## Branche : `stabilisation-parcours`

---

## 🔴 PROBLÈMES CRITIQUES IDENTIFIÉS

### 1. ROUTING - Incohérences et conflits

#### `app/index.js`
- ✅ **CORRIGÉ** : Code amélioré selon recommandations BugBot
- ⚠️ **PROBLÈME** : Charge le profil depuis AsyncStorage uniquement, pas de sync Supabase
- ⚠️ **PROBLÈME** : Boucle d'attente avec `while` peut être bloquante si `isLoading` reste `true`

#### `app/_layout.js`
- ⚠️ **PROBLÈME** : Charge le profil au démarrage, peut entrer en conflit avec `app/index.js`
- ⚠️ **PROBLÈME** : Pas de gestion d'erreur si `loadProfile()` échoue

#### `app/onboarding/profile-setup.js`
- 🔴 **BUG** : Utilise `updateProfile()` qui n'existe pas dans `profileStore`
- ⚠️ **PROBLÈME** : Devrait utiliser `saveProfile()` ou `updateField()`

#### `app/onboarding/index.js`
- ✅ **OK** : Définit `onboarding_completed` correctement

---

### 2. PROFILE STORE - Synchronisation Supabase manquante

#### `stores/profileStore.js`
- 🔴 **BUG CRITIQUE** : `loadProfile()` charge uniquement depuis AsyncStorage
- 🔴 **BUG CRITIQUE** : Pas de synchronisation avec Supabase
- ⚠️ **PROBLÈME** : `hasProfile` peut être `false` même si le profil existe dans Supabase
- ⚠️ **PROBLÈME** : `saveProfile()` sauvegarde uniquement dans AsyncStorage
- ⚠️ **PROBLÈME** : Pas d'utilisation de `profileService` pour sync Supabase

#### `lib/api/profileService.js`
- ✅ **OK** : Service bien structuré avec méthodes Supabase
- ⚠️ **PROBLÈME** : Service existe mais n'est pas utilisé dans `profileStore`

---

### 3. ASYNCSTORAGE - Clés incohérentes et doublons

#### Clés identifiées :

**Profil utilisateur :**
- `@astroia_user_profile` ✅ (utilisée dans profileStore)
- `user_profile` ⚠️ (utilisée dans exportService.js - DOUBLON)

**Thème natal :**
- `natal_chart_local` ✅ (utilisée dans natalService.js)
- `natal_chart_rapidapi` ⚠️ (utilisée dans natalServiceRapidAPI.js - alternative)

**Onboarding :**
- `onboarding_completed` ✅ (utilisée dans index.js et onboarding)

**Autres clés :**
- `@astroia_journal_entries` ✅
- `@profile_migrated_to_supabase` ✅
- `user_birth_data` ⚠️ (utilisée dans natal-reading - peut être obsolète)
- `natal_reading` ⚠️ (utilisée dans natal-reading)
- `cycle_config` ⚠️ (utilisée dans plusieurs services - peut être obsolète)

---

### 4. NATAL SERVICE - Gestion correcte mais à vérifier

#### `lib/api/natalService.js`
- ✅ **OK** : Gère bien le mode local et Supabase
- ✅ **OK** : Gestion d'erreurs correcte
- ⚠️ **PROBLÈME** : `canComputeToday()` retourne `true` en cas d'erreur (peut être intentionnel)

---

### 5. AUTH STORE - Nettoyage correct

#### `stores/authStore.js`
- ✅ **OK** : Nettoie correctement AsyncStorage lors de la déconnexion
- ✅ **OK** : Reset du profil dans le store

---

### 6. ERREURS ASYNC/AWAIT - Gestion manquante

#### Fichiers à vérifier :
- `app/_layout.js` : `loadProfile()` appelé sans `await` ni gestion d'erreur
- `app/index.js` : Boucle `while` peut bloquer indéfiniment
- `app/onboarding/profile-setup.js` : `updateProfile()` n'existe pas

---

### 7. IMPORTS - À vérifier

#### Fichiers suspects :
- `app/(tabs)/_layout.js` : Import `COLORS` au lieu de `colors` (incohérence)
- Vérifier tous les imports de stores et services

---

## 📋 PLAN DE CORRECTION

### Phase 1 : Corrections critiques (priorité absolue)
1. ✅ Corriger `app/onboarding/profile-setup.js` : remplacer `updateProfile()` par `saveProfile()`
2. ✅ Améliorer `app/index.js` : ajouter timeout à la boucle d'attente
3. ✅ Ajouter gestion d'erreur dans `app/_layout.js`
4. ✅ Synchroniser `profileStore` avec Supabase via `profileService`

### Phase 2 : Stabilisation AsyncStorage
5. ✅ Standardiser les clés AsyncStorage
6. ✅ Nettoyer les clés obsolètes
7. ✅ Documenter toutes les clés utilisées

### Phase 3 : Amélioration routing
8. ✅ Clarifier la logique de routing entre `_layout.js` et `index.js`
9. ✅ Améliorer la gestion des états de chargement

### Phase 4 : Tests et validation
10. ✅ Tester le parcours complet : login → onboarding → profil → thème natal
11. ✅ Vérifier la synchronisation Supabase
12. ✅ Valider la suppression de compte

---

## 🎯 PRIORITÉS

1. **CRITIQUE** : Fixer `updateProfile()` dans profile-setup.js
2. **CRITIQUE** : Ajouter sync Supabase dans profileStore
3. **HAUTE** : Standardiser les clés AsyncStorage
4. **HAUTE** : Améliorer la gestion d'erreurs
5. **MOYENNE** : Optimiser le routing

---

## 📝 NOTES

- Ne pas supprimer de code sans validation
- Tester chaque correction individuellement
- Commiter chaque étape avec message clair

