#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects sextile (part 2/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

SEXTILE_PART2 = {
    ('mars', 'uranus'): """# \u26b9 Sextile Mars - Uranus
**En une phrase :** Une opportunite d'action innovante qui recompense l'audace calculee.

## L'energie de cet aspect
Le sextile Mars-Uranus offre une facilite pour innover dans l'action. Cette configuration favorise les initiatives originales et les reactions rapides aux changements.

## Ton potentiel
Tu peux initier des changements audacieux et t'adapter vite aux situations nouvelles.

## Ton defi
Les opportunites d'innovation demandent d'oser sortir des sentiers battus.

## Conseil pratique
Quand une idee originale t'appelle, agis. L'audace est recompensee.""",

    ('mars', 'venus'): """# \u26b9 Sextile Mars - Venus
**En une phrase :** Une opportunite de creativite relationnelle qui recompense l'initiative en amour.

## L'energie de cet aspect
Le sextile Mars-Venus offre une facilite pour seduire et creer. Cette configuration favorise les initiatives dans les relations et les arts.

## Ton potentiel
Tu peux developper un charme actif et une creativite engagee.

## Ton defi
Les opportunites amoureuses et creatives demandent d'etre saisies.

## Conseil pratique
Fais le premier pas en amour et en creation. L'initiative ouvre des portes.""",

    ('mercury', 'moon'): """# \u26b9 Sextile Mercure - Lune
**En une phrase :** Une opportunite de communication sensible qui recompense l'expression des emotions.

## L'energie de cet aspect
Le sextile Mercure-Lune offre une facilite pour communiquer avec empathie. Cette configuration favorise la comprehension emotionnelle et l'expression des sentiments.

## Ton potentiel
Tu peux developper une communication qui touche les coeurs.

## Ton defi
Le talent de communication emotionnelle demande d'etre pratique.

## Conseil pratique
Exprime ce que tu ressens avec des mots. La parole emotionnelle guerit.""",

    ('mercury', 'neptune'): """# \u26b9 Sextile Mercure - Neptune
**En une phrase :** Une opportunite d'imagination creatrice qui recompense la pensee poetique.

## L'energie de cet aspect
Le sextile Mercure-Neptune offre une facilite pour la pensee creative et intuitive. Cette configuration favorise l'expression artistique et la perception subtile.

## Ton potentiel
Tu peux developper une communication poetique et des intuitions fiables.

## Ton defi
L'imagination demande d'etre canalisee dans des formes concretes.

## Conseil pratique
Ecris, dessine, cree. Donne forme a tes intuitions et inspirations.""",

    ('mercury', 'pluto'): """# \u26b9 Sextile Mercure - Pluton
**En une phrase :** Une opportunite de pensee profonde qui recompense l'investigation.

## L'energie de cet aspect
Le sextile Mercure-Pluton offre une facilite pour comprendre les motivations cachees. Cette configuration favorise la recherche et la communication transformatrice.

## Ton potentiel
Tu peux developper une capacite a percevoir et dire les verites profondes.

## Ton defi
La penetration intellectuelle demande d'etre cultivee activement.

## Conseil pratique
Explore les sujets en profondeur. La surface ne te satisfait pas.""",

    ('mercury', 'saturn'): """# \u26b9 Sextile Mercure - Saturne
**En une phrase :** Une opportunite de pensee structuree qui recompense la rigueur intellectuelle.

## L'energie de cet aspect
Le sextile Mercure-Saturne offre une facilite pour la pensee methodique. Cette configuration favorise l'apprentissage approfondi et la communication precise.

## Ton potentiel
Tu peux developper une expertise solide et une expression claire.

## Ton defi
La rigueur intellectuelle demande un effort soutenu pour se developper.

## Conseil pratique
Investis dans l'apprentissage approfondi. La maitrise vient avec le temps.""",

    ('mercury', 'sun'): """# \u26b9 Sextile Mercure - Soleil
**En une phrase :** Une opportunite d'expression personnelle qui recompense la communication authentique.

## L'energie de cet aspect
Le sextile Mercure-Soleil offre une facilite pour communiquer son identite. Cette configuration favorise l'expression de soi claire et engageante.

## Ton potentiel
Tu peux developper une voix personnelle qui inspire et informe.

## Ton defi
Le talent d'expression demande d'etre pratique regulierement.

## Conseil pratique
Partage tes idees et tes perspectives. Ta voix merite d'etre entendue.""",

    ('mercury', 'uranus'): """# \u26b9 Sextile Mercure - Uranus
**En une phrase :** Une opportunite de pensee originale qui recompense l'ouverture intellectuelle.

## L'energie de cet aspect
Le sextile Mercure-Uranus offre une facilite pour les idees novatrices. Cette configuration favorise l'intuition intellectuelle et la communication originale.

## Ton potentiel
Tu peux developper une pensee en avance sur son temps qui inspire.

## Ton defi
L'originalite intellectuelle demande d'oser partager des idees differentes.

## Conseil pratique
Explore les idees non conventionnelles. L'innovation commence par la pensee.""",

    ('mercury', 'venus'): """# \u26b9 Sextile Mercure - Venus
**En une phrase :** Une opportunite d'expression elegante qui recompense la diplomatie.

## L'energie de cet aspect
Le sextile Mercure-Venus offre une facilite pour la communication harmonieuse. Cette configuration favorise l'expression artistique et la negociation.

## Ton potentiel
Tu peux developper une capacite a communiquer avec grace et a creer la beaute.

## Ton defi
Le charme verbal demande d'etre cultive consciemment.

## Conseil pratique
Affine ton expression. La beaute dans les mots cree des ponts.""",

    ('moon', 'neptune'): """# \u26b9 Sextile Lune - Neptune
**En une phrase :** Une opportunite de sensibilite spirituelle qui recompense l'ouverture du coeur.

## L'energie de cet aspect
Le sextile Lune-Neptune offre une facilite pour l'intuition et la compassion. Cette configuration favorise les experiences emotionnelles significatives et l'inspiration artistique.

## Ton potentiel
Tu peux developper une empathie profonde et une creativite nourrie par l'ame.

## Ton defi
La sensibilite spirituelle demande d'etre cultivee par la pratique.

## Conseil pratique
Fais confiance a tes intuitions emotionnelles. L'ame parle par les sentiments.""",

    ('moon', 'pluto'): """# \u26b9 Sextile Lune - Pluton
**En une phrase :** Une opportunite de profondeur emotionnelle qui recompense l'authenticite affective.

## L'energie de cet aspect
Le sextile Lune-Pluton offre une facilite pour les emotions profondes et la regeneration. Cette configuration favorise la transformation emotionnelle positive.

## Ton potentiel
Tu peux developper une force emotionnelle et une capacite a accompagner les autres dans leurs profondeurs.

## Ton defi
La profondeur emotionnelle demande d'accepter d'explorer ses ombres.

## Conseil pratique
Plonge dans tes emotions profondes. La transformation vient de l'authenticite.""",

    ('moon', 'saturn'): """# \u26b9 Sextile Lune - Saturne
**En une phrase :** Une opportunite de maturite emotionnelle qui recompense la responsabilite affective.

## L'energie de cet aspect
Le sextile Lune-Saturne offre une facilite pour la stabilite emotionnelle. Cette configuration favorise les relations durables et la fiabilite affective.

## Ton potentiel
Tu peux developper une presence emotionnelle stable et securisante.

## Ton defi
La maturite emotionnelle demande d'assumer ses engagements affectifs.

## Conseil pratique
Sois present pour ceux que tu aimes. La constance construit la confiance.""",

    ('moon', 'sun'): """# \u26b9 Sextile Lune - Soleil
**En une phrase :** Une opportunite d'harmonie interieure qui recompense l'integration des polarites.

## L'energie de cet aspect
Le sextile Lune-Soleil offre une facilite pour l'equilibre entre raison et emotion. Cette configuration favorise une expression de soi coherente.

## Ton potentiel
Tu peux developper une personnalite integree ou pensee et sentiment collaborent.

## Ton defi
L'harmonie interieure demande un travail conscient d'integration.

## Conseil pratique
Honore tes deux voix interieures. La tete et le coeur peuvent s'accorder.""",

    ('moon', 'uranus'): """# \u26b9 Sextile Lune - Uranus
**En une phrase :** Une opportunite de liberte emotionnelle qui recompense l'originalite affective.

## L'energie de cet aspect
Le sextile Lune-Uranus offre une facilite pour l'independance emotionnelle. Cette configuration favorise les relations non conventionnelles et la fraicheur affective.

## Ton potentiel
Tu peux developper une vie emotionnelle authentique et libre.

## Ton defi
La liberte emotionnelle demande d'oser etre different dans tes attachements.

## Conseil pratique
Cree des liens qui respectent ton unicite. L'amour peut etre libre.""",

    ('moon', 'venus'): """# \u26b9 Sextile Lune - Venus
**En une phrase :** Une opportunite de douceur qui recompense l'ouverture affective.

## L'energie de cet aspect
Le sextile Lune-Venus offre une facilite pour l'harmonie emotionnelle. Cette configuration favorise les relations nourrissantes et l'appreciation de la beaute.

## Ton potentiel
Tu peux developper des relations tendres et un sens esthetique raffine.

## Ton defi
La douceur naturelle demande d'etre cultivee et partagee.

## Conseil pratique
Cree de la beaute dans ton quotidien. La douceur se repand par l'exemple.""",
}

async def insert_interpretations():
    """Insere les interpretations sextile part 2 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in SEXTILE_PART2.items():
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
