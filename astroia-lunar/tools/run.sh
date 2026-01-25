#!/usr/bin/env bash
set -euo pipefail

#
# Wrapper sécurisé pour exécuter les scripts tools/
#
# Usage: tools/run.sh <script-name>
# Exemple: tools/run.sh build_android
#

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Scripts autorisés (allowlist)
ALLOWED_SCRIPTS=(
  "build_android"
  "run_tests_mobile"
  "run_tests_api"
  "collect_logcat"
  "start_expo"
  "run_ab_test_opus"
  "run_ab_test_sonnet"
  "run_ab_test_analyze"
)

# Vérifier qu'un argument est fourni
if [ $# -eq 0 ]; then
  echo "❌ Usage: tools/run.sh <script-name>"
  echo ""
  echo "Scripts autorisés:"
  for script in "${ALLOWED_SCRIPTS[@]}"; do
    echo "  - $script"
  done
  exit 1
fi

SCRIPT_NAME="$1"

# Vérifier que le script est autorisé
ALLOWED=false
for allowed in "${ALLOWED_SCRIPTS[@]}"; do
  if [ "$allowed" = "$SCRIPT_NAME" ]; then
    ALLOWED=true
    break
  fi
done

if [ "$ALLOWED" = false ]; then
  echo "❌ Script non autorisé: $SCRIPT_NAME"
  echo ""
  echo "Scripts autorisés:"
  for script in "${ALLOWED_SCRIPTS[@]}"; do
    echo "  - $script"
  done
  exit 1
fi

# Exécuter le script
SCRIPT_PATH="tools/${SCRIPT_NAME}.sh"

if [ ! -f "$SCRIPT_PATH" ]; then
  echo "❌ Script introuvable: $SCRIPT_PATH"
  exit 1
fi

if [ ! -x "$SCRIPT_PATH" ]; then
  echo "❌ Script non exécutable: $SCRIPT_PATH"
  echo "Exécutez: chmod +x $SCRIPT_PATH"
  exit 1
fi

echo "✅ Exécution de: $SCRIPT_PATH"
echo "----------------------------------------"
exec "$SCRIPT_PATH"
