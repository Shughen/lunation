"""add users.dev_external_id

Revision ID: 63651f3982e9
Revises: 9737ece7c259
Create Date: 2026-01-04 00:28:37.834010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63651f3982e9'
down_revision = '9737ece7c259'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add dev_external_id column to users table
    op.add_column("users", sa.Column("dev_external_id", sa.String(), nullable=True))
    
    # Create unique constraint
    op.create_unique_constraint("uq_users_dev_external_id", "users", ["dev_external_id"])
    
    # Create index (non-unique, as unique constraint already provides uniqueness)
    op.create_index("ix_users_dev_external_id", "users", ["dev_external_id"], unique=False)


def downgrade() -> None:
    # Drop index
    op.drop_index("ix_users_dev_external_id", table_name="users")
    
    # Drop unique constraint
    op.drop_constraint("uq_users_dev_external_id", "users", type_="unique")
    
    # Drop column
    op.drop_column("users", "dev_external_id")

