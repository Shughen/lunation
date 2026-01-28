# Guide Deploiement Backend - Render

**Date** : 2026-01-28
**Application** : Lunation API (FastAPI)
**Status** : Production Ready

---

## Table des Matieres

1. [Prerequisites](#prerequisites)
2. [Configuration Render](#configuration-render)
3. [Variables d'Environnement](#variables-denvironnement)
4. [Deploiement](#deploiement)
5. [Post-Deploiement](#post-deploiement)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Comptes Requis
- [x] **Render** : https://render.com (gratuit ou $7/mois pour Starter)
- [x] **Supabase** : Base de donnees PostgreSQL deja configuree
- [x] **Anthropic** : Cle API pour generation Claude
- [x] **RapidAPI** : Cle API pour calculs astrologiques

### Code Source
- [x] Repository GitHub connecte a Render
- [x] Branch `main` a jour
- [x] Dockerfile valide dans `apps/api/`

---

## Configuration Render

### 1. Creer le Service

1. Aller sur https://dashboard.render.com
2. **New +** > **Web Service**
3. **Connect a Git Repository** > Selectionner `astroia-lunar`
4. Configurer :

| Parametre | Valeur |
|-----------|--------|
| Name | `lunation-api` |
| Region | `Frankfurt (EU Central)` (proche de Supabase EU) |
| Branch | `main` |
| Root Directory | `apps/api` |
| Runtime | `Docker` |
| Instance Type | `Free` ou `Starter ($7/mo)` |

> **Note** : Le tier Free a un "cold start" de 30-60s apres inactivite. Pour production serieuse, utiliser Starter.

### 2. Build Settings

Render detecte automatiquement le Dockerfile. Verifier :

- **Dockerfile Path** : `./Dockerfile`
- **Docker Command** : (laisser vide - utilise CMD du Dockerfile)

---

## Variables d'Environnement

Configurer dans **Environment** > **Environment Variables** :

### Variables Requises

```bash
# === DATABASE ===
DATABASE_URL=postgresql+asyncpg://postgres.[PROJECT_REF]:[PASSWORD]@aws-1-eu-west-3.pooler.supabase.com:5432/postgres

# === SECURITE ===
SECRET_KEY=<generer avec: openssl rand -hex 32>
APP_ENV=production
DEV_AUTH_BYPASS=false

# === ANTHROPIC (Claude AI) ===
ANTHROPIC_API_KEY=sk-ant-...
LUNAR_LLM_MODE=anthropic
LUNAR_CLAUDE_MODEL=opus

# === RAPIDAPI (Calculs Astrologiques) ===
RAPIDAPI_KEY=...
RAPIDAPI_HOST=best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com
```

### Variables Optionnelles

```bash
# Pool de connexions DB (ajuster si necessaire)
DATABASE_POOL_SIZE=10
DATABASE_MAX_OVERFLOW=20

# Timezone
TZ=Europe/Paris

# Desactiver Chiron (si fichiers Swiss Ephemeris absents)
DISABLE_CHIRON=true
```

### Generer SECRET_KEY

```bash
# Sur votre terminal local
openssl rand -hex 32
# Copier le resultat dans Render
```

---

## Deploiement

### 1. Premier Deploiement

1. Cliquer **Create Web Service**
2. Render clone le repo et build le Docker image
3. Attendre ~5-10 minutes pour le premier build

### 2. Verifier le Deploiement

```bash
# Health check
curl https://lunation-api.onrender.com/health

# Reponse attendue :
{
  "status": "healthy",
  "checks": {
    "database": "configured",
    "rapidapi_config": "configured"
  }
}
```

### 3. Migrations Database

Les migrations Alembic doivent etre executees manuellement la premiere fois :

**Option A : Via Render Shell**
1. Dashboard > Service > **Shell**
2. Executer :
```bash
alembic upgrade head
```

**Option B : Via Script de Demarrage**
Modifier le Dockerfile CMD (non recommande pour production) :
```dockerfile
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]
```

### 4. Verifier les Templates

```bash
# Verifier que les 1728 templates sont charges
curl https://lunation-api.onrender.com/health | jq
```

---

## Post-Deploiement

### URL de Production

Apres deploiement, Render fournit une URL :
```
https://lunation-api.onrender.com
```

Cette URL sera utilisee dans la configuration mobile.

### Configurer Domaine Custom (Optionnel)

1. Dashboard > Service > **Settings** > **Custom Domains**
2. Ajouter : `api.lunation.app` (exemple)
3. Configurer DNS chez votre registrar

### Activer Auto-Deploy

Par defaut, Render deploie automatiquement a chaque push sur `main`.

Pour desactiver :
- Dashboard > Service > **Settings** > **Build & Deploy** > **Auto-Deploy** = No

---

## Monitoring

### Logs

1. Dashboard > Service > **Logs**
2. Ou via CLI :
```bash
render logs --service lunation-api
```

### Metriques Prometheus

L'API expose `/metrics` pour Prometheus :
```bash
curl https://lunation-api.onrender.com/metrics
```

### Alertes Render

Configurer dans **Settings** > **Notifications** :
- Deploy failed
- Service down
- Health check failed

---

## Troubleshooting

### Probleme : Service ne demarre pas

**Symptome** : Build reussi mais service crash au demarrage

**Diagnostic** :
```bash
# Verifier les logs
render logs --service lunation-api --tail 100
```

**Solutions** :
1. Verifier `DATABASE_URL` correctement formate (avec `postgresql+asyncpg://`)
2. Verifier toutes les variables d'environnement requises
3. Verifier que Supabase autorise les connexions depuis Render (IP whitelist si applicable)

### Probleme : Cold Start lent (Free tier)

**Symptome** : Premier appel apres inactivite prend 30-60s

**Solutions** :
1. **Upgrader vers Starter** ($7/mois) - pas de cold start
2. **UptimeRobot** : Configurer un ping toutes les 10 minutes sur `/health`
3. **Cron job** : Ping periodique depuis autre service

### Probleme : Erreur connexion Supabase

**Symptome** : `connection refused` ou `timeout`

**Solutions** :
1. Verifier URL Supabase utilise le **pooler** (pas connexion directe)
   - Correct : `aws-1-eu-west-3.pooler.supabase.com`
   - Incorrect : `db.xxx.supabase.co`
2. Verifier mot de passe (pas de caracteres speciaux non-escapes)
3. Verifier SSL mode si requis

### Probleme : Anthropic API timeout

**Symptome** : Generations Claude echouent avec timeout

**Solutions** :
1. Verifier `ANTHROPIC_API_KEY` valide
2. Verifier quota Anthropic non depasse
3. Le systeme bascule automatiquement vers templates DB en cas d'echec

---

## Checklist Pre-Production

- [ ] DATABASE_URL pointe vers Supabase production
- [ ] SECRET_KEY genere et unique
- [ ] DEV_AUTH_BYPASS=false
- [ ] ANTHROPIC_API_KEY valide
- [ ] RAPIDAPI_KEY valide
- [ ] Health check retourne 200
- [ ] Migrations Alembic appliquees
- [ ] 1728 templates en DB
- [ ] Test endpoint `/api/lunar-returns/current` fonctionne

---

## Couts Estimes

| Tier | Prix | Cold Start | Recommande Pour |
|------|------|------------|-----------------|
| Free | $0 | 30-60s | Tests, demo |
| Starter | $7/mo | Non | Production legere |
| Standard | $25/mo | Non | Production serieuse |

**Note** : Les couts Anthropic sont separees (~$0.02/generation avec caching).

---

**Derniere mise a jour** : 2026-01-28
