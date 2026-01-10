# Logique de Routing Déterministe - Branche `stabilisation-parcours`

## 📋 Résumé des Modifications

### Fichiers Modifiés

1. **`app/index.js`**
   - Réécriture complète de la logique de routing
   - Utilisation d'un `useRef` local (`hasRunRef`) pour éviter les appels multiples
   - Attente explicite de `authLoading === false` ET `profileLoading === false`
   - Récupération d'une vue stable du profil via `useProfileStore.getState()`
   - Logique déterministe basée sur la complétude du profil + `onboarding_completed`
   - Logs détaillés pour tracer toutes les décisions

2. **`stores/profileStore.js`**
   - Export de la fonction `isProfileComplete()` pour utilisation dans le routing
   - Ajout d'une vérification de null pour `profile` dans la fonction

---

## 🎯 Logique de Routing Déterministe

### Schéma de Décision

```
┌─────────────────────────────────────┐
│  Démarrage (app/index.js)          │
└──────────────┬──────────────────────┘
               │
               ▼
    ┌──────────────────────┐
    │ authLoading === true?│
    └──────────┬───────────┘
               │ Oui
               │ └─► Attendre...
               │
               │ Non
               ▼
    ┌──────────────────────┐
    │ Session Supabase ?   │
    └──────────┬───────────┘
               │ Non
               │ └─► /(auth)/login
               │
               │ Oui
               ▼
    ┌──────────────────────┐
    │ profileLoading ?      │
    └──────────┬───────────┘
               │ Oui
               │ └─► Charger profil + Attendre (max 3s)
               │
               │ Non
               ▼
    ┌──────────────────────┐
    │ Profil complet ?     │
    │ (name, birthDate,     │
    │  birthTime,           │
    │  birthPlace)          │
    └──────────┬───────────┘
               │ Non
               │ └─► /onboarding
               │
               │ Oui
               ▼
    ┌──────────────────────┐
    │ onboarding_completed │
    │ === 'true' ?         │
    └──────────┬───────────┘
               │ Non
               │ └─► /onboarding
               │
               │ Oui
               ▼
         /(tabs)/home
```

### Tableau des Décisions

| Session | Profil Complet | onboarding_completed | Route de Destination | Raison |
|---------|----------------|----------------------|---------------------|--------|
| ❌ Non | - | - | `/(auth)/login` | Pas de session Supabase |
| ✅ Oui | ❌ Non | - | `/onboarding` | Profil incomplet (champs manquants) |
| ✅ Oui | ✅ Oui | ❌ `!== 'true'` | `/onboarding` | Profil complet mais onboarding non terminé |
| ✅ Oui | ✅ Oui | ✅ `=== 'true'` | `/(tabs)/home` | Tout est OK |

### Critères de "Profil Complet"

Un profil est considéré comme **complet** si **TOUS** les champs suivants sont remplis :

- ✅ `name` : string non vide (après trim)
- ✅ `birthDate` : Date valide (non null)
- ✅ `birthTime` : Date valide (non null)
- ✅ `birthPlace` : string non vide (après trim)

**Fonction utilisée** : `isProfileComplete(profile)` depuis `stores/profileStore.js`

---

## 📝 Scénarios Utilisateur

### Scénario A : "Vrai nouveau compte"

**État initial :**
- Compte créé, première connexion
- Profil vide (pas de `name`, `birthDate`, `birthTime`, `birthPlace`)
- Pas de clé `onboarding_completed` dans AsyncStorage

**Comportement attendu :**
- ✅ Redirection vers `/onboarding` à chaque connexion
- ✅ Continuer jusqu'à ce que le profil soit complet ET que `onboarding_completed === 'true'`

**Logs attendus :**
```
[INDEX] checkRouting() - session=true authLoading=false profileLoading=false
[INDEX] Profil détecté : { name: '(vide)', birthDate: '(manquante)', ... }
[INDEX] onboarding_completed = null
[INDEX] Décision : redirection vers /onboarding (profil incomplet)
```

---

### Scénario B : "Onboarding terminé"

**État initial :**
- Utilisateur a complété l'onboarding jusqu'à l'écran de fin
- `onboarding_completed = 'true'` dans AsyncStorage
- Profil complet (tous les champs remplis)

**Comportement attendu :**
- ✅ Redirection directe vers `/(tabs)/home` à chaque redémarrage/reconnexion
- ✅ **Jamais** d'onboarding relancé tant que `onboarding_completed === 'true'`

**Logs attendus :**
```
[INDEX] checkRouting() - session=true authLoading=false profileLoading=false
[INDEX] Profil détecté : { name: 'John', birthDate: 'présente', ... }
[INDEX] onboarding_completed = true
[INDEX] Décision : redirection vers /(tabs)/home (profil complet + onboarding_completed === true)
```

---

### Scénario C : "Suppression de compte + reconnexion"

**État initial :**
- Utilisateur clique sur "Supprimer mon compte"
- `deleteAccount()` supprime :
  - Données Supabase (profiles, natal_charts, etc.)
  - Données locales AsyncStorage (dont `onboarding_completed`)
- Utilisateur se reconnecte avec le même email

**État après reconnexion :**
- ✅ Session Supabase OK (nouvelle session créée)
- ❌ Profil inexistant ou incomplet (supprimé de Supabase)
- ❌ Pas de clé `onboarding_completed` (supprimée d'AsyncStorage)

**Comportement attendu :**
- ✅ Redirection vers `/onboarding`
- ✅ Parcours utilisateur complet comme si c'était la première fois

**Logs attendus :**
```
[INDEX] checkRouting() - session=true authLoading=false profileLoading=false
[INDEX] Profil détecté : { name: '(vide)', birthDate: '(manquante)', ... }
[INDEX] onboarding_completed = null
[INDEX] Décision : redirection vers /onboarding (profil incomplet)
```

---

### Scénario D : "Profil partiellement rempli"

**État initial :**
- Session Supabase OK
- Profil avec seulement `name` et `birthDate` remplis
- `birthTime` et `birthPlace` manquants
- `onboarding_completed` peut être `'true'` ou non

**Comportement attendu :**
- ✅ Redirection vers `/onboarding` (profil incomplet)
- ✅ **Peu importe** la valeur de `onboarding_completed` si le profil n'est pas complet

**Logs attendus :**
```
[INDEX] Profil détecté : { name: 'John', birthDate: 'présente', birthTime: '(manquante)', birthPlace: '(vide)' }
[INDEX] onboarding_completed = true (ou null)
[INDEX] Décision : redirection vers /onboarding (profil incomplet)
```

---

## 🔍 Logs de Debug

### Format des Logs

Tous les logs suivent le préfixe `[INDEX]` pour faciliter le filtrage :

1. **Au démarrage du checkRouting :**
   ```
   [INDEX] checkRouting() - session=true authLoading=false profileLoading=false
   ```

2. **État du profil :**
   ```
   [INDEX] Profil détecté : { name: 'John', birthDate: 'présente', birthTime: 'présente', birthPlace: 'Paris', isComplete: true }
   ```

3. **Valeur onboarding_completed :**
   ```
   [INDEX] onboarding_completed = true
   ```

4. **Décision finale :**
   ```
   [INDEX] Décision : redirection vers /onboarding (profil incomplet)
   [INDEX] Décision : redirection vers /onboarding (profil complet mais onboarding non terminé)
   [INDEX] Décision : redirection vers /(tabs)/home (profil complet + onboarding_completed === true)
   ```

---

## ✅ Tests Manuels à Effectuer

### Test 1 : Nouveau compte (première connexion)

1. Créer un nouveau compte via `/(auth)/signup`
2. Se connecter
3. **Vérifier** : Redirection vers `/onboarding`
4. **Vérifier les logs** : `[INDEX] Décision : redirection vers /onboarding (profil incomplet)`
5. Compléter l'onboarding jusqu'à la fin
6. **Vérifier** : `onboarding_completed = 'true'` dans AsyncStorage
7. Redémarrer l'app
8. **Vérifier** : Redirection directe vers `/(tabs)/home`

---

### Test 2 : Reconnexion (onboarding déjà terminé)

1. Se déconnecter
2. Se reconnecter avec un compte qui a déjà complété l'onboarding
3. **Vérifier** : Redirection directe vers `/(tabs)/home`
4. **Vérifier les logs** : `[INDEX] Décision : redirection vers /(tabs)/home (profil complet + onboarding_completed === true)`
5. Répéter plusieurs fois (déconnexion/reconnexion)
6. **Vérifier** : Comportement **toujours identique** (pas d'aléatoire)

---

### Test 3 : Suppression de compte + reconnexion

1. Se connecter avec un compte existant
2. Aller dans Profil → "Supprimer mon compte"
3. Confirmer la suppression
4. **Vérifier** : Redirection vers `/(auth)/login`
5. Se reconnecter avec le **même email**
6. **Vérifier** : Redirection vers `/onboarding` (comme première connexion)
7. **Vérifier les logs** : `[INDEX] Décision : redirection vers /onboarding (profil incomplet)`

---

### Test 4 : Profil partiellement rempli

1. Se connecter avec un compte
2. Aller dans Profil et remplir seulement :
   - Nom : "Test"
   - Date de naissance : 01/01/1990
   - **Ne PAS** remplir l'heure et le lieu
3. Sauvegarder
4. Redémarrer l'app
5. **Vérifier** : Redirection vers `/onboarding` (profil incomplet)
6. **Vérifier les logs** : `[INDEX] Décision : redirection vers /onboarding (profil incomplet)`

---

### Test 5 : Profil complet mais onboarding_completed manquant

1. Se connecter avec un compte
2. Remplir complètement le profil (nom, date, heure, lieu)
3. **Manuellement** supprimer la clé `onboarding_completed` d'AsyncStorage (via debug)
4. Redémarrer l'app
5. **Vérifier** : Redirection vers `/onboarding`
6. **Vérifier les logs** : `[INDEX] Décision : redirection vers /onboarding (profil complet mais onboarding non terminé)`

---

### Test 6 : Déterministe (pas d'aléatoire)

1. Se connecter avec un compte qui a complété l'onboarding
2. Noter la route de destination
3. Redémarrer l'app **10 fois de suite**
4. **Vérifier** : Même route à chaque fois (`/(tabs)/home`)
5. **Vérifier les logs** : Même séquence de logs à chaque fois
6. Répéter avec un compte sans onboarding
7. **Vérifier** : Même route à chaque fois (`/onboarding`)

---

## 🔧 Points Techniques Importants

### Éviter les Race Conditions

- ✅ `useRef` local (`hasRunRef`) pour éviter les appels multiples
- ✅ Attente explicite de `profileLoading === false` avant de prendre une décision
- ✅ Récupération d'une vue stable via `useProfileStore.getState()` (pas via les props réactives)
- ✅ `profileLoading` retiré des dépendances du `useEffect` pour éviter les boucles

### Gestion des Timeouts

- Timeout de 3 secondes maximum pour le chargement du profil
- Si timeout atteint, continuation avec l'état actuel du profil
- Log d'avertissement en cas de timeout

### Clés AsyncStorage

- **`onboarding_completed`** : clé principale pour déterminer si l'onboarding est terminé
  - Valeur attendue : `'true'` (string)
  - Définie dans : `app/onboarding/index.js` (skip) et `app/onboarding/disclaimer.js` (fin)
  - Supprimée dans : `lib/services/accountDeletionService.js`

---

## 📊 Résumé des Décisions de Routing

| Condition | Route | Priorité |
|-----------|-------|----------|
| Pas de session | `/(auth)/login` | 1 (priorité absolue) |
| Profil incomplet | `/onboarding` | 2 (priorité haute) |
| Profil complet + `onboarding_completed !== 'true'` | `/onboarding` | 3 |
| Profil complet + `onboarding_completed === 'true'` | `/(tabs)/home` | 4 |

**Note** : Les conditions sont évaluées dans cet ordre. La première condition vraie détermine la route.

---

## 🐛 Dépannage

### Problème : Toujours redirigé vers onboarding même après avoir complété

**Vérifier :**
1. La clé `onboarding_completed` est-elle bien à `'true'` dans AsyncStorage ?
2. Le profil est-il vraiment complet (tous les 4 champs remplis) ?
3. Les logs montrent-ils quelle décision est prise ?

### Problème : Comportement aléatoire (parfois onboarding, parfois home)

**Vérifier :**
1. Le flag `hasRunRef.current` est-il bien mis à `true` après la première exécution ?
2. Y a-t-il des re-renders qui déclenchent plusieurs fois le `useEffect` ?
3. Les logs montrent-ils plusieurs exécutions de `checkRouting()` ?

### Problème : Blocage sur le loader

**Vérifier :**
1. `authLoading` ou `profileLoading` restent-ils à `true` ?
2. Y a-t-il une erreur dans les logs qui empêche `setIsChecking(false)` ?
3. Le timeout de 3 secondes est-il atteint ?

---

## 📌 Notes de Développement

- La fonction `isProfileComplete()` est maintenant exportée depuis `profileStore.js` pour être réutilisable
- Le flag global `hasCheckedRouting` a été remplacé par un `useRef` local pour éviter les problèmes de persistance entre les remontages
- Les logs sont structurés pour faciliter le débogage et la compréhension du flux

