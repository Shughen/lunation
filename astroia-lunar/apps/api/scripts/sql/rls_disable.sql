-- Script: Désactiver Row Level Security (RLS) sur les tables Astroia Lunar
-- Date: 2025-01-23
-- Contexte: FastAPI gère l'authentification et l'autorisation côté application
--
-- DÉCISION: Désactiver RLS car FastAPI protège déjà les routes avec get_current_user()
--
-- Justification:
-- 1. FastAPI vérifie le JWT et extrait user_id via get_current_user() (Depends)
-- 2. Toutes les routes sensibles nécessitent authentification (401 sans token)
-- 3. RLS avec JWT nécessite sync FastAPI ↔ PostgreSQL (complexe, fragile)
-- 4. RLS policies actuelles utilisent email (inefficace) au lieu de sub
-- 5. Protection double-couche (FastAPI + RLS) = overhead sans bénéfice sécurité
--
-- Voir: apps/api/archives/RLS_DECISION.md pour détails complets

-- ============================================================================
-- ÉTAPE 1: Vérifier l'état actuel de RLS
-- ============================================================================

-- Voir quelles tables ont RLS activé
SELECT
    schemaname,
    tablename,
    rowsecurity AS rls_enabled
FROM pg_tables
WHERE schemaname = 'public'
    AND tablename IN (
        'users',
        'natal_charts',
        'lunar_returns',
        'lunar_reports',
        'transits_overview',
        'transits_events',
        'journal_entries',
        'lunar_interpretations',
        'natal_interpretations',
        'natal_aspect_interpretations',
        'voc_windows',
        'lunar_events'
    )
ORDER BY tablename;

-- ============================================================================
-- ÉTAPE 2: Lister toutes les policies RLS existantes
-- ============================================================================

SELECT
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual,
    with_check
FROM pg_policies
WHERE schemaname = 'public'
ORDER BY tablename, policyname;

-- ============================================================================
-- ÉTAPE 3: Supprimer toutes les policies RLS existantes
-- ============================================================================

-- Users
DROP POLICY IF EXISTS allow_select_own_rows ON users;
DROP POLICY IF EXISTS allow_insert_own_rows ON users;
DROP POLICY IF EXISTS allow_update_own_rows ON users;
DROP POLICY IF EXISTS allow_delete_own_rows ON users;

-- Natal Charts
DROP POLICY IF EXISTS allow_select_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_insert_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_update_own_rows ON natal_charts;
DROP POLICY IF EXISTS allow_delete_own_rows ON natal_charts;

-- Lunar Returns
DROP POLICY IF EXISTS allow_select_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_insert_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_update_own_rows ON lunar_returns;
DROP POLICY IF EXISTS allow_delete_own_rows ON lunar_returns;

-- Lunar Reports
DROP POLICY IF EXISTS allow_select_own_rows ON lunar_reports;
DROP POLICY IF EXISTS allow_insert_own_rows ON lunar_reports;
DROP POLICY IF EXISTS allow_update_own_rows ON lunar_reports;
DROP POLICY IF EXISTS allow_delete_own_rows ON lunar_reports;

-- Transits Overview
DROP POLICY IF EXISTS allow_select_own_rows ON transits_overview;
DROP POLICY IF EXISTS allow_insert_own_rows ON transits_overview;
DROP POLICY IF EXISTS allow_update_own_rows ON transits_overview;
DROP POLICY IF EXISTS allow_delete_own_rows ON transits_overview;

-- Transits Events
DROP POLICY IF EXISTS allow_select_own_rows ON transits_events;
DROP POLICY IF EXISTS allow_insert_own_rows ON transits_events;
DROP POLICY IF EXISTS allow_update_own_rows ON transits_events;
DROP POLICY IF EXISTS allow_delete_own_rows ON transits_events;

-- Journal Entries
DROP POLICY IF EXISTS allow_select_own_rows ON journal_entries;
DROP POLICY IF EXISTS allow_insert_own_rows ON journal_entries;
DROP POLICY IF EXISTS allow_update_own_rows ON journal_entries;
DROP POLICY IF EXISTS allow_delete_own_rows ON journal_entries;

-- Lunar Interpretations (table publique de référence)
DROP POLICY IF EXISTS allow_select_all ON lunar_interpretations;

-- Natal Interpretations (table publique de référence)
DROP POLICY IF EXISTS allow_select_all ON natal_interpretations;

-- Natal Aspect Interpretations (table publique de référence)
DROP POLICY IF EXISTS allow_select_all ON natal_aspect_interpretations;

-- VoC Windows (table publique partagée)
DROP POLICY IF EXISTS allow_select_all ON voc_windows;

-- Lunar Events (table publique partagée)
DROP POLICY IF EXISTS allow_select_all ON lunar_events;

-- ============================================================================
-- ÉTAPE 4: Désactiver RLS sur toutes les tables
-- ============================================================================

-- Tables utilisateur (protégées côté FastAPI)
ALTER TABLE IF EXISTS users DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS natal_charts DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS lunar_returns DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS lunar_reports DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS transits_overview DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS transits_events DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS journal_entries DISABLE ROW LEVEL SECURITY;

-- Tables de référence publiques (pas de RLS nécessaire)
ALTER TABLE IF EXISTS lunar_interpretations DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS natal_interpretations DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS natal_aspect_interpretations DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS voc_windows DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS lunar_events DISABLE ROW LEVEL SECURITY;

-- ============================================================================
-- ÉTAPE 5: Vérification finale
-- ============================================================================

-- Vérifier que RLS est désactivé partout
SELECT
    schemaname,
    tablename,
    rowsecurity AS rls_enabled
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY tablename;

-- Résultat attendu: rowsecurity = false (f) pour toutes les tables

-- Vérifier qu'il n'y a plus de policies
SELECT
    schemaname,
    tablename,
    policyname
FROM pg_policies
WHERE schemaname = 'public'
ORDER BY tablename, policyname;

-- Résultat attendu: 0 lignes (aucune policy)

-- ============================================================================
-- NOTES POST-MIGRATION
-- ============================================================================

-- ✅ Sécurité maintenue par:
--   - JWT validation dans get_current_user() (routes/auth.py)
--   - Depends(get_current_user) sur toutes les routes sensibles
--   - FK avec CASCADE DELETE pour intégrité référentielle
--   - Validation des paramètres dans les routes

-- ⚠️ Points de vigilance:
--   - S'assurer que toutes les routes utilisent get_current_user()
--   - Ne jamais exposer user_id en paramètre URL (utiliser current_user.id)
--   - Tester authentification avec pytest (401 sans token, 200 avec token)

-- 📋 Tests recommandés après migration:
--   - pytest tests/test_auth.py -v
--   - pytest tests/test_lunar_report_userid_security.py -v
--   - curl localhost:8000/api/natal-reading/reading (doit retourner 401)
--   - curl -H "Authorization: Bearer $TOKEN" localhost:8000/api/natal-reading/reading (200)
