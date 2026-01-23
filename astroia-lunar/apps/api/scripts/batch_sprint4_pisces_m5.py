"""
Batch Sprint 4 - Pisces M5 - 12 ascendants
Généré par Claude Opus 4.5 directement
"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Aries",
        "interpretation": """**Ton mois en un mot : Passion rêveuse**

Ta Lune en Poissons en Maison 5 veut créer depuis l'intuition et l'inspiration. Ton Ascendant Bélier ajoute l'urgence d'agir : tu veux manifester tes visions créatives MAINTENANT, sans attendre que tout soit parfait.

**Domaine activé** : Maison 5 — Ta créativité, ton expression personnelle, tes joies et tes amours sont au centre. Tu cherches à donner forme à tes rêves à travers l'art, le jeu ou la romance.

**Ton approche instinctive** : Le Bélier te fait passer à l'action créative rapidement, parfois avant que l'inspiration soit pleinement formée. Cette impulsion peut donner naissance à des créations brutes et authentiques.

**Tensions possibles** : L'impatience du Bélier peut t'empêcher de laisser mûrir tes inspirations. Tu risques de commencer mille projets créatifs sans les terminer.

**Conseil clé** : Canaliser ton feu créatif dans un projet qui te permet d'improviser tout en avançant.""",
        "weekly_advice": {
            "week_1": "Lance-toi dans un projet créatif sans trop réfléchir, suis ton élan.",
            "week_2": "Exprime une émotion profonde à travers un geste artistique spontané.",
            "week_3": "Ose montrer une création imparfaite qui vient du cœur.",
            "week_4": "Célèbre ta capacité à créer depuis l'intuition pure."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Taurus",
        "interpretation": """**Ton mois en un mot : Création sensuelle**

Ta Lune en Poissons en Maison 5 veut créer depuis l'imagination et l'inspiration. Ton Ascendant Taureau ajoute la matière et les sens : tu veux donner forme tangible à tes rêves, créer quelque chose de beau qu'on peut toucher.

**Domaine activé** : Maison 5 — Ta créativité et ton expression personnelle cherchent à s'incarner dans la matière. Tu ressens le besoin de créer avec tes mains, de donner une forme concrète à tes visions.

**Ton approche instinctive** : Le Taureau te fait avancer lentement mais sûrement dans tes projets créatifs. Tu cherches la beauté et le plaisir sensoriel dans tout ce que tu crées.

**Tensions possibles** : La lenteur du Taureau peut frustrer l'impatience créative des Poissons. Tu risques de procrastiner en attendant le moment "parfait" pour créer.

**Conseil clé** : Créer avec tes sens comme guides, sans te presser mais sans te bloquer non plus.""",
        "weekly_advice": {
            "week_1": "Commence un projet créatif manuel qui engage tes sens (cuisine, poterie, etc.).",
            "week_2": "Crée dans un environnement beau et confortable qui t'inspire.",
            "week_3": "Partage une création qui t'a demandé du temps et de la patience.",
            "week_4": "Savoure le processus créatif autant que le résultat."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Gemini",
        "interpretation": """**Ton mois en un mot : Imagination bavarde**

Ta Lune en Poissons en Maison 5 veut créer depuis l'intuition pure. Ton Ascendant Gémeaux ajoute la parole et le mouvement mental : tu veux raconter tes rêves, les communiquer, les explorer sous tous les angles.

**Domaine activé** : Maison 5 — Ta créativité s'exprime à travers les mots, les histoires, les conversations. Tu cherches à donner une forme narrative à tes inspirations profondes.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre différentes idées créatives. Tu explores, tu testes, tu changes d'avis. Cette versatilité peut être riche ou dispersée.

**Tensions possibles** : La légèreté du Gémeaux peut diluer la profondeur émotionnelle des Poissons. Tu risques de rester en surface de tes inspirations au lieu de les approfondir.

**Conseil clé** : Choisir un support créatif (écriture, podcast) qui honore à la fois ta profondeur et ta curiosité.""",
        "weekly_advice": {
            "week_1": "Écris une histoire courte inspirée d'un rêve ou d'une intuition.",
            "week_2": "Partage tes idées créatives avec quelqu'un qui peut t'aider à les développer.",
            "week_3": "Explore différentes formes d'expression sans t'engager immédiatement.",
            "week_4": "Choisis un projet et approfondis-le plutôt que de disperser ton énergie."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Cancer",
        "interpretation": """**Ton mois en un mot : Tendresse créative**

Ta Lune en Poissons en Maison 5 crée depuis l'émotion pure. Ton Ascendant Cancer amplifie cette sensibilité : tu veux nourrir les autres avec ta créativité, créer des choses qui touchent le cœur et réconfortent.

**Domaine activé** : Maison 5 — Ta créativité et ton expression personnelle sont guidées par l'amour et la protection. Tu cherches à créer un espace de douceur et de sécurité émotionnelle à travers ton art.

**Ton approche instinctive** : Le Cancer te fait créer depuis tes émotions les plus tendres. Tu nourris ton processus créatif comme tu nourris tes proches, avec soin et dévotion.

**Tensions possibles** : L'hypersensibilité peut te paralyser. Tu risques d'avoir peur de montrer tes créations de peur d'être blessé·e ou rejeté·e.

**Conseil clé** : Créer d'abord pour toi-même, comme un espace de sécurité émotionnelle, avant de partager.""",
        "weekly_advice": {
            "week_1": "Crée quelque chose qui réconforte ton enfant intérieur.",
            "week_2": "Partage une création avec un·e proche de confiance pour tester la réception.",
            "week_3": "Utilise ton art pour exprimer une émotion que tu as du mal à verbaliser.",
            "week_4": "Célèbre ta vulnérabilité créative comme une force, pas une faiblesse."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Leo",
        "interpretation": """**Ton mois en un mot : Magie rayonnante**

Ta Lune en Poissons en Maison 5 crée depuis l'invisible et le mystère. Ton Ascendant Lion veut illuminer le monde avec cette magie : tu cherches à transformer tes visions en quelque chose de spectaculaire et généreux.

**Domaine activé** : Maison 5 — Ta créativité veut briller et toucher les cœurs. Tu ressens le besoin de créer quelque chose de grand, de beau, qui laisse une trace lumineuse dans le monde.

**Ton approche instinctive** : Le Lion te pousse à créer avec panache et confiance. Tu veux que tes créations soient reconnues, admirées, mais aussi qu'elles servent quelque chose de plus grand que toi.

**Tensions possibles** : L'ego du Lion peut entrer en conflit avec l'humilité des Poissons. Tu risques de créer pour la gloire plutôt que pour l'âme, ou de douter de ta légitimité à briller.

**Conseil clé** : Créer depuis ton cœur le plus généreux, sans chercher la validation mais en assumant ton rayonnement.""",
        "weekly_advice": {
            "week_1": "Lance un projet créatif ambitieux qui te fait un peu peur.",
            "week_2": "Partage une création qui vient du cœur avec le grand public.",
            "week_3": "Accepte les compliments sur ton travail sans minimiser ton talent.",
            "week_4": "Offre ta créativité au service d'une cause qui te dépasse."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Virgo",
        "interpretation": """**Ton mois en un mot : Rêve précis**

Ta Lune en Poissons en Maison 5 crée depuis le chaos inspiré. Ton Ascendant Vierge cherche à perfectionner ces visions : tu veux donner une forme impeccable à tes inspirations floues.

**Domaine activé** : Maison 5 — Ta créativité oscille entre inspiration divine et perfectionnisme terrestre. Tu cherches à créer quelque chose qui soit à la fois magique et techniquement irréprochable.

**Ton approche instinctive** : La Vierge te fait analyser et améliorer tes créations. Cette quête de perfection peut affiner ton travail ou bloquer ton élan créatif par excès de critique.

**Tensions possibles** : Le jugement de la Vierge peut tuer la spontanéité des Poissons. Tu risques de sur-analyser tes inspirations au point de les perdre.

**Conseil clé** : Laisser d'abord l'inspiration couler librement, affiner ensuite avec discernement.""",
        "weekly_advice": {
            "week_1": "Crée quelque chose sans te soucier de la qualité, juste pour libérer l'inspiration.",
            "week_2": "Peaufine un projet créatif existant avec attention aux détails.",
            "week_3": "Offre tes compétences techniques au service d'un projet artistique collectif.",
            "week_4": "Accepte l'imperfection comme partie intégrante du processus créatif."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Libra",
        "interpretation": """**Ton mois en un mot : Beauté harmonieuse**

Ta Lune en Poissons en Maison 5 crée depuis l'intuition et l'émotion. Ton Ascendant Balance ajoute un sens esthétique raffiné : tu veux créer quelque chose de beau qui apporte harmonie et équilibre au monde.

**Domaine activé** : Maison 5 — Ta créativité cherche la beauté et l'harmonie. Tu ressens le besoin de créer des choses qui plaisent, qui rassemblent, qui créent du lien.

**Ton approche instinctive** : La Balance te fait collaborer dans tes projets créatifs. Tu cherches l'avis des autres, tu équilibres différentes influences, parfois au détriment de ta vision personnelle.

**Tensions possibles** : Le besoin de plaire peut diluer ton authenticité créative. Tu risques de créer pour les autres plutôt que pour ton âme.

**Conseil clé** : Créer d'abord ce qui résonne avec ton cœur, ajuster ensuite pour partager cette beauté.""",
        "weekly_advice": {
            "week_1": "Crée quelque chose d'esthétiquement plaisant qui te fait sourire.",
            "week_2": "Collabore sur un projet artistique avec quelqu'un dont tu admires le goût.",
            "week_3": "Partage une création et accueille les retours sans te perdre dedans.",
            "week_4": "Trouve le juste équilibre entre ton expression et ce qui résonne avec les autres."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Scorpio",
        "interpretation": """**Ton mois en un mot : Création cathartique**

Ta Lune en Poissons en Maison 5 crée depuis les profondeurs émotionnelles. Ton Ascendant Scorpion plonge encore plus loin : tu veux transformer ton ombre en art, révéler ce qui est caché, créer depuis la crise.

**Domaine activé** : Maison 5 — Ta créativité devient un espace de transformation intense. Tu cherches à exprimer ce qui ne peut être dit, à créer depuis tes blessures et tes mystères.

**Ton approche instinctive** : Le Scorpion te pousse à créer des œuvres qui dérangent, qui transforment, qui ne laissent pas indifférent. Cette intensité peut fasciner ou repousser.

**Tensions possibles** : L'obsession créative peut devenir destructrice. Tu risques de te perdre dans des processus trop intenses ou de créer depuis la souffrance plutôt que depuis la guérison.

**Conseil clé** : Utiliser ta créativité comme espace de transformation sans te consumer dans le processus.""",
        "weekly_advice": {
            "week_1": "Crée quelque chose qui exprime une part d'ombre que tu es prêt·e à révéler.",
            "week_2": "Utilise l'art comme rituel de transformation personnelle.",
            "week_3": "Partage une création qui ose dire une vérité inconfortable.",
            "week_4": "Laisse mourir un projet pour faire place à une renaissance créative."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Sagittarius",
        "interpretation": """**Ton mois en un mot : Vision inspirée**

Ta Lune en Poissons en Maison 5 crée depuis l'intuition mystique. Ton Ascendant Sagittaire élargit cette vision : tu veux créer quelque chose qui porte un message, qui inspire, qui ouvre des horizons.

**Domaine activé** : Maison 5 — Ta créativité cherche le sens et l'expansion. Tu ressens le besoin de créer des œuvres qui enseignent, qui font voyager, qui transmettent une sagesse.

**Ton approche instinctive** : Le Sagittaire te fait créer avec optimisme et foi en ton message. Tu veux inspirer les autres à travers ton art, partager une vision qui les élève.

**Tensions possibles** : Le besoin de sens peut t'empêcher de créer simplement pour le plaisir. Tu risques de sur-intellectualiser tes inspirations ou d'être trop didactique.

**Conseil clé** : Créer des œuvres qui portent un message tout en restant joueur et spontané.""",
        "weekly_advice": {
            "week_1": "Lance un projet créatif qui explore une quête ou une philosophie de vie.",
            "week_2": "Partage une création qui enseigne quelque chose d'important pour toi.",
            "week_3": "Explore une forme d'art d'une culture qui t'inspire ou t'est étrangère.",
            "week_4": "Crée simplement pour le plaisir, sans chercher à transmettre de message."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Capricorn",
        "interpretation": """**Ton mois en un mot : Discipline inspirée**

Ta Lune en Poissons en Maison 5 crée depuis le rêve et l'intuition. Ton Ascendant Capricorne ajoute structure et ambition : tu veux transformer tes visions en quelque chose de solide, de durable, de professionnel.

**Domaine activé** : Maison 5 — Ta créativité cherche la maîtrise et la reconnaissance. Tu ressens le besoin de prendre ton art au sérieux, d'y consacrer du temps et de l'effort.

**Ton approche instinctive** : Le Capricorne te fait travailler dur sur tes projets créatifs. Cette discipline peut donner naissance à des œuvres magistrales ou étouffer la spontanéité de l'inspiration.

**Tensions possibles** : L'ambition peut te faire créer pour la réussite plutôt que pour l'âme. Tu risques de bloquer ton inspiration sous le poids des attentes et des objectifs.

**Conseil clé** : Construire une pratique créative disciplinée qui laisse de la place à l'inspiration spontanée.""",
        "weekly_advice": {
            "week_1": "Établis une routine créative régulière même si tu n'es pas inspiré·e.",
            "week_2": "Fixe-toi un objectif concret pour un projet créatif à long terme.",
            "week_3": "Montre ton travail à un professionnel pour obtenir un retour constructif.",
            "week_4": "Permets-toi une pause créative sans culpabilité pour te ressourcer."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Aquarius",
        "interpretation": """**Ton mois en un mot : Innovation mystique**

Ta Lune en Poissons en Maison 5 crée depuis l'invisible et l'universel. Ton Ascendant Verseau ajoute l'originalité et la vision collective : tu veux créer quelque chose d'unique qui serve le bien commun.

**Domaine activé** : Maison 5 — Ta créativité cherche à bousculer les codes et à innover. Tu ressens le besoin de créer des œuvres non-conventionnelles qui libèrent et inspirent.

**Ton approche instinctive** : Le Verseau te fait expérimenter sans crainte du jugement. Tu explores des formes d'art alternatives, des collaborations inattendues, des messages révolutionnaires.

**Tensions possibles** : Le détachement du Verseau peut te couper de l'émotion pure des Poissons. Tu risques de créer des œuvres trop conceptuelles qui perdent leur cœur.

**Conseil clé** : Innover tout en restant connecté·e à ta sensibilité et à l'humanité de ton art.""",
        "weekly_advice": {
            "week_1": "Expérimente une forme d'art que tu n'as jamais essayée auparavant.",
            "week_2": "Collabore sur un projet créatif avec des personnes très différentes de toi.",
            "week_3": "Crée quelque chose qui porte un message social ou humanitaire.",
            "week_4": "Reviens à l'émotion simple : crée ce qui te touche vraiment."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 5,
        "lunar_ascendant": "Pisces",
        "interpretation": """**Ton mois en un mot : Pure inspiration**

Triple Poissons sur ta créativité : Lune, Maison 5 et Ascendant. C'est un mois où ton art devient channeling, où tu crées depuis une source qui te dépasse. L'inspiration coule comme un fleuve.

**Domaine activé** : Maison 5 — Ta créativité est à son maximum de sensibilité et de réceptivité. Tu es un canal pour l'inspiration divine, mystique, universelle. Tout devient potentiellement art.

**Ton approche instinctive** : Triple Poissons te fait créer en état de grâce, comme en transe. Tu ne contrôles pas, tu accueilles ce qui vient. Cette ouverture peut créer des œuvres magnifiques ou te perdre dans le chaos.

**Tensions possibles** : Risque de submersion créative et de perte de structure. Tu peux être paralysé·e par l'ampleur de tes inspirations ou incapable de donner forme à ce qui te traverse.

**Conseil clé** : Créer des rituels et des cadres qui canalisent ton inspiration sans la bloquer.""",
        "weekly_advice": {
            "week_1": "Crée en état de flow total, laisse l'inspiration te guider sans réfléchir.",
            "week_2": "Médite avant de créer pour te connecter à ta source intérieure.",
            "week_3": "Partage une création qui vient d'un lieu mystique en toi.",
            "week_4": "Ancre ton processus créatif avec un rituel ou un espace sacré."
        }
    }
]

if __name__ == "__main__":
    print(f"[*] Batch: Pisces M5 - {len(BATCH)} interprétations")
    asyncio.run(insert_batch(BATCH))
    print(f"[✓] Pisces M5 terminé")
