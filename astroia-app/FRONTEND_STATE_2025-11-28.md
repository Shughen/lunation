# État du frontend – 28/11/2025

Branche : `refactor-claude-2025-11-26-frontend`

## ✅ Ce qui fonctionne

- **Lancement de l'app Expo** : Démarrée correctement avec Metro Bundler
- **Thème natal** : Écran accessible + calcul fonctionnel (API backend connectée)
- **Navigation de base** : Onglets principaux (Home, Selena/Chat, Calendrier/Lunar-month, Profil)
- **Onboarding** : Welcome screen accessible, navigation vers profile-setup fonctionnelle
- **API Backend** : Connexion à FastAPI fonctionnelle (IP locale configurée)
- **Authentification** : Login/Signup fonctionnels
- **Routes modales** : Accès à `/natal-reading`, `/horoscope`, `/lunar-revolution`, `/settings`, `/journal` après welcome screen

## ❌ Ce qui est cassé / à vérifier

- **Révolution lunaire** : À tester (route accessible mais fonctionnalité à vérifier)
- **Cycle / historique** : À vérifier (logs indiquent "Profil incomplet, impossible de charger révolution")
- **Chat IA (Selena)** : À tester
- **Calendrier** : Warning "No route named 'calendar' exists" (route s'appelle `lunar-month`)
- **Comptabilité** : À vérifier
- **Astro du jour** : À tester (redirection vers page de garde mentionnée précédemment)

## 🎯 Priorités stabilisation

1. **Remettre la Révolution lunaire en état de marche** (si cassée)
2. **Vérifier / réparer le flux Cycle** (V2 ou V1 selon ce qui est en place)
3. **Tester la compatibilité et le chat IA**
4. **Corriger le warning "calendar"** (renommer ou adapter la route)
5. **Vérifier tous les écrans modaux** (natal-reading, horoscope, journal, etc.)

## 📝 Notes techniques

- **API Backend** : Configurée sur `http://192.168.0.150:8000` (IP locale)
- **iOS Simulator** : Utilise l'IP locale au lieu de localhost (problème React Native résolu)
- **Routing** : Logique de navigation simplifiée dans `app/index.js` (pas de routing guard pour l'instant)
- **Onboarding** : Utilise `onboarding_completed` dans AsyncStorage avec clé `'onboarding_completed'`

## 🔧 Configuration requise

- API backend doit être démarrée avec : `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`
- IP locale configurée dans `app.json` : `extra.fastApiUrl`

