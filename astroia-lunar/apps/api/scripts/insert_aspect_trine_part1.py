#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects trigone (part 1/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

TRINE_PART1 = {
    ('jupiter', 'mars'): """# \u25b3 Trigone Jupiter - Mars
**En une phrase :** Une energie fluide qui allie vision et action avec enthousiasme naturel.

## L'energie de cet aspect
Le trigone Jupiter-Mars cree une harmonie entre expansion et energie. Cette configuration donne une capacite naturelle a agir avec confiance et a saisir les opportunites.

## Ton potentiel
Tu entreprends avec optimisme et reussis souvent grace a ton enthousiasme communicatif.

## Ton defi
La facilite peut mener a un manque d'effort ou a sous-estimer les obstacles.

## Conseil pratique
Utilise cette aisance comme tremplin, pas comme acquis. L'effort amplifie le talent.""",

    ('jupiter', 'mercury'): """# \u25b3 Trigone Jupiter - Mercure
**En une phrase :** Un esprit naturellement synthetique qui comprend et communique les grandes idees avec facilite.

## L'energie de cet aspect
Le trigone Jupiter-Mercure harmonise la pensee et l'expansion. Cette configuration donne un optimisme intellectuel et une facilite a apprendre.

## Ton potentiel
Tu saisis rapidement les concepts et tu sais les transmettre de facon inspirante.

## Ton defi
La facilite intellectuelle peut mener a la superficialite ou a l'arrogance.

## Conseil pratique
Approfondie tes connaissances. La facilite est un don, la maitrise demande du travail.""",

    ('jupiter', 'moon'): """# \u25b3 Trigone Jupiter - Lune
**En une phrase :** Une generosite emotionnelle naturelle qui nourrit et inspire confiance.

## L'energie de cet aspect
Le trigone Jupiter-Lune harmonise les emotions et l'expansion. Cette configuration donne une foi naturelle en la vie et une capacite a soutenir les autres.

## Ton potentiel
Tu crees des espaces emotionnellement securisants et inspirants pour les autres.

## Ton defi
L'exces de confiance emotionnelle peut mener a la naivete.

## Conseil pratique
Garde cette confiance tout en developpant ton discernement emotionnel.""",

    ('jupiter', 'neptune'): """# \u25b3 Trigone Jupiter - Neptune
**En une phrase :** Une connexion spirituelle naturelle qui inspire et eleve vers des ideaux.

## L'energie de cet aspect
Le trigone Jupiter-Neptune harmonise foi et intuition. Cette configuration donne une inspiration naturelle et une capacite a percevoir le sens profond des choses.

## Ton potentiel
Tu inspires les autres par ta vision spirituelle et ta compassion naturelle.

## Ton defi
La facilite spirituelle peut mener a l'indolence ou a eviter les efforts concrets.

## Conseil pratique
Ancre tes inspirations dans des actions. La spiritualite se vit dans le quotidien.""",

    ('jupiter', 'pluto'): """# \u25b3 Trigone Jupiter - Pluton
**En une phrase :** Un pouvoir de transformation positif qui permet de regenerer et de rebondir.

## L'energie de cet aspect
Le trigone Jupiter-Pluton harmonise expansion et transformation. Cette configuration donne une resilience naturelle et une capacite a tirer parti des crises.

## Ton potentiel
Tu transformes les epreuves en opportunites de croissance avec une apparente facilite.

## Ton defi
L'aisance dans la transformation peut mener a chercher les crises inutilement.

## Conseil pratique
Utilise ce don pour aider les autres a traverser leurs crises.""",

    ('jupiter', 'saturn'): """# \u25b3 Trigone Jupiter - Saturne
**En une phrase :** Un equilibre naturel entre optimisme et realisme qui permet de construire durablement.

## L'energie de cet aspect
Le trigone Jupiter-Saturne harmonise expansion et structure. Cette configuration donne une sagesse pratique et une capacite a concretiser les ambitions.

## Ton potentiel
Tu sais quand avancer et quand consolider. Tes projets tiennent dans le temps.

## Ton defi
L'equilibre naturel peut manquer de passion ou d'audace.

## Conseil pratique
Ose des projets plus audacieux. Tu as les ressources pour les realiser.""",

    ('jupiter', 'sun'): """# \u25b3 Trigone Jupiter - Soleil
**En une phrase :** Une confiance naturelle et un optimisme qui attirent les opportunites.

## L'energie de cet aspect
Le trigone Jupiter-Soleil harmonise l'identite et l'expansion. Cette configuration donne un charisme naturel et une foi en soi communicative.

## Ton potentiel
Tu inspires confiance et tu attires les bonnes opportunites sans forcer.

## Ton defi
La facilite peut mener a l'arrogance ou au manque d'effort.

## Conseil pratique
Partage ta chance. L'abondance se multiplie quand elle circule.""",

    ('jupiter', 'uranus'): """# \u25b3 Trigone Jupiter - Uranus
**En une phrase :** Une ouverture naturelle a l'innovation qui cree des opportunites inattendues.

## L'energie de cet aspect
Le trigone Jupiter-Uranus harmonise expansion et originalite. Cette configuration donne une chance avec les changements soudains et l'innovation.

## Ton potentiel
Tu sais saisir les opportunites liees aux changements et innover avec succes.

## Ton defi
La facilite avec le changement peut mener a l'instabilite volontaire.

## Conseil pratique
Canalise cette energie dans des innovations constructives et durables.""",

    ('jupiter', 'venus'): """# \u25b3 Trigone Jupiter - Venus
**En une phrase :** Une grace naturelle qui attire l'amour, la beaute et l'abondance.

## L'energie de cet aspect
Le trigone Jupiter-Venus harmonise expansion et harmonie. Cette configuration donne un charme naturel et une appreciation de la beaute.

## Ton potentiel
Tu attires l'amour et les bonnes choses de la vie avec une apparente facilite.

## Ton defi
L'exces de facilite peut mener a la complaisance ou aux exces.

## Conseil pratique
Cultive la gratitude et partage ton abondance. La generosite amplifie la grace.""",

    ('mars', 'mercury'): """# \u25b3 Trigone Mars - Mercure
**En une phrase :** Un esprit vif qui transforme rapidement les idees en actions.

## L'energie de cet aspect
Le trigone Mars-Mercure harmonise pensee et action. Cette configuration donne une facilite a decider et a communiquer avec clarte.

## Ton potentiel
Tu sais convaincre et agir rapidement sur tes idees.

## Ton defi
La rapidite peut mener a des decisions insuffisamment reflechies.

## Conseil pratique
Prends le temps de la reflexion meme si tu peux agir vite.""",

    ('mars', 'moon'): """# \u25b3 Trigone Mars - Lune
**En une phrase :** Des emotions qui se transforment naturellement en actions protectrices.

## L'energie de cet aspect
Le trigone Mars-Lune harmonise instinct et action. Cette configuration donne une capacite a agir selon ses intuitions avec justesse.

## Ton potentiel
Tu proteges ceux que tu aimes avec courage et sensibilite.

## Ton defi
L'aisance dans les reactions emotionnelles peut manquer de nuance.

## Conseil pratique
Affine tes reactions. Le courage peut etre doux autant que fort.""",

    ('mars', 'neptune'): """# \u25b3 Trigone Mars - Neptune
**En une phrase :** Une action inspiree qui se met naturellement au service d'ideaux.

## L'energie de cet aspect
Le trigone Mars-Neptune harmonise action et inspiration. Cette configuration donne une capacite a agir pour des causes qui depassent l'ego.

## Ton potentiel
Tu te bats naturellement pour des causes justes avec grace et efficacite.

## Ton defi
L'idealisation de l'action peut eloigner du concret.

## Conseil pratique
Ancre ton inspiration dans des actions mesurables. L'ideal se realise pas a pas.""",

    ('mars', 'pluto'): """# \u25b3 Trigone Mars - Pluton
**En une phrase :** Une force interieure puissante qui permet de surmonter les obstacles avec determination.

## L'energie de cet aspect
Le trigone Mars-Pluton harmonise volonte et pouvoir. Cette configuration donne une endurance et une capacite de regeneration remarquables.

## Ton potentiel
Tu traverses les crises avec force et tu en ressors plus fort.

## Ton defi
La facilite avec le pouvoir peut mener a l'intimidation involontaire.

## Conseil pratique
Utilise ta force pour proteger et construire, pas pour dominer.""",

    ('mars', 'saturn'): """# \u25b3 Trigone Mars - Saturne
**En une phrase :** Une energie disciplinee qui accomplit methodiquement des objectifs ambitieux.

## L'energie de cet aspect
Le trigone Mars-Saturne harmonise action et structure. Cette configuration donne une endurance et une capacite a travailler dur avec constance.

## Ton potentiel
Tu atteins tes objectifs par un effort soutenu et organise.

## Ton defi
L'aisance dans l'effort peut manquer de spontaneite ou de plaisir.

## Conseil pratique
Integre du plaisir dans ton effort. La discipline joyeuse est plus durable.""",

    ('mars', 'sun'): """# \u25b3 Trigone Mars - Soleil
**En une phrase :** Une vitalite naturelle qui s'exprime par l'action et l'initiative.

## L'energie de cet aspect
Le trigone Mars-Soleil harmonise identite et energie. Cette configuration donne une confiance naturelle dans l'action et le leadership.

## Ton potentiel
Tu agis naturellement en accord avec qui tu es, ce qui inspire les autres.

## Ton defi
L'aisance dans l'action peut mener a l'impatience envers ceux qui sont plus lents.

## Conseil pratique
Adapte ton rythme aux autres. Le vrai leader aide chacun a avancer.""",
}

async def insert_interpretations():
    """Insere les interpretations trigone part 1 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in TRINE_PART1.items():
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
