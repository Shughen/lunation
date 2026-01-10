# 🔬 GUIDE COMPLET QA - Astro.IA

**Documentation complète pour les tests, CI/CD, et déploiement**

---

## 📦 Table des matières

1. [Installation des dépendances](#1-installation-des-dépendances)
2. [Tests unitaires (Jest)](#2-tests-unitaires-jest)
3. [Tests E2E (Maestro)](#3-tests-e2e-maestro)
4. [Builds EAS](#4-builds-eas)
5. [CI/CD GitHub Actions](#5-cicd-github-actions)
6. [Monitoring Sentry](#6-monitoring-sentry)
7. [Rapports et artifacts](#7-rapports-et-artifacts)

---

## 1. Installation des dépendances

### Première installation

```bash
cd astroia-app
npm install
```

### Dépendances de test

Les dépendances sont déjà configurées dans `package.json` :

```json
{
  "devDependencies": {
    "@testing-library/jest-native": "^5.4.3",
    "@testing-library/react-native": "^12.4.3",
    "jest": "^29.7.0",
    "jest-expo": "^52.0.0"
  }
}
```

---

## 2. Tests unitaires (Jest)

### 🧪 Commandes de test

#### Exécuter tous les tests
```bash
npm test
```

#### Mode watch (re-exécution automatique)
```bash
npm run test:watch
```

#### Tests avec coverage
```bash
npm run test:ci
```

#### Test d'un fichier spécifique
```bash
npm test -- app/(tabs)/__tests__/home.test.js
```

#### Tests avec pattern
```bash
npm test -- --testNamePattern="CTA"
```

### 📊 Coverage

Le rapport de coverage est généré dans `coverage/` :

```bash
# Ouvrir le rapport HTML
open coverage/lcov-report/index.html
```

**Objectifs de coverage :**
- Statements : > 80%
- Branches : > 75%
- Functions : > 80%
- Lines : > 80%

### 🎯 Tests existants

**1. Tests de l'écran Home**
- Fichier : `app/(tabs)/__tests__/home.test.js`
- Couvre :
  - Affichage du titre de bienvenue
  - Visibilité du CTA "Découvrir mon profil astral"
  - Cartes de fonctionnalités
  - Navigation vers `/profile`

**2. Tests du composant FeatureCard**
- Fichier : `components/__tests__/FeatureCard.test.js`
- Couvre :
  - Affichage du titre et description
  - Navigation au clic
  - Animation au tap

**3. Tests du hook useHapticFeedback**
- Fichier : `hooks/__tests__/useHapticFeedback.test.js`
- Couvre :
  - Retour des bonnes fonctions
  - Appel des APIs Haptics
  - Comportement platform-specific

### ✍️ Écrire de nouveaux tests

**Template de test :**

```javascript
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react-native';
import MyComponent from '../MyComponent';

describe('MyComponent', () => {
  it('devrait faire quelque chose', () => {
    render(<MyComponent />);
    
    const element = screen.getByText('Mon texte');
    expect(element).toBeTruthy();
  });
  
  it('devrait gérer les interactions', () => {
    render(<MyComponent />);
    
    const button = screen.getByText('Cliquer');
    fireEvent.press(button);
    
    expect(screen.getByText('Cliqué !')).toBeTruthy();
  });
});
```

---

## 3. Tests E2E (Maestro)

### 🎭 Installation Maestro

#### macOS/Linux
```bash
curl -Ls "https://get.maestro.mobile.dev" | bash
```

#### Homebrew
```bash
brew tap mobile-dev-inc/tap
brew install maestro
```

#### Vérifier l'installation
```bash
maestro --version
```

### 📱 Lancer les tests E2E

#### Sur iOS Simulator

**1. Démarrer le simulateur**
```bash
# Lister les simulateurs disponibles
xcrun simctl list devices

# Démarrer un simulateur spécifique
open -a Simulator
xcrun simctl boot "iPhone 15 Pro"
```

**2. Builder l'app en développement**
```bash
# Build local (rapide)
eas build --profile development --platform ios --local

# Ou installer directement
npx expo run:ios
```

**3. Exécuter les flows Maestro**

```bash
# Un flow spécifique
maestro test .maestro/01-onboarding-profil.yaml

# Tous les flows
maestro test .maestro/

# Avec screenshots
maestro test .maestro/ --format html --output maestro-report.html
```

#### Sur Android Emulator

**1. Démarrer l'émulateur**
```bash
# Lister les AVDs
emulator -list-avds

# Démarrer un AVD
emulator -avd Pixel_5_API_33
```

**2. Builder l'app**
```bash
# Build development local
eas build --profile development --platform android --local

# Ou installer directement
npx expo run:android
```

**3. Exécuter les flows**
```bash
maestro test .maestro/ --device emulator-5554
```

#### Sur device physique

**iOS :**
```bash
# 1. Connecter le device en USB
# 2. Obtenir l'UDID
idevice_id -l

# 3. Builder pour le device
eas build --profile development --platform ios --local

# 4. Installer manuellement et exécuter Maestro
maestro test .maestro/ --device <UDID>
```

**Android :**
```bash
# 1. Activer USB debugging sur le téléphone
# 2. Connecter en USB
adb devices

# 3. Exécuter les tests
maestro test .maestro/ --device <DEVICE_ID>
```

### 🧭 Flows E2E disponibles

| Flow | Description | Durée | Prérequis |
|------|-------------|-------|-----------|
| `01-onboarding-profil.yaml` | Onboarding complet + création profil | ~45s | Aucun |
| `02-chat-ia.yaml` | Chat IA avec 2 questions | ~15s | API OpenAI |
| `03-compatibilite-parent-enfant.yaml` | Analyse compatibilité parent-enfant | ~30s | Profil créé |

### 🐛 Debugging Maestro

**Mode interactif :**
```bash
maestro studio
```

**Logs détaillés :**
```bash
maestro test .maestro/01-onboarding-profil.yaml --debug
```

**Voir la hiérarchie des éléments :**
```bash
maestro hierarchy
```

**Enregistrer un nouveau flow :**
```bash
maestro record my-new-flow.yaml
```

---

## 4. Builds EAS

### 🔧 Configuration EAS

**Créer `eas.json` :**

```json
{
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
      "ios": {
        "simulator": false
      },
      "android": {
        "buildType": "apk"
      }
    },
    "production": {
      "distribution": "store",
      "ios": {
        "simulator": false
      },
      "android": {
        "buildType": "aab"
      }
    }
  }
}
```

### 📲 Builds de développement

#### iOS Simulator (pour tests locaux)

```bash
# Build et téléchargement automatique
eas build --profile development --platform ios --local

# Le .app sera dans le dossier de build
# Installer sur le simulateur :
xcrun simctl install booted path/to/app.app
```

#### Android APK (pour tests sur device)

```bash
# Build development APK
eas build --profile development --platform android

# Télécharger l'APK depuis EAS
# URL fournie dans la console

# Installer sur device connecté :
adb install path/to/app.apk
```

### 🚀 Builds de production

#### iOS App Store

```bash
# 1. Build pour production
eas build --profile production --platform ios

# 2. Attendre la fin du build (~15-20 min)

# 3. Soumettre à l'App Store
eas submit --platform ios --latest

# Configuration requise :
# - EXPO_APPLE_APP_SPECIFIC_PASSWORD dans les secrets
# - Apple Developer Program membership
```

#### Android Play Store

```bash
# 1. Build AAB pour production
eas build --profile production --platform android

# 2. Soumettre au Play Store
eas submit --platform android --latest

# Configuration requise :
# - Google Service Account JSON dans EAS
# - App créée dans Google Play Console
```

### 📦 Builds pour preview/beta

```bash
# iOS TestFlight
eas build --profile preview --platform ios
eas submit --platform ios --latest --apple-team-id YOUR_TEAM_ID

# Android Internal Testing
eas build --profile preview --platform android
eas submit --platform android --latest --track internal
```

### 🔍 Vérifier le statut des builds

```bash
# Lister tous les builds
eas build:list

# Voir les détails d'un build spécifique
eas build:view <BUILD_ID>

# Annuler un build en cours
eas build:cancel <BUILD_ID>
```

---

## 5. CI/CD GitHub Actions

### 🤖 Workflows configurés

#### 1. **CI Workflow** (`.github/workflows/ci.yml`)

Déclenché sur : `push` et `pull_request` vers `main` et `develop`

**Jobs :**
- ✅ Lint & TypeCheck
- ✅ Unit Tests avec coverage
- ⏸️ E2E Tests (commenté)
- ✅ Build Preview (sur PR)
- ✅ Sentry Release (sur main)

**Exécution :**
- Automatique à chaque push/PR
- Durée totale : ~5-10 min

#### 2. **Deploy Workflow** (`.github/workflows/deploy.yml`)

Déclenché sur : création de tag `v*`

**Jobs :**
- 🏗️ Build production iOS
- 🏗️ Build production Android
- 🚀 Submit App Store
- 🚀 Submit Play Store

**Exécution :**
```bash
# Créer un tag pour déclencher le déploiement
git tag v1.0.0
git push origin v1.0.0
```

### 🔑 Secrets GitHub à configurer

Dans `Settings > Secrets and variables > Actions` :

| Secret | Description | Requis pour |
|--------|-------------|-------------|
| `EXPO_TOKEN` | Token EAS CLI | Tous les builds |
| `CODECOV_TOKEN` | Token Codecov | Coverage reports |
| `SENTRY_AUTH_TOKEN` | Token Sentry | Releases Sentry |
| `SENTRY_ORG` | Organisation Sentry | Releases Sentry |
| `EXPO_APPLE_APP_SPECIFIC_PASSWORD` | Password Apple | Submission iOS |
| `GITHUB_TOKEN` | Auto-généré par GitHub | PR comments |

**Obtenir EXPO_TOKEN :**
```bash
eas whoami
eas login
# Token sera affiché ou créé via : https://expo.dev/accounts/[account]/settings/access-tokens
```

### 📊 Artifacts CI/CD

Les artifacts sont disponibles dans l'onglet "Actions" de GitHub :

- ✅ Coverage report (`coverage/`)
- ✅ Test results (`test-results/`)
- ✅ Maestro screenshots (si E2E activé)
- ✅ Build logs

---

## 6. Monitoring Sentry

### 🔍 Configuration

**1. Créer un compte Sentry**
- Aller sur https://sentry.io
- Créer projet React Native

**2. Récupérer le DSN**
```
https://YOUR_KEY@o0.ingest.sentry.io/YOUR_PROJECT_ID
```

**3. Configurer dans `app.json`**
```json
{
  "extra": {
    "sentryDsn": "https://abc123...@o987654.ingest.sentry.io/1234567"
  }
}
```

**4. Installer la dépendance**
```bash
npm install sentry-expo
```

**5. Initialiser dans `app/_layout.js`**
```javascript
import { initSentry } from '@/lib/sentry';

useEffect(() => {
  initSentry();
}, []);
```

### 📈 Utilisation

**Capturer une erreur :**
```javascript
import { captureError } from '@/lib/sentry';

try {
  await riskyOperation();
} catch (error) {
  captureError(error, { module: 'compatibility' });
}
```

**Définir l'utilisateur :**
```javascript
import { setUser } from '@/lib/sentry';

setUser({
  id: user.id,
  email: user.email,
  name: user.name,
});
```

**Ajouter des breadcrumbs :**
```javascript
import { addBreadcrumb } from '@/lib/sentry';

addBreadcrumb('User clicked analyze', 'user-action');
```

### 🐛 Debug Sentry

```bash
# Tester l'envoi en dev
import Sentry from '@/lib/sentry';
Sentry.Native.captureMessage('Test from dev');

# Vérifier les événements dans le dashboard Sentry
```

---

## 7. Rapports et artifacts

### 📊 Coverage Report

**Générer localement :**
```bash
npm run test:ci
open coverage/lcov-report/index.html
```

**Dans CI/CD :**
- Uploadé automatiquement sur Codecov
- Visible dans les PR comments

### 📸 Screenshots Maestro

**Emplacement local :**
```
~/.maestro/tests/<timestamp>/
```

**Lister les runs :**
```bash
ls -la ~/.maestro/tests/
```

**Générer un rapport HTML :**
```bash
maestro test .maestro/ --format html --output maestro-report.html
open maestro-report.html
```

### 📦 Builds EAS

**Télécharger un build :**
```bash
# Via CLI
eas build:view <BUILD_ID>

# Ou via web
# https://expo.dev/accounts/[account]/projects/astroia-app/builds
```

### 🐛 Logs et debugging

**Logs des tests :**
```bash
# Jest
npm test -- --verbose

# Maestro
maestro test .maestro/ --debug > maestro.log
```

**Logs des builds :**
```bash
# EAS
eas build:view <BUILD_ID> --logs

# Ou dans le dashboard :
# https://expo.dev/accounts/[account]/projects/astroia-app/builds/[BUILD_ID]
```

---

## 🚀 Quick Start

### Premier test complet

```bash
# 1. Installer les dépendances
npm install

# 2. Lancer les tests unitaires
npm test

# 3. Builder l'app de dev (iOS)
eas build --profile development --platform ios --local

# 4. Installer Maestro
curl -Ls "https://get.maestro.mobile.dev" | bash

# 5. Démarrer le simulateur
open -a Simulator

# 6. Exécuter les tests E2E
maestro test .maestro/

# 7. Voir les résultats
open ~/.maestro/tests/$(ls -t ~/.maestro/tests/ | head -1)/
```

### Checklist avant production

- [ ] Tous les tests unitaires passent (`npm test`)
- [ ] Coverage > 80% (`npm run test:ci`)
- [ ] Tests E2E passent (`maestro test .maestro/`)
- [ ] Lint sans erreurs (`npm run lint`)
- [ ] TypeCheck sans erreurs (`npm run typecheck`)
- [ ] Sentry configuré et testé
- [ ] Build iOS réussi (`eas build --profile production --platform ios`)
- [ ] Build Android réussi (`eas build --profile production --platform android`)
- [ ] Secrets GitHub configurés
- [ ] CI/CD passe sur `main`

---

## 📚 Ressources

### Documentation
- [Jest](https://jestjs.io/)
- [Testing Library React Native](https://callstack.github.io/react-native-testing-library/)
- [Maestro](https://maestro.mobile.dev/)
- [EAS Build](https://docs.expo.dev/build/introduction/)
- [Sentry](https://docs.sentry.io/platforms/react-native/)

### Outils
- [Codecov](https://codecov.io/)
- [GitHub Actions](https://github.com/features/actions)

---

**✅ Stack QA complète installée et prête ! 🎉**

