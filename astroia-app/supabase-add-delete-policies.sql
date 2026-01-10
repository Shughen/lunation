
-- Ajouter les permissions DELETE manquantes pour profiles
CREATE POLICY IF NOT EXISTS "Users can delete own profile" ON public.profiles
  FOR DELETE USING (auth.uid() = id);

-- Ajouter les permissions DELETE manquantes pour natal_charts (devrait déjà exister mais on vérifie)
CREATE POLICY IF NOT EXISTS "Users can delete own natal charts" ON public.natal_charts
  FOR DELETE USING (auth.uid() = user_id);

-- Note: Ces policies doivent être exécutées dans Supabase SQL Editor
-- pour permettre aux utilisateurs de supprimer leurs propres données
