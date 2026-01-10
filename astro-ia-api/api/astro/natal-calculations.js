// ============================================
// FONCTIONS DE CALCUL ASTRONOMIQUE
// ============================================
// Formules VSOP87, ELP2000, Jean Meeus

const ZODIAC_SIGNS = [
  { name: 'Bélier', emoji: '♈', start: 0, element: 'Feu' },
  { name: 'Taureau', emoji: '♉', start: 30, element: 'Terre' },
  { name: 'Gémeaux', emoji: '♊', start: 60, element: 'Air' },
  { name: 'Cancer', emoji: '♋', start: 90, element: 'Eau' },
  { name: 'Lion', emoji: '♌', start: 120, element: 'Feu' },
  { name: 'Vierge', emoji: '♍', start: 150, element: 'Terre' },
  { name: 'Balance', emoji: '♎', start: 180, element: 'Air' },
  { name: 'Scorpion', emoji: '♏', start: 210, element: 'Eau' },
  { name: 'Sagittaire', emoji: '♐', start: 240, element: 'Feu' },
  { name: 'Capricorne', emoji: '♑', start: 270, element: 'Terre' },
  { name: 'Verseau', emoji: '♒', start: 300, element: 'Air' },
  { name: 'Poissons', emoji: '♓', start: 330, element: 'Eau' },
];

/**
 * Convertir une longitude écliptique en signe zodiacal
 */
function longitudeToZodiac(longitude) {
  let lon = longitude % 360;
  if (lon < 0) lon += 360;

  for (let i = 0; i < ZODIAC_SIGNS.length; i++) {
    const sign = ZODIAC_SIGNS[i];
    const nextStart = i === 11 ? 360 : ZODIAC_SIGNS[i + 1].start;
    
    if (lon >= sign.start && lon < nextStart) {
      const degree = Math.floor(lon - sign.start);
      const minutes = Math.floor((lon - sign.start - degree) * 60);
      
      return {
        sign: sign.name,
        emoji: sign.emoji,
        element: sign.element,
        degree,
        minutes,
        longitude: lon,
      };
    }
  }

  return ZODIAC_SIGNS[0];
}

/**
 * Date vers Jour Julien
 */
function dateToJulianDay(year, month, day, hour, minute) {
  const a = Math.floor((14 - month) / 12);
  const y = year + 4800 - a;
  const m = month + 12 * a - 3;
  
  let jd = day + Math.floor((153 * m + 2) / 5) + 365 * y + Math.floor(y / 4) - Math.floor(y / 100) + Math.floor(y / 400) - 32045;
  jd = jd + (hour - 12) / 24 + minute / 1440;
  
  return jd;
}

/**
 * Calculer la position du Soleil (VSOP87 simplifié - précision ~1')
 */
function calculateSunPosition(jd) {
  const T = (jd - 2451545.0) / 36525.0;
  
  // Longitude moyenne du Soleil
  const L0 = 280.46646 + 36000.76983 * T + 0.0003032 * T * T;
  
  // Anomalie moyenne
  const M = 357.52911 + 35999.05029 * T - 0.0001537 * T * T;
  const MRad = M * Math.PI / 180;
  
  // Équation du centre
  const C = (1.914602 - 0.004817 * T - 0.000014 * T * T) * Math.sin(MRad);
  const C2 = (0.019993 - 0.000101 * T) * Math.sin(2 * MRad);
  const C3 = 0.000289 * Math.sin(3 * MRad);
  
  // Longitude vraie
  let sunLon = (L0 + C + C2 + C3) % 360;
  
  return sunLon < 0 ? sunLon + 360 : sunLon;
}

/**
 * Calculer la position de la Lune (ELP2000 simplifié - précision ~10')
 */
function calculateMoonPosition(jd) {
  const T = (jd - 2451545.0) / 36525.0;
  
  // Longitude moyenne de la Lune
  const Lm = 218.3164477 + 481267.88123421 * T - 0.0015786 * T * T;
  
  // Anomalie moyenne de la Lune
  const Mm = 134.9633964 + 477198.8675055 * T + 0.0087414 * T * T;
  const MmRad = Mm * Math.PI / 180;
  
  // Anomalie moyenne du Soleil
  const Ms = 357.5291092 + 35999.0502909 * T - 0.0001536 * T * T;
  const MsRad = Ms * Math.PI / 180;
  
  // Argument de la latitude
  const F = 93.272095 + 483202.0175233 * T - 0.0036539 * T * T;
  const FRad = F * Math.PI / 180;
  
  // Distance Lune-Soleil
  const D = 297.8501921 + 445267.1114034 * T - 0.0018819 * T * T;
  const DRad = D * Math.PI / 180;
  
  // Termes principaux de la longitude (ELP2000 simplifié)
  let moonLon = Lm;
  moonLon += 6.288774 * Math.sin(MmRad);                    // Terme principal
  moonLon += 1.274027 * Math.sin(2 * DRad - MmRad);         // Evection
  moonLon += 0.658314 * Math.sin(2 * DRad);                 // Variation
  moonLon += 0.213618 * Math.sin(2 * MmRad);                // Équation annuelle
  moonLon -= 0.185116 * Math.sin(MsRad);                    // Perturbation solaire
  moonLon -= 0.114332 * Math.sin(2 * FRad);                 // Réduction à l'écliptique
  
  moonLon = moonLon % 360;
  return moonLon < 0 ? moonLon + 360 : moonLon;
}

/**
 * Calculer l'obliquité de l'écliptique
 */
function calculateObliquity(jd) {
  const T = (jd - 2451545.0) / 36525.0;
  // Formule IAU 2000B
  const epsilon = 23.439291 - 0.0130042 * T - 0.00000016 * T * T + 0.000000504 * T * T * T;
  return epsilon;
}

/**
 * Calculer l'ascendant (formule de Jean Meeus - précision ~1°)
 */
function calculateAscendant(jd, lat, lon) {
  // Calcul du Temps Sidéral Local (LST)
  const T = (jd - 2451545.0) / 36525.0;
  
  // GMST à 0h UT
  let GMST0 = 280.46061837 + 360.98564736629 * (jd - 2451545.0);
  GMST0 = GMST0 + 0.000387933 * T * T - T * T * T / 38710000.0;
  
  // Convertir en LST (ajout longitude)
  let LST = (GMST0 + lon) % 360;
  if (LST < 0) LST += 360;
  
  // Obliquité de l'écliptique
  const epsilon = calculateObliquity(jd);
  const epsilonRad = epsilon * Math.PI / 180;
  
  // Latitude en radians
  const latRad = lat * Math.PI / 180;
  const lstRad = LST * Math.PI / 180;
  
  // Formule de Jean Meeus pour l'ascendant
  // tan(Asc) = cos(LST) / (sin(LST) * cos(ε) - tan(φ) * sin(ε))
  const numerator = Math.cos(lstRad);
  const denominator = Math.sin(lstRad) * Math.cos(epsilonRad) - Math.tan(latRad) * Math.sin(epsilonRad);
  
  let asc = Math.atan2(numerator, denominator) * 180 / Math.PI;
  
  // Normaliser entre 0 et 360
  if (asc < 0) asc += 360;
  
  return asc;
}

export {
  ZODIAC_SIGNS,
  longitudeToZodiac,
  dateToJulianDay,
  calculateSunPosition,
  calculateMoonPosition,
  calculateObliquity,
  calculateAscendant,
};

