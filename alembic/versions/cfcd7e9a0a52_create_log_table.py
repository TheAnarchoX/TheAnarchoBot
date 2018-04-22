"""create log table

Revision ID: cfcd7e9a0a52
Revises: 32e6169c386c
Create Date: 2018-04-13 10:58:50.360273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfcd7e9a0a52'
down_revision = 'e1a73809114b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'logs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('log_name', sa.VARCHAR(64), nullable=False, default="main-log"),
        sa.Column('title', sa.VARCHAR(512), nullable=False),
        sa.Column('description', sa.VARCHAR(2048), nullable=False),
        sa.Column('action', sa.VARCHAR(256), nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False)
    )


def downgrade():
    pass
