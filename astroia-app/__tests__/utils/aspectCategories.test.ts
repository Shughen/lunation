/**
 * Tests unitaires pour aspectCategories.ts
 */

import {
  isMajorTense,
  isMajorHarmonious,
  isMinor,
  isPersonalRelated,
  getAspectTypeWeight,
  getIntensityWeight,
  getIntensityRank,
  getAspectTypeRank,
  getFinalAspectSortKey,
  getAspectCategory,
  ORDERED_ASPECT_TYPES,
  ASPECT_TYPE_PRIORITY,
} from '../../lib/utils/aspectCategories';

describe('aspectCategories', () => {
  describe('isMajorTense', () => {
    it('devrait retourner true pour conjunction', () => {
      expect(isMajorTense('conjunction')).toBe(true);
    });

    it('devrait retourner true pour opposition', () => {
      expect(isMajorTense('opposition')).toBe(true);
    });

    it('devrait retourner true pour square', () => {
      expect(isMajorTense('square')).toBe(true);
    });

    it('devrait retourner false pour trine', () => {
      expect(isMajorTense('trine')).toBe(false);
    });

    it('devrait retourner false pour sextile', () => {
      expect(isMajorTense('sextile')).toBe(false);
    });
  });

  describe('isMajorHarmonious', () => {
    it('devrait retourner true pour trine', () => {
      expect(isMajorHarmonious('trine')).toBe(true);
    });

    it('devrait retourner true pour sextile', () => {
      expect(isMajorHarmonious('sextile')).toBe(true);
    });

    it('devrait retourner false pour conjunction', () => {
      expect(isMajorHarmonious('conjunction')).toBe(false);
    });
  });

  describe('isPersonalRelated', () => {
    it('devrait retourner true pour aspect Soleil-Lune', () => {
      expect(isPersonalRelated({ from: 'Sun', to: 'Moon' })).toBe(true);
    });

    it('devrait retourner true pour aspect Mercure-Ascendant', () => {
      expect(isPersonalRelated({ from: 'Mercury', to: 'Ascendant' })).toBe(true);
    });

    it('devrait retourner false pour aspect Neptune-Pluton', () => {
      expect(isPersonalRelated({ from: 'Neptune', to: 'Pluto' })).toBe(false);
    });
  });

  describe('getAspectTypeWeight', () => {
    it('devrait retourner 3000 pour conjunction', () => {
      expect(getAspectTypeWeight('conjunction')).toBe(3000);
    });

    it('devrait retourner 2900 pour opposition', () => {
      expect(getAspectTypeWeight('opposition')).toBe(2900);
    });

    it('devrait retourner 2800 pour square', () => {
      expect(getAspectTypeWeight('square')).toBe(2800);
    });

    it('devrait retourner 2000 pour trine', () => {
      expect(getAspectTypeWeight('trine')).toBe(2000);
    });

    it('devrait retourner 1900 pour sextile', () => {
      expect(getAspectTypeWeight('sextile')).toBe(1900);
    });

    it('devrait retourner 1000 pour quintile (mineur)', () => {
      expect(getAspectTypeWeight('quintile')).toBe(1000);
    });
  });

  describe('getIntensityWeight', () => {
    it('devrait retourner 300 pour strong', () => {
      expect(getIntensityWeight('strong')).toBe(300);
    });

    it('devrait retourner 200 pour medium', () => {
      expect(getIntensityWeight('medium')).toBe(200);
    });

    it('devrait retourner 100 pour weak', () => {
      expect(getIntensityWeight('weak')).toBe(100);
    });
  });

  describe('getFinalAspectSortKey', () => {
    it('devrait trier conjonction forte avant sextile faible', () => {
      const conjunctionStrong = getFinalAspectSortKey({
        aspect_type: 'conjunction',
        strength: 'strong',
        from: 'Sun',
        to: 'Moon',
        orb: 0.5,
      });

      const sextileWeak = getFinalAspectSortKey({
        aspect_type: 'sextile',
        strength: 'weak',
        from: 'Neptune',
        to: 'Pluto',
        orb: 5.0,
      });

      expect(conjunctionStrong).toBeGreaterThan(sextileWeak);
    });

    it('devrait trier opposition forte avant trigone fort (ordre strict des types)', () => {
      const oppositionStrong = getFinalAspectSortKey({
        aspect_type: 'opposition',
        strength: 'strong',
        from: 'Sun',
        to: 'Saturn',
        orb: 1.0,
      });

      const trineStrong = getFinalAspectSortKey({
        aspect_type: 'trine',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 0.5,
      });

      expect(oppositionStrong).toBeGreaterThan(trineStrong);
    });

    it('devrait respecter l\'ordre strict : Conj strong > Opp strong > Carré strong > Trigone strong > Sextile strong', () => {
      const conjunctionStrong = getFinalAspectSortKey({
        aspect_type: 'conjunction',
        strength: 'strong',
        from: 'Sun',
        to: 'Moon',
        orb: 0.5,
      });

      const oppositionStrong = getFinalAspectSortKey({
        aspect_type: 'opposition',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 0.5,
      });

      const squareStrong = getFinalAspectSortKey({
        aspect_type: 'square',
        strength: 'strong',
        from: 'Mercury',
        to: 'Jupiter',
        orb: 0.5,
      });

      const trineStrong = getFinalAspectSortKey({
        aspect_type: 'trine',
        strength: 'strong',
        from: 'Moon',
        to: 'Saturn',
        orb: 0.5,
      });

      const sextileStrong = getFinalAspectSortKey({
        aspect_type: 'sextile',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 0.5,
      });

      // Vérifier l'ordre strict : Conj > Opp > Carré > Trigone > Sextile
      expect(conjunctionStrong).toBeGreaterThan(oppositionStrong);
      expect(oppositionStrong).toBeGreaterThan(squareStrong);
      expect(squareStrong).toBeGreaterThan(trineStrong);
      expect(trineStrong).toBeGreaterThan(sextileStrong);
    });

    it('devrait trier aspect fort avant aspect moyen (même type)', () => {
      const squareStrong = getFinalAspectSortKey({
        aspect_type: 'square',
        strength: 'strong',
        from: 'Moon',
        to: 'Venus',
        orb: 2.0,
      });

      const squareMedium = getFinalAspectSortKey({
        aspect_type: 'square',
        strength: 'medium',
        from: 'Mercury',
        to: 'Jupiter',
        orb: 2.0,
      });

      expect(squareStrong).toBeGreaterThan(squareMedium);
    });

    it('devrait trier sextile fort avant conjonction moyenne (intensité domine)', () => {
      const sextileStrong = getFinalAspectSortKey({
        aspect_type: 'sextile',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 3.0,
      });

      const conjunctionMedium = getFinalAspectSortKey({
        aspect_type: 'conjunction',
        strength: 'medium',
        from: 'Sun',
        to: 'Moon',
        orb: 0.5,
      });

      // L'intensité domine : Fort > Moyen, même si conjonction > sextile
      // Sextile strong (3050000+) > Conjonction medium (2010000+)
      expect(sextileStrong).toBeGreaterThan(conjunctionMedium);
    });

    it('devrait trier trigone fort avant conjonction moyenne (intensité domine)', () => {
      const trineStrong = getFinalAspectSortKey({
        aspect_type: 'trine',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 1.0,
      });

      const conjunctionMedium = getFinalAspectSortKey({
        aspect_type: 'conjunction',
        strength: 'medium',
        from: 'Sun',
        to: 'Moon',
        orb: 0.5,
      });

      // L'intensité domine : Fort > Moyen
      // Trigone strong (3040000+) > Conjonction medium (2010000+)
      expect(trineStrong).toBeGreaterThan(conjunctionMedium);
    });

    it('devrait trier opposition forte avant quintile forte (type domine à intensité égale)', () => {
      const oppositionStrong = getFinalAspectSortKey({
        aspect_type: 'opposition',
        strength: 'strong',
        from: 'Sun',
        to: 'Saturn',
        orb: 2.0,
      });

      const quintileStrong = getFinalAspectSortKey({
        aspect_type: 'quintile',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 0.5,
      });

      // À intensité égale (strong), le type domine : Opposition (rang 2) > Quintile (rang 6)
      // Opposition strong (3020000+) > Quintile strong (3060000+)
      expect(oppositionStrong).toBeGreaterThan(quintileStrong);
    });

    it('devrait trier quintile forte avant conjonction moyenne (intensité domine)', () => {
      const quintileStrong = getFinalAspectSortKey({
        aspect_type: 'quintile',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 0.5,
      });

      const conjunctionMedium = getFinalAspectSortKey({
        aspect_type: 'conjunction',
        strength: 'medium',
        from: 'Sun',
        to: 'Moon',
        orb: 1.0,
      });

      // L'intensité domine absolument : un quintile Fort (intensité 3) passe avant une conjonction Moyen (intensité 2)
      // Quintile strong (3060000+) > Conjonction medium (2010000+)
      // Règle : un aspect mineur Fort peut dépasser un aspect majeur Moyen, mais pas un aspect majeur Fort
      expect(quintileStrong).toBeGreaterThan(conjunctionMedium);
    });

    it('devrait garantir qu\'un quintile fort reste derrière TOUT aspect majeur fort', () => {
      const quintileStrong = getFinalAspectSortKey({
        aspect_type: 'quintile',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 0.5,
      });

      const conjunctionStrong = getFinalAspectSortKey({
        aspect_type: 'conjunction',
        strength: 'strong',
        from: 'Sun',
        to: 'Moon',
        orb: 2.0,
      });

      const oppositionStrong = getFinalAspectSortKey({
        aspect_type: 'opposition',
        strength: 'strong',
        from: 'Sun',
        to: 'Saturn',
        orb: 2.0,
      });

      const squareStrong = getFinalAspectSortKey({
        aspect_type: 'square',
        strength: 'strong',
        from: 'Moon',
        to: 'Venus',
        orb: 2.0,
      });

      const trineStrong = getFinalAspectSortKey({
        aspect_type: 'trine',
        strength: 'strong',
        from: 'Venus',
        to: 'Jupiter',
        orb: 2.0,
      });

      const sextileStrong = getFinalAspectSortKey({
        aspect_type: 'sextile',
        strength: 'strong',
        from: 'Venus',
        to: 'Mars',
        orb: 2.0,
      });

      // Un quintile Fort (rang 6) doit être derrière TOUS les aspects majeurs Fort (rang 1 à 5)
      expect(conjunctionStrong).toBeGreaterThan(quintileStrong);
      expect(oppositionStrong).toBeGreaterThan(quintileStrong);
      expect(squareStrong).toBeGreaterThan(quintileStrong);
      expect(trineStrong).toBeGreaterThan(quintileStrong);
      expect(sextileStrong).toBeGreaterThan(quintileStrong);
    });

    it('devrait trier carré medium avant trigone medium (ordre strict des types à intensité égale)', () => {
      const squareMedium = getFinalAspectSortKey({
        aspect_type: 'square',
        strength: 'medium',
        from: 'Moon',
        to: 'Venus',
        orb: 2.0,
      });

      const trineMedium = getFinalAspectSortKey({
        aspect_type: 'trine',
        strength: 'medium',
        from: 'Venus',
        to: 'Jupiter',
        orb: 1.0,
      });

      // À intensité égale (medium), l'ordre strict des types doit être respecté
      // Carré (rang 3) > Trigone (rang 4)
      expect(squareMedium).toBeGreaterThan(trineMedium);
    });

    it('devrait départager deux trigones strong par baseScore', () => {
      const trineStrongHighScore = getFinalAspectSortKey({
        aspect_type: 'trine',
        strength: 'strong',
        from: 'Sun',      // Big Three
        to: 'Moon',       // Big Three
        orb: 0.5,         // Orbe très serré
      });

      const trineStrongLowScore = getFinalAspectSortKey({
        aspect_type: 'trine',
        strength: 'strong',
        from: 'Neptune',
        to: 'Pluto',
        orb: 5.0,         // Orbe plus large
      });

      // Même intensité (strong) et même type (trine), donc départagés par baseScore
      // Le trigone Soleil-Lune avec orbe 0.5° devrait avoir un meilleur score
      expect(trineStrongHighScore).toBeGreaterThan(trineStrongLowScore);
    });
  });

  describe('getIntensityRank', () => {
    it('devrait retourner 3 pour strong', () => {
      expect(getIntensityRank('strong')).toBe(3);
    });

    it('devrait retourner 2 pour medium', () => {
      expect(getIntensityRank('medium')).toBe(2);
    });

    it('devrait retourner 1 pour weak', () => {
      expect(getIntensityRank('weak')).toBe(1);
    });

    it('devrait retourner 1 pour valeur inconnue (weak par défaut)', () => {
      expect(getIntensityRank('unknown')).toBe(1);
      expect(getIntensityRank(null)).toBe(1);
      expect(getIntensityRank(undefined)).toBe(1);
    });
  });

  describe('ORDERED_ASPECT_TYPES et ASPECT_TYPE_PRIORITY', () => {
    it('devrait définir l\'ordre strict des types d\'aspects', () => {
      expect(ORDERED_ASPECT_TYPES[0]).toBe('conjunction');
      expect(ORDERED_ASPECT_TYPES[1]).toBe('opposition');
      expect(ORDERED_ASPECT_TYPES[2]).toBe('square');
      expect(ORDERED_ASPECT_TYPES[3]).toBe('trine');
      expect(ORDERED_ASPECT_TYPES[4]).toBe('sextile');
    });

    it('devrait créer ASPECT_TYPE_PRIORITY à partir de ORDERED_ASPECT_TYPES', () => {
      expect(ASPECT_TYPE_PRIORITY['conjunction']).toBe(1);
      expect(ASPECT_TYPE_PRIORITY['opposition']).toBe(2);
      expect(ASPECT_TYPE_PRIORITY['square']).toBe(3);
      expect(ASPECT_TYPE_PRIORITY['trine']).toBe(4);
      expect(ASPECT_TYPE_PRIORITY['sextile']).toBe(5);
      expect(ASPECT_TYPE_PRIORITY['other']).toBe(10);
    });
  });

  describe('getAspectTypeRank', () => {
    it('devrait retourner 1 pour conjunction', () => {
      expect(getAspectTypeRank('conjunction')).toBe(1);
    });

    it('devrait retourner 2 pour opposition', () => {
      expect(getAspectTypeRank('opposition')).toBe(2);
    });

    it('devrait retourner 3 pour square', () => {
      expect(getAspectTypeRank('square')).toBe(3);
    });

    it('devrait retourner 4 pour trine', () => {
      expect(getAspectTypeRank('trine')).toBe(4);
    });

    it('devrait retourner 5 pour sextile', () => {
      expect(getAspectTypeRank('sextile')).toBe(5);
    });

    it('devrait retourner 6 pour quintile', () => {
      expect(getAspectTypeRank('quintile')).toBe(6);
    });

    it('devrait retourner 7 pour semi-sextile', () => {
      expect(getAspectTypeRank('semi-sextile')).toBe(7);
    });

    it('devrait retourner 8 pour semi-square', () => {
      expect(getAspectTypeRank('semi-square')).toBe(8);
    });

    it('devrait retourner 9 pour quincunx', () => {
      expect(getAspectTypeRank('quincunx')).toBe(9);
    });

    it('devrait retourner 10 pour type inconnu', () => {
      expect(getAspectTypeRank('unknown-type')).toBe(10);
    });

    it('devrait gérer les variantes (semisextile, sesquiquadrate, etc.)', () => {
      expect(getAspectTypeRank('semisextile')).toBe(7);
      expect(getAspectTypeRank('sesquiquadrate')).toBe(8);
      expect(getAspectTypeRank('inconjunct')).toBe(9);
      expect(getAspectTypeRank('biquintile')).toBe(6);
    });
  });

  describe('getAspectCategory', () => {
    it('devrait retourner major_tense pour conjunction', () => {
      expect(getAspectCategory('conjunction')).toBe('major_tense');
    });

    it('devrait retourner major_harmonious pour trine', () => {
      expect(getAspectCategory('trine')).toBe('major_harmonious');
    });

    it('devrait retourner minor pour quintile', () => {
      expect(getAspectCategory('quintile')).toBe('minor');
    });
  });
});

