# 💕 SPRINT 8 - COMPATIBILITÉ AMOUREUSE & AMICALE

**Date :** 5 novembre 2025  
**Objectif :** Module de compatibilité universelle (couple, amis, collègues)

---

## 🎯 VISION

Un module complet pour analyser la compatibilité entre deux personnes :
- 💑 **Couple** : Compatibilité amoureuse
- 🤝 **Amis** : Compatibilité amicale
- 💼 **Collègues** : Compatibilité professionnelle

**Basé sur :**
- Signes astrologiques (Soleil, Lune, Ascendant)
- Éléments (Feu, Terre, Air, Eau)
- Aspects planétaires (Trigone, Sextile, Carré, Opposition)
- Synastrie (comparaison des thèmes)

---

## 📋 FONCTIONNALITÉS

### 1. Sélection du Type de Relation 🎭
- [ ] 3 boutons : Couple 💑 / Amis 🤝 / Collègues 💼
- [ ] Design : Cards avec icônes
- [ ] Sélection exclusive (radio button)

### 2. Saisie des 2 Personnes 👥
- [ ] **Personne 1** (Vous) : Auto-rempli depuis profil
  - Nom (optionnel)
  - Signe solaire
  - Signe lunaire
  - Ascendant
- [ ] **Personne 2** : Formulaire complet
  - Nom (optionnel)
  - Signe solaire
  - Signe lunaire
  - Ascendant

### 3. Analyse Intelligente 🤖
- [ ] Score global 0-100%
- [ ] Scores détaillés :
  - 💬 Communication
  - 🔥 Passion/Énergie
  - 🤝 Complicité
  - 🎯 Objectifs communs
- [ ] Graphique radar (optionnel)

### 4. Résultats Personnalisés 📊
- [ ] Score principal avec emoji animé
- [ ] Interprétation selon le type de relation :
  - Couple : Focus sur amour, passion, engagement
  - Amis : Focus sur complicité, valeurs, fun
  - Collègues : Focus sur collaboration, objectifs, communication
- [ ] Points forts (3-4)
- [ ] Points d'attention (2-3)
- [ ] Conseils personnalisés

### 5. Synastrie Détaillée 🌟
- [ ] Aspects planétaires :
  - Soleil-Soleil (identité)
  - Lune-Lune (émotions)
  - Vénus-Mars (attraction)
- [ ] Compatibilité élémentaire
- [ ] Maisons astrologiques (si disponible)

### 6. Historique & Partage 💾
- [ ] Sauvegarder les analyses
- [ ] Comparer plusieurs personnes
- [ ] Partager le résultat
- [ ] Export PDF (optionnel)

---

## 🎨 DESIGN

### Palette
- **Couple** : Dégradé rouge-rose `['#FF1744', '#F50057', '#E91E63']`
- **Amis** : Dégradé jaune-orange `['#FFB300', '#FF6F00', '#F57C00']`
- **Collègues** : Dégradé bleu-cyan `['#00B0FF', '#0091EA', '#01579B']`

### Structure
```
┌─────────────────────────┐
│   💑 Compatibilité      │
│        Amoureuse        │
├─────────────────────────┤
│  Choisir le type :      │
│  [Couple] [Amis] [Pro]  │
├─────────────────────────┤
│  👤 Vous                │
│  ♈ Bélier               │
│  (Auto depuis profil)   │
├─────────────────────────┤
│  👤 Autre personne      │
│  Nom : [Input]          │
│  Signes : [Selects]     │
├─────────────────────────┤
│  [Analyser] 💫          │
└─────────────────────────┘

Résultat :
┌─────────────────────────┐
│       💑 87%            │
│  Très Compatible        │
├─────────────────────────┤
│  💬 Communication  92%  │
│  🔥 Passion        85%  │
│  🤝 Complicité     83%  │
│  🎯 Objectifs      88%  │
├─────────────────────────┤
│  ✨ Points forts        │
│  • Excellent dialogue   │
│  • Valeurs communes     │
│  • Attraction forte     │
├─────────────────────────┤
│  ⚠️  Points d'attention │
│  • Gérer les conflits  │
│  • Respecter l'espace  │
└─────────────────────────┘
```

---

## 🤖 CALCUL DE COMPATIBILITÉ

### Score Global (0-100)
```
Score = (
  compatibilité_éléments × 30% +
  aspects_planétaires × 30% +
  synastrie_lune × 20% +
  ascendants × 20%
)
```

### Scores Détaillés
- **Communication** : Mercure + Air signs
- **Passion** : Vénus-Mars + Feu signs
- **Complicité** : Lune + Eau signs
- **Objectifs** : Ascendant + Terre signs

---

## 📊 TABLES SUPABASE

```sql
CREATE TABLE compatibility_analyses (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES auth.users(id),
  relation_type VARCHAR(20), -- couple, friends, colleagues
  
  -- Personne 1
  person1_name VARCHAR(100),
  person1_sun INTEGER,
  person1_moon INTEGER,
  person1_ascendant INTEGER,
  
  -- Personne 2
  person2_name VARCHAR(100),
  person2_sun INTEGER,
  person2_moon INTEGER,
  person2_ascendant INTEGER,
  
  -- Résultats
  global_score INTEGER,
  communication_score INTEGER,
  passion_score INTEGER,
  complicity_score INTEGER,
  goals_score INTEGER,
  
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🚀 IMPLÉMENTATION

### Étapes
1. **Service `compatibilityAnalysisService.js`** (30 min)
   - Calcul scores détaillés
   - Aspects planétaires
   - Génération recommandations

2. **UI Sélection Type** (20 min)
   - 3 cards : Couple, Amis, Collègues
   - Animation selection

3. **Formulaire 2 Personnes** (30 min)
   - Auto-fill personne 1 depuis profil
   - Saisie personne 2

4. **Écran Résultat** (1h)
   - Score global animé
   - 4 scores détaillés avec barres
   - Points forts / attention
   - Conseils personnalisés

5. **Stockage & Partage** (20 min)
   - Table Supabase
   - Historique
   - Bouton partage

**Durée totale : ~3h**

---

## 🎯 RÉSULTAT FINAL

**Module Compatibilité Universelle :**
- 💑 3 types de relations
- 📊 5 scores détaillés
- 🎨 Design adaptatif (couleur selon type)
- ✨ Animations émotionnelles
- 💾 Historique complet
- 📤 Partage social
- 🤖 Calculs astrologiques avancés

---

## 💡 BONUS (Optionnel)

- [ ] Graphique radar des scores
- [ ] Comparaison avec plusieurs personnes
- [ ] "Match du jour" (suggestion IA)
- [ ] Export PDF du rapport
- [ ] Mode "Blind test" (devine la compatibilité)

---

**Prêt à démarrer le Sprint 8 ? 🚀**

