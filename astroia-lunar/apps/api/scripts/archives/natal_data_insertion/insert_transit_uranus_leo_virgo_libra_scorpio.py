#!/usr/bin/env python3
"""Insert transit_uranus interpretations for Leo, Virgo, Libra, Scorpio (V2)"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_URANUS_INTERPRETATIONS = {
    # ============================================================
    # URANUS EN LION (♅ en ♌)
    # ============================================================
    ('leo', 1): """# ♅ Transit d'Uranus en Lion — Maison I

**En une phrase :** Ton identité se réinvente de façon spectaculaire avec un besoin d'expression unique.

## L'énergie du moment
Uranus en Lion dans ta maison I déclenche une révolution créative de ton identité. Tu ressens le besoin de briller de façon authentique, de te distinguer de la masse avec originalité. Ton apparence et ta présentation peuvent devenir plus théâtrales, plus audacieuses. Tu refuses les conventions qui t'empêchent d'exprimer ta singularité lumineuse.

## Ce que tu pourrais vivre
- Une transformation spectaculaire de ton image
- Le besoin irrépressible de t'exprimer de façon unique
- Une présence qui attire l'attention de façon inattendue
- La revendication de ta créativité comme partie de ton identité

## Conseils pour ce transit
- Ose briller sans te soucier des jugements
- Exprime ta créativité à travers ton apparence
- Trouve l'équilibre entre originalité et ego""",

    ('leo', 2): """# ♅ Transit d'Uranus en Lion — Maison II

**En une phrase :** Tes talents créatifs deviennent des sources de revenus et ta générosité redéfinit tes valeurs.

## L'énergie du moment
Uranus en Lion secoue ta maison des ressources avec une énergie créative et généreuse. Tes revenus peuvent venir de talents artistiques ou de ta capacité à briller. Tu valorises ce qui permet l'expression de soi et la générosité. Attention à l'équilibre entre les dépenses spectaculaires et la stabilité financière.

## Ce que tu pourrais vivre
- Des revenus liés à tes talents créatifs ou au divertissement
- Une générosité parfois excessive dans tes dépenses
- L'importance de ce qui te fait briller comme valeur
- Des fluctuations financières liées à ta créativité

## Conseils pour ce transit
- Monétise tes talents créatifs sans les brader
- Équilibre générosité et prudence financière
- Investis dans ce qui nourrit ton expression""",

    ('leo', 3): """# ♅ Transit d'Uranus en Lion — Maison III

**En une phrase :** Ta communication devient plus créative et théâtrale, captivant l'attention.

## L'énergie du moment
Uranus en Lion électrifie ta maison de la communication avec une énergie expressive. Tu t'exprimes de façon plus dramatique, plus créative, plus captivante. Tes idées veulent briller et être entendues. Tes relations avec tes proches s'animent de joie et parfois de petits drames. Tu as besoin que tes mots aient de l'impact.

## Ce que tu pourrais vivre
- Une communication plus théâtrale et expressive
- Des idées créatives qui demandent à être partagées
- Des dynamiques plus intenses avec tes proches
- L'attrait pour l'écriture créative ou la performance

## Conseils pour ce transit
- Utilise ton charisme communicatif positivement
- Garde de l'humilité malgré le désir de briller
- Amuse-toi avec tes mots et tes idées""",

    ('leo', 4): """# ♅ Transit d'Uranus en Lion — Maison IV

**En une phrase :** Ton foyer devient un lieu d'expression créative et de célébration de toi-même.

## L'énergie du moment
Uranus en Lion dans ta maison IV transforme ton espace domestique en scène personnelle. Tu as besoin que ton foyer reflète ta créativité et ta personnalité unique. Des changements spectaculaires dans ta vie familiale sont possibles. Tu prends ta place dans la dynamique familiale de façon plus affirmée.

## Ce que tu pourrais vivre
- Une décoration ou rénovation créative de ton espace
- Des changements dans les dynamiques familiales de pouvoir
- Le besoin de t'affirmer dans ton clan familial
- Un foyer qui devient lieu de créativité et de fête

## Conseils pour ce transit
- Crée un espace qui célèbre qui tu es
- Trouve ta place dans la famille sans écraser les autres
- Transforme ton foyer en sanctuaire créatif""",

    ('leo', 5): """# ♅ Transit d'Uranus en Lion — Maison V

**En une phrase :** Une explosion créative et des amours passionnées mais imprévisibles illuminent ta vie.

## L'énergie du moment
Uranus traverse sa maison de joie avec l'énergie flamboyante du Lion. Ta créativité atteint des sommets d'originalité et de brillance. En amour, tu vis des passions intenses, des coups de foudre spectaculaires, mais attention à la dramatisation. Tu veux être aimé pour ta singularité. Les jeux et divertissements prennent une dimension créative.

## Ce que tu pourrais vivre
- Une créativité exceptionnellement féconde et originale
- Des amours passionnées mais parfois instables
- Le besoin d'être célébré et admiré en amour
- Des expériences de jeu et de plaisir mémorables

## Conseils pour ce transit
- Canalise cette énergie créative exceptionnelle
- En amour, garde les pieds sur terre malgré la passion
- Célèbre la vie sans t'épuiser en drames""",

    ('leo', 6): """# ♅ Transit d'Uranus en Lion — Maison VI

**En une phrase :** Ton quotidien se transforme pour inclure plus de créativité et d'expression personnelle.

## L'énergie du moment
Uranus en Lion révolutionne ta maison du travail quotidien. Tu refuses un travail qui ne permet pas d'exprimer ta créativité. Ton environnement de travail doit te permettre de briller. Ta santé bénéficie d'activités qui nourrissent ta joie de vivre et ton expression créative.

## Ce que tu pourrais vivre
- Le besoin de créativité dans ton travail quotidien
- Des changements professionnels pour plus d'expression
- Une santé liée à ta joie de vivre et ton expression
- La transformation de tâches routinières en actes créatifs

## Conseils pour ce transit
- Injecte de la créativité dans ton quotidien
- Choisis un travail qui permet ton expression
- Prends soin de toi par des activités joyeuses""",

    ('leo', 7): """# ♅ Transit d'Uranus en Lion — Maison VII

**En une phrase :** Tes relations deviennent des scènes de passion créative et de reconnaissance mutuelle.

## L'énergie du moment
Uranus en Lion traverse ta maison des partenariats avec une énergie dramatique. Tu attires des partenaires créatifs, charismatiques, parfois égocentriques. Tes relations demandent de l'espace pour que chacun brille. Des tensions peuvent émerger autour de la reconnaissance et de l'attention. Tu cherches un partenaire qui célèbre ta singularité.

## Ce que tu pourrais vivre
- Des relations passionnées et créatives
- Des tensions autour de qui brille le plus
- L'attrait pour des partenaires charismatiques
- Le besoin d'être admiré dans tes relations

## Conseils pour ce transit
- Apprends à briller avec, pas contre, ton partenaire
- Choisis quelqu'un qui célèbre ta singularité
- Évite les drames de pouvoir en relation""",

    ('leo', 8): """# ♅ Transit d'Uranus en Lion — Maison VIII

**En une phrase :** Des transformations profondes touchent ton ego et ta relation au pouvoir.

## L'énergie du moment
Uranus en Lion plonge dans ta maison des transformations, travaillant sur ton ego et ta volonté de puissance. Des situations qui défient ton orgueil peuvent te transformer profondément. Ta relation au pouvoir et à la reconnaissance est bousculée. Tu peux vivre des renaissances spectaculaires après des épreuves d'ego.

## Ce que tu pourrais vivre
- Des défis à ton orgueil qui te transforment
- Des questions de pouvoir dans les ressources partagées
- La mort et renaissance de certains aspects de ton ego
- Des expériences intimes qui changent ta relation au contrôle

## Conseils pour ce transit
- Accepte les défis à ton ego comme opportunités de croissance
- Apprends à lâcher le besoin de contrôle
- Transforme ton orgueil en confiance humble""",

    ('leo', 9): """# ♅ Transit d'Uranus en Lion — Maison IX

**En une phrase :** Ta philosophie de vie intègre la joie créative et tes voyages célèbrent la vie.

## L'énergie du moment
Uranus en Lion traverse ta maison des horizons lointains avec une énergie festive. Tu es attiré par des philosophies qui célèbrent la vie, la créativité, l'expression de soi. Tes voyages peuvent inclure des festivals, des lieux de créativité, des cultures solaires. Tu développes une foi en ta propre lumière intérieure.

## Ce que tu pourrais vivre
- L'attrait pour des philosophies de joie et d'expression
- Des voyages vers des destinations festives ou artistiques
- Le développement d'une confiance en ta créativité unique
- L'enseignement ou le partage de ta vision lumineuse

## Conseils pour ce transit
- Cultive une philosophie qui célèbre la vie
- Voyage pour t'inspirer et créer
- Partage ta lumière avec générosité""",

    ('leo', 10): """# ♅ Transit d'Uranus en Lion — Maison X

**En une phrase :** Ta carrière s'oriente vers des domaines créatifs où tu peux briller authentiquement.

## L'énergie du moment
Uranus en Lion révolutionne ta maison de la carrière avec une énergie de star. Tu ne te contentes plus d'un rôle ordinaire dans le monde professionnel. Tu aspires à une position où ta créativité et ta singularité sont reconnues. Des opportunités spectaculaires mais parfois instables peuvent se présenter.

## Ce que tu pourrais vivre
- Une carrière dans des domaines créatifs ou de divertissement
- Le besoin de reconnaissance et de visibilité professionnelle
- Des opportunités de leadership créatif
- Des hauts et des bas spectaculaires dans ta trajectoire

## Conseils pour ce transit
- Poursuis une carrière qui permet ton expression
- Équilibre l'ambition et l'humilité
- Utilise ta visibilité pour inspirer les autres""",

    ('leo', 11): """# ♅ Transit d'Uranus en Lion — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des collectifs créatifs et tes aspirations brillent.

## L'énergie du moment
Uranus en Lion traverse ta maison des amitiés et des idéaux avec une énergie créative collective. Tu es attiré par des groupes de créatifs, d'artistes, de personnes qui osent briller. Tes aspirations incluent l'expression de ta singularité et la contribution au monde par ta créativité.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes créatives et charismatiques
- L'appartenance à des collectifs artistiques ou expressifs
- Des aspirations qui incluent briller et inspirer
- Des projets de groupe créatifs et ambitieux

## Conseils pour ce transit
- Entoure-toi de personnes qui t'inspirent à briller
- Contribue au collectif par ta créativité unique
- Rêve grand et lumineux""",

    ('leo', 12): """# ♅ Transit d'Uranus en Lion — Maison XII

**En une phrase :** Une transformation profonde de ton ego inconscient libère ta créativité authentique.

## L'énergie du moment
Uranus en Lion pénètre ta maison des profondeurs cachées, travaillant sur les aspects inconscients de ton ego. Des blessures liées à la reconnaissance, à la créativité bloquée, ou à l'expression réprimée peuvent émerger pour être guéries. Tu découvres une créativité qui vient de plus profond que l'ego.

## Ce que tu pourrais vivre
- La remontée de blessures liées à l'expression de soi
- La guérison de blocages créatifs inconscients
- Des rêves impliquant la création et la reconnaissance
- La découverte d'une créativité spirituelle

## Conseils pour ce transit
- Accueille les blessures d'ego avec compassion
- Explore ta créativité sans attente de reconnaissance
- Connecte-toi à une source créative plus grande que toi""",

    # ============================================================
    # URANUS EN VIERGE (♅ en ♍)
    # ============================================================
    ('virgo', 1): """# ♅ Transit d'Uranus en Vierge — Maison I

**En une phrase :** Ton identité se transforme vers plus d'efficacité et de service authentique.

## L'énergie du moment
Uranus en Vierge dans ta maison I révolutionne ta façon de te présenter au monde avec une énergie analytique et serviable. Tu développes une identité basée sur tes compétences pratiques et ta capacité à être utile. Ton apparence peut devenir plus sobre, plus fonctionnelle, reflétant une recherche d'efficacité authentique.

## Ce que tu pourrais vivre
- Une transformation vers plus de simplicité et d'efficacité
- Le besoin de te définir par ce que tu apportes concrètement
- Des changements dans ton apparence vers plus de fonctionnalité
- Une identité basée sur le service et les compétences

## Conseils pour ce transit
- Développe des compétences qui te distinguent
- Trouve ton identité dans le service sans t'effacer
- Simplifie ta présentation pour plus d'authenticité""",

    ('virgo', 2): """# ♅ Transit d'Uranus en Vierge — Maison II

**En une phrase :** Tes compétences pratiques deviennent tes meilleures ressources et tes valeurs s'affinent.

## L'énergie du moment
Uranus en Vierge secoue ta maison des ressources avec une énergie analytique. Tes revenus peuvent venir de tes compétences techniques, de ton sens du détail, de ta capacité à résoudre des problèmes. Tu valorises la qualité sur la quantité, l'utile sur le superflu. Tes finances bénéficient d'une approche plus méthodique.

## Ce que tu pourrais vivre
- Des revenus basés sur tes compétences spécifiques
- Une gestion financière plus rigoureuse et efficace
- Le tri de ce qui a vraiment de la valeur pour toi
- L'attrait pour des investissements pratiques et utiles

## Conseils pour ce transit
- Développe et monétise tes compétences techniques
- Gère tes finances avec méthode et précision
- Distingue l'essentiel du superflu dans tes possessions""",

    ('virgo', 3): """# ♅ Transit d'Uranus en Vierge — Maison III

**En une phrase :** Ta communication devient plus précise et tes analyses révolutionnent ta pensée.

## L'énergie du moment
Uranus en Vierge électrifie ta maison de la communication avec une énergie analytique. Ton esprit devient plus incisif, plus capable de distinguer les détails importants. Ta communication gagne en précision et en utilité. Tu es attiré par l'apprentissage de compétences techniques ou pratiques.

## Ce que tu pourrais vivre
- Une pensée plus analytique et critique
- L'apprentissage de compétences techniques nouvelles
- Une communication plus précise et moins bavarde
- Des relations avec les proches basées sur l'entraide pratique

## Conseils pour ce transit
- Affine ta pensée et ta communication
- Apprends des compétences utiles et pratiques
- Utilise ton analyse pour aider plutôt que critiquer""",

    ('virgo', 4): """# ♅ Transit d'Uranus en Vierge — Maison IV

**En une phrase :** Ton foyer se réorganise de façon plus efficace et plus saine.

## L'énergie du moment
Uranus en Vierge dans ta maison IV transforme ton espace domestique vers plus d'ordre et de fonctionnalité. Tu pourrais entreprendre un grand tri, une organisation méthodique de ton foyer. Ta vie familiale s'oriente vers des pratiques plus saines. Tu trouves ta sécurité dans un environnement bien organisé.

## Ce que tu pourrais vivre
- Une réorganisation majeure de ton espace de vie
- L'adoption de pratiques domestiques plus saines
- Des relations familiales basées sur l'aide mutuelle
- La simplification et le tri de ton foyer

## Conseils pour ce transit
- Crée un espace de vie ordonné et fonctionnel
- Adopte des habitudes familiales plus saines
- Trouve la paix dans l'organisation""",

    ('virgo', 5): """# ♅ Transit d'Uranus en Vierge — Maison V

**En une phrase :** Ta créativité s'exprime de façon plus technique et tes amours demandent de la substance.

## L'énergie du moment
Uranus en Vierge dans ta maison de la créativité apporte une expression plus précise et artisanale. Tu es attiré par des formes de création qui demandent technique et savoir-faire. En amour, tu recherches des relations qui ont du sens, de la substance, une utilité mutuelle. Les plaisirs simples et sains t'attirent.

## Ce que tu pourrais vivre
- Une créativité plus technique et artisanale
- Des amours basées sur l'estime et le respect mutuel
- Le plaisir dans les activités pratiques et utiles
- Des relations avec les enfants centrées sur l'apprentissage

## Conseils pour ce transit
- Développe un artisanat ou une technique créative
- Recherche des relations significatives plutôt que superficielles
- Trouve la joie dans la création de qualité""",

    ('virgo', 6): """# ♅ Transit d'Uranus en Vierge — Maison VI

**En une phrase :** Ton quotidien et ta santé connaissent une révolution vers plus d'efficacité et de bien-être.

## L'énergie du moment
Uranus traverse sa maison de prédilection avec l'énergie perfectionniste de la Vierge. Tes méthodes de travail se révolutionnent vers plus d'efficacité. Ta santé devient une priorité avec des approches innovantes mais pratiques. Tu optimises chaque aspect de ton quotidien pour le rendre plus fonctionnel.

## Ce que tu pourrais vivre
- Une transformation complète de tes méthodes de travail
- L'adoption de pratiques de santé innovantes et efficaces
- L'optimisation de ta routine quotidienne
- Des changements professionnels vers plus d'utilité

## Conseils pour ce transit
- Révolutionne tes habitudes vers plus d'efficacité
- Adopte une approche holistique mais pratique de la santé
- Perfectionne tes méthodes sans tomber dans l'obsession""",

    ('virgo', 7): """# ♅ Transit d'Uranus en Vierge — Maison VII

**En une phrase :** Tes relations se transforment autour du service mutuel et de l'amélioration réciproque.

## L'énergie du moment
Uranus en Vierge traverse ta maison des partenariats avec une énergie d'amélioration. Tu attires des partenaires qui t'aident à t'améliorer et vice versa. Les relations peuvent devenir plus pratiques, axées sur ce que vous construisez ensemble. Attention aux critiques excessives qui peuvent fragiliser les unions.

## Ce que tu pourrais vivre
- Des relations basées sur l'aide et l'amélioration mutuelle
- L'attrait pour des partenaires compétents et utiles
- Des tensions autour du perfectionnisme en relation
- La construction de projets pratiques ensemble

## Conseils pour ce transit
- Apprécie tes partenaires pour ce qu'ils apportent
- Évite les critiques destructrices dans les relations
- Construis des partenariats qui améliorent les deux parties""",

    ('virgo', 8): """# ♅ Transit d'Uranus en Vierge — Maison VIII

**En une phrase :** Des transformations profondes affinent ta relation aux ressources partagées et à la guérison.

## L'énergie du moment
Uranus en Vierge plonge dans ta maison des transformations avec une énergie analytique et purificatrice. Tu analyses en profondeur tes arrangements financiers partagés et les améliores. Ta relation à la guérison et à la transformation devient plus méthodique. Tu découvres que le détail peut être transformateur.

## Ce que tu pourrais vivre
- Une révision méthodique de tes finances partagées
- L'intérêt pour des techniques de guérison précises
- La transformation par l'analyse et la compréhension
- Des améliorations dans tes relations intimes par le dialogue

## Conseils pour ce transit
- Analyse et améliore tes arrangements partagés
- Explore des méthodes de guérison structurées
- Transforme-toi par la compréhension précise""",

    ('virgo', 9): """# ♅ Transit d'Uranus en Vierge — Maison IX

**En une phrase :** Ta philosophie devient plus pratique et tes voyages t'apprennent des compétences utiles.

## L'énergie du moment
Uranus en Vierge traverse ta maison des horizons lointains avec une énergie pragmatique. Tu es attiré par des sagesses qui ont des applications pratiques, des enseignements qui améliorent la vie concrètement. Tes voyages peuvent inclure des formations ou des apprentissages. Ta spiritualité devient plus terrestre.

## Ce que tu pourrais vivre
- L'attrait pour des philosophies pratiques et applicables
- Des voyages d'apprentissage ou de service
- L'intérêt pour des traditions de sagesse terrestre
- L'enseignement ou le partage de compétences pratiques

## Conseils pour ce transit
- Recherche des sagesses qui améliorent le quotidien
- Voyage pour apprendre et servir
- Intègre spiritualité et vie pratique""",

    ('virgo', 10): """# ♅ Transit d'Uranus en Vierge — Maison X

**En une phrase :** Ta carrière se réoriente vers des rôles de service, d'analyse ou de santé.

## L'énergie du moment
Uranus en Vierge révolutionne ta maison de la carrière avec une énergie de service. Tu pourrais te diriger vers des métiers de la santé, de l'analyse, de l'amélioration des systèmes. Ta réputation se construit sur ta compétence et ton utilité. Tu recherches une carrière qui contribue concrètement.

## Ce que tu pourrais vivre
- Une carrière dans la santé, l'analyse ou le service
- La réputation d'être compétent et utile
- Des changements professionnels vers plus de sens pratique
- La reconnaissance pour tes capacités d'amélioration

## Conseils pour ce transit
- Poursuis une carrière où tes compétences servent
- Construis ta réputation sur la qualité de ton travail
- Contribue à améliorer les systèmes qui t'entourent""",

    ('virgo', 11): """# ♅ Transit d'Uranus en Vierge — Maison XI

**En une phrase :** Tes cercles sociaux s'orientent vers le service collectif et l'amélioration du monde.

## L'énergie du moment
Uranus en Vierge traverse ta maison des amitiés et des idéaux avec une énergie de service. Tu es attiré par des groupes qui œuvrent pour l'amélioration concrète de la société. Tes aspirations incluent contribuer utilement au monde. Tes amis partagent des valeurs de service et de compétence.

## Ce que tu pourrais vivre
- Des amitiés avec des personnes compétentes et serviables
- L'engagement dans des causes d'amélioration pratique
- Des aspirations d'utilité et de contribution concrète
- Des projets collectifs visant l'efficacité sociale

## Conseils pour ce transit
- Rejoins des groupes qui améliorent concrètement le monde
- Contribue par tes compétences spécifiques
- Rêve d'un monde plus efficace et sain""",

    ('virgo', 12): """# ♅ Transit d'Uranus en Vierge — Maison XII

**En une phrase :** Une guérison profonde de tes patterns de perfectionnisme et d'autocritique inconscients.

## L'énergie du moment
Uranus en Vierge pénètre ta maison des profondeurs cachées, travaillant sur tes tendances perfectionnistes inconscientes. Des habitudes d'autocritique excessive peuvent être révélées et guéries. Tu développes une approche plus compatissante de tes imperfections. Le service désintéressé devient un chemin de guérison.

## Ce que tu pourrais vivre
- La prise de conscience de patterns d'autocritique
- La guérison de perfectionnisme qui bloque
- Le développement d'une compassion pratique pour toi-même
- Le service comme voie de transformation spirituelle

## Conseils pour ce transit
- Sois plus doux avec tes imperfections
- Transforme l'autocritique en amélioration bienveillante
- Découvre la spiritualité dans le service humble""",

    # ============================================================
    # URANUS EN BALANCE (♅ en ♎)
    # ============================================================
    ('libra', 1): """# ♅ Transit d'Uranus en Balance — Maison I

**En une phrase :** Ton identité se redéfinit autour de nouvelles façons de vivre les relations et l'harmonie.

## L'énergie du moment
Uranus en Balance dans ta maison I transforme ta façon de te présenter au monde à travers le prisme relationnel. Tu développes une identité qui intègre l'autre de façon nouvelle et originale. Ton apparence peut évoluer vers plus d'esthétique et d'équilibre. Tu cherches à être toi-même tout en restant en harmonie avec les autres.

## Ce que tu pourrais vivre
- Une nouvelle façon de te définir en relation avec les autres
- Des changements d'apparence vers plus d'esthétique
- Le besoin d'harmonie sans perdre ton individualité
- Une identité qui révolutionne les conventions sociales

## Conseils pour ce transit
- Trouve l'équilibre entre affirmation de soi et harmonie
- Laisse les autres t'inspirer sans te perdre
- Cultive la beauté comme expression de toi-même""",

    ('libra', 2): """# ♅ Transit d'Uranus en Balance — Maison II

**En une phrase :** Tes valeurs évoluent vers plus d'équité et tes revenus peuvent venir des partenariats.

## L'énergie du moment
Uranus en Balance secoue ta maison des ressources avec une énergie de justice et de partenariat. Tes revenus peuvent venir de collaborations ou de domaines liés à l'esthétique et aux relations. Tu valorises ce qui est juste et équitable. Ta relation à l'argent se transforme pour inclure le partage.

## Ce que tu pourrais vivre
- Des revenus issus de partenariats ou de collaborations
- L'importance croissante de l'équité dans tes finances
- La valorisation de la beauté et de l'art
- Des changements dans ta façon de partager les ressources

## Conseils pour ce transit
- Explore les partenariats comme sources de revenus
- Assure l'équité dans tes arrangements financiers
- Investis dans ce qui apporte harmonie et beauté""",

    ('libra', 3): """# ♅ Transit d'Uranus en Balance — Maison III

**En une phrase :** Ta communication devient plus diplomatique et tes idées cherchent l'équilibre.

## L'énergie du moment
Uranus en Balance électrifie ta maison de la communication avec une énergie harmonieuse. Tu développes une façon de communiquer qui recherche le consensus et l'équilibre des points de vue. Tes idées intègrent différentes perspectives. Tes relations avec tes proches s'orientent vers plus de diplomatie et d'équité.

## Ce que tu pourrais vivre
- Une communication plus diplomatique et équilibrée
- L'intérêt pour des idées qui réconcilient les opposés
- Des relations avec les proches plus harmonieuses
- L'apprentissage de la médiation et de la négociation

## Conseils pour ce transit
- Utilise la communication pour créer des ponts
- Écoute toutes les perspectives avant de conclure
- Pratique la diplomatie dans tes échanges quotidiens""",

    ('libra', 4): """# ♅ Transit d'Uranus en Balance — Maison IV

**En une phrase :** Ton foyer se transforme en lieu d'harmonie et d'équilibre relationnel.

## L'énergie du moment
Uranus en Balance dans ta maison IV révolutionne ton espace domestique avec une énergie esthétique. Tu as besoin que ton foyer soit beau, harmonieux, propice aux relations. La dynamique familiale évolue vers plus d'équité et de dialogue. Tu pourrais partager ton espace de vie de nouvelles façons.

## Ce que tu pourrais vivre
- Une transformation esthétique de ton espace de vie
- Des changements dans les relations familiales vers plus d'équilibre
- Le foyer comme lieu de rencontre et de partage
- Des cohabitations ou arrangements familiaux nouveaux

## Conseils pour ce transit
- Crée un foyer harmonieux et esthétique
- Travaille sur l'équilibre des relations familiales
- Rends ton espace accueillant pour les autres""",

    ('libra', 5): """# ♅ Transit d'Uranus en Balance — Maison V

**En une phrase :** Ta créativité s'exprime dans la beauté et tes amours recherchent l'harmonie parfaite.

## L'énergie du moment
Uranus en Balance enflamme ta maison de la créativité avec une énergie esthétique. Tu es attiré par des formes d'art qui recherchent l'équilibre et la beauté. En amour, tu poursuis une harmonie idéale, parfois au risque de l'idéalisation. Les relations créatives et les collaborations artistiques t'attirent.

## Ce que tu pourrais vivre
- Une créativité orientée vers la beauté et l'harmonie
- Des amours qui cherchent l'équilibre parfait
- L'attrait pour les collaborations artistiques
- Des plaisirs liés à l'esthétique et aux arts

## Conseils pour ce transit
- Exprime ta créativité dans la recherche du beau
- Accepte l'imperfection dans l'amour tout en visant l'harmonie
- Crée en collaboration avec d'autres""",

    ('libra', 6): """# ♅ Transit d'Uranus en Balance — Maison VI

**En une phrase :** Ton quotidien s'harmonise et tes relations de travail se transforment.

## L'énergie du moment
Uranus en Balance révolutionne ta maison du travail quotidien avec une énergie collaborative. Ton environnement de travail doit être harmonieux et équitable. Tes collègues deviennent importants pour ton bien-être. Ta santé bénéficie de l'équilibre et de relations saines.

## Ce que tu pourrais vivre
- Un environnement de travail plus harmonieux et équitable
- L'importance des relations dans ton quotidien professionnel
- La santé liée à l'équilibre relationnel
- Des méthodes de travail plus collaboratives

## Conseils pour ce transit
- Crée un environnement de travail harmonieux
- Développe des relations professionnelles équilibrées
- Prends soin de ta santé par l'équilibre de vie""",

    ('libra', 7): """# ♅ Transit d'Uranus en Balance — Maison VII

**En une phrase :** Tes relations se révolutionnent vers de nouvelles formes de partenariat plus équitables.

## L'énergie du moment
Uranus traverse son signe d'exaltation dans ta maison des partenariats, créant des changements majeurs. Tes relations intimes se transforment profondément, recherchant de nouvelles formes d'équilibre et de justice. Des unions peuvent se former ou se défaire autour de questions d'équité. Tu révolutionnes ta conception du partenariat idéal.

## Ce que tu pourrais vivre
- Des transformations majeures dans tes relations de couple
- La recherche de formes de partenariat plus équitables
- Des rencontres avec des personnes qui changent ta vision
- La redéfinition de ce qu'est un partenariat juste

## Conseils pour ce transit
- Sois ouvert à de nouvelles formes de relations
- Travaille sur l'équité réelle dans tes partenariats
- Accepte que les relations puissent évoluer radicalement""",

    ('libra', 8): """# ♅ Transit d'Uranus en Balance — Maison VIII

**En une phrase :** Des transformations profondes touchent ta façon de partager et de fusionner avec l'autre.

## L'énergie du moment
Uranus en Balance plonge dans ta maison des transformations, révolutionnant ta relation au partage profond. Les questions de ressources communes, d'intimité et de fusion sont bousculées. Tu cherches un équilibre plus juste dans ce que tu partages avec les autres. La justice dans les arrangements intimes devient importante.

## Ce que tu pourrais vivre
- Des révisions des arrangements financiers partagés
- Une transformation de ta façon de vivre l'intimité
- La recherche d'équité dans les questions de pouvoir intime
- Des expériences qui changent ta relation au partage

## Conseils pour ce transit
- Assure l'équité dans tes relations intimes
- Transforme ta relation au partage et à la fusion
- Cherche l'équilibre entre donner et recevoir""",

    ('libra', 9): """# ♅ Transit d'Uranus en Balance — Maison IX

**En une phrase :** Ta philosophie intègre la recherche de justice et d'équilibre universels.

## L'énergie du moment
Uranus en Balance traverse ta maison des horizons lointains avec une énergie de justice. Tu es attiré par des philosophies qui prônent l'équité, la paix, l'harmonie entre les peuples. Tes voyages peuvent te mener vers des cultures qui valorisent l'esthétique et les relations. Tu développes une vision du monde orientée vers l'équilibre.

## Ce que tu pourrais vivre
- L'attrait pour des philosophies de justice et de paix
- Des voyages vers des cultures raffinées et harmonieuses
- L'intérêt pour le droit international ou la médiation
- Une vision spirituelle basée sur l'équilibre et la beauté

## Conseils pour ce transit
- Développe une philosophie de justice et d'équilibre
- Voyage pour découvrir différentes façons de vivre en harmonie
- Contribue à la paix et à la compréhension mutuelle""",

    ('libra', 10): """# ♅ Transit d'Uranus en Balance — Maison X

**En une phrase :** Ta carrière s'oriente vers des domaines de collaboration, de médiation ou d'esthétique.

## L'énergie du moment
Uranus en Balance révolutionne ta maison de la carrière avec une énergie collaborative. Tu pourrais te diriger vers des métiers de la médiation, du droit, de l'art ou des relations publiques. Ta réputation se construit sur ta capacité à créer l'harmonie. Tu recherches des positions où le partenariat est central.

## Ce que tu pourrais vivre
- Une carrière dans la médiation, l'art ou les relations
- Des partenariats professionnels qui transforment ta trajectoire
- La réputation d'être juste et équitable
- Des positions de leadership collaboratif

## Conseils pour ce transit
- Poursuis une carrière qui crée de l'harmonie
- Construis ta réputation sur l'équité
- Développe des partenariats professionnels stratégiques""",

    ('libra', 11): """# ♅ Transit d'Uranus en Balance — Maison XI

**En une phrase :** Tes cercles sociaux deviennent des lieux d'harmonie et tes aspirations incluent la justice sociale.

## L'énergie du moment
Uranus en Balance traverse ta maison des amitiés et des idéaux avec une énergie de justice collective. Tu es attiré par des groupes qui œuvrent pour l'équité et la paix. Tes aspirations incluent un monde plus juste et plus beau. Tes amitiés se basent sur des valeurs d'équilibre et de réciprocité.

## Ce que tu pourrais vivre
- Des amitiés basées sur des valeurs d'équité
- L'engagement dans des causes de justice sociale
- Des aspirations d'un monde plus harmonieux
- Des groupes qui valorisent la beauté et les relations

## Conseils pour ce transit
- Entoure-toi de personnes qui partagent tes valeurs de justice
- Engage-toi pour l'équité et la paix
- Rêve d'un monde plus juste et plus beau""",

    ('libra', 12): """# ♅ Transit d'Uranus en Balance — Maison XII

**En une phrase :** Une guérison profonde de tes patterns relationnels inconscients et de ta dépendance à l'autre.

## L'énergie du moment
Uranus en Balance pénètre ta maison des profondeurs cachées, travaillant sur tes patterns relationnels inconscients. Des tendances à te perdre dans l'autre, à éviter le conflit à tout prix, ou à idéaliser les relations peuvent être révélées. Tu découvres un équilibre intérieur qui ne dépend pas de l'extérieur.

## Ce que tu pourrais vivre
- La prise de conscience de patterns de co-dépendance
- La guérison de blessures liées à l'injustice relationnelle
- Le développement d'un équilibre intérieur autonome
- Des rêves impliquant des relations et la justice

## Conseils pour ce transit
- Travaille sur ton équilibre intérieur indépendamment des autres
- Guéris les blessures relationnelles du passé
- Développe une harmonie qui vient de l'intérieur""",

    # ============================================================
    # URANUS EN SCORPION (♅ en ♏)
    # ============================================================
    ('scorpio', 1): """# ♅ Transit d'Uranus en Scorpion — Maison I

**En une phrase :** Ton identité traverse une mort et renaissance radicale vers plus d'authenticité profonde.

## L'énergie du moment
Uranus en Scorpion dans ta maison I déclenche une transformation profonde et irréversible de ton identité. Tu te défais de masques que tu portais depuis longtemps pour révéler une version plus authentique et puissante de toi-même. Ce processus peut être intense, mais il libère des ressources intérieures insoupçonnées.

## Ce que tu pourrais vivre
- Une transformation radicale de ton apparence ou attitude
- La mort d'anciennes versions de toi-même
- L'émergence d'une puissance personnelle nouvelle
- Des changements intenses qui révèlent qui tu es vraiment

## Conseils pour ce transit
- Accepte de laisser mourir ce qui ne te sert plus
- Embrasse la transformation même si elle est intense
- Découvre ta puissance authentique""",

    ('scorpio', 2): """# ♅ Transit d'Uranus en Scorpion — Maison II

**En une phrase :** Ta relation aux ressources se transforme profondément à travers des crises régénératrices.

## L'énergie du moment
Uranus en Scorpion secoue ta maison des ressources avec une énergie de transformation profonde. Tes finances peuvent traverser des crises qui mènent à une régénération. Tu développes une nouvelle relation au pouvoir de l'argent et des possessions. Des ressources cachées peuvent émerger de façon inattendue.

## Ce que tu pourrais vivre
- Des crises financières qui mènent à la transformation
- La découverte de ressources ou talents cachés
- Une nouvelle relation au pouvoir de l'argent
- Des revenus provenant de domaines transformateurs

## Conseils pour ce transit
- Vois les crises financières comme des opportunités
- Explore tes ressources cachées
- Développe une relation saine au pouvoir matériel""",

    ('scorpio', 3): """# ♅ Transit d'Uranus en Scorpion — Maison III

**En une phrase :** Ta pensée gagne en profondeur et ta communication révèle des vérités cachées.

## L'énergie du moment
Uranus en Scorpion électrifie ta maison de la communication avec une énergie pénétrante. Ta pensée devient plus incisive, capable de percer les surfaces. Tu es attiré par les sujets tabous, les mystères, les vérités cachées. Tes communications peuvent transformer ceux qui les reçoivent.

## Ce que tu pourrais vivre
- Une pensée qui perce les apparences
- L'intérêt pour les sujets profonds et tabous
- Des communications qui révèlent des secrets
- Des transformations dans les relations proches

## Conseils pour ce transit
- Utilise ta perspicacité avec sagesse
- Explore les sujets profonds qui t'attirent
- Communique les vérités avec compassion""",

    ('scorpio', 4): """# ♅ Transit d'Uranus en Scorpion — Maison IV

**En une phrase :** Ton foyer et tes racines traversent une transformation profonde qui libère des secrets familiaux.

## L'énergie du moment
Uranus en Scorpion dans ta maison IV crée des bouleversements profonds dans ta vie domestique et familiale. Des secrets de famille peuvent émerger. Tu traverses une transformation de tes fondations qui, bien qu'intense, te libère de patterns ancestraux. Ton concept de foyer et de sécurité se régénère.

## Ce que tu pourrais vivre
- Des révélations sur l'histoire familiale
- Des transformations profondes de ton lieu de vie
- La libération de patterns familiaux lourds
- Une nouvelle définition de la sécurité intérieure

## Conseils pour ce transit
- Accueille les révélations familiales avec courage
- Laisse mourir ce qui doit mourir dans ton passé
- Reconstruis des fondations plus authentiques""",

    ('scorpio', 5): """# ♅ Transit d'Uranus en Scorpion — Maison V

**En une phrase :** Ta créativité devient plus intense et tes amours transformatrices.

## L'énergie du moment
Uranus en Scorpion enflamme ta maison de la créativité avec une énergie de passion intense. Ta créativité touche des thèmes profonds, parfois sombres, mais toujours transformateurs. En amour, tu vis des passions qui te changent en profondeur. Les relations superficielles ne t'intéressent plus.

## Ce que tu pourrais vivre
- Une créativité qui explore les profondeurs de l'âme
- Des amours intenses et transformatrices
- Des passions qui te révèlent à toi-même
- Des expériences qui changent ta relation au plaisir

## Conseils pour ce transit
- Canalise l'intensité dans la création
- Accepte que l'amour te transforme profondément
- Explore les profondeurs sans te perdre""",

    ('scorpio', 6): """# ♅ Transit d'Uranus en Scorpion — Maison VI

**En une phrase :** Ton quotidien traverse une purification intense et ta santé se régénère.

## L'énergie du moment
Uranus en Scorpion révolutionne ta maison du travail quotidien et de la santé avec une énergie purificatrice. Tu pourrais traverser des crises de santé ou de travail qui mènent à une régénération. Ton quotidien doit changer en profondeur pour te permettre de te transformer. Des méthodes de guérison puissantes t'attirent.

## Ce que tu pourrais vivre
- Des crises de santé qui mènent à la régénération
- Des transformations profondes de tes routines
- L'attrait pour des pratiques de guérison intenses
- Des changements radicaux dans ton travail quotidien

## Conseils pour ce transit
- Vois les crises de santé comme des appels à la transformation
- Adopte des pratiques purificatrices
- Laisse ton quotidien se régénérer en profondeur""",

    ('scorpio', 7): """# ♅ Transit d'Uranus en Scorpion — Maison VII

**En une phrase :** Tes relations traversent des morts et renaissances qui les transforment ou les terminent.

## L'énergie du moment
Uranus en Scorpion traverse ta maison des partenariats avec une énergie de transformation profonde. Tes relations sont testées en profondeur. Certaines ne survivront pas à cette intensité tandis que d'autres se régénéreront plus fortes. Tu attires des partenaires qui te transforment et que tu transformes.

## Ce que tu pourrais vivre
- Des crises relationnelles qui transforment ou terminent
- Des partenaires intenses et transformateurs
- La mort d'anciennes façons de vivre les relations
- Des unions qui touchent des profondeurs insoupçonnées

## Conseils pour ce transit
- Accepte que les relations doivent parfois mourir pour renaître
- Choisis des partenaires qui t'aident à te transformer
- Traverse les crises relationnelles avec courage""",

    ('scorpio', 8): """# ♅ Transit d'Uranus en Scorpion — Maison VIII

**En une phrase :** Des transformations puissantes et irréversibles touchent les aspects les plus profonds de ta vie.

## L'énergie du moment
Uranus traverse sa maison naturelle de transformation avec l'énergie intense du Scorpion. Cette position est extrêmement puissante pour des changements profonds et irréversibles. Des morts et renaissances à tous les niveaux sont possibles. Tu accèdes à des pouvoirs de régénération exceptionnels.

## Ce que tu pourrais vivre
- Des transformations radicales et irréversibles
- L'accès à des ressources psychiques profondes
- Des expériences de mort symbolique puissantes
- Des changements majeurs dans les ressources partagées

## Conseils pour ce transit
- Accueille les transformations profondes avec confiance
- Utilise tes pouvoirs de régénération sagement
- Traverse les morts symboliques comme des initiations""",

    ('scorpio', 9): """# ♅ Transit d'Uranus en Scorpion — Maison IX

**En une phrase :** Ta philosophie de vie se transforme en profondeur à travers des révélations puissantes.

## L'énergie du moment
Uranus en Scorpion traverse ta maison des horizons lointains avec une énergie de quête profonde. Tu es attiré par des sagesses qui touchent les mystères de la vie et de la mort. Tes voyages peuvent te mener vers des lieux de pouvoir ou de transformation. Ta vision du monde se régénère complètement.

## Ce que tu pourrais vivre
- L'attrait pour des traditions ésotériques ou mystiques
- Des voyages transformateurs vers des lieux de pouvoir
- Des révélations spirituelles qui changent ta vision
- Une philosophie qui intègre la mort et la renaissance

## Conseils pour ce transit
- Explore les sagesses profondes avec discernement
- Voyage vers des lieux qui te transforment
- Développe une spiritualité qui embrasse tous les cycles""",

    ('scorpio', 10): """# ♅ Transit d'Uranus en Scorpion — Maison X

**En une phrase :** Ta carrière traverse des transformations radicales qui révèlent ton vrai pouvoir.

## L'énergie du moment
Uranus en Scorpion révolutionne ta maison de la carrière avec une énergie de pouvoir transformateur. Tu pourrais te diriger vers des métiers liés à la transformation, la guérison, les ressources partagées ou les crises. Ta réputation peut traverser des morts et renaissances. Tu découvres ton vrai pouvoir professionnel.

## Ce que tu pourrais vivre
- Des transformations radicales de carrière
- Des positions de pouvoir transformateur
- Une réputation qui se régénère après des crises
- Des métiers liés à la transformation ou aux ressources

## Conseils pour ce transit
- Accepte les morts professionnelles comme des renaissances
- Utilise ton pouvoir professionnellement avec éthique
- Construis une carrière alignée avec ton pouvoir profond""",

    ('scorpio', 11): """# ♅ Transit d'Uranus en Scorpion — Maison XI

**En une phrase :** Tes cercles sociaux se transforment et tes aspirations deviennent plus profondes.

## L'énergie du moment
Uranus en Scorpion traverse ta maison des amitiés et des idéaux avec une énergie transformatrice. Tes amitiés peuvent traverser des crises qui les purifient ou les terminent. Tu es attiré par des groupes qui œuvrent pour la transformation profonde du monde. Tes aspirations touchent à l'évolution collective.

## Ce que tu pourrais vivre
- Des amitiés intenses et transformatrices
- L'engagement dans des causes de transformation collective
- Des aspirations liées au pouvoir de changement
- Des groupes qui travaillent sur des thèmes profonds

## Conseils pour ce transit
- Laisse tes amitiés évoluer ou se terminer naturellement
- Engage-toi dans des causes de transformation authentique
- Rêve d'un monde transformé en profondeur""",

    ('scorpio', 12): """# ♅ Transit d'Uranus en Scorpion — Maison XII

**En une phrase :** Une transformation profonde de ton inconscient libère d'anciens karmas et traumas.

## L'énergie du moment
Uranus en Scorpion pénètre ta maison des profondeurs cachées, travaillant sur les couches les plus anciennes de ton psychisme. Des traumas enfouis, des karmas anciens peuvent remonter pour être libérés. Tu accèdes à des pouvoirs psychiques et de guérison qui étaient dormants. Une purification profonde de l'inconscient est en cours.

## Ce que tu pourrais vivre
- La remontée de traumas anciens pour guérison
- L'accès à des capacités psychiques dormantes
- Des rêves intenses révélant des contenus inconscients
- Une transformation spirituelle profonde

## Conseils pour ce transit
- Accueille ce qui remonte avec courage et compassion
- Travaille avec un thérapeute si nécessaire
- Développe tes capacités de guérison intérieure""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in TRANSIT_URANUS_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_uranus',
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
                subject='transit_uranus',
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
        print(f"✅ Transit Uranus (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
