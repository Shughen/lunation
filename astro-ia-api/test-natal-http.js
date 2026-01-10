#!/usr/bin/env node
// ============================================
// TEST HTTP DE L'API THÈME NATAL
// ============================================

const testData = {
  date: '1989-04-15',
  time: '17:55',
  lat: 48.919,
  lon: 2.543,
  tz: 'Europe/Paris',
};

const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
  yellow: '\x1b[33m',
};

async function testAPI() {
  console.log(`${colors.cyan}
╔═════════════════════════════════════════════════╗
║  🌟 TEST HTTP - API THÈME NATAL                ║
╚═════════════════════════════════════════════════╝
${colors.reset}`);

  const apiUrl = process.env.API_URL || 'http://localhost:3000';
  
  console.log(`${colors.blue}📍 Configuration :${colors.reset}`);
  console.log(`   API URL : ${apiUrl}`);
  console.log(`   Date    : ${testData.date}`);
  console.log(`   Heure   : ${testData.time}`);
  console.log(`   Lieu    : ${testData.lat}, ${testData.lon}\n`);

  try {
    console.log(`${colors.yellow}⏳ Appel API en cours...${colors.reset}\n`);
    
    const startTime = Date.now();
    
    const response = await fetch(`${apiUrl}/api/astro/natal`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(testData),
    });

    const latency = Date.now() - startTime;

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`HTTP ${response.status}: ${error}`);
    }

    const data = await response.json();
    const positions = data.chart || data.positions;

    console.log(`${colors.green}✅ RÉSULTATS :${colors.reset}\n`);
    console.log(`   ☀️  Soleil    : ${positions.sun.emoji} ${positions.sun.sign} ${positions.sun.degree}° ${positions.sun.minutes}'`);
    console.log(`   🌙 Lune      : ${positions.moon.emoji} ${positions.moon.sign} ${positions.moon.degree}° ${positions.moon.minutes}'`);
    console.log(`   ⬆️  Ascendant : ${positions.ascendant.emoji} ${positions.ascendant.sign} ${positions.ascendant.degree}° ${positions.ascendant.minutes}'`);
    console.log(`   ☿️  Mercure   : ${positions.mercury.emoji} ${positions.mercury.sign} ${positions.mercury.degree}° ${positions.mercury.minutes}'`);
    console.log(`   ♀️  Vénus     : ${positions.venus.emoji} ${positions.venus.sign} ${positions.venus.degree}° ${positions.venus.minutes}'`);
    console.log(`   ♂️  Mars      : ${positions.mars.emoji} ${positions.mars.sign} ${positions.mars.degree}° ${positions.mars.minutes}'`);

    console.log(`\n${colors.blue}📊 PERFORMANCES :${colors.reset}\n`);
    console.log(`   Latence API  : ${latency}ms`);
    console.log(`   Latence calc : ${data.latencyMs}ms`);
    console.log(`   Provider     : ${data.meta.provider}`);
    console.log(`   Version      : ${data.meta.version}`);
    console.log(`   Coût         : $${data.meta.cost}`);

    console.log(`\n${colors.green}✨ Test HTTP réussi ! L'API est opérationnelle.${colors.reset}\n`);

    return { success: true, data };

  } catch (error) {
    console.error(`\n${colors.reset}❌ ERREUR : ${error.message}\n`);
    
    if (error.message.includes('ECONNREFUSED')) {
      console.log(`${colors.yellow}💡 L'API n'est pas démarrée. Lance-la avec :${colors.reset}`);
      console.log(`   ${colors.cyan}cd /Users/remibeaurain/astroia/astro-ia-api${colors.reset}`);
      console.log(`   ${colors.cyan}vercel dev${colors.reset}\n`);
    }
    
    return { success: false, error: error.message };
  }
}

// Exécution
testAPI().catch(console.error);

