import argparse
import sqlite3
from datetime import datetime
import pandas as pd
import praw
from rich import inspect, print
from rich.traceback import install
from utils import cmd, fetchall_dict

install()

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

con = sqlite3.connect("./reddit.db")
con.row_factory = sqlite3.Row

reddit = praw.Reddit("bot1")
reddit.read_only = True


# reddit.subreddit("all").new()

for submission in reddit.front.hot(limit=2):
    result = dict(
        date=datetime.utcfromtimestamp(submission.created_utc),
        url=submission.url,
        upvote_ratio=submission.upvote_ratio,
        score=submission.score,
        is_self=submission.is_self,
    )

    print(result)

    fetchall_dict("select filename from videos")

    pd.DataFrame([result]).to_sql(
        "videos",
        con=con,
        if_exists="append",
        index=False,
        chunksize=70,
        method="multi",
    )
