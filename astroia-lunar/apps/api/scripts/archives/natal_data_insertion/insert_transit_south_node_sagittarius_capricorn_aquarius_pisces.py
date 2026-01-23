#!/usr/bin/env python3
"""
Insert transit_south_node interpretations V2 for Sagittarius, Capricorn, Aquarius, Pisces (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SOUTH_NODE_INTERPRETATIONS = {
    # ============== SAGITTARIUS ==============
    ('sagittarius', 1): """# ☋ Nœud Sud en Sagittaire – Maison I

**En une phrase :** Ton identité d'aventurier et ton optimisme aveugle doivent s'ancrer dans le concret.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison I révèle une identité construite sur l'expansion, l'optimisme et la quête de sens. Ce transit t'invite à plus de réalisme et d'attention au détail.

## Ce que tu pourrais vivre
- Un optimisme qui ignore les réalités pratiques
- Une dispersion par trop d'horizons à explorer
- Une image de « sage » ou d'« aventurier » qui te limite

## Conseils pour ce transit
- La sagesse inclut l'attention aux petites choses
- L'optimisme est une force, mais le réalisme aussi
- Ancre-toi avant de vouloir explorer encore""",

    ('sagittarius', 2): """# ☋ Nœud Sud en Sagittaire – Maison II

**En une phrase :** Ton rapport généreux et imprudent à l'argent doit s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison des ressources révèle une tendance à la générosité excessive ou à l'imprudence financière. Ce transit t'invite à plus de gestion.

## Ce que tu pourrais vivre
- Des dépenses excessives pour les voyages ou l'expansion
- Une générosité qui te laisse démuni(e)
- Un optimisme financier qui ignore les réalités

## Conseils pour ce transit
- La générosité est belle, mais pas au détriment de ta sécurité
- Gère tes finances avec attention, pas juste avec foi
- L'abondance durable demande de la prudence""",

    ('sagittarius', 3): """# ☋ Nœud Sud en Sagittaire – Maison III

**En une phrase :** Tes grandes idées doivent s'ancrer dans le concret et l'écoute.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison de la communication révèle une tendance à prêcher plutôt qu'à dialoguer. Ce transit t'invite à l'écoute et à la communication pratique.

## Ce que tu pourrais vivre
- Des discours qui généralisent trop
- Une difficulté à écouter les détails concrets
- Une communication qui prêche plutôt qu'elle n'échange

## Conseils pour ce transit
- Écoute autant que tu prêches
- Les détails comptent autant que la grande vision
- Apprends à communiquer le concret, pas seulement l'abstrait""",

    ('sagittarius', 4): """# ☋ Nœud Sud en Sagittaire – Maison IV

**En une phrase :** Ton besoin d'évasion et de liberté au foyer doit s'équilibrer avec l'ancrage.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison des racines révèle une difficulté à s'enraciner, un besoin constant d'évasion. Ce transit t'invite à créer de vraies racines.

## Ce que tu pourrais vivre
- Un foyer qui n'est jamais vraiment un chez-soi
- Une famille marquée par les absences ou les voyages
- Un passé d'errance qui laisse un vide d'ancrage

## Conseils pour ce transit
- L'aventure peut attendre, l'ancrage est nécessaire
- Crée un vrai chez-toi, pas juste une base de départ
- Tes racines peuvent coexister avec ta liberté""",

    ('sagittarius', 5): """# ☋ Nœud Sud en Sagittaire – Maison V

**En une phrase :** Tes amours aventureuses et ta créativité dispersée doivent se concentrer.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison de la joie révèle une créativité qui s'éparpille et des amours qui fuient l'engagement. Ce transit t'invite à la profondeur.

## Ce que tu pourrais vivre
- Des amours nombreuses mais sans engagement
- Une créativité qui explore sans finaliser
- Un plaisir dans l'aventure qui fuit l'intimité

## Conseils pour ce transit
- L'amour vrai demande parfois de rester
- Finalise tes projets créatifs avant d'en commencer d'autres
- La joie profonde vient aussi de l'engagement""",

    ('sagittarius', 6): """# ☋ Nœud Sud en Sagittaire – Maison VI

**En une phrase :** Ton aversion pour les routines et le travail méthodique doit s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison du travail révèle une difficulté avec les tâches routinières et le souci du détail. Ce transit t'invite à l'application pratique.

## Ce que tu pourrais vivre
- Un travail où tu évites les tâches minutieuses
- Des routines qui n'existent pas ou ne tiennent pas
- Une santé négligée au profit de l'expansion

## Conseils pour ce transit
- Les détails comptent autant que la vision
- Une bonne routine est une fondation, pas une prison
- Prends soin de ta santé concrètement, pas philosophiquement""",

    ('sagittarius', 7): """# ☋ Nœud Sud en Sagittaire – Maison VII

**En une phrase :** Ton besoin de liberté dans les relations doit s'équilibrer avec l'engagement.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison des partenariats révèle une difficulté à s'engager vraiment, un besoin de liberté qui peut nuire aux relations. Ce transit t'invite au vrai partenariat.

## Ce que tu pourrais vivre
- Des relations qui n'arrivent pas à se stabiliser
- Un besoin de liberté qui repousse les partenaires
- Des partenariats où tu es plus philosophe que présent(e)

## Conseils pour ce transit
- La liberté et l'engagement peuvent coexister
- Être présent(e) est parfois plus important qu'avoir raison
- Le vrai partenariat est concret, pas juste idéaliste""",

    ('sagittarius', 8): """# ☋ Nœud Sud en Sagittaire – Maison VIII

**En une phrase :** Ton optimisme face aux crises peut être de l'évitement.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison des transformations révèle une tendance à « positiver » les crises plutôt que de les traverser vraiment. Ce transit t'invite à la profondeur.

## Ce que tu pourrais vivre
- Un optimisme qui masque la vraie douleur
- Une fuite philosophique face aux transformations
- Des ressources partagées gérées avec trop d'optimisme

## Conseils pour ce transit
- Certaines douleurs doivent être traversées, pas expliquées
- La foi est une force, mais pas une fuite
- L'intimité vraie demande de rester avec ce qui est difficile""",

    ('sagittarius', 9): """# ☋ Nœud Sud en Sagittaire – Maison IX

**En une phrase :** Ta quête de sens et d'expansion doit s'ancrer dans le concret.

## L'énergie du moment
Le Nœud Sud en Sagittaire est dans sa maison naturelle, amplifiant la quête d'expansion, de voyages et de sens au détriment de l'ancrage pratique. Ce transit t'invite à l'équilibre.

## Ce que tu pourrais vivre
- Une quête de sens qui devient fuite du quotidien
- Des voyages qui sont des fuites plus que des découvertes
- Des certitudes philosophiques qui ferment plutôt qu'elles n'ouvrent

## Conseils pour ce transit
- La vraie sagesse s'applique au quotidien
- Voyage pour grandir, pas pour fuir
- Tes croyances sont des guides, pas des certitudes absolues""",

    ('sagittarius', 10): """# ☋ Nœud Sud en Sagittaire – Maison X

**En une phrase :** Ton ambition philosophique doit s'ancrer dans des réalisations concrètes.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison de la carrière révèle une réussite basée sur la vision et l'inspiration, mais qui manque peut-être de fondations pratiques. Ce transit t'invite au concret.

## Ce que tu pourrais vivre
- Une carrière où tu inspires mais ne concrétises pas
- Une réputation de « visionnaire » sans réalisations tangibles
- Un succès basé sur des promesses plutôt que des résultats

## Conseils pour ce transit
- Les visions doivent se concrétiser pour avoir de la valeur
- Ta carrière a besoin de fondations solides, pas juste d'inspiration
- Le détail et l'application comptent autant que la vision""",

    ('sagittarius', 11): """# ☋ Nœud Sud en Sagittaire – Maison XI

**En une phrase :** Tes idéaux et tes amitiés dispersés doivent s'ancrer dans l'engagement réel.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison des amitiés révèle des liens nombreux mais superficiels et des causes idéalistes sans engagement concret. Ce transit t'invite à la profondeur.

## Ce que tu pourrais vivre
- Des amitiés nombreuses mais qui manquent de profondeur
- Des idéaux qui restent des idées sans action
- Une dispersion sociale qui ne nourrit pas vraiment

## Conseils pour ce transit
- Moins d'amis mais plus profonds
- Engage-toi concrètement pour les causes que tu défends
- Tes idéaux doivent se traduire en actions""",

    ('sagittarius', 12): """# ☋ Nœud Sud en Sagittaire – Maison XII

**En une phrase :** Ta spiritualité d'expansion doit céder à l'intégration et au service.

## L'énergie du moment
Le Nœud Sud en Sagittaire dans ta maison de l'invisible révèle une spiritualité qui cherche toujours plus loin, plus haut, sans intégrer ce qui a été appris. Ce transit t'invite au retour et au service.

## Ce que tu pourrais vivre
- Une quête spirituelle sans fin qui ne transforme pas
- Un karma de fuite spirituelle à libérer
- Des croyances qui restent théoriques

## Conseils pour ce transit
- La vraie spiritualité se vit au quotidien
- Intègre ce que tu as appris avant de chercher encore
- Le service est la preuve de la sagesse""",

    # ============== CAPRICORN ==============
    ('capricorn', 1): """# ☋ Nœud Sud en Capricorne – Maison I

**En une phrase :** Ton identité rigide et ambitieuse doit s'ouvrir à la sensibilité.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison I révèle une identité construite sur le contrôle, l'ambition et la structure. Ce transit t'invite à plus de vulnérabilité et de douceur.

## Ce que tu pourrais vivre
- Une rigidité qui te coupe de tes émotions
- Un sérieux excessif qui isole
- Une image de « personne forte » qui empêche la vraie connexion

## Conseils pour ce transit
- La force inclut la vulnérabilité
- Le contrôle est une illusion, la confiance une force
- Tu peux être sensible sans être faible""",

    ('capricorn', 2): """# ☋ Nœud Sud en Capricorne – Maison II

**En une phrase :** Ton attachement à l'argent comme pouvoir doit s'assouplir.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison des ressources révèle une relation à l'argent marquée par le contrôle et le pouvoir. Ce transit t'invite à une relation plus intuitive et fluide.

## Ce que tu pourrais vivre
- Une obsession pour l'accumulation et le statut
- Une valeur personnelle trop liée à la réussite matérielle
- Une rigueur financière qui devient rigidité

## Conseils pour ce transit
- L'argent est un outil, pas un but
- Ta valeur ne se mesure pas à ton compte en banque
- La fluidité financière peut coexister avec la sagesse""",

    ('capricorn', 3): """# ☋ Nœud Sud en Capricorne – Maison III

**En une phrase :** Ta communication structurée et sérieuse doit s'ouvrir à l'intuition.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison de la communication révèle une parole très contrôlée et sérieuse. Ce transit t'invite à plus de spontanéité et d'intuition.

## Ce que tu pourrais vivre
- Des communications trop formelles qui manquent de chaleur
- Une difficulté à exprimer tes émotions
- Des apprentissages limités par la rigidité

## Conseils pour ce transit
- La communication peut inclure l'émotion et l'intuition
- L'apprentissage est aussi intuitif que structuré
- Parle avec ton cœur parfois, pas seulement avec ta tête""",

    ('capricorn', 4): """# ☋ Nœud Sud en Capricorne – Maison IV

**En une phrase :** Ton foyer structuré et ton passé de responsabilités doivent s'alléger.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison des racines révèle un foyer marqué par les responsabilités et le devoir. Ce transit t'invite à plus de chaleur et de liberté émotionnelle.

## Ce que tu pourrais vivre
- Un foyer où le devoir remplace l'amour
- Des responsabilités familiales qui pèsent depuis toujours
- Un passé d'enfant trop responsable

## Conseils pour ce transit
- Le foyer peut être un lieu de nourriture, pas seulement de devoir
- Libère-toi des responsabilités familiales qui ne sont pas les tiennes
- Tu as le droit d'être nourri(e), pas seulement nourricier(ère)""",

    ('capricorn', 5): """# ☋ Nœud Sud en Capricorne – Maison V

**En une phrase :** Ta créativité contrôlée et tes amours sérieuses doivent s'alléger.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison de la joie révèle une difficulté à jouer, créer et aimer librement. Ce transit t'invite à la spontanéité et à la légèreté.

## Ce que tu pourrais vivre
- Une créativité bridée par le perfectionnisme
- Des amours trop sérieuses trop vite
- Une difficulté à jouer et s'amuser sans but

## Conseils pour ce transit
- Crée pour le plaisir, sans objectif de réussite
- L'amour peut être léger et joyeux
- Le jeu est essentiel, pas une perte de temps""",

    ('capricorn', 6): """# ☋ Nœud Sud en Capricorne – Maison VI

**En une phrase :** Ton travail acharné et tes routines rigides doivent s'assouplir.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison du travail révèle une éthique de travail excessive et des routines trop structurées. Ce transit t'invite à plus de fluidité et de douceur.

## Ce que tu pourrais vivre
- Un workaholisme qui nuit à ta santé
- Des routines rigides qui étouffent
- Un travail où le devoir écrase la joie

## Conseils pour ce transit
- Le travail bien fait n'est pas le travail excessif
- Tes routines peuvent être douces et fluides
- La santé vient de l'équilibre, pas de la discipline dure""",

    ('capricorn', 7): """# ☋ Nœud Sud en Capricorne – Maison VII

**En une phrase :** Tes relations basées sur le statut et le devoir doivent s'ouvrir au cœur.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison des partenariats révèle des relations marquées par le devoir, le statut ou le calcul. Ce transit t'invite à l'amour authentique.

## Ce que tu pourrais vivre
- Des relations choisies pour le statut ou la sécurité
- Un sens du devoir qui remplace l'amour
- Des partenariats où l'émotion est contrôlée

## Conseils pour ce transit
- L'amour vrai dépasse les considérations de statut
- Le partenariat inclut la vulnérabilité
- Laisse ton cœur guider tes relations, pas ton ambition""",

    ('capricorn', 8): """# ☋ Nœud Sud en Capricorne – Maison VIII

**En une phrase :** Ton contrôle face aux transformations doit céder au lâcher-prise.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison des profondeurs révèle une résistance au changement et un besoin de contrôler l'incontrôlable. Ce transit t'invite à la foi et à l'abandon.

## Ce que tu pourrais vivre
- Des crises où le contrôle empire les choses
- Une intimité froide par peur de la vulnérabilité
- Des ressources partagées gérées avec trop de calcul

## Conseils pour ce transit
- Certaines transformations exigent le lâcher-prise
- L'intimité vraie est vulnérable
- Fais confiance au processus que tu ne peux contrôler""",

    ('capricorn', 9): """# ☋ Nœud Sud en Capricorne – Maison IX

**En une phrase :** Tes croyances rigides et ta philosophie de l'effort doivent s'ouvrir.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison de l'expansion révèle une spiritualité trop structurée ou une philosophie basée sur l'effort et le mérite. Ce transit t'invite à la grâce.

## Ce que tu pourrais vivre
- Des croyances rigides qui limitent
- Une philosophie du mérite qui épuise
- Des voyages organisés qui manquent de magie

## Conseils pour ce transit
- La sagesse inclut la grâce et le mystère
- Tu n'as pas à mériter l'expansion spirituelle
- Voyage avec ouverture à l'imprévu et à la magie""",

    ('capricorn', 10): """# ☋ Nœud Sud en Capricorne – Maison X

**En une phrase :** Ton ambition excessive et ta carrière-identité doivent s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Capricorne est dans sa maison naturelle, amplifiant l'ambition, le besoin de contrôle et l'identification à la carrière. Ce transit t'invite à l'équilibre.

## Ce que tu pourrais vivre
- Une identité entièrement définie par ta carrière
- Une ambition qui sacrifie tout le reste
- Une solitude au sommet

## Conseils pour ce transit
- Tu es plus que ta réussite professionnelle
- La vie privée mérite autant d'attention que la carrière
- Le vrai succès inclut le bonheur personnel""",

    ('capricorn', 11): """# ☋ Nœud Sud en Capricorne – Maison XI

**En une phrase :** Ton contrôle dans les groupes et tes amitiés utiles doivent évoluer.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison des amitiés révèle des relations sociales basées sur l'utilité et un rôle de contrôle dans les groupes. Ce transit t'invite à l'amitié désintéressée.

## Ce que tu pourrais vivre
- Des amitiés calculées pour leur utilité
- Un rôle d'organisateur rigide dans les groupes
- Des idéaux trop réalistes qui manquent de vision

## Conseils pour ce transit
- L'amitié vraie n'a pas besoin d'être utile
- Les groupes fonctionnent aussi sans ton contrôle
- Ose rêver au-delà du « réaliste »""",

    ('capricorn', 12): """# ☋ Nœud Sud en Capricorne – Maison XII

**En une phrase :** Ton contrôle sur le spirituel doit céder au mystère et à la dissolution.

## L'énergie du moment
Le Nœud Sud en Capricorne dans ta maison de l'invisible révèle une résistance spirituelle au lâcher-prise et au mystère. Ce transit t'invite à l'abandon dans le divin.

## Ce que tu pourrais vivre
- Une méditation qui cherche à contrôler
- Un karma de rigidité spirituelle à libérer
- Une difficulté à faire confiance à l'invisible

## Conseils pour ce transit
- Le spirituel échappe au contrôle, accepte-le
- Ton karma de contrôle peut enfin se libérer
- L'abandon au divin est la vraie force""",

    # ============== AQUARIUS ==============
    ('aquarius', 1): """# ☋ Nœud Sud en Verseau – Maison I

**En une phrase :** Ton identité d'original détaché doit s'ouvrir au cœur et à la connexion personnelle.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison I révèle une identité construite sur la différence, le détachement et l'originalité. Ce transit t'invite à plus de chaleur et de connexion personnelle.

## Ce que tu pourrais vivre
- Un détachement émotionnel qui isole
- Une originalité qui devient une cage
- Une difficulté à créer des liens personnels profonds

## Conseils pour ce transit
- L'originalité n'a pas besoin de te couper des autres
- Le détachement peut coexister avec la chaleur humaine
- Ose la connexion personnelle, pas seulement collective""",

    ('aquarius', 2): """# ☋ Nœud Sud en Verseau – Maison II

**En une phrase :** Ton rapport détaché à l'argent doit s'équilibrer avec tes besoins personnels.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison des ressources révèle un détachement excessif vis-à-vis des besoins matériels ou une relation impersonnelle à l'argent. Ce transit t'invite à honorer tes besoins.

## Ce que tu pourrais vivre
- Un désintérêt pour ta propre sécurité matérielle
- Des ressources partagées ou dispersées dans des causes
- Une difficulté à valoriser TES besoins personnels

## Conseils pour ce transit
- Tes besoins matériels personnels sont légitimes
- Tu peux contribuer au collectif ET prendre soin de toi
- L'abondance personnelle n'est pas égoïste""",

    ('aquarius', 3): """# ☋ Nœud Sud en Verseau – Maison III

**En une phrase :** Ta communication intellectuelle et détachée doit s'ouvrir au cœur.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison de la communication révèle une parole très intellectuelle et impersonnelle. Ce transit t'invite à communiquer aussi avec le cœur.

## Ce que tu pourrais vivre
- Des communications brillantes mais froides
- Une difficulté à parler de tes émotions personnelles
- Des relations avec l'entourage trop détachées

## Conseils pour ce transit
- La communication peut être intellectuelle ET chaleureuse
- Parle aussi de ce que tu ressens, pas seulement de ce que tu penses
- L'écoute empathique complète l'analyse brillante""",

    ('aquarius', 4): """# ☋ Nœud Sud en Verseau – Maison IV

**En une phrase :** Ton foyer impersonnel et ta famille choisie doivent inclure la vraie intimité.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison des racines révèle un rapport détaché au foyer et à la famille biologique. Ce transit t'invite à la vraie intimité familiale.

## Ce que tu pourrais vivre
- Un foyer qui ressemble plus à une communauté qu'à un nid
- Un détachement de ta famille biologique
- Des racines qui manquent de chaleur personnelle

## Conseils pour ce transit
- Le foyer a besoin de chaleur, pas seulement d'idéaux
- Ta famille biologique mérite aussi ta présence
- L'intimité vraie est personnelle, pas juste collective""",

    ('aquarius', 5): """# ☋ Nœud Sud en Verseau – Maison V

**En une phrase :** Ta créativité impersonnelle et tes amours détachées doivent s'ouvrir à la passion.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison de la joie révèle une créativité qui sert des idées plutôt que le cœur, et des amours qui restent détachées. Ce transit t'invite à la passion.

## Ce que tu pourrais vivre
- Une créativité brillante mais froide
- Des amours qui ressemblent plus à des amitiés
- Une difficulté à t'abandonner au plaisir et à la joie

## Conseils pour ce transit
- Crée avec ton cœur, pas seulement avec ton esprit
- L'amour romantique est différent de l'amitié
- Ose la passion et l'abandon émotionnel""",

    ('aquarius', 6): """# ☋ Nœud Sud en Verseau – Maison VI

**En une phrase :** Ton travail pour des causes et ton détachement du quotidien doivent s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison du travail révèle une tendance à négliger ton propre quotidien au profit de causes plus larges. Ce transit t'invite au soin personnel.

## Ce que tu pourrais vivre
- Un travail pour le collectif au détriment de ta santé
- Des routines inexistantes ou trop originales
- Un détachement de ton propre bien-être

## Conseils pour ce transit
- Prends soin de TOI, pas seulement de l'humanité
- Les routines personnelles ont de la valeur
- Ta santé individuelle compte autant que le bien commun""",

    ('aquarius', 7): """# ☋ Nœud Sud en Verseau – Maison VII

**En une phrase :** Tes relations amicales et détachées doivent s'ouvrir à l'intimité vraie.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison des partenariats révèle des relations qui restent au niveau de l'amitié plutôt que de l'intimité profonde. Ce transit t'invite à l'engagement émotionnel.

## Ce que tu pourrais vivre
- Des relations qui évitent l'intimité vraie
- Un besoin de liberté qui empêche l'engagement
- Des partenariats plus intellectuels qu'émotionnels

## Conseils pour ce transit
- L'amour implique la vulnérabilité, pas seulement le respect
- La liberté et l'intimité peuvent coexister
- Engage-toi émotionnellement, pas seulement intellectuellement""",

    ('aquarius', 8): """# ☋ Nœud Sud en Verseau – Maison VIII

**En une phrase :** Ton détachement face aux crises doit céder à l'immersion émotionnelle.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison des transformations révèle une tendance à intellectualiser les crises plutôt que de les traverser émotionnellement. Ce transit t'invite à plonger.

## Ce que tu pourrais vivre
- Des crises observées de loin plutôt que vécues
- Une intimité qui évite les profondeurs émotionnelles
- Un détachement qui empêche la vraie transformation

## Conseils pour ce transit
- Les transformations se vivent, elles ne s'analysent pas
- L'intimité vraie inclut les émotions difficiles
- Plonge dans l'expérience plutôt que de la regarder""",

    ('aquarius', 9): """# ☋ Nœud Sud en Verseau – Maison IX

**En une phrase :** Ta philosophie intellectuelle et impersonnelle doit s'ouvrir au cœur.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison de l'expansion révèle une spiritualité trop intellectuelle ou des croyances qui manquent de chaleur. Ce transit t'invite à une sagesse du cœur.

## Ce que tu pourrais vivre
- Des croyances brillantes mais froides
- Une philosophie qui analyse plutôt qu'elle n'inspire
- Des voyages vers l'idée plutôt que vers l'expérience

## Conseils pour ce transit
- La sagesse inclut le cœur, pas seulement l'esprit
- Voyage pour ressentir, pas seulement pour comprendre
- Ta philosophie peut être personnelle et chaleureuse""",

    ('aquarius', 10): """# ☋ Nœud Sud en Verseau – Maison X

**En une phrase :** Ta carrière au service de causes impersonnelles doit inclure ta réalisation personnelle.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison de la carrière révèle une réussite basée sur la contribution collective au détriment de l'accomplissement personnel. Ce transit t'invite à l'équilibre.

## Ce que tu pourrais vivre
- Une carrière qui sert des idéaux mais pas TES désirs
- Un succès impersonnel qui ne te nourrit pas
- Un détachement de ta propre ambition

## Conseils pour ce transit
- Ta réussite personnelle compte aussi
- Tu peux servir le collectif ET t'accomplir personnellement
- L'ambition personnelle n'est pas égoïste""",

    ('aquarius', 11): """# ☋ Nœud Sud en Verseau – Maison XI

**En une phrase :** Ta vie sociale dispersée dans les groupes doit s'ouvrir aux relations personnelles.

## L'énergie du moment
Le Nœud Sud en Verseau est dans sa maison naturelle, amplifiant la tendance à se perdre dans le collectif au détriment des relations personnelles. Ce transit t'invite à l'intimité.

## Ce que tu pourrais vivre
- Des amitiés nombreuses mais impersonnelles
- Des causes qui prennent toute la place
- Un sentiment de faire partie du groupe sans liens vrais

## Conseils pour ce transit
- Les relations personnelles nourrissent autant que le collectif
- L'amitié vraie est intime et personnelle
- Tes causes ont besoin de ton cœur, pas seulement de ta tête""",

    ('aquarius', 12): """# ☋ Nœud Sud en Verseau – Maison XII

**En une phrase :** Ton détachement spirituel doit céder à l'amour et à la compassion.

## L'énergie du moment
Le Nœud Sud en Verseau dans ta maison de l'invisible révèle une spiritualité qui observe de loin plutôt que de se fondre dans l'amour universel. Ce transit t'invite à la dévotion.

## Ce que tu pourrais vivre
- Une spiritualité intellectuelle et détachée
- Un karma de séparation à libérer
- Une difficulté à ressentir l'unité avec tout ce qui est

## Conseils pour ce transit
- Le divin se ressent par le cœur, pas seulement par l'esprit
- L'union mystique est une expérience d'amour
- Libère le karma de séparation par la compassion""",

    # ============== PISCES ==============
    ('pisces', 1): """# ☋ Nœud Sud en Poissons – Maison I

**En une phrase :** Ton identité diffuse et ta tendance à te perdre doivent céder à l'affirmation de soi.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison I révèle une identité floue, une difficulté à savoir qui tu es vraiment. Ce transit t'invite à l'incarnation et à l'affirmation de soi.

## Ce que tu pourrais vivre
- Une difficulté à te définir et à t'affirmer
- Une tendance à te perdre dans les autres ou les rêves
- Une image de victime ou de martyr à transcender

## Conseils pour ce transit
- Tu existes en tant qu'individu distinct
- L'affirmation de soi n'est pas de l'égoïsme
- Incarne-toi pleinement dans le monde matériel""",

    ('pisces', 2): """# ☋ Nœud Sud en Poissons – Maison II

**En une phrase :** Ton rapport flou à l'argent et à la valeur doit se structurer.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison des ressources révèle une difficulté à gérer l'argent et à reconnaître ta propre valeur. Ce transit t'invite à la structure et à la clarté.

## Ce que tu pourrais vivre
- Des finances chaotiques ou qui fuient entre tes doigts
- Une difficulté à te valoriser concrètement
- Une générosité excessive qui te laisse démuni(e)

## Conseils pour ce transit
- L'argent peut être géré avec clarté et méthode
- Ta valeur mérite d'être reconnue concrètement
- La structure financière n'est pas contraire à la spiritualité""",

    ('pisces', 3): """# ☋ Nœud Sud en Poissons – Maison III

**En une phrase :** Ta communication floue et intuitive doit s'ancrer dans la clarté.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison de la communication révèle une parole qui manque parfois de clarté ou se perd dans l'abstrait. Ce transit t'invite à la précision.

## Ce que tu pourrais vivre
- Des communications floues ou mal comprises
- Une difficulté à exprimer clairement tes idées
- Des relations avec l'entourage marquées par la confusion

## Conseils pour ce transit
- La clarté dans la communication est une force
- L'intuition peut s'exprimer de façon précise
- Apprends à organiser tes pensées avant de les partager""",

    ('pisces', 4): """# ☋ Nœud Sud en Poissons – Maison IV

**En une phrase :** Ton foyer idéalisé ou chaotique doit trouver de vraies fondations.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison des racines révèle un rapport au foyer et à la famille marqué par l'idéalisation, la confusion ou la fuite. Ce transit t'invite à l'ancrage réel.

## Ce que tu pourrais vivre
- Un foyer où les limites sont floues
- Une famille idéalisée ou diabolisée
- Un passé marqué par l'évasion ou le sacrifice

## Conseils pour ce transit
- Ton foyer a besoin de structure réelle
- Vois ta famille telle qu'elle est, pas telle que tu l'imagines
- Crée des fondations solides, pas des rêves""",

    ('pisces', 5): """# ☋ Nœud Sud en Poissons – Maison V

**En une phrase :** Ta créativité diffuse et tes amours sacrificielles doivent s'affirmer.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison de la joie révèle une créativité qui se perd et des amours où tu te sacrifies. Ce transit t'invite à la joie saine et à l'affirmation créative.

## Ce que tu pourrais vivre
- Une créativité qui ne se concrétise jamais
- Des amours où tu te perds ou te sacrifies
- Un plaisir qui fuit vers l'évasion ou les addictions

## Conseils pour ce transit
- Concrétise tes créations, ne les laisse pas flotter
- L'amour sain n'exige pas de te perdre
- Le vrai plaisir est présent, pas évadé""",

    ('pisces', 6): """# ☋ Nœud Sud en Poissons – Maison VI

**En une phrase :** Ton chaos quotidien et ton service sacrificiel doivent se structurer.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison du travail révèle un quotidien chaotique ou un service aux autres qui t'épuise. Ce transit t'invite à la structure et aux limites saines.

## Ce que tu pourrais vivre
- Un travail sans limites qui te consume
- Des routines inexistantes ou chaotiques
- Une santé affectée par le manque de structure

## Conseils pour ce transit
- Le service ne nécessite pas le sacrifice de soi
- Les routines et limites sont des protections
- Ta santé a besoin de structure et de discernement""",

    ('pisces', 7): """# ☋ Nœud Sud en Poissons – Maison VII

**En une phrase :** Tes relations fusionnelles et tes partenariats idéalisés doivent s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison des partenariats révèle une tendance à fusionner, idéaliser ou te sacrifier dans les relations. Ce transit t'invite à l'équilibre et à la clarté.

## Ce que tu pourrais vivre
- Des relations où tu te perds dans l'autre
- Des partenaires idéalisés qui déçoivent
- Des sauvetages de partenaires qui t'épuisent

## Conseils pour ce transit
- L'amour n'est pas la fusion, l'équilibre est possible
- Vois tes partenaires tels qu'ils sont vraiment
- Tu n'as pas à sauver l'autre pour être aimé(e)""",

    ('pisces', 8): """# ☋ Nœud Sud en Poissons – Maison VIII

**En une phrase :** Ton abandon total dans les crises doit trouver un équilibre avec le discernement.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison des transformations révèle une tendance à se dissoudre dans les crises ou à fuir dans l'évasion. Ce transit t'invite au discernement dans l'abandon.

## Ce que tu pourrais vivre
- Des crises où tu te perds complètement
- Une intimité sans limites qui te consume
- Des fuites dans les addictions face aux transformations

## Conseils pour ce transit
- L'abandon peut être discernant, pas aveugle
- L'intimité vraie inclut des limites saines
- Traverse les crises conscient(e), pas évadé(e)""",

    ('pisces', 9): """# ☋ Nœud Sud en Poissons – Maison IX

**En une phrase :** Ta spiritualité fusionnelle doit s'ancrer dans le discernement.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison de l'expansion révèle une spiritualité qui se perd dans le tout, des croyances floues ou une tendance à suivre des gourous. Ce transit t'invite au discernement.

## Ce que tu pourrais vivre
- Des croyances confuses ou changeantes
- Une spiritualité qui manque de discernement
- Des voyages qui sont des fuites plutôt que des découvertes

## Conseils pour ce transit
- La vraie sagesse inclut le discernement
- Ta spiritualité peut être profonde ET claire
- Voyage pour découvrir, pas pour fuir""",

    ('pisces', 10): """# ☋ Nœud Sud en Poissons – Maison X

**En une phrase :** Ta carrière floue ou sacrificielle doit s'affirmer avec clarté.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison de la carrière révèle une réussite qui te sacrifie ou une vocation qui reste floue. Ce transit t'invite à l'affirmation professionnelle.

## Ce que tu pourrais vivre
- Une carrière qui te consume par le service excessif
- Une direction professionnelle floue ou changeante
- Une difficulté à assumer le pouvoir et le succès

## Conseils pour ce transit
- Ta carrière peut être au service ET t'accomplir
- Définis clairement ta direction professionnelle
- Assume ton pouvoir et ton succès sans culpabilité""",

    ('pisces', 11): """# ☋ Nœud Sud en Poissons – Maison XI

**En une phrase :** Ta dissolution dans les groupes et tes idéaux flous doivent s'affirmer.

## L'énergie du moment
Le Nœud Sud en Poissons dans ta maison des amitiés révèle une tendance à te perdre dans les groupes ou à avoir des idéaux si vastes qu'ils n'ont pas de forme. Ce transit t'invite à la clarté.

## Ce que tu pourrais vivre
- Des groupes où tu perds ton identité
- Des amitiés où tu joues le sauveur
- Des idéaux trop vagues pour se concrétiser

## Conseils pour ce transit
- Tu peux appartenir à un groupe ET garder ton identité
- L'amitié n'est pas le sacrifice de soi
- Tes idéaux ont besoin de forme concrète pour se réaliser""",

    ('pisces', 12): """# ☋ Nœud Sud en Poissons – Maison XII

**En une phrase :** Ta dissolution spirituelle doit s'équilibrer avec l'incarnation.

## L'énergie du moment
Le Nœud Sud en Poissons est dans sa maison naturelle, amplifiant la tendance à fuir le monde, à te dissoudre dans l'invisible ou à vivre dans les rêves. Ce transit t'invite à l'incarnation.

## Ce que tu pourrais vivre
- Une fuite spirituelle hors du monde
- Des rêves qui remplacent la vie réelle
- Un karma de dissolution et de perte de soi

## Conseils pour ce transit
- La spiritualité vraie s'incarne dans le monde
- Les rêves sont des guides, pas des refuges
- Tu es venu(e) pour vivre, pas pour disparaître""",
}


async def insert_interpretations():
    """Insert South Node transit interpretations for Sagittarius, Capricorn, Aquarius, Pisces"""
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
        print(f"✅ Transit South Node (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
