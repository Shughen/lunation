"""Routes pour les entrées de journal quotidien"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, func, extract
from typing import Optional
from datetime import date, datetime
import logging

from database import get_db
from models.user import User
from models.journal_entry import JournalEntry
from schemas.journal import (
    JournalEntryCreate,
    JournalEntryUpdate,
    JournalEntryResponse,
    JournalEntriesListResponse
)
from routes.auth import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/entry", response_model=JournalEntryResponse, status_code=status.HTTP_201_CREATED)
async def create_journal_entry(
    entry_data: JournalEntryCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Crée une nouvelle entrée de journal.

    - Lie automatiquement l'entrée au cycle lunaire actif si month fourni
    - Une seule entrée par jour par utilisateur
    - Si une entrée existe déjà pour la date, elle est mise à jour
    """
    try:
        # Vérifier si une entrée existe déjà pour cette date
        stmt = select(JournalEntry).where(
            and_(
                JournalEntry.user_id == current_user.id,
                JournalEntry.date == entry_data.date
            )
        )
        result = await db.execute(stmt)
        existing_entry = result.scalar_one_or_none()

        if existing_entry:
            # Mettre à jour l'entrée existante
            existing_entry.mood = entry_data.mood
            existing_entry.note = entry_data.note
            if entry_data.month:
                existing_entry.month = entry_data.month
            existing_entry.updated_at = datetime.utcnow()
            await db.commit()
            await db.refresh(existing_entry)
            logger.info(f"✅ Journal entry updated: user_id={current_user.id}, date={entry_data.date}")
            return existing_entry
        else:
            # Créer une nouvelle entrée
            new_entry = JournalEntry(
                user_id=current_user.id,
                date=entry_data.date,
                mood=entry_data.mood,
                note=entry_data.note,
                month=entry_data.month
            )
            db.add(new_entry)
            await db.commit()
            await db.refresh(new_entry)
            logger.info(f"✅ Journal entry created: user_id={current_user.id}, date={entry_data.date}")
            return new_entry

    except Exception as e:
        logger.error(f"❌ Error creating journal entry: {e}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la création de l'entrée: {str(e)}"
        )


@router.get("/entries", response_model=JournalEntriesListResponse)
async def get_journal_entries(
    month: Optional[str] = None,
    year: Optional[int] = None,
    limit: int = 100,
    offset: int = 0,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Récupère les entrées de journal de l'utilisateur.

    - Filtrage optionnel par mois lunaire (format YYYY-MM)
    - Filtrage optionnel par année
    - Pagination avec limit/offset
    - Tri par date décroissante (plus récent en premier)
    """
    try:
        # Base query
        conditions = [JournalEntry.user_id == current_user.id]

        # Filtrer par mois lunaire
        if month:
            conditions.append(JournalEntry.month == month)

        # Filtrer par année
        if year:
            conditions.append(extract('year', JournalEntry.date) == year)

        # Requête pour compter le total
        count_stmt = select(func.count(JournalEntry.id)).where(and_(*conditions))
        total_result = await db.execute(count_stmt)
        total = total_result.scalar()

        # Requête pour récupérer les entrées
        stmt = (
            select(JournalEntry)
            .where(and_(*conditions))
            .order_by(JournalEntry.date.desc())
            .limit(limit)
            .offset(offset)
        )
        result = await db.execute(stmt)
        entries = result.scalars().all()

        logger.info(f"✅ Retrieved {len(entries)}/{total} journal entries for user_id={current_user.id}")

        return JournalEntriesListResponse(
            entries=entries,
            total=total,
            month=month
        )

    except Exception as e:
        logger.error(f"❌ Error fetching journal entries: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la récupération des entrées: {str(e)}"
        )


@router.get("/today", response_model=Optional[JournalEntryResponse])
async def get_today_entry(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Récupère l'entrée de journal du jour (si elle existe).

    - Retourne None si aucune entrée pour aujourd'hui
    - Utile pour afficher le widget Home
    """
    try:
        today = date.today()

        stmt = select(JournalEntry).where(
            and_(
                JournalEntry.user_id == current_user.id,
                JournalEntry.date == today
            )
        )
        result = await db.execute(stmt)
        entry = result.scalar_one_or_none()

        if entry:
            logger.info(f"✅ Found today's journal entry for user_id={current_user.id}")
            return entry
        else:
            logger.info(f"ℹ️  No journal entry for today for user_id={current_user.id}")
            return None

    except Exception as e:
        logger.error(f"❌ Error fetching today's entry: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la récupération de l'entrée du jour: {str(e)}"
        )


@router.delete("/entry/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_journal_entry(
    entry_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Supprime une entrée de journal.

    - Seul le propriétaire peut supprimer son entrée
    """
    try:
        stmt = select(JournalEntry).where(
            and_(
                JournalEntry.id == entry_id,
                JournalEntry.user_id == current_user.id
            )
        )
        result = await db.execute(stmt)
        entry = result.scalar_one_or_none()

        if not entry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entrée non trouvée"
            )

        await db.delete(entry)
        await db.commit()
        logger.info(f"✅ Journal entry deleted: id={entry_id}, user_id={current_user.id}")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error deleting journal entry: {e}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la suppression: {str(e)}"
        )
