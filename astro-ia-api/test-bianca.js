// Test avec les données exactes de Bianca (Manaus, Brésil)
import { calculateNatalChart } from './api/astro/natal-providers.js';

const testData = {
  date: '1989-11-01',
  time: '13:20',
  lat: -3.1316333,
  lon: -59.9825041,
  tz: 'America/Manaus',
};

console.log('\n🌟 TEST - BIANCA (Manaus, Brésil)\n');
console.log('📍 Données :');
console.log(`   Date : ${testData.date}`);
console.log(`   Heure : ${testData.time}`);
console.log(`   Lieu : Manaus (${testData.lat}, ${testData.lon})`);

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
    
    console.log('\n🎯 ATTENDU (Astrotheme) :\n');
    console.log('   ☀️  Soleil    : ♏ Scorpion 9°16\'');
    console.log('   🌙 Lune      : ♐ Sagittaire 13°1\'');
    console.log('   ⬆️  Ascendant : ♓ Poissons 29°29\'');  // ou Verseau selon le thème
    console.log('   ☿️  Mercure   : ♏ Scorpion 28°19\'');
    
    console.log('\n📊 MÉTADONNÉES :\n');
    console.log(`   Provider  : ${result.meta.provider}`);
    console.log(`   Coût      : $${result.meta.cost}`);
    console.log(`   Latence   : ${latency}ms`);
    console.log(`   Précision : ${JSON.stringify(result.meta.precision)}`);
    
    console.log('\n✨ Test terminé !\n');
    
  } catch (error) {
    console.error('\n❌ ERREUR :', error.message);
    console.error(error.stack);
  }
}

test();

