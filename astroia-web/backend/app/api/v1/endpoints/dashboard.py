"""
Endpoints Dashboard
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db

router = APIRouter()


@router.get("")
async def get_dashboard(db: Session = Depends(get_db)):
    """
    Retourne les données du dashboard
    """
    # Mock data pour commencer
    return {
        "stats": {
            "analyses": 142,
            "predictions": 89,
            "ml_accuracy": 98.19,
        },
        "recent_activity": [],
    }

