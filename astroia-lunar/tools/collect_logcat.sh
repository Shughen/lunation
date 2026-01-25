#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p logs
LOG="logs/logcat_$(date +%Y%m%d-%H%M%S).log"

echo "[collect_logcat] $(date -Iseconds)" | tee "$LOG"
echo "[pwd] $(pwd)" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"

# Vérifie device/emulator
echo "[cmd] adb devices" | tee -a "$LOG"
adb devices 2>&1 | tee -a "$LOG"

# Logcat : dernier chunk (5 minutes)
echo "[cmd] adb logcat -d -T 5m" | tee -a "$LOG"
adb logcat -d -T 5m 2>&1 | tee -a "$LOG"

echo "----------------------------------------" | tee -a "$LOG"
echo "[ok] logcat captured" | tee -a "$LOG"
echo "[log] $LOG" | tee -a "$LOG"
