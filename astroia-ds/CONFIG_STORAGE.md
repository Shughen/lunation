# 💾 Configuration Stockage Externe

**Date :** 5 novembre 2025  
**Disque externe :** `/Volumes/Stockage_perso/Astro-IA`

---

## 🎯 Architecture

### Stockage réparti

```
astroia-ds/                          (SSD interne - code léger)
├── src/                            ← Scripts Python (Ko)
├── notebooks/                      ← Notebooks (Ko)
├── data_external/                  → Lien vers disque externe
├── outputs/
│   ├── models/                    → Lien vers disque externe
│   ├── logs/                      → Lien vers disque externe
│   └── reports/                   ← Graphiques (Mo, en local)

/Volumes/Stockage_perso/Astro-IA/   (Disque externe - gros fichiers)
├── data/                           ← Datasets (Go)
├── models/                         ← Modèles .pkl (Go)
└── logs/                           ← Logs training (Mo)
```

---

## 🔗 Liens symboliques créés

| Lien local | Pointe vers | Type de fichiers |
|------------|-------------|------------------|
| `data_external/` | `/Volumes/Stockage_perso/Astro-IA/data/` | Datasets CSV (Go) |
| `outputs/models/` | `/Volumes/Stockage_perso/Astro-IA/models/` | Modèles .pkl (Go) |
| `outputs/logs/` | `/Volumes/Stockage_perso/Astro-IA/logs/` | Logs training (Mo) |

---

## 📝 Utilisation

### Ajouter un dataset

```bash
# Copier ton gros dataset sur le disque externe
cp ~/Downloads/huge_dataset.csv /Volumes/Stockage_perso/Astro-IA/data/dataset.csv

# OU créer un lien depuis astroia-ds
ln -s /Volumes/Stockage_perso/Astro-IA/data/dataset.csv data/dataset.csv
```

### Chemins dans les scripts

Les scripts sont **déjà configurés** pour utiliser les liens symboliques :

```python
# Dans train.py
--data ../data/dataset.csv       # Fonctionne !
--data ../data_external/xxx.csv  # Aussi !
```

---

## ⚠️ Si le disque n'est pas monté

### Vérifier que le disque est branché

```bash
ls /Volumes/Stockage_perso/Astro-IA
```

**Si erreur "No such file"** → Branche ton disque externe !

### Reconnecter les liens (si nécessaire)

```bash
cd /Users/remibeaurain/astroia/astroia-ds

# Recréer les liens symboliques
ln -sf /Volumes/Stockage_perso/Astro-IA/data data_external
ln -sf /Volumes/Stockage_perso/Astro-IA/models outputs/models
ln -sf /Volumes/Stockage_perso/Astro-IA/logs outputs/logs
```

---

## 📦 Avantages

✅ **SSD interne** : Code léger uniquement (~10 Mo)  
✅ **Disque externe** : Datasets et modèles lourds (Go)  
✅ **Transparent** : Les scripts fonctionnent normalement  
✅ **Flexible** : Change de disque facilement  
✅ **Sauvegarde** : Modèles sur disque externe = sécurisés  

---

## 🔄 Migration de fichiers existants

Si tu as déjà des fichiers dans `astroia-ds/` :

```bash
# Déplacer vers le disque externe
mv data/*.csv /Volumes/Stockage_perso/Astro-IA/data/
mv outputs/models/*.pkl /Volumes/Stockage_perso/Astro-IA/models/
mv outputs/logs/*.log /Volumes/Stockage_perso/Astro-IA/logs/
```

---

## 🧪 Test de fonctionnement

```bash
cd /Users/remibeaurain/astroia/astroia-ds

# Vérifier les liens
ls -l data_external
ls -l outputs/models
ls -l outputs/logs

# Tester l'écriture
touch /Volumes/Stockage_perso/Astro-IA/data/test.txt
ls data_external/test.txt  # Doit apparaître !
rm /Volumes/Stockage_perso/Astro-IA/data/test.txt
```

---

**Stockage externe configuré ! 💾✨**

