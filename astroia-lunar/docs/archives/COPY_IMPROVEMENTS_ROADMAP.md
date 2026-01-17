# Roadmap Améliorations Copy - Rapports Lunaires
**Date:** 2026-01-17
**Basé sur:** Audit qualité copy (tâche 2.3)

## 🎯 Objectif

Passer de **66% conformité MVP** → **100% conformité MVP**

**Problème identifié:** 1/3 des rapports < 300 mots (seuil minimum)
**Cause:** Sections "Climat général" et "Axes dominants" trop courtes

---

## 📊 État Actuel vs. Cible

| Section | Actuel | Cible MVP | Écart | Priorité |
|---------|--------|-----------|-------|----------|
| Climat général | 28 mots | 100-300 mots | -72 mots | 🔴 P1 |
| Axes dominants | 20 mots | 100-300 mots | -80 mots | 🔴 P1 |
| Aspects majeurs | 270 mots | 100-200 mots | +70 mots | ✅ OK |
| **TOTAL** | 318 mots | 300-800 mots | +18 mots | 🟡 Limite |

**Note:** 1 rapport sur 3 tombe à 282 mots (cas avec seulement 2 aspects majeurs)

---

## 🔧 Implémentation - Priorité 1: Climat Général

### Objectif
Passer de **28 mots** → **100-120 mots**

### Fichier Cible
`/Users/remibeaurain/astroia/astroia-lunar/apps/api/services/lunar_report_builder.py`

### Fonction Actuelle
```python
def _generate_general_climate(lunar_return: LunarReturn) -> str:
    """Génère description climat général du mois"""
    sign = lunar_return.moon_sign
    house = lunar_return.moon_house
    asc = lunar_return.lunar_ascendant

    # Template actuel (28 mots)
    return f"Mois d'impulsion identitaire forte. Besoin d'affirmer ton individualité, " \
           f"d'initier des projets personnels. Attention à l'impatience et à l'impulsivité. " \
           f"Ascendant {asc} : coloration du filtre perceptif ce mois-ci."
```

### Proposition Nouvelle Structure

```python
def _generate_general_climate(lunar_return: LunarReturn) -> str:
    """Génère description climat général du mois (cible: 100-120 mots)"""

    # 1. Tonalité de base (signe + maison) - 30 mots
    base_tone = _get_sign_house_tone(lunar_return.moon_sign, lunar_return.moon_house)

    # 2. Aspect dominant du mois - 40 mots
    main_aspect = _get_main_aspect_preview(lunar_return.aspects)

    # 3. Rôle ascendant lunaire - 30 mots
    asc_influence = _get_ascendant_influence(lunar_return.lunar_ascendant)

    # 4. Mini-preview dynamiques - 20 mots
    dynamics_preview = _get_dynamics_preview(lunar_return.aspects)

    return f"{base_tone}\n\n{main_aspect} {asc_influence} {dynamics_preview}"
```

### Helpers à Créer

#### 1. `_get_sign_house_tone()` - 30 mots

**Cartographie signe + maison → tonalité:**

```python
SIGN_HOUSE_TONES = {
    ('Aries', 1): "Mois d'impulsion identitaire forte. Besoin d'affirmer ton individualité, "
                  "d'initier des projets personnels. Attention à l'impatience et à l'impulsivité.",

    ('Taurus', 2): "Consolidation matérielle : gestion des finances, acquisition de biens, "
                   "sécurisation des ressources. Pragmatisme et patience au service de la stabilité.",

    ('Gemini', 3): "Communication intense et multidirectionnelle. Besoin d'échanger, d'apprendre, "
                   "de bouger dans ton environnement. Mental hyperactif, attention à la saturation.",

    ('Cancer', 4): "Retour aux bases émotionnelles. Besoin de sécurité affective, de prendre soin "
                   "de ton foyer. Sensibilité accrue, vigilance sur les replis défensifs.",

    ('Leo', 5): "Expression créative au premier plan. Besoin de briller, de créer, de jouer. "
                "Énergie vitale puissante, attention aux excès d'ego.",

    ('Virgo', 6): "Organisation du quotidien et amélioration des routines. Besoin d'efficacité, "
                  "de service utile. Perfectionnisme possible, éviter l'hypercritique.",

    ('Libra', 7): "Relations et partenariats structurent le mois. Besoin d'équilibre, de diplomatie, "
                  "de cocréation. Indécision possible, chercher le compromis sans se perdre.",

    ('Scorpio', 8): "Transformation profonde en cours. Besoin d'explorer l'intensité, les zones "
                    "cachées. Puissance émotionnelle, vigilance sur le contrôle excessif.",

    ('Sagittarius', 9): "Expansion et quête de sens. Besoin d'explorer, d'apprendre, de donner "
                        "du relief à ton existence. Optimisme moteur, attention à la dispersion.",

    ('Capricorn', 10): "Structuration de tes ambitions. Besoin d'accomplissement, de bâtir du "
                       "durable. Responsabilité et discipline au service de tes objectifs.",

    ('Aquarius', 11): "Innovation et dimension collective. Besoin de contribuer, de te démarquer, "
                      "de t'affranchir. Originalité créatrice, éviter le détachement froid.",

    ('Pisces', 12): "Dissolution des frontières et connexion subtile. Besoin de rêver, de t'abandonner, "
                    "de fusionner. Sensibilité extrême, vigilance sur la confusion ou la fuite."
}

def _get_sign_house_tone(sign: str, house: int) -> str:
    """Retourne tonalité de base selon signe lunaire et maison"""
    key = (sign, house)

    if key in SIGN_HOUSE_TONES:
        return SIGN_HOUSE_TONES[key]

    # Fallback: combiner info générique signe + maison
    sign_quality = SIGN_QUALITIES.get(sign, "qualité non définie")
    house_theme = HOUSE_THEMES.get(house, "thème non défini")

    return f"Mois marqué par {sign_quality}. Focus sur {house_theme}."
```

#### 2. `_get_main_aspect_preview()` - 40 mots

**Identifie l'aspect le plus serré (orbe minimum) et donne mini-preview:**

```python
def _get_main_aspect_preview(aspects: list) -> str:
    """Identifie aspect principal et donne preview (40 mots)"""

    if not aspects:
        return "Mois fluide sans aspects majeurs dominants."

    # Trier par orbe (aspect le plus serré = le plus puissant)
    main_aspect = min(aspects, key=lambda a: a['orb'])

    planet1 = main_aspect['planet1']
    planet2 = main_aspect['planet2']
    aspect_type = main_aspect['type']
    orb = main_aspect['orb']

    # Templates par type d'aspect
    ASPECT_PREVIEWS = {
        'conjunction': f"Ce mois lunaire se caractérise par une fusion {planet1}-{planet2} "
                      f"(orbe {orb}°). Ton rapport à {get_planet_function(planet1)} et "
                      f"{get_planet_function(planet2)} fusionne, créant une période où ces "
                      f"deux dimensions ne font qu'une.",

        'opposition': f"Dynamique principale du mois : tension {planet1}-{planet2} "
                     f"(opposition, orbe {orb}°). Deux pôles en face-à-face "
                     f"({get_planet_function(planet1)} vs. {get_planet_function(planet2)}), "
                     f"cherchant l'équilibre sans se perdre dans l'un ou l'autre extrême.",

        'square': f"Le mois s'articule autour d'une friction {planet1}-{planet2} "
                 f"(carré, orbe {orb}°). Tension dynamique entre {get_planet_function(planet1)} "
                 f"et {get_planet_function(planet2)}, moteur de changement et d'ajustements.",

        'trine': f"Mois soutenu par une harmonie {planet1}-{planet2} (trigone, orbe {orb}°). "
                f"Fluidité naturelle entre {get_planet_function(planet1)} et "
                f"{get_planet_function(planet2)}, ressource mobilisable sans effort.",

        'sextile': f"Le mois bénéficie d'une synergie {planet1}-{planet2} (sextile, orbe {orb}°). "
                  f"Opportunité de lier {get_planet_function(planet1)} et "
                  f"{get_planet_function(planet2)} de manière constructive."
    }

    return ASPECT_PREVIEWS.get(aspect_type, f"Aspect {planet1}-{planet2} structure le mois.")

# Helper: fonctions planétaires courtes
PLANET_FUNCTIONS = {
    'Sun': 'volonté consciente',
    'Moon': 'besoins émotionnels',
    'Mercury': 'intellect et communication',
    'Venus': 'relations et valeurs',
    'Mars': 'action et désir',
    'Jupiter': 'expansion et sens',
    'Saturn': 'structure et limites',
    'Uranus': 'innovation et rupture',
    'Neptune': 'fusion et inspiration',
    'Pluto': 'transformation profonde'
}

def get_planet_function(planet: str) -> str:
    return PLANET_FUNCTIONS.get(planet, planet.lower())
```

#### 3. `_get_ascendant_influence()` - 30 mots

**Décrit influence ascendant lunaire sur perception du mois:**

```python
ASCENDANT_INFLUENCES = {
    'Aries': "Ascendant lunaire Bélier colore ce mois d'une impatience motrice : "
             "besoin d'agir vite, de trancher, d'initier. Cette dimension impulsive "
             "peut accélérer ton élan ou créer de la précipitation.",

    'Taurus': "Ascendant lunaire Taureau ancre ce mois dans la matière : besoin de "
              "tangibilité, de lenteur productive, de plaisir sensoriel. Cette dimension "
              "stabilisatrice peut tempérer l'agitation ou ralentir le mouvement.",

    'Gemini': "Ascendant lunaire Gémeaux colore ce mois d'une curiosité intellectuelle : "
              "besoin de comprendre, verbaliser, multiplier les perspectives. Cette dimension "
              "analytique peut éclairer tes choix ou surinvestir le mental.",

    'Cancer': "Ascendant lunaire Cancer amplifie la dimension émotionnelle : besoin de "
              "sécurité affective, de protection, de prendre soin. Cette sensibilité accrue "
              "peut nourrir l'empathie ou favoriser les replis défensifs.",

    'Leo': "Ascendant lunaire Lion insuffle une dimension créative et généreuse : besoin "
           "de rayonner, d'exprimer ta singularité, de créer. Cette énergie solaire peut "
           "magnifier ton expression ou tomber dans l'excès d'ego.",

    'Virgo': "Ascendant lunaire Vierge apporte une dimension analytique et pratique : besoin "
             "d'ordre, de précision, de service utile. Cette exigence peut structurer ton "
             "quotidien ou déraper vers l'hypercritique.",

    'Libra': "Ascendant lunaire Balance oriente ce mois vers l'équilibre relationnel : besoin "
             "de diplomatie, d'harmonie, de cocréation. Cette dimension partenariale peut "
             "faciliter les compromis ou générer de l'indécision.",

    'Scorpio': "Ascendant lunaire Scorpion intensifie la profondeur émotionnelle : besoin "
               "d'explorer les zones cachées, de transformer en profondeur. Cette puissance "
               "peut catalyser des mutations ou basculer dans le contrôle excessif.",

    'Sagittarius': "Ascendant lunaire Sagittaire dilate ce mois vers l'expansion : besoin "
                   "de sens, d'exploration, d'optimisme conquérant. Cette dimension philosophique "
                   "peut donner du relief à ton existence ou disperser ton énergie.",

    'Capricorn': "Ascendant lunaire Capricorne structure ce mois avec pragmatisme : besoin "
                 "d'accomplissement durable, de responsabilité assumée. Cette dimension "
                 "saturnienne peut ancrer tes ambitions ou rigidifier tes approches.",

    'Aquarius': "Ascendant lunaire Verseau insuffle une dimension innovante et collective : "
                "besoin de te démarquer, de contribuer au groupe, de t'affranchir. Cette "
                "originalité peut libérer ta créativité ou te couper de l'émotion.",

    'Pisces': "Ascendant lunaire Poissons dissout les frontières ce mois-ci : besoin de "
              "fusion, de rêve, de connexion subtile. Cette sensibilité extrême peut ouvrir "
              "l'intuition ou favoriser confusion et fuite."
}

def _get_ascendant_influence(lunar_ascendant: str) -> str:
    """Retourne description influence ascendant lunaire"""
    return ASCENDANT_INFLUENCES.get(lunar_ascendant, f"Ascendant {lunar_ascendant} colore le mois.")
```

#### 4. `_get_dynamics_preview()` - 20 mots

**Mini-liste des dynamiques clés (3-4 aspects principaux):**

```python
def _get_dynamics_preview(aspects: list) -> str:
    """Liste les 2-3 dynamiques principales (20 mots)"""

    if not aspects or len(aspects) == 0:
        return ""

    # Prendre les 3 aspects les plus serrés
    top_aspects = sorted(aspects, key=lambda a: a['orb'])[:3]

    dynamics = []
    for asp in top_aspects:
        p1 = asp['planet1']
        p2 = asp['planet2']
        atype = asp['type']

        # Labels courts par type
        TYPE_LABELS = {
            'conjunction': 'fusion',
            'opposition': 'tension polarisée',
            'square': 'friction',
            'trine': 'facilité',
            'sextile': 'opportunité'
        }

        label = TYPE_LABELS.get(atype, atype)
        dynamics.append(f"{p1}-{p2} ({label})")

    preview = ', '.join(dynamics)
    return f"Dynamiques clés : {preview}."
```

### Exemple Output Final (120 mots)

**Configuration:** Lune Bélier Maison 1, Ascendant Gémeaux

```
Mois d'impulsion identitaire forte. Besoin d'affirmer ton individualité,
d'initier des projets personnels. Attention à l'impatience et à l'impulsivité.

Ce mois lunaire se caractérise par une fusion Lune-Mars (orbe 2.3°).
Ton rapport à besoins émotionnels et action fusionne, créant une période
où ces deux dimensions ne font qu'une. Favorable aux lancements, aux prises
de position claires, aux affirmations franches. Risque : confusion entre
réactivité et décision réfléchie.

Ascendant lunaire Gémeaux colore ce mois d'une curiosité intellectuelle :
besoin de comprendre, verbaliser, multiplier les perspectives. Cette dimension
analytique peut éclairer tes choix ou surinvestir le mental.

Dynamiques clés : Moon-Mars (fusion), Moon-Sun (friction), Venus-Jupiter (facilité).
```

**Comptage:** ~120 mots ✅

---

## 🔧 Implémentation - Priorité 2: Axes Dominants

### Objectif
Passer de **20 mots** → **80-100 mots**

### Fichier Cible
`/Users/remibeaurain/astroia/astroia-lunar/apps/api/services/lunar_report_builder.py`

### Fonction Actuelle

```python
def _identify_dominant_axes(lunar_return: LunarReturn) -> list:
    """Identifie 2-3 axes dominants du mois"""

    axes = []

    # Axe 1: Maison de la Lune
    house = lunar_return.moon_house
    house_theme = HOUSE_THEMES.get(house, "thème non défini")
    axes.append(f"Maison {house} : {house_theme}")

    # Axe 2: Générique
    axes.append("Période centrée sur l'intégration du cycle lunaire en cours")

    return axes
```

**Problème:** Descriptions trop sèches, pas de contexte ni de liens inter-axes.

### Proposition Nouvelle Structure

```python
def _identify_dominant_axes(lunar_return: LunarReturn) -> list:
    """Identifie et décrit 2-3 axes dominants (cible: 80-100 mots)"""

    axes = []

    # Axe 1: Maison de la Lune (focus principal)
    moon_axis = _describe_moon_house_axis(lunar_return)
    axes.append(moon_axis)

    # Axes 2-3: Maisons impliquées par aspects majeurs
    aspect_axes = _describe_aspect_houses(lunar_return)
    axes.extend(aspect_axes[:2])  # Maximum 2 axes supplémentaires

    return axes
```

### Helpers à Créer

#### 1. `_describe_moon_house_axis()` - 40 mots

**Décrit la maison lunaire avec contexte:**

```python
MOON_HOUSE_DESCRIPTIONS = {
    1: "Maison 1 (Identité, apparence) : Ce mois met l'accent sur ton image, "
       "ta manière de t'affirmer dans le monde, tes initiatives personnelles. "
       "Besoin de revoir comment tu te présentes, ce que tu incarnes. Favorable "
       "aux nouveaux départs, aux prises de position identitaires claires.",

    2: "Maison 2 (Ressources, valeurs) : Ce mois met l'accent sur ta sécurité "
       "matérielle, tes finances, ce qui a de la valeur pour toi. Questions "
       "d'argent, d'acquisitions, ou de redéfinition de tes priorités concrètes. "
       "Favorable à la consolidation, à la clarification de tes besoins tangibles.",

    3: "Maison 3 (Communication, environnement proche) : Ce mois met l'accent "
       "sur tes échanges quotidiens, tes apprentissages, tes déplacements courts. "
       "Mental hyperactif, besoin de bouger, de parler, de comprendre. Favorable "
       "aux formations, aux dialogues, à la curiosité intellectuelle.",

    4: "Maison 4 (Foyer, racines) : Ce mois met l'accent sur ton intérieur, "
       "ta famille, ton lieu de vie. Besoin de sécurité affective, de prendre "
       "soin de ton nid. Questions d'ancrage, de mémoire familiale, de bases "
       "émotionnelles. Favorable au cocooning, aux introspections.",

    5: "Maison 5 (Créativité, plaisir) : Ce mois met l'accent sur ton expression "
       "personnelle, tes créations, tes plaisirs. Besoin de jouer, de briller, "
       "de laisser une empreinte unique. Favorable aux projets artistiques, aux "
       "jeux, aux romances, à l'affirmation de ta singularité.",

    6: "Maison 6 (Quotidien, service) : Ce mois met l'accent sur tes routines, "
       "ta santé, ton travail quotidien. Besoin d'efficacité, d'amélioration "
       "des process, de service utile. Favorable à l'organisation, aux soins "
       "corporels, à l'optimisation de ton quotidien.",

    7: "Maison 7 (Relations, partenariats) : Ce mois met l'accent sur tes "
       "partenariats, tes collaborations, tes relations en miroir. Besoin de "
       "cocréation, de compromis, d'équilibre relationnel. Favorable aux "
       "négociations, aux contrats, aux ajustements interpersonnels.",

    8: "Maison 8 (Transformation, intimité) : Ce mois met l'accent sur les "
       "zones cachées, l'intensité émotionnelle, les ressources partagées. "
       "Besoin d'explorer en profondeur, de transformer, de fusionner. Favorable "
       "aux mutations internes, aux intimités, aux deuils et renaissances.",

    9: "Maison 9 (Philosophie, expansion) : Ce mois met l'accent sur le sens, "
       "les voyages lointains, l'apprentissage supérieur. Besoin d'élargir tes "
       "horizons, de comprendre le sens de ton existence. Favorable aux études, "
       "aux explorations, à la quête de perspectives nouvelles.",

    10: "Maison 10 (Carrière, accomplissement) : Ce mois met l'accent sur ton "
        "ambition, ta visibilité sociale, ton accomplissement professionnel. "
        "Besoin de structurer tes objectifs, de bâtir du durable. Favorable aux "
        "étapes de carrière, aux prises de responsabilité, à l'affirmation publique.",

    11: "Maison 11 (Collectif, idéaux) : Ce mois met l'accent sur tes projets "
        "collectifs, tes amitiés, tes engagements communautaires. Besoin de "
        "contribuer au groupe, de te démarquer dans un collectif. Favorable aux "
        "innovations sociales, aux réseaux, aux causes partagées.",

    12: "Maison 12 (Spiritualité, inconscient) : Ce mois met l'accent sur ta "
        "vie intérieure, tes rêves, ton inconscient. Besoin de solitude, de "
        "fusion subtile, de connexion spirituelle. Favorable aux introspections "
        "profondes, aux pratiques contemplatives, aux lâcher-prise."
}

def _describe_moon_house_axis(lunar_return: LunarReturn) -> str:
    """Décrit axe maison lunaire (40 mots)"""
    house = lunar_return.moon_house
    return MOON_HOUSE_DESCRIPTIONS.get(house, f"Maison {house} : thème non défini")
```

#### 2. `_describe_aspect_houses()` - 20-30 mots chacun

**Identifie maisons impliquées dans aspects majeurs et crée liens:**

```python
def _describe_aspect_houses(lunar_return: LunarReturn) -> list:
    """Identifie 1-2 axes secondaires via aspects (20-30 mots chacun)"""

    axes = []

    if not lunar_return.aspects:
        return axes

    # Collecter toutes les maisons impliquées (hors maison lunaire)
    houses_involved = set()
    moon_house = lunar_return.moon_house

    for aspect in lunar_return.aspects:
        p1_house = aspect.get('placements', {}).get('planet1', {}).get('house')
        p2_house = aspect.get('placements', {}).get('planet2', {}).get('house')

        if p1_house and p1_house != moon_house:
            houses_involved.add(p1_house)
        if p2_house and p2_house != moon_house:
            houses_involved.add(p2_house)

    # Prendre les 2 maisons les plus fréquentes
    # (ici simplification: prendre les 2 premières)
    houses_list = sorted(houses_involved)[:2]

    for house in houses_list:
        theme = HOUSE_THEMES.get(house, "thème non défini")
        # Créer lien avec maison lunaire
        link = _create_house_link(moon_house, house)
        axes.append(f"Maison {house} ({theme}) : {link}")

    return axes

def _create_house_link(moon_house: int, other_house: int) -> str:
    """Crée lien narratif entre maison lunaire et autre maison"""

    # Exemples de liens pré-écrits pour combos fréquentes
    HOUSE_LINKS = {
        (1, 7): "Ton identité personnelle (M1) dialogue avec tes relations (M7). "
                "Mois où affirmation de soi et compromis relationnel se négocient.",

        (1, 10): "Ton image personnelle (M1) rencontre ton accomplissement public (M10). "
                 "Ce que tu es et ce que tu montres professionnellement s'articulent.",

        (2, 8): "Tes ressources personnelles (M2) croisent les ressources partagées (M8). "
                "Questions d'argent propre vs. argent commun, valeurs vs. transformation.",

        (2, 10): "Ta sécurité matérielle (M2) dialogue avec ton ambition (M10). "
                 "Tes choix financiers peuvent impacter ton parcours professionnel.",

        (3, 9): "Ton environnement proche (M3) rencontre tes horizons lointains (M9). "
                "Communication locale vs. exploration distante, mental concret vs. abstrait.",

        (4, 10): "Ton foyer (M4) et ta carrière (M10) se confrontent. Mois où vie "
                 "privée et ambition publique cherchent leur équilibre.",

        (5, 11): "Ta créativité personnelle (M5) rencontre le collectif (M11). "
                 "Expression singulière vs. contribution au groupe.",

        # Fallback générique
        'default': f"Cette maison dialogue avec Maison {moon_house} ce mois-ci."
    }

    key = tuple(sorted([moon_house, other_house]))
    return HOUSE_LINKS.get(key, HOUSE_LINKS['default'])
```

### Exemple Output Final (100 mots)

**Configuration:** Lune Taureau M2, aspects M10 + M11

```
1. Maison 2 (Ressources, valeurs) : Ce mois met l'accent sur ta sécurité
   matérielle, tes finances, ce qui a de la valeur pour toi. Questions
   d'argent, d'acquisitions, ou de redéfinition de tes priorités concrètes.
   Favorable à la consolidation, à la clarification de tes besoins tangibles.

2. Maison 10 (Carrière, visibilité) : Ta sécurité matérielle (M2) dialogue
   avec ton ambition (M10). Tes choix financiers peuvent impacter ton
   parcours professionnel.

3. Maison 11 (Collectif, idéaux) : Tes ambitions professionnelles (M10)
   rencontrent tes engagements communautaires (M11). Mois où carrière et
   contribution sociale peuvent se renforcer mutuellement.
```

**Comptage:** ~100 mots ✅

---

## 📋 Plan d'Implémentation Technique

### Phase 1: Climat Général (3-4h)

**Tâches:**
1. Créer dictionnaires de données
   - [ ] `SIGN_HOUSE_TONES` (12 signes × 12 maisons = 144 combos)
   - [ ] `ASPECT_PREVIEWS` (5 types × templates)
   - [ ] `ASCENDANT_INFLUENCES` (12 signes)
   - [ ] `PLANET_FUNCTIONS` (10 planètes)

2. Créer fonctions helpers
   - [ ] `_get_sign_house_tone()`
   - [ ] `_get_main_aspect_preview()`
   - [ ] `_get_ascendant_influence()`
   - [ ] `_get_dynamics_preview()`

3. Refactorer `_generate_general_climate()`
   - [ ] Intégrer appels helpers
   - [ ] Valider format output (100-120 mots)

4. Tester
   - [ ] 3 configs existantes (Bélier M1, Taureau M2, Gémeaux M3)
   - [ ] 5 configs additionnelles (mix signes/maisons)

**Estimation:** 3-4h (1h data, 2h code, 1h tests)

---

### Phase 2: Axes Dominants (2-3h)

**Tâches:**
1. Créer dictionnaires de données
   - [ ] `MOON_HOUSE_DESCRIPTIONS` (12 maisons × 40 mots)
   - [ ] `HOUSE_LINKS` (combos fréquentes M1-M12)

2. Créer fonctions helpers
   - [ ] `_describe_moon_house_axis()`
   - [ ] `_describe_aspect_houses()`
   - [ ] `_create_house_link()`

3. Refactorer `_identify_dominant_axes()`
   - [ ] Intégrer appels helpers
   - [ ] Valider format output (80-100 mots)

4. Tester
   - [ ] 3 configs existantes
   - [ ] Cas edge: 0 aspects, 1 aspect, 5 aspects

**Estimation:** 2-3h (1h data, 1h code, 1h tests)

---

### Phase 3: Validation Globale (1h)

**Tâches:**
1. Exécuter script audit complet
   - [ ] `python apps/api/scripts/test_lunar_report_format.py`

2. Vérifier métriques MVP
   - [ ] Longueur totale: 300-800 mots (100% configs)
   - [ ] Mots ésotériques: ≤ 2/section
   - [ ] Sections: 4/4 présentes
   - [ ] Contenu actionnable: OK

3. Valider cohérence narrative
   - [ ] Climat général → Axes dominants (flow logique)
   - [ ] Axes dominants → Aspects majeurs (pas de répétitions)

**Estimation:** 1h

---

## 🎯 Critères de Succès

### Avant Implémentation
```
Bélier M1:    394 mots ✅
Taureau M2:   282 mots ⚠️ (sous minimum)
Gémeaux M3:   400 mots ✅

Conformité: 66% (2/3)
```

### Après Implémentation
```
Bélier M1:    520 mots ✅ (climat +92, axes +60)
Taureau M2:   420 mots ✅ (climat +92, axes +80)
Gémeaux M3:   540 mots ✅ (climat +92, axes +80)

Conformité: 100% (3/3)
```

**Bonus:** Amélioration qualitative (narratif plus riche, liens explicites)

---

## 🚀 Mise en Production

### Checklist Pré-Déploiement
- [ ] Tests unitaires passent (pytest)
- [ ] Script audit confirme 100% conformité
- [ ] Revue code (qualité copy, pas de régression)
- [ ] Validation échantillon utilisateur (3-5 personnes)

### Rollback Plan
Si régression détectée:
1. Garder backup ancien `_generate_general_climate()`
2. Feature flag pour bascule ancienne/nouvelle version
3. Rollback instantané si feedback négatif

---

## 📝 Notes Importantes

### Complexité Data
**Phase 1 nécessite:**
- 144 combos signe×maison (optimisation: 12 signes + 12 maisons = 24 templates combinables)
- 5 types aspects × templates
- 12 ascendants

**Total:** ~50 templates textuels

**Optimisation:** Utiliser templates génériques + variables

### Ton Copy
**Maintenir strictement:**
- ✅ Vocabulaire factuel (0 mot ésotérique ajouté)
- ✅ Formulations actionnables ("besoin de", "favorable à")
- ✅ Nuances (avantages + risques)
- ✅ Non prédictif ("ce mois met l'accent sur" vs. "vous allez")

### Performance
**Impact attendu:**
- Temps génération rapport: +20ms (négligeable)
- Taille payload JSON: +150 octets (négligeable)

---

## 🔗 Fichiers Impactés

### Modifiés
- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/services/lunar_report_builder.py`

### Nouveaux (optionnel)
- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/data/copy_templates.py` (dictionnaires)

### Tests
- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/scripts/test_lunar_report_format.py` (déjà existant)
- `/Users/remibeaurain/astroia/astroia-lunar/apps/api/tests/test_lunar_report_builder.py` (à créer si absent)

---

## ✅ Conclusion

**Effort total estimé:** 6-8h développement + tests
**Impact:** Passage 66% → 100% conformité MVP
**Risque:** Faible (additive, pas de modification structure existante)
**Valeur:** Critique pour lancement MVP (qualité copy = différenciation produit)
