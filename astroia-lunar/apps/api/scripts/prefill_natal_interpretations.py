#!/usr/bin/env python3
"""
Script d'import du seed d'interprétations natales

Usage:
    python scripts/prefill_natal_interpretations.py [--file PATH] [--dry-run] [--limit N]

Options:
    --file PATH    Chemin vers le fichier JSONL (default: seeds/natal_interpretations_fr_v2.jsonl)
    --dry-run      Mode simulation sans écriture en DB
    --limit N      Limite le nombre d'entrées à importer
"""

import asyncio
import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any

# Ajouter le répertoire parent au path pour importer les modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from models.natal_interpretation import NatalInterpretation
from config import settings


# User ID fixe pour le seed (générique)
SEED_USER_ID = 1

# Labels français par subject
SUBJECT_LABELS = {
    "sun": "Soleil",
    "moon": "Lune",
    "ascendant": "Ascendant"
}


def generate_chart_id(subject: str, sign: str, house: int) -> str:
    """Génère un chart_id déterministe basé sur subject+sign+house"""
    return f"seed-{subject}-{sign.lower()}-house{house}"


def build_input_json(subject: str, sign: str, house: int) -> Dict[str, Any]:
    """Construit le input_json (ChartPayload minimal)"""
    return {
        "subject_label": SUBJECT_LABELS[subject],
        "sign": sign,
        "degree": 15.0,  # Valeur arbitraire
        "house": house,
        "ascendant_sign": None,
        "aspects": []
    }


async def import_seed_entry(
    db: AsyncSession,
    entry: Dict[str, Any],
    dry_run: bool = False
) -> tuple[bool, str]:
    """
    Importe une entrée du seed

    Returns:
        tuple: (success: bool, status: str)
            status: "inserted", "existed", "error"
    """
    subject = entry["subject"]
    sign = entry["sign"]
    house = entry["house"]
    lang = entry["lang"]
    version = entry["version"]
    text = entry["text"]

    chart_id = generate_chart_id(subject, sign, house)
    input_json = build_input_json(subject, sign, house)

    # Vérifier si l'entrée existe déjà
    try:
        result = await db.execute(
            select(NatalInterpretation).where(
                NatalInterpretation.user_id == SEED_USER_ID,
                NatalInterpretation.chart_id == chart_id,
                NatalInterpretation.subject == subject,
                NatalInterpretation.lang == lang,
                NatalInterpretation.version == version
            )
        )
        existing = result.scalar_one_or_none()

        if existing:
            return True, "existed"

        # Insérer nouvelle entrée
        if not dry_run:
            new_entry = NatalInterpretation(
                user_id=SEED_USER_ID,
                chart_id=chart_id,
                subject=subject,
                lang=lang,
                version=version,
                input_json=input_json,
                output_text=text
            )
            db.add(new_entry)

        return True, "inserted"

    except Exception as e:
        print(f"❌ Erreur pour {subject}/{sign}/maison{house}: {e}")
        return False, "error"


async def import_seed_file(
    file_path: str,
    dry_run: bool = False,
    limit: int = None
):
    """Importe le fichier JSONL complet"""

    # Créer engine async
    # Convertir postgresql:// en postgresql+asyncpg:// pour asyncio
    database_url = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
    engine = create_async_engine(
        database_url,
        echo=False,
        pool_pre_ping=True
    )

    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    # Lire le fichier JSONL
    file_path_obj = Path(file_path)
    if not file_path_obj.exists():
        print(f"❌ Fichier introuvable: {file_path}")
        return

    entries = []
    with open(file_path_obj, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))

    total_entries = len(entries)
    if limit:
        entries = entries[:limit]

    print(f"📚 Import de {len(entries)} interprétations depuis {file_path}")
    if limit and limit < total_entries:
        print(f"   (limité à {limit} sur {total_entries} disponibles)")
    if dry_run:
        print("   🔍 MODE DRY-RUN (simulation)")
    print()

    # Import
    inserted = 0
    existed = 0
    errors = 0

    async with async_session() as session:
        for i, entry in enumerate(entries, 1):
            success, status = await import_seed_entry(session, entry, dry_run)

            if status == "inserted":
                inserted += 1
            elif status == "existed":
                existed += 1
            else:
                errors += 1

            # Progress
            if i % 50 == 0 or i == len(entries):
                print(f"   Progression: {i}/{len(entries)} ({i*100//len(entries)}%)")

        # Commit final (sauf en dry-run)
        if not dry_run and inserted > 0:
            await session.commit()
            print("\n✅ Transaction committée")
        elif dry_run:
            await session.rollback()
            print("\n🔍 Rollback (dry-run)")

    # Résumé
    print(f"\n📊 Résumé:")
    print(f"   Insérées: {inserted}")
    print(f"   Déjà existantes: {existed}")
    print(f"   Erreurs: {errors}")
    print(f"   Total traité: {len(entries)}")

    await engine.dispose()


def main():
    parser = argparse.ArgumentParser(description="Import du seed d'interprétations natales")
    parser.add_argument(
        "--file",
        default="seeds/natal_interpretations_fr_v2.jsonl",
        help="Chemin vers le fichier JSONL"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mode simulation sans écriture en DB"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limite le nombre d'entrées à importer"
    )

    args = parser.parse_args()

    # Exécuter l'import
    asyncio.run(import_seed_file(args.file, args.dry_run, args.limit))


if __name__ == "__main__":
    main()
