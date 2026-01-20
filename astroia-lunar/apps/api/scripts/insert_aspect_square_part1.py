#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects carre (part 1/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

SQUARE_PART1 = {
    ('jupiter', 'mars'): """# \u25a1 Carre Jupiter - Mars
**En une phrase :** Une tension dynamique entre ambition et action qui pousse a l'exces mais aussi a l'accomplissement.

## L'energie de cet aspect
Le carre Jupiter-Mars cree une friction entre expansion et energie. Cette configuration pousse a agir grand, parfois trop. L'impatience et l'exces d'enthousiasme sont frequents.

## Ton potentiel
Tu as l'energie pour accomplir de grandes choses si tu canalises cette tension.

## Ton defi
L'exageration dans l'effort, les promesses impossibles ou l'epuisement par exces d'engagement.

## Conseil pratique
Choisis tes batailles. L'energie est limitee, meme si elle semble infinie.""",

    ('jupiter', 'mercury'): """# \u25a1 Carre Jupiter - Mercure
**En une phrase :** Une tension entre pensee large et details qui peut disperser ou enrichir l'intellect.

## L'energie de cet aspect
Le carre Jupiter-Mercure cree une friction entre synthese et analyse. Cette configuration peut mener a des jugements hatifs ou a une pensee trop dispersee.

## Ton potentiel
Tu peux developper une pensee complete qui integre vue d'ensemble et precision.

## Ton defi
L'exageration intellectuelle, les promesses non tenues ou la dispersion mentale.

## Conseil pratique
Verifie tes affirmations. La grandeur intellectuelle demande de la precision.""",

    ('jupiter', 'moon'): """# \u25a1 Carre Jupiter - Lune
**En une phrase :** Une tension entre besoins emotionnels et soif d'expansion qui peut creer de l'instabilite affective.

## L'energie de cet aspect
Le carre Jupiter-Lune cree une friction entre securite et aventure. Cette configuration peut mener a des exces emotionnels ou a une insatisfaction chronique.

## Ton potentiel
Tu peux apprendre a nourrir ta soif de croissance tout en honorant tes besoins de securite.

## Ton defi
L'exces emotionnel, l'insatisfaction ou l'oscillation entre confort et aventure.

## Conseil pratique
Cree une base secure d'ou tu peux explorer. Les deux besoins sont legitimes.""",

    ('jupiter', 'neptune'): """# \u25a1 Carre Jupiter - Neptune
**En une phrase :** Une tension entre foi et illusion qui peut mener a la confusion ou a une grande inspiration.

## L'energie de cet aspect
Le carre Jupiter-Neptune cree une friction entre croyance et imagination. Cette configuration peut amplifier les tendances idealistes au point de la deconnexion.

## Ton potentiel
Tu peux developper un discernement spirituel qui distingue les vrais ideaux des illusions.

## Ton defi
La naivete, les esperances irrealistes ou la fuite dans les reves.

## Conseil pratique
Ancre tes inspirations dans la realite. L'ideal se teste au quotidien.""",

    ('jupiter', 'pluto'): """# \u25a1 Carre Jupiter - Pluton
**En une phrase :** Une tension entre expansion et pouvoir qui peut mener a l'exces ou a une transformation majeure.

## L'energie de cet aspect
Le carre Jupiter-Pluton cree une friction entre croissance et controle. Cette configuration peut generer des ambitions demeusurees ou des conflits de pouvoir.

## Ton potentiel
Tu peux accomplir des transformations majeures si tu utilises ce pouvoir ethiquement.

## Ton defi
La megalomanie, les manipulations pour le pouvoir ou l'obsession du succes.

## Conseil pratique
Mets ton ambition au service d'une cause plus grande que toi.""",

    ('jupiter', 'saturn'): """# \u25a1 Carre Jupiter - Saturne
**En une phrase :** Une tension classique entre expansion et restriction qui demande d'equilibrer optimisme et realisme.

## L'energie de cet aspect
Le carre Jupiter-Saturne cree une friction fondamentale entre croissance et prudence. Cette configuration peut generer de la frustration ou une sagesse pratique.

## Ton potentiel
Tu peux developper une approche equilibree qui sait quand avancer et quand consolider.

## Ton defi
L'oscillation entre exces d'optimisme et pessimisme, ou la paralysie par le doute.

## Conseil pratique
Accepte le rythme d'expansion et de contraction. Les deux sont necessaires.""",

    ('jupiter', 'sun'): """# \u25a1 Carre Jupiter - Soleil
**En une phrase :** Une tension entre ego et opportunites qui peut mener a l'arrogance ou a une grande confiance.

## L'energie de cet aspect
Le carre Jupiter-Soleil cree une friction entre identite et expansion. Cette configuration peut gonfler l'ego ou creer une insatisfaction chronique.

## Ton potentiel
Tu peux developper une confiance mesuree qui saisit les bonnes opportunites.

## Ton defi
L'exageration de soi, l'arrogance ou la dispersion dans trop d'opportunites.

## Conseil pratique
Choisis les opportunites qui alignent avec ton essence. Pas tout n'est pour toi.""",

    ('jupiter', 'uranus'): """# \u25a1 Carre Jupiter - Uranus
**En une phrase :** Une tension entre expansion et liberation qui peut creer de l'instabilite ou des percees innovantes.

## L'energie de cet aspect
Le carre Jupiter-Uranus cree une friction entre croissance et changement. Cette configuration peut mener a des actions impulsives ou a des innovations audacieuses.

## Ton potentiel
Tu peux canaliser cette energie en innovations constructives qui durent.

## Ton defi
L'instabilite chronique, les changements impulsifs ou l'impatience avec le processus.

## Conseil pratique
Stabilise une base avant de revolutionner. L'innovation a besoin de fondations.""",

    ('jupiter', 'venus'): """# \u25a1 Carre Jupiter - Venus
**En une phrase :** Une tension entre abondance et plaisir qui peut mener aux exces ou a une grande appreciation de la vie.

## L'energie de cet aspect
Le carre Jupiter-Venus cree une friction entre expansion et valeurs. Cette configuration peut amplifier les desirs au point de l'exces.

## Ton potentiel
Tu peux developper une appreciation mesuree des bonnes choses de la vie.

## Ton defi
L'exces dans les plaisirs, les depenses ou l'indulgence envers soi-meme.

## Conseil pratique
Cultive la gratitude plutot que l'accumulation. La satisfaction vient de l'interieur.""",

    ('mars', 'mercury'): """# \u25a1 Carre Mars - Mercure
**En une phrase :** Une tension entre pensee et action qui peut creer des conflits verbaux ou une communication dynamique.

## L'energie de cet aspect
Le carre Mars-Mercure cree une friction entre esprit et energie. Cette configuration peut mener a des paroles impulsives ou a une pensee combative.

## Ton potentiel
Tu peux developper une communication assertive qui defend tes idees sans agresser.

## Ton defi
L'agressivite verbale, les disputes inutiles ou les decisions precipitees.

## Conseil pratique
Compte jusqu'a dix avant de parler sous l'effet de la colere. Les mots blessent.""",

    ('mars', 'moon'): """# \u25a1 Carre Mars - Lune
**En une phrase :** Une tension entre emotions et action qui peut creer des reactions impulsives ou un courage emotionnel.

## L'energie de cet aspect
Le carre Mars-Lune cree une friction entre instinct et energie. Cette configuration peut mener a des reactions emotionnelles intenses et impulsives.

## Ton potentiel
Tu peux developper une capacite a agir avec courage pour proteger ce qui compte.

## Ton defi
Les reactions emotionnelles impulsives, l'agressivite passive ou les conflits domestiques.

## Conseil pratique
Cree un espace entre le ressenti et la reaction. L'emotion informe, elle ne doit pas diriger.""",

    ('mars', 'neptune'): """# \u25a1 Carre Mars - Neptune
**En une phrase :** Une tension entre action directe et confusion qui peut affaiblir la volonte ou inspirer l'action idealisee.

## L'energie de cet aspect
Le carre Mars-Neptune cree une friction entre energie et dissolution. Cette configuration peut mener a des actions confuses ou a une passivite frustrante.

## Ton potentiel
Tu peux apprendre a agir au service d'ideaux tout en restant ancre dans le reel.

## Ton defi
La confusion sur ce que tu veux, l'energie sabotee ou les actions autodestructrices.

## Conseil pratique
Clarifie tes intentions avant d'agir. L'action juste demande une direction claire.""",

    ('mars', 'pluto'): """# \u25a1 Carre Mars - Pluton
**En une phrase :** Une tension intense entre volonte et pouvoir qui peut creer des conflits destructeurs ou une force remarquable.

## L'energie de cet aspect
Le carre Mars-Pluton concentre une energie considerable qui demande un exutoire. Cette configuration peut mener a des confrontations intenses ou a une transformation profonde.

## Ton potentiel
Tu possedes une force de volonte et une endurance exceptionnelles quand bien canalisees.

## Ton defi
Les luttes de pouvoir destructrices, la violence ou l'autodestruction.

## Conseil pratique
Trouve des exutoires sains pour cette energie. Le sport, la creation ou le travail profond.""",

    ('mars', 'saturn'): """# \u25a1 Carre Mars - Saturne
**En une phrase :** Une tension entre impulsion et restriction qui peut frustrer ou forger une discipline remarquable.

## L'energie de cet aspect
Le carre Mars-Saturne cree une friction entre energie et controle. Cette configuration peut mener a la frustration ou a une perseverance forgee par les obstacles.

## Ton potentiel
Tu developpes une endurance et une determination remarquables face aux difficultes.

## Ton defi
La frustration chronique, la colere reprimee ou l'alternance entre exces et blocage.

## Conseil pratique
Accepte les delais comme partie du processus. L'obstacle est le chemin.""",

    ('mars', 'sun'): """# \u25a1 Carre Mars - Soleil
**En une phrase :** Une tension entre identite et energie qui peut creer des conflits d'ego ou une affirmation puissante.

## L'energie de cet aspect
Le carre Mars-Soleil cree une friction entre ego et action. Cette configuration peut mener a des conflits ou a une capacite d'affirmation remarquable.

## Ton potentiel
Tu peux developper une assertivite saine qui exprime ton identite avec force.

## Ton defi
Les conflits d'ego, l'agressivite compensatoire ou l'epuisement par suractivite.

## Conseil pratique
Agis en accord avec tes valeurs, pas pour prouver ta valeur.""",
}

async def insert_interpretations():
    """Insere les interpretations carre part 1 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in SQUARE_PART1.items():
            result = await db.execute(
                select(PregeneratedNatalAspect).where(
                    PregeneratedNatalAspect.planet1 == planet1,
                    PregeneratedNatalAspect.planet2 == planet2,
                    PregeneratedNatalAspect.aspect_type == 'square',
                    PregeneratedNatalAspect.version == 2,
                    PregeneratedNatalAspect.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP {planet1}-{planet2} square")
                skipped += 1
                continue

            interp = PregeneratedNatalAspect(
                planet1=planet1,
                planet2=planet2,
                aspect_type='square',
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"INSERT {planet1}-{planet2} square ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nResultat: {inserted} inserees, {skipped} ignorees")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
