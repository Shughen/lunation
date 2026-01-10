# 🐛 BUGS À CORRIGER

**Date:** 5 novembre 2025

---

## 🔴 BUGS PRIORITAIRES

### 1. Pré-remplissage Compatibilité ne fonctionne pas
**Module:** `app/compatibility/index.js`

**Symptôme:**
- Les données sont envoyées correctement (logs OK)
- Mais visually, les signes affichent toujours "Bélier, Bélier, Bélier"
- Alors que le profil contient : Bélier ♈, Cancer ♋, Lion ♌

**Logs:**
```
[Compatibility] Pré-remplissage: {
  sunSign: {id: 1, name: 'Bélier'},
  ascendant: {id: 4, name: 'Cancer'},
  moonSign: {id: 5, name: 'Lion'}
}
[Compatibility] Mise à jour person1 avec: {
  sunSign: 1, ascendant: 4, moonSign: 5, name: "Beaurain Rémi"
}
```

**Pourtant l'affichage ne change pas !**

**Cause probable:**
- Le `setPerson1` est appelé mais les valeurs ne se répercutent pas dans l'UI
- Possible problème de timing avec les pickers
- Parent-Enfant fonctionne, pas Compatibilité → Différence d'implémentation

**À investiguer:**
- Timing du render des zodiacPickers
- Ordre d'exécution des useEffect
- Différence entre renderZodiacPicker dans les 2 fichiers

---

### 2. Date de naissance décalée d'1 jour
**Module:** `stores/profileStore.js`

**Symptôme:**
- Utilisateur saisit : 15/04/1989
- Profil affiche : 14/04/1989 (`1989-04-14T22:00:00.000Z`)

**Cause:**
- Problème de timezone UTC
- La date est stockée en UTC mais affichée en local
- Décalage de 1 jour à cause de l'heure (22:00:00 UTC = minuit en France)

**Solution:**
- Stocker la date en format "YYYY-MM-DD" string
- Ou ajuster l'affichage pour compenser le timezone

**Impact:**
- Calcul du signe zodiacal peut être faux
- Thème natal calculé avec la mauvaise date

---

## 🟡 BUGS MINEURS

### 3. ESLint : 65 problèmes de qualité code
- Variables non utilisées
- Dépendances manquantes dans useEffect
- Pas bloquant mais à nettoyer

### 4. Maestro E2E : Java requis
- Tests E2E prêts mais Java non installé
- Commande : `brew install --cask temurin17`

---

## 📋 PROCHAINES ACTIONS

1. **Corriger la date de naissance** (décalage UTC)
2. **Débugger le pré-remplissage Compatibilité** (state update)
3. **Implémenter AstrologyAPI v3** (thème natal précis)
4. **Nettoyer ESLint** (qualité code)
5. **Installer Java** (tests E2E)

---

**Bugs documentés. On passe à l'implémentation d'AstrologyAPI ! 🚀**

