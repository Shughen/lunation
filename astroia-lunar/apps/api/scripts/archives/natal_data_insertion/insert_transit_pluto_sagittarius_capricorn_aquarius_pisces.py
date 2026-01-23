#!/usr/bin/env python3
"""Insert transit_pluto interpretations for Sagittarius, Capricorn, Aquarius, Pisces (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_PLUTO_INTERPRETATIONS = {
    # ============================================================
    # PLUTON EN SAGITTAIRE (♇ en ♐)
    # ============================================================
    ('sagittarius', 1): """# ♇ Transit de Pluton en Sagittaire — Maison I

**En une phrase :** Ton identité est transformée par une quête de vérité et de sens qui brise les limites.

## L'énergie du moment
Pluton en Sagittaire dans ta maison I transforme radicalement ta vision de toi-même et du monde. Tu traverses une mort et renaissance de tes croyances fondamentales. Tu deviens un chercheur passionné de vérité, prêt à tout transformer pour trouver le sens.

## Ce que tu pourrais vivre
- Une transformation profonde de tes croyances sur toi-même
- La mort de visions du monde qui te limitaient
- L'émergence d'une quête de sens puissante
- Des crises existentielles qui élargissent ta vision

## Conseils pour ce transit
- Laisse mourir les croyances qui te limitent
- Embrasse une quête de vérité sans compromis
- Deviens un pionnier de nouvelles visions""",

    ('sagittarius', 2): """# ♇ Transit de Pluton en Sagittaire — Maison II

**En une phrase :** Tes ressources sont transformées par une nouvelle philosophie de l'abondance.

## L'énergie du moment
Pluton en Sagittaire dans ta maison des ressources transforme ta relation à l'argent à travers une vision plus large. Tu peux acquérir des ressources par l'enseignement, les voyages ou la transmission de sagesse. Tes valeurs s'élargissent vers une vision globale.

## Ce que tu pourrais vivre
- Des finances transformées par une vision plus large
- La mort de croyances limitantes sur l'abondance
- Des revenus liés à l'expansion et à l'enseignement
- Une transformation de ce que tu considères comme précieux

## Conseils pour ce transit
- Développe une philosophie d'abondance élargie
- Valorise ce qui élève et inspire
- Transforme tes croyances sur la richesse""",

    ('sagittarius', 3): """# ♇ Transit de Pluton en Sagittaire — Maison III

**En une phrase :** Ta communication devient un véhicule de transformation philosophique puissante.

## L'énergie du moment
Pluton en Sagittaire dans ta maison de la communication transforme ta façon de penser et d'échanger vers une vision plus large et plus profonde. Tes mots ont le pouvoir de transformer les visions du monde. Tu communiques des vérités qui élargissent les consciences.

## Ce que tu pourrais vivre
- Une pensée qui embrasse des visions larges et profondes
- Des communications qui transforment les croyances
- L'intérêt pour la philosophie et les grandes questions
- Des transformations dans les relations par le partage de visions

## Conseils pour ce transit
- Utilise ta parole pour élever et transformer
- Explore les grandes questions avec tes proches
- Communique des visions qui élargissent""",

    ('sagittarius', 4): """# ♇ Transit de Pluton en Sagittaire — Maison IV

**En une phrase :** Tes fondations sont transformées par une vision du monde nouvelle et élargie.

## L'énergie du moment
Pluton en Sagittaire dans ta maison IV transforme ta vie familiale et tes racines autour de questions de croyances et de sens. Des traditions familiales peuvent être transformées ou abandonnées. Tu crées un foyer qui reflète ta nouvelle vision du monde.

## Ce que tu pourrais vivre
- Des transformations familiales liées aux croyances
- La mort de traditions qui ne résonnent plus
- La création d'un foyer ouvert sur le monde
- L'intégration de cultures ou philosophies nouvelles

## Conseils pour ce transit
- Transforme les traditions avec respect mais sans attachement
- Crée un foyer qui reflète ta vision élargie
- Honore tes racines tout en évoluant""",

    ('sagittarius', 5): """# ♇ Transit de Pluton en Sagittaire — Maison V

**En une phrase :** Ta créativité et tes amours sont transformées par une passion pour la vérité et l'aventure.

## L'énergie du moment
Pluton en Sagittaire dans ta maison de la créativité intensifie ton expression autour de la quête de sens. Tu crées des œuvres qui explorent les grandes questions. En amour, tu cherches des aventures qui transforment ta vision du monde.

## Ce que tu pourrais vivre
- Une créativité qui explore le sens et la philosophie
- Des amours passionnées avec des chercheurs de vérité
- Des aventures qui transforment ta vision
- Des plaisirs liés à l'exploration et à la découverte

## Conseils pour ce transit
- Crée des œuvres qui questionnent et élargissent
- Vis des amours comme des aventures de croissance
- Trouve la joie dans la quête de sens""",

    ('sagittarius', 6): """# ♇ Transit de Pluton en Sagittaire — Maison VI

**En une phrase :** Ton quotidien est transformé par une vision plus large du service et du sens.

## L'énergie du moment
Pluton en Sagittaire dans ta maison du travail quotidien transforme tes routines vers un sens plus large. Tu refuses un travail qui n'a pas de sens philosophique. Ta santé bénéficie d'une vision holistique et globale.

## Ce que tu pourrais vivre
- Un travail transformé pour avoir plus de sens
- Des routines qui intègrent la quête spirituelle
- Une santé liée à ta philosophie de vie
- La mort de routines qui n'ont pas de sens

## Conseils pour ce transit
- Donne du sens à ton quotidien
- Intègre ta vision du monde dans ton travail
- Trouve la sagesse dans les petites choses""",

    ('sagittarius', 7): """# ♇ Transit de Pluton en Sagittaire — Maison VII

**En une phrase :** Tes relations sont transformées par le partage de visions et d'aventures.

## L'énergie du moment
Pluton en Sagittaire dans ta maison des partenariats transforme tes relations autour du sens et de la vision partagée. Tu attires des partenaires avec qui tu peux explorer les grandes questions. Les relations sans profondeur philosophique ne te satisfont plus.

## Ce que tu pourrais vivre
- Des relations transformées par des visions partagées
- Des partenaires avec qui explorer le sens de la vie
- La fin de relations superficielles
- Des aventures transformatrices en couple

## Conseils pour ce transit
- Cherche des partenaires qui partagent ta quête
- Grandissez ensemble dans la compréhension
- Transformez vos relations en aventures de sens""",

    ('sagittarius', 8): """# ♇ Transit de Pluton en Sagittaire — Maison VIII

**En une phrase :** Des transformations profondes élargissent ta compréhension des mystères de l'existence.

## L'énergie du moment
Pluton en Sagittaire dans ta maison des transformations apporte une compréhension plus large des cycles de mort et de renaissance. Ta philosophie intègre les mystères les plus profonds. Tu développes une sagesse qui transcende les limites ordinaires.

## Ce que tu pourrais vivre
- Une compréhension élargie des mystères de la vie
- Des transformations qui élargissent ta vision
- L'intégration de sagesses sur la mort et la renaissance
- Des ressources partagées liées à l'expansion

## Conseils pour ce transit
- Explore les mystères avec une vision large
- Développe une philosophie de la transformation
- Partage les ressources avec une vision de croissance""",

    ('sagittarius', 9): """# ♇ Transit de Pluton en Sagittaire — Maison IX

**En une phrase :** Ta vision du monde traverse une transformation totale vers une vérité plus profonde.

## L'énergie du moment
Pluton traverse sa maison de prédilection avec l'énergie expansive du Sagittaire. Tes croyances et ta philosophie sont complètement transformées. Tu deviens un chercheur de vérité passionné qui n'accepte plus les réponses superficielles. Tes voyages te transforment profondément.

## Ce que tu pourrais vivre
- Une transformation radicale de ta vision du monde
- Des voyages qui changent fondamentalement ta vie
- L'émergence d'une philosophie personnelle profonde
- La mort de toutes les croyances superficielles

## Conseils pour ce transit
- Embrasse la transformation de ta vision
- Voyage vers ce qui t'appelle profondément
- Développe une sagesse authentique""",

    ('sagittarius', 10): """# ♇ Transit de Pluton en Sagittaire — Maison X

**En une phrase :** Ta carrière est transformée vers des rôles d'enseignement et de transmission de vérité.

## L'énergie du moment
Pluton en Sagittaire dans ta maison de la carrière transforme ta trajectoire vers des positions où tu peux partager ta vision et ta sagesse. Tu peux devenir enseignant, guide ou influenceur philosophique. Ta réputation se construit sur ta capacité à inspirer et à élargir.

## Ce que tu pourrais vivre
- Une carrière transformée vers l'enseignement ou l'inspiration
- Le pouvoir acquis par la vision et la sagesse
- Une réputation de personne qui élargit les horizons
- Des changements de carrière vers l'international ou la philosophie

## Conseils pour ce transit
- Développe ta carrière autour de ta vision
- Utilise ton influence pour élargir les consciences
- Enseigne ce que tu as appris de tes transformations""",

    ('sagittarius', 11): """# ♇ Transit de Pluton en Sagittaire — Maison XI

**En une phrase :** Tes cercles sociaux sont transformés vers des communautés de chercheurs de vérité.

## L'énergie du moment
Pluton en Sagittaire dans ta maison des amitiés transforme tes cercles sociaux autour de la quête de sens et de vérité. Tu es attiré par des groupes qui explorent les grandes questions. Tes aspirations incluent la transformation collective par l'élargissement des consciences.

## Ce que tu pourrais vivre
- Des amitiés avec des chercheurs et des philosophes
- L'attrait pour des communautés spirituelles ou philosophiques
- Des aspirations d'éveil collectif
- La transformation des groupes autour de visions partagées

## Conseils pour ce transit
- Rejoins des communautés de chercheurs
- Contribue à l'élargissement des consciences
- Aspire à des changements qui ont du sens""",

    ('sagittarius', 12): """# ♇ Transit de Pluton en Sagittaire — Maison XII

**En une phrase :** Une transformation profonde libère des croyances inconscientes qui limitaient ta vision.

## L'énergie du moment
Pluton en Sagittaire dans ta maison des profondeurs travaille sur tes croyances inconscientes qui limitaient ta vision du monde. Des dogmes hérités ou des peurs de l'expansion peuvent être révélés et libérés. Tu accèdes à une sagesse qui transcende les limites.

## Ce que tu pourrais vivre
- La libération de croyances inconscientes limitantes
- Des rêves révélant des vérités profondes
- L'accès à une sagesse universelle
- La transformation de peurs liées à l'expansion

## Conseils pour ce transit
- Libère les croyances qui te limitent
- Explore l'inconscient avec une vision large
- Accède à une sagesse qui transcende""",

    # ============================================================
    # PLUTON EN CAPRICORNE (♇ en ♑)
    # ============================================================
    ('capricorn', 1): """# ♇ Transit de Pluton en Capricorne — Maison I

**En une phrase :** Ton identité est profondément transformée vers une maturité et une autorité authentiques.

## L'énergie du moment
Pluton en Capricorne dans ta maison I transforme radicalement ta façon de te présenter vers plus de maturité et de responsabilité. Tu traverses une mort et renaissance de ton rapport à l'autorité et aux structures. Tu deviens un pilier de transformation des systèmes.

## Ce que tu pourrais vivre
- Une transformation profonde vers plus de maturité
- La mort de relations immatures à l'autorité
- L'émergence d'une responsabilité authentique
- Des crises qui révèlent ta vraie structure intérieure

## Conseils pour ce transit
- Assume ton autorité avec intégrité
- Transforme ta relation aux structures
- Deviens un agent de changement responsable""",

    ('capricorn', 2): """# ♇ Transit de Pluton en Capricorne — Maison II

**En une phrase :** Tes ressources sont transformées par une restructuration profonde et responsable.

## L'énergie du moment
Pluton en Capricorne dans ta maison des ressources transforme ta relation à l'argent vers plus de responsabilité et de durabilité. Tu construis une sécurité financière sur des bases solides après avoir possiblement traversé des destructions. Les valeurs superficielles sont éliminées.

## Ce que tu pourrais vivre
- Des transformations financières vers plus de solidité
- La mort de structures financières non durables
- La construction de ressources sur des bases solides
- Des crises qui révèlent ce qui est vraiment stable

## Conseils pour ce transit
- Construis des finances sur des bases durables
- Transforme ta relation à la sécurité matérielle
- Valorise ce qui résiste à l'épreuve du temps""",

    ('capricorn', 3): """# ♇ Transit de Pluton en Capricorne — Maison III

**En une phrase :** Ta communication gagne en autorité et en pouvoir de restructuration.

## L'énergie du moment
Pluton en Capricorne dans ta maison de la communication transforme ta pensée et ton expression vers plus de structure et d'autorité. Tes mots ont le pouvoir de transformer les systèmes. Tu communiques avec une gravité qui commande le respect.

## Ce que tu pourrais vivre
- Une communication avec autorité et structure
- Le pouvoir de transformer par des mots bien pesés
- Des échanges qui restructurent les relations
- La mort de communications immatures

## Conseils pour ce transit
- Utilise ton autorité communicative avec sagesse
- Transforme les structures par tes mots
- Parle avec maturité et responsabilité""",

    ('capricorn', 4): """# ♇ Transit de Pluton en Capricorne — Maison IV

**En une phrase :** Tes fondations traversent une restructuration totale vers plus d'authenticité.

## L'énergie du moment
Pluton en Capricorne dans ta maison IV transforme profondément tes fondations familiales et domestiques. Des structures familiales peuvent s'effondrer pour être reconstruites. Tu établis de nouvelles bases sur la responsabilité et l'authenticité. Des héritages de pouvoir ou de statut peuvent être transformés.

## Ce que tu pourrais vivre
- Des restructurations majeures de la vie familiale
- La transformation des dynamiques d'autorité familiale
- La reconstruction de fondations plus solides
- Des héritages de pouvoir qui se transforment

## Conseils pour ce transit
- Reconstruis tes bases sur l'authenticité
- Transforme les structures familiales avec respect
- Assume ta responsabilité au sein de la famille""",

    ('capricorn', 5): """# ♇ Transit de Pluton en Capricorne — Maison V

**En une phrase :** Ta créativité et tes amours sont transformées vers plus de profondeur et de maturité.

## L'énergie du moment
Pluton en Capricorne dans ta maison de la créativité transforme ton expression vers plus de maîtrise et de substance. En amour, tu cherches des relations matures qui construisent quelque chose de durable. Les divertissements superficiels ne te satisfont plus.

## Ce que tu pourrais vivre
- Une créativité qui construit quelque chose de durable
- Des amours matures et responsables
- La mort des plaisirs superficiels
- Des créations qui demandent maîtrise et temps

## Conseils pour ce transit
- Crée des œuvres qui durent
- Construis des relations sur des bases solides
- Trouve la joie dans la maîtrise et l'accomplissement""",

    ('capricorn', 6): """# ♇ Transit de Pluton en Capricorne — Maison VI

**En une phrase :** Ton quotidien et ta santé sont restructurés vers plus d'efficacité et de durabilité.

## L'énergie du moment
Pluton en Capricorne dans ta maison du travail quotidien transforme tes routines vers plus de structure et d'efficacité. Ta santé bénéficie de disciplines durables. Ton travail devient plus responsable et structuré.

## Ce que tu pourrais vivre
- Un travail restructuré vers plus d'efficacité
- Des routines de santé disciplinées et durables
- La mort de pratiques qui ne fonctionnent pas
- Le développement de méthodes qui durent

## Conseils pour ce transit
- Structure ton quotidien pour la durabilité
- Construis des habitudes de santé solides
- Travaille de façon responsable et efficace""",

    ('capricorn', 7): """# ♇ Transit de Pluton en Capricorne — Maison VII

**En une phrase :** Tes relations sont transformées vers plus de maturité et de structures durables.

## L'énergie du moment
Pluton en Capricorne dans ta maison des partenariats transforme tes relations vers des engagements plus matures et responsables. Tu attires des partenaires avec qui tu peux construire quelque chose de durable. Les relations légères ne te suffisent plus.

## Ce que tu pourrais vivre
- Des relations qui se formalisent ou se restructurent
- Des partenaires matures et responsables
- La fin de relations sans avenir
- La construction de partenariats durables

## Conseils pour ce transit
- Construis des relations sur des bases solides
- Assume tes responsabilités relationnelles
- Choisis des partenaires avec qui construire""",

    ('capricorn', 8): """# ♇ Transit de Pluton en Capricorne — Maison VIII

**En une phrase :** Des transformations profondes restructurent ta relation au pouvoir et aux ressources partagées.

## L'énergie du moment
Pluton en Capricorne dans ta maison des transformations crée une restructuration profonde de ta relation au pouvoir. Des structures de contrôle peuvent s'effondrer. Tu développes une autorité qui vient de l'intérieur plutôt que de l'extérieur.

## Ce que tu pourrais vivre
- La transformation de structures de pouvoir
- Des restructurations des ressources partagées
- Une autorité intérieure qui se développe
- La mort de formes de contrôle obsolètes

## Conseils pour ce transit
- Transforme ta relation au pouvoir avec sagesse
- Restructure les arrangements partagés équitablement
- Développe une autorité intérieure authentique""",

    ('capricorn', 9): """# ♇ Transit de Pluton en Capricorne — Maison IX

**En une phrase :** Ta vision du monde est transformée vers une sagesse structurée et pragmatique.

## L'énergie du moment
Pluton en Capricorne dans ta maison des horizons lointains transforme tes croyances vers plus de pragmatisme et de structure. Tu développes une philosophie qui a des applications pratiques. Tes voyages peuvent te montrer différentes formes d'autorité et de structure.

## Ce que tu pourrais vivre
- Une transformation vers une sagesse plus structurée
- L'intérêt pour des systèmes de pensée solides
- Des voyages qui transforment ta vision du pouvoir
- La mort de croyances naïves

## Conseils pour ce transit
- Développe une philosophie pragmatique et solide
- Apprends des systèmes qui ont fait leurs preuves
- Construis une vision du monde qui fonctionne""",

    ('capricorn', 10): """# ♇ Transit de Pluton en Capricorne — Maison X

**En une phrase :** Ta carrière et ton statut traversent une transformation majeure des structures de pouvoir.

## L'énergie du moment
Pluton traverse sa maison de prédilection avec l'énergie structurante du Capricorne. Ta carrière et ta place dans le monde sont profondément transformées. Des positions de pouvoir peuvent être atteintes ou perdues. Tu deviens un agent de transformation des systèmes établis.

## Ce que tu pourrais vivre
- Des transformations majeures de carrière et de statut
- L'accès à ou la perte de positions de pouvoir
- La transformation de systèmes et structures professionnels
- Une réputation de personne qui change les choses

## Conseils pour ce transit
- Utilise le pouvoir avec grande responsabilité
- Transforme les systèmes plutôt que de les servir aveuglément
- Construis une carrière qui a un impact durable""",

    ('capricorn', 11): """# ♇ Transit de Pluton en Capricorne — Maison XI

**En une phrase :** Tes cercles sociaux et aspirations sont transformés vers des objectifs structurés et durables.

## L'énergie du moment
Pluton en Capricorne dans ta maison des amitiés transforme tes cercles sociaux autour de structures et d'objectifs à long terme. Tu es attiré par des groupes qui construisent quelque chose de durable. Tes aspirations deviennent plus réalistes et structurées.

## Ce que tu pourrais vivre
- Des cercles sociaux qui se restructurent
- L'attrait pour des organisations établies ou en construction
- Des aspirations concrètes et réalisables
- Des transformations dans les dynamiques de groupe

## Conseils pour ce transit
- Rejoins des groupes qui construisent durablement
- Définis des aspirations réalistes mais ambitieuses
- Contribue à des structures qui servent le bien commun""",

    ('capricorn', 12): """# ♇ Transit de Pluton en Capricorne — Maison XII

**En une phrase :** Une transformation profonde libère des structures de contrôle inconscientes.

## L'énergie du moment
Pluton en Capricorne dans ta maison des profondeurs travaille sur les structures de contrôle et les limitations inconscientes. Des peurs liées à l'autorité ou à l'échec peuvent être révélées et libérées. Tu développes une autorité intérieure qui ne dépend pas des structures extérieures.

## Ce que tu pourrais vivre
- La libération de structures de contrôle inconscientes
- Des rêves révélant des peurs d'autorité ou d'échec
- La transformation de ta relation inconsciente au pouvoir
- Le développement d'une autorité intérieure authentique

## Conseils pour ce transit
- Travaille sur tes peurs inconscientes du pouvoir
- Libère les structures qui t'emprisonnent de l'intérieur
- Développe une autorité qui vient de l'âme""",

    # ============================================================
    # PLUTON EN VERSEAU (♇ en ♒)
    # ============================================================
    ('aquarius', 1): """# ♇ Transit de Pluton en Verseau — Maison I

**En une phrase :** Ton identité est transformée vers une expression radicalement unique et collective.

## L'énergie du moment
Pluton en Verseau dans ta maison I transforme radicalement ta façon de te présenter vers plus d'originalité et de conscience collective. Tu traverses une mort et renaissance de ton individualité dans sa relation au groupe. Tu deviens un agent de transformation collective.

## Ce que tu pourrais vivre
- Une transformation vers une identité radicalement unique
- La mort de la conformité et des attentes sociales
- L'émergence d'un rôle dans le changement collectif
- Des crises qui révèlent ton unicité et ta place dans le groupe

## Conseils pour ce transit
- Embrasse ton unicité sans te couper du collectif
- Deviens un agent de changement pour le groupe
- Transforme ta relation à l'individualité et à la communauté""",

    ('aquarius', 2): """# ♇ Transit de Pluton en Verseau — Maison II

**En une phrase :** Tes ressources sont transformées par des innovations et une vision collective de l'abondance.

## L'énergie du moment
Pluton en Verseau dans ta maison des ressources transforme ta relation à l'argent vers des modèles innovants et collectifs. Tu peux participer à de nouvelles formes d'économie. Les valeurs individualistes sont transformées vers une vision plus large.

## Ce que tu pourrais vivre
- Des finances transformées par l'innovation
- L'attrait pour de nouveaux modèles économiques
- La mort de valeurs purement individualistes
- Des ressources liées aux technologies ou au collectif

## Conseils pour ce transit
- Explore des formes innovantes de richesse
- Transforme ta vision de l'abondance vers le collectif
- Utilise tes ressources pour le bien du groupe""",

    ('aquarius', 3): """# ♇ Transit de Pluton en Verseau — Maison III

**En une phrase :** Ta communication devient un vecteur de transformation collective à travers les idées nouvelles.

## L'énergie du moment
Pluton en Verseau dans ta maison de la communication transforme ta pensée vers des idées révolutionnaires et collectives. Tes mots ont le pouvoir de changer les consciences à grande échelle. Tu peux devenir un transmetteur d'idées qui transforment la société.

## Ce que tu pourrais vivre
- Une pensée révolutionnaire et visionnaire
- Des communications qui changent les paradigmes
- L'intérêt pour les technologies de communication
- Des transformations dans les réseaux de proximité

## Conseils pour ce transit
- Utilise ta communication pour le changement collectif
- Transmets des idées qui font évoluer
- Connecte les gens autour de visions nouvelles""",

    ('aquarius', 4): """# ♇ Transit de Pluton en Verseau — Maison IV

**En une phrase :** Tes fondations sont transformées vers des formes nouvelles de communauté et d'appartenance.

## L'énergie du moment
Pluton en Verseau dans ta maison IV transforme ta vie familiale et tes racines vers des formes plus innovantes et collectives. Tu peux vivre en communauté ou créer une famille non conventionnelle. Les notions traditionnelles de foyer sont révolutionnées.

## Ce que tu pourrais vivre
- Des formes nouvelles de vie familiale ou communautaire
- La transformation des traditions vers plus d'ouverture
- La création d'un foyer connecté au monde
- La mort de concepts familiaux restrictifs

## Conseils pour ce transit
- Crée de nouvelles formes de foyer et de communauté
- Transforme les traditions tout en honorant les liens
- Trouve ton appartenance dans le collectif""",

    ('aquarius', 5): """# ♇ Transit de Pluton en Verseau — Maison V

**En une phrase :** Ta créativité et tes amours sont transformées vers des expressions collectives et technologiques.

## L'énergie du moment
Pluton en Verseau dans ta maison de la créativité transforme ton expression artistique vers des formes innovantes et collectives. En amour, tu cherches des connexions qui transcendent les conventions. Les plaisirs incluent l'innovation et la contribution au collectif.

## Ce que tu pourrais vivre
- Une créativité qui utilise les nouvelles technologies
- Des amours non conventionnelles et libres
- Des créations collaboratives et collectives
- Le plaisir de l'innovation et du changement

## Conseils pour ce transit
- Exprime ta créativité de façon innovante
- Explore des formes d'amour non conventionnelles
- Crée pour et avec le collectif""",

    ('aquarius', 6): """# ♇ Transit de Pluton en Verseau — Maison VI

**En une phrase :** Ton quotidien est transformé par la technologie et le service à la communauté.

## L'énergie du moment
Pluton en Verseau dans ta maison du travail quotidien transforme tes routines par l'innovation et la conscience collective. Ton travail peut devenir un service à la communauté élargie. Ta santé bénéficie de technologies et d'approches nouvelles.

## Ce que tu pourrais vivre
- Un travail transformé par la technologie
- Des routines qui servent le collectif
- Une santé soutenue par les innovations
- La mort de pratiques dépassées

## Conseils pour ce transit
- Intègre l'innovation dans ton quotidien
- Sers la communauté à travers ton travail
- Utilise les nouvelles approches de bien-être""",

    ('aquarius', 7): """# ♇ Transit de Pluton en Verseau — Maison VII

**En une phrase :** Tes relations sont transformées vers des partenariats égalitaires et orientés vers le collectif.

## L'énergie du moment
Pluton en Verseau dans ta maison des partenariats transforme tes relations vers des formes plus libres et égalitaires. Tu attires des partenaires avec qui tu peux contribuer au changement collectif. Les relations conventionnelles ne te suffisent plus.

## Ce que tu pourrais vivre
- Des relations transformées vers plus de liberté
- Des partenaires visionnaires et engagés socialement
- La fin de partenariats basés sur des conventions
- Des unions orientées vers le service collectif

## Conseils pour ce transit
- Crée des partenariats égalitaires et libres
- Choisis des partenaires avec une vision collective
- Transformez ensemble pour le bien du monde""",

    ('aquarius', 8): """# ♇ Transit de Pluton en Verseau — Maison VIII

**En une phrase :** Des transformations profondes touchent ta relation au pouvoir collectif et aux ressources partagées.

## L'énergie du moment
Pluton en Verseau dans ta maison des transformations crée des changements dans ta façon de partager les ressources et le pouvoir avec le groupe. Tu peux participer à des transformations collectives majeures. Les formes traditionnelles de pouvoir sont révolutionnées.

## Ce que tu pourrais vivre
- Des transformations du pouvoir collectif
- De nouvelles formes de partage des ressources
- Une compréhension de la transformation collective
- La mort de structures de pouvoir obsolètes

## Conseils pour ce transit
- Participe aux transformations collectives
- Explore de nouvelles formes de partage
- Utilise le pouvoir pour le bien du groupe""",

    ('aquarius', 9): """# ♇ Transit de Pluton en Verseau — Maison IX

**En une phrase :** Ta vision du monde est transformée vers une conscience globale et futuriste.

## L'énergie du moment
Pluton en Verseau dans ta maison des horizons lointains transforme tes croyances vers une vision globale et futuriste. Tu développes une philosophie qui embrasse l'humanité entière. Tes voyages peuvent te montrer le futur en construction.

## Ce que tu pourrais vivre
- Une transformation vers une vision globale
- L'intérêt pour les philosophies futuristes
- Des voyages vers des lieux d'innovation
- La mort de visions du monde limitées

## Conseils pour ce transit
- Développe une vision qui embrasse l'humanité
- Explore les idées qui façonnent le futur
- Voyage vers ce qui innove et transforme""",

    ('aquarius', 10): """# ♇ Transit de Pluton en Verseau — Maison X

**En une phrase :** Ta carrière est transformée vers des rôles d'innovation et de service à l'humanité.

## L'énergie du moment
Pluton en Verseau dans ta maison de la carrière transforme ta trajectoire vers des positions d'innovation et de changement social. Tu peux devenir un leader de la transformation collective. Ta réputation se construit sur ta contribution au futur.

## Ce que tu pourrais vivre
- Une carrière transformée vers l'innovation sociale
- Des positions qui servent le changement collectif
- Une réputation de visionnaire et d'innovateur
- Des transformations majeures de statut

## Conseils pour ce transit
- Développe une carrière qui sert l'humanité
- Utilise ton influence pour le changement positif
- Deviens un pionnier du futur dans ton domaine""",

    ('aquarius', 11): """# ♇ Transit de Pluton en Verseau — Maison XI

**En une phrase :** Tes cercles sociaux et aspirations atteignent une puissance transformatrice collective maximale.

## L'énergie du moment
Pluton traverse sa maison naturelle avec l'énergie révolutionnaire du Verseau. Tes réseaux sociaux et tes aspirations sont le lieu de transformations majeures. Tu es au cœur des mouvements qui changent le monde. Ton rôle dans le collectif atteint une puissance considérable.

## Ce que tu pourrais vivre
- Un rôle central dans des transformations collectives
- Des réseaux puissants et transformateurs
- Des aspirations qui touchent l'humanité entière
- Des dynamiques intenses dans les groupes

## Conseils pour ce transit
- Utilise ton influence collective avec sagesse
- Contribue aux transformations qui comptent
- Deviens un catalyseur de changement""",

    ('aquarius', 12): """# ♇ Transit de Pluton en Verseau — Maison XII

**En une phrase :** Une transformation profonde libère des patterns d'aliénation et connecte à la conscience collective.

## L'énergie du moment
Pluton en Verseau dans ta maison des profondeurs travaille sur tes patterns inconscients de séparation du collectif. Des sentiments d'aliénation ou de différence peuvent être transformés. Tu accèdes à une connexion profonde avec l'inconscient collectif.

## Ce que tu pourrais vivre
- La libération de patterns d'aliénation
- L'accès à l'inconscient collectif
- Des rêves concernant le futur de l'humanité
- La transformation de la relation entre individu et collectif

## Conseils pour ce transit
- Travaille sur tes sentiments d'aliénation
- Connecte-toi à la conscience collective
- Contribue à l'éveil depuis les profondeurs""",

    # ============================================================
    # PLUTON EN POISSONS (♇ en ♓)
    # ============================================================
    ('pisces', 1): """# ♇ Transit de Pluton en Poissons — Maison I

**En une phrase :** Ton identité traverse une dissolution et renaissance spirituelle profonde.

## L'énergie du moment
Pluton en Poissons dans ta maison I transforme radicalement ton identité à travers des processus de dissolution spirituelle. L'ego traverse une mort pour révéler une connexion plus profonde à l'universel. Tu incarnes une puissance qui vient de la connexion au divin.

## Ce que tu pourrais vivre
- Une transformation profonde vers une identité plus spirituelle
- La dissolution de l'ego séparé
- L'émergence d'une présence connectée au tout
- Des crises qui révèlent l'illusion du moi séparé

## Conseils pour ce transit
- Laisse l'ego se transformer par la grâce
- Incarne une puissance qui vient du divin
- Deviens un canal de transformation spirituelle""",

    ('pisces', 2): """# ♇ Transit de Pluton en Poissons — Maison II

**En une phrase :** Ta relation aux ressources est transformée vers une compréhension spirituelle de l'abondance.

## L'énergie du moment
Pluton en Poissons dans ta maison des ressources dissout tes attachements matériels pour révéler une richesse spirituelle. Tu découvres que la vraie sécurité est dans la connexion au divin. Les possessions matérielles perdent leur emprise.

## Ce que tu pourrais vivre
- La dissolution des attachements matériels
- La découverte d'une abondance spirituelle infinie
- Des finances qui dépendent de la grâce
- La transformation de ta relation à la sécurité

## Conseils pour ce transit
- Lâche prise sur les attachements matériels
- Découvre la richesse qui ne peut être perdue
- Fais confiance à l'abondance universelle""",

    ('pisces', 3): """# ♇ Transit de Pluton en Poissons — Maison III

**En une phrase :** Ta communication devient un véhicule de transformation spirituelle et de guérison.

## L'énergie du moment
Pluton en Poissons dans ta maison de la communication transforme ta pensée et ton expression vers des dimensions spirituelles et intuitives. Tes mots ont le pouvoir de guérir et de transformer les âmes. Tu captes et transmets des vérités qui viennent d'au-delà.

## Ce que tu pourrais vivre
- Une communication intuitive et guérisseuse
- Des capacités de perception subtiles
- Des échanges qui touchent les âmes
- La transformation par les mots spirituels

## Conseils pour ce transit
- Utilise ta communication pour guérir
- Transmets ce que tu reçois intuitivement
- Laisse tes mots être des véhicules du divin""",

    ('pisces', 4): """# ♇ Transit de Pluton en Poissons — Maison IV

**En une phrase :** Tes fondations sont transformées vers une connexion spirituelle profonde aux racines universelles.

## L'énergie du moment
Pluton en Poissons dans ta maison IV dissout les frontières de la famille et du foyer pour révéler une appartenance universelle. Des mémoires ancestrales profondes peuvent être libérées. Tu trouves ta vraie maison dans le divin.

## Ce que tu pourrais vivre
- La dissolution des frontières familiales
- L'accès à des mémoires ancestrales profondes
- La découverte d'une appartenance universelle
- La transformation de ta conception du foyer

## Conseils pour ce transit
- Laisse les frontières familiales se dissoudre
- Guéris les mémoires ancestrales
- Trouve ta maison dans le cœur divin""",

    ('pisces', 5): """# ♇ Transit de Pluton en Poissons — Maison V

**En une phrase :** Ta créativité et tes amours deviennent des canaux de transformation spirituelle.

## L'énergie du moment
Pluton en Poissons dans ta maison de la créativité transforme ton expression artistique en canal du divin. En amour, tu cherches l'union mystique qui transcende le personnel. Les plaisirs deviennent des extases spirituelles.

## Ce que tu pourrais vivre
- Une créativité comme canal du divin
- Des amours qui touchent au sacré
- Des extases qui transforment
- La dissolution des frontières dans l'amour et la création

## Conseils pour ce transit
- Laisse le divin créer à travers toi
- Cherche l'amour sacré
- Trouve la joie dans la connexion au tout""",

    ('pisces', 6): """# ♇ Transit de Pluton en Poissons — Maison VI

**En une phrase :** Ton quotidien et ta santé sont transformés par le service spirituel et la guérison.

## L'énergie du moment
Pluton en Poissons dans ta maison du travail quotidien transforme tes routines en pratiques spirituelles. Ton travail devient service désintéressé. Ta santé est maintenue par la grâce et les pratiques énergétiques.

## Ce que tu pourrais vivre
- Un travail transformé en service spirituel
- Une santé soutenue par des pratiques énergétiques
- Des routines qui sont des méditations
- La dissolution de l'ego à travers le service

## Conseils pour ce transit
- Fais de chaque tâche une offrande
- Guéris par la connexion au divin
- Sers sans attente de retour""",

    ('pisces', 7): """# ♇ Transit de Pluton en Poissons — Maison VII

**En une phrase :** Tes relations deviennent des unions mystiques qui transcendent le personnel.

## L'énergie du moment
Pluton en Poissons dans ta maison des partenariats transforme tes relations vers des dimensions spirituelles profondes. Tu cherches des partenaires avec qui tu peux vivre l'union divine. Les frontières entre toi et l'autre se dissolvent.

## Ce que tu pourrais vivre
- Des relations qui touchent au mystique
- Des partenaires hautement spirituels
- La dissolution des frontières dans l'union
- La transformation à travers l'amour divin

## Conseils pour ce transit
- Recherche l'amour sacré tout en restant ancré
- Maintiens ton identité dans la fusion
- Transforme-toi à travers l'union divine""",

    ('pisces', 8): """# ♇ Transit de Pluton en Poissons — Maison VIII

**En une phrase :** Des transformations ultimes dissolvent toutes les peurs et révèlent l'éternité.

## L'énergie du moment
Pluton en Poissons dans ta maison des transformations crée une puissance de dissolution et de régénération spirituelle maximale. Tu peux transcender toutes les peurs, y compris celle de la mort. Des pouvoirs de guérison et de transformation extraordinaires sont accessibles.

## Ce que tu pourrais vivre
- La transcendance de toutes les peurs
- L'accès à des pouvoirs de guérison profonds
- La compréhension directe de l'éternité
- Des transformations spirituelles ultimes

## Conseils pour ce transit
- Laisse toutes les peurs se dissoudre
- Utilise tes pouvoirs de guérison avec sagesse
- Traverse les transformations comme des initiations spirituelles""",

    ('pisces', 9): """# ♇ Transit de Pluton en Poissons — Maison IX

**En une phrase :** Ta vision du monde est transformée vers une compréhension mystique de l'existence.

## L'énergie du moment
Pluton en Poissons dans ta maison des horizons lointains transforme tes croyances vers une vision mystique et unitive. Tu comprends directement l'unité de toutes choses. Tes voyages peuvent être des pèlerinages spirituels transformateurs.

## Ce que tu pourrais vivre
- Une compréhension mystique de l'existence
- Des voyages de transformation spirituelle profonde
- La dissolution de toutes les croyances séparatives
- L'accès à une sagesse universelle

## Conseils pour ce transit
- Ouvre-toi à la compréhension mystique
- Voyage vers ce qui nourrit ton âme
- Développe une vision qui embrasse le tout""",

    ('pisces', 10): """# ♇ Transit de Pluton en Poissons — Maison X

**En une phrase :** Ta carrière est transformée vers un service spirituel et une guérison à grande échelle.

## L'énergie du moment
Pluton en Poissons dans ta maison de la carrière transforme ta vocation vers le service spirituel et la guérison. Tu peux devenir reconnu comme guérisseur, artiste ou guide spirituel. Ta réputation se construit sur ta capacité à toucher les âmes.

## Ce que tu pourrais vivre
- Une carrière de service spirituel ou artistique
- Une réputation de personne qui guérit et élève
- La dissolution des ambitions personnelles
- Une vocation qui est un don au monde

## Conseils pour ce transit
- Laisse ta carrière devenir un service
- Accepte la reconnaissance avec humilité
- Offre ton travail comme un cadeau spirituel""",

    ('pisces', 11): """# ♇ Transit de Pluton en Poissons — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des communautés spirituelles et tes aspirations touchent le divin.

## L'énergie du moment
Pluton en Poissons dans ta maison des amitiés transforme tes cercles sociaux en sanghas spirituelles. Tu es attiré par des communautés de pratique et de service. Tes aspirations concernent l'éveil et la guérison de l'humanité.

## Ce que tu pourrais vivre
- Des amitiés comme des liens d'âme
- L'appartenance à des communautés spirituelles
- Des aspirations d'éveil collectif
- La dissolution des frontières entre amis

## Conseils pour ce transit
- Rejoins des communautés de pratique authentique
- Contribue à l'éveil collectif
- Aspire à la guérison de tous les êtres""",

    ('pisces', 12): """# ♇ Transit de Pluton en Poissons — Maison XII

**En une phrase :** Une transformation ultime dissout toutes les illusions et révèle l'unité avec le tout.

## L'énergie du moment
Pluton en Poissons dans sa maison domicile crée la configuration de dissolution et de transformation spirituelle la plus puissante. Toutes les illusions peuvent se dissoudre. Tu peux accéder à des états d'union complète avec le divin. C'est une période de potentiel spirituel ultime.

## Ce que tu pourrais vivre
- La dissolution complète des illusions
- Des états d'union mystique avec le tout
- La libération de tous les karmas
- L'accès à la conscience cosmique

## Conseils pour ce transit
- Ouvre-toi complètement au divin
- Laisse toutes les illusions se dissoudre
- Deviens un canal pur de la grâce divine""",
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
        print(f"✅ Transit Pluto (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
