import praw
from pprint import *
import time

#User agent name in accordance with Reddit API
user_agent = "User-Agent: Crawl /r/gardening test v1 by /u/comtb"

r = praw.Reddit(user_agent=user_agent)

#set username, can also include password
r.login(username='comtb')

#input favorite reddit subs here
favorites = ['gardening', 'mtb', 'Diablo3']

#loop until keyboard inturrupt
while True:
	#Go through each subreddit in favorites and get the top 5 submissions under hot, can change to new
	for sub in favorites:
		subreddit = r.get_subreddit(sub)
		for submission in subreddit.get_hot(limit = 5):
			print subreddit
			print submission.title
			print submission.url
	#wait time in accordance with Reddit API
	time.sleep(1800)