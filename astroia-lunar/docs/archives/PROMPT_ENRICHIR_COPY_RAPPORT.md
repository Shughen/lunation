# PROMPT : Enrichir Copy Rapport Lunaire MVP (Chantier Bloquant)

**Contexte :** Le système de génération de rapports lunaires mensuels produit un copy de qualité exceptionnelle (ton senior, manifestations concrètes, structure solide), MAIS 1 rapport sur 3 passe sous le minimum MVP de 300 mots. L'audit qualité (Tâche 2.3, voir `LUNAR_COPY_AUDIT.md`) a identifié 2 sections trop courtes qui nécessitent enrichissement.

**Objectif :** Enrichir les sections "Climat général" et "Axes dominants" des rapports lunaires pour atteindre 100% de conformité MVP (tous rapports > 300 mots).

---

## 🎯 SPÉCIFICATIONS TECHNIQUES

### État Actuel (Problème)

**Rapport généré :** Format JSON avec 4 sections
```json
{
  "header": {...},
  "general_climate": "Texte court (28 mots)", // ❌ TROP COURT (cible: 120 mots)
  "dominant_axes": "Texte court (20 mots)",   // ❌ TROP COURT (cible: 100 mots)
  "major_aspects": [...] // ✅ OK (270 mots)
}
```

**Conformité actuelle :** 66% (2/3 rapports)
- Rapport Bélier M1 : 394 mots ✅
- Rapport Taureau M2 : 282 mots ❌ (< 300 minimum)
- Rapport Gémeaux M3 : 400 mots ✅

**Cause :** Sections `general_climate` et `dominant_axes` générées avec templates minimalistes.

---

### Objectif Cible

**Longueur par section :**
1. **Climat général** : 28 → **120 mots** (+92 mots, ~600 caractères)
2. **Axes dominants** : 20 → **100 mots** (+80 mots, ~500 caractères)

**Impact :** 100% rapports > 300 mots minimum MVP

**Conformité cible :** 100% (3/3 rapports)
- Bélier M1 : 394 → 520 mots ✅
- Taureau M2 : 282 → 420 mots ✅ (+ 138 mots → au-dessus de 300)
- Gémeaux M3 : 400 → 540 mots ✅

---

## 📂 FICHIERS À MODIFIER

### Fichier principal

**`/Users/remibeaurain/astroia/astroia-lunar/apps/api/services/aspect_explanation_service.py`**

Ce fichier contient :
- Fonction `build_lunar_report_v4()` (génération complète rapport)
- Templates pour `general_climate` et `dominant_axes`
- Logique de sélection des axes dominants (top 2-3 maisons)

### Fichiers de référence (lecture seule)

**Audit qualité (comprendre les critères) :**
- `/Users/remibeaurain/astroia/astroia-lunar/LUNAR_COPY_AUDIT.md` (analyse détaillée)
- `/Users/remibeaurain/astroia/astroia-lunar/COPY_IMPROVEMENTS_ROADMAP.md` (plan technique complet)
- `/Users/remibeaurain/astroia/astroia-lunar/COPY_EXAMPLES_REFERENCE.md` (exemples validés)

**Tests existants (validation) :**
- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/tests/test_lunar_report.py` (8 tests)
- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/scripts/test_lunar_report_format.py` (script validation)

**Données lunaires :**
- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/models/lunar_return.py` (modèle DB)

---

## 🎨 CRITÈRES DE QUALITÉ MVP (IMPÉRATIFS)

### 1. Ton Senior/Factuel (priorité absolue)
- ❌ **INTERDITS :** "énergie cosmique", "vibrations", "karma", "destin", "univers bienveillant"
- ✅ **RECOMMANDÉS :** "dynamique", "levier", "friction", "fusion", "catalyseur", "moteur"
- **Cible :** Maximum 2 mots ésotériques par section (actuellement 0-1, excellent)
- **Style :** Professionnel, technique mais accessible, non infantilisant

### 2. Manifestations Concrètes (actionnable)
- Descriptions de situations observables
- Exemples pratiques (vie quotidienne, relations, travail)
- Conseils applicables immédiatement
- Format "Concrètement : [exemple réel]"

### 3. Structure Pédagogique
- Progression logique (général → spécifique)
- Liens explicites entre concepts
- Contexte personnalisé (signe lunaire + maison)

### 4. Longueur Cible
- **Climat général :** 100-150 mots (cible idéale : 120 mots)
- **Axes dominants :** 80-120 mots (cible idéale : 100 mots)
- **Total rapport :** 400-600 mots (avec aspects majeurs ~270 mots)

---

## 🔧 FORMULES D'ENRICHISSEMENT

### Section "Climat Général" (28 → 120 mots)

**Structure actuelle (28 mots) :**
```python
general_climate = f"Le climat de ce mois est marqué par {tonalité} avec la Lune en {moon_sign}."
```

**Structure cible (120 mots) :**
```
1. Tonalité de base (30 mots)
   - Description du climat émotionnel général
   - Lien avec position lunaire (signe + élément)

2. Aspect dominant influent (40 mots)
   - Mention de l'aspect majeur le plus serré (plus faible orbe)
   - Impact sur l'humeur générale du mois
   - Manifestation concrète observable

3. Ascendant lunaire (30 mots)
   - Influence de l'ascendant sur la perception
   - Filtre appliqué aux événements du mois

4. Preview axes (20 mots)
   - Transition vers sections suivantes
   - Annonce des 2-3 domaines clés
```

**Exemple enrichi (Bélier Maison 1) :**
```
Le climat de ce mois est marqué par une énergie dynamique et assertive,
portée par la Lune en Bélier (élément Feu). Cette configuration favorise
l'initiative directe et l'action spontanée, avec une pointe d'impatience
productive. L'aspect dominant Sun☌Moon (orbe 0.5°) intensifie cette fusion :
volonté et émotions fonctionnent comme un seul moteur, amplifiant l'authenticité
mais réduisant la capacité de recul. Concrètement : difficulté à séparer
"ce que je veux" et "ce que je ressens" → décisions rapides, parfois impulsives.
L'ascendant lunaire en Taureau tempère cette fougue : les réactions sont
canalisées vers des objectifs concrets, tangibles. Les domaines clés du mois
se concentrent sur l'identité personnelle (Maison 1) et les ressources
matérielles (Maison 2).
```
**→ 120 mots, 0 mots ésotériques, 1 manifestation concrète**

---

### Section "Axes Dominants" (20 → 100 mots)

**Structure actuelle (20 mots) :**
```python
dominant_axes = f"Les axes dominants sont : {', '.join(axes_list)}."
```

**Structure cible (100 mots) :**
```
Pour chaque axe (2-3 maisons dominantes) :

1. Nom de la maison + domaine (5 mots)
   - Ex: "Maison 1 (Identité et apparence)"

2. Contexte mensuel (25 mots)
   - Pourquoi cet axe est activé ce mois
   - Lien avec aspects majeurs ou position lunaire

3. Manifestation concrète (15 mots)
   - Situations observables dans ce domaine
   - Exemples pratiques

4. Liens inter-axes (10 mots par paire)
   - Comment les axes interagissent
   - Tensions ou synergies
```

**Exemple enrichi (2 axes : M1 + M2) :**
```
Maison 1 (Identité et apparence) : L'activation de cette zone par la Lune
en Bélier met l'accent sur l'affirmation de soi et la visibilité sociale.
Concrètement : besoin accru de manifester sa personnalité, impatience face
aux compromis, désir d'agir selon ses valeurs propres sans négociation.
Ce focus identitaire peut générer des frictions si l'environnement demande
de la diplomatie.

Maison 2 (Ressources et valeurs) : L'ascendant lunaire en Taureau active
ce domaine matériel, favorisant la consolidation des acquis et la recherche
de sécurité tangible. Cette zone dialogue avec la Maison 1 en créant une
tension productive : l'identité assertive (M1) doit se traduire en ressources
concrètes (M2) → action canalisée vers des objectifs mesurables.
```
**→ 100 mots, 0 mots ésotériques, 2 manifestations concrètes, 1 lien inter-axes**

---

## ✅ VALIDATION & TESTS

### Tests Automatisés (à exécuter)

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

# 1. Tests unitaires (doivent passer)
pytest tests/test_lunar_report.py -v

# 2. Script de validation format (3 configurations)
python scripts/test_lunar_report_format.py

# 3. Vérifier longueur mots
# Doit afficher pour chaque config :
#   - Climat général : 100-150 mots ✅
#   - Axes dominants : 80-120 mots ✅
#   - Total rapport : > 300 mots ✅
```

### Checklist Qualité Manuelle

Après implémentation, vérifier sur 3 configurations (Bélier M1, Taureau M2, Gémeaux M3) :

- [ ] **Longueur Climat général :** 100-150 mots (cible 120)
- [ ] **Longueur Axes dominants :** 80-120 mots (cible 100)
- [ ] **Longueur totale rapport :** > 300 mots (cible 400-600)
- [ ] **Ton senior/factuel :** ≤ 2 mots ésotériques par section
- [ ] **Manifestations concrètes :** Au moins 1 par section
- [ ] **Conseils actionnables :** Présents et spécifiques
- [ ] **Structure 4 sections :** Header, Climat, Axes, Aspects (toutes présentes)
- [ ] **Cohérence :** Liens logiques entre sections
- [ ] **Pas de régression :** Section "Aspects majeurs" toujours ~270 mots

### Critères de Succès Final

**100% conformité MVP atteinte si :**
- ✅ **3/3 configurations** > 300 mots
- ✅ **100% rapports** respectent ton senior (≤2 mots ésotériques/section)
- ✅ **100% rapports** contiennent manifestations concrètes
- ✅ **Tests pytest** : 8/8 passent
- ✅ **Script validation** : 3/3 configs validées

---

## 📋 PLAN D'EXÉCUTION RECOMMANDÉ

### Phase 1 : Analyse (30 min)

1. Lire fichiers de référence :
   - `COPY_IMPROVEMENTS_ROADMAP.md` (plan technique détaillé)
   - `COPY_EXAMPLES_REFERENCE.md` (exemples validés)
   - `aspect_explanation_service.py` (code actuel)

2. Localiser fonctions à modifier :
   - Fonction `build_lunar_report_v4()` (ligne ~XXX)
   - Template `general_climate` (ligne ~XXX)
   - Template `dominant_axes` (ligne ~XXX)

### Phase 2 : Implémentation Climat Général (2-3h)

1. Créer fonction helper `_generate_general_climate_enriched()`
   - Paramètres : `moon_sign`, `moon_element`, `lunar_ascendant`, `aspects` (liste triée par orbe)
   - Retour : `str` (120 mots)

2. Implémenter formule 4 parties :
   - Tonalité base (30 mots) : Lune en signe + élément
   - Aspect dominant (40 mots) : Aspect le plus serré + manifestation
   - Ascendant lunaire (30 mots) : Filtre perceptif
   - Preview axes (20 mots) : Transition

3. Tester avec 3 configurations :
   - Bélier M1 (action) : Vérifier tonalité dynamique
   - Taureau M2 (stabilité) : Vérifier tonalité posée
   - Gémeaux M3 (communication) : Vérifier tonalité fluide

### Phase 3 : Implémentation Axes Dominants (2-3h)

1. Créer fonction helper `_generate_dominant_axes_enriched()`
   - Paramètres : `dominant_houses` (liste 2-3 maisons), `moon_sign`, `lunar_ascendant`, `aspects`
   - Retour : `str` (100 mots)

2. Implémenter formule par axe :
   - Nom maison + domaine (5 mots)
   - Contexte mensuel (25 mots) : Pourquoi activée
   - Manifestation concrète (15 mots) : Situations observables
   - Liens inter-axes (10 mots/paire) : Interactions

3. Gérer cas 2 vs 3 axes :
   - Si 2 axes : 50 mots/axe
   - Si 3 axes : 33 mots/axe

### Phase 4 : Validation (1-2h)

1. Exécuter tests automatisés :
   ```bash
   pytest tests/test_lunar_report.py -v
   python scripts/test_lunar_report_format.py
   ```

2. Analyser longueurs :
   - Climat général : 100-150 mots ? ✅/❌
   - Axes dominants : 80-120 mots ? ✅/❌
   - Total rapport : > 300 mots ? ✅/❌

3. Audit qualité manuelle :
   - Compter mots ésotériques (cible ≤2/section)
   - Vérifier manifestations concrètes présentes
   - Vérifier conseils actionnables

4. Ajustements si nécessaire :
   - Si trop long (>150 mots Climat) : Réduire preview axes
   - Si trop court (<100 mots Climat) : Enrichir aspect dominant
   - Si ton ésotérique : Remplacer vocabulaire

---

## 🎯 LIVRABLES ATTENDUS

### Code
1. **Fichier modifié :** `apps/api/services/aspect_explanation_service.py`
   - Fonction `_generate_general_climate_enriched()` (nouvelle)
   - Fonction `_generate_dominant_axes_enriched()` (nouvelle)
   - Fonction `build_lunar_report_v4()` (modifiée pour appeler helpers)

### Validation
2. **Tests passent :** `pytest tests/test_lunar_report.py -v` → 8/8 ✅
3. **Script validation :** `python scripts/test_lunar_report_format.py` → 3/3 configs ✅
4. **Rapport exemple :** JSON rapport Taureau M2 > 300 mots (actuellement 282)

### Documentation
5. **Changelog :** Résumé des modifications (formules, longueurs avant/après)
6. **Exemples :** 3 rapports générés (Bélier, Taureau, Gémeaux) avec longueurs validées

---

## 📚 RÉFÉRENCES COMPLÉMENTAIRES

### Vocabulaire Senior Recommandé

**Ton professionnel (✅ à utiliser) :**
- Dynamique, levier, friction, fusion, catalyseur, moteur
- Tension productive, synergie, polarité, axe structurant
- Manifestation, observable, actionnable, mesurable
- Filtre perceptif, prisme, contexte, cadre de référence

**Ton ésotérique (❌ à éviter) :**
- Énergie cosmique, vibrations, karma, destin, univers
- Chemin de vie, mission d'âme, leçon karmique
- Bénédiction, malédiction, fatalité, prédestination

### Exemples de Manifestations Concrètes

**Bonne manifestation (spécifique, observable) :**
- "Difficulté à séparer 'ce que je veux' et 'ce que je ressens' → décisions rapides, parfois impulsives"
- "Besoin accru de manifester sa personnalité, impatience face aux compromis"
- "Action canalisée vers des objectifs mesurables (budget, projet concret)"

**Mauvaise manifestation (vague, ésotérique) :**
- "Vous ressentirez une énergie spéciale ce mois" ❌
- "L'univers vous envoie des signes" ❌
- "Votre vibration sera élevée" ❌

---

## ⚠️ CONTRAINTES CRITIQUES

1. **NE PAS modifier la section "Aspects majeurs"** (déjà conforme, ~270 mots)
2. **NE PAS casser les tests existants** (8 tests doivent passer)
3. **NE PAS introduire de vocabulaire ésotérique** (respecter ton senior actuel)
4. **NE PAS dépasser 600 mots total** (risque de verbosité)
5. **GARDER la structure JSON 4 sections** (header, climate, axes, aspects)

---

## 🚀 COMMANDES RAPIDES

```bash
# Naviguer vers API
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

# Éditer fichier principal
# nano services/aspect_explanation_service.py

# Exécuter tests unitaires
pytest tests/test_lunar_report.py -v

# Exécuter script validation
python scripts/test_lunar_report_format.py

# Vérifier longueurs (après implémentation)
python scripts/test_lunar_report_format.py | grep "mots"
# Doit afficher pour chaque config :
#   Climat général: 100-150 mots ✅
#   Axes dominants: 80-120 mots ✅
#   Total: > 300 mots ✅
```

---

## 📞 BESOIN D'AIDE ?

**Fichiers à consulter en priorité :**
1. `COPY_IMPROVEMENTS_ROADMAP.md` → Plan technique complet (27 KB)
2. `COPY_EXAMPLES_REFERENCE.md` → Exemples de copy validés (13 KB)
3. `LUNAR_COPY_AUDIT.md` → Audit détaillé avec métriques (19 KB)

**En cas de doute sur le ton :**
- Relire exemples validés dans `COPY_EXAMPLES_REFERENCE.md`
- Vérifier vocabulaire recommandé vs interdit (ci-dessus)
- Compter mots ésotériques (cible ≤2 par section)

---

**Temps estimé total :** 6-8h
**Priorité :** 🔴 CRITIQUE (bloquant MVP)
**Effort restant MVP après tâche :** 0h (100% conformité atteinte)
