/**
 * Constantes zodiacales
 */
import type { ZodiacSign } from '../types/zodiac';

export const ZODIAC_SIGNS: readonly ZodiacSign[] = [
  {
    id: 1,
    name: 'Bélier',
    emoji: '♈',
    element: 'fire',
    quality: 'cardinal',
    ruling_planet: 'Mars',
    dates: { start: '03-21', end: '04-19' },
  },
  {
    id: 2,
    name: 'Taureau',
    emoji: '♉',
    element: 'earth',
    quality: 'fixed',
    ruling_planet: 'Vénus',
    dates: { start: '04-20', end: '05-20' },
  },
  {
    id: 3,
    name: 'Gémeaux',
    emoji: '♊',
    element: 'air',
    quality: 'mutable',
    ruling_planet: 'Mercure',
    dates: { start: '05-21', end: '06-20' },
  },
  {
    id: 4,
    name: 'Cancer',
    emoji: '♋',
    element: 'water',
    quality: 'cardinal',
    ruling_planet: 'Lune',
    dates: { start: '06-21', end: '07-22' },
  },
  {
    id: 5,
    name: 'Lion',
    emoji: '♌',
    element: 'fire',
    quality: 'fixed',
    ruling_planet: 'Soleil',
    dates: { start: '07-23', end: '08-22' },
  },
  {
    id: 6,
    name: 'Vierge',
    emoji: '♍',
    element: 'earth',
    quality: 'mutable',
    ruling_planet: 'Mercure',
    dates: { start: '08-23', end: '09-22' },
  },
  {
    id: 7,
    name: 'Balance',
    emoji: '♎',
    element: 'air',
    quality: 'cardinal',
    ruling_planet: 'Vénus',
    dates: { start: '09-23', end: '10-22' },
  },
  {
    id: 8,
    name: 'Scorpion',
    emoji: '♏',
    element: 'water',
    quality: 'fixed',
    ruling_planet: 'Pluton',
    dates: { start: '10-23', end: '11-21' },
  },
  {
    id: 9,
    name: 'Sagittaire',
    emoji: '♐',
    element: 'fire',
    quality: 'mutable',
    ruling_planet: 'Jupiter',
    dates: { start: '11-22', end: '12-21' },
  },
  {
    id: 10,
    name: 'Capricorne',
    emoji: '♑',
    element: 'earth',
    quality: 'cardinal',
    ruling_planet: 'Saturne',
    dates: { start: '12-22', end: '01-19' },
  },
  {
    id: 11,
    name: 'Verseau',
    emoji: '♒',
    element: 'air',
    quality: 'fixed',
    ruling_planet: 'Uranus',
    dates: { start: '01-20', end: '02-18' },
  },
  {
    id: 12,
    name: 'Poissons',
    emoji: '♓',
    element: 'water',
    quality: 'mutable',
    ruling_planet: 'Neptune',
    dates: { start: '02-19', end: '03-20' },
  },
] as const;

export const ELEMENTS = {
  FIRE: ['Bélier', 'Lion', 'Sagittaire'],
  EARTH: ['Taureau', 'Vierge', 'Capricorne'],
  AIR: ['Gémeaux', 'Balance', 'Verseau'],
  WATER: ['Cancer', 'Scorpion', 'Poissons'],
} as const;

export const QUALITIES = {
  CARDINAL: ['Bélier', 'Cancer', 'Balance', 'Capricorne'],
  FIXED: ['Taureau', 'Lion', 'Scorpion', 'Verseau'],
  MUTABLE: ['Gémeaux', 'Vierge', 'Sagittaire', 'Poissons'],
} as const;

