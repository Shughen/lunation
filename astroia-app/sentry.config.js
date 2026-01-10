/**
 * Configuration Sentry pour LUNA
 * Monitoring des erreurs et performance
 * 
 * ⚠️ DÉSACTIVÉ pour Expo Go (module natif)
 * Sera réactivé en production (EAS build)
 */

// import * as Sentry from "@sentry/react-native";

// Temporairement désactivé pour Expo Go
/*
Sentry.init({
  // TODO: Remplacer par ton DSN Sentry.io
  dsn: "https://YOUR_DSN_HERE@o0.ingest.sentry.io/YOUR_PROJECT_ID",
  
  // Environnement
  environment: __DEV__ ? 'development' : 'production',
  
  // Échantillonnage des traces (100% en dev, 20% en prod)
  tracesSampleRate: __DEV__ ? 1.0 : 0.2,
  
  // Activer seulement en production
  enabled: !__DEV__,
  
  // Niveau de debug
  debug: __DEV__,
  
  // Intégrations
  integrations: [
    new Sentry.ReactNativeTracing({
      // Tracer les navigations
      routingInstrumentation: new Sentry.ReactNavigationInstrumentation(),
      
      // Tracer les requêtes fetch
      traceFetch: true,
      traceXHR: true,
      
      // Performance monitoring
      enableNativeFramesTracking: true,
      enableAppStartTracking: true,
    }),
  ],
  
  // Avant d'envoyer un event
  beforeSend(event, hint) {
    // Filtrer les erreurs en développement
    if (__DEV__) {
      console.log('[Sentry] Event captured (not sent in dev):', event);
      return null; // Ne pas envoyer en dev
    }
    
    // Ajouter contexte utilisateur si disponible
    const user = event.user || {};
    event.user = {
      ...user,
      // Ne jamais envoyer d'info sensible
      id: user.id ? `user_${user.id.slice(0, 8)}` : 'anonymous',
    };
    
    return event;
  },
  
  // Avant d'envoyer une breadcrumb
  beforeBreadcrumb(breadcrumb, hint) {
    // Filtrer les breadcrumbs sensibles
    if (breadcrumb.category === 'console' && breadcrumb.message?.includes('password')) {
      return null; // Ne pas log les mots de passe
    }
    
    return breadcrumb;
  },
});

*/

// Export vide pour compatibilité
export default {
  wrap: (Component) => Component,
  captureException: () => {},
};

