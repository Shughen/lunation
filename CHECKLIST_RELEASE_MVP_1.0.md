# Checklist Release MVP 1.0 - Astroia Lunar

## ✅ Phase 1.6 - Stabilisation Completed

### États Limites & Robustesse
- [x] Cas aucun cycle lunaire → Message clair + CTA "Générer mes cycles" (index.tsx:459-479)
- [x] Skeleton loaders ajoutés (Home, Timeline, Report)
- [x] Gestion erreurs API propre sur tous les écrans
- [x] Deep links notifications configurés (index.tsx:239-246)

### UX Polish
- [x] Skeleton loaders cohérents (Skeleton.tsx)
- [x] Wording harmonisé app-wide:
  - "Mon cycle actuel" (home)
  - "Cycle en cours" (badges)
  - "Révolution lunaire" (subtitles)
- [x] Logger utility créé (utils/logger.ts)
- [x] Navigation back/forward vérifiée partout
- [x] TypeScript compilation clean (0 erreurs)

## 📋 Checklist Tests Release

### Tests Fonctionnels

#### ✅ Authentification
- [ ] Login avec email/password valides
- [ ] Login avec credentials invalides
- [ ] Logout fonctionnel
- [ ] Session persistée au redémarrage

#### ✅ Onboarding
- [ ] Welcome screen affiché au premier lancement
- [ ] Profile setup (nom + date de naissance)
- [ ] Consentement RGPD
- [ ] Disclaimer médical
- [ ] Slides onboarding complets
- [ ] Onboarding skipé si déjà complété

#### ✅ Révolutions Lunaires
- [ ] Génération des cycles depuis home
- [ ] Affichage cycle actuel sur home
- [ ] Rapport mensuel complet
- [ ] Timeline 12 mois fonctionnelle
- [ ] Navigation cycle → rapport via timeline
- [ ] Aspects majeurs cliquables (modal détail)

#### ✅ Void of Course
- [ ] Statut VoC en temps réel
- [ ] Liste fenêtres VoC à venir
- [ ] Refresh manuel fonctionnel

#### ✅ Notifications (Phase 1.4)
- [ ] Permission demandée au toggle (pas au démarrage)
- [ ] Notification début VoC schedulée
- [ ] Notification 30min avant fin VoC schedulée
- [ ] Notification début cycle lunaire schedulée
- [ ] Deep link: tap notif VoC → écran VoC
- [ ] Deep link: tap notif cycle → rapport mensuel
- [ ] Re-scheduling au focus (max 1x/24h)
- [ ] Désactivation notifications annule toutes les notifs

### Tests Permissions

#### iOS
- [ ] Permission notifications: accordée
- [ ] Permission notifications: refusée → message + lien Settings
- [ ] Ré-activation depuis Settings iOS → fonctionne
- [ ] Deep links app fermée / background / foreground

#### Android
- [ ] Permission notifications: accordée
- [ ] Permission notifications: refusée → message + lien Settings
- [ ] Ré-activation depuis Settings Android → fonctionne
- [ ] Deep links app fermée / background / foreground

### Tests États Limites

- [x] Aucun cycle généré → Message + CTA "Générer"
- [ ] API offline → Message erreur propre
- [ ] API lente → Skeleton loaders affichés
- [ ] Cycle non trouvé (ID invalide) → Message 404 propre
- [ ] Aucune fenêtre VoC à venir → Message informatif

### Tests Navigation

- [ ] Toutes les routes accessibles
- [ ] Back button fonctionnel partout
- [ ] Scroll fluide sur écrans longs (rapport, timeline)
- [ ] Pas de white screen / freeze
- [ ] Deep links depuis notifications fonctionnels

### Tests Performance

- [ ] Pas de lag au scroll
- [ ] Pas de lag au tap
- [ ] Cache daily climate fonctionnel (max 1 call/jour)
- [ ] Pas de memory leak visible

## 🐛 Bugs Connus (Limitations MVP)

### Acceptées pour MVP 1.0
1. **Daily Climate Fallback**: Si API `/daily-climate` échoue, fallback sur moonPosition seul (pas d'insight) → Acceptable MVP
2. **Notifications Re-scheduling**: Limité à 1x/24h au focus → Acceptable MVP, optimise batterie
3. **Timeline**: Affiche cycles futurs uniquement, pas d'historique → Scope MVP volontaire
4. **Offline Mode**: Pas de persistence complète offline → Hors scope MVP

### À Monitorer en Production
- Logs console en dev uniquement (vérifier build prod)
- Performance daily climate API (cache 24h actif)
- Taux erreur génération cycles lunaires

## 📦 Prochaines Étapes (Hors MVP 1.0)

### Phase 2 (Post-MVP)
- [ ] Persistence offline complète
- [ ] Historique cycles passés
- [ ] Notifications push serveur (vs local uniquement)
- [ ] Optimisation bundle size
- [ ] Tests E2E automatisés
- [ ] Monitoring erreurs prod (Sentry)

## ✅ Validation Finale

### Pré-Release
- [x] TypeScript compilation: 0 erreurs
- [x] Skele loaders: Home, Timeline, Report
- [x] Wording harmonisé
- [x] Navigation vérifiée
- [ ] Tests manuels iOS + Android
- [ ] Tests notifications complètes
- [ ] Tests permissions edge cases
- [ ] Aucun crash critique

### Release
- [ ] Tag git: `mvp-1.0`
- [ ] Build production iOS
- [ ] Build production Android
- [ ] TestFlight upload (iOS)
- [ ] Internal testing distribué (Android)

## 🎯 Critères de Succès MVP 1.0

1. ✅ **Stabilité**: Aucun crash sur parcours utilisateur nominal
2. ✅ **UX**: Skeleton loaders + messages d'erreur clairs
3. ✅ **Fonctionnel**: Toutes features Phase 1.1-1.5 opérationnelles
4. 🔄 **Notifications**: VoC + cycle lunaire fonctionnelles (à tester)
5. 🔄 **Cross-platform**: iOS + Android testés (à valider)

---

**Status**: Phase 1.6 code complete. Tests manuels requis avant tag `mvp-1.0`.
**Date**: 2024-12-31
**Version**: 1.0.0-rc1
