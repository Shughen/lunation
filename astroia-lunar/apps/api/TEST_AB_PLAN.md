# Plan Tests A/B - Opus vs Sonnet

**Date** : 2026-01-24
**Objectif** : Évaluer si Sonnet peut remplacer Opus (-40% coûts, économie $4,800/an pour 5K users)
**Durée estimée** : 30-60 minutes

---

## 🎯 Critères de Décision

### Switch vers Sonnet SI :
- ✅ Qualité Sonnet ≥ 90% Opus (score /30)
- ✅ Longueur Sonnet ≥ 1,000 chars
- ✅ Latence Sonnet < 10s (vs 12s Opus)
- ✅ Coût confirmé : -40% ($0.012 vs $0.020 sans caching)

### Rester sur Opus SI :
- ❌ Qualité Sonnet < 80% Opus
- ❌ Feedback négatif sur ton/profondeur
- ❌ Latence Sonnet > Opus (rare)

---

## 📋 Phase 1 : Génération Échantillon Opus (5-10 min)

**Objectif** : Générer 50 interprétations avec Opus pour référence

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

# Configuration actuelle : OPUS (déjà configuré)
python3 -c "from config import settings; print(f'Modèle actuel: {settings.LUNAR_CLAUDE_MODEL}')"
# Expected: opus

# Générer 50 échantillons Opus
python scripts/ab_test_generate_sample.py --model opus --count 50

# Résultat attendu :
# ✅ 50/50 générations réussies
# Durée moyenne : ~10-12s/génération
# Coût estimé : ~$0.10 (avec caching)
```

**Vérification** :
```bash
# Compter générations Opus
python scripts/ab_test_generate_sample.py --stats
# Expected : Opus = 50 générations
```

---

## 📋 Phase 2 : Génération Échantillon Sonnet (5-10 min)

**Objectif** : Générer 50 interprétations avec Sonnet pour comparaison

```bash
# Générer 50 échantillons Sonnet
python scripts/ab_test_generate_sample.py --model sonnet --count 50

# Résultat attendu :
# ✅ 50/50 générations réussies
# Durée moyenne : ~5-8s/génération (plus rapide qu'Opus)
# Coût estimé : ~$0.06 (avec caching, -40% vs Opus)
```

**Vérification** :
```bash
# Stats comparatives
python scripts/ab_test_generate_sample.py --stats

# Expected :
# Opus   : 50 générations, avg_length ~1200 chars, avg_duration ~11s
# Sonnet : 50 générations, avg_length ~1000-1200 chars, avg_duration ~6-8s
```

---

## 📋 Phase 3 : Analyse Quantitative (2 min)

**Objectif** : Comparer métriques objectives (longueur, durée, coût)

```bash
# Analyse statistique comparative
python scripts/ab_test_analyze.py --cost

# Métriques clés :
# - Longueur moyenne Sonnet ≥ 1,000 chars ? ✅/❌
# - Durée moyenne Sonnet < Opus ? ✅/❌ (attendu : OUI)
# - Coût Sonnet = -40% vs Opus ? ✅/❌ (attendu : OUI)
```

**Export données (optionnel)** :
```bash
# Export CSV pour analyse Excel/Google Sheets
python scripts/ab_test_analyze.py --raw ab_test_data.csv
```

---

## 📋 Phase 4 : Analyse Qualitative (15-30 min)

**Objectif** : Comparer qualité narrative (ton, cohérence, conseils)

```bash
# Générer rapport comparatif (20 paires)
python scripts/ab_test_analyze.py --sample 20 --export ab_test_report.md

# Ouvrir rapport
open ab_test_report.md
# ou
cat ab_test_report.md | less
```

**Évaluation manuelle** :

Pour **chaque paire** (Opus vs Sonnet), noter sur la grille :

| Critère | Opus | Sonnet | Gagnant |
|---------|------|--------|---------|
| **Ton chaleureux** (1-5) | | | |
| **Cohérence astro** (1-5) | | | |
| **Conseils actionnables** (1-5) | | | |
| **Richesse vocabulaire** (1-5) | | | |
| **Structure claire** (1-5) | | | |
| **Inspiration** (1-5) | | | |
| **TOTAL** (/30) | | | |

**Critères d'évaluation** :

- **Ton chaleureux** : Tutoiement, empathie, chaleur
- **Cohérence astro** : Lien clair avec Moon sign + House + Ascendant
- **Conseils actionnables** : Conseils concrets, pas juste descriptif
- **Richesse vocabulaire** : Variété, expressivité, évite répétitions
- **Structure claire** : Organisation logique (Tonalité → Ressources → Défis)
- **Inspiration** : Capacité à inspirer, donner envie d'agir

---

## 📋 Phase 5 : Décision (5 min)

### Calcul Score Moyen

Sur les 20 paires évaluées :

```
Score moyen Opus   : XX/30
Score moyen Sonnet : XX/30
Ratio qualité      : XX% (Sonnet/Opus)
```

### Décision Finale

**Scénario 1 : Ratio ≥ 90%** → ✅ **SWITCH SONNET**
```bash
# Modifier .env production
# LUNAR_CLAUDE_MODEL=sonnet

# Économie annuelle :
# - 1,000 users : $10/an
# - 5,000 users : $48/an
# - 10,000 users : $96/an
```

**Scénario 2 : Ratio 80-89%** → ⚙️ **HYBRIDE**
```bash
# Opus pour "full", Sonnet pour autres
# Modifier lunar_interpretation_generator.py

# Économie partielle : ~20-30%
```

**Scénario 3 : Ratio < 80%** → ❌ **RESTER OPUS**
```bash
# Pas de changement
# Qualité prioritaire sur coût
```

---

## 📊 Rapport Final

**Template à remplir** :

```markdown
# Rapport Tests A/B - Opus vs Sonnet
**Date** : 2026-01-24
**Échantillon** : 50 Opus + 50 Sonnet

## Métriques Quantitatives
| Métrique | Opus | Sonnet | Écart |
|----------|------|--------|-------|
| Générations | 50 | 50 | - |
| Longueur moy. | XXX chars | XXX chars | -X% |
| Durée moy. | XX.Xs | XX.Xs | -X% |
| Coût total | $X.XX | $X.XX | -40% |

## Métriques Qualitatives (20 paires)
| Critère | Opus | Sonnet | Écart |
|---------|------|--------|-------|
| Ton chaleureux | X.X/5 | X.X/5 | -X% |
| Cohérence astro | X.X/5 | X.X/5 | -X% |
| Score total | XX/30 | XX/30 | -X% |

## Décision
☑️ Switch Sonnet / ☐ Hybride / ☐ Rester Opus

**Justification** : [Explication]

## Impact Économique
- Économie mensuelle (5K users) : $X.XX
- Économie annuelle : $X.XX
- ROI : XXX%
```

---

## 🚀 Actions Post-Décision

### Si Switch Sonnet ✅

1. **Modifier .env production** :
   ```bash
   LUNAR_CLAUDE_MODEL=sonnet
   ```

2. **Tester en production** :
   ```bash
   # Générer 1 interprétation test
   curl -X POST https://api.astroia.com/api/lunar-returns/current \
     -H "Authorization: Bearer $JWT" \
     | jq '.metadata.model_used'
   # Expected: "claude-sonnet-4-5-20250929"
   ```

3. **Monitoring 24h** :
   - Vérifier métriques Grafana
   - Vérifier coûts Anthropic dashboard
   - Vérifier user feedback

4. **Rollback si problème** :
   ```bash
   # Restaurer Opus
   LUNAR_CLAUDE_MODEL=opus
   ```

### Si Hybride ⚙️

Modifier `services/lunar_interpretation_generator.py` :

```python
def get_configured_model(subject: str) -> str:
    """Hybrid: Opus for full, Sonnet for others"""
    if subject == 'full':
        return CLAUDE_MODELS['opus']
    else:
        return CLAUDE_MODELS['sonnet']
```

### Si Rester Opus ❌

- Aucune action
- Documenter résultats tests A/B
- Re-tester dans 3-6 mois (évolution modèles)

---

**Prêt à lancer les tests ?** Commencez par Phase 1 ! 🚀
