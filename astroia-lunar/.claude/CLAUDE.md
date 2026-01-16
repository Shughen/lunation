# Astroia Lunar – règles de contribution (Claude Code)

## Contexte
Monorepo: apps/api (FastAPI) + apps/mobile (Expo). Par défaut: NE PAS toucher apps/mobile sauf demande explicite.

## Objectif actuel
Stabiliser le backend natal (routes + services) et corriger l’intégration Anthropic (401).

## Règles strictes
- Ne jamais modifier .env
- Ne jamais afficher/commiter de secrets
- Un changement = un commit
- Priorité: correctif minimal, tests, puis refacto

## Commandes utiles
- Backend tests: cd apps/api && pytest -q
- Run API: cd apps/api && uvicorn main:app --reload --host 0.0.0.0 --port 8000

## Definition of Done (DoD)
- `pytest -q` OK
- `curl .../api/natal/interpretation` -> 200 OK
- aucun changement dans `apps/mobile` (sauf demande explicite)
- aucun secret affiché/commité

## Zones interdites
- Ne jamais modifier/commiter: `.env`, `**/*.key`, `**/secrets*`
- Ne jamais toucher: `apps/mobile`, sauf demande explicite
