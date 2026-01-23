#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Soleil en Lion/Vierge/Balance/Scorpion."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SUN_INTERPRETATIONS = {
    # LEO
    ('leo', 1): """# ☉ Transit du Soleil en Lion

**En une phrase :** Tu rayonnes de confiance — c'est ton moment pour briller et assumer ta grandeur.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Lion, son signe de prédilection. Tu es au centre de l'attention, confiant et magnétique. C'est le moment de t'affirmer avec panache et d'assumer pleinement qui tu es.

## Ce que tu pourrais vivre
- Une confiance en toi décuplée
- L'envie de te mettre en avant et d'être vu
- Une présence naturellement charismatique

## Conseils pour ce transit
- Assume ta grandeur sans te justifier
- Prends des initiatives audacieuses
- Laisse ton cœur guider tes actions""",

    ('leo', 2): """# ☉ Transit du Soleil en Lion

**En une phrase :** Tes talents méritent d'être récompensés — fais-toi payer à ta juste valeur.

## L'énergie du moment
Le Soleil en Lion illumine ta Maison 2 des ressources. Tu as conscience de ta valeur et tu veux que les autres la reconnaissent aussi. C'est le moment de demander plus, de te faire payer pour tes talents.

## Ce que tu pourrais vivre
- Un désir de reconnaissance financière pour tes talents
- L'envie de dépenser pour des choses qui reflètent ta valeur
- Une clarification de ce qui compte vraiment à tes yeux

## Conseils pour ce transit
- Demande la rémunération que tu mérites
- Investis dans des choses de qualité qui te représentent
- Reconnais tes talents comme de vraies ressources""",

    ('leo', 3): """# ☉ Transit du Soleil en Lion

**En une phrase :** Ta parole captive — exprime-toi avec flair et autorité.

## L'énergie du moment
Le Soleil en Lion traverse ta Maison 3 de la communication. Tu t'exprimes avec chaleur et assurance. C'est le moment de partager tes idées avec conviction et de captiver ton audience.

## Ce que tu pourrais vivre
- Une communication plus théâtrale et engageante
- L'envie de partager tes créations ou tes idées
- Des échanges où tu es naturellement au centre

## Conseils pour ce transit
- Présente tes idées avec conviction et enthousiasme
- Utilise ta créativité dans ta communication
- N'hésite pas à prendre la parole en public""",

    ('leo', 4): """# ☉ Transit du Soleil en Lion

**En une phrase :** Ton foyer devient ton royaume — règne avec générosité sur ta vie privée.

## L'énergie du moment
Le Soleil en Lion illumine ta Maison 4 du foyer. Tu veux un chez-toi dont tu es fier, un espace qui reflète ta grandeur. C'est le moment de créer un environnement qui te met en valeur.

## Ce que tu pourrais vivre
- L'envie de recevoir et d'impressionner chez toi
- Un besoin de fierté par rapport à ton foyer
- Des moments chaleureux et généreux en famille

## Conseils pour ce transit
- Décore ton intérieur avec des éléments qui te représentent
- Organise des moments conviviaux chez toi
- Sois généreux avec ta famille""",

    ('leo', 5): """# ☉ Transit du Soleil en Lion

**En une phrase :** La joie et la créativité explosent — vis pleinement tes passions.

## L'énergie du moment
Le Soleil en Lion traverse sa propre Maison 5, amplifiant le plaisir, la créativité et l'amour. Tu es dans ton élément pour créer, aimer et t'amuser. C'est ton moment pour briller dans tout ce qui t'apporte de la joie.

## Ce que tu pourrais vivre
- Un élan créatif puissant et inspiré
- Des romances passionnées et dramatiques
- L'envie de t'amuser et de profiter de la vie

## Conseils pour ce transit
- Crée quelque chose qui te rend fier
- En amour, exprime ta passion sans retenue
- Accorde-toi des plaisirs royaux""",

    ('leo', 6): """# ☉ Transit du Soleil en Lion

**En une phrase :** Ton travail mérite d'être reconnu — apporte de l'excellence dans ton quotidien.

## L'énergie du moment
Le Soleil en Lion illumine ta Maison 6 du travail et de la santé. Tu veux exceller dans ce que tu fais et être reconnu pour ton travail. C'est le moment d'apporter de la fierté dans tes tâches quotidiennes.

## Ce que tu pourrais vivre
- Un désir de reconnaissance pour ton travail
- L'envie d'apporter de la créativité dans tes routines
- Une attention à ta vitalité et à ton énergie

## Conseils pour ce transit
- Accomplis tes tâches avec excellence et fierté
- Prends soin de ton cœur et de ta vitalité
- N'hésite pas à montrer tes accomplissements""",

    ('leo', 7): """# ☉ Transit du Soleil en Lion

**En une phrase :** Tes relations brillent — cherche des partenaires qui t'admirent et que tu admires.

## L'énergie du moment
Le Soleil en Lion traverse ta Maison 7 des partenariats. Tu veux des relations où tu brilles et où tu peux être généreux. C'est le moment de chercher des partenaires dignes de toi.

## Ce que tu pourrais vivre
- Un désir de reconnaissance dans tes relations
- L'attirance pour des partenaires charismatiques
- L'envie de montrer votre couple au monde

## Conseils pour ce transit
- Choisis des partenaires qui t'élèvent
- Sois généreux avec ceux que tu aimes
- Montre-toi sous ton meilleur jour dans tes relations""",

    ('leo', 8): """# ☉ Transit du Soleil en Lion

**En une phrase :** Transforme-toi avec panache — ta renaissance mérite d'être célébrée.

## L'énergie du moment
Le Soleil en Lion illumine ta Maison 8 des transformations. Tu abordes les changements profonds avec courage et dignité. C'est le moment de traverser les épreuves en gardant ta fierté.

## Ce que tu pourrais vivre
- Une transformation qui renforce ta confiance
- Des questions financières partagées à clarifier
- L'envie de renaître de façon spectaculaire

## Conseils pour ce transit
- Traverse les crises avec dignité et courage
- Négocie fermement les ressources partagées
- Célèbre tes transformations comme des victoires""",

    ('leo', 9): """# ☉ Transit du Soleil en Lion

**En une phrase :** Ta vision s'élargit avec enthousiasme — explore le monde avec panache.

## L'énergie du moment
Le Soleil en Lion traverse ta Maison 9 des voyages et de la philosophie. Tu as envie de grandes aventures, de voyages mémorables et d'apprentissages qui t'élèvent. C'est le moment de voir grand.

## Ce que tu pourrais vivre
- L'envie de voyager vers des destinations prestigieuses
- Un intérêt pour des philosophies grandioses
- Des opportunités d'enseigner ou de partager ton savoir

## Conseils pour ce transit
- Planifie un voyage qui te fait rêver
- Partage généreusement ce que tu sais
- Vise haut dans tes apprentissages""",

    ('leo', 10): """# ☉ Transit du Soleil en Lion

**En une phrase :** Ta carrière atteint son apogée — brille sur la scène professionnelle.

## L'énergie du moment
Le Soleil en Lion illumine ta Maison 10 de la carrière. Tu es au sommet de ta visibilité professionnelle. C'est le moment de te faire remarquer, de prendre des responsabilités et de montrer ton leadership.

## Ce que tu pourrais vivre
- Une reconnaissance professionnelle importante
- Des opportunités de leadership ou de visibilité
- Le désir d'atteindre le sommet de ton domaine

## Conseils pour ce transit
- Assume un rôle de leader avec confiance
- Fais-toi remarquer par tes accomplissements
- Vise des positions de prestige""",

    ('leo', 11): """# ☉ Transit du Soleil en Lion

**En une phrase :** Tes projets collectifs brillent — inspire les autres par ta vision.

## L'énergie du moment
Le Soleil en Lion traverse ta Maison 11 des amitiés et des projets de groupe. Tu es un leader naturel dans les collectifs, capable d'inspirer et de fédérer. C'est le moment de briller au sein de ton réseau.

## Ce que tu pourrais vivre
- Un rôle de leader dans un groupe ou une association
- Des amitiés avec des personnes influentes
- Des projets collectifs ambitieux et inspirants

## Conseils pour ce transit
- Prends les rênes d'un projet de groupe
- Inspire les autres par ta vision
- Entoure-toi de personnes qui partagent tes ambitions""",

    ('leo', 12): """# ☉ Transit du Soleil en Lion

**En une phrase :** Ta lumière intérieure brille — cultive ta confiance dans l'intimité.

## L'énergie du moment
Le Soleil en Lion illumine ta Maison 12 de l'intériorité. C'est le moment de cultiver ta confiance intérieure, loin des regards. Ta créativité peut s'exprimer dans la solitude et la méditation.

## Ce que tu pourrais vivre
- Un travail sur ta confiance en toi en profondeur
- Une créativité qui s'exprime dans l'intimité
- Des prises de conscience sur ton besoin de reconnaissance

## Conseils pour ce transit
- Cultive ta lumière intérieure sans public
- Médite sur ce qui te rend vraiment fier
- Prépare ta prochaine grande entrée en scène""",

    # VIRGO
    ('virgo', 1): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Tu rayonnes de compétence — montre au monde ton sens du détail et ton efficacité.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Vierge, te rendant plus méthodique, analytique et soucieux de perfection. C'est le moment de te présenter sous ton jour le plus professionnel et compétent.

## Ce que tu pourrais vivre
- Un désir d'amélioration personnelle
- Une attention accrue à ta santé et ton apparence
- Une présence plus réservée mais très efficace

## Conseils pour ce transit
- Affine les détails de ton image
- Montre ta compétence par des actes concrets
- Prends soin de ta santé et de ton hygiène de vie""",

    ('virgo', 2): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Tes finances méritent de l'ordre — analyse et optimise tes ressources.

## L'énergie du moment
Le Soleil en Vierge illumine ta Maison 2 des ressources. Tu as envie de mettre de l'ordre dans tes finances, d'analyser tes dépenses et d'optimiser ta gestion. C'est le moment de faire le ménage financier.

## Ce que tu pourrais vivre
- Un besoin de clarifier ton budget
- L'envie d'économiser et d'être plus efficace
- Une analyse critique de ce qui a vraiment de la valeur

## Conseils pour ce transit
- Fais un bilan détaillé de tes finances
- Élimine les dépenses inutiles
- Développe des compétences monnayables""",

    ('virgo', 3): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Ta communication gagne en précision — analyse et exprime-toi avec clarté.

## L'énergie du moment
Le Soleil en Vierge traverse ta Maison 3 de la communication. Tu t'exprimes de façon plus précise, analytique et pratique. C'est le moment d'apprendre des choses utiles et de communiquer avec efficacité.

## Ce que tu pourrais vivre
- Une communication plus technique et détaillée
- L'envie d'apprendre des compétences pratiques
- Des échanges axés sur la résolution de problèmes

## Conseils pour ce transit
- Vérifie tes informations avant de les partager
- Apprends quelque chose d'utile et pratique
- Aide les autres avec des conseils concrets""",

    ('virgo', 4): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Ton foyer a besoin d'ordre — organise et purifie ton espace de vie.

## L'énergie du moment
Le Soleil en Vierge illumine ta Maison 4 du foyer. Tu ressens le besoin de nettoyer, ranger et organiser ton chez-toi. C'est le moment idéal pour un grand ménage ou des réparations domestiques.

## Ce que tu pourrais vivre
- L'envie de faire un grand tri et de désencombrer
- Un besoin d'hygiène et de propreté chez toi
- Des améliorations pratiques dans ton intérieur

## Conseils pour ce transit
- Fais le tri dans tes affaires
- Répare ce qui doit l'être
- Crée un environnement sain et ordonné""",

    ('virgo', 5): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Ta créativité s'affine — perfectionne tes talents avec patience.

## L'énergie du moment
Le Soleil en Vierge traverse ta Maison 5 de la créativité et des plaisirs. Tu abordes les loisirs et l'amour avec un souci du détail. C'est le moment de perfectionner un talent ou d'être plus sélectif en amour.

## Ce que tu pourrais vivre
- Une créativité orientée vers l'artisanat ou les détails
- Une approche plus analytique de l'amour
- Des plaisirs simples et sains

## Conseils pour ce transit
- Perfectionne une compétence créative
- En amour, sois attentif aux petits gestes
- Offre-toi des plaisirs qui font du bien à ta santé""",

    ('virgo', 6): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Ton quotidien atteint son excellence — optimise tes routines et ta santé.

## L'énergie du moment
Le Soleil en Vierge amplifie l'énergie de ta Maison 6 du travail et de la santé. Tu es dans ton élément pour organiser, améliorer et optimiser. C'est le moment de créer des routines parfaites.

## Ce que tu pourrais vivre
- Une productivité maximale et un sens du détail accru
- Un intérêt pour améliorer ta santé et ton alimentation
- L'envie de perfectionner tes méthodes de travail

## Conseils pour ce transit
- Mets en place des routines efficaces
- Consulte un professionnel de santé si besoin
- Aide tes collègues à s'organiser""",

    ('virgo', 7): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Tes relations demandent de l'analyse — améliore tes partenariats avec discernement.

## L'énergie du moment
Le Soleil en Vierge illumine ta Maison 7 des partenariats. Tu portes un regard plus critique sur tes relations, cherchant à les améliorer. C'est le moment de clarifier les attentes et de résoudre les problèmes.

## Ce que tu pourrais vivre
- Une analyse des forces et faiblesses de tes relations
- L'envie de résoudre des problèmes de couple
- L'attirance pour des partenaires compétents et fiables

## Conseils pour ce transit
- Discute des aspects pratiques de tes relations
- Sois utile et serviable avec ton partenaire
- Évite d'être trop critique ou perfectionniste""",

    ('virgo', 8): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Les transformations se font avec méthode — analyse ce qui doit changer.

## L'énergie du moment
Le Soleil en Vierge traverse ta Maison 8 des transformations. Tu abordes les changements profonds de façon analytique et méthodique. C'est le moment de faire le tri dans ce qui ne te sert plus.

## Ce que tu pourrais vivre
- Une analyse détaillée de tes finances partagées
- Un travail méthodique sur tes blocages
- L'envie de purifier et d'éliminer le superflu

## Conseils pour ce transit
- Fais un audit de tes ressources partagées
- Analyse tes schémas répétitifs avec lucidité
- Élimine ce qui encombre ta vie""",

    ('virgo', 9): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Ta quête de sens se fait pratique — apprends des choses utiles et concrètes.

## L'énergie du moment
Le Soleil en Vierge illumine ta Maison 9 des voyages et de la philosophie. Tu cherches une sagesse applicable, des connaissances utiles et des voyages pratiques. C'est le moment d'apprendre quelque chose de concret.

## Ce que tu pourrais vivre
- Un intérêt pour des formations pratiques
- Des voyages organisés et bien planifiés
- Une philosophie basée sur l'amélioration continue

## Conseils pour ce transit
- Inscris-toi à une formation professionnelle
- Planifie un voyage utile ou éducatif
- Cherche la sagesse dans les détails du quotidien""",

    ('virgo', 10): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Ta carrière brille par ta compétence — montre ton expertise et ton efficacité.

## L'énergie du moment
Le Soleil en Vierge traverse ta Maison 10 de la carrière. Tu es reconnu pour ton travail méticuleux et ta fiabilité. C'est le moment de montrer ton expertise et de résoudre des problèmes professionnels.

## Ce que tu pourrais vivre
- Une reconnaissance pour ta compétence technique
- Des opportunités liées à l'organisation ou l'analyse
- Un désir de perfectionner ton image professionnelle

## Conseils pour ce transit
- Montre ton expertise par des résultats concrets
- Propose des solutions aux problèmes de l'équipe
- Perfectionne tes compétences professionnelles""",

    ('virgo', 11): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Tes projets collectifs gagnent en efficacité — apporte ton sens pratique au groupe.

## L'énergie du moment
Le Soleil en Vierge illumine ta Maison 11 des amitiés et des projets de groupe. Tu contribues aux collectifs par ton sens de l'organisation et ton analyse. C'est le moment d'améliorer les projets de groupe.

## Ce que tu pourrais vivre
- Un rôle d'organisateur dans un groupe
- Des amitiés basées sur l'entraide pratique
- Des projets collectifs axés sur l'amélioration

## Conseils pour ce transit
- Propose des améliorations concrètes aux projets de groupe
- Aide tes amis avec des conseils pratiques
- Rejoins des associations à but utile""",

    ('virgo', 12): """# ☉ Transit du Soleil en Vierge

**En une phrase :** Ton monde intérieur demande de l'ordre — analyse et purifie tes profondeurs.

## L'énergie du moment
Le Soleil en Vierge traverse ta Maison 12 de l'intériorité. C'est le moment de faire le tri dans ton inconscient, d'analyser tes schémas et de purifier ton monde intérieur.

## Ce que tu pourrais vivre
- Un travail d'introspection méthodique
- L'envie de comprendre tes blocages
- Un besoin de solitude pour te recentrer

## Conseils pour ce transit
- Journalise pour analyser tes pensées
- Fais un bilan de l'année écoulée
- Élimine les pensées et habitudes qui ne te servent plus""",

    # LIBRA
    ('libra', 1): """# ☉ Transit du Soleil en Balance

**En une phrase :** Tu rayonnes d'harmonie — montre ta diplomatie et ton sens esthétique.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Balance, te rendant plus charmant, diplomatique et soucieux de l'harmonie. C'est le moment de soigner ton image et de créer des connexions agréables.

## Ce que tu pourrais vivre
- Un souci accru de ton apparence et de ton style
- Une facilité à créer des relations harmonieuses
- Un désir d'équilibre dans tous les domaines

## Conseils pour ce transit
- Soigne ton apparence avec goût
- Utilise ta diplomatie pour résoudre les conflits
- Cherche l'équilibre entre toi et les autres""",

    ('libra', 2): """# ☉ Transit du Soleil en Balance

**En une phrase :** Tes ressources cherchent l'équilibre — harmonise tes finances avec élégance.

## L'énergie du moment
Le Soleil en Balance illumine ta Maison 2 des ressources. Tu cherches l'équilibre financier et l'investissement dans la beauté. C'est le moment de gagner de l'argent grâce à tes talents relationnels ou esthétiques.

## Ce que tu pourrais vivre
- Un équilibrage de ton budget
- Des revenus liés à la relation ou à l'esthétique
- L'envie d'investir dans de belles choses

## Conseils pour ce transit
- Trouve l'équilibre entre dépenses et économies
- Monétise tes talents relationnels ou artistiques
- Investis dans ce qui embellit ta vie""",

    ('libra', 3): """# ☉ Transit du Soleil en Balance

**En une phrase :** Ta communication se fait diplomate — échange avec grâce et équité.

## L'énergie du moment
Le Soleil en Balance traverse ta Maison 3 de la communication. Tu t'exprimes avec tact et équilibre, cherchant à comprendre tous les points de vue. C'est le moment de négocier et de créer des ponts.

## Ce que tu pourrais vivre
- Des conversations équilibrées et respectueuses
- L'envie d'apprendre des sujets liés à l'art ou aux relations
- Un rôle de médiateur dans ton entourage

## Conseils pour ce transit
- Écoute tous les points de vue avant de parler
- Apprends quelque chose lié à l'art ou à la communication
- Utilise ta diplomatie pour faciliter les échanges""",

    ('libra', 4): """# ☉ Transit du Soleil en Balance

**En une phrase :** Ton foyer cherche l'harmonie — crée un espace de paix et de beauté.

## L'énergie du moment
Le Soleil en Balance illumine ta Maison 4 du foyer. Tu veux un chez-toi harmonieux, beau et paisible. C'est le moment de décorer avec goût et de créer une ambiance équilibrée.

## Ce que tu pourrais vivre
- Un besoin d'harmonie dans ta vie familiale
- L'envie d'embellir ton intérieur
- Des efforts pour maintenir la paix à la maison

## Conseils pour ce transit
- Décore ton intérieur avec goût et équilibre
- Favorise le dialogue en famille
- Crée un espace de paix chez toi""",

    ('libra', 5): """# ☉ Transit du Soleil en Balance

**En une phrase :** L'amour et la beauté t'appellent — vis des romances élégantes et crée avec grâce.

## L'énergie du moment
Le Soleil en Balance traverse ta Maison 5 de la créativité et de l'amour. Tu es attiré par les relations raffinées, la créativité artistique et les plaisirs élégants. C'est le moment de vivre l'amour avec grâce.

## Ce que tu pourrais vivre
- Des romances romantiques et équilibrées
- Une créativité orientée vers les arts visuels
- Des plaisirs raffinés et sociaux

## Conseils pour ce transit
- Crée quelque chose de beau et harmonieux
- En amour, cherche l'équilibre et le respect mutuel
- Offre-toi des sorties culturelles ou artistiques""",

    ('libra', 6): """# ☉ Transit du Soleil en Balance

**En une phrase :** Ton quotidien cherche l'équilibre — harmonise travail et bien-être.

## L'énergie du moment
Le Soleil en Balance illumine ta Maison 6 du travail et de la santé. Tu cherches l'équilibre entre effort et repos, travail et plaisir. C'est le moment d'améliorer l'ambiance au travail.

## Ce que tu pourrais vivre
- Un besoin d'harmonie dans ton environnement de travail
- L'envie d'équilibrer ta vie professionnelle et personnelle
- Une attention à l'esthétique de ton espace de travail

## Conseils pour ce transit
- Crée un environnement de travail agréable
- Trouve un équilibre entre travail et repos
- Améliore tes relations avec tes collègues""",

    ('libra', 7): """# ☉ Transit du Soleil en Balance

**En une phrase :** Tes relations sont au centre de tout — cultive des partenariats équilibrés.

## L'énergie du moment
Le Soleil en Balance amplifie l'énergie de ta Maison 7 des partenariats. Les relations sont au premier plan, que ce soit en amour ou en affaires. C'est le moment de t'engager ou de rééquilibrer tes partenariats.

## Ce que tu pourrais vivre
- Un désir profond de partenariat harmonieux
- Des opportunités de mariage ou d'association
- Un travail sur l'équilibre dans tes relations

## Conseils pour ce transit
- Investis dans tes relations importantes
- Cherche l'équilibre entre donner et recevoir
- Engage-toi si le moment est venu""",

    ('libra', 8): """# ☉ Transit du Soleil en Balance

**En une phrase :** Les transformations cherchent l'équilibre — traverse les changements avec grâce.

## L'énergie du moment
Le Soleil en Balance traverse ta Maison 8 des transformations. Tu abordes les changements profonds en cherchant l'équilibre et l'harmonie. C'est le moment de négocier les questions financières partagées.

## Ce que tu pourrais vivre
- Des négociations autour des ressources partagées
- Un besoin d'équilibre face aux transformations
- Une approche diplomatique des sujets délicats

## Conseils pour ce transit
- Négocie équitablement les questions financières
- Aborde les transformations avec grâce
- Cherche l'harmonie même dans les moments intenses""",

    ('libra', 9): """# ☉ Transit du Soleil en Balance

**En une phrase :** Ta quête de sens passe par l'autre — explore la sagesse de l'équilibre.

## L'énergie du moment
Le Soleil en Balance illumine ta Maison 9 des voyages et de la philosophie. Tu es attiré par les cultures qui valorisent l'harmonie, les voyages à deux et les philosophies de l'équilibre.

## Ce que tu pourrais vivre
- Des voyages romantiques ou culturels
- Un intérêt pour les philosophies orientales ou l'art
- Des échanges enrichissants avec des étrangers

## Conseils pour ce transit
- Voyage avec un partenaire
- Explore des philosophies qui prônent l'équilibre
- Visite des musées ou des lieux d'art""",

    ('libra', 10): """# ☉ Transit du Soleil en Balance

**En une phrase :** Ta carrière brille par tes relations — utilise ta diplomatie professionnellement.

## L'énergie du moment
Le Soleil en Balance traverse ta Maison 10 de la carrière. Tu es reconnu pour tes talents relationnels et ta capacité à créer l'harmonie. C'est le moment de briller grâce à ta diplomatie.

## Ce que tu pourrais vivre
- Des opportunités liées aux relations publiques
- Une reconnaissance pour ta capacité à fédérer
- Un partenariat professionnel important

## Conseils pour ce transit
- Utilise tes talents de médiateur au travail
- Soigne ton image professionnelle
- Développe tes partenariats d'affaires""",

    ('libra', 11): """# ☉ Transit du Soleil en Balance

**En une phrase :** Tes amitiés s'harmonisent — cultive des relations sociales équilibrées.

## L'énergie du moment
Le Soleil en Balance illumine ta Maison 11 des amitiés et des projets de groupe. Tu excelles dans les relations sociales et les collaborations équilibrées. C'est le moment de tisser des liens harmonieux.

## Ce que tu pourrais vivre
- Une vie sociale riche et équilibrée
- Des projets de groupe basés sur la collaboration
- Des amitiés mutuellement bénéfiques

## Conseils pour ce transit
- Cultive des amitiés réciproques
- Participe à des événements culturels ou artistiques
- Apporte l'harmonie dans les projets collectifs""",

    ('libra', 12): """# ☉ Transit du Soleil en Balance

**En une phrase :** Ton monde intérieur cherche l'équilibre — médite sur l'harmonie profonde.

## L'énergie du moment
Le Soleil en Balance traverse ta Maison 12 de l'intériorité. Tu cherches l'équilibre intérieur, la paix profonde et l'harmonie avec l'invisible. C'est le moment de méditer sur ce qui crée la sérénité.

## Ce que tu pourrais vivre
- Un travail sur l'équilibre intérieur
- Le besoin de paix et de solitude harmonieuse
- Des rêves liés aux relations ou à la beauté

## Conseils pour ce transit
- Médite sur l'équilibre entre donner et recevoir
- Crée un espace de paix pour ton introspection
- Explore tes besoins relationnels inconscients""",

    # SCORPIO
    ('scorpio', 1): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Tu rayonnes d'intensité — montre ta profondeur et ta puissance.

## L'énergie du moment
Le Soleil traverse ta Maison 1 en Scorpion, te donnant une présence magnétique et intense. C'est le moment de t'affirmer avec puissance et d'assumer ta profondeur.

## Ce que tu pourrais vivre
- Une intensité accrue dans ta présence
- Un regard plus pénétrant sur les gens et les situations
- Un besoin de transformation personnelle

## Conseils pour ce transit
- Assume ta profondeur sans t'excuser
- Utilise ton magnétisme avec discernement
- Transforme-toi en profondeur""",

    ('scorpio', 2): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Tes ressources demandent une transformation — creuse dans tes finances avec intensité.

## L'énergie du moment
Le Soleil en Scorpion illumine ta Maison 2 des ressources. Tu es prêt à creuser profondément dans tes finances, à éliminer le superflu et à transformer ton rapport à l'argent.

## Ce que tu pourrais vivre
- Un regard sans concession sur tes finances
- Des opportunités dans des domaines liés à la transformation
- L'envie de te libérer de dépendances matérielles

## Conseils pour ce transit
- Fais un audit profond de tes ressources
- Élimine les dépenses qui t'enchaînent
- Investis dans ce qui te transforme""",

    ('scorpio', 3): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Ta communication devient pénétrante — va au fond des choses dans tes échanges.

## L'énergie du moment
Le Soleil en Scorpion traverse ta Maison 3 de la communication. Tu communiques avec profondeur et intensité, cherchant la vérité derrière les mots. C'est le moment d'avoir des conversations qui comptent.

## Ce que tu pourrais vivre
- Des conversations intenses et révélatrices
- L'envie d'enquêter ou de rechercher la vérité
- Des échanges qui transforment

## Conseils pour ce transit
- Pose les questions qui vont au fond des choses
- Écoute ce qui n'est pas dit
- Transforme tes schémas de communication""",

    ('scorpio', 4): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Ton foyer vit une transformation — explore les profondeurs de ta vie privée.

## L'énergie du moment
Le Soleil en Scorpion illumine ta Maison 4 du foyer. Des transformations profondes touchent ta vie familiale ou ton chez-toi. C'est le moment de guérir des vieilles blessures familiales.

## Ce que tu pourrais vivre
- Des révélations ou des secrets familiaux qui émergent
- Un besoin de transformer ton espace de vie
- Des émotions intenses liées au passé

## Conseils pour ce transit
- Explore tes racines avec courage
- Transforme ton chez-toi en profondeur
- Libère-toi des héritages émotionnels lourds""",

    ('scorpio', 5): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** L'amour devient passion — vis des expériences créatives et amoureuses intenses.

## L'énergie du moment
Le Soleil en Scorpion traverse ta Maison 5 de la créativité et de l'amour. Tu vis l'amour avec passion et profondeur. Ta créativité peut explorer des thèmes intenses ou tabous.

## Ce que tu pourrais vivre
- Des amours passionnées et transformatrices
- Une créativité qui explore les profondeurs
- Des plaisirs intenses et mémorables

## Conseils pour ce transit
- Vis l'amour avec intensité mais conscience
- Crée quelque chose qui vient de tes profondeurs
- Explore les plaisirs qui te transforment""",

    ('scorpio', 6): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Ton quotidien se transforme — élimine ce qui ne sert plus dans tes routines.

## L'énergie du moment
Le Soleil en Scorpion illumine ta Maison 6 du travail et de la santé. Tu es prêt à transformer radicalement tes habitudes, à éliminer ce qui nuit à ta santé ou à ton efficacité.

## Ce que tu pourrais vivre
- Une purge de tes routines inefficaces
- Un travail en profondeur sur ta santé
- Des changements importants au travail

## Conseils pour ce transit
- Élimine les habitudes qui te tirent vers le bas
- Travaille sur les causes profondes de tes problèmes de santé
- Transforme ton approche du travail""",

    ('scorpio', 7): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Tes relations s'intensifient — vis des partenariats transformateurs.

## L'énergie du moment
Le Soleil en Scorpion traverse ta Maison 7 des partenariats. Tes relations deviennent plus intenses, plus profondes. C'est le moment de transformer tes partenariats ou d'attirer des personnes puissantes.

## Ce que tu pourrais vivre
- Des relations intenses et transformatrices
- Des révélations dans tes partenariats existants
- L'attirance pour des personnes magnétiques

## Conseils pour ce transit
- Approfondis tes relations avec courage
- Sois prêt à des transformations relationnelles
- Évite les jeux de pouvoir dans tes partenariats""",

    ('scorpio', 8): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Tu es au cœur de la transformation — plonge dans tes profondeurs avec puissance.

## L'énergie du moment
Le Soleil en Scorpion amplifie ta Maison 8, son domicile naturel. Tu es au maximum de ton pouvoir de transformation, prêt à mourir et renaître. C'est le moment des changements radicaux.

## Ce que tu pourrais vivre
- Une transformation profonde et puissante
- Des révélations sur tes mécanismes cachés
- Des opportunités financières liées aux autres

## Conseils pour ce transit
- Accueille les transformations sans résistance
- Explore tes profondeurs avec courage
- Libère ce qui doit mourir pour renaître""",

    ('scorpio', 9): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Ta quête de sens s'intensifie — explore les mystères de l'existence.

## L'énergie du moment
Le Soleil en Scorpion illumine ta Maison 9 des voyages et de la philosophie. Tu es attiré par les enseignements profonds, les voyages transformateurs et les sagesses qui touchent aux mystères de la vie.

## Ce que tu pourrais vivre
- Un intérêt pour les sciences occultes ou la psychologie
- Des voyages qui te transforment en profondeur
- Des remises en question profondes de tes croyances

## Conseils pour ce transit
- Explore des enseignements qui vont en profondeur
- Voyage vers des lieux chargés d'histoire ou de mystère
- Remets en question tes croyances superficielles""",

    ('scorpio', 10): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Ta carrière se transforme — utilise ton pouvoir avec sagesse.

## L'énergie du moment
Le Soleil en Scorpion traverse ta Maison 10 de la carrière. Tu es prêt à transformer ta position professionnelle, à prendre le pouvoir ou à changer radicalement de direction.

## Ce que tu pourrais vivre
- Des transformations importantes dans ta carrière
- Une montée en puissance professionnelle
- Des opportunités dans des domaines liés à la transformation

## Conseils pour ce transit
- Utilise ton pouvoir professionnel avec sagesse
- Prépare-toi à des changements de carrière
- Fais preuve de stratégie dans tes ambitions""",

    ('scorpio', 11): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Tes projets collectifs s'intensifient — transforme le monde avec tes alliés.

## L'énergie du moment
Le Soleil en Scorpion illumine ta Maison 11 des amitiés et des projets de groupe. Tu attires des alliés puissants et participes à des projets transformateurs. C'est le moment de t'engager pour des causes profondes.

## Ce que tu pourrais vivre
- Des amitiés intenses et transformatrices
- Des projets collectifs qui touchent aux tabous
- Un rôle de catalyseur dans les groupes

## Conseils pour ce transit
- Choisis des alliés authentiques et puissants
- Engage-toi dans des causes qui transforment
- Utilise ton influence pour le changement""",

    ('scorpio', 12): """# ☉ Transit du Soleil en Scorpion

**En une phrase :** Tes profondeurs t'appellent — explore l'inconscient avec puissance.

## L'énergie du moment
Le Soleil en Scorpion traverse ta Maison 12 de l'intériorité. Tu es invité à plonger dans tes profondeurs inconscientes, à affronter tes démons et à te transformer de l'intérieur.

## Ce que tu pourrais vivre
- Des prises de conscience profondes
- Des rêves révélateurs et intenses
- Un travail puissant sur l'inconscient

## Conseils pour ce transit
- Médite sur tes ombres avec courage
- Consulte un thérapeute si besoin
- Prépare une renaissance intérieure""",
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
