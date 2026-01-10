.PHONY: help setup install dev frontend backend test lint format docker-up docker-down docker-build clean check-env

# Couleurs pour les messages
GREEN  := \033[0;32m
YELLOW := \033[0;33m
BLUE   := \033[0;34m
RESET  := \033[0m

help: ## Affiche l'aide avec toutes les commandes disponibles
	@echo "$(BLUE)╔════════════════════════════════════════════════════════╗$(RESET)"
	@echo "$(BLUE)║       Astro.IA Web - Commandes Disponibles            ║$(RESET)"
	@echo "$(BLUE)╚════════════════════════════════════════════════════════╝$(RESET)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}'
	@echo ""

setup: ## Installation et configuration automatique complète du projet
	@echo "$(BLUE)════════════════════════════════════════════════════════$(RESET)"
	@echo "$(BLUE)     Astro.IA Web - Installation Automatique           $(RESET)"
	@echo "$(BLUE)════════════════════════════════════════════════════════$(RESET)"
	@echo ""
	@# Étape 1 : Vérifier et créer .env
	@echo "$(YELLOW)➜ [1/5] Vérification du fichier .env...$(RESET)"
	@if [ ! -f .env ]; then \
		echo "  └─ Fichier .env introuvable, copie depuis .env.example..."; \
		cp .env.example .env; \
		echo "  └─ $(GREEN)✓ Fichier .env créé avec succès$(RESET)"; \
		echo "  └─ $(YELLOW)⚠️  N'oubliez pas d'éditer .env avec vos vraies valeurs !$(RESET)"; \
	else \
		echo "  └─ $(GREEN)✓ Fichier .env existe déjà$(RESET)"; \
	fi
	@echo ""
	@# Étape 2 : Installation Frontend
	@echo "$(YELLOW)➜ [2/5] Installation des dépendances Frontend (npm)...$(RESET)"
	@if [ -d "frontend" ]; then \
		cd frontend && npm install; \
		echo "  └─ $(GREEN)✓ Dépendances Frontend installées$(RESET)"; \
	else \
		echo "  └─ $(YELLOW)⚠️  Dossier frontend/ introuvable$(RESET)"; \
	fi
	@echo ""
	@# Étape 3 : Installation Backend
	@echo "$(YELLOW)➜ [3/5] Installation des dépendances Backend (Python venv + pip)...$(RESET)"
	@if [ -d "backend" ]; then \
		cd backend && \
		if [ ! -d "venv" ]; then \
			echo "  └─ Création de l'environnement virtuel Python..."; \
			python3 -m venv venv; \
		fi && \
		echo "  └─ Installation des dépendances Python..."; \
		. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt; \
		echo "  └─ $(GREEN)✓ Dépendances Backend installées$(RESET)"; \
	else \
		echo "  └─ $(YELLOW)⚠️  Dossier backend/ introuvable$(RESET)"; \
	fi
	@echo ""
	@# Étape 4 : Build Docker
	@echo "$(YELLOW)➜ [4/5] Construction des images Docker...$(RESET)"
	@if command -v docker >/dev/null 2>&1; then \
		docker-compose build --no-cache; \
		echo "  └─ $(GREEN)✓ Images Docker construites$(RESET)"; \
	else \
		echo "  └─ $(YELLOW)⚠️  Docker non installé, étape ignorée$(RESET)"; \
	fi
	@echo ""
	@# Étape 5 : Lancer Docker Compose
	@echo "$(YELLOW)➜ [5/5] Lancement du projet avec Docker Compose...$(RESET)"
	@if command -v docker >/dev/null 2>&1; then \
		docker-compose up -d; \
		echo "  └─ $(GREEN)✓ Projet lancé avec succès !$(RESET)"; \
	else \
		echo "  └─ $(YELLOW)⚠️  Docker non installé, étape ignorée$(RESET)"; \
	fi
	@echo ""
	@# Message final avec URLs
	@echo "$(GREEN)╔════════════════════════════════════════════════════════╗$(RESET)"
	@echo "$(GREEN)║           Installation Terminée ! 🎉                  ║$(RESET)"
	@echo "$(GREEN)╚════════════════════════════════════════════════════════╝$(RESET)"
	@echo ""
	@echo "$(BLUE)🌐 URLs Locales :$(RESET)"
	@echo "  • Frontend   → $(YELLOW)http://localhost:5173$(RESET)"
	@echo "  • Backend    → $(YELLOW)http://localhost:8000$(RESET)"
	@echo "  • API Docs   → $(YELLOW)http://localhost:8000/docs$(RESET)"
	@echo ""
	@echo "$(BLUE)📝 Prochaines étapes :$(RESET)"
	@echo "  1. Éditer le fichier .env avec vos vraies valeurs"
	@echo "  2. Vérifier les logs : $(GREEN)make docker-logs$(RESET)"
	@echo "  3. Accéder au frontend : $(GREEN)http://localhost:5173$(RESET)"
	@echo ""
	@echo "$(BLUE)💡 Commandes utiles :$(RESET)"
	@echo "  • $(GREEN)make help$(RESET)         → Voir toutes les commandes"
	@echo "  • $(GREEN)make docker-logs$(RESET)  → Voir les logs en temps réel"
	@echo "  • $(GREEN)make docker-down$(RESET)  → Arrêter le projet"
	@echo ""

install: ## Installe toutes les dépendances (sans Docker)
	@echo "$(BLUE)📦 Installation des dépendances...$(RESET)"
	@cd frontend && npm install
	@cd backend && python3 -m venv venv && . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "$(GREEN)✅ Installation terminée !$(RESET)"

check-env: ## Vérifie si .env existe
	@if [ ! -f .env ]; then \
		echo "$(YELLOW)⚠️  Fichier .env introuvable !$(RESET)"; \
		echo "Exécutez : $(GREEN)make setup$(RESET) ou copiez manuellement .env.example"; \
		exit 1; \
	fi

dev: check-env ## Lance frontend + backend en parallèle (sans Docker)
	@echo "$(BLUE)🚀 Lancement du serveur de développement...$(RESET)"
	@(trap 'kill 0' SIGINT; \
		(cd backend && . venv/bin/activate && uvicorn main:app --reload --port 8000) & \
		(cd frontend && npm run dev))

frontend: ## Lance uniquement le frontend
	@echo "$(BLUE)🎨 Lancement du frontend...$(RESET)"
	@cd frontend && npm run dev

backend: check-env ## Lance uniquement le backend
	@echo "$(BLUE)🐍 Lancement du backend...$(RESET)"
	@cd backend && . venv/bin/activate && uvicorn main:app --reload --port 8000

test: ## Lance tous les tests (frontend + backend)
	@echo "$(BLUE)🧪 Exécution des tests...$(RESET)"
	@cd frontend && npm run test
	@cd backend && . venv/bin/activate && pytest

test-frontend: ## Tests frontend uniquement
	@echo "$(BLUE)🧪 Tests frontend...$(RESET)"
	@cd frontend && npm run test

test-backend: ## Tests backend uniquement
	@echo "$(BLUE)🧪 Tests backend...$(RESET)"
	@cd backend && . venv/bin/activate && pytest

lint: ## Lint tout le code (frontend + backend)
	@echo "$(BLUE)🔍 Linting du code...$(RESET)"
	@cd frontend && npm run lint
	@cd backend && . venv/bin/activate && ruff check . && black --check .

format: ## Formate tout le code
	@echo "$(BLUE)✨ Formatage du code...$(RESET)"
	@cd frontend && npm run format
	@cd backend && . venv/bin/activate && black . && ruff --fix .

docker-build: ## Rebuild les images Docker
	@echo "$(BLUE)🐳 Construction des images Docker...$(RESET)"
	@docker-compose build --no-cache
	@echo "$(GREEN)✅ Images construites !$(RESET)"

docker-up: ## Lance Docker Compose en arrière-plan
	@echo "$(BLUE)🐳 Lancement de Docker Compose...$(RESET)"
	@docker-compose up -d
	@echo "$(GREEN)✅ Containers lancés !$(RESET)"
	@echo ""
	@echo "$(BLUE)🌐 URLs :$(RESET)"
	@echo "  • Frontend → $(YELLOW)http://localhost:5173$(RESET)"
	@echo "  • Backend  → $(YELLOW)http://localhost:8000$(RESET)"
	@echo "  • API Docs → $(YELLOW)http://localhost:8000/docs$(RESET)"

docker-down: ## Arrête Docker Compose
	@echo "$(BLUE)🛑 Arrêt de Docker Compose...$(RESET)"
	@docker-compose down
	@echo "$(GREEN)✅ Containers arrêtés !$(RESET)"

docker-logs: ## Affiche les logs Docker en temps réel
	@docker-compose logs -f

docker-ps: ## Liste les containers Docker actifs
	@docker-compose ps

docker-restart: ## Redémarre tous les containers
	@echo "$(BLUE)🔄 Redémarrage des containers...$(RESET)"
	@docker-compose restart
	@echo "$(GREEN)✅ Containers redémarrés !$(RESET)"

clean: ## Nettoie les fichiers temporaires et dépendances
	@echo "$(BLUE)🧹 Nettoyage en cours...$(RESET)"
	@rm -rf frontend/node_modules frontend/dist
	@rm -rf backend/venv backend/__pycache__ backend/.pytest_cache
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "$(GREEN)✅ Nettoyage terminé !$(RESET)"

clean-docker: ## Nettoie les volumes et images Docker
	@echo "$(BLUE)🧹 Nettoyage Docker...$(RESET)"
	@docker-compose down -v
	@docker system prune -f
	@echo "$(GREEN)✅ Docker nettoyé !$(RESET)"

reset: clean clean-docker setup ## Reset complet : nettoie tout et réinstalle
	@echo "$(GREEN)✅ Reset complet terminé !$(RESET)"
