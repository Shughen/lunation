#!/usr/bin/env python3
"""Insert transit_venus interpretations for Sagittarius, Capricorn, Aquarius, Pisces (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_VENUS_INTERPRETATIONS = {
    # ============== SAGITTARIUS ==============
    ('sagittarius', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme aventurier s'enflamme et tu rayonnes d'une joie contagieuse.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ton magnétisme naturel avec une énergie de feu! Tu dégages une aura chaleureuse et enthousiaste qui attire naturellement les autres. C'est le moment parfait pour renouveler ton style avec audace et montrer ta personnalité unique.

## Ce que tu pourrais vivre
- Un charisme amplifié
- Des rencontres spontanées
- L'envie de te réinventer avec audace

## Conseils pour ce transit
- Laisse ton enthousiasme briller
- Ose les changements de style
- Séduis par ta joie de vivre""",

    ('sagittarius', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et plaisirs matériels sont dynamisés par la chance.

## L'énergie du moment
Vénus visite ta maison II, stimulant ton rapport à l'argent avec optimisme. Tu pourrais recevoir des gains inattendus ou être tenté(e) par des achats aventuriers. C'est aussi le moment de reconnaître ta valeur et d'investir dans tes rêves.

## Ce que tu pourrais vivre
- Une amélioration financière chanceuse
- Des achats qui élargissent tes horizons
- Une confiance en ta valeur

## Conseils pour ce transit
- Investis dans tes aventures
- Valorise ton optimisme naturel
- Fais-toi plaisir généreusement""",

    ('sagittarius', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient enthousiasmante et tes échanges inspirants.

## L'énergie du moment
Vénus adoucit ta maison III, rendant tes mots plus séduisants et tes idées plus attrayantes. Les conversations deviennent des aventures intellectuelles. C'est excellent pour partager tes connaissances et inspirer les autres.

## Ce que tu pourrais vivre
- Des dialogues passionnants
- Un rapprochement avec ton entourage
- Du succès dans la transmission

## Conseils pour ce transit
- Partage ton enthousiasme
- Explore ton environnement avec curiosité
- Inspire les autres par tes mots""",

    ('sagittarius', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient une base chaleureuse pour tes aventures.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant chaleur et joie à ta vie domestique. Tu as envie de rendre ton chez-toi plus accueillant, peut-être avec des touches exotiques. Les liens familiaux bénéficient de ton optimisme.

## Ce que tu pourrais vivre
- L'envie de décorer avec des souvenirs de voyage
- Des moments joyeux en famille
- Un sentiment de liberté chez toi

## Conseils pour ce transit
- Crée un chez-toi inspirant
- Partage des repas conviviaux
- Cultive la joie familiale""",

    ('sagittarius', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et la créativité explosent dans une aventure passionnante!

## L'énergie du moment
Vénus brille dans ta maison V, promettant romance aventureuse et créativité débridée. C'est LA période pour les coups de foudre, les escapades romantiques et l'expression artistique sans limites. Les plaisirs de la vie sont à savourer pleinement!

## Ce que tu pourrais vivre
- Un amour aventurier et passionné
- Une créativité sans limites
- Des moments de bonheur intense

## Conseils pour ce transit
- Lance-toi dans l'aventure amoureuse
- Exprime ta créativité librement
- Vis chaque plaisir comme une fête""",

    ('sagittarius', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien devient une aventure et tes routines plus stimulantes.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant le travail avec une touche d'aventure. Tu as besoin de variété dans tes routines et tu apportes de l'enthousiasme à tes tâches. C'est aussi un bon moment pour des activités physiques plaisantes.

## Ce que tu pourrais vivre
- Un travail plus stimulant
- L'envie de routines actives
- Du plaisir dans la diversité

## Conseils pour ce transit
- Varie tes routines quotidiennes
- Adopte des habitudes sportives
- Apporte de l'enthousiasme au travail""",

    ('sagittarius', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les partenariats s'enflamment avec passion et aventure!

## L'énergie du moment
Vénus illumine ta maison VII, favorisant les relations passionnantes et aventureuses. Si tu es en couple, l'envie de nouvelles expériences à deux se fait sentir. Si tu es célibataire, une rencontre excitante peut arriver. Les partenariats sont dynamisés.

## Ce que tu pourrais vivre
- Un amour aventurier
- Une rencontre inspirante
- Des collaborations enthousiasmantes

## Conseils pour ce transit
- Explore de nouvelles choses en couple
- Sois ouvert(e) aux rencontres
- Cultive les partenariats stimulants""",

    ('sagittarius', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité profonde et les expériences intenses t'appellent.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs et ta quête de profondeur. La sexualité et l'intimité émotionnelle deviennent des aventures transformatrices. Les questions de finances partagées peuvent aussi se clarifier.

## Ce que tu pourrais vivre
- Une intimité passionnée
- Des questions financières résolues
- Une transformation par l'amour

## Conseils pour ce transit
- Explore l'intimité avec audace
- Règle les questions d'argent partagé
- Accepte d'être transformé(e)""",

    ('sagittarius', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs et les grands espaces t'appellent avec une force irrésistible!

## L'énergie du moment
Vénus voyage dans ta maison IX, ta maison naturelle! C'est une période bénie pour les voyages, les études supérieures et l'exploration philosophique. L'amour peut venir de loin ou être lié à une aventure. Tout ce qui élargit tes horizons te séduit.

## Ce que tu pourrais vivre
- Un voyage transformateur
- Une romance avec quelqu'un de différent
- Un éveil spirituel ou philosophique

## Conseils pour ce transit
- Pars à l'aventure!
- Ouvre-toi à d'autres cultures
- Explore de nouvelles croyances""",

    ('sagittarius', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme et ton optimisme brillent dans ta carrière.

## L'énergie du moment
Vénus éclaire ta maison X, apportant grâce et enthousiasme à ton image professionnelle. Tu es perçu(e) comme inspirant(e) et charismatique. C'est excellent pour les présentations, les projets internationaux et ta réputation.

## Ce que tu pourrais vivre
- Une reconnaissance professionnelle
- Des opportunités à l'étranger
- Un projet inspirant valorisé

## Conseils pour ce transit
- Brille avec enthousiasme au travail
- Vise des objectifs ambitieux
- Montre ta vision inspirante""",

    ('sagittarius', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés s'élargissent et ton réseau devient international.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale particulièrement enrichissante. Les amitiés se diversifient et tu attires des personnes d'horizons variés. C'est le moment de rejoindre des groupes qui partagent ta soif d'aventure.

## Ce que tu pourrais vivre
- Des amitiés internationales
- Un réseau inspirant
- L'envie de causes humanitaires

## Conseils pour ce transit
- Élargis ton cercle social
- Connecte-toi avec des visionnaires
- Engage-toi pour de grandes causes""",

    ('sagittarius', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur spirituelle t'enveloppe, invitant à l'exploration intérieure.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour plus spirituelle et universelle. Tu pourrais vivre une attirance mystique ou simplement savourer des moments de méditation. C'est un temps de quête intérieure.

## Ce que tu pourrais vivre
- Une romance spirituelle
- Un besoin de retraite méditative
- Une guérison par la foi

## Conseils pour ce transit
- Explore ta spiritualité avec joie
- Accorde-toi des moments contemplatifs
- Trouve la beauté dans le mystère""",

    # ============== CAPRICORN ==============
    ('capricorn', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme discret s'affirme avec une audace nouvelle.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ton magnétisme avec une énergie plus dynamique que d'habitude. Tu dégages une assurance qui attire l'attention et le respect. C'est le moment de te montrer sous un jour plus audacieux.

## Ce que tu pourrais vivre
- Un charisme renforcé
- Des opportunités par ton image
- L'envie de moderniser ton style

## Conseils pour ce transit
- Ose te mettre en valeur
- Montre ta confiance naturelle
- Accepte les compliments avec grâce""",

    ('capricorn', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et tes valeurs sont dynamisées par des opportunités.

## L'énergie du moment
Vénus visite ta maison II, stimulant ton rapport à l'argent avec une énergie favorable. Tu pourrais recevoir des gains mérités ou être tenté(e) par des investissements de qualité. C'est le moment de reconnaître ta valeur professionnelle.

## Ce que tu pourrais vivre
- Une amélioration financière méritée
- Des achats stratégiques
- Une meilleure estime de tes compétences

## Conseils pour ce transit
- Investis judicieusement
- Valorise ton expertise
- Récompense-toi pour ton travail""",

    ('capricorn', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient plus charmante et tes échanges plus productifs.

## L'énergie du moment
Vénus adoucit ta maison III, rendant tes mots plus persuasifs et agréables. Les conversations d'affaires deviennent plus fluides. C'est excellent pour les négociations, les contrats et les échanges professionnels.

## Ce que tu pourrais vivre
- Des dialogues fructueux
- Un rapprochement professionnel
- Du succès dans les négociations

## Conseils pour ce transit
- Utilise ta diplomatie naturelle
- Communique avec charme
- Concrétise par l'écrit""",

    ('capricorn', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un havre de stabilité et de beauté classique.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant harmonie et qualité à ta vie domestique. Tu as envie d'investir dans ton chez-toi, de créer un espace digne de ton ambition. Les liens familiaux peuvent se solidifier.

## Ce que tu pourrais vivre
- L'envie d'améliorer ton habitat
- Des traditions familiales appréciées
- Un sentiment de sécurité renforcé

## Conseils pour ce transit
- Investis dans la qualité de ton foyer
- Honore les traditions familiales
- Crée des fondations solides""",

    ('capricorn', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les plaisirs arrivent comme des récompenses méritées.

## L'énergie du moment
Vénus brille dans ta maison V, t'offrant romance et moments de joie. C'est une période pour te détendre et profiter des plaisirs de la vie – tu le mérites! Les romances peuvent être plus sérieuses que frivoles, et ta créativité trouve des applications concrètes.

## Ce que tu pourrais vivre
- Un amour sérieux et stable
- Une créativité productive
- Des moments de détente méritée

## Conseils pour ce transit
- Autorise-toi à profiter
- Exprime ta créativité concrètement
- Ouvre-toi à l'amour sincère""",

    ('capricorn', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien s'améliore et ton travail devient plus satisfaisant.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant le travail et les responsabilités quotidiennes. L'ambiance professionnelle s'améliore et tu trouves plus de satisfaction dans tes tâches. C'est aussi un bon moment pour prendre soin de ta santé.

## Ce que tu pourrais vivre
- Une meilleure ambiance au travail
- Des routines plus efficaces et agréables
- Du plaisir dans l'accomplissement

## Conseils pour ce transit
- Améliore ton environnement de travail
- Adopte des habitudes saines
- Sois apprécié(e) de tes collègues""",

    ('capricorn', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les partenariats s'officialisent et se renforcent.

## L'énergie du moment
Vénus illumine ta maison VII, favorisant les relations sérieuses et les engagements. Si tu es en couple, c'est un moment pour solidifier vos liens. Si tu es célibataire, une rencontre avec un potentiel durable peut se produire. Les partenariats professionnels prospèrent.

## Ce que tu pourrais vivre
- Un engagement amoureux renforcé
- Une rencontre sérieuse
- Des partenariats solides

## Conseils pour ce transit
- Investis dans tes engagements
- Sois ouvert(e) aux relations durables
- Construis des partenariats fiables""",

    ('capricorn', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité et les finances partagées demandent ton attention.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant ta vie intime et les questions de ressources partagées. La sexualité et l'intimité émotionnelle peuvent apporter une transformation. Les investissements et héritages sont aussi favorisés.

## Ce que tu pourrais vivre
- Une intimité approfondie
- Des questions financières clarifiées
- Une transformation par les liens

## Conseils pour ce transit
- Approfondis tes liens intimes
- Gère les finances partagées sagement
- Accepte les transformations""",

    ('capricorn', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs et les connaissances supérieures t'attirent avec force.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ton intérêt pour les horizons lointains et les études supérieures. Voyages professionnels, formations ou philosophies structurées t'attirent. Une romance avec quelqu'un de différent est possible.

## Ce que tu pourrais vivre
- Un voyage professionnel enrichissant
- Une formation qui t'élève
- Un éveil à d'autres cultures

## Conseils pour ce transit
- Investis dans ta formation
- Ouvre-toi à d'autres perspectives
- Explore avec méthode""",

    ('capricorn', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme et ton professionnalisme brillent au sommet!

## L'énergie du moment
Vénus éclaire ta maison X, ta maison naturelle! C'est une période exceptionnelle pour ta carrière et ton image publique. Tu es perçu(e) comme particulièrement compétent(e) et attractif(ve). C'est excellent pour les promotions et la reconnaissance.

## Ce que tu pourrais vivre
- Une reconnaissance au sommet
- Des opportunités de carrière
- Un prestige renforcé

## Conseils pour ce transit
- Brille dans ta carrière
- Soigne ton image publique
- Vise l'excellence""",

    ('capricorn', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés se consolident et ton réseau devient stratégique.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale plus utile et agréable. Les amitiés avec des personnes influentes se renforcent. C'est le moment de cultiver un réseau qui soutient tes ambitions.

## Ce que tu pourrais vivre
- Des amitiés influentes
- Un réseau stratégique
- L'envie de causes durables

## Conseils pour ce transit
- Cultive des amitiés de qualité
- Connecte-toi avec des personnes clés
- Engage-toi pour des causes structurantes""",

    ('capricorn', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'invite à la contemplation et au repos mérité.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour plus discrète et intérieure. Tu pourrais vivre une attirance cachée ou simplement apprécier des moments de solitude productive. C'est un temps de ressourcement.

## Ce que tu pourrais vivre
- Une romance discrète
- Un besoin de repos mérité
- Une guérison silencieuse

## Conseils pour ce transit
- Accorde-toi du repos
- Explore ta vie intérieure
- Prépare discrètement l'avenir""",

    # ============== AQUARIUS ==============
    ('aquarius', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme original devient plus magnétique et audacieux.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ton magnétisme unique avec une énergie de feu. Tu dégages une aura originale et attractive qui intrigue les autres. C'est le moment de renouveler ton style avec créativité et d'affirmer ta singularité.

## Ce que tu pourrais vivre
- Un charisme amplifié
- Des rencontres inhabituelles
- L'envie d'un style unique

## Conseils pour ce transit
- Affirme ton originalité
- Ose les looks créatifs
- Séduis par ta différence""",

    ('aquarius', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et valeurs sont dynamisées par des idées innovantes.

## L'énergie du moment
Vénus visite ta maison II, stimulant ton rapport à l'argent de façon originale. Tu pourrais recevoir des gains inattendus ou être attiré(e) par des investissements innovants. C'est aussi le moment de valoriser tes talents uniques.

## Ce que tu pourrais vivre
- Des opportunités financières originales
- Des achats technologiques ou futuristes
- Une valorisation de ton unicité

## Conseils pour ce transit
- Explore des sources de revenus innovantes
- Valorise tes idées originales
- Investis dans le futur""",

    ('aquarius', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient plus attrayante et tes idées plus séduisantes.

## L'énergie du moment
Vénus adoucit ta maison III, rendant tes échanges plus agréables et tes idées plus captivantes. Les conversations sur des sujets innovants te passionnent. C'est excellent pour partager tes visions et connecter avec des esprits similaires.

## Ce que tu pourrais vivre
- Des dialogues stimulants
- Un rapprochement avec des penseurs
- Du succès dans le partage d'idées

## Conseils pour ce transit
- Partage tes visions innovantes
- Explore de nouveaux réseaux
- Connecte-toi intellectuellement""",

    ('aquarius', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un laboratoire de vie et d'expérimentation.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant une touche originale à ta vie domestique. Tu as envie de moderniser ton chez-toi, d'introduire des technologies ou des concepts innovants. Les liens familiaux peuvent évoluer.

## Ce que tu pourrais vivre
- L'envie d'un habitat moderne
- Des dynamiques familiales nouvelles
- Un sentiment de liberté chez toi

## Conseils pour ce transit
- Modernise ton espace de vie
- Réinvente les traditions familiales
- Crée un chez-toi qui te ressemble""",

    ('aquarius', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et la créativité explosent de façon inattendue!

## L'énergie du moment
Vénus brille dans ta maison V, promettant romance originale et créativité débridée. Les coups de foudre arrivent de façon inattendue, souvent avec des personnes atypiques. Ta créativité s'exprime de façon avant-gardiste et les plaisirs sont savourés différemment.

## Ce que tu pourrais vivre
- Un amour original et libre
- Une créativité avant-gardiste
- Des plaisirs inhabituels

## Conseils pour ce transit
- Sois ouvert(e) aux amours atypiques
- Exprime ta créativité unique
- Réinvente ta façon de t'amuser""",

    ('aquarius', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien s'améliore grâce à des méthodes innovantes.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant le travail avec une touche d'innovation. Tu cherches des façons originales d'améliorer tes routines. C'est aussi un bon moment pour des approches alternatives de santé et bien-être.

## Ce que tu pourrais vivre
- Un travail plus stimulant
- Des routines innovantes
- Des méthodes de bien-être alternatives

## Conseils pour ce transit
- Innove dans tes routines
- Explore des approches santé nouvelles
- Apporte de la fraîcheur au travail""",

    ('aquarius', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les partenariats prennent des formes originales.

## L'énergie du moment
Vénus illumine ta maison VII, favorisant les relations non-conventionnelles et les partenariats innovants. Si tu es en couple, l'envie de réinventer la relation se fait sentir. Si tu es célibataire, une rencontre atypique peut arriver.

## Ce que tu pourrais vivre
- Un amour libre et original
- Une rencontre inattendue
- Des collaborations innovantes

## Conseils pour ce transit
- Réinvente ta façon d'aimer
- Sois ouvert(e) aux relations atypiques
- Cultive les partenariats créatifs""",

    ('aquarius', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité et les liens profonds évoluent de façon inattendue.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs de façon originale. La sexualité et l'intimité peuvent explorer de nouveaux territoires. Les questions de finances partagées demandent des solutions innovantes.

## Ce que tu pourrais vivre
- Une intimité expérimentale
- Des questions financières à résoudre créativement
- Une transformation par l'inattendu

## Conseils pour ce transit
- Explore l'intimité différemment
- Trouve des solutions financières innovantes
- Accepte les transformations surprenantes""",

    ('aquarius', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs et les idées nouvelles t'attirent irrésistiblement.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ta soif de connaissances nouvelles et d'horizons différents. Voyages vers des destinations insolites, études avant-gardistes ou philosophies alternatives te séduisent. L'amour peut venir d'ailleurs.

## Ce que tu pourrais vivre
- Un voyage vers l'inconnu
- Une attirance pour le différent
- Un éveil à des idées nouvelles

## Conseils pour ce transit
- Explore des territoires inconnus
- Ouvre-toi à des philosophies nouvelles
- Vis des expériences qui élargissent ta vision""",

    ('aquarius', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton originalité brille dans ta carrière et ta vie publique.

## L'énergie du moment
Vénus éclaire ta maison X, apportant charme et innovation à ton image professionnelle. Tu es perçu(e) comme visionnaire et original(e). C'est excellent pour les projets innovants et ta réputation de pionnier(ère).

## Ce que tu pourrais vivre
- Une reconnaissance de ton originalité
- Des opportunités dans l'innovation
- Un projet futuriste valorisé

## Conseils pour ce transit
- Brille par ton originalité
- Propose des idées avant-gardistes
- Affirme ta vision unique""",

    ('aquarius', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés et ton réseau sont au cœur de ton épanouissement!

## L'énergie du moment
Vénus brille dans ta maison XI, ta maison naturelle! C'est une période exceptionnelle pour ta vie sociale. Les amitiés se multiplient et s'approfondissent avec des personnes qui partagent tes idéaux. Ton réseau devient une source de joie et d'opportunités.

## Ce que tu pourrais vivre
- Des amitiés épanouissantes
- Un réseau inspirant
- L'engagement pour des causes importantes

## Conseils pour ce transit
- Célèbre tes amitiés
- Connecte-toi avec des visionnaires
- Engage-toi pour l'avenir""",

    ('aquarius', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'invite à explorer les profondeurs de ton âme.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour universelle et spirituelle. Tu pourrais vivre une connexion mystique ou simplement apprécier des moments de solitude créative. C'est un temps d'inspiration intérieure.

## Ce que tu pourrais vivre
- Une romance spirituelle ou secrète
- Un besoin de solitude créative
- Une guérison par la méditation

## Conseils pour ce transit
- Explore ton monde intérieur
- Connecte-toi à l'universel
- Laisse l'inspiration venir du silence""",

    # ============== PISCES ==============
    ('pisces', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme mystérieux devient plus affirmé et magnétique.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ton magnétisme naturel avec une énergie plus directe. Tu dégages une aura romantique et séduisante qui attire naturellement les autres. C'est le moment de te montrer avec plus d'assurance.

## Ce que tu pourrais vivre
- Un charisme amplifié
- Des regards admiratifs
- L'envie d'affirmer ta beauté

## Conseils pour ce transit
- Laisse ta beauté intérieure rayonner
- Ose te montrer davantage
- Accepte l'admiration avec grâce""",

    ('pisces', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et valeurs sont touchées par une énergie favorable.

## L'énergie du moment
Vénus visite ta maison II, stimulant ton rapport à l'argent avec intuition. Tu pourrais recevoir des gains inattendus ou être guidé(e) vers de bons investissements. C'est aussi le moment de reconnaître la valeur de tes dons artistiques.

## Ce que tu pourrais vivre
- Une amélioration financière intuitive
- Des achats inspirés
- Une valorisation de tes talents artistiques

## Conseils pour ce transit
- Fais confiance à ton intuition financière
- Investis dans l'art et la beauté
- Valorise tes dons créatifs""",

    ('pisces', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient plus poétique et tes échanges plus inspirés.

## L'énergie du moment
Vénus adoucit ta maison III, rendant tes mots plus enchanteurs et tes idées plus artistiques. Les conversations deviennent des moments d'inspiration. C'est excellent pour l'écriture créative et les échanges artistiques.

## Ce que tu pourrais vivre
- Des dialogues inspirants
- Un rapprochement par l'art
- Du succès dans l'expression créative

## Conseils pour ce transit
- Exprime-toi avec poésie
- Partage tes inspirations
- Connecte-toi par l'art""",

    ('pisces', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un sanctuaire de paix et de beauté spirituelle.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant harmonie et spiritualité à ta vie domestique. Tu as envie de créer un espace sacré, un refuge artistique et apaisant. Les liens familiaux bénéficient de ta compassion.

## Ce que tu pourrais vivre
- L'envie de créer un espace sacré
- Des moments de paix en famille
- Un sentiment de sécurité spirituelle

## Conseils pour ce transit
- Transforme ton chez-toi en sanctuaire
- Apaise les tensions familiales
- Cultive la beauté intérieure""",

    ('pisces', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et la créativité s'expriment avec une intensité romantique!

## L'énergie du moment
Vénus brille dans ta maison V, promettant romance féerique et inspiration artistique. C'est une période magique pour l'amour – les connexions sont profondes et poétiques. Ta créativité s'exprime avec une beauté transcendante.

## Ce que tu pourrais vivre
- Un amour romantique et profond
- Une créativité inspirée
- Des moments de beauté pure

## Conseils pour ce transit
- Laisse-toi emporter par l'amour
- Crée depuis ton âme
- Savoure la beauté de chaque instant""",

    ('pisces', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien s'adoucit et tes routines deviennent plus spirituelles.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant le travail avec une touche de grâce. Tu apportes de la beauté aux tâches quotidiennes. C'est aussi un excellent moment pour des pratiques de bien-être holistiques.

## Ce que tu pourrais vivre
- Un travail plus harmonieux
- Des routines spirituelles
- Une guérison par le service

## Conseils pour ce transit
- Apporte de la beauté à ton travail
- Adopte des pratiques holistiques
- Sers avec compassion""",

    ('pisces', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les partenariats s'élèvent vers des connexions d'âme.

## L'énergie du moment
Vénus illumine ta maison VII, favorisant les relations profondes et spirituelles. Si tu es en couple, la connexion devient plus transcendante. Si tu es célibataire, une rencontre d'âme est possible. Les partenariats sont guidés par l'intuition.

## Ce que tu pourrais vivre
- Un amour spirituel profond
- Une rencontre d'âme
- Des collaborations inspirées

## Conseils pour ce transit
- Cherche les connexions profondes
- Sois guidé(e) par l'intuition
- Cultive l'amour inconditionnel""",

    ('pisces', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité et les liens profonds deviennent mystiques et transformateurs.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs de fusion et de transcendance. La sexualité et l'intimité peuvent devenir des expériences spirituelles. Les questions de ressources partagées se résolvent par l'intuition.

## Ce que tu pourrais vivre
- Une intimité transcendante
- Des questions résolues intuitivement
- Une transformation spirituelle

## Conseils pour ce transit
- Explore l'intimité sacrée
- Fais confiance à ton intuition financière
- Laisse-toi transformer par l'amour""",

    ('pisces', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs et la spiritualité t'appellent avec une force poétique.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ta soif de transcendance et de beauté universelle. Voyages spirituels, études mystiques ou philosophies contemplatives te séduisent. L'amour peut venir d'une connexion spirituelle.

## Ce que tu pourrais vivre
- Un voyage spirituel
- Une attirance pour le sacré
- Un éveil mystique

## Conseils pour ce transit
- Explore les chemins spirituels
- Ouvre-toi à la beauté universelle
- Cherche l'amour dans le sacré""",

    ('pisces', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta sensibilité artistique brille dans ta vie professionnelle.

## L'énergie du moment
Vénus éclaire ta maison X, apportant grâce et inspiration à ton image publique. Tu es perçu(e) comme particulièrement créatif(ve) et intuitif(ve). C'est excellent pour les carrières artistiques et ta réputation d'artiste.

## Ce que tu pourrais vivre
- Une reconnaissance de tes dons
- Des opportunités créatives
- Un projet artistique valorisé

## Conseils pour ce transit
- Brille par ta créativité
- Montre ta sensibilité
- Partage ta vision artistique""",

    ('pisces', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés s'approfondissent et ton réseau devient spirituel.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale plus riche en connexions d'âme. Les amitiés avec des personnes spirituelles ou artistiques se renforcent. C'est le moment de rejoindre des groupes qui nourrissent ton âme.

## Ce que tu pourrais vivre
- Des amitiés spirituelles
- Un réseau artistique
- L'engagement pour des causes compassionnelles

## Conseils pour ce transit
- Cultive des amitiés profondes
- Connecte-toi avec des artistes et spirituels
- Engage-toi pour la compassion""",

    ('pisces', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur sacrée t'enveloppe, invitant à l'union mystique.

## L'énergie du moment
Vénus se retire dans ta maison XII, ta maison naturelle! C'est une période bénie pour l'amour universel et la connexion spirituelle. Tu pourrais vivre une romance transcendante ou simplement te fondre dans la beauté du tout. C'est un temps de grâce.

## Ce que tu pourrais vivre
- Un amour universel et mystique
- Un besoin de solitude sacrée
- Une guérison profonde de l'âme

## Conseils pour ce transit
- Fonds-toi dans l'amour universel
- Médite et contemple
- Laisse la beauté te guérir""",
}

async def insert_interpretations():
    """Insert transit Venus interpretations into database."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_VENUS_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_venus',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='transit_venus',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            inserted += 1

        await db.commit()
        print(f"✅ Transit Venus (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
