# 🐋 Astroia Lunar API - Docker Guide

Guide complet pour containeriser et déployer l'API FastAPI avec Docker.

## 📦 Fichiers Docker

- `Dockerfile` : Image multi-stage optimisée (Python 3.10-slim)
- `.dockerignore` : Exclut fichiers inutiles du build context
- `docker-entrypoint.sh` : Script de démarrage avec migrations Alembic
- `docker-compose.example.yml` : Exemple stack complète (API + PostgreSQL)

## 🚀 Quick Start

### Option 1 : Docker seul (API uniquement)

```bash
cd apps/api

# Build image
docker build -t astroia-api .

# Run avec fichier .env
docker run -p 8000:8000 --env-file .env astroia-api

# Run avec variables inline
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/db \
  -e RAPIDAPI_KEY=your-key \
  -e ANTHROPIC_API_KEY=your-key \
  -e APP_ENV=production \
  astroia-api

# Healthcheck
curl http://localhost:8000/health
```

### Option 2 : Docker Compose (API + Database)

```bash
cd apps/api

# Copier et adapter docker-compose
cp docker-compose.example.yml docker-compose.yml
# Éditer docker-compose.yml avec vos secrets

# Lancer stack complète
docker-compose up -d

# Vérifier logs
docker-compose logs -f api

# Arrêter
docker-compose down
```

## 🔧 Migrations Alembic

### Méthode 1 : Migrations automatiques (via entrypoint)

Modifier `Dockerfile` CMD :
```dockerfile
CMD ["./docker-entrypoint.sh"]
```

Le script `docker-entrypoint.sh` exécutera `alembic upgrade head` au démarrage.

### Méthode 2 : Migrations manuelles (recommandé)

```bash
# Démarrer le container
docker-compose up -d

# Exécuter migrations manuellement
docker exec astroia-api alembic upgrade head

# Vérifier état migrations
docker exec astroia-api alembic current
```

### Méthode 3 : Avant premier démarrage

```bash
# Build image
docker build -t astroia-api .

# Run container temporaire pour migrations
docker run --rm \
  -e DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/db \
  astroia-api \
  alembic upgrade head

# Démarrer API normalement
docker run -d -p 8000:8000 --env-file .env astroia-api
```

## 🔐 Variables d'environnement requises

### Minimum viable

```bash
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/astroia_lunar
SECRET_KEY=your-secret-key-here
RAPIDAPI_KEY=your-rapidapi-key
ANTHROPIC_API_KEY=your-anthropic-key
```

### Complète (voir `.env.example`)

```bash
# Database
DATABASE_URL=postgresql+asyncpg://postgres:password@postgres:5432/astroia_lunar
DATABASE_POOL_SIZE=10
DATABASE_MAX_OVERFLOW=20

# API
APP_ENV=production
API_HOST=0.0.0.0
API_PORT=8000

# JWT
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# RapidAPI
RAPIDAPI_KEY=your-rapidapi-key
RAPIDAPI_HOST=best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
BASE_RAPID_URL=https://best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com

# Anthropic
ANTHROPIC_API_KEY=your-anthropic-key
NATAL_LLM_MODE=off  # ou 'anthropic'
NATAL_INTERPRETATION_VERSION=2

# Dev Flags (désactiver en production)
DEV_MOCK_NATAL=false
DEV_MOCK_RAPIDAPI=false
DEV_AUTH_BYPASS=false
ALLOW_DEV_PURGE=false

# Timezone
TZ=Europe/Paris
```

## 📊 Healthcheck

L'image inclut un healthcheck automatique :

```bash
# Vérifier état container
docker ps

# Tester manuellement
curl http://localhost:8000/health
curl http://localhost:8000/health/db
```

Réponse attendue :
```json
{
  "status": "healthy",
  "checks": {
    "database": "configured",
    "rapidapi_config": "configured"
  }
}
```

## 🔍 Debugging

### Logs container

```bash
# Logs API
docker logs astroia-api -f

# Logs tous services
docker-compose logs -f

# Logs spécifique
docker-compose logs api
```

### Shell interactif

```bash
# Entrer dans container
docker exec -it astroia-api /bin/bash

# Tester commandes
alembic current
pytest -q
python -c "from config import settings; print(settings.DATABASE_URL)"
```

### Tests dans container

```bash
# Run tests
docker exec astroia-api pytest -q

# Tests avec output détaillé
docker exec astroia-api pytest -v
```

## 🏗️ Build optimisé

### Multi-stage build

Le Dockerfile utilise 2 stages :
1. **Builder** : Compile dépendances Python (gcc, libpq-dev)
2. **Runtime** : Image slim sans build tools (uniquement libpq5)

Résultat : Image finale ~200MB au lieu de ~800MB

### Build arguments

```bash
# Build avec tag custom
docker build -t astroia-api:v1.0.0 .

# Build sans cache
docker build --no-cache -t astroia-api .

# Build avec context différent
docker build -f apps/api/Dockerfile -t astroia-api .
```

## 🚢 Déploiement Production

### Recommandations

1. **Variables d'environnement** : Utiliser secrets manager (AWS Secrets, Kubernetes Secrets)
2. **Migrations** : Exécuter manuellement avant déploiement (pas d'auto-migration)
3. **Workers** : Ajuster nombre workers uvicorn selon CPU
4. **Reverse proxy** : Nginx/Traefik devant API
5. **SSL/TLS** : Terminer SSL au reverse proxy
6. **Monitoring** : Prometheus/Grafana pour métriques

### Exemple Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: astroia-api
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: api
        image: astroia-api:v1.0.0
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: astroia-secrets
              key: database-url
        - name: APP_ENV
          value: "production"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 30
        resources:
          limits:
            memory: "512Mi"
            cpu: "500m"
```

### Exemple Fly.io

```toml
# fly.toml
app = "astroia-api"

[build]
  dockerfile = "Dockerfile"

[[services]]
  internal_port = 8000
  protocol = "tcp"

  [services.concurrency]
    hard_limit = 25
    soft_limit = 20

  [[services.ports]]
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443

  [[services.http_checks]]
    interval = 10000
    grace_period = "5s"
    method = "get"
    path = "/health"
```

## 🛠️ Troubleshooting

### Erreur "alembic: command not found"

Le PATH n'inclut pas `/home/appuser/.local/bin`.

Solution : Vérifier `ENV PATH` dans Dockerfile.

### Erreur "Database connection failed"

1. Vérifier DATABASE_URL
2. Vérifier que DB est accessible depuis container
3. Tester connexion manuelle :

```bash
docker exec -it astroia-api bash
python -c "from database import engine; print('DB OK')"
```

### Erreur "Permission denied" au démarrage

Le script entrypoint n'est pas exécutable.

Solution :
```bash
chmod +x docker-entrypoint.sh
docker build --no-cache -t astroia-api .
```

### Image trop volumineuse

Vérifier `.dockerignore` :
```bash
# Voir taille layers
docker history astroia-api

# Analyser contenu image
docker run --rm -it astroia-api ls -lah /app
```

## 📚 Ressources

- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [Alembic Migrations](https://alembic.sqlalchemy.org/)
- [Uvicorn Deployment](https://www.uvicorn.org/deployment/)
