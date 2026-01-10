# Analyse Complète - Fonctionnement de l'Onboarding

## Date : $(date)
## Branche : `stabilisation-parcours`

---

## 1️⃣ FLUX DE DÉMARRAGE

### 📍 Route initiale au démarrage

**Réponse** : L'app démarre sur `app/index.js` (route `index`)

**Flux exact** :

1. **`app/_layout.js`** (RootLayout)
   - Initialise l'authentification via `initializeAuth()`
   - Charge le profil via `loadProfile()`
   - Charge les cycles et révolutions lunaires
   - Configure le Stack Navigator avec seulement `index` et `(tabs)`

2. **`app/index.js`** (Point d'entrée)
   - Vérifie l'état d'authentification
   - **Si `!session`** → Redirige vers `/(auth)/login`
   - **Si `session`** → Redirige vers `/(tabs)/home`
   - **PAS de vérification onboarding/profil** dans cette version

**Conclusion** : On arrive soit sur `/login` soit sur `/home`, **jamais directement sur l'onboarding**.

---

## 2️⃣ REDIRECTION AUTOMATIQUE VERS ONBOARDING

### ❌ NON - Plus de redirection automatique

**Dans la version actuelle de `stabilisation-parcours`** :

- ✅ **Aucune redirection automatique** vers `/onboarding` au démarrage
- ✅ La vérification `onboarding_completed` a été **supprimée** de `app/index.js`
- ✅ Le routing est simplifié : uniquement `login` ou `home` selon la session

**Code dans `app/index.js` (lignes 55-67)** :
```javascript
// Décision de routing simplifiée
if (!isAuthenticated || !session) {
  router.replace('/(auth)/login');
  return;
}

// Session détectée → Home
router.replace('/(tabs)/home');
```

**Aucune mention de `/onboarding` dans le routing initial.**

---

## 3️⃣ ACCÈS MANUEL À L'ONBOARDING

### 🔍 Comment accéder aux écrans d'onboarding maintenant ?

**Réponse** : **Aucun accès direct depuis l'UI actuelle**

**Analyse** :
- ❌ Pas de bouton "Configurer mon thème natal" dans `app/(tabs)/profile.js`
- ❌ Pas de redirection vers `/onboarding` depuis le profil
- ❌ Pas de lien vers l'onboarding dans les settings

**Les écrans d'onboarding existent** mais ne sont **pas accessibles** depuis l'interface utilisateur dans la version actuelle.

**Pour y accéder** (manuellement) :
- Navigation directe : `router.push('/onboarding/index')` ou `/onboarding/profile-setup`
- Mais aucun bouton dans l'UI ne déclenche cette navigation

---

## 4️⃣ ORDRE DES ÉCRANS D'ONBOARDING

### 📋 Séquence complète (si déclenchée manuellement)

**Ordre d'enchaînement** :

1. **`/onboarding/index.js`** - Écran de bienvenue
   - 4 slides : Bienvenue, Comprends ton cycle, Écoute les astres, Journalise tes émotions
   - Bouton "Passer" → Marque `onboarding_completed = 'true'` et redirige vers `/(tabs)/home`
   - Bouton "Commencer" (dernier slide) → Redirige vers `/onboarding/profile-setup`

2. **`/onboarding/profile-setup.js`** - Étape 1/4
   - Saisie : Prénom + Date de naissance
   - Sauvegarde via `saveProfile()` dans AsyncStorage
   - Bouton "Suivant" → Redirige vers `/onboarding/consent`

3. **`/onboarding/consent.js`** - Étape 2/4
   - Consentement santé (OBLIGATOIRE) - RGPD
   - Consentement analytics (OPTIONNEL)
   - Sauvegarde dans AsyncStorage (`user_consent`)
   - Bouton "Continuer" → Redirige vers `/onboarding/cycle-setup`

4. **`/onboarding/cycle-setup.js`** - Étape 3/4
   - Saisie : Date dernières règles + Durée moyenne du cycle
   - Sauvegarde dans AsyncStorage (`cycle_config`)
   - Bouton "Suivant" → Redirige vers `/onboarding/tour`

5. **`/onboarding/tour.js`** - Étape 4/4
   - 3 slides de présentation des fonctionnalités
   - Bouton "Continuer" (dernier slide) → Redirige vers `/onboarding/disclaimer`

6. **`/onboarding/disclaimer.js`** - Dernière étape
   - Avertissements médicaux (non dispositif médical, pas de contraception, etc.)
   - Checkbox d'acceptation obligatoire
   - Bouton "Commencer à utiliser LUNA" → 
     - Marque `onboarding_completed = 'true'` dans AsyncStorage
     - Marque `disclaimer_accepted = 'true'`
     - Track analytics
     - Redirige vers `/(tabs)/home`

---

## 5️⃣ SUPPRESSION DE PROFIL + RECONNEXION

### 🔄 Scénario : Supprimer mon profil puis me reconnecter

**Question** : Est-ce que j'ai à nouveau le parcours utilisateur complet (onboarding) ?

### ❌ NON - Pas de nouveau parcours onboarding

**Explication détaillée** :

#### Étape 1 : Suppression du profil

Quand vous cliquez sur "Supprimer mon compte" dans `/settings/privacy` :

1. **AsyncStorage** : `AsyncStorage.clear()` → **TOUT est supprimé**
   - ✅ `onboarding_completed` est supprimé
   - ✅ `user_consent` est supprimé
   - ✅ `cycle_config` est supprimé
   - ✅ `@astroia_user_profile` est supprimé
   - ✅ Toutes les autres clés

2. **Supabase** : **RIEN n'est supprimé**
   - ❌ Le compte `auth.users` reste actif
   - ❌ Le profil dans `profiles` reste
   - ❌ Toutes les données restent

3. **Redirection** : `/(auth)/login`

#### Étape 2 : Reconnexion

Quand vous vous reconnectez avec le même compte :

1. **`app/index.js`** vérifie :
   - `isAuthenticated` → `true` (session Supabase toujours active)
   - `session` → existe (compte Supabase toujours actif)
   - **Résultat** : Redirige vers `/(tabs)/home`

2. **Pas de vérification** :
   - ❌ Pas de vérification `onboarding_completed` (supprimée du code)
   - ❌ Pas de vérification `hasProfile` (supprimée du code)
   - ❌ Pas de redirection vers `/onboarding`

#### Étape 3 : Chargement du profil

1. **`app/_layout.js`** appelle `loadProfile()`
2. **`profileStore.loadProfile()`** :
   - Cherche dans AsyncStorage → **VIDE** (tout supprimé)
   - **Ne cherche PAS** dans Supabase (pas de sync Supabase)
   - Résultat : `hasProfile = false`, profil vide

3. **L'utilisateur arrive sur `/home`** avec :
   - ✅ Session Supabase active
   - ❌ Profil local vide (`hasProfile = false`)
   - ❌ Pas de redirection vers onboarding

---

### 🎯 Pourquoi pas de nouveau parcours onboarding ?

**Raisons techniques** :

1. **`app/index.js` ne vérifie plus `onboarding_completed`**
   - Cette vérification a été supprimée lors de la stabilisation
   - Le routing est simplifié : session → home, pas de session → login

2. **Le profil Supabase existe toujours**
   - La suppression ne touche que AsyncStorage
   - Le compte Supabase reste actif
   - La session est donc toujours valide

3. **Pas de sync Supabase → AsyncStorage**
   - `profileStore.loadProfile()` charge uniquement depuis AsyncStorage
   - Même si le profil existe dans Supabase, il n'est pas chargé
   - Donc `hasProfile = false` mais pas de redirection

4. **Pas de logique de "première connexion"**
   - Aucune vérification pour détecter si c'est une première connexion
   - Aucune logique pour déclencher l'onboarding si le profil local est vide

---

## 📊 RÉSUMÉ VISUEL

### Flux de démarrage actuel

```
Démarrage app
    ↓
app/_layout.js (initialise auth + charge profil)
    ↓
app/index.js
    ↓
┌─────────────────┬─────────────────┐
│ !session        │ session         │
│                 │                 │
│ → /login        │ → /home         │
└─────────────────┴─────────────────┘
```

### Flux onboarding (si déclenché manuellement)

```
/onboarding/index
    ↓ (bouton "Commencer")
/onboarding/profile-setup (Étape 1/4)
    ↓ (bouton "Suivant")
/onboarding/consent (Étape 2/4)
    ↓ (bouton "Continuer")
/onboarding/cycle-setup (Étape 3/4)
    ↓ (bouton "Suivant")
/onboarding/tour (Étape 4/4)
    ↓ (bouton "Continuer")
/onboarding/disclaimer
    ↓ (bouton "Commencer")
/(tabs)/home
```

### Scénario suppression + reconnexion

```
Suppression compte
    ↓
AsyncStorage.clear() → TOUT supprimé
    ↓
Redirection → /login
    ↓
Reconnexion (même compte)
    ↓
Session Supabase toujours active
    ↓
app/index.js → session détectée
    ↓
Redirection → /home
    ↓
❌ PAS de redirection vers onboarding
❌ Profil local vide (hasProfile = false)
❌ Mais pas de logique pour déclencher onboarding
```

---

## 🔍 POINTS IMPORTANTS

### ✅ Ce qui fonctionne

- Les écrans d'onboarding existent et sont fonctionnels
- L'ordre d'enchaînement est correct
- La sauvegarde dans AsyncStorage fonctionne
- Le marquage `onboarding_completed` fonctionne

### ❌ Ce qui ne fonctionne pas / manque

- **Pas d'accès depuis l'UI** : Aucun bouton ne déclenche l'onboarding
- **Pas de redirection automatique** : Même si `onboarding_completed` n'existe pas, pas de redirection
- **Suppression incomplète** : Seul AsyncStorage est supprimé, pas Supabase
- **Pas de détection "première connexion"** : Pas de logique pour déclencher l'onboarding si profil vide

---

## 💡 RECOMMANDATIONS

Pour que l'onboarding fonctionne correctement :

1. **Ajouter un bouton dans `/profile`** pour déclencher l'onboarding manuellement
2. **Réintégrer la vérification `onboarding_completed`** dans `app/index.js` (optionnel)
3. **Ajouter une logique de détection** : Si `hasProfile = false` ET `onboarding_completed` n'existe pas → rediriger vers onboarding
4. **Corriger la suppression** : Supprimer aussi les données Supabase lors de la suppression de compte

---

**Conclusion** : L'onboarding existe mais n'est **pas accessible** depuis l'UI actuelle. Il faut soit le déclencher manuellement via navigation directe, soit ajouter un bouton dans l'interface.

