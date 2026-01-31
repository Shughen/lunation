# Astroia Lunar – Guide Claude Code

## 🎯 TL;DR

- **Projet** : Astrologie lunaire mobile (FastAPI + React Native)
- **Phase** : Sprint 9 TERMINÉ - Phase Bêta v3.0 🎉
- **Stack** : FastAPI + Expo + PostgreSQL (Supabase) + Claude Opus 4.5 + RapidAPI
- **Monorepo** : `apps/api` (backend) + `apps/mobile` (frontend)
- **État** : 100% production ready, 59 tests validés, génération IA activée

---

## 🏗️ Architecture Logique

### Backend (`apps/api`)

- **10 routes API** : auth, natal, lunar, transits, journal
- **28 services** : génération IA, cache, RapidAPI integration
- **PostgreSQL Supabase** : Migrations Alembic, RLS désactivé (JWT FastAPI)
- **Génération Claude Opus 4.5** : Temps réel avec fallbacks 4 niveaux
- **Monitoring Prometheus** : 6 métriques + 12 alertes

### Mobile (`apps/mobile`)

- **Expo ~54**, React Native 0.81, Expo Router v6
- **Zustand** (state) + **SWR** (data fetching) + **Axios** (HTTP)
- **i18n** FR/EN support
- **Tab Navigator** : 3 onglets (Home, Calendar, Profile)
- **Bottom Sheet** : Rituel quotidien (guidance, énergies, rituels, journal)
- **Stack screens** : Lunar report, Natal chart, Transits, Journal
- **Doc détaillée** : `apps/mobile/docs/SCREENS.md`

### Intégrations Externes

- **Anthropic Claude** : Interprétations natal + lunar (Opus 4.5)
- **RapidAPI** : Calculs astrologiques (natal chart, lunar returns, transits, VoC)
- **Supabase** : PostgreSQL (RLS off, JWT FastAPI auth)

---

## ⚠️ Règles NON Négociables

### 🔐 Sécurité & Exécution

- ✅ **AUTORISÉ** : Uniquement scripts `tools/*.sh` (allowlist MCP)
- ❌ **INTERDIT** : Commandes shell arbitraires, lire hors repo, modifier fichiers système

### 🚫 Zones Interdites

**JAMAIS modifier/commiter** :
- `.env`, `**/*.key`, `**/secrets*`
- `.claude/settings.json`, `.claude/settings.local.json`
- `apps/mobile/**` (sauf demande explicite)

**JAMAIS afficher** :
- `ANTHROPIC_API_KEY`, `RAPIDAPI_KEY`, `SUPABASE_KEY`, `SECRET_KEY`
- Tokens JWT, données utilisateurs

### 🔄 Workflow Git

- **Un changement = un commit** atomique
- **Toujours `pytest -q`** avant commit
- **Format commits** : `feat/fix/refactor/test/docs(api): message`

### 🎯 Zones de Travail

- ✅ `apps/api` : Modifier librement selon les règles
- ❌ `apps/mobile` : NE PAS toucher sauf demande explicite

---

## 🛠️ Commandes Essentielles

### Backend

```bash
cd apps/api

# Tests
pytest -q                                    # Run all tests (quick mode)
pytest tests/test_X.py -v                    # Run specific test (verbose)

# Run API
uvicorn main:app --reload --port 8000

# Migrations
alembic upgrade head                         # Apply pending migrations

# Health check
curl http://localhost:8000/health            # Expected: {"status":"ok"}
```

### Mobile

```bash
cd apps/mobile

npm start                                    # Start Expo dev server
npx tsc --noEmit                             # Check TypeScript errors
```

### Database

```bash
psql $DATABASE_URL                           # Connect to Supabase DB
psql $DATABASE_URL -c "SELECT COUNT(*) FROM lunar_interpretation_templates;"  # Verify migration (Expected: 1728)
```

---

## ✅ Definition of Done

### Backend

- `pytest -q` → 484+ passed (98.9%+)
- Health check → 200 OK
- Aucun secret affiché/commité
- Code respecte conventions (type hints, docstrings)

### Mobile

- App démarre sans crash
- **Aucun changement sauf demande explicite**

---

## 🔧 Command Dispatcher

Système de commandes locales dans `.claude/commands/` pour charger du contexte ciblé sans scanner le repo.

### Utilisation

```bash
./cmd <commande> [args...]     # Charge le contexte de la commande
./cmd list                      # Liste toutes les commandes disponibles
```

**Règle** : Après `./cmd`, suivre les instructions du fichier chargé. Ne jamais scanner le repo.

> **Approche BMAD-like** : Contexte ciblé + rôles spécialisés + contraintes = -90% tokens vs scan global.

### Commandes Disponibles

| Commande | Description |
|----------|-------------|
| `./cmd test` | Lancer les tests pytest |
| `./cmd commit` | Commit avec conventions projet |
| `./cmd health` | Vérifier santé système |
| `./cmd lunar:debug` | Debugger lunar returns |
| `./cmd lunar:context` | Charger architecture lunar |
| `./cmd lunar:generation` | Debugger génération Claude |
| `./cmd natal:debug` | Debugger natal charts |
| `./cmd natal:context` | Charger architecture natal |
| `./cmd api:route` | Créer nouvelle route FastAPI |
| `./cmd api:service` | Créer nouveau service |
| `./cmd db:migration` | Créer migration Alembic |
| `./cmd mobile:context` | Contexte mobile (read-only) |

### Exemples

```bash
./cmd lunar:debug timeout      # Debug timeouts Claude
./cmd api:route notifications  # Créer route notifications
./cmd test lunar               # Tests lunar uniquement
```

**Créer une commande** : voir `.claude/templates/command-template.md`

---

## 📚 Documentation Détaillée

**Architecture & Historique** :
- `apps/api/docs/ARCHITECTURE.md` — Architecture complète backend + mobile
- `apps/api/docs/SPRINTS_HISTORY.md` — Historique Sprints 2-6
- `apps/api/docs/CHANGELOG.md` — Historique commits

**Guides Pratiques** :
- `apps/api/docs/TROUBLESHOOTING.md` — Résolution problèmes courants
- `apps/api/docs/CONTRIBUTING.md` — Conventions et best practices

**Docs Techniques** :
- `apps/api/docs/LUNAR_ARCHITECTURE_V2.md` — Architecture V2 (4 couches)
- `apps/api/docs/API_LUNAR_V2.md` — API utilisateur V2
- `apps/api/docs/PROMETHEUS_METRICS.md` — Monitoring production
- `apps/api/docs/DEPLOYMENT_PRODUCTION.md` — Guide déploiement
- `apps/api/docs/AB_TESTING_GUIDE.md` — Méthodologie A/B testing

**Mobile** :
- `apps/mobile/docs/SCREENS.md` — Documentation des écrans et navigation

**Index complet** : `apps/api/docs/README.md`

---

## 📌 Fichiers Critiques

**Backend** :
- `config.py`, `main.py`, `database.py`
- `services/lunar_interpretation_generator.py` (V2 generator)
- `routes/*.py` (10 fichiers)

**Mobile** :
- `services/api.ts`, `stores/authStore.ts`
- `app/**/*.tsx`

**Docs** : `.claude/CLAUDE.md` (ce fichier)

---

## 📊 État Actuel

**Sprint 6** : ✅ **TERMINÉ** (24/01/2026)
- ✅ Génération Claude Opus 4.5 temps réel opérationnelle
- ✅ Prompt Caching activé (-90% coûts)
- ✅ Monitoring Prometheus complet (6 métriques + 12 alertes)
- ✅ Tests : 59 tests validés (35 unitaires + 24 E2E)
- ✅ A/B test Opus vs Sonnet (décision : Opus 3× plus rapide)
- ✅ Loading screen mobile animé
- ✅ **100% Production Ready** 🎯

**Sprint 7** : ✅ **TERMINÉ** (30/01/2026)
- ✅ Bottom sheet "Aujourd'hui" avec guidance lunaire par phase
- ✅ Journal multi-entrées par jour (comportement classique)
- ✅ Navigation unifiée : /journal (écriture + historique)
- ✅ Constantes LUNAR_GUIDANCE (8 phases × message + keywords)
- ✅ **Corrections pré-publication v3.0** (6 tickets P0/P1)
  - T3: Orthographe française ("confidentialité", "thème")
  - T4: Déduplication autocomplétion lieu Nominatim
  - T2: Déduplication phases lunaires calendrier
  - T1: Harmonisation dates cycle lunaire (API end_date)
  - T5: Indicateurs visuels phases (16px vs 12px)
  - T6: Section VoC améliorée (orthographe + durée + multi-jours)

**Sprint 8** : ✅ **TERMINÉ** - Refonte Aspects v5 (30/01/2026)
- ✅ **Backend v5 complet**
  - Parser markdown v5 avec section "Attention" → `shadow`
  - Paramètre `version=5` par défaut dans `aspect_explanation_service.py`
  - Query param `aspect_version` dans `/api/natal-chart` (POST & GET)
  - Fallback intelligent : v5 → v4 DB → templates (au lieu de v5 → templates)
  - Filtrage Chiron + nœuds lunaires (exclus des aspects majeurs)
  - Tests unitaires : 6/6 passés ✨
- ✅ **Mobile v5 complet**
  - Interface TypeScript : `shadow?: string` dans `AspectV4`
  - Section "⚠️ Attention" avec style amber warning
  - Affichage conditionnel (rétro-compatible v4)
  - Rendu markdown (bold, listes) via react-native-markdown-display
  - Fix profil : pas de fallbacks "Aries" si thème natal absent
- ✅ **Génération aspects (méthode manuelle Claude Code, $0 API)**
  - **225/225 aspects v5 générés** (22 batches, 100% complété)
  - Toutes planètes couvertes (Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto)
  - 5 types d'aspects : conjunction, opposition, square, trine, sextile
  - Format v5 : Brief → Insight → Concret → Conseil → Attention
- ✅ **Correctifs finaux session 30/01** :
  - Insertion 10 aspects manquants (Moon-Sun, Moon-Uranus)
  - Fix profil mobile : affichage conditionnel thème natal
  - Requête aspect_version=5 par défaut mobile
  - Support markdown pour rendu aspects
  - Doc complète : SESSION_2026-01-30_aspects_v5.md

**Résultats Sprint 8** :
- ✅ 225 aspects v5 (format bienveillant + section Attention)
- ✅ 225 aspects v4 (fallback professionnel depuis DB)
- ✅ Couverture 100% : toutes combinaisons planètes × aspects
- ✅ Budget : $0 USD (génération manuelle dans Claude Code)
- ✅ Qualité : Validation manuelle batch par batch

**Sprint 9** : ✅ **TERMINÉ** - Phase Bêta v3.0 (31/01/2026)
- ✅ **Corrections P0 (UX immédiat)**
  - Version app.json : 1.0.0 → 3.0.0
  - Version footer settings : "MVP v1.4" → "Lunation v3.0"
  - Harmonisation tutoiement complet (vous → tu) dans i18n/fr.json, settings.tsx, profile.tsx
  - Orthographe française home.tsx : "fonctionnalites peuvent etre limitees" → accents corrects
- ✅ **Configuration Bêta (P1)**
  - Nouveau fichier `config/features.ts` avec BETA_CONFIG (accès illimité)
  - Structure PRODUCTION_CONFIG préparée pour freemium futur
- ✅ **Analytics PostHog (P1)**
  - Installation posthog-react-native
  - Service `services/analytics/index.ts` complet
  - Initialisation dans `_layout.tsx`
  - Variables env documentées dans `.env.example`
- ✅ **Tracking événements clés**
  - `screen_view` : home.tsx, lunar-month/[month].tsx
  - `lunar_return_viewed` : consultation révolution lunaire
  - `journal_entry_created` : journalService.ts
  - `notification_opened` : listener dans _layout.tsx
  - `notifications_enabled` : useNotificationsStore.ts

**Prochaines étapes Phase Bêta** :
- [ ] Créer compte PostHog (eu.posthog.com)
- [ ] Ajouter EXPO_PUBLIC_POSTHOG_KEY dans .env
- [ ] Tester tracking en conditions réelles

---

## 📱 Screenshots Android (adb)

Quand l'utilisateur demande un **screenshot** ou **capture d'écran** de l'émulateur/device Android :

```bash
# Dossier de destination
/Users/remibeaurain/astroia/astroia-lunar/apps/mobile/screenshots/

# Commande à utiliser
adb exec-out screencap -p > /Users/remibeaurain/astroia/astroia-lunar/apps/mobile/screenshots/screenshot_$(date +%Y%m%d_%H%M%S).png
```

**Convention de nommage** : `screenshot_YYYYMMDD_HHMMSS.png`

---

**Dernière màj** : 2026-01-31 | **Version** : 9.0 (Phase Bêta v3.0 + Analytics PostHog)
