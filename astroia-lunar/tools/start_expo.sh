#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p logs
LOG="logs/expo_start_$(date +%Y%m%d-%H%M%S).log"

echo "[start_expo] $(date -Iseconds)" | tee "$LOG"
echo "[pwd] $(pwd)" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"

cd apps/mobile

# Start Expo dev server
echo "[cmd] npm start" | tee -a "../../$LOG"
npm start 2>&1 | tee -a "../../$LOG"

echo "----------------------------------------" | tee -a "../../$LOG"
echo "[log] $LOG" | tee -a "../../$LOG"
