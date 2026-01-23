#!/usr/bin/env python3
"""
Insert transit_lilith interpretations V2 for Sagittarius, Capricorn, Aquarius, Pisces (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_LILITH_INTERPRETATIONS = {
    # ============== SAGITTARIUS (Sagittaire) ==============
    ('sagittarius', 1): """# ⚸ Transit de Lilith en Sagittaire — Maison 1

**En une phrase :** Ta soif de liberté et de vérité devient impossible à contenir.

## L'énergie du moment
Lilith en Sagittaire dans ta maison 1 te pousse à revendiquer ta liberté totale. Tu refuses les carcans, les conventions, tout ce qui limite ton expansion. Ta présence devient plus sauvage, plus directe, parfois provocante dans sa quête de vérité.

## Ce que tu pourrais vivre
- Un besoin irrépressible de liberté dans ta façon d'être
- Une franchise qui peut choquer mais qui libère
- Un attrait pour les aventures et les expériences qui élargissent

## Conseils pour ce transit
- Ta liberté ne doit pas se faire au détriment de ta responsabilité
- La vérité peut se dire sans blesser
- L'expansion commence par l'acceptation de qui tu es""",

    ('sagittarius', 2): """# ⚸ Transit de Lilith en Sagittaire — Maison 2

**En une phrase :** Tes ressources doivent soutenir ta liberté et tes aventures.

## L'énergie du moment
Lilith traverse ta maison des ressources avec l'appétit d'expansion du Sagittaire. Tu veux de l'argent pour la liberté qu'il offre, pas pour la sécurité. Tu peux être généreux·se à l'excès ou prendre des risques financiers pour des aventures.

## Ce que tu pourrais vivre
- Un rapport à l'argent qui privilégie l'aventure sur la sécurité
- Des dépenses impulsives pour des voyages ou des expériences
- Un questionnement sur ce qui a vraiment de la valeur dans la vie

## Conseils pour ce transit
- La liberté financière demande un minimum de structure
- L'aventure n'a pas besoin d'être coûteuse
- Tes vraies richesses sont tes expériences et ta sagesse""",

    ('sagittarius', 3): """# ⚸ Transit de Lilith en Sagittaire — Maison 3

**En une phrase :** Ta parole devient un vecteur de vérité et d'expansion.

## L'énergie du moment
Lilith traverse ta maison de la communication avec la franchise du Sagittaire. Tu dis ce que tu penses sans filtre, tu partages ta vision avec passion. Tes paroles peuvent inspirer ou offenser selon l'auditoire. Tu veux des échanges qui élèvent.

## Ce que tu pourrais vivre
- Une communication directe, enthousiaste, parfois excessive
- Des débats passionnés sur des sujets philosophiques
- Une soif d'apprendre et de partager des connaissances

## Conseils pour ce transit
- L'enthousiasme est contagieux : partage-le
- La vérité peut être dite avec bienveillance
- Tes idées ont besoin de trouver leur public""",

    ('sagittarius', 4): """# ⚸ Transit de Lilith en Sagittaire — Maison 4

**En une phrase :** Ton foyer doit être un tremplin pour l'aventure, pas une prison.

## L'énergie du moment
Lilith secoue ta maison 4 avec le besoin de liberté du Sagittaire. Tu peux te sentir à l'étroit chez toi ou dans ta famille si ils limitent ton expansion. Tu veux un foyer qui t'inspire, qui t'ouvre des horizons, pas qui te confine.

## Ce que tu pourrais vivre
- Un sentiment d'étouffement dans ton espace ou ta famille
- Un désir de voyage qui entre en conflit avec les attaches
- Des questionnements sur le sens de tes racines

## Conseils pour ce transit
- Le foyer peut être une base d'exploration, pas une cage
- Tes racines peuvent t'enraciner ET te permettre de voyager
- La famille peut évoluer avec toi si tu communiques""",

    ('sagittarius', 5): """# ⚸ Transit de Lilith en Sagittaire — Maison 5

**En une phrase :** Tes amours et ta créativité prennent une dimension d'aventure et de quête.

## L'énergie du moment
Lilith traverse ta maison 5 avec l'enthousiasme du Sagittaire. Tu veux des amours qui sont des aventures, une créativité qui explore de nouveaux territoires. Tu refuses l'ennui dans les plaisirs, tu veux que la vie soit une épopée.

## Ce que tu pourrais vivre
- Des relations amoureuses qui ressemblent à des aventures
- Une créativité qui explore des thèmes philosophiques ou spirituels
- Un besoin de liberté dans les jeux et les plaisirs

## Conseils pour ce transit
- L'amour-aventure peut aussi être profond et engagé
- Ta créativité peut porter ta vision du monde
- La liberté dans le plaisir n'exclut pas le respect""",

    ('sagittarius', 6): """# ⚸ Transit de Lilith en Sagittaire — Maison 6

**En une phrase :** Ton quotidien doit avoir du sens et t'élever, sinon tu t'évades.

## L'énergie du moment
Lilith traverse ta maison 6 avec le besoin de sens du Sagittaire. Le travail routinier sans vision te pèse énormément. Tu veux que ton quotidien soit une contribution à quelque chose de plus grand. La santé passe par le mouvement et l'expansion.

## Ce que tu pourrais vivre
- Une intolérance aux routines qui n'ont pas de sens
- Un besoin de mouvement et de variété au quotidien
- Des tensions si ton travail ne correspond pas à tes valeurs

## Conseils pour ce transit
- Même les petites tâches peuvent servir une grande vision
- Le corps a besoin de mouvement et d'espace
- Ton quotidien peut être une aventure si tu le vois ainsi""",

    ('sagittarius', 7): """# ⚸ Transit de Lilith en Sagittaire — Maison 7

**En une phrase :** Tes relations doivent te permettre de grandir et d'explorer.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec l'expansion du Sagittaire. Tu veux des relations qui t'élèvent, qui t'ouvrent des horizons, qui t'inspirent. Les partenaires qui te limitent ou t'étouffent deviennent insupportables.

## Ce que tu pourrais vivre
- Une attraction pour des partenaires qui t'inspirent et t'élèvent
- Des tensions si les relations limitent ta liberté
- Un besoin d'espace et d'indépendance dans le couple

## Conseils pour ce transit
- Les meilleures relations sont des partenariats d'aventure
- La liberté dans le couple demande confiance et communication
- Tu peux grandir ensemble sans te perdre""",

    ('sagittarius', 8): """# ⚸ Transit de Lilith en Sagittaire — Maison 8

**En une phrase :** Tes transformations passent par des expériences qui élargissent ta conscience.

## L'énergie du moment
Lilith traverse ta maison 8 avec l'expansivité du Sagittaire. Tes crises transformatrices ouvrent de nouveaux horizons. La sexualité peut devenir une exploration spirituelle. Tu cherches le sens dans les expériences profondes.

## Ce que tu pourrais vivre
- Des transformations qui élargissent ta vision du monde
- Une exploration de la sexualité tantrique ou spirituelle
- Des questions profondes sur le sens de la vie et de la mort

## Conseils pour ce transit
- Les crises peuvent être des portes vers plus grand
- L'intimité peut être un chemin d'expansion
- Les tabous explorés avec conscience peuvent libérer""",

    ('sagittarius', 9): """# ⚸ Transit de Lilith en Sagittaire — Maison 9

**En une phrase :** Ta quête de vérité devient absolue et ne tolère aucun compromis.

## L'énergie du moment
Lilith est puissante en Sagittaire dans la maison 9, son domaine naturel. Ta soif de vérité, de sens, d'expansion devient totale. Tu peux remettre en question toutes les autorités spirituelles ou intellectuelles. Tu veux ta propre vérité.

## Ce que tu pourrais vivre
- Une remise en question profonde de toutes les croyances reçues
- Un désir intense de voyages initiatiques ou de rencontres élargissantes
- Des conflits avec des enseignants ou des dogmes qui te limitent

## Conseils pour ce transit
- La quête de vérité est noble, le dogmatisme est un piège
- Ta propre expérience est ton meilleur professeur
- La sagesse inclut le doute et l'humilité""",

    ('sagittarius', 10): """# ⚸ Transit de Lilith en Sagittaire — Maison 10

**En une phrase :** Ta carrière doit incarner ta vision et ta quête de sens.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'ambition visionnaire du Sagittaire. Tu veux une carrière qui porte un message, qui inspire, qui donne du sens. Les jobs sans vision ou sans éthique deviennent impossibles à supporter.

## Ce que tu pourrais vivre
- Un besoin de carrière alignée avec tes valeurs et ta vision
- Des tensions avec des autorités qui ne partagent pas tes idéaux
- Un désir de métiers liés à l'enseignement, au voyage, à la quête de sens

## Conseils pour ce transit
- Ta carrière peut être un véhicule pour ta vision
- L'idéalisme professionnel peut coexister avec le réalisme
- Ta réussite passe par l'alignement avec tes valeurs""",

    ('sagittarius', 11): """# ⚸ Transit de Lilith en Sagittaire — Maison 11

**En une phrase :** Tes cercles sociaux doivent partager ta soif de liberté et de sens.

## L'énergie du moment
Lilith traverse ta maison 11 avec l'esprit de communauté du Sagittaire. Tu veux des amitiés qui partagent ta vision, des groupes qui portent des idéaux élevés. Les cercles conformistes ou limitants ne t'intéressent plus.

## Ce que tu pourrais vivre
- Un tri dans tes amitiés basé sur les valeurs partagées
- Un attrait pour des communautés visionnaires ou alternatives
- Des engagements dans des causes qui te tiennent à cœur

## Conseils pour ce transit
- Les amitiés de vision sont précieuses et rares
- Les idéaux partagés créent des liens forts
- Ta contribution aux causes qui te passionnent fait une différence""",

    ('sagittarius', 12): """# ⚸ Transit de Lilith en Sagittaire — Maison 12

**En une phrase :** Tes croyances inconscientes et tes fuites spirituelles sont révélées.

## L'énergie du moment
Lilith en Sagittaire dans ta maison 12 éclaire tes ombres spirituelles. Des croyances limitantes, des fuites dans la quête de sens, des excès cachés liés à la recherche de liberté peuvent émerger. C'est un temps pour guérir ta relation à la transcendance.

## Ce que tu pourrais vivre
- Des prises de conscience sur tes croyances inconscientes
- Une confrontation avec tes tendances à fuir dans l'idéal
- Des expériences spirituelles profondes ou des doutes profonds

## Conseils pour ce transit
- La vraie liberté inclut l'acceptation des limites
- Les croyances inconscientes peuvent être reprogrammées
- La spiritualité est un chemin, pas une fuite""",

    # ============== CAPRICORN (Capricorne) ==============
    ('capricorn', 1): """# ⚸ Transit de Lilith en Capricorne — Maison 1

**En une phrase :** Ton ambition et ton autorité personnelle s'affirment avec force.

## L'énergie du moment
Lilith en Capricorne dans ta maison 1 éveille une ambition intense et un besoin d'être pris·e au sérieux. Tu dégages une autorité naturelle qui peut impressionner ou intimider. Tu refuses la légèreté et les situations qui ne te respectent pas.

## Ce que tu pourrais vivre
- Une présence plus grave, plus autoritaire, plus ambitieuse
- Un besoin de contrôle sur ton image et ta vie
- Des réactions de respect ou de défi face à ton autorité

## Conseils pour ce transit
- L'autorité vraie n'a pas besoin de dominer
- Ton ambition est légitime : canalise-la avec sagesse
- La gravité peut coexister avec la joie""",

    ('capricorn', 2): """# ⚸ Transit de Lilith en Capricorne — Maison 2

**En une phrase :** Tes ressources sont construites avec stratégie et ambition à long terme.

## L'énergie du moment
Lilith traverse ta maison des ressources avec la rigueur du Capricorne. Tu veux construire une sécurité durable, pas des gains éphémères. Ton rapport à l'argent devient plus stratégique, parfois plus austère. Tu peux être très exigeant·e sur ce qui a vraiment de la valeur.

## Ce que tu pourrais vivre
- Une approche plus structurée de tes finances
- Un questionnement sur ce qui construit une vraie valeur
- Des frustrations si les résultats ne viennent pas assez vite

## Conseils pour ce transit
- La construction solide demande du temps
- L'austérité n'est pas toujours nécessaire
- Tes fondations financières peuvent être solides ET te permettre de vivre""",

    ('capricorn', 3): """# ⚸ Transit de Lilith en Capricorne — Maison 3

**En une phrase :** Ta communication devient plus stratégique et plus mesurée.

## L'énergie du moment
Lilith traverse ta maison de la communication avec la retenue du Capricorne. Tu pèses tes mots, tu communiques de façon plus structurée, parfois plus froide. Tu peux avoir du mal à exprimer tes émotions mais une grande clarté dans tes idées.

## Ce que tu pourrais vivre
- Une communication plus réfléchie et stratégique
- Une difficulté à exprimer la légèreté ou l'émotion
- Un attrait pour des sujets sérieux et structurés

## Conseils pour ce transit
- La clarté est une force, mais l'émotion aussi communique
- Ta parole peut avoir du poids si tu la mesures
- L'humour peut coexister avec le sérieux""",

    ('capricorn', 4): """# ⚸ Transit de Lilith en Capricorne — Maison 4

**En une phrase :** Ton foyer doit être un bastion solide que tu contrôles.

## L'énergie du moment
Lilith secoue ta maison 4 avec la structure du Capricorne. Tu veux un foyer qui soit une forteresse, un espace que tu maîtrises. Des enjeux de contrôle peuvent émerger dans la famille. Tu peux assumer un rôle d'autorité dans le clan.

## Ce que tu pourrais vivre
- Un besoin de structure et de contrôle dans ton espace
- Des tensions autour de l'autorité familiale
- Un rapport aux origines marqué par le sens du devoir

## Conseils pour ce transit
- La maison peut être stable sans être rigide
- L'autorité familiale fonctionne mieux quand elle est bienveillante
- Les traditions ont leur valeur si elles évoluent""",

    ('capricorn', 5): """# ⚸ Transit de Lilith en Capricorne — Maison 5

**En une phrase :** Tes plaisirs et ta créativité passent par la maîtrise et la structure.

## L'énergie du moment
Lilith traverse ta maison 5 avec la discipline du Capricorne. Tes amours peuvent être plus calculés ou plus contrôlés. Ta créativité s'exprime dans des formes structurées, peut-être plus austères. Tu peux avoir du mal à te laisser aller au plaisir pur.

## Ce que tu pourrais vivre
- Une créativité disciplinée qui vise l'excellence
- Des relations amoureuses plus réservées ou stratégiques
- Une difficulté à lâcher prise dans le plaisir

## Conseils pour ce transit
- La maîtrise peut servir la créativité
- Le plaisir n'a pas besoin d'être productif
- L'amour peut être responsable ET passionné""",

    ('capricorn', 6): """# ⚸ Transit de Lilith en Capricorne — Maison 6

**En une phrase :** Ton quotidien est organisé avec rigueur et ambition.

## L'énergie du moment
Lilith traverse ta maison 6 avec l'exigence du Capricorne. Tu veux un quotidien productif, un travail qui construit quelque chose de durable. Tu peux être très dur·e avec toi-même dans tes routines. La santé passe par la discipline.

## Ce que tu pourrais vivre
- Des routines très structurées, parfois austères
- Une exigence élevée envers toi-même au travail
- Une approche disciplinée de la santé

## Conseils pour ce transit
- La discipline est une force si elle ne devient pas rigidité
- Le repos fait partie du travail
- Le corps mérite de la douceur autant que de la discipline""",

    ('capricorn', 7): """# ⚸ Transit de Lilith en Capricorne — Maison 7

**En une phrase :** Tes relations sont abordées avec sérieux et engagement à long terme.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec la maturité du Capricorne. Tu veux des relations sérieuses, qui construisent quelque chose, qui durent. Les aventures légères ne t'intéressent plus. Tu peux être exigeant·e ou te montrer froid·e.

## Ce que tu pourrais vivre
- Une recherche de partenaires matures et fiables
- Des enjeux de contrôle ou de pouvoir dans le couple
- Un engagement profond mais peut-être rigide

## Conseils pour ce transit
- Les relations durables se construisent avec patience
- La responsabilité partagée est la base d'un couple solide
- Le sérieux peut coexister avec la tendresse""",

    ('capricorn', 8): """# ⚸ Transit de Lilith en Capricorne — Maison 8

**En une phrase :** Tes transformations sont structurées et contrôlées.

## L'énergie du moment
Lilith traverse ta maison 8 avec la maîtrise du Capricorne. Tu abordes les crises et les transformations avec stratégie. Tu veux contrôler les processus de changement, ce qui peut aider ou freiner. Les questions de pouvoir et d'héritage sont centrales.

## Ce que tu pourrais vivre
- Une approche stratégique des transformations
- Des enjeux de pouvoir et de contrôle dans l'intimité
- Des questions d'héritage ou de ressources partagées

## Conseils pour ce transit
- Les transformations ont leur propre timing
- Le contrôle excessif peut bloquer les processus naturels
- Le pouvoir vrai vient de l'intérieur""",

    ('capricorn', 9): """# ⚸ Transit de Lilith en Capricorne — Maison 9

**En une phrase :** Ta quête de sens passe par la structure et la tradition.

## L'énergie du moment
Lilith traverse ta maison 9 avec le conservatisme du Capricorne. Tu peux être attiré·e par des traditions anciennes, des structures spirituelles établies, ou au contraire les remettre en question. Tu cherches une sagesse qui a fait ses preuves.

## Ce que tu pourrais vivre
- Un attrait pour des traditions ou des structures spirituelles
- Une remise en question des autorités intellectuelles ou spirituelles
- Un apprentissage qui passe par la discipline et la structure

## Conseils pour ce transit
- Les traditions portent une sagesse ancienne
- La structure peut soutenir l'expansion spirituelle
- La vraie autorité spirituelle ne s'impose pas""",

    ('capricorn', 10): """# ⚸ Transit de Lilith en Capricorne — Maison 10

**En une phrase :** Ton ambition professionnelle devient intense et implacable.

## L'énergie du moment
Lilith est très puissante en Capricorne dans la maison 10, son domaine. Ton ambition est à son maximum, tu veux atteindre les sommets. Les enjeux de pouvoir professionnels sont intenses. Tu peux impressionner ou te faire des ennemis.

## Ce que tu pourrais vivre
- Une ambition professionnelle dévorante
- Des enjeux de pouvoir intenses dans ta carrière
- Une image publique d'autorité et de compétence

## Conseils pour ce transit
- L'ambition légitime peut devenir obsession destructrice
- Le pouvoir vrai n'a pas besoin de dominer
- Ta réussite peut inspirer plutôt qu'écraser""",

    ('capricorn', 11): """# ⚸ Transit de Lilith en Capricorne — Maison 11

**En une phrase :** Tes cercles sociaux sont triés par leur sérieux et leur utilité.

## L'énergie du moment
Lilith traverse ta maison 11 avec le pragmatisme du Capricorne. Tu veux des amitiés qui servent à quelque chose, des réseaux utiles à tes objectifs. Les relations légères ou sans substance ne t'intéressent plus.

## Ce que tu pourrais vivre
- Un tri dans tes amitiés basé sur la valeur ajoutée
- Un attrait pour des groupes professionnels ou stratégiques
- Un rôle d'autorité dans les collectifs

## Conseils pour ce transit
- Les vraies amitiés dépassent l'utilité
- Les réseaux peuvent être stratégiques ET authentiques
- La contribution aux groupes construit ta réputation""",

    ('capricorn', 12): """# ⚸ Transit de Lilith en Capricorne — Maison 12

**En une phrase :** Tes ombres autour du contrôle et de l'ambition émergent de l'inconscient.

## L'énergie du moment
Lilith en Capricorne dans ta maison 12 révèle les origines de ton besoin de contrôle. Des peurs profondes d'échec, des ambitions refoulées, des enjeux de pouvoir inconscients peuvent remonter. C'est un temps pour guérir ta relation à l'autorité.

## Ce que tu pourrais vivre
- Des confrontations avec tes peurs d'échec ou d'impuissance
- Des prises de conscience sur tes schémas de contrôle
- Un travail profond sur ta relation à l'autorité intérieure

## Conseils pour ce transit
- Le contrôle excessif vient souvent de la peur
- L'autorité intérieure n'a pas besoin de contrôler l'extérieur
- Les ambitions refoulées méritent d'être reconnues""",

    # ============== AQUARIUS (Verseau) ==============
    ('aquarius', 1): """# ⚸ Transit de Lilith en Verseau — Maison 1

**En une phrase :** Ton individualité et ton côté rebelle s'expriment sans filtre.

## L'énergie du moment
Lilith en Verseau dans ta maison 1 libère ton côté le plus original et rebelle. Tu refuses de te conformer, de suivre les normes, de correspondre aux attentes. Ta présence devient électrique, provocante, magnétique pour ceux qui valorisent l'authenticité.

## Ce que tu pourrais vivre
- Une affirmation radicale de ton unicité
- Des réactions fortes des autres face à ton originalité
- Un rejet des normes et des conventions sociales

## Conseils pour ce transit
- Ton unicité est ta force, pas un défaut à cacher
- La rébellion pour la rébellion n'a pas de sens
- Tu peux être unique ET connecté·e aux autres""",

    ('aquarius', 2): """# ⚸ Transit de Lilith en Verseau — Maison 2

**En une phrase :** Tes ressources suivent des chemins non conventionnels.

## L'énergie du moment
Lilith traverse ta maison des ressources avec l'originalité du Verseau. Tu peux gagner de l'argent de façons inhabituelles ou avoir un rapport à l'argent qui défie les conventions. La vraie richesse est pour toi dans la liberté et l'innovation.

## Ce que tu pourrais vivre
- Des sources de revenus atypiques ou innovantes
- Un détachement des conventions sur l'argent et la réussite
- Des fluctuations financières liées à ton anticonformisme

## Conseils pour ce transit
- L'innovation peut être lucrative
- La liberté financière peut prendre des formes inattendues
- La vraie valeur est dans ce que tu apportes d'unique""",

    ('aquarius', 3): """# ⚸ Transit de Lilith en Verseau — Maison 3

**En une phrase :** Ta communication devient avant-gardiste et iconoclaste.

## L'énergie du moment
Lilith traverse ta maison de la communication avec l'originalité du Verseau. Tes idées sont avant-gardistes, parfois provocantes, toujours différentes. Tu peux choquer par tes opinions ou inspirer par ta vision. Les échanges conventionnels t'ennuient.

## Ce que tu pourrais vivre
- Une communication originale qui détonne
- Des idées en avance sur leur temps
- Des tensions avec ceux qui pensent de façon conventionnelle

## Conseils pour ce transit
- Tes idées originales méritent d'être partagées
- L'avant-garde peut être visionnaire ou simplement bizarre
- Trouve les publics qui peuvent entendre ta différence""",

    ('aquarius', 4): """# ⚸ Transit de Lilith en Verseau — Maison 4

**En une phrase :** Ton foyer doit être un espace de liberté et d'expérimentation.

## L'énergie du moment
Lilith secoue ta maison 4 avec le besoin de liberté du Verseau. Tu veux un espace qui te permet d'être toi-même sans jugement. Les traditions familiales peuvent être remises en question. Tu peux créer une famille choisie ou un mode de vie alternatif.

## Ce que tu pourrais vivre
- Un besoin de liberté et d'originalité dans ton espace
- Une remise en question des traditions et attentes familiales
- La création d'un foyer non conventionnel

## Conseils pour ce transit
- Ton foyer peut être aussi unique que toi
- Les racines peuvent évoluer sans être reniées
- La famille choisie est aussi valide que la famille biologique""",

    ('aquarius', 5): """# ⚸ Transit de Lilith en Verseau — Maison 5

**En une phrase :** Tes amours et ta créativité prennent des formes avant-gardistes.

## L'énergie du moment
Lilith traverse ta maison 5 avec l'originalité du Verseau. Tes relations amoureuses peuvent être non conventionnelles, tes créations innovantes et provocantes. Tu refuses les formes prévisibles de l'amour et de l'art.

## Ce que tu pourrais vivre
- Des relations amoureuses hors normes ou expérimentales
- Une créativité qui explore des territoires nouveaux
- Un besoin de liberté dans les plaisirs et les jeux

## Conseils pour ce transit
- L'amour peut prendre des formes multiples et valides
- Ta créativité la plus audacieuse est souvent la meilleure
- La liberté dans le plaisir demande responsabilité et respect""",

    ('aquarius', 6): """# ⚸ Transit de Lilith en Verseau — Maison 6

**En une phrase :** Ton quotidien doit permettre ta liberté et ton originalité.

## L'énergie du moment
Lilith traverse ta maison 6 avec l'anticonformisme du Verseau. Tu ne supportes plus les environnements de travail rigides ou conventionnels. Tu veux innover dans ton quotidien, expérimenter de nouvelles façons de travailler et de prendre soin de toi.

## Ce que tu pourrais vivre
- Une intolérance aux routines et aux environnements conventionnels
- Des innovations dans ta façon de travailler ou de prendre soin de ta santé
- Des tensions avec des collègues ou des systèmes trop rigides

## Conseils pour ce transit
- L'innovation peut transformer le quotidien
- La santé peut passer par des approches alternatives
- Ta différence au travail peut être ta contribution unique""",

    ('aquarius', 7): """# ⚸ Transit de Lilith en Verseau — Maison 7

**En une phrase :** Tes relations défient les conventions et les attentes sociales.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec la liberté du Verseau. Tu veux des relations qui respectent ton individualité, qui n'essaient pas de te conformer. Les modèles relationnels conventionnels peuvent te sembler étouffants.

## Ce que tu pourrais vivre
- Une attraction pour des partenaires originaux ou atypiques
- Un besoin de liberté et d'espace dans les relations
- Des conflits si le partenaire veut te "normaliser"

## Conseils pour ce transit
- Les relations qui honorent ton unicité sont les plus saines
- La liberté dans le couple demande confiance mutuelle
- Tu peux être engagé·e ET libre""",

    ('aquarius', 8): """# ⚸ Transit de Lilith en Verseau — Maison 8

**En une phrase :** Tes transformations passent par des voies non conventionnelles.

## L'énergie du moment
Lilith traverse ta maison 8 avec l'originalité du Verseau. Les crises transformatrices peuvent te libérer de tout ce qui est conventionnel en toi. La sexualité peut devenir expérimentale. Tu explores les profondeurs avec un regard détaché et innovant.

## Ce que tu pourrais vivre
- Des transformations qui te rendent plus libre et original
- Une approche de la sexualité qui défie les tabous sociaux
- Un détachement émotionnel qui facilite ou complique les transformations

## Conseils pour ce transit
- Les transformations radicales peuvent libérer
- L'expérimentation sexuelle demande consentement et respect
- Le détachement n'est pas la même chose que la déconnexion""",

    ('aquarius', 9): """# ⚸ Transit de Lilith en Verseau — Maison 9

**En une phrase :** Ta quête de sens passe par des chemins radicalement originaux.

## L'énergie du moment
Lilith traverse ta maison 9 avec l'iconoclasme du Verseau. Tu remets en question toutes les croyances établies, tu cherches ta propre vérité. Tu peux être attiré·e par des philosophies alternatives ou des visions du monde futuristes.

## Ce que tu pourrais vivre
- Un rejet des dogmes et des autorités intellectuelles
- Un attrait pour des idées radicales ou futuristes
- Des conflits avec ceux qui défendent les traditions

## Conseils pour ce transit
- Ta vision originale du monde a de la valeur
- Le rejet systématique peut être aussi limitant que le conformisme
- L'innovation intellectuelle peut inspirer le changement""",

    ('aquarius', 10): """# ⚸ Transit de Lilith en Verseau — Maison 10

**En une phrase :** Ta carrière doit incarner ton originalité et contribuer au changement.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'innovation du Verseau. Tu veux une carrière qui fait une différence, qui innove, qui change les règles du jeu. Les parcours conventionnels ne t'intéressent pas. Tu peux devenir un pionnier dans ton domaine.

## Ce que tu pourrais vivre
- Une carrière non conventionnelle ou innovante
- Des tensions avec des hiérarchies ou des systèmes rigides
- Une réputation d'original, de rebelle, ou de visionnaire

## Conseils pour ce transit
- Ta carrière peut être un véhicule de changement
- L'innovation professionnelle demande aussi du pragmatisme
- Ta différence peut devenir ta marque distinctive""",

    ('aquarius', 11): """# ⚸ Transit de Lilith en Verseau — Maison 11

**En une phrase :** Tes cercles sociaux et tes idéaux deviennent radicaux et avant-gardistes.

## L'énergie du moment
Lilith est très puissante en Verseau dans la maison 11, son domaine naturel. Tu veux des amitiés authentiques avec des personnes originales. Tu t'engages pour des causes progressistes ou révolutionnaires. Les groupes conventionnels ne t'intéressent plus.

## Ce que tu pourrais vivre
- Un tri radical dans tes amitiés et tes cercles
- Un engagement pour des causes avant-gardistes
- Un rôle de catalyseur de changement dans les groupes

## Conseils pour ce transit
- Les amitiés authentiques honorent la différence de chacun
- Les idéaux révolutionnaires peuvent changer le monde
- Le collectif a besoin de ta vision unique""",

    ('aquarius', 12): """# ⚸ Transit de Lilith en Verseau — Maison 12

**En une phrase :** Ton besoin de liberté a des racines profondes dans des blessures d'exclusion.

## L'énergie du moment
Lilith en Verseau dans ta maison 12 révèle les origines de ton besoin d'être différent. Des blessures d'exclusion, des moments où ta différence a été rejetée, peuvent remonter. C'est un temps pour guérir ton rapport à l'appartenance et à la liberté.

## Ce que tu pourrais vivre
- Des prises de conscience sur tes peurs d'exclusion ou de conformité
- Un travail sur les origines de ton besoin de rébellion
- Des expériences spirituelles liées à la connexion collective

## Conseils pour ce transit
- Tu peux être unique ET appartenir
- La vraie liberté n'est pas une réaction contre l'exclusion
- La guérison passe par l'acceptation de tous tes aspects""",

    # ============== PISCES (Poissons) ==============
    ('pisces', 1): """# ⚸ Transit de Lilith en Poissons — Maison 1

**En une phrase :** Ta présence devient mystérieuse, insaisissable et profondément intuitive.

## L'énergie du moment
Lilith en Poissons dans ta maison 1 dissout les contours de ton identité. Tu deviens plus fluide, plus difficile à cerner, plus sensible aux énergies environnantes. Ta présence peut être hypnotique ou déroutante. Tu absorbes beaucoup et tu dois apprendre à te protéger.

## Ce que tu pourrais vivre
- Une présence plus éthérée et mystérieuse
- Une sensibilité accrue à tout ce qui t'entoure
- Un sentiment de ne pas avoir de limites claires

## Conseils pour ce transit
- Ta sensibilité est un don si tu apprends à la protéger
- Les limites sont nécessaires même pour les âmes fluides
- Ta présence touche les autres au-delà des mots""",

    ('pisces', 2): """# ⚸ Transit de Lilith en Poissons — Maison 2

**En une phrase :** Tes ressources fluctuent avec les marées émotionnelles et spirituelles.

## L'énergie du moment
Lilith traverse ta maison des ressources avec la fluidité des Poissons. Ton rapport à l'argent peut être confus, généreux à l'excès, ou complètement détaché. Tu valorises ce qui nourrit l'âme plus que ce qui remplit le compte en banque.

## Ce que tu pourrais vivre
- Un rapport flou ou fluctuant à l'argent
- Une générosité qui peut aller jusqu'au sacrifice
- Un questionnement sur ce qui a vraiment de la valeur

## Conseils pour ce transit
- La générosité est belle, mais tu dois aussi prendre soin de toi
- Le détachement spirituel du matériel a ses limites pratiques
- Tes ressources intérieures sont ta vraie richesse""",

    ('pisces', 3): """# ⚸ Transit de Lilith en Poissons — Maison 3

**En une phrase :** Ta communication devient poétique, intuitive et parfois confuse.

## L'énergie du moment
Lilith traverse ta maison de la communication avec la poésie des Poissons. Tes mots touchent l'âme plus que l'intellect. Tu peux avoir du mal à être clair ou direct, mais ta capacité à toucher les émotions est remarquable.

## Ce que tu pourrais vivre
- Une communication plus intuitive et artistique
- Une difficulté à être précis ou factuel
- Une grande sensibilité à ce qui n'est pas dit

## Conseils pour ce transit
- Ta parole peut toucher les cœurs : utilise ce don
- La clarté est parfois nécessaire dans le monde pratique
- Les arts du langage sont ton terrain de jeu""",

    ('pisces', 4): """# ⚸ Transit de Lilith en Poissons — Maison 4

**En une phrase :** Ton foyer devient un sanctuaire spirituel ou un lieu de confusion.

## L'énergie du moment
Lilith secoue ta maison 4 avec la sensibilité des Poissons. Tu veux un espace qui nourrit ton âme, qui te permet de te retirer du monde. Les frontières familiales peuvent être floues. Tu absorbes beaucoup des émotions de ta famille.

## Ce que tu pourrais vivre
- Un besoin de sanctuaire, d'espace sacré chez toi
- Des frontières floues avec la famille d'origine
- Une sensibilité extrême aux atmosphères du foyer

## Conseils pour ce transit
- Ton foyer peut être un lieu de ressourcement spirituel
- Apprends à te protéger des émotions des autres
- La famille a ses frontières, même dans l'amour""",

    ('pisces', 5): """# ⚸ Transit de Lilith en Poissons — Maison 5

**En une phrase :** Tes amours et ta créativité prennent une dimension mystique.

## L'énergie du moment
Lilith traverse ta maison 5 avec le romantisme des Poissons. Tu tombes amoureux·se d'idéaux plus que de personnes réelles. Ta créativité est inspirée, spirituelle, parfois insaisissable. Tu cherches la fusion dans l'amour et l'art.

## Ce que tu pourrais vivre
- Des amours romantiques et idéalisés
- Une créativité très inspirée, mystique ou onirique
- Une tendance à se perdre dans les plaisirs ou les fantasmes

## Conseils pour ce transit
- L'amour idéalisé peut décevoir face à la réalité
- Ta créativité spirituelle est un don précieux
- La présence au moment présent ancre les rêves""",

    ('pisces', 6): """# ⚸ Transit de Lilith en Poissons — Maison 6

**En une phrase :** Ton quotidien doit nourrir ton âme ou il te vide.

## L'énergie du moment
Lilith traverse ta maison 6 avec la sensibilité des Poissons. Tu ne supportes pas les environnements de travail sans âme. Ta santé est très liée à ton état émotionnel et spirituel. Tu as besoin de sens et de beauté dans le quotidien.

## Ce que tu pourrais vivre
- Une sensibilité extrême à l'ambiance de ton travail
- Des symptômes physiques liés aux émotions et au stress
- Un besoin de pratiques spirituelles dans le quotidien

## Conseils pour ce transit
- Ton travail idéal nourrit l'âme autant que le corps
- La santé holistique te convient mieux que l'approche purement médicale
- La méditation et la spiritualité peuvent ancrer ton quotidien""",

    ('pisces', 7): """# ⚸ Transit de Lilith en Poissons — Maison 7

**En une phrase :** Tes relations oscillent entre fusion spirituelle et confusion des limites.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec la dissolution des Poissons. Tu cherches l'union mystique, la fusion totale avec l'autre. Mais cette quête peut mener à la confusion ou à la perte de soi. Les relations sont intenses et parfois décevantes.

## Ce que tu pourrais vivre
- Une recherche de connexion spirituelle dans les relations
- Une tendance à idéaliser ou à sauver les partenaires
- Des difficultés avec les limites dans le couple

## Conseils pour ce transit
- La fusion spirituelle est possible sans perdre ton identité
- Sauver l'autre n'est pas ton travail
- L'amour inconditionnel inclut l'amour de soi""",

    ('pisces', 8): """# ⚸ Transit de Lilith en Poissons — Maison 8

**En une phrase :** Les transformations passent par des expériences mystiques et des dissolutions profondes.

## L'énergie du moment
Lilith traverse ta maison 8 avec la profondeur spirituelle des Poissons. Les crises peuvent être des initiations mystiques. La sexualité devient sacrée ou source de confusion. Tu explores les frontières entre la vie et la mort, le réel et l'invisible.

## Ce que tu pourrais vivre
- Des transformations spirituelles profondes
- Une sexualité tantrique ou des confusions dans l'intimité
- Des expériences proches de l'au-delà ou du transcendant

## Conseils pour ce transit
- Les transformations mystiques sont puissantes et demandent du discernement
- L'intimité sacrée peut être profondément guérissante
- Garde un ancrage dans le réel pendant les voyages intérieurs""",

    ('pisces', 9): """# ⚸ Transit de Lilith en Poissons — Maison 9

**En une phrase :** Ta quête de sens devient une recherche mystique de l'unité.

## L'énergie du moment
Lilith traverse ta maison 9 avec la spiritualité des Poissons. Tu cherches une vérité qui transcende les mots et les concepts. Les traditions mystiques t'attirent. Tu veux faire l'expérience directe du divin, pas seulement y croire.

## Ce que tu pourrais vivre
- Une quête spirituelle intense et profonde
- Un attrait pour des traditions mystiques ou contemplatives
- Des expériences transcendantes qui élargissent ta conscience

## Conseils pour ce transit
- L'expérience directe du sacré transforme
- Le discernement reste nécessaire sur le chemin spirituel
- Toutes les voies mènent à l'Un si elles sont sincères""",

    ('pisces', 10): """# ⚸ Transit de Lilith en Poissons — Maison 10

**En une phrase :** Ta carrière doit servir quelque chose de plus grand que toi.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'idéalisme des Poissons. Tu veux une carrière qui a du sens spirituel, qui aide les autres, qui sert une vision plus grande. Les carrières purement matérialistes ne te satisfont plus.

## Ce que tu pourrais vivre
- Une recherche de sens spirituel dans ta vocation
- Des carrières dans l'aide, l'art, la spiritualité
- Une image publique mystérieuse ou insaisissable

## Conseils pour ce transit
- Ta carrière peut être un chemin de service
- L'idéalisme professionnel a besoin de pragmatisme
- Ta contribution peut toucher les âmes""",

    ('pisces', 11): """# ⚸ Transit de Lilith en Poissons — Maison 11

**En une phrase :** Tes cercles sociaux deviennent des espaces de connexion spirituelle.

## L'énergie du moment
Lilith traverse ta maison 11 avec la compassion des Poissons. Tu veux des amitiés qui touchent l'âme, des groupes qui servent quelque chose de plus grand. Les relations superficielles te vident. Tu peux te sentir connecté·e à l'humanité entière.

## Ce que tu pourrais vivre
- Une recherche d'amitiés spirituellement nourrissantes
- Un engagement pour des causes humanitaires ou spirituelles
- Un sentiment de connexion universelle avec les autres

## Conseils pour ce transit
- Les amitiés de l'âme sont les plus précieuses
- Les causes qui te touchent méritent ton engagement
- La compassion inclut aussi la compassion pour toi-même""",

    ('pisces', 12): """# ⚸ Transit de Lilith en Poissons — Maison 12

**En une phrase :** Tu plonges dans l'océan infini de l'inconscient et du spirituel.

## L'énergie du moment
Lilith est très puissante en Poissons dans la maison 12, son domaine ultime. C'est un transit de dissolution des limites de l'ego, de connexion avec le tout. Des expériences mystiques, des rêves prophétiques, des guérisons profondes sont possibles. Mais aussi la confusion et la perte de repères.

## Ce que tu pourrais vivre
- Des expériences spirituelles ou psychiques intenses
- Une dissolution des frontières de l'ego
- Des rêves très significatifs et des intuitions puissantes

## Conseils pour ce transit
- L'océan intérieur est immense : navigue avec sagesse
- L'ancrage est essentiel pendant ce transit dissolvant
- Ce qui se dissout fait place à quelque chose de plus vaste""",
}

async def insert_interpretations():
    """Insert all transit_lilith interpretations for Sagittarius, Capricorn, Aquarius, Pisces"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_LILITH_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_lilith',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP: transit_lilith {sign} house {house} already exists")
                skipped += 1
                continue

            interpretation = PregeneratedNatalInterpretation(
                subject='transit_lilith',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interpretation)
            print(f"INSERT: transit_lilith {sign} house {house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nDone: {inserted} inserted, {skipped} skipped")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
