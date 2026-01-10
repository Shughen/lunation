#!/bin/bash
# ============================================
# COMMANDES POUR LANCER LES TRAININGS DE NUIT
# ============================================
# Exécuter depuis /Users/remibeaurain/astroia/astroia-ds

echo "🤖 Astroia DS - Training de nuit"
echo "================================="
echo ""

# Vérifier que le disque externe est monté
if [ ! -d "/Volumes/Stockage_perso/Astro-IA" ]; then
    echo "❌ ERREUR : Disque externe non monté !"
    echo "   Branche /Volumes/Stockage_perso"
    exit 1
fi

# Vérifier que le venv existe
if [ ! -d "env" ]; then
    echo "❌ ERREUR : Virtual env non créé !"
    echo "   Exécute: python3 -m venv env"
    exit 1
fi

# Activer le venv
source env/bin/activate

echo "✅ Disque externe : OK"
echo "✅ Virtual env : OK"
echo ""

# Menu
echo "Choisis une option :"
echo "1) Training simple (8000 rounds, ~2-4h)"
echo "2) Optuna (400 trials, ~6-8h)"
echo "3) Les deux en parallèle"
echo ""
read -p "Ton choix (1/2/3) : " choice

case $choice in
    1)
        echo "🚀 Lancement Training simple..."
        caffeinate -dimsu nohup python src/train.py \
          --data data_external/dataset.csv \
          --target target \
          --rounds 8000 \
          > outputs/logs/train_$(date +%F_%H%M).log 2>&1 &
        echo "✅ Training lancé ! PID: $!"
        ;;
    2)
        echo "🚀 Lancement Optuna..."
        caffeinate -dimsu nohup python src/train_optuna.py \
          --data data_external/dataset.csv \
          --target target \
          --trials 400 \
          > outputs/logs/optuna_$(date +%F_%H%M).log 2>&1 &
        echo "✅ Optuna lancé ! PID: $!"
        ;;
    3)
        echo "🚀 Lancement des DEUX en parallèle..."
        
        caffeinate -dimsu nohup python src/train.py \
          --data data_external/dataset.csv \
          --target target \
          --rounds 8000 \
          > outputs/logs/train_$(date +%F_%H%M).log 2>&1 &
        PID1=$!
        
        caffeinate -dimsu nohup python src/train_optuna.py \
          --data data_external/dataset.csv \
          --target target \
          --trials 400 \
          > outputs/logs/optuna_$(date +%F_%H%M).log 2>&1 &
        PID2=$!
        
        echo "✅ Training lancé ! PID: $PID1"
        echo "✅ Optuna lancé ! PID: $PID2"
        ;;
    *)
        echo "❌ Choix invalide"
        exit 1
        ;;
esac

disown

echo ""
echo "📊 Surveiller les logs :"
echo "   tail -f outputs/logs/*.log"
echo ""
echo "🛑 Arrêter si besoin :"
echo "   pkill -f train.py"
echo "   pkill -f train_optuna.py"
echo ""
echo "😴 Tu peux fermer ce terminal et aller dormir !"
echo "   Les trainings continuent en arrière-plan."

