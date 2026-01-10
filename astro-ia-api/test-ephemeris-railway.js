// Test avec l'API ephemeris déployée sur Railway
import { calculateEphemerisAPI } from './api/astro/natal-ephemeris.js';

// Configurer l'URL Railway
process.env.EPHEMERIS_API_URL = 'https://web-production-d5955.up.railway.app';

const testData = {
  date: '1989-11-01',
  time: '13:20',
  lat: -3.1316333,
  lon: -59.9825041,
  tz: 'America/Manaus',
};

console.log('\n🌟 TEST - EPHEMERIS API (Railway)\n');
console.log('📍 Données :');
console.log(`   Date : ${testData.date}`);
console.log(`   Heure : ${testData.time}`);
console.log(`   Lieu : Manaus (${testData.lat}, ${testData.lon})`);
console.log(`   API URL : ${process.env.EPHEMERIS_API_URL}\n`);

async function test() {
  try {
    console.log('⏳ Appel de l\'API Railway...\n');
    
    const startTime = Date.now();
    const result = await calculateEphemerisAPI(testData);
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
    console.log('   ⬆️  Ascendant : ♒ Verseau 29°29\'');
    console.log('   ☿️  Mercure   : ♏ Scorpion 28°19\'');
    
    console.log('\n📊 MÉTADONNÉES :\n');
    console.log(`   Provider  : ${result.meta.provider}`);
    console.log(`   API URL   : ${result.meta.api_url}`);
    console.log(`   Coût      : $${result.meta.cost}`);
    console.log(`   Latence   : ${latency}ms`);
    console.log(`   Précision : ${result.meta.precision}`);
    
    console.log('\n✨ Test Railway réussi ! Swiss Ephemeris gratuit opérationnel.\n');
    
  } catch (error) {
    console.error('\n❌ ERREUR :', error.message);
    console.error(error.stack);
  }
}

test();

