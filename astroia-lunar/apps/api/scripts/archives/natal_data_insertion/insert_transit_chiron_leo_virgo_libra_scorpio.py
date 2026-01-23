#!/usr/bin/env python3
"""
Insert transit_chiron interpretations V2 for Leo, Virgo, Libra, Scorpio (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_CHIRON_INTERPRETATIONS = {
    # ============== LEO ==============
    ('leo', 1): """# ⚷ Chiron en Lion – Maison I

**En une phrase :** Un temps pour guérir les blessures liées à ton droit de briller et d'être vu(e).

## L'énergie du moment
Chiron en Lion dans ta maison I active des blessures profondes liées à ton droit d'être au centre, d'être admiré(e) et de t'exprimer pleinement. C'est une guérison de l'identité créative.

## Ce que tu pourrais vivre
- Un sentiment douloureux de ne pas avoir le droit de briller
- Des blessures liées à l'humiliation ou au rejet de ton expression
- Une opportunité de guérir en aidant les autres à assumer leur lumière

## Conseils pour ce transit
- Ta blessure de visibilité peut devenir ton don pour aider les autres à briller
- Tu as le droit d'être vu(e) et admiré(e)
- Guéris en osant prendre la lumière avec authenticité""",

    ('leo', 2): """# ⚷ Chiron en Lion – Maison II

**En une phrase :** Une période pour guérir les blessures liées à la valeur de ta créativité et de ton expression.

## L'énergie du moment
Chiron en Lion dans ta maison des ressources active des blessures autour de la reconnaissance et de la rémunération de tes talents créatifs. C'est une guérison de la valeur de ta lumière.

## Ce que tu pourrais vivre
- Un questionnement sur la valeur de tes dons créatifs
- Des blessures liées à la non-reconnaissance de tes talents
- Une opportunité de guérir en valorisant la créativité des autres

## Conseils pour ce transit
- Ta blessure de non-reconnaissance peut devenir ton don pour valoriser les talents des autres
- Ta créativité a de la valeur réelle
- Guéris en assumant le prix de ton éclat""",

    ('leo', 3): """# ⚷ Chiron en Lion – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à l'expression créative et à la parole authentique.

## L'énergie du moment
Chiron en Lion dans ta maison de la communication active des blessures liées à ta capacité de t'exprimer avec cœur et créativité. C'est une guérison de la voix créative.

## Ce que tu pourrais vivre
- Une peur de parler de toi ou de tes créations
- Des blessures liées à des moqueries sur ton expression
- Une opportunité de guérir en encourageant l'expression authentique des autres

## Conseils pour ce transit
- Ta blessure d'expression peut devenir ton don pour libérer la voix créative des autres
- Ta façon unique de t'exprimer est un cadeau
- Guéris en communiquant depuis le cœur""",

    ('leo', 4): """# ⚷ Chiron en Lion – Maison IV

**En une phrase :** Une période pour guérir les blessures liées au droit de briller dans ta famille.

## L'énergie du moment
Chiron en Lion dans ta maison des racines active des blessures liées à ta place de « star » dans la famille, au droit d'être vu(e) et célébré(e) par tes proches. C'est une guérison de l'enfant intérieur créatif.

## Ce que tu pourrais vivre
- Des souvenirs d'avoir été éteint(e) ou rabaissé(e) en famille
- Un questionnement sur ton droit à briller au foyer
- Une opportunité de guérir en créant un foyer qui célèbre chacun

## Conseils pour ce transit
- Ta blessure familiale peut devenir ton don pour créer des foyers où chacun peut briller
- Tu avais le droit d'être célébré(e) enfant, tu peux l'être maintenant
- Guéris en étant le parent qui applaudit ton enfant intérieur""",

    ('leo', 5): """# ⚷ Chiron en Lion – Maison V

**En une phrase :** Un temps pour guérir les blessures les plus profondes liées à la créativité, l'amour et la joie.

## L'énergie du moment
Chiron en Lion est dans sa maison naturelle, activant intensément les blessures liées à ton droit de créer, d'aimer passionnément et d'être heureux(se). C'est la guérison du cœur créatif.

## Ce que tu pourrais vivre
- Des blocages créatifs profonds qui remontent à l'enfance
- Des blessures dans les histoires d'amour liées au rejet
- Une opportunité de guérir en libérant la joie créative des autres

## Conseils pour ce transit
- Ta blessure créative peut devenir ton don pour inspirer les autres à créer
- Tu as le droit absolu d'être heureux(se) et de briller
- Guéris en créant et en aimant malgré la peur""",

    ('leo', 6): """# ⚷ Chiron en Lion – Maison VI

**En une phrase :** Une période pour guérir les blessures liées à la créativité au travail et au droit de briller dans le quotidien.

## L'énergie du moment
Chiron en Lion dans ta maison du travail active des blessures autour de ta capacité à exprimer ta créativité au quotidien et à être reconnu(e) dans ton travail. C'est une guérison du travail joyeux.

## Ce que tu pourrais vivre
- Un travail qui étouffe ta créativité et ta joie
- Des blessures liées au manque de reconnaissance quotidienne
- Une opportunité de guérir en apportant de la créativité au travail des autres

## Conseils pour ce transit
- Ta blessure de reconnaissance au travail peut devenir ton don pour valoriser le travail des autres
- Même le quotidien peut être une expression créative
- Guéris en mettant du cœur dans chaque tâche""",

    ('leo', 7): """# ⚷ Chiron en Lion – Maison VII

**En une phrase :** Un temps pour guérir les blessures liées au droit d'être admiré(e) dans les relations.

## L'énergie du moment
Chiron en Lion dans ta maison des partenariats active des blessures liées au besoin d'admiration dans les relations, au rejet de ta lumière par les partenaires. C'est une guérison de l'amour admiratif.

## Ce que tu pourrais vivre
- Des relations où tu n'étais pas assez admiré(e) ou célébré(e)
- Un questionnement sur le droit d'être le centre de l'attention en couple
- Une opportunité de guérir en célébrant véritablement les autres

## Conseils pour ce transit
- Ta blessure d'admiration peut devenir ton don pour véritablement voir et célébrer les autres
- Tu mérites un(e) partenaire qui admire ta lumière
- Guéris en apprenant à recevoir l'admiration sans gêne""",

    ('leo', 8): """# ⚷ Chiron en Lion – Maison VIII

**En une phrase :** Une période pour guérir les blessures liées à l'ego, la mort créative et la transformation du cœur.

## L'énergie du moment
Chiron en Lion dans ta maison des profondeurs active des blessures liées à l'humiliation profonde, la mort de l'ego créatif et la capacité de renaître après l'effondrement. C'est une guérison de l'ego blessé.

## Ce que tu pourrais vivre
- Des humiliations profondes qui ont blessé ton ego
- Un questionnement sur ce qui reste quand l'ego s'effondre
- Une opportunité de guérir en aidant les autres à traverser les morts de l'ego

## Conseils pour ce transit
- Ta blessure d'ego peut devenir ton don pour accompagner les transformations profondes
- Ton essence est au-delà de l'ego blessé
- Guéris en découvrant la lumière qui reste après l'effondrement""",

    ('leo', 9): """# ⚷ Chiron en Lion – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées à ta légitimité d'enseigner et d'inspirer.

## L'énergie du moment
Chiron en Lion dans ta maison de l'expansion active des blessures autour de ta légitimité à enseigner, inspirer et partager ta vision. C'est une guérison du maître intérieur.

## Ce que tu pourrais vivre
- Un syndrome de l'imposteur concernant l'enseignement ou l'inspiration
- Des blessures liées à des professeurs qui ont éteint ta lumière
- Une opportunité de guérir en devenant un enseignant qui inspire avec le cœur

## Conseils pour ce transit
- Ta blessure d'enseignant peut devenir ton don d'inspiration authentique
- Tu as le droit de partager ta lumière et ta vision
- Guéris en enseignant depuis le cœur, pas l'ego""",

    ('leo', 10): """# ⚷ Chiron en Lion – Maison X

**En une phrase :** Une période pour guérir les blessures liées à ta place de star et à la reconnaissance publique.

## L'énergie du moment
Chiron en Lion dans ta maison de la carrière active des blessures profondes liées à ton besoin de reconnaissance publique, ton droit de briller professionnellement et ta vocation créative. C'est une guérison de la célébrité intérieure.

## Ce que tu pourrais vivre
- Un sentiment de ne jamais être assez reconnu(e) professionnellement
- Des blessures liées à l'humiliation publique
- Une opportunité de guérir en aidant les autres à rayonner publiquement

## Conseils pour ce transit
- Ta blessure de reconnaissance peut devenir ton don pour faire briller les autres
- Tu mérites ta place sur la scène du monde
- Guéris en brillant pour inspirer, pas pour combler un manque""",

    ('leo', 11): """# ⚷ Chiron en Lion – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées à ta place unique dans les groupes.

## L'énergie du moment
Chiron en Lion dans ta maison des amitiés active des blessures autour de ton droit d'être spécial(e) dans les groupes, de ta place unique parmi les autres. C'est une guérison de l'individualité sociale.

## Ce que tu pourrais vivre
- Un sentiment de n'être qu'un parmi d'autres dans les groupes
- Des blessures liées au rejet de ta différence par les pairs
- Une opportunité de guérir en célébrant l'unicité de chacun dans les collectifs

## Conseils pour ce transit
- Ta blessure d'unicité peut devenir ton don pour valoriser la singularité de chacun
- Tu es irremplaçable dans les groupes qui te correspondent
- Guéris en brillant parmi les autres sans les éclipser""",

    ('leo', 12): """# ⚷ Chiron en Lion – Maison XII

**En une phrase :** Une période pour guérir les blessures karmiques liées à l'ego et à la lumière cachée.

## L'énergie du moment
Chiron en Lion dans ta maison de l'invisible active des blessures karmiques liées à la lumière réprimée, à l'ego blessé dans des vies passées et à la créativité sacrifiée. C'est une guérison de l'âme créative.

## Ce que tu pourrais vivre
- Un sentiment que ta lumière doit rester cachée
- Des blessures de vies passées liées à l'humiliation ou au sacrifice de soi
- Une opportunité de guérir en reconnectant au soleil intérieur

## Conseils pour ce transit
- Ta blessure de lumière cachée peut devenir ton don pour révéler la lumière secrète des autres
- Ton essence est pure lumière, au-delà des blessures de l'ego
- Guéris en laissant briller ta lumière intérieure dans le silence""",

    # ============== VIRGO ==============
    ('virgo', 1): """# ⚷ Chiron en Vierge – Maison I

**En une phrase :** Un temps pour guérir les blessures liées à l'imperfection, au corps et au sentiment de n'être jamais assez.

## L'énergie du moment
Chiron en Vierge dans ta maison I active des blessures profondes liées à ton corps, ta santé et le sentiment de n'être jamais assez bien. C'est une guérison de l'identité imparfaite.

## Ce que tu pourrais vivre
- Un sentiment douloureux de ne jamais être à la hauteur
- Des blessures liées à ton corps ou ta santé
- Une opportunité de guérir en aidant les autres à accepter leur imperfection

## Conseils pour ce transit
- Ta blessure de perfectionnisme peut devenir ton don pour aider les autres à s'accepter
- Tu es suffisant(e) tel(le) que tu es
- Guéris en accueillant l'imperfection comme humanité""",

    ('virgo', 2): """# ⚷ Chiron en Vierge – Maison II

**En une phrase :** Une période pour guérir les blessures liées à la valeur de ton travail et au service sous-payé.

## L'énergie du moment
Chiron en Vierge dans ta maison des ressources active des blessures autour de la valeur de ton travail, de ton utilité et de ta tendance à te sous-évaluer. C'est une guérison de la valeur du service.

## Ce que tu pourrais vivre
- Un travail mal rémunéré malgré tes compétences
- Un questionnement sur la valeur de ce que tu fais
- Une opportunité de guérir en aidant les autres à se valoriser

## Conseils pour ce transit
- Ta blessure de sous-évaluation peut devenir ton don pour aider les autres à reconnaître leur valeur
- Ton travail minutieux a de la valeur réelle
- Guéris en demandant ce que tu mérites vraiment""",

    ('virgo', 3): """# ⚷ Chiron en Vierge – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à l'intelligence pratique et à la communication perfectionniste.

## L'énergie du moment
Chiron en Vierge dans ta maison de la communication active des blessures liées à ta façon de penser et de communiquer, à la critique de ton intelligence ou de tes méthodes. C'est une guérison de l'esprit analytique.

## Ce que tu pourrais vivre
- Une peur d'être critiqué(e) pour tes idées ou ta communication
- Des blessures liées à l'apprentissage ou aux erreurs d'enfance
- Une opportunité de guérir en enseignant la valeur de l'erreur

## Conseils pour ce transit
- Ta blessure d'imperfection intellectuelle peut devenir ton don pour enseigner avec bienveillance
- L'erreur est le chemin vers la maîtrise
- Guéris en accueillant les imperfections de ta pensée""",

    ('virgo', 4): """# ⚷ Chiron en Vierge – Maison IV

**En une phrase :** Une période pour guérir les blessures liées au foyer critique et à la famille perfectionniste.

## L'énergie du moment
Chiron en Vierge dans ta maison des racines active des blessures liées à un foyer où rien n'était jamais assez bien, à la critique familiale et au perfectionnisme hérité. C'est une guérison de l'enfant critiqué.

## Ce que tu pourrais vivre
- Des souvenirs d'un foyer où tu étais toujours critiqué(e)
- Un questionnement sur ce qu'est un foyer « assez bon »
- Une opportunité de guérir en créant un foyer accueillant de l'imperfection

## Conseils pour ce transit
- Ta blessure de critique familiale peut devenir ton don pour créer des foyers bienveillants
- Le foyer parfait n'existe pas, le foyer aimant si
- Guéris en acceptant ton enfant intérieur tel qu'il était""",

    ('virgo', 5): """# ⚷ Chiron en Vierge – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à la créativité perfectionniste et à la peur du jugement.

## L'énergie du moment
Chiron en Vierge dans ta maison de la joie active des blessures liées à la peur que ta créativité ne soit pas assez bien, au perfectionnisme qui tue la joie. C'est une guérison du jeu imparfait.

## Ce que tu pourrais vivre
- Des blocages créatifs par peur de l'imperfection
- Des blessures dans l'amour liées à la critique ou à l'auto-critique
- Une opportunité de guérir en célébrant la créativité imparfaite des autres

## Conseils pour ce transit
- Ta blessure de perfectionnisme créatif peut devenir ton don pour libérer les autres de la peur de créer
- La joie est dans le processus, pas dans la perfection du résultat
- Guéris en créant « mal » et en t'amusant quand même""",

    ('virgo', 6): """# ⚷ Chiron en Vierge – Maison VI

**En une phrase :** Une période pour guérir les blessures profondes liées au travail, au corps et au perfectionnisme quotidien.

## L'énergie du moment
Chiron en Vierge est dans sa maison naturelle, activant intensément les blessures liées au travail, à la santé et au service. C'est la guérison du corps et du travail par excellence.

## Ce que tu pourrais vivre
- Des problèmes de santé liés au stress du perfectionnisme
- Un travail épuisant où rien n'est jamais assez
- Une opportunité de guérir en prenant soin des corps et des routines des autres

## Conseils pour ce transit
- Ta blessure de santé ou de travail peut devenir ton plus grand don de guérisseur
- Le corps imparfait est un temple sacré
- Guéris en acceptant les limites humaines""",

    ('virgo', 7): """# ⚷ Chiron en Vierge – Maison VII

**En une phrase :** Un temps pour guérir les blessures liées à la critique dans les relations et au partenaire jamais assez parfait.

## L'énergie du moment
Chiron en Vierge dans ta maison des partenariats active des blessures liées à la critique mutuelle, au perfectionnisme relationnel et à l'impossibilité de trouver le partenaire parfait. C'est une guérison de l'amour imparfait.

## Ce que tu pourrais vivre
- Des relations marquées par la critique réciproque
- Un questionnement sur ce qui constitue un « bon » partenaire
- Une opportunité de guérir en acceptant l'imperfection de l'autre et de soi

## Conseils pour ce transit
- Ta blessure de critique relationnelle peut devenir ton don pour aider les couples à s'accepter
- L'amour parfait n'existe pas, l'amour vrai accepte
- Guéris en aimant l'imperfection""",

    ('virgo', 8): """# ⚷ Chiron en Vierge – Maison VIII

**En une phrase :** Une période pour guérir les blessures liées au contrôle dans les crises et à l'impuissance face au chaos.

## L'énergie du moment
Chiron en Vierge dans ta maison des profondeurs active des blessures liées à l'impossibilité de tout contrôler, à l'impuissance face au chaos de la vie et de la mort. C'est une guérison du lâcher-prise.

## Ce que tu pourrais vivre
- Une anxiété face à ce qui ne peut être contrôlé ou prévu
- Des blessures liées à des crises où l'ordre a été détruit
- Une opportunité de guérir en acceptant le chaos comme transformation

## Conseils pour ce transit
- Ta blessure de contrôle peut devenir ton don pour accompagner les autres dans le chaos
- Le désordre est parfois le chemin vers un nouvel ordre
- Guéris en acceptant ce qui échappe à ton contrôle""",

    ('virgo', 9): """# ⚷ Chiron en Vierge – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées aux croyances perfectionnistes et à la foi insuffisante.

## L'énergie du moment
Chiron en Vierge dans ta maison de l'expansion active des blessures autour du perfectionnisme spirituel, de la foi jamais assez pure et de la quête de sens trop exigeante. C'est une guérison de la foi humble.

## Ce que tu pourrais vivre
- Un sentiment de ne jamais être assez spirituel ou sage
- Des blessures liées à des enseignements trop stricts ou critiques
- Une opportunité de guérir en enseignant une spiritualité de l'imperfection

## Conseils pour ce transit
- Ta blessure spirituelle peut devenir ton don pour enseigner la sagesse de l'humilité
- La foi parfaite n'existe pas, le chemin imparfait est le vrai chemin
- Guéris en acceptant ton humanité sur le chemin spirituel""",

    ('virgo', 10): """# ⚷ Chiron en Vierge – Maison X

**En une phrase :** Une période pour guérir les blessures liées à la perfection professionnelle et à la peur de l'erreur publique.

## L'énergie du moment
Chiron en Vierge dans ta maison de la carrière active des blessures profondes liées au perfectionnisme professionnel, à la peur de l'erreur visible et au syndrome de l'imposteur. C'est une guérison de la carrière humaine.

## Ce que tu pourrais vivre
- Une peur paralysante de faire des erreurs professionnellement
- Des blessures liées à des critiques publiques de ton travail
- Une opportunité de guérir en aidant les autres à accepter leurs erreurs professionnelles

## Conseils pour ce transit
- Ta blessure professionnelle peut devenir ton don pour humaniser le monde du travail
- L'erreur professionnelle est un droit humain
- Guéris en montrant ta vulnérabilité dans ta carrière""",

    ('virgo', 11): """# ⚷ Chiron en Vierge – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées à l'utilité dans les groupes et au service des causes.

## L'énergie du moment
Chiron en Vierge dans ta maison des amitiés active des blessures autour de ta valeur dans les collectifs, du service aux causes et du sentiment de n'être utile que si tu travailles dur. C'est une guérison du service social.

## Ce que tu pourrais vivre
- Un sentiment de devoir être utile pour appartenir
- Des blessures liées à des groupes qui t'ont exploité(e)
- Une opportunité de guérir en créant des collectifs de service mutuel

## Conseils pour ce transit
- Ta blessure de service peut devenir ton don pour créer des groupes où chacun sert et est servi
- Tu appartiens même quand tu ne travailles pas
- Guéris en acceptant de recevoir autant que tu donnes""",

    ('virgo', 12): """# ⚷ Chiron en Vierge – Maison XII

**En une phrase :** Une période pour guérir les blessures karmiques de perfectionnisme et de critique spirituelle.

## L'énergie du moment
Chiron en Vierge dans ta maison de l'invisible active des blessures karmiques liées au perfectionnisme spirituel, à l'auto-flagellation et à la difficulté d'accepter la grâce. C'est une guérison de l'âme critique.

## Ce que tu pourrais vivre
- Une voix intérieure de critique impitoyable
- Des blessures de vies passées liées à la punition ou à l'auto-mortification
- Une opportunité de guérir en acceptant la grâce sans la mériter

## Conseils pour ce transit
- Ta blessure de perfectionnisme spirituel peut devenir ton don pour aider les autres à accepter la grâce
- Tu n'as pas à être parfait(e) pour être aimé(e) par le divin
- Guéris en recevant l'amour inconditionnel sans le mériter""",

    # ============== LIBRA ==============
    ('libra', 1): """# ⚷ Chiron en Balance – Maison I

**En une phrase :** Un temps pour guérir les blessures liées à ta capacité d'être toi-même en relation.

## L'énergie du moment
Chiron en Balance dans ta maison I active des blessures profondes liées à ton identité relationnelle, ton besoin d'approbation et ta difficulté à exister seul(e). C'est une guérison de l'identité autonome.

## Ce que tu pourrais vivre
- Un sentiment de ne pas exister vraiment sans l'autre
- Des blessures liées au rejet ou à l'abandon qui ont défini ton identité
- Une opportunité de guérir en aidant les autres à trouver leur identité propre

## Conseils pour ce transit
- Ta blessure relationnelle peut devenir ton don pour aider les autres à être eux-mêmes en relation
- Tu existes pleinement même seul(e)
- Guéris en apprenant à t'aimer toi-même d'abord""",

    ('libra', 2): """# ⚷ Chiron en Balance – Maison II

**En une phrase :** Une période pour guérir les blessures liées à la dépendance financière et à la valeur par l'autre.

## L'énergie du moment
Chiron en Balance dans ta maison des ressources active des blessures autour de ta valeur définie par les relations, la dépendance matérielle aux partenaires et le partage déséquilibré. C'est une guérison de la valeur autonome.

## Ce que tu pourrais vivre
- Une difficulté à te sentir précieux(se) sans validation externe
- Des blessures liées à des situations financières déséquilibrées dans les relations
- Une opportunité de guérir en aidant les autres à trouver leur valeur indépendante

## Conseils pour ce transit
- Ta blessure de valeur relationnelle peut devenir ton don pour aider les autres à s'autonomiser
- Ta valeur ne dépend pas du regard de l'autre
- Guéris en construisant ta propre sécurité""",

    ('libra', 3): """# ⚷ Chiron en Balance – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à la communication diplomatique et à la peur du conflit.

## L'énergie du moment
Chiron en Balance dans ta maison de la communication active des blessures liées à ta difficulté à dire non, à exprimer ton désaccord et à ta peur du conflit verbal. C'est une guérison de la parole authentique.

## Ce que tu pourrais vivre
- Une difficulté à exprimer tes vrais sentiments par peur de blesser
- Des blessures liées à des conflits ou à l'évitement des conflits
- Une opportunité de guérir en facilitant la communication harmonieuse entre les autres

## Conseils pour ce transit
- Ta blessure de communication peut devenir ton don de médiation
- Dire ta vérité peut être fait avec amour
- Guéris en apprenant le conflit sain""",

    ('libra', 4): """# ⚷ Chiron en Balance – Maison IV

**En une phrase :** Une période pour guérir les blessures liées à l'harmonie familiale forcée et aux besoins sacrifiés.

## L'énergie du moment
Chiron en Balance dans ta maison des racines active des blessures liées à une famille où tu devais maintenir la paix à tout prix, sacrifiant tes propres besoins. C'est une guérison de l'enfant pacificateur.

## Ce que tu pourrais vivre
- Des souvenirs d'avoir été le médiateur ou le pacificateur familial
- Un questionnement sur ce qu'est une vraie harmonie de foyer
- Une opportunité de guérir en créant un foyer où chacun peut être authentique

## Conseils pour ce transit
- Ta blessure de pacificateur peut devenir ton don pour créer de vraies harmonies familiales
- L'harmonie vraie ne sacrifie personne
- Guéris en permettant à ton enfant intérieur d'avoir des besoins""",

    ('libra', 5): """# ⚷ Chiron en Balance – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à l'amour et à la créativité qui cherchent l'approbation.

## L'énergie du moment
Chiron en Balance dans ta maison de la joie active des blessures liées à la créativité qui cherche à plaire et aux amours qui demandent la validation. C'est une guérison de la joie autonome.

## Ce que tu pourrais vivre
- Une créativité bloquée par la peur de ne pas plaire
- Des amours où tu te perds pour faire plaisir
- Une opportunité de guérir en encourageant la créativité authentique des autres

## Conseils pour ce transit
- Ta blessure de créativité dépendante peut devenir ton don pour libérer l'expression authentique des autres
- Ta joie ne dépend pas de l'approbation extérieure
- Guéris en créant pour toi-même d'abord""",

    ('libra', 6): """# ⚷ Chiron en Balance – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au travail de relation et au service qui s'oublie.

## L'énergie du moment
Chiron en Balance dans ta maison du quotidien active des blessures autour du travail sur les relations, du service qui s'oublie et de l'harmonie au prix de ta santé. C'est une guérison de l'équilibre sain.

## Ce que tu pourrais vivre
- Un travail qui déséquilibre ta vie ou te sacrifie pour l'harmonie
- Des routines qui servent les autres au détriment de toi
- Une opportunité de guérir en créant un équilibre travail-vie authentique

## Conseils pour ce transit
- Ta blessure de déséquilibre peut devenir ton don pour aider les autres à trouver l'équilibre
- Ton bien-être compte autant que celui des autres
- Guéris en mettant tes propres besoins dans l'équation""",

    ('libra', 7): """# ⚷ Chiron en Balance – Maison VII

**En une phrase :** Un temps pour guérir les blessures les plus profondes liées aux relations et à l'équilibre du donner-recevoir.

## L'énergie du moment
Chiron en Balance est dans sa maison naturelle, activant intensément les blessures liées aux relations, aux partenariats et à l'équité. C'est la guérison relationnelle par excellence.

## Ce que tu pourrais vivre
- Des schémas relationnels douloureux qui se répètent
- Un questionnement profond sur ce qu'est une relation équilibrée
- Une opportunité de guérir en aidant les autres dans leurs relations

## Conseils pour ce transit
- Ta blessure relationnelle peut devenir ton plus grand don de conseil ou de thérapie de couple
- Les relations équilibrées sont possibles
- Guéris en créant de nouvelles façons d'être en relation""",

    ('libra', 8): """# ⚷ Chiron en Balance – Maison VIII

**En une phrase :** Une période pour guérir les blessures liées au pouvoir dans les relations et au partage inéquitable.

## L'énergie du moment
Chiron en Balance dans ta maison des profondeurs active des blessures liées aux déséquilibres de pouvoir dans l'intimité, au partage inéquitable des ressources et aux relations qui prennent plus qu'elles ne donnent.

## Ce que tu pourrais vivre
- Des relations intimes où tu as donné plus que tu n'as reçu
- Un questionnement sur l'équité dans le partage profond
- Une opportunité de guérir en rééquilibrant les dynamiques de pouvoir

## Conseils pour ce transit
- Ta blessure de déséquilibre intime peut devenir ton don pour équilibrer les dynamiques de pouvoir
- L'intimité vraie est un échange équitable
- Guéris en apprenant à recevoir autant que tu donnes""",

    ('libra', 9): """# ⚷ Chiron en Balance – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées à la justice, à l'équité et aux croyances relationnelles.

## L'énergie du moment
Chiron en Balance dans ta maison de l'expansion active des blessures autour de la justice, de l'équité universelle et des croyances sur les relations. C'est une guérison de la vision juste.

## Ce que tu pourrais vivre
- Un questionnement douloureux sur l'injustice du monde
- Des blessures liées à des croyances relationnelles transmises
- Une opportunité de guérir en enseignant une vision équilibrée du monde

## Conseils pour ce transit
- Ta blessure de justice peut devenir ton don pour promouvoir l'équité
- L'équilibre est possible même dans un monde déséquilibré
- Guéris en développant une philosophie de la relation saine""",

    ('libra', 10): """# ⚷ Chiron en Balance – Maison X

**En une phrase :** Une période pour guérir les blessures liées aux partenariats professionnels et à l'image publique relationnelle.

## L'énergie du moment
Chiron en Balance dans ta maison de la carrière active des blessures liées aux partenariats professionnels, à la collaboration et à l'équité dans la reconnaissance. C'est une guérison de la carrière partagée.

## Ce que tu pourrais vivre
- Des partenariats professionnels déséquilibrés ou douloureux
- Un questionnement sur ta place dans les collaborations
- Une opportunité de guérir en créant des partenariats professionnels équitables

## Conseils pour ce transit
- Ta blessure de partenariat professionnel peut devenir ton don pour créer des collaborations saines
- Tu mérites une reconnaissance équitable
- Guéris en apprenant à négocier ta juste place""",

    ('libra', 11): """# ⚷ Chiron en Balance – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées à ta place dans les groupes et à l'harmonie sociale.

## L'énergie du moment
Chiron en Balance dans ta maison des amitiés active des blessures autour de ta place dans les collectifs, de l'harmonie de groupe et des amitiés équilibrées. C'est une guérison sociale.

## Ce que tu pourrais vivre
- Un sentiment de devoir maintenir l'harmonie dans les groupes à ton détriment
- Des amitiés déséquilibrées qui te laissent épuisé(e)
- Une opportunité de guérir en créant des groupes véritablement équilibrés

## Conseils pour ce transit
- Ta blessure sociale peut devenir ton don pour créer des communautés harmonieuses
- L'harmonie de groupe ne devrait pas sacrifier les individus
- Guéris en choisissant des cercles qui te respectent""",

    ('libra', 12): """# ⚷ Chiron en Balance – Maison XII

**En une phrase :** Une période pour guérir les blessures karmiques liées à l'amour perdu et aux relations sacrificielles.

## L'énergie du moment
Chiron en Balance dans ta maison de l'invisible active des blessures karmiques liées aux relations sacrificielles, à l'amour perdu et aux partenariats de vies passées. C'est une guérison de l'âme relationnelle.

## Ce que tu pourrais vivre
- Des sentiments inexpliqués de perte ou de sacrifice relationnel
- Des liens karmiques qui demandent à être guéris ou libérés
- Une opportunité de guérir les relations d'autres vies

## Conseils pour ce transit
- Ta blessure relationnelle karmique peut devenir ton don pour aider les autres à guérir leurs liens d'âme
- L'amour divin est toujours équilibré
- Guéris en te réconciliant avec l'amour inconditionnel universel""",

    # ============== SCORPIO ==============
    ('scorpio', 1): """# ⚷ Chiron en Scorpion – Maison I

**En une phrase :** Un temps pour guérir les blessures liées à l'intensité, au pouvoir et à la survie.

## L'énergie du moment
Chiron en Scorpion dans ta maison I active des blessures profondes liées à ton intensité, ta puissance et ta capacité à survivre aux pires épreuves. C'est une guérison de l'identité du survivant.

## Ce que tu pourrais vivre
- Un sentiment que ton intensité effraie les autres
- Des blessures liées à des trahisons ou abus qui ont formé ton identité
- Une opportunité de guérir en aidant d'autres survivants

## Conseils pour ce transit
- Ta blessure de survie peut devenir ton don pour accompagner ceux qui traversent l'enfer
- Ton intensité est un super-pouvoir, pas un défaut
- Guéris en acceptant pleinement ta puissance""",

    ('scorpio', 2): """# ⚷ Chiron en Scorpion – Maison II

**En une phrase :** Une période pour guérir les blessures liées au pouvoir financier, à la perte et au partage des ressources.

## L'énergie du moment
Chiron en Scorpion dans ta maison des ressources active des blessures autour du pouvoir lié à l'argent, aux pertes matérielles traumatisantes et au partage douloureux des ressources.

## Ce que tu pourrais vivre
- Des blessures liées à des pertes financières ou à des héritages conflictuels
- Un questionnement sur le pouvoir que confère ou retire l'argent
- Une opportunité de guérir en aidant les autres à traverser les pertes matérielles

## Conseils pour ce transit
- Ta blessure de perte peut devenir ton don pour accompagner les autres dans les deuils matériels
- Ta valeur est au-delà de ce que tu possèdes ou perds
- Guéris en trouvant le pouvoir intérieur que rien ne peut prendre""",

    ('scorpio', 3): """# ⚷ Chiron en Scorpion – Maison III

**En une phrase :** Un temps pour guérir les blessures liées aux secrets, aux paroles empoisonnées et à la vérité cachée.

## L'énergie du moment
Chiron en Scorpion dans ta maison de la communication active des blessures liées aux secrets familiaux, aux paroles qui ont blessé profondément et à la vérité qu'on ne pouvait pas dire.

## Ce que tu pourrais vivre
- Des secrets qui demandent à être révélés ou gardés
- Des blessures liées à des mensonges ou des trahisons verbales
- Une opportunité de guérir en utilisant la parole pour transformer

## Conseils pour ce transit
- Ta blessure de secret peut devenir ton don pour libérer les autres de leurs non-dits
- La vérité guérit même quand elle fait mal d'abord
- Guéris en apprenant le pouvoir des mots vrais""",

    ('scorpio', 4): """# ⚷ Chiron en Scorpion – Maison IV

**En une phrase :** Une période pour guérir les blessures les plus sombres de l'enfance et de la famille.

## L'énergie du moment
Chiron en Scorpion dans ta maison des racines active les blessures familiales les plus profondes et sombres – abus, trahisons, secrets de famille, mort prématurée. C'est une guérison des fondations brisées.

## Ce que tu pourrais vivre
- Des traumatismes familiaux qui refont surface pour être guéris
- Un questionnement sur les secrets et tabous de ta lignée
- Une opportunité de guérir en brisant les cycles familiaux destructeurs

## Conseils pour ce transit
- Ta blessure familiale profonde peut devenir ton don pour aider les familles en crise
- Tu peux survivre et même prospérer après les pires fondations
- Guéris en transformant le poison familial en médecine""",

    ('scorpio', 5): """# ⚷ Chiron en Scorpion – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à la passion, à la créativité intense et aux amours qui consument.

## L'énergie du moment
Chiron en Scorpion dans ta maison de la joie active des blessures liées à la passion créative, aux amours obsessionnelles et à la difficulté de trouver la joie sans intensité destructrice.

## Ce que tu pourrais vivre
- Des amours qui ont brûlé plutôt que nourri
- Une créativité bloquée par des expériences traumatisantes
- Une opportunité de guérir en canalisant l'intensité créative positivement

## Conseils pour ce transit
- Ta blessure de passion peut devenir ton don pour transformer l'intensité en art
- L'amour intense peut être sain
- Guéris en apprenant la passion qui nourrit plutôt que consume""",

    ('scorpio', 6): """# ⚷ Chiron en Scorpion – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au travail sur l'ombre et à la santé comme transformation.

## L'énergie du moment
Chiron en Scorpion dans ta maison du quotidien active des blessures autour du travail avec les zones d'ombre, des maladies comme transformations et du service aux mourants ou souffrants.

## Ce que tu pourrais vivre
- Des problèmes de santé qui sont des appels à la transformation profonde
- Un travail qui te confronte à la mort, la crise ou le trauma
- Une opportunité de guérir en devenant un accompagnant des grandes transitions

## Conseils pour ce transit
- Ta blessure de santé peut devenir ton don de guérisseur des profondeurs
- La maladie peut être une initiation
- Guéris en servant ceux qui traversent les transitions les plus sombres""",

    ('scorpio', 7): """# ⚷ Chiron en Scorpion – Maison VII

**En une phrase :** Un temps pour guérir les blessures liées à la trahison, aux relations de pouvoir et à l'intimité dangereuse.

## L'énergie du moment
Chiron en Scorpion dans ta maison des partenariats active des blessures profondes liées à la trahison, aux abus dans les relations et aux dynamiques de pouvoir destructrices.

## Ce que tu pourrais vivre
- Des relations qui ont impliqué trahison ou abus
- Un questionnement sur la possibilité de faire confiance à nouveau
- Une opportunité de guérir en aidant les autres à sortir des relations toxiques

## Conseils pour ce transit
- Ta blessure de trahison peut devenir ton don pour aider les victimes de relations abusives
- La confiance peut être reconstruite
- Guéris en apprenant à reconnaître et créer des relations saines""",

    ('scorpio', 8): """# ⚷ Chiron en Scorpion – Maison VIII

**En une phrase :** Une période pour guérir les blessures les plus profondes liées à la mort, au pouvoir et à la transformation.

## L'énergie du moment
Chiron en Scorpion est dans sa maison naturelle, activant les blessures les plus intenses liées à la mort, aux abus de pouvoir, aux transformations traumatisantes et à l'intimité blessée. C'est la guérison ultime des profondeurs.

## Ce que tu pourrais vivre
- Des expériences de mort (littérale ou symbolique) qui remontent
- Un travail profond sur les traumas et les abus
- Une opportunité de devenir un guérisseur des plus grandes blessures

## Conseils pour ce transit
- Ta blessure des profondeurs peut devenir ton plus grand don de transformation
- Tu peux survivre à tout et renaître plus fort(e)
- Guéris en plongeant au fond pour remonter la lumière""",

    ('scorpio', 9): """# ⚷ Chiron en Scorpion – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées aux croyances sombres et à la foi brisée.

## L'énergie du moment
Chiron en Scorpion dans ta maison de l'expansion active des blessures autour de la foi détruite, des croyances sur le mal et la souffrance, et de la quête de sens dans le noir.

## Ce que tu pourrais vivre
- Un questionnement douloureux sur le mal et la souffrance dans le monde
- Des blessures liées à des enseignements spirituels toxiques ou abusifs
- Une opportunité de guérir en trouvant le sens dans les ténèbres

## Conseils pour ce transit
- Ta blessure de foi peut devenir ton don pour guider les autres dans la nuit de l'âme
- Le sens existe même dans les plus grandes souffrances
- Guéris en développant une spiritualité qui inclut les ténèbres""",

    ('scorpio', 10): """# ⚷ Chiron en Scorpion – Maison X

**En une phrase :** Une période pour guérir les blessures liées au pouvoir public et à la carrière de l'ombre.

## L'énergie du moment
Chiron en Scorpion dans ta maison de la carrière active des blessures liées au pouvoir dans le monde, aux trahisons professionnelles et au travail avec les zones sombres de la société.

## Ce que tu pourrais vivre
- Des trahisons ou des luttes de pouvoir dans ta carrière
- Un questionnement sur comment utiliser ton pouvoir dans le monde
- Une opportunité de guérir en aidant les autres à transformer leur rapport au pouvoir

## Conseils pour ce transit
- Ta blessure de pouvoir peut devenir ton don pour aider les autres à utiliser leur pouvoir sainement
- Le pouvoir peut servir la transformation positive
- Guéris en assumant ton pouvoir avec intégrité""",

    ('scorpio', 11): """# ⚷ Chiron en Scorpion – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées à la trahison des groupes et aux causes sombres.

## L'énergie du moment
Chiron en Scorpion dans ta maison des amitiés active des blessures autour des trahisons de groupe, des amitiés qui ont blessé profondément et des causes qui ont mal tourné.

## Ce que tu pourrais vivre
- Des trahisons dans les cercles d'amis ou les groupes
- Un questionnement sur la possibilité de faire partie d'un collectif sans être trahi
- Une opportunité de guérir en créant des groupes de transformation authentique

## Conseils pour ce transit
- Ta blessure de groupe peut devenir ton don pour créer des cercles de guérison profonde
- Des tribus authentiques et loyales existent
- Guéris en osant à nouveau appartenir à un groupe""",

    ('scorpio', 12): """# ⚷ Chiron en Scorpion – Maison XII

**En une phrase :** Une période pour guérir les blessures karmiques les plus profondes de l'âme.

## L'énergie du moment
Chiron en Scorpion dans ta maison de l'invisible active les blessures les plus anciennes et profondes de l'âme, les traumatismes de vies passées et les liens karmiques les plus sombres. C'est la guérison ultime.

## Ce que tu pourrais vivre
- Des douleurs inexplicables venant d'autres vies
- Un travail profond sur les traumas karmiques
- Une opportunité de devenir un guérisseur de l'âme

## Conseils pour ce transit
- Ta blessure karmique peut devenir ton don ultime de guérison des âmes
- Tu portes la médecine de tes plus grandes souffrances
- Guéris en te souvenant de ta vraie nature lumineuse au-delà de toutes les blessures""",
}


async def insert_interpretations():
    """Insert Chiron transit interpretations for Leo, Virgo, Libra, Scorpio"""
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
        print(f"✅ Transit Chiron (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
