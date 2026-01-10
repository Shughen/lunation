/**
 * Service de calcul de révolution lunaire
 * Calcule la position de la Lune au moment de la révolution lunaire mensuelle
 * et les aspects avec les planètes natales
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { getFinalAspectSortKey } from '@/lib/utils/aspectCategories';
import { getLocalReading } from './natalReadingService';
import { generateAspectInterpretation } from '@/lib/utils/aspectInterpretations';

// Configuration - Utiliser l'IP locale pour mobile (même que natalReadingService)
const FASTAPI_BASE_URL = 'http://192.168.0.150:8000';

export interface LunarRevolution {
  month: string; // Format YYYY-MM
  revolutionDate: string; // ISO date
  moonSign: string; // Nom du signe en français
  moonSignEmoji: string;
  moonDegree: number;
  house: number; // Maison activée (1-12)
  phase: 'new' | 'waxing' | 'full' | 'waning';
  phaseName: string; // Nom en français
  aspects: LunarAspect[];
  interpretationSummary?: string;
  focus?: string; // Domaines activés
}

export interface LunarAspect {
  from: string; // Toujours "Moon" pour révolution lunaire
  to: string; // Planète natale
  aspect_type: string; // conjunction, opposition, trine, square, sextile, etc.
  strength: 'strong' | 'medium' | 'weak';
  orb: number;
  interpretation?: string;
}

export interface BirthData {
  year: number;
  month: number;
  day: number;
  hour: number;
  minute: number;
  second?: number;
  city: string;
  country_code?: string;
  latitude: number;
  longitude: number;
  timezone?: string;
}

/**
 * Calcule la date approximative de révolution lunaire pour un mois donné
 * La révolution lunaire = moment où la Lune revient à sa position natale
 * Cycle lunaire = ~27.3 jours
 */
export function calculateRevolutionDate(birthDate: Date, targetMonth: Date): Date {
  // Calculer le nombre de jours depuis la naissance
  const daysSinceBirth = Math.floor((targetMonth.getTime() - birthDate.getTime()) / (1000 * 60 * 60 * 24));
  
  // Cycle lunaire = 27.32166 jours
  const lunarCycle = 27.32166;
  
  // Calculer le nombre de révolutions complètes
  const revolutions = Math.floor(daysSinceBirth / lunarCycle);
  
  // Date de la révolution la plus proche dans le mois cible
  const revolutionDate = new Date(birthDate);
  revolutionDate.setDate(revolutionDate.getDate() + revolutions * lunarCycle);
  
  // Ajuster pour être dans le mois cible
  while (revolutionDate.getMonth() !== targetMonth.getMonth() || 
         revolutionDate.getFullYear() !== targetMonth.getFullYear()) {
    if (revolutionDate < targetMonth) {
      revolutionDate.setDate(revolutionDate.getDate() + lunarCycle);
    } else {
      revolutionDate.setDate(revolutionDate.getDate() - lunarCycle);
    }
  }
  
  return revolutionDate;
}

/**
 * Récupère ou calcule la révolution lunaire pour un mois donné
 * @param birthData - Données de naissance
 * @param targetMonth - Mois cible (Date, sera normalisé au 1er du mois)
 * @param options - Options (force_refresh, use_api)
 */
export async function getLunarRevolution(
  birthData: BirthData,
  targetMonth: Date,
  options: { force_refresh?: boolean; use_api?: boolean } = {}
): Promise<LunarRevolution> {
  const monthKey = `${targetMonth.getFullYear()}-${String(targetMonth.getMonth() + 1).padStart(2, '0')}`;
  
  // Calculer la date de naissance
  const birthDate = new Date(
    birthData.year,
    birthData.month - 1,
    birthData.day,
    birthData.hour,
    birthData.minute,
    birthData.second || 0
  );

  // Vérifier que la date cible n'est pas trop ancienne
  // Limite minimale : date de naissance ou 2020-01-01, selon la plus récente
  const minDate = new Date(Math.max(birthDate.getTime(), new Date('2020-01-01').getTime()));
  
  if (targetMonth < minDate) {
    const minYear = minDate.getFullYear();
    const minMonth = minDate.getMonth() + 1;
    throw new Error(`Impossible de remonter aussi loin. La date la plus ancienne disponible est ${minMonth}/${minYear}.`);
  }

  // Vérifier que la date cible n'est pas avant la date de naissance
  if (targetMonth < birthDate) {
    throw new Error(`Impossible de calculer une révolution lunaire avant ta date de naissance (${birthData.day}/${birthData.month}/${birthData.year}).`);
  }
  
  // Vérifier le cache local
  if (!options.force_refresh) {
    const cached = await getCachedRevolution(monthKey);
    if (cached) {
      console.log('[LunarRevolution] ✅ Récupéré depuis cache:', monthKey);
      return cached;
    }
  }

  const revolutionDate = calculateRevolutionDate(birthDate, targetMonth);

  // Essayer d'utiliser l'API si disponible
  if (options.use_api !== false) {
    try {
      const apiResult = await fetchLunarRevolutionFromAPI(birthData, revolutionDate);
      if (apiResult) {
        await cacheRevolution(monthKey, apiResult);
        return apiResult;
      }
    } catch (error) {
      console.warn('[LunarRevolution] API non disponible, utilisation calcul basique:', error);
    }
  }

  // Fallback : calcul basique
  const basicResult = await calculateBasicLunarRevolution(birthData, revolutionDate, monthKey);
  await cacheRevolution(monthKey, basicResult);
  
  return basicResult;
}

/**
 * Récupère la révolution depuis l'API FastAPI
 */
async function fetchLunarRevolutionFromAPI(
  birthData: BirthData,
  revolutionDate: Date
): Promise<LunarRevolution | null> {
  try {
    // TODO: Implémenter endpoint API si disponible
    // Pour l'instant, retourner null pour utiliser le calcul basique
    return null;
  } catch (error) {
    console.error('[LunarRevolution] Erreur API:', error);
    return null;
  }
}

/**
 * Calcul basique de révolution lunaire
 * Utilise des approximations pour la position lunaire et les aspects
 */
async function calculateBasicLunarRevolution(
  birthData: BirthData,
  revolutionDate: Date,
  monthKey: string
): Promise<LunarRevolution> {
  // Calculer le signe lunaire approximatif à la date de révolution
  const moonSign = getMoonSignForDate(revolutionDate);
  
  // Vérifier que moonSign est valide
  if (!moonSign || !moonSign.name) {
    throw new Error(`Impossible de calculer le signe lunaire pour cette date (${revolutionDate.toISOString()}). La date est peut-être trop ancienne.`);
  }
  
  // Calculer la phase lunaire
  const phase = getMoonPhaseForDate(revolutionDate);
  
  // Calculer la maison activée (approximation basée sur l'ascendant natal)
  // Pour l'instant, utiliser une approximation simple
  const house = calculateHouse(moonSign, birthData);
  
  // Calculer les aspects entre Lune révolution et planètes natales
  const aspects = await calculateLunarRevolutionAspects(revolutionDate, birthData);
  
  // Générer un résumé d'interprétation basique
  const interpretationSummary = generateBasicInterpretation(moonSign, house, phase);
  const focus = generateFocus(house);

  return {
    month: monthKey,
    revolutionDate: revolutionDate.toISOString(),
    moonSign: moonSign.name,
    moonSignEmoji: moonSign.emoji,
    moonDegree: 0, // Sera calculé avec vraies données
    house,
    phase: phase.phase,
    phaseName: phase.name,
    aspects,
    interpretationSummary,
    focus,
  };
}

/**
 * Calcule le signe lunaire approximatif pour une date
 */
function getMoonSignForDate(date: Date): { name: string; emoji: string; element: string } {
  // Utiliser l'algorithme simplifié de moonCalculator
  const { getTodayMoonSign } = require('./moonCalculator');
  return getTodayMoonSign(date);
}

/**
 * Calcule la phase lunaire pour une date
 */
function getMoonPhaseForDate(date: Date): { phase: 'new' | 'waxing' | 'full' | 'waning'; name: string } {
  const { getMoonPhase } = require('./moonCalculator');
  const phaseData = getMoonPhase(date);
  
  let phase: 'new' | 'waxing' | 'full' | 'waning';
  if (phaseData.dayInLunation < 3.7 || phaseData.dayInLunation > 25.9) {
    phase = 'new';
  } else if (phaseData.dayInLunation < 14.8) {
    phase = 'waxing';
  } else if (phaseData.dayInLunation < 18.5) {
    phase = 'full';
  } else {
    phase = 'waning';
  }
  
  return {
    phase,
    name: phaseData.phaseName,
  };
}

/**
 * Calcule les aspects entre la Lune de révolution et les planètes natales
 */
async function calculateLunarRevolutionAspects(
  revolutionDate: Date,
  birthData: BirthData
): Promise<LunarAspect[]> {
  const aspects: LunarAspect[] = [];
  
  try {
    // Récupérer le thème natal depuis le cache
    const natalReading = await getLocalReading();
    
    if (!natalReading || !natalReading.positions || natalReading.positions.length === 0) {
      console.log('[LunarRevolution] ⚠️ Thème natal non disponible dans le cache, aspects non calculés');
      console.log('[LunarRevolution] 💡 Astuce: Va dans "Thème natal" pour charger ton thème, puis reviens ici');
      return aspects;
    }
    
    console.log('[LunarRevolution] 📊 Thème natal trouvé:', natalReading.positions.length, 'positions');
    
    // Calculer la longitude approximative de la Lune à la date de révolution
    const moonLongitude = calculateMoonLongitude(revolutionDate);
    
    // Planètes importantes à vérifier (Big Three + planètes personnelles)
    const importantPlanets = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Ascendant', 'Medium_Coeli'];
    
    // Pour chaque planète importante du thème natal
    for (const planetName of importantPlanets) {
      const natalPosition = natalReading.positions.find((p: any) => p.name === planetName);
      
      if (!natalPosition || !natalPosition.longitude) {
        continue;
      }
      
      // Calculer l'aspect entre Lune révolution et planète natale
      const aspect = calculateAspect(
        'Moon', // Toujours la Lune pour révolution
        moonLongitude,
        planetName,
        natalPosition.longitude
      );
      
      if (aspect) {
        // Générer l'interprétation
        aspect.interpretation = generateAspectInterpretation({
          from: 'Moon',
          to: planetName,
          aspect_type: aspect.aspect_type,
          strength: aspect.strength,
          orb: aspect.orb,
        });
        
        aspects.push(aspect);
      }
    }
    
    console.log('[LunarRevolution] ✅ Aspects calculés:', aspects.length);
  } catch (error) {
    console.error('[LunarRevolution] Erreur calcul aspects:', error);
  }
  
  return aspects;
}

/**
 * Calcule la longitude écliptique approximative de la Lune pour une date
 * Approximation basée sur le cycle lunaire de ~27.3 jours
 */
function calculateMoonLongitude(date: Date): number {
  // Référence : 1er janvier 2025, Lune à ~90° (Cancer)
  const referenceDate = new Date('2025-01-01T00:00:00Z');
  const referenceLongitude = 90; // Cancer
  
  // Calculer jours depuis référence
  const diffTime = date.getTime() - referenceDate.getTime();
  const diffDays = diffTime / (1000 * 60 * 60 * 24);
  
  // Cycle lunaire = 27.32166 jours pour un tour complet (360°)
  const lunarCycleDays = 27.32166;
  const degreesPerDay = 360 / lunarCycleDays;
  
  // Longitude actuelle
  const longitude = (referenceLongitude + diffDays * degreesPerDay) % 360;
  
  return longitude < 0 ? longitude + 360 : longitude;
}

/**
 * Calcule l'aspect entre deux positions planétaires
 * @param fromPlanet - Nom de la planète source (toujours "Moon" pour révolution)
 * @param fromLongitude - Longitude de la planète source
 * @param toPlanet - Nom de la planète cible (planète natale)
 * @param toLongitude - Longitude de la planète cible
 * @returns Aspect ou null si aucun aspect significatif
 */
function calculateAspect(
  fromPlanet: string,
  fromLongitude: number,
  toPlanet: string,
  toLongitude: number
): LunarAspect | null {
  // Calculer la différence angulaire
  let diff = Math.abs(fromLongitude - toLongitude);
  
  // Normaliser entre 0 et 180°
  if (diff > 180) {
    diff = 360 - diff;
  }
  
  // Orbes pour chaque type d'aspect (en degrés)
  const orbs = {
    conjunction: 8,    // 0° ± 8°
    opposition: 8,     // 180° ± 8°
    trine: 6,          // 120° ± 6°
    square: 6,         // 90° ± 6°
    sextile: 4,        // 60° ± 4°
  };
  
  // Vérifier chaque aspect majeur
  let aspectType: string | null = null;
  let exactAngle = 0;
  let orb = 0;
  
  // Conjonction (0°)
  if (diff <= orbs.conjunction) {
    aspectType = 'conjunction';
    exactAngle = 0;
    orb = diff;
  }
  // Opposition (180°)
  else if (Math.abs(diff - 180) <= orbs.opposition) {
    aspectType = 'opposition';
    exactAngle = 180;
    orb = Math.abs(diff - 180);
  }
  // Trigone (120°)
  else if (Math.abs(diff - 120) <= orbs.trine) {
    aspectType = 'trine';
    exactAngle = 120;
    orb = Math.abs(diff - 120);
  }
  // Carré (90°)
  else if (Math.abs(diff - 90) <= orbs.square) {
    aspectType = 'square';
    exactAngle = 90;
    orb = Math.abs(diff - 90);
  }
  // Sextile (60°)
  else if (Math.abs(diff - 60) <= orbs.sextile) {
    aspectType = 'sextile';
    exactAngle = 60;
    orb = Math.abs(diff - 60);
  }
  
  if (!aspectType) {
    return null;
  }
  
  // Déterminer l'intensité selon l'orbe
  let strength: 'strong' | 'medium' | 'weak';
  if (orb <= 2) {
    strength = 'strong';
  } else if (orb <= 4) {
    strength = 'medium';
  } else {
    strength = 'weak';
  }
  
  return {
    from: fromPlanet,
    to: toPlanet,
    aspect_type: aspectType,
    strength,
    orb: orb,
  };
}

/**
 * Calcule la maison activée (approximation)
 */
function calculateHouse(moonSign: { name: string } | null | undefined, birthData: BirthData): number {
  // Vérifier que moonSign est valide
  if (!moonSign || !moonSign.name) {
    console.warn('[LunarRevolution] moonSign invalide, utilisation de la maison 1 par défaut');
    return 1;
  }
  
  // Approximation basique : utiliser le signe pour déterminer la maison
  // Dans un vrai calcul, on utiliserait les maisons natales
  const signToHouse: Record<string, number> = {
    'Bélier': 1, 'Taureau': 2, 'Gémeaux': 3, 'Cancer': 4,
    'Lion': 5, 'Vierge': 6, 'Balance': 7, 'Scorpion': 8,
    'Sagittaire': 9, 'Capricorne': 10, 'Verseau': 11, 'Poissons': 12,
  };
  
  return signToHouse[moonSign.name] || 1;
}

/**
 * Génère une interprétation basique
 */
function generateBasicInterpretation(
  moonSign: { name: string; element: string },
  house: number,
  phase: { name: string }
): string {
  return `La Lune en ${moonSign.name} (${moonSign.element}) active ta Maison ${house} en phase ${phase.name}. Cette période met l'accent sur tes besoins émotionnels et tes domaines de vie liés à cette maison.`;
}

/**
 * Génère le focus selon la maison
 */
function generateFocus(house: number): string {
  const houseFocus: Record<number, string> = {
    1: 'identité et image de soi',
    2: 'valeurs et ressources',
    3: 'communication et apprentissage',
    4: 'foyer et famille',
    5: 'créativité et plaisir',
    6: 'santé et routine',
    7: 'relations et partenariats',
    8: 'transformation et partage',
    9: 'sagesse et exploration',
    10: 'carrière et responsabilités',
    11: 'amitié et projets',
    12: 'introspection et spiritualité',
  };
  
  return houseFocus[house] || 'développement personnel';
}

/**
 * Cache la révolution lunaire localement
 */
async function cacheRevolution(monthKey: string, revolution: LunarRevolution): Promise<void> {
  try {
    const cacheKey = `lunar_revolution_${monthKey}`;
    await AsyncStorage.setItem(cacheKey, JSON.stringify(revolution));
    console.log('[LunarRevolution] 💾 Révolution sauvegardée:', monthKey);
  } catch (error) {
    console.error('[LunarRevolution] Erreur cache:', error);
  }
}

/**
 * Récupère la révolution depuis le cache
 */
export async function getCachedRevolution(monthKey: string): Promise<LunarRevolution | null> {
  try {
    const cacheKey = `lunar_revolution_${monthKey}`;
    const data = await AsyncStorage.getItem(cacheKey);
    return data ? JSON.parse(data) : null;
  } catch (error) {
    console.error('[LunarRevolution] Erreur lecture cache:', error);
    return null;
  }
}

