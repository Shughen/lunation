# Logique de Routing Onboarding - LUNA

## Date : $(date)
## Fichier principal : `app/index.js`

---

## 📋 VUE D'ENSEMBLE

Le routing initial de l'application vérifie maintenant l'état d'onboarding pour rediriger l'utilisateur vers le bon écran au démarrage.

**Clé AsyncStorage** : `onboarding_completed` (valeur : `'true'`)

---

## 🔄 FLUX DE ROUTING

### Schéma textuel

```
Démarrage app
    ↓
app/index.js
    ↓
┌─────────────────────────────────────┐
│ Vérification session Supabase       │
└─────────────────────────────────────┘
    ↓
┌──────────────┬──────────────────────┐
│ !session     │ session              │
│              │                      │
│ → /login     │ ↓                    │
└──────────────┘ │                     │
                 │ Lire                │
                 │ onboarding_completed│
                 │                      │
                 ↓                      │
        ┌────────┴────────┐            │
        │                 │            │
   !== 'true'        === 'true'        │
        │                 │            │
        ↓                 ↓            │
   /onboarding      /(tabs)/home       │
   /index                               │
```

---

## 📊 DÉCISIONS DE ROUTING

### 1. Pas de session Supabase

**Condition** : `!isAuthenticated || !session`

**Action** : Redirection vers `/(auth)/login`

**Log** : `[INDEX] Pas de session → redirection vers /(auth)/login`

---

### 2. Session Supabase + Onboarding non terminé

**Condition** : 
- `isAuthenticated && session`
- `onboarding_completed !== 'true'` (clé absente, `null`, ou autre valeur)

**Action** : Redirection vers `/onboarding/index`

**Log** : `[INDEX] Redirection vers /onboarding/index (première connexion ou onboarding non terminé)`

**Cas d'usage** :
- Première connexion (utilisateur vient de créer un compte)
- Onboarding non terminé (utilisateur a quitté l'app avant la fin)
- Après suppression de compte + reconnexion (AsyncStorage vidé)

---

### 3. Session Supabase + Onboarding terminé

**Condition** :
- `isAuthenticated && session`
- `onboarding_completed === 'true'`

**Action** : Redirection vers `/(tabs)/home`

**Log** : `[INDEX] Redirection vers /(tabs)/home (onboarding déjà complété)`

---

### 4. Erreur de lecture AsyncStorage

**Condition** : Exception lors de `AsyncStorage.getItem('onboarding_completed')`

**Action** : Redirection vers `/onboarding/index` (sécurité - considérer comme première connexion)

**Log** : `[INDEX] Erreur lecture onboarding_completed: ...` puis `[INDEX] Erreur lecture onboarding → redirection vers /onboarding/index`

---

## 🔑 CLÉS ASYNCSTORAGE

### `onboarding_completed`

**Type** : `string`  
**Valeur** : `'true'` (quand terminé)

**Définie dans** :
1. `app/onboarding/index.js` ligne 83
   - Bouton "Passer" → `AsyncStorage.setItem('onboarding_completed', 'true')`
   - Redirection vers `/(tabs)/home`

2. `app/onboarding/disclaimer.js` ligne 33
   - Fin de l'onboarding → `AsyncStorage.setItem('onboarding_completed', 'true')`
   - Redirection vers `/(tabs)/home`

**Supprimée dans** :
- `lib/services/accountDeletionService.js` (fonction `cleanupLocalData()`)
  - Clé dans la liste `keysToRemove`
  - Supprimée lors de `deleteAccount()`

---

## 📝 SCÉNARIOS D'UTILISATION

### Scénario 1 : Première connexion

**Étapes** :
1. Utilisateur crée un compte (`app/(auth)/signup.js`)
2. Session Supabase créée
3. `app/index.js` vérifie `onboarding_completed`
4. Clé absente → Redirection vers `/onboarding/index`
5. Utilisateur complète l'onboarding
6. `onboarding_completed = 'true'` défini dans `disclaimer.js`
7. Redirection vers `/(tabs)/home`

**Résultat** : ✅ Utilisateur passe par l'onboarding avant d'accéder à l'app

---

### Scénario 2 : Reconnexion simple

**Étapes** :
1. Utilisateur se connecte (`app/(auth)/login.js` ou `verify-otp.js`)
2. Session Supabase récupérée
3. `app/index.js` vérifie `onboarding_completed`
4. Clé existe et vaut `'true'` → Redirection vers `/(tabs)/home`

**Résultat** : ✅ Utilisateur accède directement à l'app (onboarding déjà fait)

---

### Scénario 3 : Suppression de compte + Reconnexion

**Étapes** :
1. Utilisateur clique "Supprimer mon compte" (`app/(tabs)/profile.js`)
2. `deleteAccount()` appelé (`lib/services/accountDeletionService.js`)
3. `cleanupLocalData()` supprime toutes les clés AsyncStorage (dont `onboarding_completed`)
4. Utilisateur déconnecté
5. Utilisateur se reconnecte avec le même compte
6. Session Supabase récupérée (compte toujours actif dans `auth.users`)
7. `app/index.js` vérifie `onboarding_completed`
8. Clé absente (supprimée) → Redirection vers `/onboarding/index`

**Résultat** : ✅ Utilisateur repasse par l'onboarding (comportement "première connexion")

**Note** : Le compte Supabase (`auth.users`) reste actif, mais toutes les données locales sont supprimées. L'utilisateur doit refaire l'onboarding pour configurer son profil local.

---

### Scénario 4 : Onboarding interrompu

**Étapes** :
1. Utilisateur commence l'onboarding (`/onboarding/index`)
2. Utilisateur quitte l'app avant la fin (pas de `onboarding_completed = 'true'`)
3. Utilisateur relance l'app
4. Session Supabase toujours active
5. `app/index.js` vérifie `onboarding_completed`
6. Clé absente ou différente de `'true'` → Redirection vers `/onboarding/index`

**Résultat** : ✅ Utilisateur reprend l'onboarding depuis le début

---

## 🔧 IMPLÉMENTATION TECHNIQUE

### Fichier : `app/index.js`

**Modifications** :
1. Import `AsyncStorage`
2. Vérification `onboarding_completed` après vérification de session
3. Logs détaillés pour chaque décision
4. Gestion d'erreur avec fallback vers onboarding

**Code clé** :
```javascript
// Session détectée → Vérifier l'onboarding
const onboardingCompleted = await AsyncStorage.getItem('onboarding_completed');

if (onboardingCompleted !== 'true') {
  // Redirection vers onboarding
  router.replace('/onboarding/index');
} else {
  // Redirection vers home
  router.replace('/(tabs)/home');
}
```

**Préservation** :
- ✅ Logique de stabilisation conservée (`isChecking`, timeout profil, etc.)
- ✅ Gestion d'erreurs existante préservée
- ✅ Logs existants conservés

---

## 📊 LOGS DE DEBUG

### Séquence de logs attendue

**Première connexion** :
```
[INDEX] Mounted
[INDEX] Début checkRouting { authLoading: false, isAuthenticated: true, hasSession: true }
[INDEX] Session détectée, chargement du profil...
[INDEX] Session détectée, vérification onboarding_completed...
[INDEX] onboarding_completed = null
[INDEX] Redirection vers /onboarding/index (première connexion ou onboarding non terminé)
```

**Reconnexion (onboarding terminé)** :
```
[INDEX] Mounted
[INDEX] Début checkRouting { authLoading: false, isAuthenticated: true, hasSession: true }
[INDEX] Session détectée, chargement du profil...
[INDEX] Session détectée, vérification onboarding_completed...
[INDEX] onboarding_completed = true
[INDEX] Redirection vers /(tabs)/home (onboarding déjà complété)
```

**Après suppression de compte + reconnexion** :
```
[INDEX] Mounted
[INDEX] Début checkRouting { authLoading: false, isAuthenticated: true, hasSession: true }
[INDEX] Session détectée, chargement du profil...
[INDEX] Session détectée, vérification onboarding_completed...
[INDEX] onboarding_completed = null
[INDEX] Redirection vers /onboarding/index (première connexion ou onboarding non terminé)
```

---

## ✅ VALIDATION

### Tests manuels à effectuer

1. **Première connexion** :
   - Créer un nouveau compte
   - Vérifier redirection vers `/onboarding/index`
   - Compléter l'onboarding
   - Vérifier redirection vers `/(tabs)/home`

2. **Reconnexion simple** :
   - Se déconnecter
   - Se reconnecter
   - Vérifier redirection directe vers `/(tabs)/home` (pas d'onboarding)

3. **Suppression de compte + reconnexion** :
   - Supprimer le compte depuis Profil
   - Se reconnecter avec le même compte
   - Vérifier redirection vers `/onboarding/index` (onboarding à refaire)

4. **Onboarding interrompu** :
   - Commencer l'onboarding
   - Quitter l'app avant la fin
   - Relancer l'app
   - Vérifier redirection vers `/onboarding/index`

5. **Pas de session** :
   - Se déconnecter
   - Relancer l'app
   - Vérifier redirection vers `/(auth)/login`

---

## 🔒 CONTRAINTES RESPECTÉES

- ✅ Pas de `<Stack.Screen name="(auth)" />` ou `<Stack.Screen name="onboarding" />` dans `app/_layout.js`
- ✅ Utilisation de `router.replace(...)` (API Expo Router)
- ✅ Logique de stabilisation préservée
- ✅ Même clé `onboarding_completed` que dans les fichiers d'onboarding
- ✅ Service `accountDeletionService` non modifié

---

## 📝 NOTES IMPORTANTES

### Comportement après suppression de compte

**Important** : Après suppression de compte, l'utilisateur doit repasser par l'onboarding car :
- AsyncStorage est vidé (dont `onboarding_completed`)
- Le profil local est supprimé
- Mais le compte Supabase (`auth.users`) reste actif

C'est le comportement attendu : l'utilisateur repart "à zéro" côté app locale, mais peut se reconnecter avec le même compte.

---

### Synchronisation avec onboarding

La clé `onboarding_completed` est définie dans :
- `app/onboarding/index.js` (bouton "Passer")
- `app/onboarding/disclaimer.js` (fin normale de l'onboarding)

**Valeur** : Toujours `'true'` (string)

**Vérification** : `onboarding_completed !== 'true'` (strict, pour gérer `null`, `undefined`, ou valeurs invalides)

---

**Conclusion** : Le routing onboarding est maintenant réactivé et intégré dans le flux de démarrage, tout en préservant la logique de stabilisation existante.

