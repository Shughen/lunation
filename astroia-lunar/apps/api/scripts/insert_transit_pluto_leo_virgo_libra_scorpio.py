#!/usr/bin/env python3
"""Insert transit_pluto interpretations for Leo, Virgo, Libra, Scorpio (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_PLUTO_INTERPRETATIONS = {
    # ============================================================
    # PLUTON EN LION (♇ en ♌)
    # ============================================================
    ('leo', 1): """# ♇ Transit de Pluton en Lion — Maison I

**En une phrase :** Ton identité traverse une transformation de pouvoir qui révèle ta vraie lumière.

## L'énergie du moment
Pluton en Lion dans ta maison I transforme radicalement ton ego et ta façon de te présenter. Tu traverses une mort et renaissance de ton besoin de reconnaissance. Ta vraie puissance créative émerge, libérée des besoins superficiels d'approbation. Tu deviens un leader transformé.

## Ce que tu pourrais vivre
- Une transformation profonde de ton ego et de ta fierté
- La mort de besoins d'attention superficiels
- L'émergence d'une créativité puissante et authentique
- Des crises qui révèlent ta vraie lumière

## Conseils pour ce transit
- Laisse mourir l'ego superficiel
- Découvre ta vraie puissance créative
- Deviens un leader par la transformation intérieure""",

    ('leo', 2): """# ♇ Transit de Pluton en Lion — Maison II

**En une phrase :** Tes ressources sont transformées par ta créativité et ton expression authentique.

## L'énergie du moment
Pluton en Lion dans ta maison des ressources transforme ta relation à l'argent à travers la créativité et l'expression de soi. Tu peux acquérir du pouvoir par tes talents créatifs. Les valeurs liées à la reconnaissance et au rayonnement sont purifiées.

## Ce que tu pourrais vivre
- Des revenus transformés par la créativité
- La mort d'attachements au prestige matériel
- La découverte de ta vraie valeur créative
- Des crises qui révèlent ce qui compte vraiment

## Conseils pour ce transit
- Valorise ta créativité authentique
- Transforme ta relation au prestige et au luxe
- Trouve ta richesse dans ton expression unique""",

    ('leo', 3): """# ♇ Transit de Pluton en Lion — Maison III

**En une phrase :** Ta communication devient un outil de transformation créative et d'influence puissante.

## L'énergie du moment
Pluton en Lion dans ta maison de la communication transforme ta façon de t'exprimer vers plus de puissance créative. Tes mots ont le pouvoir d'inspirer et de transformer. Tu peux influencer et diriger par ta communication charismatique.

## Ce que tu pourrais vivre
- Une communication charismatique et transformatrice
- L'émergence d'une parole qui inspire et dirige
- Des transformations dans les relations avec les proches
- La mort de l'expression superficielle

## Conseils pour ce transit
- Utilise ton charisme communicatif avec responsabilité
- Inspire et transforme par tes mots
- Laisse mourir les expressions qui cherchent juste l'attention""",

    ('leo', 4): """# ♇ Transit de Pluton en Lion — Maison IV

**En une phrase :** Tes fondations familiales sont transformées autour de questions de fierté et de créativité.

## L'énergie du moment
Pluton en Lion dans ta maison IV transforme ta vie familiale autour de dynamiques de pouvoir, de reconnaissance et de créativité. Des egos familiaux peuvent être confrontés. Tu crées un foyer qui célèbre l'authenticité et la créativité.

## Ce que tu pourrais vivre
- Des transformations familiales liées à l'ego et la fierté
- La mort de patterns d'orgueil hérités
- La création d'un foyer qui célèbre l'expression unique
- Des dynamiques de pouvoir familial révélées et transformées

## Conseils pour ce transit
- Transforme les egos familiaux avec compassion
- Crée un foyer qui célèbre l'authenticité de chacun
- Guéris les blessures d'orgueil familiales""",

    ('leo', 5): """# ♇ Transit de Pluton en Lion — Maison V

**En une phrase :** Ta créativité et tes amours atteignent une intensité transformatrice maximale.

## L'énergie du moment
Pluton traverse sa maison de joie avec l'énergie du Lion, maximisant la transformation créative et amoureuse. Tu vis des passions dévorantes qui te transforment complètement. Ta créativité devient un pouvoir de transformation. Les plaisirs deviennent des voies d'initiation.

## Ce que tu pourrais vivre
- Une créativité d'une puissance exceptionnelle
- Des amours passionnelles et transformatrices
- Des expériences de plaisir qui changent la vie
- La transformation à travers ce que tu aimes créer

## Conseils pour ce transit
- Canalise cette puissance créative immense
- Vis les passions comme des initiations
- Transforme-toi à travers ce que tu crées et aimes""",

    ('leo', 6): """# ♇ Transit de Pluton en Lion — Maison VI

**En une phrase :** Ton quotidien est transformé pour permettre ton expression créative authentique.

## L'énergie du moment
Pluton en Lion dans ta maison du travail quotidien transforme tes routines pour qu'elles servent ta créativité et ton expression. Tu refuses un travail qui ne te permet pas de briller. Ta santé est liée à ta capacité d'expression créative.

## Ce que tu pourrais vivre
- Un travail transformé pour permettre l'expression créative
- Une santé liée au bonheur de créer
- La mort de routines qui étouffent ta lumière
- La transformation du quotidien en terrain de créativité

## Conseils pour ce transit
- Transforme ton quotidien pour qu'il nourrisse ta créativité
- Ne te contente pas d'un travail qui t'éteint
- Brille même dans les petites choses""",

    ('leo', 7): """# ♇ Transit de Pluton en Lion — Maison VII

**En une phrase :** Tes relations sont transformées par des dynamiques de pouvoir créatif et de reconnaissance mutuelle.

## L'énergie du moment
Pluton en Lion dans ta maison des partenariats transforme tes relations autour de questions de reconnaissance, de créativité et d'ego. Tu attires des partenaires puissants et créatifs avec qui les jeux de pouvoir et de lumière sont intenses.

## Ce que tu pourrais vivre
- Des relations transformées par des dynamiques d'ego
- Des partenaires créatifs et charismatiques
- Des luttes de pouvoir sur qui brille le plus
- La transformation des patterns de reconnaissance en relation

## Conseils pour ce transit
- Apprends à briller ensemble, pas en compétition
- Transforme les jeux d'ego en co-création
- Choisis des partenaires qui célèbrent ta lumière""",

    ('leo', 8): """# ♇ Transit de Pluton en Lion — Maison VIII

**En une phrase :** Des transformations profondes touchent ton ego et ta relation au pouvoir créatif.

## L'énergie du moment
Pluton en Lion dans ta maison des transformations travaille sur les dimensions profondes de ton ego et de ta créativité. Des morts symboliques de l'ego mènent à une puissance créative régénérée. Tu accèdes à un pouvoir de transformation par la créativité.

## Ce que tu pourrais vivre
- La mort et renaissance de ton ego
- La transformation de ta relation au pouvoir
- L'accès à une créativité régénératrice puissante
- Des expériences intenses qui transforment ta fierté

## Conseils pour ce transit
- Laisse l'ego mourir pour renaître transformé
- Découvre un pouvoir qui ne vient pas de l'orgueil
- Utilise ta créativité comme outil de transformation""",

    ('leo', 9): """# ♇ Transit de Pluton en Lion — Maison IX

**En une phrase :** Ta vision du monde est transformée par une foi en ta propre lumière créative.

## L'énergie du moment
Pluton en Lion dans ta maison des horizons lointains transforme tes croyances autour de la créativité, l'expression et le leadership. Tu développes une philosophie qui honore l'unicité et la lumière de chacun. Tes voyages peuvent te révéler à toi-même.

## Ce que tu pourrais vivre
- Une transformation des croyances sur la créativité et l'expression
- Des voyages qui te permettent de briller différemment
- Une philosophie qui célèbre l'unicité de chaque être
- La mort de croyances qui diminuent ta lumière

## Conseils pour ce transit
- Développe une foi en ta propre lumière
- Voyage vers des lieux qui t'inspirent créativement
- Enseigne ou partage ce que tu as de unique""",

    ('leo', 10): """# ♇ Transit de Pluton en Lion — Maison X

**En une phrase :** Ta carrière est transformée vers des rôles de leadership créatif et d'influence.

## L'énergie du moment
Pluton en Lion dans ta maison de la carrière transforme ta trajectoire vers des positions de pouvoir créatif. Tu peux devenir un leader qui inspire par sa lumière. Ta réputation se construit sur ta capacité à briller et à permettre aux autres de briller.

## Ce que tu pourrais vivre
- Une carrière transformée vers le leadership créatif
- Le pouvoir acquis par le charisme et la créativité
- Une réputation de personne qui inspire
- Des transformations radicales de statut

## Conseils pour ce transit
- Utilise ton pouvoir pour inspirer les autres
- Dirige par l'exemple créatif
- Transforme ton domaine par ta lumière""",

    ('leo', 11): """# ♇ Transit de Pluton en Lion — Maison XI

**En une phrase :** Tes cercles sociaux sont transformés autour de la créativité collective et du leadership partagé.

## L'énergie du moment
Pluton en Lion dans ta maison des amitiés transforme tes cercles sociaux autour de la créativité et de la reconnaissance. Tu es attiré par des groupes de créatifs puissants. Tes aspirations incluent briller ensemble et créer collectivement.

## Ce que tu pourrais vivre
- Des amitiés avec des créatifs et des leaders
- Des dynamiques de pouvoir dans les groupes
- Des aspirations de création et de leadership collectif
- La transformation des cercles autour de qui inspire

## Conseils pour ce transit
- Rejoins des collectifs créatifs puissants
- Contribue par ta lumière unique au groupe
- Aspire à des créations collectives qui brillent""",

    ('leo', 12): """# ♇ Transit de Pluton en Lion — Maison XII

**En une phrase :** Une transformation profonde libère ton ego des besoins inconscients de reconnaissance.

## L'énergie du moment
Pluton en Lion dans ta maison des profondeurs travaille sur les aspects inconscients de ton ego et de ton besoin de briller. Des patterns de recherche d'attention non reconnues peuvent être révélés et transformés. Tu découvres une lumière qui ne dépend pas de l'extérieur.

## Ce que tu pourrais vivre
- La révélation de besoins d'attention inconscients
- La transformation de l'ego au niveau le plus profond
- Des rêves impliquant la lumière et la reconnaissance
- La découverte d'une créativité spirituelle

## Conseils pour ce transit
- Travaille sur tes besoins inconscients de reconnaissance
- Découvre une lumière qui vient de l'intérieur
- Transforme l'ego pour qu'il serve l'âme""",

    # ============================================================
    # PLUTON EN VIERGE (♇ en ♍)
    # ============================================================
    ('virgo', 1): """# ♇ Transit de Pluton en Vierge — Maison I

**En une phrase :** Ton identité est profondément transformée vers plus d'efficacité et de service.

## L'énergie du moment
Pluton en Vierge dans ta maison I transforme radicalement ta façon de te présenter vers plus de précision et d'utilité. Tu traverses une mort et renaissance de ton identité autour du perfectionnisme et du service. Tu deviens un agent de transformation par l'amélioration concrète.

## Ce que tu pourrais vivre
- Une transformation profonde vers plus d'efficacité
- La mort de patterns de perfectionnisme destructeur
- L'émergence d'une capacité de service puissante
- Des crises qui révèlent où tu dois t'améliorer

## Conseils pour ce transit
- Transforme le perfectionnisme en excellence
- Développe ton pouvoir à travers le service
- Améliore-toi sans te détruire par la critique""",

    ('virgo', 2): """# ♇ Transit de Pluton en Vierge — Maison II

**En une phrase :** Tes ressources sont transformées par une approche méthodique et purificatrice.

## L'énergie du moment
Pluton en Vierge dans ta maison des ressources transforme ta relation à l'argent par l'analyse et l'amélioration. Tu peux acquérir des ressources par tes compétences techniques et ta capacité d'amélioration. Les valeurs superflues sont éliminées.

## Ce que tu pourrais vivre
- Des finances transformées par une gestion plus rigoureuse
- La mort d'attachements à ce qui est superflu
- La valorisation de ce qui est vraiment utile
- Des crises qui éliminent le non-essentiel

## Conseils pour ce transit
- Purifie ta relation aux ressources
- Valorise tes compétences techniques
- Élimine ce qui n'a pas de vraie valeur""",

    ('virgo', 3): """# ♇ Transit de Pluton en Vierge — Maison III

**En une phrase :** Ta communication devient un outil d'analyse et de transformation précise.

## L'énergie du moment
Pluton en Vierge dans ta maison de la communication transforme ta pensée vers plus de profondeur analytique. Tes mots ont le pouvoir de diagnostiquer et d'améliorer. Tu peux percer les illusions par une analyse rigoureuse.

## Ce que tu pourrais vivre
- Une pensée d'une précision et d'une profondeur exceptionnelles
- Des communications qui analysent et transforment
- La mort de conversations superficielles
- Des révélations par l'analyse détaillée

## Conseils pour ce transit
- Utilise ton analyse pour améliorer, pas pour critiquer
- Communique avec précision et compassion
- Transforme par la compréhension détaillée""",

    ('virgo', 4): """# ♇ Transit de Pluton en Vierge — Maison IV

**En une phrase :** Tes fondations sont transformées par une purification et une amélioration méthodique.

## L'énergie du moment
Pluton en Vierge dans ta maison IV transforme ta vie familiale et domestique par l'analyse et la purification. Des patterns familiaux de perfectionnisme ou de critique peuvent être révélés et transformés. Tu crées un foyer plus efficace et sain.

## Ce que tu pourrais vivre
- Une transformation méthodique du foyer
- La révélation de patterns familiaux critiques
- La purification de la vie domestique
- L'amélioration des relations familiales par le service mutuel

## Conseils pour ce transit
- Purifie ton foyer sans obsession
- Transforme les patterns de critique familiale
- Crée un espace qui soutient la santé de tous""",

    ('virgo', 5): """# ♇ Transit de Pluton en Vierge — Maison V

**En une phrase :** Ta créativité et tes amours sont transformées vers plus de précision et de profondeur technique.

## L'énergie du moment
Pluton en Vierge dans ta maison de la créativité intensifie ton expression artistique vers l'artisanat et la maîtrise technique. En amour, tu cherches des relations qui améliorent mutuellement. Les plaisirs superficiels ne suffisent plus.

## Ce que tu pourrais vivre
- Une créativité technique et artisanale profonde
- Des amours basées sur l'amélioration mutuelle
- La mort des divertissements superficiels
- Une transformation par la maîtrise et la technique

## Conseils pour ce transit
- Perfectionne ton art avec passion
- Cherche des relations qui t'améliorent
- Trouve le plaisir dans la maîtrise""",

    ('virgo', 6): """# ♇ Transit de Pluton en Vierge — Maison VI

**En une phrase :** Ton quotidien et ta santé traversent une transformation purificatrice complète.

## L'énergie du moment
Pluton traverse sa maison de prédilection avec l'énergie analytique de la Vierge. C'est une période de purification intense du corps, des routines et du travail. Des crises de santé peuvent mener à une régénération complète par des changements de mode de vie.

## Ce que tu pourrais vivre
- Une transformation radicale de la santé et des routines
- Des crises qui mènent à la purification
- L'élimination de ce qui nuit au corps et à l'esprit
- Le développement de capacités de guérison puissantes

## Conseils pour ce transit
- Utilise les crises comme opportunités de purification
- Transforme radicalement tes habitudes de santé
- Développe ton pouvoir de guérison""",

    ('virgo', 7): """# ♇ Transit de Pluton en Vierge — Maison VII

**En une phrase :** Tes relations sont transformées par une analyse rigoureuse et un désir d'amélioration mutuelle.

## L'énergie du moment
Pluton en Vierge dans ta maison des partenariats transforme tes relations par l'analyse et le perfectionnement. Tu attires des partenaires avec qui tu peux t'améliorer mutuellement. La critique excessive doit être transformée en soutien constructif.

## Ce que tu pourrais vivre
- Des relations transformées par l'amélioration mutuelle
- Des partenaires analytiques et orientés vers le service
- Le risque de critique destructrice en relation
- La mort de relations qui ne fonctionnent pas

## Conseils pour ce transit
- Améliore tes relations sans les détruire par la critique
- Choisis des partenaires qui grandissent avec toi
- Transforme le perfectionnisme relationnel en soutien""",

    ('virgo', 8): """# ♇ Transit de Pluton en Vierge — Maison VIII

**En une phrase :** Des transformations profondes purifient ta psyché et régénèrent par l'analyse.

## L'énergie du moment
Pluton en Vierge dans ta maison des transformations apporte une purification profonde par l'analyse et la compréhension. Tu peux comprendre et transformer les patterns les plus cachés. La guérison passe par la compréhension détaillée des causes.

## Ce que tu pourrais vivre
- Une purification profonde par l'analyse
- La compréhension et la transformation de patterns cachés
- Une guérison par la connaissance des mécanismes
- La régénération par l'amélioration systématique

## Conseils pour ce transit
- Analyse pour comprendre et guérir
- Purifie les couches les plus profondes
- Utilise la compréhension comme outil de transformation""",

    ('virgo', 9): """# ♇ Transit de Pluton en Vierge — Maison IX

**En une phrase :** Ta vision du monde est transformée vers une sagesse pratique et applicable.

## L'énergie du moment
Pluton en Vierge dans ta maison des horizons lointains transforme tes croyances vers plus de pragmatisme. Tu es attiré par des sagesses qui ont des applications pratiques. La spiritualité doit servir l'amélioration concrète de la vie.

## Ce que tu pourrais vivre
- Une transformation des croyances vers le pratique
- L'attrait pour des traditions de guérison et d'amélioration
- Des voyages orientés vers l'apprentissage de techniques
- La mort de croyances non vérifiables

## Conseils pour ce transit
- Développe une sagesse qui s'applique au quotidien
- Apprends des techniques qui améliorent vraiment
- Construis une philosophie utile""",

    ('virgo', 10): """# ♇ Transit de Pluton en Vierge — Maison X

**En une phrase :** Ta carrière est transformée vers des rôles de service, d'analyse ou de santé.

## L'énergie du moment
Pluton en Vierge dans ta maison de la carrière transforme ta trajectoire vers des métiers de service, d'amélioration ou de santé. Tu peux acquérir du pouvoir par ta compétence et ton efficacité. Ta réputation se construit sur ta capacité à produire des résultats.

## Ce que tu pourrais vivre
- Une carrière transformée vers le service ou la santé
- Le pouvoir acquis par la compétence
- Une réputation basée sur l'efficacité
- Des transformations de carrière vers l'amélioration des systèmes

## Conseils pour ce transit
- Développe une expertise qui serve vraiment
- Utilise ton pouvoir pour améliorer les systèmes
- Construis ta réputation sur les résultats""",

    ('virgo', 11): """# ♇ Transit de Pluton en Vierge — Maison XI

**En une phrase :** Tes cercles sociaux sont transformés vers des groupes de service et d'amélioration.

## L'énergie du moment
Pluton en Vierge dans ta maison des amitiés transforme tes cercles sociaux autour du service et de l'amélioration collective. Tu es attiré par des groupes qui travaillent à améliorer concrètement le monde. Tes aspirations incluent l'efficacité collective.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes compétentes et serviables
- L'attrait pour des organisations d'amélioration pratique
- Des aspirations d'efficacité et de service collectif
- La transformation des groupes vers plus de fonctionnalité

## Conseils pour ce transit
- Rejoins des groupes qui améliorent concrètement les choses
- Contribue par tes compétences au collectif
- Aspire à des améliorations mesurables""",

    ('virgo', 12): """# ♇ Transit de Pluton en Vierge — Maison XII

**En une phrase :** Une transformation profonde purifie tes patterns inconscients de perfectionnisme et de critique.

## L'énergie du moment
Pluton en Vierge dans ta maison des profondeurs travaille sur tes tendances inconscientes au perfectionnisme et à l'autocritique. Des standards impossibles que tu t'imposes peuvent être révélés et transformés. Tu découvres une acceptation qui guérit.

## Ce que tu pourrais vivre
- La révélation de patterns de perfectionnisme inconscients
- La transformation de l'autocritique excessive
- Des rêves révélant des standards impossibles
- La découverte de l'acceptation comme guérison

## Conseils pour ce transit
- Libère le perfectionnisme inconscient
- Transforme la critique en compassion
- Découvre que l'imperfection est acceptable""",

    # ============================================================
    # PLUTON EN BALANCE (♇ en ♎)
    # ============================================================
    ('libra', 1): """# ♇ Transit de Pluton en Balance — Maison I

**En une phrase :** Ton identité est profondément transformée à travers tes relations et ta quête d'équilibre.

## L'énergie du moment
Pluton en Balance dans ta maison I transforme radicalement ta façon de te définir en relation avec les autres. Tu traverses une mort et renaissance de ton identité relationnelle. Tu développes une puissance qui vient de l'équilibre et de la capacité de créer l'harmonie.

## Ce que tu pourrais vivre
- Une transformation profonde de ton identité relationnelle
- La mort de la dépendance aux autres pour te définir
- L'émergence d'une capacité de créer l'équilibre
- Des crises qui révèlent ta façon de te relier

## Conseils pour ce transit
- Transforme ta relation à toi-même avant tout
- Développe une identité qui n'a pas besoin de l'autre
- Apprends à créer l'harmonie depuis l'intérieur""",

    ('libra', 2): """# ♇ Transit de Pluton en Balance — Maison II

**En une phrase :** Tes ressources sont transformées par les partenariats et la quête d'équité.

## L'énergie du moment
Pluton en Balance dans ta maison des ressources transforme ta relation à l'argent à travers les questions de partage et d'équité. Tu peux acquérir des ressources par les partenariats. Les valeurs liées à la justice et à l'équilibre sont purifiées.

## Ce que tu pourrais vivre
- Des finances transformées par les partenariats
- La mort d'injustices dans les arrangements financiers
- La valorisation de l'équité et du partage juste
- Des crises financières liées aux relations

## Conseils pour ce transit
- Transforme les arrangements financiers vers plus d'équité
- Valorise le partage juste
- Apprends que la vraie richesse inclut les relations""",

    ('libra', 3): """# ♇ Transit de Pluton en Balance — Maison III

**En une phrase :** Ta communication devient un outil de diplomatie transformatrice et de médiation puissante.

## L'énergie du moment
Pluton en Balance dans ta maison de la communication transforme ta façon de t'exprimer vers la diplomatie et la médiation. Tes mots ont le pouvoir de réconcilier ou de diviser. Tu peux transformer les conflits par la communication équilibrée.

## Ce que tu pourrais vivre
- Une communication diplomatique et transformatrice
- Le pouvoir de médiation et de réconciliation
- Des transformations dans les relations proches
- La mort de communications qui créent des conflits

## Conseils pour ce transit
- Utilise ta communication pour créer des ponts
- Transforme les conflits par le dialogue
- Développe l'art de la négociation""",

    ('libra', 4): """# ♇ Transit de Pluton en Balance — Maison IV

**En une phrase :** Tes fondations familiales sont transformées par la recherche d'équilibre et d'harmonie.

## L'énergie du moment
Pluton en Balance dans ta maison IV transforme ta vie familiale autour de questions d'équité et d'harmonie. Des déséquilibres familiaux sont révélés et corrigés. Tu crées un foyer basé sur des relations plus justes.

## Ce que tu pourrais vivre
- Une transformation des dynamiques familiales vers l'équité
- La révélation et correction de déséquilibres anciens
- La création d'un foyer plus harmonieux
- Des crises familiales qui mènent à plus de justice

## Conseils pour ce transit
- Travaille sur l'équité dans les relations familiales
- Crée un foyer où chacun a sa place
- Transforme les déséquilibres avec patience""",

    ('libra', 5): """# ♇ Transit de Pluton en Balance — Maison V

**En une phrase :** Ta créativité et tes amours sont transformées par une quête d'harmonie et de beauté profonde.

## L'énergie du moment
Pluton en Balance dans ta maison de la créativité intensifie ton expression artistique vers la recherche de beauté et d'équilibre. En amour, tu vis des passions qui te transforment à travers la relation à l'autre. Les plaisirs superficiels sont remplacés par des expériences de beauté profonde.

## Ce que tu pourrais vivre
- Une créativité orientée vers la beauté profonde
- Des amours transformatrices qui passent par l'autre
- Le plaisir de la création harmonieuse
- La mort de relations superficielles

## Conseils pour ce transit
- Crée de la beauté qui transforme
- Vis des relations qui t'aident à grandir
- Trouve l'harmonie dans ce que tu crées et aimes""",

    ('libra', 6): """# ♇ Transit de Pluton en Balance — Maison VI

**En une phrase :** Ton quotidien est transformé par la quête d'équilibre et de relations de travail justes.

## L'énergie du moment
Pluton en Balance dans ta maison du travail quotidien transforme tes routines autour de l'équilibre et de l'équité. Ton environnement de travail doit être harmonieux et tes relations professionnelles justes. Ta santé bénéficie de l'équilibre de vie.

## Ce que tu pourrais vivre
- Un travail transformé vers plus d'harmonie
- Des relations de travail plus équitables
- Une santé liée à l'équilibre général
- La mort de routines déséquilibrées

## Conseils pour ce transit
- Crée un environnement de travail harmonieux
- Établis des relations professionnelles justes
- Trouve l'équilibre entre travail et vie""",

    ('libra', 7): """# ♇ Transit de Pluton en Balance — Maison VII

**En une phrase :** Tes relations traversent une transformation totale vers plus d'équité et d'authenticité.

## L'énergie du moment
Pluton traverse son signe d'exaltation dans ta maison des partenariats, maximisant la transformation relationnelle. Tes relations sont profondément purifiées et transformées. Des déséquilibres de pouvoir sont révélés et corrigés. Tu apprends le vrai partenariat.

## Ce que tu pourrais vivre
- Des transformations majeures dans les relations
- La fin de relations déséquilibrées
- La purification des dynamiques de pouvoir en couple
- L'émergence de partenariats vraiment équitables

## Conseils pour ce transit
- Accepte que certaines relations doivent changer ou finir
- Travaille sur l'équité réelle dans tes partenariats
- Développe une capacité de vraie relation""",

    ('libra', 8): """# ♇ Transit de Pluton en Balance — Maison VIII

**En une phrase :** Des transformations profondes touchent ta façon de fusionner et de partager avec l'autre.

## L'énergie du moment
Pluton en Balance dans ta maison des transformations travaille sur les aspects les plus profonds de tes relations. Les dynamiques de pouvoir dans l'intimité sont révélées et transformées. Tu apprends l'équité dans le partage le plus profond.

## Ce que tu pourrais vivre
- La transformation des dynamiques de pouvoir intimes
- La révélation de déséquilibres dans le partage
- Une intimité purifiée et plus équitable
- La mort de patterns de dépendance ou de domination

## Conseils pour ce transit
- Transforme les déséquilibres de pouvoir intimes
- Apprends le partage vraiment équitable
- Purifie ta façon de fusionner""",

    ('libra', 9): """# ♇ Transit de Pluton en Balance — Maison IX

**En une phrase :** Ta vision du monde est transformée vers une quête de justice et d'équilibre universels.

## L'énergie du moment
Pluton en Balance dans ta maison des horizons lointains transforme tes croyances autour de la justice et de l'équité. Tu développes une philosophie qui cherche l'équilibre et l'harmonie pour tous. Tes voyages peuvent te montrer différentes formes de justice.

## Ce que tu pourrais vivre
- Une transformation des croyances vers la justice
- L'intérêt pour les systèmes de droit et d'équité
- Des voyages vers des lieux qui t'enseignent l'équilibre
- La mort de croyances injustes

## Conseils pour ce transit
- Développe une philosophie de justice et d'équilibre
- Voyage pour comprendre différentes formes d'équité
- Construis une vision qui inclut le bien de tous""",

    ('libra', 10): """# ♇ Transit de Pluton en Balance — Maison X

**En une phrase :** Ta carrière est transformée vers des rôles de médiation, de justice ou de diplomatie.

## L'énergie du moment
Pluton en Balance dans ta maison de la carrière transforme ta trajectoire vers des positions où l'équité et la diplomatie sont centrales. Tu peux acquérir du pouvoir par ta capacité à négocier et à créer l'harmonie. Ta réputation se construit sur ta capacité à équilibrer.

## Ce que tu pourrais vivre
- Une carrière transformée vers la médiation ou le droit
- Le pouvoir acquis par la diplomatie
- Une réputation de personne juste et équilibrée
- Des transformations vers des rôles de partenariat

## Conseils pour ce transit
- Développe ta carrière autour de l'équité
- Utilise ton pouvoir pour créer la justice
- Construis des partenariats professionnels équitables""",

    ('libra', 11): """# ♇ Transit de Pluton en Balance — Maison XI

**En une phrase :** Tes cercles sociaux sont transformés vers des groupes qui œuvrent pour la justice et l'équilibre.

## L'énergie du moment
Pluton en Balance dans ta maison des amitiés transforme tes cercles sociaux autour de la justice et de l'harmonie collective. Tu es attiré par des groupes qui travaillent pour l'équité. Tes aspirations incluent un monde plus juste.

## Ce que tu pourrais vivre
- Des amitiés transformées autour de valeurs de justice
- L'attrait pour des mouvements de justice sociale
- Des aspirations d'équité et d'harmonie collective
- La transformation des groupes vers plus d'équilibre

## Conseils pour ce transit
- Rejoins des groupes qui œuvrent pour la justice
- Contribue à l'harmonie collective
- Aspire à un monde plus équitable""",

    ('libra', 12): """# ♇ Transit de Pluton en Balance — Maison XII

**En une phrase :** Une transformation profonde libère tes patterns inconscients de co-dépendance et de déséquilibre relationnel.

## L'énergie du moment
Pluton en Balance dans ta maison des profondeurs travaille sur tes tendances inconscientes en relation. Des patterns de dépendance, de peur de l'abandon ou de besoin excessif d'harmonie peuvent être révélés et transformés. Tu trouves l'équilibre intérieur.

## Ce que tu pourrais vivre
- La révélation de patterns relationnels inconscients
- La transformation de la co-dépendance profonde
- Des rêves révélant des déséquilibres cachés
- La découverte d'un équilibre qui vient de l'intérieur

## Conseils pour ce transit
- Travaille sur tes patterns relationnels inconscients
- Transforme la dépendance en autonomie reliée
- Trouve l'harmonie en toi-même""",

    # ============================================================
    # PLUTON EN SCORPION (♇ en ♏)
    # ============================================================
    ('scorpio', 1): """# ♇ Transit de Pluton en Scorpion — Maison I

**En une phrase :** Ton identité traverse une transformation totale et irréversible.

## L'énergie du moment
Pluton en Scorpion dans ta maison I est la configuration la plus intense de transformation identitaire. Tu traverses une mort et renaissance complète de qui tu es. Ta puissance personnelle atteint des niveaux extraordinaires après avoir traversé les profondeurs les plus sombres.

## Ce que tu pourrais vivre
- Une transformation identitaire totale et irréversible
- Des crises profondes qui te régénèrent complètement
- L'émergence d'une puissance personnelle considérable
- La confrontation avec tes ombres les plus profondes

## Conseils pour ce transit
- Accepte la mort totale de l'ancien toi
- Embrasse la transformation sans résister
- Deviens la version la plus puissante de toi-même""",

    ('scorpio', 2): """# ♇ Transit de Pluton en Scorpion — Maison II

**En une phrase :** Ta relation aux ressources est transformée au niveau le plus profond.

## L'énergie du moment
Pluton en Scorpion dans ta maison des ressources crée une transformation totale de ta relation à l'argent et aux possessions. Des crises financières majeures peuvent mener à une régénération complète. Tu découvres une richesse qui transcende le matériel.

## Ce que tu pourrais vivre
- Des transformations financières majeures et irréversibles
- La mort d'attachements profonds aux possessions
- La découverte de ressources intérieures insoupçonnées
- Des crises qui révèlent ta vraie relation au pouvoir matériel

## Conseils pour ce transit
- Laisse mourir ce qui doit mourir financièrement
- Découvre la richesse qui ne peut être perdue
- Transforme ta relation au pouvoir de l'argent""",

    ('scorpio', 3): """# ♇ Transit de Pluton en Scorpion — Maison III

**En une phrase :** Ta pensée et ta communication atteignent une profondeur transformatrice maximale.

## L'énergie du moment
Pluton en Scorpion dans ta maison de la communication transforme radicalement ta façon de penser et d'échanger. Tes mots ont un pouvoir de transformation et de révélation exceptionnel. Tu peux percer tous les voiles et communiquer des vérités qui changent tout.

## Ce que tu pourrais vivre
- Une pensée d'une profondeur et d'une puissance extraordinaires
- Des communications qui transforment profondément
- La révélation de secrets et de vérités cachées
- Des transformations majeures avec les proches

## Conseils pour ce transit
- Utilise ton pouvoir de parole avec grande responsabilité
- Transforme par les mots avec compassion
- Perce les illusions tout en respectant le timing""",

    ('scorpio', 4): """# ♇ Transit de Pluton en Scorpion — Maison IV

**En une phrase :** Tes fondations traversent une destruction et reconstruction totale.

## L'énergie du moment
Pluton en Scorpion dans ta maison IV crée une transformation radicale de ta vie familiale et de tes racines. Des secrets familiaux profonds peuvent être révélés. Ta relation à la maison, à la mère, aux ancêtres est complètement transformée. Tu reconstruis sur des bases totalement nouvelles.

## Ce que tu pourrais vivre
- Des bouleversements majeurs de la vie familiale
- La révélation de secrets familiaux profonds
- La reconstruction totale de tes fondations
- La transformation de l'héritage ancestral

## Conseils pour ce transit
- Accueille les révélations comme des libérations
- Reconstruis sur des bases totalement nouvelles
- Transforme l'héritage familial en puissance""",

    ('scorpio', 5): """# ♇ Transit de Pluton en Scorpion — Maison V

**En une phrase :** Ta créativité et tes amours atteignent une intensité transformatrice ultime.

## L'énergie du moment
Pluton en Scorpion dans ta maison de la créativité intensifie tout ce qui concerne l'expression de soi et l'amour. Tu vis des passions dévorantes et transformatrices. Ta créativité explore les profondeurs les plus sombres et les plus lumineuses. Les plaisirs deviennent des expériences de transformation.

## Ce que tu pourrais vivre
- Des passions amoureuses intenses et transformatrices
- Une créativité qui explore les profondeurs extrêmes
- Des expériences de plaisir et de mort symbolique
- La transformation totale à travers ce que tu aimes

## Conseils pour ce transit
- Canalise cette intensité extrême
- Vis les passions comme des initiations complètes
- Transforme-toi radicalement par la création et l'amour""",

    ('scorpio', 6): """# ♇ Transit de Pluton en Scorpion — Maison VI

**En une phrase :** Ton quotidien et ta santé traversent une purification et régénération totale.

## L'énergie du moment
Pluton en Scorpion dans ta maison du travail quotidien transforme radicalement tes routines et ta santé. Des crises de santé peuvent mener à une régénération complète. Ton travail devient un processus de transformation constant. Tu développes des pouvoirs de guérison exceptionnels.

## Ce que tu pourrais vivre
- Des transformations de santé majeures et régénératrices
- Un travail qui devient pratique de transformation
- L'élimination totale de ce qui ne sert plus
- Le développement de capacités de guérison profondes

## Conseils pour ce transit
- Utilise les crises comme opportunités de régénération totale
- Transforme complètement ce qui ne fonctionne plus
- Développe tes pouvoirs de guérison""",

    ('scorpio', 7): """# ♇ Transit de Pluton en Scorpion — Maison VII

**En une phrase :** Tes relations traversent une mort et renaissance complète.

## L'énergie du moment
Pluton en Scorpion dans ta maison des partenariats transforme radicalement tes relations. Des unions peuvent se terminer ou se transformer complètement. Tu attires des partenaires avec qui la transformation mutuelle est totale. Les jeux de pouvoir sont exposés et transcendés.

## Ce que tu pourrais vivre
- Des transformations relationnelles majeures et irréversibles
- Des fins ou renaissances complètes de relations
- Des partenaires avec qui tu te transformes profondément
- La révélation et la transformation des jeux de pouvoir

## Conseils pour ce transit
- Accepte que certaines relations doivent mourir complètement
- Transforme-toi à travers les relations avec courage
- Construis des partenariats sur la transformation mutuelle""",

    ('scorpio', 8): """# ♇ Transit de Pluton en Scorpion — Maison VIII

**En une phrase :** Une transformation ultime touche les aspects les plus profonds de ton existence.

## L'énergie du moment
Pluton traverse sa maison domicile dans son signe domicile, créant la configuration de transformation la plus puissante possible. Tout ce qui concerne la mort, la sexualité, le pouvoir et les ressources partagées est transformé au niveau le plus profond. Des pouvoirs de régénération exceptionnels sont accessibles.

## Ce que tu pourrais vivre
- Des transformations ultimes et irréversibles
- L'accès à des pouvoirs de régénération extraordinaires
- Des expériences de mort et renaissance profondes
- La transformation de ta relation au pouvoir ultime

## Conseils pour ce transit
- Accepte la transformation totale avec confiance
- Utilise tes pouvoirs avec sagesse et éthique
- Traverse les initiations comme un maître""",

    ('scorpio', 9): """# ♇ Transit de Pluton en Scorpion — Maison IX

**En une phrase :** Ta vision du monde est transformée par des révélations profondes sur les mystères de l'existence.

## L'énergie du moment
Pluton en Scorpion dans ta maison des horizons lointains transforme radicalement tes croyances et ta philosophie. Tu explores les mystères les plus profonds de l'existence. Des révélations changent complètement ta vision du monde. Tu peux devenir un transmetteur de vérités profondes.

## Ce que tu pourrais vivre
- Une transformation totale de tes croyances
- Des révélations sur les mystères de la vie et de la mort
- Des voyages vers des lieux de pouvoir transformateur
- L'émergence d'une vision du monde profonde

## Conseils pour ce transit
- Explore les mystères avec courage et discernement
- Voyage vers ce qui te transforme profondément
- Transmets les vérités profondes avec responsabilité""",

    ('scorpio', 10): """# ♇ Transit de Pluton en Scorpion — Maison X

**En une phrase :** Ta carrière et ta place dans le monde sont radicalement transformées.

## L'énergie du moment
Pluton en Scorpion dans ta maison de la carrière transforme totalement ta trajectoire professionnelle. Tu peux atteindre des positions de pouvoir considérable ou traverser des effondrements qui mènent à la reconstruction. Ta réputation est transformée par ta capacité de transformation.

## Ce que tu pourrais vivre
- Des transformations de carrière majeures et irréversibles
- L'accès à des positions de pouvoir ou leur perte transformatrice
- Une réputation basée sur ta capacité de transformation
- Des changements de statut profonds

## Conseils pour ce transit
- Utilise le pouvoir professionnel avec grande éthique
- Accepte les transformations de carrière comme des initiations
- Deviens un agent de transformation dans ton domaine""",

    ('scorpio', 11): """# ♇ Transit de Pluton en Scorpion — Maison XI

**En une phrase :** Tes cercles sociaux et aspirations sont profondément transformés.

## L'énergie du moment
Pluton en Scorpion dans ta maison des amitiés transforme radicalement tes cercles sociaux et tes idéaux. Des amitiés peuvent se terminer ou se transformer profondément. Tes aspirations touchent à la transformation collective profonde.

## Ce que tu pourrais vivre
- Des transformations majeures dans les cercles sociaux
- L'attrait pour des groupes de transformation profonde
- Des aspirations de changement collectif radical
- Des dynamiques de pouvoir révélées dans les groupes

## Conseils pour ce transit
- Laisse les amitiés évoluer ou se terminer naturellement
- Engage-toi dans des causes de transformation authentique
- Aspire à des changements qui comptent vraiment""",

    ('scorpio', 12): """# ♇ Transit de Pluton en Scorpion — Maison XII

**En une phrase :** Une transformation ultime de l'inconscient libère des karmas très anciens.

## L'énergie du moment
Pluton en Scorpion dans ta maison des profondeurs travaille sur les couches les plus anciennes et les plus profondes de ton psychisme. Des karmas très anciens peuvent être purgés. Tu accèdes à des pouvoirs de transformation et de guérison qui dépassent le personnel.

## Ce que tu pourrais vivre
- La libération de karmas très anciens
- L'accès à des pouvoirs de transformation profonds
- Des rêves intenses révélant des vérités ultimes
- La transformation de l'inconscient collectif à travers toi

## Conseils pour ce transit
- Travaille sur ce qui remonte avec grand courage
- Utilise tes pouvoirs de transformation pour le bien collectif
- Deviens un canal de guérison profonde""",
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
        print(f"✅ Transit Pluto (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
