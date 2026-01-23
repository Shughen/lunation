#!/usr/bin/env python3
"""
Insert venus_retrograde interpretations V2 for Leo, Virgo, Libra, Scorpio (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

VENUS_RETROGRADE_INTERPRETATIONS = {
    # ============== LEO (Lion) ==============
    ('leo', 1): """# ♀℞ Vénus rétrograde en Lion — Maison 1

**En une phrase :** Ta façon de briller et d'attirer l'attention est à reconsidérer.

## L'énergie du moment
Vénus rétrograde en Lion dans ta maison 1 questionne ta façon de te mettre en valeur et de séduire. Tu as peut-être été trop dans le spectacle. C'est le moment de réviser ton image avec plus d'authenticité.

## Ce que tu pourrais vivre
- Une révision de ta façon de te mettre en avant
- Des questions sur l'authenticité de ton charme
- Un retour à des expressions plus vraies de toi-même

## Conseils pour cette période
- Le charme authentique dépasse le spectacle
- Ton image gagne à refléter qui tu es vraiment
- Les looks du passé peuvent inspirer""",

    ('leo', 2): """# ♀℞ Vénus rétrograde en Lion — Maison 2

**En une phrase :** Tes dépenses pour briller et tes valeurs liées à la reconnaissance sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec l'extravagance du Lion. Les achats pour impressionner ou briller peuvent être regrettés. Tes valeurs liées à la reconnaissance méritent d'être reconsidérées.

## Ce que tu pourrais vivre
- Des achats de luxe ou pour impressionner à reconsidérer
- Une révision de tes valeurs liées à la reconnaissance
- Des questions sur ce qui te donne vraiment de la valeur

## Conseils pour cette période
- Évite les achats ostentatoires
- Ta vraie valeur ne dépend pas de ce que tu possèdes
- La simplicité a aussi son élégance""",

    ('leo', 3): """# ♀℞ Vénus rétrograde en Lion — Maison 3

**En une phrase :** Tes communications charmantes et ta façon de séduire par les mots sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec la théâtralité du Lion. Ta façon de charmer par les mots peut avoir été trop dramatique. Les échanges avec l'entourage proche méritent plus de simplicité.

## Ce que tu pourrais vivre
- Une révision de ta façon de charmer verbalement
- Des communications trop dramatiques à simplifier
- Un retour de personnes charmées par toi dans le passé

## Conseils pour cette période
- Le charme simple est plus efficace que le spectacle
- Les communications gagnent en sincérité
- Les anciennes connexions peuvent avoir de nouvelles dimensions""",

    ('leo', 4): """# ♀℞ Vénus rétrograde en Lion — Maison 4

**En une phrase :** L'expression de l'amour en famille et la décoration dramatique sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec la grandeur du Lion. La façon dont tu exprimes l'amour en famille peut avoir été trop centrée sur toi. La décoration ostentatoire mérite d'être reconsidérée.

## Ce que tu pourrais vivre
- Une révision de ta façon d'exprimer l'amour en famille
- Des choix de décoration trop voyants à reconsidérer
- Des questions sur ta place au centre de la famille

## Conseils pour cette période
- L'amour familial va dans les deux sens
- La décoration peut être belle sans être dramatique
- Chaque membre de la famille mérite de briller""",

    ('leo', 5): """# ♀℞ Vénus rétrograde en Lion — Maison 5

**En une phrase :** Les amours dramatiques et la créativité spectaculaire sont en profonde révision.

## L'énergie du moment
Vénus rétrograde est très significative en Lion dans la maison 5, domaine de l'amour et de la création. Les relations amoureuses dramatiques et la créativité pour impressionner sont à réviser. C'est une période puissante pour reconsidérer ce que tu cherches vraiment en amour.

## Ce que tu pourrais vivre
- Une révision profonde de tes amours dramatiques
- Des créations spectaculaires à reconsidérer
- Le retour d'ex avec qui tu as vécu des romances intenses

## Conseils pour cette période
- L'amour authentique vaut mieux que le spectacle
- Ta créativité peut être profonde sans être ostentatoire
- Les ex dramatiques ont des leçons sur l'égo en amour""",

    ('leo', 6): """# ♀℞ Vénus rétrograde en Lion — Maison 6

**En une phrase :** Le besoin de briller au travail et les routines de beauté voyantes sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec le besoin de reconnaissance du Lion. Le désir de briller au travail peut avoir créé des tensions. Les routines de beauté voyantes méritent d'être simplifiées.

## Ce que tu pourrais vivre
- Une révision du besoin de reconnaissance au travail
- Des routines de beauté trop élaborées à simplifier
- Des relations de travail basées sur l'admiration à reconsidérer

## Conseils pour cette période
- Le travail bien fait brille par lui-même
- La beauté quotidienne peut être simple
- Les relations de travail saines ne sont pas basées sur l'admiration""",

    ('leo', 7): """# ♀℞ Vénus rétrograde en Lion — Maison 7

**En une phrase :** Les relations de couple basées sur l'admiration mutuelle sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec le besoin de briller du Lion. Les relations où l'admiration était centrale sont à reconsidérer. L'équilibre entre donner et recevoir de l'attention mérite révision.

## Ce que tu pourrais vivre
- Une révision des relations basées sur l'admiration
- Des questions sur l'équilibre d'attention dans le couple
- Le retour d'ex admiratifs ou que tu admirais

## Conseils pour cette période
- L'amour vrai va au-delà de l'admiration
- L'attention doit être équilibrée dans le couple
- Les ex admiratifs ont des leçons sur l'égo en relation""",

    ('leo', 8): """# ♀℞ Vénus rétrograde en Lion — Maison 8

**En une phrase :** L'intimité dramatique et les jeux de pouvoir passionnels sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec l'intensité du Lion. L'intimité peut avoir été un spectacle. Les jeux de pouvoir passionnels méritent d'être reconsidérés.

## Ce que tu pourrais vivre
- Une révision de l'intimité théâtrale
- Des questions sur le pouvoir dans les relations profondes
- Le retour de passions intenses du passé

## Conseils pour cette période
- L'intimité vraie n'est pas un spectacle
- Le pouvoir en relation mérite de l'équilibre
- Les passions du passé ont des leçons sur l'égo""",

    ('leo', 9): """# ♀℞ Vénus rétrograde en Lion — Maison 9

**En une phrase :** Les croyances sur l'amour grandiose et les voyages pour briller sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec la grandeur du Lion. Tes croyances sur ce qu'est un grand amour sont à reconsidérer. Les voyages pour impressionner méritent d'être simplifiés.

## Ce que tu pourrais vivre
- Une révision de tes idéaux sur l'amour grandiose
- Des voyages de prestige compliqués
- Un questionnement sur ce qui fait un vrai amour

## Conseils pour cette période
- L'amour authentique n'a pas besoin d'être grandiose
- Les voyages simples ont aussi leur valeur
- Les vraies croyances sur l'amour viennent du cœur""",

    ('leo', 10): """# ♀℞ Vénus rétrograde en Lion — Maison 10

**En une phrase :** Ta réputation de star et tes relations professionnelles admiratives sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec le besoin de briller du Lion. Ta réputation de personne charismatique est en révision. Les relations professionnelles basées sur l'admiration méritent d'être reconsidérées.

## Ce que tu pourrais vivre
- Une révision de ton image de star professionnelle
- Des relations de travail admiratives à reconsidérer
- Le retour d'opportunités liées à ta visibilité

## Conseils pour cette période
- La vraie réussite n'a pas besoin d'applaudissements
- Les relations professionnelles saines vont au-delà de l'admiration
- Les opportunités passées peuvent revenir différemment""",

    ('leo', 11): """# ♀℞ Vénus rétrograde en Lion — Maison 11

**En une phrase :** Les amitiés où tu brilles et les groupes admiratifs sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec le besoin de reconnaissance du Lion. Les amitiés où tu es le centre d'attention sont à reconsidérer. Les groupes où l'admiration circule méritent révision.

## Ce que tu pourrais vivre
- Une révision des amitiés où tu brilles trop
- Des questions sur l'équilibre d'attention dans les groupes
- Le retour d'amis qui t'admirent ou que tu admirais

## Conseils pour cette période
- Les vraies amitiés ne sont pas basées sur l'admiration
- Chaque ami mérite sa place sous les projecteurs
- Les amis du passé ont des leçons sur l'équilibre""",

    ('leo', 12): """# ♀℞ Vénus rétrograde en Lion — Maison 12

**En une phrase :** Le besoin secret de briller et l'amour-propre inconscient sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec l'égo du Lion. Le besoin caché de reconnaissance et d'admiration est révélé. L'amour-propre et ses racines inconscientes méritent d'être examinés.

## Ce que tu pourrais vivre
- Un besoin caché de briller qui remonte
- Des questions sur l'amour-propre et son origine
- Des rêves sur la reconnaissance et l'admiration

## Conseils pour cette période
- Le besoin de briller a souvent des racines anciennes
- L'amour-propre vient de l'intérieur
- Les rêves peuvent révéler ce que tu cherches vraiment""",

    # ============== VIRGO (Vierge) ==============
    ('virgo', 1): """# ♀℞ Vénus rétrograde en Vierge — Maison 1

**En une phrase :** Ta façon perfectionniste de te présenter et ta critique de toi-même sont à réviser.

## L'énergie du moment
Vénus rétrograde en Vierge dans ta maison 1 questionne ton perfectionnisme concernant ton image. Tu as peut-être été trop critique envers toi-même. C'est le moment de réviser ton rapport à ta propre beauté.

## Ce que tu pourrais vivre
- Une révision de ton perfectionnisme concernant ton image
- Des questions sur ta critique de toi-même
- Un retour à une acceptation plus douce de toi

## Conseils pour cette période
- La perfection n'est pas nécessaire pour être attrayant·e
- L'autocritique excessive n'est pas de l'amour-propre
- Accepte-toi avec tes imperfections""",

    ('virgo', 2): """# ♀℞ Vénus rétrograde en Vierge — Maison 2

**En une phrase :** Ton rapport critique à l'argent et tes valeurs perfectionnistes sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec le discernement de la Vierge. Ton rapport peut-être trop analytique à l'argent est à reconsidérer. Les achats basés sur la fonctionnalité parfaite méritent révision.

## Ce que tu pourrais vivre
- Une révision de ton analyse excessive des finances
- Des achats basés sur la perfection à reconsidérer
- Des questions sur ce qui a vraiment de la valeur

## Conseils pour cette période
- L'argent n'a pas besoin d'être géré parfaitement
- Le plaisir a aussi sa valeur, pas juste la fonction
- Ce qui a de la valeur n'est pas toujours parfait""",

    ('virgo', 3): """# ♀℞ Vénus rétrograde en Vierge — Maison 3

**En une phrase :** Tes communications critiques et ta façon analytique d'exprimer l'affection sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec l'analyse de la Vierge. Ta façon peut-être trop critique de communiquer est à reconsidérer. Les échanges affectueux gagnent à être moins analytiques.

## Ce que tu pourrais vivre
- Une révision de tes communications critiques
- Des échanges affectifs trop analysés à simplifier
- Un besoin de plus de douceur dans les mots

## Conseils pour cette période
- L'affection n'a pas besoin d'analyse
- La critique peut être remplacée par l'appréciation
- Les mots doux simples ont leur pouvoir""",

    ('virgo', 4): """# ♀℞ Vénus rétrograde en Vierge — Maison 4

**En une phrase :** Le perfectionnisme au foyer et l'amour conditionnel en famille sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec l'exigence de la Vierge. Le perfectionnisme concernant la maison est à reconsidérer. L'amour familial conditionné par la performance mérite révision.

## Ce que tu pourrais vivre
- Une révision du perfectionnisme domestique
- Des questions sur l'amour conditionnel en famille
- Un besoin de plus de douceur et d'acceptation au foyer

## Conseils pour cette période
- La maison n'a pas besoin d'être parfaite pour être aimée
- L'amour familial peut être inconditionnel
- L'imperfection fait partie de la chaleur d'un foyer""",

    ('virgo', 5): """# ♀℞ Vénus rétrograde en Vierge — Maison 5

**En une phrase :** Les amours perfectionnistes et la créativité critique sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec le perfectionnisme de la Vierge. Les relations où tu as été trop exigeant·e sont à réviser. La créativité freinée par l'autocritique mérite d'être libérée.

## Ce que tu pourrais vivre
- Une révision des exigences en amour
- Des créations bloquées par le perfectionnisme
- Le retour d'ex avec qui les standards étaient trop élevés

## Conseils pour cette période
- L'amour parfait n'existe pas, et c'est bien ainsi
- La créativité a besoin de liberté, pas de perfection
- Les ex ont des leçons sur l'acceptation""",

    ('virgo', 6): """# ♀℞ Vénus rétrograde en Vierge — Maison 6

**En une phrase :** Les routines de beauté perfectionnistes et les relations de travail critiques sont en révision.

## L'énergie du moment
Vénus rétrograde est significative en Vierge dans la maison 6. Les routines de soin obsessionnelles et les relations de travail trop critiques sont à réviser. C'est le moment de trouver un équilibre plus doux.

## Ce que tu pourrais vivre
- Une révision des routines de beauté obsessionnelles
- Des relations de travail critiques à adoucir
- Un besoin de plus de gentillesse envers toi et les autres

## Conseils pour cette période
- Les routines de beauté peuvent être simples et efficaces
- La critique au travail peut devenir de l'aide constructive
- La gentillesse envers soi améliore le quotidien""",

    ('virgo', 7): """# ♀℞ Vénus rétrograde en Vierge — Maison 7

**En une phrase :** Les relations basées sur des standards élevés et la critique du partenaire sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec l'exigence de la Vierge. Les relations où les standards sont trop élevés sont à reconsidérer. La critique du partenaire mérite d'être transformée en acceptation.

## Ce que tu pourrais vivre
- Une révision des exigences dans le couple
- Des critiques du partenaire à transformer
- Le retour d'ex avec qui tu as été trop exigeant·e

## Conseils pour cette période
- Personne n'est parfait, et ton partenaire non plus
- L'appréciation vaut mieux que la critique
- Les ex ont des leçons sur l'acceptation en relation""",

    ('virgo', 8): """# ♀℞ Vénus rétrograde en Vierge — Maison 8

**En une phrase :** L'analyse excessive de l'intimité et le perfectionnisme dans les finances partagées sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec l'analyse de la Vierge. L'intimité trop analysée perd sa magie. Les finances partagées gérées de façon obsessionnelle méritent plus de fluidité.

## Ce que tu pourrais vivre
- Une révision de l'analyse excessive de l'intimité
- Des finances partagées gérées de façon trop rigide
- Un besoin de lâcher prise dans les domaines profonds

## Conseils pour cette période
- L'intimité demande du lâcher-prise, pas de l'analyse
- Les finances partagées peuvent être gérées avec souplesse
- La transformation n'est pas une science exacte""",

    ('virgo', 9): """# ♀℞ Vénus rétrograde en Vierge — Maison 9

**En une phrase :** Les croyances perfectionnistes sur l'amour et les voyages trop planifiés sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec le souci du détail de la Vierge. Les croyances trop rigides sur ce que devrait être l'amour méritent de la souplesse. Les voyages trop planifiés peuvent manquer de spontanéité.

## Ce que tu pourrais vivre
- Une révision des croyances rigides sur l'amour
- Des voyages trop organisés qui perdent leur magie
- Un questionnement sur la place de l'imprévu

## Conseils pour cette période
- L'amour a besoin de spontanéité autant que de structure
- Les voyages peuvent inclure de l'imprévu
- Les croyances gagnent à être flexibles""",

    ('virgo', 10): """# ♀℞ Vénus rétrograde en Vierge — Maison 10

**En une phrase :** Le perfectionnisme professionnel et les relations de travail trop exigeantes sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec l'exigence de la Vierge. Ta réputation de perfectionniste est en révision. Les relations professionnelles basées sur des standards impossibles méritent d'être assouplies.

## Ce que tu pourrais vivre
- Une révision de ton perfectionnisme professionnel
- Des relations de travail trop exigeantes à adoucir
- Le retour d'opportunités professionnelles passées

## Conseils pour cette période
- L'excellent suffit, la perfection épuise
- Les relations professionnelles gagnent en bienveillance
- Les opportunités passées peuvent revenir avec maturité""",

    ('virgo', 11): """# ♀℞ Vénus rétrograde en Vierge — Maison 11

**En une phrase :** Les amitiés basées sur des standards élevés et les groupes critiques sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec l'exigence de la Vierge. Les amitiés où les standards sont trop élevés sont à reconsidérer. Les groupes trop critiques méritent d'être équilibrés par l'acceptation.

## Ce que tu pourrais vivre
- Une révision des amitiés aux standards trop élevés
- Des groupes trop critiques à quitter ou transformer
- Le retour d'amis avec qui tu as été trop exigeant·e

## Conseils pour cette période
- Les vrais amis acceptent les imperfections
- Les groupes bienveillants sont plus nourrissants
- Les amis du passé peuvent revenir avec acceptation""",

    ('virgo', 12): """# ♀℞ Vénus rétrograde en Vierge — Maison 12

**En une phrase :** Le critique intérieur et les standards inconscients sur l'amour sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec l'autocritique de la Vierge. Le critique intérieur qui juge ta valeur et ta capacité d'aimer est révélé. Les standards inconscients sur l'amour méritent d'être examinés.

## Ce que tu pourrais vivre
- Un critique intérieur très actif sur l'amour
- Des standards inconscients sur la valeur personnelle
- Des rêves sur le perfectionnisme et l'acceptation

## Conseils pour cette période
- Le critique intérieur peut devenir un allié bienveillant
- Les standards inconscients peuvent être transformés
- L'amour de soi inconditionnel est le fondement""",

    # ============== LIBRA (Balance) ==============
    ('libra', 1): """# ♀℞ Vénus rétrograde en Balance — Maison 1

**En une phrase :** Ta façon de te présenter pour plaire et ton équilibre personnel sont en profonde révision.

## L'énergie du moment
Vénus rétrograde est très significative en Balance, signe qu'elle gouverne, dans ta maison 1. Toute ta façon de te présenter, de chercher l'harmonie, de plaire est en profonde révision. C'est une période clé pour l'authenticité.

## Ce que tu pourrais vivre
- Une révision profonde de ta façon de plaire
- Des questions sur l'équilibre entre toi et les autres
- Un retour à une image plus authentique

## Conseils pour cette période
- Plaire à tout le monde n'est pas possible ni souhaitable
- L'équilibre commence par être soi-même
- L'authenticité est plus attirante que la complaisance""",

    ('libra', 2): """# ♀℞ Vénus rétrograde en Balance — Maison 2

**En une phrase :** Tes valeurs liées à l'harmonie et tes dépenses pour plaire sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec le sens esthétique de la Balance. Les achats pour créer l'harmonie ou plaire aux autres sont à reconsidérer. Tes valeurs liées à l'équilibre méritent d'être examinées.

## Ce que tu pourrais vivre
- Des achats pour plaire ou créer l'harmonie à reconsidérer
- Des questions sur ce que tu values vraiment
- Une révision des dépenses liées à l'image

## Conseils pour cette période
- Évite les achats pour faire plaisir aux autres
- Tes vraies valeurs ne dépendent pas des autres
- L'harmonie financière vient de l'alignement intérieur""",

    ('libra', 3): """# ♀℞ Vénus rétrograde en Balance — Maison 3

**En une phrase :** Tes communications diplomatiques et ta façon d'éviter les conflits sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec la diplomatie de la Balance. Ta façon d'arrondir les angles et d'éviter les conflits est à reconsidérer. Les communications peuvent gagner en authenticité.

## Ce que tu pourrais vivre
- Une révision de ta diplomatie excessive
- Des non-dits qui demandent à être exprimés
- Un besoin de communications plus directes

## Conseils pour cette période
- La diplomatie vraie inclut l'honnêteté
- Les non-dits finissent par peser
- L'harmonie authentique passe par la vérité""",

    ('libra', 4): """# ♀℞ Vénus rétrograde en Balance — Maison 4

**En une phrase :** L'harmonie au foyer maintenue au prix de compromis et la décoration parfaite sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec le besoin d'harmonie de la Balance. La paix maintenue par des compromis excessifs est à reconsidérer. La décoration parfaite peut avoir caché des tensions.

## Ce que tu pourrais vivre
- Une révision de la fausse harmonie au foyer
- Des tensions familiales évitées qui ressurgissent
- Un besoin d'authenticité dans l'espace et les relations

## Conseils pour cette période
- La vraie harmonie ne vient pas de l'évitement
- Les tensions familiales méritent d'être adressées
- Un foyer authentique est plus chaleureux qu'un foyer parfait""",

    ('libra', 5): """# ♀℞ Vénus rétrograde en Balance — Maison 5

**En une phrase :** Les amours équilibrées et la créativité harmonieuse sont en profonde révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec le besoin de relation de la Balance. Les amours où tu as trop cherché l'équilibre au détriment de l'authenticité sont à réviser. La créativité trop polie mérite plus d'audace.

## Ce que tu pourrais vivre
- Une révision des amours trop "équilibrées"
- Des créations trop lisses à retravailler
- Le retour d'ex avec qui l'équilibre masquait des problèmes

## Conseils pour cette période
- L'amour authentique a des aspérités
- La créativité peut être déséquilibrée et belle
- Les ex équilibrés ont des leçons sur l'authenticité""",

    ('libra', 6): """# ♀℞ Vénus rétrograde en Balance — Maison 6

**En une phrase :** L'harmonie au travail maintenue par des compromis et les routines de beauté équilibrées sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec le besoin de plaire de la Balance. Les compromis excessifs au travail pour maintenir l'harmonie sont à reconsidérer. Les routines de beauté peuvent être simplifiées.

## Ce que tu pourrais vivre
- Une révision des compromis excessifs au travail
- Des routines de beauté trop élaborées
- Un besoin de plus d'authenticité dans le quotidien

## Conseils pour cette période
- Les compromis ont leurs limites
- La beauté quotidienne peut être simple
- L'authenticité au travail est plus satisfaisante""",

    ('libra', 7): """# ♀℞ Vénus rétrograde en Balance — Maison 7

**En une phrase :** Les partenariats et ta façon de maintenir l'équilibre relationnel sont en révision profonde.

## L'énergie du moment
Vénus rétrograde est doublement puissante en Balance dans la maison 7. Toutes tes relations de couple et de partenariat sont en révision profonde. La façon dont tu maintiens l'équilibre relationnel mérite d'être examinée.

## Ce que tu pourrais vivre
- Une révision profonde de ton couple et de tes partenariats
- Des questions sur l'équité et l'équilibre en relation
- Le retour d'ex significatifs

## Conseils pour cette période
- L'équilibre en relation n'est pas l'absence de conflit
- Les partenariats authentiques incluent des désaccords
- Les ex qui reviennent ont des leçons majeures""",

    ('libra', 8): """# ♀℞ Vénus rétrograde en Balance — Maison 8

**En une phrase :** L'équilibre dans l'intimité et les finances partagées équitables sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec le besoin d'équité de la Balance. L'équilibre dans l'intimité peut avoir masqué des déséquilibres. Les finances partagées méritent d'être examinées avec honnêteté.

## Ce que tu pourrais vivre
- Une révision de l'équilibre dans l'intimité
- Des questions sur l'équité des finances partagées
- Un besoin de plus d'honnêteté dans les profondeurs

## Conseils pour cette période
- L'intimité vraie n'est pas toujours équilibrée
- Les finances partagées demandent de la transparence
- L'équité profonde vient de l'honnêteté""",

    ('libra', 9): """# ♀℞ Vénus rétrograde en Balance — Maison 9

**En une phrase :** Les croyances sur l'équilibre en amour et les voyages harmonieux sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec l'idéal de la Balance. Tes croyances sur ce qu'est un amour équilibré sont à reconsidérer. Les voyages parfaitement planifiés pour l'harmonie peuvent se compliquer.

## Ce que tu pourrais vivre
- Une révision de tes idéaux sur l'amour équilibré
- Des voyages harmonieux qui rencontrent des complications
- Un questionnement sur le vrai sens de l'équilibre

## Conseils pour cette période
- L'amour équilibré inclut des moments de déséquilibre
- Les voyages imparfaits ont aussi leur charme
- L'équilibre vrai n'est pas statique""",

    ('libra', 10): """# ♀℞ Vénus rétrograde en Balance — Maison 10

**En une phrase :** Ta réputation de personne équilibrée et tes relations professionnelles harmonieuses sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec la diplomatie de la Balance. Ta réputation de personne équilibrée et diplomate est en révision. Les relations professionnelles maintenues par des compromis méritent attention.

## Ce que tu pourrais vivre
- Une révision de ton image professionnelle équilibrée
- Des relations de travail basées sur trop de compromis
- Le retour de contacts professionnels significatifs

## Conseils pour cette période
- La vraie diplomatie inclut parfois le désaccord
- Les compromis professionnels ont leurs limites
- Les contacts du passé peuvent revenir avec équité""",

    ('libra', 11): """# ♀℞ Vénus rétrograde en Balance — Maison 11

**En une phrase :** Les amitiés équilibrées et les groupes harmonieux sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec le besoin d'harmonie de la Balance. Les amitiés où l'équilibre masque des problèmes sont à réviser. Les groupes trop harmonieux peuvent avoir évité les vrais sujets.

## Ce que tu pourrais vivre
- Une révision des amitiés trop équilibrées
- Des groupes où l'harmonie cache des tensions
- Le retour d'amis avec qui l'équilibre était central

## Conseils pour cette période
- Les vraies amitiés survivent aux désaccords
- Les groupes authentiques abordent les vrais sujets
- Les amis du passé ont des leçons sur l'équilibre""",

    ('libra', 12): """# ♀℞ Vénus rétrograde en Balance — Maison 12

**En une phrase :** Le besoin inconscient de plaire et l'équilibre recherché à tout prix sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec le besoin de plaire de la Balance. Le besoin caché de maintenir l'harmonie et de plaire est révélé. Les patterns inconscients relationnels méritent d'être examinés.

## Ce que tu pourrais vivre
- Un besoin caché de plaire qui remonte
- Des patterns relationnels inconscients révélés
- Des rêves sur l'équilibre et les relations

## Conseils pour cette période
- Le besoin de plaire a des racines profondes
- Les patterns inconscients peuvent être transformés
- Tu mérites l'amour même sans chercher l'équilibre""",

    # ============== SCORPIO (Scorpion) ==============
    ('scorpio', 1): """# ♀℞ Vénus rétrograde en Scorpion — Maison 1

**En une phrase :** Ton magnétisme et ta façon intense de te présenter sont en profonde révision.

## L'énergie du moment
Vénus rétrograde en Scorpion dans ta maison 1 intensifie la révision de ton image et de ton magnétisme. Ta façon de séduire et d'attirer peut avoir été trop contrôlante ou manipulatrice. C'est le moment d'une transformation profonde.

## Ce que tu pourrais vivre
- Une révision de ton magnétisme et de ton image
- Des questions sur le contrôle dans ta façon d'attirer
- Une transformation profonde de ta présence

## Conseils pour cette période
- Le vrai magnétisme vient de l'authenticité
- Le contrôle n'est pas de la séduction
- Ta transformation peut être profonde et positive""",

    ('scorpio', 2): """# ♀℞ Vénus rétrograde en Scorpion — Maison 2

**En une phrase :** Ton attachement aux possessions et tes valeurs profondes sont en révision intense.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec l'intensité du Scorpion. L'attachement aux possessions et aux ressources est à reconsidérer. Les valeurs profondes liées au pouvoir de l'argent méritent d'être examinées.

## Ce que tu pourrais vivre
- Une révision de tes attachements matériels
- Des questions sur le pouvoir et l'argent
- Une transformation de tes valeurs profondes

## Conseils pour cette période
- L'attachement peut être libéré
- L'argent n'est pas du pouvoir
- Les valeurs profondes peuvent évoluer""",

    ('scorpio', 3): """# ♀℞ Vénus rétrograde en Scorpion — Maison 3

**En une phrase :** Tes communications intenses et ta façon de séduire par les mots profonds sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec l'intensité du Scorpion. Tes communications peuvent avoir été trop intenses ou manipulatrices. Les échanges profonds avec l'entourage méritent plus de légèreté.

## Ce que tu pourrais vivre
- Une révision des communications trop intenses
- Des secrets avec l'entourage proche qui émergent
- Un besoin d'équilibrer profondeur et légèreté

## Conseils pour cette période
- L'intensité en communication peut étouffer
- Les secrets méritent d'être traités avec soin
- La légèreté a aussi sa place dans les échanges""",

    ('scorpio', 4): """# ♀℞ Vénus rétrograde en Scorpion — Maison 4

**En une phrase :** Les secrets de famille et l'intensité émotionnelle au foyer sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec l'intensité du Scorpion. Les secrets de famille et les enjeux de pouvoir au foyer sont révélés. L'atmosphère émotionnelle intense de la maison mérite d'être adoucie.

## Ce que tu pourrais vivre
- Des secrets de famille qui émergent
- Des enjeux de pouvoir au foyer à adresser
- Un besoin de plus de légèreté à la maison

## Conseils pour cette période
- Les secrets familiaux révélés peuvent guérir
- Les enjeux de pouvoir au foyer méritent d'être transformés
- L'intensité au foyer peut être équilibrée""",

    ('scorpio', 5): """# ♀℞ Vénus rétrograde en Scorpion — Maison 5

**En une phrase :** Les amours passionnés et la créativité intense sont en révision profonde.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec l'intensité du Scorpion. Les relations amoureuses passionnées mais peut-être obsessionnelles sont à réviser. La créativité qui explore les profondeurs mérite d'être canalisée.

## Ce que tu pourrais vivre
- Une révision des amours passionnés et possessifs
- Des créations intenses à affiner
- Le retour d'ex avec qui la passion était dévorante

## Conseils pour cette période
- La passion n'est pas la possession
- La créativité profonde peut aussi être légère
- Les ex passionnés ont des leçons sur l'intensité""",

    ('scorpio', 6): """# ♀℞ Vénus rétrograde en Scorpion — Maison 6

**En une phrase :** Les relations de travail intenses et les routines de transformation sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec l'intensité du Scorpion. Les relations de travail trop intenses ou avec des enjeux de pouvoir sont à réviser. Les routines de transformation méritent d'être équilibrées.

## Ce que tu pourrais vivre
- Des relations de travail avec des enjeux de pouvoir
- Des routines de transformation trop intenses
- Un besoin d'équilibre dans le quotidien

## Conseils pour cette période
- Les relations de travail peuvent être saines sans être intenses
- Les routines de transformation ont besoin de douceur aussi
- L'équilibre quotidien favorise la vraie transformation""",

    ('scorpio', 7): """# ♀℞ Vénus rétrograde en Scorpion — Maison 7

**En une phrase :** Les relations de couple intenses et les enjeux de pouvoir relationnels sont en révision profonde.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec l'intensité du Scorpion. Les relations de couple avec des enjeux de contrôle ou de fusion sont à réviser. La transformation des dynamiques relationnelles est au premier plan.

## Ce que tu pourrais vivre
- Une révision des enjeux de pouvoir dans le couple
- Des dynamiques de contrôle à transformer
- Le retour d'ex avec qui la relation était fusionnelle

## Conseils pour cette période
- L'amour n'est pas le contrôle
- La fusion n'est pas l'intimité vraie
- Les ex intenses ont des leçons profondes""",

    ('scorpio', 8): """# ♀℞ Vénus rétrograde en Scorpion — Maison 8

**En une phrase :** L'intimité profonde et les finances partagées sont en révision majeure.

## L'énergie du moment
Vénus rétrograde est très puissante en Scorpion dans la maison 8. L'intimité, la sexualité, les finances partagées, tout ce qui est profond et partagé est en révision majeure. C'est une période de transformation relationnelle intense.

## Ce que tu pourrais vivre
- Une révision majeure de l'intimité
- Des transformations profondes dans le partage
- Le retour de passions ou de situations du passé

## Conseils pour cette période
- L'intimité vraie est transformatrice
- Le partage financier demande de la transparence
- Les retours du passé sont des occasions de guérison""",

    ('scorpio', 9): """# ♀℞ Vénus rétrograde en Scorpion — Maison 9

**En une phrase :** Les croyances profondes sur l'amour et les voyages transformateurs sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec la profondeur du Scorpion. Tes croyances profondes sur l'amour, le pouvoir et la transformation sont à réviser. Les voyages qui transforment méritent d'être reconsidérés.

## Ce que tu pourrais vivre
- Une révision des croyances profondes sur l'amour
- Des voyages transformateurs compliqués
- Un questionnement sur le sens de la transformation

## Conseils pour cette période
- Les croyances sur l'amour évoluent
- La vraie transformation ne force pas
- Les voyages intérieurs sont aussi valides""",

    ('scorpio', 10): """# ♀℞ Vénus rétrograde en Scorpion — Maison 10

**En une phrase :** Ton pouvoir professionnel et les relations de travail intenses sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec l'intensité du Scorpion. Ton image de personne puissante et tes relations professionnelles intenses sont en révision. Les enjeux de pouvoir au travail méritent d'être transformés.

## Ce que tu pourrais vivre
- Une révision de ton pouvoir professionnel
- Des relations de travail intenses à transformer
- Le retour d'opportunités ou de contacts du passé

## Conseils pour cette période
- Le vrai pouvoir n'a pas besoin de contrôle
- Les relations professionnelles saines sont équilibrées
- Les opportunités du passé peuvent revenir transformées""",

    ('scorpio', 11): """# ♀℞ Vénus rétrograde en Scorpion — Maison 11

**En une phrase :** Les amitiés intenses et les groupes transformateurs sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec l'intensité du Scorpion. Les amitiés où les enjeux sont profonds sont à réviser. Les groupes qui transforment mais aussi qui contrôlent méritent attention.

## Ce que tu pourrais vivre
- Une révision des amitiés intenses
- Des groupes avec des dynamiques de pouvoir à examiner
- Le retour d'amis profonds du passé

## Conseils pour cette période
- Les vraies amitiés transforment sans contrôler
- Les groupes sains permettent l'autonomie
- Les amis profonds du passé ont des leçons""",

    ('scorpio', 12): """# ♀℞ Vénus rétrograde en Scorpion — Maison 12

**En une phrase :** Les passions secrètes et les transformations inconscientes sont en révision profonde.

## L'énergie du moment
Vénus rétrograde est très puissante en Scorpion dans la maison 12. Les passions secrètes, les désirs cachés, les transformations inconscientes sont révélés. C'est une période majeure de révision des profondeurs.

## Ce que tu pourrais vivre
- Des passions secrètes qui remontent
- Des désirs cachés révélés
- Des transformations inconscientes qui deviennent conscientes

## Conseils pour cette période
- Les secrets intérieurs méritent d'être accueillis
- Les désirs cachés ont leur sagesse
- La transformation consciente est plus puissante""",
}

async def insert_interpretations():
    """Insert all venus_retrograde interpretations for Leo, Virgo, Libra, Scorpio"""
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
