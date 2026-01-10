/**
 * Tests unitaires pour aspectTextTemplates.ts
 */

import { getReadableInterpretation } from '../../lib/utils/aspectTextTemplates';

describe('aspectTextTemplates', () => {
  describe('getReadableInterpretation', () => {
    it('devrait générer une interprétation pour conjunction', () => {
      const aspect = {
        from: 'Sun',
        to: 'Moon',
        aspect_type: 'conjunction',
        strength: 'strong',
        orb: 0.5,
      };

      const interpretation = getReadableInterpretation(aspect);
      expect(interpretation).toBeTruthy();
      expect(interpretation).toContain('Soleil');
      expect(interpretation).toContain('Lune');
      expect(interpretation).toContain('fusionnent');
    });

    it('devrait générer une interprétation pour opposition', () => {
      const aspect = {
        from: 'Venus',
        to: 'Mars',
        aspect_type: 'opposition',
        strength: 'medium',
        orb: 2.0,
      };

      const interpretation = getReadableInterpretation(aspect);
      expect(interpretation).toBeTruthy();
      expect(interpretation).toContain('tension');
    });

    it('devrait générer une interprétation pour square', () => {
      const aspect = {
        from: 'Mercury',
        to: 'Jupiter',
        aspect_type: 'square',
        strength: 'strong',
        orb: 1.5,
      };

      const interpretation = getReadableInterpretation(aspect);
      expect(interpretation).toBeTruthy();
      expect(interpretation).toContain('friction');
    });

    it('devrait générer une interprétation pour trine', () => {
      const aspect = {
        from: 'Sun',
        to: 'Jupiter',
        aspect_type: 'trine',
        strength: 'medium',
        orb: 3.0,
      };

      const interpretation = getReadableInterpretation(aspect);
      expect(interpretation).toBeTruthy();
      expect(interpretation).toContain('synergie');
    });

    it('devrait générer une interprétation pour sextile', () => {
      const aspect = {
        from: 'Venus',
        to: 'Mars',
        aspect_type: 'sextile',
        strength: 'weak',
        orb: 4.0,
      };

      const interpretation = getReadableInterpretation(aspect);
      expect(interpretation).toBeTruthy();
      expect(interpretation).toContain('opportunité');
    });

    it('devrait générer une interprétation pour aspect mineur', () => {
      const aspect = {
        from: 'Neptune',
        to: 'Pluto',
        aspect_type: 'quintile',
        strength: 'medium',
        orb: 2.5,
      };

      const interpretation = getReadableInterpretation(aspect);
      expect(interpretation).toBeTruthy();
      expect(interpretation).toContain('lien discret');
    });

    it('devrait retourner un texte en français lisible', () => {
      const aspect = {
        from: 'Sun',
        to: 'Moon',
        aspect_type: 'conjunction',
        strength: 'strong',
        orb: 0.5,
      };

      const interpretation = getReadableInterpretation(aspect);
      
      // Vérifier qu'il n'y a pas de tokens non remplacés
      expect(interpretation).not.toContain('{A}');
      expect(interpretation).not.toContain('{B}');
      expect(interpretation).not.toContain('{planetA}');
      
      // Vérifier que c'est une phrase complète
      expect(interpretation.length).toBeGreaterThan(20);
    });
  });
});

