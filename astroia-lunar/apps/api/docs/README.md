# Documentation API Astroia Lunar

## Vue d'ensemble

Ce répertoire contient la documentation technique détaillée des fonctionnalités de l'API Astroia Lunar.

---

## Table des matières

### 1. Transits - Filtrage des aspects majeurs
Documentation complète du paramètre `major_only` pour filtrer les transits et ne retourner que les 4 aspects majeurs.

#### Fichiers:
- **[TRANSITS_MAJOR_FILTERING.md](./TRANSITS_MAJOR_FILTERING.md)** *(Documentation complète - 14 KB)*
  - Architecture détaillée du filtrage
  - Flux de propagation du paramètre
  - Code source commenté
  - Validation par tests (12 tests unitaires)
  - Schémas techniques

- **[TRANSITS_MAJOR_FILTERING_SUMMARY.md](./TRANSITS_MAJOR_FILTERING_SUMMARY.md)** *(Résumé exécutif - 6 KB)*
  - Vue d'ensemble rapide
  - Flux simplifié
  - Points d'entrée API
  - Validation finale

- **[TRANSITS_MAJOR_FILTERING_EXAMPLES.md](./TRANSITS_MAJOR_FILTERING_EXAMPLES.md)** *(Guide pratique - 14 KB)*
  - Exemples concrets d'appels API
  - Cas d'usage pratiques (mobile, expert, toggle)
  - Comparaison aspects majeurs vs mineurs
  - Scripts de validation
  - Débogage et résolution de problèmes

#### Commit de référence:
- **f3cde98**: "feat(mobile): déplacer filtrage transits majeurs vers backend"

---

### 2. Void of Course - Optimisations cache
Documentation des optimisations du cache VoC et de la retry logic.

#### Fichier:
- **[VOC_CACHE_OPTIMIZATIONS.md](./VOC_CACHE_OPTIMIZATIONS.md)** *(Documentation technique - 7 KB)*
  - Système de cache avec TTL
  - Retry logic avec exponential backoff
  - Métriques de performance
  - Tests de validation

#### Commit de référence:
- **11d8e75**: "feat(api): optimiser VoC Status avec cache et retry logic"

---

### 3. Interprétations natales
Documentation des systèmes d'interprétation des thèmes natals.

#### Fichiers:
- **[NATAL_INTERPRETATION_V3.md](./NATAL_INTERPRETATION_V3.md)** *(Version 3 - 5 KB)*
  - Système d'interprétation V3
  - Format de réponse
  - Exemples

- **[NATAL_INTERPRETATION_V4.md](./NATAL_INTERPRETATION_V4.md)** *(Version 4 - 13 KB)*
  - Évolution vers V4
  - Amélioration des prompts
  - Gestion des erreurs
  - Tests de validation

---

### 4. Explications des aspects
Documentation du service d'explication des aspects astrologiques.

#### Fichier:
- **[ASPECT_EXPLANATIONS_V4.md](./ASPECT_EXPLANATIONS_V4.md)** *(Documentation V4 - 17 KB)*
  - Système d'explication V4
  - Prompts Anthropic Claude
  - Format de réponse
  - Exemples d'utilisation

---

## Organisation des documents

### Conventions de nommage
- `FEATURE_NAME.md` - Documentation technique complète
- `FEATURE_NAME_SUMMARY.md` - Résumé exécutif (vue d'ensemble)
- `FEATURE_NAME_EXAMPLES.md` - Guide pratique avec exemples
- `FEATURE_NAME_VX.md` - Documentation versionnée (X = numéro de version)

### Structure recommandée pour nouveaux documents

```markdown
# Titre de la fonctionnalité

## Vue d'ensemble
Brève description (1-2 paragraphes)

## Architecture
Détails techniques

## Utilisation
Exemples concrets

## Tests
Validation et vérification

## Références
Commits, fichiers, liens
```

---

## Tests associés

### Transits (filtrage major_only)
```bash
# Tests unitaires (12 tests)
cd apps/api
pytest tests/test_transits_major.py -v

# Validation manuelle (5 tests)
python scripts/test_major_only_flow.py
```

### VoC Cache
```bash
# Tests unitaires
cd apps/api
pytest tests/test_voc_cache_service.py -v
```

### Interprétations natales
```bash
# Tests d'intégration
cd apps/api
pytest tests/test_natal_interpretation.py -v
```

---

## Scripts de validation

### Emplacement: `/apps/api/scripts/`

- **test_major_only_flow.py** - Validation complète du filtrage major_only (5 tests)
- **test_lunar_report_format.py** - Validation du format des rapports lunaires

**Exécution:**
```bash
cd apps/api
python scripts/test_major_only_flow.py
```

---

## Commits importants

### Chantier 4: Optimisation transits majeurs
- **f3cde98** - "feat(mobile): déplacer filtrage transits majeurs vers backend"
  - Ajout paramètre `major_only` sur 3 endpoints
  - Fonction `filter_major_aspects_only()`
  - 12 tests de validation
  - Documentation complète

- **11d8e75** - "feat(api): optimiser VoC Status avec cache et retry logic"
  - Système de cache avec TTL 6h
  - Retry logic avec exponential backoff
  - Métriques de performance

### Chantier 6: Nettoyage cycle menstruel
- **2d4c146** - "feat(mobile): nettoyer code cycle menstruel hors MVP"
  - Suppression fonctionnalités hors MVP
  - Nettoyage codebase

---

## Contribution

### Ajouter une nouvelle documentation

1. **Créer le fichier principal:**
   ```bash
   touch docs/FEATURE_NAME.md
   ```

2. **Créer les fichiers complémentaires (optionnels):**
   ```bash
   touch docs/FEATURE_NAME_SUMMARY.md
   touch docs/FEATURE_NAME_EXAMPLES.md
   ```

3. **Mettre à jour ce README:**
   - Ajouter la nouvelle section dans la table des matières
   - Lier les fichiers créés
   - Indiquer le commit de référence

4. **Ajouter les tests associés:**
   - Créer les tests dans `/apps/api/tests/`
   - Créer les scripts de validation dans `/apps/api/scripts/`
   - Documenter l'exécution des tests dans ce README

---

## Ressources externes

### Documentation API
- Swagger UI: `http://localhost:8000/docs` (FastAPI auto-généré)
- ReDoc: `http://localhost:8000/redoc` (FastAPI auto-généré)

### Providers externes
- **RapidAPI Astrology** - Calculs astrologiques (transits, thèmes natals, révolutions lunaires)
- **Anthropic Claude API** - Interprétations et explications (via IA générative)

### Dépendances
- FastAPI (routes et validation)
- SQLAlchemy (ORM et modèles DB)
- Pytest (tests unitaires et d'intégration)
- httpx (client HTTP async)

---

## Statut de la documentation

| Fonctionnalité | Documentation | Exemples | Tests | Statut |
|----------------|---------------|----------|-------|--------|
| Transits (major_only) | ✅ | ✅ | ✅ 12/12 | **Complet** |
| VoC Cache | ✅ | ⚠️ Partiel | ✅ | **Bon** |
| Interprétations natales | ✅ | ⚠️ Partiel | ✅ | **Bon** |
| Explications aspects | ✅ | ⚠️ Partiel | ⚠️ Partiel | **Moyen** |

**Légende:**
- ✅ Complet
- ⚠️ Partiel
- ❌ Manquant

---

## Prochaines étapes

1. **Compléter les exemples** pour VoC Cache et Interprétations natales
2. **Ajouter monitoring** pour les endpoints critiques (transits, VoC)
3. **Documenter les erreurs** courantes et leur résolution
4. **Créer guide de déploiement** avec configuration production

---

## Contact

Pour toute question sur cette documentation:
- Ouvrir une issue dans le repo
- Consulter les commits de référence pour le contexte
- Exécuter les tests pour valider le comportement

---

## Changelog de la documentation

### 2025-01-16
- ✅ Ajout documentation complète filtrage major_only (3 fichiers)
- ✅ Ajout script de validation test_major_only_flow.py
- ✅ Création de ce README

### 2025-01-15
- ✅ Documentation VoC Cache optimizations
- ✅ Tests unitaires VoC Cache

### 2024-12-31
- ✅ Documentation Aspect Explanations V4

### 2024-12-29
- ✅ Documentation Natal Interpretation V3 et V4

---

**Dernière mise à jour:** 2025-01-16
