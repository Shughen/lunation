#!/usr/bin/env python3
"""Insert transit_uranus interpretations for Sagittarius, Capricorn, Aquarius, Pisces (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_URANUS_INTERPRETATIONS = {
    # ============================================================
    # URANUS EN SAGITTAIRE (♅ en ♐)
    # ============================================================
    ('sagittarius', 1): """# ♅ Transit d'Uranus en Sagittaire — Maison I

**En une phrase :** Ton identité s'ouvre à de nouvelles philosophies et tu deviens un pionnier de la pensée.

## L'énergie du moment
Uranus en Sagittaire dans ta maison I déclenche une révolution de ta vision du monde et de ton identité. Tu ressens le besoin d'élargir tes horizons, de remettre en question tes croyances et de te présenter au monde comme un aventurier de la pensée. Ton apparence peut refléter des influences culturelles diverses et originales.

## Ce que tu pourrais vivre
- Une transformation de tes croyances et valeurs fondamentales
- Le besoin de liberté philosophique et spirituelle
- Une apparence qui reflète ton ouverture au monde
- L'attrait pour des modes de vie non conventionnels

## Conseils pour ce transit
- Explore de nouvelles philosophies sans perdre ton ancrage
- Laisse ton identité s'enrichir de nouvelles perspectives
- Deviens un ambassadeur de tes propres découvertes""",

    ('sagittarius', 2): """# ♅ Transit d'Uranus en Sagittaire — Maison II

**En une phrase :** Tes revenus peuvent venir d'horizons lointains et tes valeurs s'élargissent.

## L'énergie du moment
Uranus en Sagittaire secoue ta maison des ressources avec une énergie d'expansion et d'aventure. Tes revenus peuvent provenir de sources internationales, de l'enseignement, de l'édition ou du voyage. Tu valorises la liberté, la sagesse et l'aventure plus que la sécurité matérielle conventionnelle.

## Ce que tu pourrais vivre
- Des revenus liés aux voyages, à l'enseignement ou à l'international
- Une relation plus philosophique à l'argent
- L'importance de la liberté comme valeur suprême
- Des opportunités financières venues de loin

## Conseils pour ce transit
- Explore des sources de revenus internationales
- Investis dans l'éducation et les voyages
- Développe une philosophie saine de l'abondance""",

    ('sagittarius', 3): """# ♅ Transit d'Uranus en Sagittaire — Maison III

**En une phrase :** Ta pensée s'élargit à des perspectives mondiales et ta communication devient inspirante.

## L'énergie du moment
Uranus en Sagittaire électrifie ta maison de la communication avec une énergie d'expansion mentale. Tes idées s'ouvrent à des philosophies diverses, ton langage intègre des concepts de différentes cultures. Tu communiques de façon inspirante et enthousiaste. Tes proches peuvent venir de milieux culturels variés.

## Ce que tu pourrais vivre
- Une pensée qui intègre des perspectives mondiales
- L'apprentissage de langues étrangères ou de philosophies
- Une communication qui inspire et élève
- Des relations avec des personnes de cultures différentes

## Conseils pour ce transit
- Élargis tes perspectives mentales sans te disperser
- Apprends de cultures et philosophies diverses
- Communique tes découvertes avec enthousiasme""",

    ('sagittarius', 4): """# ♅ Transit d'Uranus en Sagittaire — Maison IV

**En une phrase :** Ton foyer s'ouvre au monde et tes racines deviennent cosmopolites.

## L'énergie du moment
Uranus en Sagittaire dans ta maison IV transforme ta conception du foyer et des racines. Tu pourrais déménager à l'étranger ou faire de ton foyer un lieu d'ouverture au monde. Tes racines familiales révèlent des connexions internationales ou philosophiques. La notion de "chez soi" devient plus large.

## Ce que tu pourrais vivre
- Un déménagement vers l'étranger ou un lieu différent
- Un foyer qui accueille des personnes de partout
- Des découvertes sur les origines internationales de ta famille
- Une sécurité basée sur une vision du monde élargie

## Conseils pour ce transit
- Ouvre ton foyer à différentes cultures
- Explore les connexions internationales de ta famille
- Trouve ta maison intérieure au-delà des frontières""",

    ('sagittarius', 5): """# ♅ Transit d'Uranus en Sagittaire — Maison V

**En une phrase :** Ta créativité s'inspire de cultures diverses et tes amours sont des aventures.

## L'énergie du moment
Uranus en Sagittaire enflamme ta maison de la créativité avec une énergie d'exploration. Tu es attiré par des formes d'art qui mélangent les cultures, qui élèvent l'esprit. En amour, tu recherches l'aventure, la découverte mutuelle, quelqu'un qui élargit tes horizons. Les plaisirs incluent l'apprentissage et le voyage.

## Ce que tu pourrais vivre
- Une créativité inspirée par différentes cultures
- Des amours avec des personnes de cultures différentes
- Le plaisir de l'aventure et de la découverte
- Des relations avec les enfants basées sur l'ouverture

## Conseils pour ce transit
- Laisse ta créativité s'inspirer du monde entier
- Cherche des partenaires qui t'inspirent et t'élèvent
- Fais de l'apprentissage un plaisir""",

    ('sagittarius', 6): """# ♅ Transit d'Uranus en Sagittaire — Maison VI

**En une phrase :** Ton quotidien intègre une dimension internationale et ta santé bénéficie de sagesses diverses.

## L'énergie du moment
Uranus en Sagittaire révolutionne ta maison du travail quotidien avec une énergie d'expansion. Tu pourrais travailler dans un contexte international ou intégrer des pratiques de différentes cultures dans ton quotidien. Ta santé bénéficie de traditions de bien-être du monde entier.

## Ce que tu pourrais vivre
- Un travail avec une dimension internationale
- L'intégration de pratiques de bien-être de différentes cultures
- Un quotidien qui inclut l'apprentissage et la découverte
- Des collègues ou collaborateurs de différents horizons

## Conseils pour ce transit
- Internationalise ton activité professionnelle
- Explore des approches de santé de différentes traditions
- Enrichis ton quotidien de perspectives diverses""",

    ('sagittarius', 7): """# ♅ Transit d'Uranus en Sagittaire — Maison VII

**En une phrase :** Tes relations s'élargissent à de nouveaux horizons et tes partenariats sont des aventures.

## L'énergie du moment
Uranus en Sagittaire traverse ta maison des partenariats avec une énergie d'exploration. Tu attires des partenaires de cultures différentes ou qui élargissent ta vision du monde. Tes relations demandent de l'espace pour la croissance et l'aventure. Les partenariats conventionnels ne te suffisent plus.

## Ce que tu pourrais vivre
- Des relations avec des personnes de cultures différentes
- Le besoin de liberté et de croissance dans les partenariats
- Des unions qui élargissent mutuellement les perspectives
- Des partenaires qui sont aussi des guides ou enseignants

## Conseils pour ce transit
- Recherche des partenaires qui t'aident à grandir
- Donne et demande de l'espace dans les relations
- Fais de chaque relation une aventure d'apprentissage""",

    ('sagittarius', 8): """# ♅ Transit d'Uranus en Sagittaire — Maison VIII

**En une phrase :** Des transformations profondes élargissent ta vision de la vie, de la mort et du partage.

## L'énergie du moment
Uranus en Sagittaire plonge dans ta maison des transformations avec une énergie de quête. Tu cherches une compréhension plus large des mystères de l'existence. Les ressources partagées peuvent avoir une dimension internationale. Ta philosophie de la transformation s'enrichit de perspectives diverses.

## Ce que tu pourrais vivre
- Des expériences transformatrices liées aux voyages ou cultures
- Une compréhension élargie des cycles de vie et de mort
- Des ressources partagées avec une dimension internationale
- L'exploration de traditions ésotériques diverses

## Conseils pour ce transit
- Élargis ta compréhension de la transformation
- Explore les sagesses sur la mort et la renaissance
- Gère les ressources partagées avec ouverture et équité""",

    ('sagittarius', 9): """# ♅ Transit d'Uranus en Sagittaire — Maison IX

**En une phrase :** Une révolution de ta vision du monde t'ouvre à des perspectives infinies.

## L'énergie du moment
Uranus traverse sa maison de prédilection avec l'énergie expansive du Sagittaire. Cette position est puissante pour des révélations philosophiques et spirituelles majeures. Tes voyages sont transformateurs, tes études révolutionnaires. Tu développes une vision du monde unique et originale.

## Ce que tu pourrais vivre
- Des révélations philosophiques ou spirituelles majeures
- Des voyages qui changent fondamentalement ta vision
- L'élaboration d'une philosophie personnelle unique
- L'enseignement ou la publication d'idées originales

## Conseils pour ce transit
- Reste ouvert aux révélations qui transforment tout
- Voyage vers des lieux qui élargissent ta conscience
- Partage ta vision avec générosité""",

    ('sagittarius', 10): """# ♅ Transit d'Uranus en Sagittaire — Maison X

**En une phrase :** Ta carrière prend une dimension internationale et tu deviens un visionnaire dans ton domaine.

## L'énergie du moment
Uranus en Sagittaire révolutionne ta maison de la carrière avec une énergie d'expansion. Tu pourrais te diriger vers des carrières internationales, l'enseignement supérieur, l'édition ou les voyages. Ta réputation se construit autour de ta vision large et de ton originalité philosophique.

## Ce que tu pourrais vivre
- Une carrière avec une portée internationale
- Des positions liées à l'enseignement, l'édition, ou la philosophie
- Une réputation de visionnaire dans ton domaine
- Des opportunités professionnelles venues de loin

## Conseils pour ce transit
- Donne une dimension internationale à ta carrière
- Partage ta vision à travers ton travail
- Construis une réputation de penseur original""",

    ('sagittarius', 11): """# ♅ Transit d'Uranus en Sagittaire — Maison XI

**En une phrase :** Tes cercles sociaux deviennent internationaux et tes aspirations embrassent le monde.

## L'énergie du moment
Uranus en Sagittaire traverse ta maison des amitiés et des idéaux avec une énergie cosmopolite. Tu es attiré par des groupes internationaux, des causes globales, des réseaux qui transcendent les frontières. Tes amis viennent de partout et tes aspirations concernent l'humanité entière.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes de cultures diverses
- L'engagement dans des causes globales ou humanitaires
- Des aspirations qui dépassent les frontières nationales
- L'appartenance à des réseaux internationaux

## Conseils pour ce transit
- Cultive un réseau d'amis international
- Engage-toi pour des causes qui concernent l'humanité
- Rêve à l'échelle du monde""",

    ('sagittarius', 12): """# ♅ Transit d'Uranus en Sagittaire — Maison XII

**En une phrase :** Une transformation spirituelle profonde élargit ta connexion à l'universel.

## L'énergie du moment
Uranus en Sagittaire pénètre ta maison des profondeurs cachées avec une énergie de quête spirituelle. Tu accèdes à des états de conscience élargis, des révélations sur le sens de l'existence. Des croyances inconscientes limitantes peuvent être libérées. Ta spiritualité devient plus universelle.

## Ce que tu pourrais vivre
- Des expériences spirituelles ou mystiques élargissantes
- La libération de croyances inconscientes qui limitaient
- Des rêves symboliques riches de sens philosophique
- Une connexion à une sagesse universelle

## Conseils pour ce transit
- Ouvre-toi aux expériences spirituelles avec discernement
- Libère les croyances qui rétrécissent ta vision
- Développe une spiritualité universelle""",

    # ============================================================
    # URANUS EN CAPRICORNE (♅ en ♑)
    # ============================================================
    ('capricorn', 1): """# ♅ Transit d'Uranus en Capricorne — Maison I

**En une phrase :** Ton identité se restructure autour de nouvelles façons d'exercer l'autorité et la responsabilité.

## L'énergie du moment
Uranus en Capricorne dans ta maison I révolutionne ta façon de te présenter au monde avec une énergie de restructuration. Tu développes une nouvelle relation à l'autorité, la responsabilité et la maturité. Ton apparence peut devenir plus sobre mais avec une touche d'originalité. Tu incarnes une nouvelle façon d'être adulte.

## Ce que tu pourrais vivre
- Une transformation de ton rapport à l'autorité et la responsabilité
- Une apparence qui allie tradition et originalité
- Le besoin de restructurer ton identité sur des bases solides
- Une nouvelle façon d'incarner la maturité

## Conseils pour ce transit
- Réinvente ta relation à l'autorité et à la responsabilité
- Allie tradition et innovation dans ta présentation
- Deviens l'auteur d'une nouvelle façon d'être adulte""",

    ('capricorn', 2): """# ♅ Transit d'Uranus en Capricorne — Maison II

**En une phrase :** Tes finances se restructurent de façon innovante et tes valeurs s'ancrent dans le concret.

## L'énergie du moment
Uranus en Capricorne secoue ta maison des ressources avec une énergie de restructuration. Tu développes une approche plus stratégique et à long terme de tes finances. Tes valeurs allient tradition et innovation. Tu construis une sécurité financière sur des bases solides mais originales.

## Ce que tu pourrais vivre
- Une restructuration majeure de tes finances
- L'importance croissante de la planification à long terme
- Des valeurs qui allient tradition et innovation
- Des investissements stratégiques et durables

## Conseils pour ce transit
- Restructure tes finances avec vision à long terme
- Allie prudence et innovation dans tes investissements
- Construis une sécurité financière durable""",

    ('capricorn', 3): """# ♅ Transit d'Uranus en Capricorne — Maison III

**En une phrase :** Ta communication devient plus structurée et stratégique avec une touche d'originalité.

## L'énergie du moment
Uranus en Capricorne électrifie ta maison de la communication avec une énergie de structure. Tes idées gagnent en profondeur et en pragmatisme. Tu communiques de façon plus stratégique, avec autorité mais originalité. Tes apprentissages s'orientent vers des compétences durables.

## Ce que tu pourrais vivre
- Une communication plus structurée et stratégique
- L'apprentissage de compétences avec applications à long terme
- Des relations avec les proches qui gagnent en maturité
- Des idées qui allient profondeur et innovation

## Conseils pour ce transit
- Structure ta communication pour plus d'impact
- Apprends des compétences durables et utiles
- Communique avec autorité et ouverture""",

    ('capricorn', 4): """# ♅ Transit d'Uranus en Capricorne — Maison IV

**En une phrase :** Ton foyer et tes fondations se restructurent vers plus de solidité et d'authenticité.

## L'énergie du moment
Uranus en Capricorne dans ta maison IV transforme tes fondations avec une énergie de reconstruction. Tu pourrais entreprendre des travaux majeurs ou restructurer complètement ta vie familiale. Les traditions familiales sont révisées et adaptées. Tu construis des bases plus solides pour l'avenir.

## Ce que tu pourrais vivre
- Une restructuration majeure de ton lieu de vie
- Des changements dans les hiérarchies familiales
- La révision des traditions familiales
- La construction de fondations plus durables

## Conseils pour ce transit
- Restructure ton foyer pour qu'il serve tes objectifs
- Révise les traditions familiales avec respect et innovation
- Construis des bases solides pour les générations futures""",

    ('capricorn', 5): """# ♅ Transit d'Uranus en Capricorne — Maison V

**En une phrase :** Ta créativité se structure et tes amours demandent engagement et originalité.

## L'énergie du moment
Uranus en Capricorne dans ta maison de la créativité apporte une discipline à ton expression créative. Tu es attiré par des formes d'art qui demandent maîtrise et durabilité. En amour, tu recherches des relations sérieuses mais pas conventionnelles. Les plaisirs incluent l'accomplissement et la maîtrise.

## Ce que tu pourrais vivre
- Une créativité plus disciplinée et durable
- Des amours qui allient engagement et originalité
- Le plaisir de la maîtrise et de l'accomplissement
- Des relations avec les enfants plus structurées

## Conseils pour ce transit
- Canalise ta créativité dans des projets durables
- Recherche des relations sérieuses qui respectent ta liberté
- Trouve la joie dans la maîtrise progressive""",

    ('capricorn', 6): """# ♅ Transit d'Uranus en Capricorne — Maison VI

**En une phrase :** Ton quotidien se restructure pour plus d'efficacité et ta santé bénéficie de discipline.

## L'énergie du moment
Uranus en Capricorne révolutionne ta maison du travail quotidien avec une énergie de restructuration. Tu réorganises tes routines pour plus d'efficacité à long terme. Ta santé bénéficie d'approches disciplinées mais innovantes. Ton environnement de travail se professionnalise.

## Ce que tu pourrais vivre
- Une restructuration complète de tes routines
- Des méthodes de travail plus efficaces et stratégiques
- Une santé améliorée par des habitudes disciplinées
- Un environnement professionnel qui se transforme

## Conseils pour ce transit
- Restructure ton quotidien pour l'efficacité à long terme
- Adopte des habitudes de santé durables
- Professionnalise ton approche du travail""",

    ('capricorn', 7): """# ♅ Transit d'Uranus en Capricorne — Maison VII

**En une phrase :** Tes relations se restructurent vers plus de maturité et de partenariats stratégiques.

## L'énergie du moment
Uranus en Capricorne traverse ta maison des partenariats avec une énergie de restructuration. Tes relations gagnent en maturité et en profondeur. Tu attires des partenaires établis ou ambitieux qui t'aident à construire. Les partenariats professionnels prennent de l'importance.

## Ce que tu pourrais vivre
- Des relations qui se formalisent ou se restructurent
- Des partenaires ambitieux et établis
- L'importance croissante des partenariats professionnels
- Des unions basées sur des objectifs communs à long terme

## Conseils pour ce transit
- Construis des partenariats avec vision à long terme
- Formalise tes relations quand c'est approprié
- Choisis des partenaires qui t'aident à grandir""",

    ('capricorn', 8): """# ♅ Transit d'Uranus en Capricorne — Maison VIII

**En une phrase :** Des transformations profondes restructurent ta relation au pouvoir et aux ressources partagées.

## L'énergie du moment
Uranus en Capricorne plonge dans ta maison des transformations avec une énergie de restructuration. Ta relation au pouvoir, au contrôle et aux ressources partagées est profondément révisée. Des arrangements financiers sont restructurés. Tu développes une nouvelle relation à l'autorité sur les ressources communes.

## Ce que tu pourrais vivre
- Une restructuration des arrangements financiers partagés
- Des changements dans les dynamiques de pouvoir
- Une transformation de ta relation au contrôle
- Des héritages ou successions qui se clarifient

## Conseils pour ce transit
- Restructure les arrangements financiers équitablement
- Développe une relation saine au pouvoir
- Transforme les structures qui ne servent plus""",

    ('capricorn', 9): """# ♅ Transit d'Uranus en Capricorne — Maison IX

**En une phrase :** Ta philosophie se structure autour de principes solides mais toujours évolutifs.

## L'énergie du moment
Uranus en Capricorne traverse ta maison des horizons lointains avec une énergie de structuration. Tu développes une philosophie de vie qui allie profondeur et pragmatisme. Tes voyages peuvent avoir des objectifs professionnels ou éducatifs. Tu construis une vision du monde qui a des applications concrètes.

## Ce que tu pourrais vivre
- Le développement d'une philosophie structurée et pratique
- Des voyages avec des objectifs professionnels ou éducatifs
- L'attrait pour des enseignements qui ont fait leurs preuves
- Une spiritualité qui s'intègre dans la vie concrète

## Conseils pour ce transit
- Structure ta philosophie de vie autour de principes solides
- Applique tes croyances dans le monde concret
- Voyage et étudie avec des objectifs clairs""",

    ('capricorn', 10): """# ♅ Transit d'Uranus en Capricorne — Maison X

**En une phrase :** Ta carrière connaît une révolution structurelle qui redéfinit ton autorité professionnelle.

## L'énergie du moment
Uranus traverse sa maison de chute avec l'énergie structurante du Capricorne, créant une tension créative. Ta carrière peut connaître des restructurations majeures, des changements de direction vers plus d'authenticité. Tu révolutionnes ta façon d'exercer l'autorité professionnelle. Les anciennes structures cèdent la place à de nouvelles.

## Ce que tu pourrais vivre
- Des restructurations majeures dans ta carrière
- Une nouvelle façon d'exercer l'autorité et le leadership
- La remise en question des structures établies
- L'opportunité de construire quelque chose de nouveau et durable

## Conseils pour ce transit
- Accepte les restructurations comme opportunités
- Redéfinis ton autorité professionnelle de façon authentique
- Construis des structures nouvelles et durables""",

    ('capricorn', 11): """# ♅ Transit d'Uranus en Capricorne — Maison XI

**En une phrase :** Tes cercles sociaux se restructurent et tes aspirations deviennent plus concrètes.

## L'énergie du moment
Uranus en Capricorne traverse ta maison des amitiés et des idéaux avec une énergie de structuration. Tes cercles sociaux se professionnalisent ou se réorganisent. Tes aspirations deviennent plus réalistes et stratégiques. Tu rejoins des groupes qui ont des objectifs concrets et à long terme.

## Ce que tu pourrais vivre
- Des cercles sociaux qui se restructurent
- Des aspirations plus concrètes et réalisables
- L'attrait pour des groupes avec des objectifs clairs
- Des amitiés basées sur des intérêts professionnels ou stratégiques

## Conseils pour ce transit
- Restructure tes cercles sociaux selon tes objectifs
- Définis des aspirations réalistes mais ambitieuses
- Rejoins des groupes qui construisent quelque chose de concret""",

    ('capricorn', 12): """# ♅ Transit d'Uranus en Capricorne — Maison XII

**En une phrase :** Une transformation profonde restructure tes patterns inconscients de limitation et d'autorité.

## L'énergie du moment
Uranus en Capricorne pénètre ta maison des profondeurs cachées, travaillant sur tes patterns inconscients liés à l'autorité, la responsabilité et les limitations. Des peurs anciennes de ne pas être à la hauteur peuvent être révélées et libérées. Tu restructures ta relation inconsciente au pouvoir et à la structure.

## Ce que tu pourrais vivre
- La révélation de patterns inconscients de limitation
- La libération de peurs liées à l'autorité ou l'échec
- Une restructuration de ta relation au pouvoir intérieur
- Des rêves impliquant des figures d'autorité

## Conseils pour ce transit
- Travaille sur tes peurs inconscientes de l'échec
- Libère les structures intérieures qui ne te servent plus
- Développe une autorité intérieure saine""",

    # ============================================================
    # URANUS EN VERSEAU (♅ en ♒)
    # ============================================================
    ('aquarius', 1): """# ♅ Transit d'Uranus en Verseau — Maison I

**En une phrase :** Ton identité atteint une expression révolutionnaire maximale de ton unicité.

## L'énergie du moment
Uranus en Verseau dans ta maison I est dans son signe domicile, maximisant l'énergie de révolution identitaire. Tu deviens l'incarnation même de l'originalité et de l'avant-garde. Ton apparence peut devenir radicalement différente, futuriste, unique. Tu refuses tout conformisme et incarnes le changement.

## Ce que tu pourrais vivre
- Une expression maximale de ton unicité
- Des changements radicaux d'apparence ou de style
- L'attrait pour les technologies et les idées futuristes
- Une identité qui défie toutes les conventions

## Conseils pour ce transit
- Embrasse pleinement ton unicité
- Sois un pionnier de nouvelles façons d'être
- Garde un ancrage malgré le désir de révolutionner""",

    ('aquarius', 2): """# ♅ Transit d'Uranus en Verseau — Maison II

**En une phrase :** Tes valeurs et finances se révolutionnent vers des modèles innovants et humanitaires.

## L'énergie du moment
Uranus en Verseau secoue ta maison des ressources avec une énergie maximale d'innovation. Tes revenus peuvent venir de technologies, d'innovations ou de causes humanitaires. Tu valorises la liberté, l'originalité et le progrès au-dessus de la sécurité conventionnelle. De nouveaux modèles économiques t'attirent.

## Ce que tu pourrais vivre
- Des revenus liés aux technologies ou à l'innovation
- L'attrait pour de nouveaux modèles économiques
- Des valeurs centrées sur la liberté et le progrès
- Une relation plus détachée aux possessions matérielles

## Conseils pour ce transit
- Explore les économies innovantes et alternatives
- Investis dans les technologies et le futur
- Développe une relation plus libre à l'argent""",

    ('aquarius', 3): """# ♅ Transit d'Uranus en Verseau — Maison III

**En une phrase :** Ta pensée et communication atteignent des sommets d'originalité et d'innovation.

## L'énergie du moment
Uranus en Verseau électrifie sa propre maison de la communication avec une puissance maximale. Tes idées sont à l'avant-garde, tes connexions mentales brillantes et originales. Tu communiques de façon révolutionnaire, peut-être à travers les dernières technologies. Ton réseau de proximité devient un laboratoire d'idées.

## Ce que tu pourrais vivre
- Des idées brillantes et avant-gardistes
- L'utilisation innovante des technologies de communication
- Un réseau de proches qui partagent tes visions
- Une pensée qui connecte des concepts éloignés

## Conseils pour ce transit
- Laisse ta pensée explorer les frontières
- Utilise les technologies pour amplifier tes idées
- Crée un réseau de penseurs originaux""",

    ('aquarius', 4): """# ♅ Transit d'Uranus en Verseau — Maison IV

**En une phrase :** Ton foyer devient un laboratoire du futur et ta famille une communauté d'esprits libres.

## L'énergie du moment
Uranus en Verseau dans ta maison IV transforme ton espace domestique en hub technologique et communautaire. Tu pourrais vivre en communauté, avoir un foyer connecté au monde, ou créer une famille non conventionnelle. Tes racines deviennent celles de l'humanité plutôt que d'un seul lignage.

## Ce que tu pourrais vivre
- Un foyer high-tech et connecté
- Des formes de vie communautaire ou alternatives
- Une famille qui transcende les liens biologiques
- Des racines basées sur des idées plutôt que le sang

## Conseils pour ce transit
- Crée un espace de vie qui représente le futur
- Explore des formes de vie collective
- Élargis ta définition de la famille""",

    ('aquarius', 5): """# ♅ Transit d'Uranus en Verseau — Maison V

**En une phrase :** Ta créativité s'exprime de façon révolutionnaire et tes amours transcendent les conventions.

## L'énergie du moment
Uranus en Verseau enflamme ta maison de la créativité avec une énergie maximale d'innovation. Ta créativité utilise les nouvelles technologies, explore des territoires inédits, défie les normes artistiques. En amour, tu refuses les scripts conventionnels et explores des formes de relation originales.

## Ce que tu pourrais vivre
- Une créativité qui utilise les dernières technologies
- Des amours qui défient les conventions sociales
- Des plaisirs liés aux innovations et aux idées futuristes
- Des relations avec les enfants centrées sur leur unicité

## Conseils pour ce transit
- Explore les frontières de la création
- Définis tes propres règles en amour
- Célèbre l'unicité dans tous les domaines""",

    ('aquarius', 6): """# ♅ Transit d'Uranus en Verseau — Maison VI

**En une phrase :** Ton quotidien se digitalise complètement et ta santé bénéficie d'innovations.

## L'énergie du moment
Uranus en Verseau révolutionne ta maison du travail quotidien avec une énergie technologique maximale. Ton travail peut devenir entièrement digital, flexible, ou lié aux innovations. Ta santé bénéficie des dernières avancées technologiques et d'approches non conventionnelles.

## Ce que tu pourrais vivre
- Un travail entièrement digitalisé et flexible
- L'utilisation de technologies de santé avancées
- Des routines qui intègrent les dernières innovations
- Un environnement de travail futuriste

## Conseils pour ce transit
- Embrasse la transformation digitale de ton travail
- Explore les technologies de santé et bien-être
- Crée un quotidien qui préfigure le futur""",

    ('aquarius', 7): """# ♅ Transit d'Uranus en Verseau — Maison VII

**En une phrase :** Tes relations révolutionnent les modèles conventionnels vers plus de liberté et d'équité.

## L'énergie du moment
Uranus en Verseau traverse ta maison des partenariats avec une énergie de révolution relationnelle. Tu attires des partenaires originaux, visionnaires, parfois excentriques. Tes relations défient les modèles traditionnels et expérimentent de nouvelles formes. La liberté individuelle reste primordiale dans l'union.

## Ce que tu pourrais vivre
- Des relations qui inventent leurs propres règles
- Des partenaires brillants et non conventionnels
- Le besoin de liberté maximale dans l'engagement
- Des unions basées sur des idéaux partagés

## Conseils pour ce transit
- Invente les règles de tes relations
- Choisis des partenaires qui respectent ta liberté
- Crée des partenariats basés sur des visions communes""",

    ('aquarius', 8): """# ♅ Transit d'Uranus en Verseau — Maison VIII

**En une phrase :** Des transformations radicales révolutionnent ta relation au partage et au pouvoir collectif.

## L'énergie du moment
Uranus en Verseau plonge dans ta maison des transformations avec une énergie de révolution du partage. Les ressources communes, les systèmes économiques partagés, les formes de pouvoir collectif sont repensés. Ta relation à la transformation devient plus collective et humanitaire.

## Ce que tu pourrais vivre
- Des nouvelles formes de partage des ressources
- L'intérêt pour les transformations collectives
- Des technologies qui changent la relation au pouvoir
- Une compréhension plus universelle des cycles de transformation

## Conseils pour ce transit
- Explore les nouvelles formes d'économie partagée
- Participe aux transformations collectives
- Développe une vision humanitaire du partage""",

    ('aquarius', 9): """# ♅ Transit d'Uranus en Verseau — Maison IX

**En une phrase :** Ta vision du monde atteint une perspective cosmique et universelle.

## L'énergie du moment
Uranus en Verseau traverse ta maison des horizons lointains avec une énergie de vision globale. Tu développes une philosophie qui embrasse l'humanité entière, peut-être même l'univers. Tes voyages peuvent inclure l'exploration de nouvelles frontières. Ta spiritualité devient cosmique et universelle.

## Ce que tu pourrais vivre
- Une philosophie qui embrasse l'universel
- L'intérêt pour l'espace, les nouvelles frontières
- Des voyages vers des lieux d'innovation et de futur
- Une spiritualité qui transcende les traditions

## Conseils pour ce transit
- Développe une vision véritablement universelle
- Explore les frontières de la connaissance humaine
- Embrasse une spiritualité cosmique""",

    ('aquarius', 10): """# ♅ Transit d'Uranus en Verseau — Maison X

**En une phrase :** Ta carrière te positionne à l'avant-garde de l'innovation et du changement social.

## L'énergie du moment
Uranus en Verseau révolutionne ta maison de la carrière avec une énergie maximale d'innovation. Tu pourrais devenir un pionnier dans ton domaine, travailler dans les technologies de pointe ou le changement social. Ta réputation se construit autour de ta capacité à innover et à voir le futur.

## Ce que tu pourrais vivre
- Une carrière à l'avant-garde de ton domaine
- Des positions liées à l'innovation ou au changement social
- La réputation d'être un visionnaire
- Des opportunités dans les technologies ou l'humanitaire

## Conseils pour ce transit
- Positionne-toi comme innovateur dans ton domaine
- Utilise ta carrière pour contribuer au changement
- Construis une réputation de visionnaire""",

    ('aquarius', 11): """# ♅ Transit d'Uranus en Verseau — Maison XI

**En une phrase :** Tu incarnes pleinement le pouvoir des réseaux et des aspirations collectives.

## L'énergie du moment
Uranus traverse sa maison domicile dans son signe domicile, créant une puissance maximale. Tes réseaux sociaux, tes aspirations collectives, ton engagement humanitaire atteignent leur pleine expression. Tu es au cœur des mouvements qui façonnent le futur de l'humanité.

## Ce que tu pourrais vivre
- Un réseau social étendu et influent
- L'engagement dans des causes qui changent le monde
- Des aspirations qui concernent l'humanité entière
- Un rôle central dans des mouvements collectifs

## Conseils pour ce transit
- Utilise tes réseaux pour créer le changement
- Engage-toi pleinement pour tes idéaux
- Deviens un catalyseur du futur que tu veux voir""",

    ('aquarius', 12): """# ♅ Transit d'Uranus en Verseau — Maison XII

**En une phrase :** Une révolution spirituelle te connecte à la conscience universelle.

## L'énergie du moment
Uranus en Verseau pénètre ta maison des profondeurs cachées avec une énergie de révélation cosmique. Tu peux accéder à des états de conscience qui transcendent l'individuel et te connectent au collectif universel. Des patterns inconscients liés à l'exclusion ou à la différence peuvent être libérés.

## Ce que tu pourrais vivre
- Des expériences de conscience universelle
- La libération de sentiments d'aliénation inconscients
- Des intuitions sur le futur collectif
- Une spiritualité qui transcende l'ego individuel

## Conseils pour ce transit
- Explore les états de conscience élargis
- Libère les patterns d'exclusion
- Connecte-toi à la conscience universelle""",

    # ============================================================
    # URANUS EN POISSONS (♅ en ♓)
    # ============================================================
    ('pisces', 1): """# ♅ Transit d'Uranus en Poissons — Maison I

**En une phrase :** Ton identité se dissout et se reforme autour d'une connexion plus spirituelle et universelle.

## L'énergie du moment
Uranus en Poissons dans ta maison I crée une révolution spirituelle de ton identité. Les frontières de ton moi deviennent plus fluides, plus perméables à l'universel. Tu peux développer des dons intuitifs ou artistiques exceptionnels. Ton apparence peut devenir plus éthérée, mystérieuse, hors du temps.

## Ce que tu pourrais vivre
- Une identité plus fluide et spirituelle
- Le développement de capacités intuitives ou artistiques
- Une apparence qui reflète une connexion au mystère
- Le besoin de transcender les limitations de l'ego

## Conseils pour ce transit
- Laisse ton identité devenir plus fluide
- Développe tes dons intuitifs et créatifs
- Garde un ancrage tout en explorant le mystère""",

    ('pisces', 2): """# ♅ Transit d'Uranus en Poissons — Maison II

**En une phrase :** Ta relation aux ressources devient plus intuitive et moins attachée au matériel.

## L'énergie du moment
Uranus en Poissons secoue ta maison des ressources avec une énergie dissolvante et spirituelle. Tu développes une relation plus détachée aux possessions matérielles. Tes revenus peuvent venir de dons créatifs, spirituels ou intuitifs. Tu apprends que la vraie richesse est immatérielle.

## Ce que tu pourrais vivre
- Un détachement progressif des possessions matérielles
- Des revenus liés à l'art, la spiritualité ou l'intuition
- Une vision de l'abondance qui transcende le matériel
- Des fluctuations financières qui enseignent le lâcher-prise

## Conseils pour ce transit
- Développe une relation plus spirituelle à l'abondance
- Explore des sources de revenus créatives ou intuitives
- Apprends à faire confiance à l'univers pour tes besoins""",

    ('pisces', 3): """# ♅ Transit d'Uranus en Poissons — Maison III

**En une phrase :** Ta communication devient plus intuitive et poétique, touchant des dimensions subtiles.

## L'énergie du moment
Uranus en Poissons électrifie ta maison de la communication avec une énergie intuitive et imaginative. Tes pensées deviennent plus symboliques, tes communications plus poétiques. Tu captes des informations de façon non rationnelle. Tes relations proches deviennent plus empathiques.

## Ce que tu pourrais vivre
- Une pensée plus intuitive et symbolique
- Des communications qui touchent les cœurs et les âmes
- Des capacités télépathiques ou empathiques accrues
- Des relations proches basées sur la connexion subtile

## Conseils pour ce transit
- Fais confiance à ton intuition dans la communication
- Exprime-toi de façon plus artistique et poétique
- Développe l'empathie dans tes échanges""",

    ('pisces', 4): """# ♅ Transit d'Uranus en Poissons — Maison IV

**En une phrase :** Ton foyer devient un sanctuaire spirituel et tes racines se dissolvent dans l'universel.

## L'énergie du moment
Uranus en Poissons dans ta maison IV dissout les frontières de ton espace domestique. Ton foyer peut devenir un lieu de méditation, de création artistique, d'ouverture au mystère. Les liens familiaux transcendent le biologique pour devenir spirituels. Tu trouves ta vraie maison dans le divin.

## Ce que tu pourrais vivre
- Un foyer transformé en espace sacré
- La dissolution des frontières familiales conventionnelles
- Des connexions ancestrales ou spirituelles avec le lignage
- La découverte que ta vraie maison est universelle

## Conseils pour ce transit
- Crée un espace de vie propice à la spiritualité
- Explore les dimensions spirituelles de tes racines
- Trouve ta sécurité dans ta connexion au divin""",

    ('pisces', 5): """# ♅ Transit d'Uranus en Poissons — Maison V

**En une phrase :** Ta créativité atteint des dimensions transcendantes et tes amours touchent le sacré.

## L'énergie du moment
Uranus en Poissons enflamme ta maison de la créativité avec une énergie visionnaire. Tu es capable de créations qui touchent l'âme, qui capturent des dimensions invisibles. En amour, tu recherches une union mystique, une connexion qui transcende le physique. Les plaisirs deviennent plus subtils et spirituels.

## Ce que tu pourrais vivre
- Une créativité inspirée qui touche le transcendant
- Des amours qui ont une dimension spirituelle
- Des états de joie et de béatitude spontanés
- Une connexion plus intuitive avec les enfants

## Conseils pour ce transit
- Laisse ta créativité être un canal pour le divin
- Recherche l'amour sacré sans fuir l'incarnation
- Trouve la joie dans la connexion au mystère""",

    ('pisces', 6): """# ♅ Transit d'Uranus en Poissons — Maison VI

**En une phrase :** Ton quotidien s'imprègne de spiritualité et ta santé bénéficie de méthodes énergétiques.

## L'énergie du moment
Uranus en Poissons révolutionne ta maison du travail quotidien avec une énergie de service spirituel. Ton travail peut acquérir une dimension de service désintéressé ou de guérison. Ta santé bénéficie de méthodes énergétiques et subtiles. Le quotidien devient une pratique spirituelle.

## Ce que tu pourrais vivre
- Un travail orienté vers le service ou la guérison
- L'utilisation de méthodes de santé énergétiques
- Un quotidien vécu comme pratique spirituelle
- La compassion dans les relations de travail

## Conseils pour ce transit
- Intègre la spiritualité dans ton quotidien
- Explore les méthodes de guérison énergétique
- Fais de chaque tâche un acte de service""",

    ('pisces', 7): """# ♅ Transit d'Uranus en Poissons — Maison VII

**En une phrase :** Tes relations touchent des dimensions spirituelles et les frontières entre toi et l'autre se dissolvent.

## L'énergie du moment
Uranus en Poissons traverse ta maison des partenariats avec une énergie d'union mystique. Tu attires des partenaires spirituels, artistes ou intuitifs. Les relations deviennent des espaces de fusion et de croissance spirituelle. Attention à ne pas perdre ton identité dans l'autre.

## Ce que tu pourrais vivre
- Des relations avec une dimension spirituelle
- Des partenaires intuitifs, artistes ou mystiques
- Une empathie profonde dans les unions
- Le défi de maintenir des limites saines

## Conseils pour ce transit
- Recherche des partenaires spirituellement alignés
- Maintiens ton identité tout en fusionnant
- Fais de la relation un chemin spirituel""",

    ('pisces', 8): """# ♅ Transit d'Uranus en Poissons — Maison VIII

**En une phrase :** Des transformations profondes dissolvent les peurs et ouvrent à des dimensions mystiques.

## L'énergie du moment
Uranus en Poissons plonge dans ta maison des transformations avec une énergie de dissolution spirituelle. Les peurs autour de la mort, du partage et de la perte peuvent être transcendées. Tu accèdes à des expériences mystiques profondes. Les ressources partagées peuvent avoir une dimension karmique.

## Ce que tu pourrais vivre
- La transcendance des peurs liées à la mort et à la perte
- Des expériences mystiques ou de sortie du corps
- Une compréhension intuitive des cycles cosmiques
- La dissolution des attachements aux ressources partagées

## Conseils pour ce transit
- Laisse tes peurs se dissoudre dans la confiance spirituelle
- Explore les dimensions mystiques avec discernement
- Accepte le mystère de la transformation""",

    ('pisces', 9): """# ♅ Transit d'Uranus en Poissons — Maison IX

**En une phrase :** Ta philosophie fusionne avec la mystique et tes voyages touchent des dimensions spirituelles.

## L'énergie du moment
Uranus en Poissons traverse ta maison des horizons lointains avec une énergie de quête mystique. Tu es attiré par des sagesses qui dissolvent les frontières entre les traditions, qui pointent vers l'unité. Tes voyages peuvent être intérieurs autant qu'extérieurs. Tu développes une vision du monde fondamentalement spirituelle.

## Ce que tu pourrais vivre
- L'attrait pour des traditions mystiques et contemplatives
- Des voyages vers des lieux sacrés ou des retraites
- Une philosophie qui embrasse l'unité de toutes choses
- Des expériences de conscience élargie

## Conseils pour ce transit
- Explore les traditions mystiques avec ouverture
- Voyage vers des lieux qui nourrissent ton âme
- Développe une vision unitive de la réalité""",

    ('pisces', 10): """# ♅ Transit d'Uranus en Poissons — Maison X

**En une phrase :** Ta carrière s'oriente vers le service, l'art ou la spiritualité de façon inattendue.

## L'énergie du moment
Uranus en Poissons révolutionne ta maison de la carrière avec une énergie de service et de créativité. Tu pourrais te diriger vers des carrières artistiques, spirituelles ou de service désintéressé. Ta réputation se construit autour de ta compassion et de ta créativité. Le succès conventionnel peut perdre de son attrait.

## Ce que tu pourrais vivre
- Une carrière dans l'art, la spiritualité ou le service
- Le détachement des définitions conventionnelles du succès
- Une réputation basée sur la compassion et la créativité
- Des opportunités qui semblent guidées par le destin

## Conseils pour ce transit
- Aligne ta carrière avec ta mission d'âme
- Accepte que le succès puisse prendre des formes inattendues
- Sers le monde à travers ton travail""",

    ('pisces', 11): """# ♅ Transit d'Uranus en Poissons — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des communautés spirituelles et tes aspirations touchent le divin.

## L'énergie du moment
Uranus en Poissons traverse ta maison des amitiés et des idéaux avec une énergie de communion spirituelle. Tu es attiré par des groupes spirituels, des communautés d'artistes, des collectifs animés par la compassion. Tes aspirations concernent l'éveil collectif et la guérison du monde.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes spirituellement éveillées
- L'appartenance à des communautés spirituelles
- Des aspirations liées à l'éveil et à la guérison collective
- Des expériences de conscience de groupe

## Conseils pour ce transit
- Rejoins des communautés alignées avec tes aspirations spirituelles
- Contribue à l'éveil collectif par ta présence
- Rêve d'un monde guéri et éveillé""",

    ('pisces', 12): """# ♅ Transit d'Uranus en Poissons — Maison XII

**En une phrase :** Une révolution spirituelle complète dissout les dernières illusions et t'ouvre à l'infini.

## L'énergie du moment
Uranus en Poissons traverse sa maison domicile dans le signe de la transcendance, créant une puissance spirituelle maximale. Tu peux vivre des expériences mystiques profondes qui dissolvent les illusions de l'ego. Les derniers voiles entre toi et l'infini peuvent tomber. C'est une période de transformation spirituelle ultime.

## Ce que tu pourrais vivre
- Des expériences mystiques et unitives profondes
- La dissolution des dernières illusions de séparation
- L'accès à des niveaux de conscience élevés
- La libération karmique et spirituelle

## Conseils pour ce transit
- Ouvre-toi aux expériences spirituelles avec discernement
- Laisse les illusions se dissoudre naturellement
- Confie-toi à l'infini tout en restant ancré""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in TRANSIT_URANUS_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_uranus',
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
                subject='transit_uranus',
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
        print(f"✅ Transit Uranus (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
