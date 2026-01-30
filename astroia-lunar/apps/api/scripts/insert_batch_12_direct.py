#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 12 en base de données (version=5)
Généré manuellement - Paires: mars-saturn (5 aspects) + mars-uranus (5 aspects)
"""

import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.dialects.postgresql import insert
from models.pregenerated_natal_aspect import PregeneratedNatalAspect
from config import Settings

settings = Settings()

# Les 10 aspects du Batch 12
ASPECTS = [
    # === MARS-SATURN (5 aspects) ===
    {
        "planet1": "mars",
        "planet2": "saturn",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mars - Saturne

**En une phrase :** Ton élan rencontre un mur — tu avances mais c'est dur, lent, lourd

## L'énergie de cet aspect

Ton action (Mars) fusionne avec tes limites (Saturne) ce mois-ci. Chaque effort demande le double d'énergie. Tu veux avancer mais tout semble t'en empêcher. Cette combinaison crée de la discipline, mais aussi de la frustration.

## Manifestations concrètes

- **Efforts doubles** : Tu travailles dur pour des résultats modestes
- **Discipline forcée** : Tu te contrôles, tu te retiens, tu te forces
- **Patience obligée** : Les choses prennent du temps, tu ne peux pas accélérer

## Conseil pratique

Transforme une contrainte en structure — utilise la résistance pour construire quelque chose de solide.

## Attention

Gare à la résignation — Saturne peut transformer ton élan en fatalisme si tu baisses les bras."""
    },
    {
        "planet1": "mars",
        "planet2": "saturn",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mars - Saturne

**En une phrase :** Tu veux foncer mais tout te freine — la rage monte

## L'énergie de cet aspect

Ton désir d'agir (Mars) s'oppose à des blocages (Saturne) ce mois-ci. Chaque fois que tu veux avancer, quelque chose te stoppe. Cette tension crée de la colère, de l'impuissance, parfois de la violence.

## Manifestations concrètes

- **Blocages externes** : Les autres, les circonstances, la vie te ralentissent
- **Colère contenue** : Tu ravales ta rage, elle te ronge de l'intérieur
- **Conflits d'autorité** : Tu te bats contre ceux qui ont le pouvoir de te limiter

## Conseil pratique

Identifie une vraie limite à repousser — canalise ta rage vers une action utile.

## Attention

Attention à la violence — contenue ou exprimée, Mars-Saturne peut détruire."""
    },
    {
        "planet1": "mars",
        "planet2": "saturn",
        "aspect_type": "square",
        "content": """# □ Carré Mars - Saturne

**En une phrase :** Tu sabotes ton propre élan — tu veux avancer mais tu te freines toi-même

## L'énergie de cet aspect

Ton action (Mars) entre en conflit avec ta peur (Saturne) ce mois-ci. Tu te lances, puis tu t'arrêtes. Tu oses, puis tu recules. Cette guerre intérieure crée de l'autodestruction, de la paralysie.

## Manifestations concrètes

- **Auto-sabotage** : Tu commences des projets et tu les abandonnes par peur
- **Colère implosive** : Ta rage se retourne contre toi, tu te punis
- **Inhibition chronique** : Tu n'oses plus rien par peur d'échouer

## Conseil pratique

Fais une petite action qui te fait peur chaque jour — reprends le pouvoir sur ta paralysie.

## Attention

Gare à la dépression — Mars bloqué par Saturne peut créer une rage qui se retourne en tristesse."""
    },
    {
        "planet1": "mars",
        "planet2": "saturn",
        "aspect_type": "trine",
        "content": """# △ Trigone Mars - Saturne

**En une phrase :** Ta discipline devient naturelle — tu construis avec endurance

## L'énergie de cet aspect

Ton action (Mars) et ta structure (Saturne) collaborent ce mois-ci. Tu sais doser tes efforts. Tu avances méthodiquement, sans te brûler. Ta persévérance devient ta force.

## Manifestations concrètes

- **Endurance naturelle** : Tu tiens la distance sur tes projets longs
- **Discipline sobre** : Tu te fixes des limites saines, tu les respectes
- **Résultats durables** : Ce que tu construis maintenant tiendra dans le temps

## Conseil pratique

Engage-toi dans un projet à long terme qui demande de la constance — tu as cette force maintenant.

## Attention

Attention à devenir trop rigide — parfois il faut aussi oser l'imprévu."""
    },
    {
        "planet1": "mars",
        "planet2": "saturn",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mars - Saturne

**En une phrase :** Tu canalises ton énergie — chaque action compte, rien n'est gaspillé

## L'énergie de cet aspect

Ton action (Mars) et ta capacité à structurer (Saturne) se complètent ce mois-ci. Tu n'agis pas au hasard, tu construis. Tes efforts ont du sens, de la direction. Tu es patient et déterminé.

## Manifestations concrètes

- **Actions ciblées** : Tu ne disperses pas ton énergie, tu vises juste
- **Patience active** : Tu acceptes que ça prenne du temps sans renoncer
- **Respect des limites** : Tu connais ta capacité et tu la respectes

## Conseil pratique

Crée un plan d'action réaliste pour un objectif à 6 mois — ta discipline peut tenir la route.

## Attention

Gare à trop te contrôler — parfois il faut aussi lâcher prise et improviser."""
    },

    # === MARS-URANUS (5 aspects) ===
    {
        "planet1": "mars",
        "planet2": "uranus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mars - Uranus

**En une phrase :** Ton élan devient électrique — tu casses tout pour avancer

## L'énergie de cet aspect

Ton action (Mars) fusionne avec ta soif de liberté (Uranus) ce mois-ci. Tu ne supportes plus aucune contrainte. Tes gestes deviennent imprévisibles, parfois violents. Tu veux briser les chaînes, quitte à tout casser.

## Manifestations concrètes

- **Ruptures soudaines** : Tu quittes, tu changes, tu détruis ce qui te bride
- **Gestes impulsifs** : Tu agis sans prévenir, ça surprend tout le monde
- **Innovation audacieuse** : Tu inventes de nouvelles façons de faire, radicales

## Conseil pratique

Canalise cette énergie dans une vraie révolution — personnelle, créative, professionnelle — pas dans la destruction gratuite.

## Attention

Gare aux accidents — Mars-Uranus peut créer des situations dangereuses par excès d'impulsivité."""
    },
    {
        "planet1": "mars",
        "planet2": "uranus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mars - Uranus

**En une phrase :** Tu veux te libérer mais tu ne sais pas de quoi — alors tu détruis au hasard

## L'énergie de cet aspect

Ton désir d'agir (Mars) s'oppose à ton besoin de rupture (Uranus) ce mois-ci. Tu te sens prisonnier mais tu ne sais pas de quoi. Cette tension crée de l'agitation, de la colère, parfois de la violence gratuite.

## Manifestations concrètes

- **Rébellion aveugle** : Tu te bats sans savoir contre quoi
- **Conflits explosifs** : Les tensions éclatent brutalement, de façon imprévisible
- **Instabilité** : Tu changes de direction sans cesse, tu ne tiens rien

## Conseil pratique

Identifie une vraie contrainte qui t'étouffe et agis dessus — ne gaspille pas ton énergie à te battre contre tout.

## Attention

Attention à la violence — Mars-Uranus peut devenir destructeur pour toi ou les autres."""
    },
    {
        "planet1": "mars",
        "planet2": "uranus",
        "aspect_type": "square",
        "content": """# □ Carré Mars - Uranus

**En une phrase :** Tu exploses sans prévenir — ta colère est une bombe à retardement

## L'énergie de cet aspect

Ton agressivité (Mars) entre en friction avec ton besoin d'indépendance (Uranus) ce mois-ci. Tu accumules la pression, puis tu exploses. Tes réactions sont disproportionnées, imprévisibles, parfois dangereuses.

## Manifestations concrètes

- **Colère explosive** : Tu passes de calme à furieux en une seconde
- **Accidents fréquents** : Tu te blesses, tu casses des choses, tu prends des risques stupides
- **Conflits violents** : Tes disputes deviennent physiques ou verbalement destructrices

## Conseil pratique

Trouve un exutoire physique intense — boxe, course, sport extrême — pour évacuer la pression avant qu'elle explose.

## Attention

Gare aux gestes irréversibles — sous le coup de Mars-Uranus, tu peux faire des choses que tu regretteras toute ta vie."""
    },
    {
        "planet1": "mars",
        "planet2": "uranus",
        "aspect_type": "trine",
        "content": """# △ Trigone Mars - Uranus

**En une phrase :** Ton audace devient génie — tu innoves en agissant

## L'énergie de cet aspect

Ton action (Mars) et ton originalité (Uranus) s'harmonisent ce mois-ci. Tu oses des choses que personne n'a tentées. Tes gestes sont créatifs, surprenants, libérateurs. Tu inventes en faisant.

## Manifestations concrètes

- **Innovation naturelle** : Tu trouves des solutions originales en agissant
- **Courage spontané** : Tu oses sans réfléchir, et ça marche
- **Liberté fluide** : Tu te libères sans avoir à tout casser

## Conseil pratique

Lance un projet disruptif, décalé, nouveau — tu as l'audace et la créativité pour le faire aboutir.

## Attention

Attention à l'isolement — ton originalité peut te couper des autres si tu pousses trop loin."""
    },
    {
        "planet1": "mars",
        "planet2": "uranus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mars - Uranus

**En une phrase :** Tu expérimentes avec courage — chaque tentative te libère un peu

## L'énergie de cet aspect

Ton action (Mars) et ton besoin de liberté (Uranus) se stimulent ce mois-ci. Tu testes de nouvelles façons de faire. Tes gestes deviennent plus audacieux, plus authentiques. Tu te libères petit à petit.

## Manifestations concrètes

- **Expérimentations mesurées** : Tu essaies du nouveau sans tout casser
- **Audace progressive** : Tu repousses tes limites un peu chaque jour
- **Libérations ciblées** : Tu identifies ce qui te bride et tu agis dessus

## Conseil pratique

Fais une chose différente cette semaine — change une habitude, ose un geste nouveau.

## Attention

Gare à la dispersion — trop d'expérimentations peuvent t'empêcher de creuser vraiment."""
    }
]


async def insert_batch_12():
    """Insère les 10 aspects du Batch 12 en base de données."""

    print(f"=== Insertion Batch 12 ({len(ASPECTS)} aspects) ===\n")

    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    inserted_count = 0

    async with async_session() as session:
        async with session.begin():
            for aspect in ASPECTS:
                planet1 = aspect['planet1']
                planet2 = aspect['planet2']
                aspect_type = aspect['aspect_type']
                content = aspect['content']

                # Normaliser en ordre alphabétique
                p1_norm = planet1.lower().strip()
                p2_norm = planet2.lower().strip()
                if p1_norm > p2_norm:
                    p1_norm, p2_norm = p2_norm, p1_norm

                # Upsert
                stmt = insert(PregeneratedNatalAspect).values(
                    planet1=p1_norm,
                    planet2=p2_norm,
                    aspect_type=aspect_type.lower(),
                    version=5,
                    lang='fr',
                    content=content,
                    length=len(content)
                )

                stmt = stmt.on_conflict_do_update(
                    index_elements=['planet1', 'planet2', 'aspect_type', 'version', 'lang'],
                    set_={
                        'content': stmt.excluded.content,
                        'length': stmt.excluded.length,
                    }
                )

                await session.execute(stmt)
                inserted_count += 1

                print(f"  ✓ {p1_norm} {aspect_type} {p2_norm}")

    await engine.dispose()

    print(f"\n✅ {inserted_count} aspects insérés (version=5, lang=fr)")

    # Vérifier le total
    await check_total_in_db()


async def check_total_in_db():
    """Vérifie le nombre total d'aspects v5 en BD."""
    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        from sqlalchemy import select, func
        result = await session.execute(
            select(func.count()).select_from(PregeneratedNatalAspect).where(
                PregeneratedNatalAspect.version == 5,
                PregeneratedNatalAspect.lang == 'fr'
            )
        )
        count = result.scalar()

    await engine.dispose()

    print(f"🔍 Vérification BD : {count} aspects version=5 lang=fr")
    print(f"📊 Progression : {count}/130 aspects ({round(count/130*100, 1)}%)")


if __name__ == '__main__':
    asyncio.run(insert_batch_12())
