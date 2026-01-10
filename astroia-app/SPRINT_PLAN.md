# 🚀 PLAN D'ACTION – LUNA - Cycle & Cosmos

> Roadmap sprint par sprint pour pivoter Astro.IA vers LUNA

**Objectif :** Lancer la beta publique en 4-6 semaines  
**Date de début :** 9 novembre 2025  
**Cible :** 200 testeuses qualifiées pour la beta

---

## 📊 Vue d'Ensemble

| Sprint | Durée | Objectif | Status |
|--------|-------|----------|--------|
| **Sprint 9** | 1 semaine | Onboarding & Settings | 🔵 À faire |
| **Sprint 10** | 1 semaine | Dashboard & Graphiques | 🔵 À faire |
| **Sprint 11** | 1-2 semaines | Polish & QA | 🔵 À faire |
| **Sprint 12** | 1-2 semaines | Beta & Go-to-market | 🔵 À faire |

---

## 🎯 SPRINT 9 : Onboarding & Settings

**Durée :** 1 semaine (11-17 novembre 2025)  
**Objectif :** Créer l'expérience d'accueil et les paramètres complets

### 📋 User Stories

#### US9.1 : Onboarding Complet
**En tant que** nouvelle utilisatrice  
**Je veux** un onboarding fluide et engageant  
**Afin de** comprendre rapidement la valeur de LUNA et configurer mon profil

**Critères d'acceptation :**
- [ ] Écran 1 : Splash avec logo LUNA + tagline "Suis ton cycle, écoute les étoiles"
- [ ] Écran 2 : Proposition de valeur (3 bénéfices clés avec illustrations)
- [ ] Écran 3 : Config profil simplifié (nom, email, date de naissance)
- [ ] Écran 4 : Config cycle (date dernières règles, durée moyenne cycle)
- [ ] Écran 5 : Tour guidé (3 slides : Cycle, Journal, IA)
- [ ] Écran 6 : Disclaimer bien-être (acceptation obligatoire)
- [ ] Navigation fluide avec boutons "Suivant" / "Précédent"
- [ ] Sauvegarde état onboarding (reprise si fermeture app)
- [ ] Redirection vers Home "Aujourd'hui" après complétion
- [ ] Analytics : `trackEvents.onboardingCompleted()`

**Fichiers à créer :**
```
app/onboarding/
├── index.js              # Entry point
├── welcome.js            # Écran 1-2
├── profile-setup.js      # Écran 3
├── cycle-setup.js        # Écran 4
├── tour.js               # Écran 5
└── disclaimer.js         # Écran 6
```

**Design specs :**
- Palette : Rose poudré + Lavande + Violet cosmique
- Animations : Fade-in progressive, slide entre écrans
- Illustrations : Lune stylisée, calendrier, chat bulle

---

#### US9.2 : Page Settings Complète
**En tant qu'** utilisatrice  
**Je veux** gérer mes paramètres et mes données  
**Afin de** contrôler mon expérience et ma confidentialité

**Critères d'acceptation :**
- [ ] **Section Profil**
  - Modifier nom, email, date de naissance
  - Modifier heure/lieu de naissance (optionnel)
  - Recalcul automatique thème astral
- [ ] **Section Cycle**
  - Modifier durée moyenne cycle
  - Historique des règles (liste dernières dates)
  - Bouton "Nouvelle période" (update cycle)
- [ ] **Section Notifications**
  - Toggle rappel journal quotidien (heure personnalisable)
  - Toggle alerte changement de phase
  - Toggle transits lunaires importants
  - Test notification (bouton)
- [ ] **Section Confidentialité**
  - Voir politique de confidentialité (DATA_POLICY.md)
  - Export données JSON (bouton)
  - Export données PDF (dernier mois)
  - Toggle analytics Mixpanel
  - Supprimer compte (avec confirmation double)
- [ ] **Section Apparence**
  - Toggle thème clair/sombre (optionnel Sprint 9, peut attendre)
  - Taille police (A-, A, A+) (optionnel)
- [ ] **Section À propos**
  - Version app
  - Disclaimer médical (DISCLAIMER.md)
  - CGU (à venir)
  - Contact support
  - Crédits (Supabase, OpenAI, Vercel)

**Fichiers à créer :**
```
app/settings/
├── index.js              # Page principale
├── profile.js            # Sous-page profil
├── cycle.js              # Sous-page cycle
├── notifications.js      # Sous-page notifications
├── privacy.js            # Sous-page confidentialité
└── about.js              # Sous-page à propos

lib/
├── exportService.js      # Export JSON/PDF
└── notificationService.js # Gestion notifications
```

---

#### US9.3 : Export Données
**En tant qu'** utilisatrice  
**Je veux** exporter mes données  
**Afin de** les sauvegarder ou les transférer

**Critères d'acceptation :**
- [ ] Export JSON :
  - Profil complet
  - Toutes entrées journal
  - Historique cycle
  - Analyses sauvegardées
  - Conversations IA (optionnel)
- [ ] Export PDF :
  - En-tête avec logo LUNA
  - Section profil
  - Graphique mood 30 jours
  - Liste entrées journal du mois
  - Stats du mois
- [ ] Partage via Share API native (iOS/Android)
- [ ] Analytics : `trackEvents.exportPDF(period_length)`

---

#### US9.4 : Notifications Push Setup
**En tant qu'** utilisatrice  
**Je veux** recevoir des rappels utiles  
**Afin de** maintenir mon tracking quotidien

**Critères d'acceptation :**
- [ ] Demande permission notifications (onboarding ou settings)
- [ ] Notifications locales programmables :
  - "N'oublie pas ton journal du jour 📖" (heure personnalisable)
  - "Tu entres en phase [X] aujourd'hui 🌙" (automatique)
  - "Pleine lune ce soir - énergie maximale ✨" (calcul automatique)
- [ ] Badge app non intrusif
- [ ] Bouton "Tester notification" dans Settings

**Package :**
```bash
npx expo install expo-notifications
```

---

#### US9.5 : Branding LUNA (soft rebrand)
**En tant qu'** utilisatrice  
**Je veux** voir l'identité LUNA  
**Afin de** comprendre que l'app est spécialisée cycle

**Critères d'acceptation :**
- [ ] Splash screen : Logo LUNA + tagline
- [ ] Home : Titre "LUNA - Cycle & Cosmos"
- [ ] Navigation : Renommer onglets si nécessaire
- [ ] Couleurs : Palette rose poudré dominant
- [ ] Footer : "LUNA - Suis ton cycle, écoute les étoiles"
- [ ] Pas de changement bundle ID (reste astro-ia)

---

### 🧪 Tests Sprint 9

**Tests Jest :**
```javascript
// __tests__/onboarding.test.js
- Navigation entre écrans onboarding
- Sauvegarde état onboarding
- Validation formulaire profil
- Validation formulaire cycle

// __tests__/settings.test.js
- Toggle notifications
- Export JSON
- Export PDF
- Suppression compte (mock)

// __tests__/exportService.test.js
- Génération JSON valide
- Génération PDF
```

**Tests Maestro :**
```yaml
# .maestro/09_onboarding_flow.yaml
- Compléter onboarding du début à la fin
- Vérifier redirection Home
- Vérifier sauvegarde données

# .maestro/09_settings_flow.yaml
- Ouvrir Settings
- Modifier profil
- Activer notifications
- Exporter JSON
- Revenir Home
```

---

### 📦 Livrables Sprint 9

- [ ] Onboarding complet (6 écrans)
- [ ] Settings complet (5 sous-pages)
- [ ] Export JSON/PDF fonctionnel
- [ ] Notifications setup
- [ ] Branding LUNA visible
- [ ] Tests Jest verts
- [ ] Tests Maestro exécutables
- [ ] Analytics intégré (lib/analytics.js)
- [ ] Documentation DISCLAIMER.md + DATA_POLICY.md
- [ ] README_Analytics.md

---

## 📊 SPRINT 10 : Dashboard & Graphiques

**Durée :** 1 semaine (18-24 novembre 2025)  
**Objectif :** Rendre visibles les corrélations cycle-humeur-transits

### 📋 User Stories

#### US10.1 : Home "Aujourd'hui" Refonte
**En tant qu'** utilisatrice  
**Je veux** voir l'essentiel de ma journée  
**Afin de** comprendre mon état actuel

**Critères d'acceptation :**
- [ ] Carte principale "Aujourd'hui" :
  - Phase du cycle actuelle (emoji + nom + jour X/28)
  - Transit lunaire du jour (signe + emoji)
  - Niveau d'énergie estimé (barre colorée 0-100%)
  - 1 conseil IA contextuel (généré selon phase + transit)
- [ ] Carte "Ton journal" :
  - Dernière entrée (mood + date)
  - Bouton "+ Nouvelle entrée"
  - Mini-graphique 7 derniers jours
- [ ] Carte "Cette semaine" :
  - Prochaine phase (dans X jours)
  - Prochaine pleine lune (dans X jours)
  - Suggestion activité
- [ ] Navigation rapide vers Cycle, Journal, Dashboard
- [ ] Animation fade-in au chargement
- [ ] Pull-to-refresh

**Fichiers à modifier :**
```
app/(tabs)/home.js        # Refonte complète
components/TodayCard.js   # Carte "Aujourd'hui"
components/JournalCard.js # Carte "Journal"
components/WeekCard.js    # Carte "Cette semaine"
```

---

#### US10.2 : Graphiques Cycle & Humeur
**En tant qu'** utilisatrice  
**Je veux** visualiser mes patterns  
**Afin de** mieux comprendre mes variations

**Critères d'acceptation :**
- [ ] **Graphique 30 jours** (Mood vs Cycle) :
  - Axe X : Jours (1-30)
  - Axe Y : Humeur (1-5 étoiles)
  - Background coloré par phase du cycle
  - Points cliquables (détail entrée)
  - Smooth curve
- [ ] **Graphique 90 jours** (Énergie vs Phase) :
  - Courbe énergie moyenne par phase
  - Comparaison 3 derniers cycles
  - Légende claire
- [ ] **Heatmap Cycle** (Calendrier) :
  - Vue mensuelle
  - Couleurs par phase
  - Mood par jour (emoji)
  - Cliquable → détail jour
- [ ] Export graphiques en image (PNG)

**Package :**
```bash
npm install react-native-chart-kit
# ou
npm install victory-native
```

**Fichiers à créer :**
```
components/charts/
├── MoodCycleChart.js     # Graphique 30j
├── EnergyCycleChart.js   # Graphique 90j
├── CycleHeatmap.js       # Calendrier
└── chartUtils.js         # Helpers

lib/
└── chartDataService.js   # Préparation données
```

---

#### US10.3 : Dashboard Insights IA
**En tant qu'** utilisatrice  
**Je veux** des insights automatiques  
**Afin de** découvrir mes patterns sans effort

**Critères d'acceptation :**
- [ ] Section "Insights" dans Dashboard :
  - "Tu es plus énergique en phase folliculaire" (auto-détecté)
  - "Tes meilleurs jours créatifs : J10-J14" (corrélation tags)
  - "Tu journalises plus en phase lutéale" (stats)
  - "Ta lune en [Signe] influence ton humeur" (astro)
- [ ] 3-5 insights maximum (les plus pertinents)
- [ ] Génération automatique chaque semaine
- [ ] Bouton "Rafraîchir insights"
- [ ] Explication simple pour chaque insight

**Algorithme :**
```python
# Pseudo-code
def generate_insights(user_data):
  insights = []
  
  # Énergie par phase
  energy_by_phase = calculate_avg_energy_by_phase(user_data)
  best_phase = max(energy_by_phase)
  insights.append(f"Tu es plus énergique en phase {best_phase}")
  
  # Tags populaires par phase
  tags_by_phase = count_tags_by_phase(user_data)
  insights.append(correlate_tags_phase(tags_by_phase))
  
  # Fréquence journaling
  freq_by_phase = count_entries_by_phase(user_data)
  insights.append(f"Tu journalises plus en phase {max(freq_by_phase)}")
  
  return insights[:5]
```

---

#### US10.4 : Journal Enrichi Auto-Tagging
**En tant qu'** utilisatrice  
**Je veux** des suggestions de tags intelligentes  
**Afin de** gagner du temps et mieux catégoriser

**Critères d'acceptation :**
- [ ] Suggestions contextuelles :
  - Phase menstruelle → tags "repos", "hydratation", "douceur"
  - Phase folliculaire → tags "énergie", "créativité", "nouveau"
  - Phase ovulation → tags "social", "communication", "confiance"
  - Phase lutéale → tags "organisation", "introspection", "cocooning"
- [ ] Transit lunaire :
  - Lune en Bélier → tag "initiative"
  - Lune en Taureau → tag "ancrage"
  - Lune en Gémeaux → tag "communication"
  - etc.
- [ ] Tags personnalisés (création libre)
- [ ] Historique tags (fréquence d'utilisation)
- [ ] Max 5 tags par entrée

---

#### US10.5 : Calendrier Cycle Visuel
**En tant qu'** utilisatrice  
**Je veux** voir mon cycle dans un calendrier  
**Afin de** planifier mes activités

**Critères d'acceptation :**
- [ ] Vue mensuelle (grid 7x5)
- [ ] Couleurs par phase :
  - Menstruelle : Rouge doux
  - Folliculaire : Orange pêche
  - Ovulation : Jaune doré
  - Lutéale : Violet lavande
- [ ] Indicateurs :
  - 🩸 Jours de règles
  - 🥚 Ovulation estimée
  - 📖 Jours avec entrée journal
  - ⭐ Jours importants (custom)
- [ ] Tap sur jour → détail (humeur, notes, transit)
- [ ] Navigation mois précédent/suivant
- [ ] Légende en bas

**Package :**
```bash
npm install react-native-calendars
```

---

### 🧪 Tests Sprint 10

**Tests Jest :**
```javascript
// __tests__/charts.test.js
- Génération données graphiques
- Calcul moyennes par phase
- Edge cases (peu de données)

// __tests__/insights.test.js
- Génération insights automatiques
- Pertinence insights
- Limite 5 insights max
```

**Tests Maestro :**
```yaml
# .maestro/10_dashboard_flow.yaml
- Ouvrir Dashboard
- Voir graphiques
- Interagir avec graphique (tap point)
- Swiper entre 30j/90j
- Voir insights

# .maestro/10_calendar_flow.yaml
- Ouvrir calendrier cycle
- Naviguer entre mois
- Tap sur jour
- Voir détails jour
```

---

### 📦 Livrables Sprint 10

- [ ] Home "Aujourd'hui" refonte complète
- [ ] 3 graphiques fonctionnels (30j, 90j, heatmap)
- [ ] Insights IA automatiques
- [ ] Auto-tagging journal
- [ ] Calendrier cycle visuel
- [ ] Tests Jest verts
- [ ] Tests Maestro exécutables
- [ ] Performance optimisée (graphiques fluides)

---

## 🎨 SPRINT 11 : Polish & QA

**Durée :** 1-2 semaines (25 nov - 8 déc 2025)  
**Objectif :** Stabilité, accessibilité, expérience parfaite

### 📋 User Stories

#### US11.1 : Assistant IA Spécialisé Cycle
**En tant qu'** utilisatrice  
**Je veux** des conseils pertinents à ma phase  
**Afin de** mieux gérer mon énergie

**Critères d'acceptation :**
- [ ] Prompt système enrichi :
  ```
  Tu es LUNA, assistant bien-être spécialisé dans le cycle menstruel et l'astrologie.
  
  Profil utilisatrice :
  - Nom : {name}
  - Signe solaire : {sun_sign}
  - Signe lunaire : {moon_sign}
  - Phase actuelle : {current_phase} (Jour {day_of_cycle}/28)
  - Transit lunaire : Lune en {moon_transit}
  - Humeur 7 derniers jours : {mood_history}
  
  Directives :
  - Conseils concrets, bienveillants, non médicaux
  - Suggestions routines selon phase
  - Nutrition, mouvement, repos adaptés
  - Pas de diagnostic ni traitement
  - Rappel : consulter médecin si besoin
  ```
- [ ] Réponses courtes (150-250 mots max)
- [ ] Ton doux, inclusif, positif
- [ ] Exemples de questions suggérées :
  - "Comment gérer ma fatigue aujourd'hui ?"
  - "Quelle activité faire en phase folliculaire ?"
  - "Pourquoi je me sens irritable ?"
  - "Conseils nutrition phase ovulation"

---

#### US11.2 : Accessibilité (A11y)
**En tant qu'** utilisatrice malvoyante ou avec handicap  
**Je veux** utiliser l'app facilement  
**Afin de** bénéficier de LUNA comme tout le monde

**Critères d'acceptation :**
- [ ] **VoiceOver / TalkBack** :
  - Tous boutons ont accessibilityLabel
  - Navigation au clavier fonctionnelle
  - Ordre de lecture logique
- [ ] **Contraste** :
  - Ratio minimum 4.5:1 (WCAG AA)
  - Texte lisible sur tous fonds
- [ ] **Taille police** :
  - Respect des réglages système (Dynamic Type iOS)
  - Option A-, A, A+ dans Settings
- [ ] **Tap targets** :
  - Minimum 44x44 pts (iOS HIG)
  - Espacement suffisant
- [ ] **Focus visible** :
  - Outline sur éléments actifs (navigation clavier)

**Outil de test :**
```bash
npx @react-native-community/cli doctor
# Vérifier warnings accessibilité
```

---

#### US11.3 : Performance & Optimisation
**En tant qu'** utilisatrice  
**Je veux** une app fluide et rapide  
**Afin de** ne pas perdre de temps

**Critères d'acceptation :**
- [ ] **Temps de chargement** :
  - Cold start < 3s
  - Navigation entre écrans < 300ms
  - Graphiques render < 1s
- [ ] **Animations 60fps** :
  - Utiliser `useNativeDriver: true` partout
  - Pas de lag scroll
- [ ] **Optimisation images** :
  - WebP format
  - Lazy loading
  - Cache local
- [ ] **Bundle size** :
  - < 30MB total
  - Code splitting si possible
- [ ] **Mémoire** :
  - Pas de memory leaks
  - Libérer ressources (cleanup useEffect)

**Outils :**
```bash
# Analyser bundle
npx react-native-bundle-visualizer

# Profiler performance
# Dans Chrome DevTools avec Flipper
```

---

#### US11.4 : Monitoring & Crash Tracking
**En tant que** dev  
**Je veux** détecter les bugs en production  
**Afin de** corriger rapidement

**Critères d'acceptation :**
- [ ] **Sentry** configuré :
  - Capture crashes JS
  - Capture erreurs API
  - Source maps uploadés
  - Environnements séparés (dev/staging/prod)
- [ ] **Expo Insights** (optionnel) :
  - Statistiques usage
  - Crashs natifs
- [ ] **Custom error boundaries** :
  - Écran d'erreur gracieux
  - Bouton "Réessayer"
  - Log automatique dans Sentry

**Setup Sentry :**
```bash
npm install @sentry/react-native
npx @sentry/wizard -i reactNative -p ios android
```

```javascript
// app/_layout.js
import * as Sentry from '@sentry/react-native';

Sentry.init({
  dsn: 'TON_DSN_SENTRY',
  environment: __DEV__ ? 'development' : 'production',
  tracesSampleRate: 1.0,
});
```

---

#### US11.5 : QA Complète & Tests E2E
**En tant que** QA  
**Je veux** valider tous les flows  
**Afin de** garantir zéro bug critique

**Critères d'acceptation :**
- [ ] **Tests Maestro complets** :
  - Onboarding complet
  - Création journal
  - Chat IA
  - Dashboard navigation
  - Settings modifications
  - Export données
  - Cycle tracking
- [ ] **Tests Jest exhaustifs** :
  - Coverage > 70%
  - Tous services API testés
  - Tous utils testés
- [ ] **Tests manuels** :
  - iOS (simulator + real device)
  - Android (emulator + real device)
  - Edge cases (pas de connexion, profil vide, etc.)

**Checklist QA manuelle :**
```markdown
## Fonctionnel
- [ ] Onboarding complet sans crash
- [ ] Login/Logout fonctionnel
- [ ] Profil sauvegarde correctement
- [ ] Journal crée/édite/supprime
- [ ] Chat IA répond en <3s
- [ ] Dashboard affiche stats
- [ ] Graphiques render correctement
- [ ] Notifications reçues
- [ ] Export JSON valide
- [ ] Export PDF généré

## UX
- [ ] Animations fluides
- [ ] Pas de flicker
- [ ] Loading states clairs
- [ ] Messages d'erreur utiles
- [ ] Navigation intuitive
- [ ] Retour arrière fonctionne

## Edge Cases
- [ ] Offline mode graceful
- [ ] Profil incomplet géré
- [ ] Pas de données (empty states)
- [ ] Erreurs API gérées
- [ ] Champs vides validés

## Devices
- [ ] iPhone 12 (iOS 16)
- [ ] iPhone 14 Pro Max (iOS 17)
- [ ] Samsung Galaxy S21 (Android 12)
- [ ] Pixel 6 (Android 13)
```

---

### 📦 Livrables Sprint 11

- [ ] IA spécialisée cycle fonctionnelle
- [ ] Accessibilité A11y complète
- [ ] Performance optimisée (60fps)
- [ ] Sentry configuré
- [ ] Tests Jest coverage >70%
- [ ] Tests Maestro complets
- [ ] QA manuelle validée
- [ ] Bug fixes (critiques à 0)

---

## 🚀 SPRINT 12 : Beta & Go-to-Market

**Durée :** 1-2 semaines (9-22 déc 2025)  
**Objectif :** Lancer beta publique et commencer acquisition

### 📋 User Stories

#### US12.1 : Build Production EAS
**En tant que** dev  
**Je veux** des builds production  
**Afin de** distribuer sur TestFlight et Play Store

**Critères d'acceptation :**
- [ ] **EAS Setup** :
  ```bash
  npm install -g eas-cli
  eas login
  eas build:configure
  ```
- [ ] **eas.json** configuré :
  ```json
  {
    "build": {
      "development": {
        "developmentClient": true,
        "distribution": "internal"
      },
      "preview": {
        "distribution": "internal",
        "ios": { "simulator": true }
      },
      "production": {
        "distribution": "store"
      }
    }
  }
  ```
- [ ] **Build iOS** :
  ```bash
  eas build --platform ios --profile preview
  ```
- [ ] **Build Android** :
  ```bash
  eas build --platform android --profile preview
  ```
- [ ] **TestFlight upload** (iOS)
- [ ] **Play Store Internal Testing** (Android)

---

#### US12.2 : Landing Page Minimale
**En tant que** visiteur web  
**Je veux** comprendre LUNA  
**Afin de** rejoindre la beta

**Critères d'acceptation :**
- [ ] **Page unique** (Vercel) :
  - Hero : Logo + Tagline + CTA "Rejoins la beta"
  - Section "Comment ça marche" (3 étapes)
  - Section "Fonctionnalités" (4 cards)
  - Section "À propos" (histoire authentique)
  - Section "Rejoins-nous" (formulaire email)
  - Footer (contact, mentions légales)
- [ ] **Formulaire capture email** :
  - Intégration Formspree ou Supabase
  - Validation email
  - Confirmation automatique
- [ ] **Design cohérent** :
  - Palette LUNA (rose, lavande, violet)
  - Responsive mobile-first
  - Animations douces
- [ ] **SEO basique** :
  - Meta tags (title, description)
  - OG tags (partage réseaux sociaux)
  - Favicon
  - Google Analytics

**Stack :**
```bash
npx create-next-app luna-landing
# ou Astro, ou simple HTML/CSS
```

**Deploy :**
```bash
vercel --prod
```

---

#### US12.3 : Assets Store (Screenshots & Visuels)
**En tant que** user store  
**Je veux** voir l'app avant de télécharger  
**Afin de** décider si elle me convient

**Critères d'acceptation :**
- [ ] **Screenshots iOS** (6-8) :
  1. Home "Aujourd'hui"
  2. Journal avec graphique
  3. Chat IA
  4. Dashboard insights
  5. Calendrier cycle
  6. Onboarding
- [ ] **Screenshots Android** (6-8) : idem
- [ ] **Textes store** :
  - Titre : "LUNA - Cycle & Cosmos"
  - Sous-titre : "Suis ton cycle, écoute les étoiles"
  - Description courte (170 car)
  - Description longue (4000 car)
  - Mots-clés (30 max)
- [ ] **Icône app** :
  - 1024x1024 px
  - Lune stylisée
  - Palette LUNA
- [ ] **Vidéo preview** (optionnel) :
  - 15-30s
  - Démo rapide features

**Outils :**
- Figma / Sketch pour design
- Shotbot / Mockuuups pour mockups
- Apple Guidelines / Material Design

---

#### US12.4 : Beta Testing Program
**En tant que** beta tester  
**Je veux** donner mon feedback  
**Afin d'** aider à améliorer LUNA

**Critères d'acceptation :**
- [ ] **TestFlight** (iOS) :
  - Groupe "Beta Privée" (20 pers)
  - Groupe "Beta Publique" (100 pers)
  - Formulaire feedback intégré
- [ ] **Play Store Internal Testing** (Android) :
  - Groupe "Testers Internes" (20 pers)
  - Groupe "Beta Ouverte" (100 pers)
- [ ] **Canal feedback** :
  - Formulaire in-app (Settings > Feedback)
  - Email dédié : beta@luna-app.fr
  - Discord/Telegram (optionnel)
- [ ] **Enquête satisfaction** :
  - Google Form envoyé J+7
  - 10 questions max
  - NPS (Net Promoter Score)
- [ ] **Suivi analytics** :
  - Dashboards Mixpanel actifs
  - Rapport hebdo automatique

---

#### US12.5 : Communication Lancement
**En tant que** fondateur  
**Je veux** annoncer LUNA  
**Afin d'** attirer les premiers utilisateurs

**Critères d'acceptation :**
- [ ] **Post LinkedIn** :
  - Histoire du projet
  - Problème résolu
  - CTA rejoindre beta
- [ ] **Post Instagram/TikTok** :
  - Carousel features
  - Vidéo démo 30s
  - Link in bio
- [ ] **Email liste** (si existante) :
  - Annonce lancement beta
  - Lien TestFlight/Play Store
- [ ] **Communautés** (Reddit, forums) :
  - r/astrologie
  - r/cyclemenstruel (si existe)
  - Groupes Facebook bien-être féminin
- [ ] **Presse / Influenceurs** (optionnel) :
  - Email pitchs courts (5 contacts)
  - Kit presse (screenshots, texte)

---

### 📊 Métriques de Succès Beta

**Semaine 1-2 :**
- 50 inscrits
- 85% complètent onboarding
- 60% D1 retention

**Semaine 3-4 :**
- 100 inscrits
- 3 journaux/sem/user
- 35% D7 retention

**Mois 1-2 :**
- 200 inscrits
- 5% conversion premium (10 users)
- 18% D30 retention
- Note >4.5/5

---

### 📦 Livrables Sprint 12

- [ ] Builds iOS + Android production
- [ ] TestFlight + Play Store beta live
- [ ] Landing page déployée
- [ ] Assets store complets
- [ ] Communication lancée
- [ ] 50 premiers beta testers
- [ ] Analytics trackés
- [ ] Feedback collecté

---

## 📅 Calendrier Récapitulatif

| Semaine | Dates | Sprint | Jalons |
|---------|-------|--------|--------|
| **S46** | 11-17 nov | Sprint 9 | Onboarding + Settings |
| **S47** | 18-24 nov | Sprint 10 | Dashboard + Graphiques |
| **S48** | 25 nov - 1 déc | Sprint 11 (1) | IA Cycle + A11y |
| **S49** | 2-8 déc | Sprint 11 (2) | QA + Polish |
| **S50** | 9-15 déc | Sprint 12 (1) | Builds + Landing |
| **S51** | 16-22 déc | Sprint 12 (2) | Beta lancée 🚀 |

---

## ✅ Definition of Done

**Une user story est "Done" quand :**
- [ ] Code écrit et testé localement
- [ ] Tests Jest écrits et verts
- [ ] Tests Maestro écrits (si applicable)
- [ ] ESLint clean (pas d'erreurs)
- [ ] Code review fait (si équipe)
- [ ] Docs mises à jour (README, CHANGELOG)
- [ ] Analytics trackés (si applicable)
- [ ] Testé sur iOS + Android
- [ ] Merged dans `main`

---

## 🎯 KPIs Globaux à Suivre

### Activation
- **Taux complétion onboarding** : >85%
- **Temps moyen onboarding** : <3 min

### Engagement
- **DAU/MAU ratio** : >30%
- **Sessions/jour** : >1.5
- **Entrées journal/sem** : >3
- **Messages IA/sem** : >2

### Rétention
- **D1** : >60%
- **D7** : >35%
- **D30** : >18%

### Monétisation
- **Conversion freemium→premium** : >5%
- **ARPU** : >0.25€/user/mois (avec 5% premium à 4.99€)

### Qualité
- **Crash-free rate** : >99%
- **Note App Store** : >4.5/5
- **NPS** : >40

---

## 🚨 Risques & Mitigation

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Retards développement | Moyenne | Élevé | Buffer 1 sem dans planning |
| Bugs critiques beta | Moyenne | Élevé | QA extensive Sprint 11 |
| Faible adoption | Moyenne | Critique | Marketing continu + feedback |
| Claims légaux | Faible | Critique | Disclaimer partout, avocat consulté |
| Concurrence soudaine | Faible | Moyen | Vitesse de lancement = avantage |
| Coûts API élevés | Faible | Moyen | Rate limiting + freemium |

---

## 📞 Contacts & Support

**Dev Lead :** Rémi Beaurain  
**Email :** [À compléter]  
**GitHub :** [À compléter]

**Resources :**
- [Expo Docs](https://docs.expo.dev)
- [Supabase Docs](https://supabase.com/docs)
- [Mixpanel Docs](https://docs.mixpanel.com)

---

**🌙 Prêt pour le lancement ? Let's build LUNA ! 🚀**

*Document créé le 9 novembre 2025*  
*Mise à jour continue pendant les sprints*

