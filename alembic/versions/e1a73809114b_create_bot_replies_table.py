"""create bot replies table

Revision ID: e1a73809114b
Revises: 
Create Date: 2018-04-13 10:57:41.669211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1a73809114b'
down_revision = '32e6169c386c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'bot_replies',
        sa.Column('id', sa.VARCHAR(32), primary_key=True, nullable=False),
        sa.Column('name', sa.VARCHAR(32), nullable=False),
        sa.Column('submission_id', sa.VARCHAR(32), nullable=False),
        sa.Column('parent_id', sa.VARCHAR(32), nullable=True),
        sa.Column('permalink', sa.VARCHAR(32), nullable=False),
        sa.Column('score', sa.Integer, nullable=False),
        sa.Column('body', sa.VARCHAR(16384), nullable=False),
        sa.Column('created_utc', sa.BigInteger, nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False),
    )

def downgrade():
    op.drop_table('bot_replies')