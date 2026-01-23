"""
Genere les interpretations lunaires v2 avec Claude Opus 4.5
1728 combinaisons : 12 signes x 12 maisons x 12 ascendants lunaires

Usage:
    python scripts/generate_lunar_interpretations_v2.py --mode validation
    python scripts/generate_lunar_interpretations_v2.py --mode full
    python scripts/generate_lunar_interpretations_v2.py --mode db-insert
"""

import anthropic
import os
import sys
import json
import re
import asyncio
from pathlib import Path
from typing import Tuple, List, Optional, Dict, Any
import time
import argparse
from datetime import datetime
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Essayer d'importer tqdm (optionnel, utilise seulement en mode full)
try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    print("[!] tqdm non installe, barre de progression desactivee pour le mode full")

# Ajouter le dossier parent au path pour imports relatifs
sys.path.insert(0, str(Path(__file__).parent.parent))

# === CONSTANTES ===

# Signes du zodiaque (12 signes) - format (key, label_fr)
SIGNS = [
    ('Aries', 'Belier'),
    ('Taurus', 'Taureau'),
    ('Gemini', 'Gemeaux'),
    ('Cancer', 'Cancer'),
    ('Leo', 'Lion'),
    ('Virgo', 'Vierge'),
    ('Libra', 'Balance'),
    ('Scorpio', 'Scorpion'),
    ('Sagittarius', 'Sagittaire'),
    ('Capricorn', 'Capricorne'),
    ('Aquarius', 'Verseau'),
    ('Pisces', 'Poissons')
]

# Maisons astrologiques (1-12)
HOUSES = list(range(1, 13))

# Descriptions des maisons pour le prompt
HOUSE_DESCRIPTIONS = {
    1: "identite, apparence, nouveaux departs",
    2: "ressources, valeurs, securite materielle",
    3: "communication, apprentissages, environnement proche",
    4: "foyer, famille, racines, vie interieure",
    5: "creativite, plaisir, expression personnelle, romance",
    6: "quotidien, routine, sante, organisation",
    7: "relations, partenariats, collaborations",
    8: "transformations, crises, intimite, ressources partagees",
    9: "expansion, voyages, philosophie, quete de sens",
    10: "carriere, ambitions, accomplissements, statut",
    11: "projets collectifs, amities, reseaux, ideaux",
    12: "interiorite, inconscient, spiritualite, lacher-prise"
}

# Exemples de validation (8 combinaisons diverses)
VALIDATION_EXAMPLES = [
    ('Aries', 1, 'Aries'),       # Belier M1 ASC Belier
    ('Taurus', 2, 'Cancer'),     # Taureau M2 ASC Cancer
    ('Gemini', 3, 'Leo'),        # Gemeaux M3 ASC Lion
    ('Cancer', 4, 'Virgo'),      # Cancer M4 ASC Vierge
    ('Leo', 5, 'Scorpio'),       # Lion M5 ASC Scorpion
    ('Virgo', 6, 'Sagittarius'), # Vierge M6 ASC Sagittaire
    ('Libra', 7, 'Aquarius'),    # Balance M7 ASC Verseau
    ('Scorpio', 8, 'Pisces'),    # Scorpion M8 ASC Poissons
]


def get_sign_label(sign_key: str) -> str:
    """Retourne le label francais d'un signe"""
    for key, label in SIGNS:
        if key == sign_key:
            return label
    return sign_key


def build_lunar_prompt_v2(moon_sign: str, moon_house: int, lunar_ascendant: str) -> str:
    """
    Construit le prompt pour Opus 4.5 selon template lunaire v2

    Objectif: Interpretation complete croisant les 3 parametres
    """
    moon_sign_fr = get_sign_label(moon_sign)
    lunar_asc_fr = get_sign_label(lunar_ascendant)
    house_desc = HOUSE_DESCRIPTIONS.get(moon_house, f"domaine de la Maison {moon_house}")

    prompt = f"""Tu es un astrologue senior pour l'app Lunation. Style : chaleureux, concret, moderne.

COMBINAISON DU MOIS :
- Lune natale en {moon_sign_fr}
- Maison lunaire : {moon_house} ({house_desc})
- Ascendant lunaire : {lunar_asc_fr}

GENERE UNE INTERPRETATION COMPLETE (800-1200 caracteres) :

**Ton mois en un mot : [Theme principal en 1-3 mots]**

[3-4 phrases : L'energie emotionnelle dominante. Ce que tu ressens profondement.
Comment cette combinaison unique colore ton mois. Croise les 3 parametres.]

**Domaine active** : Maison {moon_house} - [2 phrases sur ou l'energie se deploie dans le domaine "{house_desc}"]

**Ton approche instinctive** : Ascendant {lunar_asc_fr} - [2 phrases sur comment tu abordes les situations ce mois-ci avec cette energie]

**Tensions possibles** : [1-2 phrases sur les defis potentiels de cette combinaison specifique]

**Conseil cle** : [1 phrase actionnable pour ce mois, a l'infinitif]

---

GENERE AUSSI 4 CONSEILS HEBDOMADAIRES (format JSON strict) :
```json
{{
  "week_1": "[Conseil concret pour la semaine 1, lancement du cycle, 80-120 chars]",
  "week_2": "[Conseil concret pour la semaine 2, consolidation, 80-120 chars]",
  "week_3": "[Conseil concret pour la semaine 3, ajustements, 80-120 chars]",
  "week_4": "[Conseil concret pour la semaine 4, bilan et cloture, 80-120 chars]"
}}
```

CONTRAINTES STRICTES:
1. LONGUEUR interpretation : 800-1200 caracteres (max absolu 1400)
2. TON : 2e personne (tu), present, chaleureux mais pas mystique
3. INTERDIT : predictions ("tu vas rencontrer..."), conseils sante, "tu es quelqu'un de..."
4. OBLIGATOIRE : croiser les 3 parametres (signe lunaire, maison, ascendant) dans l'interpretation
5. FORMAT : Markdown pour l'interpretation, JSON valide pour weekly_advice
6. Les conseils hebdomadaires doivent etre concrets et actionnables

GENERE L'INTERPRETATION MAINTENANT (francais):"""

    return prompt


def parse_response(response_text: str) -> Tuple[str, Dict[str, str]]:
    """
    Parse la reponse de Claude pour extraire interpretation et weekly_advice

    Returns:
        tuple: (interpretation_full, weekly_advice_dict)
    """
    # Chercher le bloc JSON
    json_match = re.search(r'```json\s*(\{[^`]+\})\s*```', response_text, re.DOTALL)

    if json_match:
        json_str = json_match.group(1)
        try:
            weekly_advice = json.loads(json_str)
        except json.JSONDecodeError:
            # Essayer de nettoyer le JSON
            json_str = json_str.replace('\n', ' ').strip()
            try:
                weekly_advice = json.loads(json_str)
            except json.JSONDecodeError:
                weekly_advice = {
                    "week_1": "Pose tes intentions pour ce nouveau cycle lunaire.",
                    "week_2": "Approfondi ce que tu as commence. Reste ancre(e).",
                    "week_3": "Fais le point et ajuste ce qui doit l'etre.",
                    "week_4": "Prepare-toi pour le prochain cycle. Lache ce qui ne sert plus."
                }

        # Extraire l'interpretation (tout avant le JSON)
        interpretation = response_text[:json_match.start()].strip()

        # Nettoyer les marqueurs de code residuels
        interpretation = re.sub(r'---\s*$', '', interpretation).strip()

    else:
        # Pas de JSON trouve, utiliser tout le texte comme interpretation
        interpretation = response_text.strip()
        weekly_advice = {
            "week_1": "Pose tes intentions pour ce nouveau cycle lunaire.",
            "week_2": "Approfondi ce que tu as commence. Reste ancre(e).",
            "week_3": "Fais le point et ajuste ce qui doit l'etre.",
            "week_4": "Prepare-toi pour le prochain cycle. Lache ce qui ne sert plus."
        }

    return interpretation, weekly_advice


def generate_lunar_interpretation(
    client: anthropic.Anthropic,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    max_retries: int = 2
) -> Tuple[str, Dict[str, str], int]:
    """
    Appelle Opus 4.5 pour generer UNE interpretation lunaire complete

    Returns:
        tuple: (interpretation_full, weekly_advice, longueur)
    """
    prompt = build_lunar_prompt_v2(moon_sign, moon_house, lunar_ascendant)

    moon_sign_fr = get_sign_label(moon_sign)
    lunar_asc_fr = get_sign_label(lunar_ascendant)

    for attempt in range(max_retries + 1):
        try:
            print(f"  [*] Appel Opus 4.5 pour {moon_sign_fr} M{moon_house} ASC {lunar_asc_fr}...", end="", flush=True)

            response = client.messages.create(
                model="claude-opus-4-5-20251101",
                max_tokens=2000,
                temperature=0.7,
                messages=[{"role": "user", "content": prompt}]
            )

            text = response.content[0].text.strip()

            # Parser la reponse
            interpretation, weekly_advice = parse_response(text)
            length = len(interpretation)

            # Valider longueur (800-1400 chars)
            if length < 800 and attempt < max_retries:
                print(f" [!] Trop court ({length} chars), retry...", flush=True)
                time.sleep(1)
                continue

            if length > 1400:
                # Tronquer si trop long
                interpretation = interpretation[:1397] + "..."
                length = 1400

            print(f" [+] {length} chars")
            return interpretation, weekly_advice, length

        except Exception as e:
            print(f" [!] ERREUR (attempt {attempt + 1}): {str(e)[:80]}")
            if attempt < max_retries:
                time.sleep(2)
            else:
                raise

    raise Exception("Max retries exceeded")


def save_to_markdown(
    interpretation: str,
    weekly_advice: Dict[str, str],
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    version: int = 2
) -> Path:
    """
    Sauvegarde dans data/lunar_interpretations/v{version}/{moon_sign}/{house}_{lunar_ascendant}.md

    Returns:
        Path: Chemin du fichier sauvegarde
    """
    # Creer dossier si necessaire
    output_dir = Path(__file__).parent.parent / f"data/lunar_interpretations/v{version}/{moon_sign}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Fichier
    filename = f"M{moon_house}_{lunar_ascendant}.md"
    filepath = output_dir / filename

    # Frontmatter YAML
    frontmatter = f"""---
moon_sign: {moon_sign}
moon_sign_fr: {get_sign_label(moon_sign)}
moon_house: {moon_house}
lunar_ascendant: {lunar_ascendant}
lunar_ascendant_fr: {get_sign_label(lunar_ascendant)}
version: {version}
lang: fr
length: {len(interpretation)}
generated_at: {datetime.now().isoformat()}
weekly_advice:
  week_1: "{weekly_advice.get('week_1', '')}"
  week_2: "{weekly_advice.get('week_2', '')}"
  week_3: "{weekly_advice.get('week_3', '')}"
  week_4: "{weekly_advice.get('week_4', '')}"
---

"""

    # Ecrire
    filepath.write_text(frontmatter + interpretation, encoding='utf-8')
    print(f"  [>] Sauvegarde: {filepath.relative_to(Path.cwd())}")

    return filepath


async def insert_to_database(
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    interpretation: str,
    weekly_advice: Dict[str, str],
    version: int = 2
) -> bool:
    """
    Insere ou met a jour une interpretation dans la DB

    Returns:
        bool: True si succes
    """
    try:
        from database import async_session_maker
        from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation
        from sqlalchemy import select
        from sqlalchemy.dialects.postgresql import insert

        async with async_session_maker() as session:
            # Upsert (insert ou update si existe)
            stmt = insert(PregeneratedLunarInterpretation).values(
                moon_sign=moon_sign,
                moon_house=moon_house,
                lunar_ascendant=lunar_ascendant,
                version=version,
                lang='fr',
                interpretation_full=interpretation,
                weekly_advice=weekly_advice,
                length=len(interpretation),
                model_used='claude-opus-4-5-20251101'
            )

            stmt = stmt.on_conflict_do_update(
                index_elements=['moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'],
                set_={
                    'interpretation_full': interpretation,
                    'weekly_advice': weekly_advice,
                    'length': len(interpretation),
                    'model_used': 'claude-opus-4-5-20251101',
                    'updated_at': datetime.now()
                }
            )

            await session.execute(stmt)
            await session.commit()
            return True

    except Exception as e:
        print(f"  [!] Erreur DB: {str(e)[:100]}")
        return False


def run_validation_mode(client: anthropic.Anthropic, version: int = 2):
    """
    Phase 1 : Genere 8 exemples de validation pour verification qualite
    """
    print("=" * 80)
    print("[*] PHASE 1 : GENERATION D'EXEMPLES DE VALIDATION")
    print("=" * 80)
    print(f"Mode: Validation ({len(VALIDATION_EXAMPLES)} exemples)")
    print(f"Version: v{version} (Opus 4.5 - 1728 combinaisons)")
    print(f"Modele: Claude Opus 4.5 (claude-opus-4-5-20251101)")
    print("=" * 80)
    print()

    results = []
    total_cost = 0.0

    for i, (moon_sign, moon_house, lunar_ascendant) in enumerate(VALIDATION_EXAMPLES, 1):
        moon_sign_fr = get_sign_label(moon_sign)
        lunar_asc_fr = get_sign_label(lunar_ascendant)

        print(f"\n[{i}/{len(VALIDATION_EXAMPLES)}] {moon_sign_fr} M{moon_house} ASC {lunar_asc_fr}")

        try:
            # Generer
            interpretation, weekly_advice, length = generate_lunar_interpretation(
                client, moon_sign, moon_house, lunar_ascendant
            )

            # Sauvegarder en markdown
            filepath = save_to_markdown(
                interpretation, weekly_advice, moon_sign, moon_house, lunar_ascendant, version
            )

            # Stats
            is_valid = 800 <= length <= 1400
            results.append({
                'moon_sign': moon_sign,
                'moon_house': moon_house,
                'lunar_ascendant': lunar_ascendant,
                'length': length,
                'valid': is_valid,
                'file': filepath,
                'weekly_advice': weekly_advice
            })

            # Cout estime (Opus 4.5: ~$0.015 par requete)
            total_cost += 0.015

            # Rate limiting
            time.sleep(0.5)

        except Exception as e:
            print(f"  [!] ECHEC: {str(e)[:100]}")
            results.append({
                'moon_sign': moon_sign,
                'moon_house': moon_house,
                'lunar_ascendant': lunar_ascendant,
                'error': str(e)
            })

    # Resume
    print("\n" + "=" * 80)
    print("[*] RESUME DE LA GENERATION")
    print("=" * 80)

    successful = [r for r in results if 'length' in r]
    failed = [r for r in results if 'error' in r]

    if successful:
        lengths = [r['length'] for r in successful]
        avg_length = sum(lengths) / len(lengths)
        min_length = min(lengths)
        max_length = max(lengths)
        valid_count = sum(1 for r in successful if r['valid'])

        print(f"\n[+] Succes: {len(successful)}/{len(VALIDATION_EXAMPLES)}")
        print(f"    Longueur moyenne: {avg_length:.0f} chars")
        print(f"    Longueur min/max: {min_length}/{max_length} chars")
        print(f"    Dans les limites (800-1400): {valid_count}/{len(successful)}")
        print(f"\n[$] Cout estime: ${total_cost:.2f} USD")

    if failed:
        print(f"\n[!] Echecs: {len(failed)}/{len(VALIDATION_EXAMPLES)}")
        for r in failed:
            print(f"    - {r['moon_sign']} M{r['moon_house']} ASC {r['lunar_ascendant']}: {r['error'][:80]}")

    print("\n" + "=" * 80)
    print("[+] PHASE 1 TERMINEE")
    print("=" * 80)
    print("\nProchaines etapes:")
    print("1. Verifier la qualite des exemples generes dans:")
    print(f"   {Path(__file__).parent.parent / f'data/lunar_interpretations/v{version}'}")
    print("2. Valider le ton, le style, la longueur, les weekly_advice")
    print("3. Si valide, lancer la generation complete avec: --mode full")
    print()


def run_full_mode(client: anthropic.Anthropic, version: int = 2, save_to_db: bool = False):
    """
    Phase 2 : Genere TOUTES les combinaisons (1728 interpretations)
    12 signes x 12 maisons x 12 ascendants = 1728
    """
    total = len(SIGNS) * len(HOUSES) * len(SIGNS)

    print("=" * 80)
    print("[*] PHASE 2 : GENERATION MASSIVE COMPLETE")
    print("=" * 80)
    print(f"Mode: Full (TOUTES les combinaisons)")
    print(f"Total: {total} interpretations (12 signes x 12 maisons x 12 ascendants)")
    print(f"Version: v{version} (Opus 4.5)")
    print(f"Modele: Claude Opus 4.5 (claude-opus-4-5-20251101)")
    print(f"Cout estime: ${total * 0.015:.2f} USD (~$25-30)")
    print(f"Temps estime: ~4-6 heures")
    print(f"Sauvegarde DB: {'OUI' if save_to_db else 'NON (markdown seulement)'}")
    print("=" * 80)

    # Demander confirmation
    response = input("\n[?] CONFIRMER la generation massive ? (y/N): ")
    if response.lower() != 'y':
        print("[!] Annule par l'utilisateur")
        return

    print("\n[*] Lancement de la generation...")

    count = 0
    errors = []
    lengths = []
    db_success = 0

    # Utiliser tqdm si disponible
    if HAS_TQDM:
        iterator = tqdm(total=total, desc="Generation", unit="interp")
    else:
        iterator = None

    for moon_sign_key, moon_sign_label in SIGNS:
        for moon_house in HOUSES:
            for lunar_asc_key, lunar_asc_label in SIGNS:
                try:
                    # Generer
                    interpretation, weekly_advice, length = generate_lunar_interpretation(
                        client, moon_sign_key, moon_house, lunar_asc_key
                    )

                    # Sauvegarder en markdown
                    save_to_markdown(
                        interpretation, weekly_advice,
                        moon_sign_key, moon_house, lunar_asc_key,
                        version
                    )

                    # Sauvegarder en DB si demande
                    if save_to_db:
                        success = asyncio.run(insert_to_database(
                            moon_sign_key, moon_house, lunar_asc_key,
                            interpretation, weekly_advice, version
                        ))
                        if success:
                            db_success += 1

                    # Stats
                    count += 1
                    lengths.append(length)

                    if iterator:
                        iterator.update(1)

                    # Checkpoint tous les 100 fichiers
                    if count % 100 == 0:
                        avg = sum(lengths) / len(lengths) if lengths else 0
                        msg = f"\n[*] Checkpoint: {count}/{total} | Moyenne: {avg:.0f} chars | DB: {db_success}"
                        if iterator:
                            iterator.write(msg)
                        else:
                            print(msg)

                    # Rate limiting
                    time.sleep(0.5)

                except Exception as e:
                    errors.append((moon_sign_key, moon_house, lunar_asc_key, str(e)))
                    if iterator:
                        iterator.update(1)

    if iterator:
        iterator.close()

    # Resume final
    print("\n" + "=" * 80)
    print("[*] RESUME FINAL")
    print("=" * 80)
    print(f"\n[+] Fichiers crees: {count}/{total}")

    if save_to_db:
        print(f"[+] Insertions DB: {db_success}/{count}")

    if lengths:
        avg_length = sum(lengths) / len(lengths)
        min_length = min(lengths)
        max_length = max(lengths)
        valid_count = sum(1 for l in lengths if 800 <= l <= 1400)

        print(f"    Longueur moyenne: {avg_length:.0f} chars")
        print(f"    Longueur min/max: {min_length}/{max_length} chars")
        print(f"    Dans les limites (800-1400): {valid_count}/{len(lengths)}")
        print(f"\n[$] Cout total: ${count * 0.015:.2f} USD")

    if errors:
        print(f"\n[!] Erreurs: {len(errors)}")
        for moon_sign, moon_house, lunar_asc, error in errors[:10]:
            print(f"    - {moon_sign} M{moon_house} ASC {lunar_asc}: {error[:60]}")
        if len(errors) > 10:
            print(f"    ... et {len(errors) - 10} autres erreurs")

    print("\n" + "=" * 80)
    print("[+] PHASE 2 TERMINEE")
    print("=" * 80)


def run_db_insert_mode(version: int = 2):
    """
    Phase 3 : Insere les fichiers markdown existants dans la DB
    Utile si la generation a ete faite sans --db
    """
    print("=" * 80)
    print("[*] PHASE 3 : INSERTION EN BASE DE DONNEES")
    print("=" * 80)

    # Scanner les fichiers markdown existants
    data_dir = Path(__file__).parent.parent / f"data/lunar_interpretations/v{version}"

    if not data_dir.exists():
        print(f"[!] Dossier non trouve: {data_dir}")
        return

    # Trouver tous les fichiers markdown
    md_files = list(data_dir.glob("**/*.md"))
    print(f"[*] Fichiers trouves: {len(md_files)}")

    if not md_files:
        print("[!] Aucun fichier a inserer")
        return

    # Demander confirmation
    response = input(f"\n[?] Inserer {len(md_files)} interpretations en DB ? (y/N): ")
    if response.lower() != 'y':
        print("[!] Annule par l'utilisateur")
        return

    success_count = 0
    error_count = 0

    if HAS_TQDM:
        iterator = tqdm(md_files, desc="Insertion DB", unit="file")
    else:
        iterator = md_files

    for filepath in iterator:
        try:
            # Lire le fichier
            content = filepath.read_text(encoding='utf-8')

            # Parser le frontmatter YAML
            import yaml

            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    interpretation = parts[2].strip()

                    moon_sign = frontmatter.get('moon_sign')
                    moon_house = frontmatter.get('moon_house')
                    lunar_ascendant = frontmatter.get('lunar_ascendant')
                    weekly_advice = frontmatter.get('weekly_advice', {})

                    if moon_sign and moon_house and lunar_ascendant:
                        success = asyncio.run(insert_to_database(
                            moon_sign, moon_house, lunar_ascendant,
                            interpretation, weekly_advice, version
                        ))
                        if success:
                            success_count += 1
                        else:
                            error_count += 1
                    else:
                        error_count += 1
                else:
                    error_count += 1
            else:
                error_count += 1

        except Exception as e:
            error_count += 1
            if not HAS_TQDM:
                print(f"  [!] Erreur {filepath.name}: {str(e)[:50]}")

    print("\n" + "=" * 80)
    print("[*] RESUME INSERTION")
    print("=" * 80)
    print(f"[+] Succes: {success_count}/{len(md_files)}")
    print(f"[!] Erreurs: {error_count}/{len(md_files)}")
    print("=" * 80)


def main():
    """Point d'entree principal"""
    parser = argparse.ArgumentParser(
        description='Genere les interpretations lunaires v2 avec Claude Opus 4.5'
    )
    parser.add_argument(
        '--mode',
        choices=['validation', 'full', 'db-insert'],
        default='validation',
        help='Mode: validation (8 exemples), full (1728), db-insert (depuis fichiers)'
    )
    parser.add_argument(
        '--version',
        type=int,
        default=2,
        help='Version du prompt lunaire (defaut: 2)'
    )
    parser.add_argument(
        '--db',
        action='store_true',
        help='Sauvegarder aussi en base de donnees (mode full uniquement)'
    )

    args = parser.parse_args()

    # Mode db-insert ne necessite pas de cle API
    if args.mode == 'db-insert':
        run_db_insert_mode(args.version)
        return

    # Verifier la cle API
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("[!] ERREUR: ANTHROPIC_API_KEY non defini dans .env")
        print("\nDefinir la variable d'environnement:")
        print("  export ANTHROPIC_API_KEY=sk-ant-...")
        print("\nOu ajouter dans .env:")
        print("  ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    # Creer client Anthropic
    client = anthropic.Anthropic(api_key=api_key)

    # Lancer le mode approprie
    if args.mode == 'validation':
        run_validation_mode(client, args.version)
    else:
        run_full_mode(client, args.version, save_to_db=args.db)


if __name__ == "__main__":
    main()
