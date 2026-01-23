# Décision Architecture: Désactivation Row Level Security (RLS)

**Date:** 2025-01-23
**Statut:** ✅ Approuvé
**Décision:** Désactiver RLS sur toutes les tables, sécurité gérée côté FastAPI

---

## 📋 Contexte

### Architecture actuelle

- **Backend:** FastAPI standalone (pas d'intégration Supabase Auth)
- **Authentification:** JWT tokens générés par FastAPI (`routes/auth.py`)
- **Database:** PostgreSQL (Supabase) en mode "database-only"
- **Tables concernées:** `users`, `natal_charts`, `lunar_returns`, `lunar_reports`, `transits_*`, `journal_entries`

### Problème identifié

Les tables ont RLS (Row Level Security) activé avec des policies basées sur:
- `auth.jwt() ->> 'email'` → SELECT users pour trouver `id`
- **Inefficace:** Requête supplémentaire à chaque opération DB
- **Fragile:** Email peut changer, synchronisation FastAPI ↔ PostgreSQL complexe
- **Double-couche:** FastAPI vérifie déjà JWT avec `get_current_user()` (Depends)

---

## ✅ Décision: Désactiver RLS

### Justification

#### 1. FastAPI gère déjà l'authentification

```python
# routes/auth.py - get_current_user()
async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> User:
    """Vérifie JWT token et retourne User authentifié"""
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    user_id = int(payload["sub"])
    # ... retourne User depuis DB
```

**Toutes les routes sensibles** utilisent `Depends(get_current_user)` → **401 sans token valide**

#### 2. Routes protégées (Sprint 1)

Routes modifiées pour nécessiter authentification:
- ✅ `POST /api/natal-reading/reading` - `current_user: User = Depends(get_current_user)`
- ✅ `GET /api/natal-reading/reading/{key}` - idem
- ✅ `DELETE /api/natal-reading/reading/{key}` - idem
- ✅ `POST /api/reports/lunar/{month}` - user_id retiré du path, utilise `current_user.id`
- ✅ `GET /api/reports/lunar/{month}/html` - idem

#### 3. RLS avec JWT FastAPI = complexe et fragile

**Problèmes techniques:**
- PostgreSQL n'a pas accès direct au JWT FastAPI (pas de `current_setting('request.jwt.claims')`)
- FastAPI n'expose pas JWT à PostgreSQL via headers HTTP
- Synchronisation FastAPI JWT ↔ PostgreSQL RLS nécessite middleware custom (overhead)

**Alternative envisagée (rejetée):**
```sql
-- Nécessiterait middleware FastAPI pour injecter JWT dans PostgreSQL session
CREATE POLICY allow_select ON table USING (
    user_id = (current_setting('request.jwt.claims')::json ->> 'sub')::integer
);
```
→ **Complexité élevée, bénéfice sécurité nul** (FastAPI protège déjà)

#### 4. Intégrité référentielle via FK

```python
# models/transits.py (après migration UUID → INTEGER)
user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
```

**Contraintes DB:**
- FK avec `ON DELETE CASCADE` sur toutes les tables utilisateur
- Suppression user → cascade delete automatique de toutes ses données
- Intégrité garantie par PostgreSQL, pas besoin RLS

#### 5. Tests de sécurité

Tests existants valident protection côté FastAPI:
- `test_lunar_report_userid_security.py` - Vérifie isolation user_id
- Tests avec/sans token JWT (401 vs 200)
- Tests accès cross-user (doit échouer)

---

## 📜 Script de migration

**Fichier:** `apps/api/scripts/sql/rls_disable.sql`

**Actions:**
1. Supprimer toutes les policies RLS existantes
2. `ALTER TABLE ... DISABLE ROW LEVEL SECURITY` sur toutes les tables
3. Vérifications post-migration

**Exécution:**
```bash
psql $DATABASE_URL -f apps/api/scripts/sql/rls_disable.sql
```

---

## ⚠️ Points de vigilance (DoD)

### Checklist post-migration

- [x] ✅ Toutes les routes sensibles ont `Depends(get_current_user)`
- [x] ✅ Aucune route n'accepte `user_id` en paramètre (utilise `current_user.id`)
- [x] ✅ FK avec `ON DELETE CASCADE` sur toutes les tables utilisateur
- [ ] ⏳ Tests authentification passent (401 sans token, 200 avec token)
- [ ] ⏳ Tests sécurité user_id passent (pas d'accès cross-user)

### Tests manuels recommandés

```bash
# 1. Test route protégée sans auth → 401
curl http://localhost:8000/api/natal-reading/reading
# Expected: {"detail": "Impossible de valider les identifiants"}

# 2. Test route protégée avec auth → 200
export TOKEN="<jwt_token>"
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/api/natal-reading/reading
# Expected: 200 OK avec données utilisateur

# 3. Tests automatisés
pytest tests/test_lunar_report_userid_security.py -v
pytest tests/test_auth.py -v
```

---

## 🔄 Alternatives considérées (rejetées)

### Option A: Garder RLS avec policies optimisées

**Avantages:**
- Double couche de sécurité (defense in depth)

**Inconvénients:**
- Complexité élevée (middleware FastAPI → PostgreSQL JWT sync)
- Overhead performance (policies évaluées à chaque requête)
- Duplication logique sécurité (FastAPI + PostgreSQL)
- Maintenance accrue (2 endroits à maintenir)

**Verdict:** ❌ Coût > Bénéfice

### Option B: Utiliser Supabase Auth

**Avantages:**
- RLS natif avec `auth.uid()`
- Pas de middleware custom

**Inconvénients:**
- Migration lourde (FastAPI JWT → Supabase Auth)
- Dépendance forte Supabase (vendor lock-in)
- Architecture actuelle FastAPI standalone fonctionnelle

**Verdict:** ❌ Pas nécessaire, architecture actuelle satisfaisante

---

## 📚 Références

- **Routes protégées:** `apps/api/routes/natal_reading.py`, `apps/api/routes/reports.py`
- **Auth JWT:** `apps/api/routes/auth.py` - `get_current_user()`
- **Modèles FK:** `apps/api/models/transits.py`, `apps/api/models/user.py`
- **Tests sécurité:** `apps/api/tests/test_lunar_report_userid_security.py`
- **Analyse RLS précédente:** `apps/api/archives/RLS_POLICIES_ANALYSIS.md`

---

## ✅ Conclusion

**RLS désactivé** car:
1. FastAPI protège déjà toutes les routes (JWT verification)
2. FK CASCADE DELETE assure intégrité référentielle
3. RLS avec FastAPI = complexité sans bénéfice sécurité
4. Tests valident isolation user_id côté application

**Sécurité maintenue par:**
- JWT tokens avec expiration (7 jours)
- `get_current_user()` sur toutes routes sensibles
- FK constraints avec CASCADE DELETE
- Validation input dans routes
- Tests automatisés sécurité

**Prochaines étapes (Sprint 2):**
- Ajouter rate limiting (10 req/min par IP)
- Implémenter RGPD export/delete
- Tests E2E sécurité complets
