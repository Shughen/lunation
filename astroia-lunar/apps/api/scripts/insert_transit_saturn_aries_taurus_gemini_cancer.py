#!/usr/bin/env python3
"""Insert transit_saturn interpretations for Aries, Taurus, Gemini, Cancer (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_SATURN_INTERPRETATIONS = {
    # ============== ARIES ==============
    ('aries', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Une période de restructuration profonde de ton identité et de ta façon de t'affirmer.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es avec maturité et responsabilité. C'est un temps de consolidation personnelle où tu dois prendre tes responsabilités et construire une identité plus solide. Les raccourcis ne fonctionnent plus.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités accrues envers toi-même
- Un besoin de maturité et d'authenticité

## Conseils pour ce transit
- Construis une version plus mature de toi
- Assume tes responsabilités personnelles
- Sois patient(e) avec ton évolution""",

    ('aries', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de tes finances et de ta relation à la valeur – construis sur du solide.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à revoir ta relation à l'argent et tes valeurs. Les dépenses frivoles sont sanctionnées, mais les efforts constants sont récompensés. C'est le moment de bâtir une sécurité financière durable.

## Ce que tu pourrais vivre
- Des restrictions ou responsabilités financières
- Un besoin de budgéter et planifier
- Une réévaluation de ce qui compte vraiment

## Conseils pour ce transit
- Construis une stabilité financière durable
- Reconnais ta vraie valeur
- Évite les dépenses impulsives""",

    ('aries', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication et tes apprentissages deviennent plus sérieux et structurés.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée et ta communication. Les échanges superficiels perdent de l'attrait, tu veux du concret. Les relations avec les proches peuvent être testées.

## Ce que tu pourrais vivre
- Un besoin de communication plus sérieuse
- Des apprentissages exigeants mais durables
- Des responsabilités envers les proches

## Conseils pour ce transit
- Apprends des choses qui durent
- Communique avec précision
- Renforce tes liens avec sérieux""",

    ('aries', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent structure et responsabilité.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider tes fondations domestiques et familiales. Tu peux ressentir le poids des responsabilités familiales ou le besoin de sécuriser ton chez-toi.

## Ce que tu pourrais vivre
- Des responsabilités familiales accrues
- Un besoin de sécuriser le foyer
- Un travail sur les blessures d'enfance

## Conseils pour ce transit
- Consolide tes fondations
- Assume tes responsabilités familiales
- Travaille sur ton histoire personnelle""",

    ('aries', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Créativité et amour demandent maturité et engagement sérieux.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux l'amour et la créativité. Les romances légères ne suffisent plus, tu veux du durable. Les projets créatifs demandent discipline et persévérance.

## Ce que tu pourrais vivre
- Un besoin d'amour mature et sérieux
- Des projets créatifs exigeants
- Des responsabilités parentales possibles

## Conseils pour ce transit
- Engage-toi sérieusement en amour
- Discipline ta créativité
- Assume tes responsabilités de cœur""",

    ('aries', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton travail et ta santé demandent structure et discipline.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à restructurer ton quotidien professionnel et tes habitudes de santé. Le travail peut devenir plus exigeant mais aussi plus stable.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles accrues
- Un besoin de discipline quotidienne
- Une attention à la santé nécessaire

## Conseils pour ce transit
- Structure ton quotidien
- Prends ta santé au sérieux
- Travaille avec rigueur""",

    ('aries', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations et partenariats sont testés et demandent engagement.

## L'énergie du moment
Saturne traverse ta maison VII, testant la solidité de tes relations. Les partenariats qui ne reposent pas sur des bases solides peuvent être remis en question. C'est le temps de l'engagement mature.

## Ce que tu pourrais vivre
- Des tests dans les relations
- Un engagement sérieux ou une séparation
- Des responsabilités envers les partenaires

## Conseils pour ce transit
- Engage-toi avec maturité
- Travaille sur tes relations
- Accepte les responsabilités relationnelles""",

    ('aries', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et finances partagées demandent prudence et responsabilité.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer avec sagesse les ressources partagées et à accepter les transformations nécessaires. Les questions de dettes, héritages ou intimité demandent du sérieux.

## Ce que tu pourrais vivre
- Des responsabilités financières partagées
- Une transformation lente mais profonde
- Un travail sur les peurs et le contrôle

## Conseils pour ce transit
- Gère les finances partagées avec rigueur
- Accepte la transformation
- Travaille sur tes peurs profondes""",

    ('aries', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde et tes croyances sont restructurées.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à revoir tes croyances et ta philosophie de vie. Les voyages et les études demandent plus de sérieux. C'est le temps de construire une vision mature du monde.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études ou voyages avec un but
- Un besoin de sens concret

## Conseils pour ce transit
- Construis une philosophie solide
- Étudie avec discipline
- Voyage avec intention""",

    ('aries', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière et ta position sociale demandent efforts et responsabilité.

## L'énergie du moment
Saturne traverse ta maison X, SON domicile naturel. C'est une période cruciale pour ta carrière où tes efforts sont évalués. Les responsabilités professionnelles augmentent mais les récompenses à long terme aussi.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles majeures
- Un test de ta position sociale
- Des avancées lentes mais solides

## Conseils pour ce transit
- Construis ta réputation avec patience
- Assume tes responsabilités professionnelles
- Vise des objectifs à long terme""",

    ('aries', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et tes projets d'avenir sont évalués et restructurés.

## L'énergie du moment
Saturne traverse ta maison XI, testant la qualité de tes amitiés et la solidité de tes projets. Les relations superficielles peuvent s'éloigner, mais les vraies amitiés se renforcent.

## Ce que tu pourrais vivre
- Une évaluation de tes amitiés
- Des responsabilités dans les groupes
- Un réalisme sur tes projets d'avenir

## Conseils pour ce transit
- Garde les amitiés qui comptent
- Sois réaliste sur tes objectifs
- Assume des responsabilités collectives""",

    ('aries', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur profond et de dissolution de vieilles structures.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sérieux. C'est une période de fin de cycle où les vieilles peurs et limitations doivent être affrontées pour préparer un nouveau départ.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation à des peurs anciennes
- Un besoin de solitude constructive

## Conseils pour ce transit
- Affronte tes peurs avec courage
- Utilise la solitude pour grandir
- Prépare le prochain cycle""",

    # ============== TAURUS ==============
    ('taurus', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Une restructuration profonde de ton identité et de ton image.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es avec maturité. C'est le temps de construire une identité plus authentique et responsable.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles accrues
- Un besoin de maturité

## Conseils pour ce transit
- Construis qui tu veux vraiment être
- Assume tes responsabilités
- Sois patient(e) avec toi-même""",

    ('taurus', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances et tes valeurs sont testées et restructurées.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière durable. Les dépenses impulsives sont sanctionnées, la discipline est récompensée.

## Ce que tu pourrais vivre
- Des restrictions financières possibles
- Un besoin de budgéter sérieusement
- Une réévaluation de tes valeurs

## Conseils pour ce transit
- Construis une stabilité financière
- Reconnais ta vraie valeur
- Économise et investis sagement""",

    ('taurus', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication et tes apprentissages demandent structure.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée et ta communication. Les échanges deviennent plus sérieux.

## Ce que tu pourrais vivre
- Une communication plus structurée
- Des apprentissages exigeants
- Des responsabilités envers les proches

## Conseils pour ce transit
- Apprends des choses durables
- Communique avec précision
- Renforce tes liens proches""",

    ('taurus', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent structure et responsabilité.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider tes fondations. Les responsabilités familiales augmentent.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin de sécuriser le foyer
- Un travail sur les racines

## Conseils pour ce transit
- Consolide ton chez-toi
- Assume tes responsabilités familiales
- Travaille sur ton histoire""",

    ('taurus', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement sérieux.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux l'amour et la créativité. Les romances légères ne suffisent plus.

## Ce que tu pourrais vivre
- Un besoin d'amour mature
- Des projets créatifs exigeants
- Des responsabilités parentales

## Conseils pour ce transit
- Engage-toi sérieusement en amour
- Discipline ta créativité
- Assume tes responsabilités""",

    ('taurus', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline et structure.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à restructurer ton quotidien. Le travail peut être exigeant mais stable.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline quotidienne
- Une attention à la santé

## Conseils pour ce transit
- Structure ton quotidien
- Prends ta santé au sérieux
- Travaille avec rigueur""",

    ('taurus', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées et demandent maturité.

## L'énergie du moment
Saturne traverse ta maison VII, testant la solidité de tes relations. C'est le temps de l'engagement mature ou de la remise en question.

## Ce que tu pourrais vivre
- Des tests dans les relations
- Un engagement sérieux possible
- Des responsabilités relationnelles

## Conseils pour ce transit
- Engage-toi avec maturité
- Travaille sur tes relations
- Assume tes responsabilités""",

    ('taurus', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et finances partagées demandent prudence.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer avec sagesse les ressources partagées. Les transformations sont lentes mais profondes.

## Ce que tu pourrais vivre
- Des responsabilités financières partagées
- Une transformation lente
- Un travail sur les peurs

## Conseils pour ce transit
- Gère les finances avec rigueur
- Accepte la transformation
- Affronte tes peurs""",

    ('taurus', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde est restructurée avec maturité.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à revoir tes croyances. Les voyages et études demandent du sérieux.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études ou voyages sérieux
- Un besoin de sens concret

## Conseils pour ce transit
- Construis une philosophie solide
- Étudie avec discipline
- Voyage avec intention""",

    ('taurus', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande efforts et responsabilité – construis pour durer.

## L'énergie du moment
Saturne traverse ta maison X avec son énergie naturelle. C'est une période cruciale pour ta carrière où les efforts sont évalués.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles majeures
- Un test de ta position
- Des avancées lentes mais solides

## Conseils pour ce transit
- Construis ta réputation
- Assume tes responsabilités
- Vise le long terme""",

    ('taurus', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets d'avenir sont évalués.

## L'énergie du moment
Saturne traverse ta maison XI, testant tes amitiés et projets. Les relations superficielles peuvent s'éloigner.

## Ce que tu pourrais vivre
- Une évaluation des amitiés
- Des responsabilités dans les groupes
- Un réalisme sur l'avenir

## Conseils pour ce transit
- Garde les vraies amitiés
- Sois réaliste
- Assume des responsabilités collectives""",

    ('taurus', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur et de dissolution des vieilles structures.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur. C'est une période de fin de cycle.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation à des peurs
- Un besoin de solitude

## Conseils pour ce transit
- Affronte tes peurs
- Utilise la solitude pour grandir
- Prépare le prochain cycle""",

    # ============== GEMINI ==============
    ('gemini', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Restructuration de ton identité et de ta façon de t'exprimer.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es avec maturité. C'est le temps de construire une identité plus solide.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles
- Un besoin de maturité

## Conseils pour ce transit
- Construis une version mature de toi
- Assume tes responsabilités
- Sois patient(e)""",

    ('gemini', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances et valeurs sont restructurées.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière. La discipline est récompensée.

## Ce que tu pourrais vivre
- Des restrictions financières possibles
- Un besoin de budgéter
- Une réévaluation des valeurs

## Conseils pour ce transit
- Construis une stabilité
- Reconnais ta valeur
- Économise sagement""",

    ('gemini', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient plus sérieuse et structurée.

## L'énergie du moment
Saturne traverse ta maison III, ta maison naturelle! C'est le temps de structurer ta pensée et ta communication avec rigueur.

## Ce que tu pourrais vivre
- Une communication plus sérieuse
- Des apprentissages exigeants
- Des responsabilités intellectuelles

## Conseils pour ce transit
- Structure ta pensée
- Apprends avec rigueur
- Communique avec précision""",

    ('gemini', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent structure.

## L'énergie du moment
Saturne traverse ta maison IV, t'invitant à consolider tes fondations domestiques.

## Ce que tu pourrais vivre
- Des responsabilités familiales
- Un besoin de sécuriser le foyer
- Un travail sur les racines

## Conseils pour ce transit
- Consolide tes fondations
- Assume tes responsabilités familiales
- Travaille sur ton histoire""",

    ('gemini', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux l'amour et la créativité.

## Ce que tu pourrais vivre
- Un besoin d'amour mature
- Des projets créatifs exigeants
- Des responsabilités

## Conseils pour ce transit
- Engage-toi sérieusement
- Discipline ta créativité
- Assume tes responsabilités""",

    ('gemini', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à restructurer ton quotidien.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline
- Une attention à la santé

## Conseils pour ce transit
- Structure ton quotidien
- Prends ta santé au sérieux
- Travaille avec rigueur""",

    ('gemini', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées.

## L'énergie du moment
Saturne traverse ta maison VII, testant la solidité de tes relations.

## Ce que tu pourrais vivre
- Des tests relationnels
- Un engagement sérieux
- Des responsabilités

## Conseils pour ce transit
- Engage-toi avec maturité
- Travaille sur tes relations
- Assume tes responsabilités""",

    ('gemini', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et finances partagées demandent prudence.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer avec sagesse les ressources partagées.

## Ce que tu pourrais vivre
- Des responsabilités financières
- Une transformation lente
- Un travail sur les peurs

## Conseils pour ce transit
- Gère les finances avec rigueur
- Accepte la transformation
- Affronte tes peurs""",

    ('gemini', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde est restructurée.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à revoir tes croyances avec maturité.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études sérieuses
- Un besoin de sens

## Conseils pour ce transit
- Construis une philosophie solide
- Étudie avec discipline
- Voyage avec intention""",

    ('gemini', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande efforts et responsabilité.

## L'énergie du moment
Saturne traverse ta maison X, c'est une période cruciale pour ta carrière.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un test de ta position
- Des avancées lentes

## Conseils pour ce transit
- Construis ta réputation
- Assume tes responsabilités
- Vise le long terme""",

    ('gemini', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets sont évalués.

## L'énergie du moment
Saturne traverse ta maison XI, testant tes amitiés et projets.

## Ce que tu pourrais vivre
- Une évaluation des amitiés
- Des responsabilités de groupe
- Un réalisme nécessaire

## Conseils pour ce transit
- Garde les vraies amitiés
- Sois réaliste
- Engage-toi collectivement""",

    ('gemini', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur profond.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sérieux.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation aux peurs
- Un besoin de solitude

## Conseils pour ce transit
- Affronte tes peurs
- Utilise la solitude
- Prépare le prochain cycle""",

    # ============== CANCER ==============
    ('cancer', 1): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Une restructuration de ton identité avec maturité.

## L'énergie du moment
Saturne traverse ta maison I, t'invitant à redéfinir qui tu es. C'est le temps de construire une identité plus solide et responsable.

## Ce que tu pourrais vivre
- Un questionnement sur ton identité
- Des responsabilités personnelles
- Un besoin de maturité

## Conseils pour ce transit
- Construis qui tu veux être
- Assume tes responsabilités
- Sois patient(e)""",

    ('cancer', 2): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes finances et valeurs sont restructurées.

## L'énergie du moment
Saturne traverse ta maison II, t'invitant à bâtir une sécurité financière durable.

## Ce que tu pourrais vivre
- Des restrictions possibles
- Un besoin de budgéter
- Une réévaluation des valeurs

## Conseils pour ce transit
- Construis une stabilité
- Reconnais ta valeur
- Économise sagement""",

    ('cancer', 3): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta communication devient plus sérieuse.

## L'énergie du moment
Saturne traverse ta maison III, t'invitant à structurer ta pensée.

## Ce que tu pourrais vivre
- Une communication plus structurée
- Des apprentissages exigeants
- Des responsabilités de proximité

## Conseils pour ce transit
- Apprends des choses durables
- Communique avec précision
- Renforce tes liens""",

    ('cancer', 4): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ton foyer et ta famille demandent structure et responsabilité.

## L'énergie du moment
Saturne traverse ta maison IV, ta maison naturelle! C'est une période cruciale pour consolider tes fondations et assumer tes responsabilités familiales.

## Ce que tu pourrais vivre
- Des responsabilités familiales majeures
- Un besoin de sécuriser le foyer
- Un travail sur les blessures familiales

## Conseils pour ce transit
- Consolide tes fondations
- Assume tes responsabilités familiales
- Travaille sur ton histoire""",

    ('cancer', 5): """# ♄ Transit de Saturne en Bélier

**En une phrase :** L'amour et la créativité demandent engagement.

## L'énergie du moment
Saturne traverse ta maison V, t'invitant à prendre au sérieux l'amour et la créativité.

## Ce que tu pourrais vivre
- Un besoin d'amour mature
- Des projets créatifs exigeants
- Des responsabilités parentales

## Conseils pour ce transit
- Engage-toi sérieusement
- Discipline ta créativité
- Assume tes responsabilités""",

    ('cancer', 6): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Travail et santé demandent discipline.

## L'énergie du moment
Saturne traverse ta maison VI, t'invitant à restructurer ton quotidien.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un besoin de discipline
- Une attention à la santé

## Conseils pour ce transit
- Structure ton quotidien
- Prends ta santé au sérieux
- Travaille avec rigueur""",

    ('cancer', 7): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes relations sont testées et demandent maturité.

## L'énergie du moment
Saturne traverse ta maison VII, testant la solidité de tes relations.

## Ce que tu pourrais vivre
- Des tests relationnels
- Un engagement sérieux
- Des responsabilités relationnelles

## Conseils pour ce transit
- Engage-toi avec maturité
- Travaille sur tes relations
- Assume tes responsabilités""",

    ('cancer', 8): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Transformation et finances partagées demandent prudence.

## L'énergie du moment
Saturne traverse ta maison VIII, t'invitant à gérer avec sagesse les ressources partagées.

## Ce que tu pourrais vivre
- Des responsabilités financières
- Une transformation lente
- Un travail sur les peurs

## Conseils pour ce transit
- Gère les finances avec rigueur
- Accepte la transformation
- Affronte tes peurs""",

    ('cancer', 9): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta vision du monde est restructurée.

## L'énergie du moment
Saturne traverse ta maison IX, t'invitant à revoir tes croyances avec maturité.

## Ce que tu pourrais vivre
- Une remise en question des croyances
- Des études sérieuses
- Un besoin de sens concret

## Conseils pour ce transit
- Construis une philosophie solide
- Étudie avec discipline
- Voyage avec intention""",

    ('cancer', 10): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Ta carrière demande efforts et responsabilité.

## L'énergie du moment
Saturne traverse ta maison X, c'est une période cruciale pour ta carrière.

## Ce que tu pourrais vivre
- Des responsabilités professionnelles
- Un test de ta position
- Des avancées lentes mais solides

## Conseils pour ce transit
- Construis ta réputation
- Assume tes responsabilités
- Vise le long terme""",

    ('cancer', 11): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Tes amitiés et projets sont évalués.

## L'énergie du moment
Saturne traverse ta maison XI, testant tes amitiés et projets.

## Ce que tu pourrais vivre
- Une évaluation des amitiés
- Des responsabilités de groupe
- Un réalisme nécessaire

## Conseils pour ce transit
- Garde les vraies amitiés
- Sois réaliste
- Engage-toi collectivement""",

    ('cancer', 12): """# ♄ Transit de Saturne en Bélier

**En une phrase :** Un temps de travail intérieur profond et de fin de cycle.

## L'énergie du moment
Saturne traverse ta maison XII, t'invitant à un travail intérieur sérieux.

## Ce que tu pourrais vivre
- Un travail sur l'inconscient
- La confrontation aux peurs
- Un besoin de solitude constructive

## Conseils pour ce transit
- Affronte tes peurs
- Utilise la solitude pour grandir
- Prépare le prochain cycle""",
}

async def insert_interpretations():
    """Insert transit Saturn interpretations into database."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_SATURN_INTERPRETATIONS.items():
            # Check if already exists
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
        print(f"✅ Transit Saturn (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
