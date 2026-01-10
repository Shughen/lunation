# 🐍 Astro.IA Backend - FastAPI

**API REST moderne avec FastAPI, SQLAlchemy, et PostgreSQL**

---

## 📦 Technologies

- **FastAPI** - Framework web moderne et rapide
- **SQLAlchemy 2.0** - ORM Python
- **Alembic** - Migrations de base de données
- **PostgreSQL** - Base de données relationnelle
- **Redis** - Cache et sessions
- **Pydantic** - Validation des données
- **JWT** - Authentification
- **XGBoost** - Modèle ML parent-enfant

---

## 🚀 Démarrage Rapide

```bash
# Installation
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configuration
cp ../.env.example .env
# Éditer .env avec vos valeurs

# Lancer le serveur
uvicorn main:app --reload --port 8000
```

---

## 📁 Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/      # Routes API
│   │       └── router.py       # Router principal
│   ├── core/
│   │   ├── config.py           # Configuration
│   │   ├── security.py         # Auth & JWT
│   │   └── deps.py             # Dépendances
│   ├── db/
│   │   ├── base.py             # Base SQLAlchemy
│   │   ├── session.py          # Session DB
│   │   └── models/             # Modèles SQLAlchemy
│   ├── schemas/                # Schémas Pydantic
│   ├── services/               # Logique métier
│   ├── ml/                     # Modèles ML
│   └── utils/                  # Utilitaires
├── tests/                      # Tests
├── alembic/                    # Migrations
├── main.py                     # Point d'entrée
├── requirements.txt
└── README.md
```

---

## 🔧 Commandes Utiles

```bash
# Développement
uvicorn main:app --reload --port 8000

# Tests
pytest
pytest --cov=app tests/

# Linting
black .
ruff check .
mypy app/

# Migrations
alembic revision --autogenerate -m "Add users table"
alembic upgrade head

# Shell Python avec contexte
python -i -c "from app.db.session import SessionLocal; db = SessionLocal()"
```

---

## 📚 API Documentation

### Endpoints Principaux

#### Health Check
```bash
GET /health
```

#### Dashboard
```bash
GET /api/dashboard
```

#### Utilisateurs
```bash
POST   /api/users/register
POST   /api/users/login
GET    /api/users/me
PUT    /api/users/me
```

#### ML Parent-Enfant
```bash
POST   /api/ml/parent-child/predict
```

### Documentation Interactive

- **Swagger UI :** http://localhost:8000/docs
- **ReDoc :** http://localhost:8000/redoc

---

## 🔐 Authentification

L'API utilise JWT pour l'authentification.

```python
# Login
POST /api/users/login
{
  "email": "user@example.com",
  "password": "password123"
}

# Réponse
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer"
}

# Utilisation
GET /api/users/me
Authorization: Bearer eyJhbGci...
```

---

## 💾 Base de Données

### Modèles Principaux

- **User** - Utilisateurs
- **Profile** - Profils astrologiques
- **NatalChart** - Thèmes natals
- **Prediction** - Prédictions ML

### Migrations

```bash
# Créer une migration
alembic revision --autogenerate -m "Add table"

# Appliquer les migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 🤖 Machine Learning

Le backend intègre le modèle XGBoost optimisé (98.19% précision).

```python
from app.ml.predictor import ParentChildPredictor

predictor = ParentChildPredictor()
result = await predictor.predict(parent_data, child_data)
```

---

## 🧪 Tests

```bash
# Tous les tests
pytest

# Avec coverage
pytest --cov=app --cov-report=html

# Un fichier spécifique
pytest tests/test_api.py

# Avec logs
pytest -v -s
```

---

## 🔧 Variables d'Environnement

Voir `../.env.example` pour la liste complète.

**Obligatoires :**
- `DATABASE_URL` - URL PostgreSQL
- `SECRET_KEY` - Clé secrète JWT
- `OPENAI_API_KEY` - Clé OpenAI (si IA activée)

---

## 📊 Monitoring

### Logs

Les logs sont écrits dans `stdout` (Docker-friendly).

```python
from app.core.logging import logger

logger.info("Something happened")
logger.error("Error occurred", exc_info=True)
```

### Sentry (Optionnel)

```bash
SENTRY_DSN=https://xxx@sentry.io/xxx
```

---

## 🚢 Déploiement

### Railway

```bash
railway up
```

### Docker

```bash
docker build -t astroia-backend .
docker run -p 8000:8000 astroia-backend
```

### Render

```yaml
# render.yaml
services:
  - type: web
    name: astroia-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## 📝 Conventions de Code

### Nommage

- **Fonctions :** `snake_case`
- **Classes :** `PascalCase`
- **Constants :** `UPPER_SNAKE_CASE`
- **Modules :** `snake_case`

### Type Hints

```python
from typing import Optional, List
from app.schemas.user import User

async def get_user(user_id: int) -> Optional[User]:
    ...
```

### Docstrings

```python
async def create_user(email: str, password: str) -> User:
    """
    Crée un nouvel utilisateur.

    Args:
        email: Email de l'utilisateur
        password: Mot de passe en clair

    Returns:
        L'utilisateur créé

    Raises:
        HTTPException: Si l'email existe déjà
    """
    ...
```

---

## 🤝 Contribution

1. Créer une branche feature
2. Coder + Tests
3. Linter (`black`, `ruff`)
4. Pull Request

---

**API prête à l'emploi ! 🚀**

