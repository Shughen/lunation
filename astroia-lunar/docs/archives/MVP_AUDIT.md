# 📋 AUDIT MVP — ASTROIA LUNAR

**Date:** 2026-01-16
**Branche:** `plan/mvp-audit`
**Objectif:** Revalider le périmètre MVP, auditer l'état actuel (mobile + API), et produire un plan d'exécution découpé en chantiers indépendants.

---

## 🎯 RAPPEL: Vision MVP (Source: ROADMAP_MVP_ASTROIA.md)

Le MVP doit permettre à un utilisateur de :
1. Comprendre son **thème natal** (base)
2. Suivre ses **révolutions lunaires** mois par mois
3. Lire un **rapport lunaire mensuel clair et actionnable**
4. Identifier les **moments clés du mois** (VoC, transits majeurs)
5. Faire le lien entre ce qu'il vit et les cycles (journal simple)

### ✅ Inclus MVP
- Thème natal (interprétation v4 senior)
- Révolutions lunaires (12 mois automatiques)
- Rapport lunaire mensuel (format court)
- Void of Course (actuel + prochain)
- Transits majeurs (expliqués : pourquoi / comment)
- Mini journal (1 entrée / jour, simple)

### ❌ Exclus MVP
- Horoscope quotidien IA
- Chat IA conversationnel
- Compatibilité amoureuse
- Gamification lourde (badges, streaks)
- Parent-enfant ML
- Cycle menstruel avancé

---

## 📊 INVENTAIRE ACTUEL

### Mobile (apps/mobile/app/)

**Écrans existants (25 fichiers .tsx) :**

| Écran | Chemin | Lignes | Statut estimé |
|-------|--------|--------|---------------|
| **Home** | `index.tsx` | 622 | ✅ Fonctionnel (complexe) |
| **Welcome** | `welcome.tsx` | 122 | ✅ Onboarding |
| **Login** | `login.tsx` | 375 | ✅ Auth |
| **Onboarding** | `onboarding/index.tsx` | 317 | ✅ |
| | `onboarding/consent.tsx` | 203 | ✅ |
| | `onboarding/disclaimer.tsx` | 207 | ✅ |
| | `onboarding/profile-setup.tsx` | 878 | ✅ (volumineux) |
| **Natal Chart** | `natal-chart/index.tsx` | 362 | ✅ Calcul + sauvegarde |
| | `natal-chart/result.tsx` | 517 | ✅ Affichage |
| **Lunar** | `lunar/index.tsx` | 287 | ⚠️ Test Luna Pack (P1) |
| | `lunar/report.tsx` | 388 | ⚠️ Affichage rapport |
| | `lunar/voc.tsx` | 347 | ⚠️ Void of Course |
| **Lunar Returns** | `lunar-returns/timeline.tsx` | 334 | ✅ Timeline 12 mois |
| **Lunar Month** | `lunar-month/[month].tsx` | 349 | ✅ Détail par mois |
| **Cycle** | `cycle/index.tsx` | 397 | ⚠️ Tracking cycle menstruel |
| | `cycle/history.tsx` | 351 | ⚠️ Historique |
| **Calendar** | `calendar/month.tsx` | 245 | ⚠️ Calendrier |
| **Transits** | `transits/overview.tsx` | 469 | ⚠️ Vue d'ensemble transits |
| | `transits/details.tsx` | 262 | ⚠️ Détail transit |
| **Timeline** | `timeline.tsx` | 259 | ⚠️ Timeline générale |
| **Journal** | `journal.tsx` | 396 | ⚠️ Journal quotidien |
| **Settings** | `settings.tsx` | 401 | ✅ Paramètres |
| **Debug** | `debug/selftest.tsx` | 209 | 🧪 Dev only |

**Légende :**
- ✅ Fonctionnel / Validé
- ⚠️ Existe mais à revoir / aligner
- ❌ Manquant / Incomplet
- 🧪 Dev/Test

### API (apps/api/routes/)

**Routes existantes (9 fichiers .py) :**

| Route | Fichier | Lignes | Endpoints clés |
|-------|---------|--------|----------------|
| **Auth** | `auth.py` | 441 | POST /register, /login, GET /me |
| **Natal** | `natal.py` | 658 | POST /natal-chart, GET /natal-chart |
| | `natal_reading.py` | 217 | POST /reading/read (interprétations) |
| | `natal_interpretation.py` | 404 | POST /interpretation, DELETE /interpretation/{chart_id}/{subject} |
| **Lunar Returns** | `lunar_returns.py` | 1712 | POST /generate, GET /, /current, /{month}, /rolling, /current/report |
| **Luna Pack** | `lunar.py` | 736 | GET /current, POST /voc, /mansion, /return/report |
| **Transits** | `transits.py` | 289 | POST /natal, /lunar_return, GET /overview/{user_id}/{month} |
| **Calendar** | `calendar.py` | 269 | GET /month/{year}/{month} |
| **Reports** | `reports.py` | 136 | GET /report/{report_id} |

**Total lignes API routes:** ~4 800 LOC

---

## 🔗 MATRICE PAGE → ENDPOINT → STATUT

| Feature MVP | Screen Mobile | Endpoint API | Statut | Notes |
|-------------|---------------|--------------|--------|-------|
| **1. Thème Natal** | `natal-chart/index.tsx` | `POST /natal-chart` | ✅ | Calcul via RapidAPI OK |
| | `natal-chart/result.tsx` | `GET /natal-chart` | ✅ | Affichage positions/aspects |
| | | `POST /natal/interpretation` | ✅ | Interprétations v4 senior |
| **2. Révolutions Lunaires** | `lunar-returns/timeline.tsx` | `POST /lunar-returns/generate` | ✅ | 12 mois auto-générés |
| | | `GET /lunar-returns/` | ✅ | Liste complète |
| | | `GET /lunar-returns/current` | ✅ | Mois actuel |
| | `lunar-month/[month].tsx` | `GET /lunar-returns/{month}` | ✅ | Détail par mois |
| **3. Rapport Lunaire** | `lunar/report.tsx` | `POST /lunar/return/report` | ⚠️ | Luna Pack P1 - à valider |
| | | `GET /lunar-returns/current/report` | ⚠️ | Rapport du mois courant |
| **4. Void of Course** | `lunar/voc.tsx` | `POST /lunar/voc` | ⚠️ | Luna Pack P1 - fonctionne |
| | | `GET /lunar/voc/current` | ⚠️ | VoC actuel (cache) |
| **5. Transits Majeurs** | `transits/overview.tsx` | `POST /transits/natal` | ⚠️ | Transits vs thème natal |
| | `transits/details.tsx` | `POST /transits/lunar_return` | ⚠️ | Transits vs révolution |
| | | `GET /transits/overview/{user_id}/{month}` | ⚠️ | Vue d'ensemble mois |
| **6. Mini Journal** | `journal.tsx` | ❌ (local AsyncStorage) | ⚠️ | Pas d'endpoint back (local only) |
| **Home** | `index.tsx` | Multiple (current, climate) | ⚠️ | Hub central - complexe |

### Statut global :
- ✅ **Solidement implémenté** : Thème natal, Révolutions lunaires de base
- ⚠️ **Existe mais à revoir** : Rapports lunaires, VoC, Transits, Journal, Home
- ❌ **Manquant** : Aucune feature critique manquante, mais alignement UX à faire

---

## 📝 SYNTHÈSE ÉTAT ACTUEL

### ✅ CE QUI MARCHE

1. **Auth + Onboarding** : Complet, fonctionnel (inscription, login, profil)
2. **Thème Natal** : Calcul RapidAPI, sauvegarde DB, affichage positions/aspects
3. **Révolutions Lunaires** : Génération automatique 12 mois, timeline, détail par mois
4. **Interprétations v4 Senior** : Prompt refondé, seed offline (natal_interpretations_seed)
5. **Base technique solide** : FastAPI, PostgreSQL, JWT, Expo Router, Zustand

### ⚠️ CE QUI EXISTE MAIS NÉCESSITE ALIGNEMENT

1. **Luna Pack (Lunar)** :
   - Rapport mensuel, VoC, Mansions lunaires (28)
   - Fonctionnel techniquement mais **intégration UX à clarifier**
   - Écrans de test (`lunar/index.tsx`) vs écrans finaux MVP

2. **Transits** :
   - Endpoints existent (natal, lunar_return, overview)
   - Screens existent (overview, details)
   - **Manque : "transits majeurs contextualisés"** (lien révolution lunaire)

3. **Journal** :
   - Screen existe (`journal.tsx`)
   - **Stockage local uniquement** (AsyncStorage)
   - **Manque : liaison auto avec cycle lunaire actif**
   - **Manque : backend pour persistance/sync**

4. **Home (index.tsx)** :
   - Écran central complexe (622 LOC)
   - Gère onboarding, routing, révolution actuelle, daily climate
   - **Manque : clarté sur "Quel est mon cycle actuel ?"**
   - **Besoin : refonte UX centrée révolution lunaire**

5. **Cycle Menstruel** :
   - Screens existent (`cycle/index.tsx`, `cycle/history.tsx`)
   - **HORS MVP** selon ROADMAP (exclu explicitement)
   - **Action : supprimer ou désactiver**

6. **Calendar** :
   - Screen existe (`calendar/month.tsx`)
   - **HORS MVP ?** (non mentionné dans ROADMAP)
   - **Action : clarifier utilité ou supprimer**

7. **Timeline** :
   - Screen existe (`timeline.tsx`)
   - **Doublon avec lunar-returns/timeline ?**
   - **Action : fusionner ou clarifier**

### ❌ CE QUI MANQUE

1. **Rapport Lunaire MVP** :
   - Format défini : 1 page, 3 sections (Climat du mois, Périodes clés, Points d'attention)
   - **Endpoint existe** (`POST /lunar/return/report`) mais **format à valider**
   - **Screen existe** (`lunar/report.tsx`) mais **contenu à adapter**

2. **Transits Majeurs Contextualisés** :
   - "Peu d'aspects, liés à la révolution lunaire en cours, explication factuelle + manifestation concrète"
   - **Endpoints existent** mais **filtrage "majeurs seulement" à vérifier**
   - **Screens existent** mais **UX à retravailler**

3. **Mini Journal Liaison Auto** :
   - Endpoint backend pour persistance
   - Liaison automatique avec cycle lunaire actif (user_id + month + date)
   - Historique par mois/cycle

4. **Home Centré Révolution Lunaire** :
   - Refonte UX : "Quel est mon cycle actuel ?" en évidence
   - Affichage clair du mois lunaire en cours
   - CTA vers rapport mensuel, VoC, transits du mois

---

## ✅ CHECKLIST MVP "SOURCE OF TRUTH"

### 🔐 1. Auth + Onboarding (DONE ✅)
- [x] Inscription avec données de naissance
- [x] Login JWT
- [x] Onboarding 4 étapes (welcome, consent, disclaimer, profile-setup)
- [x] Validation profil complet

### 🌟 2. Thème Natal (DONE ✅)
- [x] Calcul via RapidAPI
- [x] Sauvegarde DB (positions, aspects, maisons)
- [x] Affichage écran result.tsx
- [x] Interprétations v4 senior (Soleil, Lune, Ascendant)
- [x] Seed offline (natal_interpretations_seed)

### 🌙 3. Révolutions Lunaires (MOSTLY DONE ✅)
- [x] Génération automatique 12 mois
- [x] Timeline visuelle (lunar-returns/timeline.tsx)
- [x] Détail par mois (lunar-month/[month].tsx)
- [x] Endpoint /current (révolution en cours)
- [ ] **TODO:** Clarifier "révolution lunaire = fil rouge UX" sur Home

### 📄 4. Rapport Lunaire Mensuel (PARTIELLEMENT ⚠️)
- [x] Endpoint `POST /lunar/return/report`
- [x] Screen `lunar/report.tsx`
- [ ] **TODO:** Valider format MVP (1 page, 3 sections)
- [ ] **TODO:** Intégrer dans Home (CTA visible)
- [ ] **TODO:** Ton clair, concret, senior (audit du contenu)

### 🌑 5. Void of Course (PARTIELLEMENT ⚠️)
- [x] Endpoint `POST /lunar/voc`
- [x] Endpoint `GET /lunar/voc/current`
- [x] Screen `lunar/voc.tsx`
- [ ] **TODO:** Affichage clair sur Home : "VoC maintenant ? oui/non + Prochaine fenêtre"
- [ ] **TODO:** Préparer notifications (infrastructure, sans activer)

### 🪐 6. Transits Majeurs Contextualisés (PARTIELLEMENT ⚠️)
- [x] Endpoints `/transits/natal`, `/transits/lunar_return`
- [x] Screens `transits/overview.tsx`, `transits/details.tsx`
- [ ] **TODO:** Filtrer "peu d'aspects" (majeurs seulement : conjonction, opposition, carré, trigone)
- [ ] **TODO:** Lien explicite avec révolution lunaire en cours
- [ ] **TODO:** Explication factuelle + manifestation concrète (améliorer copy)

### 📓 7. Mini Journal (BACKEND TERMINÉ ✅ | Mobile en attente ⏳)
- [x] Screen `journal.tsx` (UI existe)
- [x] **DONE:** Endpoint backend `POST /api/journal/entry` (user_id, date, mood, note, month)
- [x] **DONE:** Endpoint backend `GET /api/journal/entries` (liste, filtre par mois/année)
- [x] **DONE:** Endpoint backend `GET /api/journal/today` (entrée du jour)
- [x] **DONE:** Endpoint backend `DELETE /api/journal/entry/{id}` (suppression)
- [x] **DONE:** Liaison automatique avec cycle lunaire actif (champ month format "YYYY-MM")
- [x] **DONE:** Migration Alembic exécutée sur Supabase (table `journal_entries` créée)
- [ ] **TODO:** Connecter `journal.tsx` au backend (remplacer AsyncStorage)
- [ ] **TODO:** Créer widget `JournalPrompt.tsx` pour Home
- [ ] **TODO:** Affichage dans Home : "As-tu écrit aujourd'hui ?"

### 🏠 8. Home Centré Révolution Lunaire (REFONTE ⚠️)
- [x] Home existe (`index.tsx`)
- [ ] **TODO:** Refonte UX : "Quel est mon cycle actuel ?" en haut
- [ ] **TODO:** Card révolution lunaire en cours (mois, phase, date début/fin)
- [ ] **TODO:** CTA vers rapport mensuel
- [ ] **TODO:** Widget VoC (statut + prochaine fenêtre)
- [ ] **TODO:** Widget transits majeurs du mois
- [ ] **TODO:** Prompt journal quotidien

### 🧹 9. Nettoyage Hors MVP (ACTION ❌)
- [ ] **TODO:** Supprimer ou désactiver `cycle/*` (cycle menstruel hors MVP)
- [ ] **TODO:** Clarifier utilité `calendar/month.tsx` ou supprimer
- [ ] **TODO:** Fusionner `timeline.tsx` avec `lunar-returns/timeline.tsx` ou supprimer
- [ ] **TODO:** Supprimer écrans de test Luna Pack (`lunar/index.tsx`) une fois intégrés

---

## 🧱 DÉCOUPAGE EN CHANTIERS INDÉPENDANTS

### 🎯 Principe
- Chantiers parallélisables (pas de dépendances croisées)
- Scope fichiers clair
- Branche dédiée
- Validation indépendante (lint, test, curl)
- Risques identifiés

---

### 🏗️ **CHANTIER 1 : Home Centré Révolution Lunaire**

**Branche:** `feat/mvp-home-lunar-centric`

**Objectif:**
Refondre l'écran Home pour répondre clairement à "Quel est mon cycle actuel ?", avec la révolution lunaire en cours comme fil rouge.

**Scope Fichiers:**
- `apps/mobile/app/index.tsx` (refonte UX)
- `apps/mobile/components/CurrentLunarCard.tsx` (nouveau composant)
- `apps/mobile/components/VocWidget.tsx` (nouveau composant)
- `apps/mobile/components/TransitsWidget.tsx` (nouveau composant)
- `apps/mobile/components/JournalPrompt.tsx` (nouveau composant)

**Endpoints utilisés (existants):**
- `GET /lunar-returns/current`
- `GET /lunar/voc/current`
- `GET /transits/overview/{user_id}/{month}`

**Validation:**
```bash
# Mobile
cd apps/mobile
npm run lint
npm run typecheck
# Manuel : tester Home sur device/simulator

# Critères:
# - Révolution lunaire en cours visible en haut
# - Widget VoC fonctionnel
# - Widget transits du mois visible
# - Prompt journal visible
```

**Risques:**
- **Complexité index.tsx** (déjà 622 LOC) → refactorer en sous-composants
- **État partagé** (Zustand) → bien tester les subscriptions
- **Performance** (trop d'API calls) → utiliser cache/SWR

**Estimation:** 3-5 jours

---

### 🏗️ **CHANTIER 2 : Rapport Lunaire Mensuel MVP**

**Branche:** `feat/mvp-lunar-report-format`

**Objectif:**
Valider et finaliser le format MVP du rapport lunaire mensuel (1 page, 3 sections), ajuster le ton (clair, concret, senior), intégrer dans l'UX.

**Scope Fichiers:**
- `apps/api/routes/lunar.py` (valider endpoint `/return/report`)
- `apps/api/services/lunar_services.py` (ajuster format rapport si besoin)
- `apps/mobile/app/lunar/report.tsx` (adapter affichage au format MVP)
- `apps/mobile/app/index.tsx` (ajouter CTA vers rapport)

**Endpoints:**
- `POST /lunar/return/report` (audit + ajustement)
- `GET /lunar-returns/current/report` (audit + ajustement)

**Validation:**
```bash
# API
cd apps/api
pytest tests/test_lunar_report.py -v  # (créer si inexistant)
curl -X POST http://localhost:8000/api/lunar/return/report \
  -H "Authorization: Bearer TOKEN" \
  -d '{"user_id": 1, "month": "2026-01"}'

# Mobile
# Manuel : tester écran lunar/report.tsx

# Critères:
# - Format: 1 page, 3 sections (Climat, Périodes clés, Points d'attention)
# - Ton: clair, concret, senior (pas ésotérique)
# - CTA visible depuis Home
```

**Risques:**
- **Qualité copy** (audit manuel nécessaire)
- **Génération lente** (cache ou async si lourd)

**Estimation:** 2-3 jours

---

### 🏗️ **CHANTIER 3 : VoC Intégration MVP**

**Branche:** `feat/mvp-voc-integration`

**Objectif:**
Afficher clairement le statut Void of Course sur Home, préparer l'infrastructure notifications (sans activer).

**Scope Fichiers:**
- `apps/mobile/components/VocWidget.tsx` (nouveau, utilisé dans Home)
- `apps/mobile/app/lunar/voc.tsx` (audit + simplification si besoin)
- `apps/mobile/services/notificationScheduler.ts` (préparer VoC notifications)
- `apps/api/routes/lunar.py` (audit endpoint `/voc/current`)

**Endpoints:**
- `GET /lunar/voc/current`
- `POST /lunar/voc` (si besoin données détaillées)

**Validation:**
```bash
# API
curl http://localhost:8000/api/lunar/voc/current

# Mobile
# Manuel : tester widget VoC sur Home

# Critères:
# - Affichage: "VoC maintenant ? oui/non"
# - Affichage: "Prochaine fenêtre: [date/heure]"
# - Infrastructure notifications prête (code, pas activé)
```

**Risques:**
- **Précision calculs VoC** (vérifier provider/algo)
- **Notifications iOS/Android** (permissions, infrastructure)

**Estimation:** 2-3 jours

---

### 🏗️ **CHANTIER 4 : Transits Majeurs Contextualisés**

**Branche:** `feat/mvp-transits-major-contextualized`

**Objectif:**
Filtrer les transits pour ne garder que les majeurs (conjonction, opposition, carré, trigone), lier explicitement à la révolution lunaire en cours, améliorer le copy (factuel + manifestation concrète).

**Scope Fichiers:**
- `apps/api/routes/transits.py` (ajouter filtrage aspects majeurs)
- `apps/api/services/transits_services.py` (logique filtrage)
- `apps/mobile/app/transits/overview.tsx` (affichage filtré)
- `apps/mobile/app/transits/details.tsx` (améliorer copy)
- `apps/mobile/components/TransitsWidget.tsx` (widget Home)

**Endpoints:**
- `GET /transits/overview/{user_id}/{month}` (ajouter param `major_only=true`)
- `POST /transits/lunar_return` (filtrer aspects majeurs)

**Validation:**
```bash
# API
cd apps/api
pytest tests/test_transits_major.py -v  # (créer)
curl "http://localhost:8000/api/transits/overview/1/2026-01?major_only=true" \
  -H "Authorization: Bearer TOKEN"

# Mobile
# Manuel : tester transits/overview.tsx

# Critères:
# - Aspects filtrés: conjonction, opposition, carré, trigone uniquement
# - Lien révolution lunaire visible
# - Copy amélioré: explication factuelle + manifestation concrète
```

**Risques:**
- **Qualité copy** (audit manuel nécessaire)
- **Calcul aspects** (vérifier précision RapidAPI)

**Estimation:** 3-4 jours

---

### 🏗️ **CHANTIER 5 : Mini Journal Backend + Liaison**

**Branche:** `feat/mvp-journal-backend-link`

**Statut:** 🟢 **Backend TERMINÉ** (2026-01-16) | 🟡 Mobile en attente

**Objectif:**
Créer l'endpoint backend pour persistance du journal, lier automatiquement les entrées au cycle lunaire actif, afficher le prompt dans Home.

**✅ Complété (Backend):**
- ✅ Modèle `JournalEntry` créé (`apps/api/models/journal_entry.py`)
- ✅ Migration Alembic exécutée sur Supabase (`a1b2c3d4e5f6_create_journal_entries_table.py`)
- ✅ Schemas Pydantic créés (`apps/api/schemas/journal.py`)
- ✅ 4 routes API implémentées et sécurisées (`apps/api/routes/journal.py`):
  - `POST /api/journal/entry` (création/mise à jour, 1 entrée/jour max)
  - `GET /api/journal/entries` (liste avec filtres mois/année + pagination)
  - `GET /api/journal/today` (entrée du jour pour widget Home)
  - `DELETE /api/journal/entry/{id}` (suppression)
- ✅ Tests pytest créés (`apps/api/tests/test_journal.py`, 11 tests)
- ✅ Liaison automatique au cycle lunaire via champ `month` (format "YYYY-MM")

**🔜 Reste à faire (Mobile):**
- ⏳ Connecter `apps/mobile/app/journal.tsx` au backend
- ⏳ Créer widget `JournalPrompt.tsx` pour Home
- ⏳ Ajouter méthodes API dans `apps/mobile/services/api.ts`
- ⏳ Tester intégration complète

**Scope Fichiers:**
- `apps/api/routes/journal.py` (nouveau)
- `apps/api/models/journal_entry.py` (nouveau modèle)
- `apps/api/migrations/xxx_create_journal_entries.py` (migration Alembic)
- `apps/mobile/app/journal.tsx` (connecter au backend)
- `apps/mobile/components/JournalPrompt.tsx` (widget Home)
- `apps/mobile/services/api.ts` (ajouter méthodes journal)

**Endpoints (nouveaux):**
- `POST /api/journal/entry` (créer entrée)
- `GET /api/journal/entries` (liste, filtre par mois/date)
- `GET /api/journal/today` (entrée du jour)

**Validation:**
```bash
# API
cd apps/api
alembic upgrade head  # migration
pytest tests/test_journal.py -v
curl -X POST http://localhost:8000/api/journal/entry \
  -H "Authorization: Bearer TOKEN" \
  -d '{"date": "2026-01-16", "mood": "calm", "note": "Belle journée"}'

# Mobile
# Manuel : tester journal.tsx + widget Home

# Critères:
# - Entrée sauvegardée en DB avec liaison cycle lunaire (month field)
# - Widget Home: "As-tu écrit aujourd'hui ?"
# - Historique par mois fonctionnel
```

**Risques:**
- **Migration DB** (tester rollback)
- **Sync état local/distant** (conflit AsyncStorage vs DB)

**Estimation:** 3-4 jours

---

### 🏗️ **CHANTIER 6 : Nettoyage Hors MVP**

**Branche:** `feat/mvp-cleanup-out-of-scope`

**Objectif:**
Supprimer ou désactiver les écrans hors MVP (cycle menstruel, calendar, timeline doublon), nettoyer les écrans de test Luna Pack.

**Scope Fichiers:**
- `apps/mobile/app/cycle/` (supprimer ou désactiver)
- `apps/mobile/app/calendar/` (supprimer ou désactiver)
- `apps/mobile/app/timeline.tsx` (fusionner avec lunar-returns/timeline ou supprimer)
- `apps/mobile/app/lunar/index.tsx` (supprimer écran de test)
- Routes inutilisées (audit + cleanup)

**Validation:**
```bash
# Mobile
cd apps/mobile
npm run lint
npm run typecheck
# Manuel : vérifier que les écrans supprimés ne cassent pas la navigation

# Critères:
# - Aucune référence aux écrans supprimés dans le code
# - Navigation fluide sans erreurs
# - Diminution du bundle size (mesurer)
```

**Risques:**
- **Navigation cassée** (vérifier liens/routes)
- **État partagé** (vérifier Zustand stores)

**Estimation:** 1-2 jours

---

### 🏗️ **CHANTIER 7 : Tests End-to-End MVP**

**Branche:** `feat/mvp-e2e-tests`

**Objectif:**
Ajouter des tests E2E (Detox ou Maestro) pour valider les parcours MVP critiques.

**Scope Fichiers:**
- `apps/mobile/e2e/` (nouveau dossier)
- `apps/mobile/e2e/mvp-flow.test.ts` (parcours complet MVP)
- `apps/mobile/e2e/home-to-report.test.ts` (Home → Rapport lunaire)
- `apps/mobile/e2e/journal-entry.test.ts` (Créer entrée journal)

**Parcours à tester:**
1. Onboarding → Calcul thème natal → Home
2. Home → Rapport lunaire mensuel
3. Home → VoC actuel
4. Home → Transits majeurs
5. Home → Journal → Créer entrée → Retour Home

**Validation:**
```bash
# E2E
cd apps/mobile
npm run test:e2e

# Critères:
# - 5 parcours E2E passent sans erreur
# - Couverture critique fonctionnelle
```

**Risques:**
- **Flakiness tests E2E** (réseau, timing)
- **Maintenance** (coût élevé)

**Estimation:** 4-5 jours

---

### 🏗️ **CHANTIER 8 : Documentation + Déploiement MVP**

**Branche:** `feat/mvp-documentation-deployment`

**Objectif:**
Finaliser la documentation MVP, préparer le déploiement (CI/CD, env staging, TestFlight/Google Play Beta).

**Scope Fichiers:**
- `QUICKSTART_MVP.md` (guide démarrage rapide MVP)
- `docs/MVP_USER_GUIDE.md` (guide utilisateur MVP)
- `docs/MVP_API.md` (doc API MVP)
- `.github/workflows/ci-mvp.yml` (CI/CD)
- `apps/mobile/app.json` (version, build number)
- `apps/api/Dockerfile` (si déploiement containerisé)

**Validation:**
```bash
# CI/CD
# - Pipeline GitHub Actions passe (lint, test, build)

# Déploiement
# - API déployée sur staging (Render/Railway/Heroku)
# - Mobile build iOS/Android (TestFlight/Google Play Beta)
# - URL staging accessible

# Critères:
# - Documentation complète et à jour
# - CI/CD fonctionnel
# - Déploiement staging réussi
```

**Risques:**
- **Config déploiement** (env vars, secrets)
- **Build mobile** (certificates iOS, keystore Android)

**Estimation:** 3-4 jours

---

## 📅 ORDRE D'EXÉCUTION RECOMMANDÉ

### 🔹 Phase 1 : Fondations Home + Rapport (PRIORITÉ MAX)
**Durée:** 1-2 semaines

1. **CHANTIER 1** : Home Centré Révolution Lunaire (3-5j)
2. **CHANTIER 2** : Rapport Lunaire Mensuel MVP (2-3j)

**Pourquoi ?** Clarifier le "pourquoi" de l'app, rendre le MVP racontable.

---

### 🔹 Phase 2 : Features Différenciantes (PRIORITÉ HAUTE)
**Durée:** 1-2 semaines

3. **CHANTIER 3** : VoC Intégration MVP (2-3j)
4. **CHANTIER 4** : Transits Majeurs Contextualisés (3-4j)

**Pourquoi ?** Ajouter les moments clés du mois, rendre l'usage quotidien.

---

### 🔹 Phase 3 : Journal + Nettoyage (PRIORITÉ MOYENNE)
**Durée:** 1 semaine

5. **CHANTIER 5** : Mini Journal Backend + Liaison (3-4j)
6. **CHANTIER 6** : Nettoyage Hors MVP (1-2j)

**Pourquoi ?** Lien vécu/cycles, simplifier l'app.

---

### 🔹 Phase 4 : Tests + Déploiement (PRIORITÉ FINALE)
**Durée:** 1-2 semaines

7. **CHANTIER 7** : Tests End-to-End MVP (4-5j)
8. **CHANTIER 8** : Documentation + Déploiement MVP (3-4j)

**Pourquoi ?** Valider la qualité, préparer la sortie.

---

## 🎯 DÉFINITION DU "DONE" MVP

Le MVP est considéré prêt quand :

1. ✅ **Home raconte l'histoire lunaire** : "Quel est mon cycle actuel ?" évident
2. ✅ **Rapport mensuel clair** : 1 page, 3 sections, ton senior, actionnable
3. ✅ **VoC quotidien** : Widget Home + écran détail + infra notifications prête
4. ✅ **Transits majeurs contextualisés** : Filtrés, liés révolution, copy factuel
5. ✅ **Journal liaison auto** : Backend, lien cycle lunaire, widget Home
6. ✅ **Aucune feature gadget** : Cycle menstruel, calendar, timeline dédoublonné supprimés
7. ✅ **Tests E2E critiques** : 5 parcours validés
8. ✅ **Documentation complète** : Quickstart, user guide, API doc
9. ✅ **Déploiement staging** : API + Mobile (TestFlight/Google Play Beta)

---

## 🚨 RISQUES GLOBAUX

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| **Scope creep** | 🔴 Critique | Haute | Roadmap figée, revue hebdo |
| **Performance API** (calculs lourds) | 🟠 Important | Moyenne | Cache, async, queue (Celery/Redis) |
| **Qualité copy IA** (rapports, transits) | 🟠 Important | Moyenne | Audit manuel, prompts affinés |
| **Complexité Home** | 🟡 Moyen | Moyenne | Refacto composants, tests unitaires |
| **Flakiness tests E2E** | 🟡 Moyen | Haute | Retry logic, mock réseau |
| **Build mobile iOS/Android** | 🟠 Important | Moyenne | CI/CD early, test devices early |
| **Déploiement infra** | 🔴 Critique | Moyenne | Staging early, rollback plan |

---

## 📝 NOTES FINALES

### Points d'attention
- **Home = Hub central** : Toute refonte doit être testée intensément (UX + perf)
- **Luna Pack P1** : Écrans de test existent, à transformer en écrans finaux MVP
- **Transits majeurs** : Filtrage aspects = clé différenciation, audit prompt
- **Journal** : Backend simple (user_id, date, mood, note, month), pas d'over-engineering
- **Nettoyage** : Supprimer = gagner en clarté, ne pas hésiter

### Prochaines actions immédiates
1. Créer les branches pour chaque chantier
2. Assigner les chantiers (si équipe) ou prioriser (si solo)
3. Commencer Phase 1 : Home + Rapport
4. Revue hebdo de l'avancement

---

**Fin du document MVP_AUDIT.md**
