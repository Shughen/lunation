-- Table d'audit des consentements RGPD
-- Conserve l'historique de tous les consentements (accordés, modifiés, révoqués)

CREATE TABLE IF NOT EXISTS public.consents_audit (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  
  -- Type de consentement
  consent_type TEXT NOT NULL, -- 'health' | 'analytics'
  
  -- Statut
  status TEXT NOT NULL, -- 'granted' | 'revoked' | 'modified'
  
  -- Contexte
  surface TEXT, -- 'onboarding' | 'settings' | 'deeplink'
  policy_version TEXT NOT NULL, -- Ex: 'v2.0.0'
  
  -- Metadata
  ip_address TEXT,
  user_agent TEXT,
  
  -- Timestamps
  created_at TIMESTAMPTZ DEFAULT NOW(),
  
  -- Index pour requêtes rapides
  CONSTRAINT valid_type CHECK (consent_type IN ('health', 'analytics')),
  CONSTRAINT valid_status CHECK (status IN ('granted', 'revoked', 'modified'))
);

-- Index pour récupération rapide
CREATE INDEX idx_consents_user_id ON public.consents_audit(user_id);
CREATE INDEX idx_consents_type ON public.consents_audit(consent_type);
CREATE INDEX idx_consents_created_at ON public.consents_audit(created_at DESC);

-- RLS (Row Level Security)
ALTER TABLE public.consents_audit ENABLE ROW LEVEL SECURITY;

-- Policy : utilisateur voit seulement ses consentements
CREATE POLICY "Users can view own consents" 
  ON public.consents_audit
  FOR SELECT 
  USING (auth.uid() = user_id);

-- Policy : utilisateur peut créer ses consentements
CREATE POLICY "Users can create own consents" 
  ON public.consents_audit
  FOR INSERT 
  WITH CHECK (auth.uid() = user_id);

-- Policy : pas de modification (audit trail immuable)
-- Pas de DELETE non plus (on garde l'historique)

COMMENT ON TABLE public.consents_audit IS 'Audit trail des consentements RGPD - Art. 7.1 (preuve du consentement)';
COMMENT ON COLUMN public.consents_audit.consent_type IS 'Type: health (Art.9) ou analytics (Art.6)';
COMMENT ON COLUMN public.consents_audit.status IS 'granted = accordé, revoked = retiré, modified = modifié';
COMMENT ON COLUMN public.consents_audit.surface IS 'Où le consentement a été donné/retiré';
COMMENT ON COLUMN public.consents_audit.policy_version IS 'Version de la politique au moment du consentement';

