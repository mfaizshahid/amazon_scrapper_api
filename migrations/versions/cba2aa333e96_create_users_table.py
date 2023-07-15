"""create users table

Revision ID: cba2aa333e96
Revises: 
Create Date: 2023-07-15 05:05:17.952897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cba2aa333e96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True,
                              index=True, server_default=sa.text("uuid_generate_v4()")),
                    sa.Column("name", sa.String(255), nullable=False),
                    sa.Column("email", sa.String(255),
                              unique=True, nullable=False),
                    sa.Column("password", sa.String, nullable=False),
                    sa.Column("created_at", sa.DateTime(
                        timezone=False), server_default=sa.text('now()'), nullable=False),
                    sa.Column("updated_at", sa.DateTime(
                        timezone=False), server_default=sa.text('now()')),

                    )


def downgrade() -> None:
    op.drop_table("users")
