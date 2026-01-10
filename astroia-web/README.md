# 🌟 Astro.IA Web - Architecture Monorepo

**Architecture moderne avec Frontend React + Backend FastAPI + Shared utilities**

---

## 📁 Structure du Projet

```
astroia-web/
├── frontend/           # Application React (TypeScript)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
├── backend/            # API FastAPI (Python)
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── main.py
│
├── shared/             # Utilitaires communs
│   ├── types/          # Types TypeScript/Python
│   ├── constants/      # Constantes partagées
│   └── utils/          # Fonctions utilitaires
│
├── docker-compose.yml  # Orchestration Docker
├── .env.example        # Variables d'environnement
└── README.md           # Ce fichier
```

---

## 🚀 Quick Start

### Prérequis
- Node.js 18+
- Python 3.11+
- Docker & Docker Compose (optionnel)

### Installation complète

```bash
# Cloner et installer
cd astroia-web

# Option 1 : Installation manuelle
make install

# Option 2 : Avec Docker
docker-compose up --build
```

### Développement

```bash
# Terminal 1 : Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Terminal 2 : Frontend
cd frontend
npm install
npm run dev
```

---

## 🏗️ Architecture

### Frontend (React + TypeScript + Vite)
- **Framework :** React 18
- **Build :** Vite
- **State :** Zustand
- **Routing :** React Router
- **UI :** Tailwind CSS + shadcn/ui
- **API Client :** Axios + React Query

### Backend (FastAPI + Python)
- **Framework :** FastAPI
- **ORM :** SQLAlchemy
- **Validation :** Pydantic
- **Auth :** JWT
- **DB :** PostgreSQL
- **Cache :** Redis (optionnel)

### Shared
- **Types :** Partagés entre TS et Python (via dataclasses/pydantic)
- **Constants :** Variables communes (API endpoints, codes d'erreur)
- **Utils :** Fonctions réutilisables

---

## 📦 Technologies

| Couche | Technologies |
|--------|--------------|
| **Frontend** | React, TypeScript, Vite, Tailwind CSS, Zustand, React Query |
| **Backend** | FastAPI, Pydantic, SQLAlchemy, Alembic, Python 3.11+ |
| **Database** | PostgreSQL, Redis |
| **DevOps** | Docker, Docker Compose, Nginx |
| **Testing** | Vitest (frontend), Pytest (backend) |
| **Linting** | ESLint, Prettier, Black, Ruff |

---

## 🔧 Commandes Utiles

```bash
# Development
make dev              # Lance frontend + backend
make frontend         # Lance uniquement frontend
make backend          # Lance uniquement backend

# Testing
make test             # Tests frontend + backend
make test-frontend    # Tests frontend
make test-backend     # Tests backend

# Linting
make lint             # Lint tout
make format           # Format tout

# Docker
make docker-up        # Lance Docker
make docker-down      # Arrête Docker
make docker-logs      # Voir les logs
```

---

## 🌐 URLs de Développement

- **Frontend :** http://localhost:5173
- **Backend API :** http://localhost:8000
- **API Docs :** http://localhost:8000/docs
- **pgAdmin :** http://localhost:5050 (si Docker)

---

## 📝 Variables d'Environnement

Copier `.env.example` vers `.env` et remplir :

```bash
# Backend
DATABASE_URL=postgresql://user:pass@localhost:5432/astroia
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=sk-...

# Frontend
VITE_API_URL=http://localhost:8000
```

---

## 🚢 Déploiement

### Vercel (Frontend) + Railway (Backend)

```bash
# Frontend sur Vercel
cd frontend
vercel --prod

# Backend sur Railway
cd backend
railway up
```

### Docker (Production)

```bash
docker-compose -f docker-compose.prod.yml up -d
```

---

## 📚 Documentation

- [Frontend README](./frontend/README.md)
- [Backend README](./backend/README.md)
- [Shared README](./shared/README.md)
- [API Documentation](http://localhost:8000/docs)

---

## 🤝 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amazing`)
3. Commit (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing`)
5. Ouvrir une Pull Request

---

## 📄 Licence

MIT

---

**Créé avec ❤️ par l'équipe Astro.IA**

