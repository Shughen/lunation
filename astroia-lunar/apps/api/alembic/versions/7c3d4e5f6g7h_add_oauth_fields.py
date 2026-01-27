"""add oauth fields to users table

Revision ID: 7c3d4e5f6g7h
Revises: 6b2c3d4e5f6a
Create Date: 2026-01-27 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c3d4e5f6g7h'
down_revision = '6b2c3d4e5f6a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Ajouter les colonnes OAuth sur la table users
    op.add_column('users', sa.Column('auth_provider', sa.String(20), nullable=True))
    op.add_column('users', sa.Column('provider_id', sa.String(255), nullable=True))

    # Rendre hashed_password nullable (les users OAuth n'ont pas de mot de passe)
    op.alter_column('users', 'hashed_password',
                    existing_type=sa.String(),
                    nullable=True)

    # Index pour recherche rapide par provider + provider_id
    op.create_index('idx_users_oauth', 'users', ['auth_provider', 'provider_id'])


def downgrade() -> None:
    # Supprimer l'index
    op.drop_index('idx_users_oauth', 'users')

    # Supprimer les colonnes OAuth
    op.drop_column('users', 'provider_id')
    op.drop_column('users', 'auth_provider')

    # Remettre hashed_password NOT NULL (attention: peut échouer si des users OAuth existent)
    op.alter_column('users', 'hashed_password',
                    existing_type=sa.String(),
                    nullable=False)
