/**
 * Helper pour gérer les erreurs réseau de manière UX-friendly
 * Remplace les messages techniques (502, timeout) par des messages humains
 */

import { Alert } from 'react-native';
import { AxiosError } from 'axios';

/**
 * Formate un message d'erreur humain à partir d'une erreur axios/fetch
 */
export function getHumanErrorMessage(error: any): string {
  // Erreur réseau (backend down, timeout, etc.)
  if (error.code === 'ERR_NETWORK' || error.message === 'Network Error') {
    return 'Le service est temporairement indisponible. Vérifiez votre connexion internet.';
  }

  // Erreur de timeout
  if (error.code === 'ECONNABORTED' || error.message?.includes('timeout')) {
    return 'La requête a pris trop de temps. Veuillez réessayer.';
  }

  // Erreur 502 (Bad Gateway) - provider API down
  if (error.response?.status === 502) {
    return 'Le rapport est temporairement indisponible.';
  }

  // Erreur 500 (Internal Server Error)
  if (error.response?.status === 500) {
    return 'Une erreur serveur est survenue. Veuillez réessayer plus tard.';
  }

  // Erreur 503 (Service Unavailable)
  if (error.response?.status === 503) {
    return 'Le service est temporairement indisponible.';
  }

  // Erreur 404 (Not Found) - cas spécifique
  if (error.response?.status === 404) {
    return 'Contenu non trouvé.';
  }

  // Message générique pour autres erreurs
  return 'Une erreur est survenue. Veuillez réessayer.';
}

/**
 * Affiche un Alert avec message humain et bouton "Réessayer"
 * @param error - Erreur axios/fetch
 * @param onRetry - Callback appelé si l'utilisateur appuie sur "Réessayer"
 * @param customMessage - Message personnalisé (optionnel, sinon utilise getHumanErrorMessage)
 */
export function showNetworkErrorAlert(
  error: any,
  onRetry?: () => void,
  customMessage?: string
): void {
  const message = customMessage || getHumanErrorMessage(error);

  const buttons: any[] = [
    { text: 'OK', style: 'cancel' },
  ];

  if (onRetry) {
    buttons.unshift({
      text: 'Réessayer',
      onPress: onRetry,
      style: 'default',
    });
  }

  Alert.alert(
    'Erreur',
    message,
    buttons,
    { cancelable: true }
  );
}

/**
 * Vérifie si une erreur est une erreur réseau (502, 500, timeout, etc.)
 */
export function isNetworkError(error: any): boolean {
  const status = error.response?.status;
  return (
    status === 502 ||
    status === 500 ||
    status === 503 ||
    error.code === 'ERR_NETWORK' ||
    error.code === 'ECONNABORTED' ||
    error.message === 'Network Error'
  );
}

