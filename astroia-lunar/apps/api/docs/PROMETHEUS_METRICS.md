# Prometheus Metrics - Lunar V2

Documentation des métriques Prometheus pour monitoring production.

## 🎯 Endpoint `/metrics`

L'endpoint `/metrics` expose les métriques au format Prometheus text format.

**URL** : `http://localhost:8000/metrics` (dev) ou `https://api.astroia.com/metrics` (prod)
**Méthode** : GET
**Auth** : Aucune (endpoint public pour scrapers Prometheus)
**Content-Type** : `text/plain; version=0.0.4; charset=utf-8`

## 📊 Métriques Exposées

### 1. Génération d'interprétations

#### `lunar_interpretation_generated_total` (Counter)
**Description** : Total des interprétations lunaires générées.

**Labels** :
- `source` : Origine de l'interprétation (`db_temporal`, `claude`, `db_template`, `hardcoded`)
- `model` : Modèle utilisé (`claude-opus-4-5-20251101`, `template`, `none`)
- `subject` : Type d'interprétation (`full`, `climate`, `focus`, `approach`)
- `version` : Version architecture (`2`)

**Exemple** :
```promql
lunar_interpretation_generated_total{source="claude",model="claude-opus-4-5-20251101",subject="full",version="2"} 1234.0
lunar_interpretation_generated_total{source="db_template",model="template",subject="climate",version="2"} 567.0
```

**Queries utiles** :
```promql
# Total générations par source (5 dernières minutes)
rate(lunar_interpretation_generated_total[5m])

# Pourcentage générations Claude vs templates
sum(rate(lunar_interpretation_generated_total{source="claude"}[5m])) / sum(rate(lunar_interpretation_generated_total[5m])) * 100
```

---

#### `lunar_interpretation_cache_hit_total` (Counter)
**Description** : Total des cache hits (interprétations servies depuis DB temporelle).

**Labels** :
- `subject` : Type d'interprétation
- `version` : Version architecture

**Exemple** :
```promql
lunar_interpretation_cache_hit_total{subject="full",version="2"} 8765.0
```

**Queries utiles** :
```promql
# Cache hit rate (%)
rate(lunar_interpretation_cache_hit_total[5m]) / rate(lunar_interpretation_generated_total[5m]) * 100

# Cache misses (générations nécessaires)
rate(lunar_interpretation_generated_total[5m]) - rate(lunar_interpretation_cache_hit_total[5m])
```

---

#### `lunar_interpretation_fallback_total` (Counter)
**Description** : Total des fallbacks vers templates ou hardcodé.

**Labels** :
- `fallback_level` : Niveau de fallback (`db_template`, `hardcoded`)

**Exemple** :
```promql
lunar_interpretation_fallback_total{fallback_level="db_template"} 123.0
lunar_interpretation_fallback_total{fallback_level="hardcoded"} 5.0
```

**Queries utiles** :
```promql
# Taux de fallback (%)
rate(lunar_interpretation_fallback_total[5m]) / rate(lunar_interpretation_generated_total[5m]) * 100

# Alerte si trop de fallbacks hardcodé (sign of API issues)
rate(lunar_interpretation_fallback_total{fallback_level="hardcoded"}[5m]) > 10
```

---

### 2. Performance

#### `lunar_interpretation_duration_seconds` (Histogram)
**Description** : Distribution de la durée de génération des interprétations.

**Labels** :
- `source` : Origine de l'interprétation
- `subject` : Type d'interprétation

**Buckets** : `0.05, 0.1, 0.5, 1, 2, 5, 10, 30` (secondes)

**Exemple** :
```promql
lunar_interpretation_duration_seconds_bucket{source="claude",subject="full",le="5.0"} 1234.0
lunar_interpretation_duration_seconds_sum{source="claude",subject="full"} 4567.8
lunar_interpretation_duration_seconds_count{source="claude",subject="full"} 1234.0
```

**Queries utiles** :
```promql
# Durée moyenne (dernières 5min)
rate(lunar_interpretation_duration_seconds_sum[5m]) / rate(lunar_interpretation_duration_seconds_count[5m])

# p95 (95e percentile)
histogram_quantile(0.95, rate(lunar_interpretation_duration_seconds_bucket[5m]))

# p99 (99e percentile)
histogram_quantile(0.99, rate(lunar_interpretation_duration_seconds_bucket[5m]))

# Durée par source
histogram_quantile(0.95, rate(lunar_interpretation_duration_seconds_bucket{source="claude"}[5m]))
histogram_quantile(0.95, rate(lunar_interpretation_duration_seconds_bucket{source="db_temporal"}[5m]))
```

---

### 3. État système

#### `lunar_active_generations` (Gauge)
**Description** : Nombre de générations en cours (requêtes actives vers Claude API).

**Exemple** :
```promql
lunar_active_generations 3.0
```

**Queries utiles** :
```promql
# Générations actives
lunar_active_generations

# Alerte si trop de générations actives (sign of API slowdown)
lunar_active_generations > 50
```

---

### 4. Migration info

#### `lunar_migration_info` (Info)
**Description** : Métadonnées sur l'état de la migration V1 → V2.

**Labels** :
- `version` : Version architecture (`2.0`)
- `templates_count` : Nombre de templates migrés (`1728`)
- `migration_date` : Date de migration (`2026-01-23`)
- `architecture` : Architecture (`4_layers`)

**Exemple** :
```promql
lunar_migration_info{version="2.0",templates_count="1728",migration_date="2026-01-23",architecture="4_layers"} 1.0
```

---

### 5. Scheduler - Lunar Returns Refresh

#### `lunar_returns_refresh_total` (Counter)
**Description** : Nombre total d'utilisateurs traités lors du refresh quotidien.

**Labels** :
- `status` : Statut (`success`, `failed`)

**Exemple** :
```promql
lunar_returns_refresh_total{status="success"} 9.0
lunar_returns_refresh_total{status="failed"} 1.0
```

**Queries utiles** :
```promql
# Taux de succès quotidien
rate(lunar_returns_refresh_total{status="success"}[1d]) / rate(lunar_returns_refresh_total[1d]) * 100
```

---

#### `lunar_returns_refresh_duration_seconds` (Histogram)
**Description** : Durée du cycle de refresh quotidien.

**Buckets** : `5, 10, 30, 60, 120, 300, 600` (5s → 10min)

**Exemple** :
```promql
lunar_returns_refresh_duration_seconds_bucket{le="5.0"} 10.0
lunar_returns_refresh_duration_seconds_sum 450.5
lunar_returns_refresh_duration_seconds_count 10.0
```

**Queries utiles** :
```promql
# Durée moyenne
lunar_returns_refresh_duration_seconds_sum / lunar_returns_refresh_duration_seconds_count

# Alerte si durée > 5 min
lunar_returns_refresh_duration_seconds_sum / lunar_returns_refresh_duration_seconds_count > 300
```

---

#### `lunar_returns_refresh_failure_rate` (Gauge)
**Description** : Taux d'échec du dernier refresh (0-1).

**Exemple** :
```promql
lunar_returns_refresh_failure_rate 0.05
```

**Queries utiles** :
```promql
# Taux en %
lunar_returns_refresh_failure_rate * 100

# Alerte si > 20%
lunar_returns_refresh_failure_rate > 0.20
```

---

#### `lunar_returns_refresh_users_total` (Gauge)
**Description** : Nombre total d'utilisateurs traités (dernier run).

**Exemple** :
```promql
lunar_returns_refresh_users_total 15.0
```

**Queries utiles** :
```promql
# Évolution quotidienne
lunar_returns_refresh_users_total
```

---

## 🛠️ Utilisation

### Tester endpoint localement

```bash
# Démarrer API
cd apps/api
uvicorn main:app --reload

# Tester endpoint
curl http://localhost:8000/metrics

# Filtrer métriques lunaires
curl -s http://localhost:8000/metrics | grep lunar_

# Afficher métriques spécifiques
curl -s http://localhost:8000/metrics | grep lunar_interpretation_generated_total
```

### Configurer Prometheus

**Fichier** : `prometheus.yml`

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'astroia-api'
    static_configs:
      - targets: ['localhost:8000']
    metrics_path: '/metrics'
```

**Démarrer Prometheus** :
```bash
prometheus --config.file=prometheus.yml
```

**Interface** : http://localhost:9090

---

## 📈 Dashboard Grafana

### Panels recommandés

#### 1. Générations par source (Time series)
```promql
rate(lunar_interpretation_generated_total[5m])
```
**Legend** : `{{source}} - {{subject}}`

#### 2. Cache hit rate (Gauge)
```promql
rate(lunar_interpretation_cache_hit_total[5m]) / rate(lunar_interpretation_generated_total[5m]) * 100
```
**Unit** : `percent (0-100)`
**Thresholds** : 🟢 >70%, 🟡 50-70%, 🔴 <50%

#### 3. Fallback rate (Gauge)
```promql
rate(lunar_interpretation_fallback_total[5m]) / rate(lunar_interpretation_generated_total[5m]) * 100
```
**Unit** : `percent (0-100)`
**Thresholds** : 🟢 <10%, 🟡 10-30%, 🔴 >30%

#### 4. Durée génération p95 (Time series)
```promql
histogram_quantile(0.95, rate(lunar_interpretation_duration_seconds_bucket[5m]))
```
**Legend** : `{{source}} - p95`
**Unit** : `seconds`

#### 5. Générations actives (Gauge)
```promql
lunar_active_generations
```
**Unit** : `short`
**Thresholds** : 🟢 <10, 🟡 10-30, 🔴 >30

---

## 🚨 Alertes recommandées

### 1. Cache hit rate bas
```yaml
alert: LunarCacheHitRateLow
expr: rate(lunar_interpretation_cache_hit_total[5m]) / rate(lunar_interpretation_generated_total[5m]) * 100 < 50
for: 10m
annotations:
  summary: "Cache hit rate lunaire bas ({{$value}}%)"
  description: "Le cache hit rate est inférieur à 50% depuis 10min. Vérifier la DB."
```

### 2. Trop de fallbacks hardcodé
```yaml
alert: LunarHardcodedFallbackHigh
expr: rate(lunar_interpretation_fallback_total{fallback_level="hardcoded"}[5m]) > 5
for: 5m
annotations:
  summary: "Trop de fallbacks hardcodé ({{$value}}/s)"
  description: "Plus de 5 fallbacks hardcodé par seconde. Vérifier API Claude et DB templates."
```

### 3. Durée génération p95 élevée
```yaml
alert: LunarGenerationSlow
expr: histogram_quantile(0.95, rate(lunar_interpretation_duration_seconds_bucket{source="claude"}[5m])) > 10
for: 5m
annotations:
  summary: "Durée génération Claude p95 élevée ({{$value}}s)"
  description: "Le p95 de génération Claude dépasse 10s. Vérifier API Anthropic."
```

### 4. Générations actives élevées
```yaml
alert: LunarActiveGenerationsHigh
expr: lunar_active_generations > 30
for: 5m
annotations:
  summary: "Trop de générations actives ({{$value}})"
  description: "Plus de 30 générations en cours. Vérifier si API Claude ralentit."
```

### 5. Taux d'échec refresh élevé
```yaml
alert: LunarRefreshFailureRateHigh
expr: lunar_returns_refresh_failure_rate > 0.20
for: 10m
annotations:
  summary: "Taux d'échec refresh lunar returns élevé ({{$value | humanizePercentage}})"
  description: "Le taux d'échec du refresh quotidien dépasse 20%. Vérifier logs ERROR 🚨 [ALERT]."
```

### 6. Refresh trop long
```yaml
alert: LunarRefreshDurationHigh
expr: lunar_returns_refresh_duration_seconds_sum / lunar_returns_refresh_duration_seconds_count > 300
for: 5m
annotations:
  summary: "Durée refresh lunar returns élevée ({{$value}}s)"
  description: "Le refresh quotidien prend plus de 5 minutes. Optimiser ou scaler workers."
```

### 7. Aucun refresh depuis 2 jours
```yaml
alert: LunarRefreshStale
expr: time() - timestamp(lunar_returns_refresh_users_total) > 2*24*3600
for: 30m
annotations:
  summary: "Aucun refresh lunar returns depuis 2 jours"
  description: "Le dernier refresh date de plus de 2 jours. Vérifier si le cron job est actif."
```

---

## 🧪 Tests

### Tests unitaires
```bash
# Tests endpoint /metrics
pytest tests/test_metrics_endpoint.py -v

# Tests système d'alerte scheduler
pytest tests/test_scheduler_alerts.py -v
```

**Coverage** : 16 tests
- **Endpoint /metrics** (11 tests) :
  - Endpoint existe
  - Retourne 200 OK
  - Content-Type correct
  - Métriques lunaires présentes
  - Métrique migration_info présente
  - Format Prometheus valide
  - Types de métriques corrects
- **Système d'alerte scheduler** (5 tests) :
  - Requête SQL identifie users dans fenêtre
  - Alerte déclenchée si taux échec > 20%
  - Pas d'alerte si taux échec <= 20%
  - Métriques Prometheus enregistrées
  - Gestion cas limite total_users=0

---

## 📚 Références

- [Prometheus Documentation](https://prometheus.io/docs/)
- [Prometheus Client Python](https://github.com/prometheus/client_python)
- [PromQL Cheat Sheet](https://promlabs.com/promql-cheat-sheet/)
- [Grafana Dashboards](https://grafana.com/docs/grafana/latest/dashboards/)

---

**Dernière mise à jour** : 2026-01-25
**Version** : 1.1 (Sprint 6 - Système d'alerte + Cron quotidien)
**Auteur** : Claude Opus 4.5
