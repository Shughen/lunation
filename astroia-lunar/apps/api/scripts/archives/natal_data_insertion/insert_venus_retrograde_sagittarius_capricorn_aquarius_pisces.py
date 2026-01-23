#!/usr/bin/env python3
"""
Insert venus_retrograde interpretations V2 for Sagittarius, Capricorn, Aquarius, Pisces (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

VENUS_RETROGRADE_INTERPRETATIONS = {
    # ============== SAGITTARIUS (Sagittaire) ==============
    ('sagittarius', 1): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 1

**En une phrase :** Ta façon aventureuse de séduire et ton image de libre penseur·se sont en révision.

## L'énergie du moment
Vénus rétrograde en Sagittaire dans ta maison 1 remet en question ta façon libre et aventureuse de te présenter. Tu as peut-être promis plus que tu ne pouvais tenir. C'est le moment de réviser ton image avec plus de réalisme.

## Ce que tu pourrais vivre
- Une révision de ton image d'aventurier·e
- Des promesses relationnelles trop grandes à reconsidérer
- Un retour à une présentation plus réaliste

## Conseils pour cette période
- L'aventure et la constance peuvent coexister
- Les promesses méritent d'être tenues
- Ton image gagne en authenticité""",

    ('sagittarius', 2): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 2

**En une phrase :** Tes dépenses d'aventure et tes valeurs d'expansion sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec l'optimisme du Sagittaire. Les dépenses pour les voyages, l'éducation ou l'expansion sont à reconsidérer. Tes valeurs liées à la liberté méritent d'être examinées.

## Ce que tu pourrais vivre
- Des dépenses d'aventure qui dépassent les moyens
- Des questions sur les valeurs de liberté et d'expansion
- Un besoin de réviser le rapport argent-aventure

## Conseils pour cette période
- L'aventure n'a pas besoin d'être coûteuse
- La vraie liberté inclut la responsabilité
- Les valeurs d'expansion peuvent être équilibrées""",

    ('sagittarius', 3): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 3

**En une phrase :** Tes communications enthousiastes et tes promesses verbales sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec l'enthousiasme du Sagittaire. Tes paroles peuvent avoir promis plus que le réaliste. Les communications charmantes mais exagérées sont à reconsidérer.

## Ce que tu pourrais vivre
- Une révision des promesses verbales excessives
- Des communications enthousiastes à tempérer
- Un besoin de plus de constance dans les échanges

## Conseils pour cette période
- Les paroles engagent : mesure-les
- L'enthousiasme peut être tempéré par la réflexion
- La constance en communication construit la confiance""",

    ('sagittarius', 4): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 4

**En une phrase :** L'ambiance libre au foyer et les projets domestiques d'expansion sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec l'expansion du Sagittaire. Les projets de maison trop ambitieux sont à reconsidérer. L'équilibre entre liberté et enracinement au foyer mérite attention.

## Ce que tu pourrais vivre
- Des projets domestiques trop grands à revoir
- Des questions sur la liberté vs l'enracinement
- Un besoin de stabilité au foyer

## Conseils pour cette période
- Les grands projets de maison peuvent attendre
- La liberté intérieure ne contredit pas l'enracinement
- Le foyer peut être un lieu de départ et de retour""",

    ('sagittarius', 5): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 5

**En une phrase :** Les amours aventureux et la créativité d'exploration sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec l'aventure du Sagittaire. Les relations amoureuses basées sur l'aventure plus que sur l'engagement sont à réviser. La créativité d'exploration mérite d'être finalisée.

## Ce que tu pourrais vivre
- Une révision des amours aventureux mais éphémères
- Des créations exploratoires à terminer
- Le retour d'ex avec qui l'aventure primait sur l'engagement

## Conseils pour cette période
- L'amour peut être aventure ET engagement
- Les créations méritent d'être finies, pas juste commencées
- Les ex aventuriers ont des leçons sur la constance""",

    ('sagittarius', 6): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 6

**En une phrase :** Les routines trop libres et les relations de travail sans engagement sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec le besoin de liberté du Sagittaire. Les routines trop peu structurées sont à reconsidérer. Les relations de travail sans engagement réel méritent attention.

## Ce que tu pourrais vivre
- Une révision des routines trop libres
- Des relations de travail peu engagées à reconsidérer
- Un besoin de plus de structure dans le quotidien

## Conseils pour cette période
- La liberté quotidienne a besoin de cadre
- L'engagement au travail construit la réputation
- Les routines peuvent être libres ET efficaces""",

    ('sagittarius', 7): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 7

**En une phrase :** Les relations basées sur la liberté et les partenariats d'aventure sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec l'indépendance du Sagittaire. Les relations où la liberté prime sur l'engagement sont à réviser. Les partenariats d'aventure méritent plus de profondeur.

## Ce que tu pourrais vivre
- Une révision des relations trop libres
- Des partenariats d'aventure qui manquent de profondeur
- Le retour d'ex avec qui la liberté était centrale

## Conseils pour cette période
- La liberté en couple demande aussi de l'engagement
- Les partenariats gagnent en profondeur
- Les ex libres ont des leçons sur l'équilibre""",

    ('sagittarius', 8): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 8

**En une phrase :** L'intimité légère et les finances partagées optimistes sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec l'optimisme du Sagittaire. L'intimité peut avoir manqué de profondeur. Les arrangements financiers partagés trop optimistes sont à reconsidérer.

## Ce que tu pourrais vivre
- Une révision de l'intimité superficielle
- Des arrangements financiers optimistes à revoir
- Un besoin de plus de profondeur dans le partage

## Conseils pour cette période
- L'intimité vraie demande de la profondeur
- Les finances partagées demandent du réalisme
- La légèreté n'exclut pas la profondeur""",

    ('sagittarius', 9): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 9

**En une phrase :** Les croyances optimistes sur l'amour et les voyages romantiques sont en profonde révision.

## L'énergie du moment
Vénus rétrograde est significative en Sagittaire dans la maison 9. Tes croyances sur l'amour idéal et les voyages romantiques sont en profonde révision. L'idéalisme amoureux mérite un regard réaliste.

## Ce que tu pourrais vivre
- Une révision de tes croyances sur l'amour idéal
- Des voyages romantiques compliqués
- Un questionnement sur l'idéalisme en relation

## Conseils pour cette période
- L'amour réel dépasse l'amour idéal
- Les voyages romantiques peuvent être simples
- Les croyances sur l'amour peuvent maturer""",

    ('sagittarius', 10): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 10

**En une phrase :** Ta réputation d'optimiste et tes relations professionnelles enthousiastes sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec l'enthousiasme du Sagittaire. Ta réputation de personne enthousiaste est en révision. Les relations professionnelles basées sur de grandes promesses méritent attention.

## Ce que tu pourrais vivre
- Une révision de ton image professionnelle enthousiaste
- Des promesses professionnelles à revoir
- Le retour d'opportunités ou de contacts du passé

## Conseils pour cette période
- L'enthousiasme professionnel gagne en constance
- Les promesses méritent d'être tenues
- Les opportunités du passé peuvent revenir avec maturité""",

    ('sagittarius', 11): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 11

**En une phrase :** Les amitiés d'aventure et les groupes idéalistes sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec l'optimisme du Sagittaire. Les amitiés basées sur l'aventure plus que sur la constance sont à réviser. Les groupes idéalistes méritent un regard réaliste.

## Ce que tu pourrais vivre
- Une révision des amitiés d'aventure
- Des groupes idéalistes qui déçoivent
- Le retour d'amis avec qui tu as partagé des idéaux

## Conseils pour cette période
- Les vraies amitiés incluent l'aventure ET la constance
- Les groupes réalistes sont plus efficaces
- Les amis idéalistes du passé ont des leçons""",

    ('sagittarius', 12): """# ♀℞ Vénus rétrograde en Sagittaire — Maison 12

**En une phrase :** Les croyances inconscientes sur l'amour libre et les idéaux cachés sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec l'idéalisme du Sagittaire. Les croyances inconscientes sur ce que devrait être l'amour libre sont révélées. Les idéaux cachés sur les relations méritent d'être examinés.

## Ce que tu pourrais vivre
- Des croyances cachées sur l'amour libre qui remontent
- Des idéaux inconscients sur les relations révélés
- Des rêves sur la liberté et l'amour

## Conseils pour cette période
- Les croyances inconscientes peuvent être transformées
- L'amour libre a des significations multiples
- Les idéaux cachés méritent la lumière""",

    # ============== CAPRICORN (Capricorne) ==============
    ('capricorn', 1): """# ♀℞ Vénus rétrograde en Capricorne — Maison 1

**En une phrase :** Ton image sérieuse et ta façon contrôlée de séduire sont en révision.

## L'énergie du moment
Vénus rétrograde en Capricorne dans ta maison 1 remet en question ton image sérieuse et ta façon réservée de te présenter. Tu as peut-être été trop froid·e ou contrôlé·e. C'est le moment de réviser ton image avec plus de chaleur.

## Ce que tu pourrais vivre
- Une révision de ton image sérieuse
- Des questions sur ta façon contrôlée de séduire
- Un besoin de plus de chaleur dans ta présentation

## Conseils pour cette période
- Le sérieux n'exclut pas la chaleur
- Le contrôle peut être assoupli
- L'authenticité inclut la vulnérabilité""",

    ('capricorn', 2): """# ♀℞ Vénus rétrograde en Capricorne — Maison 2

**En une phrase :** Ton rapport structuré à l'argent et tes valeurs de réussite sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec la rigueur du Capricorne. Ton rapport peut-être trop contrôlé à l'argent est à reconsidérer. Les valeurs basées uniquement sur la réussite méritent d'être élargies.

## Ce que tu pourrais vivre
- Une révision du contrôle excessif sur les finances
- Des questions sur les valeurs de réussite
- Un besoin d'inclure le plaisir dans les finances

## Conseils pour cette période
- La structure financière peut inclure le plaisir
- La réussite n'est pas la seule valeur
- L'argent peut servir la joie, pas juste la sécurité""",

    ('capricorn', 3): """# ♀℞ Vénus rétrograde en Capricorne — Maison 3

**En une phrase :** Tes communications formelles et ta façon sérieuse d'échanger sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec la formalité du Capricorne. Tes communications peuvent avoir été trop froides ou formelles. Les échanges affectueux méritent plus de chaleur.

## Ce que tu pourrais vivre
- Une révision des communications trop formelles
- Des échanges affectifs qui manquent de chaleur
- Un besoin de légèreté dans les conversations

## Conseils pour cette période
- L'affection peut s'exprimer simplement
- La formalité a ses limites dans les relations
- La chaleur en communication crée des liens""",

    ('capricorn', 4): """# ♀℞ Vénus rétrograde en Capricorne — Maison 4

**En une phrase :** L'atmosphère sérieuse au foyer et les responsabilités familiales sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec la responsabilité du Capricorne. L'atmosphère peut-être trop sérieuse à la maison est à reconsidérer. Les responsabilités familiales qui pèsent méritent d'être allégées.

## Ce que tu pourrais vivre
- Une révision de l'atmosphère sérieuse au foyer
- Des responsabilités familiales qui pèsent
- Un besoin de plus de légèreté à la maison

## Conseils pour cette période
- Le foyer peut être responsable ET joyeux
- Les responsabilités familiales méritent d'être partagées
- La légèreté au foyer nourrit l'âme""",

    ('capricorn', 5): """# ♀℞ Vénus rétrograde en Capricorne — Maison 5

**En une phrase :** Les amours sérieux et la créativité contrôlée sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec la retenue du Capricorne. Les relations amoureuses peut-être trop sérieuses sont à réviser. La créativité freinée par le contrôle mérite d'être libérée.

## Ce que tu pourrais vivre
- Une révision des amours trop sérieux
- Des créations trop contrôlées à libérer
- Le retour d'ex avec qui la relation était très structurée

## Conseils pour cette période
- L'amour peut être sérieux ET joyeux
- La créativité gagne à être libérée du contrôle
- Les ex sérieux ont des leçons sur l'équilibre""",

    ('capricorn', 6): """# ♀℞ Vénus rétrograde en Capricorne — Maison 6

**En une phrase :** Les routines rigides et les relations de travail très hiérarchiques sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec la structure du Capricorne. Les routines trop rigides sont à assouplir. Les relations de travail très hiérarchiques méritent plus d'humanité.

## Ce que tu pourrais vivre
- Une révision des routines trop rigides
- Des relations de travail hiérarchiques à humaniser
- Un besoin de plus de flexibilité au quotidien

## Conseils pour cette période
- La structure peut être souple
- Les relations de travail gagnent en humanité
- Le quotidien mérite des moments de plaisir""",

    ('capricorn', 7): """# ♀℞ Vénus rétrograde en Capricorne — Maison 7

**En une phrase :** Les relations de couple très structurées et les partenariats d'affaires sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec la formalité du Capricorne. Les relations de couple trop structurées ou froides sont à réviser. Les partenariats basés uniquement sur les intérêts méritent plus de cœur.

## Ce que tu pourrais vivre
- Une révision des relations trop structurées
- Des partenariats d'intérêt qui manquent de cœur
- Le retour d'ex avec qui la relation était très formelle

## Conseils pour cette période
- Les relations sérieuses incluent la tendresse
- Les partenariats gagnent à avoir du cœur
- Les ex formels ont des leçons sur l'ouverture""",

    ('capricorn', 8): """# ♀℞ Vénus rétrograde en Capricorne — Maison 8

**En une phrase :** L'intimité contrôlée et les finances partagées très structurées sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec le contrôle du Capricorne. L'intimité peut avoir été trop contrôlée. Les arrangements financiers partagés très structurés méritent d'être assouplis.

## Ce que tu pourrais vivre
- Une révision de l'intimité trop contrôlée
- Des arrangements financiers rigides à assouplir
- Un besoin de plus de lâcher-prise dans le partage

## Conseils pour cette période
- L'intimité demande de lâcher le contrôle
- Les finances partagées peuvent être souples
- Le lâcher-prise est aussi une force""",

    ('capricorn', 9): """# ♀℞ Vénus rétrograde en Capricorne — Maison 9

**En une phrase :** Les croyances traditionnelles sur l'amour et les voyages structurés sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec la tradition du Capricorne. Les croyances traditionnelles sur l'amour sont à réviser. Les voyages très planifiés peuvent être assouplis.

## Ce que tu pourrais vivre
- Une révision des croyances traditionnelles sur l'amour
- Des voyages très structurés qui se compliquent
- Un questionnement sur les valeurs héritées

## Conseils pour cette période
- Les croyances sur l'amour peuvent évoluer
- Les voyages peuvent inclure de la spontanéité
- Les valeurs héritées méritent d'être examinées""",

    ('capricorn', 10): """# ♀℞ Vénus rétrograde en Capricorne — Maison 10

**En une phrase :** Ta réputation sérieuse et tes relations professionnelles très formelles sont en profonde révision.

## L'énergie du moment
Vénus rétrograde est très significative en Capricorne dans la maison 10, domaine de la carrière. Ta réputation professionnelle et tes relations de travail formelles sont en profonde révision. C'est le moment de reconsidérer ton image publique.

## Ce que tu pourrais vivre
- Une révision profonde de ton image professionnelle
- Des relations de travail trop formelles à humaniser
- Le retour d'opportunités ou de contacts du passé

## Conseils pour cette période
- La réputation peut être sérieuse ET chaleureuse
- Les relations professionnelles gagnent en humanité
- Les opportunités du passé peuvent revenir transformées""",

    ('capricorn', 11): """# ♀℞ Vénus rétrograde en Capricorne — Maison 11

**En une phrase :** Les amitiés très structurées et les groupes hiérarchiques sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec la structure du Capricorne. Les amitiés très formelles ou utilitaires sont à réviser. Les groupes très hiérarchiques méritent plus d'égalité.

## Ce que tu pourrais vivre
- Une révision des amitiés formelles
- Des groupes hiérarchiques qui posent question
- Le retour d'amis avec qui la relation était structurée

## Conseils pour cette période
- Les vraies amitiés vont au-delà de l'utilité
- Les groupes sains sont égalitaires
- Les amis formels du passé ont des leçons""",

    ('capricorn', 12): """# ♀℞ Vénus rétrograde en Capricorne — Maison 12

**En une phrase :** Le contrôle inconscient en amour et les limitations cachées sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec le contrôle du Capricorne. Les patterns inconscients de contrôle en amour sont révélés. Les limitations cachées que tu t'imposes méritent d'être vues.

## Ce que tu pourrais vivre
- Des patterns de contrôle en amour qui remontent
- Des limitations auto-imposées révélées
- Des rêves sur le contrôle et la libération

## Conseils pour cette période
- Les patterns de contrôle ont des origines
- Les limitations peuvent être transformées
- Le lâcher-prise intérieur libère l'amour""",

    # ============== AQUARIUS (Verseau) ==============
    ('aquarius', 1): """# ♀℞ Vénus rétrograde en Verseau — Maison 1

**En une phrase :** Ton image originale et ta façon non conventionnelle de séduire sont en révision.

## L'énergie du moment
Vénus rétrograde en Verseau dans ta maison 1 remet en question ta façon unique et détachée de te présenter. Tu as peut-être été trop distant·e ou anticonformiste. C'est le moment de réviser ton image avec plus de connexion.

## Ce que tu pourrais vivre
- Une révision de ton image originale ou excentrique
- Des questions sur ta façon détachée de séduire
- Un besoin de plus de connexion émotionnelle

## Conseils pour cette période
- L'originalité n'exclut pas la connexion
- Le détachement peut être tempéré par la présence
- L'authenticité inclut aussi la vulnérabilité""",

    ('aquarius', 2): """# ♀℞ Vénus rétrograde en Verseau — Maison 2

**En une phrase :** Tes valeurs non conventionnelles et ton rapport détaché à l'argent sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec l'originalité du Verseau. Ton rapport peut-être trop détaché ou non conventionnel à l'argent est à reconsidérer. Les valeurs qui te différencient méritent d'être ancrées.

## Ce que tu pourrais vivre
- Une révision de tes valeurs non conventionnelles
- Un rapport à l'argent trop détaché à ancrer
- Des questions sur ce qui a vraiment de la valeur

## Conseils pour cette période
- Les valeurs originales peuvent être ancrées
- L'argent est aussi une réalité matérielle
- L'originalité n'exclut pas la stabilité""",

    ('aquarius', 3): """# ♀℞ Vénus rétrograde en Verseau — Maison 3

**En une phrase :** Tes communications originales et ta façon détachée d'échanger sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec l'originalité du Verseau. Tes communications peuvent avoir été trop intellectuelles ou détachées. Les échanges affectueux méritent plus de chaleur émotionnelle.

## Ce que tu pourrais vivre
- Une révision des communications trop intellectuelles
- Des échanges affectifs qui manquent de chaleur
- Un besoin de plus de connexion dans les conversations

## Conseils pour cette période
- L'intelligence peut inclure l'émotion
- La communication gagne en chaleur
- La connexion va au-delà des idées""",

    ('aquarius', 4): """# ♀℞ Vénus rétrograde en Verseau — Maison 4

**En une phrase :** L'atmosphère non conventionnelle au foyer et les liens familiaux détachés sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec le détachement du Verseau. L'atmosphère peut-être trop froide ou intellectuelle à la maison est à reconsidérer. Les liens familiaux méritent plus de connexion émotionnelle.

## Ce que tu pourrais vivre
- Une révision de l'atmosphère détachée au foyer
- Des liens familiaux qui manquent de chaleur
- Un besoin de plus de connexion émotionnelle à la maison

## Conseils pour cette période
- Le foyer peut être original ET chaleureux
- Les liens familiaux méritent de l'attention émotionnelle
- La connexion au foyer nourrit l'âme""",

    ('aquarius', 5): """# ♀℞ Vénus rétrograde en Verseau — Maison 5

**En une phrase :** Les amours non conventionnels et la créativité intellectuelle sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec l'originalité du Verseau. Les relations amoureuses non conventionnelles sont à réviser. La créativité trop intellectuelle mérite d'intégrer plus d'émotion.

## Ce que tu pourrais vivre
- Une révision des amours non conventionnels
- Des créations trop cérébrales à réchauffer
- Le retour d'ex avec qui la relation était très libre

## Conseils pour cette période
- L'amour non conventionnel inclut aussi l'émotion
- La créativité gagne à intégrer le cœur
- Les ex libres ont des leçons sur la connexion""",

    ('aquarius', 6): """# ♀℞ Vénus rétrograde en Verseau — Maison 6

**En une phrase :** Les routines innovantes et les relations de travail détachées sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec l'innovation du Verseau. Les routines trop innovantes ou changeantes sont à stabiliser. Les relations de travail détachées méritent plus de connexion.

## Ce que tu pourrais vivre
- Une révision des routines trop innovantes
- Des relations de travail qui manquent de chaleur
- Un besoin de plus de stabilité et de connexion

## Conseils pour cette période
- L'innovation peut être stable
- Les relations de travail gagnent en humanité
- Le quotidien mérite des connexions vraies""",

    ('aquarius', 7): """# ♀℞ Vénus rétrograde en Verseau — Maison 7

**En une phrase :** Les relations de couple très libres et les partenariats intellectuels sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec l'indépendance du Verseau. Les relations où la liberté prime sur la connexion sont à réviser. Les partenariats trop intellectuels méritent plus de cœur.

## Ce que tu pourrais vivre
- Une révision des relations très libres
- Des partenariats intellectuels qui manquent de cœur
- Le retour d'ex avec qui la relation était très libre

## Conseils pour cette période
- La liberté en couple inclut la connexion
- Les partenariats gagnent à intégrer l'émotion
- Les ex libres ont des leçons sur l'équilibre""",

    ('aquarius', 8): """# ♀℞ Vénus rétrograde en Verseau — Maison 8

**En une phrase :** L'intimité détachée et les approches non conventionnelles du partage sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec le détachement du Verseau. L'intimité peut avoir manqué de profondeur émotionnelle. Les approches non conventionnelles du partage financier sont à reconsidérer.

## Ce que tu pourrais vivre
- Une révision de l'intimité trop détachée
- Des approches du partage à évaluer
- Un besoin de plus de connexion dans les profondeurs

## Conseils pour cette période
- L'intimité demande de la présence émotionnelle
- Les approches non conventionnelles ont leurs limites
- La profondeur inclut la vulnérabilité""",

    ('aquarius', 9): """# ♀℞ Vénus rétrograde en Verseau — Maison 9

**En une phrase :** Les croyances non conventionnelles sur l'amour et les voyages expérimentaux sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec l'avant-gardisme du Verseau. Les croyances non conventionnelles sur l'amour sont à réviser. Les voyages très expérimentaux méritent d'être stabilisés.

## Ce que tu pourrais vivre
- Une révision des croyances non conventionnelles sur l'amour
- Des voyages expérimentaux qui se compliquent
- Un questionnement sur les idées avant-gardistes

## Conseils pour cette période
- Les croyances progressistes méritent d'être ancrées
- Les voyages peuvent être innovants ET planifiés
- L'avant-garde n'exclut pas la sagesse""",

    ('aquarius', 10): """# ♀℞ Vénus rétrograde en Verseau — Maison 10

**En une phrase :** Ta réputation d'original et tes relations professionnelles non conventionnelles sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec l'originalité du Verseau. Ta réputation de personne originale ou non conventionnelle est en révision. Les relations professionnelles détachées méritent plus de connexion.

## Ce que tu pourrais vivre
- Une révision de ton image professionnelle originale
- Des relations de travail détachées à humaniser
- Le retour d'opportunités ou de contacts du passé

## Conseils pour cette période
- L'originalité professionnelle gagne en connexion
- Les relations de travail méritent de la chaleur
- Les opportunités passées peuvent revenir différemment""",

    ('aquarius', 11): """# ♀℞ Vénus rétrograde en Verseau — Maison 11

**En une phrase :** Les amitiés très libres et les groupes non conventionnels sont en profonde révision.

## L'énergie du moment
Vénus rétrograde est significative en Verseau dans la maison 11, domaine des amitiés et des groupes. Les amitiés très libres ou détachées sont en profonde révision. Les groupes non conventionnels méritent d'être examinés.

## Ce que tu pourrais vivre
- Une révision profonde des amitiés très libres
- Des groupes non conventionnels qui posent question
- Le retour d'amis avec qui la liberté était centrale

## Conseils pour cette période
- Les vraies amitiés incluent la constance
- Les groupes sains équilibrent liberté et connexion
- Les amis libres du passé ont des leçons""",

    ('aquarius', 12): """# ♀℞ Vénus rétrograde en Verseau — Maison 12

**En une phrase :** Le détachement inconscient en amour et les idéaux cachés de liberté sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec le détachement du Verseau. Les patterns inconscients de distance émotionnelle sont révélés. Les idéaux cachés de liberté en amour méritent d'être examinés.

## Ce que tu pourrais vivre
- Des patterns de détachement qui remontent
- Des idéaux de liberté amoureuse à examiner
- Des rêves sur la liberté et la connexion

## Conseils pour cette période
- Le détachement a souvent des origines à comprendre
- La liberté vraie inclut la capacité de connexion
- Les idéaux cachés peuvent être transformés""",

    # ============== PISCES (Poissons) ==============
    ('pisces', 1): """# ♀℞ Vénus rétrograde en Poissons — Maison 1

**En une phrase :** Ton image romantique et ta façon de te présenter avec sensibilité sont en profonde révision.

## L'énergie du moment
Vénus rétrograde est très significative en Poissons dans ta maison 1. Toute ta façon de te présenter, ton charme sensible, ton image romantique sont en profonde révision. C'est une période puissante de transformation de l'image de soi.

## Ce que tu pourrais vivre
- Une révision profonde de ton image romantique
- Des questions sur ta façon sensible de te présenter
- Un retour à une expression plus authentique

## Conseils pour cette période
- La sensibilité est une force, pas une faiblesse
- L'authenticité romantique dépasse l'illusion
- Ton image peut refléter ta vraie nature""",

    ('pisces', 2): """# ♀℞ Vénus rétrograde en Poissons — Maison 2

**En une phrase :** Ton rapport flou à l'argent et tes valeurs idéalistes sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec la confusion des Poissons. Ton rapport peut-être trop flou à l'argent est à clarifier. Les valeurs très idéalistes méritent d'être ancrées dans la réalité.

## Ce que tu pourrais vivre
- Une révision du rapport flou aux finances
- Des valeurs idéalistes à ancrer
- Des questions sur ce qui a vraiment de la valeur

## Conseils pour cette période
- Les finances demandent de la clarté
- Les valeurs peuvent être idéalistes ET pratiques
- L'ancrage n'exclut pas les rêves""",

    ('pisces', 3): """# ♀℞ Vénus rétrograde en Poissons — Maison 3

**En une phrase :** Tes communications poétiques et ta façon intuitive d'échanger sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec l'intuition des Poissons. Tes communications peuvent avoir été trop vagues ou confuses. Les échanges poétiques méritent plus de clarté.

## Ce que tu pourrais vivre
- Une révision des communications floues
- Des échanges poétiques qui ont créé de la confusion
- Un besoin de plus de clarté dans l'expression

## Conseils pour cette période
- La poésie peut être claire
- La communication gagne en précision
- L'intuition peut être exprimée clairement""",

    ('pisces', 4): """# ♀℞ Vénus rétrograde en Poissons — Maison 4

**En une phrase :** L'atmosphère rêveuse au foyer et les liens familiaux fusionnels sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec la dissolution des Poissons. L'atmosphère peut-être trop fusionnelle ou confuse à la maison est à clarifier. Les frontières familiales méritent d'être définies.

## Ce que tu pourrais vivre
- Une révision de l'atmosphère fusionnelle au foyer
- Des liens familiaux avec des frontières floues
- Un besoin de plus de clarté dans l'espace familial

## Conseils pour cette période
- Le foyer peut être sensible ET avoir des limites
- Les liens familiaux gagnent à avoir des frontières
- L'amour familial n'est pas la fusion""",

    ('pisces', 5): """# ♀℞ Vénus rétrograde en Poissons — Maison 5

**En une phrase :** Les amours romantiques idéalisés et la créativité inspirée sont en profonde révision.

## L'énergie du moment
Vénus rétrograde est très puissante en Poissons dans la maison 5, domaine de l'amour et de la création. Les amours romantiques idéalisés sont en profonde révision. La créativité inspirée mais peut-être floue mérite d'être finalisée.

## Ce que tu pourrais vivre
- Une révision profonde des amours idéalisés
- Des créations inspirées à finaliser
- Le retour d'ex avec qui l'amour était un rêve

## Conseils pour cette période
- L'amour réel dépasse l'amour rêvé
- La créativité inspirée mérite d'être concrétisée
- Les ex idéalisés ont des leçons sur la réalité""",

    ('pisces', 6): """# ♀℞ Vénus rétrograde en Poissons — Maison 6

**En une phrase :** Les routines floues et les relations de travail sans limites sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec la confusion des Poissons. Les routines trop peu définies sont à structurer. Les relations de travail avec des limites floues méritent d'être clarifiées.

## Ce que tu pourrais vivre
- Une révision des routines trop floues
- Des relations de travail sans limites claires
- Un besoin de plus de structure dans le quotidien

## Conseils pour cette période
- Les routines peuvent être flexibles ET définies
- Les relations de travail méritent des limites
- La sensibilité au travail demande de la protection""",

    ('pisces', 7): """# ♀℞ Vénus rétrograde en Poissons — Maison 7

**En une phrase :** Les relations de couple idéalisées et les partenariats fusionnels sont en profonde révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec le romantisme des Poissons. Les relations où l'idéalisation remplaçait la réalité sont en profonde révision. Les partenariats fusionnels méritent plus de limites saines.

## Ce que tu pourrais vivre
- Une révision profonde des relations idéalisées
- Des partenariats fusionnels à équilibrer
- Le retour d'ex avec qui l'amour était un rêve

## Conseils pour cette période
- L'amour réel a plus de valeur que le rêve
- La fusion n'est pas l'intimité vraie
- Les ex idéalisés ont des leçons sur la réalité""",

    ('pisces', 8): """# ♀℞ Vénus rétrograde en Poissons — Maison 8

**En une phrase :** L'intimité fusionnelle et les finances partagées floues sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec la dissolution des Poissons. L'intimité peut avoir été trop fusionnelle, perdant les individualités. Les finances partagées trop floues sont à clarifier.

## Ce que tu pourrais vivre
- Une révision de l'intimité fusionnelle
- Des finances partagées confuses à clarifier
- Un besoin de maintenir son identité dans le partage

## Conseils pour cette période
- L'intimité vraie n'efface pas l'individu
- Les finances partagées demandent de la clarté
- Se transformer n'est pas se perdre""",

    ('pisces', 9): """# ♀℞ Vénus rétrograde en Poissons — Maison 9

**En une phrase :** Les croyances romantiques sur l'amour et les quêtes spirituelles amoureuses sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec le mysticisme des Poissons. Les croyances très romantiques ou mystiques sur l'amour sont à réviser. Les quêtes spirituelles qui évitent la réalité méritent d'être ancrées.

## Ce que tu pourrais vivre
- Une révision des croyances mystiques sur l'amour
- Des quêtes spirituelles qui évitent le réel
- Un questionnement sur l'amour et le spirituel

## Conseils pour cette période
- L'amour spirituel s'incarne aussi dans le réel
- Les croyances peuvent être mystiques ET pratiques
- La spiritualité de l'amour n'est pas une fuite""",

    ('pisces', 10): """# ♀℞ Vénus rétrograde en Poissons — Maison 10

**En une phrase :** Ta réputation d'artiste sensible et tes relations professionnelles empathiques sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec la sensibilité des Poissons. Ta réputation de personne sensible ou artistique est en révision. Les relations professionnelles où l'empathie déborde méritent des limites.

## Ce que tu pourrais vivre
- Une révision de ton image professionnelle sensible
- Des relations de travail où l'empathie déborde
- Le retour d'opportunités ou de contacts du passé

## Conseils pour cette période
- La sensibilité professionnelle a besoin de limites
- L'empathie au travail peut être canalisée
- Les opportunités du passé peuvent revenir différemment""",

    ('pisces', 11): """# ♀℞ Vénus rétrograde en Poissons — Maison 11

**En une phrase :** Les amitiés sans limites et les groupes idéalistes sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec la compassion des Poissons. Les amitiés où tu donnes trop ou te perds sont à réviser. Les groupes idéalistes qui évitent la réalité méritent d'être examinés.

## Ce que tu pourrais vivre
- Une révision des amitiés où tu te perds
- Des groupes idéalistes qui déçoivent
- Le retour d'amis avec qui tu avais une connexion profonde

## Conseils pour cette période
- Les vraies amitiés ne te font pas te perdre
- Les groupes idéalistes ont besoin de réalisme
- Les amis profonds du passé ont des leçons""",

    ('pisces', 12): """# ♀℞ Vénus rétrograde en Poissons — Maison 12

**En une phrase :** L'amour inconditionnel inconscient et les sacrifices en amour sont en révision profonde.

## L'énergie du moment
Vénus rétrograde est très puissante en Poissons dans la maison 12. L'amour inconditionnel qui peut mener au sacrifice est en profonde révision. Les patterns inconscients de don de soi excessif méritent d'être vus.

## Ce que tu pourrais vivre
- Des patterns de sacrifice en amour qui remontent
- Une révision de l'amour inconditionnel mal orienté
- Des rêves très significatifs sur l'amour

## Conseils pour cette période
- L'amour inconditionnel inclut l'amour de soi
- Le sacrifice n'est pas de l'amour
- Les patterns inconscients peuvent être transformés""",
}

async def insert_interpretations():
    """Insert all venus_retrograde interpretations for Sagittarius, Capricorn, Aquarius, Pisces"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in VENUS_RETROGRADE_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'venus_retrograde',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP: venus_retrograde {sign} house {house} already exists")
                skipped += 1
                continue

            interpretation = PregeneratedNatalInterpretation(
                subject='venus_retrograde',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interpretation)
            print(f"INSERT: venus_retrograde {sign} house {house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nDone: {inserted} inserted, {skipped} skipped")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
