#!/usr/bin/env python3
"""
Insert transit_north_node interpretations V2 for Aries, Taurus, Gemini, Cancer (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_NORTH_NODE_INTERPRETATIONS = {
    # ============== ARIES ==============
    ('aries', 1): """# ☊ Nœud Nord en Bélier – Maison I

**En une phrase :** L'univers t'invite à affirmer qui tu es vraiment et à oser prendre les devants.

## L'énergie du moment
Le Nœud Nord en Bélier dans ta maison I marque une période karmique majeure. Tu es appelé(e) à développer ton identité propre, ton courage et ton leadership personnel. C'est le moment de sortir de la dépendance aux autres et de te définir par toi-même.

## Ce que tu pourrais vivre
- Un besoin impérieux de te réinventer et de redéfinir ton image
- Des situations qui exigent que tu prennes position et défendes tes choix
- Une envie de pionnier, de démarrer des projets solo

## Conseils pour ce transit
- Ose être égoïste au sens positif : pense à toi d'abord
- Initie des actions sans attendre la validation des autres
- Travaille ta confiance physique et ton assertivité""",

    ('aries', 2): """# ☊ Nœud Nord en Bélier – Maison II

**En une phrase :** Ta mission karmique passe par l'affirmation de tes valeurs et l'autonomie financière.

## L'énergie du moment
Le Nœud Nord en Bélier active ta maison des ressources. Tu es invité(e) à conquérir ton indépendance matérielle avec audace. Fini de dépendre des autres pour ta sécurité – c'est toi qui dois créer ta propre abondance.

## Ce que tu pourrais vivre
- Des opportunités pour augmenter tes revenus par ta propre initiative
- Un désir de clarifier ce qui a vraiment de la valeur pour toi
- Des défis qui testent ton rapport à l'argent et à l'estime de soi

## Conseils pour ce transit
- Lance-toi dans des projets qui valorisent tes talents uniques
- Affirme tes tarifs et ta valeur sans te sous-estimer
- Développe une relation saine et autonome avec l'argent""",

    ('aries', 3): """# ☊ Nœud Nord en Bélier – Maison III

**En une phrase :** Tu es appelé(e) à communiquer avec audace et à défendre tes idées.

## L'énergie du moment
Le Nœud Nord en Bélier dynamise ta maison de la communication. Ta croissance passe par l'expression directe et franche de tes pensées. Plus question de tourner autour du pot ou de te censurer pour plaire.

## Ce que tu pourrais vivre
- Un besoin de parler vrai, même si ça dérange
- Des discussions stimulantes où tu dois défendre ton point de vue
- Une envie d'apprendre de nouvelles compétences rapidement

## Conseils pour ce transit
- Exprime tes opinions sans attendre l'approbation générale
- Ose prendre la parole en premier dans les échanges
- Explore de nouvelles façons d'apprendre et de transmettre""",

    ('aries', 4): """# ☊ Nœud Nord en Bélier – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer ton propre foyer et tes racines avec courage.

## L'énergie du moment
Le Nœud Nord en Bélier dans ta maison des racines indique que ta croissance passe par l'affirmation de ton espace personnel. Tu dois définir ce que "chez toi" signifie vraiment, indépendamment des traditions familiales.

## Ce que tu pourrais vivre
- Un besoin de créer un foyer qui te ressemble vraiment
- Des situations où tu dois t'affirmer face à ta famille
- Une envie de couper certains liens pour mieux te construire

## Conseils pour ce transit
- Prends l'initiative dans les questions familiales ou domestiques
- Ose rompre avec les traditions qui ne te correspondent plus
- Construis ta sécurité intérieure par toi-même""",

    ('aries', 5): """# ☊ Nœud Nord en Bélier – Maison V

**En une phrase :** L'univers t'invite à exprimer ta créativité et ta joie de vivre sans retenue.

## L'énergie du moment
Le Nœud Nord en Bélier illumine ta maison de la créativité. Tu es appelé(e) à oser créer, aimer et t'amuser avec passion. C'est le moment de sortir de ta zone de confort pour briller de ta propre lumière.

## Ce que tu pourrais vivre
- Une explosion créative qui demande à s'exprimer
- Des histoires d'amour passionnées ou un renouveau romantique
- Un désir de prendre des risques créatifs ou artistiques

## Conseils pour ce transit
- Lance-toi dans un projet créatif qui t'enflamme
- Ose séduire et exprimer tes désirs amoureux
- Joue, amuse-toi, retrouve ton âme d'enfant aventurier""",

    ('aries', 6): """# ☊ Nœud Nord en Bélier – Maison VI

**En une phrase :** Ta croissance karmique passe par l'affirmation de toi au quotidien et dans ton travail.

## L'énergie du moment
Le Nœud Nord en Bélier active ta maison du travail quotidien. Tu es invité(e) à prendre les commandes de ta routine, de ta santé et de ton organisation. Fini de subir – c'est toi qui décides comment tu vis au jour le jour.

## Ce que tu pourrais vivre
- Un besoin de transformer radicalement tes habitudes
- Des opportunités de leadership dans ton travail quotidien
- Une envie de prendre ta santé en main de façon active

## Conseils pour ce transit
- Initie des changements dans ta routine sans attendre
- Affirme tes besoins et limites au travail
- Adopte une approche proactive de ta santé""",

    ('aries', 7): """# ☊ Nœud Nord en Bélier – Maison VII

**En une phrase :** Ta mission karmique t'invite à rester toi-même tout en étant en relation.

## L'énergie du moment
Le Nœud Nord en Bélier dans ta maison des partenariats crée un paradoxe fécond. Tu dois apprendre à être pleinement toi-même au sein de tes relations, sans te perdre pour faire plaisir aux autres.

## Ce que tu pourrais vivre
- Des relations qui te poussent à t'affirmer davantage
- Des négociations où tu dois défendre tes intérêts
- Une redéfinition de ce que tu attends d'un partenariat

## Conseils pour ce transit
- Reste authentique même au sein du couple ou des associations
- Ose dire non et poser tes conditions dans les relations
- Cherche des partenaires qui respectent ton indépendance""",

    ('aries', 8): """# ☊ Nœud Nord en Bélier – Maison VIII

**En une phrase :** Tu es appelé(e) à affronter tes peurs et tes zones d'ombre avec courage.

## L'énergie du moment
Le Nœud Nord en Bélier plonge dans ta maison des transformations profondes. Ta croissance passe par le courage de regarder en face ce qui te fait peur : intimité, mort symbolique, ressources partagées. C'est en osant que tu te transformes.

## Ce que tu pourrais vivre
- Des situations qui te forcent à affronter tes tabous
- Des questions d'héritage, de partage ou de dette karmique
- Une transformation intérieure majeure par le courage

## Conseils pour ce transit
- Affronte ce que tu as tendance à éviter
- Prends l'initiative dans les questions financières partagées
- Ose l'intimité vraie sans te cacher""",

    ('aries', 9): """# ☊ Nœud Nord en Bélier – Maison IX

**En une phrase :** L'univers t'invite à explorer de nouveaux horizons et défendre tes convictions.

## L'énergie du moment
Le Nœud Nord en Bélier dynamise ta maison de l'expansion. Tu es appelé(e) à partir à l'aventure, physiquement ou intellectuellement, et à affirmer ta propre philosophie de vie. C'est le moment de devenir le pionnier de tes croyances.

## Ce que tu pourrais vivre
- Une envie irrésistible de voyager ou d'explorer l'inconnu
- Des débats philosophiques où tu dois tenir ta position
- Un appel à enseigner ou partager ta vision unique

## Conseils pour ce transit
- Ose voyager seul(e) ou vers des destinations audacieuses
- Défends tes convictions même face à l'opposition
- Lance-toi dans des études ou enseignements qui t'inspirent""",

    ('aries', 10): """# ☊ Nœud Nord en Bélier – Maison X

**En une phrase :** Ta mission de vie t'appelle à devenir un leader dans ta carrière.

## L'énergie du moment
Le Nœud Nord en Bélier culmine dans ta maison de la carrière. C'est un appel puissant à prendre ta place au sommet, à devenir le pionnier de ton domaine. Ta croissance karmique passe par l'ambition et le leadership.

## Ce que tu pourrais vivre
- Des opportunités de prendre les commandes professionnelles
- Une envie de créer ta propre voie plutôt que de suivre celle des autres
- Une reconnaissance publique de ton courage et tes initiatives

## Conseils pour ce transit
- Vise haut et ose demander ce que tu mérites
- Crée ton propre chemin professionnel
- Accepte les responsabilités de leader avec confiance""",

    ('aries', 11): """# ☊ Nœud Nord en Bélier – Maison XI

**En une phrase :** Tu es invité(e) à affirmer ton individualité au sein des groupes et projets collectifs.

## L'énergie du moment
Le Nœud Nord en Bélier active ta maison des amitiés et projets futurs. Ta mission est d'apporter ta vision unique aux causes collectives, d'être le pionnier qui inspire le groupe plutôt que de te fondre dans la masse.

## Ce que tu pourrais vivre
- Un rôle de leader ou d'initiateur dans des associations
- Des amitiés qui valorisent ton individualité
- Des projets collectifs où tu dois prendre les devants

## Conseils pour ce transit
- Ose proposer tes idées innovantes au groupe
- Choisis des cercles qui célèbrent ton unicité
- Initie des projets qui servent une cause plus grande""",

    ('aries', 12): """# ☊ Nœud Nord en Bélier – Maison XII

**En une phrase :** Ta croissance karmique passe par le courage d'explorer ton monde intérieur.

## L'énergie du moment
Le Nœud Nord en Bélier se glisse dans ta maison de l'invisible. Tu es appelé(e) à être un pionnier de ton inconscient, à affronter courageusement tes peurs cachées et tes schémas karmiques. C'est une quête spirituelle qui demande de l'audace.

## Ce que tu pourrais vivre
- Un besoin de solitude active pour te reconnecter à toi
- Des révélations sur tes vies passées ou ton karma
- Une transformation spirituelle par le courage intérieur

## Conseils pour ce transit
- Explore activement ton inconscient par la méditation ou thérapie
- Affronte tes peurs les plus profondes avec bravoure
- Trouve le courage dans le silence et l'introspection""",

    # ============== TAURUS ==============
    ('taurus', 1): """# ☊ Nœud Nord en Taureau – Maison I

**En une phrase :** L'univers t'invite à incarner la stabilité, la sensualité et la valeur personnelle.

## L'énergie du moment
Le Nœud Nord en Taureau dans ta maison I t'appelle à développer ton ancrage physique et ta présence tranquille. Ta croissance passe par la patience, la constance et la connexion à tes sens. C'est le moment de devenir ton propre roc.

## Ce que tu pourrais vivre
- Un besoin de ralentir et d'habiter pleinement ton corps
- Une redéfinition de ton image vers plus d'authenticité et de stabilité
- Des situations qui testent ta capacité à rester ancré(e)

## Conseils pour ce transit
- Cultive la patience et la persévérance comme forces
- Reconnecte-toi à tes sens et au plaisir simple d'exister
- Construis une image de toi basée sur tes vraies valeurs""",

    ('taurus', 2): """# ☊ Nœud Nord en Taureau – Maison II

**En une phrase :** Ta mission karmique te guide vers la construction d'une sécurité matérielle durable.

## L'énergie du moment
Le Nœud Nord en Taureau est chez lui dans ta maison des ressources. C'est un appel puissant à bâtir ta richesse patiemment, à développer tes talents et à créer une fondation matérielle solide. La prospérité vient par la constance.

## Ce que tu pourrais vivre
- Des opportunités de construire une richesse durable
- Un clarification profonde de tes valeurs et priorités
- Une réconciliation avec l'argent et les plaisirs matériels

## Conseils pour ce transit
- Investis dans des projets à long terme
- Développe tes talents naturels comme source de revenus
- Apprends à apprécier et gérer sagement ce que tu possèdes""",

    ('taurus', 3): """# ☊ Nœud Nord en Taureau – Maison III

**En une phrase :** Tu es appelé(e) à communiquer avec calme, méthode et profondeur.

## L'énergie du moment
Le Nœud Nord en Taureau apaise ta maison de la communication. Ta croissance passe par une parole posée, réfléchie, qui dit les choses essentielles. Moins de dispersion, plus de substance dans tes échanges.

## Ce que tu pourrais vivre
- Un besoin de simplifier ta communication
- Des apprentissages qui demandent patience et pratique
- Des relations fraternelles ou de voisinage plus stables

## Conseils pour ce transit
- Prends le temps de réfléchir avant de parler
- Apprends en profondeur plutôt qu'en surface
- Cultive des échanges nourrissants et durables""",

    ('taurus', 4): """# ☊ Nœud Nord en Taureau – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un foyer stable et ressourçant.

## L'énergie du moment
Le Nœud Nord en Taureau ancre profondément ta maison des racines. Tu es appelé(e) à construire un vrai chez-toi, un sanctuaire de paix et de beauté. La sécurité intérieure vient d'un ancrage physique réel.

## Ce que tu pourrais vivre
- Un désir profond de t'enraciner quelque part
- L'envie de créer un intérieur beau et confortable
- Une réconciliation avec ton histoire familiale

## Conseils pour ce transit
- Investis dans ton habitat avec soin et patience
- Crée des rituels domestiques nourrissants
- Plante des racines là où tu te sens vraiment chez toi""",

    ('taurus', 5): """# ☊ Nœud Nord en Taureau – Maison V

**En une phrase :** L'univers t'invite à savourer les plaisirs créatifs et amoureux avec constance.

## L'énergie du moment
Le Nœud Nord en Taureau illumine ta maison de la joie. Ta croissance passe par l'appréciation sensuelle de la vie, une créativité patiente et des amours stables. C'est le moment de cultiver le bonheur durable plutôt que l'excitation passagère.

## Ce que tu pourrais vivre
- Une créativité qui s'épanouit dans la durée
- Des relations amoureuses qui se construisent patiemment
- Un rapport au plaisir plus ancré et satisfaisant

## Conseils pour ce transit
- Crée avec tes mains, reconnecte-toi au faire artisanal
- Construis des relations amoureuses sur des bases solides
- Savoure chaque moment de joie pleinement""",

    ('taurus', 6): """# ☊ Nœud Nord en Taureau – Maison VI

**En une phrase :** Ta croissance karmique passe par une routine stable et un travail concret.

## L'énergie du moment
Le Nœud Nord en Taureau structure ta maison du quotidien. Tu es invité(e) à créer des habitudes durables, un travail qui a du sens et une santé fondée sur la régularité. La constance quotidienne devient ta force.

## Ce que tu pourrais vivre
- Une transformation positive de tes routines
- Un travail plus stable ou plus en lien avec tes valeurs
- Une amélioration de santé par des habitudes constantes

## Conseils pour ce transit
- Construis des routines simples mais durables
- Choisis un travail qui correspond à tes valeurs profondes
- Prends soin de ton corps avec régularité et douceur""",

    ('taurus', 7): """# ☊ Nœud Nord en Taureau – Maison VII

**En une phrase :** Ta mission karmique t'invite à construire des relations stables et fidèles.

## L'énergie du moment
Le Nœud Nord en Taureau stabilise ta maison des partenariats. Tu es appelé(e) à développer des relations durables, basées sur la confiance et le respect mutuel. La fidélité et la patience deviennent tes alliées relationnelles.

## Ce que tu pourrais vivre
- Des relations qui se solidifient avec le temps
- Un besoin de stabilité et de sécurité en amour
- Des partenariats professionnels durables et fructueux

## Conseils pour ce transit
- Investis du temps dans tes relations importantes
- Privilégie la qualité à la quantité dans tes liens
- Construis la confiance par la constance et la fiabilité""",

    ('taurus', 8): """# ☊ Nœud Nord en Taureau – Maison VIII

**En une phrase :** Tu es appelé(e) à trouver la paix dans les transformations et l'intimité.

## L'énergie du moment
Le Nœud Nord en Taureau apaise ta maison des profondeurs. Ta croissance passe par une approche sereine des questions d'intimité, de mort symbolique et de ressources partagées. La stabilité émotionnelle devient ton ancre dans les tempêtes.

## Ce que tu pourrais vivre
- Une capacité accrue à traverser les crises avec calme
- Des questions financières partagées qui se stabilisent
- Une intimité plus profonde et plus sereine

## Conseils pour ce transit
- Aborde les transformations avec patience plutôt que peur
- Simplifie tes affaires financières partagées
- Cultive une intimité basée sur la confiance profonde""",

    ('taurus', 9): """# ☊ Nœud Nord en Taureau – Maison IX

**En une phrase :** L'univers t'invite à ancrer ta spiritualité dans le concret et le vécu.

## L'énergie du moment
Le Nœud Nord en Taureau tempère ta maison de l'expansion. Ta croissance philosophique passe par l'incarnation : une spiritualité vécue dans le corps, des croyances pratiques, une sagesse qui se vit au quotidien.

## Ce que tu pourrais vivre
- Une envie de spiritualité plus incarnée et pratique
- Des voyages vers des lieux de beauté naturelle
- Un enseignement ou apprentissage qui prend son temps

## Conseils pour ce transit
- Ancre tes croyances dans l'expérience concrète
- Voyage pour te ressourcer plutôt que pour accumuler
- Partage une sagesse simple et applicable""",

    ('taurus', 10): """# ☊ Nœud Nord en Taureau – Maison X

**En une phrase :** Ta mission de vie t'appelle à bâtir une carrière solide et alignée avec tes valeurs.

## L'énergie du moment
Le Nœud Nord en Taureau couronne ta maison de la carrière. Tu es appelé(e) à construire patiemment une position professionnelle stable, reconnue et en accord avec tes valeurs. Le succès vient par la persévérance.

## Ce que tu pourrais vivre
- Une carrière qui se construit solidement dans la durée
- Une reconnaissance pour ta fiabilité et ta constance
- Des responsabilités qui correspondent à tes vraies valeurs

## Conseils pour ce transit
- Bâtis ta réputation sur la qualité et la durabilité
- Choisis une voie professionnelle alignée avec tes valeurs
- Sois patient(e) : le succès vient avec le temps""",

    ('taurus', 11): """# ☊ Nœud Nord en Taureau – Maison XI

**En une phrase :** Tu es invité(e) à apporter stabilité et valeur aux projets collectifs.

## L'énergie du moment
Le Nœud Nord en Taureau ancre ta maison des amitiés et des idéaux. Ta mission est d'apporter du concret et de la durabilité aux causes que tu défends. Tes amitiés doivent être fidèles et tes projets, réalistes.

## Ce que tu pourrais vivre
- Des amitiés qui durent et s'approfondissent
- Des projets collectifs qui prennent forme concrètement
- Un rôle de stabilisateur dans les groupes

## Conseils pour ce transit
- Choisis des amis sur la base de valeurs partagées
- Contribue concrètement aux causes qui te tiennent à cœur
- Apporte de la constance aux projets collectifs""",

    ('taurus', 12): """# ☊ Nœud Nord en Taureau – Maison XII

**En une phrase :** Ta croissance karmique passe par la paix intérieure et l'ancrage spirituel.

## L'énergie du moment
Le Nœud Nord en Taureau apaise ta maison de l'invisible. Tu es appelé(e) à trouver la sérénité dans ta vie spirituelle, à ancrer ton rapport au divin dans le corps et les sens. La paix intérieure devient ton trésor.

## Ce que tu pourrais vivre
- Une méditation plus incarnée et paisible
- Des révélations qui apportent calme et certitude
- Un lâcher-prise serein sur les peurs anciennes

## Conseils pour ce transit
- Pratique une spiritualité qui honore le corps
- Trouve le sacré dans les plaisirs simples de la vie
- Cultive la paix intérieure comme fondation de tout""",

    # ============== GEMINI ==============
    ('gemini', 1): """# ☊ Nœud Nord en Gémeaux – Maison I

**En une phrase :** L'univers t'invite à développer ta curiosité, ta communication et ta versatilité.

## L'énergie du moment
Le Nœud Nord en Gémeaux dans ta maison I t'appelle à devenir un être de communication et d'échanges. Ta croissance passe par la curiosité, l'ouverture d'esprit et la capacité à t'adapter. C'est le moment d'embrasser ta nature multiple.

## Ce que tu pourrais vivre
- Un besoin d'apprendre, d'échanger, de communiquer
- Une redéfinition de ton identité vers plus de légèreté
- Des rencontres stimulantes qui élargissent tes horizons

## Conseils pour ce transit
- Cultive ta curiosité comme une force vitale
- Ose changer d'avis et explorer plusieurs identités
- Communique, échange, connecte-toi avec les autres""",

    ('gemini', 2): """# ☊ Nœud Nord en Gémeaux – Maison II

**En une phrase :** Ta mission karmique te guide vers la diversification de tes ressources et talents.

## L'énergie du moment
Le Nœud Nord en Gémeaux active ta maison des ressources. Tu es invité(e) à développer plusieurs sources de revenus, à valoriser ta polyvalence. L'abondance vient par l'intelligence et l'adaptabilité.

## Ce que tu pourrais vivre
- Des opportunités de revenus variées et intellectuelles
- Un questionnement sur ce qui a vraiment de la valeur pour toi
- Des talents de communication qui deviennent sources de richesse

## Conseils pour ce transit
- Diversifie tes sources de revenus
- Monétise tes compétences en communication
- Reste flexible dans ta gestion financière""",

    ('gemini', 3): """# ☊ Nœud Nord en Gémeaux – Maison III

**En une phrase :** Tu es appelé(e) à devenir un maître de la communication et des échanges.

## L'énergie du moment
Le Nœud Nord en Gémeaux est chez lui dans ta maison de la communication. C'est un appel puissant à développer tes talents d'expression, d'apprentissage et de connexion. Ta parole et ta plume deviennent des outils de croissance.

## Ce que tu pourrais vivre
- Une explosion de créativité verbale et écrite
- Des opportunités d'apprentissage passionnantes
- Des liens fraternels ou de voisinage enrichissants

## Conseils pour ce transit
- Écris, parle, partage tes idées sans retenue
- Apprends de nouvelles compétences avec enthousiasme
- Cultive un réseau de contacts stimulants""",

    ('gemini', 4): """# ☊ Nœud Nord en Gémeaux – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un foyer stimulant et ouvert aux échanges.

## L'énergie du moment
Le Nœud Nord en Gémeaux dynamise ta maison des racines. Tu es appelé(e) à créer un chez-toi qui favorise la communication, l'apprentissage et les connexions. Ta famille devient un lieu d'échanges vivants.

## Ce que tu pourrais vivre
- Un désir de créer un foyer intellectuellement stimulant
- Des conversations profondes avec ta famille
- Un besoin de légèreté et de variété dans ton intimité

## Conseils pour ce transit
- Transforme ton foyer en lieu d'échanges et d'apprentissage
- Communique davantage avec ta famille
- Apporte de la curiosité dans ta vie domestique""",

    ('gemini', 5): """# ☊ Nœud Nord en Gémeaux – Maison V

**En une phrase :** L'univers t'invite à jouer avec les mots, les idées et les connexions amoureuses légères.

## L'énergie du moment
Le Nœud Nord en Gémeaux illumine ta maison de la joie. Ta créativité passe par l'expression verbale et les jeux d'esprit. En amour, tu es appelé(e) à la légèreté, au flirt intelligent et aux connexions mentales.

## Ce que tu pourrais vivre
- Une créativité qui s'exprime par l'écriture ou la parole
- Des romances légères et intellectuellement stimulantes
- Un plaisir renouvelé dans les jeux et les échanges

## Conseils pour ce transit
- Crée avec les mots : écris, raconte, joue avec le langage
- Cherche des partenaires qui stimulent ton esprit
- Amuse-toi avec légèreté et curiosité""",

    ('gemini', 6): """# ☊ Nœud Nord en Gémeaux – Maison VI

**En une phrase :** Ta croissance karmique passe par un travail varié et une routine flexible.

## L'énergie du moment
Le Nœud Nord en Gémeaux active ta maison du quotidien. Tu es invité(e) à diversifier tes tâches, à apprendre constamment dans ton travail et à garder une routine qui laisse place à la nouveauté.

## Ce que tu pourrais vivre
- Un travail qui implique communication et variété
- Des opportunités d'apprentissage dans ton métier
- Une santé qui bénéficie du mouvement et de la variété

## Conseils pour ce transit
- Choisis un travail qui te permet d'apprendre et d'échanger
- Varie tes routines pour éviter l'ennui
- Reste mentalement actif dans ton quotidien""",

    ('gemini', 7): """# ☊ Nœud Nord en Gémeaux – Maison VII

**En une phrase :** Ta mission karmique t'invite à cultiver le dialogue dans tes relations.

## L'énergie du moment
Le Nœud Nord en Gémeaux dynamise ta maison des partenariats. Tu es appelé(e) à développer des relations basées sur la communication, l'échange d'idées et la curiosité mutuelle. Le dialogue devient le ciment de tes liens.

## Ce que tu pourrais vivre
- Des relations qui s'épanouissent par la conversation
- Un besoin de partenaires intellectuellement stimulants
- Des associations professionnelles basées sur l'échange

## Conseils pour ce transit
- Communique ouvertement avec tes partenaires
- Cherche des relations qui nourrissent ton esprit
- Cultive la curiosité envers l'autre""",

    ('gemini', 8): """# ☊ Nœud Nord en Gémeaux – Maison VIII

**En une phrase :** Tu es appelé(e) à explorer les profondeurs avec légèreté et curiosité.

## L'énergie du moment
Le Nœud Nord en Gémeaux allège ta maison des transformations. Ta croissance passe par une approche curieuse et détachée des questions profondes : intimité, mort, ressources partagées. Parler de ces sujets te libère.

## Ce que tu pourrais vivre
- Une capacité à verbaliser tes émotions profondes
- Des conversations transformatrices sur des sujets tabous
- Une approche plus légère des crises et transformations

## Conseils pour ce transit
- Parle de ce qui te fait peur pour le démystifier
- Explore les sujets profonds avec curiosité plutôt que peur
- Diversifie tes sources de revenus partagés""",

    ('gemini', 9): """# ☊ Nœud Nord en Gémeaux – Maison IX

**En une phrase :** L'univers t'invite à explorer mille philosophies plutôt qu'une seule vérité.

## L'énergie du moment
Le Nœud Nord en Gémeaux libère ta maison de l'expansion. Ta croissance passe par l'exploration de multiples perspectives, le refus du dogmatisme et la joie de découvrir toujours de nouveaux horizons intellectuels.

## Ce que tu pourrais vivre
- Une soif d'apprendre de cultures et philosophies diverses
- Des voyages qui élargissent ta vision du monde
- Un enseignement qui intègre plusieurs points de vue

## Conseils pour ce transit
- Reste ouvert(e) à toutes les perspectives
- Voyage pour découvrir, pas pour confirmer tes croyances
- Partage des connaissances variées plutôt qu'une doctrine""",

    ('gemini', 10): """# ☊ Nœud Nord en Gémeaux – Maison X

**En une phrase :** Ta mission de vie t'appelle vers une carrière basée sur la communication.

## L'énergie du moment
Le Nœud Nord en Gémeaux couronne ta maison de la carrière. Tu es appelé(e) à utiliser ta voix, ta plume ou tes talents de connexion pour réussir. Ta versatilité devient un atout professionnel majeur.

## Ce que tu pourrais vivre
- Une carrière impliquant écriture, parole ou médias
- Une reconnaissance pour ta polyvalence et ton esprit vif
- Des opportunités qui valorisent tes talents de communicateur

## Conseils pour ce transit
- Oriente ta carrière vers la communication
- Montre ta capacité à toucher à plusieurs domaines
- Utilise ta voix pour atteindre tes objectifs professionnels""",

    ('gemini', 11): """# ☊ Nœud Nord en Gémeaux – Maison XI

**En une phrase :** Tu es invité(e) à connecter les gens et faire circuler les idées.

## L'énergie du moment
Le Nœud Nord en Gémeaux active ta maison des amitiés et des réseaux. Ta mission est de créer des ponts entre les gens, de faciliter les échanges et de faire circuler l'information. Tu deviens un hub social.

## Ce que tu pourrais vivre
- Un réseau social qui s'élargit considérablement
- Un rôle de connecteur ou facilitateur dans les groupes
- Des projets collectifs basés sur la communication

## Conseils pour ce transit
- Connecte les gens qui devraient se connaître
- Participe activement aux échanges de groupe
- Utilise les réseaux pour faire avancer tes idéaux""",

    ('gemini', 12): """# ☊ Nœud Nord en Gémeaux – Maison XII

**En une phrase :** Ta croissance karmique passe par l'exploration curieuse de ton monde intérieur.

## L'énergie du moment
Le Nœud Nord en Gémeaux anime ta maison de l'invisible. Tu es appelé(e) à explorer ton inconscient avec curiosité plutôt qu'avec peur, à mettre des mots sur tes rêves et intuitions. L'écriture spirituelle te libère.

## Ce que tu pourrais vivre
- Un besoin de verbaliser tes expériences spirituelles
- Des rêves riches en messages à décoder
- Une spiritualité qui intègre la réflexion et l'échange

## Conseils pour ce transit
- Tiens un journal de tes rêves et intuitions
- Explore plusieurs pratiques spirituelles avec ouverture
- Communique sur ton chemin intérieur""",

    # ============== CANCER ==============
    ('cancer', 1): """# ☊ Nœud Nord en Cancer – Maison I

**En une phrase :** L'univers t'invite à développer ta sensibilité, ton intuition et ta capacité à prendre soin.

## L'énergie du moment
Le Nœud Nord en Cancer dans ta maison I t'appelle à incarner la douceur, l'empathie et la protection. Ta croissance passe par l'acceptation de ta vulnérabilité comme force. C'est le moment d'honorer tes émotions.

## Ce que tu pourrais vivre
- Un besoin de montrer ta sensibilité authentique
- Une redéfinition de ton image vers plus de douceur
- Des situations qui éveillent ton instinct maternel/protecteur

## Conseils pour ce transit
- Montre ta vulnérabilité comme une force, pas une faiblesse
- Développe ton intuition et fais-lui confiance
- Prends soin de toi comme tu prendrais soin d'un être cher""",

    ('cancer', 2): """# ☊ Nœud Nord en Cancer – Maison II

**En une phrase :** Ta mission karmique te guide vers une sécurité émotionnelle autant que matérielle.

## L'énergie du moment
Le Nœud Nord en Cancer adoucit ta maison des ressources. Tu es invité(e) à bâtir une sécurité qui nourrit ton cœur autant que ton compte en banque. Tes valeurs doivent inclure le bien-être émotionnel.

## Ce que tu pourrais vivre
- Un besoin de sécurité financière pour ta famille ou ton foyer
- Des revenus liés au soin, à la nutrition ou à la protection
- Une redéfinition de ce qui constitue la vraie richesse

## Conseils pour ce transit
- Investis dans ce qui nourrit ton âme, pas juste ton portefeuille
- Développe des ressources qui servent ta famille ou communauté
- Trouve l'équilibre entre sécurité matérielle et émotionnelle""",

    ('cancer', 3): """# ☊ Nœud Nord en Cancer – Maison III

**En une phrase :** Tu es appelé(e) à communiquer avec le cœur et l'intuition.

## L'énergie du moment
Le Nœud Nord en Cancer tempère ta maison de la communication. Ta croissance passe par une parole qui vient du cœur, une écoute empathique et des échanges qui nourrissent. La communication devient un acte de soin.

## Ce que tu pourrais vivre
- Une parole plus émotionnelle et authentique
- Des liens fraternels ou de voisinage basés sur le soutien mutuel
- Un apprentissage qui passe par le ressenti

## Conseils pour ce transit
- Communique ce que tu ressens, pas juste ce que tu penses
- Écoute avec empathie avant de répondre
- Apprends de façon intuitive et émotionnelle""",

    ('cancer', 4): """# ☊ Nœud Nord en Cancer – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un vrai foyer, un nid émotionnel.

## L'énergie du moment
Le Nœud Nord en Cancer est chez lui dans ta maison des racines. C'est un appel puissant à construire un foyer aimant, à guérir tes blessures familiales et à devenir le parent dont tu avais besoin. Ta maison devient ton sanctuaire.

## Ce que tu pourrais vivre
- Un besoin profond de créer un chez-toi nourrissant
- Une guérison des blessures d'enfance ou familiales
- Un appel à fonder ou renforcer ta propre famille

## Conseils pour ce transit
- Crée un foyer qui te fait te sentir en sécurité
- Guéris ta relation avec tes racines et ta lignée
- Deviens la source de tendresse que tu cherchais""",

    ('cancer', 5): """# ☊ Nœud Nord en Cancer – Maison V

**En une phrase :** L'univers t'invite à créer et aimer avec tendresse et profondeur émotionnelle.

## L'énergie du moment
Le Nœud Nord en Cancer illumine ta maison de la joie. Ta créativité s'exprime mieux quand elle vient du cœur. En amour, tu es appelé(e) à la tendresse, à l'attachement profond et à l'expression des sentiments.

## Ce que tu pourrais vivre
- Une créativité inspirée par les émotions et les souvenirs
- Des relations amoureuses profondes et nourrissantes
- Un rapport aux enfants ou à l'enfant intérieur qui s'approfondit

## Conseils pour ce transit
- Crée à partir de tes émotions les plus profondes
- Ose montrer ta tendresse en amour
- Reconnecte-toi à ton enfant intérieur avec douceur""",

    ('cancer', 6): """# ☊ Nœud Nord en Cancer – Maison VI

**En une phrase :** Ta croissance karmique passe par le soin aux autres et à toi-même au quotidien.

## L'énergie du moment
Le Nœud Nord en Cancer adoucit ta maison du travail. Tu es invité(e) à intégrer le soin et l'empathie dans ta vie professionnelle et tes routines. Ton travail peut devenir un acte d'amour.

## Ce que tu pourrais vivre
- Un travail impliquant le soin, la nutrition ou la protection
- Des routines qui nourrissent ton bien-être émotionnel
- Une santé qui s'améliore par l'auto-compassion

## Conseils pour ce transit
- Choisis un travail qui te permet de prendre soin des autres
- Crée des routines qui nourrissent ton corps et ton âme
- Traite-toi avec la douceur que tu offrirais à un enfant""",

    ('cancer', 7): """# ☊ Nœud Nord en Cancer – Maison VII

**En une phrase :** Ta mission karmique t'invite à créer des relations nourrissantes et protectrices.

## L'énergie du moment
Le Nœud Nord en Cancer adoucit ta maison des partenariats. Tu es appelé(e) à développer des relations qui ressemblent à une famille, où l'on prend soin l'un de l'autre. La tendresse devient le ciment de tes liens.

## Ce que tu pourrais vivre
- Des relations qui évoluent vers plus de profondeur émotionnelle
- Un besoin de te sentir en sécurité avec ton/ta partenaire
- Des partenariats qui fonctionnent comme une famille choisie

## Conseils pour ce transit
- Crée un espace sûr dans tes relations
- Exprime tes besoins émotionnels à tes partenaires
- Prends soin de l'autre comme tu prendrais soin d'un enfant""",

    ('cancer', 8): """# ☊ Nœud Nord en Cancer – Maison VIII

**En une phrase :** Tu es appelé(e) à accueillir tes émotions les plus profondes avec tendresse.

## L'énergie du moment
Le Nœud Nord en Cancer adoucit ta maison des profondeurs. Ta croissance passe par l'accueil bienveillant de toutes tes émotions, même les plus sombres. L'intimité devient un lieu de guérison et de réconfort.

## Ce que tu pourrais vivre
- Une capacité accrue à traverser les crises avec compassion
- Une intimité qui guérit les vieilles blessures
- Un rapport à la transformation plus doux et maternel

## Conseils pour ce transit
- Accueille tes émotions profondes sans jugement
- Crée une intimité qui se sent comme un cocon protecteur
- Permets-toi d'être vulnérable dans les moments difficiles""",

    ('cancer', 9): """# ☊ Nœud Nord en Cancer – Maison IX

**En une phrase :** L'univers t'invite à une spiritualité du cœur et de l'intuition.

## L'énergie du moment
Le Nœud Nord en Cancer tempère ta maison de l'expansion. Ta croissance philosophique passe par le ressenti plutôt que l'intellect. Ta sagesse vient de l'intuition et de la connexion émotionnelle au divin.

## Ce que tu pourrais vivre
- Une spiritualité plus intuitive et moins intellectuelle
- Des voyages vers des lieux qui touchent ton cœur
- Un enseignement qui passe par l'empathie et le soutien

## Conseils pour ce transit
- Fais confiance à ton intuition spirituelle
- Voyage vers des lieux qui nourrissent ton âme
- Partage ta sagesse avec compassion et douceur""",

    ('cancer', 10): """# ☊ Nœud Nord en Cancer – Maison X

**En une phrase :** Ta mission de vie t'appelle à prendre soin à grande échelle.

## L'énergie du moment
Le Nœud Nord en Cancer couronne ta maison de la carrière. Tu es appelé(e) à utiliser ta capacité de soin et de protection dans ta vie professionnelle. Ton rôle public peut être celui d'un parent pour beaucoup.

## Ce que tu pourrais vivre
- Une carrière dans le soin, la protection ou la nutrition
- Une reconnaissance pour ta capacité à créer des espaces sûrs
- Un rôle de figure maternelle/paternelle dans ton domaine

## Conseils pour ce transit
- Oriente ta carrière vers le soin et la protection
- Crée un environnement professionnel chaleureux
- Laisse ton intuition guider tes décisions de carrière""",

    ('cancer', 11): """# ☊ Nœud Nord en Cancer – Maison XI

**En une phrase :** Tu es invité(e) à créer une tribu, une famille choisie.

## L'énergie du moment
Le Nœud Nord en Cancer réchauffe ta maison des amitiés. Ta mission est de transformer tes cercles sociaux en famille choisie, où chacun prend soin de l'autre. Tes idéaux passent par le cœur.

## Ce que tu pourrais vivre
- Des amitiés qui deviennent comme une famille
- Des projets collectifs centrés sur le soin et la protection
- Un rôle maternel/paternel dans tes groupes

## Conseils pour ce transit
- Crée une communauté où l'on se soutient mutuellement
- Choisis des causes qui protègent les plus vulnérables
- Apporte de la chaleur et du soin à tes cercles sociaux""",

    ('cancer', 12): """# ☊ Nœud Nord en Cancer – Maison XII

**En une phrase :** Ta croissance karmique passe par l'auto-compassion et le soin de ton monde intérieur.

## L'énergie du moment
Le Nœud Nord en Cancer adoucit ta maison de l'invisible. Tu es appelé(e) à traiter ton inconscient avec la tendresse d'une mère, à guérir tes blessures karmiques par l'amour inconditionnel envers toi-même.

## Ce que tu pourrais vivre
- Une guérison profonde par l'auto-compassion
- Des rêves qui révèlent des besoins de soin non satisfaits
- Une spiritualité basée sur l'amour inconditionnel

## Conseils pour ce transit
- Traite ton enfant intérieur avec une tendresse infinie
- Médite avec l'énergie de l'amour maternel
- Guéris tes blessures en leur offrant la compassion qu'elles méritent""",
}


async def insert_interpretations():
    """Insert North Node transit interpretations for Aries, Taurus, Gemini, Cancer"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_NORTH_NODE_INTERPRETATIONS.items():
            # Check if exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_north_node',
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
                subject='transit_north_node',
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
        print(f"✅ Transit North Node (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
