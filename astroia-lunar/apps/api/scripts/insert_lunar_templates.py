#!/usr/bin/env python3
"""
Script d'insertion des templates de révolution lunaire en base.

Structure par couches :
- 12 climats par signe (lunar_climate)
- 12 focus par maison (lunar_focus)
- 12 approches par ascendant (lunar_approach)

Total : 36 entrées
"""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation


# =============================================================================
# 1. CLIMATS PAR SIGNE (12 entrées)
# Tonalité émotionnelle du mois - ce que tu ressens
# =============================================================================

LUNAR_CLIMATE_BY_SIGN = {
    'Aries': """**Climat du mois : Impulsion & Affirmation**

Ce mois lunaire t'invite à l'action directe. Tu ressens une impatience productive, un besoin de démarrer des choses, de prendre des initiatives. Les émotions circulent vite : colère rapide mais qui ne dure pas, enthousiasme contagieux, envie de te battre pour ce qui compte.

**Énergie dominante** : Feu, démarrage, courage
**Besoin principal** : Agir, décider, avancer
**Piège à éviter** : Confondre impulsivité et intuition""",

    'Taurus': """**Climat du mois : Ancrage & Stabilité**

Ce mois lunaire t'invite à ralentir et savourer. Tu ressens un besoin de confort, de sécurité matérielle, de plaisirs sensoriels. Les émotions sont stables mais tenaces : quand tu t'attaches, c'est pour de bon. Bon moment pour construire sur du solide.

**Énergie dominante** : Terre, patience, sensualité
**Besoin principal** : Sécurité, confort, plaisir des sens
**Piège à éviter** : S'entêter par peur du changement""",

    'Gemini': """**Climat du mois : Curiosité & Échanges**

Ce mois lunaire stimule ton mental. Tu ressens un besoin de communiquer, d'apprendre, de papillonner entre plusieurs sujets. Les émotions sont légères et changeantes : tu passes vite d'un état à l'autre. Bon moment pour les échanges, les petits déplacements, les apprentissages.

**Énergie dominante** : Air, mouvement mental, adaptabilité
**Besoin principal** : Stimulation intellectuelle, variété, connexion
**Piège à éviter** : Se disperser sans rien approfondir""",

    'Cancer': """**Climat du mois : Refuge & Sensibilité**

Ce mois lunaire éveille ton besoin de cocon. Tu te sens plus perméable aux ambiances, plus sensible aux non-dits familiaux, plus attaché à ce qui est familier. C'est un temps pour nourrir et être nourri, pour revenir aux sources qui te ressourcent.

**Énergie dominante** : Eau, protection, mémoire
**Besoin principal** : Sécurité affective, intimité, appartenance
**Piège à éviter** : Te replier par peur du monde extérieur""",

    'Leo': """**Climat du mois : Expression & Rayonnement**

Ce mois lunaire te pousse sur le devant de la scène. Tu ressens un besoin de briller, de créer, d'être reconnu pour ce que tu es. Les émotions sont généreuses et théâtrales : tu vis tout en grand. Bon moment pour les projets créatifs et les déclarations.

**Énergie dominante** : Feu, créativité, générosité
**Besoin principal** : Reconnaissance, expression de soi, admiration
**Piège à éviter** : Chercher l'approbation au détriment de l'authenticité""",

    'Virgo': """**Climat du mois : Analyse & Amélioration**

Ce mois lunaire active ton sens pratique. Tu ressens un besoin d'ordre, d'utilité, de perfectionner ce qui peut l'être. Les émotions passent par le filtre de la raison : tu analyses ce que tu ressens avant de l'exprimer. Bon moment pour trier, organiser, optimiser.

**Énergie dominante** : Terre, méthode, discernement
**Besoin principal** : Être utile, comprendre, améliorer
**Piège à éviter** : Critiquer (toi ou les autres) au lieu d'accepter""",

    'Libra': """**Climat du mois : Harmonie & Relation**

Ce mois lunaire t'oriente vers l'autre. Tu ressens un besoin d'équilibre, de beauté, de partage. Les émotions cherchent la mesure : tu évites les extrêmes, tu veux que tout le monde soit content. Bon moment pour les négociations, les collaborations, les choix esthétiques.

**Énergie dominante** : Air, diplomatie, esthétique
**Besoin principal** : Paix relationnelle, beauté, justice
**Piège à éviter** : Te perdre dans le compromis permanent""",

    'Scorpio': """**Climat du mois : Intensité & Transformation**

Ce mois lunaire te plonge dans les profondeurs. Tu ressens les choses avec une intensité rare, tu perçois ce qui est caché, tu ne te contentes pas des apparences. Les émotions sont puissantes et transformatrices : quelque chose meurt pour que quelque chose naisse.

**Énergie dominante** : Eau, profondeur, régénération
**Besoin principal** : Vérité, intimité authentique, transformation
**Piège à éviter** : Ruminer ou manipuler au lieu de traverser""",

    'Sagittarius': """**Climat du mois : Expansion & Optimisme**

Ce mois lunaire élargit tes horizons. Tu ressens un besoin de sens, d'aventure, de vision plus large. Les émotions sont enthousiastes et confiantes : tu crois en la vie, en l'avenir, en quelque chose de plus grand. Bon moment pour voyager, apprendre, enseigner.

**Énergie dominante** : Feu, foi, exploration
**Besoin principal** : Liberté, sens, horizons nouveaux
**Piège à éviter** : Fuir le quotidien au lieu de l'habiter""",

    'Capricorn': """**Climat du mois : Structure & Responsabilité**

Ce mois lunaire te rappelle à l'essentiel. Tu ressens un besoin de solidité, d'accomplissement, de résultats concrets. Les émotions sont contenues mais profondes : tu ne montres pas tout ce que tu ressens. Bon moment pour les projets long terme, les décisions mûries.

**Énergie dominante** : Terre, ambition, endurance
**Besoin principal** : Accomplissement, respect, structure
**Piège à éviter** : Sacrifier le présent pour un futur hypothétique""",

    'Aquarius': """**Climat du mois : Liberté & Innovation**

Ce mois lunaire secoue les habitudes. Tu ressens un besoin d'originalité, de détachement, de vision collective. Les émotions sont objectives et parfois distantes : tu observes ce que tu ressens autant que tu le vis. Bon moment pour innover, militer, penser autrement.

**Énergie dominante** : Air, indépendance, humanisme
**Besoin principal** : Liberté, originalité, contribution au collectif
**Piège à éviter** : Te couper de tes émotions au nom de la raison""",

    'Pisces': """**Climat du mois : Dissolution & Intuition**

Ce mois lunaire efface les frontières. Tu ressens une sensibilité amplifiée, une porosité aux ambiances, une connexion au subtil. Les émotions sont fluides et parfois confuses : tu absorbes ce qui t'entoure. Bon moment pour la créativité, la spiritualité, le lâcher-prise.

**Énergie dominante** : Eau, imagination, compassion
**Besoin principal** : Fusion, inspiration, transcendance
**Piège à éviter** : Te noyer dans les émotions des autres""",
}


# =============================================================================
# 2. FOCUS PAR MAISON (12 entrées)
# Domaine de vie activé - où ça se joue
# =============================================================================

LUNAR_FOCUS_BY_HOUSE = {
    1: """**Focus du mois : Toi-même**

La Lune traverse ta Maison 1 : c'est toi qui es au centre ce mois-ci. Ta façon de te présenter au monde, ton image, ton corps, ta première impression — tout ça est activé. Bon moment pour initier quelque chose de personnel, changer de look, affirmer qui tu es.

**Questions clés** : Comment je me présente ? Qu'est-ce que je veux incarner ?
**Actions favorisées** : Nouveaux départs, affirmation de soi, prendre soin de son corps""",

    2: """**Focus du mois : Tes ressources**

La Lune traverse ta Maison 2 : tes finances et ta valeur personnelle sont au centre ce mois-ci. Ce que tu possèdes, ce que tu gagnes, ce que tu vaux — tout ça demande ton attention. Bon moment pour gérer ton budget, développer un talent, négocier ta rémunération.

**Questions clés** : Qu'est-ce qui a vraiment de la valeur pour moi ? Comment je génère mes ressources ?
**Actions favorisées** : Gestion financière, développement de compétences, achats importants""",

    3: """**Focus du mois : Ta communication**

La Lune traverse ta Maison 3 : les échanges et apprentissages sont au centre ce mois-ci. Frères et sœurs, voisinage, déplacements courts, informations — tout ça circule. Bon moment pour écrire, parler, apprendre, régler des affaires administratives.

**Questions clés** : Qu'est-ce que j'ai besoin de dire ? Qu'est-ce que j'ai envie d'apprendre ?
**Actions favorisées** : Conversations importantes, formations courtes, courriers, petits voyages""",

    4: """**Focus du mois : Ton foyer**

La Lune traverse ta Maison 4 : ta vie privée et tes racines sont au centre ce mois-ci. Famille, maison, origines, vie intérieure — tout ça t'appelle. Bon moment pour les retrouvailles familiales, les travaux chez toi, l'introspection.

**Questions clés** : Où est-ce que je me sens chez moi ? Qu'est-ce que mes racines m'ont transmis ?
**Actions favorisées** : Aménagement intérieur, rencontres familiales, travail sur l'histoire personnelle""",

    5: """**Focus du mois : Ta créativité**

La Lune traverse ta Maison 5 : l'expression de toi et le plaisir sont au centre ce mois-ci. Créations, amours, enfants, jeux — tout ce qui fait vibrer ton cœur est activé. Bon moment pour créer, séduire, t'amuser, prendre des risques ludiques.

**Questions clés** : Qu'est-ce qui me fait me sentir vivant ? Comment j'exprime ma singularité ?
**Actions favorisées** : Projets créatifs, sorties, romance, activités avec les enfants""",

    6: """**Focus du mois : Ton quotidien**

La Lune traverse ta Maison 6 : ta routine et ta santé sont au centre ce mois-ci. Travail quotidien, hygiène de vie, organisation, service — tout ça demande des ajustements. Bon moment pour optimiser tes habitudes, consulter un médecin, améliorer ton efficacité.

**Questions clés** : Comment je prends soin de moi au quotidien ? Qu'est-ce que je peux améliorer ?
**Actions favorisées** : Nouvelles routines santé, organisation du travail, tri et rangement""",

    7: """**Focus du mois : Tes relations**

La Lune traverse ta Maison 7 : les partenariats sont au centre ce mois-ci. Couple, associé, collaborateur proche — les relations en tête-à-tête demandent ton attention. Bon moment pour négocier, équilibrer, regarder ce que l'autre te renvoie de toi-même.

**Questions clés** : Comment je fais équipe ? Qu'est-ce que mes relations m'apprennent sur moi ?
**Actions favorisées** : Discussions de couple, signatures de contrats, médiation""",

    8: """**Focus du mois : Tes transformations**

La Lune traverse ta Maison 8 : les crises et ressources partagées sont au centre ce mois-ci. Héritages, dettes, sexualité, ce qui doit mourir pour renaître — tout ça remonte. Bon moment pour régler des affaires d'argent commun, traverser une peur, approfondir l'intimité.

**Questions clés** : Qu'est-ce que je dois lâcher ? Qu'est-ce qui cherche à se transformer en moi ?
**Actions favorisées** : Règlements financiers, thérapie, conversations profondes""",

    9: """**Focus du mois : Ton expansion**

La Lune traverse ta Maison 9 : ta vision et tes horizons sont au centre ce mois-ci. Voyages, études, spiritualité, sens de la vie — tout ce qui élargit ta perspective t'appelle. Bon moment pour partir, publier, enseigner, explorer une philosophie.

**Questions clés** : Qu'est-ce que je crois vraiment ? Où ai-je envie d'aller ?
**Actions favorisées** : Voyages lointains, formations longues, publication, enseignement""",

    10: """**Focus du mois : Ta carrière**

La Lune traverse ta Maison 10 : ta vie professionnelle et ta réputation sont au centre ce mois-ci. Ambitions, statut social, accomplissements publics — tout ça est sous le projecteur. Bon moment pour les avancées de carrière, les prises de responsabilité, les décisions professionnelles.

**Questions clés** : Quelle empreinte je veux laisser ? Où en suis-je de mes ambitions ?
**Actions favorisées** : Demandes de promotion, projets visibles, rencontres professionnelles stratégiques""",

    11: """**Focus du mois : Tes projets collectifs**

La Lune traverse ta Maison 11 : tes amitiés et idéaux sont au centre ce mois-ci. Groupes, réseaux, causes, rêves d'avenir — tout ce qui dépasse l'individuel t'appelle. Bon moment pour militer, réseauter, rejoindre une communauté, planifier le futur.

**Questions clés** : À quel collectif j'appartiens ? Quel monde je veux contribuer à créer ?
**Actions favorisées** : Événements de groupe, networking, projets associatifs, vision long terme""",

    12: """**Focus du mois : Ton intériorité**

La Lune traverse ta Maison 12 : ta vie invisible est au centre ce mois-ci. Inconscient, spiritualité, secrets, ce qui est caché ou refoulé — tout ça remonte à la surface. Bon moment pour la retraite, la méditation, le travail thérapeutique, le lâcher-prise.

**Questions clés** : Qu'est-ce que je fuis ? Qu'est-ce qui cherche à émerger de mon inconscient ?
**Actions favorisées** : Solitude choisie, pratiques spirituelles, thérapie, repos profond""",
}


# =============================================================================
# 3. APPROCHES PAR ASCENDANT (12 entrées)
# Comment tu abordes ce mois - ta stratégie instinctive
# =============================================================================

LUNAR_APPROACH_BY_ASCENDANT = {
    'Aries': """**Ton approche ce mois : Foncer d'abord**

Avec l'ascendant lunaire en Bélier, tu abordes ce cycle en mode conquérant. Ta première réaction face aux situations nouvelles : agir vite, poser des actes, ne pas trop réfléchir. Cette approche directe te sert quand il faut débloquer une situation — elle te dessert si tu brûles des étapes importantes.

**Force** : Capacité à initier, courage, spontanéité
**Vigilance** : Écouter avant d'agir, laisser de la place aux autres""",

    'Taurus': """**Ton approche ce mois : Stabiliser d'abord**

Avec l'ascendant lunaire en Taureau, tu abordes ce cycle en mode prudent. Ta première réaction face aux situations nouvelles : prendre ton temps, évaluer la solidité, chercher le confort. Cette approche posée te sert pour construire du durable — elle te dessert si tu résistes trop au changement.

**Force** : Patience, fiabilité, sens pratique
**Vigilance** : Accepter l'inconfort temporaire du mouvement""",

    'Gemini': """**Ton approche ce mois : Comprendre d'abord**

Avec l'ascendant lunaire en Gémeaux, tu abordes ce cycle en mode curieux. Ta première réaction face aux situations nouvelles : poser des questions, chercher l'information, explorer les options. Cette approche mentale te sert pour naviguer dans la complexité — elle te dessert si tu restes bloqué dans l'analyse.

**Force** : Adaptabilité, intelligence relationnelle, vivacité
**Vigilance** : Passer à l'action même sans tout savoir""",

    'Cancer': """**Ton approche ce mois : Ressentir d'abord**

Avec l'ascendant lunaire en Cancer, tu abordes ce cycle en mode réceptif. Ta première réaction face aux situations nouvelles : sentir l'ambiance, évaluer la sécurité émotionnelle, protéger ce qui est fragile. Cette approche intuitive te sert pour créer des liens — elle te dessert si tu te fermes par peur d'être blessé.

**Force** : Empathie, intuition, capacité à nourrir
**Vigilance** : Ne pas laisser la peur dicter tes choix""",

    'Leo': """**Ton approche ce mois : Briller d'abord**

Avec l'ascendant lunaire en Lion, tu abordes ce cycle en mode rayonnant. Ta première réaction face aux situations nouvelles : prendre les choses en main, attirer l'attention, montrer l'exemple. Cette approche charismatique te sert pour inspirer — elle te dessert si tu as besoin d'applaudissements pour avancer.

**Force** : Leadership naturel, générosité, confiance
**Vigilance** : Accepter de ne pas toujours être au centre""",

    'Virgo': """**Ton approche ce mois : Analyser d'abord**

Avec l'ascendant lunaire en Vierge, tu abordes ce cycle en mode méthodique. Ta première réaction face aux situations nouvelles : observer les détails, identifier ce qui fonctionne et ce qui doit être corrigé. Cette approche analytique te sert pour optimiser — elle te dessert si tu te perds dans les détails au détriment de la vision d'ensemble.

**Force** : Sens pratique, discernement, efficacité
**Vigilance** : Ne pas laisser le perfectionnisme bloquer l'action""",

    'Libra': """**Ton approche ce mois : Harmoniser d'abord**

Avec l'ascendant lunaire en Balance, tu abordes ce cycle en mode diplomatique. Ta première réaction face aux situations nouvelles : chercher le consensus, peser le pour et le contre, créer de la beauté. Cette approche équilibrée te sert pour les négociations — elle te dessert si tu évites les conflits nécessaires.

**Force** : Diplomatie, sens esthétique, justice
**Vigilance** : Oser prendre position même si tout le monde n'est pas content""",

    'Scorpio': """**Ton approche ce mois : Sonder d'abord**

Avec l'ascendant lunaire en Scorpion, tu abordes ce cycle en mode intense. Ta première réaction face aux situations nouvelles : chercher ce qui est caché, évaluer les enjeux de pouvoir, aller au fond des choses. Cette approche pénétrante te sert pour transformer — elle te dessert si tu vois des complots partout.

**Force** : Perspicacité, résilience, authenticité
**Vigilance** : Faire confiance même sans tout contrôler""",

    'Sagittarius': """**Ton approche ce mois : Élargir d'abord**

Avec l'ascendant lunaire en Sagittaire, tu abordes ce cycle en mode expansif. Ta première réaction face aux situations nouvelles : voir le positif, chercher le sens, viser plus loin. Cette approche optimiste te sert pour garder le cap — elle te dessert si tu ignores les détails pratiques.

**Force** : Enthousiasme, vision, foi en l'avenir
**Vigilance** : Rester ancré dans le réel tout en rêvant grand""",

    'Capricorn': """**Ton approche ce mois : Structurer d'abord**

Avec l'ascendant lunaire en Capricorne, tu abordes ce cycle en mode stratégique. Ta première réaction face aux situations nouvelles : évaluer les enjeux long terme, identifier les étapes, assumer tes responsabilités. Cette approche mature te sert pour bâtir — elle te dessert si tu sacrifies le présent pour un futur hypothétique.

**Force** : Ambition, discipline, endurance
**Vigilance** : T'autoriser le plaisir et la légèreté""",

    'Aquarius': """**Ton approche ce mois : Innover d'abord**

Avec l'ascendant lunaire en Verseau, tu abordes ce cycle en mode original. Ta première réaction face aux situations nouvelles : penser différemment, questionner les conventions, chercher une voie alternative. Cette approche innovante te sert pour révolutionner — elle te dessert si tu rejettes tout ce qui est traditionnel par principe.

**Force** : Originalité, vision collective, indépendance
**Vigilance** : Accepter que certaines traditions ont du sens""",

    'Pisces': """**Ton approche ce mois : Ressentir d'abord**

Avec l'ascendant lunaire en Poissons, tu abordes ce cycle en mode fluide. Ta première réaction face aux situations nouvelles : t'adapter intuitivement, te laisser guider par l'invisible, faire confiance au flow. Cette approche réceptive te sert pour la créativité — elle te dessert si tu perds tes repères dans la confusion.

**Force** : Intuition, compassion, créativité
**Vigilance** : Garder un pied sur terre et des limites claires""",
}


async def insert_all_templates():
    """Insère tous les templates lunaires en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        # 1. Insérer les CLIMATS PAR SIGNE
        print("\n📍 Insertion des CLIMATS PAR SIGNE...")
        for sign, content in LUNAR_CLIMATE_BY_SIGN.items():
            result = await db.execute(
                select(PregeneratedLunarInterpretation).where(
                    PregeneratedLunarInterpretation.moon_sign == sign,
                    PregeneratedLunarInterpretation.moon_house == 0,  # 0 = template climat
                    PregeneratedLunarInterpretation.lunar_ascendant == '_climate_',
                    PregeneratedLunarInterpretation.version == 1,
                    PregeneratedLunarInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"  ⏭️  SKIP climate/{sign} (existe déjà)")
                skipped += 1
                continue

            entry = PregeneratedLunarInterpretation(
                moon_sign=sign,
                moon_house=0,  # Convention: 0 = template climat
                lunar_ascendant='_climate_',  # Convention: marqueur spécial
                version=1,
                lang='fr',
                interpretation_full=content.strip(),
                weekly_advice=None,
                length=len(content.strip()),
                model_used='manual'
            )
            db.add(entry)
            print(f"  ✅ INSERT climate/{sign} ({len(content.strip())} chars)")
            inserted += 1

        # 2. Insérer les FOCUS PAR MAISON
        print("\n📍 Insertion des FOCUS PAR MAISON...")
        for house, content in LUNAR_FOCUS_BY_HOUSE.items():
            result = await db.execute(
                select(PregeneratedLunarInterpretation).where(
                    PregeneratedLunarInterpretation.moon_sign == '_focus_',
                    PregeneratedLunarInterpretation.moon_house == house,
                    PregeneratedLunarInterpretation.lunar_ascendant == '_focus_',
                    PregeneratedLunarInterpretation.version == 1,
                    PregeneratedLunarInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"  ⏭️  SKIP focus/M{house} (existe déjà)")
                skipped += 1
                continue

            entry = PregeneratedLunarInterpretation(
                moon_sign='_focus_',  # Convention: marqueur spécial
                moon_house=house,
                lunar_ascendant='_focus_',  # Convention: marqueur spécial
                version=1,
                lang='fr',
                interpretation_full=content.strip(),
                weekly_advice=None,
                length=len(content.strip()),
                model_used='manual'
            )
            db.add(entry)
            print(f"  ✅ INSERT focus/M{house} ({len(content.strip())} chars)")
            inserted += 1

        # 3. Insérer les APPROCHES PAR ASCENDANT
        print("\n📍 Insertion des APPROCHES PAR ASCENDANT...")
        for ascendant, content in LUNAR_APPROACH_BY_ASCENDANT.items():
            result = await db.execute(
                select(PregeneratedLunarInterpretation).where(
                    PregeneratedLunarInterpretation.moon_sign == '_approach_',
                    PregeneratedLunarInterpretation.moon_house == 0,
                    PregeneratedLunarInterpretation.lunar_ascendant == ascendant,
                    PregeneratedLunarInterpretation.version == 1,
                    PregeneratedLunarInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"  ⏭️  SKIP approach/{ascendant} (existe déjà)")
                skipped += 1
                continue

            entry = PregeneratedLunarInterpretation(
                moon_sign='_approach_',  # Convention: marqueur spécial
                moon_house=0,
                lunar_ascendant=ascendant,
                version=1,
                lang='fr',
                interpretation_full=content.strip(),
                weekly_advice=None,
                length=len(content.strip()),
                model_used='manual'
            )
            db.add(entry)
            print(f"  ✅ INSERT approach/{ascendant} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")
        print(f"   Total attendu: 36 (12 climats + 12 focus + 12 approches)")


if __name__ == '__main__':
    asyncio.run(insert_all_templates())
