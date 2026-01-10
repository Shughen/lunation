# 🔧 Fix: Network Request Failed

## ❌ Problème

```
ERROR [NatalServiceRapidAPI] Erreur: [TypeError: Network request failed]
```

**Cause** : `localhost` ne fonctionne pas sur un device iOS/Android réel !

---

## ✅ Solution appliquée

J'ai changé l'URL du backend de :
- ❌ `http://localhost:8000`
- ✅ `http://192.168.0.150:8000` (ton IP locale)

---

## 🧪 Tester la connexion

### 1️⃣ Vérifier que le backend est accessible

Depuis ton **navigateur** sur ton **Mac**, ouvre :

```
http://192.168.0.150:8000/health
```

Tu devrais voir :
```json
{
  "status": "healthy",
  "checks": { ... }
}
```

### 2️⃣ Vérifier que le backend écoute sur toutes les interfaces

Assure-toi que le backend FastAPI écoute sur **`0.0.0.0`** et pas juste `127.0.0.1` :

```bash
cd /Users/remibeaurain/astroia/astroia-lunar/apps/api

# Lance avec --host 0.0.0.0 (important !)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Tu devrais voir :
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 3️⃣ Tester depuis ton téléphone

Sur ton **iPhone** (connecté au même WiFi), ouvre Safari et va sur :

```
http://192.168.0.150:8000/health
```

Si tu vois la réponse JSON, **ça marche !** ✅

---

## 🔄 Relancer l'app

Maintenant que l'IP est correcte :

1. **Assure-toi que le backend tourne** :
   ```bash
   cd /Users/remibeaurain/astroia/astroia-lunar/apps/api
   source .venv/bin/activate
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Recharge l'app mobile** (Cmd+R dans le simulateur ou shake + reload)

3. **Teste le calcul** dans Thème Natal avec RapidAPI activé

---

## 🐛 Si ça marche toujours pas

### Vérifier l'IP

```bash
# Sur Mac, récupère ton IP WiFi
ipconfig getifaddr en0

# Si en0 ne marche pas, essaie en1
ipconfig getifaddr en1
```

Change l'IP dans le fichier si nécessaire :

```javascript
// lib/api/natalServiceRapidAPI.js (ligne 13)
const FASTAPI_BASE_URL = __DEV__ 
  ? 'http://TON_IP_ICI:8000'  // ← Change ici
  : 'https://ton-api-prod.com';
```

### Vérifier le firewall

Si le backend ne répond toujours pas, vérifie que le firewall macOS autorise les connexions :

```bash
# Désactiver temporairement le firewall pour tester
# Préférences Système → Sécurité → Pare-feu → Désactiver
```

### Vérifier que vous êtes sur le même réseau

Ton **Mac** et ton **iPhone** doivent être sur le **même WiFi** ! 📡

---

## 📝 Checklist de résolution

- [ ] Backend lancé avec `--host 0.0.0.0`
- [ ] Backend répond sur `http://192.168.0.150:8000/health` depuis le navigateur Mac
- [ ] Backend répond depuis Safari iPhone sur la même URL
- [ ] Mac et iPhone sur le même WiFi
- [ ] IP correcte dans `natalServiceRapidAPI.js`
- [ ] App rechargée (Cmd+R)

---

**Une fois que tout est ✅, le calcul devrait marcher ! 🚀**

