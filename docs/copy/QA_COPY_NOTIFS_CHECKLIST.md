# QA Copy & Notifications Checklist

**Objectif**: Valider que tous les strings respectent l'ADN Astroia et que les notifications ne violent pas la règle "max 1/mois + VoC opt-in".

**Total Scénarios**: 30

---

## ✅ 1. Onboarding (3 scénarios)

### 1.1 Welcome Screen — Tone Factuel
**Steps**:
1. Lancer l'app pour la première fois
2. Lire le titre et le body du Welcome screen

**Expected**:
- Titre: "Bienvenue sur Astroia Lunar"
- Body mentionne "révolutions lunaires", "28 jours", "pas de notifications quotidiennes"
- Pas de promesses émotionnelles ("transformez votre vie", "découvrez vos pouvoirs")
- Pas d'emojis autres que 🌙 🌑

**ADN Validation**:
- [ ] Tone senior factuel (pas anxiogène)
- [ ] Pas de promesses de transformation
- [ ] Pas de gamification

---

### 1.2 Profile Setup — RGPD Compliance
**Steps**:
1. Taper sur "Commencer" depuis Welcome
2. Lire le body du Profile Setup screen

**Expected**:
- Body mentionne "données privées", "ne sont jamais partagées"
- Champs: prénom, date de naissance, lieu de naissance
- Pas de demande d'email sauf si nécessaire pour compte

**ADN Validation**:
- [ ] Transparence sur usage des données
- [ ] Pas de dark patterns (pré-coches, consentement forcé)
- [ ] Local-first explicite

---

### 1.3 Disclaimer Modal — Version Courte
**Steps**:
1. Compléter Profile Setup
2. Lire le disclaimer modal avant de commencer

**Expected**:
- Body ≤ 210 caractères (version courte)
- Mentionne "analyses symboliques" + "ne remplace pas avis médical"
- Checkbox "J'ai compris" (pas "J'accepte les risques" anxiogène)

**ADN Validation**:
- [ ] Avertissement clair sans ton anxiogène
- [ ] Version complète accessible via Settings > Avertissement médical
- [ ] Pas de sur-dramatisation

---

## ✅ 2. Settings (4 scénarios)

### 2.1 Notifications Toggle — Permission Flow
**Steps**:
1. Ouvrir Settings
2. Taper sur toggle "Nouveau cycle lunaire"
3. Observer le flow de demande de permission

**Expected**:
- Permission demandée **au toggle**, pas au démarrage de l'app
- Si refusée: message "Permission requise" + bouton "Ouvrir les réglages"
- Si accordée: message "Notifications activées"

**ADN Validation**:
- [ ] Pas de demande intrusive au lancement
- [ ] Message d'erreur clair et non culpabilisant
- [ ] Lien direct vers Settings système

---

### 2.2 VoC Notifications — Opt-In Explicite
**Steps**:
1. Vérifier que toggle "Void of Course" est **OFF par défaut**
2. Lire la description du toggle

**Expected**:
- Description: "Alertes optionnelles pour les fenêtres VoC à venir"
- Toggle OFF par défaut (opt-in conscient)
- Pas de pression pour activer ("Ne ratez aucune fenêtre!", "Essentiel!")

**ADN Validation**:
- [ ] Opt-in volontaire (pas opt-out)
- [ ] Description factuelle sans FOMO
- [ ] Respect du rythme utilisateur

---

### 2.3 Avertissement Médical — Version Complète
**Steps**:
1. Ouvrir Settings > Informations légales > Avertissement médical
2. Lire le texte complet

**Expected**:
- Texte complet (≥ 400 chars) via `disclaimers.medical.body`
- Mentionne "ne remplace jamais un diagnostic médical"
- Tone senior, pas défensif ni anxiogène

**ADN Validation**:
- [ ] Version complète accessible après onboarding
- [ ] Tone respectueux et factuel
- [ ] Pas de sur-justification défensive

---

### 2.4 Settings Copy — Longueur Mobile-Safe
**Steps**:
1. Parcourir tous les labels et descriptions Settings
2. Vérifier qu'aucun texte ne déborde ou ne scroll horizontalement

**Expected**:
- Labels ≤ 50 chars
- Descriptions ≤ 150 chars
- Pas de scroll horizontal sur iPhone SE

**ADN Validation**:
- [ ] Tous les strings respectent limites mobile
- [ ] Texte lisible sur petit écran
- [ ] Pas de troncature involontaire

---

## ✅ 3. Empty States (3 scénarios)

### 3.1 Aucun Cycle Généré — CTA Clair
**Steps**:
1. Lancer l'app après onboarding sans générer de cycles
2. Observer le message d'empty state sur Home

**Expected**:
- Titre: "Aucune révolution lunaire générée"
- Body explique qu'il faut générer 12 cycles
- CTA: "Générer mes cycles" (pas "Découvrez votre destin!")

**ADN Validation**:
- [ ] Message factuel sans dramatisation
- [ ] CTA actionnable et clair
- [ ] Pas de FOMO ou pression

---

### 3.2 Aucun VoC à Venir — Message Informatif
**Steps**:
1. Ouvrir écran Void of Course quand aucune fenêtre n'est calculée
2. Lire le message d'empty state

**Expected**:
- Titre: "Aucun Void of Course à venir"
- Body: "Revenez plus tard" (pas "Profitez de cette pause!")
- Pas de CTA manipulateur

**ADN Validation**:
- [ ] Tone neutre et informatif
- [ ] Pas de spin positif forcé
- [ ] Respect du vide (pas de remplissage anxiogène)

---

### 3.3 Aucune Note Journal — Incitation Douce
**Steps**:
1. Ouvrir écran Journal (Phase 2) sans notes
2. Lire le message d'empty state

**Expected**:
- Titre: "Aucune note de cycle"
- Body: "Notez vos observations hebdomadaires" (pas "Commencez maintenant!")
- Pas de badge "Nouveau!" ou compteur de streak

**ADN Validation**:
- [ ] Incitation douce sans pression
- [ ] Pas de gamification (streaks, badges)
- [ ] Respect du rythme utilisateur

---

## ✅ 4. Errors (3 scénarios)

### 4.1 Network Error — Message Non Culpabilisant
**Steps**:
1. Couper la connexion internet
2. Taper sur "Générer mes cycles" depuis Home
3. Observer le message d'erreur

**Expected**:
- Titre: "Erreur réseau"
- Body: "Vérifiez votre connexion internet" (pas "Vous n'êtes pas connecté!")
- CTA: "Réessayer" (pas "OK" passif)

**ADN Validation**:
- [ ] Message factuel sans culpabilisation
- [ ] CTA actionnable
- [ ] Pas de tone frustré ou agressif

---

### 4.2 Cycle Not Found — 404 Propre
**Steps**:
1. Naviguer vers `/lunar/report?id=99999` (ID invalide)
2. Observer le message d'erreur

**Expected**:
- Titre: "Cycle non trouvé"
- Body: "Le cycle demandé n'existe pas ou n'a pas été généré"
- CTA: "Retour" vers Home

**ADN Validation**:
- [ ] Message clair sans jargon technique
- [ ] Navigation de secours fonctionnelle
- [ ] Pas de dead-end

---

### 4.3 Generic Error — Correlation ID
**Steps**:
1. Provoquer une erreur 500 backend (si possible en staging)
2. Observer le message d'erreur générique

**Expected**:
- Titre: "Erreur"
- Body: "Une erreur inattendue s'est produite. ID: {correlation_id}"
- Correlation ID affiché pour support

**ADN Validation**:
- [ ] Correlation ID présent pour debug
- [ ] Message non technique pour l'utilisateur
- [ ] Tone calme sans panique

---

## ✅ 5. Notifications Push (5 scénarios) — **CRITIQUE ADN**

### 5.1 Nouveau Cycle — 1 Fois Par Mois Max
**Steps**:
1. Activer notifications "Nouveau cycle lunaire" dans Settings
2. Attendre le début d'un cycle (ou simuler via backend staging)
3. Vérifier la notification reçue

**Expected**:
- Title: "🌙 Nouveau cycle lunaire"
- Body: "{month} — Lune en {sign}, Ascendant {ascendant}. Consultez votre rapport mensuel."
- Fréquence: **1 fois par mois uniquement**

**ADN Validation**:
- [ ] Max 1 notification cycle/mois
- [ ] Pas de rappels "Vous n'avez pas consulté votre rapport!"
- [ ] Tone factuel sans urgence

---

### 5.2 VoC Start — Opt-In Seulement
**Steps**:
1. **Vérifier que toggle VoC est OFF par défaut**
2. Activer toggle VoC dans Settings
3. Attendre début d'une fenêtre VoC

**Expected**:
- Title: "🌑 Void of Course"
- Body: "La Lune entre en VoC jusqu'à {endTime}. Fenêtre d'observation."
- **Aucune notification si toggle OFF**

**ADN Validation**:
- [ ] Notification envoyée **uniquement si opt-in activé**
- [ ] Pas de notification par défaut
- [ ] Fréquence: 2-4x/mois max (selon fenêtres VoC réelles)

---

### 5.3 VoC End — 30 Min Avant
**Steps**:
1. Activer toggle VoC
2. Attendre 30 min avant fin d'une fenêtre VoC

**Expected**:
- Title: "🌑 Fin du VoC dans 30 min"
- Body: "La Lune quitte le Void of Course à {endTime}."
- **Aucune notification si toggle OFF**

**ADN Validation**:
- [ ] Notification envoyée uniquement si opt-in activé
- [ ] Pas de répétition (1 alerte fin = 1 notification max)
- [ ] Tone informatif sans pression

---

### 5.4 Journal Reminder — Phase 2 Weekly (Opt-In)
**Steps**:
1. Activer paywall Journal (Phase 2)
2. Activer toggle "Rappels hebdomadaires" dans Settings Journal
3. Attendre début de semaine lunaire

**Expected**:
- Title: "🌙 Note hebdomadaire"
- Body: "Semaine {weekNumber} de votre cycle. Notez vos observations si vous le souhaitez."
- **Aucune notification si toggle OFF**
- Fréquence: **max 4x/mois** (4 semaines lunaires)

**ADN Validation**:
- [ ] Opt-in explicite (pas activé par défaut)
- [ ] Tone suggestion sans obligation
- [ ] Pas de streak ou pression

---

### 5.5 Audit Fréquence Totale — Max 9 Notifs/Mois
**Steps**:
1. Activer TOUS les toggles notifications (cycle + VoC + journal)
2. Observer la fréquence totale sur 1 mois

**Expected**:
- 1 notification nouveau cycle
- 4 notifications VoC (2 starts + 2 ends) — moyenne
- 4 notifications journal hebdo (Phase 2)
- **Total: ~9 notifications/mois MAX**

**ADN Validation**:
- [ ] Fréquence totale ≤ 10 notifs/mois
- [ ] Pas de notifications "engagement" (streaks, rappels consultation)
- [ ] Respect strict du rythme mensuel/hebdomadaire

---

## ✅ 6. Paywalls (2 scénarios)

### 6.1 Journal Paywall — Tone Transparent
**Steps**:
1. Taper sur "Journal de Cycle" sans abonnement actif
2. Lire le paywall modal

**Expected**:
- Title: "Journal de Cycle"
- Features listées: notes privées, corrélations, export PDF
- Prix: "4,99 €/mois" (pas "Seulement 4,99 €!")
- CTA: "Débloquer le Journal" (pas "Commencer maintenant!")

**ADN Validation**:
- [ ] Prix affiché clairement sans dark patterns
- [ ] Pas de fausse urgence ("Offre limitée!")
- [ ] Tone factuel sans manipulation

---

### 6.2 Timeline Paywall — 7 Jours Gratuits
**Steps**:
1. Taper sur "Timeline 12 mois" sans abonnement
2. Vérifier mention de l'essai gratuit

**Expected**:
- Mention "7 jours gratuits" visible
- Explication claire: "Annulez avant la fin de l'essai pour ne pas être facturé"
- Pas de pré-coche "Renouvellement automatique"

**ADN Validation**:
- [ ] Essai gratuit mentionné clairement
- [ ] Conditions d'annulation transparentes
- [ ] Pas de subscription par défaut cachée

---

## ✅ 7. Deep Links (3 scénarios)

### 7.1 Deep Link Notification Cycle → Rapport
**Steps**:
1. Recevoir notification "Nouveau cycle lunaire"
2. Taper sur la notification (app fermée)
3. Observer la route ouverte

**Expected**:
- App s'ouvre sur `/lunar/report` (rapport du cycle actuel)
- Pas de dead-end ou écran blanc
- Bouton "Retour" fonctionnel

**ADN Validation**:
- [ ] Deep link fonctionnel depuis app fermée
- [ ] Navigation cohérente
- [ ] Pas de loop infini

---

### 7.2 Deep Link Notification VoC → Écran VoC
**Steps**:
1. Recevoir notification "Void of Course"
2. Taper sur la notification (app en background)
3. Observer la route ouverte

**Expected**:
- App s'ouvre sur `/void-of-course`
- Statut VoC actuel affiché
- Liste des prochaines fenêtres visible

**ADN Validation**:
- [ ] Deep link fonctionnel depuis background
- [ ] Écran VoC s'affiche correctement
- [ ] Pas d'erreur de chargement

---

### 7.3 Deep Link Journal → Note Semaine Actuelle
**Steps**:
1. Recevoir notification "Note hebdomadaire" (Phase 2)
2. Taper sur la notification
3. Observer la route ouverte

**Expected**:
- App s'ouvre sur `/journal` avec focus sur semaine actuelle
- Champ de texte pré-rempli si note existante
- Placeholder "Notez vos observations" si vide

**ADN Validation**:
- [ ] Deep link fonctionnel
- [ ] Focus automatique sur bonne semaine
- [ ] Pas de friction UX

---

## ✅ 8. Copy Contradictions Audit (2 scénarios)

### 8.1 Audit "Max 1 Notif/Mois" — Scan Textes
**Steps**:
1. Rechercher tous les textes mentionnant "notifications" ou "alertes"
2. Vérifier cohérence avec règle "max 1/mois + VoC opt-in"

**Expected**:
- Aucun texte ne promet "notifications quotidiennes"
- Aucun texte ne dit "restez connecté chaque jour"
- Settings descriptions cohérentes avec réalité technique

**ADN Validation**:
- [ ] Pas de contradiction entre copy et comportement réel
- [ ] Promesses alignées avec fréquence réelle
- [ ] Pas de marketing mensonger

---

### 8.2 Audit Tone Anxiogène — Scan Textes
**Steps**:
1. Rechercher mots-clés anxiogènes: "urgence", "essentiel", "ne ratez pas", "danger", "attention"
2. Vérifier qu'aucun n'apparaît dans copy app

**Expected**:
- Aucun mot anxiogène dans onboarding, settings, errors
- Tone reste factuel partout
- Pas de FOMO ou manipulation émotionnelle

**ADN Validation**:
- [ ] Aucun mot anxiogène détecté
- [ ] Tone senior et calme partout
- [ ] Pas de pression temporelle ("Agissez maintenant!")

---

## ✅ 9. Journal Phase 2 (3 scénarios)

### 9.1 Input Limite 50 Caractères
**Steps**:
1. Ouvrir Journal
2. Taper une note de 60 caractères
3. Observer le comportement

**Expected**:
- Compteur affiche "{count}/50"
- Texte bloqué à 50 caractères (pas de troncature silencieuse)
- Message si dépassement: "Limite 50 caractères atteinte"

**ADN Validation**:
- [ ] Limite technique respectée
- [ ] Feedback visuel clair
- [ ] Pas de frustration UX

---

### 9.2 Notes Hebdomadaires — Max 4 Par Cycle
**Steps**:
1. Noter une observation pour chaque semaine lunaire (1-4)
2. Vérifier que 5e note n'est pas possible

**Expected**:
- 4 semaines affichées par cycle (28 jours / 7 = 4)
- Pas de semaine 5 ou semaine 0
- Navigation entre semaines fluide

**ADN Validation**:
- [ ] Structure cohérente avec cycle 28 jours
- [ ] Pas de bug d'affichage
- [ ] Labels semaine corrects (1-4)

---

### 9.3 Journal Paywall — Accès Limité Gratuit
**Steps**:
1. Sans abonnement, tenter d'accéder au Journal
2. Observer le paywall

**Expected**:
- Paywall s'affiche avec titre "Journal de Cycle"
- Features claires (notes privées, corrélations, export)
- Prix transparent: "4,99 €/mois"

**ADN Validation**:
- [ ] Paywall non intrusif
- [ ] Valeur du journal expliquée factuellement
- [ ] Pas de pression ou fausse urgence

---

## 📊 Résumé Validation

**Total Scénarios**: 30
**Scénarios Critiques ADN** (notifications): 5

**Checklist Finale**:
- [ ] Tous les strings respectent limites mobile-safe
- [ ] Aucun mot anxiogène détecté
- [ ] Fréquence notifications ≤ 10/mois
- [ ] Opt-in notifications respecté partout
- [ ] Deep links fonctionnels (3/3)
- [ ] Paywalls transparents (2/2)
- [ ] Copy cohérent avec comportement technique

**Status**: Ready for manual QA. Blocker si 1+ scénario critique échoue.
