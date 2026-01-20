#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects conjonction (part 3/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

# Pairs 31-45: neptune-pluto to uranus-venus
CONJUNCTION_PART3 = {
    ('neptune', 'pluto'): """# \u260c Conjonction Neptune - Pluton
**En une phrase :** Une transformation spirituelle generationnelle qui influence les courants collectifs profonds.

## L'energie de cet aspect
La conjonction Neptune-Pluton est un aspect generationnel rare qui marque des periodes de transformation spirituelle collective. A l'echelle personnelle, elle donne une sensibilite aux mouvements profonds de l'humanite.

## Ton potentiel
Tu es connecte aux courants evolutifs de ton epoque et tu peux y contribuer de facon significative.

## Ton defi
La sensation d'etre submerge par des forces plus grandes que soi peut creer de l'impuissance.

## Conseil pratique
Trouve ta contribution unique aux transformations collectives. Agis localement, pense globalement.""",

    ('neptune', 'saturn'): """# \u260c Conjonction Neptune - Saturne
**En une phrase :** Une tension entre l'ideal et le reel qui demande de materialiser les reves.

## L'energie de cet aspect
La conjonction Neptune-Saturne confronte la structure a la dissolution. Cette configuration demande d'ancrer les visions dans la realite concrete. Tu oscilles entre pragmatisme et idealisime.

## Ton potentiel
Tu sais donner forme aux reves et construire des ponts entre le visible et l'invisible.

## Ton defi
La deception face a la realite et la rigidite dans les croyances sont des pieges.

## Conseil pratique
Accepte que les ideaux se concretisent imparfaitement. La structure peut servir l'inspiration.""",

    ('neptune', 'sun'): """# \u260c Conjonction Neptune - Soleil
**En une phrase :** Une identite poreuse et sensible qui peut se perdre ou se transcender dans quelque chose de plus grand.

## L'energie de cet aspect
La conjonction Neptune-Soleil dissout les contours de l'ego. Cette configuration donne une sensibilite artistique ou spirituelle et une difficulte a definir clairement son identite.

## Ton potentiel
Tu possedes une creativite et une compassion exceptionnelles. Tu peux inspirer par ta vision.

## Ton defi
La perte d'identite dans les illusions ou les dependances est un risque.

## Conseil pratique
Definis-toi par tes creations et tes valeurs. Reste ancre tout en restant ouvert au transcendant.""",

    ('neptune', 'uranus'): """# \u260c Conjonction Neptune - Uranus
**En une phrase :** Une intuition visionnaire qui percoit les possibilites revolutionnaires pour l'humanite.

## L'energie de cet aspect
La conjonction Neptune-Uranus est generationnelle et marque des epoques d'innovation spirituelle et technologique. Tu es sensible aux ideaux progressistes de ta generation.

## Ton potentiel
Tu combines intuition et innovation pour imaginer des futurs differents.

## Ton defi
L'utopisme peut te deconnecter des realites pratiques.

## Conseil pratique
Ancre tes visions dans des actions concretes. L'innovation doit servir l'humanite.""",

    ('neptune', 'venus'): """# \u260c Conjonction Neptune - Venus
**En une phrase :** Un amour idealisé et une sensibilite artistique qui cherche la beaute transcendante.

## L'energie de cet aspect
La conjonction Neptune-Venus eleve l'amour et la beaute vers des dimensions ideales. Cette configuration donne un romantisme profond et un talent artistique raffine. Tu cherches l'amour parfait.

## Ton potentiel
Tu possedes une sensibilite esthetique rare et une capacite a creer ou apprecier la beaute subtile.

## Ton defi
Les illusions amoureuses et la deception dans les relations sont frequentes.

## Conseil pratique
Accepte l'imperfection dans l'amour reel. Canalise l'ideal dans la creation artistique.""",

    ('pluto', 'saturn'): """# \u260c Conjonction Pluton - Saturne
**En une phrase :** Une volonte de fer qui transforme les structures et reconstruit sur des bases profondes.

## L'energie de cet aspect
La conjonction Pluton-Saturne concentre pouvoir et structure. Cette configuration donne une capacite a entreprendre des transformations durables et profondes. Tu ne fais pas les choses a moitie.

## Ton potentiel
Tu excelles a reconstruire ce qui doit etre change. Ta perseverance est extraordinaire.

## Ton defi
La rigidite et l'obsession du controle peuvent devenir tyranniques.

## Conseil pratique
Utilise ton pouvoir pour liberer plutot que pour contraindre. Accepte le changement comme allie.""",

    ('pluto', 'sun'): """# \u260c Conjonction Pluton - Soleil
**En une phrase :** Une identite intense et transformatrice qui exerce un magnetisme puissant.

## L'energie de cet aspect
La conjonction Pluton-Soleil intensifie l'ego et le pouvoir personnel. Cette configuration donne une presence marquante et une capacite a se regenerer completement. Tu vis les transformations identitaires comme des renaissances.

## Ton potentiel
Tu possedes un charisme puissant et une capacite a transformer les situations par ta seule presence.

## Ton defi
Les luttes de pouvoir et l'intimidation peuvent alienner les autres.

## Conseil pratique
Mets ton pouvoir au service d'une cause plus grande. La vraie force n'a pas besoin de dominer.""",

    ('pluto', 'uranus'): """# \u260c Conjonction Pluton - Uranus
**En une phrase :** Une force revolutionnaire qui transforme radicalement les structures obsoletes.

## L'energie de cet aspect
La conjonction Pluton-Uranus est generationnelle et marque des epoques de bouleversements majeurs. A l'echelle personnelle, elle donne un besoin de changements radicaux et une intolerance envers l'inauthenthique.

## Ton potentiel
Tu es un agent de transformation profonde dans les domaines ou tu t'impliques.

## Ton defi
L'impatience face au changement peut te rendre destructeur plutot que transformateur.

## Conseil pratique
Choisis tes combats. Transforme en profondeur plutot qu'en surface.""",

    ('pluto', 'venus'): """# \u260c Conjonction Pluton - Venus
**En une phrase :** Des passions intenses et transformatrices qui vivent l'amour comme une experience totale.

## L'energie de cet aspect
La conjonction Pluton-Venus intensifie l'amour et les valeurs. Cette configuration donne des attractions puissantes et des relations transformatrices. Tu ne peux pas aimer superficiellement.

## Ton potentiel
Tu possedes un magnetisme seducteur puissant et une capacite a vivre des amours profondes.

## Ton defi
La jalousie, la possessivite et les jeux de pouvoir peuvent empoisonner les relations.

## Conseil pratique
Transforme la passion en intimite profonde. Laisse l'autre libre tout en restant engage.""",

    ('saturn', 'sun'): """# \u260c Conjonction Saturne - Soleil
**En une phrase :** Une identite responsable et mature qui construit sa valeur par l'effort et la perseverance.

## L'energie de cet aspect
La conjonction Saturne-Soleil structure l'identite par l'effort. Cette configuration demande de construire la confiance en soi par les accomplissements concrets. Tu as appris tot que rien n'est gratuit.

## Ton potentiel
Tu developpes une maturite et une fiabilite qui inspirent le respect. Tes accomplissements durent.

## Ton defi
Le pessimisme et le doute de soi peuvent freiner l'epanouissement.

## Conseil pratique
Celebre tes accomplissements. La reconnaissance peut venir de l'interieur autant que de l'exterieur.""",

    ('saturn', 'uranus'): """# \u260c Conjonction Saturne - Uranus
**En une phrase :** Une tension creative entre tradition et innovation qui reconstruit les structures avec originalite.

## L'energie de cet aspect
La conjonction Saturne-Uranus confronte le nouveau et l'ancien. Cette configuration demande d'innover tout en construisant du durable. Tu cherches a reformer plutot qu'a detruire.

## Ton potentiel
Tu sais integrer l'innovation dans les structures existantes de facon realiste.

## Ton defi
L'oscillation entre conservatisme et rebellion peut creer des incoherences.

## Conseil pratique
Trouve l'equilibre entre stabilite et changement. L'innovation durable respecte certaines bases.""",

    ('saturn', 'venus'): """# \u260c Conjonction Saturne - Venus
**En une phrase :** Un amour serieux et durable qui construit des relations solides avec le temps.

## L'energie de cet aspect
La conjonction Saturne-Venus structure les relations et les valeurs. Cette configuration donne un besoin de securite affective et une capacite a s'engager durablement. Tu prends l'amour au serieux.

## Ton potentiel
Tu construis des relations fiables et durables. Ton sens des valeurs est solide.

## Ton defi
La peur de l'abandon et la froideur apparente peuvent creer de la distance.

## Conseil pratique
Ose exprimer ta tendresse. La vulnerabilite dans l'amour construit l'intimite.""",

    ('sun', 'uranus'): """# \u260c Conjonction Soleil - Uranus
**En une phrase :** Une identite originale et independante qui refuse de se conformer aux attentes.

## L'energie de cet aspect
La conjonction Soleil-Uranus electrifie l'identite. Cette configuration donne un besoin vital d'authenticite et de liberte. Tu ne peux pas pretendre etre ce que tu n'es pas.

## Ton potentiel
Tu inspires les autres par ton originalite et ton courage d'etre different.

## Ton defi
L'instabilite identitaire et le refus de tout engagement peuvent isoler.

## Conseil pratique
Trouve des communautes qui celebrent ta difference. L'independance n'exclut pas les liens.""",

    ('sun', 'venus'): """# \u260c Conjonction Soleil - Venus
**En une phrase :** Une personnalite charmante et harmonieuse qui attire naturellement l'amour et l'appreciation.

## L'energie de cet aspect
La conjonction Soleil-Venus fusionne l'identite et les valeurs relationnelles. Cette configuration donne un charme naturel et un besoin d'harmonie. Tu te definis en partie par tes relations et tes gouts esthetiques.

## Ton potentiel
Tu possedes un magnetisme agreable et une capacite a creer de la beaute autour de toi.

## Ton defi
La dependance aux autres pour la valorisation peut fragiliser l'estime de soi.

## Conseil pratique
Cultive une appreciation de toi-meme independante des autres. Ta valeur est inherente.""",

    ('uranus', 'venus'): """# \u260c Conjonction Uranus - Venus
**En une phrase :** Un amour libre et non conventionnel qui refuse les schemas relationnels traditionnels.

## L'energie de cet aspect
La conjonction Uranus-Venus electrifie l'amour et les valeurs. Cette configuration donne un besoin d'excitation et de liberte dans les relations. Tu es attire par l'inhabituel.

## Ton potentiel
Tu explores des formes d'amour originales et tu liberes les autres de leurs conditionnements affectifs.

## Ton defi
L'instabilite relationnelle et la peur de l'engagement peuvent empecher l'intimite profonde.

## Conseil pratique
Trouve des partenaires qui partagent ton besoin de liberte. L'engagement peut etre creatif.""",
}

async def insert_interpretations():
    """Insere les interpretations conjonction part 3 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in CONJUNCTION_PART3.items():
            result = await db.execute(
                select(PregeneratedNatalAspect).where(
                    PregeneratedNatalAspect.planet1 == planet1,
                    PregeneratedNatalAspect.planet2 == planet2,
                    PregeneratedNatalAspect.aspect_type == 'conjunction',
                    PregeneratedNatalAspect.version == 2,
                    PregeneratedNatalAspect.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP {planet1}-{planet2} conjunction")
                skipped += 1
                continue

            interp = PregeneratedNatalAspect(
                planet1=planet1,
                planet2=planet2,
                aspect_type='conjunction',
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"INSERT {planet1}-{planet2} conjunction ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nResultat: {inserted} inserees, {skipped} ignorees")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
