#!/usr/bin/env python3
"""
Script A/B Test Sonnet - Appel Direct Claude API
Génère 24 interprétations Sonnet pour comparaison avec Opus
"""

import asyncio
import sys
import os
import time
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from database import get_db
from config import settings
import anthropic


async def get_lunar_returns_from_opus():
    """Récupérer les 24 lunar_returns testés par Opus"""
    async for db in get_db():
        result = await db.execute(text("""
            SELECT DISTINCT lr.id, lr.user_id, lr.moon_sign, lr.moon_house, lr.lunar_ascendant
            FROM lunar_interpretations_ab_test ab
            JOIN lunar_returns lr ON ab.lunar_return_id = lr.id
            WHERE ab.model_tested = 'opus'
            ORDER BY lr.id
        """))
        rows = result.fetchall()
        return rows


async def generate_sonnet(lunar_data):
    """Génère une interprétation avec Claude Sonnet"""
    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    system_prompt = """Tu es une astrologue experte spécialisée dans les cycles lunaires.
Crée une interprétation personnalisée et chaleureuse d'une révolution lunaire.

Consignes :
- TON : tutoiement, chaleureux, empathique, inspirant
- STRUCTURE : Tonalité générale, Ressources intérieures, Défis, Dynamiques
- LONGUEUR : 1000-1200 caractères minimum
- FORMAT : Markdown avec titre "# 🌙 Ta Révolution Lunaire du Mois"
- COHÉRENCE : Intégrer Moon sign + House + Lunar Ascendant"""

    user_prompt = f"""Génère une interprétation lunaire pour :

**Révolution Lunaire** :
- Signe Lunaire : {lunar_data['moon_sign']}
- Maison Lunaire : {lunar_data['moon_house']}
- Ascendant Lunaire : {lunar_data['lunar_ascendant']}

Crée une interprétation riche, personnalisée et inspirante."""

    start = time.time()

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=2000,
        temperature=0.8,
        system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_prompt}]
    )

    duration = time.time() - start
    output_text = response.content[0].text

    return {
        "output_text": output_text,
        "duration_seconds": duration,
        "model_used": "claude-sonnet-4-5-20250929",
        "source": "claude",
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "cache_read_tokens": getattr(response.usage, 'cache_read_input_tokens', 0),
        "cache_creation_tokens": getattr(response.usage, 'cache_creation_input_tokens', 0)
    }


async def save_to_ab_test(lunar_return_id, user_id, result):
    """Sauvegarde dans table A/B test"""
    async for db in get_db():
        await db.execute(text("""
            INSERT INTO lunar_interpretations_ab_test
            (user_id, lunar_return_id, model_tested, output_text, weekly_advice, metadata, duration_seconds)
            VALUES (:user_id, :lunar_return_id, :model, :text, :advice, :metadata, :duration)
        """), {
            "user_id": user_id,
            "lunar_return_id": lunar_return_id,
            "model": "sonnet",
            "text": result["output_text"],
            "advice": json.dumps([]),
            "metadata": json.dumps({"source": result["source"], "model_used": result["model_used"]}),
            "duration": result["duration_seconds"]
        })
        await db.commit()
        break


async def main():
    print("=" * 60)
    print("🧪 A/B Test Sonnet - Appel Direct Claude API")
    print("=" * 60)
    print()

    lunar_returns = await get_lunar_returns_from_opus()
    print(f"✅ Récupéré {len(lunar_returns)} lunar_returns depuis test Opus")
    print()

    count = len(lunar_returns)
    successful = 0
    failed = 0
    total_duration = 0.0
    total_cost = 0.0

    for i, row in enumerate(lunar_returns, 1):
        try:
            print(f"[{i}/{count}] Génération Sonnet (lr_id={row.id})...", end=" ", flush=True)

            lunar_data = {
                "moon_sign": row.moon_sign,
                "moon_house": row.moon_house,
                "lunar_ascendant": row.lunar_ascendant
            }

            result = await generate_sonnet(lunar_data)
            await save_to_ab_test(row.id, row.user_id, result)

            total_duration += result["duration_seconds"]
            successful += 1

            # Coût Sonnet : $0.012/génération (sans caching)
            total_cost += 0.012

            print(f"✅ {result['duration_seconds']:.1f}s | {len(result['output_text'])} chars")

        except Exception as e:
            failed += 1
            print(f"❌ {e}")
            import traceback
            traceback.print_exc()

    print()
    print("=" * 60)
    print("📊 Résultats A/B Test - SONNET")
    print("=" * 60)
    print(f"Générations réussies : {successful}/{count} ({successful/count*100:.1f}%)" if count > 0 else "N/A")
    print(f"Générations échouées : {failed}/{count}")
    print(f"Durée moyenne        : {total_duration/successful:.1f}s" if successful > 0 else "N/A")
    print(f"Durée totale         : {total_duration:.1f}s ({total_duration/60:.1f} min)")
    print(f"Coût estimé          : ${total_cost:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
