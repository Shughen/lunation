/**
 * Configuration Sentry pour le monitoring d'erreurs
 */

import * as Sentry from 'sentry-expo';
import Constants from 'expo-constants';

// Initialiser Sentry
export function initSentry() {
  const sentryDsn = Constants.expoConfig?.extra?.sentryDsn;

  if (!sentryDsn || sentryDsn.includes('YOUR_SENTRY_DSN')) {
    console.warn('⚠️ Sentry DSN not configured. Error monitoring disabled.');
    return;
  }

  Sentry.init({
    dsn: sentryDsn,
    enableInExpoDevelopment: false,
    debug: __DEV__,
    environment: __DEV__ ? 'development' : 'production',
    
    // Taux d'échantillonnage des erreurs (100% par défaut)
    sampleRate: 1.0,
    
    // Taux d'échantillonnage des traces de performance
    tracesSampleRate: __DEV__ ? 1.0 : 0.2,
    
    // Avant d'envoyer l'événement à Sentry
    beforeSend(event, _hint) {
      // Filtrer les erreurs en développement
      if (__DEV__) {
        console.log('🐛 Sentry event (dev):', event);
        return null;
      }

      // Ajouter des informations contextuelles
      event.tags = {
        ...event.tags,
        app_version: Constants.expoConfig?.version,
        platform: Constants.platform?.ios ? 'ios' : 'android',
      };

      return event;
    },

    // Intégrations
    integrations: [
      new Sentry.Native.ReactNativeTracing({
        // Options de tracing
        tracingOrigins: ['localhost', 'astro-ia.com', /^\//],
        routingInstrumentation: new Sentry.Native.RoutingInstrumentation(),
      }),
    ],
  });
}

// Capturer une erreur manuellement
export function captureError(error, context = {}) {
  if (__DEV__) {
    console.error('🐛 Error:', error, context);
    return;
  }

  Sentry.Native.captureException(error, {
    contexts: {
      custom: context,
    },
  });
}

// Capturer un message
export function captureMessage(message, level = 'info', context = {}) {
  if (__DEV__) {
    console.log(`📝 Message (${level}):`, message, context);
    return;
  }

  Sentry.Native.captureMessage(message, {
    level,
    contexts: {
      custom: context,
    },
  });
}

// Définir l'utilisateur connecté
export function setUser(user) {
  if (!user) {
    Sentry.Native.setUser(null);
    return;
  }

  Sentry.Native.setUser({
    id: user.id,
    email: user.email,
    username: user.name,
  });
}

// Définir un contexte personnalisé
export function setContext(key, value) {
  Sentry.Native.setContext(key, value);
}

// Ajouter un breadcrumb (fil d'Ariane)
export function addBreadcrumb(message, category = 'custom', level = 'info', data = {}) {
  Sentry.Native.addBreadcrumb({
    message,
    category,
    level,
    data,
  });
}

// Wrapper pour capturer les erreurs dans les fonctions async
export function withSentryAsync(fn) {
  return async (...args) => {
    try {
      return await fn(...args);
    } catch (error) {
      captureError(error, {
        function: fn.name,
        args: JSON.stringify(args),
      });
      throw error;
    }
  };
}

export default Sentry;

