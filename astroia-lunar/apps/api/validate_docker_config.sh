#!/bin/bash
# ============================================
# 🔍 Validation Docker Configuration
# ============================================
# Vérifie que tous les fichiers Docker sont présents et valides
# Usage: ./validate_docker_config.sh

set -e

echo "🔍 Validation Docker Configuration - Astroia Lunar API"
echo "========================================================"
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0
WARNINGS=0

# ============================================
# 1. Vérifier fichiers Docker
# ============================================
echo "📦 1. Vérification fichiers Docker..."

FILES=(
    "Dockerfile"
    ".dockerignore"
    "docker-entrypoint.sh"
    "docker-compose.example.yml"
    ".env.docker.example"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✅ $file${NC}"
    else
        echo -e "${RED}❌ $file MANQUANT${NC}"
        ERRORS=$((ERRORS + 1))
    fi
done

# Vérifier permissions entrypoint
if [ -f "docker-entrypoint.sh" ]; then
    if [ -x "docker-entrypoint.sh" ]; then
        echo -e "${GREEN}✅ docker-entrypoint.sh est exécutable${NC}"
    else
        echo -e "${YELLOW}⚠️  docker-entrypoint.sh n'est pas exécutable${NC}"
        echo "   Fix: chmod +x docker-entrypoint.sh"
        WARNINGS=$((WARNINGS + 1))
    fi
fi

echo ""

# ============================================
# 2. Vérifier syntaxe Dockerfile
# ============================================
echo "🐋 2. Vérification syntaxe Dockerfile..."

if [ -f "Dockerfile" ]; then
    # Vérifier instructions clés
    if grep -q "^FROM python:3.10-slim" Dockerfile; then
        echo -e "${GREEN}✅ Base image Python 3.10-slim${NC}"
    else
        echo -e "${RED}❌ Base image incorrecte${NC}"
        ERRORS=$((ERRORS + 1))
    fi

    if grep -q "^WORKDIR /app" Dockerfile; then
        echo -e "${GREEN}✅ WORKDIR /app${NC}"
    else
        echo -e "${RED}❌ WORKDIR manquant ou incorrect${NC}"
        ERRORS=$((ERRORS + 1))
    fi

    if grep -q "^EXPOSE 8000" Dockerfile; then
        echo -e "${GREEN}✅ EXPOSE 8000${NC}"
    else
        echo -e "${RED}❌ EXPOSE 8000 manquant${NC}"
        ERRORS=$((ERRORS + 1))
    fi

    if grep -q "^USER appuser" Dockerfile; then
        echo -e "${GREEN}✅ USER non-root (appuser)${NC}"
    else
        echo -e "${YELLOW}⚠️  USER non-root non trouvé${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi

    if grep -q "^HEALTHCHECK" Dockerfile; then
        echo -e "${GREEN}✅ HEALTHCHECK configuré${NC}"
    else
        echo -e "${YELLOW}⚠️  HEALTHCHECK non trouvé${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi

    # Vérifier multi-stage
    if grep -q "^FROM.*as builder" Dockerfile; then
        echo -e "${GREEN}✅ Multi-stage build${NC}"
    else
        echo -e "${YELLOW}⚠️  Multi-stage build non détecté${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
fi

echo ""

# ============================================
# 3. Vérifier .dockerignore
# ============================================
echo "🚫 3. Vérification .dockerignore..."

if [ -f ".dockerignore" ]; then
    REQUIRED_PATTERNS=(
        ".env"
        "*.key"
        "__pycache__"
        ".pytest_cache"
        ".venv"
    )

    for pattern in "${REQUIRED_PATTERNS[@]}"; do
        if grep -q "^$pattern" .dockerignore; then
            echo -e "${GREEN}✅ Exclut: $pattern${NC}"
        else
            echo -e "${YELLOW}⚠️  Pattern non trouvé: $pattern${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
    done
fi

echo ""

# ============================================
# 4. Vérifier requirements.txt
# ============================================
echo "📦 4. Vérification requirements.txt..."

if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}✅ requirements.txt présent${NC}"

    # Vérifier dépendances critiques
    DEPS=("fastapi" "uvicorn" "sqlalchemy" "psycopg2-binary" "alembic")
    for dep in "${DEPS[@]}"; do
        if grep -qi "^$dep" requirements.txt; then
            echo -e "${GREEN}  ✅ $dep${NC}"
        else
            echo -e "${RED}  ❌ $dep MANQUANT${NC}"
            ERRORS=$((ERRORS + 1))
        fi
    done
else
    echo -e "${RED}❌ requirements.txt MANQUANT${NC}"
    ERRORS=$((ERRORS + 1))
fi

echo ""

# ============================================
# 5. Vérifier variables ENV
# ============================================
echo "🔐 5. Vérification .env.docker.example..."

if [ -f ".env.docker.example" ]; then
    ENV_VARS=(
        "DATABASE_URL"
        "SECRET_KEY"
        "RAPIDAPI_KEY"
        "ANTHROPIC_API_KEY"
        "APP_ENV"
    )

    for var in "${ENV_VARS[@]}"; do
        if grep -q "^$var=" .env.docker.example; then
            echo -e "${GREEN}✅ $var${NC}"
        else
            echo -e "${YELLOW}⚠️  $var non trouvé${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
    done
fi

echo ""

# ============================================
# 6. Vérifier docker-compose
# ============================================
echo "🐳 6. Vérification docker-compose.example.yml..."

if [ -f "docker-compose.example.yml" ]; then
    echo -e "${GREEN}✅ docker-compose.example.yml présent${NC}"

    if grep -q "services:" docker-compose.example.yml; then
        echo -e "${GREEN}  ✅ Section services${NC}"
    fi

    if grep -q "postgres:" docker-compose.example.yml; then
        echo -e "${GREEN}  ✅ Service postgres${NC}"
    fi

    if grep -q "api:" docker-compose.example.yml; then
        echo -e "${GREEN}  ✅ Service api${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  docker-compose.example.yml manquant${NC}"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""

# ============================================
# 7. Résumé
# ============================================
echo "========================================================"
echo "📊 Résumé validation"
echo "========================================================"

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ VALIDATION RÉUSSIE - Aucun problème détecté${NC}"
    echo ""
    echo "Prochaines étapes:"
    echo "  1. docker build -t astroia-api ."
    echo "  2. docker run -p 8000:8000 --env-file .env astroia-api"
    echo "  3. curl http://localhost:8000/health"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️  VALIDATION OK avec $WARNINGS avertissements${NC}"
    echo ""
    echo "Les avertissements peuvent être ignorés si intentionnels."
    exit 0
else
    echo -e "${RED}❌ VALIDATION ÉCHOUÉE - $ERRORS erreurs, $WARNINGS avertissements${NC}"
    echo ""
    echo "Corriger les erreurs avant de continuer."
    exit 1
fi
