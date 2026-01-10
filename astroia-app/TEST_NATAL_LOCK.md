# 🧪 TEST NATAL LOCK (Option C)

## ✅ TEST 1 : Mode verrouillé (profil complet)

**Contexte :** Tu as déjà calculé ton thème natal.

**Étapes :**
1. Ferme/rouvre l'app
2. Va dans **Compatibilité** → Couple
3. **Vérifie Personne 1 :**
   - [ ] NatalLockCard s'affiche avec tes 3 signes (Scorpion, Poissons, Sagittaire)
   - [ ] Pas de pickers (verrouillé)
   - [ ] Bandeau 🔒 "Données issues de ton thème natal"
   - [ ] Bouton "Recalculer mon thème natal" présent
   - [ ] Tap sur le bouton → ouvre `/natal-chart`
4. **Vérifie Personne 2 :**
   - [ ] Les 3 pickers sont bien là (éditable)
   - [ ] Auto-scroll fonctionne
5. **Remplis P2 + Analyse :**
   - [ ] Résultat s'affiche
   - [ ] Dans les logs : `[Compatibility] Analyse avec données du thème natal (verrouillé)`

**Résultat attendu :** ✅ Mode verrouillé actif

---

## 🔄 TEST 2 : Mode fallback (profil incomplet)

**Contexte :** Simuler un profil sans thème natal.

### **Option A : Via l'app (recommandé)**

1. Va dans **Paramètres** → **Profil**
2. **Supprime** ou **modifie** ta date de naissance
3. **Sauvegarde**
4. **Retour** → **Compatibilité** → Couple
5. **Vérifie Personne 1 :**
   - [ ] Les 3 pickers sont visibles (fallback)
   - [ ] Pas de NatalLockCard
   - [ ] Auto-fill fonctionne (badges "Auto")
   - [ ] Auto-scroll fonctionne
6. **Analyse :**
   - [ ] Dans les logs : `[Compatibility] Analyse avec données manuelles (fallback)`

### **Option B : Via Supabase (avancé)**

1. Ouvre le dashboard Supabase → table `profiles`
2. Localise ton utilisateur (UUID = `auth.users.id`)
3. Mets `sun_sign`, `moon_sign`, `ascendant` à `null`
4. Recharge l'app → **Compatibilité** pour vérifier le fallback

**Résultat attendu :** ✅ Mode fallback actif

---

## 📊 RÉSULTAT GLOBAL

- [ ] Mode verrouillé fonctionne (profil complet)
- [ ] Mode fallback fonctionne (profil incomplet)
- [ ] Historisation `person1_source` correcte
- [ ] UX fluide et cohérente

---

## 🐛 BUGS À REPORTER

Si tu trouves un bug :
1. **Contexte** : Mode verrouillé ou fallback ?
2. **Action** : Qu'est-ce que tu as fait ?
3. **Résultat** : Qu'est-ce qui s'est passé ?
4. **Attendu** : Qu'est-ce qui devrait se passer ?
5. **Screenshot** : Si possible

---

**Bon test !** 🚀

