# Diagnostic QA - Parcours Utilisateur

## Date : $(date)
## Branche : `stabilisation-parcours`

---

## 📋 MÉTHODOLOGIE

Analyse des flux utilisateur basée sur le code source (sans exécution de l'app). Pour chaque flux :
- **Comportement ATTENDU** : Ce qui serait logique pour l'utilisateur
- **Comportement RÉEL** : Ce que le code fait actuellement
- **Incohérences** : Problèmes identifiés

---

## 1️⃣ PREMIÈRE OUVERTURE SANS COMPTE

### Comportement ATTENDU
- L'app démarre et affiche un écran de login/inscription
- L'utilisateur peut créer un compte ou se connecter
- Pas de redirection vers l'onboarding automatique (l'onboarding doit être déclenché manuellement)

### Comportement RÉEL
**Fichier** : `app/index.js`

1. `app/_layout.js` initialise l'auth et charge le profil
2. `app/index.js` vérifie la session :
   - Si `!session` → Redirige vers `/(auth)/login` ✅
   - Si `session` → Redirige vers `/(tabs)/home` ✅
3. **PAS de vérification `onboarding_completed`** (supprimée lors de la stabilisation)

### ✅ Comportement OK
- Redirection correcte vers login si pas de session
- Pas de blocage sur un loader infini
- Gestion d'erreurs avec fallback vers login

### ⚠️ Points à améliorer
- **Pas de détection "première connexion"** : Si l'utilisateur crée un compte, il arrive directement sur `/home` sans passer par l'onboarding
- **Pas de logique pour déclencher l'onboarding** si le profil est vide après connexion

### 🐛 Bugs probables
- **Fichier** : `app/index.js` lignes 55-66
- **Problème** : Un utilisateur qui crée un compte arrive sur `/home` avec un profil vide, mais aucun mécanisme ne le guide vers l'onboarding
- **Impact** : L'utilisateur peut utiliser l'app sans avoir configuré son profil

---

## 2️⃣ CRÉATION DE COMPTE / LOGIN

### Comportement ATTENDU
- L'utilisateur peut créer un compte avec email + mot de passe
- L'utilisateur peut se connecter avec OTP (email sans mot de passe)
- Après connexion réussie, redirection vers `/home`
- Si c'est une première connexion, proposition d'onboarding

### Comportement RÉEL

#### A. Création de compte (`app/(auth)/signup.js`)
1. Formulaire email + password + confirm password
2. Validation du formulaire
3. Appel `signUp(email, password)`
4. Si session créée → Alert + redirection vers `/home`
5. Si confirmation email requise → Alert + redirection vers `/login`

#### B. Login OTP (`app/(auth)/login.js`)
1. Formulaire email uniquement
2. Appel `signInWithOTP(email)`
3. Redirection vers `/(auth)/verify-otp` avec email en paramètre
4. Saisie du code à 6 chiffres
5. Appel `verifyOTP(email, code)`
6. Si succès → Alert + redirection automatique via `useEffect` qui surveille `isAuthenticated`

#### C. Login avec mot de passe
- **Non implémenté** dans l'UI actuelle (seul OTP est disponible)

### ✅ Comportement OK
- Flux OTP fonctionnel
- Gestion des erreurs avec Alert
- Redirection automatique après connexion
- Bouton "Continuer sans compte" disponible (mode local)

### ⚠️ Points à améliorer
- **Pas de login avec mot de passe** : Seul OTP est disponible dans l'UI
- **Pas de vérification profil après connexion** : L'utilisateur arrive sur `/home` même si le profil est vide
- **Bouton "Continuer sans compte"** : Permet d'accéder à l'app sans compte, mais le profil ne sera pas sauvegardé

### 🐛 Bugs probables
- **Fichier** : `app/(auth)/signup.js` lignes 86-103
- **Problème** : La redirection vers `/home` se fait même si le profil est vide. Aucune logique pour déclencher l'onboarding
- **Fichier** : `app/(auth)/verify-otp.js` lignes 32-36
- **Problème** : Redirection automatique vers `/home` sans vérifier si le profil existe
- **Impact** : L'utilisateur peut arriver sur `/home` avec un profil vide et ne pas savoir comment configurer son profil

---

## 3️⃣ PARCOURS D'ONBOARDING

### Comportement ATTENDU
- L'onboarding doit être accessible depuis le profil ou proposé après création de compte
- Séquence : Bienvenue → Profil (nom + date) → Consentements → Cycle → Tour → Disclaimer
- Après l'onboarding, redirection vers `/home` avec profil configuré

### Comportement RÉEL

**Fichiers** : `app/onboarding/*`

**Séquence** :
1. `/onboarding/index.js` - 4 slides de bienvenue
   - Bouton "Passer" → Marque `onboarding_completed = 'true'` → `/home`
   - Bouton "Commencer" → `/onboarding/profile-setup`
2. `/onboarding/profile-setup.js` - Prénom + Date de naissance
   - Sauvegarde via `saveProfile()` → `/onboarding/consent`
3. `/onboarding/consent.js` - Consentements RGPD
   - Sauvegarde dans AsyncStorage → `/onboarding/cycle-setup`
4. `/onboarding/cycle-setup.js` - Date règles + Durée cycle
   - Sauvegarde dans AsyncStorage → `/onboarding/tour`
5. `/onboarding/tour.js` - 3 slides fonctionnalités
   - → `/onboarding/disclaimer`
6. `/onboarding/disclaimer.js` - Avertissements médicaux
   - Marque `onboarding_completed = 'true'` → `/home`

**Problème majeur** : **Aucun accès depuis l'UI** ❌
- Pas de bouton dans `/profile` pour déclencher l'onboarding
- Pas de redirection automatique vers l'onboarding après création de compte
- L'onboarding existe mais n'est pas accessible

### ✅ Comportement OK
- Séquence d'écrans bien structurée
- Sauvegarde des données dans AsyncStorage
- Marquage `onboarding_completed` à la fin

### ⚠️ Points à améliorer
- **Pas d'accès depuis l'UI** : Aucun bouton ne déclenche l'onboarding
- **Pas de redirection automatique** : Même si `onboarding_completed` n'existe pas, pas de redirection
- **Profil partiel** : L'onboarding sauvegarde seulement nom + date, pas le lieu de naissance ni l'heure

### 🐛 Bugs probables
- **Fichier** : `app/(tabs)/profile.js`
- **Problème** : Aucun bouton "Configurer mon thème natal" ou "Commencer l'onboarding"
- **Fichier** : `app/index.js`
- **Problème** : Pas de vérification `onboarding_completed` pour rediriger vers l'onboarding
- **Fichier** : `app/onboarding/profile-setup.js` ligne 36
- **Problème** : Sauvegarde seulement `name` et `birthDate`, pas `birthTime` ni `birthPlace`
- **Impact** : L'onboarding ne configure pas un profil complet pour le thème natal

---

## 4️⃣ CALCUL ET AFFICHAGE DU THÈME NATAL

### Comportement ATTENDU
- L'utilisateur accède au thème natal depuis `/home` ou `/profile`
- Si le profil est incomplet (pas de lieu de naissance), affichage d'un message pour compléter
- Calcul du thème natal avec les données du profil
- Affichage de la carte du ciel, positions planétaires, signes (Soleil, Lune, Ascendant)
- Sauvegarde automatique des signes dans le profil

### Comportement RÉEL

**Fichier** : `app/natal-chart/index.js`

1. **Vérifications** :
   - Si `!hasProfile` → Affiche empty state + bouton vers `/profile` ✅
   - Si `!profile.latitude || !profile.longitude` → Alert + redirection vers `/profile` ✅

2. **Calcul** :
   - Toggle entre RapidAPI et API V1
   - Appel `computeNatalChartForCurrentUser()` avec données du profil
   - Sauvegarde automatique des signes via `autoSaveToProfile()`
   - Synchronisation automatique du profil via `syncFromNatalChart()`

3. **Affichage** :
   - Carte circulaire du zodiaque
   - Positions planétaires (Soleil, Lune, Ascendant, Mercure, Vénus, Mars)
   - Bouton "Sauvegarder dans mon profil" (si pas déjà sauvegardé)

### ✅ Comportement OK
- Vérifications de profil complet avant calcul
- Gestion des erreurs avec Alert
- Sauvegarde automatique des signes
- Toggle entre RapidAPI et API V1

### ⚠️ Points à améliorer
- **Profil partiel** : Si l'utilisateur n'a que `name` et `birthDate` (depuis l'onboarding), il ne peut pas calculer le thème natal (manque lieu + heure)
- **Pas de guidance** : Si le profil est incomplet, l'utilisateur est redirigé vers `/profile` mais pas guidé sur ce qui manque
- **Synchronisation** : La fonction `syncFromNatalChart()` est appelée mais peut échouer silencieusement

### 🐛 Bugs probables
- **Fichier** : `app/natal-chart/index.js` lignes 57-64
- **Problème** : Vérifie seulement `latitude` et `longitude`, mais pas `birthTime` qui est aussi requis pour le calcul
- **Fichier** : `app/natal-chart/index.js` lignes 87-94
- **Problème** : `syncFromNatalChart(null)` est appelé avec `null` au lieu du résultat du calcul
- **Impact** : La synchronisation peut échouer ou ne pas fonctionner correctement

---

## 5️⃣ ACCÈS À LA "RÉVOLUTION LUNAIRE" / "CYCLE LUNAIRE"

### Comportement ATTENDU
- L'utilisateur accède à la révolution lunaire depuis `/home` (carte LunarRevolutionHero)
- Si le profil est incomplet (pas de date/heure de naissance), affichage d'un message pour configurer
- Calcul automatique de la révolution du mois actuel
- Navigation vers mois précédent/suivant
- Affichage des aspects et interprétations

### Comportement RÉEL

**Fichier** : `app/lunar-revolution/index.tsx`

1. **Vérifications** :
   - Si `!profile.birthDate || !profile.birthTime` → Affiche empty state + bouton vers `/natal-reading` ✅

2. **Chargement** :
   - `useEffect` appelle `fetchForMonth(new Date())` si profil complet
   - Le store vérifie le cache avant de faire un appel API

3. **Affichage** :
   - Carte principale avec révolution du mois
   - Liste des aspects
   - Navigation mois précédent/suivant

**Fichier** : `app/(tabs)/home.tsx`

- Carte `LunarRevolutionHero` affichée en haut
- Appel `fetchForMonth()` si profil complet (lignes 50-65)
- Bouton vers `/lunar-revolution` sur la carte

### ✅ Comportement OK
- Vérification du profil avant chargement
- Gestion du cache dans le store
- Navigation entre mois
- Affichage conditionnel sur `/home`

### ⚠️ Points à améliorer
- **Redirection** : Si profil incomplet, redirige vers `/natal-reading` au lieu de `/profile` (incohérence)
- **Chargement** : Le chargement se fait même si le profil n'a pas de `birthPlace` (seulement `birthDate` et `birthTime` requis)

### 🐛 Bugs probables
- **Fichier** : `app/lunar-revolution/index.tsx` ligne 71
- **Problème** : Redirige vers `/natal-reading` au lieu de `/profile` pour configurer le thème natal
- **Fichier** : `app/(tabs)/home.tsx` ligne 52
- **Problème** : Vérifie `profile.birthPlace` mais ce n'est pas requis pour la révolution lunaire (seulement `birthDate` et `birthTime`)
- **Impact** : L'utilisateur peut ne pas pouvoir accéder à la révolution lunaire même si `birthDate` et `birthTime` sont renseignés

---

## 6️⃣ CONSULTATION DU PROFIL

### Comportement ATTENDU
- L'utilisateur accède au profil depuis l'onglet "Profil"
- Affichage des informations du profil (nom, date, lieu, heure, signes)
- Possibilité de modifier les informations
- Indicateur de complétion du profil
- Bouton pour configurer le thème natal si incomplet

### Comportement RÉEL

**Fichier** : `app/(tabs)/profile.js`

1. **Chargement** :
   - `loadProfile()` au montage
   - Synchronisation avec le store

2. **Affichage** :
   - Avatar + nom
   - Indicateur de complétion (`getCompletionPercentage()`)
   - Champs : Date de naissance, Heure, Lieu
   - Bouton "Valider le lieu" pour géocodage
   - Bouton "Créer/Enregistrer mon profil"
   - Bouton "Voir mon profil complet" (si `hasProfile`)
   - Bouton "Paramètres"

3. **Sauvegarde** :
   - Validation du profil via `validateProfile()`
   - Sauvegarde via `saveProfile()`

### ✅ Comportement OK
- Chargement du profil au montage
- Indicateur de complétion
- Géocodage du lieu de naissance
- Validation avant sauvegarde

### ⚠️ Points à améliorer
- **Pas de bouton onboarding** : Aucun bouton pour déclencher l'onboarding depuis le profil
- **Pas de guidance** : Si le profil est incomplet, pas de message clair indiquant ce qui manque
- **Pas de lien vers thème natal** : Pas de bouton direct vers `/natal-chart` pour calculer le thème

### 🐛 Bugs probables
- **Fichier** : `app/(tabs)/profile.js` ligne 179
- **Problème** : `hasProfile` est calculé via `isProfileComplete()` mais cette fonction n'est pas visible dans le code analysé
- **Fichier** : `app/(tabs)/profile.js` lignes 85-131
- **Problème** : Le géocodage met à jour le profil mais ne vérifie pas si le profil est complet après
- **Impact** : L'utilisateur peut avoir un profil partiel sans savoir ce qui manque

---

## 7️⃣ SUPPRESSION DE PROFIL

### Comportement ATTENDU
- L'utilisateur peut supprimer son compte depuis les paramètres
- Double confirmation avant suppression
- Suppression de toutes les données (AsyncStorage + Supabase)
- Déconnexion automatique
- Redirection vers `/login`

### Comportement RÉEL

**Fichier** : `app/settings/privacy.js`

1. **Bouton "Supprimer mon compte"** :
   - Double confirmation (Alert 1 + Alert 2 avec texte "SUPPRIMER")
   - Appel `deleteAllUserData()`

**Fichier** : `lib/services/exportService.js`

2. **Fonction `deleteAllUserData()`** :
   - `AsyncStorage.clear()` → **Supprime TOUT AsyncStorage** ✅
   - **PAS de suppression Supabase** ❌
   - **PAS de déconnexion** ❌
   - Redirection vers `/(auth)/login` ✅

**Fichier** : `stores/authStore.js`

3. **Fonction `signOut()`** :
   - Appelle `supabaseSignOut()`
   - Supprime certaines clés AsyncStorage (pas tout)
   - Appelle `resetProfile()`
   - **MAIS** `deleteAllUserData()` n'appelle PAS `signOut()`

### ✅ Comportement OK
- Double confirmation avant suppression
- Suppression complète d'AsyncStorage
- Redirection vers login

### ⚠️ Points à améliorer
- **Suppression incomplète** : Seul AsyncStorage est supprimé, pas Supabase
- **Pas de déconnexion** : Le compte Supabase reste actif
- **Non-conformité RGPD** : Le droit à l'oubli n'est pas respecté (données Supabase non supprimées)

### 🐛 Bugs probables
- **Fichier** : `lib/services/exportService.js` fonction `deleteAllUserData()`
- **Problème** : `AsyncStorage.clear()` supprime tout, mais ne supprime pas les données Supabase (profiles, natal_charts, etc.)
- **Fichier** : `lib/services/exportService.js` ligne 161
- **Problème** : Sauvegarde `onboarding_completed` avant `clear()`, mais ne le restaure pas après (donc perdu)
- **Impact** : L'utilisateur pense avoir supprimé son compte, mais toutes ses données restent dans Supabase

---

## 8️⃣ RECONNEXION APRÈS SUPPRESSION

### Comportement ATTENDU
- L'utilisateur se reconnecte avec le même compte
- Si c'est une "première connexion" (profil vide), proposition d'onboarding
- Si le profil existe dans Supabase, chargement depuis Supabase
- Redirection vers `/home` avec profil chargé

### Comportement RÉEL

**Fichier** : `app/index.js`

1. **Vérification session** :
   - Si `session` existe → Redirige vers `/home` ✅
   - **PAS de vérification profil** ❌

**Fichier** : `stores/profileStore.js`

2. **Chargement profil** :
   - `loadProfile()` charge uniquement depuis AsyncStorage
   - **PAS de sync Supabase → AsyncStorage** ❌
   - Si AsyncStorage est vide → `hasProfile = false` ✅

**Fichier** : `app/_layout.js`

3. **Initialisation** :
   - Appelle `loadProfile()` au démarrage
   - Mais le profil Supabase n'est pas chargé

### ✅ Comportement OK
- Redirection correcte vers `/home` si session existe
- Détection de profil vide (`hasProfile = false`)

### ⚠️ Points à améliorer
- **Pas de sync Supabase** : Le profil Supabase n'est jamais chargé dans AsyncStorage
- **Pas de détection "première connexion"** : Aucune logique pour déclencher l'onboarding si profil vide
- **Profil vide mais session active** : L'utilisateur arrive sur `/home` avec un profil vide

### 🐛 Bugs probables
- **Fichier** : `stores/profileStore.js` fonction `loadProfile()`
- **Problème** : Charge uniquement depuis AsyncStorage, jamais depuis Supabase
- **Fichier** : `app/index.js` lignes 55-66
- **Problème** : Redirige vers `/home` même si le profil est vide après reconnexion
- **Impact** : L'utilisateur se reconnecte, arrive sur `/home` avec un profil vide, et ne sait pas comment configurer son profil (pas d'onboarding déclenché)

---

## 📊 RÉSUMÉ DES PROBLÈMES PAR PRIORITÉ

### 🔴 CRITIQUE (Bloque l'utilisation)

1. **Onboarding inaccessible** : Aucun bouton dans l'UI pour déclencher l'onboarding
   - **Fichier** : `app/(tabs)/profile.js`
   - **Solution** : Ajouter un bouton "Configurer mon thème natal" qui redirige vers `/onboarding/index`

2. **Suppression incomplète** : Les données Supabase ne sont pas supprimées
   - **Fichier** : `lib/services/exportService.js`
   - **Solution** : Ajouter la suppression des données Supabase dans `deleteAllUserData()`

3. **Pas de sync Supabase** : Le profil Supabase n'est jamais chargé
   - **Fichier** : `stores/profileStore.js`
   - **Solution** : Ajouter une fonction `syncFromSupabase()` qui charge le profil depuis Supabase

### 🟡 IMPORTANT (Dégradé UX)

4. **Pas de détection première connexion** : Aucune logique pour déclencher l'onboarding si profil vide
   - **Fichier** : `app/index.js`
   - **Solution** : Vérifier `hasProfile` et `onboarding_completed` pour rediriger vers l'onboarding

5. **Profil partiel après onboarding** : L'onboarding ne configure pas un profil complet
   - **Fichier** : `app/onboarding/profile-setup.js`
   - **Solution** : Ajouter les champs `birthTime` et `birthPlace` dans l'onboarding

6. **Redirection incohérente** : `/lunar-revolution` redirige vers `/natal-reading` au lieu de `/profile`
   - **Fichier** : `app/lunar-revolution/index.tsx`
   - **Solution** : Rediriger vers `/profile` pour configurer le thème natal

### 🟢 MINEUR (Amélioration)

7. **Pas de login avec mot de passe** : Seul OTP est disponible
   - **Fichier** : `app/(auth)/login.js`
   - **Solution** : Ajouter un formulaire de login avec mot de passe

8. **Synchronisation thème natal** : `syncFromNatalChart(null)` appelé avec `null`
   - **Fichier** : `app/natal-chart/index.js`
   - **Solution** : Passer le résultat du calcul à `syncFromNatalChart()`

9. **Vérification incomplète** : Le thème natal ne vérifie pas `birthTime`
   - **Fichier** : `app/natal-chart/index.js`
   - **Solution** : Vérifier aussi `birthTime` avant de permettre le calcul

---

## 🎯 PLAN D'ACTION RECOMMANDÉ

### Phase 1 : Corrections critiques
1. Ajouter un bouton onboarding dans `/profile`
2. Corriger la suppression de compte (Supabase)
3. Ajouter la sync Supabase → AsyncStorage

### Phase 2 : Améliorations UX
4. Ajouter la détection première connexion
5. Compléter l'onboarding (birthTime + birthPlace)
6. Corriger les redirections incohérentes

### Phase 3 : Améliorations mineures
7. Ajouter login avec mot de passe
8. Corriger la synchronisation thème natal
9. Améliorer les vérifications de profil

---

**Conclusion** : Le code est fonctionnel mais présente plusieurs incohérences dans les flux utilisateur. Les problèmes principaux sont l'accessibilité de l'onboarding, la suppression incomplète des données, et l'absence de synchronisation Supabase. Un plan d'action priorisé est proposé pour corriger ces problèmes.

