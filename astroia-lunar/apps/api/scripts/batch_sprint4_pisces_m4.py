"""
Batch Sprint 4 - Pisces M4 - 10 ascendants manquants
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
        "moon_house": 4,
        "lunar_ascendant": "Gemini",
        "interpretation": """**Ton mois en un mot : Intimité bavarde**

Ta Lune en Poissons en Maison 4 cherche la fusion émotionnelle avec tes racines familiales. Ton Ascendant Gémeaux ajoute une touche de légèreté : tu veux parler de tes émotions, les raconter, les partager. L'introspection devient bavarde.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines émotionnelles sont au centre. Tu ressens le besoin de te retirer chez toi tout en restant connecté·e par la parole et l'échange.

**Ton approche instinctive** : Le Gémeaux te fait transformer tes ressentis en mots. Tu explores ton monde intérieur en le verbalisant, parfois au risque de disperser tes émotions au lieu de les accueillir pleinement.

**Tensions possibles** : La profondeur émotionnelle des Poissons peut être diluée par la légèreté du Gémeaux. Tu risques de papillonner entre différentes émotions sans vraiment t'y plonger.

**Conseil clé** : Écrire un journal intime pour canaliser tes mots et honorer ta profondeur émotionnelle.""",
        "weekly_advice": {
            "week_1": "Crée un espace de discussion intime avec un proche de confiance.",
            "week_2": "Écris une lettre à ton enfant intérieur pour clarifier tes émotions.",
            "week_3": "Partage une histoire familiale qui t'émeut avec quelqu'un.",
            "week_4": "Médite en silence pour accueillir ce qui ne peut être dit."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Cancer",
        "interpretation": """**Ton mois en un mot : Cocon émotionnel**

Ta Lune en Poissons en Maison 4 rencontre ton Ascendant Cancer dans une fusion totale eau-eau. C'est un mois d'immersion émotionnelle profonde où ton foyer devient un sanctuaire de douceur et de vulnérabilité assumée.

**Domaine activé** : Maison 4 — Ton foyer et ta famille sont au cœur de ce mois. Tu ressens un besoin viscéral de sécurité émotionnelle, de retrouver tes racines et de te laisser porter par tes émotions les plus tendres.

**Ton approche instinctive** : Le Cancer triple cette sensibilité. Tu accueilles les émotions de tous, tu nourris et protèges ton cercle intime. Cette empathie peut être magnifique ou épuisante selon tes limites.

**Tensions possibles** : Risque de submersion émotionnelle et de confusion entre tes besoins et ceux des autres. Tu peux te perdre dans les émotions familiales et oublier ta propre identité.

**Conseil clé** : Créer un rituel quotidien de recentrage pour ne pas te noyer dans les émotions collectives.""",
        "weekly_advice": {
            "week_1": "Prépare un repas réconfortant pour toi et tes proches avec amour.",
            "week_2": "Prends un bain rituel pour te laver des émotions absorbées.",
            "week_3": "Écris sur tes limites émotionnelles et ce qui est vraiment tien.",
            "week_4": "Offre-toi une journée cocooning totale chez toi, seul·e."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Leo",
        "interpretation": """**Ton mois en un mot : Vulnérabilité royale**

Ta Lune en Poissons en Maison 4 cherche l'humilité et la dissolution dans ton intimité. Ton Ascendant Lion ajoute une touche de fierté : tu veux être noble même dans ta vulnérabilité, rayonner depuis ton cocon.

**Domaine activé** : Maison 4 — Ton foyer devient une scène privée où tu peux exprimer ta sensibilité avec dignité. Tu cherches à créer un environnement qui honore ta grandeur intérieure tout en accueillant ta fragilité.

**Ton approche instinctive** : Le Lion te pousse à transformer ton intimité en quelque chose de beau et généreux. Tu veux nourrir les tiens avec panache, créer de la magie familiale même dans les moments de repli.

**Tensions possibles** : Conflit entre ton besoin de te retirer et ton envie d'être vu·e et apprécié·e. Tu risques de dramatiser tes émotions pour attirer l'attention ou de cacher ta vraie vulnérabilité.

**Conseil clé** : Accepter que la vraie noblesse se trouve dans l'authenticité de tes émotions, pas dans leur mise en scène.""",
        "weekly_advice": {
            "week_1": "Crée un espace magnifique chez toi qui honore ta sensibilité.",
            "week_2": "Partage une émotion profonde avec fierté et sans honte.",
            "week_3": "Organise un moment familial chaleureux où tu peux briller dans ta douceur.",
            "week_4": "Médite sur l'humilité : accueille ta vulnérabilité sans besoin de reconnaissance."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Virgo",
        "interpretation": """**Ton mois en un mot : Ordre sensible**

Ta Lune en Poissons en Maison 4 veut se dissoudre dans l'océan émotionnel familial. Ton Ascendant Vierge apporte structure et discernement : tu veux organiser ton chaos intérieur, trier tes émotions, purifier ton foyer.

**Domaine activé** : Maison 4 — Ton foyer et tes racines sont au centre. Tu ressens le besoin de créer de l'ordre dans ton espace intime tout en accueillant le flou émotionnel des Poissons.

**Ton approche instinctive** : La Vierge te fait analyser tes sentiments familiaux, ranger ton intérieur physique et psychique. Cette tentative de contrôle peut t'aider ou te couper de tes émotions.

**Tensions possibles** : L'opposition entre le chaos créatif des Poissons et le besoin d'ordre de la Vierge peut créer de la frustration. Tu risques de juger tes émotions au lieu de les accueillir.

**Conseil clé** : Créer des rituels de purification qui honorent le désordre émotionnel sans chercher à tout contrôler.""",
        "weekly_advice": {
            "week_1": "Range un espace de ton foyer en écoutant tes émotions surgir.",
            "week_2": "Écris une liste de tes besoins émotionnels pour y voir plus clair.",
            "week_3": "Offre un service concret à ta famille avec amour et humilité.",
            "week_4": "Accepte que certaines émotions ne peuvent être \"résolues\" ou rangées."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Libra",
        "interpretation": """**Ton mois en un mot : Harmonie familiale**

Ta Lune en Poissons en Maison 4 cherche la fusion avec tes racines. Ton Ascendant Balance ajoute un besoin d'équilibre et d'esthétique : tu veux créer une atmosphère harmonieuse dans ton foyer, apaiser les tensions familiales.

**Domaine activé** : Maison 4 — Ton foyer devient un espace de beauté et de paix. Tu ressens le besoin de créer de l'harmonie entre tous les membres de ta famille, parfois au détriment de tes propres besoins.

**Ton approche instinctive** : La Balance te fait jouer le rôle de médiateur familial, chercher le juste milieu émotionnel. Cette quête d'équilibre peut t'empêcher de plonger dans tes propres profondeurs.

**Tensions possibles** : Tu risques de te perdre en cherchant à plaire à tout le monde dans ta famille. L'indécision de la Balance peut t'empêcher d'honorer ta vérité émotionnelle.

**Conseil clé** : Trouver l'équilibre entre accueillir les autres et honorer tes propres besoins émotionnels.""",
        "weekly_advice": {
            "week_1": "Embellis ton foyer avec des éléments qui t'apaisent vraiment.",
            "week_2": "Médite pour clarifier ce qui est ton émotion et ce qui est celle des autres.",
            "week_3": "Organise un moment de réconciliation ou de dialogue familial.",
            "week_4": "Ose dire non à ce qui déséquilibre ta paix intérieure."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Scorpio",
        "interpretation": """**Ton mois en un mot : Profondeurs ancestrales**

Ta Lune en Poissons en Maison 4 veut se dissoudre dans les eaux familiales. Ton Ascendant Scorpion plonge encore plus profond : tu explores les secrets de famille, les non-dits, les blessures transgénérationnelles.

**Domaine activé** : Maison 4 — Ton foyer et tes racines sont le terrain d'une transformation émotionnelle intense. Tu ressens le besoin de toucher le fond de tes héritages familiaux pour mieux renaître.

**Ton approche instinctive** : Le Scorpion te fait fouiller dans l'ombre familiale, révéler ce qui est caché. Cette intensité peut libérer ou bouleverser, mais elle ne laisse jamais indifférent·e.

**Tensions possibles** : L'intensité émotionnelle peut devenir obsessionnelle. Tu risques de te noyer dans les drames familiaux ou de forcer des révélations qui ne sont pas prêtes à émerger.

**Conseil clé** : Honorer les mystères familiaux sans tout déterrer, transformer ce qui est prêt à l'être.""",
        "weekly_advice": {
            "week_1": "Explore une blessure familiale ancienne avec bienveillance.",
            "week_2": "Crée un rituel de libération des schémas familiaux toxiques.",
            "week_3": "Partage un secret de famille qui pèse, si le moment est juste.",
            "week_4": "Laisse mourir ce qui doit partir pour faire place au renouveau."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Sagittarius",
        "interpretation": """**Ton mois en un mot : Foyer nomade**

Ta Lune en Poissons en Maison 4 cherche un refuge émotionnel. Ton Ascendant Sagittaire ajoute une soif de liberté et d'expansion : tu veux un foyer qui soit à la fois cocon et point de départ vers l'ailleurs.

**Domaine activé** : Maison 4 — Ton foyer est au centre, mais tu le vis comme un camp de base pour tes explorations intérieures. Tu ressens le besoin de racines qui ne t'enferment pas.

**Ton approche instinctive** : Le Sagittaire te fait chercher du sens dans tes racines, explorer d'autres cultures ou philosophies familiales. Cette quête peut t'éloigner de l'intimité simple que cherchent les Poissons.

**Tensions possibles** : Conflit entre ton besoin de te poser et ton envie de t'échapper. Tu risques de fuir l'intimité familiale en intellectualisant ou en voyageant.

**Conseil clé** : Trouver un sens profond à tes racines qui nourrisse ton besoin d'expansion plutôt que de l'entraver.""",
        "weekly_advice": {
            "week_1": "Explore les origines de ta famille, leur histoire de migration.",
            "week_2": "Crée un espace chez toi qui évoque l'ailleurs et l'aventure.",
            "week_3": "Partage avec ta famille une vision ou un rêve qui t'inspire.",
            "week_4": "Médite sur ce que signifie être libre tout en ayant des racines."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Capricorn",
        "interpretation": """**Ton mois en un mot : Structure fluide**

Ta Lune en Poissons en Maison 4 veut se dissoudre dans l'océan familial. Ton Ascendant Capricorne cherche à construire des fondations solides : tu veux créer un foyer structuré tout en honorant ta sensibilité.

**Domaine activé** : Maison 4 — Ton foyer et tes racines demandent à être consolidés. Tu ressens le besoin de responsabilité familiale, de prendre soin de tes bases émotionnelles avec maturité.

**Ton approche instinctive** : Le Capricorne te fait aborder ton intimité avec sérieux et discipline. Cette structure peut protéger ta sensibilité ou l'étouffer sous le poids des obligations.

**Tensions possibles** : La rigidité du Capricorne peut bloquer la fluidité des Poissons. Tu risques de te sentir coupable de tes émotions ou de les sacrifier au nom du devoir familial.

**Conseil clé** : Construire des structures familiales qui soutiennent ta sensibilité au lieu de la contraindre.""",
        "weekly_advice": {
            "week_1": "Identifie une responsabilité familiale que tu peux assumer avec amour.",
            "week_2": "Crée une routine chez toi qui honore tes besoins émotionnels.",
            "week_3": "Dialogue avec un aîné de ta famille sur la transmission et l'héritage.",
            "week_4": "Permets-toi de pleurer ou de lâcher prise sans culpabilité."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Aquarius",
        "interpretation": """**Ton mois en un mot : Famille universelle**

Ta Lune en Poissons en Maison 4 cherche la fusion avec tes racines. Ton Ascendant Verseau élargit cette vision : ta famille devient l'humanité entière, ton foyer s'ouvre au collectif et à l'innovation.

**Domaine activé** : Maison 4 — Ton foyer se transforme en espace d'expérimentation sociale. Tu ressens le besoin de repenser ce que signifie "famille" et de créer une intimité qui respecte ta liberté.

**Ton approche instinctive** : Le Verseau te fait aborder ton intimité de façon non-conventionnelle. Tu cherches à libérer les schémas familiaux traditionnels, parfois au risque de te couper de tes racines émotionnelles.

**Tensions possibles** : Le détachement du Verseau peut t'empêcher de plonger dans la vulnérabilité des Poissons. Tu risques d'intellectualiser tes émotions familiales au lieu de les ressentir.

**Conseil clé** : Honorer ton besoin de liberté tout en acceptant ta dépendance émotionnelle aux liens familiaux.""",
        "weekly_advice": {
            "week_1": "Imagine une structure familiale alternative qui te ressemble.",
            "week_2": "Invite chez toi des ami·es qui sont ta famille de cœur.",
            "week_3": "Libère-toi d'un schéma familial qui ne te sert plus.",
            "week_4": "Accepte ta vulnérabilité émotionnelle malgré ton besoin d'indépendance."
        }
    },
    {
        "moon_sign": "Pisces",
        "moon_house": 4,
        "lunar_ascendant": "Pisces",
        "interpretation": """**Ton mois en un mot : Océan intérieur**

Triple Poissons sur ton foyer : Lune, Maison 4 et Ascendant. C'est un mois d'immersion totale dans tes émotions familiales et tes racines. La sensibilité est à son maximum, la porosité émotionnelle aussi.

**Domaine activé** : Maison 4 — Ton foyer devient un sanctuaire spirituel, un espace de dissolution de l'ego. Tu ressens un besoin profond de retrouver ton essence à travers tes racines et ton intimité.

**Ton approche instinctive** : Triple Poissons te fait naviguer dans les eaux émotionnelles sans boussole. Cette fluidité peut être libératrice ou désorientante selon ta capacité à accepter le mystère.

**Tensions possibles** : Risque de fusion totale avec les émotions familiales au point de perdre tes limites. Tu peux te sentir submergé·e, perdu·e, incapable de distinguer où tu commences et où les autres finissent.

**Conseil clé** : Créer des rituels d'ancrage quotidiens pour ne pas te dissoudre complètement dans l'océan émotionnel.""",
        "weekly_advice": {
            "week_1": "Crée un autel ou un espace sacré chez toi pour ton âme.",
            "week_2": "Médite sur tes limites : où finis-tu, où commencent les autres?",
            "week_3": "Plonge consciemment dans une émotion familiale puis reviens à toi.",
            "week_4": "Prends un bain rituel pour te laver des énergies absorbées."
        }
    }
]

if __name__ == "__main__":
    print(f"[*] Batch: Pisces M4 - {len(BATCH)} interprétations")
    asyncio.run(insert_batch(BATCH))
    print(f"[✓] Pisces M4 terminé")
