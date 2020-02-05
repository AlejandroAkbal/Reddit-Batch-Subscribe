import os
from time import sleep

import praw
from dotenv import load_dotenv

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
        # sleep(0.1) # Wait some time to not overload reddit # EDIT: already does it by default
        print('Subscribing to', subreddit)
        reddit.subreddit(subreddit).subscribe()

    print('\nCongratulations, you have subscribed to every subreddit!')
