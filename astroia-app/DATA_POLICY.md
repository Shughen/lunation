# 🔐 POLITIQUE DE CONFIDENTIALITÉ – LUNA - Cycle & Cosmos

**Dernière mise à jour : 9 novembre 2025**

---

## 📋 Introduction

LUNA - Cycle & Cosmos ("nous", "notre", "l'application") respecte votre vie privée et s'engage à protéger vos données personnelles.

Cette politique explique :
- Quelles données nous collectons
- Comment nous les utilisons
- Comment nous les protégeons
- Vos droits concernant vos données

---

## 📊 Données Collectées

### ⚠️ Données de Santé (Art. 9 RGPD)

**Base légale :** Consentement explicite (Art. 6.1.a + Art. 9.2.a RGPD)

Les données de cycle menstruel sont considérées comme **données de santé** selon le RGPD. Nous collectons ces données UNIQUEMENT avec ton consentement explicite donné lors de l'onboarding.

**Ce que nous collectons :**
- **Dates des règles** : Date de début de chaque période
- **Phase du cycle** : Calculée automatiquement (Menstruelle, Folliculaire, Ovulation, Lutéale)
- **Durée moyenne du cycle** : Renseignée par toi (21-35 jours)
- **Symptômes et notes** : Saisis volontairement (optionnel)
- **Humeur quotidienne** : Liée à la phase du cycle

**Finalité exclusive :** Suivi personnel de ton cycle et génération de recommandations bien-être personnalisées.

**Tu peux retirer ton consentement à tout moment** dans Settings > Confidentialité (entraînera suppression de toutes tes données).

### Données de Profil
- **Informations personnelles** : Nom, email, date de naissance
- **Informations astrologiques** : Heure et lieu de naissance (optionnel)
- **Signe zodiacal** : Calculé automatiquement

### Données du Journal
- **Humeur quotidienne** : Sélectionnée par vous
- **Notes personnelles** : Texte libre
- **Tags** : Catégories choisies
- **Phase du cycle** : Enregistrée automatiquement au moment de l'entrée

### Données d'Utilisation
- **Interactions avec l'IA** : Conversations avec l'assistant
- **Navigation** : Pages visitées, fonctionnalités utilisées
- **Événements analytiques** : Via Mixpanel (anonymisé)
- **Crashs et erreurs** : Via Sentry (technique uniquement)

### Données Techniques
- **Appareil** : Type, système d'exploitation, version
- **Connexion** : Adresse IP (temporaire)
- **Identifiants** : UUID généré localement

---

## 🎯 Utilisation des Données

Nous utilisons vos données uniquement pour :

### Fonctionnalités Core
- ✅ Calculer votre thème astral
- ✅ Estimer vos phases de cycle
- ✅ Corréler cycle et transits lunaires
- ✅ Personnaliser les recommandations IA
- ✅ Afficher votre historique et statistiques

### Amélioration du Service
- ✅ Analyser l'utilisation (anonyme)
- ✅ Corriger les bugs
- ✅ Améliorer l'expérience utilisateur

### Communication
- ✅ Emails importants (réinitialisation mot de passe, changements T&C)
- ✅ Notifications push (si activées par vous)

**Nous ne vendons JAMAIS vos données à des tiers.**

---

## 🔒 Protection des Données

### Sécurité Technique

**Backend (Supabase) :**
- ✅ Chiffrement en transit (HTTPS/TLS)
- ✅ Chiffrement au repos (AES-256)
- ✅ Row Level Security (RLS) : chaque utilisatrice accède uniquement à ses propres données
- ✅ Authentification sécurisée (Magic Link)

**API (Vercel) :**
- ✅ Proxy sécurisé pour OpenAI (clé jamais exposée)
- ✅ Validation des entrées
- ✅ Rate limiting

**Application Mobile :**
- ✅ AsyncStorage sécurisé (local)
- ✅ Pas de clés API en clair
- ✅ Validation côté client et serveur

### Accès Limité
Seuls les développeurs autorisés ont accès aux données techniques (logs d'erreurs, métriques anonymes).

**Aucun humain ne lit vos journaux ou conversations IA sans votre consentement explicite.**

---

## 🌍 Partage des Données & Sous-Traitants

### Avec Qui Nous Partageons

**Services Techniques (Sous-traitants / Data Processors) :**

| Service | Finalité | Localisation | Données traitées | Garanties |
|---------|----------|--------------|------------------|-----------|
| **Supabase** | Stockage BDD | 🇪🇺 Irlande (UE) | Profil, cycle, journal | DPA + Chiffrement AES-256 |
| **Vercel** | Hébergement API | 🇺🇸 USA | Requêtes API (temporaire) | SCC + DPA |
| **OpenAI** | IA conversationnelle | 🇺🇸 USA | Messages anonymisés | SCC + Zero data retention |
| **Mixpanel** | Analytics (opt-in) | 🇺🇸 USA | Événements anonymes | SCC + Opt-out possible |
| **Sentry** | Monitoring erreurs | 🇺🇸 USA | Logs techniques | SCC + No PII |

**Transferts hors UE :**
Conformément à l'Art. 46 RGPD, les transferts vers les USA sont encadrés par :
- ✅ **Clauses Contractuelles Types (SCC)** signées avec tous les sous-traitants US
- ✅ **Data Processing Agreements (DPA)** en vigueur
- ✅ Mesures de sécurité supplémentaires (chiffrement, pseudonymisation)

**Données de santé (cycle) :**
- Stockées EXCLUSIVEMENT en UE (Supabase Irlande)
- JAMAIS transférées hors UE
- JAMAIS envoyées à Mixpanel (analytics opt-in ne collecte pas ces données)

**Aucune de ces entreprises ne peut vendre ou utiliser vos données pour leur propre compte.**

### Qui N'a PAS Accès
❌ Annonceurs  
❌ Réseaux sociaux  
❌ Courtiers en données  
❌ Assurances  
❌ Employeurs  

---

## 🇪🇺 Vos Droits (RGPD)

En tant qu'utilisatrice basée en Europe, vous avez le droit de :

### Accès
📥 **Télécharger toutes vos données** (export JSON/PDF)
- Disponible dans Settings > Confidentialité > Exporter mes données

### Rectification
✏️ **Modifier vos informations** à tout moment
- Depuis Settings > Profil

### Suppression
🗑️ **Supprimer votre compte et toutes vos données**
- Depuis Settings > Compte > Supprimer mon compte
- Suppression effective sous 30 jours

### Portabilité
📤 **Récupérer vos données** dans un format standard (JSON)

### Retrait du Consentement
🚫 **Désactiver les analytics** et notifications
- Depuis Settings > Confidentialité

### Opposition
✋ **Refuser le traitement** pour certaines finalités (analytics)

---

## 🍪 Cookies & Tracking

LUNA n'utilise PAS de cookies web traditionnels.

**Analytics Mobile (Mixpanel) :**
- Collecte anonyme des événements d'usage
- Peut être désactivé dans Settings
- Aucun tracking inter-applications

**Identifiants :**
- UUID généré localement (pas d'IDFA/AAID)
- Pas de tracking publicitaire

---

## 🔔 Notifications Push

Si vous activez les notifications :
- Nous envoyons des rappels cycle (optionnel)
- Nous envoyons des alertes transits lunaires (optionnel)
- Vous pouvez les désactiver à tout moment

**Nous n'envoyons JAMAIS de publicités par notification.**

---

## 🧒 Âge Minimum

LUNA est conçu pour les personnes de **13 ans et plus**.

Si vous avez moins de 13 ans, veuillez ne pas utiliser l'application ou demander le consentement d'un parent.

---

## 📍 Localisation

Nous ne collectons PAS votre localisation en temps réel.

Nous utilisons uniquement :
- Le **lieu de naissance** (saisi manuellement) pour calculer le thème natal
- Le **fuseau horaire** de l'appareil pour afficher les heures correctement

---

## 🕒 Durée de Conservation

**Conformément au principe de minimisation des données (Art. 5 RGPD) :**

| Type de données | Durée de conservation | Base légale | Finalité |
|-----------------|----------------------|-------------|----------|
| **Profil** | Tant que compte actif, ou 3 ans d'inactivité | Consentement | Fonctionnement app |
| **Données de cycle** ⚠️ | Tant que compte actif, ou 3 ans d'inactivité | Consentement (Art. 9) | Suivi personnel |
| **Journal** | Tant que compte actif, ou 3 ans d'inactivité | Consentement | Historique personnel |
| **Conversations IA** | 90 jours max | Intérêt légitime | Amélioration modèle |
| **Logs techniques** | 30 jours max | Intérêt légitime | Débogage & sécurité |
| **Analytics (opt-in)** | 12 mois max | Consentement | Amélioration UX |

**Suppression automatique :**
- Après **3 ans d'inactivité** (aucune connexion), ton compte et toutes tes données sont automatiquement supprimés
- Tu reçois un email d'avertissement **30 jours avant** la suppression automatique

**Suppression manuelle :**
- Après demande de suppression de compte (Settings > Confidentialité), toutes tes données sont effacées sous **30 jours maximum**
- Délai de 7 jours de rétractation (tu peux annuler la suppression pendant cette période)

---

## 🔄 Modifications de la Politique

Nous pouvons mettre à jour cette politique pour refléter :
- Des changements légaux
- De nouvelles fonctionnalités
- Des retours utilisateurs

**En cas de changement majeur**, nous vous préviendrons par :
- Email
- Notification in-app
- Popup au prochain lancement

---

## 📞 Contact & Questions

### Responsable du Traitement (DSA & RGPD)

**LUNA - Cycle & Cosmos**  
**Développeur :** Rémi Beaurain  
**Email :** privacy@luna-app.fr  
**Adresse :** [À compléter avant soumission store]  
**Téléphone :** [À compléter avant soumission store]

**Délégué à la Protection des Données (DPO) :**  
privacy@luna-app.fr

### Réclamations

Si tu estimes que tes droits ne sont pas respectés, tu peux déposer une réclamation auprès de :

**Autorité de Contrôle (France) :**  
CNIL (Commission Nationale de l'Informatique et des Libertés)  
3 Place de Fontenoy, TSA 80715, 75334 Paris Cedex 07  
Téléphone : 01 53 73 22 22  
https://www.cnil.fr/fr/plaintes

---

## 📄 Documents Liés

- [DISCLAIMER.md](./DISCLAIMER.md) - Avertissements médicaux
- [README.md](./README.md) - Documentation technique
- Conditions Générales d'Utilisation (CGU) - À venir

---

## ✅ Résumé

**En bref :**
- 🔐 Vos données sont chiffrées et protégées
- 🚫 Nous ne vendons rien à personne
- 📥 Vous pouvez tout exporter ou supprimer
- 🇪🇺 Conformité RGPD totale
- 💜 Votre bien-être avant tout

---

> **Merci de nous faire confiance avec vos données personnelles.**  
> **Nous prenons cette responsabilité très au sérieux. 🌙**

**Dernière mise à jour : 9 novembre 2025**

