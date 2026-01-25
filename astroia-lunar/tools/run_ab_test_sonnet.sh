#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p logs
LOG="logs/ab_test_sonnet_$(date +%Y%m%d-%H%M%S).log"

echo "[ab_test_sonnet] $(date -Iseconds)" | tee "$LOG"
echo "[pwd] $(pwd)" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"
echo "🧪 A/B Test - Génération SONNET (24 interprétations)" | tee -a "$LOG"
echo "💰 Coût estimé: ~\$0.29 (avec Prompt Caching)" | tee -a "$LOG"
echo "⏱️  Durée estimée: ~2-3 minutes" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"

cd apps/api

echo "[cmd] python scripts/ab_test_sonnet_direct.py" | tee -a "../../$LOG"
python scripts/ab_test_sonnet_direct.py 2>&1 | tee -a "../../$LOG"

echo "----------------------------------------" | tee -a "../../$LOG"
echo "[ok] Génération Sonnet terminée" | tee -a "../../$LOG"
echo "[log] $LOG" | tee -a "../../$LOG"
