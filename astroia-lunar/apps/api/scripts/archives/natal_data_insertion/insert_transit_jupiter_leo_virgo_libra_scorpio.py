#!/usr/bin/env python3
"""Insert transit_jupiter interpretations for Leo, Virgo, Libra, Scorpio (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_JUPITER_INTERPRETATIONS = {
    # ============== LEO ==============
    ('leo', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle royale – tu rayonnes et les opportunités affluent!

## L'énergie du moment
Jupiter traverse ta maison I, amplifiant ta présence naturelle et ton charisme. Ta confiance est au maximum, les portes s'ouvrent devant toi. C'est le moment de briller et de te lancer dans de grands projets.

## Ce que tu pourrais vivre
- Un charisme et une confiance décuplés
- Des opportunités remarquables
- Une envie de conquête positive

## Conseils pour ce transit
- Brille et montre-toi
- Saisis les grandes opportunités
- Attention à l'excès d'orgueil""",

    ('leo', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont magnifiquement favorisées.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et abondance à tes finances. Les revenus peuvent augmenter significativement, ta valeur est reconnue et récompensée.

## Ce que tu pourrais vivre
- Une augmentation notable des revenus
- Des opportunités financières prestigieuses
- Une reconnaissance de ta valeur royale

## Conseils pour ce transit
- Investis dans ce qui te valorise
- Demande ce que tu mérites
- Évite les dépenses de prestige excessives""",

    ('leo', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis – ton éloquence brille!

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel avec panache. Tes communications sont remarquées, tes idées sont appréciées.

## Ce que tu pourrais vivre
- Un succès dans la communication
- Des apprentissages stimulants
- Des relations de proximité enrichies

## Conseils pour ce transit
- Exprime tes idées avec conviction
- Apprends et enseigne
- Rayonne dans ton environnement""",

    ('leo', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis par l'expansion.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et bénédictions à ta vie domestique. Période favorable pour créer un foyer digne de toi.

## Ce que tu pourrais vivre
- Un agrandissement ou amélioration du foyer
- Des joies familiales
- Un sentiment de sécurité royale

## Conseils pour ce transit
- Crée un foyer qui te ressemble
- Cultive l'harmonie familiale
- Renforce tes fondations""",

    ('leo', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour, la créativité et les plaisirs sont exceptionnellement magnifiés!

## L'énergie du moment
Jupiter traverse ta maison V, ta maison naturelle! C'est une période exceptionnelle pour l'amour, la créativité et la joie. Tout ce qui touche au plaisir et à l'expression personnelle est béni.

## Ce que tu pourrais vivre
- Une romance passionnante
- Des succès créatifs majeurs
- Des moments de bonheur royal

## Conseils pour ce transit
- Vis l'amour pleinement
- Crée avec magnificence
- Profite de chaque plaisir""",

    ('leo', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent – tu excelles au quotidien.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail et à la santé. Les opportunités professionnelles arrivent, ta vitalité rayonne.

## Ce que tu pourrais vivre
- De meilleures conditions de travail
- Des opportunités de briller au quotidien
- Une santé florissante

## Conseils pour ce transit
- Excelle dans ton travail quotidien
- Prends soin de ta santé
- Sois généreux avec les autres""",

    ('leo', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies – période royale pour les engagements.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance et croissance à toutes tes relations. Les rencontres sont significatives, les partenariats florissants.

## Ce que tu pourrais vivre
- Une rencontre remarquable
- Un engagement favorable
- Des partenariats prestigieux

## Conseils pour ce transit
- Sois ouvert(e) aux grandes relations
- Engage-toi avec noblesse
- Collabore avec des personnes de qualité""",

    ('leo', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées – croissance profonde.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées. Les transformations sont bénéfiques et royales.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation majestueuse
- Une intimité enrichie

## Conseils pour ce transit
- Gère les finances communes avec noblesse
- Accepte ta transformation
- Explore les profondeurs avec courage""",

    ('leo', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et quête de sens sont exceptionnellement favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie d'expansion! Voyages grandioses, études prestigieuses, exploration philosophique – tout est magnifié.

## Ce que tu pourrais vivre
- Des voyages mémorables
- Des succès académiques brillants
- Une expansion spirituelle majeure

## Conseils pour ce transit
- Voyage vers de grands horizons
- Entreprends des études prestigieuses
- Explore de nouvelles philosophies""",

    ('leo', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont exceptionnellement bénies – vise le trône!

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance et expansion maximale à ta vie professionnelle. C'est le moment de viser le sommet et d'atteindre la reconnaissance.

## Ce que tu pourrais vivre
- Une promotion ou avancement majeur
- Une reconnaissance publique importante
- L'atteinte de tes plus grands objectifs

## Conseils pour ce transit
- Vise le plus haut niveau
- Accepte les grandes responsabilités
- Rayonne dans ta carrière""",

    ('leo', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent royalement.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale et tes rêves. Les amitiés prestigieuses se multiplient, tes grands souhaits se réalisent.

## Ce que tu pourrais vivre
- Des amitiés de qualité
- La réalisation de grands souhaits
- Un réseau élargi et prestigieux

## Conseils pour ce transit
- Cultive des amitiés nobles
- Engage-toi dans des causes importantes
- Rêve en grand""",

    ('leo', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure – période de grâce secrète.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle. Période favorable pour le travail intérieur et la guérison.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle profonde
- Des aides inattendues

## Conseils pour ce transit
- Médite et explore ta spiritualité
- Guéris tes blessures royales
- Fais confiance à la grâce""",

    # ============== VIRGO ==============
    ('virgo', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle et opportunités nouvelles t'accueillent.

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ton développement. Ta confiance augmente, les opportunités se présentent de façon ordonnée.

## Ce que tu pourrais vivre
- Une confiance en soi accrue
- Des opportunités concrètes
- Une envie de croissance personnelle

## Conseils pour ce transit
- Ose sortir de ta zone de confort
- Accueille les opportunités
- Équilibre analyse et action""",

    ('virgo', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont favorisées – période d'amélioration.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances. Les revenus peuvent augmenter grâce à tes compétences.

## Ce que tu pourrais vivre
- Une amélioration des revenus
- Des opportunités financières concrètes
- Une reconnaissance de tes talents

## Conseils pour ce transit
- Développe tes compétences rentables
- Valorise tes talents pratiques
- Évite les excès""",

    ('virgo', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis – période d'expansion intellectuelle.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel de façon pratique. Les échanges sont fructueux, les apprentissages utiles.

## Ce que tu pourrais vivre
- Des apprentissages enrichissants
- Des communications réussies
- Des relations de proximité améliorées

## Conseils pour ce transit
- Apprends des choses pratiques
- Communique efficacement
- Enrichis tes relations proches""",

    ('virgo', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis par l'expansion.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et améliorations à ta vie domestique. Période favorable pour optimiser ton chez-toi.

## Ce que tu pourrais vivre
- Des améliorations pratiques du foyer
- Des joies familiales
- Un sentiment de sécurité

## Conseils pour ce transit
- Améliore ton chez-toi
- Organise l'harmonie familiale
- Renforce tes fondations""",

    ('virgo', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour et la créativité sont favorisés – période de joie.

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance à l'amour et la créativité. Les romances et les projets créatifs sont bénis.

## Ce que tu pourrais vivre
- Une romance épanouissante
- Des succès créatifs
- Des moments de bonheur

## Conseils pour ce transit
- Ouvre-toi à l'amour
- Exprime ta créativité
- Profite des plaisirs simples""",

    ('virgo', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé sont exceptionnellement favorisés!

## L'énergie du moment
Jupiter traverse ta maison VI, ta maison naturelle! C'est une période exceptionnelle pour le travail et la santé. Tout ce qui touche au quotidien est béni.

## Ce que tu pourrais vivre
- Des opportunités professionnelles majeures
- Une santé florissante
- Une efficacité remarquable

## Conseils pour ce transit
- Excelle dans ton travail
- Optimise ta santé
- Sers avec générosité""",

    ('virgo', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies – période propice aux partenariats.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance à toutes tes relations. Les rencontres et partenariats sont favorisés.

## Ce que tu pourrais vivre
- Une rencontre significative
- Un engagement favorable
- Des collaborations fructueuses

## Conseils pour ce transit
- Sois ouvert(e) aux relations
- Engage-toi avec discernement
- Collabore efficacement""",

    ('virgo', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées. Les transformations sont bénéfiques.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation positive
- Une intimité améliorée

## Conseils pour ce transit
- Gère bien les finances communes
- Accepte la transformation
- Analyse les profondeurs""",

    ('virgo', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et expansion sont favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie d'expansion! Voyages, études, quête de sens – tout est magnifié.

## Ce que tu pourrais vivre
- Des voyages enrichissants
- Des succès académiques
- Une expansion de tes connaissances

## Conseils pour ce transit
- Voyage et apprends
- Entreprends des formations
- Explore de nouvelles idées""",

    ('virgo', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière est bénie – période de réussite professionnelle.

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance et expansion à ta vie professionnelle. Les promotions et la reconnaissance sont favorisées.

## Ce que tu pourrais vivre
- Une avancée professionnelle
- Une reconnaissance de ton travail
- L'atteinte de tes objectifs

## Conseils pour ce transit
- Vise l'excellence
- Accepte les responsabilités
- Profite de ta réputation""",

    ('virgo', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale. Les amitiés et les espoirs sont favorisés.

## Ce que tu pourrais vivre
- Des amitiés de qualité
- La réalisation de souhaits
- Un réseau élargi

## Conseils pour ce transit
- Cultive des amitiés utiles
- Engage-toi dans des groupes
- Planifie tes rêves""",

    ('virgo', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle. Période favorable pour le travail intérieur.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle
- Des aides inattendues

## Conseils pour ce transit
- Médite et analyse ton intérieur
- Guéris tes blessures
- Fais confiance""",

    # ============== LIBRA ==============
    ('libra', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle et opportunités t'attendent avec générosité.

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ton développement. Ta confiance augmente, les opportunités arrivent harmonieusement.

## Ce que tu pourrais vivre
- Une confiance en soi renforcée
- Des opportunités équilibrées
- Une envie de renouveau

## Conseils pour ce transit
- Ose t'affirmer
- Accueille les opportunités
- Équilibre expansion et harmonie""",

    ('libra', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont favorisées.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances. Les revenus peuvent augmenter, ta valeur est reconnue.

## Ce que tu pourrais vivre
- Une amélioration des revenus
- Des opportunités financières
- Une reconnaissance de ta valeur

## Conseils pour ce transit
- Développe tes ressources
- Valorise tes talents esthétiques
- Évite les excès""",

    ('libra', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel avec élégance. Les échanges sont fructueux et harmonieux.

## Ce que tu pourrais vivre
- Des apprentissages enrichissants
- Des communications réussies
- Des relations de proximité embellies

## Conseils pour ce transit
- Communique avec grâce
- Apprends l'art et la diplomatie
- Enrichis tes relations""",

    ('libra', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et harmonie à ta vie domestique. Période favorable pour embellir ton chez-toi.

## Ce que tu pourrais vivre
- Un embellissement du foyer
- Des joies familiales
- Un sentiment d'harmonie

## Conseils pour ce transit
- Crée un chez-toi harmonieux
- Cultive la paix familiale
- Renforce tes racines""",

    ('libra', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour et la créativité sont magnifiquement favorisés.

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance à l'amour et la créativité. Les romances sont belles, les projets créatifs florissent.

## Ce que tu pourrais vivre
- Une romance élégante
- Des succès artistiques
- Des moments de beauté

## Conseils pour ce transit
- Ouvre-toi à l'amour beau
- Exprime ta créativité artistique
- Savoure l'harmonie""",

    ('libra', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent harmonieusement.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail et à la santé. L'équilibre quotidien est favorisé.

## Ce que tu pourrais vivre
- De meilleures conditions de travail
- Une santé équilibrée
- Des relations professionnelles améliorées

## Conseils pour ce transit
- Équilibre travail et bien-être
- Crée l'harmonie au travail
- Prends soin de toi""",

    ('libra', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont exceptionnellement bénies!

## L'énergie du moment
Jupiter traverse ta maison VII, ta maison naturelle! C'est une période exceptionnelle pour toutes tes relations. L'amour et les partenariats sont magnifiés.

## Ce que tu pourrais vivre
- Une rencontre significative
- Un engagement favorable
- Des partenariats harmonieux

## Conseils pour ce transit
- Sois ouvert(e) à l'amour
- Engage-toi avec joie
- Cultive l'harmonie relationnelle""",

    ('libra', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation équilibrée
- Une intimité enrichie

## Conseils pour ce transit
- Partage équitablement
- Accepte la transformation
- Explore avec harmonie""",

    ('libra', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et expansion sont favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie d'expansion! Voyages culturels et études artistiques sont magnifiés.

## Ce que tu pourrais vivre
- Des voyages culturels enrichissants
- Des succès dans les études
- Une expansion esthétique

## Conseils pour ce transit
- Voyage vers la beauté
- Étudie l'art et la culture
- Explore l'harmonie universelle""",

    ('libra', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont bénies.

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance à ta vie professionnelle. La reconnaissance arrive avec grâce.

## Ce que tu pourrais vivre
- Une avancée professionnelle
- Une reconnaissance publique
- L'atteinte de tes objectifs

## Conseils pour ce transit
- Vise l'excellence avec élégance
- Accepte les responsabilités
- Rayonne dans ta carrière""",

    ('libra', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent harmonieusement.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale. Les amitiés et les espoirs sont bénis.

## Ce que tu pourrais vivre
- Des amitiés harmonieuses
- La réalisation de souhaits
- Un réseau élargi

## Conseils pour ce transit
- Cultive des amitiés belles
- Engage-toi dans des causes justes
- Rêve l'harmonie""",

    ('libra', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle
- Des aides inattendues

## Conseils pour ce transit
- Médite sur la beauté intérieure
- Guéris tes blessures
- Fais confiance à l'harmonie""",

    # ============== SCORPIO ==============
    ('scorpio', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle puissante – tu te transformes positivement!

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ta transformation personnelle. Ta présence magnétique est amplifiée, les opportunités arrivent.

## Ce que tu pourrais vivre
- Une présence décuplée
- Des opportunités transformatrices
- Une envie de renouveau profond

## Conseils pour ce transit
- Transforme-toi positivement
- Saisis les opportunités de pouvoir
- Canalise cette expansion""",

    ('scorpio', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont intensément favorisées.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances. Les ressources peuvent augmenter significativement.

## Ce que tu pourrais vivre
- Une augmentation des revenus
- Des opportunités financières
- Une reconnaissance de ta valeur

## Conseils pour ce transit
- Développe tes ressources stratégiquement
- Valorise tes talents profonds
- Évite les excès de pouvoir financier""",

    ('scorpio', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis avec profondeur.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel avec intensité. Les échanges sont profonds et fructueux.

## Ce que tu pourrais vivre
- Des apprentissages profonds
- Des communications percutantes
- Des relations de proximité transformées

## Conseils pour ce transit
- Communique avec profondeur
- Apprends les mystères
- Enrichis tes relations""",

    ('scorpio', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis par la transformation.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et transformation à ta vie domestique.

## Ce que tu pourrais vivre
- Une transformation du foyer
- Des guérisons familiales
- Un sentiment de sécurité profonde

## Conseils pour ce transit
- Transforme ton chez-toi
- Guéris les blessures familiales
- Renforce tes racines""",

    ('scorpio', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour et la créativité sont intensément favorisés.

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance à l'amour et la créativité avec intensité. Les passions sont magnifiées.

## Ce que tu pourrais vivre
- Une romance passionnée
- Des succès créatifs profonds
- Des moments de bonheur intense

## Conseils pour ce transit
- Vis l'amour intensément
- Crée depuis tes profondeurs
- Savoure les plaisirs""",

    ('scorpio', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent avec profondeur.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail et à la santé. La transformation quotidienne est favorisée.

## Ce que tu pourrais vivre
- Des opportunités de transformation au travail
- Une régénération de la santé
- Une efficacité profonde

## Conseils pour ce transit
- Transforme ton quotidien
- Régénère ta santé
- Sers avec intensité""",

    ('scorpio', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies avec intensité.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance à tes relations. Les rencontres sont transformatrices.

## Ce que tu pourrais vivre
- Une rencontre intense
- Un engagement profond
- Des partenariats transformateurs

## Conseils pour ce transit
- Sois ouvert(e) aux relations profondes
- Engage-toi avec intensité
- Transforme tes partenariats""",

    ('scorpio', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont exceptionnellement favorisées!

## L'énergie du moment
Jupiter traverse ta maison VIII, ta maison naturelle! C'est une période exceptionnelle pour la transformation, les finances partagées et l'intimité.

## Ce que tu pourrais vivre
- Des gains significatifs par les ressources partagées
- Une transformation majeure
- Une intimité transcendante

## Conseils pour ce transit
- Gère les finances avec sagesse
- Accepte ta grande transformation
- Explore les profondeurs""",

    ('scorpio', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et quête de vérité sont favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie d'expansion! Voyages initiatiques et quête de vérité sont magnifiés.

## Ce que tu pourrais vivre
- Des voyages transformateurs
- Des études ésotériques
- Une expansion spirituelle

## Conseils pour ce transit
- Voyage vers les mystères
- Étudie les profondeurs
- Explore la vérité""",

    ('scorpio', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont bénies avec puissance.

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance et expansion à ta vie professionnelle avec intensité.

## Ce que tu pourrais vivre
- Une avancée professionnelle majeure
- Une reconnaissance de ton pouvoir
- L'atteinte de tes objectifs

## Conseils pour ce transit
- Vise le pouvoir avec sagesse
- Accepte les grandes responsabilités
- Rayonne avec intensité""",

    ('scorpio', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent intensément.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale avec profondeur.

## Ce que tu pourrais vivre
- Des amitiés intenses
- La réalisation de souhaits profonds
- Un réseau puissant

## Conseils pour ce transit
- Cultive des amitiés profondes
- Engage-toi pour des causes transformatrices
- Rêve grand""",

    ('scorpio', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure profonde.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle intense.

## Ce que tu pourrais vivre
- Une protection puissante
- Une croissance spirituelle majeure
- Des aides transformatrices

## Conseils pour ce transit
- Médite sur tes profondeurs
- Guéris tes blessures karmiques
- Fais confiance à la transformation""",
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
        print(f"✅ Transit Jupiter (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
