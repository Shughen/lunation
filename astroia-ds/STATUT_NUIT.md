# 🌙 Training de nuit - Lancé le 5 novembre 2025

## ✅ STATUT : EN COURS

### 🤖 Processus lancés

1. **Training simple XGBoost**
   - Fichier : `src/train.py`
   - Paramètres : 8000 rounds
   - Dataset : 10,000 lignes (relation parent-enfant)
   - Log : `outputs/logs/train_*.log`
   - Durée estimée : **2-4 heures**

2. **Optimisation Optuna**
   - Fichier : `src/train_optuna.py`
   - Paramètres : 400 trials
   - Dataset : 10,000 lignes (relation parent-enfant)
   - Log : `outputs/logs/optuna_*.log`
   - Durée estimée : **6-8 heures**

### 💾 Stockage

- Dataset : `/Volumes/Stockage_perso/Astro-IA/data/dataset.csv` (10,000 lignes)
- Modèles : `/Volumes/Stockage_perso/Astro-IA/models/`
- Logs : `/Volumes/Stockage_perso/Astro-IA/logs/`

---

## 📊 DEMAIN MATIN - Comment récupérer les résultats

### 1. Vérifier que c'est terminé

```bash
ps aux | grep -E "train.py|train_optuna.py" | grep -v grep
```

Si **rien ne s'affiche** → Terminé ! ✅  
Si des **processus s'affichent** → Encore en cours...

### 2. Voir les résultats

```bash
cd /Users/remibeaurain/astroia/astroia-ds

# Métriques du training simple
cat outputs/metrics.json

# Métriques Optuna (meilleur modèle)
cat outputs/best_params.json

# Logs complets
cat outputs/logs/*.log

# Graphique d'optimisation
open outputs/reports/optuna_history.png
```

### 3. Fichiers générés

- `outputs/models/xgb_model.pkl` - Modèle simple (8000 rounds)
- `outputs/models/xgb_best.pkl` - Modèle optimisé Optuna
- `outputs/metrics.json` - Scores (accuracy, ROC-AUC, etc.)
- `outputs/best_params.json` - Meilleurs hyperparamètres trouvés
- `outputs/reports/optuna_history.png` - Courbe d'optimisation

---

## 🛑 Arrêter les trainings si besoin

```bash
# Arrêter le training simple
pkill -f train.py

# Arrêter Optuna
pkill -f train_optuna.py

# Tout arrêter
pkill -f "train.py|train_optuna.py"
```

---

## 📈 Surveiller en direct (optionnel)

```bash
# Voir les logs en temps réel
tail -f /Users/remibeaurain/astroia/astroia-ds/outputs/logs/*.log

# Ou toutes les 10 secondes
watch -n 10 'tail -n 30 /Users/remibeaurain/astroia/astroia-ds/outputs/logs/*.log'
```

---

## ⚡ Performances attendues

Pour un dataset de 10,000 lignes :

**Training simple (8000 rounds) :**
- Accuracy attendue : 70-85%
- ROC-AUC attendu : 0.75-0.90
- Temps : ~2-4h

**Optuna (400 trials) :**
- Accuracy attendue : 75-90% (meilleure que le simple)
- ROC-AUC attendu : 0.80-0.95
- Temps : ~6-8h
- Bonus : Graphique montrant l'évolution de la performance

---

## 🔋 Important

✅ Mac branché sur secteur  
✅ `caffeinate` actif (empêche la mise en veille)  
✅ Disque externe `/Volumes/Stockage_perso` branché  
✅ Processus en arrière-plan (survivent à la fermeture de Cursor)

**Tu peux :**
- Fermer Cursor ✅
- Fermer ton terminal ✅
- Utiliser ton Mac normalement ✅
- Aller dormir ! 😴

---

**Bonne nuit ! Le ML travaille pour toi ! 🤖✨**

