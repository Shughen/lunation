"""add pregenerated natal aspects table

Revision ID: 3a7b8c9d0e1f
Revises: 29640bcd2fc6
Create Date: 2026-01-20 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '3a7b8c9d0e1f'
down_revision = '29640bcd2fc6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Creer la table pregenerated_natal_aspects
    op.create_table(
        'pregenerated_natal_aspects',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('planet1', sa.String(50), nullable=False),
        sa.Column('planet2', sa.String(50), nullable=False),
        sa.Column('aspect_type', sa.String(50), nullable=False),
        sa.Column('version', sa.Integer, nullable=False, server_default='2'),
        sa.Column('lang', sa.String(10), nullable=False, server_default='fr'),
        sa.Column('content', sa.Text, nullable=False),
        sa.Column('length', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )

    # Creer les index
    op.create_index('idx_aspect_unique', 'pregenerated_natal_aspects',
                    ['planet1', 'planet2', 'aspect_type', 'version', 'lang'], unique=True)
    op.create_index('idx_aspect_lookup', 'pregenerated_natal_aspects',
                    ['planet1', 'planet2', 'aspect_type', 'version', 'lang'])
    op.create_index('idx_aspect_created_at', 'pregenerated_natal_aspects', ['created_at'])


def downgrade() -> None:
    # Supprimer les index
    op.drop_index('idx_aspect_created_at', 'pregenerated_natal_aspects')
    op.drop_index('idx_aspect_lookup', 'pregenerated_natal_aspects')
    op.drop_index('idx_aspect_unique', 'pregenerated_natal_aspects')

    # Supprimer la table
    op.drop_table('pregenerated_natal_aspects')
