#!/usr/bin/env python3
"""
Insert transit_south_node interpretations V2 for Aries, Taurus, Gemini, Cancer (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SOUTH_NODE_INTERPRETATIONS = {
    # ============== ARIES ==============
    ('aries', 1): """# ☋ Nœud Sud en Bélier – Maison I

**En une phrase :** Le moment est venu de lâcher l'ego guerrier et de t'ouvrir à la coopération.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison I signale que tu es très à l'aise avec l'indépendance, l'action solo et l'affirmation de soi. Mais ce transit t'invite à reconnaître que cette force peut devenir un piège si elle t'isole des autres.

## Ce que tu pourrais vivre
- Une tendance à vouloir tout faire seul(e) qui se retourne contre toi
- Des situations qui montrent les limites de l'approche « moi d'abord »
- Un besoin de rééquilibrer entre indépendance et partenariat

## Conseils pour ce transit
- Reconnais quand ton indépendance devient de l'isolement
- Accepte l'aide et la collaboration sans y voir une faiblesse
- Équilibre ton assertivité avec l'écoute de l'autre""",

    ('aries', 2): """# ☋ Nœud Sud en Bélier – Maison II

**En une phrase :** Il est temps de revoir ta façon conquérante de gérer tes ressources.

## L'énergie du moment
Le Nœud Sud en Bélier active ta maison des ressources avec une énergie de conquête impulsive. Tu as peut-être l'habitude de foncer tête baissée pour obtenir ce que tu veux, mais ce transit t'invite à une approche plus nuancée.

## Ce que tu pourrais vivre
- Des dépenses impulsives ou des décisions financières trop rapides
- Une tendance à valoriser ce que tu as conquis seul(e)
- Un questionnement sur le prix de ton indépendance financière

## Conseils pour ce transit
- Ralentis avant les décisions financières importantes
- Considère le partage des ressources comme une option
- Valorise la stabilité autant que la conquête""",

    ('aries', 3): """# ☋ Nœud Sud en Bélier – Maison III

**En une phrase :** Ta communication directe et combative demande à s'adoucir.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison de la communication révèle une tendance à parler sans filtrer, à défendre tes idées comme des batailles. Ce transit t'invite à découvrir la puissance du dialogue et de l'écoute.

## Ce que tu pourrais vivre
- Des conflits de communication par excès de franchise
- Une impatience dans les apprentissages qui veulent aller trop vite
- Des tensions avec l'entourage proche par ton côté direct

## Conseils pour ce transit
- Écoute autant que tu parles
- Apprends la diplomatie dans l'expression de tes idées
- Prends le temps d'entendre les autres points de vue""",

    ('aries', 4): """# ☋ Nœud Sud en Bélier – Maison IV

**En une phrase :** Le schéma du combattant solitaire dans la famille doit évoluer.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison des racines indique que tu as pu jouer le rôle du pionnier ou du rebelle dans ta famille. Ce transit t'invite à trouver une autre façon d'exister dans ton clan.

## Ce que tu pourrais vivre
- Des tensions familiales liées à ton indépendance farouche
- Un besoin de redéfinir ta place dans la famille autrement que par l'opposition
- Des souvenirs d'avoir dû te battre seul(e) pour exister

## Conseils pour ce transit
- Trouve ta place dans la famille sans être en guerre
- Accepte le soutien familial comme une force, pas une faiblesse
- Crée des racines qui nourrissent plutôt qu'elles ne confinent""",

    ('aries', 5): """# ☋ Nœud Sud en Bélier – Maison V

**En une phrase :** Ta créativité et tes amours ont besoin de moins d'ego et plus de partage.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison de la joie révèle une tendance à vivre la créativité et l'amour comme des conquêtes personnelles. Ce transit t'invite à découvrir la joie du partage et de la co-création.

## Ce que tu pourrais vivre
- Des histoires d'amour où tu as voulu dominer ou conquérir
- Une créativité qui reste trop centrée sur toi-même
- Un besoin de reconnaissance personnelle dans tes loisirs

## Conseils pour ce transit
- Crée avec et pour les autres, pas seulement pour toi
- Vis l'amour comme un partenariat, pas une conquête
- Trouve la joie dans le partage autant que dans l'expression personnelle""",

    ('aries', 6): """# ☋ Nœud Sud en Bélier – Maison VI

**En une phrase :** Ton approche combative du travail quotidien demande à s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison du travail indique une tendance à aborder le quotidien comme une série de batailles à gagner. Ce transit t'invite à découvrir le pouvoir de la collaboration et du service.

## Ce que tu pourrais vivre
- Des conflits au travail par excès de compétitivité
- Un stress lié à vouloir tout faire seul(e) et vite
- Une santé qui souffre de ton rythme de guerrier

## Conseils pour ce transit
- Travaille avec les autres plutôt que contre eux
- Ralentis ton rythme quotidien sans culpabiliser
- Prends soin de toi avec douceur, pas avec discipline militaire""",

    ('aries', 7): """# ☋ Nœud Sud en Bélier – Maison VII

**En une phrase :** Ta tendance à l'indépendance dans les relations doit trouver un équilibre.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison des partenariats crée un paradoxe : tu cherches des relations mais tu veux rester totalement indépendant(e). Ce transit t'invite à apprendre le vrai partenariat.

## Ce que tu pourrais vivre
- Des relations où tu domines ou où tu fuis l'engagement
- Des partenaires qui te reprochent ton individualisme
- Un questionnement sur comment être toi-même en couple

## Conseils pour ce transit
- Apprends à considérer l'autre comme un égal, pas un adversaire
- Accepte les compromis comme des opportunités, pas des défaites
- Cultive l'interdépendance plutôt que l'indépendance totale""",

    ('aries', 8): """# ☋ Nœud Sud en Bélier – Maison VIII

**En une phrase :** Ton approche combative des crises et de l'intimité demande à évoluer.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison des transformations indique que tu affrontes habituellement les crises en mode guerrier. Ce transit t'invite à découvrir une autre façon de traverser les épreuves.

## Ce que tu pourrais vivre
- Des crises où ta combativité empire les choses
- Une intimité perturbée par ton besoin de contrôle
- Des luttes de pouvoir autour des ressources partagées

## Conseils pour ce transit
- Face aux crises, parfois la douceur est plus forte que la force
- Apprends à partager le pouvoir dans l'intimité
- Transforme-toi par l'abandon plutôt que par la conquête""",

    ('aries', 9): """# ☋ Nœud Sud en Bélier – Maison IX

**En une phrase :** Ta quête solitaire de vérité doit s'ouvrir aux autres perspectives.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison de l'expansion révèle une tendance à imposer ta vision du monde ou à partir seul(e) en croisade philosophique. Ce transit t'invite au dialogue et à l'humilité.

## Ce que tu pourrais vivre
- Des débats philosophiques qui tournent au conflit
- Des voyages solitaires qui isolent plutôt qu'ils n'enrichissent
- Une certitude excessive dans tes croyances

## Conseils pour ce transit
- Écoute d'autres philosophies avec ouverture
- Voyage et apprends avec d'autres plutôt que seul(e)
- Ta vérité n'est pas la seule vérité""",

    ('aries', 10): """# ☋ Nœud Sud en Bélier – Maison X

**En une phrase :** Ton ambition de loup solitaire doit évoluer vers le leadership collaboratif.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison de la carrière indique que tu as construit ta réussite en mode pionnier solitaire. Ce transit t'invite à découvrir la puissance de diriger avec les autres.

## Ce que tu pourrais vivre
- Un plafond de verre dû à ton image trop individualiste
- Des conflits professionnels par excès de compétitivité
- Un questionnement sur le prix de ton ambition solitaire

## Conseils pour ce transit
- Construis ta réussite en incluant les autres
- Passe du leadership autoritaire au leadership collaboratif
- Ta carrière peut grandir si tu acceptes les partenariats""",

    ('aries', 11): """# ☋ Nœud Sud en Bélier – Maison XI

**En une phrase :** Ton individualisme dans les groupes doit céder la place à l'esprit d'équipe.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison des amitiés révèle une tendance à vouloir dominer les groupes ou à t'en isoler. Ce transit t'invite à découvrir la richesse de la collaboration égalitaire.

## Ce que tu pourrais vivre
- Des amitiés où tu prends toujours le rôle de leader
- Un sentiment de décalage avec les causes collectives
- Des projets de groupe qui souffrent de ton individualisme

## Conseils pour ce transit
- Laisse d'autres prendre le leadership dans les groupes
- Contribue aux projets collectifs sans chercher à dominer
- Tes idéaux se réalisent mieux en équipe""",

    ('aries', 12): """# ☋ Nœud Sud en Bélier – Maison XII

**En une phrase :** Ta lutte intérieure solitaire doit céder la place à l'abandon et la foi.

## L'énergie du moment
Le Nœud Sud en Bélier dans ta maison de l'invisible indique une tendance à combattre tes démons intérieurs comme un guerrier solitaire. Ce transit t'invite à découvrir le pouvoir du lâcher-prise.

## Ce que tu pourrais vivre
- Une fatigue spirituelle à force de lutter contre toi-même
- Des résistances intérieures qui s'épuisent enfin
- Un karma de guerrier solitaire qui demande à se libérer

## Conseils pour ce transit
- Cesse de te battre contre tes propres ombres
- La paix intérieure vient du lâcher-prise, pas de la victoire
- Accepte l'aide invisible plutôt que de tout porter seul(e)""",

    # ============== TAURUS ==============
    ('taurus', 1): """# ☋ Nœud Sud en Taureau – Maison I

**En une phrase :** Ta zone de confort matérielle et physique doit s'ouvrir au changement.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison I révèle un attachement excessif à la stabilité, au confort et à ce que tu possèdes. Ce transit t'invite à découvrir la liberté de lâcher prise sur le matériel.

## Ce que tu pourrais vivre
- Une résistance au changement qui te limite
- Un attachement à ton image de stabilité et de fiabilité
- Un confort qui devient une prison dorée

## Conseils pour ce transit
- Accepte que le changement peut être bénéfique
- Définis-toi par plus que ce que tu possèdes
- Explore l'inconfort comme terrain de croissance""",

    ('taurus', 2): """# ☋ Nœud Sud en Taureau – Maison II

**En une phrase :** Ton attachement aux possessions et à la sécurité matérielle doit évoluer.

## L'énergie du moment
Le Nœud Sud en Taureau est dans sa maison naturelle, amplifiant l'attachement aux biens et à la sécurité financière. Ce transit t'invite à questionner ce que signifie vraiment la richesse.

## Ce que tu pourrais vivre
- Une accumulation qui ne comble pas un vide intérieur
- Une peur de perdre qui empêche de vivre pleinement
- Un questionnement profond sur tes vraies valeurs

## Conseils pour ce transit
- La vraie richesse n'est pas que matérielle
- Ose partager et lâcher ce que tu retiens trop
- Trouve la sécurité en toi, pas dans tes possessions""",

    ('taurus', 3): """# ☋ Nœud Sud en Taureau – Maison III

**En une phrase :** Ta pensée rigide et tes habitudes mentales demandent de la flexibilité.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison de la communication révèle une tendance à la pensée fixe, aux opinions enracinées. Ce transit t'invite à plus de curiosité et d'ouverture mentale.

## Ce que tu pourrais vivre
- Des difficultés à changer d'avis ou à apprendre du nouveau
- Une communication qui tourne en rond sur les mêmes sujets
- Des relations de voisinage ou fraternelles trop routinières

## Conseils pour ce transit
- Ose questionner tes certitudes les plus ancrées
- Apprends des choses nouvelles qui te sortent de ta zone de confort
- Varie tes échanges et tes sources d'information""",

    ('taurus', 4): """# ☋ Nœud Sud en Taureau – Maison IV

**En une phrase :** Ton attachement au confort domestique et aux traditions familiales doit évoluer.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison des racines indique un fort attachement au foyer, aux traditions et au patrimoine familial. Ce transit t'invite à te libérer de ce qui t'enferme.

## Ce que tu pourrais vivre
- Un foyer qui devient une routine étouffante
- Des traditions familiales qui limitent ton évolution
- Un patrimoine qui attache plus qu'il ne libère

## Conseils pour ce transit
- Le vrai chez-toi peut évoluer et se transformer
- Libère-toi des traditions qui ne te servent plus
- Crée de nouvelles racines plutôt que de t'accrocher aux anciennes""",

    ('taurus', 5): """# ☋ Nœud Sud en Taureau – Maison V

**En une phrase :** Ta créativité et tes amours ont besoin de moins de possessivité.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison de la joie révèle une tendance à la possessivité en amour et à la routine créative. Ce transit t'invite à la légèreté et au renouvellement.

## Ce que tu pourrais vivre
- Des amours où la possessivité étouffe la passion
- Une créativité qui s'enlise dans les mêmes formules
- Des plaisirs qui deviennent des habitudes sans saveur

## Conseils pour ce transit
- Aime sans posséder, crée sans t'attacher au résultat
- Renouvelle tes sources de plaisir et de créativité
- La joie est dans le mouvement, pas dans la possession""",

    ('taurus', 6): """# ☋ Nœud Sud en Taureau – Maison VI

**En une phrase :** Tes routines confortables et ton travail stable demandent à évoluer.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison du quotidien indique un attachement excessif aux routines établies et à la sécurité de l'emploi. Ce transit t'invite à plus de flexibilité.

## Ce que tu pourrais vivre
- Un travail stable mais qui ne te fait plus grandir
- Des routines de santé devenues rigides ou obsolètes
- Une résistance au changement dans ton quotidien

## Conseils pour ce transit
- La vraie santé inclut l'adaptabilité
- Ton travail peut évoluer sans perdre en sécurité
- Révolutionne tes routines de temps en temps""",

    ('taurus', 7): """# ☋ Nœud Sud en Taureau – Maison VII

**En une phrase :** Ta recherche de stabilité dans les relations doit s'ouvrir au changement.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison des partenariats révèle un attachement excessif à la stabilité relationnelle, parfois au détriment de la vitalité. Ce transit t'invite à la transformation.

## Ce que tu pourrais vivre
- Des relations stables mais enlisées dans la routine
- Une possessivité qui étouffe tes partenaires
- Un refus de voir que certaines relations doivent évoluer

## Conseils pour ce transit
- Une relation vivante change et se renouvelle
- Lâche la possessivité pour garder la connexion
- Accepte que certains partenariats doivent se transformer""",

    ('taurus', 8): """# ☋ Nœud Sud en Taureau – Maison VIII

**En une phrase :** Ton attachement à la sécurité face aux transformations doit céder.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison des profondeurs révèle une résistance aux changements profonds, un attachement à ce qui devrait mourir. Ce transit t'invite à accepter la transformation.

## Ce que tu pourrais vivre
- Une résistance aux crises qui les prolonge
- Un attachement aux ressources partagées qui complique les situations
- Une peur du changement qui t'empêche de renaître

## Conseils pour ce transit
- Certaines choses doivent mourir pour que tu renaisse
- Lâche ce que tu retiens trop fort
- La vraie sécurité vient de ta capacité à te transformer""",

    ('taurus', 9): """# ☋ Nœud Sud en Taureau – Maison IX

**En une phrase :** Tes croyances figées et ta philosophie matérialiste doivent s'élargir.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison de l'expansion indique une philosophie trop ancrée dans le concret et le matériel. Ce transit t'invite à explorer des horizons plus vastes.

## Ce que tu pourrais vivre
- Une vision du monde trop terre-à-terre qui te limite
- Des voyages confortables qui n'élargissent pas vraiment
- Des certitudes philosophiques qui se rigidifient

## Conseils pour ce transit
- Explore des philosophies qui dépassent le matériel
- Voyage vers l'inconnu plutôt que le familier
- Tes croyances peuvent évoluer sans te perdre""",

    ('taurus', 10): """# ☋ Nœud Sud en Taureau – Maison X

**En une phrase :** Ta carrière stable et confortable doit s'ouvrir à de nouveaux défis.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison de la carrière indique un attachement à la sécurité professionnelle qui peut limiter ton évolution. Ce transit t'invite à viser plus haut.

## Ce que tu pourrais vivre
- Une carrière stable mais sans évolution
- Un confort professionnel qui devient une prison
- Une réputation de fiabilité qui limite tes possibilités

## Conseils pour ce transit
- La vraie réussite inclut la croissance et le risque
- Ta réputation peut évoluer positivement
- Ose changer de voie si nécessaire""",

    ('taurus', 11): """# ☋ Nœud Sud en Taureau – Maison XI

**En une phrase :** Ton confort dans les amitiés établies doit s'ouvrir à de nouvelles connexions.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison des amitiés révèle un attachement aux cercles établis et aux causes concrètes. Ce transit t'invite à élargir tes horizons sociaux.

## Ce que tu pourrais vivre
- Des amitiés qui s'enlisent dans la routine
- Des projets collectifs trop terre-à-terre
- Une résistance aux nouveaux réseaux et aux nouvelles idées

## Conseils pour ce transit
- Tes amis d'hier ne sont pas forcément ceux de demain
- Ouvre-toi à des causes et des groupes différents
- L'innovation sociale demande de sortir du confort""",

    ('taurus', 12): """# ☋ Nœud Sud en Taureau – Maison XII

**En une phrase :** Ton attachement au monde matériel doit céder à la dimension spirituelle.

## L'énergie du moment
Le Nœud Sud en Taureau dans ta maison de l'invisible révèle un ancrage excessif dans le tangible qui limite ton ouverture spirituelle. Ce transit t'invite à lâcher les attaches pour t'élever.

## Ce que tu pourrais vivre
- Une difficulté à méditer ou à lâcher le mental
- Un karma d'attachement matériel à libérer
- Une résistance à l'invisible et au mystère

## Conseils pour ce transit
- La vraie richesse est au-delà du visible
- Ton attachement au concret voile ta nature spirituelle
- Laisse mourir l'attachement pour renaître libre""",

    # ============== GEMINI ==============
    ('gemini', 1): """# ☋ Nœud Sud en Gémeaux – Maison I

**En une phrase :** Ta dispersion et ton besoin de tout comprendre doivent céder à une vision plus large.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison I révèle une identité construite sur la curiosité, la versatilité et le mental. Ce transit t'invite à dépasser la surface pour trouver le sens profond.

## Ce que tu pourrais vivre
- Une dispersion qui t'empêche de te connaître vraiment
- Un mental hyperactif qui te déconnecte de ton essence
- Une image de personne « touche-à-tout » qui manque de profondeur

## Conseils pour ce transit
- Tu es plus que tes idées et tes connaissances
- Cherche le sens plutôt que les informations
- Définis-toi par ta sagesse, pas seulement ton intelligence""",

    ('gemini', 2): """# ☋ Nœud Sud en Gémeaux – Maison II

**En une phrase :** Ta gestion mentale et dispersée de l'argent demande plus de foi et d'intuition.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison des ressources indique une approche très cérébrale et changeante de l'argent. Ce transit t'invite à une relation plus intuitive avec l'abondance.

## Ce que tu pourrais vivre
- Des revenus multiples mais instables
- Une analyse excessive qui bloque les opportunités
- Des valeurs qui changent trop souvent

## Conseils pour ce transit
- Fais confiance à ton intuition pour les finances
- Choisis des valeurs profondes plutôt que des idées passagères
- La vraie richesse vient du sens, pas de la multiplication""",

    ('gemini', 3): """# ☋ Nœud Sud en Gémeaux – Maison III

**En une phrase :** Ta communication intellectuelle et superficielle doit s'approfondir.

## L'énergie du moment
Le Nœud Sud en Gémeaux est dans sa maison naturelle, amplifiant la tendance à la communication rapide et légère. Ce transit t'invite à plus de profondeur et de sens dans tes échanges.

## Ce que tu pourrais vivre
- Des conversations qui restent en surface
- Une curiosité qui papillonne sans jamais approfondir
- Des connaissances nombreuses mais peu de sagesse

## Conseils pour ce transit
- Moins de quantité, plus de qualité dans tes échanges
- Approfondis un sujet plutôt que d'en effleurer mille
- Communique ce qui a du sens, pas juste ce qui est intéressant""",

    ('gemini', 4): """# ☋ Nœud Sud en Gémeaux – Maison IV

**En une phrase :** Ton foyer intellectualisé a besoin de plus de profondeur émotionnelle.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison des racines révèle un rapport mental et détaché à la famille et au foyer. Ce transit t'invite à créer des liens plus profonds.

## Ce que tu pourrais vivre
- Des conversations familiales qui restent superficielles
- Un foyer où l'on pense beaucoup mais ressent peu
- Une difficulté à s'enraciner vraiment quelque part

## Conseils pour ce transit
- Connecte-toi émotionnellement à ta famille
- Ton foyer a besoin de sens, pas juste de stimulation
- Crée des racines profondes plutôt que des connexions légères""",

    ('gemini', 5): """# ☋ Nœud Sud en Gémeaux – Maison V

**En une phrase :** Ta créativité mentale et tes amours légères demandent plus de passion et de profondeur.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison de la joie révèle une créativité très intellectuelle et des amours qui restent légères. Ce transit t'invite à plus de passion et d'engagement.

## Ce que tu pourrais vivre
- Des créations brillantes mais sans âme
- Des flirts multiples sans attachement profond
- Des plaisirs cérébraux qui ne touchent pas le cœur

## Conseils pour ce transit
- Crée avec ton cœur, pas seulement ton esprit
- Ose l'engagement émotionnel en amour
- La vraie joie vient de la profondeur, pas de la variété""",

    ('gemini', 6): """# ☋ Nœud Sud en Gémeaux – Maison VI

**En une phrase :** Ta routine intellectualisée et ton multitasking demandent plus de focus.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison du quotidien révèle une tendance à la dispersion au travail et dans les routines. Ce transit t'invite à plus de concentration et de sens.

## Ce que tu pourrais vivre
- Un travail éparpillé qui manque de profondeur
- Des routines qui changent trop souvent
- Une santé mentale agitée par trop de stimulation

## Conseils pour ce transit
- Fais moins de choses mais mieux
- Crée des routines qui apportent paix et sens
- Ton travail gagnera en qualité par la concentration""",

    ('gemini', 7): """# ☋ Nœud Sud en Gémeaux – Maison VII

**En une phrase :** Tes relations intellectuelles et légères ont besoin de plus de profondeur.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison des partenariats révèle une tendance aux relations basées sur les échanges mentaux sans engagement profond. Ce transit t'invite à plus de connexion.

## Ce que tu pourrais vivre
- Des relations où l'on parle beaucoup mais partage peu
- Des partenaires multiples sans attachement durable
- Une difficulté à s'engager vraiment

## Conseils pour ce transit
- La vraie connexion va au-delà de la conversation
- Engage-toi profondément avec moins de personnes
- Cherche une âme sœur, pas juste un(e) partenaire intellectuel(le)""",

    ('gemini', 8): """# ☋ Nœud Sud en Gémeaux – Maison VIII

**En une phrase :** Ton approche intellectuelle des profondeurs doit céder au ressenti.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison des transformations révèle une tendance à analyser plutôt que vivre les crises. Ce transit t'invite à plonger vraiment dans les profondeurs.

## Ce que tu pourrais vivre
- Une rationalisation des émotions profondes qui ne libère pas
- Des crises traitées mentalement sans vraie transformation
- Une intimité plus intellectuelle que fusionnelle

## Conseils pour ce transit
- Cesse d'analyser et ose ressentir
- Les transformations se vivent, elles ne se comprennent pas
- L'intimité vraie dépasse les mots""",

    ('gemini', 9): """# ☋ Nœud Sud en Gémeaux – Maison IX

**En une phrase :** Tes nombreuses connaissances doivent se transformer en sagesse unifiée.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison de l'expansion révèle une accumulation de connaissances sans vision d'ensemble. Ce transit t'invite à trouver le fil conducteur de tout ce que tu sais.

## Ce que tu pourrais vivre
- Beaucoup de savoirs mais peu de sagesse
- Des voyages qui collectent des informations sans transformation
- Une difficulté à avoir une philosophie de vie cohérente

## Conseils pour ce transit
- Unifie tes connaissances en une vision du monde
- Voyage pour te transformer, pas pour accumuler
- La vraie sagesse est simple, pas complexe""",

    ('gemini', 10): """# ☋ Nœud Sud en Gémeaux – Maison X

**En une phrase :** Ta carrière de communicant dispersé doit trouver une mission plus grande.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison de la carrière révèle une réussite basée sur la polyvalence et la communication, mais qui manque peut-être de profondeur. Ce transit t'invite à viser plus haut.

## Ce que tu pourrais vivre
- Une carrière brillante mais superficielle
- Une réputation de touche-à-tout sans spécialité
- Un succès qui ne comble pas ta quête de sens

## Conseils pour ce transit
- Trouve la mission qui unifie tous tes talents
- Ta carrière peut servir une vision plus grande
- Deviens un sage, pas seulement un expert""",

    ('gemini', 11): """# ☋ Nœud Sud en Gémeaux – Maison XI

**En une phrase :** Ton réseau étendu mais superficiel a besoin de connexions plus profondes.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison des amitiés révèle un réseau vaste mais peu profond, des causes multiples sans engagement. Ce transit t'invite à choisir et approfondir.

## Ce que tu pourrais vivre
- Beaucoup de connaissances mais peu de vrais amis
- Des causes multiples sans engagement profond
- Une vie sociale stimulante mais pas nourrissante

## Conseils pour ce transit
- Moins de connexions, plus de vraies amitiés
- Choisis une cause et engage-toi vraiment
- La communauté se construit sur la profondeur, pas la quantité""",

    ('gemini', 12): """# ☋ Nœud Sud en Gémeaux – Maison XII

**En une phrase :** Ton mental agité doit céder la place au silence et à l'intuition.

## L'énergie du moment
Le Nœud Sud en Gémeaux dans ta maison de l'invisible révèle un mental qui perturbe ta vie spirituelle par son agitation constante. Ce transit t'invite au silence intérieur.

## Ce que tu pourrais vivre
- Une difficulté à méditer par excès de pensées
- Une spiritualité trop intellectuelle
- Un karma de dispersion mentale à libérer

## Conseils pour ce transit
- Le silence est plus sage que mille pensées
- Ta vraie nature est au-delà du mental
- Laisse tes pensées passer comme des nuages""",

    # ============== CANCER ==============
    ('cancer', 1): """# ☋ Nœud Sud en Cancer – Maison I

**En une phrase :** Ton identité émotionnelle et protectrice doit s'ouvrir à plus d'indépendance.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison I révèle une identité construite sur l'émotionnel, le maternel et le besoin de sécurité. Ce transit t'invite à développer ton autonomie.

## Ce que tu pourrais vivre
- Une dépendance émotionnelle qui te limite
- Une image de personne « trop sensible » à transcender
- Un besoin de sécurité qui t'empêche de t'affirmer

## Conseils pour ce transit
- Ta sensibilité est une force, pas tout ce que tu es
- Développe ton indépendance sans perdre ta douceur
- Sors de ta coquille pour conquérir le monde""",

    ('cancer', 2): """# ☋ Nœud Sud en Cancer – Maison II

**En une phrase :** Ton rapport émotionnel à l'argent et à la sécurité doit évoluer.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison des ressources révèle un attachement émotionnel excessif à la sécurité matérielle. Ce transit t'invite à une relation plus détachée avec l'argent.

## Ce que tu pourrais vivre
- Une accumulation pour se sentir en sécurité
- Des finances liées aux humeurs et aux émotions
- Un attachement sentimental aux possessions

## Conseils pour ce transit
- La vraie sécurité ne dépend pas de ton compte en banque
- Libère-toi de l'attachement émotionnel aux choses
- Ta valeur ne dépend pas de ce que tu possèdes""",

    ('cancer', 3): """# ☋ Nœud Sud en Cancer – Maison III

**En une phrase :** Ta communication émotionnelle doit s'équilibrer avec plus d'objectivité.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison de la communication révèle une parole très influencée par les émotions et les humeurs. Ce transit t'invite à plus de recul et de clarté.

## Ce que tu pourrais vivre
- Des conversations trop chargées émotionnellement
- Une difficulté à communiquer objectivement
- Des relations avec l'entourage trop fusionnelles

## Conseils pour ce transit
- Prends du recul avant de communiquer sous l'émotion
- L'objectivité peut coexister avec la sensibilité
- Tes frères, sœurs et voisins ne sont pas ta responsabilité""",

    ('cancer', 4): """# ☋ Nœud Sud en Cancer – Maison IV

**En une phrase :** Ton attachement au foyer et à la famille doit s'équilibrer avec tes ambitions.

## L'énergie du moment
Le Nœud Sud en Cancer est dans sa maison naturelle, amplifiant l'attachement au cocon familial et au passé. Ce transit t'invite à sortir du nid pour construire ta place dans le monde.

## Ce que tu pourrais vivre
- Un attachement au foyer qui limite tes ambitions
- Des racines qui retiennent plutôt qu'elles ne soutiennent
- Un passé familial qui pèse sur ton présent

## Conseils pour ce transit
- Tu peux aimer ta famille sans te sacrifier pour elle
- Construis ta vie publique, pas seulement ta vie privée
- Tes racines sont là pour te soutenir, pas te retenir""",

    ('cancer', 5): """# ☋ Nœud Sud en Cancer – Maison V

**En une phrase :** Ta créativité et tes amours trop nourricières doivent s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison de la joie révèle une tendance à materner dans les relations amoureuses et à créer depuis l'émotion pure. Ce transit t'invite à plus d'équilibre.

## Ce que tu pourrais vivre
- Des amours où tu joues le rôle de parent
- Une créativité trop nostalgique ou sentimentale
- Une joie de vivre dépendante de la sécurité émotionnelle

## Conseils pour ce transit
- Aime en adulte, pas en parent ou en enfant
- Crée avec structure autant qu'avec émotion
- La joie peut exister en dehors de ta zone de confort""",

    ('cancer', 6): """# ☋ Nœud Sud en Cancer – Maison VI

**En une phrase :** Ton besoin de prendre soin des autres au travail doit s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison du quotidien révèle une tendance à materner dans l'environnement de travail et à laisser les émotions influencer tes routines.

## Ce que tu pourrais vivre
- Un rôle de « mère poule » au travail qui t'épuise
- Des routines qui dépendent trop de ton humeur
- Une santé affectée par les préoccupations émotionnelles

## Conseils pour ce transit
- Ton travail n'est pas de prendre soin de tout le monde
- Crée des routines qui ne dépendent pas de ton humeur
- Ta santé bénéficiera de plus de structure et moins d'émotionnel""",

    ('cancer', 7): """# ☋ Nœud Sud en Cancer – Maison VII

**En une phrase :** Tes relations fusionnelles et dépendantes doivent évoluer vers plus d'équilibre.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison des partenariats révèle une tendance aux relations fusionnelles, dépendantes ou maternantes. Ce transit t'invite à des partenariats plus équilibrés.

## Ce que tu pourrais vivre
- Des relations où tu prends soin de l'autre au détriment de toi
- Une dépendance émotionnelle à tes partenaires
- Des attachements qui étouffent la relation

## Conseils pour ce transit
- Une relation saine laisse de l'espace à chacun
- Cesse de materner tes partenaires
- L'interdépendance saine n'est pas la dépendance émotionnelle""",

    ('cancer', 8): """# ☋ Nœud Sud en Cancer – Maison VIII

**En une phrase :** Ton attachement émotionnel face aux transformations doit céder.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison des profondeurs révèle une résistance émotionnelle aux changements et aux pertes. Ce transit t'invite à traverser les transformations avec plus de détachement.

## Ce que tu pourrais vivre
- Des crises où l'émotion amplifie la souffrance
- Un attachement à ce qui doit mourir
- Une intimité étouffée par le besoin de sécurité

## Conseils pour ce transit
- Les transformations se traversent mieux avec du recul
- Lâche émotionnellement ce qui doit partir
- L'intimité vraie peut inclure du détachement sain""",

    ('cancer', 9): """# ☋ Nœud Sud en Cancer – Maison IX

**En une phrase :** Ta philosophie émotionnelle et tes croyances rassurantes doivent s'élargir.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison de l'expansion révèle une spiritualité basée sur le réconfort et des voyages qui cherchent le familier. Ce transit t'invite à l'aventure vraie.

## Ce que tu pourrais vivre
- Des croyances qui rassurent mais ne font pas grandir
- Des voyages vers le connu plutôt que l'inconnu
- Une philosophie trop centrée sur les émotions

## Conseils pour ce transit
- Ta spiritualité peut inclure le défi et l'inconfort
- Voyage vers ce qui te transforme, pas ce qui te rassure
- La sagesse vient parfois de sortir de sa zone de confort""",

    ('cancer', 10): """# ☋ Nœud Sud en Cancer – Maison X

**En une phrase :** Ta carrière nourricière doit s'ouvrir à d'autres formes de réussite.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison de la carrière révèle une réussite basée sur le soin, la protection ou le maternel. Ce transit t'invite à explorer d'autres formes de leadership.

## Ce que tu pourrais vivre
- Une carrière dans le soin qui t'épuise
- Une image publique de « personne qui prend soin »
- Un succès limité par le refus de s'imposer

## Conseils pour ce transit
- Tu peux réussir autrement qu'en prenant soin des autres
- Développe ton autorité et ton ambition personnelle
- Ta carrière peut évoluer vers plus de leadership direct""",

    ('cancer', 11): """# ☋ Nœud Sud en Cancer – Maison XI

**En une phrase :** Ton besoin de créer une famille avec tes amis doit s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison des amitiés révèle une tendance à transformer les groupes en familles et à materner tes amis. Ce transit t'invite à des relations plus équilibrées.

## Ce que tu pourrais vivre
- Des amitiés où tu joues le rôle de parent
- Des projets collectifs guidés par l'émotion plutôt que la vision
- Un besoin de sécurité qui limite ton engagement social

## Conseils pour ce transit
- Tes amis n'ont pas besoin que tu les maternerais
- Les causes progressistes demandent parfois du détachement
- Contribue aux groupes avec ta vision, pas juste ton soin""",

    ('cancer', 12): """# ☋ Nœud Sud en Cancer – Maison XII

**En une phrase :** Ton attachement émotionnel au passé et au karma doit se libérer.

## L'énergie du moment
Le Nœud Sud en Cancer dans ta maison de l'invisible révèle un karma d'attachement émotionnel, de dépendance ou de sur-protection. Ce transit t'invite à la libération.

## Ce que tu pourrais vivre
- Des mémoires émotionnelles de vies passées à libérer
- Un attachement à la souffrance comme zone de confort
- Une spiritualité trop centrée sur le réconfort

## Conseils pour ce transit
- Libère les attachements karmiques avec amour
- La vraie paix spirituelle dépasse le besoin de sécurité
- Ton âme cherche la liberté, pas le confort""",
}


async def insert_interpretations():
    """Insert South Node transit interpretations for Aries, Taurus, Gemini, Cancer"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_SOUTH_NODE_INTERPRETATIONS.items():
            # Check if exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_south_node',
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
                subject='transit_south_node',
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
        print(f"✅ Transit South Node (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
