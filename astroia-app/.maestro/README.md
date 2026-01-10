# 🎭 Maestro E2E Tests - Astro.IA

## 📋 Flows disponibles

### 1. `01-onboarding-profil.yaml`
**Objectif :** Tester le flow complet d'onboarding et création de profil

**Étapes :**
- Lancement de l'app
- Navigation dans l'onboarding (3 écrans)
- Saisie du profil complet :
  - Nom : TestUser
  - Date de naissance : 14/04/1989
  - Heure de naissance : 16:55
  - Lieu : Livry-Gargan
- Vérification du profil créé

**Durée estimée :** ~45 secondes

---

### 2. `02-chat-ia.yaml`
**Objectif :** Tester le chat IA et la génération de réponses

**Étapes :**
- Navigation vers l'Assistant Astral
- Envoi de 2 questions :
  1. "Quel est mon signe astrologique?"
  2. "Quelle est ma compatibilité avec le Lion?"
- Vérification des réponses de l'IA
- Vérification de l'historique

**Durée estimée :** ~15 secondes (+ temps API GPT)

**⚠️ Prérequis :** API OpenAI configurée

---

### 3. `03-compatibilite-parent-enfant.yaml`
**Objectif :** Tester l'analyse de compatibilité parent-enfant

**Étapes :**
- Navigation vers "Parent-Enfant IA"
- Vérification du pré-remplissage du profil parent
- Saisie des données enfant :
  - Signe solaire : Lion
  - Ascendant : Balance
  - Signe lunaire : Poissons
- Lancement de l'analyse
- Vérification des résultats (score + conseils)
- Test du partage
- Retour au menu

**Durée estimée :** ~30 secondes

---

## 🚀 Exécution des tests

### Installation de Maestro

```bash
# macOS/Linux
curl -Ls "https://get.maestro.mobile.dev" | bash

# Ou via Homebrew
brew tap mobile-dev-inc/tap
brew install maestro
```

### Lancer les tests

#### Sur simulateur iOS
```bash
# 1. Lancer le simulateur
open -a Simulator

# 2. Builder et installer l'app
eas build --profile development --platform ios --local
npx expo run:ios

# 3. Exécuter un flow spécifique
maestro test .maestro/01-onboarding-profil.yaml

# 4. Ou tous les flows
maestro test .maestro/
```

#### Sur émulateur Android
```bash
# 1. Lancer l'émulateur
emulator -avd Pixel_5_API_33

# 2. Builder et installer l'app
eas build --profile development --platform android --local
npx expo run:android

# 3. Exécuter un flow
maestro test .maestro/02-chat-ia.yaml
```

#### Sur device physique
```bash
# iOS : Connecter via USB et autoriser
maestro test --device <UDID> .maestro/

# Android : Connecter via USB et activer ADB
adb devices
maestro test --device <DEVICE_ID> .maestro/
```

---

## 📊 Rapports et screenshots

Les screenshots sont automatiquement sauvegardés dans :
```
~/.maestro/tests/<timestamp>/
```

Pour générer un rapport HTML :
```bash
maestro test .maestro/ --format html --output report.html
```

---

## 🐛 Debugging

### Mode interactif
```bash
maestro studio
```

### Logs détaillés
```bash
maestro test .maestro/01-onboarding-profil.yaml --debug
```

### Vérifier les éléments disponibles
```bash
maestro hierarchy
```

---

## 🔧 Configuration avancée

### Variables d'environnement
Créer un fichier `.maestro/env.yaml` :
```yaml
APP_ID: com.remibeaurain.astroiaapp
API_URL: https://api.astro-ia.com
TEST_USER: testuser@example.com
```

Utiliser dans les flows :
```yaml
- tapOn: "${TEST_USER}"
```

### Conditions et boucles
```yaml
- runFlow:
    when:
      visible: "Connexion requise"
    commands:
      - tapOn: "Se connecter"
      - inputText: "test@example.com"
```

---

## ✅ CI/CD Integration

### GitHub Actions
```yaml
- name: Run Maestro E2E Tests
  run: |
    maestro test .maestro/ \
      --format junit \
      --output test-results/
```

### Bitrise
```yaml
- maestro-cloud-upload@1:
    inputs:
      - app_path: $BITRISE_IPA_PATH
      - flow_path: .maestro/
```

---

## 📚 Ressources

- [Documentation Maestro](https://maestro.mobile.dev/)
- [API Reference](https://maestro.mobile.dev/api-reference)
- [Exemples de flows](https://github.com/mobile-dev-inc/maestro/tree/main/examples)

