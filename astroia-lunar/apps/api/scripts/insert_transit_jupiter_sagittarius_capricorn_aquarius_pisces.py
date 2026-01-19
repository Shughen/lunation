#!/usr/bin/env python3
"""Insert transit_jupiter interpretations for Sagittarius, Capricorn, Aquarius, Pisces (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_JUPITER_INTERPRETATIONS = {
    # ============== SAGITTARIUS ==============
    ('sagittarius', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle exceptionnelle – tu es béni(e) par ton maître!

## L'énergie du moment
Jupiter, ton maître, traverse ta maison I avec une énergie de feu! C'est une période exceptionnelle de chance, d'optimisme et d'expansion personnelle. Les portes s'ouvrent, les opportunités affluent.

## Ce que tu pourrais vivre
- Une confiance et un optimisme décuplés
- Des opportunités remarquables
- Une envie d'aventure et de croissance

## Conseils pour ce transit
- Lance-toi dans de grandes aventures
- Saisis toutes les opportunités
- Attention à l'excès d'optimisme""",

    ('sagittarius', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont magnifiquement favorisées.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et abondance. Les revenus peuvent augmenter significativement, souvent par des voies inattendues.

## Ce que tu pourrais vivre
- Une augmentation notable des revenus
- Des opportunités financières chanceuses
- Une reconnaissance de ta valeur

## Conseils pour ce transit
- Investis dans tes aventures
- Valorise ton optimisme
- Évite les dépenses excessives""",

    ('sagittarius', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont exceptionnellement bénis.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel avec enthousiasme. Les échanges sont fructueux et inspirants.

## Ce que tu pourrais vivre
- Des apprentissages passionnants
- Des communications réussies
- Des relations de proximité enrichies

## Conseils pour ce transit
- Apprends et enseigne avec passion
- Communique tes idées
- Explore ton environnement""",

    ('sagittarius', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis par l'expansion.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et bénédictions à ta vie domestique. Période favorable pour agrandir ou améliorer ton chez-toi.

## Ce que tu pourrais vivre
- Un agrandissement du foyer
- Des joies familiales
- Un sentiment de sécurité

## Conseils pour ce transit
- Agrandis ton espace
- Cultive la joie familiale
- Renforce tes racines""",

    ('sagittarius', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour, la créativité et les plaisirs sont magnifiquement favorisés!

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance à l'amour et la créativité. Les romances sont aventureuses, les projets créatifs florissent.

## Ce que tu pourrais vivre
- Une romance aventureuse
- Des succès créatifs
- Des moments de joie intense

## Conseils pour ce transit
- Vis l'amour avec enthousiasme
- Crée avec passion
- Profite des aventures""",

    ('sagittarius', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent avec optimisme.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail et à la santé. Les opportunités professionnelles arrivent avec enthousiasme.

## Ce que tu pourrais vivre
- De meilleures conditions de travail
- Des opportunités professionnelles
- Une santé florissante

## Conseils pour ce transit
- Travaille avec enthousiasme
- Prends soin de ta santé
- Sers avec générosité""",

    ('sagittarius', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies – période d'expansion relationnelle.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance à toutes tes relations. Les rencontres sont significatives et aventureuses.

## Ce que tu pourrais vivre
- Une rencontre inspirante
- Un engagement favorable
- Des partenariats enrichissants

## Conseils pour ce transit
- Sois ouvert(e) aux grandes relations
- Engage-toi avec optimisme
- Collabore avec enthousiasme""",

    ('sagittarius', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation positive
- Une intimité enrichie

## Conseils pour ce transit
- Gère bien les finances communes
- Accepte la transformation
- Explore avec foi""",

    ('sagittarius', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et quête de sens sont EXCEPTIONNELLEMENT favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX, sa maison et la tienne! C'est une période exceptionnelle pour les voyages, les études et l'expansion spirituelle. Le monde entier t'appelle.

## Ce que tu pourrais vivre
- Des voyages mémorables et transformateurs
- Des succès académiques majeurs
- Une expansion spirituelle profonde

## Conseils pour ce transit
- Voyage le plus possible
- Entreprends de grandes études
- Explore toutes les philosophies""",

    ('sagittarius', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont bénies – vise le plus haut!

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance et expansion maximale à ta vie professionnelle.

## Ce que tu pourrais vivre
- Une promotion ou avancement majeur
- Une reconnaissance publique
- L'atteinte de grands objectifs

## Conseils pour ce transit
- Vise les plus hauts sommets
- Accepte les grandes responsabilités
- Rayonne dans ta carrière""",

    ('sagittarius', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent magnifiquement.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale et tes rêves. Les amitiés se multiplient, tes grands souhaits se réalisent.

## Ce que tu pourrais vivre
- Des amitiés internationales
- La réalisation de grands souhaits
- Un réseau mondial

## Conseils pour ce transit
- Élargis ton cercle social
- Engage-toi dans des causes mondiales
- Rêve sans limites""",

    ('sagittarius', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure – période de grâce.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle. La foi te protège.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle
- Des aides inattendues

## Conseils pour ce transit
- Médite et explore ta foi
- Guéris avec optimisme
- Fais confiance à l'univers""",

    # ============== CAPRICORN ==============
    ('capricorn', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle et opportunités nouvelles t'accueillent.

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ton développement. Ta confiance augmente, les opportunités arrivent.

## Ce que tu pourrais vivre
- Une confiance en soi accrue
- Des opportunités concrètes
- Une envie de croissance

## Conseils pour ce transit
- Ose sortir de ta zone de confort
- Saisis les opportunités
- Équilibre optimisme et réalisme""",

    ('capricorn', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont favorisées – période de construction.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances. Les revenus peuvent augmenter de façon durable.

## Ce que tu pourrais vivre
- Une amélioration financière solide
- Des opportunités de croissance
- Une reconnaissance de ta valeur

## Conseils pour ce transit
- Construis ta richesse durablement
- Valorise tes compétences
- Évite les excès""",

    ('capricorn', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis – période d'expansion.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel. Les échanges sont fructueux et constructifs.

## Ce que tu pourrais vivre
- Des apprentissages utiles
- Des communications efficaces
- Des relations de proximité enrichies

## Conseils pour ce transit
- Apprends des choses pratiques
- Communique stratégiquement
- Enrichis tes relations""",

    ('capricorn', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis par l'expansion.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et améliorations à ta vie domestique. Période favorable pour construire des fondations solides.

## Ce que tu pourrais vivre
- Des améliorations du foyer
- Des joies familiales
- Un sentiment de sécurité

## Conseils pour ce transit
- Construis des fondations solides
- Cultive l'harmonie familiale
- Renforce tes racines""",

    ('capricorn', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour et la créativité sont favorisés – période de joie méritée.

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance à l'amour et la créativité. Les romances et projets créatifs sont bénis.

## Ce que tu pourrais vivre
- Une romance épanouissante
- Des succès créatifs
- Des moments de bonheur mérités

## Conseils pour ce transit
- Ouvre-toi à l'amour
- Exprime ta créativité
- Profite des plaisirs""",

    ('capricorn', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent – période de productivité.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail et à la santé. Les opportunités professionnelles arrivent.

## Ce que tu pourrais vivre
- De meilleures conditions de travail
- Des opportunités professionnelles
- Une santé renforcée

## Conseils pour ce transit
- Excelle dans ton travail
- Améliore ta santé
- Sers avec efficacité""",

    ('capricorn', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies – période propice aux partenariats solides.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance à toutes tes relations. Les rencontres et partenariats sont favorisés.

## Ce que tu pourrais vivre
- Une rencontre significative
- Un engagement durable
- Des partenariats solides

## Conseils pour ce transit
- Sois ouvert(e) aux relations
- Engage-toi avec sagesse
- Construis des partenariats durables""",

    ('capricorn', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation positive
- Une intimité enrichie

## Conseils pour ce transit
- Gère bien les finances communes
- Accepte la transformation
- Explore les profondeurs""",

    ('capricorn', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et expansion sont favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie d'expansion! Voyages et études sont magnifiés.

## Ce que tu pourrais vivre
- Des voyages enrichissants
- Des succès académiques
- Une expansion de ta vision

## Conseils pour ce transit
- Voyage stratégiquement
- Entreprends des formations
- Élargis tes horizons""",

    ('capricorn', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont exceptionnellement bénies!

## L'énergie du moment
Jupiter traverse ta maison X, ta maison naturelle! C'est une période exceptionnelle pour ta carrière. Les promotions et la reconnaissance arrivent.

## Ce que tu pourrais vivre
- Une promotion ou avancement majeur
- Une reconnaissance publique importante
- L'atteinte de tes plus grands objectifs

## Conseils pour ce transit
- Vise le sommet
- Accepte les grandes responsabilités
- Construis ta réputation""",

    ('capricorn', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale. Les amitiés et les espoirs sont favorisés.

## Ce que tu pourrais vivre
- Des amitiés de qualité
- La réalisation de souhaits
- Un réseau élargi

## Conseils pour ce transit
- Cultive des amitiés utiles
- Planifie tes projets d'avenir
- Rêve avec structure""",

    ('capricorn', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle
- Des aides inattendues

## Conseils pour ce transit
- Médite et planifie
- Guéris tes blessures
- Prépare l'avenir en silence""",

    # ============== AQUARIUS ==============
    ('aquarius', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle et opportunités innovantes t'attendent.

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ton développement. Ta confiance augmente, les opportunités arrivent de façon originale.

## Ce que tu pourrais vivre
- Une confiance en soi renforcée
- Des opportunités innovantes
- Une envie de renouveau original

## Conseils pour ce transit
- Ose l'innovation personnelle
- Saisis les opportunités uniques
- Rayonne avec originalité""",

    ('aquarius', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont favorisées de façon innovante.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances par des voies originales.

## Ce que tu pourrais vivre
- Des revenus par l'innovation
- Des opportunités financières uniques
- Une reconnaissance de ta valeur originale

## Conseils pour ce transit
- Développe des revenus innovants
- Valorise tes idées originales
- Évite les excès""",

    ('aquarius', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis avec originalité.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel de façon avant-gardiste. Les échanges sont stimulants.

## Ce que tu pourrais vivre
- Des apprentissages innovants
- Des communications avant-gardistes
- Des relations de proximité originales

## Conseils pour ce transit
- Apprends les technologies nouvelles
- Communique tes idées originales
- Explore ton environnement""",

    ('aquarius', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis par l'expansion innovante.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et modernisation à ta vie domestique.

## Ce que tu pourrais vivre
- Une modernisation du foyer
- Des dynamiques familiales nouvelles
- Un sentiment de liberté chez toi

## Conseils pour ce transit
- Modernise ton espace
- Réinvente les liens familiaux
- Crée un chez-toi unique""",

    ('aquarius', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour et la créativité sont favorisés de façon originale.

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance à l'amour et la créativité avec originalité. Les romances sont atypiques, les projets créatifs innovants.

## Ce que tu pourrais vivre
- Une romance originale
- Des succès créatifs innovants
- Des moments de bonheur unique

## Conseils pour ce transit
- Vis l'amour différemment
- Crée de façon avant-gardiste
- Profite des plaisirs uniques""",

    ('aquarius', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent avec innovation.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail et à la santé par des méthodes nouvelles.

## Ce que tu pourrais vivre
- Des opportunités de travail innovantes
- Des approches santé nouvelles
- Une efficacité originale

## Conseils pour ce transit
- Innove dans ton travail
- Explore des approches santé alternatives
- Sers avec originalité""",

    ('aquarius', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies avec originalité.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance à tes relations de façon unique. Les rencontres sont atypiques.

## Ce que tu pourrais vivre
- Des rencontres originales
- Des engagements non-conventionnels
- Des partenariats innovants

## Conseils pour ce transit
- Sois ouvert(e) aux relations atypiques
- Engage-toi de façon unique
- Collabore avec des innovateurs""",

    ('aquarius', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées avec innovation.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées par des voies nouvelles.

## Ce que tu pourrais vivre
- Des gains par des méthodes innovantes
- Une transformation originale
- Une intimité unique

## Conseils pour ce transit
- Gère les finances avec innovation
- Accepte la transformation unique
- Explore les profondeurs différemment""",

    ('aquarius', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et expansion sont favorisés avec avant-gardisme!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie d'expansion! Voyages vers des lieux innovants et études futuristes sont magnifiés.

## Ce que tu pourrais vivre
- Des voyages vers des lieux uniques
- Des études d'avant-garde
- Une expansion de ta vision du futur

## Conseils pour ce transit
- Voyage vers l'innovation
- Étudie le futur
- Explore de nouvelles philosophies""",

    ('aquarius', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont bénies avec originalité.

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance à ta vie professionnelle par des voies innovantes.

## Ce que tu pourrais vivre
- Une avancée professionnelle innovante
- Une reconnaissance de ton originalité
- L'atteinte d'objectifs uniques

## Conseils pour ce transit
- Vise des objectifs innovants
- Accepte des responsabilités uniques
- Rayonne avec originalité""",

    ('aquarius', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir sont exceptionnellement bénis!

## L'énergie du moment
Jupiter traverse ta maison XI, ta maison naturelle! C'est une période exceptionnelle pour ta vie sociale et tes projets humanitaires.

## Ce que tu pourrais vivre
- Des amitiés remarquables
- La réalisation de grands souhaits
- Un réseau mondial

## Conseils pour ce transit
- Élargis ton cercle social
- Engage-toi pour l'humanité
- Rêve l'avenir""",

    ('aquarius', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure innovante.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle par des voies nouvelles.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle unique
- Des aides inattendues

## Conseils pour ce transit
- Médite de façon innovante
- Guéris par des méthodes nouvelles
- Fais confiance au futur""",

    # ============== PISCES ==============
    ('pisces', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle et opportunités t'accueillent avec bienveillance.

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ton développement. Ta confiance augmente avec douceur.

## Ce que tu pourrais vivre
- Une confiance en soi renforcée
- Des opportunités bienveillantes
- Une envie de renouveau inspiré

## Conseils pour ce transit
- Ose te montrer
- Accueille les opportunités avec foi
- Rayonne avec compassion""",

    ('pisces', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont favorisées avec grâce.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances souvent par des voies intuitives.

## Ce que tu pourrais vivre
- Des revenus par des voies inspirées
- Des opportunités financières providentielles
- Une reconnaissance de ta valeur artistique

## Conseils pour ce transit
- Développe des revenus inspirés
- Valorise tes talents artistiques
- Évite les excès""",

    ('pisces', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis avec inspiration.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel avec intuition. Les échanges sont inspirants.

## Ce que tu pourrais vivre
- Des apprentissages spirituels
- Des communications inspirées
- Des relations de proximité profondes

## Conseils pour ce transit
- Apprends avec intuition
- Communique avec le cœur
- Enrichis tes relations""",

    ('pisces', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis par la grâce.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et bénédictions spirituelles à ta vie domestique.

## Ce que tu pourrais vivre
- Un foyer sanctuaire
- Des guérisons familiales
- Un sentiment de paix profonde

## Conseils pour ce transit
- Crée un sanctuaire
- Guéris les liens familiaux
- Renforce tes racines spirituelles""",

    ('pisces', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour et la créativité sont magnifiquement favorisés avec inspiration.

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance à l'amour et la créativité avec grâce. Les romances sont transcendantes, les projets créatifs inspirés.

## Ce que tu pourrais vivre
- Une romance spirituelle
- Des succès créatifs inspirés
- Des moments de bonheur transcendant

## Conseils pour ce transit
- Vis l'amour avec l'âme
- Crée depuis l'inspiration
- Profite des plaisirs spirituels""",

    ('pisces', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent avec grâce.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail et à la santé par des voies holistiques.

## Ce que tu pourrais vivre
- Un travail plus inspiré
- Des approches santé holistiques
- Un service compassionnel

## Conseils pour ce transit
- Travaille avec inspiration
- Prends soin de toi holistiquement
- Sers avec compassion""",

    ('pisces', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies avec profondeur spirituelle.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance à tes relations avec une dimension spirituelle. Les rencontres sont d'âme.

## Ce que tu pourrais vivre
- Une rencontre d'âme
- Un engagement spirituel
- Des partenariats inspirés

## Conseils pour ce transit
- Sois ouvert(e) aux connexions d'âme
- Engage-toi avec le cœur
- Collabore avec des êtres inspirés""",

    ('pisces', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées avec profondeur.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées avec dimension spirituelle.

## Ce que tu pourrais vivre
- Des gains par des voies intuitives
- Une transformation spirituelle
- Une intimité transcendante

## Conseils pour ce transit
- Gère les finances avec intuition
- Accepte la transformation spirituelle
- Explore les profondeurs de l'âme""",

    ('pisces', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et quête spirituelle sont exceptionnellement favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie d'expansion! Voyages spirituels et études mystiques sont magnifiés.

## Ce que tu pourrais vivre
- Des voyages initiatiques
- Des études spirituelles profondes
- Une expansion de la conscience

## Conseils pour ce transit
- Voyage vers le sacré
- Étudie les mystères
- Explore ta spiritualité""",

    ('pisces', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont bénies avec inspiration.

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance à ta vie professionnelle avec une touche artistique ou spirituelle.

## Ce que tu pourrais vivre
- Une avancée dans un domaine créatif
- Une reconnaissance de tes dons
- L'atteinte d'objectifs inspirés

## Conseils pour ce transit
- Vise des objectifs inspirés
- Accepte ta mission
- Rayonne avec compassion""",

    ('pisces', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent avec profondeur.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale avec dimension spirituelle. Les amitiés sont d'âme.

## Ce que tu pourrais vivre
- Des amitiés spirituelles
- La réalisation de souhaits inspirés
- Un réseau compassionnel

## Conseils pour ce transit
- Cultive des amitiés d'âme
- Engage-toi pour des causes humanitaires
- Rêve un monde meilleur""",

    ('pisces', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure exceptionnelles!

## L'énergie du moment
Jupiter traverse ta maison XII, ta maison naturelle (avec Neptune)! C'est une période exceptionnelle de grâce, protection et croissance spirituelle profonde.

## Ce que tu pourrais vivre
- Une protection divine
- Une croissance spirituelle majeure
- Des aides providentielles

## Conseils pour ce transit
- Médite profondément
- Guéris avec l'amour universel
- Fais confiance à la grâce divine""",
}

async def insert_interpretations():
    """Insert transit Jupiter interpretations into database."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_JUPITER_INTERPRETATIONS.items():
            # Check if already exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_jupiter',
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
                subject='transit_jupiter',
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
        print(f"✅ Transit Jupiter (Sagittarius, Capricorn, Aquarius, Pisces)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
