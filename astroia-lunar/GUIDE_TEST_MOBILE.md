# 🧪 Guide Test Mobile - Génération Claude Opus 4.5

## 🎯 Objectif

Tester l'app mobile en conditions réelles avec :
- ✨ Nouveau loading screen animé
- 🤖 Génération Claude Opus 4.5 en temps réel (~10 secondes)
- 💾 Cache DB fonctionnel
- 🔄 Bouton "Régénérer" pour tester plusieurs fois

---

## 📋 Prérequis

### 1. Backend API opérationnel

```bash
cd apps/api

# Vérifier que l'API est démarrée
curl http://localhost:8000/health
# → Devrait retourner 200 OK

# Si pas démarrée, lancer :
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Variables d'environnement configurées

```bash
# Vérifier .env dans apps/api/
ANTHROPIC_API_KEY=sk-ant-...           # ✅ Requis
LUNAR_LLM_MODE=anthropic               # ✅ Requis (génération Claude)
LUNAR_CLAUDE_MODEL=opus                # ✅ Requis (Opus 4.5)
```

### 3. Database avec un utilisateur de test

```bash
# Vérifier qu'il y a au moins 1 user avec lunar_returns
psql $DATABASE_URL -c "SELECT COUNT(*) FROM users;"
psql $DATABASE_URL -c "SELECT COUNT(*) FROM lunar_returns;"
```

Si aucun user, crée-en un via l'app ou directement en DB.

---

## 🚀 Lancement de l'App Mobile

### Option A : iOS Simulator (Mac)

```bash
cd apps/mobile

# Installer dépendances (si pas fait)
npm install

# Lancer Expo
npm start

# Puis taper 'i' pour ouvrir iOS Simulator
```

**Configuration API** :
- iOS Simulator peut accéder à `http://localhost:8000` directement
- Aucune config supplémentaire requise si `.env` contient :
  ```
  EXPO_PUBLIC_API_URL=http://localhost:8000
  ```

### Option B : Android Emulator

```bash
cd apps/mobile

npm start

# Puis taper 'a' pour ouvrir Android Emulator
```

**Configuration API** :
- Android Emulator doit utiliser `http://10.0.2.2:8000`
- Mettre dans `.env` :
  ```
  EXPO_PUBLIC_API_URL=http://10.0.2.2:8000
  ```

### Option C : Device Physique (iOS/Android)

```bash
cd apps/mobile

npm start

# Scanner le QR code avec Expo Go app
```

**Configuration API** :
- Device physique doit utiliser ton IP LAN
- Trouver ton IP :
  ```bash
  # Mac
  ifconfig | grep "inet " | grep -v 127.0.0.1

  # Linux
  hostname -I
  ```
- Mettre dans `.env` :
  ```
  EXPO_PUBLIC_API_URL=http://192.168.X.X:8000
  ```
  (Remplace par ton IP réelle)

---

## 🧪 Scénarios de Test

### Test 1 : Premier chargement (génération Claude)

1. **Ouvrir l'app** et se connecter
2. **Naviguer** vers "Rapport Lunaire" (via Home ou menu)
3. **Observer** le loading screen :
   - ⏳ Sablier qui se retourne
   - 🌙 Lune et étoiles scintillantes
   - Barre de progression animée
   - Texte : "Génération de ton interprétation lunaire..."

**Durée attendue** : ~10 secondes

**Résultat attendu** :
- Rapport s'affiche avec interprétation complète
- Footer dev affiche :
  ```
  📊 V2 • Source: IA Claude • claude-opus-4-5-20251101
  ```
- Bouton "🔄 Régénérer l'interprétation" visible (DEV only)

### Test 2 : Second chargement (cache hit)

1. **Retourner** à l'écran précédent (bouton ← Retour)
2. **Re-naviguer** vers "Rapport Lunaire"
3. **Observer** le loading screen (très bref)

**Durée attendue** : <1 seconde (cache DB)

**Résultat attendu** :
- Rapport s'affiche instantanément
- Footer dev affiche :
  ```
  📊 V2 • Source: Cache DB • claude-opus-4-5-20251101
  ```

### Test 3 : Régénération forcée

1. **Scroller** jusqu'en bas du rapport
2. **Appuyer** sur le bouton "🔄 Régénérer l'interprétation"
3. **Observer** le loading screen :
   - Texte : "Régénération en cours..."
   - Bouton devient "⏳ Régénération..."

**Durée attendue** : ~10 secondes (nouvelle génération Claude)

**Résultat attendu** :
- Rapport se recharge avec nouvelle interprétation (texte différent)
- Footer dev affiche :
  ```
  📊 V2 • Source: IA Claude • claude-opus-4-5-20251101
  ```
- L'ancienne version reste en historique DB

---

## 🔍 Vérifications

### Backend Logs

```bash
# Terminal API affiche :
[LunarReport] ✅ Rapport généré pour Janvier - source=claude, model=claude-opus-4-5-20251101
```

### Mobile Logs

```bash
# Expo console affiche :
[LunarReport] 🔄 Régénération pour lunar_return_id=123...
[LunarReport] ✅ Régénération réussie: {source: 'claude', model: 'claude-opus-4-5-20251101'}
```

### Database

```sql
-- Vérifier les interprétations générées
SELECT COUNT(*) FROM lunar_interpretations
WHERE user_id = 1;  -- Devrait augmenter à chaque test

-- Voir les dernières générations
SELECT id, lunar_return_id, source, model_used, created_at
FROM lunar_interpretations
WHERE user_id = 1
ORDER BY created_at DESC
LIMIT 5;
```

---

## 💰 Coûts Estimés

| Test | Appels Claude | Coût (sans caching) | Coût (avec caching) |
|------|---------------|---------------------|---------------------|
| Test 1 | 1 | $0.020 | $0.020 |
| Test 2 | 0 | $0.000 | $0.000 |
| Test 3 | 1 | $0.020 | $0.002 |
| **Total 3 tests** | **2** | **$0.040** | **$0.022** |

**Prompt Caching actif** : -90% coûts (après 1ère génération)

---

## 🐛 Troubleshooting

### Erreur : "Network request failed"

**Cause** : App ne peut pas se connecter à l'API

**Solutions** :
1. Vérifier que l'API est démarrée : `curl http://localhost:8000/health`
2. Vérifier `EXPO_PUBLIC_API_URL` dans `.env`
3. Sur device physique, vérifier que ton Mac et le device sont sur le même WiFi

### Erreur : "401 Unauthorized"

**Cause** : JWT token invalide ou expiré

**Solutions** :
1. Se déconnecter et se reconnecter
2. Vérifier `SECRET_KEY` dans `.env` backend
3. Vérifier que `DEV_AUTH_BYPASS=true` si tu veux bypass auth en dev

### Loading screen reste figé

**Cause** : Génération Claude a échoué

**Solutions** :
1. Vérifier logs backend : `tail -f logs/api.log`
2. Vérifier `ANTHROPIC_API_KEY` est valide
3. Vérifier quota Anthropic API

### Interprétation vide ou "template"

**Cause** : Génération Claude échouée → fallback templates

**Solutions** :
1. Vérifier logs backend pour voir l'erreur
2. Vérifier `LUNAR_LLM_MODE=anthropic`
3. Vérifier `LUNAR_CLAUDE_MODEL=opus`

---

## 📊 Métriques Prometheus

Pendant les tests, tu peux monitorer :

```bash
# Voir les métriques en temps réel
curl http://localhost:8000/metrics | grep lunar_

# Exemples de métriques :
# lunar_interpretation_generated_total{source="claude"} 2
# lunar_interpretation_cache_hit_total 1
# lunar_interpretation_duration_seconds_sum 20.5
```

---

## ✅ Checklist Final

Après les 3 tests, vérifie que :

- [x] Loading screen s'affiche avec animation sablier
- [x] Génération Claude prend ~10 secondes
- [x] Cache fonctionne (2e chargement <1s)
- [x] Bouton "Régénérer" fonctionne (DEV only)
- [x] Metadata affichent source="IA Claude"
- [x] DB contient 2-3 nouvelles interprétations
- [x] Coût total <$0.05

---

## 🎉 Si tout fonctionne

**Félicitations !** Le système de génération Claude Opus 4.5 est opérationnel en production.

**Prochaines étapes** :
1. Désactiver le bouton "Régénérer" en production (déjà fait via `__DEV__`)
2. Monitorer les coûts en production
3. Ajuster le cache TTL si nécessaire
4. Configurer alertes Prometheus pour coûts >$10/jour

---

**Dernière mise à jour** : 2026-01-24
**Version** : Sprint 6 - Tests Mobile Ready 🚀
