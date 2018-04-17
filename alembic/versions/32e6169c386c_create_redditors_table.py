"""create redditors table

Revision ID: 32e6169c386c
Revises: 970eb9928a13
Create Date: 2018-04-13 10:58:03.513554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32e6169c386c'
down_revision = '970eb9928a13'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'redditors',
        sa.Column('id', sa.VARCHAR(512), primary_key=True, nullable=False),
        sa.Column('username', sa.VARCHAR(512), nullable=False),
        sa.Column('permalink', sa.VARCHAR(512), nullable=False),
        sa.Column('link_karma', sa.INTEGER, nullable=False),
        sa.Column('comment_karma', sa.INTEGER, nullable=False),
        sa.Column('is_employee', sa.BOOLEAN, nullable=False),
        sa.Column('is_gold', sa.BOOLEAN, nullable=False),
        sa.Column('is_verified', sa.BOOLEAN, nullable=False),
        sa.Column('created_utc', sa.BigInteger, nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False),
    )


def downgrade():
    op.drop_table('redditors')
