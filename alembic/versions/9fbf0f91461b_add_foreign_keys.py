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
        "submissions", ["submission_id"], ["id"], ondelete="CASCADE")
    op.create_foreign_key(
        "fk_comment_author", "comments",
        "redditors", ["author_id"], ["id"], ondelete="CASCADE")
    op.create_foreign_key(
        "fk_comment_parent", "comments",
        "comments", ["parent_id"], ["id"], ondelete="CASCADE")
    op.create_foreign_key(
        "fk_submission_author", "submissions",
        "redditors", ["author_id"], ["id"], ondelete="CASCADE")
    op.create_foreign_key(
        "fk_submission_subreddit", "submissions",
        "subreddits", ["subreddit_id"], ["id"], ondelete="CASCADE")
    op.create_foreign_key(
        "fk_bot_reply_parent", "bot_replies",
        "comments", ["parent_id"], ["id"], ondelete="CASCADE")
    op.create_foreign_key(
        "fk_bot_reply_submission", "bot_replies",
        "submissions", ["submission_id"], ["id"], ondelete="CASCADE")

def downgrade():
    op.drop_constraint('fk_comment_submission', 'comments', type_='foreignkey')
    op.drop_constraint('fk_comment_author', 'comments', type_='foreignkey')
    op.drop_constraint('fk_comment_parent', 'comments', type_='foreignkey')
    op.drop_constraint('fk_submission_author', 'submissions', type_='foreignkey')
    op.drop_constraint('fk_submission_subreddit', 'submissions', type_='foreignkey')
    op.drop_constraint('fk_bot_reply_parent', 'bot_replies', type_='foreignkey')
    op.drop_constraint('fk_bot_reply_submission', 'bot_replies', type_='foreignkey')
