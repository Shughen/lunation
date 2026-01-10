# 📊 CYCLE TRACKING V2.0 - Documentation

**Date :** 10 novembre 2025  
**Version :** v2.0 (Sprint 16)  
**Inspiration :** Mon Calendrier (iOS)  
**Status :** ✅ Implémenté

---

## 🎯 **OBJECTIF**

Système de suivi de cycles personnalisé, offline-first, simple et fiable.

**Features core :**
- Log rapide début/fin des règles (1 tap)
- Historique multi-cycles
- Moyennes calculées automatiquement
- Prédiction prochaines règles
- Migration douce depuis settings/cycle.js

---

## 📦 **ARCHITECTURE**

### **Store : `cycleHistoryStore.ts`**

```typescript
interface CycleEntry {
  id: string;
  startDate: string; // ISO UTC
  endDate: string | null; // null si en cours
  cycleLength: number | null; // Durée totale cycle
  periodLength: number | null; // Durée règles
  createdAt: string;
  updatedAt: string;
}
```

**API :**
- `loadCycles()` → Charge depuis AsyncStorage
- `startPeriod(date?)` → Log début règles
- `endPeriod(date?)` → Log fin règles
- `getAverages()` → Calcule moyennes (≥2 cycles)
- `predictNextPeriod()` → Prédiction basée sur moyenne
- `getCurrentCycle()` → Cycle en cours (sans endDate)
- `migrateFromSettings()` → Migration initiale

---

## 🔄 **MIGRATION AUTOMATIQUE**

**Fichier :** `lib/services/cycleMigration.ts`

**Déclencheur :** Au premier lancement après MAJ (app/_layout.js)

**Logique :**
1. Vérifier si déjà migré (`@luna_cycle_migrated`)
2. Lire `cycle_config` (lastPeriodDate, cycleLength)
3. Créer une entrée initiale :
   - `startDate` = lastPeriodDate
   - `endDate` = startDate + 5 jours (estimation)
   - `periodLength` = 5
   - `cycleLength` = cycleLength (config)
4. Sauvegarder dans `@luna_cycle_history`
5. Marquer migration complétée

**Edge cases :**
- Pas de config → Skip migration, marquer complété
- Déjà migré → Skip
- Erreur → Log error, ne pas bloquer l'app

---

## 🩸 **QUICK PERIOD LOG**

**Composant :** `components/QuickPeriodLog.tsx`

**Comportement :**
- **Aucun cycle en cours** → Bouton rose "🩸 Début des règles"
- **Cycle en cours** → Bouton bleu "🔵 Fin des règles"
- Toast après action (Android) ou Alert (iOS)
- Haptics : medium (tap), success (ok), error (fail)

**Idempotence :**
- Impossible de démarrer 2 cycles simultanément
- Impossible de terminer si aucun cycle en cours
- Guards dans le store

**Analytics :**
- `cycle_start_logged` (totalCycles)
- `cycle_end_logged` (periodLength, totalCycles)

---

## 📊 **CYCLE STATS**

**Composant :** `components/CycleStats.tsx`

**Affichage :**
- Titre "📊 Mes cycles"
- Sous-titre "X cycles saisis"
- Deux cartes :
  - Rose : "X Jours - Règles moyennes" (🩸)
  - Jaune : "X Jours - Cycle moyen" (🔄)

**Condition :** Visible uniquement si `getAverages()` renvoie une valeur (≥2 cycles complets)

**Calcul moyennes :**
```typescript
avgPeriod = Σ(periodLength) / count(cycles complets)
avgCycle = Σ(cycleLength) / count(cycles avec cycleLength)
```

**Analytics :**
- `cycle_stats_visible` (avgPeriod, avgCycle, totalCycles)

---

## ⏱️ **CYCLE COUNTDOWN**

**Composant :** `components/CycleCountdown.tsx`

**Affichage :**
- Grand nombre "X" (jours restants)
- Label "JOURS RESTANTS"
- Texte "d MMM - Règles suivantes"

**Condition :** Visible uniquement si prédiction disponible

**Calcul prédiction :**
```typescript
lastStart = cycles[dernierCycle].startDate
nextDate = lastStart + avgCycle
daysUntil = ceil((nextDate - today) / 86400000)
```

**Analytics :**
- `cycle_prediction_shown` (daysUntil, hasAverages)

---

## 📊 **CYCLE HISTORY BAR**

**Composant :** `components/CycleHistoryBar.tsx`

**Affichage :**
- Dates "d MMM - d MMM"
- Barre horizontale :
  - **Rose** : Segment règles (periodLength)
  - **Jaune** : Reste du cycle
  - **Icône 🥚** : Ovulation (≈ cycle - 14 jours)
- Durée totale à droite

**Calcul positions :**
```typescript
periodPercentage = (periodLength / cycleLength) * 100
ovulationDay = cycleLength - 14
ovulationPercentage = (ovulationDay / cycleLength) * 100
```

---

## 📱 **ÉCRAN "MES CYCLES"**

**Route :** `app/my-cycles/index.tsx`

**Structure :**
1. Header (titre + bouton retour)
2. CycleStats (moyennes)
3. Historique (liste de CycleHistoryBar)
4. Info card (explication moyennes)

**Empty state :**
- Icône calendrier
- Titre "Aucun cycle enregistré"
- Subtitle "Commence à logger..."
- CTA "Retour à l'accueil"

**Ordre affichage :** Plus récent en premier (`.reverse()`)

---

## 🏠 **INTÉGRATION HOME**

**Modifications :** `app/(tabs)/home.tsx`

**Ajouts :**
1. Import QuickPeriodLog + CycleCountdown
2. Ajout après CycleCard :
   ```tsx
   <QuickPeriodLog />
   <CycleCountdown />
   ```
3. Route "Mes cycles" dans ExploreGrid

**ExploreGrid :** Nouvelle tuile avec icône calendrier

---

## 🔐 **EDGE CASES & SÉCURITÉ**

### **1. Deux cycles actifs (Double-tap)**
**Problème :** User tape 2x "Début" rapidement  
**Solution :** 
- Lock `isSaving` state dans QuickPeriodLog
- Early return si `isSaving === true`
- Guard dans `startPeriod()` vérifie `getCurrentCycle()`
- Toast "⚠️ Un cycle est en cours, termine-le d'abord"
**Résultat :** 1er tap lock le bouton, 2ème tap ignoré

### **2. Dates futures**
**Problème :** User sélectionne date future  
**Solution :** Guard `if (date > new Date()) return false`  
**Résultat :** Toast "❌ Impossible de logger dans le futur"

### **3. Dates incohérentes**
**Problème :** endDate ≤ startDate  
**Solution :** Guard `if (endDate <= startDate) return false`  
**Résultat :** Toast "❌ Date de fin doit être après date de début"

### **4. Migration multiple**
**Problème :** App redémarre plusieurs fois  
**Solution :** Clé `@luna_cycle_migrated` bloque la migration  
**Résultat :** Migration exécutée 1 seule fois

### **5. Migration sans config**
**Problème :** Nouveau user, pas de `cycle_config`  
**Solution :** Skip migration + `trackEvents.cycleMigrationSkipped('no_config')`  
**Résultat :** Empty state propre, pas d'entrée bidon

### **6. Calculs moyennes**
**Problème :** 1 seul cycle → division par 0  
**Solution :** `if (completeCycles.length < 2) return null`  
**Résultat :** Stats/countdown cachés si données insuffisantes

### **7. Cycle ouvert dans moyennes**
**Problème :** Cycle en cours (sans endDate) fausse les calculs  
**Solution :** Filter `c => c.endDate && c.periodLength`  
**Résultat :** Uniquement cycles complets dans moyennes

### **8. Timezones**
**Problème :** User voyage → dates décalées  
**Solution :** Stockage ISO UTC, affichage locale  
**Résultat :** Dates cohérentes quel que soit le fuseau

---

## 📈 **ANALYTICS**

### **Events :**

| Event | Payload | Trigger |
|-------|---------|---------|
| `cycle_start_logged` | `totalCycles` | Tap "Début des règles" (succès) |
| `cycle_end_logged` | `periodLength, totalCycles` | Tap "Fin des règles" (succès) |
| `cycle_prediction_shown` | `daysUntil, hasAverages` | Affichage CycleCountdown |
| `cycle_stats_visible` | `avgPeriod, avgCycle, totalCycles` | Affichage CycleStats |
| `cycle_migration_skipped` | `reason` ('no_config' \| 'invalid_data') | Migration skip |
| `cycle_button_disabled_ms` | `duration_ms` | Lock duration > 100ms (monitoring UX) |

**Pas de PII :** Aucune date, aucune donnée personnelle identifiable

---

## 🧪 **CRITÈRES D'ACCEPTATION**

### ✅ **Fonctionnels :**
- [x] On peut démarrer un cycle en 1 tap (Home)
- [x] On peut terminer le cycle en 1 tap (Home)
- [x] "Mes cycles" affiche ≥1 ligne après migration
- [x] Moyennes apparaissent après ≥2 cycles complets
- [x] Countdown s'affiche si moyenne existe, sinon caché
- [x] Aucune erreur si tap 2x sur "Début" ou "Fin" (lock + toast warning)
- [x] Tout fonctionne offline (AsyncStorage)

### ✅ **UX :**
- [x] Toast confirmations clairs (✅ / ⚠️ / ❌)
- [x] Haptics appropriés (medium tap, success ok, warning guard, error fail)
- [x] Loading states visibles (ActivityIndicator + opacity 0.5)
- [x] Empty state engageant ("Aucun cycle complet...")
- [x] Zone tactile ≥ 44px (boutons 48px + hitSlop 12px)

### ✅ **Accessibilité :**
- [x] accessibilityRole="button" sur boutons
- [x] accessibilityLabel descriptifs
- [x] Hit slop 12px minimum (md)
- [x] VoiceOver compatible

---

## 🧪 **QA SCRIPT MANUEL (Smoke Test)**

### **Setup :**
```bash
# Reset storage pour test propre
npx expo start
# Dans Metro console :
await AsyncStorage.multiRemove([
  '@luna_cycle_history',
  '@luna_cycle_migrated',
  'cycle_config'
])
# Reload app (Cmd+R)
```

### **Test 1 : Migration OFF (nouveau user)**
1. Vérifie Home : QuickPeriodLog affiche "🩸 Début des règles"
2. Vérifie ExploreGrid : "Mes cycles" présent
3. Tap "Mes cycles" → Empty state "Aucun cycle complet..."
4. Tap "Retour à l'accueil" → retour Home ✅

### **Test 2 : Migration ON (ancien user)**
```javascript
// Dans Metro console, créer ancien config :
await AsyncStorage.setItem('cycle_config', JSON.stringify({
  lastPeriodDate: '2025-10-15',
  cycleLength: 28
}))
// Reload app (Cmd+R)
```
1. Vérifie logs : `[CycleMigration] Migration en cours...`
2. Tap "Mes cycles" → ≥1 cycle affiché (avec barres rose/jaune)
3. Vérifie stats cachées (1 seul cycle < 2)
4. Vérifie countdown caché ✅

### **Test 3 : Start → End cycle**
1. Home → Tap "🩸 Début des règles"
2. Toast "✅ Règles logées !"
3. Bouton devient "🔵 Fin des règles"
4. Tap 2x "Fin" rapidement → 1er OK, 2ème toast warning
5. Bouton redevient "🩸 Début" ✅

### **Test 4 : Moyennes & countdown**
1. Répéter Test 3 pour créer 2 cycles complets
2. "Mes cycles" → Stats visibles (Règles moyennes + Cycle moyen)
3. Home → CycleCountdown visible "X JOURS RESTANTS"
4. Cycle résultat → Badge "J-X avant prochaines règles" ✅

### **Test 5 : Historique**
1. "Mes cycles" → Liste de barres horizontales
2. Plus récent en haut
3. Barres roses (règles) + jaunes (reste) + icône 🥚
4. Durée totale affichée ✅

### **Résultat attendu :** Tous les tests passent sans erreur, UX fluide

---

## 🚀 **PROCHAINES ÉTAPES (v1.1)**

### **Calendrier visuel**
- Librairie `react-native-calendars`
- Marqueurs : rouge (règles), jaune (fertile), orange (ovulation)
- Numéro jour cycle sous chaque date

### **Prédictions fertilité avancées**
- Fenêtre fertile (J-5 à J+1 ovulation)
- Ovulation précise (cycle - 14 jours)
- Icônes visuels (🌱 fertile, 🥚 ovulation)

### **Log quotidien détaillé**
- Symptômes (crampes, fatigue, acné, etc.)
- Humeur (lié au journal existant)
- Flux (léger, moyen, abondant)
- Activité sexuelle

### **Édition historique**
- Modifier dates start/end
- Supprimer un cycle
- Corriger erreurs de saisie

### **Export/Import**
- Export CSV
- Partage médical (PDF)
- Backup/Restore

---

## 📊 **MÉTRIQUES v2.0**

| Métrique | Valeur |
|----------|--------|
| **Fichiers créés** | 7 |
| **Lignes de code** | ~800 |
| **Stores** | 1 (cycleHistoryStore) |
| **Composants** | 4 (QuickLog, Stats, Countdown, HistoryBar) |
| **Écrans** | 1 (my-cycles) |
| **Analytics events** | 4 |
| **Temps implémentation** | ~8h |

---

## ✅ **CONCLUSION**

**Cycle Tracking V2.0 apporte :**
- ✅ Suivi multi-cycles personnalisé
- ✅ Moyennes calculées automatiquement
- ✅ Prédictions fiables
- ✅ UX simple (1 tap pour logger)
- ✅ Offline-first
- ✅ Migration douce
- ✅ Analytics respectueux RGPD

**Base solide pour v1.1 avec calendrier visuel et prédictions avancées !** 🚀

---

**Auteur :** Cursor AI (Claude Sonnet 4.5)  
**Date :** 10 novembre 2025  
**Sprint :** 16

