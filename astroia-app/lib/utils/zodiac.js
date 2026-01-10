/**
 * Helpers pour gérer les signes du zodiaque
 * Toutes les chaînes avec accents sont encodées en ASCII via \uXXXX pour éviter les soucis d'encodage.
 */

const ZODIAC_SIGNS = [
  {
    id: 1,
    name: 'B\u00e9lier',
    emoji: '♈',
    element: 'Feu',
    start: { month: 3, day: 21 },
    end: { month: 4, day: 19 },
  },
  {
    id: 2,
    name: 'Taureau',
    emoji: '♉',
    element: 'Terre',
    start: { month: 4, day: 20 },
    end: { month: 5, day: 20 },
  },
  {
    id: 3,
    name: 'G\u00e9meaux',
    emoji: '♊',
    element: 'Air',
    start: { month: 5, day: 21 },
    end: { month: 6, day: 20 },
  },
  {
    id: 4,
    name: 'Cancer',
    emoji: '♋',
    element: 'Eau',
    start: { month: 6, day: 21 },
    end: { month: 7, day: 22 },
  },
  {
    id: 5,
    name: 'Lion',
    emoji: '♌',
    element: 'Feu',
    start: { month: 7, day: 23 },
    end: { month: 8, day: 22 },
  },
  {
    id: 6,
    name: 'Vierge',
    emoji: '♍',
    element: 'Terre',
    start: { month: 8, day: 23 },
    end: { month: 9, day: 22 },
  },
  {
    id: 7,
    name: 'Balance',
    emoji: '♎',
    element: 'Air',
    start: { month: 9, day: 23 },
    end: { month: 10, day: 22 },
  },
  {
    id: 8,
    name: 'Scorpion',
    emoji: '♏',
    element: 'Eau',
    start: { month: 10, day: 23 },
    end: { month: 11, day: 21 },
  },
  {
    id: 9,
    name: 'Sagittaire',
    emoji: '♐',
    element: 'Feu',
    start: { month: 11, day: 22 },
    end: { month: 12, day: 21 },
  },
  {
    id: 10,
    name: 'Capricorne',
    emoji: '♑',
    element: 'Terre',
    start: { month: 12, day: 22 },
    end: { month: 1, day: 19 },
  },
  {
    id: 11,
    name: 'Verseau',
    emoji: '♒',
    element: 'Air',
    start: { month: 1, day: 20 },
    end: { month: 2, day: 18 },
  },
  {
    id: 12,
    name: 'Poissons',
    emoji: '♓',
    element: 'Eau',
    start: { month: 2, day: 19 },
    end: { month: 3, day: 20 },
  },
];

/**
 * Détermine si une date MM/DD est comprise dans la plage d'un signe
 */
function isDateInRange(month, day, start, end) {
  if (start.month === end.month && start.day === end.day) {
    return month === start.month && day === start.day;
  }

  if (start.month < end.month || (start.month === end.month && start.day <= end.day)) {
    // Plage classique sans chevauchement d'année
    if (month < start.month || month > end.month) return false;
    if (month === start.month && day < start.day) return false;
    if (month === end.month && day > end.day) return false;
    return true;
  }

  // Plage qui chevauche l'année (ex: Capricorne)
  return (
    (month === start.month && day >= start.day) ||
    month > start.month ||
    month < end.month ||
    (month === end.month && day <= end.day)
  );
}

/**
 * Retourne l'objet signe à partir d'un ID
 */
export function getSignById(id) {
  if (!id) return null;
  return ZODIAC_SIGNS.find((sign) => sign.id === Number(id)) || null;
}

/**
 * Retourne l'ID d'un signe à partir de son nom
 */
export function getSignId(name) {
  if (!name) return null;
  const normalized = name.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  const match = ZODIAC_SIGNS.find(
    (sign) => sign.name.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase() === normalized.toLowerCase()
  );
  return match ? match.id : null;
}

/**
 * Calcule le signe solaire à partir d'une date
 */
export function calculateZodiacFromDate(dateLike) {
  if (!dateLike) return null;
  const date = new Date(dateLike);
  if (Number.isNaN(date.getTime())) {
    return null;
  }

  const month = date.getMonth() + 1; // 1-12
  const day = date.getDate();

  const sign = ZODIAC_SIGNS.find((candidate) =>
    isDateInRange(month, day, candidate.start, candidate.end)
  );

  return sign || null;
}

export { ZODIAC_SIGNS };


