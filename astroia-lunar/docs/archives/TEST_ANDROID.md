# 📱 Guide de Test Android avec Expo Go

## ✅ Checklist de Configuration

### 1. API Backend
- [ ] API lancée avec `--host 0.0.0.0`
- [ ] Port 8000 accessible
- [ ] Firewall macOS autorise les connexions

### 2. Configuration Mobile
- [ ] `.env` contient `EXPO_PUBLIC_API_URL=http://192.168.0.150:8000`
- [ ] Mac et Android sur le même Wi-Fi
- [ ] IP LAN correcte (vérifier avec `ipconfig getifaddr en0`)

### 3. Test de Connexion

#### Depuis le Mac :
```bash
# Doit retourner {"status":"ok"}
curl http://192.168.0.150:8000/health
```

#### Depuis Android (via adb si connecté) :
```bash
# Si téléphone connecté en USB avec USB debugging activé
adb shell "curl http://192.168.0.150:8000/health"
```

### 4. Vérifier l'écoute réseau

```bash
# Doit afficher 0.0.0.0:8000 (pas seulement 127.0.0.1:8000)
netstat -an | grep 8000
```

### 5. Expo Go sur Android

1. Ouvrir Expo Go
2. Scanner le QR code
3. Si erreur de connexion, vérifier :
   - Les logs Expo dans le terminal
   - Les logs de l'API (erreurs CORS, etc.)
   - La console Expo Go (shake device → Show Dev Menu → Debug)

## 🔧 Solutions aux Problèmes Courants

### Problème : "Network request failed"
**Solution :**
- Vérifier que l'IP dans `.env` correspond à l'IP LAN actuelle
- Vérifier que Mac et Android sont sur le même réseau
- Vérifier le firewall macOS

### Problème : "Connection refused"
**Solution :**
- Vérifier que l'API écoute sur `0.0.0.0` (pas `127.0.0.1`)
- Vérifier que le port 8000 n'est pas bloqué

### Problème : QR code ne se charge pas
**Solution :**
- Vérifier la connexion internet du téléphone
- Essayer de taper manuellement l'URL dans Expo Go
- Redémarrer Expo avec `npx expo start -c` (clear cache)

### Problème : CORS errors dans les logs API
**Solution :**
- Vérifier que l'API autorise les requêtes depuis Expo Go
- Ajouter l'IP du téléphone dans les CORS allowed origins si nécessaire

## 📝 Commandes Utiles

```bash
# Trouver l'IP LAN du Mac
ipconfig getifaddr en0

# Vérifier que l'API écoute sur toutes les interfaces
netstat -an | grep 8000

# Tester la connexion API depuis le Mac
curl http://192.168.0.150:8000/health

# Redémarrer Expo avec cache clear
cd apps/mobile && npx expo start -c

# Voir les logs Expo en temps réel
# (dans le terminal où Expo tourne)
```

## 🌐 Alternative : Tunnel Cloudflare

Si le réseau local ne fonctionne pas, vous pouvez utiliser Cloudflare Tunnel :

```bash
# Installer cloudflared
brew install cloudflared

# Créer un tunnel
cloudflared tunnel --url http://localhost:8000
```

Puis mettre à jour `.env` :
```env
EXPO_PUBLIC_API_URL=https://votre-tunnel.trycloudflare.com
```
