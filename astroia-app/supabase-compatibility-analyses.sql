-- Table pour stocker les analyses de compatibilité (couple, amis, collègues)
CREATE TABLE IF NOT EXISTS compatibility_analyses (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  
  -- Type de relation
  relation_type VARCHAR(20) NOT NULL,
  
  -- Personne 1
  person1_name VARCHAR(100),
  person1_sun INTEGER NOT NULL,
  person1_moon INTEGER NOT NULL,
  person1_ascendant INTEGER NOT NULL,
  
  -- Personne 2
  person2_name VARCHAR(100),
  person2_sun INTEGER NOT NULL,
  person2_moon INTEGER NOT NULL,
  person2_ascendant INTEGER NOT NULL,
  
  -- Scores
  global_score INTEGER NOT NULL,
  communication_score INTEGER,
  passion_score INTEGER,
  complicity_score INTEGER,
  goals_score INTEGER,
  
  -- Metadata
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
  
  -- Contraintes
  CONSTRAINT valid_relation_type CHECK (relation_type IN ('couple', 'friends', 'colleagues')),
  CONSTRAINT valid_scores CHECK (
    global_score BETWEEN 0 AND 100 AND
    communication_score BETWEEN 0 AND 100 AND
    passion_score BETWEEN 0 AND 100 AND
    complicity_score BETWEEN 0 AND 100 AND
    goals_score BETWEEN 0 AND 100
  ),
  CONSTRAINT valid_signs CHECK (
    person1_sun BETWEEN 1 AND 12 AND
    person1_moon BETWEEN 1 AND 12 AND
    person1_ascendant BETWEEN 1 AND 12 AND
    person2_sun BETWEEN 1 AND 12 AND
    person2_moon BETWEEN 1 AND 12 AND
    person2_ascendant BETWEEN 1 AND 12
  )
);

-- Index pour performances
CREATE INDEX IF NOT EXISTS idx_compatibility_analyses_user_id ON compatibility_analyses(user_id);
CREATE INDEX IF NOT EXISTS idx_compatibility_analyses_created_at ON compatibility_analyses(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_compatibility_analyses_type ON compatibility_analyses(relation_type);

-- RLS (Row Level Security)
ALTER TABLE compatibility_analyses ENABLE ROW LEVEL SECURITY;

-- Policy : L'utilisateur ne peut voir que ses analyses
CREATE POLICY "Users can view own compatibility analyses" 
  ON compatibility_analyses
  FOR SELECT
  USING (auth.uid() = user_id);

-- Policy : L'utilisateur peut créer ses analyses
CREATE POLICY "Users can insert own compatibility analyses" 
  ON compatibility_analyses
  FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Policy : L'utilisateur peut supprimer ses analyses
CREATE POLICY "Users can delete own compatibility analyses" 
  ON compatibility_analyses
  FOR DELETE
  USING (auth.uid() = user_id);

-- Vue pour statistiques par type
CREATE OR REPLACE VIEW compatibility_stats AS
SELECT 
  user_id,
  relation_type,
  COUNT(*) as total_analyses,
  ROUND(AVG(global_score), 1) as avg_score,
  MAX(global_score) as max_score,
  MIN(global_score) as min_score
FROM compatibility_analyses
GROUP BY user_id, relation_type;

-- Fonction pour limiter à 100 analyses par utilisateur
CREATE OR REPLACE FUNCTION limit_compatibility_analyses()
RETURNS TRIGGER AS $$
DECLARE
  analysis_count INTEGER;
BEGIN
  SELECT COUNT(*) INTO analysis_count
  FROM compatibility_analyses
  WHERE user_id = NEW.user_id;
  
  -- Si plus de 100, supprimer les plus anciennes
  IF analysis_count >= 100 THEN
    DELETE FROM compatibility_analyses
    WHERE id IN (
      SELECT id FROM compatibility_analyses
      WHERE user_id = NEW.user_id
      ORDER BY created_at ASC
      LIMIT (analysis_count - 99)
    );
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger pour limiter les analyses
DROP TRIGGER IF EXISTS trigger_limit_compatibility_analyses ON compatibility_analyses;
CREATE TRIGGER trigger_limit_compatibility_analyses
  AFTER INSERT ON compatibility_analyses
  FOR EACH ROW
  EXECUTE FUNCTION limit_compatibility_analyses();

-- Commentaires
COMMENT ON TABLE compatibility_analyses IS 'Analyses de compatibilité entre deux personnes';
COMMENT ON COLUMN compatibility_analyses.relation_type IS 'Type : couple, friends, colleagues';
COMMENT ON COLUMN compatibility_analyses.global_score IS 'Score global de compatibilité (0-100)';
COMMENT ON COLUMN compatibility_analyses.communication_score IS 'Score de communication';
COMMENT ON COLUMN compatibility_analyses.passion_score IS 'Score de passion/énergie';
COMMENT ON COLUMN compatibility_analyses.complicity_score IS 'Score de complicité';
COMMENT ON COLUMN compatibility_analyses.goals_score IS 'Score d''alignement des objectifs';

