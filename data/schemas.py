from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, Text, String, Boolean, BigInteger, TIMESTAMP
from sqlalchemy.orm import relationship

false, true = False, True
Base = declarative_base()


# The Redditor Class
# class used for storing and returning Redditor information
class Redditor(Base):
    __tablename__ = "redditors"
    id = Column(String, primary_key=True)
    username = Column(String, unique=True)
    permalink = Column(String)
    link_karma = Column(Integer)
    comment_karma = Column(Integer)
    is_employee = Column(Boolean, default=False)
    is_gold = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    created_utc = Column(BigInteger)
    timestamp = Column(TIMESTAMP)


class Subreddit(Base):
    __tablename__ = "subreddits"
    id = Column(String, primary_key=True)
    name = Column(String)
    display_name = Column(String)
    display_name_prefixed = Column(String)
    lang = Column(String)
    public_description = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    permalink = Column(String)
    title = Column(String)
    header_title = Column(String, nullable=True)
    type = Column(String)
    subscribers = Column(BigInteger)
    submission_type = Column(BigInteger)
    audience_target = Column(BigInteger, nullable=True)
    whitelist_status = Column(BigInteger)
    created_utc = Column(BigInteger)
    timestamp = Column(TIMESTAMP)


class Submission(Base):
    __tablename__ = "submissions"
    id = Column(String, primary_key=True)
    name = Column(String)
    subreddit_id = Column(String, ForeignKey("subreddits.id"))
    author_id = Column(String, ForeignKey("redditors.id"))
    permalink = Column(String)
    score = Column(Integer)
    title = Column(String, nullable=True)
    url = Column(String, nullable=True)
    selftext = Column(String, nullable=True)
    created_utc = Column(BigInteger)
    timestamp = Column(TIMESTAMP)

    subreddit = relationship("Subreddit",  back_populates="submissions", cascade="all, delete, delete-orphan")
    author = relationship("Redditor",  back_populates="submissions", cascade="all, delete, delete-orphan")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(String, primary_key=True)
    name = Column(String)
    submission_id = Column(String, ForeignKey('submissions.id'))
    author_id = Column(Integer, ForeignKey('redditors.id'))
    parent_id = Column(Integer, ForeignKey('comments.id'), nullable=True, default=None)
    permalink = Column(String)
    score = Column(Integer)
    body = Column(Text)
    created_utc = Column(BigInteger)
    timestamp = Column(TIMESTAMP)

    submission = relationship("Submission", back_populates="comments", cascade="all, delete, delete-orphan")
    author = relationship("Redditor", back_populates="comments", cascade="all, delete, delete-orphan")
    parent = relationship("Comment", back_populates="comments",  cascade="all, delete, delete-orphan")


class BotReplies(Base):
    id = Column(String)
    name = Column(String)
    submission_id = Column(String, ForeignKey("submission_id"))
    parent_id = Column(String, ForeignKey("parent_id"), nullable=True)
    permalink = Column(String)
    score = Column(Integer)
    body = Column(Text(16384))
    created_utc = Column(BigInteger)
    timestamp = Column(TIMESTAMP)


class Logs(Base):
    __tablename__ = "logs"
    id = Column(Integer, autoincrement=True, primary_key=True)
    log_name = Column(String)
    title = Column(String)
    description = Column(Text)
    action = Column(String)
    timestamp = Column(TIMESTAMP)
