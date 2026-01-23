"""
Script maître pour insérer toutes les interprétations lunaires en base
Exécute tous les fichiers batch_generated_*.py
"""

import asyncio
import sys
import glob
import importlib.util
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
         'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

SIGNS_FR = {
    'Aries': 'Bélier', 'Taurus': 'Taureau', 'Gemini': 'Gémeaux',
    'Cancer': 'Cancer', 'Leo': 'Lion', 'Virgo': 'Vierge',
    'Libra': 'Balance', 'Scorpio': 'Scorpion', 'Sagittarius': 'Sagittaire',
    'Capricorn': 'Capricorne', 'Aquarius': 'Verseau', 'Pisces': 'Poissons'
}


async def main():
    scripts_dir = Path(__file__).parent
    total_inserted = 0
    errors = []

    print("=" * 80)
    print("[*] INSERTION MASSIVE DES INTERPRÉTATIONS LUNAIRES")
    print("=" * 80)
    print()

    # Parcourir tous les signes et maisons
    for sign in SIGNS:
        sign_fr = SIGNS_FR[sign]
        print(f"\n[*] Signe : {sign_fr} ({sign})")
        print("-" * 80)

        for house in range(1, 13):
            batch_file = scripts_dir / f"batch_generated_{sign.lower()}_m{house}.py"

            if not batch_file.exists():
                errors.append(f"{sign} M{house} - Fichier non trouvé")
                print(f"  [!] M{house} - Fichier non trouvé")
                continue

            try:
                # Charger le module dynamiquement
                spec = importlib.util.spec_from_file_location(f"batch_{sign}_m{house}", batch_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Récupérer le BATCH
                if not hasattr(module, 'BATCH'):
                    errors.append(f"{sign} M{house} - Pas de BATCH")
                    print(f"  [!] M{house} - Pas de BATCH dans le fichier")
                    continue

                batch = module.BATCH
                batch_size = len(batch)

                # Insérer
                from scripts.insert_lunar_v2_manual import insert_batch
                await insert_batch(batch)

                total_inserted += batch_size
                print(f"  [✓] M{house} - {batch_size} interprétations insérées")

            except Exception as e:
                errors.append(f"{sign} M{house} - Erreur: {str(e)[:50]}")
                print(f"  [!] M{house} - Erreur: {str(e)[:50]}")

    # Résumé final
    print("\n" + "=" * 80)
    print("[*] RÉSUMÉ FINAL")
    print("=" * 80)
    print(f"\n[+] Total inséré : {total_inserted}/1728")
    print(f"[+] Progression : {total_inserted * 100 / 1728:.1f}%")

    if errors:
        print(f"\n[!] Erreurs : {len(errors)}")
        for error in errors[:10]:
            print(f"    - {error}")
        if len(errors) > 10:
            print(f"    ... et {len(errors) - 10} autres erreurs")

    print("\n" + "=" * 80)
    print("[✓] TERMINÉ")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
