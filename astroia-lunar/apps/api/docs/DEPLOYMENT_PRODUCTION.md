# Guide Déploiement Production - Génération Lunaire Claude Opus 4.5

**Date** : 2026-01-24
**Version** : 1.0
**Statut** : ✅ Système validé et prêt pour production

---

## 📋 Table des Matières

1. [Prérequis](#prérequis)
2. [Configuration Production](#configuration-production)
3. [Checklist Déploiement](#checklist-déploiement)
4. [Monitoring](#monitoring)
5. [Rollback](#rollback)
6. [Troubleshooting](#troubleshooting)

---

## 🎯 Prérequis

### Infrastructure
- ✅ PostgreSQL 14+ (Supabase ou self-hosted)
- ✅ FastAPI backend déployé (Render, Railway, AWS, etc.)
- ✅ Prometheus + Grafana (monitoring)
- ✅ Budget Anthropic : $50-100/mois pour 1,000-5,000 users

### Validations
- ✅ Tests passent : 59 tests (35 unitaires + 24 E2E)
- ✅ POC réussi : 10/10 générations Claude Opus 4.5
- ✅ Prompt Caching activé : -90% coûts
- ✅ Templates DB : 1,728 templates disponibles

---

## ⚙️ Configuration Production

### 1. Variables d'environnement (.env)

```bash
# ===========================================
# GÉNÉRATION LUNAIRE - CONFIGURATION PRODUCTION
# ===========================================

# MODE GÉNÉRATION (CRITICAL)
LUNAR_LLM_MODE=anthropic           # anthropic = Claude génération | off = templates uniquement
LUNAR_INTERPRETATION_VERSION=2     # Version 2 (architecture 4 niveaux)

# ANTHROPIC API
ANTHROPIC_API_KEY=sk-ant-...       # ⚠️ SECRET - Ne JAMAIS commiter
LUNAR_CLAUDE_MODEL=opus            # opus | sonnet | haiku

# DATABASE
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/astroia_lunar
DATABASE_POOL_SIZE=20              # Pool size pour production
DATABASE_MAX_OVERFLOW=10           # Max overflow connections

# MONITORING
APP_ENV=production                 # production | development | test
API_HOST=0.0.0.0
API_PORT=8000

# SÉCURITÉ
SECRET_KEY=<your-secret-key>       # ⚠️ Générer avec: openssl rand -hex 32
DEV_AUTH_BYPASS=0                  # ⚠️ CRITICAL: Désactiver en production
```

### 2. Vérifications Base de Données

```sql
-- Vérifier templates disponibles
SELECT COUNT(*) FROM lunar_interpretation_templates;
-- Expected: 1728

-- Vérifier indexes
SELECT schemaname, tablename, indexname
FROM pg_indexes
WHERE tablename IN ('lunar_interpretations', 'lunar_interpretation_templates');
-- Expected: Indexes sur (lunar_return_id, user_id, subject, version, lang)

-- Vérifier UNIQUE constraint
SELECT conname, contype
FROM pg_constraint
WHERE conrelid = 'lunar_interpretations'::regclass
  AND contype = 'u';
-- Expected: lunar_interpretations_lunar_return_id_subject_version_lang_key
```

### 3. Health Checks

```bash
# API Health
curl https://your-api.com/health
# Expected: {"status":"healthy","checks":{"database":"configured","rapidapi_config":"configured"}}

# Metrics endpoint
curl https://your-api.com/metrics | grep lunar_
# Expected: 6 métriques lunaires (generated, cache_hit, fallback, duration, active, migration_info)
```

---

## ✅ Checklist Déploiement

### Phase 1 : Préparation (J-7)

- [ ] **Backup DB complet** : `pg_dump astroia_lunar > backup_pre_deployment.sql`
- [ ] **Tests E2E** : `pytest -v` → 59 tests passent
- [ ] **Validation Anthropic API Key** : Tester avec 1 génération manuelle
- [ ] **Review code** : Aucun secret hardcodé (run `git-secrets --scan`)
- [ ] **Documentation** : CLAUDE.md à jour

### Phase 2 : Configuration (J-1)

- [ ] **Variables d'environnement** :
  - `LUNAR_LLM_MODE=anthropic` ✅
  - `ANTHROPIC_API_KEY=sk-ant-...` ✅
  - `DEV_AUTH_BYPASS=0` ⚠️ CRITICAL
  - `APP_ENV=production` ✅
- [ ] **Database migrations** : `alembic upgrade head`
- [ ] **Vérifier templates DB** : 1,728 rows
- [ ] **Prometheus alerts** : Configurer (voir section Monitoring)

### Phase 3 : Déploiement (J-Day)

- [ ] **Deploy backend** :
  ```bash
  git pull origin main
  pip install -r requirements.txt
  alembic upgrade head
  uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
  ```
- [ ] **Smoke tests** :
  - Health check : `curl /health`
  - Metrics : `curl /metrics | grep lunar_`
  - Génération test : POST `/api/lunar-returns/current` (1 user)
- [ ] **Monitor logs** : Vérifier aucune erreur pendant 30min
- [ ] **Vérifier coûts** : Anthropic dashboard (première heure <$1)

### Phase 4 : Validation (J+1)

- [ ] **Cache hit rate** : Vérifier >0% après 24h
- [ ] **Coût quotidien** : <$5 pour <500 users
- [ ] **Taux erreur** : <5% fallbacks
- [ ] **Performance** : P95 latence <15s
- [ ] **User feedback** : Pas de plaintes qualité

---

## 📊 Monitoring

### Métriques Clés (Prometheus)

#### 1. Coût Quotidien
```promql
# Générations Claude dernières 24h
sum(increase(lunar_interpretation_generated_total{source="claude"}[24h]))

# Coût estimé (sans caching)
sum(increase(lunar_interpretation_generated_total{source="claude"}[24h])) * 0.020

# Coût estimé (avec caching -90%)
sum(increase(lunar_interpretation_generated_total{source="claude"}[24h])) * 0.002
```

#### 2. Taux de Cache Hit
```promql
# Cache hit rate (%)
sum(rate(lunar_interpretation_cache_hit_total[5m])) /
sum(rate(lunar_interpretation_generated_total[5m])) * 100
```

#### 3. Taux de Fallback
```promql
# Fallback rate (%) - doit être <10%
sum(rate(lunar_interpretation_fallback_total[5m])) /
sum(rate(lunar_interpretation_generated_total[5m])) * 100
```

#### 4. Performance (Latence)
```promql
# P95 latence (doit être <15s)
histogram_quantile(0.95,
  rate(lunar_interpretation_duration_seconds_bucket{source="claude"}[5m])
)
```

### Grafana Dashboard

**Panels recommandés** :
1. **Générations/heure** : Graph timeseries par source
2. **Coût quotidien** : Stat panel avec threshold ($10/jour)
3. **Cache hit rate** : Gauge (target >70%)
4. **P95 latency** : Graph (target <15s)
5. **Fallback rate** : Gauge (alarm si >10%)

### Logs Structurés (structlog)

```bash
# Logs de génération
tail -f /var/log/api.log | grep lunar_interpretation_generation

# Exemples de logs
# 2026-01-24 14:21:39 [info] lunar_interpretation_generation_started lang=fr lunar_return_id=12 user_id=1
# 2026-01-24 14:21:50 [info] lunar_interpretation_generated source=claude duration_ms=11421 model_used=claude-opus-4-5
```

---

## 🔄 Rollback

### Scénario 1 : Coût Trop Élevé (>$50/jour)

**Symptômes** :
- Anthropic dashboard montre coût anormal
- Metric `lunar_interpretation_generated_total{source="claude"}` explose

**Actions** :
```bash
# 1. Désactiver génération Claude immédiatement
# Éditer .env sur le serveur
LUNAR_LLM_MODE=off

# 2. Redémarrer API
sudo systemctl restart api
# ou
kill -HUP <pid>

# 3. Vérifier fallback vers templates
curl https://api.com/api/lunar-returns/current | jq '.metadata.source'
# Expected: "db_template"
```

### Scénario 2 : Qualité Insuffisante

**Symptômes** :
- User complaints
- Interprétations incohérentes

**Actions** :
```bash
# Rollback vers templates statiques
LUNAR_LLM_MODE=off

# Alternative : Switch to Sonnet (plus stable)
LUNAR_CLAUDE_MODEL=sonnet
```

### Scénario 3 : Anthropic API Down

**Symptômes** :
- Metric `lunar_interpretation_fallback_total` > 50%
- Logs : `calling_claude_api` → erreurs

**Actions** :
```bash
# Aucune action requise - fallback automatique activé
# Système bascule automatiquement :
# 1. Retry Claude (3x avec backoff)
# 2. Fallback DB templates
# 3. Fallback hardcoded

# Vérifier fallback fonctionne
curl /api/lunar-returns/current | jq '.metadata.source'
# Expected: "db_template" ou "hardcoded"
```

---

## 🐛 Troubleshooting

### Problème : Générations lentes (>30s)

**Diagnostic** :
```promql
histogram_quantile(0.95, rate(lunar_interpretation_duration_seconds_bucket[5m]))
```

**Solutions** :
1. Vérifier timeout Claude (30s) : Augmenter si nécessaire
2. Switch to Sonnet : Plus rapide (5-8s vs 10-12s)
3. Vérifier pool DB : Augmenter `DATABASE_POOL_SIZE`

### Problème : Cache hit rate faible (<20%)

**Diagnostic** :
```sql
SELECT COUNT(DISTINCT lunar_return_id) FROM lunar_interpretations;
SELECT COUNT(*) FROM lunar_returns;
```

**Solutions** :
1. **Normal au début** : Cache se construit progressivement
2. **Vérifier UNIQUE constraint** : Pas de doublons
3. **Force regenerate** : Vérifier pas utilisé par défaut

### Problème : Coût élevé malgré caching

**Diagnostic** :
```bash
# Vérifier caching Anthropic utilisé
grep "cache_control" services/lunar_interpretation_generator.py
```

**Solutions** :
1. Vérifier system message avec `cache_control: ephemeral`
2. Vérifier Anthropic dashboard : "Prompt caching usage"
3. Contact Anthropic support si caching pas appliqué

### Problème : Erreurs 500 sur /metrics

**Diagnostic** :
```bash
curl -v http://localhost:8000/metrics
```

**Solutions** :
1. Vérifier import `lunar_interpretation_generator` dans `main.py`
2. Vérifier prometheus-client installé : `pip show prometheus-client`
3. Vérifier logs : `tail -f /var/log/api.log | grep metrics`

---

## 📈 Optimisations Post-Déploiement

### Semaine 1 : Monitoring
- ✅ Vérifier métriques quotidiennement
- ✅ Ajuster alerts si faux positifs
- ✅ Analyser qualité (user feedback)

### Semaine 2 : Optimisations
- ⚙️ Évaluer switch Opus → Sonnet si budget serré
- ⚙️ Augmenter cache TTL si applicable
- ⚙️ Optimiser pool DB si goulot d'étranglement

### Mois 1 : Analyse
- 📊 Cache hit rate stable >70%
- 📊 Coût/user <$0.05/mois
- 📊 P95 latency <10s
- 📊 User satisfaction >4/5

---

## 📞 Support

**Erreurs Claude API** :
- Anthropic Support : support@anthropic.com
- Status page : https://status.anthropic.com

**Erreurs Application** :
- Logs : `tail -f /var/log/api.log`
- Métriques : Grafana dashboard
- Documentation : `docs/CLAUDE.md`

**Budget Alerts** :
- Anthropic dashboard : https://console.anthropic.com/settings/cost
- Prometheus alert : `#alerts-prod` Slack channel

---

## ✅ Validation Déploiement Réussi

**24h après déploiement** :
- ✅ 0 downtime
- ✅ >100 générations Claude réussies
- ✅ Cache hit rate >10% (et augmente)
- ✅ Coût <$5/jour
- ✅ Taux erreur <5%
- ✅ P95 latency <15s
- ✅ User feedback positif

**🎉 Déploiement validé - Système production ready !**

---

**Dernière mise à jour** : 2026-01-24
**Auteur** : Claude Opus 4.5
**Version** : 1.0
