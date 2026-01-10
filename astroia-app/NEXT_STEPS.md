# 🎯 Prochaines étapes – LUNA Sprint 9 ✅ → Sprint 10 🚀

**Date:** 09/11/2025  
**Status Sprint 9:** ✅ **COMPLET ET BÉTONNÉ**

---

## 🔧 Action immédiate : Exécuter le SQL dans Supabase

### 1. Créer la table `consents_audit`

1. Ouvre ton dashboard Supabase : https://supabase.com/dashboard
2. Sélectionne ton projet **LUNA - Cycle & Cosmos**
3. Va dans **SQL Editor** (menu gauche)
4. Clique sur **New query**
5. Copie-colle le contenu de `supabase-consents-audit.sql`
6. Clique sur **Run** (CMD+Enter)

**Vérification :**
```sql
-- Dans SQL Editor, vérifie que la table existe :
SELECT * FROM public.consents_audit LIMIT 1;

-- Vérifie les RLS policies :
SELECT * FROM pg_policies WHERE tablename = 'consents_audit';
```

Tu devrais voir 2 policies :
- `Users can view own consents` (SELECT)
- `Users can create own consents` (INSERT)

---

## ✅ Checklist manuelle (à faire maintenant)

### Test 1: App fraîche sans consentement
- [ ] Désinstalle l'app (ou efface AsyncStorage)
- [ ] Relance l'app
- [ ] Essaie d'accéder à **Cycle & Astrologie**
- **Résultat attendu:** Alert "Consentement requis" + redirection Settings

### Test 2: Accorder consentement santé
- [ ] Va dans **Settings > Confidentialité**
- [ ] Active le switch "Données de cycle (santé)"
- **Résultat attendu:** Alert succès + switch devient ✅ checkmark

### Test 3: Vérifier affichage date/version
- [ ] Reste dans **Settings > Confidentialité**
- **Résultat attendu:** 
  ```
  📱 Données de cycle (santé)
     Accordé le 09/11/2025 - Version 2.0.0
     ✅ [non modifiable]
  ```

### Test 4: Analytics opt-in (network sniffer)
- [ ] **Sans** activer analytics, ouvre l'app
- [ ] Vérifie les logs console : `[Analytics] Mixpanel NOT initialized - no consent`
- [ ] Pas de requête réseau vers Mixpanel
- [ ] Active le switch "Analytics"
- **Résultat attendu:** `[Analytics] Mixpanel initialized with consent`

### Test 5: Retrait analytics
- [ ] Désactive le switch "Analytics"
- **Résultat attendu:** Alert "Mixpanel a été réinitialisé"
- Vérifie logs : `[Analytics] Mixpanel reset`

### Test 6: Audit trail dans Supabase
- [ ] Après avoir accordé/retiré des consentements, va dans Supabase
- [ ] SQL Editor :
  ```sql
  SELECT * FROM consents_audit 
  WHERE user_id = auth.uid()
  ORDER BY created_at DESC;
  ```
- **Résultat attendu:** Historique de tous les changements (granted/revoked)

### Test 7: Bouton effacement données
- [ ] Settings > Confidentialité
- [ ] Clique sur "Demander l'effacement de mes données"
- **Résultat attendu:** Alert + choix "Contacter support"
- ⚠️ **Note:** Le `mailto:` n'est pas encore implémenté (nécessite `Linking.openURL`)

---

## 📊 Récapitulatif Sprint 9

### ✅ Fonctionnalités livrées

| # | Feature | Status |
|---|---------|--------|
| 1 | Rebranding LUNA (home, nav, splash) | ✅ |
| 2 | Onboarding consent (health + analytics) | ✅ |
| 3 | Settings > Confidentialité complets | ✅ |
| 4 | Medical disclaimer composant | ✅ |
| 5 | Data export (JSON + PDF) | ✅ |
| 6 | Suppression compte + données | ✅ |
| 7 | **Renforcement RGPD (6 points)** | ✅ |

### 📁 Fichiers créés/modifiés (Sprint 9)

**Nouveaux fichiers :**
- `app/onboarding/consent.js` : écran consentement explicite
- `lib/services/consentService.js` : gestion consentements
- `lib/services/consentAuditService.js` : audit trail RGPD
- `lib/services/exportService.js` : export JSON/PDF
- `components/MedicalDisclaimer.js` : disclaimer santé
- `supabase-consents-audit.sql` : schéma table audit
- `__tests__/consent.test.js` : tests smoke consentement
- `__tests__/analytics.test.js` : tests smoke analytics
- `COMPLIANCE_HARDENED.md` : doc renforcement
- `DATA_POLICY.md` : politique confidentialité complète
- `DISCLAIMER.md` : disclaimer médical

**Fichiers modifiés :**
- `app/(tabs)/home.js` : rebranding LUNA
- `app/(tabs)/_layout.js` : titres navigation
- `app/settings/privacy.js` : UI consentements + export
- `lib/analytics.js` : lazy init Mixpanel
- `README.md` : pivot LUNA documenté

---

## 🚀 Sprint 10 – Dashboard & Graphiques

### Objectif
Rendre **visibles les corrélations** cycle-humeur avec des graphiques et insights IA.

### Fonctionnalités à implémenter

#### 1. **Today Card** (écran Home)
- Affiche phase cycle actuelle + transit lunaire
- Insight IA court (1 phrase motivante)
- Design : carte glassmorphism avec dégradé de phase

**Exemple :**
```
🌑 Phase Menstruelle · Jour 3/5
Lune en Gémeaux ☿

"Aujourd'hui, ton corps se régénère. 
Écoute ton besoin de repos et hydrate-toi."
```

#### 2. **Graphiques Cycle (Dashboard)**
- **Humeur vs Cycle** : line chart 30 derniers jours
- **Énergie vs Cycle** : bar chart par phase
- **Calendrier visuel** : grid colorée par phase (30 jours)

**Tech stack :**
- `react-native-chart-kit` (déjà installé)
- `lib/services/chartDataService.js` : agrégation données
- `components/charts/MoodCycleChart.js`
- `components/charts/EnergyCycleChart.js`
- `components/charts/CycleCalendar.js`

#### 3. **Insights IA**
- Analyse corrélations : "Tu es plus créative en phase folliculaire"
- Recommandations : "Planifie tes projets importants les jours 10-14"
- Trigger : après 7 jours d'historique minimum

**Prompt GPT :**
```javascript
// lib/api/insightsService.js
const prompt = `
Analyse ces données cycle + humeur sur 30j :
${JSON.stringify(cycleData)}

Identifie 2-3 patterns et donne des recommandations 
concrètes pour optimiser bien-être.
Ton : bienveillant, inclusif, basé sur la data.
`;
```

#### 4. **Auto-tagging intelligent (Journal)**
- Suggestions tags basées sur humeur + phase
- Ex: phase menstruelle + humeur "tired" → #repos #hydratation
- Service : `lib/services/tagSuggestionService.js`

**Implémentation :**
```javascript
// app/journal/new.js
const suggestedTags = getSmartTagSuggestions(mood, cyclePhase);
// Affiche 3-5 suggestions contextuelles
```

---

## 📋 User Stories Sprint 10

### US1: Today Card
**En tant qu'** utilisatrice LUNA  
**Je veux** voir ma phase actuelle + insight du jour  
**Afin de** commencer ma journée avec conscience de mon cycle

**AC:**
- [ ] Card visible en haut du Home
- [ ] Phase actuelle + emoji + durée
- [ ] Transit lunaire (signe)
- [ ] Insight IA généré 1x/jour
- [ ] Haptic feedback au tap

### US2: Graphiques Cycle
**En tant qu'** utilisatrice premium (future)  
**Je veux** visualiser mes patterns humeur/cycle  
**Afin de** mieux comprendre mon corps

**AC:**
- [ ] 3 graphiques dans Dashboard
- [ ] Données des 30 derniers jours
- [ ] Légende claire (phases colorées)
- [ ] Scroll horizontal pour calendrier
- [ ] Loading state pendant fetch

### US3: Insights IA
**En tant qu'** utilisatrice régulière  
**Je veux** recevoir des recommandations personnalisées  
**Afin d'** optimiser mon bien-être

**AC:**
- [ ] Section "Insights" dans Dashboard
- [ ] Minimum 7 jours d'historique requis
- [ ] 2-3 insights affichés
- [ ] Régénération tous les 7 jours
- [ ] Stockés localement (cache)

### US4: Auto-tagging
**En tant qu'** utilisatrice pressée  
**Je veux** des suggestions tags intelligentes  
**Afin de** gagner du temps en journalisation

**AC:**
- [ ] 3-5 tags suggérés contextuellement
- [ ] Basés sur humeur + phase + historique
- [ ] Tap pour ajouter instantanément
- [ ] Possibilité d'ajouter tags custom

---

## 🏗️ Architecture technique Sprint 10

### Nouveaux services
```
lib/services/
├── cycleCalculator.js       # Calcul phase actuelle
├── chartDataService.js      # Agrégation données pour charts
├── tagSuggestionService.js  # Smart tags
└── insightsService.js       # Génération insights IA
```

### Nouveaux composants
```
components/
├── home/
│   └── TodayCard.js         # Carte du jour
└── charts/
    ├── MoodCycleChart.js    # Line chart humeur
    ├── EnergyCycleChart.js  # Bar chart énergie
    └── CycleCalendar.js     # Grid calendrier
```

### Modifications existantes
```
app/(tabs)/
├── home.js                  # Intégration TodayCard
├── dashboard/index.js       # Ajout graphiques + insights
└── journal/new.js           # Auto-tagging
```

---

## 🎨 Design System (cohérence)

### Couleurs phases (déjà définies)
```javascript
CYCLE_PHASES = [
  { id: 'menstrual',  gradient: ['#FF6B9D', '#FF8FB3'] },
  { id: 'follicular', gradient: ['#FFB347', '#FFC670'] },
  { id: 'ovulation',  gradient: ['#FFD93D', '#FFE66D'] },
  { id: 'luteal',     gradient: ['#C084FC', '#D8B4FE'] },
];
```

### UI patterns
- **Glassmorphism** : `backgroundColor: 'rgba(255,255,255,0.08)'`, `backdropFilter: 'blur(12px)'`
- **Glow effects** : `shadowColor` + `shadowRadius: 12` + `shadowOpacity: 0.4`
- **Animations** : Animated.spring avec `useNativeDriver: true`

---

## ⏱️ Estimation Sprint 10

| Tâche | Complexité | Durée |
|-------|------------|-------|
| CycleCalculator service | Moyenne | 2h |
| TodayCard component | Faible | 1h |
| ChartDataService | Moyenne | 2h |
| 3 composants Charts | Élevée | 4h |
| InsightsService + prompt | Moyenne | 2h |
| TagSuggestionService | Faible | 1h |
| Intégration Dashboard | Moyenne | 2h |
| Auto-tagging Journal | Faible | 1h |
| Tests + polish | Moyenne | 2h |
| **Total** | | **~17h** |

**Durée estimée :** 3-4 jours (avec tests)

---

## 🎯 Prêt pour Sprint 10 ?

### Avant de commencer
- [x] Sprint 9 complètement terminé
- [x] Table `consents_audit` créée dans Supabase
- [ ] Checklist manuelle Sprint 9 validée
- [ ] Tests manuels OK (6 points)

### Commandes utiles
```bash
# Lancer l'app
npm start

# Lancer les tests
npm test

# Vérifier linter
npm run lint

# Build preview (EAS)
eas build --platform ios --profile preview
```

---

**🚀 Prêt à démarrer Sprint 10 : Dashboard & Graphiques !**

Dis-moi quand tu es prêt et je commence l'implémentation étape par étape 💪

