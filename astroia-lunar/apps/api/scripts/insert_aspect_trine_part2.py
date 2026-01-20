#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects trigone (part 2/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

TRINE_PART2 = {
    ('mars', 'uranus'): """# \u25b3 Trigone Mars - Uranus
**En une phrase :** Une energie d'action originale qui innove et libere avec efficacite.

## L'energie de cet aspect
Le trigone Mars-Uranus harmonise action et liberte. Cette configuration donne une capacite a innover dans l'action et a reagir vite aux changements.

## Ton potentiel
Tu initie des changements avec efficacite et tu t'adaptes rapidement aux situations nouvelles.

## Ton defi
La facilite avec le changement peut mener a l'ennui dans la routine.

## Conseil pratique
Cree de la nouveaute dans ton quotidien pour rester motive.""",

    ('mars', 'venus'): """# \u25b3 Trigone Mars - Venus
**En une phrase :** Une harmonie naturelle entre desir et attraction qui facilite les relations et la creativite.

## L'energie de cet aspect
Le trigone Mars-Venus harmonise le masculin et le feminin. Cette configuration donne un charme actif et une creativite fluide.

## Ton potentiel
Tu seduis et tu crees avec une aisance naturelle qui attire les bonnes choses.

## Ton defi
L'aisance relationnelle peut mener a eviter l'effort dans les relations profondes.

## Conseil pratique
Approfondis les relations faciles. L'intimite demande plus que le charme.""",

    ('mercury', 'moon'): """# \u25b3 Trigone Mercure - Lune
**En une phrase :** Une pensee naturellement connectee aux emotions qui communique avec empathie.

## L'energie de cet aspect
Le trigone Mercure-Lune harmonise raison et emotion. Cette configuration donne une intelligence emotionnelle naturelle.

## Ton potentiel
Tu comprends et tu exprimes les emotions avec facilite et justesse.

## Ton defi
La facilite a melanger pensee et emotion peut manquer d'objectivite.

## Conseil pratique
Developpe aussi ta capacite d'analyse froide quand necessaire.""",

    ('mercury', 'neptune'): """# \u25b3 Trigone Mercure - Neptune
**En une phrase :** Un esprit naturellement imaginatif qui percoit et communique les subtilites.

## L'energie de cet aspect
Le trigone Mercure-Neptune harmonise logique et intuition. Cette configuration donne une pensee creative et une capacite a percevoir l'invisible.

## Ton potentiel
Tu communiques avec poesie et tu saisis les nuances que d'autres manquent.

## Ton defi
La facilite imaginative peut eloigner de la precision factuelle.

## Conseil pratique
Ancre tes intuitions dans des faits verifiables quand c'est important.""",

    ('mercury', 'pluto'): """# \u25b3 Trigone Mercure - Pluton
**En une phrase :** Un esprit penetrant qui comprend naturellement les motivations profondes.

## L'energie de cet aspect
Le trigone Mercure-Pluton harmonise pensee et profondeur. Cette configuration donne une capacite d'investigation et de persuasion naturelles.

## Ton potentiel
Tu percois ce qui est cache et tu communiques avec impact.

## Ton defi
La facilite a percevoir les profondeurs peut mener a voir des complots partout.

## Conseil pratique
Utilise ta penetration pour comprendre, pas pour manipuler.""",

    ('mercury', 'saturn'): """# \u25b3 Trigone Mercure - Saturne
**En une phrase :** Une pensee naturellement structuree qui organise et communique avec precision.

## L'energie de cet aspect
Le trigone Mercure-Saturne harmonise pensee et discipline. Cette configuration donne une rigueur intellectuelle et une communication claire.

## Ton potentiel
Tu structures les idees complexes et tu les transmets de facon comprehensible.

## Ton defi
La rigueur naturelle peut manquer de creativite ou de fantaisie.

## Conseil pratique
Ose des idees moins structurees parfois. L'innovation vient aussi du chaos.""",

    ('mercury', 'sun'): """# \u25b3 Trigone Mercure - Soleil
**En une phrase :** Une communication naturellement alignee avec l'identite qui s'exprime avec clarte.

## L'energie de cet aspect
Le trigone Mercure-Soleil harmonise pensee et ego. Cette configuration donne une expression de soi claire et une pensee personnelle.

## Ton potentiel
Tu communiques qui tu es avec aisance et authenticite.

## Ton defi
L'alignement naturel peut manquer de perspective sur soi-meme.

## Conseil pratique
Cherche des feedbacks externes pour enrichir ta vision de toi-meme.""",

    ('mercury', 'uranus'): """# \u25b3 Trigone Mercure - Uranus
**En une phrase :** Un esprit naturellement original qui pense vite et innove avec facilite.

## L'energie de cet aspect
Le trigone Mercure-Uranus harmonise pensee et originalite. Cette configuration donne une intelligence vive et des idees novatrices.

## Ton potentiel
Tu percois des connexions que d'autres ne voient pas et tu les communiques avec eclat.

## Ton defi
La facilite avec l'originalite peut mepriser la pensee conventionnelle.

## Conseil pratique
Traduis tes idees originales dans un langage accessible aux autres.""",

    ('mercury', 'venus'): """# \u25b3 Trigone Mercure - Venus
**En une phrase :** Une communication naturellement elegante qui charme et harmonise.

## L'energie de cet aspect
Le trigone Mercure-Venus harmonise pensee et beaute. Cette configuration donne une expression raffinee et un talent pour la diplomatie.

## Ton potentiel
Tu communiques avec grace et tu crees l'harmonie par les mots.

## Ton defi
L'elegance naturelle peut eviter les verites desagreables.

## Conseil pratique
La verite peut etre dite avec grace. N'evite pas les sujets difficiles.""",

    ('moon', 'neptune'): """# \u25b3 Trigone Lune - Neptune
**En une phrase :** Une sensibilite naturellement spirituelle qui percoit et nourrit avec compassion.

## L'energie de cet aspect
Le trigone Lune-Neptune harmonise emotion et intuition. Cette configuration donne une empathie profonde et une connexion naturelle au subtil.

## Ton potentiel
Tu ressens ce que les autres ressentent et tu offres une presence guerissante.

## Ton defi
La porosite emotionnelle peut confondre tes emotions avec celles des autres.

## Conseil pratique
Protege ta sensibilite par des frontieres claires. Tu peux compatir sans absorber.""",

    ('moon', 'pluto'): """# \u25b3 Trigone Lune - Pluton
**En une phrase :** Une profondeur emotionnelle naturelle qui transforme et regenere avec intensite.

## L'energie de cet aspect
Le trigone Lune-Pluton harmonise emotion et transformation. Cette configuration donne une force emotionnelle et une capacite de regeneration.

## Ton potentiel
Tu traverses les crises emotionnelles avec force et tu en ressors transforme.

## Ton defi
L'aisance avec l'intensite peut rechercher le drame inutilement.

## Conseil pratique
Apprecie aussi la legerete. Toutes les emotions ne doivent pas etre intenses.""",

    ('moon', 'saturn'): """# \u25b3 Trigone Lune - Saturne
**En une phrase :** Une stabilite emotionnelle naturelle qui offre securite et fiabilite.

## L'energie de cet aspect
Le trigone Lune-Saturne harmonise emotion et structure. Cette configuration donne une maturite emotionnelle et une capacite a offrir du soutien stable.

## Ton potentiel
Tu es un roc pour les autres, fiable et constant dans tes engagements.

## Ton defi
La stabilite naturelle peut manquer de spontaneite emotionnelle.

## Conseil pratique
Laisse-toi surprendre par tes emotions parfois. La vulnerabilite est humaine.""",

    ('moon', 'sun'): """# \u25b3 Trigone Lune - Soleil
**En une phrase :** Une harmonie naturelle entre conscient et inconscient qui cree une personnalite equilibree.

## L'energie de cet aspect
Le trigone Lune-Soleil harmonise identite et emotions. Cette configuration donne une coherence interieure et une expression de soi authentique.

## Ton potentiel
Tu es en paix avec toi-meme et tu l'exprimes naturellement.

## Ton defi
L'harmonie interieure peut manquer de profondeur psychologique.

## Conseil pratique
Explore aussi tes ombres. L'integration complete inclut les parts difficiles.""",

    ('moon', 'uranus'): """# \u25b3 Trigone Lune - Uranus
**En une phrase :** Une liberte emotionnelle naturelle qui s'adapte et innove dans les relations.

## L'energie de cet aspect
Le trigone Lune-Uranus harmonise emotion et independance. Cette configuration donne une originalite emotionnelle et une adaptabilite.

## Ton potentiel
Tu vis tes emotions de facon authentique et non conventionnelle.

## Ton defi
L'aisance avec le changement emotionnel peut manquer de profondeur.

## Conseil pratique
Permets-toi aussi des attachements durables. La liberte n'exclut pas l'engagement.""",

    ('moon', 'venus'): """# \u25b3 Trigone Lune - Venus
**En une phrase :** Une douceur naturelle qui attire l'affection et cree l'harmonie.

## L'energie de cet aspect
Le trigone Lune-Venus harmonise besoins emotionnels et valeurs. Cette configuration donne un charme naturel et une capacite a nourrir les relations.

## Ton potentiel
Tu crees une atmosphere agreable et tu attires l'amour naturellement.

## Ton defi
L'aisance relationnelle peut eviter les conflits necessaires.

## Conseil pratique
L'harmonie veritable inclut la capacite a traverser les desaccords.""",
}

async def insert_interpretations():
    """Insere les interpretations trigone part 2 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in TRINE_PART2.items():
            result = await db.execute(
                select(PregeneratedNatalAspect).where(
                    PregeneratedNatalAspect.planet1 == planet1,
                    PregeneratedNatalAspect.planet2 == planet2,
                    PregeneratedNatalAspect.aspect_type == 'trine',
                    PregeneratedNatalAspect.version == 2,
                    PregeneratedNatalAspect.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP {planet1}-{planet2} trine")
                skipped += 1
                continue

            interp = PregeneratedNatalAspect(
                planet1=planet1,
                planet2=planet2,
                aspect_type='trine',
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"INSERT {planet1}-{planet2} trine ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nResultat: {inserted} inserees, {skipped} ignorees")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
