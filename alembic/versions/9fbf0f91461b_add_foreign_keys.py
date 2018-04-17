"""add foreign keys

Revision ID: 9fbf0f91461b
Revises: cfcd7e9a0a52
Create Date: 2018-04-13 12:56:50.622799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fbf0f91461b'
down_revision = 'cfcd7e9a0a52'
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key(
        "fk_comment_submission", "comments",
        "submissions", ["submission_id"], ["id"])
    op.create_foreign_key(
        "fk_comment_author", "comments",
        "redditors", ["author_id"], ["id"])
    op.create_foreign_key(
        "fk_comment_parent", "comments",
        "comments", ["parent_id"], ["id"])
    op.create_foreign_key(
        "fk_submission_author", "submissions",
        "redditors", ["author_id"], ["id"])
    op.create_foreign_key(
        "fk_submission_subreddit", "submissions",
        "subreddit", ["subreddit_id"], ["id"])

def downgrade():
    pass
