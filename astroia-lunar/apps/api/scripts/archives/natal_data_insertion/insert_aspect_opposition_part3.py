#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects opposition (part 3/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

OPPOSITION_PART3 = {
    ('neptune', 'pluto'): """# \u260d Opposition Neptune - Pluton
**En une phrase :** Un aspect generationnel rare qui marque des tensions collectives entre ideaux spirituels et transformations profondes.

## L'energie de cet aspect
L'opposition Neptune-Pluton est extremement rare et concerne des generations entieres. Elle symbolise des tensions entre dissolution et regeneration au niveau collectif.

## Ton potentiel
Tu participes a des mouvements de transformation spirituelle qui depassent l'individuel.

## Ton defi
Se sentir impuissant face aux forces collectives ou se perdre dans des ideologies extremes.

## Conseil pratique
Trouve ta contribution unique aux transformations collectives. L'individu compte dans le collectif.""",

    ('neptune', 'saturn'): """# \u260d Opposition Neptune - Saturne
**En une phrase :** Une tension entre reve et realite qui demande de construire des ponts entre l'ideal et le concret.

## L'energie de cet aspect
L'opposition Neptune-Saturne polarise l'inspiration et la structure. Cette configuration peut creer des periodes de doute sur ses ideaux ou une capacite a materialiser les reves.

## Ton potentiel
Tu sais donner forme aux visions et ancrer l'inspiration dans la realite.

## Ton defi
La deception face a l'ecart entre l'ideal et le reel ou le cynisme peuvent survenir.

## Conseil pratique
Accepte l'imperfection de la realisation. Le reve guide, le travail accomplit.""",

    ('neptune', 'sun'): """# \u260d Opposition Neptune - Soleil
**En une phrase :** Une tension entre identite claire et dissolution qui demande de trouver sa voie sans perdre son ame.

## L'energie de cet aspect
L'opposition Neptune-Soleil polarise l'ego et la transcendance. Cette configuration peut creer des periodes de confusion identitaire ou une identite spirituelle elevee.

## Ton potentiel
Tu peux inspirer les autres par ta vision tout en restant ancre dans ta realite.

## Ton defi
La perte d'identite dans les illusions ou les dependances peut destabiliser.

## Conseil pratique
Definis-toi par tes creations et tes valeurs. L'ego sain sert l'ame.""",

    ('neptune', 'uranus'): """# \u260d Opposition Neptune - Uranus
**En une phrase :** Un aspect generationnel qui marque des tensions entre ideaux spirituels et revolutions technologiques.

## L'energie de cet aspect
L'opposition Neptune-Uranus concerne des generations et marque des periodes de tension entre tradition spirituelle et innovation. A l'echelle personnelle, elle donne une sensibilite a ces themes.

## Ton potentiel
Tu peux integrer intuition et innovation pour imaginer des futurs spirituels nouveaux.

## Ton defi
L'oscillation entre utopisme spirituel et technologie deshumanisante.

## Conseil pratique
Mets la technologie au service de la connexion humaine. L'innovation peut servir l'ame.""",

    ('neptune', 'venus'): """# \u260d Opposition Neptune - Venus
**En une phrase :** Une tension entre amour ideal et amour reel qui peut creer des desillusions ou un amour transcendant.

## L'energie de cet aspect
L'opposition Neptune-Venus polarise l'amour romantique et l'amour spirituel. Cette configuration peut creer des attentes irrealistes ou une capacite d'amour inconditionnel.

## Ton potentiel
Tu peux vivre des amours profondes et inspirer par ta vision de l'amour.

## Ton defi
Les illusions amoureuses, la deception et les sacrifices excessifs peuvent blesser.

## Conseil pratique
Aime les personnes reelles, pas les projections. L'amour veritable accepte l'imperfection.""",

    ('pluto', 'saturn'): """# \u260d Opposition Pluton - Saturne
**En une phrase :** Une tension puissante entre transformation et structure qui peut creer des crises ou des reconstructions majeures.

## L'energie de cet aspect
L'opposition Pluton-Saturne polarise le pouvoir et l'autorite. Cette configuration peut creer des confrontations avec les structures etablies ou une capacite de reforme profonde.

## Ton potentiel
Tu sais transformer les structures obsoletes et construire sur des bases renouvelees.

## Ton defi
Les luttes de pouvoir avec l'autorite ou la rigidite face au changement necessaire.

## Conseil pratique
Transforme les systemes de l'interieur. Le pouvoir durable construit plus qu'il ne detruit.""",

    ('pluto', 'sun'): """# \u260d Opposition Pluton - Soleil
**En une phrase :** Une tension intense entre identite et pouvoir qui peut creer des crises de transformation personnelle profondes.

## L'energie de cet aspect
L'opposition Pluton-Soleil polarise l'ego et les forces transformatrices. Cette configuration peut creer des confrontations de pouvoir ou des renaissances identitaires.

## Ton potentiel
Tu possedes une capacite de regeneration identitaire et un charisme puissant.

## Ton defi
Les luttes de pouvoir qui epuisent ou les crises identitaires destructrices.

## Conseil pratique
Laisse mourir ce qui doit mourir dans ton identite. La renaissance suit la mort de l'ancien.""",

    ('pluto', 'uranus'): """# \u260d Opposition Pluton - Uranus
**En une phrase :** Un aspect generationnel qui marque des periodes de tensions revolutionnaires et de transformations societales majeures.

## L'energie de cet aspect
L'opposition Pluton-Uranus concerne des generations et marque des periodes de bouleversements. A l'echelle personnelle, elle donne une sensibilite aux transformations collectives.

## Ton potentiel
Tu participes activement aux changements de ton epoque avec intensite et vision.

## Ton defi
L'extremisme revolutionnaire ou l'impuissance face aux forces collectives.

## Conseil pratique
Trouve ton role dans les transformations collectives. L'individu peut influencer le cours de l'histoire.""",

    ('pluto', 'venus'): """# \u260d Opposition Pluton - Venus
**En une phrase :** Une tension intense entre amour et pouvoir qui peut creer des passions destructrices ou transformatrices.

## L'energie de cet aspect
L'opposition Pluton-Venus polarise l'amour et l'intensite. Cette configuration peut creer des attractions fatales ou des amours profondement transformateurs.

## Ton potentiel
Tu sais vivre des amours intenses qui transforment profondement les deux partenaires.

## Ton defi
La jalousie, la possessivite ou les jeux de pouvoir peuvent empoisonner les relations.

## Conseil pratique
Transforme la passion en intimite profonde. L'amour veritable libere plutot qu'il n'enchaine.""",

    ('saturn', 'sun'): """# \u260d Opposition Saturne - Soleil
**En une phrase :** Une tension entre expression de soi et responsabilites qui demande de construire une identite solide par l'effort.

## L'energie de cet aspect
L'opposition Saturne-Soleil polarise l'ego et la discipline. Cette configuration peut creer des periodes de doute ou une maturite remarquable.

## Ton potentiel
Tu developpes une identite forgee par l'experience et les epreuves surmontees.

## Ton defi
Le pessimisme, le doute de soi ou la pression excessive des responsabilites.

## Conseil pratique
Celebre tes accomplissements. La reconnaissance interieure compte plus que l'externe.""",

    ('saturn', 'uranus'): """# \u260d Opposition Saturne - Uranus
**En une phrase :** Une tension classique entre tradition et innovation qui demande d'equilibrer stabilite et changement.

## L'energie de cet aspect
L'opposition Saturne-Uranus polarise la structure et la liberation. Cette configuration peut creer des oscillations entre conservatisme et rebellion.

## Ton potentiel
Tu sais integrer l'innovation dans les structures existantes de facon durable.

## Ton defi
L'immobilisme par peur du changement ou la destruction prematuree des fondations.

## Conseil pratique
Reforme plutot que de revolutionner. Le changement durable respecte certaines bases.""",

    ('saturn', 'venus'): """# \u260d Opposition Saturne - Venus
**En une phrase :** Une tension entre amour et devoir qui demande d'equilibrer engagement et liberte affective.

## L'energie de cet aspect
L'opposition Saturne-Venus polarise l'affection et la responsabilite. Cette configuration peut creer des relations difficiles ou des engagements solides.

## Ton potentiel
Tu construis des relations durables basees sur le respect mutuel et l'engagement.

## Ton defi
La froideur apparente, la peur de l'intimite ou le sacrifice de l'amour pour le devoir.

## Conseil pratique
L'amour et la responsabilite ne s'excluent pas. L'engagement peut etre chaleureux.""",

    ('sun', 'uranus'): """# \u260d Opposition Soleil - Uranus
**En une phrase :** Une tension entre identite stable et besoin de changement qui peut creer de l'instabilite ou une originalite assumee.

## L'energie de cet aspect
L'opposition Soleil-Uranus polarise l'ego et l'independance. Cette configuration peut creer des ruptures identitaires ou une liberte d'etre soi remarquable.

## Ton potentiel
Tu sais te reinventer et exprimer ton originalite de facon authentique.

## Ton defi
L'instabilite identitaire ou le refus de tout engagement peuvent isoler.

## Conseil pratique
Sois fidele a toi-meme tout en creant des liens. L'originalite n'exclut pas l'appartenance.""",

    ('sun', 'venus'): """# \u260d Opposition Soleil - Venus
**En une phrase :** Une tension entre expression de soi et harmonie relationnelle qui demande d'equilibrer authenticite et diplomatie.

## L'energie de cet aspect
L'opposition Soleil-Venus polarise l'identite et les relations. Cette configuration peut creer une oscillation entre s'affirmer et plaire aux autres.

## Ton potentiel
Tu peux etre authentique tout en maintenant des relations harmonieuses.

## Ton defi
La perte de soi dans les relations ou l'affirmation excessive qui blesse.

## Conseil pratique
Sois toi-meme avec elegance. L'authenticite n'empeche pas la grace.""",

    ('uranus', 'venus'): """# \u260d Opposition Uranus - Venus
**En une phrase :** Une tension entre liberte et attachement qui peut creer des relations non conventionnelles ou de l'instabilite affective.

## L'energie de cet aspect
L'opposition Uranus-Venus polarise l'independance et l'amour. Cette configuration peut creer des attractions soudaines ou des ruptures inattendues.

## Ton potentiel
Tu sais vivre des relations qui respectent la liberte de chacun.

## Ton defi
L'instabilite relationnelle ou la peur de l'engagement peuvent empecher l'intimite.

## Conseil pratique
Trouve des partenaires qui partagent ton besoin d'espace. L'amour libre a ses propres regles.""",
}

async def insert_interpretations():
    """Insere les interpretations opposition part 3 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in OPPOSITION_PART3.items():
            result = await db.execute(
                select(PregeneratedNatalAspect).where(
                    PregeneratedNatalAspect.planet1 == planet1,
                    PregeneratedNatalAspect.planet2 == planet2,
                    PregeneratedNatalAspect.aspect_type == 'opposition',
                    PregeneratedNatalAspect.version == 2,
                    PregeneratedNatalAspect.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP {planet1}-{planet2} opposition")
                skipped += 1
                continue

            interp = PregeneratedNatalAspect(
                planet1=planet1,
                planet2=planet2,
                aspect_type='opposition',
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"INSERT {planet1}-{planet2} opposition ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nResultat: {inserted} inserees, {skipped} ignorees")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
