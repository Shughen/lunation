# Diagnostic - Bouton "Supprimer mon profil/compte"

## Date : $(date)
## Branche : `stabilisation-parcours`

---

## 1️⃣ RECHERCHE DU BOUTON

### ❌ Résultat : Le texte exact "Supprimer mon profil" n'existe PAS dans le projet

**Cependant**, il existe un bouton similaire :

### 📍 Localisation du bouton

**Fichier** : `app/settings/index.js`  
**Ligne** : 118-123  
**Composant** : `SettingsItem` avec le label `"Supprimer mon compte"`

```javascript
<SettingsItem
  icon="trash-outline"
  label="Supprimer mon compte"
  iconColor="#EF4444"
  onPress={() => router.push('/settings/privacy')}
/>
```

**Section** : "Confidentialité & Données" (ligne 103-124)

---

## 2️⃣ CONDITIONS D'AFFICHAGE

### ✅ Le bouton s'affiche TOUJOURS

**Aucune condition** : Le bouton "Supprimer mon compte" dans `app/settings/index.js` s'affiche **sans condition**. Il n'y a pas de vérification de `hasProfile`, `isAuthenticated`, ou autre.

**Code** :
```javascript
// Ligne 118-123 - Pas de condition if/else
<SettingsItem
  icon="trash-outline"
  label="Supprimer mon compte"
  iconColor="#EF4444"
  onPress={() => router.push('/settings/privacy')}
/>
```

### 📍 Où le bouton apparaît dans l'UI

1. **Écran** : `/settings` (Paramètres)
2. **Section** : "Confidentialité & Données"
3. **Position** : Après "Politique de confidentialité" et "Exporter mes données"
4. **Style** : Icône poubelle rouge (`#EF4444`)

---

## 3️⃣ EXPLICATION EN FRANÇAIS SIMPLE

### ✅ Dans quel cas le bouton apparaît

Le bouton **apparaît toujours** dans l'écran Paramètres, section "Confidentialité & Données", **peu importe** :
- Si vous avez un profil complet ou non
- Si vous êtes connecté ou non
- Si vous avez des données ou non

**Accès** : `/(tabs)/profile` → Bouton "Paramètres" → Section "Confidentialité & Données" → "Supprimer mon compte"

### ⚠️ Dans quel cas il est normal qu'il ne s'affiche pas

**Il devrait toujours s'afficher**, sauf si :
- L'écran `/settings` n'est pas accessible (problème de navigation)
- L'utilisateur n'a pas les permissions pour accéder aux paramètres

### 🔍 Version actuelle de la branche `stabilisation-parcours`

**Note importante** : Dans la version actuelle, le routing a été simplifié dans `app/index.js`. Le flux ne vérifie plus `hasProfile` pour rediriger vers `/profile`. 

**Impact potentiel** :
- Si l'utilisateur n'a pas de profil complet, il peut quand même accéder à `/settings` depuis `/profile`
- Le bouton devrait donc être visible même sans profil complet

---

## 4️⃣ CE QUE FAIT LE BOUTON EXACTEMENT

### 🔄 Flux d'action

1. **Clic sur "Supprimer mon compte"** dans `app/settings/index.js`
   - → Redirige vers `/settings/privacy` (ligne 122)

2. **Dans `app/settings/privacy.js`** :
   - Le bouton "Supprimer mon compte" est dans la "Zone de danger" (ligne 345-359)
   - Appelle `handleDeleteAccount()` (ligne 130)

3. **Première confirmation** (ligne 131-142) :
   - Alert : "⚠️ Supprimer mon compte"
   - Message : "Cette action est IRRÉVERSIBLE..."
   - Options : "Annuler" ou "Supprimer définitivement"

4. **Deuxième confirmation** (ligne 145-167) :
   - Alert : "Confirmation finale"
   - Message : "Tape 'SUPPRIMER' pour confirmer"
   - Options : "Annuler" ou "Continuer"

5. **Action finale** (ligne 154-158) :
   - Appelle `deleteAllUserData()` depuis `lib/services/exportService.js`
   - Affiche "Compte supprimé" puis redirige vers `/(auth)/login`

---

### 🗑️ Fonctions appelées

#### 1. `deleteAllUserData()` - `lib/services/exportService.js` (ligne 158-175)

```javascript
export async function deleteAllUserData() {
  // Sauvegarder les infos d'onboarding pour afficher écran de départ
  const onboardingCompleted = await AsyncStorage.getItem('onboarding_completed');
  
  // Tout supprimer
  await AsyncStorage.clear();
  
  // Restaurer juste le flag onboarding si on veut montrer le login
  // (optionnel selon UX souhaité)
  
  console.log('[ExportService] All user data deleted');
  return { success: true };
}
```

**Ce qu'elle fait** :
- ✅ Supprime **TOUT** AsyncStorage avec `AsyncStorage.clear()`
- ❌ **NE supprime PAS** les données Supabase (profiles, natal_charts, etc.)
- ❌ **NE supprime PAS** le compte Supabase (auth.users)
- ❌ **NE supprime PAS** les données dans les autres tables Supabase

---

### 📊 Données supprimées

#### ✅ Supprimées (AsyncStorage uniquement)

- `@astroia_user_profile` - Profil utilisateur local
- `@astroia_journal_entries` - Entrées du journal
- `natal_chart_local` - Thème natal local
- `@profile_migrated_to_supabase` - Flag de migration
- `onboarding_completed` - Flag d'onboarding
- `user_consent` - Consentements
- `cycle_config` - Configuration cycle
- `sync_queue` - File de synchronisation
- **TOUTES les autres clés AsyncStorage**

#### ❌ NON supprimées (Supabase)

- ❌ Table `profiles` - Le profil reste dans Supabase
- ❌ Table `natal_charts` - Les thèmes natals restent dans Supabase
- ❌ Table `compatibility_analyses` - Les analyses restent
- ❌ Table `compatibility_history` - L'historique reste
- ❌ Table `daily_horoscopes` - Les horoscopes restent
- ❌ Table `journal_entries` - Les entrées du journal restent (si sauvegardées)
- ❌ Table `chat_conversations` - Les conversations restent
- ❌ Table `chat_messages` - Les messages restent
- ❌ Compte `auth.users` - Le compte utilisateur reste actif dans Supabase

---

### 🔄 Redirection après suppression

**Écran de destination** : `/(auth)/login` (ligne 157)

```javascript
Alert.alert('Compte supprimé', 'Tes données ont été supprimées', [
  { text: 'OK', onPress: () => router.replace('/(auth)/login') },
]);
```

---

## ⚠️ PROBLÈMES IDENTIFIÉS

### 🔴 Problème 1 : Suppression incomplète

**Le bouton "Supprimer mon compte" ne supprime QUE les données AsyncStorage**, pas les données Supabase.

**Impact** :
- Les données restent dans Supabase (profiles, natal_charts, etc.)
- Le compte utilisateur reste actif
- Non conforme au RGPD (droit à l'oubli)

### 🔴 Problème 2 : `clearProfile()` n'existe pas

Dans `app/settings/index.js` ligne 19, il y a :
```javascript
const { profile, clearProfile } = useProfileStore();
```

**Mais** `clearProfile` n'existe pas dans `stores/profileStore.js`. Il existe seulement `resetProfile()`.

**Impact** : Le code dans `handleLogout()` (ligne 31) qui appelle `clearProfile()` va probablement planter.

### 🔴 Problème 3 : Pas de suppression Supabase

Aucune fonction ne supprime les données dans Supabase lors de la suppression du compte.

---

## 📋 RÉSUMÉ

| Aspect | Détail |
|--------|-------|
| **Bouton** | "Supprimer mon compte" (pas "Supprimer mon profil") |
| **Localisation** | `app/settings/index.js` ligne 118-123 |
| **Condition d'affichage** | Aucune - s'affiche toujours |
| **Action au clic** | Redirige vers `/settings/privacy` |
| **Fonction principale** | `deleteAllUserData()` dans `lib/services/exportService.js` |
| **Données supprimées** | AsyncStorage uniquement (tout) |
| **Données NON supprimées** | Toutes les données Supabase |
| **Redirection** | `/(auth)/login` |
| **Problèmes** | 1) Suppression incomplète, 2) `clearProfile()` n'existe pas, 3) Pas de suppression Supabase |

---

**Conclusion** : Le bouton existe mais la suppression est **incomplète**. Seules les données locales (AsyncStorage) sont supprimées, pas les données cloud (Supabase).

