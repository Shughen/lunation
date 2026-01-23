#!/usr/bin/env python3
"""
Insert transit_lilith interpretations V2 for Aries, Taurus, Gemini, Cancer (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_LILITH_INTERPRETATIONS = {
    # ============== ARIES (Bélier) ==============
    ('aries', 1): """# ⚸ Transit de Lilith en Bélier — Maison 1

**En une phrase :** Ta part d'ombre réclame d'exister pleinement et de s'affirmer sans compromis.

## L'énergie du moment
Lilith en Bélier dans ta maison 1 réveille un besoin viscéral d'authenticité brute. Tu ne supportes plus les masques, ni les tiens ni ceux des autres. Cette énergie peut être déstabilisante car elle te pousse à montrer des facettes de toi que tu cachais peut-être. Ton magnétisme devient plus intense, presque provocant.

## Ce que tu pourrais vivre
- Une envie irrépressible de te réinventer physiquement ou dans ton image
- Des réactions impulsives qui surprennent ton entourage (et toi-même)
- Une attraction pour les situations qui te permettent de tester tes limites

## Conseils pour ce transit
- Canalise cette énergie brute dans une activité physique intense
- Observe tes colères : elles révèlent ce qui compte vraiment pour toi
- Ne te censure pas, mais choisis tes batailles avec discernement""",

    ('aries', 2): """# ⚸ Transit de Lilith en Bélier — Maison 2

**En une phrase :** Tes désirs matériels s'intensifient et questionnent ta relation à la possession.

## L'énergie du moment
Lilith en Bélier secoue ta maison des ressources. Tu pourrais ressentir une faim insatiable de sécurité financière ou, au contraire, une envie de tout envoyer balader. Cette période révèle tes rapports complexes à l'argent, aux possessions, et à ce que tu crois mériter. Des tabous autour de l'argent peuvent remonter.

## Ce que tu pourrais vivre
- Des achats impulsifs qui défient la raison mais satisfont un besoin profond
- Une remise en question de ce qui te donne vraiment de la valeur
- Des tensions autour de questions d'argent avec des proches

## Conseils pour ce transit
- Identifie les croyances limitantes héritées sur l'argent et la réussite
- Permets-toi de désirer sans culpabiliser, mais pose des garde-fous
- Explore ce qui te fait te sentir riche au-delà du matériel""",

    ('aries', 3): """# ⚸ Transit de Lilith en Bélier — Maison 3

**En une phrase :** Ta parole devient plus incisive et refuse toute forme de censure.

## L'énergie du moment
Lilith traverse ta maison de la communication avec l'énergie brûlante du Bélier. Tes mots peuvent devenir des armes ou des outils de libération. Tu n'as plus envie de tourner autour du pot ni de ménager les susceptibilités. Cette période peut créer des tensions avec l'entourage proche, mais aussi des conversations libératrices.

## Ce que tu pourrais vivre
- Des vérités qui sortent de façon brutale, parfois malgré toi
- Une fascination pour des sujets tabous ou controversés
- Des frictions avec frères, sœurs ou voisins sur des non-dits

## Conseils pour ce transit
- Utilise cette énergie pour écrire, t'exprimer créativement
- Apprends à dire les choses vraies avec bienveillance
- Ne confonds pas authenticité et agressivité gratuite""",

    ('aries', 4): """# ⚸ Transit de Lilith en Bélier — Maison 4

**En une phrase :** Les fantômes familiaux se réveillent et demandent à être confrontés.

## L'énergie du moment
Lilith remue les fondations de ta maison 4 avec l'impétuosité du Bélier. Des mémoires familiales, des secrets ou des blessures anciennes peuvent remonter. Tu pourrais ressentir une colère sourde envers tes origines ou un besoin urgent de te libérer de schémas hérités. Ton rapport à ton espace intime change.

## Ce que tu pourrais vivre
- Des conflits ou des révélations dans la sphère familiale
- Un besoin de transformer radicalement ton lieu de vie
- Une confrontation avec ce que tu as toujours tu sur ton passé

## Conseils pour ce transit
- Accueille ce qui remonte sans te laisser submerger
- Le travail sur les lignées peut être particulièrement puissant maintenant
- Créer un espace vraiment à toi peut être thérapeutique""",

    ('aries', 5): """# ⚸ Transit de Lilith en Bélier — Maison 5

**En une phrase :** Tes désirs créatifs et amoureux s'expriment sans filtre.

## L'énergie du moment
Lilith enflamme ta maison 5 avec la fougue du Bélier. C'est une période d'intensité créative et romantique où tu refuses de jouer selon les règles établies. Ta sexualité, ta créativité, ton rapport au plaisir deviennent des terrains d'exploration sauvage. Tu veux vivre passionnément.

## Ce que tu pourrais vivre
- Des attractions puissantes pour des personnes ou situations "interdites"
- Une créativité débridée qui peut choquer ou fasciner
- Des prises de risques dans les jeux, l'amour, l'expression de soi

## Conseils pour ce transit
- Canalise cette énergie brûlante dans un projet créatif audacieux
- En amour, distingue passion authentique et autodestruction
- Permets à ton enfant intérieur rebelle de s'exprimer sainement""",

    ('aries', 6): """# ⚸ Transit de Lilith en Bélier — Maison 6

**En une phrase :** Tu ne tolères plus ce qui te fait du mal dans ton quotidien.

## L'énergie du moment
Lilith traverse ta maison du quotidien avec l'énergie combative du Bélier. Les routines qui t'étouffent, les situations de travail toxiques, les habitudes auto-destructrices : tout est mis en lumière. Ton corps peut exprimer des révoltes si tu ignores ses signaux. C'est un appel à assainir ton quotidien.

## Ce que tu pourrais vivre
- Une intolérance accrue aux environnements de travail malsains
- Des symptômes physiques qui t'obligent à ralentir ou changer
- Un désir de rompre avec des habitudes qui ne te servent plus

## Conseils pour ce transit
- Écoute ton corps comme un allié, pas comme un ennemi
- N'hésite pas à poser des limites fermes au travail
- Explore des pratiques de santé alternatives qui te correspondent""",

    ('aries', 7): """# ⚸ Transit de Lilith en Bélier — Maison 7

**En une phrase :** Tes relations sont le miroir de ta part sauvage qui demande sa place.

## L'énergie du moment
Lilith secoue ta maison des partenariats avec la fougue du Bélier. Les rapports de force dans tes relations deviennent visibles. Tu peux être attiré·e par des personnes intenses ou conflictuelles, ou projeter sur l'autre ta propre colère refoulée. C'est une période pour revoir tes contrats relationnels.

## Ce que tu pourrais vivre
- Des conflits révélateurs dans tes relations importantes
- Une attraction pour des partenaires magnétiques mais compliqués
- Une prise de conscience de ce que tu sacrifies pour plaire

## Conseils pour ce transit
- Ce que tu reproches à l'autre parle souvent de toi : écoute
- Réclame ta place dans tes relations sans écraser l'autre
- Les relations qui survivent à ce transit en sortent plus authentiques""",

    ('aries', 8): """# ⚸ Transit de Lilith en Bélier — Maison 8

**En une phrase :** Tu plonges dans tes profondeurs pour y affronter tes démons.

## L'énergie du moment
Lilith est chez elle dans la maison 8, et avec le Bélier, elle y met le feu. C'est une période d'intensité transformatrice où tout ce qui était caché remonte : désirs inavoués, peurs profondes, rapports à la mort et à la sexualité. Les questions d'argent partagé ou d'héritages peuvent aussi créer des remous.

## Ce que tu pourrais vivre
- Des expériences psychologiques ou sexuelles intenses et transformatrices
- Des crises qui te forcent à mourir à d'anciennes versions de toi
- Des révélations sur des secrets ou des manipulations

## Conseils pour ce transit
- Le travail thérapeutique profond est particulièrement efficace maintenant
- Explore ta sexualité en conscience, sans te juger
- Accueille les fins comme des renaissances nécessaires""",

    ('aries', 9): """# ⚸ Transit de Lilith en Bélier — Maison 9

**En une phrase :** Tes croyances sont bousculées par une soif de vérité brute.

## L'énergie du moment
Lilith traverse ta maison de l'expansion avec l'énergie pionnière du Bélier. Tu remets en question les dogmes, les certitudes acquises, les systèmes de pensée hérités. Tu peux être attiré·e par des philosophies marginales ou des expériences qui élargissent radicalement ta vision du monde.

## Ce que tu pourrais vivre
- Une remise en question profonde de tes croyances spirituelles ou politiques
- Un attrait pour des voyages ou des rencontres qui te sortent de ta zone de confort
- Des conflits avec des figures d'autorité intellectuelle ou spirituelle

## Conseils pour ce transit
- Questionne, mais ne jette pas le bébé avec l'eau du bain
- Un voyage initiatique peut être transformateur maintenant
- Construis ta propre philosophie plutôt que d'en rejeter une pour une autre""",

    ('aries', 10): """# ⚸ Transit de Lilith en Bélier — Maison 10

**En une phrase :** Ta carrière devient le théâtre de ton émancipation radicale.

## L'énergie du moment
Lilith secoue ta maison de la carrière avec la combativité du Bélier. Tu ne supportes plus les hiérarchies absurdes, les compromis qui te diminuent, les rôles qu'on t'impose. Tu veux réussir selon tes propres termes, quitte à provoquer. Ta réputation peut être chahutée, mais ton authenticité gagne du terrain.

## Ce que tu pourrais vivre
- Des tensions ou des ruptures avec l'autorité professionnelle
- Une envie de créer quelque chose de radicalement personnel
- Des réactions fortes de l'extérieur face à ton audace

## Conseils pour ce transit
- Affirme ta différence sans brûler tous tes ponts
- Ta réussite passe par l'alignement avec tes valeurs profondes
- Les réactions des autres reflètent leurs propres peurs, pas ta valeur""",

    ('aries', 11): """# ⚸ Transit de Lilith en Bélier — Maison 11

**En une phrase :** Tu te libères des groupes qui ne te permettent pas d'être toi.

## L'énergie du moment
Lilith traverse ta maison des amitiés et des idéaux avec l'indépendance du Bélier. Tu ne veux plus te conformer pour appartenir. Certaines amitiés peuvent être remises en question si elles t'obligent à jouer un rôle. Tu es attiré·e par des cercles plus marginaux ou des causes audacieuses.

## Ce que tu pourrais vivre
- Un tri naturel dans ton cercle social, parfois douloureux
- Une envie de rejoindre des communautés alternatives ou rebelles
- Des tensions avec des groupes qui ne tolèrent pas ta différence

## Conseils pour ce transit
- Les vraies amitiés supportent ton authenticité : garde celles-là
- Tes idéaux évoluent : c'est normal et sain
- Tu peux être un électron libre tout en créant des liens vrais""",

    ('aries', 12): """# ⚸ Transit de Lilith en Bélier — Maison 12

**En une phrase :** Tu fais face à l'ombre de l'ombre, cette part de toi que tu refuses de voir.

## L'énergie du moment
Lilith dans ta maison 12 avec l'énergie du Bélier peut être déstabilisant. C'est une plongée dans l'inconscient, où surgissent des colères anciennes, des désirs refoulés depuis longtemps, des parts de toi que tu as sacrifiées. Cette période demande du courage pour regarder ce que tu as toujours fui.

## Ce que tu pourrais vivre
- Des rêves intenses, révélateurs, parfois perturbants
- Un sentiment de fatigue ou de confusion si tu résistes au processus
- Des prises de conscience soudaines sur des schémas auto-sabotants

## Conseils pour ce transit
- La méditation, l'art, la thérapie sont tes meilleurs alliés
- Ce qui émerge demande à être accueilli, pas combattu
- L'isolement conscient peut être régénérateur si tu l'utilises bien""",

    # ============== TAURUS (Taureau) ==============
    ('taurus', 1): """# ⚸ Transit de Lilith en Taureau — Maison 1

**En une phrase :** Ton corps et tes désirs sensuels réclament d'être pleinement habités.

## L'énergie du moment
Lilith en Taureau dans ta maison 1 t'invite à incarner pleinement ta nature sensuelle et terrestre. Tu ne veux plus cacher ton corps, tes appétits, ta façon d'occuper l'espace. Cette énergie peut être très magnétique, mais aussi créer des tensions si tu as des conflits avec ton image corporelle.

## Ce que tu pourrais vivre
- Un rapport transformé à ton corps, ses désirs et ses besoins
- Une présence plus assumée, plus terrienne, plus sensuelle
- Des réactions fortes des autres face à ta nouvelle assurance

## Conseils pour ce transit
- Réconcilie-toi avec ton corps dans tout ce qu'il est
- Explore les plaisirs sensoriels sans culpabilité
- Ta valeur n'est pas négociable : incarne-la""",

    ('taurus', 2): """# ⚸ Transit de Lilith en Taureau — Maison 2

**En une phrase :** Tes rapports à l'argent et aux possessions révèlent des enjeux de pouvoir profonds.

## L'énergie du moment
Lilith est puissante en Taureau dans la maison 2, son territoire naturel. Tes désirs matériels s'intensifient, tout comme tes peurs de manquer. Tu peux osciller entre possessivité excessive et rejet total du matériel. Cette période révèle ce que tu crois vraiment mériter.

## Ce que tu pourrais vivre
- Une obsession ou au contraire un détachement radical par rapport à l'argent
- Des conflits autour de possessions, de territoire, de ce qui t'appartient
- Une prise de conscience de ta valeur au-delà du matériel

## Conseils pour ce transit
- Examine tes croyances sur l'abondance et le mérite
- Tu as le droit de désirer : trouve l'équilibre entre avidité et privation
- Construis une sécurité qui ne dépend pas que du matériel""",

    ('taurus', 3): """# ⚸ Transit de Lilith en Taureau — Maison 3

**En une phrase :** Ta parole devient plus lente, plus sensuelle, mais aussi plus obstinée.

## L'énergie du moment
Lilith traverse ta maison de la communication avec la ténacité du Taureau. Tes mots prennent du poids, tu ne parles plus pour ne rien dire. Mais tu peux aussi devenir têtu·e dans tes opinions. Ta voix, ton écriture peuvent devenir plus séduisantes ou plus provocantes.

## Ce que tu pourrais vivre
- Une façon de communiquer plus directe, parfois jusqu'à l'entêtement
- Des non-dits avec l'entourage proche qui finissent par sortir
- Un attrait pour des sujets liés au corps, à la sensualité, aux tabous

## Conseils pour ce transit
- Ta parole a du pouvoir : utilise-le consciemment
- Reste ouvert·e aux autres points de vue malgré tes convictions
- L'écriture sensorielle ou érotique peut être un excellent exutoire""",

    ('taurus', 4): """# ⚸ Transit de Lilith en Taureau — Maison 4

**En une phrase :** Ton besoin d'un espace sécurisant devient viscéral et non négociable.

## L'énergie du moment
Lilith en Taureau secoue ta maison 4, révélant tes besoins profonds de sécurité et d'enracinement. Des enjeux familiaux liés aux possessions, à l'héritage matériel, au territoire peuvent émerger. Tu veux créer un cocon qui te ressemble vraiment, quitte à bousculer l'ordre établi.

## Ce que tu pourrais vivre
- Des tensions familiales autour de questions d'argent ou de propriété
- Un besoin impérieux de transformer ton espace de vie
- Des mémoires liées au manque ou à l'insécurité qui remontent

## Conseils pour ce transit
- Crée un chez-toi qui nourrit tous tes sens
- Les conflits familiaux autour du matériel cachent souvent des blessures émotionnelles
- Ta sécurité intérieure ne dépend pas d'un lieu""",

    ('taurus', 5): """# ⚸ Transit de Lilith en Taureau — Maison 5

**En une phrase :** Tes plaisirs et ta créativité s'incarnent avec une intensité sensuelle.

## L'énergie du moment
Lilith traverse ta maison 5 avec la volupté du Taureau. Tes désirs de plaisir, de création, de romance deviennent très physiques, très terre-à-terre. Tu veux jouir de la vie pleinement, sans restriction. Ta créativité peut prendre des formes plus sensuelles ou provocantes.

## Ce que tu pourrais vivre
- Des attractions très physiques et intenses
- Une créativité qui passe par le corps et les sens
- Un rapport aux plaisirs sans complexe, parfois excessif

## Conseils pour ce transit
- Crée avec tes mains, ton corps, tes sens
- En amour, cherche la profondeur au-delà de l'attraction physique
- L'excès de plaisir peut être fuite : vérifie ce que tu évites""",

    ('taurus', 6): """# ⚸ Transit de Lilith en Taureau — Maison 6

**En une phrase :** Ton corps au quotidien réclame plus de respect et de plaisir.

## L'énergie du moment
Lilith en Taureau traverse ta maison 6, mettant en lumière ton rapport au corps dans le quotidien. Tu ne tolères plus les routines qui négligent tes besoins physiques. L'alimentation, le sommeil, le confort au travail deviennent des sujets sensibles. Tu veux un quotidien qui nourrit, pas qui épuise.

## Ce que tu pourrais vivre
- Une intolérance aux environnements de travail inconfortables
- Des changements dans ton rapport à la nourriture, parfois extrêmes
- Un besoin de ralentir le rythme quotidien

## Conseils pour ce transit
- Ton corps sait ce dont il a besoin : écoute-le
- Transforme tes routines en rituels de plaisir simple
- Ne sacrifie pas ton confort pour la productivité""",

    ('taurus', 7): """# ⚸ Transit de Lilith en Taureau — Maison 7

**En une phrase :** Tes relations deviennent le terrain où s'expriment tes besoins de sécurité et de possession.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec l'énergie possessive du Taureau. Les questions de territoire, de fidélité, de sécurité émotionnelle et matérielle dans les relations sont au premier plan. Tu peux te montrer très loyal·e mais aussi jaloux·se ou possessif·ve.

## Ce que tu pourrais vivre
- Des enjeux de possessivité ou de jalousie dans tes relations
- Une attraction pour des partenaires qui incarnent la stabilité ou au contraire la menacent
- Des négociations autour des ressources partagées

## Conseils pour ce transit
- La sécurité relationnelle ne passe pas par le contrôle
- Exprime tes besoins de stabilité sans étouffer l'autre
- Les relations qui valorisent ta vraie valeur méritent ton investissement""",

    ('taurus', 8): """# ⚸ Transit de Lilith en Taureau — Maison 8

**En une phrase :** Tes rapports à l'argent partagé, à la sexualité et à la mort se transforment profondément.

## L'énergie du moment
Lilith en Taureau dans la maison 8 crée une tension entre le besoin de sécurité et l'appel de la transformation. Les questions d'argent partagé, d'héritages, de dettes peuvent devenir conflictuelles. Ta sexualité prend une dimension plus profonde, plus instinctive, parfois plus sombre.

## Ce que tu pourrais vivre
- Des tensions autour d'argent qui n'est pas que le tien
- Une sexualité plus intense, plus exigeante, plus révélatrice
- Une confrontation avec ce que tu possèdes vraiment vs ce qui t'échappe

## Conseils pour ce transit
- Les possessions partagées sont des miroirs de confiance
- Explore ta sexualité comme un chemin de transformation
- Ce que tu retiens trop fort finit par t'échapper""",

    ('taurus', 9): """# ⚸ Transit de Lilith en Taureau — Maison 9

**En une phrase :** Tes croyances sont questionnées par un besoin de vérité incarnée.

## L'énergie du moment
Lilith traverse ta maison 9 avec le pragmatisme du Taureau. Les belles théories ne te suffisent plus : tu veux des croyances qui ont du sens dans le concret. Tu peux remettre en question des systèmes de pensée trop abstraits ou des enseignements qui ne nourrissent pas ta vie réelle.

## Ce que tu pourrais vivre
- Un rejet des spiritualités qui nient le corps ou le plaisir
- Un attrait pour des philosophies plus terriennes, plus concrètes
- Des voyages qui te reconnectent à la terre, à la nature

## Conseils pour ce transit
- La vraie sagesse s'incarne dans le quotidien
- Cherche des enseignements qui honorent le corps
- Tes valeurs sont tes vraies croyances""",

    ('taurus', 10): """# ⚸ Transit de Lilith en Taureau — Maison 10

**En une phrase :** Ta carrière doit refléter tes vraies valeurs ou elle devient insupportable.

## L'énergie du moment
Lilith secoue ta maison 10 avec la ténacité du Taureau. Tu ne veux plus d'une carrière qui ne te nourrit pas vraiment. Les questions d'argent et de valeur dans le monde professionnel sont centrales. Tu veux construire quelque chose de solide, mais qui respecte ce que tu vaux vraiment.

## Ce que tu pourrais vivre
- Une insatisfaction profonde si ton travail ne reflète pas tes valeurs
- Des négociations ou des conflits autour de ta rémunération
- Un désir de créer quelque chose de durable et d'authentique

## Conseils pour ce transit
- Ton travail doit valoriser ce que tu apportes réellement
- Construis sur la durée plutôt que de chercher le succès rapide
- N'accepte pas d'être sous-payé·e ou sous-estimé·e""",

    ('taurus', 11): """# ⚸ Transit de Lilith en Taureau — Maison 11

**En une phrase :** Tu redéfinis ton appartenance aux groupes selon tes vraies valeurs.

## L'énergie du moment
Lilith traverse ta maison 11 avec la solidité du Taureau. Tu ne veux plus faire partie de cercles qui ne partagent pas tes valeurs profondes. Les questions d'argent ou de ressources au sein des groupes peuvent créer des tensions. Tu cherches des amitiés durables et authentiques.

## Ce que tu pourrais vivre
- Un tri dans tes amitiés basé sur la cohérence des valeurs
- Des tensions dans des groupes autour de questions matérielles
- Un attrait pour des communautés qui valorisent la simplicité et l'authenticité

## Conseils pour ce transit
- Tes vrais amis partagent tes valeurs, pas juste tes intérêts
- Les groupes qui te demandent de renier tes valeurs ne te méritent pas
- Contribue concrètement aux causes qui te tiennent à cœur""",

    ('taurus', 12): """# ⚸ Transit de Lilith en Taureau — Maison 12

**En une phrase :** Tes attachements secrets et tes peurs de manquer émergent de l'inconscient.

## L'énergie du moment
Lilith en Taureau dans ta maison 12 révèle tes rapports cachés à la sécurité, aux possessions, au corps. Des peurs anciennes de privation, des attachements secrets, des désirs refoulés liés au confort et au plaisir peuvent émerger. C'est une période pour guérir tes rapports à la matière.

## Ce que tu pourrais vivre
- Des rêves liés à l'argent, à la nourriture, au corps, au confort
- Une confrontation avec des addictions liées au confort ou au plaisir
- Un travail profond sur tes peurs de manquer

## Conseils pour ce transit
- Ce qui t'accroche secrètement demande à être reconnu
- L'abondance vraie vient de l'intérieur
- Prends soin de ton corps même dans l'invisible""",

    # ============== GEMINI (Gémeaux) ==============
    ('gemini', 1): """# ⚸ Transit de Lilith en Gémeaux — Maison 1

**En une phrase :** Ta communication devient magnétique et tu refuses de te taire.

## L'énergie du moment
Lilith en Gémeaux dans ta maison 1 aiguise ton intellect et libère ta parole. Tu ne supportes plus de devoir modérer ce que tu dis ou ce que tu penses. Ton esprit devient plus vif, parfois mordant. Tu peux fasciner ou irriter par ta façon de dire les vérités qui dérangent.

## Ce que tu pourrais vivre
- Une parole plus libre, plus provocante, plus incisive
- Un esprit qui tourne à plein régime, parfois jusqu'à l'agitation
- Des réactions polarisées des autres face à ton franc-parler

## Conseils pour ce transit
- Ta parole est un pouvoir : utilise-le consciemment
- L'esprit a besoin de stimulation : nourris-le
- Dire la vérité et blesser gratuitement sont deux choses différentes""",

    ('gemini', 2): """# ⚸ Transit de Lilith en Gémeaux — Maison 2

**En une phrase :** Ta valeur personnelle est liée à ton intelligence et ta capacité de communication.

## L'énergie du moment
Lilith traverse ta maison des ressources avec la polyvalence des Gémeaux. Tu peux avoir plusieurs sources de revenus ou changer souvent de rapport à l'argent. Ta valeur te semble liée à tes idées, tes mots, tes connaissances. Des tensions peuvent naître de communications liées à l'argent.

## Ce que tu pourrais vivre
- Une multiplication des sources de revenus ou une instabilité financière
- Des négociations tendues autour de ta valeur intellectuelle
- Un questionnement sur ce que valent vraiment tes idées

## Conseils pour ce transit
- Tes idées ont de la valeur : fais-toi payer justement
- La diversification peut être une force ou une dispersion
- Ta valeur ne se résume pas à ce que tu sais""",

    ('gemini', 3): """# ⚸ Transit de Lilith en Gémeaux — Maison 3

**En une phrase :** Ta communication devient libérée de toute censure et peut provoquer.

## L'énergie du moment
Lilith est puissante en Gémeaux dans sa maison naturelle. Ta parole se libère totalement, pour le meilleur et le pire. Tu peux dire des vérités que personne n'ose dire, mais aussi blesser par des mots trop rapides. Les échanges avec l'entourage proche sont intenses.

## Ce que tu pourrais vivre
- Des conversations qui vont au fond des choses, sans filtre
- Des conflits ou des révélations avec frères, sœurs, voisins
- Une fascination pour des informations cachées ou des sujets tabous

## Conseils pour ce transit
- Ta parole libérée peut être guérisseuse ou destructrice : choisis
- Les secrets qui sortent peuvent libérer
- Écouter est aussi important que parler""",

    ('gemini', 4): """# ⚸ Transit de Lilith en Gémeaux — Maison 4

**En une phrase :** Les non-dits familiaux et les secrets domestiques remontent à la surface.

## L'énergie du moment
Lilith traverse ta maison 4 avec la curiosité des Gémeaux. Les histoires familiales qu'on ne raconte pas, les secrets de famille, les communications tues peuvent émerger. Tu peux avoir besoin de mouvement et de stimulation dans ton foyer, ou des conflits verbaux peuvent agiter ton espace.

## Ce que tu pourrais vivre
- Des révélations ou des conversations difficiles en famille
- Un besoin de stimulation intellectuelle dans ton espace privé
- Une remise en question des récits familiaux qu'on t'a transmis

## Conseils pour ce transit
- Les vérités familiales méritent d'être dites, avec précaution
- Ton foyer peut être un lieu d'échange et d'apprentissage
- Ne confonds pas agitation mentale et instabilité""",

    ('gemini', 5): """# ⚸ Transit de Lilith en Gémeaux — Maison 5

**En une phrase :** Ta créativité et tes amours passent par les mots et l'esprit.

## L'énergie du moment
Lilith traverse ta maison 5 avec l'intelligence vive des Gémeaux. Tu es attiré·e par les esprits brillants, par le jeu intellectuel, par la séduction verbale. Ta créativité passe par les mots, l'écriture, la communication. Les aventures amoureuses peuvent être multiples ou stimulantes intellectuellement.

## Ce que tu pourrais vivre
- Des flirts ou des relations qui passent par l'échange d'idées
- Une créativité qui s'exprime par l'écriture ou la parole
- Une tendance à la dispersion amoureuse ou créative

## Conseils pour ce transit
- L'intelligence est sexy, mais l'intimité va au-delà des mots
- Écris, parle, crée : tes idées veulent vivre
- La profondeur demande parfois de choisir plutôt que papillonner""",

    ('gemini', 6): """# ⚸ Transit de Lilith en Gémeaux — Maison 6

**En une phrase :** Ton quotidien ne supporte plus la routine monotone.

## L'énergie du moment
Lilith traverse ta maison 6 avec l'agitation des Gémeaux. Tu as besoin de variété et de stimulation dans ton quotidien. Le travail répétitif t'épuise. Ta santé peut être affectée par le stress mental ou le manque de nouveauté. Les communications au travail peuvent être tendues.

## Ce que tu pourrais vivre
- Une intolérance à la routine et aux tâches répétitives
- Du stress lié à trop de mental, pas assez de repos
- Des échanges conflictuels avec collègues autour de non-dits

## Conseils pour ce transit
- Introduis de la variété dans ton quotidien
- Le mental a besoin de pauses : médite
- Les tensions au travail cachent souvent des communications manquées""",

    ('gemini', 7): """# ⚸ Transit de Lilith en Gémeaux — Maison 7

**En une phrase :** Tes relations sont le terrain de jeux intellectuels et de vérités à dire.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec la dualité des Gémeaux. Tu peux être attiré·e par plusieurs personnes à la fois ou par des relations où l'échange intellectuel prime. Les non-dits dans le couple peuvent devenir insupportables. Tu veux des relations où on peut tout se dire.

## Ce que tu pourrais vivre
- Une attraction pour des partenaires stimulants intellectuellement
- Des conversations de fond qui clarifient ou compliquent les relations
- Une difficulté à te fixer sur un·e seul·e partenaire

## Conseils pour ce transit
- La communication vraie est le fondement des relations durables
- L'intellect séduit, mais le cœur connecte
- Être transparent ne signifie pas tout dire sans filtre""",

    ('gemini', 8): """# ⚸ Transit de Lilith en Gémeaux — Maison 8

**En une phrase :** Tu explores les profondeurs par les mots et les idées interdites.

## L'énergie du moment
Lilith traverse ta maison 8 avec la curiosité des Gémeaux. Tu es attiré·e par les connaissances occultes, les secrets, les sujets tabous. Les communications sur l'argent partagé ou la sexualité peuvent être complexes. Tu veux comprendre ce qui est caché.

## Ce que tu pourrais vivre
- Une fascination pour des savoirs interdits ou ésotériques
- Des conversations profondes sur la mort, le sexe, les tabous
- Des manipulations ou des révélations dans les échanges intimes

## Conseils pour ce transit
- Certaines vérités se révèlent progressivement
- L'intellect peut être une défense contre l'intimité vraie
- Explore les profondeurs, mais garde les pieds sur terre""",

    ('gemini', 9): """# ⚸ Transit de Lilith en Gémeaux — Maison 9

**En une phrase :** Tes croyances sont secouées par un esprit qui remet tout en question.

## L'énergie du moment
Lilith traverse ta maison 9 avec le scepticisme des Gémeaux. Aucune vérité établie n'est sacrée, tu veux tout questionner, tout vérifier. Tu peux être attiré·e par des idées alternatives ou controversées. L'enseignement et l'apprentissage prennent une dimension provocante.

## Ce que tu pourrais vivre
- Une remise en question radicale de ce qu'on t'a enseigné
- Des débats passionnés sur des questions philosophiques ou spirituelles
- Un attrait pour des théories marginales ou non conventionnelles

## Conseils pour ce transit
- Questionner est sain, mais trouve aussi des ancrages
- Toutes les vérités ne se valent pas : discerne
- Ton esprit critique est un outil, pas une fin en soi""",

    ('gemini', 10): """# ⚸ Transit de Lilith en Gémeaux — Maison 10

**En une phrase :** Ta carrière passe par la communication et refuse les cadres rigides.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'adaptabilité des Gémeaux. Tu veux une carrière qui utilise tes talents de communication, qui te permette de bouger, d'apprendre, de changer. Les structures trop rigides deviennent insupportables. Ta parole professionnelle peut faire des vagues.

## Ce que tu pourrais vivre
- Un besoin de diversité et de stimulation dans ta carrière
- Des prises de parole publiques qui peuvent choquer ou inspirer
- Des tensions avec une hiérarchie qui limite ta liberté d'expression

## Conseils pour ce transit
- Ta carrière peut combiner plusieurs facettes
- Dis ce que tu penses, mais stratégiquement
- L'adaptabilité est une force, pas de l'instabilité""",

    ('gemini', 11): """# ⚸ Transit de Lilith en Gémeaux — Maison 11

**En une phrase :** Tes amitiés et tes cercles sociaux sont filtrés par l'intelligence.

## L'énergie du moment
Lilith traverse ta maison 11 avec la sociabilité des Gémeaux. Tu veux des amitiés stimulantes intellectuellement, des échanges qui te nourrissent l'esprit. Tu peux te sentir à l'étroit dans des groupes où la pensée unique domine. Les réseaux sociaux peuvent devenir un terrain d'expression intense.

## Ce que tu pourrais vivre
- Un tri dans tes amitiés basé sur la qualité des échanges
- Une présence plus marquée dans des réseaux de communication
- Des débats ou des conflits d'idées au sein de groupes

## Conseils pour ce transit
- Les vrais amis enrichissent ta pensée, ils ne l'étouffent pas
- Les réseaux sont des outils, pas des substituts aux relations vraies
- Partage tes idées marginales avec ceux qui peuvent les entendre""",

    ('gemini', 12): """# ⚸ Transit de Lilith en Gémeaux — Maison 12

**En une phrase :** Tes pensées cachées et tes non-dits refoulés cherchent une voie de sortie.

## L'énergie du moment
Lilith en Gémeaux dans ta maison 12 active le bavardage intérieur et les pensées qu'on n'ose pas exprimer. Des idées refoulées, des mots qu'on n'a jamais dits, des communications manquées du passé peuvent remonter. L'inconscient est agité, les rêves peuvent être très verbaux.

## Ce que tu pourrais vivre
- Un mental très actif qui peut perturber le sommeil
- Des prises de conscience sur ce que tu t'es toujours empêché de dire
- Des rêves où la parole joue un rôle central

## Conseils pour ce transit
- Écris tes pensées secrètes, même si personne ne les lit
- Le journal intime est un excellent allié pour ce transit
- Ce qui demande à être dit trouvera son moment""",

    # ============== CANCER (Cancer) ==============
    ('cancer', 1): """# ⚸ Transit de Lilith en Cancer — Maison 1

**En une phrase :** Ton côté sauvage s'exprime à travers tes émotions et ton besoin de protection.

## L'énergie du moment
Lilith en Cancer dans ta maison 1 réveille tes émotions brutes et ton instinct protecteur. Tu peux osciller entre une vulnérabilité assumée et une carapace défensive. Ta présence devient plus émotionnelle, plus intuitive, parfois plus difficile à cerner pour les autres.

## Ce que tu pourrais vivre
- Des humeurs intenses qui influencent ton image
- Un besoin de te protéger tout en voulant être vu·e authentiquement
- Une sensibilité accrue aux atmosphères et aux énergies des autres

## Conseils pour ce transit
- Tes émotions sont une force, pas une faiblesse
- Protège-toi sans te fermer complètement
- Ton intuition est un guide fiable maintenant""",

    ('cancer', 2): """# ⚸ Transit de Lilith en Cancer — Maison 2

**En une phrase :** Ta sécurité financière est intimement liée à ta sécurité émotionnelle.

## L'énergie du moment
Lilith traverse ta maison 2 avec l'émotivité du Cancer. Tes finances peuvent fluctuer avec tes émotions. Tu peux chercher la sécurité matérielle pour combler un vide affectif, ou au contraire rejeter l'argent si tu l'associes à des blessures émotionnelles. Les questions de valeur touchent au cœur.

## Ce que tu pourrais vivre
- Des dépenses émotionnelles, liées au réconfort ou à la nostalgie
- Une connexion forte entre tes ressources et ton histoire familiale
- Des fluctuations financières qui suivent tes états d'âme

## Conseils pour ce transit
- Distingue besoins émotionnels et besoins matériels
- Ton rapport à l'argent raconte ton histoire familiale
- La vraie sécurité vient de l'intérieur""",

    ('cancer', 3): """# ⚸ Transit de Lilith en Cancer — Maison 3

**En une phrase :** Ta communication devient plus émotionnelle et tes mots touchent au cœur.

## L'énergie du moment
Lilith traverse ta maison de la communication avec la sensibilité du Cancer. Tes paroles sont chargées d'émotion, tu communiques avec le cœur. Les échanges avec l'entourage proche peuvent réveiller des blessures anciennes. Tes mots peuvent blesser ou guérir profondément.

## Ce que tu pourrais vivre
- Des communications très émotionnelles avec frères, sœurs, voisins
- Des non-dits d'enfance qui ressurgissent
- Une écriture ou une parole plus touchante et personnelle

## Conseils pour ce transit
- Tes mots portent tes émotions : sois conscient·e de leur impact
- Guérir les relations de l'enfance peut passer par la parole
- L'écriture intime peut être très libératrice""",

    ('cancer', 4): """# ⚸ Transit de Lilith en Cancer — Maison 4

**En une phrase :** Le foyer devient le terrain de confrontation avec tes blessures les plus profondes.

## L'énergie du moment
Lilith est très puissante en Cancer dans la maison 4, son territoire. Les fantômes familiaux, les mémoires maternelles, les blessures d'enfance demandent à être reconnues. Ton rapport au foyer, à la famille, aux origines est transformé. Des émotions très anciennes peuvent remonter.

## Ce que tu pourrais vivre
- Des tensions ou des révélations familiales intenses
- Un besoin de transformer radicalement ton espace ou tes liens familiaux
- Une confrontation avec tes blessures maternelles ou d'enfance

## Conseils pour ce transit
- La guérison familiale passe par la reconnaissance des ombres
- Ton foyer peut devenir un sanctuaire de guérison
- Les mémoires douloureuses demandent à être accueillies, pas enfouies""",

    ('cancer', 5): """# ⚸ Transit de Lilith en Cancer — Maison 5

**En une phrase :** Tes créations et tes amours sont imprégnées d'une intensité émotionnelle.

## L'énergie du moment
Lilith traverse ta maison 5 avec la profondeur du Cancer. Ta créativité devient un canal pour exprimer des émotions intenses. Tes amours peuvent être très nourriciers ou très étouffants. La relation aux enfants, réels ou symboliques, peut réveiller des enjeux profonds.

## Ce que tu pourrais vivre
- Une créativité qui puise dans l'enfance et les émotions
- Des relations amoureuses où le care et la protection sont centraux
- Des enjeux intenses autour de la parentalité ou de l'enfant intérieur

## Conseils pour ce transit
- Crée depuis tes émotions les plus profondes
- Aimer et étouffer sont différents : trouve l'équilibre
- Ton enfant intérieur a besoin d'attention""",

    ('cancer', 6): """# ⚸ Transit de Lilith en Cancer — Maison 6

**En une phrase :** Ton quotidien doit prendre soin de toi, sinon tu craques.

## L'énergie du moment
Lilith traverse ta maison 6 avec le besoin de sécurité du Cancer. Ton corps réagit fortement au stress émotionnel. Le travail qui ne nourrit pas ton cœur devient insupportable. Tu as besoin que ton quotidien soit un cocon, pas une source de stress.

## Ce que tu pourrais vivre
- Des symptômes physiques liés au stress émotionnel
- Un besoin de changer de travail ou d'environnement quotidien
- Une sensibilité accrue aux ambiances de travail

## Conseils pour ce transit
- Prends soin de toi au quotidien comme tu prendrais soin d'un enfant
- L'environnement de travail compte autant que le travail lui-même
- Les émotions non exprimées se somatisent""",

    ('cancer', 7): """# ⚸ Transit de Lilith en Cancer — Maison 7

**En une phrase :** Tes relations révèlent tes besoins émotionnels les plus profonds.

## L'énergie du moment
Lilith traverse ta maison des partenariats avec l'intensité émotionnelle du Cancer. Tu veux des relations où tu peux être vulnérable, mais tu peux aussi reproduire des schémas familiaux. Les enjeux de dépendance et d'indépendance émotionnelle sont au premier plan.

## Ce que tu pourrais vivre
- Une attraction pour des partenaires protecteurs ou au contraire très demandeurs
- Des résonances entre tes relations actuelles et ta famille d'origine
- Des besoins émotionnels intenses dans le couple

## Conseils pour ce transit
- Tes relations sont des miroirs de tes blessures d'enfance
- La dépendance affective n'est pas de l'amour
- Être vulnérable avec les bonnes personnes est une force""",

    ('cancer', 8): """# ⚸ Transit de Lilith en Cancer — Maison 8

**En une phrase :** Tu plonges dans les profondeurs émotionnelles où se cachent tes peurs les plus anciennes.

## L'énergie du moment
Lilith en Cancer dans la maison 8 remue les émotions les plus profondes et les plus anciennes. C'est un transit de guérison intense où les blessures d'enfance, les peurs viscérales, les attachements émotionnels peuvent être transformés. La relation à la mort et aux fins peut être très présente.

## Ce que tu pourrais vivre
- Des émotions très intenses liées à des pertes ou des transformations
- Une guérison profonde de blessures émotionnelles anciennes
- Une sexualité où l'intimité émotionnelle est centrale

## Conseils pour ce transit
- Les émotions qui remontent demandent à être traversées
- La thérapie est particulièrement puissante maintenant
- Mourir à d'anciennes façons d'aimer peut te libérer""",

    ('cancer', 9): """# ⚸ Transit de Lilith en Cancer — Maison 9

**En une phrase :** Tes croyances sont filtrées par tes émotions et tes racines.

## L'énergie du moment
Lilith traverse ta maison 9 avec la sensibilité du Cancer. Les enseignements qui parlent au cœur te touchent, ceux qui sont trop abstraits te laissent froid·e. Tu peux chercher des racines spirituelles ou remettre en question ce qu'on t'a appris dans l'enfance.

## Ce que tu pourrais vivre
- Une spiritualité plus intuitive et émotionnelle
- Un retour aux racines culturelles ou spirituelles familiales
- Des voyages qui reconnectent à l'origine ou à la mémoire

## Conseils pour ce transit
- La sagesse qui touche le cœur est celle qui transforme
- Tes racines peuvent être une source de guidance
- L'intellect et l'émotion peuvent s'unir dans la quête de sens""",

    ('cancer', 10): """# ⚸ Transit de Lilith en Cancer — Maison 10

**En une phrase :** Ta carrière doit avoir du sens pour ton cœur ou elle devient vide.

## L'énergie du moment
Lilith secoue ta maison 10 avec l'émotivité du Cancer. Tu ne peux plus séparer ton travail de ce que tu ressens. Ta carrière doit prendre soin des autres ou de quelque chose qui te touche. Les enjeux familiaux et professionnels peuvent se mélanger.

## Ce que tu pourrais vivre
- Un besoin de sens émotionnel dans ta carrière
- Des tensions entre vie familiale et vie professionnelle
- Une image publique plus vulnérable ou plus protectrice

## Conseils pour ce transit
- Trouve un travail qui nourrit ton cœur
- Équilibre les responsabilités familiales et professionnelles
- Ta sensibilité peut être une force dans le monde professionnel""",

    ('cancer', 11): """# ⚸ Transit de Lilith en Cancer — Maison 11

**En une phrase :** Tes amitiés deviennent des familles choisies ou se révèlent superficielles.

## L'énergie du moment
Lilith traverse ta maison 11 avec le besoin de connexion du Cancer. Tu veux des amitiés qui te nourrissent émotionnellement, des cercles où tu te sens vraiment accueilli·e. Les groupes qui ne te donnent pas ce sentiment d'appartenance deviennent insupportables.

## Ce que tu pourrais vivre
- Un tri dans tes amitiés basé sur la qualité émotionnelle
- Un désir de créer ou de rejoindre des communautés bienveillantes
- Des enjeux émotionnels dans tes participations collectives

## Conseils pour ce transit
- Tes vrais amis sont ta famille choisie
- Les groupes doivent te nourrir, pas te drainer
- Apporte ta sensibilité aux causes qui te touchent""",

    ('cancer', 12): """# ⚸ Transit de Lilith en Cancer — Maison 12

**En une phrase :** Les émotions les plus enfouies remontent des profondeurs de ton inconscient.

## L'énergie du moment
Lilith en Cancer dans ta maison 12 ouvre les portes des caves émotionnelles les plus profondes. Des blessures d'enfance, des mémoires familiales, des émotions refoulées depuis toujours peuvent émerger. C'est un transit de guérison profonde qui demande du temps et de la douceur.

## Ce que tu pourrais vivre
- Des rêves très émotionnels liés au passé et à la famille
- Des vagues d'émotions dont tu ne connais pas l'origine
- Un besoin de solitude pour intégrer ce qui remonte

## Conseils pour ce transit
- Les émotions anciennes ont besoin d'être pleurées
- Le travail sur les mémoires familiales est puissant maintenant
- La solitude peut être un baume de guérison""",
}

async def insert_interpretations():
    """Insert all transit_lilith interpretations for Aries, Taurus, Gemini, Cancer"""
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
