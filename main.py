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
import platform
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


def process_submission(submission):
    if submission.id in SEEN_POSTS or submission.stickied:
        return
    else:
        SEEN_POSTS.add(submission.id)
        print("#" * 200)
        print(f"Submission: {submission.name}")
        print(f"ID: {submission.id}")
        print(f"Author: {submission.author}")
        print(f"Title: {submission.title}")
        if submission.is_self:
            print(f"Content: {submission.selftext}")
        else:
            print(f"URL: {submission.url}")
        print("Comments:")
        for comment in submission.comments():
            print(f"Comment: {comment.name}")
            print(f"ID: {comment.id}")
            print(f"Author: {comment.author}")
            print(f"Body: {comment.body}")


def praw_connect():
    reddit_config = config['Reddit']
    reddit_user_agent = reddit_config['REDDIT_USER_AGENT']
    reddit_client_id = reddit_config['REDDIT_CLIENT_ID']

    print("Connecting to Reddit....")
    reddit = praw.Reddit("TheAnarchoBot")
    if reddit:
        print(f"{config['Bot']['BOT_NAME']} (Version: {config['Bot']['BOT_VERSION']}) connected to Reddit \n"
              f"USER_AGENT =  {reddit_user_agent}\n"
              f"CLIENT_ID = {reddit_client_id}")
        print("Mode = Read-Only") if reddit.read_only else print("Mode = Read/Write")
        return reddit

def show_info():
    pmachine = platform.machine()
    pversion = platform.version()
    pplatform = platform.platform()
    psys = platform.system()
    pproc = platform.processor()
    ppy = platform.python_version()
    print(f"Machine: {pmachine}")
    print(f"Version: {pversion}")
    print(f"Platform: {pplatform}")
    print(f"System: {psys}")
    print(f"Processor: {pproc}")
    print(f"Python Version: {ppy}")

def run():
    show_info()
    reddit = praw_connect()
    subreddit = reddit.subreddit(config['Reddit']['REDDIT_GRAB_SUBREDDIT'])
    print(f"Subreddit to process: {subreddit}")
    for submission in subreddit.stream.submissions():
        try:
            process_submission(submission)
        except APIException as ex:
            print(ex)
            t.sleep(60)
            continue


if __name__ == "__main__":
    os.system('cls')
    run()
