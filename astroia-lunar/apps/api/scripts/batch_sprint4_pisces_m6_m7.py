"""
Batch Sprint 4 - Pisces M6 et M7 - 24 ascendants
Généré par Claude Opus 4.5 directement
"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

# Significations des maisons
# M6: quotidien, travail, santé, routines, service
# M7: relations, partenariats, mariage, l'autre comme miroir

BATCH = []

# PISCES M6 - 12 ascendants
for asc, (interpretation, advice) in {
    "Aries": (
        """**Ton mois en un mot : Service impulsif**

Ta Lune en Poissons en Maison 6 veut servir avec compassion et dévouement. Ton Ascendant Bélier ajoute l'urgence d'agir : tu veux aider immédiatement, te rendre utile sans attendre.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé et tes routines sont au centre. Tu cherches à être utile tout en préservant ton bien-être.

**Ton approche instinctive** : Le Bélier te fait te jeter dans le service aux autres sans toujours vérifier tes limites. Cette générosité impulsive peut épuiser tes ressources.

**Tensions possibles** : Tu risques de te sacrifier trop vite au nom du service ou de t'épuiser en aidant tout le monde sauf toi-même.

**Conseil clé** : Canaliser ton élan de service en te fixant des limites claires pour protéger ton énergie.""",
        {"week_1": "Identifie un acte de service concret que tu peux accomplir cette semaine.", "week_2": "Vérifie que tu te mets au service sans te sacrifier.", "week_3": "Crée une routine quotidienne qui nourrit ton corps et ton âme.", "week_4": "Repose-toi activement : ton repos sert aussi les autres."}
    ),
    "Taurus": (
        """**Ton mois en un mot : Routine sensuelle**

Ta Lune en Poissons en Maison 6 veut servir depuis la compassion. Ton Ascendant Taureau ancre ce service dans des gestes concrets et réguliers : tu veux aider en créant du confort et de la stabilité.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace de rituels apaisants. Tu cherches à créer des routines qui nourrissent ton corps tout en servant les autres.

**Ton approche instinctive** : Le Taureau te fait servir patiemment, avec constance. Tu prends soin des autres en leur offrant confort matériel et présence stable.

**Tensions possibles** : La résistance au changement peut te faire rester dans des routines qui ne te servent plus. Tu risques de confondre service et dépendance matérielle.

**Conseil clé** : Créer des routines de soin qui honorent ton corps sans devenir rigides.""",
        {"week_1": "Établis une routine matinale qui nourrit ton corps avec plaisir.", "week_2": "Offre un soin concret à quelqu'un (repas, massage, aide pratique).", "week_3": "Ajuste une habitude qui ne te sert plus, en douceur.", "week_4": "Savoure le plaisir d'un quotidien simple et bien ancré."}
    ),
    "Gemini": (
        """**Ton mois en un mot : Service bavard**

Ta Lune en Poissons en Maison 6 veut servir avec empathie. Ton Ascendant Gémeaux ajoute la communication : tu aides en écoutant, en parlant, en partageant des informations utiles.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace d'échanges au service des autres. Tu cherches à être utile par tes mots et ta curiosité.

**Ton approche instinctive** : Le Gémeaux te fait servir en communiquant. Tu aides les autres en les écoutant, en leur apprenant des choses, en créant des connexions.

**Tensions possibles** : La dispersion mentale peut diluer ton service. Tu risques de papillonner entre différentes tâches sans vraiment aider en profondeur.

**Conseil clé** : Choisir quelques actes de service concrets plutôt que de t'éparpiller en surface.""",
        {"week_1": "Écoute vraiment quelqu'un sans chercher à résoudre immédiatement.", "week_2": "Partage une information utile qui peut aider quelqu'un.", "week_3": "Organise ton quotidien pour moins de dispersion, plus d'efficacité.", "week_4": "Reste silencieux·se parfois : le service n'est pas toujours verbal."}
    ),
    "Cancer": (
        """**Ton mois en un mot : Soin maternel**

Ta Lune en Poissons en Maison 6 veut servir avec compassion infinie. Ton Ascendant Cancer amplifie cette tendance : tu veux nourrir, protéger, prendre soin de tous comme une mère.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace de nurturing. Tu cherches à créer des routines qui soignent et nourrissent, autant toi que les autres.

**Ton approche instinctive** : Le Cancer te fait servir depuis l'émotion et l'empathie totale. Tu absorbes les besoins des autres et cherches à les combler avec dévouement.

**Tensions possibles** : Tu risques de te perdre complètement dans le service aux autres et d'oublier tes propres besoins. L'épuisement par compassion est réel.

**Conseil clé** : Apprendre à nourrir ton propre enfant intérieur avant de nourrir les autres.""",
        {"week_1": "Prépare un repas réconfortant pour toi-même avant de nourrir les autres.", "week_2": "Vérifie que tu te mets des limites dans ton service.", "week_3": "Prends soin de ton corps comme tu prendrais soin d'un enfant.", "week_4": "Accepte de recevoir du soin sans culpabilité."}
    ),
    "Leo": (
        """**Ton mois en un mot : Service généreux**

Ta Lune en Poissons en Maison 6 veut servir humblement. Ton Ascendant Lion ajoute du panache : tu veux servir avec noblesse, transformer ton quotidien en quelque chose de magnifique.

**Domaine activé** : Maison 6 — Ton quotidien et ton service deviennent une scène où tu peux rayonner. Tu cherches à être utile tout en apportant chaleur et créativité.

**Ton approche instinctive** : Le Lion te fait servir généreusement, avec le cœur. Tu veux que ton service soit remarqué, apprécié, mais aussi authentiquement aimant.

**Tensions possibles** : Le besoin de reconnaissance peut entrer en conflit avec l'humilité du service. Tu risques de servir pour briller plutôt que par pur don.

**Conseil clé** : Servir depuis ton cœur le plus généreux sans chercher les applaudissements.""",
        {"week_1": "Offre un service qui vient du cœur, sans attendre de retour.", "week_2": "Transforme une tâche quotidienne en rituel créatif et joyeux.", "week_3": "Accepte les compliments sur ton aide sans fausse modestie.", "week_4": "Sers dans l'ombre parfois, juste pour l'âme de ton geste."}
    ),
    "Virgo": (
        """**Ton mois en un mot : Perfection dévouée**

Ta Lune en Poissons en Maison 6 veut servir avec compassion. Ton Ascendant Vierge est dans son élément en Maison 6 : tu veux servir avec excellence, perfectionner chaque détail.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace d'amélioration constante. Tu cherches à optimiser tes routines et ton service avec discernement.

**Ton approche instinctive** : La Vierge te fait analyser comment mieux servir, mieux aider. Cette quête de perfection peut améliorer ton impact ou te paralyser.

**Tensions possibles** : Le perfectionnisme peut te faire juger ton service comme jamais assez bon. Tu risques de t'épuiser à vouloir tout faire parfaitement.

**Conseil clé** : Accepter que le service imparfait mais sincère vaut mieux que la perfection paralysante.""",
        {"week_1": "Améliore une routine quotidienne avec discernement, pas perfectionnisme.", "week_2": "Offre un service simple mais excellent dans son exécution.", "week_3": "Pardonne-toi quand ton aide n'est pas parfaite.", "week_4": "Repose-toi : le repos fait partie du service à toi-même."}
    ),
    "Libra": (
        """**Ton mois en un mot : Service harmonieux**

Ta Lune en Poissons en Maison 6 veut servir avec compassion. Ton Ascendant Balance cherche l'équilibre : tu veux aider tout en préservant l'harmonie et la beauté de ton quotidien.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace d'équilibre délicat entre service et bien-être. Tu cherches à aider sans te déséquilibrer.

**Ton approche instinctive** : La Balance te fait servir en créant de l'harmonie. Tu cherches des solutions qui conviennent à tous, parfois au détriment de tes propres besoins.

**Tensions possibles** : L'indécision peut te paralyser dans ton service. Tu risques de chercher l'équilibre parfait au lieu d'agir.

**Conseil clé** : Trouver le juste milieu entre don de soi et préservation de ton énergie.""",
        {"week_1": "Identifie où tu t'es déséquilibré·e dans ton service aux autres.", "week_2": "Crée un planning quotidien qui honore tes besoins ET ceux des autres.", "week_3": "Dis non à une demande pour préserver ton équilibre.", "week_4": "Embellis une routine quotidienne pour qu'elle te nourrisse vraiment."}
    ),
    "Scorpio": (
        """**Ton mois en un mot : Service transformateur**

Ta Lune en Poissons en Maison 6 veut servir avec compassion. Ton Ascendant Scorpion plonge plus profond : tu veux aider en transformant, en touchant ce qui est caché, en guérissant vraiment.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace de transformation profonde. Tu cherches à servir d'une manière qui change vraiment les choses.

**Ton approche instinctive** : Le Scorpion te fait servir avec intensité. Tu veux aller au fond des problèmes, révéler ce qui est caché pour mieux guérir.

**Tensions possibles** : L'intensité peut épuiser toi et les autres. Tu risques de forcer des transformations qui ne sont pas prêtes à émerger.

**Conseil clé** : Servir en profondeur sans brûler tes ressources, respecter le rythme de chacun.""",
        {"week_1": "Aide quelqu'un en abordant la vraie source de son problème.", "week_2": "Transforme une habitude toxique en routine régénératrice.", "week_3": "Offre ton service sans t'attacher au résultat de la transformation.", "week_4": "Prends du recul : laisse mourir ce qui doit mourir, même dans ton service."}
    ),
    "Sagittarius": (
        """**Ton mois en un mot : Service inspirant**

Ta Lune en Poissons en Maison 6 veut servir avec compassion. Ton Ascendant Sagittaire élargit cette vision : tu veux servir en inspirant, en enseignant, en ouvrant des horizons.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace d'enseignement et de partage de sagesse. Tu cherches à servir en donnant du sens.

**Ton approche instinctive** : Le Sagittaire te fait servir avec optimisme et foi. Tu aides en montrant des perspectives plus larges, en inspirant l'espoir.

**Tensions possibles** : Le besoin de sens peut te faire négliger le service concret et quotidien. Tu risques d'être trop dans la vision et pas assez dans l'action.

**Conseil clé** : Inspirer tout en restant ancré·e dans le service pratique et humble.""",
        {"week_1": "Partage une philosophie de vie qui peut aider quelqu'un concrètement.", "week_2": "Sers dans une cause qui a du sens pour toi.", "week_3": "Aide quelqu'un à voir plus grand sans négliger ses besoins immédiats.", "week_4": "Accepte que le service humble vaut autant que le grand message."}
    ),
    "Capricorn": (
        """**Ton mois en un mot : Service structuré**

Ta Lune en Poissons en Maison 6 veut servir avec compassion. Ton Ascendant Capricorne ajoute structure et discipline : tu veux créer des systèmes durables qui aident vraiment.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace de construction de routines solides. Tu cherches à servir de manière responsable et durable.

**Ton approche instinctive** : Le Capricorne te fait servir avec sérieux et engagement long terme. Tu bâtis des structures de soin qui perdurent.

**Tensions possibles** : La rigidité peut étouffer la fluidité du service compassionnel. Tu risques de te sentir obligé·e de servir par devoir plutôt que par amour.

**Conseil clé** : Créer des structures de service qui laissent place à la spontanéité et à la compassion.""",
        {"week_1": "Établis une routine de service régulière et durable.", "week_2": "Prends une responsabilité concrète pour aider quelqu'un long terme.", "week_3": "Assouplis une structure qui t'empêche de servir avec cœur.", "week_4": "Permets-toi de ne pas toujours être responsable du bien-être des autres."}
    ),
    "Aquarius": (
        """**Ton mois en un mot : Service collectif**

Ta Lune en Poissons en Maison 6 veut servir avec compassion universelle. Ton Ascendant Verseau élargit à l'humanité : tu veux servir le collectif, innover dans ta façon d'aider.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace d'expérimentation sociale. Tu cherches à servir d'une manière qui libère et innove.

**Ton approche instinctive** : Le Verseau te fait servir de façon non-conventionnelle. Tu cherches des solutions originales, des systèmes alternatifs de soin.

**Tensions possibles** : Le détachement peut te couper de l'empathie directe. Tu risques de servir l'idée de l'humanité sans vraiment aider les individus.

**Conseil clé** : Innover dans ton service tout en restant connecté·e aux besoins humains réels.""",
        {"week_1": "Expérimente une forme de service que tu n'as jamais essayée.", "week_2": "Rejoins un collectif qui sert une cause humanitaire.", "week_3": "Aide quelqu'un d'une manière qui le libère plutôt que de créer dépendance.", "week_4": "Reviens à la compassion simple : sers un individu avec cœur."}
    ),
    "Pisces": (
        """**Ton mois en un mot : Service sacré**

Triple Poissons sur ton service : Lune, Maison 6 et Ascendant. C'est un mois où tu es appelé·e à servir depuis une source spirituelle profonde. Le service devient prière.

**Domaine activé** : Maison 6 — Ton quotidien devient un espace sacré de dévouement. Tu cherches à servir comme un acte spirituel, une offrande.

**Ton approche instinctive** : Triple Poissons te fait servir sans limites, te dissoudre dans le service aux autres. Cette dévotion peut être sainte ou épuisante.

**Tensions possibles** : Tu risques de te perdre totalement dans le service et d'oublier que tu as aussi un corps qui a besoin de soin.

**Conseil clé** : Créer des limites sacrées qui protègent ton énergie tout en honorant ton appel au service.""",
        {"week_1": "Crée un rituel quotidien qui transforme le service en acte spirituel.", "week_2": "Sers avec tout ton cœur mais pose des limites claires.", "week_3": "Prends soin de ton corps : ton corps est aussi sacré.", "week_4": "Accepte que tu ne peux pas sauver tout le monde, et c'est OK."}
    ),
}.items():
    BATCH.append({
        "moon_sign": "Pisces",
        "moon_house": 6,
        "lunar_ascendant": asc,
        "interpretation": interpretation,
        "weekly_advice": advice
    })

# PISCES M7 - 12 ascendants
for asc, (interpretation, advice) in {
    "Aries": (
        """**Ton mois en un mot : Relation passionnée**

Ta Lune en Poissons en Maison 7 cherche la fusion dans les relations. Ton Ascendant Bélier ajoute l'urgence : tu veux te connecter intensément et maintenant, créer des liens qui brûlent.

**Domaine activé** : Maison 7 — Tes relations, partenariats et mariages sont au centre. Tu cherches à rencontrer l'autre dans sa pleine intensité émotionnelle.

**Ton approche instinctive** : Le Bélier te fait foncer dans les relations sans trop réfléchir. Tu veux vivre l'amour et les connexions avec passion et spontanéité.

**Tensions possibles** : L'impulsivité peut te faire perdre tes limites dans les relations. Tu risques de te jeter dans des fusions qui te font oublier qui tu es.

**Conseil clé** : Rencontrer l'autre avec passion tout en gardant ton identité intacte.""",
        {"week_1": "Initie une conversation profonde avec quelqu'un qui t'intrigue.", "week_2": "Exprime un besoin relationnel clairement et sans détour.", "week_3": "Vérifie que tu ne te perds pas dans le miroir de l'autre.", "week_4": "Ose la vulnérabilité dans une relation qui compte."}
    ),
    "Taurus": (
        """**Ton mois en un mot : Amour stable**

Ta Lune en Poissons en Maison 7 cherche la fusion émotionnelle. Ton Ascendant Taureau cherche la stabilité : tu veux des relations profondes mais aussi sûres et durables.

**Domaine activé** : Maison 7 — Tes relations demandent à la fois intimité et sécurité. Tu cherches à construire des partenariats qui nourrissent ton besoin de beauté et de constance.

**Ton approche instinctive** : Le Taureau te fait avancer lentement dans les relations. Tu testes la solidité du lien avant de t'engager pleinement.

**Tensions possibles** : La peur du changement peut te garder dans des relations qui ne te servent plus. Tu risques de confondre stabilité et stagnation.

**Conseil clé** : Construire des relations stables qui laissent place à l'évolution et à la profondeur émotionnelle.""",
        {"week_1": "Renforce un lien existant par un geste tangible et sensuel.", "week_2": "Dialogue sur ce qui crée la sécurité dans tes relations.", "week_3": "Ose lâcher une relation qui est stable mais morte.", "week_4": "Savoure la présence simple et physique de quelqu'un que tu aimes."}
    ),
    "Gemini": (
        """**Ton mois en un mot : Dialogue profond**

Ta Lune en Poissons en Maison 7 cherche la fusion émotionnelle. Ton Ascendant Gémeaux ajoute la communication : tu veux explorer l'autre par les mots, créer de l'intimité en parlant.

**Domaine activé** : Maison 7 — Tes relations deviennent des espaces de dialogue. Tu cherches à comprendre l'autre à travers l'échange et la curiosité.

**Ton approche instinctive** : Le Gémeaux te fait explorer différentes facettes de l'autre. Tu questionnes, tu t'intéresses, tu cherches à comprendre intellectuellement.

**Tensions possibles** : La légèreté du Gémeaux peut t'empêcher de plonger dans la vraie intimité. Tu risques de rester en surface des relations.

**Conseil clé** : Utiliser les mots comme pont vers l'intimité, pas comme refuge contre la profondeur.""",
        {"week_1": "Pose des questions vraiment profondes à quelqu'un que tu aimes.", "week_2": "Écoute l'autre sans chercher immédiatement à répondre ou analyser.", "week_3": "Partage une vérité sur toi que tu n'as jamais verbalisée.", "week_4": "Reste en silence ensemble : l'intimité n'est pas toujours verbale."}
    ),
    "Cancer": (
        """**Ton mois en un mot : Fusion nourricière**

Ta Lune en Poissons en Maison 7 cherche la fusion totale. Ton Ascendant Cancer amplifie : tu veux créer une relation qui soit comme un cocon, nourrir et être nourri·e émotionnellement.

**Domaine activé** : Maison 7 — Tes relations deviennent des espaces de nurturing mutuel. Tu cherches quelqu'un qui prend soin de toi autant que tu prends soin d'eux.

**Ton approche instinctive** : Le Cancer te fait aborder les relations avec une sensibilité extrême. Tu absorbes les émotions de l'autre et cherches à les apaiser.

**Tensions possibles** : La fusion peut devenir codépendance. Tu risques de perdre tes limites et d'oublier où tu finis et où l'autre commence.

**Conseil clé** : Nourrir la relation tout en gardant ton propre espace émotionnel.""",
        {"week_1": "Crée un moment de tendresse partagée avec quelqu'un que tu aimes.", "week_2": "Vérifie que tu ne te sacrifies pas pour maintenir la paix relationnelle.", "week_3": "Demande ce dont tu as besoin émotionnellement, clairement.", "week_4": "Accepte que l'autre ne peut pas tout combler, et c'est OK."}
    ),
    "Leo": (
        """**Ton mois en un mot : Amour royal**

Ta Lune en Poissons en Maison 7 cherche l'humilité dans la fusion. Ton Ascendant Lion veut être vu·e et célébré·e : tu cherches une relation où tu peux briller tout en te donnant totalement.

**Domaine activé** : Maison 7 — Tes relations demandent à la fois générosité et reconnaissance. Tu veux aimer avec grandeur et être aimé·e avec admiration.

**Ton approche instinctive** : Le Lion te fait apporter chaleur et créativité dans les relations. Tu veux que tes partenariats soient magnifiques et inspirants.

**Tensions possibles** : Le besoin de reconnaissance peut entrer en conflit avec la dissolution du moi des Poissons. Tu risques d'attendre des applaudissements même dans l'intimité.

**Conseil clé** : Aimer généreusement sans chercher constamment à être admiré·e pour ton amour.""",
        {"week_1": "Offre un geste d'amour grand et généreux sans attendre de retour.", "week_2": "Exprime ta vulnérabilité même si ça ternit ton image.", "week_3": "Célèbre une relation qui te fait grandir, pas seulement briller.", "week_4": "Accepte d'être aimé·e pour qui tu es vraiment, pas pour ton éclat."}
    ),
    "Virgo": (
        """**Ton mois en un mot : Amour perfectible**

Ta Lune en Poissons en Maison 7 cherche l'acceptation totale de l'autre. Ton Ascendant Vierge analyse et perfectionne : tu veux améliorer la relation tout en l'acceptant telle qu'elle est.

**Domaine activé** : Maison 7 — Tes relations oscillent entre idéalisation et critique. Tu cherches la perfection tout en ressentant que l'amour doit être inconditionnel.

**Ton approche instinctive** : La Vierge te fait remarquer ce qui peut être amélioré dans la relation. Cette analyse peut être utile ou destructrice selon ton intention.

**Tensions possibles** : Le jugement peut bloquer l'intimité. Tu risques de critiquer l'autre au lieu d'accepter ses imperfections.

**Conseil clé** : Servir la relation avec discernement tout en acceptant que l'amour parfait n'existe pas.""",
        {"week_1": "Identifie une amélioration constructive que tu peux proposer dans une relation.", "week_2": "Accepte consciemment une imperfection de l'autre sans chercher à la changer.", "week_3": "Offre ton aide pratique à quelqu'un que tu aimes.", "week_4": "Pardonne-toi de ne pas être le·la partenaire parfait·e."}
    ),
    "Libra": (
        """**Ton mois en un mot : Harmonie fusionnelle**

Ta Lune en Poissons en Maison 7 cherche la fusion. Ton Ascendant Balance est chez lui en Maison 7 : tu veux créer des relations parfaitement équilibrées et harmonieuses.

**Domaine activé** : Maison 7 — Tes relations sont au cœur de ta vie. Tu cherches le partenaire idéal, celui qui crée une harmonie parfaite avec toi.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre relationnel constant. Tu veux que tout soit juste, beau, harmonieux entre toi et l'autre.

**Tensions possibles** : L'indécision peut te paralyser. Tu risques de te perdre en cherchant l'équilibre parfait au lieu de vivre la relation.

**Conseil clé** : Accepter que les relations déséquilibrées temporairement font partie de la danse de l'intimité.""",
        {"week_1": "Identifie un déséquilibre dans une relation et dialogue dessus.", "week_2": "Crée un moment de beauté partagée avec quelqu'un que tu aimes.", "week_3": "Prends une décision relationnelle même si elle déplaît temporairement.", "week_4": "Accepte que l'harmonie parfaite n'existe pas, et vis quand même l'amour."}
    ),
    "Scorpio": (
        """**Ton mois en un mot : Intimité totale**

Ta Lune en Poissons en Maison 7 cherche la fusion. Ton Ascendant Scorpion plonge dans les abysses : tu veux une intimité qui révèle tout, qui transforme, qui ne cache rien.

**Domaine activé** : Maison 7 — Tes relations deviennent des espaces de vérité absolue. Tu cherches quelqu'un avec qui tu peux montrer ton ombre et être aimé·e quand même.

**Ton approche instinctive** : Le Scorpion te fait aller au fond de l'intimité. Tu veux tout savoir, tout révéler, fusionner complètement avec l'autre.

**Tensions possibles** : L'intensité peut suffoquer l'autre. Tu risques de forcer une profondeur qui n'est pas prête ou de créer de la dépendance émotionnelle.

**Conseil clé** : Honorer l'intensité de ton besoin d'intimité tout en respectant le rythme de l'autre.""",
        {"week_1": "Partage un secret ou une vérité profonde avec quelqu'un de confiance.", "week_2": "Explore une dynamique de pouvoir dans une relation importante.", "week_3": "Laisse mourir ce qui doit mourir dans une relation pour mieux renaître.", "week_4": "Accepte que certains mystères de l'autre restent mystères."}
    ),
    "Sagittarius": (
        """**Ton mois en un mot : Liberté partagée**

Ta Lune en Poissons en Maison 7 cherche la fusion. Ton Ascendant Sagittaire cherche la liberté : tu veux une relation qui soit à la fois intimité profonde et espace d'expansion.

**Domaine activé** : Maison 7 — Tes relations oscillent entre besoin de fusion et besoin d'indépendance. Tu cherches quelqu'un qui explore le monde avec toi.

**Ton approche instinctive** : Le Sagittaire te fait aborder les relations avec optimisme et soif d'aventure. Tu veux un·e partenaire de voyage autant qu'un·e amant·e.

**Tensions possibles** : La peur de l'enfermement peut t'empêcher de t'engager vraiment. Tu risques de fuir l'intimité quand elle devient trop profonde.

**Conseil clé** : Créer des relations qui honorent à la fois ton besoin de liberté et d'intimité profonde.""",
        {"week_1": "Propose une aventure ou un voyage à quelqu'un que tu aimes.", "week_2": "Dialogue sur ce que signifie la liberté dans votre relation.", "week_3": "Engage-toi dans l'intimité sans sentir que tu perds ta liberté.", "week_4": "Accepte que l'amour puisse être une aventure qui te fait aussi poser tes valises."}
    ),
    "Capricorn": (
        """**Ton mois en un mot : Engagement profond**

Ta Lune en Poissons en Maison 7 cherche la fusion émotionnelle. Ton Ascendant Capricorne cherche l'engagement durable : tu veux une relation qui soit à la fois intense et construite pour durer.

**Domaine activé** : Maison 7 — Tes relations demandent sérieux et profondeur. Tu cherches un partenariat qui soit responsable autant qu'aimant.

**Ton approche instinctive** : Le Capricorne te fait aborder les relations avec maturité. Tu cherches à construire quelque chose de solide tout en honorant ta sensibilité.

**Tensions possibles** : Le sérieux peut étouffer la spontanéité émotionnelle. Tu risques de traiter l'amour comme un contrat plutôt qu'une danse.

**Conseil clé** : Construire des relations durables qui laissent place à la vulnérabilité et à l'émotion.""",
        {"week_1": "Prends un engagement concret envers quelqu'un que tu aimes.", "week_2": "Dialogue sur les responsabilités dans votre relation.", "week_3": "Permets-toi d'être vulnérable même si ça ne semble pas «sérieux».", "week_4": "Célèbre la durée d'une relation qui a traversé le temps."}
    ),
    "Aquarius": (
        """**Ton mois en un mot : Amitié profonde**

Ta Lune en Poissons en Maison 7 cherche la fusion émotionnelle. Ton Ascendant Verseau cherche la liberté et l'amitié : tu veux une relation qui soit connexion d'âmes sans possession.

**Domaine activé** : Maison 7 — Tes relations demandent à la fois intimité et indépendance. Tu cherches des partenariats qui libèrent plutôt qu'enferment.

**Ton approche instinctive** : Le Verseau te fait aborder les relations de façon non-conventionnelle. Tu veux réinventer ce que signifie être ensemble.

**Tensions possibles** : Le détachement peut t'empêcher de plonger dans la vraie intimité. Tu risques de théoriser l'amour au lieu de le vivre.

**Conseil clé** : Innover dans ta façon d'aimer tout en acceptant la dépendance émotionnelle qui vient avec.""",
        {"week_1": "Propose une forme de relation qui sort des codes traditionnels.", "week_2": "Dialogue sur ce que signifie la liberté dans l'intimité.", "week_3": "Accepte d'avoir besoin de l'autre, même si ça va contre ton indépendance.", "week_4": "Célèbre une amitié qui est aussi profonde qu'un amour."}
    ),
    "Pisces": (
        """**Ton mois en un mot : Fusion mystique**

Triple Poissons sur tes relations : Lune, Maison 7 et Ascendant. C'est un mois où l'amour devient prière, où tu ne sais plus où tu finis et où l'autre commence.

**Domaine activé** : Maison 7 — Tes relations sont des espaces de dissolution totale du moi. Tu cherches quelqu'un avec qui fusionner complètement.

**Ton approche instinctive** : Triple Poissons te fait vivre l'amour comme une expérience mystique. Tu te donnes entièrement, parfois jusqu'à te perdre.

**Tensions possibles** : La fusion totale peut devenir codépendance. Tu risques de ne plus savoir qui tu es sans l'autre.

**Conseil clé** : Vivre l'amour comme une communion sacrée tout en gardant ton propre ancrage.""",
        {"week_1": "Médite sur ce qui est à toi et ce qui appartient à l'autre dans la relation.", "week_2": "Crée un rituel sacré avec quelqu'un que tu aimes.", "week_3": "Pose une limite même si ça rompt temporairement la fusion.", "week_4": "Célèbre l'amour qui te fait grandir, pas celui qui te fait disparaître."}
    ),
}.items():
    BATCH.append({
        "moon_sign": "Pisces",
        "moon_house": 7,
        "lunar_ascendant": asc,
        "interpretation": interpretation,
        "weekly_advice": advice
    })

if __name__ == "__main__":
    print(f"[*] Batch: Pisces M6-M7 - {len(BATCH)} interprétations")
    asyncio.run(insert_batch(BATCH))
    print(f"[✓] Pisces M6-M7 terminé")
