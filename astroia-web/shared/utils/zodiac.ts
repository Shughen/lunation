/**
 * Utilitaires astrologiques
 */
import { ZODIAC_SIGNS } from '../constants/zodiac';
import type { ZodiacSign, ZodiacSignId } from '../types/zodiac';

/**
 * Calcule le signe zodiacal depuis une date de naissance
 */
export function getZodiacSign(date: Date): ZodiacSign {
  const month = date.getMonth() + 1; // 1-12
  const day = date.getDate();

  const dateStr = `${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;

  for (const sign of ZODIAC_SIGNS) {
    const { start, end } = sign.dates;

    // Gérer le cas du Capricorne (chevauche l'année)
    if (sign.id === 10) {
      if (dateStr >= start || dateStr <= end) {
        return sign;
      }
    } else {
      if (dateStr >= start && dateStr <= end) {
        return sign;
      }
    }
  }

  // Fallback (ne devrait jamais arriver)
  return ZODIAC_SIGNS[0];
}

/**
 * Retourne un signe zodiacal par son ID
 */
export function getZodiacSignById(id: ZodiacSignId): ZodiacSign | undefined {
  return ZODIAC_SIGNS.find(sign => sign.id === id);
}

/**
 * Retourne un signe zodiacal par son nom
 */
export function getZodiacSignByName(name: string): ZodiacSign | undefined {
  return ZODIAC_SIGNS.find(
    sign => sign.name.toLowerCase() === name.toLowerCase()
  );
}

/**
 * Vérifie si deux signes sont compatibles (même élément ou éléments compatibles)
 */
export function areSignsCompatible(sign1: ZodiacSign, sign2: ZodiacSign): boolean {
  // Même élément = très compatible
  if (sign1.element === sign2.element) {
    return true;
  }

  // Éléments compatibles : Feu+Air, Terre+Eau
  const compatible = [
    ['fire', 'air'],
    ['earth', 'water'],
  ];

  return compatible.some(
    pair =>
      (pair.includes(sign1.element) && pair.includes(sign2.element))
  );
}

/**
 * Calcule la compatibilité élémentaire (0-1)
 */
export function calculateElementCompatibility(
  sign1: ZodiacSign,
  sign2: ZodiacSign
): number {
  if (sign1.element === sign2.element) {
    return 0.9;
  }

  if (areSignsCompatible(sign1, sign2)) {
    return 0.7;
  }

  return 0.4;
}

