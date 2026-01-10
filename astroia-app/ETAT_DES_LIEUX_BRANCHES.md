# État des Lieux des Branches Git - Astro.IA

## Date : $(date)
## Repository : `astroia-app`

---

## 📊 RÉSUMÉ GLOBAL

**Total de branches locales** : 22 branches  
**Branches distantes** : 4 branches (`origin/main`, `origin/bugbot-test`, `origin/2025-11-12-4ge9-Nvbtd`, `origin/2025-11-15-r0bg-oUkNm`)

---

## 🎯 CLASSIFICATION DES BRANCHES

### ✅ À GARDER ABSOLUMENT

Ces branches contiennent du travail important et actif :

1. **`main`** ⭐ **BRANCHE PRINCIPALE**
2. **`stabilisation-parcours`** ⭐ **BRANCHE ACTIVE** (actuellement checkout)
3. **`bugbot-test`** ⭐ **BRANCHE DE TEST**
4. **`feature/cycle-tracking-v2`** ⭐ **FEATURE BRANCH**

---

### 📚 POTENTIELLEMENT UTILES

Ces branches peuvent contenir du travail intéressant à relire :

5. **`fix-auth-flow-nZ0NH`** (identique à main actuellement)

---

### 🗑️ PROBABLEMENT JETABLES

Ces branches sont des worktrees auto-générées sans travail significatif :

6-21. **Toutes les branches `2025-11-15-xxxxx`** (18 branches)
   - `2025-11-15-01rh-DMnDP`
   - `2025-11-15-0wm3-5K9b5`
   - `2025-11-15-25pb-F92hI`
   - `2025-11-15-3ann-Qw8It`
   - `2025-11-15-43pz-rsYva`
   - `2025-11-15-4nr1-QLFrj`
   - `2025-11-15-asyd-Y0VUy`
   - `2025-11-15-bo1s-tbhmW`
   - `2025-11-15-bq9g-MzzMl`
   - `2025-11-15-fj9t-oofs7`
   - `2025-11-15-gfcw-RoWZ4`
   - `2025-11-15-gneq-3kPrd`
   - `2025-11-15-il9c-KBbNI`
   - `2025-11-15-ox02-sHdtp`
   - `2025-11-15-re6t-mwbeJ`
   - `2025-11-15-rwkz-c1PbB`
   - `2025-11-15-v7rv-FaetY`
   - `2025-11-15-ys6i-A5XUl` (worktree actuel)

**Caractéristiques** :
- Toutes pointent vers le même commit que `main` (`0426c7f`)
- Sont des worktrees Git (indiquées par le chemin entre parenthèses)
- Aucun commit unique sur ces branches
- Probablement créées automatiquement par Cursor ou un outil similaire

---

## 📋 ANALYSE DÉTAILLÉE DES BRANCHES IMPORTANTES

### 1. **`main`** ⭐ BRANCHE PRINCIPALE

**Base** : Branche racine (pas de base)  
**Dernier commit** : `0426c7f` - "Merge 2025-11-12-4ge9-Nvbtd into main: thème natal + cycles + révolution lunaire"  
**Statut** : Synchronisée avec `origin/main`

**Contenu** :
- Merge de la feature "thème natal + cycles + révolution lunaire"
- Contient les fonctionnalités principales de l'app
- Branche de production

**Recommandation** : ✅ **À GARDER** - C'est la branche principale, ne jamais supprimer.

---

### 2. **`stabilisation-parcours`** ⭐ BRANCHE ACTIVE

**Base** : `main` (commit `0426c7f`)  
**Dernier commit** : `8e8c397` - "docs: analyse complète du fonctionnement onboarding dans stabilisation-parcours"  
**Statut** : Branche locale uniquement (pas poussée sur origin)  
**Branche actuelle** : ✅ Vous êtes actuellement sur cette branche

**Contenu** (10 commits depuis main) :
1. Corrections de routing (suppression Stack.Screen invalides, simplification flux)
2. Amélioration gestion d'erreurs dans `app/_layout.js` et `app/index.js`
3. Correction bug `updateProfile` → `saveProfile` dans onboarding
4. Documentation complète (diagnostics, analyses, récapitulatifs)

**Modifications** :
- `app/index.js` : Simplification routing (login/home uniquement)
- `app/_layout.js` : Gestion d'erreurs améliorée
- `app/onboarding/profile-setup.js` : Correction bug
- Documentation : 5 fichiers MD créés

**Recommandation** : ✅ **MERGER DANS MAIN** après validation des tests. Cette branche contient des corrections importantes de stabilisation qui devraient être intégrées.

---

### 3. **`bugbot-test`** ⭐ BRANCHE DE TEST

**Base** : `main` (commit `0426c7f`)  
**Dernier commit** : `617a5f5` - "fix: amélioration du routing initial selon recommandations BugBot"  
**Statut** : Synchronisée avec `origin/bugbot-test`

**Contenu** (2 commits depuis main) :
1. Test BugBot avec commentaire de test
2. Amélioration routing selon recommandations BugBot

**Modifications** :
- `app/index.js` : Améliorations de routing (timeout, gestion erreurs)

**Recommandation** : ⚠️ **À FUSIONNER OU SUPPRIMER** après merge. Cette branche était un test BugBot. Les améliorations sont déjà intégrées dans `stabilisation-parcours` (qui est plus complète). On peut soit merger dans main, soit supprimer si le travail est déjà dans `stabilisation-parcours`.

---

### 4. **`feature/cycle-tracking-v2`** ⭐ FEATURE BRANCH

**Base** : Ancienne base (commit `4ec33c8`), pas directement basée sur `main` actuel  
**Dernier commit** : `4ec33c8` - "chore(analytics): add cycle tracking v2 events + complete documentation"

**Contenu** (5 commits) :
1. Analytics cycle tracking v2
2. Écran MyCycles avec historique et stats
3. Composants CycleStats, CycleCountdown, HistoryBar
4. QuickPeriodLog component
5. Migration depuis settings vers history

**Recommandation** : ✅ **À GARDER** - Feature branch avec travail significatif sur le tracking de cycle. À merger dans main si la feature est prête, ou à garder pour référence.

---

### 5. **`fix-auth-flow-nZ0NH`**

**Base** : `main` (même commit `0426c7f`)  
**Dernier commit** : Identique à `main`

**Contenu** : Aucune différence avec `main`

**Recommandation** : 🗑️ **PROBABLEMENT JETABLE** - Identique à main, probablement un worktree ou une branche de test qui n'a pas évolué.

---

## 🔍 BRANCHES DISTANTES

### `origin/2025-11-12-4ge9-Nvbtd`
- Feature branch distante : "thème natal + cycles + gestion gender/hasCycles"
- Déjà mergée dans `main` (commit `0426c7f`)
- **Recommandation** : Peut être supprimée côté distant si plus utilisée

### `origin/2025-11-15-r0bg-oUkNm`
- Branche distante avec documentation sur branches et worktrees
- **Recommandation** : À vérifier si contient du contenu utile

---

## 📊 STATISTIQUES

| Catégorie | Nombre | Pourcentage |
|-----------|--------|-------------|
| À garder | 4 | 18% |
| Potentiellement utiles | 1 | 5% |
| Probablement jetables | 18 | 82% |
| **Total** | **23** | **100%** |

---

## 🎯 RECOMMANDATIONS GLOBALES

### Actions immédiates

1. **`stabilisation-parcours`** :
   - ✅ Tester les corrections
   - ✅ Merger dans `main` une fois validé
   - ✅ Garder la branche pour référence après merge

2. **`bugbot-test`** :
   - ⚠️ Vérifier si les améliorations sont déjà dans `stabilisation-parcours`
   - Si oui : Supprimer après merge de `stabilisation-parcours`
   - Si non : Merger dans `main` ou `stabilisation-parcours`

3. **`feature/cycle-tracking-v2`** :
   - ✅ Garder si la feature est en cours
   - ✅ Merger dans `main` si prête
   - ✅ Supprimer après merge si terminée

### Nettoyage (à faire après validation)

4. **Branches `2025-11-15-xxxxx`** :
   - 🗑️ Supprimer toutes les branches worktree auto-générées
   - 🗑️ Supprimer `fix-auth-flow-nZ0NH` (identique à main)

**Commande suggérée** (à exécuter après validation) :
```bash
# Supprimer les branches worktree (exemple)
git branch -D 2025-11-15-01rh-DMnDP 2025-11-15-0wm3-5K9b5 ...
# Supprimer fix-auth-flow
git branch -D fix-auth-flow-nZ0NH
```

---

## 📝 NOTES IMPORTANTES

- **Worktrees** : Les branches `2025-11-15-xxxxx` sont des worktrees Git. Supprimer ces branches ne supprime pas les worktrees eux-mêmes. Pour supprimer les worktrees, utiliser `git worktree remove <path>`.

- **Branche actuelle** : Vous êtes sur `stabilisation-parcours` (worktree `A5XUl`).

- **Synchronisation** : `main` et `bugbot-test` sont synchronisées avec origin. `stabilisation-parcours` n'est pas encore poussée.

---

**Conclusion** : Le repository contient principalement des worktrees auto-générées. Les branches importantes sont `main`, `stabilisation-parcours`, `bugbot-test` et `feature/cycle-tracking-v2`. Un nettoyage des branches worktree est recommandé après validation du travail sur `stabilisation-parcours`.

