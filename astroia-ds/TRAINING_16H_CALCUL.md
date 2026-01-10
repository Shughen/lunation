# 🧮 CALCUL TRAINING 16H - XGBoost Parent-Enfant

## 📊 ANALYSE DU DERNIER RUN

### Exécution du 5 novembre 2025

**Commande lancée** :
```bash
python src/train_optuna.py --trials 1000
```

**Résultats mesurés** :
- ✅ **Trials exécutés** : 1000 (Trial 0 → Trial 999)
- ⏱️ **Temps total** : 10378.60 secondes = **2h 52min 58s**
- 🎯 **Meilleur ROC-AUC** : 0.9819 (Trial 772)
- ⚡ **Temps moyen/trial** : 10.38 secondes

**Meilleurs hyperparamètres trouvés** :
```json
{
  "n_estimators": 3760,
  "max_depth": 3,
  "learning_rate": 0.024,
  "subsample": 0.607,
  "colsample_bytree": 0.944,
  "min_child_weight": 16.40,
  "gamma": 0.59,
  "reg_lambda": 1.14,
  "reg_alpha": 6.06
}
```

---

## 🧮 CALCUL POUR 16H

### Produit en croix

**Données** :
- 1000 trials = 10378 secondes (2h53)
- Objectif = 57600 secondes (16h)

**Calcul** :
```
X trials = (57600 s × 1000 trials) / 10378 s
X = 5549 trials
```

### Options de lancement

| Trials | Durée estimée | Recommandation |
|--------|---------------|----------------|
| **5500** | ~15h 45min | ✅ Recommandé (marge de sécurité) |
| **5550** | ~16h 00min | ✅ Objectif exact |
| **5600** | ~16h 05min | ✅ Légèrement au-dessus |

---

## 🚀 LANCER UN TRAINING 16H

### Option 1 : Script automatique (RECOMMANDÉ)

```bash
cd /Users/remibeaurain/astroia/astroia-ds
./train_16h.sh
```

Ce script :
- ✅ Lance 5550 trials (~16h)
- ✅ Active automatiquement l'environnement virtuel
- ✅ Crée un log horodaté
- ✅ Affiche la progression
- ✅ Sauvegarde le modèle final dans `outputs/models/`

### Option 2 : Commande manuelle

```bash
cd /Users/remibeaurain/astroia/astroia-ds
source env/bin/activate
python src/train_optuna.py --trials 5550 --seed 42
```

---

## 📈 PROGRESSION ATTENDUE

**Estimation basée sur le dernier run** :

| Temps écoulé | Trials complétés | % Progression |
|--------------|------------------|---------------|
| 2h | ~690 | 12.4% |
| 4h | ~1385 | 24.9% |
| 6h | ~2080 | 37.5% |
| 8h | ~2770 | 49.9% |
| 10h | ~3465 | 62.4% |
| 12h | ~4155 | 74.9% |
| 14h | ~4850 | 87.4% |
| 16h | ~5550 | 100% ✅ |

**Note** : Chaque trial prend ~10.4 secondes en moyenne.

---

## 📉 POURQUOI LE DERNIER RUN ÉTAIT PLUS COURT ?

### Explication

1. **Paramètre `--trials` par défaut** : 200 (dans le code)
2. **Lancé avec** : `--trials 1000` explicitement
3. **Résultat** : 1000 trials en 2h53 au lieu de 16h

### Ce qui s'est passé

Le script `train_optuna.py` a ce paramètre par défaut :
```python
p.add_argument("--trials", type=int, default=200)
```

Pour avoir 16h, il faut passer `--trials 5550` !

---

## 🎯 OBJECTIFS DU PROCHAIN RUN

1. **Durée** : ~16h de training continu
2. **Trials** : 5550 essais Optuna
3. **ROC-AUC cible** : > 0.9820 (améliorer 0.9819)
4. **Output** :
   - Modèle final : `outputs/models/xgb_best.pkl`
   - Historique : `outputs/reports/optuna_history.png`
   - Logs : `outputs/logs/training_16h_YYYYMMDD_HHMMSS.log`

---

## 🔍 SURVEILLANCE DU TRAINING

### Vérifier la progression en temps réel

```bash
# Voir les dernières lignes du log
tail -f /Users/remibeaurain/astroia/astroia-ds/outputs/logs/training_16h_*.log

# Compter les trials complétés
grep "Trial.*finished" /Users/remibeaurain/astroia/astroia-ds/outputs/logs/training_16h_*.log | wc -l

# Voir le meilleur score actuel
grep "Best is trial" /Users/remibeaurain/astroia/astroia-ds/outputs/logs/training_16h_*.log | tail -1
```

---

## 📝 CHECKLIST AVANT DE LANCER

- [ ] L'ordinateur est branché (pas sur batterie)
- [ ] Espace disque suffisant (>1GB libre)
- [ ] Pas d'autres tâches lourdes en cours
- [ ] Environnement virtuel activé
- [ ] Dataset présent : `data_external/dataset.csv`
- [ ] Dossiers créés : `outputs/models`, `outputs/logs`, `outputs/reports`

---

## 🚨 TROUBLESHOOTING

### Si le training s'arrête prématurément

1. **Vérifier les logs** :
   ```bash
   tail -50 outputs/logs/training_16h_*.log
   ```

2. **Vérifier l'espace disque** :
   ```bash
   df -h
   ```

3. **Relancer avec moins de trials** :
   ```bash
   ./train_16h.sh  # Modifie --trials 5550 → 4000 si nécessaire
   ```

### Si les résultats sont moins bons

- **Cause probable** : Overfitting sur le validation set
- **Solution** : Utiliser les paramètres du Trial 772 (ROC-AUC 0.9819)
- **Fichier** : `outputs/best_params.json`

---

## 📅 HISTORIQUE DES RUNS

| Date | Trials | Durée | ROC-AUC | Notes |
|------|--------|-------|---------|-------|
| 2025-11-05 | 1000 | 2h53 | 0.9819 | Premier run avec dataset étendu ✅ |
| (à venir) | 5550 | ~16h | ? | Run 16h pour optimisation poussée |

---

**Créé le** : 2025-11-06  
**Dernière mise à jour** : 2025-11-06


