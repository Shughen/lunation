#!/usr/bin/env python3
"""Insert transit_saturn interpretations for Leo, Virgo, Libra, Scorpio (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SATURN_INTERPRETATIONS = {
    # ============== LEO ==============
    ('leo', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité royale – construis avec humilité.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es avec maturité. Ton ego est testé, mais c'est l'occasion de construire une confiance plus authentique et durable.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles
- Un besoin de maturité et d'humilité

## Conseils pour ce transit
- Construis une confiance solide
- Assume tes responsabilités
- Tempère ton ego avec sagesse""",

    ('leo', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances et valeurs sont restructurées avec rigueur.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière durable. Les dépenses de prestige sont questionnées.

## Ce que tu pourrais vivre
- Des restrictions financières possibles
- Un besoin de budgéter sérieusement
- Une réévaluation de tes valeurs

## Conseils pour ce transit
- Construis une stabilité durable
- Reconnais ta vraie valeur
- Économise avec sagesse""",

    ('leo', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient plus mesurée et structurée.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée et ta communication avec plus de profondeur.

## Ce que tu pourrais vivre
- Une communication plus réfléchie
- Des apprentissages exigeants
- Des responsabilités intellectuelles

## Conseils pour ce transit
- Apprends des choses durables
- Communique avec précision
- Pèse tes mots""",

    ('leo', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent structure et responsabilité.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider tes fondations domestiques avec maturité.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin de sécuriser le foyer
- Un travail sur les racines

## Conseils pour ce transit
- Consolide tes fondations
- Assume tes responsabilités familiales
- Travaille sur ton histoire""",

    ('leo', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement et discipline.

## L'énergie du moment
Saturne traverse ta maison V, ta maison naturelle! C'est le temps de prendre au sérieux l'amour et la créativité, de construire plutôt que de papillonner.

## Ce que tu pourrais vivre
- Un besoin d'amour mature et engagé
- Des projets créatifs exigeants
- Des responsabilités parentales

## Conseils pour ce transit
- Engage-toi sérieusement en amour
- Discipline ta créativité
- Assume tes responsabilités de cœur""",

    ('leo', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline et structure.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à restructurer ton quotidien professionnel et tes habitudes de santé.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline quotidienne
- Une attention à la santé

## Conseils pour ce transit
- Structure ton quotidien
- Prends ta santé au sérieux
- Travaille avec rigueur""",

    ('leo', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées et demandent maturité.

## L'énergie du moment
Saturne traverse ta maison VII, testant la solidité de tes relations. Les partenariats superficiels sont remis en question.

## Ce que tu pourrais vivre
- Des tests dans les relations
- Un engagement sérieux ou une fin
- Des responsabilités relationnelles

## Conseils pour ce transit
- Engage-toi avec maturité
- Travaille sur tes relations
- Assume tes responsabilités""",

    ('leo', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et ressources partagées demandent prudence.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer avec sagesse les ressources partagées et à accepter les transformations nécessaires.

## Ce que tu pourrais vivre
- Des responsabilités financières partagées
- Une transformation lente mais profonde
- Un travail sur le contrôle

## Conseils pour ce transit
- Gère les finances avec rigueur
- Accepte la transformation
- Travaille sur tes peurs""",

    ('leo', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde est restructurée avec sagesse.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à revoir tes croyances avec maturité et réalisme.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études ou voyages avec un but
- Un besoin de sens concret

## Conseils pour ce transit
- Construis une philosophie solide
- Étudie avec discipline
- Voyage avec intention""",

    ('leo', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande efforts et responsabilité – construis ta réputation.

## L'énergie du moment
Saturne traverse ta maison X avec son énergie naturelle. C'est une période cruciale pour ta carrière et ta réputation.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles majeures
- Un test de ta position sociale
- Des avancées lentes mais solides

## Conseils pour ce transit
- Construis ta réputation avec patience
- Assume tes responsabilités
- Vise des objectifs durables""",

    ('leo', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets d'avenir sont évalués.

## L'énergie du moment
Saturne traverse ta maison XI, testant la qualité de tes amitiés et la solidité de tes projets.

## Ce que tu pourrais vivre
- Une évaluation de tes amitiés
- Des responsabilités dans les groupes
- Un réalisme sur l'avenir

## Conseils pour ce transit
- Garde les amitiés sincères
- Sois réaliste sur tes objectifs
- Assume des responsabilités collectives""",

    ('leo', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur et de dissolution des vieilles structures de l'ego.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur profond sur ton ego et tes peurs cachées.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation à des peurs d'ego
- Un besoin de solitude constructive

## Conseils pour ce transit
- Affronte tes peurs avec humilité
- Utilise la solitude pour grandir
- Prépare le prochain cycle""",

    # ============== VIRGO ==============
    ('virgo', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité avec rigueur et méthode.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es avec encore plus de rigueur et d'auto-discipline.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles accrues
- Un perfectionnisme testé

## Conseils pour ce transit
- Construis une version solide de toi
- Assume tes responsabilités
- Évite l'auto-critique excessive""",

    ('virgo', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances et valeurs sont restructurées avec méthode.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière avec ta rigueur naturelle.

## Ce que tu pourrais vivre
- Des restrictions financières possibles
- Un besoin de budgéter avec précision
- Une réévaluation de tes compétences

## Conseils pour ce transit
- Construis une stabilité méthodique
- Reconnais ta vraie valeur
- Économise avec stratégie""",

    ('virgo', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication et tes apprentissages deviennent très structurés.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée et ta communication avec encore plus de précision.

## Ce que tu pourrais vivre
- Une communication très structurée
- Des apprentissages exigeants
- Des responsabilités intellectuelles

## Conseils pour ce transit
- Apprends des choses concrètes
- Communique avec précision
- Évite l'excès de critique""",

    ('virgo', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent organisation et responsabilité.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider tes fondations avec méthode.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin d'organiser le foyer
- Un travail sur les racines

## Conseils pour ce transit
- Organise tes fondations
- Assume tes responsabilités familiales
- Travaille sur ton histoire""",

    ('virgo', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement et discipline.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux l'amour et la créativité, domaines où tu peux être timide.

## Ce que tu pourrais vivre
- Un besoin d'amour mature
- Des projets créatifs exigeants
- Des responsabilités parentales

## Conseils pour ce transit
- Engage-toi sérieusement en amour
- Discipline ta créativité
- Ose t'exprimer""",

    ('virgo', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé sont restructurés – ton domaine naturel!

## L'énergie du moment
Saturne traverse ta maison VI, ta maison naturelle! C'est une période importante pour restructurer ton travail et tes habitudes de santé avec encore plus de rigueur.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles majeures
- Un besoin de discipline quotidienne parfaite
- Une attention accrue à la santé

## Conseils pour ce transit
- Excelle dans ton travail
- Structure ta santé avec méthode
- Évite le perfectionnisme excessif""",

    ('virgo', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées et demandent engagement.

## L'énergie du moment
Saturne traverse ta maison VII, testant la solidité de tes relations avec des critères exigeants.

## Ce que tu pourrais vivre
- Des tests dans les relations
- Un engagement sérieux ou une réévaluation
- Des responsabilités relationnelles

## Conseils pour ce transit
- Engage-toi avec discernement
- Travaille sur tes relations
- Évite la critique excessive du partenaire""",

    ('virgo', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et ressources partagées demandent analyse et prudence.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à analyser et gérer avec sagesse les ressources partagées.

## Ce que tu pourrais vivre
- Des responsabilités financières partagées
- Une transformation méthodique
- Un travail sur les peurs

## Conseils pour ce transit
- Analyse les finances avec rigueur
- Accepte la transformation
- Travaille sur tes anxiétés""",

    ('virgo', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde est restructurée avec réalisme.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à revoir tes croyances avec analyse et réalisme.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études ou voyages méthodiques
- Un besoin de sens pratique

## Conseils pour ce transit
- Construis une philosophie réaliste
- Étudie avec discipline
- Voyage avec un but""",

    ('virgo', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande efforts et responsabilité – excelle avec rigueur.

## L'énergie du moment
Saturne traverse ta maison X, c'est une période cruciale pour ta carrière où ton perfectionnisme est mis à l'épreuve.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles majeures
- Un test de tes compétences
- Des avancées par l'excellence

## Conseils pour ce transit
- Construis ta réputation par la qualité
- Assume tes responsabilités
- Vise l'excellence durable""",

    ('virgo', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets d'avenir sont évalués avec discernement.

## L'énergie du moment
Saturne traverse ta maison XI, testant la qualité de tes amitiés avec des critères exigeants.

## Ce que tu pourrais vivre
- Une évaluation des amitiés
- Des responsabilités dans les groupes
- Un réalisme sur l'avenir

## Conseils pour ce transit
- Garde les amitiés de qualité
- Sois réaliste sur tes objectifs
- Contribue méthodiquement aux groupes""",

    ('virgo', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur et de confrontation aux anxiétés.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sur tes anxiétés et tes peurs cachées.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation à des anxiétés
- Un besoin de solitude productive

## Conseils pour ce transit
- Affronte tes anxiétés
- Utilise la solitude pour t'analyser
- Prépare le prochain cycle""",

    # ============== LIBRA ==============
    ('libra', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité – apprends à t'affirmer seul(e).

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es indépendamment des autres. C'est le temps de construire une identité autonome.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles
- Un besoin d'autonomie

## Conseils pour ce transit
- Construis ton indépendance
- Assume tes responsabilités personnelles
- Apprends à décider seul(e)""",

    ('libra', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances et valeurs sont restructurées.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir ta propre sécurité financière sans dépendre des autres.

## Ce que tu pourrais vivre
- Des restrictions financières possibles
- Un besoin de budgéter
- Une réévaluation de tes valeurs

## Conseils pour ce transit
- Construis ton autonomie financière
- Reconnais ta propre valeur
- Économise sagement""",

    ('libra', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient plus affirmée et structurée.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée et affirmer tes idées.

## Ce que tu pourrais vivre
- Une communication plus affirmée
- Des apprentissages exigeants
- Des responsabilités de communication

## Conseils pour ce transit
- Exprime tes idées avec assurance
- Apprends des choses durables
- Affirme tes opinions""",

    ('libra', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer demande structure et décisions personnelles.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider tes fondations en prenant des décisions personnelles.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin de créer ton propre foyer
- Un travail sur l'autonomie émotionnelle

## Conseils pour ce transit
- Consolide tes fondations
- Assume tes choix domestiques
- Crée ta sécurité intérieure""",

    ('libra', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement personnel.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux tes propres désirs créatifs et amoureux.

## Ce que tu pourrais vivre
- Un besoin d'amour mature
- Des projets créatifs personnels
- Des responsabilités

## Conseils pour ce transit
- Affirme tes désirs amoureux
- Discipline ta créativité personnelle
- Assume tes choix de cœur""",

    ('libra', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline personnelle.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à restructurer ton quotidien avec discipline.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline personnelle
- Une attention à ta santé

## Conseils pour ce transit
- Structure ton quotidien
- Prends soin de toi
- Travaille avec rigueur""",

    ('libra', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont profondément testées – période cruciale!

## L'énergie du moment
Saturne traverse ta maison VII, ta maison naturelle mais dans le signe opposé! C'est un test majeur pour toutes tes relations et partenariats.

## Ce que tu pourrais vivre
- Des tests majeurs dans les relations
- Un engagement sérieux ou une séparation
- Des responsabilités relationnelles lourdes

## Conseils pour ce transit
- Engage-toi avec maturité totale
- Réévalue tes relations
- Apprends l'équilibre entre soi et l'autre""",

    ('libra', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et ressources partagées demandent autonomie.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer les ressources partagées avec plus d'autonomie.

## Ce que tu pourrais vivre
- Des responsabilités financières
- Une transformation de la dépendance
- Un travail sur le contrôle

## Conseils pour ce transit
- Gère tes finances avec autonomie
- Accepte la transformation
- Travaille sur l'interdépendance saine""",

    ('libra', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde est restructurée avec tes propres critères.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à forger tes propres croyances et convictions.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études avec un but personnel
- Un besoin de ta propre vérité

## Conseils pour ce transit
- Construis ta propre philosophie
- Étudie ce qui t'intéresse vraiment
- Affirme tes convictions""",

    ('libra', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande affirmation et responsabilité personnelle.

## L'énergie du moment
Saturne traverse ta maison X, c'est une période cruciale pour affirmer ta carrière par tes propres moyens.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un test de ton ambition personnelle
- Des avancées par l'initiative

## Conseils pour ce transit
- Construis ta réputation personnelle
- Assume tes responsabilités
- Affirme tes objectifs de carrière""",

    ('libra', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets sont évalués – garde ton indépendance.

## L'énergie du moment
Saturne traverse ta maison XI, testant tes amitiés et ton indépendance au sein des groupes.

## Ce que tu pourrais vivre
- Une évaluation des amitiés
- Des responsabilités de groupe
- Un besoin d'indépendance sociale

## Conseils pour ce transit
- Garde les amitiés authentiques
- Reste toi-même dans les groupes
- Assume des responsabilités tout en restant autonome""",

    ('libra', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur sur la codépendance et les peurs.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sur tes dépendances et tes peurs de l'abandon.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient relationnel
- La confrontation à des peurs de solitude
- Un besoin de temps seul(e)

## Conseils pour ce transit
- Affronte tes peurs de solitude
- Utilise le temps seul(e) pour grandir
- Prépare une nouvelle autonomie""",

    # ============== SCORPIO ==============
    ('scorpio', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité avec discipline et contrôle.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es avec maturité. Ton pouvoir personnel est testé et restructuré.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles
- Un travail sur le contrôle

## Conseils pour ce transit
- Construis une identité solide
- Assume tes responsabilités
- Maîtrise ton pouvoir""",

    ('scorpio', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances et valeurs sont restructurées avec rigueur.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière avec ta profondeur habituelle.

## Ce que tu pourrais vivre
- Des restrictions financières possibles
- Un besoin de contrôler les finances
- Une réévaluation des valeurs

## Conseils pour ce transit
- Construis une stabilité stratégique
- Reconnais ta vraie valeur
- Économise avec prévoyance""",

    ('scorpio', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient plus stratégique et structurée.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée et ta communication avec encore plus de précision.

## Ce que tu pourrais vivre
- Une communication plus calculée
- Des apprentissages profonds
- Des responsabilités intellectuelles

## Conseils pour ce transit
- Apprends des choses stratégiques
- Communique avec impact
- Structure tes idées""",

    ('scorpio', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent transformation et responsabilité.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider et transformer tes fondations familiales.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin de sécuriser le foyer
- Un travail sur les secrets familiaux

## Conseils pour ce transit
- Consolide tes fondations
- Assume tes responsabilités familiales
- Guéris les blessures familiales""",

    ('scorpio', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement profond.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux l'amour et la créativité avec ton intensité naturelle.

## Ce que tu pourrais vivre
- Un besoin d'amour engagé et profond
- Des projets créatifs intenses
- Des responsabilités

## Conseils pour ce transit
- Engage-toi totalement en amour
- Discipline ta créativité
- Assume tes passions""",

    ('scorpio', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline et transformation.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à restructurer ton quotidien avec rigueur et transformation.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline intense
- Une transformation des habitudes de santé

## Conseils pour ce transit
- Structure ton quotidien
- Transforme ta santé
- Travaille avec intensité""",

    ('scorpio', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées et transformées.

## L'énergie du moment
Saturne traverse ta maison VII, testant la solidité de tes relations avec une intensité transformatrice.

## Ce que tu pourrais vivre
- Des tests profonds dans les relations
- Un engagement transformateur ou une fin
- Des responsabilités relationnelles

## Conseils pour ce transit
- Engage-toi avec profondeur
- Transforme tes relations
- Assume les responsabilités""",

    ('scorpio', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et ressources partagées – ton domaine restructuré!

## L'énergie du moment
Saturne traverse ta maison VIII, ta maison naturelle! C'est une période majeure de restructuration de ta relation au pouvoir, à l'intimité et aux ressources partagées.

## Ce que tu pourrais vivre
- Des responsabilités financières importantes
- Une transformation profonde mais contrôlée
- Un travail majeur sur le pouvoir

## Conseils pour ce transit
- Gère le pouvoir avec sagesse
- Accepte la transformation contrôlée
- Travaille sur tes peurs de vulnérabilité""",

    ('scorpio', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde est restructurée avec profondeur.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à revoir tes croyances profondes avec maturité.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études ésotériques ou profondes
- Un besoin de vérité absolue

## Conseils pour ce transit
- Construis une philosophie profonde
- Étudie les mystères avec discipline
- Voyage vers la transformation""",

    ('scorpio', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande pouvoir et responsabilité – construis ton influence.

## L'énergie du moment
Saturne traverse ta maison X, c'est une période cruciale pour construire ta position de pouvoir et d'influence.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles majeures
- Un test de ton pouvoir
- Des avancées stratégiques

## Conseils pour ce transit
- Construis ton influence avec patience
- Assume tes responsabilités de pouvoir
- Vise le contrôle durable""",

    ('scorpio', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets sont évalués avec intensité.

## L'énergie du moment
Saturne traverse ta maison XI, testant la profondeur de tes amitiés et tes projets transformateurs.

## Ce que tu pourrais vivre
- Une évaluation des loyautés
- Des responsabilités dans les groupes
- Un réalisme sur les projets

## Conseils pour ce transit
- Garde les amitiés loyales
- Sois réaliste mais déterminé
- Transforme tes groupes""",

    ('scorpio', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur profond sur le pouvoir et le contrôle.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sur tes peurs de perte de contrôle et tes ombres.

## Ce que tu pourrais vivre
- Un travail sur l'ombre
- La confrontation aux peurs de pouvoir
- Un besoin de solitude transformatrice

## Conseils pour ce transit
- Affronte ton ombre
- Utilise la solitude pour te régénérer
- Prépare ta renaissance""",
}

async def insert_interpretations():
    """Insert transit Saturn interpretations into database."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_SATURN_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_saturn',
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
                subject='transit_saturn',
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
        print(f"✅ Transit Saturn (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
