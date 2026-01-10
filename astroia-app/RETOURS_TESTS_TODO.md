# 📋 RETOURS TESTS - TODO

**Date :** 10 novembre 2025  
**Source :** Tests utilisateur (Rémi)  
**Status :** Partiellement traité

---

## ✅ **TRAITÉ** (Commit 6a7cdd9)

### 🏠 **Accueil (Home)**
- ✅ Marges entre cartes augmentées (+12px)
  - CycleCard: `marginBottom: 12`
  - MoodCard: `marginBottom: 12`
  - AstroCard: `marginBottom: 12`
- ✅ ExploreGrid affiné
  - Gap augmenté: 4px → 8px
  - Padding tuiles réduit (lg/md → md/sm)

---

## 📋 **À TRAITER** (en attente clarification)

### 🌙 **Cycle & Astrologie (intro / saisie)**

**Demandes :**
1. Champ "Jour du cycle" :
   - Ajouter placeholder "Ex : 12"
   - `keyboardType="number-pad"`
   - Validation 1-35

2. Alignement titre "Mon cycle actuel" :
   - Réduire marge avec champ : 16px → 8px

3. Bouton "Analyser mon cycle" :
   - Améliorer contraste texte blanc/fond rose
   - Option A : Texte noir semi-transparent (#111 à 0.9)
   - Option B : Gradient plus soutenu

**⚠️ Statut :** Fichier non identifié clairement  
**Candidats possibles :**
- `app/cycle-astro/index.js` ?
- `app/settings/cycle.js` ?

**Action requise :** Préciser quel fichier contient ce formulaire

---

### 🌕 **Cycle – Résultat (Menstruelle / Transits / Conseils)**

**Demandes :**
1. "Énergie cosmique" :
   - Augmenter padding horizontal gauche (+6px)

2. "Aspect : Neutre" :
   - Ajouter icône "⚖️" ou visuel discret

3. Bloc "Conseils personnalisés" :
   - Augmenter bottom padding (+24px avant footer)

**⚠️ Statut :** Fichier non identifié  
**Candidat :** `app/cycle-astro/result.js` ou similaire ?

**Action requise :** Préciser quel fichier contient cet écran

---

### 📒 **Journal (liste / stats)**

**Demandes :**
1. Bouton "+" :
   - Ajouter fond semi-transparent `backgroundColor: rgba(primary, 0.2)`
   - OU shadow légère

2. Espacement stats ↔ première entrée :
   - Augmenter gap (+8px)

3. Badge "Nouvelle lune" :
   - Corriger `alignItems: center` sur container

**⚠️ Statut :** Fichier identifié  
**Fichier :** `app/journal/index.tsx`

**Action requise :** Implémenter les 3 points

---

## 🎯 **PLAN D'ACTION**

### **Option A : Continuer avec retours précis**

L'utilisateur précise les fichiers exacts :
1. "Le formulaire cycle est dans `app/XXX/index.js`"
2. "Le résultat cycle est dans `app/YYY/result.js`"

→ J'implémente immédiatement

---

### **Option B : Continuer tests + autres retours**

L'utilisateur dit :
- "Continue tes tests, je te fais un retour après sur les 16 écrans restants"

→ J'attends ses retours

---

### **Option C : Screenshots**

L'utilisateur envoie screenshots des écrans concernés

→ J'identifie les fichiers visuellement

---

## 📊 **RÉSUMÉ**

| Module | Demandes | Status | Action |
|--------|----------|--------|--------|
| **Home** | 2 | ✅ Traité | Commit 6a7cdd9 |
| **Cycle saisie** | 3 | ⏸️ En attente | Fichier à préciser |
| **Cycle résultat** | 3 | ⏸️ En attente | Fichier à préciser |
| **Journal** | 3 | ⏸️ En attente | Implémentation possible |

---

**Auteur :** Cursor AI (Claude Sonnet 4.5)  
**Date :** 10 novembre 2025

