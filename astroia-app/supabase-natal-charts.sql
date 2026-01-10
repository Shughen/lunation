-- ============================================
-- TABLE: natal_charts
-- Thèmes natals calculés
-- ============================================

CREATE TABLE IF NOT EXISTS public.natal_charts (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
  
  -- Données de naissance
  birth_date DATE NOT NULL,
  birth_time TIME NOT NULL,
  birth_place TEXT NOT NULL,
  latitude NUMERIC(9,6) NOT NULL,
  longitude NUMERIC(9,6) NOT NULL,
  timezone TEXT NOT NULL,
  
  -- Positions planétaires (stockées en JSONB)
  positions JSONB NOT NULL,
  
  -- Métadonnées
  computed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  version TEXT DEFAULT 'V1-simplified',
  
  -- Timestamps
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index pour performances
CREATE INDEX IF NOT EXISTS natal_charts_user_id_idx ON public.natal_charts(user_id);
CREATE INDEX IF NOT EXISTS natal_charts_computed_at_idx ON public.natal_charts(computed_at DESC);

-- RLS (Row Level Security)
ALTER TABLE public.natal_charts ENABLE ROW LEVEL SECURITY;

-- Policy: Les utilisateurs peuvent voir leurs propres thèmes
CREATE POLICY "Users can view own natal charts" ON public.natal_charts
  FOR SELECT USING (auth.uid() = user_id);

-- Policy: Les utilisateurs peuvent créer leurs propres thèmes
CREATE POLICY "Users can create own natal charts" ON public.natal_charts
  FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Policy: Les utilisateurs peuvent mettre à jour leurs propres thèmes
CREATE POLICY "Users can update own natal charts" ON public.natal_charts
  FOR UPDATE USING (auth.uid() = user_id);

-- Policy: Les utilisateurs peuvent supprimer leurs propres thèmes
CREATE POLICY "Users can delete own natal charts" ON public.natal_charts
  FOR DELETE USING (auth.uid() = user_id);

-- Trigger pour updated_at
CREATE TRIGGER set_updated_at
  BEFORE UPDATE ON public.natal_charts
  FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- ============================================
-- FONCTION: Vérifier la limite de calcul (1 par 24h)
-- ============================================

CREATE OR REPLACE FUNCTION public.can_compute_natal_chart(p_user_id UUID)
RETURNS BOOLEAN AS $$
DECLARE
  last_computation TIMESTAMP WITH TIME ZONE;
BEGIN
  -- Récupérer la dernière date de calcul
  SELECT computed_at INTO last_computation
  FROM public.natal_charts
  WHERE user_id = p_user_id
  ORDER BY computed_at DESC
  LIMIT 1;
  
  -- Si aucun calcul, autoriser
  IF last_computation IS NULL THEN
    RETURN TRUE;
  END IF;
  
  -- Vérifier si plus de 24h se sont écoulées
  RETURN (NOW() - last_computation) > INTERVAL '24 hours';
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- ============================================
-- Fin du schéma natal_charts
-- ============================================

