#!/usr/bin/env python3
"""
Insert transit_north_node interpretations V2 for Sagittarius, Capricorn, Aquarius, Pisces (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_NORTH_NODE_INTERPRETATIONS = {
    # ============== SAGITTARIUS ==============
    ('sagittarius', 1): """# ☊ Nœud Nord en Sagittaire – Maison I

**En une phrase :** L'univers t'invite à incarner l'aventurier, le philosophe et l'explorateur de sens.

## L'énergie du moment
Le Nœud Nord en Sagittaire dans ta maison I t'appelle à devenir un être de quête, d'expansion et d'optimisme. Ta croissance passe par la foi en la vie, l'ouverture à l'inconnu et le courage d'explorer.

## Ce que tu pourrais vivre
- Un besoin de te définir par tes idéaux et ta vision
- Une redéfinition de ton image vers plus d'audace et d'ouverture
- Des situations qui t'invitent à l'aventure et à l'expansion

## Conseils pour ce transit
- Deviens l'aventurier de ta propre vie
- Cultive l'optimisme et la foi comme forces personnelles
- Ose voir grand et élargir tes horizons""",

    ('sagittarius', 2): """# ☊ Nœud Nord en Sagittaire – Maison II

**En une phrase :** Ta mission karmique te guide vers une abondance qui vient de l'expansion et de la foi.

## L'énergie du moment
Le Nœud Nord en Sagittaire élargit ta maison des ressources. Tu es invité(e) à développer une relation généreuse et optimiste avec l'argent, à valoriser les expériences et la sagesse.

## Ce que tu pourrais vivre
- Des revenus liés à l'enseignement, les voyages ou la philosophie
- Un questionnement sur ce qui constitue la vraie richesse
- Une abondance qui vient quand tu oses voir grand

## Conseils pour ce transit
- Valorise les expériences autant que les possessions
- Ose investir dans ton expansion personnelle
- Fais confiance que l'abondance vient quand tu suis ta vision""",

    ('sagittarius', 3): """# ☊ Nœud Nord en Sagittaire – Maison III

**En une phrase :** Tu es appelé(e) à communiquer tes visions et tes idéaux avec enthousiasme.

## L'énergie du moment
Le Nœud Nord en Sagittaire enflamme ta maison de la communication. Ta croissance passe par le partage de tes grandes idées, l'enseignement inspirant et la communication qui élève.

## Ce que tu pourrais vivre
- Une communication plus inspirante et visionnaire
- Des apprentissages liés à la philosophie, aux langues ou aux voyages
- Un rôle de messager d'idées qui élargissent les horizons

## Conseils pour ce transit
- Partage tes visions avec enthousiasme
- Apprends des sujets qui élargissent ta compréhension du monde
- Communique pour inspirer et élever les autres""",

    ('sagittarius', 4): """# ☊ Nœud Nord en Sagittaire – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un foyer ouvert sur le monde.

## L'énergie du moment
Le Nœud Nord en Sagittaire élargit ta maison des racines. Tu es appelé(e) à créer un chez-toi qui célèbre la diversité, l'exploration et la quête de sens. Ta famille devient une base pour l'aventure.

## Ce que tu pourrais vivre
- Un foyer multiculturel ou ouvert aux différences
- Des racines qui t'encouragent à explorer plutôt qu'à te confiner
- Une philosophie familiale basée sur l'ouverture et la foi

## Conseils pour ce transit
- Crée un foyer qui célèbre l'aventure et l'ouverture
- Transmets des valeurs d'exploration à ta famille
- Fais de ta maison une porte vers le monde""",

    ('sagittarius', 5): """# ☊ Nœud Nord en Sagittaire – Maison V

**En une phrase :** L'univers t'invite à créer et aimer avec passion et soif d'aventure.

## L'énergie du moment
Le Nœud Nord en Sagittaire embrase ta maison de la joie. Ta créativité s'exprime dans la quête de sens et l'exploration. En amour, tu cherches un(e) partenaire d'aventure.

## Ce que tu pourrais vivre
- Une créativité inspirée par les voyages et les grandes questions
- Des amours qui sont des aventures d'expansion
- Un plaisir trouvé dans l'exploration et la découverte

## Conseils pour ce transit
- Crée avec la joie de l'explorateur
- Vis l'amour comme une grande aventure
- Trouve le plaisir dans ce qui élargit tes horizons""",

    ('sagittarius', 6): """# ☊ Nœud Nord en Sagittaire – Maison VI

**En une phrase :** Ta croissance karmique passe par un travail qui a du sens et qui élève.

## L'énergie du moment
Le Nœud Nord en Sagittaire élève ta maison du quotidien. Tu es invité(e) à trouver un travail aligné avec tes valeurs et ta quête de sens. Ta santé bénéficie d'une vision optimiste.

## Ce que tu pourrais vivre
- Un travail qui a une dimension philosophique ou éducative
- Des routines qui incluent croissance et exploration
- Une santé qui s'améliore par l'optimisme et la foi

## Conseils pour ce transit
- Trouve un travail qui correspond à tes idéaux
- Intègre l'apprentissage et l'exploration dans ton quotidien
- Garde une attitude optimiste envers ta santé""",

    ('sagittarius', 7): """# ☊ Nœud Nord en Sagittaire – Maison VII

**En une phrase :** Ta mission karmique t'invite à des relations qui élèvent et élargissent ta vision.

## L'énergie du moment
Le Nœud Nord en Sagittaire élargit ta maison des partenariats. Tu es appelé(e) à des relations qui t'aident à grandir, à voir plus loin et à explorer de nouveaux horizons ensemble.

## Ce que tu pourrais vivre
- Des relations qui élargissent ta vision du monde
- Un besoin de partenaires philosophes ou aventuriers
- Des associations basées sur des idéaux partagés

## Conseils pour ce transit
- Cherche des partenaires qui t'aident à grandir
- Partage tes aventures et tes quêtes avec tes proches
- Crée des relations basées sur une vision commune""",

    ('sagittarius', 8): """# ☊ Nœud Nord en Sagittaire – Maison VIII

**En une phrase :** Tu es appelé(e) à trouver du sens dans les transformations et les crises.

## L'énergie du moment
Le Nœud Nord en Sagittaire illumine ta maison des profondeurs. Ta croissance passe par la capacité à trouver une signification supérieure dans les épreuves, à voir la mort comme passage vers plus grand.

## Ce que tu pourrais vivre
- Une philosophie de vie qui intègre les transformations
- Une capacité à traverser les crises avec foi et optimisme
- Des questions profondes qui trouvent des réponses qui élèvent

## Conseils pour ce transit
- Trouve le sens caché dans tes transformations
- Garde la foi même dans les moments sombres
- Développe une philosophie qui inclut les mystères de l'existence""",

    ('sagittarius', 9): """# ☊ Nœud Nord en Sagittaire – Maison IX

**En une phrase :** L'univers t'invite à embrasser pleinement la quête de sens et l'exploration.

## L'énergie du moment
Le Nœud Nord en Sagittaire est chez lui dans ta maison de l'expansion. C'est un appel puissant à voyager, étudier, enseigner et développer ta propre philosophie de vie. L'aventure est ton chemin.

## Ce que tu pourrais vivre
- Des voyages qui transforment ta vision du monde
- Une quête spirituelle ou philosophique intense
- Un rôle d'enseignant ou de guide pour les autres

## Conseils pour ce transit
- Voyage autant que tu peux, physiquement et mentalement
- Développe et assume ta propre philosophie de vie
- Partage ta sagesse avec générosité""",

    ('sagittarius', 10): """# ☊ Nœud Nord en Sagittaire – Maison X

**En une phrase :** Ta mission de vie t'appelle à inspirer et élever par ta carrière.

## L'énergie du moment
Le Nœud Nord en Sagittaire couronne ta maison de la carrière. Tu es appelé(e) à une position qui inspire, enseigne ou élargit les horizons des autres. Ta réussite vient de ta vision.

## Ce que tu pourrais vivre
- Une carrière dans l'enseignement, l'édition, les voyages ou la philosophie
- Une reconnaissance pour ta vision et ton optimisme
- Un rôle de guide ou d'inspirateur dans ton domaine

## Conseils pour ce transit
- Oriente ta carrière vers ce qui t'inspire profondément
- Vise à élever et inspirer les autres par ton travail
- Construis ta réputation sur ta vision et tes idéaux""",

    ('sagittarius', 11): """# ☊ Nœud Nord en Sagittaire – Maison XI

**En une phrase :** Tu es invité(e) à porter des idéaux qui élèvent l'humanité.

## L'énergie du moment
Le Nœud Nord en Sagittaire élargit ta maison des amitiés et des idéaux. Ta mission est de rassembler autour de grandes visions, de créer des communautés d'explorateurs et de penseurs.

## Ce que tu pourrais vivre
- Des amitiés avec des philosophes, des voyageurs ou des visionnaires
- Des projets collectifs basés sur des idéaux élevés
- Un rôle d'inspirateur dans tes cercles sociaux

## Conseils pour ce transit
- Choisis des amis qui partagent ta soif d'exploration
- Porte des causes qui élèvent et élargissent les horizons
- Inspire tes groupes par ta vision et ton optimisme""",

    ('sagittarius', 12): """# ☊ Nœud Nord en Sagittaire – Maison XII

**En une phrase :** Ta croissance karmique passe par une quête spirituelle profonde et expansive.

## L'énergie du moment
Le Nœud Nord en Sagittaire illumine ta maison de l'invisible. Tu es appelé(e) à une spiritualité qui élargit ta conscience, qui te connecte à quelque chose de plus grand. Ta foi devient ton guide intérieur.

## Ce que tu pourrais vivre
- Une quête spirituelle qui ouvre des horizons insoupçonnés
- Des expériences mystiques liées à l'expansion de conscience
- Une foi profonde qui guide tes pas dans l'invisible

## Conseils pour ce transit
- Explore diverses traditions spirituelles avec ouverture
- Fais confiance à ta guidance intérieure
- Trouve le sens dans ce qui dépasse la compréhension ordinaire""",

    # ============== CAPRICORN ==============
    ('capricorn', 1): """# ☊ Nœud Nord en Capricorne – Maison I

**En une phrase :** L'univers t'invite à incarner la maturité, la responsabilité et l'ambition constructive.

## L'énergie du moment
Le Nœud Nord en Capricorne dans ta maison I t'appelle à devenir un pilier de force et de stabilité. Ta croissance passe par l'acceptation de tes responsabilités et la construction patiente de toi-même.

## Ce que tu pourrais vivre
- Un besoin de te définir par tes accomplissements et ta maturité
- Une redéfinition de ton image vers plus de sérieux et de structure
- Des situations qui exigent discipline et persévérance

## Conseils pour ce transit
- Assume pleinement tes responsabilités avec dignité
- Construis-toi étape par étape avec patience
- Incarne l'autorité sage et la maturité""",

    ('capricorn', 2): """# ☊ Nœud Nord en Capricorne – Maison II

**En une phrase :** Ta mission karmique te guide vers une richesse construite avec discipline et patience.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison des ressources. Tu es invité(e) à bâtir ta sécurité financière avec méthode, à valoriser ce qui dure et à développer une relation mature avec l'argent.

## Ce que tu pourrais vivre
- Une construction patiente de ta richesse matérielle
- Des revenus liés à la gestion, la structure ou l'autorité
- Un rapport à l'argent plus responsable et stratégique

## Conseils pour ce transit
- Construis ta richesse brique par brique
- Valorise les investissements à long terme
- Développe une discipline financière solide""",

    ('capricorn', 3): """# ☊ Nœud Nord en Capricorne – Maison III

**En une phrase :** Tu es appelé(e) à communiquer avec autorité, structure et responsabilité.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison de la communication. Ta croissance passe par une parole mesurée, des idées bien construites et une communication qui a du poids.

## Ce que tu pourrais vivre
- Une communication plus structurée et responsable
- Des apprentissages qui demandent discipline et persévérance
- Un rôle de référent ou d'autorité dans ton entourage

## Conseils pour ce transit
- Mesure tes paroles et donne-leur du poids
- Apprends avec discipline et méthode
- Deviens une source fiable d'information""",

    ('capricorn', 4): """# ☊ Nœud Nord en Capricorne – Maison IV

**En une phrase :** Ta mission karmique t'invite à devenir le pilier de ta famille et de ton foyer.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison des racines. Tu es appelé(e) à assumer des responsabilités familiales, à créer un foyer stable et à devenir une figure d'autorité bienveillante.

## Ce que tu pourrais vivre
- Un rôle de chef de famille ou de pilier domestique
- La construction d'un patrimoine familial durable
- Des responsabilités accrues envers tes proches

## Conseils pour ce transit
- Assume ton rôle de pilier familial avec dignité
- Construis un foyer qui dure pour les générations
- Deviens l'ancre de stabilité pour les tiens""",

    ('capricorn', 5): """# ☊ Nœud Nord en Capricorne – Maison V

**En une phrase :** L'univers t'invite à une créativité disciplinée et un amour mature.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison de la joie. Ta créativité s'épanouit dans la discipline et la maîtrise. En amour, tu cherches des relations matures et durables.

## Ce que tu pourrais vivre
- Une créativité qui demande travail et persévérance
- Des amours sérieuses, engagées et durables
- Un rapport au plaisir plus mature et responsable

## Conseils pour ce transit
- Maîtrise ton art par la pratique disciplinée
- Construis des amours basées sur l'engagement solide
- Trouve la joie dans l'accomplissement durable""",

    ('capricorn', 6): """# ☊ Nœud Nord en Capricorne – Maison VI

**En une phrase :** Ta croissance karmique passe par l'excellence professionnelle et la rigueur quotidienne.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison du quotidien. Tu es invité(e) à développer une éthique de travail impeccable, des routines solides et une approche professionnelle de ta santé.

## Ce que tu pourrais vivre
- Un travail où tu assumes des responsabilités croissantes
- Des routines structurées et efficaces
- Une santé qui s'améliore par la discipline

## Conseils pour ce transit
- Deviens irréprochable dans ton travail quotidien
- Structure tes routines avec rigueur
- Prends soin de ta santé avec la même discipline que ton travail""",

    ('capricorn', 7): """# ☊ Nœud Nord en Capricorne – Maison VII

**En une phrase :** Ta mission karmique t'invite à des partenariats structurés et durables.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison des partenariats. Tu es appelé(e) à des relations basées sur l'engagement, la responsabilité mutuelle et la construction commune.

## Ce que tu pourrais vivre
- Des relations qui se formalisent et se structurent
- Un besoin de partenaires fiables et responsables
- Des associations professionnelles stratégiques et durables

## Conseils pour ce transit
- Engage-toi sérieusement dans tes relations importantes
- Choisis des partenaires avec qui tu peux construire
- Crée des partenariats qui durent dans le temps""",

    ('capricorn', 8): """# ☊ Nœud Nord en Capricorne – Maison VIII

**En une phrase :** Tu es appelé(e) à gérer les crises et les ressources partagées avec maturité.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison des profondeurs. Ta croissance passe par une approche responsable des transformations, une gestion sage des ressources partagées et une maturité face à la mort.

## Ce que tu pourrais vivre
- Une capacité à gérer les crises avec calme et autorité
- Une organisation rigoureuse des finances partagées
- Une maturité face aux questions de vie et de mort

## Conseils pour ce transit
- Gère les crises avec le calme de l'expérience
- Structure les questions de ressources partagées
- Affronte les profondeurs avec sagesse et maturité""",

    ('capricorn', 9): """# ☊ Nœud Nord en Capricorne – Maison IX

**En une phrase :** L'univers t'invite à une sagesse construite sur l'expérience et la tradition.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison de l'expansion. Ta croissance philosophique passe par la sagesse traditionnelle, l'étude rigoureuse et l'expérience plutôt que les théories abstraites.

## Ce que tu pourrais vivre
- Une philosophie basée sur l'expérience et la tradition
- Des études exigeantes qui mènent à une vraie maîtrise
- Un enseignement qui fait autorité par son sérieux

## Conseils pour ce transit
- Fonde ta vision du monde sur l'expérience concrète
- Étudie avec rigueur et persévérance
- Enseigne ce que tu as véritablement maîtrisé""",

    ('capricorn', 10): """# ☊ Nœud Nord en Capricorne – Maison X

**En une phrase :** Ta mission de vie t'appelle au sommet de ta profession.

## L'énergie du moment
Le Nœud Nord en Capricorne est chez lui dans ta maison de la carrière. C'est un appel puissant à atteindre les sommets de ta profession, à assumer des responsabilités majeures et à bâtir un héritage durable.

## Ce que tu pourrais vivre
- Une ascension professionnelle majeure
- Des responsabilités importantes et une reconnaissance publique
- La construction d'un héritage qui te survivra

## Conseils pour ce transit
- Vise le sommet avec détermination et patience
- Assume les responsabilités que ta position implique
- Construis quelque chose qui durera après toi""",

    ('capricorn', 11): """# ☊ Nœud Nord en Capricorne – Maison XI

**En une phrase :** Tu es invité(e) à structurer et organiser les efforts collectifs.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison des amitiés et des idéaux. Ta mission est d'apporter organisation et structure aux causes collectives, d'être le pilier fiable de tes réseaux.

## Ce que tu pourrais vivre
- Un rôle d'organisateur ou de gestionnaire dans les groupes
- Des amitiés avec des personnes matures et fiables
- Des projets collectifs qui demandent structure et discipline

## Conseils pour ce transit
- Apporte structure et organisation aux causes que tu soutiens
- Choisis des amis qui partagent ton sens des responsabilités
- Construis des réseaux durables et fiables""",

    ('capricorn', 12): """# ☊ Nœud Nord en Capricorne – Maison XII

**En une phrase :** Ta croissance karmique passe par la discipline spirituelle et la solitude constructive.

## L'énergie du moment
Le Nœud Nord en Capricorne structure ta maison de l'invisible. Tu es appelé(e) à une spiritualité disciplinée, une méditation rigoureuse et un travail intérieur méthodique.

## Ce que tu pourrais vivre
- Des pratiques spirituelles structurées et régulières
- Une solitude qui devient source de force intérieure
- Un travail karmique méthodique et persévérant

## Conseils pour ce transit
- Structure tes pratiques spirituelles avec discipline
- Utilise la solitude pour te construire intérieurement
- Affronte ton karma avec patience et persévérance""",

    # ============== AQUARIUS ==============
    ('aquarius', 1): """# ☊ Nœud Nord en Verseau – Maison I

**En une phrase :** L'univers t'invite à incarner l'original, le visionnaire et le révolutionnaire.

## L'énergie du moment
Le Nœud Nord en Verseau dans ta maison I t'appelle à devenir pleinement unique, à assumer ta différence comme un don. Ta croissance passe par l'innovation, l'indépendance et la pensée libre.

## Ce que tu pourrais vivre
- Un besoin de te définir par ton unicité et ton originalité
- Une redéfinition de ton image vers plus d'authenticité
- Des situations qui t'invitent à sortir des normes

## Conseils pour ce transit
- Assume ta différence comme une force
- Libère-toi des attentes conventionnelles
- Deviens le visionnaire que tu es appelé(e) à être""",

    ('aquarius', 2): """# ☊ Nœud Nord en Verseau – Maison II

**En une phrase :** Ta mission karmique te guide vers une relation libre et innovante avec l'argent.

## L'énergie du moment
Le Nœud Nord en Verseau libère ta maison des ressources. Tu es invité(e) à développer des sources de revenus non conventionnelles, à valoriser l'innovation et à repenser ta relation aux possessions.

## Ce que tu pourrais vivre
- Des revenus liés à la technologie, l'innovation ou les réseaux
- Un rapport à l'argent plus détaché et original
- Une clarification de tes valeurs vers plus d'indépendance

## Conseils pour ce transit
- Explore des sources de revenus innovantes
- Libère-toi des modèles traditionnels de richesse
- Valorise ce qui te rend libre plutôt que ce qui t'attache""",

    ('aquarius', 3): """# ☊ Nœud Nord en Verseau – Maison III

**En une phrase :** Tu es appelé(e) à communiquer des idées révolutionnaires et avant-gardistes.

## L'énergie du moment
Le Nœud Nord en Verseau électrifie ta maison de la communication. Ta croissance passe par le partage d'idées originales, l'utilisation de nouvelles technologies et une pensée qui sort des sentiers battus.

## Ce que tu pourrais vivre
- Une communication innovante et non conventionnelle
- Des apprentissages liés à la technologie ou aux sciences
- Un rôle de transmetteur d'idées révolutionnaires

## Conseils pour ce transit
- Ose partager tes idées les plus originales
- Utilise les nouvelles technologies pour communiquer
- Pense et parle librement, hors des conventions""",

    ('aquarius', 4): """# ☊ Nœud Nord en Verseau – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un foyer libre et non conventionnel.

## L'énergie du moment
Le Nœud Nord en Verseau libère ta maison des racines. Tu es appelé(e) à créer un chez-toi qui respecte l'indépendance de chacun, qui accueille la différence et qui brise les moules familiaux.

## Ce que tu pourrais vivre
- Un foyer non conventionnel ou une famille choisie
- Une libération des schémas familiaux limitants
- Un besoin d'espace et de liberté dans ta vie privée

## Conseils pour ce transit
- Crée un foyer qui respecte l'unicité de chacun
- Libère-toi des traditions familiales qui t'étouffent
- Choisis ta famille autant que tu l'hérites""",

    ('aquarius', 5): """# ☊ Nœud Nord en Verseau – Maison V

**En une phrase :** L'univers t'invite à une créativité expérimentale et un amour libre.

## L'énergie du moment
Le Nœud Nord en Verseau électrifie ta maison de la joie. Ta créativité s'exprime dans l'avant-garde et l'expérimentation. En amour, tu cherches la liberté et les connexions intellectuelles.

## Ce que tu pourrais vivre
- Une créativité expérimentale et innovante
- Des amours non conventionnelles ou basées sur l'amitié
- Un plaisir trouvé dans l'originalité et la surprise

## Conseils pour ce transit
- Expérimente sans crainte dans ta créativité
- Vis l'amour comme une connexion entre esprits libres
- Trouve la joie dans ce qui est unique et différent""",

    ('aquarius', 6): """# ☊ Nœud Nord en Verseau – Maison VI

**En une phrase :** Ta croissance karmique passe par un travail innovant et des méthodes révolutionnaires.

## L'énergie du moment
Le Nœud Nord en Verseau modernise ta maison du quotidien. Tu es invité(e) à révolutionner ta façon de travailler, à adopter des méthodes innovantes et à repenser tes routines.

## Ce que tu pourrais vivre
- Un travail dans les technologies ou les domaines innovants
- Des routines non conventionnelles mais efficaces
- Une approche originale de la santé et du bien-être

## Conseils pour ce transit
- Innove dans ta façon de travailler
- Adopte des routines qui te libèrent plutôt qu'elles ne t'enferment
- Explore des approches alternatives pour ta santé""",

    ('aquarius', 7): """# ☊ Nœud Nord en Verseau – Maison VII

**En une phrase :** Ta mission karmique t'invite à des relations basées sur l'amitié et la liberté mutuelle.

## L'énergie du moment
Le Nœud Nord en Verseau libère ta maison des partenariats. Tu es appelé(e) à des relations qui respectent l'indépendance de chacun, basées sur l'amitié, le partage d'idéaux et la liberté.

## Ce que tu pourrais vivre
- Des relations qui laissent de l'espace à chacun
- Un besoin de partenaires intellectuellement stimulants
- Des associations basées sur des valeurs progressistes

## Conseils pour ce transit
- Crée des relations qui respectent ta liberté et celle de l'autre
- Choisis des partenaires qui sont d'abord des amis
- Base tes associations sur des idéaux partagés""",

    ('aquarius', 8): """# ☊ Nœud Nord en Verseau – Maison VIII

**En une phrase :** Tu es appelé(e) à aborder les transformations avec détachement et vision innovante.

## L'énergie du moment
Le Nœud Nord en Verseau allège ta maison des profondeurs. Ta croissance passe par une approche plus détachée et intellectuelle des crises, une vision progressiste de la transformation.

## Ce que tu pourrais vivre
- Une capacité à prendre du recul face aux crises
- Des transformations qui libèrent plutôt qu'elles n'attachent
- Une approche innovante des questions d'intimité et de pouvoir

## Conseils pour ce transit
- Garde une perspective large face aux transformations
- Libère-toi des attachements qui t'emprisonnent
- Innove dans ta façon de gérer le pouvoir et l'intimité""",

    ('aquarius', 9): """# ☊ Nœud Nord en Verseau – Maison IX

**En une phrase :** L'univers t'invite à développer une philosophie progressiste et universelle.

## L'énergie du moment
Le Nœud Nord en Verseau élargit ta maison de l'expansion. Ta croissance passe par des idées qui transcendent les frontières, une spiritualité universelle et une vision de l'avenir.

## Ce que tu pourrais vivre
- Une philosophie humaniste et progressiste
- Des voyages vers des lieux innovants ou des communautés alternatives
- Un enseignement qui promeut la liberté de pensée

## Conseils pour ce transit
- Développe une vision qui embrasse l'humanité entière
- Explore des philosophies non conventionnelles
- Enseigne des idées qui libèrent l'esprit""",

    ('aquarius', 10): """# ☊ Nœud Nord en Verseau – Maison X

**En une phrase :** Ta mission de vie t'appelle à innover et révolutionner ton domaine professionnel.

## L'énergie du moment
Le Nœud Nord en Verseau électrifie ta maison de la carrière. Tu es appelé(e) à une position qui change les règles, qui innove et qui sert une vision progressiste du monde.

## Ce que tu pourrais vivre
- Une carrière dans l'innovation, la technologie ou les causes humanitaires
- Une reconnaissance pour ton originalité et ta vision
- Un rôle de pionnier ou de réformateur dans ton domaine

## Conseils pour ce transit
- Oriente ta carrière vers l'innovation et le changement
- N'aie pas peur d'être différent professionnellement
- Utilise ta position pour faire avancer des causes progressistes""",

    ('aquarius', 11): """# ☊ Nœud Nord en Verseau – Maison XI

**En une phrase :** Tu es invité(e) à rassembler autour de visions d'avenir et de progrès.

## L'énergie du moment
Le Nœud Nord en Verseau est chez lui dans ta maison des amitiés et des idéaux. C'est un appel puissant à créer des communautés visionnaires, à porter des causes humanitaires et à connecter les esprits libres.

## Ce que tu pourrais vivre
- Des amitiés avec des originaux, des innovateurs, des visionnaires
- Un rôle central dans des mouvements progressistes
- Des projets collectifs qui imaginent un monde meilleur

## Conseils pour ce transit
- Rassemble des esprits libres autour de visions communes
- Porte des causes qui servent l'humanité
- Sois le catalyseur du changement dans tes réseaux""",

    ('aquarius', 12): """# ☊ Nœud Nord en Verseau – Maison XII

**En une phrase :** Ta croissance karmique passe par une spiritualité libre et universelle.

## L'énergie du moment
Le Nœud Nord en Verseau libère ta maison de l'invisible. Tu es appelé(e) à une spiritualité qui transcende les dogmes, qui connecte au cosmos et qui libère l'âme des limitations.

## Ce que tu pourrais vivre
- Une spiritualité non conventionnelle et universelle
- Des expériences de conscience élargie
- Une libération des schémas karmiques par le détachement

## Conseils pour ce transit
- Explore des voies spirituelles non conventionnelles
- Connecte-toi à la conscience universelle
- Libère-toi des croyances limitantes par la vision élargie""",

    # ============== PISCES ==============
    ('pisces', 1): """# ☊ Nœud Nord en Poissons – Maison I

**En une phrase :** L'univers t'invite à incarner la compassion, l'intuition et la connexion au divin.

## L'énergie du moment
Le Nœud Nord en Poissons dans ta maison I t'appelle à devenir un être de sensibilité, de créativité et de spiritualité. Ta croissance passe par le lâcher-prise, la foi et l'ouverture du cœur.

## Ce que tu pourrais vivre
- Un besoin de te définir par ta sensibilité et ta spiritualité
- Une redéfinition de ton image vers plus de douceur et de fluidité
- Des situations qui t'invitent à faire confiance à l'invisible

## Conseils pour ce transit
- Accepte ta nature sensible et intuitive comme une force
- Laisse-toi guider par ta foi et ton intuition
- Deviens un canal de compassion pour le monde""",

    ('pisces', 2): """# ☊ Nœud Nord en Poissons – Maison II

**En une phrase :** Ta mission karmique te guide vers une abondance qui vient du lâcher-prise et de la foi.

## L'énergie du moment
Le Nœud Nord en Poissons dissout ta maison des ressources. Tu es invité(e) à développer une relation fluide avec l'argent, à valoriser l'invisible et à faire confiance que tes besoins seront comblés.

## Ce que tu pourrais vivre
- Des revenus liés à l'art, la spiritualité ou l'aide aux autres
- Un détachement croissant des possessions matérielles
- Une abondance qui vient quand tu lâches prise

## Conseils pour ce transit
- Fais confiance que l'univers pourvoira à tes besoins
- Valorise les richesses invisibles : créativité, intuition, amour
- Donne généreusement et reçois avec gratitude""",

    ('pisces', 3): """# ☊ Nœud Nord en Poissons – Maison III

**En une phrase :** Tu es appelé(e) à communiquer par l'intuition, l'art et la poésie.

## L'énergie du moment
Le Nœud Nord en Poissons enchante ta maison de la communication. Ta croissance passe par une parole qui touche l'âme, une expression artistique et une communication intuitive.

## Ce que tu pourrais vivre
- Une communication plus poétique et inspirée
- Des apprentissages liés à l'art, la musique ou la spiritualité
- Une capacité accrue de capter les non-dits

## Conseils pour ce transit
- Exprime-toi à travers l'art, la poésie ou la musique
- Écoute avec ton intuition autant qu'avec tes oreilles
- Laisse ton imagination guider ta communication""",

    ('pisces', 4): """# ☊ Nœud Nord en Poissons – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un foyer spirituel et compassionnel.

## L'énergie du moment
Le Nœud Nord en Poissons spiritualise ta maison des racines. Tu es appelé(e) à créer un chez-toi qui soit un sanctuaire de paix, de créativité et de connexion au divin.

## Ce que tu pourrais vivre
- Un foyer qui devient un lieu de retraite spirituelle
- Une guérison des blessures familiales par le pardon et la compassion
- Un sentiment d'appartenance à une famille cosmique

## Conseils pour ce transit
- Transforme ton foyer en sanctuaire de paix
- Guéris les blessures familiales par la compassion
- Connecte tes racines à quelque chose de plus grand""",

    ('pisces', 5): """# ☊ Nœud Nord en Poissons – Maison V

**En une phrase :** L'univers t'invite à créer et aimer avec abandon et inspiration divine.

## L'énergie du moment
Le Nœud Nord en Poissons enchante ta maison de la joie. Ta créativité s'exprime comme un canal de l'inspiration divine. En amour, tu cherches l'âme sœur, la connexion transcendante.

## Ce que tu pourrais vivre
- Une créativité inspirée, presque médiumnique
- Des amours romantiques et spirituelles
- Un plaisir trouvé dans l'art, la musique et la beauté

## Conseils pour ce transit
- Laisse l'inspiration te traverser sans contrôle
- Vis l'amour comme une expérience spirituelle
- Trouve la joie dans la beauté et l'enchantement""",

    ('pisces', 6): """# ☊ Nœud Nord en Poissons – Maison VI

**En une phrase :** Ta croissance karmique passe par le service compassionnel et la guérison.

## L'énergie du moment
Le Nœud Nord en Poissons adoucit ta maison du quotidien. Tu es invité(e) à un travail de service, de guérison ou d'aide aux autres. Ta santé bénéficie d'approches holistiques et spirituelles.

## Ce que tu pourrais vivre
- Un travail dans l'aide, le soin ou les arts
- Des routines qui incluent méditation et pratiques spirituelles
- Une santé qui s'améliore par des approches alternatives

## Conseils pour ce transit
- Trouve un travail qui te permet de servir et guérir
- Intègre la spiritualité dans ton quotidien
- Prends soin de ton corps avec douceur et compassion""",

    ('pisces', 7): """# ☊ Nœud Nord en Poissons – Maison VII

**En une phrase :** Ta mission karmique t'invite à des relations basées sur l'âme et la compassion.

## L'énergie du moment
Le Nœud Nord en Poissons spiritualise ta maison des partenariats. Tu es appelé(e) à des relations d'âme, où la connexion dépasse l'ego et où la compassion guide les interactions.

## Ce que tu pourrais vivre
- Des relations qui touchent l'âme profondément
- Un besoin de partenaires spirituellement connectés
- Des associations basées sur la compassion et le service commun

## Conseils pour ce transit
- Cherche des connexions d'âme dans tes relations
- Pratique le pardon et la compassion avec tes partenaires
- Base tes relations sur quelque chose de plus grand que l'ego""",

    ('pisces', 8): """# ☊ Nœud Nord en Poissons – Maison VIII

**En une phrase :** Tu es appelé(e) à te transformer par le lâcher-prise et la dissolution de l'ego.

## L'énergie du moment
Le Nœud Nord en Poissons dissout ta maison des profondeurs. Ta croissance passe par l'acceptation du mystère, le lâcher-prise total et la transformation par l'abandon à quelque chose de plus grand.

## Ce que tu pourrais vivre
- Des transformations qui se font par le lâcher-prise
- Une intimité qui devient expérience mystique
- Une dissolution des peurs face à la mort et au changement

## Conseils pour ce transit
- Abandonne-toi aux transformations nécessaires
- Laisse mourir ce qui doit mourir sans résistance
- Trouve dans l'intimité une porte vers le transcendant""",

    ('pisces', 9): """# ☊ Nœud Nord en Poissons – Maison IX

**En une phrase :** L'univers t'invite à une spiritualité mystique et une foi sans frontières.

## L'énergie du moment
Le Nœud Nord en Poissons illumine ta maison de l'expansion. Ta croissance passe par l'ouverture à toutes les traditions spirituelles, la foi intuitive et la connexion au divin universel.

## Ce que tu pourrais vivre
- Une spiritualité qui transcende toutes les religions
- Des voyages vers des lieux saints ou inspirants
- Un enseignement qui vient de l'intuition et de l'inspiration

## Conseils pour ce transit
- Ouvre-toi à la sagesse de toutes les traditions
- Voyage vers des lieux qui nourrissent ton âme
- Enseigne par l'exemple et l'inspiration plutôt que par les mots""",

    ('pisces', 10): """# ☊ Nœud Nord en Poissons – Maison X

**En une phrase :** Ta mission de vie t'appelle à servir et inspirer à grande échelle.

## L'énergie du moment
Le Nœud Nord en Poissons illumine ta maison de la carrière. Tu es appelé(e) à une vocation qui sert, guérit ou inspire. Ta réussite vient de ta capacité à canaliser quelque chose de plus grand.

## Ce que tu pourrais vivre
- Une carrière dans l'art, la spiritualité ou l'aide aux autres
- Une reconnaissance pour ta compassion et ton inspiration
- Un rôle de guide spirituel ou de guérisseur public

## Conseils pour ce transit
- Oriente ta carrière vers le service et l'inspiration
- Laisse ta vocation te trouver plutôt que de la forcer
- Deviens un canal visible de compassion pour le monde""",

    ('pisces', 11): """# ☊ Nœud Nord en Poissons – Maison XI

**En une phrase :** Tu es invité(e) à créer des communautés compassionnelles et spirituellement connectées.

## L'énergie du moment
Le Nœud Nord en Poissons adoucit ta maison des amitiés et des idéaux. Ta mission est de rassembler des âmes dans un esprit de compassion, de service et de connexion spirituelle.

## Ce que tu pourrais vivre
- Des amitiés avec des artistes, des mystiques ou des guérisseurs
- Des projets collectifs de service ou d'aide humanitaire
- Un rôle d'unificateur spirituel dans tes cercles

## Conseils pour ce transit
- Crée des communautés basées sur la compassion
- Porte des causes qui servent les plus vulnérables
- Rassemble les gens autour de valeurs spirituelles""",

    ('pisces', 12): """# ☊ Nœud Nord en Poissons – Maison XII

**En une phrase :** Ta croissance karmique passe par la dissolution de l'ego et l'union mystique.

## L'énergie du moment
Le Nœud Nord en Poissons est chez lui dans ta maison de l'invisible. C'est un appel puissant à la vie contemplative, à la dissolution des barrières entre toi et le divin, à l'union mystique.

## Ce que tu pourrais vivre
- Des expériences mystiques profondes et transformatrices
- Une dissolution progressive de l'ego séparé
- Une connexion directe avec la source de toute chose

## Conseils pour ce transit
- Consacre du temps à la méditation et à la contemplation
- Laisse les frontières de ton ego se dissoudre
- Vis l'unité avec tout ce qui est""",
}


async def insert_interpretations():
    """Insert North Node transit interpretations for Sagittarius, Capricorn, Aquarius, Pisces"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_NORTH_NODE_INTERPRETATIONS.items():
            # Check if exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_north_node',
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
                subject='transit_north_node',
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
        print(f"✅ Transit North Node (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
