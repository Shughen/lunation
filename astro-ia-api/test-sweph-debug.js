// Test debug de sweph
import sweph from 'sweph';

const constants = sweph.constants;
const IFLAG = constants.SEFLG_SWIEPH | constants.SEFLG_SPEED;

console.log('\n🔍 TEST DEBUG SWEPH\n');

// Date de test
const year = 1989;
const month = 4;
const day = 15;
const hour = 17 + 55/60;

// Calculer Julian Day
const julday = sweph.julday(year, month, day, hour, constants.SE_GREG_CAL);
console.log('Julian Day:', julday);

// Tester calc_ut pour le Soleil
console.log('\n📍 Test Soleil (SE_SUN =', constants.SE_SUN, ')');
const sunResult = sweph.calc_ut(julday, constants.SE_SUN, IFLAG);
console.log('Résultat complet:', JSON.stringify(sunResult, null, 2));

// Tester houses
console.log('\n📍 Test Houses (Placidus)');
const lat = 48.919;
const lon = 2.543;
const housesResult = sweph.houses(julday, lat, lon, 'P');
console.log('Résultat complet:', JSON.stringify(housesResult, null, 2));

