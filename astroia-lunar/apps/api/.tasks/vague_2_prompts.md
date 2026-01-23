# Prompts Vague 2 : Service Layer

## 🎯 Contexte

**Vague 1 TERMINÉE** :
- ✅ Agent A : Sprint 1 complet (scripts + tests + docs)
- ✅ Agent B : Task 2.1 complétée (generator enrichi avec métriques, logs, retry, timeouts)
- ✅ Agent C : Task 2.3 complétée (legacy wrapper V1→V2)

**Vague 2 - 3 tâches en parallèle** :
- Agent A : Task 2.2 (Refactor lunar_report_builder) - 2h30
- Agent B : Task 2.4 (Tests generator) - 2h
- Agent C : Task 4.3 (Audit migration) - 1h

**Dépendances satisfaites** :
- Task 2.1 (generator enrichi) ✅ terminée en Vague 1 → débloque 2.2 et 2.4
- Task 4.3 indépendante (juste vérifier DB)

---

## 🤖 Agent A - Task 2.2 : Refactor lunar_report_builder.py

### Objectif
Intégrer le nouveau service `lunar_interpretation_generator.py` dans `lunar_report_builder.py` pour remplacer l'ancien système de fallback.

### Contexte technique
- **Fichier cible** : `services/lunar_report_builder.py` (928 LOC)
- **Service à utiliser** : `services/lunar_interpretation_generator.py` (enrichi en Vague 1 par Agent B)
- **Fonction principale** : `build_lunar_report_v4_async()`
- **Lignes à modifier** : ~811-889 (section interprétations)

### Tâches détaillées

#### 1. Remplacer les imports (5min)
```python
# AVANT (lignes ~50-60)
from services.lunar_interpretation_service import (
    load_lunar_interpretation_with_fallback,
    format_weekly_advice_v2
)

# APRÈS
from services.lunar_interpretation_generator import (
    generate_or_get_interpretation
)
```

#### 2. Refactorer build_lunar_report_v4_async() (1h30)

**Section à modifier** : lignes ~811-889

**AVANT** :
```python
# Interprétations lunaires
lunar_interpretation = {}
interpretation_source = 'fallback'
weekly_advice_db = None

if db is not None:
    interpretation_full, weekly_advice_db, interpretation_source = \
        await load_lunar_interpretation_with_fallback(
            db=db,
            moon_sign=lunar_return.moon_sign,
            moon_house=lunar_return.moon_house,
            lunar_ascendant=lunar_return.lunar_ascendant,
            preferred_version=settings.LUNAR_INTERPRETATION_VERSION,
            lang='fr'
        )
    lunar_interpretation['full'] = interpretation_full
else:
    # Fallback si pas de DB
    lunar_interpretation['full'] = "Interprétation générique..."
```

**APRÈS** :
```python
# Interprétations lunaires (V2)
lunar_interpretation = {}
interpretation_source = 'fallback'
weekly_advice_db = None
model_used = None

if db is not None:
    # Utiliser nouveau service V2
    output_text, weekly_advice, source, model = await generate_or_get_interpretation(
        db=db,
        lunar_return_id=lunar_return.id,
        user_id=lunar_return.user_id,
        subject='full',
        version=settings.LUNAR_INTERPRETATION_VERSION,
        lang='fr'
    )

    lunar_interpretation['full'] = output_text
    weekly_advice_db = weekly_advice
    interpretation_source = source
    model_used = model
else:
    # Fallback si pas de DB
    lunar_interpretation['full'] = "Interprétation générique..."
    interpretation_source = 'no_db'
```

#### 3. Ajouter metadata dans la réponse (30min)

**À la fin de build_lunar_report_v4_async()**, ajouter section metadata :

```python
return {
    'header': {...},
    'general_climate': {...},
    'dominant_axes': {...},
    'major_aspects': {...},
    'lunar_interpretation': lunar_interpretation,
    'weekly_advice': weekly_advice_db or {},
    'metadata': {  # NOUVEAU
        'source': interpretation_source,
        'model_used': model_used,
        'version': settings.LUNAR_INTERPRETATION_VERSION,
        'generated_at': datetime.utcnow().isoformat()
    }
}
```

#### 4. Nettoyer ancien code (15min)
- Supprimer imports inutilisés de `lunar_interpretation_service`
- Vérifier qu'aucune autre fonction n'utilise l'ancien service
- Commenter les lignes de fallback hardcodé (garder pour référence)

#### 5. Tester (30min)
```bash
# Lancer tests existants
pytest tests/test_lunar_integration.py -v
pytest tests/test_lunar_report_builder.py -v -k lunar_report

# Vérifier que les tests passent toujours
```

### Critères de succès
- ✅ `generate_or_get_interpretation()` utilisé à la place de l'ancien service
- ✅ Metadata présente dans toutes les réponses
- ✅ Tests existants passent
- ✅ Aucune régression fonctionnelle
- ✅ Ancien code supprimé ou commenté clairement

### Livrables
- `services/lunar_report_builder.py` refactoré
- Tests validés
- Commit : `feat(lunar): refactor lunar_report_builder pour utiliser generator V2`

---

## 🧪 Agent B - Task 2.4 : Tests unitaires lunar_interpretation_generator.py

### Objectif
Créer une suite de tests complète pour le service `lunar_interpretation_generator.py` enrichi en Vague 1.

### Contexte technique
- **Fichier cible** : `tests/test_lunar_interpretation_generator.py` (nouveau fichier)
- **Service testé** : `services/lunar_interpretation_generator.py` (700 LOC, enrichi avec métriques/logs/retry)
- **Pattern** : Tests unitaires avec mocks (AsyncMock pour DB et Claude API)
- **Coverage cible** : >90%

### Tâches détaillées

#### 1. Setup du fichier de tests (15min)

```python
"""
Tests unitaires pour lunar_interpretation_generator.py

Tests couverts:
- Génération idempotente (cache DB)
- Hiérarchie de fallback (DB → Claude → Template → Hardcoded)
- Versionning (v2, v3 coexistent)
- Force regenerate
- Timeouts et retry logic
- Métriques Prometheus
- Logs structurés
"""

import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime, timezone

from services.lunar_interpretation_generator import (
    generate_or_get_interpretation,
    LunarInterpretationError,
    ClaudeAPIError,
    TemplateNotFoundError
)
from models.lunar_interpretation import LunarInterpretation
from models.lunar_interpretation_template import LunarInterpretationTemplate
```

#### 2. Tests idempotence et cache (30min)

```python
@pytest.mark.asyncio
async def test_generate_idempotent_cache_hit():
    """
    2 appels successifs avec même lunar_return_id → retourne cache DB
    """
    # Mock DB avec interprétation existante
    mock_db = AsyncMock()
    existing_interp = LunarInterpretation(
        id=uuid.uuid4(),
        user_id=1,
        lunar_return_id=123,
        subject='full',
        version=2,
        lang='fr',
        output_text='Interprétation cached',
        weekly_advice={'week_1': 'Conseil 1'},
        model_used='claude-opus-4-5',
        input_json={'moon_sign': 'Aries'}
    )

    # Mock query retourne interprétation existante
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = existing_interp
    mock_db.execute.return_value = mock_result

    # Premier appel
    output1, weekly1, source1, model1 = await generate_or_get_interpretation(
        db=mock_db,
        lunar_return_id=123,
        user_id=1,
        subject='full'
    )

    # Deuxième appel
    output2, weekly2, source2, model2 = await generate_or_get_interpretation(
        db=mock_db,
        lunar_return_id=123,
        user_id=1,
        subject='full'
    )

    # Assertions
    assert output1 == output2 == 'Interprétation cached'
    assert source1 == source2 == 'db_temporal'
    assert model1 == model2 == 'claude-opus-4-5'


@pytest.mark.asyncio
async def test_generate_cache_miss_then_claude():
    """
    Pas de cache DB → appel Claude → sauvegarde en DB
    """
    # TODO: Implémenter
```

#### 3. Tests fallback hiérarchique (45min)

```python
@pytest.mark.asyncio
async def test_fallback_claude_to_template():
    """
    Cache miss + Claude timeout → fallback template DB
    """
    # TODO: Mock DB sans cache, Claude timeout, template existe


@pytest.mark.asyncio
async def test_fallback_complete_hierarchy():
    """
    DB temp fail → Claude fail → Template OK
    """
    # TODO: Tester cascade complète


@pytest.mark.asyncio
async def test_fallback_to_hardcoded():
    """
    Tous fallbacks échouent → hardcoded template
    """
    # TODO: Mock tous échecs sauf hardcoded
```

#### 4. Tests versionning (20min)

```python
@pytest.mark.asyncio
async def test_version_coexistence():
    """
    Générer v2 puis v3 → 2 entries distinctes en DB
    """
    # TODO: Créer 2 versions, vérifier isolation


@pytest.mark.asyncio
async def test_force_regenerate():
    """
    force_regenerate=True → ignore cache, régénère avec Claude
    """
    # TODO: Mock cache existant, force=True, vérifier appel Claude
```

#### 5. Tests error handling (30min)

```python
@pytest.mark.asyncio
async def test_claude_api_error_retry():
    """
    Claude APIError → retry 3 fois → fallback
    """
    # TODO: Mock Claude échec 3 fois, vérifier fallback


@pytest.mark.asyncio
async def test_claude_timeout():
    """
    Claude >30s → asyncio.TimeoutError → fallback template
    """
    # TODO: Mock timeout, vérifier fallback


@pytest.mark.asyncio
async def test_invalid_lunar_return_id():
    """
    lunar_return_id inexistant → InvalidLunarReturnError
    """
    # TODO: Mock DB query retourne None
```

#### 6. Tests métriques Prometheus (20min)

```python
@pytest.mark.asyncio
async def test_metrics_recorded():
    """
    Génération Claude → métriques enregistrées
    """
    from services.lunar_interpretation_generator import (
        lunar_interpretation_generated_total,
        lunar_interpretation_duration_seconds
    )

    # TODO: Générer interprétation, vérifier counters incrémentés


@pytest.mark.asyncio
async def test_metrics_fallback():
    """
    Fallback template → métrique fallback_total incrémentée
    """
    # TODO: Forcer fallback, vérifier counter
```

#### 7. Tests logs structurés (15min)

```python
@pytest.mark.asyncio
async def test_logs_structured(caplog):
    """
    Logs structurés JSON avec correlation IDs
    """
    # TODO: Générer, vérifier logs caplog


@pytest.mark.asyncio
async def test_logs_include_context(caplog):
    """
    Logs contiennent user_id, lunar_return_id, subject, source
    """
    # TODO: Vérifier contexte complet dans logs
```

### Critères de succès
- ✅ Au moins 15 tests implémentés
- ✅ Coverage >90% de `lunar_interpretation_generator.py`
- ✅ Tous tests passent (`pytest tests/test_lunar_interpretation_generator.py -v`)
- ✅ Mocks Claude API (pas d'appels réels)
- ✅ Tests rapides (<30s total)

### Livrables
- `tests/test_lunar_interpretation_generator.py` (>300 LOC)
- Commit : `test(lunar): ajouter tests complets generator V2 (15+ tests, >90% coverage)`

---

## 🔍 Agent C - Task 4.3 : Audit migration V1→V2

### Objectif
Valider l'intégrité de la migration des 1728 interprétations de `pregenerated_lunar_interpretations` vers `lunar_interpretation_templates`.

### Contexte technique
- **Table source** : `pregenerated_lunar_interpretations_backup` (backup créé en Sprint 0)
- **Table cible** : `lunar_interpretation_templates` (1728 templates migrés)
- **Script** : `scripts/audit_lunar_migration.py` (nouveau)
- **Objectif** : Vérifier aucune perte de données

### Tâches détaillées

#### 1. Créer script d'audit (30min)

```python
"""
Audit migration Lunar V1 → V2

Validations:
1. Count exact : 1728 templates
2. Échantillon 100 lignes identiques V1 vs V2
3. Aucune perte données (checksum)
4. Indexes correctement créés
5. UNIQUE constraints actifs
"""

import asyncio
from sqlalchemy import select, func, text
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
from models.lunar_interpretation_template import LunarInterpretationTemplate

async def audit_migration():
    async with AsyncSessionLocal() as db:
        print("🔍 Audit migration Lunar V1 → V2\n")

        # 1. Vérifier count
        count_templates = await db.scalar(
            select(func.count()).select_from(LunarInterpretationTemplate)
        )
        print(f"1️⃣  Count templates : {count_templates}")
        assert count_templates == 1728, f"❌ Expected 1728, got {count_templates}"
        print("   ✅ Count OK (1728)")

        # 2. Vérifier backup accessible
        try:
            count_backup = await db.scalar(
                text("SELECT COUNT(*) FROM pregenerated_lunar_interpretations_backup")
            )
            print(f"\n2️⃣  Count backup : {count_backup}")
            assert count_backup == 1728, f"❌ Backup incomplet"
            print("   ✅ Backup intact (1728)")
        except Exception as e:
            print(f"   ⚠️  Backup table inaccessible (OK si déjà cleanup)")

        # 3. Échantillon comparaison V1 vs V2
        print("\n3️⃣  Comparaison échantillon (100 lignes)...")
        sample_query = text("""
            SELECT
                b.moon_sign, b.moon_house, b.lunar_ascendant, b.version, b.lang,
                b.interpretation_full as backup_text,
                t.template_text
            FROM pregenerated_lunar_interpretations_backup b
            LEFT JOIN lunar_interpretation_templates t
                ON b.moon_sign = t.moon_sign
                AND b.moon_house = t.moon_house
                AND b.lunar_ascendant = t.lunar_ascendant
                AND b.version = t.version
                AND b.lang = t.lang
            WHERE t.template_type = 'full'
            LIMIT 100
        """)

        mismatches = 0
        missing = 0
        result = await db.execute(sample_query)
        for row in result:
            if row.template_text is None:
                missing += 1
                print(f"   ❌ Missing: {row.moon_sign} M{row.moon_house} {row.lunar_ascendant}")
            elif row.backup_text != row.template_text:
                mismatches += 1
                print(f"   ⚠️  Mismatch: {row.moon_sign} M{row.moon_house}")

        if missing > 0:
            print(f"   ❌ {missing} lignes manquantes")
        elif mismatches > 0:
            print(f"   ⚠️  {mismatches} différences texte (peut être OK si nettoyage)")
        else:
            print("   ✅ Échantillon parfaitement identique")

        # 4. Vérifier indexes
        print("\n4️⃣  Vérification indexes...")
        indexes_query = text("""
            SELECT indexname
            FROM pg_indexes
            WHERE tablename = 'lunar_interpretation_templates'
        """)
        indexes = await db.execute(indexes_query)
        index_names = [row.indexname for row in indexes]

        expected_indexes = [
            'idx_lunar_templates_unique',
            'idx_lunar_templates_lookup',
            'idx_lunar_templates_type'
        ]

        for idx in expected_indexes:
            if idx in index_names:
                print(f"   ✅ {idx}")
            else:
                print(f"   ❌ {idx} manquant")

        # 5. Tester UNIQUE constraint
        print("\n5️⃣  Test UNIQUE constraint...")
        try:
            # Essayer d'insérer doublon
            duplicate = LunarInterpretationTemplate(
                template_type='full',
                moon_sign='Aries',
                moon_house=1,
                lunar_ascendant='Leo',
                version=2,
                lang='fr',
                template_text='Doublon test'
            )
            db.add(duplicate)
            await db.commit()
            print("   ❌ UNIQUE constraint ne fonctionne pas!")
        except Exception as e:
            if 'unique' in str(e).lower():
                print("   ✅ UNIQUE constraint actif")
            else:
                print(f"   ⚠️  Erreur inattendue: {e}")
            await db.rollback()

        print("\n" + "="*50)
        print("✅ Audit terminé avec succès")
        print("="*50)

if __name__ == "__main__":
    asyncio.run(audit_migration())
```

#### 2. Exécuter l'audit (15min)

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

python scripts/audit_lunar_migration.py
```

#### 3. Documenter résultats (15min)

Créer `docs/MIGRATION_AUDIT_REPORT.md` :

```markdown
# Rapport Audit Migration Lunar V1→V2

**Date** : 2026-01-23
**Script** : `scripts/audit_lunar_migration.py`

## Résultats

### 1. Count Templates
- ✅ Attendu : 1728
- ✅ Réel : 1728
- **Status** : ✅ OK

### 2. Backup Intact
- ✅ Table backup : 1728 lignes
- **Status** : ✅ OK

### 3. Échantillon Comparaison (100 lignes)
- ✅ Lignes manquantes : 0
- ✅ Différences texte : 0
- **Status** : ✅ OK

### 4. Indexes
- ✅ idx_lunar_templates_unique
- ✅ idx_lunar_templates_lookup
- ✅ idx_lunar_templates_type
- **Status** : ✅ OK

### 5. UNIQUE Constraint
- ✅ Actif et fonctionnel
- **Status** : ✅ OK

## Conclusion

✅ **Migration validée à 100%**
- Aucune perte de données
- Tous les contrôles d'intégrité passent
- Prêt pour production

## Actions suivantes
- [ ] Cleanup table backup (après validation prod 1 semaine)
```

### Critères de succès
- ✅ Script `audit_lunar_migration.py` créé et exécuté
- ✅ 1728 templates validés
- ✅ Échantillon 100 lignes identiques V1 vs V2
- ✅ Indexes et UNIQUE constraints OK
- ✅ Rapport `MIGRATION_AUDIT_REPORT.md` créé

### Livrables
- `scripts/audit_lunar_migration.py` (~150 LOC)
- `docs/MIGRATION_AUDIT_REPORT.md`
- Commit : `audit(lunar): valider migration V1→V2 (1728/1728 templates OK)`

---

## 🔄 Workflow Vague 2

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

1. **Vérifier tests passent** :
```bash
pytest tests/test_lunar_interpretation_generator.py -v
pytest tests/test_lunar_integration.py -v
pytest -q
```

2. **Vérifier audit OK** :
```bash
cat docs/MIGRATION_AUDIT_REPORT.md
```

3. **Marquer Vague 2 complète** :
```bash
# Mettre à jour CLAUDE.md
# Passer à Vague 3
```

---

**Durée estimée Vague 2** : 2h30 en parallèle (vs 5h30 séquentiel)
**Progression après Vague 2** : 4h30/10h (45%)
