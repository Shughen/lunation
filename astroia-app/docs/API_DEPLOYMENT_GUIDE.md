# 🚀 Guide de déploiement de l'API Astro.IA

Ce guide explique comment déployer l'API proxy sécurisée sur Vercel.

## 📋 Prérequis

- Compte [Vercel](https://vercel.com) (gratuit)
- Clé API [OpenAI](https://platform.openai.com/api-keys)
- Clé Service Role Supabase (Dashboard → Settings → API)

---

## 📁 Structure de l'API

L'API est dans le dossier `/Users/remibeaurain/astroia/astro-ia-api/` :

```
astro-ia-api/
├── api/
│   └── ai/
│       └── chat.ts           # Endpoint principal
├── package.json
├── vercel.json              # Configuration Vercel
├── tsconfig.json            # Configuration TypeScript
└── .env.local               # Variables locales (à créer)
```

---

## 🔧 Installation locale

### 1. Créer `.env.local`

Dans le dossier `astro-ia-api/`, créez `.env.local` :

```bash
# OpenAI
OPENAI_API_KEY=sk-proj-VOTRE_CLE_ICI

# Supabase
SUPABASE_URL=https://tirfwrwgyzsfrdhtidug.supabase.co
SUPABASE_SERVICE_ROLE=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.VOTRE_SERVICE_ROLE_KEY
```

⚠️ **La clé Service Role est PRIVÉE** - ne JAMAIS l'exposer côté client !

### 2. Installer les dépendances

```bash
cd /Users/remibeaurain/astroia/astro-ia-api
npm install
```

### 3. Tester localement

```bash
npm run dev
```

L'API sera disponible sur `http://localhost:3000`

### 4. Tester avec curl

```bash
curl -X POST http://localhost:3000/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "messages": [
      {"role": "user", "content": "Parle-moi du signe du Lion"}
    ]
  }'
```

---

## 🚀 Déploiement sur Vercel

### Méthode 1 : CLI Vercel (Recommandée)

```bash
# Installer Vercel CLI
npm i -g vercel

# Se connecter
vercel login

# Déployer
cd /Users/remibeaurain/astroia/astro-ia-api
vercel --prod
```

### Méthode 2 : GitHub + Vercel Dashboard

1. Créer un repo GitHub pour `astro-ia-api`
2. Push le code
3. Aller sur [vercel.com/new](https://vercel.com/new)
4. Importer le repo
5. Configurer les variables d'environnement (voir ci-dessous)
6. Déployer

---

## 🔐 Configuration des variables d'environnement

Dans Vercel Dashboard → Settings → Environment Variables :

| Variable | Valeur | Scope |
|----------|--------|-------|
| `OPENAI_API_KEY` | `sk-proj-...` | Production + Preview |
| `SUPABASE_URL` | `https://tirfwrwgyzsfrdhtidug.supabase.co` | Production + Preview |
| `SUPABASE_SERVICE_ROLE` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` | Production + Preview |

⚠️ **Redéployer après avoir ajouté les variables !**

---

## 📱 Configuration de l'app mobile

Une fois l'API déployée, récupère l'URL (ex: `https://astro-ia-api.vercel.app`)

### Mettre à jour `app.json`

```json
{
  "extra": {
    "aiApiUrl": "https://astro-ia-api.vercel.app/api/ai/chat"
  }
}
```

### Redémarrer l'app

```bash
cd /Users/remibeaurain/astroia/astroia-app
npx expo start --clear
```

---

## 🧪 Tests complets

### Test 1 : Santé de l'API

```bash
curl https://astro-ia-api.vercel.app/api/ai/chat \
  -X OPTIONS
```

Doit retourner `200 OK`

### Test 2 : Requête simple

```bash
curl -X POST https://astro-ia-api.vercel.app/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "00000000-0000-0000-0000-000000000000",
    "messages": [
      {"role": "user", "content": "Quelle est la particularité du signe du Bélier ?"}
    ]
  }'
```

### Test 3 : Avec profil astro

```bash
curl -X POST https://astro-ia-api.vercel.app/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "00000000-0000-0000-0000-000000000000",
    "messages": [
      {"role": "user", "content": "Comment gérer mon stress ?"}
    ],
    "astroProfile": {
      "name": "Rémi",
      "birthDate": "1990-05-15",
      "zodiacSign": "Taureau",
      "zodiacElement": "Terre"
    }
  }'
```

---

## 📊 Monitoring

### Logs Vercel

Dashboard → Deployments → Logs

### Erreurs courantes

| Erreur | Cause | Solution |
|--------|-------|----------|
| `401 Unauthorized` | Clé OpenAI invalide | Vérifier `OPENAI_API_KEY` |
| `429 Too Many Requests` | Rate limit OpenAI | Attendre ou upgrade plan |
| `500 Internal Server Error` | Erreur serveur | Voir les logs Vercel |
| `CORS error` | Config CORS | Vérifier `vercel.json` |

---

## 💰 Coûts

### OpenAI (gpt-4o-mini)

- Input : ~$0.15 / 1M tokens
- Output : ~$0.60 / 1M tokens
- Estimation : ~$0.001 par message

### Vercel

- Plan gratuit : 100GB bandwidth/mois
- Fonctions : 100h/mois
- Largement suffisant pour démarrer

### Supabase

- Plan gratuit : 500MB DB, 1GB bandwidth
- Upgrade si dépassement

---

## 🔒 Sécurité

### ✅ Bonnes pratiques

- Service Role **JAMAIS** exposée côté client
- Variables d'environnement dans Vercel
- Validation avec Zod
- Rate limiting (à implémenter)
- CORS configuré

### ⚠️ À implémenter plus tard

- Rate limiting par user
- Authentication header
- Webhook Stripe pour paiements
- Monitoring avec Sentry

---

## 🚀 Mise en production

### Checklist

- [ ] API déployée sur Vercel
- [ ] Variables d'environnement configurées
- [ ] Tests passés
- [ ] App mobile mise à jour avec l'URL
- [ ] Testée sur device réel
- [ ] Logs vérifiés
- [ ] Budget OpenAI configuré

---

## 📚 Ressources

- [Vercel Docs](https://vercel.com/docs)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Supabase Service Role](https://supabase.com/docs/guides/api#the-service_role-key)

---

**Ton API est maintenant prête ! 🎉**

Coût estimé : **< $5/mois** pour 1000 messages

