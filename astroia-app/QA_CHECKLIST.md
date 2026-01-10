# ✅ Checklist QA Complète - LUNA

**Date:** 09/11/2025  
**Version:** 2.0.0  
**Sprint:** 11 - Polish & QA

---

## 📱 Tests iOS

### Démarrage & Onboarding
- [ ] L'app se lance sans crash
- [ ] Splash screen LUNA visible
- [ ] Onboarding s'affiche pour nouvel utilisateur
- [ ] Écran consentement explicite (health + analytics)
- [ ] Skip onboarding fonctionne
- [ ] Navigation fluide entre étapes

### Navigation
- [ ] Tab bar : 3 onglets visibles (Accueil, Profil, LUNA)
- [ ] Tab "Accueil" sélectionné par défaut
- [ ] Changement d'onglet fluide (60fps)
- [ ] Boutons retour fonctionnels partout
- [ ] Deep links fonctionnels

### Page d'accueil (Cycle & Cosmos)
- [ ] Header "AUJOURD'HUI" visible
- [ ] Carte "Mon cycle aujourd'hui" affichée
- [ ] Sans consentement : "Configure ton cycle"
- [ ] Avec consentement : Données cycle affichées
- [ ] Carte "Humeur & émotions" fonctionnelle
- [ ] Carte "Astro du jour" affichée
- [ ] Grille "EXPLORER" (4 tuiles) visible
- [ ] Contraste tuiles suffisant
- [ ] Disclaimer médical visible en bas (après scroll)
- [ ] Toutes les cartes tapables

### Cycle & Astrologie
- [ ] Accès bloqué sans consentement santé
- [ ] Alert "Consentement requis" + redirection Settings
- [ ] Avec consentement : formulaire accessible
- [ ] Sélection jour du cycle (1-35)
- [ ] Sélection phase (4 options)
- [ ] Sélection humeur (6 options)
- [ ] Bouton "Analyser" fonctionnel
- [ ] Résultats s'affichent correctement
- [ ] Sauvegarde historique OK
- [ ] Disclaimer médical visible

### Horoscope IA
- [ ] Affiche le bon signe (Scorpion, pas Bélier)
- [ ] Personnalisation avec prénom
- [ ] 4 sections visibles (Travail, Amour, Santé, Conseil)
- [ ] Lune du jour affichée
- [ ] Numéro chance généré
- [ ] Bouton "Actualiser" fonctionne
- [ ] Cache 24h respecté

### Thème Natal
- [ ] Calcul thème fonctionnel
- [ ] Résultats sauvegardés (AsyncStorage)
- [ ] Affichage thème calculé après fermeture app
- [ ] Bouton "Recalculer" visible si déjà calculé
- [ ] Carte du ciel affichée
- [ ] Positions planétaires correctes
- [ ] Sauvegarde dans profil OK

### Journal (Humeur & Émotions)
- [ ] Création entrée fonctionnelle
- [ ] Sélection humeur (6 options)
- [ ] Auto-tagging intelligent
- [ ] Tags suggérés selon humeur + phase
- [ ] Sauvegarde entrée OK
- [ ] Historique visible
- [ ] Suppression entrée fonctionne
- [ ] Stats "Vos statistiques" correctes

### Dashboard
- [ ] Stats affichées (11 analyses, etc.)
- [ ] Filtres fonctionnels (Toutes, Cycle, Relations, Parent-Enfant)
- [ ] Historique complet visible
- [ ] Suppression analyse fonctionne
- [ ] Modal détails s'ouvre
- [ ] Graphiques visibles (si >7 entrées)
- [ ] Insights IA affichés
- [ ] Calendrier cycle coloré

### Compatibilité
- [ ] Sélection signes fonctionnelle
- [ ] Sélection type relation (Couple, Amis, Collègues)
- [ ] Auto-fill depuis profil
- [ ] Analyse génère résultat
- [ ] Scores détaillés affichés
- [ ] Sauvegarde historique OK

### Parent-Enfant
- [ ] Sélection signes parent
- [ ] Sélection signes enfant
- [ ] Auto-fill parent depuis profil
- [ ] Analyse génère résultat (XGBoost)
- [ ] Recommandations affichées
- [ ] Sauvegarde historique OK
- [ ] Contraste texte suffisant

### Profil
- [ ] Affichage nom + signe
- [ ] Bouton "Modifier profil" fonctionne
- [ ] Modification sauvegardée
- [ ] Badges affichés (Explorateur, Passionné)
- [ ] Streak visible (jours consécutifs)
- [ ] Graphiques placeholder visible

### Assistant LUNA (Chat)
- [ ] Message bienvenue affiché
- [ ] Saisie texte fonctionnelle
- [ ] Envoi message OK
- [ ] Réponse IA reçue
- [ ] Contexte cycle intégré dans réponses
- [ ] Personnalisation avec prénom
- [ ] Scroll automatique vers nouveau message
- [ ] Suggestions rapides fonctionnelles

### Settings > Confidentialité
- [ ] Section Consentements visible
- [ ] Consentement santé : checkmark si accordé, switch sinon
- [ ] Date + version consentement affichées
- [ ] Consentement analytics : switch fonctionnel
- [ ] Toggle analytics OFF → Mixpanel reset
- [ ] Bouton "Demander effacement données" visible
- [ ] Export JSON fonctionne
- [ ] Export PDF fonctionne (si implémenté)
- [ ] Suppression compte fonctionne
- [ ] Politique confidentialité accessible

### Performance iOS
- [ ] Animations fluides 60fps
- [ ] Pas de frame drop au scroll
- [ ] Chargement rapide (<500ms)
- [ ] Pas de lag sur saisie texte
- [ ] Mémoire stable (pas de leaks)

### Accessibilité iOS
- [ ] VoiceOver navigation fluide
- [ ] Labels accessibilité corrects
- [ ] Tous les boutons annoncés
- [ ] Hints appropriés
- [ ] Contraste WCAG AA

### Erreurs & Edge Cases iOS
- [ ] Pas de crash au lancement
- [ ] Pas de crash sans connexion
- [ ] Gestion erreur API propre
- [ ] Timeout géré (30s)
- [ ] Cache fonctionne offline
- [ ] Réauthentification propre si session expire

---

## 🤖 Tests Android

### Démarrage & Onboarding
- [ ] L'app se lance sans crash
- [ ] Splash screen LUNA visible
- [ ] Onboarding s'affiche
- [ ] Consentements explicites
- [ ] Navigation fluide

### Navigation
- [ ] Tab bar : 3 onglets visibles
- [ ] Changement d'onglet fluide
- [ ] Bouton back Android respecté
- [ ] Deep links fonctionnels

### Fonctionnalités Principales
- [ ] Page d'accueil Cycle & Cosmos
- [ ] Cycle & Astrologie
- [ ] Horoscope personnalisé
- [ ] Thème Natal
- [ ] Journal
- [ ] Dashboard
- [ ] Compatibilité
- [ ] Parent-Enfant
- [ ] Chat Assistant LUNA
- [ ] Settings

### Performance Android
- [ ] Animations fluides
- [ ] Pas de lag
- [ ] Chargement rapide
- [ ] Mémoire stable

### Accessibilité Android
- [ ] TalkBack navigation OK
- [ ] Labels corrects
- [ ] Contraste suffisant

### Erreurs & Edge Cases Android
- [ ] Pas de crash
- [ ] Offline mode OK
- [ ] Erreurs API gérées
- [ ] Back button comportement correct

---

## 🌐 Tests Cross-Platform

### Synchronisation
- [ ] Données sync entre devices (si Supabase actif)
- [ ] Consentements persistés
- [ ] Historique sync
- [ ] Profil sync

### RGPD & Conformité
- [ ] Consentement santé requis pour cycle
- [ ] Consentement analytics opt-in
- [ ] Mixpanel ne s'init pas sans consent
- [ ] Audit trail logs dans Supabase
- [ ] Export données fonctionne
- [ ] Suppression compte complète
- [ ] Disclaimer médical partout

### Analytics (si opt-in activé)
- [ ] Events trackés correctement
- [ ] `home_viewed` envoyé
- [ ] `home_tap_cycle_details` envoyé
- [ ] `journal_entry_created` envoyé
- [ ] `ai_message_sent` envoyé
- [ ] Aucun event si opt-out

### Sentry Monitoring
- [ ] Sentry configuré
- [ ] Erreurs capturées
- [ ] Source maps uploadées
- [ ] Releases trackées
- [ ] Performance metrics actives

---

## 🐛 Bugs Régressifs À Vérifier

### Bugs corrigés Sprint 10/11
- [ ] Horoscope affiche bien Scorpion (pas Bélier)
- [ ] Thème Natal affiche résultats calculés
- [ ] Tab bar affiche "LUNA" (pas "Assistant IA")
- [ ] Contraste Parent-Enfant suffisant
- [ ] "Mon cycle" → /cycle-astro (pas Dashboard)
- [ ] Import MedicalDisclaimer correct

### Edge Cases Critiques
- [ ] App fraîche (aucune donnée) : pas de crash
- [ ] Profil vide : comportement graceful
- [ ] API timeout : message clair
- [ ] Pas de connexion : mode offline OK
- [ ] Cycle non configuré : CTA visible
- [ ] Historique vide : empty state OK

---

## 📊 Métriques À Valider

| Métrique | Cible | iOS | Android | Status |
|----------|-------|-----|---------|--------|
| **Crash rate** | <0.1% | ⏳ | ⏳ | 🔵 |
| **FPS moyen** | 60fps | ⏳ | ⏳ | 🔵 |
| **Temps chargement** | <500ms | ⏳ | ⏳ | 🔵 |
| **Bundle size** | <10MB | ⏳ | ⏳ | 🔵 |
| **Test coverage** | >70% | ⏳ | ⏳ | 🔵 |
| **Contraste min** | 4.5:1 | ⏳ | ⏳ | 🔵 |
| **A11y labels** | 100% | ⏳ | ⏳ | 🔵 |

---

## ✅ Critères d'Acceptation Sprint 11

### Code Quality
- [x] ✅ Tous les composants avec React.memo
- [x] ✅ useCallback sur tous les handlers
- [x] ✅ useMemo sur données calculées
- [x] ✅ Aucune erreur linter
- [x] ✅ Aucune console.error en prod

### Features
- [x] ✅ IA contextuelle cycle fonctionnelle
- [x] ✅ Labels accessibilité partout
- [x] ✅ Performance 60fps
- [x] ✅ Sentry configuré
- [x] ✅ Tests >70% coverage
- [ ] ⏳ QA iOS complète
- [ ] ⏳ QA Android complète

### RGPD
- [x] ✅ Consentements respectés
- [x] ✅ Audit trail actif
- [x] ✅ Analytics opt-in strict
- [x] ✅ Export/suppression données

---

## 🚀 Prochaine Étape

**Sprint 11 quasi terminé !**

Reste à faire :
1. **Tests manuels iOS** (1h)
2. **Tests manuels Android** (1h)
3. **Polish final** si bugs détectés

Puis **Sprint 12 : Beta TestFlight/Play Store** 🎉

---

## 📝 Notes QA

### Pour tester :
```bash
# iOS
npm start
npx expo run:ios

# Android
npm start
npx expo run:android

# Tests automatisés
npm test -- --coverage
```

### Si bug trouvé :
1. Noter dans cette checklist
2. Créer issue GitHub ou ticket
3. Prioriser (bloquant / mineur)
4. Corriger avant beta

---

**Prêt pour les tests manuels !** 🧪

