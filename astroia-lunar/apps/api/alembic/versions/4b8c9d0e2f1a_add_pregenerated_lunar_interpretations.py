"""add pregenerated lunar interpretations table

Revision ID: 4b8c9d0e2f1a
Revises: 3a7b8c9d0e1f
Create Date: 2026-01-20 14:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB


# revision identifiers, used by Alembic.
revision = '4b8c9d0e2f1a'
down_revision = '3a7b8c9d0e1f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Creer la table pregenerated_lunar_interpretations
    op.create_table(
        'pregenerated_lunar_interpretations',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('moon_sign', sa.String(50), nullable=False),
        sa.Column('moon_house', sa.Integer, nullable=False),
        sa.Column('lunar_ascendant', sa.String(50), nullable=False),
        sa.Column('version', sa.Integer, nullable=False, server_default='1'),
        sa.Column('lang', sa.String(10), nullable=False, server_default='fr'),
        sa.Column('interpretation_full', sa.Text, nullable=False),
        sa.Column('weekly_advice', JSONB, nullable=True),
        sa.Column('length', sa.Integer, nullable=False),
        sa.Column('model_used', sa.String(50), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )

    # Creer les index
    op.create_index('idx_lunar_interp_unique', 'pregenerated_lunar_interpretations',
                    ['moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'], unique=True)
    op.create_index('idx_lunar_interp_lookup', 'pregenerated_lunar_interpretations',
                    ['moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'])
    op.create_index('idx_lunar_interp_created_at', 'pregenerated_lunar_interpretations', ['created_at'])


def downgrade() -> None:
    # Supprimer les index
    op.drop_index('idx_lunar_interp_created_at', 'pregenerated_lunar_interpretations')
    op.drop_index('idx_lunar_interp_lookup', 'pregenerated_lunar_interpretations')
    op.drop_index('idx_lunar_interp_unique', 'pregenerated_lunar_interpretations')

    # Supprimer la table
    op.drop_table('pregenerated_lunar_interpretations')
