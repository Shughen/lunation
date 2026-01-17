# Tests du filtrage transits `major_only`

## Vue d'ensemble

Le fichier `test_transits_major.py` contient 12 tests unitaires pour valider le filtrage des aspects majeurs dans les transits planétaires.

## Contexte

Lorsque `major_only=true` est passé aux endpoints de transits, seuls les **4 aspects majeurs** doivent être retournés:
1. **Conjonction** (0°)
2. **Opposition** (180°)
3. **Carré** (90°)
4. **Trigone** (120°)

Les aspects mineurs (sextile, quincunx, semisextile, etc.) sont exclus.

## Routes testées

Les tests valident le filtrage sur ces endpoints:
- `POST /api/transits/natal?major_only=true`
- `POST /api/transits/lunar_return?major_only=true`
- `GET /api/transits/overview/{user_id}/{month}?major_only=true`

## Tests inclus

### 1. Tests de la fonction `filter_major_aspects_only()`

| Test | Description |
|------|-------------|
| `test_filter_major_aspects_only_all_major` | Vérifie que tous les aspects majeurs sont conservés |
| `test_filter_major_aspects_only_mixed` | Teste le filtrage avec aspects majeurs + mineurs |
| `test_filter_major_aspects_only_disabled` | Vérifie que tous aspects sont conservés quand `major_only=False` |
| `test_filter_major_aspects_only_case_insensitive` | Teste l'insensibilité à la casse |
| `test_filter_major_aspects_fallback_aspect_key` | Teste la compatibilité avec clé `aspect` au lieu de `aspect_type` |

### 2. Tests de la fonction `generate_transit_insights()`

| Test | Description |
|------|-------------|
| `test_generate_transit_insights_major_only_true` | Vérifie le filtrage dans generation d'insights |
| `test_generate_transit_insights_major_only_false` | Vérifie que tous aspects sont retournés quand `major_only=False` |
| `test_generate_transit_insights_major_only_four_types` | Valide que seuls les 4 types majeurs sont retournés |
| `test_generate_transit_insights_empty` | Teste le comportement avec données vides |
| `test_generate_transit_insights_with_old_format` | Vérifie la compatibilité avec l'ancien format API |

### 3. Tests de validation

| Test | Description |
|------|-------------|
| `test_major_aspects_definition` | Valide la définition des 4 aspects majeurs |
| `test_aspects_sorted_by_orb` | Vérifie le tri par orbe (le plus serré d'abord) |

## Exécution des tests

```bash
# Exécuter tous les tests transits major_only
cd apps/api
pytest tests/test_transits_major.py -v

# Exécuter un test spécifique
pytest tests/test_transits_major.py::test_generate_transit_insights_major_only_true -v

# Exécuter tous les tests transits (nouveaux + existants)
pytest tests/test_transits_major.py tests/test_transits_services.py -v
```

## Résultats attendus

Tous les 12 tests doivent passer:
```
tests/test_transits_major.py::test_filter_major_aspects_only_all_major PASSED
tests/test_transits_major.py::test_filter_major_aspects_only_mixed PASSED
tests/test_transits_major.py::test_filter_major_aspects_only_disabled PASSED
tests/test_transits_major.py::test_filter_major_aspects_only_case_insensitive PASSED
tests/test_transits_major.py::test_filter_major_aspects_fallback_aspect_key PASSED
tests/test_transits_major.py::test_generate_transit_insights_major_only_true PASSED
tests/test_transits_major.py::test_generate_transit_insights_major_only_false PASSED
tests/test_transits_major.py::test_generate_transit_insights_major_only_four_types PASSED
tests/test_transits_major.py::test_generate_transit_insights_empty PASSED
tests/test_transits_major.py::test_generate_transit_insights_with_old_format PASSED
tests/test_transits_major.py::test_major_aspects_definition PASSED
tests/test_transits_major.py::test_aspects_sorted_by_orb PASSED

======================== 12 passed in 0.02s ========================
```

## Implémentation validée

Ces tests valident l'implémentation dans:
- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/services/transits_services.py`
  - Fonction `filter_major_aspects_only(events, major_only)`
  - Fonction `generate_transit_insights(transits_data, major_only)`

- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/routes/transits.py`
  - Endpoint `POST /api/transits/natal?major_only={bool}`
  - Endpoint `POST /api/transits/lunar_return?major_only={bool}`
  - Endpoint `GET /api/transits/overview/{user_id}/{month}?major_only={bool}`

## Notes

- Ces tests sont des **tests unitaires purs** qui n'utilisent pas la base de données
- Ils s'exécutent très rapidement (< 0.02s)
- Ils ne dépendent pas du `setup_test_db` fixture de `conftest.py`
- Compatibles avec les formats API existants (ancien format `aspects` et nouveau format `events`)
