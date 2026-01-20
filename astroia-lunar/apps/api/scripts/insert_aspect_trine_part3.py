#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects trigone (part 3/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

TRINE_PART3 = {
    ('neptune', 'pluto'): """# \u25b3 Trigone Neptune - Pluton
**En une phrase :** Un aspect generationnel qui harmonise intuition spirituelle et transformation profonde.

## L'energie de cet aspect
Le trigone Neptune-Pluton est generationnel et dure des decennies. Il cree une harmonie entre les energies de dissolution et de regeneration au niveau collectif.

## Ton potentiel
Tu participes naturellement aux mouvements spirituels et transformateurs de ton epoque.

## Ton defi
L'aspect generationnel peut sembler impersonnel ou hors de portee individuelle.

## Conseil pratique
Trouve comment tu incarnes cette transformation spirituelle a ton echelle.""",

    ('neptune', 'saturn'): """# \u25b3 Trigone Neptune - Saturne
**En une phrase :** Une capacite naturelle a materialiser les reves et a structurer l'inspiration.

## L'energie de cet aspect
Le trigone Neptune-Saturne harmonise l'ideal et le reel. Cette configuration donne une capacite a donner forme aux visions de facon pratique.

## Ton potentiel
Tu sais transformer les inspirations en realisations concretes et durables.

## Ton defi
L'aisance a concretiser les reves peut manquer de l'audace de l'impossible.

## Conseil pratique
Ose des reves plus grands. Tu as la capacite de les realiser.""",

    ('neptune', 'sun'): """# \u25b3 Trigone Neptune - Soleil
**En une phrase :** Une identite naturellement inspiree qui rayonne compassion et creativite.

## L'energie de cet aspect
Le trigone Neptune-Soleil harmonise ego et transcendance. Cette configuration donne un charisme inspire et une identite spirituelle.

## Ton potentiel
Tu inspires les autres par ta vision et tu exprimes naturellement la beaute.

## Ton defi
L'aisance spirituelle peut eviter les realites difficiles.

## Conseil pratique
Ancre ton inspiration dans des actions concretes. L'ideal se vit au quotidien.""",

    ('neptune', 'uranus'): """# \u25b3 Trigone Neptune - Uranus
**En une phrase :** Un aspect generationnel qui harmonise intuition et innovation pour des avenirs visionnaires.

## L'energie de cet aspect
Le trigone Neptune-Uranus est generationnel et cree une synergie entre inspiration et originalite au niveau collectif.

## Ton potentiel
Tu combines naturellement intuition spirituelle et pensee novatrice.

## Ton defi
L'aspect generationnel peut sembler abstrait au niveau personnel.

## Conseil pratique
Incarne cette synergie dans des projets concrets qui servent l'avenir.""",

    ('neptune', 'venus'): """# \u25b3 Trigone Neptune - Venus
**En une phrase :** Un amour naturellement spirituel et une sensibilite artistique raffinee.

## L'energie de cet aspect
Le trigone Neptune-Venus harmonise amour et transcendance. Cette configuration donne une capacite d'amour inconditionnel et un talent artistique.

## Ton potentiel
Tu crees et tu aimes avec une beaute qui eleve les autres.

## Ton defi
L'idealisation naturelle peut manquer d'ancrage dans l'amour reel.

## Conseil pratique
Aime les personnes reelles dans leur imperfection. La beaute est aussi dans le concret.""",

    ('pluto', 'saturn'): """# \u25b3 Trigone Pluton - Saturne
**En une phrase :** Un pouvoir naturel de transformation structuree qui reconstruit durablement.

## L'energie de cet aspect
Le trigone Pluton-Saturne harmonise transformation et structure. Cette configuration donne une capacite a reformer les systemes en profondeur.

## Ton potentiel
Tu transformes les structures avec patience et efficacite, creant des changements durables.

## Ton defi
L'aisance avec le pouvoir peut devenir ambition excessive.

## Conseil pratique
Mets ton pouvoir au service du bien commun. La transformation durable sert tous.""",

    ('pluto', 'sun'): """# \u25b3 Trigone Pluton - Soleil
**En une phrase :** Une identite puissante qui se regenere et transforme avec charisme naturel.

## L'energie de cet aspect
Le trigone Pluton-Soleil harmonise ego et pouvoir. Cette configuration donne un magnetisme et une capacite de renouvellement remarquables.

## Ton potentiel
Tu renas de tes cendres et tu inspires les autres par ta force interieure.

## Ton defi
L'aisance avec le pouvoir peut intimider involontairement.

## Conseil pratique
Utilise ton charisme pour elever les autres, pas pour les dominer.""",

    ('pluto', 'uranus'): """# \u25b3 Trigone Pluton - Uranus
**En une phrase :** Un aspect generationnel qui harmonise revolution et transformation pour des changements profonds.

## L'energie de cet aspect
Le trigone Pluton-Uranus est generationnel et cree une synergie entre changement radical et transformation profonde.

## Ton potentiel
Tu participes naturellement aux grandes transformations de ton epoque.

## Ton defi
L'aspect generationnel peut sembler impersonnel.

## Conseil pratique
Trouve ton role unique dans les transformations collectives.""",

    ('pluto', 'venus'): """# \u25b3 Trigone Pluton - Venus
**En une phrase :** Une capacite naturelle a vivre des amours profondes et transformatrices.

## L'energie de cet aspect
Le trigone Pluton-Venus harmonise amour et intensite. Cette configuration donne une passion profonde et un magnetisme seducteur.

## Ton potentiel
Tu vis des amours qui transforment positivement les deux partenaires.

## Ton defi
L'aisance avec l'intensite peut rechercher le drame inutilement.

## Conseil pratique
Apprecie aussi la legerete en amour. L'intimite profonde inclut la joie simple.""",

    ('saturn', 'sun'): """# \u25b3 Trigone Saturne - Soleil
**En une phrase :** Une identite naturellement mature qui s'affirme par l'effort et la responsabilite.

## L'energie de cet aspect
Le trigone Saturne-Soleil harmonise ego et discipline. Cette configuration donne une confiance construite et une autorite naturelle.

## Ton potentiel
Tu inspires respect par ta maturite et ta fiabilite.

## Ton defi
La maturite naturelle peut manquer de legerete ou de spontaneite.

## Conseil pratique
Permets-toi aussi la joie et le jeu. La sagesse inclut le rire.""",

    ('saturn', 'uranus'): """# \u25b3 Trigone Saturne - Uranus
**En une phrase :** Une capacite naturelle a innover de facon structuree et durable.

## L'energie de cet aspect
Le trigone Saturne-Uranus harmonise tradition et innovation. Cette configuration donne une capacite a reformer les systemes de facon pratique.

## Ton potentiel
Tu integres le nouveau dans l'ancien avec sagesse et efficacite.

## Ton defi
L'equilibre naturel peut manquer d'audace revolutionnaire.

## Conseil pratique
Ose des innovations plus radicales. Tu as la structure pour les soutenir.""",

    ('saturn', 'venus'): """# \u25b3 Trigone Saturne - Venus
**En une phrase :** Une capacite naturelle a construire des relations durables et des valeurs solides.

## L'energie de cet aspect
Le trigone Saturne-Venus harmonise amour et engagement. Cette configuration donne une loyaute naturelle et un sens des valeurs stable.

## Ton potentiel
Tu construis des relations fiables et tu apprécies la beaute durable.

## Ton defi
La stabilité naturelle peut manquer de passion ou de spontaneite.

## Conseil pratique
Injecte de la nouveaute dans tes relations etablies. La fidelite peut etre aventureuse.""",

    ('sun', 'uranus'): """# \u25b3 Trigone Soleil - Uranus
**En une phrase :** Une identite naturellement originale qui s'exprime avec authenticite et liberte.

## L'energie de cet aspect
Le trigone Soleil-Uranus harmonise ego et independance. Cette configuration donne une originalite assumee et un charisme unique.

## Ton potentiel
Tu inspires les autres par ton authenticite et ton courage d'etre different.

## Ton defi
L'aisance avec l'originalite peut mepriser le conventionnel.

## Conseil pratique
L'originalite n'exclut pas le respect des autres. Sois unique avec grace.""",

    ('sun', 'venus'): """# \u25b3 Trigone Soleil - Venus
**En une phrase :** Un charme naturel qui attire l'amour et la reconnaissance avec aisance.

## L'energie de cet aspect
Le trigone Soleil-Venus harmonise identite et valeurs. Cette configuration donne un magnetisme agreable et une appreciation de la beaute.

## Ton potentiel
Tu attires naturellement ce que tu desires et tu crees de l'harmonie autour de toi.

## Ton defi
La facilite peut mener a la complaisance ou a eviter l'effort.

## Conseil pratique
Cultive ce que tu as recu. Le charme naturel se developpe aussi.""",

    ('uranus', 'venus'): """# \u25b3 Trigone Uranus - Venus
**En une phrase :** Une capacite naturelle a vivre des relations libres et une creativite originale.

## L'energie de cet aspect
Le trigone Uranus-Venus harmonise amour et liberte. Cette configuration donne une originalite relationnelle et un talent artistique unique.

## Ton potentiel
Tu crees des relations qui respectent l'independance et tu exprimes une beaute originale.

## Ton defi
L'aisance avec la liberte peut eviter l'engagement profond.

## Conseil pratique
L'engagement et la liberte ne s'excluent pas. Cree tes propres regles relationnelles.""",
}

async def insert_interpretations():
    """Insere les interpretations trigone part 3 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in TRINE_PART3.items():
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
