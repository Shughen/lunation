"""
Router principal API v1
"""
from fastapi import APIRouter

from app.api.v1.endpoints import dashboard

api_router = APIRouter()

# Inclure les routers des endpoints
api_router.include_router(
    dashboard.router,
    prefix="/dashboard",
    tags=["dashboard"]
)

# Ajouter d'autres routers ici
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(ml.router, prefix="/ml", tags=["ml"])

