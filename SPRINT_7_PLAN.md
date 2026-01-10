# 🌟 SPRINT 7 - HOROSCOPE QUOTIDIEN IA

**Date :** 5 novembre 2025  
**Objectif :** Créer un horoscope quotidien personnalisé avec IA

---

## 🎯 OBJECTIFS

Implémenter un horoscope quotidien intelligent qui :
- Se base sur le signe solaire de l'utilisateur
- Génère des prédictions via GPT-3.5-turbo
- Intègre les transits planétaires du jour
- Est renouvelé chaque jour à minuit
- Est stocké en cache pour éviter les appels répétés

---

## 📋 TÂCHES

### 1. Backend - Service Horoscope ✨
- [ ] Créer `lib/api/horoscopeService.js`
- [ ] Fonction `getDailyHoroscope(sign, date)`
- [ ] Cache avec AsyncStorage (1 horoscope/jour/signe)
- [ ] Appel API GPT-3.5 avec prompt astrologique
- [ ] Intégration transits planétaires du jour

### 2. UI - Écran Horoscope 🎨
- [ ] Améliorer `app/horoscope/index.js`
- [ ] Card Hero avec signe + date du jour
- [ ] 4 sections :
  - 💼 Travail & Carrière
  - ❤️ Amour & Relations
  - 💪 Santé & Bien-être
  - ✨ Conseil du jour
- [ ] Indicateur "Dernière mise à jour"
- [ ] Bouton "Rafraîchir" (si +24h)

### 3. Animation & UX 🎬
- [ ] Animation fadeIn au chargement
- [ ] Skeleton loader pendant la génération
- [ ] Particle effect cosmique en arrière-plan
- [ ] Swipe pour voir horoscope de demain/hier

### 4. Personnalisation 🧠
- [ ] Intégrer les données du profil utilisateur
- [ ] Mentionner la Lune actuelle
- [ ] Adapter selon l'ascendant si disponible
- [ ] Numéro chance du jour (random seed = date)

### 5. Stockage & Cache 💾
- [ ] Table Supabase `daily_horoscopes`
- [ ] Cache AsyncStorage (key: `horoscope_${sign}_${date}`)
- [ ] Invalidation automatique à minuit
- [ ] Historique des 7 derniers jours

### 6. Notifications (Optionnel) 🔔
- [ ] Push notification à 8h du matin
- [ ] "Votre horoscope du jour est prêt !"
- [ ] Deep link vers /horoscope

---

## 🎨 DESIGN

### Palette Horoscope
- Dégradé aube : `['#FF6B9D', '#C239B3', '#4E54C8']`
- Accent doré : `#F59E0B`
- Cards semi-transparentes

### Structure
```
┌─────────────────────────┐
│   🌅 Horoscope du Jour  │
│   Lundi 5 novembre      │
├─────────────────────────┤
│   ♌ Lion                │
│   "Aujourd'hui..."      │
├─────────────────────────┤
│ 💼 Travail & Carrière   │
│ [Texte IA]              │
├─────────────────────────┤
│ ❤️ Amour & Relations    │
│ [Texte IA]              │
├─────────────────────────┤
│ 💪 Santé & Bien-être    │
│ [Texte IA]              │
├─────────────────────────┤
│ ✨ Conseil du jour      │
│ [Texte IA]              │
├─────────────────────────┤
│ 🍀 Numéro chance : 7    │
│ 🌙 Lune en Gémeaux      │
└─────────────────────────┘
```

---

## 🤖 PROMPT GPT-3.5

```
Tu es un astrologue professionnel expert.

Génère un horoscope quotidien pour le signe {SIGNE}.
Date : {DATE}
Lune actuelle : {MOON_SIGN}

Structure ta réponse en 4 parties :

1. TRAVAIL & CARRIÈRE (50 mots max)
2. AMOUR & RELATIONS (50 mots max)
3. SANTÉ & BIEN-ÊTRE (50 mots max)
4. CONSEIL DU JOUR (30 mots max)

Ton ton : bienveillant, précis, actionnable.
Utilise des métaphores cosmiques.
Sois positif mais réaliste.
```

---

## 📊 TABLES SUPABASE

```sql
CREATE TABLE daily_horoscopes (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  sign VARCHAR(20) NOT NULL,
  date DATE NOT NULL,
  work TEXT NOT NULL,
  love TEXT NOT NULL,
  health TEXT NOT NULL,
  advice TEXT NOT NULL,
  lucky_number INTEGER,
  moon_sign VARCHAR(20),
  created_at TIMESTAMP DEFAULT NOW(),
  
  UNIQUE(sign, date)
);
```

---

## 🚀 ÉTAPES D'IMPLÉMENTATION

1. **Service horoscope** (30 min)
2. **UI écran** (1h)
3. **Intégration API GPT** (30 min)
4. **Cache & stockage** (30 min)
5. **Tests** (30 min)

**Durée totale estimée : 3h**

---

## 🎯 RÉSULTAT FINAL

**Un horoscope quotidien :**
- 🤖 Généré par IA (GPT-3.5)
- 🎨 Design premium
- ⚡ Instantané (cache)
- 📱 Personnalisé (profil utilisateur)
- 💾 Historique 7 jours
- 🔔 Push notification (optionnel)

---

**Prêt à démarrer le Sprint 7 ? 🚀**

