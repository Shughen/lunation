#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects carre (part 3/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

SQUARE_PART3 = {
    ('neptune', 'pluto'): """# \u25a1 Carre Neptune - Pluton
**En une phrase :** Un aspect generationnel extremement rare qui marque des tensions profondes entre spiritualite et transformation collective.

## L'energie de cet aspect
Le carre Neptune-Pluton est si rare qu'il ne concerne pratiquement personne vivant aujourd'hui. Il symboliserait des tensions majeures entre dissolution et regeneration au niveau collectif.

## Ton potentiel
Cet aspect marquerait une epoque de transformation spirituelle intense.

## Ton defi
Les tensions entre ideaux spirituels et forces de transformation profondes.

## Conseil pratique
Si tu as cet aspect, tu portes une mission generationnelle unique.""",

    ('neptune', 'saturn'): """# \u25a1 Carre Neptune - Saturne
**En une phrase :** Une tension entre reve et realite qui peut creer de la deception ou une capacite a materialiser l'ideal.

## L'energie de cet aspect
Le carre Neptune-Saturne cree une friction entre inspiration et structure. Cette configuration peut mener a des deceptions face au reel ou a une sagesse pratique.

## Ton potentiel
Tu peux apprendre a donner forme aux reves sans les trahir.

## Ton defi
La deception, le cynisme ou la difficulte a concretiser les aspirations.

## Conseil pratique
L'ideal guide, le travail accomplit. Accepte l'imperfection de la realisation.""",

    ('neptune', 'sun'): """# \u25a1 Carre Neptune - Soleil
**En une phrase :** Une tension entre identite claire et dissolution qui peut creer de la confusion ou une creativite transcendante.

## L'energie de cet aspect
Le carre Neptune-Soleil cree une friction entre ego et transcendance. Cette configuration peut brouiller l'identite ou ouvrir a une creativite spirituelle.

## Ton potentiel
Tu peux developper une identite qui integre le mystere sans se perdre.

## Ton defi
La confusion identitaire, les illusions sur soi ou les tendances a la fuite.

## Conseil pratique
Definis-toi par tes creations et tes valeurs concretes. L'ego sain sert l'ame.""",

    ('neptune', 'uranus'): """# \u25a1 Carre Neptune - Uranus
**En une phrase :** Un aspect generationnel qui marque des tensions entre ideaux spirituels et revolutions technologiques.

## L'energie de cet aspect
Le carre Neptune-Uranus concerne des generations et marque des periodes de tension entre tradition spirituelle et innovation. A l'echelle personnelle, il donne une sensibilite a ces themes.

## Ton potentiel
Tu peux contribuer a reconcilier spiritualite et progres.

## Ton defi
L'oscillation entre utopisme spirituel et materialisme technologique.

## Conseil pratique
La technologie peut servir l'ame. L'innovation peut etre spirituelle.""",

    ('neptune', 'venus'): """# \u25a1 Carre Neptune - Venus
**En une phrase :** Une tension entre amour ideal et amour reel qui peut creer des desillusions ou un amour transcendant.

## L'energie de cet aspect
Le carre Neptune-Venus cree une friction entre romantisme et realite. Cette configuration peut mener a des deceptions amoureuses ou a un raffinement artistique.

## Ton potentiel
Tu peux developper un amour qui accepte l'imperfection tout en aspirant au beau.

## Ton defi
Les illusions amoureuses, les deceptions ou les sacrifices excessifs.

## Conseil pratique
Aime les personnes reelles, pas les projections. La beaute est aussi dans l'imparfait.""",

    ('pluto', 'saturn'): """# \u25a1 Carre Pluton - Saturne
**En une phrase :** Une tension puissante entre transformation et structure qui peut creer des crises ou des reconstructions majeures.

## L'energie de cet aspect
Le carre Pluton-Saturne cree une friction entre pouvoir et autorite. Cette configuration peut mener a des confrontations avec les systemes ou a une capacite de reforme profonde.

## Ton potentiel
Tu peux transformer les structures obsoletes et construire du neuf durable.

## Ton defi
Les luttes de pouvoir avec l'autorite, la rigidite ou l'obsession du controle.

## Conseil pratique
Transforme les systemes de l'interieur. Le pouvoir durable construit.""",

    ('pluto', 'sun'): """# \u25a1 Carre Pluton - Soleil
**En une phrase :** Une tension intense entre identite et pouvoir qui peut creer des crises de transformation ou un charisme remarquable.

## L'energie de cet aspect
Le carre Pluton-Soleil cree une friction entre ego et forces transformatrices. Cette configuration peut mener a des crises identitaires profondes ou a une regeneration puissante.

## Ton potentiel
Tu developpes une capacite de renaissance et un charisme magnetique.

## Ton defi
Les luttes de pouvoir, les crises d'ego ou les confrontations destructrices.

## Conseil pratique
Laisse mourir ce qui doit mourir. La renaissance suit la mort de l'ancien.""",

    ('pluto', 'uranus'): """# \u25a1 Carre Pluton - Uranus
**En une phrase :** Un aspect generationnel qui marque des periodes de tensions revolutionnaires et de transformations radicales.

## L'energie de cet aspect
Le carre Pluton-Uranus concerne des generations et marque des periodes de bouleversements. A l'echelle personnelle, il donne une sensibilite aux transformations collectives.

## Ton potentiel
Tu participes activement aux changements de ton epoque.

## Ton defi
L'extremisme, l'impatience ou le sentiment d'impuissance face aux forces collectives.

## Conseil pratique
Trouve ton role dans les transformations. L'individu peut influencer l'histoire.""",

    ('pluto', 'venus'): """# \u25a1 Carre Pluton - Venus
**En une phrase :** Une tension intense entre amour et pouvoir qui peut creer des passions destructrices ou transformatrices.

## L'energie de cet aspect
Le carre Pluton-Venus cree une friction entre affection et intensite. Cette configuration peut mener a des relations intenses et potentiellement difficiles.

## Ton potentiel
Tu peux vivre des amours qui transforment profondement quand tu transcendes les jeux de pouvoir.

## Ton defi
La jalousie, la possessivite ou les attractions fatales.

## Conseil pratique
L'amour veritable libere. Transforme la passion en intimite profonde.""",

    ('saturn', 'sun'): """# \u25a1 Carre Saturne - Soleil
**En une phrase :** Une tension entre expression de soi et responsabilites qui peut creer des obstacles ou forger le caractere.

## L'energie de cet aspect
Le carre Saturne-Soleil cree une friction entre ego et discipline. Cette configuration peut mener a des periodes de doute ou a une maturite forgee par les epreuves.

## Ton potentiel
Tu developpes une identite solide construite par l'effort et la perseverance.

## Ton defi
Le pessimisme, le doute de soi ou la pression excessive des responsabilites.

## Conseil pratique
Les obstacles forgent le caractere. Celebre tes accomplissements.""",

    ('saturn', 'uranus'): """# \u25a1 Carre Saturne - Uranus
**En une phrase :** Une tension classique entre tradition et innovation qui peut creer des conflits ou une capacite de reforme.

## L'energie de cet aspect
Le carre Saturne-Uranus cree une friction entre structure et liberte. Cette configuration peut mener a des oscillations entre conservatisme et rebellion.

## Ton potentiel
Tu peux developper une capacite a innover de facon durable et structuree.

## Ton defi
L'immobilisme par peur ou la destruction prematuree des fondations.

## Conseil pratique
Reforme plutot que de revolutionner. Le changement durable respecte certaines bases.""",

    ('saturn', 'venus'): """# \u25a1 Carre Saturne - Venus
**En une phrase :** Une tension entre amour et devoir qui peut creer des difficultes relationnelles ou des engagements solides.

## L'energie de cet aspect
Le carre Saturne-Venus cree une friction entre affection et responsabilite. Cette configuration peut mener a des inhibitions amoureuses ou a une fidelite profonde.

## Ton potentiel
Tu construis des relations durables basees sur le respect et l'engagement.

## Ton defi
La froideur, la peur de l'intimite ou le sacrifice de l'amour pour le devoir.

## Conseil pratique
L'amour merite de l'espace dans ta vie. L'engagement peut etre chaleureux.""",

    ('sun', 'uranus'): """# \u25a1 Carre Soleil - Uranus
**En une phrase :** Une tension entre identite stable et besoin de changement qui peut creer de l'instabilite ou une originalite assumee.

## L'energie de cet aspect
Le carre Soleil-Uranus cree une friction entre ego et independance. Cette configuration peut mener a des ruptures identitaires ou a un courage d'etre different.

## Ton potentiel
Tu developpes une identite authentique qui refuse les compromis avec l'essence.

## Ton defi
L'instabilite identitaire, la rebellion sterile ou la difficulte a s'engager.

## Conseil pratique
Sois fidele a toi-meme tout en creant des liens. L'originalite n'exclut pas l'appartenance.""",

    ('sun', 'venus'): """# \u25a1 Carre Soleil - Venus
**En une phrase :** Une tension entre expression de soi et harmonie qui peut creer des conflits relationnels ou un raffinement personnel.

## L'energie de cet aspect
Le carre Soleil-Venus cree une friction entre identite et valeurs. Cette configuration peut mener a des oscillations entre s'affirmer et plaire.

## Ton potentiel
Tu peux developper une expression de soi qui integre authenticite et grace.

## Ton defi
La perte de soi dans les relations ou l'affirmation qui blesse.

## Conseil pratique
Sois toi-meme avec elegance. L'authenticite n'empeche pas la diplomatie.""",

    ('uranus', 'venus'): """# \u25a1 Carre Uranus - Venus
**En une phrase :** Une tension entre liberte et attachement qui peut creer de l'instabilite relationnelle ou des relations innovantes.

## L'energie de cet aspect
Le carre Uranus-Venus cree une friction entre independance et amour. Cette configuration peut mener a des attractions soudaines et des ruptures inattendues.

## Ton potentiel
Tu peux developper des relations qui honorent la liberte de chacun.

## Ton defi
L'instabilite relationnelle, la peur de l'engagement ou les ruptures impulsives.

## Conseil pratique
La liberte et l'amour ne s'excluent pas. Cree tes propres regles relationnelles.""",
}

async def insert_interpretations():
    """Insere les interpretations carre part 3 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in SQUARE_PART3.items():
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
