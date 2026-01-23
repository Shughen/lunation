"""Batch: Aries M3 - 12 ascendants (Communication)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Parole directe**

Double feu en Maison 3 : ta communication devient une arme. Tu dis ce que tu penses sans filtre, tes idées fusent, tu veux convaincre et agir vite. Les échanges quotidiens prennent une intensité nouvelle.

**Domaine activé** : Maison 3 — Communication, apprentissages, environnement proche, frères/sœurs. Tu ressens le besoin de t'exprimer, d'échanger, de bouger dans ton quartier. Les petits déplacements t'appellent.

**Ton approche instinctive** : Tu parles d'abord, tu réfléchis ensuite. Cette spontanéité peut être rafraîchissante ou créer des malentendus. Ton mental est en ébullition.

**Tensions possibles** : Les disputes verbales sont probables si tu ne tempères pas ton impulsivité. Tu peux blesser sans le vouloir par des mots trop directs.

**Conseil clé** : Canaliser ta parole percutante vers des échanges constructifs.""",
        'weekly_advice': {
            'week_1': "Exprime une idée qui te tient à cœur cette semaine.",
            'week_2': "Écoute autant que tu parles. L'autre a des choses à dire.",
            'week_3': "Réfléchis avant de répondre dans les moments tendus.",
            'week_4': "Fais le bilan de tes échanges ce mois. Qu'as-tu appris ?"
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Idées ancrées**

Ta Lune en Bélier en Maison 3 bouillonne d'idées et de mots. L'ascendant Taureau te pousse à exprimer ces idées de manière posée, concrète, avec patience. Tu veux communiquer, mais solidement.

**Domaine activé** : Maison 3 — Tes échanges quotidiens, ton apprentissage, tes relations de voisinage. Tu cherches des conversations qui ont du sens et mènent quelque part.

**Ton approche instinctive** : Le Taureau te fait prendre ton temps avant de parler. Tu préfères les mots pesés aux réactions à chaud. Cette lenteur peut frustrer ton côté Bélier.

**Tensions possibles** : Tu peux garder des choses pour toi trop longtemps puis exploser. Le décalage entre ce que tu penses et ce que tu dis crée de la tension.

**Conseil clé** : Trouver le bon timing pour exprimer tes idées avec impact.""",
        'weekly_advice': {
            'week_1': "Prépare ce que tu veux dire avant une conversation importante.",
            'week_2': "Exprime une idée que tu gardes depuis trop longtemps.",
            'week_3': "Fais une pause avant de répondre sous le coup de l'émotion.",
            'week_4': "Ancre une nouvelle habitude de communication."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Tourbillon mental**

Ta Lune Bélier en Maison 3 veut s'exprimer, et l'ascendant Gémeaux amplifie cette énergie communicative au maximum. Ton mental carbure, les idées affluent, tu veux tout dire, tout apprendre, tout explorer.

**Domaine activé** : Maison 3 — Communication, curiosité, environnement proche. C'est un mois de stimulation intellectuelle intense. Les conversations, lectures, échanges rapides te nourrissent.

**Ton approche instinctive** : Tu jongle avec les idées, tu passes d'un sujet à l'autre avec agilité. Ta parole est vive, parfois trop. Tu t'adaptes à tous les interlocuteurs.

**Tensions possibles** : Dispersion mentale garantie si tu ne te canalises pas. Tu peux commencer dix conversations sans en finir aucune.

**Conseil clé** : Choisir un fil conducteur et le suivre malgré les distractions.""",
        'weekly_advice': {
            'week_1': "Laisse ton mental s'exprimer librement. Note tes idées.",
            'week_2': "Choisis une idée à approfondir cette semaine.",
            'week_3': "Fais le tri dans le flux mental. Qu'est-ce qui compte vraiment ?",
            'week_4': "Synthétise ce que tu as appris ce mois."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Parole émotionnelle**

Ta Lune Bélier en Maison 3 veut s'exprimer directement. L'ascendant Cancer colore cette communication d'une tonalité émotionnelle. Tu parles avec le cœur, parfois de manière défensive.

**Domaine activé** : Maison 3 — Les échanges avec ton entourage proche, ta fratrie, tes voisins. Les conversations touchent à des sujets sensibles, familiaux, intimes.

**Ton approche instinctive** : Tu ressens avant de penser. Tes mots portent tes émotions, parfois malgré toi. La communication devient un espace de vulnérabilité.

**Tensions possibles** : Tu peux sur-réagir à des remarques anodines. La sensibilité Cancer peut rendre les échanges Bélier plus blessants qu'ils ne le devraient.

**Conseil clé** : Exprimer tes émotions sans te laisser submerger par elles.""",
        'weekly_advice': {
            'week_1': "Ose parler de ce que tu ressens vraiment.",
            'week_2': "Écoute les besoins émotionnels de ton entourage proche.",
            'week_3': "Si une conversation te blesse, prends du recul avant de réagir.",
            'week_4': "Renforce un lien avec un proche par un échange sincère."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Expression flamboyante**

Ta Lune Bélier en Maison 3 veut se faire entendre, et l'ascendant Lion amplifie cette envie avec théâtralité. Tu communiques pour briller, convaincre, inspirer. Ta parole a du panache.

**Domaine activé** : Maison 3 — Communication, environnement proche, apprentissages. Tu veux être le centre des conversations, celui·celle qu'on écoute et qu'on admire.

**Ton approche instinctive** : Tu t'exprimes avec générosité et confiance. Tes mots sont forts, parfois excessifs. Tu sais captiver un auditoire.

**Tensions possibles** : Le besoin d'être entendu·e peut éclipser les autres. Tu risques de monopoliser la parole ou de dramatiser.

**Conseil clé** : Briller par ta parole tout en laissant de la place aux autres.""",
        'weekly_advice': {
            'week_1': "Prends la parole sur un sujet qui te passionne.",
            'week_2': "Encourage quelqu'un d'autre à s'exprimer.",
            'week_3': "Vérifie que tu écoutes autant que tu parles.",
            'week_4': "Célèbre les échanges qui t'ont fait grandir ce mois."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision verbale**

Ta Lune Bélier en Maison 3 bouillonne d'idées, mais l'ascendant Vierge les filtre, les organise, les précise. Tu veux communiquer efficacement, avec les bons mots, au bon moment.

**Domaine activé** : Maison 3 — Communication, apprentissages pratiques, organisation du quotidien. Tu analyses tes échanges, tu cherches l'information utile.

**Ton approche instinctive** : Tu détailles, tu corriges, tu précises. Chaque mot compte. Cette rigueur peut ralentir ton impulsivité Bélier.

**Tensions possibles** : Tu peux devenir trop critique dans tes échanges, pointer les erreurs au lieu de valoriser. L'analyse tue parfois la spontanéité.

**Conseil clé** : Allier l'élan Bélier à la précision Vierge pour une communication percutante et juste.""",
        'weekly_advice': {
            'week_1': "Organise tes idées avant de les exprimer.",
            'week_2': "Apprends quelque chose de pratique et utile.",
            'week_3': "Évite les critiques inutiles dans tes échanges.",
            'week_4': "Fais le point sur ce que tu as appris ce mois."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Dialogue équilibré**

Ta Lune Bélier en Maison 3 veut s'exprimer avec force, mais l'ascendant Balance cherche l'harmonie. Tu oscilles entre dire ce que tu penses et préserver la relation.

**Domaine activé** : Maison 3 — Communication et échanges quotidiens. Tu cherches des conversations équilibrées où chacun·e peut s'exprimer. La diplomatie t'intéresse.

**Ton approche instinctive** : Tu pèses tes mots, tu cherches le consensus. Cette diplomatie peut frustrer ton côté Bélier qui veut trancher.

**Tensions possibles** : Tu peux dire ce que l'autre veut entendre au lieu de ta vérité. L'indécision Balance bloque parfois l'expression directe Bélier.

**Conseil clé** : Être diplomate sans te perdre — ta vérité compte aussi.""",
        'weekly_advice': {
            'week_1': "Exprime ton point de vue avec tact mais clarté.",
            'week_2': "Cherche des compromis qui respectent aussi tes besoins.",
            'week_3': "Ose un désaccord constructif si nécessaire.",
            'week_4': "Évalue la qualité de tes échanges ce mois."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Parole pénétrante**

Ta Lune Bélier en Maison 3 veut communiquer, et l'ascendant Scorpion donne à tes mots une profondeur intense. Tu ne fais pas de small talk : tu veux des échanges vrais, qui touchent au cœur.

**Domaine activé** : Maison 3 — Communication et environnement proche. Les conversations superficielles t'ennuient. Tu cherches la vérité cachée, les non-dits.

**Ton approche instinctive** : Tu creuses, tu questionnes, tu perces les façades. Tes mots peuvent être tranchants, révélateurs, parfois blessants.

**Tensions possibles** : L'intensité peut effrayer ou braquer tes interlocuteurs. Tu peux aller trop loin dans la confrontation verbale.

**Conseil clé** : Utiliser ta profondeur pour des échanges transformateurs, pas destructeurs.""",
        'weekly_advice': {
            'week_1': "Engage une conversation profonde avec quelqu'un de confiance.",
            'week_2': "Observe plus, parle moins. Les silences révèlent.",
            'week_3': "Évite les joutes verbales qui ne mènent nulle part.",
            'week_4': "Intègre les révélations de ce mois."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vision partagée**

Ta Lune Bélier en Maison 3 bouillonne d'idées, et l'ascendant Sagittaire les projette vers l'horizon. Tu communiques avec enthousiasme, tu veux transmettre une vision, inspirer.

**Domaine activé** : Maison 3 — Communication, apprentissages, échanges. Tu es attiré·e par les grands sujets, les idées philosophiques, les discussions qui élèvent.

**Ton approche instinctive** : Tu vois grand, tu parles grand. Les détails t'ennuient, tu préfères les synthèses audacieuses. Ton optimisme est contagieux.

**Tensions possibles** : Tu peux exagérer ou promettre plus que tu ne peux tenir. Les généralisations peuvent manquer de nuance.

**Conseil clé** : Partager ta vision en restant ancré·e dans le réel.""",
        'weekly_advice': {
            'week_1': "Partage une idée qui t'inspire avec ton entourage.",
            'week_2': "Apprends quelque chose qui élargit ta perspective.",
            'week_3': "Vérifie les détails de ce que tu affirmes.",
            'week_4': "Quelle vision emportes-tu de ce mois ?"
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Parole structurée**

Ta Lune Bélier en Maison 3 veut s'exprimer avec urgence, mais l'ascendant Capricorne structure cette impulsion. Tu communiques de manière réfléchie, stratégique, avec un objectif.

**Domaine activé** : Maison 3 — Communication, apprentissages, échanges quotidiens. Tu privilégies les échanges utiles, les conversations qui font avancer les choses.

**Ton approche instinctive** : Tu pèses tes mots, tu réfléchis à leur impact. Cette maîtrise peut sembler froide mais elle est efficace.

**Tensions possibles** : Tu peux retenir des choses importantes par prudence excessive. L'impulsivité Bélier se heurte à la réserve Capricorne.

**Conseil clé** : Communiquer avec stratégie sans perdre ta spontanéité.""",
        'weekly_advice': {
            'week_1': "Définis un objectif de communication pour ce cycle.",
            'week_2': "Exprime-toi dans un contexte professionnel ou formel.",
            'week_3': "Assouplit ta communication sans perdre en sérieux.",
            'week_4': "Évalue l'efficacité de tes échanges ce mois."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Idées originales**

Ta Lune Bélier en Maison 3 bouillonne d'idées, et l'ascendant Verseau leur donne une tournure originale, avant-gardiste. Tu penses différemment et tu veux que ça se sache.

**Domaine activé** : Maison 3 — Communication, échanges, apprentissages. Tu es attiré·e par les idées nouvelles, les concepts innovants, les discussions qui sortent des sentiers battus.

**Ton approche instinctive** : Tu cherches l'angle inattendu, la perspective décalée. Tes idées peuvent surprendre ou déstabiliser.

**Tensions possibles** : Tu peux être perçu·e comme provocateur·rice ou difficile à suivre. L'originalité à tout prix peut isoler.

**Conseil clé** : Partager tes idées originales en les rendant accessibles.""",
        'weekly_advice': {
            'week_1': "Explore une idée qui te semble folle mais excitante.",
            'week_2': "Partage cette idée avec quelqu'un d'ouvert.",
            'week_3': "Traduis tes concepts en termes compréhensibles.",
            'week_4': "Quelle idée neuve emportes-tu de ce mois ?"
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Intuition exprimée**

Ta Lune Bélier en Maison 3 veut communiquer avec force, mais l'ascendant Poissons ajoute une dimension intuitive et floue. Tu exprimes ce que tu ressens plus que ce que tu penses.

**Domaine activé** : Maison 3 — Communication et environnement proche. Tes échanges ont une qualité poétique, empathique, parfois confuse.

**Ton approche instinctive** : Tu perçois les non-dits, les ambiances. Ta communication passe autant par le ressenti que par les mots. L'art, la musique peuvent être des canaux d'expression.

**Tensions possibles** : Tu peux avoir du mal à exprimer clairement ce que tu veux dire. L'impulsivité Bélier brouillée par le flou Poissons crée de la confusion.

**Conseil clé** : Traduire tes intuitions en mots clairs sans perdre leur essence.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition dans tes échanges.",
            'week_2': "Exprime quelque chose de difficile à verbaliser.",
            'week_3': "Si tu te sens incompris·e, reformule autrement.",
            'week_4': "Qu'as-tu compris sur ta manière de communiquer ?"
        }
    }
]

if __name__ == "__main__":
    asyncio.run(insert_batch(BATCH))
    print(f"\n[BATCH] Aries M3 complete - 36/1728")
