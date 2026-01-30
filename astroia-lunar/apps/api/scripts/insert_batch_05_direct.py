#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 5 en base de données (version=5)
Généré manuellement - Paires: sun-uranus (5 aspects) + sun-neptune (5 aspects)
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

# Les 10 aspects du Batch 5
ASPECTS = [
    # === SUN-URANUS (5 aspects) ===
    {
        "planet1": "sun",
        "planet2": "uranus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Soleil - Uranus

**En une phrase :** Tu ne peux plus faire semblant — ton besoin de liberté explose

## L'énergie de cet aspect

Ton identité profonde (Soleil) fusionne avec ton besoin de rupture (Uranus) ce mois-ci. Tout ce qui te bride devient insupportable. Tu as envie de casser les codes, de te réinventer, de vivre selon tes propres règles.

## Manifestations concrètes

- **Changements soudains** : Tu prends des décisions radicales que personne ne voit venir
- **Authenticité brute** : Tu montres qui tu es vraiment, sans filtre ni compromis
- **Créativité électrique** : Tes idées sont originales, décalées, parfois géniales

## Conseil pratique

Initie un changement que tu repousses depuis trop longtemps — tu as l'énergie pour briser les chaînes.

## Attention

Gare à tout casser par principe — la liberté ne veut pas dire détruire ce qui fonctionne."""
    },
    {
        "planet1": "sun",
        "planet2": "uranus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Soleil - Uranus

**En une phrase :** Stabilité ou liberté ? Tu es tiraillé entre les deux

## L'énergie de cet aspect

Ton besoin de cohérence (Soleil) et ton désir de rupture (Uranus) se font face ce mois-ci. Une partie de toi veut avancer sur ses rails, l'autre veut tout dérailler. Les tensions surgissent entre ce que tu es et ce que tu pourrais devenir.

## Manifestations concrètes

- **Instabilité émotionnelle** : Tu passes de l'ennui à l'excitation sans transition
- **Rébellion inattendue** : Tu résistes à ce qu'on attend de toi, même si c'était ton plan
- **Opportunités déstabilisantes** : Des possibilités surgissent qui remettent tout en question

## Conseil pratique

Ne choisis pas entre stabilité et changement — trouve comment intégrer les deux dans ta vie.

## Attention

Attention à saboter ta sécurité juste pour sentir l'adrénaline — la liberté a besoin de fondations."""
    },
    {
        "planet1": "sun",
        "planet2": "uranus",
        "aspect_type": "square",
        "content": """# □ Carré Soleil - Uranus

**En une phrase :** Tu veux briser tes chaînes mais tu ne sais pas lesquelles

## L'énergie de cet aspect

Ton identité (Soleil) entre en friction avec ton besoin d'indépendance (Uranus) ce mois-ci. Tu te sens coincé, mais tu ne sais pas vraiment de quoi tu veux te libérer. Cette frustration crée de l'agitation, de l'impatience, parfois de la colère.

## Manifestations concrètes

- **Agitation constante** : Tu ne tiens plus en place, tout t'irrite
- **Décisions impulsives** : Tu changes d'avis brutalement pour le simple plaisir du changement
- **Conflits avec l'autorité** : Tu te rebelles contre les règles, même celles que tu as choisies

## Conseil pratique

Identifie une vraie contrainte qui t'étouffe et agis dessus — ne te bats pas contre des fantômes.

## Attention

Gare à la rébellion gratuite — parfois tu luttes juste parce que tu t'ennuies."""
    },
    {
        "planet1": "sun",
        "planet2": "uranus",
        "aspect_type": "trine",
        "content": """# △ Trigone Soleil - Uranus

**En une phrase :** Ta liberté devient ton style — tu inventes ta propre voie

## L'énergie de cet aspect

Ton essence (Soleil) et ton génie créatif (Uranus) s'harmonisent ce mois-ci. Tu te sens libre d'être toi-même sans avoir à te battre pour ça. Ton originalité devient naturelle, évidente, inspirante pour les autres.

## Manifestations concrètes

- **Authenticité spontanée** : Tu fais à ta manière sans te justifier
- **Innovations faciles** : Tes idées décalées trouvent leur place, les gens adhèrent
- **Indépendance sereine** : Tu n'as besoin de personne pour te sentir entier

## Conseil pratique

Partage une idée que tu gardais secrète par peur d'être trop différent — c'est le bon moment.

## Attention

Attention à l'isolement — ton indépendance peut te couper des autres si tu pousses trop loin."""
    },
    {
        "planet1": "sun",
        "planet2": "uranus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Soleil - Uranus

**En une phrase :** Tu respires mieux — de petites libertés ouvrent de grandes portes

## L'énergie de cet aspect

Ton identité (Soleil) et ton besoin d'espace (Uranus) se stimulent doucement ce mois-ci. Tu découvres qu'être toi-même passe par de petites audaces. Chaque liberté gagnée te rapproche de qui tu veux vraiment être.

## Manifestations concrètes

- **Expérimentations légères** : Tu tentes des trucs nouveaux sans pression
- **Réseau stimulant** : Tu rencontres des gens décalés qui t'inspirent
- **Flexibilité assumée** : Tu changes de plan sans culpabiliser

## Conseil pratique

Fais une chose différente cette semaine — prends un autre chemin, dis oui à l'inattendu.

## Attention

Gare à la dispersion — trop de nouveautés peuvent t'empêcher de creuser vraiment."""
    },

    # === SUN-NEPTUNE (5 aspects) ===
    {
        "planet1": "sun",
        "planet2": "neptune",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Soleil - Neptune

**En une phrase :** Tes contours se dissolvent — tu deviens perméable à l'invisible

## L'énergie de cet aspect

Ton identité (Soleil) fusionne avec l'imaginaire (Neptune) ce mois-ci. Tes frontières deviennent floues. Tu ressens tout intensément, comme si tu absorbais les émotions du monde. Ta sensibilité est à son maximum, ton intuition aussi.

## Manifestations concrètes

- **Sensibilité extrême** : Tu captes les non-dits, les ambiances, parfois trop
- **Créativité visionnaire** : Tes idées sont poétiques, ton art touche l'âme
- **Confusion identitaire** : Tu ne sais plus toujours où tu commences et où les autres finissent

## Conseil pratique

Crée quelque chose de tes rêves, de tes visions — c'est le moment de donner forme à l'invisible.

## Attention

Gare à te perdre dans les autres ou dans l'illusion — garde un pied dans le réel."""
    },
    {
        "planet1": "sun",
        "planet2": "neptune",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Soleil - Neptune

**En une phrase :** Rêve ou réalité ? Tu ne sais plus trop où tu en es

## L'énergie de cet aspect

Ton besoin de clarté (Soleil) et ton attirance pour le flou (Neptune) s'opposent ce mois-ci. D'un côté tu veux être lucide, de l'autre tu préfères le rêve. Cette tension crée de la confusion sur ce que tu veux vraiment.

## Manifestations concrètes

- **Illusions persistantes** : Tu idéalises des situations ou des gens qui ne sont pas ce qu'ils semblent
- **Fatigue inexpliquée** : Ton énergie se dilue, tu te sens vidé sans raison
- **Fuite dans l'imaginaire** : Tu préfères rêver ta vie plutôt que la vivre

## Conseil pratique

Ancre-toi dans le concret — fais une liste de ce qui est réel vs ce que tu imagines.

## Attention

Attention aux fuites (alcool, écrans, substances) — Neptune te tend des échappatoires tentantes."""
    },
    {
        "planet1": "sun",
        "planet2": "neptune",
        "aspect_type": "square",
        "content": """# □ Carré Soleil - Neptune

**En une phrase :** Tu te mens à toi-même — la vérité fait peur

## L'énergie de cet aspect

Ta volonté (Soleil) se heurte à ton besoin d'illusion (Neptune) ce mois-ci. Quand la réalité devient trop dure, tu la floutes. Mais cette stratégie crée plus de problèmes qu'elle n'en résout. Tu te sens perdu, désillusionné, peut-être même trahi.

## Manifestations concrètes

- **Déceptions répétées** : Ce que tu croyais vrai s'effondre, les masques tombent
- **Victimisation** : Tu te sens impuissant face aux événements, comme emporté par le courant
- **Évitement constant** : Tu fuis les confrontations, tu dis oui quand tu penses non

## Conseil pratique

Nomme une illusion que tu entretiens — écris-la, puis écris la vérité en face.

## Attention

Gare à la fuite — Neptune te propose l'oubli mais ce n'est pas une solution."""
    },
    {
        "planet1": "sun",
        "planet2": "neptune",
        "aspect_type": "trine",
        "content": """# △ Trigone Soleil - Neptune

**En une phrase :** Ton imaginaire te nourrit — tu crées de la beauté sans effort

## L'énergie de cet aspect

Ton essence (Soleil) et ton monde intérieur (Neptune) coulent ensemble ce mois-ci. Ta sensibilité devient un don, ta perméabilité une force. Tu captes des choses que les autres ne voient pas, et tu les transmets avec grâce.

## Manifestations concrètes

- **Créativité fluide** : Tes projets artistiques s'imposent d'eux-mêmes, comme canalisés
- **Compassion naturelle** : Tu ressens ce que vivent les autres sans qu'ils aient à parler
- **Spiritualité douce** : Tu te connectes à quelque chose de plus grand sans forcer

## Conseil pratique

Offre ton art, ton écoute, ta présence — ce que tu donnes maintenant touche profondément.

## Attention

Attention à négliger le quotidien — Neptune peut te faire oublier les factures et les responsabilités."""
    },
    {
        "planet1": "sun",
        "planet2": "neptune",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Soleil - Neptune

**En une phrase :** Ton intuition murmure — elle guide tes choix sans bruit

## L'énergie de cet aspect

Ton identité (Soleil) et ton intuition (Neptune) se complètent ce mois-ci. Tu sens les choses avant de les comprendre. Tes rêves te parlent. Ta créativité trouve des canaux d'expression doux et accessibles.

## Manifestations concrètes

- **Synchronicités fréquentes** : Des signes apparaissent au bon moment, tu tombes sur les bonnes personnes
- **Art accessible** : Tu exprimes ta sensibilité sans te perdre dedans
- **Empathie mesurée** : Tu ressens les autres sans t'oublier

## Conseil pratique

Note tes rêves au réveil cette semaine — ils contiennent des messages pour toi.

## Attention

Gare à trop attendre des signes — Neptune peut te faire procrastiner au nom de l'intuition."""
    }
]


async def insert_batch_05():
    """Insère les 10 aspects du Batch 5 en base de données."""

    print(f"=== Insertion Batch 5 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_05())
