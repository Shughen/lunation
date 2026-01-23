# Prompts Vague 3 : API Routes

## 🎯 Contexte

**Vague 2 TERMINÉE** :
- ✅ Agent A : Task 2.2 complétée (lunar_report_builder refactoré avec V2)
- ✅ Agent B : Task 2.4 complétée (33 tests generator, 88% coverage)
- ✅ Agent C : Task 4.3 complétée (audit migration validé 1728/1728)

**Vague 3 - 3 tâches en parallèle** :
- Agent A : Task 3.1 (Update routes/lunar.py) - 1h30
- Agent B : Task 3.2 (Route POST /regenerate) - 1h30
- Agent C : Task 3.3 (Route GET /metadata) - 1h

**Dépendances satisfaites** :
- Task 2.2 (lunar_report_builder refactoré) ✅ terminée en Vague 2 → débloque 3.1
- Task 2.1 (generator enrichi) ✅ terminée en Vague 1 → débloque 3.2 et 3.3
- Vague 3 entièrement débloquée

---

## 🔧 Agent A - Task 3.1 : Update routes/lunar.py

### Objectif
Mettre à jour l'endpoint existant `/api/lunar-returns/current/report` pour exposer les metadata du nouveau système V2 (source, model_used, version, etc.).

### Contexte technique
- **Fichier cible** : `routes/lunar.py` (existant)
- **Service utilisé** : `services/lunar_report_builder.py` (déjà refactoré en Task 2.2)
- **Endpoints concernés** : Routes utilisant `build_lunar_report_v4_async()`
- **Objectif** : Exposer metadata dans réponses API

### Tâches détaillées

#### 1. Lire et comprendre routes/lunar.py (15min)

```bash
# Lire le fichier routes
cat routes/lunar.py | grep -A 20 "def.*report"

# Identifier les endpoints utilisant build_lunar_report_v4_async
grep -n "build_lunar_report_v4_async" routes/lunar.py
```

**Endpoints potentiels à vérifier** :
- `POST /api/lunar-returns/current/report`
- `POST /api/reports/lunar/{month}` (dans routes/reports.py)

#### 2. Mettre à jour endpoint principal (45min)

**Fichier** : `routes/lunar.py`

**Trouver la fonction endpoint** (probablement autour des lignes ~100-200) :

**AVANT** :
```python
@router.post("/returns/current/report")
async def get_lunar_return_report(
    request: LunarReturnReportRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # ... logique existante ...

    # Build report
    report = await build_lunar_report_v4_async(
        lunar_return=lunar_return,
        db=db
    )

    return JSONResponse({
        'report': report,
        'lunar_return_id': lunar_return.id
    })
```

**APRÈS** :
```python
@router.post("/returns/current/report")
async def get_lunar_return_report(
    request: LunarReturnReportRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # ... logique existante (inchangée) ...

    # Build report (déjà refactoré en Task 2.2)
    report = await build_lunar_report_v4_async(
        lunar_return=lunar_return,
        db=db
    )

    # Extraire metadata du report
    metadata = report.get('metadata', {
        'source': 'unknown',
        'model_used': None,
        'version': 2,
        'generated_at': datetime.utcnow().isoformat()
    })

    return JSONResponse({
        'report': report,
        'lunar_return_id': lunar_return.id,
        'metadata': metadata  # NOUVEAU : Exposer metadata V2
    })
```

#### 3. Vérifier routes/reports.py si nécessaire (15min)

**Fichier** : `routes/reports.py`

Si ce fichier utilise aussi `build_lunar_report_v4_async()`, appliquer la même modification :

```python
# Chercher usage de build_lunar_report_v4_async
grep -n "build_lunar_report_v4_async" routes/reports.py

# Si trouvé, ajouter metadata comme ci-dessus
```

#### 4. Ajouter logging pour debug (10min)

```python
import logging

logger = logging.getLogger(__name__)

# Dans la fonction endpoint, après génération report
logger.info(
    f"Lunar report generated for user {current_user.id}",
    extra={
        'user_id': current_user.id,
        'lunar_return_id': lunar_return.id,
        'source': metadata.get('source'),
        'model_used': metadata.get('model_used')
    }
)
```

#### 5. Tester l'endpoint (20min)

```bash
# Démarrer API
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Dans un autre terminal, tester avec curl
curl -X POST http://localhost:8000/api/lunar-returns/current/report \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "birth_datetime": "1990-01-15T10:30:00",
    "birth_location": {
      "latitude": 48.8566,
      "longitude": 2.3522,
      "city": "Paris"
    }
  }' | jq '.metadata'

# Vérifier que metadata est présente
```

**Tests existants** :
```bash
# Lancer tests routes lunaires
pytest tests/test_lunar_integration.py -v -k report
pytest tests/ -v -k lunar_return
```

### Critères de succès
- ✅ Endpoint `/api/lunar-returns/current/report` retourne metadata
- ✅ Metadata contient : source, model_used, version, generated_at
- ✅ Tests existants passent (pas de régression)
- ✅ Aucune modification de la logique métier (juste exposition metadata)
- ✅ Logs structurés ajoutés

### Livrables
- `routes/lunar.py` mis à jour
- (Optionnel) `routes/reports.py` mis à jour si nécessaire
- Tests validés
- Commit : `feat(api): exposer metadata V2 dans routes lunaires`

---

## 🆕 Agent B - Task 3.2 : Route POST /api/lunar/interpretation/regenerate

### Objectif
Créer un nouvel endpoint permettant de forcer la régénération d'une interprétation lunaire (cas d'usage : amélioration prompt, utilisateur insatisfait, debug).

### Contexte technique
- **Nouveau endpoint** : `POST /api/lunar/interpretation/regenerate`
- **Service utilisé** : `services/lunar_interpretation_generator.py` (enrichi en Vague 1)
- **Paramètre clé** : `force_regenerate=True`
- **Sécurité** : Vérifier ownership (user_id)

### Tâches détaillées

#### 1. Créer la route dans routes/lunar.py (45min)

**Ajouter après les routes existantes** (autour ligne ~200) :

```python
@router.post("/interpretation/regenerate", status_code=201)
async def regenerate_lunar_interpretation(
    lunar_return_id: int,
    subject: str = 'full',
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Force la régénération d'une interprétation lunaire

    Args:
        lunar_return_id: ID de la lunar return
        subject: Type d'interprétation ('full', 'climate', etc.)

    Returns:
        Nouvelle interprétation générée avec metadata

    Raises:
        404: Si lunar_return_id inexistant ou non accessible

    Cas d'usage:
        - Amélioration du prompt (nouvelle version)
        - Utilisateur insatisfait de la qualité
        - Debug/test génération Claude
    """
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from models.lunar_return import LunarReturn

    logger.info(
        f"Force regenerate requested by user {current_user.id} for lunar_return {lunar_return_id}",
        extra={'user_id': current_user.id, 'lunar_return_id': lunar_return_id}
    )

    # Vérifier que lunar_return existe et appartient à l'utilisateur
    lunar_return = await db.get(LunarReturn, lunar_return_id)

    if not lunar_return:
        raise HTTPException(status_code=404, detail="LunarReturn not found")

    if lunar_return.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to regenerate this interpretation"
        )

    # Forcer régénération (ignore cache DB temporelle)
    try:
        output, weekly, source, model = await generate_or_get_interpretation(
            db=db,
            lunar_return_id=lunar_return_id,
            user_id=current_user.id,
            subject=subject,
            force_regenerate=True  # KEY: Force regeneration
        )
    except Exception as e:
        logger.error(
            f"Failed to regenerate interpretation: {e}",
            extra={'lunar_return_id': lunar_return_id, 'error': str(e)}
        )
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

    logger.info(
        f"Interpretation regenerated successfully",
        extra={
            'lunar_return_id': lunar_return_id,
            'source': source,
            'model': model
        }
    )

    return {
        'interpretation': output,
        'weekly_advice': weekly,
        'metadata': {
            'source': source,
            'model_used': model,
            'subject': subject,
            'regenerated_at': datetime.utcnow().isoformat(),
            'forced': True
        }
    }
```

#### 2. Ajouter imports nécessaires (5min)

**En haut du fichier routes/lunar.py**, vérifier/ajouter :

```python
from datetime import datetime
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)
```

#### 3. Mettre à jour schemas si nécessaire (15min)

**Fichier** : `schemas/lunar.py` (optionnel, si on veut un schema structuré)

```python
from pydantic import BaseModel

class RegenerateInterpretationRequest(BaseModel):
    lunar_return_id: int
    subject: str = 'full'

class RegenerateInterpretationResponse(BaseModel):
    interpretation: str
    weekly_advice: dict
    metadata: dict
```

Puis utiliser dans la route :
```python
@router.post("/interpretation/regenerate", response_model=RegenerateInterpretationResponse)
async def regenerate_lunar_interpretation(
    request: RegenerateInterpretationRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # ...
```

#### 4. Tester l'endpoint (25min)

**Test manuel avec curl** :

```bash
# 1. Générer un JWT token
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password"}' | jq -r '.access_token'

# 2. Tester regenerate (remplacer TOKEN et lunar_return_id)
curl -X POST http://localhost:8000/api/lunar/interpretation/regenerate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{"lunar_return_id": 123, "subject": "full"}' | jq

# 3. Vérifier que metadata.forced = true
```

**Test unitaire** :

```python
# tests/test_lunar_routes.py (créer si n'existe pas)

import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_regenerate_interpretation_success():
    """Regenerate avec force_regenerate=True"""
    # Mock generate_or_get_interpretation
    with patch('services.lunar_interpretation_generator.generate_or_get_interpretation') as mock_gen:
        mock_gen.return_value = (
            "Nouvelle interprétation",
            {"week_1": "Conseil"},
            "claude",
            "claude-opus-4-5"
        )

        # Call endpoint
        response = client.post(
            "/api/lunar/interpretation/regenerate",
            json={"lunar_return_id": 1, "subject": "full"},
            headers={"Authorization": f"Bearer {jwt_token}"}
        )

        assert response.status_code == 201
        assert response.json()['metadata']['forced'] == True
        assert response.json()['metadata']['source'] == 'claude'


@pytest.mark.asyncio
async def test_regenerate_interpretation_forbidden():
    """Regenerate d'une lunar_return d'un autre user → 403"""
    # TODO: Implémenter
```

#### 5. Documentation (10min)

Ajouter dans la docstring de la route :

```python
"""
Force la régénération d'une interprétation lunaire

**Cas d'usage** :
- Amélioration du prompt (nouvelle version model)
- Utilisateur insatisfait de la qualité
- Debug/test génération Claude

**Comportement** :
- Ignore cache DB temporelle
- Force appel Claude Opus 4.5 (ou fallback templates si échec)
- Sauvegarde nouvelle version en DB
- Ancienne version reste en historique

**Rate limiting** :
- Recommandé : max 10 regenerates/jour par user (à implémenter si nécessaire)
"""
```

### Critères de succès
- ✅ Endpoint fonctionne (201 Created)
- ✅ `force_regenerate=True` utilisé correctement
- ✅ Ownership check (403 si pas le bon user)
- ✅ Logs structurés complets
- ✅ Tests unitaires passent
- ✅ Documentation inline claire

### Livrables
- `routes/lunar.py` avec nouveau endpoint
- (Optionnel) `schemas/lunar.py` mis à jour
- Tests créés
- Commit : `feat(api): ajouter endpoint POST /lunar/interpretation/regenerate`

---

## 📊 Agent C - Task 3.3 : Route GET /api/lunar/interpretation/metadata

### Objectif
Créer un endpoint de statistiques permettant à l'utilisateur de voir ses interprétations lunaires (nombre total, répartition sources, modèles utilisés, taux de cache).

### Contexte technique
- **Nouveau endpoint** : `GET /api/lunar/interpretation/metadata`
- **Type** : Read-only, stats agrégées
- **Table** : `lunar_interpretations` (V2)
- **Performance** : <100ms (requêtes optimisées)

### Tâches détaillées

#### 1. Créer la route dans routes/lunar.py (30min)

**Ajouter après les routes existantes** :

```python
@router.get("/interpretation/metadata")
async def get_lunar_interpretation_metadata(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Statistiques des interprétations lunaires de l'utilisateur

    Returns:
        - total_interpretations: Nombre total d'interprétations générées
        - models_used: Répartition par modèle (claude-opus-4-5, template, etc.)
        - sources: Répartition par source (db_temporal, claude, db_template, hardcoded)
        - cached_rate: Pourcentage de cache hits
        - last_generated: Date de dernière génération

    Performance: <100ms (requêtes optimisées avec indexes)
    """
    from sqlalchemy import func, select
    from models.lunar_interpretation import LunarInterpretation

    # Query 1: Count total
    total_query = select(func.count()).select_from(LunarInterpretation).where(
        LunarInterpretation.user_id == current_user.id
    )
    total = await db.scalar(total_query) or 0

    # Query 2: Répartition par modèle
    models_query = select(
        LunarInterpretation.model_used,
        func.count().label('count')
    ).where(
        LunarInterpretation.user_id == current_user.id
    ).group_by(LunarInterpretation.model_used)

    models_result = await db.execute(models_query)
    models_stats = {row.model_used: row.count for row in models_result}

    # Query 3: Dernière génération
    last_query = select(func.max(LunarInterpretation.created_at)).where(
        LunarInterpretation.user_id == current_user.id
    )
    last_generated = await db.scalar(last_query)

    # Calcul taux de cache (approximation: modèle "template" = cache)
    template_count = models_stats.get('template', 0)
    cached_rate = (template_count / total * 100) if total > 0 else 0

    return {
        'user_id': current_user.id,
        'total_interpretations': total,
        'models_used': models_stats,
        'cached_rate': round(cached_rate, 2),
        'last_generated': last_generated.isoformat() if last_generated else None,
        'stats': {
            'claude_generations': models_stats.get('claude-opus-4-5', 0) + models_stats.get('claude-sonnet-4-5', 0),
            'template_fallbacks': models_stats.get('template', 0),
            'other': sum(v for k, v in models_stats.items() if k not in ['claude-opus-4-5', 'claude-sonnet-4-5', 'template'])
        }
    }
```

#### 2. Optimiser performance avec indexes (10min)

**Vérifier que les indexes existent** :

```sql
-- Vérifier indexes sur lunar_interpretations
SELECT indexname FROM pg_indexes WHERE tablename = 'lunar_interpretations';

-- Si manquant, créer migration Alembic
-- Index sur user_id pour filtrage rapide
CREATE INDEX IF NOT EXISTS idx_lunar_interpretations_user_id
ON lunar_interpretations(user_id);

-- Index composite user_id + created_at pour last_generated
CREATE INDEX IF NOT EXISTS idx_lunar_interpretations_user_created
ON lunar_interpretations(user_id, created_at DESC);
```

**Si indexes manquent**, créer migration :

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

alembic revision -m "add indexes lunar_interpretations user_id"
```

Puis dans le fichier de migration :

```python
def upgrade():
    op.create_index(
        'idx_lunar_interpretations_user_id',
        'lunar_interpretations',
        ['user_id']
    )
    op.create_index(
        'idx_lunar_interpretations_user_created',
        'lunar_interpretations',
        ['user_id', 'created_at'],
        postgresql_using='btree'
    )

def downgrade():
    op.drop_index('idx_lunar_interpretations_user_created')
    op.drop_index('idx_lunar_interpretations_user_id')
```

#### 3. Ajouter cache applicatif (optionnel, 10min)

**Pour performance optimale** (si endpoint appelé fréquemment) :

```python
from services.interpretation_cache_service import interpretation_cache

@router.get("/interpretation/metadata")
async def get_lunar_interpretation_metadata(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Vérifier cache (TTL 5 minutes)
    cache_key = f"lunar_metadata_user_{current_user.id}"
    cached = interpretation_cache.get(cache_key)
    if cached:
        return cached

    # ... (requêtes DB comme ci-dessus) ...

    result = {
        'user_id': current_user.id,
        # ... stats ...
    }

    # Sauver en cache (5 min)
    interpretation_cache.set(cache_key, result, ttl=300)

    return result
```

#### 4. Tester l'endpoint (15min)

**Test manuel** :

```bash
# Appel simple
curl -X GET http://localhost:8000/api/lunar/interpretation/metadata \
  -H "Authorization: Bearer TOKEN" | jq

# Vérifier structure réponse
{
  "user_id": 123,
  "total_interpretations": 42,
  "models_used": {
    "claude-opus-4-5": 30,
    "template": 12
  },
  "cached_rate": 28.57,
  "last_generated": "2026-01-23T17:30:00",
  "stats": {
    "claude_generations": 30,
    "template_fallbacks": 12,
    "other": 0
  }
}
```

**Test unitaire** :

```python
@pytest.mark.asyncio
async def test_get_metadata_empty_user():
    """User sans interprétations → stats à zéro"""
    # Mock DB query retourne 0
    response = client.get(
        "/api/lunar/interpretation/metadata",
        headers={"Authorization": f"Bearer {jwt_token}"}
    )

    assert response.status_code == 200
    assert response.json()['total_interpretations'] == 0
    assert response.json()['cached_rate'] == 0


@pytest.mark.asyncio
async def test_get_metadata_with_data():
    """User avec 10 interprétations → stats correctes"""
    # TODO: Seed DB avec 10 interprétations
    # Vérifier stats cohérentes
```

#### 5. Documentation (5min)

```python
"""
Statistiques des interprétations lunaires de l'utilisateur

**Use cases** :
- Dashboard utilisateur (afficher stats génération)
- Monitoring qualité (ratio Claude vs templates)
- Analytics (modèles les plus utilisés)

**Performance** :
- Requêtes optimisées avec indexes
- Cache applicatif (5min TTL)
- Temps réponse < 100ms

**Données retournées** :
- total_interpretations: Nombre total
- models_used: Répartition par modèle IA
- cached_rate: % d'interprétations depuis templates (fallback)
- last_generated: Timestamp dernière génération

**Évolutions futures** :
- Ajouter durée moyenne de génération
- Ajouter répartition par subject (full, climate, etc.)
- Ajouter historique par mois
"""
```

### Critères de succès
- ✅ Endpoint fonctionne (200 OK)
- ✅ Stats correctes (count, répartition, pourcentages)
- ✅ Performance <100ms (vérifier avec logs)
- ✅ Indexes créés si nécessaires
- ✅ Tests unitaires passent
- ✅ Documentation inline complète

### Livrables
- `routes/lunar.py` avec nouveau endpoint
- (Optionnel) Migration Alembic pour indexes
- Tests créés
- Commit : `feat(api): ajouter endpoint GET /lunar/interpretation/metadata`

---

## 🔄 Workflow Vague 3

### Démarrage parallèle

**Les 3 agents peuvent démarrer IMMÉDIATEMENT en parallèle** :

```bash
# Agent A
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
# Copier le prompt Agent A ci-dessus dans une nouvelle session Claude Code

# Agent B
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
# Copier le prompt Agent B ci-dessus dans une nouvelle session Claude Code

# Agent C
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
# Copier le prompt Agent C ci-dessus dans une nouvelle session Claude Code
```

### Validation finale

Après complétion des 3 agents :

1. **Vérifier API fonctionne** :
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Tester endpoint existant (Agent A)
curl http://localhost:8000/api/lunar-returns/current/report | jq '.metadata'

# Tester regenerate (Agent B)
curl -X POST http://localhost:8000/api/lunar/interpretation/regenerate \
  -H "Authorization: Bearer TOKEN" \
  -d '{"lunar_return_id": 1}' | jq

# Tester stats (Agent C)
curl http://localhost:8000/api/lunar/interpretation/metadata \
  -H "Authorization: Bearer TOKEN" | jq
```

2. **Vérifier tests passent** :
```bash
pytest tests/test_lunar_routes.py -v
pytest tests/test_lunar_integration.py -v
pytest -q
```

3. **Marquer Vague 3 complète** :
```bash
# Mettre à jour CLAUDE.md
# Passer à Vague 4
```

---

**Durée estimée Vague 3** : 1h30 en parallèle (vs 4h séquentiel)
**Progression après Vague 3** : 8h30/10h (85%)
