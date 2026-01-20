# Rapport MVP Lunation - Bugs & Effet Whahou

## Score actuel: 8.7/10 → Objectif: 10/10

---

## PARTIE 1: BUGS MINEURS À CORRIGER (Bloquants pour stores)

### Bug #1: Bouton "← Retour" non réactif
- **Localisation**: Header de tous les écrans (Rapport Mensuel, Thème Natal, VoC, Journal)
- **Symptôme**: Le tap sur "← Retour" ne déclenche pas de navigation
- **Workaround actuel**: Le bouton BACK Android fonctionne
- **Impact UX**: Frustration utilisateur, surtout sur iOS où pas de bouton hardware
- **Priorité**: HAUTE
- **Fix suggéré**: Vérifier que le `TouchableOpacity` ou `Pressable` englobe bien tout le texte avec un `hitSlop` suffisant

### Bug #2: Bouton X de la modal d'interprétation
- **Localisation**: Modal d'interprétation planétaire (Thème Natal)
- **Symptôme**: Le X en haut à droite ne répond pas au tap
- **Workaround**: Bouton BACK Android ou bouton "Fermer" en bas
- **Priorité**: MOYENNE
- **Fix suggéré**: Augmenter la zone de tap du X, vérifier le z-index

### Bug #3: Section DEV QA Tools visible
- **Localisation**: Écran Réglages (en bas)
- **Symptôme**: Section de debug visible en mode non-dev
- **Impact**: Non professionnel pour les stores, confusion utilisateur
- **Priorité**: HAUTE (bloquant stores)
- **Fix suggéré**: Conditionner l'affichage avec `__DEV__` ou une variable d'environnement

### Bug #4: Footer technique visible
- **Localisation**: Rapport Mensuel (en bas)
- **Contenu**: "Rapport généré par templates v4 (architecture déterministe)"
- **Impact**: Casse l'immersion, non professionnel
- **Priorité**: MOYENNE
- **Fix suggéré**: Masquer en prod ou reformuler en "Généré spécialement pour toi"

### Bug #5: Onboarding bypassed en mode DEV
- **Localisation**: Flow de première connexion
- **Symptôme**: Les étapes Profile Setup, Consent RGPD, Disclaimer, Slides sont sautées
- **Impact**: Impossible de tester le vrai flow utilisateur
- **Priorité**: HAUTE (critique pour stores)
- **À vérifier**: Le flag DEV_AUTH_BYPASS et son comportement en build release

---

## PARTIE 2: VÉRIFICATIONS À FAIRE

### Check #1: Transits du mois
- **État actuel**: Affiche "Aucun transit majeur ce mois-ci"
- **Question**: Est-ce un vrai empty state ou un bug API/calcul?
- **Action**: Vérifier les logs API et les données de transits

### Check #2: Notifications push
- **État actuel**: Toggle présent, boutons QA pour tester
- **Question**: Fonctionnent-elles en conditions réelles?
- **Action**: Tester sur device physique avec l'app en background

### Check #3: Comportement offline
- **Question**: Que se passe-t-il sans connexion?
- **Action**: Couper le réseau et tester chaque écran

---

## PARTIE 3: EFFET WHAHOU - Ce qui manque pour 10/10

### Whahou #1: Wheel Chart du Thème Natal (Impact: +0.5)
- **Actuel**: Liste textuelle des positions planétaires
- **Attendu**: Graphique circulaire avec les 12 maisons et les planètes positionnées
- **Librairies suggérées**:
  - `react-native-svg` pour dessiner le cercle
  - `d3-shape` pour les calculs de positionnement
- **Complexité**: MOYENNE (3-5 jours)
- **Valeur perçue**: TRÈS HAUTE - C'est l'élément visuel signature de toute app astro

### Whahou #2: Animations de transition (Impact: +0.3)
- **Actuel**: Transitions instantanées entre écrans
- **Attendu**:
  - Fade-in des cards au scroll
  - Slide-in des modals
  - Animation de la lune au chargement
- **Librairies suggérées**:
  - `react-native-reanimated` (déjà installé?)
  - `moti` pour des animations déclaratives
- **Complexité**: FAIBLE (1-2 jours)
- **Valeur perçue**: HAUTE - Donne une impression de polish premium

### Whahou #3: Haptics & Sons subtils (Impact: +0.2)
- **Actuel**: Aucun feedback sensoriel
- **Attendu**:
  - Vibration légère au tap sur les planètes
  - Son doux à l'ouverture de l'app (optionnel)
  - Haptic feedback sur les actions importantes
- **Librairie**: `expo-haptics`
- **Complexité**: TRÈS FAIBLE (quelques heures)
- **Valeur perçue**: MOYENNE - Renforce la sensation premium

### Whahou #4: Notifications push intelligentes (Impact: +0.3)
- **Actuel**: Structure en place mais pas exploitée
- **Attendu**:
  - "La Lune entre en Bélier dans 2h - prépare-toi!"
  - "Nouvelle Lune ce soir - moment idéal pour tes intentions"
  - "Pause lunaire (VoC) commence dans 30min"
- **Complexité**: MOYENNE (2-3 jours)
- **Valeur perçue**: TRÈS HAUTE - Engagement quotidien

### Whahou #5: Illustrations personnalisées (Impact: +0.2)
- **Actuel**: Emojis zodiacaux
- **Attendu**: Icônes/illustrations custom pour chaque signe et planète
- **Complexité**: Dépend des assets (design externe)
- **Valeur perçue**: HAUTE - Identité visuelle unique

---

## PARTIE 4: ROADMAP SUGGÉRÉE

### Sprint 1 - Corrections critiques (1-2 jours)
1. [ ] Fixer bouton "← Retour"
2. [ ] Masquer DEV QA Tools en prod
3. [ ] Masquer footer technique du rapport
4. [ ] Vérifier onboarding complet

### Sprint 2 - Polish UX (2-3 jours)
5. [ ] Fixer bouton X de la modal
6. [ ] Vérifier transits du mois
7. [ ] Tester notifications réelles
8. [ ] Tester mode offline

### Sprint 3 - Effet Whahou (5-7 jours)
9. [ ] Wheel Chart du thème natal
10. [ ] Animations de transition
11. [ ] Haptics feedback
12. [ ] Notifications push intelligentes

---

## PARTIE 5: CHECKLIST PRÉ-STORES

### App Store (iOS)
- [ ] Build release sans DEV_AUTH_BYPASS
- [ ] Onboarding complet testé
- [ ] Privacy Policy URL configurée
- [ ] Screenshots des écrans principaux
- [ ] Icône app et splash screen OK
- [ ] Age rating: 4+

### Google Play
- [ ] Build release APK/AAB
- [ ] Target API level ≥ 33
- [ ] Privacy Policy URL
- [ ] Screenshots
- [ ] Content rating questionnaire

---

## Score détaillé

| Critère | Actuel | Après bugs fix | Après Whahou |
|---------|--------|----------------|--------------|
| Complétude MVP | 9/10 | 9.5/10 | 10/10 |
| Design/UX | 8.5/10 | 9/10 | 10/10 |
| Qualité contenu | 9.5/10 | 9.5/10 | 10/10 |
| Stabilité | 8/10 | 9/10 | 9.5/10 |
| Publiabilité | 8.5/10 | 9.5/10 | 10/10 |
| **TOTAL** | **8.7/10** | **9.3/10** | **9.9/10** |
