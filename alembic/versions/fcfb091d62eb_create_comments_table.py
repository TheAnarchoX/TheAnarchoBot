"""create comments table

Revision ID: fcfb091d62eb
Revises: 
Create Date: 2018-04-13 10:57:41.669211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcfb091d62eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.VARCHAR(32), primary_key=True, nullable=False),
        sa.Column('name', sa.VARCHAR(32), nullable=False),
        sa.Column('submission_id', sa.VARCHAR(32), nullable=False),
        sa.Column('author_id', sa.VARCHAR(32), nullable=False),
        sa.Column('parent_id', sa.VARCHAR(32), nullable=True),
        sa.Column('permalink', sa.VARCHAR(32), nullable=False),
        sa.Column('score', sa.Integer, nullable=False),
        sa.Column('body', sa.VARCHAR(16384), nullable=False),
        sa.Column('created_utc', sa.BigInteger, nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False),
    )

def downgrade():
    op.drop_table('comments')