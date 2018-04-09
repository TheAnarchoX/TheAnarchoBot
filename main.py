#!/usr/bin/python

__author__ = "TheAnarchoX"
# DO ALL THE IMPORTS
import _pickle as cPickle
import os
import time as t
import configparser
import praw
from praw.exceptions import APIException
import atexit
import sqlalchemy
import alembic
at = atexit._clear()
config = configparser.ConfigParser()
config.read('config.ini')

SEEN_POSTS = set()

if os.path.exists(config['Bot']['BOT_PICKLE_FILE']):
    with open(config['Bot']['BOT_PICKLE_FILE'], "rb") as data_file:
        SEEN_POSTS = cPickle.load(data_file)


# @atexit.register
def save_seen_posts():
    if config['Test']['DELETE_PICKLE_FILE'] and os.path.exists(config['Bot']['BOT_PICKLE_FILE']):
        try:
            try:
                os.remove(config['Test']['DELETE_PICKLE_FILE'])
            except OSError:
                pass
        except Exception as ex:
            print(ex)
            exit(1)
    with open(config['Bot']['BOT_PICKLE_FILE'], "wb") as f:
        cPickle.dump(SEEN_POSTS, f)


def process_submission(submission, reddit):
    if submission.id in SEEN_POSTS or submission.stickied:
        return
    else:
        SEEN_POSTS.add(submission.id)
        print("#" * 30)
        print(f"Submission: {submission.name}")
        print(f"ID: {submission.id}")
        print(f"Author: {submission.author}")
        print(f"Title: {submission.title}")
        if submission.is_self:
            print(f"Content: {submission.selftext}")
        else:
            print(f"URL: {submission.url}")
        for x in range(1, 100):
            submission.reply(f"Useful comment {x}")


def praw_connect():
    reddit_config = config['Reddit']
    reddit_user_agent = reddit_config['REDDIT_USER_AGENT']
    reddit_client_id = reddit_config['REDDIT_CLIENT_ID']

    reddit = praw.Reddit("TheAnarchoBot")
    if reddit:
        print(f"{config['Bot']['BOT_NAME']} (Version: {config['Bot']['BOT_VERSION']}) connected to Reddit \n"
              f"USER_AGENT =  {reddit_user_agent}\n"
              f"CLIENT_ID = {reddit_client_id}")
        print("Mode = Read-Only") if reddit.read_only else print("Mode = Read/Write")
        return reddit


def run():
    reddit = praw_connect()
    subreddit = reddit.subreddit(config['Reddit']['REDDIT_GRAB_SUBREDDIT'])
    for submission in subreddit.hot(limit=int(config['Reddit']['REDDIT_REQUEST_LIMIT'])):
        try:
            process_submission(submission, reddit)
        except APIException as ex:
            print(ex)
            t.sleep(60)
            continue


if __name__ == "__main__":
    os.system('cls')
    run()
