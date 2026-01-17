# 🌙 Guide Utilisateur Lunation — MVP

**Version:** 1.0.0
**Dernière mise à jour:** 2026-01-17

---

## Table des matières

1. [Introduction](#1-introduction)
2. [Onboarding](#2-onboarding)
3. [Écran Home](#3-écran-home)
4. [Rapport Lunaire Mensuel](#4-rapport-lunaire-mensuel)
5. [VoC (Void of Course)](#5-voc-void-of-course)
6. [Transits Majeurs](#6-transits-majeurs)
7. [Mini Journal](#7-mini-journal)
8. [FAQ](#8-faq)

---

## 1. Introduction

### Qu'est-ce que Lunation (Astroia Lunar) ?

**Lunation** est une application mobile qui vous aide à comprendre vos cycles émotionnels et énergétiques mensuels grâce à l'astrologie lunaire. Contrairement aux horoscopes quotidiens génériques, Lunation se concentre sur **vos rythmes personnels** en analysant votre thème natal et vos révolutions lunaires.

### Philosophie MVP : Révolutions Lunaires et Cycles Lunaires

Au cœur de Lunation se trouve un concept astrologique puissant : **la révolution lunaire**.

#### Qu'est-ce qu'une révolution lunaire ?

Une révolution lunaire se produit environ tous les **28 jours**, lorsque la Lune retourne à la position exacte qu'elle occupait lors de votre naissance. Ce moment marque le début d'un nouveau cycle lunaire personnel, qui dure jusqu'à la prochaine révolution (environ un mois).

Chaque révolution lunaire possède ses propres caractéristiques :
- **Un ascendant lunaire** : le signe qui se levait à l'horizon au moment exact de la révolution
- **Une maison lunaire** : la zone de vie activée par la Lune pendant ce cycle
- **Des thèmes mensuels** : les énergies dominantes du mois à venir

#### Pourquoi se concentrer sur les cycles lunaires ?

La Lune influence nos émotions, notre intuition et nos rythmes intérieurs. En suivant vos révolutions lunaires, vous pouvez :
- **Anticiper** les périodes d'énergie haute ou basse
- **Comprendre** pourquoi certains mois sont plus intenses que d'autres
- **Naviguer** vos cycles avec plus de clarté et d'intention
- **Faire le lien** entre votre vécu quotidien et les influences astrologiques

Lunation vous accompagne mois après mois dans cette exploration, avec des outils pratiques et des insights concrets.

---

## 2. Onboarding

Lors de votre première utilisation, Lunation vous guide à travers 4 étapes essentielles pour créer votre profil astrologique personnalisé.

### Étape 1 : Écran de bienvenue

L'écran de bienvenue vous présente l'application et sa mission : vous aider à suivre vos cycles lunaires personnels.

**Action :** Appuyez sur "Commencer" pour démarrer votre parcours.

### Étape 2 : Consentement

Lunation vous demande votre accord pour :
- Collecter vos données de naissance (date, heure, lieu)
- Calculer votre thème natal
- Générer vos révolutions lunaires mensuelles

**Important :** Vos données sont stockées de manière sécurisée et ne sont jamais partagées avec des tiers. Elles servent uniquement aux calculs astrologiques.

**Action :** Lisez les conditions et acceptez pour continuer.

### Étape 3 : Disclaimer

L'astrologie est un outil de réflexion et de connaissance de soi, mais ne remplace pas :
- Un avis médical
- Un conseil professionnel
- Une thérapie

Lunation vous offre des insights pour mieux vous comprendre, mais les décisions importantes de votre vie vous appartiennent.

**Action :** Prenez connaissance du disclaimer et acceptez pour avancer.

### Étape 4 : Configuration du profil

C'est l'étape la plus importante ! Pour calculer votre thème natal et vos révolutions lunaires, Lunation a besoin de vos données de naissance précises.

#### Informations requises :

1. **Date de naissance** : jour, mois, année (ex : 15 avril 1989)
2. **Heure de naissance** : heure et minute exactes (ex : 17h55)
   - **Astuce :** Votre acte de naissance officiel contient cette information. Si vous ne la connaissez pas, demandez à vos parents ou consultez votre mairie.
3. **Lieu de naissance** : ville et pays (ex : Paris, France)
   - L'application détecte automatiquement les coordonnées géographiques (latitude/longitude) et le fuseau horaire.

#### Pourquoi ces informations sont-elles si importantes ?

- La **date** détermine la position des planètes dans le ciel.
- L'**heure exacte** calcule votre ascendant et vos maisons astrologiques (les zones de vie).
- Le **lieu** (coordonnées) assure la précision des calculs en fonction de votre position sur Terre.

**Une erreur de quelques minutes peut changer votre ascendant ou vos maisons !**

**Action :** Remplissez tous les champs avec précision, puis validez.

### Calcul du thème natal

Une fois vos données validées, Lunation lance automatiquement le calcul de votre thème natal.

**Que se passe-t-il en coulisses ?**
- Connexion à l'API d'éphémérides RapidAPI (calculs astronomiques précis)
- Calcul des positions planétaires au moment exact de votre naissance
- Détermination de votre ascendant, de vos maisons et de vos aspects planétaires
- Sauvegarde de votre thème natal dans votre profil

**Durée :** Environ 5 secondes.

**Résultat :** Votre thème natal est prêt ! Vous êtes redirigé vers l'écran principal (Home).

---

## 3. Écran Home

L'écran **Home** est le cœur de Lunation. C'est votre tableau de bord quotidien, conçu pour répondre à une question essentielle : **"Quel est mon cycle lunaire actuel ?"**

### Vision d'ensemble

L'écran Home se compose de 4 widgets principaux :

1. **Current Lunar Card** : Votre révolution lunaire en cours
2. **VoC Widget** : Le statut Void of Course du jour
3. **Transits Widget** : Les 3 transits majeurs du mois
4. **Journal Prompt** : Invitation à écrire dans votre journal

Chaque widget vous donne un aperçu rapide et vous permet d'accéder aux détails en un clic.

---

### 3.1 Current Lunar Card

**Objectif :** Afficher votre révolution lunaire actuelle (le cycle en cours).

#### Informations affichées :

- **Période du cycle** : Date de début et date de fin (ex : "15 janvier - 12 février 2026")
- **Ascendant lunaire** : Le signe dominant de ce cycle (ex : "Ascendant Taureau")
- **Maison de la Lune** : La zone de vie activée (ex : "Lune en Maison 5 - Créativité et Romance")
- **Phase lunaire** : Nouvelle Lune, Premier Quartier, Pleine Lune, Dernier Quartier

#### Que faire avec cette information ?

- **Identifiez le thème du mois** : Chaque révolution lunaire met en lumière une zone spécifique de votre vie. Si votre Lune est en Maison 7 (relations), le mois sera tourné vers les partenariats et les collaborations.
- **Anticipez l'énergie globale** : L'ascendant lunaire colore le ton émotionnel du mois. Un ascendant Bélier sera plus dynamique et impulsif qu'un ascendant Poissons, plus contemplatif.

**Action :** Appuyez sur la carte pour accéder au rapport lunaire mensuel complet.

---

### 3.2 VoC Widget

**Objectif :** Vous informer du statut Void of Course actuel.

#### Informations affichées :

- **VoC maintenant ?** Oui/Non (avec indicateur visuel)
- **Prochaine fenêtre VoC** : Date et heure de début (ex : "Demain à 14h30")

#### Qu'est-ce que le Void of Course (VoC) ?

Le **Void of Course** (en français : "course à vide") désigne une période où la Lune n'effectue plus d'aspects majeurs avant de changer de signe. Astrologiquement, c'est un moment où les actions importantes ont tendance à "ne mener nulle part" ou à nécessiter des ajustements futurs.

#### Que faire pendant une fenêtre VoC ?

**À privilégier :**
- Activités routinières et tâches administratives
- Méditation, repos, introspection
- Activités créatives sans enjeu
- Rangement et organisation

**À éviter :**
- Prendre des décisions importantes
- Signer des contrats
- Lancer de nouveaux projets
- Faire des achats conséquents

**Note :** Le VoC n'est pas une période "négative", simplement un moment où l'énergie lunaire est en transition. Utilisez-le pour ralentir et vous reconnecter à vous-même.

**Action :** Appuyez sur le widget pour consulter le calendrier complet des fenêtres VoC à venir (écran détaillé).

---

### 3.3 Transits Widget

**Objectif :** Afficher les 3 transits planétaires majeurs du mois.

#### Informations affichées :

- **Nom du transit** (ex : "Saturne carré Vénus natal")
- **Date d'activation** (ex : "20 janvier 2026")
- **Type d'aspect** : Conjonction, Opposition, Carré ou Trigone (icônes visuelles)
- **Résumé en 1 ligne** (ex : "Réévaluation des relations importantes")

#### Qu'est-ce qu'un transit ?

Un transit se produit lorsqu'une planète en mouvement dans le ciel (transit) forme un aspect avec une planète de votre thème natal (position de naissance). Les transits influencent vos expériences et vos opportunités du moment.

**Exemple concret :**
Si Jupiter (planète de l'expansion) transite en conjonction avec votre Soleil natal (identité), vous pourriez vivre une période de confiance accrue, d'opportunités professionnelles ou de reconnaissance publique.

#### Pourquoi seulement les transits majeurs ?

Lunation filtre les centaines de transits quotidiens pour ne garder que les **4 aspects majeurs** :
1. **Conjonction** (0°) : Fusion d'énergies, nouveau départ
2. **Opposition** (180°) : Tension créative, prise de conscience
3. **Carré** (90°) : Friction, défi à surmonter
4. **Trigone** (120°) : Fluidité, opportunité naturelle

Ces aspects sont les plus significatifs et faciles à observer dans votre quotidien.

**Action :** Appuyez sur le widget pour accéder à la vue détaillée des transits du mois.

---

### 3.4 Journal Prompt

**Objectif :** Vous inviter à écrire une entrée dans votre journal quotidien.

#### Informations affichées :

- **"As-tu écrit aujourd'hui ?"** (question simple)
- **Statut** : Coche verte si vous avez déjà écrit aujourd'hui, sinon invitation à le faire
- **Lien automatique** : L'entrée sera liée au cycle lunaire en cours

#### Pourquoi tenir un journal lunaire ?

Le journal vous aide à :
- **Observer vos patterns émotionnels** au fil des cycles
- **Faire le lien** entre votre vécu et les influences lunaires
- **Ancrer vos insights** pour mieux les comprendre plus tard
- **Créer un historique** de vos mois lunaires

**Exemple d'utilisation :**
Vous écrivez chaque jour 2-3 phrases sur votre humeur, vos réalisations ou vos défis. À la fin du mois, vous relisez vos entrées et constatez : "Ah, c'était pendant ma révolution lunaire en Maison 10, pas étonnant que j'étais obsédé par mon travail !"

**Action :** Appuyez sur le prompt pour ouvrir l'écran du journal et créer une entrée.

---

## 4. Rapport Lunaire Mensuel

Le **Rapport Lunaire Mensuel** est le cœur de Lunation. C'est un document synthétique d'une page qui vous donne les clés pour naviguer votre cycle lunaire actuel.

### Comment accéder au rapport ?

Deux chemins possibles :
1. Depuis l'écran **Home**, appuyez sur la **Current Lunar Card**
2. Depuis le menu principal, sélectionnez **"Révolutions Lunaires"** puis **"Rapport du mois actuel"**

### Format du rapport

Le rapport se divise en **4 sections** :

---

#### 4.1 Header (En-tête)

**Contenu :**
- **Période du cycle** : "15 janvier - 12 février 2026"
- **Ascendant lunaire** : "Ascendant Taureau"
- **Maison de la Lune** : "Lune en Maison 5"
- **Phase lunaire** : Nouvelle Lune

**Utilité :** Vous donner le contexte général du mois. Vous savez immédiatement quelle zone de vie est activée et quel ton émotionnel domine.

---

#### 4.2 Climat du Mois

**Contenu :**
Un paragraphe de 3-5 phrases décrivant l'**énergie globale** de ce cycle lunaire.

**Exemple fictif :**
> "Ce cycle lunaire met l'accent sur la créativité et l'expression personnelle (Maison 5). Avec un ascendant Taureau, vous chercherez à ancrer ces inspirations dans la matière : projets artistiques concrets, hobbies structurés. La Nouvelle Lune invite à planter de nouvelles graines, pas à récolter. C'est un mois de gestation, où les idées prennent forme lentement mais sûrement."

**Ton :** Clair, factuel, sans jargon ésotérique. Vous devez pouvoir relier cette description à votre quotidien.

---

#### 4.3 Axes et Dynamiques

**Contenu :**
Analyse des **aspects majeurs** entre les planètes de la révolution lunaire et votre thème natal.

**Exemple fictif :**
> **Vénus trigone Jupiter natal** (18 janvier)
> "Cette configuration favorise les opportunités sociales et financières. Vous pourriez recevoir une proposition intéressante ou rencontrer des personnes inspirantes. Restez ouvert aux collaborations créatives."
>
> **Mars carré Saturne natal** (25 janvier)
> "Une tension entre votre désir d'action (Mars) et vos limites actuelles (Saturne). Vous pourriez ressentir de la frustration ou des retards dans vos projets. Patience et discipline seront vos meilleurs alliés."

**Format :** Chaque aspect est présenté avec :
- **Nom de l'aspect** et **date précise**
- **Explication factuelle** : Que se passe-t-il astrologiquement ?
- **Manifestation concrète** : Comment cela peut se traduire dans votre vie ?

---

#### 4.4 Points d'Attention

**Contenu :**
3-4 conseils pratiques pour tirer le meilleur parti de ce cycle lunaire.

**Exemple fictif :**
> 1. **Créez un espace pour la créativité** : Que ce soit un carnet de croquis, un bullet journal ou une soirée musique, accordez-vous du temps pour exprimer votre créativité sans jugement.
> 2. **Ancrez vos projets dans le réel** : L'ascendant Taureau vous invite à passer de l'idée à l'action concrète. Fixez-vous un objectif mesurable pour le mois.
> 3. **Gérez les frustrations fin janvier** : Le carré Mars-Saturne peut générer de l'impatience. Prévoyez des soupapes (sport, méditation) pour canaliser cette énergie.

**Ton :** Actionnable, bienveillant, pragmatique.

---

### Comment interpréter le contenu ?

**Principe clé :** Le rapport lunaire est un **guide**, pas une prophétie.

Les configurations astrologiques décrivent des **tendances énergétiques**, mais votre libre arbitre reste entier. Utilisez le rapport comme une boussole :
- Si vous reconnaissez une dynamique décrite, vous gagnez en clarté.
- Si vous ne la reconnaissez pas, c'est peut-être qu'elle se manifeste de manière subtile ou dans un autre domaine de votre vie.

**Astuce :** Relisez le rapport en fin de mois et notez ce qui a résonné. Cela vous aide à affiner votre compréhension de votre fonctionnement lunaire.

---

## 5. VoC (Void of Course)

### Qu'est-ce que le VoC ?

Le **Void of Course** (VoC) est une période astrologique où la Lune ne forme plus d'aspects majeurs avant de changer de signe. Cette transition peut durer de quelques minutes à plusieurs heures (rarement plus de 24h).

#### Contexte astronomique

La Lune se déplace très rapidement dans le ciel (environ 13° par jour). Tous les 2-3 jours, elle change de signe. Juste avant ce changement, il arrive un moment où elle ne forme plus aucun aspect avec les autres planètes : c'est le VoC.

#### Signification astrologique

Le VoC est considéré comme un moment où :
- L'énergie lunaire est "en pause"
- Les actions lancées ont tendance à "ne pas prendre"
- Les décisions peuvent nécessiter des révisions futures

**Analogie :** Imaginez la Lune comme une négociatrice qui quitte une réunion (signe) pour se rendre à une autre. Entre les deux, elle ne peut rien conclure. C'est le VoC.

---

### Comment consulter les fenêtres VoC ?

**Depuis l'écran Home :**
1. Consultez le **VoC Widget** pour savoir si vous êtes actuellement en VoC.
2. Appuyez sur le widget pour accéder à l'écran détaillé **VoC**.

**Écran VoC :**
- **VoC actuel** : Si une fenêtre VoC est en cours, vous voyez l'heure de début et de fin.
- **Prochaines fenêtres VoC** : Calendrier des 7 prochains jours avec toutes les périodes VoC à venir.
- **Durée de chaque fenêtre** : Affichée en heures et minutes.

**Exemple d'affichage fictif :**
```
VoC actuel :
🌑 En cours - Fin dans 2h15 (aujourd'hui à 16h30)

Prochaines fenêtres :
📅 Demain 18h00 - 20h30 (2h30)
📅 20 janvier 08h15 - 10h00 (1h45)
📅 22 janvier 22h00 - 23h45 (1h45)
```

---

### Conseils d'utilisation du VoC

**À privilégier pendant le VoC :**
- Tâches routinières (courses, ménage, emails administratifs)
- Activités contemplatives (lecture, méditation, marche)
- Travail créatif sans pression de résultat (brainstorming, écriture libre)
- Repos et recharge énergétique

**À éviter pendant le VoC :**
- Prendre des décisions importantes (signer un contrat, accepter une offre)
- Lancer un projet majeur (création d'entreprise, déménagement)
- Faire des achats importants (voiture, appartement, équipement coûteux)
- Planifier des événements critiques (réunion décisive, premier rendez-vous)

**Important :** Le VoC n'est pas une interdiction absolue ! Si vous n'avez pas le choix (urgence professionnelle, opportunité unique), agissez. Soyez simplement conscient qu'il pourra y avoir des ajustements ou des imprévus.

**Astuce pratique :** Si vous avez une décision importante à prendre, attendez que le VoC soit terminé pour finaliser. Utilisez le VoC pour réfléchir, et agissez ensuite.

---

### Notifications VoC (à venir)

Lunation prépare une fonctionnalité de notifications pour vous alerter :
- **Avant le début** d'une fenêtre VoC (ex : "VoC dans 1 heure")
- **Pendant** une fenêtre VoC importante

Cette fonctionnalité sera activée dans une version future. L'infrastructure est déjà prête, mais les notifications ne sont pas encore activées dans le MVP.

---

## 6. Transits Majeurs

### Qu'est-ce qu'un transit ?

Un **transit** se produit lorsqu'une planète en mouvement dans le ciel (en temps réel) forme un aspect avec une planète de votre thème natal (position à votre naissance).

**Exemple :**
Vous êtes né avec Vénus à 15° Gémeaux. Aujourd'hui, Jupiter transite à 15° Sagittaire. Ces deux planètes sont en **opposition** (180°) : c'est un transit.

#### Pourquoi les transits sont importants ?

Les transits activent les promesses de votre thème natal. Ils déclenchent des événements, des rencontres, des opportunités ou des défis selon la nature des planètes et de l'aspect.

**Analogie musicale :**
Votre thème natal est la partition. Les transits sont les musiciens qui jouent cette partition en temps réel. Certaines notes résonnent fort (transits majeurs), d'autres sont subtiles (transits mineurs).

---

### Comment consulter les transits du mois ?

**Depuis l'écran Home :**
1. Consultez le **Transits Widget** pour voir les 3 transits majeurs à venir.
2. Appuyez sur le widget pour accéder à l'écran **Transits Overview**.

**Écran Transits Overview :**
- **Liste des transits majeurs du mois** : Tous les transits impliquant les 4 aspects majeurs (conjonction, opposition, carré, trigone).
- **Filtrage par aspect** : Vous pouvez afficher uniquement les conjonctions, ou uniquement les carrés, etc.
- **Tri par date** : Les transits sont classés par ordre chronologique.

**Exemple d'affichage fictif :**
```
Transits de janvier 2026 :

18 jan : Vénus trigone Jupiter natal ♀△♃
         "Opportunités sociales et créatives"

22 jan : Soleil conjonction Mercure natal ☉☌☿
         "Clarté mentale et communication fluide"

25 jan : Mars carré Saturne natal ♂□♄
         "Tension entre action et contraintes"
```

---

### Les 4 aspects majeurs expliqués

Lunation se concentre sur les 4 aspects astrologiques les plus significatifs :

#### 6.1 Conjonction (0°) ☌

**Symbole :** Fusion
**Énergie :** Intensification, nouveau départ

**Explication :**
Deux planètes sont au même degré, leurs énergies se mélangent. C'est comme deux musiciens jouant la même note : le son est amplifié.

**Manifestation concrète :**
- Soleil conjonction Vénus natal : Période de confiance en soi, charisme accru, opportunités relationnelles.
- Saturne conjonction Lune natale : Besoin de structure émotionnelle, confrontation avec les responsabilités familiales.

**Conseil :** Les conjonctions sont des moments de **concentration d'énergie**. Utilisez-les pour lancer des projets liés aux planètes concernées.

---

#### 6.2 Opposition (180°) ☍

**Symbole :** Polarité, miroir
**Énergie :** Tension créative, prise de conscience

**Explication :**
Deux planètes se font face, comme deux pôles opposés. Cette tension peut créer des conflits ou des prises de conscience.

**Manifestation concrète :**
- Mars opposition Vénus natal : Désirs contradictoires entre indépendance et relation, passion et harmonie.
- Uranus opposition Mercure natal : Pensées disruptives, révélations soudaines, besoin de liberté intellectuelle.

**Conseil :** Les oppositions vous invitent à **intégrer les deux pôles**. Cherchez l'équilibre plutôt que de choisir un camp.

---

#### 6.3 Carré (90°) □

**Symbole :** Friction, obstacle
**Énergie :** Défi à surmonter, croissance par l'effort

**Explication :**
Deux planètes forment un angle de 90°, créant une friction. C'est inconfortable, mais c'est cette friction qui génère la croissance.

**Manifestation concrète :**
- Saturne carré Soleil natal : Sentiment de limitation, épreuves de confiance en soi, besoin de prouver sa valeur.
- Pluton carré Vénus natal : Transformation intense des relations, remise en question des dynamiques amoureuses.

**Conseil :** Les carrés sont des **moments d'action nécessaire**. Accueillez le défi comme une opportunité de renforcement.

---

#### 6.4 Trigone (120°) △

**Symbole :** Fluidité, harmonie
**Énergie :** Opportunité naturelle, facilité

**Explication :**
Deux planètes forment un angle de 120°, elles se soutiennent mutuellement. L'énergie circule sans effort.

**Manifestation concrète :**
- Jupiter trigone Soleil natal : Chance naturelle, expansion facile, confiance et optimisme.
- Neptune trigone Lune natale : Sensibilité créative accrue, inspiration artistique, compassion.

**Conseil :** Les trigones sont des **portes ouvertes**. Profitez-en pour agir sans forcer. Attention toutefois à ne pas rester passif : les trigones apportent des opportunités, mais vous devez les saisir.

---

### Écran de détail d'un transit

Lorsque vous appuyez sur un transit dans la liste, vous accédez à un écran détaillé :

**Informations affichées :**
1. **Nom du transit** : "Mars carré Saturne natal"
2. **Date exacte** : "25 janvier 2026, 14h30"
3. **Planètes impliquées** :
   - Mars en transit (position actuelle dans le ciel)
   - Saturne natal (position dans votre thème)
4. **Type d'aspect** : Carré (90°)
5. **Explication factuelle** : Que signifie cet aspect ?
6. **Manifestation concrète** : Comment cela peut se traduire dans votre vie ?
7. **Conseils pratiques** : Comment naviguer cette énergie ?

**Exemple fictif de contenu :**
```
Mars carré Saturne natal
25 janvier 2026

Explication :
Mars (action, désir, volonté) forme un carré avec votre Saturne natal (structure, limites, discipline). Cette configuration crée une tension entre votre envie d'avancer rapidement et les contraintes de la réalité.

Manifestation :
Vous pourriez ressentir de la frustration face à des retards ou des obstacles dans vos projets. Votre énergie est là, mais les circonstances semblent freiner vos élans. C'est une invitation à ralentir et à structurer vos actions.

Conseils :
1. Canalisez votre énergie avec discipline (sport, travail méthodique).
2. Acceptez que certaines choses prennent du temps.
3. Évitez les conflits d'autorité : choisissez vos batailles avec sagesse.
```

**Ton :** Factuel, pédagogique, sans catastrophisme. L'objectif est de vous donner des **clés de compréhension**, pas de vous inquiéter.

---

## 7. Mini Journal

Le **Mini Journal** est un outil simple et puissant pour ancrer vos observations quotidiennes et faire le lien avec vos cycles lunaires.

### Comment créer une entrée ?

**Depuis l'écran Home :**
1. Appuyez sur le **Journal Prompt** ("As-tu écrit aujourd'hui ?")
2. Vous êtes redirigé vers l'écran **Journal**

**Écran Journal :**
- **Formulaire de création** :
  - **Date** : Automatiquement définie sur aujourd'hui (modifiable)
  - **Humeur** : Sélectionnez une humeur parmi 5 options (calme, joyeux, anxieux, triste, énergique)
  - **Note** : Champ de texte libre (500 caractères max)
- **Bouton "Enregistrer"** : Sauvegarde l'entrée

**Limite :** 1 entrée par jour maximum. Si vous créez une entrée alors qu'une existe déjà pour aujourd'hui, l'ancienne est remplacée.

---

### Lien automatique au cycle lunaire

Chaque entrée de journal est **automatiquement liée** au cycle lunaire en cours.

**Comment ça marche ?**
Lorsque vous créez une entrée le 20 janvier 2026, Lunation détecte que vous êtes dans votre révolution lunaire de janvier 2026 (ex : "15 janvier - 12 février"). L'entrée est donc liée à ce cycle spécifique.

**Pourquoi c'est utile ?**
Vous pouvez ensuite filtrer vos entrées par cycle lunaire et observer :
- "Quand ma Lune est en Maison 5, je me sens plus créatif et léger."
- "Mes révolutions lunaires avec ascendant Capricorne sont toujours des mois où je me concentre sur le travail."

C'est un **journal à la fois quotidien et cyclique**.

---

### Visualiser les entrées passées

**Écran Journal (onglet Historique) :**
- **Liste des entrées** : Toutes vos entrées classées par ordre chronologique décroissant (les plus récentes en haut)
- **Filtres** :
  - Par mois lunaire (ex : "Janvier 2026")
  - Par humeur (ex : "Toutes les entrées 'joyeux'")
  - Par période (ex : "Les 30 derniers jours")
- **Détail d'une entrée** : Date, humeur, note complète, cycle lunaire associé

**Exemple d'affichage fictif :**
```
Mes entrées :

20 janvier 2026 | Calme 😌
"Journée productive au travail. J'ai bouclé le dossier en retard. Sensation de clarté mentale."
Cycle : Janvier 2026 (Lune Maison 5, Asc. Taureau)

19 janvier 2026 | Énergique ⚡
"Envie de sortir, de voir du monde. J'ai appelé des amis pour organiser un brunch."
Cycle : Janvier 2026 (Lune Maison 5, Asc. Taureau)

18 janvier 2026 | Anxieux 😰
"Beaucoup de doutes sur mon projet perso. Je ne sais pas si je vais y arriver."
Cycle : Janvier 2026 (Lune Maison 5, Asc. Taureau)
```

**Fonctionnalité à venir :** Statistiques mensuelles (humeur dominante, nombre d'entrées, mots-clés récurrents).

---

### Conseils pour tenir un journal lunaire efficace

**1. Soyez régulier (mais bienveillant)**
L'idéal est d'écrire chaque jour, même 2 phrases. Mais si vous sautez un jour, ce n'est pas grave. Reprenez le lendemain.

**2. Notez des faits et des émotions**
Mélangez observations concrètes ("Réunion importante au bureau") et ressentis ("Je me sentais confiant").

**3. Relisez en fin de cycle**
À la fin de chaque révolution lunaire (tous les 28 jours), relisez vos entrées du mois. Vous verrez des patterns émerger.

**4. Connectez-vous aux transits**
Si vous savez qu'un transit important arrive (ex : "Mars carré Saturne le 25 janvier"), notez vos ressentis ce jour-là. Cela vous aide à valider (ou invalider) les prédictions astrologiques.

**5. Soyez honnête**
Votre journal est privé. Écrivez sans filtre, sans jugement. C'est votre espace de vérité.

---

## 8. FAQ

### Questions générales

**Q : Lunation est-il gratuit ?**
R : Le MVP (version actuelle) est gratuit. Des fonctionnalités premium pourraient être ajoutées dans le futur (ex : rapports PDF, analyses avancées).

**Q : Mes données sont-elles sécurisées ?**
R : Oui. Vos données de naissance et vos entrées de journal sont stockées de manière sécurisée et ne sont jamais partagées avec des tiers. Elles servent uniquement aux calculs astrologiques.

**Q : L'application fonctionne-t-elle hors ligne ?**
R : Partiellement. Vous pouvez consulter vos rapports lunaires et entrées de journal déjà téléchargés. Les calculs astrologiques nécessitent une connexion internet.

**Q : Lunation est-il disponible sur Android et iOS ?**
R : Oui ! L'application est développée avec Expo (React Native) et fonctionne sur les deux plateformes.

---

### Questions sur le thème natal

**Q : Je ne connais pas mon heure de naissance exacte. Que faire ?**
R : Consultez votre acte de naissance officiel (disponible en mairie) ou demandez à vos parents. Sans heure précise, l'ascendant et les maisons ne peuvent pas être calculés correctement, ce qui réduit la précision des révolutions lunaires.

**Q : Puis-je modifier mes données de naissance après inscription ?**
R : Oui, dans les paramètres de l'application. Attention : modifier vos données recalculera entièrement votre thème natal et vos révolutions lunaires.

**Q : Pourquoi mon ascendant est différent de mon signe solaire ?**
R : Le signe solaire (ex : "je suis Bélier") correspond à la position du Soleil à votre naissance. L'ascendant correspond au signe qui se levait à l'horizon à l'heure exacte de votre naissance. Ce sont deux informations différentes et complémentaires.

---

### Questions sur les révolutions lunaires

**Q : Combien de révolutions lunaires ai-je par an ?**
R : Environ 13 (12-13 cycles selon l'année). Chaque révolution dure environ 28 jours.

**Q : Ma révolution lunaire change-t-elle chaque mois ?**
R : Oui. Chaque mois, la Lune retourne à sa position natale à un moment différent, créant un nouveau thème lunaire avec un nouvel ascendant et une nouvelle maison.

**Q : Puis-je consulter les révolutions lunaires futures ?**
R : Oui. Lunation génère automatiquement vos 12 prochains mois de révolutions lunaires. Vous pouvez les consulter dans l'écran "Révolutions Lunaires".

---

### Questions sur le VoC

**Q : Le VoC dure combien de temps ?**
R : De quelques minutes à plusieurs heures. Rarement plus de 24h. La durée varie selon la vitesse de la Lune et les aspects qu'elle forme.

**Q : Dois-je vraiment éviter toute action pendant le VoC ?**
R : Non. Le VoC est un **indicateur**, pas une interdiction. Si vous avez une urgence ou une opportunité unique, agissez. Soyez simplement conscient qu'il peut y avoir des ajustements futurs.

**Q : Comment savoir si je suis en VoC en ce moment ?**
R : Consultez le **VoC Widget** sur l'écran Home. Il affiche en temps réel le statut VoC.

---

### Questions sur les transits

**Q : Pourquoi Lunation ne montre que les transits majeurs ?**
R : Il y a des centaines de transits quotidiens. Lunation filtre pour ne garder que les **4 aspects majeurs** (conjonction, opposition, carré, trigone), qui sont les plus significatifs et les plus faciles à observer dans votre vie.

**Q : Un transit négatif signifie-t-il qu'il va m'arriver quelque chose de grave ?**
R : Non. Un carré ou une opposition peut être inconfortable, mais c'est souvent un **catalyseur de croissance**. L'astrologie décrit des énergies, pas des événements figés. Votre réaction et vos choix font la différence.

**Q : Combien de temps dure un transit ?**
R : Cela dépend de la vitesse de la planète en transit. Un transit rapide (Lune, Mercure, Vénus, Mars) dure quelques heures à quelques jours. Un transit lent (Jupiter, Saturne, Uranus, Neptune, Pluton) peut durer plusieurs semaines à plusieurs mois.

---

### Questions sur le journal

**Q : Mon journal est-il privé ?**
R : Oui. Personne d'autre que vous n'a accès à vos entrées de journal. Elles sont stockées dans votre compte sécurisé.

**Q : Puis-je exporter mon journal ?**
R : Pas encore dans le MVP. Cette fonctionnalité pourrait être ajoutée dans une version future (export PDF ou CSV).

**Q : Puis-je écrire plusieurs entrées par jour ?**
R : Non. Lunation limite à 1 entrée par jour pour encourager la concision et la régularité.

---

### Questions techniques

**Q : L'application consomme-t-elle beaucoup de données ?**
R : Non. Les appels API sont légers (quelques Ko par requête). Seule la première synchronisation (calcul du thème natal) nécessite un peu plus de données.

**Q : Puis-je utiliser Lunation sur plusieurs appareils ?**
R : Oui, si vous vous connectez avec le même compte. Vos données sont synchronisées via le backend.

**Q : Comment contacter le support ?**
R : Via l'écran "Paramètres" > "Support" ou par email à support@astroia.com.

---

## Conclusion

**Lunation** est bien plus qu'une application d'astrologie : c'est un **compagnon de route** pour mieux comprendre vos cycles émotionnels et énergétiques.

En suivant vos révolutions lunaires mois après mois, en consultant les fenêtres VoC, en observant les transits majeurs et en tenant votre journal, vous développez une **intelligence cyclique** qui vous aide à naviguer votre vie avec plus de clarté et d'intention.

L'astrologie n'est pas une science exacte, mais un **langage symbolique** pour décrire les rythmes du cosmos et leurs résonances en nous. Utilisez Lunation avec curiosité, bienveillance et discernement.

**Bon voyage lunaire !** 🌙

---

**Fait avec 🌙 et ⭐ par l'équipe Astroia**
Version 1.0.0 — Janvier 2026
