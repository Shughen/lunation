# 🔍 Configuration Sentry - Astro.IA

## 📋 Étapes d'installation

### 1. Créer un compte Sentry

1. Aller sur https://sentry.io
2. Créer un compte (gratuit pour petits projets)
3. Créer un nouveau projet :
   - Platform : **React Native**
   - Project name : **astro-ia-app**
   - Organization : **astro-ia**

### 2. Récupérer le DSN

Après création du projet, copier le **DSN** (Data Source Name) :
```
https://YOUR_KEY@o0.ingest.sentry.io/YOUR_PROJECT_ID
```

### 3. Configurer l'application

**Fichier : `app.json`**

Remplacer le placeholder :
```json
{
  "extra": {
    "sentryDsn": "https://YOUR_SENTRY_DSN@o0.ingest.sentry.io/YOUR_PROJECT_ID"
  }
}
```

Par votre vrai DSN :
```json
{
  "extra": {
    "sentryDsn": "https://abc123def456@o987654.ingest.sentry.io/1234567"
  }
}
```

### 4. Installer les dépendances

```bash
npm install sentry-expo
```

### 5. Initialiser Sentry dans l'app

**Fichier : `app/_layout.js`**

```javascript
import { initSentry } from '@/lib/sentry';

export default function RootLayout() {
  // Initialiser Sentry au démarrage
  useEffect(() => {
    initSentry();
  }, []);

  // ... reste du code
}
```

---

## 🚀 Utilisation

### Capturer une erreur automatiquement

Les erreurs non gérées sont automatiquement capturées :

```javascript
throw new Error('Something went wrong!');
// → Envoyé à Sentry automatiquement
```

### Capturer une erreur manuellement

```javascript
import { captureError } from '@/lib/sentry';

try {
  await riskyOperation();
} catch (error) {
  captureError(error, {
    module: 'compatibility',
    operation: 'analyze',
  });
}
```

### Capturer un message

```javascript
import { captureMessage } from '@/lib/sentry';

captureMessage('User completed onboarding', 'info', {
  userId: '123',
  screens: 3,
});
```

### Définir l'utilisateur connecté

```javascript
import { setUser } from '@/lib/sentry';

// Après login
setUser({
  id: user.id,
  email: user.email,
  name: user.name,
});

// Après logout
setUser(null);
```

### Ajouter un breadcrumb (fil d'Ariane)

```javascript
import { addBreadcrumb } from '@/lib/sentry';

addBreadcrumb('User clicked analyze button', 'user-action', 'info', {
  screen: 'compatibility',
  analysisType: 'parent-child',
});
```

### Wrapper pour fonctions async

```javascript
import { withSentryAsync } from '@/lib/sentry';

const analyzeCompatibility = withSentryAsync(async (data) => {
  // Si une erreur survient, elle sera automatiquement envoyée à Sentry
  const result = await api.analyze(data);
  return result;
});
```

---

## 📊 Dashboard Sentry

Une fois configuré, vous verrez dans le dashboard Sentry :

### Erreurs
- Stack traces complètes
- Contexte de l'utilisateur
- Appareil et OS
- Version de l'app
- Breadcrumbs (historique des actions)

### Performance
- Temps de chargement des écrans
- Durée des requêtes API
- Transactions lentes

### Releases
- Associer les erreurs aux versions
- Voir les nouvelles erreurs par version
- Tendances de stabilité

---

## 🔧 Configuration avancée

### Source Maps (pour stack traces lisibles)

**Fichier : `eas.json`**

```json
{
  "build": {
    "production": {
      "env": {
        "SENTRY_ORG": "astro-ia",
        "SENTRY_PROJECT": "astro-ia-app",
        "SENTRY_AUTH_TOKEN": "YOUR_AUTH_TOKEN"
      }
    }
  }
}
```

Les source maps seront automatiquement uploadées après chaque build.

### Filtrer les erreurs

**Fichier : `lib/sentry.js`**

```javascript
beforeSend(event, hint) {
  // Ignorer certaines erreurs
  if (event.exception?.values?.[0]?.value?.includes('Network request failed')) {
    return null; // Ne pas envoyer
  }
  
  return event;
}
```

### Enrichir les événements

```javascript
import { setContext } from '@/lib/sentry';

// Après une analyse
setContext('last_analysis', {
  type: 'parent-child',
  score: 87,
  timestamp: new Date().toISOString(),
});
```

---

## 🧪 Tester Sentry

### En développement

```javascript
// Forcer l'envoi en dev
import Sentry from '@/lib/sentry';

Sentry.Native.captureMessage('Test message from dev');
```

### En production

1. Builder l'app : `eas build --profile production`
2. Installer l'app
3. Déclencher une erreur volontaire
4. Vérifier le dashboard Sentry

---

## 💰 Pricing Sentry

**Plan gratuit :**
- 5,000 erreurs/mois
- 10,000 transactions de performance/mois
- 1 membre d'équipe
- Rétention des données : 30 jours

**Plan Team ($26/mois) :**
- 50,000 erreurs/mois
- 100,000 transactions/mois
- 5 membres d'équipe
- Rétention : 90 jours
- Alertes personnalisées

---

## 🔒 Sécurité & Confidentialité

### Données sensibles

**Ne jamais envoyer :**
- Mots de passe
- Tokens d'authentification
- Données personnelles sensibles

**Scrubber automatique :**

```javascript
beforeSend(event) {
  // Nettoyer les données sensibles
  if (event.request?.data) {
    delete event.request.data.password;
    delete event.request.data.token;
  }
  return event;
}
```

### RGPD

Ajouter dans la politique de confidentialité :
> "Nous utilisons Sentry pour surveiller la stabilité de l'application et corriger les bugs. Les données d'erreur sont anonymisées et ne contiennent aucune information personnelle identifiable."

---

## 📚 Ressources

- [Documentation Sentry](https://docs.sentry.io/platforms/react-native/)
- [Sentry Expo](https://docs.expo.dev/guides/using-sentry/)
- [Best Practices](https://docs.sentry.io/platforms/react-native/best-practices/)
- [Performance Monitoring](https://docs.sentry.io/platforms/react-native/performance/)

