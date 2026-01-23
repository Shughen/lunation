"""Batch: Aries M1 - 12 ascendants"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Feu intérieur**

Ce mois-ci, tout converge vers toi. Ta Lune en Bélier en Maison 1 avec un ascendant lunaire Bélier crée une triple charge de feu : tu vibres d'une énergie brute, impatiente, tournée vers l'action immédiate. Tes émotions s'expriment sans filtre, tes envies deviennent des impulsions.

**Domaine activé** : Maison 1 — Ton image, ton corps, ta manière de te présenter au monde sont au centre de ce cycle. Tu ressens le besoin viscéral de t'affirmer, de prendre de la place, d'exister pleinement. Les projets personnels t'appellent.

**Ton approche instinctive** : Avec l'ascendant Bélier, tu fonces d'abord, tu réfléchis ensuite. Face aux obstacles, ta première réaction est de charger. Cette spontanéité te rend magnétique mais peut brusquer ton entourage.

**Tensions possibles** : Trop d'impulsivité risque de créer des conflits. L'impatience peut te faire abandonner avant d'avoir vraiment commencé.

**Conseil clé** : Canaliser cette énergie brute vers un projet concret qui te représente.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une initiative personnelle. C'est le moment d'oser.",
            'week_2': "Tiens bon sur tes engagements, même si l'excitation retombe.",
            'week_3': "Ajuste ton approche si tu sens des résistances. Écoute les retours.",
            'week_4': "Célèbre ce que tu as initié. Prépare le terrain pour la suite."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Impulsion maîtrisée**

Ta Lune en Bélier en Maison 1 te pousse à agir, à t'affirmer, à prendre les devants. Mais ton ascendant lunaire Taureau vient tempérer cette fougue : tu ressens l'urgence d'agir tout en cherchant la stabilité. C'est une danse entre l'élan et l'ancrage.

**Domaine activé** : Maison 1 — Ton identité est en jeu ce mois-ci. Tu veux te montrer tel·le que tu es, sans masque. Les questions d'apparence, de confiance en soi et d'affirmation personnelle occupent ton esprit émotionnel.

**Ton approche instinctive** : L'ascendant Taureau te fait chercher du concret avant de bouger. Tu as besoin de sentir le sol sous tes pieds. Cette prudence peut frustrer ton côté Bélier impatient, mais elle t'évite les faux départs.

**Tensions possibles** : L'envie de foncer (Bélier) contre le besoin de sécurité (Taureau) crée une friction interne. Tu peux te sentir tiraillé·e entre action et attente.

**Conseil clé** : Agir de manière progressive — un pas concret à la fois, sans perdre l'élan.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment avant de te lancer.",
            'week_2': "Pose des bases solides pour tes projets personnels.",
            'week_3': "Si tu te sens bloqué·e, fais un petit pas plutôt que rien.",
            'week_4': "Savoure les progrès, même modestes. La constance paie."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Affirmation curieuse**

Ta Lune en Bélier en Maison 1 veut s'exprimer, exister, prendre sa place. Ton ascendant lunaire Gémeaux ajoute une dimension mentale et communicative : tu t'affirmes par la parole, les idées, les échanges. Ton énergie est vive, mobile, parfois dispersée.

**Domaine activé** : Maison 1 — C'est toi le sujet central de ce cycle. Ta manière de te présenter, ton style, ta façon de t'exprimer sont en transformation. Tu cherches à montrer qui tu es vraiment, avec authenticité.

**Ton approche instinctive** : Face aux situations, tu cherches d'abord à comprendre, à questionner, à verbaliser. L'ascendant Gémeaux te rend adaptable mais peut te faire papillonner d'une idée à l'autre sans concrétiser.

**Tensions possibles** : L'impulsivité du Bélier peut entrer en conflit avec la tendance Gémeaux à trop réfléchir. Tu risques de t'éparpiller ou de changer d'avis trop vite.

**Conseil clé** : Choisir un message central et le porter avec conviction, sans te perdre dans les détails.""",
        'weekly_advice': {
            'week_1': "Exprime clairement ce que tu veux. Les mots comptent.",
            'week_2': "Approfondis une idée plutôt que d'en explorer dix.",
            'week_3': "Écoute les feedbacks, ils affinent ton positionnement.",
            'week_4': "Synthétise ce que tu as appris sur toi ce mois-ci."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Guerrier sensible**

Ta Lune en Bélier en Maison 1 te donne une énergie combative, un besoin d'action et d'affirmation. Mais ton ascendant lunaire Cancer apporte une couche émotionnelle profonde : sous la carapace du guerrier, il y a une sensibilité à fleur de peau.

**Domaine activé** : Maison 1 — Tu es appelé·e à te définir, à montrer ta vraie nature. Ce mois active des questions d'identité personnelle. Tu veux être vu·e, reconnu·e, mais aussi protégé·e dans ta vulnérabilité.

**Ton approche instinctive** : L'ascendant Cancer te fait d'abord ressentir avant d'agir. Tu testes l'ambiance, tu jauges la sécurité émotionnelle. Cette prudence peut sembler contradictoire avec ton impulsivité Bélier.

**Tensions possibles** : Le besoin de foncer (Bélier) se heurte au besoin de se sentir en sécurité (Cancer). Tu peux osciller entre audace et repli.

**Conseil clé** : Honorer ta sensibilité sans qu'elle te freine — elle est une force, pas une faiblesse.""",
        'weekly_advice': {
            'week_1': "Ose montrer qui tu es, même si ça te rend vulnérable.",
            'week_2': "Crée un espace sûr d'où tu peux agir avec confiance.",
            'week_3': "Si tu te sens à fleur de peau, prends soin de toi d'abord.",
            'week_4': "Intègre ce que tu as appris sur tes besoins émotionnels."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Éclat personnel**

Double feu en action : ta Lune en Bélier en Maison 1 combinée à un ascendant lunaire Lion crée une énergie rayonnante, affirmée, presque théâtrale. Tu veux briller, être vu·e, reconnu·e. Ton charisme est au maximum ce mois-ci.

**Domaine activé** : Maison 1 — Tout tourne autour de ton image, ta présence, ta manière d'occuper l'espace. C'est le moment de te mettre en avant, de prendre le lead, de montrer ta lumière sans complexe.

**Ton approche instinctive** : Avec l'ascendant Lion, tu abordes les situations avec confiance et générosité. Tu veux inspirer, guider, être au centre. Cette assurance est magnétique mais peut intimider.

**Tensions possibles** : L'ego peut prendre trop de place. Le besoin de reconnaissance risque de te rendre dépendant·e du regard des autres.

**Conseil clé** : Briller authentiquement, pour toi d'abord — le reste suivra naturellement.""",
        'weekly_advice': {
            'week_1': "Prends une initiative visible. Montre-toi.",
            'week_2': "Reste généreux·se avec les autres, même sous les projecteurs.",
            'week_3': "Vérifie que ton éclat ne fait pas d'ombre à ceux qui t'entourent.",
            'week_4': "Célèbre tes victoires, grandes ou petites."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Action précise**

Ta Lune en Bélier en Maison 1 te pousse à agir, à t'affirmer sans attendre. Ton ascendant lunaire Vierge tempère cette impulsivité avec un besoin d'analyse et de précision. Tu veux avancer, mais de manière organisée.

**Domaine activé** : Maison 1 — Ton identité, ton corps, ta manière de te présenter sont au cœur de ce cycle. Tu ressens le besoin de te définir clairement, peut-être de corriger certains aspects de ton image.

**Ton approche instinctive** : L'ascendant Vierge te fait analyser avant d'agir. Tu cherches le détail qui compte, la méthode efficace. Cette rigueur peut ralentir ton élan Bélier mais évite les erreurs.

**Tensions possibles** : L'impulsivité du Bélier peut s'impatienter face au perfectionnisme Vierge. Tu risques soit de foncer sans réfléchir, soit de trop analyser et ne jamais démarrer.

**Conseil clé** : Trouver l'équilibre entre l'élan spontané et la préparation méthodique.""",
        'weekly_advice': {
            'week_1': "Définis un objectif clair et les premières étapes concrètes.",
            'week_2': "Exécute avec méthode, sans chercher la perfection immédiate.",
            'week_3': "Ajuste les détails qui ne fonctionnent pas.",
            'week_4': "Fais le bilan : qu'as-tu accompli ? Que garder pour la suite ?"
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Affirmation relationnelle**

Ta Lune en Bélier en Maison 1 veut s'affirmer, exister par elle-même. Mais ton ascendant lunaire Balance cherche l'harmonie, le consensus, le regard de l'autre. C'est un mois où tu oscilles entre "moi d'abord" et "nous ensemble".

**Domaine activé** : Maison 1 — Ton identité personnelle est en jeu, mais tu la définis aussi en miroir des autres. La question "qui suis-je ?" se mêle à "qui suis-je pour les autres ?".

**Ton approche instinctive** : L'ascendant Balance te fait chercher le compromis, peser le pour et le contre. Tu veux plaire tout en t'affirmant — un équilibre délicat à trouver.

**Tensions possibles** : Le Bélier veut trancher, la Balance veut négocier. Tu risques de te perdre dans les considérations relationnelles au détriment de tes propres besoins.

**Conseil clé** : T'affirmer avec diplomatie — dire ce que tu veux sans écraser l'autre.""",
        'weekly_advice': {
            'week_1': "Clarifie tes besoins personnels avant de consulter les autres.",
            'week_2': "Cherche des accords qui respectent aussi tes envies.",
            'week_3': "Si tu te sens tiraillé·e, reviens à ce qui compte pour toi.",
            'week_4': "Trouve l'équilibre entre affirmation et relation."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Intensité brute**

Ta Lune en Bélier en Maison 1 te donne une énergie directe, impatiente. Ton ascendant lunaire Scorpion ajoute de la profondeur, de l'intensité, une dimension magnétique et parfois obsessionnelle. Tu ne fais rien à moitié ce mois-ci.

**Domaine activé** : Maison 1 — Ton identité, ta présence, ta manière d'être au monde sont en transformation. Tu ressens le besoin de te réinventer, de laisser mourir certains aspects de toi pour en révéler d'autres.

**Ton approche instinctive** : L'ascendant Scorpion te fait creuser, chercher la vérité cachée. Tu ne te contentes pas des apparences. Cette intensité peut être perçue comme intimidante.

**Tensions possibles** : L'impulsivité Bélier combinée à l'intensité Scorpion peut créer des réactions excessives. Attention aux conflits de pouvoir et aux fixations.

**Conseil clé** : Canaliser cette puissance vers une transformation personnelle choisie.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment changer en toi.",
            'week_2': "Plonge dans le processus sans te laisser submerger.",
            'week_3': "Si ça devient trop intense, prends du recul.",
            'week_4': "Observe la transformation accomplie. Tu n'es plus le·la même."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Élan aventurier**

Double feu expansif : ta Lune en Bélier en Maison 1 combinée à un ascendant lunaire Sagittaire crée une énergie enthousiaste, optimiste, tournée vers l'aventure. Tu veux vivre grand, explorer, repousser tes limites.

**Domaine activé** : Maison 1 — Ton identité s'élargit. Tu ressens le besoin de te redéfinir à travers de nouvelles expériences. Ta vision de toi-même s'agrandit, devient plus ambitieuse.

**Ton approche instinctive** : L'ascendant Sagittaire te fait voir grand, chercher le sens, l'horizon lointain. Tu abordes les situations avec foi et enthousiasme, parfois au détriment des détails pratiques.

**Tensions possibles** : L'excès d'optimisme peut te faire surestimer tes capacités ou négliger les obstacles réels. Le manque de patience aggrave ce risque.

**Conseil clé** : Viser haut tout en gardant un pied sur terre — l'aventure se construit aussi pas à pas.""",
        'weekly_advice': {
            'week_1': "Définis une vision inspirante pour ce cycle.",
            'week_2': "Fais un premier pas concret vers cette vision.",
            'week_3': "Reste ouvert·e aux ajustements sans perdre ton cap.",
            'week_4': "Célèbre le chemin parcouru, pas seulement la destination."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Ambition incarnée**

Ta Lune en Bélier en Maison 1 te pousse à l'action immédiate. Ton ascendant lunaire Capricorne structure cette énergie vers des objectifs à long terme. Tu veux agir, mais de manière stratégique, avec un but solide.

**Domaine activé** : Maison 1 — Ton identité se construit autour de tes accomplissements. Tu veux être reconnu·e pour ce que tu fais, pas seulement pour qui tu es. L'image que tu projettes doit refléter ta compétence.

**Ton approche instinctive** : L'ascendant Capricorne te fait planifier, structurer, viser le sommet. Tu prends les choses au sérieux, parfois trop. Cette discipline canalise ton impulsivité Bélier.

**Tensions possibles** : L'envie de foncer (Bélier) peut s'impatienter face au besoin de construire lentement (Capricorne). Tu risques de te frustrer ou de te surcharger de responsabilités.

**Conseil clé** : Utiliser ton énergie d'action pour bâtir quelque chose de durable.""",
        'weekly_advice': {
            'week_1': "Fixe un objectif ambitieux mais réaliste pour ce mois.",
            'week_2': "Mets en place une routine qui sert cet objectif.",
            'week_3': "Persévère même si les résultats tardent.",
            'week_4': "Évalue tes progrès avec objectivité. Ajuste pour le prochain cycle."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Affirmation libre**

Ta Lune en Bélier en Maison 1 te donne une énergie d'affirmation directe. Ton ascendant lunaire Verseau ajoute un besoin d'originalité, d'indépendance, de différence. Tu veux être toi-même, mais un "toi-même" unique, hors normes.

**Domaine activé** : Maison 1 — Ton identité se définit par ce qui te distingue des autres. Tu ressens le besoin de briser les moules, de montrer ta singularité. Les conventions t'étouffent.

**Ton approche instinctive** : L'ascendant Verseau te fait chercher des solutions originales, penser différemment. Tu abordes les situations avec détachement et innovation, parfois au détriment de l'émotion.

**Tensions possibles** : L'impulsivité Bélier peut se heurter au détachement Verseau. Tu risques d'agir de manière provocatrice juste pour être différent·e.

**Conseil clé** : Cultiver ton originalité au service de quelque chose de plus grand que toi.""",
        'weekly_advice': {
            'week_1': "Affirme ce qui te rend unique sans chercher à choquer.",
            'week_2': "Connecte ton individualité à un projet collectif.",
            'week_3': "Reste ouvert·e aux idées des autres, même conventionnelles.",
            'week_4': "Trouve comment ton originalité peut servir les autres."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Feu dans l'eau**

Ta Lune en Bélier en Maison 1 te pousse à agir, à t'affirmer. Ton ascendant lunaire Poissons ajoute une dimension intuitive, rêveuse, parfois floue. Tu ressens une urgence d'action tout en étant attiré·e par le lâcher-prise.

**Domaine activé** : Maison 1 — Ton identité se cherche entre affirmation et dissolution. Tu veux exister pleinement mais aussi te fondre dans quelque chose de plus vaste. C'est un mois de redéfinition spirituelle de soi.

**Ton approche instinctive** : L'ascendant Poissons te fait ressentir avant tout. Tu perçois les ambiances, les non-dits, les courants invisibles. Cette sensibilité peut te rendre hésitant·e à agir.

**Tensions possibles** : L'impulsivité Bélier peut être noyée par l'indécision Poissons. Tu risques de rêver l'action au lieu de la vivre, ou d'agir de manière confuse.

**Conseil clé** : Laisser ton intuition guider ton élan — agir depuis le ressenti, pas contre lui.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition avant de te lancer.",
            'week_2': "Agis même si tout n'est pas clair — fais confiance au flow.",
            'week_3': "Si tu te sens perdu·e, reviens à ton corps, à ta respiration.",
            'week_4': "Intègre les insights de ce mois. Qu'as-tu compris sur toi ?"
        }
    }
]

if __name__ == "__main__":
    asyncio.run(insert_batch(BATCH))
    print(f"\n[BATCH] Aries M1 complete - 12/1728")
