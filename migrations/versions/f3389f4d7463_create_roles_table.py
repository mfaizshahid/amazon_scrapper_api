"""create roles table

Revision ID: f3389f4d7463
Revises: cba2aa333e96
Create Date: 2023-07-15 17:20:33.128289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3389f4d7463'
down_revision = 'cba2aa333e96'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table("roles",
                    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True,
                              server_default=sa.text("uuid_generate_v4()")),
                    sa.Column("name", sa.String(255), nullable=False),
                    sa.Column("created_at", sa.DateTime(
                        timezone=False), server_default=sa.text('now()'), nullable=False),
                    sa.Column("updated_at", sa.DateTime(
                        timezone=False), onupdate=sa.text('now()')),
                    sa.Column("is_active", sa.Boolean(),
                              server_default="t", nullable=False),
                    )


def downgrade() -> None:
    op.drop_table("roles")
