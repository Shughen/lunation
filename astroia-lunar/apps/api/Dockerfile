# ============================================
# 🌙 Astroia Lunar API - Dockerfile
# ============================================
# FastAPI backend pour calculs astrologiques et révolutions lunaires
#
# Build:
#   cd apps/api
#   docker build -t astroia-api .
#
# Run (développement):
#   docker run -p 8000:8000 --env-file .env astroia-api
#
# Run (avec variables d'environnement):
#   docker run -p 8000:8000 \
#     -e DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/db \
#     -e ANTHROPIC_API_KEY=your-key \
#     -e RAPIDAPI_KEY=your-key \
#     astroia-api
#
# Healthcheck:
#   curl http://localhost:8000/health
# ============================================

# ============================================
# Stage 1: Builder (pour optimisation future)
# ============================================
FROM python:3.10-slim as builder

# Variables d'environnement pour build Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# Installer dependencies système pour build (psycopg2, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copier et installer requirements
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# ============================================
# Stage 2: Runtime
# ============================================
FROM python:3.10-slim

# Metadata
LABEL maintainer="Astroia Team"
LABEL description="Lunation API - FastAPI backend pour calculs astrologiques"
LABEL version="1.0.0"

# Variables d'environnement
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/home/appuser/.local/bin:$PATH"

WORKDIR /app

# Installer uniquement les runtime dependencies (libpq pour psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Créer user non-root pour sécurité
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Copier les dépendances Python depuis builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Copier le code source
COPY --chown=appuser:appuser . .

# Changer vers user non-root
USER appuser

# Exposer port API
EXPOSE 8000

# Healthcheck (vérifie endpoint /health toutes les 30s)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# ============================================
# Commande de démarrage
# ============================================
# Note: Les migrations Alembic doivent être exécutées AVANT le démarrage
# Option 1 (recommandé): Exécuter migrations manuellement:
#   docker exec <container> alembic upgrade head
#
# Option 2: Utiliser un script entrypoint (non fourni ici)
#
# Par défaut, on démarre directement uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Pour auto-reload en dev (NON recommandé en production):
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
