# 🤖 ENTRAÎNEMENT ML EN COURS

**Date de lancement:** 5 novembre 2025  
**Statut:** 🟢 **EN COURS**

---

## 📊 CONFIGURATION

**Dataset:** `data_external/dataset_big.csv`  
**Taille:** 500,000 lignes  
**Algorithm:** XGBoost + Optuna  
**Trials:** 1,000 optimisations  
**Durée estimée:** **~22 heures**

**PID:** 5929

---

## 📁 FICHIERS

**Logs:**
```
outputs/logs/training_night_20251105_*.log
```

**Modèle final:**
```
outputs/models/xgb_best.pkl
```

**Métriques:**
```
outputs/best_params.json
```

**Graphiques:**
```
outputs/reports/optuna_history.png
```

---

## 🔍 SUIVRE LA PROGRESSION

### Voir les logs en direct
```bash
cd /Users/remibeaurain/astroia/astroia-ds
tail -f outputs/logs/training_night_*.log
```

### Vérifier que ça tourne
```bash
ps aux | grep train_optuna | grep -v grep
```

### Voir le PID
```bash
cat outputs/logs/training.pid
```

---

## ⏸️ ARRÊTER L'ENTRAÎNEMENT

```bash
kill 5929
# OU
kill $(cat outputs/logs/training.pid)
```

---

## 📈 PROGRESSION ATTENDUE

| Heure | Trials | Progression | Best ROC-AUC estimé |
|-------|--------|-------------|---------------------|
| +2h | ~90 | 9% | 0.72 |
| +6h | ~270 | 27% | 0.76 |
| +12h | ~545 | 54% | 0.79 |
| +18h | ~818 | 82% | 0.82 |
| +22h | 1000 | 100% | **0.85+** ✅ |

---

## ✅ RÉSULTATS FINAUX

**Le modèle sera disponible dans :**
```
outputs/models/xgb_best.pkl
```

**À copier vers l'API :**
```bash
cp outputs/models/xgb_best.pkl ../astro-ia-api/api/ml/xgb_best.pkl
```

**Puis redéployer :**
```bash
cd ../astro-ia-api
# Redéployer sur Vercel
```

---

## 🎯 APRÈS L'ENTRAÎNEMENT

1. **Copier le modèle** vers l'API
2. **Vérifier les métriques** (ROC-AUC > 0.80)
3. **Tester** l'analyse Parent-Enfant dans l'app
4. **Comparer** les résultats avec l'ancien modèle

---

## 🔧 PARAMÈTRES D'OPTIMISATION

**Hyperparamètres optimisés :**
- `n_estimators`: 400-4000 (nombre d'arbres)
- `max_depth`: 3-10 (profondeur)
- `learning_rate`: 0.001-0.2 (taux d'apprentissage)
- `subsample`: 0.6-1.0 (échantillonnage)
- `colsample_bytree`: 0.6-1.0 (features)
- `min_child_weight`: 1-20 (régularisation)
- `gamma`: 0-5 (splitting)
- `reg_lambda`: 0.001-10 (L2)
- `reg_alpha`: 0.001-10 (L1)

**Stratégie:**
- Optuna TPE (Tree-structured Parzen Estimator)
- Maximisation ROC-AUC
- 1000 trials pour exploration exhaustive

---

## 💻 UTILISATION DU MAC

**Pendant l'entraînement:**
- ✅ Navigation web OK
- ✅ Bureautique OK
- ⚠️ Pas de jeux/vidéo lourds (CPU utilisé à ~80%)
- ⚠️ Le Mac peut chauffer
- ⚠️ Batterie se décharge plus vite

**Recommandation:**
- Laisser le Mac branché
- Ne pas le mettre en veille
- Vérifier toutes les 4-6h que ça tourne

---

## 📞 EN CAS DE PROBLÈME

### Le processus s'est arrêté

```bash
# Vérifier le dernier log
tail -50 outputs/logs/training_night_*.log

# Relancer si nécessaire
source env/bin/activate
python src/train_optuna.py --data data_external/dataset_big.csv --trials 1000
```

### Mémoire insuffisante

```bash
# Réduire le nombre de trials
python src/train_optuna.py --data data_external/dataset_big.csv --trials 500
```

### Mac en surchauffe

```bash
# Arrêter temporairement
kill $(cat outputs/logs/training.pid)

# Relancer plus tard avec moins de CPU
python src/train_optuna.py --data data_external/dataset_big.csv --trials 500
```

---

**✅ Entraînement lancé ! Rendez-vous dans 22h ! 🚀**

**Tu peux vérifier la progression : `tail -f outputs/logs/training_night_*.log`**

