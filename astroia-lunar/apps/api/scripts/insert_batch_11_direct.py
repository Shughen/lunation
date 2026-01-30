#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 11 en base de données (version=5)
Généré manuellement - Paires: mars-mercury (5 aspects) + mars-jupiter (5 aspects)
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

# Les 10 aspects du Batch 11
ASPECTS = [
    # === MARS-MERCURY (5 aspects) ===
    {
        "planet1": "mars",
        "planet2": "mercury",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mars - Mercure

**En une phrase :** Tes mots deviennent des armes — tu parles vite, tu tranches net

## L'énergie de cet aspect

Ton action (Mars) fusionne avec ton intellect (Mercure) ce mois-ci. Quand tu penses, tu veux agir immédiatement. Quand tu parles, c'est direct, parfois agressif. Tes idées ont du feu, tes mots ont du tranchant.

## Manifestations concrètes

- **Communication directe** : Tu dis les choses sans détour, parfois trop brutalement
- **Décisions rapides** : Tu analyses vite et tu agis sans hésiter
- **Débats passionnés** : Tu défends tes idées avec force, tu ne lâches rien

## Conseil pratique

Utilise cette clarté pour négocier, argumenter, convaincre — tu as le verbe et l'élan.

## Attention

Gare aux mots qui blessent — sous le coup de l'action, tu peux dire des choses que tu regretteras."""
    },
    {
        "planet1": "mars",
        "planet2": "mercury",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mars - Mercure

**En une phrase :** Ta tête freine ton élan — tu penses trop, tu agis mal

## L'énergie de cet aspect

Ton impulsion d'agir (Mars) s'oppose à ton besoin de réfléchir (Mercure) ce mois-ci. Quand tu veux foncer, ta tête te dit d'attendre. Quand tu analyses, ton impatience te pousse à trancher trop vite. Cette tension crée de la maladresse.

## Manifestations concrètes

- **Actions impulsives** : Tu agis sans réfléchir par frustration, puis tu regrettes
- **Paralysie d'analyse** : Tu réfléchis trop et tu perds ton timing
- **Disputes intellectuelles** : Tes échanges deviennent des combats verbaux

## Conseil pratique

Compte jusqu'à trois avant de parler quand tu es énervé — laisse l'adrénaline redescendre.

## Attention

Attention à blesser avec les mots — Mars-Mercure peut transformer un désaccord en guerre."""
    },
    {
        "planet1": "mars",
        "planet2": "mercury",
        "aspect_type": "square",
        "content": """# □ Carré Mars - Mercure

**En une phrase :** Ton impatience te fait dire n'importe quoi — tu attaques, tu regrettes

## L'énergie de cet aspect

Ton agressivité (Mars) entre en conflit avec ta communication (Mercure) ce mois-ci. Tu t'énerves vite, tu coupes la parole, tu attaques verbalement. Tes mots sortent avant que tu puisses les filtrer. Cette friction crée des disputes, des malentendus.

## Manifestations concrètes

- **Agressivité verbale** : Tu hausses le ton, tu interromps, tu blesses avec les mots
- **Accidents de communication** : Tu dis l'inverse de ce que tu voulais dire
- **Frustration mentale** : Ton esprit tourne trop vite, tu ne peux pas suivre tes pensées

## Conseil pratique

Écris ce que tu veux dire dans un brouillon — relis à froid avant d'envoyer.

## Attention

Gare aux mots définitifs — une phrase lancée dans la colère peut détruire une relation."""
    },
    {
        "planet1": "mars",
        "planet2": "mercury",
        "aspect_type": "trine",
        "content": """# △ Trigone Mars - Mercure

**En une phrase :** Tes idées deviennent actions — tu passes du plan à la réalisation sans effort

## L'énergie de cet aspect

Ton élan (Mars) et ton intelligence (Mercure) collaborent ce mois-ci. Quand tu as une idée, tu sais comment l'exécuter. Quand tu parles, tes mots portent de la force. Tu es stratégique, rapide, efficace.

## Manifestations concrètes

- **Exécution fluide** : Tu transformes tes plans en réalité sans blocage
- **Communication efficace** : Tu convaincre facilement, tes arguments sont clairs et percutants
- **Réactivité mentale** : Tu réagis vite aux situations, tu trouves des solutions rapides

## Conseil pratique

Lance ce projet que tu planifies depuis trop longtemps — tu as l'intelligence et l'énergie maintenant.

## Attention

Attention à aller trop vite — les autres ne suivent pas forcément ton rythme."""
    },
    {
        "planet1": "mars",
        "planet2": "mercury",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mars - Mercure

**En une phrase :** Tu combines tête et jambes — tu penses en agissant, tu agis en pensant

## L'énergie de cet aspect

Ton action (Mars) et ton intellect (Mercure) se stimulent ce mois-ci. Tu apprends en faisant. Tes discussions te donnent envie d'agir. Tes actions te font réfléchir. C'est un va-et-vient productif.

## Manifestations concrètes

- **Apprentissage actif** : Tu retiens mieux en pratiquant qu'en écoutant
- **Débats constructifs** : Tes échanges te poussent à bouger, à créer
- **Projets concrets** : Tu passes de l'idée au prototype rapidement

## Conseil pratique

Engage une conversation difficile que tu repousses — tu as les mots et le courage maintenant.

## Attention

Gare à l'impatience — parfois il faut laisser mûrir une idée avant d'agir."""
    },

    # === MARS-JUPITER (5 aspects) ===
    {
        "planet1": "mars",
        "planet2": "jupiter",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mars - Jupiter

**En une phrase :** Ton audace devient immense — tu veux tout, tu oses tout

## L'énergie de cet aspect

Ton action (Mars) fusionne avec ton optimisme (Jupiter) ce mois-ci. Tu te sens invincible, prêt à conquérir le monde. Tes projets deviennent grandioses, ton courage sans limite. Tu vises haut et tu fonces.

## Manifestations concrètes

- **Projets ambitieux** : Tu lances des choses grandes, tu ne te contentes pas de petit
- **Confiance totale** : Tu crois en ta capacité à réussir, tu ne doutes pas
- **Énergie débordante** : Tu veux agir, explorer, conquérir

## Conseil pratique

Lance ce projet fou qui te fait peur — tu as l'audace et la foi pour y aller.

## Attention

Gare à la sur-confiance — Jupiter peut te faire sous-estimer les obstacles."""
    },
    {
        "planet1": "mars",
        "planet2": "jupiter",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mars - Jupiter

**En une phrase :** Tu vises trop haut — ton ambition dépasse tes moyens

## L'énergie de cet aspect

Ton élan (Mars) s'oppose à ton besoin d'expansion (Jupiter) ce mois-ci. Tu veux aller trop vite, trop loin, trop grand. Tes ressources ne suivent pas tes ambitions. Cette tension crée de la frustration, parfois de l'épuisement.

## Manifestations concrètes

- **Projets démesurés** : Tu t'engages dans trop de choses en même temps
- **Épuisement** : Tu te disperses, tu ne tiens pas la distance
- **Conflits d'ego** : Tu te bats pour des causes trop grandes pour toi

## Conseil pratique

Choisis un seul projet important et donne tout — mieux vaut un succès qu'une multitude d'échecs.

## Attention

Attention à l'hybris — vouloir tout conquérir peut te faire tout perdre."""
    },
    {
        "planet1": "mars",
        "planet2": "jupiter",
        "aspect_type": "square",
        "content": """# □ Carré Mars - Jupiter

**En une phrase :** Tu forces le destin — tu veux gagner à tout prix, quitte à tricher

## L'énergie de cet aspect

Ton agressivité (Mars) se frotte à ton optimisme (Jupiter) ce mois-ci. Tu crois que tout t'est dû, que les règles ne s'appliquent pas à toi. Cette arrogance crée des conflits, parfois des chutes spectaculaires.

## Manifestations concrètes

- **Arrogance** : Tu te crois au-dessus des autres, tu ne respectes pas les limites
- **Risques stupides** : Tu prends des paris dangereux en te croyant immunisé
- **Conflits d'autorité** : Tu défies ceux qui ont plus de pouvoir que toi

## Conseil pratique

Demande-toi : est-ce que je force ou est-ce que je me bats pour du juste ? Puis ajuste.

## Attention

Gare à la chute — Jupiter-Mars peut te faire monter haut juste pour te faire tomber de plus haut."""
    },
    {
        "planet1": "mars",
        "planet2": "jupiter",
        "aspect_type": "trine",
        "content": """# △ Trigone Mars - Jupiter

**En une phrase :** Ta foi te propulse — tu avances avec confiance et grâce

## L'énergie de cet aspect

Ton action (Mars) et ton optimisme (Jupiter) s'harmonisent ce mois-ci. Tu oses sans forcer, tu conquiers sans écraser. Tes projets avancent naturellement. Les opportunités se présentent au bon moment. Tu es dans le flow.

## Manifestations concrètes

- **Succès facile** : Les portes s'ouvrent, les projets se concrétisent
- **Leadership naturel** : Les gens te suivent parce que tu inspires
- **Énergie joyeuse** : Tu agis avec enthousiasme, ça se transmet

## Conseil pratique

Prends une initiative qui te passionne — tu as le courage et la chance maintenant.

## Attention

Attention à tenir cette réussite pour acquise — la gratitude maintient l'élan."""
    },
    {
        "planet1": "mars",
        "planet2": "jupiter",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mars - Jupiter

**En une phrase :** Tu grandis en agissant — chaque effort t'élève

## L'énergie de cet aspect

Ton action (Mars) et ton besoin de sens (Jupiter) se stimulent ce mois-ci. Tu n'agis pas juste pour agir, tu veux que ça ait du sens. Tes efforts te font grandir, découvrir, évoluer.

## Manifestations concrètes

- **Projets porteurs** : Ce que tu lances a un impact positif
- **Courage mesuré** : Tu oses sans te mettre en danger stupidement
- **Optimisme réaliste** : Tu crois en toi sans nier les obstacles

## Conseil pratique

Engage-toi dans une cause qui te dépasse — défendre quelque chose de grand te fera grandir.

## Attention

Gare à l'activisme épuisant — tu peux te battre sans te sacrifier."""
    }
]


async def insert_batch_11():
    """Insère les 10 aspects du Batch 11 en base de données."""

    print(f"=== Insertion Batch 11 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_11())
