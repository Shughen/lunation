# ⚡ CHEATSHEET - Commandes Essentielles

## 🧪 Tests

```bash
# Tests unitaires
npm test                    # Tous les tests
npm run test:watch          # Mode watch
npm run test:ci             # Tests + coverage
npm test -- home.test.js    # Test spécifique

# Tests E2E
maestro test .maestro/                              # Tous les flows
maestro test .maestro/01-onboarding-profil.yaml    # Un flow
maestro studio                                      # Mode interactif
maestro test .maestro/ --format html --output report.html  # Rapport HTML
```

## 🏗️ Builds EAS

```bash
# Development
eas build --profile development --platform ios --local     # iOS Simulator
eas build --profile development --platform android         # Android APK

# Preview
eas build --profile preview --platform all                 # iOS + Android

# Production
eas build --profile production --platform ios              # iOS App Store
eas build --profile production --platform android          # Android Play Store

# Statut
eas build:list              # Lister les builds
eas build:view BUILD_ID     # Détails d'un build
```

## 📱 Simulateurs/Émulateurs

```bash
# iOS
open -a Simulator                           # Ouvrir Simulator
xcrun simctl list devices                   # Lister les devices
xcrun simctl boot "iPhone 15 Pro"           # Démarrer un device
xcrun simctl install booted app.app         # Installer une app

# Android
emulator -list-avds                         # Lister les AVDs
emulator -avd Pixel_5_API_33                # Démarrer un AVD
adb devices                                 # Devices connectés
adb install app.apk                         # Installer une APK
```

## 🚀 Déploiement

```bash
# TestFlight (iOS)
eas submit --platform ios --latest

# Play Store (Android)
eas submit --platform android --latest --track internal

# Git tag (trigger deploy workflow)
git tag v1.0.0
git push origin v1.0.0
```

## 🔍 Quality

```bash
# Lint
npm run lint                # ESLint
npm run typecheck           # TypeScript
npm run validate            # Lint + TypeCheck + Tests

# Coverage
npm run test:ci             # Tests avec coverage
open coverage/lcov-report/index.html  # Voir le rapport
```

## 📦 Installation

```bash
# Première installation
npm install

# Après pull
npm ci                      # Clean install

# Sentry
npm install sentry-expo

# Maestro
curl -Ls "https://get.maestro.mobile.dev" | bash
```

## 🔧 Utilitaires

```bash
# Expo
npx expo start                          # Dev server
npx expo run:ios                        # Run iOS
npx expo run:android                    # Run Android
npx expo install                        # Install compatible packages

# EAS
eas whoami                              # Utilisateur connecté
eas login                               # Se connecter
eas build:configure                     # Configurer EAS
```

## 📊 Rapports

```bash
# Maestro screenshots
open ~/.maestro/tests/$(ls -t ~/.maestro/tests/ | head -1)/

# Coverage
open coverage/lcov-report/index.html

# GitHub Actions artifacts
# https://github.com/YOUR_ORG/YOUR_REPO/actions
```

---

**Copier-coller ces commandes au besoin ! 🚀**

