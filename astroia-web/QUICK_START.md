# 🚀 Quick Start - Astro.IA Web

**Lancez votre projet en 5 minutes !**

---

## ✅ Prérequis

- Node.js 18+
- Python 3.11+
- PostgreSQL 15+
- Redis (optionnel)

---

## 📦 Installation Complète

### Option 1 : Installation Automatique (Make)

```bash
cd /Users/remibeaurain/astroia/astroia-web

# 1. Installer toutes les dépendances
make install

# 2. Configurer l'environnement
cp .env.example .env
# Éditer .env avec vos valeurs

# 3. Lancer le développement
make dev
```

### Option 2 : Installation Manuelle

#### Backend (FastAPI)

```bash
cd backend

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
uvicorn main:app --reload --port 8000
```

#### Frontend (React)

```bash
cd frontend

# Installer les dépendances
npm install

# Lancer le serveur de développement
npm run dev
```

---

## 🐳 Option 3 : Docker (Le Plus Simple)

```bash
cd /Users/remibeaurain/astroia/astroia-web

# Lancer tout avec Docker Compose
docker-compose up --build

# Ou en arrière-plan
docker-compose up -d
```

**URLs :**
- Frontend : http://localhost:5173
- Backend : http://localhost:8000
- API Docs : http://localhost:8000/docs

---

## 🔧 Configuration

### 1. Copier .env.example

Il faut créer le fichier `.env` manuellement (bloqué par .gitignore) :

```bash
cd /Users/remibeaurain/astroia/astroia-web

# Créer .env depuis .env.example
cat .env.example > .env
```

### 2. Éditer .env

Ouvrir `.env` et remplir au minimum :

```bash
# Backend
DATABASE_URL=postgresql://astroia:password@localhost:5432/astroia_db
SECRET_KEY=changez-cette-cle-en-production
OPENAI_API_KEY=sk-votre-cle-ici

# Frontend
VITE_API_URL=http://localhost:8000
```

### 3. Créer la base de données

```bash
# Avec PostgreSQL installé localement
createdb astroia_db

# Ou avec psql
psql -U postgres -c "CREATE DATABASE astroia_db;"
```

---

## 🎯 Tester

### Backend

```bash
cd backend
source venv/bin/activate

# Lancer les tests
pytest

# Avec coverage
pytest --cov=app
```

### Frontend

```bash
cd frontend

# Lancer les tests
npm run test

# Avec UI
npm run test:ui
```

---

## 🌐 Accès

Une fois lancé, accédez à :

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend** | http://localhost:5173 | Application React |
| **Backend** | http://localhost:8000 | API FastAPI |
| **API Docs (Swagger)** | http://localhost:8000/docs | Documentation interactive |
| **API Docs (ReDoc)** | http://localhost:8000/redoc | Documentation alternative |
| **Health Check** | http://localhost:8000/health | Statut de l'API |

---

## 📚 Structure du Projet

```
astroia-web/
├── frontend/           # React + TypeScript + Vite
├── backend/            # FastAPI + Python
├── shared/             # Types & utils communs
├── docker-compose.yml  # Orchestration Docker
├── Makefile            # Commandes utiles
├── .env.example        # Template environnement
└── README.md           # Documentation
```

---

## 🛠️ Commandes Utiles

```bash
# Développement
make dev              # Lance frontend + backend
make frontend         # Frontend uniquement
make backend          # Backend uniquement

# Tests
make test             # Tous les tests
make test-frontend    # Tests frontend
make test-backend     # Tests backend

# Linting
make lint             # Lint tout
make format           # Formate tout

# Docker
make docker-up        # Lance Docker
make docker-down      # Arrête Docker
make docker-logs      # Logs en temps réel

# Nettoyage
make clean            # Supprime node_modules, venv, etc.
```

---

## 🔥 Troubleshooting

### Problème : Port 8000 déjà utilisé

```bash
# Trouver le processus
lsof -i :8000

# Tuer le processus
kill -9 <PID>
```

### Problème : Port 5173 déjà utilisé

```bash
# Même chose pour le frontend
lsof -i :5173
kill -9 <PID>
```

### Problème : Base de données non accessible

```bash
# Vérifier que PostgreSQL tourne
pg_isready

# Si pas de réponse, lancer PostgreSQL
brew services start postgresql@15  # macOS
sudo service postgresql start       # Linux
```

### Problème : Module Python non trouvé

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🎨 Développement

### Ajouter un nouveau endpoint

1. **Backend** : `backend/app/api/v1/endpoints/mon_endpoint.py`
2. **Frontend** : `frontend/src/services/monService.ts`
3. **Shared** : `shared/types/monType.ts` (si nécessaire)

### Ajouter un nouveau composant

```bash
cd frontend/src/components
mkdir MonComposant
touch MonComposant/index.tsx
```

### Ajouter une migration DB

```bash
cd backend
alembic revision --autogenerate -m "Add new table"
alembic upgrade head
```

---

## 📖 Documentation Complète

- [Frontend README](./frontend/README.md)
- [Backend README](./backend/README.md)
- [Shared README](./shared/README.md)
- [API Documentation](http://localhost:8000/docs)

---

## ✅ Checklist de Premier Lancement

- [ ] Node.js 18+ installé
- [ ] Python 3.11+ installé
- [ ] PostgreSQL installé et lancé
- [ ] `.env` créé et rempli
- [ ] Base de données créée
- [ ] Dépendances backend installées
- [ ] Dépendances frontend installées
- [ ] Backend lancé (http://localhost:8000)
- [ ] Frontend lancé (http://localhost:5173)
- [ ] Testé un appel API (http://localhost:8000/health)

---

**Prêt à coder ! 🚀✨**

