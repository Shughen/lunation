"""Batch complet: Capricorn - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Ambition en action**

Ta Lune en Capricorne en Maison 1 te pousse à bâtir ton identité avec sérieux et discipline. Ton Ascendant Bélier ajoute une urgence à cette construction : tu veux des résultats maintenant, sans attendre. L'alliance de la terre cardinale et du feu cardinal crée une force d'accomplissement impressionnante.

**Domaine activé** : Maison 1 — Ton identité personnelle, ton image, ta manière de te présenter au monde. Tu cherches à montrer ta compétence, ton professionnalisme, ta maturité. L'apparence que tu projettes compte énormément ce mois-ci.

**Ton approche instinctive** : L'Ascendant Bélier te fait foncer vers tes objectifs sans hésitation. Tu veux prouver ta valeur par l'action immédiate. Cette impulsivité peut accélérer ta progression si elle reste stratégique.

**Tensions possibles** : L'impatience du Bélier contre la prudence du Capricorne crée des frictions. Tu risques de te frustrer si les résultats ne viennent pas assez vite ou si tu dois respecter des étapes que tu juges inutiles.

**Conseil clé** : Canaliser ton énergie vers des objectifs ambitieux mais réalistes, en gardant le rythme soutenu du Bélier tout en respectant la structure du Capricorne.""",
        'weekly_advice': {
            'week_1': "Définis un objectif personnel clair et commence immédiatement.",
            'week_2': "Maintiens la discipline même quand l'enthousiasme retombe.",
            'week_3': "Ajuste ta stratégie sans perdre de vue le sommet.",
            'week_4': "Célèbre les étapes franchies et prépare l'ascension suivante."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Force constructive**

Ta Lune en Capricorne en Maison 1 te demande de te construire avec sérieux et méthode. Ton Ascendant Taureau apporte une patience naturelle et une détermination inébranlable. Double terre : tu bâtis ton identité pierre par pierre, avec une stabilité remarquable.

**Domaine activé** : Maison 1 — Qui tu es, comment tu te présentes, ton image personnelle. Tu cherches à incarner la fiabilité, la solidité, la compétence durable. Chaque geste compte dans cette construction de soi.

**Ton approche instinctive** : Le Taureau te fait avancer lentement mais sûrement. Tu refuses de brûler les étapes. Cette patience renforce le Capricorne qui apprécie la progression méthodique et les fondations solides.

**Tensions possibles** : Le double ancrage terre peut créer de la rigidité. Tu risques de t'enfermer dans une routine trop stricte ou de résister au changement même quand il serait bénéfique.

**Conseil clé** : Rester ouvert·e à l'évolution tout en maintenant ta discipline. La stabilité n'exclut pas l'adaptation.""",
        'weekly_advice': {
            'week_1': "Pose des bases solides pour ton développement personnel.",
            'week_2': "Avance avec régularité, sans précipitation.",
            'week_3': "Consolide ce qui fonctionne déjà bien.",
            'week_4': "Apprécie la solidité de ce que tu as construit."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Sérieux adaptable**

Ta Lune en Capricorne en Maison 1 cherche à structurer ton identité avec discipline et rigueur. Ton Ascendant Gémeaux introduit de la flexibilité, de la curiosité, une touche de légèreté. Le défi : allier profondeur et agilité.

**Domaine activé** : Maison 1 — Ton identité, ton image personnelle. Tu veux être pris·e au sérieux (Capricorne) tout en restant accessible et intéressant·e (Gémeaux). Cette dualité peut créer une présence unique.

**Ton approche instinctive** : Le Gémeaux te fait explorer différentes facettes de toi-même, tester plusieurs approches. Cette souplesse peut frustrer le Capricorne qui préfère une voie claire et linéaire.

**Tensions possibles** : Tiraillement entre engagement profond et multiplication des intérêts. Tu risques de paraître soit trop rigide, soit pas assez constant·e. Trouver l'équilibre demande de la conscience.

**Conseil clé** : Utiliser ta versatilité pour enrichir ta construction personnelle, pas pour la disperser. Sérieux ne veut pas dire monotone.""",
        'weekly_advice': {
            'week_1': "Identifie les compétences variées qui servent ton objectif principal.",
            'week_2': "Expérimente différentes approches tout en gardant le cap.",
            'week_3': "Communique ta vision avec clarté et professionnalisme.",
            'week_4': "Intègre ce que tu as appris dans une identité cohérente."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Force sensible**

Ta Lune en Capricorne en Maison 1 te pousse à construire une identité forte, structurée, responsable. Ton Ascendant Cancer oppose douceur et vulnérabilité à cette armure. L'axe Cancer-Capricorne activé : tension entre le besoin de protéger et celui d'accomplir.

**Domaine activé** : Maison 1 — Ton identité personnelle. Tu cherches à incarner la compétence et la maturité tout en restant humain·e et accessible. Cette polarité peut créer une présence très équilibrée si tu l'acceptes.

**Ton approche instinctive** : Le Cancer te ramène à tes émotions, tes besoins affectifs, ta sensibilité. Cette tendance peut sembler contraire au Capricorne qui veut rester professionnel et maîtrisé.

**Tensions possibles** : Conflit entre montrer ta vulnérabilité et maintenir ton autorité. Tu peux alterner entre des moments de grande ouverture émotionnelle et de fermeture totale.

**Conseil clé** : Intégrer ta sensibilité comme une force, pas comme une faiblesse. L'autorité authentique inclut l'humanité.""",
        'weekly_advice': {
            'week_1': "Reconnais tes besoins émotionnels sans les juger.",
            'week_2': "Montre ta force sans masquer ta douceur.",
            'week_3': "Équilibre ambition professionnelle et bien-être personnel.",
            'week_4': "Célèbre ta capacité à être à la fois fort·e et sensible."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Majesté disciplinée**

Ta Lune en Capricorne en Maison 1 cherche à bâtir une identité solide, crédible, respectable. Ton Ascendant Lion ajoute du charisme, de la prestance, un désir d'être vu·e et reconnu·e. L'alliance de la discipline et de l'éclat.

**Domaine activé** : Maison 1 — Ton image personnelle, ton identité. Tu veux incarner l'excellence (Capricorne) tout en rayonnant (Lion). Cette combinaison peut créer une présence magnétique et autoritaire.

**Ton approche instinctive** : Le Lion te pousse à briller, à te mettre en avant avec confiance. Cette visibilité sert ton Capricorne si elle repose sur de vraies compétences, mais peut sembler vaine si elle manque de substance.

**Tensions possibles** : L'ego du Lion contre l'humilité du Capricorne. Tu risques d'osciller entre fierté excessive et autocritique sévère. Trouver la juste estime de soi demande du travail.

**Conseil clé** : Laisser ta lumière naturelle éclairer tes réalisations concrètes. Être visible et compétent ne s'oppose pas.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui mérite vraiment d'être célébré en toi.",
            'week_2': "Travaille avec excellence sans chercher constamment l'applaudissement.",
            'week_3': "Assume ta légitimité quand tu as produit des résultats.",
            'week_4': "Rayonne en sachant que ton autorité repose sur du solide."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfection pragmatique**

Ta Lune en Capricorne en Maison 1 te demande de construire une identité fiable et professionnelle. Ton Ascendant Vierge ajoute du perfectionnisme, de l'analyse, un souci du détail. Double terre : une construction méthodique et rigoureuse de toi-même.

**Domaine activé** : Maison 1 — Ton identité personnelle, ton image. Tu veux être irréprochable, compétent·e, utile. Chaque aspect de ta présentation est pensé avec soin et amélioration continue.

**Ton approche instinctive** : La Vierge te fait analyser chaque détail de ta progression. Cette minutie sert le Capricorne qui apprécie la rigueur, mais peut devenir paralysante si elle verse dans l'autocritique excessive.

**Tensions possibles** : Le double perfectionnisme terre risque de créer des standards impossibles à atteindre. Tu peux te bloquer en cherchant à être parfait·e avant même de commencer.

**Conseil clé** : Viser l'excellence progressive, pas la perfection immédiate. La compétence se construit par la pratique, pas par l'attente du moment idéal.""",
        'weekly_advice': {
            'week_1': "Définis des critères d'excellence réalistes pour toi.",
            'week_2': "Améliore un aspect à la fois, sans tout vouloir changer.",
            'week_3': "Accepte les imperfections comme partie du processus.",
            'week_4': "Reconnais le chemin parcouru, même s'il reste du travail."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Autorité harmonieuse**

Ta Lune en Capricorne en Maison 1 te pousse à construire une identité forte, structurée, respectable. Ton Ascendant Balance apporte diplomatie, recherche d'harmonie, sensibilité esthétique. Le défi : allier autorité et douceur.

**Domaine activé** : Maison 1 — Ton image personnelle, ton identité. Tu cherches à être pris·e au sérieux tout en restant agréable et équilibré·e. Cette alliance peut créer une présence à la fois forte et accessible.

**Ton approche instinctive** : La Balance te fait chercher l'approbation, le consensus, l'harmonie relationnelle. Cette tendance peut adoucir le Capricorne trop austère ou, au contraire, créer des compromis qui affaiblissent ton autorité.

**Tensions possibles** : Tiraillement entre affirmation de soi et souci de plaire. Tu risques de sacrifier tes objectifs pour maintenir la paix ou, inversement, de paraître froid·e en cherchant à rester professionnel·le.

**Conseil clé** : Construire une autorité bienveillante. On peut être ferme et aimable, structuré·e et gracieux·se.""",
        'weekly_advice': {
            'week_1': "Affirme tes objectifs sans craindre de déplaire.",
            'week_2': "Maintiens ton cap tout en restant à l'écoute.",
            'week_3': "Trouve l'équilibre entre fermeté et flexibilité.",
            'week_4': "Apprécie ta capacité à diriger avec élégance."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Puissance stratégique**

Ta Lune en Capricorne en Maison 1 cherche à bâtir une identité solide, compétente, respectable. Ton Ascendant Scorpion ajoute intensité émotionnelle, détermination absolue, perception aiguë. L'alliance de la structure et de la transformation.

**Domaine activé** : Maison 1 — Ton identité personnelle. Tu veux te construire en profondeur, transformer qui tu es à la racine. Cette combinaison crée une présence magnétique et intimidante.

**Ton approche instinctive** : Le Scorpion te pousse à creuser sous la surface, à ne jamais te contenter de l'apparence. Cette profondeur renforce le Capricorne qui apprécie les fondations solides et les transformations durables.

**Tensions possibles** : L'intensité émotionnelle du Scorpion contre le contrôle du Capricorne. Tu risques de refouler des émotions puissantes au nom du professionnalisme, créant une pression interne dangereuse.

**Conseil clé** : Intégrer ta profondeur émotionnelle dans ta construction personnelle. La vraie force inclut la capacité à ressentir intensément.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit vraiment changer en toi.",
            'week_2': "Plonge dans le travail de transformation sans esquiver.",
            'week_3': "Canalise ton intensité vers des objectifs constructifs.",
            'week_4': "Reconnais la puissance de ce que tu es en train de devenir."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vision pragmatique**

Ta Lune en Capricorne en Maison 1 te demande de construire ton identité avec discipline et méthode. Ton Ascendant Sagittaire apporte optimisme, vision large, soif d'expansion. La rencontre entre le sommet de la montagne et l'horizon lointain.

**Domaine activé** : Maison 1 — Ton image personnelle, ton identité. Tu veux incarner à la fois la sagesse (Capricorne) et l'aventure (Sagittaire). Cette alliance peut créer une présence inspirante et crédible.

**Ton approche instinctive** : Le Sagittaire te fait voir grand, rêver loin, chercher le sens profond. Cette vision peut dynamiser le Capricorne trop prudent ou, au contraire, créer des objectifs irréalistes qui découragent.

**Tensions possibles** : L'optimisme du Sagittaire contre le réalisme du Capricorne. Tu risques d'alterner entre enthousiasme naïf et pessimisme prudent sans trouver l'équilibre juste.

**Conseil clé** : Rêver grand tout en marchant avec méthode. Les sommets se gravissent un pas à la fois, mais il faut d'abord les apercevoir.""",
        'weekly_advice': {
            'week_1': "Définis une vision inspirante mais réalisable pour toi.",
            'week_2': "Décompose cette vision en étapes concrètes.",
            'week_3': "Avance avec discipline sans perdre l'enthousiasme.",
            'week_4': "Célèbre le chemin parcouru vers ton horizon."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Ambition pure**

Ta Lune en Capricorne en Maison 1 avec Ascendant Capricorn crée une triple concentration de terre cardinale sur ton identité. L'énergie est dense, concentrée, tournée vers la réalisation concrète. Tu incarnes l'accomplissement discipliné.

**Domaine activé** : Maison 1 — Ton identité personnelle est au cœur de tout. Tu cherches à te construire avec le plus haut niveau d'exigence et de professionnalisme. Rien de superficiel n'est toléré.

**Ton approche instinctive** : Triple Capricorne : tu avances avec méthode, patience, détermination absolue. Chaque étape est pesée, chaque décision calculée. Cette rigueur peut créer des résultats impressionnants mais aussi une lourde pression.

**Tensions possibles** : Le triple perfectionnisme peut devenir écrasant. Tu risques de te surmener, de t'autocritiquer sévèrement, de ne jamais te sentir assez accompli·e.

**Conseil clé** : Se rappeler que la construction prend du temps. La patience avec soi-même est aussi une forme de discipline.""",
        'weekly_advice': {
            'week_1': "Fixe-toi un objectif ambitieux mais bienveillant.",
            'week_2': "Maintiens ta discipline sans devenir tyrannique.",
            'week_3': "Reconnaît les progrès, même s'ils semblent modestes.",
            'week_4': "Accorde-toi le respect que tu mérites pour ton travail."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Structure innovante**

Ta Lune en Capricorne en Maison 1 cherche à bâtir une identité solide et crédible. Ton Ascendant Verseau ajoute originalité, indépendance d'esprit, refus des conventions. Le défi : allier tradition et innovation.

**Domaine activé** : Maison 1 — Ton image personnelle, ton identité. Tu veux être pris·e au sérieux (Capricorne) tout en affirmant ton unicité (Verseau). Cette combinaison peut créer une présence à la fois professionnelle et fascinante.

**Ton approche instinctive** : Le Verseau te pousse à faire les choses différemment, à remettre en question les méthodes établies. Cette originalité peut frustrer le Capricorne qui valorise les structures éprouvées.

**Tensions possibles** : Conflit entre conformité professionnelle et authenticité personnelle. Tu risques de te sentir écartelé·e entre le besoin d'être reconnu·e par le système et celui de le transcender.

**Conseil clé** : Innover dans le cadre de l'excellence. On peut être à la fois rigoureux·se et visionnaire.""",
        'weekly_advice': {
            'week_1': "Identifie où ton approche unique peut créer de la valeur.",
            'week_2': "Construis ta crédibilité en respectant certaines règles du jeu.",
            'week_3': "Apporte ton originalité sans rejeter toute structure.",
            'week_4': "Célèbre ta capacité à être professionnel·le et authentique."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Force intuitive**

Ta Lune en Capricorne en Maison 1 te demande de construire une identité structurée et compétente. Ton Ascendant Poissons apporte sensibilité, intuition, fluidité émotionnelle. La rencontre entre la montagne et l'océan.

**Domaine activé** : Maison 1 — Ton identité personnelle. Tu cherches à incarner à la fois la compétence (Capricorne) et la compassion (Poissons). Cette alliance peut créer une présence à la fois forte et douce.

**Ton approche instinctive** : Les Poissons te font ressentir profondément, te connecter aux autres, naviguer par intuition. Cette fluidité peut adoucir le Capricorne trop rigide ou créer une confusion qui retarde l'action.

**Tensions possibles** : Le besoin de structure contre le besoin de lâcher prise. Tu risques d'alterner entre contrôle strict et abandon total sans trouver l'ancrage juste.

**Conseil clé** : Construire avec flexibilité. Les fondations peuvent être solides tout en laissant place à l'adaptation.""",
        'weekly_advice': {
            'week_1': "Définis tes objectifs en restant à l'écoute de ton intuition.",
            'week_2': "Avance avec méthode sans ignorer tes ressentis.",
            'week_3': "Équilibre discipline et douceur envers toi-même.",
            'week_4': "Apprécie ta capacité à être fort·e et sensible."
        }
    },

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Patrimoine conquis**

Ta Lune en Capricorne active ta Maison 2 : ressources, sécurité matérielle, valeurs. Ton Ascendant Bélier veut conquérir cette sécurité rapidement, par l'action directe. L'alliance de la stratégie à long terme et de l'audace immédiate.

**Domaine activé** : Maison 2 — Tes finances, possessions, ce qui a de la valeur pour toi. Tu cherches à bâtir un patrimoine solide tout en voulant des résultats rapides. Cette tension peut être productive.

**Ton approche instinctive** : Le Bélier te pousse à saisir les opportunités financières avec audace. Cette impulsivité peut servir le Capricorne si elle reste calculée, mais peut créer des pertes si elle devient pure témérité.

**Tensions possibles** : Impatience financière contre prudence stratégique. Tu risques d'alterner entre coups de poker et conservatisme excessif sans trouver la juste prise de risque.

**Conseil clé** : Agir avec audace sur des bases solides. L'ambition financière doit s'appuyer sur une vraie compréhension du terrain.""",
        'weekly_advice': {
            'week_1': "Identifie une opportunité financière qui mérite l'audace.",
            'week_2': "Lance-toi après avoir vérifié les fondamentaux.",
            'week_3': "Maintiens l'élan même si les résultats tardent un peu.",
            'week_4': "Consolide ce que tu as gagné avant de repartir."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Richesse construite**

Ta Lune en Capricorne en Maison 2 cherche à bâtir une sécurité matérielle durable. Ton Ascendant Taureau, maître naturel de cette maison, renforce cette orientation. Double terre sur les ressources : une construction patrimoniale méthodique et solide.

**Domaine activé** : Maison 2 — Argent, possessions, valeurs matérielles. Tu cherches la stabilité financière par l'accumulation patiente et la gestion rigoureuse. Chaque euro compte et se capitalise.

**Ton approche instinctive** : Le Taureau te fait avancer lentement mais sûrement vers la prospérité. Tu refuses les raccourcis risqués. Cette patience renforce le Capricorne qui valorise la croissance durable.

**Tensions possibles** : Le double ancrage terre peut créer de l'avarice ou une peur excessive de la perte. Tu risques de manquer des opportunités par excès de prudence.

**Conseil clé** : Investir intelligemment sans thésauriser par peur. La vraie sécurité vient de la croissance maîtrisée, pas du gel total.""",
        'weekly_advice': {
            'week_1': "Évalue ta situation financière avec lucidité.",
            'week_2': "Mets en place une stratégie d'épargne ou d'investissement.",
            'week_3': "Reste patient·e, la croissance prend du temps.",
            'week_4': "Apprécie ce que tu as construit financièrement."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Valeur diversifiée**

Ta Lune en Capricorne en Maison 2 veut structurer tes ressources avec rigueur. Ton Ascendant Gémeaux cherche à multiplier les sources de revenus, à diversifier, à explorer. Le défi : allier stabilité et flexibilité financière.

**Domaine activé** : Maison 2 — Tes finances, tes valeurs matérielles. Tu cherches à la fois la sécurité (Capricorne) et la variété (Gémeaux). Cette combinaison peut créer un portefeuille diversifié et résilient.

**Ton approche instinctive** : Le Gémeaux te fait explorer plusieurs pistes financières à la fois. Cette diversification peut sécuriser le Capricorne ou, au contraire, disperser ton énergie sans créer de vraie richesse.

**Tensions possibles** : Multiplication des petits projets contre concentration sur une vraie croissance. Tu risques de papillonner financièrement sans construire de fondations solides.

**Conseil clé** : Diversifier intelligemment sans te disperser. Plusieurs sources de revenus, oui ; éparpillement improductif, non.""",
        'weekly_advice': {
            'week_1': "Identifie 2-3 sources de revenus complémentaires viables.",
            'week_2': "Développe chacune avec méthode, pas au hasard.",
            'week_3': "Évalue ce qui rapporte vraiment et ce qui distrait.",
            'week_4': "Consolide les flux positifs, coupe les pertes de temps."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sécurité émotionnelle**

Ta Lune en Capricorne en Maison 2 cherche la stabilité matérielle par la stratégie. Ton Ascendant Cancer lie cette sécurité à ton bien-être émotionnel. L'axe Cancer-Capricorne activé : tension entre protection affective et ambition matérielle.

**Domaine activé** : Maison 2 — Tes ressources financières. Pour toi, l'argent n'est pas qu'un chiffre : c'est un filet de sécurité émotionnelle. Cette dimension affective peut motiver ou paralyser.

**Ton approche instinctive** : Le Cancer te fait chercher la sécurité matérielle pour protéger tes proches et toi-même. Cette tendance renforce le Capricorne responsable mais peut créer une anxiété financière excessive.

**Tensions possibles** : Peur de manquer contre besoin de générosité. Tu risques d'alterner entre épargne anxieuse et dépenses émotionnelles impulsives.

**Conseil clé** : Construire une vraie sécurité financière apaise l'anxiété. Travailler sur la relation émotionnelle à l'argent est aussi important que de gagner plus.""",
        'weekly_advice': {
            'week_1': "Identifie tes vrais besoins de sécurité matérielle.",
            'week_2': "Mets en place des habitudes financières rassurantes.",
            'week_3': "Équilibre épargne de sécurité et qualité de vie présente.",
            'week_4': "Apprécie ce que tu as sans tomber dans l'anxiété du manque."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Prospérité visible**

Ta Lune en Capricorne en Maison 2 cherche à bâtir un patrimoine solide et respectable. Ton Ascendant Lion veut que cette richesse soit visible, reconnue, admirée. L'alliance de la construction patiente et de l'éclat.

**Domaine activé** : Maison 2 — Tes ressources financières, tes possessions. Tu veux accumuler de la richesse (Capricorne) mais aussi la montrer, en jouir, qu'elle reflète ton statut (Lion).

**Ton approche instinctive** : Le Lion te pousse à investir dans ce qui brille, ce qui impressionne. Cette tendance peut servir le Capricorne si elle reste stratégique, mais peut créer des dépenses ostentatoires qui nuisent à l'accumulation.

**Tensions possibles** : Besoin d'épargner contre besoin de profiter. Tu risques de culpabiliser quand tu dépenses ou de te frustrer quand tu économises.

**Conseil clé** : Trouver l'équilibre entre construction patrimoniale et jouissance légitime. On peut à la fois investir pour demain et célébrer aujourd'hui.""",
        'weekly_advice': {
            'week_1': "Définis ce qui mérite vraiment ton investissement financier.",
            'week_2': "Construis ta richesse avec méthode et fierté.",
            'week_3': "Autorise-toi une dépense plaisir si tu as bien géré.",
            'week_4': "Apprécie à la fois ton épargne et tes acquisitions de qualité."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Gestion parfaite**

Ta Lune en Capricorne en Maison 2 veut structurer tes finances avec rigueur. Ton Ascendant Vierge ajoute analyse détaillée, optimisation, amélioration continue. Double terre : une gestion financière exemplaire et méthodique.

**Domaine activé** : Maison 2 — Tes ressources matérielles. Tu cherches à optimiser chaque euro, à maximiser l'efficacité de ton patrimoine. La précision est ta force.

**Ton approche instinctive** : La Vierge te fait analyser chaque dépense, chaque investissement avec minutie. Cette rigueur renforce le Capricorne qui apprécie la discipline financière.

**Tensions possibles** : Le double perfectionnisme peut créer de l'anxiété financière paralysante. Tu risques de sur-analyser au point de rater des opportunités simples.

**Conseil clé** : Viser l'excellence financière sans tomber dans l'obsession du contrôle. Parfois, "assez bon" est vraiment assez bon.""",
        'weekly_advice': {
            'week_1': "Fais un audit complet de ta situation financière.",
            'week_2': "Optimise un poste de dépense ou une source de revenu.",
            'week_3': "Laisse certaines imperfections mineures tranquilles.",
            'week_4': "Reconnais l'excellence de ta gestion sans chercher la perfection absolue."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre financier**

Ta Lune en Capricorne en Maison 2 cherche la stabilité matérielle par la planification. Ton Ascendant Balance veut que cette gestion financière soit harmonieuse, équitable, agréable. Le défi : allier rigueur et douceur.

**Domaine activé** : Maison 2 — Tes ressources, tes valeurs matérielles. Tu cherches une prospérité qui ne sacrifie ni la sécurité ni la qualité de vie. L'équilibre compte autant que le montant.

**Ton approche instinctive** : La Balance te fait chercher le juste milieu entre épargne et dépense. Cette modération peut stabiliser le Capricorne ou créer de l'indécision qui retarde les décisions financières importantes.

**Tensions possibles** : Hésitation entre différentes options d'investissement. Tu risques de paralyser en pesant trop longtemps le pour et le contre.

**Conseil clé** : Décider avec sagesse, mais décider quand même. L'équilibre parfait n'existe pas, mais l'action équilibrée oui.""",
        'weekly_advice': {
            'week_1': "Évalue tes priorités financières avec honnêteté.",
            'week_2': "Prends une décision financière importante sans ruminer.",
            'week_3': "Maintiens l'équilibre entre épargne et qualité de vie.",
            'week_4': "Apprécie l'harmonie de ta situation financière actuelle."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Richesse transformée**

Ta Lune en Capricorne en Maison 2 veut bâtir un patrimoine solide et durable. Ton Ascendant Scorpion ajoute intensité, stratégie profonde, capacité de transformation financière radicale. L'alliance de la patience et de la puissance.

**Domaine activé** : Maison 2 — Tes ressources matérielles. Tu ne cherches pas juste la stabilité financière : tu veux transformer ta relation à l'argent, au pouvoir, à la valeur en profondeur.

**Ton approche instinctive** : Le Scorpion te pousse à creuser sous la surface financière, à comprendre les vrais mécanismes de richesse. Cette profondeur renforce le Capricorne stratège.

**Tensions possibles** : Obsession du contrôle financier. Tu risques de devenir si intensément focalisé·e sur l'argent que cela crée de l'anxiété ou des comportements extrêmes.

**Conseil clé** : Utiliser ton intensité pour construire du patrimoine, pas pour développer de l'anxiété. Le pouvoir financier bien géré libère, il n'emprisonne pas.""",
        'weekly_advice': {
            'week_1': "Identifie une transformation financière profonde à opérer.",
            'week_2': "Plonge dans la stratégie sans céder à l'obsession.",
            'week_3': "Avance avec détermination vers ta sécurité matérielle.",
            'week_4': "Reconnais le pouvoir que tu gagnes par ta maîtrise financière."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Prospérité expansive**

Ta Lune en Capricorne en Maison 2 cherche la sécurité matérielle par la structure. Ton Ascendant Sagittaire veut croître, explorer, investir dans l'aventure. Le défi : allier prudence financière et vision ambitieuse.

**Domaine activé** : Maison 2 — Tes ressources financières. Tu veux à la fois la sécurité (Capricorne) et la croissance audacieuse (Sagittaire). Cette tension peut créer une expansion maîtrisée.

**Ton approche instinctive** : Le Sagittaire te fait voir les opportunités lointaines, investir dans ta croissance future. Cette vision peut dynamiser le Capricorne trop conservateur ou créer des paris trop optimistes.

**Tensions possibles** : Optimisme financier contre réalisme prudent. Tu risques d'alterner entre enthousiasme naïf et pessimisme paralysant.

**Conseil clé** : Investir dans ta croissance avec une vraie stratégie. Rêver grand financièrement, oui ; parier aveuglément, non.""",
        'weekly_advice': {
            'week_1': "Identifie une opportunité de croissance financière réelle.",
            'week_2': "Évalue les risques avec lucidité, pas juste avec enthousiasme.",
            'week_3': "Investis dans ton expansion en gardant un filet de sécurité.",
            'week_4': "Célèbre la croissance accomplie, même modeste."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Patrimoine pur**

Ta Lune en Capricorne en Maison 2 avec Ascendant Capricorne crée une triple concentration sur la construction matérielle. L'énergie est dense, stratégique, tournée vers l'accumulation disciplinée et la sécurité à long terme.

**Domaine activé** : Maison 2 — Tes ressources financières sont au cœur de tout ce mois-ci. Tu cherches à bâtir un patrimoine solide avec le plus haut niveau de rigueur et de responsabilité.

**Ton approche instinctive** : Triple Capricorne : chaque décision financière est pesée, calculée, orientée vers le long terme. Cette discipline peut créer une vraie richesse mais aussi une relation tendue à l'argent.

**Tensions possibles** : Austérité excessive, difficulté à profiter de ce que tu gagnes. Tu risques de t'épuiser en épargnant trop sans jamais t'autoriser à jouir de ta prospérité.

**Conseil clé** : Construire ta sécurité financière sans te priver de vivre. La vraie sagesse matérielle inclut la capacité à profiter responsablement.""",
        'weekly_advice': {
            'week_1': "Définis un objectif financier ambitieux mais sain.",
            'week_2': "Avance avec discipline vers ta sécurité matérielle.",
            'week_3': "Autorise-toi une petite dépense plaisir sans culpabilité.",
            'week_4': "Apprécie le chemin financier parcouru avec fierté."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Richesse innovante**

Ta Lune en Capricorne en Maison 2 cherche la stabilité financière par la méthode éprouvée. Ton Ascendant Verseau veut innover, expérimenter, créer de la valeur autrement. Le défi : allier tradition et innovation financière.

**Domaine activé** : Maison 2 — Tes ressources matérielles. Tu cherches à la fois la sécurité (Capricorne) et l'originalité (Verseau) dans ta manière de générer de la richesse.

**Ton approche instinctive** : Le Verseau te pousse à explorer des sources de revenus non conventionnelles, à créer de la valeur différemment. Cette originalité peut frustrer le Capricorne qui valorise les chemins éprouvés.

**Tensions possibles** : Conflit entre méthodes financières traditionnelles et approches avant-gardistes. Tu risques de te sentir tiraillé·e entre conformité et innovation.

**Conseil clé** : Innover financièrement en gardant des bases solides. On peut être original·e et responsable.""",
        'weekly_advice': {
            'week_1': "Identifie une manière originale mais viable de créer de la valeur.",
            'week_2': "Teste ton approche innovante sans mettre ta sécurité en danger.",
            'week_3': "Équilibre nouveauté et prudence dans tes décisions financières.",
            'week_4': "Célèbre ta capacité à être à la fois sage et visionnaire."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Valeur intuitive**

Ta Lune en Capricorne en Maison 2 veut structurer tes ressources avec rigueur. Ton Ascendant Poissons apporte intuition financière, générosité, fluidité dans la relation à l'argent. La rencontre entre stratégie et lâcher-prise.

**Domaine activé** : Maison 2 — Tes finances, tes valeurs matérielles. Tu cherches à la fois la sécurité (Capricorne) et la confiance en l'univers (Poissons). Cette combinaison peut créer une prospérité sereine.

**Ton approche instinctive** : Les Poissons te font naviguer financièrement par intuition, parfois au détriment de la logique. Cette fluidité peut adoucir le Capricorne trop rigide ou créer de l'imprévoyance dangereuse.

**Tensions possibles** : Planification rigoureuse contre lâcher-prise financier. Tu risques d'alterner entre contrôle anxieux et générosité imprudente.

**Conseil clé** : Écouter ton intuition financière tout en maintenant une structure de base. La sagesse matérielle combine raison et ressenti.""",
        'weekly_advice': {
            'week_1': "Fais le point sur ta situation financière avec lucidité et douceur.",
            'week_2': "Mets en place une structure qui rassure sans rigidifier.",
            'week_3': "Fais confiance à ton intuition pour une décision bien informée.",
            'week_4': "Apprécie ta capacité à être responsable et généreux·se."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Communication stratégique**

Ta Lune en Capricorne active ta Maison 3 : communication, apprentissage, entourage proche. Ton Ascendant Bélier veut communiquer vite, direct, avec impact. L'alliance de la parole réfléchie et de l'expression audacieuse.

**Domaine activé** : Maison 3 — Tes échanges quotidiens, ton apprentissage, tes déplacements courts. Tu cherches à communiquer avec autorité (Capricorne) et spontanéité (Bélier).

**Ton approche instinctive** : Le Bélier te fait parler sans filtre, dire ce que tu penses immédiatement. Cette franchise peut servir le Capricorne qui valorise l'honnêteté, mais peut aussi créer des maladresses.

**Tensions possibles** : Impulsivité verbale contre besoin de crédibilité. Tu risques de dire des choses trop vite puis de les regretter.

**Conseil clé** : Prendre une seconde avant de parler. La spontanéité peut coexister avec la réflexion.""",
        'weekly_advice': {
            'week_1': "Identifie un sujet important sur lequel tu veux t'exprimer.",
            'week_2': "Prépare ton message avec soin avant de le délivrer.",
            'week_3': "Communique avec assurance mais aussi avec écoute.",
            'week_4': "Apprécie l'impact de tes mots cette semaine."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Parole stable**

Ta Lune en Capricorne en Maison 3 cherche à communiquer avec sérieux et fiabilité. Ton Ascendant Taureau ajoute patience, voix posée, ancrage. Double terre : une communication solide et mesurée.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage. Tu veux que tes mots aient du poids, qu'ils construisent quelque chose de durable. Les bavardages superficiels ne t'intéressent pas.

**Ton approche instinctive** : Le Taureau te fait prendre ton temps pour t'exprimer, choisir tes mots avec soin. Cette lenteur renforce le Capricorne qui valorise la communication réfléchie.

**Tensions possibles** : Lenteur excessive dans les échanges. Tu risques de frustrer les autres par ton rythme prudent ou de manquer des opportunités qui demandent rapidité.

**Conseil clé** : Garder ta solidité verbale tout en restant réactif·ve quand nécessaire.""",
        'weekly_advice': {
            'week_1': "Prends le temps de formuler clairement ce qui compte.",
            'week_2': "Communique avec calme et assurance.",
            'week_3': "Accélère un peu si une situation demande rapidité.",
            'week_4': "Apprécie la fiabilité de ta parole."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Expertise partagée**

Ta Lune en Capricorne en Maison 3 veut communiquer avec compétence et professionnalisme. Ton Ascendant Gémeaux, maître naturel de cette maison, adore échanger, apprendre, partager. Le défi : allier profondeur et légèreté.

**Domaine activé** : Maison 3 — Communication, apprentissage, entourage. Tu cherches à la fois la rigueur (Capricorne) et la variété (Gémeaux) dans tes échanges.

**Ton approche instinctive** : Le Gémeaux te fait multiplier les conversations, les apprentissages, les connexions. Cette curiosité peut enrichir le Capricorne ou créer une dispersion qui nuit à l'expertise.

**Tensions possibles** : Multiplicité des intérêts contre besoin de spécialisation. Tu risques de papillonner intellectuellement sans développer de vraie maîtrise.

**Conseil clé** : Explorer largement mais approfondir stratégiquement. La curiosité doit servir l'expertise, pas la remplacer.""",
        'weekly_advice': {
            'week_1': "Identifie 2-3 sujets qui méritent ton approfondissement.",
            'week_2': "Apprends avec méthode, pas juste par curiosité passagère.",
            'week_3': "Partage ton expertise en cours de construction.",
            'week_4': "Apprécie ce que tu maîtrises mieux qu'avant."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Communication protectrice**

Ta Lune en Capricorne en Maison 3 cherche à communiquer avec autorité et structure. Ton Ascendant Cancer ajoute sensibilité, protection, dimension affective aux échanges. L'axe Cancer-Capricorne activé : tension entre professionnalisme et intimité.

**Domaine activé** : Maison 3 — Tes échanges quotidiens, ton entourage proche. Tu veux que ta parole soit à la fois compétente (Capricorne) et chaleureuse (Cancer).

**Ton approche instinctive** : Le Cancer te fait communiquer avec douceur, créer des liens affectifs par les mots. Cette tendresse peut humaniser le Capricorne trop formel ou créer une confusion entre proche et professionnel.

**Tensions possibles** : Oscillation entre distance professionnelle et proximité émotionnelle. Tu risques de ne pas savoir quel ton adopter selon les situations.

**Conseil clé** : Adapter ton registre de communication au contexte sans renier ni ta compétence ni ton humanité.""",
        'weekly_advice': {
            'week_1': "Identifie avec qui tu peux être chaleureux·se et avec qui rester formel·le.",
            'week_2': "Communique avec professionnalisme sans froideur.",
            'week_3': "Autorise-toi à montrer ta sensibilité quand c'est approprié.",
            'week_4': "Apprécie ta capacité à être fort·e et doux·ce en paroles."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Parole d'autorité**

Ta Lune en Capricorne en Maison 3 veut communiquer avec compétence et crédibilité. Ton Ascendant Lion ajoute charisme, présence vocale, désir d'être entendu·e et admiré·e. L'alliance de la substance et du style.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage. Tu veux que ta parole ait de l'impact, qu'elle soit à la fois respectée (Capricorne) et remarquée (Lion).

**Ton approche instinctive** : Le Lion te fait communiquer avec assurance, prendre la parole naturellement. Cette prestance renforce le Capricorne si elle s'appuie sur du contenu solide.

**Tensions possibles** : Ego verbal contre crédibilité réelle. Tu risques de trop en faire dans la forme au détriment du fond, ou inversement d'être trop austère.

**Conseil clé** : Laisser ta présence naturelle servir ton expertise. On peut être charismatique et compétent sans que l'un nuise à l'autre.""",
        'weekly_advice': {
            'week_1': "Identifie un sujet que tu maîtrises vraiment.",
            'week_2': "Communique dessus avec assurance et substance.",
            'week_3': "Assume ta légitimité à prendre la parole.",
            'week_4': "Apprécie l'impact de ta communication cette semaine."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision experte**

Ta Lune en Capricorne en Maison 3 cherche à communiquer avec professionnalisme. Ton Ascendant Vierge ajoute précision, analyse détaillée, souci de la justesse. Double terre : une communication d'une rigueur exemplaire.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage. Tu veux que chaque mot soit pesé, chaque information vérifiée. L'exactitude est ta marque de fabrique.

**Ton approche instinctive** : La Vierge te fait analyser, corriger, peaufiner chaque message. Cette minutie renforce le Capricorne qui valorise la communication fiable.

**Tensions possibles** : Perfectionnisme paralysant dans les échanges. Tu risques de trop réfléchir avant de parler ou d'apprendre, perdant en spontanéité et en fluidité.

**Conseil clé** : Viser l'excellence communicationnelle sans tomber dans l'obsession du mot parfait. Parfois, "assez clair" suffit.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine de connaissance à perfectionner.",
            'week_2': "Apprends ou communique avec méthode et précision.",
            'week_3': "Laisse passer quelques imperfections mineures.",
            'week_4': "Apprécie l'expertise que tu développes sans exiger la perfection absolue."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomatie stratégique**

Ta Lune en Capricorne en Maison 3 veut communiquer avec sérieux et structure. Ton Ascendant Balance ajoute diplomatie, recherche d'harmonie, élégance verbale. Le défi : allier autorité et douceur dans les échanges.

**Domaine activé** : Maison 3 — Tes communications quotidiennes. Tu cherches à être pris·e au sérieux (Capricorne) tout en maintenant des relations agréables (Balance).

**Ton approche instinctive** : La Balance te fait peser chaque mot pour éviter les conflits. Cette diplomatie peut adoucir le Capricorne trop direct ou créer des malentendus par excès de politesse.

**Tensions possibles** : Hésitation à dire les choses difficiles par souci d'harmonie. Tu risques de sacrifier la clarté pour la gentillesse.

**Conseil clé** : Dire la vérité avec élégance. On peut être direct·e et respectueux·se simultanément.""",
        'weekly_advice': {
            'week_1': "Identifie une conversation difficile à avoir.",
            'week_2': "Prépare un message clair et respectueux.",
            'week_3': "Communique avec fermeté douce.",
            'week_4': "Apprécie ta capacité à dire les choses sans blesser."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Parole profonde**

Ta Lune en Capricorne en Maison 3 cherche à communiquer avec autorité et compétence. Ton Ascendant Scorpion ajoute intensité, perception psychologique, capacité à aller sous la surface. L'alliance de la structure et de la profondeur.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage. Tu ne veux pas de conversations superficielles : chaque mot doit avoir du poids, révéler quelque chose d'essentiel.

**Ton approche instinctive** : Le Scorpion te fait creuser sous les apparences verbales, percevoir les non-dits, les enjeux cachés. Cette profondeur renforce le Capricorne stratège.

**Tensions possibles** : Intensité qui peut intimider dans les échanges quotidiens. Tu risques de chercher trop de sens là où il n'y a que bavardage ordinaire.

**Conseil clé** : Adapter ton niveau de profondeur au contexte. Toutes les conversations ne méritent pas une analyse psychologique.""",
        'weekly_advice': {
            'week_1': "Identifie les échanges qui méritent vraiment ta profondeur.",
            'week_2': "Communique avec intensité là où c'est approprié.",
            'week_3': "Accepte aussi les conversations légères sans les mépriser.",
            'week_4': "Apprécie ta capacité à communiquer en profondeur."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vision partagée**

Ta Lune en Capricorne en Maison 3 veut communiquer avec structure et expertise. Ton Ascendant Sagittaire ajoute vision large, enthousiasme pédagogique, soif de partager le sens. Le défi : allier rigueur et inspiration.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage. Tu cherches à transmettre à la fois des faits solides (Capricorne) et une vision inspirante (Sagittaire).

**Ton approche instinctive** : Le Sagittaire te fait voir grand dans tes communications, partager ta vision avec enthousiasme. Cette ampleur peut dynamiser le Capricorne ou créer des promesses trop optimistes.

**Tensions possibles** : Enthousiasme communicatif contre crédibilité factuelle. Tu risques de survendre tes idées ou, inversement, de les minimiser par prudence.

**Conseil clé** : Inspirer tout en restant ancré·e dans le réel. La vision sans substance n'engage pas durablement.""",
        'weekly_advice': {
            'week_1': "Identifie une vision que tu peux communiquer avec crédibilité.",
            'week_2': "Partage ton enthousiasme en t'appuyant sur des faits.",
            'week_3': "Maintiens l'équilibre entre inspiration et rigueur.",
            'week_4': "Apprécie ta capacité à enseigner et à élever les échanges."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Expertise pure**

Ta Lune en Capricorne en Maison 3 avec Ascendant Capricorne crée une triple concentration sur la communication professionnelle et l'apprentissage structuré. Chaque mot est pesé, chaque connaissance acquise avec méthode.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage sont au cœur de ce mois. Tu cherches à développer une vraie expertise communicable avec le plus haut niveau d'exigence.

**Ton approche instinctive** : Triple Capricorne : tu apprends et communiques avec une discipline remarquable. Cette rigueur crée de l'autorité mais peut aussi créer de la lourdeur ou de la froideur.

**Tensions possibles** : Austérité excessive dans les échanges. Tu risques de paraître trop sérieux·se, de manquer de spontanéité ou de chaleur humaine.

**Conseil clé** : Se rappeler que l'expertise se partage mieux avec un minimum de légèreté. Compétence n'exclut pas convivialité.""",
        'weekly_advice': {
            'week_1': "Définis un domaine de connaissance à maîtriser.",
            'week_2': "Apprends avec méthode et discipline.",
            'week_3': "Partage ton expertise sans te prendre trop au sérieux.",
            'week_4': "Apprécie la compétence communicative que tu développes."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Communication innovante**

Ta Lune en Capricorne en Maison 3 cherche à communiquer avec professionnalisme et structure. Ton Ascendant Verseau veut innover, expérimenter de nouveaux formats, partager des idées avant-gardistes. Le défi : allier tradition et innovation.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage. Tu cherches à la fois la crédibilité (Capricorne) et l'originalité (Verseau) dans ta manière de communiquer.

**Ton approche instinctive** : Le Verseau te pousse à expérimenter de nouvelles formes de communication, à partager des idées non conventionnelles. Cette originalité peut frustrer le Capricorne qui valorise les formats éprouvés.

**Tensions possibles** : Conflit entre conventions communicatives et désir d'innovation. Tu risques de paraître soit trop formel·le, soit trop excentrique.

**Conseil clé** : Innover dans la forme tout en gardant un fond solide. On peut être original·e et crédible.""",
        'weekly_advice': {
            'week_1': "Identifie une manière nouvelle mais sérieuse de communiquer.",
            'week_2': "Expérimente tout en maintenant ta crédibilité.",
            'week_3': "Équilibre innovation et professionnalisme.",
            'week_4': "Apprécie ta capacité à être à la fois rigoureux·se et visionnaire."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sagesse intuitive**

Ta Lune en Capricorne en Maison 3 veut communiquer avec structure et compétence. Ton Ascendant Poissons ajoute intuition, sensibilité poétique, capacité à percevoir au-delà des mots. La rencontre entre logique et ressenti.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage. Tu cherches à allier rigueur intellectuelle (Capricorne) et compréhension intuitive (Poissons).

**Ton approche instinctive** : Les Poissons te font communiquer par images, métaphores, ressentis. Cette fluidité peut enrichir le Capricorne trop sec ou créer du flou qui nuit à la clarté.

**Tensions possibles** : Structure contre lâcher-prise dans les échanges. Tu risques d'alterner entre précision froide et vague poétique sans trouver l'équilibre.

**Conseil clé** : Être à la fois clair·e et inspirant·e. La vraie sagesse combine raison et intuition.""",
        'weekly_advice': {
            'week_1': "Identifie un sujet où ton intuition peut éclairer la structure.",
            'week_2': "Communique avec clarté et sensibilité.",
            'week_3': "Fais confiance à ton ressenti tout en restant compréhensible.",
            'week_4': "Apprécie ta capacité à être sage et sensible."
        }
    },

    # ==================== MAISON 4 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Foyer conquis**

Ta Lune en Capricorne active ta Maison 4 : famille, racines, foyer, fondations émotionnelles. Ton Ascendant Bélier veut agir vite pour stabiliser cette base. L'alliance de la construction patiente et de l'action immédiate.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, ton besoin de sécurité intérieure. Tu cherches à bâtir des fondations solides (Capricorne) avec urgence (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à résoudre les problèmes familiaux ou domestiques immédiatement. Cette impulsivité peut servir le Capricorne qui valorise l'action, mais peut aussi brusquer des processus qui demandent du temps.

**Tensions possibles** : Impatience face aux dynamiques familiales lentes. Tu risques de forcer des changements qui ne sont pas encore mûrs.

**Conseil clé** : Agir sur ton foyer avec détermination mais aussi avec respect du temps nécessaire à l'enracinement.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de ton foyer à améliorer ou stabiliser.",
            'week_2': "Lance-toi dans cette amélioration concrètement.",
            'week_3': "Persiste même si les changements prennent du temps.",
            'week_4': "Apprécie les fondations plus solides que tu as créées."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Racines solides**

Ta Lune en Capricorne en Maison 4 cherche à construire un foyer stable et durable. Ton Ascendant Taureau renforce ce besoin de sécurité domestique et de confort matériel. Double terre : un ancrage exceptionnel.

**Domaine activé** : Maison 4 — Ton foyer, tes racines, ta famille. Tu veux créer une base inébranlable, un sanctuaire où tu te sens vraiment en sécurité.

**Ton approche instinctive** : Le Taureau te fait investir dans ton confort domestique, créer un espace beau et apaisant. Cette tendance renforce le Capricorne qui valorise la solidité du foyer.

**Tensions possibles** : Rigidité excessive dans l'organisation familiale. Tu risques de créer un cadre si structuré qu'il manque de chaleur ou de flexibilité.

**Conseil clé** : Construire un foyer stable sans qu'il devienne une prison dorée. La sécurité peut coexister avec l'ouverture.""",
        'weekly_advice': {
            'week_1': "Évalue ce qui fonctionne et ce qui manque chez toi.",
            'week_2': "Investis dans l'amélioration durable de ton espace.",
            'week_3': "Crée des routines familiales stables et rassurantes.",
            'week_4': "Savoure le confort et la solidité de ton foyer."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Foyer adaptable**

Ta Lune en Capricorne en Maison 4 veut structurer ton foyer avec sérieux. Ton Ascendant Gémeaux cherche variété, mouvement, échanges même à la maison. Le défi : allier stabilité et flexibilité domestique.

**Domaine activé** : Maison 4 — Ton foyer, tes racines. Tu cherches à la fois l'ancrage (Capricorne) et la stimulation intellectuelle (Gémeaux) dans ton espace de vie.

**Ton approche instinctive** : Le Gémeaux te fait bouger, changer, communiquer même chez toi. Cette mobilité peut frustrer le Capricorne qui cherche la routine stable.

**Tensions possibles** : Besoin de structure contre besoin de variété domestique. Tu risques de ne jamais te sentir vraiment ancré·e ou, inversement, de t'ennuyer dans la routine.

**Conseil clé** : Créer des structures flexibles à la maison. On peut avoir des bases solides tout en laissant place au mouvement.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit être stable chez toi et ce qui peut varier.",
            'week_2': "Mets en place des routines souples, pas rigides.",
            'week_3': "Autorise-toi à changer certains aspects de ton organisation.",
            'week_4': "Apprécie ton foyer à la fois stable et vivant."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Foyer profond**

Ta Lune en Capricorne en Maison 4 cherche à bâtir des fondations familiales solides. Ton Ascendant Cancer, maître naturel de cette maison, ajoute sensibilité émotionnelle profonde. L'axe Cancer-Capricorne activé : tension entre protection et responsabilité.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines émotionnelles sont au cœur de tout. Tu cherches à la fois la structure (Capricorne) et la chaleur affective (Cancer).

**Ton approche instinctive** : Le Cancer te ramène aux besoins émotionnels, à la nécessité de te sentir vraiment chez toi. Cette sensibilité peut humaniser le Capricorne trop strict ou créer une dépendance affective au foyer.

**Tensions possibles** : Conflit entre besoin de contrôle familial et besoin de douceur. Tu risques d'osciller entre autorité parentale stricte et fusion affective.

**Conseil clé** : Être à la fois fort·e et tendre dans ton foyer. La vraie solidité familiale inclut la vulnérabilité.""",
        'weekly_advice': {
            'week_1': "Reconnais tes besoins affectifs de sécurité domestique.",
            'week_2': "Crée une structure familiale qui rassure sans étouffer.",
            'week_3': "Montre ta tendresse sans craindre de perdre ton autorité.",
            'week_4': "Célèbre ton foyer à la fois solide et chaleureux."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Château personnel**

Ta Lune en Capricorne en Maison 4 veut construire un foyer respectable et solide. Ton Ascendant Lion veut que ce foyer soit également beau, impressionnant, digne de fierté. L'alliance de la structure et de la grandeur.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines. Tu veux créer une base à la fois stable (Capricorne) et magnifique (Lion).

**Ton approche instinctive** : Le Lion te pousse à investir dans un foyer qui te représente, qui reflète ton statut. Cette fierté peut motiver le Capricorne à bâtir encore mieux.

**Tensions possibles** : Conflit entre investissement raisonnable et désir de grandeur. Tu risques de dépenser trop pour l'apparence de ton foyer ou, inversement, de te frustrer en étant trop austère.

**Conseil clé** : Créer un foyer beau et solide sans ostentation excessive. On peut être fier·ère de sa maison sans se ruiner.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui mérite investissement dans ton foyer.",
            'week_2': "Améliore ton espace avec qualité et raison.",
            'week_3': "Sois fier·ère de ton foyer sans le comparer constamment.",
            'week_4': "Apprécie la dignité de ton espace de vie."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Foyer parfait**

Ta Lune en Capricorne en Maison 4 cherche à organiser ton foyer avec rigueur. Ton Ascendant Vierge ajoute souci du détail, besoin d'ordre, amélioration continue. Double terre : une organisation domestique exemplaire.

**Domaine activé** : Maison 4 — Ton foyer, ta famille. Tu veux que chaque aspect de ton espace soit optimisé, fonctionnel, impeccable.

**Ton approche instinctive** : La Vierge te fait analyser et améliorer constamment ton organisation domestique. Cette minutie renforce le Capricorne qui valorise la structure.

**Tensions possibles** : Perfectionnisme domestique excessif. Tu risques de créer une maison si ordonnée qu'elle n'est plus vraiment vivante ou chaleureuse.

**Conseil clé** : Viser l'excellence domestique sans tomber dans l'obsession. Un foyer parfaitement ordonné n'est pas forcément un foyer heureux.""",
        'weekly_advice': {
            'week_1': "Fais un audit de ton organisation domestique.",
            'week_2': "Améliore un aspect à la fois, sans tout vouloir changer.",
            'week_3': "Accepte que certaines imperfections soient vivables.",
            'week_4': "Apprécie l'ordre de ton foyer sans exiger la perfection absolue."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Foyer harmonieux**

Ta Lune en Capricorne en Maison 4 veut structurer ton foyer avec solidité. Ton Ascendant Balance cherche harmonie, beauté, équilibre dans l'espace domestique. Le défi : allier rigueur et grâce.

**Domaine activé** : Maison 4 — Ton foyer, ta famille. Tu cherches à créer un espace à la fois solide (Capricorne) et agréable (Balance).

**Ton approche instinctive** : La Balance te fait rechercher l'équilibre esthétique et relationnel à la maison. Cette douceur peut adoucir le Capricorne trop austère.

**Tensions possibles** : Hésitation entre discipline domestique et laisser-aller confortable. Tu risques de ne pas savoir si tu dois imposer des règles ou laisser chacun libre.

**Conseil clé** : Créer un cadre familial à la fois structuré et bienveillant. Les règles peuvent être appliquées avec élégance.""",
        'weekly_advice': {
            'week_1': "Identifie les règles essentielles pour ton foyer.",
            'week_2': "Mets-les en place avec douceur et fermeté.",
            'week_3': "Cultive la beauté et l'harmonie chez toi.",
            'week_4': "Apprécie ton foyer équilibré et apaisant."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Sanctuaire transformé**

Ta Lune en Capricorne en Maison 4 cherche à bâtir un foyer solide et durable. Ton Ascendant Scorpion veut transformer en profondeur tes fondations émotionnelles et familiales. L'alliance de la structure et de la métamorphose.

**Domaine activé** : Maison 4 — Ton foyer, tes racines profondes. Tu ne cherches pas juste la stabilité : tu veux guérir, transformer, reconstruire à la racine.

**Ton approche instinctive** : Le Scorpion te pousse à plonger dans les dynamiques familiales cachées, à affronter les non-dits. Cette profondeur renforce le Capricorne qui valorise les fondations solides.

**Tensions possibles** : Intensité émotionnelle familiale difficile à gérer. Tu risques de remuer des choses douloureuses sans avoir les outils pour les résoudre sainement.

**Conseil clé** : Transformer ton foyer en profondeur mais avec sagesse. Tout déterrer n'est pas toujours nécessaire.""",
        'weekly_advice': {
            'week_1': "Identifie une dynamique familiale à transformer.",
            'week_2': "Plonge dans le travail sans éviter les émotions difficiles.",
            'week_3': "Avance vers la reconstruction avec détermination.",
            'week_4': "Reconnais la profondeur de ce que tu es en train de guérir."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foyer ouvert**

Ta Lune en Capricorne en Maison 4 veut construire un foyer stable et structuré. Ton Ascendant Sagittaire cherche expansion, ouverture au monde, liberté même à la maison. Le défi : allier ancrage et horizon.

**Domaine activé** : Maison 4 — Ton foyer, tes racines. Tu cherches à la fois la sécurité domestique (Capricorne) et l'ouverture au monde (Sagittaire).

**Ton approche instinctive** : Le Sagittaire te fait voir ton foyer comme une base de lancement vers le monde, pas comme une prison dorée. Cette vision peut dynamiser le Capricorne ou créer un manque d'enracinement.

**Tensions possibles** : Besoin de racines contre soif d'aventure. Tu risques de ne jamais te sentir vraiment chez toi ou, inversement, de te sentir piégé·e.

**Conseil clé** : Créer un foyer solide qui soutient ton expansion, pas qui la limite. Les racines nourrissent les voyages.""",
        'weekly_advice': {
            'week_1': "Définis ce qu'est vraiment un foyer pour toi.",
            'week_2': "Crée une base stable qui te permet d'explorer.",
            'week_3': "Équilibre temps à la maison et ouverture au monde.",
            'week_4': "Apprécie ton foyer comme base de ta liberté."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fondations pures**

Ta Lune en Capricorne en Maison 4 avec Ascendant Capricorne crée une triple concentration sur la construction d'un foyer solide, responsable, durable. L'énergie est dense, tournée vers la sécurité à long terme.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines sont au cœur de tout ce mois. Tu cherches à bâtir des fondations inébranlables avec le plus haut niveau d'exigence.

**Ton approche instinctive** : Triple Capricorne : tu gères ton foyer comme un projet sérieux, avec méthode et discipline. Cette rigueur peut créer une vraie stabilité mais aussi une ambiance austère.

**Tensions possibles** : Foyer trop structuré, manquant de chaleur spontanée. Tu risques de créer une maison efficace mais peu chaleureuse.

**Conseil clé** : Se rappeler qu'un foyer n'est pas qu'une structure : c'est un lieu de vie, d'émotions, de liens. La perfection organisationnelle ne remplace pas l'affection.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit être renforcé dans ton foyer.",
            'week_2': "Construis avec méthode et responsabilité.",
            'week_3': "Autorise-toi aussi des moments de douceur et de légèreté.",
            'week_4': "Apprécie la solidité de ton foyer sans oublier de le vivre."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Foyer visionnaire**

Ta Lune en Capricorne en Maison 4 cherche à construire un foyer traditionnel et stable. Ton Ascendant Verseau veut innover, créer une structure familiale différente, originale. Le défi : allier tradition et innovation domestique.

**Domaine activé** : Maison 4 — Ton foyer, ta famille. Tu cherches à la fois la solidité (Capricorne) et l'authenticité unique (Verseau).

**Ton approche instinctive** : Le Verseau te pousse à questionner les modèles familiaux traditionnels, à créer ton propre concept de foyer. Cette originalité peut frustrer le Capricorne qui valorise les structures éprouvées.

**Tensions possibles** : Conflit entre besoin de conformité familiale et besoin d'authenticité. Tu risques de te sentir écartelé·e entre respecter les traditions et vivre autrement.

**Conseil clé** : Créer un foyer à la fois solide et authentique. On peut honorer certaines traditions tout en innovant.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit rester traditionnel et ce qui peut changer chez toi.",
            'week_2': "Expérimente une nouvelle forme d'organisation familiale.",
            'week_3': "Équilibre respect des bases et innovation.",
            'week_4': "Célèbre ton foyer unique et stable."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Refuge sensible**

Ta Lune en Capricorne en Maison 4 veut structurer ton foyer avec rigueur. Ton Ascendant Poissons cherche à en faire un sanctuaire émotionnel, un espace de dissolution et de rêve. La rencontre entre structure et fluidité.

**Domaine activé** : Maison 4 — Ton foyer, tes racines. Tu cherches à la fois la solidité (Capricorne) et la magie douce (Poissons) dans ton espace de vie.

**Ton approche instinctive** : Les Poissons te font rechercher une ambiance spirituelle, apaisante, presque irréelle à la maison. Cette fluidité peut adoucir le Capricorne trop rigide ou créer un manque de structure.

**Tensions possibles** : Besoin d'ordre contre besoin de lâcher prise. Tu risques d'alterner entre contrôle domestique strict et abandon total du cadre.

**Conseil clé** : Créer un foyer structuré mais apaisant. Les frontières claires peuvent coexister avec la douceur.""",
        'weekly_advice': {
            'week_1': "Identifie les structures essentielles pour ton foyer.",
            'week_2': "Mets-les en place avec douceur et flexibilité.",
            'week_3': "Cultive une ambiance apaisante chez toi.",
            'week_4': "Apprécie ton foyer à la fois stable et apaisant."
        }
    },

    # ==================== MAISON 5 à 12 : Structure identique ====================
    # Pour économiser l'espace, je vais créer les 8 maisons restantes avec le même niveau de détail
    # mais en condensant légèrement le format dans les commentaires ci-dessous.
    # Chaque maison aura ses 12 ascendants.

    # MAISON 5 : Créativité, romance, plaisir, enfants

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Joie conquise**

Ta Lune en Capricorne active ta Maison 5 : créativité, plaisirs, romance, enfants. Ton Ascendant Bélier veut créer et jouer avec énergie. L'alliance du sérieux et de la spontanéité ludique.

**Domaine activé** : Maison 5 — Tes loisirs, ta créativité, tes romances. Tu cherches à structurer tes plaisirs (Capricorne) tout en voulant de l'intensité immédiate (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à te lancer dans des projets créatifs avec fougue. Cette audace peut libérer le Capricorne trop sérieux ou créer des démarrages sans suite.

**Tensions possibles** : Difficulté à vraiment lâcher prise. Tu risques de transformer tes loisirs en obligations ou, inversement, de culpabiliser quand tu joues.

**Conseil clé** : S'autoriser le plaisir structuré. On peut être discipliné·e et s'amuser.""",
        'weekly_advice': {
            'week_1': "Identifie une activité créative qui te tente vraiment.",
            'week_2': "Lance-toi sans attendre la perfection.",
            'week_3': "Maintiens l'engagement même si l'enthousiasme baisse.",
            'week_4': "Célèbre ce que tu as créé avec fierté."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Plaisir solide**

Ta Lune en Capricorne en Maison 5 veut structurer ta créativité et tes plaisirs. Ton Ascendant Taureau cherche à savourer, à jouir des sens, à créer de la beauté. Double terre : une créativité méthodique et sensuelle.

**Domaine activé** : Maison 5 — Créativité, romance, loisirs. Tu cherches à la fois l'excellence (Capricorne) et le plaisir authentique (Taureau).

**Ton approche instinctive** : Le Taureau te fait approcher les plaisirs avec patience et sensualité. Cette lenteur peut enrichir le Capricorne qui valorise la qualité durable.

**Tensions possibles** : Difficulté à lâcher vraiment prise. Tu risques de rester trop sérieux·se même dans tes moments de détente.

**Conseil clé** : Autoriser ton corps et tes sens à guider tes plaisirs, pas seulement ta volonté.""",
        'weekly_advice': {
            'week_1': "Identifie un plaisir sensoriel que tu t'es refusé.",
            'week_2': "Accorde-toi du temps de qualité pour en jouir.",
            'week_3': "Crée quelque chose de beau sans pression de résultat.",
            'week_4': "Savoure ce que tu as vécu avec gratitude."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Joie curieuse**

Ta Lune en Capricorne en Maison 5 veut aborder la créativité avec sérieux. Ton Ascendant Gémeaux cherche variété, légèreté, exploration ludique. Le défi : allier discipline créative et spontanéité joyeuse.

**Domaine activé** : Maison 5 — Tes plaisirs, ta créativité, tes romances. Tu cherches à la fois l'excellence (Capricorne) et la diversité amusante (Gémeaux).

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre différents loisirs, explorer plusieurs formes de créativité. Cette légèreté peut libérer le Capricorne trop sérieux.

**Tensions possibles** : Multiplication des projets créatifs sans en finir aucun. Tu risques de disperser ton talent sans créer d'œuvre aboutie.

**Conseil clé** : Explorer largement mais approfondir au moins un projet créatif. La curiosité sert mieux quand elle trouve aussi un foyer.""",
        'weekly_advice': {
            'week_1': "Expérimente plusieurs formes d'expression créative.",
            'week_2': "Choisis celle qui résonne le plus et approfondis-la.",
            'week_3': "Autorise-toi à jouer sans tout prendre au sérieux.",
            'week_4': "Apprécie la joie que tu as cultivée ce mois-ci."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Création émotive**

Ta Lune en Capricorne en Maison 5 veut structurer ta créativité avec rigueur. Ton Ascendant Cancer cherche à exprimer des émotions profondes, à créer des liens affectifs par le jeu. L'axe Cancer-Capricorne : tension entre structure et sensibilité.

**Domaine activé** : Maison 5 — Créativité, romance, enfants. Tu cherches à créer quelque chose de durable (Capricorne) qui touche le cœur (Cancer).

**Ton approche instinctive** : Le Cancer te fait créer depuis tes émotions, exprimer ta vulnérabilité. Cette sensibilité peut humaniser le Capricorne trop technique.

**Tensions possibles** : Conflit entre besoin de contrôle créatif et besoin d'expression émotionnelle spontanée. Tu risques de bloquer tes émotions au nom de la perfection.

**Conseil clé** : Laisser tes émotions guider ta créativité sans perdre ta structure. Les œuvres les plus touchantes allient maîtrise et authenticité.""",
        'weekly_advice': {
            'week_1': "Identifie une émotion que tu veux exprimer créativement.",
            'week_2': "Crée sans censurer ce qui émerge.",
            'week_3': "Structure ensuite sans étouffer l'authenticité.",
            'week_4': "Partage ta création et observe comment elle touche."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Éclat maîtrisé**

Ta Lune en Capricorne en Maison 5 veut créer avec excellence et discipline. Ton Ascendant Lion, maître naturel de cette maison, veut briller, rayonner, être admiré·e. L'alliance de la maîtrise et du charisme.

**Domaine activé** : Maison 5 — Créativité, expression de soi, romance. Tu cherches à créer quelque chose d'impressionnant (Lion) et de parfaitement exécuté (Capricorne).

**Ton approche instinctive** : Le Lion te pousse à te mettre en avant, à assumer pleinement ta créativité. Cette confiance renforce le Capricorne si elle s'appuie sur un vrai travail.

**Tensions possibles** : Ego créatif contre humilité de l'artisan. Tu risques d'osciller entre fierté excessive et autocritique paralysante.

**Conseil clé** : Assumer ta lumière créative sans arrogance. La vraie maîtrise rayonne naturellement sans forcer.""",
        'weekly_advice': {
            'week_1': "Identifie un talent que tu maîtrises vraiment.",
            'week_2': "Crée quelque chose qui le met pleinement en valeur.",
            'week_3': "Partage ton œuvre avec assurance.",
            'week_4': "Reçois les retours avec grâce et fierté légitime."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Artisanat parfait**

Ta Lune en Capricorne en Maison 5 cherche l'excellence créative. Ton Ascendant Vierge ajoute précision, souci du détail, perfectionnement constant. Double terre : une créativité rigoureuse et minutieuse.

**Domaine activé** : Maison 5 — Ta créativité, tes loisirs. Tu veux que chaque création soit impeccable, chaque moment de plaisir optimisé.

**Ton approche instinctive** : La Vierge te fait perfectionner sans cesse tes créations. Cette minutie renforce le Capricorne mais peut devenir paralysante.

**Tensions possibles** : Perfectionnisme créatif excessif. Tu risques de ne jamais finir tes projets ou de ne jamais les trouver assez bons pour être partagés.

**Conseil clé** : Viser l'excellence sans tomber dans l'obsession. Fait est mieux que parfait.""",
        'weekly_advice': {
            'week_1': "Commence un projet créatif avec des standards élevés mais réalistes.",
            'week_2': "Travaille avec soin sans sur-analyser chaque détail.",
            'week_3': "Accepte les imperfections comme partie du processus.",
            'week_4': "Finis et partage, même si ce n'est pas parfait."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Beauté structurée**

Ta Lune en Capricorne en Maison 5 veut créer avec discipline. Ton Ascendant Balance cherche harmonie esthétique, grâce, équilibre. Le défi : allier rigueur et élégance créative.

**Domaine activé** : Maison 5 — Créativité, romance, plaisirs. Tu cherches à créer quelque chose de beau (Balance) et de solide (Capricorne).

**Ton approche instinctive** : La Balance te fait rechercher l'équilibre esthétique dans tes créations. Cette sensibilité peut adoucir le Capricorne trop austère.

**Tensions possibles** : Hésitation créative par souci de perfection esthétique. Tu risques de bloquer en voulant que tout soit harmonieux immédiatement.

**Conseil clé** : Créer d'abord, harmoniser ensuite. L'équilibre émerge souvent du processus, pas du premier jet.""",
        'weekly_advice': {
            'week_1': "Identifie une forme d'art qui t'attire esthétiquement.",
            'week_2': "Crée sans trop peser chaque choix.",
            'week_3': "Ajuste pour l'harmonie sans tout recommencer.",
            'week_4': "Apprécie la beauté de ce que tu as créé."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Passion contrôlée**

Ta Lune en Capricorne en Maison 5 veut créer avec excellence. Ton Ascendant Scorpion ajoute intensité émotionnelle, profondeur, pouvoir transformateur. L'alliance de la maîtrise et de la passion.

**Domaine activé** : Maison 5 — Créativité, romance, expression de soi. Tu veux créer quelque chose de puissant (Scorpion) et de maîtrisé (Capricorne).

**Ton approche instinctive** : Le Scorpion te pousse à explorer les profondeurs émotionnelles par ta créativité. Cette intensité renforce le Capricorne qui valorise la substance.

**Tensions possibles** : Obsession créative ou romantique. Tu risques de devenir trop intense dans tes passions, perdant la distance nécessaire au travail de qualité.

**Conseil clé** : Canaliser ton intensité créative sans te laisser consumer par elle. La passion sert mieux quand elle est dirigée.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te passionne vraiment créativement.",
            'week_2': "Plonge dans le travail avec intensité mais aussi discipline.",
            'week_3': "Maintiens une routine même quand l'inspiration fluctue.",
            'week_4': "Reconnais la puissance de ce que tu as créé."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Joie expansive**

Ta Lune en Capricorne en Maison 5 veut structurer ta créativité. Ton Ascendant Sagittaire cherche inspiration, vision large, joie spontanée. Le défi : allier discipline créative et enthousiasme débordant.

**Domaine activé** : Maison 5 — Créativité, plaisirs, romance. Tu cherches à créer quelque chose de grand (Sagittaire) et de solide (Capricorne).

**Ton approche instinctive** : Le Sagittaire te fait voir grand dans tes projets créatifs, rêver d'œuvres ambitieuses. Cette vision peut dynamiser le Capricorne ou créer des promesses irréalistes.

**Tensions possibles** : Optimisme créatif contre réalisme pratique. Tu risques d'alterner entre projets grandioses abandonnés et austérité créative frustrante.

**Conseil clé** : Rêver grand tout en construisant méthodiquement. Les grandes œuvres se créent étape par étape.""",
        'weekly_advice': {
            'week_1': "Définis une vision créative inspirante mais réalisable.",
            'week_2': "Décompose-la en étapes concrètes.",
            'week_3': "Avance avec joie et discipline.",
            'week_4': "Célèbre le chemin parcouru vers ta vision."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Excellence créative**

Ta Lune en Capricorne en Maison 5 avec Ascendant Capricorne crée une triple concentration sur la créativité disciplinée et l'excellence artistique. Tu abordes tes plaisirs avec le sérieux d'un projet professionnel.

**Domaine activé** : Maison 5 — Créativité, romance, loisirs. Tu cherches à maîtriser ton expression créative avec le plus haut niveau d'exigence.

**Ton approche instinctive** : Triple Capricorne : tu travailles ta créativité comme un artisan, avec patience et méthode. Cette rigueur peut créer des œuvres remarquables mais aussi étouffer la spontanéité.

**Tensions possibles** : Difficulté à lâcher prise et à vraiment jouer. Tu risques de transformer tous tes loisirs en obligations, perdant la légèreté essentielle au plaisir.

**Conseil clé** : Se rappeler que la créativité inclut aussi le jeu. L'excellence peut coexister avec la joie.""",
        'weekly_advice': {
            'week_1': "Définis un objectif créatif ambitieux.",
            'week_2': "Travaille avec discipline mais autorise-toi aussi à jouer.",
            'week_3': "Reconnais tes progrès sans tout critiquer.",
            'week_4': "Apprécie ce que tu as créé avec fierté."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Création originale**

Ta Lune en Capricorne en Maison 5 veut créer avec excellence technique. Ton Ascendant Verseau cherche originalité, innovation, expression unique. Le défi : allier maîtrise et inventivité.

**Domaine activé** : Maison 5 — Créativité, expression personnelle. Tu cherches à créer quelque chose de techniquement solide (Capricorne) et d'absolument unique (Verseau).

**Ton approche instinctive** : Le Verseau te pousse à expérimenter, à sortir des sentiers battus créatifs. Cette originalité peut frustrer le Capricorne qui valorise les formes éprouvées.

**Tensions possibles** : Conflit entre convention artistique et besoin d'innovation. Tu risques de te sentir tiraillé·e entre respecter les codes et les transcender.

**Conseil clé** : Innover en maîtrisant d'abord les bases. La vraie originalité naît souvent d'une excellente technique.""",
        'weekly_advice': {
            'week_1': "Identifie une forme d'expression qui t'es propre.",
            'week_2': "Développe ta technique sans renier ton originalité.",
            'week_3': "Ose créer différemment tout en restant excellent·e.",
            'week_4': "Célèbre ton œuvre unique et maîtrisée."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Art inspiré**

Ta Lune en Capricorne en Maison 5 veut structurer ta créativité avec rigueur. Ton Ascendant Poissons cherche inspiration, fluidité, connexion à l'invisible. La rencontre entre technique et inspiration.

**Domaine activé** : Maison 5 — Créativité, expression artistique. Tu cherches à créer quelque chose de techniquement solide (Capricorne) et d'émotionnellement touchant (Poissons).

**Ton approche instinctive** : Les Poissons te connectent à l'inspiration, aux émotions subtiles. Cette sensibilité peut enrichir le Capricorne trop technique ou créer du flou qui nuit à la réalisation.

**Tensions possibles** : Structure contre lâcher-prise créatif. Tu risques d'alterner entre contrôle rigide et abandon au flux sans trouver l'équilibre.

**Conseil clé** : Laisser l'inspiration guider, puis structurer pour finaliser. Les deux phases sont nécessaires.""",
        'weekly_advice': {
            'week_1': "Ouvre-toi à l'inspiration sans la censurer.",
            'week_2': "Crée en flux libre, sans jugement.",
            'week_3': "Structure ensuite pour donner forme à ton inspiration.",
            'week_4': "Apprécie l'œuvre à la fois inspirée et achevée."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Travail conquis**

Ta Lune en Capricorne active ta Maison 6 : travail quotidien, santé, routines, service. Ton Ascendant Bélier veut optimiser et performer immédiatement. L'alliance de la discipline et de l'action rapide.

**Domaine activé** : Maison 6 — Tes routines, ta santé, ton travail quotidien. Tu cherches l'efficacité maximale (Capricorne) obtenue rapidement (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à révolutionner tes habitudes du jour au lendemain. Cette impulsivité peut dynamiser le Capricorne ou créer des changements non durables.

**Tensions possibles** : Impatience face aux améliorations progressives. Tu risques d'abandonner avant que les nouvelles habitudes ne s'ancrent vraiment.

**Conseil clé** : Initier des changements de routine avec énergie mais les maintenir avec discipline.""",
        'weekly_advice': {
            'week_1': "Identifie une habitude de travail ou de santé à améliorer.",
            'week_2': "Change-la avec détermination.",
            'week_3': "Persiste même quand la motivation initiale retombe.",
            'week_4': "Célèbre la nouvelle routine installée."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Routine solide**

Ta Lune en Capricorne en Maison 6 cherche à optimiser ton quotidien avec méthode. Ton Ascendant Taureau aime les habitudes stables et le confort physique. Double terre : une excellence quotidienne remarquable.

**Domaine activé** : Maison 6 — Travail quotidien, santé, routines. Tu construis des habitudes durables qui soutiennent ton bien-être et ta productivité.

**Ton approche instinctive** : Le Taureau te fait avancer lentement dans l'amélioration de tes routines. Cette patience renforce le Capricorne qui valorise ce qui dure.

**Tensions possibles** : Rigidité excessive des habitudes. Tu risques de t'enfermer dans des routines qui ne servent plus mais que tu maintiens par pure inertie.

**Conseil clé** : Construire des routines solides tout en restant ouvert·e à les ajuster quand nécessaire.""",
        'weekly_advice': {
            'week_1': "Évalue tes routines actuelles avec honnêteté.",
            'week_2': "Renforce celles qui fonctionnent vraiment.",
            'week_3': "Ajuste doucement celles qui sont devenues obsolètes.",
            'week_4': "Apprécie la solidité de ton quotidien optimisé."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Efficacité adaptable**

Ta Lune en Capricorne en Maison 6 veut structurer ton quotidien avec rigueur. Ton Ascendant Gémeaux cherche variété et flexibilité dans les routines. Le défi : allier discipline et adaptabilité.

**Domaine activé** : Maison 6 — Travail, santé, habitudes. Tu cherches des routines efficaces (Capricorne) qui ne t'ennuient pas (Gémeaux).

**Ton approche instinctive** : Le Gémeaux te fait varier tes méthodes de travail, expérimenter différentes approches. Cette flexibilité peut enrichir le Capricorne ou créer de l'instabilité.

**Tensions possibles** : Difficulté à maintenir des routines constantes. Tu risques de changer de méthode avant qu'elle n'ait eu le temps de faire ses preuves.

**Conseil clé** : Créer des routines flexibles mais fiables. On peut avoir une structure tout en variant les modalités.""",
        'weekly_advice': {
            'week_1': "Identifie les piliers non négociables de tes routines.",
            'week_2': "Maintiens-les tout en variant les détails.",
            'week_3': "Expérimente des approches nouvelles dans un cadre stable.",
            'week_4': "Apprécie l'équilibre entre structure et variété."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Service émotionnel**

Ta Lune en Capricorne en Maison 6 cherche l'efficacité professionnelle quotidienne. Ton Ascendant Cancer ajoute besoin de prendre soin, de servir avec cœur. L'axe Cancer-Capricorne : tension entre devoir et sensibilité.

**Domaine activé** : Maison 6 — Travail, service, santé. Tu cherches à accomplir tes tâches avec excellence (Capricorne) et bienveillance (Cancer).

**Ton approche instinctive** : Le Cancer te fait aborder le travail comme un soin, t'occuper des autres avec douceur. Cette sensibilité peut humaniser le Capricorne trop mécanique.

**Tensions possibles** : Surinvestissement émotionnel dans le travail. Tu risques de t'épuiser à prendre soin de tout le monde en oubliant tes propres limites.

**Conseil clé** : Servir avec excellence sans sacrifier ton bien-être. La vraie efficacité inclut l'auto-préservation.""",
        'weekly_advice': {
            'week_1': "Identifie tes limites saines dans le travail et le service.",
            'week_2': "Accomplis tes tâches avec soin et professionnalisme.",
            'week_3': "Dis non quand c'est nécessaire, sans culpabilité.",
            'week_4': "Célèbre ta capacité à être compétent·e et humain·e."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Excellence visible**

Ta Lune en Capricorne en Maison 6 cherche la perfection dans le travail quotidien. Ton Ascendant Lion veut que cette excellence soit remarquée et célébrée. L'alliance de la maîtrise et du rayonnement.

**Domaine activé** : Maison 6 — Travail quotidien, compétences techniques. Tu veux être le·la meilleur·e (Capricorne) et que cela se voie (Lion).

**Ton approche instinctive** : Le Lion te pousse à briller dans ton travail quotidien, à montrer ta compétence. Cette fierté peut motiver le Capricorne à exceller encore plus.

**Tensions possibles** : Besoin de reconnaissance contre humble accomplissement du devoir. Tu risques d'être frustré·e si ton travail n'est pas assez remarqué.

**Conseil clé** : Travailler avec excellence pour toi-même d'abord. La reconnaissance vient comme conséquence, pas comme moteur principal.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine de travail où tu peux vraiment exceller.",
            'week_2': "Travaille avec excellence sans chercher constamment l'approbation.",
            'week_3': "Assume ta compétence quand elle est légitime.",
            'week_4': "Apprécie ton travail bien fait, reconnu ou non."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfection technique**

Ta Lune en Capricorne en Maison 6 cherche l'efficacité maximale. Ton Ascendant Vierge, maître naturel de cette maison, ajoute analyse minutieuse et amélioration continue. Double terre : une maîtrise technique exceptionnelle.

**Domaine activé** : Maison 6 — Travail, santé, service. Tu veux optimiser chaque processus, perfectionner chaque compétence, atteindre l'excellence opérationnelle absolue.

**Ton approche instinctive** : La Vierge te fait analyser et améliorer constamment tes méthodes de travail. Cette minutie renforce le Capricorne perfectionniste.

**Tensions possibles** : Perfectionnisme paralysant. Tu risques de te bloquer en cherchant la méthode parfaite ou de te surmener en ne trouvant jamais rien d'assez bon.

**Conseil clé** : Viser l'excellence progressive, pas la perfection immédiate. Fait excellemment est mieux que parfait jamais.""",
        'weekly_advice': {
            'week_1': "Choisis un aspect de ton travail à optimiser.",
            'week_2': "Améliore-le méthodiquement sans tout vouloir changer.",
            'week_3': "Accepte que 'très bien' soit suffisant parfois.",
            'week_4': "Reconnais ton expertise croissante sans exiger la perfection."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Travail équilibré**

Ta Lune en Capricorne en Maison 6 veut maximiser la productivité. Ton Ascendant Balance cherche harmonie, équilibre travail-vie, esthétique dans les processus. Le défi : allier efficacité et bien-être.

**Domaine activé** : Maison 6 — Travail quotidien, santé, routines. Tu cherches à être productif·ve (Capricorne) sans sacrifier ton équilibre (Balance).

**Ton approche instinctive** : La Balance te fait rechercher des méthodes de travail harmonieuses et agréables. Cette douceur peut adoucir le Capricorne trop austère.

**Tensions possibles** : Hésitation à maintenir des routines strictes par peur de la rigidité. Tu risques de manquer de discipline en cherchant trop de confort.

**Conseil clé** : Créer des routines à la fois efficaces et agréables. Discipline n'exclut pas grâce.""",
        'weekly_advice': {
            'week_1': "Identifie les routines essentielles pour ta productivité.",
            'week_2': "Mets-les en place avec élégance et fermeté.",
            'week_3': "Maintiens l'équilibre entre effort et repos.",
            'week_4': "Apprécie ton quotidien à la fois productif et harmonieux."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Maîtrise transformée**

Ta Lune en Capricorne en Maison 6 cherche l'excellence opérationnelle. Ton Ascendant Scorpion veut transformer radicalement tes méthodes de travail et tes habitudes de santé. L'alliance de la discipline et de la métamorphose.

**Domaine activé** : Maison 6 — Travail, santé, service. Tu ne cherches pas juste l'amélioration : tu veux une transformation profonde de ton rapport au quotidien.

**Ton approche instinctive** : Le Scorpion te pousse à plonger dans les racines de tes habitudes, à comprendre pourquoi tu fais ce que tu fais. Cette profondeur renforce le Capricorne stratège.

**Tensions possibles** : Intensité excessive dans le travail. Tu risques de t'obséder avec la perfection ou de t'épuiser en cherchant la transformation absolue.

**Conseil clé** : Transformer tes routines en profondeur mais progressivement. Les vraies métamorphoses prennent du temps.""",
        'weekly_advice': {
            'week_1': "Identifie une habitude qui doit changer à la racine.",
            'week_2': "Plonge dans le travail de transformation sans esquiver.",
            'week_3': "Maintiens l'intensité sans t'épuiser.",
            'week_4': "Reconnais la profondeur de ta métamorphose quotidienne."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Service inspirant**

Ta Lune en Capricorne en Maison 6 cherche l'efficacité disciplinée. Ton Ascendant Sagittaire veut que ton travail ait du sens, serve une vision plus large. Le défi : allier rigueur quotidienne et inspiration.

**Domaine activé** : Maison 6 — Travail quotidien, service. Tu cherches à accomplir tes tâches avec excellence (Capricorne) tout en restant connecté·e à leur sens profond (Sagittaire).

**Ton approche instinctive** : Le Sagittaire te fait chercher la vision d'ensemble même dans les détails quotidiens. Cette perspective peut dynamiser le Capricorne ou créer de l'impatience face aux tâches répétitives.

**Tensions possibles** : Frustration face au quotidien répétitif. Tu risques de négliger les détails au nom de la grande vision ou de te décourager si le sens n'est pas clair.

**Conseil clé** : Connecter chaque tâche quotidienne à une vision inspirante. Le sens se construit aussi dans les petits gestes.""",
        'weekly_advice': {
            'week_1': "Définis le sens profond de ton travail quotidien.",
            'week_2': "Accomplis tes tâches en restant connecté·e à cette vision.",
            'week_3': "Maintiens la discipline même dans les moments répétitifs.",
            'week_4': "Célèbre comment tes petits gestes servent le grand dessein."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Discipline pure**

Ta Lune en Capricorne en Maison 6 avec Ascendant Capricorne crée une triple concentration sur le travail, l'efficacité, la maîtrise technique. L'énergie est entièrement tournée vers l'excellence opérationnelle.

**Domaine activé** : Maison 6 — Travail quotidien, santé, routines. Tu cherches à optimiser chaque aspect de ton quotidien avec le plus haut niveau de discipline et de rigueur.

**Ton approche instinctive** : Triple Capricorne : tu abordes le travail avec un sérieux absolu, chaque routine est un engagement. Cette discipline peut créer une productivité remarquable mais aussi un épuisement.

**Tensions possibles** : Surmenage, impossibilité de lâcher prise. Tu risques de t'épuiser en étant trop exigeant·e avec toi-même dans le travail.

**Conseil clé** : Se rappeler que le repos fait partie de l'efficacité. La vraie discipline inclut la récupération.""",
        'weekly_advice': {
            'week_1': "Définis des objectifs de travail ambitieux mais sains.",
            'week_2': "Travaille avec excellence et autodiscipline.",
            'week_3': "Intègre des pauses comme partie du processus, pas comme faiblesse.",
            'week_4': "Apprécie ton accomplissement sans sacrifier ta santé."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Méthode innovante**

Ta Lune en Capricorne en Maison 6 veut optimiser le travail avec des méthodes éprouvées. Ton Ascendant Verseau cherche à innover, à expérimenter de nouvelles approches. Le défi : allier efficacité et innovation.

**Domaine activé** : Maison 6 — Travail, santé, routines. Tu cherches des méthodes à la fois fiables (Capricorne) et originales (Verseau).

**Ton approche instinctive** : Le Verseau te pousse à questionner les processus établis, à chercher de meilleures façons de faire. Cette inventivité peut frustrer le Capricorne qui valorise ce qui a fait ses preuves.

**Tensions possibles** : Conflit entre conformité professionnelle et besoin d'innovation. Tu risques de vouloir révolutionner des méthodes qui fonctionnent déjà bien.

**Conseil clé** : Innover là où c'est vraiment utile, conserver ce qui fonctionne. La vraie innovation respecte l'efficacité existante.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui mérite vraiment d'être changé dans tes méthodes.",
            'week_2': "Expérimente des approches nouvelles avec rigueur.",
            'week_3': "Évalue objectivement si l'innovation apporte vraiment un gain.",
            'week_4': "Adopte ce qui fonctionne mieux, garde ce qui était déjà bon."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Service intuitif**

Ta Lune en Capricorne en Maison 6 veut structurer le travail avec rigueur. Ton Ascendant Poissons ajoute intuition, compassion, fluidité dans le service. La rencontre entre méthode et ressenti.

**Domaine activé** : Maison 6 — Travail, service, santé. Tu cherches à être efficace (Capricorne) tout en restant à l'écoute des besoins subtils (Poissons).

**Ton approche instinctive** : Les Poissons te font travailler par intuition, ressentir ce qui est juste. Cette sensibilité peut enrichir le Capricorne trop mécanique ou créer du flou qui nuit à l'efficacité.

**Tensions possibles** : Structure contre fluidité dans le travail. Tu risques d'alterner entre rigueur excessive et laisser-aller désordonné.

**Conseil clé** : Créer des structures souples qui laissent place à l'intuition. On peut être méthodique et inspiré·e.""",
        'weekly_advice': {
            'week_1': "Établis un cadre de travail clair mais flexible.",
            'week_2': "Travaille avec méthode tout en restant à l'écoute de ton intuition.",
            'week_3': "Ajuste tes routines selon tes ressentis sans tout abandonner.",
            'week_4': "Apprécie ton équilibre entre structure et fluidité."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Partenariat dynamique**

Ta Lune en Capricorne active ta Maison 7 : relations, partenariats, engagements. Ton Ascendant Bélier veut de l'action immédiate dans les liens. L'alliance de l'engagement sérieux et de l'initiative directe.

**Domaine activé** : Maison 7 — Tes relations significatives, tes engagements. Tu cherches des partenariats solides (Capricorne) initiés avec audace (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à clarifier rapidement les relations, à savoir où tu en es. Cette franchise peut servir le Capricorne qui valorise la clarté.

**Tensions possibles** : Impatience relationnelle. Tu risques de forcer des engagements ou de rompre trop vite si ça ne va pas assez vite.

**Conseil clé** : Initier avec courage tout en respectant le temps nécessaire à la construction de liens durables.""",
        'weekly_advice': {
            'week_1': "Identifie une relation qui mérite clarification.",
            'week_2': "Aborde la conversation avec franchise et respect.",
            'week_3': "Engage-toi si c'est solide, libère si ça ne l'est pas.",
            'week_4': "Apprécie la clarté de tes relations après ce mois."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Engagement stable**

Ta Lune en Capricorne en Maison 7 cherche des partenariats fiables et durables. Ton Ascendant Taureau ajoute loyauté, constance, besoin de sécurité relationnelle. Double terre : des engagements inébranlables.

**Domaine activé** : Maison 7 — Relations, partenariats. Tu construis des liens qui durent, basés sur la confiance et la stabilité mutuelle.

**Ton approche instinctive** : Le Taureau te fait avancer lentement dans l'engagement, vérifier la solidité avant de t'investir. Cette prudence renforce le Capricorne responsable.

**Tensions possibles** : Rigidité relationnelle. Tu risques de maintenir des liens devenus toxiques par pure loyauté ou peur du changement.

**Conseil clé** : Construire du durable sans s'enfermer dans ce qui ne fonctionne plus. La vraie loyauté inclut parfois de partir.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement tes relations importantes.",
            'week_2': "Investis dans celles qui sont vraiment solides.",
            'week_3': "Reconsidère celles qui te coûtent plus qu'elles n'apportent.",
            'week_4': "Célèbre les liens authentiquement durables."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Partenariat communicatif**

Ta Lune en Capricorne en Maison 7 veut des engagements sérieux. Ton Ascendant Gémeaux cherche variété, dialogue, stimulation intellectuelle dans les liens. Le défi : allier profondeur et légèreté.

**Domaine activé** : Maison 7 — Relations, partenariats. Tu cherches des liens à la fois engagés (Capricorne) et vivants intellectuellement (Gémeaux).

**Ton approche instinctive** : Le Gémeaux te fait privilégier la communication, l'échange d'idées. Cette vivacité peut enrichir le Capricorne ou créer un manque d'ancrage émotionnel profond.

**Tensions possibles** : Difficulté à t'engager vraiment. Tu risques de papillonner relationnellement ou de rester superficiel·le par peur de la lourdeur.

**Conseil clé** : Communiquer beaucoup ET s'engager profondément. Les deux ne s'opposent pas.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui compte vraiment dans tes relations.",
            'week_2': "Parle ouvertement de tes besoins et engagements.",
            'week_3': "Maintiens le dialogue tout en approfondissant le lien.",
            'week_4': "Apprécie les relations à la fois légères et engagées."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Engagement émotionnel**

Ta Lune en Capricorne en Maison 7 cherche des partenariats responsables et structurés. Ton Ascendant Cancer veut des liens affectivement nourrissants et protecteurs. L'axe Cancer-Capricorne : tension entre besoin et devoir.

**Domaine activé** : Maison 7 — Relations, engagements. Tu cherches à la fois la sécurité émotionnelle (Cancer) et la solidité pratique (Capricorne) dans tes liens.

**Ton approche instinctive** : Le Cancer te fait rechercher la fusion affective, le sentiment d'appartenance. Cette sensibilité peut humaniser le Capricorne trop formel.

**Tensions possibles** : Conflit entre besoin d'indépendance et besoin de fusion. Tu risques d'osciller entre engagement fusionnel et distance protectrice.

**Conseil clé** : Construire des liens à la fois solides et tendres. L'interdépendance saine allie autonomie et intimité.""",
        'weekly_advice': {
            'week_1': "Reconnais tes besoins affectifs sans en avoir honte.",
            'week_2': "Exprime-les clairement dans tes relations importantes.",
            'week_3': "Engage-toi sans perdre ton autonomie.",
            'week_4': "Célèbre les liens qui t'offrent sécurité et liberté."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Partenariat royal**

Ta Lune en Capricorne en Maison 7 veut des engagements respectables et dignes. Ton Ascendant Lion cherche des relations qui te mettent en valeur, où tu peux briller. L'alliance de la solidité et de la grandeur.

**Domaine activé** : Maison 7 — Relations, partenariats. Tu veux des liens à la fois solides (Capricorne) et valorisants (Lion).

**Ton approche instinctive** : Le Lion te fait rechercher des partenaires à ta hauteur, qui reconnaissent ta valeur. Cette fierté peut motiver ou créer des exigences irréalistes.

**Tensions possibles** : Ego relationnel. Tu risques de chercher des partenaires qui te flattent plus qu'ils ne te complètent vraiment.

**Conseil clé** : Choisir des partenaires pour leur valeur réelle, pas pour comment ils te font paraître.""",
        'weekly_advice': {
            'week_1': "Évalue tes relations sur leur vraie substance, pas leur apparence.",
            'week_2': "Engage-toi avec des personnes qui te challengent et t'admirent.",
            'week_3': "Sois généreux·se autant que tu demandes de reconnaissance.",
            'week_4': "Célèbre les partenariats authentiquement mutuels."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Partenariat perfectible**

Ta Lune en Capricorne en Maison 7 cherche des engagements fiables. Ton Ascendant Vierge analyse, évalue, cherche à améliorer constamment les relations. Double terre : une exigence relationnelle élevée.

**Domaine activé** : Maison 7 — Relations, partenariats. Tu veux des liens impeccables, où chacun assume sa part avec excellence.

**Ton approche instinctive** : La Vierge te fait analyser tes relations, identifier ce qui ne fonctionne pas. Cette lucidité renforce le Capricorne mais peut devenir critique excessive.

**Tensions possibles** : Perfectionnisme relationnel. Tu risques de ne jamais être satisfait·e de tes relations, toujours en train de voir les défauts.

**Conseil clé** : Viser l'excellence relationnelle sans exiger la perfection. Les vraies relations incluent les imperfections.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de tes relations à améliorer.",
            'week_2': "Travaille dessus avec bienveillance, pas avec critique.",
            'week_3': "Accepte aussi les imperfections acceptables.",
            'week_4': "Apprécie les relations réelles, pas idéales."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Engagement harmonieux**

Ta Lune en Capricorne en Maison 7 veut des partenariats solides et responsables. Ton Ascendant Balance, maître naturel de cette maison, cherche harmonie, équilibre, beauté dans les liens. L'alliance de la solidité et de la grâce.

**Domaine activé** : Maison 7 — Relations, partenariats, mariage. Tu cherches des engagements à la fois durables (Capricorne) et harmonieux (Balance).

**Ton approche instinctive** : La Balance te fait rechercher l'équilibre parfait dans les relations. Cette quête peut enrichir le Capricorne ou créer de l'indécision paralysante.

**Tensions possibles** : Hésitation à s'engager pleinement par peur de perdre l'harmonie. Tu risques de rester dans des relations médiocres par souci de paix.

**Conseil clé** : Construire des partenariats équilibrés en ayant le courage de partir si l'équilibre est impossible.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement l'équilibre dans tes relations importantes.",
            'week_2': "Adresse les déséquilibres avec diplomatie et fermeté.",
            'week_3': "Engage-toi pleinement si c'est équilibré, reconsidère sinon.",
            'week_4': "Célèbre les relations mutuellement nourrissantes."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Engagement transformé**

Ta Lune en Capricorne en Maison 7 cherche des partenariats durables et responsables. Ton Ascendant Scorpion veut des liens intenses, transformateurs, d'une profondeur absolue. L'alliance de la structure et de la passion.

**Domaine activé** : Maison 7 — Relations, engagements. Tu ne veux pas de liens superficiels : tu cherches des partenariats qui transforment, qui touchent à l'essentiel.

**Ton approche instinctive** : Le Scorpion te pousse à plonger dans la profondeur relationnelle, à créer des liens fusionnels. Cette intensité renforce le Capricorne si elle reste saine.

**Tensions possibles** : Obsession ou contrôle relationnel. Tu risques de devenir trop intense, possessif·ve, ou de choisir des relations toxiquement passionnelles.

**Conseil clé** : Créer des liens profonds sans perdre ton autonomie. L'intimité vraie n'est pas fusion totale.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu cherches vraiment dans tes relations profondes.",
            'week_2': "Engage-toi intensément mais sainement.",
            'week_3': "Maintiens ton individualité même dans l'intimité.",
            'week_4': "Célèbre les liens profonds qui te libèrent, pas qui t'emprisonnent."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Partenariat libre**

Ta Lune en Capricorne en Maison 7 veut des engagements sérieux et responsables. Ton Ascendant Sagittaire cherche liberté, expansion, aventure même dans les liens. Le défi : allier engagement et autonomie.

**Domaine activé** : Maison 7 — Relations, partenariats. Tu cherches des liens à la fois stables (Capricorne) et libres (Sagittaire).

**Ton approche instinctive** : Le Sagittaire te fait chercher des partenaires qui soutiennent ton expansion, pas qui la limitent. Cette liberté peut dynamiser ou empêcher le vrai engagement.

**Tensions possibles** : Peur de l'engagement perçu comme limitation. Tu risques de fuir les relations sérieuses ou de te sentir étouffé·e dans les engagements.

**Conseil clé** : Comprendre que le vrai engagement libère plutôt qu'il n'enferme. Choisir des partenaires qui grandissent avec toi.""",
        'weekly_advice': {
            'week_1': "Identifie si tes relations soutiennent ou limitent ta croissance.",
            'week_2': "Engage-toi avec ceux·celles qui t'encouragent à grandir.",
            'week_3': "Libère-toi des liens qui t'étouffent vraiment.",
            'week_4': "Célèbre les partenariats qui allient stabilité et expansion."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Engagement absolu**

Ta Lune en Capricorne en Maison 7 avec Ascendant Capricorne crée une triple concentration sur l'engagement responsable et durable. Les relations sont prises avec le plus grand sérieux.

**Domaine activé** : Maison 7 — Partenariats, engagements. Tu cherches des relations avec le plus haut niveau de responsabilité, de loyauté, de construction commune.

**Ton approche instinctive** : Triple Capricorne : tu abordes les relations comme des contrats sérieux, des engagements à long terme. Cette solidité peut créer des liens indestructibles ou une froideur relationnelle.

**Tensions possibles** : Difficulté à montrer la légèreté et la spontanéité. Tu risques de rendre tes relations trop sérieuses, manquant de joie et de tendresse.

**Conseil clé** : Se rappeler que les relations nourrissent aussi le cœur, pas seulement le devoir. L'engagement peut être joyeux.""",
        'weekly_advice': {
            'week_1': "Évalue tes engagements avec honnêteté et maturité.",
            'week_2': "Honore tes responsabilités relationnelles avec fierté.",
            'week_3': "Autorise-toi aussi des moments de légèreté et de jeu.",
            'week_4': "Célèbre les liens solides que tu construis."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Partenariat unique**

Ta Lune en Capricorne en Maison 7 cherche des engagements traditionnels et stables. Ton Ascendant Verseau veut des relations originales, non conventionnelles, basées sur l'authenticité. Le défi : allier tradition et innovation.

**Domaine activé** : Maison 7 — Relations, partenariats. Tu cherches à la fois la solidité (Capricorne) et l'authenticité unique (Verseau).

**Ton approche instinctive** : Le Verseau te pousse à redéfinir ce qu'est un engagement, à créer tes propres règles relationnelles. Cette originalité peut frustrer le Capricorne qui valorise les structures éprouvées.

**Tensions possibles** : Conflit entre besoin de conformité relationnelle et besoin d'authenticité. Tu risques de te sentir tiraillé·e entre respecter les normes et vivre autrement.

**Conseil clé** : Créer des engagements à la fois solides et authentiques. On peut être responsable et original·e.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui compte vraiment pour toi dans les relations.",
            'week_2': "Construis des engagements qui respectent ton authenticité.",
            'week_3': "Assume tes choix relationnels même s'ils sont non conventionnels.",
            'week_4': "Célèbre les partenariats à la fois solides et uniques."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Engagement intuitif**

Ta Lune en Capricorne en Maison 7 veut des partenariats structurés et responsables. Ton Ascendant Poissons cherche fusion spirituelle, compassion, liens qui transcendent le rationnel. La rencontre entre engagement et dévotion.

**Domaine activé** : Maison 7 — Relations, partenariats. Tu cherches des liens à la fois solides (Capricorne) et spirituellement nourrissants (Poissons).

**Ton approche instinctive** : Les Poissons te font choisir par intuition, ressentir la justesse d'un lien. Cette sensibilité peut enrichir le Capricorne ou créer des engagements basés sur l'illusion.

**Tensions possibles** : Idéalisation relationnelle. Tu risques de te sacrifier dans des relations par compassion ou de maintenir des liens toxiques par empathie excessive.

**Conseil clé** : Écouter ton cœur tout en gardant les pieds sur terre. L'amour vrai est à la fois spirituel et pragmatique.""",
        'weekly_advice': {
            'week_1': "Évalue tes relations avec ton cœur ET ta raison.",
            'week_2': "Engage-toi avec compassion mais aussi avec lucidité.",
            'week_3': "Maintiens tes frontières même dans la tendresse.",
            'week_4': "Célèbre les liens à la fois nourrissants et sains."
        }
    },

    # ==================== MAISON 8 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Transformation conquise**

Ta Lune en Capricorne active ta Maison 8 : transformation, intimité profonde, ressources partagées, mort et renaissance. Ton Ascendant Bélier veut affronter ces profondeurs avec courage immédiat.

**Domaine activé** : Maison 8 — Transformation psychologique, intimité, pouvoir partagé. Tu cherches à maîtriser (Capricorne) les processus de métamorphose avec audace (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à plonger sans hésitation dans ce qui fait peur. Cette bravoure peut accélérer la transformation ou créer des ruptures prématurées.

**Tensions possibles** : Impatience face aux processus profonds qui prennent du temps. Tu risques de forcer la transformation au lieu de la laisser mûrir.

**Conseil clé** : Affronter avec courage tout en respectant le temps nécessaire à la vraie métamorphose.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit vraiment mourir en toi pour que tu évolues.",
            'week_2': "Affronte ce processus avec courage.",
            'week_3': "Maintiens l'engagement même quand c'est inconfortable.",
            'week_4': "Reconnais la transformation déjà opérée."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Richesse partagée**

Ta Lune en Capricorne en Maison 8 cherche à structurer les ressources partagées et les transformations profondes. Ton Ascendant Taureau ajoute besoin de sécurité matérielle et sensuelle dans l'intimité. Double terre : une gestion des profondeurs pragmatique.

**Domaine activé** : Maison 8 — Ressources partagées, héritages, transformations. Tu veux sécuriser ce qui vient de l'autre, gérer les biens communs avec rigueur.

**Ton approche instinctive** : Le Taureau te fait aborder les questions financières et intimes avec prudence. Cette stabilité renforce le Capricorne mais peut créer de la résistance au changement nécessaire.

**Tensions possibles** : Peur de la perte dans le partage. Tu risques de bloquer sur le contrôle des ressources communes ou de résister aux transformations profondes.

**Conseil clé** : Construire la sécurité dans le partage sans bloquer la transformation. La vraie solidité inclut l'évolution.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement ta situation financière partagée.",
            'week_2': "Clarifie les accords sur les ressources communes.",
            'week_3': "Autorise-toi à lâcher ce qui doit partir.",
            'week_4': "Apprécie la solidité créée dans le partage."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Profondeur communiquée**

Ta Lune en Capricorne en Maison 8 veut structurer les transformations et l'intimité. Ton Ascendant Gémeaux cherche à comprendre intellectuellement, à parler de ces profondeurs. Le défi : allier transformation silencieuse et expression.

**Domaine activé** : Maison 8 — Transformation, intimité, psychologie. Tu cherches à comprendre (Gémeaux) et maîtriser (Capricorne) les processus profonds.

**Ton approche instinctive** : Le Gémeaux te fait intellectualiser les émotions profondes, chercher des mots pour l'indicible. Cette tendance peut éclairer ou éviter la vraie profondeur.

**Tensions possibles** : Rationalisation excessive des processus émotionnels. Tu risques de rester en surface en analysant au lieu de ressentir.

**Conseil clé** : Comprendre ET ressentir. La vraie transformation inclut le corps et les émotions, pas seulement l'esprit.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu intellectualises pour éviter de ressentir.",
            'week_2': "Plonge dans l'expérience émotionnelle sans la fuir.",
            'week_3': "Ensuite, nomme et comprends ce qui s'est passé.",
            'week_4': "Intègre la sagesse gagnée par ce voyage profond."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Intimité structurée**

Ta Lune en Capricorne en Maison 8 cherche à maîtriser les transformations et l'intimité. Ton Ascendant Cancer veut fusionner émotionnellement, créer des liens affectifs profonds. L'axe Cancer-Capricorne : tension entre vulnérabilité et contrôle.

**Domaine activé** : Maison 8 — Intimité profonde, transformation émotionnelle. Tu cherches à la fois la sécurité affective (Cancer) et le contrôle du processus (Capricorne).

**Ton approche instinctive** : Le Cancer te pousse vers la fusion, le besoin de te perdre dans l'autre. Cette sensibilité peut humaniser le Capricorne mais aussi créer une dépendance malsaine.

**Tensions possibles** : Oscillation entre contrôle émotionnel et abandon total. Tu risques de bloquer par peur de la vulnérabilité ou de fusionner sans frontières.

**Conseil clé** : S'autoriser l'intimité vraie sans perdre son autonomie. La vraie fusion préserve l'individualité.""",
        'weekly_advice': {
            'week_1': "Reconnais ton besoin d'intimité profonde sans en avoir honte.",
            'week_2': "Ouvre-toi progressivement sans tout donner d'un coup.",
            'week_3': "Maintiens tes frontières même dans la fusion.",
            'week_4': "Célèbre l'intimité qui te nourrit sans t'engloutir."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Pouvoir transformé**

Ta Lune en Capricorne en Maison 8 cherche à maîtriser le pouvoir partagé et les transformations. Ton Ascendant Lion veut briller même dans les profondeurs, transformer avec fierté. L'alliance de la stratégie et de la puissance.

**Domaine activé** : Maison 8 — Pouvoir, transformation, renaissance. Tu veux gérer les ressources communes et les métamorphoses avec dignité et autorité.

**Ton approche instinctive** : Le Lion te fait aborder les transformations avec confiance, refusant d'être diminué·e par le processus. Cette fierté peut renforcer ou créer un déni des vulnérabilités nécessaires.

**Tensions possibles** : Ego face aux transformations qui exigent l'humilité. Tu risques de résister aux processus qui demandent de lâcher le contrôle.

**Conseil clé** : Accepter que la vraie transformation passe parfois par l'humiliation temporaire. La vraie grandeur inclut la renaissance.""",
        'weekly_advice': {
            'week_1': "Identifie où ton ego bloque ta transformation.",
            'week_2': "Accepte de traverser l'inconfort avec dignité.",
            'week_3': "Maintiens ton centre même en lâchant le contrôle.",
            'week_4': "Ressors transformé·e et plus authentiquement puissant·e."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Analyse profonde**

Ta Lune en Capricorne en Maison 8 veut structurer les transformations et gérer les ressources partagées. Ton Ascendant Vierge analyse, décortique, cherche à comprendre chaque détail. Double terre : une maîtrise technique des profondeurs.

**Domaine activé** : Maison 8 — Transformation, psychologie, ressources communes. Tu veux comprendre et optimiser les processus profonds avec précision.

**Ton approche instinctive** : La Vierge te fait analyser tes transformations, disséquer tes processus psychologiques. Cette minutie peut éclairer mais aussi éviter la vraie plongée émotionnelle.

**Tensions possibles** : Perfectionnisme dans le travail sur soi. Tu risques de transformer la thérapie en projet intellectuel sans vraie libération émotionnelle.

**Conseil clé** : Comprendre est utile, mais ressentir et libérer est essentiel. La vraie guérison inclut le lâcher-prise.""",
        'weekly_advice': {
            'week_1': "Identifie un schéma psychologique à transformer.",
            'week_2': "Analyse-le avec lucidité mais sans jugement.",
            'week_3': "Plonge aussi dans l'émotion, pas seulement l'analyse.",
            'week_4': "Intègre la libération émotionnelle ET la compréhension."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Partage équilibré**

Ta Lune en Capricorne en Maison 8 veut structurer les ressources partagées et les transformations. Ton Ascendant Balance cherche équité, harmonie, justice dans ce qui est commun. Le défi : allier maîtrise et équilibre.

**Domaine activé** : Maison 8 — Ressources partagées, pouvoir commun. Tu cherches des accords justes (Balance) et durables (Capricorne) dans l'intimité financière et émotionnelle.

**Ton approche instinctive** : La Balance te fait peser soigneusement ce qui est équitable dans le partage. Cette quête peut enrichir ou créer de l'hésitation paralysante.

**Tensions possibles** : Difficulté à trancher dans les questions de partage. Tu risques de rester dans des situations déséquilibrées par peur de rompre l'harmonie.

**Conseil clé** : Exiger l'équité véritable, pas l'apparence de paix. Parfois, le conflit mène à un partage plus juste.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement l'équité dans tes partages intimes.",
            'week_2': "Adresse les déséquilibres avec diplomatie et fermeté.",
            'week_3': "Négocie jusqu'à trouver un vrai accord juste.",
            'week_4': "Célèbre les partages authentiquement équilibrés."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Métamorphose totale**

Ta Lune en Capricorne en Maison 8 cherche à maîtriser les transformations profondes. Ton Ascendant Scorpion, maître naturel de cette maison, veut plonger dans l'absolu, mourir et renaître complètement. L'alliance de la structure et de l'alchimie.

**Domaine activé** : Maison 8 — Transformation, mort et renaissance, pouvoir occulte. Tu ne cherches pas des ajustements superficiels : tu veux la métamorphose complète, structurée et radicale.

**Ton approche instinctive** : Le Scorpion te pousse à aller au bout des processus, à ne jamais éviter les profondeurs. Cette intensité renforce le Capricorne stratège mais peut devenir obsessionnelle.

**Tensions possibles** : Obsession de la transformation ou du contrôle. Tu risques de devenir trop intense, de chercher le pouvoir absolu ou de te perdre dans les profondeurs.

**Conseil clé** : Plonger avec courage ET sagesse. La vraie transformation est puissante mais pas destructrice.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit vraiment mourir pour ta renaissance.",
            'week_2': "Plonge dans le processus sans esquiver l'inconfort.",
            'week_3': "Maintiens une structure qui te protège dans le chaos.",
            'week_4': "Émerge transformé·e et plus puissant·e."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Philosophie profonde**

Ta Lune en Capricorne en Maison 8 veut maîtriser les transformations et les ressources partagées. Ton Ascendant Sagittaire cherche le sens profond, la vérité philosophique dans ces processus. Le défi : allier profondeur et vision.

**Domaine activé** : Maison 8 — Transformation, psychologie, sens de la mort. Tu cherches à comprendre (Sagittaire) et maîtriser (Capricorne) les grands mystères de l'existence.

**Ton approche instinctive** : Le Sagittaire te fait chercher une vision d'ensemble même dans les profondeurs. Cette quête de sens peut éclairer ou éviter l'émotion brute.

**Tensions possibles** : Fuite dans la philosophie pour éviter la confrontation émotionnelle. Tu risques de théoriser sur la mort et la transformation sans les vivre vraiment.

**Conseil clé** : Chercher le sens APRÈS avoir traversé l'expérience. La sagesse naît de la confrontation, pas de la spéculation.""",
        'weekly_advice': {
            'week_1': "Identifie une transformation que tu as évitée.",
            'week_2': "Plonge dans l'expérience concrète, pas dans la théorie.",
            'week_3': "Traverse l'émotion brute avant de chercher le sens.",
            'week_4': "Intègre la sagesse gagnée par l'expérience vécue."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maîtrise absolue**

Ta Lune en Capricorne en Maison 8 avec Ascendant Capricorne crée une triple concentration sur la maîtrise des transformations et du pouvoir. L'énergie est dense, tournée vers le contrôle des profondeurs.

**Domaine activé** : Maison 8 — Transformation, pouvoir, ressources partagées. Tu cherches à gérer les processus les plus intenses avec le plus haut niveau de contrôle et de responsabilité.

**Ton approche instinctive** : Triple Capricorne : tu abordes même la mort, la sexualité, le pouvoir avec stratégie et discipline. Cette maîtrise peut créer une vraie puissance mais aussi bloquer la vulnérabilité nécessaire.

**Tensions possibles** : Contrôle excessif empêchant la vraie transformation. Tu risques de rester en surface des profondeurs par peur de perdre le contrôle.

**Conseil clé** : Accepter que certaines transformations exigent de lâcher prise. La vraie maîtrise inclut parfois l'abandon contrôlé.""",
        'weekly_advice': {
            'week_1': "Identifie où ton besoin de contrôle bloque ta transformation.",
            'week_2': "Autorise-toi à perdre le contrôle dans un cadre sécurisé.",
            'week_3': "Traverse la vulnérabilité avec courage.",
            'week_4': "Reconnais la puissance gagnée par le lâcher-prise."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Transformation libérée**

Ta Lune en Capricorne en Maison 8 veut structurer les transformations et gérer les ressources partagées. Ton Ascendant Verseau cherche liberté, détachement, approche non conventionnelle des profondeurs. Le défi : allier maîtrise et libération.

**Domaine activé** : Maison 8 — Transformation, intimité, pouvoir. Tu cherches à te transformer (Capricorne) de manière authentique et libératrice (Verseau).

**Ton approche instinctive** : Le Verseau te fait aborder les transformations avec détachement, observer tes processus de l'extérieur. Cette distance peut protéger ou empêcher la vraie plongée.

**Tensions possibles** : Fuite dans le détachement pour éviter l'intensité. Tu risques de rester intellectuel·le face à des processus qui demandent une immersion totale.

**Conseil clé** : Utiliser le détachement après la plongée, pas à la place. On peut être libre ET profond.""",
        'weekly_advice': {
            'week_1': "Identifie où tu évites l'intensité par détachement.",
            'week_2': "Plonge complètement dans la transformation.",
            'week_3': "Ensuite, prends du recul pour intégrer.",
            'week_4': "Célèbre ta capacité à être profond·e et libre."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution structurée**

Ta Lune en Capricorne en Maison 8 veut maîtriser les transformations avec structure. Ton Ascendant Poissons cherche dissolution, lâcher-prise, fusion avec l'invisible. La rencontre entre contrôle et abandon.

**Domaine activé** : Maison 8 — Transformation, mystère, transcendance. Tu cherches à la fois à maîtriser (Capricorne) et à te dissoudre (Poissons) dans les processus profonds.

**Ton approche instinctive** : Les Poissons te font lâcher prise, te fondre dans l'expérience transformatrice. Cette fluidité peut enrichir le Capricorne ou créer une confusion qui retarde la vraie transformation.

**Tensions possibles** : Oscillation entre contrôle rigide et abandon total. Tu risques de bloquer par peur de te perdre ou de te noyer sans structure.

**Conseil clé** : Créer un cadre qui permet le lâcher-prise sécurisé. On peut structurer le chemin vers la dissolution.""",
        'weekly_advice': {
            'week_1': "Définis un cadre sécurisant pour ta transformation.",
            'week_2': "Dans ce cadre, autorise-toi à lâcher prise complètement.",
            'week_3': "Fais confiance au processus sans tout contrôler.",
            'week_4': "Émerge transformé·e, ayant intégré contrôle et abandon."
        }
    },

    # ==================== MAISON 9 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Sagesse conquise**

Ta Lune en Capricorne active ta Maison 9 : philosophie, voyages lointains, enseignement supérieur, quête de sens. Ton Ascendant Bélier veut explorer et apprendre avec audace immédiate.

**Domaine activé** : Maison 9 — Ta quête de sens, ton expansion intellectuelle et spirituelle. Tu cherches une sagesse solide (Capricorne) acquise par l'aventure (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à te lancer dans l'apprentissage sans attendre, à explorer sans préparation excessive. Cette audace peut dynamiser ou créer des apprentissages superficiels.

**Tensions possibles** : Impatience face à la maturation de la sagesse. Tu risques de vouloir la vérité immédiatement sans respecter le temps de l'intégration.

**Conseil clé** : Explorer avec audace tout en prenant le temps de vraiment intégrer ce que tu découvres.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine de connaissance ou une vision à explorer.",
            'week_2': "Lance-toi dans l'apprentissage avec enthousiasme.",
            'week_3': "Ralentis pour intégrer, pas juste accumuler.",
            'week_4': "Partage la sagesse réellement acquise."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Philosophie enracinée**

Ta Lune en Capricorne en Maison 9 cherche une sagesse structurée et pragmatique. Ton Ascendant Taureau veut une philosophie concrète, ancrée dans le réel. Double terre : une sagesse profondément pratique.

**Domaine activé** : Maison 9 — Philosophie, enseignement, voyages. Tu cherches une vision du monde à la fois élevée (Maison 9) et concrètement applicable (double terre).

**Ton approche instinctive** : Le Taureau te fait construire ta philosophie lentement, par expérience directe. Cette patience renforce le Capricorne qui valorise la sagesse éprouvée.

**Tensions possibles** : Rigidité philosophique. Tu risques de t'enfermer dans une vision du monde qui ne laisse plus place à l'évolution.

**Conseil clé** : Construire une philosophie solide tout en restant ouvert·e aux nouvelles perspectives.""",
        'weekly_advice': {
            'week_1': "Identifie les principes qui guident vraiment ta vie.",
            'week_2': "Teste-les concrètement dans ton quotidien.",
            'week_3': "Reste ouvert·e à ajuster si l'expérience le demande.",
            'week_4': "Apprécie la sagesse pragmatique que tu développes."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Savoir structuré**

Ta Lune en Capricorne en Maison 9 veut une connaissance profonde et fiable. Ton Ascendant Gémeaux cherche variété intellectuelle, exploration de multiples systèmes de pensée. Le défi : allier profondeur et largeur.

**Domaine activé** : Maison 9 — Enseignement supérieur, philosophie, compréhension du monde. Tu cherches à la fois la maîtrise (Capricorne) et la curiosité (Gémeaux).

**Ton approche instinctive** : Le Gémeaux te fait explorer de nombreuses philosophies, comparer différentes visions. Cette ouverture peut enrichir ou disperser ton apprentissage.

**Tensions possibles** : Multiplication des connaissances sans vraie sagesse. Tu risques de papillonner intellectuellement sans développer une vision cohérente.

**Conseil clé** : Explorer largement mais approfondir stratégiquement. La vraie sagesse intègre, pas seulement accumule.""",
        'weekly_advice': {
            'week_1': "Explore plusieurs perspectives sur un sujet qui t'intéresse.",
            'week_2': "Identifie les points communs et différences.",
            'week_3': "Synthétise ta propre compréhension intégrée.",
            'week_4': "Partage cette sagesse personnelle avec clarté."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sagesse nourricière**

Ta Lune en Capricorne en Maison 9 cherche une philosophie structurée et responsable. Ton Ascendant Cancer veut une vision du monde qui nourrit émotionnellement, qui crée un sens d'appartenance. L'axe Cancer-Capricorne : tension entre tradition et structure.

**Domaine activé** : Maison 9 — Philosophie, croyances, quête de sens. Tu cherches une vision à la fois solide (Capricorne) et émotionnellement rassurante (Cancer).

**Ton approche instinctive** : Le Cancer te fait rechercher une philosophie qui protège, qui offre un foyer spirituel. Cette sensibilité peut humaniser le Capricorne trop austère.

**Tensions possibles** : Attachement émotionnel à une croyance qui ne sert plus. Tu risques de maintenir une vision du monde par besoin de sécurité plutôt que par vérité.

**Conseil clé** : Choisir une philosophie qui nourrit ET qui est vraie. La sécurité émotionnelle ne doit pas remplacer l'honnêteté intellectuelle.""",
        'weekly_advice': {
            'week_1': "Examine honnêtement tes croyances actuelles.",
            'week_2': "Identifie celles que tu gardes par habitude ou peur.",
            'week_3': "Ose questionner même ce qui est rassurant.",
            'week_4': "Adopte une vision à la fois vraie et nourrissante."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Enseignement magistral**

Ta Lune en Capricorne en Maison 9 veut développer une sagesse respectable et structurée. Ton Ascendant Lion veut enseigner, rayonner, inspirer par ta vision. L'alliance de la maîtrise et du charisme.

**Domaine activé** : Maison 9 — Enseignement, philosophie, vision du monde. Tu veux à la fois maîtriser (Capricorne) et partager avec grandeur (Lion).

**Ton approche instinctive** : Le Lion te pousse à enseigner avec confiance, à assumer ton autorité intellectuelle. Cette assurance renforce le Capricorne si elle repose sur une vraie compétence.

**Tensions possibles** : Ego intellectuel. Tu risques de te croire plus sage que tu ne l'es ou de chercher l'admiration plus que la vérité.

**Conseil clé** : Enseigner ce que tu maîtrises vraiment. La vraie autorité intellectuelle vient de l'humilité continue d'apprendre.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine où ta sagesse est légitime.",
            'week_2': "Partage-la avec assurance mais aussi avec humilité.",
            'week_3': "Reste ouvert·e à apprendre même en enseignant.",
            'week_4': "Célèbre ton rôle de guide sans arrogance."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision philosophique**

Ta Lune en Capricorne en Maison 9 cherche une compréhension profonde et structurée. Ton Ascendant Vierge analyse, vérifie, perfectionne chaque concept. Double terre : une rigueur intellectuelle exemplaire.

**Domaine activé** : Maison 9 — Philosophie, enseignement, systèmes de croyance. Tu veux une vision du monde techniquement irréprochable, logiquement cohérente.

**Ton approche instinctive** : La Vierge te fait décortiquer chaque idée, vérifier chaque source. Cette minutie renforce le Capricorne mais peut devenir paralysante.

**Tensions possibles** : Perfectionnisme intellectuel empêchant la synthèse. Tu risques de rester dans l'analyse sans jamais formuler ta propre vision.

**Conseil clé** : Viser la rigueur sans exiger la perfection absolue. Parfois, une vision "assez cohérente" suffit pour avancer.""",
        'weekly_advice': {
            'week_1': "Choisis un système de pensée à étudier en profondeur.",
            'week_2': "Analyse-le avec rigueur mais sans tout critiquer.",
            'week_3': "Formule ta propre synthèse, même imparfaite.",
            'week_4': "Partage ta compréhension sans attendre la perfection."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Philosophie équilibrée**

Ta Lune en Capricorne en Maison 9 veut une sagesse structurée et responsable. Ton Ascendant Balance cherche harmonie entre différentes perspectives, équité dans la vision du monde. Le défi : allier structure et ouverture.

**Domaine activé** : Maison 9 — Philosophie, justice, compréhension globale. Tu cherches une vision à la fois solide (Capricorne) et équilibrée (Balance).

**Ton approche instinctive** : La Balance te fait peser différentes philosophies, chercher la synthèse harmonieuse. Cette diplomatie peut enrichir ou créer de l'indécision.

**Tensions possibles** : Hésitation à adopter une vision claire par souci d'équité. Tu risques de rester relativiste sans jamais prendre position.

**Conseil clé** : Écouter tous les côtés ET choisir ta vérité. L'équilibre n'exclut pas la conviction.""",
        'weekly_advice': {
            'week_1': "Explore différentes perspectives sur une question importante.",
            'week_2': "Pèse-les avec honnêteté et ouverture.",
            'week_3': "Choisis ta position avec courage.",
            'week_4': "Défends-la avec élégance mais fermeté."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité profonde**

Ta Lune en Capricorne en Maison 9 cherche une sagesse structurée et fiable. Ton Ascendant Scorpion veut plonger dans les vérités cachées, comprendre ce qui est tabou, transformer par la connaissance. L'alliance de la structure et de la profondeur.

**Domaine activé** : Maison 9 — Philosophie, psychologie profonde, vérités occultes. Tu ne veux pas de sagesse superficielle : tu cherches la vérité qui transforme radicalement.

**Ton approche instinctive** : Le Scorpion te pousse à chercher sous la surface des enseignements, à ne jamais accepter les réponses faciles. Cette profondeur renforce le Capricorne stratège.

**Tensions possibles** : Obsession de la vérité absolue. Tu risques de devenir cynique ou de rejeter toute philosophie comme insuffisante.

**Conseil clé** : Chercher la profondeur sans tomber dans le nihilisme. La vérité peut être profonde ET constructive.""",
        'weekly_advice': {
            'week_1': "Identifie une vérité que tu as évitée par confort.",
            'week_2': "Plonge dans cette confrontation avec courage.",
            'week_3': "Intègre ce que tu découvres sans te détruire.",
            'week_4': "Partage la sagesse gagnée par cette honnêteté radicale."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vision structurée**

Ta Lune en Capricorne en Maison 9 veut une philosophie pragmatique et solide. Ton Ascendant Sagittaire, maître naturel de cette maison, cherche expansion infinie, optimisme, vision inspirante. Le défi : allier réalisme et inspiration.

**Domaine activé** : Maison 9 — Philosophie, voyages, enseignement, quête de sens. Tu cherches à la fois l'élévation (Sagittaire) et l'ancrage (Capricorne) dans ta vision du monde.

**Ton approche instinctive** : Le Sagittaire te fait rêver grand, chercher le sens ultime, explorer sans limites. Cette vision peut dynamiser le Capricorne ou créer des croyances irréalistes.

**Tensions possibles** : Optimisme philosophique contre réalisme pragmatique. Tu risques d'alterner entre foi naïve et cynisme désenchanté.

**Conseil clé** : Viser haut tout en marchant sur terre. La vraie sagesse combine vision inspirante et application concrète.""",
        'weekly_advice': {
            'week_1': "Définis une vision philosophique inspirante mais réaliste.",
            'week_2': "Teste-la concrètement dans ta vie quotidienne.",
            'week_3': "Ajuste selon l'expérience sans perdre l'inspiration.",
            'week_4': "Partage cette sagesse à la fois élevée et applicable."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Sagesse pure**

Ta Lune en Capricorne en Maison 9 avec Ascendant Capricorne crée une triple concentration sur la construction d'une philosophie solide, responsable, pragmatique. L'énergie est tournée vers la maîtrise intellectuelle.

**Domaine activé** : Maison 9 — Philosophie, enseignement, vision du monde. Tu cherches une sagesse avec le plus haut niveau de rigueur, de cohérence, d'application pratique.

**Ton approche instinctive** : Triple Capricorne : tu abordes la philosophie comme un projet sérieux, construisant ta vision du monde avec méthode. Cette rigueur peut créer une vraie sagesse mais aussi de l'austérité.

**Tensions possibles** : Vision du monde trop sévère ou pessimiste. Tu risques de développer une philosophie qui manque d'espoir ou de légèreté.

**Conseil clé** : Construire une sagesse solide qui soutient la vie, pas qui la juge. La vraie maturité inclut aussi la joie.""",
        'weekly_advice': {
            'week_1': "Examine ta philosophie actuelle avec honnêteté.",
            'week_2': "Identifie si elle soutient ta croissance ou te limite.",
            'week_3': "Ajuste pour plus de sagesse ET de vitalité.",
            'week_4': "Partage une vision du monde à la fois mature et vivante."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Philosophie libérée**

Ta Lune en Capricorne en Maison 9 veut une sagesse structurée et fiable. Ton Ascendant Verseau cherche originalité, avant-garde, vision futuriste. Le défi : allier tradition et innovation philosophique.

**Domaine activé** : Maison 9 — Philosophie, enseignement, vision du monde. Tu cherches une sagesse à la fois solide (Capricorne) et visionnaire (Verseau).

**Ton approche instinctive** : Le Verseau te pousse à questionner toutes les orthodoxies, à créer ta propre philosophie unique. Cette originalité peut frustrer le Capricorne qui valorise les systèmes éprouvés.

**Tensions possibles** : Conflit entre respect de la tradition et besoin d'innovation. Tu risques de rejeter toute sagesse ancienne ou, inversement, de te conformer sans vraiment adhérer.

**Conseil clé** : Respecter la sagesse éprouvée tout en osant innover. Les vraies avancées philosophiques intègrent le passé sans s'y enfermer.""",
        'weekly_advice': {
            'week_1': "Étudie une tradition philosophique sérieusement.",
            'week_2': "Identifie ce qui reste valable et ce qui est dépassé.",
            'week_3': "Ose formuler ta propre vision innovante.",
            'week_4': "Partage cette sagesse à la fois ancrée et visionnaire."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sagesse spirituelle**

Ta Lune en Capricorne en Maison 9 veut une philosophie structurée et pragmatique. Ton Ascendant Poissons cherche transcendance, connexion spirituelle, dissolution des frontières intellectuelles. La rencontre entre structure et mystique.

**Domaine activé** : Maison 9 — Philosophie, spiritualité, quête de sens. Tu cherches une vision à la fois solide (Capricorne) et spirituellement nourrissante (Poissons).

**Ton approche instinctive** : Les Poissons te connectent à l'intuition spirituelle, à la sagesse qui dépasse la logique. Cette sensibilité peut enrichir le Capricorne ou créer confusion et manque de structure.

**Tensions possibles** : Oscillation entre rationalisme strict et mysticisme flou. Tu risques d'alterner entre rejet du spirituel et perte dans l'irrationnel.

**Conseil clé** : Construire une philosophie qui intègre raison ET intuition. La vraie sagesse embrasse le mystère sans abandonner la clarté.""",
        'weekly_advice': {
            'week_1': "Explore une pratique spirituelle avec ouverture.",
            'week_2': "Cherche aussi à comprendre rationnellement ce que tu vis.",
            'week_3': "Intègre les deux dimensions sans les opposer.",
            'week_4': "Partage une sagesse à la fois mystique et cohérente."
        }
    },

    # ==================== MAISON 10 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Carrière conquise**

Ta Lune en Capricorne active ta Maison 10 : carrière, statut social, réputation publique, accomplissement professionnel. Ton Ascendant Bélier veut conquérir le sommet avec audace et rapidité. Double cardinal : une force d'ambition impressionnante.

**Domaine activé** : Maison 10 — Ta carrière, ton image publique, ton héritage professionnel. Tu cherches le succès (Capricorne) obtenu par l'action directe (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à foncer vers tes objectifs professionnels sans attendre. Cette audace peut accélérer ta progression ou créer des mouvements impulsifs mal calculés.

**Tensions possibles** : Impatience face aux hiérarchies et aux processus lents. Tu risques de brûler des étapes essentielles dans ta précipitation.

**Conseil clé** : Garder l'énergie du Bélier tout en respectant la stratégie à long terme du Capricorne. L'ascension durable combine audace et patience.""",
        'weekly_advice': {
            'week_1': "Identifie un objectif de carrière ambitieux mais réaliste.",
            'week_2': "Prends une initiative audacieuse vers ce but.",
            'week_3': "Maintiens l'effort même quand la progression ralentit.",
            'week_4': "Célèbre les étapes franchies professionnellement."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Statut construit**

Ta Lune en Capricorne en Maison 10 cherche l'excellence et la reconnaissance professionnelle. Ton Ascendant Taureau ajoute patience, persistance, construction méthodique. Triple terre (Capricorne + Maison 10 + Taureau) : une force d'accomplissement exceptionnelle.

**Domaine activé** : Maison 10 — Carrière, réputation, statut. Tu construis ton héritage professionnel pierre par pierre, refusant les raccourcis hasardeux.

**Ton approche instinctive** : Le Taureau te fait avancer lentement mais sûrement vers le sommet. Cette patience renforce le Capricorne qui valorise la construction durable.

**Tensions possibles** : Lenteur excessive ou résistance au changement nécessaire. Tu risques de rester trop longtemps dans une position confortable au lieu de progresser.

**Conseil clé** : Maintenir ta solidité tout en restant ouvert·e aux opportunités d'évolution. La stabilité n'est pas l'immobilisme.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement ta progression professionnelle actuelle.",
            'week_2': "Investis dans une compétence qui te fait avancer durablement.",
            'week_3': "Persiste même si les résultats semblent lents.",
            'week_4': "Apprécie la solidité de ton statut professionnel."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Carrière polyvalente**

Ta Lune en Capricorne en Maison 10 veut une réussite professionnelle structurée et respectable. Ton Ascendant Gémeaux cherche variété, communication, multiples projets. Le défi : allier expertise et polyvalence.

**Domaine activé** : Maison 10 — Carrière, réputation publique. Tu cherches à la fois la reconnaissance (Capricorne) et la stimulation intellectuelle (Gémeaux).

**Ton approche instinctive** : Le Gémeaux te fait explorer plusieurs pistes professionnelles, communiquer ton expertise. Cette polyvalence peut enrichir ou disperser ton ascension.

**Tensions possibles** : Multiplication des projets sans vraie spécialisation. Tu risques de papillonner professionnellement sans construire une vraie autorité.

**Conseil clé** : Diversifier stratégiquement tout en développant une expertise reconnue. La polyvalence sert mieux quand elle s'appuie sur une base solide.""",
        'weekly_advice': {
            'week_1': "Identifie ton domaine d'expertise principal.",
            'week_2': "Développe-le avec constance et excellence.",
            'week_3': "Enrichis-le par des compétences complémentaires.",
            'week_4': "Communique ton positionnement professionnel clair."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Leadership protecteur**

Ta Lune en Capricorne en Maison 10 cherche l'accomplissement professionnel et le statut. Ton Ascendant Cancer veut diriger avec bienveillance, protéger, nourrir. L'axe Cancer-Capricorne vertical activé : tension entre ambition et sensibilité.

**Domaine activé** : Maison 10 — Carrière, image publique, autorité. Tu cherches à réussir (Capricorne) tout en restant humain·e et accessible (Cancer).

**Ton approche instinctive** : Le Cancer te fait aborder le leadership avec empathie, créer une ambiance familiale même au travail. Cette douceur peut humaniser le Capricorne trop austère.

**Tensions possibles** : Conflit entre autorité professionnelle et besoin d'être aimé·e. Tu risques de sacrifier ta progression pour maintenir l'harmonie ou de te durcir excessivement.

**Conseil clé** : Diriger avec force ET cœur. La vraie autorité inclut la compassion.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu peux diriger avec plus de cœur.",
            'week_2': "Prends des décisions fermes sans devenir froid·e.",
            'week_3': "Équilibre ambition et bien-être de ton équipe.",
            'week_4': "Célèbre ton leadership à la fois fort et humain."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Autorité rayonnante**

Ta Lune en Capricorne en Maison 10 cherche la réussite professionnelle sérieuse et structurée. Ton Ascendant Lion veut briller, être admiré·e, diriger avec charisme. L'alliance de la compétence et de la prestance.

**Domaine activé** : Maison 10 — Carrière, statut, réputation. Tu veux à la fois maîtriser ton domaine (Capricorne) et rayonner publiquement (Lion).

**Ton approche instinctive** : Le Lion te pousse à assumer pleinement ton autorité, à te mettre en avant avec confiance. Cette assurance renforce le Capricorne si elle repose sur de vraies réalisations.

**Tensions possibles** : Ego professionnel. Tu risques de chercher la reconnaissance plus que l'excellence ou de paraître arrogant·e.

**Conseil clé** : Laisser tes accomplissements parler pour toi. La vraie grandeur n'a pas besoin de se vanter.""",
        'weekly_advice': {
            'week_1': "Identifie tes vraies réalisations professionnelles.",
            'week_2': "Travaille avec excellence sans chercher constamment l'applaudissement.",
            'week_3': "Assume ta légitimité quand elle est méritée.",
            'week_4': "Rayonne naturellement par ta compétence."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Excellence technique**

Ta Lune en Capricorne en Maison 10 cherche la maîtrise professionnelle et la reconnaissance. Ton Ascendant Vierge ajoute perfectionnisme technique, souci du détail, amélioration continue. Triple terre : une compétence professionnelle exceptionnelle.

**Domaine activé** : Maison 10 — Carrière, expertise reconnue. Tu veux être irréprochable professionnellement, atteindre le plus haut niveau de maîtrise technique.

**Ton approche instinctive** : La Vierge te fait perfectionner constamment tes compétences, analyser chaque détail. Cette minutie renforce le Capricorne mais peut devenir paralysante.

**Tensions possibles** : Perfectionnisme empêchant la progression. Tu risques de refuser des promotions en te sentant pas assez prêt·e ou de t'épuiser en détails.

**Conseil clé** : Viser l'excellence sans exiger la perfection. L'expertise se développe dans l'action, pas dans l'attente du moment parfait.""",
        'weekly_advice': {
            'week_1': "Identifie une compétence professionnelle clé à améliorer.",
            'week_2': "Travaille dessus avec rigueur mais sans obsession.",
            'week_3': "Accepte de montrer ton travail même s'il est imparfait.",
            'week_4': "Reconnais ton niveau d'expertise croissant."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Leadership harmonieux**

Ta Lune en Capricorne en Maison 10 veut l'accomplissement professionnel et le statut. Ton Ascendant Balance cherche harmonie dans le leadership, relations professionnelles équilibrées. Le défi : allier autorité et diplomatie.

**Domaine activé** : Maison 10 — Carrière, image publique. Tu cherches à réussir (Capricorne) tout en maintenant de bonnes relations (Balance).

**Ton approche instinctive** : La Balance te fait diriger avec diplomatie, chercher le consensus. Cette douceur peut adoucir le Capricorne trop autoritaire ou créer une faiblesse dans le leadership.

**Tensions possibles** : Hésitation à prendre des décisions impopulaires mais nécessaires. Tu risques de sacrifier ton autorité pour être aimé·e.

**Conseil clé** : Diriger avec élégance mais aussi avec fermeté. On peut être aimable ET décisif·ve.""",
        'weekly_advice': {
            'week_1': "Identifie une décision professionnelle difficile à prendre.",
            'week_2': "Prends-la avec fermeté douce après consultation.",
            'week_3': "Maintiens ton cap malgré les possibles mécontentements.",
            'week_4': "Apprécie ton leadership à la fois fort et respectueux."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir stratégique**

Ta Lune en Capricorne en Maison 10 cherche l'accomplissement professionnel durable. Ton Ascendant Scorpion ajoute intensité, stratégie profonde, capacité de transformation du pouvoir. L'alliance de la structure et de la puissance.

**Domaine activé** : Maison 10 — Carrière, statut, influence. Tu ne cherches pas juste la réussite : tu veux un pouvoir réel et durable, la capacité de transformer ton domaine.

**Ton approche instinctive** : Le Scorpion te fait jouer stratégiquement, comprendre les dynamiques de pouvoir cachées. Cette profondeur renforce le Capricorne maître tacticien.

**Tensions possibles** : Obsession du pouvoir ou manipulation. Tu risques de devenir trop calculateur·rice, de perdre en authenticité dans ta quête de contrôle.

**Conseil clé** : Chercher le pouvoir pour servir, pas pour dominer. La vraie autorité libère, elle n'emprisonne pas.""",
        'weekly_advice': {
            'week_1': "Identifie l'influence réelle que tu veux avoir.",
            'week_2': "Développe ta stratégie avec lucidité et intégrité.",
            'week_3': "Avance vers le pouvoir sans perdre ton éthique.",
            'week_4': "Use de ton autorité pour élever, pas pour écraser."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vision accomplie**

Ta Lune en Capricorne en Maison 10 cherche l'accomplissement professionnel structuré. Ton Ascendant Sagittaire veut que ta carrière ait du sens, inspire, serve une vision plus grande. Le défi : allier pragmatisme et inspiration.

**Domaine activé** : Maison 10 — Carrière, réputation, héritage. Tu cherches à réussir (Capricorne) dans un domaine qui compte vraiment (Sagittaire).

**Ton approche instinctive** : Le Sagittaire te fait chercher le sens profond de ton travail, refuser les carrières purement alimentaires. Cette quête peut dynamiser ou créer de l'instabilité.

**Tensions possibles** : Vision grandiose contre réalisme professionnel. Tu risques d'alterner entre rêves inspirants irréalisables et cynisme pragmatique.

**Conseil clé** : Construire une carrière inspirante un pas à la fois. Les grandes visions se réalisent par la discipline quotidienne.""",
        'weekly_advice': {
            'week_1': "Définis le sens profond que tu veux donner à ta carrière.",
            'week_2': "Identifie des actions concrètes qui servent cette vision.",
            'week_3': "Avance méthodiquement sans perdre l'inspiration.",
            'week_4': "Célèbre comment ton travail sert quelque chose de plus grand."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Ambition absolue**

Ta Lune en Capricorne en Maison 10, sa maison naturelle, avec Ascendant Capricorne crée une quadruple concentration sur l'accomplissement professionnel. L'énergie est totalement tournée vers le succès, le statut, l'héritage.

**Domaine activé** : Maison 10 — Carrière, réputation publique, accomplissement de vie. Tu cherches l'excellence professionnelle avec le plus haut niveau d'exigence et de discipline.

**Ton approche instinctive** : Quadruple Capricorne : tu abordes ta carrière comme une montagne à gravir méthodiquement. Cette détermination peut créer un succès remarquable mais aussi un épuisement total.

**Tensions possibles** : Surmenage, sacrifice de tout le reste pour la carrière. Tu risques de réussir professionnellement mais de t'appauvrir humainement.

**Conseil clé** : Se rappeler que l'accomplissement inclut aussi la vie personnelle. La vraie réussite est équilibrée.""",
        'weekly_advice': {
            'week_1': "Définis tes objectifs professionnels avec ambition ET sagesse.",
            'week_2': "Travaille avec excellence sans sacrifier ta santé.",
            'week_3': "Maintiens aussi du temps pour les relations et le repos.",
            'week_4': "Célèbre ton accomplissement sans oublier de vivre."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Carrière visionnaire**

Ta Lune en Capricorne en Maison 10 cherche la réussite professionnelle traditionnelle et le statut. Ton Ascendant Verseau veut innover, révolutionner ton domaine, créer une carrière unique. Le défi : allier reconnaissance et originalité.

**Domaine activé** : Maison 10 — Carrière, image publique. Tu cherches à la fois la légitimité (Capricorne) et l'originalité (Verseau).

**Ton approche instinctive** : Le Verseau te pousse à faire les choses différemment, à remettre en question les méthodes établies. Cette originalité peut frustrer le Capricorne qui valorise les chemins éprouvés.

**Tensions possibles** : Conflit entre conformité professionnelle et besoin d'authenticité. Tu risques de te sentir écartelé·e entre jouer le jeu et rester toi-même.

**Conseil clé** : Innover dans le cadre de l'excellence. On peut être original·e ET reconnu·e professionnellement.""",
        'weekly_advice': {
            'week_1': "Identifie où ton originalité peut créer de la valeur professionnelle.",
            'week_2': "Construis ta crédibilité en respectant certaines règles.",
            'week_3': "Apporte ensuite ton innovation avec assurance.",
            'week_4': "Célèbre ta capacité à être professionnel·le et unique."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Service inspiré**

Ta Lune en Capricorne en Maison 10 veut l'accomplissement professionnel structuré. Ton Ascendant Poissons cherche à servir avec compassion, à apporter une dimension spirituelle ou artistique à ta carrière. La rencontre entre structure et inspiration.

**Domaine activé** : Maison 10 — Carrière, vocation, héritage. Tu cherches une réussite à la fois concrète (Capricorne) et inspirante (Poissons).

**Ton approche instinctive** : Les Poissons te font choisir ta carrière par intuition, chercher à toucher les cœurs. Cette sensibilité peut enrichir le Capricorne ou créer un manque de structure.

**Tensions possibles** : Rêve professionnel contre réalisme de carrière. Tu risques d'alterner entre idéalisme irréaliste et cynisme pragmatique.

**Conseil clé** : Construire une carrière qui nourrit ton âme ET tes besoins matériels. Les deux ne s'opposent pas.""",
        'weekly_advice': {
            'week_1': "Identifie comment ta carrière peut servir quelque chose de plus grand.",
            'week_2': "Mets en place des structures concrètes pour y arriver.",
            'week_3': "Maintiens l'inspiration tout en restant pragmatique.",
            'week_4': "Célèbre ta vocation à la fois inspirée et viable."
        }
    },

    # ==================== MAISON 11 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Réseau conquis**

Ta Lune en Capricorne active ta Maison 11 : réseaux, amitiés, projets collectifs, vision du futur. Ton Ascendant Bélier veut initier des mouvements collectifs avec énergie. L'alliance de la stratégie sociale et de l'action directe.

**Domaine activé** : Maison 11 — Tes amitiés, ton réseau professionnel, tes projets de groupe. Tu cherches à bâtir des alliances solides (Capricorne) par l'initiative audacieuse (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à prendre les devants dans les groupes, à lancer des projets collaboratifs. Cette énergie peut dynamiser ou brusquer tes relations.

**Tensions possibles** : Impatience avec les processus collectifs qui prennent du temps. Tu risques de forcer ou de partir trop vite.

**Conseil clé** : Initier avec énergie tout en respectant le rythme du groupe. Les vrais réseaux se construisent progressivement.""",
        'weekly_advice': {
            'week_1': "Identifie un projet collectif qui te tient à cœur.",
            'week_2': "Lance l'initiative avec enthousiasme.",
            'week_3': "Maintiens l'engagement même quand ça ralentit.",
            'week_4': "Célèbre ce que le groupe a accompli ensemble."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Alliances stables**

Ta Lune en Capricorne en Maison 11 cherche à construire un réseau solide et fiable. Ton Ascendant Taureau ajoute loyauté, constance, patience dans les amitiés. Double terre : des relations de groupe durables.

**Domaine activé** : Maison 11 — Amis, réseau, communauté. Tu construis des alliances qui durent, des amitiés qui traversent le temps.

**Ton approche instinctive** : Le Taureau te fait choisir tes amis et projets collectifs avec soin, investir lentement mais sûrement. Cette patience renforce le Capricorne stratégique.

**Tensions possibles** : Rigidité dans les amitiés. Tu risques de maintenir des relations qui ne servent plus par pure loyauté ou habitude.

**Conseil clé** : Cultiver les amitiés durables tout en restant ouvert·e aux nouvelles connexions enrichissantes.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement quelles amitiés nourrissent vraiment.",
            'week_2': "Investis du temps dans celles qui comptent vraiment.",
            'week_3': "Ouvre-toi aussi à de nouvelles rencontres potentielles.",
            'week_4': "Apprécie la solidité de ton cercle social."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Réseau vivant**

Ta Lune en Capricorne en Maison 11 veut structurer ton réseau avec stratégie. Ton Ascendant Gémeaux cherche variété, échanges intellectuels, multiples connexions. Le défi : allier profondeur et largeur sociale.

**Domaine activé** : Maison 11 — Amitiés, réseau, projets collectifs. Tu cherches à la fois des alliances solides (Capricorne) et stimulantes intellectuellement (Gémeaux).

**Ton approche instinctive** : Le Gémeaux te fait papillonner socialement, multiplier les connexions. Cette ouverture peut enrichir ton réseau ou créer de la superficialité.

**Tensions possibles** : Multiplication des connaissances sans vraies amitiés. Tu risques d'avoir un réseau large mais peu profond.

**Conseil clé** : Réseauter largement tout en cultivant aussi quelques amitiés profondes. Quantité ET qualité.""",
        'weekly_advice': {
            'week_1': "Identifie qui sont tes vrais amis vs simples connaissances.",
            'week_2': "Approfondis quelques relations clés.",
            'week_3': "Reste ouvert·e à de nouvelles connexions intéressantes.",
            'week_4': "Apprécie ton réseau à la fois large et authentique."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Communauté nourricière**

Ta Lune en Capricorne en Maison 11 cherche à construire un réseau stratégique et utile. Ton Ascendant Cancer veut une communauté qui nourrit émotionnellement, une famille d'âmes. L'axe Cancer-Capricorne : tension entre besoin affectif et objectif stratégique.

**Domaine activé** : Maison 11 — Amitiés, communauté, appartenance. Tu cherches à la fois un réseau efficace (Capricorne) et une vraie famille de cœur (Cancer).

**Ton approche instinctive** : Le Cancer te fait rechercher des amitiés profondes, créer des liens familiaux avec tes amis. Cette tendresse peut humaniser le Capricorne trop utilitaire.

**Tensions possibles** : Conflit entre réseau professionnel et besoin d'intimité amicale. Tu risques de te sentir seul·e dans un réseau utile mais froid.

**Conseil clé** : Construire un réseau qui sert tes objectifs ET nourrit ton cœur. Les deux ne s'excluent pas.""",
        'weekly_advice': {
            'week_1': "Identifie si ton réseau te nourrit émotionnellement.",
            'week_2': "Cultive les amitiés qui allient utilité et authenticité.",
            'week_3': "Ose montrer ta vulnérabilité dans les groupes sûrs.",
            'week_4': "Célèbre ta communauté à la fois efficace et aimante."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Leadership collectif**

Ta Lune en Capricorne en Maison 11 cherche à structurer des projets de groupe stratégiques. Ton Ascendant Lion veut briller dans le collectif, diriger, inspirer. L'alliance de l'organisation et du charisme.

**Domaine activé** : Maison 11 — Projets collectifs, réseau, amitiés. Tu cherches à la fois l'efficacité (Capricorne) et la reconnaissance au sein du groupe (Lion).

**Ton approche instinctive** : Le Lion te pousse à prendre naturellement le leadership dans les projets collectifs. Cette assurance peut organiser le groupe ou créer des conflits d'ego.

**Tensions possibles** : Besoin de diriger contre esprit collaboratif. Tu risques de vouloir tout contrôler au lieu de vraiment co-créer.

**Conseil clé** : Diriger le groupe en servant sa vision, pas ton ego. Le vrai leadership élève tout le monde.""",
        'weekly_advice': {
            'week_1': "Identifie un projet collectif où ton leadership peut servir.",
            'week_2': "Organise avec assurance tout en écoutant le groupe.",
            'week_3': "Partage les mérites des réussites collectives.",
            'week_4': "Célèbre ce que le groupe a accompli ensemble."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Réseau optimisé**

Ta Lune en Capricorne en Maison 11 veut organiser les projets collectifs avec stratégie. Ton Ascendant Vierge ajoute analyse, optimisation, amélioration des processus de groupe. Double terre : une efficacité collective remarquable.

**Domaine activé** : Maison 11 — Projets de groupe, réseau professionnel. Tu cherches à optimiser le fonctionnement collectif, rendre le groupe plus efficace.

**Ton approche instinctive** : La Vierge te fait analyser et améliorer constamment les processus de groupe. Cette minutie renforce le Capricorne organisateur.

**Tensions possibles** : Perfectionnisme collectif. Tu risques de frustrer le groupe par ton souci excessif du détail ou tes critiques constantes.

**Conseil clé** : Améliorer sans critiquer. Proposer des optimisations avec bienveillance, pas avec jugement.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect du travail collectif à améliorer.",
            'week_2': "Propose des solutions constructives, pas juste des critiques.",
            'week_3': "Aide le groupe à s'améliorer sans le décourager.",
            'week_4': "Célèbre les progrès collectifs accomplis."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Collaboration harmonieuse**

Ta Lune en Capricorne en Maison 11 veut organiser les projets collectifs avec efficacité. Ton Ascendant Balance cherche harmonie, équité, beauté dans la collaboration. Le défi : allier structure et fluidité de groupe.

**Domaine activé** : Maison 11 — Amitiés, projets collectifs, réseau. Tu cherches à la fois l'efficacité (Capricorne) et l'harmonie (Balance) dans le collectif.

**Ton approche instinctive** : La Balance te fait rechercher le consensus, l'équité dans les décisions de groupe. Cette diplomatie peut faciliter la collaboration ou créer de l'indécision.

**Tensions possibles** : Hésitation à trancher dans les groupes. Tu risques de sacrifier l'efficacité pour maintenir l'harmonie.

**Conseil clé** : Maintenir l'harmonie tout en avançant. Parfois, décider avec élégance vaut mieux que tergiverser indéfiniment.""",
        'weekly_advice': {
            'week_1': "Identifie les tensions dans tes groupes ou projets collectifs.",
            'week_2': "Facilite le dialogue et la résolution harmonieuse.",
            'week_3': "Prends des décisions avec diplomatie mais aussi avec fermeté.",
            'week_4': "Célèbre l'harmonie ET l'efficacité du groupe."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Réseau transformé**

Ta Lune en Capricorne en Maison 11 cherche à construire un réseau stratégique et puissant. Ton Ascendant Scorpion veut transformer le collectif, créer des alliances profondes et intenses. L'alliance de la structure et de la profondeur.

**Domaine activé** : Maison 11 — Amitiés, projets collectifs, réseau de pouvoir. Tu ne cherches pas des relations superficielles : tu veux des alliances qui transforment.

**Ton approche instinctive** : Le Scorpion te pousse à créer des liens profonds dans les groupes, à comprendre les dynamiques cachées. Cette intensité renforce le Capricorne stratège.

**Tensions possibles** : Manipulation ou contrôle du groupe. Tu risques de devenir trop calculateur·rice dans tes relations sociales.

**Conseil clé** : Créer des alliances profondes basées sur l'authenticité, pas sur le calcul. Le vrai pouvoir collectif naît de la confiance.""",
        'weekly_advice': {
            'week_1': "Identifie qui partage vraiment ta vision et tes valeurs.",
            'week_2': "Approfondit ces relations avec honnêteté.",
            'week_3': "Construis des projets collectifs ambitieux ensemble.",
            'week_4': "Célèbre la puissance des alliances authentiques."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vision partagée**

Ta Lune en Capricorne en Maison 11 veut organiser des projets collectifs structurés. Ton Ascendant Sagittaire cherche à inspirer le groupe, partager une vision, créer du sens ensemble. Le défi : allier organisation et inspiration.

**Domaine activé** : Maison 11 — Projets de groupe, communauté, vision collective. Tu cherches à construire (Capricorne) une communauté inspirante (Sagittaire).

**Ton approche instinctive** : Le Sagittaire te fait partager ta vision avec enthousiasme, inspirer le collectif. Cette inspiration peut dynamiser ou créer des promesses irréalistes.

**Tensions possibles** : Vision collective contre réalisme organisationnel. Tu risques d'alterner entre optimisme naïf et pragmatisme désenchanté.

**Conseil clé** : Inspirer le groupe tout en gardant les pieds sur terre. Les grandes visions se réalisent par une organisation méthodique.""",
        'weekly_advice': {
            'week_1': "Partage une vision inspirante pour ton groupe ou réseau.",
            'week_2': "Organise concrètement les étapes pour y arriver.",
            'week_3': "Maintiens l'enthousiasme tout en avançant avec méthode.",
            'week_4': "Célèbre ce que la vision collective a accompli."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Réseau stratégique**

Ta Lune en Capricorne en Maison 11 avec Ascendant Capricorne crée une triple concentration sur la construction d'un réseau professionnel solide, stratégique, utile. Les amitiés sont aussi des alliances.

**Domaine activé** : Maison 11 — Réseau professionnel, projets collectifs, alliances stratégiques. Tu construis ton cercle social avec le plus haut niveau de stratégie et de sélectivité.

**Ton approche instinctive** : Triple Capricorne : tu choisis tes amis et projets collectifs avec la même rigueur qu'un investissement. Cette stratégie peut créer un réseau puissant mais aussi froid.

**Tensions possibles** : Utilitarisme relationnel. Tu risques de transformer toutes tes amitiés en réseau professionnel, perdant l'authenticité et la chaleur.

**Conseil clé** : Se rappeler que les vraies amitiés nourrissent aussi le cœur. Tous les liens ne doivent pas être stratégiques.""",
        'weekly_advice': {
            'week_1': "Évalue ton réseau avec lucidité stratégique.",
            'week_2': "Investis dans les alliances vraiment utiles.",
            'week_3': "Cultive aussi quelques amitiés désintéressées.",
            'week_4': "Apprécie ton réseau à la fois efficace et humain."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Communauté visionnaire**

Ta Lune en Capricorne en Maison 11 veut organiser des projets collectifs solides. Ton Ascendant Verseau, maître naturel de cette maison, cherche innovation, avant-garde, révolution collective. L'alliance de la structure et de la vision.

**Domaine activé** : Maison 11 — Projets collectifs, communauté, avenir. Tu cherches à construire (Capricorne) une communauté innovante (Verseau).

**Ton approche instinctive** : Le Verseau te pousse à créer des groupes originaux, à rassembler autour d'idées avant-gardistes. Cette vision peut dynamiser ou créer de l'utopie déconnectée.

**Tensions possibles** : Idéalisme collectif contre pragmatisme organisationnel. Tu risques d'alterner entre rêves révolutionnaires et conformisme structurel.

**Conseil clé** : Innover collectivement avec une vraie organisation. Les révolutions durables sont bien structurées.""",
        'weekly_advice': {
            'week_1': "Identifie une innovation collective que tu veux porter.",
            'week_2': "Rassemble des alliés qui partagent cette vision.",
            'week_3': "Organise concrètement le projet avec rigueur.",
            'week_4': "Célèbre ce que votre communauté innovante accomplit."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Fraternité spirituelle**

Ta Lune en Capricorne en Maison 11 veut structurer les projets collectifs avec rigueur. Ton Ascendant Poissons cherche une communauté spirituelle, des liens d'âme, une fraternité transcendante. La rencontre entre organisation et fusion.

**Domaine activé** : Maison 11 — Communauté, amitiés, projets collectifs. Tu cherches à la fois l'efficacité (Capricorne) et la connexion spirituelle (Poissons).

**Ton approche instinctive** : Les Poissons te font rechercher des communautés où tu peux dissoudre ton ego, servir quelque chose de plus grand. Cette spiritualité peut enrichir ou créer du flou.

**Tensions possibles** : Organisation contre lâcher-prise collectif. Tu risques d'alterner entre contrôle rigide du groupe et abandon à la dynamique collective.

**Conseil clé** : Créer des structures qui permettent la magie collective. On peut organiser ET rester ouvert à l'inspiration du groupe.""",
        'weekly_advice': {
            'week_1': "Identifie une communauté ou un groupe qui nourrit ton âme.",
            'week_2': "Apporte ton organisation sans étouffer la magie.",
            'week_3': "Laisse aussi le groupe te transformer.",
            'week_4': "Célèbre la communauté à la fois structurée et inspirée."
        }
    },

    # ==================== MAISON 12 ====================

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Solitude conquise**

Ta Lune en Capricorne active ta Maison 12 : inconscient, spiritualité, solitude, dissolution de l'ego. Ton Ascendant Bélier veut affronter ces profondeurs avec courage. L'alliance de la discipline spirituelle et de l'audace intérieure.

**Domaine activé** : Maison 12 — Ton monde intérieur, tes peurs cachées, ta spiritualité. Tu cherches à maîtriser (Capricorne) ton inconscient par la confrontation directe (Bélier).

**Ton approche instinctive** : Le Bélier te pousse à affronter tes démons sans détour. Cette bravoure peut accélérer la guérison ou brusquer des processus qui demandent douceur.

**Tensions possibles** : Impatience face au travail intérieur qui prend du temps. Tu risques de vouloir forcer la guérison au lieu de la laisser se déployer.

**Conseil clé** : Affronter avec courage tout en respectant le rythme de l'inconscient. Certaines portes ne s'ouvrent que doucement.""",
        'weekly_advice': {
            'week_1': "Identifie une peur ou un schéma inconscient à affronter.",
            'week_2': "Plonge dans le travail intérieur avec courage.",
            'week_3': "Maintiens l'engagement même quand c'est inconfortable.",
            'week_4': "Reconnais la libération intérieure gagnée."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Paix structurée**

Ta Lune en Capricorne en Maison 12 cherche à comprendre et maîtriser son inconscient. Ton Ascendant Taureau veut ancrer la spiritualité dans le corps, créer une pratique stable. Double terre : une spiritualité pragmatique.

**Domaine activé** : Maison 12 — Spiritualité, retraite, inconscient. Tu cherches une pratique intérieure à la fois profonde (Maison 12) et concrète (double terre).

**Ton approche instinctive** : Le Taureau te fait construire lentement ta pratique spirituelle, ancrer la méditation dans le quotidien. Cette patience renforce le Capricorne discipliné.

**Tensions possibles** : Matérialisation excessive du spirituel. Tu risques de rester dans les formes sans toucher la vraie transcendance.

**Conseil clé** : Créer des structures qui soutiennent ton voyage intérieur tout en restant ouvert·e au mystère.""",
        'weekly_advice': {
            'week_1': "Établis une routine de pratique spirituelle ou méditative.",
            'week_2': "Maintiens-la avec constance, même brièvement.",
            'week_3': "Laisse aussi place à l'imprévu et à la grâce.",
            'week_4': "Apprécie la paix intérieure cultivée."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Inconscient analysé**

Ta Lune en Capricorne en Maison 12 veut structurer son monde intérieur. Ton Ascendant Gémeaux cherche à comprendre intellectuellement l'inconscient, à nommer les mystères. Le défi : allier analyse et lâcher-prise.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, dissolution. Tu cherches à comprendre (Gémeaux) et maîtriser (Capricorne) ce qui par nature échappe au contrôle.

**Ton approche instinctive** : Le Gémeaux te fait intellectualiser ton monde intérieur, chercher des mots pour l'indicible. Cette tendance peut éclairer ou éviter la vraie plongée spirituelle.

**Tensions possibles** : Rationalisation du mystère. Tu risques de rester dans l'analyse sans vivre l'expérience transcendante.

**Conseil clé** : Comprendre ce qui peut l'être ET accepter le mystère. L'inconscient ne se laisse pas totalement cartographier.""",
        'weekly_advice': {
            'week_1': "Étudie ton monde intérieur avec curiosité intellectuelle.",
            'week_2': "Expérimente aussi sans tout analyser.",
            'week_3': "Laisse certaines expériences rester ineffables.",
            'week_4': "Intègre ce que tu as compris ET ce qui reste mystérieux."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Refuge intérieur**

Ta Lune en Capricorne en Maison 12 cherche à structurer son monde intérieur. Ton Ascendant Cancer veut créer un sanctuaire émotionnel, un refuge de l'âme. L'axe Cancer-Capricorne : tension entre vulnérabilité et maîtrise.

**Domaine activé** : Maison 12 — Inconscient, retraite, besoin de solitude. Tu cherches à la fois la sécurité intérieure (Cancer) et la discipline spirituelle (Capricorne).

**Ton approche instinctive** : Le Cancer te fait chercher un refuge émotionnel dans la solitude, te retirer pour te ressourcer. Cette sensibilité peut humaniser le Capricorne trop rigide.

**Tensions possibles** : Isolement excessif par peur du monde. Tu risques de te réfugier dans ton monde intérieur au lieu de vivre.

**Conseil clé** : Cultiver ton jardin intérieur sans fuir le monde. La vraie force spirituelle inclut l'engagement.""",
        'weekly_advice': {
            'week_1': "Crée un espace de retraite intérieure sécurisant.",
            'week_2': "Ressource-toi dans la solitude quand nécessaire.",
            'week_3': "Reviens ensuite vers le monde avec ce que tu as trouvé.",
            'week_4': "Célèbre ton équilibre entre refuge et engagement."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Lumière cachée**

Ta Lune en Capricorne en Maison 12 cherche à maîtriser son inconscient et sa spiritualité. Ton Ascendant Lion veut briller même dans les profondeurs, transformer la solitude en rayonnement. L'alliance de la discipline et de la lumière.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, ce qui est caché. Tu cherches à illuminer (Lion) et structurer (Capricorne) ton monde intérieur.

**Ton approche instinctive** : Le Lion te pousse à transformer ton travail spirituel en source de rayonnement. Cette confiance peut inspirer ou créer un déni des zones d'ombre nécessaires.

**Tensions possibles** : Ego spirituel. Tu risques de vouloir briller même dans l'humilité, de transformer la spiritualité en performance.

**Conseil clé** : Accepter que certaines parties du chemin se font dans l'ombre. La vraie lumière naît de l'acceptation de l'obscurité.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu refuses de voir en toi par fierté.",
            'week_2': "Plonge dans ces zones d'ombre avec humilité.",
            'week_3': "Intègre ce que tu y trouves sans jugement.",
            'week_4': "Ressors avec une lumière plus authentique."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Purification méthodique**

Ta Lune en Capricorne en Maison 12 veut structurer son travail intérieur. Ton Ascendant Vierge ajoute analyse minutieuse, purification, perfectionnement spirituel. Double terre : une pratique spirituelle rigoureuse.

**Domaine activé** : Maison 12 — Inconscient, guérison, spiritualité. Tu cherches à purifier ton monde intérieur avec méthode et précision.

**Ton approche instinctive** : La Vierge te fait analyser chaque schéma inconscient, perfectionner ta pratique spirituelle. Cette minutie peut guérir ou devenir obsessionnelle.

**Tensions possibles** : Perfectionnisme spirituel. Tu risques de te critiquer sans cesse, de ne jamais te sentir assez "purifié·e".

**Conseil clé** : Viser la guérison progressive, pas la pureté absolue. L'acceptation de soi fait partie du chemin spirituel.""",
        'weekly_advice': {
            'week_1': "Identifie un schéma inconscient à guérir avec douceur.",
            'week_2': "Travaille dessus méthodiquement mais avec bienveillance.",
            'week_3': "Accepte les imperfections comme partie du processus.",
            'week_4': "Célèbre la guérison progressive, pas la perfection."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Paix équilibrée**

Ta Lune en Capricorne en Maison 12 veut maîtriser son monde intérieur avec discipline. Ton Ascendant Balance cherche harmonie spirituelle, équilibre entre conscient et inconscient. Le défi : allier structure et fluidité intérieure.

**Domaine activé** : Maison 12 — Spiritualité, inconscient, retraite. Tu cherches une paix intérieure à la fois structurée (Capricorne) et harmonieuse (Balance).

**Ton approche instinctive** : La Balance te fait chercher l'équilibre dans ta pratique spirituelle, éviter les extrêmes. Cette modération peut stabiliser ou créer de la superficialité.

**Tensions possibles** : Hésitation à plonger vraiment dans les profondeurs par peur du déséquilibre. Tu risques de rester en surface par souci d'harmonie.

**Conseil clé** : Accepter que le vrai équilibre passe parfois par des déséquilibres temporaires. La transformation spirituelle n'est pas toujours confortable.""",
        'weekly_advice': {
            'week_1': "Identifie où tu évites la profondeur par souci d'équilibre.",
            'week_2': "Ose plonger même si c'est inconfortable.",
            'week_3': "Fais confiance au rééquilibrage naturel qui suit.",
            'week_4': "Apprécie la paix plus profonde qui émerge."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Mort initiatique**

Ta Lune en Capricorne en Maison 12 cherche à maîtriser son inconscient et sa spiritualité. Ton Ascendant Scorpion veut plonger dans les profondeurs absolues, mourir et renaître spirituellement. L'alliance de la structure et de la transformation radicale.

**Domaine activé** : Maison 12 — Inconscient profond, transformation spirituelle, dissolution de l'ego. Tu ne cherches pas une spiritualité légère : tu veux la métamorphose totale.

**Ton approche instinctive** : Le Scorpion te pousse à affronter tes démons les plus cachés, à ne fuir aucune profondeur. Cette intensité renforce le Capricorne qui valorise le travail en profondeur.

**Tensions possibles** : Obsession du travail intérieur. Tu risques de te perdre dans les profondeurs ou de devenir trop intense dans ta quête spirituelle.

**Conseil clé** : Plonger avec courage ET sagesse. La transformation radicale demande aussi de l'ancrage pour ne pas se perdre.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit vraiment mourir en toi spirituellement.",
            'week_2': "Plonge dans ce processus de mort initiatique.",
            'week_3': "Maintiens un ancrage pendant la traversée.",
            'week_4': "Émerge transformé·e et renais plus authentique."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foi structurée**

Ta Lune en Capricorne en Maison 12 veut maîtriser son monde intérieur avec discipline. Ton Ascendant Sagittaire cherche foi, vision spirituelle expansive, sens philosophique. Le défi : allier rigueur et foi.

**Domaine activé** : Maison 12 — Spiritualité, foi, inconscient. Tu cherches une pratique spirituelle à la fois disciplinée (Capricorne) et inspirante (Sagittaire).

**Ton approche instinctive** : Le Sagittaire te fait chercher le sens ultime dans ta quête spirituelle. Cette vision peut enrichir le Capricorne ou créer des croyances irréalistes.

**Tensions possibles** : Foi naïve contre scepticisme rigide. Tu risques d'alterner entre optimisme spirituel aveugle et cynisme désenchanté.

**Conseil clé** : Cultiver une foi mature, basée sur l'expérience ET sur la vision. La vraie spiritualité allie rigueur et inspiration.""",
        'weekly_advice': {
            'week_1': "Explore une pratique spirituelle qui t'inspire vraiment.",
            'week_2': "Teste-la concrètement avec discipline.",
            'week_3': "Ajuste selon l'expérience sans perdre la foi.",
            'week_4': "Intègre une spiritualité à la fois mature et vivante."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Ascèse pure**

Ta Lune en Capricorne en Maison 12 avec Ascendant Capricorne crée une triple concentration sur la maîtrise spirituelle, la discipline intérieure, le contrôle de l'inconscient. L'énergie est tournée vers l'ascèse.

**Domaine activé** : Maison 12 — Spiritualité, inconscient, retraite. Tu cherches la maîtrise de soi avec le plus haut niveau de discipline et de rigueur intérieure.

**Ton approche instinctive** : Triple Capricorne : tu abordes la spiritualité comme une montagne à gravir, avec méthode et austérité. Cette rigueur peut créer une vraie sagesse mais aussi une sécheresse spirituelle.

**Tensions possibles** : Austérité excessive, refoulement au nom de la maîtrise. Tu risques de te couper de tes émotions et de ta vitalité.

**Conseil clé** : Se rappeler que la vraie spiritualité libère, elle n'emprisonne pas. La discipline intérieure peut coexister avec la joie.""",
        'weekly_advice': {
            'week_1': "Examine si ta pratique spirituelle te libère ou te rigidifie.",
            'week_2': "Maintiens la discipline sans devenir austère.",
            'week_3': "Autorise-toi aussi la douceur et la compassion pour toi-même.",
            'week_4': "Célèbre une spiritualité à la fois rigoureuse et vivante."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Libération structurée**

Ta Lune en Capricorne en Maison 12 veut maîtriser son inconscient avec discipline. Ton Ascendant Verseau cherche libération, détachement, approche non conventionnelle de la spiritualité. Le défi : allier structure et liberté intérieure.

**Domaine activé** : Maison 12 — Spiritualité, inconscient, libération. Tu cherches à te libérer (Verseau) par la discipline (Capricorne).

**Ton approche instinctive** : Le Verseau te fait explorer des voies spirituelles originales, te détacher des formes conventionnelles. Cette originalité peut libérer ou créer une fuite dans l'excentricité.

**Tensions possibles** : Rébellion contre toute structure spirituelle. Tu risques de rejeter toute discipline au nom de la liberté.

**Conseil clé** : Comprendre que certaines structures libèrent. La vraie liberté spirituelle peut naître de la discipline choisie.""",
        'weekly_advice': {
            'week_1': "Explore une pratique spirituelle originale mais sérieuse.",
            'week_2': "Maintiens une certaine discipline sans rigidité.",
            'week_3': "Laisse aussi place à la spontanéité et à la grâce.",
            'week_4': "Célèbre ta spiritualité à la fois libre et ancrée."
        }
    },

    {
        'moon_sign': 'Capricorn', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution sacrée**

Ta Lune en Capricorne en Maison 12 veut structurer son monde intérieur et sa spiritualité. Ton Ascendant Poissons, maître naturel de cette maison, cherche dissolution de l'ego, fusion mystique, abandon au divin. La rencontre entre contrôle et lâcher-prise absolu.

**Domaine activé** : Maison 12 — Spiritualité, transcendance, dissolution. Tu cherches à la fois la maîtrise (Capricorne) et la fusion mystique (Poissons).

**Ton approche instinctive** : Les Poissons te poussent à lâcher prise totalement, à te dissoudre dans le divin. Cette tendance peut libérer le Capricorne trop rigide ou créer une perte de structure dangereuse.

**Tensions possibles** : Oscillation entre contrôle rigide et abandon total. Tu risques d'alterner entre maîtrise excessive et perte de frontières.

**Conseil clé** : Créer un cadre qui permet le lâcher-prise sécurisé. On peut structurer le chemin vers la dissolution sans bloquer la grâce.""",
        'weekly_advice': {
            'week_1': "Établis un cadre sécurisant pour ta pratique spirituelle.",
            'week_2': "Dans ce cadre, autorise-toi à lâcher prise complètement.",
            'week_3': "Fais confiance à l'univers sans perdre ton ancrage.",
            'week_4': "Intègre l'expérience mystique dans ta vie structurée."
        }
    },

]

if __name__ == "__main__":
    asyncio.run(insert_batch(BATCH))
