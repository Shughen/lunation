#!/bin/bash
# ============================================
# 🌙 Astroia Lunar API - Docker Entrypoint
# ============================================
# Script de démarrage pour container Docker
# Exécute migrations Alembic puis démarre uvicorn
#
# Usage:
#   chmod +x docker-entrypoint.sh
#   Dans Dockerfile: CMD ["./docker-entrypoint.sh"]
# ============================================

set -e

echo "🚀 Astroia Lunar API - Starting..."

# ============================================
# 1. Attendre la base de données (optionnel)
# ============================================
# Utile si DB et API démarrent ensemble (docker-compose)
if [ -n "$DATABASE_URL" ]; then
    echo "⏳ Waiting for database to be ready..."

    # Extraire host et port depuis DATABASE_URL
    # Format: postgresql://user:pass@host:port/db
    DB_HOST=$(echo "$DATABASE_URL" | sed -n 's/.*@\(.*\):.*/\1/p')
    DB_PORT=$(echo "$DATABASE_URL" | sed -n 's/.*:\([0-9]*\)\/.*/\1/p')

    if [ -n "$DB_HOST" ] && [ -n "$DB_PORT" ]; then
        # Attendre que le port DB soit ouvert (max 30s)
        timeout 30 bash -c "until nc -z $DB_HOST $DB_PORT; do sleep 1; done" || {
            echo "⚠️  Warning: Database not reachable at $DB_HOST:$DB_PORT"
            echo "   Continuing anyway..."
        }
        echo "✅ Database connection available"
    fi
fi

# ============================================
# 2. Exécuter migrations Alembic
# ============================================
echo "🔄 Running Alembic migrations..."

# Option 1: Upgrade automatique (recommandé pour dev/staging)
alembic upgrade head || {
    echo "❌ Migration failed! Stopping container."
    exit 1
}

echo "✅ Migrations completed successfully"

# Option 2: Stamp seulement (si migrations déjà appliquées manuellement)
# alembic stamp head

# ============================================
# 3. Démarrer uvicorn
# ============================================
echo "🌙 Starting Uvicorn server..."

# Production: pas de --reload
if [ "$APP_ENV" = "production" ]; then
    echo "📦 Environment: PRODUCTION"
    exec uvicorn main:app \
        --host "${API_HOST:-0.0.0.0}" \
        --port "${API_PORT:-8000}" \
        --workers "${WORKERS:-1}"
else
    echo "🔧 Environment: ${APP_ENV:-development}"
    exec uvicorn main:app \
        --host "${API_HOST:-0.0.0.0}" \
        --port "${API_PORT:-8000}"
fi
