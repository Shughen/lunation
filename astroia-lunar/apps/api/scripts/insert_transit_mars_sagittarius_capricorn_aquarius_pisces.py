#!/usr/bin/env python3
"""Insert transit_mars interpretations for Sagittarius, Capricorn, Aquarius, Pisces (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MARS_INTERPRETATIONS = {
    # ============== SAGITTARIUS ==============
    ('sagittarius', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie aventurière explose et tu es prêt(e) à conquérir de nouveaux territoires!

## L'énergie du moment
Mars traverse ta maison I avec une énergie de feu qui amplifie ton enthousiasme naturel! Tu dégages une aura d'optimisme combatif et de détermination joyeuse. C'est le moment de te lancer dans de nouvelles aventures.

## Ce que tu pourrais vivre
- Un boost d'énergie et d'enthousiasme
- L'envie de partir à l'aventure
- Une affirmation de soi spontanée

## Conseils pour ce transit
- Lance-toi dans de nouvelles aventures
- Canalise cette énergie dans le sport
- Attention à l'impulsivité excessive""",

    ('sagittarius', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se mobilise pour des conquêtes financières audacieuses.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de prospérité par l'action. Tu as l'énergie pour prendre des risques financiers ou te battre pour de meilleures opportunités.

## Ce que tu pourrais vivre
- Une motivation financière optimiste
- Des investissements audacieux
- Des dépenses aventureuses

## Conseils pour ce transit
- Saisis les opportunités financières
- Évite les risques excessifs
- Investis dans tes projets d'expansion""",

    ('sagittarius', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus directes et enthousiastes.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes échanges plus passionnés et tes idées plus affirmées. Tu as envie de partager tes convictions avec énergie.

## Ce que tu pourrais vivre
- Des communications passionnées
- Des débats philosophiques animés
- Des déplacements rapides et nombreux

## Conseils pour ce transit
- Partage tes idées avec passion
- Évite le fanatisme dans les débats
- Canalise dans l'enseignement ou l'écriture""",

    ('sagittarius', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec dynamisme.

## L'énergie du moment
Mars active ta maison IV, te poussant à transformer ton espace domestique avec enthousiasme. Travaux, déménagement vers quelque chose de plus grand, ou tensions familiales animées.

## Ce que tu pourrais vivre
- Des projets domestiques ambitieux
- Des tensions familiales possibles
- Un besoin d'espace et de liberté chez toi

## Conseils pour ce transit
- Transforme ton foyer avec joie
- Gère les conflits avec optimisme
- Crée un espace qui inspire l'aventure""",

    ('sagittarius', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'enflamment avec une joie explosive!

## L'énergie du moment
Mars embrase ta maison V, décuplant ta créativité et tes désirs avec enthousiasme. Les romances sont aventureuses, les projets créatifs sont audacieux, les jeux sont compétitifs!

## Ce que tu pourrais vivre
- Une créativité audacieuse et joyeuse
- Des romances aventureuses
- Des compétitions sportives passionnées

## Conseils pour ce transit
- Crée avec audace et joie
- Vis tes passions comme des aventures
- Canalise dans le sport ou les arts""",

    ('sagittarius', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail est maximale mais tu veux rester libre.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail impressionnante. Tu es efficace mais tu as du mal avec les contraintes. L'exercice physique en plein air est essentiel.

## Ce que tu pourrais vivre
- Une productivité énergique
- Une impatience avec la routine
- Un besoin d'activité physique variée

## Conseils pour ce transit
- Travaille efficacement mais garde ta liberté
- Varie tes activités physiques
- Évite les conflits avec les règles""",

    ('sagittarius', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont dynamisées par l'aventure et la passion.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles avec enthousiasme. Les couples peuvent vivre des aventures communes ou des tensions philosophiques.

## Ce que tu pourrais vivre
- Des aventures en couple
- Des débats passionnés sur les valeurs
- Des partenariats dynamiques

## Conseils pour ce transit
- Partage des aventures avec ton partenaire
- Transforme les conflits en quêtes communes
- Trouve des partenaires qui partagent ta vision""",

    ('sagittarius', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions d'intimité et de transformation t'appellent à l'aventure intérieure.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les enjeux de transformation. La sexualité est exploratoire, les questions profondes te passionnent.

## Ce que tu pourrais vivre
- Une sexualité plus aventureuse
- Des questions existentielles intenses
- Une transformation par l'exploration

## Conseils pour ce transit
- Explore l'intimité avec ouverture
- Règle les questions financières partagées
- Accepte les transformations avec foi""",

    ('sagittarius', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure et l'expansion sont au cœur de ton existence!

## L'énergie du moment
Mars enflamme ta maison IX, ta maison naturelle! C'est une période exceptionnelle pour les voyages, les études et l'exploration philosophique. Tu as une énergie immense pour repousser tes limites.

## Ce que tu pourrais vivre
- Des voyages aventureux et audacieux
- Des études passionnées
- Une quête de sens active

## Conseils pour ce transit
- Pars à l'aventure sans hésiter
- Défends tes convictions avec passion
- Explore de nouveaux territoires""",

    ('sagittarius', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle vise haut avec enthousiasme.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour viser des objectifs ambitieux. C'est le moment de prendre des initiatives audacieuses pour ta carrière.

## Ce que tu pourrais vivre
- Une ambition visionnaire
- Des avancées par l'audace
- Des conflits avec les limites imposées

## Conseils pour ce transit
- Vise des objectifs ambitieux
- Gère les résistances avec optimisme
- Affirme ta vision professionnelle""",

    ('sagittarius', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans l'action pour de grandes causes.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie d'agir pour des causes universelles et de mener des mouvements.

## Ce que tu pourrais vivre
- Un leadership enthousiaste dans les groupes
- Des débats passionnés sur l'avenir
- Un engagement pour des causes mondiales

## Conseils pour ce transit
- Mène des projets visionnaires
- Partage ton enthousiasme
- Engage-toi pour des causes qui t'inspirent""",

    ('sagittarius', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre quête spirituelle et frustrations cachées.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. L'énergie peut être frustrée ou canalisée vers une profonde quête spirituelle.

## Ce que tu pourrais vivre
- De la frustration face aux limites
- Une quête spirituelle active
- Des combats intérieurs avec la foi

## Conseils pour ce transit
- Explore ta spiritualité activement
- Libère les frustrations par la méditation
- Prépare tes prochaines aventures en silence""",

    # ============== CAPRICORN ==============
    ('capricorn', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle s'affirme avec une force nouvelle et impatiente.

## L'énergie du moment
Mars traverse ta maison I, te donnant une énergie et une combativité inhabituelles. Tu es plus direct(e), plus impatient(e), prêt(e) à agir maintenant plutôt qu'à planifier longuement.

## Ce que tu pourrais vivre
- Un boost d'énergie et d'initiative
- L'envie d'agir immédiatement
- Une affirmation de soi plus directe

## Conseils pour ce transit
- Passe à l'action sans trop attendre
- Équilibre impulsion et stratégie
- Canalise l'énergie dans des projets concrets""",

    ('capricorn', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se concentre sur la construction de ta sécurité financière.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de sécurité matérielle par l'action. Tu as l'énergie pour te battre pour tes intérêts financiers avec détermination.

## Ce que tu pourrais vivre
- Une motivation financière forte
- Des négociations assertives
- Des investissements stratégiques

## Conseils pour ce transit
- Défends tes intérêts financiers
- Évite les dépenses impulsives
- Construis ta sécurité avec action""",

    ('capricorn', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus directes et efficaces.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes échanges plus vifs et tes décisions plus rapides. Tu as moins de patience pour les discussions sans fin.

## Ce que tu pourrais vivre
- Des communications plus directes
- Des décisions rapides
- Des frictions avec les proches

## Conseils pour ce transit
- Exprime-toi avec clarté et force
- Évite d'être trop brusque
- Utilise cette énergie pour négocier""",

    ('capricorn', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec une volonté de transformation.

## L'énergie du moment
Mars active ta maison IV, te poussant à agir dans ton espace domestique. Travaux structurels, réorganisation stratégique, ou tensions familiales autour de l'autorité.

## Ce que tu pourrais vivre
- Des projets domestiques structurels
- Des conflits d'autorité en famille
- Un besoin de solidifier ton territoire

## Conseils pour ce transit
- Améliore ton foyer structurellement
- Gère les tensions avec sagesse
- Construis des fondations solides""",

    ('capricorn', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'expriment avec une énergie nouvelle!

## L'énergie du moment
Mars embrase ta maison V, éveillant créativité et désirs avec plus de spontanéité. Tu as envie de créer, de profiter, de vivre des passions – même si ce n'est pas très "productif".

## Ce que tu pourrais vivre
- Une créativité plus spontanée
- Des passions amoureuses directes
- Des loisirs compétitifs

## Conseils pour ce transit
- Autorise-toi à créer et profiter
- Vis tes passions maintenant
- Équilibre plaisir et responsabilité""",

    ('capricorn', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail atteint des sommets de productivité.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail impressionnante. Tu es ultra-efficace et exigeant(e). L'exercice physique structuré est essentiel.

## Ce que tu pourrais vivre
- Une productivité exceptionnelle
- Des tensions avec les inefficaces
- Un besoin de routine sportive

## Conseils pour ce transit
- Excelle dans ton travail
- Évite d'être trop dur avec les autres
- Intègre un sport structuré""",

    ('capricorn', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont sous tension, entre ambition commune et confrontation.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Les partenariats peuvent être dynamisés par des objectifs communs ou tendus par des conflits de direction.

## Ce que tu pourrais vivre
- Des partenariats actifs et ambitieux
- Des confrontations sur les objectifs
- Une clarification des engagements

## Conseils pour ce transit
- Définis des objectifs communs
- Gère les conflits avec pragmatisme
- Choisis des partenaires fiables""",

    ('capricorn', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions de pouvoir et de ressources partagées demandent de l'action.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant les enjeux de pouvoir et de finances partagées. La sexualité, les investissements, les transformations profondes sont activés.

## Ce que tu pourrais vivre
- Des négociations financières intenses
- Des questions de pouvoir à résoudre
- Une transformation par l'action

## Conseils pour ce transit
- Règle les questions financières partagées
- Gère le pouvoir avec stratégie
- Accepte les transformations nécessaires""",

    ('capricorn', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'expansion et les nouvelles perspectives t'appellent avec force.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif de connaissances pratiques et d'horizons nouveaux. Voyages professionnels, formations stratégiques, expansion de ta vision.

## Ce que tu pourrais vivre
- Un voyage avec des objectifs clairs
- Des formations intensives
- Des débats sur la direction à prendre

## Conseils pour ce transit
- Élargis tes horizons stratégiquement
- Apprends ce qui sert tes objectifs
- Défends ta vision avec assurance""",

    ('capricorn', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'enflamme – tu vises le sommet!

## L'énergie du moment
Mars dynamise ta maison X, ta maison naturelle! C'est une période exceptionnelle pour ta carrière. Tu as l'énergie pour gravir les échelons, prendre le pouvoir, atteindre tes objectifs.

## Ce que tu pourrais vivre
- Une ambition décuplée
- Des avancées professionnelles significatives
- Des conflits de pouvoir au travail

## Conseils pour ce transit
- Saisis les opportunités de carrière
- Gère les rivalités avec stratégie
- Affirme ton autorité naturelle""",

    ('capricorn', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans l'action collective structurée.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie de mener des projets collectifs avec des objectifs clairs.

## Ce que tu pourrais vivre
- Un leadership dans des organisations
- Des tensions sur les méthodes
- Un engagement pour des causes structurantes

## Conseils pour ce transit
- Organise des projets collectifs
- Gère les différends avec pragmatisme
- Engage-toi pour des résultats concrets""",

    ('capricorn', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre préparation stratégique et repos.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. L'énergie peut être canalisée vers une préparation stratégique ou se manifester par de la fatigue.

## Ce que tu pourrais vivre
- De la fatigue ou frustration cachée
- Une préparation en coulisses
- Des ennemis cachés à identifier

## Conseils pour ce transit
- Planifie en secret tes prochains moves
- Repose-toi stratégiquement
- Identifie les obstacles invisibles""",

    # ============== AQUARIUS ==============
    ('aquarius', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle s'affirme avec une force innovante et directe.

## L'énergie du moment
Mars traverse ta maison I, te donnant une énergie et une combativité amplifiées. Tu es plus assertif(ve), plus direct(e), prêt(e) à agir pour tes idées révolutionnaires.

## Ce que tu pourrais vivre
- Un boost d'énergie personnelle
- L'envie d'agir différemment
- Une affirmation de ton originalité

## Conseils pour ce transit
- Lance-toi dans des projets innovants
- Canalise cette énergie dans l'action
- Affirme ton unicité avec force""",

    ('aquarius', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se mobilise pour des conquêtes financières innovantes.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de prospérité par des moyens originaux. Tu as l'énergie pour développer des sources de revenus innovantes.

## Ce que tu pourrais vivre
- Une motivation pour des revenus originaux
- Des investissements dans l'innovation
- Des conflits sur les valeurs

## Conseils pour ce transit
- Explore des sources de revenus innovantes
- Évite les dépenses technologiques impulsives
- Valorise tes idées originales""",

    ('aquarius', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus percutantes et avant-gardistes.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes échanges plus vifs et tes idées plus provocatrices. Tu as envie de partager tes visions révolutionnaires.

## Ce que tu pourrais vivre
- Des communications provocatrices
- Des débats sur l'avenir
- Une pensée rapide et innovante

## Conseils pour ce transit
- Partage tes idées avant-gardistes
- Évite les conflits pour le plaisir de provoquer
- Canalise dans l'innovation""",

    ('aquarius', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec une volonté de changement.

## L'énergie du moment
Mars active ta maison IV, te poussant à transformer ton espace domestique de façon originale. Modernisation, changements radicaux, ou tensions familiales sur les traditions.

## Ce que tu pourrais vivre
- Des projets de modernisation domestique
- Des tensions sur les changements
- Un besoin de liberté chez toi

## Conseils pour ce transit
- Modernise ton foyer à ta façon
- Gère les résistances au changement
- Crée un espace qui reflète tes idées""",

    ('aquarius', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'expriment de façon unique et audacieuse!

## L'énergie du moment
Mars embrase ta maison V, décuplant ta créativité originale et tes désirs uniques. Les romances sont électriques, les projets créatifs sont avant-gardistes.

## Ce que tu pourrais vivre
- Une créativité révolutionnaire
- Des passions atypiques
- Des expressions artistiques originales

## Conseils pour ce transit
- Crée de façon innovante
- Vis des romances qui te surprennent
- Exprime ton unicité artistique""",

    ('aquarius', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail s'intensifie dans l'innovation.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail orientée vers l'innovation. Tu veux améliorer les méthodes, révolutionner les processus.

## Ce que tu pourrais vivre
- Une productivité innovante
- Des tensions avec les méthodes traditionnelles
- Un besoin d'activités physiques variées

## Conseils pour ce transit
- Propose des améliorations au travail
- Gère les résistances au changement
- Varie tes activités physiques""",

    ('aquarius', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont dynamisées par des idées partagées ou des conflits d'indépendance.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Les partenariats peuvent être dynamisés par des visions communes ou tendus par des besoins de liberté.

## Ce que tu pourrais vivre
- Des partenariats sur des projets innovants
- Des tensions autour de l'indépendance
- Des relations électriques

## Conseils pour ce transit
- Partage des idées avec tes partenaires
- Respecte le besoin de liberté de chacun
- Trouve des partenaires qui innovent avec toi""",

    ('aquarius', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions de transformation et de ressources partagées demandent une approche nouvelle.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant les enjeux de transformation et de finances partagées. Tu cherches des solutions innovantes aux problèmes profonds.

## Ce que tu pourrais vivre
- Des approches nouvelles de l'intimité
- Des solutions innovantes aux questions d'argent
- Une transformation radicale

## Conseils pour ce transit
- Aborde les questions profondes différemment
- Innove dans les finances partagées
- Accepte les transformations révolutionnaires""",

    ('aquarius', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'exploration d'idées nouvelles et d'horizons futuristes t'appelle.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif de connaissances avant-gardistes et d'horizons nouveaux. Voyages vers des lieux innovants, études futuristes, débats sur l'avenir.

## Ce que tu pourrais vivre
- Des voyages vers des lieux innovants
- Des études sur le futur
- Des débats sur la société de demain

## Conseils pour ce transit
- Explore des idées futuristes
- Apprends des technologies nouvelles
- Défends ta vision de l'avenir""",

    ('aquarius', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle vise à révolutionner ton domaine.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour faire avancer ta carrière de façon innovante. C'est le moment de proposer des changements audacieux.

## Ce que tu pourrais vivre
- Une ambition révolutionnaire
- Des initiatives innovantes au travail
- Des conflits avec les méthodes établies

## Conseils pour ce transit
- Propose des innovations professionnelles
- Gère les résistances au changement
- Affirme ta vision originale""",

    ('aquarius', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale explose dans l'action collective pour le changement!

## L'énergie du moment
Mars traverse ta maison XI, ta maison naturelle! C'est une période exceptionnelle pour l'action collective, les projets de groupe et l'engagement pour des causes humanitaires.

## Ce que tu pourrais vivre
- Un leadership dans des mouvements
- Des actions collectives intenses
- Un engagement révolutionnaire

## Conseils pour ce transit
- Mène des projets de changement social
- Coordonne l'énergie collective
- Engage-toi pour l'avenir de l'humanité""",

    ('aquarius', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre travail souterrain et préparation.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. L'énergie peut travailler en coulisses pour préparer de futures révolutions.

## Ce que tu pourrais vivre
- De la frustration face aux obstacles invisibles
- Un travail préparatoire en secret
- Des révélations sur des forces cachées

## Conseils pour ce transit
- Prépare tes futures actions en silence
- Identifie les forces qui te freinent
- Médite sur tes prochaines révolutions""",

    # ============== PISCES ==============
    ('pisces', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle s'affirme avec une force nouvelle et directe.

## L'énergie du moment
Mars traverse ta maison I, te donnant une énergie et une combativité inhabituelles pour toi. Tu es plus assertif(ve), plus direct(e), prêt(e) à agir pour tes rêves.

## Ce que tu pourrais vivre
- Un boost d'énergie et de confiance
- L'envie d'agir pour toi-même
- Une affirmation de tes désirs

## Conseils pour ce transit
- Passe à l'action pour tes rêves
- Équilibre action et sensibilité
- Canalise l'énergie dans la création""",

    ('pisces', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se mobilise pour des conquêtes matérielles guidées par l'intuition.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de sécurité matérielle. Tu as l'énergie pour te battre pour tes ressources, guidé(e) par ton intuition.

## Ce que tu pourrais vivre
- Une motivation financière intuitive
- Des achats guidés par les émotions
- Des conflits sur les valeurs matérielles

## Conseils pour ce transit
- Défends tes intérêts financiers
- Équilibre intuition et réflexion
- Investis dans ce qui nourrit ton âme""",

    ('pisces', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus directes et tes idées plus affirmées.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes échanges plus vifs et tes pensées plus décisives. Tu as envie d'exprimer tes visions avec plus de force.

## Ce que tu pourrais vivre
- Des communications plus directes
- Une pensée plus rapide
- Des frictions possibles avec les proches

## Conseils pour ce transit
- Exprime tes idées avec confiance
- Évite d'être trop brusque
- Utilise cette énergie pour créer""",

    ('pisces', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec une volonté de transformation.

## L'énergie du moment
Mars active ta maison IV, te poussant à agir dans ton espace domestique. Création d'un sanctuaire, nettoyage énergétique, ou tensions familiales émotionnelles.

## Ce que tu pourrais vivre
- Des projets de transformation du foyer
- Des tensions émotionnelles en famille
- Un besoin de protéger ton espace sacré

## Conseils pour ce transit
- Transforme ton foyer en sanctuaire
- Gère les émotions familiales
- Protège ton espace de paix""",

    ('pisces', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'expriment avec une énergie nouvelle et inspirée!

## L'énergie du moment
Mars embrase ta maison V, décuplant ta créativité et tes désirs romantiques. Les romances sont passionnées, les projets créatifs sont intenses et inspirés.

## Ce que tu pourrais vivre
- Une créativité inspirée et active
- Des passions romantiques intenses
- Des expressions artistiques passionnées

## Conseils pour ce transit
- Crée avec passion et inspiration
- Vis tes romances pleinement
- Canalise dans l'art""",

    ('pisces', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail s'intensifie, mais garde ton équilibre.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail accrue. Tu es plus efficace mais tu dois veiller à ne pas t'épuiser. L'exercice doux est essentiel.

## Ce que tu pourrais vivre
- Une productivité augmentée
- Des tensions possibles au travail
- Un besoin de pratiques corporelles douces

## Conseils pour ce transit
- Travaille avec énergie mais conscience
- Évite le surmenage
- Intègre yoga ou natation""",

    ('pisces', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont dynamisées, entre passion et confrontation des sensibilités.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Les couples peuvent vivre des passions intenses ou des confrontations émotionnelles.

## Ce que tu pourrais vivre
- Des relations plus passionnées
- Des confrontations émotionnelles
- Des partenariats actifs

## Conseils pour ce transit
- Exprime tes besoins relationnels
- Transforme la tension en connexion
- Trouve des partenaires qui te dynamisent""",

    ('pisces', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions d'intimité et de transformation demandent une action guidée par l'intuition.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les enjeux de transformation. La sexualité est plus intense, les processus de guérison sont activés.

## Ce que tu pourrais vivre
- Une intimité plus profonde et active
- Des processus de guérison accélérés
- Une transformation spirituelle

## Conseils pour ce transit
- Explore l'intimité avec conscience
- Utilise cette énergie pour guérir
- Accepte les transformations spirituelles""",

    ('pisces', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'exploration spirituelle et les horizons mystiques t'appellent.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif de transcendance et d'horizons spirituels. Voyages initiatiques, études mystiques, quêtes de sens profondes.

## Ce que tu pourrais vivre
- Un voyage spirituel ou pèlerinage
- Des études ésotériques passionnées
- Une quête de sens active

## Conseils pour ce transit
- Explore activement ta spiritualité
- Voyage vers des lieux sacrés
- Cherche des enseignements profonds""",

    ('pisces', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'affirme, guidée par ta vision artistique.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour faire avancer ta carrière. C'est le moment de prendre des initiatives pour tes projets créatifs ou spirituels.

## Ce que tu pourrais vivre
- Une ambition artistique ou spirituelle
- Des initiatives pour ta carrière créative
- Des défis avec le monde matériel

## Conseils pour ce transit
- Affirme ta vision professionnelle
- Agis pour tes projets créatifs
- Équilibre rêve et action concrète""",

    ('pisces', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans l'action pour des causes compassionnelles.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie d'agir pour des causes humanitaires et compassionnelles.

## Ce que tu pourrais vivre
- Un engagement actif pour des causes
- Des tensions possibles dans les groupes
- Une action pour les plus vulnérables

## Conseils pour ce transit
- Mène des projets compassionnels
- Gère les conflits avec empathie
- Engage-toi pour des causes qui touchent ton cœur""",

    ('pisces', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre travail spirituel et batailles de l'âme.

## L'énergie du moment
Mars se retire dans ta maison XII, ta maison naturelle! C'est une période de travail intérieur intense. L'énergie peut être frustrée ou canalisée vers une profonde transformation spirituelle.

## Ce que tu pourrais vivre
- Un travail spirituel intense
- Des combats avec l'inconscient
- Une préparation à une renaissance

## Conseils pour ce transit
- Médite et travaille sur toi-même
- Libère les énergies bloquées
- Prépare ta prochaine renaissance en silence""",
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
        print(f"✅ Transit Mars (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
