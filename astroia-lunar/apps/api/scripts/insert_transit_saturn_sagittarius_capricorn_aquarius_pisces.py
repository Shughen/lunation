#!/usr/bin/env python3
"""Insert transit_saturn interpretations for Sagittarius, Capricorn, Aquarius, Pisces (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SATURN_INTERPRETATIONS = {
    # ============== SAGITTARIUS ==============
    ('sagittarius', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité aventurière – apprends la discipline.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es avec maturité. Ton optimisme naturel est tempéré par le réalisme.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles
- Un besoin de discipline

## Conseils pour ce transit
- Construis une confiance mature
- Assume tes responsabilités
- Tempère l'optimisme avec le réalisme""",

    ('sagittarius', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances et valeurs sont restructurées avec réalisme.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière au lieu de tout risquer.

## Ce que tu pourrais vivre
- Des restrictions financières possibles
- Un besoin de budgéter
- Une réévaluation des valeurs

## Conseils pour ce transit
- Construis une stabilité concrète
- Évite les risques excessifs
- Économise sagement""",

    ('sagittarius', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient plus structurée et concrète.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée et communiquer avec plus de précision.

## Ce que tu pourrais vivre
- Une communication plus concrète
- Des apprentissages exigeants
- Des responsabilités intellectuelles

## Conseils pour ce transit
- Apprends des choses pratiques
- Communique avec précision
- Structure tes idées""",

    ('sagittarius', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent ancrage et responsabilité.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à t'ancrer et consolider tes fondations au lieu de toujours courir.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin de s'ancrer
- Un travail sur les racines

## Conseils pour ce transit
- Pose-toi et consolide
- Assume tes responsabilités familiales
- Crée un vrai foyer""",

    ('sagittarius', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement au lieu de papillonnage.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux l'amour et la créativité au lieu de multiplier les aventures.

## Ce que tu pourrais vivre
- Un besoin d'amour engagé
- Des projets créatifs exigeants
- Des responsabilités

## Conseils pour ce transit
- Engage-toi vraiment en amour
- Discipline ta créativité
- Profondis au lieu de survoler""",

    ('sagittarius', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline et routine.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à accepter la routine et la discipline quotidienne.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline quotidienne
- Une attention à la santé

## Conseils pour ce transit
- Accepte la routine
- Prends ta santé au sérieux
- Travaille avec constance""",

    ('sagittarius', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées – engagement ou liberté?

## L'énergie du moment
Saturne traverse ta maison VII, testant ton besoin de liberté contre l'engagement relationnel.

## Ce que tu pourrais vivre
- Des tests dans les relations
- Un engagement sérieux ou une séparation
- Des responsabilités relationnelles

## Conseils pour ce transit
- Apprends à t'engager
- Travaille sur tes relations
- Équilibre liberté et engagement""",

    ('sagittarius', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et ressources partagées demandent prudence.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer avec sagesse les ressources partagées et à accepter les transformations.

## Ce que tu pourrais vivre
- Des responsabilités financières
- Une transformation lente
- Un travail sur les peurs

## Conseils pour ce transit
- Gère les finances avec prudence
- Accepte la transformation
- Travaille sur tes peurs""",

    ('sagittarius', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes croyances sont testées – construis une sagesse solide.

## L'énergie du moment
Saturne traverse ta maison IX, ta maison naturelle! C'est un test majeur de tes croyances et de ta philosophie de vie. Ce en quoi tu crois doit résister à l'épreuve du temps.

## Ce que tu pourrais vivre
- Une remise en question profonde des croyances
- Des études ou voyages avec un but sérieux
- Un besoin de sagesse pratique

## Conseils pour ce transit
- Construis une philosophie qui tient
- Étudie avec rigueur
- Voyage avec intention""",

    ('sagittarius', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande efforts concrets et responsabilité.

## L'énergie du moment
Saturne traverse ta maison X, c'est une période cruciale pour concrétiser tes ambitions professionnelles.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un test de tes ambitions
- Des avancées par le travail

## Conseils pour ce transit
- Travaille pour tes objectifs
- Assume tes responsabilités
- Concrétise tes visions""",

    ('sagittarius', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets sont évalués avec réalisme.

## L'énergie du moment
Saturne traverse ta maison XI, testant tes amitiés et tes grands projets d'avenir.

## Ce que tu pourrais vivre
- Une évaluation des amitiés
- Des responsabilités de groupe
- Un réalisme sur l'avenir

## Conseils pour ce transit
- Garde les amitiés sincères
- Sois réaliste sur tes projets
- Engage-toi concrètement""",

    ('sagittarius', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur sur la fuite et les peurs.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sur ta tendance à fuir et tes peurs cachées.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation aux fuites
- Un besoin de solitude

## Conseils pour ce transit
- Affronte ce que tu fuis
- Utilise la solitude pour grandir
- Prépare le prochain cycle""",

    # ============== CAPRICORN ==============
    ('capricorn', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité – ton maître te teste!

## L'énergie du moment
Saturne, ton maître, traverse ta maison I. C'est une période majeure de redéfinition de ton identité avec encore plus de responsabilité et de maturité.

## Ce que tu pourrais vivre
- Un questionnement profond sur ton identité
- Des responsabilités personnelles accrues
- Un besoin de structure encore plus grande

## Conseils pour ce transit
- Construis ta meilleure version
- Assume pleinement tes responsabilités
- Sois patient(e) avec toi-même""",

    ('capricorn', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances sont restructurées avec ta rigueur naturelle.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière avec ta discipline naturelle.

## Ce que tu pourrais vivre
- Des restrictions financières possibles
- Un besoin de contrôle financier
- Une réévaluation des valeurs

## Conseils pour ce transit
- Construis une stabilité inébranlable
- Reconnais ta valeur
- Économise stratégiquement""",

    ('capricorn', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient encore plus structurée.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée et communication avec encore plus de précision.

## Ce que tu pourrais vivre
- Une communication très structurée
- Des apprentissages exigeants
- Des responsabilités intellectuelles

## Conseils pour ce transit
- Apprends des choses durables
- Communique avec précision
- Structure toutes tes idées""",

    ('capricorn', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent structure et leadership.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider tes fondations familiales avec autorité.

## Ce que tu pourrais vivre
- Des responsabilités familiales de chef
- Un besoin de sécuriser le foyer
- Un travail sur les racines

## Conseils pour ce transit
- Consolide tes fondations
- Assume le leadership familial
- Travaille sur ton histoire""",

    ('capricorn', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement sérieux.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux l'amour et la créativité, domaines où tu peux être distant.

## Ce que tu pourrais vivre
- Un besoin d'amour mature
- Des projets créatifs structurés
- Des responsabilités

## Conseils pour ce transit
- Engage-toi en amour
- Discipline ta créativité
- Ouvre-toi au plaisir structuré""",

    ('capricorn', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé sont optimisés avec discipline.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à perfectionner ton quotidien professionnel et ta santé.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline parfaite
- Une attention méticuleuse à la santé

## Conseils pour ce transit
- Excelle dans ton travail quotidien
- Prends ta santé au sérieux
- Structure chaque détail""",

    ('capricorn', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées – l'engagement est essentiel.

## L'énergie du moment
Saturne traverse ta maison VII, testant la solidité de tes relations avec des standards élevés.

## Ce que tu pourrais vivre
- Des tests majeurs dans les relations
- Un engagement sérieux ou une séparation
- Des responsabilités relationnelles

## Conseils pour ce transit
- Engage-toi avec tes standards
- Travaille sur tes relations
- Assume les responsabilités""",

    ('capricorn', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et ressources partagées demandent contrôle.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer les ressources partagées et les transformations avec ton contrôle naturel.

## Ce que tu pourrais vivre
- Des responsabilités financières importantes
- Une transformation contrôlée
- Un travail sur le pouvoir

## Conseils pour ce transit
- Gère les finances avec maîtrise
- Accepte la transformation
- Travaille sur la vulnérabilité""",

    ('capricorn', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde est restructurée avec tes standards.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à construire une philosophie qui résiste à tes propres critères exigeants.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études ou voyages avec un but
- Un besoin de sens pratique

## Conseils pour ce transit
- Construis une philosophie solide
- Étudie avec tes standards
- Voyage avec intention""",

    ('capricorn', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière est au sommet des responsabilités – ton moment!

## L'énergie du moment
Saturne traverse ta maison X, sa maison et la tienne! C'est LE moment majeur de ta carrière où tout ton travail peut porter ses fruits ou être testé.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles maximales
- Un test ultime de ta position
- Des avancées majeures ou des leçons

## Conseils pour ce transit
- Donne tout pour ta carrière
- Assume le leadership total
- Construis ton héritage""",

    ('capricorn', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets sont évalués avec tes critères.

## L'énergie du moment
Saturne traverse ta maison XI, testant tes amitiés et projets avec tes standards élevés.

## Ce que tu pourrais vivre
- Une évaluation sévère des amitiés
- Des responsabilités de groupe
- Un réalisme sur l'avenir

## Conseils pour ce transit
- Garde les amitiés qui comptent
- Sois réaliste mais ambitieux
- Assume des responsabilités collectives""",

    ('capricorn', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur sur le contrôle et les peurs.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sur ton besoin de contrôle et tes peurs cachées.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation aux peurs de faiblesse
- Un besoin de solitude

## Conseils pour ce transit
- Affronte tes peurs de vulnérabilité
- Utilise la solitude pour grandir
- Prépare le prochain grand cycle""",

    # ============== AQUARIUS ==============
    ('aquarius', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité unique avec discipline.

## L'énergie du moment
Saturne, ton ancien maître, traverse ta maison I. C'est une période de redéfinition de ton identité avec structure et discipline.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles
- Un besoin de structure dans l'originalité

## Conseils pour ce transit
- Structure ton unicité
- Assume tes responsabilités
- Discipline ton originalité""",

    ('aquarius', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances sont restructurées avec méthode.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière stable.

## Ce que tu pourrais vivre
- Des restrictions financières
- Un besoin de budgéter
- Une réévaluation des valeurs

## Conseils pour ce transit
- Construis une stabilité financière
- Reconnais ta valeur
- Économise méthodiquement""",

    ('aquarius', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient plus structurée et concrète.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer tes idées innovantes avec rigueur.

## Ce que tu pourrais vivre
- Une communication plus structurée
- Des apprentissages exigeants
- Des responsabilités intellectuelles

## Conseils pour ce transit
- Structure tes idées innovantes
- Apprends avec rigueur
- Communique concrètement""",

    ('aquarius', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer demande structure et stabilité.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider tes fondations même si tu aimes le changement.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin de stabilité
- Un travail sur les racines

## Conseils pour ce transit
- Crée une base stable
- Assume tes responsabilités familiales
- Trouve la liberté dans la structure""",

    ('aquarius', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement et structure.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à structurer tes expressions créatives et tes amours.

## Ce que tu pourrais vivre
- Un besoin d'amour structuré
- Des projets créatifs disciplinés
- Des responsabilités

## Conseils pour ce transit
- Engage-toi en amour
- Structure ta créativité
- Assume tes choix""",

    ('aquarius', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline systématique.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à structurer ton quotidien avec méthode.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline
- Une attention à la santé

## Conseils pour ce transit
- Structure ton quotidien
- Prends ta santé au sérieux
- Systématise ton travail""",

    ('aquarius', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées – engagement ou indépendance?

## L'énergie du moment
Saturne traverse ta maison VII, testant ton besoin d'indépendance contre l'engagement relationnel.

## Ce que tu pourrais vivre
- Des tests dans les relations
- Un engagement sérieux
- Des responsabilités relationnelles

## Conseils pour ce transit
- Trouve l'équilibre liberté/engagement
- Travaille sur tes relations
- Assume les responsabilités""",

    ('aquarius', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et ressources partagées demandent structure.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer les ressources partagées et les transformations avec méthode.

## Ce que tu pourrais vivre
- Des responsabilités financières
- Une transformation structurée
- Un travail sur le détachement

## Conseils pour ce transit
- Gère les finances méthodiquement
- Accepte la transformation
- Structure le changement""",

    ('aquarius', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes croyances et ta vision sont restructurées.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à construire une philosophie qui résiste au temps.

## Ce que tu pourrais vivre
- Une remise en question des idéaux
- Des études structurées
- Un besoin de sens concret

## Conseils pour ce transit
- Construis une vision solide
- Étudie avec rigueur
- Concrétise tes idéaux""",

    ('aquarius', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande efforts et responsabilité concrète.

## L'énergie du moment
Saturne traverse ta maison X, c'est une période cruciale pour concrétiser tes ambitions professionnelles.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un test de tes objectifs
- Des avancées par le travail

## Conseils pour ce transit
- Construis ta réputation
- Assume tes responsabilités
- Concrétise ta vision""",

    ('aquarius', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets sont profondément évalués.

## L'énergie du moment
Saturne traverse ta maison XI, ta maison naturelle avec Uranus. C'est un test majeur de tes amitiés et de tes projets humanitaires.

## Ce que tu pourrais vivre
- Une évaluation sérieuse des amitiés
- Des responsabilités dans les groupes
- Un réalisme sur l'avenir

## Conseils pour ce transit
- Garde les amitiés authentiques
- Structure tes projets d'avenir
- Assume des responsabilités collectives""",

    ('aquarius', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur sur le détachement et les peurs.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sur ton détachement émotionnel et tes peurs cachées.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation aux peurs d'intimité
- Un besoin de solitude

## Conseils pour ce transit
- Affronte tes peurs cachées
- Utilise la solitude constructivement
- Prépare le prochain cycle""",

    # ============== PISCES ==============
    ('pisces', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité sensible avec discipline.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es avec structure. Ton côté rêveur doit s'ancrer dans la réalité.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles
- Un besoin d'ancrage

## Conseils pour ce transit
- Ancre tes rêves dans la réalité
- Assume tes responsabilités
- Structure ta sensibilité""",

    ('pisces', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances sont restructurées avec réalisme.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière concrète au lieu de rêver.

## Ce que tu pourrais vivre
- Des restrictions financières
- Un besoin de budgéter concrètement
- Une réévaluation des valeurs

## Conseils pour ce transit
- Construis une stabilité réelle
- Reconnais ta valeur
- Économise avec discipline""",

    ('pisces', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient plus structurée et concrète.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée intuitive avec plus de logique.

## Ce que tu pourrais vivre
- Une communication plus structurée
- Des apprentissages exigeants
- Des responsabilités de communication

## Conseils pour ce transit
- Structure tes intuitions
- Apprends des choses concrètes
- Communique clairement""",

    ('pisces', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer demande structure et ancrage.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à créer un foyer stable et sécurisant.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin de sécurité
- Un travail sur les racines

## Conseils pour ce transit
- Crée un vrai foyer stable
- Assume tes responsabilités familiales
- Ancre-toi""",

    ('pisces', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement et discipline.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à structurer tes élans créatifs et amoureux au lieu de les laisser flotter.

## Ce que tu pourrais vivre
- Un besoin d'amour engagé
- Des projets créatifs disciplinés
- Des responsabilités

## Conseils pour ce transit
- Engage-toi vraiment en amour
- Discipline ta créativité
- Concrétise tes visions artistiques""",

    ('pisces', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline quotidienne.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à structurer ton quotidien avec rigueur.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline
- Une attention à la santé

## Conseils pour ce transit
- Structure ton quotidien
- Prends ta santé au sérieux
- Travaille avec constance""",

    ('pisces', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées – engagement ou sacrifice?

## L'énergie du moment
Saturne traverse ta maison VII, testant tes relations et ta tendance au sacrifice.

## Ce que tu pourrais vivre
- Des tests dans les relations
- Un engagement sérieux
- Des limites à poser

## Conseils pour ce transit
- Engage-toi avec des limites saines
- Travaille sur tes relations
- Évite le sacrifice excessif""",

    ('pisces', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et ressources partagées demandent ancrage.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer les ressources partagées et les transformations avec réalisme.

## Ce que tu pourrais vivre
- Des responsabilités financières
- Une transformation ancrée
- Un travail sur les peurs

## Conseils pour ce transit
- Gère les finances concrètement
- Accepte la transformation
- Ancre tes peurs""",

    ('pisces', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes croyances et ta spiritualité sont restructurées.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à construire une spiritualité qui s'applique dans la vie réelle.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études spirituelles structurées
- Un besoin de sens pratique

## Conseils pour ce transit
- Ancre ta spiritualité
- Étudie avec discipline
- Applique tes croyances""",

    ('pisces', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande efforts concrets et responsabilité.

## L'énergie du moment
Saturne traverse ta maison X, c'est une période cruciale pour concrétiser tes rêves professionnels.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un test de tes aspirations
- Des avancées par le travail concret

## Conseils pour ce transit
- Concrétise tes rêves de carrière
- Assume tes responsabilités
- Travaille avec discipline""",

    ('pisces', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets humanitaires sont évalués.

## L'énergie du moment
Saturne traverse ta maison XI, testant tes amitiés et tes idéaux humanitaires.

## Ce que tu pourrais vivre
- Une évaluation des amitiés
- Des responsabilités de groupe
- Un réalisme sur l'avenir

## Conseils pour ce transit
- Garde les amitiés sincères
- Concrétise tes idéaux
- Engage-toi vraiment""",

    ('pisces', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps majeur de travail intérieur et de fin de cycle.

## L'énergie du moment
Saturne traverse ta maison XII, ta maison naturelle avec Neptune! C'est une période majeure de travail intérieur, de confrontation aux peurs et de préparation à une renaissance.

## Ce que tu pourrais vivre
- Un travail profond sur l'inconscient
- La confrontation aux peurs et illusions
- Un besoin de solitude transformatrice

## Conseils pour ce transit
- Affronte tes illusions
- Utilise la solitude pour guérir
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
        print(f"✅ Transit Saturn (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
