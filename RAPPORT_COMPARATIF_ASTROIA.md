# 📊 Rapport Comparatif : astroia-lunar vs Astro-IA

**Date :** 2025-01-XX  
**Objectif :** Inventaire complet des fonctionnalités produit et synthèse comparative pour décision de consolidation

---

## 🎯 Executive Summary

**astroia-lunar** est un monorepo FastAPI + Expo centré sur les **révolutions lunaires** avec architecture backend autonome (PostgreSQL, JWT). **Astro-IA (astroia-app)** est une app React Native complète avec Supabase (BaaS), orientée **cycles menstruels + astrologie + IA conversationnelle**. Les deux repos partagent des fonctionnalités astrologiques de base (thème natal, compatibilité) mais divergent sur l'architecture, les services externes (RapidAPI vs éphemeris-api) et les innovations produit (révolutions lunaires vs cycle menstruel + IA).

**Recommandation initiale :** Conserver astroia-lunar comme base backend pour sa modularité FastAPI, et intégrer les fonctionnalités uniques d'Astro-IA (cycle menstruel, IA, compatibilité parent-enfant ML) en tant que nouvelles routes/screens.

---

## 1️⃣ Inventaire des Fonctionnalités par Repo

### Table des Features

| Feature | Repo | Description | Emplacement Code | État | Dépendances | Notes |
|---------|------|-------------|------------------|------|-------------|-------|
| **AUTHENTIFICATION** |
| Auth JWT | astroia-lunar | Inscription/connexion avec tokens JWT | `apps/api/routes/auth.py` | ✅ Done | python-jose, bcrypt | Backend autonome |
| Auth Supabase Magic Link | Astro-IA | Auth via Supabase avec Magic Link | `app/(auth)/login.js`, Supabase Auth | ✅ Done | Supabase Client | BaaS, email OTP |
| Profil utilisateur | Les deux | Stockage données utilisateur + naissance | `models/user.py` (lunar) / `supabase-schema.sql` (astro-ia) | ✅ Done | DB native | Formats différents (Integer ID vs UUID) |
| **THÈME NATAL** |
| Calcul thème natal | astroia-lunar | Via RapidAPI (Best Astrology API) | `routes/natal.py`, `services/natal_reading_service.py` | ✅ Done | RapidAPI | 10 planètes + aspects + maisons |
| Calcul thème natal | Astro-IA | Via ephemeris-api (Clojure) | `lib/api/natalService.js`, `lib/api/natalServiceRapidAPI.js` | ✅ Done | ephemeris-api (legacy) / RapidAPI (nouveau) | Double implémentation |
| Visualisation carte du ciel | Astro-IA | Affichage graphique du thème | `app/natal-chart/index.js` | ✅ Done | React Native | Unique à Astro-IA |
| Interprétation natal | astroia-lunar | Génération interprétations textuelles | `routes/natal_interpretation.py`, `routes/natal_reading.py` | ✅ Done | RapidAPI | Système de cache par clé |
| Reading natal complet | Astro-IA | Lecture astrologique détaillée | `app/natal-reading/` | ✅ Done | Services API | UI dédiée avec sections |
| **RÉVOLUTIONS LUNAIRES** |
| Génération 12 révolutions | astroia-lunar | Calcul automatique 12 mois de révolutions | `routes/lunar_returns.py` | ✅ Done | RapidAPI, Swiss Ephemeris | Génération rolling, calcul ascendant lunaire |
| Affichage timeline | astroia-lunar | Timeline des révolutions lunaires | `app/lunar-returns/timeline.tsx` | ✅ Done | Expo Router | Vue chronologique |
| Rapport lunaire mensuel | astroia-lunar | Rapport détaillé par mois (Luna Pack) | `routes/lunar.py`, `routes/reports.py` | ✅ Done | RapidAPI | Génération HTML possible |
| **LUNA PACK (P1)** |
| Lunar Return Report | astroia-lunar | Rapport mensuel complet révolution lunaire | `routes/lunar.py` | ✅ Done | RapidAPI | Stockage JSONB, historique |
| Void of Course (VoC) | astroia-lunar | Détection fenêtres VoC en temps réel | `routes/lunar.py`, `app/lunar/voc.tsx` | ✅ Done | Swiss Ephemeris, cache | Alertes, refresh auto 5min |
| Lunar Mansions (28) | astroia-lunar | Système 28 mansions lunaires quotidiennes | `routes/lunar.py` | ✅ Done | Calculs natifs | Cache quotidien, historique |
| **TRANSITS** |
| Transits natals | astroia-lunar | Transits planétaires sur thème natal | `routes/transits.py` | ✅ Done | RapidAPI | Vue overview + détails |
| Transits sur révolutions | astroia-lunar | Transits croisés avec révolutions lunaires | `routes/transits.py` | ✅ Done | RapidAPI | Stockage en DB avec UUID |
| Vue overview transits | astroia-lunar | Badge énergie + insights clés | `app/transits/overview.tsx` | ✅ Done | Expo Router | Badges colorés par aspect |
| Détails aspect | astroia-lunar | Visualisation aspect spécifique | `app/transits/details.tsx` | ✅ Done | Expo Router | Interprétation détaillée |
| **CALENDRIER LUNAIRE** |
| Phases lunaires | astroia-lunar | Dates exactes phases (nouvelle, pleine, quartiers) | `routes/calendar.py` | ✅ Done | Swiss Ephemeris | Période personnalisable |
| Événements lunaires | astroia-lunar | Éclipses, super lunes, etc. | `routes/calendar.py` | ✅ Done | Calculs natifs | Liste événements |
| Calendrier annuel | astroia-lunar | Vue complète année avec phases + événements | `routes/calendar.py` | ✅ Done | Swiss Ephemeris | Génération complète |
| Calendrier mensuel | astroia-lunar | Vue mois avec événements + phases | `app/calendar/month.tsx` | ✅ Done | Expo Router | Navigation mois |
| **COMPATIBILITÉ ASTROLOGIQUE** |
| Compatibilité couple | Astro-IA | Analyse compatibilité amoureuse | `app/compatibility/index.js`, `lib/api/compatibilityService.js` | ✅ Done | Supabase, calculs natifs | Scores détaillés (communication, passion, etc.) |
| Compatibilité amis | Astro-IA | Analyse relation amicale | `app/compatibility/index.js` | ✅ Done | Supabase | Même base que couple |
| Compatibilité collègues | Astro-IA | Analyse relation professionnelle | `app/compatibility/index.js` | ✅ Done | Supabase | Algorithme adapté |
| **PARENT-ENFANT ML** |
| Analyse parent-enfant | Astro-IA | ML XGBoost (98.19% accuracy) | `app/parent-child/`, `lib/api/parentChildService.js` | ✅ Done | XGBoost, Python backend | Innovation unique, 6 planètes |
| **CYCLE MENSTRUEL** |
| Tracking cycle | Astro-IA | 4 phases (Menstruelle, Folliculaire, Ovulation, Lutéale) | `app/cycle-astro/index.js`, `app/my-cycles/` | ✅ Done | Supabase | Innovation produit unique |
| Corrélation cycle + astro | Astro-IA | Cycle + transits lunaires + thème natal | `lib/api/cycleAstroService.js` | ✅ Done | Supabase | Calcul énergie cosmique |
| Recommandations wellness | Astro-IA | Activités/nutrition selon phase + transit | `app/cycle-astro/` | ✅ Done | Logique métier | Badges activités |
| Mood tracking cycle | Astro-IA | 6 humeurs (Énergique, Calme, Créative, etc.) | `app/cycle-astro/` | ✅ Done | Supabase | Intégré au cycle |
| **JOURNAL & TRACKING** |
| Journal d'humeur | Astro-IA | Entrées journalières avec mood + notes + tags | `app/journal/`, `lib/api/journalService.js` | ✅ Done | Supabase | Historique complet |
| **IA CONVERSATIONNELLE** |
| Chat IA | Astro-IA | GPT-3.5-turbo avec contexte astrologique | `app/(tabs)/chat.js`, `lib/api/aiChatService.js` | ✅ Done | OpenAI, Vercel API Proxy | System prompts personnalisés |
| Horoscope quotidien IA | Astro-IA | Génération horoscope quotidien par IA | `app/horoscope/`, `lib/api/horoscopeService.js` | ✅ Done | OpenAI, cache Supabase | Personnalisé selon profil |
| **DASHBOARD & GAMIFICATION** |
| Dashboard stats | Astro-IA | Stats analyses, badges, streaks | `app/dashboard/` | ✅ Done | Supabase | Vue centralisée |
| Système badges | Astro-IA | Badges débloqués (explorateur, compatibilité, etc.) | `app/dashboard/` | ✅ Done | Logique métier | Gamification |
| Streaks | Astro-IA | Séries de jours consécutifs | `app/dashboard/` | ✅ Done | Calculs | Rétention |
| Historique analyses | Astro-IA | Liste complète analyses filtrable | `app/dashboard/` | ✅ Done | Supabase | Filtres par type |
| **ONBOARDING** |
| Onboarding complet | astroia-lunar | Flow multi-étapes (profil, cycle, consent) | `app/onboarding/` | ✅ Done | Expo Router | 5 écrans |
| Onboarding complet | Astro-IA | Flow similaire + tour guidé | `app/onboarding/` | ✅ Done | Expo Router | 6 écrans (index, profile-setup, consent, cycle-setup, tour, disclaimer) |
| **SETTINGS & UX** |
| Settings | astroia-lunar | Notifications VoC, ville par défaut, version | `app/settings/index.tsx` | ✅ Done | AsyncStorage | Paramètres basiques |
| Settings | Astro-IA | Settings complets (privacy, data policy, cycle, etc.) | `app/settings/` | ✅ Done | Supabase | 6 sous-pages |
| Design system | astroia-lunar | Thème violet/or/noir mystique | `constants/theme.ts` | ✅ Done | Expo Linear Gradient | Palette cohérente |
| Design system | Astro-IA | Thème violet/rose/lavande féminin | `constants/theme.js`, `theme/` | ✅ Done | Expo Linear Gradient | Palette différenciée |
| **INFRASTRUCTURE** |
| Base de données | astroia-lunar | PostgreSQL 16 avec Alembic migrations | `apps/api/database.py`, `alembic/` | ✅ Done | PostgreSQL, SQLAlchemy | Backend autonome |
| Base de données | Astro-IA | Supabase (PostgreSQL avec RLS) | `supabase-schema.sql` | ✅ Done | Supabase | BaaS, RLS policies |
| API REST | astroia-lunar | FastAPI avec Swagger docs | `apps/api/main.py` | ✅ Done | FastAPI, Uvicorn | OpenAPI complet |
| API Proxy | Astro-IA | Vercel serverless pour OpenAI | `astro-ia-api/` (probablement) | ✅ Done | Vercel, Edge Runtime | Sécurisation clés |
| Cache | astroia-lunar | Cache in-memory (VoC, Mansions) | `services/` | ✅ Done | Python dict | TTL 5min |
| Cache | Astro-IA | AsyncStorage + Supabase cache | `lib/api/` | ✅ Done | AsyncStorage | Cache local + cloud |

---

## 2️⃣ Map des Écrans par Repo

### astroia-lunar (Expo Router)

```
app/
├── index.tsx                    # Accueil (grille 12 mois lunaires + daily climate)
├── welcome.tsx                  # Écran de bienvenue
├── login.tsx                    # Connexion
├── onboarding/
│   ├── _layout.tsx              # Layout onboarding
│   ├── index.tsx                # Début onboarding
│   ├── profile-setup.tsx        # Setup profil (nom, date/heure/lieu naissance)
│   ├── cycle-setup.tsx          # Setup cycle menstruel (optionnel)
│   ├── consent.tsx              # Consentement données
│   └── disclaimer.tsx           # Disclaimer médical
├── lunar/
│   ├── index.tsx                # Luna Pack hub (test 3 features)
│   ├── report.tsx               # Rapport lunaire détaillé
│   └── voc.tsx                  # Void of Course en temps réel
├── lunar-month/
│   └── [month].tsx              # Détail révolution lunaire par mois
├── lunar-returns/
│   └── timeline.tsx             # Timeline des révolutions
├── transits/
│   ├── overview.tsx             # Vue d'ensemble transits
│   └── details.tsx              # Détails aspect transit
├── calendar/
│   └── month.tsx                # Calendrier mensuel (phases + événements)
├── natal-chart/
│   ├── index.tsx                # Calcul/sélection thème natal
│   └── result.tsx               # Résultat thème natal
├── cycle/
│   ├── index.tsx                # Tracking cycle menstruel
│   └── history.tsx              # Historique cycles
├── settings/
│   └── index.tsx                # Paramètres app
└── debug/
    └── selftest.tsx             # Tests développement
```

**Total : ~18 écrans**

### Astro-IA (Expo Router)

```
app/
├── index.js                     # Point d'entrée (routing conditionnel)
├── (auth)/
│   ├── _layout.js               # Layout auth
│   ├── login.js                 # Connexion Magic Link
│   ├── signup.js                # Inscription
│   └── verify-otp.js            # Vérification OTP
├── (tabs)/
│   ├── _layout.js               # Layout tabs navigation
│   ├── home.tsx                 # Accueil (CTA analyses)
│   ├── chat.js                  # Chat IA conversationnel
│   ├── profile.js               # Profil astral
│   └── lunar-month.js           # Vue mois lunaire
├── onboarding/
│   ├── _layout.js               # Layout onboarding
│   ├── index.js                 # Début onboarding
│   ├── profile-setup.js         # Setup profil
│   ├── consent.js               # Consentement
│   ├── cycle-setup.js           # Setup cycle
│   ├── tour.js                  # Tour guidé (unique à Astro-IA)
│   └── disclaimer.js            # Disclaimer
├── choose-analysis/
│   └── index.js                 # Sélection type d'analyse
├── compatibility/
│   └── index.js                 # Compatibilité (couple/amis/collègues)
├── parent-child/
│   └── index.js                 # Analyse parent-enfant ML
├── cycle-astro/
│   └── index.js                 # Cycle menstruel + astrologie
├── natal-chart/
│   └── index.js                 # Thème natal avec visualisation
├── natal-reading/
│   ├── _layout.js               # Layout reading
│   ├── setup.js                 # Setup reading
│   └── index.jsx                # Reading complet
├── horoscope/
│   └── index.js                 # Horoscope quotidien IA
├── journal/
│   ├── index.tsx                # Liste entrées journal
│   └── new.js                   # Nouvelle entrée
├── dashboard/
│   └── index.js                 # Dashboard stats + badges + historique
├── settings/
│   ├── index.js                 # Settings principal
│   ├── cycle.js                 # Settings cycle
│   ├── privacy.js               # Privacy policy
│   ├── data-policy.js           # Data policy
│   ├── disclaimer.js            # Disclaimer
│   └── about.js                 # À propos
├── calendar/
│   └── index.tsx                # Calendrier (probablement phases)
├── lunar-revolution/
│   ├── index.tsx                # Vue révolutions lunaires
│   └── [month].tsx              # Détail mois
├── my-cycles/
│   └── index.tsx                # Mes cycles (historique)
└── profile/
    └── summary.js               # Résumé profil
```

**Total : ~30 écrans**

---

## 3️⃣ Map des Endpoints API par Repo

### astroia-lunar (FastAPI)

```
/api/auth/
├── POST /register                # Inscription
├── POST /login                   # Connexion
└── GET /me                       # Profil utilisateur

/api/
├── POST /natal-chart             # Calculer thème natal (avec sauvegarde)
├── GET /natal-chart              # Récupérer thème natal
└── POST /natal-chart/external    # Pass-through RapidAPI

/api/natal/
├── POST /reading                 # Générer reading natal complet
├── GET /reading/{cache_key}      # Récupérer reading (cache)
├── DELETE /reading/{cache_key}   # Supprimer reading
├── POST /interpretation          # Générer interprétation
└── DELETE /interpretation/{chart_id}/{subject}  # Supprimer interprétation

/api/lunar-returns/
├── POST /generate                # Générer 12 révolutions lunaires
├── GET /                         # Liste révolutions
├── GET /next                     # Prochaine révolution
├── GET /rolling                  # Génération rolling (auto-next)
├── GET /year/{year}              # Révolutions d'une année
└── GET /{month}                  # Détail par mois

/api/lunar/ (Luna Pack)
├── GET /current                  # Position Lune actuelle
├── GET /daily-climate            # Climat lunaire du jour
├── POST /return/report           # Générer rapport mensuel
├── GET /return/report/history/{user_id}  # Historique rapports
├── POST /voc                     # Calculer Void of Course
├── GET /voc/current              # VoC actuel (cache)
├── GET /voc/next_window          # Prochaine fenêtre VoC
├── POST /mansion                 # Calculer mansion lunaire
└── GET /mansion/today            # Mansion du jour (cache)

/api/transits/
├── POST /natal                   # Transits sur thème natal
├── POST /lunar_return            # Transits sur révolution lunaire
├── GET /overview/{user_id}/{month}  # Vue d'ensemble transits
└── GET /overview/{user_id}       # Liste overviews

/api/calendar/
├── POST /phases                  # Phases lunaires (période)
├── POST /events                  # Événements lunaires
├── POST /year                    # Calendrier annuel
└── GET /month                    # Calendrier mensuel

/api/reports/
├── POST /lunar/{user_id}/{month}  # Générer rapport mensuel
└── GET /lunar/{user_id}/{month}/html  # Rapport HTML

/ (système)
├── GET /                         # Health check
└── GET /health                   # Status API
```

**Total : ~30 endpoints**

### Astro-IA (Supabase + Vercel)

**Supabase (PostgreSQL avec RLS) :**
- Tables accessibles via client Supabase avec RLS
- Pas d'endpoints REST explicites (client SDK)

**Vercel API Proxy :**
```
/api/ai/
├── POST /chat                    # Chat GPT-3.5-turbo
└── POST /horoscope               # Horoscope quotidien IA
```

**Services client (lib/api/) :**
- `profileService.js` - Profil utilisateur
- `natalService.js` - Thème natal
- `compatibilityService.js` - Compatibilité
- `parentChildService.js` - Parent-enfant ML
- `cycleAstroService.js` - Cycle + astro
- `journalService.js` - Journal
- `horoscopeService.js` - Horoscope
- `aiChatService.js` - Chat IA
- `dashboardService.js` - Dashboard

**Total : ~10 services (pas d'API REST structurée)**

---

## 4️⃣ Map DB / Tables Principales par Repo

### astroia-lunar (PostgreSQL avec SQLAlchemy)

```sql
-- Table utilisateurs
users (
  id INTEGER PRIMARY KEY,
  email TEXT UNIQUE,
  hashed_password TEXT,
  birth_date, birth_time, birth_latitude, birth_longitude,
  birth_place_name, birth_timezone,
  is_active, is_premium BOOLEAN,
  created_at, updated_at TIMESTAMPTZ
)

-- Thème natal
natal_charts (
  id UUID PRIMARY KEY,
  user_id INTEGER FK → users.id,
  birth_date DATE, birth_time TIME,
  birth_place TEXT, latitude NUMERIC, longitude NUMERIC, timezone TEXT,
  positions JSONB,  -- Toutes données astrologiques
  computed_at, created_at, updated_at TIMESTAMPTZ,
  version TEXT
)

-- Interprétations natal
natal_interpretations (
  id INTEGER PRIMARY KEY,
  chart_id UUID FK → natal_charts.id,
  subject TEXT,  -- "big_three", "houses", "aspects", etc.
  interpretation TEXT,
  created_at TIMESTAMPTZ
)

-- Readings natal (cache)
natal_readings_cache (
  cache_key TEXT PRIMARY KEY,
  user_id INTEGER,
  chart_id UUID,
  reading JSONB,
  expires_at TIMESTAMPTZ
)

-- Révolutions lunaires
lunar_returns (
  id INTEGER PRIMARY KEY,
  user_id INTEGER FK → users.id,
  month TEXT,  -- YYYY-MM (legacy)
  return_date TIMESTAMPTZ,  -- Date exacte révolution
  lunar_ascendant TEXT, moon_house INTEGER, moon_sign TEXT,
  aspects, planets, houses JSON,
  interpretation TEXT,
  raw_data JSON,
  calculated_at TIMESTAMPTZ
)

-- Luna Pack
lunar_reports (
  id INTEGER PRIMARY KEY,
  user_id INTEGER FK → users.id,
  month TEXT,  -- YYYY-MM
  report JSONB,
  created_at TIMESTAMPTZ
)

lunar_voc_windows (
  id INTEGER PRIMARY KEY,
  start_at, end_at TIMESTAMPTZ,
  source JSONB,
  created_at TIMESTAMPTZ
)

lunar_mansions_daily (
  id INTEGER PRIMARY KEY,
  date DATE UNIQUE,
  mansion_id INTEGER,  -- 1-28
  data JSONB,
  created_at TIMESTAMPTZ
)

-- Transits
transits_overview (
  id INTEGER PRIMARY KEY,
  user_id UUID,  -- Pointe vers auth.users.id (Supabase) !
  month TEXT,  -- YYYY-MM
  overview JSONB,
  created_at, updated_at TIMESTAMPTZ
)

transits_events (
  id INTEGER PRIMARY KEY,
  user_id UUID,  -- Pointe vers auth.users.id (Supabase) !
  date DATE,
  transit_planet TEXT, natal_point TEXT, aspect_type TEXT,
  orb INTEGER,  -- * 100
  interpretation TEXT,
  raw_data JSONB,
  created_at TIMESTAMPTZ
)

-- Calendrier
lunar_phases (
  id INTEGER PRIMARY KEY,
  date TIMESTAMPTZ,
  phase_type TEXT,  -- "new_moon", "full_moon", etc.
  data JSONB,
  created_at TIMESTAMPTZ
)

lunar_events (
  id INTEGER PRIMARY KEY,
  date TIMESTAMPTZ,
  event_type TEXT,  -- "eclipse", "super_moon", etc.
  data JSONB,
  created_at TIMESTAMPTZ
)
```

**Total : ~13 tables**

### Astro-IA (Supabase PostgreSQL avec RLS)

```sql
-- Profils utilisateurs
profiles (
  id UUID PRIMARY KEY FK → auth.users.id,
  email TEXT UNIQUE,
  name TEXT,
  birth_date TIMESTAMPTZ,
  birth_time TIME,
  birth_place TEXT,
  zodiac_sign TEXT,
  zodiac_element TEXT,
  zodiac_emoji TEXT,
  sun_sign, moon_sign, ascendant TEXT,
  sun_degree, moon_degree, asc_degree NUMERIC,
  created_at, updated_at TIMESTAMPTZ
)

-- Journal d'humeur
journal_entries (
  id UUID PRIMARY KEY,
  user_id UUID FK → auth.users.id,
  mood TEXT CHECK (mood IN ('amazing', 'happy', 'neutral', 'sad', 'anxious')),
  note TEXT,
  tags TEXT[],
  moon_phase TEXT,
  created_at, updated_at TIMESTAMPTZ
)

-- Conversations IA
chat_conversations (
  id UUID PRIMARY KEY,
  user_id UUID FK → auth.users.id,
  title TEXT,
  created_at, updated_at TIMESTAMPTZ
)

chat_messages (
  id UUID PRIMARY KEY,
  conversation_id UUID FK → chat_conversations.id,
  user_id UUID FK → auth.users.id,
  role TEXT CHECK (role IN ('user', 'assistant')),
  content TEXT,
  created_at TIMESTAMPTZ
)

-- Compatibilité
compatibility_analyses (
  id UUID PRIMARY KEY,
  user_id UUID FK → auth.users.id,
  relation_type TEXT,  -- 'couple', 'friends', 'colleagues'
  person1_data, person2_data JSONB,
  global_score INTEGER,
  detailed_scores JSONB,  -- {communication, passion, etc.}
  recommendations JSONB,
  created_at TIMESTAMPTZ
)

compatibility_history (
  id UUID PRIMARY KEY,
  user_id UUID FK → auth.users.id,
  type TEXT,  -- 'parent-child', 'cycle-astro'
  person1_data, person2_data JSONB,
  compatibility_score INTEGER,
  interpretation JSONB,
  created_at TIMESTAMPTZ
)

-- Thèmes nataux
natal_charts (
  id UUID PRIMARY KEY,
  user_id UUID FK → auth.users.id,
  chart_data JSONB,
  interpretations JSONB,
  created_at TIMESTAMPTZ
)

-- Horoscopes quotidiens
daily_horoscopes (
  id UUID PRIMARY KEY,
  user_id UUID FK → auth.users.id,
  date DATE,
  content TEXT,
  recommendations TEXT[],
  created_at TIMESTAMPTZ
)
```

**Total : ~8 tables principales**

---

## 5️⃣ Doublons & Risques Techniques

### ✅ Fonctionnalités Présentes dans les 2 Repos

| Feature | astroia-lunar | Astro-IA | Divergences |
|---------|---------------|----------|-------------|
| **Thème natal** | ✅ RapidAPI | ✅ ephemeris-api + RapidAPI | Lunar: API unique. Astro-IA: double impl (legacy + nouveau) |
| **Onboarding** | ✅ 5 écrans | ✅ 6 écrans | Lunar: plus simple. Astro-IA: tour guidé en plus |
| **Settings** | ✅ Basique | ✅ Complet | Lunar: VoC, ville. Astro-IA: 6 sous-pages (privacy, data, etc.) |
| **Auth** | ✅ JWT backend | ✅ Supabase Magic Link | Lunar: autonome. Astro-IA: BaaS |
| **Profil utilisateur** | ✅ Table users | ✅ Table profiles | Lunar: Integer ID. Astro-IA: UUID (Supabase) |

### 🟡 Fonctionnalités Uniques à un Repo

**Uniques à astroia-lunar :**
- ✅ Révolutions lunaires (12 mois automatiques)
- ✅ Luna Pack complet (Rapports, VoC, Mansions)
- ✅ Transits natals + sur révolutions
- ✅ Calendrier lunaire (phases + événements)
- ✅ Interprétations natal structurées
- ✅ Architecture backend FastAPI modulaire

**Uniques à Astro-IA :**
- ✅ Cycle menstruel + corrélation astrologique
- ✅ IA conversationnelle (GPT-3.5)
- ✅ Horoscope quotidien IA
- ✅ Compatibilité astrologique (couple/amis/collègues)
- ✅ Parent-enfant ML (XGBoost)
- ✅ Journal d'humeur
- ✅ Dashboard + gamification (badges, streaks)
- ✅ Visualisation carte du ciel

### 🔴 Risques Techniques Majeurs

1. **Incompatibilité UUID vs Integer ID**
   - **Problème :** astroia-lunar utilise `users.id INTEGER`, Astro-IA utilise `auth.users.id UUID`
   - **Impact :** Transits dans lunar pointent vers UUID Supabase (hybride !)
   - **Solution :** Unifier sur UUID ou créer mapping table

2. **Double dépendance RapidAPI**
   - **Problème :** Les deux repos appellent RapidAPI pour natal
   - **Impact :** Coûts doublés, clés API séparées
   - **Solution :** Centraliser dans backend unique

3. **Architecture divergente**
   - **Problème :** Lunar = backend autonome FastAPI, Astro-IA = BaaS Supabase
   - **Impact :** Migration complexe si consolidation
   - **Solution :** Conserver FastAPI, migrer Supabase vers client API

4. **Services externes multiples**
   - **Problème :** Lunar = RapidAPI + Swiss Ephemeris, Astro-IA = ephemeris-api (legacy) + OpenAI
   - **Impact :** Maintenance multiple
   - **Solution :** Standardiser sur RapidAPI + OpenAI via proxy

5. **États partiels / POC**
   - **Problème :** Certaines features peuvent être non finalisées
   - **Impact :** Bugs cachés, incompatibilités
   - **Solution :** Audit fonctionnel complet avant consolidation

---

## 6️⃣ Recommandations : Feature Set Cible

### 🎯 MVP (4-7 features max)

**Objectif :** Valider marché avec produit minimal viable, focus sur innovation différenciante.

| Feature | Repo Source | Justification | Effort | Risque |
|---------|-------------|---------------|--------|--------|
| 1. Auth JWT | astroia-lunar | Backend autonome, plus simple que Supabase Magic Link | Faible | Faible |
| 2. Thème natal | astroia-lunar | RapidAPI unifié, meilleure implémentation | Moyen | Faible |
| 3. Cycle menstruel + astro | Astro-IA | **Innovation unique**, différenciation marché | Moyen | Moyen |
| 4. Révolutions lunaires (12 mois) | astroia-lunar | Core feature du produit "lunar" | Moyen | Faible |
| 5. Luna Pack : VoC | astroia-lunar | Feature différenciante, temps réel | Faible | Faible |
| 6. Dashboard basique | Astro-IA | Rétention, visualisation données | Faible | Faible |
| 7. Onboarding simplifié | astroia-lunar | 5 écrans suffisants pour MVP | Faible | Faible |

**Dépendances MVP :**
- PostgreSQL + FastAPI backend (astroia-lunar)
- RapidAPI (thème natal)
- Swiss Ephemeris (VoC, phases)
- Expo mobile app

**Rejet MVP :**
- ❌ IA conversationnelle (coût OpenAI élevé, complexité)
- ❌ Compatibilité (peut attendre V1)
- ❌ Parent-enfant ML (complexité backend Python)
- ❌ Journal (nice-to-have)
- ❌ Calendrier complet (MVP = phases basiques)
- ❌ Transits (complexité, peut attendre V1)

---

### 🚀 V1 (7-12 features)

**Objectif :** Produit complet avec toutes les fonctionnalités core astrologiques.

| Feature | Repo Source | Justification | Effort | Risque |
|---------|-------------|---------------|--------|--------|
| **MVP +** |
| 8. Luna Pack : Lunar Mansions | astroia-lunar | Complète le Luna Pack, valeur ajoutée | Faible | Faible |
| 9. Transits natals | astroia-lunar | Feature core astrologie, demandée | Moyen | Moyen |
| 10. Calendrier lunaire | astroia-lunar | Phases + événements, valeur UX | Moyen | Faible |
| 11. Compatibilité couple | Astro-IA | Feature populaire, algorithmes OK | Moyen | Faible |
| 12. Journal d'humeur | Astro-IA | Tracking quotidien, rétention | Faible | Faible |
| 13. Visualisation carte du ciel | Astro-IA | UX améliorée pour natal | Moyen | Faible |
| 14. Settings complets | Astro-IA | Privacy, data policy, cycle | Faible | Faible |

**Rejet V1 :**
- ❌ IA conversationnelle (coût, complexité, peut attendre V2 si demandé)
- ❌ Parent-enfant ML (complexité backend, niche)
- ❌ Compatibilité amis/collègues (prioriser couple)
- ❌ Horoscope IA (coût OpenAI)
- ❌ Dashboard gamification avancée (badges, streaks → V2)
- ❌ Transits sur révolutions (complexité, V2)

---

### 🌟 V2 (Le reste + nouvelles)

**Objectif :** Features avancées, différenciation premium, monétisation.

| Feature | Repo Source | Justification | Effort | Risque |
|---------|-------------|---------------|--------|--------|
| **V1 +** |
| 15. IA conversationnelle | Astro-IA | Différenciation premium, monétisation | Élevé | Élevé (coût) |
| 16. Horoscope quotidien IA | Astro-IA | Engagement quotidien | Moyen | Moyen (coût) |
| 17. Parent-enfant ML | Astro-IA | Innovation unique, premium | Élevé | Élevé (backend Python) |
| 18. Compatibilité amis/collègues | Astro-IA | Extension compatibilité | Faible | Faible |
| 19. Transits sur révolutions | astroia-lunar | Feature avancée | Moyen | Moyen |
| 20. Dashboard gamification | Astro-IA | Badges, streaks, rétention | Moyen | Faible |
| 21. Luna Pack : Rapports HTML | astroia-lunar | Export, partage | Faible | Faible |
| 22. Calendrier annuel complet | astroia-lunar | Vue long terme | Faible | Faible |

**Nouvelles features V2 (à développer) :**
- Notifications push (VoC, phases importantes)
- Export PDF (rapports, thème natal)
- Partage social (thème natal, compatibilité)
- Mode premium (toutes features avancées)
- Multilingue (i18n)

---

## 7️⃣ Roadmap Technique Proposée

### Phase 1 : Consolidation Backend (Semaines 1-2)
1. ✅ Conserver FastAPI (astroia-lunar) comme backend principal
2. ✅ Migrer auth Supabase → JWT (si nécessaire, sinon garder Supabase Auth)
3. ✅ Unifier modèle User (UUID ou Integer ? Décision requise)
4. ✅ Centraliser appels RapidAPI dans service unique
5. ✅ Créer endpoint cycle menstruel (nouveau, basé sur Astro-IA)

### Phase 2 : MVP Mobile (Semaines 3-4)
1. ✅ Base app Expo (astroia-lunar)
2. ✅ Intégrer écrans cycle menstruel (depuis Astro-IA)
3. ✅ Intégrer dashboard basique (depuis Astro-IA)
4. ✅ Unifier design system (palette hybride ?)
5. ✅ Tests E2E MVP

### Phase 3 : V1 (Semaines 5-8)
1. ✅ Ajouter transits natals
2. ✅ Ajouter calendrier lunaire
3. ✅ Ajouter compatibilité couple
4. ✅ Ajouter journal d'humeur
5. ✅ Finaliser UX/UI
6. ✅ Tests complets

### Phase 4 : V2 (Semaines 9-12+)
1. ✅ Évaluer ROI IA conversationnelle (coûts vs valeur)
2. ✅ Si ROI positif : intégrer chat IA + horoscope IA
3. ✅ Évaluer besoin parent-enfant ML (backend Python séparé ?)
4. ✅ Gamification avancée
5. ✅ Features premium

---

## 8️⃣ Décisions Techniques Critiques

### ❓ Questions Ouvertes (Réponse requise)

1. **UUID vs Integer ID ?**
   - Option A : Migrer astroia-lunar vers UUID (compatible Supabase)
   - Option B : Garder Integer, créer mapping table pour transits
   - **Recommandation :** Option A (UUID) pour compatibilité future

2. **Auth : JWT vs Supabase Magic Link ?**
   - Option A : Garder JWT (backend autonome)
   - Option B : Migrer vers Supabase Auth (BaaS, moins de maintenance)
   - **Recommandation :** Option B si on garde Supabase pour d'autres features, sinon Option A

3. **Design System : Palette unique ou hybride ?**
   - Option A : Palette mystique (violet/or) de lunar
   - Option B : Palette féminine (rose/lavande) d'Astro-IA
   - Option C : Hybride (violet/rose)
   - **Recommandation :** Option C (hybride) pour différenciation

4. **Architecture Backend : FastAPI pur vs Hybride FastAPI + Supabase ?**
   - Option A : FastAPI pur (tout migré)
   - Option B : Hybride (FastAPI pour astro, Supabase pour auth/DB simple)
   - **Recommandation :** Option A (FastAPI pur) pour simplicité

5. **Services Externes : Standardiser sur quoi ?**
   - RapidAPI : ✅ Garder (thème natal, transits)
   - Swiss Ephemeris : ✅ Garder (VoC, phases)
   - OpenAI : ❓ V2 uniquement si ROI positif
   - ephemeris-api (legacy) : ❌ Abandonner

---

## 9️⃣ Résumé des Métriques

### Lignes de Code (Estimation)

| Repo | Backend | Frontend | Total |
|------|---------|----------|-------|
| astroia-lunar | ~15,000 | ~10,000 | ~25,000 |
| Astro-IA | ~2,000 (Vercel) | ~15,000 | ~17,000 |
| **Total** | **~17,000** | **~25,000** | **~42,000** |

### Fonctionnalités

| Catégorie | astroia-lunar | Astro-IA | Total Unique |
|-----------|---------------|----------|--------------|
| Core Astrology | 8 | 6 | 12 |
| Luna Pack | 3 | 0 | 3 |
| Cycle & Tracking | 1 | 3 | 4 |
| IA & ML | 0 | 3 | 3 |
| UX/Infra | 5 | 6 | 10 |
| **Total** | **17** | **18** | **32** |

### Dépendances Externes

| Service | astroia-lunar | Astro-IA | Coût Estimé |
|---------|---------------|----------|-------------|
| RapidAPI | ✅ | ✅ | ~$50-200/mois |
| OpenAI GPT-3.5 | ❌ | ✅ | ~$100-500/mois (selon usage) |
| Supabase | ❌ | ✅ | Gratuit (free tier) ou ~$25/mois |
| Swiss Ephemeris | ✅ | ❌ | Gratuit (librairie) |
| PostgreSQL | ✅ (self-hosted) | ✅ (Supabase) | $0-50/mois |

---

## 🔟 Conclusion & Prochaines Étapes

### Points Forts à Conserver

✅ **astroia-lunar :**
- Architecture backend FastAPI modulaire et propre
- Luna Pack complet (innovation produit)
- Révolutions lunaires (core feature)
- Transits structurés

✅ **Astro-IA :**
- Cycle menstruel + astrologie (innovation unique)
- IA conversationnelle (différenciation premium)
- UX soignée (dashboard, visualisations)
- Gamification (rétention)

### Actions Immédiates

1. **Décision architecture :** UUID vs Integer ID ? Auth JWT vs Supabase ?
2. **Audit fonctionnel :** Tester toutes features dans les 2 repos, identifier bugs
3. **Prototype MVP :** Intégrer cycle menstruel dans astroia-lunar
4. **Roadmap détaillée :** Planifier sprints MVP/V1/V2 avec estimations
5. **Migration plan :** Documenter étapes consolidation code

### Risques à Mitiger

⚠️ **Incompatibilité UUID/Integer :** Résoudre avant consolidation  
⚠️ **Coûts OpenAI :** Évaluer ROI avant intégration V2  
⚠️ **Complexité parent-enfant ML :** Backend Python séparé ou intégré ?  
⚠️ **Double maintenance :** Éviter de garder 2 backends en parallèle trop longtemps

---

**Rapport généré le :** 2025-01-XX  
**Prochaine revue :** Après décisions techniques critiques

---

> 💡 **Note :** Ce rapport est un instantané. Des features peuvent être partiellement implémentées ou en évolution. Un audit fonctionnel manuel est recommandé avant consolidation.

