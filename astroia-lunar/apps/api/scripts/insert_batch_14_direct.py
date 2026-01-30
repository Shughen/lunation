#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 14 en base de données (version=5)
Généré manuellement - Paires: jupiter-saturn (5 aspects) + saturn-neptune (5 aspects)
**DERNIER BATCH FINAL** - 130/130 aspects complétés !
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

# Les 10 derniers aspects du Batch 14
ASPECTS = [
    # === JUPITER-SATURN (5 aspects) ===
    {
        "planet1": "jupiter",
        "planet2": "saturn",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Jupiter - Saturne

**En une phrase :** Ton rêve rencontre le réel — tu construis ce qui dure

## L'énergie de cet aspect

Ton optimisme (Jupiter) fusionne avec ta structure (Saturne) ce mois-ci. Tu ne rêves plus sans agir, tu n'agis plus sans vision. Tes projets deviennent solides, ancrés, réalistes. Tu bâtis pour le long terme.

## Manifestations concrètes

- **Ambitions réalistes** : Tu vises haut mais avec un plan concret
- **Discipline inspirée** : Tes efforts ont du sens, tu sais pourquoi tu construis
- **Projets durables** : Ce que tu lances maintenant tiendra dans le temps

## Conseil pratique

Lance un projet à long terme qui te passionne — tu as la vision et la structure maintenant.

## Attention

Gare à devenir trop sérieux — garde ta capacité à rêver même en construisant."""
    },
    {
        "planet1": "jupiter",
        "planet2": "saturn",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Jupiter - Saturne

**En une phrase :** Ton rêve bute contre tes limites — frustration garantie

## L'énergie de cet aspect

Ton désir d'expansion (Jupiter) s'oppose à tes contraintes (Saturne) ce mois-ci. Tu veux grandir mais tout te freine. Tes ambitions rencontrent la dure réalité. Cette tension crée du découragement, parfois de la résignation.

## Manifestations concrètes

- **Projets bloqués** : Tes plans butent sur des obstacles concrets
- **Pessimisme croissant** : Tu perds foi en tes capacités
- **Conflits internes** : Une part de toi veut oser, l'autre veut se protéger

## Conseil pratique

Identifie une limite réelle et trouve un moyen créatif de la contourner — ne la subis pas.

## Attention

Attention à la résignation — Saturne peut te faire abandonner tes rêves légitimes."""
    },
    {
        "planet1": "jupiter",
        "planet2": "saturn",
        "aspect_type": "square",
        "content": """# □ Carré Jupiter - Saturne

**En une phrase :** Tu veux tout et tu n'oses rien — paralysie par conflit interne

## L'énergie de cet aspect

Ton optimisme (Jupiter) entre en conflit avec ta peur (Saturne) ce mois-ci. Tu te sens tiraillé entre l'envie de foncer et la peur d'échouer. Cette guerre intérieure crée de l'immobilisme, parfois de l'amertume.

## Manifestations concrètes

- **Immobilisme** : Tu ne lances rien par peur que ça ne marche pas
- **Frustration chronique** : Tu sais ce que tu veux mais tu ne passes pas à l'acte
- **Autodestruction** : Tu sabotes tes projets avant qu'ils échouent

## Conseil pratique

Fais un petit pas vers ton rêve — prouve à Saturne que l'échec ne tue pas.

## Attention

Gare à la prophétie auto-réalisatrice — à force de ne rien tenter, tu garantis l'échec."""
    },
    {
        "planet1": "jupiter",
        "planet2": "saturn",
        "aspect_type": "trine",
        "content": """# △ Trigone Jupiter - Saturne

**En une phrase :** Ton rêve se construit — patience et foi s'allient

## L'énergie de cet aspect

Ton optimisme (Jupiter) et ta structure (Saturne) collaborent ce mois-ci. Tu crois en tes projets ET tu sais comment les bâtir. Tu as la vision à long terme et l'endurance pour tenir. C'est l'équilibre parfait.

## Manifestations concrètes

- **Réalisations durables** : Ce que tu construis maintenant durera
- **Sagesse pragmatique** : Tu rêves sans illusions, tu construis sans cynisme
- **Patience confiante** : Tu sais que ça prendra du temps et tu es ok avec ça

## Conseil pratique

Engage-toi dans un projet sur 5 ans — tu as la maturité et la foi pour le mener au bout.

## Attention

Attention à devenir trop prudent — parfois il faut aussi oser l'imprévu."""
    },
    {
        "planet1": "jupiter",
        "planet2": "saturn",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Jupiter - Saturne

**En une phrase :** Tu grandis avec méthode — chaque étape compte

## L'énergie de cet aspect

Ton besoin de sens (Jupiter) et ta capacité à structurer (Saturne) se complètent ce mois-ci. Tu construis tes rêves étape par étape. Chaque effort te rapproche de ta vision. Tu as la patience active.

## Manifestations concrètes

- **Projets progressifs** : Tu avances régulièrement, sans brûler les étapes
- **Ambitions mesurées** : Tu vises haut mais de façon réaliste
- **Succès lents** : Tes réussites prennent du temps mais elles sont solides

## Conseil pratique

Crée un plan d'action sur 1 an pour un objectif qui compte — ta discipline peut tenir la distance.

## Attention

Gare à l'excès de prudence — parfois il faut aussi oser le saut dans le vide."""
    },

    # === SATURN-NEPTUNE (5 aspects) ===
    {
        "planet1": "saturn",
        "planet2": "neptune",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Saturne - Neptune

**En une phrase :** Ton rêve se solidifie ou ta structure se dissout — tu ne sais plus

## L'énergie de cet aspect

Ta structure (Saturne) fusionne avec ton imaginaire (Neptune) ce mois-ci. Soit tu donnes forme à tes rêves, soit tes limites se dissolvent dans le flou. Cette fusion crée de la confusion, parfois de la désillusion.

## Manifestations concrètes

- **Rêves réalistes** : Tu arrives à matérialiser ce qui semblait impossible
- **Structures floues** : Tes limites deviennent poreuses, tu ne sais plus où tu en es
- **Désillusion constructive** : Ce que tu croyais solide s'effondre, mais ça ouvre une porte

## Conseil pratique

Donne une forme concrète à un rêve — un dessin, un plan, une première action — sors-le du flou.

## Attention

Gare à la résignation spirituelle — Neptune peut te faire accepter l'inacceptable au nom du lâcher-prise."""
    },
    {
        "planet1": "saturn",
        "planet2": "neptune",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Saturne - Neptune

**En une phrase :** Le réel contre le rêve — tu dois choisir ou tout perdre

## L'énergie de cet aspect

Ta responsabilité (Saturne) s'oppose à ton besoin d'évasion (Neptune) ce mois-ci. Une part de toi veut tenir ses engagements, l'autre veut tout fuir. Cette tension crée de la culpabilité, parfois de la fuite dans l'illusion.

## Manifestations concrètes

- **Fuites addictives** : Tu échappes à tes responsabilités via l'alcool, les écrans, les rêveries
- **Culpabilité paralysante** : Tu te sens coupable de vouloir rêver
- **Désillusions brutales** : Tes illusions s'effondrent face à la dure réalité

## Conseil pratique

Accepte que le rêve et le réel ne s'opposent pas — trouve comment rêver en construisant.

## Attention

Attention aux fuites — Neptune peut te faire éviter tes responsabilités jusqu'à ce qu'elles explosent."""
    },
    {
        "planet1": "saturn",
        "planet2": "neptune",
        "aspect_type": "square",
        "content": """# □ Carré Saturne - Neptune

**En une phrase :** Ta peur paralyse ton rêve — ou ton rêve sabote ta structure

## L'énergie de cet aspect

Ta peur (Saturne) entre en conflit avec ton besoin d'illusion (Neptune) ce mois-ci. Soit tu renonces à tes rêves par peur, soit tu te mens à toi-même pour ne pas voir la réalité. Les deux créent de la souffrance.

## Manifestations concrètes

- **Rêves abandonnés** : Tu tues tes rêves avant même d'essayer
- **Illusions persistantes** : Tu te mens sur ta situation pour ne pas affronter la vérité
- **Dépression voilée** : Tu te sens vide, perdu, sans savoir pourquoi

## Conseil pratique

Nomme un rêve que tu as abandonné par peur — puis demande-toi : qu'est-ce que je risque vraiment ?

## Attention

Gare à la victimisation — Neptune peut te faire croire que tu es impuissant alors que tu as du pouvoir."""
    },
    {
        "planet1": "saturn",
        "planet2": "neptune",
        "aspect_type": "trine",
        "content": """# △ Trigone Saturne - Neptune

**En une phrase :** Tu matérialises le subtil — tes rêves prennent forme avec grâce

## L'énergie de cet aspect

Ta structure (Saturne) et ton imaginaire (Neptune) s'harmonisent ce mois-ci. Tu arrives à donner forme à ce qui était flou. Tes rêves deviennent projets, tes intuitions deviennent méthodes. C'est l'alchimie parfaite.

## Manifestations concrètes

- **Rêves concrétisés** : Ce que tu imaginais se matérialise naturellement
- **Discipline inspirée** : Tu structures ton art, ta spiritualité, ta créativité
- **Réalisme sans cynisme** : Tu vois la réalité sans perdre ta capacité à rêver

## Conseil pratique

Transforme un rêve en plan d'action — tu as la capacité de rendre réel ce qui semblait impossible.

## Attention

Attention à négliger le quotidien — Neptune peut te faire oublier les responsabilités concrètes."""
    },
    {
        "planet1": "saturn",
        "planet2": "neptune",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Saturne - Neptune

**En une phrase :** Tu construis avec sensibilité — chaque limite peut être poétique

## L'énergie de cet aspect

Ta capacité à structurer (Saturne) et ton imaginaire (Neptune) se complètent ce mois-ci. Tu donnes forme à tes intuitions. Tes limites deviennent des cadres créatifs. Tu bâtis avec âme.

## Manifestations concrètes

- **Créativité structurée** : Ton art trouve sa forme, ta spiritualité trouve sa pratique
- **Limites douces** : Tu poses des frontières sans fermer ton cœur
- **Projets inspirés** : Ce que tu construis a du sens au-delà du concret

## Conseil pratique

Crée un rituel quotidien qui nourrit ton âme — méditation, art, écriture — et tiens-le sur la durée.

## Attention

Gare à l'isolement — Neptune peut te faire fuir les autres au nom de la spiritualité."""
    }
]


async def insert_batch_14():
    """Insère les 10 derniers aspects du Batch 14 en base de données."""

    print(f"=== Insertion Batch 14 - DERNIER BATCH FINAL ({len(ASPECTS)} aspects) ===\n")

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

    if count >= 130:
        print(f"\n🎉🎉🎉 TOUS LES 130 ASPECTS SONT GÉNÉRÉS ET INSÉRÉS ! 🎉🎉🎉")
        print(f"✨ Refonte aspects v5 COMPLÈTE - $0 USD dépensé ✨")


if __name__ == '__main__':
    asyncio.run(insert_batch_14())
