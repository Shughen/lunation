# 🧪 TEST MANUEL - Fonctionnalité Parent-Enfant IA

---

## 📋 PRÉPARATION

### 1. Lancer l'app mobile
```bash
cd /Users/remibeaurain/astroia/astroia-app
npx expo start --clear
```

### 2. (Optionnel) Tester l'API directement

**Si l'API est déployée sur Vercel :**
```bash
curl -X POST https://astro-ia-niei71xao-remibeaurain-4057s-projects.vercel.app/api/ml/parent-child \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"sun_sign": 5, "moon_sign": 8, "ascendant": 2, "mercury": 5, "venus": 6, "mars": 4},
    "enfant": {"sun_sign": 3, "moon_sign": 7, "ascendant": 11, "mercury": 3, "venus": 3, "mars": 9},
    "age_diff": 28
  }'
```

**Attendu :** JSON avec `"success": true` et score ~70-90%

---

## 🎯 SCÉNARIOS DE TEST

### ✅ Test 1 : Navigation basique

1. **Ouvrir l'app** Astro.IA
2. **Vérifier** que la carte "Parent-Enfant IA" apparaît sur l'écran d'accueil
3. **Cliquer** sur la carte
4. **Vérifier** que l'écran s'ouvre avec :
   - Titre "🤖 Analyse IA"
   - Section Parent avec 3 sélecteurs
   - Section Enfant avec 3 sélecteurs
   - Bouton "Analyser la compatibilité"

**Résultat attendu :** ✅ Interface complète visible

---

### ✅ Test 2 : Sélection des signes

1. **Scroll** horizontal dans "Signe solaire" parent
2. **Sélectionner** "Lion ♌"
3. **Vérifier** que le bouton devient violet/actif
4. **Répéter** pour Lune et Ascendant parent
5. **Répéter** pour les 3 signes enfant

**Résultat attendu :** ✅ Sélections visuellement claires

---

### ✅ Test 3 : Analyse avec signes compatibles

**Configuration :**
- Parent : Soleil Lion (5), Lune Cancer (4), Ascendant Taureau (2)
- Enfant : Soleil Sagittaire (9), Lune Poissons (12), Ascendant Vierge (6)

**Actions :**
1. Configurer les signes
2. Cliquer "Analyser la compatibilité"
3. Observer le loader
4. Attendre la réponse (~3-5 secondes)

**Résultat attendu :**
- ✅ Score élevé (70-95%)
- ✅ Emoji vert 💚 ou bleu 💙
- ✅ Titre "Relation harmonieuse" ou mieux
- ✅ 3-4 recommandations affichées
- ✅ Détails techniques visibles

---

### ✅ Test 4 : Analyse avec signes opposés

**Configuration :**
- Parent : Soleil Bélier (1), Lune Bélier (1), Ascendant Bélier (1)
- Enfant : Soleil Balance (7), Lune Balance (7), Ascendant Balance (7)

**Actions :**
1. Configurer les signes (signes opposés = opposition)
2. Cliquer "Analyser"

**Résultat attendu :**
- ✅ Score moyen/faible (45-65%)
- ✅ Emoji jaune 💛 ou orange 🧡
- ✅ Recommandations de communication
- ✅ Mention des différences élémentaires

---

### ✅ Test 5 : Nouvelle analyse

1. Après avoir vu un résultat
2. Cliquer "Nouvelle analyse"
3. Vérifier le retour au formulaire
4. Modifier les signes
5. Relancer l'analyse

**Résultat attendu :** ✅ Formulaire réinitialisé, nouveau résultat

---

### ✅ Test 6 : Gestion d'erreur (API offline)

**Simulation :**
1. Mettre l'avion mode ON
2. Lancer une analyse
3. Observer l'erreur

**Résultat attendu :** ✅ Alert "Erreur" avec message clair

---

### ✅ Test 7 : Intégration profil utilisateur

**Si profil rempli :**
1. Aller dans Profil
2. Remplir date de naissance
3. Retourner à Parent-Enfant
4. Observer si les données parent sont pré-remplies

**Résultat attendu :** ✅ Données parent = profil utilisateur (si disponible)

---

## 🐛 BUGS À SURVEILLER

| Bug potentiel | Comment tester | Fix si présent |
|---------------|----------------|----------------|
| API timeout | Attendre >10 sec | Augmenter timeout Vercel |
| Modèle non trouvé | Appel API direct | Vérifier .pkl uploadé |
| Crash sélection signe | Cliquer rapidement | Debounce les clics |
| Scroll cassé sur Android | Test sur Android | Ajuster ScrollView |
| Erreur CORS | Console logs | Vérifier headers Vercel |

---

## 📊 MÉTRIQUES À RELEVER

Pendant les tests, noter :

- ⏱️ **Temps de réponse API** : _____ secondes
- 🎨 **UI fluide ?** : Oui / Non
- 📱 **Compatible iOS ?** : Oui / Non / Non testé
- 🤖 **Compatible Android ?** : Oui / Non / Non testé
- 💯 **Score pertinent ?** : Oui / Non
- 💬 **Recommandations utiles ?** : Oui / Non

---

## ✅ VALIDATION FINALE

Avant de considérer la fonctionnalité prête :

- [ ] Tous les tests passent
- [ ] API déployée et accessible
- [ ] Aucun crash observé
- [ ] Performance acceptable (<5 sec)
- [ ] UI cohérente avec le reste de l'app
- [ ] Recommandations personnalisées
- [ ] Gestion d'erreur propre

---

## 🎯 PROCHAINES ACTIONS

**Si tests OK :**
1. Déployer en production
2. Annoncer aux utilisateurs
3. Collecter feedback
4. Itérer sur recommandations

**Si bugs :**
1. Noter dans GitHub Issues
2. Prioriser (bloquant vs. mineur)
3. Fixer
4. Re-tester

---

**Bonne chance pour les tests ! 🚀**

