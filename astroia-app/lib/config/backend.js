import Constants from 'expo-constants';

export function getFastApiBaseUrl() {
  const envValue =
    process.env.EXPO_PUBLIC_FASTAPI_URL ||
    process.env.FASTAPI_BASE_URL ||
    Constants.expoConfig?.extra?.fastapiBaseUrl ||
    Constants.manifest2?.extra?.fastapiBaseUrl;

  if (!envValue) {
    console.warn('[BackendConfig] FASTAPI base URL non défini, fallback localhost:8000');
    console.warn('[BackendConfig] ⚠️ ATTENTION: localhost ne fonctionnera pas depuis un device physique !');
    console.warn('[BackendConfig] Pour configurer:');
    console.warn('[BackendConfig]   1. Créez un fichier .env à la racine du projet');
    console.warn('[BackendConfig]   2. Ajoutez: EXPO_PUBLIC_FASTAPI_URL=http://VOTRE_IP_LOCALE:8000');
    console.warn('[BackendConfig]   3. Redémarrez Expo');
    console.warn('[BackendConfig]   Exemple: EXPO_PUBLIC_FASTAPI_URL=http://192.168.1.100:8000');
    return 'http://localhost:8000';
  }

  const cleanedUrl = envValue.trim().replace(/\/+$/, '');
  console.log('[BackendConfig] URL FastAPI utilisée:', cleanedUrl);
  
  // Avertissement si on utilise localhost en développement
  if (__DEV__ && cleanedUrl.includes('localhost') || cleanedUrl.includes('127.0.0.1')) {
    console.warn('[BackendConfig] ⚠️ ATTENTION: Vous utilisez localhost/127.0.0.1');
    console.warn('[BackendConfig] Cela ne fonctionnera PAS depuis un device physique (iPhone/Android)');
    console.warn('[BackendConfig] Utilisez votre IP locale (ex: http://192.168.x.x:8000)');
  }

  return cleanedUrl;
}


