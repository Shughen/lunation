#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p logs
LOG="logs/tests_mobile_$(date +%Y%m%d-%H%M%S).log"

echo "[run_tests_mobile] $(date -Iseconds)" | tee "$LOG"
echo "[pwd] $(pwd)" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"

cd apps/mobile

# Typecheck
echo "[cmd] npm run typecheck" | tee -a "../../$LOG"
npm run typecheck 2>&1 | tee -a "../../$LOG"

# Tests
echo "[cmd] npm test" | tee -a "../../$LOG"
npm test 2>&1 | tee -a "../../$LOG"

echo "----------------------------------------" | tee -a "../../$LOG"
echo "[ok] tests done" | tee -a "../../$LOG"
echo "[log] $LOG" | tee -a "../../$LOG"
