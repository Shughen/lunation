#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p logs
LOG="logs/tests_api_$(date +%Y%m%d-%H%M%S).log"

echo "[run_tests_api] $(date -Iseconds)" | tee "$LOG"
echo "[pwd] $(pwd)" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"

cd apps/api

# Tests pytest
echo "[cmd] pytest -q" | tee -a "../../$LOG"
pytest -q 2>&1 | tee -a "../../$LOG"

echo "----------------------------------------" | tee -a "../../$LOG"
echo "[ok] tests done" | tee -a "../../$LOG"
echo "[log] $LOG" | tee -a "../../$LOG"
