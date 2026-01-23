#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Mercure en Lion/Vierge/Balance/Scorpion."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MERCURY_INTERPRETATIONS = {
    # LEO
    ('leo', 1): """# ☿ Transit de Mercure en Lion

**En une phrase :** Tes idées veulent briller — exprime-toi avec confiance et panache.

## L'énergie du moment
Mercure en Lion traverse ta Maison 1, rendant ta communication plus confiante et charismatique. Tu veux que tes idées soient entendues et admirées.

## Ce que tu pourrais vivre
- Une communication plus théâtrale et engageante
- L'envie de partager tes créations et idées
- Un besoin de reconnaissance intellectuelle

## Conseils pour ce transit
- Présente tes idées avec assurance
- N'aie pas peur de briller par ta parole
- Évite l'arrogance dans tes échanges""",

    ('leo', 2): """# ☿ Transit de Mercure en Lion

**En une phrase :** Tes idées sur la valeur s'affirment — communique sur ce que tu vaux.

## L'énergie du moment
Mercure en Lion traverse ta Maison 2, te donnant confiance pour parler de ta valeur et négocier. Tu veux être reconnu financièrement pour tes talents.

## Ce que tu pourrais vivre
- Des négociations confiantes sur ta valeur
- Des idées ambitieuses pour tes finances
- L'envie de dépenser pour ce qui te représente

## Conseils pour ce transit
- Négocie avec confiance
- Communique sur tes talents
- Évite les dépenses pour impressionner""",

    ('leo', 3): """# ☿ Transit de Mercure en Lion

**En une phrase :** Ta communication rayonne — captive par ta parole.

## L'énergie du moment
Mercure en Lion traverse ta Maison 3, rendant ta communication plus captivante et créative. Tu veux être le centre de la conversation.

## Ce que tu pourrais vivre
- Une parole qui captive et inspire
- L'envie de partager tes créations verbales
- Des échanges où tu brilles naturellement

## Conseils pour ce transit
- Présente tes idées avec créativité
- Prends la parole en public si possible
- Laisse aussi les autres s'exprimer""",

    ('leo', 4): """# ☿ Transit de Mercure en Lion

**En une phrase :** Les discussions à la maison s'animent — prends la parole en famille.

## L'énergie du moment
Mercure en Lion traverse ta Maison 4, apportant de l'énergie créative dans les communications familiales. Tu veux être reconnu chez toi.

## Ce que tu pourrais vivre
- Des conversations animées en famille
- L'envie de diriger les discussions domestiques
- Des idées créatives pour ton foyer

## Conseils pour ce transit
- Partage tes idées pour la maison
- Anime les discussions familiales
- Évite de monopoliser la parole""",

    ('leo', 5): """# ☿ Transit de Mercure en Lion

**En une phrase :** Ta créativité mentale explose — brille par tes idées.

## L'énergie du moment
Mercure en Lion amplifie ta Maison 5, maximisant ta créativité intellectuelle et tes échanges ludiques. Tu veux t'amuser et être admiré pour ton esprit.

## Ce que tu pourrais vivre
- Une créativité intellectuelle au maximum
- Des flirts basés sur le charisme verbal
- Des jeux où tu aimes briller

## Conseils pour ce transit
- Lance des projets créatifs intellectuels
- Séduis par ton esprit et ton humour
- Partage ta joie de vivre""",

    ('leo', 6): """# ☿ Transit de Mercure en Lion

**En une phrase :** Ton travail mérite de briller — montre ton excellence.

## L'énergie du moment
Mercure en Lion traverse ta Maison 6, rendant ton approche du travail plus confiante et créative. Tu veux être reconnu pour tes accomplissements.

## Ce que tu pourrais vivre
- Une envie de montrer tes réalisations
- Des communications confiantes au travail
- L'envie d'améliorer tes méthodes avec créativité

## Conseils pour ce transit
- Présente tes accomplissements
- Apporte de la créativité dans tes tâches
- Reste humble malgré tes succès""",

    ('leo', 7): """# ☿ Transit de Mercure en Lion

**En une phrase :** Les échanges avec tes partenaires s'animent — brille ensemble.

## L'énergie du moment
Mercure en Lion traverse ta Maison 7, rendant les communications relationnelles plus chaleureuses et généreuses. Tu veux partager la lumière.

## Ce que tu pourrais vivre
- Des échanges généreux avec ton partenaire
- L'envie de montrer votre couple au monde
- Des négociations confiantes en affaires

## Conseils pour ce transit
- Félicite et encourage ton partenaire
- Communiquez ensemble avec assurance
- Partagez la reconnaissance""",

    ('leo', 8): """# ☿ Transit de Mercure en Lion

**En une phrase :** Tes pensées explorent les profondeurs avec courage — affronte les vérités.

## L'énergie du moment
Mercure en Lion traverse ta Maison 8, te donnant le courage d'aborder les sujets profonds et délicats. Tu veux la vérité même si elle est difficile.

## Ce que tu pourrais vivre
- Des conversations courageuses sur des sujets tabous
- Des réflexions sur le pouvoir et la transformation
- L'envie de comprendre les motivations cachées

## Conseils pour ce transit
- Aborde les sujets difficiles avec dignité
- Négocie les ressources partagées avec confiance
- Évite les luttes d'ego""",

    ('leo', 9): """# ☿ Transit de Mercure en Lion

**En une phrase :** Ta quête de savoir s'enflamme — partage ta sagesse avec générosité.

## L'énergie du moment
Mercure en Lion traverse ta Maison 9, rendant ta recherche de sens plus enthousiaste et généreuse. Tu veux partager ce que tu apprends.

## Ce que tu pourrais vivre
- Un enthousiasme pour l'apprentissage
- L'envie d'enseigner ou de partager tes connaissances
- Des idées grandioses sur le sens de la vie

## Conseils pour ce transit
- Partage généreusement ton savoir
- Vise des apprentissages qui t'inspirent
- Évite de prêcher avec arrogance""",

    ('leo', 10): """# ☿ Transit de Mercure en Lion

**En une phrase :** Ta communication professionnelle brille — fais-toi remarquer.

## L'énergie du moment
Mercure en Lion traverse ta Maison 10, mettant tes talents de communication au service de ta carrière. Tu es visible et reconnu pour tes idées.

## Ce que tu pourrais vivre
- Des opportunités de visibilité professionnelle
- Une communication confiante avec les supérieurs
- L'envie de prendre le leadership intellectuel

## Conseils pour ce transit
- Présente tes idées aux décideurs
- Assume un rôle de leader dans les communications
- Reste accessible malgré ta confiance""",

    ('leo', 11): """# ☿ Transit de Mercure en Lion

**En une phrase :** Tes échanges avec tes amis brillent — inspire ton groupe.

## L'énergie du moment
Mercure en Lion traverse ta Maison 11, rendant tes communications amicales plus chaleureuses et inspirantes. Tu veux motiver ton réseau.

## Ce que tu pourrais vivre
- Un rôle de leader d'opinion dans ton groupe
- Des échanges enthousiastes avec tes amis
- Des projets collectifs portés par ta vision

## Conseils pour ce transit
- Inspire tes amis par tes idées
- Organise des événements pour ton groupe
- Laisse aussi les autres briller""",

    ('leo', 12): """# ☿ Transit de Mercure en Lion

**En une phrase :** Ta confiance intérieure grandit — cultive tes idées en secret.

## L'énergie du moment
Mercure en Lion traverse ta Maison 12, stimulant ta créativité intérieure et ta confiance secrète. Tu prépares tes prochaines grandes idées.

## Ce que tu pourrais vivre
- Des idées créatives qui mûrissent en toi
- Une confiance intérieure qui grandit
- Des rêves d'expression et de reconnaissance

## Conseils pour ce transit
- Cultive tes idées avant de les partager
- Médite sur ce qui te rend vraiment fier
- Prépare tes futures présentations""",

    # VIRGO
    ('virgo', 1): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ton esprit analytique est à son maximum — organise et perfectionne.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 1, rendant ta communication précise et analytique. Tu veux comprendre et améliorer tout ce que tu touches.

## Ce que tu pourrais vivre
- Une pensée particulièrement claire et organisée
- Un souci du détail dans ta communication
- Le besoin d'améliorer et d'optimiser

## Conseils pour ce transit
- Profite de ta clarté mentale
- Analyse et améliore ce qui peut l'être
- Évite d'être trop critique envers toi-même""",

    ('virgo', 2): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Tes réflexions financières sont précises — analyse et optimise.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 2, rendant ta gestion financière plus méthodique. Tu veux comprendre où va ton argent.

## Ce que tu pourrais vivre
- Une analyse détaillée de tes finances
- L'envie d'optimiser ton budget
- Des idées pratiques pour valoriser tes talents

## Conseils pour ce transit
- Fais un budget détaillé
- Analyse tes dépenses et optimise
- Développe des compétences pratiques""",

    ('virgo', 3): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ta communication atteint la perfection — exprime-toi avec précision.

## L'énergie du moment
Mercure en Vierge amplifie ta Maison 3, maximisant ta capacité d'analyse et de communication précise. C'est le moment idéal pour écrire, étudier et organiser.

## Ce que tu pourrais vivre
- Une communication particulièrement claire
- Des apprentissages efficaces
- L'envie de corriger et perfectionner

## Conseils pour ce transit
- Lance les projets d'écriture ou d'organisation
- Étudie des sujets pratiques
- Aide les autres avec des conseils concrets""",

    ('virgo', 4): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ton foyer demande de l'organisation — mets de l'ordre chez toi.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 4, orientant tes pensées vers l'organisation domestique. Tu veux un chez-toi fonctionnel et ordonné.

## Ce que tu pourrais vivre
- L'envie de ranger et d'organiser chez toi
- Des réflexions pratiques sur ton habitat
- Des conversations utiles en famille

## Conseils pour ce transit
- Organise et trie tes affaires
- Planifie des améliorations pratiques
- Aide ta famille avec des conseils concrets""",

    ('virgo', 5): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ta créativité se fait précise — perfectionne tes talents.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 5, rendant ta créativité plus technique et orientée vers la perfection. Tu veux maîtriser ton art.

## Ce que tu pourrais vivre
- Une créativité orientée vers l'artisanat
- Des échanges amoureux où tu analyses beaucoup
- L'envie de perfectionner une compétence

## Conseils pour ce transit
- Perfectionne un talent technique
- En amour, ne sois pas trop critique
- Crée quelque chose de précis et utile""",

    ('virgo', 6): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ton efficacité est au maximum — organise et améliore.

## L'énergie du moment
Mercure en Vierge amplifie ta Maison 6, maximisant ton efficacité et ton sens de l'organisation. Tu es au top de ta productivité.

## Ce que tu pourrais vivre
- Une productivité optimale
- Des améliorations dans tes méthodes de travail
- Une attention particulière à ta santé

## Conseils pour ce transit
- Organise ton travail efficacement
- Consulte un professionnel de santé
- Améliore tes routines quotidiennes""",

    ('virgo', 7): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Les échanges relationnels se font précis — améliore tes partenariats.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 7, rendant les communications avec les partenaires plus analytiques. Tu veux améliorer tes relations.

## Ce que tu pourrais vivre
- Des discussions constructives avec ton partenaire
- L'envie d'analyser et d'améliorer tes relations
- Des négociations précises en affaires

## Conseils pour ce transit
- Discute des améliorations possibles
- Sois utile et serviable avec ton partenaire
- Évite les critiques excessives""",

    ('virgo', 8): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ton analyse des profondeurs est aiguisée — comprends les mécanismes.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 8, rendant ton analyse des situations profondes particulièrement précise. Tu veux comprendre les mécanismes cachés.

## Ce que tu pourrais vivre
- Une analyse lucide de tes schémas
- Des réflexions pratiques sur les finances partagées
- L'envie de comprendre ce qui te bloque

## Conseils pour ce transit
- Analyse tes mécanismes avec bienveillance
- Organise les questions financières partagées
- Évite de trop intellectualiser les émotions""",

    ('virgo', 9): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ta quête de savoir se fait pratique — apprends ce qui est utile.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 9, orientant ta curiosité vers des apprentissages pratiques et applicables. Tu veux une sagesse qui fonctionne.

## Ce que tu pourrais vivre
- Un intérêt pour des formations professionnelles
- Des voyages bien organisés
- Une philosophie pragmatique

## Conseils pour ce transit
- Inscris-toi à une formation qualifiante
- Planifie tes voyages dans les détails
- Cherche la sagesse dans les petites choses""",

    ('virgo', 10): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ta communication professionnelle est impeccable — montre ton expertise.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 10, rendant ta communication professionnelle particulièrement précise et compétente. Tu es reconnu pour ton expertise.

## Ce que tu pourrais vivre
- Une reconnaissance pour ta compétence technique
- Des communications professionnelles efficaces
- L'envie de perfectionner ta réputation

## Conseils pour ce transit
- Montre ton expertise par des résultats
- Communique avec précision au travail
- Propose des améliorations concrètes""",

    ('virgo', 11): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Tes échanges avec tes amis sont constructifs — aide ton réseau.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 11, rendant tes communications amicales plus pratiques et utiles. Tu veux aider concrètement tes amis.

## Ce que tu pourrais vivre
- Des conseils pratiques échangés avec tes amis
- Des projets de groupe bien organisés
- L'envie d'améliorer les choses pour tous

## Conseils pour ce transit
- Offre ton aide pratique à tes amis
- Organise les projets collectifs
- Propose des améliorations constructives""",

    ('virgo', 12): """# ☿ Transit de Mercure en Vierge

**En une phrase :** Ton analyse intérieure est précise — comprends tes profondeurs.

## L'énergie du moment
Mercure en Vierge traverse ta Maison 12, rendant ton analyse de l'inconscient plus précise. Tu peux comprendre tes mécanismes cachés.

## Ce que tu pourrais vivre
- Une analyse lucide de tes schémas inconscients
- Des pensées qui s'organisent dans la solitude
- L'envie de comprendre tes blocages

## Conseils pour ce transit
- Journalise pour analyser tes pensées
- Médite pour clarifier ton mental
- Travaille sur tes blocages avec méthode""",

    # LIBRA
    ('libra', 1): """# ☿ Transit de Mercure en Balance

**En une phrase :** Tes idées cherchent l'harmonie — communique avec diplomatie.

## L'énergie du moment
Mercure en Balance traverse ta Maison 1, rendant ta communication plus diplomatique et équilibrée. Tu veux des échanges harmonieux.

## Ce que tu pourrais vivre
- Une communication plus raffinée et diplomatique
- Le besoin de comprendre tous les points de vue
- Une attention à l'esthétique de tes mots

## Conseils pour ce transit
- Communique avec tact et grâce
- Cherche l'équilibre dans tes échanges
- Évite de trop hésiter par souci d'harmonie""",

    ('libra', 2): """# ☿ Transit de Mercure en Balance

**En une phrase :** Tes réflexions financières cherchent l'équilibre — harmonise ton budget.

## L'énergie du moment
Mercure en Balance traverse ta Maison 2, orientant tes pensées vers l'équilibre financier. Tu veux une gestion harmonieuse.

## Ce que tu pourrais vivre
- Des réflexions sur l'équilibre de ton budget
- L'envie d'investir dans la beauté
- Des négociations équilibrées

## Conseils pour ce transit
- Équilibre tes revenus et dépenses
- Négocie de façon équitable
- Investis dans ce qui embellit ta vie""",

    ('libra', 3): """# ☿ Transit de Mercure en Balance

**En une phrase :** Ta communication se fait diplomate — échange avec grâce.

## L'énergie du moment
Mercure en Balance traverse ta Maison 3, rendant ta communication particulièrement élégante et diplomatique. Tu excelles dans l'art de la conversation.

## Ce que tu pourrais vivre
- Des échanges harmonieux et équilibrés
- Un rôle de médiateur dans les conversations
- L'envie d'apprendre des sujets liés à l'art ou aux relations

## Conseils pour ce transit
- Utilise ta diplomatie pour faciliter les échanges
- Apprends quelque chose lié à l'art ou à la communication
- Écoute tous les points de vue""",

    ('libra', 4): """# ☿ Transit de Mercure en Balance

**En une phrase :** Les discussions à la maison cherchent la paix — crée l'harmonie.

## L'énergie du moment
Mercure en Balance traverse ta Maison 4, apportant une communication plus diplomatique à la maison. Tu veux la paix familiale.

## Ce que tu pourrais vivre
- Des conversations apaisantes en famille
- L'envie d'embellir ton intérieur
- Des réflexions sur l'équilibre domestique

## Conseils pour ce transit
- Favorise le dialogue en famille
- Apporte de la beauté chez toi
- Médite sur ce qui crée l'harmonie""",

    ('libra', 5): """# ☿ Transit de Mercure en Balance

**En une phrase :** Ta créativité se fait élégante — crée avec grâce.

## L'énergie du moment
Mercure en Balance traverse ta Maison 5, rendant ta créativité plus raffinée et esthétique. Tu veux créer de la beauté.

## Ce que tu pourrais vivre
- Une créativité orientée vers l'esthétique
- Des échanges amoureux élégants et romantiques
- L'envie de créer quelque chose de beau

## Conseils pour ce transit
- Crée quelque chose d'harmonieux
- En amour, séduis par ton élégance
- Apprécie les arts et la culture""",

    ('libra', 6): """# ☿ Transit de Mercure en Balance

**En une phrase :** Ton travail cherche l'équilibre — harmonise tes méthodes.

## L'énergie du moment
Mercure en Balance traverse ta Maison 6, orientant tes pensées vers l'équilibre au travail. Tu veux une vie professionnelle harmonieuse.

## Ce que tu pourrais vivre
- Un besoin d'harmonie avec les collègues
- L'envie d'équilibrer travail et vie personnelle
- Des réflexions sur l'esthétique de ton espace de travail

## Conseils pour ce transit
- Améliore les relations avec tes collègues
- Crée un environnement de travail agréable
- Cherche l'équilibre dans tes routines""",

    ('libra', 7): """# ☿ Transit de Mercure en Balance

**En une phrase :** Les communications relationnelles sont optimales — dialogue et négocie.

## L'énergie du moment
Mercure en Balance amplifie ta Maison 7, rendant les échanges avec les partenaires particulièrement fluides. C'est le moment idéal pour dialoguer.

## Ce que tu pourrais vivre
- Des conversations équilibrées avec ton partenaire
- Des négociations harmonieuses en affaires
- L'envie de trouver des compromis

## Conseils pour ce transit
- Discute ouvertement avec tes partenaires
- Négocie des accords équitables
- Cherche le compromis plutôt que la victoire""",

    ('libra', 8): """# ☿ Transit de Mercure en Balance

**En une phrase :** Tes pensées sur les profondeurs cherchent l'équilibre — aborde les sujets délicats avec tact.

## L'énergie du moment
Mercure en Balance traverse ta Maison 8, rendant ton approche des sujets profonds plus diplomatique. Tu abordes les transformations avec grâce.

## Ce que tu pourrais vivre
- Des conversations délicates mais équilibrées
- Des négociations sur les ressources partagées
- L'envie de trouver l'harmonie dans les changements

## Conseils pour ce transit
- Aborde les sujets difficiles avec diplomatie
- Négocie équitablement les questions financières
- Cherche l'équilibre dans les transformations""",

    ('libra', 9): """# ☿ Transit de Mercure en Balance

**En une phrase :** Ta quête de savoir passe par les autres — apprends de la diversité.

## L'énergie du moment
Mercure en Balance traverse ta Maison 9, orientant ta curiosité vers les cultures et perspectives différentes. Tu veux comprendre l'autre.

## Ce que tu pourrais vivre
- Un intérêt pour les philosophies de l'équilibre
- L'envie de voyager à deux ou pour des raisons culturelles
- Des échanges enrichissants avec des étrangers

## Conseils pour ce transit
- Voyage pour découvrir d'autres cultures
- Apprends de personnes différentes de toi
- Explore des sagesses qui parlent d'harmonie""",

    ('libra', 10): """# ☿ Transit de Mercure en Balance

**En une phrase :** Ta communication professionnelle brille par sa diplomatie — utilise ton charme.

## L'énergie du moment
Mercure en Balance traverse ta Maison 10, mettant tes talents diplomatiques au service de ta carrière. Tu es reconnu pour ton tact.

## Ce que tu pourrais vivre
- Des opportunités liées aux relations ou à la communication
- Une reconnaissance pour ta diplomatie
- L'envie de soigner ton image professionnelle

## Conseils pour ce transit
- Utilise ta diplomatie au travail
- Développe des partenariats professionnels
- Soigne ton image avec élégance""",

    ('libra', 11): """# ☿ Transit de Mercure en Balance

**En une phrase :** Tes échanges avec tes amis sont harmonieux — cultive des liens équilibrés.

## L'énergie du moment
Mercure en Balance traverse ta Maison 11, rendant tes communications amicales particulièrement agréables. Tu veux des amitiés équilibrées.

## Ce que tu pourrais vivre
- Des conversations agréables avec tes amis
- Des projets de groupe basés sur la collaboration
- L'envie de participer à des événements culturels

## Conseils pour ce transit
- Organise des sorties culturelles avec tes amis
- Favorise la collaboration dans les projets
- Cultive des amitiés réciproques""",

    ('libra', 12): """# ☿ Transit de Mercure en Balance

**En une phrase :** Tes pensées intérieures cherchent la paix — médite sur l'équilibre.

## L'énergie du moment
Mercure en Balance traverse ta Maison 12, orientant tes réflexions intérieures vers l'harmonie. Tu cherches la paix mentale.

## Ce que tu pourrais vivre
- Des réflexions sur l'équilibre intérieur
- Le besoin de paix et de solitude harmonieuse
- Des rêves liés aux relations

## Conseils pour ce transit
- Médite sur l'équilibre entre donner et recevoir
- Crée un espace de paix pour tes réflexions
- Explore tes besoins relationnels cachés""",

    # SCORPIO
    ('scorpio', 1): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Tes pensées deviennent pénétrantes — va au fond des choses.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 1, rendant ta communication plus intense et investigatrice. Tu veux la vérité, pas les apparences.

## Ce que tu pourrais vivre
- Une pensée pénétrante et investigatrice
- L'envie de découvrir ce qui est caché
- Une communication plus intense et magnétique

## Conseils pour ce transit
- Va au fond des sujets qui t'intéressent
- Utilise ton intuition dans les échanges
- Évite la manipulation ou l'obsession""",

    ('scorpio', 2): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Tes réflexions financières creusent en profondeur — transforme ta relation à l'argent.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 2, intensifiant ta réflexion sur les ressources et la valeur. Tu veux comprendre ta relation à l'argent.

## Ce que tu pourrais vivre
- Une analyse profonde de tes finances
- Des révélations sur ta relation à l'argent
- L'envie de transformer ta situation financière

## Conseils pour ce transit
- Explore les racines de ta relation à l'argent
- Élimine ce qui ne sert plus
- Investis dans ce qui te transforme""",

    ('scorpio', 3): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Ta communication devient investigatrice — découvre la vérité.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 3, rendant ta communication plus intense et ta curiosité plus profonde. Tu veux comprendre ce qui est caché.

## Ce que tu pourrais vivre
- Des conversations profondes et révélatrices
- L'envie de découvrir des secrets ou des vérités
- Une communication magnétique

## Conseils pour ce transit
- Pose les questions qui vont au fond
- Écoute ce qui n'est pas dit
- Évite les paroles blessantes""",

    ('scorpio', 4): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Les discussions familiales s'intensifient — explore les profondeurs du passé.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 4, intensifiant les communications familiales et les réflexions sur le passé. Des secrets peuvent émerger.

## Ce que tu pourrais vivre
- Des révélations sur ton histoire familiale
- Des conversations profondes avec tes proches
- L'envie de transformer quelque chose chez toi

## Conseils pour ce transit
- Explore ton histoire familiale
- Aborde les sujets difficiles avec courage
- Transforme ce qui a besoin de l'être""",

    ('scorpio', 5): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Ta créativité plonge dans les profondeurs — crée depuis ton ombre.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 5, rendant ta créativité plus intense et profonde. Tu veux créer quelque chose qui touche l'âme.

## Ce que tu pourrais vivre
- Une créativité qui explore les profondeurs
- Des échanges amoureux intenses et révélateurs
- L'envie de créer quelque chose de puissant

## Conseils pour ce transit
- Crée depuis tes profondeurs
- En amour, communique avec authenticité
- Explore les thèmes qui te fascinent""",

    ('scorpio', 6): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Ton analyse du quotidien devient profonde — transforme tes routines.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 6, intensifiant ton analyse du travail et de la santé. Tu veux comprendre les causes profondes.

## Ce que tu pourrais vivre
- Une analyse profonde de tes habitudes
- L'envie de transformer tes routines inefficaces
- Des réflexions sur les causes de tes problèmes de santé

## Conseils pour ce transit
- Élimine les habitudes qui ne servent plus
- Comprends les causes profondes de tes problèmes
- Transforme tes méthodes de travail""",

    ('scorpio', 7): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Les échanges relationnels s'intensifient — va au fond de tes relations.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 7, rendant les communications avec les partenaires plus intenses et profondes. Tu veux la vérité dans tes relations.

## Ce que tu pourrais vivre
- Des conversations profondes et transformatrices
- Des révélations sur tes relations
- L'envie de vérité et d'authenticité

## Conseils pour ce transit
- Parle authentiquement avec ton partenaire
- Explore les dynamiques cachées de tes relations
- Évite les manipulations""",

    ('scorpio', 8): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Ton esprit atteint ses profondeurs maximales — explore les mystères.

## L'énergie du moment
Mercure en Scorpion amplifie ta Maison 8, maximisant ton pouvoir d'investigation et de transformation. Tu peux comprendre les mécanismes les plus cachés.

## Ce que tu pourrais vivre
- Une compréhension profonde des mystères
- Des conversations sur la mort, le sexe, le pouvoir
- Des révélations sur tes mécanismes cachés

## Conseils pour ce transit
- Explore ce qui t'attire dans les profondeurs
- Transforme ce que tu comprends
- Utilise tes découvertes avec sagesse""",

    ('scorpio', 9): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Ta quête de savoir devient une investigation — découvre les vérités cachées.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 9, orientant ta curiosité vers les enseignements profonds et les vérités cachées. Tu veux une sagesse transformatrice.

## Ce que tu pourrais vivre
- Un intérêt pour les sciences occultes ou la psychologie
- Des voyages vers des lieux chargés de mystère
- Des remises en question profondes

## Conseils pour ce transit
- Explore des enseignements qui transforment
- Voyage vers des lieux de pouvoir
- Remets en question tes croyances superficielles""",

    ('scorpio', 10): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Ta communication professionnelle devient stratégique — utilise ton pouvoir avec sagesse.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 10, rendant ta communication professionnelle plus stratégique et puissante. Tu sais comment avoir de l'impact.

## Ce que tu pourrais vivre
- Une communication professionnelle magnétique
- Des stratégies de carrière bien pensées
- L'envie de transformer ta position

## Conseils pour ce transit
- Communique stratégiquement au travail
- Transforme ta carrière si nécessaire
- Utilise ton influence avec éthique""",

    ('scorpio', 11): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Tes échanges avec tes amis s'intensifient — crée des liens profonds.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 11, intensifiant tes communications amicales. Tu veux des amitiés authentiques et profondes.

## Ce que tu pourrais vivre
- Des conversations profondes avec tes amis
- L'envie de t'engager dans des causes transformatrices
- Des révélations sur tes véritables objectifs

## Conseils pour ce transit
- Choisis des amis authentiques
- Engage-toi dans des causes qui transforment
- Partage tes vérités avec ton réseau""",

    ('scorpio', 12): """# ☿ Transit de Mercure en Scorpion

**En une phrase :** Ton esprit plonge dans l'inconscient — explore tes profondeurs.

## L'énergie du moment
Mercure en Scorpion traverse ta Maison 12, intensifiant ton exploration de l'inconscient. Tu peux comprendre ce qui était caché.

## Ce que tu pourrais vivre
- Des révélations sur tes mécanismes inconscients
- Des rêves révélateurs et intenses
- Un travail profond sur l'ombre

## Conseils pour ce transit
- Explore ton inconscient avec courage
- Journalise tes rêves et intuitions
- Transforme ce que tu découvres en toi""",
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
