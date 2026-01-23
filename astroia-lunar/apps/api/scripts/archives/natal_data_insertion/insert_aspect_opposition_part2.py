#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects opposition (part 2/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

OPPOSITION_PART2 = {
    ('mars', 'uranus'): """# \u260d Opposition Mars - Uranus
**En une phrase :** Une tension electrique entre action et liberation qui peut creer des ruptures soudaines ou des innovations audacieuses.

## L'energie de cet aspect
L'opposition Mars-Uranus polarise l'impulsion et l'independance. Cette configuration peut creer des actions imprevisibles ou une rebellion contre les contraintes.

## Ton potentiel
Tu sais initier des changements audacieux et te liberer des situations oppressantes.

## Ton defi
L'impulsivite dangereuse ou les ruptures prematurees peuvent creer du chaos.

## Conseil pratique
Canalise ton energie revolutionnaire dans des actions reflechies. La vraie liberte demande de la strategie.""",

    ('mars', 'venus'): """# \u260d Opposition Mars - Venus
**En une phrase :** Une tension classique entre masculin et feminin qui peut creer des attractions intenses ou des conflits relationnels.

## L'energie de cet aspect
L'opposition Mars-Venus polarise le desir et l'attraction. Cette configuration cree une dynamique forte dans les relations amoureuses et creatives.

## Ton potentiel
Tu possedes un magnetisme relationnel puissant et une passion creatrice.

## Ton defi
Les conflits entre ce que tu veux et ce que tu attires peuvent creer de la frustration.

## Conseil pratique
Integre ton assertivite et ta receptivite. L'equilibre cree des relations plus harmonieuses.""",

    ('mercury', 'moon'): """# \u260d Opposition Mercure - Lune
**En une phrase :** Une tension entre raison et emotion qui peut creer des conflits interieurs ou une intelligence emotionnelle developpee.

## L'energie de cet aspect
L'opposition Mercure-Lune polarise la pensee et le ressenti. Cette configuration peut creer une oscillation entre analyse froide et reaction emotionnelle.

## Ton potentiel
Tu peux developper une communication qui honore a la fois la logique et les sentiments.

## Ton defi
Les malentendus emotionnels ou la rationalisation excessive des sentiments peuvent survenir.

## Conseil pratique
Ecoute tes emotions comme source d'information valide. La tete et le coeur peuvent collaborer.""",

    ('mercury', 'neptune'): """# \u260d Opposition Mercure - Neptune
**En une phrase :** Une tension entre logique et intuition qui peut creer de la confusion ou une pensee visionnaire.

## L'energie de cet aspect
L'opposition Mercure-Neptune polarise le rationnel et l'imaginaire. Cette configuration peut osciller entre clarte mentale et brouillard conceptuel.

## Ton potentiel
Tu peux communiquer des visions inspirees quand tu ancres ton intuition dans la clarte.

## Ton defi
La confusion mentale, les malentendus ou la tendance a la fabulation peuvent poser probleme.

## Conseil pratique
Verifie tes perceptions avant de communiquer. L'inspiration a besoin de structure pour etre comprise.""",

    ('mercury', 'pluto'): """# \u260d Opposition Mercure - Pluton
**En une phrase :** Une tension entre pensee de surface et profondeur qui peut creer des obsessions mentales ou une penetration psychologique.

## L'energie de cet aspect
L'opposition Mercure-Pluton polarise la communication et le pouvoir. Cette configuration peut creer des pensees obsessionnelles ou une capacite d'investigation profonde.

## Ton potentiel
Tu peux percevoir les motivations cachees et communiquer des verites transformatrices.

## Ton defi
La manipulation par les mots ou les pensees negatives obsessionnelles peuvent nuire.

## Conseil pratique
Utilise ton pouvoir mental pour guerir plutot que pour blesser. La verite libere quand elle est dite avec compassion.""",

    ('mercury', 'saturn'): """# \u260d Opposition Mercure - Saturne
**En une phrase :** Une tension entre fluidite mentale et rigueur qui peut creer des blocages ou une pensee structuree.

## L'energie de cet aspect
L'opposition Mercure-Saturne polarise la communication et la discipline. Cette configuration peut creer des periodes de doute intellectuel ou une rigueur mentale.

## Ton potentiel
Tu developpes une pensee precise et fiable, capable de structurer des idees complexes.

## Ton defi
Le pessimisme mental, les blocages d'expression ou l'exces de critique peuvent freiner.

## Conseil pratique
Valorise ta profondeur sans te censurer. Les idees meritent d'etre partagees meme imparfaites.""",

    ('mercury', 'sun'): """# \u260d Opposition Mercure - Soleil
**En une phrase :** Une tension entre pensee et identite qui demande d'aligner communication et expression personnelle.

## L'energie de cet aspect
L'opposition Mercure-Soleil est rare astronomiquement mais symbolise une distance entre ce que tu penses et qui tu es.

## Ton potentiel
Tu peux developper une objectivite sur toi-meme et communiquer avec recul.

## Ton defi
Le decalage entre ce que tu dis et ce que tu es peut creer des malentendus.

## Conseil pratique
Aligne tes paroles avec ton essence. L'authenticite se communique naturellement.""",

    ('mercury', 'uranus'): """# \u260d Opposition Mercure - Uranus
**En une phrase :** Une tension entre pensee conventionnelle et eclairs de genie qui peut creer de l'instabilite mentale ou de l'innovation.

## L'energie de cet aspect
L'opposition Mercure-Uranus polarise la communication et l'originalite. Cette configuration peut creer des idees brillantes mais difficiles a communiquer.

## Ton potentiel
Tu sais percevoir des connexions que d'autres ne voient pas et innover intellectuellement.

## Ton defi
L'instabilite mentale ou la difficulte a faire comprendre tes idees peuvent isoler.

## Conseil pratique
Trouve des ponts entre tes intuitions et le langage commun. Le genie a besoin de traducteurs.""",

    ('mercury', 'venus'): """# \u260d Opposition Mercure - Venus
**En une phrase :** Une tension entre communication et valeurs qui peut creer des desaccords esthetiques ou une expression raffinee.

## L'energie de cet aspect
L'opposition Mercure-Venus polarise la pensee et l'harmonie. Cette configuration peut creer une oscillation entre dire la verite et maintenir l'harmonie.

## Ton potentiel
Tu peux communiquer avec elegance tout en restant authentique.

## Ton defi
Eviter les sujets difficiles pour maintenir la paix ou communiquer de facon superficielle.

## Conseil pratique
La verite peut etre dite avec grace. L'harmonie veritable inclut l'authenticite.""",

    ('moon', 'neptune'): """# \u260d Opposition Lune - Neptune
**En une phrase :** Une tension entre besoins emotionnels et aspirations spirituelles qui peut creer de la confusion ou une sensibilite transcendante.

## L'energie de cet aspect
L'opposition Lune-Neptune polarise la securite emotionnelle et la dissolution des frontieres. Cette configuration peut creer une hypersensibilite ou une connexion spirituelle profonde.

## Ton potentiel
Tu possedes une empathie et une intuition remarquables qui peuvent servir les autres.

## Ton defi
La confusion entre tes emotions et celles des autres ou les illusions emotionnelles.

## Conseil pratique
Ancre-toi dans ton corps pour distinguer ce qui t'appartient. La compassion commence par toi-meme.""",

    ('moon', 'pluto'): """# \u260d Opposition Lune - Pluton
**En une phrase :** Une tension intense entre besoins emotionnels et forces de transformation qui peut creer des crises ou une regeneration profonde.

## L'energie de cet aspect
L'opposition Lune-Pluton polarise la securite et la transformation. Cette configuration peut creer des emotions intenses qui demandent d'etre traversees.

## Ton potentiel
Tu possedes une force emotionnelle et une capacite de regeneration remarquables.

## Ton defi
Les emotions obsessionnelles, la manipulation affective ou le controle excessif.

## Conseil pratique
Laisse les emotions circuler sans les retenir ni les amplifier. La transformation se fait dans le lacher-prise.""",

    ('moon', 'saturn'): """# \u260d Opposition Lune - Saturne
**En une phrase :** Une tension entre besoins emotionnels et responsabilites qui peut creer de la froideur ou une maturite emotionnelle.

## L'energie de cet aspect
L'opposition Lune-Saturne polarise les besoins affectifs et les exigences du reel. Cette configuration peut creer une inhibition emotionnelle ou une stabilite remarquable.

## Ton potentiel
Tu developpes une fiabilite emotionnelle et une capacite a supporter les difficultes.

## Ton defi
La repression des besoins affectifs ou la peur de la vulnerabilite peuvent isoler.

## Conseil pratique
Honore tes besoins emotionnels autant que tes responsabilites. Prendre soin de soi n'est pas egoiste.""",

    ('moon', 'sun'): """# \u260d Opposition Lune - Soleil
**En une phrase :** Une tension fondamentale entre conscient et inconscient qui cree une richesse interieure par l'integration des polarites.

## L'energie de cet aspect
L'opposition Lune-Soleil (Pleine Lune natale) cree une polarite entre l'identite et les emotions. Cette configuration donne une conscience aigue des tensions interieures.

## Ton potentiel
Tu developpes une capacite d'integration des opposites et une richesse psychologique.

## Ton defi
L'oscillation entre ce que tu veux etre et ce que tu ressens peut creer des tiraillements.

## Conseil pratique
Accueille les deux poles sans choisir. L'integration se fait dans l'acceptation.""",

    ('moon', 'uranus'): """# \u260d Opposition Lune - Uranus
**En une phrase :** Une tension entre securite emotionnelle et besoin de liberte qui peut creer de l'instabilite ou une independance affective saine.

## L'energie de cet aspect
L'opposition Lune-Uranus polarise les besoins de securite et de changement. Cette configuration peut creer des emotions imprevisibles ou une originalite emotionnelle.

## Ton potentiel
Tu sais te liberer des conditionnements emotionnels et vivre des emotions authentiques.

## Ton defi
L'instabilite emotionnelle ou la difficulte a creer des liens durables peuvent isoler.

## Conseil pratique
Cree ta propre forme de securite emotionnelle. L'independance n'exclut pas l'intimite.""",

    ('moon', 'venus'): """# \u260d Opposition Lune - Venus
**En une phrase :** Une tension entre besoins emotionnels et desirs relationnels qui demande d'equilibrer ce que tu donnes et ce que tu recois.

## L'energie de cet aspect
L'opposition Lune-Venus polarise les besoins affectifs et les valeurs relationnelles. Cette configuration peut creer une oscillation entre nourrir et etre nourri.

## Ton potentiel
Tu peux developper des relations equilibrees ou les besoins de chacun sont honores.

## Ton defi
La dependance affective ou le sacrifice de tes besoins pour plaire peuvent desequilibrer.

## Conseil pratique
Donne ce que tu peux donner joyeusement. Recevoir est aussi important que donner.""",
}

async def insert_interpretations():
    """Insere les interpretations opposition part 2 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in OPPOSITION_PART2.items():
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
