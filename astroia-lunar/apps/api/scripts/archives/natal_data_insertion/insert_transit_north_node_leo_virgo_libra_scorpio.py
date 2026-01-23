#!/usr/bin/env python3
"""
Insert transit_north_node interpretations V2 for Leo, Virgo, Libra, Scorpio (houses 1-12)
Total: 48 interpretations (4 signs × 12 houses)
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_NORTH_NODE_INTERPRETATIONS = {
    # ============== LEO ==============
    ('leo', 1): """# ☊ Nœud Nord en Lion – Maison I

**En une phrase :** L'univers t'invite à briller, à exprimer ta créativité et à assumer ta royauté intérieure.

## L'énergie du moment
Le Nœud Nord en Lion dans ta maison I t'appelle à devenir le héros de ta propre vie. Ta croissance passe par l'expression de toi-même avec fierté, générosité et courage. C'est le moment de monter sur scène.

## Ce que tu pourrais vivre
- Un besoin d'être vu(e), reconnu(e) et apprécié(e) pour qui tu es
- Une redéfinition de ton image vers plus de confiance et d'éclat
- Des situations qui te poussent à prendre le devant de la scène

## Conseils pour ce transit
- Assume ta singularité avec fierté et panache
- Exprime ta créativité sans te soucier du regard des autres
- Développe ta générosité comme marque de noblesse personnelle""",

    ('leo', 2): """# ☊ Nœud Nord en Lion – Maison II

**En une phrase :** Ta mission karmique te guide vers l'affirmation de ta valeur unique et créative.

## L'énergie du moment
Le Nœud Nord en Lion illumine ta maison des ressources. Tu es invité(e) à reconnaître ta valeur exceptionnelle et à monétiser tes talents créatifs. L'abondance vient quand tu oses briller pleinement.

## Ce que tu pourrais vivre
- Des opportunités de revenus liées à ta créativité ou ton leadership
- Une prise de conscience de ta valeur unique
- Un rapport à l'argent plus généreux et confiant

## Conseils pour ce transit
- Valorise tes talents créatifs comme sources de richesse
- Investis dans ce qui te fait briller
- Sois généreux avec tes ressources""",

    ('leo', 3): """# ☊ Nœud Nord en Lion – Maison III

**En une phrase :** Tu es appelé(e) à communiquer avec passion, créativité et cœur.

## L'énergie du moment
Le Nœud Nord en Lion enflamme ta maison de la communication. Ta croissance passe par une expression créative et théâtrale de tes idées. Ta parole doit inspirer, émouvoir et captiver.

## Ce que tu pourrais vivre
- Une communication plus expressive et dramatique
- Des talents d'orateur ou de conteur qui s'éveillent
- Des échanges chaleureux et généreux avec ton entourage

## Conseils pour ce transit
- Mets du cœur et de la passion dans tes communications
- Ose raconter des histoires, captiver ton audience
- Sois généreux dans le partage de tes connaissances""",

    ('leo', 4): """# ☊ Nœud Nord en Lion – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un foyer où tu es le roi/la reine.

## L'énergie du moment
Le Nœud Nord en Lion réchauffe ta maison des racines. Tu es appelé(e) à faire de ton foyer un château, un lieu de créativité et de fierté familiale. C'est en assumant ton rôle central à la maison que tu grandis.

## Ce que tu pourrais vivre
- Un désir de créer un foyer lumineux et accueillant
- Un rôle de leader ou de pilier dans ta famille
- Une fierté retrouvée pour tes origines et ta lignée

## Conseils pour ce transit
- Transforme ton foyer en expression de ta créativité
- Assume un rôle de cœur dans ta famille
- Transmets la joie et la confiance à tes proches""",

    ('leo', 5): """# ☊ Nœud Nord en Lion – Maison V

**En une phrase :** L'univers t'invite à une explosion de créativité, de joie et d'amour passionné.

## L'énergie du moment
Le Nœud Nord en Lion est chez lui dans ta maison de la joie. C'est un appel puissant à créer, aimer et t'amuser avec magnificence. Ta croissance passe par l'expression totale de ta flamme intérieure.

## Ce que tu pourrais vivre
- Une créativité qui demande à s'exprimer pleinement
- Des amours passionnées et théâtrales
- Un bonheur de vivre qui rayonne autour de toi

## Conseils pour ce transit
- Crée sans retenue, exprime ton génie unique
- Vis l'amour comme une grande aventure romantique
- Laisse ton enfant intérieur jouer et rayonner""",

    ('leo', 6): """# ☊ Nœud Nord en Lion – Maison VI

**En une phrase :** Ta croissance karmique passe par un travail qui te permet de briller.

## L'énergie du moment
Le Nœud Nord en Lion illumine ta maison du quotidien. Tu es invité(e) à mettre de la créativité et de la fierté dans ton travail. Même les tâches ordinaires peuvent devenir des occasions de briller.

## Ce que tu pourrais vivre
- Un travail qui met en valeur tes talents créatifs
- Un leadership naturel dans ton environnement professionnel
- Des routines qui incluent expression de soi et plaisir

## Conseils pour ce transit
- Apporte ta touche personnelle et créative à ton travail
- Assume un rôle de leader bienveillant avec tes collègues
- Fais de tes routines des moments de joie""",

    ('leo', 7): """# ☊ Nœud Nord en Lion – Maison VII

**En une phrase :** Ta mission karmique t'invite à rayonner au sein de tes relations.

## L'énergie du moment
Le Nœud Nord en Lion illumine ta maison des partenariats. Tu es appelé(e) à être pleinement toi-même dans tes relations, à apporter ta lumière sans te diminuer pour l'autre.

## Ce que tu pourrais vivre
- Des relations où tu es célébré(e) pour qui tu es
- Un besoin de partenaires qui admirent ta lumière
- Des associations où tu as un rôle central et créatif

## Conseils pour ce transit
- Reste toi-même, brillant(e) et généreux(se), en couple
- Cherche des partenaires qui célèbrent ton éclat
- Apporte générosité et chaleur dans toutes tes relations""",

    ('leo', 8): """# ☊ Nœud Nord en Lion – Maison VIII

**En une phrase :** Tu es appelé(e) à transformer tes ombres en lumière créatrice.

## L'énergie du moment
Le Nœud Nord en Lion illumine ta maison des profondeurs. Ta croissance passe par la capacité à rester lumineux même dans les crises, à transformer les épreuves en performances créatives.

## Ce que tu pourrais vivre
- Une capacité à trouver la lumière même dans les moments sombres
- Des transformations qui renforcent ta confiance en toi
- Une intimité où tu peux briller et être admiré(e)

## Conseils pour ce transit
- Garde ta flamme allumée même dans les tempêtes
- Transforme tes blessures en forces créatives
- Ose être toi-même dans l'intimité la plus profonde""",

    ('leo', 9): """# ☊ Nœud Nord en Lion – Maison IX

**En une phrase :** L'univers t'invite à développer une philosophie personnelle et à la partager avec passion.

## L'énergie du moment
Le Nœud Nord en Lion enflamme ta maison de l'expansion. Ta croissance passe par le développement d'une vision du monde personnelle et courageuse. Tu es appelé(e) à enseigner et inspirer avec cœur.

## Ce que tu pourrais vivre
- Une envie de partager ta vision avec passion
- Des voyages qui nourrissent ta créativité et ta confiance
- Un rôle d'enseignant ou d'inspirateur charismatique

## Conseils pour ce transit
- Développe et assume ta propre philosophie de vie
- Voyage comme un roi/une reine découvrant son royaume
- Enseigne avec passion et générosité""",

    ('leo', 10): """# ☊ Nœud Nord en Lion – Maison X

**En une phrase :** Ta mission de vie t'appelle à devenir une figure publique créative et inspirante.

## L'énergie du moment
Le Nœud Nord en Lion couronne ta maison de la carrière. Tu es appelé(e) à occuper une place de leader, à briller professionnellement et à inspirer par ton exemple. Ta carrière est une scène.

## Ce que tu pourrais vivre
- Une carrière qui te met en lumière publiquement
- Une reconnaissance pour ton leadership et ta créativité
- Un rôle d'inspiration pour les autres dans ton domaine

## Conseils pour ce transit
- Vise les positions qui te permettent de rayonner
- Assume ton rôle de leader avec générosité
- Inspire les autres par ton exemple et ta passion""",

    ('leo', 11): """# ☊ Nœud Nord en Lion – Maison XI

**En une phrase :** Tu es invité(e) à inspirer les groupes et porter des idéaux avec cœur.

## L'énergie du moment
Le Nœud Nord en Lion réchauffe ta maison des amitiés et des idéaux. Ta mission est d'apporter ta lumière unique aux causes collectives, d'inspirer tes cercles par ta générosité et ta créativité.

## Ce que tu pourrais vivre
- Un rôle de leader ou d'inspirateur dans les groupes
- Des amitiés qui célèbrent ton unicité
- Des projets collectifs portés par ta vision créative

## Conseils pour ce transit
- Apporte ta flamme unique aux causes qui te tiennent à cœur
- Choisis des cercles qui valorisent ta lumière
- Inspire tes amis par ta générosité et ton courage""",

    ('leo', 12): """# ☊ Nœud Nord en Lion – Maison XII

**En une phrase :** Ta croissance karmique passe par la découverte de ta lumière intérieure secrète.

## L'énergie du moment
Le Nœud Nord en Lion illumine ta maison de l'invisible. Tu es appelé(e) à découvrir que ta vraie royauté est intérieure, que ta créativité peut s'exprimer dans le silence et la solitude.

## Ce que tu pourrais vivre
- Une créativité qui s'éveille dans l'introspection
- Une confiance intérieure indépendante du regard extérieur
- Des expériences spirituelles qui révèlent ta lumière cachée

## Conseils pour ce transit
- Découvre ta royauté intérieure, au-delà des apparences
- Crée dans le secret, pour toi-même d'abord
- Trouve ta source de lumière dans le silence""",

    # ============== VIRGO ==============
    ('virgo', 1): """# ☊ Nœud Nord en Vierge – Maison I

**En une phrase :** L'univers t'invite à développer ta précision, ton discernement et ton sens du service.

## L'énergie du moment
Le Nœud Nord en Vierge dans ta maison I t'appelle à incarner l'humilité utile, la compétence pratique et le souci du détail. Ta croissance passe par le perfectionnement de toi-même au service des autres.

## Ce que tu pourrais vivre
- Un besoin de te définir par tes compétences et ton utilité
- Une redéfinition de ton image vers plus de simplicité et d'efficacité
- Des situations qui exigent précision et discernement

## Conseils pour ce transit
- Cultive l'excellence dans les détails de ta vie
- Développe des compétences pratiques et utiles
- Définis-toi par ce que tu fais de bien, pas par ce que tu possèdes""",

    ('virgo', 2): """# ☊ Nœud Nord en Vierge – Maison II

**En une phrase :** Ta mission karmique te guide vers une gestion sage et méthodique de tes ressources.

## L'énergie du moment
Le Nœud Nord en Vierge structure ta maison des ressources. Tu es invité(e) à développer une relation saine et organisée avec l'argent, à valoriser tes compétences pratiques.

## Ce que tu pourrais vivre
- Une amélioration de ta gestion financière
- Des revenus liés à tes compétences techniques ou analytiques
- Une clarification de ce qui a vraiment de la valeur pratique

## Conseils pour ce transit
- Organise et structure tes finances avec méthode
- Valorise tes compétences pratiques comme sources de revenus
- Évite le gaspillage, cultive la simplicité""",

    ('virgo', 3): """# ☊ Nœud Nord en Vierge – Maison III

**En une phrase :** Tu es appelé(e) à communiquer avec précision, clarté et utilité.

## L'énergie du moment
Le Nœud Nord en Vierge affine ta maison de la communication. Ta croissance passe par une parole précise, des analyses claires et une transmission de connaissances pratiques.

## Ce que tu pourrais vivre
- Une communication plus structurée et analytique
- Des apprentissages techniques ou pratiques
- Des échanges basés sur l'entraide et le conseil utile

## Conseils pour ce transit
- Communique clairement et avec précision
- Apprends des compétences pratiques et applicables
- Rends-toi utile à ton entourage proche""",

    ('virgo', 4): """# ☊ Nœud Nord en Vierge – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un foyer organisé et fonctionnel.

## L'énergie du moment
Le Nœud Nord en Vierge structure ta maison des racines. Tu es appelé(e) à créer un chez-toi ordonné, pratique et sain. La simplicité fonctionnelle devient ta base de sécurité.

## Ce que tu pourrais vivre
- Un besoin d'organiser et de purifier ton espace de vie
- Une amélioration des habitudes domestiques
- Un rapport plus pratique et sain à ta famille

## Conseils pour ce transit
- Organise ton foyer de façon fonctionnelle et saine
- Crée des routines domestiques efficaces
- Simplifie ton environnement de vie""",

    ('virgo', 5): """# ☊ Nœud Nord en Vierge – Maison V

**En une phrase :** L'univers t'invite à une créativité méthodique et un amour fait de petites attentions.

## L'énergie du moment
Le Nœud Nord en Vierge tempère ta maison de la joie. Ta créativité s'exprime mieux dans le détail et la précision. En amour, les petits gestes quotidiens comptent plus que les grands drames.

## Ce que tu pourrais vivre
- Une créativité artisanale, patiente et minutieuse
- Des relations amoureuses basées sur le service mutuel
- Un plaisir trouvé dans les choses simples et bien faites

## Conseils pour ce transit
- Crée avec patience et souci du détail
- Montre ton amour par des gestes pratiques et attentionnés
- Trouve la joie dans les petites choses bien faites""",

    ('virgo', 6): """# ☊ Nœud Nord en Vierge – Maison VI

**En une phrase :** Ta croissance karmique passe par l'excellence dans le service quotidien.

## L'énergie du moment
Le Nœud Nord en Vierge est chez lui dans ta maison du travail. C'est un appel puissant à développer des compétences, à servir avec excellence et à prendre soin de ta santé avec méthode.

## Ce que tu pourrais vivre
- Un travail où tes compétences sont reconnues et développées
- Des routines de santé qui portent leurs fruits
- Un perfectionnement constant dans ton métier

## Conseils pour ce transit
- Deviens excellent(e) dans ton domaine par la pratique
- Sers les autres avec humilité et compétence
- Prends soin de ta santé de façon méthodique""",

    ('virgo', 7): """# ☊ Nœud Nord en Vierge – Maison VII

**En une phrase :** Ta mission karmique t'invite à des relations pratiques et mutuellement utiles.

## L'énergie du moment
Le Nœud Nord en Vierge tempère ta maison des partenariats. Tu es appelé(e) à développer des relations basées sur l'entraide concrète, le soutien pratique et l'amélioration mutuelle.

## Ce que tu pourrais vivre
- Des relations qui s'améliorent par les petites attentions
- Un besoin de partenaires fiables et serviables
- Des associations professionnelles efficaces et complémentaires

## Conseils pour ce transit
- Montre ton amour par des actes de service concrets
- Cherche des partenaires avec qui tu te complètes utilement
- Améliore tes relations par l'attention aux détails""",

    ('virgo', 8): """# ☊ Nœud Nord en Vierge – Maison VIII

**En une phrase :** Tu es appelé(e) à analyser et organiser tes zones d'ombre avec discernement.

## L'énergie du moment
Le Nœud Nord en Vierge structure ta maison des profondeurs. Ta croissance passe par une approche méthodique des questions profondes : analyser tes peurs, organiser tes ressources partagées.

## Ce que tu pourrais vivre
- Une capacité accrue à analyser et comprendre tes profondeurs
- Une organisation plus claire des finances partagées
- Une transformation par l'amélioration progressive

## Conseils pour ce transit
- Analyse tes peurs et blocages avec objectivité
- Organise méthodiquement les ressources partagées
- Transforme-toi par de petites améliorations quotidiennes""",

    ('virgo', 9): """# ☊ Nœud Nord en Vierge – Maison IX

**En une phrase :** L'univers t'invite à une spiritualité pratique et applicable au quotidien.

## L'énergie du moment
Le Nœud Nord en Vierge tempère ta maison de l'expansion. Ta croissance philosophique passe par le concret et l'applicable. Ta sagesse doit être utile, pas juste théorique.

## Ce que tu pourrais vivre
- Une philosophie de vie pratique et applicable
- Des voyages qui ont un but utile ou éducatif
- Un enseignement basé sur des méthodes concrètes

## Conseils pour ce transit
- Développe une spiritualité qui s'applique au quotidien
- Voyage pour apprendre des compétences pratiques
- Enseigne des connaissances utiles et vérifiables""",

    ('virgo', 10): """# ☊ Nœud Nord en Vierge – Maison X

**En une phrase :** Ta mission de vie t'appelle à exceller par ta compétence et ton service.

## L'énergie du moment
Le Nœud Nord en Vierge structure ta maison de la carrière. Tu es appelé(e) à bâtir une réputation sur tes compétences pratiques, ton efficacité et ta capacité à résoudre des problèmes.

## Ce que tu pourrais vivre
- Une carrière basée sur l'expertise technique ou le service
- Une reconnaissance pour ta fiabilité et ton efficacité
- Un perfectionnement constant de tes compétences professionnelles

## Conseils pour ce transit
- Deviens un(e) expert(e) reconnu(e) dans ton domaine
- Construis ta réputation sur ta fiabilité et ton utilité
- Améliore constamment tes compétences professionnelles""",

    ('virgo', 11): """# ☊ Nœud Nord en Vierge – Maison XI

**En une phrase :** Tu es invité(e) à servir les causes collectives avec compétence et méthode.

## L'énergie du moment
Le Nœud Nord en Vierge structure ta maison des amitiés et des idéaux. Ta mission est d'apporter des solutions pratiques aux problèmes collectifs, d'être utile à tes réseaux.

## Ce que tu pourrais vivre
- Un rôle d'aide pratique et efficace dans les groupes
- Des amitiés basées sur l'entraide concrète
- Des projets collectifs qui résolvent des problèmes réels

## Conseils pour ce transit
- Apporte des solutions pratiques aux causes que tu soutiens
- Sois l'ami(e) sur qui on peut compter pour l'aide concrète
- Utilise tes compétences au service du collectif""",

    ('virgo', 12): """# ☊ Nœud Nord en Vierge – Maison XII

**En une phrase :** Ta croissance karmique passe par le service humble et discret.

## L'énergie du moment
Le Nœud Nord en Vierge purifie ta maison de l'invisible. Tu es appelé(e) à servir sans reconnaissance, à améliorer ton monde intérieur avec méthode et à trouver le sacré dans les gestes simples.

## Ce que tu pourrais vivre
- Un service altruiste qui se fait dans l'ombre
- Des pratiques spirituelles simples et régulières
- Une guérison par l'amélioration patiente de soi

## Conseils pour ce transit
- Sers sans attendre de reconnaissance
- Pratique une spiritualité simple et quotidienne
- Améliore-toi par de petits gestes réguliers""",

    # ============== LIBRA ==============
    ('libra', 1): """# ☊ Nœud Nord en Balance – Maison I

**En une phrase :** L'univers t'invite à développer la diplomatie, l'harmonie et la grâce relationnelle.

## L'énergie du moment
Le Nœud Nord en Balance dans ta maison I t'appelle à incarner l'équilibre, la beauté et l'art de la relation. Ta croissance passe par la capacité à créer l'harmonie autour de toi.

## Ce que tu pourrais vivre
- Un besoin de te définir à travers tes relations et collaborations
- Une redéfinition de ton image vers plus d'élégance et de diplomatie
- Des situations qui exigent tact et sens de la négociation

## Conseils pour ce transit
- Cultive l'élégance et la grâce dans ta présentation
- Développe tes compétences diplomatiques
- Définis-toi aussi par ta capacité à créer des liens harmonieux""",

    ('libra', 2): """# ☊ Nœud Nord en Balance – Maison II

**En une phrase :** Ta mission karmique te guide vers un équilibre entre donner et recevoir dans tes finances.

## L'énergie du moment
Le Nœud Nord en Balance équilibre ta maison des ressources. Tu es invité(e) à créer une relation juste avec l'argent, à valoriser la beauté et l'esthétique, à partager équitablement.

## Ce que tu pourrais vivre
- Des revenus liés à l'esthétique, l'art ou la médiation
- Un questionnement sur l'équilibre entre tes besoins et ceux des autres
- Une valorisation de ce qui crée harmonie et beauté

## Conseils pour ce transit
- Crée un équilibre entre générosité et réception
- Investis dans la beauté et l'harmonie
- Développe des partenariats financiers équitables""",

    ('libra', 3): """# ☊ Nœud Nord en Balance – Maison III

**En une phrase :** Tu es appelé(e) à communiquer avec diplomatie, nuance et sens de l'écoute.

## L'énergie du moment
Le Nœud Nord en Balance harmonise ta maison de la communication. Ta croissance passe par une parole qui crée des ponts, qui considère tous les points de vue et qui apaise les tensions.

## Ce que tu pourrais vivre
- Une communication plus nuancée et diplomatique
- Un rôle de médiateur dans ton entourage
- Des apprentissages liés à l'art, l'esthétique ou les relations

## Conseils pour ce transit
- Écoute toujours l'autre point de vue avant de répondre
- Communique avec tact et élégance
- Utilise ta parole pour créer des ponts""",

    ('libra', 4): """# ☊ Nœud Nord en Balance – Maison IV

**En une phrase :** Ta mission karmique t'invite à créer un foyer harmonieux et esthétiquement équilibré.

## L'énergie du moment
Le Nœud Nord en Balance embellit ta maison des racines. Tu es appelé(e) à créer un chez-toi où règnent paix, beauté et relations harmonieuses. L'équilibre familial devient ta priorité.

## Ce que tu pourrais vivre
- Un désir de créer un intérieur beau et harmonieux
- Un rôle de médiateur dans les relations familiales
- Un besoin de paix et d'équilibre dans ton espace privé

## Conseils pour ce transit
- Crée un foyer esthétiquement plaisant et équilibré
- Favorise l'harmonie dans les relations familiales
- Fais de ta maison un lieu de paix et de beauté""",

    ('libra', 5): """# ☊ Nœud Nord en Balance – Maison V

**En une phrase :** L'univers t'invite à créer avec grâce et à aimer avec équilibre.

## L'énergie du moment
Le Nœud Nord en Balance illumine ta maison de la joie. Ta créativité s'épanouit dans la recherche de la beauté et de l'harmonie. En amour, tu cherches l'équilibre parfait.

## Ce que tu pourrais vivre
- Une créativité orientée vers la beauté et l'esthétique
- Des relations amoureuses qui cherchent l'équilibre du donner-recevoir
- Un plaisir trouvé dans les arts et l'élégance

## Conseils pour ce transit
- Crée des œuvres harmonieuses et esthétiques
- Cultive des amours où chacun donne et reçoit équitablement
- Trouve la joie dans la beauté et les arts""",

    ('libra', 6): """# ☊ Nœud Nord en Balance – Maison VI

**En une phrase :** Ta croissance karmique passe par des relations de travail harmonieuses.

## L'énergie du moment
Le Nœud Nord en Balance harmonise ta maison du quotidien. Tu es invité(e) à créer de bonnes relations avec tes collègues, à travailler en partenariat et à apporter de la beauté à ta routine.

## Ce que tu pourrais vivre
- Un travail impliquant collaboration et diplomatie
- Des routines qui incluent l'esthétique et l'harmonie
- Des relations de travail qui s'améliorent

## Conseils pour ce transit
- Cultive de bonnes relations avec tes collègues
- Apporte de la beauté et de l'harmonie à ton quotidien
- Travaille en partenariat plutôt qu'en solo""",

    ('libra', 7): """# ☊ Nœud Nord en Balance – Maison VII

**En une phrase :** Ta mission karmique t'invite à maîtriser l'art du partenariat équilibré.

## L'énergie du moment
Le Nœud Nord en Balance est chez lui dans ta maison des partenariats. C'est un appel puissant à développer des relations équilibrées, justes et harmonieuses. L'autre devient ton miroir de croissance.

## Ce que tu pourrais vivre
- Des relations qui s'équilibrent vers plus de justice
- Un apprentissage profond de l'art du compromis
- Des partenariats qui t'élèvent par leur harmonie

## Conseils pour ce transit
- Apprends à trouver l'équilibre dans toutes tes relations
- Maîtrise l'art du compromis et de la négociation
- Cherche des partenariats véritablement équilibrés""",

    ('libra', 8): """# ☊ Nœud Nord en Balance – Maison VIII

**En une phrase :** Tu es appelé(e) à trouver l'équilibre dans les questions d'intimité et de partage.

## L'énergie du moment
Le Nœud Nord en Balance équilibre ta maison des profondeurs. Ta croissance passe par un partage équitable des ressources, une intimité harmonieuse et une transformation en douceur.

## Ce que tu pourrais vivre
- Des questions de partage qui trouvent un équilibre juste
- Une intimité basée sur la réciprocité
- Des transformations qui se font dans la grâce

## Conseils pour ce transit
- Crée un équilibre juste dans les finances partagées
- Cultive une intimité où chacun donne et reçoit
- Traverse les transformations avec grâce et diplomatie""",

    ('libra', 9): """# ☊ Nœud Nord en Balance – Maison IX

**En une phrase :** L'univers t'invite à une philosophie de l'équilibre et du juste milieu.

## L'énergie du moment
Le Nœud Nord en Balance élargit ta maison de l'expansion. Ta croissance philosophique passe par la considération de tous les points de vue, le rejet des extrêmes et la recherche de l'harmonie.

## Ce que tu pourrais vivre
- Une philosophie qui cherche l'équilibre et la justice
- Des voyages qui élargissent ta vision des relations
- Un enseignement sur l'art de vivre ensemble

## Conseils pour ce transit
- Développe une vision du monde équilibrée
- Voyage pour comprendre d'autres perspectives
- Enseigne l'art du dialogue et du compromis""",

    ('libra', 10): """# ☊ Nœud Nord en Balance – Maison X

**En une phrase :** Ta mission de vie t'appelle à exceller dans les domaines de la médiation et de l'harmonie.

## L'énergie du moment
Le Nœud Nord en Balance couronne ta maison de la carrière. Tu es appelé(e) à bâtir une carrière basée sur tes talents diplomatiques, ton sens de l'esthétique ou ta capacité à créer des partenariats.

## Ce que tu pourrais vivre
- Une carrière dans la diplomatie, le droit, l'art ou les relations publiques
- Une reconnaissance pour tes talents de médiateur
- Des partenariats professionnels stratégiques

## Conseils pour ce transit
- Oriente ta carrière vers la médiation ou l'esthétique
- Utilise tes talents diplomatiques professionnellement
- Construis ta réputation sur l'équité et l'élégance""",

    ('libra', 11): """# ☊ Nœud Nord en Balance – Maison XI

**En une phrase :** Tu es invité(e) à créer des réseaux harmonieux et des amitiés équilibrées.

## L'énergie du moment
Le Nœud Nord en Balance harmonise ta maison des amitiés. Ta mission est de créer des connexions basées sur l'équité, de favoriser l'harmonie dans les groupes et de porter des idéaux de justice.

## Ce que tu pourrais vivre
- Des amitiés qui s'équilibrent vers plus de réciprocité
- Un rôle de médiateur ou d'harmonisateur dans les groupes
- Des causes liées à la justice et l'équité sociale

## Conseils pour ce transit
- Crée des amitiés équilibrées où chacun donne et reçoit
- Utilise tes talents diplomatiques au service des groupes
- Soutiens des causes de justice et d'équité""",

    ('libra', 12): """# ☊ Nœud Nord en Balance – Maison XII

**En une phrase :** Ta croissance karmique passe par la paix intérieure et l'harmonie avec l'invisible.

## L'énergie du moment
Le Nœud Nord en Balance apaise ta maison de l'invisible. Tu es appelé(e) à trouver l'équilibre intérieur, à faire la paix avec tes zones d'ombre et à développer une relation harmonieuse avec le divin.

## Ce que tu pourrais vivre
- Une paix intérieure qui se développe progressivement
- Une réconciliation avec tes parts d'ombre
- Une spiritualité basée sur l'harmonie et la beauté

## Conseils pour ce transit
- Cultive l'équilibre intérieur par la méditation
- Fais la paix avec ce que tu cherchais à cacher
- Trouve la beauté dans tes pratiques spirituelles""",

    # ============== SCORPIO ==============
    ('scorpio', 1): """# ☊ Nœud Nord en Scorpion – Maison I

**En une phrase :** L'univers t'invite à embrasser ta puissance, ta profondeur et ta capacité de transformation.

## L'énergie du moment
Le Nœud Nord en Scorpion dans ta maison I t'appelle à incarner l'intensité, la passion et le pouvoir de régénération. Ta croissance passe par l'acceptation de ta nature profonde et magnétique.

## Ce que tu pourrais vivre
- Un besoin de montrer ta vraie nature, même si elle dérange
- Une redéfinition de ton image vers plus d'authenticité brute
- Des situations qui exigent courage et capacité de transformation

## Conseils pour ce transit
- Assume ta nature intense et magnétique
- Développe ton pouvoir personnel sans t'excuser
- Transforme-toi profondément, encore et encore""",

    ('scorpio', 2): """# ☊ Nœud Nord en Scorpion – Maison II

**En une phrase :** Ta mission karmique te guide vers une relation profonde et transformatrice avec tes ressources.

## L'énergie du moment
Le Nœud Nord en Scorpion intensifie ta maison des ressources. Tu es invité(e) à développer un rapport puissant avec l'argent, à creuser jusqu'aux racines de tes valeurs et à transmuter ta relation aux possessions.

## Ce que tu pourrais vivre
- Une transformation profonde de ton rapport à l'argent
- Des ressources qui viennent par la transformation ou la crise
- Un questionnement intense sur tes vraies valeurs

## Conseils pour ce transit
- Explore les profondeurs de ta relation à l'argent
- Accepte les crises financières comme opportunités de renaissance
- Valorise ce qui a une vraie substance, pas le superficiel""",

    ('scorpio', 3): """# ☊ Nœud Nord en Scorpion – Maison III

**En une phrase :** Tu es appelé(e) à communiquer avec profondeur, intensité et pouvoir de transformation.

## L'énergie du moment
Le Nœud Nord en Scorpion approfondit ta maison de la communication. Ta croissance passe par une parole qui va au cœur des choses, qui n'a pas peur des sujets tabous et qui transforme.

## Ce que tu pourrais vivre
- Une communication plus profonde et incisive
- Des conversations qui creusent sous la surface
- Des apprentissages liés à la psychologie ou aux mystères

## Conseils pour ce transit
- Ose dire ce que d'autres n'osent pas dire
- Explore les sujets tabous avec courage
- Utilise ta parole pour provoquer des prises de conscience""",

    ('scorpio', 4): """# ☊ Nœud Nord en Scorpion – Maison IV

**En une phrase :** Ta mission karmique t'invite à transformer tes racines et guérir tes blessures familiales.

## L'énergie du moment
Le Nœud Nord en Scorpion plonge dans ta maison des racines. Tu es appelé(e) à creuser dans ton histoire familiale, à affronter les secrets et les blessures pour te transformer profondément.

## Ce que tu pourrais vivre
- Une plongée dans les secrets ou traumatismes familiaux
- Une transformation profonde de ton sentiment de sécurité
- Un besoin de guérir tes racines pour te libérer

## Conseils pour ce transit
- Affronte les secrets et blessures familiaux avec courage
- Transforme ton rapport à tes origines
- Crée un foyer qui honore les profondeurs de l'âme""",

    ('scorpio', 5): """# ☊ Nœud Nord en Scorpion – Maison V

**En une phrase :** L'univers t'invite à créer et aimer avec une intensité transformatrice.

## L'énergie du moment
Le Nœud Nord en Scorpion embrase ta maison de la joie. Ta créativité s'exprime dans les profondeurs émotionnelles. En amour, tu es appelé(e) à des passions qui transforment.

## Ce que tu pourrais vivre
- Une créativité qui puise dans tes zones d'ombre
- Des amours intenses et transformatrices
- Un rapport aux plaisirs qui inclut l'intensité émotionnelle

## Conseils pour ce transit
- Crée à partir de tes émotions les plus profondes
- Accepte les passions amoureuses qui te transforment
- Trouve la joie dans l'intensité et la profondeur""",

    ('scorpio', 6): """# ☊ Nœud Nord en Scorpion – Maison VI

**En une phrase :** Ta croissance karmique passe par un travail qui te transforme en profondeur.

## L'énergie du moment
Le Nœud Nord en Scorpion intensifie ta maison du quotidien. Tu es invité(e) à un travail qui implique transformation, guérison ou investigation. Ta santé bénéficie des approches profondes.

## Ce que tu pourrais vivre
- Un travail lié à la transformation, la guérison ou l'investigation
- Des routines qui incluent des pratiques de purification profonde
- Une santé qui s'améliore en affrontant les causes profondes

## Conseils pour ce transit
- Cherche un travail qui transforme toi et les autres
- Adopte des pratiques de santé qui vont à la racine
- N'aie pas peur de transformer radicalement tes habitudes""",

    ('scorpio', 7): """# ☊ Nœud Nord en Scorpion – Maison VII

**En une phrase :** Ta mission karmique t'invite à des relations profondes et transformatrices.

## L'énergie du moment
Le Nœud Nord en Scorpion intensifie ta maison des partenariats. Tu es appelé(e) à des relations qui ne restent pas en surface, qui impliquent intimité, pouvoir et transformation mutuelle.

## Ce que tu pourrais vivre
- Des relations qui te transforment profondément
- Un besoin de partenaires avec qui tu peux être vraiment toi
- Des associations qui impliquent pouvoir et intimité

## Conseils pour ce transit
- Cherche des relations qui permettent une vraie profondeur
- Accepte le pouvoir et l'intensité dans tes partenariats
- Transforme-toi à travers le miroir de l'autre""",

    ('scorpio', 8): """# ☊ Nœud Nord en Scorpion – Maison VIII

**En une phrase :** Tu es appelé(e) à maîtriser l'art de la transformation et de la renaissance.

## L'énergie du moment
Le Nœud Nord en Scorpion est chez lui dans ta maison des profondeurs. C'est un appel puissant à embrasser les cycles de mort et renaissance, à explorer l'intimité profonde et les ressources partagées.

## Ce que tu pourrais vivre
- Des transformations majeures et des renaissances
- Une intimité profonde et transformatrice
- Des questions de pouvoir et de ressources partagées

## Conseils pour ce transit
- Accepte les morts symboliques comme chemins vers la renaissance
- Plonge dans l'intimité sans peur
- Maîtrise les questions de pouvoir et de ressources partagées""",

    ('scorpio', 9): """# ☊ Nœud Nord en Scorpion – Maison IX

**En une phrase :** L'univers t'invite à une quête spirituelle profonde et transformatrice.

## L'énergie du moment
Le Nœud Nord en Scorpion approfondit ta maison de l'expansion. Ta croissance passe par une spiritualité qui ne craint pas les ténèbres, par des voyages initiatiques et une philosophie de la transformation.

## Ce que tu pourrais vivre
- Une quête spirituelle qui explore les mystères
- Des voyages vers des lieux de pouvoir ou de transformation
- Un enseignement sur les profondeurs de l'existence

## Conseils pour ce transit
- Explore les traditions spirituelles qui embrassent les ténèbres
- Voyage vers des lieux qui transforment
- Développe une philosophie qui inclut mort et renaissance""",

    ('scorpio', 10): """# ☊ Nœud Nord en Scorpion – Maison X

**En une phrase :** Ta mission de vie t'appelle à exercer un pouvoir transformateur dans le monde.

## L'énergie du moment
Le Nœud Nord en Scorpion couronne ta maison de la carrière. Tu es appelé(e) à une position de pouvoir, une carrière qui implique transformation, guérison ou investigation des profondeurs.

## Ce que tu pourrais vivre
- Une carrière impliquant pouvoir et transformation
- Une reconnaissance pour ta capacité à régénérer
- Un rôle public qui touche aux tabous ou aux profondeurs

## Conseils pour ce transit
- Assume un rôle de pouvoir avec intégrité
- Oriente ta carrière vers la transformation ou la guérison
- N'aie pas peur d'être associé(e) aux sujets profonds""",

    ('scorpio', 11): """# ☊ Nœud Nord en Scorpion – Maison XI

**En une phrase :** Tu es invité(e) à transformer les groupes et porter des causes profondes.

## L'énergie du moment
Le Nœud Nord en Scorpion intensifie ta maison des amitiés et des idéaux. Ta mission est d'apporter une transformation profonde aux collectifs, de porter des causes qui touchent aux tabous.

## Ce que tu pourrais vivre
- Des amitiés profondes et transformatrices
- Un rôle de transformation dans les groupes
- Des causes liées à la mort, la sexualité, le pouvoir ou la guérison

## Conseils pour ce transit
- Choisis des amis qui acceptent ta profondeur
- Transforme les groupes auxquels tu appartiens
- Porte des causes qui osent toucher aux tabous""",

    ('scorpio', 12): """# ☊ Nœud Nord en Scorpion – Maison XII

**En une phrase :** Ta croissance karmique passe par l'exploration des profondeurs de l'inconscient.

## L'énergie du moment
Le Nœud Nord en Scorpion plonge dans ta maison de l'invisible. Tu es appelé(e) à explorer tes zones d'ombre les plus profondes, à transmuter ton karma et à renaître spirituellement.

## Ce que tu pourrais vivre
- Une plongée profonde dans ton inconscient
- Des révélations sur tes vies passées ou ton karma
- Une transformation spirituelle majeure

## Conseils pour ce transit
- Explore ton inconscient sans peur
- Transmute tes schémas karmiques les plus anciens
- Accepte les morts symboliques comme libérations""",
}


async def insert_interpretations():
    """Insert North Node transit interpretations for Leo, Virgo, Libra, Scorpio"""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_NORTH_NODE_INTERPRETATIONS.items():
            # Check if exists
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_north_node',
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
                subject='transit_north_node',
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
        print(f"✅ Transit North Node (Leo, Virgo, Libra, Scorpio)")
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == '__main__':
    asyncio.run(insert_interpretations())
