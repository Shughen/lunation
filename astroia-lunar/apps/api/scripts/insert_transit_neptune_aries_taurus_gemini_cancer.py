#!/usr/bin/env python3
"""Insert transit_neptune interpretations for Aries, Taurus, Gemini, Cancer (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_NEPTUNE_INTERPRETATIONS = {
    # ============================================================
    # NEPTUNE EN BÉLIER (♆ en ♈)
    # ============================================================
    ('aries', 1): """# ♆ Transit de Neptune en Bélier — Maison I

**En une phrase :** Ton identité se dissout pour renaître autour d'une inspiration spirituelle active.

## L'énergie du moment
Neptune en Bélier dans ta maison I crée une brume autour de ton sens de soi, mais une brume chargée d'inspiration. Tu peux te sentir incertain de qui tu es vraiment, mais cette dissolution ouvre la porte à une identité plus spirituellement inspirée. Tu incarnes une nouvelle forme de guerrier spirituel ou d'artiste pionnier.

## Ce que tu pourrais vivre
- Une confusion temporaire sur ton identité et ta direction
- L'émergence d'un nouveau toi plus inspiré et spirituel
- Des idéaux élevés concernant qui tu veux devenir
- Une sensibilité accrue qui peut te sembler vulnérable

## Conseils pour ce transit
- Accepte la dissolution comme prélude à la renaissance
- Ancre tes idéaux dans l'action concrète
- Protège ta sensibilité sans te fermer""",

    ('aries', 2): """# ♆ Transit de Neptune en Bélier — Maison II

**En une phrase :** Ta relation aux ressources se spiritualise et tes valeurs deviennent plus idéalistes.

## L'énergie du moment
Neptune en Bélier dissout tes certitudes financières pour les remplacer par des valeurs plus élevées. Tu peux être moins attaché au matériel mais aussi plus vulnérable aux illusions financières. L'argent peut venir de poursuites inspirées ou artistiques. Tes valeurs s'orientent vers l'action pour le bien commun.

## Ce que tu pourrais vivre
- Une relation plus détachée à l'argent et aux possessions
- Des idéaux élevés concernant ce qui a de la valeur
- Un risque de confusion ou de déception financière
- Des revenus possibles de sources artistiques ou spirituelles

## Conseils pour ce transit
- Garde un ancrage pratique dans tes finances
- Méfie-toi des investissements qui semblent trop beaux
- Aligne tes dépenses avec tes valeurs spirituelles""",

    ('aries', 3): """# ♆ Transit de Neptune en Bélier — Maison III

**En une phrase :** Ta pensée devient plus intuitive et ta communication plus inspirée.

## L'énergie du moment
Neptune en Bélier dans ta maison de la communication apporte une dimension intuitive et poétique à ton mental. Tu peux capter des informations de façon non rationnelle, communiquer de manière plus inspirante. Attention à la confusion dans les échanges quotidiens. Tes idées peuvent être visionnaires mais parfois floues.

## Ce que tu pourrais vivre
- Une pensée plus intuitive et imaginative
- Une communication qui touche et inspire
- Des malentendus possibles dans les échanges quotidiens
- Des relations avec les proches teintées d'idéalisme

## Conseils pour ce transit
- Fais confiance à ton intuition tout en vérifiant les faits
- Exprime-toi de façon artistique et inspirée
- Clarifie les communications importantes par écrit""",

    ('aries', 4): """# ♆ Transit de Neptune en Bélier — Maison IV

**En une phrase :** Ton foyer devient un sanctuaire spirituel et tes racines se reconnectent au divin.

## L'énergie du moment
Neptune en Bélier dans ta maison IV dissout les frontières de ton espace domestique pour en faire un lieu sacré. Tu peux idéaliser la famille ou la maison parfaite. Des secrets familiaux peuvent émerger. Tu cherches une sécurité qui vient de la connexion spirituelle plutôt que des murs.

## Ce que tu pourrais vivre
- Un foyer transformé en espace de méditation ou création
- Des révélations sur l'histoire spirituelle de ta famille
- Une idéalisation de la vie domestique parfaite
- Le besoin de sécurité émotionnelle et spirituelle

## Conseils pour ce transit
- Crée un espace sacré dans ton foyer
- Accepte ta famille telle qu'elle est, pas idéalisée
- Trouve ta sécurité dans ta connexion intérieure""",

    ('aries', 5): """# ♆ Transit de Neptune en Bélier — Maison V

**En une phrase :** Ta créativité atteint des dimensions inspirées et tes amours deviennent idéalistes.

## L'énergie du moment
Neptune en Bélier enflamme ta maison de la créativité avec une inspiration divine. Tu es capable de créations qui touchent l'âme et transcendent le commun. En amour, tu peux idéaliser tes partenaires, vivre des romances presque mystiques mais parfois déconnectées de la réalité.

## Ce que tu pourrais vivre
- Une créativité exceptionnellement inspirée
- Des amours romantiques mais potentiellement illusoires
- L'idéalisation des relations et des plaisirs
- Une connexion plus intuitive avec les enfants

## Conseils pour ce transit
- Canalise ton inspiration dans des œuvres concrètes
- Garde les pieds sur terre en amour
- Profite de la magie tout en restant lucide""",

    ('aries', 6): """# ♆ Transit de Neptune en Bélier — Maison VI

**En une phrase :** Ton quotidien se spiritualise et ta santé demande une approche plus holistique.

## L'énergie du moment
Neptune en Bélier dans ta maison du travail quotidien dissout les frontières entre le sacré et le profane. Ton travail peut devenir un service spirituel ou artistique. Ta santé est sensible aux influences subtiles et bénéficie d'approches holistiques. Attention à la confusion dans l'organisation quotidienne.

## Ce que tu pourrais vivre
- Un travail qui devient une forme de service spirituel
- Une sensibilité accrue aux environnements et substances
- Le besoin d'approches de santé plus naturelles et subtiles
- Une possible confusion dans l'organisation quotidienne

## Conseils pour ce transit
- Intègre la spiritualité dans ton quotidien
- Sois attentif à ce que tu absorbes (nourriture, environnement)
- Structure ton quotidien pour éviter la dispersion""",

    ('aries', 7): """# ♆ Transit de Neptune en Bélier — Maison VII

**En une phrase :** Tes relations se teintent d'idéalisme et tu cherches l'union spirituelle parfaite.

## L'énergie du moment
Neptune en Bélier traverse ta maison des partenariats, apportant une quête de l'amour idéal. Tu peux idéaliser tes partenaires ou chercher une union quasi-mystique. Les déceptions sont possibles si la réalité ne correspond pas au rêve. Des partenaires artistes ou spirituels peuvent apparaître.

## Ce que tu pourrais vivre
- L'idéalisation des partenaires et des relations
- La recherche d'une union spirituelle ou artistique
- Des déceptions si les illusions se dissipent
- Des partenaires intuitifs, artistes ou spirituels

## Conseils pour ce transit
- Aime les personnes réelles, pas tes projections
- Recherche la spiritualité dans les relations tout en restant ancré
- Communique clairement pour éviter les malentendus""",

    ('aries', 8): """# ♆ Transit de Neptune en Bélier — Maison VIII

**En une phrase :** Des transformations subtiles dissolvent tes peurs et t'ouvrent à des dimensions invisibles.

## L'énergie du moment
Neptune en Bélier plonge dans ta maison des transformations, dissolvant les frontières entre visible et invisible. Tu peux développer une sensibilité aux énergies subtiles, aux dimensions non physiques. Les questions de ressources partagées peuvent être floues. Une guérison profonde des peurs est possible.

## Ce que tu pourrais vivre
- Une ouverture aux dimensions subtiles et spirituelles
- La dissolution de peurs profondes autour de la mort
- Une possible confusion dans les finances partagées
- Des expériences mystiques ou psychiques

## Conseils pour ce transit
- Explore le subtil avec discernement
- Clarifie tous les arrangements financiers partagés
- Utilise cette sensibilité pour la guérison""",

    ('aries', 9): """# ♆ Transit de Neptune en Bélier — Maison IX

**En une phrase :** Ta quête spirituelle s'enflamme et ta vision du monde devient plus mystique.

## L'énergie du moment
Neptune en Bélier traverse ta maison des horizons lointains avec une énergie de quête active. Tu es attiré par des chemins spirituels qui demandent engagement et action. Tes voyages peuvent avoir une dimension de pèlerinage. Ta philosophie de vie fusionne avec une vision mystique du monde.

## Ce que tu pourrais vivre
- Une quête spirituelle active et engagée
- Des voyages vers des lieux sacrés ou inspirants
- Le développement d'une vision du monde mystique
- L'attrait pour des enseignements qui élèvent l'âme

## Conseils pour ce transit
- Suis ton appel spirituel avec discernement
- Voyage pour nourrir ton âme
- Intègre tes visions dans ta philosophie de vie""",

    ('aries', 10): """# ♆ Transit de Neptune en Bélier — Maison X

**En une phrase :** Ta carrière s'oriente vers des idéaux élevés et ta réputation se teinte de mystère.

## L'énergie du moment
Neptune en Bélier dans ta maison de la carrière dissout les ambitions conventionnelles pour les remplacer par des aspirations plus élevées. Ta vocation peut devenir artistique, spirituelle ou de service. Ta réputation peut être idéalisée ou mal comprise. Tu cherches un travail qui a du sens profond.

## Ce que tu pourrais vivre
- Une carrière qui s'oriente vers l'art, la spiritualité ou le service
- Une réputation teintée de mystère ou d'idéalisation
- Une confusion possible sur ta direction professionnelle
- Le besoin de trouver un sens profond dans ton travail

## Conseils pour ce transit
- Aligne ta carrière avec tes idéaux sans perdre le sens pratique
- Accepte que ta réputation soit vue différemment selon les gens
- Cherche le sens avant le succès conventionnel""",

    ('aries', 11): """# ♆ Transit de Neptune en Bélier — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des communautés d'âme et tes aspirations touchent le divin.

## L'énergie du moment
Neptune en Bélier traverse ta maison des amitiés et des idéaux avec une énergie de fraternité spirituelle. Tu es attiré par des groupes qui partagent des idéaux élevés et une vision inspirée. Attention à l'idéalisation des amis ou des causes. Tes rêves d'avenir incluent une dimension de transcendance.

## Ce que tu pourrais vivre
- Des amitiés basées sur des connexions d'âme
- L'attrait pour des groupes spirituels ou artistiques
- Une possible idéalisation puis déception dans les amitiés
- Des aspirations qui incluent le bien commun et le spirituel

## Conseils pour ce transit
- Rejoins des communautés alignées avec tes idéaux
- Reste lucide sur les personnes et les groupes
- Rêve grand tout en agissant concrètement""",

    ('aries', 12): """# ♆ Transit de Neptune en Bélier — Maison XII

**En une phrase :** Une dissolution spirituelle profonde te reconnecte à la source de tout.

## L'énergie du moment
Neptune traverse sa maison naturelle avec l'énergie active du Bélier, créant une puissante ouverture spirituelle. Les frontières de l'ego se dissolvent pour révéler l'unité avec le tout. Tu peux vivre des expériences mystiques profondes. D'anciens karmas et illusions sont libérés.

## Ce que tu pourrais vivre
- Des expériences mystiques et unitives profondes
- La dissolution de patterns inconscients anciens
- Une connexion plus forte à l'intuition et aux rêves
- La libération de peurs et illusions inconscientes

## Conseils pour ce transit
- Pratique la méditation et l'introspection
- Accueille les dissolutions comme des libérations
- Reste ancré tout en explorant les profondeurs""",

    # ============================================================
    # NEPTUNE EN TAUREAU (♆ en ♉)
    # ============================================================
    ('taurus', 1): """# ♆ Transit de Neptune en Taureau — Maison I

**En une phrase :** Ton identité se spiritualise à travers une connexion plus profonde aux sens et à la nature.

## L'énergie du moment
Neptune en Taureau dans ta maison I apporte une dimension spirituelle à ta présence physique. Tu développes une beauté naturelle, une grâce terrestre. Ton corps devient un temple et ta présence peut avoir un effet apaisant sur les autres. L'art et la beauté deviennent des expressions de ton être.

## Ce que tu pourrais vivre
- Une présence plus sereine et enracinée
- Le développement d'une beauté naturelle et spirituelle
- Une sensibilité accrue aux plaisirs sensoriels
- Une connexion plus profonde avec la nature

## Conseils pour ce transit
- Cultive la beauté comme pratique spirituelle
- Connecte-toi à ton corps avec révérence
- Ancre ta spiritualité dans les sens""",

    ('taurus', 2): """# ♆ Transit de Neptune en Taureau — Maison II

**En une phrase :** Tes valeurs évoluent vers une appréciation plus spirituelle de l'abondance terrestre.

## L'énergie du moment
Neptune en Taureau dans ta maison des ressources crée une relation presque mystique avec le monde matériel. Tu peux voir la spiritualité dans la nature, la nourriture, la beauté terrestre. Tes finances peuvent être floues mais tu découvres que la vraie richesse est dans l'appréciation simple de ce qui est.

## Ce que tu pourrais vivre
- Une vision spirituelle de l'abondance matérielle
- Des finances qui demandent plus de clarté et d'attention
- L'appréciation des plaisirs simples et naturels
- Une générosité qui peut dépasser la prudence

## Conseils pour ce transit
- Trouve le sacré dans le matériel sans t'y attacher
- Garde une gestion claire de tes finances
- Cultive la gratitude pour l'abondance simple""",

    ('taurus', 3): """# ♆ Transit de Neptune en Taureau — Maison III

**En une phrase :** Ta communication devient plus poétique et sensuelle, touchant les cœurs.

## L'énergie du moment
Neptune en Taureau dans ta maison de la communication apporte une qualité artistique et sensible à tes mots. Tu communiques avec une beauté naturelle qui touche les sens autant que l'intellect. Tes pensées s'imprègnent de qualités esthétiques. Les échanges avec les proches gagnent en profondeur émotionnelle.

## Ce que tu pourrais vivre
- Une communication plus artistique et touchante
- Des pensées qui s'expriment en images et sensations
- Des malentendus possibles si le concret n'est pas clarifié
- Une connexion plus profonde avec les proches

## Conseils pour ce transit
- Exprime-toi avec la beauté d'un artiste
- Clarifie les détails pratiques par écrit
- Apprécie les échanges silencieux et sensuels""",

    ('taurus', 4): """# ♆ Transit de Neptune en Taureau — Maison IV

**En une phrase :** Ton foyer devient un paradis terrestre où nature et spiritualité se rencontrent.

## L'énergie du moment
Neptune en Taureau dans ta maison IV transforme ton espace domestique en jardin d'Eden. Tu aspires à un foyer en harmonie avec la nature, beau et paisible. Les traditions familiales peuvent prendre une dimension spirituelle. Tu trouves la sécurité dans la connexion à la terre et à la nature.

## Ce que tu pourrais vivre
- Un foyer transformé en espace naturel et spirituel
- L'attrait pour une vie plus proche de la nature
- Une idéalisation de la vie rurale ou écologique
- Des racines familiales liées à la terre

## Conseils pour ce transit
- Crée un espace de vie qui honore la nature
- Connecte-toi aux traditions ancestrales de ta région
- Trouve ta sécurité dans la terre sous tes pieds""",

    ('taurus', 5): """# ♆ Transit de Neptune en Taureau — Maison V

**En une phrase :** Ta créativité s'exprime avec une beauté sensuelle et tes amours deviennent une communion des sens.

## L'énergie du moment
Neptune en Taureau dans ta maison de la créativité apporte une expression artistique riche et sensuelle. Tu es attiré par les arts qui engagent les sens : musique, sculpture, cuisine, parfums. En amour, tu recherches une connexion qui honore le corps autant que l'âme.

## Ce que tu pourrais vivre
- Une créativité sensuelle et esthétique
- Des amours qui célèbrent les sens et le corps
- Le plaisir des arts tactiles et sensuels
- Une romance idéalisée avec la nature ou la beauté

## Conseils pour ce transit
- Exprime ta créativité à travers les sens
- Apprécie la beauté de l'amour incarné
- Évite d'idéaliser les plaisirs au point de perdre la mesure""",

    ('taurus', 6): """# ♆ Transit de Neptune en Taureau — Maison VI

**En une phrase :** Ton quotidien devient une pratique de présence et ta santé bénéficie de la nature.

## L'énergie du moment
Neptune en Taureau dans ta maison du travail quotidien transforme les tâches ordinaires en méditations. Tu es attiré par un travail qui engage le corps et les sens de façon significative. Ta santé bénéficie de la connexion à la nature, de l'alimentation saine, des soins corporels respectueux.

## Ce que tu pourrais vivre
- Un travail qui devient une forme de méditation en mouvement
- L'attrait pour des métiers liés à la nature ou au corps
- Une santé soutenue par des pratiques naturelles
- Le besoin de beauté dans l'environnement de travail

## Conseils pour ce transit
- Transforme ton quotidien en pratique de présence
- Soigne ton corps avec des moyens naturels
- Travaille dans un environnement qui nourrit tes sens""",

    ('taurus', 7): """# ♆ Transit de Neptune en Taureau — Maison VII

**En une phrase :** Tes relations deviennent des jardins de délices où amour et beauté se cultivent.

## L'énergie du moment
Neptune en Taureau traverse ta maison des partenariats avec une énergie de romance terrestre. Tu attires des partenaires qui partagent ton amour de la beauté, de la nature, des plaisirs sensuels. L'amour devient une célébration des sens. Attention à idéaliser le confort au détriment de la croissance.

## Ce que tu pourrais vivre
- Des relations riches en plaisirs sensuels
- Des partenaires artistes ou connectés à la nature
- Une idéalisation du confort et de la stabilité en couple
- Le besoin de beauté partagée dans les relations

## Conseils pour ce transit
- Cultive la beauté ensemble dans tes relations
- Évite de confondre confort et vrai amour
- Apprécie les plaisirs simples partagés""",

    ('taurus', 8): """# ♆ Transit de Neptune en Taureau — Maison VIII

**En une phrase :** Des transformations profondes touchent ta relation aux possessions et au partage sensuel.

## L'énergie du moment
Neptune en Taureau dans ta maison des transformations dissout les attachements aux possessions et au contrôle. Tu découvres que le vrai partage transcende le matériel. Les questions d'argent commun peuvent être floues. Une dimension spirituelle se révèle dans l'intimité physique.

## Ce que tu pourrais vivre
- La dissolution d'attachements matériels profonds
- Une dimension spirituelle dans l'intimité physique
- Une confusion possible dans les finances partagées
- La transformation de ta relation à la possession

## Conseils pour ce transit
- Lâche prise sur les attachements matériels
- Explore la dimension sacrée de l'intimité
- Clarifie tous les arrangements financiers partagés""",

    ('taurus', 9): """# ♆ Transit de Neptune en Taureau — Maison IX

**En une phrase :** Ta quête spirituelle s'ancre dans la terre et la nature devient ton temple.

## L'énergie du moment
Neptune en Taureau traverse ta maison des horizons lointains avec une spiritualité terrestre. Tu es attiré par des sagesses qui honorent la nature, la Terre-Mère, les cycles naturels. Tes voyages peuvent te mener vers des lieux naturels sacrés. Ta philosophie intègre le corps et la terre.

## Ce que tu pourrais vivre
- Une spiritualité enracinée dans la nature
- Des voyages vers des sites naturels sacrés
- L'attrait pour des traditions qui honorent la Terre
- Une philosophie qui intègre le physique et le spirituel

## Conseils pour ce transit
- Trouve le sacré dans la nature
- Pèlerine vers des lieux naturels qui t'appellent
- Développe une spiritualité incarnée""",

    ('taurus', 10): """# ♆ Transit de Neptune en Taureau — Maison X

**En une phrase :** Ta carrière s'oriente vers la beauté, la nature ou des valeurs terriennes spiritualisées.

## L'énergie du moment
Neptune en Taureau dans ta maison de la carrière inspire une vocation liée à la beauté, la nature ou l'art. Tu peux devenir connu pour ton esthétique, ton lien à la terre. Ta réputation se construit autour de valeurs authentiques et de qualité. Les carrières superficielles ne te satisfont plus.

## Ce que tu pourrais vivre
- Une carrière dans l'art, la beauté ou l'écologie
- Une réputation basée sur l'authenticité et la qualité
- Une confusion possible sur la direction professionnelle
- Le besoin de sens et de beauté dans ton travail

## Conseils pour ce transit
- Poursuis une carrière alignée avec tes valeurs profondes
- Construis ta réputation sur la qualité et l'authenticité
- Accepte que le succès prenne des formes non conventionnelles""",

    ('taurus', 11): """# ♆ Transit de Neptune en Taureau — Maison XI

**En une phrase :** Tes cercles sociaux partagent une vision de beauté et d'harmonie avec la nature.

## L'énergie du moment
Neptune en Taureau traverse ta maison des amitiés avec une énergie de communauté terrestre. Tu es attiré par des groupes qui partagent l'amour de la nature, de l'art, de la vie simple. Tes aspirations incluent un monde plus beau et plus en harmonie avec la terre.

## Ce que tu pourrais vivre
- Des amitiés basées sur l'amour de la beauté et de la nature
- L'attrait pour des communautés écologiques ou artistiques
- Des aspirations d'harmonie entre humains et nature
- Une possible idéalisation de certaines amitiés

## Conseils pour ce transit
- Rejoins des communautés qui partagent tes valeurs
- Contribue à créer un monde plus beau
- Reste lucide sur les personnes tout en les appréciant""",

    ('taurus', 12): """# ♆ Transit de Neptune en Taureau — Maison XII

**En une phrase :** Une dissolution profonde te libère des attachements matériels inconscients.

## L'énergie du moment
Neptune en Taureau dans ta maison des profondeurs travaille sur tes attachements inconscients au matériel. Des peurs anciennes liées au manque ou à la survie peuvent être libérées. Tu développes une sécurité intérieure qui ne dépend pas des possessions. La nature devient un chemin de guérison spirituelle.

## Ce que tu pourrais vivre
- La libération de peurs inconscientes liées au manque
- Des rêves impliquant la nature et l'abondance
- Une guérison par la connexion à la terre
- La dissolution d'attachements matériels profonds

## Conseils pour ce transit
- Travaille sur tes peurs inconscientes de manque
- Utilise la nature comme pratique de guérison
- Développe une sécurité intérieure spirituelle""",

    # ============================================================
    # NEPTUNE EN GÉMEAUX (♆ en ♊)
    # ============================================================
    ('gemini', 1): """# ♆ Transit de Neptune en Gémeaux — Maison I

**En une phrase :** Ton identité devient plus fluide et ta présence acquiert une qualité de mercure spirituel.

## L'énergie du moment
Neptune en Gémeaux dans ta maison I rend ton identité plus changeante, plus difficile à définir. Tu peux incarner différentes facettes de toi-même de façon naturelle. Ta communication devient presque magique, tes mots touchent les cœurs. Tu représentes une nouvelle façon de penser et de s'exprimer.

## Ce que tu pourrais vivre
- Une identité plus fluide et adaptable
- Une communication qui semble inspirée ou channelée
- Une possible confusion sur qui tu es vraiment
- Le don de toucher les gens par tes mots

## Conseils pour ce transit
- Accepte la fluidité de ton identité
- Utilise ton don de communication pour inspirer
- Garde un ancrage dans ta vérité profonde""",

    ('gemini', 2): """# ♆ Transit de Neptune en Gémeaux — Maison II

**En une phrase :** Tes revenus peuvent venir de la communication inspirée et tes valeurs deviennent plus intellectuelles.

## L'énergie du moment
Neptune en Gémeaux dans ta maison des ressources lie tes finances à ta capacité de communiquer et transmettre. Tu peux gagner ta vie par les mots, les idées, l'enseignement. Tes valeurs s'orientent vers le savoir et la connexion. Attention aux confusions dans les communications financières.

## Ce que tu pourrais vivre
- Des revenus liés à l'écriture, l'enseignement ou la communication
- Une valorisation du savoir et des idées
- Une possible confusion dans les transactions financières
- Une relation plus détachée au matériel

## Conseils pour ce transit
- Monétise tes talents de communication
- Clarifie toutes les communications financières
- Valorise les richesses intellectuelles autant que matérielles""",

    ('gemini', 3): """# ♆ Transit de Neptune en Gémeaux — Maison III

**En une phrase :** Ta pensée et communication atteignent une dimension presque télépathique.

## L'énergie du moment
Neptune traverse sa maison de communication avec l'énergie versatile des Gémeaux. Tes échanges deviennent plus intuitifs, presque télépathiques. Tu captes les non-dits, communiques entre les lignes. Tes idées ont une qualité poétique et inspirée. Les malentendus sont possibles si tu n'ancres pas dans le concret.

## Ce que tu pourrais vivre
- Une communication intuitive et inspirée
- Des connexions presque télépathiques avec les proches
- Des idées qui semblent venir d'ailleurs
- Des malentendus si le message n'est pas clarifié

## Conseils pour ce transit
- Fais confiance à ton intuition dans les échanges
- Clarifie les communications importantes
- Utilise ton don pour inspirer et connecter""",

    ('gemini', 4): """# ♆ Transit de Neptune en Gémeaux — Maison IV

**En une phrase :** Ton foyer devient un lieu de pensée et d'échange spirituel.

## L'énergie du moment
Neptune en Gémeaux dans ta maison IV transforme ton espace domestique en salon de conversations profondes. La communication devient centrale dans ta vie familiale. Des histoires et mémoires familiales peuvent émerger de façon floue. Ta sécurité vient des connexions intellectuelles et spirituelles.

## Ce que tu pourrais vivre
- Un foyer centré sur les échanges et les idées
- Des mémoires familiales qui émergent de façon diffuse
- Une sécurité trouvée dans la connexion mentale
- Une famille qui communique de façon plus intuitive

## Conseils pour ce transit
- Crée un espace de dialogue ouvert dans ton foyer
- Explore les histoires familiales avec curiosité
- Trouve ta sécurité dans la connexion d'esprit""",

    ('gemini', 5): """# ♆ Transit de Neptune en Gémeaux — Maison V

**En une phrase :** Ta créativité s'exprime par les mots inspirés et tes amours naissent des échanges d'âme.

## L'énergie du moment
Neptune en Gémeaux dans ta maison de la créativité apporte une expression artistique verbale et intellectuelle. L'écriture, la poésie, la chanson peuvent devenir des canaux d'inspiration. En amour, tu es attiré par les connexions mentales profondes, les conversations qui touchent l'âme.

## Ce que tu pourrais vivre
- Une créativité littéraire ou musicale inspirée
- Des amours basées sur la connexion intellectuelle
- Le plaisir des jeux de mots et d'esprit
- Des romances qui commencent par des conversations

## Conseils pour ce transit
- Exprime ta créativité par l'écriture ou les mots
- Recherche des partenaires qui stimulent ton esprit
- Trouve la romance dans le dialogue profond""",

    ('gemini', 6): """# ♆ Transit de Neptune en Gémeaux — Maison VI

**En une phrase :** Ton quotidien s'imprègne de communication spirituelle et ta santé bénéficie du mental calme.

## L'énergie du moment
Neptune en Gémeaux dans ta maison du travail quotidien transforme tes tâches en échanges significatifs. Ton travail peut impliquer la communication inspirée, l'écriture ou l'enseignement. Ta santé est sensible au mental : calmer les pensées devient essentiel pour ton bien-être.

## Ce que tu pourrais vivre
- Un travail centré sur la communication ou les idées
- Une santé liée à l'état de ton mental
- Le besoin de calmer le bavardage intérieur
- Un environnement de travail basé sur l'échange

## Conseils pour ce transit
- Pratique des techniques pour calmer le mental
- Cherche un travail qui permet l'expression
- Sois attentif à la qualité de tes pensées""",

    ('gemini', 7): """# ♆ Transit de Neptune en Gémeaux — Maison VII

**En une phrase :** Tes relations se fondent sur une communication d'âme et les mots deviennent des ponts.

## L'énergie du moment
Neptune en Gémeaux traverse ta maison des partenariats avec une énergie de communication transcendante. Tu attires des partenaires avec qui tu peux avoir des conversations profondes et inspirées. Les mots deviennent le tissu de tes relations. Attention aux malentendus si la communication n'est pas claire.

## Ce que tu pourrais vivre
- Des relations basées sur la connexion intellectuelle
- Des partenaires communiquants et spirituels
- Le risque de malentendus ou d'idéalisation
- Le besoin de dialogue ouvert et profond

## Conseils pour ce transit
- Cultive une communication ouverte et claire
- Recherche des partenaires avec qui échanger en profondeur
- Évite de projeter tes idéaux sur les autres""",

    ('gemini', 8): """# ♆ Transit de Neptune en Gémeaux — Maison VIII

**En une phrase :** Des transformations profondes passent par la communication et la révélation de secrets.

## L'énergie du moment
Neptune en Gémeaux dans ta maison des transformations apporte des changements à travers les mots et les révélations. Des secrets peuvent être partagés, des vérités profondes communiquées. Ta compréhension de la mort et des transformations s'approfondit par l'échange et la réflexion.

## Ce que tu pourrais vivre
- Des révélations transformatrices par la communication
- L'intérêt pour les sujets tabous et les mystères
- Une confusion possible dans les communications sur l'argent partagé
- Des conversations qui changent profondément

## Conseils pour ce transit
- Utilise les mots pour guérir et transformer
- Sois clair dans les discussions sur les ressources partagées
- Explore les mystères par la recherche et le dialogue""",

    ('gemini', 9): """# ♆ Transit de Neptune en Gémeaux — Maison IX

**En une phrase :** Ta quête spirituelle passe par l'exploration de multiples perspectives et traditions.

## L'énergie du moment
Neptune en Gémeaux traverse ta maison des horizons lointains avec une curiosité spirituelle. Tu explores différentes philosophies, langues, traditions sans t'attacher à une seule. Tes voyages peuvent être intellectuels autant que physiques. Tu développes une vision qui intègre la multiplicité.

## Ce que tu pourrais vivre
- L'exploration de multiples chemins spirituels
- Des voyages qui enrichissent ta compréhension du monde
- Une philosophie qui embrasse la diversité
- Le risque de dispersion dans la quête de sens

## Conseils pour ce transit
- Explore largement mais trouve aussi la profondeur
- Voyage pour élargir tes perspectives
- Intègre les différentes sagesses en une vision personnelle""",

    ('gemini', 10): """# ♆ Transit de Neptune en Gémeaux — Maison X

**En une phrase :** Ta carrière s'oriente vers la communication inspirée et l'enseignement spirituel.

## L'énergie du moment
Neptune en Gémeaux dans ta maison de la carrière inspire une vocation liée aux mots et aux idées. Tu peux devenir écrivain, enseignant, communicateur d'idées qui élèvent. Ta réputation se construit autour de ta capacité à inspirer par les mots. Le chemin professionnel peut sembler flou mais guidé.

## Ce que tu pourrais vivre
- Une carrière dans l'écriture, l'enseignement ou la communication
- Une réputation de communicateur inspiré
- Une direction professionnelle qui se clarifie avec le temps
- Le besoin de transmettre quelque chose de significatif

## Conseils pour ce transit
- Poursuis une carrière qui utilise ton don de communication
- Accepte que le chemin soit parfois flou
- Construis ta réputation sur des idées qui comptent""",

    ('gemini', 11): """# ♆ Transit de Neptune en Gémeaux — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des réseaux de communication spirituelle.

## L'énergie du moment
Neptune en Gémeaux traverse ta maison des amitiés avec une énergie de connexion mentale et spirituelle. Tu es attiré par des groupes où les idées sont partagées librement et où la communication élève. Tes aspirations incluent la diffusion d'idées inspirées et la connexion à travers les mots.

## Ce que tu pourrais vivre
- Des amitiés basées sur le partage d'idées
- L'attrait pour des groupes de discussion ou d'étude
- Des aspirations liées à la communication et à l'éducation
- Des connexions qui peuvent être idéalisées

## Conseils pour ce transit
- Rejoins des réseaux qui stimulent ta pensée
- Partage tes idées avec générosité
- Reste lucide sur les personnes au-delà des mots""",

    ('gemini', 12): """# ♆ Transit de Neptune en Gémeaux — Maison XII

**En une phrase :** Une dissolution des pensées anciennes libère ton mental pour une conscience plus élevée.

## L'énergie du moment
Neptune en Gémeaux dans ta maison des profondeurs travaille sur tes patterns mentaux inconscients. Les pensées répétitives et les croyances limitantes peuvent se dissoudre. Tu développes un accès à une pensée plus intuitive et inspirée. Le mental rationnel s'ouvre au mystère.

## Ce que tu pourrais vivre
- La dissolution de patterns de pensée limitants
- Des rêves riches en messages et symboles verbaux
- L'accès à une intuition qui parle en mots et idées
- La libération du bavardage mental incessant

## Conseils pour ce transit
- Pratique le silence mental par la méditation
- Accueille les pensées intuitives qui émergent
- Laisse les vieilles croyances se dissoudre""",

    # ============================================================
    # NEPTUNE EN CANCER (♆ en ♋)
    # ============================================================
    ('cancer', 1): """# ♆ Transit de Neptune en Cancer — Maison I

**En une phrase :** Ton identité se teinte d'une sensibilité profonde et d'une compassion universelle.

## L'énergie du moment
Neptune en Cancer dans ta maison I rend ton identité profondément sensible et empathique. Tu absorbes les émotions autour de toi et peux incarner une présence maternelle et compatissante. Ta présence a un effet apaisant et guérisseur sur les autres. Attention à ne pas te perdre dans les émotions des autres.

## Ce que tu pourrais vivre
- Une sensibilité émotionnelle accrue
- Une présence naturellement apaisante et guérisseuse
- Le risque de confusion émotionnelle avec les autres
- L'incarnation d'une compassion universelle

## Conseils pour ce transit
- Protège ta sensibilité sans te fermer
- Utilise ton empathie pour aider sans te perdre
- Développe des limites émotionnelles saines""",

    ('cancer', 2): """# ♆ Transit de Neptune en Cancer — Maison II

**En une phrase :** Tes valeurs s'orientent vers la sécurité émotionnelle et le soin des autres.

## L'énergie du moment
Neptune en Cancer dans ta maison des ressources lie tes finances au domaine émotionnel et familial. Tu peux gagner ta vie par le soin, la nourriture, l'hébergement. Tes vraies valeurs sont émotionnelles et familiales. Les finances peuvent être floues quand elles concernent la famille.

## Ce que tu pourrais vivre
- Des revenus liés au soin, à la nourriture ou au foyer
- Une valorisation de la sécurité émotionnelle
- Une confusion possible dans les finances familiales
- Une générosité émotionnelle qui peut excéder les moyens

## Conseils pour ce transit
- Reconnais que ta vraie richesse est émotionnelle
- Garde une clarté dans les finances impliquant la famille
- Trouve des façons de valoriser ton don de soin""",

    ('cancer', 3): """# ♆ Transit de Neptune en Cancer — Maison III

**En une phrase :** Ta communication devient plus empathique et tes mots portent une charge émotionnelle.

## L'énergie du moment
Neptune en Cancer dans ta maison de la communication apporte une qualité émotionnelle profonde à tes échanges. Tu communiques avec le cœur, tes mots peuvent émouvoir et guérir. Les malentendus peuvent venir de communications non verbales ou émotionnelles mal comprises.

## Ce que tu pourrais vivre
- Une communication plus empathique et émotionnelle
- Des connexions profondes avec les proches
- Le risque de malentendus émotionnels
- Une pensée influencée par les états d'âme

## Conseils pour ce transit
- Exprime tes émotions clairement
- Vérifie que tu as bien compris les autres
- Utilise ton empathie pour communiquer avec le cœur""",

    ('cancer', 4): """# ♆ Transit de Neptune en Cancer — Maison IV

**En une phrase :** Ton foyer devient un sanctuaire d'amour inconditionnel et de guérison familiale.

## L'énergie du moment
Neptune en Cancer dans sa maison de prédilection crée un espace domestique imprégné de spiritualité et d'amour. Ton foyer peut devenir un lieu de guérison pour toi et les autres. Des mémoires familiales profondes peuvent émerger pour être guéries. Tu cherches un amour familial inconditionnel.

## Ce que tu pourrais vivre
- Un foyer transformé en sanctuaire de guérison
- L'émergence et la guérison de blessures familiales
- Une idéalisation possible de la famille parfaite
- Une connexion profonde aux ancêtres et aux racines

## Conseils pour ce transit
- Crée un espace de paix et d'amour dans ton foyer
- Guéris les blessures familiales avec compassion
- Accepte ta famille réelle, pas idéalisée""",

    ('cancer', 5): """# ♆ Transit de Neptune en Cancer — Maison V

**En une phrase :** Ta créativité s'exprime avec une profondeur émotionnelle touchante et tes amours deviennent des refuges.

## L'énergie du moment
Neptune en Cancer dans ta maison de la créativité apporte une expression artistique profondément émotionnelle. Tu crées des œuvres qui touchent l'âme et évoquent la nostalgie, l'amour, la tendresse. En amour, tu cherches un refuge émotionnel, un partenaire qui est aussi un foyer.

## Ce que tu pourrais vivre
- Une créativité émotionnellement riche et touchante
- Des amours qui offrent sécurité émotionnelle
- Une connexion profonde et intuitive avec les enfants
- Des plaisirs liés à la maison et à l'intimité

## Conseils pour ce transit
- Laisse tes émotions nourrir ta créativité
- Recherche des relations qui te nourrissent émotionnellement
- Crée un espace de jeu et de tendresse""",

    ('cancer', 6): """# ♆ Transit de Neptune en Cancer — Maison VI

**En une phrase :** Ton quotidien devient un acte de soin et ta santé reflète ton état émotionnel.

## L'énergie du moment
Neptune en Cancer dans ta maison du travail quotidien transforme tes tâches en actes de soin et d'amour. Tu es attiré par les métiers qui nourrissent et guérissent. Ta santé est étroitement liée à ton bien-être émotionnel et à ton alimentation.

## Ce que tu pourrais vivre
- Un travail orienté vers le soin et l'alimentation
- Une santé sensible aux émotions et à la nourriture
- Le besoin de créer un environnement de travail nourrissant
- L'importance du bien-être émotionnel au quotidien

## Conseils pour ce transit
- Prends soin de toi comme tu prendrais soin des autres
- Sois attentif à ce que tu manges et à son effet sur toi
- Crée un quotidien qui nourrit ton âme""",

    ('cancer', 7): """# ♆ Transit de Neptune en Cancer — Maison VII

**En une phrase :** Tes relations deviennent des espaces de nourriture émotionnelle et de guérison mutuelle.

## L'énergie du moment
Neptune en Cancer traverse ta maison des partenariats avec une énergie de fusion émotionnelle. Tu attires des partenaires avec qui tu peux créer un cocon d'amour et de sécurité. Les relations peuvent être très nourrissantes ou très absorbantes. Tu cherches l'amour inconditionnel.

## Ce que tu pourrais vivre
- Des relations profondément émotionnelles
- Des partenaires qui deviennent comme une famille
- Le risque de co-dépendance émotionnelle
- La recherche de l'amour maternel dans les relations

## Conseils pour ce transit
- Offre et reçois le soin dans tes relations
- Maintiens ton identité dans l'union
- Recherche la nourriture émotionnelle, pas la dépendance""",

    ('cancer', 8): """# ♆ Transit de Neptune en Cancer — Maison VIII

**En une phrase :** Des transformations profondes guérissent tes blessures émotionnelles les plus anciennes.

## L'énergie du moment
Neptune en Cancer dans ta maison des transformations travaille sur tes blessures émotionnelles les plus profondes. Des mémoires anciennes liées à la mère, au foyer, à la sécurité peuvent remonter pour être guéries. Tu découvres que la vraie sécurité vient de l'amour inconditionnel.

## Ce que tu pourrais vivre
- La guérison de blessures émotionnelles profondes
- Des mémoires d'enfance qui émergent
- La transformation de ta relation à la sécurité
- Des expériences émotionnelles intenses et guérisseuses

## Conseils pour ce transit
- Accueille les émotions qui remontent avec compassion
- Travaille sur tes blessures d'attachement
- Trouve la sécurité dans l'amour qui ne peut être perdu""",

    ('cancer', 9): """# ♆ Transit de Neptune en Cancer — Maison IX

**En une phrase :** Ta spiritualité s'ancre dans l'amour inconditionnel et la compassion universelle.

## L'énergie du moment
Neptune en Cancer traverse ta maison des horizons lointains avec une énergie de compassion universelle. Tu es attiré par des spiritualités qui honorent la Mère Divine, l'amour inconditionnel. Tes voyages peuvent te mener vers des lieux qui nourrissent ton âme. Ta philosophie devient une philosophie du cœur.

## Ce que tu pourrais vivre
- Une spiritualité centrée sur l'amour et la compassion
- L'attrait pour les traditions qui honorent le féminin sacré
- Des voyages vers des lieux de guérison émotionnelle
- Une vision du monde basée sur l'interdépendance

## Conseils pour ce transit
- Développe une spiritualité du cœur
- Voyage vers des lieux qui nourrissent ton âme
- Intègre la compassion dans ta philosophie de vie""",

    ('cancer', 10): """# ♆ Transit de Neptune en Cancer — Maison X

**En une phrase :** Ta carrière s'oriente vers le soin et tu deviens connu pour ta capacité à nourrir.

## L'énergie du moment
Neptune en Cancer dans ta maison de la carrière inspire une vocation de soin et de nourriture. Tu peux devenir reconnu pour ta capacité à créer des espaces sûrs, à prendre soin des autres. Ta réputation se construit autour de ta compassion et de ton instinct maternel, quel que soit ton genre.

## Ce que tu pourrais vivre
- Une carrière dans le soin, l'alimentation ou l'hébergement
- Une réputation de personne nourrissante et protectrice
- Une confusion possible sur la direction professionnelle
- Le besoin de trouver sa famille dans le travail

## Conseils pour ce transit
- Poursuis une carrière qui te permet de prendre soin
- Accepte que ta réputation soit liée à ton cœur
- Crée une ambiance familiale dans ton travail""",

    ('cancer', 11): """# ♆ Transit de Neptune en Cancer — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des familles d'âme et tes aspirations incluent le soin collectif.

## L'énergie du moment
Neptune en Cancer traverse ta maison des amitiés avec une énergie de famille choisie. Tu es attiré par des groupes qui fonctionnent comme des familles aimantes. Tes aspirations incluent le bien-être collectif et la création de communautés nourrissantes.

## Ce que tu pourrais vivre
- Des amitiés qui ressemblent à des liens familiaux
- L'attrait pour des communautés de soin mutuel
- Des aspirations liées au bien-être collectif
- Une possible idéalisation des groupes

## Conseils pour ce transit
- Crée ou rejoins des familles d'âme
- Contribue au bien-être de ta communauté
- Reste lucide sur les dynamiques de groupe""",

    ('cancer', 12): """# ♆ Transit de Neptune en Cancer — Maison XII

**En une phrase :** Une guérison profonde des blessures maternelles et familiales inconscientes.

## L'énergie du moment
Neptune en Cancer dans ta maison des profondeurs travaille sur tes blessures les plus anciennes liées à la mère, au foyer, à l'appartenance. Des mémoires pré-natales ou de la petite enfance peuvent émerger. Tu accèdes à un amour inconditionnel qui guérit les blessures d'attachement.

## Ce que tu pourrais vivre
- La guérison de blessures liées à la mère ou au foyer
- Des rêves impliquant la famille et l'enfance
- L'accès à un amour inconditionnel et universel
- La dissolution de patterns de dépendance émotionnelle

## Conseils pour ce transit
- Accueille les mémoires anciennes avec compassion
- Travaille sur tes blessures d'attachement
- Découvre l'amour inconditionnel en toi-même""",
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
        print(f"✅ Transit Neptune (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
