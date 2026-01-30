# Guide Test Android - Aspects v4

## ✅ Tests Backend Validés

**Résultats**:
- ✅ 31 tests Python passés (100%)
- ✅ Sextile inclus dans MAJOR_ASPECT_TYPES
- ✅ Orbes variables: 8° standard, 10° luminaires
- ✅ Filtrage fonctionne: 16 aspects affichés vs 6 avant (+166%)

## 📱 Test sur Android/iOS

### Option 1: Expo Go (Recommandé)

```bash
# 1. Lancer l'API backend
cd /Users/remibeaurain/astroia/apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 2. Dans un nouveau terminal, lancer l'app mobile
cd /Users/remibeaurain/astroia/apps/mobile
npm start

# 3. Scanner le QR code avec Expo Go (app sur votre téléphone)
```

### Option 2: Android Studio

```bash
# 1. Lancer l'API backend (même commande)
cd /Users/remibeaurain/astroia/apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 2. Lancer Android Studio
cd /Users/remibeaurain/astroia/apps/mobile
npx expo run:android
```

### Option 3: Build de développement

```bash
# Si les options ci-dessus ne marchent pas
cd /Users/remibeaurain/astroia/apps/mobile
npx expo start --dev-client
```

## 🧪 Test Manuel dans l'App

### Étape 1: Calculer un thème natal

1. Ouvrir l'app
2. Aller dans l'onglet "Profile" ou "Home"
3. Calculer votre thème natal (25/08/1994, 10:30, Paris)

### Étape 2: Vérifier les aspects

1. Aller dans la section "Aspects"
2. **Compter le nombre d'aspects affichés**
3. Vérifier la présence de **sextiles** (symbole ⚹)

### Résultats Attendus

**Avant correction**:
- 6 aspects affichés
- Pas de sextiles

**Après correction**:
- **15-18 aspects affichés** (selon thème natal)
- **Sextiles présents** (⚹)
- Aspects avec orbes jusqu'à 10° si Soleil/Lune impliqué(e)

### Exemples d'aspects à vérifier

Pour votre thème (25/08/1994, 10:30, Paris), vous devriez voir:

**Sextiles** (nouveaux):
- ✅ Soleil-MC (0.1°) ⚹
- ✅ Saturne-Pluton (0.4°) ⚹
- ✅ Lune-MC (0.6°) ⚹
- ✅ Neptune-Pluton (1.9°) ⚹
- ✅ Vénus-MC (2.8°) ⚹
- ✅ Lune-Saturne (3.4°) ⚹
- ✅ Lune-Neptune (5.3°) ⚹

**Autres aspects majeurs**:
- ✅ Soleil-Lune trigone (0.3°) △
- ✅ Saturne-Neptune conjonction (1.5°) ☌
- ✅ Soleil-Vénus conjonction (2.7°) ☌
- ✅ Mars-MC conjonction (3.8°) ☌
- ✅ Mercure-Pluton opposition (6.4°) ☍

**Total attendu**: ~16 aspects

## 🐛 Dépannage

### L'app ne démarre pas

```bash
cd /Users/remibeaurain/astroia/apps/mobile
rm -rf node_modules
npm install
npm start
```

### Erreurs TypeScript

Les modifications TypeScript sont compatibles. Si erreur:
```bash
# Vérifier que les types sont corrects
cat utils/natalChartUtils.ts | grep -A 5 "getMaxOrb"
```

### API non accessible depuis mobile

Si l'app mobile ne peut pas joindre l'API:

1. Vérifier que l'API tourne sur `0.0.0.0:8000` (pas `localhost`)
2. Vérifier l'URL dans `apps/mobile/services/api.ts`
3. Si sur réseau local, utiliser l'IP locale (ex: `http://192.168.1.X:8000`)

### Aspects toujours à 6

Si vous voyez toujours 6 aspects:

1. Vérifier que l'API est bien redémarrée (`uvicorn main:app --reload`)
2. Vider le cache de l'app (force quit + relance)
3. Vérifier les logs de l'API pour voir les requêtes

## 📊 Validation Finale

Prenez une capture d'écran de la section Aspects et vérifiez:

- [ ] Nombre d'aspects ≥ 12
- [ ] Sextiles présents (symbole ⚹)
- [ ] Orbes variés (certains > 6° si luminaires)
- [ ] Aucun aspect mineur (quinconce, semi-carré, etc.)

## 🎯 Checklist Complète

Backend:
- [x] Tests Python passés (31/31)
- [x] Sextile dans MAJOR_ASPECT_TYPES
- [x] Orbes variables implémentées
- [x] Template sextile ajouté

Mobile:
- [x] TypeScript mis à jour
- [x] getMaxOrb() ajoutée
- [x] filterMajorAspectsV4 refactorisé
- [ ] **Test manuel sur appareil** ← À FAIRE

Documentation:
- [x] ASPECT_V4_CORRECTION.md créé
- [x] Guide test Android créé

## 📞 Support

Si problème, vérifier:
1. Logs API: `tail -f logs/api.log` (si configuré)
2. Console mobile: Regarder les erreurs dans Metro bundler
3. Requête réseau: Vérifier que `aspect_version=4` est envoyé

---

**Date**: 2026-01-30
**Status**: ✅ Backend validé, test mobile en attente
