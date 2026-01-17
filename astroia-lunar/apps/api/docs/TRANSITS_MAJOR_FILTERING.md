# Documentation: Filtrage des Aspects Majeurs (major_only)

## Vue d'ensemble

Le système de transits implémente un mécanisme de filtrage permettant de ne retourner que les **4 aspects majeurs** en astrologie :
- **Conjonction** (0°)
- **Opposition** (180°)
- **Carré** (90°)
- **Trigone** (120°)

Ce filtrage est contrôlé par le paramètre query `major_only` disponible sur tous les endpoints de transits.

---

## Architecture du filtrage

### 1. Point d'entrée: Routes API

Trois endpoints acceptent le paramètre `major_only`:

#### `/api/transits/natal` (POST)
```python
@router.post("/natal", response_model=TransitsResponse)
async def natal_transits(
    request: NatalTransitsRequest,
    major_only: bool = False,  # ← Paramètre query
    db: AsyncSession = Depends(get_db)
):
```

#### `/api/transits/lunar_return` (POST)
```python
@router.post("/lunar_return", response_model=TransitsResponse)
async def lunar_return_transits(
    request: LunarReturnTransitsRequest,
    major_only: bool = False,  # ← Paramètre query
    db: AsyncSession = Depends(get_db)
):
```

#### `/api/transits/overview/{user_id}/{month}` (GET)
```python
@router.get("/overview/{user_id}/{month}", response_model=TransitsOverviewDB)
async def get_transits_overview(
    user_id: UUID,
    month: str,
    major_only: bool = False,  # ← Paramètre query
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
```

**Usage:**
```bash
# Retourner tous les aspects
curl -X POST "http://localhost:8000/api/transits/natal"

# Retourner uniquement les aspects majeurs
curl -X POST "http://localhost:8000/api/transits/natal?major_only=true"
```

---

### 2. Propagation vers le service

Le paramètre `major_only` est propagé à la fonction de génération d'insights:

**Fichier:** `/apps/api/routes/transits.py`
```python
# Ligne 62 (natal) et ligne 154 (lunar_return)
insights = transits_services.generate_transit_insights(result, major_only=major_only)
```

---

### 3. Logique de filtrage dans le service

**Fichier:** `/apps/api/services/transits_services.py`

#### Fonction `filter_major_aspects_only()` (lignes 145-168)

Cette fonction filtre les événements de transit pour ne garder que les aspects majeurs:

```python
def filter_major_aspects_only(events: list, major_only: bool = False) -> list:
    """
    Filtre les aspects pour ne garder que les majeurs (conjonction, opposition, carré, trigone).
    """
    if not major_only:
        return events  # Pas de filtrage

    # Définition des 4 aspects majeurs
    major_aspect_types = ["conjunction", "opposition", "square", "trine"]

    filtered = []
    for event in events:
        # Support de plusieurs formats de clés: aspect_type, aspect
        aspect_type = event.get("aspect_type") or event.get("aspect", "")

        # Comparaison insensible à la casse
        if aspect_type.lower() in major_aspect_types:
            filtered.append(event)

    return filtered
```

**Caractéristiques:**
- Comparaison **insensible à la casse** (`lower()`)
- Support de **deux formats de clés**: `aspect_type` (RapidAPI) et `aspect` (format legacy)
- Retourne la liste non modifiée si `major_only=False`

---

#### Fonction `generate_transit_insights()` (lignes 235-405)

Cette fonction génère les insights et applique le filtrage:

**Étapes d'exécution:**

1. **Extraction des événements** (lignes 266-272):
```python
events = []
if "events" in transits_data and isinstance(transits_data["events"], list):
    events = transits_data["events"]
elif "aspects" in transits_data and isinstance(transits_data["aspects"], list):
    events = transits_data["aspects"]  # Format legacy
```

2. **Filtrage des points non-planétaires** (ligne 275):
```python
# TOUJOURS filtrer les points non-planétaires (nœuds lunaires, Chiron, etc.)
events = filter_non_planetary_points(events)
```

3. **Filtrage des aspects majeurs** (ligne 278):
```python
# Filtrer pour ne garder que les aspects majeurs si demandé
events = filter_major_aspects_only(events, major_only)
```

4. **Tri par orbe** (lignes 281-285):
```python
# Trier par importance (orbe le plus serré en valeur absolue)
sorted_events = sorted(
    events,
    key=lambda e: abs(e.get("orb", 10))
)[:5]  # Top 5 aspects
```

5. **Génération des insights** (lignes 296-391):
   - Normalisation des noms de planètes
   - Génération d'interprétations contextuelles
   - Construction de la structure de réponse

---

### 4. Filtrage sur récupération (endpoint /overview)

Pour l'endpoint GET `/overview/{user_id}/{month}`, le filtrage est appliqué **à la volée** sur les données en cache:

**Fichier:** `/apps/api/routes/transits.py` (lignes 261-278)
```python
# Si major_only=True, filtrer les aspects dans les données avant de retourner
if major_only and overview.overview:
    # Recalculer les insights avec filtrage pour natal_transits
    if "natal_transits" in overview.overview:
        natal_data = overview.overview["natal_transits"]
        filtered_insights = transits_services.generate_transit_insights(natal_data, major_only=True)
        overview.overview["insights"] = filtered_insights

    # Recalculer les insights avec filtrage pour lunar_return_transits
    if "lunar_return_transits" in overview.overview:
        lr_data = overview.overview["lunar_return_transits"]
        filtered_lr_insights = transits_services.generate_transit_insights(lr_data, major_only=True)
        overview.overview["lr_insights"] = filtered_lr_insights
```

**Avantage:** Les données brutes sont conservées en DB, le filtrage est appliqué uniquement à la lecture selon la demande.

---

## Définition des aspects majeurs

### Aspects inclus (4 types)

| Aspect | Angle | Nom anglais | Nature |
|--------|-------|-------------|---------|
| Conjonction | 0° | `conjunction` | Fusion, amplification |
| Opposition | 180° | `opposition` | Tension, polarité |
| Carré | 90° | `square` | Friction, défi |
| Trigone | 120° | `trine` | Harmonie, fluidité |

### Aspects exclus (mineurs)

Les aspects suivants sont **filtrés** quand `major_only=true`:

- **Sextile** (60°)
- **Quinconce** (150°)
- **Semi-carré** (45°)
- **Sesqui-carré** (135°)
- **Semi-sextile** (30°)
- Autres aspects mineurs

---

## Validation par tests

### Fichier de tests: `/apps/api/tests/test_transits_major.py`

Le comportement du filtrage est validé par **12 tests unitaires**:

#### Tests de la fonction `filter_major_aspects_only()`

1. `test_filter_major_aspects_only_all_major`: Tous aspects majeurs → tous conservés
2. `test_filter_major_aspects_only_mixed`: Mélange majeurs/mineurs → seuls majeurs conservés
3. `test_filter_major_aspects_only_disabled`: `major_only=False` → tous conservés
4. `test_filter_major_aspects_only_case_insensitive`: Insensibilité à la casse (CONJUNCTION, Opposition, etc.)
5. `test_filter_major_aspects_fallback_aspect_key`: Support clé `aspect` (legacy)

#### Tests de la fonction `generate_transit_insights()`

6. `test_generate_transit_insights_major_only_true`: Filtrage activé → seuls majeurs retournés
7. `test_generate_transit_insights_major_only_false`: Filtrage désactivé → tous retournés
8. `test_generate_transit_insights_major_only_four_types`: Validation des 4 types majeurs uniquement
9. `test_generate_transit_insights_empty`: Données vides → gestion correcte
10. `test_generate_transit_insights_with_old_format`: Support format legacy (`aspects` au lieu de `events`)

#### Tests de validation

11. `test_major_aspects_definition`: Validation stricte de la définition des 4 aspects majeurs
12. `test_aspects_sorted_by_orb`: Tri par orbe (le plus serré en premier)

**Exécution des tests:**
```bash
cd apps/api
pytest tests/test_transits_major.py -v
```

**Résultat attendu:**
```
12 passed in 0.01s
```

---

## Flux complet de données

```
┌─────────────────────────────────────────────────────────────────────┐
│ 1. Client (mobile app)                                              │
│    POST /api/transits/natal?major_only=true                         │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 2. Route API (apps/api/routes/transits.py)                         │
│    - Récupère paramètre query: major_only = True                   │
│    - Appelle service RapidAPI                                       │
│    - Propage major_only au service                                  │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 3. Service transits_services.py                                     │
│    generate_transit_insights(result, major_only=True)               │
│                                                                      │
│    a) Extraction des événements (events ou aspects)                │
│    b) Filtrage non-planétaires (TOUJOURS)                          │
│    c) filter_major_aspects_only(events, major_only=True)            │
│       └─→ Ne garde que: conjunction, opposition, square, trine     │
│    d) Tri par orbe (le plus serré en premier)                      │
│    e) Génération insights et interprétations                        │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 4. Réponse API                                                      │
│    {                                                                 │
│      "insights": [...],                                             │
│      "major_aspects": [                                             │
│        {                                                             │
│          "aspect": "conjunction" | "opposition" | "square" | "trine"│
│        }                                                             │
│      ]                                                               │
│    }                                                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Commit de référence

**Commit f3cde98**: "feat(mobile): déplacer filtrage transits majeurs vers backend"

Ce commit a déplacé le filtrage `major_only` du frontend (mobile) vers le backend, centralisant ainsi la logique métier et garantissant un comportement cohérent.

**Changements clés:**
- Ajout paramètre `major_only` sur routes `/natal`, `/lunar_return`, `/overview`
- Implémentation fonction `filter_major_aspects_only()` dans service
- Intégration filtrage dans `generate_transit_insights()`
- Ajout tests complets de validation

---

## Remarques importantes

### 1. Double filtrage
Le système applique **deux filtrages successifs**:
1. **Filtrage des points non-planétaires** (TOUJOURS actif, non optionnel)
   - Exclut: nœuds lunaires, Chiron, Lilith, Part de Fortune, etc.
2. **Filtrage des aspects majeurs** (optionnel, contrôlé par `major_only`)
   - Ne garde que: conjonction, opposition, carré, trigone

### 2. Conservation des données brutes
Les données brutes retournées par RapidAPI (incluant TOUS les aspects) sont sauvegardées en base de données. Le filtrage `major_only` est appliqué:
- À la génération des insights (lors du POST)
- À la récupération depuis le cache (lors du GET)

Cela permet de réutiliser les mêmes données pour différents niveaux de filtrage.

### 3. Comportement par défaut
Par défaut, `major_only=False`, donc tous les aspects sont retournés (après filtrage des points non-planétaires).

### 4. RapidAPI pré-filtre déjà
Le payload envoyé à RapidAPI spécifie déjà `"aspect_types": ["major"]` (ligne 102 dans `transits_services.py`), ce qui signifie que RapidAPI retourne déjà principalement des aspects majeurs. Le filtrage backend est donc une **double sécurité** et une **normalisation** au cas où RapidAPI retournerait d'autres aspects.

---

## Prochaines étapes possibles

1. **Monitoring**: Ajouter des métriques pour suivre l'utilisation de `major_only=true` vs `false`
2. **Configuration dynamique**: Permettre à l'utilisateur de personnaliser quels aspects sont considérés "majeurs"
3. **Performance**: Si RapidAPI retourne déjà uniquement les majeurs, évaluer si le filtrage backend est nécessaire
4. **Documentation API**: Ajouter exemples dans la documentation OpenAPI/Swagger

---

## Conclusion

Le filtrage `major_only` est correctement implémenté et validé:
- Paramètre propagé de la route → service → fonction de filtrage
- Définition claire et stricte des 4 aspects majeurs
- Tests complets (12 tests passant avec succès)
- Comportement cohérent sur POST et GET
- Documentation exhaustive

Le commit f3cde98 a réussi à centraliser cette logique côté backend, rendant le système plus maintenable et cohérent.
