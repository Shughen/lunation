#!/usr/bin/env python3
"""Insert transit_neptune interpretations for Leo, Virgo, Libra, Scorpio (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_NEPTUNE_INTERPRETATIONS = {
    # ============================================================
    # NEPTUNE EN LION (♆ en ♌)
    # ============================================================
    ('leo', 1): """# ♆ Transit de Neptune en Lion — Maison I

**En une phrase :** Ton identité s'illumine d'une créativité spirituelle et tu incarnes l'artiste divin.

## L'énergie du moment
Neptune en Lion dans ta maison I apporte une dimension inspirée à ta présence. Tu rayonnes d'une lumière spirituelle, d'une créativité qui semble venir d'ailleurs. Ton ego se dissout pour laisser place à un canal créatif. Tu peux inspirer les autres par ta simple présence lumineuse.

## Ce que tu pourrais vivre
- Une présence rayonnante et inspirante
- La dissolution de l'ego au profit de la créativité divine
- Une confusion possible sur ton identité d'artiste
- L'incarnation d'une lumière spirituelle

## Conseils pour ce transit
- Laisse ta lumière briller sans ego
- Deviens un canal pour la créativité divine
- Reste humble malgré le rayonnement""",

    ('leo', 2): """# ♆ Transit de Neptune en Lion — Maison II

**En une phrase :** Tes talents créatifs deviennent des sources de revenus spirituels.

## L'énergie du moment
Neptune en Lion dans ta maison des ressources lie tes finances à ta créativité inspirée. Tu peux gagner ta vie par l'art, le spectacle, ou toute expression qui touche le cœur. Tes valeurs s'orientent vers ce qui fait briller l'âme plutôt que le compte en banque.

## Ce que tu pourrais vivre
- Des revenus liés à la créativité et à l'art
- Une valorisation de l'expression et de la lumière
- Une générosité qui peut dépasser la prudence
- La découverte que ta vraie richesse est ton rayonnement

## Conseils pour ce transit
- Monétise ta créativité de façon éthique
- Garde une gestion pratique malgré les rêves
- Investis dans ce qui nourrit ton âme créative""",

    ('leo', 3): """# ♆ Transit de Neptune en Lion — Maison III

**En une phrase :** Ta communication devient dramatique et inspirée, touchant les cœurs.

## L'énergie du moment
Neptune en Lion dans ta maison de la communication apporte une qualité théâtrale et inspirante à tes mots. Tu communiques comme un artiste, avec passion et émotion. Tes idées ont une dimension créative et généreuse. Attention à ne pas exagérer ou dramatiser.

## Ce que tu pourrais vivre
- Une communication expressive et touchante
- Des idées créatives et généreuses
- Une possible tendance à la dramatisation
- Des échanges passionnés avec les proches

## Conseils pour ce transit
- Utilise ton éloquence pour inspirer
- Garde un sens des proportions dans la communication
- Exprime ta créativité à travers tes mots""",

    ('leo', 4): """# ♆ Transit de Neptune en Lion — Maison IV

**En une phrase :** Ton foyer devient une scène de créativité et d'amour généreux.

## L'énergie du moment
Neptune en Lion dans ta maison IV transforme ton espace domestique en palais de créativité et de célébration. Tu veux un foyer qui brille, qui inspire, qui accueille avec générosité. Des idéaux élevés concernant la famille peuvent te guider ou te décevoir.

## Ce que tu pourrais vivre
- Un foyer transformé en espace créatif et festif
- Des idéaux élevés concernant la vie familiale
- Le besoin de briller au sein de ta famille
- Une générosité parfois excessive envers les proches

## Conseils pour ce transit
- Crée un foyer qui célèbre la vie
- Accepte que ta famille soit humaine, pas idéale
- Partage ta lumière avec tes proches""",

    ('leo', 5): """# ♆ Transit de Neptune en Lion — Maison V

**En une phrase :** Ta créativité atteint des sommets d'inspiration divine et tes amours deviennent des romances épiques.

## L'énergie du moment
Neptune traverse sa maison de joie avec l'énergie lumineuse du Lion. Ta créativité peut être exceptionnellement inspirée, presque channelée. En amour, tu vis des romances qui ressemblent à des contes de fées, avec le risque d'idéalisation. Le jeu et le plaisir prennent une dimension spirituelle.

## Ce que tu pourrais vivre
- Une créativité divinement inspirée
- Des amours romantiques et idéalisées
- Des plaisirs qui touchent l'âme
- Une connexion magique avec les enfants

## Conseils pour ce transit
- Canalise cette inspiration exceptionnelle
- Garde les pieds sur terre en amour
- Célèbre la vie avec joie et conscience""",

    ('leo', 6): """# ♆ Transit de Neptune en Lion — Maison VI

**En une phrase :** Ton travail quotidien devient une expression créative et ton bien-être dépend de ta joie.

## L'énergie du moment
Neptune en Lion dans ta maison du travail quotidien transforme tes tâches en performances créatives. Tu as besoin de briller même dans le quotidien. Ta santé est liée à ta joie de vivre et à ton expression créative. Un travail sans âme peut te rendre malade.

## Ce que tu pourrais vivre
- Un travail qui devient expression créative
- Une santé liée au bonheur et à la créativité
- Le besoin de reconnaissance dans le quotidien
- L'importance de la joie pour ton bien-être

## Conseils pour ce transit
- Injecte de la créativité dans ton quotidien
- Prends soin de toi par la joie et l'expression
- Trouve des façons de briller chaque jour""",

    ('leo', 7): """# ♆ Transit de Neptune en Lion — Maison VII

**En une phrase :** Tes relations deviennent des romances dignes de films et tu cherches un amour qui illumine.

## L'énergie du moment
Neptune en Lion traverse ta maison des partenariats avec une énergie de romance épique. Tu attires des partenaires créatifs, charismatiques, parfois théâtraux. Tu cherches un amour qui te fait briller et te fait sentir spécial. L'idéalisation est forte.

## Ce que tu pourrais vivre
- Des relations romantiques et passionnées
- Des partenaires créatifs ou dans le spectacle
- L'idéalisation intense des partenaires
- Le besoin de briller ensemble

## Conseils pour ce transit
- Apprécie la romance tout en restant lucide
- Choisis un partenaire qui t'aime, toi, pas l'image
- Créez ensemble plutôt que de rivaliser""",

    ('leo', 8): """# ♆ Transit de Neptune en Lion — Maison VIII

**En une phrase :** Des transformations profondes illuminent les zones d'ombre et révèlent ta puissance créative.

## L'énergie du moment
Neptune en Lion dans ta maison des transformations apporte la lumière dans les profondeurs. Ton ego peut traverser des morts symboliques qui libèrent ta vraie lumière créative. Les questions de pouvoir et de reconnaissance sont transformées. Tu découvres un rayonnement qui ne dépend pas de l'extérieur.

## Ce que tu pourrais vivre
- La transformation de ton besoin de reconnaissance
- La découverte d'une lumière intérieure stable
- Des expériences intimes qui révèlent ta vraie puissance
- La dissolution de l'ego pour une créativité plus pure

## Conseils pour ce transit
- Accepte la mort de l'ego superficiel
- Découvre ta vraie lumière intérieure
- Transforme le besoin d'approbation en rayonnement authentique""",

    ('leo', 9): """# ♆ Transit de Neptune en Lion — Maison IX

**En une phrase :** Ta quête spirituelle devient une aventure héroïque vers la lumière divine.

## L'énergie du moment
Neptune en Lion traverse ta maison des horizons lointains avec une énergie de quête lumineuse. Tu es attiré par des spiritualités qui célèbrent la lumière, la joie, la créativité divine. Tes voyages peuvent te mener vers des lieux d'inspiration et de célébration.

## Ce que tu pourrais vivre
- Une spiritualité joyeuse et lumineuse
- Des voyages vers des lieux d'art et d'inspiration
- Une philosophie qui célèbre la vie et la créativité
- L'attrait pour des traditions festives et lumineuses

## Conseils pour ce transit
- Développe une spiritualité joyeuse
- Voyage vers des lieux qui t'inspirent
- Intègre la célébration dans ta pratique spirituelle""",

    ('leo', 10): """# ♆ Transit de Neptune en Lion — Maison X

**En une phrase :** Ta carrière s'oriente vers l'art ou l'inspiration et tu deviens connu pour ta lumière.

## L'énergie du moment
Neptune en Lion dans ta maison de la carrière inspire une vocation créative et lumineuse. Tu peux devenir artiste, performer, inspirateur. Ta réputation se construit autour de ta capacité à illuminer et à toucher les cœurs. Le chemin vers le succès peut être flou mais guidé par l'inspiration.

## Ce que tu pourrais vivre
- Une carrière dans l'art, le spectacle ou l'inspiration
- Une réputation de personne lumineuse et créative
- Une direction professionnelle guidée par l'inspiration
- Le besoin d'une carrière qui a du cœur

## Conseils pour ce transit
- Poursuis une carrière qui te permet de briller authentiquement
- Accepte que le succès vienne de façon inattendue
- Inspire les autres par ton travail""",

    ('leo', 11): """# ♆ Transit de Neptune en Lion — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des collectifs créatifs et tes aspirations brillent d'idéaux.

## L'énergie du moment
Neptune en Lion traverse ta maison des amitiés avec une énergie de création collective. Tu es attiré par des groupes d'artistes, de créatifs, de personnes qui veulent illuminer le monde. Tes aspirations incluent apporter plus de lumière et de joie dans le collectif.

## Ce que tu pourrais vivre
- Des amitiés avec des créatifs et des rêveurs
- L'attrait pour des collectifs artistiques
- Des aspirations d'apporter de la lumière au monde
- Une possible idéalisation des groupes ou des causes

## Conseils pour ce transit
- Rejoins des collectifs créatifs et inspirants
- Contribue par ta lumière au bien commun
- Reste lucide sur les dynamiques de groupe""",

    ('leo', 12): """# ♆ Transit de Neptune en Lion — Maison XII

**En une phrase :** Une transformation profonde de ton ego révèle la lumière divine en toi.

## L'énergie du moment
Neptune en Lion dans ta maison des profondeurs travaille sur la dissolution de l'ego pour révéler ta vraie lumière. Des besoins inconscients de reconnaissance peuvent être guéris. Tu découvres une créativité qui vient de la source divine plutôt que de l'ego. L'humilité et le rayonnement se rejoignent.

## Ce que tu pourrais vivre
- La dissolution des besoins d'ego inconscients
- La découverte d'une créativité sans ego
- Des rêves de lumière et de transformation
- L'accès à une source créative universelle

## Conseils pour ce transit
- Laisse l'ego se dissoudre dans la lumière divine
- Découvre une créativité qui ne cherche pas la gloire
- Rayonne sans avoir besoin d'approbation""",

    # ============================================================
    # NEPTUNE EN VIERGE (♆ en ♍)
    # ============================================================
    ('virgo', 1): """# ♆ Transit de Neptune en Vierge — Maison I

**En une phrase :** Ton identité s'oriente vers le service spirituel et la guérison humble.

## L'énergie du moment
Neptune en Vierge dans ta maison I crée une identité dédiée au service et à la guérison. Tu incarnes l'archétype du guérisseur ou du serviteur spirituel. Ta présence a une qualité purificatrice et apaisante. Tu peux te sentir appelé à aider et à améliorer.

## Ce que tu pourrais vivre
- Une identité orientée vers le service
- Une présence purificatrice et guérisseuse
- Un possible sentiment de ne jamais en faire assez
- L'incarnation de l'humilité spirituelle

## Conseils pour ce transit
- Sers sans te perdre dans le perfectionnisme
- Accepte que l'imperfection fasse partie du voyage
- Deviens un canal humble de guérison""",

    ('virgo', 2): """# ♆ Transit de Neptune en Vierge — Maison II

**En une phrase :** Tes valeurs s'orientent vers l'utilité spirituelle et le service qui a du sens.

## L'énergie du moment
Neptune en Vierge dans ta maison des ressources lie tes finances au service et à la guérison. Tu peux gagner ta vie par des activités qui améliorent, guérissent ou purifient. Tes vraies valeurs sont dans ce qui est utile et significatif plutôt que ostentatoire.

## Ce que tu pourrais vivre
- Des revenus liés aux métiers de soin ou de service
- Une valorisation de l'utilité et de la qualité
- Une confusion possible si l'argent semble "impur"
- La découverte que la vraie richesse est dans le service

## Conseils pour ce transit
- Trouve une façon de gagner ta vie par le service
- Accepte que l'argent puisse être utilisé pour le bien
- Valorise la qualité sur la quantité""",

    ('virgo', 3): """# ♆ Transit de Neptune en Vierge — Maison III

**En une phrase :** Ta communication devient un outil de guérison et d'amélioration.

## L'énergie du moment
Neptune en Vierge dans ta maison de la communication apporte une qualité analytique mais aussi intuitive à tes échanges. Tu communiques pour aider, améliorer, guérir. Tes mots peuvent avoir un effet thérapeutique. Attention au perfectionnisme dans la communication.

## Ce que tu pourrais vivre
- Une communication orientée vers l'aide
- Des conseils intuitifs et pratiques
- Un possible perfectionnisme dans l'expression
- Une écoute empathique des détails significatifs

## Conseils pour ce transit
- Utilise tes mots pour guérir et améliorer
- Évite la critique excessive
- Écoute les détails qui révèlent le vrai besoin""",

    ('virgo', 4): """# ♆ Transit de Neptune en Vierge — Maison IV

**En une phrase :** Ton foyer devient un lieu de guérison et de purification spirituelle.

## L'énergie du moment
Neptune en Vierge dans ta maison IV transforme ton espace domestique en sanctuaire de santé et de pureté. Tu aspires à un foyer sain, ordonné, au service du bien-être. Des patterns familiaux liés au perfectionnisme ou au service peuvent être révélés et guéris.

## Ce que tu pourrais vivre
- Un foyer orienté vers la santé et la pureté
- La guérison de patterns familiaux perfectionnistes
- Le besoin de servir et prendre soin des proches
- Un espace domestique simplifié et purifié

## Conseils pour ce transit
- Crée un foyer qui soutient la santé de tous
- Guéris les patterns de perfectionnisme familial
- Trouve la paix dans l'ordre sans l'obsession""",

    ('virgo', 5): """# ♆ Transit de Neptune en Vierge — Maison V

**En une phrase :** Ta créativité s'exprime dans l'artisanat et tes amours cherchent la perfection.

## L'énergie du moment
Neptune en Vierge dans ta maison de la créativité apporte une expression artistique détaillée et technique. Tu es attiré par l'artisanat, les arts qui demandent précision et dévouement. En amour, tu peux chercher le partenaire parfait ou vouloir améliorer tes relations.

## Ce que tu pourrais vivre
- Une créativité technique et artisanale
- Des amours marquées par le désir d'amélioration
- Le plaisir de perfectionner et d'affiner
- Des attentes élevées en romance

## Conseils pour ce transit
- Exprime ta créativité dans l'artisanat et le détail
- Accepte l'imperfection en amour
- Trouve la beauté dans le travail bien fait""",

    ('virgo', 6): """# ♆ Transit de Neptune en Vierge — Maison VI

**En une phrase :** Ton quotidien devient une pratique spirituelle de service et ta santé une priorité sacrée.

## L'énergie du moment
Neptune traverse sa maison naturelle d'exil avec l'énergie de la Vierge, créant une tension créative. Ton travail quotidien devient une forme de service spirituel. Ta santé est intimement liée à ta capacité de servir et à ton état spirituel. L'équilibre entre perfectionnisme et acceptation est clé.

## Ce que tu pourrais vivre
- Un travail vécu comme service spirituel
- Une santé sensible à l'état mental et spirituel
- Le besoin d'un environnement de travail pur et sain
- Des pratiques de santé holistiques et détaillées

## Conseils pour ce transit
- Fais de ton travail une offrande
- Prends soin de ta santé avec attention mais sans obsession
- Sers sans t'épuiser""",

    ('virgo', 7): """# ♆ Transit de Neptune en Vierge — Maison VII

**En une phrase :** Tes relations deviennent des espaces d'amélioration mutuelle et de service partagé.

## L'énergie du moment
Neptune en Vierge traverse ta maison des partenariats avec une énergie de perfectionnement relationnel. Tu attires des partenaires orientés vers le service ou la santé. Les relations peuvent être vues comme des projets d'amélioration. Attention au criticisme ou aux attentes irréalistes.

## Ce que tu pourrais vivre
- Des relations orientées vers l'aide mutuelle
- Des partenaires dans les domaines de la santé ou du service
- Le risque de vouloir perfectionner l'autre
- Le service comme langage d'amour

## Conseils pour ce transit
- Aidez-vous mutuellement sans vous critiquer
- Acceptez les imperfections de chacun
- Servez ensemble une cause plus grande""",

    ('virgo', 8): """# ♆ Transit de Neptune en Vierge — Maison VIII

**En une phrase :** Des transformations profondes purifient et guérissent tes patterns les plus anciens.

## L'énergie du moment
Neptune en Vierge dans ta maison des transformations apporte une guérison méthodique des blessures profondes. Tu analyses et purifies les patterns inconscients. La transformation passe par la compréhension et le service. Des perfectionnismes inconscients peuvent être révélés et libérés.

## Ce que tu pourrais vivre
- Une guérison analytique et méthodique
- La purification de patterns profonds
- La transformation par le service et la compréhension
- La libération de perfectionnismes inconscients

## Conseils pour ce transit
- Guéris avec méthode et compassion
- Analyse sans te perdre dans les détails
- Sers ta propre transformation comme tu servirais un autre""",

    ('virgo', 9): """# ♆ Transit de Neptune en Vierge — Maison IX

**En une phrase :** Ta quête spirituelle devient pratique et tu cherches des sagesses applicables.

## L'énergie du moment
Neptune en Vierge traverse ta maison des horizons lointains avec une spiritualité pragmatique. Tu es attiré par des enseignements qui ont des applications pratiques pour améliorer la vie. Tes voyages peuvent inclure des retraites de santé ou des pèlerinages de service.

## Ce que tu pourrais vivre
- Une spiritualité orientée vers l'application pratique
- Des voyages de service ou de guérison
- L'intérêt pour des traditions de santé et de pureté
- Une philosophie du service et de l'amélioration

## Conseils pour ce transit
- Cherche des sagesses qui se vivent au quotidien
- Voyage pour servir et apprendre
- Intègre spiritualité et pratique quotidienne""",

    ('virgo', 10): """# ♆ Transit de Neptune en Vierge — Maison X

**En une phrase :** Ta carrière s'oriente vers le service et la guérison à une échelle plus large.

## L'énergie du moment
Neptune en Vierge dans ta maison de la carrière inspire une vocation de service et de guérison. Tu peux devenir reconnu pour ta capacité à améliorer, guérir, servir. Ta réputation se construit sur ta compétence humble et ton dévouement.

## Ce que tu pourrais vivre
- Une carrière dans la santé, le service ou l'amélioration
- Une réputation de personne compétente et serviable
- Une confusion possible sur la direction si le service n'est pas clair
- Le besoin d'une carrière qui aide vraiment

## Conseils pour ce transit
- Poursuis une carrière de service authentique
- Construis ta réputation sur la compétence et l'humilité
- Serve à travers ton métier""",

    ('virgo', 11): """# ♆ Transit de Neptune en Vierge — Maison XI

**En une phrase :** Tes cercles sociaux s'orientent vers le service collectif et l'amélioration du monde.

## L'énergie du moment
Neptune en Vierge traverse ta maison des amitiés avec une énergie de service collectif. Tu es attiré par des groupes qui œuvrent pour améliorer concrètement la société. Tes aspirations incluent un monde meilleur par des actions pratiques et significatives.

## Ce que tu pourrais vivre
- Des amitiés basées sur le service partagé
- L'attrait pour des organisations humanitaires pratiques
- Des aspirations d'amélioration concrète du monde
- Le don de tes compétences au collectif

## Conseils pour ce transit
- Rejoins des groupes de service efficace
- Contribue par tes compétences spécifiques
- Rêve d'un monde meilleur et agis pour le créer""",

    ('virgo', 12): """# ♆ Transit de Neptune en Vierge — Maison XII

**En une phrase :** Une guérison profonde de tes patterns de perfectionnisme et de critique inconscients.

## L'énergie du moment
Neptune en Vierge dans ta maison des profondeurs travaille sur tes tendances perfectionnistes et auto-critiques inconscientes. Des standards impossibles que tu t'imposes peuvent être révélés et libérés. Tu découvres que l'imperfection est parfaite et que le service vient de l'amour, pas du devoir.

## Ce que tu pourrais vivre
- La guérison du perfectionnisme inconscient
- La libération de l'auto-critique excessive
- Des rêves révélant des standards impossibles
- La découverte du service par amour, pas par devoir

## Conseils pour ce transit
- Sois compatissant avec tes imperfections
- Libère les standards impossibles
- Découvre le service joyeux et non obligé""",

    # ============================================================
    # NEPTUNE EN BALANCE (♆ en ♎)
    # ============================================================
    ('libra', 1): """# ♆ Transit de Neptune en Balance — Maison I

**En une phrase :** Ton identité se teinte de grâce et tu incarnes l'harmonie et la beauté.

## L'énergie du moment
Neptune en Balance dans ta maison I apporte une qualité de grâce et d'harmonie à ta présence. Tu rayonnes de beauté et de paix. Ton identité peut être difficile à définir car tu reflètes ce que les autres ont besoin de voir. Tu incarnes un idéal de beauté et d'équilibre.

## Ce que tu pourrais vivre
- Une présence gracieuse et harmonieuse
- Une identité qui s'adapte aux autres
- Le risque de te perdre en voulant plaire
- L'incarnation d'un idéal esthétique

## Conseils pour ce transit
- Cultive ta propre identité au-delà de ce que les autres veulent
- Utilise ta grâce pour créer l'harmonie
- Reste toi-même tout en étant adaptable""",

    ('libra', 2): """# ♆ Transit de Neptune en Balance — Maison II

**En une phrase :** Tes valeurs s'orientent vers la beauté et l'harmonie comme vraies richesses.

## L'énergie du moment
Neptune en Balance dans ta maison des ressources lie tes finances à l'art et à l'harmonie. Tu peux gagner ta vie par la beauté, la diplomatie ou la création d'équilibre. Tes vraies valeurs sont esthétiques et relationnelles. L'argent peut être compliqué dans les partenariats.

## Ce que tu pourrais vivre
- Des revenus liés à l'art, la beauté ou la diplomatie
- Une valorisation de l'harmonie et de l'esthétique
- Des finances floues dans les arrangements partagés
- La générosité pour maintenir l'harmonie

## Conseils pour ce transit
- Trouve une façon de valoriser la beauté
- Clarifie les arrangements financiers dans les relations
- Investis dans ce qui crée l'harmonie""",

    ('libra', 3): """# ♆ Transit de Neptune en Balance — Maison III

**En une phrase :** Ta communication devient diplomatique et poétique, créant des ponts.

## L'énergie du moment
Neptune en Balance dans ta maison de la communication apporte une qualité diplomatique et artistique à tes mots. Tu communiques pour créer l'harmonie, parfois au détriment de la vérité directe. Tes idées cherchent l'équilibre et la beauté. Attention à éviter les conflits au point de ne plus rien dire.

## Ce que tu pourrais vivre
- Une communication diplomatique et harmonieuse
- Des idées qui cherchent l'équilibre des perspectives
- Le risque d'éviter les vérités difficiles
- Une expression artistique et poétique

## Conseils pour ce transit
- Communique avec grâce tout en restant honnête
- Cherche l'harmonie sans sacrifier la vérité
- Exprime-toi avec beauté""",

    ('libra', 4): """# ♆ Transit de Neptune en Balance — Maison IV

**En une phrase :** Ton foyer devient un sanctuaire de beauté et d'harmonie relationnelle.

## L'énergie du moment
Neptune en Balance dans ta maison IV transforme ton espace domestique en havre de paix et de beauté. Tu aspires à un foyer harmonieux où les relations sont équilibrées. Des idéaux de famille parfaite peuvent te guider ou te décevoir.

## Ce que tu pourrais vivre
- Un foyer transformé en espace d'art et d'harmonie
- Des idéaux de relations familiales parfaites
- Le besoin d'équilibre dans la vie domestique
- La décoration comme expression spirituelle

## Conseils pour ce transit
- Crée un espace de beauté et de paix
- Accepte que les relations familiales soient imparfaites
- Trouve l'harmonie intérieure avant de la chercher à l'extérieur""",

    ('libra', 5): """# ♆ Transit de Neptune en Balance — Maison V

**En une phrase :** Ta créativité s'exprime dans l'harmonie et tes amours deviennent des œuvres d'art.

## L'énergie du moment
Neptune en Balance dans ta maison de la créativité apporte une expression artistique raffinée et équilibrée. Tu es attiré par les arts qui créent la beauté et l'harmonie. En amour, tu cherches le partenaire idéal, la romance parfaite, avec le risque d'idéalisation.

## Ce que tu pourrais vivre
- Une créativité harmonieuse et esthétique
- Des amours romantiques et idéalisées
- La recherche de la relation parfaite
- Le plaisir dans la beauté et l'art

## Conseils pour ce transit
- Exprime ta créativité dans la recherche du beau
- Aime les personnes réelles, pas les idéaux
- Trouve la beauté dans l'imperfection de l'amour""",

    ('libra', 6): """# ♆ Transit de Neptune en Balance — Maison VI

**En une phrase :** Ton quotidien s'harmonise et ta santé bénéficie de l'équilibre.

## L'énergie du moment
Neptune en Balance dans ta maison du travail quotidien transforme tes routines en quête d'équilibre. Ton environnement de travail doit être harmonieux et beau. Ta santé est sensible aux déséquilibres relationnels et bénéficie de la paix.

## Ce que tu pourrais vivre
- Un travail dans un environnement harmonieux
- Une santé liée à l'équilibre relationnel
- Le besoin de beauté dans le quotidien
- Des relations de travail diplomatiques

## Conseils pour ce transit
- Crée un environnement de travail harmonieux
- Prends soin de l'équilibre dans ta vie
- Intègre la beauté dans ton quotidien""",

    ('libra', 7): """# ♆ Transit de Neptune en Balance — Maison VII

**En une phrase :** Tes relations atteignent une dimension spirituelle d'union idéale.

## L'énergie du moment
Neptune traverse son signe d'exaltation dans ta maison des partenariats, maximisant la quête de l'amour idéal. Tu cherches l'âme sœur parfaite, l'union spirituelle ultime. Les relations peuvent atteindre des sommets romantiques mais aussi des déceptions si l'idéal ne se matérialise pas.

## Ce que tu pourrais vivre
- La recherche de l'amour parfait et spirituel
- Des relations romantiques intenses et idéalisées
- Le risque de grandes déceptions amoureuses
- Des partenaires artistes ou spirituels

## Conseils pour ce transit
- Apprécie les relations réelles au-delà des idéaux
- Recherche la croissance spirituelle en couple
- Maintiens ton identité dans l'union""",

    ('libra', 8): """# ♆ Transit de Neptune en Balance — Maison VIII

**En une phrase :** Des transformations profondes touchent ta façon de fusionner et de partager.

## L'énergie du moment
Neptune en Balance dans ta maison des transformations dissout les frontières dans les relations intimes. Tu peux vivre des fusions profondes avec les partenaires. Les questions de partage et d'équité dans les ressources communes peuvent être floues mais aussi purifiées.

## Ce que tu pourrais vivre
- Des fusions profondes dans l'intimité
- La transformation de ta façon de partager
- Des questions floues sur les ressources communes
- La découverte de l'équité spirituelle dans les échanges

## Conseils pour ce transit
- Clarifie les arrangements financiers partagés
- Explore la dimension spirituelle de l'intimité
- Maintiens l'équilibre dans les échanges profonds""",

    ('libra', 9): """# ♆ Transit de Neptune en Balance — Maison IX

**En une phrase :** Ta quête spirituelle s'oriente vers l'harmonie universelle et la beauté divine.

## L'énergie du moment
Neptune en Balance traverse ta maison des horizons lointains avec une vision d'harmonie cosmique. Tu es attiré par des philosophies qui prônent la paix, la beauté et l'équilibre. Tes voyages peuvent te mener vers des lieux d'art et de culture raffinée.

## Ce que tu pourrais vivre
- Une spiritualité orientée vers la paix et l'harmonie
- Des voyages vers des lieux de beauté et de culture
- L'attrait pour des traditions esthétiques et équilibrées
- Une vision du monde basée sur l'interconnexion harmonieuse

## Conseils pour ce transit
- Développe une spiritualité de beauté et de paix
- Voyage vers des lieux qui nourrissent ton sens esthétique
- Intègre l'harmonie dans ta philosophie de vie""",

    ('libra', 10): """# ♆ Transit de Neptune en Balance — Maison X

**En une phrase :** Ta carrière s'oriente vers l'art, la diplomatie ou la création d'harmonie.

## L'énergie du moment
Neptune en Balance dans ta maison de la carrière inspire une vocation artistique ou diplomatique. Tu peux devenir reconnu pour ta capacité à créer la beauté ou à résoudre les conflits. Ta réputation se construit sur ta grâce et ton sens de l'équilibre.

## Ce que tu pourrais vivre
- Une carrière dans l'art, la mode ou la diplomatie
- Une réputation de personne gracieuse et équilibrée
- Une direction professionnelle qui cherche l'harmonie
- Le besoin d'une carrière belle et significative

## Conseils pour ce transit
- Poursuis une carrière qui crée de la beauté
- Utilise ta diplomatie professionnellement
- Construis ta réputation sur la grâce et l'équilibre""",

    ('libra', 11): """# ♆ Transit de Neptune en Balance — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des espaces d'harmonie et tes aspirations incluent la paix mondiale.

## L'énergie du moment
Neptune en Balance traverse ta maison des amitiés avec une énergie de fraternité harmonieuse. Tu es attiré par des groupes qui œuvrent pour la paix, la justice et la beauté. Tes aspirations incluent un monde plus harmonieux et équitable.

## Ce que tu pourrais vivre
- Des amitiés basées sur l'harmonie et l'esthétique
- L'attrait pour des mouvements de paix et d'art
- Des aspirations de justice et d'équilibre mondial
- Une possible idéalisation des groupes

## Conseils pour ce transit
- Rejoins des groupes qui créent l'harmonie
- Contribue à la paix et à la beauté collective
- Reste lucide sur les dynamiques de groupe""",

    ('libra', 12): """# ♆ Transit de Neptune en Balance — Maison XII

**En une phrase :** Une guérison profonde de tes patterns de dépendance relationnelle inconscients.

## L'énergie du moment
Neptune en Balance dans ta maison des profondeurs travaille sur tes patterns relationnels inconscients. Des tendances à te perdre dans l'autre, à éviter le conflit à tout prix, ou à chercher ton identité dans les relations peuvent être révélées et guéries. Tu découvres une harmonie intérieure.

## Ce que tu pourrais vivre
- La guérison de patterns de co-dépendance
- La libération du besoin d'approbation relationnelle
- Des rêves révélant des idéaux relationnels irréalistes
- La découverte de l'équilibre intérieur autonome

## Conseils pour ce transit
- Travaille sur ton équilibre intérieur
- Libère le besoin de l'autre pour te sentir complet
- Découvre l'harmonie qui ne dépend pas de l'extérieur""",

    # ============================================================
    # NEPTUNE EN SCORPION (♆ en ♏)
    # ============================================================
    ('scorpio', 1): """# ♆ Transit de Neptune en Scorpion — Maison I

**En une phrase :** Ton identité se transforme profondément vers une présence magnétique et mystérieuse.

## L'énergie du moment
Neptune en Scorpion dans ta maison I apporte une intensité mystérieuse à ta présence. Tu dégages une aura de profondeur et de mystère. Ton identité traverse des morts et renaissances subtiles. Tu peux devenir un canal pour des énergies de transformation et de guérison profonde.

## Ce que tu pourrais vivre
- Une présence magnétique et mystérieuse
- Des transformations profondes de l'identité
- La dissolution et renaissance de qui tu es
- L'incarnation du mystère et de la profondeur

## Conseils pour ce transit
- Accepte les transformations de ton identité
- Utilise ton magnétisme avec éthique
- Explore les profondeurs de ton être""",

    ('scorpio', 2): """# ♆ Transit de Neptune en Scorpion — Maison II

**En une phrase :** Ta relation aux ressources se transforme profondément vers des valeurs spirituelles.

## L'énergie du moment
Neptune en Scorpion dans ta maison des ressources dissout les attachements matériels pour révéler des richesses plus profondes. Tes finances peuvent être liées à des domaines transformateurs ou occultes. Tu découvres que le vrai pouvoir n'est pas dans l'argent mais dans la transformation intérieure.

## Ce que tu pourrais vivre
- La transformation de ta relation à l'argent
- Des finances liées à des domaines de transformation
- La dissolution d'attachements matériels profonds
- La découverte de ressources intérieures puissantes

## Conseils pour ce transit
- Laisse tes attachements matériels se transformer
- Explore les ressources de ton monde intérieur
- Utilise l'argent comme outil de transformation""",

    ('scorpio', 3): """# ♆ Transit de Neptune en Scorpion — Maison III

**En une phrase :** Ta communication devient pénétrante et tes mots peuvent transformer.

## L'énergie du moment
Neptune en Scorpion dans ta maison de la communication apporte une profondeur et une intensité à tes échanges. Tu captes les non-dits, les secrets, les vérités cachées. Tes mots ont le pouvoir de transformer ceux qui les reçoivent. Attention à la manipulation ou à l'utilisation négative de cette capacité.

## Ce que tu pourrais vivre
- Une communication qui perce les surfaces
- L'intérêt pour les sujets tabous et mystérieux
- Des échanges transformateurs avec les proches
- Le risque de manipulation verbale

## Conseils pour ce transit
- Utilise ton pouvoir de communication pour guérir
- Respecte les secrets des autres
- Transforme par les mots avec éthique""",

    ('scorpio', 4): """# ♆ Transit de Neptune en Scorpion — Maison IV

**En une phrase :** Ton foyer devient un lieu de transformation profonde et de guérison ancestrale.

## L'énergie du moment
Neptune en Scorpion dans ta maison IV transforme ton espace domestique en chaudron de transformation. Des secrets familiaux peuvent émerger. La guérison des lignées ancestrales est possible. Ta sécurité vient de ta capacité à traverser les transformations.

## Ce que tu pourrais vivre
- Des révélations sur les secrets familiaux
- La guérison de blessures ancestrales profondes
- Un foyer qui devient lieu de transformation
- Des expériences intenses dans la vie familiale

## Conseils pour ce transit
- Accueille les révélations familiales avec courage
- Guéris les blessures ancestrales qui émergent
- Fais de ton foyer un lieu de renaissance""",

    ('scorpio', 5): """# ♆ Transit de Neptune en Scorpion — Maison V

**En une phrase :** Ta créativité puise dans les profondeurs et tes amours deviennent des transformations.

## L'énergie du moment
Neptune en Scorpion dans ta maison de la créativité apporte une expression artistique intense et transformatrice. Tu crées des œuvres qui touchent l'âme profonde, qui transforment ceux qui les reçoivent. En amour, tu vis des passions intenses qui te changent en profondeur.

## Ce que tu pourrais vivre
- Une créativité qui explore les profondeurs
- Des amours passionnelles et transformatrices
- Des plaisirs intenses et parfois obsessionnels
- Des créations qui touchent le tabou et le mystère

## Conseils pour ce transit
- Canalise l'intensité dans la création
- Accepte que l'amour te transforme
- Explore les profondeurs avec discernement""",

    ('scorpio', 6): """# ♆ Transit de Neptune en Scorpion — Maison VI

**En une phrase :** Ton quotidien devient une pratique de transformation et ta santé une régénération.

## L'énergie du moment
Neptune en Scorpion dans ta maison du travail quotidien transforme tes routines en pratiques de transformation. Tu peux être attiré par des métiers de guérison profonde ou de transformation. Ta santé passe par la régénération et la purification profonde.

## Ce que tu pourrais vivre
- Un travail lié à la transformation ou la guérison
- Une santé qui passe par des crises régénératrices
- Des pratiques de purification profonde
- Des relations de travail intenses

## Conseils pour ce transit
- Fais de ton quotidien une pratique de transformation
- Accepte les crises de santé comme des purifications
- Travaille dans un domaine qui transforme""",

    ('scorpio', 7): """# ♆ Transit de Neptune en Scorpion — Maison VII

**En une phrase :** Tes relations deviennent des alchimies de transformation mutuelle.

## L'énergie du moment
Neptune en Scorpion traverse ta maison des partenariats avec une énergie de fusion transformatrice. Tu attires des partenaires intenses avec qui tu vis des transformations profondes. Les relations peuvent être des chaudrons alchimiques où les deux partenaires sont changés. L'intensité peut être enivrante ou destructrice.

## Ce que tu pourrais vivre
- Des relations intenses et transformatrices
- Des partenaires magnétiques et profonds
- Des fusions qui changent les deux personnes
- Le risque de relations toxiques si mal canalisées

## Conseils pour ce transit
- Choisis des partenaires qui grandissent avec toi
- Transforme-toi dans la relation sans te perdre
- Utilise l'intensité pour la croissance mutuelle""",

    ('scorpio', 8): """# ♆ Transit de Neptune en Scorpion — Maison VIII

**En une phrase :** Des transformations profondes et mystiques t'ouvrent aux mystères de l'existence.

## L'énergie du moment
Neptune traverse sa maison de profondeur avec l'intensité du Scorpion, créant une puissance transformatrice maximale. Tu peux vivre des expériences mystiques profondes, des morts et renaissances symboliques puissantes. L'accès aux dimensions invisibles est facilité. Les peurs les plus profondes peuvent être transcendées.

## Ce que tu pourrais vivre
- Des expériences mystiques et transformatrices profondes
- La transcendance des peurs les plus anciennes
- L'accès aux dimensions subtiles et invisibles
- Des transformations radicales et irréversibles

## Conseils pour ce transit
- Accueille les transformations profondes avec confiance
- Explore les mystères avec discernement
- Utilise cette période pour une guérison profonde""",

    ('scorpio', 9): """# ♆ Transit de Neptune en Scorpion — Maison IX

**En une phrase :** Ta quête spirituelle plonge dans les mystères occultes et les traditions ésotériques.

## L'énergie du moment
Neptune en Scorpion traverse ta maison des horizons lointains avec une soif de mystère. Tu es attiré par les traditions ésotériques, occultes, celles qui explorent les mystères de la vie et de la mort. Tes voyages peuvent te mener vers des lieux de pouvoir ou d'initiation.

## Ce que tu pourrais vivre
- L'attrait pour les traditions ésotériques et occultes
- Des voyages vers des lieux de pouvoir spirituel
- Une philosophie qui intègre les mystères
- Des révélations profondes sur le sens de l'existence

## Conseils pour ce transit
- Explore les traditions occultes avec discernement
- Voyage vers des lieux qui t'initient
- Intègre le mystère dans ta compréhension du monde""",

    ('scorpio', 10): """# ♆ Transit de Neptune en Scorpion — Maison X

**En une phrase :** Ta carrière s'oriente vers des domaines de transformation profonde et de pouvoir.

## L'énergie du moment
Neptune en Scorpion dans ta maison de la carrière inspire une vocation liée à la transformation. Tu peux devenir reconnu pour ta capacité à guérir profondément, à transformer les situations, à accéder aux mystères. Ta réputation peut être entourée de mystère ou de controverse.

## Ce que tu pourrais vivre
- Une carrière dans la guérison, la psychologie profonde ou l'occulte
- Une réputation de personne profonde et transformatrice
- Des changements de carrière radicaux
- Le pouvoir et ses responsabilités

## Conseils pour ce transit
- Utilise ton pouvoir professionnel avec éthique
- Poursuis une carrière qui transforme vraiment
- Accepte le mystère qui entoure ta réputation""",

    ('scorpio', 11): """# ♆ Transit de Neptune en Scorpion — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des fraternités de transformation et tes aspirations touchent aux mystères collectifs.

## L'énergie du moment
Neptune en Scorpion traverse ta maison des amitiés avec une énergie de transformation collective. Tu es attiré par des groupes qui travaillent sur des transformations profondes de la société ou de la conscience. Des amitiés intenses et karmiques sont possibles.

## Ce que tu pourrais vivre
- Des amitiés intenses et transformatrices
- L'attrait pour des groupes occultes ou de transformation
- Des aspirations de transformation collective profonde
- Des liens karmiques dans les cercles sociaux

## Conseils pour ce transit
- Rejoins des groupes de transformation authentique
- Contribue aux changements collectifs profonds
- Maintiens ton discernement dans les groupes intenses""",

    ('scorpio', 12): """# ♆ Transit de Neptune en Scorpion — Maison XII

**En une phrase :** Une transformation profonde de ton inconscient te libère des karmas les plus anciens.

## L'énergie du moment
Neptune en Scorpion dans ta maison des profondeurs travaille sur les couches les plus anciennes de ton psychisme et de ton karma. Des vies passées ou des mémoires ancestrales très profondes peuvent être révélées et libérées. Tu accèdes à des pouvoirs de guérison et de transformation qui dépassent l'ordinaire.

## Ce que tu pourrais vivre
- La libération de karmas très anciens
- L'accès à des mémoires de vies passées
- Des rêves intenses et transformateurs
- Le développement de capacités psychiques profondes

## Conseils pour ce transit
- Accueille ce qui remonte des profondeurs
- Utilise cette période pour une guérison karmique
- Développe tes dons avec responsabilité""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in TRANSIT_NEPTUNE_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_neptune',
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
                subject='transit_neptune',
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
        print(f"✅ Transit Neptune (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
