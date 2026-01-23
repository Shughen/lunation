#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects sextile (part 1/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

SEXTILE_PART1 = {
    ('jupiter', 'mars'): """# \u26b9 Sextile Jupiter - Mars
**En une phrase :** Une opportunite d'allier vision et action qui recompense l'initiative.

## L'energie de cet aspect
Le sextile Jupiter-Mars offre une opportunite d'expansion par l'action. Cette configuration facilite l'initiative et l'entreprise quand tu saisis les occasions.

## Ton potentiel
Tu peux accomplir beaucoup en combinant enthousiasme et effort cible.

## Ton defi
Les opportunites passent si tu ne les saisis pas. Le sextile demande de l'action.

## Conseil pratique
Identifie les opportunites et agis. Le sextile ne donne rien sans effort.""",

    ('jupiter', 'mercury'): """# \u26b9 Sextile Jupiter - Mercure
**En une phrase :** Une opportunite d'elargir ta pensee qui recompense la curiosite intellectuelle.

## L'energie de cet aspect
Le sextile Jupiter-Mercure offre une facilite d'apprentissage et de communication. Cette configuration favorise les echanges d'idees et l'enseignement.

## Ton potentiel
Tu peux developper une pensee riche et partager tes connaissances efficacement.

## Ton defi
Le talent inutilise ne se developpe pas. Cultive activement ton intellect.

## Conseil pratique
Saisis les occasions d'apprendre et de transmettre. La connaissance grandit en circulant.""",

    ('jupiter', 'moon'): """# \u26b9 Sextile Jupiter - Lune
**En une phrase :** Une opportunite de croissance emotionnelle qui recompense l'ouverture du coeur.

## L'energie de cet aspect
Le sextile Jupiter-Lune offre une facilite pour le soutien emotionnel et la generosite. Cette configuration favorise les relations nourrissantes.

## Ton potentiel
Tu peux creer des liens enrichissants et nourrir les autres avec aisance.

## Ton defi
Sans effort conscient, cette facilite peut rester latente.

## Conseil pratique
Ouvre ton coeur aux opportunites de connexion. La generosite se developpe en la pratiquant.""",

    ('jupiter', 'neptune'): """# \u26b9 Sextile Jupiter - Neptune
**En une phrase :** Une opportunite d'inspiration spirituelle qui recompense la quete de sens.

## L'energie de cet aspect
Le sextile Jupiter-Neptune offre une facilite pour la foi et l'intuition. Cette configuration favorise les experiences spirituelles significatives.

## Ton potentiel
Tu peux developper une sagesse inspiree et une compassion active.

## Ton defi
L'inspiration sans action reste un reve. Concretise tes intuitions.

## Conseil pratique
Suis tes inspirations par des actions concretes. L'ideal se realise pas a pas.""",

    ('jupiter', 'pluto'): """# \u26b9 Sextile Jupiter - Pluton
**En une phrase :** Une opportunite de transformation positive qui recompense l'engagement dans le changement.

## L'energie de cet aspect
Le sextile Jupiter-Pluton offre une facilite pour rebondir et transformer les situations. Cette configuration favorise les renouvellements constructifs.

## Ton potentiel
Tu peux transformer les crises en opportunites de croissance significatives.

## Ton defi
Le potentiel de transformation demande d'accepter le changement.

## Conseil pratique
Engage-toi dans les transformations necessaires. Le renouvellement apporte l'expansion.""",

    ('jupiter', 'saturn'): """# \u26b9 Sextile Jupiter - Saturne
**En une phrase :** Une opportunite d'equilibrer croissance et structure qui recompense la planification.

## L'energie de cet aspect
Le sextile Jupiter-Saturne offre une facilite pour concretiser les ambitions. Cette configuration favorise les projets bien planifies.

## Ton potentiel
Tu peux accomplir des objectifs ambitieux par un effort structure.

## Ton defi
Sans plan d'action, l'equilibre naturel reste theorique.

## Conseil pratique
Planifie tes projets ambitieux. La vision a besoin de structure pour se realiser.""",

    ('jupiter', 'sun'): """# \u26b9 Sextile Jupiter - Soleil
**En une phrase :** Une opportunite d'expression confiante qui recompense l'initiative personnelle.

## L'energie de cet aspect
Le sextile Jupiter-Soleil offre une facilite pour rayonner et saisir les opportunites. Cette configuration favorise l'expansion personnelle.

## Ton potentiel
Tu peux developper ta confiance et attirer les bonnes opportunites.

## Ton defi
Les portes s'ouvrent mais tu dois les franchir activement.

## Conseil pratique
Ose te mettre en avant. La confiance se construit en agissant.""",

    ('jupiter', 'uranus'): """# \u26b9 Sextile Jupiter - Uranus
**En une phrase :** Une opportunite d'innovation qui recompense la prise de risque calculee.

## L'energie de cet aspect
Le sextile Jupiter-Uranus offre une facilite pour innover et profiter des changements. Cette configuration favorise les opportunites inattendues.

## Ton potentiel
Tu peux saisir les occasions liees a l'innovation et au changement.

## Ton defi
Les opportunites innovantes passent vite. Sois pret a reagir.

## Conseil pratique
Reste ouvert aux opportunites inhabituelles. L'inattendu peut etre ta chance.""",

    ('jupiter', 'venus'): """# \u26b9 Sextile Jupiter - Venus
**En une phrase :** Une opportunite d'harmonie et d'abondance qui recompense l'appreciation de la beaute.

## L'energie de cet aspect
Le sextile Jupiter-Venus offre une facilite pour attirer l'amour et les bonnes choses. Cette configuration favorise les relations agreables et la creativite.

## Ton potentiel
Tu peux developper des relations enrichissantes et un talent artistique.

## Ton defi
La facilite ne dispense pas de cultiver ce qui t'est donne.

## Conseil pratique
Investis dans tes relations et ta creativite. Le don se developpe par la pratique.""",

    ('mars', 'mercury'): """# \u26b9 Sextile Mars - Mercure
**En une phrase :** Une opportunite d'action reflechie qui recompense la decision rapide.

## L'energie de cet aspect
Le sextile Mars-Mercure offre une facilite pour agir sur ses idees. Cette configuration favorise la prise de decision et la communication assertive.

## Ton potentiel
Tu peux transformer efficacement tes idees en actions concretes.

## Ton defi
Les opportunites d'action demandent d'etre saisies au bon moment.

## Conseil pratique
N'hesite pas trop longtemps. L'action rapide sur les bonnes idees paie.""",

    ('mars', 'moon'): """# \u26b9 Sextile Mars - Lune
**En une phrase :** Une opportunite d'action emotionnellement alignee qui recompense l'ecoute de l'instinct.

## L'energie de cet aspect
Le sextile Mars-Lune offre une facilite pour agir selon ses intuitions. Cette configuration favorise les actions protectrices et nourrissantes.

## Ton potentiel
Tu peux agir de facon juste pour proteger et soutenir ce qui compte.

## Ton defi
Le potentiel demande de faire confiance a ton instinct et d'agir.

## Conseil pratique
Ecoute ton intuition et agis en consequence. L'instinct est un guide fiable.""",

    ('mars', 'neptune'): """# \u26b9 Sextile Mars - Neptune
**En une phrase :** Une opportunite d'action inspiree qui recompense l'engagement pour des ideaux.

## L'energie de cet aspect
Le sextile Mars-Neptune offre une facilite pour agir au service d'ideaux. Cette configuration favorise l'action creative et compassionnelle.

## Ton potentiel
Tu peux te mobiliser efficacement pour des causes qui te depassent.

## Ton defi
L'inspiration sans action reste un reve. Passe a l'acte.

## Conseil pratique
Agis sur tes inspirations. L'ideal se realise par des gestes concrets.""",

    ('mars', 'pluto'): """# \u26b9 Sextile Mars - Pluton
**En une phrase :** Une opportunite de force transformatrice qui recompense la determination.

## L'energie de cet aspect
Le sextile Mars-Pluton offre une facilite pour surmonter les obstacles. Cette configuration favorise l'endurance et la capacite de regeneration.

## Ton potentiel
Tu peux mobiliser une force considerable quand tu t'engages pleinement.

## Ton defi
Cette force demande d'etre activee consciemment dans les defis.

## Conseil pratique
Face aux obstacles, engage ta determination. Tu as plus de force que tu ne crois.""",

    ('mars', 'saturn'): """# \u26b9 Sextile Mars - Saturne
**En une phrase :** Une opportunite d'effort structure qui recompense la discipline.

## L'energie de cet aspect
Le sextile Mars-Saturne offre une facilite pour l'effort organise. Cette configuration favorise les accomplissements par le travail methodique.

## Ton potentiel
Tu peux atteindre des objectifs ambitieux par un effort soutenu et organise.

## Ton defi
Sans discipline active, le potentiel de travail reste theorique.

## Conseil pratique
Cree des routines d'effort. La discipline reguliere accomplit les grands projets.""",

    ('mars', 'sun'): """# \u26b9 Sextile Mars - Soleil
**En une phrase :** Une opportunite d'action authentique qui recompense l'initiative personnelle.

## L'energie de cet aspect
Le sextile Mars-Soleil offre une facilite pour agir en accord avec soi. Cette configuration favorise le leadership et l'affirmation saine.

## Ton potentiel
Tu peux developper une assertivite naturelle qui inspire les autres.

## Ton defi
Le potentiel d'action demande de passer a l'acte regulierement.

## Conseil pratique
Prends des initiatives qui expriment qui tu es. L'action authentique construit l'identite.""",
}

async def insert_interpretations():
    """Insere les interpretations sextile part 1 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in SEXTILE_PART1.items():
            result = await db.execute(
                select(PregeneratedNatalAspect).where(
                    PregeneratedNatalAspect.planet1 == planet1,
                    PregeneratedNatalAspect.planet2 == planet2,
                    PregeneratedNatalAspect.aspect_type == 'sextile',
                    PregeneratedNatalAspect.version == 2,
                    PregeneratedNatalAspect.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP {planet1}-{planet2} sextile")
                skipped += 1
                continue

            interp = PregeneratedNatalAspect(
                planet1=planet1,
                planet2=planet2,
                aspect_type='sextile',
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"INSERT {planet1}-{planet2} sextile ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nResultat: {inserted} inserees, {skipped} ignorees")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
