# 🧪 CHECKLIST DE TEST - LUNA v1.0

**Date:** 10 novembre 2025  
**Testeur:** Rémi  
**Environnement:** Expo Go (iOS)

---

## 🏠 **1. ÉCRAN HOME**

### 1.1 CycleCard
- [ ] Affiche le jour du cycle (ex: "Jour 11/24")
- [ ] Affiche la phase correcte (Menstruelle / Folliculaire / Ovulatoire / Lutéale)
- [ ] Affiche le % d'énergie (ex: "Énergie : 80%")
- [ ] Badge "Fertile" visible si en période d'ovulation
- [ ] Badge "Fertilité moyenne" visible si proche ovulation
- [ ] Tap → ouvre `/settings/cycle` avec historique

### 1.2 MoodCard
- [ ] Affiche "Aucune humeur aujourd'hui" si pas d'entrée
- [ ] Si humeur du jour → affiche emoji + texte
- [ ] Bouton "Ouvrir le journal" → va à `/journal`
- [ ] Bouton rapide mood → ouvre modal inline

### 1.3 AstroCard
- [ ] Affiche le mantra du jour basé sur la Lune
- [ ] Affiche le signe lunaire actuel (ex: "🌙 en Scorpion")
- [ ] Tap → ouvre `/astro` avec horoscope détaillé

### 1.4 ExploreGrid
- [ ] 6 tuiles visibles : Compatibilité couple, Parent-Enfant, Thème natal, Chat IA, Journal, Paramètres
- [ ] Tap sur chaque tuile → navigation correcte
- [ ] Icônes et textes bien alignés

---

## 🌙 **2. THÈME NATAL**

### 2.1 Calcul
- [ ] Si pas de données astro → affiche "Calcule ton thème natal"
- [ ] Saisir date/heure/lieu → calcul Swiss Ephemeris
- [ ] Affiche Soleil, Lune, Ascendant, et 7 autres planètes
- [ ] Positions en degrés correctes (ex: "Soleil : 17°43' en Scorpion")

### 2.2 Visualisation
- [ ] Roue zodiacale avec 12 signes en cercle
- [ ] Planètes positionnées au bon angle (trigonométrie)
- [ ] Labels lisibles (pas de chevauchement)
- [ ] Scroll vertical fonctionne pour voir détails

### 2.3 Insights
- [ ] 3-5 insights générés (forces, défis, conseil cycle)
- [ ] Texte adapté au cycle actuel
- [ ] Emojis présents et pertinents

---

## 💑 **3. COMPATIBILITÉ**

### 3.1 Couple
- [ ] **Personne 1 (Auto)** : Soleil, Ascendant, Lune auto-remplis depuis profil
- [ ] Badge "Auto" vert visible sur les 3 champs
- [ ] **Scroll automatique** : Les 3 pickers se positionnent sur les bons signes
- [ ] **Personne 2 (Manuel)** : Saisir nom + 3 signes manuellement
- [ ] Bouton "Analyser" → calcul compatibilité
- [ ] Score global affiché (ex: "78%")
- [ ] 3 scores détaillés : Émotionnel, Intellectuel, Physique
- [ ] Texte d'analyse pertinent

### 3.2 Parent-Enfant
- [ ] Même logique que couple
- [ ] Parent auto-rempli
- [ ] Enfant manuel
- [ ] ML XGBoost utilisé pour analyse
- [ ] Recommandations éducatives affichées

### 3.3 Amitié
- [ ] Même logique
- [ ] Focus sur complicité et communication

---

## 💬 **4. CHAT IA**

### 4.1 Conversation
- [ ] Premier message → affiche "Salut [Prénom] 🌙"
- [ ] Contexte automatique : cycle + humeur + astro injecté
- [ ] Réponses pertinentes et personnalisées
- [ ] Scroll fluide
- [ ] Loader pendant réponse IA

### 4.2 Contexte
- [ ] IA mentionne la phase du cycle si pertinent
- [ ] IA adapte conseils selon énergie (ex: "Je vois que tu es en phase folliculaire...")
- [ ] IA utilise le profil astro (ex: "En tant que Scorpion...")

---

## 📓 **5. JOURNAL**

### 5.1 Nouvelle entrée
- [ ] Bouton "+" → modal création
- [ ] Sélection humeur (5 emojis)
- [ ] Texte libre (placeholder pertinent)
- [ ] Tags automatiques (optionnel)
- [ ] Sauvegarde → retour liste

### 5.2 Liste
- [ ] Entrées triées par date (plus récente en haut)
- [ ] Affiche emoji + date + extrait texte
- [ ] Tap → ouvre détail complet
- [ ] Scroll infini si 50+ entrées

### 5.3 Édition/Suppression
- [ ] Tap sur entrée → modal édition
- [ ] Modifier humeur ou texte
- [ ] Bouton supprimer → confirmation
- [ ] Suppression → mise à jour liste

---

## ⚙️ **6. PARAMÈTRES**

### 6.1 Profil
- [ ] Modifier nom, prénom, date de naissance
- [ ] Sauvegarder → profil mis à jour
- [ ] Impact sur auto-fill compatibilité

### 6.2 Cycle
- [ ] Saisir date dernières règles
- [ ] Saisir durée cycle habituelle (21-35 jours)
- [ ] Sauvegarder → CycleCard se met à jour
- [ ] DateTimePicker natif iOS/Android

### 6.3 Données astrologiques
- [ ] Modifier lieu de naissance
- [ ] Recalcul thème si changement
- [ ] Validation coordonnées

### 6.4 Consentement
- [ ] Toggle analytics Mixpanel
- [ ] Texte RGPD visible
- [ ] Lien "En savoir plus" → `/settings/data-policy`

### 6.5 À propos
- [ ] Version app affichée
- [ ] Liens : Avertissement médical, Politique données, Contact
- [ ] Tap → ouvre pages dédiées

---

## 🎯 **7. NAVIGATION & UX**

### 7.1 Tab bar
- [ ] 3 onglets : Home, Profil, Chat
- [ ] Labels accessibilité VoiceOver
- [ ] Badge notifications si pertinent

### 7.2 Back navigation
- [ ] Toutes les sous-pages ont un header avec retour
- [ ] Bouton "<" fonctionne partout
- [ ] Pas de navigation bloquée

### 7.3 Animations
- [ ] Transitions fluides entre pages
- [ ] Haptic feedback sur boutons importants
- [ ] Pas de lag à 60fps

### 7.4 Accessibilité
- [ ] Labels VoiceOver sur tous les boutons
- [ ] Contraste WCAG AA respecté
- [ ] Taille texte adaptative

---

## ⚡ **8. PERFORMANCE**

- [ ] Lancement app < 3 secondes
- [ ] Navigation instantanée entre tabs
- [ ] Pas de crash pendant 5 min d'utilisation
- [ ] Scroll fluide partout
- [ ] Mémoire stable (pas de fuites)

---

## 🐛 **9. EDGE CASES**

- [ ] Pas de profil → affiche onboarding
- [ ] Pas de date cycle → affiche "Configure ton cycle"
- [ ] Pas de thème natal → affiche "Calcule ton thème"
- [ ] Pas d'internet → mode offline (données locales seulement)
- [ ] IA timeout → message d'erreur gracieux

---

## 📱 **10. BUGS CONNUS (À VÉRIFIER RÉSOLUS)**

- [x] ~~Natal chart planètes au milieu~~ → **FIXÉ**
- [x] ~~Compatibilité auto-fill ascendant/lune~~ → **FIXÉ**
- [x] ~~Compatibilité auto-scroll disparu~~ → **FIXÉ**
- [x] ~~`Platform` import manquant cycle.js~~ → **FIXÉ**
- [x] ~~Hooks rendered more than previous~~ → **FIXÉ**
- [x] ~~`person2.sunSign of undefined`~~ → **FIXÉ**

---

## ✅ **SYNTHÈSE**

**Total items:** ~80  
**Priorité haute:** Sections 1-3 (Home, Natal, Compatibilité)  
**Priorité moyenne:** Sections 4-6 (Chat, Journal, Paramètres)  
**Priorité basse:** Sections 7-10 (UX, Performance, Edge cases)

---

**Instructions:**
1. Teste dans l'ordre (Home → Natal → Compatibilité → reste)
2. Coche ✅ ce qui fonctionne
3. Note ❌ ce qui bug + screenshot/description
4. Retour complet ou au fur et à mesure

**Bon test !** 🚀

