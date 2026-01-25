# Astroia Lunar – Architecture Détaillée

## 🏗️ Vue d'Ensemble

**Stack** : FastAPI + Expo React Native + PostgreSQL (Supabase) + Anthropic Claude + RapidAPI
**Monorepo** : `apps/api` (backend) + `apps/mobile` (frontend React Native)

---

## 📊 Architecture Backend (`apps/api`)

### Routes principales (10 fichiers)

```
routes/
├── auth.py                          POST /api/auth/login, /register
├── natal.py                         POST /api/natal-chart (JWT+DEV)
├── natal_reading.py                 POST/GET /api/natal/reading (JWT+DEV)
├── natal_interpretation.py          POST /api/natal/interpretation (JWT)
├── natal_aspect_interpretation.py   POST /api/natal/aspects/enrich (JWT)
├── lunar_returns.py                 POST /api/lunar-returns/current (JWT+DEV)
├── lunar.py                         POST /api/reports/lunar/{month} (JWT)
├── reports.py                       POST /api/reports/lunar/{month} (JWT)
├── transits.py                      GET /api/transits/overview/{month} (JWT)
└── journal.py                       CRUD /api/journal/entries (JWT)
```

### Services critiques (28 fichiers)

```
services/
├── natal_interpretation_service.py           (1335 LOC) Anthropic integration
├── lunar_report_builder.py                   (928 LOC) Reports V4 + V2 migration
├── lunar_interpretation_generator.py         (700 LOC) 🆕 V2 generator avec métriques/logs/retry
├── interpretation_cache_service.py           (695 LOC) Cache applicatif
├── voc_cache_service.py                      (467 LOC) VoC cache + retry logic
├── rapidapi_client.py                        (317 LOC) Best Astrology API client
├── lunar_interpretation_legacy_wrapper.py    (181 LOC) 🆕 Wrapper rétrocompatibilité V1→V2
├── lunar_interpretation_service.py           Interprétations lunaires DB/IA (V1 deprecated)
├── lunar_interpretation_v2_service.py        V2 avec fallback templates
├── transits_service.py                       Calculs transits
├── daily_climate_service.py                  Ambiance journalière
└── ... (17 autres services)
```

### Dépendances Production (requirements.txt)

```python
# Core
fastapi==0.109.0, uvicorn[standard]==0.27.0, pydantic>=2.11.7

# Database
sqlalchemy==2.0.25, alembic==1.13.1, psycopg2-binary==2.9.9, asyncpg==0.29.0

# AI/LLM
anthropic==0.39.0

# Observabilité (Sprint 5 - Task 2.1) 🆕
structlog==24.1.0           # Logs structurés JSON
prometheus-client==0.20.0   # Métriques production
tenacity==8.2.3             # Retry logic avec exponential backoff

# Testing
pytest==7.4.4, pytest-asyncio==0.23.3
```

### Modèles SQLAlchemy (12 fichiers)

```
models/
User (INTEGER PK)
├── NatalChart (UUID PK, FK user_id INTEGER)
├── LunarReturn (FK user_id INTEGER)
├── TransitsOverview (FK user_id INTEGER)
├── JournalEntry (FK user_id INTEGER)
├── LunarInterpretation (v1, fichiers JSON obsolètes)
├── LunarInterpretationV2 (v2, pré-générées en DB)
└── autres relations...
```

### Intégrations externes

#### Anthropic Claude (natal_interpretation_service.py)

- **Modèles** : Haiku (rapide), Sonnet (équilibré), Opus 4.5 (haute qualité)
- **Usage** : Interprétations natal + lunar (si `LUNAR_LLM_MODE=anthropic`)
- **Config** : `ANTHROPIC_API_KEY`, `NATAL_LLM_MODE=anthropic`

#### RapidAPI Best Astrology API (rapidapi_client.py)

- **Endpoints** : Natal chart, Lunar returns, Transits, VoC
- **Fallback** : Swiss Ephemeris local si échec RapidAPI
- **Config** : `RAPIDAPI_KEY`, retry logic avec exponential backoff

#### Supabase PostgreSQL (database.py)

- **Auth désactivée** côté Supabase (JWT FastAPI only)
- **RLS désactivé** (doc commit e3531c8)
- **Config** : `SUPABASE_URL`, `SUPABASE_KEY`, `SECRET_KEY`

### Configuration (.env)

```bash
# Versions et modes
LUNAR_INTERPRETATION_VERSION=2          # 1 (fichiers) | 2 (DB)
LUNAR_LLM_MODE=off                      # off (templates) | anthropic (Opus)
NATAL_LLM_MODE=anthropic                # anthropic only

# Auth & Dev
DEV_AUTH_BYPASS=true                    # Dev only: skip JWT on some routes
SECRET_KEY=your-secret-key-here         # JWT signing

# External services
ANTHROPIC_API_KEY=sk-ant-...
RAPIDAPI_KEY=...
SUPABASE_URL=https://....supabase.co
SUPABASE_KEY=eyJ...
DATABASE_URL=postgresql://...

# Caching
INTERPRETATION_CACHE_TTL=3600           # 1h cache interprétations
VOC_CACHE_TTL=3600                      # 1h cache VoC
```

---

## 📱 Architecture Mobile (`apps/mobile`)

### Écrans principaux

```
app/
├── index.tsx                        Home (guards + 5 widgets)
├── lunar/report.tsx                 Rapport lunaire V2
├── natal-chart/
│   ├── index.tsx                    Formulaire thème natal
│   └── result.tsx                   Affichage résultats
├── transits/
│   ├── overview.tsx                 Vue mensuelle transits
│   └── details.tsx                  Détails timing/themes/advice
├── journal/
│   ├── index.tsx                    Liste entrées
│   └── [id].tsx                     Détail entrée
├── settings.tsx                     Paramètres utilisateur
└── onboarding/*                     Welcome flow complet
```

### État intégration API

```
✅ Fonctionnel : Auth, Lunar returns, Natal chart, Transits overview, VoC, Journal
⚠️ En cours : Natal interpretations enrichies, Transits details (timing/themes/advice)
```

### Stack technique

```
- Expo ~54.0.30, React Native 0.81.5
- Expo Router v6 (file-based routing)
- Zustand (state management)
- SWR (data fetching + cache)
- Axios (HTTP client)
- TypeScript 5.9.2
- i18n (FR/EN support)
```

---

## 🏗️ Architecture Lunaire V2 : 4 Couches

```
Layer 1: FAITS ASTRONOMIQUES (immutables)
  └─ LunarReturn (existant) : moon_sign, moon_house, lunar_ascendant, aspects

Layer 2: NARRATION IA TEMPORELLE (régénérable) ⭐ NOUVEAU
  └─ LunarInterpretation : user_id, lunar_return_id FK, input_json, output_text
     Génération: Claude Opus 4.5 à la volée
     Cache: DB temporelle (idempotence via UNIQUE constraint)

Layer 3: CACHE APPLICATION (FastAPI)
  └─ LunarReport (existant) : cache court terme (TTL 1h)

Layer 4: FALLBACK TEMPLATES (statiques) ⭐ NOUVEAU
  └─ LunarInterpretationTemplate : 1728 templates migrés depuis V1
     Utilisation: Fallback si génération Claude échoue
```

### Hiérarchie de Génération

1. **LunarInterpretation** (DB temporelle) → Cache hit ⚡
2. **Claude Opus 4.5** (génération) → Temps réel 🤖
3. **LunarInterpretationTemplate** (DB statique) → Fallback 1 📚
4. **Templates hardcodés** (code) → Fallback 2 💾

---

## 📋 Décisions Architecturales

- **RLS Supabase désactivé** (commit e3531c8) : Auth JWT FastAPI only
- **user_id uniformisé INTEGER** partout (commit 4acca51)
- **Cache application 1h** pour interprétations (commit 24e06a6)
- **Lunar V1 (dépréciée)** : `pregenerated_lunar_interpretations` → MIGRÉE vers V2
- **Lunar V2 (actuelle)** : LunarInterpretation (temporelle) + LunarInterpretationTemplate (fallback)
  - Génération à la volée via Claude Opus 4.5
  - Hiérarchie fallback : DB temporelle → Claude → DB templates → hardcoded
  - Versionning complet (input_json + model_used)
  - Idempotence garantie (UNIQUE constraints)

---

## 📚 Documentation Technique Associée

- **LUNAR_ARCHITECTURE_V2.md** : Architecture V2 détaillée (4 couches)
- **MIGRATION_PLAN.md** : Plan migration V1→V2 (5 sprints)
- **API_LUNAR_V2.md** : Documentation API utilisateur V2
- **PROMETHEUS_METRICS.md** : Monitoring production (6 métriques + 12 alertes)
- **DEPLOYMENT_PRODUCTION.md** : Guide déploiement production
- **AB_TESTING_GUIDE.md** : Méthodologie A/B testing Opus vs Sonnet

---

**Dernière mise à jour** : 2026-01-24
