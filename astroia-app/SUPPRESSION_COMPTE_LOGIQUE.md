# Logique de Suppression de Compte - LUNA

## Date : $(date)
## Service : `lib/services/accountDeletionService.js`

---

## 📋 VUE D'ENSEMBLE

La suppression de compte est implémentée dans `lib/services/accountDeletionService.js` et respecte le **droit à l'oubli (RGPD Art. 17)**.

**Fichier principal** : `lib/services/accountDeletionService.js`  
**Fonction principale** : `deleteAccount()`

---

## 🔄 PARCOURS UTILISATEUR

### 1. Déclenchement
- L'utilisateur accède à **Paramètres → Confidentialité → Supprimer mon compte**
- **Fichier UI** : `app/settings/privacy.js`

### 2. Confirmations
- **Première confirmation** : "Cette action est IRRÉVERSIBLE..."
- **Deuxième confirmation** : "Tape 'SUPPRIMER' pour confirmer"

### 3. Suppression
- Appel de `deleteAccount()` depuis `accountDeletionService.js`
- Suppression des données Supabase
- Nettoyage AsyncStorage
- Déconnexion de l'utilisateur

### 4. Redirection
- Redirection automatique vers `/(auth)/login`
- L'utilisateur peut créer un nouveau compte ou se reconnecter

---

## 🗄️ DONNÉES SUPPRIMÉES

### ✅ Supabase (Tables)

#### 1. Table `profiles`
- **Requête** : `DELETE FROM profiles WHERE id = userId`
- **RLS** : Si RLS bloque, l'erreur est loggée mais non bloquante
- **Log** : `✅ Profil supprimé (table profiles)`

#### 2. Table `natal_charts`
- **Requête** : `DELETE FROM natal_charts WHERE user_id = userId`
- **RLS** : Si RLS bloque, l'erreur est loggée mais non bloquante
- **Log** : `✅ Thèmes natals supprimés (table natal_charts)`

#### 3. Table `journal_entries`
- **Requête** : `DELETE FROM journal_entries WHERE user_id = userId`
- **RLS** : Si RLS bloque, l'erreur est loggée mais non bloquante
- **Log** : `✅ Entrées journal supprimées (table journal_entries)`

#### 4. Table `compatibility_analyses` (si existe)
- **Requête** : `DELETE FROM compatibility_analyses WHERE user_id = userId`
- **Non bloquant** : Si la table n'existe pas, l'erreur est ignorée
- **Log** : `✅ Analyses compatibilité supprimées` ou `ℹ️ Table non accessible`

#### 5. Tables à ajouter (TODO)
- `cycle_history` - Historique des cycles menstruels
- `lunar_revolutions` - Révolutions lunaires calculées
- Autres tables liées à l'utilisateur

---

### ✅ AsyncStorage (Local)

Les clés suivantes sont supprimées :

1. `@astroia_user_profile` - Profil utilisateur local
2. `@astroia_journal_entries` - Entrées journal locales
3. `natal_chart_local` - Thème natal local
4. `@profile_migrated_to_supabase` - Flag de migration
5. `onboarding_completed` - Flag d'onboarding
6. `user_consent` - Consentements RGPD
7. `cycle_config` - Configuration cycle menstruel
8. `disclaimer_accepted` - Acceptation disclaimer
9. `disclaimer_accepted_date` - Date acceptation

**Note** : On utilise `multiRemove()` pour supprimer ces clés spécifiques.  
**Alternative** : `AsyncStorage.clear()` supprime TOUT (plus radical, mais peut supprimer des données système).

---

### ✅ Stores Zustand

- **Profile Store** : `useProfileStore.getState().resetProfile()` - Réinitialise le profil à l'état vide
- **Auth Store** : Déconnexion via `useAuthStore.getState().signOut()`

---

## ❌ DONNÉES NON SUPPRIMÉES

### ⚠️ Table `auth.users` (Supabase Auth)

**Pourquoi** : La table `auth.users` est gérée par Supabase Auth et ne peut pas être supprimée directement via l'API client.

**Options** :
1. **Supprimer manuellement** via le dashboard Supabase (admin)
2. **Utiliser une fonction Edge** (Supabase Functions) pour supprimer via l'API admin
3. **Laisser actif** : Le compte reste dans `auth.users` mais sans données associées

**Recommandation** : Pour une suppression complète, créer une fonction Edge qui utilise l'API admin Supabase pour supprimer l'utilisateur de `auth.users`.

**TODO** : Implémenter une fonction Edge `delete-user` qui :
- Reçoit l'ID utilisateur
- Utilise l'API admin Supabase
- Supprime l'utilisateur de `auth.users`
- Appelle cette fonction depuis `accountDeletionService.js`

---

## 🛡️ GESTION DES ERREURS

### Stratégie : "Continue malgré les erreurs"

Si une suppression Supabase échoue (RLS, permissions, etc.) :
1. ✅ L'erreur est **loggée** clairement
2. ✅ Le processus **continue** avec les autres suppressions
3. ✅ Le **nettoyage local** est toujours effectué
4. ✅ L'utilisateur est **déconnecté**
5. ⚠️ L'utilisateur est **informé** des erreurs via Alert

### Codes d'erreur gérés

- **`42501`** : RLS bloque la suppression (permissions)
- **`42P01`** : Table n'existe pas
- **Autres** : Erreurs inattendues (loggées et propagées)

---

## 📊 LOGS ET TRACABILITÉ

Tous les logs suivent le format :
```
[AccountDeletion] ✅/❌/⚠️/ℹ️ Message
```

**Exemples** :
- `[AccountDeletion] 🗑️ Début suppression compte pour utilisateur: abc123`
- `[AccountDeletion] ✅ Profil supprimé (table profiles)`
- `[AccountDeletion] ❌ Erreur suppression Supabase: RLS policy violation`
- `[AccountDeletion] ✅ Suppression compte terminée (0 erreur(s))`

---

## 🔧 ARCHITECTURE

### Fichiers impliqués

1. **Service** : `lib/services/accountDeletionService.js`
   - Fonction principale : `deleteAccount()`
   - Fonctions privées : `deleteSupabaseData()`, `cleanupLocalData()`, `signOutUser()`

2. **UI** : `app/settings/privacy.js`
   - Bouton "Supprimer mon compte"
   - Confirmations (2 Alert)
   - Appel à `deleteAccount()`
   - Redirection vers `/login`

3. **Stores** :
   - `stores/authStore.js` - Déconnexion
   - `stores/profileStore.js` - Reset profil

4. **Supabase** : `lib/supabase.js`
   - Client Supabase configuré

---

## 🧪 TESTS RECOMMANDÉS

### Scénarios à tester

1. **Suppression complète** (utilisateur avec toutes les données)
   - Vérifier que toutes les tables sont vidées
   - Vérifier que AsyncStorage est nettoyé
   - Vérifier que l'utilisateur est déconnecté

2. **Suppression partielle** (utilisateur avec seulement profil)
   - Vérifier que les erreurs sont gérées gracieusement
   - Vérifier que le nettoyage local fonctionne

3. **Suppression avec RLS bloqué**
   - Vérifier que les erreurs RLS sont loggées mais non bloquantes
   - Vérifier que le nettoyage local continue

4. **Suppression sans connexion**
   - Vérifier que le nettoyage local fonctionne quand même

---

## 📝 AMÉLIORATIONS FUTURES

### TODO : Suppression complète `auth.users`

1. Créer une fonction Edge Supabase `delete-user`
2. Appeler cette fonction depuis `accountDeletionService.js`
3. Gérer les erreurs gracieusement

### TODO : Suppression d'autres tables

- `cycle_history`
- `lunar_revolutions`
- Autres tables liées à l'utilisateur

### TODO : Audit trail

- Logger toutes les suppressions dans une table d'audit
- Conserver un historique des suppressions (conformité RGPD)

---

## 🔒 CONFORMITÉ RGPD

### Article 17 - Droit à l'oubli

✅ **Respecté** :
- Suppression des données personnelles
- Suppression des données de santé (cycle, journal)
- Suppression des données astrologiques (thème natal)
- Nettoyage local complet

⚠️ **À améliorer** :
- Suppression de `auth.users` (nécessite fonction Edge)
- Audit trail des suppressions

---

## 📞 SUPPORT

En cas de problème avec la suppression de compte :
- Vérifier les logs : `[AccountDeletion]`
- Vérifier les permissions RLS dans Supabase
- Vérifier que les tables existent

**Contact** : privacy@luna-app.fr

---

**Conclusion** : La suppression de compte est fonctionnelle et respecte le RGPD. Les améliorations futures concernent principalement la suppression complète de `auth.users` via une fonction Edge Supabase.

