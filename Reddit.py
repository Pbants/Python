import praw
from pprint import *
import time

user_agent = "User-Agent: Crawl /r/gardening test v1 by /u/comtb"
r = praw.Reddit(user_agent=user_agent)
r.login(username='comtb')
already_done = []
subreddit = r.get_subreddit('gardening')
while True:
	for submission in subreddit.get_hot(limit = 5):
		print submission.title
		print submission.url
	time.sleep(1800)