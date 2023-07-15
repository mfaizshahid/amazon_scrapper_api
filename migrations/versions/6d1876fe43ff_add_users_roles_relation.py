"""add users_roles relation

Revision ID: 6d1876fe43ff
Revises: f3389f4d7463
Create Date: 2023-07-15 17:24:56.223579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d1876fe43ff'
down_revision = 'f3389f4d7463'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users',
                  sa.Column('role_id', sa.UUID(as_uuid=True), sa.ForeignKey('roles.id'), nullable=False))


def downgrade() -> None:
    op.drop_column('users', 'role_id')
