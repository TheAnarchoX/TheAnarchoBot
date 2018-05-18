#!/usr/bin/python
import urllib3

__author__ = "TheAnarchoX"

# DO ALL THE IMPORTS
from _pickle import load, dump
import os
import sys
import time as t
import configparser
import praw
from praw.exceptions import APIException
import atexit
import platform
import datetime
from data.engine import  DB
import sqlalchemy
import json


class BgColors:
    HEADER = '\033[95m'
    MESSAGE = '\033[96m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


at = atexit._clear()
config = configparser.ConfigParser()
config.read('config.ini')

SEEN_SUBMISSIONS = set()
SEEN_COMMENTS = set()

if os.path.exists(config['Bot']['BOT_PICKLE_FILE_SUBMISSIONS']):
    with open(config['Bot']['BOT_PICKLE_FILE_SUBMISSIONS'], "rb") as data_file:
        SEEN_SUBMISSIONS = load(data_file)

if os.path.exists(config['Bot']['BOT_PICKLE_FILE_COMMENTS']):
    with open(config['Bot']['BOT_PICKLE_FILE_COMMENTS'], "rb") as data_file:
        SEEN_COMMENTS = load(data_file)


def check_connection():
    try:
        http = urllib3.PoolManager()
        r = http.request('get', 'http://216.58.192.142')
        if(r.status == 200):
            return True
        else:
            raise urllib3.exceptions.HTTPError
    except urllib3.exceptions.HTTPError as err:
        return False

@atexit.register
def save_seen_submissions():
    with open(config['Bot']['BOT_PICKLE_FILE_SUBMISSIONS'], "wb") as f:
        dump(SEEN_SUBMISSIONS, f)

@atexit.register
def save_seen_comments():
    with open(config['Bot']['BOT_PICKLE_FILE_COMMENTS'], "wb") as f:
        dump(SEEN_COMMENTS, f)


def log_comment(comment):
  if(config['Log']['LOG_CHANNEL'] == "File"):
      loc = config['File']['FILE_LOCATION'] + f"LOG_COMMENTS_{t.strftime('%Y_%m_%d')}.txt"
      entry = f"[{t.strftime('%H:%M:%S')}] Comment: {comment.id} by {comment.author} : {comment.body} posted to submission: {comment.submission.title}\n"
      e = bytearray()
      e.extend(entry.encode())
      with open(loc, "a+b") as f:
          f.write(e)

def log_submission(submission):
    if(config['Log']['LOG_CHANNEL'] == "File"):
        loc = config['File']['FILE_LOCATION'] + f"LOG_SUBMISSIONS_{t.strftime('%Y_%m_%d')}.txt"
        entry = f"[{t.strftime('%H:%M:%S')}] Submission: {submission.id} by {submission.author} : {submission.title}\n"
        e = bytearray()
        e.extend(entry.encode())
        with open(loc, "a+b") as f:
            f.write(e)


def store_submission(submission):
    db =  DB()
    print(db)
    return


def process_submission(submission):
    print(f"{BgColors.FAIL}#{BgColors.ENDC}" * 165)
    print(f"{BgColors.MESSAGE}Submission:{BgColors.ENDC}")
    print(f"{BgColors.FAIL}#{BgColors.ENDC}" * 165)
    if submission.id in SEEN_SUBMISSIONS or submission.stickied:
        if submission.id in SEEN_SUBMISSIONS:
            print(f"{BgColors.WARNING}Submission with ID {submission.id} already processed {BgColors.ENDC}")
        elif submission.stickied:
            print(
                f"{BgColors.WARNING}Submission with ID {submission.id} is stickied and will not be processed {BgColors.ENDC}")
        return
    else:
        SEEN_SUBMISSIONS.add(submission.id)
        log_submission(submission)
        print(f"{BgColors.OKGREEN}Submission Permalink: {BgColors.ENDC}{BgColors.MESSAGE} https://reddit.com{submission.permalink}")
        print(f"{BgColors.OKGREEN}Submission Name: {BgColors.ENDC}{BgColors.MESSAGE} {submission.name}")
        print(f"{BgColors.OKGREEN}Submission ID: {BgColors.ENDC}{BgColors.MESSAGE} {submission.id}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Submission Subreddit: {BgColors.ENDC}{BgColors.MESSAGE} {submission.subreddit} (https://reddit.com/r/{submission.subreddit}) {BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Submission Title: {BgColors.ENDC}{BgColors.MESSAGE} {submission.title}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Submission Created At: {BgColors.ENDC}{BgColors.MESSAGE} {datetime.datetime.fromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Submission Score: {BgColors.ENDC}{BgColors.MESSAGE} {submission.score}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Submission Upvotes: {BgColors.ENDC}{BgColors.MESSAGE} {submission.ups}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Submission Downvotes: {BgColors.ENDC}{BgColors.MESSAGE} {submission.downs}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Submission Author: {BgColors.ENDC}{BgColors.MESSAGE} {submission.author}  (https://reddit.com/user/{submission.author}){BgColors.ENDC}")
        if submission.is_self:
            print(
                f"{BgColors.OKGREEN}Submission Content: \n{BgColors.ENDC}{BgColors.MESSAGE} {submission.selftext}{BgColors.ENDC}")
        else:
            print(
                f"{BgColors.OKGREEN}Submission URL: \n{BgColors.ENDC}{BgColors.MESSAGE} {submission.url}{BgColors.ENDC}")
        store_submission(submission)


def store_comment(comment):

    return


def process_comment(comment, count):
    print(f"{BgColors.FAIL}#{BgColors.ENDC}" * 165)
    print(f"{BgColors.MESSAGE}Comment:{BgColors.ENDC}")
    print(f"{BgColors.MESSAGE}Total Comments Processed: {count} {BgColors.ENDC}")
    print(f"{BgColors.FAIL}#{BgColors.ENDC}" * 165)
    if comment.id in SEEN_COMMENTS or comment.stickied:
        if comment.id in SEEN_COMMENTS:
            print(f"{BgColors.WARNING}Comment with ID {comment.id} already processed{BgColors.ENDC}")
        elif comment.stickied:
            print(
                f"{BgColors.WARNING}Comment with ID {comment.id} is stickied and will not be processed{BgColors.ENDC}")
        return
    else:
        SEEN_COMMENTS.add(comment.id)
        log_comment(comment)
        print(f"{BgColors.OKGREEN}Comment Permalink: {BgColors.ENDC}{BgColors.MESSAGE}https://reddit.com{comment.permalink}{BgColors.ENDC}")
        print(f"{BgColors.OKGREEN}Comment Name: {BgColors.ENDC}{BgColors.MESSAGE}{comment.name}{BgColors.ENDC}")
        print(f"{BgColors.OKGREEN}Comment ID: {BgColors.ENDC}{BgColors.MESSAGE}{comment.id}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Comment Subreddit:{BgColors.ENDC}{BgColors.MESSAGE} {comment.subreddit} (https://reddit.com/r/{comment.subreddit}){BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Comment Created At: {BgColors.ENDC}{BgColors.MESSAGE}{datetime.datetime.fromtimestamp(int(comment.created_utc)).strftime('%Y-%m-%d %H:%M:%S')}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Comment Parent Submission ID:{BgColors.ENDC}{BgColors.MESSAGE} {comment.submission.id}{BgColors.ENDC}")
        print(
            f"{BgColors.OKGREEN}Comment Parent Submission Title: {BgColors.ENDC}{BgColors.MESSAGE}{comment.submission.title}{BgColors.ENDC}")
        print(f"{BgColors.OKGREEN}Comment Score:{BgColors.ENDC}{BgColors.MESSAGE} {comment.score}{BgColors.ENDC}")
        print(f"{BgColors.OKGREEN}Comment Upvotes:{BgColors.ENDC}{BgColors.MESSAGE} {comment.ups}{BgColors.ENDC}")
        print(f"{BgColors.OKGREEN}Comment Downvotes:{BgColors.ENDC}{BgColors.MESSAGE} {comment.downs}{BgColors.ENDC}")
        print(f"{BgColors.OKGREEN}Comment Author:{BgColors.ENDC}{BgColors.MESSAGE} {comment.author}  (https://reddit.com/user/{comment.author}) {BgColors.ENDC}")
        print(f"{BgColors.OKGREEN}Comment Body: \n{BgColors.ENDC}{BgColors.MESSAGE} {comment.body}{BgColors.ENDC}")
        print(f"{BgColors.FAIL}#{BgColors.ENDC}" * 165)
        print(f"{BgColors.MESSAGE}Parent Comment:{BgColors.ENDC}")
        print(f"{BgColors.FAIL}#{BgColors.ENDC}" * 165)
        if not comment.is_root:
            print(
                f"{BgColors.OKGREEN}Parent Comment Permalink:{BgColors.ENDC}{BgColors.MESSAGE} https://reddit.com{comment.parent().permalink}{BgColors.ENDC}")
            print(
                f"{BgColors.OKGREEN}Parent Comment Name:{BgColors.ENDC}{BgColors.MESSAGE} {comment.parent().name}{BgColors.ENDC}")
            print(
                f"{BgColors.OKGREEN}Parent Comment ID:{BgColors.ENDC}{BgColors.MESSAGE} {comment.parent().id}{BgColors.ENDC}")
            print(
                f"{BgColors.OKGREEN}Parent Comment Created At:{BgColors.ENDC}{BgColors.MESSAGE} {datetime.datetime.fromtimestamp(int(comment.parent().created_utc)).strftime('%Y-%m-%d %H:%M:%S')}{BgColors.ENDC}")
            print(
                f"{BgColors.OKGREEN}Parent Comment Score: {BgColors.ENDC}{BgColors.MESSAGE} {comment.parent().score}{BgColors.ENDC}")
            print(
                f"{BgColors.OKGREEN}Parent Comment Upvotes:{BgColors.ENDC}{BgColors.MESSAGE} {comment.parent().ups}{BgColors.ENDC}")
            print(
                f"{BgColors.OKGREEN}Parent Comment Downvotes: {BgColors.ENDC}{BgColors.MESSAGE} {comment.parent().downs}{BgColors.ENDC}")
            print(
                f"{BgColors.OKGREEN}Parent Comment Author:{BgColors.ENDC}{BgColors.MESSAGE} {comment.parent().author} (https://reddit.com/user/{comment.parent().author}) {BgColors.ENDC}")
            print(
                f"{BgColors.OKGREEN}Parent Comment Body: \n{BgColors.ENDC}{BgColors.MESSAGE} {comment.parent().body}{BgColors.ENDC}")
        else:
            print(f"{BgColors.MESSAGE}Comment is root comment{BgColors.ENDC}")
        store_comment(comment)
        process_submission(comment.submission)


def praw_connect():
    reddit_config = config['Reddit']
    reddit_user_agent = reddit_config['REDDIT_USER_AGENT']
    reddit_client_id = reddit_config['REDDIT_CLIENT_ID']
    bot_env = config['Bot']['BOT_ENV']

    print(f"{BgColors.MESSAGE}Checking for active internet connection {BgColors.ENDC}")
    if check_connection():
        print(f"{BgColors.OKGREEN}Internet connection active {BgColors.ENDC}")
    else:
        sys.exit(f"{BgColors.FAIL}No active internet connection found, exiting now....{BgColors.MESSAGE}")
    print(f"{BgColors.MESSAGE}Connecting to Reddit.... {BgColors.ENDC}")

    print(f"{BgColors.FAIL}~{BgColors.ENDC}" * 165)
    reddit = praw.Reddit("TheAnarchoBot")
    if reddit:
        print(f"{BgColors.FAIL}{config['Bot']['BOT_NAME']} {BgColors.ENDC}"
              f"{BgColors.MESSAGE}(Version: {BgColors.ENDC}"
              f"{BgColors.FAIL}{config['Bot']['BOT_VERSION']}{BgColors.ENDC}"
              f"{BgColors.MESSAGE}){BgColors.ENDC}{BgColors.OKGREEN} connected to Reddit {BgColors.ENDC}\n"
              f"{BgColors.MESSAGE}Source Code: https://github.com/TheAnarchoX/TheAnarchoBot {BgColors.ENDC}\n"
              f"{BgColors.OKBLUE}USER_AGENT: {BgColors.ENDC}{BgColors.OKGREEN}{reddit_user_agent}{BgColors.ENDC}\n"
              f"{BgColors.OKBLUE}ENV: {BgColors.ENDC}{BgColors.OKGREEN}{bot_env}{BgColors.ENDC}\n"
              f"{BgColors.OKBLUE}CLIENT_ID: {BgColors.ENDC} {BgColors.OKGREEN} {reddit_client_id} {BgColors.ENDC}")
        print(f"{BgColors.OKBLUE}Mode: {BgColors.ENDC} Read-Only") if reddit.read_only else print(
            f"{BgColors.OKBLUE}Mode: {BgColors.ENDC} {BgColors.OKGREEN}Read/Write{BgColors.ENDC}")
        return reddit


def show_info():
    print(f"{BgColors.FAIL}~{BgColors.ENDC}" * 165)
    pmachine = platform.machine()
    pversion = platform.version()
    pplatform = platform.platform()
    psys = platform.system()
    pproc = platform.processor()
    ppy = platform.python_version()
    print(f"{BgColors.OKBLUE}Machine:{BgColors.ENDC} {BgColors.OKGREEN}{pmachine} {BgColors.ENDC}")
    print(f"{BgColors.OKBLUE}Version: {BgColors.ENDC}{BgColors.OKGREEN}{pversion} {BgColors.ENDC}")
    print(f"{BgColors.OKBLUE}Platform: {BgColors.ENDC}{BgColors.OKGREEN}{pplatform} {BgColors.ENDC}")
    print(f"{BgColors.OKBLUE}System:{BgColors.ENDC}{BgColors.OKGREEN} {psys} {BgColors.ENDC}")
    print(f"{BgColors.OKBLUE}Processor: {BgColors.ENDC}{BgColors.OKGREEN}{pproc} {BgColors.ENDC}")
    print(f"{BgColors.OKBLUE}Python Version: {BgColors.ENDC}{BgColors.OKGREEN}{ppy} {BgColors.ENDC}")
    print(f"{BgColors.FAIL}~{BgColors.ENDC}" * 165)


def run():
    show_info()
    reddit = praw_connect()
    subreddit = reddit.subreddit(config['Reddit']['REDDIT_GRAB_SUBREDDIT'])
    count = 0
    print(f"{BgColors.FAIL}~{BgColors.ENDC}" * 165)
    print(f"{BgColors.OKBLUE}Subreddit to process: {BgColors.ENDC}{BgColors.OKGREEN} {subreddit}{BgColors.ENDC}")
    for comment in subreddit.stream.comments():
        try:
            count = count + 1
            process_comment(comment, count)
        except APIException as ex:
            print(ex)
            t.sleep(60)
            continue


if __name__ == "__main__":
    os.system('cls')
    try:
        run()
    except KeyboardInterrupt:
        print(f"{BgColors.MESSAGE}~{BgColors.ENDC}" * 165)
        print(f"{BgColors.FAIL}User interrupted script exiting...{BgColors.ENDC}")
        print(f"{BgColors.MESSAGE}~{BgColors.ENDC}" * 165)
        sys.exit(1)
