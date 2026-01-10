/**
 * Service d'export PDF
 * Génération rapports cycle mensuels professionnels
 */

// Temporairement désactivé (modules natifs)
// import * as Print from 'expo-print';
// import * as Sharing from 'expo-sharing';

/**
 * Génère un rapport PDF du cycle mensuel
 * @param {Object} cycleData - Données cycle du mois
 * @param {Array} insights - Insights IA
 * @returns {Promise<string>} URI du PDF
 */
export async function generateCycleReport(cycleData, insights = []) {
  try {
    const html = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
      padding: 40px;
      color: #1E1B4B;
      max-width: 800px;
      margin: 0 auto;
    }
    
    .header {
      text-align: center;
      margin-bottom: 40px;
      border-bottom: 3px solid #C084FC;
      padding-bottom: 30px;
    }
    
    .logo {
      font-size: 48px;
      margin-bottom: 10px;
    }
    
    h1 {
      color: #C084FC;
      font-size: 32px;
      margin: 10px 0;
    }
    
    .subtitle {
      color: #666;
      font-size: 14px;
    }
    
    .section {
      margin: 30px 0;
      padding: 20px;
      background: #F9FAFB;
      border-radius: 12px;
      border-left: 4px solid #FFB6C1;
    }
    
    h2 {
      color: #1E1B4B;
      font-size: 22px;
      margin-bottom: 15px;
    }
    
    .stat-row {
      display: flex;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid #E5E7EB;
    }
    
    .stat-row:last-child {
      border-bottom: none;
    }
    
    .stat-label {
      font-weight: 600;
      color: #6B7280;
    }
    
    .stat-value {
      color: #1E1B4B;
      font-weight: 700;
    }
    
    .insight {
      background: linear-gradient(135deg, #FFF5F7 0%, #F3E8FF 100%);
      padding: 15px 20px;
      border-radius: 10px;
      margin: 10px 0;
      border-left: 3px solid #C084FC;
    }
    
    .insight-emoji {
      font-size: 24px;
      margin-right: 10px;
    }
    
    .phase-badge {
      display: inline-block;
      padding: 5px 15px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 600;
      margin-right: 10px;
    }
    
    .phase-menstrual { background: #FFE4EC; color: #FF6B9D; }
    .phase-follicular { background: #FFF4E6; color: #FFB347; }
    .phase-ovulation { background: #FFFAEB; color: #FFD93D; }
    .phase-luteal { background: #F3E8FF; color: #C084FC; }
    
    .footer {
      margin-top: 50px;
      padding-top: 20px;
      border-top: 2px solid #E5E7EB;
      text-align: center;
      font-size: 12px;
      color: #9CA3AF;
    }
    
    .disclaimer {
      background: #FEF3C7;
      border: 1px solid #FCD34D;
      border-radius: 8px;
      padding: 15px;
      margin: 20px 0;
      font-size: 13px;
      color: #92400E;
    }
  </style>
</head>
<body>
  <div class="header">
    <div class="logo">🌙</div>
    <h1>LUNA - Rapport Cycle</h1>
    <div class="subtitle">
      Période : ${cycleData.startDate || 'N/A'} — ${cycleData.endDate || new Date().toLocaleDateString('fr-FR')}
    </div>
  </div>

  <div class="section">
    <h2>📊 Résumé du Cycle</h2>
    <div class="stat-row">
      <span class="stat-label">Durée moyenne cycle :</span>
      <span class="stat-value">${cycleData.cycleLength || 28} jours</span>
    </div>
    <div class="stat-row">
      <span class="stat-label">Phase actuelle :</span>
      <span class="stat-value">
        <span class="phase-badge phase-${(cycleData.currentPhase || '').toLowerCase()}">${cycleData.currentPhase || 'N/A'}</span>
      </span>
    </div>
    <div class="stat-row">
      <span class="stat-label">Jour du cycle :</span>
      <span class="stat-value">Jour ${cycleData.dayOfCycle || 'N/A'}</span>
    </div>
    <div class="stat-row">
      <span class="stat-label">Énergie moyenne :</span>
      <span class="stat-value">${cycleData.avgEnergy || 'N/A'}%</span>
    </div>
    <div class="stat-row">
      <span class="stat-label">Prochaines règles (prévision) :</span>
      <span class="stat-value">${cycleData.nextPeriodDate || 'N/A'}</span>
    </div>
  </div>

  ${insights && insights.length > 0 ? `
    <div class="section">
      <h2>💡 Insights Personnalisés</h2>
      ${insights.map(insight => `
        <div class="insight">
          <span class="insight-emoji">${insight.emoji}</span>
          <span>${insight.text}</span>
        </div>
      `).join('')}
    </div>
  ` : ''}

  <div class="disclaimer">
    ⚕️ <strong>Important :</strong> LUNA est un outil de bien-être, pas un dispositif médical. 
    Les prédictions de cycle sont basées sur des moyennes et peuvent varier. 
    Consulte toujours un·e professionnel·le pour avis médical.
  </div>

  <div class="footer">
    <p><strong>LUNA - Cycle & Cosmos</strong></p>
    <p>Généré le ${new Date().toLocaleDateString('fr-FR')} à ${new Date().toLocaleTimeString('fr-FR')}</p>
    <p>© 2025 Astroia - Tous droits réservés</p>
    <p style="margin-top: 10px;">
      support@luna-app.fr | luna-app.fr
    </p>
  </div>
</body>
</html>
    `;
    
    // Générer le PDF (temporairement désactivé - module natif)
    console.log('[PDF] Module temporairement désactivé');
    throw new Error('Export PDF disponible uniquement dans la version native (TestFlight/Play Store)');
    
    // const { uri } = await Print.printToFileAsync({ html });
    // console.log('[PDF] Rapport généré:', uri);
    // return uri;
  } catch (error) {
    console.error('[PDF] Erreur génération:', error);
    throw error;
  }
}

/**
 * Génère et partage un rapport PDF
 * @param {Object} cycleData - Données cycle
 * @param {Array} insights - Insights IA
 */
export async function shareCycleReport(cycleData, insights) {
  try {
    const uri = await generateCycleReport(cycleData, insights);
    
    // Vérifier si le partage est disponible
    const isAvailable = await Sharing.isAvailableAsync();
    
    if (!isAvailable) {
      throw new Error('Partage non disponible sur cet appareil');
    }
    
    // Partager le PDF
    await Sharing.shareAsync(uri, {
      mimeType: 'application/pdf',
      dialogTitle: 'Partager mon rapport cycle LUNA',
      UTI: 'com.adobe.pdf',
    });
    
    console.log('[PDF] Rapport partagé');
  } catch (error) {
    console.error('[PDF] Erreur partage:', error);
    throw error;
  }
}

export default {
  generateCycleReport,
  shareCycleReport,
};

