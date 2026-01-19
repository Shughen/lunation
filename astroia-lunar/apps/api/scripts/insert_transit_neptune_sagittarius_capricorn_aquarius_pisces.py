#!/usr/bin/env python3
"""Insert transit_neptune interpretations for Sagittarius, Capricorn, Aquarius, Pisces (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_NEPTUNE_INTERPRETATIONS = {
    # ============================================================
    # NEPTUNE EN SAGITTAIRE (♆ en ♐)
    # ============================================================
    ('sagittarius', 1): """# ♆ Transit de Neptune en Sagittaire — Maison I

**En une phrase :** Ton identité s'ouvre à des dimensions spirituelles vastes et tu incarnes le chercheur mystique.

## L'énergie du moment
Neptune en Sagittaire dans ta maison I apporte une dimension de quête spirituelle à ton identité. Tu rayonnes d'optimisme et de foi, incarnant le pèlerin ou le prophète. Ta présence peut inspirer et élever, mais attention à ne pas te perdre dans des croyances sans fondement.

## Ce que tu pourrais vivre
- Une identité de chercheur spirituel
- Un rayonnement d'optimisme et de foi
- Le risque de croyances excessives ou naïves
- L'incarnation du guide ou de l'enseignant

## Conseils pour ce transit
- Cherche la vérité avec ouverture et discernement
- Inspire par ta foi sans imposer tes croyances
- Reste ancré tout en explorant les horizons""",

    ('sagittarius', 2): """# ♆ Transit de Neptune en Sagittaire — Maison II

**En une phrase :** Tes valeurs s'élèvent vers la spiritualité et tes ressources viennent de ta foi.

## L'énergie du moment
Neptune en Sagittaire dans ta maison des ressources lie tes finances à tes croyances et à ta quête de sens. Tu peux gagner ta vie par l'enseignement spirituel, les voyages ou l'édition. La foi que tout s'arrangera peut t'aider ou te rendre imprudent.

## Ce que tu pourrais vivre
- Des revenus liés à l'enseignement ou aux voyages
- Une valorisation de la sagesse et de l'expérience
- La générosité basée sur la foi en l'abondance
- Un risque de négligence des détails financiers

## Conseils pour ce transit
- Fais confiance à l'univers tout en étant pratique
- Monétise ta sagesse et tes expériences
- Équilibre foi et prudence dans les finances""",

    ('sagittarius', 3): """# ♆ Transit de Neptune en Sagittaire — Maison III

**En une phrase :** Ta communication devient philosophique et inspirante, portant des messages de sens.

## L'énergie du moment
Neptune en Sagittaire dans ta maison de la communication apporte une dimension philosophique et inspirante à tes échanges. Tu parles de sens, de but, de spiritualité. Tes idées peuvent être visionnaires mais parfois trop abstraites pour le quotidien.

## Ce que tu pourrais vivre
- Une communication philosophique et inspirante
- Des idées qui cherchent le sens et la vérité
- Un possible manque de précision dans les détails
- Des échanges qui élèvent les conversations

## Conseils pour ce transit
- Partage tes visions tout en restant accessible
- Vérifie les détails dans les communications importantes
- Inspire par tes mots avec humilité""",

    ('sagittarius', 4): """# ♆ Transit de Neptune en Sagittaire — Maison IV

**En une phrase :** Ton foyer devient un temple d'exploration spirituelle et de foi.

## L'énergie du moment
Neptune en Sagittaire dans ta maison IV transforme ton espace domestique en lieu de quête spirituelle. Tu peux aspirer à vivre dans un ashram, à voyager ou à faire de ton foyer un espace d'enseignement. Les racines familiales peuvent révéler des traditions spirituelles.

## Ce que tu pourrais vivre
- Un foyer ouvert à la spiritualité et à l'exploration
- Des origines familiales liées à des traditions de foi
- L'idéalisation de la vie nomade ou spirituelle
- Le besoin de sens dans la vie domestique

## Conseils pour ce transit
- Crée un espace qui nourrit ta quête spirituelle
- Explore les traditions spirituelles de ta famille
- Trouve ta maison intérieure dans la foi""",

    ('sagittarius', 5): """# ♆ Transit de Neptune en Sagittaire — Maison V

**En une phrase :** Ta créativité s'inspire de quêtes spirituelles et tes amours deviennent des aventures de foi.

## L'énergie du moment
Neptune en Sagittaire dans ta maison de la créativité apporte une inspiration liée à la quête de sens. Tu crées des œuvres qui explorent la philosophie, la spiritualité, les voyages de l'âme. En amour, tu cherches un compagnon d'aventure spirituelle.

## Ce que tu pourrais vivre
- Une créativité inspirée par la spiritualité
- Des amours avec des chercheurs et des voyageurs
- L'idéalisation de l'aventure romantique
- Des plaisirs liés à l'exploration et à la découverte

## Conseils pour ce transit
- Exprime ta quête spirituelle à travers l'art
- Cherche des partenaires qui partagent ta soif d'exploration
- Trouve la joie dans la découverte""",

    ('sagittarius', 6): """# ♆ Transit de Neptune en Sagittaire — Maison VI

**En une phrase :** Ton quotidien devient une pratique spirituelle et ta santé bénéficie de la foi.

## L'énergie du moment
Neptune en Sagittaire dans ta maison du travail quotidien transforme tes routines en pèlerinage. Tu peux être attiré par des métiers liés à l'enseignement, aux voyages ou à la spiritualité. Ta santé bénéficie d'une attitude positive et d'approches holistiques.

## Ce que tu pourrais vivre
- Un travail qui intègre voyage et spiritualité
- Une santé soutenue par une attitude optimiste
- Le besoin de sens dans les tâches quotidiennes
- Des routines qui incluent des pratiques spirituelles

## Conseils pour ce transit
- Fais de ton quotidien un pèlerinage
- Cultive l'optimisme pour ta santé
- Trouve du sens même dans les petites tâches""",

    ('sagittarius', 7): """# ♆ Transit de Neptune en Sagittaire — Maison VII

**En une phrase :** Tes relations deviennent des quêtes partagées de sens et de vérité.

## L'énergie du moment
Neptune en Sagittaire traverse ta maison des partenariats avec une énergie d'aventure spirituelle. Tu attires des partenaires philosophes, voyageurs ou enseignants spirituels. Les relations sont des voyages de découverte mutuelle. L'idéalisation est forte.

## Ce que tu pourrais vivre
- Des relations avec des chercheurs et des philosophes
- Des partenariats d'exploration et de croissance
- L'idéalisation du partenaire parfait
- Des unions basées sur des visions partagées

## Conseils pour ce transit
- Explorez ensemble les grandes questions
- Gardez les pieds sur terre malgré les visions
- Grandissez spirituellement en couple""",

    ('sagittarius', 8): """# ♆ Transit de Neptune en Sagittaire — Maison VIII

**En une phrase :** Des transformations profondes élargissent ta compréhension des mystères de l'existence.

## L'énergie du moment
Neptune en Sagittaire dans ta maison des transformations apporte une compréhension élargie des cycles de vie et de mort. Ta philosophie intègre les mystères profonds. Les ressources partagées peuvent être liées à des questions spirituelles ou internationales.

## Ce que tu pourrais vivre
- Une compréhension philosophique de la transformation
- Des expériences qui élargissent ta vision des mystères
- Des ressources partagées avec une dimension internationale
- La foi face aux transformations profondes

## Conseils pour ce transit
- Intègre les transformations dans ta philosophie
- Explore les mystères avec foi et discernement
- Gère les ressources partagées avec sagesse""",

    ('sagittarius', 9): """# ♆ Transit de Neptune en Sagittaire — Maison IX

**En une phrase :** Ta quête spirituelle atteint des sommets d'inspiration et de vision.

## L'énergie du moment
Neptune traverse sa maison de prédilection avec l'énergie expansive du Sagittaire. C'est une période exceptionnelle pour l'exploration spirituelle, les voyages de l'âme, la découverte de sens. Ta vision du monde peut être profondément transformée par des révélations et des expériences d'expansion.

## Ce que tu pourrais vivre
- Des expériences spirituelles majeures et expansives
- Des voyages qui changent ta vie et ta vision
- Le développement d'une philosophie personnelle profonde
- L'attrait pour l'enseignement et le partage de sagesse

## Conseils pour ce transit
- Ouvre-toi aux expériences qui élargissent ta conscience
- Voyage pour ton âme autant que pour ton corps
- Partage ce que tu découvres avec générosité""",

    ('sagittarius', 10): """# ♆ Transit de Neptune en Sagittaire — Maison X

**En une phrase :** Ta carrière s'oriente vers l'enseignement, la spiritualité ou les horizons lointains.

## L'énergie du moment
Neptune en Sagittaire dans ta maison de la carrière inspire une vocation de guide spirituel ou de passeur de sagesse. Tu peux devenir enseignant, éditeur, guide de voyage ou conférencier inspirant. Ta réputation se construit sur ta capacité à élever et à inspirer.

## Ce que tu pourrais vivre
- Une carrière dans l'enseignement ou la spiritualité
- Une réputation de personne sage et inspirante
- Des opportunités internationales ou multiculturelle
- Le besoin d'une carrière qui a du sens profond

## Conseils pour ce transit
- Poursuis une carrière qui élève et inspire
- Partage ta sagesse à travers ton métier
- Construis ta réputation sur l'authenticité de ta quête""",

    ('sagittarius', 11): """# ♆ Transit de Neptune en Sagittaire — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des sanghas de chercheurs et tes aspirations embrassent l'humanité.

## L'énergie du moment
Neptune en Sagittaire traverse ta maison des amitiés avec une énergie de fraternité universelle. Tu es attiré par des groupes de chercheurs spirituels, de voyageurs, de philosophes. Tes aspirations concernent l'élévation de la conscience humaine.

## Ce que tu pourrais vivre
- Des amitiés avec des chercheurs et des sages
- L'appartenance à des communautés spirituelles
- Des aspirations pour l'évolution de l'humanité
- Des idéaux élevés parfois trop abstraits

## Conseils pour ce transit
- Rejoins des communautés de chercheurs authentiques
- Contribue à l'élévation collective
- Garde tes idéaux ancrés dans le réel""",

    ('sagittarius', 12): """# ♆ Transit de Neptune en Sagittaire — Maison XII

**En une phrase :** Une expansion spirituelle profonde dissout les limitations de la conscience ordinaire.

## L'énergie du moment
Neptune en Sagittaire dans ta maison des profondeurs ouvre les portes de la conscience élargie. Tu peux vivre des expériences mystiques d'union avec le tout, de compréhension cosmique. Des croyances inconscientes limitantes peuvent être transcendées.

## Ce que tu pourrais vivre
- Des expériences d'expansion de conscience
- La dissolution de croyances limitantes inconscientes
- Des rêves prophétiques ou visionnaires
- L'accès à une sagesse universelle

## Conseils pour ce transit
- Ouvre-toi à l'expansion avec discernement
- Libère les croyances qui limitent
- Intègre les visions dans ta vie quotidienne""",

    # ============================================================
    # NEPTUNE EN CAPRICORNE (♆ en ♑)
    # ============================================================
    ('capricorn', 1): """# ♆ Transit de Neptune en Capricorne — Maison I

**En une phrase :** Ton identité intègre une dimension spirituelle de responsabilité et de service mature.

## L'énergie du moment
Neptune en Capricorne dans ta maison I apporte une dimension de sagesse mature à ta présence. Tu incarnes une autorité spirituelle, une responsabilité qui vient de la connexion au divin. Ton identité peut sembler sérieuse mais cache une profonde compassion.

## Ce que tu pourrais vivre
- Une présence d'autorité spirituelle mature
- L'incarnation de la responsabilité avec compassion
- Une confusion possible sur ton rôle et ton statut
- Le développement d'une sagesse par l'expérience

## Conseils pour ce transit
- Assume ton autorité spirituelle avec humilité
- Intègre la compassion dans ta responsabilité
- Accepte que ta position soit mal comprise parfois""",

    ('capricorn', 2): """# ♆ Transit de Neptune en Capricorne — Maison II

**En une phrase :** Tes valeurs allient ambition et spiritualité, cherchant un succès qui a du sens.

## L'énergie du moment
Neptune en Capricorne dans ta maison des ressources lie tes finances à un succès qui a du sens spirituel. Tu peux réussir dans des domaines qui allient structure et inspiration. La confusion peut venir de la tension entre réussite matérielle et idéaux spirituels.

## Ce que tu pourrais vivre
- Des revenus liés à des positions d'autorité ou de structure
- La recherche d'un succès qui a du sens spirituel
- Une tension entre ambition et valeurs spirituelles
- La construction patiente de ressources durables

## Conseils pour ce transit
- Construis un succès qui sert un but plus élevé
- Intègre tes valeurs spirituelles dans tes ambitions
- Sois patient dans la construction de tes ressources""",

    ('capricorn', 3): """# ♆ Transit de Neptune en Capricorne — Maison III

**En une phrase :** Ta communication gagne en autorité et transmet une sagesse structurée.

## L'énergie du moment
Neptune en Capricorne dans ta maison de la communication apporte une qualité d'autorité et de structure à tes échanges. Tu peux communiquer des visions avec une crédibilité qui vient de l'expérience. Tes idées ont un poids et une maturité.

## Ce que tu pourrais vivre
- Une communication qui porte l'autorité de l'expérience
- Des idées qui allient vision et structure
- La transmission de sagesse de façon organisée
- Une pensée qui intègre idéal et réalité

## Conseils pour ce transit
- Transmets ta sagesse avec structure et clarté
- Utilise ton autorité communicative avec responsabilité
- Construis tes idées sur des fondations solides""",

    ('capricorn', 4): """# ♆ Transit de Neptune en Capricorne — Maison IV

**En une phrase :** Ton foyer devient un lieu de tradition spiritualisée et de structure bienveillante.

## L'énergie du moment
Neptune en Capricorne dans ta maison IV transforme les traditions familiales en pratiques spirituelles. Tu aspires à un foyer qui allie structure et compassion, autorité et amour. Les questions d'héritage familial peuvent prendre une dimension spirituelle.

## Ce que tu pourrais vivre
- Des traditions familiales spiritualisées
- Un foyer structuré mais compatissant
- La guérison des patterns d'autorité familiale
- La construction de fondations spirituelles solides

## Conseils pour ce transit
- Spiritualise les traditions plutôt que les rejeter
- Crée une structure familiale bienveillante
- Construis des fondations qui durent""",

    ('capricorn', 5): """# ♆ Transit de Neptune en Capricorne — Maison V

**En une phrase :** Ta créativité s'exprime avec maîtrise et tes amours cherchent la durabilité.

## L'énergie du moment
Neptune en Capricorne dans ta maison de la créativité apporte une expression artistique maîtrisée et mature. Tu es attiré par des formes d'art classiques ou qui demandent une longue maîtrise. En amour, tu cherches des relations sérieuses et durables avec une dimension spirituelle.

## Ce que tu pourrais vivre
- Une créativité qui demande maîtrise et patience
- Des amours sérieuses et spirituellement significatives
- Le plaisir de la construction et de l'accomplissement
- Des loisirs qui développent des compétences

## Conseils pour ce transit
- Développe une maîtrise artistique avec patience
- Cherche des relations qui construisent quelque chose
- Trouve la joie dans l'accomplissement progressif""",

    ('capricorn', 6): """# ♆ Transit de Neptune en Capricorne — Maison VI

**En une phrase :** Ton quotidien devient une discipline spirituelle et ta santé bénéficie de la structure.

## L'énergie du moment
Neptune en Capricorne dans ta maison du travail quotidien transforme tes routines en pratiques disciplinées avec une dimension spirituelle. Ton travail peut être sérieux et responsable, servant un but plus élevé. Ta santé bénéficie de routines bien structurées.

## Ce que tu pourrais vivre
- Un travail qui allie responsabilité et service spirituel
- Des routines de santé disciplinées et efficaces
- Le besoin de structure dans la vie quotidienne
- Une pratique spirituelle intégrée dans le travail

## Conseils pour ce transit
- Fais de la discipline une pratique spirituelle
- Structure ton quotidien pour le bien-être
- Sers à travers ton travail responsable""",

    ('capricorn', 7): """# ♆ Transit de Neptune en Capricorne — Maison VII

**En une phrase :** Tes relations deviennent des engagements sérieux avec une dimension spirituelle.

## L'énergie du moment
Neptune en Capricorne traverse ta maison des partenariats avec une énergie d'engagement mature. Tu attires des partenaires responsables et établis qui partagent une vision à long terme. Les relations sont des structures qui soutiennent la croissance spirituelle.

## Ce que tu pourrais vivre
- Des relations sérieuses et engagées
- Des partenaires matures et responsables
- Des unions qui construisent quelque chose de durable
- La recherche de partenariats significatifs

## Conseils pour ce transit
- Engage-toi dans des relations qui construisent
- Choisis des partenaires avec qui grandir sur le long terme
- Fais de ton couple une structure de soutien mutuel""",

    ('capricorn', 8): """# ♆ Transit de Neptune en Capricorne — Maison VIII

**En une phrase :** Des transformations profondes restructurent ta relation au pouvoir et aux ressources partagées.

## L'énergie du moment
Neptune en Capricorne dans ta maison des transformations apporte une restructuration spirituelle de ta relation au pouvoir. Les questions d'héritage, de contrôle et de ressources partagées sont transformées. Tu développes une vision mature de la transformation.

## Ce que tu pourrais vivre
- La transformation de ta relation au pouvoir
- Des restructurations des ressources partagées
- Une compréhension mature des cycles de transformation
- La dissolution de structures de contrôle obsolètes

## Conseils pour ce transit
- Restructure tes arrangements partagés avec sagesse
- Développe une relation mature au pouvoir
- Accepte les transformations comme des constructions""",

    ('capricorn', 9): """# ♆ Transit de Neptune en Capricorne — Maison IX

**En une phrase :** Ta quête spirituelle devient une construction disciplinée de sagesse.

## L'énergie du moment
Neptune en Capricorne traverse ta maison des horizons lointains avec une énergie de construction spirituelle. Tu es attiré par des traditions qui ont fait leurs preuves, des enseignements qui se construisent avec le temps. Ta philosophie intègre patience et persévérance.

## Ce que tu pourrais vivre
- Une spiritualité qui se construit avec discipline
- L'attrait pour des traditions établies
- Des études ou formations spirituelles structurées
- Une philosophie qui intègre le temps et la maturité

## Conseils pour ce transit
- Construis ta sagesse avec patience
- Étudie des traditions qui ont fait leurs preuves
- Intègre la discipline dans ta pratique spirituelle""",

    ('capricorn', 10): """# ♆ Transit de Neptune en Capricorne — Maison X

**En une phrase :** Ta carrière atteint une dimension d'autorité spirituelle et de service responsable.

## L'énergie du moment
Neptune en Capricorne dans ta maison de la carrière crée une tension créative entre ambition et spiritualité. Tu peux atteindre des positions d'autorité qui servent un but plus élevé. Ta réputation se construit sur ta capacité à incarner la responsabilité avec compassion.

## Ce que tu pourrais vivre
- Une carrière qui allie autorité et service spirituel
- Une réputation d'intégrité et de responsabilité
- Des positions de leadership avec une dimension spirituelle
- La confusion entre ambition personnelle et service

## Conseils pour ce transit
- Utilise ton autorité pour servir le bien commun
- Construis une carrière qui a du sens spirituel
- Incarne la responsabilité avec compassion""",

    ('capricorn', 11): """# ♆ Transit de Neptune en Capricorne — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des structures de soutien spirituel et tes aspirations se concrétisent.

## L'énergie du moment
Neptune en Capricorne traverse ta maison des amitiés avec une énergie de construction collective. Tu es attiré par des groupes qui travaillent de façon structurée vers des objectifs spirituels. Tes aspirations deviennent plus réalistes et réalisables.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes responsables et spirituelles
- L'appartenance à des organisations structurées
- Des aspirations qui se concrétisent avec le temps
- La contribution à des projets collectifs durables

## Conseils pour ce transit
- Rejoins des groupes qui construisent quelque chose
- Travaille patiemment vers tes aspirations
- Contribue de façon responsable au collectif""",

    ('capricorn', 12): """# ♆ Transit de Neptune en Capricorne — Maison XII

**En une phrase :** Une dissolution des structures rigides inconscientes libère une autorité spirituelle authentique.

## L'énergie du moment
Neptune en Capricorne dans ta maison des profondeurs travaille sur tes patterns inconscients d'autorité et de contrôle. Des structures rigides que tu t'imposes peuvent être dissoutes. Tu découvres une autorité qui vient de l'intérieur plutôt que de l'extérieur.

## Ce que tu pourrais vivre
- La dissolution de patterns de contrôle inconscients
- La libération de rigidités intérieures
- Des rêves impliquant l'autorité et la structure
- La découverte d'une autorité spirituelle authentique

## Conseils pour ce transit
- Laisse les structures rigides se dissoudre
- Développe une autorité intérieure flexible
- Libère le besoin de tout contrôler""",

    # ============================================================
    # NEPTUNE EN VERSEAU (♆ en ♒)
    # ============================================================
    ('aquarius', 1): """# ♆ Transit de Neptune en Verseau — Maison I

**En une phrase :** Ton identité devient un canal pour des visions futuristes et humanitaires.

## L'énergie du moment
Neptune en Verseau dans ta maison I apporte une dimension visionnaire et humanitaire à ta présence. Tu incarnes le futur, les possibilités nouvelles, la conscience collective. Ta présence peut inspirer le changement et l'innovation. Tu peux te sentir en avance sur ton temps.

## Ce que tu pourrais vivre
- Une identité visionnaire et avant-gardiste
- L'incarnation d'idéaux humanitaires
- Une possible confusion sur ta place dans le monde actuel
- La présence comme catalyseur de changement

## Conseils pour ce transit
- Incarne le futur que tu veux voir
- Utilise ta vision pour inspirer le changement
- Reste connecté au présent malgré tes visions""",

    ('aquarius', 2): """# ♆ Transit de Neptune en Verseau — Maison II

**En une phrase :** Tes valeurs s'orientent vers l'innovation et le bien collectif plutôt que personnel.

## L'énergie du moment
Neptune en Verseau dans ta maison des ressources lie tes finances à l'innovation et aux causes humanitaires. Tu peux gagner ta vie par la technologie, l'innovation sociale ou le travail collectif. Les possessions personnelles ont moins d'importance que la contribution au monde.

## Ce que tu pourrais vivre
- Des revenus liés à l'innovation ou aux causes sociales
- Une valorisation du bien collectif
- Une relation plus détachée aux possessions personnelles
- Des finances qui passent par les réseaux et le collectif

## Conseils pour ce transit
- Explore des modèles économiques innovants
- Valorise ta contribution au collectif
- Utilise tes ressources pour le bien commun""",

    ('aquarius', 3): """# ♆ Transit de Neptune en Verseau — Maison III

**En une phrase :** Ta communication devient un vecteur de visions futuristes et d'idéaux humanitaires.

## L'énergie du moment
Neptune en Verseau dans ta maison de la communication apporte des idées visionnaires et avant-gardistes. Tu communiques sur le futur, les possibilités, les changements nécessaires. Tes mots peuvent inspirer des mouvements et des changements collectifs.

## Ce que tu pourrais vivre
- Une communication visionnaire et innovante
- Des idées qui concernent le collectif et l'avenir
- Des échanges à travers les réseaux et la technologie
- Une pensée qui connecte des personnes éloignées

## Conseils pour ce transit
- Partage tes visions pour inspirer le changement
- Utilise les technologies de communication avec sagesse
- Connecte les gens autour d'idées communes""",

    ('aquarius', 4): """# ♆ Transit de Neptune en Verseau — Maison IV

**En une phrase :** Ton foyer devient un espace de communauté et d'innovation sociale.

## L'énergie du moment
Neptune en Verseau dans ta maison IV transforme ton espace domestique en hub de connexion et d'innovation. Tu peux vivre en communauté, avoir un foyer high-tech, ou faire de ta maison un lieu de réunion pour des causes. Ta famille devient ta tribu choisie.

## Ce que tu pourrais vivre
- Un foyer connecté et communautaire
- Des formes de vie collective ou alternatives
- Une famille élargie aux amis et aux causes
- La sécurité trouvée dans le collectif

## Conseils pour ce transit
- Crée un espace qui connecte les gens
- Explore des formes de vie innovantes
- Trouve ta famille dans ta communauté d'âme""",

    ('aquarius', 5): """# ♆ Transit de Neptune en Verseau — Maison V

**En une phrase :** Ta créativité s'exprime à travers les nouvelles technologies et tes amours transcendent les conventions.

## L'énergie du moment
Neptune en Verseau dans ta maison de la créativité apporte une expression artistique innovante et technologique. Tu es attiré par les arts numériques, les créations collaboratives, les formes nouvelles. En amour, tu cherches des relations qui défient les conventions.

## Ce que tu pourrais vivre
- Une créativité qui utilise les nouvelles technologies
- Des amours non conventionnelles et libres
- Le plaisir de l'innovation et de l'expérimentation
- Des créations qui sont des collaborations

## Conseils pour ce transit
- Explore les nouvelles formes d'expression créative
- Aime de façon authentique, pas conventionnelle
- Crée en collaboration avec d'autres""",

    ('aquarius', 6): """# ♆ Transit de Neptune en Verseau — Maison VI

**En une phrase :** Ton quotidien intègre la technologie spirituelle et le service à la communauté.

## L'énergie du moment
Neptune en Verseau dans ta maison du travail quotidien transforme tes routines en contributions au collectif. Tu peux travailler dans des domaines innovants ou utiliser la technologie pour le bien-être. Ta santé bénéficie d'approches avant-gardistes.

## Ce que tu pourrais vivre
- Un travail lié à l'innovation ou aux causes sociales
- Des routines qui intègrent la technologie de bien-être
- Le service à travers les réseaux et les communautés
- Des approches de santé innovantes

## Conseils pour ce transit
- Utilise la technologie pour améliorer ton bien-être
- Travaille pour le bien collectif
- Intègre l'innovation dans ton quotidien""",

    ('aquarius', 7): """# ♆ Transit de Neptune en Verseau — Maison VII

**En une phrase :** Tes relations deviennent des partenariats pour le changement et la liberté.

## L'énergie du moment
Neptune en Verseau traverse ta maison des partenariats avec une énergie de liberté et d'idéal collectif. Tu attires des partenaires visionnaires et engagés dans des causes. Les relations sont des alliances pour créer le changement, avec beaucoup de liberté individuelle.

## Ce que tu pourrais vivre
- Des relations avec des personnes visionnaires
- Des partenariats basés sur des idéaux partagés
- Le besoin de liberté dans l'engagement
- Des unions qui servent des causes plus grandes

## Conseils pour ce transit
- Cherche des partenaires qui partagent tes visions
- Maintiens la liberté dans l'engagement
- Faites équipe pour changer le monde""",

    ('aquarius', 8): """# ♆ Transit de Neptune en Verseau — Maison VIII

**En une phrase :** Des transformations profondes t'ouvrent à une conscience collective et transpersonnelle.

## L'énergie du moment
Neptune en Verseau dans ta maison des transformations apporte des changements liés à la conscience collective. Tu peux vivre des expériences de connexion au champ universel. Les ressources partagées peuvent être gérées de façon innovante ou collective.

## Ce que tu pourrais vivre
- Des expériences de conscience collective
- Des transformations qui concernent le groupe
- Des formes innovantes de partage des ressources
- La dissolution des frontières individuelles

## Conseils pour ce transit
- Ouvre-toi à la conscience transpersonnelle
- Explore des formes de partage innovantes
- Accepte que ta transformation serve le collectif""",

    ('aquarius', 9): """# ♆ Transit de Neptune en Verseau — Maison IX

**En une phrase :** Ta quête spirituelle embrasse une vision globale et universelle de l'humanité.

## L'énergie du moment
Neptune en Verseau traverse ta maison des horizons lointains avec une vision cosmique et humanitaire. Tu es attiré par des philosophies qui concernent l'humanité entière, peut-être même l'univers. Ta spiritualité devient une science de la conscience.

## Ce que tu pourrais vivre
- Une spiritualité universelle et non dogmatique
- L'intérêt pour les sciences de la conscience
- Des voyages vers des communautés innovantes
- Une philosophie qui embrasse toute l'humanité

## Conseils pour ce transit
- Développe une spiritualité universelle
- Explore les frontières de la conscience
- Voyage vers des lieux d'innovation spirituelle""",

    ('aquarius', 10): """# ♆ Transit de Neptune en Verseau — Maison X

**En une phrase :** Ta carrière s'oriente vers l'innovation sociale et le service à l'humanité.

## L'énergie du moment
Neptune en Verseau dans ta maison de la carrière inspire une vocation humanitaire ou innovante. Tu peux devenir reconnu pour ta contribution au changement social, à l'innovation ou aux causes humanitaires. Ta réputation se construit autour de ta vision du futur.

## Ce que tu pourrais vivre
- Une carrière dans l'innovation sociale ou la technologie
- Une réputation de visionnaire et d'humaniste
- Des positions qui servent le changement collectif
- Le besoin d'une carrière qui fait une différence

## Conseils pour ce transit
- Poursuis une carrière qui contribue au futur
- Utilise ton influence pour le bien collectif
- Incarne le changement que tu veux voir""",

    ('aquarius', 11): """# ♆ Transit de Neptune en Verseau — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des réseaux de visionnaires et tes aspirations concernent l'humanité entière.

## L'énergie du moment
Neptune traverse sa maison naturelle avec l'énergie du Verseau, maximisant l'idéalisme collectif. Tu es au cœur de réseaux de changement, de communautés de visionnaires. Tes aspirations concernent l'évolution de toute l'humanité.

## Ce que tu pourrais vivre
- Des réseaux de personnes engagées et visionnaires
- Des aspirations d'évolution collective
- L'appartenance à des mouvements de changement
- La dissolution des frontières entre soi et le groupe

## Conseils pour ce transit
- Rejoins des réseaux qui créent le changement
- Contribue à l'évolution collective
- Garde ton individualité dans le collectif""",

    ('aquarius', 12): """# ♆ Transit de Neptune en Verseau — Maison XII

**En une phrase :** Une dissolution des séparations inconscientes te connecte à la conscience universelle.

## L'énergie du moment
Neptune en Verseau dans ta maison des profondeurs travaille sur les frontières inconscientes entre toi et le collectif. Tu peux vivre des expériences de connexion à la conscience de l'humanité. Les patterns de séparation et d'aliénation peuvent être dissous.

## Ce que tu pourrais vivre
- Des expériences de conscience universelle
- La dissolution des sentiments d'aliénation
- Des rêves concernant le futur de l'humanité
- L'accès à l'inconscient collectif

## Conseils pour ce transit
- Ouvre-toi à la conscience universelle
- Libère les patterns d'isolement
- Contribue au rêve collectif de l'humanité""",

    # ============================================================
    # NEPTUNE EN POISSONS (♆ en ♓)
    # ============================================================
    ('pisces', 1): """# ♆ Transit de Neptune en Poissons — Maison I

**En une phrase :** Ton identité devient un canal pur pour le divin et tu incarnes la compassion universelle.

## L'énergie du moment
Neptune en Poissons dans ta maison I est dans sa position la plus puissante, maximisant ta connexion au spirituel. Ton identité devient fluide, presque transparente au divin. Tu incarnes la compassion, l'art, la spiritualité dans leur forme la plus pure. Les frontières de ton ego se dissolvent.

## Ce que tu pourrais vivre
- Une présence presque éthérée et spirituelle
- L'incarnation de la compassion universelle
- La dissolution de l'ego et de ses limites
- Des capacités artistiques ou spirituelles exceptionnelles

## Conseils pour ce transit
- Deviens un canal pur pour le divin
- Protège ta sensibilité sans te fermer
- Reste ancré malgré la dissolution""",

    ('pisces', 2): """# ♆ Transit de Neptune en Poissons — Maison II

**En une phrase :** Tes valeurs transcendent complètement le matériel pour embrasser le spirituel.

## L'énergie du moment
Neptune en Poissons dans ta maison des ressources dissout profondément les attachements matériels. Tu découvres que la vraie richesse est totalement spirituelle. Les finances peuvent être floues mais soutenues par la grâce. Tu apprends à faire confiance à l'univers.

## Ce que tu pourrais vivre
- Un détachement profond des possessions
- Des finances soutenues par la grâce
- La découverte de richesses spirituelles infinies
- La générosité sans calcul

## Conseils pour ce transit
- Fais confiance à l'univers pour tes besoins
- Garde un minimum de structure financière
- Découvre la richesse de l'âme""",

    ('pisces', 3): """# ♆ Transit de Neptune en Poissons — Maison III

**En une phrase :** Ta communication devient poésie pure et tes mots sont des prières.

## L'énergie du moment
Neptune en Poissons dans ta maison de la communication apporte une qualité mystique et poétique maximale à tes échanges. Tu communiques comme un médium, un poète, un mystique. Les mots ordinaires ne suffisent plus pour exprimer ce que tu perçois.

## Ce que tu pourrais vivre
- Une communication presque médiumnique
- Des capacités d'expression artistique exceptionnelles
- Une connexion intuitive profonde avec les proches
- Le risque de confusion dans les communications pratiques

## Conseils pour ce transit
- Exprime-toi à travers l'art et la poésie
- Clarifie les communications pratiques
- Utilise tes dons de communication pour guérir""",

    ('pisces', 4): """# ♆ Transit de Neptune en Poissons — Maison IV

**En une phrase :** Ton foyer devient un ashram et ta vraie maison est le divin.

## L'énergie du moment
Neptune en Poissons dans ta maison IV transforme complètement ta relation au foyer et aux racines. Ton espace domestique devient un sanctuaire de méditation et de spiritualité. Tu découvres que ta vraie maison est l'univers, le divin, la conscience infinie.

## Ce que tu pourrais vivre
- Un foyer transformé en espace de pure spiritualité
- La dissolution des attachements aux racines terrestres
- La découverte de ta maison dans le divin
- Une connexion profonde avec tous les ancêtres

## Conseils pour ce transit
- Fais de ton foyer un espace sacré
- Trouve ta sécurité dans le divin
- Garde un ancrage malgré la dissolution""",

    ('pisces', 5): """# ♆ Transit de Neptune en Poissons — Maison V

**En une phrase :** Ta créativité devient un canal pour le divin et tes amours touchent le sacré.

## L'énergie du moment
Neptune en Poissons dans ta maison de la créativité apporte une inspiration artistique et spirituelle maximale. Tu es capable de créations qui sont des transmissions du divin. En amour, tu cherches l'union mystique, la fusion avec le tout à travers l'autre.

## Ce que tu pourrais vivre
- Une créativité comme canal du divin
- Des amours qui touchent des dimensions mystiques
- Le plaisir de la béatitude spirituelle
- Des expériences de joie et d'extase spirituelles

## Conseils pour ce transit
- Laisse le divin créer à travers toi
- Recherche l'amour sacré tout en restant humain
- Trouve la joie dans la connexion au tout""",

    ('pisces', 6): """# ♆ Transit de Neptune en Poissons — Maison VI

**En une phrase :** Ton quotidien devient une offrande et ta santé est un yoga.

## L'énergie du moment
Neptune en Poissons dans ta maison du travail quotidien transforme chaque tâche en pratique spirituelle. Ton travail devient service désintéressé, offrande au divin. Ta santé est maintenue par la grâce et les pratiques spirituelles. L'ego disparaît dans le service.

## Ce que tu pourrais vivre
- Un travail comme service désintéressé
- Une santé soutenue par la pratique spirituelle
- La dissolution de l'ego à travers le service
- Des routines qui sont des méditations

## Conseils pour ce transit
- Fais de chaque tâche une offrande
- Soutiens ta santé par des pratiques spirituelles
- Sers sans attente de reconnaissance""",

    ('pisces', 7): """# ♆ Transit de Neptune en Poissons — Maison VII

**En une phrase :** Tes relations deviennent des unions mystiques et l'autre est le miroir du divin.

## L'énergie du moment
Neptune en Poissons traverse ta maison des partenariats avec une énergie d'union mystique maximale. Tu cherches dans l'autre le reflet du divin. Les relations peuvent atteindre des sommets spirituels ou des abîmes de confusion. L'amour idéal peut se manifester ou l'illusion peut dominer.

## Ce que tu pourrais vivre
- Des relations comme unions mystiques
- Des partenaires hautement spirituels ou artistiques
- Le risque de grandes illusions en amour
- La dissolution des frontières entre toi et l'autre

## Conseils pour ce transit
- Recherche le divin à travers l'amour humain
- Garde ton discernement malgré la fusion
- Maintiens ton identité dans l'union""",

    ('pisces', 8): """# ♆ Transit de Neptune en Poissons — Maison VIII

**En une phrase :** Des transformations mystiques profondes dissolvent toutes les peurs et révèlent l'éternité.

## L'énergie du moment
Neptune en Poissons dans ta maison des transformations crée une puissance spirituelle extraordinaire. Tu peux transcender toutes les peurs, y compris celle de la mort. Les expériences mystiques de dissolution de l'ego et de retour à la source sont possibles.

## Ce que tu pourrais vivre
- Des expériences mystiques de transcendance
- La dissolution de toutes les peurs profondes
- La compréhension directe de l'éternité
- Des transformations spirituelles majeures

## Conseils pour ce transit
- Ouvre-toi aux expériences transcendantes
- Libère toutes les peurs dans la confiance divine
- Intègre les révélations dans ta vie humaine""",

    ('pisces', 9): """# ♆ Transit de Neptune en Poissons — Maison IX

**En une phrase :** Ta quête spirituelle atteint l'illumination et ta vision embrasse l'infini.

## L'énergie du moment
Neptune en Poissons traverse ta maison des horizons lointains avec une énergie de réalisation spirituelle. Tu peux accéder à des états de conscience élevés, à des visions de l'infini. Toutes les frontières philosophiques se dissolvent dans l'unité. La vérité ultime est accessible.

## Ce que tu pourrais vivre
- Des expériences d'illumination et de réalisation
- L'accès à la vérité ultime au-delà des mots
- Des voyages intérieurs vers l'infini
- La dissolution de toutes les croyances dans l'unité

## Conseils pour ce transit
- Ouvre-toi aux révélations ultimes
- Intègre les visions dans ta vie quotidienne
- Partage ce que tu reçois avec humilité""",

    ('pisces', 10): """# ♆ Transit de Neptune en Poissons — Maison X

**En une phrase :** Ta carrière devient une mission spirituelle et ta réputation celle d'un être de lumière.

## L'énergie du moment
Neptune en Poissons dans ta maison de la carrière transforme ta vocation en mission spirituelle. Tu peux devenir reconnu comme artiste, guérisseur, guide spirituel. Ta réputation se construit sur ta capacité à toucher les âmes et à canaliser le divin.

## Ce que tu pourrais vivre
- Une carrière comme mission spirituelle
- Une réputation de personne inspirée et compassionnée
- La dissolution des ambitions personnelles au profit du service
- Une vocation qui est un don au monde

## Conseils pour ce transit
- Laisse ta carrière devenir un service
- Accepte la reconnaissance sans t'y attacher
- Offre ton travail comme un cadeau au monde""",

    ('pisces', 11): """# ♆ Transit de Neptune en Poissons — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des sanghas de lumière et tes aspirations touchent le divin.

## L'énergie du moment
Neptune en Poissons traverse ta maison des amitiés avec une énergie de fraternité spirituelle ultime. Tu es attiré par des communautés de pratique spirituelle, des groupes qui vibrent à des fréquences élevées. Tes aspirations concernent l'éveil de l'humanité entière.

## Ce que tu pourrais vivre
- Des amitiés comme des liens d'âme
- L'appartenance à des communautés spirituelles pures
- Des aspirations d'éveil collectif
- La dissolution des frontières entre amis

## Conseils pour ce transit
- Rejoins des communautés de pratique authentique
- Contribue à l'éveil par ta présence
- Maintiens ton discernement dans les groupes""",

    ('pisces', 12): """# ♆ Transit de Neptune en Poissons — Maison XII

**En une phrase :** La dissolution ultime de toutes les illusions révèle l'unité avec le tout.

## L'énergie du moment
Neptune en Poissons dans sa maison domicile crée la configuration la plus puissante pour l'éveil spirituel. Toutes les illusions peuvent se dissoudre. Tu peux accéder à des états d'union complète avec le divin, de dissolution de l'ego dans l'océan cosmique. C'est une période de potentiel spirituel maximal.

## Ce que tu pourrais vivre
- Des états d'union mystique avec le tout
- La dissolution complète de l'ego
- L'accès à la conscience cosmique
- La libération de tous les karmas et illusions

## Conseils pour ce transit
- Ouvre-toi complètement au divin
- Garde un ancrage pour fonctionner dans le monde
- Partage la grâce que tu reçois avec tous""",
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
        print(f"✅ Transit Neptune (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
