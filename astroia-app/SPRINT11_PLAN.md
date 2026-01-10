# 🔧 Sprint 11 - Polish & QA

**Date début:** 09/11/2025  
**Durée estimée:** 1-2 semaines  
**Objectif:** Perfectionner l'app LUNA pour la beta publique

---

## 🎯 Objectifs Sprint 11

### **Phase 1 : IA Spécialisée Cycle** 🤖
- Enrichir les prompts IA avec contexte de phase du cycle
- Adapter les recommandations selon la phase menstruelle
- Améliorer la pertinence des insights

### **Phase 2 : Accessibilité (A11y)** ♿
- Contraste WCAG AA (4.5:1 minimum)
- Labels accessibles pour VoiceOver/TalkBack
- Navigation clavier
- Tailles de touche ≥44px

### **Phase 3 : Performance** ⚡
- Optimisations 60fps garantis
- Lazy loading des images
- Memoization des composants
- Réduction bundle size

### **Phase 4 : Monitoring** 📊
- Sentry setup (error tracking)
- Analytics dashboard
- Performance monitoring
- Crash reports

### **Phase 5 : Tests** 🧪
- Jest coverage >70%
- Tests E2E critiques
- Tests accessibilité
- Tests performance

### **Phase 6 : QA Exhaustif** ✅
- Tests manuels iOS
- Tests manuels Android
- Edge cases
- Régression testing

---

## 📋 User Stories Sprint 11

### US1: IA Contextuelle Phase Cycle
**En tant qu'** utilisatrice LUNA  
**Je veux** que l'IA adapte ses recommandations selon ma phase actuelle  
**Afin d'** avoir des conseils vraiment pertinents pour mon cycle

**Acceptance Criteria:**
- [ ] Assistant IA connaît la phase actuelle (menstruelle, folliculaire, ovulation, lutéale)
- [ ] Recommandations adaptées (ex: repos en phase menstruelle, énergie en ovulation)
- [ ] Insights dashboard mentionnent explicitement la phase
- [ ] Horoscope IA intègre le contexte cycle si disponible

---

### US2: App Accessible WCAG AA
**En tant qu'** utilisatrice avec handicap visuel  
**Je veux** pouvoir utiliser LUNA avec VoiceOver  
**Afin d'** accéder aux fonctionnalités comme tout le monde

**Acceptance Criteria:**
- [ ] Tous les boutons ont des labels accessibles
- [ ] Contraste minimum 4.5:1 partout
- [ ] Navigation VoiceOver fluide
- [ ] Textes alternatifs pour icônes
- [ ] Focus visible au clavier

---

### US3: App Fluide 60fps
**En tant qu'** utilisatrice  
**Je veux** une app qui ne lag jamais  
**Afin d'** avoir une expérience premium

**Acceptance Criteria:**
- [ ] Toutes les animations à 60fps constant
- [ ] Pas de frame drop au scroll
- [ ] Chargement rapide des écrans (<500ms)
- [ ] Images optimisées
- [ ] Bundle size <10MB

---

### US4: Monitoring Proactif
**En tant que** développeur  
**Je veux** être alerté des erreurs avant les users  
**Afin de** corriger proactivement

**Acceptance Criteria:**
- [ ] Sentry configuré et actif
- [ ] Alertes email sur crashes
- [ ] Source maps uploadées
- [ ] Release tracking
- [ ] Performance monitoring

---

### US5: Tests Robustes
**En tant que** développeur  
**Je veux** une couverture de tests >70%  
**Afin d'** éviter les régressions

**Acceptance Criteria:**
- [ ] Tests unitaires services critiques
- [ ] Tests composants principaux
- [ ] Tests E2E flow principal
- [ ] Coverage report automatique
- [ ] CI/CD intégré

---

### US6: QA Complet
**En tant que** QA  
**Je veux** tester tous les scénarios  
**Afin de** garantir zéro bug critique

**Acceptance Criteria:**
- [ ] Checklist QA complète (iOS + Android)
- [ ] Tous les edge cases testés
- [ ] Pas de bug bloquant
- [ ] Pas de crash
- [ ] Performance validée

---

## 🏗️ Architecture Technique Sprint 11

### 1. IA Contextuelle Cycle

**Nouveau service : `lib/services/contextService.js`**
```javascript
export async function getAIContext() {
  const cycleData = await getCycleData();
  const profile = await getProfile();
  
  return {
    phase: cycleData.currentPhase,
    dayOfCycle: cycleData.dayOfCycle,
    energy: cycleData.energyLevel,
    mood: await getLatestMood(),
    profile: {
      name: profile.name,
      sunSign: profile.sunSign,
      moonSign: profile.moonSign,
    }
  };
}
```

**Modification : `lib/analytics.js`**
- Enrichir tous les prompts avec `getAIContext()`

---

### 2. Accessibilité

**Fichier : `constants/accessibility.js`**
```javascript
export const A11Y_LABELS = {
  home: {
    cycleCard: "Voir les détails de mon cycle actuel",
    moodCard: "Ouvrir le journal d'humeur",
    astroCard: "Voir l'analyse astrologique du jour",
  },
  // ...
};
```

**Modifications :**
- Tous les `Pressable` → `accessibilityLabel`
- Tous les `TouchableOpacity` → `accessibilityRole`
- Contraste vérifié avec `polished` lib

---

### 3. Performance

**Optimisations :**
```javascript
// React.memo sur tous les composants lourds
export default React.memo(CycleCard);

// useMemo pour calculs coûteux
const chartData = useMemo(() => 
  processChartData(rawData), 
  [rawData]
);

// useCallback pour fonctions passées en props
const handlePress = useCallback(() => {
  router.push('/cycle-astro');
}, [router]);
```

**Images :**
- Lazy loading avec `react-native-fast-image`
- Compression WebP
- Sizes adaptatives

---

### 4. Monitoring Sentry

**Setup :**
```bash
npm install @sentry/react-native
npx @sentry/wizard -i reactNative -p ios android
```

**Config : `sentry.config.js`**
```javascript
import * as Sentry from "@sentry/react-native";

Sentry.init({
  dsn: "YOUR_DSN",
  tracesSampleRate: 1.0,
  environment: __DEV__ ? 'development' : 'production',
});
```

---

### 5. Tests Jest

**Config : `jest.config.js`**
```javascript
module.exports = {
  preset: 'jest-expo',
  coverageThreshold: {
    global: {
      statements: 70,
      branches: 70,
      functions: 70,
      lines: 70,
    },
  },
};
```

**Tests prioritaires :**
- `__tests__/services/cycleCalculator.test.js`
- `__tests__/services/chartDataService.test.js`
- `__tests__/components/home/CycleCard.test.js`
- `__tests__/integration/cycle-flow.test.js`

---

## ⏱️ Estimation Sprint 11

| Tâche | Complexité | Durée |
|-------|------------|-------|
| IA contextuelle cycle | Moyenne | 3h |
| Accessibilité labels | Faible | 2h |
| Accessibilité contraste | Moyenne | 2h |
| Performance memoization | Moyenne | 3h |
| Performance images | Faible | 1h |
| Sentry setup | Faible | 1h |
| Tests services | Élevée | 4h |
| Tests composants | Moyenne | 3h |
| Tests E2E | Élevée | 3h |
| QA iOS | Moyenne | 3h |
| QA Android | Moyenne | 3h |
| Polish UI bugs | Faible | 2h |
| **Total** | | **~30h** |

**Durée estimée :** 1-2 semaines (avec tests exhaustifs)

---

## 🚀 Plan d'Exécution

### **Jour 1-2 : IA Contextuelle** 🤖
1. Créer `contextService.js`
2. Enrichir prompts Assistant IA
3. Enrichir prompts Insights
4. Tester pertinence

### **Jour 3-4 : Accessibilité** ♿
1. Audit contraste complet
2. Ajout labels accessibilité
3. Tests VoiceOver iOS
4. Tests TalkBack Android

### **Jour 5-6 : Performance** ⚡
1. Profiling React DevTools
2. Memoization composants
3. Lazy loading images
4. Tests 60fps

### **Jour 7 : Monitoring** 📊
1. Setup Sentry
2. Test crash reporting
3. Performance metrics

### **Jour 8-10 : Tests** 🧪
1. Tests unitaires services
2. Tests composants
3. Tests E2E
4. Coverage >70%

### **Jour 11-12 : QA** ✅
1. Checklist QA iOS
2. Checklist QA Android
3. Edge cases
4. Polish final

---

## ✅ Definition of Done - Sprint 11

### IA Contextuelle
- [ ] Assistant IA adapte ses réponses selon phase cycle
- [ ] Insights mentionnent la phase actuelle
- [ ] Recommandations pertinentes par phase

### Accessibilité
- [ ] Contraste WCAG AA partout
- [ ] Labels accessibilité sur tous les boutons
- [ ] VoiceOver navigation fluide
- [ ] Tailles touch ≥44px

### Performance
- [ ] 60fps constant vérifié
- [ ] Images optimisées
- [ ] Bundle <10MB
- [ ] Temps chargement <500ms

### Monitoring
- [ ] Sentry configuré
- [ ] Alertes actives
- [ ] Source maps uploadées
- [ ] Releases trackées

### Tests
- [ ] Coverage >70%
- [ ] Tests services critiques
- [ ] Tests E2E flow principal
- [ ] Aucun test failing

### QA
- [ ] Checklist iOS complète
- [ ] Checklist Android complète
- [ ] Zéro bug bloquant
- [ ] Zéro crash

---

## 📊 Métriques Cibles

| Métrique | Cible | Actuel | Status |
|----------|-------|--------|--------|
| Contraste minimum | 4.5:1 | TBD | 🔵 |
| FPS moyen | 60 | TBD | 🔵 |
| Temps chargement | <500ms | TBD | 🔵 |
| Bundle size | <10MB | TBD | 🔵 |
| Test coverage | >70% | ~5% | 🔵 |
| Crash rate | <0.1% | TBD | 🔵 |

---

## 🎯 Livrable Final Sprint 11

**App LUNA prête pour beta publique :**
- ✅ IA ultra pertinente
- ✅ Accessible WCAG AA
- ✅ Fluide 60fps
- ✅ Monitorée (Sentry)
- ✅ Testée >70%
- ✅ QA complète iOS/Android

**Prêt pour Sprint 12 : Beta TestFlight/Play Store !** 🚀

---

## 🚀 C'est parti !

**Première tâche : IA Contextuelle Cycle**

Je commence maintenant l'implémentation ! 💪

