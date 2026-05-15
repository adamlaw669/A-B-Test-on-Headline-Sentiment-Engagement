# importing the necessary libraries
import os
from pathlib import Path

import pandas as pd
import praw
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_ENV_PATH = PROJECT_ROOT / "data.env"
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_CSV = DATA_DIR / "apple_posts.csv"


def get_reddit_client():
    load_dotenv(dotenv_path=DATA_ENV_PATH)  # Load environment variables from .env file
    client_secret = os.environ.get('client_secret') #getting my secret from the .env file
    client_id = os.environ.get('client_id') #getting my id from the .env file

    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent='A/B test',
    )


def fetch_posts(reddit, subreddit_name='apple', limit=1000):
    # pulling the data from the reddit
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.top(limit=limit):
        posts.append(
            {
                'title': post.title,
                'score': post.score,
                'score_ratio': post.upvote_ratio,
                'spoiler': post.spoiler,
                'over_18': post.over_18,
                'self_post': post.is_self,
                'edited': post.edited,
                'locked': post.locked,
                'num_comments': post.num_comments,
                'created_utc': post.created_utc,
                'url': post.url,
                'id': post.id,
                'author': post.author.name if post.author else None,
            }
        )
    return posts


#defining a function to create the dataframe
def create_df(posts):
    df = pd.DataFrame(posts)
    df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
    df['day'] = df['created_utc'].dt.date
    df['hour'] = df['created_utc'].dt.hour
    df.sort_values(by='day', ascending=False, inplace=True)
    return df


def main():
    reddit = get_reddit_client()
    posts = fetch_posts(reddit)
    df = create_df(posts)

    #Storing the dataframe to a csv file to avoid making to many api calls
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)


if __name__ == '__main__':
    main()
