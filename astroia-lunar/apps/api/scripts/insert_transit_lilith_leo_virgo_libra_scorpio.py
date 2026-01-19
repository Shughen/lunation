#!/usr/bin/env python3
"""
Insert transit_lilith interpretations V2 for Leo, Virgo, Libra, Scorpio (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_LILITH_INTERPRETATIONS = {
    # ============== LEO (Lion) ==============
    ('leo', 1): """# ⚸ Transit de Lilith en Lion — Maison 1

**En une phrase :** Ta présence devient irrésistible et tu refuses de briller à moitié.

## L'énergie du moment
Lilith en Lion dans ta maison 1 éveille un magnétisme royal et une soif de reconnaissance brute. Tu ne supportes plus d'être ignoré·e ou sous-estimé·e. Ta présence devient plus théâtrale, plus assumée, parfois plus provocante. Tu veux briller sans demander la permission.

## Ce que tu pourrais vivre
- Une présence qui attire naturellement tous les regards
- Un ego qui s'affirme avec force, parfois jusqu'à l'excès
- Des réactions polarisées : on t'adore ou on te jalouse

## Conseils pour ce transit
- Brille sans écraser les autres : la vraie grandeur élève
- Ta créativité veut s'exprimer : donne-lui une scène
- L'attention que tu cherches, donne-la-toi d'abord toi-même""",

    ('leo', 2): """# ⚸ Transit de Lilith en Lion — Maison 2

**En une phrase :** Ta valeur personnelle est liée à ta capacité de briller et de créer.

## L'énergie du moment
Lilith traverse ta maison des ressources avec l'éclat du Lion. Tu veux être rémunéré·e à la hauteur de ton talent unique. Des tensions peuvent naître si tu sens que ta valeur n'est pas reconnue. Tu peux dépenser généreusement pour maintenir une image brillante.

## Ce que tu pourrais vivre
- Un besoin de ressources qui soutiennent ton expression créative
- Des dépenses luxueuses ou excessives pour briller
- Des frustrations si ton talent n'est pas valorisé financièrement

## Conseils pour ce transit
- Ta créativité a une valeur : fais-la reconnaître
- Le luxe extérieur ne remplace pas la richesse intérieure
- Investis dans ce qui te permet de briller authentiquement""",

    ('leo', 3): """# ⚸ Transit de Lilith en Lion — Maison 3

**En une phrase :** Ta parole devient un spectacle et tu refuses d'être banal·e.

## L'énergie du moment
Lilith traverse ta maison de la communication avec la théâtralité du Lion. Tu veux que tes mots marquent, impressionnent, inspirent. Tu peux avoir un style expressif, dramatique, parfois excessif. Les échanges deviennent des scènes où tu joues le premier rôle.

## Ce que tu pourrais vivre
- Une façon de communiquer plus expressive et captivante
- Un besoin d'être entendu·e et admiré·e dans les échanges
- Des tensions avec l'entourage si tu monopolises l'attention

## Conseils pour ce transit
- Ta parole a du pouvoir : utilise-la pour inspirer
- Laisse aussi la place aux autres dans les conversations
- L'écriture créative peut être un excellent exutoire""",

    ('leo', 4): """# ⚸ Transit de Lilith en Lion — Maison 4

**En une phrase :** Ton foyer doit refléter ta grandeur ou tu t'y sens à l'étroit.

## L'énergie du moment
Lilith secoue ta maison 4 avec la fierté du Lion. Tu veux un espace qui te ressemble, qui impressionne, qui rayonne. Des enjeux d'égo peuvent émerger dans la famille. Tu peux vouloir être le soleil de ton foyer, ce qui peut créer des tensions.

## Ce que tu pourrais vivre
- Un besoin de transformer ton espace en palace personnel
- Des tensions familiales autour de questions de reconnaissance
- Une redéfinition de ta place dans la famille

## Conseils pour ce transit
- Ton foyer peut être un lieu de créativité et de joie
- Prendre sa place en famille ne signifie pas éclipser les autres
- Les blessures d'égo familiales peuvent guérir dans l'amour""",

    ('leo', 5): """# ⚸ Transit de Lilith en Lion — Maison 5

**En une phrase :** Ta créativité et tes amours deviennent incandescentes.

## L'énergie du moment
Lilith est très puissante en Lion dans la maison 5, son terrain de jeu naturel. Ta créativité brûle d'une intensité rare. Tes amours sont passionnées, dramatiques, inoubliables. Tu veux vivre des expériences qui te font te sentir vivant·e et admiré·e.

## Ce que tu pourrais vivre
- Une période de créativité exceptionnelle et audacieuse
- Des romances intenses où tu veux être adoré·e
- Un besoin de prendre des risques pour te sentir vibrant·e

## Conseils pour ce transit
- Crée comme si ta vie en dépendait : elle en sera transformée
- En amour, cherche qui t'admire ET te voit vraiment
- Le jeu et le plaisir sont des besoins légitimes""",

    ('leo', 6): """# ⚸ Transit de Lilith en Lion — Maison 6

**En une phrase :** Le travail quotidien doit te permettre de briller ou il te consume.

## L'énergie du moment
Lilith traverse ta maison 6 avec l'exigence du Lion. Tu ne supportes plus un travail où tu es invisible ou interchangeable. Tu veux apporter ta touche unique, être reconnu·e pour ta contribution. Un travail qui ne te met pas en valeur devient insupportable.

## Ce que tu pourrais vivre
- Une frustration si ton travail ne te permet pas de briller
- Un besoin de reconnaissance quotidienne pour ta valeur
- Des tensions avec des collègues ou supérieurs qui t'éclipsent

## Conseils pour ce transit
- Ton travail quotidien peut devenir un art
- Cherche les occasions de montrer ta créativité, même petites
- La reconnaissance extérieure vient après la reconnaissance de soi""",

    ('leo', 7): """# ⚸ Transit de Lilith en Lion — Maison 7

**En une phrase :** Tes relations doivent t'élever ou elles deviennent étouffantes.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec l'exigence du Lion. Tu veux des relations où tu es admiré·e, où tu peux briller, où l'autre reconnaît ta grandeur. Des tensions peuvent naître si le partenaire te vole la vedette ou ne te voit pas.

## Ce que tu pourrais vivre
- Une attraction pour des partenaires qui t'admirent
- Des conflits d'égo dans le couple, chacun voulant briller
- Un besoin de relations qui te mettent en valeur

## Conseils pour ce transit
- Les meilleures relations permettent à chacun de briller
- Admirer l'autre ne diminue pas ta propre lumière
- La générosité dans l'amour attire l'admiration authentique""",

    ('leo', 8): """# ⚸ Transit de Lilith en Lion — Maison 8

**En une phrase :** Ta puissance de transformation devient visible et peut intimider.

## L'énergie du moment
Lilith traverse ta maison 8 avec l'intensité dramatique du Lion. Ta capacité de transformation est puissante et ne passe pas inaperçue. Les questions de pouvoir, de contrôle, de sexualité sont vécues avec une intensité théâtrale. Tu peux fasciner ou effrayer.

## Ce que tu pourrais vivre
- Une sexualité intense où tu veux être adoré·e
- Des transformations spectaculaires, visibles de l'extérieur
- Des enjeux de pouvoir où l'égo joue un rôle central

## Conseils pour ce transit
- La vraie puissance n'a pas besoin de démonstration
- L'intimité demande de lâcher le masque royal
- Ta capacité de renaissance peut inspirer les autres""",

    ('leo', 9): """# ⚸ Transit de Lilith en Lion — Maison 9

**En une phrase :** Ta quête de sens doit être épique et inspirante.

## L'énergie du moment
Lilith traverse ta maison 9 avec la grandeur du Lion. Tu cherches des croyances qui t'élèvent, des aventures qui font de toi un héros. Les philosophies plates ne t'intéressent pas, tu veux de l'inspiration et de la noblesse. Tu peux vouloir enseigner ou guider.

## Ce que tu pourrais vivre
- Un attrait pour des spiritualités ou des philosophies grandioses
- Un désir de voyages qui te transforment en héros de ta propre histoire
- Une envie d'enseigner, de partager ta vision du monde

## Conseils pour ce transit
- La vraie grandeur est dans le service, pas dans l'égo spirituel
- Tes aventures peuvent inspirer les autres
- La sagesse et l'humilité peuvent coexister avec la noblesse""",

    ('leo', 10): """# ⚸ Transit de Lilith en Lion — Maison 10

**En une phrase :** Ta carrière doit te couronner ou elle ne vaut pas ton investissement.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'ambition du Lion. Tu veux une carrière royale, où ta singularité est reconnue, où tu as une place de choix. Les compromis qui te diminuent deviennent intolérables. Tu veux briller dans le monde, pas te fondre dans la masse.

## Ce que tu pourrais vivre
- Un désir intense de reconnaissance professionnelle
- Des tensions avec des autorités qui ne reconnaissent pas ta valeur
- Un besoin de créer ta propre scène si celle qu'on t'offre est trop petite

## Conseils pour ce transit
- Ta carrière peut être une œuvre créative
- La vraie autorité vient de l'intérieur
- Brille sans écraser ceux qui travaillent avec toi""",

    ('leo', 11): """# ⚸ Transit de Lilith en Lion — Maison 11

**En une phrase :** Tes cercles sociaux doivent te permettre de briller ou ils t'ennuient.

## L'énergie du moment
Lilith traverse ta maison 11 avec le besoin de reconnaissance du Lion. Tu veux faire partie de cercles où tu es apprécié·e pour ta singularité. Les groupes où tu dois t'effacer ne t'intéressent plus. Tu peux devenir le centre d'un groupe ou créer le tien.

## Ce que tu pourrais vivre
- Une position de leader naturel dans les groupes
- Des tensions si tu sens que tes contributions sont invisibilisées
- Un attrait pour des cercles créatifs ou inspirants

## Conseils pour ce transit
- Les meilleurs groupes célèbrent l'individualité de chacun
- Leadership et collaboration ne sont pas incompatibles
- Tes idéaux peuvent inspirer un collectif""",

    ('leo', 12): """# ⚸ Transit de Lilith en Lion — Maison 12

**En une phrase :** Ta soif de reconnaissance a des racines secrètes dans des blessures d'égo cachées.

## L'énergie du moment
Lilith en Lion dans ta maison 12 éclaire les zones d'ombre de ton égo. Des blessures de reconnaissance, des rêves de grandeur non réalisés, des hontes secrètes liées à ta valeur peuvent remonter. C'est un temps pour guérir ton rapport à la visibilité.

## Ce que tu pourrais vivre
- Des rêves de gloire ou des cauchemars d'humiliation
- Une confrontation avec ce que tu caches sur ton besoin de briller
- Un travail profond sur l'égo et ses illusions

## Conseils pour ce transit
- Ton besoin de briller vient peut-être d'une blessure ancienne
- La créativité secrète peut être très guérissante
- Briller intérieurement est le fondement de toute vraie lumière""",

    # ============== VIRGO (Vierge) ==============
    ('virgo', 1): """# ⚸ Transit de Lilith en Vierge — Maison 1

**En une phrase :** Ta perfectionnisme et ton sens critique deviennent des outils de transformation.

## L'énergie du moment
Lilith en Vierge dans ta maison 1 aiguise ton sens du détail et ta capacité d'analyse. Tu deviens plus critique envers toi-même et les autres. Ton corps peut devenir un sujet d'obsession ou de transformation. Tu refuses la médiocrité et l'à-peu-près.

## Ce que tu pourrais vivre
- Un regard plus acéré sur toi-même et ton image
- Un désir de perfectionner ton corps ou ton apparence
- Une tendance à l'autocritique qui peut être constructive ou destructrice

## Conseils pour ce transit
- La perfection est un horizon, pas une destination
- Ton sens critique peut servir l'amélioration, pas la destruction
- Ton corps mérite du soin, pas de la torture""",

    ('virgo', 2): """# ⚸ Transit de Lilith en Vierge — Maison 2

**En une phrase :** Ta valeur est liée à ta compétence et ton utilité concrète.

## L'énergie du moment
Lilith traverse ta maison des ressources avec la précision de la Vierge. Tu valorises ce qui est pratique, utile, bien fait. Tes finances peuvent être gérées de façon très méticuleuse ou au contraire te stresser par leur désordre. Tu veux que ta valeur soit reconnue pour ton travail concret.

## Ce que tu pourrais vivre
- Un rapport exigeant à l'argent et aux possessions
- Une valorisation de toi-même à travers tes compétences pratiques
- Du stress si tes finances ne sont pas parfaitement ordonnées

## Conseils pour ce transit
- Ta valeur dépasse ce que tu fais ou possèdes
- L'ordre financier peut être rassurant, pas obsessionnel
- Offre-toi la sécurité de savoir que tu es compétent·e""",

    ('virgo', 3): """# ⚸ Transit de Lilith en Vierge — Maison 3

**En une phrase :** Ta communication devient précise, analytique, parfois tranchante.

## L'énergie du moment
Lilith traverse ta maison de la communication avec le discernement de la Vierge. Tes mots sont choisis avec soin, ta pensée est analytique et précise. Tu peux être très critique dans tes échanges, ce qui peut blesser ou aider, selon ton intention.

## Ce que tu pourrais vivre
- Une communication plus structurée et détaillée
- Des critiques qui sortent facilement, parfois trop
- Un intérêt pour des sujets pratiques ou liés à la santé

## Conseils pour ce transit
- La critique constructive aide, la critique gratuite détruit
- Ton analyse est précieuse : partage-la avec bienveillance
- L'écriture technique ou pratique peut être un bon exutoire""",

    ('virgo', 4): """# ⚸ Transit de Lilith en Vierge — Maison 4

**En une phrase :** Ton foyer doit être ordonné et fonctionnel ou il te stresse.

## L'énergie du moment
Lilith secoue ta maison 4 avec l'exigence de la Vierge. Tu veux un espace parfaitement organisé, propre, fonctionnel. Des tensions familiales peuvent naître de ton besoin de tout contrôler. Tu peux aussi prendre soin de ta famille de façon très concrète.

## Ce que tu pourrais vivre
- Un besoin obsessionnel d'ordre et de propreté chez toi
- Des critiques envers les membres de ta famille
- Un rôle de service ou de soin dans le foyer

## Conseils pour ce transit
- L'ordre apaise, l'obsession épuise
- Ta famille n'a pas besoin d'être parfaite pour mériter ton amour
- Prendre soin est un acte d'amour, pas de contrôle""",

    ('virgo', 5): """# ⚸ Transit de Lilith en Vierge — Maison 5

**En une phrase :** Ta créativité s'exprime dans la précision et le raffinement.

## L'énergie du moment
Lilith traverse ta maison 5 avec la minutie de la Vierge. Ta créativité passe par l'artisanat, le détail, la perfection technique. Tes amours peuvent être analysées, critiquées, améliorées. Tu veux des plaisirs raffinés, pas grossiers.

## Ce que tu pourrais vivre
- Une créativité méticuleuse, artisanale, parfois perfectionniste
- Une tendance à analyser tes relations amoureuses au lieu de les vivre
- Un plaisir dans les choses bien faites, bien pensées

## Conseils pour ce transit
- L'art du détail est un art noble
- En amour, l'analyse doit laisser place au ressenti
- Le plaisir peut être simple et imparfait""",

    ('virgo', 6): """# ⚸ Transit de Lilith en Vierge — Maison 6

**En une phrase :** Ton quotidien et ta santé deviennent des sujets d'attention intense.

## L'énergie du moment
Lilith est puissante en Vierge dans la maison 6, son domaine naturel. Ta santé, ton travail quotidien, tes routines sont scrutés avec une attention extrême. Tu peux devenir très conscient·e de ce qui fonctionne ou non dans ton corps et ton quotidien.

## Ce que tu pourrais vivre
- Une conscience accrue de ton corps et de ses besoins
- Un perfectionnisme au travail qui peut épuiser
- Des changements drastiques dans tes habitudes de santé

## Conseils pour ce transit
- Ton corps te guide si tu l'écoutes sans obsession
- Le perfectionnisme au travail a ses limites
- Les petits ajustements quotidiens ont plus d'impact que les révolutions""",

    ('virgo', 7): """# ⚸ Transit de Lilith en Vierge — Maison 7

**En une phrase :** Tes relations sont passées au crible de ton sens critique.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec l'exigence de la Vierge. Tu vois clairement les défauts de tes partenaires, ce qui peut aider à améliorer les relations ou les détruire. Tu veux des relations qui fonctionnent bien, pas des idéaux impossibles.

## Ce que tu pourrais vivre
- Une tendance à critiquer tes partenaires
- Un désir de relations pratiques et fonctionnelles
- Des conflits si tes exigences sont irréalistes

## Conseils pour ce transit
- La critique constante tue l'amour
- Les relations parfaites n'existent pas
- Le service mutuel est une belle expression de l'amour""",

    ('virgo', 8): """# ⚸ Transit de Lilith en Vierge — Maison 8

**En une phrase :** Tu analyses les profondeurs avec une précision qui peut être dérangeante.

## L'énergie du moment
Lilith traverse ta maison 8 avec le scalpel de la Vierge. Tu veux comprendre les mécanismes des transformations, de la sexualité, des crises. Ta capacité d'analyse des zones d'ombre est remarquable, mais peut aussi devenir obsessionnelle.

## Ce que tu pourrais vivre
- Une analyse très fine de tes schémas psychologiques profonds
- Une approche de la sexualité qui peut être technique
- Une obsession pour comprendre ce qui se cache

## Conseils pour ce transit
- L'analyse aide mais ne remplace pas l'expérience
- Les profondeurs ne peuvent pas être entièrement cartographiées
- La guérison passe aussi par le ressenti, pas seulement la compréhension""",

    ('virgo', 9): """# ⚸ Transit de Lilith en Vierge — Maison 9

**En une phrase :** Tes croyances doivent être pratiques et vérifiables ou elles ne t'intéressent pas.

## L'énergie du moment
Lilith traverse ta maison 9 avec le pragmatisme de la Vierge. Tu rejettes les grandes théories qui ne s'appliquent pas. Tu veux une spiritualité concrète, des connaissances utiles, des voyages qui servent à quelque chose.

## Ce que tu pourrais vivre
- Un scepticisme envers les croyances non vérifiables
- Un attrait pour des connaissances pratiques et applicables
- Des critiques envers les systèmes de pensée flous

## Conseils pour ce transit
- Tout n'est pas mesurable ou vérifiable
- La pratique quotidienne est une forme de spiritualité
- Garde un espace pour le mystère dans ta vision du monde""",

    ('virgo', 10): """# ⚸ Transit de Lilith en Vierge — Maison 10

**En une phrase :** Ta carrière doit être irréprochable ou elle te frustre.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'exigence de la Vierge. Tu veux une réputation de compétence et de fiabilité. Le travail mal fait te frustre, que ce soit le tien ou celui des autres. Tu peux être très critique envers les systèmes professionnels.

## Ce que tu pourrais vivre
- Un perfectionnisme professionnel qui peut impressionner ou épuiser
- Des critiques envers les dysfonctionnements au travail
- Un besoin de reconnaissance pour ta compétence technique

## Conseils pour ce transit
- L'excellence est admirable, l'obsession est destructrice
- Ta capacité de critique peut améliorer les systèmes
- Le service est noble, l'épuisement ne l'est pas""",

    ('virgo', 11): """# ⚸ Transit de Lilith en Vierge — Maison 11

**En une phrase :** Tes cercles sociaux sont filtrés par leur utilité et leur fonctionnement.

## L'énergie du moment
Lilith traverse ta maison 11 avec le sens pratique de la Vierge. Tu veux des amitiés qui fonctionnent, des groupes efficaces, des causes concrètes. Les réseaux désorganisés ou les idéaux vagues te frustrent.

## Ce que tu pourrais vivre
- Un tri dans tes amitiés basé sur la fiabilité
- Un rôle de service ou d'amélioration dans les groupes
- Une critique des groupes qui ne fonctionnent pas bien

## Conseils pour ce transit
- Les vraies amitiés ne sont pas des contrats de service
- Tu peux aider les groupes à mieux fonctionner
- L'imperfection fait partie de l'humain""",

    ('virgo', 12): """# ⚸ Transit de Lilith en Vierge — Maison 12

**En une phrase :** Ton perfectionnisme a des racines cachées dans des peurs de ne pas être assez.

## L'énergie du moment
Lilith en Vierge dans ta maison 12 révèle les origines de ton exigence. Des peurs de ne pas être à la hauteur, des critiques intériorisées, des hontes liées à l'imperfection peuvent remonter. C'est un temps pour guérir ton rapport à l'erreur.

## Ce que tu pourrais vivre
- Des anxiétés cachées liées à la peur de mal faire
- Une confrontation avec tes voix critiques intérieures
- Des rêves où l'ordre et le désordre se confrontent

## Conseils pour ce transit
- Tu as le droit d'être imparfait·e
- La critique intérieure peut devenir une alliée bienveillante
- Le repos et le lâcher-prise sont des compétences à cultiver""",

    # ============== LIBRA (Balance) ==============
    ('libra', 1): """# ⚸ Transit de Lilith en Balance — Maison 1

**En une phrase :** Tu cherches ta propre voie entre l'harmonie et l'authenticité brute.

## L'énergie du moment
Lilith en Balance dans ta maison 1 crée une tension entre le désir de plaire et le besoin d'être vrai·e. Tu peux osciller entre une séduction raffinée et une provocation assumée. Ta beauté devient plus magnétique, ton charme plus ambigu.

## Ce que tu pourrais vivre
- Un questionnement sur l'image que tu projettes aux autres
- Une tension entre diplomatie et authenticité
- Un charme plus trouble, plus fascinant

## Conseils pour ce transit
- L'harmonie vraie n'exclut pas l'authenticité
- Ta beauté n'a pas besoin d'approbation
- Plaire à tout le monde, c'est ne plaire à personne vraiment""",

    ('libra', 2): """# ⚸ Transit de Lilith en Balance — Maison 2

**En une phrase :** Ta valeur est questionnée à travers le miroir des autres.

## L'énergie du moment
Lilith traverse ta maison des ressources avec la dépendance relationnelle de la Balance. Tu peux mesurer ta valeur à travers ce que les autres pensent de toi ou ce qu'ils t'apportent. Les questions de partage des ressources deviennent sensibles.

## Ce que tu pourrais vivre
- Une tendance à lier ta valeur au regard des autres
- Des enjeux autour de l'argent dans les relations
- Un questionnement sur ce qui t'appartient vraiment

## Conseils pour ce transit
- Ta valeur ne dépend pas du miroir des autres
- L'équilibre financier dans les relations est important
- Ce que tu possèdes vraiment est au-delà du matériel""",

    ('libra', 3): """# ⚸ Transit de Lilith en Balance — Maison 3

**En une phrase :** Ta communication oscille entre diplomatie et vérités dérangeantes.

## L'énergie du moment
Lilith traverse ta maison de la communication avec l'ambivalence de la Balance. Tu veux dire les choses avec grâce mais aussi avec vérité. Tu peux charmer avec tes mots ou révéler des vérités que les conventions cachaient.

## Ce que tu pourrais vivre
- Une parole qui hésite entre politesse et franchise
- Des échanges sur les relations et leur équilibre
- Une capacité à voir les deux côtés de chaque sujet

## Conseils pour ce transit
- L'élégance et la vérité peuvent coexister
- Voir les deux côtés n'empêche pas de choisir
- Les mots justes trouvent le chemin entre blesser et mentir""",

    ('libra', 4): """# ⚸ Transit de Lilith en Balance — Maison 4

**En une phrase :** Ton foyer doit être beau et harmonieux ou il te perturbe.

## L'énergie du moment
Lilith secoue ta maison 4 avec l'esthétisme de la Balance. Tu veux un espace raffiné, équilibré, agréable. Les conflits familiaux te sont particulièrement difficiles car tu voudrais que tout soit harmonieux. Tu peux jouer le rôle de médiateur dans la famille.

## Ce que tu pourrais vivre
- Un besoin de beauté et d'harmonie dans ton espace
- Un rôle de pacificateur dans les conflits familiaux
- Une tension entre maintenir la paix et être authentique

## Conseils pour ce transit
- La beauté intérieure de ton foyer compte autant que la décoration
- Être le médiateur permanent est épuisant
- Les conflits révèlent parfois des vérités nécessaires""",

    ('libra', 5): """# ⚸ Transit de Lilith en Balance — Maison 5

**En une phrase :** Tes amours et ta créativité sont imprégnées de raffinement et d'ambiguïté.

## L'énergie du moment
Lilith traverse ta maison 5 avec la séduction de la Balance. Tes relations amoureuses sont plus sophistiquées, plus esthétiques, mais aussi plus ambiguës. Ta créativité passe par l'équilibre des formes, la beauté, l'harmonie.

## Ce que tu pourrais vivre
- Des amours complexes où l'équilibre est difficile à trouver
- Une créativité artistique qui vise la beauté
- Un jeu de séduction plus élaboré

## Conseils pour ce transit
- L'amour n'est pas toujours harmonieux : accepte les dissonances
- Ta créativité peut révéler la beauté cachée
- Séduire et aimer vraiment sont deux choses différentes""",

    ('libra', 6): """# ⚸ Transit de Lilith en Balance — Maison 6

**En une phrase :** Ton quotidien doit être équilibré et agréable ou il t'épuise.

## L'énergie du moment
Lilith traverse ta maison 6 avec le besoin d'harmonie de la Balance. Tu souffres si ton environnement de travail est conflictuel ou laid. Tu recherches un équilibre entre travail et vie personnelle. Les relations au travail deviennent centrales.

## Ce que tu pourrais vivre
- Une sensibilité aux conflits et aux tensions au travail
- Un besoin d'équilibre entre différentes sphères de vie
- Une attention à l'esthétique de ton environnement quotidien

## Conseils pour ce transit
- L'harmonie au travail est importante mais pas toujours possible
- L'équilibre parfait est un mythe : vise le "assez bien"
- Embellir ton quotidien peut être thérapeutique""",

    ('libra', 7): """# ⚸ Transit de Lilith en Balance — Maison 7

**En une phrase :** Tes relations révèlent tes ombres autour de l'harmonie et du compromis.

## L'énergie du moment
Lilith est puissante en Balance dans la maison 7, son domaine. Tu es confronté·e à tes schémas relationnels, à ta façon de te perdre ou de te trouver dans l'autre. Les questions d'équité, de compromis, de dépendance sont au premier plan.

## Ce que tu pourrais vivre
- Des relations intenses qui révèlent tes patterns
- Des tensions autour de l'équilibre du donner et recevoir
- Une prise de conscience de ce que tu sacrifies pour l'harmonie

## Conseils pour ce transit
- Les relations sont des miroirs de ton rapport à toi-même
- L'harmonie vraie ne demande pas de se renier
- L'équilibre se trouve dans la conscience, pas dans le calcul""",

    ('libra', 8): """# ⚸ Transit de Lilith en Balance — Maison 8

**En une phrase :** Les transformations passent par les relations et ce qu'elles révèlent.

## L'énergie du moment
Lilith traverse ta maison 8 avec l'intensité relationnelle de la Balance. Les crises transformatrices viennent souvent des relations. L'intimité et le partage deviennent des terrains d'exploration profonde. Les questions de pouvoir dans le couple sont centrales.

## Ce que tu pourrais vivre
- Des transformations profondes initiées par les relations
- Une exploration de l'intimité et de ses enjeux de pouvoir
- Des questions sur les ressources partagées et l'équité

## Conseils pour ce transit
- Les relations peuvent être des catalyseurs de transformation
- L'intimité vraie demande de lâcher le contrôle
- Le partage équitable est un idéal, pas une comptabilité""",

    ('libra', 9): """# ⚸ Transit de Lilith en Balance — Maison 9

**En une phrase :** Ta quête de sens cherche l'équilibre entre différentes vérités.

## L'énergie du moment
Lilith traverse ta maison 9 avec la diplomatie de la Balance. Tu cherches une vision du monde qui intègre les opposés, qui trouve la vérité entre les extrêmes. Tu peux être attiré·e par les philosophies de l'harmonie ou critiquer les dogmes unilatéraux.

## Ce que tu pourrais vivre
- Une capacité à voir les mérites de différentes croyances
- Une difficulté à t'engager dans une seule voie spirituelle
- Un attrait pour l'art, la beauté comme voie de sagesse

## Conseils pour ce transit
- Toutes les vérités ne se valent pas, même si elles méritent d'être entendues
- L'équilibre philosophique peut aussi être une forme d'évitement
- La beauté peut être un chemin vers le sens""",

    ('libra', 10): """# ⚸ Transit de Lilith en Balance — Maison 10

**En une phrase :** Ta carrière doit être élégante et relationnelle ou elle ne te satisfait pas.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'esthétisme et le sens relationnel de la Balance. Tu veux une carrière qui passe par les relations, qui soit belle, qui crée de l'harmonie. Les environnements professionnels conflictuels ou laids te sont difficiles.

## Ce que tu pourrais vivre
- Un désir de carrière dans les domaines de la beauté ou des relations
- Des tensions si ton travail crée des conflits
- Un rôle de médiateur ou de diplomate dans ta profession

## Conseils pour ce transit
- Ta carrière peut créer de la beauté dans le monde
- Être professionnel·le ne signifie pas éviter tous les conflits
- Les relations professionnelles sont un capital précieux""",

    ('libra', 11): """# ⚸ Transit de Lilith en Balance — Maison 11

**En une phrase :** Tes cercles sociaux doivent être harmonieux ou tu t'en éloignes.

## L'énergie du moment
Lilith traverse ta maison 11 avec le besoin social de la Balance. Tu veux des amitiés équilibrées, des groupes où chacun a sa place. Les cercles conflictuels ou injustes te deviennent intolérables. Tu peux jouer un rôle de médiateur dans les groupes.

## Ce que tu pourrais vivre
- Un tri dans tes amitiés basé sur la qualité des échanges
- Un rôle de pacificateur dans les conflits de groupe
- Un attrait pour des causes liées à la justice et à l'équité

## Conseils pour ce transit
- Les amitiés équilibrées sont précieuses mais rares
- Être toujours le médiateur peut t'effacer
- Les idéaux de justice méritent ton engagement""",

    ('libra', 12): """# ⚸ Transit de Lilith en Balance — Maison 12

**En une phrase :** Tes ombres autour des relations et de l'harmonie émergent de l'inconscient.

## L'énergie du moment
Lilith en Balance dans ta maison 12 révèle ce que tu caches sur tes besoins relationnels. Des dépendances secrètes, des peurs de l'abandon, des compromis qui t'ont fait perdre ta vérité peuvent remonter. C'est un temps pour guérir tes blessures relationnelles.

## Ce que tu pourrais vivre
- Des rêves sur les relations et leurs enjeux cachés
- Une confrontation avec ta peur d'être seul·e
- Un travail sur ce que tu as sacrifié pour plaire

## Conseils pour ce transit
- L'harmonie avec toi-même précède l'harmonie avec les autres
- Les relations secrètes ou imaginaires parlent de tes besoins
- Tu peux être en relation ET être toi-même""",

    # ============== SCORPIO (Scorpion) ==============
    ('scorpio', 1): """# ⚸ Transit de Lilith en Scorpion — Maison 1

**En une phrase :** Ton magnétisme devient intense et ta présence transforme ceux qui t'approchent.

## L'énergie du moment
Lilith en Scorpion dans ta maison 1 est une configuration très puissante. Tu dégages une intensité qui ne laisse personne indifférent. Ta présence peut fasciner, intimider, attirer irrésistiblement. Tu refuses la superficialité et tu montres tes profondeurs.

## Ce que tu pourrais vivre
- Un magnétisme qui attire ou repousse fortement
- Une transformation profonde de ton image et de ta présence
- Des regards intenses des autres, de l'attraction ou de la méfiance

## Conseils pour ce transit
- Ton pouvoir de présence est immense : utilise-le consciemment
- La profondeur attire ceux qui sont prêts pour elle
- Tu n'as pas à t'excuser de ton intensité""",

    ('scorpio', 2): """# ⚸ Transit de Lilith en Scorpion — Maison 2

**En une phrase :** Tes ressources sont transformées par des cycles de mort et renaissance.

## L'énergie du moment
Lilith traverse ta maison des ressources avec l'intensité du Scorpion. Ton rapport à l'argent et aux possessions passe par des transformations profondes. Tu peux vivre des pertes qui se révèlent libératrices ou des gains qui viennent de zones sombres.

## Ce que tu pourrais vivre
- Des transformations financières parfois radicales
- Un rapport intense et complexe à l'argent
- Des questions sur ce que tu possèdes vraiment vs ce qui te possède

## Conseils pour ce transit
- Les pertes peuvent être des libérations déguisées
- Ton pouvoir sur les ressources est plus grand que tu ne le crois
- La vraie richesse survit à toutes les transformations""",

    ('scorpio', 3): """# ⚸ Transit de Lilith en Scorpion — Maison 3

**En une phrase :** Tes paroles ont le pouvoir de transformer ou de détruire.

## L'énergie du moment
Lilith traverse ta maison de la communication avec la puissance du Scorpion. Tes mots deviennent des instruments de transformation. Tu perces les apparences, tu dis ce que personne n'ose dire, tu touches les zones sensibles. Ton pouvoir de parole est immense.

## Ce que tu pourrais vivre
- Une communication intense qui va au cœur des choses
- Des révélations ou des confrontations avec l'entourage proche
- Une fascination pour les sujets tabous et les vérités cachées

## Conseils pour ce transit
- Tes paroles ont un pouvoir de vie ou de mort symbolique
- Révéler les vérités peut guérir ou blesser : choisis
- La communication profonde crée des liens vrais""",

    ('scorpio', 4): """# ⚸ Transit de Lilith en Scorpion — Maison 4

**En une phrase :** Les secrets de famille et les mémoires ancestrales remontent à la surface.

## L'énergie du moment
Lilith secoue ta maison 4 avec l'intensité du Scorpion. Les secrets de famille, les traumatismes hérités, les zones d'ombre du clan peuvent émerger. Ton rapport aux origines passe par une transformation profonde. Le foyer peut être un lieu de guérison intense.

## Ce que tu pourrais vivre
- Des révélations ou des confrontations familiales profondes
- Un travail sur les mémoires transgénérationnelles
- Une transformation radicale de ton rapport aux origines

## Conseils pour ce transit
- Les secrets de famille ont besoin de lumière pour être guéris
- Ton foyer peut être un lieu de transformation profonde
- Les mémoires ancestrales peuvent se libérer à travers toi""",

    ('scorpio', 5): """# ⚸ Transit de Lilith en Scorpion — Maison 5

**En une phrase :** Tes amours et ta créativité sont des expériences de transformation totale.

## L'énergie du moment
Lilith en Scorpion dans ta maison 5 crée des expériences intenses. Les amours sont des fournaises de transformation, la créativité puise dans les profondeurs les plus sombres. Tu ne veux pas d'aventures superficielles mais des expériences qui te transforment.

## Ce que tu pourrais vivre
- Des relations amoureuses intenses et transformatrices
- Une créativité qui explore les tabous et les profondeurs
- Des expériences de plaisir qui frôlent l'interdit

## Conseils pour ce transit
- L'amour peut être une initiation, pas juste un divertissement
- Ta créativité la plus puissante vient des zones d'ombre
- L'intensité n'est pas incompatible avec le respect""",

    ('scorpio', 6): """# ⚸ Transit de Lilith en Scorpion — Maison 6

**En une phrase :** Ton quotidien devient un terrain de transformation et de purification.

## L'énergie du moment
Lilith traverse ta maison 6 avec l'intensité du Scorpion. Ton rapport au travail et à la santé passe par des transformations profondes. Tu ne tolères plus ce qui t'empoisonne au quotidien. Des crises peuvent révéler ce qui doit changer.

## Ce que tu pourrais vivre
- Une intolérance totale aux environnements toxiques
- Des transformations de santé, parfois par des crises
- Un travail qui touche aux zones d'ombre ou à la transformation

## Conseils pour ce transit
- Ce qui ne te sert plus doit partir
- Les crises de santé sont des messagers : écoute-les
- Le quotidien peut être un chemin de transformation""",

    ('scorpio', 7): """# ⚸ Transit de Lilith en Scorpion — Maison 7

**En une phrase :** Tes relations sont des miroirs intenses où se jouent pouvoir et transformation.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec la profondeur du Scorpion. Les relations deviennent des champs d'exploration des enjeux de pouvoir, de contrôle, d'intimité. Tu attires des personnes intenses ou tu provoques l'intensité chez les autres.

## Ce que tu pourrais vivre
- Des relations qui transforment profondément les deux partenaires
- Des enjeux de pouvoir et de contrôle dans le couple
- Une attraction pour des personnes magnétiques et complexes

## Conseils pour ce transit
- Les jeux de pouvoir révèlent des blessures à guérir
- L'intimité vraie demande de lâcher le contrôle
- Les relations transformatrices sont les plus précieuses""",

    ('scorpio', 8): """# ⚸ Transit de Lilith en Scorpion — Maison 8

**En une phrase :** Tu es au cœur du volcan transformateur de ton existence.

## L'énergie du moment
Lilith est chez elle au maximum en Scorpion dans la maison 8. C'est un transit d'une puissance rare où tout ce qui est caché peut être révélé, où les transformations les plus profondes sont possibles. La mort et la renaissance sont des thèmes centraux.

## Ce que tu pourrais vivre
- Des transformations existentielles majeures
- Une exploration intense de la sexualité et de ses mystères
- Des confrontations avec la mort, le tabou, l'interdit

## Conseils pour ce transit
- Tu es capable de renaître de tes cendres
- Ce qui meurt en toi fait place à plus grand
- L'intensité de ce transit est une initiation""",

    ('scorpio', 9): """# ⚸ Transit de Lilith en Scorpion — Maison 9

**En une phrase :** Tes croyances sont transformées par des prises de conscience profondes.

## L'énergie du moment
Lilith traverse ta maison 9 avec la profondeur du Scorpion. Ta quête de sens passe par l'exploration des mystères, des zones d'ombre de la spiritualité, des vérités cachées. Tu peux être attiré·e par des traditions ésotériques ou remettre en question les dogmes.

## Ce que tu pourrais vivre
- Une exploration des dimensions occultes ou mystiques
- Une remise en question profonde de tes croyances
- Des voyages ou des rencontres qui transforment ta vision du monde

## Conseils pour ce transit
- Les mystères méritent d'être explorés avec respect
- Ta quête de vérité peut devenir obsessionnelle : équilibre
- Les vérités profondes transforment celui qui les trouve""",

    ('scorpio', 10): """# ⚸ Transit de Lilith en Scorpion — Maison 10

**En une phrase :** Ta carrière devient un terrain de transformation et de pouvoir.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'intensité du Scorpion. Tu veux une carrière qui a du pouvoir, qui transforme, qui touche aux profondeurs. Les jeux de pouvoir professionnels deviennent visibles. Ta réputation peut être intense : admirée ou crainte.

## Ce que tu pourrais vivre
- Une carrière liée à la transformation ou au pouvoir
- Des enjeux de pouvoir intenses dans le monde professionnel
- Une réputation magnétique qui fascine ou intimide

## Conseils pour ce transit
- Ton pouvoir professionnel peut transformer ou détruire
- Les jeux de pouvoir révèlent des enjeux plus profonds
- Une carrière alignée avec ta profondeur est la plus satisfaisante""",

    ('scorpio', 11): """# ⚸ Transit de Lilith en Scorpion — Maison 11

**En une phrase :** Tes cercles sociaux se transforment, seuls les liens profonds survivent.

## L'énergie du moment
Lilith traverse ta maison 11 avec l'intensité du Scorpion. Les amitiés superficielles ne te satisfont plus. Tu veux des liens qui vont au fond, des groupes qui transforment. Certaines relations peuvent mourir pour faire place à des connexions plus profondes.

## Ce que tu pourrais vivre
- Un tri radical dans tes amitiés et tes cercles
- Une attraction pour des groupes qui explorent les profondeurs
- Des enjeux de pouvoir ou de transformation dans les collectifs

## Conseils pour ce transit
- Les vraies amitiés survivent à l'intensité
- Les groupes de transformation peuvent être très puissants
- Tes idéaux méritent ta profondeur d'engagement""",

    ('scorpio', 12): """# ⚸ Transit de Lilith en Scorpion — Maison 12

**En une phrase :** Tu plonges dans les profondeurs ultimes de ton inconscient.

## L'énergie du moment
Lilith en Scorpion dans ta maison 12 est une configuration d'une profondeur extrême. Les couches les plus enfouies de ton inconscient peuvent être révélées. Des mémoires très anciennes, des traumatismes oubliés, des pouvoirs cachés peuvent émerger.

## Ce que tu pourrais vivre
- Des expériences psychiques ou spirituelles intenses
- Une confrontation avec tes peurs les plus profondes
- Des rêves très significatifs, parfois perturbants

## Conseils pour ce transit
- Ce qui émerge des profondeurs demande à être intégré
- Tu es plus fort·e que tes peurs les plus profondes
- L'accompagnement thérapeutique peut être précieux""",
}

async def insert_interpretations():
    """Insert all transit_lilith interpretations for Leo, Virgo, Libra, Scorpio"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_LILITH_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_lilith',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP: transit_lilith {sign} house {house} already exists")
                skipped += 1
                continue

            interpretation = PregeneratedNatalInterpretation(
                subject='transit_lilith',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interpretation)
            print(f"INSERT: transit_lilith {sign} house {house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nDone: {inserted} inserted, {skipped} skipped")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
