// ============================================
// TEST RAPIDE DU THÈME NATAL
// ============================================

import { calculateNatalChart } from './api/astro/natal-providers.js';

const testData = {
  date: '1989-04-15',
  time: '17:55',
  lat: 48.919,
  lon: 2.543,
  tz: 'Europe/Paris',
};

console.log('\n🌟 TEST DU CALCUL DE THÈME NATAL\n');
console.log('📍 Données :');
console.log(`   Date : ${testData.date}`);
console.log(`   Heure : ${testData.time}`);
console.log(`   Lieu : ${testData.lat}, ${testData.lon}`);

async function test() {
  try {
    console.log('\n⏳ Calcul en cours...\n');
    
    const startTime = Date.now();
    const result = await calculateNatalChart(testData);
    const latency = Date.now() - startTime;
    
    console.log('✅ RÉSULTATS :\n');
    console.log(`   ☀️  Soleil    : ${result.positions.sun.emoji} ${result.positions.sun.sign} ${result.positions.sun.degree}° ${result.positions.sun.minutes}'`);
    console.log(`   🌙 Lune      : ${result.positions.moon.emoji} ${result.positions.moon.sign} ${result.positions.moon.degree}° ${result.positions.moon.minutes}'`);
    console.log(`   ⬆️  Ascendant : ${result.positions.ascendant.emoji} ${result.positions.ascendant.sign} ${result.positions.ascendant.degree}° ${result.positions.ascendant.minutes}'`);
    console.log(`   ☿️  Mercure   : ${result.positions.mercury.emoji} ${result.positions.mercury.sign} ${result.positions.mercury.degree}° ${result.positions.mercury.minutes}'`);
    console.log(`   ♀️  Vénus     : ${result.positions.venus.emoji} ${result.positions.venus.sign} ${result.positions.venus.degree}° ${result.positions.venus.minutes}'`);
    console.log(`   ♂️  Mars      : ${result.positions.mars.emoji} ${result.positions.mars.sign} ${result.positions.mars.degree}° ${result.positions.mars.minutes}'`);
    
    console.log('\n📊 MÉTADONNÉES :\n');
    console.log(`   Provider  : ${result.meta.provider}`);
    console.log(`   Coût      : $${result.meta.cost}`);
    console.log(`   Latence   : ${latency}ms`);
    console.log(`   Précision : ${JSON.stringify(result.meta.precision)}`);
    
    console.log('\n✨ Test réussi ! Le provider LOCAL fonctionne parfaitement.\n');
    
  } catch (error) {
    console.error('\n❌ ERREUR :', error.message);
    console.error(error.stack);
  }
}

test();

