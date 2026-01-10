# 🔗 Système de Tri des Aspects Astrologiques - Documentation

## 📋 Vue d'ensemble

Ce document décrit la logique de tri des aspects astrologiques implémentée dans l'écran de lecture de thème natal. Le système priorise les aspects les plus importants selon les principes de l'astrologie traditionnelle et moderne.

**Date** : Novembre 2025  
**Fichier principal** : `lib/utils/aspectInterpretations.js`  
**Fonction principale** : `sortAspects(aspects)`

---

## 🎯 Objectif

Trier les aspects astrologiques selon leur importance, en combinant :
- **La catégorie d'aspect** : major_tense > major_harmonious > minor (hiérarchie astrologique classique)
- L'importance du type d'aspect (conjonction > opposition/carré > trigone > sextile > autres)
- La combinaison de planètes (personnelles > sociales > lentes)
- L'intensité calculée (strong > medium > weak)
- La proximité de l'orbe (plus petit = mieux)

---

## 📐 Classification et Tri des Aspects

### Catégories d'Aspects

Les aspects sont classés en 3 catégories selon l'astrologie classique :

| Catégorie | Types d'aspects | Poids | Description |
|-----------|----------------|-------|-------------|
| **major_tense** | Conjonction, Opposition, Carré | 1000 | Aspects tendus majeurs (priorité maximale) |
| **major_harmonious** | Trigone, Sextile | 500 | Aspects harmonieux majeurs |
| **minor** | Quintile, Sesquiquadrate, etc. | 0 | Aspects mineurs (tous les autres) |

**Hiérarchie** : `major_tense > major_harmonious > minor`

### Formule de Calcul du Score

```
score = importance_aspect + bonus_combinaison_planètes + bonus_intensité + bonus_orbe
```

**Score total possible** : 1 à 11

**Important** : Le tri s'effectue d'abord par catégorie (poids), puis par score décroissant au sein de chaque catégorie.

### 1. Importance du Type d'Aspect

| Type d'aspect | Score | Description |
|--------------|-------|-------------|
| `conjunction` | 5 | Conjonction = le plus important |
| `opposition` | 4 | Opposition = très important |
| `square` | 4 | Carré = très important |
| `trine` | 3 | Trigone = important |
| `sextile` | 2 | Sextile = modérément important |
| Autres (quintile, sesquiquadrate, etc.) | 1 | Aspects mineurs |

### 2. Bonus de Combinaison de Planètes

**Catégories de planètes** :

- **Planètes personnelles** : `["Sun", "Moon", "Mercury", "Venus", "Mars", "Ascendant", "Medium_Coeli"]`
- **Planètes sociales** : `["Jupiter", "Saturn"]`
- **Planètes lentes / Points** : Tout le reste (Uranus, Neptune, Pluto, Lilith, Nodes, Chiron, etc.)

**Bonus selon la combinaison** :

| Combinaison | Bonus | Exemple |
|------------|-------|---------|
| perso ↔ perso | +3 | Soleil ↔ Lune |
| perso ↔ sociale | +2 | Soleil ↔ Jupiter |
| perso ↔ lente/point | +1 | Soleil ↔ Neptune |
| Autres combinaisons | 0 | Jupiter ↔ Saturne, Neptune ↔ Pluto, etc. |

### 3. Bonus d'Intensité

| Intensité | Bonus | Description |
|-----------|-------|-------------|
| `strong` | +2 | Aspect très marqué (orbe serré) |
| `medium` | +1 | Aspect modéré |
| `weak` | 0 | Aspect faible (orbe large) |

### 4. Bonus d'Orbe

**Formule** :
```
bonus_orbe = (10 - min(10, |orb|)) / 10
```

**Exemples** :
- Orbe 0.5° → `(10 - 0.5) / 10 = 0.95` (très élevé)
- Orbe 2.0° → `(10 - 2.0) / 10 = 0.80`
- Orbe 5.0° → `(10 - 5.0) / 10 = 0.50`
- Orbe 10.0°+ → `(10 - 10) / 10 = 0.00` (plafond)

**Principe** : Plus l'orbe est petit, plus le bonus est élevé. Un aspect exact (orbe < 1°) a un bonus maximal proche de 1.0.

---

## 🔢 Exemples de Calcul

### Exemple 1 : Soleil Conjonction Lune (Strong, orbe 0.8°)

```
importance_aspect = 5 (conjunction)
bonus_combinaison = 3 (perso ↔ perso)
bonus_intensité = 2 (strong)
bonus_orbe = (10 - 0.8) / 10 = 0.92

score = 5 + 3 + 2 + 0.92 = 10.92
```

**Résultat** : Très haut score, apparaîtra en premier.

### Exemple 2 : Jupiter Trigone Neptune (Medium, orbe 3.5°)

```
importance_aspect = 3 (trine)
bonus_combinaison = 0 (sociale ↔ lente)
bonus_intensité = 1 (medium)
bonus_orbe = (10 - 3.5) / 10 = 0.65

score = 3 + 0 + 1 + 0.65 = 4.65
```

**Résultat** : Score modéré, apparaîtra plus bas dans la liste.

### Exemple 3 : Mercure Quintile Nœud Sud (Strong, orbe 0.1°)

```
importance_aspect = 1 (quintile)
bonus_combinaison = 1 (perso ↔ lente)
bonus_intensité = 2 (strong)
bonus_orbe = (10 - 0.1) / 10 = 0.99

score = 1 + 1 + 2 + 0.99 = 4.99
```

**Résultat** : Malgré un aspect mineur (quintile), le score est élevé grâce à l'orbe très serré et l'intensité strong.

---

## 📊 Règles de Sélection des "Aspects Clés du Thème"

### Critères

1. **Tri** : Tous les aspects sont triés par `sortAspects()` (par catégorie puis score)
2. **Filtrage** :
   - **Uniquement les aspects majeurs** : conjunction, opposition, square, trine, sextile
   - Exclusion des aspects avec `strength === 'weak'`
3. **Limite** : Les 7 premiers aspects après filtrage

### Exemple

Si on a 41 aspects triés :
- 15 aspects majeurs (10 "strong" + 5 "medium")
- 12 aspects majeurs "weak" (exclus)
- 14 aspects mineurs (tous exclus de cette section)

**Aspects clés** : Les 7 premiers parmi les 15 aspects majeurs non-"weak" (donc les 7 plus importants selon la hiérarchie catégorie + score).

---

## 🎨 Organisation de l'UI

### Section "Aspects Clés du Thème"

- **Position** : Après les positions planétaires, avant la liste complète
- **Titre** : `🔗 Aspects clés du thème`
- **Sous-titre** : `Les aspects majeurs (conjonction, opposition, carré, trigone, sextile) sont triés par importance astrologique et proximité de l'orbe.`
- **Contenu** : Jusqu'à 7 aspects majeurs uniquement (excluant les "weak" et les aspects mineurs)
- **Affichage** : Cartes avec emoji, type, planètes, orbe, badge d'intensité, mini-interprétation

### Section "Aspects" (Liste Complète)

- **Position** : Après "Aspects Clés du Thème"
- **Titre** : `🔗 Aspects (X/Y)` où X = aspects affichés, Y = total
- **Bouton toggle** :
  - `🔼 Tout afficher` : Affiche tous les aspects (y compris "weak")
  - `🔽 Masquer aspects faibles` : Cache les aspects "weak"
- **Contenu** : Tous les aspects triés **par catégorie puis score** (major_tense > major_harmonious > minor), **excluant ceux déjà affichés dans "Aspects Clés"** (évite les doublons)
- **Affichage** : Même format que les aspects clés
- **Ordre d'affichage** :
  1. Aspects tendus majeurs (conjonction, opposition, carré)
  2. Aspects harmonieux majeurs (trigone, sextile)
  3. Aspects mineurs (quintile, sesquiquadrate, etc.)

### Logique de Déduplication

Pour éviter d'afficher deux fois le même aspect :

1. Création d'un `Set` des IDs des aspects clés :
   ```javascript
   const keyAspectIds = new Set(
     keyAspects.map(asp => `${asp.from}-${asp.to}-${asp.aspect_type}`)
   );
   ```

2. Filtrage de la liste complète :
   ```javascript
   const filteredAspects = sortedAspects.filter(asp => {
     const aspectId = `${asp.from}-${asp.to}-${asp.aspect_type}`;
     return !keyAspectIds.has(aspectId);
   });
   ```

**Résultat** : Les aspects clés n'apparaissent qu'une seule fois dans l'UI.

---

## 🔍 Comparaison avec l'Ancien Système

### Avant (filterAspectsByRelevance)

- Tri simple par force (strong > medium > weak)
- En cas d'égalité, tri par orbe croissant
- Pas de prise en compte du type d'aspect
- Pas de prise en compte des planètes

### Après (sortAspects v1)

- Score composite multi-critères
- Priorité aux aspects majeurs (conjonction, opposition, carré)
- Priorité aux planètes personnelles
- Bonus d'orbe plus nuancé
- Tri plus précis et conforme à l'astrologie traditionnelle

### Après (sortAspects v2 - Actuel)

- **Hiérarchie par catégorie** : major_tense > major_harmonious > minor
- Score composite au sein de chaque catégorie
- Section "Aspects Clés" limitée aux aspects majeurs uniquement
- Liste complète triée par catégorie puis score
- Conforme aux usages astrologiques classiques

---

## 📁 Fichiers Modifiés

### Créés / Modifiés

1. **`lib/utils/aspectInterpretations.js`**
   - Ajout de `sortAspects()` : Fonction principale de tri (par catégorie puis score)
   - Ajout de `getAspectCategory()` : Classification des aspects (major_tense, major_harmonious, minor)
   - Ajout de `calculateAspectScore()` : Calcul du score
   - Ajout de `getPlanetCategory()` : Catégorisation des planètes
   - Ajout de `getPlanetCombinationBonus()` : Bonus de combinaison
   - Ajout de `getIntensityBonus()` : Bonus d'intensité
   - Ajout de `getOrbBonus()` : Bonus d'orbe
   - Définition des constantes : `MAJOR_ASPECTS`, `ASPECT_CATEGORIES`, `CATEGORY_WEIGHT`, `ASPECT_IMPORTANCE`, `PERSONAL_PLANETS`, `SOCIAL_PLANETS`
   - `filterAspectsByRelevance()` marquée comme dépréciée (conservée pour compatibilité)

2. **`app/natal-reading/index.js`**
   - Import de `sortAspects` et `MAJOR_ASPECTS`
   - Calcul de `keyAspects` : Les 7 premiers aspects **majeurs uniquement** (excluant "weak" et "minor")
   - Calcul de `filteredAspects` : Liste complète triée par catégorie puis score, avec déduplication
   - Ajout de la section "Aspects Clés du Thème" (uniquement aspects majeurs)
   - Réorganisation de la section "Aspects" (liste complète triée par catégorie)
   - Mise à jour du sous-titre pour préciser "aspects majeurs"
   - Ajout du style `aspectsSubtitle`
   - Correction du compteur d'aspects affichés

3. **`lib/utils/astrologyTranslations.js`**
   - Ajout de `'Lilith': 'Lilith'` pour gérer la variante sans préfixe

---

## ✅ Tests et Vérifications

### Tests Manuels

1. **Vérifier le tri** :
   - Les aspects tendus majeurs (conjonction, opposition, carré) apparaissent en premier
   - Les aspects harmonieux majeurs (trigone, sextile) apparaissent ensuite
   - Les aspects mineurs (quintile, etc.) apparaissent en dernier
   - Au sein de chaque catégorie, tri par score décroissant
   - Les aspects impliquant des planètes personnelles sont prioritaires
   - Les aspects avec orbe serré sont mieux classés

2. **Vérifier la section "Aspects Clés"** :
   - Affiche au maximum 7 aspects
   - N'affiche **que des aspects majeurs** (conjunction, opposition, square, trine, sextile)
   - N'affiche pas d'aspects "weak"
   - N'affiche pas d'aspects mineurs (quintile, etc.)
   - Les aspects sont triés par catégorie puis score

3. **Vérifier la liste complète** :
   - Respecte l'ordre : major_tense > major_harmonious > minor
   - Ne duplique pas les aspects déjà affichés dans "Aspects Clés"
   - Le compteur (X/Y) reste correct

3. **Vérifier la déduplication** :
   - Un aspect affiché dans "Aspects Clés" n'apparaît pas dans la liste complète
   - Le compteur d'aspects est correct (X/Y)

4. **Vérifier le toggle** :
   - "Tout afficher" : Affiche tous les aspects (y compris "weak")
   - "Masquer aspects faibles" : Cache les "weak"
   - Le compteur se met à jour correctement

### Tests Automatisés

```bash
# Linter
npm run lint

# Type-check
npm run typecheck

# Tests Jest
npm test
```

**Résultat** : ✅ Aucune erreur de lint détectée.

---

## 🎯 Choix UX

### Nombre d'Aspects Clés

**Choix** : 7 aspects clés

**Rationale** :
- Assez pour couvrir les aspects majeurs du thème
- Pas trop pour ne pas surcharger l'écran
- Facilement ajustable (modifier `.slice(0, 7)`)

### Exclusion des "Weak"

**Choix** : Exclure les aspects "weak" des aspects clés

**Rationale** :
- Les aspects "weak" sont moins significatifs
- L'utilisateur peut les voir dans la liste complète s'il le souhaite
- Garde la section "Aspects Clés" concise et pertinente

### Déduplication

**Choix** : Exclure les aspects clés de la liste complète

**Rationale** :
- Évite la confusion visuelle
- Évite le doublon d'information
- L'utilisateur voit d'abord les aspects clés, puis les autres

---

## 📝 Exemples Concrets d'Ordre d'Affichage

### Exemple 1 : Thème avec Aspects Variés

**Aspects triés (ordre d'affichage)** :

1. **Aspects Clés du Thème** (7 premiers, uniquement majeurs) :
   - Conjonction Soleil–Pluton (strong, orbe 0.5°)
   - Carré Lune–Saturne (strong, orbe 1.2°)
   - Opposition Mars–Jupiter (medium, orbe 2.8°)
   - Trigone Soleil–Jupiter (strong, orbe 0.9°)
   - Sextile Vénus–Mars (medium, orbe 3.1°)
   - Conjonction Mercure–Vénus (medium, orbe 4.2°)
   - Carré Ascendant–Saturne (medium, orbe 5.0°)

2. **Aspects (Liste Complète)** - Suite, triés par catégorie :
   - **Aspects tendus majeurs** restants :
     - Conjonction Neptune–Pluton (weak, orbe 6.5°) — si "Tout afficher"
   - **Aspects harmonieux majeurs** restants :
     - Trigone Uranus–Neptune (medium, orbe 3.8°)
     - Sextile Mars–Uranus (weak, orbe 7.2°) — si "Tout afficher"
   - **Aspects mineurs** :
     - Quintile Soleil–Lune (strong, orbe 0.3°)
     - Quintile Vénus–Jupiter (medium, orbe 2.1°)
     - Sesquiquadrate Mars–Saturne (weak, orbe 8.0°) — si "Tout afficher"

### Exemple 2 : Cas Limite

Si un thème n'a que 5 aspects majeurs (tous non-"weak"), alors :
- **Aspects Clés** : Les 5 aspects majeurs
- **Aspects (Liste Complète)** : Tous les aspects mineurs triés par score

---

## 🔮 Améliorations Futures Possibles

### Court Terme

1. **Personnalisation du nombre d'aspects clés**
   - Paramètre utilisateur (5, 7, 10)
   - Sauvegarde dans les préférences

2. **Filtres avancés**
   - Filtrer par type d'aspect (conjonction uniquement, etc.)
   - Filtrer par planète (Soleil uniquement, etc.)
   - Filtrer par maison

### Moyen Terme

3. **Visualisation graphique**
   - Carte du ciel avec les aspects dessinés
   - Graphique de répartition des aspects par type
   - Graphique de répartition par intensité

4. **Comparaison de thèmes**
   - Comparer deux thèmes natals
   - Aspects communs / différents
   - Synastrie (aspects entre deux thèmes)

---

## 📚 Références Astrologiques

### Importance des Aspects

Selon l'astrologie traditionnelle :

1. **Aspects majeurs** (conjonction, opposition, carré, trigone, sextile) : Les plus importants
2. **Aspects mineurs** (quintile, sesquiquadrate, etc.) : Moins importants mais significatifs si l'orbe est serré

### Importance des Planètes

1. **Planètes personnelles** : Liées à la personnalité individuelle
2. **Planètes sociales** : Liées à la société et aux structures
3. **Planètes lentes** : Influences générationnelles et transpersonnelles

### Importance de l'Orbe

- **Aspect exact** (orbe < 1°) : Effet maximal
- **Aspect serré** (orbe < 3°) : Effet important
- **Aspect large** (orbe > 5°) : Effet atténué

---

## 🎉 Conclusion

Le système de tri des aspects est maintenant conforme aux principes de l'astrologie traditionnelle et moderne. Il priorise les aspects les plus significatifs tout en restant flexible et extensible.

**Prochaines étapes** :
1. Tester visuellement dans l'app
2. Ajuster les poids si nécessaire (importance, bonus, etc.)
3. Ajouter des filtres avancés si demandé

---

**Version** : 1.0.0  
**Auteur** : Assistant IA  
**Date** : 12 novembre 2025

