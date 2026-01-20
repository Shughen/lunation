#!/usr/bin/env python3
"""Script d'insertion des interpretations aspects conjonction (part 2/3)."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_aspect import PregeneratedNatalAspect

# Pairs 16-30: mars-uranus to moon-venus
CONJUNCTION_PART2 = {
    ('mars', 'uranus'): """# \u260c Conjonction Mars - Uranus
**En une phrase :** Une energie explosive et imprevisible qui cherche l'action revolutionnaire.

## L'energie de cet aspect
La conjonction Mars-Uranus cree une impulsion soudaine et liberatrice. Cette configuration donne un besoin intense d'independance dans l'action. Tu detestes les contraintes et les routines.

## Ton potentiel
Tu excelles a initier des changements rapides et a briser les schemas obsoletes. Ton courage est remarquable.

## Ton defi
L'impulsivite peut mener a des accidents ou des conflits soudains. L'impatience sabote les projets a long terme.

## Conseil pratique
Trouve des canaux sains pour cette energie electrique. Accepte un minimum de structure pour maximiser ton impact.""",

    ('mars', 'venus'): """# \u260c Conjonction Mars - Venus
**En une phrase :** Une fusion du masculin et du feminin qui cree un magnetisme seducteur et creatif.

## L'energie de cet aspect
La conjonction Mars-Venus unit le desir et l'attraction. Cette configuration donne un charme actif et une capacite a poursuivre ce que tu veux en amour et dans l'art. Tu sais ce que tu veux et tu vas le chercher.

## Ton potentiel
Tu possedes un magnetisme naturel et une passion creatrice. Tu sais initier les relations avec aisance.

## Ton defi
Les desirs peuvent devenir imperieux. L'impatience en amour cree des tensions.

## Conseil pratique
Equilibre le donner et le recevoir dans tes relations. Utilise ta creativite comme exutoire.""",

    ('mercury', 'moon'): """# \u260c Conjonction Mercure - Lune
**En une phrase :** Un esprit intuitif qui pense avec le coeur et communique avec sensibilite.

## L'energie de cet aspect
La conjonction Mercure-Lune lie la pensee aux emotions. Cette configuration donne une excellente memoire et une communication empreinte de sensibilite. Tu comprends intuitivement ce que les autres ressentent.

## Ton potentiel
Tu excelles a exprimer les emotions et a creer des liens empathiques par la parole.

## Ton defi
Les humeurs peuvent colorer excessivement la pensee. L'hypersensibilite aux mots peut blesser.

## Conseil pratique
Distingue ce que tu ressens de ce que tu penses. Utilise ton empathie pour communiquer avec bienveillance.""",

    ('mercury', 'neptune'): """# \u260c Conjonction Mercure - Neptune
**En une phrase :** Un esprit imaginatif et poetique qui percoit au-dela des mots.

## L'energie de cet aspect
La conjonction Mercure-Neptune ouvre l'esprit aux dimensions subtiles. Cette configuration donne une pensee creative et intuitive, capable de saisir l'ineffable. Tu communiques souvent par images et metaphores.

## Ton potentiel
Tu possedes un talent pour l'ecriture creative, la musique, ou toute forme d'expression artistique.

## Ton defi
La confusion mentale et la difficulte a communiquer clairement peuvent poser probleme.

## Conseil pratique
Ancre tes inspirations dans des formes concretes. Verifie que tu es bien compris.""",

    ('mercury', 'pluto'): """# \u260c Conjonction Mercure - Pluton
**En une phrase :** Un esprit penetrant qui va au fond des choses et decouvre ce qui est cache.

## L'energie de cet aspect
La conjonction Mercure-Pluton donne une pensee profonde et investigatrice. Cette configuration cree un besoin de comprendre les motivations cachees et les verites profondes. Tu ne te contentes jamais des apparences.

## Ton potentiel
Tu excelles dans la recherche, la psychologie, et tout domaine qui demande de penetrer les mysteres.

## Ton defi
L'obsession mentale et la manipulation par les mots sont des pieges possibles.

## Conseil pratique
Utilise ton pouvoir mental de facon ethique. Accepte que certains mysteres restent insondables.""",

    ('mercury', 'saturn'): """# \u260c Conjonction Mercure - Saturne
**En une phrase :** Un esprit serieux et methodique qui structure la pensee avec rigueur.

## L'energie de cet aspect
La conjonction Mercure-Saturne donne une pensee disciplinee et concentree. Cette configuration favorise l'apprentissage approfondi et la communication precise. Tu preferes la qualite a la quantite.

## Ton potentiel
Tu excelles dans les domaines qui demandent concentration et rigueur intellectuelle.

## Ton defi
Le pessimisme mental et la peur de s'exprimer peuvent bloquer la communication.

## Conseil pratique
Valorise ta profondeur intellectuelle. Ose partager tes idees malgre le doute.""",

    ('mercury', 'sun'): """# \u260c Conjonction Mercure - Soleil
**En une phrase :** Une identite qui s'exprime par l'intellect et la communication.

## L'energie de cet aspect
La conjonction Mercure-Soleil fusionne la pensee et l'ego. Cette configuration donne une forte identification au mental et aux idees. Tu as besoin d'exprimer tes pensees pour te sentir vivant.

## Ton potentiel
Tu communiques avec clarte et assurance. Tes idees sont personnelles et authentiques.

## Ton defi
L'objectivite peut souffrir d'un mental trop proche de l'ego.

## Conseil pratique
Cultive l'ecoute autant que l'expression. Reste ouvert aux perspectives differentes.""",

    ('mercury', 'uranus'): """# \u260c Conjonction Mercure - Uranus
**En une phrase :** Un esprit brillant et original qui pense en dehors des cadres etablis.

## L'energie de cet aspect
La conjonction Mercure-Uranus accelere et libere la pensee. Cette configuration donne des eclairs de genie et une capacite a percevoir les connexions inhabituelles. Tu t'ennuies rapidement avec le conventionnel.

## Ton potentiel
Tu excelles a innover et a trouver des solutions originales. Ton esprit est en avance sur son temps.

## Ton defi
La dispersion mentale et la difficulte a communiquer de facon accessible peuvent isoler.

## Conseil pratique
Trouve des moyens de rendre tes idees comprehensibles aux autres. Canalise ton genie.""",

    ('mercury', 'venus'): """# \u260c Conjonction Mercure - Venus
**En une phrase :** Un esprit charmant et diplomatique qui communique avec grace et elegance.

## L'energie de cet aspect
La conjonction Mercure-Venus harmonise la pensee et les valeurs esthetiques. Cette configuration donne un talent pour les mots et une appreciation de la beaute dans le langage. Tu sais dire les choses de facon agreable.

## Ton potentiel
Tu excelles dans la negociation, l'art, et toute communication qui requiert du charme.

## Ton defi
La tendance a eviter les sujets difficiles peut manquer de profondeur.

## Conseil pratique
Ose aborder les sujets delicats avec ta diplomatie naturelle. La verite peut etre dite avec grace.""",

    ('moon', 'neptune'): """# \u260c Conjonction Lune - Neptune
**En une phrase :** Une sensibilite psychique profonde qui ressent les emotions collectives et les mondes subtils.

## L'energie de cet aspect
La conjonction Lune-Neptune dissout les frontieres emotionnelles. Cette configuration donne une empathie profonde et une connexion aux dimensions spirituelles. Tu absorbes les ambiances comme une eponge.

## Ton potentiel
Tu possedes des dons artistiques et intuitifs remarquables. Ta compassion est sans limites.

## Ton defi
La confusion entre tes emotions et celles des autres peut destabiliser. Les illusions emotionnelles sont frequentes.

## Conseil pratique
Protege ta sensibilite par des limites saines. Ancre-toi regulierement dans le concret.""",

    ('moon', 'pluto'): """# \u260c Conjonction Lune - Pluton
**En une phrase :** Des emotions intenses et profondes qui transforment et regenerent en permanence.

## L'energie de cet aspect
La conjonction Lune-Pluton intensifie la vie emotionnelle. Cette configuration donne des sentiments puissants et une capacite de regeneration psychique. Tu vis les emotions a fond.

## Ton potentiel
Tu possedes une force emotionnelle rare et une capacite a accompagner les autres dans les crises.

## Ton defi
Les emotions peuvent devenir obsessionnelles ou manipulatrices. Le controle emotionnel est excessif.

## Conseil pratique
Fais confiance au processus de transformation. Laisse les emotions circuler sans les retenir.""",

    ('moon', 'saturn'): """# \u260c Conjonction Lune - Saturne
**En une phrase :** Des emotions disciplinees qui s'expriment avec reserve et responsabilite.

## L'energie de cet aspect
La conjonction Lune-Saturne structure la vie emotionnelle. Cette configuration demande de maturer les reponses emotionnelles et d'assumer ses besoins. Tu as appris tot a etre responsable.

## Ton potentiel
Tu offres une stabilite emotionnelle fiable. Ta maturite inspire confiance.

## Ton defi
La repression emotionnelle et la difficulte a s'ouvrir peuvent isoler.

## Conseil pratique
Permets-toi de ressentir sans juger. La vulnerabilite est une force, pas une faiblesse.""",

    ('moon', 'sun'): """# \u260c Conjonction Lune - Soleil
**En une phrase :** Une harmonie entre le conscient et l'inconscient qui cree une personnalite unifiee.

## L'energie de cet aspect
La conjonction Lune-Soleil fusionne l'identite et les emotions. Cette configuration donne une forte coherence interne mais peut manquer d'objectivite sur soi. Tu ressens et agis de facon alignee.

## Ton potentiel
Tu possedes une integrite naturelle et une capacite a agir selon tes valeurs profondes.

## Ton defi
Le manque de recul sur toi-meme peut creer des angles morts. Tu peux projeter tes besoins sur les autres.

## Conseil pratique
Cherche des miroirs exterieurs pour gagner en objectivite. Accueille les perspectives differentes.""",

    ('moon', 'uranus'): """# \u260c Conjonction Lune - Uranus
**En une phrase :** Des emotions libres et imprevisibles qui refusent les schemas emotionnels conventionnels.

## L'energie de cet aspect
La conjonction Lune-Uranus electrifie la vie emotionnelle. Cette configuration donne des besoins d'independance affective et des reactions emotionnelles inattendues. Tu ne supportes pas les routines emotionnelles.

## Ton potentiel
Tu offres une fraicheur emotionnelle unique et une capacite a liberer les autres de leurs conditionnements.

## Ton defi
L'instabilite emotionnelle et la difficulte a s'engager durablement peuvent creer de l'insecurite.

## Conseil pratique
Trouve des partenaires qui apprecient ton originalite. Cree de la stabilite a ta facon.""",

    ('moon', 'venus'): """# \u260c Conjonction Lune - Venus
**En une phrase :** Une douceur naturelle qui attire l'amour et cree l'harmonie autour de soi.

## L'energie de cet aspect
La conjonction Lune-Venus harmonise les besoins emotionnels et les valeurs relationnelles. Cette configuration donne un besoin d'harmonie et de beaute dans la vie quotidienne. Tu sais creer un environnement agreable.

## Ton potentiel
Tu possedes un charme naturel et une capacite a attirer l'affection. Les relations te nourrissent.

## Ton defi
La dependance affective et l'evitement des conflits peuvent devenir problematiques.

## Conseil pratique
Cultive l'autonomie emotionnelle. Ose exprimer tes besoins meme s'ils creent des tensions.""",
}

async def insert_interpretations():
    """Insere les interpretations conjonction part 2 en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (planet1, planet2), content in CONJUNCTION_PART2.items():
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
