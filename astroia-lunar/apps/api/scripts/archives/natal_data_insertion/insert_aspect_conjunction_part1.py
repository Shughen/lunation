#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects conjonction (part 1/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

# Pairs 1-15: jupiter-mars to mars-venus
CONJUNCTION_PART1 = {
    ('jupiter', 'mars'): """# \u260c Conjonction Jupiter - Mars
**En une phrase :** Une energie d'action expansive qui pousse a entreprendre grand et a prendre des risques calcules.

## L'energie de cet aspect
La conjonction Jupiter-Mars fusionne l'expansion jupiterienne avec l'energie martienne. Cette combinaison cree un moteur puissant pour l'action. Tu possedes une capacite naturelle a te lancer dans des projets ambitieux avec enthousiasme et determination.

## Ton potentiel
Tu excelles a transformer les idees en actions concretes. Ta confiance en toi inspire les autres a te suivre. Les defis te motivent plutot que de te freiner.

## Ton defi
Le piege est de surestimer tes capacites ou de t'engager dans trop de projets simultanement. L'impatience peut te pousser a bruler les etapes.

## Conseil pratique
Canalise cette energie dans des projets qui ont du sens pour toi. Prends le temps d'evaluer les risques avant de foncer.""",

    ('jupiter', 'mercury'): """# \u260c Conjonction Jupiter - Mercure
**En une phrase :** Un esprit curieux et optimiste qui voit toujours la vue d'ensemble et communique avec enthousiasme.

## L'energie de cet aspect
La conjonction Jupiter-Mercure amplifie les facultes mentales. Cette configuration donne un esprit synthetique capable de relier des idees disparates. Tu as un talent naturel pour l'enseignement et la transmission des connaissances.

## Ton potentiel
Tu sais vulgariser des concepts complexes et inspirer par ta vision. Les echanges intellectuels te stimulent et t'enrichissent.

## Ton defi
Attention a ne pas tomber dans l'exageration ou les promesses impossibles. Le surplus d'idees peut disperser ton energie mentale.

## Conseil pratique
Ancre tes grandes idees dans des plans d'action concrets. Ecoute autant que tu parles.""",

    ('jupiter', 'moon'): """# \u260c Conjonction Jupiter - Lune
**En une phrase :** Une generosite emotionnelle naturelle qui nourrit les autres et attire l'abondance affective.

## L'energie de cet aspect
La conjonction Jupiter-Lune amplifie la sensibilite emotionnelle de facon positive. Cette configuration cree une capacite naturelle a faire confiance a la vie et a tes intuitions. Tu as un don pour creer des espaces accueillants.

## Ton potentiel
Ta chaleur emotionnelle attire les gens vers toi. Tu sais instinctivement ce dont les autres ont besoin pour se sentir bien.

## Ton defi
Le risque est de trop donner ou d'attendre trop des relations. Les exces emotionnels peuvent t'epuiser.

## Conseil pratique
Etablis des limites saines dans tes relations. Nourris-toi emotionnellement avant de nourrir les autres.""",

    ('jupiter', 'neptune'): """# \u260c Conjonction Jupiter - Neptune
**En une phrase :** Une connexion spirituelle profonde qui inspire la compassion universelle et les ideaux eleves.

## L'energie de cet aspect
La conjonction Jupiter-Neptune amplifie la dimension mystique et creative. Cette configuration ouvre les portes de l'imaginaire et de la spiritualite. Tu possedes une sensibilite artistique et une foi profonde en quelque chose de plus grand.

## Ton potentiel
Tu inspires les autres par ta vision idealisee du monde. Ton imagination est une source inepuisable de creativite.

## Ton defi
Le piege est de fuir la realite dans l'illusion ou de te perdre dans des utopies irrealisables.

## Conseil pratique
Ancre tes inspirations dans des actions concretes. Developpe ton discernement face aux illusions.""",

    ('jupiter', 'pluto'): """# \u260c Conjonction Jupiter - Pluton
**En une phrase :** Un pouvoir de transformation intense qui permet d'accomplir des changements majeurs.

## L'energie de cet aspect
La conjonction Jupiter-Pluton fusionne expansion et transformation profonde. Cette configuration donne une capacite a regenerer et a reconstruire sur de nouvelles bases. Tu possedes une force interieure considerable.

## Ton potentiel
Tu sais transformer les crises en opportunites de croissance. Ta determination te permet d'atteindre des objectifs que d'autres jugent impossibles.

## Ton defi
Le risque est d'abuser du pouvoir ou de vouloir tout controler. L'obsession peut devenir destructrice.

## Conseil pratique
Utilise ton influence pour servir le bien commun. Accepte ce qui echappe a ton controle.""",

    ('jupiter', 'saturn'): """# \u260c Conjonction Jupiter - Saturne
**En une phrase :** Un equilibre rare entre expansion et structure qui permet de construire durablement.

## L'energie de cet aspect
La conjonction Jupiter-Saturne marie l'optimisme a la prudence. Cette configuration permet de concretiser les grands projets avec methode et patience. Tu sais quand accelerer et quand consolider.

## Ton potentiel
Tu excelles a planifier sur le long terme et a construire des fondations solides pour tes ambitions.

## Ton defi
La tension entre croissance et restriction peut creer des periodes d'hesitation ou de frustration.

## Conseil pratique
Alterne les phases d'expansion et de consolidation. Fais confiance au timing naturel des choses.""",

    ('jupiter', 'sun'): """# \u260c Conjonction Jupiter - Soleil
**En une phrase :** Une personnalite rayonnante et optimiste qui inspire naturellement confiance et admiration.

## L'energie de cet aspect
La conjonction Jupiter-Soleil amplifie l'identite et la vitalite. Cette configuration donne une presence naturellement charismatique et une vision positive de la vie. Tu attires les opportunites par ton rayonnement.

## Ton potentiel
Tu inspires les autres par ta confiance et ton enthousiasme. Les portes s'ouvrent naturellement devant toi.

## Ton defi
L'exces de confiance peut mener a l'arrogance ou a sous-estimer les difficultes.

## Conseil pratique
Reste humble malgre tes succes. Utilise ton influence pour elever les autres.""",

    ('jupiter', 'uranus'): """# \u260c Conjonction Jupiter - Uranus
**En une phrase :** Un esprit revolutionnaire qui cherche a etendre les horizons par l'innovation et la liberte.

## L'energie de cet aspect
La conjonction Jupiter-Uranus fusionne expansion et originalite. Cette configuration produit une soif de liberte et d'experiences nouvelles. Tu es attire par tout ce qui sort de l'ordinaire.

## Ton potentiel
Tu sais percevoir les tendances futures et innover de facon visionnaire. L'inattendu te stimule.

## Ton defi
L'instabilite et l'impatience peuvent te faire abandonner des projets prometteurs trop tot.

## Conseil pratique
Canalise ton besoin de changement dans des innovations constructives. Accepte certaines structures comme support a ta liberte.""",

    ('jupiter', 'venus'): """# \u260c Conjonction Jupiter - Venus
**En une phrase :** Une grace naturelle et un sens de l'harmonie qui attirent l'amour et l'abondance.

## L'energie de cet aspect
La conjonction Jupiter-Venus amplifie l'amour et la beaute. Cette configuration donne un charme naturel et un talent pour les arts. Tu sais apprecier et creer la beaute autour de toi.

## Ton potentiel
Tu attires l'amour et les relations harmonieuses. Ton sens esthetique est developpe et apprecie.

## Ton defi
L'exces de gourmandise ou de dependance aux plaisirs peut devenir problematique.

## Conseil pratique
Cultive la moderation dans les plaisirs. Partage ton appreciation de la beaute avec les autres.""",

    ('mars', 'mercury'): """# \u260c Conjonction Mars - Mercure
**En une phrase :** Un esprit vif et combatif qui pense vite et s'exprime avec force.

## L'energie de cet aspect
La conjonction Mars-Mercure accelere les processus mentaux. Cette configuration donne une pensee rapide et un esprit de repartie. Tu sais argumenter et defendre tes idees avec vigueur.

## Ton potentiel
Tu excelles dans les debats et les situations qui demandent des decisions rapides. Ta communication est directe et efficace.

## Ton defi
L'impatience intellectuelle peut te rendre cassant ou agressif dans les echanges.

## Conseil pratique
Prends le temps d'ecouter avant de reagir. Transforme ton energie mentale en actions constructives.""",

    ('mars', 'moon'): """# \u260c Conjonction Mars - Lune
**En une phrase :** Des emotions intenses qui se transforment rapidement en action et reaction.

## L'energie de cet aspect
La conjonction Mars-Lune fusionne l'instinct emotionnel et l'energie d'action. Cette configuration cree des reactions emotionnelles rapides et intenses. Tu ressens les choses profondement et reponds immediatement.

## Ton potentiel
Tu as la capacite de proteger ceux que tu aimes avec ferosite. Ton courage emotionnel est remarquable.

## Ton defi
Les reactions impulsives basees sur les emotions peuvent creer des conflits inutiles.

## Conseil pratique
Cree un espace entre le ressenti et l'action. Canalise l'intensite emotionnelle dans des activites physiques.""",

    ('mars', 'neptune'): """# \u260c Conjonction Mars - Neptune
**En une phrase :** Une energie d'action inspiree qui se met au service d'ideaux ou de visions artistiques.

## L'energie de cet aspect
La conjonction Mars-Neptune mele action et inspiration. Cette configuration peut creer soit une energie creative exceptionnelle, soit une confusion entre desir et realite. Tu es motive par des ideaux plutot que par des interets personnels.

## Ton potentiel
Tu sais te battre pour des causes qui depassent ta personne. Ta creativite peut s'exprimer avec passion.

## Ton defi
La difficulte a agir de facon directe peut mener a la passivite ou aux strategies indirectes.

## Conseil pratique
Clarifie tes motivations avant d'agir. Trouve des canaux concrets pour exprimer ton inspiration.""",

    ('mars', 'pluto'): """# \u260c Conjonction Mars - Pluton
**En une phrase :** Une volonte de fer et une capacite de regeneration qui permettent de surmonter tous les obstacles.

## L'energie de cet aspect
La conjonction Mars-Pluton concentre une puissance considerable. Cette configuration donne une determination inflexible et une capacite a transformer radicalement les situations. Tu ne recules devant rien.

## Ton potentiel
Tu possedes une endurance et une resilience exceptionnelles. Tu sais renaitre de tes cendres.

## Ton defi
L'intensite peut devenir destructrice si elle n'est pas canalisee. Le controle excessif blesse les relations.

## Conseil pratique
Choisis tes combats avec sagesse. Utilise ta puissance pour construire plutot que detruire.""",

    ('mars', 'saturn'): """# \u260c Conjonction Mars - Saturne
**En une phrase :** Une energie disciplinee et endurant qui construit avec methode et perseverance.

## L'energie de cet aspect
La conjonction Mars-Saturne cree une action structuree. Cette configuration demande d'apprendre a canaliser l'energie dans des efforts soutenus. Tu excelles dans les projets qui demandent de la discipline.

## Ton potentiel
Tu sais perseverer quand les autres abandonnent. Ta capacite de travail est impressionnante.

## Ton defi
La frustration peut s'accumuler quand l'action est bloquee. La rigidite peut empecher l'adaptation.

## Conseil pratique
Alterne effort et recuperation. Celebre les progres incrementaux.""",

    ('mars', 'sun'): """# \u260c Conjonction Mars - Soleil
**En une phrase :** Une vitalite ardente et une volonte affirmee qui ne reculent pas devant les defis.

## L'energie de cet aspect
La conjonction Mars-Soleil fusionne identite et energie d'action. Cette configuration donne une personnalite dynamique et competitive. Tu as besoin de te depasser et de prouver ta valeur.

## Ton potentiel
Tu possedes un courage naturel et une capacite d'initiative remarquable. Tu inspires par ton exemple.

## Ton defi
L'ego peut devenir trop combatif ou dominateur. L'impatience freine parfois les resultats.

## Conseil pratique
Canalise ton energie dans des defis constructifs. Apprends a collaborer autant qu'a competitionner.""",
}

async def insert_interpretations():
    """Insere les interpretations conjonction part 1 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in CONJUNCTION_PART1.items():
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
