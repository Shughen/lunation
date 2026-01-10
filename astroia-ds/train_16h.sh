#!/bin/bash
# Script pour lancer un training de 16h (~5550 trials)
# Basé sur le calcul : 10.38s/trial × 5550 = 57609s = 16h00min

set -e

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   🚀 TRAINING ML - 16H (~5550 trials)  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

cd "$(dirname "$0")"

# Vérifier l'environnement
if [ ! -d "env" ]; then
    echo -e "${YELLOW}⚠️  Environnement virtuel non trouvé${NC}"
    exit 1
fi

# Activer l'environnement
source env/bin/activate

# Timestamp pour les logs
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="outputs/logs/training_16h_${TIMESTAMP}.log"
PID_FILE="outputs/logs/training.pid"

echo -e "${GREEN}📊 Paramètres :${NC}"
echo "   - Trials : 5550"
echo "   - Durée estimée : ~16h"
echo "   - Dataset : data_external/dataset.csv"
echo "   - Log : ${LOG_FILE}"
echo ""

# Créer les dossiers
mkdir -p outputs/logs outputs/models outputs/reports

# Sauvegarder le PID
echo $$ > "$PID_FILE"

# Lancer le training
echo -e "${BLUE}🔥 Démarrage du training...${NC}"
echo "   Start: $(date)"
echo ""

python src/train_optuna.py \
    --data data_external/dataset.csv \
    --trials 5550 \
    --seed 42 \
    --outdir outputs \
    2>&1 | tee "$LOG_FILE"

echo ""
echo -e "${GREEN}✅ Training terminé !${NC}"
echo "   End: $(date)"
echo "   Log: ${LOG_FILE}"

# Nettoyer le PID
rm -f "$PID_FILE"


