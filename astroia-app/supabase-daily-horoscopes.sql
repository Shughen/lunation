-- Table pour stocker les horoscopes quotidiens
CREATE TABLE IF NOT EXISTS daily_horoscopes (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  
  -- Données horoscope
  sign VARCHAR(20) NOT NULL,
  date DATE NOT NULL,
  
  -- Contenu
  work TEXT NOT NULL,
  love TEXT NOT NULL,
  health TEXT NOT NULL,
  advice TEXT NOT NULL,
  
  -- Infos cosmiques
  lucky_number INTEGER,
  moon_sign VARCHAR(20),
  
  -- Metadata
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
  
  -- Contraintes
  UNIQUE(sign, date),
  CONSTRAINT valid_sign CHECK (sign IN (
    'bélier', 'taureau', 'gémeaux', 'cancer',
    'lion', 'vierge', 'balance', 'scorpion',
    'sagittaire', 'capricorne', 'verseau', 'poissons'
  )),
  CONSTRAINT valid_lucky_number CHECK (lucky_number BETWEEN 1 AND 49)
);

-- Index pour performances
CREATE INDEX IF NOT EXISTS idx_daily_horoscopes_sign_date ON daily_horoscopes(sign, date DESC);
CREATE INDEX IF NOT EXISTS idx_daily_horoscopes_date ON daily_horoscopes(date DESC);

-- RLS (Row Level Security)
ALTER TABLE daily_horoscopes ENABLE ROW LEVEL SECURITY;

-- Policy : Tout le monde peut lire les horoscopes
CREATE POLICY "Anyone can view daily horoscopes" 
  ON daily_horoscopes
  FOR SELECT
  USING (true);

-- Policy : Seuls les admins peuvent insérer (via service_role)
CREATE POLICY "Service role can insert horoscopes" 
  ON daily_horoscopes
  FOR INSERT
  WITH CHECK (true);

-- Vue pour les horoscopes récents (7 derniers jours)
CREATE OR REPLACE VIEW recent_horoscopes AS
SELECT *
FROM daily_horoscopes
WHERE date >= CURRENT_DATE - INTERVAL '7 days'
ORDER BY date DESC, sign;

-- Fonction pour nettoyer les vieux horoscopes (>30 jours)
CREATE OR REPLACE FUNCTION cleanup_old_horoscopes()
RETURNS void AS $$
BEGIN
  DELETE FROM daily_horoscopes
  WHERE date < CURRENT_DATE - INTERVAL '30 days';
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Commentaires
COMMENT ON TABLE daily_horoscopes IS 'Horoscopes quotidiens générés par IA';
COMMENT ON COLUMN daily_horoscopes.sign IS 'Signe du zodiaque (minuscules)';
COMMENT ON COLUMN daily_horoscopes.date IS 'Date de l''horoscope';
COMMENT ON COLUMN daily_horoscopes.work IS 'Prédictions travail & carrière';
COMMENT ON COLUMN daily_horoscopes.love IS 'Prédictions amour & relations';
COMMENT ON COLUMN daily_horoscopes.health IS 'Prédictions santé & bien-être';
COMMENT ON COLUMN daily_horoscopes.advice IS 'Conseil du jour';

