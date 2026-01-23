"""add_performance_indexes_natal_lunar

Optimizations de performance pour queries critiques:
- Index sur natal_charts.user_id pour lookup rapide
- Index sur lunar_reports.created_at pour cache expiration queries

Revision ID: ef694464b50e
Revises: 4b8c9d0e2f1a
Create Date: 2026-01-23 12:03:10.093636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef694464b50e'
down_revision = '4b8c9d0e2f1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Index sur natal_charts.user_id pour accélération lookup par utilisateur
    # Note: UNIQUE constraint crée déjà un index, mais on l'explicite pour garantir la performance
    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_natal_charts_user_id
        ON natal_charts (user_id)
    """)

    # Index sur lunar_reports.created_at pour queries de cache expiration
    # Utilisé pour filtrer les rapports obsolètes (> 30 jours)
    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_lunar_reports_created_at
        ON lunar_reports (created_at DESC)
    """)

    # Index composite sur lunar_reports (user_id, created_at) pour queries combinées
    # Optimise "SELECT * FROM lunar_reports WHERE user_id = ? ORDER BY created_at DESC"
    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_lunar_reports_user_created
        ON lunar_reports (user_id, created_at DESC)
    """)


def downgrade() -> None:
    # Supprimer les index dans l'ordre inverse
    op.execute("DROP INDEX IF EXISTS idx_lunar_reports_user_created")
    op.execute("DROP INDEX IF EXISTS idx_lunar_reports_created_at")
    op.execute("DROP INDEX IF EXISTS idx_natal_charts_user_id")

