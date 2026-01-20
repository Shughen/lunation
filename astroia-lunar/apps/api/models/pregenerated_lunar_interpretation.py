"""
Modèle SQLAlchemy pour pregenerated_lunar_interpretations
Stocke les interprétations IA pré-générées pour les révolutions lunaires
"""

from sqlalchemy import Column, String, Integer, Text, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base
import uuid


class PregeneratedLunarInterpretation(Base):
    """
    Cache pour les interprétations IA des révolutions lunaires

    Clé composite: (moon_sign, moon_house, lunar_ascendant, version, lang)

    Structure:
    - interpretation_full: texte structuré (tonalité, ressources, défis, dynamiques)
    - weekly_advice: JSONB avec conseils par semaine (week_1 à week_4)

    Scope: ~1728 combinaisons max (12 signes × 12 maisons × 12 ascendants)
    Note: En pratique, on génère à la demande et cache.
    """
    __tablename__ = "pregenerated_lunar_interpretations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    moon_sign = Column(String(50), nullable=False, index=True)        # Aries, Taurus, etc.
    moon_house = Column(Integer, nullable=False, index=True)          # 1-12
    lunar_ascendant = Column(String(50), nullable=False, index=True)  # Aries, Taurus, etc.
    version = Column(Integer, nullable=False, default=1, index=True)  # Version du prompt
    lang = Column(String(10), nullable=False, default='fr', index=True)  # fr, en, etc.

    # Interprétation enrichie IA
    interpretation_full = Column(Text, nullable=False)  # Texte structuré complet

    # Conseils hebdomadaires (JSONB)
    # Structure: {
    #   "week_1": {"dates": "...", "theme": "...", "conseil": "...", "focus": "..."},
    #   "week_2": {...}, "week_3": {...}, "week_4": {...}
    # }
    weekly_advice = Column(JSONB, nullable=True)

    # Métadonnées
    length = Column(Integer, nullable=False)  # Longueur interpretation_full
    model_used = Column(String(50), nullable=True)  # sonnet, haiku, etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        # Contrainte unicité : 1 seule interprétation par combinaison
        Index(
            'idx_lunar_interp_unique',
            'moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang',
            unique=True
        ),
        # Index pour lookup rapide
        Index('idx_lunar_interp_lookup', 'moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'),
        Index('idx_lunar_interp_created_at', 'created_at'),
    )

    def __repr__(self):
        return (
            f"<PregeneratedLunarInterpretation("
            f"moon_sign={self.moon_sign}, moon_house={self.moon_house}, "
            f"lunar_ascendant={self.lunar_ascendant}, version={self.version}, lang={self.lang})>"
        )
