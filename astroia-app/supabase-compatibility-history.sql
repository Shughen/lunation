-- Table pour stocker l'historique des analyses de compatibilité parent-enfant
CREATE TABLE IF NOT EXISTS compatibility_history (
  id UUID DEFAULT gen_random_uuid() PRIMARY_KEY,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  
  -- Données parent
  parent_sun_sign INTEGER NOT NULL,
  parent_moon_sign INTEGER NOT NULL,
  parent_ascendant INTEGER NOT NULL,
  
  -- Données enfant
  child_sun_sign INTEGER NOT NULL,
  child_moon_sign INTEGER NOT NULL,
  child_ascendant INTEGER NOT NULL,
  
  -- Résultat
  compatibility_score INTEGER NOT NULL,
  interpretation_level VARCHAR(50),
  interpretation_emoji VARCHAR(10),
  
  -- Metadata
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
  
  -- Contraintes
  CONSTRAINT valid_score CHECK (compatibility_score >= 0 AND compatibility_score <= 100),
  CONSTRAINT valid_signs CHECK (
    parent_sun_sign BETWEEN 1 AND 12 AND
    parent_moon_sign BETWEEN 1 AND 12 AND
    parent_ascendant BETWEEN 1 AND 12 AND
    child_sun_sign BETWEEN 1 AND 12 AND
    child_moon_sign BETWEEN 1 AND 12 AND
    child_ascendant BETWEEN 1 AND 12
  )
);

-- Index pour performances
CREATE INDEX IF NOT EXISTS idx_compatibility_history_user_id ON compatibility_history(user_id);
CREATE INDEX IF NOT EXISTS idx_compatibility_history_created_at ON compatibility_history(created_at DESC);

-- RLS (Row Level Security)
ALTER TABLE compatibility_history ENABLE ROW LEVEL SECURITY;

-- Policy : L'utilisateur ne peut voir que son historique
CREATE POLICY "Users can view own compatibility history" 
  ON compatibility_history
  FOR SELECT
  USING (auth.uid() = user_id);

-- Policy : L'utilisateur peut insérer dans son historique
CREATE POLICY "Users can insert own compatibility history" 
  ON compatibility_history
  FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Policy : L'utilisateur peut supprimer son historique
CREATE POLICY "Users can delete own compatibility history" 
  ON compatibility_history
  FOR DELETE
  USING (auth.uid() = user_id);

-- Fonction pour limiter à 50 analyses par utilisateur (optionnel)
CREATE OR REPLACE FUNCTION limit_compatibility_history()
RETURNS TRIGGER AS $$
DECLARE
  history_count INTEGER;
BEGIN
  SELECT COUNT(*) INTO history_count
  FROM compatibility_history
  WHERE user_id = NEW.user_id;
  
  -- Si plus de 50, supprimer les plus anciennes
  IF history_count >= 50 THEN
    DELETE FROM compatibility_history
    WHERE id IN (
      SELECT id FROM compatibility_history
      WHERE user_id = NEW.user_id
      ORDER BY created_at ASC
      LIMIT (history_count - 49)
    );
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger pour limiter l'historique
DROP TRIGGER IF EXISTS trigger_limit_compatibility_history ON compatibility_history;
CREATE TRIGGER trigger_limit_compatibility_history
  AFTER INSERT ON compatibility_history
  FOR EACH ROW
  EXECUTE FUNCTION limit_compatibility_history();

-- Commentaires
COMMENT ON TABLE compatibility_history IS 'Historique des analyses de compatibilité parent-enfant';
COMMENT ON COLUMN compatibility_history.compatibility_score IS 'Score de compatibilité (0-100)';
COMMENT ON COLUMN compatibility_history.interpretation_level IS 'Niveau : Excellente, Bonne, Moyenne, Délicate';

