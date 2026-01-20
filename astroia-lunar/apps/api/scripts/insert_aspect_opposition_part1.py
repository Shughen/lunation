#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects opposition (part 1/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

OPPOSITION_PART1 = {
    ('jupiter', 'mars'): """# \u260d Opposition Jupiter - Mars
**En une phrase :** Une tension entre l'expansion et l'action qui demande d'equilibrer ambition et realisme.

## L'energie de cet aspect
L'opposition Jupiter-Mars cree une polarite entre vouloir grand et agir concretement. Cette configuration peut alterner entre exces d'optimisme et frustration. Tu oscilles entre projets grandioses et impatience.

## Ton potentiel
Tu peux accomplir beaucoup quand tu trouves l'equilibre entre vision et action concrete.

## Ton defi
L'exageration dans l'effort ou les promesses impossibles a tenir peuvent creer des deceptions.

## Conseil pratique
Divise tes grands projets en etapes realisables. L'action mesuree accomplit plus que l'enthousiasme debordant.""",

    ('jupiter', 'mercury'): """# \u260d Opposition Jupiter - Mercure
**En une phrase :** Une tension entre la vue d'ensemble et les details qui enrichit la pensee quand elle est integree.

## L'energie de cet aspect
L'opposition Jupiter-Mercure polarise la pensee entre synthese et analyse. Cette configuration peut creer une oscillation entre generalisation excessive et details pointilleux.

## Ton potentiel
Tu peux developper une pensee complete qui voit a la fois le global et le specifique.

## Ton defi
Les jugements hatifs ou les promesses intellectuelles non tenues peuvent nuire a ta credibilite.

## Conseil pratique
Verifie tes affirmations avant de les partager. La precision renforce la vision.""",

    ('jupiter', 'moon'): """# \u260d Opposition Jupiter - Lune
**En une phrase :** Une tension entre besoins emotionnels et soif d'expansion qui demande d'equilibrer securite et croissance.

## L'energie de cet aspect
L'opposition Jupiter-Lune cree une polarite entre le besoin de securite emotionnelle et le desir d'horizons nouveaux. Tu peux osciller entre le confort du foyer et l'appel de l'aventure.

## Ton potentiel
Tu sais nourrir les autres tout en les inspirant a grandir. Ta generosite emotionnelle est vaste.

## Ton defi
Les exces emotionnels ou l'instabilite affective peuvent creer des hauts et des bas.

## Conseil pratique
Cree une base secure d'ou tu peux explorer. La croissance n'exclut pas les racines.""",

    ('jupiter', 'neptune'): """# \u260d Opposition Jupiter - Neptune
**En une phrase :** Une tension entre foi et illusion qui demande de discerner les vrais ideaux des fausses promesses.

## L'energie de cet aspect
L'opposition Jupiter-Neptune amplifie les tendances idealistes au risque de la deconnexion du reel. Cette configuration peut creer une grande inspiration ou de grandes desillusions.

## Ton potentiel
Tu peux inspirer par ta vision spirituelle quand elle reste ancree dans la realite.

## Ton defi
La naivete excessive et les promesses utopiques peuvent mener a la deception.

## Conseil pratique
Developpe ton discernement spirituel. Les vrais ideaux se verifient dans le quotidien.""",

    ('jupiter', 'pluto'): """# \u260d Opposition Jupiter - Pluton
**En une phrase :** Une tension entre expansion et pouvoir qui demande d'utiliser l'influence avec sagesse.

## L'energie de cet aspect
L'opposition Jupiter-Pluton cree une polarite entre croissance et controle. Cette configuration peut osciller entre megalomanie et transformation profonde.

## Ton potentiel
Tu peux accomplir des transformations majeures quand tu allies vision et profondeur.

## Ton defi
Les luttes de pouvoir pour l'expansion ou la manipulation peuvent corrompre tes bonnes intentions.

## Conseil pratique
Mets ton influence au service du bien commun. Le vrai pouvoir transforme positivement.""",

    ('jupiter', 'saturn'): """# \u260d Opposition Jupiter - Saturne
**En une phrase :** Une tension classique entre expansion et contraction qui demande d'equilibrer optimisme et realisme.

## L'energie de cet aspect
L'opposition Jupiter-Saturne est une polarite fondamentale entre croissance et structure. Cette configuration cree une alternance entre phases d'expansion et de consolidation.

## Ton potentiel
Tu developpes une sagesse qui sait quand avancer et quand consolider.

## Ton defi
L'oscillation entre exces d'optimisme et pessimisme peut creer de l'instabilite.

## Conseil pratique
Accepte le rythme naturel d'expansion et de contraction. Les deux sont necessaires.""",

    ('jupiter', 'sun'): """# \u260d Opposition Jupiter - Soleil
**En une phrase :** Une tension entre identite et expansion qui demande de trouver ta propre voie de croissance.

## L'energie de cet aspect
L'opposition Jupiter-Soleil cree une polarite entre l'ego et les opportunites exterieures. Tu peux te sentir tiraille entre qui tu es et ce que la vie t'offre.

## Ton potentiel
Tu peux integrer les opportunites tout en restant fidele a toi-meme.

## Ton defi
L'inflation de l'ego ou la dispersion dans les opportunites peuvent te faire perdre ton centre.

## Conseil pratique
Choisis les opportunites qui alignent avec ton essence. Pas tout ce qui brille n'est pour toi.""",

    ('jupiter', 'uranus'): """# \u260d Opposition Jupiter - Uranus
**En une phrase :** Une tension entre expansion conventionnelle et liberation radicale qui demande d'innover avec sagesse.

## L'energie de cet aspect
L'opposition Jupiter-Uranus cree une polarite entre croissance etablie et changement soudain. Tu oscilles entre opportunites traditionnelles et ruptures liberatrices.

## Ton potentiel
Tu peux allier vision d'avenir et innovations pratiques pour creer des changements durables.

## Ton defi
L'instabilite entre conservatisme opportuniste et rebellion peut creer de l'incoherence.

## Conseil pratique
Integre l'innovation dans une vision plus large. Le changement radical peut servir la croissance.""",

    ('jupiter', 'venus'): """# \u260d Opposition Jupiter - Venus
**En une phrase :** Une tension entre abondance et plaisir qui demande d'equilibrer generosite et exces.

## L'energie de cet aspect
L'opposition Jupiter-Venus amplifie le desir de plaisir et de confort. Cette configuration peut osciller entre generosite excessive et auto-indulgence.

## Ton potentiel
Tu sais apprecier et partager les bonnes choses de la vie avec mesure.

## Ton defi
Les exces dans les plaisirs ou les depenses peuvent creer des desequilibres.

## Conseil pratique
Cultive l'appreciation plutot que l'accumulation. La vraie abondance est interieure.""",

    ('mars', 'mercury'): """# \u260d Opposition Mars - Mercure
**En une phrase :** Une tension entre pensee et action qui peut creer des conflits verbaux ou une communication dynamique.

## L'energie de cet aspect
L'opposition Mars-Mercure polarise l'esprit et l'energie d'action. Cette configuration peut creer des debats intenses ou une pensee combative.

## Ton potentiel
Tu sais defendre tes idees avec vigueur et penser strategiquement.

## Ton defi
L'agressivite verbale ou les disputes inutiles peuvent deteriorer les relations.

## Conseil pratique
Canalise ton energie mentale dans des debats constructifs. Les mots peuvent construire ou detruire.""",

    ('mars', 'moon'): """# \u260d Opposition Mars - Lune
**En une phrase :** Une tension entre emotions et action qui demande d'equilibrer sensibilite et assertivite.

## L'energie de cet aspect
L'opposition Mars-Lune polarise les besoins emotionnels et l'energie d'action. Cette configuration peut creer des conflits entre ce que tu ressens et ce que tu fais.

## Ton potentiel
Tu peux agir de facon protectrice et courageux pour ceux que tu aimes.

## Ton defi
Les reactions emotionnelles impulsives ou l'agressivite passive peuvent blesser.

## Conseil pratique
Prends le temps de ressentir avant d'agir. L'action juste honore les emotions sans y reagir.""",

    ('mars', 'neptune'): """# \u260d Opposition Mars - Neptune
**En une phrase :** Une tension entre action directe et inspiration subtile qui demande de clarifier les motivations.

## L'energie de cet aspect
L'opposition Mars-Neptune cree une polarite entre agir et rever. Cette configuration peut osciller entre passivite inspiree et action confuse.

## Ton potentiel
Tu peux agir au service d'ideaux eleves quand tes motivations sont claires.

## Ton defi
La confusion sur ce que tu veux vraiment ou les actions sabotees par l'inconscient peuvent frustrer.

## Conseil pratique
Clarifie tes intentions avant d'agir. L'action inspiree demande une direction claire.""",

    ('mars', 'pluto'): """# \u260d Opposition Mars - Pluton
**En une phrase :** Une tension intense entre volonte et pouvoir qui peut creer des confrontations transformatrices.

## L'energie de cet aspect
L'opposition Mars-Pluton concentre une energie considerable dans les confrontations. Cette configuration peut creer des luttes de pouvoir intenses ou des transformations profondes.

## Ton potentiel
Tu possedes une force de volonte et une capacite de transformation remarquables.

## Ton defi
Les affrontements destructeurs ou la volonte de domination peuvent causer des dommages.

## Conseil pratique
Choisis tes combats avec sagesse. La vraie puissance transforme sans detruire.""",

    ('mars', 'saturn'): """# \u260d Opposition Mars - Saturne
**En une phrase :** Une tension entre action et restriction qui demande d'apprendre la patience dans l'effort.

## L'energie de cet aspect
L'opposition Mars-Saturne cree une polarite entre impulsion et controle. Cette configuration peut creer des frustrations ou une discipline remarkquable.

## Ton potentiel
Tu developpes une endurance et une perseverance exceptionnelles dans l'effort.

## Ton defi
La frustration face aux obstacles ou l'alternance entre exces et repression peuvent epuiser.

## Conseil pratique
Accepte les delais comme partie du processus. L'effort soutenu surpasse l'impulsion.""",

    ('mars', 'sun'): """# \u260d Opposition Mars - Soleil
**En une phrase :** Une tension entre identite et action qui demande d'aligner volonte et expression personnelle.

## L'energie de cet aspect
L'opposition Mars-Soleil polarise l'ego et l'energie d'action. Cette configuration peut creer des conflits entre ce que tu es et ce que tu fais.

## Ton potentiel
Tu peux developper une assertivite saine qui exprime ton identite authentique.

## Ton defi
Les conflits d'ego ou l'epuisement par une action non alignee peuvent survenir.

## Conseil pratique
Agis en accord avec tes valeurs profondes. L'action authentique renforce l'identite.""",
}

async def insert_interpretations():
    """Insere les interpretations opposition part 1 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in OPPOSITION_PART1.items():
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
