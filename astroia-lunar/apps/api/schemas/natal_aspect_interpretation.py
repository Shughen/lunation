"""
Schemas Pydantic pour les interpretations d'aspects natals
"""

from pydantic import BaseModel, Field
from typing import Literal


# Planetes supportees pour les aspects
AspectPlanet = Literal[
    'sun', 'moon', 'mercury', 'venus', 'mars',
    'jupiter', 'saturn', 'uranus', 'neptune', 'pluto'
]

# Types d'aspects supportes
AspectType = Literal[
    'conjunction', 'opposition', 'trine', 'square', 'sextile'
]


class NatalAspectInterpretationRequest(BaseModel):
    """Request pour obtenir une interpretation d'aspect natal"""
    planet1: AspectPlanet = Field(..., description="Premiere planete")
    planet2: AspectPlanet = Field(..., description="Deuxieme planete")
    aspect_type: AspectType = Field(..., description="Type d'aspect")
    lang: str = Field(default='fr', description="Langue de l'interpretation")


class NatalAspectInterpretationResponse(BaseModel):
    """Response contenant l'interpretation d'aspect"""
    planet1: str = Field(..., description="Premiere planete (ordre alphabetique)")
    planet2: str = Field(..., description="Deuxieme planete (ordre alphabetique)")
    aspect_type: str = Field(..., description="Type d'aspect")
    text: str = Field(..., description="Texte de l'interpretation (markdown)")
    source: str = Field(..., description="Source: 'pregenerated' ou 'placeholder'")
    version: int = Field(default=2, description="Version du contenu")

    class Config:
        from_attributes = True
