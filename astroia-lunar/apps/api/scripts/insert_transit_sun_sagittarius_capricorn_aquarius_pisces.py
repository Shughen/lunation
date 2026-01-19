#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Soleil en Sagittaire/Capricorne/Verseau/Poissons."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SUN_INTERPRETATIONS = {
    # SAGITTARIUS
    ('sagittarius', 1): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Tu rayonnes d'optimisme — montre ton enthousiasme et ton goût pour l'aventure.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Sagittaire, te rendant plus optimiste, aventurier et philosophe. C'est le moment de t'affirmer avec enthousiasme et de viser haut.

## Ce que tu pourrais vivre
- Un regain d'optimisme et de confiance
- L'envie d'explorer de nouveaux horizons
- Une présence plus expansive et joyeuse

## Conseils pour ce transit
- Vise grand et partage ton enthousiasme
- Lance-toi dans une nouvelle aventure
- Montre ta générosité et ton ouverture d'esprit""",

    ('sagittarius', 2): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Tes ressources s'élargissent — vois grand pour ta prospérité.

## L'énergie du moment
Le Soleil en Sagittaire illumine ta Maison 2 des ressources. Tu vois tes finances avec optimisme et tu es prêt à investir dans ton expansion. C'est le moment de viser la prospérité.

## Ce que tu pourrais vivre
- Des opportunités financières liées à l'étranger ou l'enseignement
- L'envie d'investir dans tes connaissances
- Une vision optimiste de tes ressources

## Conseils pour ce transit
- Investis dans ton développement personnel
- Explore de nouvelles sources de revenus
- Évite la dépense excessive par optimisme""",

    ('sagittarius', 3): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Ta communication s'élargit — partage tes visions et inspire les autres.

## L'énergie du moment
Le Soleil en Sagittaire traverse ta Maison 3 de la communication. Tu communiques avec enthousiasme et envergure, partageant des idées inspirantes. C'est le moment de transmettre ta vision.

## Ce que tu pourrais vivre
- Des conversations stimulantes sur des grands sujets
- L'envie de partager tes connaissances
- Des déplacements ou voyages courts

## Conseils pour ce transit
- Enseigne ou partage ce que tu sais
- Explore de nouveaux sujets d'apprentissage
- Inspire les autres par tes paroles""",

    ('sagittarius', 4): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Ton foyer s'ouvre au monde — apporte l'aventure dans ta vie privée.

## L'énergie du moment
Le Soleil en Sagittaire illumine ta Maison 4 du foyer. Tu as envie d'espace, de liberté dans ton chez-toi, peut-être d'accueillir des personnes d'horizons différents.

## Ce que tu pourrais vivre
- Un besoin d'espace et de liberté à la maison
- L'envie de déménager ou de voyager en famille
- Des discussions philosophiques en famille

## Conseils pour ce transit
- Apporte une touche d'ailleurs dans ta déco
- Organise des activités expansives en famille
- Accueille la diversité chez toi""",

    ('sagittarius', 5): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** La joie et l'aventure t'appellent — vis des expériences qui élargissent ton horizon.

## L'énergie du moment
Le Soleil en Sagittaire traverse ta Maison 5 de la créativité et de l'amour. Tu vis l'amour et les plaisirs avec enthousiasme et goût de l'aventure. C'est le moment de t'amuser grandement.

## Ce que tu pourrais vivre
- Des amours avec des personnes d'horizons différents
- Une créativité inspirée par les voyages ou la philosophie
- Des plaisirs expansifs et aventureux

## Conseils pour ce transit
- Vis des aventures amoureuses ou créatives
- Explore de nouvelles formes d'expression
- Offre-toi des expériences mémorables""",

    ('sagittarius', 6): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Ton quotidien cherche du sens — trouve la philosophie dans ton travail.

## L'énergie du moment
Le Soleil en Sagittaire illumine ta Maison 6 du travail et de la santé. Tu cherches un sens plus élevé dans tes routines, une philosophie dans ton quotidien.

## Ce que tu pourrais vivre
- Un besoin de sens dans ton travail
- L'envie d'améliorer ta santé par des méthodes holistiques
- Des opportunités de travail liées à l'étranger

## Conseils pour ce transit
- Trouve la philosophie dans tes tâches quotidiennes
- Explore des pratiques de santé alternatives
- Élargis ton cadre de travail""",

    ('sagittarius', 7): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Tes relations s'élargissent — cherche des partenaires qui partagent ta vision.

## L'énergie du moment
Le Soleil en Sagittaire traverse ta Maison 7 des partenariats. Tu es attiré par des partenaires qui partagent ta soif d'aventure et de connaissance. C'est le moment de t'associer avec des visionnaires.

## Ce que tu pourrais vivre
- Des relations avec des personnes d'horizons différents
- Un besoin de liberté dans tes partenariats
- Des projets communs orientés vers l'expansion

## Conseils pour ce transit
- Cherche des partenaires qui élargissent ton monde
- Voyage ou explore avec ton partenaire
- Maintiens ta liberté dans tes engagements""",

    ('sagittarius', 8): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Les transformations t'élèvent — trouve la sagesse dans les épreuves.

## L'énergie du moment
Le Soleil en Sagittaire illumine ta Maison 8 des transformations. Tu abordes les changements profonds avec optimisme et foi. C'est le moment de trouver le sens dans les crises.

## Ce que tu pourrais vivre
- Une approche philosophique des transformations
- Des opportunités financières liées à l'étranger
- Une quête de sens face aux changements

## Conseils pour ce transit
- Trouve la leçon dans chaque épreuve
- Explore les philosophies de la transformation
- Aie confiance dans le processus de renouveau""",

    ('sagittarius', 9): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Ta quête de sens atteint son apogée — explore, apprends et partage ta sagesse.

## L'énergie du moment
Le Soleil en Sagittaire amplifie ta Maison 9, son domicile naturel. C'est le moment idéal pour voyager, étudier et élargir ta vision du monde. Ta soif de connaissance est à son maximum.

## Ce que tu pourrais vivre
- Des voyages inspirants et transformateurs
- Des opportunités d'études ou d'enseignement
- Une clarification de tes convictions

## Conseils pour ce transit
- Voyage vers des destinations qui t'inspirent
- Inscris-toi à une formation qui t'élève
- Partage ta sagesse avec générosité""",

    ('sagittarius', 10): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Ta carrière vise haut — montre ta vision et ton expertise.

## L'énergie du moment
Le Soleil en Sagittaire traverse ta Maison 10 de la carrière. Tu es reconnu pour ta vision large et ton expertise. C'est le moment de viser des positions d'envergure.

## Ce que tu pourrais vivre
- Des opportunités liées à l'international ou l'enseignement
- Une reconnaissance pour tes connaissances
- L'envie de viser plus haut professionnellement

## Conseils pour ce transit
- Affiche tes ambitions avec confiance
- Développe ton expertise reconnue
- Vise des positions à portée internationale""",

    ('sagittarius', 11): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Tes projets collectifs visent haut — inspire ton réseau avec ta vision.

## L'énergie du moment
Le Soleil en Sagittaire illumine ta Maison 11 des amitiés et des projets de groupe. Tu attires des amis du monde entier et participes à des projets visionnaires.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes d'horizons différents
- Des projets collectifs à portée internationale
- Une vision inspirante pour l'avenir

## Conseils pour ce transit
- Rejoins des groupes qui partagent ta vision
- Cultive des amitiés internationales
- Inspire les autres par tes idéaux""",

    ('sagittarius', 12): """# ☉ Transit du Soleil en Sagittaire

**En une phrase :** Ta spiritualité s'approfondit — explore les mystères avec foi.

## L'énergie du moment
Le Soleil en Sagittaire traverse ta Maison 12 de l'intériorité. Tu explores ta spiritualité avec optimisme et ouverture. C'est le moment de méditer sur le sens de la vie.

## Ce que tu pourrais vivre
- Une connexion profonde avec ta spiritualité
- Des retraites ou des voyages intérieurs
- Des rêves prophétiques ou inspirants

## Conseils pour ce transit
- Médite sur les grandes questions de l'existence
- Fais une retraite spirituelle
- Prépare-toi à une nouvelle expansion""",

    # CAPRICORN
    ('capricorn', 1): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Tu rayonnes d'autorité — montre ta maturité et ton ambition.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Capricorne, te donnant une présence sérieuse, ambitieuse et responsable. C'est le moment de t'affirmer professionnellement et de montrer ta fiabilité.

## Ce que tu pourrais vivre
- Une prise de responsabilité accrue
- Un désir de reconnaissance pour ta maturité
- Une présence plus autoritaire et structurée

## Conseils pour ce transit
- Assume tes responsabilités avec fierté
- Projette une image professionnelle
- Travaille sur tes objectifs à long terme""",

    ('capricorn', 2): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Tes finances demandent de la structure — construis ta sécurité avec discipline.

## L'énergie du moment
Le Soleil en Capricorne illumine ta Maison 2 des ressources. Tu abordes tes finances avec sérieux et ambition. C'est le moment de planifier et de construire ta sécurité matérielle.

## Ce que tu pourrais vivre
- Un besoin de structurer tes finances
- Des objectifs financiers à long terme
- Une discipline accrue dans tes dépenses

## Conseils pour ce transit
- Planifie tes finances sur le long terme
- Investis dans des valeurs sûres
- Développe des compétences qui augmentent ta valeur""",

    ('capricorn', 3): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Ta communication gagne en autorité — exprime-toi avec sérieux et structure.

## L'énergie du moment
Le Soleil en Capricorne traverse ta Maison 3 de la communication. Tu communiques de façon plus structurée, plus professionnelle. C'est le moment de formaliser tes idées.

## Ce que tu pourrais vivre
- Une communication plus formelle et efficace
- Des études ou formations professionnelles
- Des échanges avec des personnes d'autorité

## Conseils pour ce transit
- Structure tes idées avant de les présenter
- Inscris-toi à une formation qualifiante
- Communique avec professionnalisme""",

    ('capricorn', 4): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Ton foyer devient ton projet — construis des fondations solides.

## L'énergie du moment
Le Soleil en Capricorne illumine ta Maison 4 du foyer. Tu veux un chez-toi stable, structuré, qui te sert de base pour tes ambitions. C'est le moment d'investir dans ton patrimoine.

## Ce que tu pourrais vivre
- Des projets immobiliers ou de rénovation
- Un rôle d'autorité dans ta famille
- Un besoin de structure domestique

## Conseils pour ce transit
- Investis dans ton patrimoine immobilier
- Établis des règles claires à la maison
- Renforce les fondations de ta vie privée""",

    ('capricorn', 5): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Ta créativité se structure — construis des œuvres qui durent.

## L'énergie du moment
Le Soleil en Capricorne traverse ta Maison 5 de la créativité et de l'amour. Tu abordes les plaisirs et l'amour avec sérieux. C'est le moment de créer quelque chose de durable.

## Ce que tu pourrais vivre
- Une créativité orientée vers des projets durables
- Des relations amoureuses sérieuses
- Des loisirs qui construisent quelque chose

## Conseils pour ce transit
- Crée quelque chose qui traversera le temps
- En amour, cherche la stabilité
- Transforme un hobby en projet structuré""",

    ('capricorn', 6): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Ton quotidien devient efficace — structure tes routines pour réussir.

## L'énergie du moment
Le Soleil en Capricorne illumine ta Maison 6 du travail et de la santé. Tu es au maximum de ton efficacité professionnelle, avec une discipline exemplaire.

## Ce que tu pourrais vivre
- Une productivité et une efficacité accrues
- Des responsabilités professionnelles supplémentaires
- Un régime de santé discipliné

## Conseils pour ce transit
- Établis des routines de travail efficaces
- Prends ta santé au sérieux
- Montre ta fiabilité à tes supérieurs""",

    ('capricorn', 7): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Tes relations se formalisent — cherche des partenariats durables et engagés.

## L'énergie du moment
Le Soleil en Capricorne traverse ta Maison 7 des partenariats. Tu recherches des engagements sérieux et des partenaires fiables. C'est le moment de formaliser tes relations.

## Ce que tu pourrais vivre
- Des engagements officiels (mariage, contrat)
- L'attirance pour des partenaires matures et ambitieux
- Un travail sur la structure de tes relations

## Conseils pour ce transit
- Formalise tes engagements importants
- Choisis des partenaires fiables et ambitieux
- Travaille sur le long terme dans tes relations""",

    ('capricorn', 8): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Les transformations se font avec méthode — gère les crises avec maturité.

## L'énergie du moment
Le Soleil en Capricorne illumine ta Maison 8 des transformations. Tu abordes les changements profonds avec sérieux et stratégie. C'est le moment de gérer les ressources partagées avec prudence.

## Ce que tu pourrais vivre
- Une gestion rigoureuse des finances partagées
- Des transformations planifiées et contrôlées
- Des héritages ou successions à gérer

## Conseils pour ce transit
- Planifie tes successions et héritages
- Aborde les transformations avec stratégie
- Gère les ressources partagées avec rigueur""",

    ('capricorn', 9): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Ta quête de sens se structure — construis une philosophie solide.

## L'énergie du moment
Le Soleil en Capricorne traverse ta Maison 9 des voyages et de la philosophie. Tu cherches une sagesse pratique, des études qui mènent à des résultats concrets.

## Ce que tu pourrais vivre
- Des études ou formations qualifiantes
- Des voyages d'affaires ou professionnels
- Une philosophie pragmatique et réaliste

## Conseils pour ce transit
- Obtiens des diplômes ou certifications
- Voyage pour des raisons professionnelles
- Développe une vision réaliste du monde""",

    ('capricorn', 10): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Ta carrière atteint son sommet — assume ton ambition et ton leadership.

## L'énergie du moment
Le Soleil en Capricorne amplifie ta Maison 10, son domicile naturel. C'est le moment de briller professionnellement, de prendre des responsabilités et d'atteindre tes objectifs.

## Ce que tu pourrais vivre
- Des promotions ou reconnaissances importantes
- Des responsabilités de leadership
- L'atteinte d'objectifs de carrière

## Conseils pour ce transit
- Vise des positions de responsabilité
- Montre ton expertise et ta fiabilité
- Travaille sur ta réputation professionnelle""",

    ('capricorn', 11): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Tes projets collectifs se structurent — construis des alliances durables.

## L'énergie du moment
Le Soleil en Capricorne illumine ta Maison 11 des amitiés et des projets de groupe. Tu attires des alliés sérieux et contribues à des projets structurés.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes influentes
- Des projets collectifs bien organisés
- Des objectifs à long terme partagés

## Conseils pour ce transit
- Construis un réseau professionnel solide
- Engage-toi dans des projets structurés
- Définis des objectifs clairs pour l'avenir""",

    ('capricorn', 12): """# ☉ Transit du Soleil en Capricorne

**En une phrase :** Ta solitude devient productive — travaille sur toi en coulisses.

## L'énergie du moment
Le Soleil en Capricorne traverse ta Maison 12 de l'intériorité. C'est le moment de travailler sur toi-même avec discipline, de préparer en secret tes prochaines ambitions.

## Ce que tu pourrais vivre
- Un travail intérieur structuré et discipliné
- Des projets préparés en coulisses
- Une réflexion sur tes véritables ambitions

## Conseils pour ce transit
- Travaille sur tes blocages avec méthode
- Prépare discrètement tes prochains objectifs
- Médite sur le sens de ton ambition""",

    # AQUARIUS
    ('aquarius', 1): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Tu rayonnes d'originalité — montre ton unicité et ta vision du futur.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Verseau, te rendant plus original, indépendant et tourné vers l'avenir. C'est le moment de t'affirmer dans ta différence.

## Ce que tu pourrais vivre
- Un besoin d'afficher ton originalité
- L'envie de te démarquer de la masse
- Une présence plus détachée et intellectuelle

## Conseils pour ce transit
- Assume ta différence avec fierté
- Innove dans ta façon de te présenter
- Montre ta vision unique du monde""",

    ('aquarius', 2): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Tes ressources s'innovent — explore des façons originales de gagner.

## L'énergie du moment
Le Soleil en Verseau illumine ta Maison 2 des ressources. Tu es prêt à explorer des revenus alternatifs, des technologies ou des approches innovantes.

## Ce que tu pourrais vivre
- Des opportunités dans les nouvelles technologies
- Un détachement vis-à-vis de l'argent
- Des revenus liés à des idées originales

## Conseils pour ce transit
- Explore les cryptomonnaies ou revenus alternatifs
- Monétise tes idées innovantes
- Détache-toi des approches traditionnelles""",

    ('aquarius', 3): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Ta communication devient avant-gardiste — partage des idées innovantes.

## L'énergie du moment
Le Soleil en Verseau traverse ta Maison 3 de la communication. Tu communiques de façon originale, partageant des idées qui sortent des sentiers battus.

## Ce que tu pourrais vivre
- Des échanges stimulants sur des sujets innovants
- L'envie d'apprendre des technologies nouvelles
- Une communication via les réseaux sociaux

## Conseils pour ce transit
- Partage tes idées sur les plateformes digitales
- Apprends quelque chose de technologique
- Connecte-toi avec des esprits originaux""",

    ('aquarius', 4): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Ton foyer s'émancipe — crée un espace de vie non-conventionnel.

## L'énergie du moment
Le Soleil en Verseau illumine ta Maison 4 du foyer. Tu as envie d'un chez-toi original, peut-être partagé ou en coliving, avec beaucoup de liberté.

## Ce que tu pourrais vivre
- Des changements inhabituels dans ta vie domestique
- L'envie d'une habitation non-conventionnelle
- Un détachement émotionnel de la famille traditionnelle

## Conseils pour ce transit
- Innove dans ton mode de vie domestique
- Apporte de la technologie dans ton foyer
- Redéfinis ce que signifie "famille" pour toi""",

    ('aquarius', 5): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Ta créativité devient expérimentale — explore des expressions originales.

## L'énergie du moment
Le Soleil en Verseau traverse ta Maison 5 de la créativité et de l'amour. Tu es attiré par des expériences créatives et amoureuses hors du commun.

## Ce que tu pourrais vivre
- Une créativité technologique ou numérique
- Des amours non-conventionnelles
- Des plaisirs alternatifs et originaux

## Conseils pour ce transit
- Expérimente de nouvelles formes de création
- En amour, reste ouvert aux relations atypiques
- Amuse-toi de façons inhabituelles""",

    ('aquarius', 6): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Ton quotidien s'émancipe — révolutionne tes routines.

## L'énergie du moment
Le Soleil en Verseau illumine ta Maison 6 du travail et de la santé. Tu veux un travail qui te laisse libre et des routines peu conventionnelles.

## Ce que tu pourrais vivre
- Un désir de travail flexible ou à distance
- Des méthodes de santé alternatives
- L'envie de changer radicalement tes routines

## Conseils pour ce transit
- Négocie plus de flexibilité au travail
- Explore des approches de santé innovantes
- Libère-toi des routines qui t'enferment""",

    ('aquarius', 7): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Tes relations s'émancipent — cherche des partenariats basés sur la liberté.

## L'énergie du moment
Le Soleil en Verseau traverse ta Maison 7 des partenariats. Tu recherches des relations qui respectent ton indépendance et partagent tes idéaux.

## Ce que tu pourrais vivre
- Des relations non-conventionnelles ou à distance
- L'attirance pour des partenaires originaux
- Un besoin de liberté dans l'engagement

## Conseils pour ce transit
- Choisis des partenaires qui respectent ton indépendance
- Redéfinis les règles de tes relations
- Connecte-toi sur des idéaux communs""",

    ('aquarius', 8): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Les transformations se font par rupture — détache-toi du passé.

## L'énergie du moment
Le Soleil en Verseau illumine ta Maison 8 des transformations. Tu es prêt à des changements radicaux, à te libérer de ce qui t'enchaîne.

## Ce que tu pourrais vivre
- Des ruptures libératrices
- Une approche détachée des crises
- Des innovations financières (crypto, financement participatif)

## Conseils pour ce transit
- Libère-toi des attaches qui ne servent plus
- Explore des approches innovantes de la transformation
- Détache-toi émotionnellement du passé""",

    ('aquarius', 9): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Ta quête de sens devient universelle — explore des philosophies progressistes.

## L'énergie du moment
Le Soleil en Verseau traverse ta Maison 9 des voyages et de la philosophie. Tu es attiré par des idées avant-gardistes, des utopies et des visions du futur.

## Ce que tu pourrais vivre
- Un intérêt pour les philosophies futuristes
- Des voyages vers des lieux innovants
- Des études dans des domaines émergents

## Conseils pour ce transit
- Explore des courants de pensée progressistes
- Voyage vers des lieux d'innovation
- Connecte-toi avec des communautés internationales""",

    ('aquarius', 10): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Ta carrière devient innovante — fais ta marque par ton originalité.

## L'énergie du moment
Le Soleil en Verseau illumine ta Maison 10 de la carrière. Tu es reconnu pour ton originalité et tes idées novatrices. C'est le moment de te démarquer.

## Ce que tu pourrais vivre
- Des opportunités dans des secteurs innovants
- Une reconnaissance pour tes idées originales
- Un positionnement professionnel unique

## Conseils pour ce transit
- Propose des idées innovantes au travail
- Positionne-toi dans des secteurs d'avenir
- Assume ton originalité professionnelle""",

    ('aquarius', 11): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Tes projets collectifs brillent — fédère autour de ta vision du futur.

## L'énergie du moment
Le Soleil en Verseau amplifie ta Maison 11, son domicile naturel. Tu es au cœur des réseaux, des projets collectifs et des causes humanitaires.

## Ce que tu pourrais vivre
- Une vie sociale intense et stimulante
- Des projets collectifs innovants
- Des amitiés basées sur des idéaux partagés

## Conseils pour ce transit
- Engage-toi dans des causes qui te tiennent à cœur
- Fédère ton réseau autour de projets innovants
- Cultive des amitiés intellectuellement stimulantes""",

    ('aquarius', 12): """# ☉ Transit du Soleil en Verseau

**En une phrase :** Ton inconscient s'éveille au futur — médite sur ta contribution à l'humanité.

## L'énergie du moment
Le Soleil en Verseau traverse ta Maison 12 de l'intériorité. Tu explores ta connexion avec le collectif, les causes universelles et ta contribution au monde.

## Ce que tu pourrais vivre
- Des intuitions sur l'avenir de l'humanité
- Un travail sur ton détachement émotionnel
- Des rêves de nature collective ou prophétique

## Conseils pour ce transit
- Médite sur ta contribution à l'humanité
- Travaille sur ton besoin de liberté intérieure
- Prépare-toi à servir des causes plus grandes que toi""",

    # PISCES
    ('pisces', 1): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Tu rayonnes de sensibilité — montre ta compassion et ta créativité.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Poissons, te rendant plus sensible, intuitif et créatif. C'est le moment de te connecter à ta spiritualité et d'exprimer ta sensibilité.

## Ce que tu pourrais vivre
- Une sensibilité accrue aux ambiances
- Un besoin de connexion spirituelle
- Une présence plus douce et empathique

## Conseils pour ce transit
- Laisse transparaître ta sensibilité
- Connecte-toi à ta dimension spirituelle
- Exprime ta créativité artistique""",

    ('pisces', 2): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Tes ressources suivent le flux — fais confiance à l'abondance universelle.

## L'énergie du moment
Le Soleil en Poissons illumine ta Maison 2 des ressources. Ton rapport à l'argent devient plus fluide, moins matérialiste. C'est le moment de faire confiance.

## Ce que tu pourrais vivre
- Des revenus liés à la créativité ou au spirituel
- Un détachement vis-à-vis du matériel
- Une intuition financière à suivre

## Conseils pour ce transit
- Fais confiance à l'abondance
- Valorise tes talents artistiques ou intuitifs
- Évite les décisions financières impulsives""",

    ('pisces', 3): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Ta communication devient poétique — exprime-toi avec âme et intuition.

## L'énergie du moment
Le Soleil en Poissons traverse ta Maison 3 de la communication. Tu communiques de façon plus intuitive, plus artistique, parfois plus floue aussi.

## Ce que tu pourrais vivre
- Une communication plus poétique ou artistique
- Des intuitions dans les conversations
- Des difficultés à être précis mais beaucoup de sensibilité

## Conseils pour ce transit
- Exprime-toi à travers l'art ou la poésie
- Fais confiance à tes intuitions dans les échanges
- Sois patient avec les malentendus""",

    ('pisces', 4): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Ton foyer devient un sanctuaire — crée un espace de paix et de spiritualité.

## L'énergie du moment
Le Soleil en Poissons illumine ta Maison 4 du foyer. Tu as besoin d'un chez-toi paisible, spirituel, peut-être proche de l'eau. C'est le moment de créer un refuge.

## Ce que tu pourrais vivre
- Un besoin de paix et de calme à la maison
- Des souvenirs ou émotions du passé qui remontent
- L'envie de créer un espace de méditation

## Conseils pour ce transit
- Crée un coin méditation chez toi
- Prends soin de l'atmosphère de ton foyer
- Accueille les émotions familiales avec compassion""",

    ('pisces', 5): """# ☉ Transit du Soleil en Poissons

**En une phrase :** L'amour devient transcendant — vis des expériences créatives et amoureuses profondes.

## L'énergie du moment
Le Soleil en Poissons traverse ta Maison 5 de la créativité et de l'amour. Tu vis l'amour de façon romantique et idéaliste. Ta créativité est inspirée par l'invisible.

## Ce que tu pourrais vivre
- Des amours romantiques et idéalisées
- Une créativité inspirée et spirituelle
- Des plaisirs liés à l'art, la musique, la nature

## Conseils pour ce transit
- Crée quelque chose qui vient de ton âme
- En amour, laisse-toi porter par le rêve
- Offre-toi des moments de beauté et d'évasion""",

    ('pisces', 6): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Ton quotidien cherche la fluidité — trouve un rythme qui respecte ta sensibilité.

## L'énergie du moment
Le Soleil en Poissons illumine ta Maison 6 du travail et de la santé. Tu as besoin d'un travail qui a du sens et de routines qui respectent ta nature sensible.

## Ce que tu pourrais vivre
- Un besoin de travail significatif ou créatif
- Une sensibilité accrue à ton environnement de travail
- Des pratiques de santé holistiques

## Conseils pour ce transit
- Trouve du sens dans tes tâches quotidiennes
- Pratique le yoga, la méditation ou des soins énergétiques
- Sois attentif aux signaux de ton corps""",

    ('pisces', 7): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Tes relations deviennent profondes — cherche des connexions d'âme.

## L'énergie du moment
Le Soleil en Poissons traverse ta Maison 7 des partenariats. Tu recherches des relations qui touchent l'âme, des connexions spirituelles ou artistiques.

## Ce que tu pourrais vivre
- Des relations empreintes de romance et d'idéalisme
- L'attirance pour des âmes sensibles ou artistiques
- Un besoin de fusion émotionnelle

## Conseils pour ce transit
- Cherche des partenaires qui nourrissent ton âme
- Évite d'idéaliser excessivement l'autre
- Partage des moments de beauté et de spiritualité""",

    ('pisces', 8): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Les transformations se font par lâcher-prise — laisse le flux te porter.

## L'énergie du moment
Le Soleil en Poissons illumine ta Maison 8 des transformations. Tu es invité à te dissoudre dans le changement, à faire confiance au processus de mort et renaissance.

## Ce que tu pourrais vivre
- Une dissolution des vieilles structures
- Des expériences mystiques ou transpersonnelles
- Un lâcher-prise profond sur le contrôle

## Conseils pour ce transit
- Lâche prise sur ce qui doit partir
- Fais confiance au processus de transformation
- Explore ta spiritualité en profondeur""",

    ('pisces', 9): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Ta quête de sens devient mystique — explore les dimensions spirituelles.

## L'énergie du moment
Le Soleil en Poissons traverse ta Maison 9 des voyages et de la philosophie. Tu es attiré par les traditions mystiques, les voyages vers des lieux sacrés et la sagesse universelle.

## Ce que tu pourrais vivre
- Un intérêt pour les traditions spirituelles
- Des voyages vers des lieux d'eau ou spirituels
- Des expériences qui élargissent ta conscience

## Conseils pour ce transit
- Explore une tradition spirituelle qui t'attire
- Voyage vers des lieux qui nourrissent ton âme
- Médite sur l'unité de toutes choses""",

    ('pisces', 10): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Ta carrière cherche du sens — aligne ton travail avec ta mission d'âme.

## L'énergie du moment
Le Soleil en Poissons illumine ta Maison 10 de la carrière. Tu as besoin d'un travail qui a du sens, qui aide les autres ou qui exprime ta créativité.

## Ce que tu pourrais vivre
- Un questionnement sur le sens de ta carrière
- Des opportunités dans les domaines de l'aide ou de l'art
- Un désir de contribuer au monde

## Conseils pour ce transit
- Aligne ta carrière avec tes valeurs profondes
- Explore les métiers de l'aide ou de la création
- Fais confiance à ton intuition professionnelle""",

    ('pisces', 11): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Tes projets collectifs deviennent humanitaires — engage-toi pour plus grand que toi.

## L'énergie du moment
Le Soleil en Poissons traverse ta Maison 11 des amitiés et des projets de groupe. Tu es attiré par des causes humanitaires et des communautés spirituelles.

## Ce que tu pourrais vivre
- Des amitiés basées sur la compassion partagée
- Des projets collectifs à dimension spirituelle
- Un sens de la fraternité universelle

## Conseils pour ce transit
- Engage-toi dans des causes humanitaires
- Rejoins des groupes qui partagent ta sensibilité
- Soutiens tes amis avec compassion""",

    ('pisces', 12): """# ☉ Transit du Soleil en Poissons

**En une phrase :** Tu retournes à la source — plonge dans l'océan de ton inconscient.

## L'énergie du moment
Le Soleil en Poissons amplifie ta Maison 12, son domicile naturel. C'est un temps de dissolution de l'ego, de connexion avec l'infini et de préparation spirituelle.

## Ce que tu pourrais vivre
- Une connexion profonde avec le divin
- Des rêves prophétiques et révélateurs
- Un besoin de solitude et de retrait

## Conseils pour ce transit
- Accorde-toi du temps de solitude méditative
- Écoute tes rêves et tes intuitions
- Prépare ta renaissance à venir""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_SUN_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_sun',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP transit_sun/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='transit_sun',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT transit_sun/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
