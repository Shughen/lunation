# ✨ Sprint 13 - Améliorations & Features Premium

**Date début:** 09/11/2025  
**Durée estimée:** 1-2 semaines  
**Objectif:** Enrichir LUNA avec features premium et remplacer les stubs

---

## 🎯 Objectifs Sprint 13

### **Phase 1 : Cycle Calculator Réel** 🩸
- Remplacer les stubs par calculs réels
- Algorithme prédiction cycle
- Gestion cycles irréguliers
- Fenêtre fertile calculée

### **Phase 2 : Moon Calculator** 🌙
- Calcul position lunaire réelle (éphémérides)
- Signe lunaire quotidien précis
- Phase lunaire (nouvelle, pleine, etc.)
- Intégration API astronomique

### **Phase 3 : Notifications Push** 🔔
- Rappels début de cycle
- Changement de phase
- Insights IA quotidiens
- Horoscope du jour
- Permission opt-in

### **Phase 4 : Export PDF Avancé** 📄
- Rapport cycle mensuel
- Graphiques inclus
- Insights IA résumés
- Design professionnel
- Partage email/social

### **Phase 5 : Mode Offline Complet** ✈️
- Cache intelligent
- Queue sync automatique
- Indicateur connexion
- Données critiques offline
- Retry automatique

### **Phase 6 : Onboarding Interactif** 🎓
- Tour guidé fonctionnalités
- Tooltips contextuels
- Progress tracking
- Skip possible
- Gamification

---

## 📋 User Stories Sprint 13

### US1: Calculs Cycle Réels
**En tant qu'** utilisatrice  
**Je veux** un calcul précis de mon cycle  
**Afin d'** avoir des prédictions fiables

**Acceptance Criteria:**
- [ ] Algorithme calcul jour du cycle précis
- [ ] Gestion cycles irréguliers (21-35 jours)
- [ ] Prédiction prochaines règles
- [ ] Fenêtre fertile calculée (J10-J17)
- [ ] Historique cycles sauvegardé

---

### US2: Position Lunaire Réelle
**En tant qu'** utilisatrice astrologie  
**Je veux** la vraie position de la Lune  
**Afin d'** avoir des recommandations précises

**Acceptance Criteria:**
- [ ] Calcul signe lunaire quotidien réel
- [ ] Phase lunaire (nouvelle, croissant, pleine, décroissant)
- [ ] Pourcentage illumination
- [ ] Intégration API éphémérides gratuite
- [ ] Mise à jour quotidienne automatique

---

### US3: Notifications Intelligentes
**En tant qu'** utilisatrice  
**Je veux** être rappelée des moments clés  
**Afin de** ne rien manquer

**Acceptance Criteria:**
- [ ] Notification "Tes règles arrivent dans 2 jours"
- [ ] Notification "Tu entres en phase d'ovulation"
- [ ] Notification "Insight du jour disponible"
- [ ] Notification "Horoscope prêt"
- [ ] Opt-in (permission explicite)
- [ ] Fréquence configurable (Settings)

---

### US4: Export PDF Professionnel
**En tant qu'** utilisatrice premium (futur)  
**Je veux** exporter un rapport PDF  
**Afin de** partager avec mon médecin ou garder

**Acceptance Criteria:**
- [ ] Génération PDF rapport cycle (1 mois)
- [ ] Graphiques inclus (humeur, énergie)
- [ ] Insights IA résumés
- [ ] Design professionnel LUNA branding
- [ ] Partage email/WhatsApp
- [ ] Sauvegarde locale

---

### US5: Mode Offline Robuste
**En tant qu'** utilisatrice  
**Je veux** utiliser LUNA sans connexion  
**Afin de** journaliser partout

**Acceptance Criteria:**
- [ ] Toutes features critiques offline
- [ ] Sync automatique au retour connexion
- [ ] Indicateur online/offline visible
- [ ] Queue des actions en attente
- [ ] Aucune perte de données

---

### US6: Onboarding Guidé
**En tant que** nouvelle utilisatrice  
**Je veux** être guidée pas-à-pas  
**Afin de** comprendre rapidement LUNA

**Acceptance Criteria:**
- [ ] Tour interactif 5 étapes
- [ ] Tooltips sur fonctions clés
- [ ] Skip possible à tout moment
- [ ] Progress bar visible
- [ ] Animations fluides

---

## 🏗️ Architecture Technique Sprint 13

### 1. cycleCalculator.js (Service Réel)

**Fichier : `lib/services/cycleCalculator.js`**
```javascript
/**
 * Calcule le jour actuel du cycle
 */
export function getCurrentCycleDay(lastPeriodStart, cycleLength = 28) {
  const today = new Date();
  const start = new Date(lastPeriodStart);
  const diffTime = today - start;
  const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
  return (diffDays % cycleLength) + 1;
}

/**
 * Détermine la phase actuelle
 */
export function getCurrentPhase(cycleDay) {
  if (cycleDay <= 5) return 'menstrual';
  if (cycleDay <= 13) return 'follicular';
  if (cycleDay <= 16) return 'ovulation';
  return 'luteal';
}

/**
 * Calcule la fenêtre fertile (J10-J17)
 */
export function isFertile(cycleDay) {
  return cycleDay >= 10 && cycleDay <= 17;
}

/**
 * Prédit la prochaine période
 */
export function predictNextPeriod(lastPeriodStart, cycleLength = 28) {
  const start = new Date(lastPeriodStart);
  const nextPeriod = new Date(start);
  nextPeriod.setDate(start.getDate() + cycleLength);
  return nextPeriod;
}

/**
 * Calcule le niveau d'énergie selon la phase
 */
export function calculateEnergyLevel(phase, dayInPhase) {
  const energyMap = {
    menstrual: [30, 35, 40, 45, 50],       // J1-5
    follicular: [55, 60, 65, 70, 75, 80, 85, 90], // J6-13
    ovulation: [95, 100, 95],              // J14-16
    luteal: [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35], // J17-27
  };
  
  return energyMap[phase]?.[dayInPhase] || 50;
}
```

**Intégration :**
- Remplacer stub dans `app/(tabs)/home.js`
- Utiliser dans `TodayCard.js`
- Utiliser dans `chartDataService.js`

---

### 2. moonCalculator.js (Éphémérides)

**Fichier : `lib/services/moonCalculator.js`**
```javascript
import { sun, moon } from 'astronomia';

/**
 * Calcule le signe lunaire actuel (réel)
 */
export function getTodayMoonSign() {
  const now = new Date();
  const jd = toJulianDay(now);
  const moonPos = moon.apparentPosition(jd);
  
  // Longitude lunaire en degrés
  const longitude = moonPos.lon * (180 / Math.PI);
  
  // Déterminer le signe (30° par signe)
  const signIndex = Math.floor(longitude / 30);
  const signs = [
    { name: 'Bélier', emoji: '♈' },
    { name: 'Taureau', emoji: '♉' },
    { name: 'Gémeaux', emoji: '♊' },
    { name: 'Cancer', emoji: '♋' },
    { name: 'Lion', emoji: '♌' },
    { name: 'Vierge', emoji: '♍' },
    { name: 'Balance', emoji: '♎' },
    { name: 'Scorpion', emoji: '♏' },
    { name: 'Sagittaire', emoji: '♐' },
    { name: 'Capricorne', emoji: '♑' },
    { name: 'Verseau', emoji: '♒' },
    { name: 'Poissons', emoji: '♓' },
  ];
  
  return signs[signIndex];
}

/**
 * Calcule la phase lunaire actuelle
 */
export function getMoonPhase() {
  const now = new Date();
  const jd = toJulianDay(now);
  const phase = moon.phase(jd);
  
  // Phase en degrés (0° = nouvelle, 180° = pleine)
  const phaseDegrees = phase * (180 / Math.PI);
  const illumination = Math.round(((1 - Math.cos(phase)) / 2) * 100);
  
  let phaseName = '';
  if (phaseDegrees < 45) phaseName = 'Nouvelle lune';
  else if (phaseDegrees < 90) phaseName = 'Premier croissant';
  else if (phaseDegrees < 135) phaseName = 'Premier quartier';
  else if (phaseDegrees < 180) phaseName = 'Gibbeuse croissante';
  else if (phaseDegrees < 225) phaseName = 'Pleine lune';
  else if (phaseDegrees < 270) phaseName = 'Gibbeuse décroissante';
  else if (phaseDegrees < 315) phaseName = 'Dernier quartier';
  else phaseName = 'Dernier croissant';
  
  return { phaseName, illumination };
}

function toJulianDay(date) {
  return (date.getTime() / 86400000) + 2440587.5;
}
```

**Alternative API gratuite :**
```javascript
// Si astronomia trop complexe, utiliser API
const response = await fetch(
  `https://api.astronomyapi.com/api/v2/bodies/positions/moon?...`
);
```

---

### 3. Notifications Push

**Setup Expo Notifications :**
```bash
npx expo install expo-notifications
```

**Service : `lib/services/notificationService.js`**
```javascript
import * as Notifications from 'expo-notifications';
import { hasHealthConsent } from './consentService';

// Config handler
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: true,
  }),
});

export async function requestPermission() {
  const { status: existingStatus } = await Notifications.getPermissionsAsync();
  let finalStatus = existingStatus;
  
  if (existingStatus !== 'granted') {
    const { status } = await Notifications.requestPermissionsAsync();
    finalStatus = status;
  }
  
  return finalStatus === 'granted';
}

export async function scheduleNextPeriodReminder(nextPeriodDate) {
  const consent = await hasHealthConsent();
  if (!consent) return;
  
  // 2 jours avant
  const reminderDate = new Date(nextPeriodDate);
  reminderDate.setDate(reminderDate.getDate() - 2);
  
  await Notifications.scheduleNotificationAsync({
    content: {
      title: '🩸 Tes règles arrivent',
      body: 'Dans 2 jours environ. Prépare-toi en douceur.',
      data: { type: 'period_reminder' },
    },
    trigger: {
      date: reminderDate,
    },
  });
}
```

---

### 4. Export PDF

**Package : `react-native-pdf-lib` ou `expo-print`**
```bash
npx expo install expo-print expo-sharing
```

**Service : `lib/services/pdfService.js`**
```javascript
import * as Print from 'expo-print';
import * as Sharing from 'expo-sharing';

export async function generateCycleReport(cycleData, insights) {
  const html = `
    <html>
      <head>
        <style>
          body { font-family: Arial; padding: 40px; }
          h1 { color: #C084FC; }
          .chart { margin: 20px 0; }
          .insight { 
            background: #F3E8FF; 
            padding: 15px; 
            border-radius: 10px; 
            margin: 10px 0; 
          }
        </style>
      </head>
      <body>
        <h1>🌙 LUNA - Rapport Cycle</h1>
        <p>Période : ${cycleData.startDate} - ${cycleData.endDate}</p>
        
        <h2>📊 Résumé</h2>
        <p>Durée cycle : ${cycleData.cycleLength} jours</p>
        <p>Phase actuelle : ${cycleData.currentPhase}</p>
        <p>Énergie moyenne : ${cycleData.avgEnergy}%</p>
        
        <h2>💡 Insights IA</h2>
        ${insights.map(i => `
          <div class="insight">
            ${i.emoji} ${i.text}
          </div>
        `).join('')}
        
        <footer>
          <p style="color: #999; font-size: 12px;">
            Généré par LUNA - Cycle & Cosmos<br>
            ${new Date().toLocaleDateString('fr-FR')}
          </p>
        </footer>
      </body>
    </html>
  `;
  
  const { uri } = await Print.printToFileAsync({ html });
  await Sharing.shareAsync(uri);
}
```

---

### 5. Mode Offline

**Service : `lib/services/syncService.js`**
```javascript
import NetInfo from '@react-native-community/netinfo';
import AsyncStorage from '@react-native-async-storage/async-storage';

let syncQueue = [];
let isOnline = true;

// Écouter changements connexion
NetInfo.addEventListener(state => {
  const wasOffline = !isOnline;
  isOnline = state.isConnected;
  
  if (isOnline && wasOffline) {
    console.log('[Sync] Back online, processing queue');
    processQueue();
  }
});

export async function queueAction(action) {
  syncQueue.push({
    ...action,
    timestamp: Date.now(),
  });
  
  await AsyncStorage.setItem('sync_queue', JSON.stringify(syncQueue));
  
  if (isOnline) {
    processQueue();
  }
}

async function processQueue() {
  if (syncQueue.length === 0) return;
  
  console.log(`[Sync] Processing ${syncQueue.length} actions`);
  
  for (const action of syncQueue) {
    try {
      await executeAction(action);
      syncQueue = syncQueue.filter(a => a.timestamp !== action.timestamp);
    } catch (error) {
      console.error('[Sync] Action failed:', error);
      // Garder dans la queue pour retry
    }
  }
  
  await AsyncStorage.setItem('sync_queue', JSON.stringify(syncQueue));
}
```

---

### 6. Onboarding Amélioré

**Package : `react-native-onboarding-swiper`**
```bash
npm install react-native-onboarding-swiper
```

**Écrans onboarding :**
1. **Bienvenue** : Logo LUNA + tagline
2. **Cycle** : Explication suivi cycle
3. **Astrologie** : Explication corrélation cosmos
4. **IA** : Présentation assistant contextuel
5. **Confidentialité** : Consentements RGPD

---

## ⏱️ Estimation Sprint 13

| Tâche | Complexité | Durée |
|-------|------------|-------|
| cycleCalculator réel | Moyenne | 3h |
| moonCalculator API | Moyenne | 3h |
| Notifications setup | Moyenne | 3h |
| Notifications smart | Moyenne | 2h |
| Export PDF service | Moyenne | 3h |
| Export PDF design | Faible | 2h |
| Sync service offline | Élevée | 4h |
| Offline UI indicators | Faible | 1h |
| Onboarding swiper | Moyenne | 3h |
| Onboarding tooltips | Faible | 2h |
| Tests features | Moyenne | 3h |
| Integration & polish | Faible | 2h |
| **Total** | | **~31h** |

**Durée estimée :** 1-2 semaines

---

## 🚀 Plan d'Exécution

### **Jour 1-2 : Services Réels** 📐
1. Implémenter `cycleCalculator.js`
2. Intégrer dans Home, TodayCard, Dashboard
3. Tests calculs (Jest)
4. Implémenter `moonCalculator.js`
5. Intégrer API éphémérides
6. Tests position lunaire

### **Jour 3-4 : Notifications** 🔔
1. Setup expo-notifications
2. Permission request UI
3. Notifications prédictives cycle
4. Notifications insights quotidiens
5. Settings notifications
6. Tests iOS + Android

### **Jour 5-6 : Export PDF** 📄
1. Setup expo-print
2. Générer HTML template
3. Graphiques en images
4. Design professionnel
5. Partage multi-plateformes
6. Tests export

### **Jour 7-8 : Mode Offline** ✈️
1. Service sync queue
2. Indicateurs UI online/offline
3. Cache intelligent
4. Retry automatique
5. Tests déconnexion

### **Jour 9-10 : Onboarding** 🎓
1. Setup onboarding swiper
2. 5 écrans guidés
3. Tooltips contextuels
4. Progress tracking
5. Tests UX

---

## 📦 Packages à Installer

```bash
cd /Users/remibeaurain/astroia/astroia-app

# Notifications
npx expo install expo-notifications

# Export PDF
npx expo install expo-print expo-sharing

# Onboarding (optionnel, peut faire custom)
npm install react-native-onboarding-swiper

# Astronomie (calculs lunaires)
npm install astronomia
# Ou utiliser API gratuite astronomy-api.com
```

---

## ✅ Definition of Done - Sprint 13

### Cycle Calculator
- [ ] Calculs cycle précis
- [ ] Gestion cycles irréguliers
- [ ] Prédiction prochaines règles
- [ ] Fenêtre fertile
- [ ] Tests coverage >80%

### Moon Calculator
- [ ] Position lunaire réelle
- [ ] Phase lunaire actuelle
- [ ] Intégration API
- [ ] Mise à jour quotidienne
- [ ] Fallback si API down

### Notifications
- [ ] Permission request fluide
- [ ] 4 types notifs (cycle, phase, insight, horoscope)
- [ ] Schedule automatique
- [ ] Settings on/off
- [ ] Tests iOS + Android

### Export PDF
- [ ] Génération rapport cycle
- [ ] Graphiques inclus
- [ ] Design professionnel
- [ ] Partage multi-canaux
- [ ] Tests export

### Mode Offline
- [ ] Features critiques offline
- [ ] Sync automatique
- [ ] Indicateurs UI
- [ ] Queue persistante
- [ ] 0 perte de données

### Onboarding
- [ ] 5 écrans guidés
- [ ] Animations fluides
- [ ] Skip possible
- [ ] Progress tracking
- [ ] Tests UX

---

## 🎯 Livrable Final Sprint 13

**LUNA 2.1.0 - Features Premium :**
- ✅ Calculs cycle réels (prédictions précises)
- ✅ Position lunaire réelle (astronomie)
- ✅ Notifications intelligentes
- ✅ Export PDF rapports
- ✅ Mode offline robuste
- ✅ Onboarding interactif

**Prêt pour production publique !** 🎉

---

## 💡 Alternatives Sprint 13

Si tu préfères **d'autres features**, on peut faire :

### Option B : Monétisation
- Paywall Premium (4,99€/mois)
- RevenueCat integration
- Features premium (export PDF, analyses illimitées)
- Trial 7 jours

### Option C : Social
- Partage insights sur réseaux
- Communauté LUNA (forum)
- Success stories
- Referral program

### Option D : Advanced Astro
- Transits planétaires (pas que Lune)
- Prévisions annuelles
- Retrogrades Mercury, Venus
- Éclipses alerts

---

**Quelle option préfères-tu pour Sprint 13 ?**

A. Features Premium (plan ci-dessus) ✨  
B. Monétisation 💰  
C. Social & Community 👥  
D. Advanced Astro 🪐  
E. Autre ? (dis-moi !)

Je continue avec le plan actuel (Option A) ou tu veux changer ? 🚀

