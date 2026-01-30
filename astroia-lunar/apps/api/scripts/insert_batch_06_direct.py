#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 6 en base de données (version=5)
Généré manuellement - Paires: sun-pluto (5 aspects) + moon-mercury (5 aspects)
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

# Les 10 aspects du Batch 6
ASPECTS = [
    # === SUN-PLUTO (5 aspects) ===
    {
        "planet1": "sun",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Soleil - Pluton

**En une phrase :** Tu touches le fond de toi-même — ta puissance devient terrifiante

## L'énergie de cet aspect

Ton identité (Soleil) fusionne avec ton pouvoir de transformation (Pluton) ce mois-ci. Ce qui était enfoui remonte à la surface. Tu ressens une intensité presque insoutenable. Tout devient une question de vie ou de mort, de vérité ou de mensonge.

## Manifestations concrètes

- **Intensité magnétique** : Les gens te sentent différent, puissant, parfois effrayant
- **Obsessions profondes** : Tu creuses jusqu'à comprendre vraiment, quitte à détruire des illusions
- **Transformation radicale** : Tu lâches qui tu étais pour devenir qui tu dois être

## Conseil pratique

Utilise cette puissance pour détruire une vieille version de toi qui ne sert plus — renaître fait mal mais libère.

## Attention

Gare à vouloir tout contrôler par peur de perdre le pouvoir — Pluton ne se contrôle pas, il se traverse."""
    },
    {
        "planet1": "sun",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Soleil - Pluton

**En une phrase :** Un duel de pouvoir — avec les autres ou avec toi-même

## L'énergie de cet aspect

Ton identité (Soleil) entre en confrontation avec des forces de transformation (Pluton) ce mois-ci. Des luttes de pouvoir émergent. Soit tu résistes à un changement inévitable, soit quelqu'un cherche à te contrôler. La tension est forte, presque violente.

## Manifestations concrètes

- **Conflits de pouvoir** : Des rapports de force surgissent, tu dois défendre ton territoire
- **Manipulations visibles** : Tu vois les jeux de pouvoir que tu ne voyais pas avant
- **Crises identitaires** : Des événements te forcent à lâcher une image de toi

## Conseil pratique

Identifie où tu perds ton pouvoir — reprends-le sans écraser personne, juste en posant tes limites.

## Attention

Attention à devenir ce que tu combats — à force de lutter contre la manipulation, tu peux manipuler aussi."""
    },
    {
        "planet1": "sun",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Soleil - Pluton

**En une phrase :** Tu te bats contre ta propre transformation — ça fait mal

## L'énergie de cet aspect

Ta volonté (Soleil) résiste à ta propre métamorphose (Pluton) ce mois-ci. Une partie de toi sait qu'il faut mourir à quelque chose pour renaître, mais l'autre refuse. Cette guerre intérieure crée de la rage, de la frustration, parfois de l'autodestruction.

## Manifestations concrètes

- **Colère profonde** : Une rage sourde monte sans que tu saches vraiment pourquoi
- **Autodestruction** : Tu sabotes ce qui fonctionne comme pour forcer un changement
- **Obsessions toxiques** : Tu fixes sur ce qui te détruit plutôt que sur ce qui te construit

## Conseil pratique

Demande-toi : qu'est-ce qui doit mourir en moi pour que je puisse avancer ? Puis laisse partir.

## Attention

Gare à retourner ta rage contre toi — Pluton te demande de détruire des patterns, pas toi-même."""
    },
    {
        "planet1": "sun",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Soleil - Pluton

**En une phrase :** Ta transformation est naturelle — tu renais sans te brûler

## L'énergie de cet aspect

Ton essence (Soleil) et ta capacité de renaissance (Pluton) collaborent ce mois-ci. Tu lâches ce qui ne sert plus sans t'y accrocher. Tu trouves du pouvoir dans ta vulnérabilité. Ta transformation est profonde mais fluide.

## Manifestations concrètes

- **Pouvoir personnel** : Tu assumes ton intensité sans la minimiser ni l'imposer
- **Guérison profonde** : Tu touches des blessures anciennes et elles commencent à cicatriser
- **Magnétisme naturel** : Ta présence devient puissante sans effort

## Conseil pratique

Plonge dans ce qui fait peur — tu as la force de traverser tes abysses maintenant.

## Attention

Attention à sous-estimer ton impact — ton intensité peut écraser les autres même si ce n'est pas ton intention."""
    },
    {
        "planet1": "sun",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Soleil - Pluton

**En une phrase :** Tu découvres ta profondeur — couche par couche, tu deviens vrai

## L'énergie de cet aspect

Ton identité (Soleil) et ton pouvoir de transformation (Pluton) se stimulent ce mois-ci. Tu es prêt à voir ce que tu évitais. Les conversations profondes t'attirent. Tu veux comprendre les mécanismes cachés, en toi et autour de toi.

## Manifestations concrètes

- **Introspection fructueuse** : Tu explores tes zones d'ombre sans te perdre
- **Conversations intenses** : Tu creuses les sujets, tu veux aller au fond des choses
- **Libération progressive** : Tu lâches de vieux schémas, un peu chaque jour

## Conseil pratique

Commence une thérapie, un journal intime profond, ou une conversation vraie — tu es prêt à creuser.

## Attention

Gare à l'obsession de la profondeur — parfois la légèreté a aussi sa place."""
    },

    # === MOON-MERCURY (5 aspects) ===
    {
        "planet1": "moon",
        "planet2": "mercury",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Lune - Mercure

**En une phrase :** Tu mets des mots sur tes émotions — ton cœur devient lisible

## L'énergie de cet aspect

Tes émotions (Lune) et ton intellect (Mercure) fusionnent ce mois-ci. Tu comprends ce que tu ressens. Quand quelque chose te touche, tu sais l'expliquer. Tes pensées sont teintées d'émotion, tes émotions passent par les mots.

## Manifestations concrètes

- **Clarté émotionnelle** : Tu identifies tes besoins et tu peux les nommer
- **Communication sensible** : Tu parles de ce qui te touche sans te perdre
- **Mémoire vive** : Les souvenirs remontent, chargés d'émotions précises

## Conseil pratique

Écris ce que tu ressens vraiment — tes mots portent ton cœur maintenant.

## Attention

Gare à trop analyser tes émotions — parfois il faut juste les vivre sans les décortiquer."""
    },
    {
        "planet1": "moon",
        "planet2": "mercury",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Lune - Mercure

**En une phrase :** Ton cœur et ta tête se contredisent — lequel écouter ?

## L'énergie de cet aspect

Ce que tu ressens (Lune) et ce que tu penses (Mercure) se font face ce mois-ci. Tes émotions disent une chose, ta logique une autre. Cette tension crée de la confusion, des hésitations, parfois des malentendus dans les échanges.

## Manifestations concrètes

- **Messages brouillés** : Tu dis une chose mais tu en ressens une autre
- **Suranalyse émotionnelle** : Tu réfléchis tellement à ce que tu ressens que tu ne le ressens plus
- **Incompréhension mutuelle** : Les autres ne comprennent pas tes émotions, ou toi les leurs

## Conseil pratique

Laisse de l'espace entre ce que tu ressens et ce que tu en dis — l'émotion n'a pas toujours besoin d'explication.

## Attention

Attention à rationaliser tes besoins au point de les nier — ta logique peut étouffer ton cœur."""
    },
    {
        "planet1": "moon",
        "planet2": "mercury",
        "aspect_type": "square",
        "content": """# □ Carré Lune - Mercure

**En une phrase :** Tes mots trahissent tes émotions — tu te sens incompris

## L'énergie de cet aspect

Tes émotions (Lune) et ta communication (Mercure) s'entrechoquent ce mois-ci. Quand tu parles, ça sort mal. Quand tu ressens quelque chose, tu ne trouves pas les mots. Cette friction crée de la frustration, des malentendus, parfois des disputes.

## Manifestations concrètes

- **Maladresses verbales** : Tu dis l'inverse de ce que tu voulais dire
- **Émotions réprimées** : Tu ne sais pas exprimer ce qui te fait mal, alors ça sort de travers
- **Agacement facile** : Les petites remarques te blessent plus que d'habitude

## Conseil pratique

Prends trois respirations avant de répondre quand tu es touché — laisse l'émotion se calmer avant de parler.

## Attention

Gare aux mots qui blessent — sous le coup de l'émotion, tu peux dire des choses que tu regretteras."""
    },
    {
        "planet1": "moon",
        "planet2": "mercury",
        "aspect_type": "trine",
        "content": """# △ Trigone Lune - Mercure

**En une phrase :** Tes émotions s'expriment avec grâce — tu te fais comprendre sans forcer

## L'énergie de cet aspect

Tes émotions (Lune) et ta communication (Mercure) coulent ensemble ce mois-ci. Quand tu parles de ce que tu ressens, c'est fluide. Les gens comprennent ton cœur. Tes mots apaisent, éclairent, connectent.

## Manifestations concrètes

- **Écoute empathique** : Tu comprends ce que les autres ressentent sans qu'ils aient besoin de tout dire
- **Écriture libératrice** : Si tu écris, les mots coulent et touchent juste
- **Dialogues apaisants** : Tes conversations créent du lien, même sur des sujets sensibles

## Conseil pratique

Initie une conversation vraie avec quelqu'un qui compte — tu as les mots pour créer du lien.

## Attention

Attention à trop parler de tes émotions — parfois il faut aussi les garder pour toi."""
    },
    {
        "planet1": "moon",
        "planet2": "mercury",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Lune - Mercure

**En une phrase :** Tes mots portent ton cœur — tu exprimes ce qui compte vraiment

## L'énergie de cet aspect

Tes émotions (Lune) et ton intellect (Mercure) se complètent ce mois-ci. Tu arrives à parler de ce qui te touche sans te noyer dedans. Tes pensées accueillent tes sentiments. Tu peux nommer tes besoins avec douceur.

## Manifestations concrètes

- **Clarifications utiles** : Tu mets des mots sur des ressentis flous, ça apaise
- **Conversations nécessaires** : Tu oses dire ce qui doit être dit, avec tact
- **Apprentissages émotionnels** : Tu comprends mieux comment tu fonctionnes

## Conseil pratique

Tiens un journal cette semaine — écris ce que tu ressens, tu vas découvrir des choses sur toi.

## Attention

Gare à intellectualiser ce qui devrait rester simple — toutes les émotions n'ont pas besoin d'être expliquées."""
    }
]


async def insert_batch_06():
    """Insère les 10 aspects du Batch 6 en base de données."""

    print(f"=== Insertion Batch 6 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_06())
