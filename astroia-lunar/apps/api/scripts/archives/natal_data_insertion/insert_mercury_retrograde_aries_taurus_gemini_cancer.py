#!/usr/bin/env python3
"""
Insert mercury_retrograde interpretations V2 for Aries, Taurus, Gemini, Cancer (all 12 houses each)
Total: 4 signs × 12 houses = 48 interpretations
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

MERCURY_RETROGRADE_INTERPRETATIONS = {
    # ============== ARIES (Bélier) ==============
    ('aries', 1): """# ☿℞ Mercure rétrograde en Bélier — Maison 1

**En une phrase :** Ta façon de t'affirmer et de communiquer sur toi-même est à reconsidérer.

## L'énergie du moment
Mercure rétrograde en Bélier dans ta maison 1 t'invite à ralentir ton impulsivité habituelle. Tes paroles et actions spontanées peuvent être mal interprétées. C'est le moment de réfléchir à l'image que tu projettes et à ta façon de te présenter au monde.

## Ce que tu pourrais vivre
- Des malentendus liés à ta façon de t'exprimer trop directement
- Un besoin de repenser ton image ou ta communication personnelle
- Des projets personnels qui demandent à être revus

## Conseils pour cette période
- Compte jusqu'à dix avant de parler ou d'agir impulsivement
- Revois tes projets personnels plutôt que d'en lancer de nouveaux
- Profite de ce temps pour clarifier ton message personnel""",

    ('aries', 2): """# ☿℞ Mercure rétrograde en Bélier — Maison 2

**En une phrase :** Tes décisions financières impulsives méritent d'être reconsidérées.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec l'énergie pressée du Bélier. Les achats impulsifs peuvent se révéler être des erreurs. C'est le moment de revoir tes finances, de récupérer de l'argent qu'on te doit, de renégocier des contrats.

## Ce que tu pourrais vivre
- Des retards dans les paiements ou les transactions
- Des achats impulsifs que tu pourrais regretter
- La nécessité de revoir ton budget ou tes investissements

## Conseils pour cette période
- Évite les achats importants non planifiés
- Vérifie tes relevés bancaires et tes contrats
- C'est un bon moment pour récupérer ce qu'on te doit""",

    ('aries', 3): """# ☿℞ Mercure rétrograde en Bélier — Maison 3

**En une phrase :** Les communications quotidiennes et les échanges avec l'entourage demandent plus d'attention.

## L'énergie du moment
Mercure rétrograde dans sa zone de communication avec l'impatience du Bélier peut créer des étincelles. Les malentendus avec frères, sœurs, voisins sont possibles. Les courts trajets peuvent être perturbés. Tes messages peuvent être mal interprétés.

## Ce que tu pourrais vivre
- Des malentendus dans les échanges quotidiens
- Des problèmes avec les transports ou les déplacements locaux
- Des communications manquées ou mal formulées

## Conseils pour cette période
- Relis tes messages avant de les envoyer
- Prévois du temps supplémentaire pour tes déplacements
- Clarifie les malentendus au lieu de les laisser s'envenimer""",

    ('aries', 4): """# ☿℞ Mercure rétrograde en Bélier — Maison 4

**En une phrase :** Les communications familiales et les projets domestiques nécessitent patience et révision.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec l'énergie pressée du Bélier. Les tensions familiales liées à des malentendus sont possibles. Les projets de rénovation peuvent connaître des retards. Des souvenirs ou des sujets familiaux non résolus peuvent resurgir.

## Ce que tu pourrais vivre
- Des malentendus ou des tensions avec la famille
- Des retards dans les projets liés à la maison
- Le retour de sujets familiaux qu'on croyait réglés

## Conseils pour cette période
- Évite de lancer de gros travaux dans la maison
- Prends le temps de clarifier les choses avec la famille
- C'est un bon moment pour réorganiser ton espace""",

    ('aries', 5): """# ☿℞ Mercure rétrograde en Bélier — Maison 5

**En une phrase :** Les communications en amour et les projets créatifs demandent à être revus.

## L'énergie du moment
Mercure rétrograde dans ta maison des plaisirs avec l'impétuosité du Bélier peut créer des drames romantiques basés sur des malentendus. Les projets créatifs lancés impulsivement peuvent nécessiter des révisions. Les communications avec les enfants peuvent être compliquées.

## Ce que tu pourrais vivre
- Des malentendus dans les relations amoureuses
- Des projets créatifs qui nécessitent d'être retravaillés
- Des messages romantiques mal interprétés

## Conseils pour cette période
- Clarifie tes intentions en amour plutôt que de supposer
- Revois et améliore tes créations plutôt que d'en commencer de nouvelles
- Évite les déclarations impulsives que tu pourrais regretter""",

    ('aries', 6): """# ☿℞ Mercure rétrograde en Bélier — Maison 6

**En une phrase :** Les communications au travail et les routines quotidiennes demandent plus d'attention.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec l'impatience du Bélier. Les erreurs au travail dues à la précipitation sont possibles. Les équipements de bureau ou de santé peuvent dysfonctionner. Les communications avec les collègues peuvent être tendues.

## Ce que tu pourrais vivre
- Des erreurs ou des malentendus au travail
- Des équipements qui tombent en panne
- Des rendez-vous médicaux à reprogrammer

## Conseils pour cette période
- Vérifie ton travail deux fois avant de le soumettre
- Fais sauvegarder tes appareils électroniques
- C'est un bon moment pour revoir tes routines de santé""",

    ('aries', 7): """# ☿℞ Mercure rétrograde en Bélier — Maison 7

**En une phrase :** Les communications dans les relations importantes méritent une attention particulière.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec l'énergie conflictuelle du Bélier. Les discussions avec ton partenaire ou tes associés peuvent facilement dégénérer. Les contrats et les accords demandent à être relus attentivement. D'anciens partenaires peuvent réapparaître.

## Ce que tu pourrais vivre
- Des malentendus ou des disputes dans le couple
- Des contrats ou des accords qui nécessitent une révision
- Le retour d'ex-partenaires ou d'anciens associés

## Conseils pour cette période
- Écoute avant de réagir dans les discussions de couple
- Relis tous les contrats avant de signer
- Les ex qui reviennent ne sont pas toujours une bonne nouvelle""",

    ('aries', 8): """# ☿℞ Mercure rétrograde en Bélier — Maison 8

**En une phrase :** Les communications sur l'argent partagé et les sujets intimes nécessitent prudence.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec l'impulsivité du Bélier. Les discussions sur l'argent partagé peuvent être tendues. Les questions d'héritage, de taxes, de dettes peuvent resurgir. Les conversations intimes peuvent être mal comprises.

## Ce que tu pourrais vivre
- Des complications avec les impôts, les assurances, les héritages
- Des malentendus sur l'argent partagé avec un partenaire
- Des sujets tabous qui reviennent dans les conversations

## Conseils pour cette période
- Vérifie attentivement tout document financier complexe
- Évite les discussions financières quand tu es énervé·e
- C'est un bon moment pour régulariser des situations administratives en suspens""",

    ('aries', 9): """# ☿℞ Mercure rétrograde en Bélier — Maison 9

**En une phrase :** Les voyages lointains et les communications sur tes croyances demandent prudence.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec l'impatience du Bélier. Les voyages à l'étranger peuvent être perturbés. Les discussions philosophiques peuvent devenir des disputes. Les publications ou les formations peuvent connaître des retards.

## Ce que tu pourrais vivre
- Des perturbations dans les voyages lointains
- Des débats qui dégénèrent sur des questions de croyances
- Des retards dans les projets académiques ou éditoriaux

## Conseils pour cette période
- Vérifie et re-vérifie tous les détails de voyage
- Évite les débats d'opinions qui peuvent s'envenimer
- Revois et améliore tes projets d'enseignement ou de publication""",

    ('aries', 10): """# ☿℞ Mercure rétrograde en Bélier — Maison 10

**En une phrase :** Les communications professionnelles et ta réputation demandent une attention particulière.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec l'énergie impulsive du Bélier. Les paroles trop directes au travail peuvent te nuire. Les projets professionnels peuvent connaître des retards. Ta réputation peut être affectée par des malentendus.

## Ce que tu pourrais vivre
- Des malentendus avec des supérieurs ou des clients
- Des retards dans des projets professionnels importants
- Des communications professionnelles qui créent des problèmes

## Conseils pour cette période
- Sois particulièrement diplomate dans tes communications professionnelles
- Évite de signer de nouveaux contrats de travail importants
- C'est un bon moment pour reprendre contact avec d'anciens collègues""",

    ('aries', 11): """# ☿℞ Mercure rétrograde en Bélier — Maison 11

**En une phrase :** Les communications dans tes cercles sociaux et tes projets collectifs demandent de la patience.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec l'impétuosité du Bélier. Les discussions avec des amis peuvent déraper facilement. Les projets de groupe peuvent connaître des retards. Les réseaux sociaux peuvent être source de malentendus.

## Ce que tu pourrais vivre
- Des malentendus ou des disputes avec des amis
- Des projets collectifs qui prennent du retard
- Des messages mal interprétés sur les réseaux sociaux

## Conseils pour cette période
- Ne prends pas les réactions de tes amis personnellement
- Revois les projets de groupe existants plutôt que d'en lancer de nouveaux
- Sois prudent·e avec ce que tu publies en ligne""",

    ('aries', 12): """# ☿℞ Mercure rétrograde en Bélier — Maison 12

**En une phrase :** Ton dialogue intérieur et tes pensées secrètes demandent à être examinés.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec l'énergie agitée du Bélier. Tes pensées peuvent tourner en boucle, surtout sur des frustrations non exprimées. Des secrets peuvent refaire surface. C'est un temps d'introspection sur tes schémas de pensée.

## Ce que tu pourrais vivre
- Des pensées agitées ou des insomnies mentales
- Des secrets qui reviennent à la surface
- Un besoin de comprendre tes motivations cachées

## Conseils pour cette période
- La méditation ou l'écriture peuvent calmer le mental
- Fais attention à ce que tu dis en confidence
- C'est un bon moment pour une thérapie ou un travail introspectif""",

    # ============== TAURUS (Taureau) ==============
    ('taurus', 1): """# ☿℞ Mercure rétrograde en Taureau — Maison 1

**En une phrase :** Ta façon de communiquer sur toi-même et ton image demandent une révision en profondeur.

## L'énergie du moment
Mercure rétrograde en Taureau dans ta maison 1 te ralentit pour revoir ton image et ta façon de te présenter. Les changements de look planifiés peuvent ne pas donner les résultats attendus. C'est le moment de réfléchir à ce que tu veux vraiment communiquer sur toi.

## Ce que tu pourrais vivre
- Des hésitations sur des changements personnels
- Des incompréhensions sur qui tu es vraiment
- Un besoin de revenir à une image plus authentique

## Conseils pour cette période
- Évite les changements drastiques de look
- Prends le temps de réfléchir à ton message personnel
- Reviens à ce qui te représente vraiment""",

    ('taurus', 2): """# ☿℞ Mercure rétrograde en Taureau — Maison 2

**En une phrase :** Tes finances et tes valeurs demandent une révision minutieuse.

## L'énergie du moment
Mercure rétrograde est très significatif en Taureau dans la maison 2, domaine de l'argent et des valeurs. Les transactions financières peuvent être ralenties ou compliquées. C'est le moment idéal pour revoir ton budget, tes dépenses, et ce à quoi tu accordes de la valeur.

## Ce que tu pourrais vivre
- Des retards ou des complications dans les transactions financières
- Des achats qui ne correspondent pas à tes attentes
- Une réflexion profonde sur tes vraies valeurs

## Conseils pour cette période
- Évite les achats importants et les investissements
- Revois ton budget et tes abonnements
- Récupère l'argent qu'on te doit""",

    ('taurus', 3): """# ☿℞ Mercure rétrograde en Taureau — Maison 3

**En une phrase :** Les communications quotidiennes sont ralenties mais plus réfléchies.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec la lenteur du Taureau. Les échanges prennent plus de temps mais peuvent être plus profonds. Les malentendus sont souvent liés au fait de ne pas avoir pris le temps de bien formuler les choses.

## Ce que tu pourrais vivre
- Des communications plus lentes que d'habitude
- Des malentendus qui viennent du manque de clarté
- Un besoin de repenser ta façon de t'exprimer

## Conseils pour cette période
- Prends le temps de bien formuler tes messages
- Préfère les conversations en face à face
- C'est un bon moment pour reprendre contact avec des proches""",

    ('taurus', 4): """# ☿℞ Mercure rétrograde en Taureau — Maison 4

**En une phrase :** Les projets domestiques et les communications familiales demandent patience.

## L'énergie du moment
Mercure rétrograde en Taureau traverse ta maison du foyer, ralentissant tout ce qui touche à la maison et à la famille. Les projets de décoration ou de rénovation peuvent prendre plus de temps. Les discussions familiales sur les finances ou les possessions peuvent ressurgir.

## Ce que tu pourrais vivre
- Des retards dans les projets liés à la maison
- Des discussions familiales sur l'argent ou les héritages
- Des souvenirs ou des objets du passé qui refont surface

## Conseils pour cette période
- Reporte les gros achats pour la maison
- Résous les vieux différends familiaux plutôt que de les éviter
- C'est un bon moment pour trier et organiser""",

    ('taurus', 5): """# ☿℞ Mercure rétrograde en Taureau — Maison 5

**En une phrase :** Les plaisirs et les communications romantiques demandent plus de profondeur.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec la sensualité du Taureau. Les communications romantiques peuvent être mal interprétées si elles manquent de sincérité. Les projets créatifs méritent d'être revus et améliorés plutôt que lancés.

## Ce que tu pourrais vivre
- Des malentendus dans les communications romantiques
- Des projets créatifs qui nécessitent des révisions
- Un retour sur d'anciennes passions ou ex-relations

## Conseils pour cette période
- Exprime tes sentiments de façon authentique et directe
- Peaufine tes créations plutôt que d'en commencer de nouvelles
- Les ex qui reviennent peuvent avoir quelque chose à t'apprendre""",

    ('taurus', 6): """# ☿℞ Mercure rétrograde en Taureau — Maison 6

**En une phrase :** Les routines quotidiennes et les communications au travail nécessitent des ajustements.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec la lenteur du Taureau. Le travail peut sembler plus lent ou les tâches peuvent nécessiter d'être refaites. C'est le moment de revoir tes habitudes de santé et d'alimentation.

## Ce que tu pourrais vivre
- Des tâches au travail qui prennent plus de temps
- Des équipements qui fonctionnent au ralenti
- Un besoin de revoir tes routines de santé

## Conseils pour cette période
- Accepte le rythme plus lent et travaille en profondeur
- Fais vérifier tes équipements avant qu'ils ne tombent en panne
- Revois ton alimentation et tes habitudes de bien-être""",

    ('taurus', 7): """# ☿℞ Mercure rétrograde en Taureau — Maison 7

**En une phrase :** Les communications relationnelles et les contrats demandent une attention particulière.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec l'énergie possessive du Taureau. Les discussions avec ton partenaire sur l'argent ou les possessions peuvent être compliquées. Les contrats méritent d'être relus attentivement.

## Ce que tu pourrais vivre
- Des discussions difficiles sur l'argent dans le couple
- Des contrats qui nécessitent des révisions
- Le retour d'anciens partenaires avec des questions non résolues

## Conseils pour cette période
- Sois patient·e dans les discussions avec ton partenaire
- Relis tous les contrats et accords avant de signer
- Les vieux différends relationnels méritent d'être résolus""",

    ('taurus', 8): """# ☿℞ Mercure rétrograde en Taureau — Maison 8

**En une phrase :** Les questions financières complexes et les communications intimes demandent de la prudence.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec l'énergie matérialiste du Taureau. Les questions d'argent partagé, d'héritage, de taxes peuvent être compliquées. Les communications sur l'intimité peuvent être maladroites.

## Ce que tu pourrais vivre
- Des retards ou des complications avec les impôts ou les héritages
- Des discussions sur l'argent partagé qui tournent en rond
- Un besoin de clarifier des sujets intimes

## Conseils pour cette période
- Vérifie trois fois tout document financier complexe
- Sois patient·e avec les procédures administratives
- Les conversations intimes méritent du temps et de la douceur""",

    ('taurus', 9): """# ☿℞ Mercure rétrograde en Taureau — Maison 9

**En une phrase :** Les voyages et les apprentissages demandent plus de préparation.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec la prudence du Taureau. Les voyages peuvent être retardés ou nécessiter des ajustements. Les formations ou les publications peuvent prendre plus de temps que prévu.

## Ce que tu pourrais vivre
- Des perturbations dans les plans de voyage
- Des retards dans les projets académiques ou éditoriaux
- Une révision de tes croyances ou de ta philosophie de vie

## Conseils pour cette période
- Planifie tes voyages avec des marges de sécurité
- Revois et améliore tes projets d'étude ou de publication
- Prends le temps de réfléchir à ce en quoi tu crois vraiment""",

    ('taurus', 10): """# ☿℞ Mercure rétrograde en Taureau — Maison 10

**En une phrase :** Les communications professionnelles et ta réputation demandent de la prudence.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec la stabilité du Taureau. Les projets professionnels peuvent être ralentis. Les communications avec les supérieurs demandent d'être bien réfléchies. Ta réputation doit être protégée.

## Ce que tu pourrais vivre
- Des projets professionnels qui prennent du retard
- Des communications avec la hiérarchie qui demandent de la diplomatie
- Une réflexion sur ta direction professionnelle

## Conseils pour cette période
- Évite les changements de carrière majeurs maintenant
- Sois particulièrement soigneux·se dans tes communications officielles
- Profite de ce temps pour planifier tes prochains objectifs""",

    ('taurus', 11): """# ☿℞ Mercure rétrograde en Taureau — Maison 11

**En une phrase :** Les communications dans tes réseaux et tes projets collectifs demandent de la patience.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec l'énergie du Taureau. Les projets de groupe peuvent être ralentis. Les communications avec des amis sur des sujets d'argent peuvent être délicates.

## Ce que tu pourrais vivre
- Des projets de groupe qui prennent plus de temps
- Des malentendus avec des amis, surtout sur l'argent
- Un besoin de revoir tes objectifs à long terme

## Conseils pour cette période
- Sois patient·e avec les projets collectifs
- Évite les prêts ou les affaires d'argent entre amis
- Revois tes objectifs et tes aspirations""",

    ('taurus', 12): """# ☿℞ Mercure rétrograde en Taureau — Maison 12

**En une phrase :** Tes pensées secrètes et ton monde intérieur demandent de l'attention.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec la profondeur du Taureau. Des pensées sur la sécurité, l'argent, les possessions peuvent occuper ton esprit de façon obsessionnelle. Des secrets liés aux biens matériels peuvent refaire surface.

## Ce que tu pourrais vivre
- Des préoccupations mentales sur la sécurité matérielle
- Des secrets ou des situations cachées qui réapparaissent
- Un besoin de repos et de réflexion intérieure

## Conseils pour cette période
- Prends du temps pour le repos mental
- Examine tes peurs profondes sur la sécurité
- C'est un bon moment pour des pratiques méditatives""",

    # ============== GEMINI (Gémeaux) ==============
    ('gemini', 1): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 1

**En une phrase :** Ta façon de communiquer et de te présenter demande une révision fondamentale.

## L'énergie du moment
Mercure rétrograde est très significatif en Gémeaux dans ta maison 1, car Mercure gouverne les Gémeaux. Ta communication personnelle, ta façon de penser et de te présenter sont profondément remises en question. C'est un temps puissant de recalibrage mental.

## Ce que tu pourrais vivre
- Une révision profonde de ta façon de communiquer
- Des malentendus sur qui tu es vraiment
- Un besoin de repenser ton image et ton message

## Conseils pour cette période
- Utilise ce temps pour vraiment réfléchir à comment tu veux être perçu·e
- Les malentendus sont des opportunités de clarification
- Reconnecte avec ta vraie façon de penser""",

    ('gemini', 2): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 2

**En une phrase :** Tes idées sur l'argent et la valeur demandent à être repensées.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec l'énergie mentale des Gémeaux. Tu peux avoir plusieurs idées contradictoires sur tes finances. Les communications liées à l'argent peuvent être confuses ou changeantes.

## Ce que tu pourrais vivre
- De la confusion sur tes priorités financières
- Des erreurs de communication dans les transactions
- Un besoin de clarifier ce que tu values vraiment

## Conseils pour cette période
- Évite les décisions financières impulsives
- Clarifie par écrit tous les accords financiers
- Profite de ce temps pour réviser ton rapport à l'argent""",

    ('gemini', 3): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 3

**En une phrase :** Toutes les formes de communication sont amplifiées et demandent une attention maximale.

## L'énergie du moment
Mercure rétrograde est doublement puissant en Gémeaux dans la maison 3. Toutes les communications sont sujettes à révision. Les malentendus sont probables mais aussi les opportunités de vraiment clarifier les choses. Les transports peuvent être perturbés.

## Ce que tu pourrais vivre
- Des malentendus fréquents dans les communications
- Des problèmes avec les transports ou les appareils de communication
- Un besoin de revisiter des conversations importantes

## Conseils pour cette période
- Vérifie trois fois tous tes messages importants
- Aie des plans B pour tes déplacements
- C'est le moment idéal pour recontacter des personnes""",

    ('gemini', 4): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 4

**En une phrase :** Les communications familiales et les discussions sur le foyer demandent de la clarté.

## L'énergie du moment
Mercure rétrograde traverse ta maison du foyer avec l'agitation des Gémeaux. Les discussions familiales peuvent être confuses ou tourner en rond. Les décisions sur le logement méritent d'être reportées ou revues.

## Ce que tu pourrais vivre
- Des malentendus dans la famille
- Des décisions sur le logement qui nécessitent plus de réflexion
- Des souvenirs et des discussions du passé qui refont surface

## Conseils pour cette période
- Sois clair·e dans tes communications avec la famille
- Évite les décisions majeures sur le logement
- Les vieux sujets qui reviennent méritent d'être résolus""",

    ('gemini', 5): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 5

**En une phrase :** Les communications romantiques et créatives sont intenses mais nécessitent de la prudence.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec la vivacité des Gémeaux. Les flirts et les communications romantiques peuvent être particulièrement confus. La créativité mentale est forte mais les projets peuvent nécessiter des révisions.

## Ce que tu pourrais vivre
- Des messages romantiques mal interprétés
- Des projets créatifs qui nécessitent d'être retravaillés
- Le retour d'anciennes flammes ou de vieilles passions

## Conseils pour cette période
- Clarifie tes intentions amoureuses explicitement
- Révise tes créations plutôt que d'en lancer de nouvelles
- Les ex qui reviennent ont peut-être quelque chose à enseigner""",

    ('gemini', 6): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 6

**En une phrase :** Les communications au travail et les routines quotidiennes demandent une organisation rigoureuse.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec l'énergie dispersée des Gémeaux. Les tâches multiples peuvent mener à des erreurs. Les communications avec les collègues peuvent être confuses. Les problèmes techniques sont probables.

## Ce que tu pourrais vivre
- Des erreurs dues au multitâche
- Des malentendus avec les collègues
- Des problèmes techniques avec les équipements

## Conseils pour cette période
- Concentre-toi sur une tâche à la fois
- Vérifie et re-vérifie ton travail
- Fais sauvegarder et mettre à jour tes appareils""",

    ('gemini', 7): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 7

**En une phrase :** Les communications dans les partenariats sont intenses et demandent beaucoup de clarté.

## L'énergie du moment
Mercure rétrograde traverse ta maison des relations avec l'énergie communicative des Gémeaux. Les discussions avec les partenaires peuvent être animées mais confuses. Les contrats méritent une relecture très attentive.

## Ce que tu pourrais vivre
- Des discussions intenses avec ton partenaire
- Des contrats qui nécessitent des révisions
- Le retour d'ex-partenaires avec des messages à transmettre

## Conseils pour cette période
- Écoute vraiment ce que ton partenaire essaie de dire
- Relis tous les contrats plusieurs fois avant de signer
- Les retours d'ex peuvent être significatifs mais prudence""",

    ('gemini', 8): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 8

**En une phrase :** Les communications sur les finances partagées et les sujets profonds demandent de la délicatesse.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec la curiosité des Gémeaux. Les discussions sur l'argent partagé peuvent être confuses. Les conversations profondes peuvent tourner en rond ou révéler des informations importantes.

## Ce que tu pourrais vivre
- De la confusion sur les finances partagées
- Des révélations ou des secrets qui refont surface
- Des discussions profondes qui nécessitent plusieurs reprises

## Conseils pour cette période
- Sois très précis·e dans les communications financières
- Les secrets qui reviennent demandent à être traités
- Approfondis les discussions importantes sur plusieurs sessions""",

    ('gemini', 9): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 9

**En une phrase :** Les voyages et les communications sur les grandes idées demandent de la flexibilité.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec l'adaptabilité des Gémeaux. Les voyages peuvent être perturbés mais aussi pleins de surprises. Les discussions philosophiques peuvent être stimulantes mais aussi confuses.

## Ce que tu pourrais vivre
- Des changements de plans de voyage
- Des idées qui évoluent et se contredisent
- Un besoin de revoir tes croyances

## Conseils pour cette période
- Sois flexible avec tes plans de voyage
- Les idées contradictoires peuvent mener à une synthèse
- Révise tes connaissances plutôt que d'en acquérir de nouvelles""",

    ('gemini', 10): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 10

**En une phrase :** Les communications professionnelles et ta réputation publique demandent une attention maximale.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec l'énergie communicative des Gémeaux. Tes paroles publiques peuvent être mal interprétées. Les projets professionnels peuvent nécessiter des révisions. Ta réputation peut être affectée par des malentendus.

## Ce que tu pourrais vivre
- Des communications professionnelles mal comprises
- Des projets qui nécessitent d'être retravaillés
- Des anciens collègues ou employeurs qui réapparaissent

## Conseils pour cette période
- Sois très soigneux·se dans tes communications officielles
- Révise les projets existants plutôt que d'en lancer de nouveaux
- Les retours d'anciens contacts professionnels peuvent être utiles""",

    ('gemini', 11): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 11

**En une phrase :** Les communications dans tes réseaux sociaux et tes projets collectifs sont intenses.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec l'énergie sociale des Gémeaux. Les communications dans tes groupes peuvent être confuses ou mal comprises. Les réseaux sociaux peuvent être une source de malentendus.

## Ce que tu pourrais vivre
- Des malentendus avec des amis ou dans des groupes
- Des messages sur les réseaux sociaux qui créent des problèmes
- Le retour d'anciens amis avec des nouvelles importantes

## Conseils pour cette période
- Réfléchis avant de poster sur les réseaux sociaux
- Clarifie les malentendus avec tes amis directement
- Les anciens amis qui reviennent peuvent avoir des raisons""",

    ('gemini', 12): """# ☿℞ Mercure rétrograde en Gémeaux — Maison 12

**En une phrase :** Ton mental intérieur est très actif et demande de la gestion consciente.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec l'agitation mentale des Gémeaux. Tes pensées peuvent être particulièrement agitées. Des informations cachées peuvent émerger. Les rêves peuvent être très communicatifs.

## Ce que tu pourrais vivre
- Un mental très actif, parfois jusqu'à l'insomnie
- Des secrets ou des informations cachées qui émergent
- Des rêves significatifs avec des messages

## Conseils pour cette période
- Pratique des techniques de calme mental
- Note tes rêves et tes intuitions
- Les secrets qui émergent demandent à être traités avec sagesse""",

    # ============== CANCER (Cancer) ==============
    ('cancer', 1): """# ☿℞ Mercure rétrograde en Cancer — Maison 1

**En une phrase :** Ta façon de communiquer sur toi est teintée d'émotions et nécessite de la clarté.

## L'énergie du moment
Mercure rétrograde en Cancer dans ta maison 1 rend tes communications très personnelles et émotionnelles. Tu peux avoir du mal à t'exprimer clairement car les émotions interfèrent. C'est le moment de revoir comment tu te présentes au monde.

## Ce que tu pourrais vivre
- Des communications personnelles chargées d'émotion
- Des malentendus liés à ta sensibilité
- Un besoin de revoir ton image et ta façon de t'exprimer

## Conseils pour cette période
- Sépare ce que tu ressens de ce que tu veux communiquer
- Prends du recul avant de répondre à ce qui te touche
- C'est un bon moment pour réfléchir à ton message personnel""",

    ('cancer', 2): """# ☿℞ Mercure rétrograde en Cancer — Maison 2

**En une phrase :** Tes décisions financières sont influencées par tes émotions et nécessitent du recul.

## L'énergie du moment
Mercure rétrograde traverse ta maison des ressources avec l'émotivité du Cancer. Les achats émotionnels ou nostalgiques peuvent se multiplier. Les communications sur l'argent avec la famille peuvent être délicates.

## Ce que tu pourrais vivre
- Des achats émotionnels que tu pourrais regretter
- Des discussions sur l'argent qui touchent des cordes sensibles
- Un besoin de sécurité financière accru

## Conseils pour cette période
- Évite les achats réconfort impulsifs
- Sépare les discussions émotionnelles des discussions financières
- Revois ton budget avec un regard objectif""",

    ('cancer', 3): """# ☿℞ Mercure rétrograde en Cancer — Maison 3

**En une phrase :** Les communications quotidiennes sont plus sensibles et les malentendus plus émotionnels.

## L'énergie du moment
Mercure rétrograde traverse ta maison de la communication avec la sensibilité du Cancer. Les échanges avec l'entourage proche peuvent être chargés émotionnellement. Les malentendus peuvent toucher plus profondément que d'habitude.

## Ce que tu pourrais vivre
- Des conversations avec la famille qui réveillent des émotions
- Des malentendus qui blessent plus que prévu
- Un besoin de communications plus profondes et authentiques

## Conseils pour cette période
- Exprime tes émotions clairement plutôt que de les sous-entendre
- Prends les malentendus avec du recul émotionnel
- C'est un bon moment pour des conversations de cœur à cœur""",

    ('cancer', 4): """# ☿℞ Mercure rétrograde en Cancer — Maison 4

**En une phrase :** Les communications familiales et les souvenirs sont au cœur de cette période.

## L'énergie du moment
Mercure rétrograde en Cancer dans la maison 4 est très significatif pour tout ce qui touche au foyer et à la famille. Les souvenirs refont surface, les vieux albums et les conversations du passé reviennent. Les projets domestiques peuvent être retardés.

## Ce que tu pourrais vivre
- Des souvenirs et des émotions du passé qui remontent
- Des discussions familiales sur le passé
- Des projets de maison qui nécessitent d'être revus

## Conseils pour cette période
- Accueille les souvenirs comme des occasions de guérison
- Résous les vieux malentendus familiaux
- C'est un bon moment pour organiser photos et souvenirs""",

    ('cancer', 5): """# ☿℞ Mercure rétrograde en Cancer — Maison 5

**En une phrase :** Les communications romantiques et créatives sont très émotionnelles.

## L'énergie du moment
Mercure rétrograde traverse ta maison des plaisirs avec l'émotivité du Cancer. Les déclarations d'amour peuvent être mal comprises. La créativité est nourrie par les émotions et les souvenirs. Les relations avec les enfants peuvent être plus sensibles.

## Ce que tu pourrais vivre
- Des communications romantiques très émotionnelles
- Une créativité inspirée par la nostalgie et les souvenirs
- Des situations avec les enfants qui demandent de la patience

## Conseils pour cette période
- Exprime tes sentiments clairement en amour
- Utilise ta sensibilité pour créer
- Sois patient·e et compréhensif·ve avec les enfants""",

    ('cancer', 6): """# ☿℞ Mercure rétrograde en Cancer — Maison 6

**En une phrase :** Les routines quotidiennes et la santé sont influencées par l'état émotionnel.

## L'énergie du moment
Mercure rétrograde traverse ta maison du quotidien avec la sensibilité du Cancer. Ton travail peut être affecté par ton état émotionnel. Les communications avec les collègues peuvent être plus délicates. La santé peut refléter les émotions.

## Ce que tu pourrais vivre
- Un travail affecté par ton humeur
- Des communications sensibles avec les collègues
- Des symptômes de santé liés au stress émotionnel

## Conseils pour cette période
- Prends soin de ton bien-être émotionnel au travail
- Sépare les émotions personnelles du professionnel
- Écoute ce que ton corps te dit sur tes émotions""",

    ('cancer', 7): """# ☿℞ Mercure rétrograde en Cancer — Maison 7

**En une phrase :** Les communications dans les relations sont très sensibles et demandent de la délicatesse.

## L'énergie du moment
Mercure rétrograde traverse ta maison des partenariats avec l'émotivité du Cancer. Les discussions avec ton partenaire peuvent facilement toucher des zones sensibles. Les malentendus peuvent créer des blessures émotionnelles.

## Ce que tu pourrais vivre
- Des discussions de couple très émotionnelles
- Des malentendus qui blessent plus que prévu
- Le retour de sentiments ou de partenaires du passé

## Conseils pour cette période
- Communique avec douceur et écoute avec empathie
- Ne prends pas les malentendus personnellement
- Les retours du passé ont peut-être quelque chose à enseigner""",

    ('cancer', 8): """# ☿℞ Mercure rétrograde en Cancer — Maison 8

**En une phrase :** Les communications sur les sujets profonds et l'argent partagé sont très chargées.

## L'énergie du moment
Mercure rétrograde traverse ta maison des transformations avec la profondeur émotionnelle du Cancer. Les discussions sur l'héritage, l'argent partagé, la mort peuvent être très intenses. Les secrets de famille peuvent refaire surface.

## Ce que tu pourrais vivre
- Des discussions très émotionnelles sur les finances partagées
- Des secrets ou des histoires de famille qui reviennent
- Un besoin de traiter des émotions profondes

## Conseils pour cette période
- Aborde les sujets sensibles avec beaucoup de douceur
- Les secrets qui reviennent demandent à être traités
- C'est un bon moment pour guérir des blessures anciennes""",

    ('cancer', 9): """# ☿℞ Mercure rétrograde en Cancer — Maison 9

**En une phrase :** Les voyages et les croyances sont teintés de nostalgie et d'émotion.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'expansion avec la nostalgie du Cancer. Les voyages vers des lieux connus ou significatifs sont favorisés. Les croyances héritées de la famille peuvent être reconsidérées.

## Ce que tu pourrais vivre
- Des voyages de mémoire ou de retour aux sources
- Une révision des croyances transmises par la famille
- Une envie d'apprendre sur tes racines ou ton histoire

## Conseils pour cette période
- Les voyages dans des lieux familiers peuvent être ressourçants
- Réexamine ce que tu crois et d'où ça vient
- C'est un bon moment pour explorer ton histoire familiale""",

    ('cancer', 10): """# ☿℞ Mercure rétrograde en Cancer — Maison 10

**En une phrase :** Les communications professionnelles sont influencées par les émotions et nécessitent de la prudence.

## L'énergie du moment
Mercure rétrograde traverse ta maison de carrière avec la sensibilité du Cancer. Les émotions peuvent interférer avec le professionnalisme. Les communications avec la hiérarchie peuvent être délicates. Ta réputation peut être affectée par des malentendus.

## Ce que tu pourrais vivre
- Des émotions qui affectent ton travail
- Des communications sensibles avec les supérieurs
- Un besoin de sécurité dans ta carrière

## Conseils pour cette période
- Sépare les émotions personnelles du travail autant que possible
- Sois diplomate dans tes communications professionnelles
- Réfléchis à ce que tu veux vraiment dans ta carrière""",

    ('cancer', 11): """# ☿℞ Mercure rétrograde en Cancer — Maison 11

**En une phrase :** Les communications avec les amis sont plus émotionnelles et significatives.

## L'énergie du moment
Mercure rétrograde traverse ta maison des amitiés avec l'émotivité du Cancer. Les amitiés qui comptent vraiment sont mises en lumière. Les communications dans les groupes peuvent être plus sensibles.

## Ce que tu pourrais vivre
- Des conversations profondes avec de vrais amis
- Des malentendus dans les groupes qui touchent émotionnellement
- Le retour d'anciens amis avec des nouvelles significatives

## Conseils pour cette période
- Nourris les amitiés qui comptent vraiment
- Ne prends pas les malentendus de groupe personnellement
- Les anciens amis qui reviennent ont peut-être quelque chose d'important""",

    ('cancer', 12): """# ☿℞ Mercure rétrograde en Cancer — Maison 12

**En une phrase :** Ton monde intérieur est très actif et les émotions inconscientes demandent de l'attention.

## L'énergie du moment
Mercure rétrograde traverse ta maison de l'inconscient avec la profondeur du Cancer. Des émotions très anciennes peuvent remonter. Les rêves peuvent être très significatifs et émotionnels. C'est un temps puissant pour l'introspection.

## Ce que tu pourrais vivre
- Des émotions anciennes qui remontent sans raison apparente
- Des rêves très chargés émotionnellement
- Un besoin de solitude et de réflexion

## Conseils pour cette période
- Accueille les émotions qui remontent avec compassion
- Note tes rêves et leurs messages
- C'est un excellent moment pour la thérapie ou le travail intérieur""",
}

async def insert_interpretations():
    """Insert all mercury_retrograde interpretations for Aries, Taurus, Gemini, Cancer"""
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
