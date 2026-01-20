"""
Route pour interpretations d'aspects du theme natal
Recupere les interpretations pre-generees depuis la DB
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from database import get_db
from models.user import User
from schemas.natal_aspect_interpretation import (
    NatalAspectInterpretationRequest,
    NatalAspectInterpretationResponse
)
from services.natal_aspect_interpretation_service import (
    get_aspect_interpretation,
    ASPECT_PLANETS,
    ASPECT_TYPES
)
from routes.auth import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/aspect-interpretation", response_model=NatalAspectInterpretationResponse, status_code=status.HTTP_200_OK)
async def get_natal_aspect_interpretation(
    request: NatalAspectInterpretationRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Recupere une interpretation d'aspect natal

    Strategie:
    - Cherche d'abord dans les interpretations pre-generees (DB)
    - Si non trouve, retourne un placeholder

    Args:
        request: Donnees de l'aspect (planet1, planet2, aspect_type, lang)

    Returns:
        NatalAspectInterpretationResponse avec texte et source

    Raises:
        HTTPException 400: Si planetes ou type d'aspect invalides
    """
    # Valider les planetes
    planet1_lower = request.planet1.lower()
    planet2_lower = request.planet2.lower()

    if planet1_lower not in ASPECT_PLANETS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Planete invalide: {request.planet1}. Planetes supportees: {', '.join(ASPECT_PLANETS)}"
        )

    if planet2_lower not in ASPECT_PLANETS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Planete invalide: {request.planet2}. Planetes supportees: {', '.join(ASPECT_PLANETS)}"
        )

    if planet1_lower == planet2_lower:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Les deux planetes doivent etre differentes"
        )

    # Valider le type d'aspect
    aspect_lower = request.aspect_type.lower()
    if aspect_lower not in ASPECT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Type d'aspect invalide: {request.aspect_type}. Types supportes: {', '.join(ASPECT_TYPES)}"
        )

    logger.info(
        f"Demande interpretation aspect - user={current_user.id}, "
        f"{planet1_lower}-{planet2_lower} {aspect_lower}, lang={request.lang}"
    )

    try:
        # Obtenir l'interpretation (DB ou placeholder)
        text, source, p1_norm, p2_norm = await get_aspect_interpretation(
            db=db,
            planet1=planet1_lower,
            planet2=planet2_lower,
            aspect_type=aspect_lower,
            version=2,
            lang=request.lang
        )

        logger.info(f"Interpretation aspect retournee: {p1_norm}-{p2_norm} {aspect_lower} (source={source})")

        return NatalAspectInterpretationResponse(
            planet1=p1_norm,
            planet2=p2_norm,
            aspect_type=aspect_lower,
            text=text,
            source=source,
            version=2
        )

    except Exception as e:
        logger.error(f"Erreur recuperation interpretation aspect: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
