# Test du bug de date (-1 jour)

## Symptôme
Quand on envoie `"date": "2001-02-09"`, en base on se retrouve avec `2001-02-08`.

## Logs ajoutés
Les logs suivants ont été ajoutés dans `routes/natal.py` pour tracer le problème :

1. **Ligne ~76** : Log de ce qui est reçu du mobile
   ```
   📅 REÇU DU MOBILE: date=... (type=...), time=..., timezone=...
   ```

2. **Ligne ~104** : Log de ce qui est envoyé à RapidAPI
   ```
   📤 ENVOYÉ À RAPIDAPI: year=..., month=..., day=...
   ```

3. **Ligne ~373** : Log de la conversion date/time
   ```
   🔄 CONVERSION: '2001-02-09' → 2001-02-09 (type=...)
   ```

4. **Ligne ~427** : Log juste avant sauvegarde en base
   ```
   💾 JUSTE AVANT SAUVEGARDE DB:
      birth_date=... (type=...)
   ```

## Test à effectuer

### 1. Lancer l'API avec les logs
```bash
cd apps/api
uvicorn main:app --reload --log-level debug
```

### 2. Appeler l'endpoint POST /api/natal-chart

**Important** : S'assurer d'être authentifié et d'avoir un token valide.

```bash
curl -X POST http://localhost:8000/api/natal-chart \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_TOKEN>' \
  -d '{
    "date": "2001-02-09",
    "time": "11:30",
    "latitude": 44.8378,
    "longitude": -0.5792,
    "place_name": "Bordeaux",
    "timezone": "Europe/Paris"
  }'
```

### 3. Vérifier les logs

Chercher dans les logs de l'API (stdout) :

1. **Ligne REÇU DU MOBILE** : Vérifier que `date=2001-02-09`
2. **Ligne ENVOYÉ À RAPIDAPI** : Vérifier que `day=9`
3. **Ligne CONVERSION** : Vérifier que `2001-02-09 → 2001-02-09`
4. **Ligne JUSTE AVANT SAUVEGARDE** : Vérifier que `birth_date=2001-02-09`

### 4. Vérifier en base

```sql
SELECT id, birth_date, birth_time, positions->'moon' as moon_position
FROM natal_charts
ORDER BY created_at DESC
LIMIT 1;
```

**Si birth_date = 2001-02-08** : Noter à quelle étape dans les logs la date change.

## Scénarios possibles

### Scénario A : Le mobile envoie la mauvaise date
- Les logs montreront `REÇU DU MOBILE: date=2001-02-08`
- → Bug dans le mobile (apps/mobile)

### Scénario B : La conversion backend échoue
- Les logs montreront `REÇU: 2001-02-09` mais `CONVERSION: 2001-02-09 → 2001-02-08`
- → Bug dans `date.fromisoformat()` (peu probable)

### Scénario C : PostgreSQL fait une conversion
- Les logs montreront `JUSTE AVANT SAUVEGARDE: birth_date=2001-02-09`
- Mais en base : `2001-02-08`
- → Problème de timezone dans PostgreSQL (vérifier TIMESTAMP WITH TIME ZONE)

### Scénario D : RapidAPI modifie la date
- Les logs montreront `ENVOYÉ: day=9`
- Mais RapidAPI retourne des données calculées pour le 8
- → Vérifier la timezone dans l'appel RapidAPI

## Solution selon le scénario

### Si A (mobile envoie mauvaise date)
→ Vérifier le code JavaScript/TypeScript dans apps/mobile
→ Chercher `new Date()`, `.toISOString()`, conversions de timezone

### Si B (conversion backend)
→ Vérifier les imports et versions de Python
→ Tester manuellement `date.fromisoformat("2001-02-09")`

### Si C (PostgreSQL)
→ Vérifier le type de colonne : `Column(Date)` pas `Column(DateTime)`
→ Vérifier la timezone de la session PostgreSQL

### Si D (RapidAPI)
→ Vérifier le timezone envoyé à RapidAPI
→ Tester avec différentes timezones

## Après identification du bug

Une fois le scénario identifié, créer un fix et le tester avec :
```bash
python scripts/test_nathan_rapidapi.py
```

Puis vérifier que le thème de Nathan a bien la Lune en Virgo.
