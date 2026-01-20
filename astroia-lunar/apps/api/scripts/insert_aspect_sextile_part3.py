#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects sextile (part 3/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

SEXTILE_PART3 = {
    ('neptune', 'pluto'): """# \u26b9 Sextile Neptune - Pluton
**En une phrase :** Un aspect generationnel qui offre des opportunites de transformation spirituelle collective.

## L'energie de cet aspect
Le sextile Neptune-Pluton est generationnel et dure des decennies. Il cree une opportunite de synergie entre intuition spirituelle et transformation profonde au niveau collectif.

## Ton potentiel
Tu participes a des mouvements de conscience qui transforment la societe.

## Ton defi
L'aspect generationnel demande de trouver comment l'incarner personnellement.

## Conseil pratique
Contribue aux transformations spirituelles de ton epoque a ton echelle.""",

    ('neptune', 'saturn'): """# \u26b9 Sextile Neptune - Saturne
**En une phrase :** Une opportunite de materialiser les reves qui recompense l'effort inspire.

## L'energie de cet aspect
Le sextile Neptune-Saturne offre une facilite pour donner forme aux visions. Cette configuration favorise la realisation pratique des inspirations.

## Ton potentiel
Tu peux construire des ponts entre l'ideal et le reel avec succes.

## Ton defi
La facilite demande quand meme un effort pour concretiser les reves.

## Conseil pratique
Travaille tes visions. L'inspiration se realise par l'action disciplinee.""",

    ('neptune', 'sun'): """# \u26b9 Sextile Neptune - Soleil
**En une phrase :** Une opportunite de creativite spirituelle qui recompense l'expression inspiree.

## L'energie de cet aspect
Le sextile Neptune-Soleil offre une facilite pour l'expression creative et spirituelle. Cette configuration favorise le charisme inspire et la connexion au transcendant.

## Ton potentiel
Tu peux developper une presence inspirante qui eleve les autres.

## Ton defi
Le talent spirituel demande d'etre cultive par la pratique creative.

## Conseil pratique
Exprime ta vision a travers l'art ou le service. L'inspiration partagee grandit.""",

    ('neptune', 'uranus'): """# \u26b9 Sextile Neptune - Uranus
**En une phrase :** Un aspect generationnel qui offre des opportunites d'innovation spirituelle.

## L'energie de cet aspect
Le sextile Neptune-Uranus est generationnel et cree une opportunite de synergie entre intuition et innovation au niveau collectif.

## Ton potentiel
Tu combines naturellement vision spirituelle et pensee novatrice.

## Ton defi
L'aspect generationnel demande une incarnation personnelle pour etre actif.

## Conseil pratique
Innove dans les domaines de l'ame. La spiritualite peut etre avant-gardiste.""",

    ('neptune', 'venus'): """# \u26b9 Sextile Neptune - Venus
**En une phrase :** Une opportunite d'amour spirituel qui recompense l'ouverture du coeur a l'ideal.

## L'energie de cet aspect
Le sextile Neptune-Venus offre une facilite pour l'amour inconditionnel et la beaute transcendante. Cette configuration favorise l'expression artistique et les relations aimantes.

## Ton potentiel
Tu peux developper un amour qui eleve et une creativite qui inspire.

## Ton defi
La grace amoureuse demande d'etre partagee pour s'epanouir.

## Conseil pratique
Aime sans conditions. Cree de la beaute qui nourrit l'ame.""",

    ('pluto', 'saturn'): """# \u26b9 Sextile Pluton - Saturne
**En une phrase :** Une opportunite de transformation structuree qui recompense la perseverance dans le changement.

## L'energie de cet aspect
Le sextile Pluton-Saturne offre une facilite pour les reformes profondes et durables. Cette configuration favorise la reconstruction methodique.

## Ton potentiel
Tu peux transformer les structures avec patience et efficacite.

## Ton defi
La transformation structuree demande un engagement soutenu.

## Conseil pratique
Engage-toi dans les changements a long terme. La transformation durable prend du temps.""",

    ('pluto', 'sun'): """# \u26b9 Sextile Pluton - Soleil
**En une phrase :** Une opportunite de regeneration identitaire qui recompense l'authenticite profonde.

## L'energie de cet aspect
Le sextile Pluton-Soleil offre une facilite pour la transformation personnelle. Cette configuration favorise le charisme et la capacite de renouvellement.

## Ton potentiel
Tu peux te reinventer et inspirer les autres par ta force interieure.

## Ton defi
Le potentiel de transformation demande d'accepter de changer.

## Conseil pratique
Embrasse les transformations necessaires. La renaissance construit le charisme.""",

    ('pluto', 'uranus'): """# \u26b9 Sextile Pluton - Uranus
**En une phrase :** Un aspect generationnel qui offre des opportunites de changement revolutionnaire constructif.

## L'energie de cet aspect
Le sextile Pluton-Uranus est generationnel et cree une opportunite de synergie entre transformation profonde et innovation au niveau collectif.

## Ton potentiel
Tu participes naturellement aux evolutions majeures de ton epoque.

## Ton defi
L'aspect generationnel demande de trouver ton role personnel dans les changements.

## Conseil pratique
Trouve ta contribution unique aux transformations collectives.""",

    ('pluto', 'venus'): """# \u26b9 Sextile Pluton - Venus
**En une phrase :** Une opportunite d'amour transformateur qui recompense l'intimite profonde.

## L'energie de cet aspect
Le sextile Pluton-Venus offre une facilite pour les relations intenses et transformatrices. Cette configuration favorise la passion creatrice et l'amour profond.

## Ton potentiel
Tu peux vivre des amours qui transforment positivement les deux partenaires.

## Ton defi
La profondeur relationnelle demande d'oser l'intimite veritable.

## Conseil pratique
Ose la vulnerabilite en amour. La transformation vient de l'ouverture.""",

    ('saturn', 'sun'): """# \u26b9 Sextile Saturne - Soleil
**En une phrase :** Une opportunite de maturite qui recompense l'effort personnel.

## L'energie de cet aspect
Le sextile Saturne-Soleil offre une facilite pour construire une identite solide. Cette configuration favorise les accomplissements durables et le respect.

## Ton potentiel
Tu peux developper une autorite naturelle basee sur tes accomplissements.

## Ton defi
La maturite demande un effort soutenu pour se developper.

## Conseil pratique
Investis dans ton developpement a long terme. La reconnaissance vient avec le temps.""",

    ('saturn', 'uranus'): """# \u26b9 Sextile Saturne - Uranus
**En une phrase :** Une opportunite d'innovation structuree qui recompense la reforme pragmatique.

## L'energie de cet aspect
Le sextile Saturne-Uranus offre une facilite pour integrer tradition et innovation. Cette configuration favorise les reformes durables et pratiques.

## Ton potentiel
Tu peux innover de facon qui respecte les fondations et qui dure.

## Ton defi
L'equilibre entre ancien et nouveau demande un effort conscient.

## Conseil pratique
Reforme progressivement. Le changement durable respecte certaines bases.""",

    ('saturn', 'venus'): """# \u26b9 Sextile Saturne - Venus
**En une phrase :** Une opportunite de fidelite qui recompense l'engagement relationnel.

## L'energie de cet aspect
Le sextile Saturne-Venus offre une facilite pour les relations stables et les valeurs durables. Cette configuration favorise la fidelite et l'appreciation de la beaute classique.

## Ton potentiel
Tu peux construire des relations solides et developper un gout raffine.

## Ton defi
La fidelite demande un engagement actif dans la duree.

## Conseil pratique
Investis dans tes relations et tes valeurs. La duree construit la profondeur.""",

    ('sun', 'uranus'): """# \u26b9 Sextile Soleil - Uranus
**En une phrase :** Une opportunite d'originalite qui recompense l'expression authentique de ta difference.

## L'energie de cet aspect
Le sextile Soleil-Uranus offre une facilite pour l'expression originale. Cette configuration favorise l'independance et le charisme unique.

## Ton potentiel
Tu peux developper une identite distincte qui inspire par son authenticite.

## Ton defi
L'originalite demande d'oser etre different visiblement.

## Conseil pratique
Exprime ce qui te rend unique. L'authenticite attire les bonnes personnes.""",

    ('sun', 'venus'): """# \u26b9 Sextile Soleil - Venus
**En une phrase :** Une opportunite de charme qui recompense l'expression agreable de soi.

## L'energie de cet aspect
Le sextile Soleil-Venus offre une facilite pour plaire et creer l'harmonie. Cette configuration favorise les relations agreables et l'expression artistique.

## Ton potentiel
Tu peux developper un charme naturel et une appreciation de la beaute.

## Ton defi
Le charme demande d'etre cultive et partage pour s'epanouir.

## Conseil pratique
Exprime ta douceur. La beaute que tu crees enrichit le monde.""",

    ('uranus', 'venus'): """# \u26b9 Sextile Uranus - Venus
**En une phrase :** Une opportunite de relations innovantes qui recompense l'ouverture relationnelle.

## L'energie de cet aspect
Le sextile Uranus-Venus offre une facilite pour les relations originales et la creativite novatrice. Cette configuration favorise l'amour libre et l'art avant-gardiste.

## Ton potentiel
Tu peux developper des relations qui respectent l'individualite et une expression artistique unique.

## Ton defi
L'originalite relationnelle demande d'oser des formes d'amour non conventionnelles.

## Conseil pratique
Explore les relations qui te correspondent vraiment. L'amour a plusieurs formes.""",
}

async def insert_interpretations():
    """Insere les interpretations sextile part 3 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in SEXTILE_PART3.items():
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
