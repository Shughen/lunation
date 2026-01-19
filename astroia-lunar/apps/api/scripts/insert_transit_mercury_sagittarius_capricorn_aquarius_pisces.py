#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Mercure en Sagittaire/Capricorne/Verseau/Poissons."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MERCURY_INTERPRETATIONS = {
    # SAGITTARIUS
    ('sagittarius', 1): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Tes idées s'élargissent — communique avec enthousiasme et vision.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 1, rendant ta communication plus optimiste et expansive. Tu veux partager ta vision et tes idées.

## Ce que tu pourrais vivre
- Une communication enthousiaste et inspirante
- L'envie de partager tes connaissances
- Des pensées qui visent large

## Conseils pour ce transit
- Partage tes idées avec enthousiasme
- Vise grand dans tes projets intellectuels
- Évite de promettre plus que tu ne peux tenir""",

    ('sagittarius', 2): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Tes réflexions financières voient grand — investis dans ton expansion.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 2, orientant tes pensées vers des projets financiers ambitieux. Tu veux investir dans ce qui t'élargit.

## Ce que tu pourrais vivre
- Un optimisme financier
- Des idées pour investir dans l'éducation ou les voyages
- L'envie de diversifier tes sources de revenus

## Conseils pour ce transit
- Investis dans ton développement personnel
- Évite les excès par optimisme
- Explore de nouvelles pistes de revenus""",

    ('sagittarius', 3): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Ta communication s'enflamme — partage ta vision avec enthousiasme.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 3, rendant ta communication plus inspirante et philosophique. Tu veux transmettre et enseigner.

## Ce que tu pourrais vivre
- Des conversations stimulantes sur les grandes idées
- L'envie d'apprendre et d'enseigner
- Des projets de voyage ou d'études

## Conseils pour ce transit
- Partage tes connaissances généreusement
- Apprends quelque chose qui t'inspire
- Évite de prêcher ou d'imposer tes vues""",

    ('sagittarius', 4): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Les discussions à la maison s'élargissent — apporte l'aventure au foyer.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 4, apportant un souffle d'ouverture dans les communications familiales. Tu veux de l'espace.

## Ce que tu pourrais vivre
- Des discussions philosophiques en famille
- L'envie de voyager avec ta famille
- Un besoin d'espace mental chez toi

## Conseils pour ce transit
- Partage tes visions avec ta famille
- Planifie des aventures familiales
- Apporte une touche d'ailleurs chez toi""",

    ('sagittarius', 5): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Ta créativité vise large — amuse-toi avec les grandes idées.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 5, stimulant ta créativité philosophique et ton goût pour l'aventure intellectuelle. Tu veux explorer.

## Ce que tu pourrais vivre
- Une créativité inspirée par les voyages ou la philosophie
- Des échanges amoureux stimulants intellectuellement
- L'envie de vivre de grandes aventures

## Conseils pour ce transit
- Lance des projets créatifs ambitieux
- En amour, partage tes rêves et visions
- Amuse-toi avec des idées et des découvertes""",

    ('sagittarius', 6): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Ton travail cherche du sens — trouve la philosophie dans le quotidien.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 6, créant un besoin de sens dans ton travail quotidien. Tu veux que tes tâches aient un but.

## Ce que tu pourrais vivre
- Un besoin de sens dans ton travail
- L'envie d'améliorer ta santé par des méthodes alternatives
- De l'impatience avec les tâches routinières

## Conseils pour ce transit
- Trouve le sens dans tes tâches quotidiennes
- Explore des approches de santé holistiques
- Évite de négliger les détails par excès d'enthousiasme""",

    ('sagittarius', 7): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Les dialogues avec tes partenaires s'élargissent — vise ensemble.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 7, rendant les échanges avec les partenaires plus stimulants et orientés vers l'avenir. Vous voulez grandir ensemble.

## Ce que tu pourrais vivre
- Des conversations sur l'avenir et les projets communs
- L'attirance pour des partenaires qui partagent ta vision
- L'envie de voyager ou d'apprendre avec ton partenaire

## Conseils pour ce transit
- Partage tes visions d'avenir avec ton partenaire
- Planifie des aventures ensemble
- Respecte la liberté de pensée de chacun""",

    ('sagittarius', 8): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Tes réflexions profondes trouvent du sens — cherche la sagesse dans les crises.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 8, apportant une vision philosophique aux transformations. Tu cherches le sens des épreuves.

## Ce que tu pourrais vivre
- Une approche philosophique des crises
- Des réflexions sur le sens de la vie et de la mort
- L'envie de comprendre les mécanismes profonds

## Conseils pour ce transit
- Cherche la leçon dans chaque épreuve
- Explore les philosophies de la transformation
- Aie confiance dans le processus de changement""",

    ('sagittarius', 9): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Ta soif de savoir est à son maximum — explore et enseigne.

## L'énergie du moment
Mercure en Sagittaire amplifie ta Maison 9, maximisant ta curiosité intellectuelle et ton goût pour les voyages. Tu veux tout apprendre et tout partager.

## Ce que tu pourrais vivre
- Une soif intense de connaissance
- Des projets de voyages et d'études
- L'envie d'enseigner et de transmettre

## Conseils pour ce transit
- Lance-toi dans des études ou des voyages
- Enseigne ce que tu sais
- Évite de te disperser dans trop de directions""",

    ('sagittarius', 10): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Ta communication professionnelle vise haut — partage ta vision.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 10, rendant ta communication professionnelle plus ambitieuse et inspirante. Tu veux viser plus haut.

## Ce que tu pourrais vivre
- Des opportunités liées à l'international ou à l'enseignement
- L'envie de viser des positions plus élevées
- Une communication qui inspire au travail

## Conseils pour ce transit
- Affiche tes ambitions professionnelles
- Développe ton expertise et partage-la
- Vise des postes à portée internationale""",

    ('sagittarius', 11): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Tes échanges avec tes amis visent haut — inspire ton réseau.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 11, rendant tes communications amicales plus inspirantes et tournées vers l'avenir. Tu veux un réseau qui partage ta vision.

## Ce que tu pourrais vivre
- Des conversations passionnantes sur l'avenir
- Des amitiés avec des personnes d'horizons variés
- Des projets collectifs ambitieux

## Conseils pour ce transit
- Inspire tes amis par ta vision
- Rejoins des groupes qui partagent tes idéaux
- Partage tes rêves pour l'avenir""",

    ('sagittarius', 12): """# ☿ Transit de Mercure en Sagittaire

**En une phrase :** Tes pensées intérieures s'élargissent — médite sur le sens de la vie.

## L'énergie du moment
Mercure en Sagittaire traverse ta Maison 12, orientant tes réflexions intérieures vers les grandes questions. Tu cherches le sens caché de l'existence.

## Ce que tu pourrais vivre
- Des réflexions profondes sur le sens de la vie
- Des intuitions et des révélations spirituelles
- L'envie de méditer et de te retirer

## Conseils pour ce transit
- Médite sur les grandes questions de l'existence
- Fais une retraite si possible
- Prépare ta prochaine expansion""",

    # CAPRICORN
    ('capricorn', 1): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Tes pensées se structurent — communique avec autorité et méthode.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 1, rendant ta communication plus structurée et professionnelle. Tu veux être pris au sérieux.

## Ce que tu pourrais vivre
- Une communication plus formelle et structurée
- Des pensées orientées vers les objectifs
- Un besoin de crédibilité intellectuelle

## Conseils pour ce transit
- Communique avec professionnalisme
- Structure tes idées avant de les présenter
- Évite d'être trop rigide""",

    ('capricorn', 2): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Tes réflexions financières se structurent — planifie à long terme.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 2, rendant ta gestion financière plus méthodique et stratégique. Tu veux construire une sécurité durable.

## Ce que tu pourrais vivre
- Une planification financière rigoureuse
- Des réflexions sur les investissements à long terme
- L'envie de construire une sécurité solide

## Conseils pour ce transit
- Planifie tes finances sur le long terme
- Investis dans des valeurs sûres
- Développe des compétences monnayables""",

    ('capricorn', 3): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Ta communication devient professionnelle — exprime-toi avec structure.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 3, rendant ta communication plus structurée et efficace. Tu veux des échanges qui servent.

## Ce que tu pourrais vivre
- Une communication formelle et efficace
- Des études ou formations professionnalisantes
- L'envie de formaliser tes idées

## Conseils pour ce transit
- Structure tes présentations et écrits
- Inscris-toi à une formation qualifiante
- Communique avec des objectifs clairs""",

    ('capricorn', 4): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Les discussions à la maison deviennent sérieuses — structure ta vie familiale.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 4, apportant du sérieux dans les communications familiales. Tu veux mettre de l'ordre chez toi.

## Ce que tu pourrais vivre
- Des discussions sérieuses sur la famille
- L'envie de planifier des projets immobiliers
- Un besoin de structure à la maison

## Conseils pour ce transit
- Discute des projets à long terme avec ta famille
- Planifie des améliorations de ton patrimoine
- Établis des règles claires à la maison""",

    ('capricorn', 5): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Ta créativité se structure — crée quelque chose de durable.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 5, rendant ta créativité plus orientée vers des résultats durables. Tu veux que tes créations comptent.

## Ce que tu pourrais vivre
- Une créativité orientée vers des projets structurés
- Des échanges amoureux plus sérieux
- L'envie de maîtriser une compétence créative

## Conseils pour ce transit
- Travaille sur un projet créatif à long terme
- En amour, discute de l'avenir
- Transforme un hobby en quelque chose de sérieux""",

    ('capricorn', 6): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Ton travail atteint son efficacité maximale — organise et excelle.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 6, maximisant ton efficacité et ton sens de l'organisation au travail. Tu veux des résultats.

## Ce que tu pourrais vivre
- Une productivité optimale
- Des méthodes de travail efficaces
- Une attention rigoureuse à ta santé

## Conseils pour ce transit
- Organise ton travail efficacement
- Établis des routines qui fonctionnent
- Consulte un professionnel de santé si nécessaire""",

    ('capricorn', 7): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Les discussions relationnelles se formalisent — clarifie tes engagements.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 7, rendant les communications avec les partenaires plus formelles et orientées vers les engagements. Tu veux de la clarté.

## Ce que tu pourrais vivre
- Des discussions sérieuses sur l'avenir de la relation
- Des négociations formelles en affaires
- L'envie de formaliser des accords

## Conseils pour ce transit
- Discute des engagements à long terme
- Formalise tes accords par écrit
- Sois clair sur tes attentes""",

    ('capricorn', 8): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Tes réflexions profondes deviennent stratégiques — planifie les transformations.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 8, rendant ton approche des transformations plus stratégique. Tu veux contrôler le changement.

## Ce que tu pourrais vivre
- Une planification des questions financières partagées
- Des réflexions stratégiques sur les changements
- L'envie de maîtriser les processus de transformation

## Conseils pour ce transit
- Planifie les successions ou héritages
- Aborde les transformations de façon méthodique
- Évite de vouloir tout contrôler""",

    ('capricorn', 9): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Ta quête de savoir se fait pragmatique — apprends ce qui mène quelque part.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 9, orientant ta curiosité vers des apprentissages qui ont des débouchés concrets. Tu veux une sagesse applicable.

## Ce que tu pourrais vivre
- Un intérêt pour des formations certifiantes
- Des voyages d'affaires ou professionnels
- Une philosophie pragmatique de la vie

## Conseils pour ce transit
- Obtiens des diplômes ou certifications
- Voyage pour des raisons professionnelles
- Développe une vision réaliste du monde""",

    ('capricorn', 10): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Ta communication professionnelle est au sommet — assume ton expertise.

## L'énergie du moment
Mercure en Capricorne amplifie ta Maison 10, maximisant ta crédibilité et ton autorité professionnelle. C'est le moment de briller par ta compétence.

## Ce que tu pourrais vivre
- Une reconnaissance pour ton expertise
- Des opportunités de leadership intellectuel
- Une communication professionnelle impeccable

## Conseils pour ce transit
- Assume ton autorité intellectuelle
- Présente tes idées avec professionnalisme
- Construis ta réputation par tes paroles et actes""",

    ('capricorn', 11): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Tes échanges avec tes amis se structurent — construis des alliances durables.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 11, rendant tes communications amicales plus orientées vers des objectifs communs. Tu veux des résultats collectifs.

## Ce que tu pourrais vivre
- Des projets de groupe bien organisés
- Des amitiés avec des personnes influentes
- Des objectifs à long terme partagés

## Conseils pour ce transit
- Structure les projets collectifs
- Définis des objectifs clairs avec tes alliés
- Construis un réseau professionnel solide""",

    ('capricorn', 12): """# ☿ Transit de Mercure en Capricorne

**En une phrase :** Tes pensées intérieures se structurent — travaille méthodiquement sur toi.

## L'énergie du moment
Mercure en Capricorne traverse ta Maison 12, rendant ton travail intérieur plus méthodique. Tu peux comprendre et structurer ton inconscient.

## Ce que tu pourrais vivre
- Un travail méthodique sur tes blocages
- Des réflexions structurées sur ton passé
- L'envie de préparer discrètement tes projets

## Conseils pour ce transit
- Travaille sur tes blocages avec méthode
- Planifie en secret tes prochains objectifs
- Médite sur le sens de ton ambition""",

    # AQUARIUS
    ('aquarius', 1): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Tes idées deviennent originales — communique de façon innovante.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 1, rendant ta communication plus originale et avant-gardiste. Tu veux te démarquer par tes idées.

## Ce que tu pourrais vivre
- Des idées originales et innovantes
- L'envie de communiquer différemment
- Un détachement intellectuel

## Conseils pour ce transit
- Assume ton originalité intellectuelle
- Expérimente de nouvelles façons de communiquer
- Évite de te couper des autres par ton originalité""",

    ('aquarius', 2): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Tes réflexions financières s'innovent — explore des revenus alternatifs.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 2, orientant tes pensées vers des approches financières innovantes. Tu veux sortir des sentiers battus.

## Ce que tu pourrais vivre
- Des idées originales pour gagner de l'argent
- Un intérêt pour les nouvelles technologies financières
- Un détachement vis-à-vis des approches traditionnelles

## Conseils pour ce transit
- Explore des sources de revenus innovantes
- Informe-toi sur les nouvelles technologies
- Ne néglige pas les bases financières""",

    ('aquarius', 3): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Ta communication devient avant-gardiste — partage des idées qui sortent du lot.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 3, rendant ta communication plus originale et technologique. Tu veux des échanges qui sortent de l'ordinaire.

## Ce que tu pourrais vivre
- Des conversations sur des sujets innovants
- L'utilisation créative des technologies de communication
- Des idées qui bousculent

## Conseils pour ce transit
- Partage tes idées innovantes
- Utilise les réseaux sociaux de façon créative
- Connecte-toi avec des esprits originaux""",

    ('aquarius', 4): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Les discussions à la maison s'innovent — repense ton mode de vie.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 4, apportant des idées originales pour ta vie domestique. Tu veux un foyer qui sort de l'ordinaire.

## Ce que tu pourrais vivre
- Des idées innovantes pour ton habitat
- Des discussions sur des modes de vie alternatifs
- Un détachement vis-à-vis des traditions familiales

## Conseils pour ce transit
- Repense ton mode de vie domestique
- Apporte de la technologie chez toi
- Respecte les différences familiales""",

    ('aquarius', 5): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Ta créativité devient expérimentale — innove dans tes expressions.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 5, stimulant ta créativité vers des formes originales et technologiques. Tu veux créer différemment.

## Ce que tu pourrais vivre
- Une créativité orientée vers le digital ou l'innovation
- Des échanges amoureux atypiques
- L'envie d'expérimenter de nouvelles formes d'expression

## Conseils pour ce transit
- Expérimente des créations originales
- En amour, reste ouvert aux relations atypiques
- Utilise la technologie dans ta créativité""",

    ('aquarius', 6): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Ton travail s'émancipe — innove dans tes méthodes.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 6, créant un besoin d'innovation dans ton travail et tes routines. Tu veux faire différemment.

## Ce que tu pourrais vivre
- Des méthodes de travail innovantes
- Un intérêt pour des approches de santé alternatives
- L'envie de changer radicalement tes routines

## Conseils pour ce transit
- Innove dans tes méthodes de travail
- Explore des approches de santé nouvelles
- Garde une certaine structure malgré l'innovation""",

    ('aquarius', 7): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Les échanges relationnels s'émancipent — communique avec liberté.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 7, rendant les communications avec les partenaires plus libres et originales. Tu veux des échanges sans contrainte.

## Ce que tu pourrais vivre
- Des discussions sur la liberté dans les relations
- L'attirance pour des partenaires originaux
- Des échanges intellectuellement stimulants

## Conseils pour ce transit
- Communique librement avec tes partenaires
- Respecte l'indépendance intellectuelle de chacun
- Connecte-toi sur des idéaux communs""",

    ('aquarius', 8): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Tes réflexions profondes s'émancipent — pense différemment les transformations.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 8, apportant un regard innovant sur les transformations. Tu veux aborder les changements autrement.

## Ce que tu pourrais vivre
- Des approches innovantes de la transformation
- Un intérêt pour les technologies financières partagées
- Un détachement émotionnel face aux crises

## Conseils pour ce transit
- Explore des approches nouvelles du changement
- Détache-toi des vieilles façons de penser
- Évite le détachement émotionnel excessif""",

    ('aquarius', 9): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Ta quête de savoir devient futuriste — explore des idées d'avant-garde.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 9, orientant ta curiosité vers des domaines innovants et futuristes. Tu veux comprendre ce qui vient.

## Ce que tu pourrais vivre
- Un intérêt pour les idées futuristes
- L'envie de voyager vers des lieux d'innovation
- Des réflexions sur l'avenir de l'humanité

## Conseils pour ce transit
- Explore des courants de pensée progressistes
- Voyage vers des pôles d'innovation
- Connecte-toi avec des communautés internationales""",

    ('aquarius', 10): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Ta communication professionnelle innove — démarque-toi par tes idées.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 10, rendant ta communication professionnelle plus originale. Tu veux te faire remarquer par ton innovation.

## Ce que tu pourrais vivre
- Des opportunités dans des secteurs innovants
- Une reconnaissance pour tes idées originales
- L'envie de te positionner différemment professionnellement

## Conseils pour ce transit
- Propose des idées innovantes au travail
- Positionne-toi dans des secteurs d'avenir
- Assume ton originalité professionnelle""",

    ('aquarius', 11): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Tes échanges avec ton réseau sont au maximum — innove et connecte.

## L'énergie du moment
Mercure en Verseau amplifie ta Maison 11, maximisant tes échanges avec ton réseau et tes idées pour l'avenir. Tu es au cœur de l'innovation collective.

## Ce que tu pourrais vivre
- Une vie sociale très stimulante intellectuellement
- Des projets collectifs innovants
- Des échanges sur le futur et les idéaux

## Conseils pour ce transit
- Participe activement à des communautés innovantes
- Lance des projets collectifs d'avant-garde
- Partage ta vision du futur""",

    ('aquarius', 12): """# ☿ Transit de Mercure en Verseau

**En une phrase :** Tes pensées intérieures s'émancipent — libère ton mental des vieilles idées.

## L'énergie du moment
Mercure en Verseau traverse ta Maison 12, créant une libération des schémas de pensée anciens. Tu peux voir les choses autrement.

## Ce que tu pourrais vivre
- Des intuitions sur l'avenir
- Un détachement des vieilles façons de penser
- Des idées innovantes qui émergent de l'inconscient

## Conseils pour ce transit
- Libère-toi des pensées limitantes
- Médite sur ta contribution à l'humanité
- Prépare des idées nouvelles pour l'avenir""",

    # PISCES
    ('pisces', 1): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Tes pensées deviennent intuitives — communique avec ton âme.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 1, rendant ta communication plus intuitive et poétique. Tu ressens plus que tu ne penses.

## Ce que tu pourrais vivre
- Une pensée plus intuitive et moins logique
- Une communication plus artistique et sensible
- Des difficultés à être précis mais beaucoup de créativité

## Conseils pour ce transit
- Fais confiance à ton intuition
- Exprime-toi à travers l'art ou la poésie
- Sois patient avec les malentendus""",

    ('pisces', 2): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Tes réflexions financières deviennent intuitives — fais confiance au flux.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 2, rendant ton rapport aux finances plus intuitif et moins rationnel. Tu sens les opportunités.

## Ce que tu pourrais vivre
- Des intuitions financières à suivre
- Un détachement vis-à-vis du matériel
- Des opportunités liées à la créativité

## Conseils pour ce transit
- Écoute ton intuition financière
- Évite les décisions financières majeures
- Valorise les richesses non matérielles""",

    ('pisces', 3): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Ta communication devient poétique — exprime-toi avec l'âme.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 3, rendant ta communication plus intuitive et artistique. Tu parles avec le cœur plus qu'avec la tête.

## Ce que tu pourrais vivre
- Une communication poétique et inspirée
- Des intuitions dans les conversations
- Des difficultés à être concret mais beaucoup de sensibilité

## Conseils pour ce transit
- Exprime-toi à travers l'art
- Fais confiance à tes intuitions dans les échanges
- Sois patient avec les malentendus""",

    ('pisces', 4): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Les pensées sur le foyer deviennent rêveuses — crée un sanctuaire.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 4, rendant tes réflexions sur le foyer plus intuitives et spirituelles. Tu rêves d'un refuge.

## Ce que tu pourrais vivre
- Des rêveries sur ton foyer idéal
- Des conversations sensibles en famille
- L'envie de créer un espace spirituel chez toi

## Conseils pour ce transit
- Crée un espace de méditation chez toi
- Communique avec compassion en famille
- Laisse ton intuition guider tes choix domestiques""",

    ('pisces', 5): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Ta créativité devient inspirée — crée depuis ton âme.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 5, rendant ta créativité plus intuitive et spirituelle. Tu veux créer quelque chose qui touche l'âme.

## Ce que tu pourrais vivre
- Une créativité très inspirée et artistique
- Des échanges amoureux romantiques et poétiques
- L'envie de créer quelque chose de transcendant

## Conseils pour ce transit
- Crée depuis ton inspiration intérieure
- En amour, communique avec poésie
- Laisse-toi porter par la muse""",

    ('pisces', 6): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Ton travail devient intuitif — trouve le sens dans le service.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 6, rendant ton approche du travail plus intuitive et orientée vers le service. Tu veux aider.

## Ce que tu pourrais vivre
- Un travail guidé par l'intuition
- Un intérêt pour les pratiques de santé holistiques
- Des difficultés avec les tâches trop rationnelles

## Conseils pour ce transit
- Écoute ton intuition au travail
- Pratique des soins énergétiques ou le yoga
- Évite les environnements trop stressants""",

    ('pisces', 7): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Les échanges relationnels deviennent profonds — connecte-toi âme à âme.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 7, rendant les communications avec les partenaires plus intuitives et empathiques. Tu ressens ce que l'autre pense.

## Ce que tu pourrais vivre
- Des échanges télépathiques avec ton partenaire
- Une communication basée sur l'empathie
- Des malentendus possibles mais beaucoup de connexion

## Conseils pour ce transit
- Communique avec le cœur
- Fais confiance à ton intuition relationnelle
- Évite les attentes non exprimées""",

    ('pisces', 8): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Tes pensées profondes se dissolvent — lâche prise sur le mental.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 8, créant un processus de dissolution des vieilles pensées. Tu comprends au-delà du mental.

## Ce que tu pourrais vivre
- Des intuitions sur les mystères de la vie
- Un lâcher-prise mental face aux transformations
- Des expériences mystiques ou transpersonnelles

## Conseils pour ce transit
- Fais confiance à ta compréhension intuitive
- Lâche prise sur le besoin de tout comprendre
- Explore ta spiritualité""",

    ('pisces', 9): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Ta quête de savoir devient mystique — explore les dimensions spirituelles.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 9, orientant ta curiosité vers les enseignements spirituels et mystiques. Tu cherches une sagesse transcendante.

## Ce que tu pourrais vivre
- Un intérêt pour les traditions mystiques
- Des voyages intérieurs ou des retraites
- Des intuitions prophétiques

## Conseils pour ce transit
- Explore une tradition spirituelle
- Médite sur l'unité de toutes choses
- Fais confiance à tes visions""",

    ('pisces', 10): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Ta communication professionnelle devient inspirée — aligne travail et âme.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 10, rendant ta communication professionnelle plus inspirée et orientée vers le service. Tu veux un travail qui a du sens.

## Ce que tu pourrais vivre
- Des opportunités dans les domaines créatifs ou de l'aide
- Une communication professionnelle intuitive
- L'envie d'aligner ta carrière avec ton âme

## Conseils pour ce transit
- Communique avec inspiration au travail
- Écoute ton intuition pour les décisions de carrière
- Trouve le sens spirituel de ton travail""",

    ('pisces', 11): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Tes échanges avec tes amis deviennent profonds — connecte-toi avec compassion.

## L'énergie du moment
Mercure en Poissons traverse ta Maison 11, rendant tes communications amicales plus intuitives et empathiques. Tu ressens les besoins de ton groupe.

## Ce que tu pourrais vivre
- Des échanges profonds avec tes amis
- Une communication basée sur la compassion
- Des projets collectifs à dimension spirituelle

## Conseils pour ce transit
- Soutiens tes amis avec compassion
- Engage-toi dans des causes humanitaires
- Partage tes visions spirituelles""",

    ('pisces', 12): """# ☿ Transit de Mercure en Poissons

**En une phrase :** Ton mental fusionne avec l'inconscient — écoute la voix de l'âme.

## L'énergie du moment
Mercure en Poissons amplifie ta Maison 12, dissolvant les frontières entre conscient et inconscient. Tu reçois des messages de l'au-delà.

## Ce que tu pourrais vivre
- Une connexion directe avec ton inconscient
- Des rêves prophétiques et révélateurs
- Des intuitions très fortes

## Conseils pour ce transit
- Journalise tes rêves et intuitions
- Médite et écoute ta voix intérieure
- Laisse ton mental se reposer dans le silence""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_MERCURY_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_mercury',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP transit_mercury/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='transit_mercury',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT transit_mercury/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
