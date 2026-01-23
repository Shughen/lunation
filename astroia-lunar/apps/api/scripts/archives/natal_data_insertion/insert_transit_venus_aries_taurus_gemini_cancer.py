#!/usr/bin/env python3
"""Insert transit_venus interpretations for Aries, Taurus, Gemini, Cancer (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_VENUS_INTERPRETATIONS = {
    # ============== ARIES ==============
    ('aries', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta façon d'aimer et de te montrer devient plus directe, spontanée et audacieuse.

## L'énergie du moment
Vénus en Bélier dans ta maison I enflamme ton charme personnel. Tu dégages une aura magnétique, une assurance qui attire naturellement les regards. C'est le moment de renouveler ton style, d'oser une nouvelle coupe ou un look plus audacieux. Tu as envie de plaire et tu n'as pas peur de le montrer.

## Ce que tu pourrais vivre
- Un regain de confiance dans ton apparence
- Des coups de cœur soudains et passionnés
- L'envie de prendre les devants en amour

## Conseils pour ce transit
- Ose te mettre en avant sans complexe
- Profite de ce magnétisme pour créer des connexions
- Attention à ne pas paraître trop pressant(e)""",

    ('aries', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes désirs matériels s'intensifient et tu veux te faire plaisir sans attendre.

## L'énergie du moment
Vénus traverse ta maison II et éveille ton appétit pour les belles choses. Tu as envie de dépenser pour toi, de t'offrir ce qui te fait plaisir maintenant. Cette énergie peut aussi attirer des opportunités financières inattendues ou des cadeaux. Ton rapport à l'argent devient plus impulsif mais aussi plus dynamique.

## Ce que tu pourrais vivre
- Des achats coup de cœur ou impulsifs
- Une rentrée d'argent inattendue
- L'envie de valoriser tes talents

## Conseils pour ce transit
- Fais-toi plaisir mais garde un œil sur ton budget
- Explore de nouvelles sources de revenus
- Valorise ce que tu possèdes déjà""",

    ('aries', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes échanges deviennent plus charmeurs et tes paroles ont un pouvoir de séduction accru.

## L'énergie du moment
Vénus dans ta maison III rend ta communication plus agréable et persuasive. Tu as le mot juste pour plaire, convaincre et créer des liens. Les conversations légères peuvent mener à des connexions plus profondes. C'est aussi un bon moment pour renouer avec des proches ou explorer ton quartier sous un nouveau jour.

## Ce que tu pourrais vivre
- Des discussions stimulantes et séduisantes
- Un rapprochement avec frères, sœurs ou voisins
- L'envie d'apprendre quelque chose de nouveau

## Conseils pour ce transit
- Utilise ton charme dans tes communications
- Propose des sorties ou des activités locales
- Écris ce message que tu repousses depuis longtemps""",

    ('aries', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tu as envie d'embellir ton chez-toi et de réchauffer l'ambiance familiale.

## L'énergie du moment
Vénus visite ta maison IV et apporte douceur et harmonie dans ton foyer. Tu pourrais avoir envie de décorer, réaménager ou simplement rendre ton espace plus accueillant. Les relations familiales bénéficient de cette énergie affectueuse. C'est un bon moment pour recevoir des proches ou passer du temps de qualité en famille.

## Ce que tu pourrais vivre
- L'envie de redécorer ou embellir ton intérieur
- Des moments chaleureux en famille
- Un sentiment de sécurité affective renforcé

## Conseils pour ce transit
- Investis dans le confort de ton chez-toi
- Organise un repas ou une soirée à la maison
- Prends soin de tes racines et de tes proches""",

    ('aries', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** La romance, la créativité et les plaisirs sont au premier plan de ta vie.

## L'énergie du moment
Vénus en maison V t'invite à vivre pleinement tes passions! C'est LE transit pour les romances, les flirts et les aventures amoureuses. Ta créativité est aussi stimulée – tu as envie de t'exprimer, de jouer, de créer. Si tu as des enfants, les moments partagés avec eux sont particulièrement joyeux.

## Ce que tu pourrais vivre
- Une nouvelle romance ou un renouveau amoureux
- Une explosion de créativité
- Des sorties, fêtes et moments de pur plaisir

## Conseils pour ce transit
- Laisse-toi aller aux plaisirs sans culpabiliser
- Exprime ta créativité sous toutes ses formes
- Si tu es en couple, ravive la flamme""",

    ('aries', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tu trouves plus de plaisir dans ton quotidien et tes routines deviennent plus agréables.

## L'énergie du moment
Vénus adoucit ta maison VI, transformant le travail et les tâches quotidiennes en expériences plus plaisantes. Les relations avec tes collègues s'améliorent, l'ambiance au bureau devient plus légère. Tu pourrais aussi être attiré(e) par des routines bien-être ou des soins esthétiques. Prends soin de toi au quotidien.

## Ce que tu pourrais vivre
- Une meilleure ambiance au travail
- L'envie de prendre soin de ta santé et ton apparence
- Du plaisir trouvé dans les petites tâches

## Conseils pour ce transit
- Embellis ton espace de travail
- Adopte une routine bien-être qui te fait du bien
- Sois agréable avec tes collègues et équipes""",

    ('aries', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes relations de couple et partenariats sont au cœur de tes préoccupations affectives.

## L'énergie du moment
Vénus dans ta maison VII met l'accent sur le "nous". C'est un moment privilégié pour les relations amoureuses sérieuses, les associations et les partenariats. Si tu es en couple, l'harmonie et la complicité sont favorisées. Si tu es célibataire, une rencontre significative peut se produire. Les négociations et accords sont aussi favorisés.

## Ce que tu pourrais vivre
- Un rapprochement significatif avec ton/ta partenaire
- Une rencontre importante si tu es célibataire
- Des collaborations harmonieuses

## Conseils pour ce transit
- Investis dans ta relation de couple
- Sois ouvert(e) aux compromis
- C'est le bon moment pour officialiser un partenariat""",

    ('aries', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité profonde et les liens fusionnels t'attirent avec intensité.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs et ta sexualité. Tu recherches des connexions profondes, authentiques, transformatrices. Ce transit peut aussi concerner les finances partagées – héritages, emprunts, investissements communs. Il y a quelque chose de magnétique et mystérieux dans ton aura en ce moment.

## Ce que tu pourrais vivre
- Une intimité plus intense avec ton/ta partenaire
- Des questions autour de l'argent partagé
- Une attraction pour ce qui est caché ou tabou

## Conseils pour ce transit
- Ose approfondir tes liens intimes
- Examine tes finances communes avec lucidité
- Laisse-toi transformer par l'amour""",

    ('aries', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et la beauté se trouvent dans l'ailleurs, l'étranger et l'aventure.

## L'énergie du moment
Vénus en maison IX t'appelle vers des horizons lointains. Voyages, cultures étrangères, philosophies nouvelles te séduisent particulièrement. Tu pourrais vivre une romance avec quelqu'un d'une autre culture ou être attiré(e) par des études, formations ou expériences qui élargissent ta vision du monde.

## Ce que tu pourrais vivre
- L'envie de voyager ou d'explorer
- Une attirance pour quelqu'un de différent
- Un intérêt pour la spiritualité ou la philosophie

## Conseils pour ce transit
- Planifie un voyage ou une aventure
- Ouvre-toi à des perspectives nouvelles
- Explore ce qui te fait rêver""",

    ('aries', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme brille dans ta vie professionnelle et publique.

## L'énergie du moment
Vénus illumine ta maison X, apportant grâce et diplomatie à ton image professionnelle. Tu es perçu(e) comme particulièrement agréable et charismatique par tes supérieurs et le public. C'est un excellent moment pour les négociations, présentations ou pour améliorer ta réputation. L'art et la beauté peuvent jouer un rôle dans ta carrière.

## Ce que tu pourrais vivre
- Une reconnaissance professionnelle positive
- Des opportunités grâce à ton réseau
- Un projet créatif mis en lumière

## Conseils pour ce transit
- Soigne ton image professionnelle
- Utilise ton charme dans les négociations
- Montre ton côté créatif au travail""",

    ('aries', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés s'épanouissent et ton réseau social t'apporte de la joie.

## L'énergie du moment
Vénus dans ta maison XI rend tes interactions sociales particulièrement agréables. Tu attires des personnes bienveillantes et tes amitiés existantes se renforcent. C'est le moment idéal pour participer à des événements sociaux, rejoindre des groupes ou associations. Tes espoirs et projets futurs sont teintés d'optimisme.

## Ce que tu pourrais vivre
- Des rencontres amicales enrichissantes
- Un soutien inattendu de ton réseau
- L'envie de t'impliquer dans une cause

## Conseils pour ce transit
- Participe à des événements sociaux
- Cultive tes amitiés précieuses
- Connecte-toi avec des personnes partageant tes valeurs""",

    ('aries', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'enveloppe, favorisant l'amour discret et l'introspection.

## L'énergie du moment
Vénus se retire dans ta maison XII, invitant à une forme d'amour plus subtile et spirituelle. Tu pourrais vivre une attirance secrète ou simplement apprécier des moments de solitude douce. C'est un temps pour guérir d'anciennes blessures affectives, pardonner et te reconnecter à toi-même. La créativité inspirée par le rêve est favorisée.

## Ce que tu pourrais vivre
- Une attirance ou relation discrète
- Un besoin de solitude apaisante
- Une guérison émotionnelle en profondeur

## Conseils pour ce transit
- Accorde-toi des moments de retraite
- Explore ta spiritualité avec douceur
- Laisse l'art et la musique t'inspirer""",

    # ============== TAURUS ==============
    ('taurus', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tu rayonnes d'une assurance nouvelle et ton charme devient plus audacieux.

## L'énergie du moment
Vénus enflamme ta maison I, te donnant une présence magnétique et une confiance renouvelée. Tu as envie de te montrer, d'être vu(e) et apprécié(e). Ton style pourrait évoluer vers quelque chose de plus affirmé. Les autres sont naturellement attirés par ton énergie positive et ta joie de vivre.

## Ce que tu pourrais vivre
- Un boost de confiance en ton apparence
- Des compliments et de l'attention positive
- L'envie de renouveler ton image

## Conseils pour ce transit
- Mets-toi en valeur sans hésiter
- Profite de cette période pour faire bonne impression
- Sois authentique dans ta façon de séduire""",

    ('taurus', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et tes plaisirs matériels sont favorisés par une énergie dynamique.

## L'énergie du moment
Vénus, ta planète maîtresse, traverse ta maison II avec une énergie de feu. Tes revenus pourraient augmenter ou tu pourrais être tenté(e) par des achats impulsifs mais satisfaisants. C'est le moment de reconnaître ta valeur et de demander ce que tu mérites. Le plaisir des sens est particulièrement important.

## Ce que tu pourrais vivre
- Une amélioration de ta situation financière
- Des achats plaisir ou des cadeaux
- Une prise de conscience de ta valeur

## Conseils pour ce transit
- Demande cette augmentation ou ce tarif
- Fais-toi plaisir avec modération
- Investis dans ce qui a vraiment de la valeur pour toi""",

    ('taurus', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes mots deviennent plus charmeurs et tes échanges plus agréables.

## L'énergie du moment
Vénus adoucit ta maison III, rendant ta communication plus séduisante et persuasive. Les conversations légères peuvent mener à des connexions significatives. C'est un bon moment pour les petits déplacements agréables, les rencontres de voisinage et les échanges avec tes proches. L'écriture et l'expression créative sont favorisées.

## Ce que tu pourrais vivre
- Des échanges plaisants et stimulants
- Un rapprochement avec ton entourage proche
- L'envie d'apprendre quelque chose de nouveau

## Conseils pour ce transit
- Exprime-toi avec charme et diplomatie
- Explore ton environnement local
- Renoue avec des proches négligés""",

    ('taurus', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un nid douillet que tu as envie d'embellir.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant harmonie et beauté à ton espace domestique. Tu as envie de rendre ton chez-toi plus confortable et esthétique. Les relations familiales bénéficient de cette douceur – c'est le moment pour des réconciliations ou des moments chaleureux en famille.

## Ce que tu pourrais vivre
- L'envie de décorer ou réaménager
- Des moments de tendresse en famille
- Un sentiment de sécurité émotionnelle

## Conseils pour ce transit
- Investis dans le confort de ton intérieur
- Organise un moment convivial chez toi
- Cultive l'harmonie familiale""",

    ('taurus', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour, la créativité et les plaisirs illuminent ta vie avec passion.

## L'énergie du moment
Vénus brille dans ta maison V, éveillant romance et créativité. C'est une période magique pour les affaires de cœur – nouvelles rencontres ou renouveau dans une relation existante. Ta créativité s'exprime avec plus de spontanéité. Les loisirs, les jeux et les moments de joie pure sont essentiels maintenant.

## Ce que tu pourrais vivre
- Un coup de foudre ou un regain de passion
- Une inspiration créative forte
- Des moments de pur bonheur

## Conseils pour ce transit
- Ouvre ton cœur à la romance
- Exprime ta créativité librement
- Accorde-toi des plaisirs sans culpabilité""",

    ('taurus', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien s'embellit et tu trouves du plaisir dans tes routines.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant ton travail quotidien et tes routines. L'ambiance avec les collègues s'améliore, et tu trouves plus de satisfaction dans tes tâches habituelles. C'est aussi un bon moment pour adopter des habitudes de bien-être ou des soins esthétiques.

## Ce que tu pourrais vivre
- Une meilleure ambiance professionnelle
- L'envie de prendre soin de toi au quotidien
- Du plaisir trouvé dans l'organisation

## Conseils pour ce transit
- Embellis ton espace de travail
- Adopte une routine beauté ou bien-être
- Sois agréable avec ton entourage professionnel""",

    ('taurus', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes relations de couple et partenariats s'épanouissent avec dynamisme.

## L'énergie du moment
Vénus illumine ta maison VII, mettant l'accent sur le couple et les associations. Si tu es en relation, c'est un moment de rapprochement et d'harmonie. Si tu es célibataire, une rencontre significative est possible. Les partenariats professionnels bénéficient aussi de cette énergie favorable.

## Ce que tu pourrais vivre
- Un renouveau dans ta relation de couple
- Une rencontre importante
- Des collaborations fructueuses

## Conseils pour ce transit
- Investis du temps dans tes relations importantes
- Sois ouvert(e) aux compromis
- Célèbre l'amour sous toutes ses formes""",

    ('taurus', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité profonde et les liens passionnels t'appellent avec force.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs et ta quête de profondeur. La sexualité et l'intimité émotionnelle prennent une importance particulière. Ce transit peut aussi concerner les ressources partagées – héritages, dettes, investissements communs.

## Ce que tu pourrais vivre
- Une intensification de ta vie intime
- Des questions financières partagées
- Une transformation par les liens profonds

## Conseils pour ce transit
- Explore l'intimité avec confiance
- Règle les questions d'argent partagé
- Laisse-toi transformer par l'amour profond""",

    ('taurus', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'aventure, les voyages et les nouvelles philosophies te séduisent.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ton goût pour l'ailleurs et l'inconnu. Tu pourrais être attiré(e) par des cultures étrangères, des voyages lointains ou des études qui élargissent tes horizons. Une romance avec quelqu'un de différent ou étranger est possible.

## Ce que tu pourrais vivre
- Un voyage ou un projet d'exploration
- Une attirance pour l'exotique
- Un intérêt pour la spiritualité ou la philosophie

## Conseils pour ce transit
- Planifie une aventure qui te fait rêver
- Ouvre-toi à des perspectives nouvelles
- Laisse-toi inspirer par d'autres cultures""",

    ('taurus', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme et ta grâce brillent dans ta vie professionnelle.

## L'énergie du moment
Vénus éclaire ta maison X, apportant diplomatie et attractivité à ton image publique. Tu es perçu(e) favorablement par tes supérieurs et le monde professionnel. C'est un excellent moment pour les négociations, les présentations ou pour améliorer ta réputation.

## Ce que tu pourrais vivre
- Une reconnaissance professionnelle
- Des opportunités grâce à ton charme
- Un projet créatif mis en valeur

## Conseils pour ce transit
- Soigne ton image professionnelle
- Utilise ta diplomatie naturelle
- Mets en avant tes talents artistiques""",

    ('taurus', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés fleurissent et ton réseau t'apporte bonheur et opportunités.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale particulièrement agréable. Les amitiés se renforcent, de nouvelles connexions se créent. C'est le moment de participer à des groupes, associations ou événements sociaux. Tes espoirs pour l'avenir sont teintés d'optimisme.

## Ce que tu pourrais vivre
- Des rencontres amicales précieuses
- Un soutien de ton réseau
- L'envie de t'impliquer collectivement

## Conseils pour ce transit
- Cultive tes amitiés avec attention
- Participe à des événements sociaux
- Connecte-toi avec ta communauté""",

    ('taurus', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'enveloppe, invitant à l'amour discret et à l'introspection.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour plus subtile et spirituelle. Tu pourrais vivre une attirance secrète ou simplement apprécier la solitude et le calme. C'est un temps propice pour guérir d'anciennes blessures du cœur et te reconnecter à ta vie intérieure.

## Ce que tu pourrais vivre
- Une romance discrète ou secrète
- Un besoin de retraite et de paix
- Une guérison émotionnelle

## Conseils pour ce transit
- Accorde-toi des moments de solitude
- Explore ta spiritualité
- Laisse l'art et la musique t'apaiser""",

    # ============== GEMINI ==============
    ('gemini', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tu dégages un charme vif et ta personnalité séduit avec spontanéité.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ton magnétisme personnel. Tu attires naturellement les regards et les sympathies. C'est le moment idéal pour renouveler ton image, oser un nouveau style ou simplement te montrer tel(le) que tu es. Ta confiance en toi est contagieuse.

## Ce que tu pourrais vivre
- Un regain de confiance en ton apparence
- De l'attention et des compliments
- L'envie de te réinventer

## Conseils pour ce transit
- Mets-toi en valeur sans complexe
- Fais une bonne première impression
- Exprime ton charme naturel""",

    ('gemini', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et plaisirs matériels bénéficient d'une énergie favorable.

## L'énergie du moment
Vénus visite ta maison II, stimulant ton rapport à l'argent et aux possessions. Tu pourrais recevoir des gains inattendus ou être tenté(e) par des achats plaisir. C'est aussi le moment de reconnaître ta propre valeur et d'investir en toi-même.

## Ce que tu pourrais vivre
- Une amélioration financière
- Des envies d'achats ou de cadeaux
- Une prise de conscience de tes talents

## Conseils pour ce transit
- Fais-toi plaisir avec sagesse
- Valorise tes compétences
- Investis dans ce qui compte vraiment""",

    ('gemini', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient irrésistible et tes échanges sont enrichissants.

## L'énergie du moment
Vénus brille dans ta maison III, ta maison naturelle! Tes mots sont particulièrement charmeurs et persuasifs. Les conversations légères peuvent mener à des connexions profondes. C'est un excellent moment pour les écrits, les présentations et les rencontres de proximité.

## Ce que tu pourrais vivre
- Des échanges stimulants et agréables
- Un rapprochement avec l'entourage proche
- Du succès dans la communication

## Conseils pour ce transit
- Utilise ton charme verbal
- Explore ton quartier avec curiosité
- Renoue avec des proches""",

    ('gemini', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un cocon d'harmonie que tu as envie de chérir.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant douceur et beauté à ta vie domestique. Tu as envie d'embellir ton chez-toi, de créer une atmosphère chaleureuse. Les relations familiales s'adoucissent, favorisant réconciliations et moments tendres.

## Ce que tu pourrais vivre
- L'envie de décorer ou réorganiser
- Des moments précieux en famille
- Un sentiment de paix intérieure

## Conseils pour ce transit
- Crée un espace qui te ressemble
- Passe du temps de qualité en famille
- Cultive ton bien-être à la maison""",

    ('gemini', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Romance, créativité et joie de vivre explosent dans ta vie!

## L'énergie du moment
Vénus illumine ta maison V, promettant des moments de pur bonheur. C'est la période idéale pour les romances, les aventures amoureuses et l'expression créative. Ta joie de vivre est contagieuse et tu attires naturellement les expériences plaisantes.

## Ce que tu pourrais vivre
- Un coup de cœur ou un renouveau amoureux
- Une créativité débordante
- Des moments de fête et de plaisir

## Conseils pour ce transit
- Ouvre-toi à l'amour sans retenue
- Exprime ta créativité joyeusement
- Profite de chaque instant de bonheur""",

    ('gemini', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien devient plus agréable et tes routines plus harmonieuses.

## L'énergie du moment
Vénus adoucit ta maison VI, transformant le travail en plaisir. L'ambiance avec les collègues s'améliore, et tu trouves de la satisfaction dans tes tâches habituelles. C'est aussi un bon moment pour prendre soin de ta santé et de ton apparence.

## Ce que tu pourrais vivre
- Une meilleure atmosphère au travail
- L'envie de routines bien-être
- Du plaisir dans l'organisation

## Conseils pour ce transit
- Embellis ton environnement de travail
- Adopte des habitudes saines
- Sois agréable avec ton entourage""",

    ('gemini', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes relations et partenariats s'épanouissent dans l'harmonie.

## L'énergie du moment
Vénus brille dans ta maison VII, favorisant le couple et les associations. Si tu es en relation, l'amour et la complicité sont au rendez-vous. Si tu es célibataire, une rencontre significative peut arriver. Les partenariats de toute nature sont bénis.

## Ce que tu pourrais vivre
- Un rapprochement amoureux
- Une rencontre importante
- Des collaborations réussies

## Conseils pour ce transit
- Investis dans tes relations clés
- Sois ouvert(e) au compromis
- Célèbre l'amour et l'amitié""",

    ('gemini', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité profonde et les connexions passionnelles t'appellent.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs et ta quête de profondeur émotionnelle. La sexualité et l'intimité sont particulièrement importantes. Les questions de finances partagées, héritages ou investissements peuvent aussi se présenter.

## Ce que tu pourrais vivre
- Une vie intime plus intense
- Des questions d'argent partagé
- Une transformation par l'amour

## Conseils pour ce transit
- Explore l'intimité avec audace
- Règle les questions financières communes
- Accepte la transformation""",

    ('gemini', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs, l'aventure et les nouvelles philosophies te font vibrer.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ta soif d'exploration. Voyages, cultures étrangères et études supérieures te séduisent particulièrement. Une romance avec quelqu'un de différent ou d'étranger est possible.

## Ce que tu pourrais vivre
- Un voyage ou un projet d'aventure
- Une attirance pour l'exotique
- Un éveil spirituel ou philosophique

## Conseils pour ce transit
- Planifie cette escapade qui te fait rêver
- Ouvre-toi à d'autres perspectives
- Explore de nouvelles croyances""",

    ('gemini', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme brille dans ta carrière et ta vie publique.

## L'énergie du moment
Vénus illumine ta maison X, apportant grâce et attractivité à ton image professionnelle. Tu es perçu(e) favorablement par tes supérieurs et le monde. C'est excellent pour les négociations, présentations et améliorer ta réputation.

## Ce que tu pourrais vivre
- Une reconnaissance au travail
- Des opportunités par ton réseau
- Un projet créatif valorisé

## Conseils pour ce transit
- Soigne ton image publique
- Utilise ta diplomatie
- Mets en avant tes talents""",

    ('gemini', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés fleurissent et ta vie sociale est source de joie.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant tes interactions sociales particulièrement agréables. Les amitiés se renforcent, de nouvelles connexions se forment. C'est le moment idéal pour les groupes, associations et événements collectifs.

## Ce que tu pourrais vivre
- Des rencontres amicales enrichissantes
- Un soutien de ta communauté
- L'envie de t'engager pour une cause

## Conseils pour ce transit
- Cultive tes amitiés précieuses
- Participe à des événements sociaux
- Connecte-toi avec tes réseaux""",

    ('gemini', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'invite à l'introspection et à l'amour subtil.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour plus discrète et spirituelle. Tu pourrais vivre une attirance secrète ou simplement savourer la solitude. C'est un temps de guérison émotionnelle et de reconnexion intérieure.

## Ce que tu pourrais vivre
- Une romance secrète ou cachée
- Un besoin de retraite paisible
- Une guérison du cœur

## Conseils pour ce transit
- Accorde-toi des moments seul(e)
- Explore ta vie intérieure
- Laisse l'art t'inspirer""",

    # ============== CANCER ==============
    ('cancer', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme s'affirme avec audace et tu rayonnes d'une confiance nouvelle.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ton magnétisme et ta présence. Tu dégages une énergie attractive qui ne passe pas inaperçue. C'est le moment de renouveler ton style, d'oser te montrer et d'embrasser ta beauté unique.

## Ce que tu pourrais vivre
- Un boost de confiance en toi
- De l'attention et de l'admiration
- L'envie de transformer ton image

## Conseils pour ce transit
- Ose te mettre en valeur
- Fais une impression mémorable
- Exprime ton charme sans retenue""",

    ('cancer', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et tes plaisirs matériels sont bénis par Vénus.

## L'énergie du moment
Vénus visite ta maison II, apportant une énergie favorable à tes finances et possessions. Tu pourrais recevoir de l'argent inattendu ou être tenté(e) par des achats plaisir. C'est aussi le moment de reconnaître ta valeur personnelle.

## Ce que tu pourrais vivre
- Une amélioration de tes revenus
- Des cadeaux ou achats agréables
- Une meilleure estime de toi

## Conseils pour ce transit
- Fais-toi plaisir raisonnablement
- Reconnais tes talents
- Investis en toi-même""",

    ('cancer', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient charmante et tes échanges enrichissants.

## L'énergie du moment
Vénus adoucit ta maison III, rendant tes mots plus séduisants et tes échanges plus harmonieux. Les conversations légères peuvent mener à des connexions significatives. C'est un bon moment pour les écrits, les rencontres locales et les liens avec tes proches.

## Ce que tu pourrais vivre
- Des dialogues agréables et fructueux
- Un rapprochement avec ton entourage
- L'envie d'apprendre et de partager

## Conseils pour ce transit
- Exprime-toi avec grâce
- Explore ton environnement proche
- Renoue avec des proches négligés""",

    ('cancer', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un sanctuaire d'amour et de beauté.

## L'énergie du moment
Vénus se pose dans ta maison IV, ta maison naturelle! C'est une période bénie pour la vie domestique et familiale. Tu as envie d'embellir ton chez-toi, de créer une atmosphère chaleureuse et accueillante. Les liens familiaux se renforcent dans la douceur.

## Ce que tu pourrais vivre
- L'envie de décorer et embellir
- Des moments précieux en famille
- Un profond sentiment de paix

## Conseils pour ce transit
- Crée le cocon dont tu rêves
- Reçois des proches chez toi
- Cultive l'harmonie familiale""",

    ('cancer', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour, la créativité et la joie illuminent ta vie!

## L'énergie du moment
Vénus brille dans ta maison V, promettant romance et moments de bonheur. C'est la période idéale pour les aventures amoureuses, l'expression créative et les plaisirs de la vie. Si tu as des enfants, les moments partagés sont particulièrement joyeux.

## Ce que tu pourrais vivre
- Un coup de foudre ou un renouveau
- Une créativité épanouie
- Des moments de pur plaisir

## Conseils pour ce transit
- Ouvre ton cœur à l'amour
- Exprime ta créativité librement
- Profite des plaisirs simples""",

    ('cancer', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien s'illumine et tes routines deviennent agréables.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant le travail et les tâches quotidiennes. L'ambiance avec les collègues s'améliore, tu trouves du plaisir dans tes routines. C'est aussi le moment idéal pour prendre soin de ta santé et de ton bien-être.

## Ce que tu pourrais vivre
- Une meilleure atmosphère au travail
- L'envie de routines bien-être
- Du plaisir dans l'organisation

## Conseils pour ce transit
- Embellis ton espace de travail
- Adopte des habitudes saines
- Sois bienveillant(e) envers toi-même""",

    ('cancer', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes relations de couple et partenariats sont au cœur de ton attention.

## L'énergie du moment
Vénus illumine ta maison VII, favorisant l'amour et les associations. Si tu es en couple, l'harmonie et la tendresse règnent. Si tu es célibataire, une rencontre significative peut se produire. Tous les partenariats bénéficient de cette énergie.

## Ce que tu pourrais vivre
- Un rapprochement avec ton partenaire
- Une rencontre importante
- Des collaborations harmonieuses

## Conseils pour ce transit
- Investis dans tes relations
- Sois ouvert(e) aux compromis
- Célèbre l'amour et les liens""",

    ('cancer', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité profonde et les liens passionnels t'attirent intensément.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs et ta quête de connexion profonde. La sexualité et l'intimité émotionnelle prennent de l'importance. Les questions de finances partagées peuvent aussi se poser.

## Ce que tu pourrais vivre
- Une vie intime plus intense
- Des questions d'argent partagé
- Une transformation par l'amour

## Conseils pour ce transit
- Explore l'intimité avec confiance
- Règle les questions financières communes
- Accepte les transformations""",

    ('cancer', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs et l'aventure te séduisent avec passion.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ton goût pour l'exploration. Voyages lointains, cultures étrangères et philosophies nouvelles t'attirent. Une romance avec quelqu'un de différent ou d'étranger est possible.

## Ce que tu pourrais vivre
- Un voyage ou une aventure
- Une attirance pour l'exotique
- Un éveil spirituel

## Conseils pour ce transit
- Planifie un voyage qui te fait rêver
- Ouvre-toi à d'autres cultures
- Explore de nouvelles croyances""",

    ('cancer', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme rayonne dans ta vie professionnelle et publique.

## L'énergie du moment
Vénus éclaire ta maison X, apportant grâce et diplomatie à ton image professionnelle. Tu es perçu(e) favorablement par tes supérieurs et le public. C'est excellent pour les négociations et améliorer ta réputation.

## Ce que tu pourrais vivre
- Une reconnaissance au travail
- Des opportunités par ton charme
- Un projet créatif valorisé

## Conseils pour ce transit
- Soigne ton image publique
- Utilise ta diplomatie naturelle
- Mets en avant tes talents""",

    ('cancer', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés s'épanouissent et ton réseau t'apporte de la joie.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale particulièrement agréable. Les amitiés se renforcent et de nouvelles connexions se créent. C'est le moment parfait pour les groupes, associations et événements collectifs.

## Ce que tu pourrais vivre
- Des rencontres amicales précieuses
- Un soutien de ta communauté
- L'envie de t'engager pour une cause

## Conseils pour ce transit
- Cultive tes amitiés
- Participe à des événements sociaux
- Connecte-toi avec tes réseaux""",

    ('cancer', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'enveloppe, invitant à l'introspection amoureuse.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour plus subtile et spirituelle. Tu pourrais vivre une attirance discrète ou simplement savourer la solitude. C'est un temps de guérison émotionnelle.

## Ce que tu pourrais vivre
- Une romance secrète
- Un besoin de solitude paisible
- Une guérison du cœur

## Conseils pour ce transit
- Accorde-toi des moments de retraite
- Explore ta spiritualité
- Laisse l'art t'apaiser""",
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
        print(f"✅ Transit Venus (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
