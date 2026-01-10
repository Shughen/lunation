# 📊 LUNA – Analytics & Tracking Guide

## 🎯 Objectif
Ce module centralise tout le suivi analytique de l'application via **Mixpanel** et **Supabase logs**.

---

## ⚙️ Installation

```bash
npm install mixpanel-react-native
```

Ajoute ton token Mixpanel dans `/lib/analytics.js` :
```js
const mixpanel = new Mixpanel('TON_TOKEN_MIXPANEL_ICI', true);
```

---

## 📈 Événements suivis

| Événement | Description | Propriétés |
|-----------|--------------|-------------|
| onboarding_completed | Fin de l'onboarding | birth_date, cycle_length |
| journal_entry_created | Nouvelle entrée du journal | mood, phase |
| ai_message_sent | Message utilisateur → IA | length, phase, topic |
| ai_message_received | Réponse IA | latency, tokens_used |
| cycle_phase_changed | Changement de phase du cycle | old_phase, new_phase |
| dashboard_opened | Ouverture du dashboard | days_since_signup |
| export_pdf | Export PDF ou JSON | period_length |
| subscription_upgraded | Passage premium | plan_type, price |
| app_open | Ouverture appli | phase, day_of_cycle |

---

## 🧠 Bonnes pratiques

1. Appelle `trackEvents.appOpen()` dès le lancement de l'app.  
2. Loggue chaque action clé utilisateur (journal, IA, abonnement…).  
3. Pour un nouvel événement → ajoute-le dans `trackEvents`.  
4. Active les **dashboards Mixpanel** :
   - Activation
   - Engagement
   - Rétention
   - Monétisation

---

## 📬 Exemple d'utilisation

```js
import { trackEvents } from '@/lib/analytics';

trackEvents.onboardingCompleted('1989-04-15', 29);
trackEvents.journalEntryCreated('happy', 'luteal');
trackEvents.aiMessageSent(120, 'follicular', 'stress relief');
```

---

## 🧾 Rapports hebdo (optionnel)
Une Edge Function Supabase peut agréger les stats et envoyer un mail :
- users actifs
- journaux créés
- messages IA envoyés
- upgrades premium

