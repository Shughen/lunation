-- Migration Supabase : Audit trail consentements RGPD
-- À exécuter dans Dashboard Supabase → SQL Editor

-- Table audit trail consentements RGPD
CREATE TABLE IF NOT EXISTS consent_audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  consent_type TEXT NOT NULL, -- 'health' | 'analytics'
  status TEXT NOT NULL, -- 'granted' | 'revoked'
  surface TEXT NOT NULL, -- 'onboarding' | 'settings' | 'profile'
  timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Index pour requêtes rapides
CREATE INDEX IF NOT EXISTS idx_consent_audit_user
  ON consent_audit_log(user_id, timestamp DESC);

CREATE INDEX IF NOT EXISTS idx_consent_audit_type
  ON consent_audit_log(consent_type, timestamp DESC);

-- Row Level Security
ALTER TABLE consent_audit_log ENABLE ROW LEVEL SECURITY;

-- Policy : utilisateur peut lire ses propres logs
DROP POLICY IF EXISTS "Users can read own audit logs" ON consent_audit_log;
CREATE POLICY "Users can read own audit logs"
  ON consent_audit_log
  FOR SELECT
  USING (auth.uid() = user_id);

-- Policy : insert uniquement via service (tous les utilisateurs authentifiés peuvent insérer leurs propres logs)
DROP POLICY IF EXISTS "Service can insert audit logs" ON consent_audit_log;
CREATE POLICY "Service can insert audit logs"
  ON consent_audit_log
  FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Vérifier que la table a été créée
SELECT 'Table consent_audit_log créée avec succès' AS status;
