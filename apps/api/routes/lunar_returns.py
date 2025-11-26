"""
Routes pour les révolutions lunaires
Gère la génération et la récupération des révolutions lunaires depuis Supabase
"""

from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from uuid import UUID
from datetime import datetime
import logging
from dateutil import parser as date_parser

from schemas.lunar_return import (
    LunarReturnGenerateRequest,
    LunarReturnResponse,
    UserProfileForLunarReturn
)
from services.lunar_return_service import (
    calculate_lunar_return,
    create_lunar_return,
    list_lunar_returns,
    get_lunar_return_by_id
)

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/generate", response_model=LunarReturnResponse, status_code=status.HTTP_201_CREATED)
async def generate_lunar_return(request: LunarReturnGenerateRequest):
    """
    Génère et sauvegarde une révolution lunaire pour un utilisateur
    
    Processus:
    1. Récupère le profil utilisateur depuis Supabase
    2. Calcule la date exacte de la révolution lunaire
    3. Calcule les positions planétaires via RapidAPI
    4. Génère les aspects et interprétations
    5. Sauvegarde dans Supabase (table lunar_returns)
    """
    try:
        logger.info(f"🌙 Génération révolution lunaire cycle {request.cycle_number} pour user {request.user_id}")
        
        # Récupérer le profil utilisateur depuis Supabase
        from lib.supabase_client import get_supabase_client
        supabase = get_supabase_client()
        
        logger.info(f"🔍 Récupération profil utilisateur {request.user_id} depuis Supabase...")
        
        try:
            profile_response = supabase.table("profiles")\
                .select("*")\
                .eq("id", str(request.user_id))\
                .single()\
                .execute()
        except Exception as e:
            logger.error(f"❌ Erreur lors de la récupération du profil: {type(e).__name__}: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erreur lors de la récupération du profil: {str(e)}"
            )
        
        if not profile_response.data:
            logger.warning(f"⚠️ Profil {request.user_id} non trouvé dans Supabase")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Profil utilisateur {request.user_id} non trouvé"
            )
        
        profile_data = profile_response.data
        logger.info(f"✅ Profil trouvé: {profile_data.get('birth_place', 'N/A')}")
        
        # Vérifier que les données nécessaires sont présentes
        if not profile_data.get("birth_date"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Date de naissance manquante dans le profil"
            )
        
        if not profile_data.get("birth_place"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Lieu de naissance manquant dans le profil"
            )
        
        # Construire le profil pour le calcul
        # Parser birth_date (format TIMESTAMP ou DATE)
        birth_date_str = profile_data["birth_date"]
        if isinstance(birth_date_str, str):
            # Nettoyer le format de date
            birth_date_str = birth_date_str.replace("Z", "+00:00")
            try:
                birth_date = datetime.fromisoformat(birth_date_str)
            except ValueError:
                # Essayer un autre format
                birth_date = date_parser.parse(birth_date_str)
        else:
            birth_date = birth_date_str
        
        # Parser birth_time (format TIME, pas DATETIME)
        birth_time = None
        if profile_data.get("birth_time"):
            birth_time_str = profile_data["birth_time"]
            try:
                # birth_time est un TIME (HH:MM:SS), pas un DATETIME
                if isinstance(birth_time_str, str):
                    # Extraire les heures et minutes du TIME
                    parts = birth_time_str.split(":")
                    hour = int(parts[0]) if len(parts) > 0 else 0
                    minute = int(parts[1]) if len(parts) > 1 else 0
                    # Créer un datetime avec la date de naissance + heure
                    birth_time = birth_date.replace(hour=hour, minute=minute, second=0, microsecond=0)
                else:
                    birth_time = birth_time_str
            except Exception as e:
                logger.warning(f"⚠️ Impossible de parser birth_time: {birth_time_str}, erreur: {e}")
        
        # Récupérer latitude/longitude depuis le cache local ou Supabase
        # Si elles ne sont pas dans Supabase, utiliser des valeurs par défaut ou chercher depuis birth_place
        latitude = profile_data.get("latitude")
        longitude = profile_data.get("longitude")
        
        # Si latitude/longitude manquantes, utiliser des valeurs par défaut pour Paris
        if latitude is None or longitude is None:
            logger.warning(f"⚠️ Latitude/Longitude manquantes pour user {request.user_id}, utilisation de Paris par défaut")
            latitude = latitude or 48.8566
            longitude = longitude or 2.3522
        
        user_profile = UserProfileForLunarReturn(
            birth_date=birth_date,
            birth_time=birth_time,
            birth_place=profile_data["birth_place"],
            latitude=float(latitude),
            longitude=float(longitude),
            timezone=profile_data.get("timezone", "Europe/Paris")
        )
        
        logger.info(f"📋 Profil utilisateur construit: {user_profile.birth_place}, lat={user_profile.latitude}, lon={user_profile.longitude}")
        
        # Calculer la révolution
        computed_data = await calculate_lunar_return(user_profile, request.cycle_number)
        
        # Sauvegarder dans Supabase
        created = await create_lunar_return(request.user_id, computed_data)
        
        return LunarReturnResponse(**created)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Erreur génération révolution lunaire: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la génération de la révolution lunaire: {str(e)}"
        )


@router.get("", response_model=List[LunarReturnResponse])
async def get_lunar_returns(
    user_id: UUID,
    limit: int = 50
):
    """
    Liste les révolutions lunaires d'un utilisateur
    
    Args:
        user_id: ID de l'utilisateur
        limit: Nombre maximum de résultats (défaut: 50)
    """
    try:
        logger.info(f"📋 Liste révolutions lunaires pour user {user_id}")
        
        lunar_returns = await list_lunar_returns(user_id, limit)
        
        # Convertir les résultats en LunarReturnResponse
        return [
            LunarReturnResponse(**lr)
            for lr in lunar_returns
        ]
        
    except Exception as e:
        logger.error(f"❌ Erreur liste révolutions: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la récupération des révolutions: {str(e)}"
        )


@router.get("/{lunar_return_id}", response_model=LunarReturnResponse)
async def get_lunar_return(lunar_return_id: UUID):
    """
    Récupère une révolution lunaire par son ID
    
    Args:
        lunar_return_id: ID de la révolution lunaire
    """
    try:
        logger.info(f"🔍 Récupération révolution lunaire {lunar_return_id}")
        
        lunar_return = await get_lunar_return_by_id(lunar_return_id)
        
        if not lunar_return:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Révolution lunaire non trouvée"
            )
        
        return LunarReturnResponse(**lunar_return)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Erreur récupération révolution: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la récupération de la révolution: {str(e)}"
        )

