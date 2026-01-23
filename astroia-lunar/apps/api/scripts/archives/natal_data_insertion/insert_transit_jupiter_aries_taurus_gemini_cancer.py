#!/usr/bin/env python3
"""Insert transit_jupiter interpretations for Aries, Taurus, Gemini, Cancer (V2)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_JUPITER_INTERPRETATIONS = {
    # ============== ARIES ==============
    ('aries', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Une période d'expansion personnelle exceptionnelle où tu peux te réinventer avec optimisme!

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de grande chance pour ton développement personnel. Tu rayonnes de confiance et d'optimisme. Les opportunités arrivent naturellement vers toi. C'est le moment idéal pour lancer de nouveaux projets et t'affirmer.

## Ce que tu pourrais vivre
- Une confiance en soi décuplée
- Des opportunités qui tombent du ciel
- Une envie de te réinventer positivement

## Conseils pour ce transit
- Ose entreprendre et te montrer
- Profite de cette période faste
- Attention à l'excès de confiance""",

    ('aries', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Une période bénie pour l'expansion financière et la valorisation de tes talents.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances. C'est une période favorable pour augmenter tes revenus, recevoir des bonus ou développer de nouvelles sources de richesse. Ta valeur personnelle est reconnue.

## Ce que tu pourrais vivre
- Une amélioration significative de tes revenus
- Des opportunités financières inattendues
- Une reconnaissance de ta valeur

## Conseils pour ce transit
- Investis dans tes talents
- Saisis les opportunités financières
- Évite les dépenses excessives par excès d'optimisme""",

    ('aries', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication, apprentissages et connexions locales s'enrichissent de façon remarquable.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton univers intellectuel et relationnel proche. Les échanges sont fructueux, les apprentissages passionnants. C'est excellent pour les études, l'écriture, et les relations avec les proches.

## Ce que tu pourrais vivre
- Des opportunités d'apprentissage enrichissantes
- Des rencontres stimulantes dans ton environnement
- Un succès dans la communication

## Conseils pour ce transit
- Apprends, écris, communique
- Renforce tes liens avec les proches
- Explore ton environnement local""",

    ('aries', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion et bénédictions pour ton foyer, ta famille et tes racines.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et protection à ta vie domestique. C'est une période favorable pour déménager vers plus grand, améliorer ton chez-toi, ou renforcer les liens familiaux. Un sentiment de sécurité émotionnelle t'enveloppe.

## Ce que tu pourrais vivre
- Un déménagement ou agrandissement favorable
- Des bénédictions familiales
- Un sentiment de sécurité intérieure

## Conseils pour ce transit
- Améliore ou agrandis ton chez-toi
- Investis dans ta famille
- Cultive tes racines""",

    ('aries', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Romance, créativité et joie de vivre sont magnifiées – profite pleinement!

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance et expansion à l'amour, la créativité et les plaisirs. Les romances sont favorisées, les projets créatifs florissent, les moments de joie se multiplient. Si tu veux des enfants, période propice.

## Ce que tu pourrais vivre
- Une romance épanouissante
- Un succès créatif ou artistique
- Des moments de bonheur intenses

## Conseils pour ce transit
- Ouvre-toi à l'amour et à la joie
- Lance tes projets créatifs
- Savoure chaque plaisir""",

    ('aries', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amélioration du quotidien, du travail et de la santé – tout s'aligne positivement.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations à ton travail quotidien et ta santé. Les opportunités professionnelles arrivent, l'ambiance au bureau s'améliore. Ta santé bénéficie aussi de cette influence protectrice.

## Ce que tu pourrais vivre
- Une amélioration de tes conditions de travail
- Des opportunités professionnelles
- Une meilleure santé et vitalité

## Conseils pour ce transit
- Accepte les nouvelles responsabilités
- Adopte de meilleures habitudes de vie
- Sois généreux avec tes collègues""",

    ('aries', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations et partenariats sont bénis – période idéale pour s'engager ou collaborer.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance et croissance à toutes tes relations importantes. Si tu es célibataire, une rencontre significative peut arriver. En couple, la relation s'épanouit. Les partenariats professionnels prospèrent.

## Ce que tu pourrais vivre
- Une rencontre importante ou un engagement
- L'épanouissement de ta relation existante
- Des partenariats fructueux

## Conseils pour ce transit
- Sois ouvert(e) aux relations significatives
- Engage-toi si le moment est venu
- Développe des collaborations""",

    ('aries', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation profonde, héritages et ressources partagées sont favorisés.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans les domaines de l'intimité, des finances partagées et de la transformation. Héritages, investissements, remboursements de dettes sont favorisés. Une guérison intérieure est possible.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation intérieure bénéfique
- Une intimité épanouissante

## Conseils pour ce transit
- Gère bien les finances partagées
- Accepte la transformation
- Explore les profondeurs avec confiance""",

    ('aries', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion maximale par les voyages, les études et la quête de sens – le monde t'appartient!

## L'énergie du moment
Jupiter traverse ta maison IX, SON domicile naturel! C'est une période exceptionnelle pour les voyages lointains, les études supérieures, et l'exploration philosophique ou spirituelle. Ta vision du monde s'élargit considérablement.

## Ce que tu pourrais vivre
- Des voyages inoubliables
- Un succès dans les études
- Une expansion spirituelle majeure

## Conseils pour ce transit
- Voyage le plus possible
- Lance-toi dans des études
- Explore de nouvelles philosophies""",

    ('aries', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation publique sont bénies – vise le sommet!

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance et expansion à ta vie professionnelle. C'est une période idéale pour les promotions, la reconnaissance publique, et l'atteinte de tes objectifs de carrière. Ta réputation brille.

## Ce que tu pourrais vivre
- Une promotion ou reconnaissance majeure
- L'atteinte d'objectifs professionnels
- Une amélioration de ta réputation

## Conseils pour ce transit
- Vise haut dans ta carrière
- Accepte les responsabilités accrues
- Profite de ta bonne réputation""",

    ('aries', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes amitiés, réseaux et espoirs pour l'avenir s'épanouissent magnifiquement.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale et tes projets d'avenir. Les amitiés se multiplient, ton réseau s'élargit, tes espoirs se concrétisent. L'engagement dans des causes te comble.

## Ce que tu pourrais vivre
- Des amitiés nouvelles et enrichissantes
- La réalisation de tes souhaits
- Un réseau qui s'élargit considérablement

## Conseils pour ce transit
- Élargis ton cercle social
- Engage-toi dans des groupes ou associations
- Ose rêver grand""",

    ('aries', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure – une période de grâce cachée.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant une protection invisible et une croissance spirituelle. C'est une période favorable pour la méditation, le travail sur soi, et la guérison d'anciennes blessures. Des aides inattendues peuvent arriver.

## Ce que tu pourrais vivre
- Une protection contre les difficultés
- Une croissance spirituelle profonde
- Des aides providentielles cachées

## Conseils pour ce transit
- Médite et explore ta spiritualité
- Fais confiance à l'univers
- Guéris tes blessures intérieures""",

    # ============== TAURUS ==============
    ('taurus', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle et nouvelles opportunités s'offrent à toi avec générosité.

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ton développement personnel. Ta confiance augmente, les opportunités se présentent naturellement. C'est le moment de te lancer dans de nouveaux projets avec optimisme.

## Ce que tu pourrais vivre
- Une confiance en soi accrue
- Des opportunités nouvelles
- Une envie de changement positif

## Conseils pour ce transit
- Ose sortir de ta zone de confort
- Accueille les nouvelles opportunités
- Rayonne avec confiance""",

    ('taurus', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur personnelle sont exceptionnellement favorisées.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances. C'est une période très favorable pour augmenter tes revenus, développer tes ressources et voir ta valeur reconnue. Les gains peuvent être significatifs.

## Ce que tu pourrais vivre
- Une augmentation de revenus importante
- Des opportunités financières favorables
- Une reconnaissance de tes talents

## Conseils pour ce transit
- Développe tes sources de revenus
- Investis dans tes talents
- Attention aux dépenses excessives""",

    ('taurus', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis – période d'expansion intellectuelle.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel et relationnel proche. Les échanges sont fructueux, les études favorisées, les rencontres locales enrichissantes. Excellent pour l'écriture et la communication.

## Ce que tu pourrais vivre
- Des apprentissages passionnants
- Des relations de proximité enrichies
- Un succès dans la communication

## Conseils pour ce transit
- Lance-toi dans des études ou formations
- Communique et partage tes idées
- Renforce tes liens avec les proches""",

    ('taurus', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta vie familiale sont bénis par l'expansion et la protection.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et bénédictions à ta vie domestique. Période favorable pour un déménagement, des améliorations de l'habitat, ou un renforcement des liens familiaux. Tu te sens en sécurité.

## Ce que tu pourrais vivre
- Un agrandissement ou amélioration du foyer
- Des joies familiales
- Un sentiment de sécurité profonde

## Conseils pour ce transit
- Investis dans ton chez-toi
- Cultive l'harmonie familiale
- Construis des fondations solides""",

    ('taurus', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour, la créativité et les plaisirs sont magnifiés – période de joie!

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance et expansion à ta vie amoureuse et créative. Les romances sont favorisées, les projets artistiques florissent, les plaisirs se multiplient. Période propice pour avoir des enfants.

## Ce que tu pourrais vivre
- Une belle romance ou un renouveau amoureux
- Des succès créatifs
- Des moments de pur bonheur

## Conseils pour ce transit
- Ouvre-toi à l'amour
- Exprime ta créativité
- Savoure les plaisirs de la vie""",

    ('taurus', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent notablement sous cette influence bénéfique.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations à ton quotidien professionnel et ta santé. Les opportunités de travail arrivent, les conditions s'améliorent. Ta vitalité bénéficie aussi de cette protection.

## Ce que tu pourrais vivre
- De meilleures conditions de travail
- Des opportunités professionnelles
- Une santé renforcée

## Conseils pour ce transit
- Accepte les nouvelles responsabilités
- Améliore tes habitudes de santé
- Sois généreux dans le service""",

    ('taurus', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies – période idéale pour les engagements et partenariats.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance et croissance à tes relations. Les rencontres significatives sont favorisées, les relations existantes s'épanouissent. Les partenariats prospèrent.

## Ce que tu pourrais vivre
- Une rencontre importante
- Un engagement ou mariage favorable
- Des partenariats fructueux

## Conseils pour ce transit
- Sois ouvert(e) aux relations
- Engage-toi si tu es prêt(e)
- Développe des collaborations""",

    ('taurus', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées – croissance profonde.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité, les finances partagées et la transformation personnelle. Héritages, investissements et remboursements sont favorisés.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation bénéfique
- Une intimité épanouie

## Conseils pour ce transit
- Gère bien les finances partagées
- Accepte la transformation
- Explore les profondeurs""",

    ('taurus', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et quête de sens sont exceptionnellement favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie naturelle d'expansion! Voyages lointains, études supérieures, exploration spirituelle – tout est favorisé. Ta vision du monde s'élargit considérablement.

## Ce que tu pourrais vivre
- Des voyages mémorables
- Des succès dans les études
- Une expansion de ta vision

## Conseils pour ce transit
- Voyage vers de nouveaux horizons
- Entreprends des études
- Explore de nouvelles philosophies""",

    ('taurus', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont bénies – période de réussite professionnelle.

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance et expansion à ta vie professionnelle. Promotions, reconnaissance, atteinte d'objectifs – tout est favorisé. Ta réputation s'améliore.

## Ce que tu pourrais vivre
- Une promotion ou avancement
- Une reconnaissance publique
- L'atteinte de tes objectifs

## Conseils pour ce transit
- Vise haut professionnellement
- Accepte les responsabilités
- Profite de ta bonne réputation""",

    ('taurus', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent – tes souhaits peuvent se réaliser.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale et tes rêves. Les amitiés se multiplient, ton réseau s'élargit, tes espoirs se concrétisent.

## Ce que tu pourrais vivre
- Des amitiés nouvelles et précieuses
- La réalisation de souhaits
- Un réseau élargi

## Conseils pour ce transit
- Cultive tes amitiés
- Engage-toi dans des groupes
- Ose rêver grand""",

    ('taurus', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure – période de grâce secrète.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle. Période favorable pour la méditation, la guérison intérieure, et le travail sur l'inconscient.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle
- Des aides inattendues

## Conseils pour ce transit
- Médite et explore ta spiritualité
- Guéris tes blessures anciennes
- Fais confiance au processus""",

    # ============== GEMINI ==============
    ('gemini', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle et opportunités nouvelles t'attendent avec enthousiasme.

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ton développement personnel. Ta confiance et ton optimisme augmentent naturellement. C'est le moment de te lancer dans de nouvelles aventures.

## Ce que tu pourrais vivre
- Une confiance en soi rayonnante
- Des opportunités multiples
- Une envie de renouveau

## Conseils pour ce transit
- Lance-toi dans tes projets
- Accueille les opportunités
- Rayonne avec optimisme""",

    ('gemini', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont favorisées – période d'abondance potentielle.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances et ta valeur personnelle. Les revenus peuvent augmenter, les opportunités financières se multiplient.

## Ce que tu pourrais vivre
- Une amélioration des revenus
- Des opportunités financières
- Une reconnaissance de ta valeur

## Conseils pour ce transit
- Développe tes ressources
- Valorise tes talents
- Évite les excès de dépenses""",

    ('gemini', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont exceptionnellement bénis!

## L'énergie du moment
Jupiter traverse ta maison III, ta maison naturelle! C'est une période exceptionnelle pour la communication, les échanges intellectuels et les apprentissages. Tout ce qui touche aux mots et aux idées est favorisé.

## Ce que tu pourrais vivre
- Un succès dans la communication
- Des apprentissages passionnants
- Des relations de proximité enrichies

## Conseils pour ce transit
- Communique, écris, enseigne
- Apprends avec passion
- Explore ton environnement""",

    ('gemini', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont bénis par l'expansion et la protection.

## L'énergie du moment
Jupiter traverse ta maison IV, apportant croissance et bénédictions à ta vie domestique et familiale. Période favorable pour le foyer et les liens familiaux.

## Ce que tu pourrais vivre
- Un agrandissement ou amélioration du foyer
- Des joies familiales
- Un sentiment de sécurité

## Conseils pour ce transit
- Améliore ton chez-toi
- Cultive l'harmonie familiale
- Renforce tes racines""",

    ('gemini', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour, la créativité et les plaisirs sont magnifiés – vis pleinement!

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance et expansion à l'amour et la créativité. Les romances sont favorisées, les projets créatifs florissent.

## Ce que tu pourrais vivre
- Une romance épanouissante
- Des succès créatifs
- Des moments de bonheur

## Conseils pour ce transit
- Ouvre-toi à l'amour
- Exprime ta créativité
- Profite des plaisirs""",

    ('gemini', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent sous cette influence protectrice.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail quotidien et à la santé. Les opportunités professionnelles arrivent, la vitalité augmente.

## Ce que tu pourrais vivre
- De meilleures conditions de travail
- Des opportunités professionnelles
- Une santé améliorée

## Conseils pour ce transit
- Saisis les opportunités au travail
- Améliore tes habitudes de santé
- Sois généreux avec les autres""",

    ('gemini', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations et partenariats sont bénis – période propice aux engagements.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance et croissance à toutes tes relations importantes. Les rencontres significatives et les partenariats sont favorisés.

## Ce que tu pourrais vivre
- Une rencontre significative
- Un engagement favorable
- Des partenariats fructueux

## Conseils pour ce transit
- Sois ouvert(e) aux relations
- Engage-toi si tu es prêt(e)
- Collabore avec confiance""",

    ('gemini', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées – croissance profonde.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées. Les héritages et transformations sont favorisés.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation positive
- Une intimité enrichie

## Conseils pour ce transit
- Gère bien les finances communes
- Accepte de te transformer
- Explore les profondeurs""",

    ('gemini', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et expansion spirituelle sont exceptionnellement favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie naturelle! Voyages lointains, études supérieures, quête de sens – tout est magnifié. Ta vision s'élargit.

## Ce que tu pourrais vivre
- Des voyages transformateurs
- Des succès académiques
- Une expansion spirituelle

## Conseils pour ce transit
- Voyage vers de nouveaux horizons
- Entreprends des études
- Explore de nouvelles idées""",

    ('gemini', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont bénies – vise le succès!

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance et expansion à ta vie professionnelle. Les promotions et la reconnaissance sont favorisées.

## Ce que tu pourrais vivre
- Une avancée professionnelle
- Une reconnaissance publique
- L'atteinte de tes objectifs

## Conseils pour ce transit
- Vise haut dans ta carrière
- Accepte les responsabilités
- Profite de ta réputation""",

    ('gemini', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent – tes rêves peuvent se réaliser.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale et tes espoirs. Les amitiés se multiplient, tes souhaits se concrétisent.

## Ce que tu pourrais vivre
- Des amitiés nouvelles
- La réalisation de souhaits
- Un réseau élargi

## Conseils pour ce transit
- Élargis ton cercle social
- Engage-toi dans des groupes
- Rêve grand""",

    ('gemini', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure – période de grâce.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle. Période favorable pour le travail intérieur et la guérison.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle
- Des aides inattendues

## Conseils pour ce transit
- Médite et explore ta spiritualité
- Guéris tes blessures
- Fais confiance""",

    # ============== CANCER ==============
    ('cancer', 1): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Expansion personnelle et opportunités nouvelles t'accueillent avec bienveillance.

## L'énergie du moment
Jupiter traverse ta maison I, ouvrant une période de chance pour ton développement personnel. Ta confiance augmente, les portes s'ouvrent naturellement. C'est le moment de te renouveler.

## Ce que tu pourrais vivre
- Une confiance en soi renforcée
- Des opportunités nouvelles
- Une envie de te réinventer

## Conseils pour ce transit
- Ose te lancer
- Accueille les opportunités
- Rayonne avec assurance""",

    ('cancer', 2): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes finances et ta valeur sont favorisées – période d'abondance.

## L'énergie du moment
Jupiter traverse ta maison II, apportant chance et croissance à tes finances. Les revenus peuvent augmenter, ta valeur est reconnue.

## Ce que tu pourrais vivre
- Une amélioration des revenus
- Des opportunités financières
- Une reconnaissance de ta valeur

## Conseils pour ce transit
- Développe tes ressources
- Valorise tes talents
- Évite les excès""",

    ('cancer', 3): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Communication et apprentissages sont bénis – période d'expansion intellectuelle.

## L'énergie du moment
Jupiter traverse ta maison III, élargissant ton horizon intellectuel. Les échanges sont fructueux, les apprentissages enrichissants.

## Ce que tu pourrais vivre
- Des apprentissages passionnants
- Des relations de proximité enrichies
- Un succès dans la communication

## Conseils pour ce transit
- Apprends et communique
- Renforce tes liens proches
- Explore ton environnement""",

    ('cancer', 4): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ton foyer et ta famille sont exceptionnellement bénis!

## L'énergie du moment
Jupiter traverse ta maison IV, ta maison naturelle! C'est une période exceptionnelle pour la vie domestique et familiale. Protection, croissance, bénédictions – tout est favorisé.

## Ce que tu pourrais vivre
- Un agrandissement ou amélioration majeure
- Des joies familiales profondes
- Un sentiment de sécurité intense

## Conseils pour ce transit
- Investis dans ton foyer
- Cultive l'harmonie familiale
- Renforce tes racines""",

    ('cancer', 5): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** L'amour, la créativité et les plaisirs sont magnifiés – période de joie.

## L'énergie du moment
Jupiter traverse ta maison V, apportant chance et expansion à l'amour et la créativité. Les romances et les projets créatifs sont favorisés.

## Ce que tu pourrais vivre
- Une romance épanouissante
- Des succès créatifs
- Des moments de bonheur

## Conseils pour ce transit
- Ouvre-toi à l'amour
- Exprime ta créativité
- Savoure les plaisirs""",

    ('cancer', 6): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Travail et santé s'améliorent sous cette influence bénéfique.

## L'énergie du moment
Jupiter traverse ta maison VI, apportant des améliorations au travail quotidien et à la santé. Les opportunités arrivent, la vitalité augmente.

## Ce que tu pourrais vivre
- De meilleures conditions de travail
- Des opportunités professionnelles
- Une santé renforcée

## Conseils pour ce transit
- Saisis les opportunités
- Améliore tes habitudes de santé
- Sers avec générosité""",

    ('cancer', 7): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Tes relations sont bénies – période idéale pour les engagements.

## L'énergie du moment
Jupiter traverse ta maison VII, apportant chance et croissance à tes relations. Les rencontres et partenariats sont favorisés.

## Ce que tu pourrais vivre
- Une rencontre significative
- Un engagement favorable
- Des partenariats fructueux

## Conseils pour ce transit
- Sois ouvert(e) aux relations
- Engage-toi si tu es prêt(e)
- Collabore avec confiance""",

    ('cancer', 8): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Transformation et ressources partagées sont favorisées.

## L'énergie du moment
Jupiter traverse ta maison VIII, apportant croissance dans l'intimité et les finances partagées. Les transformations sont bénéfiques.

## Ce que tu pourrais vivre
- Des gains par les ressources partagées
- Une transformation positive
- Une intimité enrichie

## Conseils pour ce transit
- Gère bien les finances communes
- Accepte la transformation
- Explore les profondeurs""",

    ('cancer', 9): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Voyages, études et expansion spirituelle sont favorisés!

## L'énergie du moment
Jupiter traverse ta maison IX avec son énergie d'expansion! Voyages, études, quête de sens – tout est magnifié.

## Ce que tu pourrais vivre
- Des voyages transformateurs
- Des succès académiques
- Une expansion spirituelle

## Conseils pour ce transit
- Voyage vers de nouveaux horizons
- Entreprends des études
- Explore ta spiritualité""",

    ('cancer', 10): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Ta carrière et ta réputation sont bénies – vise la réussite!

## L'énergie du moment
Jupiter traverse ta maison X, apportant chance et expansion à ta vie professionnelle. Les promotions et la reconnaissance sont favorisées.

## Ce que tu pourrais vivre
- Une avancée professionnelle
- Une reconnaissance publique
- L'atteinte de tes objectifs

## Conseils pour ce transit
- Vise haut professionnellement
- Accepte les responsabilités
- Profite de ta réputation""",

    ('cancer', 11): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Amitiés et projets d'avenir s'épanouissent – tes souhaits peuvent se réaliser.

## L'énergie du moment
Jupiter traverse ta maison XI, apportant expansion à ta vie sociale et tes rêves. Les amitiés et les espoirs sont favorisés.

## Ce que tu pourrais vivre
- Des amitiés nouvelles
- La réalisation de souhaits
- Un réseau élargi

## Conseils pour ce transit
- Élargis ton cercle social
- Engage-toi dans des groupes
- Rêve grand""",

    ('cancer', 12): """# ♃ Transit de Jupiter en Bélier

**En une phrase :** Protection spirituelle et croissance intérieure – période de grâce.

## L'énergie du moment
Jupiter traverse ta maison XII, apportant protection et croissance spirituelle. Période favorable pour le travail intérieur.

## Ce que tu pourrais vivre
- Une protection providentielle
- Une croissance spirituelle
- Des aides inattendues

## Conseils pour ce transit
- Médite et explore ta spiritualité
- Guéris tes blessures
- Fais confiance au processus""",
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
        print(f"✅ Transit Jupiter (Aries, Taurus, Gemini, Cancer)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
