#!/usr/bin/env python3
"""Insert transit_pluto interpretations for Aries, Taurus, Gemini, Cancer (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_PLUTO_INTERPRETATIONS = {
    # ============================================================
    # PLUTON EN BÉLIER (♇ en ♈)
    # ============================================================
    ('aries', 1): """# ♇ Transit de Pluton en Bélier — Maison I

**En une phrase :** Une transformation totale de ton identité te fait renaître comme un guerrier de lumière.

## L'énergie du moment
Pluton en Bélier dans ta maison I déclenche une métamorphose radicale de qui tu es. Tu traverses une mort et renaissance de ton identité, souvent à travers des épreuves qui détruisent l'ancien toi pour révéler une version plus authentique et puissante. Tu deviens un pionnier de ta propre transformation.

## Ce que tu pourrais vivre
- Une transformation profonde et irréversible de ton identité
- Des crises existentielles qui mènent à la renaissance
- L'émergence d'une force personnelle considérable
- La confrontation avec tes propres ombres

## Conseils pour ce transit
- Accepte la mort de l'ancien toi
- Embrasse ta puissance personnelle avec responsabilité
- Traverse les crises comme des initiations""",

    ('aries', 2): """# ♇ Transit de Pluton en Bélier — Maison II

**En une phrase :** Une transformation profonde de ta relation aux ressources révèle ton vrai pouvoir matériel.

## L'énergie du moment
Pluton en Bélier dans ta maison des ressources bouleverse ta relation à l'argent et aux possessions. Des crises financières peuvent mener à une régénération complète. Tu découvres que ton vrai pouvoir n'est pas dans ce que tu possèdes mais dans ta capacité à te régénérer et à conquérir.

## Ce que tu pourrais vivre
- Des transformations majeures de ta situation financière
- La mort de vieux attachements matériels
- La découverte de ressources intérieures puissantes
- Des crises qui révèlent ton vrai rapport au pouvoir matériel

## Conseils pour ce transit
- Laisse mourir les attachements obsolètes
- Développe ton pouvoir de régénération financière
- Utilise les crises comme occasions de reconstruction""",

    ('aries', 3): """# ♇ Transit de Pluton en Bélier — Maison III

**En une phrase :** Ta pensée et ta communication se transforment pour devenir des outils de pouvoir et de vérité.

## L'énergie du moment
Pluton en Bélier dans ta maison de la communication transforme radicalement ta façon de penser et de t'exprimer. Tes mots gagnent en puissance et en impact. Tu peux percer les illusions et communiquer des vérités qui transforment. Les relations avec les proches peuvent traverser des crises purificatrices.

## Ce que tu pourrais vivre
- Une transformation profonde de ta pensée
- Des communications qui ont le pouvoir de transformer
- Des crises ou ruptures avec des proches
- La découverte de vérités cachées dans l'environnement proche

## Conseils pour ce transit
- Utilise ton pouvoir de parole avec responsabilité
- Accepte que certaines vérités doivent être dites
- Laisse les relations superficielles mourir""",

    ('aries', 4): """# ♇ Transit de Pluton en Bélier — Maison IV

**En une phrase :** Une transformation radicale de tes fondations te fait renaître de tes racines.

## L'énergie du moment
Pluton en Bélier dans ta maison IV bouleverse tes fondations et ta vie familiale. Des secrets familiaux peuvent émerger. Ton lieu de vie peut changer drastiquement. Tu reconstruis tes bases sur une authenticité nouvelle, souvent après la destruction de ce qui semblait stable.

## Ce que tu pourrais vivre
- Des bouleversements majeurs dans la vie familiale
- La révélation de secrets ou patterns familiaux profonds
- Des déménagements ou changements de domicile transformateurs
- La reconstruction de tes fondations sur de nouvelles bases

## Conseils pour ce transit
- Accueille les révélations familiales avec courage
- Reconstruis tes bases sur l'authenticité
- Transforme l'héritage familial en puissance personnelle""",

    ('aries', 5): """# ♇ Transit de Pluton en Bélier — Maison V

**En une phrase :** Ta créativité et tes amours traversent une mort et renaissance intense.

## L'énergie du moment
Pluton en Bélier dans ta maison de la créativité intensifie dramatiquement ton expression créative et ta vie amoureuse. Tu vis des passions dévorantes qui te transforment. Ta créativité puise dans les profondeurs et produit des œuvres puissantes. Les jeux deviennent des enjeux.

## Ce que tu pourrais vivre
- Des amours passionnelles et transformatrices
- Une créativité qui explore le pouvoir et la transformation
- Des crises liées aux enfants ou à la création
- Des plaisirs intenses mais potentiellement obsessionnels

## Conseils pour ce transit
- Canalise l'intensité dans la création
- Évite les relations destructrices
- Transforme-toi à travers ce que tu crées""",

    ('aries', 6): """# ♇ Transit de Pluton en Bélier — Maison VI

**En une phrase :** Ton quotidien et ta santé traversent une purification radicale.

## L'énergie du moment
Pluton en Bélier dans ta maison du travail quotidien transforme profondément tes routines et ta santé. Des crises de santé peuvent mener à une régénération complète. Ton travail quotidien peut changer radicalement. Tu développes un pouvoir de guérison et de transformation du quotidien.

## Ce que tu pourrais vivre
- Des transformations majeures de ton travail ou de tes routines
- Des crises de santé qui mènent à la régénération
- L'élimination de ce qui ne te sert plus au quotidien
- Le développement de capacités de guérison

## Conseils pour ce transit
- Utilise les crises de santé comme opportunités de transformation
- Élimine les routines toxiques
- Développe ton pouvoir de régénération quotidienne""",

    ('aries', 7): """# ♇ Transit de Pluton en Bélier — Maison VII

**En une phrase :** Tes relations traversent des morts et renaissances qui révèlent leur vraie nature.

## L'énergie du moment
Pluton en Bélier dans ta maison des partenariats transforme radicalement tes relations. Des unions peuvent se terminer, d'autres peuvent se régénérer profondément. Tu attires des partenaires puissants ou tu deviens toi-même plus puissant dans les relations. Les jeux de pouvoir sont exposés.

## Ce que tu pourrais vivre
- Des fins ou transformations majeures de relations
- La révélation de dynamiques de pouvoir cachées
- Des partenaires intenses et transformateurs
- La renaissance de relations sur des bases nouvelles

## Conseils pour ce transit
- Accepte que certaines relations doivent mourir
- Travaille sur les jeux de pouvoir en relation
- Reconstruis les partenariats sur l'authenticité""",

    ('aries', 8): """# ♇ Transit de Pluton en Bélier — Maison VIII

**En une phrase :** Des transformations extrêmement profondes touchent les aspects les plus cachés de ta vie.

## L'énergie du moment
Pluton traverse sa maison naturelle avec l'énergie intense du Bélier. C'est une période de transformation maximale touchant la sexualité, les ressources partagées, la mort et la renaissance. Des pouvoirs de régénération exceptionnels sont accessibles. Tu touches le fond pour rebondir plus haut.

## Ce que tu pourrais vivre
- Des transformations profondes et irréversibles
- Des crises financières liées aux ressources partagées
- Des expériences intenses liées à la sexualité ou à la mort
- L'accès à des pouvoirs de régénération considérables

## Conseils pour ce transit
- Embrasse la transformation totale
- Utilise tes pouvoirs de régénération avec sagesse
- Traverse les morts symboliques comme des initiations""",

    ('aries', 9): """# ♇ Transit de Pluton en Bélier — Maison IX

**En une phrase :** Tes croyances et ta vision du monde sont détruites et reconstruites.

## L'énergie du moment
Pluton en Bélier dans ta maison des horizons lointains transforme radicalement tes croyances et ta philosophie. D'anciennes certitudes meurent pour faire place à une compréhension plus profonde. Tes voyages peuvent être transformateurs. Tu peux devenir un pionnier de nouvelles visions du monde.

## Ce que tu pourrais vivre
- L'effondrement de croyances qui te semblaient solides
- Des voyages qui te transforment profondément
- La confrontation avec des vérités qui changent ta vision
- L'émergence d'une philosophie personnelle puissante

## Conseils pour ce transit
- Laisse mourir les croyances obsolètes
- Voyage vers des lieux qui te transforment
- Construis une vision du monde authentique""",

    ('aries', 10): """# ♇ Transit de Pluton en Bélier — Maison X

**En une phrase :** Ta carrière et ta place dans le monde sont radicalement transformées.

## L'énergie du moment
Pluton en Bélier dans ta maison de la carrière déclenche une transformation majeure de ta trajectoire professionnelle. Des positions de pouvoir peuvent être atteintes ou perdues. Tu reconstruis ta réputation sur des bases plus authentiques. Tu deviens un agent de changement dans ton domaine.

## Ce que tu pourrais vivre
- Des changements radicaux de carrière ou de statut
- L'accès à des positions de pouvoir ou leur perte
- La reconstruction de ta réputation
- La transformation de ton rôle dans le monde

## Conseils pour ce transit
- Utilise le pouvoir professionnel avec éthique
- Accepte que ta place dans le monde doive changer
- Deviens un pionnier de transformation dans ton domaine""",

    ('aries', 11): """# ♇ Transit de Pluton en Bélier — Maison XI

**En une phrase :** Tes cercles sociaux et tes aspirations sont profondément transformés.

## L'énergie du moment
Pluton en Bélier dans ta maison des amitiés transforme radicalement tes cercles sociaux et tes idéaux. Des amitiés peuvent se terminer dramatiquement tandis que d'autres s'intensifient. Tes aspirations changent pour refléter une vision plus authentique et puissante de l'avenir.

## Ce que tu pourrais vivre
- Des ruptures ou transformations dans les amitiés
- L'attrait pour des groupes de transformation ou de pouvoir
- La mort d'anciens rêves et la naissance de nouveaux
- Des luttes de pouvoir dans les cercles sociaux

## Conseils pour ce transit
- Laisse partir les amitiés qui ne servent plus ta croissance
- Engage-toi dans des causes qui transforment vraiment
- Redéfinis tes aspirations avec authenticité""",

    ('aries', 12): """# ♇ Transit de Pluton en Bélier — Maison XII

**En une phrase :** Une transformation profonde de ton inconscient libère d'anciens karmas et révèle ta vraie puissance.

## L'énergie du moment
Pluton en Bélier dans ta maison des profondeurs travaille sur les couches les plus anciennes de ton psychisme. Des contenus inconscients puissants remontent. D'anciens karmas peuvent être purgés. Tu accèdes à des ressources intérieures dont tu ignorais l'existence.

## Ce que tu pourrais vivre
- La remontée de contenus inconscients puissants
- La libération de karmas et patterns très anciens
- Des rêves intenses révélant des vérités profondes
- L'accès à des pouvoirs intérieurs cachés

## Conseils pour ce transit
- Travaille sur ce qui remonte avec courage
- Utilise cette période pour une purification profonde
- Découvre ta vraie puissance intérieure""",

    # ============================================================
    # PLUTON EN TAUREAU (♇ en ♉)
    # ============================================================
    ('taurus', 1): """# ♇ Transit de Pluton en Taureau — Maison I

**En une phrase :** Ton identité se transforme à travers une révolution de ta relation au corps et au matériel.

## L'énergie du moment
Pluton en Taureau dans ta maison I transforme profondément ton rapport au corps, aux sens et à la matière. Ton identité passe par une mort et renaissance liée à ce que tu possèdes et à ce que tu incarnes. Tu développes une puissance tranquille mais implacable.

## Ce que tu pourrais vivre
- Une transformation profonde de ton rapport au corps
- Des changements radicaux d'apparence ou de style de vie
- La découverte d'une force intérieure stable et profonde
- La mort d'attachements qui définissaient ton identité

## Conseils pour ce transit
- Transforme ta relation au corps et aux possessions
- Développe une puissance intérieure stable
- Laisse mourir ce qui encombrait ton identité""",

    ('taurus', 2): """# ♇ Transit de Pluton en Taureau — Maison II

**En une phrase :** Une transformation totale de ta relation aux ressources révèle ce qui a vraiment de la valeur.

## L'énergie du moment
Pluton traverse son signe de chute dans ta maison des ressources, créant une tension transformatrice maximale. Tout ce que tu possèdes ou crois posséder peut être remis en question. Des crises financières mènent à une compréhension plus profonde de la vraie valeur et de la vraie sécurité.

## Ce que tu pourrais vivre
- Des bouleversements majeurs de ta situation financière
- La destruction d'attachements matériels profonds
- La découverte de ce qui a vraiment de la valeur
- La reconstruction de ta relation à l'abondance

## Conseils pour ce transit
- Accepte la transformation de ta relation au matériel
- Découvre la sécurité qui ne dépend pas des possessions
- Reconstruis sur des valeurs authentiques""",

    ('taurus', 3): """# ♇ Transit de Pluton en Taureau — Maison III

**En une phrase :** Ta communication devient un outil de transformation concrète et durable.

## L'énergie du moment
Pluton en Taureau dans ta maison de la communication transforme ta façon de penser et d'échanger vers plus de profondeur et de substance. Tes mots acquièrent un poids et une permanence. Les relations proches peuvent être transformées par des vérités nécessaires.

## Ce que tu pourrais vivre
- Une communication plus profonde et substantielle
- Des transformations dans les relations avec les proches
- La fin de conversations superficielles
- L'émergence d'une pensée qui construit durablement

## Conseils pour ce transit
- Parle pour transformer, pas pour bavarder
- Construis des relations de qualité avec tes proches
- Développe une pensée profonde et pratique""",

    ('taurus', 4): """# ♇ Transit de Pluton en Taureau — Maison IV

**En une phrase :** Tes fondations sont détruites et reconstruites sur des bases plus authentiques et durables.

## L'énergie du moment
Pluton en Taureau dans ta maison IV transforme profondément ta relation à la maison, à la famille et aux racines. Des héritages matériels ou émotionnels peuvent être transformés. Tu reconstruis tes fondations sur ce qui est vraiment solide et durable.

## Ce que tu pourrais vivre
- Des transformations majeures du lieu de vie
- La révélation de questions familiales liées à l'argent ou aux possessions
- La reconstruction de fondations plus solides
- La mort d'attachements aux biens familiaux

## Conseils pour ce transit
- Reconstruis tes bases sur l'essentiel
- Transforme l'héritage familial avec sagesse
- Trouve ta vraie sécurité intérieure""",

    ('taurus', 5): """# ♇ Transit de Pluton en Taureau — Maison V

**En une phrase :** Ta créativité et tes amours se transforment vers plus de profondeur sensorielle.

## L'énergie du moment
Pluton en Taureau dans ta maison de la créativité intensifie ton expression artistique et ta vie amoureuse à travers les sens. Tu crées des œuvres qui durent. En amour, tu cherches des connexions profondes et sensuelles qui transforment à travers le corps.

## Ce que tu pourrais vivre
- Une créativité profonde et sensorielle
- Des amours intenses qui passent par le corps
- Des transformations liées aux plaisirs et à la jouissance
- Des œuvres qui ont une substance durable

## Conseils pour ce transit
- Crée des œuvres qui ont de la substance
- Explore les dimensions transformatrices de la sensualité
- Trouve le plaisir dans ce qui est profond et durable""",

    ('taurus', 6): """# ♇ Transit de Pluton en Taureau — Maison VI

**En une phrase :** Ton quotidien et ta santé traversent une transformation vers plus de substance et d'ancrage.

## L'énergie du moment
Pluton en Taureau dans ta maison du travail quotidien transforme profondément tes routines et ta relation au corps. Ta santé peut traverser des crises qui mènent à une régénération par des moyens naturels et concrets. Ton travail acquiert plus de substance et de valeur.

## Ce que tu pourrais vivre
- Une transformation de tes habitudes de santé vers le naturel
- Des changements de travail vers des activités plus substantielles
- La régénération par la connexion au corps et à la nature
- L'élimination de ce qui est superflu dans le quotidien

## Conseils pour ce transit
- Simplifie et approfondie ton quotidien
- Guéris par la connexion au corps et à la nature
- Travaille sur ce qui a une vraie valeur""",

    ('taurus', 7): """# ♇ Transit de Pluton en Taureau — Maison VII

**En une phrase :** Tes relations sont transformées par des questions de valeurs et de ressources partagées.

## L'énergie du moment
Pluton en Taureau dans ta maison des partenariats transforme tes relations autour de questions de valeurs, d'argent et de possessions. Les unions sont testées sur leur capacité à construire ensemble. Des partenariats peuvent se terminer ou se reconstruire sur des bases plus solides.

## Ce que tu pourrais vivre
- Des transformations relationnelles liées à l'argent et aux valeurs
- Des crises qui révèlent ce que vaut vraiment une relation
- Des partenariats qui construisent quelque chose de durable
- La fin de relations basées sur des valeurs superficielles

## Conseils pour ce transit
- Construis des relations sur des valeurs solides
- Clarifie les questions matérielles dans les partenariats
- Laisse partir ce qui n'a pas de substance""",

    ('taurus', 8): """# ♇ Transit de Pluton en Taureau — Maison VIII

**En une phrase :** Des transformations profondes touchent ta relation aux ressources partagées et à la possession.

## L'énergie du moment
Pluton en Taureau dans ta maison des transformations crée des changements majeurs autour de ce que tu partages avec les autres et de tes attachements profonds. Des héritages ou des dettes peuvent transformer ta vie. Tu apprends à lâcher prise sur le matériel pour accéder à une richesse plus profonde.

## Ce que tu pourrais vivre
- Des transformations majeures des ressources partagées
- La mort d'attachements matériels profonds
- Des crises d'héritage ou de propriété
- La découverte d'une richesse qui transcende le matériel

## Conseils pour ce transit
- Laisse mourir les attachements qui t'emprisonnent
- Transforme ta relation au pouvoir matériel
- Découvre la vraie richesse dans le lâcher-prise""",

    ('taurus', 9): """# ♇ Transit de Pluton en Taureau — Maison IX

**En une phrase :** Ta vision du monde se transforme pour intégrer une sagesse pratique et terrestre.

## L'énergie du moment
Pluton en Taureau dans ta maison des horizons lointains transforme tes croyances vers plus de pragmatisme et d'ancrage. Tu es attiré par des philosophies qui ont des applications concrètes. Tes voyages peuvent te transformer en te reconnectant à la terre et à la nature.

## Ce que tu pourrais vivre
- Une transformation de tes croyances vers plus de substance
- Des voyages vers des lieux qui te reconnectent à la terre
- L'attrait pour des sagesses pratiques et ancestrales
- La mort de croyances abstraites ou déconnectées

## Conseils pour ce transit
- Développe une philosophie ancrée dans le réel
- Voyage vers des lieux qui te transforment par la nature
- Construis une vision du monde qui a de la substance""",

    ('taurus', 10): """# ♇ Transit de Pluton en Taureau — Maison X

**En une phrase :** Ta carrière et ta réputation sont transformées pour construire quelque chose de durable.

## L'énergie du moment
Pluton en Taureau dans ta maison de la carrière transforme ta trajectoire professionnelle vers des réalisations plus substantielles et durables. Tu peux acquérir du pouvoir matériel ou le perdre pour le reconstruire sur des bases plus solides. Ta réputation se construit sur ce que tu produis de concret.

## Ce que tu pourrais vivre
- Des transformations de carrière vers plus de substance
- L'acquisition ou la perte de pouvoir matériel
- La construction d'une réputation sur des réalisations concrètes
- Des changements de statut liés à des questions de valeur

## Conseils pour ce transit
- Construis une carrière qui a de la substance
- Utilise le pouvoir matériel avec responsabilité
- Crée quelque chose qui dure""",

    ('taurus', 11): """# ♇ Transit de Pluton en Taureau — Maison XI

**En une phrase :** Tes cercles sociaux et aspirations se transforment vers des valeurs plus authentiques.

## L'énergie du moment
Pluton en Taureau dans ta maison des amitiés transforme tes cercles sociaux autour de questions de valeurs partagées. Des groupes peuvent être transformés ou quittés. Tes aspirations s'orientent vers des objectifs plus concrets et substantiels.

## Ce que tu pourrais vivre
- Des transformations dans les amitiés liées aux valeurs
- L'attrait pour des groupes qui construisent quelque chose de concret
- Des aspirations plus réalistes et substantielles
- La fin de liens basés sur des valeurs superficielles

## Conseils pour ce transit
- Entoure-toi de personnes aux valeurs solides
- Aspire à des objectifs qui ont de la substance
- Contribue à construire quelque chose de durable collectivement""",

    ('taurus', 12): """# ♇ Transit de Pluton en Taureau — Maison XII

**En une phrase :** Une transformation profonde de tes attachements inconscients te libère vers une vraie sécurité.

## L'énergie du moment
Pluton en Taureau dans ta maison des profondeurs travaille sur tes attachements inconscients au matériel et à la sécurité. Des peurs anciennes liées au manque peuvent être purgées. Tu découvres une sécurité intérieure qui ne dépend pas de ce que tu possèdes.

## Ce que tu pourrais vivre
- La libération de peurs inconscientes liées au manque
- Des rêves révélant des attachements profonds
- La transformation de ta relation inconsciente aux possessions
- La découverte d'une sécurité qui vient de l'intérieur

## Conseils pour ce transit
- Travaille sur tes peurs profondes de manque
- Libère les attachements inconscients
- Découvre la sécurité qui ne peut être perdue""",

    # ============================================================
    # PLUTON EN GÉMEAUX (♇ en ♊)
    # ============================================================
    ('gemini', 1): """# ♇ Transit de Pluton en Gémeaux — Maison I

**En une phrase :** Ton identité se transforme à travers une révolution de ta pensée et de ta communication.

## L'énergie du moment
Pluton en Gémeaux dans ta maison I transforme profondément ton mental et ta façon de te présenter. Tu développes un pouvoir de communication considérable. Ton identité passe par une mort et renaissance liée à ce que tu penses et dis. Tu deviens un agent de transformation par les idées.

## Ce que tu pourrais vivre
- Une transformation profonde de ta façon de penser
- L'émergence d'un pouvoir de communication intense
- Des crises d'identité liées aux idées et aux communications
- La capacité de transformer par les mots

## Conseils pour ce transit
- Utilise ton pouvoir de parole avec responsabilité
- Transforme ta pensée pour transformer ton identité
- Deviens un vecteur d'idées qui changent le monde""",

    ('gemini', 2): """# ♇ Transit de Pluton en Gémeaux — Maison II

**En une phrase :** Tes ressources se transforment à travers l'information et la communication.

## L'énergie du moment
Pluton en Gémeaux dans ta maison des ressources transforme ta relation à l'argent à travers l'information et les idées. Tu peux gagner du pouvoir par la connaissance. Les valeurs liées à l'intellect et à la communication deviennent centrales.

## Ce que tu pourrais vivre
- Des transformations financières liées à l'information
- Le pouvoir gagné par la connaissance et les connexions
- Des changements de valeurs vers l'intellectuel
- La mort d'anciennes façons de gagner sa vie

## Conseils pour ce transit
- Valorise et monétise tes compétences intellectuelles
- Utilise l'information comme source de pouvoir
- Transforme ta relation à la valeur des idées""",

    ('gemini', 3): """# ♇ Transit de Pluton en Gémeaux — Maison III

**En une phrase :** Ta pensée et communication atteignent une profondeur et une puissance transformatrices.

## L'énergie du moment
Pluton traverse sa maison de communication avec l'énergie vive des Gémeaux. Ta pensée devient capable de percer les illusions. Ta communication a le pouvoir de transformer profondément ceux qui t'écoutent. Les relations proches traversent des purifications par la vérité.

## Ce que tu pourrais vivre
- Une pensée d'une profondeur et d'une acuité exceptionnelles
- Des communications qui transforment ceux qui les reçoivent
- Des révélations ou des ruptures avec des proches
- L'apprentissage de vérités qui changent tout

## Conseils pour ce transit
- Utilise ton pouvoir mental pour le bien
- Communique les vérités avec compassion
- Laisse mourir les échanges superficiels""",

    ('gemini', 4): """# ♇ Transit de Pluton en Gémeaux — Maison IV

**En une phrase :** Tes fondations sont transformées par des révélations et une nouvelle compréhension familiale.

## L'énergie du moment
Pluton en Gémeaux dans ta maison IV transforme ta vie familiale et domestique à travers des révélations et de nouvelles façons de communiquer. Des secrets familiaux peuvent être révélés. La façon dont ta famille communique change profondément.

## Ce que tu pourrais vivre
- Des révélations qui transforment ta compréhension familiale
- Une nouvelle façon de communiquer dans la famille
- Des secrets mis en lumière
- Une transformation de ton rapport à ton histoire

## Conseils pour ce transit
- Accueille les vérités familiales avec courage
- Transforme la communication dans ta famille
- Comprends ton histoire pour la transcender""",

    ('gemini', 5): """# ♇ Transit de Pluton en Gémeaux — Maison V

**En une phrase :** Ta créativité et tes amours se transforment par l'intellect et la communication profonde.

## L'énergie du moment
Pluton en Gémeaux dans ta maison de la créativité intensifie ton expression artistique et ta vie amoureuse à travers l'esprit. Tu crées des œuvres qui transforment par les idées. En amour, tu cherches des connexions qui passent par des échanges profonds et transformateurs.

## Ce que tu pourrais vivre
- Une créativité intellectuellement intense
- Des amours qui transforment par la communication
- Des jeux d'esprit qui deviennent des enjeux profonds
- Des créations qui véhiculent des vérités puissantes

## Conseils pour ce transit
- Crée des œuvres qui transforment les esprits
- Cherche des partenaires avec qui échanger en profondeur
- Utilise les mots comme outils de création""",

    ('gemini', 6): """# ♇ Transit de Pluton en Gémeaux — Maison VI

**En une phrase :** Ton quotidien et ta santé sont transformés par une nouvelle façon de penser et communiquer.

## L'énergie du moment
Pluton en Gémeaux dans ta maison du travail quotidien transforme tes routines par l'information et la communication. Ton travail peut impliquer la transmission d'idées puissantes. Ta santé est liée à l'état de ton mental et bénéficie de nouvelles compréhensions.

## Ce que tu pourrais vivre
- Un travail transformé par les nouvelles technologies
- Une santé liée aux patterns de pensée
- Des routines qui intègrent l'apprentissage transformateur
- La guérison par la compréhension et l'information

## Conseils pour ce transit
- Transforme tes pensées pour transformer ta santé
- Travaille dans des domaines qui transmettent des idées puissantes
- Apprends des choses qui changent ton quotidien""",

    ('gemini', 7): """# ♇ Transit de Pluton en Gémeaux — Maison VII

**En une phrase :** Tes relations sont transformées par des communications profondes et des révélations.

## L'énergie du moment
Pluton en Gémeaux dans ta maison des partenariats transforme tes relations par ce qui est dit ou révélé. Des vérités émergent dans les couples. Tu attires des partenaires intellectuellement puissants avec qui les échanges sont transformateurs mais potentiellement manipulateurs.

## Ce que tu pourrais vivre
- Des relations transformées par des vérités révélées
- Des partenaires intellectuellement intenses
- Des jeux de pouvoir à travers la communication
- La fin de relations basées sur des non-dits

## Conseils pour ce transit
- Communique les vérités dans tes relations
- Évite les manipulations par les mots
- Construis des partenariats sur l'échange authentique""",

    ('gemini', 8): """# ♇ Transit de Pluton en Gémeaux — Maison VIII

**En une phrase :** Des transformations profondes passent par l'information et la révélation de secrets.

## L'énergie du moment
Pluton en Gémeaux dans ta maison des transformations apporte des changements puissants à travers l'information et les secrets révélés. Tu peux découvrir des vérités qui transforment complètement ta compréhension. La communication devient un outil de pouvoir profond.

## Ce que tu pourrais vivre
- Des révélations qui transforment profondément
- L'accès à des informations secrètes ou cachées
- La transformation par la compréhension profonde
- Le pouvoir à travers la connaissance des secrets

## Conseils pour ce transit
- Utilise les informations avec éthique
- Transforme-toi par la compréhension profonde
- Respecte les secrets des autres""",

    ('gemini', 9): """# ♇ Transit de Pluton en Gémeaux — Maison IX

**En une phrase :** Ta vision du monde est transformée par de nouvelles idées et compréhensions.

## L'énergie du moment
Pluton en Gémeaux dans ta maison des horizons lointains transforme tes croyances par l'acquisition de nouvelles connaissances. D'anciennes certitudes meurent face à de nouvelles informations. Tu peux devenir un transmetteur d'idées qui changent les visions du monde.

## Ce que tu pourrais vivre
- Une transformation des croyances par les nouvelles informations
- Des voyages qui apportent des idées transformatrices
- L'attrait pour l'enseignement ou l'écriture qui transforme
- La mort de certitudes face à de nouvelles compréhensions

## Conseils pour ce transit
- Reste ouvert aux idées qui transforment ta vision
- Transmets ce que tu apprends de transformateur
- Voyage pour acquérir des connaissances qui changent""",

    ('gemini', 10): """# ♇ Transit de Pluton en Gémeaux — Maison X

**En une phrase :** Ta carrière et ta réputation sont transformées par ta capacité à communiquer et informer.

## L'énergie du moment
Pluton en Gémeaux dans ta maison de la carrière transforme ta trajectoire professionnelle par l'information et la communication. Tu peux atteindre le pouvoir par les idées et les mots. Ta réputation se construit sur ta capacité à transmettre des vérités qui comptent.

## Ce que tu pourrais vivre
- Une carrière transformée par la communication
- Le pouvoir acquis par l'information et les idées
- Une réputation basée sur la transmission d'idées
- Des changements de carrière vers les médias ou l'éducation

## Conseils pour ce transit
- Utilise ton pouvoir de communication pour ton ascension
- Construis ta réputation sur des idées de valeur
- Transforme ton domaine par les nouvelles idées""",

    ('gemini', 11): """# ♇ Transit de Pluton en Gémeaux — Maison XI

**En une phrase :** Tes cercles sociaux et aspirations sont transformés par le partage d'idées puissantes.

## L'énergie du moment
Pluton en Gémeaux dans ta maison des amitiés transforme tes cercles sociaux par les idées et l'information. Tu es attiré par des groupes qui partagent des connaissances puissantes. Tes aspirations incluent la transformation du monde par les idées.

## Ce que tu pourrais vivre
- Des amitiés basées sur le partage d'idées transformatrices
- L'attrait pour des réseaux intellectuellement puissants
- Des aspirations liées à la transformation par la connaissance
- Des changements dans les cercles selon les idées partagées

## Conseils pour ce transit
- Rejoins des réseaux qui partagent des idées puissantes
- Contribue à la transformation collective par tes idées
- Aspire à changer le monde par la connaissance""",

    ('gemini', 12): """# ♇ Transit de Pluton en Gémeaux — Maison XII

**En une phrase :** Une transformation profonde de ton inconscient passe par de nouvelles compréhensions.

## L'énergie du moment
Pluton en Gémeaux dans ta maison des profondeurs travaille sur tes patterns mentaux inconscients. Des pensées et croyances cachées peuvent être révélées et transformées. Tu accèdes à une compréhension plus profonde de ton propre mental.

## Ce que tu pourrais vivre
- La révélation de patterns de pensée inconscients
- Des rêves riches en messages et informations
- La transformation de croyances inconscientes
- L'accès à des compréhensions profondes cachées

## Conseils pour ce transit
- Explore tes pensées inconscientes avec courage
- Transforme tes croyances limitantes cachées
- Utilise les rêves comme source d'information""",

    # ============================================================
    # PLUTON EN CANCER (♇ en ♋)
    # ============================================================
    ('cancer', 1): """# ♇ Transit de Pluton en Cancer — Maison I

**En une phrase :** Ton identité est profondément transformée à travers des processus émotionnels intenses.

## L'énergie du moment
Pluton en Cancer dans ta maison I transforme radicalement ton identité à travers les émotions et la famille. Tu traverses une mort et renaissance de qui tu es au niveau émotionnel. Tu développes une puissance qui vient de la profondeur de tes sentiments et de ta capacité à nourrir.

## Ce que tu pourrais vivre
- Une transformation profonde de ton identité émotionnelle
- Des crises qui passent par les sentiments profonds
- L'émergence d'une force liée à ta capacité de soin
- La mort d'anciennes façons de te protéger émotionnellement

## Conseils pour ce transit
- Traverse les émotions intenses comme des initiations
- Développe ta puissance à travers la vulnérabilité
- Transforme ta relation à la famille et aux émotions""",

    ('cancer', 2): """# ♇ Transit de Pluton en Cancer — Maison II

**En une phrase :** Ta relation aux ressources est transformée par des besoins émotionnels profonds.

## L'énergie du moment
Pluton en Cancer dans ta maison des ressources transforme ta relation à l'argent à travers le prisme émotionnel et familial. Des questions d'héritage ou de ressources familiales peuvent être au centre. Tu découvres que ta vraie sécurité est émotionnelle.

## Ce que tu pourrais vivre
- Des transformations financières liées à la famille
- La découverte de la sécurité émotionnelle comme vraie richesse
- Des crises autour des héritages ou biens familiaux
- La mort d'attachements matériels émotionnellement chargés

## Conseils pour ce transit
- Transforme ta relation émotionnelle à l'argent
- Travaille sur les questions financières familiales
- Trouve ta sécurité dans l'amour, pas dans les possessions""",

    ('cancer', 3): """# ♇ Transit de Pluton en Cancer — Maison III

**En une phrase :** Ta communication se transforme pour exprimer des vérités émotionnelles profondes.

## L'énergie du moment
Pluton en Cancer dans ta maison de la communication transforme ta façon de t'exprimer vers plus de profondeur émotionnelle. Tu communiques des vérités qui touchent le cœur. Les relations avec les proches peuvent traverser des transformations émotionnelles intenses.

## Ce que tu pourrais vivre
- Une communication plus émotionnellement chargée
- Des transformations dans les relations fraternelles ou proches
- L'expression de vérités émotionnelles longtemps cachées
- Des échanges qui touchent et transforment émotionnellement

## Conseils pour ce transit
- Exprime tes émotions profondes avec authenticité
- Laisse les relations superficielles se transformer ou mourir
- Communique du cœur""",

    ('cancer', 4): """# ♇ Transit de Pluton en Cancer — Maison IV

**En une phrase :** Une transformation totale de tes fondations familiales et émotionnelles.

## L'énergie du moment
Pluton traverse son signe d'exaltation dans ta maison des racines, créant une transformation maximale de ta vie familiale et émotionnelle. Des secrets familiaux profonds peuvent être révélés. Ta relation à la maison, à la mère, aux ancêtres est complètement transformée.

## Ce que tu pourrais vivre
- Des révélations profondes sur l'histoire familiale
- La transformation radicale de ton lieu de vie
- La guérison de blessures familiales ancestrales
- La mort et renaissance de ta conception de la famille

## Conseils pour ce transit
- Accueille les révélations familiales comme des libérations
- Transforme ton héritage familial en puissance
- Reconstruis tes fondations sur l'amour authentique""",

    ('cancer', 5): """# ♇ Transit de Pluton en Cancer — Maison V

**En une phrase :** Ta créativité et tes amours sont transformées par des émotions intenses et profondes.

## L'énergie du moment
Pluton en Cancer dans ta maison de la créativité intensifie ton expression artistique et ta vie amoureuse à travers le prisme émotionnel. Tu crées des œuvres qui touchent l'âme. En amour, tu vis des passions qui transforment par leur intensité émotionnelle.

## Ce que tu pourrais vivre
- Une créativité profondément émotionnelle
- Des amours qui transforment par leur intensité
- Des relations intenses avec les enfants
- Des plaisirs qui passent par le cœur

## Conseils pour ce transit
- Crée à partir de tes émotions les plus profondes
- Aime avec tout ton cœur malgré les risques
- Transforme-toi à travers ce que tu aimes""",

    ('cancer', 6): """# ♇ Transit de Pluton en Cancer — Maison VI

**En une phrase :** Ton quotidien et ta santé sont transformés par le soin et la guérison émotionnelle.

## L'énergie du moment
Pluton en Cancer dans ta maison du travail quotidien transforme tes routines à travers le soin et les émotions. Ton travail peut devenir une forme de guérison. Ta santé est profondément liée à ton bien-être émotionnel et familial.

## Ce que tu pourrais vivre
- Un travail transformé en service de guérison
- Une santé liée au traitement des émotions
- Des routines qui intègrent le soin de soi et des autres
- La transformation du quotidien par l'amour

## Conseils pour ce transit
- Fais de ton travail un acte de soin
- Guéris ton corps par l'attention aux émotions
- Transforme ton quotidien en espace de nourriture""",

    ('cancer', 7): """# ♇ Transit de Pluton en Cancer — Maison VII

**En une phrase :** Tes relations sont transformées par des processus émotionnels profonds et des questions de soin.

## L'énergie du moment
Pluton en Cancer dans ta maison des partenariats transforme tes relations par des émotions intenses et des questions de nourriture mutuelle. Tu attires des partenaires qui te transforment émotionnellement. Les dynamiques de dépendance et de soin sont révélées et transformées.

## Ce que tu pourrais vivre
- Des relations qui transforment par leur intensité émotionnelle
- La révélation de dynamiques de co-dépendance
- Des partenaires qui réveillent des blessures d'enfance
- La transformation des patterns relationnels familiaux

## Conseils pour ce transit
- Travaille sur tes besoins émotionnels dans les relations
- Évite les dynamiques de dépendance destructrices
- Transforme les blessures d'enfance à travers les relations""",

    ('cancer', 8): """# ♇ Transit de Pluton en Cancer — Maison VIII

**En une phrase :** Des transformations profondes guérissent les blessures émotionnelles les plus anciennes.

## L'énergie du moment
Pluton en Cancer dans ta maison des transformations travaille sur tes blessures émotionnelles les plus profondes. Des mémoires d'enfance ou familiales peuvent remonter pour être guéries. Tu accèdes à une puissance de guérison émotionnelle considérable.

## Ce que tu pourrais vivre
- La guérison de blessures émotionnelles profondes
- Des mémoires d'enfance qui remontent pour être transformées
- La mort de patterns émotionnels hérités
- L'accès à une puissance de régénération émotionnelle

## Conseils pour ce transit
- Accueille les émotions qui remontent avec compassion
- Travaille sur les blessures d'attachement
- Utilise ta puissance de guérison pour toi et les autres""",

    ('cancer', 9): """# ♇ Transit de Pluton en Cancer — Maison IX

**En une phrase :** Ta vision du monde est transformée par une compréhension émotionnelle et intuitive profonde.

## L'énergie du moment
Pluton en Cancer dans ta maison des horizons lointains transforme tes croyances par les émotions et l'intuition. Tu développes une philosophie qui honore les sentiments et la sagesse du cœur. Tes voyages peuvent te reconnecter à tes racines profondes.

## Ce que tu pourrais vivre
- Une transformation des croyances par le cœur
- Des voyages vers des lieux d'origine ou émotionnellement significatifs
- Une philosophie qui intègre le féminin et l'émotionnel
- La mort de croyances qui nient les sentiments

## Conseils pour ce transit
- Développe une sagesse du cœur
- Voyage vers ce qui te touche profondément
- Construis une vision qui honore les émotions""",

    ('cancer', 10): """# ♇ Transit de Pluton en Cancer — Maison X

**En une phrase :** Ta carrière est transformée vers des rôles de soin et de protection.

## L'énergie du moment
Pluton en Cancer dans ta maison de la carrière transforme ta trajectoire vers des rôles de nourriture et de protection. Tu peux atteindre le pouvoir par ta capacité à prendre soin. Ta réputation se construit sur ton aptitude à créer des espaces sûrs.

## Ce que tu pourrais vivre
- Une carrière transformée vers le soin et la protection
- Le pouvoir acquis par la capacité à nourrir
- Une réputation maternelle ou protectrice
- Des changements de carrière vers la famille ou le foyer

## Conseils pour ce transit
- Développe ta carrière autour de ta capacité de soin
- Utilise ton pouvoir pour protéger et nourrir
- Crée des espaces sûrs dans ton travail""",

    ('cancer', 11): """# ♇ Transit de Pluton en Cancer — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des familles transformatrices.

## L'énergie du moment
Pluton en Cancer dans ta maison des amitiés transforme tes cercles sociaux en liens quasi-familiaux. Tu es attiré par des groupes qui fonctionnent comme des familles de choix. Tes aspirations incluent la création de communautés nourrissantes.

## Ce que tu pourrais vivre
- Des amitiés qui deviennent comme des liens familiaux
- L'attrait pour des communautés de soutien mutuel
- Des aspirations liées à la protection du collectif
- Des transformations dans les groupes autour des émotions

## Conseils pour ce transit
- Crée ou rejoins des familles d'âme
- Contribue au bien-être émotionnel collectif
- Transforme tes cercles en espaces de soutien""",

    ('cancer', 12): """# ♇ Transit de Pluton en Cancer — Maison XII

**En une phrase :** Une transformation profonde guérit les blessures maternelles et ancestrales inconscientes.

## L'énergie du moment
Pluton en Cancer dans ta maison des profondeurs travaille sur les blessures les plus anciennes liées à la mère, au foyer et à l'attachement. Des mémoires pré-natales ou transgénérationnelles peuvent être libérées. Tu accèdes à une guérison profonde des lignées.

## Ce que tu pourrais vivre
- La guérison de blessures maternelles profondes
- La libération de patterns transgénérationnels
- Des rêves liés à la mère et aux ancêtres
- L'accès à la guérison des lignées familiales

## Conseils pour ce transit
- Travaille sur tes blessures d'attachement avec compassion
- Libère les patterns hérités des lignées
- Guéris pour toi et pour tes ancêtres""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in TRANSIT_PLUTO_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_pluto',
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
                subject='transit_pluto',
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
        print(f"✅ Transit Pluto (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
