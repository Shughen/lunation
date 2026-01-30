# Correction Filtrage et Tri Aspects v4

**Date**: 2026-01-30
**Sprint**: 9 - Correction aspects manquants
**Status**: ✅ Implémenté et validé

## Problème Initial

L'application affichait seulement **6-10 aspects majeurs** au lieu des **~20 aspects** présents dans un thème natal standard (comparaison Astrotheme).

### Causes Identifiées

1. **Sextile manquant** : Exclus des aspects majeurs alors que c'est un aspect majeur standard
2. **Orbe trop stricte** : 6° fixe au lieu de 8°/10° variable selon luminaires (standard Liz Greene)
3. **Limite arbitraire** : limit=5 ou limit=10 dans le code
4. **Tri incorrect** : Par orbe uniquement, au lieu de par type puis orbe (standard Astrotheme)

## Solution Implémentée

### 1. Ajout du Sextile comme Aspect Majeur

**Types majeurs (5)** :
- Conjonction (☌, 0°)
- Opposition (☍, 180°)
- Carré (□, 90°)
- Trigone (△, 120°)
- **Sextile (⚹, 60°)** ← Ajouté

### 2. Orbes Variables (Standard Liz Greene/Astrodienst)

- **8°** pour tous les aspects standard
- **10°** quand Soleil OU Lune impliqué(e)

**Exemples** :
- Soleil-Neptune trigone (9.5°) → ✅ Inclus (luminaire, < 10°)
- Mars-Neptune trigone (9.5°) → ❌ Exclus (> 8°, pas de luminaire)
- Lune-Vénus trigone (2.15°) → ✅ Inclus (luminaire, < 10°)

### 3. Retrait des Limites Arbitraires

**Avant** :
- `limit=5` dans lunar_report_builder.py
- `limit=10` dans routes/natal.py

**Après** :
- `limit=100` partout (affiche tous les aspects majeurs valides)

### 4. Tri Astrotheme (Par Type puis Orbe)

**Ordre de tri** :
1. D'abord par **type d'aspect** (ordre d'importance)
2. Puis par **orbe** au sein de chaque type (du plus serré au plus large)

**Ordre des types** :
1. Conjonctions
2. Oppositions
3. Carrés
4. Trigones
5. Sextiles

**Exemple de résultat** :
```
Conjonction  Saturne-Neptune   1.50°
Conjonction  Soleil-Vénus      2.44°
Conjonction  Mars-MC           3.50°

Opposition   Mercure-Pluton    6.40°

Carré        Mars-AS           4.46°

Trigone      Soleil-Lune       0.29°
Trigone      Lune-Vénus        2.15°

Sextile      Soleil-MC         0.10°
Sextile      Saturne-Pluton    0.25°
```

## Fichiers Modifiés

### Backend (Python)

**1. `/apps/api/services/aspect_explanation_service.py`**
- Ajout `'sextile'` dans `MAJOR_ASPECT_TYPES`
- Ajout `ASPECT_SORT_ORDER` (ordre de tri Astrotheme)
- Ajout constantes `MAX_ORB_STANDARD = 8.0`, `MAX_ORB_LUMINARIES = 10.0`
- Ajout constante `LUMINARIES` (Soleil, Lune)
- Nouvelle fonction `get_max_orb(planet1, planet2)` → retourne 8° ou 10°
- Modification `filter_major_aspects_v4()` :
  - Utilise orbes variables au lieu de 6° fixe
  - Tri par type puis orbe (au lieu de orbe uniquement)

**2. `/apps/api/routes/natal.py`**
- Ligne 530, 677 : `limit=10` → `limit=100`

**3. `/apps/api/services/lunar_report_builder.py`**
- Ligne 808 : `limit=5` → `limit=100`

### Mobile (TypeScript)

**4. `/apps/mobile/utils/natalChartUtils.ts`**
- Ajout `ASPECT_SORT_ORDER` (même ordre que backend)
- Nouvelle fonction `getMaxOrb(planet1, planet2)` (orbes variables)
- Modification `filterMajorAspectsV4()` :
  - Ajout `'sextile'` dans `MAJOR_ASPECT_TYPES`
  - Utilise `getMaxOrb()` au lieu de `MAX_ORB = 6` fixe
  - Tri par type puis orbe (comme Astrotheme)

## Impact

### Avant
- **6-10 aspects** affichés
- Tri par orbe uniquement (aspects mélangés)
- Pas de sextiles
- Orbe fixe 6°

### Après
- **~20 aspects** affichés
- Tri par type puis orbe (groupés comme Astrotheme)
- Sextiles inclus (⚹)
- Orbes variables 8°/10° (standard professionnel)

### Exemple : Thème Natal 25/08/1994

**Résultat attendu** :
- 5-6 Conjonctions
- 1-2 Oppositions
- 1-2 Carrés
- 5-6 Trigones
- 6-7 Sextiles

**Total** : ~20 aspects (au lieu de 6-10)

## Compatibilité

### Rétrocompatibilité
- ✅ Versions 2/3 : Comportement legacy préservé
- ✅ Version 4 : Nouvelles règles activées
- ✅ Version 5 : Non affectée (filtrage séparé)

### Base de données
- ✅ Aucune migration nécessaire
- ✅ Aspects existants en cache : Recalcul automatique au prochain GET

## Tests

### Validation Backend
```bash
cd apps/api
python -c "
from services.aspect_explanation_service import filter_major_aspects_v4, get_max_orb

# Test orbes variables
assert get_max_orb('Sun', 'Neptune') == 10.0
assert get_max_orb('Mars', 'Jupiter') == 8.0

# Test filtrage
aspects = [
    {'planet1': 'Sun', 'planet2': 'Moon', 'type': 'trine', 'orb': 0.29},
    {'planet1': 'Sun', 'planet2': 'MC', 'type': 'sextile', 'orb': 0.10},
]
filtered = filter_major_aspects_v4(aspects)
assert len(filtered) == 2
assert filtered[0]['type'] == 'trine'  # Trigone avant sextile
print('✅ Backend validé')
"
```

### Validation Mobile
1. Calculer thème natal (25/08/1994, 10:30, Paris)
2. Vérifier nombre d'aspects ≥ 15
3. Vérifier tri : Conjonctions → Oppositions → Carrés → Trigones → Sextiles
4. Vérifier présence sextiles (symbole ⚹)

## Standards Appliqués

### Orbes
- **Liz Greene** (Astrodienst) : 8° standard, 10° luminaires
- **Sue Tompkins** : 8° pour aspects majeurs
- **Robert Pelletier** : 8° standard

### Tri
- **Astrotheme** : Par type puis orbe
- **Astrodienst** : Par type puis orbe

### Types Majeurs
- **Consensus** : Conjonction, Opposition, Carré, Trigone, Sextile (5 types)

## Notes Techniques

### Fonction get_max_orb()

```python
def get_max_orb(planet1: str, planet2: str) -> float:
    """Retourne 10° si luminaire, sinon 8°"""
    p1 = planet1.lower().replace('_', '').replace(' ', '')
    p2 = planet2.lower().replace('_', '').replace(' ', '')

    if p1 in LUMINARIES or p2 in LUMINARIES:
        return 10.0
    return 8.0
```

### Tri Astrotheme

```python
def sort_key(aspect):
    type_priority = ASPECT_SORT_ORDER.get(aspect['type'].lower(), 99)
    orb = abs(aspect['orb'])
    return (type_priority, orb)  # Tuple : type d'abord, orbe ensuite

filtered.sort(key=sort_key)
```

## Références

- **Plan initial** : `docs/ASPECT_V4_CORRECTION.md`
- **Standards** : Liz Greene (Astrodienst), Astrotheme
- **Issue** : Sprint 9 - Aspects manquants

---

**Auteur** : Claude Code
**Validé par** : Remi Beaurain
**Date de validation** : 2026-01-30
