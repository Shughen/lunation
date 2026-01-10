#!/usr/bin/env node
// ============================================
// TEST DES PROVIDERS DE THÈME NATAL
// ============================================
// Compare les résultats de LOCAL vs PROKERALA vs ASTROLOGER

const fetch = require('node-fetch');

const TEST_DATA = {
  date: '1989-04-15',
  time: '17:55',
  lat: 48.919,
  lon: 2.543,
  tz: 'Europe/Paris',
  name: 'Test Livry-Gargan',
};

const EXPECTED_RESULTS = {
  sun: { sign: 'Bélier', emoji: '♈' },
  moon: { sign: 'Lion', emoji: '♌' },
  ascendant: { sign: 'Cancer', emoji: '♋' },
};

// Couleurs pour terminal
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
};

async function testProvider(providerName, apiUrl = 'http://localhost:3000') {
  console.log(`\n${colors.blue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}`);
  console.log(`${colors.cyan}🧪 Test Provider: ${providerName.toUpperCase()}${colors.reset}`);
  console.log(`${colors.blue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}`);

  try {
    const startTime = Date.now();
    
    const response = await fetch(`${apiUrl}/api/astro/natal`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...TEST_DATA,
        provider: providerName,
      }),
    });

    const latency = Date.now() - startTime;

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`HTTP ${response.status}: ${error}`);
    }

    const data = await response.json();
    
    // Extraire les positions
    const positions = data.chart || data.positions;
    
    console.log(`\n📊 Résultats :`);
    console.log(`   ☀️  Soleil    : ${positions.sun.emoji} ${positions.sun.sign} ${positions.sun.degree}° ${positions.sun.minutes}'`);
    console.log(`   🌙 Lune      : ${positions.moon.emoji} ${positions.moon.sign} ${positions.moon.degree}° ${positions.moon.minutes}'`);
    console.log(`   ⬆️  Ascendant : ${positions.ascendant.emoji} ${positions.ascendant.sign} ${positions.ascendant.degree}° ${positions.ascendant.minutes}'`);
    
    // Vérifier exactitude
    const sunCorrect = positions.sun.sign === EXPECTED_RESULTS.sun.sign;
    const moonCorrect = positions.moon.sign === EXPECTED_RESULTS.moon.sign;
    const ascCorrect = positions.ascendant.sign === EXPECTED_RESULTS.ascendant.sign;
    
    console.log(`\n✅ Validation :`);
    console.log(`   Soleil    : ${sunCorrect ? colors.green + '✓' : colors.red + '✗'} ${colors.reset}`);
    console.log(`   Lune      : ${moonCorrect ? colors.green + '✓' : colors.red + '✗'} ${colors.reset}`);
    console.log(`   Ascendant : ${ascCorrect ? colors.green + '✓' : colors.red + '✗'} ${colors.reset}`);
    
    // Métadonnées
    console.log(`\n📈 Performances :`);
    console.log(`   Latence   : ${latency}ms`);
    console.log(`   Provider  : ${data.meta.provider}`);
    console.log(`   Coût      : ${data.meta.cost !== undefined ? '$' + data.meta.cost : 'N/A'}`);
    if (data.meta.precision) {
      console.log(`   Précision : ${typeof data.meta.precision === 'string' ? data.meta.precision : JSON.stringify(data.meta.precision)}`);
    }
    
    return {
      provider: providerName,
      success: true,
      latency,
      correct: sunCorrect && moonCorrect && ascCorrect,
      positions,
      meta: data.meta,
    };

  } catch (error) {
    console.log(`\n${colors.red}❌ Erreur : ${error.message}${colors.reset}`);
    
    return {
      provider: providerName,
      success: false,
      error: error.message,
    };
  }
}

async function main() {
  console.log(`${colors.cyan}
╔═════════════════════════════════════════════════╗
║  🌟 TEST DES PROVIDERS DE THÈME NATAL          ║
╚═════════════════════════════════════════════════╝
${colors.reset}`);

  console.log(`📍 Données de test :`);
  console.log(`   Nom       : ${TEST_DATA.name}`);
  console.log(`   Date      : ${TEST_DATA.date}`);
  console.log(`   Heure     : ${TEST_DATA.time}`);
  console.log(`   Lieu      : ${TEST_DATA.lat}, ${TEST_DATA.lon}`);
  console.log(`   Timezone  : ${TEST_DATA.tz}`);
  
  console.log(`\n🎯 Résultats attendus :`);
  console.log(`   Soleil    : ${EXPECTED_RESULTS.sun.emoji} ${EXPECTED_RESULTS.sun.sign}`);
  console.log(`   Lune      : ${EXPECTED_RESULTS.moon.emoji} ${EXPECTED_RESULTS.moon.sign}`);
  console.log(`   Ascendant : ${EXPECTED_RESULTS.ascendant.emoji} ${EXPECTED_RESULTS.ascendant.sign}`);

  // URL de l'API (local ou production)
  const apiUrl = process.env.API_URL || 'http://localhost:3000';
  console.log(`\n🌐 API URL : ${apiUrl}`);

  // Tester chaque provider
  const results = [];
  
  // 1. LOCAL (toujours disponible)
  results.push(await testProvider('local', apiUrl));
  
  // 2. PROKERALA (si configuré)
  if (process.env.PROKERALA_API_KEY) {
    results.push(await testProvider('prokerala', apiUrl));
  } else {
    console.log(`\n${colors.yellow}⚠️  PROKERALA skipped: PROKERALA_API_KEY not set${colors.reset}`);
  }
  
  // 3. ASTROLOGER (si configuré)
  if (process.env.ASTROLOGER_API_URL) {
    results.push(await testProvider('astrologer', apiUrl));
  } else {
    console.log(`\n${colors.yellow}⚠️  ASTROLOGER skipped: ASTROLOGER_API_URL not set${colors.reset}`);
  }

  // Résumé
  console.log(`\n${colors.blue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}`);
  console.log(`${colors.cyan}📊 RÉSUMÉ COMPARATIF${colors.reset}`);
  console.log(`${colors.blue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}\n`);

  console.log(`${'Provider'.padEnd(15)} ${'Statut'.padEnd(12)} ${'Latence'.padEnd(12)} ${'Précision'.padEnd(12)} ${'Coût'}`);
  console.log(`${'─'.repeat(60)}`);

  results.forEach(result => {
    const status = result.success 
      ? (result.correct ? colors.green + '✓ Success' : colors.yellow + '⚠ Warning') + colors.reset
      : colors.red + '✗ Failed' + colors.reset;
    
    const latency = result.latency ? `${result.latency}ms` : 'N/A';
    const accuracy = result.correct !== undefined ? (result.correct ? '✓' : '✗') : 'N/A';
    const cost = result.meta?.cost !== undefined ? `$${result.meta.cost}` : 'N/A';
    
    console.log(
      `${result.provider.padEnd(15)} ` +
      `${status.padEnd(20)} ` +
      `${latency.padEnd(12)} ` +
      `${accuracy.padEnd(12)} ` +
      `${cost}`
    );
  });

  console.log(`\n${colors.cyan}✨ Recommandation :${colors.reset}`);
  
  const successfulProviders = results.filter(r => r.success && r.correct);
  
  if (successfulProviders.length === 0) {
    console.log(`   ${colors.red}❌ Aucun provider fonctionnel !${colors.reset}`);
  } else {
    // Trouver le plus rapide
    const fastest = successfulProviders.reduce((prev, current) => 
      (prev.latency < current.latency) ? prev : current
    );
    
    console.log(`   ${colors.green}✓ ${fastest.provider.toUpperCase()} - Le plus rapide (${fastest.latency}ms)${colors.reset}`);
    
    // Recommandation selon le contexte
    const localResult = results.find(r => r.provider === 'local');
    if (localResult?.success && localResult?.correct) {
      console.log(`   ${colors.green}→ LOCAL recommandé pour MVP (gratuit, rapide)${colors.reset}`);
    }
  }

  console.log(`\n${colors.blue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${colors.reset}\n`);
}

// Exécution
main().catch(console.error);

