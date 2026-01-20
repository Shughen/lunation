# Prompt de démarrage - Interprétations Transits V2

## Contexte

Les interprétations **natales V2** sont terminées (2304 interprétations).
Maintenant, nous générons les interprétations de **transits V2** (2304 interprétations).

---

## Objectif

Générer **2304 interprétations de transits** en français, même structure que les natales :
- 16 sujets × 12 signes × 12 maisons = 2304

---

## Les 16 sujets de transits

| # | Sujet | Description | Priorité |
|---|-------|-------------|----------|
| 1 | `transit_sun` | Soleil en transit | 🔴 Haute |
| 2 | `transit_moon` | Lune en transit | 🔴 Haute |
| 3 | `transit_mercury` | Mercure en transit | 🔴 Haute |
| 4 | `transit_venus` | Vénus en transit | 🔴 Haute |
| 5 | `transit_mars` | Mars en transit | 🔴 Haute |
| 6 | `transit_jupiter` | Jupiter en transit | 🔴 Haute |
| 7 | `transit_saturn` | Saturne en transit | 🔴 Haute |
| 8 | `transit_uranus` | Uranus en transit | 🟠 Moyenne |
| 9 | `transit_neptune` | Neptune en transit | 🟠 Moyenne |
| 10 | `transit_pluto` | Pluton en transit | 🟠 Moyenne |
| 11 | `transit_north_node` | Noeud Nord en transit | 🟡 Basse |
| 12 | `transit_south_node` | Noeud Sud en transit | 🟡 Basse |
| 13 | `transit_chiron` | Chiron en transit | 🟡 Basse |
| 14 | `transit_lilith` | Lilith en transit | 🟡 Basse |
| 15 | `mercury_retrograde` | Mercure rétrograde | 🟠 Moyenne |
| 16 | `venus_retrograde` | Vénus rétrograde | 🟠 Moyenne |

---

## Structure d'une interprétation transit

```markdown
# �transit_symbol Transit de [Planète] en [Signe]

**En une phrase :** [Impact du transit sur cette maison]

## L'énergie du moment
[Description de l'énergie du transit dans ce signe traversant cette maison]

## Ce que tu pourrais vivre
[2-3 manifestations concrètes possibles]

## Conseils pour ce transit
- [Conseil 1]
- [Conseil 2]
- [Conseil 3]
```

---

## Table PostgreSQL

Réutiliser `pregenerated_natal_interpretations` avec :
- `subject`: `transit_sun`, `transit_moon`, etc.
- `sign`: signe du transit (aries, taurus, etc.)
- `house`: maison natale traversée (1-12)
- `version`: 2
- `lang`: fr

---

## Prompt à copier après /clear

```
Je continue le travail sur les interprétations astrologiques pour astroia-lunar.

**Contexte :**
- Interprétations natales V2 : ✅ TERMINÉES (2304/2304)
- Interprétations transits V2 : ⏳ À FAIRE (0/2304)

**Objectif :**
Générer les interprétations de transits V2 (2304 interprétations).
- 16 sujets × 12 signes × 12 maisons = 2304
- Même pattern que les natales : scripts Python d'insertion par groupe de 48

**Sujets à générer (dans l'ordre) :**
1. transit_sun (0/144)
2. transit_moon (0/144)
3. transit_mercury (0/144)
4. transit_venus (0/144)
5. transit_mars (0/144)
6. transit_jupiter (0/144)
7. transit_saturn (0/144)
8. transit_uranus (0/144)
9. transit_neptune (0/144)
10. transit_pluto (0/144)
11. transit_north_node (0/144)
12. transit_south_node (0/144)
13. transit_chiron (0/144)
14. transit_lilith (0/144)
15. mercury_retrograde (0/144)
16. venus_retrograde (0/144)

**Format d'interprétation :**
- Titre : # ☉ Transit de Soleil en Bélier (Maison X)
- Sections : "L'énergie du moment", "Ce que tu pourrais vivre", "Conseils pour ce transit"
- 600-1000 caractères par interprétation
- Français, tutoiement

**Méthode :**
1. Créer un script Python `insert_transit_[planet]_[signs].py`
2. Générer 48 interprétations par script (4 signes × 12 maisons)
3. Exécuter avec dangerouslyDisableSandbox=true
4. Continuer sans interruption jusqu'à complétion

**Commencer par transit_sun (Soleil en transit).**
Une fois terminé, continuer avec transit_moon, etc. sans s'arrêter.
```

---

## Vérification

```bash
cd apps/api && python3 -c "
import asyncio
from sqlalchemy import select, func
import sys
sys.path.insert(0, '.')
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

async def check():
    async with AsyncSessionLocal() as db:
        result = await db.execute(
            select(
                PregeneratedNatalInterpretation.subject,
                func.count(PregeneratedNatalInterpretation.id)
            ).where(
                PregeneratedNatalInterpretation.version == 2,
                PregeneratedNatalInterpretation.lang == 'fr',
                PregeneratedNatalInterpretation.subject.like('transit_%')
            ).group_by(PregeneratedNatalInterpretation.subject)
        )
        total = 0
        for subject, count in result.all():
            print(f'{subject}: {count}/144')
            total += count
        print(f'---')
        print(f'Total transits: {total}/2304')

asyncio.run(check())
"
```

---

## Progression attendue

| Phase | Sujets | Interprétations |
|-------|--------|-----------------|
| 1 | transit_sun à transit_mars | 720 |
| 2 | transit_jupiter, transit_saturn | 288 |
| 3 | transit_uranus à transit_pluto | 432 |
| 4 | transit_north_node à transit_lilith | 576 |
| 5 | mercury_retrograde, venus_retrograde | 288 |
| **TOTAL** | **16 sujets** | **2304** |
