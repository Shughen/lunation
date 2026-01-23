"""Batch: Aries M2 - 12 ascendants"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Conquête matérielle**

Ta Lune en Bélier en Maison 2 active tes besoins de sécurité et de ressources avec une énergie combative. Avec l'ascendant lunaire Bélier, tu fonces vers ce que tu veux posséder, gagner, obtenir. Ton rapport à l'argent et aux valeurs est direct, impulsif.

**Domaine activé** : Maison 2 — Tes finances, tes possessions, ta valeur personnelle sont au cœur de ce cycle. Tu ressens une urgence de construire ta sécurité matérielle, d'affirmer ce que tu vaux.

**Ton approche instinctive** : Double Bélier signifie action immédiate. Tu veux des résultats maintenant. Les opportunités financières t'attirent, surtout celles qui demandent de l'audace.

**Tensions possibles** : L'impulsivité peut mener à des dépenses compulsives ou des investissements risqués. Le besoin de gratification immédiate nuit à l'épargne.

**Conseil clé** : Transformer ton énergie d'action en construction patiente de tes ressources.""",
        'weekly_advice': {
            'week_1': "Fais le point sur tes finances. Où en es-tu vraiment ?",
            'week_2': "Lance une initiative pour augmenter tes revenus.",
            'week_3': "Résiste aux achats impulsifs cette semaine.",
            'week_4': "Définis une stratégie financière pour le mois prochain."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sécurité active**

Ta Lune en Bélier en Maison 2 te pousse à agir pour ta sécurité matérielle. L'ascendant lunaire Taureau renforce cette dimension : tu veux du concret, du solide, du durable. L'argent n'est pas un but mais un moyen de te sentir ancré·e.

**Domaine activé** : Maison 2 — Tes ressources, tes talents, ta valeur propre sont activés. Tu cherches à stabiliser tes finances et à affirmer ce que tu apportes au monde.

**Ton approche instinctive** : Le Taureau te fait chercher la sécurité avant tout. Tu prends le temps de vérifier la solidité avant d'investir ton énergie. Cette prudence équilibre l'impulsivité Bélier.

**Tensions possibles** : Le Bélier veut bouger vite, le Taureau veut être sûr. Tu peux te sentir freiné·e par ton propre besoin de certitudes.

**Conseil clé** : Construire ta sécurité financière par des actions régulières plutôt qu'un grand coup.""",
        'weekly_advice': {
            'week_1': "Identifie une source de revenus stable à développer.",
            'week_2': "Mets en place une routine d'épargne, même petite.",
            'week_3': "Valorise tes talents concrets. Qu'as-tu à offrir ?",
            'week_4': "Fais le bilan de ta solidité financière."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Valeurs multiples**

Ta Lune en Bélier en Maison 2 veut agir pour sécuriser ses ressources. L'ascendant lunaire Gémeaux disperse cette énergie vers plusieurs pistes : tu explores différentes sources de revenus, différentes façons de valoriser tes talents.

**Domaine activé** : Maison 2 — Ton rapport à l'argent, à ce que tu possèdes et à ta valeur personnelle est stimulé. Tu repenses ce qui compte vraiment pour toi.

**Ton approche instinctive** : Le Gémeaux te fait comparer, analyser, diversifier. Tu cherches l'information avant d'investir. Les opportunités liées à la communication ou au commerce t'attirent.

**Tensions possibles** : Tu risques de t'éparpiller entre trop d'options financières sans en approfondir aucune. L'indécision peut bloquer l'action.

**Conseil clé** : Choisir deux ou trois pistes maximum et les creuser vraiment.""",
        'weekly_advice': {
            'week_1': "Explore tes options financières sans t'engager encore.",
            'week_2': "Sélectionne la piste la plus prometteuse et agis.",
            'week_3': "Communique sur ta valeur. Fais-toi connaître.",
            'week_4': "Évalue ce qui a marché. Simplifie pour la suite."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sécurité émotionnelle**

Ta Lune en Bélier en Maison 2 active tes besoins matériels avec urgence. L'ascendant lunaire Cancer lie profondément sécurité financière et sécurité émotionnelle. L'argent représente pour toi un cocon protecteur.

**Domaine activé** : Maison 2 — Tes ressources et ta valeur personnelle sont au centre. Tu cherches à créer une base solide qui te permette de te sentir émotionnellement en sécurité.

**Ton approche instinctive** : Le Cancer te fait agir pour protéger, nourrir, sécuriser. Tes décisions financières sont influencées par tes émotions. La famille peut jouer un rôle dans tes ressources.

**Tensions possibles** : L'impulsivité Bélier peut faire des achats émotionnels regrettables. L'anxiété Cancer peut bloquer les prises de risque nécessaires.

**Conseil clé** : Créer un matelas de sécurité qui apaise ton besoin émotionnel tout en restant actif·ve.""",
        'weekly_advice': {
            'week_1': "Examine le lien entre tes émotions et tes dépenses.",
            'week_2': "Crée un fonds de sécurité, même symbolique.",
            'week_3': "Ne laisse pas l'anxiété dicter tes choix financiers.",
            'week_4': "Célèbre ce que tu as construit ce mois-ci."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Valeur rayonnante**

Ta Lune en Bélier en Maison 2 veut conquérir des ressources. L'ascendant lunaire Lion ajoute une dimension de fierté et de générosité. Tu veux non seulement avoir, mais avoir avec style, montrer ta réussite.

**Domaine activé** : Maison 2 — Ta valeur personnelle, tes talents, tes finances sont au premier plan. Tu ressens le besoin d'être reconnu·e pour ce que tu apportes et ce que tu possèdes.

**Ton approche instinctive** : Le Lion te fait viser haut et grand. Tu n'es pas intéressé·e par la médiocrité financière. Tu veux briller aussi dans ce domaine.

**Tensions possibles** : Le besoin de paraître peut mener à des dépenses excessives. L'orgueil peut t'empêcher de demander de l'aide ou d'accepter un travail "en dessous" de toi.

**Conseil clé** : Investir dans ce qui reflète vraiment ta valeur, pas seulement ton image.""",
        'weekly_advice': {
            'week_1': "Affirme ta valeur professionnelle avec confiance.",
            'week_2': "Investis dans quelque chose qui te fait briller durablement.",
            'week_3': "Sois généreux·se mais pas au détriment de tes besoins.",
            'week_4': "Mesure ta valeur à ce que tu crées, pas à ce que tu possèdes."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Gestion efficace**

Ta Lune en Bélier en Maison 2 te pousse à agir sur tes finances. L'ascendant lunaire Vierge canalise cette énergie vers l'organisation, l'analyse, l'optimisation. Tu veux non seulement gagner mais bien gérer.

**Domaine activé** : Maison 2 — Tes ressources, tes compétences pratiques, ta capacité à produire de la valeur sont au centre. Tu analyses ce qui fonctionne et ce qui doit être amélioré.

**Ton approche instinctive** : La Vierge te fait détailler, budgétiser, planifier. Tu cherches l'efficacité maximale dans l'utilisation de tes ressources. Chaque euro compte.

**Tensions possibles** : L'impulsivité Bélier peut se frustrer face à la méticulosité Vierge. Tu risques soit de trop analyser, soit d'agir sans plan.

**Conseil clé** : Allier l'élan d'action à une gestion précise — agir vite, mais avec méthode.""",
        'weekly_advice': {
            'week_1': "Fais un budget détaillé de ta situation actuelle.",
            'week_2': "Identifie une compétence monétisable à développer.",
            'week_3': "Optimise une dépense récurrente.",
            'week_4': "Analyse ce qui a marché financièrement ce mois-ci."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Valeur partagée**

Ta Lune en Bélier en Maison 2 veut conquérir des ressources personnelles. L'ascendant lunaire Balance introduit la dimension relationnelle : tes finances sont liées aux autres, aux partenariats, aux collaborations.

**Domaine activé** : Maison 2 — Ta valeur personnelle et tes ressources sont activées, mais à travers le prisme des relations. Les questions de "qui apporte quoi" émergent.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre, le juste partage, la beauté aussi. Tu es attiré·e par les investissements esthétiques ou relationnels.

**Tensions possibles** : Le Bélier veut tout pour lui, la Balance veut partager. Tu peux te sentir tiraillé·e entre tes intérêts et ceux des autres.

**Conseil clé** : Créer des partenariats financiers équitables qui servent tes intérêts aussi.""",
        'weekly_advice': {
            'week_1': "Clarifie ta contribution dans tes partenariats financiers.",
            'week_2': "N'hésite pas à négocier ce que tu mérites.",
            'week_3': "Trouve un équilibre entre donner et recevoir.",
            'week_4': "Évalue si tes relations financières sont justes."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir financier**

Ta Lune en Bélier en Maison 2 veut agir sur tes ressources. L'ascendant lunaire Scorpion ajoute une dimension de profondeur et de contrôle. Tu veux non seulement avoir mais maîtriser, transformer ta situation financière.

**Domaine activé** : Maison 2 — Tes ressources, tes valeurs profondes, ce à quoi tu tiens vraiment sont au cœur du cycle. Des questions de pouvoir liées à l'argent peuvent émerger.

**Ton approche instinctive** : Le Scorpion te fait creuser, investiguer, contrôler. Tu veux comprendre les mécanismes financiers, trouver les leviers cachés.

**Tensions possibles** : L'obsession du contrôle peut créer de l'anxiété. Le tout-ou-rien Scorpion peut mener à des paris financiers risqués.

**Conseil clé** : Utiliser ton intensité pour transformer durablement ta situation financière.""",
        'weekly_advice': {
            'week_1': "Examine tes croyances profondes sur l'argent.",
            'week_2': "Identifie un levier financier inexploité.",
            'week_3': "Lâche le besoin de tout contrôler.",
            'week_4': "Observe la transformation opérée dans ton rapport à l'argent."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Abondance optimiste**

Ta Lune en Bélier en Maison 2 active tes ressources avec énergie. L'ascendant lunaire Sagittaire ajoute optimisme et vision large. Tu crois en l'abondance, tu vises grand, parfois au-delà du réaliste.

**Domaine activé** : Maison 2 — Tes finances, tes talents, ta valeur sont expansifs ce mois-ci. Tu ressens que les limites peuvent être repoussées, que plus est possible.

**Ton approche instinctive** : Le Sagittaire te fait voir les opportunités partout. Tu es attiré·e par les investissements à l'étranger, les formations, tout ce qui élargit tes horizons financiers.

**Tensions possibles** : L'excès d'optimisme peut mener à des dépenses excessives ou des investissements hasardeux. Le détail financier t'ennuie.

**Conseil clé** : Garder ta vision large tout en vérifiant les fondamentaux pratiques.""",
        'weekly_advice': {
            'week_1': "Définis une vision ambitieuse pour tes finances.",
            'week_2': "Investis dans ta formation ou ton développement.",
            'week_3': "Vérifie que ton optimisme repose sur du concret.",
            'week_4': "Célèbre l'expansion accomplie, prépare la suite."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Construction solide**

Ta Lune en Bélier en Maison 2 veut agir vite sur tes ressources. L'ascendant lunaire Capricorne structure cette impulsion vers le long terme. Tu veux bâtir une sécurité durable, pas juste un gain immédiat.

**Domaine activé** : Maison 2 — Tes finances, ta valeur professionnelle, tes actifs sont au centre. Tu penses en termes de patrimoine, d'investissement, de construction.

**Ton approche instinctive** : Le Capricorne te fait planifier, structurer, patienter si nécessaire. Tu acceptes de sacrifier le présent pour le futur. La discipline financière t'attire.

**Tensions possibles** : L'impatience Bélier peut s'irriter de la lenteur Capricorne. Tu risques de te priver excessivement ou de trop travailler pour l'argent.

**Conseil clé** : Allier l'énergie d'action du Bélier à la patience stratégique du Capricorne.""",
        'weekly_advice': {
            'week_1': "Définis un objectif financier à 6 mois.",
            'week_2': "Mets en place une structure d'épargne automatique.",
            'week_3': "Investis ton énergie dans ce qui a une valeur durable.",
            'week_4': "Évalue tes fondations financières. Sont-elles solides ?"
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Valeur innovante**

Ta Lune en Bélier en Maison 2 active tes ressources avec dynamisme. L'ascendant lunaire Verseau apporte originalité et détachement. Tu cherches des moyens non conventionnels de créer de la valeur.

**Domaine activé** : Maison 2 — Tes finances, tes talents, ta valeur propre sont revisités sous un angle innovant. Les sources de revenus traditionnelles t'ennuient.

**Ton approche instinctive** : Le Verseau te fait chercher l'original, le différent, le futuriste. Les cryptos, la tech, l'économie collaborative t'attirent.

**Tensions possibles** : L'attrait du nouveau peut te faire négliger les bases solides. Le détachement Verseau peut rendre difficile l'engagement financier durable.

**Conseil clé** : Innover dans tes sources de revenus tout en gardant un socle stable.""",
        'weekly_advice': {
            'week_1': "Explore une source de revenus non conventionnelle.",
            'week_2': "Teste une nouvelle approche financière à petite échelle.",
            'week_3': "Équilibre innovation et sécurité.",
            'week_4': "Évalue ce qui mérite d'être poursuivi."
        }
    },
    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Valeur intuitive**

Ta Lune en Bélier en Maison 2 veut agir sur tes ressources. L'ascendant lunaire Poissons ajoute une dimension intuitive et parfois floue. Ton rapport à l'argent est émotionnel, créatif, pas toujours rationnel.

**Domaine activé** : Maison 2 — Tes finances, tes talents artistiques ou spirituels, ta valeur intangible sont activés. Tu cherches un sens au-delà du matériel.

**Ton approche instinctive** : Le Poissons te fait ressentir les opportunités plus que les analyser. Tu peux avoir des intuitions financières justes ou te perdre dans des illusions.

**Tensions possibles** : L'impulsivité Bélier combinée au flou Poissons peut mener à des décisions financières confuses. La limite entre générosité et sacrifice de soi est poreuse.

**Conseil clé** : Écouter ton intuition financière tout en vérifiant les faits concrets.""",
        'weekly_advice': {
            'week_1': "Note tes intuitions sur l'argent cette semaine.",
            'week_2': "Valorise tes talents créatifs ou spirituels.",
            'week_3': "Vérifie que ta générosité ne te met pas en danger.",
            'week_4': "Fais le tri entre intuition juste et illusion."
        }
    }
]

if __name__ == "__main__":
    asyncio.run(insert_batch(BATCH))
    print(f"\n[BATCH] Aries M2 complete - 24/1728")
