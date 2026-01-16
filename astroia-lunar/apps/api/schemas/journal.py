"""Schemas Pydantic pour JournalEntry"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date as Date, datetime


# === INPUT SCHEMAS ===

class JournalEntryCreate(BaseModel):
    """Schema pour créer une entrée de journal"""
    date: Date = Field(..., description="Date de l'entrée (YYYY-MM-DD)")
    mood: Optional[str] = Field(None, description="Humeur: calm, excited, anxious, sad, neutral, etc.")
    note: Optional[str] = Field(None, description="Note libre de l'utilisateur")
    month: Optional[str] = Field(None, description="Mois lunaire associé (format YYYY-MM)")


class JournalEntryUpdate(BaseModel):
    """Schema pour mettre à jour une entrée de journal"""
    mood: Optional[str] = Field(None, description="Humeur")
    note: Optional[str] = Field(None, description="Note")


# === OUTPUT SCHEMAS ===

class JournalEntryResponse(BaseModel):
    """Schema de réponse pour une entrée de journal"""
    id: int
    user_id: int
    date: Date
    mood: Optional[str] = None
    note: Optional[str] = None
    month: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class JournalEntriesListResponse(BaseModel):
    """Schema de réponse pour une liste d'entrées"""
    entries: List[JournalEntryResponse]
    total: int
    month: Optional[str] = None
