#!/usr/bin/env python3
"""
Insert transit_south_node interpretations V2 for Leo, Virgo, Libra, Scorpio (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SOUTH_NODE_INTERPRETATIONS = {
    # ============== LEO ==============
    ('leo', 1): """# ☋ Nœud Sud en Lion – Maison I

**En une phrase :** Ton ego et ton besoin de briller doivent céder la place à l'esprit de groupe.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison I révèle une identité construite sur le besoin d'attention, de reconnaissance et de différenciation. Ce transit t'invite à découvrir la force du collectif.

## Ce que tu pourrais vivre
- Un besoin de reconnaissance qui te limite
- Une image de « star » qui isole des autres
- Un ego qui demande à être tempéré par l'humilité

## Conseils pour ce transit
- Tu n'as pas besoin d'être le centre pour avoir de la valeur
- L'humilité peut coexister avec la confiance
- Contribue au groupe plutôt que de chercher à y briller""",

    ('leo', 2): """# ☋ Nœud Sud en Lion – Maison II

**En une phrase :** Ton attachement aux possessions qui te distinguent doit évoluer.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison des ressources révèle une tendance à valoriser ce qui brille, ce qui impressionne. Ce transit t'invite à une relation plus simple avec l'argent.

## Ce que tu pourrais vivre
- Des dépenses pour impressionner ou paraître
- Un attachement aux possessions qui flattent l'ego
- Une valeur personnelle trop liée au statut

## Conseils pour ce transit
- Ta valeur ne dépend pas de ce que tu possèdes de prestigieux
- L'abondance vraie est souvent simple et partagée
- Dépense pour l'utile plutôt que pour l'impressionnant""",

    ('leo', 3): """# ☋ Nœud Sud en Lion – Maison III

**En une phrase :** Ta communication dramatique et centrée sur toi doit s'ouvrir au dialogue.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison de la communication révèle une parole qui cherche l'attention et l'applaudissement. Ce transit t'invite à écouter autant que tu parles.

## Ce que tu pourrais vivre
- Des conversations où tu monopolises l'attention
- Une communication théâtrale qui fatigue les autres
- Un besoin de reconnaissance intellectuelle excessif

## Conseils pour ce transit
- L'écoute est aussi importante que la parole
- Tes idées ont de la valeur sans les mettre en scène
- Le dialogue vrai demande de l'espace pour l'autre""",

    ('leo', 4): """# ☋ Nœud Sud en Lion – Maison IV

**En une phrase :** Ton besoin d'être le roi/la reine du foyer doit s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison des racines révèle un besoin d'être le centre de la famille, de briller dans l'intimité. Ce transit t'invite à partager la scène domestique.

## Ce que tu pourrais vivre
- Un foyer où tout tourne autour de toi
- Un besoin de reconnaissance familiale excessif
- Des racines construites sur l'ego plutôt que l'amour

## Conseils pour ce transit
- Le foyer n'est pas ta scène personnelle
- Laisse les autres membres de la famille briller aussi
- Crée un chez-toi qui nourrit tous, pas juste ton ego""",

    ('leo', 5): """# ☋ Nœud Sud en Lion – Maison V

**En une phrase :** Ta créativité égocentrique et tes amours dramatiques doivent mûrir.

## L'énergie du moment
Le Nœud Sud en Lion est dans sa maison naturelle, amplifiant le besoin de briller à travers la créativité et l'amour. Ce transit t'invite à créer et aimer pour partager, pas pour être admiré(e).

## Ce que tu pourrais vivre
- Une créativité qui cherche l'applaudissement plutôt que l'expression
- Des amours théâtrales et centrées sur l'ego
- Un plaisir qui dépend du regard admiratif des autres

## Conseils pour ce transit
- Crée pour le plaisir de créer, pas pour être admiré(e)
- Aime sans exiger d'être le centre de l'univers de l'autre
- La vraie joie ne dépend pas de l'applaudissement""",

    ('leo', 6): """# ☋ Nœud Sud en Lion – Maison VI

**En une phrase :** Ton besoin de briller au travail quotidien doit s'équilibrer avec le service.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison du travail révèle un besoin de reconnaissance même dans les tâches ordinaires. Ce transit t'invite à servir sans chercher la gloire.

## Ce que tu pourrais vivre
- Un travail où tu cherches à te démarquer excessivement
- Des routines qui deviennent des performances
- Une difficulté à faire les choses simples simplement

## Conseils pour ce transit
- Le travail bien fait n'a pas besoin d'applaudissements
- Sers avec humilité sans perdre ta dignité
- L'excellence peut être discrète""",

    ('leo', 7): """# ☋ Nœud Sud en Lion – Maison VII

**En une phrase :** Ton besoin d'être admiré(e) dans les relations doit céder à l'égalité vraie.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison des partenariats révèle un besoin d'être le/la star de tes relations. Ce transit t'invite à des partenariats plus égalitaires.

## Ce que tu pourrais vivre
- Des relations où tu monopolises l'attention
- Un besoin d'être admiré(e) par ton/ta partenaire
- Des difficultés quand l'autre veut aussi briller

## Conseils pour ce transit
- Une relation saine laisse briller les deux partenaires
- Tu n'as pas besoin d'être admiré(e) pour être aimé(e)
- L'égalité est plus épanouissante que l'adoration""",

    ('leo', 8): """# ☋ Nœud Sud en Lion – Maison VIII

**En une phrase :** Ton ego face aux transformations doit se dissoudre.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison des profondeurs révèle une résistance de l'ego face aux crises et aux changements. Ce transit t'invite à laisser mourir ce qui doit mourir, y compris l'orgueil.

## Ce que tu pourrais vivre
- Des crises où l'orgueil amplifie la souffrance
- Une résistance à la vulnérabilité et à l'intimité vraie
- Des luttes de pouvoir pour préserver l'image

## Conseils pour ce transit
- L'ego peut mourir sans que tu disparaisses
- La vraie force se montre dans la vulnérabilité
- Les transformations demandent de l'humilité""",

    ('leo', 9): """# ☋ Nœud Sud en Lion – Maison IX

**En une phrase :** Ta philosophie centrée sur toi doit s'ouvrir à l'universel.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison de l'expansion révèle une quête de sens qui sert l'ego plus que l'âme. Ce transit t'invite à une spiritualité plus humble et universelle.

## Ce que tu pourrais vivre
- Des croyances qui te mettent au centre
- Des voyages qui servent ton image plutôt que ta croissance
- Un enseignement qui cherche l'admiration

## Conseils pour ce transit
- La vraie sagesse est humble
- Voyage pour apprendre, pas pour impressionner
- Ta philosophie peut servir plus grand que toi""",

    ('leo', 10): """# ☋ Nœud Sud en Lion – Maison X

**En une phrase :** Ton besoin de gloire professionnelle doit céder à une contribution plus large.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison de la carrière révèle une ambition qui cherche la célébrité et l'adoration. Ce transit t'invite à une réussite qui sert quelque chose de plus grand.

## Ce que tu pourrais vivre
- Une carrière qui nourrit l'ego plus que l'âme
- Un succès qui isole au sommet
- Un besoin de reconnaissance qui n'est jamais comblé

## Conseils pour ce transit
- La vraie réussite sert plus que ton image
- Le leadership peut être humble et collaboratif
- Ta contribution compte plus que ta gloire""",

    ('leo', 11): """# ☋ Nœud Sud en Lion – Maison XI

**En une phrase :** Ton besoin de briller dans les groupes doit céder à la contribution collective.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison des amitiés révèle une tendance à vouloir être la star des groupes. Ce transit t'invite à contribuer au collectif sans chercher les projecteurs.

## Ce que tu pourrais vivre
- Un rôle de leader qui cherche la gloire personnelle
- Des amitiés où tu attends de l'admiration
- Des causes qui servent ton image plutôt que l'idéal

## Conseils pour ce transit
- Le groupe peut briller sans que tu sois au centre
- L'amitié vraie n'a pas besoin d'admiration
- Tes idéaux dépassent ton ego personnel""",

    ('leo', 12): """# ☋ Nœud Sud en Lion – Maison XII

**En une phrase :** L'ego secret doit se dissoudre dans l'unité spirituelle.

## L'énergie du moment
Le Nœud Sud en Lion dans ta maison de l'invisible révèle un ego caché qui résiste à la dissolution spirituelle. Ce transit t'invite à lâcher les dernières attaches à l'identité séparée.

## Ce que tu pourrais vivre
- Une résistance spirituelle à l'humilité
- Un karma d'orgueil à libérer
- Une difficulté à se fondre dans le tout

## Conseils pour ce transit
- L'âme est au-delà de l'ego qui brille
- La dissolution n'est pas une perte mais une expansion
- Trouve ta vraie lumière au-delà de l'ego""",

    # ============== VIRGO ==============
    ('virgo', 1): """# ☋ Nœud Sud en Vierge – Maison I

**En une phrase :** Ton perfectionnisme et ton auto-critique doivent céder à plus de foi et de fluidité.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison I révèle une identité construite sur la perfection, l'analyse et la critique. Ce transit t'invite à embrasser l'imperfection et le mystère.

## Ce que tu pourrais vivre
- Une auto-critique paralysante qui te limite
- Un besoin de contrôle et de perfection épuisant
- Une image de « personne parfaite » impossible à maintenir

## Conseils pour ce transit
- L'imperfection est humaine et belle
- Lâche le contrôle et fais confiance au flux de la vie
- Tu n'as pas besoin d'être parfait(e) pour avoir de la valeur""",

    ('virgo', 2): """# ☋ Nœud Sud en Vierge – Maison II

**En une phrase :** Ta gestion anxieuse et perfectionniste de l'argent doit s'assouplir.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison des ressources révèle une approche trop analytique et anxieuse des finances. Ce transit t'invite à plus de confiance et de fluidité.

## Ce que tu pourrais vivre
- Une inquiétude excessive pour les détails financiers
- Un rapport à l'argent trop analytique et contrôlant
- Une difficulté à profiter de ce que tu as

## Conseils pour ce transit
- L'abondance vient aussi de la foi, pas seulement du calcul
- Tu peux lâcher le contrôle financier sans tout perdre
- Apprends à recevoir avec gratitude sans tout analyser""",

    ('virgo', 3): """# ☋ Nœud Sud en Vierge – Maison III

**En une phrase :** Ta communication analytique et critique doit s'adoucir.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison de la communication révèle une parole trop critique, analytique ou perfectionniste. Ce transit t'invite à plus de bienveillance et de poésie.

## Ce que tu pourrais vivre
- Des communications qui dissèquent plutôt qu'elles n'inspirent
- Une critique qui blesse même quand elle est juste
- Des apprentissages bloqués par le perfectionnisme

## Conseils pour ce transit
- La parole peut être bienveillante sans être moins vraie
- Apprends avec joie, pas avec anxiété de perfection
- Communique pour inspirer, pas pour corriger""",

    ('virgo', 4): """# ☋ Nœud Sud en Vierge – Maison IV

**En une phrase :** Ton foyer trop ordonné et ton perfectionnisme domestique doivent s'assouplir.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison des racines révèle un besoin excessif d'ordre et de contrôle dans le foyer. Ce transit t'invite à accepter le beau désordre de la vie.

## Ce que tu pourrais vivre
- Un foyer impeccable mais sans chaleur
- Une critique familiale qui blesse les proches
- Un passé analysé à l'excès au lieu d'être guéri

## Conseils pour ce transit
- Le foyer parfait n'existe pas, accepte le vivant
- Ta famille n'a pas besoin de ta critique, mais de ton amour
- Guéris ton passé par la compassion, pas par l'analyse""",

    ('virgo', 5): """# ☋ Nœud Sud en Vierge – Maison V

**En une phrase :** Ta créativité et tes amours perfectionnistes doivent se libérer.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison de la joie révèle une créativité bloquée par le perfectionnisme et des amours trop critiques. Ce transit t'invite au lâcher-prise joyeux.

## Ce que tu pourrais vivre
- Une créativité paralysée par la peur de l'imperfection
- Des amours où la critique remplace la passion
- Un rapport au plaisir trop contrôlé

## Conseils pour ce transit
- Crée librement, l'imperfection est créative
- Aime sans chercher à améliorer l'autre
- La joie vient du lâcher-prise, pas du contrôle""",

    ('virgo', 6): """# ☋ Nœud Sud en Vierge – Maison VI

**En une phrase :** Ton perfectionnisme au travail et ton anxiété pour la santé doivent céder.

## L'énergie du moment
Le Nœud Sud en Vierge est dans sa maison naturelle, amplifiant le perfectionnisme professionnel et l'anxiété sanitaire. Ce transit t'invite à la confiance et au lâcher-prise.

## Ce que tu pourrais vivre
- Un travail où rien n'est jamais assez bien
- Une hypocondrie ou des routines de santé obsessionnelles
- Un épuisement par excès de perfectionnisme quotidien

## Conseils pour ce transit
- Le travail bien fait ne signifie pas parfait
- Ta santé bénéficiera de moins d'anxiété, pas plus de contrôle
- Accepte que certaines choses échappent à ton contrôle""",

    ('virgo', 7): """# ☋ Nœud Sud en Vierge – Maison VII

**En une phrase :** Ta critique dans les relations doit céder à l'acceptation inconditionnelle.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison des partenariats révèle une tendance à critiquer et vouloir améliorer tes partenaires. Ce transit t'invite à l'amour inconditionnel.

## Ce que tu pourrais vivre
- Des relations où la critique remplace l'acceptation
- Un besoin de partenaires « parfaits » qui n'existent pas
- Des associations professionnelles gâchées par le perfectionnisme

## Conseils pour ce transit
- Aime l'autre tel qu'il est, pas tel que tu voudrais qu'il soit
- Le partenaire parfait n'existe pas, l'amour réel si
- Lâche le besoin de critiquer pour améliorer""",

    ('virgo', 8): """# ☋ Nœud Sud en Vierge – Maison VIII

**En une phrase :** Ton besoin de contrôler et d'analyser les profondeurs doit se dissoudre.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison des transformations révèle une tendance à analyser plutôt que vivre les crises. Ce transit t'invite à l'abandon et à la foi.

## Ce que tu pourrais vivre
- Des crises où l'analyse empêche la transformation
- Un contrôle de l'intimité qui bloque la vraie connexion
- Une résistance au mystère de la mort et de la renaissance

## Conseils pour ce transit
- Certaines choses ne se comprennent pas, elles se vivent
- L'intimité vraie demande l'abandon, pas le contrôle
- Fais confiance au processus de transformation""",

    ('virgo', 9): """# ☋ Nœud Sud en Vierge – Maison IX

**En une phrase :** Ta philosophie trop analytique doit s'ouvrir à la foi et au mystère.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison de l'expansion révèle une spiritualité trop mentale et une difficulté à croire sans comprendre. Ce transit t'invite au saut de la foi.

## Ce que tu pourrais vivre
- Des croyances trop terre-à-terre qui limitent
- Des voyages organisés au millimètre qui perdent leur magie
- Un enseignement trop technique qui manque d'inspiration

## Conseils pour ce transit
- La sagesse inclut le mystère et l'incompréhensible
- Voyage avec ouverture à l'imprévu
- Enseigne avec foi, pas seulement avec méthode""",

    ('virgo', 10): """# ☋ Nœud Sud en Vierge – Maison X

**En une phrase :** Ta carrière de perfectionniste doit s'ouvrir à la vision et à l'inspiration.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison de la carrière révèle une réussite basée sur la compétence technique et l'attention aux détails. Ce transit t'invite à une vision plus large.

## Ce que tu pourrais vivre
- Une carrière techniquement parfaite mais sans âme
- Une réputation d'expert qui limite d'autres possibilités
- Un perfectionnisme professionnel qui épuise

## Conseils pour ce transit
- Ta carrière peut avoir une dimension plus inspirante
- L'excellence inclut la vision, pas seulement l'exécution
- Lâche le perfectionnisme pour une contribution plus grande""",

    ('virgo', 11): """# ☋ Nœud Sud en Vierge – Maison XI

**En une phrase :** Ta critique des groupes et des amis doit céder à l'acceptation.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison des amitiés révèle une tendance à critiquer les imperfections des groupes et des amis. Ce transit t'invite à l'acceptation et à la vision.

## Ce que tu pourrais vivre
- Des groupes que tu quittes parce qu'ils ne sont pas parfaits
- Des amitiés gâchées par tes critiques
- Des idéaux si précis qu'ils sont irréalisables

## Conseils pour ce transit
- Les groupes parfaits n'existent pas, contribue au réel
- Tes amis ont besoin de ton soutien, pas de ta critique
- Les grandes visions acceptent l'imperfection du chemin""",

    ('virgo', 12): """# ☋ Nœud Sud en Vierge – Maison XII

**En une phrase :** Ton mental analytique doit se dissoudre dans la conscience unifiée.

## L'énergie du moment
Le Nœud Sud en Vierge dans ta maison de l'invisible révèle un mental qui analyse et critique même dans l'espace spirituel. Ce transit t'invite à la dissolution dans le mystère.

## Ce que tu pourrais vivre
- Une spiritualité trop technique ou analytique
- Un karma de perfectionnisme et de critique à libérer
- Une difficulté à lâcher prise dans la méditation

## Conseils pour ce transit
- Le divin ne s'analyse pas, il se vit
- Ton karma de perfection peut enfin se libérer
- La vraie paix vient quand le mental se tait""",

    # ============== LIBRA ==============
    ('libra', 1): """# ☋ Nœud Sud en Balance – Maison I

**En une phrase :** Ton identité construite sur l'approbation des autres doit céder à l'affirmation de soi.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison I révèle une identité qui dépend trop du regard et de l'approbation des autres. Ce transit t'invite à t'affirmer indépendamment.

## Ce que tu pourrais vivre
- Une difficulté à savoir qui tu es sans le miroir des autres
- Un besoin d'harmonie qui te fait renier tes propres désirs
- Une image de « personne agréable » qui te limite

## Conseils pour ce transit
- Tu existes indépendamment de l'approbation des autres
- L'harmonie vraie inclut le respect de toi-même
- Ose te définir par ce que TU veux vraiment""",

    ('libra', 2): """# ☋ Nœud Sud en Balance – Maison II

**En une phrase :** Ta dépendance financière aux autres doit céder à l'autonomie.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison des ressources révèle une tendance à dépendre des autres pour ta sécurité financière ou à trop partager. Ce transit t'invite à l'indépendance.

## Ce que tu pourrais vivre
- Des finances trop liées à des partenaires
- Une difficulté à valoriser tes propres ressources
- Un équilibre financier qui dépend des autres

## Conseils pour ce transit
- Construis ta propre indépendance financière
- Ta valeur ne dépend pas de ce que tu reçois des autres
- L'équilibre vrai inclut ton autonomie""",

    ('libra', 3): """# ☋ Nœud Sud en Balance – Maison III

**En une phrase :** Ta communication diplomatique à l'excès doit oser la franchise.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison de la communication révèle une parole trop soucieuse de plaire, qui perd en authenticité. Ce transit t'invite à plus de franchise.

## Ce que tu pourrais vivre
- Des communications édulcorées pour ne froisser personne
- Une difficulté à exprimer ton avis réel
- Des relations de voisinage ou fraternelles trop policées

## Conseils pour ce transit
- La vraie diplomatie inclut la vérité
- Ton opinion a de la valeur même si elle déplaît
- L'harmonie vraie se construit sur l'authenticité""",

    ('libra', 4): """# ☋ Nœud Sud en Balance – Maison IV

**En une phrase :** Ton besoin d'harmonie familiale à tout prix doit s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison des racines révèle un besoin excessif de paix familiale qui peut te faire nier tes propres besoins. Ce transit t'invite à t'affirmer.

## Ce que tu pourrais vivre
- Un foyer où tu évites les conflits au détriment de toi
- Des relations familiales trop dépendantes
- Un passé où tu as trop sacrifié pour l'harmonie

## Conseils pour ce transit
- L'harmonie vraie n'exige pas que tu te renies
- Ta famille peut survivre à tes affirmations
- Crée un foyer qui respecte aussi TES besoins""",

    ('libra', 5): """# ☋ Nœud Sud en Balance – Maison V

**En une phrase :** Ta créativité qui cherche l'approbation et tes amours dépendantes doivent mûrir.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison de la joie révèle une créativité qui cherche la validation et des amours où tu te perds dans l'autre. Ce transit t'invite à créer et aimer pour toi.

## Ce que tu pourrais vivre
- Une créativité qui attend l'approbation avant de s'exprimer
- Des amours où tu te définis par l'autre
- Un plaisir qui dépend du partage obligatoire

## Conseils pour ce transit
- Crée pour toi-même, l'approbation est un bonus
- Aime sans te perdre dans l'autre
- La joie peut aussi être solitaire et entière""",

    ('libra', 6): """# ☋ Nœud Sud en Balance – Maison VI

**En une phrase :** Ta tendance à trop t'adapter au travail doit céder à l'affirmation de tes méthodes.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison du travail révèle une tendance à trop s'adapter aux autres dans le quotidien professionnel. Ce transit t'invite à affirmer tes propres méthodes.

## Ce que tu pourrais vivre
- Un travail où tu fais tout pour plaire aux collègues
- Des routines qui dépendent des préférences des autres
- Une santé affectée par trop de compromis

## Conseils pour ce transit
- Tes méthodes de travail ont de la valeur
- Tu n'as pas à plaire à tout le monde au bureau
- Prends soin de TOI, pas seulement de l'harmonie collective""",

    ('libra', 7): """# ☋ Nœud Sud en Balance – Maison VII

**En une phrase :** Ta dépendance aux relations et ton besoin d'être en couple doivent évoluer.

## L'énergie du moment
Le Nœud Sud en Balance est dans sa maison naturelle, amplifiant la dépendance relationnelle et le besoin d'être toujours en couple. Ce transit t'invite à l'autonomie dans les relations.

## Ce que tu pourrais vivre
- Une difficulté à être seul(e)
- Des relations où tu te définis par l'autre
- Un besoin d'harmonie qui te fait tout accepter

## Conseils pour ce transit
- Tu es entier(e) même sans partenaire
- L'équilibre vrai inclut ton indépendance
- Apprends à être bien seul(e) pour mieux être à deux""",

    ('libra', 8): """# ☋ Nœud Sud en Balance – Maison VIII

**En une phrase :** Ton évitement des conflits face aux crises doit céder au courage d'affronter.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison des transformations révèle une tendance à éviter les confrontations nécessaires dans les moments de crise. Ce transit t'invite au courage.

## Ce que tu pourrais vivre
- Des crises prolongées par l'évitement du conflit
- Une intimité qui manque de profondeur par peur de bousculer
- Des ressources partagées mal gérées par excès de conciliation

## Conseils pour ce transit
- Certaines transformations demandent la confrontation
- L'intimité vraie peut supporter le conflit
- Le courage est parfois plus aimant que l'évitement""",

    ('libra', 9): """# ☋ Nœud Sud en Balance – Maison IX

**En une phrase :** Ta philosophie qui cherche à plaire à tous doit affirmer sa propre vérité.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison de l'expansion révèle une spiritualité et des croyances qui cherchent le consensus. Ce transit t'invite à affirmer ta propre vision.

## Ce que tu pourrais vivre
- Des croyances qui changent selon l'interlocuteur
- Des voyages en groupe qui ne te transforment pas vraiment
- Un enseignement qui cherche trop à plaire

## Conseils pour ce transit
- Ta vérité peut exister même si elle ne plaît pas à tous
- Voyage seul(e) parfois pour vraiment te découvrir
- Enseigne ce que tu crois, pas ce qui fera l'unanimité""",

    ('libra', 10): """# ☋ Nœud Sud en Balance – Maison X

**En une phrase :** Ta carrière construite sur les relations et l'image agréable doit affirmer sa singularité.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison de la carrière révèle une réussite qui dépend trop des autres, de l'image et du réseau. Ce transit t'invite à une réussite plus personnelle.

## Ce que tu pourrais vivre
- Une carrière qui dépend trop des partenariats
- Une réputation d'être « agréable » plutôt que compétent(e)
- Un succès qui n'est pas vraiment le tien

## Conseils pour ce transit
- Construis ta réussite sur TES compétences
- Tu peux réussir sans tout le monde
- Ta singularité est ton atout le plus précieux""",

    ('libra', 11): """# ☋ Nœud Sud en Balance – Maison XI

**En une phrase :** Ton besoin d'être accepté(e) dans les groupes doit céder à l'affirmation de ta vision.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison des amitiés révèle une tendance à te conformer aux groupes pour être accepté(e). Ce transit t'invite à apporter ta vision unique.

## Ce que tu pourrais vivre
- Des groupes où tu te conformes plutôt que contribuer
- Des amitiés où tu fais tout pour plaire
- Des idéaux qui changent selon les cercles

## Conseils pour ce transit
- Apporte TA vision aux groupes, même si elle détonne
- Les vrais amis acceptent ta singularité
- Tes idéaux méritent d'être défendus""",

    ('libra', 12): """# ☋ Nœud Sud en Balance – Maison XII

**En une phrase :** Ta dépendance spirituelle aux autres doit céder à ton propre chemin intérieur.

## L'énergie du moment
Le Nœud Sud en Balance dans ta maison de l'invisible révèle une spiritualité qui cherche encore l'approbation ou le guide extérieur. Ce transit t'invite à ton propre chemin.

## Ce que tu pourrais vivre
- Une spiritualité qui dépend de maîtres ou de groupes
- Un karma de dépendance à libérer
- Une difficulté à méditer seul(e)

## Conseils pour ce transit
- Ta connexion au divin est directe et personnelle
- Tu es ton propre guide intérieur
- Le chemin spirituel est finalement solitaire""",

    # ============== SCORPIO ==============
    ('scorpio', 1): """# ☋ Nœud Sud en Scorpion – Maison I

**En une phrase :** Ton identité intense et contrôlante doit s'ouvrir à plus de légèreté et de confiance.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison I révèle une identité construite sur l'intensité, le contrôle et la profondeur. Ce transit t'invite à la légèreté et à la simplicité.

## Ce que tu pourrais vivre
- Une intensité qui épuise toi et les autres
- Un besoin de contrôle qui limite ta liberté
- Une image sombre ou mystérieuse qui isole

## Conseils pour ce transit
- Tu peux être profond(e) sans être toujours intense
- Le contrôle est une illusion, la confiance une force
- La légèreté n'est pas superficialité""",

    ('scorpio', 2): """# ☋ Nœud Sud en Scorpion – Maison II

**En une phrase :** Ton rapport obsessionnel aux ressources et au pouvoir doit s'assouplir.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison des ressources révèle une relation intense et parfois obsessionnelle avec l'argent et les possessions. Ce transit t'invite à plus de légèreté.

## Ce que tu pourrais vivre
- Une obsession pour les ressources et la sécurité
- Des luttes de pouvoir autour de l'argent
- Une difficulté à apprécier simplement ce que tu as

## Conseils pour ce transit
- L'abondance peut être simple et légère
- Lâche les luttes de pouvoir financières
- Ta valeur ne dépend pas de ton pouvoir sur les ressources""",

    ('scorpio', 3): """# ☋ Nœud Sud en Scorpion – Maison III

**En une phrase :** Ta communication intense et perçante doit apprendre la légèreté.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison de la communication révèle une parole qui va toujours aux profondeurs, parfois de façon blessante. Ce transit t'invite à plus de douceur.

## Ce que tu pourrais vivre
- Des communications qui creusent trop et font mal
- Une difficulté à rester en surface quand c'est approprié
- Des relations avec l'entourage marquées par l'intensité

## Conseils pour ce transit
- Tout n'a pas besoin d'être profond et intense
- La légèreté dans la communication est un art
- Apprends à converser sans tout décortiquer""",

    ('scorpio', 4): """# ☋ Nœud Sud en Scorpion – Maison IV

**En une phrase :** Ton foyer intense et les secrets familiaux doivent céder à la lumière.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison des racines révèle un passé familial marqué par les secrets, l'intensité ou les luttes de pouvoir. Ce transit t'invite à la guérison et à la légèreté.

## Ce que tu pourrais vivre
- Un foyer où l'intensité émotionnelle est la norme
- Des secrets familiaux qui demandent à être révélés
- Un passé marqué par les luttes de pouvoir

## Conseils pour ce transit
- Ton foyer peut être un lieu de paix, pas de drames
- Les secrets familiaux peuvent être libérés en douceur
- Crée de nouvelles racines basées sur la confiance, pas le contrôle""",

    ('scorpio', 5): """# ☋ Nœud Sud en Scorpion – Maison V

**En une phrase :** Tes amours intenses et ta créativité obsessionnelle doivent s'alléger.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison de la joie révèle une créativité qui puise dans les ténèbres et des amours trop intenses. Ce transit t'invite à la joie simple.

## Ce que tu pourrais vivre
- Des amours qui consument plutôt qu'elles n'épanouissent
- Une créativité qui ne touche qu'au sombre
- Un rapport au plaisir marqué par l'excès ou le contrôle

## Conseils pour ce transit
- L'amour peut être léger et joyeux
- Ta créativité peut aussi célébrer la lumière
- Le plaisir simple est aussi valable que l'intensité""",

    ('scorpio', 6): """# ☋ Nœud Sud en Scorpion – Maison VI

**En une phrase :** Ton travail obsessionnel et ton contrôle de la santé doivent céder.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison du travail révèle une approche trop intense et contrôlante du quotidien. Ce transit t'invite à la simplicité et à la confiance.

## Ce que tu pourrais vivre
- Un travail qui devient une obsession
- Un contrôle excessif de la santé et des routines
- Des relations de travail marquées par les luttes de pouvoir

## Conseils pour ce transit
- Le travail peut être fait avec légèreté
- La santé bénéficie de la confiance, pas du contrôle obsessionnel
- Lâche les luttes de pouvoir au quotidien""",

    ('scorpio', 7): """# ☋ Nœud Sud en Scorpion – Maison VII

**En une phrase :** Tes relations intenses et les luttes de pouvoir doivent céder à l'équilibre.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison des partenariats révèle des relations marquées par l'intensité, la jalousie ou les luttes de pouvoir. Ce transit t'invite à des liens plus équilibrés.

## Ce que tu pourrais vivre
- Des relations qui consument par leur intensité
- De la jalousie ou de la possessivité
- Des partenariats marqués par les luttes de pouvoir

## Conseils pour ce transit
- L'amour vrai n'a pas besoin de tout contrôler
- L'équilibre est plus durable que l'intensité
- Laisse à l'autre sa liberté pour qu'il choisisse de rester""",

    ('scorpio', 8): """# ☋ Nœud Sud en Scorpion – Maison VIII

**En une phrase :** Ton attraction pour les profondeurs et les transformations doit trouver un équilibre.

## L'énergie du moment
Le Nœud Sud en Scorpion est dans sa maison naturelle, amplifiant l'attraction pour l'intensité, les crises et les transformations. Ce transit t'invite à la paix et à la stabilité.

## Ce que tu pourrais vivre
- Une fascination pour les crises et les renaissances
- Des transformations épuisantes à répétition
- Une intimité marquée par l'obsession

## Conseils pour ce transit
- Tu n'as pas besoin de crise pour te sentir vivant(e)
- La stabilité peut coexister avec la profondeur
- L'intimité vraie est paisible, pas seulement intense""",

    ('scorpio', 9): """# ☋ Nœud Sud en Scorpion – Maison IX

**En une phrase :** Ta quête spirituelle obsessionnelle des mystères doit s'ouvrir à la simplicité.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison de l'expansion révèle une spiritualité trop focalisée sur les mystères sombres. Ce transit t'invite à une sagesse plus lumineuse.

## Ce que tu pourrais vivre
- Une spiritualité fascinée par l'occulte et les ténèbres
- Des voyages vers des lieux de pouvoir ou de mort
- Des croyances trop centrées sur la transformation

## Conseils pour ce transit
- La sagesse inclut aussi la lumière et la joie
- Voyage vers des lieux qui élèvent, pas seulement qui transforment
- Ta philosophie peut célébrer la vie, pas seulement comprendre la mort""",

    ('scorpio', 10): """# ☋ Nœud Sud en Scorpion – Maison X

**En une phrase :** Ta carrière basée sur le pouvoir et l'intensité doit s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison de la carrière révèle une réussite construite sur le pouvoir, le contrôle ou les zones d'ombre. Ce transit t'invite à une réussite plus lumineuse.

## Ce que tu pourrais vivre
- Une carrière qui utilise le pouvoir de façon excessive
- Une réputation d'être quelqu'un avec qui il ne faut pas jouer
- Un succès construit sur des zones d'ombre

## Conseils pour ce transit
- Le vrai leadership n'a pas besoin de la peur
- Ta réussite peut être construite sur la confiance, pas le contrôle
- Une carrière peut être puissante et lumineuse à la fois""",

    ('scorpio', 11): """# ☋ Nœud Sud en Scorpion – Maison XI

**En une phrase :** Ton contrôle des groupes et tes amitiés intenses doivent s'équilibrer.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison des amitiés révèle des relations de groupe marquées par l'intensité et les luttes de pouvoir. Ce transit t'invite à des connexions plus légères.

## Ce que tu pourrais vivre
- Des amitiés qui deviennent obsessionnelles
- Un rôle de pouvoir dans les groupes qui isole
- Des idéaux portés avec trop d'intensité

## Conseils pour ce transit
- L'amitié peut être légère et joyeuse
- Le pouvoir dans les groupes peut être partagé
- Tes idéaux peuvent s'exprimer sans drame""",

    ('scorpio', 12): """# ☋ Nœud Sud en Scorpion – Maison XII

**En une phrase :** Ton attachement aux profondeurs et aux mystères de l'inconscient doit céder à la paix.

## L'énergie du moment
Le Nœud Sud en Scorpion dans ta maison de l'invisible révèle une fascination pour les zones d'ombre de l'inconscient. Ce transit t'invite à la lumière spirituelle.

## Ce que tu pourrais vivre
- Une spiritualité fascinée par les ténèbres
- Un karma d'intensité et de pouvoir à libérer
- Des rêves marqués par la mort et la transformation

## Conseils pour ce transit
- L'illumination est au-delà des ténèbres, pas dans leur exploration éternelle
- Ton karma peut se libérer dans la paix, pas seulement dans l'intensité
- La lumière spirituelle est ta destination, pas les profondeurs""",
}


async def insert_interpretations():
    """Insert South Node transit interpretations for Leo, Virgo, Libra, Scorpio"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_SOUTH_NODE_INTERPRETATIONS.items():
            # Check if exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_south_node',
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
                subject='transit_south_node',
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
        print(f"✅ Transit South Node (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
