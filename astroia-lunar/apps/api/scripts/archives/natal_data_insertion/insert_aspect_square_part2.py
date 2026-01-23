#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects carre (part 2/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

SQUARE_PART2 = {
    ('mars', 'uranus'): """# \u25a1 Carre Mars - Uranus
**En une phrase :** Une tension explosive entre action et liberation qui peut creer des ruptures soudaines ou des innovations audacieuses.

## L'energie de cet aspect
Le carre Mars-Uranus cree une friction electrique entre impulsion et independance. Cette configuration peut mener a des actions imprevisibles ou des accidents.

## Ton potentiel
Tu peux canaliser cette energie en innovations courageuses et en actions liberatrices.

## Ton defi
L'impulsivite dangereuse, les ruptures prematurees ou l'instabilite chronique.

## Conseil pratique
Trouve des exutoires surs pour cette energie. L'innovation calculee vaut mieux que la rebellion aveugle.""",

    ('mars', 'venus'): """# \u25a1 Carre Mars - Venus
**En une phrase :** Une tension entre desir et attraction qui peut creer des conflits relationnels ou une passion creatrice.

## L'energie de cet aspect
Le carre Mars-Venus cree une friction entre masculin et feminin. Cette configuration peut mener a des tensions dans les relations ou a une creativite dynamique.

## Ton potentiel
Tu peux transformer cette tension en passion creatrice et en magnetisme.

## Ton defi
Les conflits relationnels, l'impatience en amour ou les desirs contradictoires.

## Conseil pratique
Accepte la tension comme source d'energie. Le desir et l'harmonie peuvent coexister.""",

    ('mercury', 'moon'): """# \u25a1 Carre Mercure - Lune
**En une phrase :** Une tension entre raison et emotion qui peut creer des conflits interieurs ou une intelligence emotionnelle developpee.

## L'energie de cet aspect
Le carre Mercure-Lune cree une friction entre pensee et sentiment. Cette configuration peut mener a des oscillations entre analyse froide et reaction emotionnelle.

## Ton potentiel
Tu peux developper une communication qui integre logique et sensibilite.

## Ton defi
Les malentendus emotionnels, l'anxiete ou les pensees obsessionnelles.

## Conseil pratique
Reconnais quand tu penses et quand tu ressens. Les deux ont leur place.""",

    ('mercury', 'neptune'): """# \u25a1 Carre Mercure - Neptune
**En une phrase :** Une tension entre logique et intuition qui peut creer de la confusion ou une pensee visionnaire.

## L'energie de cet aspect
Le carre Mercure-Neptune cree une friction entre raison et imagination. Cette configuration peut brouiller la pensee ou ouvrir a des perceptions subtiles.

## Ton potentiel
Tu peux developper une pensee qui integre intuition et clarte.

## Ton defi
La confusion mentale, les malentendus ou la tendance a la fabulation.

## Conseil pratique
Verifie tes perceptions avant d'agir. L'intuition a besoin d'ancrage.""",

    ('mercury', 'pluto'): """# \u25a1 Carre Mercure - Pluton
**En une phrase :** Une tension entre pensee et profondeur qui peut creer des obsessions ou une penetration psychologique.

## L'energie de cet aspect
Le carre Mercure-Pluton cree une friction entre communication et pouvoir. Cette configuration peut mener a des pensees obsessionnelles ou a une capacite d'investigation.

## Ton potentiel
Tu peux developper une pensee profonde qui transforme.

## Ton defi
Les obsessions mentales, la manipulation verbale ou la paranoiia.

## Conseil pratique
Utilise ta penetration pour comprendre, pas pour controler.""",

    ('mercury', 'saturn'): """# \u25a1 Carre Mercure - Saturne
**En une phrase :** Une tension entre pensee et structure qui peut creer des blocages ou une rigueur intellectuelle.

## L'energie de cet aspect
Le carre Mercure-Saturne cree une friction entre communication et discipline. Cette configuration peut mener a des inhibitions d'expression ou a une pensee precise.

## Ton potentiel
Tu peux developper une pensee structuree et fiable.

## Ton defi
Les blocages d'expression, le pessimisme mental ou l'autocritique excessive.

## Conseil pratique
Tes idees meritent d'etre partagees. La perfection n'est pas requise pour communiquer.""",

    ('mercury', 'sun'): """# \u25a1 Carre Mercure - Soleil
**En une phrase :** Une tension rare entre pensee et identite qui demande d'aligner expression et essence.

## L'energie de cet aspect
Le carre Mercure-Soleil est astronomiquement rare. Symboliquement, il represente un decalage entre ce que tu penses et qui tu es.

## Ton potentiel
Tu peux developper une objectivite sur toi-meme et une communication authentique.

## Ton defi
Le decalage entre paroles et actes ou la difficulte a exprimer ton essence.

## Conseil pratique
Aligne tes mots avec ton coeur. L'authenticite se communique.""",

    ('mercury', 'uranus'): """# \u25a1 Carre Mercure - Uranus
**En une phrase :** Une tension entre pensee conventionnelle et originale qui peut creer de l'instabilite mentale ou du genie.

## L'energie de cet aspect
Le carre Mercure-Uranus cree une friction entre logique et intuition soudaine. Cette configuration peut disperser la pensee ou generer des eclairs de genie.

## Ton potentiel
Tu peux developper une pensee originale qui innove et surprend.

## Ton defi
L'instabilite mentale, la dispersion ou la difficulte a communiquer tes idees.

## Conseil pratique
Structure tes intuitions. Le genie a besoin d'un vehicule pour etre compris.""",

    ('mercury', 'venus'): """# \u25a1 Carre Mercure - Venus
**En une phrase :** Une tension entre communication et harmonie qui peut creer des desaccords ou un raffinement expressif.

## L'energie de cet aspect
Le carre Mercure-Venus cree une friction entre expression et valeurs. Cette configuration peut mener a des difficultes a exprimer l'affection ou a un raffinement du langage.

## Ton potentiel
Tu peux developper une communication qui allie verite et diplomatie.

## Ton defi
La difficulte a exprimer les sentiments ou les malentendus en amour.

## Conseil pratique
Les mots d'amour peuvent etre appris. L'expression de l'affection se cultive.""",

    ('moon', 'neptune'): """# \u25a1 Carre Lune - Neptune
**En une phrase :** Une tension entre besoins emotionnels et aspirations spirituelles qui peut creer de la confusion ou une sensibilite profonde.

## L'energie de cet aspect
Le carre Lune-Neptune cree une friction entre emotion et dissolution. Cette configuration peut brouiller les emotions ou ouvrir a une compassion profonde.

## Ton potentiel
Tu peux developper une sensibilite qui percoit et guerit sans se perdre.

## Ton defi
La confusion emotionnelle, les illusions affectives ou les dependencies.

## Conseil pratique
Ancre-toi dans ton corps pour distinguer tes emotions de celles des autres.""",

    ('moon', 'pluto'): """# \u25a1 Carre Lune - Pluton
**En une phrase :** Une tension intense entre besoins emotionnels et forces de transformation qui peut creer des crises ou une force interieure.

## L'energie de cet aspect
Le carre Lune-Pluton cree une friction entre securite et transformation. Cette configuration peut mener a des emotions intenses et des crises periodiques.

## Ton potentiel
Tu developpes une force emotionnelle et une resilience remarquables.

## Ton defi
Les emotions obsessionnelles, le controle affectif ou les crises repetitives.

## Conseil pratique
Laisse les emotions circuler. Le controle excessif cree les crises.""",

    ('moon', 'saturn'): """# \u25a1 Carre Lune - Saturne
**En une phrase :** Une tension entre besoins emotionnels et responsabilites qui peut creer de la froideur ou une maturite emotionnelle.

## L'energie de cet aspect
Le carre Lune-Saturne cree une friction entre besoins et devoirs. Cette configuration peut mener a une inhibition emotionnelle ou a une fiabilite profonde.

## Ton potentiel
Tu developpes une stabilite emotionnelle et une capacite a supporter les difficultes.

## Ton defi
La repression emotionnelle, la melancolie ou la difficulte a recevoir.

## Conseil pratique
Tes besoins emotionnels sont legitimes. Prendre soin de toi n'est pas egoiste.""",

    ('moon', 'sun'): """# \u25a1 Carre Lune - Soleil
**En une phrase :** Une tension fondamentale entre conscient et inconscient qui demande l'integration des polarites interieures.

## L'energie de cet aspect
Le carre Lune-Soleil (quartier de lune natal) cree une friction entre volonte et emotions. Cette configuration peut mener a des conflits interieurs ou a une richesse psychologique.

## Ton potentiel
Tu developpes une conscience de soi nuancee qui integre raison et emotion.

## Ton defi
Les conflits entre ce que tu veux et ce que tu ressens, ou l'ambivalence.

## Conseil pratique
Accueille les deux voix interieures. Le conflit est source de croissance.""",

    ('moon', 'uranus'): """# \u25a1 Carre Lune - Uranus
**En une phrase :** Une tension entre securite emotionnelle et besoin de liberte qui peut creer de l'instabilite ou une independance saine.

## L'energie de cet aspect
Le carre Lune-Uranus cree une friction entre attachement et detachement. Cette configuration peut mener a des emotions imprevisibles ou a une liberte emotionnelle.

## Ton potentiel
Tu peux developper une independance emotionnelle saine qui n'exclut pas l'intimite.

## Ton defi
L'instabilite emotionnelle, les ruptures soudaines ou la peur de l'engagement.

## Conseil pratique
La securite et la liberte peuvent coexister. Cree tes propres regles.""",

    ('moon', 'venus'): """# \u25a1 Carre Lune - Venus
**En une phrase :** Une tension entre besoins emotionnels et desirs relationnels qui peut creer des conflits affectifs ou une sensibilite raffinee.

## L'energie de cet aspect
Le carre Lune-Venus cree une friction entre ce que tu as besoin et ce que tu veux en amour. Cette configuration peut mener a des insatisfactions ou a un raffinement affectif.

## Ton potentiel
Tu peux developper une capacite a equilibrer donner et recevoir en amour.

## Ton defi
L'insatisfaction affective, les attentes irrealistes ou les sacrifices excessifs.

## Conseil pratique
Distingue tes vrais besoins de tes desirs conditionnes. L'amour de soi d'abord.""",
}

async def insert_interpretations():
    """Insere les interpretations carre part 2 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in SQUARE_PART2.items():
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
