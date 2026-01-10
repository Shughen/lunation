# Astro.IA — Feuille de route & Guide de développement

## 🎯 Vision du projet

**Astro.IA** est une application mobile Expo/React Native combinant :  
- **Astrologie moderne** : profil natal, compatibilités, transits.  
- **IA** : génération de textes, journaux guidés, conseils personnalisés.  
- **UX premium** : interface fluide, mystique et minimaliste.

> Cible : iOS & Android via Expo Go (développement) puis EAS (production).

---

## ⚙️ Stack technique

- **Expo SDK 54**, **React Native 0.81**, **expo-router 6**
- UI : `react-native`, `@expo/vector-icons`, `expo-linear-gradient`
- État local : **Zustand**, AsyncStorage
- Backend (futur) : **Supabase** ou **Firebase**
- IA (futur) : API OpenAI / Anthropic via proxy Cloudflare Workers ou Vercel

---

## 🚀 Lancement du projet

```bash
# Installer les dépendances
npm install

# Lancer avec tunnel (utile sur iPhone)
npx expo start --tunnel
```

---

## 🧩 Structure du projet (expo-router)

```
app/
  _layout.js              # Layout racine
  index.js                # Redirige vers /home
  (tabs)/
    _layout.js            # Bottom tabs
    home.js               # Accueil (CTA “Découvrir mon profil astral”)
    profile.js            # Profil utilisateur
    chat.js               # Chat IA (placeholder)
  (auth)/                 # (Sprint 3) login / onboarding
  journal/                # (Sprint 2) journal guidé
lib/
  theme.ts                # Palette, spacing, typo
  store.ts                # Zustand store
  api/
    index.ts              # (Sprint 4+) Helpers réseau
assets/
  fonts/
  images/
```

---

## 🎨 Design system

| Élément | Valeur |
|----------|---------|
| **Fond** | `#0B1020 → #1A1440` (dégradé bleu nuit/violet) |
| **Primaire** | `#8B5CF6` |
| **Accent** | `#EAB308` |
| **Texte** | `#EDEDED` |
| **Muted** | `#9AA3B2` |
| **Fonts** | Inter ou Montserrat |
| **Radii** | 12 / 20 |
| **Espaces (px)** | 4, 8, 12, 16, 24 |

---

## 🧱 Sprints & étapes

### ✅ Sprint 1 — *Skeleton & Navigation*
**Objectif** : base de navigation et 3 onglets.  
- [ ] Créer `(tabs)/_layout.js` avec `Tabs` (Home, Profile, Chat)
- [ ] `index.js` redirige vers `/home`
- [ ] `home.js` : CTA “Découvrir mon profil astral”
- [ ] `profile.js`, `chat.js` : placeholders
- [ ] `lib/theme.ts` : couleurs, spacing, typo

**Prompt pour Cursor :**
> Crée la structure de navigation avec Expo Router :  
> - `Tabs` avec Home, Profile, Chat.  
> - `home.js` : fond dégradé, bouton CTA “Découvrir mon profil astral”.  
> - `profile.js` et `chat.js` : placeholders.  
> - `lib/theme.ts` : palette et helpers.  
> - Aucun warning Metro.

---

### 🚀 Sprint 2 — *Journal & stockage local*
**Objectif** : journal d’humeur local.  
- [ ] Installer `@react-native-async-storage/async-storage` & Zustand  
- [ ] `journal/index.js` : liste d’entrées  
- [ ] `journal/new.js` : formulaire simple  
- [ ] Persistance dans AsyncStorage

**Prompt Cursor :**
> Implémente un module Journal :  
> - Création et affichage d’entrées (Zustand + AsyncStorage).  
> - Interface conforme au thème.  
> - Bouton d’accès depuis Home.

---

### 🔐 Sprint 3 — *Profil utilisateur minimal*
**Objectif** : saisie des infos de naissance.  
- [ ] Formulaire Nom / Date / Heure / Ville  
- [ ] Persistance (Zustand + AsyncStorage)  
- [ ] Validation basique

**Prompt Cursor :**
> Implémente `profile.js` avec un formulaire pour Nom, Date, Heure, Ville.  
> Sauvegarde locale via Zustand + AsyncStorage.  
> Style conforme au thème et responsive.

---

### 🧠 Sprint 4 — *Chat IA (MVP stub)*
**Objectif** : chat simulé pour UI.  
- [ ] `chat.js` : UI de chat bubble + input  
- [ ] Stub local simulant une réponse IA  
- [ ] Architecture prête pour API future

**Prompt Cursor :**
> Crée un chat basique avec bubbles et champ d’entrée.  
> Réponses simulées via un stub (setTimeout).  
> Prépare l’architecture pour brancher une vraie API plus tard.

---

### ☁️ Sprint 5 — *Backend & IA réelles*
**Objectif** : relier Supabase et proxy IA.  
- [ ] API `/api/generate` (Cloudflare / Vercel)
- [ ] Variables d’environnement (`.env`)  
- [ ] Auth + stockage Supabase

---

## ✅ Standards qualité

- **Imports** absolus (via `jsconfig.json` / `tsconfig.json`)
- **Composants** : simples, réutilisables
- **État** : isolé par module
- **Commit** : `feat:`, `fix:`, `chore:`
- **Branches** : `main`, `feat/<nom>`
- **PR** : petites, commentées
- **Tests manuels** : via Expo Go iPhone
- **0 warning Metro**

---

## 💡 Backlog futur

- Compatibilités astro (“synastry” MVP)
- Mode hors-ligne enrichi
- Thèmes visuels (clair/sombre cosmique)
- Notifications (journal quotidien)
- Export PDF du journal

---

## 📦 Environment

Créer `.env` (non versionné) :
```
EXPO_PUBLIC_API_BASE=https://astro-ia.example.com
```

---

## 🧭 Definition of Done (DoD)

- Fonctionne sur iPhone (Expo Go)
- Aucun warning ni erreur Metro
- Style cohérent avec `theme.ts`
- Code commenté, clair
- Persistance locale OK

---

## ✨ Auteur

Projet Astro.IA — Rémi Beaurain (2025)
