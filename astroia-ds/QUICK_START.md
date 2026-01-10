# ⚡ Quick Start - Astroia DS

Guide ultra-rapide pour lancer ton premier training !

---

## 🚀 Setup initial (5 min)

```bash
# 1. Aller dans le dossier
cd /Users/remibeaurain/astroia/astroia-ds

# 2. Créer l'environnement virtuel
python3 -m venv env

# 3. Activer
source env/bin/activate

# 4. Installer
pip install -U pip
pip install -r requirements.txt
```

---

## 📊 Préparer tes données

### Remplace le dataset d'exemple

```bash
# Copie ton CSV dans data/
cp ~/chemin/vers/ton_dataset.csv data/dataset.csv
```

### Format requis

Ton CSV doit avoir :
- Une colonne `target` (0 ou 1)
- Des features numériques

Exemple :
```csv
feature1,feature2,feature3,target
10,20,30,1
15,25,35,0
```

---

## 🎯 Training rapide (test - 2 min)

```bash
source env/bin/activate
python src/train.py --data data/dataset.csv --target target --rounds 100
```

Résultat : `outputs/models/xgb_model.pkl`

---

## 🌙 Training de nuit (6-8h)

### Option A : Simple (8000 rounds)

```bash
cd /Users/remibeaurain/astroia/astroia-ds
source env/bin/activate

caffeinate -dimsu nohup python src/train.py \
  --data data/dataset.csv \
  --target target \
  --rounds 8000 \
  > outputs/logs/train_$(date +%F_%H%M).log 2>&1 &

disown
```

### Option B : Optuna (meilleur modèle)

```bash
cd /Users/remibeaurain/astroia/astroia-ds
source env/bin/activate

caffeinate -dimsu nohup python src/train_optuna.py \
  --data data/dataset.csv \
  --target target \
  --trials 400 \
  > outputs/logs/optuna_$(date +%F_%H%M).log 2>&1 &

disown
```

---

## 📈 Vérifier la progression

```bash
# Voir les logs en temps réel
tail -f outputs/logs/*.log

# Ou toutes les 10 secondes
watch -n 10 'tail -n 20 outputs/logs/*.log'
```

---

## 🎉 Demain matin

```bash
# Voir les résultats
cat outputs/metrics.json

# Ou meilleurs params
cat outputs/best_params.json

# Graphique Optuna
open outputs/reports/optuna_history.png
```

---

**C'est tout ! Le reste est dans README.md** 📚

