export interface LocationResult {
  display_name: string;
  lat: string;
  lon: string;
  [key: string]: any;
}

/**
 * Normalise un nom de lieu pour la comparaison
 * - Lowercase
 * - Retire les accents
 * - Garde seulement les 2 premiers segments (ville, région)
 */
export function normalizeLocationName(displayName: string): string {
  return displayName
    .split(',')
    .map(s => s.trim())
    .slice(0, 2)
    .join(',')
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, ''); // Retire diacritiques
}

/**
 * Déduplique les résultats Nominatim par nom normalisé
 * Limite à 5 résultats max
 */
export function deduplicateLocations<T extends LocationResult>(
  results: T[]
): T[] {
  const seen = new Map<string, T>();

  for (const result of results) {
    const key = normalizeLocationName(result.display_name);

    if (!seen.has(key)) {
      seen.set(key, result);
    }
  }

  return Array.from(seen.values()).slice(0, 5);
}
