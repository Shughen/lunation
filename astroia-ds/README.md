# 🤖 Astroia DS - Data Science & Machine Learning

**Date :** 5 novembre 2025  
**Projet :** Analyse et prédiction parent-enfant avec XGBoost

---

## 📁 Structure

```
astroia-ds/
├── data/
│   ├── dataset.csv              # TON dataset (à remplacer)
│   └── dataset_example.csv      # Exemple de format
├── env/                          # Virtual environment Python
├── notebooks/
│   └── 01_parent_enfant_MVP.ipynb  # Notebook d'exploration
├── src/
│   ├── train.py                 # Training simple
│   └── train_optuna.py          # Optimisation hyperparamètres
├── outputs/
│   ├── models/                  # Modèles entraînés (.pkl)
│   ├── logs/                    # Logs d'entraînement
│   └── reports/                 # Graphiques et rapports
└── requirements.txt
```

---

## 🚀 Installation (une fois)

### 1. Créer l'environnement virtuel

```bash
cd /Users/remibeaurain/astroia/astroia-ds

# Créer le venv
python3 -m venv env

# Activer
source env/bin/activate

# Installer les dépendances
pip install -U pip
pip install -r requirements.txt
```

---

## 📊 Préparer ton dataset

### Format requis : `data/dataset.csv`

```csv
parent_age,child_age,age_gap,cohabitation_months,events_count,target
34,5,29,48,2,1
29,4,25,12,0,0
...
```

**Colonnes :**
- Features numériques (parent_age, child_age, etc.)
- **target** : 0 (négatif) ou 1 (positif)

**Remplace** `data/dataset.csv` par ton vrai dataset !

---

## 🎯 Lancer un entraînement

### Option 1 : Notebook (interactif)

```bash
# Activer le venv
source env/bin/activate

# Lancer Jupyter
jupyter notebook notebooks/01_parent_enfant_MVP.ipynb
```

Exécute les cellules une par une.

### Option 2 : Script simple

```bash
# Activer le venv
source env/bin/activate

# Training rapide (2000 rounds)
python src/train.py --data data/dataset.csv --target target --rounds 2000
```

**Résultats** :
- Modèle : `outputs/models/xgb_model.pkl`
- Métriques : `outputs/metrics.json`

### Option 3 : Optuna (optimisation)

```bash
# Recherche de meilleurs hyperparamètres
python src/train_optuna.py --data data/dataset.csv --target target --trials 200
```

**Résultats** :
- Modèle optimisé : `outputs/models/xgb_best.pkl`
- Meilleurs paramètres : `outputs/best_params.json`
- Graphique : `outputs/reports/optuna_history.png`

---

## 🌙 Lancer toute la nuit (sans fermer le Mac)

### A) Training intensif (8000 rounds)

```bash
cd /Users/remibeaurain/astroia/astroia-ds
source env/bin/activate

caffeinate -dimsu \
nohup python src/train.py --data data/dataset.csv --target target --rounds 8000 \
  > outputs/logs/train_$(date +%F_%H%M).log 2>&1 &
disown
```

### B) Optuna (400 trials - ~6-8h)

```bash
cd /Users/remibeaurain/astroia/astroia-ds
source env/bin/activate

caffeinate -dimsu \
nohup python src/train_optuna.py --data data/dataset.csv --target target --trials 400 \
  > outputs/logs/optuna_$(date +%F_%H%M).log 2>&1 &
disown
```

**Important :**
- ⚡ Branche ton Mac
- 💻 Ne ferme PAS le capot (ou configure "Ne pas se mettre en veille")
- ✅ Tu peux fermer Cursor, ça continue

### Vérifier la progression

```bash
# Voir les derniers logs
tail -f outputs/logs/*.log

# Ou
watch -n 10 'tail -n 20 outputs/logs/*.log'
```

---

## 📈 Demain matin - Résultats

### Fichiers à vérifier

```bash
cd /Users/remibeaurain/astroia/astroia-ds

# Modèle entraîné
ls -lh outputs/models/

# Métriques
cat outputs/metrics.json

# Ou meilleurs params (Optuna)
cat outputs/best_params.json

# Graphique d'optimisation
open outputs/reports/optuna_history.png
```

### Métriques importantes

- **ROC AUC** : Score entre 0.5 (aléatoire) et 1.0 (parfait)
  - > 0.7 : Bon
  - > 0.8 : Très bon
  - > 0.9 : Excellent
  
- **Precision/Recall** : Voir dans `metrics.json`

---

## 🔧 Utiliser le modèle entraîné

```python
import joblib
import pandas as pd

# Charger le modèle
model = joblib.load('outputs/models/xgb_model.pkl')

# Prédire
new_data = pd.DataFrame({
    'parent_age': [35],
    'child_age': [6],
    'age_gap': [29],
    'cohabitation_months': [50],
    'events_count': [3]
})

prediction = model.predict(new_data)
proba = model.predict_proba(new_data)

print(f"Prediction: {prediction[0]}")
print(f"Probability: {proba[0][1]:.2%}")
```

---

## 📚 Ressources

- **XGBoost** : https://xgboost.readthedocs.io/
- **Optuna** : https://optuna.readthedocs.io/
- **Scikit-learn** : https://scikit-learn.org/

---

**Setup complet ! Prêt pour le ML ! 🤖**

