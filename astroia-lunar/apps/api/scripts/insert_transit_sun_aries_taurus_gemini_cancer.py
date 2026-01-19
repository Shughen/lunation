#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Soleil en Bélier/Taureau/Gémeaux/Cancer."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SUN_INTERPRETATIONS = {
    # ARIES
    ('aries', 1): """# ☉ Transit du Soleil en Bélier

**En une phrase :** Ta vitalité explose et tu es prêt à conquérir le monde — c'est ton moment pour briller.

## L'énergie du moment
Le Soleil traverse ta Maison 1, celle de l'identité et de l'image de soi. En Bélier, cette énergie est doublement dynamique : c'est le moment de prendre des initiatives, d'affirmer qui tu es et de te lancer dans de nouveaux projets. Tu rayonnes naturellement et les autres te remarquent.

## Ce que tu pourrais vivre
- Un regain d'énergie physique et de motivation
- L'envie de prendre les devants dans un domaine de ta vie
- Des occasions de te mettre en avant ou de te présenter sous un nouveau jour

## Conseils pour ce transit
- Ose te montrer tel que tu es vraiment
- Lance un projet personnel qui te tient à cœur
- Profite de cette énergie pour faire du sport ou bouger davantage""",

    ('aries', 2): """# ☉ Transit du Soleil en Bélier

**En une phrase :** L'heure est à l'action financière — prends l'initiative pour améliorer ta sécurité matérielle.

## L'énergie du moment
Le Soleil en Bélier traverse ta Maison 2 des ressources et de l'estime de soi. Cette énergie te pousse à agir concrètement pour augmenter tes revenus ou valoriser tes talents. Tu as envie de prouver ta valeur de façon tangible.

## Ce que tu pourrais vivre
- Des opportunités de gagner plus par tes propres initiatives
- Un besoin de clarifier ce qui compte vraiment pour toi
- L'envie d'investir en toi-même ou dans tes compétences

## Conseils pour ce transit
- Fais le point sur tes finances et prends une décision courageuse
- Reconnais ta valeur et demande ce que tu mérites
- Évite les dépenses impulsives même si l'énergie est vive""",

    ('aries', 3): """# ☉ Transit du Soleil en Bélier

**En une phrase :** Tes idées fusent et ta parole porte — c'est le moment de communiquer avec audace.

## L'énergie du moment
Le Soleil en Bélier illumine ta Maison 3 de la communication et des échanges. Tu as des idées à défendre, des choses à dire, et l'énergie pour les exprimer. Les conversations sont vives, les déplacements peuvent s'accélérer.

## Ce que tu pourrais vivre
- Des échanges stimulants qui t'encouragent à aller de l'avant
- L'envie d'apprendre quelque chose de nouveau rapidement
- Des nouvelles ou des contacts qui te poussent à agir

## Conseils pour ce transit
- Exprime tes idées sans attendre le moment parfait
- Initie une conversation importante que tu repoussais
- Reste ouvert aux échanges même si tu es sûr de toi""",

    ('aries', 4): """# ☉ Transit du Soleil en Bélier

**En une phrase :** Ton foyer a besoin d'action — c'est le moment de dynamiser ta vie privée.

## L'énergie du moment
Le Soleil en Bélier traverse ta Maison 4 du foyer et des racines. Tu peux ressentir l'envie de faire des changements chez toi, de prendre des initiatives familiales ou de réaffirmer ton territoire personnel. L'énergie peut être intense à la maison.

## Ce que tu pourrais vivre
- Un besoin de réorganiser ou de rafraîchir ton espace de vie
- Des discussions animées avec la famille ou les colocataires
- L'envie de t'affirmer dans ta sphère privée

## Conseils pour ce transit
- Canalise ton énergie dans des projets domestiques concrets
- Évite les conflits familiaux en choisissant tes batailles
- Accorde-toi des moments de calme malgré l'agitation""",

    ('aries', 5): """# ☉ Transit du Soleil en Bélier

**En une phrase :** La créativité et la joie de vivre t'appellent — ose t'exprimer et t'amuser.

## L'énergie du moment
Le Soleil en Bélier illumine ta Maison 5 de la créativité, des plaisirs et de l'amour. Tu as envie de te faire plaisir, de créer, de séduire, de jouer. L'énergie est ludique mais aussi compétitive — tu veux briller et être reconnu.

## Ce que tu pourrais vivre
- Un élan créatif à saisir immédiatement
- Des rencontres amoureuses passionnées ou des moments intenses en couple
- L'envie de prendre des risques pour le plaisir

## Conseils pour ce transit
- Lance-toi dans un projet créatif sans trop réfléchir
- Profite des moments de joie sans culpabilité
- En amour, ose faire le premier pas""",

    ('aries', 6): """# ☉ Transit du Soleil en Bélier

**En une phrase :** Ton quotidien a besoin d'un coup de fouet — c'est le moment d'améliorer tes routines.

## L'énergie du moment
Le Soleil en Bélier traverse ta Maison 6 du travail quotidien et de la santé. Tu as l'énergie pour attaquer tes tâches avec vigueur, améliorer ton hygiène de vie ou lancer de nouvelles routines. La productivité peut être au maximum.

## Ce que tu pourrais vivre
- Un regain de motivation pour accomplir tes tâches
- L'envie de commencer un nouveau programme sportif ou alimentaire
- Des initiatives au travail qui te permettent de te démarquer

## Conseils pour ce transit
- Profite de cette énergie pour tacler les tâches que tu repoussais
- Commence une nouvelle routine santé
- Évite le surmenage malgré ton enthousiasme""",

    ('aries', 7): """# ☉ Transit du Soleil en Bélier

**En une phrase :** Tes relations sont sous les projecteurs — affirme-toi tout en restant à l'écoute.

## L'énergie du moment
Le Soleil en Bélier illumine ta Maison 7 des partenariats et des relations. Tu peux avoir besoin de clarifier ta position dans tes relations ou de prendre des initiatives avec un partenaire. L'équilibre entre indépendance et compromis est au cœur de ce transit.

## Ce que tu pourrais vivre
- Des discussions franches avec ton partenaire ou un associé
- L'envie de redéfinir les termes d'une relation
- Des rencontres avec des personnes dynamiques et directes

## Conseils pour ce transit
- Exprime clairement tes besoins dans tes relations
- Écoute aussi le point de vue de l'autre avant de trancher
- Profite de cette énergie pour avancer ensemble sur un projet""",

    ('aries', 8): """# ☉ Transit du Soleil en Bélier

**En une phrase :** L'heure est aux transformations profondes — affronte ce qui doit changer.

## L'énergie du moment
Le Soleil en Bélier traverse ta Maison 8 des transformations et des ressources partagées. Ce transit te pousse à regarder en face les zones de ta vie qui ont besoin d'un renouveau radical. Les questions d'argent partagé peuvent aussi être au premier plan.

## Ce que tu pourrais vivre
- Un besoin de faire le ménage dans ta vie (relations, finances, émotions)
- Des révélations ou des prises de conscience profondes
- L'envie de t'attaquer à un tabou ou un sujet délicat

## Conseils pour ce transit
- Affronte avec courage ce que tu évitais
- Clarifie les situations financières partagées
- Accepte que certaines choses doivent mourir pour renaître""",

    ('aries', 9): """# ☉ Transit du Soleil en Bélier

**En une phrase :** L'aventure t'appelle — élargis tes horizons avec audace.

## L'énergie du moment
Le Soleil en Bélier illumine ta Maison 9 des voyages, des études et de la philosophie. Tu as soif d'ailleurs, de nouvelles perspectives, d'expansion. C'est le moment de sortir de ta zone de confort intellectuelle ou géographique.

## Ce que tu pourrais vivre
- L'envie de voyager ou de planifier une aventure
- Un intérêt soudain pour un nouveau domaine d'études
- Des discussions passionnées sur des sujets de fond

## Conseils pour ce transit
- Planifie un voyage ou une exploration même modeste
- Ose défendre tes convictions
- Inscris-toi à une formation qui t'attire depuis longtemps""",

    ('aries', 10): """# ☉ Transit du Soleil en Bélier

**En une phrase :** Ta carrière est en ébullition — c'est le moment de viser haut et d'agir.

## L'énergie du moment
Le Soleil en Bélier traverse ta Maison 10 de la carrière et de la réputation. Tu es visible, tes actions professionnelles sont remarquées. C'est le moment de prendre des initiatives audacieuses pour ta carrière et de montrer de quoi tu es capable.

## Ce que tu pourrais vivre
- Des opportunités professionnelles qui demandent de l'audace
- Une reconnaissance de tes efforts ou de tes initiatives
- L'envie de redéfinir tes objectifs de carrière

## Conseils pour ce transit
- Prends l'initiative sur un projet professionnel important
- Fais-toi remarquer par tes actions, pas seulement tes paroles
- Définis clairement tes ambitions et fais un premier pas""",

    ('aries', 11): """# ☉ Transit du Soleil en Bélier

**En une phrase :** Tes projets collectifs prennent vie — mobilise ton réseau avec enthousiasme.

## L'énergie du moment
Le Soleil en Bélier illumine ta Maison 11 des amitiés et des projets de groupe. Tu as l'énergie pour fédérer les autres autour de tes idées, prendre des initiatives dans un collectif ou renouer avec des amis. L'esprit d'équipe est vivifié.

## Ce que tu pourrais vivre
- Des invitations à rejoindre de nouveaux groupes ou projets
- L'envie de prendre les rênes d'un projet collectif
- Des discussions stimulantes avec des amis partageant tes idéaux

## Conseils pour ce transit
- Propose tes idées à ton réseau sans hésiter
- Rejoins un groupe ou une association qui te correspond
- Soutiens activement les projets de tes amis""",

    ('aries', 12): """# ☉ Transit du Soleil en Bélier

**En une phrase :** Un temps de retrait actif — prépare en coulisses ta prochaine renaissance.

## L'énergie du moment
Le Soleil en Bélier traverse ta Maison 12 de l'inconscient et du retrait. Cette énergie dynamique dans un secteur introspectif te demande d'agir sur ton monde intérieur. C'est le moment de clore des cycles avant de repartir.

## Ce que tu pourrais vivre
- Un besoin de solitude pour recharger tes batteries
- Des prises de conscience sur des schémas à transformer
- L'envie de méditer, créer ou rêver loin du tumulte

## Conseils pour ce transit
- Accorde-toi du temps seul pour faire le point
- Travaille sur tes peurs ou tes blocages avec courage
- Prépare mentalement tes prochaines initiatives""",

    # TAURUS
    ('taurus', 1): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Tu rayonnes de stabilité — affirme ta présence avec calme et assurance.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Taureau, te donnant une présence solide et rassurante. C'est le moment de te montrer tel que tu es, avec tes qualités de fiabilité et de persévérance. Les autres apprécient ta constance.

## Ce que tu pourrais vivre
- Un regain de confiance en toi et en ton corps
- L'envie de prendre soin de ton apparence ou de ta santé
- Une présence plus affirmée dans tes interactions

## Conseils pour ce transit
- Investis dans ton image de façon durable
- Ancre-toi dans tes valeurs pour te présenter au monde
- Profite de ta stabilité pour rassurer les autres""",

    ('taurus', 2): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Tes ressources sont au centre de ton attention — construis ta sécurité patiemment.

## L'énergie du moment
Le Soleil en Taureau illumine ta Maison 2, amplifiant les thèmes de valeur personnelle et de sécurité matérielle. Tu es naturellement attiré par ce qui est beau, stable et durable. C'est le moment de solidifier tes finances.

## Ce que tu pourrais vivre
- Une clarification de ce qui compte vraiment pour toi
- Des opportunités de revenus liées à tes talents naturels
- L'envie de faire des achats de qualité plutôt que de quantité

## Conseils pour ce transit
- Fais le point sur ton budget avec réalisme
- Investis dans des choses durables
- Reconnais tes talents et trouve comment les monétiser""",

    ('taurus', 3): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Ta communication gagne en profondeur — prends le temps de bien exprimer tes idées.

## L'énergie du moment
Le Soleil en Taureau traverse ta Maison 3 de la communication. Tes échanges sont plus réfléchis, tes mots plus pesés. Tu préfères la qualité à la quantité dans tes conversations. L'apprentissage se fait mieux par la pratique.

## Ce que tu pourrais vivre
- Des conversations approfondies sur des sujets concrets
- L'envie d'apprendre quelque chose de pratique et utile
- Des échanges avec tes proches autour de questions matérielles

## Conseils pour ce transit
- Prends le temps de formuler tes pensées avant de parler
- Apprends par l'expérience plutôt que par la théorie
- Renforce les liens avec tes frères, sœurs ou voisins""",

    ('taurus', 4): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Ton foyer devient un cocon — investis dans le confort de ta maison.

## L'énergie du moment
Le Soleil en Taureau illumine ta Maison 4 du foyer. Tu ressens un besoin profond de confort domestique, de stabilité familiale et de racines solides. C'est le moment de créer un chez-toi qui te ressemble et te ressource.

## Ce que tu pourrais vivre
- L'envie de décorer ou d'améliorer ton intérieur
- Des moments chaleureux en famille ou chez toi
- Un besoin de sécurité émotionnelle et matérielle

## Conseils pour ce transit
- Investis dans ton confort domestique
- Cuisine des bons petits plats pour toi et les tiens
- Crée un espace où tu te sens vraiment en sécurité""",

    ('taurus', 5): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Les plaisirs simples t'appellent — savoure la vie avec tes cinq sens.

## L'énergie du moment
Le Soleil en Taureau traverse ta Maison 5 de la créativité et des plaisirs. Tu es attiré par les joies sensuelles, la beauté, l'art et les plaisirs de la table. L'amour se vit de façon plus tactile et présente.

## Ce que tu pourrais vivre
- Un élan créatif orienté vers l'artisanat ou les arts manuels
- Des moments de plaisir sensoriel (gastronomie, nature, musique)
- Une romance qui se développe lentement mais sûrement

## Conseils pour ce transit
- Offre-toi des plaisirs qui engagent tes sens
- Crée quelque chose de beau et de tangible
- En amour, prends ton temps et savoure chaque étape""",

    ('taurus', 6): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Tes routines se stabilisent — construis des habitudes durables pour ta santé.

## L'énergie du moment
Le Soleil en Taureau illumine ta Maison 6 du quotidien et de la santé. Tu as envie de routines qui fonctionnent vraiment, de méthodes éprouvées et de résultats tangibles. C'est le moment de solidifier tes habitudes de travail et de bien-être.

## Ce que tu pourrais vivre
- Un désir de simplifier et stabiliser ton quotidien
- Des progrès lents mais constants dans ta santé
- Une productivité accrue grâce à des méthodes fiables

## Conseils pour ce transit
- Établis des routines que tu peux maintenir sur le long terme
- Privilégie une alimentation saine et nourrissante
- Au travail, mise sur la qualité plutôt que la vitesse""",

    ('taurus', 7): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Tes relations cherchent la stabilité — construis des partenariats durables.

## L'énergie du moment
Le Soleil en Taureau traverse ta Maison 7 des partenariats. Tu recherches des relations fiables, des engagements solides et des partenaires sur qui tu peux compter. C'est le moment de consolider tes liens les plus importants.

## Ce que tu pourrais vivre
- Un besoin de clarifier l'engagement dans tes relations
- Des moments de partage simple mais profond avec ton partenaire
- L'attirance pour des personnes stables et fiables

## Conseils pour ce transit
- Investis du temps de qualité dans tes relations importantes
- Discute des questions pratiques avec ton partenaire
- Montre ta loyauté par des actes concrets""",

    ('taurus', 8): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Les transformations se font en douceur — accepte les changements à ton rythme.

## L'énergie du moment
Le Soleil en Taureau illumine ta Maison 8 des transformations. Cette énergie stable dans un secteur de mutation peut créer une tension entre ton besoin de sécurité et les changements nécessaires. Les questions financières partagées demandent attention.

## Ce que tu pourrais vivre
- Un besoin de sécuriser tes ressources partagées
- Des transformations qui se font progressivement
- Une résistance aux changements trop brusques

## Conseils pour ce transit
- Accepte les transformations nécessaires mais à ton rythme
- Clarifie les questions d'argent avec tes proches
- Trouve la sécurité même dans le changement""",

    ('taurus', 9): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Ta quête de sens s'ancre dans le réel — cherche la sagesse dans le concret.

## L'énergie du moment
Le Soleil en Taureau traverse ta Maison 9 des voyages et de la philosophie. Tu es attiré par une sagesse pratique, des voyages qui offrent du confort et des apprentissages qui ont une application concrète. L'expansion se fait pas à pas.

## Ce que tu pourrais vivre
- L'envie de voyager pour découvrir de nouvelles saveurs et paysages
- Un intérêt pour des philosophies ancrées dans le quotidien
- Des études ou formations à visée pratique

## Conseils pour ce transit
- Voyage pour le plaisir des sens et la beauté
- Cherche des enseignements que tu peux appliquer
- Prends le temps d'intégrer ce que tu apprends""",

    ('taurus', 10): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Ta carrière demande de la patience — construis ta réputation brique par brique.

## L'énergie du moment
Le Soleil en Taureau illumine ta Maison 10 de la carrière. Tu es visible pour ta fiabilité et ta constance. C'est le moment de consolider ta position professionnelle plutôt que de chercher des changements radicaux. Les résultats viendront.

## Ce que tu pourrais vivre
- Une reconnaissance pour ton travail constant
- Des opportunités qui demandent de la patience
- Un besoin de sécurité professionnelle

## Conseils pour ce transit
- Continue sur ta lancée avec persévérance
- Montre ta valeur par des résultats concrets
- Ne te précipite pas vers de nouvelles opportunités""",

    ('taurus', 11): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Tes amitiés s'approfondissent — cultive des liens durables avec ton réseau.

## L'énergie du moment
Le Soleil en Taureau traverse ta Maison 11 des amitiés et des projets collectifs. Tu préfères les amis de longue date aux nouvelles rencontres, les projets solides aux idées en l'air. C'est le moment de renforcer les liens qui comptent.

## Ce que tu pourrais vivre
- Des moments de partage simple avec tes amis fidèles
- L'envie de contribuer concrètement à un projet de groupe
- Une clarification de tes objectifs à long terme

## Conseils pour ce transit
- Cultive tes amitiés les plus durables
- Apporte une contribution tangible à une cause
- Définis des objectifs réalistes et atteignables""",

    ('taurus', 12): """# ☉ Transit du Soleil en Taureau

**En une phrase :** Le repos t'appelle — accorde-toi du temps pour te ressourcer profondément.

## L'énergie du moment
Le Soleil en Taureau illumine ta Maison 12 du retrait et de l'intériorité. Tu as besoin de calme, de confort et de moments de solitude régénératrice. C'est le temps de prendre soin de toi loin des regards et des obligations.

## Ce que tu pourrais vivre
- Un besoin de cocooning et de repos sensoriel
- Des moments de méditation ou de contemplation
- Une connexion avec ta vie intérieure

## Conseils pour ce transit
- Offre-toi des moments de détente luxuriante
- Médite dans un environnement beau et confortable
- Prépare en douceur la prochaine étape de ton année""",

    # GEMINI
    ('gemini', 1): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Tu pétilles d'idées et de curiosité — montre ta vivacité au monde.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Gémeaux, te rendant plus communicatif, curieux et adaptable. C'est le moment de te présenter sous ton jour le plus vif et intellectuel. Les échanges et les rencontres sont favorisés.

## Ce que tu pourrais vivre
- Un regain de curiosité et d'envie d'apprendre
- Une facilité à communiquer et à te connecter aux autres
- Une image de toi plus légère et dynamique

## Conseils pour ce transit
- Ose engager la conversation avec de nouvelles personnes
- Montre ta polyvalence et ton intelligence
- Évite de te disperser dans trop de directions""",

    ('gemini', 2): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Tes idées ont de la valeur — monétise ta créativité intellectuelle.

## L'énergie du moment
Le Soleil en Gémeaux illumine ta Maison 2 des ressources. Tu peux trouver de nouvelles sources de revenus grâce à tes idées, ta communication ou ta polyvalence. C'est le moment de réfléchir à comment valoriser tes talents intellectuels.

## Ce que tu pourrais vivre
- Des opportunités financières liées à la communication
- Une réflexion sur la diversification de tes revenus
- L'envie de valoriser plusieurs compétences à la fois

## Conseils pour ce transit
- Explore plusieurs pistes pour augmenter tes revenus
- Utilise tes talents de communication pour négocier
- Reste flexible dans ta gestion financière""",

    ('gemini', 3): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Ta parole porte loin — c'est ton moment pour communiquer, apprendre et échanger.

## L'énergie du moment
Le Soleil en Gémeaux amplifie l'énergie de ta Maison 3 de la communication. Tu es particulièrement vif, curieux et bavard. Les idées fusent, les échanges se multiplient, et tu as soif d'informations nouvelles.

## Ce que tu pourrais vivre
- Des conversations passionnantes et stimulantes
- L'envie d'écrire, de bloguer ou de partager tes idées
- Des déplacements courts mais enrichissants

## Conseils pour ce transit
- Partage tes idées à travers l'écriture ou la parole
- Satisfais ta curiosité en explorant de nouveaux sujets
- Renoue avec des frères, sœurs ou voisins""",

    ('gemini', 4): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Ton foyer s'anime — apporte de la légèreté et de la communication chez toi.

## L'énergie du moment
Le Soleil en Gémeaux traverse ta Maison 4 du foyer. L'ambiance à la maison est plus légère, les conversations plus animées. Tu peux avoir envie de réorganiser ton espace ou d'inviter des gens chez toi.

## Ce que tu pourrais vivre
- Des discussions animées en famille
- L'envie de réaménager ou de rafraîchir ton intérieur
- Un besoin de variété dans ta vie domestique

## Conseils pour ce transit
- Apporte de la nouveauté dans ton quotidien à la maison
- Discute ouvertement avec ta famille
- Travaille de chez toi si tu le peux""",

    ('gemini', 5): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** La créativité mentale t'inspire — joue avec les mots et les idées.

## L'énergie du moment
Le Soleil en Gémeaux illumine ta Maison 5 de la créativité et des plaisirs. Tu es attiré par les jeux de l'esprit, les échanges flirtatifs et les activités ludiques intellectuelles. L'amour passe par la conversation.

## Ce que tu pourrais vivre
- Un élan créatif orienté vers l'écriture ou les jeux de mots
- Des flirts basés sur l'humour et l'intelligence
- L'envie de t'amuser à travers des activités intellectuelles

## Conseils pour ce transit
- Exprime ta créativité à travers les mots
- Séduis par ton esprit et ton humour
- Amuse-toi à apprendre ou à jouer à des jeux de société""",

    ('gemini', 6): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Ton quotidien gagne en variété — adapte tes routines avec flexibilité.

## L'énergie du moment
Le Soleil en Gémeaux traverse ta Maison 6 du travail et de la santé. Tu as besoin de variété dans ton quotidien, de tâches diversifiées et de flexibilité dans tes routines. La monotonie te pèse particulièrement.

## Ce que tu pourrais vivre
- Un quotidien plus varié et stimulant
- L'envie d'optimiser tes méthodes de travail
- Des informations importantes sur ta santé

## Conseils pour ce transit
- Varie tes tâches pour éviter l'ennui
- Informe-toi sur des méthodes pour améliorer ta santé
- Communique davantage avec tes collègues""",

    ('gemini', 7): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Tes relations passent par le dialogue — communique ouvertement avec tes partenaires.

## L'énergie du moment
Le Soleil en Gémeaux illumine ta Maison 7 des partenariats. Les échanges sont au cœur de tes relations. Tu recherches des partenaires avec qui tu peux discuter, débattre et apprendre. La communication est la clé.

## Ce que tu pourrais vivre
- Des discussions importantes avec ton partenaire
- L'attirance pour des personnes vives et communicatives
- Le besoin de variété et de stimulation dans tes relations

## Conseils pour ce transit
- Parle ouvertement de ce que tu ressens
- Cherche des activités intellectuelles à partager
- Écoute autant que tu parles""",

    ('gemini', 8): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Les questions profondes t'intriguent — explore les mystères avec curiosité.

## L'énergie du moment
Le Soleil en Gémeaux traverse ta Maison 8 des transformations. Tu abordes les sujets profonds avec curiosité intellectuelle plutôt qu'émotionnelle. C'est le moment de chercher à comprendre les mécanismes cachés.

## Ce que tu pourrais vivre
- Un intérêt pour les sujets tabous ou mystérieux
- Des conversations profondes mais légères à la fois
- Des informations importantes sur des ressources partagées

## Conseils pour ce transit
- Informe-toi sur les questions financières communes
- Explore tes zones d'ombre avec curiosité
- Communique sur les sujets délicats""",

    ('gemini', 9): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Ta soif de savoir s'amplifie — explore toutes les directions qui t'attirent.

## L'énergie du moment
Le Soleil en Gémeaux illumine ta Maison 9 des voyages et de la connaissance. Tu veux tout savoir, tout explorer, tout comprendre. Les voyages courts sont favorisés, de même que les études variées.

## Ce que tu pourrais vivre
- Une curiosité insatiable pour de nouveaux domaines
- Des voyages ou déplacements stimulants intellectuellement
- Des échanges avec des personnes d'horizons différents

## Conseils pour ce transit
- Explore plusieurs sujets plutôt qu'un seul en profondeur
- Voyage léger et découvre de nouveaux lieux
- Échange avec des gens de cultures différentes""",

    ('gemini', 10): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Tes talents de communication brillent — fais-toi remarquer par tes idées.

## L'énergie du moment
Le Soleil en Gémeaux traverse ta Maison 10 de la carrière. Tu es visible pour ta vivacité d'esprit, ta polyvalence et tes compétences en communication. C'est le moment de présenter tes idées et de networker.

## Ce que tu pourrais vivre
- Des opportunités liées à la communication ou aux médias
- Une reconnaissance de ta polyvalence professionnelle
- Des échanges importants avec des personnes influentes

## Conseils pour ce transit
- Présente tes idées aux bonnes personnes
- Développe ton réseau professionnel
- Montre ta capacité à gérer plusieurs projets""",

    ('gemini', 11): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Ton réseau s'active — multiplie les connexions et les échanges d'idées.

## L'énergie du moment
Le Soleil en Gémeaux illumine ta Maison 11 des amitiés et des projets de groupe. C'est le moment idéal pour socialiser, échanger des idées et participer à des projets collectifs stimulants intellectuellement.

## Ce que tu pourrais vivre
- Des rencontres avec des personnes intéressantes
- Des projets de groupe basés sur l'échange d'idées
- Une vie sociale particulièrement active

## Conseils pour ce transit
- Participe à des événements de networking
- Rejoins des groupes de discussion ou d'apprentissage
- Partage tes idées pour l'avenir avec tes amis""",

    ('gemini', 12): """# ☉ Transit du Soleil en Gémeaux

**En une phrase :** Ton esprit vagabonde — laisse tes pensées explorer ton monde intérieur.

## L'énergie du moment
Le Soleil en Gémeaux traverse ta Maison 12 de l'intériorité. Ton mental peut être très actif même dans les moments de repos. C'est le temps de journaliser, méditer ou explorer tes pensées inconscientes.

## Ce que tu pourrais vivre
- Un flux de pensées difficile à calmer
- Des intuitions qui arrivent par fragments
- L'envie d'écrire un journal intime

## Conseils pour ce transit
- Journalise pour clarifier tes pensées
- Médite pour calmer le mental
- Explore tes rêves et tes intuitions""",

    # CANCER
    ('cancer', 1): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Ta sensibilité devient ta force — montre au monde ta douceur et ta profondeur.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Cancer, te rendant plus sensible, intuitif et protecteur. C'est le moment de t'affirmer avec ton cœur, de montrer ton côté nurturing et de créer des connexions émotionnelles.

## Ce que tu pourrais vivre
- Une sensibilité accrue aux ambiances et aux émotions
- Un besoin de te sentir en sécurité pour t'exprimer
- Une image de toi plus douce et accueillante

## Conseils pour ce transit
- Assume ta sensibilité comme une qualité
- Prends soin de toi comme tu prendrais soin d'un proche
- Montre ta capacité à accueillir et à écouter""",

    ('cancer', 2): """# ☉ Transit du Soleil en Cancer

**En une phrase :** La sécurité matérielle t'appelle — construis un nid financier confortable.

## L'énergie du moment
Le Soleil en Cancer illumine ta Maison 2 des ressources. Tu ressens un besoin profond de sécurité financière et émotionnelle. C'est le moment de prendre soin de tes finances comme tu prendrais soin de ta famille.

## Ce que tu pourrais vivre
- Un besoin de sécuriser tes revenus
- L'envie d'investir dans ton foyer ou ta famille
- Une clarification de ce qui te fait te sentir en sécurité

## Conseils pour ce transit
- Épargne pour te sentir plus en sécurité
- Investis dans ce qui nourrit ton bien-être
- Écoute ton intuition pour les décisions financières""",

    ('cancer', 3): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Ta communication se teinte d'émotion — exprime tes sentiments avec tes proches.

## L'énergie du moment
Le Soleil en Cancer traverse ta Maison 3 de la communication. Tes échanges sont plus émotionnels, plus personnels. Tu as besoin de conversations qui viennent du cœur et de liens authentiques avec ton entourage proche.

## Ce que tu pourrais vivre
- Des conversations intimes avec tes proches
- L'envie de renouer avec ta famille proche
- Une communication plus intuitive qu'intellectuelle

## Conseils pour ce transit
- Appelle les membres de ta famille pour prendre des nouvelles
- Exprime tes émotions dans tes conversations
- Écoute ton intuition dans tes échanges""",

    ('cancer', 4): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Ton foyer est au centre de tout — ressource-toi dans ton cocon.

## L'énergie du moment
Le Soleil en Cancer illumine puissamment ta Maison 4 du foyer. C'est le moment de te recentrer sur ta vie privée, ta famille et ton chez-toi. Tu as besoin de racines solides et d'un sanctuaire où te ressourcer.

## Ce que tu pourrais vivre
- Un besoin intense de rentrer chez toi et de t'y sentir bien
- Des moments forts en famille
- L'envie de créer un nid douillet et sécurisant

## Conseils pour ce transit
- Passe du temps de qualité en famille
- Améliore le confort de ton intérieur
- Ressource-toi dans ton cocon avant d'affronter le monde""",

    ('cancer', 5): """# ☉ Transit du Soleil en Cancer

**En une phrase :** L'amour prend des teintes protectrices — aime et crée avec ton cœur.

## L'énergie du moment
Le Soleil en Cancer traverse ta Maison 5 de la créativité et de l'amour. Tu as envie d'aimer de façon protectrice, de créer quelque chose qui vient de ton cœur et de t'occuper de ceux que tu aimes.

## Ce que tu pourrais vivre
- Une créativité nourrie par tes émotions
- Des moments tendres en amour ou avec des enfants
- L'envie de prendre soin de tes proches

## Conseils pour ce transit
- Crée quelque chose qui exprime tes émotions
- En amour, montre ta tendresse et ta protection
- Passe du temps avec des enfants ou ton enfant intérieur""",

    ('cancer', 6): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Ton quotidien a besoin de douceur — prends soin de ta santé et de ton rythme.

## L'énergie du moment
Le Soleil en Cancer illumine ta Maison 6 du travail et de la santé. Tu as besoin d'un environnement de travail chaleureux et d'une routine qui respecte tes émotions. Ta santé est liée à ton équilibre émotionnel.

## Ce que tu pourrais vivre
- Un besoin de confort dans ton environnement de travail
- Une attention particulière à ton alimentation et ta digestion
- L'envie de prendre soin des autres au travail

## Conseils pour ce transit
- Créé une ambiance chaleureuse dans ton espace de travail
- Mange des repas faits maison et nourrissants
- Écoute tes émotions pour préserver ta santé""",

    ('cancer', 7): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Tes relations cherchent la tendresse — cultive des liens qui te sécurisent.

## L'énergie du moment
Le Soleil en Cancer traverse ta Maison 7 des partenariats. Tu recherches des relations où tu te sens en sécurité, protégé et compris émotionnellement. C'est le moment de nourrir tes partenariats avec tendresse.

## Ce que tu pourrais vivre
- Un besoin de sécurité et de fidélité dans tes relations
- Des moments de partage émotionnel profond
- L'attirance pour des personnes protectrices ou nurturing

## Conseils pour ce transit
- Exprime tes besoins émotionnels à ton partenaire
- Crée des rituels intimes avec ceux que tu aimes
- Montre ta capacité à prendre soin de l'autre""",

    ('cancer', 8): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Les transformations touchent tes émotions — laisse le passé se transformer.

## L'énergie du moment
Le Soleil en Cancer illumine ta Maison 8 des transformations. Les changements profonds sont liés à ton histoire familiale, à tes attachements émotionnels. C'est le moment de guérir les blessures du passé.

## Ce que tu pourrais vivre
- Des émotions intenses liées à ton passé ou ta famille
- Un besoin de sécurité face aux changements
- Des révélations sur tes schémas émotionnels

## Conseils pour ce transit
- Permets-toi de pleurer ce qui doit partir
- Explore tes mémoires familiales avec douceur
- Cherche la sécurité intérieure plutôt qu'extérieure""",

    ('cancer', 9): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Ta quête de sens se teinte d'émotion — voyage vers tes racines.

## L'énergie du moment
Le Soleil en Cancer traverse ta Maison 9 des voyages et de la philosophie. Tu es attiré par les voyages qui te ramènent à tes origines, les philosophies du cœur et les sagesses ancestrales.

## Ce que tu pourrais vivre
- L'envie de visiter les lieux de tes ancêtres
- Un intérêt pour les traditions familiales ou culturelles
- Des apprentissages qui parlent à ton cœur

## Conseils pour ce transit
- Explore ton arbre généalogique ou ton histoire familiale
- Voyage vers des lieux chargés d'émotion
- Cherche une sagesse qui résonne avec ton cœur""",

    ('cancer', 10): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Ta carrière s'humanise — brille par ton empathie et ta bienveillance.

## L'énergie du moment
Le Soleil en Cancer illumine ta Maison 10 de la carrière. Tu es reconnu pour tes qualités humaines, ta capacité à prendre soin des autres et ton intuition. C'est le moment de montrer ton côté nurturing au travail.

## Ce que tu pourrais vivre
- Une reconnaissance pour ta bienveillance professionnelle
- Des opportunités dans les domaines du care ou de l'accompagnement
- Un besoin de sécurité dans ta carrière

## Conseils pour ce transit
- Montre ton côté humain au travail
- Utilise ton intuition pour prendre des décisions
- Cherche un travail qui a du sens pour toi""",

    ('cancer', 11): """# ☉ Transit du Soleil en Cancer

**En une phrase :** Tes amitiés deviennent famille — cultive des liens profonds avec ton cercle.

## L'énergie du moment
Le Soleil en Cancer traverse ta Maison 11 des amitiés. Tu recherches des amitiés qui ressemblent à de la famille, des groupes où tu te sens appartenir et en sécurité. C'est le moment de créer une tribu bienveillante.

## Ce que tu pourrais vivre
- Des moments chaleureux avec tes amis proches
- L'envie de recevoir chez toi et de nourrir les autres
- Des projets collectifs orientés vers le bien-être commun

## Conseils pour ce transit
- Invite tes amis pour un repas fait maison
- Rejoins des groupes qui partagent tes valeurs profondes
- Prends soin de tes amis comme de ta famille""",

    ('cancer', 12): """# ☉ Transit du Soleil en Cancer

**En une phrase :** L'introspection t'appelle — plonge dans tes profondeurs émotionnelles.

## L'énergie du moment
Le Soleil en Cancer illumine ta Maison 12 de l'intériorité. C'est un temps de retrait émotionnel, de connexion avec ton inconscient et de guérison des vieilles blessures. Tes rêves peuvent être particulièrement révélateurs.

## Ce que tu pourrais vivre
- Un besoin de solitude et de protection
- Des émotions du passé qui remontent
- Une sensibilité accrue à l'invisible et à l'intuitif

## Conseils pour ce transit
- Accorde-toi du temps seul pour te ressourcer
- Journalise tes rêves et tes émotions
- Prends soin de toi avec une tendresse maternelle""",
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
