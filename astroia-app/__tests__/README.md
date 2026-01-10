# 📚 Documentation des Helpers de Tests

Ce répertoire contient des helpers réutilisables pour faciliter l'écriture et la maintenance des tests dans le projet Astro.IA.

## 📦 Helpers Disponibles

### mockStores.js
Helpers pour mocker les stores Zustand dans les tests.

### mockServices.js
Helpers pour mocker les services API dans les tests.

### mockSupabase.js, mockAsyncStorage.js, mockAnalytics.js
Helpers existants créés lors des P1/P2.

## 💡 Bonnes Pratiques

1. Réinitialiser les mocks dans `beforeEach()` pour éviter les fuites entre les tests
2. Utiliser les helpers plutôt que de créer des mocks inline pour la cohérence
3. Ne pas tout réécrire : refactorer progressivement les tests existants
