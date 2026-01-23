#!/usr/bin/env python3
"""Insert transit_venus interpretations for Leo, Virgo, Libra, Scorpio (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_VENUS_INTERPRETATIONS = {
    # ============== LEO ==============
    ('leo', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme devient flamboyant et tu attires tous les regards.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ta présence naturelle et ton magnétisme. Tu rayonnes d'une confiance séduisante qui attire naturellement les autres. C'est le moment parfait pour renouveler ton style, mettre en valeur ta beauté unique et te montrer sous ton meilleur jour.

## Ce que tu pourrais vivre
- Un boost de confiance en ton apparence
- Des compliments et de l'admiration
- L'envie de te réinventer visuellement

## Conseils pour ce transit
- Mets-toi en valeur avec audace
- Fais une entrée remarquée
- Exprime ton charme naturel""",

    ('leo', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances prospèrent et tu as envie de te faire plaisir.

## L'énergie du moment
Vénus visite ta maison II, apportant une énergie favorable à tes revenus et possessions. Tu pourrais recevoir de l'argent inattendu ou être attiré(e) par de beaux objets. C'est aussi le moment de reconnaître ta propre valeur et de demander ce que tu mérites vraiment.

## Ce que tu pourrais vivre
- Une amélioration financière
- Des achats plaisir ou des cadeaux
- Une meilleure estime personnelle

## Conseils pour ce transit
- Profite des belles choses avec modération
- Valorise tes talents uniques
- Investis dans ce qui te fait vibrer""",

    ('leo', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes mots deviennent séducteurs et tes échanges sont enrichissants.

## L'énergie du moment
Vénus adoucit ta maison III, rendant ta communication particulièrement charmante et persuasive. Les conversations légères peuvent mener à des connexions profondes. C'est un excellent moment pour l'écriture, les présentations et les rencontres locales.

## Ce que tu pourrais vivre
- Des dialogues stimulants et agréables
- Un rapprochement avec ton entourage proche
- Du succès dans tes communications

## Conseils pour ce transit
- Utilise ton éloquence naturelle
- Explore ton quartier avec curiosité
- Renoue avec des proches""",

    ('leo', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un palais de douceur et d'harmonie.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant beauté et chaleur à ta vie domestique. Tu as envie d'embellir ton intérieur, de créer une atmosphère luxueuse et accueillante. Les relations familiales bénéficient de cette douceur.

## Ce que tu pourrais vivre
- L'envie de décorer somptueusement
- Des moments précieux en famille
- Un sentiment de sécurité émotionnelle

## Conseils pour ce transit
- Crée un chez-toi qui te ressemble
- Organise des réunions familiales
- Cultive l'harmonie domestique""",

    ('leo', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Romance, créativité et plaisirs sont à leur apogée dans ta vie!

## L'énergie du moment
Vénus brille dans ta maison V, ta maison naturelle! C'est une période exceptionnelle pour l'amour, la créativité et la joie de vivre. Les romances s'enflamment, ta créativité explose, et chaque moment devient une célébration. Les plaisirs de la vie sont particulièrement intenses.

## Ce que tu pourrais vivre
- Un coup de foudre passionné
- Une explosion créative
- Des moments de bonheur pur

## Conseils pour ce transit
- Laisse-toi emporter par l'amour
- Crée et exprime-toi avec passion
- Savoure chaque plaisir""",

    ('leo', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien devient plus agréable et tes routines plus harmonieuses.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant le travail et les tâches quotidiennes. L'ambiance avec les collègues s'améliore notablement. Tu trouves du plaisir dans l'organisation et les routines bien-être t'attirent particulièrement.

## Ce que tu pourrais vivre
- Une meilleure ambiance au travail
- L'envie de prendre soin de toi
- Du plaisir dans les détails

## Conseils pour ce transit
- Embellis ton espace de travail
- Adopte des routines luxueuses
- Sois généreux(se) avec tes collègues""",

    ('leo', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les partenariats brillent de mille feux dans ta vie.

## L'énergie du moment
Vénus illumine ta maison VII, favorisant toutes tes relations importantes. Si tu es en couple, l'amour se renouvelle avec passion. Si tu es célibataire, une rencontre significative peut illuminer ta vie. Les partenariats de toute nature sont bénis.

## Ce que tu pourrais vivre
- Un rapprochement amoureux intense
- Une rencontre marquante
- Des collaborations fructueuses

## Conseils pour ce transit
- Investis dans ta relation principale
- Sois ouvert(e) à l'amour
- Cultive tes partenariats""",

    ('leo', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité profonde et les liens passionnels t'appellent avec intensité.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs et ta quête de connexion profonde. La sexualité et l'intimité émotionnelle deviennent centrales. Les questions de finances partagées ou d'héritages peuvent aussi se présenter.

## Ce que tu pourrais vivre
- Une vie intime plus intense
- Des questions d'argent partagé
- Une transformation par l'amour

## Conseils pour ce transit
- Explore l'intimité avec passion
- Règle les questions financières communes
- Accepte d'être transformé(e)""",

    ('leo', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'aventure, les voyages et les horizons lointains te font rêver.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ta soif d'exploration. Voyages exotiques, cultures étrangères et philosophies nouvelles t'attirent irrésistiblement. Une romance avec quelqu'un de différent est possible.

## Ce que tu pourrais vivre
- Un voyage passionnant
- Une attirance pour l'exotique
- Un éveil spirituel ou philosophique

## Conseils pour ce transit
- Planifie cette aventure qui te fait vibrer
- Ouvre-toi à d'autres cultures
- Explore de nouvelles croyances""",

    ('leo', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme royal brille dans ta vie professionnelle et publique.

## L'énergie du moment
Vénus éclaire ta maison X, apportant grâce et prestige à ton image publique. Tu es perçu(e) comme particulièrement attractif(ve) et charismatique par le monde professionnel. C'est excellent pour les négociations et ta réputation.

## Ce que tu pourrais vivre
- Une reconnaissance professionnelle
- Des opportunités par ton charme
- Un projet créatif mis en lumière

## Conseils pour ce transit
- Brille dans le monde professionnel
- Utilise ta présence naturelle
- Montre tes talents artistiques""",

    ('leo', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés rayonnent et ton réseau social t'apporte de la joie.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale particulièrement riche et agréable. Les amitiés se renforcent, de nouvelles connexions se créent. Tu es au centre de ton cercle social et ton charisme attire les bonnes personnes.

## Ce que tu pourrais vivre
- Des rencontres amicales précieuses
- Un soutien de ta communauté
- L'envie de briller en groupe

## Conseils pour ce transit
- Sois le soleil de ton groupe d'amis
- Participe à des événements sociaux
- Partage ta lumière avec les autres""",

    ('leo', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'enveloppe, invitant à l'amour discret et spirituel.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour plus intime et spirituelle. Tu pourrais vivre une attirance secrète ou simplement savourer des moments de solitude créative. C'est un temps de guérison et de reconnexion intérieure.

## Ce que tu pourrais vivre
- Une romance discrète
- Un besoin de retraite paisible
- Une guérison émotionnelle

## Conseils pour ce transit
- Accorde-toi des moments de solitude
- Explore ta vie intérieure
- Laisse l'art t'inspirer""",

    # ============== VIRGO ==============
    ('virgo', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme discret devient plus affirmé et tu attires l'attention.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ton magnétisme naturel. Tu dégages une énergie plus audacieuse que d'habitude, ce qui attire les regards et les sympathies. C'est le moment d'oser te mettre en valeur et de montrer ta beauté unique.

## Ce que tu pourrais vivre
- Un regain de confiance en ton apparence
- Des compliments inattendus
- L'envie de renouveler ton style

## Conseils pour ce transit
- Ose te montrer davantage
- Soigne ton apparence avec plaisir
- Accepte les compliments avec grâce""",

    ('virgo', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances sont favorisées et tu apprécies les belles choses.

## L'énergie du moment
Vénus visite ta maison II, stimulant ton rapport à l'argent et aux plaisirs matériels. Tu pourrais recevoir des gains inattendus ou être tenté(e) par des achats de qualité. C'est aussi le moment de reconnaître ta valeur personnelle.

## Ce que tu pourrais vivre
- Une amélioration financière
- Des achats réfléchis mais plaisants
- Une meilleure estime de tes compétences

## Conseils pour ce transit
- Investis dans la qualité
- Valorise tes talents pratiques
- Fais-toi plaisir avec discernement""",

    ('virgo', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient plus charmante et tes échanges plus harmonieux.

## L'énergie du moment
Vénus adoucit ta maison III, rendant tes mots plus agréables et persuasifs. Les conversations deviennent des moments de plaisir et de connexion. C'est excellent pour l'écriture, les présentations et les liens avec tes proches.

## Ce que tu pourrais vivre
- Des dialogues enrichissants
- Un rapprochement avec ton entourage
- Du succès dans tes communications

## Conseils pour ce transit
- Exprime-toi avec élégance
- Explore ton environnement local
- Renoue des liens négligés""",

    ('virgo', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un havre de paix et de beauté ordonnée.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant harmonie et esthétique à ta vie domestique. Tu as envie de ranger, d'organiser et d'embellir ton chez-toi avec goût. Les relations familiales bénéficient de cette douceur.

## Ce que tu pourrais vivre
- L'envie d'harmoniser ton intérieur
- Des moments de qualité en famille
- Un sentiment de sérénité à la maison

## Conseils pour ce transit
- Crée un espace beau et fonctionnel
- Passe du temps avec tes proches
- Cultive l'harmonie domestique""",

    ('virgo', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et la créativité illuminent ta vie avec une joie inattendue.

## L'énergie du moment
Vénus brille dans ta maison V, éveillant romance et expression créative. C'est une période favorable aux plaisirs du cœur et de l'art. Ta créativité s'exprime avec plus de spontanéité et les moments de joie sont particulièrement appréciés.

## Ce que tu pourrais vivre
- Un coup de cœur ou un renouveau amoureux
- Une inspiration créative
- Des moments de bonheur simple

## Conseils pour ce transit
- Ouvre-toi aux plaisirs de l'amour
- Laisse ta créativité s'exprimer
- Profite des moments de détente""",

    ('virgo', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien devient un art et tes routines sont sources de plaisir.

## L'énergie du moment
Vénus traverse ta maison VI, ta maison naturelle! C'est une période bénie pour le travail et les routines quotidiennes. Tu trouves du plaisir dans l'organisation, le soin de ta santé et les détails bien faits. L'ambiance professionnelle s'améliore.

## Ce que tu pourrais vivre
- Une grande satisfaction au travail
- L'envie de routines bien-être raffinées
- Du plaisir dans la perfection

## Conseils pour ce transit
- Perfectionne ton art de vivre quotidien
- Adopte des habitudes saines et agréables
- Sois bienveillant(e) avec tes collègues""",

    ('virgo', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les partenariats sont au cœur de tes préoccupations.

## L'énergie du moment
Vénus illumine ta maison VII, favorisant les relations de couple et les associations. Si tu es en relation, l'harmonie et la tendresse règnent. Si tu es célibataire, une rencontre significative peut se produire. Les partenariats professionnels sont aussi favorisés.

## Ce que tu pourrais vivre
- Un rapprochement avec ton partenaire
- Une rencontre prometteuse
- Des collaborations harmonieuses

## Conseils pour ce transit
- Investis dans tes relations importantes
- Sois ouvert(e) au compromis
- Cultive l'équilibre dans le couple""",

    ('virgo', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité profonde et les liens transformateurs t'attirent.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs et ta quête de connexion profonde. La sexualité et l'intimité émotionnelle deviennent importantes. Les questions de finances partagées peuvent aussi se présenter.

## Ce que tu pourrais vivre
- Une vie intime plus riche
- Des questions d'argent partagé
- Une transformation par les liens profonds

## Conseils pour ce transit
- Explore l'intimité avec confiance
- Règle les questions financières communes
- Accepte d'évoluer par l'amour""",

    ('virgo', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs et les nouvelles connaissances te séduisent.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ton goût pour l'exploration intellectuelle et physique. Voyages, études et philosophies nouvelles t'attirent. Une romance avec quelqu'un de différent ou d'étranger est possible.

## Ce que tu pourrais vivre
- Un voyage d'étude ou de plaisir
- Une attirance pour d'autres cultures
- Un éveil intellectuel ou spirituel

## Conseils pour ce transit
- Planifie un voyage enrichissant
- Ouvre-toi à d'autres perspectives
- Apprends quelque chose de nouveau""",

    ('virgo', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton professionnalisme et ton charme discret brillent au travail.

## L'énergie du moment
Vénus éclaire ta maison X, apportant grâce à ton image professionnelle. Tu es perçu(e) favorablement par tes supérieurs. C'est excellent pour les négociations, les présentations et améliorer ta réputation professionnelle.

## Ce que tu pourrais vivre
- Une reconnaissance de ton travail
- Des opportunités professionnelles
- Une image publique améliorée

## Conseils pour ce transit
- Soigne ton image professionnelle
- Utilise ta diplomatie naturelle
- Mets en valeur tes compétences""",

    ('virgo', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés fleurissent et ton réseau t'apporte satisfaction.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale particulièrement agréable. Les amitiés se renforcent avec des personnes de qualité. C'est le moment de participer à des groupes ou associations qui partagent tes valeurs.

## Ce que tu pourrais vivre
- Des rencontres amicales enrichissantes
- Un soutien de personnes bienveillantes
- L'envie de contribuer à une cause

## Conseils pour ce transit
- Cultive tes amitiés de qualité
- Participe à des groupes constructifs
- Connecte-toi avec ta communauté""",

    ('virgo', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'invite à la contemplation et à l'amour discret.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour plus subtile et intérieure. Tu pourrais vivre une attirance discrète ou simplement apprécier des moments de solitude productive. C'est un temps de guérison et de ressourcement.

## Ce que tu pourrais vivre
- Une romance discrète ou intérieure
- Un besoin de retraite réparatrice
- Une guérison émotionnelle

## Conseils pour ce transit
- Accorde-toi des moments de solitude
- Pratique des activités contemplatives
- Laisse l'art et la nature t'apaiser""",

    # ============== LIBRA ==============
    ('libra', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme naturel s'affirme avec une énergie plus directe et passionnée.

## L'énergie du moment
Vénus, ta planète maîtresse, traverse ta maison I avec une énergie de feu! Tu rayonnes d'une assurance nouvelle et ton magnétisme est particulièrement puissant. C'est LE moment pour renouveler ton image, oser des choix audacieux et te montrer sous un jour différent.

## Ce que tu pourrais vivre
- Un boost de confiance exceptionnel
- Une attractivité amplifiée
- L'envie de te réinventer

## Conseils pour ce transit
- Ose l'audace dans ton style
- Prends des initiatives en amour
- Exprime ta personnalité pleinement""",

    ('libra', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et tes valeurs sont dynamisées par une énergie favorable.

## L'énergie du moment
Vénus visite ta maison II, stimulant ton rapport à l'argent et aux possessions. Tu pourrais recevoir des gains inattendus ou être attiré(e) par de beaux objets. C'est aussi le moment de reconnaître ta valeur et de demander ce que tu mérites.

## Ce que tu pourrais vivre
- Une amélioration de tes revenus
- Des achats plaisir impulsifs
- Une prise de conscience de ta valeur

## Conseils pour ce transit
- Fais-toi plaisir avec élégance
- Valorise tes talents artistiques
- Investis dans ce qui t'embellit""",

    ('libra', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient irrésistiblement charmante et persuasive.

## L'énergie du moment
Vénus adoucit ta maison III, rendant tes échanges particulièrement agréables. Tes mots sont choisis avec élégance et tu séduisais par ton esprit. C'est excellent pour les négociations, l'écriture et les rencontres locales.

## Ce que tu pourrais vivre
- Des conversations captivantes
- Un rapprochement avec ton entourage
- Du succès dans tes communications

## Conseils pour ce transit
- Utilise ton éloquence naturelle
- Explore ton quartier avec style
- Renoue avec des proches""",

    ('libra', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un sanctuaire d'harmonie et de beauté.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant équilibre et esthétique à ta vie domestique. Tu as envie de décorer, d'harmoniser les espaces et de créer une atmosphère raffinée. Les relations familiales bénéficient de ta diplomatie naturelle.

## Ce que tu pourrais vivre
- L'envie de redécorer avec goût
- Des moments d'harmonie en famille
- Un sentiment de paix intérieure

## Conseils pour ce transit
- Crée un chez-toi harmonieux
- Joue le médiateur en famille
- Cultive la beauté domestique""",

    ('libra', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et la créativité s'enflamment avec passion!

## L'énergie du moment
Vénus brille dans ta maison V, promettant romance et expression artistique. C'est une période exceptionnelle pour les affaires de cœur - les romances s'intensifient et la créativité s'exprime avec audace. Les plaisirs de la vie sont particulièrement savoureux.

## Ce que tu pourrais vivre
- Un coup de foudre passionné
- Une inspiration artistique forte
- Des moments de joie pure

## Conseils pour ce transit
- Laisse-toi emporter par l'amour
- Crée avec passion
- Savoure les plaisirs esthétiques""",

    ('libra', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien devient plus élégant et tes routines plus agréables.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant le travail et les tâches quotidiennes. Tu apportes une touche d'élégance à tout ce que tu fais. L'ambiance professionnelle s'harmonise et tu trouves du plaisir dans les détails bien faits.

## Ce que tu pourrais vivre
- Une meilleure ambiance au travail
- L'envie de routines esthétiques
- Du plaisir dans l'organisation

## Conseils pour ce transit
- Embellis ton espace de travail
- Adopte des habitudes raffinées
- Crée l'harmonie avec tes collègues""",

    ('libra', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les partenariats sont au zénith de leur potentiel!

## L'énergie du moment
Vénus illumine ta maison VII, ta maison naturelle! C'est une période bénie pour toutes tes relations. Si tu es en couple, l'amour se renouvelle avec intensité. Si tu es célibataire, une rencontre significative peut transformer ta vie. Les partenariats brillent.

## Ce que tu pourrais vivre
- Un amour passionné et renouvelé
- Une rencontre destinée
- Des collaborations exceptionnelles

## Conseils pour ce transit
- Investis pleinement dans l'amour
- Sois ouvert(e) aux nouvelles relations
- Célèbre tous tes partenariats""",

    ('libra', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité profonde et les liens transformateurs t'appellent.

## L'énergie du moment
Vénus plonge dans ta maison VIII, intensifiant tes désirs et ta quête de profondeur. La sexualité et l'intimité émotionnelle prennent une dimension transformatrice. Les questions de finances partagées peuvent aussi se clarifier.

## Ce que tu pourrais vivre
- Une vie intime intensifiée
- Des questions d'argent partagé
- Une transformation par l'amour

## Conseils pour ce transit
- Explore l'intimité avec confiance
- Règle les questions financières communes
- Laisse l'amour te transformer""",

    ('libra', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs et les horizons lointains te font vibrer de désir.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ta soif d'exploration et de beauté lointaine. Voyages culturels, études artistiques et philosophies esthétiques t'attirent. Une romance avec quelqu'un de différent est particulièrement favorisée.

## Ce que tu pourrais vivre
- Un voyage culturel enrichissant
- Une attirance pour l'exotique
- Un éveil artistique ou spirituel

## Conseils pour ce transit
- Planifie un voyage culturel
- Ouvre-toi à d'autres esthétiques
- Explore de nouvelles philosophies""",

    ('libra', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton charme et ta diplomatie brillent dans ta carrière.

## L'énergie du moment
Vénus éclaire ta maison X, apportant grâce et attractivité à ton image publique. Tu es perçu(e) comme particulièrement élégant(e) et charismatique. C'est excellent pour les négociations, les présentations et ta réputation.

## Ce que tu pourrais vivre
- Une reconnaissance professionnelle
- Des opportunités par ton charme
- Un projet artistique valorisé

## Conseils pour ce transit
- Brille avec élégance au travail
- Utilise ta diplomatie innée
- Mets en avant tes talents artistiques""",

    ('libra', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés s'épanouissent et ton cercle social rayonne.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale particulièrement harmonieuse. Les amitiés se renforcent avec des personnes qui partagent ton sens de l'esthétique. C'est le moment parfait pour les événements mondains et les groupes artistiques.

## Ce que tu pourrais vivre
- Des rencontres amicales raffinées
- Un cercle social harmonieux
- L'envie de t'impliquer culturellement

## Conseils pour ce transit
- Cultive tes amitiés avec élégance
- Participe à des événements culturels
- Connecte-toi avec des artistes""",

    ('libra', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'enveloppe, invitant à l'amour mystique.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour plus subtile et spirituelle. Tu pourrais vivre une attirance secrète ou simplement savourer la beauté de la solitude. C'est un temps de guérison et d'inspiration artistique profonde.

## Ce que tu pourrais vivre
- Une romance secrète ou platonique
- Un besoin de retraite esthétique
- Une guérison par l'art

## Conseils pour ce transit
- Accorde-toi des moments contemplatifs
- Explore la beauté intérieure
- Laisse l'art t'inspirer profondément""",

    # ============== SCORPIO ==============
    ('scorpio', 1): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton magnétisme devient plus direct et ton charme plus audacieux.

## L'énergie du moment
Vénus traverse ta maison I, amplifiant ton attractivité naturelle avec une énergie de feu. Tu dégages une présence magnétique encore plus puissante que d'habitude. C'est le moment d'oser te montrer, de renouveler ton style avec audace.

## Ce que tu pourrais vivre
- Un magnétisme intensifié
- Des regards et de l'attention
- L'envie de transformer ton image

## Conseils pour ce transit
- Mets ton charme au service de tes désirs
- Ose les changements audacieux
- Exprime ta séduction naturelle""",

    ('scorpio', 2): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes finances et tes plaisirs matériels sont favorisés intensément.

## L'énergie du moment
Vénus visite ta maison II, stimulant ton rapport à l'argent et aux possessions. Tu pourrais recevoir des gains inattendus ou être attiré(e) par des objets de désir. C'est aussi le moment de reconnaître ta valeur profonde.

## Ce que tu pourrais vivre
- Une amélioration financière
- Des achats passionnels
- Une prise de conscience de ta valeur

## Conseils pour ce transit
- Investis dans ce qui t'attire vraiment
- Valorise tes talents uniques
- Fais-toi plaisir stratégiquement""",

    ('scorpio', 3): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ta communication devient plus séduisante et tes mots plus percutants.

## L'énergie du moment
Vénus adoucit ta maison III, rendant tes échanges plus charmants sans perdre en profondeur. Les conversations peuvent devenir des jeux de séduction subtils. C'est excellent pour convaincre et créer des liens.

## Ce que tu pourrais vivre
- Des dialogues captivants
- Un rapprochement avec des proches
- Du succès dans tes communications

## Conseils pour ce transit
- Utilise ton charme verbal
- Explore ton environnement avec curiosité
- Renoue des liens importants""",

    ('scorpio', 4): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton foyer devient un nid de douceur et de transformation.

## L'énergie du moment
Vénus se pose dans ta maison IV, apportant harmonie et beauté à ta vie domestique. Tu as envie de transformer ton chez-toi en un espace plus accueillant et esthétique. Les liens familiaux peuvent se guérir.

## Ce que tu pourrais vivre
- L'envie de transformer ton intérieur
- Des moments de guérison familiale
- Un sentiment de sécurité émotionnelle

## Conseils pour ce transit
- Crée un sanctuaire personnel
- Guéris les blessures familiales
- Cultive l'intimité domestique""",

    ('scorpio', 5): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et la créativité brûlent d'une flamme intense!

## L'énergie du moment
Vénus brille dans ta maison V, promettant des romances passionnées et une créativité puissante. C'est une période d'amour intense, de plaisirs profonds et d'expression artistique transformatrice. Les liaisons peuvent être dévorantes.

## Ce que tu pourrais vivre
- Un amour passionné et transformateur
- Une créativité intense
- Des plaisirs profonds

## Conseils pour ce transit
- Vis l'amour avec intensité
- Crée depuis tes profondeurs
- Savoure les plaisirs passionnément""",

    ('scorpio', 6): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton quotidien devient plus agréable et tes routines plus satisfaisantes.

## L'énergie du moment
Vénus traverse ta maison VI, adoucissant le travail et les tâches quotidiennes. L'ambiance professionnelle s'améliore et tu trouves du plaisir dans l'efficacité. C'est aussi un bon moment pour prendre soin de ta santé.

## Ce que tu pourrais vivre
- Une meilleure ambiance au travail
- L'envie de routines bien-être
- Du plaisir dans le contrôle

## Conseils pour ce transit
- Transforme ton espace de travail
- Adopte des habitudes régénérantes
- Sois stratégique avec tes collègues""",

    ('scorpio', 7): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'amour et les partenariats s'intensifient avec passion.

## L'énergie du moment
Vénus illumine ta maison VII, favorisant les relations profondes et transformatrices. Si tu es en couple, l'amour peut se régénérer avec intensité. Si tu es célibataire, une rencontre magnétique peut survenir. Les partenariats sont transformateurs.

## Ce que tu pourrais vivre
- Un amour régénéré ou transformé
- Une rencontre magnétique
- Des collaborations puissantes

## Conseils pour ce transit
- Investis intensément dans l'amour
- Sois ouvert(e) à la transformation relationnelle
- Cultive les liens profonds""",

    ('scorpio', 8): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'intimité la plus profonde et les liens fusionnels t'appellent!

## L'énergie du moment
Vénus plonge dans ta maison VIII, ta maison naturelle! C'est une période exceptionnelle pour l'intimité, la sexualité et les connexions profondes. Les désirs sont exacerbés et les liens peuvent être transformateurs. Les finances partagées sont aussi favorisées.

## Ce que tu pourrais vivre
- Une intimité transformatrice
- Des questions de finances partagées résolues
- Une renaissance par l'amour

## Conseils pour ce transit
- Plonge dans l'intimité sans peur
- Règle les questions financières communes
- Laisse l'amour te régénérer""",

    ('scorpio', 9): """# ♀ Transit de Vénus en Bélier

**En une phrase :** L'ailleurs et les mystères lointains t'attirent avec force.

## L'énergie du moment
Vénus voyage dans ta maison IX, éveillant ta soif d'exploration des profondeurs de l'existence. Voyages initiatiques, philosophies ésotériques et cultures mystérieuses t'attirent. Une romance avec quelqu'un de différent peut être transformatrice.

## Ce que tu pourrais vivre
- Un voyage initiatique
- Une attirance pour le mystérieux
- Un éveil spirituel profond

## Conseils pour ce transit
- Explore les mystères de l'ailleurs
- Ouvre-toi à des savoirs cachés
- Vis des expériences transformatrices""",

    ('scorpio', 10): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Ton magnétisme brille dans ta carrière et ta vie publique.

## L'énergie du moment
Vénus éclaire ta maison X, apportant charme et pouvoir à ton image professionnelle. Tu es perçu(e) comme particulièrement magnétique et influent(e). C'est excellent pour les négociations stratégiques et ta réputation.

## Ce que tu pourrais vivre
- Une reconnaissance de ton pouvoir
- Des opportunités par ton magnétisme
- Un projet passionnel valorisé

## Conseils pour ce transit
- Utilise ton charme stratégiquement
- Brille avec intensité au travail
- Montre tes talents cachés""",

    ('scorpio', 11): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Tes amitiés s'approfondissent et ton réseau devient plus puissant.

## L'énergie du moment
Vénus brille dans ta maison XI, rendant ta vie sociale plus riche en connexions significatives. Les amitiés superficielles ne t'intéressent pas – tu cherches des liens authentiques. C'est le moment de rejoindre des groupes qui partagent tes passions profondes.

## Ce que tu pourrais vivre
- Des amitiés intenses et loyales
- Un réseau influent
- L'envie de causes transformatrices

## Conseils pour ce transit
- Cultive des amitiés profondes
- Connecte-toi avec des personnes puissantes
- Engage-toi pour des causes qui comptent""",

    ('scorpio', 12): """# ♀ Transit de Vénus en Bélier

**En une phrase :** Une douceur secrète t'enveloppe, invitant à l'amour caché et mystique.

## L'énergie du moment
Vénus se retire dans ta maison XII, favorisant une forme d'amour secrète et transformatrice. Tu pourrais vivre une attirance cachée ou simplement plonger dans les profondeurs de ton âme. C'est un temps de guérison karmique.

## Ce que tu pourrais vivre
- Une romance secrète intense
- Un besoin de retraite régénératrice
- Une guérison des blessures anciennes

## Conseils pour ce transit
- Explore tes profondeurs en solitude
- Guéris tes blessures secrètes
- Laisse l'amour te transformer de l'intérieur""",
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
        print(f"✅ Transit Venus (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
