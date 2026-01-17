# Notes d'exécution des tests Maestro

## Tests créés (Tâche 7.2)

5 tests E2E critiques MVP ont été créés:

1. **2_onboarding_to_home.yaml** - Onboarding complet → Home
2. **3_home_to_lunar_report.yaml** - Home → Rapport lunaire
3. **4_home_to_voc.yaml** - Home → VoC actuel
4. **5_home_to_transits.yaml** - Home → Transits majeurs
5. **6_journal_create_entry.yaml** - Home → Journal → Créer entrée

## Prérequis pour l'exécution

### 1. Application installée

```bash
# Vérifier que l'app est installée sur le simulateur/device
# iOS: com.remi.astroia
# Android: com.remi.astroia
```

### 2. État initial de l'application

Certains tests nécessitent un état spécifique:

- **Test 2 (onboarding)**: Requiert un reset complet de l'app (premier lancement)
- **Tests 3-6**: Requièrent que l'onboarding soit déjà complété

### 3. Données backend

Les tests supposent que:
- L'API backend est accessible
- Un cycle lunaire actuel existe
- Les transits sont calculés pour le mois en cours
- Le VoC status est disponible

## Ajustements potentiellement nécessaires

### 1. Sélecteurs d'éléments

Les tests utilisent principalement des sélecteurs par texte. Si le texte change ou n'est pas trouvé, vous devrez ajuster:

```yaml
# Approche actuelle (texte visible)
- tapOn: "Continuer"

# Alternative (ID si défini dans le code)
- tapOn:
    id: "button-continue"

# Alternative (position)
- tapOn:
    point: "50%,90%"
```

### 2. Date picker (test onboarding)

Le test 2 simplifie la saisie de date. En réalité, vous devrez peut-être:

```yaml
# Approche actuelle (simplifiée)
- tapOn:
    id: "input-birth-date"
- tapOn: "Continuer"

# Approche réaliste (dépend du composant)
- tapOn:
    id: "input-birth-date"
- tapOn: "1990"  # Année
- tapOn: "Janvier"  # Mois
- tapOn: "15"  # Jour
- tapOn: "Valider"
```

### 3. Input journal (test 6)

Le test suppose un input accessible par ID. Ajustez si nécessaire:

```yaml
# Approche actuelle
- tapOn:
    id: "input-journal-note"
- inputText: "Test entrée journal"

# Alternative si le modal ouvre directement le clavier
- inputText: "Test entrée journal"
```

### 4. Délais d'attente

Les délais (`wait`) sont configurés conservativement. Ajustez selon les performances:

```yaml
# Réduire si l'app est rapide
- runFlow:
    wait: 1000  # au lieu de 2000

# Augmenter si l'API est lente
- runFlow:
    wait: 5000  # au lieu de 2000
```

### 5. Regex pour assertions flexibles

Certains tests utilisent des regex pour gérer le contenu dynamique:

```yaml
# Année dynamique (2026, 2027, etc.)
- assertVisible:
    text: ".*\\d{4}.*"
    regex: true

# VoC actif OU inactif
- assertVisible:
    text: "(La Lune est Void of Course|Prochaine fenêtre)"
    regex: true
```

## Ordre d'exécution recommandé

Pour un premier run complet:

1. Reset l'application complètement
2. Exécuter `2_onboarding_to_home.yaml` (configure l'app)
3. Exécuter `3_home_to_lunar_report.yaml`
4. Exécuter `4_home_to_voc.yaml`
5. Exécuter `5_home_to_transits.yaml`
6. Exécuter `6_journal_create_entry.yaml`

```bash
cd apps/mobile

# Test complet séquentiel
maestro test maestro/flows/2_onboarding_to_home.yaml
maestro test maestro/flows/3_home_to_lunar_report.yaml
maestro test maestro/flows/4_home_to_voc.yaml
maestro test maestro/flows/5_home_to_transits.yaml
maestro test maestro/flows/6_journal_create_entry.yaml

# Ou tous en une fois
maestro test maestro/flows/
```

## Debug et troubleshooting

### Mode debug

```bash
# Exécuter un test en mode debug (verbose)
maestro test --debug maestro/flows/3_home_to_lunar_report.yaml
```

### Mode interactif

```bash
# Lancer Maestro Studio pour explorer l'app manuellement
maestro studio

# Utile pour:
# - Identifier les sélecteurs corrects
# - Tester des interactions
# - Capturer l'arborescence de la vue
```

### Screenshots

Tous les tests incluent des screenshots à la fin. Vérifiez les dans:

```
~/.maestro/tests/<test-run-id>/screenshots/
```

### Logs

Si un test échoue, vérifiez:

1. La console Maestro (stack trace)
2. Les logs de l'app (via Xcode/Android Studio)
3. Les screenshots capturés au moment de l'échec

## Cas d'échec connus

### 1. "Element not found"

Cause: Le texte ou l'ID n'existe pas au moment de l'assertion.

Solution:
- Ajouter un délai avant l'assertion
- Vérifier que le texte exact correspond (casse, espaces)
- Utiliser Maestro Studio pour identifier le bon sélecteur

### 2. "App not installed"

Cause: L'app n'est pas installée sur le simulateur/device.

Solution:
```bash
# iOS: Installer via Xcode ou npx expo run:ios
# Android: Installer via npx expo run:android
```

### 3. "Timeout waiting for element"

Cause: L'élément met trop de temps à apparaître.

Solution:
- Augmenter le délai d'attente
- Vérifier que l'API backend répond correctement
- Vérifier les logs de l'app pour des erreurs

### 4. Backend non disponible

Cause: L'API backend n'est pas accessible ou retourne des erreurs.

Solution:
- Lancer le backend localement: `cd apps/api && uvicorn main:app --reload`
- Vérifier la connectivité réseau du simulateur
- Vérifier les variables d'environnement (EXPO_PUBLIC_API_URL)

## Validation des tests

Pour valider qu'un test fonctionne:

1. L'exécution complète sans erreur
2. Tous les `assertVisible` passent
3. Les screenshots montrent l'état attendu
4. L'app termine dans l'état attendu (ex: Home screen pour la plupart des tests)

## Maintenance future

Quand mettre à jour ces tests:

1. Changement de texte dans l'UI (i18n)
2. Refactoring de composants (nouveaux IDs)
3. Changement de flow (nouvelles étapes d'onboarding)
4. Ajout/suppression de fonctionnalités
5. Changement de structure de données API (header, format)

## Ressources

- [Documentation Maestro](https://maestro.mobile.dev/)
- [Sélecteurs Maestro](https://maestro.mobile.dev/api-reference/selectors)
- [Commandes Maestro](https://maestro.mobile.dev/api-reference/commands)
- [Exemples communautaire](https://github.com/mobile-dev-inc/maestro/tree/main/maestro-test/src/test/resources)
