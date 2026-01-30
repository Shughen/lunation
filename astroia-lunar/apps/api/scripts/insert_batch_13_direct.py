#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 13 en base de données (version=5)
Généré manuellement - Paires: mercury-jupiter (5 aspects) + mercury-saturn (5 aspects)
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

# Les 10 aspects du Batch 13
ASPECTS = [
    # === MERCURY-JUPITER (5 aspects) ===
    {
        "planet1": "mercury",
        "planet2": "jupiter",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mercure - Jupiter

**En une phrase :** Ton esprit s'élargit — tu penses grand, tu vois loin

## L'énergie de cet aspect

Ton intellect (Mercure) fusionne avec ton optimisme (Jupiter) ce mois-ci. Tu ne penses plus en petit. Tes idées deviennent grandes, généreuses, inspirantes. Tu veux apprendre, comprendre, enseigner.

## Manifestations concrètes

- **Curiosité expansive** : Tu veux tout savoir, tout comprendre
- **Communication inspirante** : Tes mots portent une vision, ils élèvent
- **Apprentissages profonds** : Ce que tu apprends fait sens, ça te nourrit

## Conseil pratique

Partage une idée qui te passionne — écris, enseigne, parle — ton esprit rayonne maintenant.

## Attention

Gare à l'arrogance intellectuelle — savoir beaucoup ne te rend pas supérieur."""
    },
    {
        "planet1": "mercury",
        "planet2": "jupiter",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mercure - Jupiter

**En une phrase :** Tu te perds dans les détails ou tu survoles tout — jamais d'équilibre

## L'énergie de cet aspect

Ton besoin de précision (Mercure) s'oppose à ta vision globale (Jupiter) ce mois-ci. Soit tu te noies dans les détails, soit tu survoles sans approfondir. Cette tension crée de la confusion, parfois de l'arrogance.

## Manifestations concrètes

- **Sur-analyse** : Tu compliques ce qui est simple par excès de réflexion
- **Survol superficiel** : Tu penses comprendre mais tu passes à côté de l'essentiel
- **Dogmatisme** : Tu crois détenir la vérité, tu ne remets plus rien en question

## Conseil pratique

Alterne entre zoom et dézoom — regarde le détail puis prends du recul, l'un nourrit l'autre.

## Attention

Attention au syndrome de l'imposteur ou à son inverse — l'arrogance — les deux cachent le même doute."""
    },
    {
        "planet1": "mercury",
        "planet2": "jupiter",
        "aspect_type": "square",
        "content": """# □ Carré Mercure - Jupiter

**En une phrase :** Tu promets trop, tu parles trop — tes mots dépassent ta pensée

## L'énergie de cet aspect

Ton intellect (Mercure) se frotte à ton optimisme (Jupiter) ce mois-ci. Tu t'engages sans réfléchir, tu promets sans mesurer. Tes idées sont grandes mais floues. Cette friction crée des malentendus, des déceptions.

## Manifestations concrètes

- **Promesses excessives** : Tu t'engages intellectuellement dans trop de choses
- **Discours creux** : Tu parles beaucoup mais tu dis peu
- **Sur-confiance mentale** : Tu crois tout comprendre, tu ne vérifies plus tes infos

## Conseil pratique

Avant de t'engager intellectuellement, demande-toi si tu peux vraiment tenir — mieux vaut un oui solide qu'un oui vague.

## Attention

Gare au bullshit — Jupiter-Mercure peut te faire croire que tu sais alors que tu ne fais que brasser de l'air."""
    },
    {
        "planet1": "mercury",
        "planet2": "jupiter",
        "aspect_type": "trine",
        "content": """# △ Trigone Mercure - Jupiter

**En une phrase :** Ton intelligence devient sagesse — tu comprends et tu transmets avec grâce

## L'énergie de cet aspect

Ton intellect (Mercure) et ta vision (Jupiter) collaborent ce mois-ci. Tu penses clairement et largement. Tes idées ont du fond et de la forme. Tu apprends facilement, tu enseignes naturellement.

## Manifestations concrètes

- **Compréhension fluide** : Les concepts complexes deviennent évidents
- **Communication claire** : Tu expliques simplement ce qui est compliqué
- **Optimisme intelligent** : Tu vois les possibilités sans nier les obstacles

## Conseil pratique

Écris ce que tu sais — un article, un livre, un cours — ton esprit peut éclairer les autres.

## Attention

Attention à tenir ton intelligence pour acquise — continue à apprendre, même si ça vient facilement."""
    },
    {
        "planet1": "mercury",
        "planet2": "jupiter",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mercure - Jupiter

**En une phrase :** Tu apprends avec joie — chaque idée t'ouvre une porte

## L'énergie de cet aspect

Ton intellect (Mercure) et ton besoin de sens (Jupiter) se stimulent ce mois-ci. Tu cherches à comprendre pourquoi, pas juste comment. Tes apprentissages deviennent des quêtes, tes idées des chemins.

## Manifestations concrètes

- **Curiosité profonde** : Tu veux comprendre le sens, pas juste les faits
- **Conversations enrichissantes** : Les échanges te font grandir intellectuellement
- **Synthèses élégantes** : Tu relies les idées entre elles, tu vois les patterns

## Conseil pratique

Explore une philosophie, une théorie, un domaine nouveau — ton esprit a faim de sens.

## Attention

Gare à l'abstraction excessive — parfois il faut aussi revenir au concret."""
    },

    # === MERCURY-SATURN (5 aspects) ===
    {
        "planet1": "mercury",
        "planet2": "saturn",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mercure - Saturne

**En une phrase :** Ton esprit devient sérieux — tu penses avec rigueur, parfois avec lourdeur

## L'énergie de cet aspect

Ton intellect (Mercure) fusionne avec ta structure (Saturne) ce mois-ci. Tes pensées deviennent plus lentes, plus profondes, plus sombres. Tu analyses tout avec pessimisme. Ta communication devient difficile, retenue.

## Manifestations concrètes

- **Pensées lourdes** : Ton esprit rumine, tourne en boucle sur ce qui ne va pas
- **Communication bloquée** : Tu as du mal à parler, les mots ne sortent pas
- **Rigueur excessive** : Tu te critiques mentalement, tu doutes de tout

## Conseil pratique

Écris tes pensées sombres sur papier — sortir les mots de ta tête les allège.

## Attention

Gare à la rumination dépressive — Saturne peut transformer la réflexion en prison mentale."""
    },
    {
        "planet1": "mercury",
        "planet2": "saturn",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mercure - Saturne

**En une phrase :** Ta tête te dit non — chaque idée se heurte à un mur de doutes

## L'énergie de cet aspect

Ton esprit (Mercure) s'oppose à ta peur de l'erreur (Saturne) ce mois-ci. Tu penses, puis tu te censures. Tu parles, puis tu regrettes. Cette tension crée du silence, de l'inhibition, parfois de l'amertume.

## Manifestations concrètes

- **Autocensure** : Tu ne dis pas ce que tu penses par peur d'être jugé
- **Critique externe** : Les autres invalident tes idées, ou tu crois qu'ils le font
- **Blocages intellectuels** : Tu te sens stupide, tu n'oses plus réfléchir à voix haute

## Conseil pratique

Parle à quelqu'un de confiance — une idée partagée te libère de la prison mentale.

## Attention

Attention à la paranoïa intellectuelle — tout le monde ne te juge pas autant que tu le crois."""
    },
    {
        "planet1": "mercury",
        "planet2": "saturn",
        "aspect_type": "square",
        "content": """# □ Carré Mercure - Saturne

**En une phrase :** Ton esprit te punit — chaque pensée est critiquée, jugée, rejetée

## L'énergie de cet aspect

Ton intellect (Mercure) entre en guerre avec ton exigence (Saturne) ce mois-ci. Tu te juges stupide, incompétent, insuffisant. Tes idées te semblent nulles. Cette guerre mentale crée de l'anxiété, parfois du mutisme.

## Manifestations concrètes

- **Anxiété mentale** : Ton esprit te harcèle, tu ne peux pas l'arrêter
- **Mutisme défensif** : Tu préfères ne rien dire plutôt que de risquer l'erreur
- **Perfectionnisme paralysant** : Tu ne termines rien car rien n'est assez bon

## Conseil pratique

Fais une chose imparfaite — écris mal, parle maladroitement — prouve à ton esprit que l'erreur ne tue pas.

## Attention

Gare à l'auto-sabotage — Saturne peut devenir un tyran mental qui détruit toute créativité."""
    },
    {
        "planet1": "mercury",
        "planet2": "saturn",
        "aspect_type": "trine",
        "content": """# △ Trigone Mercure - Saturne

**En une phrase :** Ton esprit devient structure — tu penses avec profondeur et clarté

## L'énergie de cet aspect

Ton intellect (Mercure) et ta rigueur (Saturne) s'harmonisent ce mois-ci. Tu penses de façon organisée, méthodique, solide. Tes idées ont des fondations. Ta communication est précise, fiable.

## Manifestations concrètes

- **Pensée structurée** : Tes raisonnements sont logiques, clairs, vérifiables
- **Communication sobre** : Tu dis l'essentiel, rien de superflu
- **Apprentissages durables** : Ce que tu apprends s'ancre vraiment

## Conseil pratique

Formalise tes idées — écris un plan, une méthode, un système — ton esprit peut structurer du complexe.

## Attention

Attention à la rigidité mentale — parfois il faut aussi laisser place à l'intuition et au chaos créatif."""
    },
    {
        "planet1": "mercury",
        "planet2": "saturn",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mercure - Saturne

**En une phrase :** Tu construis tes idées — pensée par pensée, tu solidifies ta compréhension

## L'énergie de cet aspect

Ton intellect (Mercure) et ta capacité à structurer (Saturne) se complètent ce mois-ci. Tu apprends méthodiquement. Tes idées se précisent, se solidifient. Tu passes du flou au net.

## Manifestations concrètes

- **Apprentissage patient** : Tu acceptes que comprendre prenne du temps
- **Communication réfléchie** : Tu pèses tes mots avant de parler
- **Rigueur mesurée** : Tu vérifies sans devenir obsessionnel

## Conseil pratique

Étudie quelque chose de complexe qui demande de la rigueur — ton esprit a cette discipline maintenant.

## Attention

Gare à trop contrôler — parfois il faut aussi laisser l'esprit vagabonder librement."""
    }
]


async def insert_batch_13():
    """Insère les 10 aspects du Batch 13 en base de données."""

    print(f"=== Insertion Batch 13 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_13())
