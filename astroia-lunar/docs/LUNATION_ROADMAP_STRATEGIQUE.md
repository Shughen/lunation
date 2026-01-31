# Lunation — Roadmap Stratégique v3.0

**Date** : 31 janvier 2026  
**Auteur** : Analyse stratégique Claude Opus 4.5  
**Objectif** : Guide d'implémentation pour monétisation, rétention et features futures  

---

## Table des matières

1. [Contexte et problématique](#contexte-et-problématique)
2. [Stratégie d'accès aux révolutions futures](#stratégie-daccès-aux-révolutions-futures)
3. [Modèle de monétisation Freemium](#modèle-de-monétisation-freemium)
4. [Stratégie de notifications](#stratégie-de-notifications)
5. [Feature "Buddy Astro"](#feature-buddy-astro)
6. [Métriques à tracker](#métriques-à-tracker)
7. [Roadmap d'implémentation](#roadmap-dimpllémentation)
8. [Spécifications techniques](#spécifications-techniques)

---

## Contexte et problématique

### Statistiques du marché apps astro

- **75% de churn** après le premier lancement (standard industrie)
- Les utilisateurs satisfont leur curiosité initiale et ne reviennent pas
- Le contenu statique (thème natal) ne crée pas d'habitude

### Avantages compétitifs de Lunation

1. **Révolutions lunaires personnalisées** — contenu unique qui se renouvelle mensuellement
2. **Rituel quotidien** — guidance du jour, mansion lunaire, énergies
3. **Journal intégré** — potentiel de création d'habitude
4. **Interprétations IA** — personnalisation profonde avec Claude Opus 4.5

### Objectifs stratégiques

- **Rétention J+7** : Passer de ~25% (standard) à 40%+
- **Rétention J+30** : Atteindre 20%+
- **Conversion freemium** : Viser 5-8% des utilisateurs actifs
- **LTV (Lifetime Value)** : 15-25€ par utilisateur payant

---

## Stratégie d'accès aux révolutions futures

### Phase Bêta (actuel)

**Comportement** : Tout ouvert, accès illimité

**Objectif** : Collecter des données d'usage pour valider les hypothèses

```typescript
// config/features.ts
export const BETA_CONFIG = {
  lunarReturns: {
    pastMonthsAccess: 'unlimited',
    futureMonthsAccess: 'unlimited',
    interpretationsAccess: 'full',
  },
  journal: {
    historyLimit: null, // illimité
  },
  natalChart: {
    aspectsAccess: 'full',
  },
};
```

### Phase Production

**Comportement** : Freemium avec aperçus

| Contenu | Gratuit | Premium |
|---------|---------|---------|
| Révolution mois en cours | ✅ Complète avec interprétation | ✅ |
| Révolution mois suivant | ⚡ Aperçu (date + signe + maison, sans interprétation) | ✅ Complète |
| Révolutions M+2 et au-delà | 🔒 Bloqué | ✅ |
| Révolutions passées | 🔒 Dernier mois seulement | ✅ Illimité |

**Écran d'aperçu (mois suivant gratuit)** :

```typescript
// components/LunarReturnPreview.tsx

interface LunarReturnPreviewProps {
  month: string;
  year: number;
  returnDate: Date;
  moonSign: string;
  moonHouse: number;
  lunarAscendant: string;
}

/*
  Affichage pour utilisateurs gratuits :
  
  ┌─────────────────────────────────────┐
  │ 🌙 Révolution Lunaire               │
  │    Mai 2026                         │
  │                                     │
  │ 📅 Date de ta révolution            │
  │    23 mai 2026, 14:32               │
  │                                     │
  │ 🌙 Position de la Lune              │
  │    Signe : Lion                     │
  │    Maison : Maison 8                │
  │                                     │
  │ ⬆️ Ascendant de ta révolution       │
  │    Scorpion                         │
  │                                     │
  │ ┌─────────────────────────────────┐ │
  │ │ 🔒 Interprétation complète      │ │
  │ │                                 │ │
  │ │ Découvre ce que ce mois te      │ │
  │ │ réserve avec Lunation Premium   │ │
  │ │                                 │ │
  │ │ [Débloquer pour 4,99€/mois]     │ │
  │ └─────────────────────────────────┘ │
  └─────────────────────────────────────┘
*/
```

**Écran bloqué (M+2 et au-delà)** :

```typescript
// components/LunarReturnLocked.tsx

/*
  ┌─────────────────────────────────────┐
  │ 🌙 Révolution Lunaire               │
  │    Juin 2026                        │
  │                                     │
  │         🔮                          │
  │                                     │
  │   Ta révolution de juin sera        │
  │   disponible le 1er mai 2026        │
  │                                     │
  │   Ou débloque maintenant avec       │
  │   Lunation Premium                  │
  │                                     │
  │   [Voir les avantages Premium]      │
  │                                     │
  │   ─────────────────────────         │
  │                                     │
  │   🔔 Me notifier quand              │
  │      disponible                     │
  └─────────────────────────────────────┘
*/
```

---

## Modèle de monétisation Freemium

### Structure des tiers

#### Tier Gratuit

```typescript
// config/tiers.ts
export const FREE_TIER = {
  name: 'Gratuit',
  price: 0,
  features: {
    // Thème natal
    natalChart: {
      bigThree: true,           // Soleil, Lune, Ascendant
      planets: true,            // Positions sans interprétations
      houses: true,             // Liste des maisons
      aspects: 'list_only',     // Liste sans détails
      interpretations: false,   // Pas d'interprétations IA
    },
    
    // Révolutions lunaires
    lunarReturns: {
      currentMonth: 'full',           // Complet avec interprétation
      nextMonth: 'preview',           // Aperçu sans interprétation
      futureMonths: 'locked',         // Bloqué
      pastMonths: 'last_one_only',    // Dernier mois seulement
    },
    
    // Calendrier
    calendar: {
      moonPhases: true,         // Phases lunaires visibles
      phasesSigns: true,        // Signe astro des phases
      vocWindows: 'today_only', // VoC du jour seulement
    },
    
    // Rituel quotidien
    dailyRitual: {
      guidance: 'short',        // Version courte
      energies: true,           // Jauges créativité/intuition
      mansion: true,            // Mansion lunaire
      rituals: 'one_only',      // 1 rituel suggéré
      transits: false,          // Pas de transits personnels
    },
    
    // Journal
    journal: {
      enabled: true,
      historyDays: 7,           // 7 jours d'historique
      patterns: false,          // Pas d'analyse des patterns
    },
    
    // Notifications
    notifications: {
      newMoonReminder: true,
      fullMoonReminder: true,
      lunarReturnReminder: true,
      vocAlerts: false,         // Pas d'alertes VoC
      dailyGuidance: false,     // Pas de guidance quotidienne
    },
  },
};
```

#### Tier Premium

```typescript
export const PREMIUM_TIER = {
  name: 'Premium',
  prices: {
    monthly: 4.99,
    yearly: 29.99,  // ~2.50€/mois, 50% de réduction
  },
  trialDays: 7,
  features: {
    // Thème natal
    natalChart: {
      bigThree: true,
      planets: true,
      houses: true,
      aspects: 'full',              // Détails + interprétations
      interpretations: true,        // Interprétations IA complètes
    },
    
    // Révolutions lunaires
    lunarReturns: {
      currentMonth: 'full',
      nextMonth: 'full',
      futureMonths: 'full',         // Tous les mois futurs
      pastMonths: 'unlimited',      // Historique illimité
    },
    
    // Calendrier
    calendar: {
      moonPhases: true,
      phasesSigns: true,
      vocWindows: 'week',           // VoC de la semaine
    },
    
    // Rituel quotidien
    dailyRitual: {
      guidance: 'full',             // Version complète
      energies: true,
      mansion: true,
      rituals: 'all',               // Tous les rituels
      transits: true,               // Transits personnels
    },
    
    // Journal
    journal: {
      enabled: true,
      historyDays: null,            // Illimité
      patterns: true,               // Analyse IA des patterns émotionnels
    },
    
    // Notifications
    notifications: {
      newMoonReminder: true,
      fullMoonReminder: true,
      lunarReturnReminder: true,
      vocAlerts: true,              // Alertes VoC
      dailyGuidance: true,          // Guidance quotidienne
      aspectAlerts: true,           // Alertes aspects importants
    },
    
    // Bonus
    extras: {
      exportPdf: true,              // Export PDF des rapports
      widgets: true,                // Widgets iOS/Android
      buddyAstro: true,             // Feature sociale (future)
    },
  },
};
```

### Implémentation du paywall

```typescript
// services/subscription.ts

import { Platform } from 'react-native';
import Purchases from 'react-native-purchases';

export const REVENUE_CAT_API_KEY = {
  ios: 'appl_XXXXX',
  android: 'goog_XXXXX',
};

export async function initializePurchases(userId: string) {
  Purchases.configure({
    apiKey: Platform.OS === 'ios' 
      ? REVENUE_CAT_API_KEY.ios 
      : REVENUE_CAT_API_KEY.android,
    appUserID: userId,
  });
}

export async function checkPremiumStatus(): Promise<boolean> {
  const customerInfo = await Purchases.getCustomerInfo();
  return customerInfo.entitlements.active['premium'] !== undefined;
}

export async function purchaseMonthly(): Promise<boolean> {
  try {
    const offerings = await Purchases.getOfferings();
    const monthlyPackage = offerings.current?.monthly;
    if (monthlyPackage) {
      await Purchases.purchasePackage(monthlyPackage);
      return true;
    }
    return false;
  } catch (error) {
    console.error('Purchase failed:', error);
    return false;
  }
}

export async function purchaseYearly(): Promise<boolean> {
  try {
    const offerings = await Purchases.getOfferings();
    const yearlyPackage = offerings.current?.annual;
    if (yearlyPackage) {
      await Purchases.purchasePackage(yearlyPackage);
      return true;
    }
    return false;
  } catch (error) {
    console.error('Purchase failed:', error);
    return false;
  }
}

export async function restorePurchases(): Promise<boolean> {
  try {
    const customerInfo = await Purchases.restorePurchases();
    return customerInfo.entitlements.active['premium'] !== undefined;
  } catch (error) {
    console.error('Restore failed:', error);
    return false;
  }
}
```

### Écran de paywall

```typescript
// app/premium/index.tsx

/*
  Design du paywall :
  
  ┌─────────────────────────────────────┐
  │         ✨ Lunation Premium         │
  │                                     │
  │   Débloque tout le potentiel de     │
  │        ta guidance lunaire          │
  │                                     │
  │  ┌─────────────────────────────┐    │
  │  │ ✅ Révolutions illimitées   │    │
  │  │    Passées et futures       │    │
  │  │                             │    │
  │  │ ✅ Interprétations IA       │    │
  │  │    Claude Opus 4.5          │    │
  │  │                             │    │
  │  │ ✅ Aspects détaillés        │    │
  │  │    Thème natal complet      │    │
  │  │                             │    │
  │  │ ✅ Alertes personnalisées   │    │
  │  │    VoC, transits, guidance  │    │
  │  │                             │    │
  │  │ ✅ Journal illimité         │    │
  │  │    Avec analyse des patterns│    │
  │  └─────────────────────────────┘    │
  │                                     │
  │  ┌─────────────────────────────┐    │
  │  │  ANNUEL        MENSUEL     │    │
  │  │  29,99€        4,99€       │    │
  │  │  (2,50€/mois)  /mois       │    │
  │  │  [POPULAIRE]               │    │
  │  └─────────────────────────────┘    │
  │                                     │
  │  [ Commencer l'essai gratuit 7j ]   │
  │                                     │
  │  Annuler à tout moment              │
  │  Restaurer mes achats               │
  └─────────────────────────────────────┘
*/
```

---

## Stratégie de notifications

### Principe directeur

Les notifications sont le **moteur principal de rétention**. Elles doivent être :
- **Personnalisées** (basées sur le thème natal)
- **Pertinentes** (liées à des événements réels)
- **Non-spam** (2-3 par semaine maximum)
- **Actionnables** (mènent vers du contenu)

### Types de notifications

#### 1. Notifications de cycle lunaire

```typescript
// services/notifications/lunarCycle.ts

interface LunarCycleNotification {
  type: 'new_moon' | 'full_moon' | 'lunar_return' | 'phase_change';
  title: string;
  body: string;
  data: {
    screen: string;
    params?: Record<string, any>;
  };
  scheduledFor: Date;
}

// Nouvelle Lune
const newMoonNotification: LunarCycleNotification = {
  type: 'new_moon',
  title: '🌑 Nouvelle Lune ce soir',
  body: 'Moment idéal pour poser tes intentions. Qu\'est-ce que tu veux manifester ?',
  data: {
    screen: 'journal',
    params: { prompt: 'new_moon_intentions' },
  },
  scheduledFor: newMoonDate,
};

// Pleine Lune
const fullMoonNotification: LunarCycleNotification = {
  type: 'full_moon',
  title: '🌕 Pleine Lune en {sign}',
  body: 'Ton énergie créative est à son maximum. C\'est le moment de célébrer tes avancées.',
  data: {
    screen: 'daily_ritual',
  },
  scheduledFor: fullMoonDate,
};

// Révolution lunaire personnelle
const lunarReturnNotification: LunarCycleNotification = {
  type: 'lunar_return',
  title: '🌙 Ta nouvelle révolution commence',
  body: 'Un nouveau mois lunaire s\'ouvre pour toi. Découvre les thèmes de {month}.',
  data: {
    screen: 'lunar_return',
    params: { month: currentMonth },
  },
  scheduledFor: lunarReturnDate,
};
```

#### 2. Notifications Void of Course (Premium)

```typescript
// services/notifications/voc.ts

interface VocNotification {
  type: 'voc_starting' | 'voc_ending';
  title: string;
  body: string;
  scheduledFor: Date;
}

// Début de VoC
const vocStartingNotification: VocNotification = {
  type: 'voc_starting',
  title: '⏸️ Pause lunaire dans 1h',
  body: 'La Lune entre en Void of Course à {time}. Évite les décisions importantes jusqu\'à {endTime}.',
  scheduledFor: subHours(vocStartTime, 1),
};

// Fin de VoC
const vocEndingNotification: VocNotification = {
  type: 'voc_ending',
  title: '▶️ La Lune est de retour',
  body: 'Fin de la pause lunaire. Tu peux reprendre tes projets en toute confiance.',
  scheduledFor: vocEndTime,
};
```

#### 3. Notifications de guidance quotidienne (Premium)

```typescript
// services/notifications/dailyGuidance.ts

interface DailyGuidanceNotification {
  type: 'morning_guidance' | 'evening_reflection';
  title: string;
  body: string;
  scheduledFor: Date;
}

// Guidance du matin (8h)
const morningGuidance: DailyGuidanceNotification = {
  type: 'morning_guidance',
  title: '☀️ Ta guidance du jour',
  body: '{guidanceShort}', // Généré dynamiquement
  scheduledFor: setHours(today, 8),
};

// Réflexion du soir (21h) - 2x par semaine
const eveningReflection: DailyGuidanceNotification = {
  type: 'evening_reflection',
  title: '🌙 Moment de réflexion',
  body: 'Comment s\'est passée ta journée ? Prends 2 minutes pour écrire dans ton journal.',
  scheduledFor: setHours(today, 21),
};
```

#### 4. Notifications d'aspects importants (Premium)

```typescript
// services/notifications/aspects.ts

interface AspectNotification {
  type: 'major_aspect';
  title: string;
  body: string;
  aspectType: string;
  planets: [string, string];
  scheduledFor: Date;
}

// Exemple : Transit important
const majorAspectNotification: AspectNotification = {
  type: 'major_aspect',
  title: '⭐ Aspect puissant aujourd\'hui',
  body: 'Soleil trigone ta Lune natale — journée d\'harmonie émotionnelle.',
  aspectType: 'trine',
  planets: ['transit_sun', 'natal_moon'],
  scheduledFor: aspectExactDate,
};
```

#### 5. Notifications de réengagement

```typescript
// services/notifications/reengagement.ts

interface ReengagementNotification {
  type: 'journal_reminder' | 'inactive_user' | 'feature_discovery';
  title: string;
  body: string;
  trigger: 'days_since_last_visit' | 'days_since_last_journal';
  triggerValue: number;
}

// Rappel journal (3 jours sans écrire)
const journalReminder: ReengagementNotification = {
  type: 'journal_reminder',
  title: '📝 Ton journal t\'attend',
  body: 'Tu n\'as pas écrit depuis 3 jours. Comment te sens-tu avec la Lune en {currentSign} ?',
  trigger: 'days_since_last_journal',
  triggerValue: 3,
};

// Utilisateur inactif (7 jours)
const inactiveUserNotification: ReengagementNotification = {
  type: 'inactive_user',
  title: '🌙 La Lune a bougé depuis ta dernière visite',
  body: 'Tu as manqué {eventsCount} événements lunaires. Rattrape ton retard !',
  trigger: 'days_since_last_visit',
  triggerValue: 7,
};
```

### Calendrier de notifications (exemple semaine type)

```
Lundi    : —
Mardi    : Guidance du matin (Premium)
Mercredi : Alerte VoC si applicable (Premium)
Jeudi    : Réflexion du soir (Premium)
Vendredi : —
Samedi   : Guidance du matin (Premium)
Dimanche : Rappel journal si inactif

+ Notifications événementielles (nouvelle lune, pleine lune, révolution)
```

### Implémentation technique

```typescript
// services/notifications/scheduler.ts

import * as Notifications from 'expo-notifications';
import { lunarService } from '@/services/lunar';
import { userService } from '@/services/user';

export async function scheduleWeeklyNotifications(userId: string) {
  const user = await userService.getUser(userId);
  const isPremium = user.subscription?.status === 'active';
  
  // Annuler les notifications existantes
  await Notifications.cancelAllScheduledNotificationsAsync();
  
  // Récupérer les événements lunaires du mois
  const lunarEvents = await lunarService.getMonthEvents();
  
  // Notifications gratuites (tout le monde)
  for (const event of lunarEvents) {
    if (event.type === 'new_moon' || event.type === 'full_moon') {
      await scheduleNotification({
        title: event.type === 'new_moon' ? '🌑 Nouvelle Lune ce soir' : '🌕 Pleine Lune ce soir',
        body: event.type === 'new_moon' 
          ? 'Moment idéal pour poser tes intentions.'
          : `Pleine Lune en ${event.sign}. Ton énergie est à son maximum.`,
        trigger: { date: subHours(event.date, 6) },
        data: { screen: 'calendar' },
      });
    }
  }
  
  // Révolution lunaire personnelle
  const nextReturn = await lunarService.getNextLunarReturn(userId);
  if (nextReturn) {
    await scheduleNotification({
      title: '🌙 Ta nouvelle révolution commence demain',
      body: `Découvre les thèmes de ${nextReturn.monthName}.`,
      trigger: { date: subDays(nextReturn.date, 1) },
      data: { screen: 'lunar_return' },
    });
  }
  
  // Notifications Premium uniquement
  if (isPremium) {
    // VoC de la semaine
    const vocWindows = await lunarService.getWeekVocWindows();
    for (const voc of vocWindows) {
      await scheduleNotification({
        title: '⏸️ Pause lunaire dans 1h',
        body: `Évite les décisions importantes jusqu'à ${format(voc.endTime, 'HH:mm')}.`,
        trigger: { date: subHours(voc.startTime, 1) },
        data: { screen: 'calendar' },
      });
    }
    
    // Guidance bi-hebdomadaire
    const tuesdayMorning = getNextWeekday(2, 8); // Mardi 8h
    const saturdayMorning = getNextWeekday(6, 8); // Samedi 8h
    
    await scheduleNotification({
      title: '☀️ Ta guidance du jour',
      body: 'Découvre l\'énergie lunaire qui t\'accompagne aujourd\'hui.',
      trigger: { date: tuesdayMorning },
      data: { screen: 'home' },
    });
    
    await scheduleNotification({
      title: '☀️ Ta guidance du week-end',
      body: 'Comment profiter de l\'énergie lunaire ce week-end ?',
      trigger: { date: saturdayMorning },
      data: { screen: 'home' },
    });
  }
}

async function scheduleNotification(config: {
  title: string;
  body: string;
  trigger: Notifications.NotificationTriggerInput;
  data?: Record<string, any>;
}) {
  await Notifications.scheduleNotificationAsync({
    content: {
      title: config.title,
      body: config.body,
      data: config.data,
      sound: true,
    },
    trigger: config.trigger,
  });
}
```

---

## Feature "Buddy Astro"

### Concept

Permettre aux utilisateurs d'ajouter des proches pour voir comment leurs cycles lunaires interagissent. Crée de la valeur sociale et des raisons de revenir.

### User flow

```
1. Profil → "Ajouter un proche"
2. Entrer prénom + date/heure/lieu de naissance
3. Voir la compatibilité lunaire
4. Recevoir des notifications sur les interactions de cycles
```

### Écrans

#### Liste des proches

```typescript
// app/buddies/index.tsx

/*
  ┌─────────────────────────────────────┐
  │ 👥 Mes proches                      │
  │                                     │
  │ ┌─────────────────────────────────┐ │
  │ │ 🌙 Marie                        │ │
  │ │ Soleil Poissons • Lune Bélier  │ │
  │ │ Compatibilité lunaire : 78%     │ │
  │ │                          →      │ │
  │ └─────────────────────────────────┘ │
  │                                     │
  │ ┌─────────────────────────────────┐ │
  │ │ 🌙 Thomas                       │ │
  │ │ Soleil Scorpion • Lune Cancer   │ │
  │ │ Compatibilité lunaire : 85%     │ │
  │ │                          →      │ │
  │ └─────────────────────────────────┘ │
  │                                     │
  │ [ + Ajouter un proche ]             │
  │                                     │
  │ ───────────────────────────────     │
  │                                     │
  │ 💡 Astuce                           │
  │ Ajoute ton partenaire ou tes amis   │
  │ proches pour découvrir comment vos  │
  │ cycles lunaires s'influencent.      │
  └─────────────────────────────────────┘
*/
```

#### Détail compatibilité

```typescript
// app/buddies/[id].tsx

/*
  ┌─────────────────────────────────────┐
  │ ← Retour                            │
  │                                     │
  │ 🌙 Toi & Marie                      │
  │    Compatibilité lunaire            │
  │                                     │
  │ ┌─────────────────────────────────┐ │
  │ │        78%                      │ │
  │ │   ████████████░░░░              │ │
  │ │   Harmonie naturelle            │ │
  │ └─────────────────────────────────┘ │
  │                                     │
  │ 🌙 Vos Lunes                        │
  │ ┌─────────────────────────────────┐ │
  │ │ Toi        ↔        Marie      │ │
  │ │ Lion               Bélier      │ │
  │ │                                 │ │
  │ │ Trigone de feu 🔥              │ │
  │ │ Vos besoins émotionnels        │ │
  │ │ s'harmonisent naturellement.   │ │
  │ └─────────────────────────────────┘ │
  │                                     │
  │ 📅 Ce mois-ci ensemble              │
  │ ┌─────────────────────────────────┐ │
  │ │ Ta révolution : 6 janv (Lion)  │ │
  │ │ Sa révolution : 12 janv (Bélier)│ │
  │ │                                 │ │
  │ │ 💡 Période du 6-12 janv :      │ │
  │ │ Tu entres dans ton nouveau     │ │
  │ │ cycle avant elle. Partage ton  │ │
  │ │ énergie renouvelée !           │ │
  │ └─────────────────────────────────┘ │
  │                                     │
  │ 🔔 Notifications pour ce duo        │
  │ [ ] Alerter quand nos cycles        │
  │     interagissent                   │
  └─────────────────────────────────────┘
*/
```

### Notifications duo

```typescript
// services/notifications/buddyAstro.ts

interface BuddyNotification {
  type: 'cycle_interaction' | 'lunar_return_sync' | 'full_moon_impact';
  title: string;
  body: string;
  buddyName: string;
}

// Exemple : Les deux révolutions lunaires sont proches
const cycleInteractionNotification: BuddyNotification = {
  type: 'cycle_interaction',
  title: '🌙 Synchronicité avec Marie',
  body: 'Vos révolutions lunaires sont à 3 jours d\'écart. Période de connexion intense.',
  buddyName: 'Marie',
};

// Exemple : Pleine Lune impacte les deux
const fullMoonImpactNotification: BuddyNotification = {
  type: 'full_moon_impact',
  title: '🌕 Pleine Lune pour toi et Thomas',
  body: 'Cette Pleine Lune en Cancer active ta Lune ET celle de Thomas. Soirée émotionnelle en vue.',
  buddyName: 'Thomas',
};
```

### Modèle de données

```typescript
// types/buddy.ts

interface Buddy {
  id: string;
  userId: string;        // Propriétaire
  name: string;
  birthDate: Date;
  birthTime: string;     // "HH:mm" ou null si inconnu
  birthPlace: {
    name: string;
    lat: number;
    lon: number;
    timezone: string;
  };
  
  // Calculé
  natalChart: {
    sun: { sign: string; degree: number };
    moon: { sign: string; degree: number };
    ascendant?: { sign: string; degree: number };
  };
  
  // Compatibilité avec l'utilisateur
  compatibility: {
    overall: number;     // 0-100
    moonHarmony: number;
    elementBalance: string;
    keyAspects: Aspect[];
  };
  
  // Préférences
  notificationsEnabled: boolean;
  createdAt: Date;
}
```

### Limitations

| Tier | Nombre de proches |
|------|-------------------|
| Gratuit | 0 |
| Premium | 3 |

---

## Métriques à tracker

### Métriques d'acquisition

```typescript
// analytics/acquisition.ts

interface AcquisitionMetrics {
  // Downloads
  dailyDownloads: number;
  weeklyDownloads: number;
  monthlyDownloads: number;
  
  // Sources
  organicInstalls: number;
  paidInstalls: number;
  referralInstalls: number;
  
  // Onboarding
  onboardingStarted: number;
  onboardingCompleted: number;
  onboardingDropoff: {
    step: number;
    count: number;
  }[];
}
```

### Métriques de rétention

```typescript
// analytics/retention.ts

interface RetentionMetrics {
  // DAU / WAU / MAU
  dau: number;           // Daily Active Users
  wau: number;           // Weekly Active Users
  mau: number;           // Monthly Active Users
  dauMauRatio: number;   // Stickiness (objectif: > 20%)
  
  // Cohortes
  retentionD1: number;   // % utilisateurs revenus J+1
  retentionD7: number;   // % utilisateurs revenus J+7
  retentionD30: number;  // % utilisateurs revenus J+30
  
  // Churn
  dailyChurnRate: number;
  monthlyChurnRate: number;
}
```

### Métriques d'engagement

```typescript
// analytics/engagement.ts

interface EngagementMetrics {
  // Sessions
  avgSessionDuration: number;      // En secondes
  avgSessionsPerUser: number;      // Par semaine
  
  // Écrans
  screenViews: {
    home: number;
    calendar: number;
    profile: number;
    lunarReturn: number;
    natalChart: number;
    journal: number;
  };
  
  // Features
  journalEntriesPerUser: number;
  lunarReturnsViewed: number;
  aspectsClicked: number;
  notificationOpenRate: number;
  
  // Depth
  avgScreensPerSession: number;
  scrollDepth: {
    screen: string;
    avgDepth: number;
  }[];
}
```

### Métriques de monétisation

```typescript
// analytics/monetization.ts

interface MonetizationMetrics {
  // Conversion
  freeToTrialRate: number;        // % gratuits → essai
  trialToPaidRate: number;        // % essais → payants
  overallConversionRate: number;  // % gratuits → payants
  
  // Revenue
  mrr: number;                    // Monthly Recurring Revenue
  arr: number;                    // Annual Recurring Revenue
  arpu: number;                   // Average Revenue Per User
  arppu: number;                  // Average Revenue Per Paying User
  ltv: number;                    // Lifetime Value
  
  // Subscriptions
  activeSubscriptions: number;
  monthlySubscriptions: number;
  yearlySubscriptions: number;
  
  // Churn revenue
  monthlyChurnRevenue: number;
  cancellationReasons: {
    reason: string;
    count: number;
  }[];
}
```

### Implémentation avec Analytics

```typescript
// services/analytics.ts

import analytics from '@react-native-firebase/analytics';

export const Analytics = {
  // Événements d'écran
  trackScreenView: (screenName: string) => {
    analytics().logScreenView({
      screen_name: screenName,
      screen_class: screenName,
    });
  },
  
  // Événements personnalisés
  trackEvent: (eventName: string, params?: Record<string, any>) => {
    analytics().logEvent(eventName, params);
  },
  
  // Événements spécifiques Lunation
  trackLunarReturnViewed: (month: string, isPremium: boolean) => {
    analytics().logEvent('lunar_return_viewed', {
      month,
      is_premium: isPremium,
    });
  },
  
  trackJournalEntry: (wordCount: number, moonSign: string) => {
    analytics().logEvent('journal_entry_created', {
      word_count: wordCount,
      moon_sign: moonSign,
    });
  },
  
  trackNotificationOpened: (notificationType: string) => {
    analytics().logEvent('notification_opened', {
      notification_type: notificationType,
    });
  },
  
  trackPaywallShown: (trigger: string) => {
    analytics().logEvent('paywall_shown', {
      trigger,
    });
  },
  
  trackSubscriptionStarted: (plan: 'monthly' | 'yearly', fromTrial: boolean) => {
    analytics().logEvent('subscription_started', {
      plan,
      from_trial: fromTrial,
    });
  },
  
  // Propriétés utilisateur
  setUserProperties: (properties: {
    isPremium: boolean;
    sunSign: string;
    moonSign: string;
    accountAgeDays: number;
  }) => {
    analytics().setUserProperties({
      is_premium: properties.isPremium.toString(),
      sun_sign: properties.sunSign,
      moon_sign: properties.moonSign,
      account_age_days: properties.accountAgeDays.toString(),
    });
  },
};
```

---

## Roadmap d'implémentation

### Phase 1 : Bêta (actuel → +2 semaines)

**Objectif** : Collecter des données d'usage

| Tâche | Priorité | Estimation |
|-------|----------|------------|
| Corriger vouvoiement/tutoiement | P0 | 2h |
| Mettre à jour version v3.0 | P0 | 15min |
| Intégrer Firebase Analytics | P1 | 4h |
| Tracker les événements clés | P1 | 2h |
| Implémenter notifications basiques | P1 | 4h |

**Livrables** :
- [ ] App cohérente (orthographe, ton)
- [ ] Analytics fonctionnels
- [ ] Notifications nouvelle lune / pleine lune / révolution

---

### Phase 2 : Pré-lancement (+2 → +4 semaines)

**Objectif** : Préparer la monétisation

| Tâche | Priorité | Estimation |
|-------|----------|------------|
| Intégrer RevenueCat | P0 | 8h |
| Créer écran paywall | P0 | 6h |
| Implémenter tiers gratuit/premium | P0 | 8h |
| Créer aperçu révolutions futures | P1 | 4h |
| Limiter journal à 7 jours (gratuit) | P1 | 2h |
| Ajouter signes astro sur phases calendrier | P2 | 2h |

**Livrables** :
- [ ] Paywall fonctionnel
- [ ] Abonnement mensuel et annuel
- [ ] Essai gratuit 7 jours
- [ ] Limitations tier gratuit actives

---

### Phase 3 : Lancement (+4 → +6 semaines)

**Objectif** : Lancer sur les stores

| Tâche | Priorité | Estimation |
|-------|----------|------------|
| Screenshots App Store / Play Store | P0 | 4h |
| Description et métadonnées | P0 | 2h |
| Soumettre iOS | P0 | 1h |
| Soumettre Android | P0 | 1h |
| Préparer support utilisateurs | P1 | 2h |
| Landing page web | P2 | 8h |

**Livrables** :
- [ ] App publiée sur App Store
- [ ] App publiée sur Play Store
- [ ] Page web de présentation

---

### Phase 4 : Post-lancement (+6 → +10 semaines)

**Objectif** : Optimiser rétention et conversion

| Tâche | Priorité | Estimation |
|-------|----------|------------|
| Notifications Premium (VoC, guidance) | P1 | 8h |
| A/B test paywall | P1 | 4h |
| Analyse cohortes et ajustements | P1 | Continu |
| Widgets iOS/Android | P2 | 16h |
| Export PDF rapports | P2 | 8h |

**Livrables** :
- [ ] Notifications Premium complètes
- [ ] Données de conversion analysées
- [ ] Widgets fonctionnels

---

### Phase 5 : Feature Buddy Astro (+10 → +14 semaines)

**Objectif** : Ajouter dimension sociale

| Tâche | Priorité | Estimation |
|-------|----------|------------|
| Design écrans Buddy Astro | P1 | 4h |
| Backend stockage proches | P1 | 8h |
| Calcul compatibilité lunaire | P1 | 8h |
| Notifications duo | P2 | 4h |
| Tests et polish | P2 | 4h |

**Livrables** :
- [ ] Feature Buddy Astro complète (Premium)
- [ ] Notifications interactions de cycles

---

## Spécifications techniques

### Structure de fichiers à créer

```
apps/mobile/
├── config/
│   ├── tiers.ts                    # Configuration gratuit/premium
│   ├── features.ts                 # Feature flags
│   └── analytics.ts                # Configuration analytics
│
├── services/
│   ├── subscription/
│   │   ├── index.ts                # Service principal
│   │   ├── revenueCat.ts           # Intégration RevenueCat
│   │   └── hooks.ts                # useSubscription, usePremium
│   │
│   ├── notifications/
│   │   ├── index.ts                # Service principal
│   │   ├── scheduler.ts            # Planification
│   │   ├── lunarCycle.ts           # Notifs cycle lunaire
│   │   ├── voc.ts                  # Notifs VoC
│   │   ├── dailyGuidance.ts        # Notifs guidance
│   │   └── reengagement.ts         # Notifs réengagement
│   │
│   └── analytics/
│       ├── index.ts                # Service principal
│       ├── events.ts               # Définition des événements
│       └── userProperties.ts       # Propriétés utilisateur
│
├── components/
│   ├── premium/
│   │   ├── PaywallModal.tsx        # Modal paywall
│   │   ├── PremiumBadge.tsx        # Badge Premium
│   │   ├── LockedContent.tsx       # Contenu verrouillé
│   │   └── UpgradeButton.tsx       # Bouton upgrade
│   │
│   └── LunarReturnPreview.tsx      # Aperçu révolution (gratuit)
│
├── app/
│   ├── premium/
│   │   └── index.tsx               # Écran paywall complet
│   │
│   └── buddies/                    # (Phase 5)
│       ├── index.tsx               # Liste des proches
│       ├── [id].tsx                # Détail compatibilité
│       └── add.tsx                 # Ajouter un proche
│
├── hooks/
│   ├── useSubscription.ts          # État abonnement
│   ├── usePremiumFeature.ts        # Vérifier accès feature
│   └── useAnalytics.ts             # Tracking simplifié
│
└── stores/
    └── subscriptionStore.ts        # Zustand store abonnement
```

### Variables d'environnement à ajouter

```bash
# .env

# RevenueCat
REVENUE_CAT_IOS_KEY=appl_XXXXX
REVENUE_CAT_ANDROID_KEY=goog_XXXXX

# Firebase Analytics
FIREBASE_API_KEY=XXXXX
FIREBASE_PROJECT_ID=lunation-app

# Feature flags
ENABLE_PREMIUM=true
ENABLE_BUDDY_ASTRO=false
ENABLE_WIDGETS=false
```

### Dépendances à installer

```bash
# Monétisation
npm install react-native-purchases

# Analytics
npm install @react-native-firebase/app @react-native-firebase/analytics

# Notifications (déjà installé avec Expo)
# expo-notifications

# Widgets (Phase 4)
npm install react-native-widget-extension  # iOS
```

---

## Conclusion

Ce document sert de référence pour l'implémentation progressive des fonctionnalités de monétisation et rétention de Lunation. 

**Priorités immédiates** :
1. Corrections UX (vouvoiement, version)
2. Intégration analytics
3. Notifications basiques

**Priorités court terme** :
4. Système de monétisation freemium
5. Notifications avancées

**Priorités moyen terme** :
6. Feature Buddy Astro
7. Widgets

La clé du succès est de **mesurer avant d'optimiser**. Les données de la bêta guideront les ajustements du modèle freemium.
