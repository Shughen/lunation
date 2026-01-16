"""Modèle JournalEntry - Entrées journal quotidien liées au cycle lunaire"""

from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    # Données entrée
    date = Column(Date, nullable=False, index=True)  # Date de l'entrée
    mood = Column(String, nullable=True)  # Humeur: calm, excited, anxious, sad, neutral, etc.
    note = Column(Text, nullable=True)  # Texte libre

    # Lien cycle lunaire (format "YYYY-MM")
    month = Column(String, nullable=True, index=True)  # Ex: "2026-01" pour lier à la révolution lunaire

    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relations
    user = relationship("User", back_populates="journal_entries")

    def __repr__(self):
        return f"<JournalEntry user_id={self.user_id} date={self.date}>"
