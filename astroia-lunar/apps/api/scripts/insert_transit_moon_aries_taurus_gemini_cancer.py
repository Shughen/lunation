#!/usr/bin/env python3
"""Script d'insertion des interprétations Transit Lune en Bélier/Taureau/Gémeaux/Cancer."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

TRANSIT_MOON_INTERPRETATIONS = {
    # ARIES
    ('aries', 1): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Tes émotions sont vives et impulsives — agis spontanément sur ce que tu ressens.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 1, amplifiant ton besoin d'action et d'affirmation. Tes émotions te poussent à bouger, à prendre les devants. Tu ressens les choses intensément et veux agir tout de suite.

## Ce que tu pourrais vivre
- Une envie soudaine de changer quelque chose dans ta vie
- De l'impatience si les choses ne bougent pas assez vite
- Un regain d'énergie et de courage émotionnel

## Conseils pour ce transit
- Canalise ton énergie dans une activité physique
- Exprime ce que tu ressens directement
- Évite les décisions trop impulsives""",

    ('aries', 2): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Tes besoins matériels se font sentir — tu veux agir pour ta sécurité.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 2, éveillant tes besoins de sécurité et de ressources. Tu as envie d'agir pour améliorer ta situation financière ou de faire des achats impulsifs.

## Ce que tu pourrais vivre
- Une impulsion pour acheter quelque chose
- L'envie de prendre une initiative financière
- Une réflexion rapide sur ce qui compte pour toi

## Conseils pour ce transit
- Réfléchis avant les dépenses impulsives
- Agis sur une idée pour augmenter tes revenus
- Reconnais ta valeur et défends-la""",

    ('aries', 3): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Tes pensées s'accélèrent — exprime ce que tu as sur le cœur.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 3, rendant ta communication plus directe et tes pensées plus rapides. Tu as besoin de parler, d'échanger, de bouger.

## Ce que tu pourrais vivre
- Des conversations animées ou des débats
- L'envie de dire ce que tu penses sans filtrer
- Des déplacements courts ou des messages nombreux

## Conseils pour ce transit
- Exprime-toi mais reste à l'écoute
- Utilise cette énergie pour les tâches mentales urgentes
- Évite les paroles blessantes sous le coup de l'émotion""",

    ('aries', 4): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Chez toi, l'énergie est vive — canalise-la pour éviter les tensions.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 4, apportant de l'agitation à la maison. Tu peux te sentir à l'étroit ou avoir envie de changement dans ton environnement domestique.

## Ce que tu pourrais vivre
- De l'agitation ou des tensions à la maison
- L'envie de réorganiser ou de nettoyer énergiquement
- Des émotions liées à la famille qui remontent

## Conseils pour ce transit
- Fais du sport ou du ménage pour canaliser l'énergie
- Évite les disputes familiales
- Crée un espace où tu peux être seul si besoin""",

    ('aries', 5): """# ☽ Transit de la Lune en Bélier

**En une phrase :** La joie demande de l'action — amuse-toi spontanément.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 5, stimulant ton besoin de plaisir et d'expression créative. Tu as envie de t'amuser, de créer ou de flirter de façon spontanée.

## Ce que tu pourrais vivre
- Un élan créatif à saisir tout de suite
- L'envie de sortir, de jouer, de t'amuser
- Un flirt ou une attirance soudaine

## Conseils pour ce transit
- Suis ton impulsion créative
- Amuse-toi sans trop planifier
- En amour, ose faire le premier pas""",

    ('aries', 6): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Ton corps demande du mouvement — réponds à ses besoins énergiques.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 6, activant ton besoin de productivité et de santé. Tu veux accomplir des tâches rapidement et efficacement.

## Ce que tu pourrais vivre
- Une productivité élevée et de l'impatience
- L'envie de faire du sport ou de bouger
- De l'irritation si les tâches traînent

## Conseils pour ce transit
- Attaque les tâches que tu repoussais
- Fais une séance de sport intense
- Évite de te surmener par excès d'enthousiasme""",

    ('aries', 7): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Tes relations ont besoin de clarté — exprime directement tes besoins.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 7, rendant tes interactions plus directes. Tu as besoin que les choses soient claires dans tes relations.

## Ce que tu pourrais vivre
- Des discussions franches avec ton partenaire
- L'envie de résoudre un conflit rapidement
- De l'impatience envers les autres

## Conseils pour ce transit
- Exprime tes besoins clairement mais avec tact
- Écoute aussi le point de vue de l'autre
- Évite les disputes pour des broutilles""",

    ('aries', 8): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Des émotions profondes demandent à sortir — affronte-les avec courage.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 8, réveillant des émotions intenses. Tu peux ressentir des pulsions ou des besoins de transformation.

## Ce que tu pourrais vivre
- Des émotions intenses qui surgissent
- Un besoin de clarifier une situation financière partagée
- Une pulsion de changement radical

## Conseils pour ce transit
- Accueille les émotions sans les refouler
- Évite les confrontations financières impulsives
- Transforme l'énergie en action constructive""",

    ('aries', 9): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Ton esprit a soif d'aventure — explore de nouvelles idées.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 9, stimulant ta soif de découverte. Tu as envie d'apprendre, de voyager ou d'explorer de nouvelles perspectives.

## Ce que tu pourrais vivre
- Un enthousiasme soudain pour un nouveau sujet
- L'envie de partir à l'aventure
- Des discussions passionnées sur des idées

## Conseils pour ce transit
- Explore une nouvelle idée qui t'attire
- Planifie une escapade même courte
- Défends tes convictions avec passion""",

    ('aries', 10): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Ton ambition s'éveille — prends une initiative professionnelle.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 10, activant ton besoin de réussite et de reconnaissance. Tu as envie d'agir pour ta carrière.

## Ce que tu pourrais vivre
- Une impulsion pour prendre les devants au travail
- Un besoin de reconnaissance professionnelle
- De l'impatience face aux blocages de carrière

## Conseils pour ce transit
- Lance une initiative professionnelle
- Montre ton leadership
- Évite les conflits avec les supérieurs""",

    ('aries', 11): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Tes amis t'énergisent — participe activement à la vie de groupe.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 11, stimulant ton besoin de connexion sociale et d'action collective. Tu as envie de rejoindre tes amis ou de t'impliquer dans un projet de groupe.

## Ce que tu pourrais vivre
- Une envie de voir tes amis ou de faire une activité ensemble
- L'impulsion de t'engager dans une cause
- Des discussions animées dans un groupe

## Conseils pour ce transit
- Contacte tes amis pour une activité
- Propose une idée à ton groupe
- Canalise ton énergie dans un projet collectif""",

    ('aries', 12): """# ☽ Transit de la Lune en Bélier

**En une phrase :** Des émotions cachées émergent — accorde-toi du temps seul.

## L'énergie du moment
La Lune en Bélier traverse ta Maison 12, créant une tension entre le besoin d'action et celui de retrait. Des émotions refoulées peuvent surgir.

## Ce que tu pourrais vivre
- De l'agitation intérieure sans cause apparente
- Des rêves intenses ou de l'insomnie
- Le besoin de te retirer pour te ressourcer

## Conseils pour ce transit
- Accorde-toi des moments de solitude
- Fais une activité physique pour libérer les tensions
- Journalise tes émotions pour mieux les comprendre""",

    # TAURUS
    ('taurus', 1): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Tu as besoin de stabilité — ancre-toi dans ton corps et tes sens.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 1, te rendant plus calme, plus posé et plus sensible aux plaisirs sensoriels. Tu as besoin de confort et de stabilité.

## Ce que tu pourrais vivre
- Un désir de confort physique et émotionnel
- Une approche plus lente et réfléchie
- Un besoin de sécurité et de routine

## Conseils pour ce transit
- Prends soin de ton corps et de tes sens
- Offre-toi un plaisir simple
- Évite les changements brusques""",

    ('taurus', 2): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Tes besoins matériels sont au premier plan — apprécie ce que tu as.

## L'énergie du moment
La Lune en Taureau amplifie ta Maison 2, renforçant ton besoin de sécurité financière et de confort matériel. Tu apprécies ce qui est stable et durable.

## Ce que tu pourrais vivre
- Un besoin de faire le point sur tes finances
- L'envie d'acheter quelque chose de beau et durable
- Une appréciation de ce que tu possèdes déjà

## Conseils pour ce transit
- Apprécie ce que tu as avec gratitude
- Évite les dépenses excessives par besoin de confort
- Réfléchis à ce qui te fait vraiment te sentir en sécurité""",

    ('taurus', 3): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Ta communication se fait posée — prends le temps de bien t'exprimer.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 3, ralentissant tes pensées et ta communication. Tu préfères les échanges calmes et les sujets concrets.

## Ce que tu pourrais vivre
- Des conversations posées et constructives
- L'envie de réfléchir avant de parler
- Des échanges sur des sujets pratiques

## Conseils pour ce transit
- Prends le temps de formuler tes pensées
- Évite les discussions trop abstraites
- Communique sur des sujets concrets""",

    ('taurus', 4): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Ton foyer t'appelle — ressource-toi dans ton cocon.

## L'énergie du moment
La Lune en Taureau illumine ta Maison 4, renforçant ton besoin de confort domestique. Tu veux être chez toi, entouré de choses familières et réconfortantes.

## Ce que tu pourrais vivre
- Un besoin intense de rentrer chez toi
- L'envie de cuisiner ou de prendre soin de ton intérieur
- Un sentiment de paix dans ton foyer

## Conseils pour ce transit
- Passe du temps chez toi à te ressourcer
- Cuisine un bon repas maison
- Crée une ambiance chaleureuse""",

    ('taurus', 5): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Les plaisirs simples t'attirent — savoure la vie avec tes sens.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 5, éveillant ton besoin de plaisirs sensoriels et de créativité. Tu as envie de profiter des bonnes choses de la vie.

## Ce que tu pourrais vivre
- L'envie de te faire plaisir simplement
- Une créativité orientée vers le tangible
- Des moments de tendresse et de sensualité

## Conseils pour ce transit
- Offre-toi un plaisir sensoriel
- Crée quelque chose avec tes mains
- En amour, privilégie la tendresse""",

    ('taurus', 6): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Ton corps a besoin de soins — adopte un rythme stable.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 6, mettant l'accent sur ta santé et tes routines. Tu as besoin d'un quotidien régulier et nourrissant.

## Ce que tu pourrais vivre
- Un besoin de régularité dans ton emploi du temps
- L'envie de manger sainement et de bien dormir
- Une productivité constante mais pas excessive

## Conseils pour ce transit
- Établis une routine réconfortante
- Mange des aliments nourrissants
- Respecte ton besoin de repos""",

    ('taurus', 7): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Tes relations cherchent la stabilité — cultive la loyauté.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 7, renforçant ton besoin de relations stables et fiables. Tu apprécies les partenaires sur qui tu peux compter.

## Ce que tu pourrais vivre
- Un besoin de réassurance dans tes relations
- Des moments de partage calme avec ton partenaire
- Une appréciation de la loyauté

## Conseils pour ce transit
- Passe du temps de qualité avec ton partenaire
- Montre ta fiabilité
- Évite les discussions qui créent de l'insécurité""",

    ('taurus', 8): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Les changements te résistent — accepte de transformer à ton rythme.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 8, créant une tension entre ton besoin de stabilité et les transformations nécessaires. Tu peux résister aux changements.

## Ce que tu pourrais vivre
- Une résistance émotionnelle aux changements
- Un besoin de sécuriser tes ressources partagées
- Des émotions profondes liées à la possession

## Conseils pour ce transit
- Accepte le changement à ton rythme
- Sécurise ce qui peut l'être
- Ne t'accroche pas à ce qui doit partir""",

    ('taurus', 9): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Ta quête de sens s'ancre — cherche la sagesse dans le concret.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 9, orientant ta soif de connaissance vers le pratique. Tu cherches une sagesse applicable au quotidien.

## Ce que tu pourrais vivre
- Un intérêt pour des apprentissages pratiques
- L'envie de voyager confortablement
- Une réflexion sur tes valeurs profondes

## Conseils pour ce transit
- Apprends quelque chose d'utile
- Si tu voyages, privilégie le confort
- Médite sur ce qui donne du sens à ta vie""",

    ('taurus', 10): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Ta carrière a besoin de solidité — construis avec patience.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 10, renforçant ton besoin de stabilité professionnelle. Tu veux une carrière qui te sécurise.

## Ce que tu pourrais vivre
- Un besoin de reconnaissance pour ton travail constant
- L'envie de solidifier ta position professionnelle
- Une approche patiente de tes ambitions

## Conseils pour ce transit
- Montre ta fiabilité au travail
- Évite les changements de carrière impulsifs
- Construis ta réputation par la constance""",

    ('taurus', 11): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Tes amitiés t'ancrent — apprécie les liens durables.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 11, mettant l'accent sur tes amitiés stables et tes projets concrets. Tu apprécies les amis fidèles.

## Ce que tu pourrais vivre
- Des moments agréables avec des amis de longue date
- L'envie de contribuer concrètement à un groupe
- Une réflexion sur tes objectifs à long terme

## Conseils pour ce transit
- Entretiens tes amitiés de longue date
- Participe à un projet collectif concret
- Définis des objectifs réalistes""",

    ('taurus', 12): """# ☽ Transit de la Lune en Taureau

**En une phrase :** Ton monde intérieur demande du calme — ressource-toi en profondeur.

## L'énergie du moment
La Lune en Taureau traverse ta Maison 12, créant un besoin de retrait paisible. Tu as besoin de solitude confortable pour te régénérer.

## Ce que tu pourrais vivre
- Un besoin de retrait calme et confortable
- Des émotions qui demandent du temps pour être digérées
- Un sommeil réparateur si tu te le permets

## Conseils pour ce transit
- Accorde-toi du temps seul dans un endroit confortable
- Médite ou fais une activité relaxante
- Écoute les besoins profonds de ton corps""",

    # GEMINI
    ('gemini', 1): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Ton esprit s'active — connecte-toi et échange avec les autres.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 1, rendant ton humeur plus légère et curieuse. Tu as besoin de stimulation mentale et de communication.

## Ce que tu pourrais vivre
- Une curiosité accrue et des idées multiples
- L'envie de parler, d'échanger, de te connecter
- Une certaine dispersion émotionnelle

## Conseils pour ce transit
- Satisfais ta curiosité
- Échange avec les autres
- Évite de te disperser dans trop de directions""",

    ('gemini', 2): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Tes idées ont de la valeur — explore plusieurs pistes financières.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 2, stimulant ta réflexion sur tes ressources. Tu peux avoir plusieurs idées pour gagner de l'argent.

## Ce que tu pourrais vivre
- Des réflexions sur diverses sources de revenus
- L'envie de parler d'argent ou de négocier
- Une certaine indécision sur les priorités financières

## Conseils pour ce transit
- Note tes idées financières pour plus tard
- Évite les décisions financières précipitées
- Explore plusieurs options sans te disperser""",

    ('gemini', 3): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Ta communication est à son apogée — exprime-toi librement.

## L'énergie du moment
La Lune en Gémeaux amplifie ta Maison 3, rendant ta communication particulièrement fluide. Tu as besoin de parler, d'écrire, de partager.

## Ce que tu pourrais vivre
- Un flot de pensées et d'idées à partager
- Des échanges multiples et stimulants
- De l'agitation mentale si tu ne peux pas communiquer

## Conseils pour ce transit
- Écris, appelle, envoie des messages
- Apprends quelque chose de nouveau
- Évite le bavardage excessif""",

    ('gemini', 4): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Ton foyer s'anime — apporte de la légèreté à la maison.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 4, rendant l'atmosphère domestique plus légère et communicative. Tu as envie d'échanger avec ta famille.

## Ce que tu pourrais vivre
- Des conversations animées à la maison
- L'envie de réorganiser ou de rafraîchir ton intérieur
- Une certaine agitation domestique

## Conseils pour ce transit
- Discute avec tes proches
- Apporte de la nouveauté dans ton intérieur
- Évite les discussions superficielles qui tournent en boucle""",

    ('gemini', 5): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Le jeu et l'esprit se mêlent — amuse-toi intelligemment.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 5, stimulant ta créativité mentale et ton goût pour le jeu. Tu as envie de t'amuser de façon intellectuelle.

## Ce que tu pourrais vivre
- Des jeux de mots ou d'esprit
- Des flirts légers et amusants
- Une créativité basée sur les idées

## Conseils pour ce transit
- Joue à des jeux de société ou de réflexion
- Flirte avec légèreté
- Exprime ta créativité par l'écriture""",

    ('gemini', 6): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Ton quotidien demande de la variété — varie tes activités.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 6, créant un besoin de diversité dans ton travail et tes routines. Tu t'ennuies vite si c'est monotone.

## Ce que tu pourrais vivre
- Un besoin de varier tes tâches
- Des échanges nombreux au travail
- De l'impatience face à la routine

## Conseils pour ce transit
- Varie tes activités dans la journée
- Communique davantage avec tes collègues
- Évite la monotonie""",

    ('gemini', 7): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Tes relations passent par les mots — dialogue avec tes proches.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 7, rendant la communication essentielle dans tes relations. Tu as besoin d'échanger pour te sentir connecté.

## Ce que tu pourrais vivre
- Des discussions importantes avec ton partenaire
- Le besoin de stimulation intellectuelle dans tes relations
- Une légèreté bienvenue dans les échanges

## Conseils pour ce transit
- Parle ouvertement avec ton partenaire
- Partage des idées et des découvertes
- Évite les conversations trop superficielles""",

    ('gemini', 8): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Les profondeurs t'intriguent — explore-les avec curiosité.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 8, éveillant ta curiosité pour les sujets profonds ou tabous. Tu veux comprendre ce qui est caché.

## Ce que tu pourrais vivre
- Une curiosité pour les sujets psychologiques
- Des conversations sur des sujets profonds
- Un besoin de comprendre les mécanismes cachés

## Conseils pour ce transit
- Pose des questions sur ce qui t'intrigue
- Explore un sujet profond avec légèreté
- Évite de rationaliser tes émotions""",

    ('gemini', 9): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Ta soif d'apprendre s'éveille — explore de nouvelles idées.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 9, stimulant ta curiosité intellectuelle et ton goût pour l'apprentissage. Tu veux découvrir de nouveaux sujets.

## Ce que tu pourrais vivre
- Un intérêt soudain pour un nouveau domaine
- L'envie de voyager mentalement ou physiquement
- Des discussions stimulantes sur des idées

## Conseils pour ce transit
- Explore un nouveau sujet qui t'attire
- Planifie un voyage même court
- Échange des idées avec des personnes différentes""",

    ('gemini', 10): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Ta communication professionnelle brille — fais-toi remarquer par tes idées.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 10, mettant tes talents de communication au service de ta carrière. Tu peux te faire remarquer par tes idées.

## Ce que tu pourrais vivre
- Des opportunités de présenter tes idées au travail
- Une visibilité accrue grâce à ta communication
- Des échanges importants avec des supérieurs

## Conseils pour ce transit
- Présente tes idées avec clarté
- Networke et échange avec des contacts professionnels
- Utilise les réseaux sociaux pour ta carrière""",

    ('gemini', 11): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Tes amis stimulent ton esprit — échange et connecte-toi.

## L'énergie du moment
La Lune en Gémeaux amplifie ta Maison 11, rendant ta vie sociale particulièrement stimulante. Tu as besoin d'échanges avec tes amis et ton réseau.

## Ce que tu pourrais vivre
- Des échanges nombreux avec tes amis
- Des idées de projets collectifs
- Une vie sociale animée et stimulante

## Conseils pour ce transit
- Organise une sortie avec des amis
- Participe à des discussions de groupe
- Partage tes idées pour l'avenir""",

    ('gemini', 12): """# ☽ Transit de la Lune en Gémeaux

**En une phrase :** Ton mental a besoin de calme — laisse tes pensées se poser.

## L'énergie du moment
La Lune en Gémeaux traverse ta Maison 12, créant de l'agitation mentale intérieure. Tu peux avoir du mal à calmer tes pensées.

## Ce que tu pourrais vivre
- Des pensées qui tournent en boucle
- De l'insomnie ou des rêves agités
- Un besoin de verbaliser tes émotions cachées

## Conseils pour ce transit
- Journalise pour libérer ton mental
- Pratique une méditation guidée
- Évite la surstimulation avant le coucher""",

    # CANCER
    ('cancer', 1): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Tes émotions sont à fleur de peau — prends soin de toi avec tendresse.

## L'énergie du moment
La Lune en Cancer, son signe de prédilection, traverse ta Maison 1. Tu es particulièrement sensible, intuitif et réceptif aux ambiances. Prends soin de toi.

## Ce que tu pourrais vivre
- Une sensibilité émotionnelle accrue
- Un besoin de confort et de sécurité
- Une intuition particulièrement forte

## Conseils pour ce transit
- Écoute tes émotions sans les juger
- Entoure-toi de personnes bienveillantes
- Prends soin de toi comme d'un enfant""",

    ('cancer', 2): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Ta sécurité matérielle te touche émotionnellement — nourris ton sentiment de sécurité.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 2, liant tes émotions à ta sécurité financière. Tu te sens bien quand tes besoins matériels sont couverts.

## Ce que tu pourrais vivre
- Des émotions liées à l'argent ou à la sécurité
- Un besoin de savoir que tu as assez
- Une réflexion sur ce qui te fait te sentir en sécurité

## Conseils pour ce transit
- Rassure-toi sur ta situation financière
- Évite les dépenses émotionnelles
- Nourris ton sentiment de sécurité intérieure""",

    ('cancer', 3): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Ta communication se teinte d'émotion — exprime ce que tu ressens vraiment.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 3, rendant ta communication plus émotionnelle et intuitive. Tu communiques avec ton cœur.

## Ce que tu pourrais vivre
- Des conversations chargées d'émotion
- Un besoin de parler à cœur ouvert
- Une sensibilité aux mots et aux non-dits

## Conseils pour ce transit
- Exprime tes sentiments à tes proches
- Écoute avec empathie
- Évite les discussions trop rationnelles""",

    ('cancer', 4): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Ton foyer est ton refuge — ressource-toi dans ton cocon.

## L'énergie du moment
La Lune en Cancer amplifie ta Maison 4, créant un besoin intense de chez-soi et de famille. Tu veux être dans ton cocon, entouré de ceux que tu aimes.

## Ce que tu pourrais vivre
- Un besoin impérieux de rentrer chez toi
- Des émotions liées à la famille ou au passé
- Un sentiment de paix profonde à la maison

## Conseils pour ce transit
- Passe du temps chez toi
- Occupe-toi de ta famille
- Crée un environnement chaleureux et sécurisant""",

    ('cancer', 5): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Ton cœur s'ouvre à l'amour — vis des moments tendres.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 5, rendant tes expériences de plaisir et d'amour plus émotionnelles. Tu as besoin de tendresse et de connexion.

## Ce que tu pourrais vivre
- Des moments de tendresse et d'affection
- Une créativité nourrie par les émotions
- Un besoin de prendre soin de ceux que tu aimes

## Conseils pour ce transit
- Exprime ton affection à ceux que tu aimes
- Crée quelque chose qui vient du cœur
- Offre-toi des plaisirs réconfortants""",

    ('cancer', 6): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Ton corps parle de tes émotions — prends soin de ta santé avec douceur.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 6, liant ta santé à tes émotions. Tu peux ressentir physiquement ce que tu vis émotionnellement.

## Ce que tu pourrais vivre
- Une sensibilité digestive ou émotionnelle
- Un besoin de routines réconfortantes
- L'envie de prendre soin des autres au travail

## Conseils pour ce transit
- Mange des aliments réconfortants et sains
- Crée un environnement de travail chaleureux
- Écoute ce que ton corps te dit""",

    ('cancer', 7): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Tes relations demandent de la tendresse — nourris tes liens.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 7, rendant tes relations plus émotionnelles et protectrices. Tu as besoin de te sentir en sécurité avec l'autre.

## Ce que tu pourrais vivre
- Un besoin de réassurance dans tes relations
- Des moments de partage émotionnel profond
- L'envie de prendre soin de ton partenaire

## Conseils pour ce transit
- Exprime tes besoins émotionnels
- Prends soin de ton partenaire
- Crée des moments d'intimité""",

    ('cancer', 8): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Tes émotions profondes remontent — accueille-les avec compassion.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 8, amplifiant les émotions profondes et les mémoires anciennes. Tu peux revivre des blessures du passé.

## Ce que tu pourrais vivre
- Des émotions intenses liées au passé
- Un besoin de sécurité face aux changements
- Des révélations émotionnelles

## Conseils pour ce transit
- Accueille tes émotions sans les fuir
- Prends soin de toi pendant ce processus
- Parle à quelqu'un de confiance si besoin""",

    ('cancer', 9): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Ta quête de sens passe par le cœur — cherche ce qui te touche.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 9, orientant ta recherche de sens vers l'émotionnel. Tu cherches une sagesse qui parle à ton cœur.

## Ce que tu pourrais vivre
- Un intérêt pour les traditions familiales ou ancestrales
- L'envie de voyager vers des lieux chargés d'émotion
- Une réflexion sur tes racines et tes valeurs

## Conseils pour ce transit
- Explore ton histoire familiale
- Voyage vers des lieux qui te touchent
- Cherche une sagesse qui te réconforte""",

    ('cancer', 10): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Ta carrière a besoin d'authenticité — montre ton humanité au travail.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 10, créant un besoin de sens et d'humanité dans ta vie professionnelle. Tu veux un travail qui compte.

## Ce que tu pourrais vivre
- Un questionnement sur le sens de ta carrière
- Le besoin de te sentir utile professionnellement
- Une sensibilité aux relations au travail

## Conseils pour ce transit
- Montre ton côté humain au travail
- Réfléchis à l'impact de ton travail
- Prends soin de tes collègues""",

    ('cancer', 11): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Tes amis sont ta famille — nourris ces liens précieux.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 11, rendant tes amitiés plus émotionnelles et protectrices. Tu considères tes amis comme une famille.

## Ce que tu pourrais vivre
- Des moments chaleureux avec tes amis
- L'envie de prendre soin de ton cercle
- Un besoin d'appartenance à un groupe bienveillant

## Conseils pour ce transit
- Organise un moment convivial avec tes amis
- Montre ton affection à ton réseau
- Soutiens un ami qui traverse un moment difficile""",

    ('cancer', 12): """# ☽ Transit de la Lune en Cancer

**En une phrase :** Tes émotions les plus profondes émergent — laisse-les couler.

## L'énergie du moment
La Lune en Cancer traverse ta Maison 12, amplifiant ta sensibilité intérieure et ton intuition. Tu peux ressentir des émotions sans cause apparente.

## Ce que tu pourrais vivre
- Des émotions qui surgissent de nulle part
- Des rêves émotionnels et révélateurs
- Un besoin intense de solitude et de repos

## Conseils pour ce transit
- Accorde-toi du temps seul
- Pleure si tu en as besoin
- Écoute tes rêves et tes intuitions""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in TRANSIT_MOON_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'transit_moon',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP transit_moon/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='transit_moon',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT transit_moon/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
