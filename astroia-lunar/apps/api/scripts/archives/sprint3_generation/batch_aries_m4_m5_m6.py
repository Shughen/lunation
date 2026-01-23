"""Batch: Aries M4, M5, M6 - 36 interpretations"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # === MAISON 4 : Foyer, Famille, Racines ===
    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Aries',
     'interpretation': """**Ton mois en un mot : Feu intérieur**

Double Bélier en Maison 4 : tu vis tes émotions domestiques avec intensité. Le foyer devient un champ de bataille ou un terrain de conquête. Tu veux prendre les commandes chez toi.

**Domaine activé** : Maison 4 — Famille, racines, vie privée. Des tensions familiales peuvent émerger, ou un besoin urgent de transformer ton espace de vie.

**Ton approche instinctive** : Tu fonces dans les affaires familiales. La patience n'est pas ton fort quand il s'agit de ton foyer.

**Tensions possibles** : Conflits familiaux, impatience avec les proches, agitation à la maison.

**Conseil clé** : Canaliser ton énergie vers des améliorations concrètes de ton espace de vie.""",
     'weekly_advice': {'week_1': "Identifie ce qui doit changer chez toi.", 'week_2': "Agis sur un projet domestique concret.", 'week_3': "Gère les tensions familiales avec recul.", 'week_4': "Apprécie le chemin parcouru à la maison."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
     'interpretation': """**Ton mois en un mot : Ancrage actif**

Ta Lune Bélier en Maison 4 veut bouger les choses chez toi. L'ascendant Taureau cherche la stabilité. Tu oscilles entre changement et sécurité dans ton foyer.

**Domaine activé** : Maison 4 — Ton chez-toi, ta famille, tes racines. Tu veux un cocon solide mais tu as besoin d'action pour le construire.

**Ton approche instinctive** : Tu prends le temps de stabiliser avant de bouger. La sécurité du foyer prime.

**Tensions possibles** : Frustration si les changements tardent. Résistance au changement malgré l'envie d'action.

**Conseil clé** : Construire ta sécurité domestique pas à pas.""",
     'weekly_advice': {'week_1': "Définis ce que signifie 'sécurité' pour toi à la maison.", 'week_2': "Fais un changement concret mais mesuré.", 'week_3': "Savoure les moments de calme chez toi.", 'week_4': "Évalue la solidité de tes bases."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
     'interpretation': """**Ton mois en un mot : Foyer animé**

Ta Lune Bélier en Maison 4 dynamise ton espace privé. L'ascendant Gémeaux ajoute communication et mouvement. Ta maison devient un lieu d'échanges intenses.

**Domaine activé** : Maison 4 — Famille, foyer, racines. Beaucoup de conversations familiales, d'allées et venues, d'activité mentale à la maison.

**Ton approche instinctive** : Tu veux discuter, échanger, comprendre ta famille. La curiosité guide tes actions domestiques.

**Tensions possibles** : Agitation mentale à la maison, difficultés à trouver le calme.

**Conseil clé** : Créer des espaces de calme au milieu de l'activité.""",
     'weekly_advice': {'week_1': "Engage une conversation importante en famille.", 'week_2': "Aménage un espace calme chez toi.", 'week_3': "Réduis le bruit mental à la maison.", 'week_4': "Qu'as-tu compris sur ta famille ce mois ?"}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
     'interpretation': """**Ton mois en un mot : Protection active**

Ta Lune Bélier en Maison 4 te pousse à agir pour ta famille. L'ascendant Cancer amplifie le besoin de protection et de soin. Tu es gardien·ne de ton foyer.

**Domaine activé** : Maison 4 — Famille et racines avec une intensité émotionnelle forte. Tu ressens profondément les dynamiques familiales.

**Ton approche instinctive** : Tu protèges les tiens, parfois de manière excessive. Les émotions familiales te touchent au cœur.

**Tensions possibles** : Surprotection, hypersensibilité aux tensions familiales, difficulté à lâcher prise.

**Conseil clé** : Protéger sans étouffer, aimer sans contrôler.""",
     'weekly_advice': {'week_1': "Exprime ton amour à tes proches de manière concrète.", 'week_2': "Laisse de l'espace à ceux que tu aimes.", 'week_3': "Prends soin de toi aussi, pas seulement des autres.", 'week_4': "Célèbre les liens familiaux qui te nourrissent."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Leo',
     'interpretation': """**Ton mois en un mot : Roi de ton foyer**

Ta Lune Bélier en Maison 4 veut diriger chez toi. L'ascendant Lion ajoute fierté et générosité. Tu veux que ta maison rayonne, que ta famille soit fière.

**Domaine activé** : Maison 4 — Ton foyer devient un théâtre où tu joues un rôle central. La décoration, l'accueil, la générosité domestique t'importent.

**Ton approche instinctive** : Tu prends le lead naturellement à la maison. Tu veux être admiré·e par tes proches.

**Tensions possibles** : Ego en jeu dans les affaires familiales, besoin d'être le centre de l'attention à la maison.

**Conseil clé** : Rayonner en famille tout en laissant briller les autres.""",
     'weekly_advice': {'week_1': "Organise quelque chose de spécial chez toi.", 'week_2': "Mets en valeur un membre de ta famille.", 'week_3': "Accepte de ne pas toujours être au centre.", 'week_4': "Célèbre la fierté d'appartenir à ta famille."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
     'interpretation': """**Ton mois en un mot : Ordre domestique**

Ta Lune Bélier en Maison 4 veut agir sur ton foyer. L'ascendant Vierge canalise cette énergie vers l'organisation, le rangement, l'amélioration pratique.

**Domaine activé** : Maison 4 — Ton espace de vie demande de l'attention. Tu remarques ce qui doit être réparé, rangé, optimisé.

**Ton approche instinctive** : Tu analyses ta maison avec un œil critique. Chaque détail compte. L'ordre te rassure.

**Tensions possibles** : Perfectionnisme domestique épuisant, critiques envers les cohabitants désordonnés.

**Conseil clé** : Améliorer sans obsession — l'imperfection fait aussi partie du foyer.""",
     'weekly_advice': {'week_1': "Identifie une amélioration prioritaire chez toi.", 'week_2': "Fais le tri dans un espace encombré.", 'week_3': "Accepte que tout ne soit pas parfait.", 'week_4': "Apprécie ce que tu as accompli à la maison."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Libra',
     'interpretation': """**Ton mois en un mot : Harmonie familiale**

Ta Lune Bélier en Maison 4 veut agir, parfois brusquement, dans ton foyer. L'ascendant Balance cherche l'équilibre et la paix. Tu oscilles entre action et diplomatie à la maison.

**Domaine activé** : Maison 4 — Les relations familiales demandent de l'attention. Tu veux créer un espace beau et harmonieux.

**Ton approche instinctive** : Tu cherches le compromis en famille, l'esthétique chez toi. La décoration t'intéresse.

**Tensions possibles** : Difficultés à trancher dans les décisions familiales, évitement des conflits nécessaires.

**Conseil clé** : Créer l'harmonie sans sacrifier tes besoins.""",
     'weekly_advice': {'week_1': "Embellis un espace de ta maison.", 'week_2': "Cherche un compromis familial équitable.", 'week_3': "Ose dire ce que tu penses même si ça crée des vagues.", 'week_4': "Évalue l'équilibre dans ta vie familiale."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
     'interpretation': """**Ton mois en un mot : Transformation profonde**

Ta Lune Bélier en Maison 4 active tes racines avec intensité. L'ascendant Scorpion creuse en profondeur. Des secrets familiaux peuvent émerger, des dynamiques anciennes à transformer.

**Domaine activé** : Maison 4 — Famille, héritage émotionnel, passé. Tu plonges dans les eaux profondes de ton histoire familiale.

**Ton approche instinctive** : Tu veux comprendre, transformer, parfois détruire pour reconstruire. L'intensité émotionnelle est forte.

**Tensions possibles** : Conflits de pouvoir familiaux, confrontations aux ombres du passé, émotions intenses.

**Conseil clé** : Transformer les schémas familiaux avec courage mais compassion.""",
     'weekly_advice': {'week_1': "Explore une dynamique familiale qui te pèse.", 'week_2': "Laisse émerger ce qui doit être transformé.", 'week_3': "Ne force pas les révélations, laisse-les venir.", 'week_4': "Intègre les prises de conscience de ce mois."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
     'interpretation': """**Ton mois en un mot : Horizons familiaux**

Ta Lune Bélier en Maison 4 dynamise ton foyer. L'ascendant Sagittaire élargit ta vision de la famille. Tu veux de l'espace, de la liberté, même chez toi.

**Domaine activé** : Maison 4 — Ton rapport à la maison, aux racines. Tu peux rêver de déménagement, de voyage, d'élargissement de ton espace vital.

**Ton approche instinctive** : Tu vois grand pour ta vie domestique. Les petites cases t'étouffent.

**Tensions possibles** : Sentiment d'être à l'étroit chez toi, impatience avec les routines domestiques.

**Conseil clé** : Apporter l'aventure dans ton foyer plutôt que le fuir.""",
     'weekly_advice': {'week_1': "Imagine ta maison idéale sans limite.", 'week_2': "Apporte un élément d'ailleurs chez toi.", 'week_3': "Trouve de l'espace intérieur même dans le quotidien.", 'week_4': "Qu'as-tu appris sur ton besoin de liberté à la maison ?"}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
     'interpretation': """**Ton mois en un mot : Fondations solides**

Ta Lune Bélier en Maison 4 veut agir sur ton foyer. L'ascendant Capricorne structure cette énergie. Tu construis ta sécurité familiale avec discipline et vision long terme.

**Domaine activé** : Maison 4 — Patrimoine familial, maison, racines. Tu penses en termes de durée, d'investissement, de transmission.

**Ton approche instinctive** : Tu planifies, tu construis étape par étape. La maison est un projet sérieux.

**Tensions possibles** : Trop de sérieux à la maison, manque de légèreté familiale, pression auto-imposée.

**Conseil clé** : Construire solide tout en préservant la joie du foyer.""",
     'weekly_advice': {'week_1': "Définis un objectif à long terme pour ta maison.", 'week_2': "Fais un pas concret vers cet objectif.", 'week_3': "Allège l'atmosphère — la maison n'est pas que travail.", 'week_4': "Évalue la solidité de tes fondations familiales."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
     'interpretation': """**Ton mois en un mot : Foyer atypique**

Ta Lune Bélier en Maison 4 dynamise ton chez-toi. L'ascendant Verseau apporte originalité et détachement. Ta vision de la famille sort des normes traditionnelles.

**Domaine activé** : Maison 4 — Racines et foyer repensés. Tu questionnes les modèles familiaux, tu inventes ta propre définition du "chez-soi".

**Ton approche instinctive** : Tu veux de l'espace, de l'indépendance, même en famille. Les structures rigides t'étouffent.

**Tensions possibles** : Sentiment de décalage avec ta famille d'origine, difficulté à t'engager dans la vie domestique conventionnelle.

**Conseil clé** : Créer ta propre tribu, ta propre définition du foyer.""",
     'weekly_advice': {'week_1': "Questionne ce que 'famille' signifie vraiment pour toi.", 'week_2': "Introduis un élément original dans ton espace.", 'week_3': "Honore ta différence tout en restant connecté·e.", 'week_4': "Définis ta propre vision du foyer idéal."}},

    {'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
     'interpretation': """**Ton mois en un mot : Sanctuaire sensible**

Ta Lune Bélier en Maison 4 veut agir sur ton foyer. L'ascendant Poissons ajoute une dimension spirituelle et émotionnelle. Ta maison est un refuge pour l'âme.

**Domaine activé** : Maison 4 — Ton espace intime, tes racines. Tu as besoin d'un lieu où te ressourcer, loin du bruit du monde.

**Ton approche instinctive** : Tu ressens l'ambiance de ta maison intensément. L'harmonie énergétique du lieu t'importe.

**Tensions possibles** : Trop de perméabilité aux émotions familiales, difficulté à poser des limites chez toi.

**Conseil clé** : Créer un sanctuaire protégé tout en restant actif·ve.""",
     'weekly_advice': {'week_1': "Purifie l'énergie de ton espace de vie.", 'week_2': "Crée un coin de ressourcement chez toi.", 'week_3': "Pose des limites émotionnelles à la maison.", 'week_4': "Célèbre le refuge que tu as créé."}},

    # === MAISON 5 : Créativité, Plaisir, Expression ===
    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Aries',
     'interpretation': """**Ton mois en un mot : Explosion créative**

Double feu en Maison 5 : ta créativité est en feu. Tu veux t'exprimer, jouer, aimer, créer avec une énergie débordante. La vie est un terrain de jeu.

**Domaine activé** : Maison 5 — Créativité, plaisir, romance, enfants. Tu vis intensément les domaines de l'expression personnelle et de la joie.

**Ton approche instinctive** : Tu fonces dans ce qui te plaît. Les hésitations n'ont pas leur place quand il s'agit de passion.

**Tensions possibles** : Impulsivité amoureuse, excès dans la recherche du plaisir, ego créatif surdimensionné.

**Conseil clé** : Exprimer ta flamme créative sans te brûler ni brûler les autres.""",
     'weekly_advice': {'week_1': "Lance un projet créatif sans trop réfléchir.", 'week_2': "Vis un moment de plaisir pur.", 'week_3': "Canalise ton énergie si elle devient trop intense.", 'week_4': "Célèbre ce que tu as créé ce mois."}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
     'interpretation': """**Ton mois en un mot : Plaisir ancré**

Ta Lune Bélier en Maison 5 brûle de créer et de s'amuser. L'ascendant Taureau ancre cette énergie dans les plaisirs sensoriels. Tu veux du beau, du bon, du tangible.

**Domaine activé** : Maison 5 — Expression créative, romance, plaisir. Tu cherches des joies durables, pas des feux de paille.

**Ton approche instinctive** : Tu prends le temps de savourer. La qualité prime sur la quantité dans les plaisirs.

**Tensions possibles** : Frustration si le plaisir tarde, attachement excessif aux sources de joie.

**Conseil clé** : Savourer les plaisirs tout en restant ouvert·e à la nouveauté.""",
     'weekly_advice': {'week_1': "Offre-toi un plaisir sensoriel de qualité.", 'week_2': "Crée quelque chose de beau et durable.", 'week_3': "Évite la routine dans le plaisir.", 'week_4': "Apprécie ce qui t'a vraiment nourri·e ce mois."}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
     'interpretation': """**Ton mois en un mot : Jeu d'esprit**

Ta Lune Bélier en Maison 5 veut jouer et créer. L'ascendant Gémeaux ajoute une dimension intellectuelle et communicative. Tu t'amuses avec les mots, les idées, les échanges.

**Domaine activé** : Maison 5 — Créativité, expression, plaisir. Le jeu mental te stimule autant que le jeu physique.

**Ton approche instinctive** : Tu papillonnes entre plusieurs sources de plaisir, plusieurs projets créatifs.

**Tensions possibles** : Dispersion créative, flirts multiples, difficulté à approfondir une passion.

**Conseil clé** : Jouer avec légèreté tout en choisissant une passion à approfondir.""",
     'weekly_advice': {'week_1': "Explore plusieurs pistes créatives.", 'week_2': "Choisis celle qui t'enthousiasme le plus.", 'week_3': "Partage ta créativité par la communication.", 'week_4': "Fais le bilan de ce qui t'a vraiment amusé·e."}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
     'interpretation': """**Ton mois en un mot : Création nourricière**

Ta Lune Bélier en Maison 5 veut s'exprimer et créer. L'ascendant Cancer ajoute une dimension émotionnelle et protectrice. Tu crées pour nourrir, pour prendre soin.

**Domaine activé** : Maison 5 — Créativité, enfants, expression. Les liens avec les enfants ou ta créativité 'enfantine' sont activés.

**Ton approche instinctive** : Tu mets du cœur dans ce que tu crées. Tes œuvres sont comme tes enfants.

**Tensions possibles** : Hypersensibilité aux critiques de tes créations, surprotection de tes projets.

**Conseil clé** : Créer avec amour sans t'identifier totalement à tes œuvres.""",
     'weekly_advice': {'week_1': "Crée quelque chose qui vient du cœur.", 'week_2': "Partage ta création même si ça te rend vulnérable.", 'week_3': "Accepte les retours sans te sentir attaqué·e.", 'week_4': "Célèbre ce que tu as fait naître ce mois."}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Leo',
     'interpretation': """**Ton mois en un mot : Éclat créatif**

Double feu en Maison 5 : tu rayonnes de créativité. Ta Lune Bélier et ton ascendant Lion veulent briller, s'exprimer, être admirés. La scène est à toi.

**Domaine activé** : Maison 5 — Expression personnelle, créativité, romance, spectacle. Tu veux être vu·e, applaudi·e, aimé·e.

**Ton approche instinctive** : Tu te mets en avant naturellement. Ton charisme créatif est au maximum.

**Tensions possibles** : Ego créatif surdimensionné, besoin d'attention excessif, drame émotionnel.

**Conseil clé** : Briller authentiquement en inspirant les autres à briller aussi.""",
     'weekly_advice': {'week_1': "Prends le centre de la scène sur un projet.", 'week_2': "Encourage la créativité des autres.", 'week_3': "Vérifie que ton ego ne prend pas toute la place.", 'week_4': "Célèbre ton éclat et celui des autres."}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
     'interpretation': """**Ton mois en un mot : Création précise**

Ta Lune Bélier en Maison 5 veut créer avec élan. L'ascendant Vierge apporte précision et perfectionnisme. Tu veux que ta créativité soit impeccable.

**Domaine activé** : Maison 5 — Expression créative, plaisir. Tu analyses tes œuvres, tu cherches à les améliorer constamment.

**Ton approche instinctive** : Tu peaufines, tu corriges, tu affines. Le détail compte dans ta création.

**Tensions possibles** : Blocage créatif par excès de perfectionnisme, critique intérieure qui tue la spontanéité.

**Conseil clé** : Créer d'abord, perfectionner ensuite — l'élan prime sur la perfection.""",
     'weekly_advice': {'week_1': "Crée quelque chose sans juger.", 'week_2': "Peaufine ensuite avec bienveillance.", 'week_3': "Accepte l'imperfection comme partie du processus.", 'week_4': "Apprécie tes progrès, pas seulement le résultat."}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Libra',
     'interpretation': """**Ton mois en un mot : Beauté en action**

Ta Lune Bélier en Maison 5 veut s'exprimer. L'ascendant Balance cherche l'harmonie et l'esthétique. Tu crées pour embellir, pour plaire, pour équilibrer.

**Domaine activé** : Maison 5 — Créativité, romance, expression. L'art, la beauté, les relations amoureuses t'appellent.

**Ton approche instinctive** : Tu cherches l'équilibre dans ta créativité, la beauté dans ton expression.

**Tensions possibles** : Hésitation créative, peur de déplaire, créations qui cherchent trop à plaire.

**Conseil clé** : Créer ce qui te plaît vraiment, pas ce qui devrait plaire.""",
     'weekly_advice': {'week_1': "Crée quelque chose de beau selon tes critères.", 'week_2': "Partage-le sans chercher l'approbation.", 'week_3': "Trouve l'équilibre entre plaisir personnel et échange.", 'week_4': "Quelle beauté as-tu créée ce mois ?"}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
     'interpretation': """**Ton mois en un mot : Passion intense**

Ta Lune Bélier en Maison 5 veut créer et aimer. L'ascendant Scorpion intensifie tout. Tes passions sont profondes, tes créations transformatrices.

**Domaine activé** : Maison 5 — Romance, créativité, expression. Tu vis ces domaines avec une intensité qui peut être magnétique ou effrayante.

**Ton approche instinctive** : Tu te donnes à fond ou pas du tout. Le tiède ne t'intéresse pas.

**Tensions possibles** : Obsession amoureuse, créativité sombre, jalousie dans les relations.

**Conseil clé** : Canaliser l'intensité vers la création plutôt que la destruction.""",
     'weekly_advice': {'week_1': "Plonge dans une passion créative.", 'week_2': "Exprime ce qui est profond en toi.", 'week_3': "Évite les jeux de pouvoir en amour.", 'week_4': "Intègre les transformations de ce mois."}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
     'interpretation': """**Ton mois en un mot : Aventure créative**

Double feu expansif en Maison 5 : ta créativité veut explorer, grandir, s'aventurer. Tu crées avec enthousiasme et vision.

**Domaine activé** : Maison 5 — Expression, plaisir, romance. Tu cherches des expériences créatives qui t'élargissent, t'élèvent.

**Ton approche instinctive** : Tu vois grand pour tes projets créatifs. L'optimisme guide ta création.

**Tensions possibles** : Projets créatifs trop ambitieux, promesses romantiques excessives.

**Conseil clé** : Rêver grand tout en ancrant ta créativité dans le réel.""",
     'weekly_advice': {'week_1': "Lance un projet créatif ambitieux.", 'week_2': "Explore une forme d'expression nouvelle.", 'week_3': "Vérifie que tes projets sont réalisables.", 'week_4': "Célèbre l'expansion créative accomplie."}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
     'interpretation': """**Ton mois en un mot : Création structurée**

Ta Lune Bélier en Maison 5 veut jouer et créer. L'ascendant Capricorne structure cette énergie. Tu crées avec discipline, pour des résultats durables.

**Domaine activé** : Maison 5 — Expression créative avec un objectif. Tu veux que ta création mène quelque part.

**Ton approche instinctive** : Tu planifies ta créativité, tu lui donnes un cadre. Le jeu a un but.

**Tensions possibles** : Trop de sérieux tue la spontanéité créative, plaisir vécu comme improductif.

**Conseil clé** : Permettre à la créativité d'être joueuse, pas seulement productive.""",
     'weekly_advice': {'week_1': "Définis un objectif pour ta créativité.", 'week_2': "Laisse aussi de la place au jeu pur.", 'week_3': "Allège ton rapport à la création.", 'week_4': "Qu'as-tu construit de créatif ce mois ?"}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
     'interpretation': """**Ton mois en un mot : Originalité brûlante**

Ta Lune Bélier en Maison 5 veut s'exprimer. L'ascendant Verseau apporte originalité et avant-gardisme. Ta créativité sort des sentiers battus.

**Domaine activé** : Maison 5 — Expression unique, expérimentations créatives. Tu refuses les formats convenus.

**Ton approche instinctive** : Tu innoves, tu surprends, tu choques parfois. La norme t'ennuie.

**Tensions possibles** : Originalité pour l'originalité, difficulté à être compris·e.

**Conseil clé** : Être unique tout en restant connecté·e à ce qui touche les autres.""",
     'weekly_advice': {'week_1': "Crée quelque chose de vraiment original.", 'week_2': "Partage-le avec des esprits ouverts.", 'week_3': "Vérifie que ton originalité communique quelque chose.", 'week_4': "Qu'as-tu apporté de nouveau ce mois ?"}},

    {'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
     'interpretation': """**Ton mois en un mot : Création inspirée**

Ta Lune Bélier en Maison 5 veut créer avec élan. L'ascendant Poissons ajoute inspiration, intuition, dimension artistique. Tu crées depuis un espace au-delà du mental.

**Domaine activé** : Maison 5 — Expression artistique, créativité intuitive. L'art, la musique, la poésie t'appellent.

**Ton approche instinctive** : Tu laisses venir l'inspiration, tu te laisses guider par le flow créatif.

**Tensions possibles** : Difficulté à concrétiser les inspirations, rêverie créative sans action.

**Conseil clé** : Laisser l'inspiration guider l'action — créer ce qui vient à toi.""",
     'weekly_advice': {'week_1': "Ouvre-toi à l'inspiration sans la forcer.", 'week_2': "Traduis une intuition en création concrète.", 'week_3': "Ne perds pas tes idées dans les limbes.", 'week_4': "Qu'est-ce qui t'a été inspiré ce mois ?"}},

    # === MAISON 6 : Quotidien, Santé, Organisation ===
    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Aries',
     'interpretation': """**Ton mois en un mot : Action quotidienne**

Double Bélier en Maison 6 : ton quotidien s'accélère. Tu veux optimiser, améliorer, foncer dans les tâches. L'énergie au travail est au maximum.

**Domaine activé** : Maison 6 — Travail quotidien, santé, routines. Tu as besoin de bouger, d'agir, de ne pas rester inactif·ve.

**Ton approche instinctive** : Tu attaques ta to-do list avec énergie. La procrastination n'existe pas ce mois.

**Tensions possibles** : Épuisement par excès d'activité, impatience avec les tâches lentes.

**Conseil clé** : Canaliser ton énergie vers des routines durables, pas des sprints.""",
     'weekly_advice': {'week_1': "Lance-toi dans une amélioration de routine.", 'week_2': "Maintiens l'élan sans t'épuiser.", 'week_3': "Écoute les signaux de ton corps.", 'week_4': "Évalue ce que tes routines ont accompli."}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
     'interpretation': """**Ton mois en un mot : Routine solide**

Ta Lune Bélier en Maison 6 veut bouger au quotidien. L'ascendant Taureau cherche la stabilité. Tu construis des habitudes durables avec énergie.

**Domaine activé** : Maison 6 — Travail, santé, organisation. Tu veux des routines qui tiennent dans le temps.

**Ton approche instinctive** : Tu établis des habitudes concrètes, tangibles. La régularité te sécurise.

**Tensions possibles** : Résistance au changement une fois la routine établie.

**Conseil clé** : Créer des routines solides mais flexibles.""",
     'weekly_advice': {'week_1': "Identifie une habitude à ancrer ce mois.", 'week_2': "Pratique-la quotidiennement.", 'week_3': "Ajuste si nécessaire sans abandonner.", 'week_4': "Apprécie la solidité de ta nouvelle routine."}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
     'interpretation': """**Ton mois en un mot : Quotidien varié**

Ta Lune Bélier en Maison 6 veut de l'action au quotidien. L'ascendant Gémeaux ajoute variété et communication. Tu as besoin de stimulation dans tes tâches.

**Domaine activé** : Maison 6 — Travail, routines. Tu gères plusieurs tâches à la fois, tu communiques beaucoup au travail.

**Ton approche instinctive** : Tu jongles entre les activités, tu varies les plaisirs quotidiens.

**Tensions possibles** : Dispersion dans les tâches, stress par excès de multitasking.

**Conseil clé** : Varier sans s'éparpiller — une chose à la fois, puis passer à l'autre.""",
     'weekly_advice': {'week_1': "Organise ta semaine avec variété.", 'week_2': "Termine ce que tu commences avant de switcher.", 'week_3': "Simplifie si tu te sens débordé·e.", 'week_4': "Qu'est-ce qui a vraiment fonctionné dans tes routines ?"}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
     'interpretation': """**Ton mois en un mot : Soin quotidien**

Ta Lune Bélier en Maison 6 veut agir au quotidien. L'ascendant Cancer ajoute une dimension de soin et de protection. Tu prends soin de toi et des autres dans les petites choses.

**Domaine activé** : Maison 6 — Santé, quotidien, service. Tu es attentif·ve à ton bien-être et à celui de ton entourage.

**Ton approche instinctive** : Tu agis pour protéger, nourrir. Les routines de soin t'importent.

**Tensions possibles** : Surmenage par excès de service aux autres, oubli de tes propres besoins.

**Conseil clé** : Prendre soin de toi d'abord pour mieux servir les autres.""",
     'weekly_advice': {'week_1': "Établis une routine de self-care.", 'week_2': "Équilibre service aux autres et à toi-même.", 'week_3': "Écoute les besoins de ton corps.", 'week_4': "Célèbre le soin que tu t'es apporté."}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Leo',
     'interpretation': """**Ton mois en un mot : Excellence quotidienne**

Ta Lune Bélier en Maison 6 veut performer au quotidien. L'ascendant Lion ajoute fierté et désir de reconnaissance. Tu veux briller dans ton travail de tous les jours.

**Domaine activé** : Maison 6 — Travail, performance quotidienne. Tu veux être fier·e de ce que tu accomplis.

**Ton approche instinctive** : Tu donnes le meilleur de toi dans les tâches quotidiennes. Tu veux être reconnu·e.

**Tensions possibles** : Frustration si le quotidien semble trop banal, ego blessé par des tâches ingrates.

**Conseil clé** : Trouver de la grandeur dans les petites choses quotidiennes.""",
     'weekly_advice': {'week_1': "Accomplis une tâche avec excellence.", 'week_2': "Accepte les tâches modestes avec grâce.", 'week_3': "Reconnais tes efforts même non vus.", 'week_4': "Célèbre ce que tu as accompli au quotidien."}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
     'interpretation': """**Ton mois en un mot : Perfectionnisme actif**

Ta Lune Bélier en Maison 6 veut avancer vite. L'ascendant Vierge veut que ce soit parfait. Tu optimises, analyses, améliores constamment ton quotidien.

**Domaine activé** : Maison 6 — Organisation, santé, efficacité. Tu traques les inefficacités, tu peaufines tes routines.

**Ton approche instinctive** : Tu analyses chaque détail de ton quotidien. L'amélioration continue t'anime.

**Tensions possibles** : Anxiété liée au perfectionnisme, critique excessive de toi-même.

**Conseil clé** : Viser l'amélioration, pas la perfection absolue.""",
     'weekly_advice': {'week_1': "Identifie une amélioration clé pour ton quotidien.", 'week_2': "Implémente-la sans viser la perfection.", 'week_3': "Accepte que 'assez bien' soit parfois suffisant.", 'week_4': "Apprécie les progrès réalisés."}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Libra',
     'interpretation': """**Ton mois en un mot : Équilibre quotidien**

Ta Lune Bélier en Maison 6 veut de l'action. L'ascendant Balance cherche l'harmonie. Tu travailles à équilibrer ton quotidien, à créer des routines plaisantes.

**Domaine activé** : Maison 6 — Travail et bien-être. Tu veux un quotidien qui soit à la fois productif et agréable.

**Ton approche instinctive** : Tu cherches l'équilibre entre effort et repos, travail et plaisir.

**Tensions possibles** : Difficulté à trancher entre tâches, procrastination par désir de faire les choses 'bien'.

**Conseil clé** : Agir maintenant et ajuster ensuite plutôt que chercher l'équilibre parfait d'abord.""",
     'weekly_advice': {'week_1': "Équilibre tes journées entre tâches et pauses.", 'week_2': "Décide et agis, même imparfaitement.", 'week_3': "Rééquilibre si tu t'es déséquilibré·e.", 'week_4': "Quel équilibre quotidien as-tu trouvé ?"}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
     'interpretation': """**Ton mois en un mot : Transformation quotidienne**

Ta Lune Bélier en Maison 6 veut agir. L'ascendant Scorpion intensifie chaque tâche. Ton quotidien devient un terrain de transformation profonde.

**Domaine activé** : Maison 6 — Routines, santé, travail. Tu ne fais rien à moitié, même les tâches ordinaires.

**Ton approche instinctive** : Tu transformes, tu purges, tu élimines l'inutile. L'intensité marque ton quotidien.

**Tensions possibles** : Obsession des détails, relations de travail tendues, épuisement par excès d'intensité.

**Conseil clé** : Utiliser l'intensité pour des transformations choisies, pas subies.""",
     'weekly_advice': {'week_1': "Identifie ce qui doit être éliminé de tes routines.", 'week_2': "Transforme une habitude qui ne te sert plus.", 'week_3': "Évite l'obsession du contrôle.", 'week_4': "Observe ce qui a changé dans ton quotidien."}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
     'interpretation': """**Ton mois en un mot : Sens au quotidien**

Ta Lune Bélier en Maison 6 veut de l'action quotidienne. L'ascendant Sagittaire cherche du sens. Tu as besoin que ton travail serve à quelque chose de plus grand.

**Domaine activé** : Maison 6 — Travail et routines avec une quête de sens. Le quotidien banal t'ennuie.

**Ton approche instinctive** : Tu cherches à élever tes tâches, à leur donner une dimension.

**Tensions possibles** : Impatience avec les tâches qui semblent absurdes, tendance à négliger le pratique.

**Conseil clé** : Trouver du sens dans les petites choses ou les relier à une vision plus grande.""",
     'weekly_advice': {'week_1': "Connecte tes tâches à un but plus large.", 'week_2': "Accepte que certaines tâches soient juste pratiques.", 'week_3': "Trouve de la joie dans le quotidien ordinaire.", 'week_4': "Quel sens as-tu donné à ton quotidien ce mois ?"}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
     'interpretation': """**Ton mois en un mot : Discipline productive**

Ta Lune Bélier en Maison 6 veut avancer. L'ascendant Capricorne structure cette énergie. Tu construis des routines efficaces et durables.

**Domaine activé** : Maison 6 — Travail, organisation, productivité. Tu es sérieux·se dans tes tâches quotidiennes.

**Ton approche instinctive** : Tu planifies, tu structures, tu persévères. La discipline est ton alliée.

**Tensions possibles** : Trop de travail, oubli du plaisir, rigidité dans les routines.

**Conseil clé** : Être productif·ve sans sacrifier la joie de vivre.""",
     'weekly_advice': {'week_1': "Établis une structure claire pour ta semaine.", 'week_2': "Exécute avec discipline.", 'week_3': "Intègre des moments de légèreté.", 'week_4': "Évalue ta productivité et ton bien-être."}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
     'interpretation': """**Ton mois en un mot : Routines innovantes**

Ta Lune Bélier en Maison 6 veut de l'action quotidienne. L'ascendant Verseau apporte originalité. Tu réinventes tes routines, tu refuses les méthodes standard.

**Domaine activé** : Maison 6 — Travail et quotidien repensés. Les approches conventionnelles t'ennuient.

**Ton approche instinctive** : Tu innoves dans tes méthodes de travail, tu testes des approches originales.

**Tensions possibles** : Résistance aux processus établis, routines trop changeantes.

**Conseil clé** : Innover dans les méthodes tout en gardant une structure stable.""",
     'weekly_advice': {'week_1': "Teste une nouvelle façon de faire.", 'week_2': "Évalue ce qui fonctionne.", 'week_3': "Garde ce qui marche, change le reste.", 'week_4': "Quelle innovation as-tu apportée à ton quotidien ?"}},

    {'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
     'interpretation': """**Ton mois en un mot : Flow quotidien**

Ta Lune Bélier en Maison 6 veut agir. L'ascendant Poissons ajoute fluidité et intuition. Ton quotidien oscille entre action et lâcher-prise.

**Domaine activé** : Maison 6 — Routines et santé avec une dimension spirituelle. L'écoute du corps et de l'intuition guide ton quotidien.

**Ton approche instinctive** : Tu ressens ce dont tu as besoin plutôt que de suivre un plan rigide.

**Tensions possibles** : Manque de structure, procrastination rêveuse, oubli des tâches pratiques.

**Conseil clé** : Allier intuition et structure — écouter ton corps tout en tenant tes engagements.""",
     'weekly_advice': {'week_1': "Crée une routine qui respecte ton rythme.", 'week_2': "Écoute ton corps sur ce dont il a besoin.", 'week_3': "Ne néglige pas les tâches pratiques.", 'week_4': "Quel équilibre as-tu trouvé entre flow et structure ?"}},
]

if __name__ == "__main__":
    asyncio.run(insert_batch(BATCH))
    print(f"\n[BATCH] Aries M4-M5-M6 complete - 72/1728")
