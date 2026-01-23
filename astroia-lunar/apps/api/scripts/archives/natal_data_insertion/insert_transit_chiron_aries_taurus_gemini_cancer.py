#!/usr/bin/env python3
"""
Insert transit_chiron interpretations V2 for Aries, Taurus, Gemini, Cancer (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_CHIRON_INTERPRETATIONS = {
    # ============== ARIES ==============
    ('aries', 1): """# ⚷ Chiron en Bélier – Maison I

**En une phrase :** Une opportunité de guérir tes blessures d'identité et d'existence légitime.

## L'énergie du moment
Chiron en Bélier dans ta maison I active tes blessures les plus profondes liées à ton droit d'exister, d'être toi-même et de t'affirmer. C'est un temps de guérison de l'identité.

## Ce que tu pourrais vivre
- Des situations qui ravivent la blessure « je n'ai pas le droit d'être moi »
- Un questionnement profond sur qui tu es vraiment
- Une opportunité de guérir en aidant d'autres à s'affirmer

## Conseils pour ce transit
- Ta blessure d'exister est ta plus grande force de guérisseur
- Affirme-toi même quand ça fait mal
- En t'acceptant pleinement, tu montres le chemin aux autres""",

    ('aries', 2): """# ⚷ Chiron en Bélier – Maison II

**En une phrase :** Une période pour guérir tes blessures liées à la valeur personnelle et à l'autonomie financière.

## L'énergie du moment
Chiron en Bélier dans ta maison des ressources active des blessures anciennes autour de ta valeur et de ta capacité à te suffire. C'est le moment de guérir ton rapport à l'argent et à l'estime de soi.

## Ce que tu pourrais vivre
- Des doutes sur ta capacité à subvenir à tes propres besoins
- Des situations qui questionnent ta valeur intrinsèque
- Une opportunité de guérir en aidant d'autres à reconnaître leur valeur

## Conseils pour ce transit
- Ta blessure de valeur peut devenir ta capacité à valoriser les autres
- L'autonomie financière est un chemin de guérison
- Tu mérites d'exister et de prospérer""",

    ('aries', 3): """# ⚷ Chiron en Bélier – Maison III

**En une phrase :** Un temps pour guérir tes blessures d'expression et de communication.

## L'énergie du moment
Chiron en Bélier dans ta maison de la communication active des blessures liées à ta capacité à t'exprimer et à être entendu(e). C'est une période pour guérir ta voix intérieure.

## Ce que tu pourrais vivre
- Des situations où tu te sens non entendu(e) ou incompris(e)
- Des blessures anciennes liées à l'expression ou l'apprentissage
- Une opportunité de guérir en donnant la parole aux autres

## Conseils pour ce transit
- Ta difficulté à t'exprimer peut devenir ton don pour aider les autres à parler
- Ta voix mérite d'être entendue
- Guéris en osant dire ce qui est difficile à dire""",

    ('aries', 4): """# ⚷ Chiron en Bélier – Maison IV

**En une phrase :** Une période pour guérir les blessures familiales et le sentiment de ne pas avoir sa place.

## L'énergie du moment
Chiron en Bélier dans ta maison des racines active des blessures profondes liées à ta famille et à ton sentiment d'appartenance. C'est le moment de guérir ton enfant intérieur.

## Ce que tu pourrais vivre
- Des souvenirs douloureux de l'enfance qui remontent
- Un questionnement sur ta place dans ta famille
- Une opportunité de créer le foyer que tu n'as pas eu

## Conseils pour ce transit
- Ta blessure familiale peut devenir ton don pour créer des espaces sûrs
- Tu peux te donner ce que tu n'as pas reçu
- Guéris ton enfant intérieur en l'écoutant avec amour""",

    ('aries', 5): """# ⚷ Chiron en Bélier – Maison V

**En une phrase :** Un temps pour guérir tes blessures créatives et ta peur de briller.

## L'énergie du moment
Chiron en Bélier dans ta maison de la joie active des blessures liées à ta créativité, ton droit au plaisir et à l'amour. C'est une période pour guérir ton élan créatif blessé.

## Ce que tu pourrais vivre
- Des blocages créatifs qui révèlent des blessures anciennes
- Des schémas douloureux dans les relations amoureuses
- Une opportunité de guérir en encourageant la créativité des autres

## Conseils pour ce transit
- Ta blessure créative peut devenir ton don pour inspirer les autres
- Tu as le droit de briller et d'être heureux(se)
- Guéris en créant malgré la peur""",

    ('aries', 6): """# ⚷ Chiron en Bélier – Maison VI

**En une phrase :** Une période pour guérir tes blessures liées au travail et au corps.

## L'énergie du moment
Chiron en Bélier dans ta maison du quotidien active des blessures autour du service, du travail et de la santé. C'est le moment de guérir ton rapport au corps et à l'utilité.

## Ce que tu pourrais vivre
- Des problèmes de santé qui sont des messages de l'âme
- Un questionnement sur ton utilité et ta place au travail
- Une opportunité de guérir en prenant soin des autres

## Conseils pour ce transit
- Ta blessure de santé ou de travail peut devenir ton don de guérisseur
- Écoute les messages de ton corps
- Guéris en servant avec amour""",

    ('aries', 7): """# ⚷ Chiron en Bélier – Maison VII

**En une phrase :** Un temps pour guérir tes blessures relationnelles et ta peur du rejet.

## L'énergie du moment
Chiron en Bélier dans ta maison des partenariats active des blessures profondes liées aux relations, au rejet et à la capacité d'être en couple tout en restant soi-même.

## Ce que tu pourrais vivre
- Des relations qui réveillent des blessures anciennes
- Un questionnement sur ta capacité à être aimé(e) tel(le) que tu es
- Une opportunité de guérir en aidant les autres dans leurs relations

## Conseils pour ce transit
- Ta blessure relationnelle peut devenir ton don de conseil ou de médiation
- Tu mérites d'être aimé(e) sans te perdre
- Guéris en apprenant à être pleinement toi en relation""",

    ('aries', 8): """# ⚷ Chiron en Bélier – Maison VIII

**En une phrase :** Une période pour guérir les blessures de pouvoir, d'intimité et de transformation.

## L'énergie du moment
Chiron en Bélier dans ta maison des profondeurs active des blessures liées au pouvoir, à la sexualité, à la mort et aux ressources partagées. C'est une guérison des profondeurs.

## Ce que tu pourrais vivre
- Des crises qui révèlent des blessures de pouvoir ou d'abus
- Un questionnement profond sur l'intimité et le partage
- Une opportunité de guérir en accompagnant d'autres dans leurs transformations

## Conseils pour ce transit
- Ta blessure de pouvoir peut devenir ton don d'accompagnement dans les crises
- La vulnérabilité dans l'intimité est une force
- Guéris en transmutant tes plus grandes douleurs""",

    ('aries', 9): """# ⚷ Chiron en Bélier – Maison IX

**En une phrase :** Un temps pour guérir tes blessures de sens, de foi et de légitimité spirituelle.

## L'énergie du moment
Chiron en Bélier dans ta maison de l'expansion active des blessures liées à ta quête de sens, tes croyances et ta légitimité à avoir une vision. C'est une guérison philosophique.

## Ce que tu pourrais vivre
- Un questionnement douloureux sur le sens de ta vie
- Des blessures liées à l'éducation ou aux croyances imposées
- Une opportunité de guérir en partageant ta sagesse durement acquise

## Conseils pour ce transit
- Ta blessure de sens peut devenir ton don d'enseignement authentique
- Tu as le droit d'avoir ta propre vision du monde
- Guéris en trouvant ton propre chemin spirituel""",

    ('aries', 10): """# ⚷ Chiron en Bélier – Maison X

**En une phrase :** Une période pour guérir les blessures de reconnaissance et de place dans le monde.

## L'énergie du moment
Chiron en Bélier dans ta maison de la carrière active des blessures profondes liées à ta place dans le monde, ta légitimité professionnelle et la reconnaissance. C'est une guérison de vocation.

## Ce que tu pourrais vivre
- Un questionnement douloureux sur ta mission de vie
- Des situations qui ravivent le sentiment de ne pas mériter le succès
- Une opportunité de guérir en aidant les autres à trouver leur voie

## Conseils pour ce transit
- Ta blessure de reconnaissance peut devenir ton don pour valoriser les autres
- Tu mérites ta place au soleil
- Guéris en assumant ta vocation de guérisseur public""",

    ('aries', 11): """# ⚷ Chiron en Bélier – Maison XI

**En une phrase :** Un temps pour guérir les blessures d'appartenance et de différence.

## L'énergie du moment
Chiron en Bélier dans ta maison des amitiés active des blessures liées à l'appartenance aux groupes, au sentiment d'être différent et aux idéaux déçus. C'est une guérison sociale.

## Ce que tu pourrais vivre
- Un sentiment douloureux de ne pas appartenir
- Des amitiés qui réveillent des blessures de rejet
- Une opportunité de guérir en créant des espaces d'accueil pour les différents

## Conseils pour ce transit
- Ta blessure de différence peut devenir ton don pour inclure les exclus
- Tu appartiens, même quand tu te sens à part
- Guéris en accueillant ceux qui se sentent seuls""",

    ('aries', 12): """# ⚷ Chiron en Bélier – Maison XII

**En une phrase :** Une période pour guérir les blessures les plus profondes et invisibles de l'âme.

## L'énergie du moment
Chiron en Bélier dans ta maison de l'invisible active les blessures karmiques les plus anciennes, les douleurs cachées et les sacrifices passés. C'est une guérison spirituelle profonde.

## Ce que tu pourrais vivre
- Des douleurs inexpliquées qui viennent de très loin
- Un contact avec des blessures de vies passées
- Une opportunité de guérir en servant silencieusement

## Conseils pour ce transit
- Tes blessures invisibles sont tes dons de guérison les plus puissants
- La guérison se fait aussi dans le silence et la solitude
- Guéris en te connectant à la source de toute guérison""",

    # ============== TAURUS ==============
    ('taurus', 1): """# ⚷ Chiron en Taureau – Maison I

**En une phrase :** Un temps pour guérir les blessures liées au corps, à la valeur et à l'incarnation.

## L'énergie du moment
Chiron en Taureau dans ta maison I active des blessures profondes liées à ton corps physique, ta valeur intrinsèque et ton droit à occuper l'espace. C'est une guérison de l'incarnation.

## Ce que tu pourrais vivre
- Un rapport difficile au corps qui demande attention
- Des questionnements sur ta valeur fondamentale
- Une opportunité de guérir en aidant les autres à s'incarner pleinement

## Conseils pour ce transit
- Ta blessure corporelle peut devenir ton don pour aider les autres à habiter leur corps
- Tu as le droit d'exister concrètement et de prendre de la place
- Guéris en honorant ton corps comme un temple""",

    ('taurus', 2): """# ⚷ Chiron en Taureau – Maison II

**En une phrase :** Une période pour guérir les blessures de manque, de perte et d'insécurité matérielle.

## L'énergie du moment
Chiron en Taureau est dans sa maison naturelle, activant profondément les blessures liées à l'argent, aux possessions et à la sécurité. C'est le moment de guérir ta relation à l'abondance.

## Ce que tu pourrais vivre
- Des peurs de manque qui remontent à la surface
- Un questionnement profond sur ce qui a vraiment de la valeur
- Une opportunité de guérir en aidant les autres à trouver leur sécurité intérieure

## Conseils pour ce transit
- Ta blessure de manque peut devenir ton don pour générer l'abondance vraie
- La vraie sécurité est intérieure
- Guéris en apprenant que tu es suffisant(e) tel(le) que tu es""",

    ('taurus', 3): """# ⚷ Chiron en Taureau – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à l'apprentissage lent et à la communication simple.

## L'énergie du moment
Chiron en Taureau dans ta maison de la communication active des blessures liées au rythme d'apprentissage, à la simplicité d'expression ou à la voix physique. C'est une guérison de la parole.

## Ce que tu pourrais vivre
- Des difficultés d'élocution ou de communication qui refont surface
- Un sentiment de ne pas être assez rapide ou brillant intellectuellement
- Une opportunité de guérir en valorisant la communication simple et vraie

## Conseils pour ce transit
- Ta blessure d'expression peut devenir ton don pour communiquer l'essentiel
- La lenteur est une forme de sagesse
- Guéris en parlant de ce qui compte vraiment""",

    ('taurus', 4): """# ⚷ Chiron en Taureau – Maison IV

**En une phrase :** Une période pour guérir les blessures de sécurité, de foyer et d'enracinement.

## L'énergie du moment
Chiron en Taureau dans ta maison des racines active des blessures profondes liées à la sécurité du foyer, aux besoins de base non comblés et à l'ancrage. C'est une guérison des fondations.

## Ce que tu pourrais vivre
- Des souvenirs de manque ou d'insécurité dans l'enfance
- Un questionnement sur ce qui constitue un vrai chez-soi
- Une opportunité de guérir en créant des espaces de sécurité pour les autres

## Conseils pour ce transit
- Ta blessure de sécurité peut devenir ton don pour créer des havres de paix
- Tu peux construire le foyer stable que tu n'as pas eu
- Guéris en t'enracinant profondément""",

    ('taurus', 5): """# ⚷ Chiron en Taureau – Maison V

**En une phrase :** Un temps pour guérir les blessures liées au plaisir, au corps et à la sensualité créative.

## L'énergie du moment
Chiron en Taureau dans ta maison de la joie active des blessures liées au plaisir physique, à la sensualité et à la créativité concrète. C'est une guérison du rapport au plaisir.

## Ce que tu pourrais vivre
- Une difficulté à profiter des plaisirs simples
- Des blessures liées au corps dans l'intimité amoureuse
- Une opportunité de guérir en créant de la beauté tangible

## Conseils pour ce transit
- Ta blessure de plaisir peut devenir ton don pour aider les autres à s'incarner dans la joie
- Le plaisir sain est un droit, pas un luxe
- Guéris en créant et en savourant sans culpabilité""",

    ('taurus', 6): """# ⚷ Chiron en Taureau – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au corps au travail et aux routines de santé.

## L'énergie du moment
Chiron en Taureau dans ta maison du quotidien active des blessures autour du corps physique dans le travail, de la santé et des routines. C'est une guérison du rapport au corps utile.

## Ce que tu pourrais vivre
- Des problèmes de santé liés à la stabilité ou à la nutrition
- Un questionnement sur la valeur de ton travail quotidien
- Une opportunité de guérir en prenant soin du corps des autres

## Conseils pour ce transit
- Ta blessure de santé peut devenir ton don de guérisseur du corps
- Le travail peut nourrir plutôt qu'épuiser
- Guéris en honorant les besoins simples de ton corps""",

    ('taurus', 7): """# ⚷ Chiron en Taureau – Maison VII

**En une phrase :** Un temps pour guérir les blessures de stabilité et de sécurité dans les relations.

## L'énergie du moment
Chiron en Taureau dans ta maison des partenariats active des blessures liées à la stabilité relationnelle, à la possessivité ou à la peur de perdre l'autre. C'est une guérison du lien sécure.

## Ce que tu pourrais vivre
- Des peurs d'abandon ou de perte dans les relations
- Un questionnement sur ce qui constitue une vraie sécurité à deux
- Une opportunité de guérir en offrant une présence stable aux autres

## Conseils pour ce transit
- Ta blessure de sécurité relationnelle peut devenir ton don de présence fidèle
- L'amour vrai n'est pas possessif mais stable
- Guéris en apprenant que l'attachement sain existe""",

    ('taurus', 8): """# ⚷ Chiron en Taureau – Maison VIII

**En une phrase :** Une période pour guérir les blessures de perte matérielle et de lâcher-prise.

## L'énergie du moment
Chiron en Taureau dans ta maison des profondeurs active des blessures liées aux pertes matérielles, à l'attachement et à la difficulté de lâcher. C'est une guérison de la relation à l'impermanence.

## Ce que tu pourrais vivre
- Des pertes matérielles qui activent des blessures profondes
- Un questionnement sur l'attachement aux possessions
- Une opportunité de guérir en aidant les autres à traverser les pertes

## Conseils pour ce transit
- Ta blessure de perte peut devenir ton don pour accompagner les deuils
- Lâcher n'est pas perdre, c'est transformer
- Guéris en apprenant que ta valeur est au-delà de ce que tu possèdes""",

    ('taurus', 9): """# ⚷ Chiron en Taureau – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées aux croyances matérialistes et à la foi concrète.

## L'énergie du moment
Chiron en Taureau dans ta maison de l'expansion active des blessures autour de la foi, de la philosophie trop terre-à-terre ou du manque de sens transcendant. C'est une guérison de la vision.

## Ce que tu pourrais vivre
- Un questionnement sur le sens de l'existence matérielle
- Des blessures liées à un matérialisme qui ne comble pas
- Une opportunité de guérir en enseignant une sagesse incarnée

## Conseils pour ce transit
- Ta blessure philosophique peut devenir ton don pour enseigner une spiritualité pratique
- Le sacré est aussi dans la matière
- Guéris en trouvant le sens dans le concret""",

    ('taurus', 10): """# ⚷ Chiron en Taureau – Maison X

**En une phrase :** Une période pour guérir les blessures de valeur professionnelle et de réussite matérielle.

## L'énergie du moment
Chiron en Taureau dans ta maison de la carrière active des blessures liées à ta valeur professionnelle, au succès matériel et à la stabilité de carrière. C'est une guérison de la vocation concrète.

## Ce que tu pourrais vivre
- Un questionnement douloureux sur ta valeur sur le marché du travail
- Des blessures liées à l'insécurité professionnelle
- Une opportunité de guérir en aidant les autres à construire leur carrière

## Conseils pour ce transit
- Ta blessure de valeur professionnelle peut devenir ton don de coaching
- Ta carrière peut être stable ET significative
- Guéris en assumant ta valeur dans le monde""",

    ('taurus', 11): """# ⚷ Chiron en Taureau – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées aux ressources partagées et aux valeurs collectives.

## L'énergie du moment
Chiron en Taureau dans ta maison des amitiés active des blessures autour du partage des ressources, des valeurs de groupe et de la sécurité dans les collectifs. C'est une guérison sociale.

## Ce que tu pourrais vivre
- Des conflits de valeurs dans les groupes
- Un sentiment de ne pas avoir sa place dans les communautés stables
- Une opportunité de guérir en créant des groupes qui valorisent chacun

## Conseils pour ce transit
- Ta blessure de valeur sociale peut devenir ton don pour créer des communautés prospères
- Tu appartiens à des groupes qui partagent tes vraies valeurs
- Guéris en contribuant concrètement aux collectifs""",

    ('taurus', 12): """# ⚷ Chiron en Taureau – Maison XII

**En une phrase :** Une période pour guérir les blessures profondes d'incarnation et d'attachement au monde.

## L'énergie du moment
Chiron en Taureau dans ta maison de l'invisible active des blessures karmiques liées au corps, à la matière et à la difficulté d'être pleinement incarné(e). C'est une guérison de l'âme dans la chair.

## Ce que tu pourrais vivre
- Un sentiment de ne pas vouloir être dans ce corps ou ce monde
- Des blessures anciennes liées à la survie physique
- Une opportunité de guérir en aidant les âmes à s'incarner

## Conseils pour ce transit
- Ta blessure d'incarnation peut devenir ton don pour réconcilier l'esprit et la matière
- Être dans un corps est un privilège, pas une punition
- Guéris en acceptant pleinement ta présence sur Terre""",

    # ============== GEMINI ==============
    ('gemini', 1): """# ⚷ Chiron en Gémeaux – Maison I

**En une phrase :** Un temps pour guérir les blessures liées à l'intelligence, à la parole et à la dualité intérieure.

## L'énergie du moment
Chiron en Gémeaux dans ta maison I active des blessures profondes liées à ton intelligence, ta capacité à penser et à t'exprimer. C'est une guérison de l'identité mentale.

## Ce que tu pourrais vivre
- Un sentiment douloureux de ne pas être assez intelligent(e)
- Des blessures liées à la façon dont tu penses ou parles
- Une opportunité de guérir en aidant les autres à développer leur mental

## Conseils pour ce transit
- Ta blessure d'intelligence peut devenir ton don pour valoriser tous les types d'intelligences
- Ta façon de penser est unique et valable
- Guéris en acceptant la richesse de ton mental""",

    ('gemini', 2): """# ⚷ Chiron en Gémeaux – Maison II

**En une phrase :** Une période pour guérir les blessures liées aux compétences intellectuelles comme source de valeur.

## L'énergie du moment
Chiron en Gémeaux dans ta maison des ressources active des blessures autour de la valeur de tes idées et de tes compétences mentales. C'est une guérison de la valeur intellectuelle.

## Ce que tu pourrais vivre
- Un questionnement sur la valeur marchande de tes idées
- Des blessures liées à l'utilisation de tes compétences de communication
- Une opportunité de guérir en aidant les autres à valoriser leurs talents mentaux

## Conseils pour ce transit
- Ta blessure de valeur intellectuelle peut devenir ton don pour aider les autres à monétiser leurs idées
- Tes idées ont de la valeur concrète
- Guéris en reconnaissant la richesse de ton mental""",

    ('gemini', 3): """# ⚷ Chiron en Gémeaux – Maison III

**En une phrase :** Un temps pour guérir les blessures profondes de communication et d'apprentissage.

## L'énergie du moment
Chiron en Gémeaux est dans sa maison naturelle, activant intensément les blessures liées à la parole, l'écoute, l'apprentissage et les relations fraternelles. C'est une guérison fondamentale de la communication.

## Ce que tu pourrais vivre
- Des blessures d'enfance liées à l'école ou aux frères et sœurs
- Des difficultés de communication qui remontent à la surface
- Une opportunité de guérir en devenant un pont de communication pour les autres

## Conseils pour ce transit
- Ta blessure de communication peut devenir ton don de traducteur ou de médiateur
- Apprendre autrement est encore apprendre
- Guéris en trouvant ta propre façon de communiquer""",

    ('gemini', 4): """# ⚷ Chiron en Gémeaux – Maison IV

**En une phrase :** Une période pour guérir les blessures de communication familiale et les non-dits.

## L'énergie du moment
Chiron en Gémeaux dans ta maison des racines active des blessures liées à la communication au sein de la famille, aux secrets et aux malentendus familiaux. C'est une guérison des mots dans la famille.

## Ce que tu pourrais vivre
- Des non-dits familiaux qui refont surface
- Un questionnement sur ce qui n'a jamais été dit dans ton enfance
- Une opportunité de guérir en brisant le silence familial

## Conseils pour ce transit
- Ta blessure de communication familiale peut devenir ton don pour libérer la parole dans les familles
- Ce qui n'est pas dit peut être dit maintenant
- Guéris en apportant les mots qui manquaient""",

    ('gemini', 5): """# ⚷ Chiron en Gémeaux – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à l'expression créative et au jeu intellectuel.

## L'énergie du moment
Chiron en Gémeaux dans ta maison de la joie active des blessures liées à l'expression créative verbale, au jeu d'esprit et à la légèreté amoureuse. C'est une guérison du plaisir mental.

## Ce que tu pourrais vivre
- Des blocages d'écriture ou d'expression créative
- Des blessures dans les flirts et la communication amoureuse
- Une opportunité de guérir en encourageant l'expression créative des autres

## Conseils pour ce transit
- Ta blessure d'expression peut devenir ton don pour libérer la créativité verbale des autres
- Le jeu mental est une forme de joie légitime
- Guéris en osant écrire, parler et jouer avec les mots""",

    ('gemini', 6): """# ⚷ Chiron en Gémeaux – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au travail mental et à l'anxiété quotidienne.

## L'énergie du moment
Chiron en Gémeaux dans ta maison du quotidien active des blessures autour du travail intellectuel, de la communication au travail et de l'anxiété mentale. C'est une guérison du mental au quotidien.

## Ce que tu pourrais vivre
- De l'anxiété ou des ruminations qui affectent ta santé
- Des difficultés de communication au travail
- Une opportunité de guérir en aidant les autres à calmer leur mental

## Conseils pour ce transit
- Ta blessure mentale peut devenir ton don pour apaiser l'anxiété des autres
- Le mental peut être un outil, pas un maître
- Guéris en apprenant à calmer les pensées""",

    ('gemini', 7): """# ⚷ Chiron en Gémeaux – Maison VII

**En une phrase :** Un temps pour guérir les blessures de communication et de compréhension dans les relations.

## L'énergie du moment
Chiron en Gémeaux dans ta maison des partenariats active des blessures liées à la communication dans les relations, aux malentendus et à la connexion intellectuelle. C'est une guérison du dialogue à deux.

## Ce que tu pourrais vivre
- Des malentendus récurrents dans les relations
- Un sentiment de ne pas être compris(e) par tes partenaires
- Une opportunité de guérir en facilitant la communication dans les couples

## Conseils pour ce transit
- Ta blessure de communication relationnelle peut devenir ton don de conseiller de couple
- Être vraiment compris(e) est possible
- Guéris en apprenant à dire et à écouter vraiment""",

    ('gemini', 8): """# ⚷ Chiron en Gémeaux – Maison VIII

**En une phrase :** Une période pour guérir les blessures liées aux paroles blessantes et aux vérités cachées.

## L'énergie du moment
Chiron en Gémeaux dans ta maison des profondeurs active des blessures liées aux mots qui ont fait mal, aux secrets révélés cruellement et à la communication dans l'intimité. C'est une guérison des mots profonds.

## Ce que tu pourrais vivre
- Des souvenirs de paroles qui ont profondément blessé
- Un questionnement sur ce qui peut ou ne peut pas être dit
- Une opportunité de guérir en utilisant les mots pour transformer

## Conseils pour ce transit
- Ta blessure des mots peut devenir ton don pour utiliser la parole de façon thérapeutique
- Les mots peuvent guérir autant qu'ils blessent
- Guéris en apprenant le pouvoir transformateur de la communication""",

    ('gemini', 9): """# ⚷ Chiron en Gémeaux – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées à la pensée et à la légitimité intellectuelle.

## L'énergie du moment
Chiron en Gémeaux dans ta maison de l'expansion active des blessures autour de ta légitimité à penser, à enseigner et à avoir des idées. C'est une guérison de l'autorité intellectuelle.

## Ce que tu pourrais vivre
- Un syndrome de l'imposteur intellectuel
- Des blessures liées à l'éducation ou aux professeurs
- Une opportunité de guérir en partageant ta pensée unique

## Conseils pour ce transit
- Ta blessure de légitimité intellectuelle peut devenir ton don pour valoriser toutes les pensées
- Tu as le droit de penser et de partager tes idées
- Guéris en assumant ton rôle de passeur d'idées""",

    ('gemini', 10): """# ⚷ Chiron en Gémeaux – Maison X

**En une phrase :** Une période pour guérir les blessures liées à la communication professionnelle et à la voix publique.

## L'énergie du moment
Chiron en Gémeaux dans ta maison de la carrière active des blessures liées à ta voix professionnelle, à ta légitimité de communicant et à ta réputation intellectuelle. C'est une guérison de la parole publique.

## Ce que tu pourrais vivre
- Une peur de parler publiquement qui bloque ta carrière
- Un questionnement sur ta légitimité à communiquer professionnellement
- Une opportunité de guérir en devenant un communicant authentique

## Conseils pour ce transit
- Ta blessure de voix publique peut devenir ton don de porte-parole
- Ta façon unique de communiquer est ta marque
- Guéris en assumant ta voix professionnelle""",

    ('gemini', 11): """# ⚷ Chiron en Gémeaux – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées à la place dans les réseaux et les échanges de groupe.

## L'énergie du moment
Chiron en Gémeaux dans ta maison des amitiés active des blessures autour de la communication dans les groupes, du partage d'idées et de la connexion intellectuelle avec les pairs. C'est une guérison sociale.

## Ce que tu pourrais vivre
- Un sentiment de ne pas être sur la même longueur d'onde que les autres
- Des blessures liées aux échanges dans les groupes
- Une opportunité de guérir en créant des espaces d'échange bienveillants

## Conseils pour ce transit
- Ta blessure de connexion intellectuelle peut devenir ton don pour créer des communautés d'échange
- Tu as ta place dans les cercles qui te correspondent
- Guéris en facilitant les échanges entre esprits différents""",

    ('gemini', 12): """# ⚷ Chiron en Gémeaux – Maison XII

**En une phrase :** Une période pour guérir les blessures profondes du mental et de la parole intérieure.

## L'énergie du moment
Chiron en Gémeaux dans ta maison de l'invisible active des blessures karmiques liées au mental, à la pensée et à la communication avec l'invisible. C'est une guérison du dialogue avec l'âme.

## Ce que tu pourrais vivre
- Des pensées intrusives ou douloureuses de sources profondes
- Un questionnement sur la voix intérieure vraie
- Une opportunité de guérir en canalisant des messages pour les autres

## Conseils pour ce transit
- Ta blessure mentale profonde peut devenir ton don de médium ou de canal
- Le silence intérieur est accessible
- Guéris en distinguant la voix de l'ego de celle de l'âme""",

    # ============== CANCER ==============
    ('cancer', 1): """# ⚷ Chiron en Cancer – Maison I

**En une phrase :** Un temps pour guérir les blessures de sensibilité, de vulnérabilité et d'identité émotionnelle.

## L'énergie du moment
Chiron en Cancer dans ta maison I active des blessures profondes liées à ta sensibilité, ta nature émotionnelle et ton droit d'avoir des besoins. C'est une guérison de l'identité sensible.

## Ce que tu pourrais vivre
- Un sentiment douloureux d'être trop sensible pour ce monde
- Des blessures liées au fait de montrer ta vulnérabilité
- Une opportunité de guérir en aidant les autres à accueillir leur sensibilité

## Conseils pour ce transit
- Ta blessure de sensibilité peut devenir ton don d'empathie profonde
- Ta vulnérabilité est une force, pas une faiblesse
- Guéris en acceptant ta nature profondément émotionnelle""",

    ('cancer', 2): """# ⚷ Chiron en Cancer – Maison II

**En une phrase :** Une période pour guérir les blessures liées à la nourriture émotionnelle et à la sécurité intérieure.

## L'énergie du moment
Chiron en Cancer dans ta maison des ressources active des blessures autour de la nourriture (au sens large), de la sécurité émotionnelle et des besoins de base. C'est une guérison du rapport à la nourriture de l'âme.

## Ce que tu pourrais vivre
- Des problèmes avec la nourriture ou l'argent liés aux émotions
- Un questionnement sur ce qui te nourrit vraiment
- Une opportunité de guérir en nourrissant les autres

## Conseils pour ce transit
- Ta blessure de manque peut devenir ton don pour nourrir ceux qui ont faim (d'amour)
- Tu mérites d'être nourri(e) à tous les niveaux
- Guéris en apprenant à te nourrir toi-même émotionnellement""",

    ('cancer', 3): """# ⚷ Chiron en Cancer – Maison III

**En une phrase :** Un temps pour guérir les blessures liées à l'expression émotionnelle et à la communication du cœur.

## L'énergie du moment
Chiron en Cancer dans ta maison de la communication active des blessures liées à l'expression de tes émotions, à la communication avec la famille proche et à l'écoute empathique. C'est une guérison de la parole du cœur.

## Ce que tu pourrais vivre
- Une difficulté à exprimer ce que tu ressens vraiment
- Des blessures liées à l'écoute (ou au manque d'écoute) dans l'enfance
- Une opportunité de guérir en écoutant vraiment les autres avec ton cœur

## Conseils pour ce transit
- Ta blessure d'expression émotionnelle peut devenir ton don d'écoute profonde
- Tes émotions méritent d'être entendues
- Guéris en apprenant à parler depuis le cœur""",

    ('cancer', 4): """# ⚷ Chiron en Cancer – Maison IV

**En une phrase :** Une période pour guérir les blessures les plus profondes de l'enfance et de la famille.

## L'énergie du moment
Chiron en Cancer est dans sa maison naturelle, activant les blessures les plus fondamentales liées à la mère, à la famille et à la sécurité émotionnelle. C'est la guérison de l'enfant intérieur par excellence.

## Ce que tu pourrais vivre
- Des souvenirs d'enfance douloureux qui refont surface
- Un questionnement profond sur la relation maternelle
- Une opportunité de guérir en devenant le parent que tu n'as pas eu

## Conseils pour ce transit
- Ta blessure familiale peut devenir ton don pour créer la famille de cœur
- Tu peux te donner ce que tu n'as pas reçu enfant
- Guéris en adoptant ton enfant intérieur avec amour inconditionnel""",

    ('cancer', 5): """# ⚷ Chiron en Cancer – Maison V

**En une phrase :** Un temps pour guérir les blessures liées à la créativité émotionnelle et à l'amour maternel.

## L'énergie du moment
Chiron en Cancer dans ta maison de la joie active des blessures liées à la créativité qui vient du cœur, au rapport aux enfants et à l'amour protecteur. C'est une guérison de la joie maternelle.

## Ce que tu pourrais vivre
- Des blessures autour de la maternité ou du rapport aux enfants
- Une difficulté à créer depuis les émotions
- Une opportunité de guérir en nourrissant la créativité des autres

## Conseils pour ce transit
- Ta blessure de maternité peut devenir ton don pour accueillir tous les enfants intérieurs
- Ta créativité émotionnelle est précieuse
- Guéris en aimant et en créant sans peur""",

    ('cancer', 6): """# ⚷ Chiron en Cancer – Maison VI

**En une phrase :** Une période pour guérir les blessures liées au soin des autres et à l'épuisement émotionnel.

## L'énergie du moment
Chiron en Cancer dans ta maison du quotidien active des blessures autour du soin excessif des autres, de l'oubli de soi et de l'épuisement émotionnel. C'est une guérison du rapport au service.

## Ce que tu pourrais vivre
- Un épuisement à force de prendre soin des autres
- Des problèmes de santé liés aux émotions non exprimées
- Une opportunité de guérir en apprenant à prendre soin de toi aussi

## Conseils pour ce transit
- Ta blessure de sur-don peut devenir ton don pour enseigner le soin de soi
- Tu ne peux pas verser d'une coupe vide
- Guéris en te traitant avec la même douceur que tu offres aux autres""",

    ('cancer', 7): """# ⚷ Chiron en Cancer – Maison VII

**En une phrase :** Un temps pour guérir les blessures liées à la dépendance émotionnelle et au soin dans les relations.

## L'énergie du moment
Chiron en Cancer dans ta maison des partenariats active des blessures liées au besoin d'être protégé(e), à la dépendance émotionnelle et au rôle de parent dans les relations. C'est une guérison du lien émotionnel.

## Ce que tu pourrais vivre
- Des relations où tu donnes trop ou attends trop
- Un questionnement sur la dépendance vs l'interdépendance
- Une opportunité de guérir en créant des relations mutuellement nourrissantes

## Conseils pour ce transit
- Ta blessure de dépendance peut devenir ton don pour créer des liens sains
- Tu peux être nourri(e) ET autonome
- Guéris en apprenant l'attachement sécure""",

    ('cancer', 8): """# ⚷ Chiron en Cancer – Maison VIII

**En une phrase :** Une période pour guérir les blessures profondes de l'âme familiale et des transmissions émotionnelles.

## L'énergie du moment
Chiron en Cancer dans ta maison des profondeurs active des blessures liées aux transmissions familiales, aux héritages émotionnels et aux deuils non faits. C'est une guérison transgénérationnelle.

## Ce que tu pourrais vivre
- Des émotions qui ne t'appartiennent pas mais viennent de tes ancêtres
- Un questionnement profond sur l'héritage émotionnel familial
- Une opportunité de guérir en libérant les deuils familiaux non faits

## Conseils pour ce transit
- Ta blessure transgénérationnelle peut devenir ton don pour libérer les lignées
- Tu peux rompre les cycles de douleur familiale
- Guéris en pleurant les larmes non pleurées de ta lignée""",

    ('cancer', 9): """# ⚷ Chiron en Cancer – Maison IX

**En une phrase :** Un temps pour guérir les blessures liées à la foi, au sentiment d'appartenance cosmique et à la mère spirituelle.

## L'énergie du moment
Chiron en Cancer dans ta maison de l'expansion active des blessures autour de la foi nourricière, du sentiment d'être aimé(e) par l'univers et de la confiance dans la vie. C'est une guérison de la foi maternelle.

## Ce que tu pourrais vivre
- Un questionnement sur l'amour divin et maternel
- Des blessures liées à une spiritualité qui n'a pas nourri
- Une opportunité de guérir en trouvant une foi qui nourrit l'âme

## Conseils pour ce transit
- Ta blessure de foi peut devenir ton don pour aider les autres à se sentir aimés par l'univers
- Tu es enfant de la vie, tu es voulu(e) et aimé(e)
- Guéris en trouvant la Mère cosmique qui t'accueille""",

    ('cancer', 10): """# ⚷ Chiron en Cancer – Maison X

**En une phrase :** Une période pour guérir les blessures liées à la vocation de soin et à la place publique de nourricier.

## L'énergie du moment
Chiron en Cancer dans ta maison de la carrière active des blessures liées à ton rôle de soignant dans le monde, à la reconnaissance de tes dons de soin et à ta mission de nourrir. C'est une guérison de la vocation maternelle.

## Ce que tu pourrais vivre
- Un questionnement sur ta vocation de soin ou de protection
- Des blessures liées à la reconnaissance de ton rôle nourricier
- Une opportunité de guérir en assumant publiquement ta mission de soin

## Conseils pour ce transit
- Ta blessure de soignant peut devenir ta vocation reconnue
- Le monde a besoin de ta capacité à nourrir et protéger
- Guéris en assumant ton rôle de parent du monde""",

    ('cancer', 11): """# ⚷ Chiron en Cancer – Maison XI

**En une phrase :** Un temps pour guérir les blessures liées à la famille choisie et au soin collectif.

## L'énergie du moment
Chiron en Cancer dans ta maison des amitiés active des blessures autour de la création de famille choisie, de la place émotionnelle dans les groupes et du soin mutuel entre amis. C'est une guérison de la famille d'âme.

## Ce que tu pourrais vivre
- Un sentiment de ne pas appartenir à une tribu aimante
- Des blessures liées au rejet émotionnel des groupes
- Une opportunité de guérir en créant des familles choisies

## Conseils pour ce transit
- Ta blessure d'appartenance peut devenir ton don pour créer des tribus aimantes
- Tu mérites une famille d'âme qui te chérit
- Guéris en rassemblant ceux qui cherchent aussi leur tribu""",

    ('cancer', 12): """# ⚷ Chiron en Cancer – Maison XII

**En une phrase :** Une période pour guérir les blessures karmiques les plus profondes de l'âme maternelle.

## L'énergie du moment
Chiron en Cancer dans ta maison de l'invisible active les blessures les plus anciennes liées à la mère, à la séparation de la source et à la solitude émotionnelle cosmique. C'est la guérison ultime de l'enfant abandonné.

## Ce que tu pourrais vivre
- Un sentiment profond de séparation de la source d'amour
- Des blessures de vies passées liées à l'abandon maternel
- Une opportunité de guérir en te reconnectant à l'amour universel inconditionnel

## Conseils pour ce transit
- Ta blessure cosmique peut devenir ton don pour ramener les âmes perdues à l'amour
- Tu n'as jamais été vraiment séparé(e) de l'amour
- Guéris en te souvenant que tu es toujours aimé(e) par le cosmos""",
}


async def insert_interpretations():
    """Insert Chiron transit interpretations for Aries, Taurus, Gemini, Cancer"""
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
        print(f"✅ Transit Chiron (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
