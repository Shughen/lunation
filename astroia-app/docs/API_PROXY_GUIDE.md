# 🚀 Guide de déploiement de l'API Proxy IA

Ce guide explique comment déployer l'API proxy pour l'IA sur Vercel.

## 📁 Structure de l'API

Créez un nouveau dossier séparé pour l'API (ou dans le même repo) :

```
astro-ia-api/
├── api/
│   └── generate.js      # Endpoint principal
├── package.json
├── vercel.json
└── .env.local          # Clés API (local uniquement)
```

## 📝 Fichiers à créer

### 1. `package.json`

```json
{
  "name": "astro-ia-api",
  "version": "1.0.0",
  "type": "module",
  "dependencies": {
    "openai": "^4.20.1"
  }
}
```

### 2. `vercel.json`

```json
{
  "version": 2,
  "functions": {
    "api/**/*.js": {
      "memory": 1024,
      "maxDuration": 30
    }
  },
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Credentials", "value": "true" },
        { "key": "Access-Control-Allow-Origin", "value": "*" },
        { "key": "Access-Control-Allow-Methods", "value": "GET,POST,OPTIONS" },
        { "key": "Access-Control-Allow-Headers", "value": "Content-Type, Authorization" }
      ]
    }
  ]
}
```

### 3. `api/generate.js`

```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Système prompt astrologique
const ASTRO_SYSTEM_PROMPT = `Tu es un assistant astrologique expert et bienveillant.
Tu combines connaissances traditionnelles et approche moderne de l'astrologie.
Tu réponds de manière claire, empathique et personnalisée.
Tu utilises des emojis cosmiques quand approprié : ✨🌙⭐🔮💫`;

export default async function handler(req, res) {
  // CORS preflight
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { messages, userProfile } = req.body;

    if (!messages || !Array.isArray(messages)) {
      return res.status(400).json({ error: 'Messages array required' });
    }

    // Enrichir le contexte avec le profil utilisateur si disponible
    let contextualizedMessages = [...messages];
    if (userProfile) {
      const profileContext = `Contexte utilisateur: ${userProfile.name || 'Utilisateur'}, né(e) le ${userProfile.birthDate || 'date inconnue'}, signe ${userProfile.zodiacSign || 'inconnu'}.`;
      contextualizedMessages = [
        { role: 'system', content: ASTRO_SYSTEM_PROMPT + '\n\n' + profileContext },
        ...messages
      ];
    } else {
      contextualizedMessages = [
        { role: 'system', content: ASTRO_SYSTEM_PROMPT },
        ...messages
      ];
    }

    // Appel à OpenAI
    const completion = await openai.chat.completions.create({
      model: 'gpt-4o-mini', // Ou gpt-3.5-turbo pour moins cher
      messages: contextualizedMessages,
      temperature: 0.7,
      max_tokens: 500,
    });

    const response = completion.choices[0].message;

    return res.status(200).json({
      message: response.content,
      usage: completion.usage,
    });

  } catch (error) {
    console.error('API Error:', error);
    return res.status(500).json({
      error: 'Internal server error',
      details: error.message
    });
  }
}
```

## 🚀 Déploiement sur Vercel

### Étape 1 : Créer le projet

1. Va sur [vercel.com](https://vercel.com)
2. Connecte ton compte GitHub
3. Importe le projet (ou crée un nouveau repo)

### Étape 2 : Configurer les variables d'environnement

Dans les paramètres Vercel (Settings > Environment Variables) :

```
OPENAI_API_KEY=sk-votre-cle-openai
```

### Étape 3 : Déployer

```bash
# Installer Vercel CLI (optionnel)
npm i -g vercel

# Déployer
vercel --prod
```

### Étape 4 : Obtenir l'URL

Après le déploiement, tu obtiendras une URL comme :
```
https://astro-ia-api.vercel.app
```

### Étape 5 : Tester

```bash
curl -X POST https://astro-ia-api.vercel.app/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Parle-moi du signe du Lion"}
    ]
  }'
```

## 📱 Intégration dans l'app

Une fois déployée, mets à jour `app.json` :

```json
{
  "extra": {
    "aiApiUrl": "https://astro-ia-api.vercel.app/api/generate"
  }
}
```

## 🔒 Sécurité (optionnel)

Pour sécuriser l'API, ajoute une clé API simple :

```javascript
// Dans api/generate.js
const API_KEY = process.env.API_SECRET_KEY;

if (req.headers.authorization !== `Bearer ${API_KEY}`) {
  return res.status(401).json({ error: 'Unauthorized' });
}
```

Puis dans l'app :

```javascript
fetch(apiUrl, {
  headers: {
    'Authorization': 'Bearer votre-cle-secrete'
  }
})
```

## 💡 Alternative : Anthropic Claude

Pour utiliser Claude à la place d'OpenAI :

```javascript
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

const message = await anthropic.messages.create({
  model: 'claude-3-sonnet-20240229',
  max_tokens: 500,
  messages: contextualizedMessages,
});
```

---

**C'est prêt ! Tu peux déployer l'API maintenant ! 🚀**

