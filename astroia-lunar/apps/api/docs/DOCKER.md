# 🚀 Docker Quick Start - Astroia Lunar API

Guide ultra-rapide pour containeriser et lancer l'API.

## ⚡ TL;DR

```bash
# 1. Build
cd apps/api
docker build -t astroia-api .

# 2. Run (avec .env)
docker run -p 8000:8000 --env-file .env astroia-api

# 3. Check
curl http://localhost:8000/health
```

## 🐳 Build l'image

```bash
cd apps/api
docker build -t astroia-api .
```

**Temps estimé** : 2-3 minutes (première fois)

**Taille image** : ~200 MB (multi-stage build optimisé)

## 🏃 Run le container

### Option 1 : Avec fichier .env existant

```bash
docker run -p 8000:8000 --env-file .env astroia-api
```

### Option 2 : Avec variables inline

```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql+asyncpg://postgres:password@host:5432/db \
  -e RAPIDAPI_KEY=your-rapidapi-key \
  -e ANTHROPIC_API_KEY=your-anthropic-key \
  -e SECRET_KEY=your-secret-jwt-key \
  -e APP_ENV=production \
  astroia-api
```

### Option 3 : Avec Docker Compose (recommandé)

```bash
# Copier et adapter config
cp docker-compose.example.yml docker-compose.yml
cp .env.docker.example .env.docker

# Éditer .env.docker avec vos secrets
nano .env.docker

# Lancer stack (API + PostgreSQL)
docker-compose up -d

# Voir logs
docker-compose logs -f api
```

## 🔧 Migrations Database

### Avant premier démarrage

```bash
# Option 1 : Migrations auto via entrypoint
# Modifier Dockerfile CMD: CMD ["./docker-entrypoint.sh"]
# Rebuild et run

# Option 2 : Migrations manuelles (recommandé)
docker-compose up -d
docker exec astroia-api alembic upgrade head
```

## ✅ Vérification

```bash
# Health check simple
curl http://localhost:8000/health

# Health check database
curl http://localhost:8000/health/db

# Docs API
open http://localhost:8000/docs
```

**Réponse attendue /health :**
```json
{
  "status": "healthy",
  "checks": {
    "database": "configured",
    "rapidapi_config": "configured"
  }
}
```

## 🛠️ Commandes utiles

```bash
# Voir containers running
docker ps

# Logs API
docker logs astroia-api -f

# Shell dans container
docker exec -it astroia-api /bin/bash

# Tests dans container
docker exec astroia-api pytest -q

# Alembic status
docker exec astroia-api alembic current

# Arrêter container
docker stop astroia-api

# Supprimer container
docker rm astroia-api

# Rebuild sans cache
docker build --no-cache -t astroia-api .
```

## 🐋 Docker Compose - Commandes

```bash
# Démarrer stack
docker-compose up -d

# Voir tous les logs
docker-compose logs -f

# Logs API uniquement
docker-compose logs -f api

# Logs DB uniquement
docker-compose logs -f postgres

# Status services
docker-compose ps

# Arrêter stack
docker-compose down

# Arrêter + supprimer volumes
docker-compose down -v
```

## 🔐 Variables d'environnement minimales

```bash
# Requis
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/astroia_lunar
SECRET_KEY=your-jwt-secret-key
RAPIDAPI_KEY=your-rapidapi-key
ANTHROPIC_API_KEY=your-anthropic-key

# Optionnel (avec defaults)
APP_ENV=production
API_HOST=0.0.0.0
API_PORT=8000
TZ=Europe/Paris
```

## 📝 Fichiers de config

| Fichier | Usage |
|---------|-------|
| `.env` | Variables locales (dev) |
| `.env.docker.example` | Template pour Docker |
| `docker-compose.yml` | Config stack Docker (ne pas commiter) |
| `docker-compose.example.yml` | Template stack (commiter) |

## 🚨 Troubleshooting rapide

### "Database connection failed"
```bash
# Vérifier DATABASE_URL
docker exec astroia-api env | grep DATABASE_URL

# Tester connexion manuelle
docker exec -it astroia-api bash
python -c "from config import settings; print(settings.DATABASE_URL)"
```

### "alembic: command not found"
```bash
# PATH incorrect, vérifier Dockerfile
docker exec astroia-api which alembic
```

### "Permission denied"
```bash
# Script entrypoint pas exécutable
chmod +x docker-entrypoint.sh
docker build --no-cache -t astroia-api .
```

### Image trop volumineuse
```bash
# Vérifier .dockerignore
docker history astroia-api
docker run --rm -it astroia-api ls -lah /app
```

## 📚 Documentation complète

- **Setup détaillé** : `DOCKER_README.md`
- **Validation specs** : `DOCKER_VALIDATION.md`
- **Config env** : `.env.docker.example`
- **Stack exemple** : `docker-compose.example.yml`

## 🎯 Next Steps

1. ✅ Build image locale
2. ✅ Test en local avec Docker
3. 🔜 Push image sur registry (Docker Hub, GCP, AWS ECR)
4. 🔜 Deploy sur staging
5. 🔜 Deploy sur production (K8s, Fly.io, etc.)

---

**Support** : Voir `DOCKER_README.md` pour troubleshooting avancé et déploiement production.
