# Implémentation Auto-Heal Natal Chart - MVP

## Résumé

Ce document décrit l'implémentation du système d'auto-heal et de fallback mock pour garantir que les utilisateurs reçoivent **toujours** un natal chart complet, même en cas d'échec RapidAPI.

## Objectif MVP

**Garantir qu'un utilisateur obtient TOUJOURS un natal chart complet** (≥10 planètes, 12 maisons, aspects optionnels), même si RapidAPI échoue, sans jamais bloquer l'onboarding mobile.

## Modifications Effectuées

### 1. Service de Mock Complet (`services/natal_chart_mock.py`) ✅

**Nouveau fichier** créé pour générer des natal charts mock déterministes et complets.

**Fonction principale:** `generate_complete_natal_mock(birth_data: dict, reason: str = "rapidapi_unavailable") -> dict`

**Caractéristiques:**
- Génération déterministe basée sur hash SHA256 des données de naissance
- Produit une structure JSONB complète avec:
  - Big3 (sun, moon, ascendant)
  - 10+ planètes (sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune, pluto + ascendant)
  - 12 maisons avec sign + degree
  - aspects vides `[]` (MVP accepte)
  - **Métadonnées `_mock: true` et `_reason`** pour détection par le mobile

**Exemple d'utilisation:**
```python
mock = generate_complete_natal_mock({
    "year": 1990,
    "month": 5,
    "day": 15,
    "hour": 14,
    "minute": 30,
    "latitude": 48.8566,
    "longitude": 2.3522
}, reason="rapidapi_503")

# mock contient:
# - _mock: True
# - _reason: "rapidapi_503"
# - 10+ planètes, 12 maisons, Big3 complets
```

### 2. Helper de Détection (`utils/natal_chart_helpers.py`) ✅

**Fonction ajoutée:** `is_chart_incomplete(positions: dict) -> bool`

**Critères d'incomplétude (CORRIGÉS selon spécifications utilisateur):**
1. Big3 manquants (sun, moon, ascendant top-level)
2. Moins de 10 planètes dans `positions["planets"]`
3. Exactement 12 maisons requises dans `positions["houses"]`
4. **IMPORTANT:** `aspects=[]` est ACCEPTABLE (MVP, ne pas rejeter)

**Exemple:**
```python
incomplete = {
    "sun": {"sign": "Aries"},
    "moon": {"sign": "Taurus"},
    "ascendant": {"sign": "Gemini"},
    "planets": {"sun": {...}, "moon": {...}},  # 2 planètes < 10
    "houses": {str(i): {...} for i in range(1, 8)},  # 7 maisons < 12
    "aspects": []  # OK, pas incomplet
}

is_chart_incomplete(incomplete)  # True (< 10 planètes, < 12 maisons)
```

### 3. Endpoint Dev Purge (`routes/natal.py`) ✅

**Nouveau endpoint:** `POST /natal-chart/dev/purge`

**Sécurité 3 couches:**
1. `APP_ENV == "development"` (retourne 404 sinon)
2. `ALLOW_DEV_PURGE == True` (retourne 404 sinon)
3. Authentification via `get_current_user`

**Scope:** Supprime uniquement le natal chart du `current_user`, pas d'impact global.

**Réponse:**
```json
{
  "message": "Natal chart purgé",
  "user_id": 123,
  "deleted_count": 1,
  "correlation_id": "uuid"
}
```

### 4. Amélioration Gestion Erreurs RapidAPI (`services/natal_reading_service.py`) ✅

**Changements:**
- Erreurs RapidAPI retournent maintenant **HTTP 503** (Service Unavailable) au lieu de 502
- Détail structuré avec:
  ```json
  {
    "code": "rapidapi_403",
    "message": "RapidAPI service unavailable",
    "provider_status": 403,
    "provider_body_preview": "..."
  }
  ```
- Logs enrichis avec endpoint, status, body preview, payload keys (sans secrets)
- **Pas d'assumptions** sur quotas ou raisons (générique "service unavailable")

### 5. Fallback Mock sur POST (`routes/natal.py`) ✅

**Localisation:** Fonction `calculate_natal_chart()`, around line 528

**Logique:**
```python
except HTTPException as e:
    if e.status_code == 503:  # RapidAPI fail
        # Extraire error code depuis detail
        error_code = "rapidapi_unavailable"
        if isinstance(e.detail, dict):
            error_code = e.detail.get("code", "rapidapi_unavailable")

        # Générer mock avec métadonnées
        raw_data = generate_complete_natal_mock(birth_data, reason=error_code)

        # Continuer flow normal avec mock
```

**Impact:** POST /api/natal-chart ne retourne jamais 503, utilise mock en fallback transparent.

### 6. Auto-Heal sur GET (`routes/natal.py`) ✅

**Localisation:** Fonction `get_natal_chart()`, lines 887-935

**Logique:**
```python
# Après vérification if not chart: raise 404

if is_chart_incomplete(chart.positions):
    logger.warning(f"🔧 Chart incomplet détecté, auto-heal avec mock")

    # Récupérer birth data depuis current_user
    birth_data = extract_birth_data(current_user)

    # Générer mock complet
    mock_positions = generate_complete_natal_mock(birth_data, reason="auto_heal")

    # Mettre à jour en DB
    chart.positions = mock_positions
    await db.commit()
    await db.refresh(chart)
```

**Impact:** GET /api/natal-chart ne retourne jamais de chart incomplet, auto-heal transparent et rapide (pas de retry RapidAPI).

## Tests Pytest ✅

### Tests Créés

1. **`tests/test_natal_chart_mock.py`** (23 tests)
   - Tests des helpers déterministes (`_deterministic_hash`, `_get_sign_from_seed`, etc.)
   - Tests de `generate_complete_natal_mock()`:
     - Structure complète (Big3, planets, houses, aspects, métadonnées)
     - 10+ planètes, 12 maisons, aspects vides
     - Déterminisme (mêmes données → même mock)
     - Métadonnées `_mock` et `_reason`

2. **`tests/test_natal_chart_helpers.py`** (27 tests)
   - Tests de `is_chart_incomplete()`:
     - Détection Big3 manquants
     - Détection < 10 planètes
     - Détection != 12 maisons
     - **IMPORTANT:** `aspects=[]` accepté (MVP)
   - Tests de `extract_big3_from_positions()`

3. **`tests/test_natal_chart_autoheal.py`** (17 tests)
   - Tests d'intégration:
     - Fallback mock sur POST (RapidAPI 503)
     - Auto-heal sur GET (chart incomplet)
     - Métadonnées mock présentes
     - Flow end-to-end conceptuel

**Total: 67 tests, tous passent ✅**

## Test End-to-End

**Script:** `scripts/test_autoheal_e2e.sh`

**Scénarios testés:**
1. Purge du chart existant (`POST /natal-chart/dev/purge`)
2. Création chart (`POST /natal-chart`)
   - Vérification RapidAPI vs mock
   - Vérification structure complète
3. Lecture chart (`GET /natal-chart`)
   - Vérification Big3 extraits
   - Vérification complétude (auto-heal si nécessaire)

**Lancement:**
```bash
chmod +x scripts/test_autoheal_e2e.sh
./scripts/test_autoheal_e2e.sh
```

## Fichiers Modifiés/Créés

### Nouveaux Fichiers
- `services/natal_chart_mock.py` - Service de mock complet déterministe
- `tests/test_natal_chart_mock.py` - Tests unitaires mock (23 tests)
- `tests/test_natal_chart_helpers.py` - Tests unitaires helpers (27 tests)
- `tests/test_natal_chart_autoheal.py` - Tests intégration (17 tests)
- `scripts/test_autoheal_e2e.sh` - Script test end-to-end

### Fichiers Modifiés
- `utils/natal_chart_helpers.py` - Ajout `is_chart_incomplete()`
- `routes/natal.py` - Ajout endpoint purge + fallback POST + auto-heal GET
- `services/natal_reading_service.py` - Amélioration gestion erreurs RapidAPI (503)

## Décisions Techniques (Validées par Utilisateur)

### 1. Mock avec Métadonnées (PAS Transparent)
- `_mock: true` et `_reason: "error_code"` ajoutés dans positions JSONB
- Le mobile peut détecter et afficher un warning à l'utilisateur
- Permet traçabilité et debugging

### 2. Auto-Heal Rapide (Pas de Retry RapidAPI)
- Fallback DIRECT sur mock si chart incomplet détecté
- Pas de tentative RapidAPI lors du GET (évite timeout)
- L'utilisateur peut manuellement purger + recalculer si besoin

### 3. Mock Permanent (Pas de Recalcul Auto)
- Pas de flag `is_mock` en DB, pas de recalcul automatique
- Le mock reste jusqu'à purge manuelle + nouveau POST
- Simplicité MVP, évite boucles de recalcul

### 4. Aspects Vides Acceptés
- `aspects: []` est VALIDE pour MVP
- `is_chart_incomplete()` ne rejette PAS les aspects vides
- Génération d'aspects calculés hors scope MVP

### 5. RapidAPI Erreurs → 503
- Toutes erreurs RapidAPI retournent HTTP 503 (Service Unavailable)
- Détail structuré avec `code`, `provider_status`, `provider_body_preview`
- Pas d'assumptions sur quotas/pricing (générique)

## Validation

### Critères de Succès MVP
- ✅ POST /api/natal-chart ne retourne jamais 503 (fallback mock)
- ✅ GET /api/natal-chart ne retourne jamais chart incomplet (auto-heal)
- ✅ Charts contiennent toujours ≥10 planètes, 12 maisons
- ✅ Aspects vides `[]` acceptés (MVP)
- ✅ Métadonnées `_mock` et `_reason` présentes pour détection mobile
- ✅ Endpoint purge disponible pour tests
- ✅ 67 tests pytest passent

### Prochaines Étapes (Hors MVP)
- Génération d'aspects calculés (si RapidAPI ne les fournit pas)
- Recalcul automatique des mocks après X jours
- Monitoring quotas RapidAPI (alertes proactives)
- UI mobile pour afficher warning "données simulées"

## Références

- Plan d'implémentation: `~/.claude/plans/mighty-moseying-matsumoto.md`
- Documentation natal_chart_mock: `services/natal_chart_mock.py:1-237`
- Documentation is_chart_incomplete: `utils/natal_chart_helpers.py:100-168`
- Tests unitaires: `tests/test_natal_chart_*.py`

---

**Date d'implémentation:** 2026-01-04
**Version:** MVP 1.0
**Status:** ✅ Complété et testé
