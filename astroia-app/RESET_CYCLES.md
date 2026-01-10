# 🔄 RESET CYCLES - GUIDE RAPIDE

## Problème
Storage corrompu avec 6 cycles invalides qui bloquent toute création.

## Solution (2 min)

### Méthode 1 : Via Metro Console (RECOMMANDÉ)

1. Dans le terminal où tourne Expo, appuie sur **`j`**
2. Une fenêtre Chrome s'ouvre (React Native Debugger)
3. Ouvre la **Console** (onglet en haut)
4. Copie-colle cette ligne :

```javascript
AsyncStorage.multiRemove(['@luna_cycle_history', '@luna_cycle_migrated', 'cycle_config']).then(() => console.log('✅ Storage nettoyé !'))
```

5. Appuie sur **Entrée**
6. Tu devrais voir : `✅ Storage nettoyé !`
7. Dans l'app, appuie sur **R** (ou CMD+R) pour recharger
8. ✅ **C'est propre !**

### Méthode 2 : Via Code (Alternative)

Si la méthode 1 ne marche pas, je vais créer un bouton "Reset" temporaire dans l'app.

## Vérification après reset

1. Home → "Suivi rapide" devrait afficher **"Début des règles"**
2. "Mes cycles" → Devrait être vide ou montrer empty state
3. Countdown → "Prédictions non disponibles" (normal, besoin 2 cycles)

## Créer ton 1er cycle propre

1. Home → Tap **"Début des règles"**
2. Toast "✅ Règles logées !"
3. Attendre quelques jours OU
4. "Mes cycles" → "+" → Créer cycle passé manuel

