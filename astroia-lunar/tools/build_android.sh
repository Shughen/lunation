#!/usr/bin/env bash
set -euo pipefail

# Toujours se placer à la racine du repo
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p logs
LOG="logs/build_android_$(date +%Y%m%d-%H%M%S).log"

echo "[build_android] $(date -Iseconds)" | tee "$LOG"
echo "[pwd] $(pwd)" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"

# Build & run android (dev build)
cd apps/mobile
echo "[cmd] npm run android" | tee -a "../../$LOG"
npm run android 2>&1 | tee -a "../../$LOG"

echo "----------------------------------------" | tee -a "../../$LOG"
echo "[ok] build done" | tee -a "../../$LOG"
echo "[log] $LOG" | tee -a "../../$LOG"
