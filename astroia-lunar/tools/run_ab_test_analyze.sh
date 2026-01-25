#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p logs
LOG="logs/ab_test_analyze_$(date +%Y%m%d-%H%M%S).log"

echo "[ab_test_analyze] $(date -Iseconds)" | tee "$LOG"
echo "[pwd] $(pwd)" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"

cd apps/api

echo "[cmd] python scripts/ab_test_analyze.py --cost" | tee -a "../../$LOG"
python scripts/ab_test_analyze.py --cost 2>&1 | tee -a "../../$LOG"

echo "----------------------------------------" | tee -a "../../$LOG"
echo "[ok] Analyse terminée" | tee -a "../../$LOG"
echo "[log] $LOG" | tee -a "../../$LOG"
