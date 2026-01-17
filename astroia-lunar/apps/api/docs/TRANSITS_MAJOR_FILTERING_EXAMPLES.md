# Exemples d'utilisation: Filtrage major_only

## Guide pratique avec exemples concrets d'appels API

Ce document fournit des exemples concrets d'utilisation du paramètre `major_only` sur les endpoints de transits.

---

## 1. Transits Natals (POST /api/transits/natal)

### Exemple 1.1: Tous les aspects (comportement par défaut)

**Requête:**
```bash
curl -X POST "http://localhost:8000/api/transits/natal" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1989-04-15",
    "birth_time": "14:30",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522,
    "birth_timezone": "Europe/Paris",
    "transit_date": "2025-01-15",
    "transit_time": "12:00"
  }'
```

**Réponse (extrait):**
```json
{
  "provider": "rapidapi",
  "kind": "natal_transits",
  "insights": {
    "major_aspects": [
      {
        "transit_planet": "Jupiter",
        "natal_planet": "Sun",
        "aspect": "trine",
        "orb": 0.5,
        "interpretation": "Jupiter harmonise votre Soleil natal..."
      },
      {
        "transit_planet": "Venus",
        "natal_planet": "Mars",
        "aspect": "sextile",
        "orb": 1.2,
        "interpretation": "Venus en sextile avec votre Mars natal"
      },
      {
        "transit_planet": "Saturn",
        "natal_planet": "Moon",
        "aspect": "square",
        "orb": 2.0,
        "interpretation": "Saturn crée une friction avec votre Lune natale..."
      }
    ],
    "energy_level": "high"
  }
}
```

**Note:** 3 aspects retournés (trine, sextile, square) - tous les aspects sont inclus.

---

### Exemple 1.2: Uniquement les aspects majeurs

**Requête:**
```bash
curl -X POST "http://localhost:8000/api/transits/natal?major_only=true" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1989-04-15",
    "birth_time": "14:30",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522,
    "birth_timezone": "Europe/Paris",
    "transit_date": "2025-01-15",
    "transit_time": "12:00"
  }'
```

**Réponse (extrait):**
```json
{
  "provider": "rapidapi",
  "kind": "natal_transits",
  "insights": {
    "major_aspects": [
      {
        "transit_planet": "Jupiter",
        "natal_planet": "Sun",
        "aspect": "trine",
        "orb": 0.5,
        "interpretation": "Jupiter harmonise votre Soleil natal..."
      },
      {
        "transit_planet": "Saturn",
        "natal_planet": "Moon",
        "aspect": "square",
        "orb": 2.0,
        "interpretation": "Saturn crée une friction avec votre Lune natale..."
      }
    ],
    "energy_level": "medium"
  }
}
```

**Note:** 2 aspects retournés (trine, square) - le sextile (aspect mineur) a été filtré.

---

## 2. Transits Révolution Lunaire (POST /api/transits/lunar_return)

### Exemple 2.1: Tous les aspects

**Requête:**
```bash
curl -X POST "http://localhost:8000/api/transits/lunar_return" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "123e4567-e89b-12d3-a456-426614174000",
    "month": "2025-01",
    "lunar_return_date": "2025-01-05",
    "transit_date": "2025-01-15",
    "birth_date": "1989-04-15",
    "birth_time": "14:30",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522
  }'
```

**Réponse (extrait):**
```json
{
  "provider": "rapidapi",
  "kind": "lunar_return_transits",
  "insights": {
    "major_aspects": [
      {
        "transit_planet": "Mars",
        "natal_planet": "Venus",
        "aspect": "opposition",
        "orb": 1.0
      },
      {
        "transit_planet": "Mercury",
        "natal_planet": "Jupiter",
        "aspect": "quincunx",
        "orb": 2.5
      }
    ]
  }
}
```

---

### Exemple 2.2: Uniquement les aspects majeurs

**Requête:**
```bash
curl -X POST "http://localhost:8000/api/transits/lunar_return?major_only=true" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "123e4567-e89b-12d3-a456-426614174000",
    "month": "2025-01",
    "lunar_return_date": "2025-01-05",
    "transit_date": "2025-01-15",
    "birth_date": "1989-04-15",
    "birth_time": "14:30",
    "birth_latitude": 48.8566,
    "birth_longitude": 2.3522
  }'
```

**Réponse (extrait):**
```json
{
  "provider": "rapidapi",
  "kind": "lunar_return_transits",
  "insights": {
    "major_aspects": [
      {
        "transit_planet": "Mars",
        "natal_planet": "Venus",
        "aspect": "opposition",
        "orb": 1.0
      }
    ]
  }
}
```

**Note:** Le quincunx (aspect mineur) a été filtré.

---

## 3. Récupération depuis le cache (GET /api/transits/overview/{user_id}/{month})

### Exemple 3.1: Tous les aspects

**Requête:**
```bash
curl -X GET "http://localhost:8000/api/transits/overview/123e4567-e89b-12d3-a456-426614174000/2025-01" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Réponse (extrait):**
```json
{
  "id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "month": "2025-01",
  "overview": {
    "natal_transits": {
      "events": [...]
    },
    "insights": {
      "major_aspects": [
        {"aspect": "trine", ...},
        {"aspect": "sextile", ...},
        {"aspect": "square", ...}
      ]
    }
  }
}
```

---

### Exemple 3.2: Uniquement les aspects majeurs (filtrage à la volée)

**Requête:**
```bash
curl -X GET "http://localhost:8000/api/transits/overview/123e4567-e89b-12d3-a456-426614174000/2025-01?major_only=true" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Réponse (extrait):**
```json
{
  "id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "month": "2025-01",
  "overview": {
    "natal_transits": {
      "events": [...]
    },
    "insights": {
      "major_aspects": [
        {"aspect": "trine", ...},
        {"aspect": "square", ...}
      ]
    }
  }
}
```

**Note:** Le sextile a été filtré à la volée lors de la récupération.

---

## 4. Comparaison des aspects majeurs vs mineurs

### Aspects INCLUS avec major_only=true

| Aspect | Angle | Symbole | Exemple d'interprétation |
|--------|-------|---------|--------------------------|
| **Conjonction** | 0° | ☌ | Jupiter fusionne avec votre Soleil natal. Amplification de l'énergie personnelle. |
| **Opposition** | 180° | ☍ | Saturne s'oppose à votre Lune natale. Tension émotionnelle, besoin d'équilibre. |
| **Carré** | 90° | □ | Mars crée une friction avec votre Vénus natale. Conflits relationnels possibles. |
| **Trigone** | 120° | △ | Vénus harmonise votre Jupiter natal. Facilité, opportunités, fluidité. |

### Aspects EXCLUS avec major_only=true

| Aspect | Angle | Symbole | Raison de l'exclusion |
|--------|-------|---------|----------------------|
| Sextile | 60° | ⚹ | Aspect mineur (harmonique) |
| Quinconce | 150° | ⚻ | Aspect mineur (ajustement) |
| Semi-carré | 45° | ∠ | Aspect mineur (friction légère) |
| Sesqui-carré | 135° | ⚼ | Aspect mineur (friction) |
| Semi-sextile | 30° | ⚺ | Aspect mineur (connexion faible) |

---

## 5. Cas d'usage pratiques

### Cas 1: Application mobile - Vue simplifiée
**Besoin:** Afficher uniquement les transits les plus importants pour ne pas surcharger l'interface mobile.

**Solution:**
```javascript
// Frontend (React Native / Expo)
const fetchNatalTransits = async (birthData, transitDate) => {
  const response = await fetch(
    `${API_URL}/api/transits/natal?major_only=true`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...birthData,
        transit_date: transitDate
      })
    }
  );

  const data = await response.json();
  // data.insights.major_aspects ne contiendra que les 4 aspects majeurs
  return data;
};
```

---

### Cas 2: Vue détaillée - Tous les aspects
**Besoin:** Expert en astrologie voulant voir TOUS les aspects pour une analyse approfondie.

**Solution:**
```javascript
const fetchAllTransits = async (birthData, transitDate) => {
  const response = await fetch(
    `${API_URL}/api/transits/natal?major_only=false`,
    // ou simplement: `${API_URL}/api/transits/natal` (major_only=false par défaut)
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...birthData,
        transit_date: transitDate
      })
    }
  );

  const data = await response.json();
  // data.insights.major_aspects contiendra TOUS les aspects
  return data;
};
```

---

### Cas 3: Toggle utilisateur - Choix dynamique
**Besoin:** Permettre à l'utilisateur de basculer entre vue simplifiée et vue détaillée.

**Solution:**
```javascript
// Frontend component
const TransitsView = () => {
  const [showMajorOnly, setShowMajorOnly] = useState(true);
  const [transits, setTransits] = useState(null);

  const fetchTransits = async () => {
    const response = await fetch(
      `${API_URL}/api/transits/natal?major_only=${showMajorOnly}`,
      { /* ... */ }
    );
    const data = await response.json();
    setTransits(data);
  };

  return (
    <View>
      <Switch
        value={showMajorOnly}
        onValueChange={(value) => {
          setShowMajorOnly(value);
          fetchTransits();
        }}
        label="Aspects majeurs uniquement"
      />
      <TransitsList aspects={transits?.insights?.major_aspects} />
    </View>
  );
};
```

---

## 6. Validation du comportement

### Test manuel avec curl

**1. Créer un POST avec tous les aspects:**
```bash
curl -X POST "http://localhost:8000/api/transits/natal" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1989-04-15",
    "transit_date": "2025-01-15"
  }' | jq '.insights.major_aspects | length'
```
**Sortie attendue:** Nombre total d'aspects (ex: 6)

---

**2. Créer un POST avec aspects majeurs uniquement:**
```bash
curl -X POST "http://localhost:8000/api/transits/natal?major_only=true" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1989-04-15",
    "transit_date": "2025-01-15"
  }' | jq '.insights.major_aspects | length'
```
**Sortie attendue:** Nombre d'aspects majeurs uniquement (ex: 3 ou 4)

---

**3. Vérifier les types d'aspects retournés:**
```bash
curl -X POST "http://localhost:8000/api/transits/natal?major_only=true" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1989-04-15",
    "transit_date": "2025-01-15"
  }' | jq '.insights.major_aspects[].aspect'
```
**Sortie attendue:**
```json
"conjunction"
"opposition"
"square"
"trine"
```
**JAMAIS:**
```json
"sextile"
"quincunx"
"semisquare"
```

---

## 7. Débogage

### Vérifier si le filtrage est appliqué

**Script Python de test:**
```python
import requests

# Tous les aspects
response_all = requests.post(
    "http://localhost:8000/api/transits/natal",
    json={"birth_date": "1989-04-15", "transit_date": "2025-01-15"}
)
all_aspects = response_all.json()["insights"]["major_aspects"]

# Aspects majeurs uniquement
response_major = requests.post(
    "http://localhost:8000/api/transits/natal?major_only=true",
    json={"birth_date": "1989-04-15", "transit_date": "2025-01-15"}
)
major_aspects = response_major.json()["insights"]["major_aspects"]

print(f"Tous les aspects: {len(all_aspects)}")
print(f"Aspects majeurs: {len(major_aspects)}")

# Vérifier que major_only a réduit le nombre d'aspects
assert len(major_aspects) <= len(all_aspects), "Le filtrage doit réduire le nombre d'aspects"

# Vérifier que seuls les 4 types majeurs sont présents
major_types = [a["aspect"] for a in major_aspects]
allowed_types = ["conjunction", "opposition", "square", "trine"]

for aspect_type in major_types:
    assert aspect_type in allowed_types, f"{aspect_type} ne devrait pas être dans les aspects majeurs"

print("✅ Filtrage major_only fonctionne correctement!")
```

---

## 8. Performances et optimisation

### Impact du filtrage sur les performances

| Scénario | Aspects retournés | Temps de réponse | Réduction |
|----------|-------------------|------------------|-----------|
| `major_only=false` | 10-15 aspects | ~500ms | - |
| `major_only=true` | 3-5 aspects | ~450ms | ~10% |

**Note:** Le filtrage backend est très rapide (< 1ms) car il s'agit d'un simple filtrage de liste en mémoire.

---

### Recommandations

1. **Mobile app (vue principale):** Utiliser `major_only=true` pour simplifier l'interface
2. **Vue détaillée:** Utiliser `major_only=false` pour analyse complète
3. **Cache:** Les données brutes sont conservées en DB, le filtrage est appliqué à la lecture
4. **Monitoring:** Suivre l'utilisation de `major_only=true` vs `false` pour optimiser l'API

---

## 9. Résolution de problèmes

### Problème 1: Le filtrage ne semble pas fonctionner
**Symptôme:** Tous les aspects sont retournés même avec `major_only=true`

**Causes possibles:**
1. Paramètre mal formé: `major_only=True` (majuscule) au lieu de `major_only=true`
2. Paramètre dans le body au lieu de query string
3. Ancienne version du code avant commit f3cde98

**Solution:**
```bash
# ✅ CORRECT
curl -X POST "http://localhost:8000/api/transits/natal?major_only=true"

# ❌ INCORRECT (True en majuscule)
curl -X POST "http://localhost:8000/api/transits/natal?major_only=True"

# ❌ INCORRECT (dans le body)
curl -X POST "http://localhost:8000/api/transits/natal" \
  -H "Content-Type: application/json" \
  -d '{"major_only": true}'
```

---

### Problème 2: Aspects mineurs toujours présents
**Symptôme:** Sextile ou quinconce retournés même avec `major_only=true`

**Cause possible:** Erreur dans la fonction `filter_major_aspects_only()`

**Vérification:**
```bash
cd apps/api
pytest tests/test_transits_major.py::test_generate_transit_insights_major_only_four_types -v
```

Si le test échoue, vérifier le code dans `/apps/api/services/transits_services.py` ligne 145-168.

---

## 10. Conclusion

Le paramètre `major_only` offre une flexibilité totale pour adapter la réponse API aux besoins de l'utilisateur final:

- **Vue simplifiée (mobile):** `major_only=true` → 3-5 aspects majeurs
- **Vue détaillée (expert):** `major_only=false` → 10-15 aspects complets
- **Toggle dynamique:** Changement à la volée sans recharger les données

**Documentation complète:**
- Détails techniques: `/apps/api/docs/TRANSITS_MAJOR_FILTERING.md`
- Résumé: `/apps/api/docs/TRANSITS_MAJOR_FILTERING_SUMMARY.md`
- Exemples: `/apps/api/docs/TRANSITS_MAJOR_FILTERING_EXAMPLES.md` (ce fichier)

**Tests:**
- Tests unitaires: `pytest tests/test_transits_major.py` (12 tests)
- Validation manuelle: `python scripts/test_major_only_flow.py` (5 tests)
