# 🚀 Guide de Déploiement LUNA - Beta

**Version:** 2.0.0  
**Date:** 09/11/2025  
**Sprint:** 12 - Beta TestFlight & Play Store

---

## 🎯 Prérequis

### Comptes Requis

1. **Expo Account** (gratuit)
   - URL : https://expo.dev
   - Login : remibeaurain@icloud.com
   - Utilisé pour : EAS Build

2. **Apple Developer** (99$/an)
   - URL : https://developer.apple.com
   - Requis pour : TestFlight, App Store
   - Team ID : À récupérer après inscription

3. **Google Play Console** (25$ one-time)
   - URL : https://play.google.com/console
   - Requis pour : Play Store Internal/Production

4. **Vercel** (gratuit)
   - URL : https://vercel.com
   - Utilisé pour : Landing page

---

## 📦 Étape 1 : Installation EAS CLI

```bash
# Installer EAS CLI globalement
npm install -g eas-cli

# Vérifier installation
eas --version
# Doit afficher : eas-cli/5.x.x

# Login avec ton compte Expo
eas login
# Email : remibeaurain@icloud.com
# Password : [ton mot de passe Expo]

# Vérifier connexion
eas whoami
# Doit afficher : remibeaurain
```

---

## 🍎 Étape 2 : Build iOS (TestFlight)

### 2.1. Créer App sur App Store Connect

1. **Se connecter** : https://appstoreconnect.apple.com
2. **Mes Apps** → Cliquer **+** (en haut à gauche)
3. **Nouvelle App :**
   - Plateformes : iOS
   - Nom : LUNA - Cycle & Cosmos
   - Langue principale : Français (France)
   - Bundle ID : com.astroia.luna (créer si n'existe pas)
   - SKU : luna-cycle-cosmos-001
   - Accès utilisateur : Accès complet
4. **Informations de l'app :**
   - Catégorie : Santé & Forme
   - Sous-titre : Cycle menstruel & astrologie
   - URL confidentialité : https://luna-app.fr/privacy
   - Pays : France (+ autres pays francophones)

### 2.2. Configurer Certificats (EAS le fait automatiquement)

```bash
# EAS gère automatiquement les certificats
# Pas besoin de créer manuellement les provisioning profiles
```

### 2.3. Build iOS avec EAS

```bash
cd /Users/remibeaurain/astroia/astroia-app

# Build preview (pour TestFlight)
eas build --platform ios --profile preview

# Suivre les instructions :
# - Sélectionner compte Apple Developer
# - EAS créera les certificats automatiquement
# - Attendre 10-15 minutes pour le build

# Vérifier status build
eas build:list

# Une fois terminé, télécharger ou submit directement
```

### 2.4. Submit à TestFlight

```bash
# Option A : Submit automatique
eas submit --platform ios

# Option B : Manual upload
# 1. Télécharger IPA depuis EAS
# 2. Upload via Transporter app (Mac)
# 3. Ou via Application Loader
```

### 2.5. Configurer TestFlight

1. **App Store Connect** → Ton app → TestFlight
2. **Sélectionner le build** uploadé
3. **Informations de test beta :**
   - Notes de test : "Première beta LUNA ! Testez le suivi cycle + astrologie IA"
   - Email beta : support@luna-app.fr
   - Instructions testeurs : "Configurez votre cycle dès le premier lancement"
4. **Groupes de testeurs :**
   - Créer groupe "Beta Publique LUNA"
   - Activer "Testeurs externes"
   - Ajouter 10-20 emails testeurs
5. **Soumettre pour review beta** (délai : 24-48h)
6. **Une fois approuvé** : Lien public TestFlight généré

**Lien public sera du type :**
```
https://testflight.apple.com/join/XXXXXXXX
```

---

## 🤖 Étape 3 : Build Android (Play Store)

### 3.1. Créer App sur Google Play Console

1. **Se connecter** : https://play.google.com/console
2. **Créer une application**
   - Nom : LUNA - Cycle & Cosmos
   - Langue par défaut : Français (France)
   - App ou jeu : Application
   - Gratuite ou payante : Gratuite
3. **Tableau de bord** → Remplir sections obligatoires

### 3.2. Configuration App

**Fiche du Play Store :**
1. Principale fiche du Play Store → Configurer
2. Détails de l'app :
   - Nom : LUNA - Cycle & Cosmos
   - Description courte : [copier depuis STORE_METADATA.md]
   - Description complète : [copier depuis STORE_METADATA.md]
3. Graphismes :
   - Icône : 512x512px
   - Visuel de la fonctionnalité : 1024x500px
   - Screenshots : 1080x1920px (minimum 2)
4. Catégorie : Santé & Remise en forme
5. Coordonnées :
   - Email : support@luna-app.fr
   - Site web : https://luna-app.fr
   - Adresse physique : (requis)

**Classification du contenu :**
1. Répondre au questionnaire
2. Public cible : Tous publics (12+)
3. Pas de contenu sensible
4. Données collectées : Avec consentement RGPD

**Politique de confidentialité :**
- URL : https://luna-app.fr/privacy
- (Obligatoire pour app avec données santé)

### 3.3. Build Android avec EAS

```bash
cd /Users/remibeaurain/astroia/astroia-app

# Build production (AAB pour Play Store)
eas build --platform android --profile production

# Attendre 10-15 minutes

# Vérifier status
eas build:list

# Télécharger AAB une fois terminé
```

### 3.4. Upload sur Play Store Internal

```bash
# Option A : Submit automatique (recommandé)
eas submit --platform android

# Option B : Manual upload
# 1. Play Console → Ta app → Version → Internal testing
# 2. Créer une release
# 3. Télécharger le AAB
# 4. Ajouter notes de version
# 5. Déployer
```

### 3.5. Configurer Internal Testing

1. **Play Console** → Ton app → Internal testing
2. **Créer une release**
   - Nom : Beta 2.0.0
   - Notes : "Première version beta LUNA"
3. **Testeurs internes :**
   - Créer liste emails
   - Ajouter 10-20 testeurs
   - Générer lien opt-in
4. **Publier la version** (pas de review pour internal)
5. **Copier le lien de test**

**Lien internal testing sera du type :**
```
https://play.google.com/apps/internaltest/XXXXXXXXXXXXXXXX
```

---

## 🌐 Étape 4 : Landing Page

### 4.1. Créer Dossier Landing

```bash
mkdir -p /Users/remibeaurain/astroia/luna-landing
cd /Users/remibeaurain/astroia/luna-landing

# Init git
git init
git remote add origin https://github.com/Shughen/luna-landing.git
```

### 4.2. Structure Fichiers

```
luna-landing/
├── index.html           # Page d'accueil
├── privacy.html         # Politique confidentialité
├── support.html         # Support & contact
├── style.css           # Styles
├── assets/
│   ├── logo.png        # Logo LUNA
│   ├── app-store-badge.svg
│   ├── google-play-badge.svg
│   └── screenshots/
│       ├── home.png
│       ├── cycle.png
│       ├── dashboard.png
│       ├── chat.png
│       └── natal.png
└── vercel.json         # Config Vercel
```

### 4.3. Créer index.html

(Copier le HTML de STORE_METADATA.md section Landing Page)

### 4.4. Deploy sur Vercel

```bash
cd /Users/remibeaurain/astroia/luna-landing

# Install Vercel CLI si pas déjà fait
npm install -g vercel

# Deploy
vercel

# Questions :
# - Project name: luna-landing
# - Directory: ./
# - Build command: [laisser vide]
# - Output directory: [laisser vide]

# Une fois validé, deploy en production
vercel --prod

# Résultat : URL temporaire (ex: luna-landing.vercel.app)
```

### 4.5. Configurer Domaine Custom

**Si tu as luna-app.fr :**
```bash
# Ajouter domaine dans Vercel
vercel domains add luna-app.fr

# Configurer DNS chez ton registrar :
# A     @      76.76.21.21
# CNAME www    cname.vercel-dns.com
```

**Si pas de domaine :**
- Utiliser URL Vercel temporaire : `luna-landing.vercel.app`
- Ou acheter domaine sur Namecheap/OVH (~10€/an)

---

## 🧪 Étape 5 : Tests Beta

### 5.1. Inviter Testeurs iOS

**Via TestFlight :**
1. App Store Connect → TestFlight → Groupes externes
2. Créer groupe "Beta LUNA"
3. Ajouter emails testeurs (un par ligne)
4. Ou copier lien public TestFlight
5. Envoyer invitations

**Email type :**
```
Objet : 🌙 Invitation Beta LUNA - Cycle & Cosmos

Bonjour,

Tu es invité(e) à tester LUNA en avant-première !

LUNA est une app innovante qui relie ton cycle menstruel et l'astrologie lunaire pour ton bien-être.

🔗 Rejoindre la beta :
[Lien TestFlight]

📱 Instructions :
1. Installe TestFlight depuis l'App Store (si pas déjà fait)
2. Clique sur le lien ci-dessus
3. Accepte l'invitation
4. Télécharge LUNA
5. Configure ton cycle dès le premier lancement

💬 Feedback :
Partage tes impressions à support@luna-app.fr

Merci et bienvenue ! 🌸

L'équipe LUNA
```

### 5.2. Inviter Testeurs Android

**Via Play Store Internal :**
1. Google Play Console → Internal testing
2. Créer liste testeurs
3. Copier lien opt-in
4. Envoyer invitations

**Email type similaire, remplacer le lien**

### 5.3. Collecter Feedback

**Google Form (recommandé) :**
```
Titre : Feedback Beta LUNA 2.0.0

Questions :
1. Sur quelle plateforme ? (iOS / Android)
2. Note globale ? (1-5 étoiles)
3. Qu'as-tu aimé ? (texte libre)
4. Qu'as-tu moins aimé ? (texte libre)
5. Bugs rencontrés ? (texte libre)
6. Fonctionnalité manquante ? (texte libre)
7. Recommanderais-tu LUNA ? (Oui/Non/Peut-être)
8. Email (optionnel pour follow-up)
```

**Lien à partager dans l'app ou par email**

---

## 🔍 Étape 6 : Monitoring Beta

### 6.1. Sentry Dashboard

**Vérifier :**
- Crashes : 0 attendu
- Erreurs : <5% transactions
- Performance : <5s avg response time

**URL :** https://sentry.io/organizations/astroia/projects/luna-app/

### 6.2. Mixpanel Analytics (si opt-in)

**Métriques clés :**
```sql
-- D1 Retention
SELECT COUNT(DISTINCT user_id) 
FROM events 
WHERE event = 'app_open' 
AND date = CURRENT_DATE - 1

-- Events par user
SELECT user_id, COUNT(*) as events
FROM events
WHERE date >= CURRENT_DATE - 7
GROUP BY user_id
ORDER BY events DESC
```

### 6.3. Supabase Logs

**Tables à monitorer :**
```sql
-- Consentements accordés
SELECT COUNT(*) FROM consents_audit 
WHERE status = 'granted' 
AND created_at >= NOW() - INTERVAL '7 days';

-- Analyses créées
SELECT COUNT(*) FROM compatibility_history 
WHERE created_at >= NOW() - INTERVAL '7 days';

-- Utilisateurs actifs
SELECT COUNT(DISTINCT user_id) FROM chat_messages 
WHERE created_at >= NOW() - INTERVAL '7 days';
```

---

## ✅ Checklist Déploiement

### Avant Build
- [x] Code commit + push sur main
- [x] Tests passent (npm test)
- [x] Aucune erreur linter
- [x] app.json configuré
- [x] eas.json configuré
- [ ] Assets créés (icon, splash)
- [x] Secrets configurés

### iOS Build
- [ ] Apple Developer account actif
- [ ] App créée sur App Store Connect
- [ ] Build EAS iOS lancé
- [ ] Build réussi (pas d'erreurs)
- [ ] IPA uploadé automatiquement
- [ ] Build visible dans TestFlight
- [ ] Compliance beta remplie
- [ ] Beta review soumise (24-48h)

### Android Build
- [ ] Google Play Console account actif
- [ ] App créée sur Play Console
- [ ] Classification contenu remplie
- [ ] Build EAS Android lancé
- [ ] Build réussi (pas d'erreurs)
- [ ] AAB uploadé sur Internal testing
- [ ] Release publiée (instant, pas de review)
- [ ] Lien internal testing copié

### Landing Page
- [ ] Repo luna-landing créé
- [ ] index.html + style.css créés
- [ ] Assets téléchargés (badges stores)
- [ ] Deploy Vercel réussi
- [ ] Domaine luna-app.fr configuré (ou URL Vercel)
- [ ] Privacy policy accessible
- [ ] Support email actif

### Testeurs Beta
- [ ] 10+ invitations iOS envoyées
- [ ] 10+ invitations Android envoyées
- [ ] Instructions claires partagées
- [ ] Google Form feedback créé
- [ ] Lien feedback partagé

---

## 🐛 Troubleshooting

### Build iOS Échoue

**Erreur : "No valid code signing certificates"**
```bash
# Solution : EAS créera automatiquement
# S'assurer d'être connecté au bon Apple ID
eas build --platform ios --profile preview --clear-credentials
```

**Erreur : "Bundle identifier already exists"**
```
Solution : Changer dans app.json
"bundleIdentifier": "com.astroia.luna2"
```

**Erreur : "Provisioning profile expired"**
```bash
# Régénérer les certificats
eas build --platform ios --profile preview --clear-credentials
```

---

### Build Android Échoue

**Erreur : "Keystore not found"**
```bash
# EAS créera automatiquement un keystore
eas build --platform android --profile production
# Accepter la création automatique
```

**Erreur : "Package name already in use"**
```
Solution : Changer dans app.json
"package": "com.astroia.luna2"
```

---

### Submit Échoue

**iOS : "Missing compliance information"**
```
Solution : App Store Connect → Ton app → General → App Privacy
Remplir le questionnaire de conformité encryption
```

**Android : "Missing privacy policy"**
```
Solution : Play Console → Politique de confidentialité
Ajouter URL : https://luna-app.fr/privacy
```

---

## 📊 Timeline Déploiement

| Étape | Durée | Status |
|-------|-------|--------|
| Configuration EAS | 1h | ✅ |
| Création assets | 2-3h | ⏳ |
| Build iOS | 15min | ⏳ |
| Build Android | 15min | ⏳ |
| Submit iOS TestFlight | 5min | ⏳ |
| Submit Android Internal | 5min | ⏳ |
| Review beta iOS | 24-48h | ⏳ |
| Publish Android | Instant | ⏳ |
| Landing page | 2-3h | ⏳ |
| Invitations testeurs | 30min | ⏳ |
| **Total** | **~2-3 jours** | ⏳ |

---

## 🎯 Commandes Complètes

### Build Both Platforms
```bash
# Build iOS + Android simultanément
eas build --platform all --profile production

# Submit both
eas submit --platform ios
eas submit --platform android
```

### Monitoring
```bash
# Voir tous les builds
eas build:list

# Voir détails d'un build
eas build:view [BUILD_ID]

# Voir logs en temps réel
eas build:view [BUILD_ID] --json

# Cancel un build
eas build:cancel [BUILD_ID]
```

### Updates OTA (Over-The-Air)
```bash
# Pour les updates mineurs (pas besoin de rebuild)
eas update --branch production --message "Fix bugs critiques"

# Les users avec l'app recevront l'update au prochain lancement
```

---

## 🚀 Post-Déploiement

### Semaine 1 Beta
- [ ] Envoyer invitations (20+ testeurs)
- [ ] Monitorer crashes Sentry
- [ ] Collecter feedback (Google Form)
- [ ] Identifier bugs bloquants
- [ ] Hotfix si critique

### Semaine 2 Beta
- [ ] Analyser métriques (retention, crashes)
- [ ] Itérer si nécessaire (beta 2.0.1)
- [ ] Valider KPIs (D7 retention >30%)
- [ ] Préparer production publique

---

## ✅ Success Criteria Beta

**Pour passer en production :**
- Crash rate <1% (Sentry)
- D7 Retention >30% (Mixpanel)
- Feedback score >4/5 (Survey)
- 0 bugs bloquants (GitHub Issues)
- 20+ testeurs actifs

**Si critères atteints → Sprint 13 : Production publique ! 🎉**

---

**Prêt à déployer LUNA ! 🚀**

**Prochaines commandes :**
```bash
# 1. Build iOS
eas build --platform ios --profile preview

# 2. Build Android
eas build --platform android --profile production

# 3. Submit
eas submit --platform ios
eas submit --platform android
```

Bonne chance ! 💪

