# 🚀 Sprint 12 - Beta TestFlight & Play Store

**Date début:** 09/11/2025  
**Durée estimée:** 1-2 semaines  
**Objectif:** Déployer LUNA en beta publique iOS + Android

---

## 🎯 Objectifs Sprint 12

### **Phase 1 : Configuration EAS Build** ⚙️
- Setup Expo Application Services (EAS)
- Configuration `app.json` production
- Configuration `eas.json` (preview, production)
- Secrets management (API keys)

### **Phase 2 : Assets & Branding** 🎨
- Icône app LUNA (1024x1024)
- Splash screen (iPhone, Android)
- Adaptive icon Android
- Assets iOS (tous formats)
- Assets Android (toutes densités)

### **Phase 3 : Metadata Stores** 📝
- Description App Store (FR + EN)
- Keywords SEO
- Screenshots iOS (6.5", 5.5")
- Screenshots Android (Phone, Tablet)
- Privacy Policy URL
- Support URL

### **Phase 4 : Build iOS Beta** 🍎
- Configuration App Store Connect
- Provisioning profiles
- Build EAS iOS
- Upload TestFlight
- Invitation testeurs beta

### **Phase 5 : Build Android Beta** 🤖
- Configuration Google Play Console
- Build EAS Android (AAB)
- Upload Play Store Internal
- Invitation testeurs beta

### **Phase 6 : Landing Page** 🌐
- Page minimale luna-app.fr
- Liens stores (badge iOS/Android)
- Contact support
- Politique confidentialité

---

## 📋 User Story Sprint 12

### US1: Configuration EAS
**En tant que** développeur  
**Je veux** configurer EAS Build  
**Afin de** créer des builds production iOS/Android

**Acceptance Criteria:**
- [ ] Compte EAS créé (expo.dev)
- [ ] `eas.json` configuré (3 profiles)
- [ ] `app.json` avec bundleId + package
- [ ] Secrets configurés (API keys)
- [ ] Build local réussit

---

### US2: Assets Production
**En tant que** designer  
**Je veux** des assets professionnels  
**Afin de** respecter les guidelines stores

**Acceptance Criteria:**
- [ ] Icône 1024x1024 (PNG transparent impossible, fond)
- [ ] Splash screen adaptatif
- [ ] Adaptive icon Android (foreground + background)
- [ ] Tous les formats générés automatiquement

---

### US3: Store Listing
**En tant que** product manager  
**Je veux** une description engageante  
**Afin d'** attirer les beta testeuses

**Acceptance Criteria:**
- [ ] Description FR (max 4000 caractères)
- [ ] Description EN (traduction)
- [ ] Keywords SEO optimisés
- [ ] Screenshots 5 écrans clés
- [ ] Catégorie : Santé & Forme / Lifestyle

---

### US4: Beta iOS
**En tant que** utilisatrice iOS  
**Je veux** tester LUNA sur iPhone  
**Afin de** donner mon feedback

**Acceptance Criteria:**
- [ ] Build uploadé sur TestFlight
- [ ] Invitation 5-10 testeurs
- [ ] App installable via lien
- [ ] Feedback collecté
- [ ] Crashlytics actif

---

### US5: Beta Android
**En tant que** utilisatrice Android  
**Je veux** tester LUNA sur Android  
**Afin de** donner mon feedback

**Acceptance Criteria:**
- [ ] Build uploadé sur Play Store Internal
- [ ] Track "Internal testing" activée
- [ ] Invitation 5-10 testeurs
- [ ] App installable via lien
- [ ] Crashlytics actif

---

### US6: Landing Page
**En tant que** visiteur web  
**Je veux** découvrir LUNA  
**Afin de** télécharger l'app

**Acceptance Criteria:**
- [ ] Page luna-app.fr accessible
- [ ] Hero section claire
- [ ] Badges App Store + Play Store
- [ ] Liens politique confidentialité
- [ ] Contact support

---

## 🏗️ Architecture Technique Sprint 12

### 1. Configuration EAS

**Fichier : `eas.json`**
```json
{
  "cli": {
    "version": ">= 5.0.0"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal",
      "ios": {
        "simulator": true
      }
    },
    "production": {
      "autoIncrement": true
    }
  },
  "submit": {
    "production": {}
  }
}
```

**Fichier : `app.json` (extrait)**
```json
{
  "expo": {
    "name": "LUNA - Cycle & Cosmos",
    "slug": "luna-cycle-cosmos",
    "version": "2.0.0",
    "ios": {
      "bundleIdentifier": "com.astroia.luna",
      "buildNumber": "1"
    },
    "android": {
      "package": "com.astroia.luna",
      "versionCode": 1
    }
  }
}
```

---

### 2. Assets Production

**Icône app (1024x1024):**
- Design : Lune croissant 🌙 stylisée
- Couleurs : Dégradé rose poudré → lavande
- Fond : Violet cosmique (#121128)
- Format : PNG, pas de transparence (required iOS)

**Splash screen:**
- Logo LUNA centré
- Fond dégradé identique app
- Texte "Cycle & Cosmos"
- Loading indicator

**Commandes génération :**
```bash
# Générer tous les assets depuis icon.png
npx expo prebuild --clean

# Ou avec EAS
eas build:configure
```

---

### 3. Store Metadata

**Description FR (App Store) :**
```
🌙 LUNA - Cycle & Cosmos

L'app qui relie ton corps et les cycles du ciel.

LUNA t'aide à mieux comprendre ton cycle menstruel en le corrélant avec l'astrologie et les transits lunaires. Reçois des recommandations personnalisées selon ta phase actuelle et ton thème astral.

✨ FONCTIONNALITÉS :

🩸 SUIVI CYCLE
• Tracking cycle menstruel (4 phases)
• Calcul automatique phase actuelle
• Niveau d'énergie en temps réel
• Prédiction fertilité

🌙 ASTROLOGIE LUNAIRE
• Transit lunaire quotidien
• Corrélation cycle-cosmos
• Recommandations personnalisées
• Mantras & conseils du jour

🤖 ASSISTANT IA CONTEXTUEL
• Chatbot intelligent spécialisé cycle
• Réponses adaptées à ta phase
• Conseils bien-être personnalisés
• Disponible 24/7

📖 JOURNAL D'HUMEUR
• Suivi émotions quotidiennes
• Auto-tagging intelligent
• Graphiques humeur/cycle
• Insights IA automatiques

🪐 ASTROLOGIE COMPLÈTE
• Thème natal détaillé
• Horoscope quotidien IA
• Compatibilité amoureuse
• Analyse parent-enfant

📊 DASHBOARD & GRAPHIQUES
• Visualisation 30 jours
• Corrélations cycle-humeur
• Calendrier menstruel coloré
• Statistiques détaillées

🔐 CONFIDENTIALITÉ & RGPD
• Données santé strictement protégées
• Stockage EU uniquement
• Consentement explicite requis
• Export/suppression à tout moment

⚕️ BIEN-ÊTRE, PAS MÉDICAL
LUNA est un outil de bien-être personnel, pas un dispositif médical. Toujours consulter un professionnel pour avis médical.

Rejoins la beta et découvre une nouvelle façon de vivre ton cycle ! 🌸
```

**Keywords (30 max) :**
```
cycle menstruel, astrologie, lune, bien-être féminin, suivi cycle, ovulation, fertilité, horoscope, thème natal, journal intime, humeur, émotions, intelligence artificielle, IA, wellness, santé féminine, cosmique, transit lunaire, phases lune, compatibilité amoureuse, couple, relations, mindfulness, méditation, développement personnel
```

**Catégories :**
- iOS : Santé & Forme / Lifestyle
- Android : Santé & Remise en forme / Lifestyle

---

### 4. Build iOS

**Prérequis :**
- Compte Apple Developer (99$/an)
- App Store Connect app créée
- Bundle ID enregistré : `com.astroia.luna`

**Commandes :**
```bash
# 1. Login EAS
eas login

# 2. Configuration projet
eas build:configure

# 3. Build preview (TestFlight)
eas build --platform ios --profile preview

# 4. Submit à App Store Connect
eas submit --platform ios
```

**TestFlight :**
1. App Store Connect → TestFlight
2. Ajouter testeurs internes (email)
3. Créer groupe "Beta LUNA"
4. Activer testing externe (5-10 testeurs)
5. Partager lien public TestFlight

---

### 5. Build Android

**Prérequis :**
- Compte Google Play Console (25$ one-time)
- App créée dans console
- Package name : `com.astroia.luna`

**Commandes :**
```bash
# 1. Build AAB
eas build --platform android --profile production

# 2. Submit à Play Store
eas submit --platform android
```

**Play Store Internal Testing :**
1. Google Play Console → Testing → Internal testing
2. Créer release
3. Upload AAB
4. Ajouter testeurs (email ou liste)
5. Publier version interne
6. Partager lien Play Store beta

---

### 6. Landing Page

**Structure minimale :**
```
luna-app.fr/
├── index.html          # Page d'accueil
├── privacy.html        # Politique confidentialité
├── support.html        # Contact support
├── assets/
│   ├── logo.png
│   ├── screenshot1.png
│   └── app-store-badge.svg
└── style.css
```

**Hébergement :**
- Vercel (gratuit, intégré Git)
- Cloudflare Pages
- Netlify

**Commande deploy Vercel :**
```bash
cd landing-page/
vercel --prod
```

---

## ⏱️ Estimation Sprint 12

| Tâche | Complexité | Durée |
|-------|------------|-------|
| Configuration EAS | Moyenne | 2h |
| Création assets | Moyenne | 3h |
| Metadata stores | Faible | 2h |
| Build iOS | Moyenne | 2h |
| Setup TestFlight | Faible | 1h |
| Build Android | Moyenne | 2h |
| Setup Play Store | Moyenne | 2h |
| Landing page | Faible | 3h |
| Tests beta | Élevée | 5h |
| Ajustements feedback | Moyenne | 3h |
| **Total** | | **~25h** |

**Durée estimée :** 1-2 semaines (avec reviews stores)

---

## 🚀 Plan d'Exécution

### **Jour 1-2 : Configuration & Assets** ⚙️
1. Setup compte EAS
2. Configuration `eas.json`
3. Mise à jour `app.json`
4. Création icône + splash
5. Test builds locaux

### **Jour 3 : Metadata Stores** 📝
1. Rédiger descriptions FR/EN
2. Capturer 5-6 screenshots
3. Préparer keywords
4. Remplir App Store Connect
5. Remplir Google Play Console

### **Jour 4 : Build iOS** 🍎
1. Build EAS iOS production
2. Upload App Store Connect
3. Configurer TestFlight
4. Inviter testeurs beta (5-10)
5. Tests installation

### **Jour 5 : Build Android** 🤖
1. Build EAS Android AAB
2. Upload Play Console
3. Configurer Internal testing
4. Inviter testeurs beta (5-10)
5. Tests installation

### **Jour 6-7 : Landing Page** 🌐
1. Design page accueil
2. Badges stores
3. Politique confidentialité
4. Support contact
5. Deploy Vercel

### **Jour 8-14 : Beta Testing** 🧪
1. Collecter feedback testeurs
2. Identifier bugs critiques
3. Hotfixes si nécessaire
4. Itération beta 2 si besoin
5. Validation finale

---

## 📱 Configuration App

### app.json (Production)

```json
{
  "expo": {
    "name": "LUNA - Cycle & Cosmos",
    "slug": "luna-cycle-cosmos",
    "version": "2.0.0",
    "orientation": "portrait",
    "userInterfaceStyle": "dark",
    "icon": "./assets/icon.png",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#121128"
    },
    "assetBundlePatterns": ["**/*"],
    
    "ios": {
      "bundleIdentifier": "com.astroia.luna",
      "buildNumber": "1",
      "supportsTablet": true,
      "infoPlist": {
        "NSHealthShareUsageDescription": "LUNA a besoin d'accéder à vos données de cycle menstruel pour fournir des recommandations personnalisées.",
        "NSHealthUpdateUsageDescription": "LUNA enregistre vos données de cycle pour le suivi et l'analyse."
      }
    },
    
    "android": {
      "package": "com.astroia.luna",
      "versionCode": 1,
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#121128"
      },
      "permissions": [
        "android.permission.INTERNET",
        "android.permission.ACCESS_NETWORK_STATE"
      ]
    },
    
    "web": {
      "favicon": "./assets/favicon.png"
    },
    
    "plugins": [
      "expo-router",
      "@sentry/react-native"
    ],
    
    "extra": {
      "aiApiUrl": "https://astro-ia-niei71xao-remibeaurain-4057s-projects.vercel.app/api/ai/chat",
      "eas": {
        "projectId": "YOUR_EAS_PROJECT_ID"
      }
    }
  }
}
```

---

### eas.json

```json
{
  "cli": {
    "version": ">= 5.0.0"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal",
      "ios": {
        "simulator": true
      }
    },
    "preview": {
      "distribution": "internal",
      "channel": "preview",
      "ios": {
        "simulator": false,
        "buildConfiguration": "Release"
      },
      "android": {
        "buildType": "apk"
      }
    },
    "production": {
      "channel": "production",
      "autoIncrement": true,
      "ios": {
        "buildConfiguration": "Release"
      },
      "android": {
        "buildType": "aab"
      }
    }
  },
  "submit": {
    "production": {
      "ios": {
        "appleId": "YOUR_APPLE_ID@email.com",
        "ascAppId": "YOUR_ASC_APP_ID",
        "appleTeamId": "YOUR_TEAM_ID"
      },
      "android": {
        "serviceAccountKeyPath": "./google-play-service-account.json",
        "track": "internal"
      }
    }
  }
}
```

---

## 🎨 Assets à Créer

### Icône App (icon.png)
```
Taille : 1024x1024px
Format : PNG
Background : Violet #121128
Design : Lune croissant 🌙 stylisée
Couleur lune : Dégradé rose→lavande
Padding : 20% (Apple requirement)
```

**Prompt Midjourney/DALL-E :**
```
App icon design, minimalist crescent moon, 
gradient from powder pink to lavender,
dark purple cosmic background,
modern, feminine, wellness app,
1024x1024, centered, 20% padding
```

### Splash Screen (splash.png)
```
Taille : 1284x2778px (iPhone 13 Pro Max)
Format : PNG
Background : Dégradé violet→rose
Logo : LUNA centré
Texte : "Cycle & Cosmos" en dessous
Loading : Optionnel (géré nativement)
```

### Adaptive Icon Android
```
Foreground : 432x432px (logo seul, transparent)
Background : 432x432px (fond violet uni)
Safe area : 66dp (Android mask)
```

---

## 📝 Store Descriptions

### App Store (FR)

**Titre :** LUNA - Cycle & Cosmos  
**Sous-titre :** Cycle menstruel & astrologie  

**Description courte (170 caractères) :**
```
Suis ton cycle, écoute les étoiles. L'app qui relie cycle menstruel et astrologie lunaire pour ton bien-être.
```

**Description complète :** (voir section précédente)

**Keywords (100 caractères max) :**
```
cycle,menstruel,astrologie,lune,bien-être,ovulation,fertilité,horoscope,IA
```

---

### Google Play (FR)

**Titre :** LUNA - Cycle & Cosmos  
**Description courte (80 caractères) :**
```
Cycle menstruel & astrologie - Bien-être cosmique personnalisé
```

**Description complète :** (même que App Store)

**Catégorie :** Santé & Remise en forme  
**Type de contenu :** PEGI 3 / Tout public  
**Politique confidentialité :** https://luna-app.fr/privacy  
**Email support :** support@luna-app.fr

---

## 📸 Screenshots à Capturer

### 5 écrans clés :

1. **Home - Cycle & Cosmos** ✨
   - Header AUJOURD'HUI
   - Carte cycle
   - Grille Explorer

2. **Cycle & Astrologie** 🌙
   - Formulaire tracking
   - Résultats analyse
   - Recommandations

3. **Dashboard & Graphiques** 📊
   - Stats overview
   - Graphique humeur/cycle
   - Insights IA

4. **Assistant LUNA** 💬
   - Chat conversationnel
   - Réponses IA contextuelles
   - Interface moderne

5. **Thème Natal** 🪐
   - Carte du ciel
   - Positions planétaires
   - Profil astral

**Tailles iOS :**
- 6.5" (1284x2778) : iPhone 13 Pro Max, 14 Pro Max
- 5.5" (1242x2208) : iPhone 8 Plus

**Tailles Android :**
- Phone : 1080x1920
- 7" Tablet : 1200x1920
- 10" Tablet : 1600x2560

---

## 🛠️ Commandes EAS

### Setup Initial
```bash
# Installer EAS CLI
npm install -g eas-cli

# Login
eas login

# Init projet
eas init --id YOUR_PROJECT_ID

# Configuration
eas build:configure
```

### Builds
```bash
# iOS Preview (TestFlight)
eas build --platform ios --profile preview

# Android Internal (Play Store)
eas build --platform android --profile production

# Build simultané
eas build --platform all --profile production
```

### Submit
```bash
# iOS → App Store Connect
eas submit --platform ios

# Android → Play Console
eas submit --platform android
```

### Monitoring
```bash
# Status build
eas build:list

# Logs build
eas build:view [BUILD_ID]

# Cancel build
eas build:cancel [BUILD_ID]
```

---

## 📊 Métriques Beta Target

| Métrique | Cible Beta | Mesure |
|----------|------------|--------|
| **Testeurs** | 10-20 | TestFlight + Play Store |
| **Crash rate** | <1% | Sentry |
| **D1 Retention** | >60% | Mixpanel |
| **D7 Retention** | >30% | Mixpanel |
| **Feedback score** | >4/5 | Survey |
| **Bugs bloquants** | 0 | GitHub Issues |
| **Temps réponse IA** | <5s | Vercel logs |

---

## ✅ Definition of Done - Sprint 12

### Configuration
- [ ] EAS account créé et configuré
- [ ] `app.json` production ready
- [ ] `eas.json` avec 3 profiles
- [ ] Secrets configurés

### Assets
- [ ] Icône 1024x1024 créée
- [ ] Splash screen créé
- [ ] Adaptive icon Android
- [ ] Tous les formats générés

### Metadata
- [ ] Description FR complète
- [ ] Description EN traduite
- [ ] Keywords optimisés
- [ ] 5 screenshots capturés
- [ ] Privacy policy URL configurée

### Builds
- [ ] Build iOS réussi
- [ ] Upload TestFlight OK
- [ ] Build Android réussi
- [ ] Upload Play Store OK

### Beta
- [ ] 10+ testeurs invités
- [ ] App installable iOS
- [ ] App installable Android
- [ ] Feedback collecté
- [ ] Crashlytics actif

### Landing
- [ ] Page luna-app.fr live
- [ ] Badges stores fonctionnels
- [ ] Privacy policy accessible
- [ ] Contact support actif

---

## 🎯 Livrable Final Sprint 12

**LUNA 2.0.0 en BETA PUBLIQUE :**
- ✅ iOS sur TestFlight
- ✅ Android sur Play Store Internal
- ✅ Landing page live
- ✅ 10-20 testeurs actifs
- ✅ Monitoring Sentry actif
- ✅ Feedback collecté

**Prêt pour Sprint 13 : Production publique !** 🎉

---

## 🚀 C'est parti !

**Première tâche : Configuration EAS**

Je commence maintenant ! 💪

