# 📊 Tri et Interprétation des Aspects Astrologiques

## Vue d'ensemble

Ce document décrit le système de tri professionnel des aspects astrologiques et la génération d'interprétations lisibles pour l'application Astro.IA.

**Version** : 3.0.0  
**Date** : Novembre 2025  
**Fichiers principaux** :
- `lib/utils/aspectCategories.ts` - Catégorisation et tri
- `lib/utils/aspectTextTemplates.ts` - Templates d'interprétation
- `lib/utils/gptInterpreter.ts` - Mode GPT optionnel
- `lib/utils/profileGenerator.ts` - Génération de profil

---

## 🎯 Objectifs

1. **Tri astrologique professionnel** : Hiérarchie conforme aux pratiques astrologiques classiques
2. **Interprétations lisibles** : Templates en français compréhensibles pour le grand public
3. **Sélection intelligente** : Garantir des aspects personnels dans les "Aspects clés"
4. **Flexibilité** : Support du mode GPT optionnel pour des interprétations enrichies

---

## 📐 Hiérarchie de Tri

### Priorité 1 : Aspects Majeurs Tendus

Ces aspects sont les plus importants et les plus influents :

- **Conjonction** (conjunction) - Poids : 3000
- **Opposition** (opposition) - Poids : 2900
- **Carré** (square) - Poids : 2800

### Priorité 2 : Aspects Majeurs Harmonieux

Ces aspects apportent de la fluidité et de l'harmonie :

- **Trigone** (trine) - Poids : 2000
- **Sextile** (sextile) - Poids : 1900

### Priorité 3 : Aspects Mineurs

Tous les autres aspects (Quintile, Semi-sextile, Sesquiquadrate, etc.) :

- **Mineurs** - Poids : 1000

---

## 🔢 Calcul de la Clé de Tri

### Formule

```
cléDeTri = poidsType + poidsIntensité + scoreBase
```

### Composantes

1. **Poids du type d'aspect** (`poidsType`)
   - Conjonction : 3000
   - Opposition : 2900
   - Carré : 2800
   - Trigone : 2000
   - Sextile : 1900
   - Mineurs : 1000

2. **Poids de l'intensité** (`poidsIntensité`)
   - Fort (strong) : 300
   - Moyen (medium) : 200
   - Faible (weak) : 100

3. **Score de base** (`scoreBase`)
   - Bonus combinaison planètes : 0 à 30 points
     - Perso ↔ Perso : +30
     - Perso ↔ Sociale : +20
     - Perso ↔ Lente/Point : +10
   - Bonus orbe : 0 à 10 points (plus petit = mieux)
   - Bonus Big Three : 0 ou 20 points (si implique Soleil/Lune/Ascendant/MC)

### Exemples de Calcul

**Exemple 1 : Conjonction Forte Soleil-Lune (orbe 0.5°)**
```
poidsType = 3000 (conjunction)
poidsIntensité = 300 (strong)
scoreBase = 30 (perso↔perso) + 9.5 (orbe) + 20 (Big Three) = 59.5

cléDeTri = 3000 + 300 + 59.5 = 3359.5
```

**Exemple 2 : Sextile Faible Neptune-Pluton (orbe 5°)**
```
poidsType = 1900 (sextile)
poidsIntensité = 100 (weak)
scoreBase = 0 (lente↔lente) + 5 (orbe) + 0 (pas Big Three) = 5

cléDeTri = 1900 + 100 + 5 = 2005
```

**Résultat** : La conjonction Soleil-Lune est prioritaire (3359.5 > 2005).

---

## 📊 Tri Final

### Ordre de Tri

1. **Par catégorie** : Majeurs tendus > Majeurs harmonieux > Mineurs
2. **Par intensité** : Fort > Moyen > Faible (à l'intérieur de chaque catégorie)
3. **Par score de base** : Score élevé > Score faible (en cas d'égalité)
4. **Par orbe** : Orbe petit > Orbe grand (en cas d'égalité totale)

### Exemple de Tri

Aspects avant tri :
1. Sextile Moyen Neptune-Pluton (orbe 3°)
2. Conjonction Forte Soleil-Lune (orbe 0.5°)
3. Carré Forte Mars-Saturne (orbe 2°)
4. Trigone Moyen Vénus-Jupiter (orbe 4°)

Aspects après tri :
1. **Conjonction Forte Soleil-Lune** (3359.5)
2. **Carré Forte Mars-Saturne** (3100+)
3. **Trigone Moyen Vénus-Jupiter** (2200+)
4. **Sextile Moyen Neptune-Pluton** (2100+)

---

## 🔗 Sélection des "Aspects Clés du Thème"

### Règles de Sélection

1. **Nombre total** : Toujours 7 aspects maximum
2. **Minimum aspects personnels** : 4 aspects sur 7 doivent impliquer des planètes personnelles/angles
3. **Types d'aspects** : Uniquement les aspects majeurs (conjunction, opposition, square, trine, sextile)
4. **Intensité** : Exclusion des aspects "weak"

### Planètes Personnelles

- Soleil (Sun)
- Lune (Moon)
- Mercure (Mercury)
- Vénus (Venus)
- Mars (Mars)
- Ascendant
- Milieu du Ciel (Medium_Coeli)

### Stratégie de Sélection

**Étape 1** : Filtrer les aspects candidats (majeurs + non weak)

**Étape 2** : Séparer les aspects personnels des non-personnels

**Étape 3** : Construire la liste
- Si ≥ 4 aspects personnels disponibles :
  - Prendre 4 aspects personnels minimum
  - Compléter jusqu'à 7 avec des aspects personnels supplémentaires ou non-personnels
- Si < 4 aspects personnels disponibles :
  - Prendre tous les aspects personnels disponibles
  - Compléter avec des non-personnels pour atteindre 7

**Étape 4** : Validation finale (s'assurer que tous sont majeurs et non weak)

---

## 📝 Templates d'Interprétation

### Format

Chaque template génère une phrase en français lisible qui décrit l'influence de l'aspect.

### Templates par Type

#### Conjonction
```
"Fusion puissante entre Soleil et Lune : une énergie combinée qui amplifie leurs qualités. Soleil (identité et volonté) et Lune (émotions et besoins) se renforcent mutuellement."
```

#### Opposition
```
"Tension créatrice marquée entre Vénus et Mars : un tiraillement qui demande un équilibre. Vénus (affects et valeurs) et Mars (action et désir) se complètent en s'opposant."
```

#### Carré
```
"Friction dynamique intense : Mercure et Jupiter s'affrontent, incitant à un ajustement intérieur. Mercure (communication et pensée) et Jupiter (expansion et chance) créent une tension constructive."
```

#### Trigone
```
"Harmonie fluide profonde : Soleil et Jupiter coopèrent naturellement. Soleil (identité et volonté) et Jupiter (expansion et chance) s'entraident avec facilité."
```

#### Sextile
```
"Opportunité positive marquée : Vénus et Mars s'entraident de manière constructive. Vénus (affects et valeurs) et Mars (action et désir) forment un duo complémentaire."
```

#### Aspect Mineur
```
"Soleil et Neptune forment un aspect subtil mais notable (quintile), influençant en toile de fond. Soleil (identité et volonté) et Neptune (intuition et rêves) créent une connexion discrète."
```

### Adaptation selon l'Intensité

- **Fort (strong)** : Version enrichie avec détails supplémentaires
- **Moyen (medium)** : Version standard
- **Faible (weak)** : Version simplifiée

---

## 🤖 Mode GPT Optionnel

### Activation

Le mode GPT peut être activé via la variable `USE_GPT_INTERP` dans `lib/utils/gptInterpreter.ts`.

```typescript
import { setUseGPTInterp } from '@/lib/utils/gptInterpreter';

// Activer le mode GPT
setUseGPTInterp(true);

// Désactiver le mode GPT
setUseGPTInterp(false);
```

### Comportement

- **Mode GPT activé** : Les interprétations sont générées via l'API GPT (à implémenter)
- **Mode GPT désactivé** : Utilisation des templates locaux (par défaut)

### TODO : Intégration GPT

L'intégration complète de GPT nécessite :
1. Configuration de l'API GPT
2. Création des prompts astrologiques
3. Gestion du cache et de la limite de tokens
4. Fallback sur templates en cas d'erreur

---

## 📖 Génération de Profil Astrologique

### Template Local

Le profil génère un texte basé sur :
- **Big Three** : Soleil, Lune, Ascendant
- **Élément dominant** : Si disponible
- **Positions planétaires** : Planètes personnelles

### Exemple de Profil

```
Ton Soleil en Bélier révèle une personnalité dynamique, entreprenante, impulsive. Ta Lune en Cancer colore ton monde émotionnel de sensible, protecteur, intuitif. L'Ascendant en Balance façonne ta manière d'être perçu(e) : harmonieux, diplomate, esthète. Ces trois piliers composent l'essence de ton thème natal. L'élément Feu domine ton thème, imprégnant tes choix et ta façon d'être.
```

### Mode GPT

Si activé, le profil peut être enrichi via GPT avec :
- Analyse plus approfondie des combinaisons
- Interprétation des maisons
- Synthèse des aspects majeurs

---

## 🧪 Tests

### Tests de Tri

**Fichier** : `__tests__/utils/aspectCategories.test.ts`

Vérifie :
- Catégorisation correcte (majeur tendu, majeur harmonieux, mineur)
- Poids des types d'aspects
- Poids des intensités
- Calcul de la clé de tri
- Ordre de tri (conjonction forte > opposition forte > sextile fort > sextile moyen)

### Tests d'Interprétation

**Fichier** : `__tests__/utils/aspectTextTemplates.test.ts`

Vérifie :
- Génération de texte pour chaque type d'aspect
- Remplacement correct des noms de planètes
- Phrases complètes et lisibles en français
- Absence de tokens non remplacés

---

## 📁 Structure des Fichiers

```
lib/utils/
├── aspectCategories.ts       # Catégorisation et tri
├── aspectTextTemplates.ts    # Templates d'interprétation
├── gptInterpreter.ts         # Mode GPT optionnel
├── profileGenerator.ts       # Génération de profil
└── aspectInterpretations.js  # Fonctions utilitaires (anciennes)

app/natal-reading/
└── index.js                  # Écran principal (utilise les nouveaux modules)

__tests__/utils/
├── aspectCategories.test.ts     # Tests de tri
└── aspectTextTemplates.test.ts  # Tests d'interprétation

docs/
└── ASPECT_SORTING_AND_INTERPRETATION.md  # Cette documentation
```

---

## 🔄 Migration depuis l'Ancien Système

### Changements Majeurs

1. **Tri** : Nouvelle hiérarchie avec poids précis au lieu de catégories floues
2. **Interprétations** : Templates lisibles au lieu de phrases génériques
3. **Profil** : Génération cohérente au lieu de phrases absurdes de l'API
4. **Sélection** : Garantie d'aspects personnels dans les aspects clés

### Compatibilité

L'ancien système est conservé en fallback si les nouveaux modules ne peuvent pas être chargés :
- `generateAspectInterpretation()` (ancien) reste disponible
- `generateBigThreeSummary()` (ancien) reste disponible
- `sortAspects()` utilise la nouvelle logique mais a un fallback

---

## 🚀 Prochaines Étapes

1. **Intégration GPT** : Implémenter les appels API réels
2. **Cache** : Mettre en cache les interprétations GPT
3. **Personnalisation** : Ajouter des variations selon les signes/maisons
4. **Tests E2E** : Vérifier le comportement complet dans l'app

---

**Version** : 3.0.0  
**Auteur** : Assistant IA  
**Date** : Novembre 2025

