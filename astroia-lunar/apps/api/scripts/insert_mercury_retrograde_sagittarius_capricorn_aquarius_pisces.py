#!/usr/bin/env python3
"""
Insert mercury_retrograde interpretations V2 for Sagittarius, Capricorn, Aquarius, Pisces (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

MERCURY_RETROGRADE_INTERPRETATIONS = {
    # ============== SAGITTARIUS (Sagittaire) ==============
    ('sagittarius', 1): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 1

**En une phrase :** Ta façon de t'exprimer et de te présenter manque peut-être de nuance.

## L'énergie du moment
Mercure rétrograde en Sagittaire dans ta maison 1 peut créer des situations où tes paroles dépassent ta pensée. Ton enthousiasme communicationnel peut mener à des malentendus. C'est le moment de réviser comment tu te présentes au monde.

## Ce que tu pourrais vivre
- Des paroles trop directes qui créent des malentendus
- Un besoin de nuancer ton message personnel
- Des projets personnels trop ambitieux à réviser

## Conseils pour cette période
- Pense avant de parler pour éviter l'excès
- Révise ton image avec plus de réalisme
- L'enthousiasme est bon mais la mesure aussi""",

    ('sagittarius', 2): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 2

**En une phrase :** Tes décisions financières peuvent être trop optimistes et nécessitent une révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec l'optimisme du Sagittaire. Tu peux surestimer tes ressources ou prendre des risques financiers excessifs. C'est le moment de revoir tes finances avec plus de réalisme.

## Ce que tu pourrais vivre
- Des décisions financières trop optimistes
- Des dépenses excessives pour l'aventure ou l'expansion
- Un besoin de réviser ton rapport à l'abondance

## Conseils pour cette période
- Revois ton budget avec réalisme
- Évite les investissements risqués
- L'optimisme financier doit être tempéré par la prudence""",

    ('sagittarius', 3): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 3

**En une phrase :** Tes communications peuvent être trop directes ou philosophiques pour être comprises.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec l'excès du Sagittaire. Tes paroles peuvent être trop philosophiques, trop longues ou trop directes. Les échanges quotidiens peuvent souffrir d'un manque de nuance.

## Ce que tu pourrais vivre
- Des communications qui perdent les gens dans les détails philosophiques
- Des paroles trop directes qui blessent involontairement
- Des malentendus liés à l'excès de confiance

## Conseils pour cette période
- Simplifie et raccourcis tes messages
- La franchise n'exclut pas le tact
- Écoute autant que tu parles""",

    ('sagittarius', 4): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 4

**En une phrase :** Les communications familiales et les projets domestiques peuvent être trop ambitieux.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec l'enthousiasme du Sagittaire. Les projets pour la maison peuvent être trop grands. Les discussions familiales sur les croyances ou les voyages peuvent créer des tensions.

## Ce que tu pourrais vivre
- Des projets domestiques trop ambitieux à réviser
- Des débats philosophiques dans la famille
- Un besoin de plus d'espace ou de mouvement à la maison

## Conseils pour cette période
- Revois tes projets de maison avec réalisme
- Les débats familiaux ne valent pas toujours la peine
- Trouve la liberté dans ton espace, pas loin de lui""",

    ('sagittarius', 5): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 5

**En une phrase :** Les communications romantiques et créatives peuvent promettre plus qu'elles ne peuvent tenir.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec l'excès du Sagittaire. Les promesses romantiques peuvent être trop grandes. Les projets créatifs peuvent être trop ambitieux pour être réalisés maintenant.

## Ce que tu pourrais vivre
- Des déclarations amoureuses excessives ou prématurées
- Des projets créatifs qui nécessitent d'être réduits en taille
- Le retour d'ex avec de grandes promesses

## Conseils pour cette période
- En amour, promets moins, fais plus
- Tes créations gagnent à être finies plutôt qu'élargies
- Les ex qui reviennent avec de grandes promesses : prudence""",

    ('sagittarius', 6): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 6

**En une phrase :** Les routines et le travail quotidien peuvent souffrir d'un manque de concentration.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec l'agitation du Sagittaire. Tu peux avoir du mal à te concentrer sur les détails. Les routines peuvent sembler étouffantes et tu veux t'échapper.

## Ce que tu pourrais vivre
- Des erreurs au travail dues au manque de focus
- Une difficulté à supporter la routine
- Des promesses de productivité non tenues

## Conseils pour cette période
- Force-toi à rester concentré·e sur les détails
- Les routines sont nécessaires même si elles semblent limitantes
- Finis ce que tu commences avant de passer à autre chose""",

    ('sagittarius', 7): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 7

**En une phrase :** Les communications relationnelles peuvent être trop franches ou promettre trop.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec la franchise du Sagittaire. Les discussions de couple peuvent être trop directes. Les contrats et accords peuvent contenir des promesses irréalistes.

## Ce que tu pourrais vivre
- Des paroles trop directes qui blessent le partenaire
- Des engagements ou contrats trop ambitieux
- Le retour d'ex avec des projets d'aventure

## Conseils pour cette période
- La franchise doit être tempérée par la gentillesse
- Relis tous les contrats avec un œil réaliste
- Les grandes promesses relationnelles méritent du temps""",

    ('sagittarius', 8): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 8

**En une phrase :** Les communications sur les finances partagées et les sujets profonds peuvent être trop légères.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec l'optimisme du Sagittaire. Tu peux sous-estimer la complexité des questions financières partagées. Les sujets profonds peuvent être traités trop superficiellement.

## Ce que tu pourrais vivre
- Des arrangements financiers partagés à réviser
- Une tendance à minimiser la profondeur des enjeux
- Des discussions profondes qui restent en surface

## Conseils pour cette période
- Les finances partagées méritent plus de sérieux
- Ne minimise pas les sujets importants
- La profondeur demande du temps""",

    ('sagittarius', 9): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 9

**En une phrase :** Tes voyages et tes grandes idées sont en profonde révision.

## L'énergie du moment
Mercure rétrograde est très significatif en Sagittaire dans la maison 9, son domaine. Tous les aspects de tes voyages, de tes études supérieures, de tes croyances sont à revoir. C'est le moment de réviser et non d'étendre.

## Ce que tu pourrais vivre
- Des plans de voyage qui se compliquent
- Des projets académiques ou éditoriaux qui nécessitent des révisions
- Une remise en question de tes croyances

## Conseils pour cette période
- Confirme et reconfirme tous les détails de voyage
- Révise tes projets d'étude ou de publication
- C'est le temps de réfléchir plutôt que d'étendre""",

    ('sagittarius', 10): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 10

**En une phrase :** Les communications professionnelles peuvent promettre trop ou manquer de réalisme.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec l'optimisme du Sagittaire. Tu peux faire des promesses professionnelles difficiles à tenir. Les projets de carrière peuvent être trop ambitieux.

## Ce que tu pourrais vivre
- Des engagements professionnels trop ambitieux
- Des communications qui promettent trop
- Un besoin de revoir tes objectifs de carrière

## Conseils pour cette période
- Promets moins au travail, livre plus
- Revois tes objectifs de carrière avec réalisme
- La réputation se bâtit sur la fiabilité, pas sur les promesses""",

    ('sagittarius', 11): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 11

**En une phrase :** Les communications dans les groupes peuvent être trop enthousiastes ou idéalistes.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec l'enthousiasme du Sagittaire. Les projets de groupe peuvent être trop ambitieux. Les communications avec les amis peuvent être trop directes ou trop philosophiques.

## Ce que tu pourrais vivre
- Des projets collectifs trop ambitieux à réviser
- Des débats avec les amis qui s'enflamment
- Un besoin de revoir tes idéaux et tes espoirs

## Conseils pour cette période
- Les projets de groupe gagnent à être plus modestes
- Évite les débats philosophiques avec les amis
- L'idéalisme mérite d'être tempéré par le réalisme""",

    ('sagittarius', 12): """# ☿℞ Mercure rétrograde en Sagittaire — Maison 12

**En une phrase :** Tes grandes croyances inconscientes et ta quête de sens intérieure sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec l'énergie expansive du Sagittaire. Tu peux reconsidérer tes croyances profondes. Les rêves peuvent être porteurs de messages spirituels. C'est un temps de quête intérieure.

## Ce que tu pourrais vivre
- Une remise en question de tes croyances profondes
- Des rêves à thème spirituel ou philosophique
- Un besoin de retraite et de réflexion

## Conseils pour cette période
- Les grandes questions méritent du temps de réflexion
- Les rêves peuvent être des guides spirituels
- La retraite intérieure est favorable""",

    # ============== CAPRICORN (Capricorne) ==============
    ('capricorn', 1): """# ☿℞ Mercure rétrograde en Capricorne — Maison 1

**En une phrase :** Ta façon de te présenter et de communiquer professionnellement est à réviser.

## L'énergie du moment
Mercure rétrograde en Capricorne dans ta maison 1 met en lumière ta communication professionnelle et ta présentation sérieuse. Tu peux paraître trop rigide ou froid·e. C'est le moment de réviser ton image avec plus de chaleur.

## Ce que tu pourrais vivre
- Une image qui paraît trop froide ou distante
- Des communications personnelles trop formelles
- Un besoin de réviser ta présentation

## Conseils pour cette période
- Ajoute de la chaleur à ta communication
- Le sérieux ne doit pas exclure l'accessibilité
- Révise ton image pour plus d'authenticité""",

    ('capricorn', 2): """# ☿℞ Mercure rétrograde en Capricorne — Maison 2

**En une phrase :** Tes structures financières et ta relation à la sécurité matérielle sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec la rigueur du Capricorne. C'est le moment idéal pour réviser tes structures financières, tes plans à long terme, tes investissements. La patience est de mise.

## Ce que tu pourrais vivre
- Des retards dans les projets financiers à long terme
- Un besoin de réviser tes plans d'investissement
- Des communications sur l'argent qui demandent de la patience

## Conseils pour cette période
- Revois tes structures financières avec soin
- La patience est ta meilleure alliée financière
- Les plans à long terme méritent d'être réexaminés""",

    ('capricorn', 3): """# ☿℞ Mercure rétrograde en Capricorne — Maison 3

**En une phrase :** Tes communications quotidiennes peuvent être trop formelles ou rigides.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec le sérieux du Capricorne. Tes messages peuvent paraître trop formels ou froids. Les échanges avec l'entourage proche peuvent manquer de légèreté.

## Ce que tu pourrais vivre
- Des communications trop formelles ou distantes
- Des malentendus liés au ton trop sérieux
- Un besoin de réviser ta façon de t'exprimer

## Conseils pour cette période
- Assouplit ta façon de communiquer
- La légèreté n'est pas incompatible avec le sérieux
- Prends le temps de vraiment écouter""",

    ('capricorn', 4): """# ☿℞ Mercure rétrograde en Capricorne — Maison 4

**En une phrase :** Les structures familiales et les responsabilités domestiques sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec la structure du Capricorne. Les responsabilités familiales peuvent sembler plus lourdes. Les discussions sur les traditions ou les obligations familiales sont à revoir.

## Ce que tu pourrais vivre
- Des responsabilités familiales qui se compliquent
- Des discussions sur les structures et les traditions du foyer
- Un besoin de réviser les règles de la maison

## Conseils pour cette période
- Les responsabilités méritent d'être réévaluées
- Les traditions familiales peuvent évoluer
- Allège les structures trop rigides""",

    ('capricorn', 5): """# ☿℞ Mercure rétrograde en Capricorne — Maison 5

**En une phrase :** Les plaisirs et la créativité peuvent sembler trop sérieux ou contrôlés.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec le contrôle du Capricorne. La spontanéité en amour ou dans la créativité peut être difficile. Les expressions de joie peuvent sembler forcées.

## Ce que tu pourrais vivre
- Une difficulté à lâcher prise dans les plaisirs
- Une créativité qui semble trop calculée
- Des communications amoureuses trop sérieuses

## Conseils pour cette période
- Permets-toi plus de spontanéité
- La créativité n'a pas besoin d'être parfaite
- L'amour gagne à être plus léger""",

    ('capricorn', 6): """# ☿℞ Mercure rétrograde en Capricorne — Maison 6

**En une phrase :** Les routines de travail et les systèmes du quotidien sont en révision approfondie.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec la structure du Capricorne. C'est le moment idéal pour réviser les systèmes de travail, les processus, les routines. La patience avec les retards est nécessaire.

## Ce que tu pourrais vivre
- Des systèmes de travail qui nécessitent des révisions
- Des retards dans les processus habituels
- Un besoin d'améliorer les structures du quotidien

## Conseils pour cette période
- Revois tes systèmes et processus de travail
- La patience avec les retards est essentielle
- Améliore les structures plutôt que d'en créer de nouvelles""",

    ('capricorn', 7): """# ☿℞ Mercure rétrograde en Capricorne — Maison 7

**En une phrase :** Les structures relationnelles et les engagements à long terme sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec le sérieux du Capricorne. Les engagements à long terme sont à revoir. Les communications de couple peuvent être trop formelles ou axées sur les responsabilités.

## Ce que tu pourrais vivre
- Des discussions sur les engagements à long terme
- Des contrats et accords qui nécessitent des révisions
- Des communications de couple trop axées sur le devoir

## Conseils pour cette période
- Revois les engagements et les contrats avec soin
- L'amour inclut aussi la légèreté, pas juste le devoir
- Les structures relationnelles peuvent être assouplies""",

    ('capricorn', 8): """# ☿℞ Mercure rétrograde en Capricorne — Maison 8

**En une phrase :** Les structures financières complexes et les transformations profondes demandent de la patience.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec la prudence du Capricorne. Les questions financières complexes demandent une révision minutieuse. Les transformations prennent plus de temps que prévu.

## Ce que tu pourrais vivre
- Des procédures financières complexes qui se ralentissent
- Des transformations qui demandent plus de patience
- Un besoin de réviser les structures partagées

## Conseils pour cette période
- La patience est essentielle dans les affaires complexes
- Les transformations ne peuvent pas être forcées
- Revois les structures avec soin et rigueur""",

    ('capricorn', 9): """# ☿℞ Mercure rétrograde en Capricorne — Maison 9

**En une phrase :** Les voyages professionnels et les formations structurées sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec la structure du Capricorne. Les voyages professionnels peuvent être retardés. Les formations ou certifications peuvent nécessiter des révisions.

## Ce que tu pourrais vivre
- Des voyages professionnels qui se compliquent
- Des formations ou certifications à réviser
- Un besoin de structurer tes croyances et connaissances

## Conseils pour cette période
- Vérifie tous les détails des voyages professionnels
- Révise tes plans de formation
- La sagesse inclut la structure et la flexibilité""",

    ('capricorn', 10): """# ☿℞ Mercure rétrograde en Capricorne — Maison 10

**En une phrase :** Ta carrière et tes structures professionnelles sont en révision profonde.

## L'énergie du moment
Mercure rétrograde est très significatif en Capricorne dans la maison 10, domaine de la carrière. Tous les aspects de ta vie professionnelle sont à revoir. C'est le moment de réviser tes objectifs et tes méthodes.

## Ce que tu pourrais vivre
- Des projets professionnels qui nécessitent des révisions
- Des communications avec la hiérarchie qui demandent du soin
- Un besoin de reconsidérer ta direction de carrière

## Conseils pour cette période
- Revois tes objectifs professionnels avec soin
- Les communications officielles méritent une attention maximale
- C'est le temps de consolider plutôt que d'avancer""",

    ('capricorn', 11): """# ☿℞ Mercure rétrograde en Capricorne — Maison 11

**En une phrase :** Les structures des projets de groupe et les objectifs à long terme sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec la structure du Capricorne. Les projets collectifs à long terme nécessitent des révisions. Les communications dans les groupes peuvent être trop formelles.

## Ce que tu pourrais vivre
- Des projets de groupe qui nécessitent d'être restructurés
- Des communications avec les amis trop axées sur les obligations
- Un besoin de revoir tes objectifs à long terme

## Conseils pour cette période
- Revois les structures des projets collectifs
- L'amitié inclut aussi la détente, pas juste les projets
- Tes objectifs à long terme méritent d'être reconsidérés""",

    ('capricorn', 12): """# ☿℞ Mercure rétrograde en Capricorne — Maison 12

**En une phrase :** Tes structures intérieures et tes limites inconscientes sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec le contrôle du Capricorne. Tes structures mentales profondes sont à réviser. Les limitations que tu t'imposes inconsciemment peuvent être vues.

## Ce que tu pourrais vivre
- Des prises de conscience sur tes auto-limitations
- Des structures mentales rigides qui sont révélées
- Un besoin de relâcher le contrôle intérieur

## Conseils pour cette période
- Examine les structures que tu t'imposes
- Le contrôle excessif a des racines profondes
- Le relâchement peut être thérapeutique""",

    # ============== AQUARIUS (Verseau) ==============
    ('aquarius', 1): """# ☿℞ Mercure rétrograde en Verseau — Maison 1

**En une phrase :** Ta façon originale de communiquer et de te présenter est à réviser.

## L'énergie du moment
Mercure rétrograde en Verseau dans ta maison 1 remet en question ton originalité communicationnelle. Ta différence peut créer des malentendus. C'est le moment de revoir comment ton unicité est perçue.

## Ce que tu pourrais vivre
- Des malentendus liés à ta façon unique de t'exprimer
- Un besoin de réviser ton image originale
- Des réactions inattendues à ta communication

## Conseils pour cette période
- L'originalité est précieuse mais doit être comprise
- Révise comment tu présentes ta différence
- Être compris·e est aussi important qu'être unique""",

    ('aquarius', 2): """# ☿℞ Mercure rétrograde en Verseau — Maison 2

**En une phrase :** Tes idées innovantes sur l'argent et les valeurs sont à réviser.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec l'innovation du Verseau. Tes approches non conventionnelles des finances peuvent ne pas fonctionner comme prévu. Les technologies financières peuvent dysfonctionner.

## Ce que tu pourrais vivre
- Des systèmes financiers innovants qui buguent
- Des idées non conventionnelles sur l'argent à revoir
- Des problèmes avec les technologies de paiement

## Conseils pour cette période
- Vérifie tes systèmes financiers technologiques
- Les approches innovantes méritent des tests
- Garde des solutions de secours classiques""",

    ('aquarius', 3): """# ☿℞ Mercure rétrograde en Verseau — Maison 3

**En une phrase :** Tes communications innovantes et tes technologies sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec l'énergie technologique du Verseau. Tous les appareils de communication peuvent dysfonctionner. Tes idées originales peuvent être mal comprises.

## Ce que tu pourrais vivre
- Des problèmes technologiques avec les communications
- Des idées innovantes qui sont mal comprises
- Un besoin de simplifier ta façon de communiquer

## Conseils pour cette période
- Sauvegarde tes données et prépare des plans B
- Simplifie tes messages pour être mieux compris·e
- Les technologies demandent des vérifications""",

    ('aquarius', 4): """# ☿℞ Mercure rétrograde en Verseau — Maison 4

**En une phrase :** Les technologies du foyer et les arrangements familiaux non conventionnels sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec l'innovation du Verseau. Les systèmes domotiques peuvent dysfonctionner. Les arrangements familiaux non traditionnels peuvent nécessiter des ajustements.

## Ce que tu pourrais vivre
- Des technologies de maison intelligente qui buguent
- Des arrangements familiaux non conventionnels à revoir
- Un besoin de simplifier la technologie à la maison

## Conseils pour cette période
- Vérifie les systèmes technologiques de ta maison
- Les arrangements familiaux méritent d'être réévalués
- La simplicité peut être bienvenue""",

    ('aquarius', 5): """# ☿℞ Mercure rétrograde en Verseau — Maison 5

**En une phrase :** Les approches originales de l'amour et de la créativité sont à réviser.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec l'originalité du Verseau. Les approches non conventionnelles de l'amour peuvent créer de la confusion. Les projets créatifs innovants peuvent nécessiter des révisions.

## Ce que tu pourrais vivre
- Des communications amoureuses trop détachées ou inhabituelles
- Des projets créatifs innovants qui nécessitent des ajustements
- Le retour d'ex non conventionnels

## Conseils pour cette période
- L'originalité en amour doit aussi inclure la connexion
- Tes créations innovantes méritent d'être peaufinées
- Les relations inhabituelles méritent de la réflexion""",

    ('aquarius', 6): """# ☿℞ Mercure rétrograde en Verseau — Maison 6

**En une phrase :** Les technologies au travail et les approches innovantes du quotidien sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec l'innovation du Verseau. Les systèmes technologiques au travail peuvent dysfonctionner. Les approches non conventionnelles de la santé peuvent nécessiter des révisions.

## Ce que tu pourrais vivre
- Des bugs technologiques au travail
- Des méthodes de travail innovantes qui ne fonctionnent pas
- Des approches alternatives de santé à reconsidérer

## Conseils pour cette période
- Sauvegarde et vérifie tous les systèmes de travail
- Garde des méthodes traditionnelles en réserve
- Les innovations santé méritent d'être testées prudemment""",

    ('aquarius', 7): """# ☿℞ Mercure rétrograde en Verseau — Maison 7

**En une phrase :** Les approches non conventionnelles des relations et les contrats innovants sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec la liberté du Verseau. Les arrangements relationnels non conventionnels peuvent créer de la confusion. Les contrats utilisant de nouvelles technologies méritent attention.

## Ce que tu pourrais vivre
- De la confusion dans les arrangements relationnels inhabituels
- Des contrats électroniques qui posent des problèmes
- Le retour d'ex avec des propositions non conventionnelles

## Conseils pour cette période
- Clarifie les arrangements relationnels non traditionnels
- Vérifie les aspects technologiques des contrats
- L'innovation relationnelle demande de la communication""",

    ('aquarius', 8): """# ☿℞ Mercure rétrograde en Verseau — Maison 8

**En une phrase :** Les technologies financières et les approches innovantes des transformations sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec l'innovation du Verseau. Les cryptomonnaies et autres technologies financières peuvent être problématiques. Les approches non conventionnelles du changement méritent d'être reconsidérées.

## Ce que tu pourrais vivre
- Des problèmes avec les technologies financières avancées
- Des approches innovantes de transformation qui ne fonctionnent pas
- Un besoin de réviser les systèmes partagés

## Conseils pour cette période
- Sois prudent·e avec les technologies financières
- Les transformations demandent parfois des approches classiques
- Vérifie tous les systèmes partagés""",

    ('aquarius', 9): """# ☿℞ Mercure rétrograde en Verseau — Maison 9

**En une phrase :** Les voyages technologiques et les idées révolutionnaires sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec l'innovation du Verseau. Les voyages utilisant beaucoup de technologie peuvent se compliquer. Les idées révolutionnaires peuvent nécessiter d'être reconsidérées.

## Ce que tu pourrais vivre
- Des problèmes technologiques pendant les voyages
- Des idées novatrices qui nécessitent des ajustements
- Un besoin de réviser tes croyances non conventionnelles

## Conseils pour cette période
- Aie des solutions de secours non technologiques pour tes voyages
- Les idées révolutionnaires méritent d'être testées
- La sagesse ancienne peut compléter l'innovation""",

    ('aquarius', 10): """# ☿℞ Mercure rétrograde en Verseau — Maison 10

**En une phrase :** Les technologies professionnelles et les approches de carrière innovantes sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec l'innovation du Verseau. Les systèmes technologiques professionnels peuvent dysfonctionner. Les approches de carrière non conventionnelles peuvent nécessiter des ajustements.

## Ce que tu pourrais vivre
- Des bugs dans les systèmes professionnels
- Des stratégies de carrière innovantes qui ne fonctionnent pas comme prévu
- Un besoin de réviser ton image professionnelle unique

## Conseils pour cette période
- Sauvegarde et vérifie tous les systèmes professionnels
- Les approches classiques ont aussi leur valeur
- Ton originalité professionnelle mérite d'être bien présentée""",

    ('aquarius', 11): """# ☿℞ Mercure rétrograde en Verseau — Maison 11

**En une phrase :** Les réseaux sociaux et les projets collectifs innovants sont en révision profonde.

## L'énergie du moment
Mercure rétrograde est très significatif en Verseau dans la maison 11, domaine des groupes et des idéaux. Tous les aspects de tes réseaux et de tes projets collectifs sont à revoir. Les technologies sociales peuvent dysfonctionner.

## Ce que tu pourrais vivre
- Des problèmes avec les réseaux sociaux et les technologies de groupe
- Des projets collectifs innovants qui nécessitent des révisions
- Un besoin de reconsidérer tes idéaux et tes objectifs

## Conseils pour cette période
- Vérifie tous les systèmes de communication de groupe
- Les projets innovants méritent d'être révisés
- Reconsidère tes idéaux avec réalisme""",

    ('aquarius', 12): """# ☿℞ Mercure rétrograde en Verseau — Maison 12

**En une phrase :** Tes pensées non conventionnelles et tes fuites technologiques sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec l'innovation du Verseau. Des pensées inhabituelles peuvent émerger de l'inconscient. La tendance à fuir dans le virtuel peut être révélée.

## Ce que tu pourrais vivre
- Des idées bizarres ou futuristes qui émergent
- Une prise de conscience de ta dépendance technologique
- Des rêves à thème futuriste ou technologique

## Conseils pour cette période
- Les idées inhabituelles méritent d'être notées
- Examine ta relation à la technologie
- Le monde intérieur a ses propres innovations""",

    # ============== PISCES (Poissons) ==============
    ('pisces', 1): """# ☿℞ Mercure rétrograde en Poissons — Maison 1

**En une phrase :** Ta façon de communiquer peut être floue ou mal comprise.

## L'énergie du moment
Mercure rétrograde en Poissons dans ta maison 1 peut rendre tes communications très floues. Ce que tu dis peut être mal interprété. C'est le moment de clarifier ton message personnel et ton image.

## Ce que tu pourrais vivre
- Des communications personnelles confuses ou vagues
- Une image floue ou mal comprise par les autres
- Un besoin de clarifier ce que tu veux vraiment dire

## Conseils pour cette période
- Sois plus direct·e et clair·e dans tes communications
- Vérifie que les autres t'ont bien compris·e
- Ton image peut nécessiter une clarification""",

    ('pisces', 2): """# ☿℞ Mercure rétrograde en Poissons — Maison 2

**En une phrase :** Tes finances peuvent être confuses et les limites floues.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec la confusion des Poissons. Les limites financières peuvent être floues. L'argent peut fuir de façon invisible. Les communications sur l'argent peuvent être mal comprises.

## Ce que tu pourrais vivre
- De la confusion sur tes finances
- Des dépenses qui passent inaperçues
- Des malentendus sur les questions d'argent

## Conseils pour cette période
- Vérifie tes comptes régulièrement
- Clarifie toutes les transactions
- Les limites financières ont besoin d'être définies clairement""",

    ('pisces', 3): """# ☿℞ Mercure rétrograde en Poissons — Maison 3

**En une phrase :** Toutes tes communications peuvent être teintées de confusion ou de malentendu.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec le flou des Poissons. Les messages peuvent être mal compris de façon spectaculaire. Les communications importantes peuvent se perdre. La confusion dans les échanges quotidiens est probable.

## Ce que tu pourrais vivre
- Des messages importants qui se perdent ou sont mal compris
- Des communications pleines de malentendus
- Une confusion dans les échanges quotidiens

## Conseils pour cette période
- Confirme que tes messages ont été reçus et compris
- Sois le plus clair·e possible dans tes communications
- Les malentendus nécessitent des clarifications patientes""",

    ('pisces', 4): """# ☿℞ Mercure rétrograde en Poissons — Maison 4

**En une phrase :** Les communications familiales et les frontières du foyer peuvent être confuses.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec la dissolution des Poissons. Les limites familiales peuvent être floues. Les communications avec la famille peuvent être confuses. Des souvenirs vagues ou des malentendus anciens peuvent refaire surface.

## Ce que tu pourrais vivre
- De la confusion dans les communications familiales
- Des frontières floues à la maison
- Des souvenirs du passé qui reviennent de façon confuse

## Conseils pour cette période
- Clarifie les communications avec la famille
- Établis des limites claires même avec les proches
- Les souvenirs confus peuvent être clarifiés""",

    ('pisces', 5): """# ☿℞ Mercure rétrograde en Poissons — Maison 5

**En une phrase :** Les communications romantiques et créatives peuvent être très confuses.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec le romantisme confus des Poissons. Les messages amoureux peuvent être mal interprétés de façon dramatique. La créativité est inspirée mais peut manquer de clarté.

## Ce que tu pourrais vivre
- Des malentendus romantiques significatifs
- Une créativité inspirée mais floue
- Le retour d'ex avec des messages confus

## Conseils pour cette période
- Clarifie tes intentions amoureuses explicitement
- Canalise la créativité inspirée avec structure
- Les ex qui reviennent peuvent apporter de la confusion""",

    ('pisces', 6): """# ☿℞ Mercure rétrograde en Poissons — Maison 6

**En une phrase :** Le travail quotidien et les routines de santé peuvent manquer de clarté.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec le flou des Poissons. Les tâches au travail peuvent être confuses. Les diagnostics de santé peuvent être incertains. Les routines peuvent se dissoudre.

## Ce que tu pourrais vivre
- De la confusion sur les tâches de travail
- Des questions de santé difficiles à diagnostiquer
- Des routines qui se dissolvent

## Conseils pour cette période
- Demande des clarifications au travail
- Les questions de santé méritent un deuxième avis
- Maintiens une structure même si c'est difficile""",

    ('pisces', 7): """# ☿℞ Mercure rétrograde en Poissons — Maison 7

**En une phrase :** Les communications relationnelles peuvent être très confuses et idéalisées.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec le romantisme des Poissons. Les communications de couple peuvent être teintées d'idéalisation ou de confusion. Les contrats peuvent contenir des zones floues.

## Ce que tu pourrais vivre
- Des malentendus romantiques significatifs
- Des contrats avec des clauses confuses
- Le retour d'ex idéalisés

## Conseils pour cette période
- Clarifie les communications avec ton partenaire
- Lis tous les contrats avec grande attention aux détails
- Les retours d'ex peuvent être basés sur l'idéalisation""",

    ('pisces', 8): """# ☿℞ Mercure rétrograde en Poissons — Maison 8

**En une phrase :** Les communications sur les finances partagées et les sujets profonds peuvent être très confuses.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec la dissolution des Poissons. Les questions financières partagées peuvent être particulièrement confuses. Les limites dans l'intimité peuvent être floues.

## Ce que tu pourrais vivre
- Une grande confusion sur les finances partagées
- Des limites floues dans l'intimité
- Des communications sur des sujets profonds qui se perdent

## Conseils pour cette période
- Documente tout ce qui concerne les finances partagées
- Les limites sont importantes même dans l'intimité
- Les sujets profonds méritent de la clarté""",

    ('pisces', 9): """# ☿℞ Mercure rétrograde en Poissons — Maison 9

**En une phrase :** Les voyages et les croyances peuvent être sources de confusion mais aussi d'inspiration.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec la spiritualité des Poissons. Les voyages peuvent être perturbés par des confusions. Les croyances peuvent être remises en question ou approfondies.

## Ce que tu pourrais vivre
- Des voyages pleins de complications et de confusions
- Une remise en question de tes croyances spirituelles
- Des insights spirituels mêlés de confusion

## Conseils pour cette période
- Vérifie tous les détails de voyage plusieurs fois
- La confusion spirituelle peut précéder la clarté
- Accepte de ne pas tout comprendre maintenant""",

    ('pisces', 10): """# ☿℞ Mercure rétrograde en Poissons — Maison 10

**En une phrase :** Les communications professionnelles peuvent être confuses et ta réputation floue.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec la confusion des Poissons. Tes communications professionnelles peuvent être mal comprises. Ta réputation peut être affectée par des malentendus.

## Ce que tu pourrais vivre
- Des communications professionnelles confuses
- Une réputation affectée par des malentendus
- Une direction de carrière qui semble floue

## Conseils pour cette période
- Sois particulièrement clair·e dans les communications officielles
- Corrige les malentendus professionnels rapidement
- C'est le moment de clarifier ta vision de carrière""",

    ('pisces', 11): """# ☿℞ Mercure rétrograde en Poissons — Maison 11

**En une phrase :** Les communications dans les groupes et les idéaux peuvent être sources de confusion.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec le flou des Poissons. Les communications dans les groupes peuvent être confuses. Les idéaux peuvent sembler nébuleux. Les amitiés peuvent être teintées d'idéalisation.

## Ce que tu pourrais vivre
- De la confusion dans les communications de groupe
- Des idéaux flous ou changeants
- Des amitiés basées sur l'idéalisation

## Conseils pour cette période
- Clarifie les communications dans les groupes
- Les idéaux méritent d'être définis clairement
- Les vraies amitiés survivent au delà de l'idéalisation""",

    ('pisces', 12): """# ☿℞ Mercure rétrograde en Poissons — Maison 12

**En une phrase :** Ton inconscient est très actif et les frontières mentales sont dissoutes.

## L'énergie du moment
Mercure rétrograde est très puissant en Poissons dans la maison 12. Les pensées inconscientes affluent. Les rêves sont très significatifs. Les frontières entre conscient et inconscient sont floues. C'est un temps d'immersion intérieure.

## Ce que tu pourrais vivre
- Des pensées et des images qui affluent de l'inconscient
- Des rêves très significatifs et prophétiques
- Une confusion entre imagination et réalité

## Conseils pour cette période
- Note tes rêves et tes intuitions
- L'introspection est particulièrement puissante
- Garde un ancrage dans la réalité quotidienne""",
}

async def insert_interpretations():
    """Insert all mercury_retrograde interpretations for Sagittarius, Capricorn, Aquarius, Pisces"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in MERCURY_RETROGRADE_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'mercury_retrograde',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP: mercury_retrograde {sign} house {house} already exists")
                skipped += 1
                continue

            interpretation = PregeneratedNatalInterpretation(
                subject='mercury_retrograde',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interpretation)
            print(f"INSERT: mercury_retrograde {sign} house {house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nDone: {inserted} inserted, {skipped} skipped")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
