# ⚙️ SPRINT 12 - SETTINGS & ONBOARDING

**Date :** 5 novembre 2025  
**Objectif :** Écran de paramètres + Expérience premier lancement

---

## 🎯 VISION

Finaliser l'expérience utilisateur avec :
- ⚙️ Écran Settings complet
- 👋 Onboarding pour nouveaux utilisateurs
- 🔔 Gestion des notifications
- 🌓 Toggle thème sombre/clair (préparation)
- 📱 Gestion du compte
- ℹ️ À propos & Support

---

## 📋 TÂCHES

### 1. Écran Settings ⚙️

#### Structure
```
┌─────────────────────────┐
│   ⚙️ Paramètres         │
├─────────────────────────┤
│ 👤 Mon Compte           │
│   • Modifier profil     │
│   • Email               │
│   • Mot de passe        │
├─────────────────────────┤
│ 🔔 Notifications        │
│   • Horoscope (8h) [ON] │
│   • Rappels [OFF]       │
│   • Badges [ON]         │
├─────────────────────────┤
│ 🎨 Apparence            │
│   • Thème [Sombre]      │
│   • Langue [Français]   │
├─────────────────────────┤
│ 💾 Données              │
│   • Vider le cache      │
│   • Export données      │
│   • Supprimer compte    │
├─────────────────────────┤
│ ℹ️ À propos             │
│   • Version 1.0.0       │
│   • Support             │
│   • CGU & Confidentialité│
│   • Déconnexion         │
└─────────────────────────┘
```

#### Fonctionnalités
- [ ] Navigation depuis profil ou menu
- [ ] Sections avec dividers
- [ ] Toggles pour notifications
- [ ] Boutons d'action (modifier, exporter, etc.)
- [ ] Modal confirmation pour actions critiques
- [ ] Liens externes (CGU, support)

---

### 2. Onboarding Premier Lancement 👋

#### Flow (3 screens)

**Screen 1 - Welcome**
```
Illustration cosmique
"Bienvenue sur Astro.IA"
"L'astrologie propulsée par l'IA"
[Suivant]
```

**Screen 2 - Features**
```
🌙 Thème natal précis
🤖 Chat IA personnalisé
💕 Compatibilité avancée
📅 Horoscope quotidien
[Suivant]
```

**Screen 3 - Permissions**
```
🔔 Notifications
"Recevez votre horoscope à 8h"
[Autoriser] [Plus tard]

✨ Commencer !
```

#### Implémentation
- [ ] 3 screens avec swipe horizontal
- [ ] Pagination dots
- [ ] Skip button
- [ ] AsyncStorage flag `onboarding_completed`
- [ ] Afficher seulement au premier lancement

---

### 3. Gestion Notifications 🔔

**Types de notifications :**
- [ ] **Horoscope quotidien** : 8h du matin
- [ ] **Rappel journal** : Tous les soirs 20h (optionnel)
- [ ] **Badge unlocked** : Instantané
- [ ] **Streak reminder** : Si pas ouvert depuis 2 jours

**Implémentation :**
- [ ] Expo Notifications
- [ ] Demande de permission
- [ ] Scheduling local (8h, 20h)
- [ ] Deep linking vers screens

---

### 4. Cache & Data Management 💾

- [ ] **Vider le cache** :
  - AsyncStorage (horoscopes, analyses locales)
  - Confirmation obligatoire
  - Message "Cache vidé avec succès"

- [ ] **Export données** (RGPD) :
  - JSON avec toutes les données utilisateur
  - Téléchargement ou partage
  - Format lisible

- [ ] **Supprimer compte** :
  - Modal avec confirmation forte
  - Input "SUPPRIMER" pour valider
  - Suppression Supabase + local
  - Logout automatique

---

### 5. À Propos & Support ℹ️

- [ ] **Version de l'app** :
  - Afficher version depuis package.json
  - Build number
  - Environnement (dev/prod)

- [ ] **Support** :
  - Email : support@astroia.app
  - Bouton "Nous contacter" (mailto)
  - FAQ (optionnel)

- [ ] **Légal** :
  - CGU (lien externe ou modal)
  - Politique de confidentialité
  - Crédits (APIs utilisées)

---

### 6. Toggle Thème (Préparation) 🌓

- [ ] Store Zustand `themeStore.js`
- [ ] State : `theme: 'dark' | 'light'`
- [ ] Persistence AsyncStorage
- [ ] Toggle dans Settings
- [ ] Palette light à définir (Sprint futur)

---

## 🎨 DESIGN

### Settings Screen
- Fond : Dégradé standard sombre
- Sections : Cards avec titles
- Toggles : Switch natif iOS/Android
- Dividers : Subtle entre sections
- Actions destructives : Rouge

### Onboarding
- Fond : Dégradé cosmique animé
- Illustrations : Emojis géants (80-100px)
- Texte : Centré, clair, concis
- Boutons : CTA doré
- Dots : Pagination en bas

---

## 🚀 IMPLÉMENTATION

### Étapes
1. **Screen Settings** (1h30)
   - Structure de base
   - Sections Mon Compte
   - Section Notifications
   - Section Apparence
   - Section Données
   - Section À propos

2. **Onboarding** (1h)
   - 3 screens avec Swiper
   - AsyncStorage flag
   - Logic premier lancement

3. **Notifications** (1h)
   - Expo Notifications
   - Permissions
   - Scheduling
   - Deep links

4. **Cache & Data** (45min)
   - Vider cache
   - Export JSON
   - Supprimer compte

5. **Tests** (30min)

**TOTAL : ~5h**

---

## 🎯 RÉSULTAT FINAL

**App avec :**
- ⚙️ Settings complets
- 👋 Onboarding nouveau user
- 🔔 Notifications push
- 💾 Gestion données (RGPD)
- ℹ️ Support & légal
- 🌓 Thème (préparé)

---

**Prêt pour le Sprint 12 ! 🚀**

