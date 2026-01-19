#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Lune en Sagittaire/Capricorne/Verseau/Poissons."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MOON_INTERPRETATIONS = {
    # SAGITTARIUS
    ('sagittarius', 1): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Tu as besoin d'espace et d'aventure — élargis tes horizons.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 1, éveillant ton optimisme et ton goût pour l'aventure. Tu as besoin de liberté et d'expansion.

## Ce que tu pourrais vivre
- Un regain d'optimisme et d'enthousiasme
- L'envie de bouger, de voyager, d'explorer
- Un besoin de sens et de vision

## Conseils pour ce transit
- Fais quelque chose qui t'ouvre l'esprit
- Suis ton enthousiasme
- Évite de t'engager dans trop de directions""",

    ('sagittarius', 2): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Tes ressources veulent grandir — vois grand pour ta prospérité.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 2, éveillant ton optimisme financier. Tu veux que tes ressources s'élargissent.

## Ce que tu pourrais vivre
- Un optimisme sur tes finances
- L'envie d'investir dans ton développement
- Des dépenses liées aux voyages ou à l'éducation

## Conseils pour ce transit
- Investis dans ce qui t'élargit l'esprit
- Évite les excès financiers par optimisme
- Réfléchis à ce qui a vraiment de la valeur""",

    ('sagittarius', 3): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Tes idées s'élargissent — partage ta vision avec enthousiasme.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 3, rendant ta communication plus enthousiaste et philosophique. Tu veux partager des idées qui inspirent.

## Ce que tu pourrais vivre
- Des conversations stimulantes et inspirantes
- L'envie d'apprendre quelque chose de nouveau
- Des échanges sur des sujets philosophiques

## Conseils pour ce transit
- Partage tes idées avec enthousiasme
- Apprends quelque chose qui t'ouvre l'esprit
- Évite de prêcher ou d'imposer tes vues""",

    ('sagittarius', 4): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Ton foyer a besoin d'espace — apporte l'aventure chez toi.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 4, éveillant ton besoin de liberté à la maison. Tu veux de l'espace et de l'aventure dans ta vie privée.

## Ce que tu pourrais vivre
- Un besoin d'espace chez toi
- L'envie de voyager en famille ou de recevoir des étrangers
- Des discussions philosophiques à la maison

## Conseils pour ce transit
- Apporte une touche d'ailleurs chez toi
- Crée de l'espace pour respirer
- Partage tes visions avec ta famille""",

    ('sagittarius', 5): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** La joie et l'aventure t'appellent — amuse-toi grandement.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 5, amplifiant ton goût pour les plaisirs et l'aventure. Tu veux des expériences qui élargissent tes horizons.

## Ce que tu pourrais vivre
- Des aventures amoureuses ou amicales
- Une créativité inspirée par les voyages ou la philosophie
- Des plaisirs expansifs et joyeux

## Conseils pour ce transit
- Vis des aventures qui t'inspirent
- Crée quelque chose qui reflète ta vision
- En amour, cherche quelqu'un qui partage tes rêves""",

    ('sagittarius', 6): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Ton quotidien cherche du sens — trouve la philosophie dans le travail.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 6, créant un besoin de sens dans ton travail quotidien. Tu veux que tes routines aient un but plus élevé.

## Ce que tu pourrais vivre
- Un besoin de sens dans ton travail
- L'envie d'améliorer ta santé par des méthodes alternatives
- De l'impatience avec les tâches routinières

## Conseils pour ce transit
- Trouve le sens dans tes tâches quotidiennes
- Explore des approches de santé holistiques
- Évite de négliger les détails par excès d'enthousiasme""",

    ('sagittarius', 7): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Tes relations veulent de l'espace — cherche des partenaires qui t'élèvent.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 7, créant un besoin de liberté et de croissance dans tes relations. Tu veux des partenaires qui partagent ta vision.

## Ce que tu pourrais vivre
- Un besoin de liberté dans tes relations
- L'attirance pour des personnes d'horizons différents
- Des projets d'aventure à deux

## Conseils pour ce transit
- Partage tes visions avec ton partenaire
- Planifie une aventure ensemble
- Respecte le besoin de liberté de chacun""",

    ('sagittarius', 8): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Les transformations t'élèvent — trouve la sagesse dans les épreuves.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 8, apportant de l'optimisme face aux transformations. Tu cherches le sens des crises.

## Ce que tu pourrais vivre
- Une approche philosophique des épreuves
- Un optimisme face aux changements
- Des réflexions sur le sens de la vie et de la mort

## Conseils pour ce transit
- Cherche la leçon dans chaque épreuve
- Aie confiance dans le processus de transformation
- Évite de fuir les émotions difficiles""",

    ('sagittarius', 9): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Ta soif d'apprendre est à son maximum — explore et partage.

## L'énergie du moment
La Lune en Sagittaire amplifie ta Maison 9, créant un besoin intense de sens, de voyage et d'apprentissage. Tu veux élargir tes horizons au maximum.

## Ce que tu pourrais vivre
- Une soif intense de connaissance
- L'envie de voyager ou de planifier un voyage
- Des discussions philosophiques passionnantes

## Conseils pour ce transit
- Explore un sujet qui te passionne
- Planifie une aventure
- Partage ta sagesse avec générosité""",

    ('sagittarius', 10): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Ta carrière vise haut — montre ta vision et ton expertise.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 10, éveillant tes ambitions et ton désir de reconnaissance pour ta vision. Tu veux une carrière qui a du sens.

## Ce que tu pourrais vivre
- Un besoin de sens dans ta carrière
- L'envie de viser plus haut professionnellement
- Des opportunités liées à l'international ou l'enseignement

## Conseils pour ce transit
- Affiche tes ambitions avec confiance
- Partage ton expertise
- Vise des objectifs qui ont du sens pour toi""",

    ('sagittarius', 11): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Tes amis t'inspirent — partage des visions d'avenir.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 11, stimulant ta vie sociale et tes projets collectifs. Tu veux des amis qui partagent tes idéaux.

## Ce que tu pourrais vivre
- Des moments joyeux avec des amis inspirants
- Des projets collectifs ambitieux
- Des discussions sur l'avenir et les idéaux

## Conseils pour ce transit
- Rejoins des groupes qui partagent tes valeurs
- Partage ta vision de l'avenir
- Inspire tes amis par ton optimisme""",

    ('sagittarius', 12): """# ☽ Transit de la Lune en Sagittaire

**En une phrase :** Ta spiritualité s'élargit — explore les mystères avec foi.

## L'énergie du moment
La Lune en Sagittaire traverse ta Maison 12, orientant ton monde intérieur vers la quête de sens. Tu cherches une connexion spirituelle expansive.

## Ce que tu pourrais vivre
- Des intuitions sur le sens de la vie
- Des rêves inspirants et prophétiques
- Un besoin de retrait pour méditer

## Conseils pour ce transit
- Médite sur les grandes questions
- Fais confiance à tes intuitions
- Prépare une nouvelle expansion de conscience""",

    # CAPRICORN
    ('capricorn', 1): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Tu as besoin de structure — prends tes responsabilités avec sérieux.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 1, éveillant ton sens des responsabilités et ton ambition. Tu veux être pris au sérieux.

## Ce que tu pourrais vivre
- Un besoin de contrôle et de structure
- Une attitude plus sérieuse et responsable
- Un regard critique sur toi-même

## Conseils pour ce transit
- Prends tes responsabilités
- Projette une image professionnelle
- Évite d'être trop dur envers toi-même""",

    ('capricorn', 2): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Tes finances demandent de la rigueur — planifie à long terme.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 2, créant un besoin de sécurité financière et de planification. Tu veux construire une base solide.

## Ce que tu pourrais vivre
- Un besoin de sécurité financière
- L'envie de planifier tes finances
- Une approche prudente des dépenses

## Conseils pour ce transit
- Planifie tes finances à long terme
- Évite les dépenses impulsives
- Investis dans des valeurs sûres""",

    ('capricorn', 3): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Ta communication se fait sérieuse — exprime-toi avec autorité.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 3, rendant ta communication plus structurée et professionnelle. Tu veux être pris au sérieux.

## Ce que tu pourrais vivre
- Une communication plus formelle
- Des échanges sur des sujets sérieux
- Un besoin de prouver ta compétence

## Conseils pour ce transit
- Structure tes idées avant de les présenter
- Communique avec professionnalisme
- Évite d'être trop rigide""",

    ('capricorn', 4): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Ton foyer a besoin de structure — construis des fondations solides.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 4, créant un besoin de stabilité et de structure à la maison. Tu veux un foyer qui te sécurise.

## Ce que tu pourrais vivre
- Un besoin de stabilité domestique
- L'envie de travailler sur ton patrimoine
- Des responsabilités familiales

## Conseils pour ce transit
- Renforce les fondations de ton foyer
- Prends tes responsabilités familiales
- Crée une structure rassurante chez toi""",

    ('capricorn', 5): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Tes plaisirs se structurent — crée quelque chose de durable.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 5, apportant du sérieux dans les domaines du plaisir et de la créativité. Tu veux que tes créations durent.

## Ce que tu pourrais vivre
- Une créativité orientée vers des résultats durables
- Des amours sérieuses
- Des plaisirs modérés mais satisfaisants

## Conseils pour ce transit
- Crée quelque chose qui traversera le temps
- En amour, cherche la stabilité
- Permets-toi des plaisirs sans culpabilité""",

    ('capricorn', 6): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Ton quotidien devient productif — structure tes routines.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 6, maximisant ta productivité et ta discipline. Tu veux accomplir et être efficace.

## Ce que tu pourrais vivre
- Une productivité élevée
- Un besoin de routines structurées
- Une attention à ta santé par la discipline

## Conseils pour ce transit
- Accomplis les tâches importantes
- Établis des routines efficaces
- Prends soin de ta santé avec discipline""",

    ('capricorn', 7): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Tes relations demandent du sérieux — engage-toi avec responsabilité.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 7, créant un besoin d'engagement et de sérieux dans tes relations. Tu veux des partenariats solides.

## Ce que tu pourrais vivre
- Un besoin de clarifier les engagements
- Des discussions sur l'avenir de la relation
- L'attirance pour des partenaires fiables

## Conseils pour ce transit
- Discute des engagements avec ton partenaire
- Sois fiable et responsable
- Évite d'être trop froid ou distant""",

    ('capricorn', 8): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Les transformations se font avec méthode — gère les crises avec maturité.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 8, apportant structure et contrôle dans les domaines de transformation. Tu veux gérer les crises avec sagesse.

## Ce que tu pourrais vivre
- Une approche contrôlée des émotions profondes
- Des questions financières partagées à gérer
- Un travail méthodique sur les blocages

## Conseils pour ce transit
- Gère les crises avec maturité
- Planifie les questions financières partagées
- Évite de réprimer tes émotions""",

    ('capricorn', 9): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Ta quête de sens se structure — construis une vision réaliste.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 9, orientant ta recherche de sens vers le pragmatique. Tu veux une philosophie qui fonctionne.

## Ce que tu pourrais vivre
- Un intérêt pour des formations certifiantes
- Des voyages d'affaires ou professionnels
- Une vision réaliste de l'avenir

## Conseils pour ce transit
- Obtiens des qualifications concrètes
- Voyage pour des raisons pratiques
- Développe une philosophie applicable""",

    ('capricorn', 10): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Ta carrière est au premier plan — assume ton ambition.

## L'énergie du moment
La Lune en Capricorne amplifie ta Maison 10, maximisant ton ambition et ton besoin de reconnaissance professionnelle. Tu veux réussir.

## Ce que tu pourrais vivre
- Un focus intense sur ta carrière
- Des responsabilités professionnelles accrues
- Un besoin de reconnaissance pour tes accomplissements

## Conseils pour ce transit
- Assume ton ambition
- Montre ta fiabilité professionnelle
- Évite de sacrifier tout pour le travail""",

    ('capricorn', 11): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Tes projets collectifs se structurent — contribue avec responsabilité.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 11, créant un besoin de structure dans tes amitiés et projets de groupe. Tu veux des résultats concrets.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes influentes
- Des projets de groupe bien organisés
- Une définition claire de tes objectifs à long terme

## Conseils pour ce transit
- Contribue de façon responsable aux projets de groupe
- Définis des objectifs réalistes
- Cultive des amitiés durables""",

    ('capricorn', 12): """# ☽ Transit de la Lune en Capricorne

**En une phrase :** Ton monde intérieur demande de la structure — travaille sur tes blocages avec méthode.

## L'énergie du moment
La Lune en Capricorne traverse ta Maison 12, créant un besoin de structurer ton monde intérieur. Tu veux comprendre et maîtriser tes profondeurs.

## Ce que tu pourrais vivre
- Un travail méthodique sur l'inconscient
- Des peurs liées à l'échec ou au contrôle
- Un besoin de solitude productive

## Conseils pour ce transit
- Travaille sur tes blocages avec méthode
- Médite sur tes peurs du contrôle
- Prépare discrètement tes prochains objectifs""",

    # AQUARIUS
    ('aquarius', 1): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Tu as besoin de liberté — affirme ton originalité.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 1, éveillant ton besoin d'indépendance et d'originalité. Tu veux être unique et libre.

## Ce que tu pourrais vivre
- Un besoin de te démarquer
- L'envie de casser la routine
- Un détachement émotionnel

## Conseils pour ce transit
- Assume ton originalité
- Expérimente quelque chose de nouveau
- Évite de te couper de tes émotions""",

    ('aquarius', 2): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Tes ressources s'innovent — explore des revenus alternatifs.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 2, créant un besoin de liberté financière et d'innovation. Tu veux des approches différentes.

## Ce que tu pourrais vivre
- Un intérêt pour des revenus alternatifs
- Un détachement vis-à-vis du matériel
- Des idées originales pour gagner de l'argent

## Conseils pour ce transit
- Explore des sources de revenus innovantes
- Ne néglige pas tes besoins matériels de base
- Expérimente de nouvelles approches""",

    ('aquarius', 3): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Ta communication devient originale — partage des idées innovantes.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 3, stimulant tes idées originales et ta communication alternative. Tu veux des échanges stimulants.

## Ce que tu pourrais vivre
- Des idées originales et avant-gardistes
- Des échanges stimulants sur les réseaux
- Une communication qui sort de l'ordinaire

## Conseils pour ce transit
- Partage tes idées innovantes
- Connecte-toi avec des esprits originaux
- Utilise les technologies pour communiquer""",

    ('aquarius', 4): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Ton foyer s'émancipe — crée un espace non-conventionnel.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 4, créant un besoin de liberté et d'originalité chez toi. Tu veux un foyer qui reflète ta différence.

## Ce que tu pourrais vivre
- Un besoin de changement à la maison
- L'envie d'un mode de vie alternatif
- Un détachement émotionnel de la famille traditionnelle

## Conseils pour ce transit
- Apporte de l'innovation chez toi
- Accepte les différences familiales
- Crée ton propre concept de foyer""",

    ('aquarius', 5): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Tes plaisirs deviennent originaux — amuse-toi différemment.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 5, rendant tes expériences de plaisir plus originales et libres. Tu veux des relations et des loisirs hors du commun.

## Ce que tu pourrais vivre
- Des amours non-conventionnelles
- Une créativité technologique ou avant-gardiste
- Des plaisirs alternatifs et originaux

## Conseils pour ce transit
- Expérimente de nouvelles formes de plaisir
- En amour, reste ouvert aux relations atypiques
- Exprime ta créativité de façon originale""",

    ('aquarius', 6): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Ton quotidien s'émancipe — révolutionne tes routines.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 6, créant un besoin de liberté dans ton travail et tes routines. Tu veux sortir du moule.

## Ce que tu pourrais vivre
- Un désir de flexibilité au travail
- L'envie de changer radicalement tes routines
- Un intérêt pour des méthodes de santé alternatives

## Conseils pour ce transit
- Innove dans tes méthodes de travail
- Explore des approches de santé alternatives
- Évite de rejeter toutes les structures""",

    ('aquarius', 7): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Tes relations cherchent la liberté — connecte-toi sur des idéaux.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 7, créant un besoin d'espace et d'originalité dans tes relations. Tu veux des partenaires qui respectent ta liberté.

## Ce que tu pourrais vivre
- Un besoin d'indépendance dans les relations
- L'attirance pour des personnes originales
- Des relations basées sur des idéaux partagés

## Conseils pour ce transit
- Respecte le besoin de liberté de chacun
- Connecte-toi sur des idéaux communs
- Évite le détachement émotionnel excessif""",

    ('aquarius', 8): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Les transformations se font par rupture — libère-toi du passé.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 8, apportant un désir de changement radical et de libération. Tu veux te détacher de ce qui t'enchaîne.

## Ce que tu pourrais vivre
- Des ruptures libératrices
- Un détachement émotionnel face aux crises
- Des approches innovantes de la transformation

## Conseils pour ce transit
- Libère-toi de ce qui ne sert plus
- Détache-toi émotionnellement du passé
- Accepte les changements soudains""",

    ('aquarius', 9): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Ta quête de sens devient universelle — explore des idées progressistes.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 9, orientant ta recherche de sens vers l'avant-garde et l'universel. Tu veux une vision du futur.

## Ce que tu pourrais vivre
- Un intérêt pour des idées futuristes
- L'envie de voyager vers des lieux innovants
- Des réflexions sur l'avenir de l'humanité

## Conseils pour ce transit
- Explore des courants de pensée progressistes
- Connecte-toi avec des communautés internationales
- Réfléchis à ta contribution à l'humanité""",

    ('aquarius', 10): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Ta carrière devient innovante — démarque-toi par ton originalité.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 10, créant un besoin d'originalité et de liberté dans ta carrière. Tu veux faire les choses différemment.

## Ce que tu pourrais vivre
- Des opportunités dans des secteurs innovants
- Un désir de te démarquer professionnellement
- Un besoin d'autonomie au travail

## Conseils pour ce transit
- Propose des idées innovantes
- Positionne-toi dans des secteurs d'avenir
- Évite de suivre le troupeau""",

    ('aquarius', 11): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Tes amitiés et tes projets brillent — fédère autour de ta vision.

## L'énergie du moment
La Lune en Verseau amplifie ta Maison 11, maximisant ta vie sociale et tes projets collectifs. Tu es au cœur des réseaux.

## Ce que tu pourrais vivre
- Une vie sociale très active
- Des projets collectifs stimulants
- Des amitiés basées sur des idéaux partagés

## Conseils pour ce transit
- Participe activement à ta communauté
- Fédère les autres autour de tes idées
- Cultive des amitiés authentiques""",

    ('aquarius', 12): """# ☽ Transit de la Lune en Verseau

**En une phrase :** Ton inconscient s'éveille au collectif — médite sur ta contribution.

## L'énergie du moment
La Lune en Verseau traverse ta Maison 12, créant une connexion entre ton monde intérieur et le collectif. Tu réfléchis à ta place dans l'humanité.

## Ce que tu pourrais vivre
- Des intuitions sur l'avenir collectif
- Un détachement des attaches personnelles
- Des rêves de nature universelle

## Conseils pour ce transit
- Médite sur ta contribution à l'humanité
- Libère-toi des attaches limitantes
- Connecte-toi à quelque chose de plus grand""",

    # PISCES
    ('pisces', 1): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Ta sensibilité est à son apogée — laisse couler tes émotions.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 1, amplifiant ta sensibilité et ton intuition. Tu absorbes les émotions de ton environnement.

## Ce que tu pourrais vivre
- Une sensibilité extrême aux ambiances
- Un besoin de rêverie et d'évasion
- Une intuition particulièrement forte

## Conseils pour ce transit
- Protège-toi des énergies négatives
- Laisse tes émotions s'exprimer
- Connecte-toi à ta spiritualité""",

    ('pisces', 2): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Tes ressources suivent le flux — fais confiance à l'abondance.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 2, créant un rapport plus fluide et moins matérialiste à l'argent. Tu fais confiance au flux.

## Ce que tu pourrais vivre
- Un détachement vis-à-vis du matériel
- Des revenus liés à la créativité ou au spirituel
- Une confusion possible sur tes finances

## Conseils pour ce transit
- Fais confiance à l'abondance
- Évite les décisions financières majeures
- Valorise les richesses non matérielles""",

    ('pisces', 3): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Ta communication devient intuitive — exprime-toi avec ton âme.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 3, rendant ta communication plus intuitive et poétique. Tu ressens plus que tu ne penses.

## Ce que tu pourrais vivre
- Une communication plus floue mais plus sensible
- Des intuitions dans les conversations
- Un besoin d'expression artistique

## Conseils pour ce transit
- Exprime-toi à travers l'art ou la poésie
- Fais confiance à tes intuitions
- Sois patient avec les malentendus""",

    ('pisces', 4): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Ton foyer devient un sanctuaire — ressource-toi dans la paix.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 4, créant un besoin de paix et de spiritualité chez toi. Tu veux un refuge pour ton âme.

## Ce que tu pourrais vivre
- Un besoin intense de calme à la maison
- Des émotions du passé qui remontent
- L'envie de créer un espace sacré

## Conseils pour ce transit
- Crée un espace de paix chez toi
- Accueille les émotions du passé
- Ressource-toi dans la solitude""",

    ('pisces', 5): """# ☽ Transit de la Lune en Poissons

**En une phrase :** L'amour devient transcendant — vis des moments de pure magie.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 5, rendant tes expériences de plaisir et d'amour plus romantiques et spirituelles. Tu vis l'amour comme un rêve.

## Ce que tu pourrais vivre
- Des amours romantiques et idéalisées
- Une créativité inspirée et spirituelle
- Des moments de pure magie

## Conseils pour ce transit
- Laisse-toi porter par le romantisme
- Crée quelque chose qui vient de ton âme
- Évite d'idéaliser excessivement""",

    ('pisces', 6): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Ton corps parle de ton âme — écoute ses messages subtils.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 6, liant ta santé à ton état émotionnel et spirituel. Tu es sensible aux énergies.

## Ce que tu pourrais vivre
- Une sensibilité accrue à ton environnement de travail
- Des symptômes physiques liés aux émotions
- Un besoin de pratiques de santé douces

## Conseils pour ce transit
- Pratique le yoga ou la méditation
- Écoute les messages de ton corps
- Évite les environnements toxiques""",

    ('pisces', 7): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Tes relations deviennent profondes — connecte-toi âme à âme.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 7, rendant tes relations plus empathiques et spirituelles. Tu veux des connexions d'âme.

## Ce que tu pourrais vivre
- Des relations empreintes de compassion
- Un besoin de fusion émotionnelle
- L'attirance pour des âmes sensibles

## Conseils pour ce transit
- Connecte-toi avec empathie
- Évite de te perdre dans l'autre
- Cherche des relations qui nourrissent ton âme""",

    ('pisces', 8): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Les transformations se font par lâcher-prise — laisse le flux t'emporter.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 8, créant un processus de dissolution et de renaissance. Tu es invité à lâcher prise.

## Ce que tu pourrais vivre
- Une dissolution des vieilles structures
- Des expériences mystiques ou transpersonnelles
- Un lâcher-prise profond

## Conseils pour ce transit
- Lâche prise sur ce qui doit partir
- Fais confiance au processus de transformation
- Accueille les expériences mystiques""",

    ('pisces', 9): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Ta quête de sens devient mystique — explore les dimensions spirituelles.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 9, orientant ta recherche de sens vers le mystique et le transcendant. Tu cherches l'union avec le divin.

## Ce que tu pourrais vivre
- Un intérêt pour les traditions mystiques
- Des voyages intérieurs ou des retraites
- Des expériences qui élargissent ta conscience

## Conseils pour ce transit
- Explore une tradition spirituelle
- Médite sur l'unité de toutes choses
- Voyage vers des lieux sacrés""",

    ('pisces', 10): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Ta carrière cherche du sens — aligne ton travail avec ton âme.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 10, créant un besoin de sens et de spiritualité dans ta vie professionnelle. Tu veux un travail qui serve.

## Ce que tu pourrais vivre
- Un questionnement sur le sens de ta carrière
- Des opportunités dans les domaines de l'aide ou de l'art
- Un besoin d'aligner travail et valeurs profondes

## Conseils pour ce transit
- Réfléchis au sens de ton travail
- Explore des carrières qui aident les autres
- Fais confiance à ton intuition professionnelle""",

    ('pisces', 11): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Tes amitiés deviennent compassion — soutiens et sois soutenu.

## L'énergie du moment
La Lune en Poissons traverse ta Maison 11, rendant tes amitiés plus empathiques et spirituelles. Tu veux aider et être aidé.

## Ce que tu pourrais vivre
- Des moments de compassion partagée
- L'envie de t'engager pour des causes humanitaires
- Des amitiés spirituelles

## Conseils pour ce transit
- Soutiens un ami dans le besoin
- Engage-toi dans une cause humanitaire
- Cultive des amitiés basées sur la compassion""",

    ('pisces', 12): """# ☽ Transit de la Lune en Poissons

**En une phrase :** Tu retournes à la source — plonge dans l'océan de ton inconscient.

## L'énergie du moment
La Lune en Poissons amplifie ta Maison 12, créant une connexion maximale avec ton inconscient et le divin. C'est un temps de dissolution et de renaissance intérieure.

## Ce que tu pourrais vivre
- Une connexion profonde avec le divin
- Des rêves prophétiques et révélateurs
- Un besoin de solitude et de retrait

## Conseils pour ce transit
- Accorde-toi du temps de solitude méditative
- Écoute tes rêves et tes intuitions
- Laisse-toi porter par le flux de l'univers""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_MOON_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_moon',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP transit_moon/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='transit_moon',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT transit_moon/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
