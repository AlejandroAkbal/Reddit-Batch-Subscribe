import os
from time import sleep

from dotenv import load_dotenv

import praw
from prawcore.exceptions import Forbidden, NotFound


# Load environment variables
load_dotenv()

# Authenticate to reddit
reddit = praw.Reddit(
    user_agent='Python:batch-subscribe-v1:v1',
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD')
)

print('Logged in as %s\n' % reddit.user.me())

# Read file contents and subscribe to everything inside
with open('list.txt', 'r') as f:
    list = f.readlines()
    for subreddit in list:
        try:
            print(f'Subscribing to {subreddit}')
            reddit.subreddit(subreddit).subscribe()

        # Exceptions, you can add more if you wish
        except Forbidden:
            print(f'Subreddit {subreddit} is private/quarantined/banned')

        except NotFound:
            print(f'Subreddit {subreddit} does not exist')

    print('Congratulations, you have subscribed to every subreddit')
    print(exist)                                                                                                                                                                                           ~                                                                                                                                                                                                                  ~                             
