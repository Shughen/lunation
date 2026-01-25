# Scripts Outils - Astroia Lunar

Ces scripts sont les **seuls** exécutables autorisés par Claude Code via MCP (allowlist stricte).

**🔐 Sécurité** : Claude ne peut exécuter AUCUNE commande système en direct (npm, adb, pytest, etc.). Seuls ces scripts sont autorisés.

---

## 📦 Scripts disponibles

### 1️⃣ `build_android.sh`

**Objectif** : Build et lancement de l'app Android (dev build)

**Commande interne** :
```bash
cd apps/mobile && npm run android
```

**Utilisation** :
```bash
./tools/build_android.sh
```

**Log** : `logs/build_android_YYYYMMDD-HHMMSS.log`

**Use case** :
- Build après modification du code natif (Java/Kotlin)
- Test sur émulateur/device Android
- Debugging de crashes au démarrage

---

### 2️⃣ `run_tests_mobile.sh`

**Objectif** : Tests et typecheck de l'app mobile

**Commandes internes** :
```bash
cd apps/mobile
npm run typecheck  # TypeScript
npm test           # Jest
```

**Utilisation** :
```bash
./tools/run_tests_mobile.sh
```

**Log** : `logs/tests_mobile_YYYYMMDD-HHMMSS.log`

**Use case** :
- Vérifier les types TypeScript avant commit
- Lancer les tests unitaires (Jest + Testing Library)
- CI/CD local

---

### 3️⃣ `run_tests_api.sh`

**Objectif** : Tests backend (pytest)

**Commande interne** :
```bash
cd apps/api && pytest -q
```

**Utilisation** :
```bash
./tools/run_tests_api.sh
```

**Log** : `logs/tests_api_YYYYMMDD-HHMMSS.log`

**Use case** :
- Vérifier les tests après modification du backend
- Validation avant commit (backend)
- CI/CD local

---

### 4️⃣ `collect_logcat.sh`

**Objectif** : Capturer les logs Android (logcat)

**Commandes internes** :
```bash
adb devices
adb logcat -d -T 5m
```

**Utilisation** :
```bash
./tools/collect_logcat.sh
```

**Log** : `logs/logcat_YYYYMMDD-HHMMSS.log`

**Use case** :
- App crash au runtime (NullPointerException, etc.)
- Debugging d'erreurs réseau (API calls)
- Vérifier les console.log React Native

**Note** : Capture uniquement les **5 dernières minutes** de logs (évite de saturer le fichier).

---

### 5️⃣ `start_expo.sh`

**Objectif** : Démarrer le serveur Expo dev

**Commande interne** :
```bash
cd apps/mobile && npm start
```

**Utilisation** :
```bash
./tools/start_expo.sh
```

**Log** : `logs/expo_start_YYYYMMDD-HHMMSS.log`

**Use case** :
- Démarrer l'app en mode dev
- Tester sur Expo Go
- Hot reload pendant le développement

**Note** : Ce script lance un processus **bloquant** (serveur Expo). Pour l'arrêter : `Ctrl+C`.

---

## 🔄 Workflow avec Claude Code

### Exemple 1 : Fix erreur TypeScript

**Toi** :
> Lance `tools/run_tests_mobile.sh` et corrige les erreurs TypeScript

**Claude** :
1. Exécute `run_tests_mobile.sh` via MCP
2. Lit `logs/tests_mobile_YYYYMMDD-HHMMSS.log`
3. Identifie les erreurs (ex: `Type 'string' is not assignable to type 'number'`)
4. Patch les fichiers concernés (via Edit tool)
5. Relance `run_tests_mobile.sh`
6. ✅ Tests passent !

### Exemple 2 : Debugging crash Android

**Toi** :
> L'app crash au clic sur "Générer rapport lunaire", récupère les logs

**Claude** :
1. Exécute `collect_logcat.sh` via MCP
2. Lit `logs/logcat_YYYYMMDD-HHMMSS.log`
3. Identifie la stack trace (ex: `NullPointerException at LunarReportScreen.tsx:42`)
4. Analyse le code concerné
5. Propose un fix (ex: ajout de nullish coalescing `?.`)
6. Tu appliques le fix
7. Relance l'app avec `build_android.sh`

### Exemple 3 : Tests API après changement backend

**Toi** :
> J'ai modifié l'endpoint POST /api/lunar/interpretation/regenerate, vérifie que les tests passent

**Claude** :
1. Exécute `run_tests_api.sh` via MCP
2. Lit `logs/tests_api_YYYYMMDD-HHMMSS.log`
3. Identifie les tests qui échouent (ex: `test_regenerate_endpoint`)
4. Analyse le diff entre ancien/nouveau comportement
5. Met à jour les tests (via Edit tool)
6. Relance `run_tests_api.sh`
7. ✅ Tests passent !

---

## 📝 Ajouter un nouveau script

### Étape 1 : Créer le script

```bash
# Créer le fichier
cat > tools/mon_nouveau_script.sh <<'SCRIPT'
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p logs
LOG="logs/mon_nouveau_script_$(date +%Y%m%d-%H%M%S).log"

echo "[mon_nouveau_script] $(date -Iseconds)" | tee "$LOG"
echo "[pwd] $(pwd)" | tee -a "$LOG"
echo "----------------------------------------" | tee -a "$LOG"

# Ta commande ici
cd apps/mobile
echo "[cmd] npm run ma-commande" | tee -a "../../$LOG"
npm run ma-commande 2>&1 | tee -a "../../$LOG"

echo "----------------------------------------" | tee -a "../../$LOG"
echo "[ok] done" | tee -a "../../$LOG"
echo "[log] $LOG" | tee -a "../../$LOG"
SCRIPT

# Rendre exécutable
chmod +x tools/mon_nouveau_script.sh
```

### Étape 2 : Mettre à jour la allowlist MCP

```bash
# Supprimer l'ancienne config
claude mcp remove shell-safe

# Ajouter la nouvelle (avec le script en plus)
claude mcp add --transport stdio shell-safe -- \
  mcp-unix-shell \
  --allowed-commands=tools/build_android.sh,tools/run_tests_mobile.sh,tools/run_tests_api.sh,tools/collect_logcat.sh,tools/start_expo.sh,tools/mon_nouveau_script.sh
```

### Étape 3 : Mettre à jour la documentation

1. Ajouter le script dans `.claude/CLAUDE.md` → section "Scripts autorisés"
2. Ajouter la description ici (dans ce README)

---

## 🚨 Règles importantes

### ✅ DO (Faire)

- **Toujours** écrire les logs dans `logs/*.log` avec timestamp
- **Toujours** utiliser `set -euo pipefail` en début de script
- **Toujours** se placer à la racine du repo (`ROOT_DIR`)
- **Toujours** utiliser des chemins relatifs (pas de `/Users/...` en dur)
- **Toujours** afficher la commande exécutée avant de l'exécuter (`echo "[cmd] ..."`)

### ❌ DON'T (Ne pas faire)

- ❌ **JAMAIS** dumper l'environnement (`printenv`, `env`, `export`)
- ❌ **JAMAIS** afficher des secrets (API keys, tokens, passwords)
- ❌ **JAMAIS** modifier des fichiers système (hors du repo)
- ❌ **JAMAIS** exécuter des commandes destructives (`rm -rf /`, `sudo`, etc.)
- ❌ **JAMAIS** installer des packages globalement (`npm install -g`, `pip install --global`)

---

## 📊 Statistiques

| Script | Durée typique | Use case principal |
|--------|---------------|-------------------|
| `build_android.sh` | 3-5 min | Build app après changement code natif |
| `run_tests_mobile.sh` | 30-60s | Validation avant commit (mobile) |
| `run_tests_api.sh` | 10-30s | Validation avant commit (backend) |
| `collect_logcat.sh` | 5-10s | Debugging crash runtime Android |
| `start_expo.sh` | Continu | Développement en mode hot reload |

---

## 🔧 Debugging

### Script ne s'exécute pas

```bash
# Vérifier les permissions
ls -la tools/*.sh
# Devrait afficher : -rwxr-xr-x

# Si manquant, réparer :
chmod +x tools/*.sh
```

### Log non créé

```bash
# Vérifier que le dossier logs/ existe
ls -ld logs/

# Si manquant, créer :
mkdir -p logs
```

### Erreur "command not found"

**Cause** : `npm`, `adb`, `pytest` non dans le PATH

**Solution** :
```bash
# Vérifier npm
which npm

# Vérifier adb
which adb

# Vérifier pytest
which pytest

# Si manquant, installer/configurer le PATH
```

---

## 📚 Ressources

- **Configuration MCP** : [docs/MCP_SECURE_SETUP.md](../docs/MCP_SECURE_SETUP.md)
- **Règles de sécurité** : [.claude/CLAUDE.md](../.claude/CLAUDE.md) → section "Règles Strictes"
- **Serveur MCP utilisé** : [mcp-unix-shell](https://github.com/gamunu/mcp-unix-shell)
