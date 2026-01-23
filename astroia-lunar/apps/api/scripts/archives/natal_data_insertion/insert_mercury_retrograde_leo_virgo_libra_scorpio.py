#!/usr/bin/env python3
"""
Insert mercury_retrograde interpretations V2 for Leo, Virgo, Libra, Scorpio (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

MERCURY_RETROGRADE_INTERPRETATIONS = {
    # ============== LEO (Lion) ==============
    ('leo', 1): """# ☿℞ Mercure rétrograde en Lion — Maison 1

**En une phrase :** Ta façon de te présenter et de t'exprimer est à réviser avec humilité.

## L'énergie du moment
Mercure rétrograde en Lion dans ta maison 1 peut créer des malentendus liés à ton ego ou à ta façon de te mettre en avant. C'est le moment de revoir comment tu communiques sur toi-même et si ton message correspond vraiment à qui tu es.

## Ce que tu pourrais vivre
- Des malentendus liés à une communication trop théâtrale
- Un besoin de réviser ton image publique
- Des retours sur la façon dont les autres te perçoivent

## Conseils pour cette période
- Modère ton expression pour être mieux compris·e
- Réfléchis à l'image que tu veux vraiment projeter
- L'authenticité est plus puissante que le spectacle""",

    ('leo', 2): """# ☿℞ Mercure rétrograde en Lion — Maison 2

**En une phrase :** Tes dépenses liées au plaisir et au luxe méritent d'être reconsidérées.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec l'énergie dépensière du Lion. Les achats de luxe ou pour briller peuvent se révéler décevants. C'est le moment de revoir ta relation à l'argent et au statut.

## Ce que tu pourrais vivre
- Des achats ostentatoires que tu pourrais regretter
- Des communications sur l'argent teintées d'orgueil
- Un besoin de revoir ta relation au luxe

## Conseils pour cette période
- Évite les achats pour impressionner
- Reconsidère ce qui te donne vraiment de la valeur
- La vraie richesse n'est pas toujours visible""",

    ('leo', 3): """# ☿℞ Mercure rétrograde en Lion — Maison 3

**En une phrase :** Tes communications peuvent paraître trop centrées sur toi et créer des malentendus.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec la théâtralité du Lion. Tes paroles peuvent paraître égocentriques même si ce n'est pas ton intention. Les échanges avec l'entourage proche peuvent être compliqués par des questions d'égo.

## Ce que tu pourrais vivre
- Des communications qui semblent trop centrées sur toi
- Des malentendus liés à des questions de fierté
- Un besoin de laisser plus de place aux autres

## Conseils pour cette période
- Écoute autant que tu parles
- La générosité dans la communication crée de meilleurs échanges
- Laisse les autres briller aussi dans les conversations""",

    ('leo', 4): """# ☿℞ Mercure rétrograde en Lion — Maison 4

**En une phrase :** Les communications familiales et ta place dans la famille sont à reconsidérer.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec l'énergie dominante du Lion. Des enjeux de pouvoir ou de reconnaissance dans la famille peuvent émerger. Les discussions sur qui décide à la maison peuvent être tendues.

## Ce que tu pourrais vivre
- Des tensions familiales liées à des questions de pouvoir
- Un besoin de reconnaissance dans la famille
- Des projets domestiques qui nécessitent d'être revus

## Conseils pour cette période
- Cède un peu sur les questions de contrôle à la maison
- La famille n'est pas un théâtre où tu dois toujours briller
- Revois les projets de maison avec réalisme""",

    ('leo', 5): """# ☿℞ Mercure rétrograde en Lion — Maison 5

**En une phrase :** Les communications romantiques et créatives sont très expressives mais peuvent être mal comprises.

## L'énergie du moment
Mercure rétrograde est très significatif en Lion dans la maison 5, domaine de la créativité et de l'amour. Les déclarations amoureuses peuvent être dramatiques mais mal interprétées. Les projets créatifs peuvent nécessiter des révisions importantes.

## Ce que tu pourrais vivre
- Des communications amoureuses trop théâtrales
- Des projets créatifs qui demandent à être retravaillés
- Le retour d'anciennes flammes avec du drame

## Conseils pour cette période
- Exprime tes sentiments avec sincérité plutôt qu'avec spectacle
- Révise et améliore tes créations existantes
- Les ex qui reviennent apportent souvent des leçons d'égo""",

    ('leo', 6): """# ☿℞ Mercure rétrograde en Lion — Maison 6

**En une phrase :** Les communications au travail peuvent souffrir d'un besoin excessif de reconnaissance.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec le besoin de briller du Lion. Tu peux vouloir être reconnu·e pour ton travail au point de créer des tensions. Les tâches routinières peuvent sembler en dessous de toi.

## Ce que tu pourrais vivre
- Des frustrations si ton travail n'est pas reconnu
- Des communications avec les collègues compliquées par l'égo
- Un rejet des tâches qui ne te mettent pas en valeur

## Conseils pour cette période
- Le travail bien fait est sa propre récompense
- La reconnaissance viendra, patience
- Même les petites tâches méritent d'être faites avec fierté""",

    ('leo', 7): """# ☿℞ Mercure rétrograde en Lion — Maison 7

**En une phrase :** Les communications relationnelles peuvent être compliquées par des questions d'égo.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec l'orgueil du Lion. Les discussions de couple peuvent devenir des batailles d'égo. Les contrats et accords peuvent être affectés par le besoin de paraître en position de force.

## Ce que tu pourrais vivre
- Des disputes de couple liées à des questions de fierté
- Des négociations compliquées par le besoin de gagner
- Le retour d'ex avec des enjeux de pouvoir non résolus

## Conseils pour cette période
- Lâche le besoin d'avoir raison dans le couple
- Les meilleures relations ne sont pas des compétitions
- Les ex qui reviennent ont des leçons sur ton égo""",

    ('leo', 8): """# ☿℞ Mercure rétrograde en Lion — Maison 8

**En une phrase :** Les communications sur les finances partagées et l'intimité sont compliquées par l'orgueil.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec l'égo du Lion. Les discussions sur l'argent partagé peuvent être affectées par la fierté. Les conversations intimes peuvent souffrir du besoin de paraître fort·e.

## Ce que tu pourrais vivre
- Des discussions financières compliquées par l'égo
- Une difficulté à montrer ta vulnérabilité
- Des secrets liés à l'orgueil qui refont surface

## Conseils pour cette période
- La vulnérabilité est une force, pas une faiblesse
- Les discussions financières demandent de l'humilité
- Les secrets d'égo méritent d'être examinés""",

    ('leo', 9): """# ☿℞ Mercure rétrograde en Lion — Maison 9

**En une phrase :** Les communications sur tes croyances peuvent être trop dogmatiques.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec l'assurance du Lion. Tu peux vouloir avoir raison sur les grandes questions au point de ne plus écouter. Les voyages peuvent être affectés par un désir de faire les choses en grand.

## Ce que tu pourrais vivre
- Des débats philosophiques où tu veux dominer
- Des plans de voyage trop ambitieux qui se compliquent
- Un besoin de réviser tes certitudes

## Conseils pour cette période
- La vraie sagesse inclut l'écoute des autres perspectives
- Simplifie tes plans de voyage
- Révise tes croyances avec humilité""",

    ('leo', 10): """# ☿℞ Mercure rétrograde en Lion — Maison 10

**En une phrase :** Les communications professionnelles peuvent souffrir d'un besoin excessif de reconnaissance.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec le besoin de briller du Lion. Les paroles au travail peuvent être trop centrées sur toi. Ta réputation peut être affectée par une communication qui paraît arrogante.

## Ce que tu pourrais vivre
- Des communications professionnelles qui semblent égocentriques
- Des projets retardés par le besoin de tout contrôler
- Des malentendus qui affectent ta réputation

## Conseils pour cette période
- Laisse ton travail parler pour toi
- La collaboration vaut mieux que la domination
- Révise ton image professionnelle avec objectivité""",

    ('leo', 11): """# ☿℞ Mercure rétrograde en Lion — Maison 11

**En une phrase :** Les communications dans les groupes peuvent être compliquées par ton besoin de leadership.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec l'énergie dominante du Lion. Tu peux vouloir être le centre d'attention dans les groupes. Les projets collectifs peuvent souffrir de ton besoin de diriger.

## Ce que tu pourrais vivre
- Des tensions dans les groupes si tu veux trop mener
- Des malentendus avec des amis sur des questions de leadership
- Un besoin de réviser ta place dans les collectifs

## Conseils pour cette période
- Les meilleurs leaders savent aussi suivre
- L'amitié n'est pas une scène où tu dois performer
- Révise ta façon de contribuer aux groupes""",

    ('leo', 12): """# ☿℞ Mercure rétrograde en Lion — Maison 12

**En une phrase :** Ton égo secret et tes besoins de reconnaissance cachés demandent de l'attention.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec l'énergie du Lion. Des blessures d'égo enfouies peuvent remonter. Des secrets liés à ton besoin de briller peuvent émerger. C'est un temps pour examiner ton orgueil caché.

## Ce que tu pourrais vivre
- Des blessures d'égo anciennes qui refont surface
- Des secrets liés au besoin de reconnaissance
- Un travail profond sur l'orgueil et l'humilité

## Conseils pour cette période
- Examine d'où vient ton besoin de briller
- Les blessures d'égo peuvent être guéries
- L'humilité intérieure apporte la paix""",

    # ============== VIRGO (Vierge) ==============
    ('virgo', 1): """# ☿℞ Mercure rétrograde en Vierge — Maison 1

**En une phrase :** Ta communication personnelle et ton perfectionnisme sont à réviser.

## L'énergie du moment
Mercure rétrograde est très significatif en Vierge, signe qu'il gouverne. Dans ta maison 1, c'est ta façon de te présenter et de communiquer sur toi qui est recalibrée. Ton autocritique peut être excessive. C'est le moment de revoir ton image avec bienveillance.

## Ce que tu pourrais vivre
- Une autocritique accrue sur ton image
- Des communications personnelles trop analytiques
- Un besoin de réviser comment tu te présentes

## Conseils pour cette période
- Sois plus doux·ce avec toi-même
- Ton perfectionnisme peut être un obstacle
- L'authenticité vaut mieux que la perfection""",

    ('virgo', 2): """# ☿℞ Mercure rétrograde en Vierge — Maison 2

**En une phrase :** Tes analyses financières et ton rapport aux détails matériels sont à réviser.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec l'analyse minutieuse de la Vierge. Tu peux trop analyser tes finances au point de ne plus agir. Les petits détails des transactions peuvent créer des complications.

## Ce que tu pourrais vivre
- Une analyse excessive de tes finances
- Des erreurs dans les détails des transactions
- Un besoin de revoir ton système de gestion de l'argent

## Conseils pour cette période
- Ne te perds pas dans les détails financiers
- Vérifie tous les calculs et les virgules
- C'est un bon moment pour organiser tes papiers financiers""",

    ('virgo', 3): """# ☿℞ Mercure rétrograde en Vierge — Maison 3

**En une phrase :** Toutes tes communications sont soumises à un examen minutieux.

## L'énergie du moment
Mercure rétrograde est doublement fort en Vierge dans la maison 3. Chaque mot, chaque détail de ta communication est important. Les erreurs d'écriture, les coquilles, les malentendus sont probables mais aussi les opportunités de perfectionner ta façon de communiquer.

## Ce que tu pourrais vivre
- Des erreurs dans les messages malgré les vérifications
- Un besoin de tout relire plusieurs fois
- Des malentendus sur des détails

## Conseils pour cette période
- Vérifie trois fois avant d'envoyer
- Accepte que la perfection n'existe pas
- C'est le moment idéal pour améliorer tes systèmes de communication""",

    ('virgo', 4): """# ☿℞ Mercure rétrograde en Vierge — Maison 4

**En une phrase :** L'organisation de ton foyer et les communications familiales demandent une révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec le sens de l'ordre de la Vierge. C'est le moment idéal pour réorganiser, trier, nettoyer. Les communications familiales peuvent être critiques mais aussi clarifiantes.

## Ce que tu pourrais vivre
- Un besoin de réorganiser ton espace
- Des critiques dans les communications familiales
- Des projets domestiques qui demandent d'être repensés

## Conseils pour cette période
- Profite de ce temps pour un grand tri
- Tempère tes critiques envers la famille
- Améliore les systèmes de ton foyer""",

    ('virgo', 5): """# ☿℞ Mercure rétrograde en Vierge — Maison 5

**En une phrase :** La créativité et les communications amoureuses sont soumises à l'analyse.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec l'esprit critique de la Vierge. Tu peux sur-analyser tes relations amoureuses. Tes créations peuvent te sembler imparfaites. C'est le moment de réviser et perfectionner.

## Ce que tu pourrais vivre
- Une tendance à analyser excessivement en amour
- Des créations qui semblent toujours à améliorer
- Un perfectionnisme qui peut bloquer le plaisir

## Conseils pour cette période
- L'amour n'a pas besoin d'être parfait
- Tes créations méritent d'être terminées, pas perfectionnées à l'infini
- Permets-toi le plaisir imparfait""",

    ('virgo', 6): """# ☿℞ Mercure rétrograde en Vierge — Maison 6

**En une phrase :** Les routines de travail et de santé sont en révision approfondie.

## L'énergie du moment
Mercure rétrograde est très puissant en Vierge dans la maison 6, domaine du quotidien et de la santé. C'est le moment idéal pour revoir tes systèmes, tes routines, ton alimentation. Les détails au travail demandent une attention maximale.

## Ce que tu pourrais vivre
- Un besoin de revoir toutes tes routines
- Des erreurs au travail dues à trop de perfectionnisme
- Une analyse approfondie de ta santé

## Conseils pour cette période
- Améliore tes systèmes de travail existants
- Ne laisse pas l'analyse paralyser l'action
- C'est un excellent moment pour optimiser ta santé""",

    ('virgo', 7): """# ☿℞ Mercure rétrograde en Vierge — Maison 7

**En une phrase :** Les communications relationnelles sont soumises à une analyse critique.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec l'esprit analytique de la Vierge. Tu peux être trop critique envers ton partenaire. Les contrats demandent une relecture très minutieuse.

## Ce que tu pourrais vivre
- Une tendance à critiquer ton partenaire
- Des contrats qui nécessitent des corrections
- Un besoin de clarifier les rôles dans les relations

## Conseils pour cette période
- La critique doit être constructive et bienveillante
- Relis chaque clause des contrats
- Améliore les systèmes de communication dans le couple""",

    ('virgo', 8): """# ☿℞ Mercure rétrograde en Vierge — Maison 8

**En une phrase :** Les détails financiers complexes et les analyses profondes demandent de la précision.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec la minutie de la Vierge. Les documents financiers complexes méritent une attention extrême. L'analyse psychologique peut être très approfondie mais aussi obsessionnelle.

## Ce que tu pourrais vivre
- Des erreurs dans des documents financiers complexes
- Une analyse psychologique qui tourne en boucle
- Un besoin de clarifier des détails dans les affaires partagées

## Conseils pour cette période
- Vérifie chaque chiffre dans les documents importants
- L'analyse a ses limites, passe aussi à l'action
- Clarifie les détails des arrangements financiers""",

    ('virgo', 9): """# ☿℞ Mercure rétrograde en Vierge — Maison 9

**En une phrase :** Les grands concepts et les voyages sont soumis à une analyse détaillée.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec le souci du détail de la Vierge. Tu peux perdre de vue la grande image à force de te concentrer sur les détails. Les voyages nécessitent une préparation méticuleuse.

## Ce que tu pourrais vivre
- Une perte de vue d'ensemble à force de détails
- Des voyages qui nécessitent beaucoup de préparation
- Un besoin de vérifier les détails de tes croyances

## Conseils pour cette période
- N'oublie pas la forêt pour les arbres
- Prépare tes voyages avec soin mais sans obsession
- Les grands principes méritent d'être vérifiés dans les détails""",

    ('virgo', 10): """# ☿℞ Mercure rétrograde en Vierge — Maison 10

**En une phrase :** Les détails professionnels et la qualité de ton travail sont sous les projecteurs.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec le perfectionnisme de la Vierge. Chaque détail de ton travail peut être scruté. Les erreurs professionnelles sont plus visibles. C'est le moment de réviser et améliorer.

## Ce que tu pourrais vivre
- Un examen détaillé de ton travail
- Des erreurs qui sont plus remarquées que d'habitude
- Un besoin de perfectionner tes compétences professionnelles

## Conseils pour cette période
- Vérifie trois fois ton travail avant de le soumettre
- Utilise ce temps pour améliorer tes méthodes
- La qualité constante bâtit la réputation""",

    ('virgo', 11): """# ☿℞ Mercure rétrograde en Vierge — Maison 11

**En une phrase :** Les détails des projets de groupe et les communications avec les amis sont à réviser.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec l'attention aux détails de la Vierge. Les projets collectifs peuvent être ralentis par le besoin de tout vérifier. Les communications avec les amis peuvent être trop analytiques.

## Ce que tu pourrais vivre
- Des projets de groupe qui s'enlisent dans les détails
- Des critiques qui compliquent les amitiés
- Un besoin de réviser ta contribution aux collectifs

## Conseils pour cette période
- Les détails importent mais ne perdez pas l'élan
- Sois moins critique avec tes amis
- Améliore ta façon de collaborer""",

    ('virgo', 12): """# ☿℞ Mercure rétrograde en Vierge — Maison 12

**En une phrase :** Ton critique intérieur et tes pensées obsessionnelles demandent de l'attention.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec l'esprit critique de la Vierge. Ton juge intérieur peut être particulièrement actif. Des pensées obsessionnelles sur les détails peuvent perturber ton repos.

## Ce que tu pourrais vivre
- Un critique intérieur très actif
- Des pensées qui tournent en boucle sur des détails
- Un besoin de calmer le mental analytique

## Conseils pour cette période
- Observe ton critique intérieur avec compassion
- La méditation peut calmer l'analyse excessive
- Tu mérites de te pardonner l'imperfection""",

    # ============== LIBRA (Balance) ==============
    ('libra', 1): """# ☿℞ Mercure rétrograde en Balance — Maison 1

**En une phrase :** Ta façon de te présenter et de chercher l'harmonie est à reconsidérer.

## L'énergie du moment
Mercure rétrograde en Balance dans ta maison 1 te pousse à réviser comment tu te présentes aux autres. Tu peux avoir trop cherché à plaire au détriment de ton authenticité. C'est le moment de trouver l'équilibre entre diplomatie et vérité.

## Ce que tu pourrais vivre
- Des questions sur ton image et ta façon de plaire
- Des malentendus liés à des messages trop nuancés
- Un besoin de réviser l'équilibre entre toi et les autres

## Conseils pour cette période
- L'authenticité attire plus que la complaisance
- Trouve ta propre voix au lieu de chercher le consensus
- Révise ton image avec honnêteté""",

    ('libra', 2): """# ☿℞ Mercure rétrograde en Balance — Maison 2

**En une phrase :** Tes décisions financières basées sur l'esthétique ou les relations sont à revoir.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec le sens esthétique de la Balance. Les achats liés à la beauté ou à l'harmonie peuvent se révéler décevants. Les finances partagées avec un partenaire demandent de la clarification.

## Ce que tu pourrais vivre
- Des achats esthétiques que tu pourrais regretter
- Des communications sur l'argent dans le couple
- Un besoin de réviser tes valeurs liées à l'apparence

## Conseils pour cette période
- La vraie beauté n'est pas toujours coûteuse
- Clarifie les questions d'argent avec ton partenaire
- Révise ce qui a vraiment de la valeur pour toi""",

    ('libra', 3): """# ☿℞ Mercure rétrograde en Balance — Maison 3

**En une phrase :** Tes communications peuvent être trop diplomatiques et manquer de clarté.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec la diplomatie de la Balance. À force de vouloir ménager tout le monde, tes messages peuvent être confus. Les malentendus peuvent venir de l'indécision ou du manque de fermeté.

## Ce que tu pourrais vivre
- Des messages trop nuancés qui créent de la confusion
- Une difficulté à dire les choses directement
- Des malentendus avec l'entourage proche

## Conseils pour cette période
- Parfois, la clarté est plus gentille que la diplomatie excessive
- Dis ce que tu penses vraiment, avec respect
- Les vrais malentendus se clarifient avec franchise""",

    ('libra', 4): """# ☿℞ Mercure rétrograde en Balance — Maison 4

**En une phrase :** L'harmonie familiale et la décoration du foyer sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec le sens esthétique de la Balance. Les projets de décoration peuvent ne pas donner les résultats attendus. Les communications familiales peuvent souffrir de trop de compromis.

## Ce que tu pourrais vivre
- Des projets de décoration à revoir
- Des situations familiales où tout le monde évite le conflit
- Un besoin de trouver le vrai équilibre à la maison

## Conseils pour cette période
- Reporte les achats importants pour la maison
- L'harmonie superficielle cache parfois des tensions
- Trouve le vrai équilibre, pas juste l'apparence de la paix""",

    ('libra', 5): """# ☿℞ Mercure rétrograde en Balance — Maison 5

**En une phrase :** Les communications romantiques peuvent être trop diplomatiques pour être claires.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec le charme de la Balance. Les messages amoureux peuvent être si diplomatiques qu'ils sont mal compris. La créativité peut souffrir d'un excès de recherche d'équilibre.

## Ce que tu pourrais vivre
- Des communications romantiques trop subtiles
- Une créativité qui cherche trop le consensus
- Le retour d'ex avec des questions relationnelles non résolues

## Conseils pour cette période
- En amour, sois clair·e sur tes sentiments
- Ta créativité n'a pas besoin de plaire à tout le monde
- Les ex qui reviennent apportent des leçons sur les relations""",

    ('libra', 6): """# ☿℞ Mercure rétrograde en Balance — Maison 6

**En une phrase :** L'harmonie au travail et l'équilibre quotidien sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec le besoin d'harmonie de la Balance. Tu peux éviter les conflits au travail au point de ne pas résoudre les vrais problèmes. L'équilibre travail-vie personnelle demande d'être revu.

## Ce que tu pourrais vivre
- Des tensions au travail dues à l'évitement des conflits
- Un déséquilibre entre travail et vie personnelle
- Des communications professionnelles trop diplomatiques

## Conseils pour cette période
- Parfois, affronter un problème crée plus d'harmonie que l'éviter
- Revois ton équilibre de vie avec honnêteté
- La vraie collaboration inclut la discussion des désaccords""",

    ('libra', 7): """# ☿℞ Mercure rétrograde en Balance — Maison 7

**En une phrase :** Les communications relationnelles et les partenariats sont en profonde révision.

## L'énergie du moment
Mercure rétrograde est très significatif en Balance dans la maison 7, domaine des relations. Tous les aspects de tes communications de couple ou de partenariat sont à revoir. C'est le moment de clarifier les attentes et les malentendus.

## Ce que tu pourrais vivre
- Des discussions importantes sur la relation
- Des contrats et accords qui nécessitent une révision
- Le retour d'ex avec des conversations non terminées

## Conseils pour cette période
- C'est le moment idéal pour clarifier les choses dans le couple
- Relis tous les contrats et accords
- Les ex qui reviennent ont des raisons relationnelles""",

    ('libra', 8): """# ☿℞ Mercure rétrograde en Balance — Maison 8

**En une phrase :** Les communications sur les finances partagées et l'intimité demandent de l'équilibre.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec la diplomatie de la Balance. Les discussions sur l'argent partagé peuvent être évitées au lieu d'être clarifiées. L'intimité peut souffrir de communications trop superficielles.

## Ce que tu pourrais vivre
- Des questions financières partagées qui restent en suspens
- Une intimité affectée par le manque de communication profonde
- Un besoin d'équilibrer le pouvoir dans les relations intimes

## Conseils pour cette période
- Les discussions difficiles créent plus d'harmonie que l'évitement
- L'intimité vraie demande de la profondeur, pas de la diplomatie
- Clarifie les questions de finances partagées""",

    ('libra', 9): """# ☿℞ Mercure rétrograde en Balance — Maison 9

**En une phrase :** Tes croyances et tes voyages sont influencés par le désir d'harmonie.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec l'équilibre de la Balance. Tu peux avoir du mal à te positionner sur des questions philosophiques. Les voyages planifiés avec un partenaire peuvent nécessiter des ajustements.

## Ce que tu pourrais vivre
- Une difficulté à prendre position sur des croyances
- Des voyages avec des partenaires qui se compliquent
- Un besoin de trouver tes propres convictions

## Conseils pour cette période
- Tu n'as pas à être d'accord avec tout le monde
- Planifie les voyages avec flexibilité
- Trouve tes propres croyances, au-delà du consensus""",

    ('libra', 10): """# ☿℞ Mercure rétrograde en Balance — Maison 10

**En une phrase :** Les communications professionnelles peuvent être trop diplomatiques pour être efficaces.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec le charme de la Balance. Tu peux éviter les confrontations professionnelles nécessaires. Ta réputation peut être affectée par un manque de clarté.

## Ce que tu pourrais vivre
- Des communications professionnelles qui manquent de fermeté
- Des projets retardés par la recherche du consensus
- Un besoin de clarifier ta position professionnelle

## Conseils pour cette période
- La clarté est plus respectée que la diplomatie excessive
- Prends position quand c'est nécessaire
- Révise ton image professionnelle avec honnêteté""",

    ('libra', 11): """# ☿℞ Mercure rétrograde en Balance — Maison 11

**En une phrase :** Les communications dans les groupes peuvent souffrir de trop de compromis.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec le besoin d'harmonie de la Balance. Les projets de groupe peuvent être ralentis par la recherche du consensus. Les amitiés peuvent souffrir de communications trop superficielles.

## Ce que tu pourrais vivre
- Des projets collectifs bloqués par l'indécision
- Des amitiés affectées par l'évitement des vrais sujets
- Un besoin de clarifier ta place dans les groupes

## Conseils pour cette période
- Les meilleurs groupes incluent des opinions diverses
- Les vraies amitiés survivent aux désaccords
- Prends position au lieu de toujours chercher le compromis""",

    ('libra', 12): """# ☿℞ Mercure rétrograde en Balance — Maison 12

**En une phrase :** Ton besoin caché d'harmonie et de plaire demande de l'attention.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec le besoin d'équilibre de la Balance. Des patterns inconscients de recherche d'approbation peuvent émerger. Des secrets liés aux relations peuvent refaire surface.

## Ce que tu pourrais vivre
- Des prises de conscience sur ton besoin de plaire
- Des secrets relationnels qui reviennent
- Un travail profond sur l'équilibre intérieur

## Conseils pour cette période
- Examine d'où vient ton besoin d'harmonie
- L'équilibre vrai vient de l'intérieur
- Les secrets relationnels méritent d'être examinés""",

    # ============== SCORPIO (Scorpion) ==============
    ('scorpio', 1): """# ☿℞ Mercure rétrograde en Scorpion — Maison 1

**En une phrase :** Ta façon de communiquer et ton intensité personnelle sont en révision.

## L'énergie du moment
Mercure rétrograde en Scorpion dans ta maison 1 met en lumière ton intensité communicationnelle. Tes paroles peuvent être trop incisives ou révéler des choses que tu préférerais garder cachées. C'est le moment de recalibrer ton expression.

## Ce que tu pourrais vivre
- Des paroles trop intenses ou révélatrices
- Un besoin de réviser ton image et ta présence
- Des secrets sur toi qui pourraient émerger

## Conseils pour cette période
- L'intensité est une force si elle est maîtrisée
- Révise comment tu veux être perçu·e
- Ce qui est caché peut être libéré avec sagesse""",

    ('scorpio', 2): """# ☿℞ Mercure rétrograde en Scorpion — Maison 2

**En une phrase :** Les communications sur l'argent et tes ressources cachées sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec l'intensité du Scorpion. Les questions d'argent peuvent révéler des enjeux de pouvoir. Des ressources cachées ou oubliées peuvent être retrouvées.

## Ce que tu pourrais vivre
- Des discussions intenses sur l'argent
- Des découvertes de ressources oubliées
- Un besoin de transformer ton rapport à l'argent

## Conseils pour cette période
- Les discussions financières demandent de la profondeur
- C'est le moment de retrouver l'argent oublié ou qu'on te doit
- Examine tes enjeux de pouvoir liés à l'argent""",

    ('scorpio', 3): """# ☿℞ Mercure rétrograde en Scorpion — Maison 3

**En une phrase :** Tes communications quotidiennes peuvent être trop intenses ou révélatrices.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec l'intensité du Scorpion. Les conversations peuvent aller plus profond que prévu. Des secrets de l'entourage proche peuvent émerger.

## Ce que tu pourrais vivre
- Des conversations qui vont plus loin que prévu
- Des secrets avec frères, sœurs ou voisins
- Un besoin de communications plus profondes

## Conseils pour cette période
- L'intensité peut effrayer : dose-la
- Les secrets qui émergent demandent de la discrétion
- C'est le moment pour des conversations vraies""",

    ('scorpio', 4): """# ☿℞ Mercure rétrograde en Scorpion — Maison 4

**En une phrase :** Les secrets de famille et les communications profondes sur le passé sont en révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec l'énergie révélatrice du Scorpion. Des secrets de famille peuvent émerger. Les conversations sur le passé peuvent être intenses et transformatrices.

## Ce que tu pourrais vivre
- Des secrets de famille qui reviennent à la surface
- Des conversations profondes sur le passé
- Un besoin de transformer ta relation aux origines

## Conseils pour cette période
- Les secrets familiaux révélés peuvent guérir
- Les conversations profondes avec la famille peuvent libérer
- Protège ce qui doit rester privé""",

    ('scorpio', 5): """# ☿℞ Mercure rétrograde en Scorpion — Maison 5

**En une phrase :** Les communications amoureuses et créatives sont intenses et révélatrices.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec la passion du Scorpion. Les communications amoureuses peuvent être très intenses. Les créations peuvent révéler des profondeurs que tu n'avais pas prévues.

## Ce que tu pourrais vivre
- Des déclarations amoureuses d'une intensité inattendue
- Des créations qui révèlent des parts cachées de toi
- Le retour d'ex avec des révélations

## Conseils pour cette période
- L'intensité en amour doit être dosée
- Tes créations profondes sont précieuses
- Les ex qui reviennent ont des vérités à partager""",

    ('scorpio', 6): """# ☿℞ Mercure rétrograde en Scorpion — Maison 6

**En une phrase :** Les communications au travail peuvent révéler des enjeux de pouvoir cachés.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec l'intensité du Scorpion. Les dynamiques de pouvoir au travail peuvent être mises en lumière. Des informations cachées sur le travail peuvent émerger.

## Ce que tu pourrais vivre
- Des révélations sur les dynamiques de pouvoir au travail
- Des communications intenses avec les collègues
- Des informations cachées qui émergent

## Conseils pour cette période
- Utilise les informations révélées avec sagesse
- Les enjeux de pouvoir au travail demandent de la finesse
- Ta santé peut révéler des tensions non exprimées""",

    ('scorpio', 7): """# ☿℞ Mercure rétrograde en Scorpion — Maison 7

**En une phrase :** Les communications relationnelles peuvent révéler des vérités cachées.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec l'intensité du Scorpion. Les discussions de couple peuvent aller très profond. Des secrets relationnels peuvent émerger. C'est le moment de vérité dans les relations.

## Ce que tu pourrais vivre
- Des conversations de couple très intenses
- Des secrets qui émergent dans les relations
- Le retour d'ex avec des révélations significatives

## Conseils pour cette période
- La vérité dans les relations peut être libératrice
- Les secrets révélés demandent d'être traités avec soin
- L'intensité relationnelle peut être transformatrice""",

    ('scorpio', 8): """# ☿℞ Mercure rétrograde en Scorpion — Maison 8

**En une phrase :** Les communications sur les transformations profondes et les tabous sont en révision.

## L'énergie du moment
Mercure rétrograde est très puissant en Scorpion dans la maison 8. Toutes les communications sur les sujets profonds - sexualité, mort, argent partagé - sont à revoir. Des secrets enfouis peuvent émerger. C'est un temps de transformation intérieure.

## Ce que tu pourrais vivre
- Des révélations sur des sujets profonds et tabous
- Des communications intenses sur les finances partagées
- Un travail profond sur tes transformations

## Conseils pour cette période
- Les vérités profondes qui émergent peuvent libérer
- Les sujets tabous méritent d'être abordés avec sagesse
- Ce temps de transformation est puissant""",

    ('scorpio', 9): """# ☿℞ Mercure rétrograde en Scorpion — Maison 9

**En une phrase :** Tes croyances profondes et ta quête de vérité sont en révision intense.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec la profondeur du Scorpion. Ta recherche de vérité peut te mener à des découvertes dérangeantes. Les voyages peuvent révéler des aspects cachés de la réalité.

## Ce que tu pourrais vivre
- Des remises en question profondes de tes croyances
- Des voyages qui révèlent des vérités cachées
- Un besoin de comprendre les mystères

## Conseils pour cette période
- La quête de vérité peut être déstabilisante
- Intègre les révélations progressivement
- Les voyages initiatiques sont favorisés""",

    ('scorpio', 10): """# ☿℞ Mercure rétrograde en Scorpion — Maison 10

**En une phrase :** Les communications professionnelles peuvent révéler des enjeux de pouvoir.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec l'intensité du Scorpion. Les dynamiques de pouvoir professionnelles sont mises en lumière. Des informations cachées sur ta carrière peuvent émerger.

## Ce que tu pourrais vivre
- Des révélations sur les enjeux de pouvoir au travail
- Des communications professionnelles intenses
- Ta réputation affectée par des informations révélées

## Conseils pour cette période
- Utilise les informations professionnelles avec stratégie
- Les enjeux de pouvoir demandent de la finesse
- Protège ta réputation avec discernement""",

    ('scorpio', 11): """# ☿℞ Mercure rétrograde en Scorpion — Maison 11

**En une phrase :** Les communications dans les groupes peuvent révéler des dynamiques cachées.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec l'intensité du Scorpion. Les dynamiques de pouvoir dans les groupes sont révélées. Les amitiés peuvent être transformées par des vérités qui émergent.

## Ce que tu pourrais vivre
- Des révélations sur les dynamiques de groupe
- Des communications intenses avec les amis
- Des transformations dans tes cercles sociaux

## Conseils pour cette période
- Les vérités révélées peuvent transformer les amitiés
- Les dynamiques de groupe cachées méritent d'être vues
- Les vrais amis survivent à l'intensité""",

    ('scorpio', 12): """# ☿℞ Mercure rétrograde en Scorpion — Maison 12

**En une phrase :** Les profondeurs de ton inconscient sont en révision intense.

## L'énergie du moment
Mercure rétrograde est très puissant en Scorpion dans la maison 12. Les secrets les plus enfouis peuvent émerger. Les rêves peuvent être très révélateurs. C'est un temps de transformation psychologique profonde.

## Ce que tu pourrais vivre
- Des secrets très anciens qui remontent
- Des rêves intenses et révélateurs
- Un travail profond sur l'inconscient

## Conseils pour cette période
- Accueille ce qui émerge avec courage
- Les rêves sont des messages précieux maintenant
- La thérapie ou le travail intérieur est très efficace""",
}

async def insert_interpretations():
    """Insert all mercury_retrograde interpretations for Leo, Virgo, Libra, Scorpio"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in MERCURY_RETROGRADE_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'mercury_retrograde',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"SKIP: mercury_retrograde {sign} house {house} already exists")
                skipped += 1
                continue

            interpretation = PregeneratedNatalInterpretation(
                subject='mercury_retrograde',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interpretation)
            print(f"INSERT: mercury_retrograde {sign} house {house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\nDone: {inserted} inserted, {skipped} skipped")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
