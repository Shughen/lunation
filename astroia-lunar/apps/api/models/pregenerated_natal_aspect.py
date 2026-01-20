"""
Modele SQLAlchemy pour pregenerated_natal_aspects
Stocke les interpretations pre-generees des aspects entre planetes natales
"""

from sqlalchemy import Column, String, Integer, Text, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base
import uuid


class PregeneratedNatalAspect(Base):
    """
    Stocke les interpretations astrologiques pre-generees des aspects natals

    Scope: ~225 lignes (45 paires de planetes x 5 types d'aspects)

    Planetes: sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune, pluto
    Aspects: conjunction, opposition, trine, square, sextile

    Gestion symetrie: planet1 < planet2 (ordre alphabetique)
    Ex: (moon, sun) -> car 'm' < 's'
    """
    __tablename__ = "pregenerated_natal_aspects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    planet1 = Column(String(50), nullable=False, index=True)        # Planete 1 (ordre alpha)
    planet2 = Column(String(50), nullable=False, index=True)        # Planete 2 (ordre alpha)
    aspect_type = Column(String(50), nullable=False, index=True)    # conjunction, opposition, trine, square, sextile
    version = Column(Integer, nullable=False, default=2, index=True)
    lang = Column(String(10), nullable=False, default='fr', index=True)
    content = Column(Text, nullable=False)                          # Markdown complet
    length = Column(Integer, nullable=False)                        # Longueur du contenu (pour stats)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        # Contrainte unicite : 1 seule interpretation par (planet1, planet2, aspect_type, version, lang)
        Index(
            'idx_aspect_unique',
            'planet1', 'planet2', 'aspect_type', 'version', 'lang',
            unique=True
        ),
        # Index pour lookup rapide
        Index('idx_aspect_lookup', 'planet1', 'planet2', 'aspect_type', 'version', 'lang'),
        Index('idx_aspect_created_at', 'created_at'),
    )

    def __repr__(self):
        return f"<PregeneratedNatalAspect(planet1={self.planet1}, planet2={self.planet2}, aspect_type={self.aspect_type}, version={self.version}, lang={self.lang})>"
