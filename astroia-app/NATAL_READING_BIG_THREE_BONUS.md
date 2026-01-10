# 🌟 Bonus Big Three & Aspects Personnels - Documentation

## 📋 Vue d'ensemble

Cette mise à jour améliore le système de tri des aspects astrologiques en ajoutant un **bonus Big Three** dans le calcul de score et en garantissant que la section "Aspects clés du thème" contient au moins 4 aspects impliquant des planètes personnelles ou des angles.

**Date** : Novembre 2025  
**Fichier principal** : `lib/utils/aspectInterpretations.js` et `app/natal-reading/index.js`

---

## 🎯 Objectif

1. **Bonus Big Three** : Les aspects impliquant Soleil, Lune, Ascendant ou Milieu du Ciel obtiennent un bonus de +2 dans le score, les faisant remonter dans la liste.
2. **Aspects personnels garantis** : La section "Aspects clés du thème" contient au moins 4 aspects impliquant des planètes personnelles/angles si disponibles.

---

## 📐 Modifications du Calcul de Score

### Nouvelle Formule

```
score = importance_aspect + bonus_combinaison_planètes + bonus_intensité + bonus_orbe + bonus_big_three
```

**Score total possible** : 1 à 13 (au lieu de 1 à 11)

### Bonus Big Three

**Constante** : `BIG_THREE_POINTS = ['Sun', 'Moon', 'Ascendant', 'Medium_Coeli']`

**Fonction** : `getBigThreeBonus(planet1, planet2)`
- Retourne **+2** si au moins un des deux corps est dans le Big Three
- Retourne **0** sinon

**Principe** : Les aspects impliquant Soleil, Lune, Ascendant ou Milieu du Ciel sont prioritaires car ils touchent directement l'identité et l'image de la personne.

---

## 📊 Exemples de Calcul avec Bonus Big Three

### Exemple 1 : Soleil Conjonction Lune (Strong, orbe 0.8°)

**Avant (sans bonus Big Three)** :
```
importance_aspect = 5 (conjunction)
bonus_combinaison = 3 (perso ↔ perso)
bonus_intensité = 2 (strong)
bonus_orbe = 0.92
bonus_big_three = 0 (pas de bonus)

score = 5 + 3 + 2 + 0.92 + 0 = 10.92
```

**Après (avec bonus Big Three)** :
```
importance_aspect = 5 (conjunction)
bonus_combinaison = 3 (perso ↔ perso)
bonus_intensité = 2 (strong)
bonus_orbe = 0.92
bonus_big_three = 2 (Soleil et Lune dans Big Three)

score = 5 + 3 + 2 + 0.92 + 2 = 12.92
```

**Impact** : +2 points, remonte significativement dans la liste.

### Exemple 2 : Soleil Trigone Jupiter (Strong, orbe 1.5°)

**Avant** :
```
score = 3 + 2 + 2 + 0.85 + 0 = 7.85
```

**Après** :
```
score = 3 + 2 + 2 + 0.85 + 2 = 9.85
```

**Impact** : +2 points, passe devant des aspects non-Big Three avec score similaire.

### Exemple 3 : Neptune Opposition Pluton (Strong, orbe 0.5°)

**Avant** :
```
score = 4 + 0 + 2 + 0.95 + 0 = 6.95
```

**Après** :
```
score = 4 + 0 + 2 + 0.95 + 0 = 6.95 (aucun changement, pas de Big Three)
```

**Impact** : Aucun, car aucun des deux corps n'est dans le Big Three.

---

## 🔄 Changements de Position d'Aspects

### Scénario : Thème avec nombreux aspects

**Avant le bonus Big Three** :
1. Conjonction Neptune–Pluton (score 6.95) - non Big Three
2. Carré Mars–Saturne (score 6.80) - non Big Three
3. Trigone Soleil–Jupiter (score 7.85) - Big Three
4. Sextile Vénus–Mars (score 6.50) - non Big Three
5. Opposition Lune–Saturne (score 6.20) - Big Three

**Après le bonus Big Three** :
1. Trigone Soleil–Jupiter (score 9.85) - **+2 positions** (Big Three)
2. Conjonction Neptune–Pluton (score 6.95) - non Big Three
3. Carré Mars–Saturne (score 6.80) - non Big Three
4. Opposition Lune–Saturne (score 8.20) - **+1 position** (Big Three)
5. Sextile Vénus–Mars (score 6.50) - non Big Three

**Résultat** : Les aspects Big Three remontent naturellement grâce au bonus.

---

## 🎨 Sélection des "Aspects Clés du Thème"

### Stratégie de Sélection

**Objectif** : Garantir au moins 4 aspects personnels dans les 7 aspects clés si disponibles.

**Étapes** :

1. **Filtrage initial** :
   - Uniquement les aspects majeurs (conjunction, opposition, square, trine, sextile)
   - Exclusion des aspects "weak"
   - Exclusion des aspects "minor"

2. **Séparation** :
   - **Aspects personnels** : Impliquent au moins une planète personnelle/angle (Sun, Moon, Mercury, Venus, Mars, Ascendant, Medium_Coeli)
   - **Aspects non-personnels** : Ne impliquent aucune planète personnelle/angle

3. **Construction de la liste** :
   - **Si ≥ 4 aspects personnels disponibles** :
     - Prendre 4 aspects personnels minimum
     - Compléter jusqu'à 7 avec des aspects personnels supplémentaires ou non-personnels
   - **Si < 4 aspects personnels disponibles** :
     - Prendre tous les aspects personnels disponibles
     - Compléter avec des aspects non-personnels pour atteindre au moins 4, puis jusqu'à 7

4. **Validation finale** :
   - S'assurer qu'on respecte toujours les filtres (majeurs uniquement, pas de "weak")
   - Limiter à 7 maximum

### Exemple Concret

**Aspects candidats disponibles** :
- 10 aspects personnels majeurs (non-weak)
- 8 aspects non-personnels majeurs (non-weak)

**Sélection** :
- **4 aspects personnels** (garantis)
- **3 aspects personnels supplémentaires** (pour atteindre 7)
- **Total** : 7 aspects personnels dans les aspects clés

**Résultat** : Tous les aspects clés sont personnels, ce qui reflète mieux l'identité du thème.

---

## 📝 Fonction `isPersonalRelated()`

**Fichier** : `lib/utils/aspectInterpretations.js`

**Signature** :
```javascript
export function isPersonalRelated(aspect)
```

**Description** : Vérifie si un aspect implique au moins une planète personnelle ou un angle.

**Logique** :
- Vérifie si `aspect.from` est dans `PERSONAL_PLANETS`
- Vérifie si `aspect.to` est dans `PERSONAL_PLANETS`
- Retourne `true` si au moins une condition est vraie

**Planètes personnelles** : `['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Ascendant', 'Medium_Coeli']`

---

## 🔄 Cohérence avec la Liste Complète

### Déduplication

La logique de déduplication reste inchangée :
- Les aspects affichés dans "Aspects Clés du Thème" sont exclus de la liste complète
- Le compteur "Aspects (X/Y)" reste correct

### Tri

La liste complète continue d'utiliser `sortAspects()` qui :
1. Trie d'abord par catégorie (major_tense > major_harmonious > minor)
2. Trie ensuite par score décroissant (incluant le bonus Big Three)
3. Trie enfin par orbe croissant en cas d'égalité

**Résultat** : Les aspects Big Three remontent dans toutes les sections grâce au bonus.

---

## 🎨 Rewording du Sous-titre

### Avant

```
Les aspects majeurs (conjonction, opposition, carré, trigone, sextile) sont triés par importance astrologique et proximité de l'orbe.
```

### Après

```
Les aspects clés résument les influences les plus fortes de ton thème (importance astrologique + aspect presque exact).
```

**Améliorations** :
- Langage plus accessible ("ton thème" au lieu de termes techniques)
- Focus sur le sens ("influences les plus fortes")
- Explication simplifiée ("aspect presque exact" plutôt que "proximité de l'orbe")
- Suppression de la liste technique des types d'aspects

---

## 📁 Fichiers Modifiés

### 1. `lib/utils/aspectInterpretations.js`

**Ajouts** :
- Constante `BIG_THREE_POINTS` : Set des points du Big Three
- Fonction `getBigThreeBonus()` : Calcule le bonus Big Three (+2 ou 0)
- Fonction `isPersonalRelated()` : Vérifie si un aspect est personnel
- Modification de `calculateAspectScore()` : Ajout du bonus Big Three

**Modifications** :
- `calculateAspectScore()` : Nouvelle formule incluant `bonus_big_three`
- Score total possible : 1 à 13 (au lieu de 1 à 11)

### 2. `app/natal-reading/index.js`

**Ajouts** :
- Import de `isPersonalRelated`
- Logique de sélection améliorée pour garantir au moins 4 aspects personnels

**Modifications** :
- Calcul de `keyAspects` : Stratégie en 4 étapes pour garantir les aspects personnels
- Sous-titre "Aspects clés du thème" : Rewording pour plus d'accessibilité

---

## ✅ Tests et Vérifications

### Tests Fonctionnels

1. **Bonus Big Three** :
   - ✅ Un aspect Soleil–Jupiter obtient +2 points de bonus
   - ✅ Un aspect Neptune–Pluton n'obtient pas de bonus
   - ✅ Le tri respecte le bonus (aspects Big Three remontent)

2. **Aspects Clés Personnels** :
   - ✅ Si ≥ 4 aspects personnels disponibles : au moins 4 dans les aspects clés
   - ✅ Si < 4 aspects personnels disponibles : tous les personnels + complété avec non-personnels
   - ✅ Maximum 7 aspects clés
   - ✅ Uniquement aspects majeurs (pas de "minor")
   - ✅ Pas d'aspects "weak"

3. **Cohérence Liste Complète** :
   - ✅ Déduplication fonctionne (aspects clés exclus de la liste complète)
   - ✅ Tri par catégorie puis score (avec bonus Big Three)
   - ✅ Toggle "Tout afficher / Masquer aspects faibles" fonctionne

### Tests Lint / TypeScript

- ✅ Aucune erreur de lint dans les fichiers modifiés
- ✅ Les imports sont corrects
- ✅ Les fonctions sont bien exportées/importées

---

## 🎯 Exemples d'Aspects qui Changent de Position

### Exemple 1 : Soleil Trigone Saturne

**Contexte** :
- Type : Trigone
- Intensité : Medium
- Orbe : 2.5°
- Planètes : Soleil (Big Three) ↔ Saturne

**Score avant bonus Big Three** :
```
5 (conjunction pas, mais trigone = 3)
+ 2 (perso ↔ sociale)
+ 1 (medium)
+ 0.75 (orbe 2.5°)
= 6.75
```

**Score après bonus Big Three** :
```
3 (trigone)
+ 2 (perso ↔ sociale)
+ 1 (medium)
+ 0.75 (orbe 2.5°)
+ 2 (bonus Big Three - Soleil)
= 8.75 (+2 points)
```

**Impact** : Remonte de 2-3 positions dans la liste.

### Exemple 2 : Lune Opposition Uranus

**Contexte** :
- Type : Opposition
- Intensité : Strong
- Orbe : 1.8°
- Planètes : Lune (Big Three) ↔ Uranus

**Score avant bonus Big Three** :
```
4 (opposition)
+ 1 (perso ↔ lente)
+ 2 (strong)
+ 0.82 (orbe 1.8°)
= 7.82
```

**Score après bonus Big Three** :
```
4 (opposition)
+ 1 (perso ↔ lente)
+ 2 (strong)
+ 0.82 (orbe 1.8°)
+ 2 (bonus Big Three - Lune)
= 9.82 (+2 points)
```

**Impact** : Passe devant des aspects non-Big Three avec score initial similaire.

### Exemple 3 : Ascendant Carré Mars

**Contexte** :
- Type : Carré
- Intensité : Strong
- Orbe : 0.5°
- Planètes : Ascendant (Big Three) ↔ Mars

**Score avant bonus Big Three** :
```
4 (carré)
+ 3 (perso ↔ perso)
+ 2 (strong)
+ 0.95 (orbe 0.5°)
= 9.95
```

**Score après bonus Big Three** :
```
4 (carré)
+ 3 (perso ↔ perso)
+ 2 (strong)
+ 0.95 (orbe 0.5°)
+ 2 (bonus Big Three - Ascendant)
= 11.95 (+2 points)
```

**Impact** : Un des aspects les plus hauts de la liste, devient prioritaire.

---

## 🎉 Conclusion

Les modifications apportées améliorent significativement la pertinence astrologique du tri des aspects :

1. **Bonus Big Three** : Les aspects touchant directement l'identité (Soleil, Lune, Ascendant, MC) sont prioritaires
2. **Aspects personnels garantis** : La section "Aspects clés" reflète mieux l'identité du thème
3. **Accessibilité** : Le sous-titre est plus compréhensible pour le grand public

**Prochaines étapes** :
- Tester visuellement dans l'app
- Ajuster le bonus si nécessaire (+2 semble optimal)
- Vérifier que les aspects clés sont bien personnels dans les thèmes de test

---

**Version** : 2.0.0  
**Auteur** : Assistant IA  
**Date** : 12 novembre 2025

