# 🚀 Déploiement de l'API ML Parent-Enfant

## 📦 Fichiers ajoutés

```
api/ml/
  ├── parent-child.py        (API Python avec modèle ML)
  └── xgb_best.pkl          (Modèle XGBoost 3.4 MB)

requirements.txt            (Dépendances Python)
vercel.json                 (Configuration mise à jour)
```

---

## 🔧 Déploiement sur Vercel

### Option 1 : Via l'interface Vercel (Recommandé)

1. **Push vers Git**
   ```bash
   cd /Users/remibeaurain/astroia/astro-ia-api
   git add .
   git commit -m "feat: Add ML parent-child prediction API"
   git push origin main
   ```

2. **Vercel auto-déploiera** automatiquement via GitHub

3. **Vérifier** : https://astro-ia-niei71xao-remibeaurain-4057s-projects.vercel.app/api/ml/parent-child

---

### Option 2 : Via CLI Vercel

```bash
cd /Users/remibeaurain/astroia/astro-ia-api

# Installer Vercel CLI si nécessaire
npm install -g vercel

# Déployer
vercel --prod
```

---

## ✅ Test de l'API

### Avec curl :

```bash
curl -X POST https://astro-ia-niei71xao-remibeaurain-4057s-projects.vercel.app/api/ml/parent-child \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {
      "sun_sign": 5,
      "moon_sign": 8,
      "ascendant": 2,
      "mercury": 5,
      "venus": 6,
      "mars": 4
    },
    "enfant": {
      "sun_sign": 3,
      "moon_sign": 7,
      "ascendant": 11,
      "mercury": 3,
      "venus": 3,
      "mars": 9
    },
    "age_diff": 28
  }'
```

### Réponse attendue :

```json
{
  "success": true,
  "prediction": 1,
  "compatibility_score": 87,
  "probability": {
    "difficile": 0.1294,
    "harmonieuse": 0.8706
  },
  "interpretation": {
    "level": "Excellente",
    "emoji": "💚",
    "title": "Relation très harmonieuse",
    "description": "..."
  },
  "recommendations": [...],
  "model_accuracy": 98.19
}
```

---

## 📱 Test dans l'app mobile

1. **Lancer Expo**
   ```bash
   cd /Users/remibeaurain/astroia/astroia-app
   npx expo start --clear
   ```

2. **Naviguer vers** "Parent-Enfant IA" depuis la page d'accueil

3. **Sélectionner** les signes astrologiques parent/enfant

4. **Cliquer** "Analyser la compatibilité"

5. **Voir** le résultat avec :
   - Score de compatibilité (0-100%)
   - Interprétation détaillée
   - Recommandations personnalisées
   - Détails techniques du modèle

---

## 🔍 Troubleshooting

### Erreur 500 (Modèle non trouvé)

**Cause :** Le fichier `xgb_best.pkl` n'est pas déployé

**Solution :**
```bash
# Vérifier que le fichier existe
ls -lh api/ml/xgb_best.pkl

# S'assurer qu'il n'est pas dans .gitignore
cat .gitignore | grep pkl

# Si dans .gitignore, le retirer pour ce fichier spécifique
# Puis commit et push
```

### Erreur 413 (Payload trop grand)

**Cause :** Le modèle .pkl (3.4 MB) dépasse la limite

**Solution :** Le modèle est déjà optimal. Vercel supporte jusqu'à 50 MB par fichier.

### Erreur de dépendances Python

**Cause :** requirements.txt incomplet

**Solution :**
```bash
# Vérifier requirements.txt
cat requirements.txt

# Devrait contenir :
# joblib>=1.3.0
# numpy>=1.24.0
# scikit-learn>=1.3.0
# xgboost>=2.0.0
```

---

## 🎯 Prochaines améliorations

1. **Cache des prédictions** (Redis/Vercel KV)
2. **Batch predictions** (analyser plusieurs enfants)
3. **Explainability** (feature importance avec SHAP)
4. **A/B testing** (comparer plusieurs modèles)
5. **Monitoring** (logs des prédictions, temps de réponse)

---

## 📊 Caractéristiques du modèle

- **Type :** XGBoost Classifier
- **Précision :** 98.19% ROC-AUC
- **Dataset :** 500,000 profils parent-enfant
- **Trials Optuna :** 2500
- **Temps d'entraînement :** 5h27
- **Features :** 20 (signes astrologiques + calculs)
- **Taille :** 3.4 MB

---

**Modèle prêt à l'emploi ! 🤖✨**

