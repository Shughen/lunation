# Astroia Lunar – Guide de Contribution

Ce document définit les conventions de développement, workflows Git et best practices pour contribuer au projet.

---

## 💡 Principes de Développement

### Quand travailler sur le backend

1. **Toujours lire avant de modifier** : Utiliser le tool Read avant toute modification
2. **Run tests après chaque changement** : `pytest -q`
3. **Commit atomique** : Un changement = un commit
4. **Ne pas refactor pendant un fix** : Focus sur le problème uniquement

### Quand NE PAS toucher le mobile

- ❌ Sauf demande explicite de l'utilisateur
- ❌ Ne pas "améliorer" le code frontend spontanément
- ❌ Ne pas synchroniser API changes avec mobile automatiquement

---

## 🔄 Workflow Git

### Principes

- ✅ **Un changement = un commit** (atomicité)
- ✅ Commits clairs et descriptifs (feat/fix/refactor/test/docs)
- ✅ Toujours run `pytest -q` avant commit
- ✅ Respecter le format de commit conventional

### Conventions de commits

```bash
# Format
<type>(<scope>): <message>

# Types
feat(api): ajouter endpoint X           # Nouvelle fonctionnalité
fix(api): corriger bug Y dans service Z # Correction de bug
test(api): ajouter tests pour X         # Ajout/modification tests
refactor(api): simplifier service Y     # Refactoring code
docs(api): documenter decision Z        # Documentation
perf(api): optimiser query X            # Optimisation performance
chore(api): mettre à jour dependencies  # Maintenance/tâches diverses

# Scopes
api      : Backend FastAPI
mobile   : Frontend React Native
docs     : Documentation
scripts  : Scripts utilitaires
tests    : Tests
ci       : CI/CD
```

### Exemples

```bash
# ✅ Bon
feat(api): ajouter endpoint POST /api/lunar/interpretation/regenerate
fix(api): corriger timeout génération Claude (30s max)
test(api): ajouter 11 tests E2E routes lunaires V2
refactor(api): simplifier lunar_report_builder avec fallback V2
docs(api): documenter architecture V2 (4 couches)
perf(api): cache RapidAPI Lunar Returns (TTL 30j, -60% API calls)

# ❌ Mauvais
update stuff                            # Trop vague
fix bug                                 # Pas de contexte
WIP                                     # Work in progress, pas pour main
Added new feature for lunar             # Anglais mixé avec scope manquant
```

### Workflow commit

```bash
# 1. Vérifier état
git status
git diff

# 2. Run tests
cd apps/api
pytest -q
# Expected: 484+ passed, <10 failed

# 3. Ajouter changements
git add <fichiers modifiés>

# 4. Commit avec message clair
git commit -m "feat(api): ajouter endpoint /metrics Prometheus

- 6 métriques exposées (generated, cache_hit, fallback, duration, active, migration_info)
- Tests : 11 passed (test_metrics_endpoint.py)
- Documentation : docs/PROMETHEUS_METRICS.md (322 lignes)"

# 5. Push
git push origin <branch>
```

---

## 🎨 Code Style

### Python (Backend)

```python
# Type hints partout (Python 3.11+)
def generate_interpretation(
    lunar_return_id: int,
    force_regenerate: bool = False
) -> tuple[str, str, dict, str]:
    """Generate lunar interpretation for given lunar return.

    Args:
        lunar_return_id: ID of the lunar return
        force_regenerate: Force new generation bypassing cache

    Returns:
        Tuple of (interpretation, weekly_advice, metadata, source)

    Raises:
        InvalidLunarReturnError: If lunar_return_id invalid
        ClaudeAPIError: If Claude API fails
    """
    pass

# Docstrings sur fonctions publiques
# Format: Google style docstring

# Async/await pour I/O operations
async def fetch_from_api(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

# Exception handling avec logs clairs
import structlog

logger = structlog.get_logger()

try:
    result = await generate_interpretation(lunar_return_id)
except ClaudeAPIError as e:
    logger.error("claude_api_error", error=str(e), lunar_return_id=lunar_return_id)
    # Fallback logic
    result = get_template_interpretation(lunar_return_id)
```

### TypeScript (Mobile)

```typescript
// Interfaces claires
interface LunarReport {
  lunarReturnId: number;
  interpretation: string;
  weeklyAdvice: string;
  metadata: {
    source: 'db_temporal' | 'claude' | 'db_template' | 'hardcoded';
    modelUsed: string;
    version: number;
    generatedAt: string;
  };
}

// Async/await pour appels API
const fetchLunarReport = async (userId: number): Promise<LunarReport> => {
  const response = await api.get(`/api/lunar-returns/current/report`);
  return response.data;
};

// Error handling
try {
  const report = await fetchLunarReport(userId);
  setReport(report);
} catch (error) {
  console.error('Failed to fetch lunar report:', error);
  setError('Impossible de charger ton rapport lunaire');
}
```

---

## 🧪 Tests

### Backend (pytest)

```bash
# Run tous les tests
cd apps/api
pytest -q                                    # Quick mode
pytest -v                                    # Verbose mode
pytest --lf                                  # Last failed only

# Run tests spécifiques
pytest tests/test_lunar_interpretation_generator.py -v
pytest tests/test_lunar_interpretation_generator.py::test_generate_with_cache -v

# Run avec coverage
pytest --cov=services --cov-report=html
```

### Patterns de tests

```python
import pytest
from unittest.mock import AsyncMock, MagicMock

# Tests unitaires
@pytest.mark.asyncio
async def test_generate_interpretation_with_cache():
    """Test génération avec cache hit."""
    # Arrange
    mock_db = AsyncMock()
    mock_db.scalar.return_value = cached_interpretation

    # Act
    result = await generate_interpretation(
        db=mock_db,
        lunar_return_id=123
    )

    # Assert
    assert result[0] == cached_interpretation.interpretation_full
    assert result[3] == "db_temporal"  # source

# Tests E2E
@pytest.mark.asyncio
async def test_e2e_regenerate_endpoint():
    """Test endpoint POST /regenerate."""
    response = await client.post(
        "/api/lunar/interpretation/regenerate",
        json={"lunar_return_id": 123},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    assert response.json()["metadata"]["source"] == "claude"

# Tests avec DB réelle (auto-skip si DB indisponible)
@pytest.mark.real_db
@pytest.mark.asyncio
async def test_lunar_interpretation_idempotence():
    """Test idempotence via UNIQUE constraint."""
    # Nécessite PostgreSQL réel
    # Auto-skip via pytest.skip() si DB indisponible
    pass
```

---

## 🎯 Priorités de Développement

1. **Correctif minimal** : Fix the bug, don't refactor the world
2. **Tests** : Ensure it works
3. **Refacto** : Only if necessary

### Anti-patterns

```python
# ❌ Mauvais : Refactor pendant un fix
def fix_bug_and_refactor_everything():
    # Fix bug
    # + Rename variables
    # + Extract functions
    # + Add type hints partout
    # + Rewrite logic complètement
    pass

# ✅ Bon : Focus sur le bug uniquement
def fix_bug():
    # Fix bug
    # Run tests
    # Commit
    pass

def refactor_code():
    # Refactor dans commit séparé
    # Si vraiment nécessaire
    pass
```

---

## 🚫 Zones de Travail

### Backend (`apps/api`)

- ✅ **Modifier librement** selon les règles ci-dessus
- ✅ Services, routes, models, tests
- ✅ Documentation technique
- ✅ Scripts utilitaires

### Mobile (`apps/mobile`)

- ❌ **NE PAS toucher** sauf demande explicite
- ❌ Ne pas synchroniser API changes automatiquement
- ❌ Ne pas "améliorer" le code frontend spontanément

---

## ✅ Definition of Done

### Backend

- [ ] `pytest -q` → 484+ passed (98.9%+)
- [ ] `curl http://localhost:8000/health` → 200 OK
- [ ] Aucun secret affiché/commité
- [ ] Tests auth OK
- [ ] Code respecte conventions (type hints, docstrings)
- [ ] Commit avec message clair
- [ ] Documentation mise à jour si nécessaire

### Mobile

- [ ] App démarre sans crash
- [ ] Écrans principaux accessibles
- [ ] Intégration API fonctionnelle
- [ ] **Aucun changement sauf demande explicite**

### Documentation

- [ ] CLAUDE.md à jour (si changements architecturaux)
- [ ] Commits clairs et atomiques
- [ ] README.md à jour si nécessaire
- [ ] SPRINTS_HISTORY.md à jour si fin de sprint

---

## 📚 Ressources Complémentaires

**Documentation** :
- `ARCHITECTURE.md` — Architecture complète
- `SPRINTS_HISTORY.md` — Historique des sprints
- `TROUBLESHOOTING.md` — Guide dépannage
- `CHANGELOG.md` — Historique commits

**Guides Techniques** :
- `LUNAR_ARCHITECTURE_V2.md` — Architecture V2 détaillée
- `MIGRATION_PLAN.md` — Plan migration V1→V2
- `API_LUNAR_V2.md` — Documentation API utilisateur
- `PROMETHEUS_METRICS.md` — Monitoring production
- `DEPLOYMENT_PRODUCTION.md` — Guide déploiement

---

**Dernière mise à jour** : 2026-01-24
