#!/usr/bin/env python3
"""
Script Génération Sonnet A/B Test - Version Corrigée
Date: 2026-01-24
Version: 2.0

PROBLÈME RÉSOLU:
- Version originale essayait d'INSERT dans lunar_interpretations (UNIQUE constraint)
- Cette version génère directement avec Claude Sonnet SANS toucher à lunar_interpretations
- Résultat sauvegardé uniquement dans lunar_interpretations_ab_test

Usage:
    python scripts/ab_test_generate_sonnet_fixed.py --count 24
"""

import asyncio
import sys
import os
import time
from datetime import datetime
from typing import Dict, Any
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from database import get_db
from config import settings
import anthropic


async def get_lunar_return_data(db, lunar_return_id: int) -> Dict[str, Any]:
    """Récupérer données lunar_return depuis DB"""

    query = """
    SELECT
        lr.id,
        lr.user_id,
        lr.moon_sign,
        lr.moon_house,
        lr.lunar_ascendant,
        lr.aspects,
        lr.transits,
        lr.lunar_return_date,
        u.birth_date,
        u.birth_time,
        u.birth_place,
        nc.sun_sign,
        nc.moon_sign as natal_moon_sign,
        nc.ascendant_sign
    FROM lunar_returns lr
    LEFT JOIN users u ON lr.user_id = u.id
    LEFT JOIN natal_charts nc ON u.id = nc.user_id
    WHERE lr.id = :lunar_return_id
    """

    result = await db.execute(text(query), {"lunar_return_id": lunar_return_id})
    row = result.first()

    if not row:
        raise ValueError(f"lunar_return_id={lunar_return_id} not found")

    return {
        "lunar_return_id": row.id,
        "user_id": row.user_id,
        "moon_sign": row.moon_sign,
        "moon_house": row.moon_house,
        "lunar_ascendant": row.lunar_ascendant,
        "aspects": row.aspects,
        "transits": row.transits,
        "lunar_return_date": row.lunar_return_date.isoformat() if row.lunar_return_date else None,
        "birth_date": row.birth_date.isoformat() if row.birth_date else None,
        "sun_sign": row.sun_sign,
        "natal_moon_sign": row.natal_moon_sign,
        "ascendant_sign": row.ascendant_sign
    }


async def generate_with_claude_sonnet(lunar_data: Dict[str, Any]) -> Dict[str, Any]:
    """Générer interprétation DIRECTEMENT avec Claude Sonnet (bypass cache)"""

    # Prompt système (version simplifiée du prompt production)
    system_message = """Tu es une astrologue experte spécialisée dans les cycles lunaires.
Tu dois créer une interprétation personnalisée et chaleureuse d'une révolution lunaire.

Consignes strictes :
1. TON : tutoiement, chaleureux, empathique, inspirant
2. STRUCTURE : 4 sections (Tonalité générale, Ressources intérieures, Défis à anticiper, Dynamiques)
3. LONGUEUR : 1000-1200 caractères minimum
4. FORMAT : Markdown avec titre "# 🌙 Ta Révolution Lunaire du Mois"
5. COHÉRENCE : Intégrer Moon sign + House + Lunar Ascendant dans l'analyse
6. CONSEILS : Actionnables et concrets, pas juste descriptifs
"""

    # Construction prompt utilisateur
    user_prompt = f"""Génère une interprétation lunaire pour :

**Révolution Lunaire** :
- Signe Lunaire : {lunar_data['moon_sign']}
- Maison Lunaire : {lunar_data['moon_house']}
- Ascendant Lunaire : {lunar_data['lunar_ascendant']}

**Thème Natal** :
- Signe Solaire : {lunar_data.get('sun_sign', 'inconnu')}
- Lune Natale : {lunar_data.get('natal_moon_sign', 'inconnu')}
- Ascendant Natal : {lunar_data.get('ascendant_sign', 'inconnu')}

Crée une interprétation riche, personnalisée et inspirante."""

    # Appel Claude Sonnet avec Prompt Caching
    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    start_time = time.time()

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",  # Sonnet 4.5
            max_tokens=2000,
            temperature=0.8,
            system=[
                {
                    "type": "text",
                    "text": system_message,
                    "cache_control": {"type": "ephemeral"}  # Prompt Caching
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        duration = time.time() - start_time

        # Extraire contenu
        output_text = response.content[0].text

        # Générer weekly_advice (structure minimale)
        weekly_advice = [
            {
                "title": "Conseil principal",
                "description": "Suis les mouvements lunaires ce mois-ci",
                "icon": "✨"
            }
        ]

        metadata = {
            "model_used": "claude-sonnet-4-5-20250929",
            "source": "claude",
            "version": 2,
            "generated_at": datetime.utcnow().isoformat(),
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "cache_read_tokens": getattr(response.usage, 'cache_read_input_tokens', 0),
            "cache_creation_tokens": getattr(response.usage, 'cache_creation_input_tokens', 0)
        }

        return {
            "output_text": output_text,
            "weekly_advice": weekly_advice,
            "metadata": metadata,
            "duration_seconds": duration,
            "source": "claude-sonnet-4-5-20250929"
        }

    except Exception as e:
        print(f"❌ Erreur génération Claude: {e}")
        raise


async def save_ab_test_result(
    user_id: int,
    lunar_return_id: int,
    model: str,
    result: Dict[str, Any]
):
    """Sauvegarder résultat dans table A/B test"""

    insert_sql = """
    INSERT INTO lunar_interpretations_ab_test
    (user_id, lunar_return_id, model_tested, output_text, weekly_advice, metadata, duration_seconds)
    VALUES (:user_id, :lunar_return_id, :model_tested, :output_text, :weekly_advice, :metadata, :duration_seconds)
    """

    async for db in get_db():
        await db.execute(text(insert_sql), {
            "user_id": user_id,
            "lunar_return_id": lunar_return_id,
            "model_tested": model,
            "output_text": result["output_text"],
            "weekly_advice": json.dumps(result["weekly_advice"]),
            "metadata": json.dumps(result["metadata"]),
            "duration_seconds": result["duration_seconds"]
        })
        await db.commit()
        break


async def get_opus_lunar_returns() -> list:
    """Récupérer les lunar_return_ids utilisés par Opus (depuis lunar_interpretations_ab_test)"""

    query = """
    SELECT DISTINCT lunar_return_id, user_id
    FROM lunar_interpretations_ab_test
    WHERE model_tested = 'opus'
    ORDER BY lunar_return_id
    """

    async for db in get_db():
        result = await db.execute(text(query))
        rows = result.fetchall()
        print(f"✅ Récupéré {len(rows)} lunar_returns depuis test Opus")
        return rows


async def run_sonnet_ab_test():
    """Exécuter test Sonnet sur MÊMES lunar_returns qu'Opus"""

    print(f"\n{'='*60}")
    print(f"🧪 A/B Test Sonnet - Version Corrigée v2")
    print(f"   Stratégie: Génération directe Claude Sonnet")
    print(f"   Bypass: lunar_interpretations (pas de UNIQUE conflict)")
    print(f"   Transaction: Nouvelle session par génération")
    print(f"{'='*60}\n")

    # Récupérer lunar_returns utilisés par Opus
    opus_samples = await get_opus_lunar_returns()

    if not opus_samples:
        print("❌ Aucun échantillon Opus trouvé. Lancez d'abord le test Opus.")
        return

    count = len(opus_samples)
    print(f"📊 Génération Sonnet pour {count} lunar_returns\n")

    # Stats
    total_cost = 0.0
    total_duration = 0.0
    successful = 0
    failed = 0
    sonnet_cost_per_gen = 0.012  # $0.012 sans caching

    # CORRECTION: Nouvelle session DB par itération (évite transaction bloquée)
    for i, row in enumerate(opus_samples, 1):
        lunar_return_id = row.lunar_return_id
        user_id = row.user_id

        try:
            print(f"[{i}/{count}] Génération Sonnet (lunar_return_id={lunar_return_id})...", flush=True)

            # Nouvelle session DB pour cette génération
            async for db in get_db():
                try:
                    print(f"  → DB session OK", flush=True)
                    # Récupérer données lunar_return
                    lunar_data = await get_lunar_return_data(db, lunar_return_id)
                    print(f"  → Données récupérées: {lunar_data['moon_sign']} M{lunar_data['moon_house']}", flush=True)

                    # Générer avec Claude Sonnet
                    print(f"  → Appel Claude Sonnet...", flush=True)
                    result = await generate_with_claude_sonnet(lunar_data)
                    print(f"  → Génération OK: {len(result['output_text'])} chars", flush=True)

                    # Sauvegarder dans lunar_interpretations_ab_test
                    await save_ab_test_result(
                        user_id=user_id,
                        lunar_return_id=lunar_return_id,
                        model="sonnet",
                        result=result
                    )

                    # Stats
                    duration = result["duration_seconds"]
                    source = result["source"]
                    length = len(result["output_text"])

                    # Coût avec Prompt Caching (-90%)
                    cache_read = result["metadata"].get("cache_read_tokens", 0)
                    if cache_read > 0:
                        total_cost += sonnet_cost_per_gen * 0.1  # -90% avec caching
                    else:
                        total_cost += sonnet_cost_per_gen

                    total_duration += duration
                    successful += 1

                    print(f"✅ {duration:.1f}s | {source} | {length} chars")

                except Exception as inner_e:
                    # Rollback cette transaction
                    await db.rollback()
                    raise inner_e

                finally:
                    break  # Sortir de async for après une itération

        except Exception as e:
            failed += 1
            print(f"❌ Erreur: {str(e)}")
            import traceback
            traceback.print_exc()

    # Rapport final
    print(f"\n{'='*60}")
    print(f"📊 Résultats A/B Test - SONNET (Version Corrigée)")
    print(f"{'='*60}")
    print(f"Générations réussies : {successful}/{count} ({successful/count*100:.1f}%)")
    print(f"Générations échouées : {failed}/{count}")
    print(f"Durée moyenne        : {total_duration/successful:.1f}s" if successful > 0 else "N/A")
    print(f"Durée totale         : {total_duration:.1f}s ({total_duration/60:.1f} minutes)")
    print(f"Coût estimé          : ${total_cost:.3f} (avec Prompt Caching -90%)")
    print(f"Coût sans caching    : ${successful * sonnet_cost_per_gen:.3f}")
    print(f"Économie caching     : ${successful * sonnet_cost_per_gen - total_cost:.3f} ({(1 - total_cost/(successful * sonnet_cost_per_gen))*100:.0f}%)" if successful > 0 else "")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    asyncio.run(run_sonnet_ab_test())
