#!/usr/bin/env python3
"""
Insert transit_chiron interpretations V2 for Sagittarius, Capricorn, Aquarius, Pisces (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_CHIRON_INTERPRETATIONS = {
    # ============== SAGITTARIUS ==============
    ('sagittarius', 1): """# ⚷ Chiron en Sagittaire – Maison I

**En une phrase :** Un temps pour guérir les blessures liées au sens de la vie, à la foi et à ta quête de vérité.

## L'énergie du moment
Chiron en Sagittaire dans ta maison I active des blessures profondes liées à ta recherche de sens, ta foi brisée et ton droit d'avoir une vision. C'est une guérison de l'identité de chercheur.

## Ce que tu pourrais vivre
- Un sentiment douloureux de perte de sens ou de direction
- Des blessures liées à des croyances qui t'ont déçu(e)
- Une opportunité de guérir en aidant les autres à trouver leur sens

## Conseils pour ce transit
- Ta blessure de sens peut devenir ton don pour guider les autres dans leur quête
- Le sens existe même quand il semble perdu
- Guéris en créant ton propre système de croyances authentique""",

    ('sagittarius', 2): """# ⚷ Chiron en Sagittaire – Maison II

**En une phrase :** Une période pour guérir les blessures liées aux promesses non tenues et à l'optimisme financier trahi.

## L'énergie du moment
Chiron en Sagittaire dans ta maison des ressources active des blessures autour des promesses d'abondance non réalisées, de la foi naïve en l'argent et des espoirs matériels déçus.

## Ce que tu pourrais vivre
- Des déceptions financières qui ont brisé ton optimisme
- Un questionnement sur ce qui constitue la vraie richesse
- Une opportunité de guérir en développant une foi mature en l'abondance

## Conseils pour ce transit
- Ta blessure d'espoir peut devenir ton don pour enseigner une prospérité sage
- L'abondance vraie ne repose pas sur l'optimisme aveugle
- Guéris en développant une foi réaliste en la vie qui pourvoit""",

    ('sagittarius', 3): """# ⚷ Chiron en Sagittaire – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à l'enseignement, aux grandes idées et à la communication de ta vérité.

## L'énergie du moment
Chiron en Sagittaire dans ta maison de la communication active des blessures liées à ta légitimité d'enseigner, de partager ta vision et de communiquer les grandes vérités.

## Ce que tu pourrais vivre
- Un sentiment de ne pas être légitime pour enseigner ou partager
- Des blessures liées à des professeurs ou à des enseignements qui ont fait mal
- Une opportunité de guérir en communiquant ta sagesse durement acquise

## Conseils pour ce transit
- Ta blessure d'enseignement peut devenir ton don de transmission authentique
- Tu as le droit de partager ta vérité
- Guéris en osant enseigner ce que tu as appris par la douleur""",

    ('sagittarius', 4): """# ⚷ Chiron en Sagittaire – Maison IV

**En une phrase :** Une période pour guérir les blessures liées aux croyances familiales et à la foi transmise.

## L'énergie du moment
Chiron en Sagittaire dans ta maison des racines active des blessures liées aux croyances familiales imposées, à la religion de l'enfance ou au manque de sens dans le foyer.

## Ce que tu pourrais vivre
- Des blessures liées aux croyances religieuses ou philosophiques familiales
- Un questionnement sur les vérités transmises par ta lignée
- Une opportunité de guérir en créant un foyer ouvert à la quête de sens

## Conseils pour ce transit
- Ta blessure de foi familiale peut devenir ton don pour libérer les autres des dogmes hérités
- Tu peux choisir tes propres croyances
- Guéris en créant un foyer où chacun peut chercher sa propre vérité""",

    ('sagittarius', 5): """# ⚷ Chiron en Sagittaire – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à la joie de croire, à l'optimisme amoureux et à la créativité inspirée.

## L'énergie du moment
Chiron en Sagittaire dans ta maison de la joie active des blessures liées à l'enthousiasme trahi, aux amours qui ont brisé la foi et à la créativité inspirée qui s'est heurtée au réel.

## Ce que tu pourrais vivre
- Des amours qui ont brisé ton optimisme
- Une créativité qui a été découragée ou moquée
- Une opportunité de guérir en retrouvant la joie de croire

## Conseils pour ce transit
- Ta blessure d'enthousiasme peut devenir ton don pour raviver l'espoir des autres
- La joie peut revenir même après les déceptions
- Guéris en osant à nouveau croire et créer avec foi""",

    ('sagittarius', 6): """# ⚷ Chiron en Sagittaire – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au sens du travail et à la quête dans le quotidien.

## L'énergie du moment
Chiron en Sagittaire dans ta maison du travail active des blessures autour du manque de sens dans le travail, de la routine qui tue l'âme et de la santé affectée par la perte de foi.

## Ce que tu pourrais vivre
- Un travail qui a perdu son sens et sa flamme
- Des problèmes de santé liés à un manque de direction
- Une opportunité de guérir en trouvant le sacré dans le quotidien

## Conseils pour ce transit
- Ta blessure de sens au travail peut devenir ton don pour inspirer les autres dans leur quotidien
- Le sens peut exister dans les petites choses
- Guéris en apportant ta quête dans tes routines""",

    ('sagittarius', 7): """# ⚷ Chiron en Sagittaire – Maison VII

**En une phrase :** Un temps pour guérir les blessures liées aux partenaires qui ont brisé ta foi ou limité ta liberté.

## L'énergie du moment
Chiron en Sagittaire dans ta maison des partenariats active des blessures liées à des relations qui ont étouffé ta liberté, trahi ta confiance ou brisé tes idéaux.

## Ce que tu pourrais vivre
- Des relations qui ont limité ton expansion ou ta quête
- Un questionnement sur la possibilité d'être en couple ET libre
- Une opportunité de guérir en créant des relations qui élèvent

## Conseils pour ce transit
- Ta blessure de liberté relationnelle peut devenir ton don pour aider les couples à grandir ensemble
- L'amour peut libérer plutôt qu'emprisonner
- Guéris en trouvant des partenaires qui partagent ta quête""",

    ('sagittarius', 8): """# ⚷ Chiron en Sagittaire – Maison VIII

**En une phrase :** Une période pour guérir les blessures liées à la perte de sens dans les crises et à la foi testée.

## L'énergie du moment
Chiron en Sagittaire dans ta maison des profondeurs active des blessures liées aux crises qui ont brisé ta foi, aux transformations qui ont semblé dénuées de sens et aux pertes qui ont ébranlé tes croyances.

## Ce que tu pourrais vivre
- Des crises qui ont détruit tes croyances
- Un questionnement sur le sens de la souffrance et de la mort
- Une opportunité de guérir en trouvant le sens au cœur des ténèbres

## Conseils pour ce transit
- Ta blessure de foi testée peut devenir ton don pour accompagner les autres dans les nuits de l'âme
- Le sens peut survivre aux pires épreuves
- Guéris en développant une foi qui n'a pas peur des ténèbres""",

    ('sagittarius', 9): """# ⚷ Chiron en Sagittaire – Maison IX

**En une phrase :** Un temps pour guérir les blessures profondes liées à la quête de vérité et à la foi.

## L'énergie du moment
Chiron en Sagittaire est dans sa maison naturelle, activant les blessures les plus profondes liées à ta recherche de sens, tes croyances et ta vision de la vie. C'est la guérison du chercheur de vérité.

## Ce que tu pourrais vivre
- Une crise de foi profonde ou une remise en question totale
- Des blessures liées à des maîtres spirituels ou des enseignements
- Une opportunité de devenir un vrai sage par tes propres blessures

## Conseils pour ce transit
- Ta blessure de foi peut devenir ton plus grand don de sagesse authentique
- La vérité existe au-delà de toutes les croyances brisées
- Guéris en trouvant ta propre vérité au cœur de tes doutes""",

    ('sagittarius', 10): """# ⚷ Chiron en Sagittaire – Maison X

**En une phrase :** Une période pour guérir les blessures liées à ta vocation, ta vision publique et ta mission de vie.

## L'énergie du moment
Chiron en Sagittaire dans ta maison de la carrière active des blessures liées à ta mission de vie, à ta vision professionnelle et à ta légitimité d'inspirer à grande échelle.

## Ce que tu pourrais vivre
- Un questionnement douloureux sur ta mission de vie
- Des blessures liées à une vocation frustrée ou incomprise
- Une opportunité de guérir en assumant publiquement ta vision

## Conseils pour ce transit
- Ta blessure de mission peut devenir ton don pour aider les autres à trouver leur vocation
- Tu as une contribution unique à apporter au monde
- Guéris en osant porter ta vision dans le monde""",

    ('sagittarius', 11): """# ⚷ Chiron en Sagittaire – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées aux idéaux déçus et aux groupes qui ont trahi ta vision.

## L'énergie du moment
Chiron en Sagittaire dans ta maison des amitiés active des blessures autour des idéaux collectifs trahis, des causes qui ont déçu et des groupes qui n'étaient pas à la hauteur de leurs promesses.

## Ce que tu pourrais vivre
- Des déceptions avec des mouvements ou des groupes idéalistes
- Un questionnement sur la possibilité de changer le monde
- Une opportunité de guérir en portant des idéaux avec sagesse

## Conseils pour ce transit
- Ta blessure d'idéaux peut devenir ton don pour porter des visions réalistes mais inspirantes
- Les idéaux peuvent survivre aux déceptions
- Guéris en portant une espérance mature""",

    ('sagittarius', 12): """# ⚷ Chiron en Sagittaire – Maison XII

**En une phrase :** Une période pour guérir les blessures karmiques liées à la foi, aux vies passées de chercheur et au sens perdu.

## L'énergie du moment
Chiron en Sagittaire dans ta maison de l'invisible active des blessures karmiques liées à des vies de quête, à des enseignements qui ont mal tourné et à la foi perdue à travers les incarnations.

## Ce que tu pourrais vivre
- Des souvenirs d'autres vies où ta foi a été brisée
- Un karma de chercheur déçu ou de faux prophète
- Une opportunité de guérir en te reconnectant à la vérité au-delà de toutes les croyances

## Conseils pour ce transit
- Ta blessure de foi karmique peut devenir ton don de sagesse universelle
- La vérité existe au-delà de toutes les formes qu'elle a prises
- Guéris en trouvant la source de toute sagesse en toi""",

    # ============== CAPRICORN ==============
    ('capricorn', 1): """# ⚷ Chiron en Capricorne – Maison I

**En une phrase :** Un temps pour guérir les blessures liées à l'autorité, la responsabilité et le droit de réussir.

## L'énergie du moment
Chiron en Capricorne dans ta maison I active des blessures profondes liées à ton rapport à l'autorité, tes responsabilités et ton droit d'être reconnu(e). C'est une guérison de l'identité mature.

## Ce que tu pourrais vivre
- Un sentiment de porter trop de responsabilités ou pas assez de reconnaissance
- Des blessures liées à des figures d'autorité (père, patrons)
- Une opportunité de guérir en devenant une autorité bienveillante

## Conseils pour ce transit
- Ta blessure d'autorité peut devenir ton don pour aider les autres à assumer leur pouvoir
- Tu mérites le succès et la reconnaissance
- Guéris en apprenant à être ton propre parent intérieur bienveillant""",

    ('capricorn', 2): """# ⚷ Chiron en Capricorne – Maison II

**En une phrase :** Une période pour guérir les blessures liées au travail acharné non récompensé et à la valeur du mérite.

## L'énergie du moment
Chiron en Capricorne dans ta maison des ressources active des blessures autour du travail non reconnu, de l'effort sans récompense et de la valeur liée uniquement à la production.

## Ce que tu pourrais vivre
- Un sentiment d'avoir travaillé dur sans jamais recevoir ce que tu mérites
- Des blessures liées à la pauvreté ou à la peur de l'échec financier
- Une opportunité de guérir en reconnaissant ta valeur au-delà de la productivité

## Conseils pour ce transit
- Ta blessure de non-reconnaissance peut devenir ton don pour valoriser le travail des autres
- Ta valeur ne dépend pas uniquement de ce que tu produis
- Guéris en apprenant à recevoir sans avoir à le mériter totalement""",

    ('capricorn', 3): """# ⚷ Chiron en Capricorne – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à la communication structurée et à la parole d'autorité.

## L'énergie du moment
Chiron en Capricorne dans ta maison de la communication active des blessures liées à ta parole prise au sérieux, à ta légitimité de communiquer et à des éducateurs sévères.

## Ce que tu pourrais vivre
- Un sentiment de ne pas être pris(e) au sérieux quand tu parles
- Des blessures liées à l'éducation rigide ou à la critique
- Une opportunité de guérir en communiquant avec autorité et compassion

## Conseils pour ce transit
- Ta blessure de communication peut devenir ton don pour enseigner avec sagesse
- Ta parole a du poids quand tu assumes ton autorité
- Guéris en apprenant à communiquer avec structure ET cœur""",

    ('capricorn', 4): """# ⚷ Chiron en Capricorne – Maison IV

**En une phrase :** Une période pour guérir les blessures liées au père absent ou trop strict et aux responsabilités familiales précoces.

## L'énergie du moment
Chiron en Capricorne dans ta maison des racines active des blessures profondes liées au père, aux responsabilités d'adulte prises trop tôt et au manque de soutien parental structurant.

## Ce que tu pourrais vivre
- Des souvenirs d'un père absent, froid ou trop exigeant
- Un passé où tu as dû être responsable trop tôt
- Une opportunité de guérir en créant le foyer stable que tu n'as pas eu

## Conseils pour ce transit
- Ta blessure paternelle peut devenir ton don pour être un parent présent et structurant
- Tu peux te donner maintenant la structure et le soutien dont tu as manqué
- Guéris en devenant le parent intérieur que tu aurais voulu avoir""",

    ('capricorn', 5): """# ⚷ Chiron en Capricorne – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à la joie interdite, au jeu vu comme perte de temps et à la créativité « sérieuse ».

## L'énergie du moment
Chiron en Capricorne dans ta maison de la joie active des blessures liées à la culpabilité de s'amuser, à la créativité jugée non productive et aux amours trop sérieuses.

## Ce que tu pourrais vivre
- Une difficulté à t'amuser sans culpabilité
- Des blessures liées à une créativité réprimée parce que « non sérieuse »
- Une opportunité de guérir en intégrant joie et responsabilité

## Conseils pour ce transit
- Ta blessure de joie peut devenir ton don pour aider les autres à s'accorder le plaisir
- Le jeu a de la valeur en soi
- Guéris en t'autorisant le plaisir sans le mériter par le travail""",

    ('capricorn', 6): """# ⚷ Chiron en Capricorne – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au travail comme seule valeur et à la santé négligée pour la carrière.

## L'énergie du moment
Chiron en Capricorne dans ta maison du travail active des blessures autour du workaholisme, de la santé sacrifiée sur l'autel du devoir et de la valeur uniquement par le travail.

## Ce que tu pourrais vivre
- Un épuisement professionnel ou des problèmes de santé liés au travail excessif
- Un questionnement sur la valeur de tout ce travail
- Une opportunité de guérir en trouvant un équilibre travail-santé

## Conseils pour ce transit
- Ta blessure de surmenage peut devenir ton don pour aider les autres à trouver l'équilibre
- Tu as de la valeur même quand tu ne travailles pas
- Guéris en prenant soin de ton corps autant que de ta carrière""",

    ('capricorn', 7): """# ⚷ Chiron en Capricorne – Maison VII

**En une phrase :** Un temps pour guérir les blessures liées aux relations de devoir et aux partenariats trop structurés.

## L'énergie du moment
Chiron en Capricorne dans ta maison des partenariats active des blessures liées aux relations basées sur le devoir plutôt que l'amour, aux partenaires froids ou aux mariages de raison.

## Ce que tu pourrais vivre
- Des relations où le devoir a remplacé l'amour
- Un questionnement sur ce qu'est un vrai engagement
- Une opportunité de guérir en créant des partenariats engagés ET aimants

## Conseils pour ce transit
- Ta blessure de relation froide peut devenir ton don pour aider les couples à allier engagement et chaleur
- L'engagement peut coexister avec la tendresse
- Guéris en apprenant que l'amour n'exclut pas la responsabilité""",

    ('capricorn', 8): """# ⚷ Chiron en Capricorne – Maison VIII

**En une phrase :** Une période pour guérir les blessures liées au contrôle face à la mort et au pouvoir froid.

## L'énergie du moment
Chiron en Capricorne dans ta maison des profondeurs active des blessures liées au contrôle face à ce qui ne peut être contrôlé, au pouvoir exercé sans cœur et à la peur de perdre le contrôle.

## Ce que tu pourrais vivre
- Une peur profonde de perdre le contrôle dans les crises
- Des blessures liées à des abus de pouvoir ou à des héritages conflictuels
- Une opportunité de guérir en acceptant le lâcher-prise structuré

## Conseils pour ce transit
- Ta blessure de contrôle peut devenir ton don pour aider les autres à traverser les transitions avec structure et grâce
- Le vrai pouvoir inclut le lâcher-prise
- Guéris en apprenant à faire confiance au processus de transformation""",

    ('capricorn', 9): """# ⚷ Chiron en Capricorne – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées aux croyances rigides et à la foi sans joie.

## L'énergie du moment
Chiron en Capricorne dans ta maison de l'expansion active des blessures autour des systèmes de croyances trop rigides, de la spiritualité comme devoir et de l'enseignement autoritaire.

## Ce que tu pourrais vivre
- Des blessures liées à une éducation religieuse trop stricte
- Un questionnement sur la différence entre structure et rigidité
- Une opportunité de guérir en enseignant une sagesse structurée mais ouverte

## Conseils pour ce transit
- Ta blessure de dogme peut devenir ton don pour créer des cadres souples de compréhension
- La structure peut servir la liberté spirituelle
- Guéris en trouvant une foi qui structure sans étouffer""",

    ('capricorn', 10): """# ⚷ Chiron en Capricorne – Maison X

**En une phrase :** Une période pour guérir les blessures profondes liées à la réussite, au père et à l'autorité.

## L'énergie du moment
Chiron en Capricorne est dans sa maison naturelle, activant les blessures les plus profondes liées à la carrière, au succès et aux figures d'autorité. C'est la guérison de la vocation par excellence.

## Ce que tu pourrais vivre
- Des blessures profondes liées au père ou aux figures d'autorité
- Un sentiment de ne jamais être assez bon(ne) professionnellement
- Une opportunité de devenir une autorité guérisseuse

## Conseils pour ce transit
- Ta blessure d'autorité peut devenir ton plus grand don de leadership compatissant
- Tu mérites ta place au sommet
- Guéris en devenant l'autorité que tu aurais voulu rencontrer""",

    ('capricorn', 11): """# ⚷ Chiron en Capricorne – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées à la structure des groupes et aux idéaux pragmatiques.

## L'énergie du moment
Chiron en Capricorne dans ta maison des amitiés active des blessures autour des groupes trop hiérarchiques, des idéaux trop rigides et des amitiés de devoir plutôt que de cœur.

## Ce que tu pourrais vivre
- Des expériences douloureuses dans des organisations hiérarchiques
- Un questionnement sur comment porter des idéaux avec réalisme
- Une opportunité de guérir en créant des structures sociales efficaces et humaines

## Conseils pour ce transit
- Ta blessure de groupe peut devenir ton don pour créer des organisations saines
- La structure peut servir l'humanité
- Guéris en apportant du cœur aux systèmes""",

    ('capricorn', 12): """# ⚷ Chiron en Capricorne – Maison XII

**En une phrase :** Une période pour guérir les blessures karmiques liées à l'autorité, au pouvoir et à la solitude du leadership.

## L'énergie du moment
Chiron en Capricorne dans ta maison de l'invisible active des blessures karmiques liées aux vies de pouvoir, d'autorité ou de solitude au sommet. C'est une guérison de l'âme de leader.

## Ce que tu pourrais vivre
- Des souvenirs d'autres vies de responsabilité ou de solitude
- Un karma de leadership à transmuter
- Une opportunité de guérir en servant depuis une autorité humble

## Conseils pour ce transit
- Ta blessure de pouvoir karmique peut devenir ton don de leadership spirituel
- L'autorité vraie est au service de tous
- Guéris en mettant ta structure intérieure au service du divin""",

    # ============== AQUARIUS ==============
    ('aquarius', 1): """# ⚷ Chiron en Verseau – Maison I

**En une phrase :** Un temps pour guérir les blessures liées à ta différence, ton originalité et ton sentiment d'être à part.

## L'énergie du moment
Chiron en Verseau dans ta maison I active des blessures profondes liées à ton unicité, ta différence et ton sentiment d'aliénation. C'est une guérison de l'identité unique.

## Ce que tu pourrais vivre
- Un sentiment douloureux d'être trop différent(e) pour appartenir
- Des blessures liées au rejet de ton originalité
- Une opportunité de guérir en aidant les autres à embrasser leur différence

## Conseils pour ce transit
- Ta blessure de différence peut devenir ton don pour valoriser l'unicité de chacun
- Ta singularité est ta force, pas ta malédiction
- Guéris en acceptant pleinement ce qui te rend unique""",

    ('aquarius', 2): """# ⚷ Chiron en Verseau – Maison II

**En une phrase :** Une période pour guérir les blessures liées à la valeur de l'originalité et aux revenus non conventionnels.

## L'énergie du moment
Chiron en Verseau dans ta maison des ressources active des blessures autour de la difficulté à monétiser tes talents uniques et à trouver ta valeur dans un monde qui ne comprend pas ta différence.

## Ce que tu pourrais vivre
- Des difficultés à faire reconnaître la valeur de tes idées innovantes
- Un questionnement sur comment vivre de ta singularité
- Une opportunité de guérir en aidant les autres à valoriser leur originalité

## Conseils pour ce transit
- Ta blessure de valeur unique peut devenir ton don pour aider les marginaux à prospérer
- L'innovation a de la valeur même quand le monde ne la voit pas encore
- Guéris en créant tes propres chemins de prospérité""",

    ('aquarius', 3): """# ⚷ Chiron en Verseau – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à la pensée différente et à la communication innovante.

## L'énergie du moment
Chiron en Verseau dans ta maison de la communication active des blessures liées à ta façon unique de penser, au rejet de tes idées avant-gardistes et à ta communication hors norme.

## Ce que tu pourrais vivre
- Un sentiment de ne pas être compris(e) quand tu partages tes idées
- Des blessures liées au rejet de ta façon de penser
- Une opportunité de guérir en créant des ponts de communication pour les idées nouvelles

## Conseils pour ce transit
- Ta blessure de pensée différente peut devenir ton don pour traduire l'innovation
- Tes idées ont de la valeur même si elles sont en avance
- Guéris en trouvant ceux qui comprennent ta langue""",

    ('aquarius', 4): """# ⚷ Chiron en Verseau – Maison IV

**En une phrase :** Une période pour guérir les blessures liées à la différence dans la famille et au sentiment de ne pas appartenir à sa lignée.

## L'énergie du moment
Chiron en Verseau dans ta maison des racines active des blessures liées au sentiment d'être l'alien de la famille, le mouton noir ou celui/celle qui ne rentre pas dans le moule familial.

## Ce que tu pourrais vivre
- Des souvenirs d'avoir été le « différent » de la famille
- Un questionnement sur ton appartenance à ta lignée
- Une opportunité de guérir en créant ta propre famille de choix

## Conseils pour ce transit
- Ta blessure d'appartenance peut devenir ton don pour accueillir les « différents »
- Tu peux aimer ta famille ET être toi-même
- Guéris en créant un foyer qui célèbre l'unicité""",

    ('aquarius', 5): """# ⚷ Chiron en Verseau – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à la créativité avant-gardiste et aux amours atypiques.

## L'énergie du moment
Chiron en Verseau dans ta maison de la joie active des blessures liées à la créativité trop originale, aux amours non conventionnelles et à la joie d'être différent qui dérange.

## Ce que tu pourrais vivre
- Des créations rejetées parce que trop innovantes
- Des amours atypiques qui ont fait souffrir
- Une opportunité de guérir en célébrant les expressions uniques

## Conseils pour ce transit
- Ta blessure créative peut devenir ton don pour libérer l'expression originale des autres
- L'amour prend toutes les formes
- Guéris en osant créer et aimer à ta façon unique""",

    ('aquarius', 6): """# ⚷ Chiron en Verseau – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au travail innovant et à la santé atypique.

## L'énergie du moment
Chiron en Verseau dans ta maison du travail active des blessures autour du travail non conventionnel, de la santé hors norme et de la difficulté à s'insérer dans le monde professionnel standard.

## Ce que tu pourrais vivre
- Des difficultés à trouver ta place dans un travail « normal »
- Des problèmes de santé atypiques ou incompris
- Une opportunité de guérir en créant des approches de travail et de santé innovantes

## Conseils pour ce transit
- Ta blessure professionnelle peut devenir ton don pour créer de nouvelles façons de travailler
- Ton corps unique a besoin de soins uniques
- Guéris en inventant ton propre chemin quotidien""",

    ('aquarius', 7): """# ⚷ Chiron en Verseau – Maison VII

**En une phrase :** Un temps pour guérir les blessures liées aux relations atypiques et au besoin de liberté en amour.

## L'énergie du moment
Chiron en Verseau dans ta maison des partenariats active des blessures liées aux relations non conventionnelles, au besoin de liberté dans l'amour et au rejet à cause de ta différence.

## Ce que tu pourrais vivre
- Des relations qui n'ont pas survécu à ton besoin de liberté
- Un questionnement sur la possibilité d'être aimé(e) tel(le) que tu es
- Une opportunité de guérir en créant des partenariats qui honorent l'unicité

## Conseils pour ce transit
- Ta blessure relationnelle peut devenir ton don pour aider les couples atypiques
- L'amour peut respecter la liberté de chacun
- Guéris en trouvant ceux qui célèbrent ta différence""",

    ('aquarius', 8): """# ⚷ Chiron en Verseau – Maison VIII

**En une phrase :** Une période pour guérir les blessures liées à l'aliénation profonde et au sentiment d'être un étranger dans ce monde.

## L'énergie du moment
Chiron en Verseau dans ta maison des profondeurs active des blessures liées à un sentiment d'aliénation existentielle, de ne pas être de cette planète ou de ce temps.

## Ce que tu pourrais vivre
- Un sentiment profond de ne pas appartenir à ce monde
- Des transformations liées à ta différence radicale
- Une opportunité de guérir en comprenant ta mission d'avant-garde

## Conseils pour ce transit
- Ta blessure d'aliénation peut devenir ton don pour accompagner les autres « étrangers »
- Tu es peut-être ici pour apporter quelque chose de nouveau
- Guéris en acceptant ta mission de pont vers le futur""",

    ('aquarius', 9): """# ⚷ Chiron en Verseau – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées aux croyances avant-gardistes et à la vision trop en avance.

## L'énergie du moment
Chiron en Verseau dans ta maison de l'expansion active des blessures autour de visions du monde trop en avance, de croyances rejetées et d'enseignements trop innovants.

## Ce que tu pourrais vivre
- Des idées philosophiques rejetées parce que trop avant-gardistes
- Des blessures liées à une vision du monde incomprise
- Une opportunité de guérir en partageant ta vision quand le monde est prêt

## Conseils pour ce transit
- Ta blessure de vision peut devenir ton don pour préparer le futur
- Les idées en avance sur leur temps finissent par être comprises
- Guéris en faisant confiance à ton timing unique""",

    ('aquarius', 10): """# ⚷ Chiron en Verseau – Maison X

**En une phrase :** Une période pour guérir les blessures liées à une carrière atypique et à une place unique dans le monde.

## L'énergie du moment
Chiron en Verseau dans ta maison de la carrière active des blessures liées à une vocation hors norme, à un parcours professionnel atypique et à la difficulté d'être reconnu(e) pour ta différence.

## Ce que tu pourrais vivre
- Une carrière qui ne rentre pas dans les cases
- Des blessures liées à la non-reconnaissance de ton apport unique
- Une opportunité de guérir en créant ta propre catégorie professionnelle

## Conseils pour ce transit
- Ta blessure de carrière unique peut devenir ton don pour aider les autres à sortir des sentiers battus
- Tu peux créer un chemin qui n'existe pas encore
- Guéris en assumant pleinement ta place de pionnier""",

    ('aquarius', 11): """# ⚷ Chiron en Verseau – Maison XI

**En une phrase :** Un temps pour guérir les blessures profondes liées à l'appartenance, aux groupes et à la différence sociale.

## L'énergie du moment
Chiron en Verseau est dans sa maison naturelle, activant les blessures les plus profondes liées à l'appartenance, aux cercles sociaux et au sentiment de ne jamais trouver sa tribu.

## Ce que tu pourrais vivre
- Un sentiment profond de ne jamais vraiment appartenir à aucun groupe
- Des blessures liées au rejet social de ta différence
- Une opportunité de créer des communautés pour les « différents »

## Conseils pour ce transit
- Ta blessure d'appartenance peut devenir ton plus grand don pour créer des espaces d'accueil
- Ta tribu existe, elle est peut-être simplement dispersée
- Guéris en rassemblant ceux qui, comme toi, cherchent leur place""",

    ('aquarius', 12): """# ⚷ Chiron en Verseau – Maison XII

**En une phrase :** Une période pour guérir les blessures karmiques liées à l'aliénation cosmique et à la différence de l'âme.

## L'énergie du moment
Chiron en Verseau dans ta maison de l'invisible active des blessures karmiques liées à un sentiment d'être étranger à cette dimension, des vies d'isolement et une différence de l'âme.

## Ce que tu pourrais vivre
- Un sentiment de ne pas venir de cette planète ou cette dimension
- Des blessures de vies passées liées à l'exclusion pour différence
- Une opportunité de guérir en te reconnectant à ta famille cosmique

## Conseils pour ce transit
- Ta blessure d'alien cosmique peut devenir ton don pour aider les âmes perdues à retrouver leur chemin
- Tu appartiens à l'univers tout entier
- Guéris en te souvenant de ton origine stellaire""",

    # ============== PISCES ==============
    ('pisces', 1): """# ⚷ Chiron en Poissons – Maison I

**En une phrase :** Un temps pour guérir les blessures liées à la sensibilité extrême, à la dissolution du moi et à la victimisation.

## L'énergie du moment
Chiron en Poissons dans ta maison I active des blessures profondes liées à ta sensibilité, ta perméabilité aux souffrances du monde et ta tendance à te perdre. C'est une guérison de l'identité spirituelle.

## Ce que tu pourrais vivre
- Un sentiment d'être trop sensible pour ce monde
- Des blessures liées à la perte de soi ou au sacrifice
- Une opportunité de guérir en aidant les autres ultra-sensibles

## Conseils pour ce transit
- Ta blessure de sensibilité peut devenir ton don d'empathie guérissante
- Ta porosité est un canal, pas une faiblesse
- Guéris en apprenant à être un canal sans te perdre""",

    ('pisces', 2): """# ⚷ Chiron en Poissons – Maison II

**En une phrase :** Une période pour guérir les blessures liées au détachement des biens matériels et à la difficulté de s'incarner.

## L'énergie du moment
Chiron en Poissons dans ta maison des ressources active des blessures autour du rapport flou à l'argent, de la difficulté à posséder et de la confusion entre spirituel et matériel.

## Ce que tu pourrais vivre
- Des difficultés à gérer l'argent ou à te sentir légitime d'en avoir
- Un questionnement sur la valeur du matériel dans une vie spirituelle
- Une opportunité de guérir en réconciliant spiritualité et prospérité

## Conseils pour ce transit
- Ta blessure de détachement peut devenir ton don pour aider les autres à avoir une relation saine avec l'argent
- L'abondance et la spiritualité ne sont pas incompatibles
- Guéris en t'incarnant pleinement dans le monde matériel""",

    ('pisces', 3): """# ⚷ Chiron en Poissons – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à la communication intuitive et à la parole non entendue.

## L'énergie du moment
Chiron en Poissons dans ta maison de la communication active des blessures liées à ta façon intuitive de communiquer, à la difficulté d'être compris(e) et à la parole qui se perd.

## Ce que tu pourrais vivre
- Un sentiment que personne ne comprend vraiment ce que tu veux dire
- Des blessures liées à une communication trop subtile ou confuse
- Une opportunité de guérir en devenant un canal de communication intuitive

## Conseils pour ce transit
- Ta blessure de communication peut devenir ton don pour traduire l'indicible
- L'intuition est une forme valide de communication
- Guéris en trouvant les mots pour ce qui n'en a pas""",

    ('pisces', 4): """# ⚷ Chiron en Poissons – Maison IV

**En une phrase :** Une période pour guérir les blessures liées à un foyer chaotique, aux addictions familiales et au sacrifice maternel.

## L'énergie du moment
Chiron en Poissons dans ta maison des racines active des blessures profondes liées à un foyer où régnait la confusion, l'addiction ou le sacrifice, et au manque de limites familiales.

## Ce que tu pourrais vivre
- Des souvenirs d'un foyer chaotique ou empreint d'addictions
- Un questionnement sur ce qu'est un vrai sanctuaire
- Une opportunité de guérir en créant un foyer paisible et ancré

## Conseils pour ce transit
- Ta blessure familiale peut devenir ton don pour créer des havres de paix
- Tu mérites un foyer avec des limites saines
- Guéris en créant le sanctuaire que tu n'as pas eu""",

    ('pisces', 5): """# ⚷ Chiron en Poissons – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à la créativité sacrifiée et aux amours fusionnelles.

## L'énergie du moment
Chiron en Poissons dans ta maison de la joie active des blessures liées à la créativité qui se dissout, aux amours où tu te perds et à la difficulté de trouver une joie saine.

## Ce que tu pourrais vivre
- Une créativité bloquée par la peur de se dissoudre
- Des amours où tu as perdu ton identité
- Une opportunité de guérir en canalisant l'inspiration divine

## Conseils pour ce transit
- Ta blessure créative peut devenir ton don de canalisation artistique
- L'amour peut être transcendant sans être destructeur
- Guéris en créant comme un canal, pas comme un sacrifice""",

    ('pisces', 6): """# ⚷ Chiron en Poissons – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au service sacrificiel et à la santé comme mystère.

## L'énergie du moment
Chiron en Poissons dans ta maison du travail active des blessures autour du service qui se perd dans le sacrifice, des maladies mystérieuses et du travail de guérison.

## Ce que tu pourrais vivre
- Un épuisement par un service sans limites
- Des problèmes de santé d'origine mystérieuse ou spirituelle
- Une opportunité de guérir en servant avec discernement

## Conseils pour ce transit
- Ta blessure de service peut devenir ton don de guérison spirituelle
- Servir n'est pas se sacrifier
- Guéris en apprenant les limites sacrées du don""",

    ('pisces', 7): """# ⚷ Chiron en Poissons – Maison VII

**En une phrase :** Un temps pour guérir les blessures liées aux relations où tu te perds et au sauveur-victime.

## L'énergie du moment
Chiron en Poissons dans ta maison des partenariats active des blessures liées aux relations fusionnelles, au schéma sauveur-victime et à la perte de soi dans l'autre.

## Ce que tu pourrais vivre
- Des relations où tu as joué le sauveur ou la victime
- Un questionnement sur comment être en relation sans se perdre
- Une opportunité de guérir en créant des relations conscientes

## Conseils pour ce transit
- Ta blessure relationnelle peut devenir ton don pour aider les relations codépendantes
- L'amour vrai n'exige pas la dissolution
- Guéris en apprenant l'amour qui respecte les frontières""",

    ('pisces', 8): """# ⚷ Chiron en Poissons – Maison VIII

**En une phrase :** Une période pour guérir les blessures liées à la dissolution dans les crises et à la perte de limites dans l'intimité.

## L'énergie du moment
Chiron en Poissons dans ta maison des profondeurs active des blessures liées à la dissolution traumatique, à la perte de soi dans les crises et aux expériences de mort approchée.

## Ce que tu pourrais vivre
- Des crises où tu as perdu tout sens de toi-même
- Des blessures liées à des expériences aux frontières de la mort
- Une opportunité de guérir en accompagnant les autres dans les transitions

## Conseils pour ce transit
- Ta blessure de dissolution peut devenir ton don pour accompagner les passages
- Tu peux traverser les profondeurs sans te perdre
- Guéris en apprenant à naviguer l'océan sans te noyer""",

    ('pisces', 9): """# ⚷ Chiron en Poissons – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées à la foi naïve, aux illusions spirituelles et au martyre religieux.

## L'énergie du moment
Chiron en Poissons dans ta maison de l'expansion active des blessures autour de la foi qui a déçu, des gourous qui ont trahi et des illusions spirituelles brisées.

## Ce que tu pourrais vivre
- Des désillusions spirituelles profondes
- Des blessures liées à des enseignants qui ont abusé de ta confiance
- Une opportunité de guérir en développant un discernement spirituel

## Conseils pour ce transit
- Ta blessure de foi peut devenir ton don pour guider sans créer de dépendance
- La vraie spiritualité inclut le discernement
- Guéris en trouvant une foi mature qui a traversé les doutes""",

    ('pisces', 10): """# ⚷ Chiron en Poissons – Maison X

**En une phrase :** Une période pour guérir les blessures liées à la vocation sacrificielle et à la mission impossible.

## L'énergie du moment
Chiron en Poissons dans ta maison de la carrière active des blessures liées à une vocation de service qui t'a consumé(e), à des missions impossibles et au sacrifice public.

## Ce que tu pourrais vivre
- Une vocation de service qui a mené à l'épuisement
- Des blessures liées à des missions qui semblaient impossibles
- Une opportunité de guérir en servant le monde avec des limites saines

## Conseils pour ce transit
- Ta blessure de vocation peut devenir ton don pour aider les autres à servir sans s'épuiser
- Ta mission est réalisable avec les bonnes limites
- Guéris en servant de façon soutenable""",

    ('pisces', 11): """# ⚷ Chiron en Poissons – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées aux idéaux perdus et aux groupes qui ont trahi la vision.

## L'énergie du moment
Chiron en Poissons dans ta maison des amitiés active des blessures autour des utopies brisées, des groupes qui ont mal tourné et des amitiés où tu as été sacrifié(e).

## Ce que tu pourrais vivre
- Des déceptions avec des mouvements ou des communautés spirituelles
- Un questionnement sur la possibilité d'un monde meilleur
- Une opportunité de guérir en portant des idéaux avec sagesse

## Conseils pour ce transit
- Ta blessure d'utopie peut devenir ton don pour créer des communautés conscientes
- L'idéal peut exister avec du réalisme
- Guéris en portant une vision qui n'oublie pas l'humain""",

    ('pisces', 12): """# ⚷ Chiron en Poissons – Maison XII

**En une phrase :** Une période pour guérir les blessures les plus profondes de l'âme, la séparation du divin et la souffrance universelle.

## L'énergie du moment
Chiron en Poissons est dans sa maison naturelle, activant les blessures les plus profondes de l'âme – la séparation de la source, la souffrance karmique et la blessure d'incarnation. C'est la guérison ultime.

## Ce que tu pourrais vivre
- Un sentiment profond de séparation de la source divine
- Des blessures de toutes les vies qui remontent
- Une opportunité de guérison totale et de retour à l'unité

## Conseils pour ce transit
- Ta blessure de séparation peut devenir ton don ultime de reconnexion des âmes à la source
- Tu n'as jamais été vraiment séparé(e) de l'amour divin
- Guéris en te souvenant de ton unité avec tout ce qui est""",
}


async def insert_interpretations():
    """Insert Chiron transit interpretations for Sagittarius, Capricorn, Aquarius, Pisces"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_CHIRON_INTERPRETATIONS.items():
            # Check if exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_chiron',
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
                subject='transit_chiron',
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
        print(f"✅ Transit Chiron (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
