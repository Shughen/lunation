/**
 * Tests pour filterMajorAspectsV4
 * Valide les règles v4: types majeurs (+ sextile), orbe variable (8°/10°), exclure Lilith
 */

import { filterMajorAspectsV4 } from '../natalChartUtils';

describe('filterMajorAspectsV4', () => {
  const mockAspects = [
    { planet1: 'sun', planet2: 'moon', type: 'conjunction', orb: 2.5 },      // ✅ v4 (luminaires)
    { planet1: 'mercury', planet2: 'venus', type: 'sextile', orb: 1.0 },     // ✅ v4 (sextile inclus)
    { planet1: 'mars', planet2: 'jupiter', type: 'trine', orb: 4.5 },        // ✅ v4
    { planet1: 'saturn', planet2: 'uranus', type: 'square', orb: 7.0 },      // ✅ v4 (< 8°)
    { planet1: 'neptune', planet2: 'pluto', type: 'opposition', orb: 5.8 },  // ✅ v4
    { planet1: 'mean_lilith', planet2: 'sun', type: 'conjunction', orb: 3.0 }, // ❌ Lilith
    { planet1: 'moon', planet2: 'chiron', type: 'trine', orb: 6.0 },         // ✅ v4 (luminaire, < 10°)
    { planet1: 'venus', planet2: 'mars', type: 'quincunx', orb: 2.0 },       // ❌ quincunx (mineur)
    { planet1: 'sun', planet2: 'neptune', type: 'trine', orb: 9.5 },         // ✅ v4 (luminaire, < 10°)
    { planet1: 'mars', planet2: 'neptune', type: 'trine', orb: 9.5 },        // ❌ (> 8°, pas de luminaire)
    { planet1: 'saturn', planet2: 'uranus', type: 'square', orb: 8.5 },      // ❌ (> 8°)
  ];

  describe('v4 filtering (default)', () => {
    it('devrait retenir les 5 aspects majeurs (conjunction, opposition, square, trine, sextile)', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      const types = filtered.map(a => a.type);
      expect(types.every(t => ['conjunction', 'opposition', 'square', 'trine', 'sextile'].includes(t))).toBe(true);
    });

    it('devrait inclure les sextiles (aspect majeur)', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      expect(filtered.find(a => a.type === 'sextile')).toBeDefined();
    });

    it('devrait exclure les quincunx', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      expect(filtered.find(a => a.type === 'quincunx')).toBeUndefined();
    });

    it('devrait utiliser orbe 10° pour aspects avec Soleil', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      // Sun-Neptune trine (9.5°) doit être inclus (< 10°)
      const sunNeptuneAspect = filtered.find(a =>
        (a.planet1 === 'sun' && a.planet2 === 'neptune') ||
        (a.planet1 === 'neptune' && a.planet2 === 'sun')
      );
      expect(sunNeptuneAspect).toBeDefined();
    });

    it('devrait utiliser orbe 10° pour aspects avec Lune', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      // Moon-Chiron trine (6.0°) doit être inclus (< 10°)
      const moonChironAspect = filtered.find(a =>
        (a.planet1 === 'moon' && a.planet2 === 'chiron') ||
        (a.planet1 === 'chiron' && a.planet2 === 'moon')
      );
      expect(moonChironAspect).toBeDefined();
    });

    it('devrait utiliser orbe 8° pour aspects sans luminaires', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      // Mars-Neptune trine (9.5°) doit être exclu (> 8°, pas de luminaire)
      const marsNeptuneAspect = filtered.find(a =>
        (a.planet1 === 'mars' && a.planet2 === 'neptune') ||
        (a.planet1 === 'neptune' && a.planet2 === 'mars')
      );
      expect(marsNeptuneAspect).toBeUndefined();
    });

    it('devrait exclure Lilith (mean_lilith)', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      const hasLilith = filtered.some(a =>
        a.planet1?.toLowerCase().includes('lilith') ||
        a.planet2?.toLowerCase().includes('lilith')
      );
      expect(hasLilith).toBe(false);
    });

    it('devrait trier par orbe croissant', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      for (let i = 1; i < filtered.length; i++) {
        const prevOrb = Math.abs(filtered[i - 1].orb);
        const currOrb = Math.abs(filtered[i].orb);
        expect(prevOrb).toBeLessThanOrEqual(currOrb);
      }
    });

    it('devrait retourner 7 aspects valides pour le jeu de test', () => {
      // Attendus:
      // - sun-moon conjunction (2.5°, luminaires)
      // - mercury-venus sextile (1.0°, < 8°)
      // - mars-jupiter trine (4.5°, < 8°)
      // - saturn-uranus square (7.0°, < 8°)
      // - neptune-pluto opposition (5.8°, < 8°)
      // - moon-chiron trine (6.0°, luminaire)
      // - sun-neptune trine (9.5°, luminaire < 10°)
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      expect(filtered).toHaveLength(7);
    });
  });

  describe('v2/v3 legacy (conserver tous)', () => {
    it('devrait conserver tous les aspects pour v2', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 2);

      expect(filtered.length).toBe(mockAspects.length);
    });

    it('devrait conserver tous les aspects pour v3', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 3);

      expect(filtered.length).toBe(mockAspects.length);
    });

    it('devrait trier par orbe même en v2', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 2);

      for (let i = 1; i < filtered.length; i++) {
        const prevOrb = Math.abs(filtered[i - 1].orb);
        const currOrb = Math.abs(filtered[i].orb);
        expect(prevOrb).toBeLessThanOrEqual(currOrb);
      }
    });
  });

  describe('edge cases', () => {
    it('devrait gérer aspects vides', () => {
      const filtered = filterMajorAspectsV4([], 4);
      expect(filtered).toEqual([]);
    });

    it('devrait gérer orbe négatif (prendre valeur absolue)', () => {
      const negativeOrb = [
        { planet1: 'sun', planet2: 'moon', type: 'conjunction', orb: -3.5 }
      ];
      const filtered = filterMajorAspectsV4(negativeOrb, 4);

      expect(filtered).toHaveLength(1);
      expect(Math.abs(filtered[0].orb)).toBe(3.5);
    });

    it('devrait exclure Lilith avec variantes (lilith, mean_lilith, blackmoonlilith)', () => {
      const lilithVariants = [
        { planet1: 'lilith', planet2: 'sun', type: 'conjunction', orb: 2.0 },
        { planet1: 'mean_lilith', planet2: 'moon', type: 'trine', orb: 3.0 },
        { planet1: 'blackmoonlilith', planet2: 'venus', type: 'opposition', orb: 4.0 },
        { planet1: 'sun', planet2: 'Black_Moon_Lilith', type: 'square', orb: 5.0 },
      ];

      const filtered = filterMajorAspectsV4(lilithVariants, 4);

      expect(filtered).toHaveLength(0); // Tous exclus
    });
  });
});
