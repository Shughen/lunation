/**
 * Service d'export des données utilisateur
 * Permet d'exporter les données en JSON ou PDF conformément au RGPD
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import * as FileSystem from 'expo-file-system';
// import * as Sharing from 'expo-sharing'; // Temporairement désactivé
import { Alert, Platform, Share } from 'react-native';

/**
 * Exporte toutes les données utilisateur en JSON
 */
export async function exportDataJSON() {
  try {
    // Récupérer toutes les clés
    const allKeys = await AsyncStorage.getAllKeys();
    const allData = await AsyncStorage.multiGet(allKeys);
    
    // Organiser les données par catégorie
    const exportData = {
      exportDate: new Date().toISOString(),
      version: '2.0.0',
      data: {},
    };

    allData.forEach(([key, value]) => {
      try {
        exportData.data[key] = JSON.parse(value);
      } catch {
        exportData.data[key] = value;
      }
    });

    // Créer le fichier JSON
    const fileName = `LUNA_export_${Date.now()}.json`;
    const filePath = `${FileSystem.documentDirectory}${fileName}`;
    
    await FileSystem.writeAsStringAsync(
      filePath,
      JSON.stringify(exportData, null, 2),
      { encoding: FileSystem.EncodingType.UTF8 }
    );

    // Partager le fichier (utilise Share natif temporairement)
    await Share.share({
      url: filePath,
      title: 'Exporter mes données LUNA',
    });

    return { success: true, filePath };
  } catch (error) {
    console.error('[ExportService] Export JSON error:', error);
    throw error;
  }
}

/**
 * Exporte les données du dernier mois en PDF
 * Format simple avec texte (pas de libs PDF complexes pour MVP)
 */
export async function exportDataPDF() {
  try {
    // Pour MVP, on crée un fichier texte formaté
    // Plus tard : utiliser react-native-pdf-lib ou équivalent
    
    const exportText = await generateExportText();
    
    const fileName = `LUNA_rapport_${Date.now()}.txt`;
    const filePath = `${FileSystem.documentDirectory}${fileName}`;
    
    await FileSystem.writeAsStringAsync(
      filePath,
      exportText,
      { encoding: FileSystem.EncodingType.UTF8 }
    );

    // Partager
    // Utiliser Share natif temporairement
    await Share.share({
      url: filePath,
      title: 'Rapport LUNA',
    });

    return { success: true, filePath };
  } catch (error) {
    console.error('[ExportService] Export PDF error:', error);
    throw error;
  }
}

/**
 * Génère le texte d'export formaté
 */
async function generateExportText() {
  const profile = await AsyncStorage.getItem('user_profile');
  const cycleConfig = await AsyncStorage.getItem('cycle_config');
  
  let text = `🌙 LUNA - Cycle & Cosmos\n`;
  text += `Rapport généré le ${new Date().toLocaleDateString('fr-FR')}\n`;
  text += `\n${'='.repeat(50)}\n\n`;
  
  // Profil
  if (profile) {
    const profileData = JSON.parse(profile);
    text += `📋 PROFIL\n`;
    text += `Nom : ${profileData.name || 'Non renseigné'}\n`;
    text += `Date de naissance : ${profileData.birthDate || 'Non renseignée'}\n`;
    text += `Signe solaire : ${profileData.zodiacSign || 'Non calculé'}\n`;
    text += `\n`;
  }

  // Cycle
  if (cycleConfig) {
    const cycle = JSON.parse(cycleConfig);
    text += `🩸 CYCLE MENSTRUEL\n`;
    text += `Dernières règles : ${cycle.lastPeriodDate || 'Non renseigné'}\n`;
    text += `Durée moyenne : ${cycle.cycleLength || 28} jours\n`;
    text += `\n`;
  }

  // Journal
  const allKeys = await AsyncStorage.getAllKeys();
  const journalKeys = allKeys.filter(k => k.startsWith('journal_'));
  
  if (journalKeys.length > 0) {
    text += `📖 JOURNAL (${journalKeys.length} entrées)\n`;
    text += `\n`;
    
    // Limiter aux 30 dernières entrées pour le rapport
    const recentEntries = journalKeys.slice(0, 30);
    
    for (const key of recentEntries) {
      const entry = await AsyncStorage.getItem(key);
      if (entry) {
        const entryData = JSON.parse(entry);
        text += `${entryData.date || 'Date inconnue'}\n`;
        text += `  Humeur : ${entryData.mood || 'Non renseignée'}\n`;
        if (entryData.note) {
          text += `  Note : ${entryData.note}\n`;
        }
        text += `\n`;
      }
    }
  }

  text += `\n${'='.repeat(50)}\n\n`;
  text += `Fin du rapport\n`;
  text += `LUNA - Suis ton cycle, écoute les étoiles 🌙\n`;
  
  return text;
}

/**
 * Supprime toutes les données utilisateur
 * Conformité RGPD - droit à l'oubli
 */
export async function deleteAllUserData() {
  try {
    // Sauvegarder les infos d'onboarding pour afficher écran de départ
    const onboardingCompleted = await AsyncStorage.getItem('onboarding_completed');
    
    // Tout supprimer
    await AsyncStorage.clear();
    
    // Restaurer juste le flag onboarding si on veut montrer le login
    // (optionnel selon UX souhaité)
    
    console.log('[ExportService] All user data deleted');
    return { success: true };
  } catch (error) {
    console.error('[ExportService] Delete data error:', error);
    throw error;
  }
}

export default {
  exportDataJSON,
  exportDataPDF,
  deleteAllUserData,
};

