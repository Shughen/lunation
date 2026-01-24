# Guide Tests A/B - Opus vs Sonnet

**Date** : 2026-01-24
**Version** : 1.0
**Objectif** : Comparer qualité et coûts Claude Opus 4.5 vs Sonnet 4.5

---

## 📊 Comparatif Modèles

| Critère | **Opus 4.5** | **Sonnet 4.5** | **Haiku 3.5** |
|---------|--------------|----------------|---------------|
| **Qualité** | ⭐⭐⭐⭐⭐ Excellente | ⭐⭐⭐⭐ Très bonne | ⭐⭐⭐ Bonne |
| **Coût/génération** | $0.020 | $0.012 | $0.002 |
| **Économie vs Opus** | - | **-40%** | **-90%** |
| **Latence moyenne** | 10-12s | 5-8s | 2-4s |
| **Longueur output** | 1,200-1,400 chars | 1,000-1,200 chars | 800-1,000 chars |
| **Use case** | Production (qualité max) | A/B testing | Prototypage rapide |

---

## 🎯 Méthodologie Tests A/B

### Phase 1 : Configuration (1h)

**1.1 Backup configuration actuelle**
```bash
# Sauvegarder état Opus
cp .env .env.opus_backup
grep "LUNAR_CLAUDE_MODEL" .env >> ab_test_log.txt
```

**1.2 Activer Sonnet**
```bash
# Modifier .env
LUNAR_CLAUDE_MODEL=sonnet

# Redémarrer API
sudo systemctl restart api
# ou
kill -HUP <pid>
```

**1.3 Validation switch**
```bash
# Vérifier configuration chargée
python3 -c "
from config import settings
print(f'Model: {settings.LUNAR_CLAUDE_MODEL}')
# Expected: sonnet
"

# Tester génération
curl -X POST https://api.astroia.com/api/lunar-returns/current \
  -H "Authorization: Bearer $JWT" \
  | jq '.metadata.model_used'
# Expected: "claude-sonnet-4-5-20250929"
```

### Phase 2 : Génération Échantillon (2-3h)

**2.1 Générer 100 interprétations Sonnet**

Script de génération :
```bash
# Utiliser script POC modifié pour 100 générations
python scripts/test_claude_generation_poc.py --count 100 --model sonnet
```

**2.2 Stocker dans table séparée**
```sql
-- Créer table temporaire pour test A/B
CREATE TABLE IF NOT EXISTS lunar_interpretations_ab_test (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER NOT NULL,
    lunar_return_id INTEGER NOT NULL,
    model_tested VARCHAR(50) NOT NULL,  -- 'opus' | 'sonnet'
    output_text TEXT NOT NULL,
    weekly_advice JSONB,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index pour requêtes
CREATE INDEX idx_ab_test_model ON lunar_interpretations_ab_test(model_tested);
```

### Phase 3 : Analyse Quantitative (30min)

**3.1 Métriques Coût**
```sql
-- Coût total par modèle
SELECT
    model_tested,
    COUNT(*) as total_generations,
    CASE
        WHEN model_tested = 'opus' THEN COUNT(*) * 0.020
        WHEN model_tested = 'sonnet' THEN COUNT(*) * 0.012
    END as total_cost_usd
FROM lunar_interpretations_ab_test
GROUP BY model_tested;
```

**3.2 Métriques Qualité (longueur)**
```sql
-- Longueur moyenne par modèle
SELECT
    model_tested,
    COUNT(*) as count,
    AVG(LENGTH(output_text)) as avg_length,
    MIN(LENGTH(output_text)) as min_length,
    MAX(LENGTH(output_text)) as max_length,
    STDDEV(LENGTH(output_text)) as stddev_length
FROM lunar_interpretations_ab_test
GROUP BY model_tested;
```

**3.3 Métriques Performance**
```promql
# Latence P95 par modèle
histogram_quantile(0.95,
  rate(lunar_interpretation_duration_seconds_bucket{model=~"opus|sonnet"}[1h])
) by (model)

# Durée moyenne
avg by (model) (
  rate(lunar_interpretation_duration_seconds_sum[1h]) /
  rate(lunar_interpretation_duration_seconds_count[1h])
)
```

### Phase 4 : Analyse Qualitative (2-3h)

**4.1 Échantillonnage aléatoire**
```sql
-- Sélectionner 20 paires Opus/Sonnet pour même lunar_return_id
WITH sample AS (
    SELECT DISTINCT lunar_return_id
    FROM lunar_interpretations_ab_test
    GROUP BY lunar_return_id
    HAVING COUNT(DISTINCT model_tested) = 2  -- Les deux modèles ont généré
    ORDER BY RANDOM()
    LIMIT 20
)
SELECT
    a.lunar_return_id,
    a.model_tested,
    a.output_text,
    a.metadata
FROM lunar_interpretations_ab_test a
JOIN sample s ON a.lunar_return_id = s.lunar_return_id
ORDER BY a.lunar_return_id, a.model_tested;
```

**4.2 Grille d'évaluation**

Pour chaque paire (Opus vs Sonnet), évaluer :

| Critère | Opus | Sonnet | Gagnant |
|---------|------|--------|---------|
| **Ton chaleureux** (1-5) | | | |
| **Cohérence astro** (1-5) | | | |
| **Conseils actionnables** (1-5) | | | |
| **Richesse vocabulaire** (1-5) | | | |
| **Structure claire** (1-5) | | | |
| **Inspiration** (1-5) | | | |
| **TOTAL** (/30) | | | |

**4.3 Analyse différences**
```python
# Script analyse qualitative
import pandas as pd

# Charger échantillon
df = pd.read_sql("SELECT * FROM lunar_interpretations_ab_test WHERE ...", conn)

# Comparer longueur
df.groupby('model_tested')['output_text'].apply(lambda x: x.str.len().mean())

# Analyse sentiment (optionnel avec library)
# from textblob import TextBlob
# df['sentiment'] = df['output_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
```

### Phase 5 : Test Utilisateur (optionnel, 1 semaine)

**5.1 Split traffic 50/50**
```python
# Dans lunar_interpretation_generator.py
import random

def get_configured_model() -> str:
    """A/B test: 50% Opus, 50% Sonnet"""
    if random.random() < 0.5:
        return CLAUDE_MODELS['opus']
    else:
        return CLAUDE_MODELS['sonnet']
```

**5.2 Tracking user satisfaction**
```sql
-- Créer table feedback
CREATE TABLE lunar_interpretation_feedback (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER NOT NULL,
    lunar_return_id INTEGER NOT NULL,
    interpretation_id UUID NOT NULL,
    model_used VARCHAR(50),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    feedback_text TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Analyser satisfaction par modèle
SELECT
    model_used,
    COUNT(*) as total_ratings,
    AVG(rating) as avg_rating,
    STDDEV(rating) as stddev_rating
FROM lunar_interpretation_feedback
GROUP BY model_used;
```

---

## 📈 Résultats Attendus

### Scénario 1 : Sonnet équivalent (-40% coût)

**Métriques cibles** :
- ✅ Qualité Sonnet ≥ 90% Opus (score /30)
- ✅ Longueur Sonnet ≥ 1,000 chars
- ✅ User satisfaction Sonnet ≥ 4/5
- ✅ Coût : $0.012 vs $0.020 (**-40%**)

**Décision** : Switch to Sonnet en production ✅

### Scénario 2 : Sonnet inférieur (qualité)

**Métriques observées** :
- ⚠️ Qualité Sonnet < 80% Opus
- ⚠️ User satisfaction Sonnet < 3.5/5
- ⚠️ Feedback négatif sur ton/profondeur

**Décision** : Rester sur Opus ❌

### Scénario 3 : Hybride (best of both)

**Stratégie** :
- ✅ Sonnet pour `subject='climate'|'focus'|'approach'` (courts)
- ✅ Opus pour `subject='full'` (interprétation complète)
- 💰 Économie partielle : ~20-30%

```python
def get_configured_model(subject: str) -> str:
    """Hybrid strategy: Opus for full, Sonnet for others"""
    if subject == 'full':
        return CLAUDE_MODELS['opus']
    else:
        return CLAUDE_MODELS['sonnet']
```

---

## 💰 Impact Financier

### Projection Mensuelle (1,000 users actifs)

| Modèle | Générations/mois | Coût sans cache | Coût avec cache (-90%) | Économie vs Opus |
|--------|------------------|-----------------|------------------------|------------------|
| **Opus** | 1,000 | $20.00 | $2.00 | - |
| **Sonnet** | 1,000 | $12.00 | **$1.20** | **-40%** ($0.80/mois) |
| **Hybride** | 1,000 | $16.00 | **$1.60** | **-20%** ($0.40/mois) |

**Économie annuelle** (5,000 users) :
- Sonnet : **$4,800/an** (vs Opus)
- Hybride : **$2,400/an** (vs Opus)

---

## ✅ Checklist Validation

### Avant de switcher en production

- [ ] **100 générations Sonnet** testées
- [ ] **20 évaluations qualitatives** complétées
- [ ] **Métriques quantitatives** : longueur ≥ 1,000 chars
- [ ] **Latence P95** : < 10s (vs 12s Opus)
- [ ] **Coût validé** : -40% confirmé
- [ ] **Tests utilisateur** (optionnel) : satisfaction ≥ 4/5
- [ ] **Rollback plan** : .env.opus_backup disponible
- [ ] **Monitoring** : Alertes Prometheus configurées

### Switch to Sonnet

```bash
# 1. Backup Opus config
cp .env .env.opus_backup

# 2. Switch to Sonnet
echo "LUNAR_CLAUDE_MODEL=sonnet" >> .env

# 3. Redémarrer API
sudo systemctl restart api

# 4. Valider
curl /api/lunar-returns/current | jq '.metadata.model_used'
# Expected: "claude-sonnet-4-5-20250929"

# 5. Monitor 24h
# Vérifier métriques Grafana (coût, qualité, latence)
```

### Rollback si problème

```bash
# Restaurer Opus
cp .env.opus_backup .env
sudo systemctl restart api

# Valider
curl /api/lunar-returns/current | jq '.metadata.model_used'
# Expected: "claude-opus-4-5-20251101"
```

---

## 📊 Template Rapport A/B

```markdown
# Rapport Tests A/B - Opus vs Sonnet
**Date** : YYYY-MM-DD
**Durée test** : X jours
**Échantillon** : N générations

## Résumé Exécutif
- Gagnant : Opus | Sonnet | Hybride
- Économie mensuelle : $X.XX
- Recommandation : Switch | Rester | Hybride

## Métriques Quantitatives
| Métrique | Opus | Sonnet | Écart |
|----------|------|--------|-------|
| Générations | XX | XX | - |
| Coût total | $X.XX | $X.XX | -X% |
| Longueur moy. | XXX chars | XXX chars | -X% |
| Latence P95 | X.Xs | X.Xs | -X% |

## Métriques Qualitatives
| Critère | Opus | Sonnet | Écart |
|---------|------|--------|-------|
| Ton chaleureux | X/5 | X/5 | -X% |
| Cohérence astro | X/5 | X/5 | -X% |
| Score total | XX/30 | XX/30 | -X% |

## User Feedback (optionnel)
- Satisfaction Opus : X.X/5 (N ratings)
- Satisfaction Sonnet : X.X/5 (N ratings)
- Commentaires : [résumé]

## Recommandation Finale
[Justification détaillée]

## Plan d'Action
1. [ ] Action 1
2. [ ] Action 2
```

---

## 🔗 Ressources

- **Anthropic Pricing** : https://www.anthropic.com/pricing
- **Claude Models Comparison** : https://docs.anthropic.com/en/docs/models-overview
- **Prometheus Queries** : `docs/PROMETHEUS_METRICS.md`
- **Deployment Guide** : `docs/DEPLOYMENT_PRODUCTION.md`

---

**Dernière mise à jour** : 2026-01-24
**Auteur** : Claude Opus 4.5
**Version** : 1.0
