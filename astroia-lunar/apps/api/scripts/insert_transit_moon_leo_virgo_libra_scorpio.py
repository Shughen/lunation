#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Lune en Lion/Vierge/Balance/Scorpion."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MOON_INTERPRETATIONS = {
    # LEO
    ('leo', 1): """# ☽ Transit de la Lune en Lion

**En une phrase :** Tu as besoin de briller — exprime ta créativité et ta joie.

## L'énergie du moment
La Lune en Lion traverse ta Maison 1, éveillant ton besoin de reconnaissance et d'expression. Tu veux être vu, apprécié et célébré.

## Ce que tu pourrais vivre
- Un besoin d'attention et de reconnaissance
- Une envie de te montrer sous ton meilleur jour
- Un regain de confiance et de charisme

## Conseils pour ce transit
- Exprime ta créativité
- Montre-toi avec fierté
- Évite de chercher la validation à tout prix""",

    ('leo', 2): """# ☽ Transit de la Lune en Lion

**En une phrase :** Ta valeur mérite d'être reconnue — affirme ce que tu vaux.

## L'énergie du moment
La Lune en Lion traverse ta Maison 2, liant tes émotions à ta valeur personnelle et financière. Tu veux des choses de qualité qui reflètent ta valeur.

## Ce que tu pourrais vivre
- Un désir de posséder de belles choses
- Le besoin d'être reconnu pour ta valeur
- Une générosité dans les dépenses

## Conseils pour ce transit
- Reconnais ta propre valeur
- Évite les achats ostentatoires
- Investis dans ce qui te rend vraiment fier""",

    ('leo', 3): """# ☽ Transit de la Lune en Lion

**En une phrase :** Ta parole porte — exprime-toi avec cœur et panache.

## L'énergie du moment
La Lune en Lion traverse ta Maison 3, rendant ta communication plus chaleureuse et dramatique. Tu veux être entendu et admiré pour tes idées.

## Ce que tu pourrais vivre
- Une communication plus expressive et théâtrale
- L'envie de partager tes créations ou tes idées
- Un besoin d'être reconnu intellectuellement

## Conseils pour ce transit
- Exprime tes idées avec passion
- Partage tes créations
- Évite d'écraser les autres pour briller""",

    ('leo', 4): """# ☽ Transit de la Lune en Lion

**En une phrase :** Ton foyer mérite d'être célébré — crée un espace dont tu es fier.

## L'énergie du moment
La Lune en Lion traverse ta Maison 4, éveillant ton besoin d'un foyer qui te représente. Tu veux une maison dont tu peux être fier.

## Ce que tu pourrais vivre
- L'envie de recevoir et d'impressionner chez toi
- Un besoin de fierté par rapport à ton foyer
- Des moments chaleureux en famille

## Conseils pour ce transit
- Décore ton espace avec des éléments qui te représentent
- Organise un moment festif à la maison
- Montre ta générosité à ta famille""",

    ('leo', 5): """# ☽ Transit de la Lune en Lion

**En une phrase :** La joie et la créativité t'appellent — vis pleinement le moment.

## L'énergie du moment
La Lune en Lion amplifie ta Maison 5, créant un besoin intense de plaisir, de créativité et d'amour. Tu veux t'amuser et être admiré.

## Ce que tu pourrais vivre
- Un élan créatif puissant
- Des moments de joie et de célébration
- Des flirts ou des moments romantiques intenses

## Conseils pour ce transit
- Crée quelque chose qui te rend fier
- Profite des plaisirs de la vie
- En amour, montre ta générosité""",

    ('leo', 6): """# ☽ Transit de la Lune en Lion

**En une phrase :** Ton travail mérite de la reconnaissance — brille dans ton quotidien.

## L'énergie du moment
La Lune en Lion traverse ta Maison 6, créant un besoin de reconnaissance pour ton travail quotidien. Tu veux que tes efforts soient vus et appréciés.

## Ce que tu pourrais vivre
- Un besoin d'être félicité pour ton travail
- L'envie d'apporter de la créativité dans tes tâches
- Une attention à ta vitalité physique

## Conseils pour ce transit
- Accomplis tes tâches avec excellence
- Prends soin de ta vitalité
- N'hésite pas à montrer tes accomplissements""",

    ('leo', 7): """# ☽ Transit de la Lune en Lion

**En une phrase :** Tes relations demandent de briller — admire et sois admiré.

## L'énergie du moment
La Lune en Lion traverse ta Maison 7, créant un besoin d'admiration mutuelle dans tes relations. Tu veux des partenaires qui t'élèvent.

## Ce que tu pourrais vivre
- Un désir de montrer ton couple au monde
- Le besoin d'être admiré par ton partenaire
- Des moments chaleureux et généreux à deux

## Conseils pour ce transit
- Admire sincèrement ton partenaire
- Sois généreux dans tes relations
- Évite les rivalités d'ego""",

    ('leo', 8): """# ☽ Transit de la Lune en Lion

**En une phrase :** Tes émotions profondes demandent de la dignité — traverse les crises avec fierté.

## L'énergie du moment
La Lune en Lion traverse ta Maison 8, créant une tension entre ton besoin de briller et les profondeurs émotionnelles. Tu veux traverser les épreuves avec dignité.

## Ce que tu pourrais vivre
- Des émotions intenses liées au pouvoir ou au contrôle
- Un besoin de garder ta fierté face aux crises
- Des questions sur les ressources partagées

## Conseils pour ce transit
- Garde ta dignité dans les moments difficiles
- Évite les luttes de pouvoir
- Transforme-toi avec courage""",

    ('leo', 9): """# ☽ Transit de la Lune en Lion

**En une phrase :** Ta quête de sens veut de la grandeur — vise haut et inspire.

## L'énergie du moment
La Lune en Lion traverse ta Maison 9, éveillant ton désir de grandes aventures et de sagesse. Tu veux des expériences qui t'élèvent.

## Ce que tu pourrais vivre
- L'envie de voyages grandioses
- Un intérêt pour des philosophies inspirantes
- Le désir de partager ta sagesse

## Conseils pour ce transit
- Planifie une aventure qui te fait rêver
- Partage ce que tu as appris
- Inspire les autres par ta vision""",

    ('leo', 10): """# ☽ Transit de la Lune en Lion

**En une phrase :** Ta carrière mérite la lumière — brille sur la scène professionnelle.

## L'énergie du moment
La Lune en Lion traverse ta Maison 10, amplifiant ton besoin de reconnaissance professionnelle. Tu veux être vu et respecté pour tes accomplissements.

## Ce que tu pourrais vivre
- Un besoin intense de reconnaissance au travail
- L'envie de prendre les devants professionnellement
- Une visibilité accrue

## Conseils pour ce transit
- Montre ton leadership
- Fais-toi remarquer par tes accomplissements
- Reste humble malgré les louanges""",

    ('leo', 11): """# ☽ Transit de la Lune en Lion

**En une phrase :** Tes amis t'inspirent — brille au sein de ton groupe.

## L'énergie du moment
La Lune en Lion traverse ta Maison 11, créant un besoin d'être apprécié dans tes cercles sociaux. Tu veux inspirer et être admiré par tes amis.

## Ce que tu pourrais vivre
- Un rôle de leader dans un groupe
- Des moments festifs avec tes amis
- L'envie d'inspirer ton réseau

## Conseils pour ce transit
- Organise un événement avec tes amis
- Encourage et soutiens ton groupe
- Laisse aussi briller les autres""",

    ('leo', 12): """# ☽ Transit de la Lune en Lion

**En une phrase :** Ta lumière intérieure brille — cultive ta confiance en toi.

## L'énergie du moment
La Lune en Lion traverse ta Maison 12, créant un besoin de cultiver ta confiance intérieure loin des regards. Ta créativité peut s'exprimer dans la solitude.

## Ce que tu pourrais vivre
- Un travail sur ta confiance en toi
- Une créativité qui s'exprime dans l'intimité
- Des rêves de reconnaissance ou de célébrité

## Conseils pour ce transit
- Cultive ta valeur intérieure sans public
- Crée pour toi-même
- Médite sur ce qui te rend vraiment fier""",

    # VIRGO
    ('virgo', 1): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Tu as besoin d'ordre — organise-toi et prends soin de toi.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 1, éveillant ton besoin de perfection et d'analyse. Tu veux te sentir utile et efficace.

## Ce que tu pourrais vivre
- Un regard critique sur toi-même
- L'envie de t'améliorer
- Un besoin de routine et d'ordre

## Conseils pour ce transit
- Occupe-toi de ta santé
- Évite l'autocritique excessive
- Trouve des façons d'être utile""",

    ('virgo', 2): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Tes finances méritent de l'attention — analyse et organise.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 2, rendant ton approche des finances plus analytique. Tu veux de l'ordre dans tes ressources.

## Ce que tu pourrais vivre
- Un besoin de faire le point sur tes finances
- L'envie d'économiser ou d'optimiser
- Une analyse de ce qui a de la valeur pour toi

## Conseils pour ce transit
- Fais un budget détaillé
- Élimine les dépenses inutiles
- Valorise les choses simples et utiles""",

    ('virgo', 3): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Ta communication gagne en précision — exprime-toi clairement.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 3, rendant ta communication plus précise et analytique. Tu veux être compris exactement.

## Ce que tu pourrais vivre
- Une communication détaillée et précise
- L'envie d'apprendre des choses pratiques
- Une attention aux détails dans les échanges

## Conseils pour ce transit
- Vérifie tes informations avant de les partager
- Apprends quelque chose d'utile
- Évite d'être trop critique dans tes mots""",

    ('virgo', 4): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Ton foyer a besoin d'ordre — nettoie et organise ton espace.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 4, créant un besoin de propreté et d'organisation chez toi. Tu te sens mieux dans un environnement ordonné.

## Ce que tu pourrais vivre
- L'envie de faire le ménage ou de ranger
- Un besoin d'hygiène et de propreté
- Une attention aux détails de ton intérieur

## Conseils pour ce transit
- Fais du tri dans tes affaires
- Nettoie un espace qui en a besoin
- Crée un environnement fonctionnel""",

    ('virgo', 5): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Ta créativité se fait précise — perfectionne tes talents.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 5, orientant ta créativité vers la précision et l'amélioration. Tu veux perfectionner ce que tu crées.

## Ce que tu pourrais vivre
- Une créativité orientée vers l'artisanat
- Un regard critique sur tes créations
- Des plaisirs simples et sains

## Conseils pour ce transit
- Perfectionne un talent ou une compétence
- Offre-toi des plaisirs modérés
- Évite de trop critiquer tes créations""",

    ('virgo', 6): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Ton quotidien atteint son excellence — optimise et prends soin de toi.

## L'énergie du moment
La Lune en Vierge amplifie ta Maison 6, maximisant ton efficacité et ton attention à la santé. Tu es au top de ta productivité.

## Ce que tu pourrais vivre
- Une productivité optimale
- Un intérêt pour améliorer ta santé
- Le besoin de routines efficaces

## Conseils pour ce transit
- Accomplis les tâches qui demandent de la précision
- Fais attention à ton alimentation
- Consulte un professionnel de santé si besoin""",

    ('virgo', 7): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Tes relations demandent de l'analyse — améliore-les avec discernement.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 7, rendant ton regard sur les relations plus analytique. Tu veux améliorer tes partenariats.

## Ce que tu pourrais vivre
- Une analyse des forces et faiblesses de tes relations
- L'envie d'aider ou de servir ton partenaire
- Un regard critique (peut-être trop) sur l'autre

## Conseils pour ce transit
- Sois utile à ton partenaire
- Évite d'être trop critique
- Discute des améliorations possibles""",

    ('virgo', 8): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Les profondeurs demandent de l'analyse — comprends tes mécanismes.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 8, orientant ton analyse vers les profondeurs psychologiques. Tu veux comprendre ce qui se passe en toi.

## Ce que tu pourrais vivre
- Une analyse de tes schémas émotionnels
- Un besoin de comprendre tes blocages
- Une attention aux finances partagées

## Conseils pour ce transit
- Analyse tes mécanismes avec bienveillance
- Mets de l'ordre dans les finances partagées
- Évite de trop intellectualiser les émotions""",

    ('virgo', 9): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Ta quête de sens se fait pratique — apprends des choses utiles.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 9, orientant ta recherche de connaissance vers le pratique. Tu veux une sagesse applicable.

## Ce que tu pourrais vivre
- Un intérêt pour des formations pratiques
- L'envie de voyager de façon organisée
- Une philosophie pragmatique

## Conseils pour ce transit
- Inscris-toi à une formation qualifiante
- Planifie un voyage bien organisé
- Cherche la sagesse dans les détails""",

    ('virgo', 10): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Ta carrière demande de l'excellence — montre ta compétence.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 10, mettant l'accent sur ton professionnalisme et ta compétence. Tu veux être reconnu pour ton efficacité.

## Ce que tu pourrais vivre
- Un besoin de montrer ton expertise
- Une attention aux détails professionnels
- L'envie d'améliorer ta réputation

## Conseils pour ce transit
- Accomplis tes tâches avec excellence
- Montre ta fiabilité
- Évite le perfectionnisme paralysant""",

    ('virgo', 11): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Tes projets collectifs gagnent en efficacité — contribue concrètement.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 11, orientant ta contribution aux groupes vers l'aide concrète. Tu veux être utile à tes amis.

## Ce que tu pourrais vivre
- L'envie d'aider concrètement tes amis
- Une contribution pratique à un projet de groupe
- Une analyse de tes objectifs à long terme

## Conseils pour ce transit
- Propose ton aide à un ami
- Contribue de façon pratique à un projet
- Définis des objectifs réalistes""",

    ('virgo', 12): """# ☽ Transit de la Lune en Vierge

**En une phrase :** Ton monde intérieur demande de l'ordre — médite et analyse.

## L'énergie du moment
La Lune en Vierge traverse ta Maison 12, créant un besoin de comprendre ton inconscient. Tu veux mettre de l'ordre dans tes pensées.

## Ce que tu pourrais vivre
- Une analyse de tes rêves et intuitions
- Un besoin de solitude productive
- Des inquiétudes ou ruminations à gérer

## Conseils pour ce transit
- Journalise pour clarifier tes pensées
- Médite pour calmer le mental
- Évite les inquiétudes excessives""",

    # LIBRA
    ('libra', 1): """# ☽ Transit de la Lune en Balance

**En une phrase :** Tu as besoin d'harmonie — cherche l'équilibre en toi et autour de toi.

## L'énergie du moment
La Lune en Balance traverse ta Maison 1, éveillant ton besoin de beauté, d'harmonie et de relations. Tu veux te sentir en paix avec toi-même et les autres.

## Ce que tu pourrais vivre
- Un besoin de plaire et d'être apprécié
- Une attention à ton apparence et ton style
- Un désir d'éviter les conflits

## Conseils pour ce transit
- Soigne ton apparence avec goût
- Cherche l'équilibre dans tes actions
- Évite de trop dépendre du regard des autres""",

    ('libra', 2): """# ☽ Transit de la Lune en Balance

**En une phrase :** Tes ressources cherchent l'équilibre — harmonise tes finances.

## L'énergie du moment
La Lune en Balance traverse ta Maison 2, créant un besoin d'équilibre dans tes finances. Tu veux un budget harmonieux.

## Ce que tu pourrais vivre
- Un besoin d'équilibrer tes dépenses et revenus
- L'envie d'acheter de belles choses
- Une réflexion sur le partage des ressources

## Conseils pour ce transit
- Équilibre ton budget
- Investis dans la beauté avec modération
- Partage équitablement si nécessaire""",

    ('libra', 3): """# ☽ Transit de la Lune en Balance

**En une phrase :** Ta communication se fait diplomate — échange avec tact et grâce.

## L'énergie du moment
La Lune en Balance traverse ta Maison 3, rendant ta communication plus diplomatique et harmonieuse. Tu veux des échanges agréables.

## Ce que tu pourrais vivre
- Des conversations harmonieuses et agréables
- L'envie de trouver des compromis
- Un rôle de médiateur dans les échanges

## Conseils pour ce transit
- Écoute tous les points de vue
- Communique avec tact
- Évite de fuir les sujets difficiles par souci d'harmonie""",

    ('libra', 4): """# ☽ Transit de la Lune en Balance

**En une phrase :** Ton foyer cherche la paix — crée un espace harmonieux.

## L'énergie du moment
La Lune en Balance traverse ta Maison 4, créant un besoin de beauté et d'harmonie chez toi. Tu veux un foyer paisible et esthétique.

## Ce que tu pourrais vivre
- Un besoin d'harmonie à la maison
- L'envie d'embellir ton intérieur
- Un désir de paix en famille

## Conseils pour ce transit
- Décore ton espace avec goût
- Favorise le dialogue en famille
- Crée une atmosphère apaisante""",

    ('libra', 5): """# ☽ Transit de la Lune en Balance

**En une phrase :** L'amour et la beauté t'appellent — vis des moments élégants.

## L'énergie du moment
La Lune en Balance traverse ta Maison 5, éveillant ton goût pour les plaisirs raffinés et l'amour romantique. Tu veux de la beauté dans tes loisirs.

## Ce que tu pourrais vivre
- Des romances élégantes et équilibrées
- Une créativité artistique
- Des plaisirs culturels et esthétiques

## Conseils pour ce transit
- Offre-toi une sortie culturelle
- En amour, crée des moments romantiques
- Exprime ta créativité à travers l'art""",

    ('libra', 6): """# ☽ Transit de la Lune en Balance

**En une phrase :** Ton quotidien cherche l'équilibre — harmonise travail et bien-être.

## L'énergie du moment
La Lune en Balance traverse ta Maison 6, créant un besoin d'harmonie dans ton travail et ta santé. Tu veux un quotidien équilibré.

## Ce que tu pourrais vivre
- Un besoin d'équilibre travail-vie personnelle
- L'envie d'améliorer l'ambiance au travail
- Une attention à l'esthétique de ton espace de travail

## Conseils pour ce transit
- Crée un environnement de travail agréable
- Équilibre effort et repos
- Améliore tes relations avec tes collègues""",

    ('libra', 7): """# ☽ Transit de la Lune en Balance

**En une phrase :** Tes relations sont au centre de tout — cultive l'harmonie avec les autres.

## L'énergie du moment
La Lune en Balance amplifie ta Maison 7, mettant les relations au premier plan. Tu as un besoin intense de connexion et d'harmonie avec les autres.

## Ce que tu pourrais vivre
- Un besoin d'être en couple ou en partenariat
- Des moments de partage harmonieux
- L'envie de résoudre les conflits

## Conseils pour ce transit
- Investis dans tes relations importantes
- Cherche le compromis
- Exprime tes besoins tout en écoutant l'autre""",

    ('libra', 8): """# ☽ Transit de la Lune en Balance

**En une phrase :** Les transformations cherchent l'équilibre — traverse les changements avec grâce.

## L'énergie du moment
La Lune en Balance traverse ta Maison 8, créant un besoin d'harmonie face aux changements profonds. Tu veux traverser les crises avec dignité.

## Ce que tu pourrais vivre
- Un besoin d'équité dans les ressources partagées
- Une approche diplomatique des sujets délicats
- Des négociations financières

## Conseils pour ce transit
- Négocie équitablement
- Aborde les sujets difficiles avec tact
- Cherche l'équilibre dans les transformations""",

    ('libra', 9): """# ☽ Transit de la Lune en Balance

**En une phrase :** Ta quête de sens passe par l'autre — explore la sagesse du partage.

## L'énergie du moment
La Lune en Balance traverse ta Maison 9, orientant ta recherche de sens vers les relations et l'équilibre. Tu veux une philosophie de l'harmonie.

## Ce que tu pourrais vivre
- Un intérêt pour les philosophies de l'équilibre
- L'envie de voyager à deux
- Des échanges enrichissants avec d'autres cultures

## Conseils pour ce transit
- Voyage avec un partenaire
- Explore des sagesses qui parlent d'harmonie
- Échange avec des personnes de cultures différentes""",

    ('libra', 10): """# ☽ Transit de la Lune en Balance

**En une phrase :** Ta carrière brille par tes relations — utilise ta diplomatie.

## L'énergie du moment
La Lune en Balance traverse ta Maison 10, mettant en avant tes talents relationnels au travail. Tu veux être reconnu pour ta capacité à créer l'harmonie.

## Ce que tu pourrais vivre
- Des opportunités liées aux relations
- Une reconnaissance pour ta diplomatie
- Un besoin d'équilibre carrière-vie personnelle

## Conseils pour ce transit
- Utilise ta diplomatie au travail
- Développe des partenariats professionnels
- Soigne ton image publique""",

    ('libra', 11): """# ☽ Transit de la Lune en Balance

**En une phrase :** Tes amitiés s'harmonisent — cultive des liens équilibrés.

## L'énergie du moment
La Lune en Balance traverse ta Maison 11, mettant l'accent sur l'harmonie dans tes amitiés et tes groupes. Tu veux des relations sociales équilibrées.

## Ce que tu pourrais vivre
- Une vie sociale agréable et harmonieuse
- L'envie de participer à des événements culturels
- Des projets de groupe basés sur la collaboration

## Conseils pour ce transit
- Organise une sortie culturelle avec tes amis
- Favorise la collaboration dans les projets de groupe
- Cultive des amitiés réciproques""",

    ('libra', 12): """# ☽ Transit de la Lune en Balance

**En une phrase :** Ton monde intérieur cherche la paix — médite sur l'harmonie.

## L'énergie du moment
La Lune en Balance traverse ta Maison 12, créant un besoin de paix intérieure et d'équilibre spirituel. Tu cherches l'harmonie profonde.

## Ce que tu pourrais vivre
- Un besoin de solitude paisible
- Des réflexions sur l'équilibre intérieur
- Des rêves liés aux relations ou à la beauté

## Conseils pour ce transit
- Médite sur l'équilibre intérieur
- Crée un espace de paix pour ton introspection
- Explore tes besoins relationnels inconscients""",

    # SCORPIO
    ('scorpio', 1): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Tes émotions sont intenses — plonge dans tes profondeurs.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 1, amplifiant l'intensité de tes émotions et ton magnétisme. Tu ressens tout plus profondément.

## Ce que tu pourrais vivre
- Des émotions intenses et profondes
- Un regard pénétrant sur les autres
- Un besoin de vérité et d'authenticité

## Conseils pour ce transit
- Accueille tes émotions sans les fuir
- Utilise ton intuition
- Évite les manipulations ou les jeux de pouvoir""",

    ('scorpio', 2): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Tes ressources demandent une transformation — regarde en face ta situation.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 2, intensifiant ton rapport à l'argent et à la valeur personnelle. Tu veux transformer ta situation financière.

## Ce que tu pourrais vivre
- Un regard sans concession sur tes finances
- Un désir de contrôle sur tes ressources
- Des réflexions profondes sur ta valeur

## Conseils pour ce transit
- Fais un audit honnête de tes finances
- Élimine ce qui ne sert plus
- Travaille sur ta confiance en ta valeur""",

    ('scorpio', 3): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Ta communication devient pénétrante — va au fond des choses.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 3, rendant tes échanges plus profonds et intenses. Tu veux des conversations qui vont à l'essentiel.

## Ce que tu pourrais vivre
- Des conversations profondes et révélatrices
- L'envie de découvrir des secrets ou des vérités
- Une communication intense et magnétique

## Conseils pour ce transit
- Pose les questions qui comptent vraiment
- Écoute ce qui n'est pas dit
- Évite les paroles blessantes""",

    ('scorpio', 4): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Ton foyer vit des intensités — transforme ton espace intérieur.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 4, amplifiant les émotions liées à la famille et au passé. Des mémoires profondes peuvent remonter.

## Ce que tu pourrais vivre
- Des émotions intenses liées au passé familial
- Un besoin de transformer quelque chose chez toi
- Des révélations ou secrets familiaux

## Conseils pour ce transit
- Explore tes racines avec courage
- Transforme un aspect de ton chez-toi
- Libère les mémoires émotionnelles""",

    ('scorpio', 5): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** L'amour devient passion — vis des expériences intenses.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 5, intensifiant tes expériences de plaisir et d'amour. Tu vis tout avec passion.

## Ce que tu pourrais vivre
- Des amours passionnés et intenses
- Une créativité qui touche aux profondeurs
- Des plaisirs qui transforment

## Conseils pour ce transit
- Vis l'amour avec intensité mais conscience
- Crée quelque chose qui vient de tes profondeurs
- Évite la jalousie ou la possessivité""",

    ('scorpio', 6): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Ton quotidien se transforme — élimine ce qui ne sert plus.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 6, créant un besoin de transformer tes routines et ta santé. Tu veux éliminer ce qui nuit.

## Ce que tu pourrais vivre
- L'envie de purger tes routines inefficaces
- Un travail profond sur ta santé
- Des transformations au travail

## Conseils pour ce transit
- Élimine les habitudes nocives
- Travaille sur les causes profondes de tes problèmes
- Accepte les changements nécessaires""",

    ('scorpio', 7): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Tes relations s'intensifient — vis des connexions profondes.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 7, intensifiant tes relations. Tu veux des connexions authentiques et profondes.

## Ce que tu pourrais vivre
- Des relations intenses et transformatrices
- Un besoin de vérité dans tes partenariats
- Des révélations sur tes relations

## Conseils pour ce transit
- Approfondis tes relations avec courage
- Évite les jeux de pouvoir
- Accepte les transformations relationnelles""",

    ('scorpio', 8): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Tu es au cœur de tes profondeurs — transforme-toi.

## L'énergie du moment
La Lune en Scorpion amplifie ta Maison 8, créant une intensité émotionnelle maximale. C'est le moment des transformations profondes.

## Ce que tu pourrais vivre
- Des émotions intenses qui demandent à être vécues
- Des révélations sur tes mécanismes profonds
- Un besoin de mourir à quelque chose pour renaître

## Conseils pour ce transit
- Accueille les transformations
- Explore tes profondeurs avec courage
- Libère ce qui doit mourir""",

    ('scorpio', 9): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Ta quête de sens s'intensifie — explore les mystères de l'existence.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 9, orientant ta recherche de sens vers les profondeurs. Tu veux comprendre les mystères.

## Ce que tu pourrais vivre
- Un intérêt pour les sujets ésotériques ou psychologiques
- L'envie de voyager vers des lieux chargés d'histoire
- Des remises en question profondes

## Conseils pour ce transit
- Explore un sujet mystérieux qui t'attire
- Voyage vers des lieux de pouvoir
- Remets en question tes croyances superficielles""",

    ('scorpio', 10): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Ta carrière se transforme — utilise ton pouvoir avec sagesse.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 10, intensifiant tes ambitions et ton désir de pouvoir. Tu veux avoir un impact profond.

## Ce que tu pourrais vivre
- Des transformations dans ta carrière
- Un besoin de pouvoir ou de contrôle professionnel
- Des révélations sur ta vocation

## Conseils pour ce transit
- Utilise ton influence avec sagesse
- Transforme positivement ton environnement professionnel
- Évite les luttes de pouvoir""",

    ('scorpio', 11): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Tes projets collectifs s'intensifient — engage-toi pour transformer.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 11, intensifiant tes engagements collectifs. Tu veux des amis authentiques et des causes qui transforment.

## Ce que tu pourrais vivre
- Des amitiés intenses et transformatrices
- Un engagement dans des causes profondes
- Des révélations sur tes objectifs

## Conseils pour ce transit
- Choisis des amis authentiques
- Engage-toi dans des causes de transformation
- Évite les dynamiques de groupe toxiques""",

    ('scorpio', 12): """# ☽ Transit de la Lune en Scorpion

**En une phrase :** Tes profondeurs inconscientes s'activent — plonge dans l'ombre.

## L'énergie du moment
La Lune en Scorpion traverse ta Maison 12, amplifiant ton monde intérieur et ton inconscient. Des émotions profondes peuvent émerger.

## Ce que tu pourrais vivre
- Des émotions intenses sans cause apparente
- Des rêves révélateurs et puissants
- Un travail profond sur l'inconscient

## Conseils pour ce transit
- Médite sur tes ombres avec courage
- Journalise tes rêves et intuitions
- Accepte ce qui émerge des profondeurs""",
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
