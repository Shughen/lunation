/**
 * Service de synchronisation offline
 * Queue d'actions + sync automatique au retour connexion
 */

import NetInfo from '@react-native-community/netinfo';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { supabase } from '../supabase';

let syncQueue = [];
let isOnline = true;
let listeners = [];

/**
 * Initialise le service de sync
 */
export function initSyncService() {
  // Charger la queue depuis AsyncStorage
  loadQueue();
  
  // Écouter changements connexion
  NetInfo.addEventListener(state => {
    const wasOffline = !isOnline;
    isOnline = state.isConnected ?? true;
    
    // Notifier listeners
    notifyListeners(isOnline);
    
    // Si retour online, process queue
    if (isOnline && wasOffline) {
      console.log('[Sync] Back online, processing queue');
      processQueue();
    } else if (!isOnline) {
      console.log('[Sync] Offline mode activated');
    }
  });
  
  console.log('[Sync] Service initialized');
}

/**
 * Ajoute un listener pour changements connexion
 * @param {Function} callback - (isOnline) => void
 * @returns {Function} Unsubscribe function
 */
export function addConnectivityListener(callback) {
  listeners.push(callback);
  
  // Retourne fonction unsubscribe
  return () => {
    listeners = listeners.filter(cb => cb !== callback);
  };
}

function notifyListeners(online) {
  listeners.forEach(cb => cb(online));
}

/**
 * Ajoute une action à la queue de sync
 * @param {Object} action - { type, data, timestamp }
 */
export async function queueAction(action) {
  try {
    syncQueue.push({
      ...action,
      id: Date.now() + Math.random(),
      timestamp: Date.now(),
      retries: 0,
    });
    
    await saveQueue();
    
    console.log(`[Sync] Action queued: ${action.type}`);
    
    // Si online, process immédiatement
    if (isOnline) {
      processQueue();
    }
  } catch (error) {
    console.error('[Sync] Erreur queue action:', error);
  }
}

/**
 * Process la queue d'actions
 */
async function processQueue() {
  if (syncQueue.length === 0) {
    console.log('[Sync] Queue vide');
    return;
  }
  
  if (!isOnline) {
    console.log('[Sync] Offline, skip processing');
    return;
  }
  
  console.log(`[Sync] Processing ${syncQueue.length} actions...`);
  
  const actionsToProcess = [...syncQueue];
  
  for (const action of actionsToProcess) {
    try {
      await executeAction(action);
      
      // Succès : retirer de la queue
      syncQueue = syncQueue.filter(a => a.id !== action.id);
      console.log(`[Sync] Action ${action.type} completed`);
      
    } catch (error) {
      console.error(`[Sync] Action ${action.type} failed:`, error);
      
      // Incrémenter retries
      const actionInQueue = syncQueue.find(a => a.id === action.id);
      if (actionInQueue) {
        actionInQueue.retries += 1;
        
        // Si trop de retries (>3), abandonner
        if (actionInQueue.retries > 3) {
          console.error(`[Sync] Action ${action.type} abandoned after 3 retries`);
          syncQueue = syncQueue.filter(a => a.id !== action.id);
        }
      }
    }
  }
  
  await saveQueue();
}

/**
 * Exécute une action selon son type
 */
async function executeAction(action) {
  switch (action.type) {
    case 'save_journal_entry':
      return await saveJournalEntryToSupabase(action.data);
      
    case 'save_analysis':
      return await saveAnalysisToSupabase(action.data);
      
    case 'update_profile':
      return await updateProfileToSupabase(action.data);
      
    case 'delete_analysis':
      return await deleteAnalysisFromSupabase(action.data);
      
    default:
      console.warn(`[Sync] Unknown action type: ${action.type}`);
  }
}

// Helpers Supabase (exemples)
async function saveJournalEntryToSupabase(data) {
  const { error } = await supabase
    .from('journal_entries')
    .insert(data);
  
  if (error) throw error;
}

async function saveAnalysisToSupabase(data) {
  const { error } = await supabase
    .from('compatibility_history')
    .insert(data);
  
  if (error) throw error;
}

async function updateProfileToSupabase(data) {
  const { error } = await supabase
    .from('profiles')
    .update(data)
    .eq('id', data.id);
  
  if (error) throw error;
}

async function deleteAnalysisFromSupabase(data) {
  const { error } = await supabase
    .from('compatibility_history')
    .delete()
    .eq('id', data.id);
  
  if (error) throw error;
}

/**
 * Sauvegarde la queue dans AsyncStorage
 */
async function saveQueue() {
  try {
    await AsyncStorage.setItem('sync_queue', JSON.stringify(syncQueue));
  } catch (error) {
    console.error('[Sync] Erreur save queue:', error);
  }
}

/**
 * Charge la queue depuis AsyncStorage
 */
async function loadQueue() {
  try {
    const stored = await AsyncStorage.getItem('sync_queue');
    if (stored) {
      syncQueue = JSON.parse(stored);
      console.log(`[Sync] Queue loaded: ${syncQueue.length} actions`);
      
      // Process si online
      if (isOnline) {
        processQueue();
      }
    }
  } catch (error) {
    console.error('[Sync] Erreur load queue:', error);
  }
}

/**
 * Retourne l'état connexion actuel
 */
export function getConnectionStatus() {
  return isOnline;
}

/**
 * Retourne le nombre d'actions en attente
 */
export function getPendingActionsCount() {
  return syncQueue.length;
}

/**
 * Force le traitement de la queue (pour bouton "Sync now")
 */
export async function forceSyncNow() {
  if (!isOnline) {
    throw new Error('Pas de connexion internet');
  }
  
  await processQueue();
}

/**
 * Nettoie la queue (pour debug ou reset)
 */
export async function clearQueue() {
  syncQueue = [];
  await saveQueue();
  console.log('[Sync] Queue cleared');
}

export default {
  initSyncService,
  addConnectivityListener,
  queueAction,
  getConnectionStatus,
  getPendingActionsCount,
  forceSyncNow,
  clearQueue,
};

