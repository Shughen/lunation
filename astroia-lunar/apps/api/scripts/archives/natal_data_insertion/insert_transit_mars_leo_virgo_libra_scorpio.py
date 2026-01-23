#!/usr/bin/env python3
"""Insert transit_mars interpretations for Leo, Virgo, Libra, Scorpio (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MARS_INTERPRETATIONS = {
    # ============== LEO ==============
    ('leo', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie royale s'enflamme et tu es prêt(e) à conquérir le monde!

## L'énergie du moment
Mars traverse ta maison I avec une énergie de feu qui amplifie ta présence naturelle. Tu dégages une aura de puissance et de détermination qui impressionne. C'est le moment de prendre les devants et de briller par l'action.

## Ce que tu pourrais vivre
- Un charisme et une énergie décuplés
- L'envie de diriger et d'agir
- Une confiance en soi flamboyante

## Conseils pour ce transit
- Lance-toi dans des projets audacieux
- Canalise cette énergie dans le sport
- Attention à l'ego et à l'impulsivité""",

    ('leo', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se mobilise pour conquérir richesse et reconnaissance.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de prospérité et de possessions. Tu as l'énergie pour te battre pour ce que tu mérites – financièrement et en termes de reconnaissance. Attention aux dépenses grandioses.

## Ce que tu pourrais vivre
- Une motivation forte pour gagner
- Des achats impulsifs et luxueux
- Des conflits autour des ressources

## Conseils pour ce transit
- Demande ce que tu vaux vraiment
- Contrôle les dépenses de prestige
- Investis dans ce qui te valorise""",

    ('leo', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus percutantes et énergiques.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes mots plus impactants et tes idées plus affirmées. Tu as envie de convaincre, de briller par ton éloquence. Les échanges peuvent être passionnés.

## Ce que tu pourrais vivre
- Des discours passionnés
- Des débats animés
- Une communication plus directe

## Conseils pour ce transit
- Utilise ton éloquence naturelle
- Évite les conflits d'ego dans les échanges
- Canalise dans la création ou l'enseignement""",

    ('leo', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec force et ambition.

## L'énergie du moment
Mars active ta maison IV, te poussant à agir dans ton espace domestique. Travaux ambitieux, réorganisation royale – tu veux que ton chez-toi reflète ta grandeur. Les tensions familiales sont possibles.

## Ce que tu pourrais vivre
- Des projets domestiques ambitieux
- Des conflits de leadership en famille
- Un besoin de régner sur ton territoire

## Conseils pour ce transit
- Transforme ton foyer avec style
- Évite les conflits d'autorité en famille
- Crée un espace qui te ressemble""",

    ('leo', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions explosent avec une intensité royale!

## L'énergie du moment
Mars embrase ta maison V, ta maison naturelle! C'est une période exceptionnelle pour la créativité, les romances passionnées et les plaisirs de la vie. Tu rayonnes et attires naturellement l'admiration.

## Ce que tu pourrais vivre
- Une créativité flamboyante
- Des romances passionnées et théâtrales
- Des victoires dans les compétitions

## Conseils pour ce transit
- Crée avec audace et passion
- Vis tes amours intensément
- Brille sur scène, littéralement ou non""",

    ('leo', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail est royale, mais attention au surmenage.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail impressionnante. Tu veux exceller et être reconnu(e) pour ton efficacité. L'exercice physique est essentiel.

## Ce que tu pourrais vivre
- Une productivité exceptionnelle
- Des tensions avec ceux qui ralentissent
- Un besoin de mouvement physique

## Conseils pour ce transit
- Travaille avec excellence
- Évite de dominer tes collègues
- Intègre le sport noble dans ta routine""",

    ('leo', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont sous haute tension, entre passion royale et confrontation.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Les conflits d'ego en couple peuvent éclater, mais cette énergie peut aussi alimenter une passion ardente.

## Ce que tu pourrais vivre
- Des confrontations de pouvoir en couple
- Une passion théâtrale
- Des partenariats dynamiques

## Conseils pour ce transit
- Partage le trône dans la relation
- Transforme les conflits en passion
- Choisis des partenaires à ta hauteur""",

    ('leo', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions de pouvoir et d'intimité sont au cœur de cette période intense.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les enjeux de pouvoir. La sexualité est passionnée, les questions financières partagées sont urgentes.

## Ce que tu pourrais vivre
- Une sexualité intense et dominante
- Des conflits autour du pouvoir et de l'argent
- Une transformation profonde de l'ego

## Conseils pour ce transit
- Explore l'intimité avec générosité
- Règle les questions de pouvoir financier
- Accepte de transformer ton ego""",

    ('leo', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure et la quête de grandeur t'appellent avec force!

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif d'horizons royaux. Voyages prestigieux, études ambitieuses, quêtes philosophiques – tu vises grand.

## Ce que tu pourrais vivre
- Un voyage mémorable
- Des débats où tu brilles
- Une quête de sens grandiose

## Conseils pour ce transit
- Vise des destinations prestigieuses
- Partage ta vision avec conviction
- Apprends des maîtres""",

    ('leo', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'enflamme – tu vises le trône!

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour conquérir le sommet. C'est le moment de prendre des initiatives audacieuses pour ta carrière. Attention aux conflits avec d'autres leaders.

## Ce que tu pourrais vivre
- Une ambition royale décuplée
- Des avancées vers le sommet
- Des conflits de pouvoir

## Conseils pour ce transit
- Vise la première place
- Gère les rivalités avec noblesse
- Affirme ton leadership""",

    ('leo', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans le leadership de groupe.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets collectifs. Tu as envie de mener, d'inspirer les groupes, de diriger des causes nobles.

## Ce que tu pourrais vivre
- Un leadership naturel dans les groupes
- Des tensions avec d'autres leaders
- Un engagement pour des causes royales

## Conseils pour ce transit
- Mène avec inspiration
- Partage la reconnaissance
- Engage-toi pour des causes dignes""",

    ('leo', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre repos du guerrier et batailles internes.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. Ton ego peut être mis à l'épreuve. C'est un moment pour le travail intérieur et la régénération.

## Ce que tu pourrais vivre
- De la fatigue ou frustration cachée
- Des défis à l'ego venant de l'ombre
- Un travail spirituel profond

## Conseils pour ce transit
- Accepte le repos du guerrier
- Libère les colères de l'ego
- Prépare ton retour glorieux""",

    # ============== VIRGO ==============
    ('virgo', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle s'affirme avec une force nouvelle et directe.

## L'énergie du moment
Mars traverse ta maison I, te donnant une énergie et une combativité inhabituelles. Tu es plus assertif(ve), plus impatient(e) avec les détails. C'est le moment d'agir plutôt que d'analyser.

## Ce que tu pourrais vivre
- Un boost d'énergie et d'initiative
- L'envie d'agir sans trop réfléchir
- Une affirmation de soi plus directe

## Conseils pour ce transit
- Passe à l'action maintenant
- Équilibre analyse et impulsion
- Canalise l'énergie dans le sport""",

    ('virgo', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se concentre sur les gains financiers avec efficacité.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de sécurité matérielle par l'action. Tu as l'énergie pour optimiser tes revenus, demander ce que tu mérites. Attention aux dépenses impulsives.

## Ce que tu pourrais vivre
- Une motivation forte pour améliorer tes finances
- Des achats utiles mais impulsifs
- Une affirmation de ta valeur professionnelle

## Conseils pour ce transit
- Négocie activement ton salaire
- Évite les achats non planifiés
- Investis dans tes compétences""",

    ('virgo', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus directes et efficaces.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes échanges plus vifs et tes analyses plus percutantes. Tu as moins de patience pour les détails inutiles et tu vas droit au but.

## Ce que tu pourrais vivre
- Des communications plus directes
- Des analyses rapides et efficaces
- Des frictions avec l'entourage proche

## Conseils pour ce transit
- Exprime-toi avec clarté
- Évite d'être trop critique
- Utilise cette énergie pour apprendre vite""",

    ('virgo', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec efficacité.

## L'énergie du moment
Mars active ta maison IV, te poussant à agir dans ton espace domestique. Organisation intensive, ménage de printemps, travaux d'amélioration – tu veux que tout soit parfait.

## Ce que tu pourrais vivre
- Des projets d'organisation domestique
- Des tensions familiales possibles
- Un besoin d'efficacité à la maison

## Conseils pour ce transit
- Organise et améliore ton foyer
- Gère les tensions avec calme
- Crée un espace fonctionnel""",

    ('virgo', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'expriment avec une énergie nouvelle!

## L'énergie du moment
Mars embrase ta maison V, éveillant créativité et désirs avec plus de spontanéité que d'habitude. Tu as envie de créer, de jouer, de vivre des passions sans trop les analyser.

## Ce que tu pourrais vivre
- Une créativité plus spontanée
- Des passions amoureuses directes
- Des loisirs actifs et énergiques

## Conseils pour ce transit
- Crée sans trop réfléchir
- Vis tes passions maintenant
- Canalise dans des activités physiques""",

    ('virgo', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail atteint des sommets d'efficacité!

## L'énergie du moment
Mars dynamise ta maison VI, ta maison naturelle! C'est une période exceptionnelle pour le travail et la productivité. Tu es ultra-efficace mais aussi plus exigeant(e). L'exercice physique est essentiel.

## Ce que tu pourrais vivre
- Une productivité exceptionnelle
- Une exigence accrue envers toi et les autres
- Un besoin de mouvement physique

## Conseils pour ce transit
- Excelle dans ton travail
- Évite le perfectionnisme excessif
- Intègre un sport dans ta routine""",

    ('virgo', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont dynamisées, entre efficacité et confrontation.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Tu as moins de patience pour les imperfections des autres. Les partenariats demandent de l'action.

## Ce que tu pourrais vivre
- Des confrontations sur les détails
- Une volonté d'améliorer les relations
- Des partenariats actifs

## Conseils pour ce transit
- Communique tes besoins clairement
- Évite la critique excessive
- Agis pour améliorer tes relations""",

    ('virgo', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions d'intimité et de transformation demandent ton attention.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les enjeux de ressources partagées. Tu analyses ces domaines avec une nouvelle énergie d'action.

## Ce que tu pourrais vivre
- Une sexualité plus intense et directe
- Des questions financières à résoudre
- Une transformation par l'action

## Conseils pour ce transit
- Explore l'intimité avec confiance
- Règle les questions d'argent partagé
- Agis pour te transformer""",

    ('virgo', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure et l'expansion intellectuelle t'appellent.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif de connaissances pratiques et d'horizons nouveaux. Voyages utiles, formations efficaces, applications concrètes de la philosophie.

## Ce que tu pourrais vivre
- Un voyage avec un but précis
- Des apprentissages intensifs
- Une quête de sens pratique

## Conseils pour ce transit
- Apprends de façon active
- Voyage avec un objectif
- Applique ce que tu découvres""",

    ('virgo', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'enflamme avec efficacité.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour exceller professionnellement. C'est le moment de prendre des initiatives concrètes pour ta carrière.

## Ce que tu pourrais vivre
- Une productivité professionnelle maximale
- Des avancées par l'efficacité
- Des tensions avec la hiérarchie

## Conseils pour ce transit
- Excelle dans ton travail
- Gère les conflits avec professionnalisme
- Vise des résultats concrets""",

    ('virgo', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans l'action collective utile.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie d'agir efficacement pour des causes pratiques.

## Ce que tu pourrais vivre
- Un rôle actif dans des groupes
- Des tensions avec des amis sur les méthodes
- Un engagement pour des causes concrètes

## Conseils pour ce transit
- Apporte ton efficacité aux groupes
- Évite de critiquer les autres
- Engage-toi utilement""",

    ('virgo', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre analyse profonde et repos.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. L'énergie peut être dirigée vers l'analyse de l'inconscient ou se manifester par de la fatigue.

## Ce que tu pourrais vivre
- De la fatigue mentale
- Une analyse profonde de soi
- Un besoin de repos productif

## Conseils pour ce transit
- Repose ton esprit analytique
- Médite plutôt qu'analyser
- Prépare silencieusement tes prochains projets""",

    # ============== LIBRA ==============
    ('libra', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle s'affirme de façon inhabituelle et directe!

## L'énergie du moment
Mars traverse ta maison I, t'apportant une énergie combative qui contraste avec ton naturel diplomatique. Tu es plus assertif(ve), plus direct(e), prêt(e) à te battre pour toi-même.

## Ce que tu pourrais vivre
- Un boost d'énergie personnelle
- L'envie de t'affirmer fortement
- Des confrontations possibles

## Conseils pour ce transit
- Ose t'affirmer pour toi-même
- Équilibre force et diplomatie
- Canalise l'énergie constructivement""",

    ('libra', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se concentre sur tes finances avec détermination.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de sécurité matérielle. Tu as l'énergie pour te battre pour ce que tu mérites financièrement. Attention aux dépenses impulsives.

## Ce que tu pourrais vivre
- Une motivation financière forte
- Des achats impulsifs possibles
- Des conflits autour de l'argent

## Conseils pour ce transit
- Défends tes intérêts financiers
- Évite les dépenses non réfléchies
- Valorise ce que tu apportes""",

    ('libra', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus directes et affirmées.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes échanges plus vifs et moins diplomatiques que d'habitude. Tu as envie de dire ce que tu penses vraiment.

## Ce que tu pourrais vivre
- Des communications plus directes
- Des débats passionnés
- Des frictions avec les proches

## Conseils pour ce transit
- Exprime-toi avec force mais tact
- Évite les conflits inutiles
- Utilise cette énergie pour défendre tes idées""",

    ('libra', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec intensité.

## L'énergie du moment
Mars active ta maison IV, te poussant à agir dans ton espace domestique. Travaux, réorganisation, ou tensions familiales – ton chez-toi demande de l'action.

## Ce que tu pourrais vivre
- Des projets domestiques actifs
- Des tensions familiales possibles
- Un besoin de transformer ton espace

## Conseils pour ce transit
- Canalise l'énergie dans l'amélioration
- Gère les conflits avec diplomatie
- Crée un espace harmonieux""",

    ('libra', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'enflamment avec une énergie nouvelle!

## L'énergie du moment
Mars embrase ta maison V, éveillant créativité et désirs avec plus d'audace. Les romances sont passionnées, les projets créatifs sont dynamiques.

## Ce que tu pourrais vivre
- Une créativité plus audacieuse
- Des passions amoureuses intenses
- Des loisirs énergiques

## Conseils pour ce transit
- Crée avec audace
- Vis tes passions pleinement
- Équilibre passion et harmonie""",

    ('libra', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail s'intensifie avec efficacité.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail accrue. Tu es plus direct(e) avec tes collègues et moins tolérant(e) envers l'inefficacité.

## Ce que tu pourrais vivre
- Une productivité augmentée
- Des tensions avec des collègues
- Un besoin d'activité physique

## Conseils pour ce transit
- Travaille efficacement
- Garde ta diplomatie au bureau
- Intègre le sport dans ta routine""",

    ('libra', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont sous haute tension – confrontation ou passion?

## L'énergie du moment
Mars traverse ta maison VII, ta maison naturelle, avec une énergie opposée à ta nature! Les relations sont dynamisées, parfois par le conflit, parfois par la passion renouvelée.

## Ce que tu pourrais vivre
- Des confrontations en couple
- Une passion intense ravivée
- Des partenariats actifs ou conflictuels

## Conseils pour ce transit
- Affirme-toi dans la relation
- Transforme la tension en passion
- Cherche l'équilibre dans la confrontation""",

    ('libra', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions d'intimité et de pouvoir sont au premier plan.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les enjeux de ressources partagées. La sexualité est plus directe, les questions financières plus urgentes.

## Ce que tu pourrais vivre
- Une sexualité plus intense
- Des négociations financières actives
- Une transformation par la confrontation

## Conseils pour ce transit
- Explore l'intimité avec audace
- Règle les questions d'argent partagé
- Accepte les transformations""",

    ('libra', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure et les horizons lointains t'appellent avec force.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif d'exploration et de vérité. Voyages, études, débats philosophiques – tu as l'énergie pour élargir ta vision.

## Ce que tu pourrais vivre
- Un voyage stimulant
- Des débats passionnés sur les idées
- Une quête de sens active

## Conseils pour ce transit
- Explore de nouveaux horizons
- Défends tes convictions avec équilibre
- Apprends activement""",

    ('libra', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'affirme avec force.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour avancer dans ta carrière de façon plus assertive. C'est le moment de prendre des initiatives audacieuses.

## Ce que tu pourrais vivre
- Une ambition plus affirmée
- Des avancées par l'action directe
- Des tensions possibles avec l'autorité

## Conseils pour ce transit
- Prends des initiatives de carrière
- Équilibre ambition et diplomatie
- Affirme ta valeur professionnelle""",

    ('libra', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans l'action collective.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie d'agir pour des causes, parfois de façon plus directe que d'habitude.

## Ce que tu pourrais vivre
- Un dynamisme dans les groupes
- Des tensions sur les directions à prendre
- Un engagement militant

## Conseils pour ce transit
- Apporte ton énergie aux groupes
- Gère les différends avec diplomatie
- Engage-toi pour des causes justes""",

    ('libra', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre frustrations cachées et travail sur soi.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. L'énergie peut être frustrée ou canalisée vers un profond travail intérieur.

## Ce que tu pourrais vivre
- De la frustration ou fatigue cachée
- Des conflits intérieurs
- Un travail spirituel profond

## Conseils pour ce transit
- Libère les frustrations en douceur
- Médite sur tes colères refoulées
- Prépare tes prochaines actions en silence""",

    # ============== SCORPIO ==============
    ('scorpio', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle explose avec une force brute et directe!

## L'énergie du moment
Mars, ton ancien maître, traverse ta maison I avec une énergie de feu! Tu dégages une puissance et une détermination impressionnantes. C'est le moment de prendre des initiatives audacieuses et de t'affirmer pleinement.

## Ce que tu pourrais vivre
- Une énergie et une combativité décuplées
- L'envie de conquérir et d'agir
- Une présence magnétique amplifiée

## Conseils pour ce transit
- Lance-toi dans l'action
- Canalise cette puissance positivement
- Attention à l'impulsivité et l'agressivité""",

    ('scorpio', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se mobilise pour conquérir des ressources avec intensité.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de pouvoir matériel. Tu as l'énergie pour te battre intensément pour tes finances et tes possessions.

## Ce que tu pourrais vivre
- Une motivation financière intense
- Des acquisitions par la force
- Des conflits autour des ressources

## Conseils pour ce transit
- Défends tes intérêts avec stratégie
- Évite les dépenses impulsives
- Investis dans ce qui compte vraiment""",

    ('scorpio', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus directes et percutantes.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes mots encore plus tranchants et tes idées plus combatives. Tu as envie de convaincre avec force.

## Ce que tu pourrais vivre
- Des communications puissantes
- Des débats intenses
- Des frictions avec les proches

## Conseils pour ce transit
- Utilise ton pouvoir de persuasion
- Évite les paroles blessantes
- Canalise dans l'investigation""",

    ('scorpio', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec une force transformatrice.

## L'énergie du moment
Mars active ta maison IV, te poussant à transformer ton espace domestique avec intensité. Travaux profonds, réorganisation radicale, ou tensions familiales intenses.

## Ce que tu pourrais vivre
- Des transformations domestiques profondes
- Des conflits familiaux intenses
- Un besoin de contrôler ton territoire

## Conseils pour ce transit
- Transforme ton foyer positivement
- Gère les tensions avec profondeur
- Protège ton espace sacré""",

    ('scorpio', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'enflamment avec une intensité extrême!

## L'énergie du moment
Mars embrase ta maison V, décuplant créativité et désirs. Les romances sont passionnées et intenses, les projets créatifs sont puissants.

## Ce que tu pourrais vivre
- Une créativité puissante
- Des passions dévorantes
- Des compétitions intenses

## Conseils pour ce transit
- Crée avec toute ton intensité
- Vis tes passions profondément
- Canalise dans des expressions artistiques""",

    ('scorpio', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail atteint une intensité remarquable.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail intense. Tu es ultra-efficace mais aussi très exigeant(e). L'exercice physique intense est essentiel.

## Ce que tu pourrais vivre
- Une productivité intense
- Des tensions avec ceux qui ne suivent pas
- Un besoin de sport intense

## Conseils pour ce transit
- Travaille avec intensité contrôlée
- Évite d'écraser les collègues
- Fais du sport exigeant""",

    ('scorpio', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont sous haute tension, entre passion et combat.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Les confrontations peuvent être violentes mais cette énergie peut aussi créer une passion brûlante.

## Ce que tu pourrais vivre
- Des confrontations intenses en couple
- Une passion dévorante
- Des combats de pouvoir en partenariat

## Conseils pour ce transit
- Canalise la tension en passion
- Évite les jeux de pouvoir destructeurs
- Choisis tes batailles relationnelles""",

    ('scorpio', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions d'intimité et de pouvoir atteignent leur paroxysme!

## L'énergie du moment
Mars plonge dans ta maison VIII, ta maison naturelle avec une énergie de feu! La sexualité, le pouvoir, les finances partagées, les transformations profondes – tout est intensifié au maximum.

## Ce que tu pourrais vivre
- Une sexualité extrêmement intense
- Des combats de pouvoir profonds
- Une transformation radicale

## Conseils pour ce transit
- Explore l'intimité avec conscience
- Gère le pouvoir avec sagesse
- Accepte une transformation profonde""",

    ('scorpio', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure et la quête de vérité t'appellent avec intensité.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif de vérité profonde et d'horizons transformateurs. Voyages initiatiques, études ésotériques, quêtes de sens intenses.

## Ce que tu pourrais vivre
- Un voyage transformateur
- Des débats sur les vérités cachées
- Une quête spirituelle intense

## Conseils pour ce transit
- Explore les profondeurs de l'existence
- Défends tes convictions avec passion
- Recherche les vérités cachées""",

    ('scorpio', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'enflamme avec une force stratégique.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour conquérir le sommet par la stratégie et la force. C'est le moment de prendre le pouvoir professionnellement.

## Ce que tu pourrais vivre
- Une ambition intense et stratégique
- Des avancées par la force
- Des conflits de pouvoir au travail

## Conseils pour ce transit
- Vise le sommet avec stratégie
- Gère les rivalités avec intelligence
- Affirme ton pouvoir professionnel""",

    ('scorpio', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans l'action collective transformatrice.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie de transformer les groupes de l'intérieur, de mener des causes profondes.

## Ce que tu pourrais vivre
- Un leadership intense dans les groupes
- Des tensions de pouvoir avec des amis
- Un engagement pour des causes transformatrices

## Conseils pour ce transit
- Mène avec ta puissance naturelle
- Évite les manipulations de groupe
- Engage-toi pour des transformations profondes""",

    ('scorpio', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre batailles de l'ombre et régénération.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension intense entre action et retrait. L'énergie peut travailler dans l'ombre ou se manifester par des ennemis cachés.

## Ce que tu pourrais vivre
- Des combats intérieurs intenses
- Des ennemis cachés qui se manifestent
- Une régénération profonde

## Conseils pour ce transit
- Affronte tes démons intérieurs
- Identifie les forces cachées
- Prépare ta renaissance en silence""",
}

async def insert_interpretations():
    """Insert transit Mars interpretations into database."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_MARS_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_mars',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='transit_mars',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            inserted += 1

        await db.commit()
        print(f"✅ Transit Mars (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
