"""create subreddits table

Revision ID: 970eb9928a13
Revises: 1c10f4a1e450
Create Date: 2018-04-13 10:57:55.334679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '970eb9928a13'
down_revision = '1c10f4a1e450'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'subreddits',
        sa.Column('id', sa.VARCHAR(512), nullable=False, primary_key=True),
        sa.Column('name', sa.VARCHAR(512), nullable=False),
        sa.Column('display_name', sa.VARCHAR(512), nullable=False),
        sa.Column('display_name_prefixed', sa.VARCHAR(512), nullable=False),
        sa.Column('lang', sa.VARCHAR(16), nullable=False),
        sa.Column('public_description', sa.VARCHAR(512), nullable=True),
        sa.Column('description', sa.VARCHAR(512), nullable=True),
        sa.Column('permalink', sa.VARCHAR(512), nullable=False),
        sa.Column('title', sa.VARCHAR(512), nullable=False),
        sa.Column('header_title', sa.VARCHAR(512), nullable=True),
        sa.Column('type', sa.VARCHAR(32), nullable=False),
        sa.Column('subscribers', sa.BigInteger, nullable=False),
        sa.Column('submission_type', sa.BigInteger, nullable=False),
        sa.Column('audience_target', sa.BigInteger, nullable=True),
        sa.Column('whitelist_status', sa.BigInteger, nullable=False),
        sa.Column('created_utc', sa.BigInteger, nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False),
    )


def downgrade():
    op.drop_table('subreddits')
