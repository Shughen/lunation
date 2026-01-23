"""
Script de correction des accents dans pregenerated_lunar_interpretations

Corrige tous les textes français sans accents en ajoutant les accents appropriés.
"""

import asyncio
import logging
from sqlalchemy import select, update
from database import AsyncSessionLocal
from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionnaire exhaustif de remplacement des mots sans accents
# Ordre: plus spécifique en premier (pour éviter les remplacements partiels)
ACCENT_FIXES = {
    # === PRÉPOSITIONS ET MOTS COURTS (très fréquents) ===
    # ORDRE IMPORTANT : patterns spécifiques en premier
    'active là ': 'active la ',  # Erreur fréquente
    'activé là ': 'active la ',  # Erreur fréquente
    ' là Maison': ' la Maison',
    ' là M': ' la M',
    "D'ou ": "D'où ",
    'd\'ou ': 'd\'où ',
    'Conseil cle': 'Conseil clé',
    'conseil cle': 'conseil clé',
    'lacher': 'lâcher',
    'relacher': 'relâcher',
    'gacher': 'gâcher',
    'Belier': 'Bélier',
    'belier': 'bélier',

    # Accords avec "énergie" (féminin)
    'energie émotionnelle est curieux': 'énergie émotionnelle est curieuse',
    'energie émotionnelle est structure': 'énergie émotionnelle est structurée',
    'energie émotionnelle est intuitif': 'énergie émotionnelle est intuitive',
    'energie émotionnelle est reflechi': 'énergie émotionnelle est réfléchie',
    'energie émotionnelle est dynamique': 'énergie émotionnelle est dynamique',
    'energie émotionnelle est analytique': 'énergie émotionnelle est analytique',
    'energie émotionnelle est harmonieux': 'énergie émotionnelle est harmonieuse',
    'energie émotionnelle est expansif': 'énergie émotionnelle est expansive',
    'energie émotionnelle est stable': 'énergie émotionnelle est stable',
    'energie émotionnelle est profonde': 'énergie émotionnelle est profonde',
    'energie émotionnelle est intense': 'énergie émotionnelle est intense',
    'energie émotionnelle est leger': 'énergie émotionnelle est légère',
    'energie émotionnelle est fluide': 'énergie émotionnelle est fluide',
    'energie émotionnelle est volatil': 'énergie émotionnelle est volatile',
    'energie émotionnelle est dense': 'énergie émotionnelle est dense',

    # Participes avec "porté par" → "portée par" (accord avec énergie)
    ', porté par un besoin': ', portée par un besoin',
    ', porte par un besoin': ', portée par un besoin',

    # Prépositions générales (après les patterns spécifiques)
    ' a ': ' à ',
    ' a l': ' à l',
    ' a t': ' à t',
    ' ou ': ' où ',
    'deja': 'déjà',
    ' ca ': ' ça ',

    # === NOMS EN -ITÉ ===
    'creativite': 'créativité',
    'securite': 'sécurité',
    'interiorite': 'intériorité',
    'spiritualite': 'spiritualité',
    'materialite': 'matérialité',
    'realite': 'réalité',
    'identite': 'identité',
    'stabilite': 'stabilité',
    'activite': 'activité',
    'visibilite': 'visibilité',
    'sensibilite': 'sensibilité',
    'fluidite': 'fluidité',
    'intensite': 'intensité',
    'originalite': 'originalité',
    'integrite': 'intégrité',
    'regularite': 'régularité',
    'singularite': 'singularité',
    'possibilite': 'possibilité',
    'capacite': 'capacité',
    'opportunite': 'opportunité',
    'priorite': 'priorité',
    'proximite': 'proximité',
    'intimite': 'intimité',
    'clarte': 'clarté',
    'generosite': 'générosité',
    'serenite': 'sérénité',
    'maturite': 'maturité',
    'liberte': 'liberté',
    'fragilite': 'fragilité',
    'authenticite': 'authenticité',
    'spontaneite': 'spontanéité',
    'sociabilite': 'sociabilité',
    'adaptabilite': 'adaptabilité',
    'receptivite': 'réceptivité',
    'curiosite': 'curiosité',
    'legerete': 'légèreté',
    'velocite': 'vélocité',
    'mobilite': 'mobilité',
    'fertilite': 'fertilité',
    'docilite': 'docilité',
    'fraternite': 'fraternité',
    'egalite': 'égalité',
    'neutralite': 'neutralité',
    'dualite': 'dualité',
    'variete': 'variété',
    'diversite': 'diversité',
    'complexite': 'complexité',
    'simplicite': 'simplicité',
    'universalite': 'universalité',
    'specificite': 'spécificité',
    'particularite': 'particularité',
    'totalite': 'totalité',
    'verite': 'vérité',
    'sincerite': 'sincérité',
    'fidelite': 'fidélité',
    'loyaute': 'loyauté',
    'celebrite': 'célébrité',
    'notoriete': 'notoriété',
    'autorite': 'autorité',
    'paternite': 'paternité',
    'maternite': 'maternité',
    'dignite': 'dignité',
    'sobriete': 'sobriété',
    'austerite': 'austérité',
    'severite': 'sévérité',
    'rigidite': 'rigidité',
    'solidite': 'solidité',
    'fermete': 'fermeté',
    'lenteur': 'lenteur',
    'profondeur': 'profondeur',

    # === NOMS EN -TION / -SION ===
    'emotion': 'émotion',
    'relation': 'relation',
    'evolution': 'évolution',
    'revolution': 'révolution',
    'elevation': 'élévation',
    'meditation': 'méditation',
    'reflexion': 'réflexion',
    'decision': 'décision',
    'precision': 'précision',
    'expression': 'expression',
    'depression': 'dépression',
    'regression': 'régression',
    'progression': 'progression',
    'tension': 'tension',
    'attention': 'attention',
    'intention': 'intention',
    'protection': 'protection',
    'ection': 'ection',
    'creation': 'création',
    'recreation': 'récréation',
    'generation': 'génération',
    'regeneration': 'régénération',
    'degeneration': 'dégénération',
    'renovation': 'rénovation',
    'transformation': 'transformation',
    'deviation': 'déviation',
    'elevation': 'élévation',

    # === NOMS EN -GIE ===
    'energie': 'énergie',
    'strategie': 'stratégie',
    'liturgie': 'liturgie',
    'allegorie': 'allégorie',
    'categorie': 'catégorie',

    # === NOMS FÉMININS COURANTS ===
    'generalite': 'généralité',
    'esthetique': 'esthétique',
    'necessite': 'nécessité',
    'qualite': 'qualité',
    'periode': 'période',
    'sphere': 'sphère',
    'atmosphere': 'atmosphère',
    'maniere': 'manière',
    'matiere': 'matière',
    'premiere': 'première',
    'derniere': 'dernière',
    'lumiere': 'lumière',
    'priere': 'prière',
    'carriere': 'carrière',
    'frontiere': 'frontière',
    'riviere': 'rivière',
    'preoccupation': 'préoccupation',
    'preoccupations': 'préoccupations',

    # === NOMS MASCULINS COURANTS ===
    'theme': 'thème',
    'systeme': 'système',
    'probleme': 'problème',
    'phenomene': 'phénomène',
    'schema': 'schéma',
    'cinema': 'cinéma',
    'poeme': 'poème',
    'blaspheme': 'blasphème',
    'stratageme': 'stratagème',

    # === VERBES CONJUGUÉS ===
    'integrer': 'intégrer',
    'integre': 'intègre',
    'integres': 'intègres',
    'integrons': 'intégrons',
    'integrez': 'intégrez',
    'integrent': 'intègrent',
    'integrait': 'intégrait',
    'integrerais': 'intégrerais',
    'integrerait': 'intégrerait',
    'generer': 'générer',
    'genere': 'génère',
    'generes': 'génères',
    'generons': 'générons',
    'generez': 'générez',
    'generent': 'génèrent',
    'reveler': 'révéler',
    'revele': 'révèle',
    'reveles': 'révèles',
    'revelons': 'révélons',
    'revelez': 'révélez',
    'revelent': 'révèlent',
    'eclaire': 'éclaire',
    'eclairer': 'éclairer',
    'eclaircir': 'éclaircir',
    'elever': 'élever',
    'eleve': 'élève',
    'eleves': 'élèves',
    'elevons': 'élevons',
    'elevez': 'élevez',
    'elevent': 'élèvent',
    'elaborer': 'élaborer',
    'elabore': 'élabore',
    'elabores': 'élabores',
    'elaborons': 'élaborons',
    'elaborez': 'élaborez',
    'elaborent': 'élaborent',
    'eviter': 'éviter',
    'evite': 'évite',
    'evites': 'évites',
    'evitons': 'évitons',
    'evitez': 'évitez',
    'evitent': 'évitent',
    'evoluer': 'évoluer',
    'evolue': 'évolue',
    'evolues': 'évolues',
    'evoluons': 'évoluons',
    'evoluez': 'évoluez',
    'evoluent': 'évoluent',
    'etre': 'être',
    'etais': 'étais',
    'etait': 'était',
    'etions': 'étions',
    'etiez': 'étiez',
    'etaient': 'étaient',
    'ecouter': 'écouter',
    'ecoute': 'écoute',
    'ecoutes': 'écoutes',
    'ecoutons': 'écoutons',
    'ecoutez': 'écoutez',
    'ecoutent': 'écoutent',
    'equilibrer': 'équilibrer',
    'equilibre': 'équilibre',
    'equilibres': 'équilibres',
    'equilibrons': 'équilibrons',
    'equilibrez': 'équilibrez',
    'equilibrent': 'équilibrent',

    # === PARTICIPES PASSÉS ===
    'active': 'activé',
    'activee': 'activée',
    'actives': 'activés',
    'activees': 'activées',
    'structure': 'structuré',
    'structuree': 'structurée',
    'structures': 'structurés',
    'structurees': 'structurées',
    'integree': 'intégrée',
    'integres': 'intégrés',
    'integrees': 'intégrées',
    'generee': 'générée',
    'generes': 'générés',
    'generees': 'générées',
    'revelee': 'révélée',
    'reveles': 'révélés',
    'revelees': 'révélées',
    'eclairee': 'éclairée',
    'eclaires': 'éclairés',
    'eclairees': 'éclairées',
    'elevee': 'élevée',
    'elevees': 'élevées',
    'elaboree': 'élaborée',
    'elaborees': 'élaborées',
    'reflechi': 'réfléchi',
    'reflechie': 'réfléchie',
    'reflechis': 'réfléchis',
    'reflechies': 'réfléchies',
    'equilibree': 'équilibrée',
    'equilibrees': 'équilibrées',
    'liee': 'liée',
    'liees': 'liées',
    'lies': 'liés',
    'lie': 'lié',

    # === ADJECTIFS ===
    'creatif': 'créatif',
    'creative': 'créative',
    'creatifs': 'créatifs',
    'creatives': 'créatives',
    'emotionnel': 'émotionnel',
    'emotionnelle': 'émotionnelle',
    'emotionnels': 'émotionnels',
    'emotionnelles': 'émotionnelles',
    'intuitif': 'intuitif',
    'intuitive': 'intuitive',
    'intuitifs': 'intuitifs',
    'intuitives': 'intuitives',
    'reflechi': 'réfléchi',
    'reflechie': 'réfléchie',
    'reflechis': 'réfléchis',
    'reflechies': 'réfléchies',
    'generale': 'générale',
    'general': 'général',
    'generaux': 'généraux',
    'generales': 'générales',
    'profonde': 'profonde',
    'profond': 'profond',
    'profonds': 'profonds',
    'profondes': 'profondes',
    'etendu': 'étendu',
    'etendue': 'étendue',
    'etendus': 'étendus',
    'etendues': 'étendues',
    'eleve': 'élevé',
    'elevee': 'élevée',
    'eleves': 'élevés',
    'elevees': 'élevées',
    'eclaire': 'éclairé',
    'eclairee': 'éclairée',
    'eclaires': 'éclairés',
    'eclairees': 'éclairées',
    'etroit': 'étroit',
    'etroite': 'étroite',
    'etroits': 'étroits',
    'etroites': 'étroites',

    # === NOMS PROPRES / SIGNES ===
    'Gemeaux': 'Gémeaux',
    'gemeaux': 'gémeaux',
    'Verseau': 'Verseau',
    'verseau': 'verseau',
    'Belier': 'Bélier',
    'belier': 'bélier',

    # === ADVERBES ===
    'particulierement': 'particulièrement',
    'specialement': 'spécialement',
    'generalement': 'généralement',
    'egalement': 'également',
    'eventuellement': 'éventuellement',
    'reellement': 'réellement',
    'evidemment': 'évidemment',
    'preferablement': 'préférablement',
    'precisement': 'précisément',
    'regulierement': 'régulièrement',
    'litteralement': 'littéralement',
    'naturellement': 'naturellement',
    'profondement': 'profondément',
    'intensement': 'intensément',
    'serieusement': 'sérieusement',
    'completement': 'complètement',
    'extremement': 'extrêmement',

    # === AUTRES MOTS COURANTS ===
    'evenement': 'événement',
    'evenements': 'événements',
    'etape': 'étape',
    'etapes': 'étapes',
    'etoile': 'étoile',
    'etoiles': 'étoiles',
    'eclat': 'éclat',
    'eclats': 'éclats',
    'meme': 'même',
    'memes': 'mêmes',
    'tete': 'tête',
    'tetes': 'têtes',
    'pret': 'prêt',
    'prete': 'prête',
    'prets': 'prêts',
    'pretes': 'prêtes',
    'francais': 'français',
    'francaise': 'française',
    'naitre': 'naître',
    'maitre': 'maître',
    'maitrise': 'maîtrise',
    'maitriser': 'maîtriser',
    'role': 'rôle',
    'roles': 'rôles',
    'controle': 'contrôle',
    'controler': 'contrôler',
    'difficulte': 'difficulté',
    'difficultes': 'difficultés',
    'dela': 'delà',
    'synthetique': 'synthétique',
    'esthetique': 'esthétique',
    'ethique': 'éthique',
    'poetique': 'poétique',
    'magnetique': 'magnétique',
    'energique': 'énergique',
    'theorique': 'théorique',
    'pratique': 'pratique',
    'mystique': 'mystique',
    'cosmique': 'cosmique',
    'karmique': 'karmique',
    'harmonique': 'harmonique',
    'melodique': 'mélodique',
    'rythmique': 'rythmique',
    'chaotique': 'chaotique',
    'heroique': 'héroïque',
    'stoique': 'stoïque',
    'egoiste': 'égoïste',
    'altruiste': 'altruiste',
    'idealiste': 'idéaliste',
    'realiste': 'réaliste',
    'materialiste': 'matérialiste',
    'spiritualiste': 'spiritualiste',
}


def fix_accents(text: str) -> str:
    """
    Corrige les accents manquants dans un texte français

    Args:
        text: Texte sans accents

    Returns:
        Texte avec accents corrigés
    """
    if not text:
        return text

    result = text

    # Appliquer tous les remplacements
    for wrong, correct in ACCENT_FIXES.items():
        result = result.replace(wrong, correct)

    return result


async def fix_all_interpretations():
    """
    Corrige tous les accents dans la table pregenerated_lunar_interpretations
    """
    async with AsyncSessionLocal() as db:
        # Récupérer toutes les entrées
        result = await db.execute(
            select(PregeneratedLunarInterpretation)
        )
        entries = result.scalars().all()

        logger.info(f"📊 Trouvé {len(entries)} entrées à corriger")

        count_updated = 0

        for entry in entries:
            original = entry.interpretation_full

            if original:
                # Corriger les accents
                fixed = fix_accents(original)

                # Si changement, mettre à jour
                if fixed != original:
                    entry.interpretation_full = fixed
                    count_updated += 1

                    if count_updated % 100 == 0:
                        logger.info(f"✅ Corrigé {count_updated} entrées...")

        # Commit
        await db.commit()

        logger.info(f"✅ Correction terminée : {count_updated}/{len(entries)} entrées mises à jour")

        # Afficher un échantillon
        result = await db.execute(
            select(PregeneratedLunarInterpretation)
            .where(PregeneratedLunarInterpretation.version == 2)
            .limit(2)
        )
        samples = result.scalars().all()

        logger.info("\n=== ÉCHANTILLON APRÈS CORRECTION ===")
        for sample in samples:
            logger.info(f"\n{sample.moon_sign} M{sample.moon_house} ASC {sample.lunar_ascendant}:")
            logger.info(f"{sample.interpretation_full[:300]}...")


if __name__ == "__main__":
    asyncio.run(fix_all_interpretations())
