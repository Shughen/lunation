# 🌊 Vague 4 : Testing & QA - Prompts Agents IA

**Durée totale** : 2h en parallèle (3 agents)
**Prérequis** : Vague 3 terminée (routes API complètes)
**Objectif** : Valider la qualité, la performance et l'intégration complète du système V2

---

## 📋 Vue d'ensemble Vague 4

| Agent | Tâche | Durée | Fichiers principaux |
|-------|-------|-------|---------------------|
| Agent A | Task 3.4 : Tests E2E routes | 2h | `tests/test_lunar_routes_e2e.py` |
| Agent B | Task 4.1 : Tests intégration | 1h30 | `tests/test_lunar_integration.py` |
| Agent C | Task 4.2 : Benchmarks performance | 1h30 | `tests/test_lunar_performance.py`, `docs/PERFORMANCE_BENCHMARKS.md` |

---

## 🤖 Agent A - Task 3.4 : Tests E2E Routes API (2h)

### 📊 Contexte

Tu es l'Agent A de la Vague 4. Ta mission est de créer des tests end-to-end complets pour valider que toutes les routes API de la Vague 3 fonctionnent correctement ensemble.

**Prérequis complétés** :
- ✅ Vague 3 terminée : 3 routes API créées
  - GET /api/lunar-returns/current/report (Agent A, 3.1)
  - POST /api/lunar/interpretation/regenerate (Agent B, 3.2)
  - GET /api/lunar/interpretation/metadata (Agent C, 3.3)
- ✅ Service generator V2 opérationnel avec fallbacks
- ✅ Tests unitaires existants (514 passed)

### 🎯 Objectif

Créer des tests E2E qui valident les scénarios utilisateur complets, de bout en bout.

### 📝 Tâches principales

#### 1. Créer fichier `tests/test_lunar_routes_e2e.py` (1h)

**Tests à implémenter** (minimum 10 tests) :

**a) Scénario complet génération → metadata (3 tests)** :
```python
@pytest.mark.asyncio
async def test_e2e_generate_and_check_metadata(override_dependencies):
    """
    Scénario complet :
    1. Générer une interprétation via GET /lunar-returns/current/report
    2. Vérifier metadata via GET /interpretation/metadata
    3. Valider que total_interpretations a augmenté
    """
    # Step 1: Première lecture metadata (baseline)
    # Step 2: Générer interprétation
    # Step 3: Seconde lecture metadata (vérifier +1)
    pass

@pytest.mark.asyncio
async def test_e2e_multiple_generations_models_used(override_dependencies):
    """
    Générer plusieurs interprétations et vérifier que models_used
    reflète correctement la distribution.
    """
    pass

@pytest.mark.asyncio
async def test_e2e_cached_rate_calculation(override_dependencies):
    """
    Générer interprétations, attendre >1h, générer à nouveau,
    vérifier que cached_rate est calculé correctement.
    """
    pass
```

**b) Scénario régénération forcée (3 tests)** :
```python
@pytest.mark.asyncio
async def test_e2e_force_regenerate_bypasses_cache(override_dependencies):
    """
    1. Générer interprétation normale
    2. Force regenerate avec POST /regenerate
    3. Vérifier que metadata.forced = True
    4. Vérifier que nouvelle version créée en DB
    """
    pass

@pytest.mark.asyncio
async def test_e2e_regenerate_updates_model_used(override_dependencies):
    """
    Régénérer plusieurs fois et vérifier que model_used
    dans metadata est mis à jour.
    """
    pass

@pytest.mark.asyncio
async def test_e2e_regenerate_ownership_check(override_dependencies):
    """
    Vérifier que user A ne peut pas régénérer
    l'interprétation de user B (403 Forbidden).
    """
    pass
```

**c) Tests d'intégration metadata (2 tests)** :
```python
@pytest.mark.asyncio
async def test_e2e_metadata_cache_invalidation(override_dependencies):
    """
    1. GET metadata (mise en cache)
    2. Générer nouvelle interprétation
    3. GET metadata (doit être rafraîchi si >10min)
    """
    pass

@pytest.mark.asyncio
async def test_e2e_metadata_empty_then_populated(override_dependencies):
    """
    Nouvel utilisateur :
    1. GET metadata → total=0
    2. Générer interprétation
    3. GET metadata → total=1, models_used=[...]
    """
    pass
```

**d) Tests fallback hierarchy (2 tests)** :
```python
@pytest.mark.asyncio
async def test_e2e_fallback_to_template_on_claude_failure(override_dependencies):
    """
    Simuler échec Claude API, vérifier que fallback
    vers template fonctionne et metadata.source = 'db_template'.
    """
    pass

@pytest.mark.asyncio
async def test_e2e_metadata_reflects_fallback_source(override_dependencies):
    """
    Générer avec différents fallbacks, vérifier que
    metadata reflète correctement la source utilisée.
    """
    pass
```

#### 2. Validation et documentation (30min)

**a) Exécuter tous les tests E2E** :
```bash
pytest tests/test_lunar_routes_e2e.py -v
# Objectif : 10+ tests passed
```

**b) Vérifier compatibilité avec suite existante** :
```bash
pytest -q
# Objectif : Aucune régression (514+ passed)
```

**c) Documenter les scénarios** :
Ajouter docstrings détaillés expliquant :
- Le scénario utilisateur
- Les étapes de validation
- Les assertions critiques

#### 3. Gestion des erreurs et edge cases (30min)

**Tests edge cases** :
```python
@pytest.mark.asyncio
async def test_e2e_concurrent_requests_same_user():
    """Vérifier que requêtes concurrentes ne causent pas de race conditions."""
    pass

@pytest.mark.asyncio
async def test_e2e_metadata_after_db_failure():
    """Vérifier fallback sur cache expiré si DB inaccessible."""
    pass
```

### 📦 Livrables

1. ✅ Fichier `tests/test_lunar_routes_e2e.py` avec 10+ tests
2. ✅ Tous tests E2E passent (10+ passed)
3. ✅ Aucune régression dans suite existante (pytest -q)
4. ✅ Documentation claire des scénarios dans docstrings

### 🎯 Critères de succès

- [ ] 10+ tests E2E créés
- [ ] Tous tests passent sans erreur
- [ ] Code coverage E2E > 80% sur routes testées
- [ ] Aucune régression dans suite existante
- [ ] Docstrings complètes et claires

### 📚 Références

**Fichiers à étudier** :
- `routes/lunar.py` : Endpoint GET /metadata
- `routes/lunar_returns.py` : Endpoints avec metadata V2
- `services/lunar_interpretation_generator.py` : Service génération
- `tests/test_auth_protected_routes.py` : Exemples tests auth
- `tests/conftest.py` : Fixtures disponibles

**Pattern de test E2E** :
```python
@pytest.mark.asyncio
async def test_e2e_scenario_name(override_dependencies):
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Step 1: Setup
        # Step 2: Action
        # Step 3: Validation
        pass
```

---

## 🤖 Agent B - Task 4.1 : Tests Intégration Service → DB (1h30)

### 📊 Contexte

Tu es l'Agent B de la Vague 4. Ta mission est de créer des tests d'intégration qui valident l'interaction entre le service generator et la base de données, sans passer par les routes HTTP.

**Prérequis complétés** :
- ✅ Service `lunar_interpretation_generator.py` enrichi (Vague 1, 2.1)
- ✅ Tests unitaires generator (33 tests, Vague 2, 2.4)
- ✅ Modèles DB LunarInterpretation + LunarInterpretationTemplate

### 🎯 Objectif

Valider que le service generator interagit correctement avec la base de données dans tous les scénarios (cache hit, miss, fallback, erreurs).

### 📝 Tâches principales

#### 1. Créer fichier `tests/test_lunar_integration.py` (1h)

**Tests à implémenter** (minimum 8 tests) :

**a) Tests cache DB temporelle (3 tests)** :
```python
@pytest.mark.asyncio
async def test_integration_cache_hit_from_db():
    """
    1. Créer LunarInterpretation en DB
    2. Appeler generate_or_get_interpretation()
    3. Vérifier cache hit (pas de nouvelle génération)
    4. Vérifier source = 'db_temporal'
    """
    pass

@pytest.mark.asyncio
async def test_integration_idempotence_constraint():
    """
    Vérifier que contrainte UNIQUE (lunar_return_id, subject, lang, version)
    empêche les doublons.
    """
    pass

@pytest.mark.asyncio
async def test_integration_cache_miss_creates_new():
    """
    1. DB vide
    2. Appeler generate_or_get_interpretation()
    3. Vérifier nouvelle entrée créée en DB
    4. Vérifier input_json + output_text sauvegardés
    """
    pass
```

**b) Tests fallback templates (2 tests)** :
```python
@pytest.mark.asyncio
async def test_integration_fallback_to_template():
    """
    1. Simuler échec Claude (timeout)
    2. Vérifier fallback vers LunarInterpretationTemplate
    3. Vérifier source = 'db_template'
    """
    pass

@pytest.mark.asyncio
async def test_integration_template_lookup():
    """
    Créer template en DB avec combinaison spécifique,
    vérifier qu'il est trouvé et utilisé correctement.
    """
    pass
```

**c) Tests metadata persistence (2 tests)** :
```python
@pytest.mark.asyncio
async def test_integration_metadata_saved_to_db():
    """
    Générer interprétation, vérifier que model_used,
    created_at, version sont sauvegardés en DB.
    """
    pass

@pytest.mark.asyncio
async def test_integration_weekly_advice_persistence():
    """
    Vérifier que weekly_advice (JSONB) est sauvegardé
    et récupéré correctement de la DB.
    """
    pass
```

**d) Tests force_regenerate (1 test)** :
```python
@pytest.mark.asyncio
async def test_integration_force_regenerate_bypasses_cache():
    """
    1. Cache hit normal
    2. force_regenerate=True → nouvelle génération
    3. Vérifier nouvelle entrée DB créée
    """
    pass
```

#### 2. Tests avec DB réelle (optionnel mais recommandé) (15min)

Si possible, créer quelques tests avec connexion DB réelle Supabase :

```python
@pytest.mark.skipif(not DB_AVAILABLE, reason="DB Supabase non accessible")
@pytest.mark.asyncio
async def test_integration_real_db_save_and_retrieve():
    """
    Test avec vraie DB Supabase :
    1. Sauvegarder interprétation
    2. Récupérer depuis DB
    3. Vérifier intégrité données
    4. Cleanup
    """
    pass
```

#### 3. Validation et documentation (15min)

**a) Exécuter tests intégration** :
```bash
pytest tests/test_lunar_integration.py -v
# Objectif : 8+ tests passed
```

**b) Vérifier compatibilité** :
```bash
pytest -q
# Objectif : Aucune régression
```

**c) Documenter patterns d'intégration** :
Ajouter commentaires expliquant :
- Setup DB pour tests
- Mocking vs vraie DB
- Cleanup après tests

### 📦 Livrables

1. ✅ Fichier `tests/test_lunar_integration.py` avec 8+ tests
2. ✅ Tests intégration passent (8+ passed)
3. ✅ Documentation patterns d'intégration
4. ✅ Aucune régression dans suite existante

### 🎯 Critères de succès

- [ ] 8+ tests d'intégration créés
- [ ] Tous tests passent sans erreur
- [ ] Coverage intégration service/DB > 70%
- [ ] Aucune régression dans suite existante
- [ ] Documentation claire des patterns

### 📚 Références

**Fichiers à étudier** :
- `services/lunar_interpretation_generator.py` : Service à tester
- `models/lunar_interpretation.py` : Modèle DB temporelle
- `models/lunar_interpretation_template.py` : Modèle templates
- `tests/test_lunar_interpretation_generator.py` : Tests unitaires existants
- `tests/conftest.py` : Fixtures DB disponibles

**Pattern de test intégration** :
```python
@pytest.mark.asyncio
async def test_integration_scenario(db_session):
    # Setup DB state
    # Call service
    # Verify DB state changed
    # Cleanup
    pass
```

---

## 🤖 Agent C - Task 4.2 : Benchmarks Performance (1h30)

### 📊 Contexte

Tu es l'Agent C de la Vague 4. Ta mission est de créer des benchmarks de performance pour mesurer et documenter les performances du système V2.

**Prérequis complétés** :
- ✅ Routes API complètes avec cache (Vague 3)
- ✅ Indexes DB existants (user_id, created_at, model_used)
- ✅ Cache applicatif (TTL 10min pour metadata)

### 🎯 Objectif

Mesurer et documenter les performances du système pour identifier les optimisations futures et établir des baselines.

### 📝 Tâches principales

#### 1. Créer fichier `tests/test_lunar_performance.py` (45min)

**Benchmarks à implémenter** (minimum 6 benchmarks) :

**a) Benchmarks cache (2 benchmarks)** :
```python
@pytest.mark.asyncio
async def test_benchmark_metadata_cache_hit():
    """
    Mesurer temps de réponse GET /metadata avec cache hit.

    Objectif : < 50ms
    """
    import time

    # Warmup cache
    # Mesurer 100 requêtes avec cache hit
    # Calculer moyenne, min, max, p95, p99
    # Assert moyenne < 50ms
    pass

@pytest.mark.asyncio
async def test_benchmark_metadata_cache_miss():
    """
    Mesurer temps de réponse GET /metadata avec cache miss (calcul DB).

    Objectif : < 200ms
    """
    # Clear cache
    # Mesurer 10 requêtes avec cache miss
    # Calculer moyenne
    # Assert moyenne < 200ms
    pass
```

**b) Benchmarks génération (2 benchmarks)** :
```python
@pytest.mark.asyncio
async def test_benchmark_generation_db_cache_hit():
    """
    Mesurer temps génération avec cache DB temporelle.

    Objectif : < 100ms
    """
    # Créer LunarInterpretation en DB
    # Mesurer 50 générations (toutes cache hits)
    # Assert moyenne < 100ms
    pass

@pytest.mark.asyncio
async def test_benchmark_generation_template_fallback():
    """
    Mesurer temps génération avec fallback template.

    Objectif : < 300ms
    """
    # Mock échec Claude
    # Mesurer 20 générations (fallback template)
    # Assert moyenne < 300ms
    pass
```

**c) Benchmarks requêtes DB (2 benchmarks)** :
```python
@pytest.mark.asyncio
async def test_benchmark_db_query_with_indexes():
    """
    Mesurer performance requêtes SQL avec indexes.

    - COUNT(*) WHERE user_id = X
    - GROUP BY model_used
    - MAX(created_at) WHERE user_id = X

    Objectif : < 50ms par requête
    """
    pass

@pytest.mark.asyncio
async def test_benchmark_concurrent_metadata_requests():
    """
    Mesurer performance avec 10 requêtes concurrentes.

    Objectif : < 500ms pour toutes (p95)
    """
    import asyncio

    # Lancer 10 requêtes en parallèle
    # Mesurer temps total
    # Assert p95 < 500ms
    pass
```

#### 2. Créer documentation `docs/PERFORMANCE_BENCHMARKS.md` (30min)

**Structure du document** :

```markdown
# Performance Benchmarks - Lunar Interpretation V2

**Date** : 2026-01-23
**Version** : V2 (Sprint 5 Vague 4)
**Environment** : Test local (MacBook M1, SQLite in-memory)

## 📊 Résultats Benchmarks

### Cache Performance

| Endpoint | Scénario | Moyenne | P95 | P99 | Objectif | Status |
|----------|----------|---------|-----|-----|----------|--------|
| GET /metadata | Cache hit | Xms | Xms | Xms | < 50ms | ✅ |
| GET /metadata | Cache miss | Xms | Xms | Xms | < 200ms | ✅ |

### Génération Performance

| Scénario | Moyenne | P95 | P99 | Objectif | Status |
|----------|---------|-----|-----|----------|--------|
| DB cache hit | Xms | Xms | Xms | < 100ms | ✅ |
| Template fallback | Xms | Xms | Xms | < 300ms | ✅ |

### Requêtes DB Performance

| Requête | Moyenne | Objectif | Status |
|---------|---------|----------|--------|
| COUNT user_id | Xms | < 50ms | ✅ |
| GROUP BY model_used | Xms | < 50ms | ✅ |
| MAX created_at | Xms | < 50ms | ✅ |

## 🎯 Optimisations Recommandées

### Court terme
- [ ] Optimisation 1 (si benchmark échoue)
- [ ] Optimisation 2

### Long terme
- [ ] Migration vers PostgreSQL production (vs SQLite test)
- [ ] Ajout index composite si nécessaire

## 📈 Evolution

| Date | Version | Amélioration | Note |
|------|---------|--------------|------|
| 2026-01-23 | V2 Initial | Baseline établie | - |

## 🔍 Méthodologie

**Setup** :
- Environment : MacBook M1, 16GB RAM
- DB : SQLite in-memory (tests)
- Python : 3.10.11
- FastAPI : 0.109.0

**Mesures** :
- Moyenne : Mean de N requêtes
- P95 : 95th percentile
- P99 : 99th percentile

**Données de test** :
- 100 interprétations pré-créées
- 5 utilisateurs différents
```

#### 3. Analyse et recommandations (15min)

**a) Analyser les résultats** :
- Identifier les bottlenecks
- Comparer avec objectifs
- Noter les déviations

**b) Recommandations d'optimisation** :
```markdown
## Recommandations

### Si metadata cache miss > 200ms
- [ ] Vérifier si indexes sont utilisés (EXPLAIN ANALYZE)
- [ ] Considérer index composite (user_id, created_at)

### Si génération template > 300ms
- [ ] Profiler lookup template
- [ ] Optimiser requête SELECT template

### Si requêtes concurrentes > 500ms
- [ ] Vérifier connection pool size
- [ ] Tester avec connection pooling optimisé
```

### 📦 Livrables

1. ✅ Fichier `tests/test_lunar_performance.py` avec 6+ benchmarks
2. ✅ Document `docs/PERFORMANCE_BENCHMARKS.md` avec résultats
3. ✅ Recommandations d'optimisation documentées
4. ✅ Tous benchmarks exécutés avec succès

### 🎯 Critères de succès

- [ ] 6+ benchmarks créés
- [ ] Tous benchmarks exécutables (même si échouent)
- [ ] Résultats documentés dans PERFORMANCE_BENCHMARKS.md
- [ ] Recommandations d'optimisation claires
- [ ] Baselines établies pour tracking futur

### 📚 Références

**Fichiers à étudier** :
- `routes/lunar.py` : Endpoints à benchmarker
- `services/lunar_interpretation_generator.py` : Service génération
- `models/lunar_interpretation.py` : Requêtes DB à mesurer
- `services/interpretation_cache_service.py` : Cache à mesurer

**Libraries utiles** :
```python
import time
import asyncio
from statistics import mean, stdev
import pytest

# Exemple de benchmark
start = time.perf_counter()
# ... code à mesurer
elapsed = time.perf_counter() - start
```

**Percentiles** :
```python
import numpy as np

times = [...]  # Liste de temps mesurés
p95 = np.percentile(times, 95)
p99 = np.percentile(times, 99)
```

---

## 📋 Checklist Vague 4

### Agent A (Tests E2E)
- [ ] Fichier test_lunar_routes_e2e.py créé
- [ ] 10+ tests E2E implémentés
- [ ] Tous tests passent
- [ ] Aucune régression (pytest -q)
- [ ] Docstrings complètes
- [ ] Commit: `test(api): ajouter tests E2E routes lunar V2`

### Agent B (Tests Intégration)
- [ ] Fichier test_lunar_integration.py créé
- [ ] 8+ tests intégration implémentés
- [ ] Tous tests passent
- [ ] Patterns d'intégration documentés
- [ ] Aucune régression (pytest -q)
- [ ] Commit: `test(api): ajouter tests intégration service/DB V2`

### Agent C (Benchmarks Performance)
- [ ] Fichier test_lunar_performance.py créé
- [ ] 6+ benchmarks implémentés
- [ ] Document PERFORMANCE_BENCHMARKS.md créé
- [ ] Résultats documentés
- [ ] Recommandations rédigées
- [ ] Commit: `perf(api): ajouter benchmarks performance V2`

---

## 🎯 Coordination Inter-Agents

**Ordre d'exécution recommandé** :
1. **Parallèle** : Les 3 agents peuvent travailler en parallèle (pas de dépendances)
2. **Review croisée** : Chaque agent peut relire les tests des autres
3. **Validation finale** : Un agent valide que pytest -q passe pour tous

**Communication** :
- Si un agent découvre un bug, le signaler immédiatement
- Si un test échoue, débugger avant de passer à la suite
- Partager les patterns de test utiles

**Validation finale** (après les 3 agents) :
```bash
# Exécuter toute la suite
pytest -v

# Objectif : 530+ tests passed (514 + 16 nouveaux minimum)
# Vérifier : 0 failed
```

---

## 📚 Ressources Communes

**Documentation à consulter** :
- `.claude/CLAUDE.md` : État du projet
- `docs/MIGRATION_PLAN.md` : Plan migration V2
- `docs/LUNAR_ARCHITECTURE_V2.md` : Architecture V2

**Commandes utiles** :
```bash
# Lancer tests d'un agent spécifique
pytest tests/test_lunar_routes_e2e.py -v
pytest tests/test_lunar_integration.py -v
pytest tests/test_lunar_performance.py -v

# Coverage pour un fichier
pytest tests/test_lunar_routes_e2e.py --cov=routes.lunar --cov-report=term

# Profiling performance
pytest tests/test_lunar_performance.py --durations=10
```

**Fixtures disponibles** (conftest.py) :
- `override_dependencies` : Override auth + DB
- `fake_user` : Mock User
- `FakeAsyncSession` : Mock DB session

---

**Bonne chance aux 3 agents ! 🚀**

La Vague 4 est critique pour garantir la qualité et la performance du système V2 avant la mise en production.
