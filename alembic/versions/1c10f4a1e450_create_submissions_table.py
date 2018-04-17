"""create submissions table

Revision ID: 1c10f4a1e450
Revises: fcfb091d62eb
Create Date: 2018-04-13 10:57:48.663694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c10f4a1e450'
down_revision = 'fcfb091d62eb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'submissions',
        sa.Column('id', sa.VARCHAR(32), primary_key=True , nullable=False),
        sa.Column('name', sa.VARCHAR(512), nullable=False),
        sa.Column('subreddit_id', sa.VARCHAR(32),nullable=False),
        sa.Column('author_id', sa.VARCHAR(32), nullable=False),
        sa.Column('permalink', sa.VARCHAR(32), nullable=False),
        sa.Column('url', sa.VARCHAR(32), nullable=True),
        sa.Column('score', sa.Integer, nullable=False),
        sa.Column('title', sa.VARCHAR(512), nullable=False),
        sa.Column('selftext', sa.VARCHAR(16384), nullable=True),
        sa.Column('created_utc', sa.BigInteger, nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False),
    )


def downgrade():
    op.drop_table('submissions')
