#!/usr/bin/env python3
"""Insert transit_mars interpretations for Aries, Taurus, Gemini, Cancer (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MARS_INTERPRETATIONS = {
    # ============== ARIES ==============
    ('aries', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie vitale explose et tu te sens prêt(e) à conquérir le monde!

## L'énergie du moment
Mars, chez lui en Bélier, traverse ta maison I – c'est une configuration de feu pur! Ton énergie physique et ta combativité sont au maximum. Tu dégages une aura de confiance et de détermination qui impressionne. C'est le moment de prendre des initiatives audacieuses.

## Ce que tu pourrais vivre
- Un boost d'énergie et de vitalité
- L'envie de prendre les devants
- Une affirmation de soi puissante

## Conseils pour ce transit
- Lance les projets qui te tiennent à cœur
- Canalise cette énergie dans le sport
- Attention à l'impulsivité excessive""",

    ('aries', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se concentre sur les finances et la conquête de ressources.

## L'énergie du moment
Mars dynamise ta maison II, te poussant à agir pour améliorer ta situation financière. Tu as l'énergie pour te battre pour ce que tu mérites – une augmentation, un nouveau client, une opportunité. Attention cependant aux dépenses impulsives.

## Ce que tu pourrais vivre
- Une motivation forte pour gagner plus
- Des achats impulsifs possibles
- Des conflits autour de l'argent

## Conseils pour ce transit
- Demande ce que tu vaux vraiment
- Réfléchis avant les grosses dépenses
- Investis ton énergie dans tes talents""",

    ('aries', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta communication devient plus directe et percutante.

## L'énergie du moment
Mars enflamme ta maison III, rendant tes mots plus tranchants et tes idées plus affirmées. Tu as envie de défendre tes opinions et de convaincre. Les échanges avec les proches peuvent être vifs. Tes déplacements deviennent plus rapides, parfois imprudents.

## Ce que tu pourrais vivre
- Des débats animés et passionnés
- Des frictions avec frères, sœurs ou voisins
- Une conduite plus rapide/agressive

## Conseils pour ce transit
- Défends tes idées avec diplomatie
- Prudence sur la route
- Utilise cette énergie pour apprendre""",

    ('aries', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer, entre rénovations et tensions familiales.

## L'énergie du moment
Mars active ta maison IV, éveillant l'envie d'agir dans ton espace domestique. Travaux, déménagement, grand ménage – tu as l'énergie pour transformer ton chez-toi. Mais attention aux tensions familiales, les conflits peuvent éclater facilement.

## Ce que tu pourrais vivre
- Des travaux ou rénovations énergiques
- Des tensions avec la famille
- Un besoin de défendre ton territoire

## Conseils pour ce transit
- Canalise l'énergie dans les travaux
- Évite les sujets sensibles en famille
- Protège ton espace personnel""",

    ('aries', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité s'enflamme et tes passions brûlent avec intensité!

## L'énergie du moment
Mars embrase ta maison V, décuplant ta créativité et tes désirs romantiques. C'est une période de passion, d'audace créative et de prise de risques en amour. Si tu as des enfants, les relations peuvent être animées.

## Ce que tu pourrais vivre
- Une créativité explosive
- Des romances passionnées et audacieuses
- Des compétitions sportives ou ludiques

## Conseils pour ce transit
- Crée avec passion et audace
- Vis intensément mais pas imprudemment
- Canalise l'énergie dans le sport ou l'art""",

    ('aries', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail est maximale, mais attention au surmenage.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail impressionnante. Tu peux abattre des montagnes de tâches et tu as peu de patience pour les inefficacités. L'exercice physique devient essentiel pour canaliser cette énergie.

## Ce que tu pourrais vivre
- Une productivité exceptionnelle
- Des conflits avec collègues
- Un risque de surmenage ou blessure

## Conseils pour ce transit
- Travaille efficacement mais repose-toi
- Évite les conflits au bureau
- Fais du sport régulièrement""",

    ('aries', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations de couple et partenariats sont sous haute tension énergétique.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Si ta relation manque d'honnêteté, des conflits peuvent éclater. Mais cette énergie peut aussi raviver la passion ou t'attirer vers des partenaires dynamiques et assertifs.

## Ce que tu pourrais vivre
- Des disputes ou confrontations en couple
- Une passion renouvelée
- Des conflits avec associés ou adversaires

## Conseils pour ce transit
- Exprime tes frustrations calmement
- Transforme la tension en passion
- Négocie avec fermeté mais respect""",

    ('aries', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Désirs profonds et questions de pouvoir sont au cœur de cette période intense.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les questions de ressources partagées. Sexualité, héritages, dettes – tout ce qui est caché ou tabou remonte avec force. C'est un transit de transformation, parfois brutal.

## Ce que tu pourrais vivre
- Une sexualité intensifiée
- Des conflits autour de l'argent partagé
- Une confrontation avec des peurs profondes

## Conseils pour ce transit
- Explore tes désirs avec conscience
- Règle les questions financières en suspens
- Accepte de te transformer""",

    ('aries', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure t'appelle et tu as soif de conquêtes intellectuelles ou géographiques.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif d'exploration et de vérité. Voyages, études, quêtes spirituelles – tu as l'énergie pour repousser tes limites. Attention cependant au fanatisme ou aux conflits d'opinions.

## Ce que tu pourrais vivre
- Un voyage aventureux
- Des débats philosophiques passionnés
- Une quête de sens intense

## Conseils pour ce transit
- Pars à l'aventure si possible
- Défends tes convictions sans fanatisme
- Étudie avec passion""",

    ('aries', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'enflamme et tu vises le sommet!

## L'énergie du moment
Mars dynamise ta maison X, te donnant une énergie combative pour ta carrière. C'est le moment de prendre des initiatives audacieuses, de demander une promotion, de lancer un projet ambitieux. Mais attention aux conflits avec l'autorité.

## Ce que tu pourrais vivre
- Une ambition décuplée
- Des conflits avec supérieurs
- Des avancées professionnelles par l'action

## Conseils pour ce transit
- Prends des initiatives au travail
- Gère les conflits avec diplomatie
- Vise haut mais reste stratégique""",

    ('aries', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie, entre dynamisme de groupe et possibles frictions.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets collectifs. Tu as envie de te battre pour des causes, de dynamiser des groupes, de mener des actions collectives. Mais les conflits avec les amis ou au sein des groupes sont possibles.

## Ce que tu pourrais vivre
- Un leadership dans des groupes
- Des frictions avec des amis
- Un engagement militant actif

## Conseils pour ce transit
- Mène des projets collectifs
- Gère les tensions entre amis
- Engage-toi pour ce qui compte""",

    ('aries', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie travaille en profondeur, entre frustrations cachées et batailles intérieures.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et repos. L'énergie peut être frustrée, tournée vers l'intérieur. C'est un moment pour travailler sur toi-même, affronter tes démons intérieurs et préparer silencieusement tes prochaines batailles.

## Ce que tu pourrais vivre
- De la frustration ou de la fatigue
- Des ennemis cachés qui se manifestent
- Un travail intérieur profond

## Conseils pour ce transit
- Canalise l'énergie dans la méditation
- Identifie et libère tes colères refoulées
- Prépare tes prochaines actions en silence""",

    # ============== TAURUS ==============
    ('taurus', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle s'affirme avec une force nouvelle et directe.

## L'énergie du moment
Mars traverse ta maison I, te donnant une énergie et une détermination inhabituelles pour toi. Tu es plus combatif(ve), plus direct(e), plus impatient(e). C'est le moment d'agir pour toi-même, de prendre des initiatives personnelles.

## Ce que tu pourrais vivre
- Un boost d'énergie physique
- L'envie d'agir immédiatement
- Une affirmation de soi plus forte

## Conseils pour ce transit
- Passe à l'action sur tes projets
- Fais du sport pour canaliser l'énergie
- Attention à ne pas brusquer les autres""",

    ('taurus', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se concentre intensément sur la conquête financière.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de sécurité matérielle de façon combative. Tu as l'énergie pour te battre pour tes revenus, défendre tes intérêts financiers, mais aussi pour dépenser impulsivement.

## Ce que tu pourrais vivre
- Une motivation intense pour gagner
- Des dépenses impulsives
- Des conflits autour des possessions

## Conseils pour ce transit
- Négocie avec force mais sagesse
- Réfléchis avant les achats importants
- Défends tes intérêts financiers""",

    ('taurus', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus directes et énergiques.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes échanges plus vifs et assertifs. Tu as envie de défendre tes idées avec force. Les relations avec les proches peuvent être tendues. Tes déplacements sont plus rapides.

## Ce que tu pourrais vivre
- Des discussions animées
- Des frictions avec l'entourage proche
- Une pensée plus rapide et décisive

## Conseils pour ce transit
- Exprime-toi avec force mais tact
- Prudence dans les déplacements
- Utilise cette énergie pour apprendre""",

    ('taurus', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec force et détermination.

## L'énergie du moment
Mars active ta maison IV, te poussant à agir dans ton espace domestique. Travaux, déménagement, réorganisation – tu as l'énergie pour transformer ton chez-toi. Les tensions familiales peuvent surgir.

## Ce que tu pourrais vivre
- Des travaux ou changements à la maison
- Des conflits avec la famille
- Un besoin de protéger ton territoire

## Conseils pour ce transit
- Canalise l'énergie dans l'amélioration du foyer
- Gère les tensions familiales avec calme
- Défends ton espace personnel""",

    ('taurus', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'enflamment avec une énergie débordante!

## L'énergie du moment
Mars embrase ta maison V, décuplant ta créativité et tes désirs. Les romances sont passionnées, les activités créatives sont intenses. Si tu as des enfants, les interactions sont dynamiques.

## Ce que tu pourrais vivre
- Une créativité puissante
- Des passions amoureuses intenses
- Des compétitions ou jeux animés

## Conseils pour ce transit
- Crée avec passion
- Vis tes romances intensément
- Canalise l'énergie dans des activités physiques""",

    ('taurus', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie professionnelle est au maximum, attention au surmenage.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail impressionnante. Tu peux accomplir énormément mais tu risques de t'épuiser. Les relations avec les collègues peuvent être tendues.

## Ce que tu pourrais vivre
- Une productivité exceptionnelle
- Des tensions au travail
- Un besoin d'activité physique intense

## Conseils pour ce transit
- Travaille efficacement mais repose-toi
- Évite les conflits professionnels
- Intègre le sport dans ta routine""",

    ('taurus', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont sous tension, entre passion et confrontation.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant toutes tes relations importantes. Les conflits de couple peuvent éclater, mais cette énergie peut aussi raviver la passion. Les partenariats sont dynamiques.

## Ce que tu pourrais vivre
- Des disputes ou confrontations
- Une passion renouvelée
- Des négociations intenses

## Conseils pour ce transit
- Communique tes frustrations calmement
- Transforme la tension en passion
- Défends tes intérêts avec respect""",

    ('taurus', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions de pouvoir et d'intimité sont au cœur de cette période intense.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les questions de ressources partagées. La sexualité est plus intense, les questions financières plus pressantes.

## Ce que tu pourrais vivre
- Une sexualité intensifiée
- Des conflits autour des finances partagées
- Une transformation profonde

## Conseils pour ce transit
- Explore l'intimité avec conscience
- Règle les questions d'argent en suspens
- Accepte les transformations nécessaires""",

    ('taurus', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure et l'expansion t'appellent avec force.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif d'horizons nouveaux. Voyages, études, quêtes de sens – tu as l'énergie pour repousser tes limites. Attention aux conflits d'opinions.

## Ce que tu pourrais vivre
- Un voyage énergique
- Des débats passionnés
- Une quête spirituelle active

## Conseils pour ce transit
- Explore de nouveaux horizons
- Défends tes convictions avec ouverture
- Apprends activement""",

    ('taurus', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'enflamme avec détermination.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour gravir les échelons. C'est le moment de prendre des initiatives de carrière audacieuses. Attention aux conflits avec l'autorité.

## Ce que tu pourrais vivre
- Une ambition décuplée
- Des avancées professionnelles
- Des tensions avec la hiérarchie

## Conseils pour ce transit
- Prends des initiatives de carrière
- Gère les conflits avec diplomatie
- Vise tes objectifs avec détermination""",

    ('taurus', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie avec dynamisme et possibles frictions.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie d'agir collectivement, de mener des causes. Les tensions avec les amis sont possibles.

## Ce que tu pourrais vivre
- Un dynamisme dans les groupes
- Des conflits avec des amis
- Un engagement actif pour des causes

## Conseils pour ce transit
- Mène des projets collectifs
- Gère les tensions amicales
- Engage-toi avec passion""",

    ('taurus', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie travaille en profondeur, entre repos forcé et batailles intérieures.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. L'énergie peut être frustrée ou tournée vers l'intérieur. C'est un moment pour le travail intérieur.

## Ce que tu pourrais vivre
- De la fatigue ou frustration
- Des ennemis cachés qui se révèlent
- Un travail sur soi profond

## Conseils pour ce transit
- Repose-toi suffisamment
- Libère tes colères refoulées
- Prépare tes prochaines actions en silence""",

    # ============== GEMINI ==============
    ('gemini', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle explose et tu es prêt(e) pour l'action!

## L'énergie du moment
Mars traverse ta maison I, te donnant une énergie et une combativité décuplées. Tu es plus direct(e), plus impatient(e), plus audacieux(se). C'est le moment de te lancer dans ce que tu repousses depuis longtemps.

## Ce que tu pourrais vivre
- Un boost d'énergie vitale
- L'envie d'agir sans attendre
- Une affirmation de soi puissante

## Conseils pour ce transit
- Lance-toi dans l'action
- Canalise l'énergie dans le mouvement
- Attention à l'impatience""",

    ('gemini', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se mobilise pour des conquêtes financières.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de gagner et de posséder. Tu as l'énergie pour te battre pour tes intérêts financiers. Attention aux dépenses impulsives.

## Ce que tu pourrais vivre
- Une motivation pour gagner plus
- Des achats impulsifs
- Des tensions autour de l'argent

## Conseils pour ce transit
- Défends tes intérêts financiers
- Réfléchis avant de dépenser
- Valorise tes compétences""",

    ('gemini', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications s'enflamment et tes idées s'affirment avec force!

## L'énergie du moment
Mars enflamme ta maison III, ta maison naturelle! Tes mots sont plus percutants, tes idées plus affirmées. Tu as envie de convaincre, de débattre, d'apprendre vite. Les échanges avec les proches peuvent être électriques.

## Ce que tu pourrais vivre
- Des communications passionnées
- Des apprentissages rapides
- Des frictions avec l'entourage proche

## Conseils pour ce transit
- Utilise cette énergie communicative
- Prudence dans les débats
- Canalise dans l'écriture ou l'étude""",

    ('gemini', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer avec intensité.

## L'énergie du moment
Mars active ta maison IV, te poussant à agir dans ton espace domestique. Travaux, réorganisation, ou tensions familiales – ton chez-toi devient le centre de ton énergie.

## Ce que tu pourrais vivre
- Des travaux ou changements domestiques
- Des tensions familiales
- Un besoin de défendre ton espace

## Conseils pour ce transit
- Transforme ton chez-toi positivement
- Gère les conflits familiaux calmement
- Protège ton territoire""",

    ('gemini', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'enflamment avec intensité!

## L'énergie du moment
Mars embrase ta maison V, décuplant ta créativité et tes désirs. Les romances sont passionnées, les projets créatifs sont intenses. Le jeu et la compétition t'attirent.

## Ce que tu pourrais vivre
- Une créativité explosive
- Des passions amoureuses intenses
- Des activités ludiques compétitives

## Conseils pour ce transit
- Crée avec audace
- Vis tes passions pleinement
- Canalise dans le sport ou l'art""",

    ('gemini', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail est maximale, garde le cap sans t'épuiser.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail impressionnante. Tu es efficace mais impatient(e). L'exercice physique est essentiel.

## Ce que tu pourrais vivre
- Une productivité exceptionnelle
- Des tensions avec collègues
- Un besoin de mouvement physique

## Conseils pour ce transit
- Travaille efficacement
- Évite les conflits au travail
- Intègre l'exercice quotidien""",

    ('gemini', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations sont dynamisées, entre passion et confrontation possible.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Les couples peuvent vivre des tensions ou une passion renouvelée. Les partenariats sont actifs.

## Ce que tu pourrais vivre
- Des confrontations en couple
- Une passion ravivée
- Des négociations intenses

## Conseils pour ce transit
- Exprime tes besoins clairement
- Transforme la tension en connexion
- Défends tes intérêts avec respect""",

    ('gemini', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions d'intimité et de pouvoir sont au premier plan.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les enjeux de pouvoir. La sexualité, les finances partagées, les transformations profondes sont au cœur de cette période.

## Ce que tu pourrais vivre
- Une sexualité plus intense
- Des questions financières urgentes
- Une transformation profonde

## Conseils pour ce transit
- Explore l'intimité consciemment
- Règle les questions d'argent partagé
- Accepte de te transformer""",

    ('gemini', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure et l'expansion intellectuelle t'appellent avec force.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif d'exploration. Voyages, études, débats philosophiques – tu as l'énergie pour élargir tes horizons.

## Ce que tu pourrais vivre
- Un voyage stimulant
- Des débats passionnés
- Une quête de sens active

## Conseils pour ce transit
- Pars à l'aventure
- Apprends avec passion
- Défends tes idées avec ouverture""",

    ('gemini', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'enflamme avec détermination.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour avancer dans ta carrière. C'est le moment de prendre des initiatives, de viser plus haut. Attention aux conflits hiérarchiques.

## Ce que tu pourrais vivre
- Une ambition forte
- Des avancées de carrière
- Des tensions avec l'autorité

## Conseils pour ce transit
- Prends des initiatives audacieuses
- Gère les conflits avec tact
- Vise tes objectifs avec détermination""",

    ('gemini', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans l'action collective.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie de mener, d'agir pour des causes, de dynamiser ton réseau.

## Ce que tu pourrais vivre
- Un leadership dans des groupes
- Des tensions avec des amis
- Un engagement militant

## Conseils pour ce transit
- Mène des projets collectifs
- Gère les frictions amicales
- Engage-toi pour tes valeurs""",

    ('gemini', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre repos et combats internes.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. L'énergie peut être frustrée ou canalisée vers le travail intérieur.

## Ce que tu pourrais vivre
- De la fatigue ou frustration cachée
- Des ennemis cachés qui se manifestent
- Un travail spirituel profond

## Conseils pour ce transit
- Repose-toi suffisamment
- Libère tes frustrations en douceur
- Prépare silencieusement tes prochaines actions""",

    # ============== CANCER ==============
    ('cancer', 1): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie personnelle s'affirme avec une force nouvelle et directe.

## L'énergie du moment
Mars traverse ta maison I, te donnant une énergie combative inhabituelle. Tu es plus assertif(ve), plus direct(e), prêt(e) à agir. C'est le moment de prendre des initiatives pour toi-même.

## Ce que tu pourrais vivre
- Un boost d'énergie vitale
- L'envie d'agir pour toi
- Une affirmation de soi plus forte

## Conseils pour ce transit
- Passe à l'action
- Canalise l'énergie dans le sport
- Affirme-toi sans agressivité""",

    ('cancer', 2): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie se concentre sur la sécurité financière avec détermination.

## L'énergie du moment
Mars enflamme ta maison II, stimulant ton désir de sécurité matérielle. Tu as l'énergie pour te battre pour tes revenus et tes possessions. Attention aux dépenses impulsives.

## Ce que tu pourrais vivre
- Une motivation financière forte
- Des achats impulsifs possibles
- Des tensions autour des ressources

## Conseils pour ce transit
- Défends tes intérêts financiers
- Évite les dépenses impulsives
- Valorise tes talents""",

    ('cancer', 3): """# ♂ Transit de Mars en Bélier

**En une phrase :** Tes communications deviennent plus directes et affirmées.

## L'énergie du moment
Mars dynamise ta maison III, rendant tes échanges plus vifs et directs. Tu as envie de défendre tes idées, de convaincre. Les relations avec les proches peuvent être animées.

## Ce que tu pourrais vivre
- Des discussions passionnées
- Des frictions avec l'entourage proche
- Une pensée plus rapide

## Conseils pour ce transit
- Exprime-toi clairement
- Prudence dans les débats sensibles
- Utilise cette énergie pour apprendre""",

    ('cancer', 4): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se concentre sur ton foyer et tes racines avec intensité!

## L'énergie du moment
Mars active ta maison IV, ta maison naturelle! Tu as une énergie puissante pour transformer ton chez-toi – travaux, déménagement, réorganisation. Mais les tensions familiales peuvent être vives.

## Ce que tu pourrais vivre
- Des travaux domestiques intenses
- Des conflits familiaux possibles
- Un besoin fort de protéger ton territoire

## Conseils pour ce transit
- Canalise l'énergie dans l'amélioration du foyer
- Gère les tensions familiales avec douceur
- Protège ton espace personnel""",

    ('cancer', 5): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ta créativité et tes passions s'enflamment avec une énergie nouvelle!

## L'énergie du moment
Mars embrase ta maison V, décuplant ta créativité et tes désirs romantiques. Les romances sont passionnées, les projets créatifs sont dynamiques. Les moments avec les enfants sont animés.

## Ce que tu pourrais vivre
- Une créativité intense
- Des passions amoureuses vives
- Des activités ludiques énergiques

## Conseils pour ce transit
- Crée avec passion
- Vis tes romances intensément
- Canalise dans des activités physiques""",

    ('cancer', 6): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie au travail est maximale, mais reste vigilant(e) à ton bien-être.

## L'énergie du moment
Mars dynamise ta maison VI, te donnant une capacité de travail impressionnante. Tu es productif(ve) mais impatient(e). L'exercice physique est essentiel pour ton équilibre.

## Ce que tu pourrais vivre
- Une productivité exceptionnelle
- Des tensions professionnelles possibles
- Un besoin d'activité physique

## Conseils pour ce transit
- Travaille efficacement
- Évite le surmenage
- Intègre l'exercice régulier""",

    ('cancer', 7): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les relations de couple sont sous haute tension, entre passion et confrontation.

## L'énergie du moment
Mars traverse ta maison VII, intensifiant les dynamiques relationnelles. Les conflits peuvent éclater mais cette énergie peut aussi raviver la passion. Les partenariats sont actifs.

## Ce que tu pourrais vivre
- Des confrontations en couple
- Une passion renouvelée
- Des négociations intenses

## Conseils pour ce transit
- Exprime tes besoins calmement
- Transforme la tension en connexion
- Défends tes intérêts avec respect""",

    ('cancer', 8): """# ♂ Transit de Mars en Bélier

**En une phrase :** Les questions d'intimité et de pouvoir sont au premier plan.

## L'énergie du moment
Mars plonge dans ta maison VIII, intensifiant ta vie intime et les enjeux de ressources partagées. La sexualité, les finances communes, les transformations profondes sont activées.

## Ce que tu pourrais vivre
- Une sexualité plus intense
- Des questions financières à régler
- Une transformation profonde

## Conseils pour ce transit
- Explore l'intimité avec conscience
- Règle les questions d'argent partagé
- Accepte les transformations""",

    ('cancer', 9): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'aventure et l'expansion t'appellent avec une force nouvelle.

## L'énergie du moment
Mars enflamme ta maison IX, éveillant ta soif d'horizons nouveaux. Voyages, études, quêtes de sens – tu as l'énergie pour élargir ta vision du monde.

## Ce que tu pourrais vivre
- Un voyage aventureux
- Des débats philosophiques
- Une quête spirituelle active

## Conseils pour ce transit
- Explore de nouveaux horizons
- Apprends avec passion
- Défends tes convictions""",

    ('cancer', 10): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton ambition professionnelle s'enflamme avec détermination.

## L'énergie du moment
Mars dynamise ta maison X, te donnant l'énergie pour avancer dans ta carrière. C'est le moment de prendre des initiatives audacieuses. Attention aux conflits avec l'autorité.

## Ce que tu pourrais vivre
- Une ambition forte
- Des avancées professionnelles
- Des tensions hiérarchiques

## Conseils pour ce transit
- Prends des initiatives
- Gère les conflits avec tact
- Vise tes objectifs""",

    ('cancer', 11): """# ♂ Transit de Mars en Bélier

**En une phrase :** Ton énergie sociale s'intensifie dans l'action collective.

## L'énergie du moment
Mars traverse ta maison XI, énergisant ta vie sociale et tes projets de groupe. Tu as envie d'agir pour des causes qui te tiennent à cœur.

## Ce que tu pourrais vivre
- Un dynamisme dans les groupes
- Des tensions avec des amis
- Un engagement pour des causes

## Conseils pour ce transit
- Mène des projets collectifs
- Gère les frictions amicales
- Engage-toi avec cœur""",

    ('cancer', 12): """# ♂ Transit de Mars en Bélier

**En une phrase :** L'énergie se tourne vers l'intérieur, entre repos et travail sur soi.

## L'énergie du moment
Mars se retire dans ta maison XII, créant une tension entre action et retrait. L'énergie peut être frustrée ou canalisée vers un profond travail intérieur.

## Ce que tu pourrais vivre
- De la fatigue ou frustration
- Des défis cachés à affronter
- Un travail spirituel profond

## Conseils pour ce transit
- Repose-toi suffisamment
- Libère tes émotions refoulées
- Prépare silencieusement l'avenir""",
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
        print(f"✅ Transit Mars (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
