#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 4 en base de données (version=5)
Généré manuellement - Paires: sun-mercury (5 aspects) + sun-saturn (5 aspects)
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

# Les 10 aspects du Batch 4
ASPECTS = [
    # === SUN-MERCURY (5 aspects) ===
    {
        "planet1": "sun",
        "planet2": "mercury",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Soleil - Mercure

**En une phrase :** Ta tête et ton cœur parlent le même langage — tu sais te faire comprendre

## L'énergie de cet aspect

Ton identité (Soleil) et ton intelligence (Mercure) ne font qu'un ce mois-ci. Quand tu parles, on sent que ça vient de ton centre. Tes idées te ressemblent, tes mots portent ta personnalité.

## Manifestations concrètes

- **Communication fluide** : Tu articules clairement ce que tu penses et ressens, sans filtre
- **Décisions rapides** : Tu analyses vite, tu tranches sans ruminer
- **Curiosité active** : Ton besoin d'apprendre te pousse vers de nouvelles découvertes

## Conseil pratique

Profite de cette clarté pour écrire, négocier ou présenter quelque chose qui te tient à cœur.

## Attention

Gare à confondre conviction et vérité — tu peux être tellement sûr de toi que tu n'écoutes plus."""
    },
    {
        "planet1": "sun",
        "planet2": "mercury",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Soleil - Mercure

**En une phrase :** Ton cœur dit oui, ta tête dit non — il faut trancher

## L'énergie de cet aspect

Ce que tu veux (Soleil) et ce que tu penses (Mercure) tirent chacun de leur côté ce mois-ci. Tu peux te sentir écartelé entre tes intuitions et ta logique, entre ce qui t'anime et ce qui semble raisonnable.

## Manifestations concrètes

- **Hésitations fréquentes** : Tu réfléchis trop, tu remets en question tes choix instinctifs
- **Dialogues intérieurs** : Une part de toi argumente pendant que l'autre veut juste foncer
- **Communication double** : Ce que tu dis ne reflète pas toujours ce que tu ressens vraiment

## Conseil pratique

Écoute alternativement ton cœur puis ta raison — la réponse émerge dans l'échange, pas dans le combat.

## Attention

Attention à intellectualiser tes envies jusqu'à les éteindre — parfois il faut agir avant de comprendre."""
    },
    {
        "planet1": "sun",
        "planet2": "mercury",
        "aspect_type": "square",
        "content": """# □ Carré Soleil - Mercure

**En une phrase :** Ton mental fait de la résistance — tes pensées ralentissent ton élan

## L'énergie de cet aspect

Ta volonté (Soleil) bute contre ton analyse (Mercure) ce mois-ci. Quand tu veux avancer, ta tête te dit d'attendre, de vérifier, de tout peser. Tes pensées deviennent un frein à main que tu oublies de desserrer.

## Manifestations concrètes

- **Paralysie d'analyse** : Tu surpenses jusqu'à ne plus savoir quoi faire
- **Mots maladroits** : Tu cherches la formule parfaite et tu finis par ne rien dire
- **Jugement critique** : Tu te sabotes mentalement avant même d'essayer

## Conseil pratique

Fixe une deadline pour décider — à partir de là, tu passes à l'action même si tout n'est pas clair.

## Attention

Gare à l'auto-sabotage intellectuel — ton mental peut devenir ton pire ennemi s'il contrôle tout."""
    },
    {
        "planet1": "sun",
        "planet2": "mercury",
        "aspect_type": "trine",
        "content": """# △ Trigone Soleil - Mercure

**En une phrase :** Ta pensée et ton être coulent ensemble — tu communiques avec grâce

## L'énergie de cet aspect

Ton identité profonde (Soleil) et ton intelligence (Mercure) collaborent naturellement ce mois-ci. Quand tu parles, les mots viennent sans effort. Quand tu réfléchis, tu es aligné avec ce qui compte vraiment pour toi.

## Manifestations concrètes

- **Expression naturelle** : Tu trouves les mots justes sans chercher, tu te fais comprendre facilement
- **Apprentissage fluide** : Ce que tu apprends fait sens immédiatement, ça s'intègre
- **Clarté mentale** : Tes pensées sont organisées, ton esprit est calme et précis

## Conseil pratique

Utilise cette clarté pour écrire ce qui te traverse, ou enseigner ce que tu sais — ça sortira tout seul.

## Attention

Attention à tenir pour acquis cette facilité — les autres ne te comprennent pas forcément aussi vite."""
    },
    {
        "planet1": "sun",
        "planet2": "mercury",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Soleil - Mercure

**En une phrase :** Ta curiosité alimente ton identité — apprendre te fait grandir

## L'énergie de cet aspect

Ton essence (Soleil) et ton intelligence (Mercure) se stimulent mutuellement ce mois-ci. Plus tu apprends, plus tu te découvres. Plus tu t'exprimes, plus tu comprends qui tu es vraiment.

## Manifestations concrètes

- **Conversations éclairantes** : Les échanges t'aident à clarifier ce que tu veux
- **Curiosité ciblée** : Tu cherches des infos sur ce qui te passionne vraiment
- **Expression authentique** : Tu arrives à dire "je" sans te perdre dans les nuances

## Conseil pratique

Engage une conversation profonde avec quelqu'un qui te challenge — tu vas apprendre sur toi.

## Attention

Gare à rester dans ta tête — tu peux analyser ta propre identité au lieu de la vivre."""
    },

    # === SUN-SATURN (5 aspects) ===
    {
        "planet1": "sun",
        "planet2": "saturn",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Soleil - Saturne

**En une phrase :** Tu te construis pierre par pierre — ta maturité devient ta force

## L'énergie de cet aspect

Ton identité (Soleil) et ta structure intérieure (Saturne) fusionnent ce mois-ci. Tu sens le poids de tes responsabilités, mais tu es prêt à les porter. Tu deviens plus solide, plus fiable, plus toi.

## Manifestations concrètes

- **Sérieux accru** : Les frivolités t'intéressent moins, tu veux du concret
- **Discipline naturelle** : Tu poses des limites sans t'excuser, tu tiens tes engagements
- **Réalisme assumé** : Tu vois les choses telles qu'elles sont, sans faux espoirs

## Conseil pratique

Engage-toi dans un projet à long terme qui demande de la persévérance — tu as cette force maintenant.

## Attention

Gare à devenir trop dur avec toi-même — exigence n'est pas punition."""
    },
    {
        "planet1": "sun",
        "planet2": "saturn",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Soleil - Saturne

**En une phrase :** Tes envies butent contre tes limites — il faut négocier

## L'énergie de cet aspect

Ce que tu veux être (Soleil) se heurte à ce qui te freine (Saturne) ce mois-ci. Tes élans rencontrent des barrières, réelles ou mentales. Tu peux te sentir bridé, comme si avancer demandait une permission que personne ne donne.

## Manifestations concrètes

- **Sentiment de blocage** : Chaque initiative semble se heurter à un obstacle
- **Découragement facile** : Tu doutes de toi avant même de commencer
- **Obligations pesantes** : Tes responsabilités t'empêchent d'être qui tu veux

## Conseil pratique

Identifie une limite que tu peux repousser cette semaine — petite victoire, grand effet sur ton moral.

## Attention

Attention à te résigner trop vite — certaines barrières sont dans ta tête, pas dans la réalité."""
    },
    {
        "planet1": "sun",
        "planet2": "saturn",
        "aspect_type": "square",
        "content": """# □ Carré Soleil - Saturne

**En une phrase :** Ton élan se fracasse contre un mur — apprends à construire autrement

## L'énergie de cet aspect

Ta volonté (Soleil) entre en conflit avec tes contraintes (Saturne) ce mois-ci. Quand tu veux briller, quelque chose te ramène à la dure réalité. Tes ambitions butent sur des limites, et ça crée de la frustration, voire de la colère.

## Manifestations concrètes

- **Frustrations récurrentes** : Ce que tu veux semble constamment hors de portée
- **Critique intérieure** : Une voix te dit que tu n'es pas à la hauteur
- **Fatigue morale** : Avancer demande tellement d'efforts que tu as envie d'abandonner

## Conseil pratique

Transforme une contrainte en défi — trouve une façon créative de contourner l'obstacle plutôt que de foncer dedans.

## Attention

Gare à l'auto-sabotage — tu peux devenir ton propre geôlier si tu intériorises trop les limites."""
    },
    {
        "planet1": "sun",
        "planet2": "saturn",
        "aspect_type": "trine",
        "content": """# △ Trigone Soleil - Saturne

**En une phrase :** Ta discipline devient invisible — tu avances avec autorité naturelle

## L'énergie de cet aspect

Ton identité (Soleil) et ta structure (Saturne) travaillent main dans la main ce mois-ci. Tu incarnes une forme de maturité tranquille. Tes efforts ne sont plus des sacrifices, ils sont ton style. Tu construis sans forcer.

## Manifestations concrètes

- **Confiance sobre** : Tu sais ce que tu vaux sans avoir besoin de le crier
- **Endurance naturelle** : Les projets longs ne te font plus peur, tu t'organises
- **Respect instinctif** : Les gens te prennent au sérieux sans que tu doives le demander

## Conseil pratique

Lance cette chose que tu repousses depuis des mois — tu as maintenant l'endurance pour aller au bout.

## Attention

Attention à devenir trop austère — la discipline ne doit pas étouffer ta joie de vivre."""
    },
    {
        "planet1": "sun",
        "planet2": "saturn",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Soleil - Saturne

**En une phrase :** Tu poses des fondations — chaque petit pas compte

## L'énergie de cet aspect

Ton être profond (Soleil) et ta capacité à structurer (Saturne) se complètent ce mois-ci. Tu as envie de solidifier ce qui compte. Les efforts ne te font pas peur s'ils ont du sens. Tu es prêt à construire patiemment.

## Manifestations concrètes

- **Projets concrets** : Tu passes des idées à l'action, avec méthode
- **Patience active** : Tu acceptes que les choses prennent du temps, sans renoncer
- **Sagesse pratique** : Tu sais quand dire non pour protéger tes priorités

## Conseil pratique

Crée un plan d'action réaliste pour un objectif à 6 mois — ta discipline actuelle peut tenir la distance.

## Attention

Gare à devenir trop sérieux — ne sacrifie pas ton plaisir sur l'autel de la productivité."""
    }
]


async def insert_batch_04():
    """Insère les 10 aspects du Batch 4 en base de données."""

    print(f"=== Insertion Batch 4 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_04())
