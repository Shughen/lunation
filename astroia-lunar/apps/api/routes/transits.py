"""
Routes FastAPI pour les Transits (P2)
Endpoints pour transits natals et transits sur révolutions lunaires
"""

from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, text
from typing import Dict, Any, Optional
from datetime import datetime, date
from uuid import UUID
import logging

from database import get_db
from services import transits_services
from schemas.transits import (
    NatalTransitsRequest,
    LunarReturnTransitsRequest,
    TransitsResponse,
    TransitsOverviewDB
)
from models.transits import TransitsOverview, TransitsEvent
from routes.auth import get_current_user
from models.user import User
from config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/transits", tags=["Transits"])


@router.post("/natal", response_model=TransitsResponse, status_code=200)
async def natal_transits(
    request: NatalTransitsRequest,
    major_only: bool = False,
    db: AsyncSession = Depends(get_db)
):
    """
    Calcule les transits planétaires actuels croisés avec le thème natal.

    Analyse les aspects formés par les planètes en transit avec les positions natales,
    permettant de comprendre les influences astrologiques du moment.

    - **user_id**: (Optionnel) ID utilisateur pour sauvegarde en DB
    - **birth_date**: Date de naissance
    - **transit_date**: Date du transit à calculer
    - **major_only**: Si True, ne retourne que les aspects majeurs (conjonction, opposition, carré, trigone)
    """
    try:
        # Conversion du modèle Pydantic en dict pour l'API
        payload = request.model_dump(exclude_none=True)

        logger.info(
            f"🔄 Calcul Natal Transits - user: {request.user_id}, "
            f"transit_date: {request.transit_date}, major_only: {major_only}"
        )

        # Appel au service RapidAPI
        result = await transits_services.get_natal_transits(payload)

        # Générer des insights avec filtrage optionnel des aspects majeurs
        insights = transits_services.generate_transit_insights(result, major_only=major_only)
        
        # Sauvegarde optionnelle en DB si user_id fourni
        if request.user_id:
            try:
                # Extraire le mois depuis transit_date
                transit_month = request.transit_date[:7]  # YYYY-MM
                
                # Vérifier si overview existe déjà pour ce mois
                stmt = select(TransitsOverview).where(
                    and_(
                        TransitsOverview.user_id == request.user_id,
                        TransitsOverview.month == transit_month
                    )
                )
                existing = await db.execute(stmt)
                existing_overview = existing.scalar_one_or_none()
                
                overview_data = {
                    "natal_transits": result,
                    "insights": insights,
                    "last_updated": datetime.now().isoformat()
                }
                
                if existing_overview:
                    # Mise à jour
                    existing_overview.overview = overview_data
                    logger.info(f"♻️  Transits overview mis à jour pour {transit_month}")
                else:
                    # Création
                    overview = TransitsOverview(
                        user_id=request.user_id,
                        month=transit_month,
                        overview=overview_data
                    )
                    db.add(overview)
                    logger.info(f"💾 Nouveau transits overview sauvegardé pour {transit_month}")
                
                await db.commit()
                
            except Exception as e:
                logger.error(f"❌ Erreur sauvegarde transits overview: {str(e)}")
                await db.rollback()
                # On continue malgré l'erreur DB
        
        return TransitsResponse(
            provider="rapidapi",
            kind="natal_transits",
            data=result,
            insights=insights,
            cached=False
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur calcul Natal Transits: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Erreur provider RapidAPI: {str(e)}"
        )


@router.post("/lunar_return", response_model=TransitsResponse, status_code=200)
async def lunar_return_transits(
    request: LunarReturnTransitsRequest,
    major_only: bool = False,
    db: AsyncSession = Depends(get_db)
):
    """
    Calcule les transits planétaires sur une révolution lunaire.

    Analyse comment les planètes en transit interagissent avec la carte
    de révolution lunaire du mois, pour affiner les prévisions mensuelles.

    - **user_id**: (Optionnel) ID utilisateur pour sauvegarde en DB
    - **month**: (Optionnel) Mois au format YYYY-MM pour indexation
    - **lunar_return_date**: Date de la révolution lunaire
    - **transit_date**: Date actuelle
    - **major_only**: Si True, ne retourne que les aspects majeurs (conjonction, opposition, carré, trigone)
    """
    try:
        # Conversion du modèle Pydantic en dict pour l'API
        payload = request.model_dump(exclude_none=True)

        logger.info(
            f"🌙 Calcul Lunar Return Transits - user: {request.user_id}, "
            f"LR date: {request.lunar_return_date}, transit: {request.transit_date}, major_only: {major_only}"
        )

        # Appel au service RapidAPI
        result = await transits_services.get_lunar_return_transits(payload)

        # Générer des insights avec filtrage optionnel des aspects majeurs
        insights = transits_services.generate_transit_insights(result, major_only=major_only)
        
        # Sauvegarde optionnelle en DB si user_id et month fournis
        if request.user_id and request.month:
            try:
                # Vérifier si overview existe déjà pour ce mois
                stmt = select(TransitsOverview).where(
                    and_(
                        TransitsOverview.user_id == request.user_id,
                        TransitsOverview.month == request.month
                    )
                )
                existing = await db.execute(stmt)
                existing_overview = existing.scalar_one_or_none()
                
                overview_data = {
                    "lunar_return_transits": result,
                    "insights": insights,
                    "last_updated": datetime.now().isoformat()
                }
                
                if existing_overview:
                    # Fusionner avec données existantes
                    if existing_overview.overview:
                        existing_overview.overview.update(overview_data)
                    else:
                        existing_overview.overview = overview_data
                    logger.info(f"♻️  LR Transits ajoutés à l'overview {request.month}")
                else:
                    # Création
                    overview = TransitsOverview(
                        user_id=request.user_id,
                        month=request.month,
                        overview=overview_data
                    )
                    db.add(overview)
                    logger.info(f"💾 Nouveau LR transits overview sauvegardé pour {request.month}")
                
                await db.commit()
                
            except Exception as e:
                logger.error(f"❌ Erreur sauvegarde LR transits overview: {str(e)}")
                await db.rollback()
        
        return TransitsResponse(
            provider="rapidapi",
            kind="lunar_return_transits",
            data=result,
            insights=insights,
            cached=False
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur calcul Lunar Return Transits: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Erreur provider RapidAPI: {str(e)}"
        )


@router.get("/overview/{user_id}/{month}", response_model=TransitsOverviewDB)
async def get_transits_overview(
    user_id: str,
    month: str,
    major_only: bool = False,
    current_user: User = Depends(get_current_user),
    x_dev_user_id: Optional[str] = Header(default=None, alias="X-Dev-User-Id"),
    db: AsyncSession = Depends(get_db)
):
    """
    Récupère la vue d'ensemble des transits pour un utilisateur et un mois donnés.

    Retourne les données en cache incluant les transits natals et LR du mois.
    Peut filtrer pour ne retourner que les aspects majeurs.

    - **user_id**: ID de l'utilisateur (integer string)
    - **month**: Mois au format YYYY-MM
    - **major_only**: Si True, filtre uniquement les aspects majeurs (conjonction, opposition, carré, trigone)

    En mode DEV_AUTH_BYPASS, utilise l'ID du header X-Dev-User-Id.
    """
    try:
        # === CONVERT user_id (str) to INTEGER ===
        try:
            user_id_int = int(user_id)
        except ValueError:
            raise HTTPException(
                status_code=422,
                detail=f"Invalid user_id format: {user_id} (must be integer)"
            )

        # === SECURITY CHECK: Verify user_id matches current_user ===
        # In production, users can only access their own transits
        if settings.APP_ENV != "development" or not settings.DEV_AUTH_BYPASS:
            if user_id_int != current_user.id:
                raise HTTPException(
                    status_code=403,
                    detail="Forbidden: cannot access other user's transits"
                )

        # En mode DEV_AUTH_BYPASS, utiliser l'ID du header si fourni
        if settings.APP_ENV == "development" and settings.DEV_AUTH_BYPASS and x_dev_user_id:
            try:
                user_id_int = int(x_dev_user_id)
                logger.debug(f"🔧 DEV_AUTH_BYPASS: utilisation user_id du header X-Dev-User-Id: {user_id_int}")
            except (ValueError, TypeError):
                logger.warning(f"⚠️ user_id du header X-Dev-User-Id invalide, utilisation de l'ID de l'URL: {user_id_int}")

        stmt = select(TransitsOverview).where(
            and_(
                TransitsOverview.user_id == user_id_int,
                TransitsOverview.month == month
            )
        )
        result = await db.execute(stmt)
        overview = result.scalar_one_or_none()

        if not overview:
            raise HTTPException(
                status_code=404,
                detail=f"Aucun transits overview trouvé pour user {user_id_int} et mois {month}"
            )

        # Si major_only=True, filtrer les aspects dans les données avant de retourner
        if major_only and overview.overview:
            # Recalculer les insights avec filtrage pour natal_transits
            if "natal_transits" in overview.overview:
                natal_data = overview.overview["natal_transits"]
                filtered_insights = transits_services.generate_transit_insights(natal_data, major_only=True)
                overview.overview["insights"] = filtered_insights

            # Recalculer les insights avec filtrage pour lunar_return_transits
            if "lunar_return_transits" in overview.overview:
                lr_data = overview.overview["lunar_return_transits"]
                filtered_lr_insights = transits_services.generate_transit_insights(lr_data, major_only=True)
                # Fusionner ou remplacer selon la logique métier
                if "insights" not in overview.overview:
                    overview.overview["insights"] = filtered_lr_insights
                else:
                    # Combiner les insights natal + LR
                    overview.overview["lr_insights"] = filtered_lr_insights

        return overview
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Erreur récupération transits overview: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erreur interne du serveur lors de la récupération des transits"
        )


@router.get("/overview/{user_id}", response_model=list[TransitsOverviewDB])
async def get_user_transits_history(
    user_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    """
    Récupère l'historique des transits overview pour un utilisateur.
    
    - **user_id**: ID de l'utilisateur
    """
    try:
        stmt = select(TransitsOverview).where(
            TransitsOverview.user_id == user_id
        ).order_by(TransitsOverview.month.desc())
        
        result = await db.execute(stmt)
        overviews = result.scalars().all()
        
        return overviews
        
    except Exception as e:
        logger.error(f"❌ Erreur récupération historique transits: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

