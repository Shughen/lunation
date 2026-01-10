# 🌙 Fonctionnalité Cycle & Astrologie

## 📋 Résumé

Cette fonctionnalité combine le **cycle menstruel** avec les **transits astrologiques** pour fournir des recommandations personnalisées sur l'énergie, l'humeur et les activités recommandées.

## 🎯 Concept

**Marché ciblé** : Femmes FR 16-45 ans, wellness + spiritualité

**Différenciation** : 
- ✅ **ZÉRO concurrence FR directe** (Elia c'est fun, pas sérieux)
- ✅ Combine cycle menstruel + thème natal + transits lunaires
- ✅ Gen Z FR cherche activement ce type de solution
- ✅ Rétention haute (suivi quotidien = habit building)

## 🚀 Comment tester

### 1. Lancer l'app
```bash
npm start
```

### 2. Navigation
1. **Page d'accueil** → Nouveau bouton **"Cycle & Astrologie"** 🌙 (couleur rose)
2. Clique dessus

### 3. Formulaire
Tu dois renseigner :
- **Jour du cycle** : Entre 1 et 35 (ex: 14 pour ovulation)
- **Phase du cycle** : 
  - 🌑 Menstruelle (1-5 jours) - Énergie basse, repos
  - 🌒 Folliculaire (6-13 jours) - Énergie montante, créativité
  - 🌕 Ovulation (14-16 jours) - Énergie maximale, sociabilité
  - 🌘 Lutéale (17-28 jours) - Énergie stable, organisation
- **Humeur** : ⚡ Énergique / 😌 Calme / 🎨 Créative / 😴 Fatiguée / 😤 Irritable / 🥺 Émotive
- **Symptômes** (optionnel) : Texte libre

### 4. Résultat
Après l'analyse, tu verras :
- 🌙 **Phase lunaire actuelle** + Signe du zodiaque
- 📊 **Niveau d'énergie cosmique** (20-100%)
- 🌟 **Transits du jour** (Lune en quel signe + aspect)
- ✨ **Activités recommandées** (ex: Yoga doux, Présentation publique, etc.)
- 💡 **Conseils personnalisés** (basés sur phase + transits + thème natal)

### 5. Dashboard
- Va dans le **Dashboard** (bouton en page d'accueil)
- Tu verras :
  - 🌙 **Statistique "Cycle & Astro"** : Nombre d'analyses effectuées
  - 🌙 **Filtre "Cycle & Astro"** : Dans l'historique pour afficher uniquement ces analyses
  - 📊 **Historique complet** : Toutes tes analyses avec possibilité de supprimer

## 🧪 Scénarios de test

### Scénario 1 : Énergie haute
- **Phase** : Ovulation (jour 14)
- **Humeur** : Énergique
- **Résultat attendu** : 
  - Énergie cosmique > 80%
  - Recommandations : Présentation publique, socialisation, sport intense
  - Transits harmonieux

### Scénario 2 : Repos nécessaire
- **Phase** : Menstruelle (jour 2)
- **Humeur** : Fatiguée
- **Résultat attendu** :
  - Énergie cosmique < 60%
  - Recommandations : Yoga doux, lecture, repos, hydratation
  - Conseils de ressourcement

### Scénario 3 : Créativité
- **Phase** : Folliculaire (jour 10)
- **Humeur** : Créative
- **Résultat attendu** :
  - Énergie cosmique 70-85%
  - Recommandations : Nouveaux projets, activités artistiques, cardio
  - Encouragement à sortir de la zone de confort

## 📂 Fichiers créés/modifiés

### Nouveaux fichiers
1. **`app/cycle-astro/index.js`** (23KB)
   - Interface complète avec formulaire et résultats
   - Gestion des états et animations
   - Intégration avec le profil utilisateur

2. **`lib/api/cycleAstroService.js`** (13KB)
   - Calcul de la position lunaire
   - Calcul du niveau d'énergie (cycle + transits + thème natal)
   - Génération des recommandations personnalisées
   - Sauvegarde AsyncStorage + Supabase

### Fichiers modifiés
3. **`app/(tabs)/home.js`**
   - Ajout du bouton "Cycle & Astrologie" avec icône 🌙

4. **`app/dashboard/index.js`**
   - Ajout de la statistique "Cycle & Astro"
   - Ajout du filtre dans l'historique
   - Gestion de l'affichage des analyses cycle-astro

5. **`lib/api/dashboardService.js`**
   - Intégration des stats cycleAstroAnalyses
   - Récupération de l'historique depuis AsyncStorage + Supabase
   - Gestion de la suppression

## 🎨 Design

- **Couleur principale** : Rose (#EC4899) pour différencier de Parent-Enfant (violet)
- **Icône** : 🌙 (Lune)
- **Style** : Cohérent avec le reste de l'app (dark mode, gradients)

## 🔍 Logique métier

### Calcul du niveau d'énergie

```
Énergie = Base * Multiplicateur_Phase + Bonus_Compatibilité + Bonus_Transit

Où :
- Base = 70
- Multiplicateur_Phase :
  - Menstruelle : 0.5
  - Folliculaire : 0.8
  - Ovulation : 1.0
  - Lutéale : 0.7
- Bonus_Compatibilité : +10 si élément du signe = élément de la phase
- Bonus_Transit : +15 si Lune en harmonie avec signe natal
```

### Éléments astrologiques

- **Feu** (Bélier, Lion, Sagittaire) : Action, énergie haute
- **Terre** (Taureau, Vierge, Capricorne) : Stabilité, concret
- **Air** (Gémeaux, Balance, Verseau) : Communication, idées
- **Eau** (Cancer, Scorpion, Poissons) : Émotions, intuition

### Harmonies élémentaires

- **Feu + Air** : Très compatible (le feu a besoin d'air)
- **Terre + Eau** : Très compatible (l'eau nourrit la terre)
- **Feu + Eau** : Opposés (conflictuel)
- **Terre + Air** : Opposés (difficile)

## ✅ Checklist de test

- [ ] Lancer l'app sans erreur
- [ ] Voir le bouton "Cycle & Astrologie" sur la page d'accueil
- [ ] Cliquer et accéder au formulaire
- [ ] Remplir le formulaire avec des données valides
- [ ] Lancer l'analyse et voir les résultats
- [ ] Vérifier que les recommandations sont pertinentes
- [ ] Refaire une nouvelle analyse
- [ ] Aller au Dashboard
- [ ] Vérifier que la stat "Cycle & Astro" s'affiche
- [ ] Filtrer par "Cycle & Astro" dans l'historique
- [ ] Supprimer une analyse
- [ ] Tester avec différentes phases du cycle
- [ ] Tester avec différentes humeurs

## 🐛 Points d'attention

1. **Profil incomplet** : Si l'utilisateur n'a pas renseigné son profil astral, un message s'affiche pour l'inviter à le compléter
2. **Validation** : Le jour du cycle doit être entre 1 et 35
3. **Sauvegarde** : Les données sont sauvegardées localement (AsyncStorage) ET en ligne (Supabase si connecté)
4. **Transit lunaire** : Calcul approximatif (simplifié) - peut être amélioré avec une vraie API d'éphémérides

## 🚀 Améliorations futures possibles

1. **Calendrier visuel** : Vue calendrier du cycle avec prédictions
2. **Graphiques** : Courbes d'énergie sur plusieurs jours
3. **Notifications** : Rappels pour tracker quotidiennement
4. **Intégration santé** : Sync avec Apple Health / Google Fit
5. **API éphémérides** : Position lunaire précise en temps réel
6. **Statistiques avancées** : Corrélations cycle/humeur sur plusieurs mois
7. **Export PDF** : Rapport mensuel téléchargeable

## 📊 Métriques de succès

- **Rétention** : Suivi quotidien → habit building
- **Engagement** : Nombre d'analyses par utilisatrice
- **Satisfaction** : Pertinence des recommandations
- **Partage** : Taux de partage sur réseaux sociaux

## 🎯 Positionnement marché

**Concurrent principal** : Elia (menstruoscope basique)

**Notre différenciation** :
- ✅ Analyse complète (thème natal + transits + cycle)
- ✅ Recommandations concrètes et actionnables
- ✅ Interface moderne et engageante
- ✅ 100% en français
- ✅ Gratuit (vs Co-Star payant)

**Audience cible** :
- Femmes 16-45 ans
- Intéressées par wellness + spiritualité
- Gen Z FR (80% s'intéressent à l'astrologie)
- Cherchent à mieux comprendre leur cycle

---

**🎉 Prêt à tester !** Lance `npm start` et va sur la page d'accueil pour voir le nouveau bouton. 🌙

