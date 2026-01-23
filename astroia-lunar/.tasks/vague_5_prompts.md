# 🌊 Vague 5 : Monitoring & Cleanup - Prompts Agents IA

**Durée totale** : 2h en parallèle (3 agents)
**Prérequis** : Vague 4 terminée (Tests E2E + Tests intégration complets)
**Objectif** : Finaliser l'observabilité, documenter l'API, et nettoyer le projet

---

## 📋 Vue d'ensemble Vague 5

| Agent | Tâche | Durée | Fichiers principaux |
|-------|-------|-------|---------------------|
| Agent A | Task 5.1 : Métriques Prometheus dashboard | 2h | `monitoring/prometheus_dashboard.json`, `docs/MONITORING.md` |
| Agent B | Task 5.2 : Documentation API utilisateur | 1h30 | `docs/API_LUNAR_V2.md` |
| Agent C | Task 5.3 + 5.4 : Cleanup + CLAUDE.md final | 45min | `.tasks/cleanup.md`, `.claude/CLAUDE.md` |

---

## 🤖 Agent A - Task 5.1 : Dashboard Métriques Prometheus (2h)

### 📊 Contexte

Tu es l'Agent A de la Vague 5. Ta mission est de créer un dashboard Prometheus/Grafana pour monitorer les métriques de génération d'interprétations lunaires V2.

**Prérequis complétés** :
- ✅ Vague 1 (2.1) : Service generator enrichi avec 5 métriques Prometheus
  - `lunar_interpretation_generated_total` : Total générations (counter)
  - `lunar_interpretation_cache_hit_total` : Cache hits (counter)
  - `lunar_interpretation_fallback_total` : Fallbacks (counter)
  - `lunar_interpretation_duration_seconds` : Durée génération (histogram)
  - `lunar_active_generations` : Générations actives (gauge)
- ✅ Routes API exposent métriques via endpoint `/metrics` (FastAPI + prometheus_client)

### 🎯 Objectif

Créer un dashboard Grafana configuré pour monitorer la santé et les performances du système V2 en production.

### 📝 Tâches principales

#### 1. Créer fichier `monitoring/prometheus_dashboard.json` (1h15)

**Structure du dashboard Grafana** :

```json
{
  "dashboard": {
    "title": "Lunar Interpretation V2 - Production Monitoring",
    "tags": ["lunar", "v2", "production"],
    "timezone": "browser",
    "panels": [
      // Panel 1: Générations par source
      // Panel 2: Taux de cache hit
      // Panel 3: Distribution fallbacks
      // Panel 4: Durée génération (P50/P95/P99)
      // Panel 5: Générations actives
      // Panel 6: Erreurs par type
    ]
  }
}
```

**Panels à créer** (6 panels minimum) :

**a) Panel 1 : Générations par source (Time Series)** :
```json
{
  "title": "Générations par source",
  "targets": [
    {
      "expr": "rate(lunar_interpretation_generated_total[5m])",
      "legendFormat": "{{source}} - {{model}}"
    }
  ],
  "description": "Nombre de générations par minute, groupées par source (claude, db_template, hardcoded)"
}
```

**b) Panel 2 : Taux de cache hit (Gauge)** :
```json
{
  "title": "Cache Hit Rate (%)",
  "targets": [
    {
      "expr": "rate(lunar_interpretation_cache_hit_total[5m]) / (rate(lunar_interpretation_cache_hit_total[5m]) + rate(lunar_interpretation_generated_total{source='claude'}[5m])) * 100"
    }
  ],
  "thresholds": {
    "mode": "absolute",
    "steps": [
      { "value": 0, "color": "red" },
      { "value": 50, "color": "yellow" },
      { "value": 80, "color": "green" }
    ]
  }
}
```

**c) Panel 3 : Distribution fallbacks (Pie Chart)** :
```json
{
  "title": "Distribution Fallbacks",
  "targets": [
    {
      "expr": "lunar_interpretation_fallback_total",
      "legendFormat": "{{fallback_level}}"
    }
  ],
  "description": "Répartition entre db_template et hardcoded fallbacks"
}
```

**d) Panel 4 : Durée génération (Heatmap)** :
```json
{
  "title": "Latence génération (P50/P95/P99)",
  "targets": [
    {
      "expr": "histogram_quantile(0.50, rate(lunar_interpretation_duration_seconds_bucket[5m]))",
      "legendFormat": "P50"
    },
    {
      "expr": "histogram_quantile(0.95, rate(lunar_interpretation_duration_seconds_bucket[5m]))",
      "legendFormat": "P95"
    },
    {
      "expr": "histogram_quantile(0.99, rate(lunar_interpretation_duration_seconds_bucket[5m]))",
      "legendFormat": "P99"
    }
  ]
}
```

**e) Panel 5 : Générations actives (Graph)** :
```json
{
  "title": "Générations actives simultanées",
  "targets": [
    {
      "expr": "lunar_active_generations",
      "legendFormat": "Active"
    }
  ],
  "alert": {
    "conditions": [
      {
        "evaluator": { "type": "gt", "params": [10] },
        "query": { "params": ["A", "5m", "now"] }
      }
    ],
    "message": "Plus de 10 générations simultanées - risque de surcharge"
  }
}
```

**f) Panel 6 : Erreurs et timeouts (Stat)** :
```json
{
  "title": "Erreurs Claude API",
  "targets": [
    {
      "expr": "rate(lunar_interpretation_generated_total{source='db_template'}[5m]) + rate(lunar_interpretation_generated_total{source='hardcoded'}[5m])",
      "legendFormat": "Fallback rate (erreurs Claude)"
    }
  ],
  "thresholds": {
    "mode": "absolute",
    "steps": [
      { "value": 0, "color": "green" },
      { "value": 0.1, "color": "yellow" },
      { "value": 0.5, "color": "red" }
    ]
  }
}
```

#### 2. Créer documentation `docs/MONITORING.md` (30min)

**Structure du document** :

```markdown
# Monitoring Lunar Interpretation V2

**Date** : 2026-01-23
**Version** : V2 (Sprint 5 Vague 5)

## 📊 Métriques Disponibles

### Métriques Production

| Métrique | Type | Labels | Description |
|----------|------|--------|-------------|
| `lunar_interpretation_generated_total` | Counter | source, model, subject, version | Total générations |
| `lunar_interpretation_cache_hit_total` | Counter | subject, version | Cache hits DB temporelle |
| `lunar_interpretation_fallback_total` | Counter | fallback_level | Fallbacks (db_template, hardcoded) |
| `lunar_interpretation_duration_seconds` | Histogram | source, subject | Durée génération (buckets: 0.05-30s) |
| `lunar_active_generations` | Gauge | - | Générations actives simultanées |

### Endpoint Métriques

```bash
# Exposition métriques Prometheus
GET http://localhost:8000/metrics

# Format : Prometheus text format
# Actualisation : Temps réel
```

## 🎯 SLOs (Service Level Objectives)

### Disponibilité
- **Target** : 99.5% uptime
- **Mesure** : Ratio requêtes réussies / total requêtes

### Performance
- **Cache hit rate** : > 80% (objectif)
- **P95 latence** :
  - Cache hit : < 100ms
  - Claude génération : < 5s
  - Template fallback : < 300ms
  - Hardcoded fallback : < 50ms

### Qualité
- **Claude usage** : > 60% des générations (via Claude, pas fallback)
- **Error rate** : < 1% (fallback = erreur Claude)

## 🚨 Alertes Recommandées

### Alert 1 : Cache hit rate faible
```yaml
alert: LunarCacheHitRateLow
expr: |
  rate(lunar_interpretation_cache_hit_total[10m]) /
  (rate(lunar_interpretation_cache_hit_total[10m]) +
   rate(lunar_interpretation_generated_total{source='claude'}[10m])) < 0.5
for: 15m
severity: warning
message: "Cache hit rate < 50% pendant 15min"
```

### Alert 2 : Fallback rate élevé
```yaml
alert: LunarFallbackRateHigh
expr: |
  rate(lunar_interpretation_fallback_total[5m]) /
  rate(lunar_interpretation_generated_total[5m]) > 0.2
for: 10m
severity: critical
message: "Fallback rate > 20% - Claude API issues"
```

### Alert 3 : Latence P95 élevée
```yaml
alert: LunarLatencyP95High
expr: |
  histogram_quantile(0.95,
    rate(lunar_interpretation_duration_seconds_bucket{source='claude'}[5m])
  ) > 10
for: 5m
severity: warning
message: "P95 latence Claude > 10s"
```

### Alert 4 : Générations simultanées élevées
```yaml
alert: LunarHighConcurrency
expr: lunar_active_generations > 20
for: 5m
severity: warning
message: "Plus de 20 générations simultanées - risque throttling Claude"
```

## 📈 Dashboard Grafana

Importer le dashboard pré-configuré :
- Fichier : `monitoring/prometheus_dashboard.json`
- Grafana ID : (à remplir après upload)

### Panels disponibles
1. **Générations par source** (Time Series)
2. **Cache hit rate** (Gauge)
3. **Distribution fallbacks** (Pie Chart)
4. **Latence génération** (Heatmap P50/P95/P99)
5. **Générations actives** (Graph)
6. **Erreurs Claude** (Stat)

## 🔍 Requêtes Utiles

### Cache hit rate sur 24h
```promql
rate(lunar_interpretation_cache_hit_total[24h]) /
(rate(lunar_interpretation_cache_hit_total[24h]) +
 rate(lunar_interpretation_generated_total{source='claude'}[24h]))
```

### Top 5 sujets générés
```promql
topk(5, rate(lunar_interpretation_generated_total[1h]))
```

### Temps moyen par source
```promql
rate(lunar_interpretation_duration_seconds_sum[5m]) /
rate(lunar_interpretation_duration_seconds_count[5m])
```

## 🛠️ Troubleshooting

### Cache hit rate < 50%
- Vérifier TTL cache (devrait être infini pour DB temporelle)
- Vérifier UNIQUE constraint (empêche doublons)
- Analyser logs : `grep "cache_hit" logs/production.log`

### Fallback rate > 10%
- Vérifier status Claude API : https://status.anthropic.com
- Vérifier ANTHROPIC_API_KEY valide
- Analyser logs : `grep "ClaudeAPIError" logs/production.log`
- Vérifier quota Claude (rate limiting)

### P95 latence > 10s
- Vérifier timeout configuré (30s max)
- Analyser retry attempts (max 3)
- Vérifier réseau (latence vers Claude API)

## 📚 Références

- Prometheus docs : https://prometheus.io/docs/
- Grafana dashboards : https://grafana.com/grafana/dashboards/
- Claude API status : https://status.anthropic.com
```

#### 3. Tests et validation (15min)

**a) Vérifier métriques exposées** :
```bash
# Lancer l'API
uvicorn main:app --reload

# Vérifier endpoint /metrics
curl http://localhost:8000/metrics | grep lunar_interpretation

# Output attendu :
# lunar_interpretation_generated_total{source="claude",model="claude-opus-4-5-20251101",...} 42.0
# lunar_interpretation_cache_hit_total{subject="full",version="2"} 128.0
# ...
```

**b) Valider format Prometheus** :
```bash
# Vérifier format Prometheus text
curl http://localhost:8000/metrics | promtool check metrics
```

**c) Tester dashboard Grafana** (optionnel si Grafana installé) :
```bash
# Importer dashboard dans Grafana
curl -X POST http://localhost:3000/api/dashboards/db \
  -H "Content-Type: application/json" \
  -d @monitoring/prometheus_dashboard.json
```

### 📦 Livrables

1. ✅ Fichier `monitoring/prometheus_dashboard.json` (6+ panels)
2. ✅ Document `docs/MONITORING.md` complet
3. ✅ Métriques validées via endpoint `/metrics`
4. ✅ Alertes recommandées documentées (4+ alertes)

### 🎯 Critères de succès

- [ ] 6+ panels Grafana créés
- [ ] Dashboard JSON valide et importable
- [ ] Documentation monitoring complète (métriques, SLOs, alertes)
- [ ] Endpoint `/metrics` accessible et conforme Prometheus
- [ ] 4+ alertes recommandées avec seuils clairs

### 📚 Références

**Fichiers à étudier** :
- `services/lunar_interpretation_generator.py` : Métriques implémentées (lignes 46-74)
- `main.py` : Exposition métriques via `/metrics` endpoint
- `requirements.txt` : prometheus-client==0.20.0

**Documentation** :
- Prometheus Python client : https://github.com/prometheus/client_python
- Grafana dashboard JSON : https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/create-dashboard/
- FastAPI + Prometheus : https://fastapi.tiangolo.com/advanced/middleware/

---

## 🤖 Agent B - Task 5.2 : Documentation API Utilisateur (1h30)

### 📊 Contexte

Tu es l'Agent B de la Vague 5. Ta mission est de créer une documentation complète de l'API Lunar Interpretation V2 pour les développeurs frontend et utilisateurs finaux.

**Prérequis complétés** :
- ✅ Vague 3 : 3 routes API complètes
  - GET `/api/lunar-returns/current/report` : Rapport lunaire avec metadata V2
  - POST `/api/lunar/interpretation/regenerate` : Force regenerate
  - GET `/api/lunar/interpretation/metadata` : Stats utilisateur
- ✅ Architecture V2 opérationnelle (4 niveaux fallback)

### 🎯 Objectif

Documenter l'API V2 de manière claire et complète pour faciliter l'intégration frontend et l'utilisation par les développeurs.

### 📝 Tâches principales

#### 1. Créer fichier `docs/API_LUNAR_V2.md` (1h)

**Structure du document** :

```markdown
# API Lunar Interpretation V2

**Version** : 2.0.0
**Date** : 2026-01-23
**Base URL** : `https://api.astroia.app` (production) | `http://localhost:8000` (dev)

## 📚 Table des matières

1. [Introduction](#introduction)
2. [Authentification](#authentification)
3. [Endpoints](#endpoints)
4. [Modèles de données](#modèles-de-données)
5. [Codes d'erreur](#codes-derreur)
6. [Exemples d'utilisation](#exemples-dutilisation)
7. [Migration V1 → V2](#migration-v1--v2)

---

## 🎯 Introduction

L'API Lunar Interpretation V2 fournit des interprétations astrologiques lunaires personnalisées, générées dynamiquement via IA (Claude Opus 4.5) avec fallback intelligent vers templates.

### Nouveautés V2

- ✨ **Génération à la volée** : Interprétations générées dynamiquement (pas de pré-génération)
- 🔄 **Fallback hiérarchique** : 4 niveaux (DB temporelle → Claude → DB templates → Hardcoded)
- 📊 **Metadata enrichies** : source, model_used, version, generated_at
- 🔁 **Force regenerate** : Endpoint dédié pour régénérer à la demande
- 📈 **Stats utilisateur** : Endpoint metadata avec stats d'utilisation

### Architecture V2

```
Layer 1: FAITS ASTRONOMIQUES (LunarReturn) - Immuables
Layer 2: NARRATION IA (LunarInterpretation) - Temporelle, régénérable
Layer 3: CACHE APPLICATION (LunarReport) - Court terme (1h)
Layer 4: FALLBACK TEMPLATES - Statiques (1728 templates)
```

---

## 🔐 Authentification

Toutes les routes V2 nécessitent un **JWT token** valide.

### Obtenir un token

```bash
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response** :
```json
{
  "access_token": "<JWT_TOKEN_HERE>",
  "token_type": "bearer"
}
```

### Utiliser le token

```bash
# Header Authorization requis
Authorization: Bearer <JWT_TOKEN_HERE>
```

---

## 📡 Endpoints

### 1. GET /api/lunar-returns/current/report

Récupère le rapport lunaire du mois en cours avec interprétation V2.

**Auth** : ✅ Requis (JWT)

**Query Parameters** :
- Aucun (utilise le thème natal de l'utilisateur authentifié)

**Response** :
```json
{
  "lunar_return": {
    "month": "2026-01",
    "return_date": "2026-01-15T14:23:45Z",
    "moon_sign": "Aries",
    "moon_house": 4,
    "lunar_ascendant": "Leo",
    "aspects": [
      {
        "first_planet": "Moon",
        "second_planet": "Sun",
        "aspect": "Trine",
        "orb": 2.5
      }
    ]
  },
  "interpretation": {
    "full": "Interprétation complète du mois...",
    "climate": "Ambiance émotionnelle...",
    "focus": "Zones de focus...",
    "approach": "Approche du mois...",
    "weekly_advice": {
      "week_1": "Conseil semaine 1...",
      "week_2": "Conseil semaine 2...",
      "week_3": "Conseil semaine 3...",
      "week_4": "Conseil semaine 4..."
    }
  },
  "metadata": {
    "source": "claude",
    "model_used": "claude-opus-4-5-20251101",
    "version": 2,
    "generated_at": "2026-01-23T10:30:00Z"
  }
}
```

**Champs metadata** :
- `source` : `"db_temporal"` (cache), `"claude"` (génération), `"db_template"` (fallback 1), `"hardcoded"` (fallback 2)
- `model_used` : Nom du modèle Claude ou `"template"` ou `"placeholder"`
- `version` : Version du prompt (2 = V2)
- `generated_at` : Timestamp de génération

**Exemples d'utilisation** :
```bash
# cURL
curl -X GET "http://localhost:8000/api/lunar-returns/current/report" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# JavaScript (fetch)
const response = await fetch('http://localhost:8000/api/lunar-returns/current/report', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
const data = await response.json();
console.log(data.metadata.source); // "claude" ou "db_temporal"
```

**Erreurs** :
- `401 Unauthorized` : Token manquant ou invalide
- `404 Not Found` : Utilisateur n'a pas de thème natal
- `503 Service Unavailable` : Tous les fallbacks ont échoué

---

### 2. POST /api/lunar/interpretation/regenerate

Force la régénération d'une interprétation (bypass cache).

**Auth** : ✅ Requis (JWT)

**Body** :
```json
{
  "lunar_return_id": 123,
  "subject": "full"
}
```

**Parameters** :
- `lunar_return_id` (integer, required) : ID de la révolution lunaire
- `subject` (string, optional) : Type d'interprétation (`"full"`, `"climate"`, `"focus"`, `"approach"`). Défaut : `"full"`

**Response** :
```json
{
  "interpretation": "Nouvelle interprétation régénérée...",
  "weekly_advice": {
    "week_1": "Nouveau conseil...",
    "week_2": "...",
    "week_3": "...",
    "week_4": "..."
  },
  "metadata": {
    "source": "claude",
    "model_used": "claude-opus-4-5-20251101",
    "subject": "full",
    "regenerated_at": "2026-01-23T11:45:00Z",
    "forced": true
  }
}
```

**Use Cases** :
1. Amélioration du prompt (nouvelle version du modèle)
2. Qualité insatisfaisante (utilisateur veut une nouvelle génération)
3. Debug/test génération Claude temps réel

**Exemples d'utilisation** :
```bash
# cURL
curl -X POST "http://localhost:8000/api/lunar/interpretation/regenerate" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"lunar_return_id": 123, "subject": "full"}'

# JavaScript (fetch)
const response = await fetch('http://localhost:8000/api/lunar/interpretation/regenerate', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    lunar_return_id: 123,
    subject: 'full'
  })
});
```

**Erreurs** :
- `401 Unauthorized` : Token manquant ou invalide
- `403 Forbidden` : Utilisateur ne possède pas ce LunarReturn
- `404 Not Found` : LunarReturn introuvable
- `422 Validation Error` : lunar_return_id manquant

---

### 3. GET /api/lunar/interpretation/metadata

Récupère les statistiques d'utilisation des interprétations pour l'utilisateur authentifié.

**Auth** : ✅ Requis (JWT)

**Query Parameters** :
- Aucun (utilise l'utilisateur authentifié)

**Response** :
```json
{
  "total_interpretations": 42,
  "models_used": [
    {
      "model": "claude-opus-4-5-20251101",
      "count": 30,
      "percentage": 71.4
    },
    {
      "model": "template",
      "count": 12,
      "percentage": 28.6
    }
  ],
  "cached_rate": 85.7,
  "last_generated": "2026-01-23T10:30:00Z",
  "cached": false
}
```

**Champs** :
- `total_interpretations` : Nombre total d'interprétations générées
- `models_used` : Répartition par modèle (Claude, template, etc.)
- `cached_rate` : Taux d'utilisation du cache (%)
- `last_generated` : Date de la dernière génération
- `cached` : `true` si réponse depuis cache applicatif (TTL 10min)

**Exemples d'utilisation** :
```bash
# cURL
curl -X GET "http://localhost:8000/api/lunar/interpretation/metadata" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# JavaScript (fetch)
const response = await fetch('http://localhost:8000/api/lunar/interpretation/metadata', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
const data = await response.json();
console.log(`Cache rate: ${data.cached_rate}%`);
```

**Erreurs** :
- `401 Unauthorized` : Token manquant ou invalide

---

## 📊 Modèles de données

### LunarInterpretation (DB)

Table : `lunar_interpretations`

```sql
CREATE TABLE lunar_interpretations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    lunar_return_id INTEGER NOT NULL REFERENCES lunar_returns(id) ON DELETE CASCADE,
    subject VARCHAR(50) NOT NULL,  -- 'full' | 'climate' | 'focus' | 'approach'
    version INTEGER NOT NULL DEFAULT 2,
    lang VARCHAR(10) NOT NULL DEFAULT 'fr',
    input_json JSONB NOT NULL,  -- Contexte complet envoyé à Claude
    output_text TEXT NOT NULL,  -- Interprétation générée
    weekly_advice JSONB,        -- Conseils hebdomadaires
    model_used VARCHAR(50),     -- 'claude-opus-4-5', 'template', etc.
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE (lunar_return_id, subject, lang, version)  -- Idempotence
);
```

**Indexes** :
- `idx_lunar_interpretations_user` : `user_id`
- `idx_lunar_interpretations_return` : `lunar_return_id`
- `idx_lunar_interpretations_unique` : `(lunar_return_id, subject, lang, version)` UNIQUE

### LunarInterpretationTemplate (Fallback)

Table : `lunar_interpretation_templates`

1728 templates statiques utilisés comme fallback.

---

## ⚠️ Codes d'erreur

| Code | Message | Description |
|------|---------|-------------|
| 401 | Unauthorized | JWT token manquant ou invalide |
| 403 | Forbidden | Accès refusé (ownership check) |
| 404 | Not Found | Ressource introuvable (LunarReturn, NatalChart) |
| 422 | Validation Error | Paramètres invalides |
| 503 | Service Unavailable | Tous les fallbacks ont échoué |

---

## 💡 Exemples d'utilisation

### Exemple 1 : Récupérer rapport lunaire

```typescript
// React Native (apps/mobile)
import { getLunarReport } from '@/services/api';

const LunarReportScreen = () => {
  const [report, setReport] = useState(null);

  useEffect(() => {
    const fetchReport = async () => {
      try {
        const data = await getLunarReport();
        setReport(data);
        console.log('Source:', data.metadata.source); // "claude" ou "db_temporal"
      } catch (error) {
        console.error('Error:', error);
      }
    };
    fetchReport();
  }, []);

  return (
    <View>
      <Text>{report?.interpretation.full}</Text>
      <Text style={{ fontSize: 10, color: 'gray' }}>
        Source: {report?.metadata.source} ({report?.metadata.model_used})
      </Text>
    </View>
  );
};
```

### Exemple 2 : Force regenerate

```typescript
// Bouton "Régénérer l'interprétation"
const handleRegenerate = async (lunarReturnId: number) => {
  try {
    const response = await fetch('/api/lunar/interpretation/regenerate', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        lunar_return_id: lunarReturnId,
        subject: 'full'
      })
    });

    if (response.ok) {
      const data = await response.json();
      alert('Interprétation régénérée !');
      // Mettre à jour l'UI avec data.interpretation
    }
  } catch (error) {
    alert('Erreur lors de la régénération');
  }
};
```

### Exemple 3 : Afficher stats metadata

```typescript
// Dashboard utilisateur
const MetadataStats = () => {
  const [metadata, setMetadata] = useState(null);

  useEffect(() => {
    const fetchMetadata = async () => {
      const response = await fetch('/api/lunar/interpretation/metadata', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setMetadata(data);
    };
    fetchMetadata();
  }, []);

  return (
    <View>
      <Text>Total interprétations : {metadata?.total_interpretations}</Text>
      <Text>Cache rate : {metadata?.cached_rate}%</Text>
      <Text>Modèles utilisés :</Text>
      {metadata?.models_used.map(m => (
        <Text key={m.model}>- {m.model}: {m.percentage}%</Text>
      ))}
    </View>
  );
};
```

---

## 🔄 Migration V1 → V2

### Changements majeurs

| Aspect | V1 | V2 |
|--------|----|----|
| Stockage | Fichiers JSON statiques | DB temporelle + templates |
| Génération | Pré-générée (1728 combinaisons) | À la volée (Claude Opus 4.5) |
| Fallback | Fichiers JSON → hardcoded | DB temporelle → Claude → DB templates → hardcoded |
| Metadata | Aucune | source, model_used, version, generated_at |
| Régénération | Impossible | Endpoint dédié `/regenerate` |
| Stats | Aucune | Endpoint `/metadata` avec stats |

### Guide de migration frontend

**Avant (V1)** :
```typescript
// Interprétation statique, toujours la même
const interpretation = lunarReport.interpretation;
```

**Après (V2)** :
```typescript
// Interprétation dynamique avec metadata
const interpretation = lunarReport.interpretation.full;
const source = lunarReport.metadata.source; // "claude" ou "db_temporal"

// Afficher la source à l'utilisateur (optionnel)
if (source === 'claude') {
  console.log('✨ Interprétation générée par IA');
} else if (source === 'db_temporal') {
  console.log('⚡ Interprétation depuis cache');
}
```

### Rétrocompatibilité

✅ Les routes V1 continuent de fonctionner via legacy wrapper :
- `GET /api/lunar-returns/current/report` retourne format compatible V1+V2
- Champ `interpretation` contient à la fois V1 (texte simple) et V2 (objet avec metadata)

---

## 📚 Ressources

- **Architecture V2** : `docs/LUNAR_ARCHITECTURE_V2.md`
- **Plan migration** : `docs/MIGRATION_PLAN.md`
- **Monitoring** : `docs/MONITORING.md`
- **Code source** :
  - Generator : `services/lunar_interpretation_generator.py`
  - Routes : `routes/lunar_returns.py`, `routes/lunar.py`
  - Modèles : `models/lunar_interpretation.py`
```

#### 2. Validation et exemples (30min)

**a) Tester les exemples cURL** :
```bash
# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'

# Sauver le token
TOKEN="eyJhbGci..."

# Tester GET /current/report
curl -X GET http://localhost:8000/api/lunar-returns/current/report \
  -H "Authorization: Bearer $TOKEN"

# Tester POST /regenerate
curl -X POST http://localhost:8000/api/lunar/interpretation/regenerate \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"lunar_return_id":1}'

# Tester GET /metadata
curl -X GET http://localhost:8000/api/lunar/interpretation/metadata \
  -H "Authorization: Bearer $TOKEN"
```

**b) Vérifier format responses** :
- JSON valide
- Champs metadata présents
- Types corrects (integer, string, etc.)

### 📦 Livrables

1. ✅ Document `docs/API_LUNAR_V2.md` complet (6+ sections)
2. ✅ 3 endpoints documentés avec exemples
3. ✅ Code examples TypeScript/React Native
4. ✅ Guide de migration V1→V2
5. ✅ Exemples cURL testés

### 🎯 Critères de succès

- [ ] Documentation API complète (introduction, auth, endpoints, exemples)
- [ ] 3 endpoints documentés avec request/response examples
- [ ] Code examples fonctionnels (TypeScript)
- [ ] Guide migration V1→V2 clair
- [ ] Tous les exemples cURL testés et validés

### 📚 Références

**Fichiers à étudier** :
- `routes/lunar_returns.py` : Endpoints API
- `routes/lunar.py` : Metadata + regenerate
- `schemas/lunar.py` : Schémas Pydantic
- `docs/LUNAR_ARCHITECTURE_V2.md` : Architecture V2

---

## 🤖 Agent C - Task 5.3 + 5.4 : Cleanup & CLAUDE.md Final (45min)

### 📊 Contexte

Tu es l'Agent C de la Vague 5. Ta mission est de nettoyer le projet et finaliser la documentation CLAUDE.md avec le statut complet du Sprint 5.

**Prérequis complétés** :
- ✅ Vague 4 : Tests validés (525 passed, 33 skipped)
- ✅ Sprint 5 Vagues 1-4 terminées
- ✅ Architecture V2 complète et opérationnelle

### 🎯 Objectif

Préparer le projet pour production : cleanup fichiers temporaires, archivage, et documentation finale.

### 📝 Tâches principales

#### 1. Cleanup fichiers temporaires (15min)

**a) Identifier fichiers à archiver** :
```bash
# Lister fichiers untracked
git status --short | grep "??"

# Lister fichiers .pyc et __pycache__
find . -name "*.pyc" -o -name "__pycache__"

# Lister logs temporaires
find . -name "*.log"
```

**b) Créer `.tasks/cleanup_report.md`** :
```markdown
# Cleanup Report - Sprint 5 Vague 5

**Date** : 2026-01-23
**Agent** : Agent C

## Fichiers nettoyés

### Scripts archivés (déjà fait Sprint 4)
- ✅ 149 fichiers archivés dans `scripts/archives/`
  - 30 scripts Sprint 3 génération
  - 107 scripts insertion données natales
  - 12 scripts utilitaires historiques

### Cache et fichiers temporaires
- [ ] `__pycache__/` directories (à ignorer via .gitignore)
- [ ] `.pytest_cache/` (à ignorer via .gitignore)
- [ ] `*.pyc` files (déjà ignorés)

### Logs
- [ ] `logs/*.log` (déjà ignorés via .gitignore)

## Actions recommandées

### Immédiat
- Aucune action nécessaire (cleanup Sprint 4 suffisant)

### Futur
- Considérer archivage scripts Sprint 5 si nouveaux scripts créés
- Nettoyer logs production > 30 jours (rotation)

## Statut
✅ **Projet propre et prêt pour production**
```

**c) Vérifier .gitignore** :
```bash
# Vérifier que .gitignore contient bien :
# __pycache__/
# *.pyc
# .pytest_cache/
# logs/*.log
# .env

cat .gitignore | grep -E "__pycache__|*.pyc|pytest_cache|logs"
```

#### 2. Mettre à jour CLAUDE.md final (30min)

**a) Lire CLAUDE.md actuel** :
```bash
cat .claude/CLAUDE.md | grep -A 20 "Sprint 5"
```

**b) Mettre à jour section "Sprint 5"** :

Ajouter dans `.claude/CLAUDE.md` :

```markdown
### 🌊 Vague 5 : Monitoring & Cleanup (2h) - ✅ **COMPLÈTE**

| Agent | Tâches | Durée | État | Dépendances |
|-------|--------|-------|------|-------------|
| **Agent A** | Task 5.1 : Métriques Prometheus | 2h | ✅ **TERMINÉ** | ✅ Vague 1 (2.1) |
| **Agent B** | Task 5.2 : Docs API utilisateur | 1h30 | ✅ **TERMINÉ** | ✅ Vague 3 (routes finales) |
| **Agent C** | Task 5.3 + 5.4 : Cleanup + CLAUDE.md | 45min | ✅ **TERMINÉ** | ✅ Vague 4 (validation) |

**Réalisations Agent A (23/01/2026)** :
- ✅ Task 5.1 : Dashboard Prometheus créé
  - **Dashboard Grafana** : `monitoring/prometheus_dashboard.json` (6 panels)
  - **Documentation** : `docs/MONITORING.md` (métriques, SLOs, alertes)
  - **Panels créés** :
    1. Générations par source (Time Series)
    2. Cache hit rate (Gauge)
    3. Distribution fallbacks (Pie Chart)
    4. Latence génération P50/P95/P99 (Heatmap)
    5. Générations actives (Graph)
    6. Erreurs Claude API (Stat)
  - **Alertes documentées** : 4 alertes (cache low, fallback high, latency high, concurrency high)
  - **Métriques validées** : Endpoint `/metrics` opérationnel

**Réalisations Agent B (23/01/2026)** :
- ✅ Task 5.2 : Documentation API V2 complète
  - **Document** : `docs/API_LUNAR_V2.md` (documentation exhaustive)
  - **Sections** : Introduction, Auth, 3 endpoints, Modèles, Erreurs, Exemples, Migration V1→V2
  - **Endpoints documentés** :
    1. GET `/api/lunar-returns/current/report` : Rapport lunaire avec metadata V2
    2. POST `/api/lunar/interpretation/regenerate` : Force regenerate
    3. GET `/api/lunar/interpretation/metadata` : Stats utilisateur
  - **Code examples** : TypeScript/React Native (3 exemples)
  - **Guide migration** : V1→V2 avec rétrocompatibilité
  - **Exemples cURL** : Tous testés et validés

**Réalisations Agent C (23/01/2026)** :
- ✅ Task 5.3 + 5.4 : Cleanup et documentation finale
  - **Cleanup report** : `.tasks/cleanup_report.md` (audit complet)
  - **Fichiers nettoyés** : Projet déjà propre (cleanup Sprint 4 suffisant)
  - **CLAUDE.md** : Mise à jour finale avec statut Sprint 5 complet
  - **Statut final** : ✅ Projet prêt pour production

**État** : ✅ **COMPLÈTE - 3/3 agents terminés avec succès**

**Sprint 5 : TERMINÉ** ✅
- ✅ Architecture V2 complète (4 couches)
- ✅ Génération à la volée (Claude Opus 4.5 + fallbacks)
- ✅ Tests complets (525 passed)
- ✅ Monitoring Prometheus opérationnel
- ✅ Documentation API complète
- ✅ Projet prêt pour production 🚀
```

**c) Mettre à jour "Timeline Vagues"** :
```markdown
```
Vague 1 (2h)    : ✅ TERMINÉE
Vague 2 (2h30)  : ✅ TERMINÉE
Vague 3 (1h30)  : ✅ TERMINÉE
Vague 4 (3h30)  : ✅ TERMINÉE
Vague 5 (2h)    : ✅ TERMINÉE
────────────────────────────────────────────────
Total : 11h30 (vs 23h séquentiel = 50% gain)
Progression : 11h30/11h30 (100% COMPLÉTÉ ✅)
```
```

**d) Mettre à jour "Checklist Vagues"** :
```markdown
- [x] **Vague 1** : ✅ TERMINÉE
- [x] **Vague 2** : ✅ TERMINÉE
- [x] **Vague 3** : ✅ TERMINÉE
- [x] **Vague 4** : ✅ TERMINÉE
- [x] **Vague 5** : ✅ TERMINÉE - **SPRINT 5 COMPLET** 🎉
```

#### 3. Commit final (5min)

```bash
# Vérifier status
git status

# Commit Vague 5
git add monitoring/ docs/MONITORING.md docs/API_LUNAR_V2.md .tasks/cleanup_report.md .claude/CLAUDE.md
git commit -m "feat(monitoring): Sprint 5 Vague 5 COMPLET - Dashboard Prometheus + Docs API V2 + Cleanup final

- Agent A: Dashboard Grafana 6 panels + docs monitoring (MONITORING.md)
- Agent B: Documentation API V2 complète (API_LUNAR_V2.md)
- Agent C: Cleanup report + CLAUDE.md final

Sprint 5 TERMINÉ ✅ - Architecture Lunar V2 prête pour production 🚀"
```

### 📦 Livrables

1. ✅ Cleanup report (`.tasks/cleanup_report.md`)
2. ✅ CLAUDE.md mis à jour avec statut Sprint 5 final
3. ✅ Commit final Sprint 5

### 🎯 Critères de succès

- [ ] Cleanup report créé et complet
- [ ] CLAUDE.md mis à jour avec toutes les réalisations Vague 5
- [ ] Timeline mise à jour (100% complété)
- [ ] Commit final effectué

### 📚 Références

**Fichiers à modifier** :
- `.claude/CLAUDE.md` : Documentation principale
- `.tasks/cleanup_report.md` : Rapport cleanup (à créer)

---

## 📋 Checklist Vague 5

### Agent A (Métriques Prometheus)
- [ ] Dashboard Grafana créé (6+ panels)
- [ ] Document MONITORING.md créé
- [ ] Métriques validées via `/metrics`
- [ ] 4+ alertes documentées
- [ ] Commit: `feat(monitoring): ajouter dashboard Prometheus + docs`

### Agent B (Documentation API)
- [ ] Document API_LUNAR_V2.md créé
- [ ] 3 endpoints documentés
- [ ] Code examples TypeScript validés
- [ ] Guide migration V1→V2 complet
- [ ] Exemples cURL testés
- [ ] Commit: `docs(api): ajouter documentation API Lunar V2`

### Agent C (Cleanup & Final)
- [ ] Cleanup report créé
- [ ] CLAUDE.md mis à jour
- [ ] Timeline 100% complétée
- [ ] Commit final Sprint 5
- [ ] Commit: `feat(monitoring): Sprint 5 Vague 5 COMPLET`

---

## 🎯 Coordination Inter-Agents

**Ordre d'exécution recommandé** :
1. **Parallèle** : Les 3 agents peuvent travailler en parallèle (pas de dépendances)
2. **Validation finale** : Agent C valide que tous les livrables sont présents

**Communication** :
- Signaler si fichiers manquants ou problèmes bloquants
- Partager progrès toutes les 30min

**Validation finale** (après les 3 agents) :
```bash
# Vérifier livrables
ls monitoring/prometheus_dashboard.json  # Agent A
ls docs/MONITORING.md                     # Agent A
ls docs/API_LUNAR_V2.md                   # Agent B
ls .tasks/cleanup_report.md               # Agent C

# Vérifier tests passent toujours
pytest -q
# Objectif : 525+ passed, 33 skipped
```

---

**Bonne chance aux 3 agents ! 🚀**

Le Sprint 5 est la dernière vague - après celle-ci, l'architecture Lunar V2 sera complète et prête pour production !
