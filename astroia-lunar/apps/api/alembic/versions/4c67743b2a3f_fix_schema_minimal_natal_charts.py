"""fix schema minimal natal_charts

Revision ID: 4c67743b2a3f
Revises: a1b2c3d4e5f6
Create Date: 2026-01-17 14:35:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4c67743b2a3f'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Ajouter les colonnes manquantes à natal_charts (avec server_default pour éviter NOT NULL errors)
    op.execute("""
        ALTER TABLE natal_charts
        ADD COLUMN IF NOT EXISTS birth_date DATE,
        ADD COLUMN IF NOT EXISTS birth_time TIME,
        ADD COLUMN IF NOT EXISTS birth_place TEXT,
        ADD COLUMN IF NOT EXISTS latitude NUMERIC(9,6),
        ADD COLUMN IF NOT EXISTS longitude NUMERIC(9,6),
        ADD COLUMN IF NOT EXISTS timezone TEXT,
        ADD COLUMN IF NOT EXISTS computed_at TIMESTAMPTZ DEFAULT NOW(),
        ADD COLUMN IF NOT EXISTS version TEXT DEFAULT 'v1-simplified',
        ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ DEFAULT NOW(),
        ADD COLUMN IF NOT EXISTS updated_at TIMESTAMPTZ DEFAULT NOW()
    """)

    # Ajouter la colonne overview à transits_overview
    op.execute("""
        ALTER TABLE transits_overview
        ADD COLUMN IF NOT EXISTS overview JSONB NOT NULL DEFAULT '{}'::jsonb
    """)

    # Rendre positions NOT NULL sur natal_charts (si la colonne existe déjà)
    op.execute("""
        ALTER TABLE natal_charts
        ALTER COLUMN positions SET NOT NULL
    """)


def downgrade() -> None:
    # Rollback: supprimer les colonnes ajoutées
    op.execute("""
        ALTER TABLE natal_charts
        DROP COLUMN IF EXISTS birth_date,
        DROP COLUMN IF EXISTS birth_time,
        DROP COLUMN IF EXISTS birth_place,
        DROP COLUMN IF EXISTS latitude,
        DROP COLUMN IF EXISTS longitude,
        DROP COLUMN IF EXISTS timezone,
        DROP COLUMN IF EXISTS computed_at,
        DROP COLUMN IF EXISTS version,
        DROP COLUMN IF EXISTS created_at,
        DROP COLUMN IF EXISTS updated_at
    """)

    op.execute("""
        ALTER TABLE transits_overview
        DROP COLUMN IF EXISTS overview
    """)
