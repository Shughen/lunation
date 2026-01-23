#!/usr/bin/env python3
"""Insert transit_uranus interpretations for Aries, Taurus, Gemini, Cancer (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_URANUS_INTERPRETATIONS = {
    # ============================================================
    # URANUS EN BÉLIER (♅ en ♈)
    # ============================================================
    ('aries', 1): """# ♅ Transit d'Uranus en Bélier — Maison I

**En une phrase :** Une révolution identitaire qui te pousse à devenir radicalement toi-même.

## L'énergie du moment
Uranus en Bélier dans ta maison I déclenche une transformation profonde de ton identité. Tu ressens un besoin urgent d'authenticité, de te libérer des masques que tu portes depuis trop longtemps. Cette énergie électrique te rend imprévisible, même à tes propres yeux. Tu pourrais changer radicalement d'apparence, d'attitude ou de direction de vie sans prévenir. C'est le temps de la réinvention totale.

## Ce que tu pourrais vivre
- Des changements soudains dans ton apparence ou ton style personnel
- Une affirmation de soi plus directe, parfois provocatrice
- Le besoin de casser les moules qui ne te correspondent plus
- Des réveils de conscience sur qui tu es vraiment

## Conseils pour ce transit
- Accueille tes impulsions de changement sans les réprimer
- Expérimente de nouvelles façons d'être toi-même
- Ne crains pas de surprendre ton entourage par tes métamorphoses""",

    ('aries', 2): """# ♅ Transit d'Uranus en Bélier — Maison II

**En une phrase :** Tes valeurs et tes finances connaissent des fluctuations imprévisibles qui te libèrent des anciennes dépendances matérielles.

## L'énergie du moment
Uranus en Bélier secoue ta maison des ressources avec une énergie pionnière et imprévisible. Tes revenus peuvent fluctuer de manière inattendue, mais cette instabilité t'apprend à développer de nouvelles sources de richesse, souvent originales. Tu remets en question ce que tu considérais comme précieux et découvres de nouvelles valeurs plus authentiques.

## Ce que tu pourrais vivre
- Des changements soudains dans ta situation financière
- L'envie de gagner ta vie différemment, de façon plus indépendante
- Une remise en question de tes attachements matériels
- Des opportunités inattendues de revenus alternatifs

## Conseils pour ce transit
- Diversifie tes sources de revenus pour plus de stabilité
- Explore des façons innovantes de valoriser tes talents
- Développe ton indépendance financière progressivement""",

    ('aries', 3): """# ♅ Transit d'Uranus en Bélier — Maison III

**En une phrase :** Ta façon de penser et communiquer se révolutionne avec des idées audacieuses.

## L'énergie du moment
Uranus électrifie ta maison de la communication avec l'énergie directe du Bélier. Ton mental s'accélère, tes idées deviennent plus originales, parfois provocatrices. Tu pourrais surprendre par des opinions tranchées ou des façons de t'exprimer inhabituelles. Tes relations avec tes proches (frères, sœurs, voisins) connaissent des rebondissements.

## Ce que tu pourrais vivre
- Des révélations soudaines qui changent ta perception
- Une communication plus directe, parfois électrique
- Des tensions ou réconciliations inattendues avec tes proches
- L'attrait pour des sujets avant-gardistes ou controversés

## Conseils pour ce transit
- Ose exprimer tes idées originales sans autocensure
- Reste ouvert aux points de vue qui bousculent tes certitudes
- Utilise cette énergie pour apprendre de nouvelles compétences""",

    ('aries', 4): """# ♅ Transit d'Uranus en Bélier — Maison IV

**En une phrase :** Ton foyer et tes racines traversent une révolution qui te libère des conditionnements familiaux.

## L'énergie du moment
Uranus en Bélier dans ta maison IV agite les fondations de ta vie. Ton lieu de vie, ta famille, tes racines sont bousculés par des événements inattendus. Tu pourrais ressentir le besoin de déménager, de changer radicalement ton cadre de vie, ou de te libérer d'héritages familiaux qui t'étouffaient. L'insécurité temporaire mène à une plus grande liberté intérieure.

## Ce que tu pourrais vivre
- Un déménagement ou une rénovation majeure et soudaine
- Des révélations familiales qui changent ta perspective
- Le besoin de t'affranchir des attentes parentales
- Une redéfinition de ce que "maison" signifie pour toi

## Conseils pour ce transit
- Accepte que tes bases aient besoin d'être secouées
- Crée un foyer qui reflète ton authenticité actuelle
- Travaille sur les blessures familiales qui émergent""",

    ('aries', 5): """# ♅ Transit d'Uranus en Bélier — Maison V

**En une phrase :** Ta créativité explose et tes amours prennent des tournures excitantes mais imprévisibles.

## L'énergie du moment
Uranus enflamme ta maison de la créativité avec l'audace du Bélier. Tu ressens un besoin urgent de t'exprimer différemment, de créer quelque chose de nouveau, de prendre des risques artistiques. En amour, tu refuses la routine et recherches l'excitation, les coups de foudre, les connexions électriques. Attention aux liaisons aussi intenses que brèves.

## Ce que tu pourrais vivre
- Une explosion créative avec des projets audacieux
- Des rencontres amoureuses coup de foudre
- Le besoin de plus de liberté dans tes relations romantiques
- Des changements concernant les enfants ou ta parentalité

## Conseils pour ce transit
- Laisse ta créativité s'exprimer sans limites
- Accepte que l'amour puisse être une aventure imprévisible
- Canalise cette énergie dans des projets qui te passionnent""",

    ('aries', 6): """# ♅ Transit d'Uranus en Bélier — Maison VI

**En une phrase :** Ton quotidien et ta santé réclament une révolution vers plus d'autonomie.

## L'énergie du moment
Uranus en Bélier déstabilise ta maison du travail quotidien et de la santé. Tu ne supportes plus la routine, les horaires rigides, les tâches répétitives. Tu pourrais changer radicalement de méthodes de travail ou même de métier. Côté santé, ton corps t'envoie des signaux pour adopter des approches plus naturelles et indépendantes.

## Ce que tu pourrais vivre
- Des changements soudains dans ton emploi ou tes conditions de travail
- Le besoin d'autonomie dans ton organisation quotidienne
- Des symptômes physiques liés au stress de la contrainte
- L'attrait pour des méthodes de santé alternatives

## Conseils pour ce transit
- Réorganise ton quotidien pour plus de liberté
- Écoute les signaux de ton corps sans les ignorer
- Explore des techniques de bien-être non conventionnelles""",

    ('aries', 7): """# ♅ Transit d'Uranus en Bélier — Maison VII

**En une phrase :** Tes relations se transforment radicalement, entre ruptures libératrices et rencontres électriques.

## L'énergie du moment
Uranus traverse ta maison des partenariats avec l'énergie combative du Bélier. Tes relations intimes et professionnelles sont mises à l'épreuve. Tu ne supportes plus les compromis qui t'étouffent et réclames plus d'espace dans tes unions. Des séparations soudaines ou des rencontres inattendues peuvent survenir. L'autre te sert de miroir pour ta propre révolution.

## Ce que tu pourrais vivre
- Des tensions ou séparations dans tes relations établies
- Des rencontres avec des personnes originales et déstabilisantes
- Le besoin de redéfinir les règles de tes partenariats
- Des conflits qui révèlent des vérités importantes

## Conseils pour ce transit
- Communique tes besoins de liberté plutôt que de fuir
- Sois ouvert à de nouvelles formes de relations
- Apprends de chaque partenaire ce qu'ils révèlent de toi""",

    ('aries', 8): """# ♅ Transit d'Uranus en Bélier — Maison VIII

**En une phrase :** Des transformations profondes et soudaines touchent tes ressources partagées et ta vie intime.

## L'énergie du moment
Uranus en Bélier plonge dans tes eaux profondes, bousculant ta maison VIII des transformations. Des héritages, des dettes, des questions de propriété partagée peuvent connaître des rebondissements. Ta sexualité évolue vers plus de liberté et d'expérimentation. Tu traverses des petites morts psychologiques qui te régénèrent puissamment.

## Ce que tu pourrais vivre
- Des changements soudains dans tes finances partagées
- Des révélations sur des secrets longtemps gardés
- Une libération de tabous autour de la sexualité ou de la mort
- Des expériences transformatrices intenses et inattendues

## Conseils pour ce transit
- Accueille les transformations même si elles déstabilisent
- Explore tes profondeurs avec courage et curiosité
- Protège-toi financièrement dans les arrangements partagés""",

    ('aries', 9): """# ♅ Transit d'Uranus en Bélier — Maison IX

**En une phrase :** Tes croyances volent en éclats pour faire place à une vision du monde révolutionnaire.

## L'énergie du moment
Uranus enflamme ta maison de la philosophie et des horizons lointains. Tes certitudes sont ébranlées par des révélations ou des expériences qui élargissent ta conscience. Tu pourrais être attiré par des voyages dans des contrées inconnues, des études originales, ou des philosophies qui remettent tout en question. L'aventure intellectuelle et spirituelle t'appelle.

## Ce que tu pourrais vivre
- Une remise en question de tes croyances fondamentales
- Des voyages qui changent ta perspective sur la vie
- L'attrait pour des enseignements non conventionnels
- Des révélations spirituelles ou philosophiques soudaines

## Conseils pour ce transit
- Reste ouvert aux idées qui bousculent tes certitudes
- Voyage, physiquement ou intellectuellement
- Construis ta propre philosophie plutôt que suivre aveuglément""",

    ('aries', 10): """# ♅ Transit d'Uranus en Bélier — Maison X

**En une phrase :** Ta carrière et ta réputation connaissent des retournements qui t'orientent vers une voie plus authentique.

## L'énergie du moment
Uranus en Bélier électrifie ta maison de la carrière avec une énergie de pionnier. Tu ne veux plus jouer un rôle qui ne te correspond pas dans le monde professionnel. Des changements soudains de direction, des reconversions audacieuses, des prises de position publiques controversées sont possibles. Tu réclames une carrière alignée avec qui tu es vraiment.

## Ce que tu pourrais vivre
- Des changements radicaux dans ta trajectoire professionnelle
- Le besoin de t'affranchir de l'autorité et des conventions
- Une réputation qui se transforme, en bien ou en déstabilisation
- Des opportunités inattendues qui changent ta direction

## Conseils pour ce transit
- Ose prendre des risques dans ta carrière
- Ne reste pas dans une voie qui ne te correspond plus
- Construis ta propre définition du succès""",

    ('aries', 11): """# ♅ Transit d'Uranus en Bélier — Maison XI

**En une phrase :** Ton cercle social se révolutionne et tes aspirations prennent une direction inattendue.

## L'énergie du moment
Uranus traverse sa maison naturelle avec l'énergie audacieuse du Bélier. Tes amitiés changent radicalement : certaines se terminent brusquement tandis que de nouvelles connexions avec des personnes originales apparaissent. Tes rêves d'avenir et tes idéaux se transforment. Tu attires des groupes et des causes qui correspondent à ta nouvelle identité.

## Ce que tu pourrais vivre
- Des ruptures ou renouvellements dans tes cercles d'amis
- L'attrait pour des communautés avant-gardistes ou alternatives
- Une redéfinition de tes espoirs et aspirations
- L'engagement dans des causes progressistes ou révolutionnaires

## Conseils pour ce transit
- Laisse partir les amitiés qui ne résonnent plus avec toi
- Rejoins des groupes alignés avec tes nouvelles valeurs
- Ose rêver grand et différemment""",

    ('aries', 12): """# ♅ Transit d'Uranus en Bélier — Maison XII

**En une phrase :** Des prises de conscience soudaines émergent de ton inconscient et libèrent d'anciens schémas.

## L'énergie du moment
Uranus en Bélier pénètre ta maison des profondeurs cachées. Des contenus inconscients remontent à la surface de façon inattendue, parfois à travers des rêves intenses ou des intuitions fulgurantes. D'anciens schémas d'auto-sabotage peuvent être révélés et libérés. Tu vis une révolution intérieure silencieuse mais puissante.

## Ce que tu pourrais vivre
- Des révélations sur tes patterns inconscients
- Des intuitions ou expériences mystiques soudaines
- Le besoin de te retirer pour intégrer les changements
- La libération de peurs ou de blocages anciens

## Conseils pour ce transit
- Accorde de l'attention à tes rêves et intuitions
- Pratique des techniques d'exploration intérieure
- Laisse partir ce qui émerge sans t'y accrocher""",

    # ============================================================
    # URANUS EN TAUREAU (♅ en ♉)
    # ============================================================
    ('taurus', 1): """# ♅ Transit d'Uranus en Taureau — Maison I

**En une phrase :** Ta façon de te présenter au monde évolue vers plus d'authenticité matérielle et sensorielle.

## L'énergie du moment
Uranus en Taureau dans ta maison I apporte des changements progressifs mais profonds à ton identité. Tu redéfinis ta relation au corps, au confort, à la beauté. Ton apparence peut changer de façon inattendue, reflétant une nouvelle connexion à tes sens et à la nature. Tu apprends à incarner le changement plutôt qu'à le combattre.

## Ce que tu pourrais vivre
- Une transformation de ton rapport au corps et à l'apparence
- Le besoin de te libérer des possessions qui t'encombrent
- Une nouvelle appréciation de la simplicité et de l'authenticité
- Des changements dans ta façon d'aborder le monde matériel

## Conseils pour ce transit
- Reconnecte-toi à tes sens et à la nature
- Simplifie ta vie matérielle pour plus de liberté
- Accepte que ton identité puisse évoluer lentement mais sûrement""",

    ('taurus', 2): """# ♅ Transit d'Uranus en Taureau — Maison II

**En une phrase :** Tes finances et valeurs subissent une révolution qui transforme ta relation à l'abondance.

## L'énergie du moment
Uranus traverse son domicile d'exil dans ta maison des ressources, créant une tension créatrice. Tes revenus peuvent fluctuer de façon inhabituelle, mais tu développes une nouvelle intelligence financière. Tu remets en question ce que tu possèdes et ce qui te possède. De nouvelles formes de richesse et de valeur émergent dans ta vie.

## Ce que tu pourrais vivre
- Des hauts et des bas financiers inattendus
- L'attrait pour des investissements ou revenus non conventionnels
- Une redéfinition profonde de ce qui a de la valeur pour toi
- La libération d'attachements matériels qui t'alourdissaient

## Conseils pour ce transit
- Diversifie tes sources de revenus
- Explore les nouvelles économies et technologies financières
- Distingue tes vrais besoins de tes habitudes de consommation""",

    ('taurus', 3): """# ♅ Transit d'Uranus en Taureau — Maison III

**En une phrase :** Ta communication devient plus concrète et tes idées s'ancrent dans le réel de façon innovante.

## L'énergie du moment
Uranus en Taureau dans ta maison de la communication apporte une révolution dans ta façon de penser et d'échanger. Tes idées deviennent plus pratiques, orientées vers des solutions concrètes. Tes relations avec tes proches évoluent, parfois avec des tensions autour de questions matérielles. Tu développes une pensée originale mais ancrée.

## Ce que tu pourrais vivre
- Des idées innovantes avec des applications pratiques
- Des changements dans tes habitudes de déplacement
- Des révisions de tes relations avec frères, sœurs, voisins
- L'apprentissage de nouvelles compétences manuelles ou techniques

## Conseils pour ce transit
- Traduis tes idées en projets concrets
- Reste ouvert aux nouvelles technologies de communication
- Cultive des échanges authentiques et directs""",

    ('taurus', 4): """# ♅ Transit d'Uranus en Taureau — Maison IV

**En une phrase :** Ton foyer et tes racines se transforment pour créer une base plus authentique et durable.

## L'énergie du moment
Uranus en Taureau agite tes fondations avec une énergie qui cherche à construire du nouveau sur de l'ancien. Ton lieu de vie peut changer, ou tu peux le rénover profondément. Des révélations familiales liées aux questions matérielles ou territoriales sont possibles. Tu redéfinis ce qui constitue ta vraie sécurité.

## Ce que tu pourrais vivre
- Des changements majeurs dans ton habitat ou sa localisation
- Des questions d'héritage ou de propriété familiale
- Une nouvelle conception de ce qui te sécurise vraiment
- L'envie de créer un foyer plus écologique ou autonome

## Conseils pour ce transit
- Crée un espace de vie qui reflète tes vraies valeurs
- Travaille sur tes attachements aux biens familiaux
- Développe une sécurité intérieure indépendante du lieu""",

    ('taurus', 5): """# ♅ Transit d'Uranus en Taureau — Maison V

**En une phrase :** Ta créativité prend forme concrètement et tes plaisirs se réinventent de façon plus authentique.

## L'énergie du moment
Uranus en Taureau éveille ta maison de la créativité avec une énergie qui veut incarner l'originalité. Tu es attiré par des formes d'expression artistique qui engagent les sens et le corps. En amour, tu recherches des connexions authentiques, sensuelles, ancrées dans le réel. Les jeux et plaisirs se réinventent vers plus de simplicité.

## Ce que tu pourrais vivre
- Une créativité qui s'exprime à travers des médiums concrets
- Des amours qui déstabilisent tes habitudes de confort
- Une nouvelle approche des plaisirs plus naturelle et sensorielle
- Des changements concernant les enfants ou la parentalité

## Conseils pour ce transit
- Exprime ta créativité avec tes mains et ton corps
- Recherche l'authenticité plutôt que le superficiel en amour
- Redécouvre les plaisirs simples et sensuels""",

    ('taurus', 6): """# ♅ Transit d'Uranus en Taureau — Maison VI

**En une phrase :** Ton quotidien et ta santé évoluent vers des approches plus naturelles et durables.

## L'énergie du moment
Uranus en Taureau révolutionne ta maison du travail quotidien et de la santé. Tu aspires à une routine qui respecte ton corps et la nature. Ton environnement de travail peut changer, avec une orientation vers des activités plus concrètes ou écologiques. Ta santé réclame une approche plus naturelle et respectueuse de tes rythmes.

## Ce que tu pourrais vivre
- Des changements dans ton travail vers plus d'autonomie
- L'attrait pour des méthodes de santé naturelles
- Une réorganisation de ton quotidien plus alignée avec tes besoins
- Des prises de conscience sur ton rapport au corps et à l'alimentation

## Conseils pour ce transit
- Simplifie ta routine quotidienne
- Explore les approches de santé holistiques
- Crée un environnement de travail plus agréable et naturel""",

    ('taurus', 7): """# ♅ Transit d'Uranus en Taureau — Maison VII

**En une phrase :** Tes relations se transforment autour des questions de valeurs et de ressources partagées.

## L'énergie du moment
Uranus en Taureau traverse ta maison des partenariats, apportant des changements dans tes unions. Les questions matérielles et de valeurs deviennent centrales dans tes relations. Tu pourrais attirer des partenaires originaux ou voir tes relations existantes évoluer vers plus d'authenticité ou de rupture si les valeurs divergent trop.

## Ce que tu pourrais vivre
- Des tensions ou évolutions dans les aspects matériels de tes relations
- Des rencontres avec des personnes aux valeurs différentes
- Le besoin de redéfinir ce que tu partages avec les autres
- Une nouvelle conception du partenariat plus équitable

## Conseils pour ce transit
- Clarifie tes valeurs et ce qui est négociable ou non
- Sois ouvert à de nouvelles formes de partenariat
- Travaille sur les questions d'argent dans tes relations""",

    ('taurus', 8): """# ♅ Transit d'Uranus en Taureau — Maison VIII

**En une phrase :** Des transformations profondes touchent tes ressources partagées et ta relation à la possession.

## L'énergie du moment
Uranus en Taureau plonge dans ta maison des transformations, créant des changements puissants autour de ce que tu partages avec d'autres. Héritages, dettes, investissements communs peuvent connaître des rebondissements. Ta relation à ce qui te possède ou ce que tu possèdes est profondément remise en question. Une libération des attachements est en cours.

## Ce que tu pourrais vivre
- Des changements inattendus dans tes finances partagées
- Des révélations sur des questions d'argent ou de propriété
- Une transformation de ta relation à la possession et au contrôle
- Des expériences qui changent ta vision de ce qui a vraiment de la valeur

## Conseils pour ce transit
- Révise tes arrangements financiers partagés
- Lâche prise sur ce que tu ne contrôles pas
- Explore ta relation psychologique à l'argent et aux possessions""",

    ('taurus', 9): """# ♅ Transit d'Uranus en Taureau — Maison IX

**En une phrase :** Tes croyances s'ancrent dans l'expérience concrète et ta philosophie devient plus pratique.

## L'énergie du moment
Uranus en Taureau traverse ta maison des horizons lointains, transformant tes croyances par l'expérience directe. Tu es moins intéressé par les théories abstraites que par ce qui fonctionne concrètement. Les voyages peuvent t'amener vers des lieux naturels ou agricoles. Ta spiritualité s'ancre dans le corps et la terre.

## Ce que tu pourrais vivre
- Une remise en question de croyances non vérifiées par l'expérience
- L'attrait pour des sagesses anciennes et terriennes
- Des voyages vers des destinations naturelles ou rurales
- Une philosophie de vie plus simple et pragmatique

## Conseils pour ce transit
- Base tes croyances sur ton expérience directe
- Explore des traditions spirituelles liées à la terre
- Voyage pour expérimenter plutôt que pour fuir""",

    ('taurus', 10): """# ♅ Transit d'Uranus en Taureau — Maison X

**En une phrase :** Ta carrière évolue vers des activités plus concrètes, durables et alignées avec tes valeurs.

## L'énergie du moment
Uranus en Taureau révolutionne ta maison de la carrière avec une énergie qui cherche à construire quelque chose de durable. Tu pourrais changer de direction professionnelle vers des domaines plus concrets, écologiques ou liés aux ressources. Ta réputation se transforme autour de tes valeurs et de ce que tu produis réellement.

## Ce que tu pourrais vivre
- Des changements de carrière vers des activités plus tangibles
- L'envie de créer quelque chose de durable et utile
- Une remise en question de ton rapport au succès et à l'argent
- Des opportunités dans des secteurs innovants mais concrets

## Conseils pour ce transit
- Aligne ta carrière avec tes vraies valeurs
- Développe des compétences concrètes et durables
- Construis ta réputation sur ce que tu produis réellement""",

    ('taurus', 11): """# ♅ Transit d'Uranus en Taureau — Maison XI

**En une phrase :** Tes amitiés et aspirations se réorientent vers des valeurs plus authentiques et durables.

## L'énergie du moment
Uranus en Taureau traverse ta maison des amitiés et des idéaux, transformant tes cercles sociaux. Tu es attiré par des personnes qui partagent des valeurs concrètes et un désir de construire quelque chose de durable. Tes rêves d'avenir deviennent plus réalistes mais pas moins ambitieux. Les causes écologiques ou économiques peuvent t'attirer.

## Ce que tu pourrais vivre
- Des changements dans tes cercles d'amis selon les valeurs partagées
- L'attrait pour des communautés focalisées sur la durabilité
- Une redéfinition de tes aspirations vers plus de concret
- L'engagement dans des projets collectifs à impact tangible

## Conseils pour ce transit
- Entoure-toi de personnes aux valeurs alignées
- Définis des objectifs réalistes mais inspirants
- Contribue à des causes qui produisent des résultats concrets""",

    ('taurus', 12): """# ♅ Transit d'Uranus en Taureau — Maison XII

**En une phrase :** Une révolution silencieuse transforme ta relation aux attachements matériels inconscients.

## L'énergie du moment
Uranus en Taureau pénètre ta maison des profondeurs cachées, travaillant sur tes attachements inconscients. Des peurs anciennes liées à la sécurité matérielle peuvent remonter pour être libérées. Tu développes une nouvelle relation au corps et aux sens à travers des pratiques introspectives. Une guérison profonde de tes blessures d'abondance est possible.

## Ce que tu pourrais vivre
- Des prises de conscience sur tes attachements inconscients
- Des libérations de peurs anciennes liées au manque
- Le développement d'une spiritualité incarnée
- Des intuitions concernant les ressources et la valeur

## Conseils pour ce transit
- Explore tes croyances inconscientes sur l'argent et la valeur
- Pratique des techniques corporelles de libération
- Développe une sécurité intérieure indépendante du matériel""",

    # ============================================================
    # URANUS EN GÉMEAUX (♅ en ♊)
    # ============================================================
    ('gemini', 1): """# ♅ Transit d'Uranus en Gémeaux — Maison I

**En une phrase :** Ton identité se réinvente à travers une communication et une pensée révolutionnaires.

## L'énergie du moment
Uranus en Gémeaux dans ta maison I électrifie ton mental et ta façon de te présenter. Tu deviens plus vif, plus curieux, plus imprévisible dans tes expressions. Ton identité se fragmente puis se recompose autour de nouvelles idées et de nouvelles façons de communiquer. Tu pourrais surprendre par ta versatilité et ton originalité intellectuelle.

## Ce que tu pourrais vivre
- Une accélération de ta pensée et de ton expression
- Le besoin de te présenter différemment selon les contextes
- L'attrait pour de nouvelles technologies de communication
- Une identité plus fluide et adaptable

## Conseils pour ce transit
- Explore différentes facettes de ta personnalité
- Apprends de nouvelles façons de communiquer
- Reste ancré malgré la multiplicité de tes intérêts""",

    ('gemini', 2): """# ♅ Transit d'Uranus en Gémeaux — Maison II

**En une phrase :** Tes revenus se diversifient et tes valeurs intellectuelles prennent de l'importance.

## L'énergie du moment
Uranus en Gémeaux secoue ta maison des ressources avec une énergie mentale et communicative. Tes sources de revenus peuvent se multiplier mais aussi fluctuer. Tu valorises davantage les idées, les connaissances, les connexions. La communication et l'information deviennent des ressources précieuses.

## Ce que tu pourrais vivre
- Des revenus provenant de sources multiples et variées
- L'importance croissante du savoir comme richesse
- Des fluctuations financières liées aux communications ou aux idées
- Une remise en question de ce que tu considères comme précieux

## Conseils pour ce transit
- Monétise tes compétences de communication
- Diversifie tes sources de revenus intellectuels
- Reste adaptable face aux changements économiques""",

    ('gemini', 3): """# ♅ Transit d'Uranus en Gémeaux — Maison III

**En une phrase :** Ta communication et ta pensée atteignent de nouveaux sommets d'originalité.

## L'énergie du moment
Uranus traverse sa maison de prédilection avec l'énergie vive des Gémeaux. Ton mental s'électrifie, tes idées fusent, ta communication devient brillante mais parfois erratique. Tu es attiré par les nouvelles technologies, les médias innovants, les façons de penser qui brisent les conventions. Tes relations proches s'animent de discussions passionnantes.

## Ce que tu pourrais vivre
- Une explosion d'idées originales et de connexions inattendues
- L'attrait pour les dernières technologies de l'information
- Des échanges stimulants avec des personnes brillantes
- Une curiosité insatiable pour tout ce qui est nouveau

## Conseils pour ce transit
- Canalise le flux d'idées dans des projets concrets
- Utilise les nouvelles technologies à ton avantage
- Garde du temps pour approfondir au-delà de la surface""",

    ('gemini', 4): """# ♅ Transit d'Uranus en Gémeaux — Maison IV

**En une phrase :** Ton foyer devient un lieu d'échange et de connexion avec le monde extérieur.

## L'énergie du moment
Uranus en Gémeaux dans ta maison IV transforme ton espace domestique en hub de communication. Tu pourrais travailler de chez toi de façon plus connectée, ou ton foyer pourrait devenir un lieu de passage et d'échange. Des nouvelles concernant ta famille peuvent circuler de façon inattendue. Ton sentiment de sécurité se base sur les connexions plutôt que sur les murs.

## Ce que tu pourrais vivre
- Un foyer plus connecté et technologique
- Des nouvelles familiales qui circulent rapidement
- Le besoin de mobilité même dans ta vie domestique
- Une famille qui communique de nouvelles façons

## Conseils pour ce transit
- Crée un espace de vie qui facilite la connexion
- Reste en contact avec ta famille malgré les distances
- Trouve ta sécurité dans l'adaptabilité""",

    ('gemini', 5): """# ♅ Transit d'Uranus en Gémeaux — Maison V

**En une phrase :** Ta créativité s'exprime par les mots et tes amours naissent des échanges intellectuels.

## L'énergie du moment
Uranus en Gémeaux enflamme ta maison de la créativité avec une énergie communicative. Tu es attiré par les formes d'expression qui jouent avec les mots, les idées, les médias. En amour, les connexions intellectuelles priment et tu peux être séduit par l'esprit avant tout. Les jeux et divertissements incluent l'apprentissage et l'échange.

## Ce que tu pourrais vivre
- Une créativité qui s'exprime par l'écriture ou les médias
- Des amours qui naissent des conversations et des idées partagées
- Le besoin de stimulation intellectuelle dans les loisirs
- Des interactions ludiques et légères avec les enfants

## Conseils pour ce transit
- Explore l'écriture créative ou les médias numériques
- Recherche des partenaires qui stimulent ton esprit
- Apprends en jouant et joue en apprenant""",

    ('gemini', 6): """# ♅ Transit d'Uranus en Gémeaux — Maison VI

**En une phrase :** Ton quotidien se digitalise et ta santé bénéficie de l'information.

## L'énergie du moment
Uranus en Gémeaux révolutionne ta maison du travail quotidien. Tes méthodes de travail deviennent plus digitales, plus connectées, plus flexibles. Tu pourrais jongler entre plusieurs tâches ou emplois. Ta santé bénéficie d'un meilleur accès à l'information, mais attention à la surcharge mentale et à l'hyperconnexion.

## Ce que tu pourrais vivre
- Un travail plus flexible et basé sur la communication
- La gestion de multiples projets ou responsabilités
- L'utilisation de la technologie pour ta santé
- Le besoin de déconnexion pour préserver ton équilibre

## Conseils pour ce transit
- Organise ton travail pour maximiser la flexibilité
- Utilise la technologie sans en devenir esclave
- Préserve des moments de calme mental""",

    ('gemini', 7): """# ♅ Transit d'Uranus en Gémeaux — Maison VII

**En une phrase :** Tes relations se tissent autour de la communication et des idées partagées.

## L'énergie du moment
Uranus en Gémeaux traverse ta maison des partenariats, transformant tes relations par la communication. Tu attires des partenaires intellectuellement stimulants mais parfois instables. Tes unions existantes évoluent vers plus d'échange verbal et de liberté de pensée. Les relations peuvent se former ou se défaire via les moyens de communication.

## Ce que tu pourrais vivre
- Des relations basées sur la stimulation intellectuelle
- La rencontre de partenaires via les médias ou réseaux
- Le besoin de communiquer davantage dans tes relations
- Des changements rapides dans tes partenariats

## Conseils pour ce transit
- Communique ouvertement avec tes partenaires
- Recherche des relations qui nourrissent ton esprit
- Accepte que les relations puissent évoluer rapidement""",

    ('gemini', 8): """# ♅ Transit d'Uranus en Gémeaux — Maison VIII

**En une phrase :** Des révélations et informations transforment ta relation aux ressources partagées.

## L'énergie du moment
Uranus en Gémeaux pénètre ta maison des transformations, apportant des changements par l'information. Des secrets peuvent être révélés, des découvertes peuvent transformer ta situation financière partagée. Ta curiosité te pousse à explorer les sujets tabous, la psychologie profonde, les mystères de l'existence.

## Ce que tu pourrais vivre
- Des informations qui changent ta situation financière
- Des révélations sur des sujets cachés ou tabous
- L'intérêt pour la recherche et l'investigation profonde
- Des communications transformatrices sur des sujets intimes

## Conseils pour ce transit
- Reste curieux face aux mystères sans te perdre
- Utilise l'information pour transformer positivement
- Communique sur les sujets difficiles avec ouverture""",

    ('gemini', 9): """# ♅ Transit d'Uranus en Gémeaux — Maison IX

**En une phrase :** Ta vision du monde s'élargit par l'accès à de multiples perspectives et informations.

## L'énergie du moment
Uranus en Gémeaux traverse ta maison des horizons lointains, multipliant tes sources de connaissance. Tu es attiré par des philosophies diverses, des cultures variées, des enseignements qui se croisent. Les voyages deviennent des occasions d'apprendre et de communiquer. Tu développes une vision du monde interconnectée et plurielle.

## Ce que tu pourrais vivre
- L'exploration de multiples systèmes de pensée
- Des voyages qui élargissent tes perspectives
- L'apprentissage de nouvelles langues ou modes de communication
- Une philosophie de vie qui intègre la diversité

## Conseils pour ce transit
- Reste ouvert à toutes les perspectives sans te disperser
- Voyage pour apprendre et communiquer
- Développe une pensée qui intègre la complexité""",

    ('gemini', 10): """# ♅ Transit d'Uranus en Gémeaux — Maison X

**En une phrase :** Ta carrière s'oriente vers la communication et les idées innovantes.

## L'énergie du moment
Uranus en Gémeaux révolutionne ta maison de la carrière avec une énergie intellectuelle. Tu pourrais te diriger vers des métiers de communication, d'écriture, de médias ou de technologie. Ta réputation se construit autour de tes idées et de ta capacité à communiquer. Des changements rapides de direction sont possibles.

## Ce que tu pourrais vivre
- Une carrière liée à la communication ou aux médias
- Des changements de direction professionnelle fréquents
- La reconnaissance pour tes idées originales
- L'utilisation de la technologie dans ton métier

## Conseils pour ce transit
- Développe tes compétences de communication
- Reste adaptable face aux évolutions du marché
- Construis ta réputation sur la qualité de tes idées""",

    ('gemini', 11): """# ♅ Transit d'Uranus en Gémeaux — Maison XI

**En une phrase :** Ton réseau s'étend et tes aspirations s'orientent vers la connexion et l'échange.

## L'énergie du moment
Uranus en Gémeaux traverse ta maison des amitiés et des idéaux avec une énergie de réseau. Tes cercles sociaux s'élargissent, se connectent, se transforment. Tu es attiré par des communautés qui partagent des idées et de l'information. Tes aspirations incluent la création de liens et le partage de connaissances.

## Ce que tu pourrais vivre
- Un réseau social qui s'étend et se diversifie
- Des amitiés basées sur les idées et les intérêts partagés
- L'attrait pour des communautés en ligne ou connectées
- Des aspirations liées à la communication et à l'échange

## Conseils pour ce transit
- Cultive un réseau diversifié et stimulant
- Utilise les réseaux pour partager et apprendre
- Définis des aspirations qui connectent plutôt qu'isolent""",

    ('gemini', 12): """# ♅ Transit d'Uranus en Gémeaux — Maison XII

**En une phrase :** Des pensées inconscientes remontent et transforment ta relation au mental.

## L'énergie du moment
Uranus en Gémeaux pénètre ta maison des profondeurs cachées, éclairant les recoins de ton mental. Des pensées inconscientes, des souvenirs oubliés, des patterns mentaux émergent à la conscience. Tu développes une nouvelle relation à ton esprit, peut-être à travers la méditation ou l'écriture introspective.

## Ce que tu pourrais vivre
- Des prises de conscience sur tes patterns de pensée
- Des rêves riches en informations et symboles
- Le besoin de calmer le mental pour accéder au silence
- Des intuitions qui arrivent sous forme de mots ou d'idées

## Conseils pour ce transit
- Pratique des techniques pour observer tes pensées
- Écris pour accéder à ton inconscient
- Trouve l'équilibre entre le mental actif et le silence""",

    # ============================================================
    # URANUS EN CANCER (♅ en ♋)
    # ============================================================
    ('cancer', 1): """# ♅ Transit d'Uranus en Cancer — Maison I

**En une phrase :** Ton identité se transforme autour de nouvelles façons de vivre l'émotionnel et le familial.

## L'énergie du moment
Uranus en Cancer dans ta maison I révolutionne ta façon de vivre et d'exprimer tes émotions. Tu développes une nouvelle identité qui intègre ta sensibilité de façon originale. Tu pourrais surprendre par des réactions émotionnelles inattendues ou une façon nouvelle de prendre soin des autres. Ton apparence reflète ton évolution émotionnelle.

## Ce que tu pourrais vivre
- Une nouvelle façon de vivre et montrer tes émotions
- Le besoin de te libérer des attentes familiales sur ton identité
- Une sensibilité qui s'exprime de façon plus authentique
- Des changements dans ton apparence liés à ton état émotionnel

## Conseils pour ce transit
- Honore ta sensibilité comme force plutôt que faiblesse
- Libère-toi des rôles familiaux qui ne te correspondent plus
- Exprime tes émotions de façon authentique et créative""",

    ('cancer', 2): """# ♅ Transit d'Uranus en Cancer — Maison II

**En une phrase :** Ta relation à la sécurité matérielle se réinvente autour de valeurs émotionnelles.

## L'énergie du moment
Uranus en Cancer secoue ta maison des ressources, transformant ta conception de la sécurité. Tu réalises que la vraie richesse est dans les liens émotionnels et le sentiment d'appartenance. Tes revenus peuvent fluctuer en lien avec des activités de soin ou domestiques. Tu valorises ce qui nourrit émotionnellement.

## Ce que tu pourrais vivre
- Des changements financiers liés à la famille ou au foyer
- Une nouvelle définition de la sécurité et de l'abondance
- L'importance croissante du bien-être émotionnel comme valeur
- Des revenus possibles dans les métiers du soin ou de la nourriture

## Conseils pour ce transit
- Développe une sécurité intérieure indépendante des finances
- Valorise les ressources émotionnelles autant que matérielles
- Explore des sources de revenus liées au soin et au foyer""",

    ('cancer', 3): """# ♅ Transit d'Uranus en Cancer — Maison III

**En une phrase :** Ta communication devient plus émotionnelle et tes liens proches se transforment.

## L'énergie du moment
Uranus en Cancer dans ta maison de la communication apporte une révolution dans tes échanges. Tu communiques de façon plus émotionnelle, plus intuitive, plus maternante. Tes relations avec tes proches (frères, sœurs, voisins) évoluent autour de questions émotionnelles ou familiales. Tu développes une pensée qui intègre le cœur.

## Ce que tu pourrais vivre
- Une communication plus empathique et émotionnelle
- Des changements dans tes relations fraternelles ou de voisinage
- L'intérêt pour des sujets liés à la famille et aux émotions
- Une façon de penser qui honore l'intuition

## Conseils pour ce transit
- Communique avec ton cœur autant qu'avec ta tête
- Prends soin de tes liens avec tes proches
- Développe ton intuition comme outil de communication""",

    ('cancer', 4): """# ♅ Transit d'Uranus en Cancer — Maison IV

**En une phrase :** Ton foyer et ta famille vivent une révolution qui redéfinit ce que signifie "maison".

## L'énergie du moment
Uranus traverse sa position d'exaltation dans ta maison des racines, créant des changements profonds dans ta vie domestique et familiale. Ton concept de famille peut s'élargir ou se transformer radicalement. Des déménagements ou rénovations importantes sont possibles. Tu crées un nouveau sens du foyer et de l'appartenance.

## Ce que tu pourrais vivre
- Des transformations majeures de ton lieu de vie
- Une redéfinition de ce qui constitue ta famille
- Des révélations concernant tes origines ou tes ancêtres
- Le besoin de créer un foyer non conventionnel

## Conseils pour ce transit
- Accepte que ta conception de la famille puisse évoluer
- Crée un foyer qui nourrit ton âme
- Travaille sur les blessures familiales qui émergent""",

    ('cancer', 5): """# ♅ Transit d'Uranus en Cancer — Maison V

**En une phrase :** Ta créativité s'exprime avec plus d'émotion et tes amours touchent des cordes profondes.

## L'énergie du moment
Uranus en Cancer enflamme ta maison de la créativité avec une énergie émotionnelle. Tu es attiré par des formes d'expression qui touchent le cœur, qui évoquent la nostalgie ou les liens familiaux. En amour, tu recherches une connexion profonde et nourricière, même si elle prend des formes inattendues. Ta relation avec les enfants évolue.

## Ce que tu pourrais vivre
- Une créativité émotionnellement chargée et touchante
- Des amours qui éveillent des émotions profondes
- Des changements dans ta façon de vivre la parentalité
- Le besoin de jouer et créer dans un espace sécurisant

## Conseils pour ce transit
- Laisse tes émotions nourrir ta créativité
- Recherche des relations qui offrent sécurité et excitation
- Honore ton enfant intérieur et ses besoins""",

    ('cancer', 6): """# ♅ Transit d'Uranus en Cancer — Maison VI

**En une phrase :** Ton quotidien se réorganise autour du soin et du bien-être émotionnel.

## L'énergie du moment
Uranus en Cancer révolutionne ta maison du travail quotidien et de la santé. Ton environnement de travail devient plus important pour ton bien-être émotionnel. Tu pourrais être attiré par des métiers du soin ou créer un quotidien plus nourrissant. Ta santé est intimement liée à ton état émotionnel.

## Ce que tu pourrais vivre
- Des changements de travail vers des activités de soin
- Le besoin d'un environnement de travail émotionnellement sain
- Une attention accrue au lien entre émotions et santé
- La création de routines qui nourrissent ton bien-être

## Conseils pour ce transit
- Crée un environnement de travail qui te nourrit
- Prends soin de ta santé émotionnelle au quotidien
- Explore les liens entre alimentation, émotions et santé""",

    ('cancer', 7): """# ♅ Transit d'Uranus en Cancer — Maison VII

**En une phrase :** Tes relations intimes se transforment autour des besoins émotionnels et du soin mutuel.

## L'énergie du moment
Uranus en Cancer traverse ta maison des partenariats, révolutionnant tes relations les plus proches. Tu recherches des partenaires qui offrent sécurité émotionnelle tout en étant originaux. Des changements dans ta façon de vivre l'intimité et le soin dans les relations sont en cours. Tu attires des partenaires qui éveillent tes besoins de connexion profonde.

## Ce que tu pourrais vivre
- Des relations qui transforment ta façon de vivre l'intimité
- Le besoin de sécurité et de liberté dans les partenariats
- Des partenaires qui touchent des cordes émotionnelles profondes
- Une redéfinition de ce que signifie prendre soin l'un de l'autre

## Conseils pour ce transit
- Communique tes besoins émotionnels clairement
- Recherche l'équilibre entre sécurité et liberté
- Apprends de nouvelles façons de nourrir tes relations""",

    ('cancer', 8): """# ♅ Transit d'Uranus en Cancer — Maison VIII

**En une phrase :** Des transformations profondes touchent tes liens émotionnels et tes ressources partagées familiales.

## L'énergie du moment
Uranus en Cancer plonge dans ta maison des transformations, créant des changements émotionnels profonds. Des questions d'héritage familial (matériel et émotionnel) peuvent émerger. Tu traverses des expériences qui transforment ta relation à la vulnérabilité et à l'intimité. Des libérations émotionnelles puissantes sont possibles.

## Ce que tu pourrais vivre
- Des questions d'héritage ou de ressources familiales
- Des transformations profondes de ta vie émotionnelle
- La libération de patterns familiaux transmis
- Des expériences intimes qui changent ta vision de la vulnérabilité

## Conseils pour ce transit
- Accueille les émotions qui remontent pour être libérées
- Travaille sur les héritages émotionnels familiaux
- Accepte la vulnérabilité comme porte vers la transformation""",

    ('cancer', 9): """# ♅ Transit d'Uranus en Cancer — Maison IX

**En une phrase :** Tes croyances évoluent vers une spiritualité plus émotionnelle et intuitive.

## L'énergie du moment
Uranus en Cancer traverse ta maison des horizons lointains, transformant ta philosophie de vie. Tu es attiré par des sagesses qui honorent le féminin, la Terre-Mère, les cycles naturels. Tes voyages peuvent te mener vers des lieux qui résonnent émotionnellement ou ancestralement. Ta spiritualité devient plus intuitive et moins intellectuelle.

## Ce que tu pourrais vivre
- L'attrait pour des spiritualités liées à la nature et aux ancêtres
- Des voyages vers des lieux d'origine ou émotionnellement significatifs
- Une philosophie de vie qui intègre le cœur et l'intuition
- Des révélations spirituelles à travers les émotions

## Conseils pour ce transit
- Honore la sagesse qui vient du cœur
- Explore tes racines à travers les voyages ou la recherche
- Développe une spiritualité qui nourrit ton âme""",

    ('cancer', 10): """# ♅ Transit d'Uranus en Cancer — Maison X

**En une phrase :** Ta carrière s'oriente vers des activités de soin et ta réputation se construit autour de ta capacité à nourrir.

## L'énergie du moment
Uranus en Cancer révolutionne ta maison de la carrière avec une énergie maternante. Tu pourrais te diriger vers des métiers du soin, de l'alimentation, de l'habitat ou de la famille. Ta réputation se transforme autour de ta capacité à prendre soin et à créer des espaces sécurisants. Tu redéfinis ce que signifie réussir.

## Ce que tu pourrais vivre
- Une carrière liée au soin, à la famille ou au foyer
- Une réputation basée sur ta capacité à nourrir les autres
- Des changements professionnels liés à des besoins émotionnels
- La création d'un équilibre travail-famille nouveau

## Conseils pour ce transit
- Intègre tes valeurs familiales dans ta carrière
- Construis une réputation sur ton authenticité émotionnelle
- Crée un travail qui honore tes besoins de sécurité""",

    ('cancer', 11): """# ♅ Transit d'Uranus en Cancer — Maison XI

**En une phrase :** Tes amitiés deviennent comme une famille et tes aspirations incluent le bien-être collectif.

## L'énergie du moment
Uranus en Cancer traverse ta maison des amitiés et des idéaux, créant des liens quasi-familiaux. Ton cercle social devient un clan, une tribu qui partage des valeurs de soin et de protection mutuelle. Tes aspirations incluent la création de communautés nourricières et la protection des plus vulnérables.

## Ce que tu pourrais vivre
- Des amitiés qui ressemblent à des liens familiaux
- L'attrait pour des communautés de soin et de soutien
- Des aspirations liées à la protection des autres
- La création ou l'appartenance à des familles choisies

## Conseils pour ce transit
- Cultive des amitiés qui nourrissent mutuellement
- Engage-toi dans des causes de protection et de soin
- Crée ou rejoins des communautés comme des familles""",

    ('cancer', 12): """# ♅ Transit d'Uranus en Cancer — Maison XII

**En une phrase :** Une guérison profonde de tes blessures familiales et émotionnelles inconscientes.

## L'énergie du moment
Uranus en Cancer pénètre ta maison des profondeurs cachées, travaillant sur tes mémoires émotionnelles les plus anciennes. Des blessures familiales inconscientes peuvent remonter pour être guéries. Tu développes une connexion plus profonde avec tes ancêtres et leurs héritages. Une guérison du lignage féminin ou maternel est possible.

## Ce que tu pourrais vivre
- La remontée de mémoires familiales oubliées
- Des rêves impliquant la famille ou les ancêtres
- La guérison de blessures liées à la mère ou au foyer
- Une connexion intuitive avec le lignage familial

## Conseils pour ce transit
- Accueille les émotions anciennes avec compassion
- Explore l'histoire de ta famille pour comprendre tes patterns
- Pratique des rituels de guérison ancestrale""",
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
        print(f"✅ Transit Uranus (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
