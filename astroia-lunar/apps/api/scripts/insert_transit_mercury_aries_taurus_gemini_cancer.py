#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Mercure en Bélier/Taureau/Gémeaux/Cancer."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MERCURY_INTERPRETATIONS = {
    # ARIES
    ('aries', 1): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Tes pensées s'accélèrent — communique avec audace et spontanéité.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 1, rendant ta communication directe et rapide. Tu as des idées à défendre et l'énergie pour les exprimer. Ton mental est vif et compétitif.

## Ce que tu pourrais vivre
- Une communication plus directe et assertive
- Des idées qui fusent et veulent être exprimées
- Un besoin de prendre les devants intellectuellement

## Conseils pour ce transit
- Exprime tes idées sans tourner autour du pot
- Lance les conversations et projets que tu repoussais
- Évite les paroles impulsives que tu pourrais regretter""",

    ('aries', 2): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Tes idées sur l'argent s'activent — négocie avec audace.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 2, stimulant ta réflexion sur les finances et tes talents. Tu as des idées pour augmenter tes revenus et l'audace de les défendre.

## Ce que tu pourrais vivre
- Des négociations financières dynamiques
- Des idées rapides pour gagner de l'argent
- L'envie de défendre ta valeur

## Conseils pour ce transit
- Négocie ton salaire ou tes tarifs
- Lance une idée commerciale qui te tient à cœur
- Réfléchis avant les décisions financières impulsives""",

    ('aries', 3): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Ta communication est au maximum — échange, apprends et partage.

## L'énergie du moment
Mercure en Bélier amplifie ta Maison 3, maximisant ta vivacité d'esprit et ta communication. Les idées fusent, les conversations sont vives et les échanges nombreux.

## Ce que tu pourrais vivre
- Une communication rapide et directe
- Des débats stimulants
- Des déplacements courts mais intenses

## Conseils pour ce transit
- Lance les discussions importantes
- Apprends quelque chose de nouveau rapidement
- Évite les disputes verbales inutiles""",

    ('aries', 4): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Les discussions à la maison s'animent — aborde les sujets familiaux.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 4, apportant de l'énergie dans les communications familiales. Tu as envie de régler des questions domestiques ou de discuter franchement.

## Ce que tu pourrais vivre
- Des conversations animées en famille
- L'envie de réorganiser ton espace de vie
- Des décisions rapides concernant le foyer

## Conseils pour ce transit
- Aborde les sujets que tu évitais en famille
- Planifie des changements domestiques
- Évite les conflits verbaux à la maison""",

    ('aries', 5): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Ta créativité mentale s'active — joue avec les idées.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 5, stimulant ta créativité intellectuelle et tes échanges amoureux. Tu veux t'amuser avec les mots et les idées.

## Ce que tu pourrais vivre
- Une créativité vive basée sur les idées
- Des flirts stimulants intellectuellement
- Des jeux d'esprit et de mots

## Conseils pour ce transit
- Lance un projet créatif basé sur une idée
- En amour, séduis par ton esprit
- Joue à des jeux qui stimulent ton mental""",

    ('aries', 6): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Ton efficacité s'accélère — attaque tes tâches avec méthode.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 6, rendant ton travail quotidien plus rapide et efficace. Tu veux accomplir les choses rapidement.

## Ce que tu pourrais vivre
- Une productivité accélérée
- Des communications directes avec les collègues
- L'envie d'améliorer tes méthodes de travail

## Conseils pour ce transit
- Attaque les tâches que tu repoussais
- Communique directement avec ton équipe
- Prends des décisions rapides pour ta santé""",

    ('aries', 7): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Les discussions avec les partenaires s'intensifient — clarifie tes attentes.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 7, rendant les échanges avec les partenaires plus directs. Tu as besoin de clarifier les choses dans tes relations.

## Ce que tu pourrais vivre
- Des discussions franches avec ton partenaire
- Des négociations directes en affaires
- L'envie de régler les malentendus rapidement

## Conseils pour ce transit
- Exprime clairement tes besoins relationnels
- Négocie les termes de tes partenariats
- Évite les paroles blessantes dans les discussions""",

    ('aries', 8): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Ton esprit explore les profondeurs — cherche la vérité.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 8, stimulant ta curiosité pour les sujets profonds ou tabous. Tu veux comprendre ce qui est caché.

## Ce que tu pourrais vivre
- Des conversations sur des sujets profonds
- Des recherches sur les finances partagées
- L'envie de découvrir des secrets

## Conseils pour ce transit
- Pose les questions directes sur les sujets délicats
- Informe-toi sur les questions financières partagées
- Explore les profondeurs avec courage""",

    ('aries', 9): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Ta soif d'apprendre s'enflamme — explore de nouveaux territoires.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 9, stimulant ta curiosité intellectuelle et ton goût pour l'aventure. Tu veux élargir tes horizons rapidement.

## Ce que tu pourrais vivre
- Un intérêt soudain pour un nouveau domaine
- Des discussions passionnées sur des idées
- Des projets de voyage ou d'études

## Conseils pour ce transit
- Lance-toi dans un nouvel apprentissage
- Défends tes idées avec conviction
- Planifie un voyage qui t'inspire""",

    ('aries', 10): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Ta communication professionnelle s'affirme — prends les devants.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 10, rendant ta communication professionnelle plus assertive. Tu veux faire entendre tes idées au travail.

## Ce que tu pourrais vivre
- Des opportunités de présenter tes idées
- Une communication directe avec les supérieurs
- L'envie de prendre des initiatives professionnelles

## Conseils pour ce transit
- Propose tes idées aux bonnes personnes
- Prends l'initiative dans les communications pro
- Évite d'être trop confrontationnel""",

    ('aries', 11): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Tes échanges avec tes amis s'activent — partage tes idées.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 11, stimulant tes échanges avec tes amis et ton réseau. Tu veux partager tes idées pour l'avenir.

## Ce que tu pourrais vivre
- Des discussions animées avec tes amis
- Des projets de groupe qui avancent vite
- L'envie de fédérer autour de tes idées

## Conseils pour ce transit
- Propose tes idées à ton réseau
- Lance des projets collectifs
- Écoute aussi les idées des autres""",

    ('aries', 12): """# ☿ Transit de Mercure en Bélier

**En une phrase :** Ton mental explore l'inconscient — écoute tes intuitions.

## L'énergie du moment
Mercure en Bélier traverse ta Maison 12, créant une activité mentale intense dans ton monde intérieur. Tes pensées peuvent être rapides mais floues.

## Ce que tu pourrais vivre
- Des intuitions soudaines
- Des pensées qui surgissent de nulle part
- Des rêves actifs et révélateurs

## Conseils pour ce transit
- Journalise tes pensées et intuitions
- Médite pour clarifier ton mental
- Évite de ruminer des pensées négatives""",

    # TAURUS
    ('taurus', 1): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Tes pensées se posent — communique avec calme et réflexion.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 1, ralentissant ton mental et rendant ta communication plus posée. Tu réfléchis avant de parler.

## Ce que tu pourrais vivre
- Une communication plus réfléchie et mesurée
- Des idées qui mûrissent lentement
- Un besoin de temps pour t'exprimer

## Conseils pour ce transit
- Prends le temps de formuler tes pensées
- Communique sur des sujets concrets
- Évite de te précipiter dans les décisions""",

    ('taurus', 2): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Tes réflexions financières s'approfondissent — planifie avec soin.

## L'énergie du moment
Mercure en Taureau amplifie ta Maison 2, concentrant tes pensées sur les questions pratiques et financières. Tu veux des solutions durables.

## Ce que tu pourrais vivre
- Une réflexion approfondie sur tes finances
- Des idées pour sécuriser tes ressources
- Des négociations patientes et efficaces

## Conseils pour ce transit
- Planifie tes finances à long terme
- Prends des décisions financières réfléchies
- Valorise la qualité sur la quantité""",

    ('taurus', 3): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Ta communication devient substantielle — exprime-toi avec poids.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 3, rendant ta communication plus lente mais plus profonde. Tes mots ont du poids.

## Ce que tu pourrais vivre
- Des conversations profondes et constructives
- Un apprentissage lent mais durable
- Des échanges sur des sujets pratiques

## Conseils pour ce transit
- Prends le temps de bien t'exprimer
- Apprends quelque chose de pratique
- Évite les conversations superficielles""",

    ('taurus', 4): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Les réflexions sur le foyer s'approfondissent — planifie ton chez-toi.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 4, orientant tes pensées vers ton foyer et ta sécurité. Tu réfléchis à ton confort domestique.

## Ce que tu pourrais vivre
- Des réflexions sur ton habitat
- L'envie de planifier des améliorations chez toi
- Des conversations calmes en famille

## Conseils pour ce transit
- Planifie des projets pour ton foyer
- Discute sereinement avec ta famille
- Réfléchis à ce qui te fait te sentir en sécurité""",

    ('taurus', 5): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Ta créativité devient concrète — donne forme à tes idées.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 5, rendant ta créativité plus tangible. Tu veux créer quelque chose de concret et durable.

## Ce que tu pourrais vivre
- Une créativité orientée vers l'artisanat
- Des conversations amoureuses profondes
- Des plaisirs intellectuels simples

## Conseils pour ce transit
- Crée quelque chose avec tes mains
- En amour, communique avec patience
- Savoure les plaisirs de l'esprit""",

    ('taurus', 6): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Ton travail devient méthodique — organise tes tâches avec soin.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 6, rendant ton approche du travail plus méthodique. Tu veux des systèmes qui fonctionnent.

## Ce que tu pourrais vivre
- Une productivité constante et fiable
- Des réflexions sur ta santé et ton bien-être
- L'envie d'optimiser tes routines

## Conseils pour ce transit
- Établis des méthodes de travail durables
- Réfléchis à ton alimentation et ta santé
- Évite de te précipiter dans les tâches""",

    ('taurus', 7): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Les discussions relationnelles s'approfondissent — construis la confiance.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 7, favorisant les communications posées et fiables avec les partenaires. Tu veux des échanges constructifs.

## Ce que tu pourrais vivre
- Des conversations profondes avec ton partenaire
- Des négociations patientes en affaires
- L'envie de construire la confiance par les mots

## Conseils pour ce transit
- Prends le temps d'écouter ton partenaire
- Négocie avec patience et fermeté
- Construis des accords durables""",

    ('taurus', 8): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Ton esprit explore les ressources profondes — planifie les transformations.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 8, orientant tes réflexions vers les ressources partagées et les changements profonds. Tu veux sécuriser les transformations.

## Ce que tu pourrais vivre
- Des réflexions sur les finances partagées
- Des conversations sur les héritages ou investissements
- Une approche pratique des transformations

## Conseils pour ce transit
- Planifie les questions financières partagées
- Aborde les sujets profonds avec patience
- Réfléchis à ce que tu veux transformer""",

    ('taurus', 9): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Ta quête de savoir devient pratique — apprends ce qui est utile.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 9, orientant ta curiosité vers des apprentissages pratiques. Tu veux une sagesse applicable.

## Ce que tu pourrais vivre
- Un intérêt pour des formations pratiques
- Des voyages planifiés avec soin
- Des réflexions sur des philosophies concrètes

## Conseils pour ce transit
- Inscris-toi à une formation qualifiante
- Planifie un voyage confortable
- Cherche la sagesse dans le quotidien""",

    ('taurus', 10): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Ta communication professionnelle devient solide — construis ta réputation.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 10, rendant ta communication professionnelle plus fiable et substantielle. Tu bâtis ta crédibilité.

## Ce que tu pourrais vivre
- Une reconnaissance pour ta fiabilité
- Des communications professionnelles posées
- L'envie de construire ta réputation par les actes

## Conseils pour ce transit
- Communique avec professionnalisme et constance
- Bâtis ta crédibilité par tes paroles
- Prends des décisions de carrière réfléchies""",

    ('taurus', 11): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Tes échanges avec tes amis s'ancrent — cultive des liens durables.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 11, favorisant les communications profondes avec tes amis. Tu veux des échanges constructifs.

## Ce que tu pourrais vivre
- Des conversations de qualité avec tes amis
- Des projets collectifs qui avancent lentement mais sûrement
- Des réflexions sur tes objectifs à long terme

## Conseils pour ce transit
- Cultive des conversations profondes avec tes amis
- Planifie des projets collectifs durables
- Réfléchis à ce que tu veux vraiment accomplir""",

    ('taurus', 12): """# ☿ Transit de Mercure en Taureau

**En une phrase :** Ton mental se calme — médite et réfléchis en profondeur.

## L'énergie du moment
Mercure en Taureau traverse ta Maison 12, ralentissant ton mental et favorisant l'introspection. Tu as besoin de calme pour penser.

## Ce que tu pourrais vivre
- Des pensées lentes et profondes
- Un besoin de solitude pour réfléchir
- Des intuitions qui mûrissent lentement

## Conseils pour ce transit
- Accorde-toi du temps de réflexion calme
- Médite pour clarifier tes pensées
- Laisse tes idées mûrir naturellement""",

    # GEMINI
    ('gemini', 1): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Ton esprit est vif comme l'éclair — communique, apprends, connecte.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 1, maximisant ta vivacité d'esprit et ta communication. Tu es curieux de tout et prêt à échanger.

## Ce que tu pourrais vivre
- Une communication particulièrement fluide
- Une curiosité insatiable
- Des échanges nombreux et stimulants

## Conseils pour ce transit
- Satisfais ta curiosité
- Échange avec le maximum de personnes
- Évite de te disperser dans trop de directions""",

    ('gemini', 2): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Tes idées ont de la valeur — explore plusieurs pistes.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 2, stimulant ta réflexion sur les moyens de valoriser tes talents. Tu as plusieurs idées pour gagner.

## Ce que tu pourrais vivre
- Des idées multiples pour tes finances
- L'envie de diversifier tes revenus
- Des négociations vives et habiles

## Conseils pour ce transit
- Explore plusieurs pistes financières
- Utilise tes talents de communication
- Note tes idées pour y revenir""",

    ('gemini', 3): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Ta communication atteint son apogée — brille par tes idées.

## L'énergie du moment
Mercure en Gémeaux amplifie au maximum ta Maison 3. C'est le moment idéal pour communiquer, apprendre, écrire et échanger.

## Ce que tu pourrais vivre
- Un flot d'idées et de conversations
- Des apprentissages rapides
- Des déplacements nombreux et stimulants

## Conseils pour ce transit
- Lance tous les projets de communication
- Apprends autant que tu peux
- Partage tes idées avec le monde""",

    ('gemini', 4): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Ton foyer s'anime intellectuellement — échange avec ta famille.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 4, apportant de la légèreté et de la communication à la maison. L'ambiance devient plus animée.

## Ce que tu pourrais vivre
- Des conversations animées en famille
- L'envie de réorganiser ton espace
- Des idées pour améliorer ton chez-toi

## Conseils pour ce transit
- Discute ouvertement avec ta famille
- Apporte de la nouveauté chez toi
- Travaille de chez toi si possible""",

    ('gemini', 5): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Ta créativité intellectuelle explose — joue avec les idées.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 5, stimulant ta créativité mentale et tes échanges ludiques. Tu veux t'amuser avec les mots et les idées.

## Ce que tu pourrais vivre
- Une créativité basée sur les idées
- Des flirts stimulants intellectuellement
- Des jeux de mots et d'esprit

## Conseils pour ce transit
- Lance un projet créatif intellectuel
- Séduis par ton esprit vif
- Amuse-toi avec des jeux de réflexion""",

    ('gemini', 6): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Ton travail gagne en variété — diversifie tes tâches.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 6, rendant ton quotidien plus varié et communicatif. Tu as besoin de diversité dans ton travail.

## Ce que tu pourrais vivre
- Des tâches variées et stimulantes
- Des échanges nombreux avec les collègues
- L'envie d'optimiser tes méthodes

## Conseils pour ce transit
- Varie tes activités quotidiennes
- Communique davantage au travail
- Informe-toi sur ta santé""",

    ('gemini', 7): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Les dialogues avec tes partenaires sont fluides — échange et négocie.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 7, facilitant les échanges avec les partenaires. La communication est au cœur de tes relations.

## Ce que tu pourrais vivre
- Des conversations stimulantes avec ton partenaire
- Des négociations fluides en affaires
- Le besoin de stimulation intellectuelle dans les relations

## Conseils pour ce transit
- Parle ouvertement avec tes partenaires
- Partage des idées et des découvertes
- Cherche des partenaires qui stimulent ton esprit""",

    ('gemini', 8): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Ton esprit explore les mystères — pose les questions qui comptent.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 8, stimulant ta curiosité pour les sujets profonds et cachés. Tu veux comprendre les mécanismes secrets.

## Ce que tu pourrais vivre
- Une curiosité pour les sujets tabous
- Des recherches sur les finances partagées
- Des conversations profondes mais légères

## Conseils pour ce transit
- Pose les questions qui t'intriguent
- Informe-toi sur les investissements
- Explore les profondeurs avec légèreté""",

    ('gemini', 9): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Ta soif de savoir est insatiable — explore dans toutes les directions.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 9, amplifiant ta curiosité intellectuelle au maximum. Tu veux tout savoir sur tout.

## Ce que tu pourrais vivre
- Une curiosité insatiable
- Des projets de voyages ou d'études
- Des échanges avec des personnes d'horizons variés

## Conseils pour ce transit
- Explore plusieurs sujets en même temps
- Voyage pour découvrir de nouveaux horizons
- Échange avec des personnes différentes""",

    ('gemini', 10): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Tes talents de communication brillent au travail — fais-toi remarquer.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 10, mettant tes compétences en communication au service de ta carrière. Tu peux te faire remarquer.

## Ce que tu pourrais vivre
- Des opportunités liées à la communication
- Une visibilité accrue pour tes idées
- Des échanges importants avec des influents

## Conseils pour ce transit
- Présente tes idées professionnellement
- Développe ton réseau
- Utilise les médias pour ta carrière""",

    ('gemini', 11): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Tes échanges avec ton réseau sont au maximum — connecte et partage.

## L'énergie du moment
Mercure en Gémeaux amplifie ta Maison 11, maximisant tes échanges avec tes amis et ton réseau. C'est le moment de socialiser et d'échanger des idées.

## Ce que tu pourrais vivre
- Une vie sociale très active intellectuellement
- Des projets de groupe stimulants
- Des idées pour l'avenir qui fusent

## Conseils pour ce transit
- Participe activement à ta communauté
- Lance des projets collectifs
- Partage ta vision avec tes amis""",

    ('gemini', 12): """# ☿ Transit de Mercure en Gémeaux

**En une phrase :** Ton mental est agité intérieurement — laisse tes pensées se poser.

## L'énergie du moment
Mercure en Gémeaux traverse ta Maison 12, créant beaucoup d'activité mentale intérieure. Tes pensées peuvent tourner en boucle.

## Ce que tu pourrais vivre
- Un flux de pensées difficile à calmer
- Des intuitions par fragments
- Des rêves agités mais révélateurs

## Conseils pour ce transit
- Journalise pour libérer ton mental
- Médite pour calmer les pensées
- Écoute tes intuitions""",

    # CANCER
    ('cancer', 1): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Tes pensées se teintent d'émotion — communique avec le cœur.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 1, rendant ta communication plus émotionnelle et intuitive. Tu exprimes tes pensées avec sensibilité.

## Ce que tu pourrais vivre
- Une communication plus personnelle et sensible
- Des pensées liées aux souvenirs et aux émotions
- Un besoin de se sentir compris

## Conseils pour ce transit
- Exprime ce que tu ressens vraiment
- Écoute ton intuition dans les échanges
- Évite de trop intellectualiser les émotions""",

    ('cancer', 2): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Tes réflexions financières sont intuitives — écoute ton instinct.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 2, liant tes pensées financières à tes émotions. Tu as une intuition pour ce qui a de la valeur.

## Ce que tu pourrais vivre
- Des intuitions sur tes finances
- Des réflexions sur ce qui te sécurise
- L'envie de valoriser ce qui te touche émotionnellement

## Conseils pour ce transit
- Écoute ton intuition financière
- Réfléchis à ce qui te fait te sentir en sécurité
- Évite les décisions financières sous le coup de l'émotion""",

    ('cancer', 3): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Ta communication devient intime — parle à cœur ouvert.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 3, rendant tes échanges plus personnels et émotionnels. Tu communiques avec ton cœur.

## Ce que tu pourrais vivre
- Des conversations intimes et personnelles
- Des échanges chaleureux avec tes proches
- Des pensées liées à la famille

## Conseils pour ce transit
- Parle à cœur ouvert avec tes proches
- Écoute avec empathie
- Renoue avec des membres de ta famille""",

    ('cancer', 4): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Ton mental se tourne vers le foyer — réfléchis à ta vie privée.

## L'énergie du moment
Mercure en Cancer amplifie ta Maison 4, concentrant tes pensées sur ta famille et ton foyer. Tu réfléchis à tes racines.

## Ce que tu pourrais vivre
- Des pensées sur ta famille et ton passé
- Des conversations profondes avec tes proches
- L'envie de créer un nid intellectuel chez toi

## Conseils pour ce transit
- Réfléchis à ce qui fait un bon foyer pour toi
- Discute avec ta famille de sujets importants
- Crée un espace pour lire et réfléchir chez toi""",

    ('cancer', 5): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Ta créativité se nourrit d'émotions — crée avec ton cœur.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 5, rendant ta créativité plus émotionnelle et intuitive. Tu veux créer quelque chose qui touche.

## Ce que tu pourrais vivre
- Une créativité nourrie par les émotions
- Des échanges amoureux empreints de tendresse
- L'envie de transmettre quelque chose de personnel

## Conseils pour ce transit
- Crée quelque chose qui vient du cœur
- En amour, communique tes sentiments
- Partage tes souvenirs et histoires""",

    ('cancer', 6): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Ton travail se teinte d'humanité — prends soin des autres.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 6, rendant ton approche du travail plus humaine et attentionnée. Tu veux aider et prendre soin.

## Ce que tu pourrais vivre
- Une attention accrue aux besoins des collègues
- Des réflexions sur ton bien-être au travail
- L'envie de créer une ambiance chaleureuse

## Conseils pour ce transit
- Prends soin de l'atmosphère au travail
- Écoute les besoins de ton équipe
- Attention à ton alimentation émotionnelle""",

    ('cancer', 7): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Les échanges avec tes partenaires se font intimes — partage tes émotions.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 7, rendant les communications relationnelles plus émotionnelles. Tu veux te sentir compris.

## Ce que tu pourrais vivre
- Des conversations intimes avec ton partenaire
- Un besoin de connexion émotionnelle par les mots
- L'envie de comprendre ce que ressent l'autre

## Conseils pour ce transit
- Exprime tes besoins émotionnels
- Écoute les émotions de ton partenaire
- Crée des moments d'intimité verbale""",

    ('cancer', 8): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Tes pensées explorent les profondeurs émotionnelles — accueille ce qui émerge.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 8, orientant tes réflexions vers les émotions profondes et le passé. Tu veux comprendre tes mécanismes émotionnels.

## Ce que tu pourrais vivre
- Des pensées sur le passé et les blessures
- Des conversations profondes sur les émotions
- Des intuitions sur les ressources partagées

## Conseils pour ce transit
- Explore tes émotions profondes avec douceur
- Parle de ce qui te touche vraiment
- Fais confiance à ton intuition""",

    ('cancer', 9): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Ta quête de sens passe par le cœur — cherche la sagesse émotionnelle.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 9, orientant ta recherche de sens vers l'émotionnel et l'intime. Tu cherches une sagesse qui parle au cœur.

## Ce que tu pourrais vivre
- Un intérêt pour les traditions familiales
- L'envie de voyager vers des lieux chargés d'histoire
- Des réflexions sur tes racines et ta philosophie de vie

## Conseils pour ce transit
- Explore tes racines et ton histoire familiale
- Voyage vers des lieux qui te touchent
- Cherche une sagesse qui résonne émotionnellement""",

    ('cancer', 10): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Ta communication professionnelle se fait humaine — montre ton empathie.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 10, rendant ta communication professionnelle plus empathique et attentionnée. Tu te fais remarquer par ton humanité.

## Ce que tu pourrais vivre
- Une reconnaissance pour ton écoute et ton empathie
- Des opportunités liées au care ou à l'accompagnement
- L'envie d'humaniser ton environnement de travail

## Conseils pour ce transit
- Montre ton côté humain au travail
- Utilise ton intuition professionnellement
- Communique avec empathie""",

    ('cancer', 11): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Tes échanges avec tes amis se font intimes — nourris ces liens.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 11, rendant tes communications amicales plus personnelles et chaleureuses. Tu considères tes amis comme une famille.

## Ce que tu pourrais vivre
- Des conversations profondes avec tes amis
- L'envie de prendre soin de ton réseau
- Des projets collectifs qui ont du cœur

## Conseils pour ce transit
- Partage tes émotions avec tes amis proches
- Crée des moments chaleureux avec ton groupe
- Soutiens émotionnellement ton réseau""",

    ('cancer', 12): """# ☿ Transit de Mercure en Cancer

**En une phrase :** Tes pensées plongent dans l'inconscient — écoute ta voix intérieure.

## L'énergie du moment
Mercure en Cancer traverse ta Maison 12, rendant tes pensées plus intuitives et liées à l'inconscient. Tes rêves sont particulièrement révélateurs.

## Ce que tu pourrais vivre
- Des pensées liées au passé qui remontent
- Des rêves émotionnels et révélateurs
- Un besoin de solitude pour réfléchir

## Conseils pour ce transit
- Journalise tes rêves et intuitions
- Accorde-toi du temps seul pour réfléchir
- Écoute ta voix intérieure""",
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
