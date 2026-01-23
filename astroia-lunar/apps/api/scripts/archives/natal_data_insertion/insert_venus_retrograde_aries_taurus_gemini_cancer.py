#!/usr/bin/env python3
"""
Insert venus_retrograde interpretations V2 for Aries, Taurus, Gemini, Cancer (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

VENUS_RETROGRADE_INTERPRETATIONS = {
    # ============== ARIES (Bélier) ==============
    ('aries', 1): """# ♀℞ Vénus rétrograde en Bélier — Maison 1

**En une phrase :** Ta façon de te présenter en amour et ta relation à ta propre beauté sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde en Bélier dans ta maison 1 remet en question ta façon de séduire et de te montrer. Tu peux avoir été trop direct·e ou impulsif·ve en amour. C'est le moment de réviser ton image et ta façon d'attirer.

## Ce que tu pourrais vivre
- Une révision de ton image et de ton style
- Des réflexions sur ta façon de te mettre en avant en amour
- Le retour de questions sur l'estime de soi

## Conseils pour cette période
- Évite les changements de look drastiques
- Reconsidère ta façon de te présenter en relation
- L'impulsivité en amour mérite une pause""",

    ('aries', 2): """# ♀℞ Vénus rétrograde en Bélier — Maison 2

**En une phrase :** Tes valeurs et tes achats impulsifs liés au plaisir sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec l'impulsivité du Bélier. Les achats plaisir faits impulsivement peuvent être regrettés. C'est le moment de revoir ce que tu values vraiment et comment tu dépenses pour le plaisir.

## Ce que tu pourrais vivre
- Des achats impulsifs liés à la beauté ou au plaisir regrettés
- Une révision de tes valeurs profondes
- Des questions sur l'argent et les relations

## Conseils pour cette période
- Évite les achats de luxe impulsifs
- Reconsidère ce qui a vraiment de la valeur pour toi
- Les dépenses pour impressionner méritent réflexion""",

    ('aries', 3): """# ♀℞ Vénus rétrograde en Bélier — Maison 3

**En une phrase :** Tes communications amoureuses et tes échanges affectueux sont à revoir.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec la franchise du Bélier. Tes mots doux ou tes déclarations peuvent avoir été trop directs. Les relations avec l'entourage proche peuvent être révisées.

## Ce que tu pourrais vivre
- Des communications amoureuses trop directes à nuancer
- Une révision des relations avec frères, sœurs, voisins
- Le retour de conversations non terminées sur l'amour

## Conseils pour cette période
- Adoucis ta communication affective
- Les relations de proximité méritent de l'attention
- Les anciennes conversations amoureuses peuvent reprendre""",

    ('aries', 4): """# ♀℞ Vénus rétrograde en Bélier — Maison 4

**En une phrase :** L'amour et l'harmonie au foyer sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec l'énergie combative du Bélier. L'harmonie familiale peut avoir été perturbée par trop de conflits. C'est le moment de réviser les décisions de décoration et les relations familiales.

## Ce que tu pourrais vivre
- Une révision des choix de décoration
- Des questions sur l'harmonie et l'amour dans la famille
- Le retour de conflits familiaux à résoudre

## Conseils pour cette période
- Reporte les achats importants pour la maison
- Travaille sur l'harmonie familiale
- Les vieux conflits méritent d'être résolus avec amour""",

    ('aries', 5): """# ♀℞ Vénus rétrograde en Bélier — Maison 5

**En une phrase :** Tes amours, tes créations et tes plaisirs impulsifs sont profondément en révision.

## L'énergie du moment
Vénus rétrograde est très significative en Bélier dans la maison 5, domaine de l'amour et de la créativité. Les relations romantiques impulsives sont à reconsidérer. Les créations faites dans l'urgence méritent d'être revues.

## Ce que tu pourrais vivre
- Une révision profonde de tes relations amoureuses
- Le retour d'ex ou de sentiments anciens
- Des créations à retravailler

## Conseils pour cette période
- Ne commence pas de nouvelle relation importante
- Les ex qui reviennent ont des leçons à offrir
- Peaufine tes créations existantes""",

    ('aries', 6): """# ♀℞ Vénus rétrograde en Bélier — Maison 6

**En une phrase :** Les relations au travail et les habitudes de beauté sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec l'énergie du Bélier. Les relations avec les collègues peuvent avoir été trop directes. Les routines de beauté et de bien-être méritent d'être revues.

## Ce que tu pourrais vivre
- Des relations de travail à réviser
- Des habitudes de beauté ou de bien-être à reconsidérer
- Un flirt au travail qui se complique

## Conseils pour cette période
- Adoucis tes relations professionnelles
- Revois tes routines de soin
- Les mélanges amour-travail sont délicats maintenant""",

    ('aries', 7): """# ♀℞ Vénus rétrograde en Bélier — Maison 7

**En une phrase :** Tes relations de couple et tes partenariats sont en révision profonde.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec l'impulsivité du Bélier. C'est une période clé pour revoir tes relations importantes. Les décisions impulsives en couple méritent d'être reconsidérées.

## Ce que tu pourrais vivre
- Une révision profonde de ta relation de couple
- Le retour d'ex significatifs
- Des contrats ou accords à reconsidérer

## Conseils pour cette période
- Ne prends pas de décision définitive en relation
- Les ex qui reviennent ont des raisons
- Révise les accords plutôt que d'en créer de nouveaux""",

    ('aries', 8): """# ♀℞ Vénus rétrograde en Bélier — Maison 8

**En une phrase :** L'intimité et les finances partagées sont à reconsidérer avec prudence.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec l'intensité du Bélier. Les questions d'intimité et d'argent partagé sont au premier plan. Les décisions financières impulsives avec un partenaire méritent révision.

## Ce que tu pourrais vivre
- Une révision de l'intimité dans le couple
- Des questions financières partagées à reconsidérer
- Le retour de passions anciennes

## Conseils pour cette période
- L'intimité mérite de la profondeur, pas de la précipitation
- Revois les arrangements financiers partagés
- Les passions qui reviennent ont des leçons""",

    ('aries', 9): """# ♀℞ Vénus rétrograde en Bélier — Maison 9

**En une phrase :** Les amours lointains et les croyances sur l'amour sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec l'élan du Bélier. Les relations à distance ou avec des personnes d'autres cultures sont en révision. Tes croyances sur l'amour méritent d'être reconsidérées.

## Ce que tu pourrais vivre
- Une révision de relations à distance
- Des questions sur tes croyances amoureuses
- Le retour de personnes rencontrées en voyage

## Conseils pour cette période
- Les relations à distance demandent de la patience
- Reconsidère ce que tu crois sur l'amour
- Les rencontres de voyage peuvent refaire surface""",

    ('aries', 10): """# ♀℞ Vénus rétrograde en Bélier — Maison 10

**En une phrase :** Ta réputation et tes relations professionnelles sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec l'ambition du Bélier. Ta façon de te présenter professionnellement et tes relations au travail sont en révision. Les décisions de carrière impulsives méritent réflexion.

## Ce que tu pourrais vivre
- Une révision de ton image professionnelle
- Des relations professionnelles à reconsidérer
- Le retour d'anciennes opportunités ou de contacts

## Conseils pour cette période
- Soigne ton image professionnelle
- Les relations professionnelles méritent de la diplomatie
- Les opportunités passées peuvent revenir""",

    ('aries', 11): """# ♀℞ Vénus rétrograde en Bélier — Maison 11

**En une phrase :** Les amitiés et les relations dans les groupes sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec l'énergie du Bélier. Certaines amitiés peuvent avoir été trop conflictuelles. Les relations dans les groupes méritent d'être revues.

## Ce que tu pourrais vivre
- Une révision de certaines amitiés
- Des amis d'enfance ou du passé qui reviennent
- Des dynamiques de groupe à reconsidérer

## Conseils pour cette période
- Les vraies amitiés survivent aux révisions
- Les amis du passé ont peut-être quelque chose à offrir
- Adoucis tes relations dans les groupes""",

    ('aries', 12): """# ♀℞ Vénus rétrograde en Bélier — Maison 12

**En une phrase :** Tes amours secrets et ta relation à l'amour inconditionnel sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec l'intensité du Bélier. Des amours secrets ou des sentiments cachés peuvent remonter. Ta relation à l'amour de soi et à l'amour inconditionnel est en révision.

## Ce que tu pourrais vivre
- Des sentiments cachés qui refont surface
- Une révision de l'amour de soi
- Des amours du passé qui réapparaissent en rêve

## Conseils pour cette période
- Les sentiments cachés méritent d'être examinés
- L'amour de soi est fondamental maintenant
- Les rêves amoureux peuvent être significatifs""",

    # ============== TAURUS (Taureau) ==============
    ('taurus', 1): """# ♀℞ Vénus rétrograde en Taureau — Maison 1

**En une phrase :** Ta beauté, ton style et ta façon de te présenter sont en profonde révision.

## L'énergie du moment
Vénus rétrograde est très significative en Taureau, signe qu'elle gouverne, dans ta maison 1. Toute ta relation à ta beauté, à ton corps, à ton style est à reconsidérer. C'est une période puissante de révision de l'image de soi.

## Ce que tu pourrais vivre
- Une révision profonde de ton image et de ton style
- Des questions sur ta relation à ton corps
- Un retour à des styles ou des looks du passé

## Conseils pour cette période
- Évite les changements de look majeurs
- Explore ce qui te fait te sentir vraiment beau·belle
- Les anciens styles ont peut-être quelque chose à offrir""",

    ('taurus', 2): """# ♀℞ Vénus rétrograde en Taureau — Maison 2

**En une phrase :** Tes valeurs et ta relation à l'argent et au plaisir sont en révision profonde.

## L'énergie du moment
Vénus rétrograde est doublement puissante en Taureau dans la maison 2. Toute ta relation aux valeurs, à l'argent, aux possessions, au plaisir est à reconsidérer. C'est une période cruciale pour réviser ce qui compte vraiment.

## Ce que tu pourrais vivre
- Une révision profonde de tes valeurs
- Des questions sur ta relation à l'argent et aux possessions
- Un retour à des objets ou des valeurs du passé

## Conseils pour cette période
- Évite les achats importants
- Reconsidère ce qui a vraiment de la valeur
- Les objets du passé peuvent avoir une nouvelle signification""",

    ('taurus', 3): """# ♀℞ Vénus rétrograde en Taureau — Maison 3

**En une phrase :** Tes communications affectueuses et tes échanges sur les valeurs sont à revoir.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec la sensualité du Taureau. Ta façon d'exprimer l'affection peut sembler trop lente ou trop matérielle. Les échanges avec l'entourage proche sur les valeurs méritent attention.

## Ce que tu pourrais vivre
- Une révision de ta façon d'exprimer l'affection
- Des conversations sur l'argent avec la famille proche
- Un retour de personnes avec qui tu as des affinités

## Conseils pour cette période
- Exprime ton affection de façon authentique
- Les discussions sur les valeurs méritent de la patience
- Les anciens liens méritent peut-être d'être revisités""",

    ('taurus', 4): """# ♀℞ Vénus rétrograde en Taureau — Maison 4

**En une phrase :** La beauté et le confort de ton foyer sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec le sens esthétique du Taureau. La décoration, le confort, l'harmonie de ton espace sont en révision. Les relations familiales liées aux possessions ou aux valeurs méritent attention.

## Ce que tu pourrais vivre
- Une révision de la décoration et du confort chez toi
- Des questions familiales liées aux possessions ou à l'héritage
- Un désir de retourner à des ambiances du passé

## Conseils pour cette période
- Reporte les gros achats de décoration
- Les questions familiales sur les biens méritent de la délicatesse
- Le confort peut être retrouvé dans la simplicité""",

    ('taurus', 5): """# ♀℞ Vénus rétrograde en Taureau — Maison 5

**En une phrase :** Tes amours et tes créations sont en révision profonde et sensorielle.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec la sensualité du Taureau. Les relations amoureuses et la créativité passent par une révision profonde. Les plaisirs sensuels et les expressions créatives méritent d'être reconsidérés.

## Ce que tu pourrais vivre
- Une révision de ta vie amoureuse et sensuelle
- Des créations à retravailler ou des styles à revisiter
- Le retour d'anciens amours

## Conseils pour cette période
- L'amour mérite de la profondeur, pas de la nouveauté
- Tes créations passées ont peut-être de la valeur
- Les ex qui reviennent apportent des leçons sur les valeurs""",

    ('taurus', 6): """# ♀℞ Vénus rétrograde en Taureau — Maison 6

**En une phrase :** Les routines de beauté et le confort au travail sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec le sens pratique du Taureau. Tes habitudes de beauté, de bien-être, ton confort au travail sont en révision. Les relations professionnelles liées aux valeurs méritent attention.

## Ce que tu pourrais vivre
- Une révision de tes routines de beauté et de bien-être
- Des questions sur le confort et les conditions de travail
- Un retour à d'anciennes méthodes de soin

## Conseils pour cette période
- Les produits de beauté essayés avant peuvent être meilleurs que les nouveaux
- Le confort au travail mérite de l'attention
- Les anciennes routines ont peut-être de la valeur""",

    ('taurus', 7): """# ♀℞ Vénus rétrograde en Taureau — Maison 7

**En une phrase :** Tes relations de couple et la stabilité relationnelle sont en révision profonde.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec la loyauté du Taureau. La stabilité et la sécurité dans tes relations sont au premier plan. Les questions de valeurs partagées et de fidélité sont en révision.

## Ce que tu pourrais vivre
- Une révision de la stabilité dans ton couple
- Des questions sur les valeurs partagées avec un partenaire
- Le retour d'ex stables ou de relations passées sécurisantes

## Conseils pour cette période
- La stabilité relationnelle mérite d'être cultivée
- Les valeurs partagées sont le fondement d'une relation
- Les ex qui reviennent peuvent offrir de la sécurité""",

    ('taurus', 8): """# ♀℞ Vénus rétrograde en Taureau — Maison 8

**En une phrase :** L'intimité et les finances partagées sont en révision avec focus sur la sécurité.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec l'attachement du Taureau. Les questions de sécurité émotionnelle et financière dans l'intimité sont centrales. Les attachements matériels dans les relations sont à réviser.

## Ce que tu pourrais vivre
- Une révision de l'intimité et de la sécurité émotionnelle
- Des questions sur les finances partagées et les héritages
- Un retour de passions liées à la sécurité

## Conseils pour cette période
- La sécurité émotionnelle ne vient pas de l'attachement
- Les finances partagées méritent de la clarté
- Les patterns d'attachement peuvent être révisés""",

    ('taurus', 9): """# ♀℞ Vénus rétrograde en Taureau — Maison 9

**En une phrase :** Tes croyances sur l'amour et le plaisir sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec les valeurs du Taureau. Tes croyances sur ce qui a de la valeur, sur l'amour, sur le plaisir sont en révision. Les voyages liés au luxe ou à la beauté peuvent être compliqués.

## Ce que tu pourrais vivre
- Une révision de tes croyances sur l'amour et les valeurs
- Des voyages de luxe ou romantiques compliqués
- Un retour à des philosophies de vie passées

## Conseils pour cette période
- Tes valeurs peuvent évoluer avec sagesse
- Les voyages méritent de la simplicité
- Les anciennes croyances sur l'amour peuvent être révisées""",

    ('taurus', 10): """# ♀℞ Vénus rétrograde en Taureau — Maison 10

**En une phrase :** Ta réputation et tes réussites liées à la beauté ou aux valeurs sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec le sens de la valeur du Taureau. Ta réputation professionnelle, surtout si elle est liée à la beauté, l'art ou les finances, est en révision. La façon dont tu es valorisé·e professionnellement est à reconsidérer.

## Ce que tu pourrais vivre
- Une révision de ta valeur professionnelle
- Des questions sur ta réputation et ton image publique
- Le retour d'opportunités passées ou de contacts professionnels

## Conseils pour cette période
- Ta valeur professionnelle mérite d'être reconnue
- La réputation se construit sur la constance
- Les opportunités passées peuvent revenir avec plus de valeur""",

    ('taurus', 11): """# ♀℞ Vénus rétrograde en Taureau — Maison 11

**En une phrase :** Les amitiés et les valeurs partagées dans les groupes sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec la loyauté du Taureau. Les amitiés basées sur des valeurs communes sont en révision. Les relations dans les groupes liés à l'argent ou à la beauté méritent attention.

## Ce que tu pourrais vivre
- Une révision d'amitiés basées sur des valeurs
- Des questions sur la loyauté et la constance en amitié
- Le retour d'amis fidèles du passé

## Conseils pour cette période
- Les vraies amitiés sont basées sur des valeurs partagées
- La loyauté en amitié va dans les deux sens
- Les amis du passé peuvent avoir de la valeur maintenant""",

    ('taurus', 12): """# ♀℞ Vénus rétrograde en Taureau — Maison 12

**En une phrase :** Ta relation secrète au plaisir et à la beauté est en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec la sensualité du Taureau. Tes désirs cachés, tes plaisirs secrets, ta relation inconsciente à la beauté et à la valeur sont en révision. Des attachements cachés peuvent émerger.

## Ce que tu pourrais vivre
- Des désirs ou des attachements cachés qui remontent
- Une révision de ta relation inconsciente au plaisir
- Des rêves significatifs sur l'amour ou la beauté

## Conseils pour cette période
- Les désirs cachés méritent d'être examinés
- Ta relation au plaisir a des racines profondes
- Les rêves peuvent révéler ce que tu values vraiment""",

    # ============== GEMINI (Gémeaux) ==============
    ('gemini', 1): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 1

**En une phrase :** Ta façon de charmer et de te présenter est à réviser avec plus de profondeur.

## L'énergie du moment
Vénus rétrograde en Gémeaux dans ta maison 1 questionne ta façon de séduire et de te présenter. Tu as peut-être été trop changeant·e ou superficiel·le dans ton approche. C'est le moment de réviser ton image avec plus de constance.

## Ce que tu pourrais vivre
- Une révision de ta façon de charmer
- Des questions sur l'inconstance dans ton image
- Un retour à des styles ou des approches passés

## Conseils pour cette période
- La profondeur est plus attirante que la variété
- Ton image gagne à être plus constante
- Les anciens styles peuvent avoir de la valeur""",

    ('gemini', 2): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 2

**En une phrase :** Tes valeurs changeantes et tes achats variés sont à reconsidérer.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec la curiosité des Gémeaux. Tes valeurs peuvent avoir été trop changeantes. Les achats variés et nombreux peuvent nécessiter une révision.

## Ce que tu pourrais vivre
- Une révision de valeurs qui ont trop changé
- Des achats multiples et variés à reconsidérer
- Un besoin de clarifier ce qui compte vraiment

## Conseils pour cette période
- Les valeurs constantes ont plus de poids
- Évite les achats impulsifs et variés
- Clarifie ce qui a vraiment de la valeur pour toi""",

    ('gemini', 3): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 3

**En une phrase :** Les communications affectueuses et les flirts sont en révision.

## L'énergie du moment
Vénus rétrograde est significative en Gémeaux dans la maison 3. Toutes tes communications charmantes, tes flirts, tes échanges affectueux sont à réviser. Les relations avec l'entourage proche méritent de la profondeur.

## Ce que tu pourrais vivre
- Une révision des flirts et communications légères
- Des échanges avec des ex ou d'anciennes connaissances
- Un besoin de plus de profondeur dans les communications

## Conseils pour cette période
- Les flirts méritent de la sincérité
- Les anciennes conversations peuvent reprendre
- La communication profonde est plus satisfaisante""",

    ('gemini', 4): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 4

**En une phrase :** L'harmonie changeante au foyer et les communications familiales sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison du foyer avec la versatilité des Gémeaux. L'harmonie au foyer peut avoir été trop changeante. Les communications familiales sur les sentiments méritent de la constance.

## Ce que tu pourrais vivre
- Une révision de l'ambiance et de la décoration fluctuante
- Des communications familiales à approfondir
- Un retour à des ambiances ou des décorations passées

## Conseils pour cette période
- La stabilité au foyer apporte du confort
- Les conversations familiales méritent de la continuité
- Les anciennes décorations ont peut-être leur charme""",

    ('gemini', 5): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 5

**En une phrase :** Les amours multiples et la créativité dispersée sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec la variété des Gémeaux. Les relations amoureuses peuvent avoir été trop nombreuses ou superficielles. La créativité dispersée mérite d'être focalisée.

## Ce que tu pourrais vivre
- Une révision d'amours multiples ou changeants
- Des créations variées à unifier ou à approfondir
- Le retour de plusieurs ex ou de flirts passés

## Conseils pour cette période
- L'amour profond vaut mieux que les aventures multiples
- Concentre ta créativité sur un projet
- Les retours multiples demandent du discernement""",

    ('gemini', 6): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 6

**En une phrase :** Les routines de beauté changeantes et les relations de travail légères sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec la variabilité des Gémeaux. Tes routines de beauté ont peut-être changé trop souvent. Les relations de travail légères méritent plus de constance.

## Ce que tu pourrais vivre
- Une révision des routines de beauté multiples
- Des relations de travail superficielles à approfondir
- Un retour à d'anciennes méthodes qui fonctionnaient

## Conseils pour cette période
- La constance dans les routines de beauté porte ses fruits
- Les relations de travail gagnent en profondeur
- Les anciennes méthodes éprouvées ont leur valeur""",

    ('gemini', 7): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 7

**En une phrase :** Les relations de couple basées sur la communication légère sont à approfondir.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec l'intellect des Gémeaux. Les relations basées principalement sur l'échange intellectuel léger méritent plus de profondeur émotionnelle. Les communications de couple sont à réviser.

## Ce que tu pourrais vivre
- Une révision des communications dans le couple
- Un besoin de plus de profondeur émotionnelle en relation
- Le retour d'ex avec qui tu avais une bonne communication

## Conseils pour cette période
- Les relations profondes vont au-delà des mots
- Les communications de couple méritent de la sincérité
- Les ex communicatifs ont peut-être quelque chose à offrir""",

    ('gemini', 8): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 8

**En une phrase :** L'intimité intellectualisée et les discussions sur les finances partagées sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec la cérébralité des Gémeaux. L'intimité peut avoir été trop dans la tête et pas assez dans le cœur. Les discussions sur les finances partagées nécessitent de la clarté.

## Ce que tu pourrais vivre
- Une révision de l'intimité trop intellectualisée
- Des conversations sur les finances partagées à clarifier
- Un besoin de profondeur émotionnelle dans l'intimité

## Conseils pour cette période
- L'intimité vraie passe par le corps et les émotions
- Les finances partagées demandent de la clarté, pas juste des mots
- La profondeur émotionnelle enrichit les relations""",

    ('gemini', 9): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 9

**En une phrase :** Les croyances changeantes sur l'amour et les relations à distance sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec la curiosité des Gémeaux. Tes idées sur l'amour ont peut-être trop changé. Les relations à distance basées sur la communication peuvent être révisées.

## Ce que tu pourrais vivre
- Une révision de tes croyances sur l'amour
- Des relations à distance à reconsidérer
- Un retour de personnes rencontrées dans des contextes d'apprentissage

## Conseils pour cette période
- Les croyances sur l'amour gagnent en constance
- Les relations à distance demandent plus que des mots
- Les rencontres intellectuelles passées peuvent resurgir""",

    ('gemini', 10): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 10

**En une phrase :** Ta réputation de charme et tes relations professionnelles variées sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec la sociabilité des Gémeaux. Ta réputation de personne charmante et communicative est en révision. Les relations professionnelles multiples peuvent nécessiter de la sélection.

## Ce que tu pourrais vivre
- Une révision de ton image professionnelle charmante
- Des relations professionnelles à approfondir ou à trier
- Le retour de contacts professionnels du passé

## Conseils pour cette période
- La profondeur professionnelle a plus de valeur que le charme seul
- Sélectionne les relations professionnelles qui comptent
- Les contacts passés peuvent avoir de la valeur""",

    ('gemini', 11): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 11

**En une phrase :** Les amitiés nombreuses et les relations de groupe légères sont à réviser.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec la sociabilité des Gémeaux. Tu as peut-être eu trop d'amitiés superficielles. Les relations dans les groupes méritent plus de profondeur.

## Ce que tu pourrais vivre
- Une révision des amitiés nombreuses mais superficielles
- Un besoin de profondeur dans les relations de groupe
- Le retour d'amis du passé avec qui tu avais une connexion

## Conseils pour cette période
- La qualité des amitiés vaut mieux que la quantité
- Les relations de groupe gagnent en profondeur
- Les vrais amis du passé méritent ton attention""",

    ('gemini', 12): """# ♀℞ Vénus rétrograde en Gémeaux — Maison 12

**En une phrase :** Les amours secrets et les fantasmes changeants sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec l'agitation des Gémeaux. Des amours secrets ou des fantasmes variés peuvent émerger. La relation inconsciente au charme et à la séduction est en révision.

## Ce que tu pourrais vivre
- Des fantasmes ou des désirs cachés qui changent
- Une révision de ta relation inconsciente à la séduction
- Des rêves avec des messages multiples sur l'amour

## Conseils pour cette période
- Les désirs secrets méritent d'être examinés avec constance
- La séduction inconsciente a des patterns à comprendre
- Les rêves peuvent révéler des désirs profonds""",

    # ============== CANCER (Cancer) ==============
    ('cancer', 1): """# ♀℞ Vénus rétrograde en Cancer — Maison 1

**En une phrase :** Ta façon de te présenter avec sensibilité et ta relation à ton apparence sont en révision.

## L'énergie du moment
Vénus rétrograde en Cancer dans ta maison 1 questionne ta façon de te montrer avec sensibilité. Tu peux avoir été trop protecteur·rice de ton image. C'est le moment de réviser ta relation à ton apparence avec plus d'ouverture.

## Ce que tu pourrais vivre
- Une révision de ton image sensible et protégée
- Des questions sur ta façon de te présenter émotionnellement
- Un retour à des looks ou des styles du passé

## Conseils pour cette période
- La vulnérabilité peut être attirante
- Ton image gagne à montrer ta vraie sensibilité
- Les styles du passé peuvent avoir leur charme""",

    ('cancer', 2): """# ♀℞ Vénus rétrograde en Cancer — Maison 2

**En une phrase :** Ta relation émotionnelle à l'argent et aux possessions est en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des ressources avec l'émotivité du Cancer. Ta relation émotionnelle à l'argent et aux possessions est à reconsidérer. Les achats de confort ou nostalgiques méritent attention.

## Ce que tu pourrais vivre
- Une révision des achats émotionnels ou nostalgiques
- Des questions sur la sécurité financière et émotionnelle
- Un attachement à des objets du passé à reconsidérer

## Conseils pour cette période
- Sépare les émotions des décisions financières
- La vraie sécurité ne vient pas des possessions
- Les objets sentimentaux ont leur place, mais avec mesure""",

    ('cancer', 3): """# ♀℞ Vénus rétrograde en Cancer — Maison 3

**En une phrase :** Les communications affectueuses et les échanges avec la famille proche sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de la communication avec la tendresse du Cancer. Tes communications affectueuses, surtout avec la famille proche, sont à réviser. Les échanges émotionnels méritent de la clarté.

## Ce que tu pourrais vivre
- Une révision des communications émotionnelles
- Des échanges affectifs avec frères, sœurs, entourage proche
- Un retour de personnes avec qui tu as des liens émotionnels

## Conseils pour cette période
- Les communications émotionnelles gagnent en clarté
- Les liens familiaux proches méritent de l'attention
- Les anciennes connexions affectives peuvent être revisitées""",

    ('cancer', 4): """# ♀℞ Vénus rétrograde en Cancer — Maison 4

**En une phrase :** L'amour et l'harmonie au foyer sont en révision profonde.

## L'énergie du moment
Vénus rétrograde est très significative en Cancer dans la maison 4, son domaine émotionnel. Tout ce qui touche à l'amour dans la famille, à l'harmonie du foyer, aux mémoires affectives est en révision. C'est une période puissante pour les questions familiales.

## Ce que tu pourrais vivre
- Une révision profonde de l'amour et de l'harmonie familiale
- Des questions sur les mémoires affectives et le passé
- Un retour de personnes ou de situations familiales du passé

## Conseils pour cette période
- L'amour familial mérite d'être cultivé consciemment
- Les mémoires du passé peuvent guérir
- L'harmonie au foyer demande un travail intérieur""",

    ('cancer', 5): """# ♀℞ Vénus rétrograde en Cancer — Maison 5

**En une phrase :** Les amours nourriciers et la créativité émotionnelle sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des plaisirs avec l'émotivité du Cancer. Les relations amoureuses où tu as joué un rôle nourricier sont à réviser. La créativité émotionnelle et les expressions artistiques sensibles méritent d'être reconsidérées.

## Ce que tu pourrais vivre
- Une révision des amours où tu as trop donné
- Des créations émotionnelles à retravailler
- Le retour d'ex avec qui tu avais une connexion émotionnelle

## Conseils pour cette période
- L'amour équilibré ne t'épuise pas
- Ta créativité émotionnelle est précieuse
- Les ex émotionnellement significatifs ont des leçons""",

    ('cancer', 6): """# ♀℞ Vénus rétrograde en Cancer — Maison 6

**En une phrase :** Les routines de soin et les relations de travail émotionnelles sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison du quotidien avec l'attention du Cancer. Tes routines de soin de toi et des autres sont à réviser. Les relations de travail où l'émotionnel est présent méritent d'être reconsidérées.

## Ce que tu pourrais vivre
- Une révision des routines de soin et de bien-être
- Des relations de travail émotionnelles à clarifier
- Un retour à d'anciennes habitudes réconfortantes

## Conseils pour cette période
- Prendre soin de toi est aussi important que prendre soin des autres
- Les émotions au travail méritent des limites
- Les anciennes habitudes réconfortantes ont leur valeur""",

    ('cancer', 7): """# ♀℞ Vénus rétrograde en Cancer — Maison 7

**En une phrase :** Les relations de couple basées sur le soin et la protection sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des partenariats avec le besoin de sécurité du Cancer. Les relations où tu as joué le rôle de protecteur·rice ou de parent sont à réviser. La sécurité émotionnelle dans le couple est au premier plan.

## Ce que tu pourrais vivre
- Une révision des rôles dans ton couple
- Des questions sur la sécurité émotionnelle relationnelle
- Le retour d'ex avec qui tu avais une connexion familière

## Conseils pour cette période
- Les relations adultes ne sont pas parentales
- La sécurité émotionnelle vient de l'intérieur aussi
- Les ex qui reviennent ont des leçons sur l'attachement""",

    ('cancer', 8): """# ♀℞ Vénus rétrograde en Cancer — Maison 8

**En une phrase :** L'intimité émotionnelle et les liens profonds sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des transformations avec la profondeur émotionnelle du Cancer. L'intimité et les liens émotionnels profonds sont à reconsidérer. Les attachements qui créent de la dépendance méritent attention.

## Ce que tu pourrais vivre
- Une révision de l'intimité émotionnelle
- Des questions sur les attachements et la dépendance
- Le retour de liens profonds du passé

## Conseils pour cette période
- L'intimité saine n'est pas de la fusion
- Les attachements peuvent être revisités avec conscience
- Les liens profonds du passé ont des enseignements""",

    ('cancer', 9): """# ♀℞ Vénus rétrograde en Cancer — Maison 9

**En une phrase :** Les croyances sur l'amour et le foyer idéal sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'expansion avec les valeurs familiales du Cancer. Tes croyances sur ce qu'est un foyer idéal, un amour idéal, sont à reconsidérer. Les voyages vers des lieux significatifs émotionnellement sont favorisés.

## Ce que tu pourrais vivre
- Une révision de tes croyances sur l'amour et la famille
- Des voyages vers des lieux de mémoire ou familiaux
- Un questionnement sur ce qui fait un vrai foyer

## Conseils pour cette période
- Tes idéaux sur l'amour peuvent évoluer
- Les voyages de mémoire peuvent être guérissants
- Le vrai foyer est aussi un état intérieur""",

    ('cancer', 10): """# ♀℞ Vénus rétrograde en Cancer — Maison 10

**En une phrase :** Ta réputation de personne attentionnée et tes relations professionnelles de soin sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de carrière avec la bienveillance du Cancer. Ta réputation de personne attentionnée et tes relations de soin professionnelles sont à réviser. La façon dont tu prends soin au travail mérite attention.

## Ce que tu pourrais vivre
- Une révision de ton image professionnelle bienveillante
- Des relations de soin au travail à reconsidérer
- Le retour de contacts professionnels significatifs

## Conseils pour cette période
- Prendre soin au travail a des limites saines
- Ta réputation de bienveillance mérite d'être authentique
- Les contacts professionnels du passé peuvent revenir""",

    ('cancer', 11): """# ♀℞ Vénus rétrograde en Cancer — Maison 11

**En une phrase :** Les amitiés nourricières et les groupes comme des familles sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison des amitiés avec l'énergie familiale du Cancer. Les amitiés où tu joues un rôle nourricier sont à réviser. Les groupes vécus comme des familles méritent d'être reconsidérés.

## Ce que tu pourrais vivre
- Une révision des amitiés où tu donnes trop
- Des questions sur les groupes vécus comme des familles
- Le retour d'amis qui sont comme de la famille

## Conseils pour cette période
- L'amitié équilibrée nourrit dans les deux sens
- Les groupes ne remplacent pas les familles saines
- Les amis-famille du passé ont leur place""",

    ('cancer', 12): """# ♀℞ Vénus rétrograde en Cancer — Maison 12

**En une phrase :** Les amours cachés et les besoins émotionnels inconscients sont en révision.

## L'énergie du moment
Vénus rétrograde traverse ta maison de l'inconscient avec l'émotivité du Cancer. Les amours secrets, les besoins émotionnels cachés, les attachements inconscients sont en révision. C'est une période puissante pour l'introspection amoureuse.

## Ce que tu pourrais vivre
- Des besoins émotionnels cachés qui remontent
- Une révision des attachements inconscients
- Des rêves significatifs sur l'amour et la famille

## Conseils pour cette période
- Les besoins cachés méritent d'être reconnus
- Les attachements inconscients peuvent être guéris
- Les rêves portent des messages sur tes vrais besoins""",
}

async def insert_interpretations():
    """Insert all venus_retrograde interpretations for Aries, Taurus, Gemini, Cancer"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in VENUS_RETROGRADE_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'venus_retrograde',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP: venus_retrograde {sign} house {house} already exists")
                skipped += 1
                continue

            interpretation = PregeneratedNatalInterpretation(
                subject='venus_retrograde',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interpretation)
            print(f"INSERT: venus_retrograde {sign} house {house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nDone: {inserted} inserted, {skipped} skipped")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
