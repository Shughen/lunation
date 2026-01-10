/**
 * Types liés à l'astrologie
 */

export type ZodiacSignId = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12;

export interface ZodiacSign {
  id: ZodiacSignId;
  name: string;
  emoji: string;
  element: 'fire' | 'earth' | 'air' | 'water';
  quality: 'cardinal' | 'fixed' | 'mutable';
  ruling_planet: string;
  dates: {
    start: string; // Format: "MM-DD"
    end: string;   // Format: "MM-DD"
  };
}

export interface PlanetPosition {
  planet: string;
  sign: string;
  degree: number;
  house?: number;
}

export interface NatalChart {
  sun: PlanetPosition;
  moon: PlanetPosition;
  ascendant: PlanetPosition;
  mercury?: PlanetPosition;
  venus?: PlanetPosition;
  mars?: PlanetPosition;
  jupiter?: PlanetPosition;
  saturn?: PlanetPosition;
}

